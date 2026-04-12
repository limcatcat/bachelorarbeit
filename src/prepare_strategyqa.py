import json
import random
from pathlib import Path

SEED = 42
N = 300

def main():

    raw_path = Path("data/raw/strategyqa_test.jsonl")

    # Load raw boolq dataset
    with open(raw_path, encoding="utf-8") as f:
        rows = [json.loads(line) for line in f]

    # Shuffle reproducibly
    random.seed(SEED)
    random.shuffle(rows)

    subset = rows[:N]

    # Normalize schema
    processed = []

    for i, row in enumerate(subset):
        processed.append({
            "id": f"strategyqa_{i}",
            "dataset": "strategyqa",
            "question": row["question"],
            "context": row["facts"],
            "answer": row["answer"]
        })

    # Save processed dataset
    output_path = Path("data/processed/strategyqa_test_seed42_n{N}.jsonl")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for item in processed:
            f.write(json.dumps(item) + "\n")

if __name__ == "__main__":
    main()