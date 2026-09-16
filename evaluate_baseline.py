import json
import re
import torch

from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "HuggingFaceTB/SmolLM2-135M"
TEST_FILE = "data/baseline_test.json"
OUTPUT_FILE = "data/baseline_results_final.json"


print("Loading base model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

model.eval()

print("Model loaded.\n")


# -----------------------------
# Normalize text
# -----------------------------

def normalize(text):
    text = text.lower().strip()

    replacements = {
        "common salt": "table salt",
        "m/s": "meters per second",
        "m/sec": "meters per second",
        "cm2": "square centimeters",
        "cm²": "square centimeters",
        "sq cm": "square centimeters",
        "sq. cm": "square centimeters",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove commas inside numbers
    text = re.sub(r"(?<=\d),(?=\d)", "", text)

    # Normalize multiplication symbol
    text = text.replace("×", "x")

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Remove punctuation except useful math symbols
    text = re.sub(r"[^\w\s%+\-=/^x.]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text.rstrip(".")


# -----------------------------
# Extract ONLY the answer
# -----------------------------

def extract_answer(text):

    text = text.strip()

    # If the model generates "Answer:", remove it
    if text.lower().startswith("answer:"):
        text = text.split(":", 1)[1].strip()

    # The model sometimes generates:
    #
    # 50
    # Explanation: ...
    #
    # We only want "50".

    explanation_match = re.search(
        r"\n\s*Explanation\s*:",
        text,
        flags=re.IGNORECASE
    )

    if explanation_match:
        text = text[:explanation_match.start()]

    # Also stop if it starts another question
    stop_patterns = [
        r"\n\s*Question\s*:",
        r"\n\s*Q\s*:",
        r"\n\s*A\s*:",
        r"\n\s*Answer\s*:",
    ]

    for pattern in stop_patterns:
        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:
            text = text[:match.start()]

    # Take only the first non-empty line.
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if lines:
        text = lines[0]

    return text.strip()


# -----------------------------
# Check answer
# -----------------------------

def answers_match(model_answer, expected_answer):

    model_text = normalize(model_answer)
    expected_text = normalize(expected_answer)

    # Exact match
    if model_text == expected_text:
        return True

    # Speed of light equivalents
    speed_answers = {
        "3 x 10^8 meters per second",
        "3 x 10 8 meters per second",
        "300000000 meters per second",
        "299792458 meters per second",
    }

    if expected_text in speed_answers:
        if model_text in speed_answers:
            return True

    # Allow an answer such as:
    # "180"
    # "180 centimeters"
    #
    # but do NOT search inside explanations.

    pattern = r"(?<!\w)" + re.escape(expected_text) + r"(?!\w)"

    if re.search(pattern, model_text):
        return True

    return False


# -----------------------------
# Load test data
# -----------------------------

with open(TEST_FILE, "r", encoding="utf-8") as f:
    test_data = json.load(f)


results = []
correct = 0


# -----------------------------
# Evaluation
# -----------------------------

for i, item in enumerate(test_data, start=1):

    question = item["question"]
    expected = item["ground_truth"]

    prompt = f"Question: {question}\nAnswer:"

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=80,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    # Remove prompt tokens
    generated_tokens = outputs[0][
        inputs["input_ids"].shape[1]:
    ]

    generated_text = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    )

    model_answer = extract_answer(generated_text)

    is_correct = answers_match(
        model_answer,
        expected
    )

    if is_correct:
        correct += 1

    results.append({
        "id": item["id"],
        "category": item["category"],
        "question": question,
        "expected": expected,
        "model_answer": model_answer,
        "correct": is_correct
    })

    print(
        f"{i:02d}. "
        f"Expected: {expected} | "
        f"Model: {model_answer} | "
        f"{'✓' if is_correct else '✗'}"
    )


# -----------------------------
# Save results
# -----------------------------

accuracy = (correct / len(test_data)) * 100

output = {
    "model": MODEL_NAME,
    "type": "baseline",
    "total_questions": len(test_data),
    "correct": correct,
    "accuracy": accuracy,
    "results": results
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(
        output,
        f,
        indent=2,
        ensure_ascii=False
    )


print("\n==============================")
print("BASELINE RESULTS")
print("==============================")
print(f"Total questions: {len(test_data)}")
print(f"Correct: {correct}")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Saved to: {OUTPUT_FILE}")