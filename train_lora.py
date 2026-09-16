import json
import torch

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from peft import LoraConfig, get_peft_model


# ==========================================
# 1. CONFIGURATION
# ==========================================

MODEL_NAME = "HuggingFaceTB/SmolLM2-135M"

TRAIN_FILE = "data/train.json"

OUTPUT_DIR = "lora_adapter"


# ==========================================
# 2. LOAD TRAINING DATA
# ==========================================

print("Loading training data...")

with open(TRAIN_FILE, "r", encoding="utf-8") as f:
    training_data = json.load(f)

print(f"Training examples: {len(training_data)}")


# ==========================================
# 3. CONVERT DATA INTO TEXT
# ==========================================

formatted_data = []

for item in training_data:

    text = (
        f"Question: {item['question']}\n"
        f"Answer: {item['answer']}"
    )

    formatted_data.append({
        "text": text
    })


dataset = Dataset.from_list(formatted_data)

print("Dataset prepared.")


# ==========================================
# 4. LOAD TOKENIZER
# ==========================================

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


# ==========================================
# 5. TOKENIZE DATA
# ==========================================

def tokenize_function(examples):

    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=128,
    )


tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=["text"]
)

print("Dataset tokenized.")


# ==========================================
# 6. LOAD BASE MODEL
# ==========================================

print("Loading base model...")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME
)

print("Base model loaded.")


# ==========================================
# 7. CONFIGURE LoRA
# ==========================================

print("Configuring LoRA...")

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
    ],
    bias="none",
    task_type="CAUSAL_LM",
)


# Attach LoRA to the model
model = get_peft_model(
    model,
    lora_config
)


# Show trainable parameters
model.print_trainable_parameters()


# ==========================================
# 8. TRAINING CONFIGURATION
# ==========================================

training_args = TrainingArguments(

    output_dir=OUTPUT_DIR,

    # CPU-friendly settings
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,

    # One pass through the dataset initially
    num_train_epochs=1,

    learning_rate=2e-4,

    logging_steps=10,

    save_strategy="epoch",

    report_to="none",

    # Important for CPU systems
    fp16=False,
    bf16=False,
)


# ==========================================
# 9. DATA COLLATOR
# ==========================================

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)


# ==========================================
# 10. TRAINER
# ==========================================

trainer = Trainer(

    model=model,

    args=training_args,

    train_dataset=tokenized_dataset,

    data_collator=data_collator,
)


# ==========================================
# 11. START TRAINING
# ==========================================

print("\nStarting LoRA fine-tuning...\n")

trainer.train()


# ==========================================
# 12. SAVE LoRA ADAPTER
# ==========================================

print("\nSaving LoRA adapter...")

model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("\nTraining complete!")
print(f"LoRA adapter saved to: {OUTPUT_DIR}")