import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
from torch.utils.data import DataLoader
from tqdm import tqdm

# 1. Load the fine-tuned model and tokenizer
model_path = "../../finetuning/models/codellama-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# 2. Load the evaluation dataset (using the same for example)
dataset = load_dataset("json", data_files="../../data/processed/code_finetuning_dataset.jsonl")

# 3. Prepare the dataset for evaluation
def tokenize_function(examples):
    return tokenizer(examples["prompt"], truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["prompt", "completion"])
tokenized_dataset.set_format(type="torch", columns=["input_ids", "attention_mask"])

# 4. Create a DataLoader
data_loader = DataLoader(tokenized_dataset["train"], batch_size=4)

# 5. Evaluation
model.eval()
predictions = []

with torch.no_grad():
    for batch in tqdm(data_loader):
        outputs = model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            max_length=150, # Increase to allow generation
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
        # Decode predictions
        batch_predictions = [tokenizer.decode(g, skip_special_tokens=True) for g in outputs]
        predictions.extend(batch_predictions)

# 6. Display predictions
for i, prediction in enumerate(predictions):
    print(f"Prompt {i+1}:\n{dataset["train"][i]["prompt"]}")
    print(f"Generated Completion {i+1}:\n{prediction}")
    print("-"*20)


