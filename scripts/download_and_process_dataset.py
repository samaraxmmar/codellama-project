from datasets import load_dataset
import json
import os

# Create the directory if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

dataset = load_dataset("samaxr/code-summary-java")

with open("data/processed/code_finetuning_dataset.jsonl", "w") as f:
    for item in dataset["train"]:
        # Ensure 'code' and 'summary' keys exist
        if "code" in item and "summary" in item:
            f.write(json.dumps({"prompt": item["code"], "completion": item["summary"]}) + "\n")
        else:
            print(f"Skipping item due to missing 'code' or 'summary' key: {item}")


