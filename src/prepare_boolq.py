import json
import random
from pathlib import Path

SEED = 42
N = 300

def main():

    raw_path = Path("data/raw/boolq_validation.jsonl")

    # Load raw boolq dataset
    with open(raw_path) as f:
        rows = [json.loads(line) for line in f]

    # Shuffle reproducibly
    random.seed(SEED)
    random.shuffle(rows)

    subset = rows[:N]

    # Normalize schema
    processed = []

    for i, row in enumerate(subset):
        processed.append({
            "id": f"boolq_{i}",
            "dataset": "boolq",
            "question": row["question"],
            "context": row["passage"],
            "answer": row["answer"]
        })

    # Save processed dataset
    output_path = Path("data/processed/boolq_validation_seed42_n300.jsonl")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        for item in processed:
            f.write(json.dumps(item) + "\n")

if __name__ == "__main__":
    main()