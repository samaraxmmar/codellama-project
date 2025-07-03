import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import load_dataset

# 1. Load the dataset
dataset = load_dataset("json", data_files="../../data/processed/code_finetuning_dataset.jsonl")

# 2. Load the CodeLlama tokenizer and model
model_name = "codellama/CodeLlama-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Add a padding token if the tokenizer doesn't have one
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# 3. Prepare the dataset for training
def tokenize_function(examples):
    # Concatenate prompt and completion for causal training
    return tokenizer([f"{p}{c}" for p, c in zip(examples["prompt"], examples["completion"])], truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["prompt", "completion"])

# 4. Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=500,
)

# 5. Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    tokenizer=tokenizer,
)

# 6. Start training
trainer.train()

# 7. Save the fine-tuned model
model.save_pretrained("../../finetuning/models/codellama-finetuned")
tokenizer.save_pretrained("../../finetuning/models/codellama-finetuned")


