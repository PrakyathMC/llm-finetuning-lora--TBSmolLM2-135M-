
# LLM Fine-Tuning with LoRA

A practical experiment exploring **LoRA (Low-Rank Adaptation)** for fine-tuning a small causal language model on educational question-answering tasks.

The project focuses on building a reproducible workflow for:

**Base Model → Baseline Evaluation → LoRA Fine-Tuning → Evaluation → Comparison**

---

## Model

**Base model:** `HuggingFaceTB/SmolLM2-135M`

SmolLM2-135M is a small causal language model used here to experiment with parameter-efficient fine-tuning on a local machine.

---

## Objective

The goal of this experiment was to determine whether LoRA fine-tuning could improve the model's ability to answer basic educational questions across subjects such as:

* Mathematics
* Chemistry
* Biology
* General Science

Rather than assuming that fine-tuning would improve performance, the experiment uses a locked evaluation set to measure the actual change.

---

## Dataset

### Training Dataset

The training dataset contains **223 question-answer examples** covering educational topics.

Each training example follows the structure:

```json
{
  "id": 1,
  "category": "Mathematics",
  "question": "What is 7 multiplied by 8?",
  "answer": "56"
}
```

### Evaluation Dataset

The evaluation set contains **30 held-out questions**.

The test questions are kept separate from the training data to measure performance on questions the model did not train on.

Example:

```json
{
  "id": 1,
  "category": "Mathematics",
  "question": "What is 15 multiplied by 12?",
  "ground_truth": "180"
}
```

---

## Baseline Evaluation

Before fine-tuning, the base SmolLM2-135M model was evaluated on the locked 30-question test set.

### Baseline Result

**18 / 30 correct**

**Accuracy: 60%**

This establishes the reference point against which the LoRA model is compared.

---

## LoRA Fine-Tuning

The model was fine-tuned using **LoRA (Low-Rank Adaptation)** through the PEFT library.

Instead of updating all model parameters, LoRA introduces trainable low-rank adapter parameters into selected transformer layers while keeping the original model weights frozen.

For this experiment:

* Training examples: **223**
* Epochs: **1**
* Trainable parameters: **921,600**
* Total model parameters: **135,436,608**
* Trainable parameter percentage: **0.6805%**

The resulting adapter was saved separately in:

```text
lora_adapter/
```

The adapter directory is excluded from Git because it contains generated model artifacts.

---

## Results

The same 30-question evaluation set was used for both models.

| Model             | Correct | Accuracy |
| ----------------- | ------: | -------: |
| Base SmolLM2-135M | 18 / 30 |      60% |
| LoRA SmolLM2-135M | 18 / 30 |      60% |

### Result

LoRA produced **no net improvement** on this evaluation set.

Although the LoRA model changed several individual predictions, the number of correct answers remained the same.

This experiment therefore does **not** provide evidence that the current LoRA configuration improved the model's educational QA performance.

---

## What This Experiment Demonstrates

The main purpose of the project is not simply to obtain a higher accuracy number.

It demonstrates a complete fine-tuning workflow:

```text
                ┌─────────────────┐
                │   Base Model    │
                │ SmolLM2-135M    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Baseline     │
                │   Evaluation    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Training Data   │
                │  223 examples   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ LoRA Fine-Tune  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ LoRA Adapter    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Same Test Set   │
                │    30 questions │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Compare Results │
                └─────────────────┘
```

The experiment also demonstrates why a **fixed evaluation set** and a **baseline measurement** are important before judging whether fine-tuning helped.

---

## Project Structure

```text
llm-finetuning-lora-experiment/
│
├── data/
│   ├── train.json
│   ├── baseline_test.json
│   ├── baseline_results_final.json
│   └── lora_results_final.json
│
├── create training data.py
├── download_model.py
├── test_model.py
├── train_lora.py
├── evaluate_baseline.py
├── evaluate_lora.py
├── requirements.txt
├── .gitignore
└── README.md
```

The generated `lora_adapter/` directory is intentionally excluded from version control.

---

## Installation

Create a Python environment and install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Experiment

### 1. Test the base model

```bash
python test_model.py
```

### 2. Run baseline evaluation

```bash
python evaluate_baseline.py
```

### 3. Train the LoRA adapter

```bash
python train_lora.py
```

This creates:

```text
lora_adapter/
```

### 4. Evaluate the LoRA model

```bash
python evaluate_lora.py
```

---

## Current Conclusion

The first LoRA experiment resulted in:

**Base model: 60%**

**LoRA model: 60%**

The current configuration therefore did not demonstrate measurable improvement on the 30-question held-out evaluation set.

This provides a baseline for future experiments involving changes to training data, LoRA configuration, training duration, prompting, evaluation methodology, or model selection.

---

## Technologies

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face PEFT
* LoRA
* SmolLM2
* JSON-based datasets
* Local model inference and fine-tuning
