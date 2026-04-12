import json
import random
from pathlib import Path

SEED = 42
N = 300
SPLIT = "test"

QUESTION = "What is the fine-grained user intent (subflow label) for this customer service conversation?"


def format_original_turns(original: list) -> str:
    lines = []
    for speaker, text in original:
        role = str(speaker).strip().lower()
        if role == "agent":
            label = "Agent"
        elif role == "customer":
            label = "Customer"
        else:
            label = "Action"
        lines.append(f"{label}: {text}")
    return "\n".join(lines)


def main():

    raw_path = Path("data/raw/abcd_v1.1.json")

    # Load raw abcd dataset
    with open(raw_path, encoding="utf-8") as f:
        data = json.load(f)

    if SPLIT not in data:
        raise KeyError(f"Split {SPLIT!r} not in {raw_path}; keys: {list(data.keys())}")

    rows = data[SPLIT]

    # Shuffle reproducibly
    random.seed(SEED)
    random.shuffle(rows)

    subset = rows[:N]

    # Normalize schema
    processed = []

    for i, convo in enumerate(subset):
        scenario = convo["scenario"]
        subflow = scenario["subflow"]
        processed.append({
            "id": f"abcd_{i}",
            "dataset": "abcd",
            "question": QUESTION,
            "context": format_original_turns(convo["original"]),
            "answer": subflow,
        })

    # Save processed dataset
    output_path = Path(f"data/processed/abcd_{SPLIT}_seed42_n{N}.jsonl")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for item in processed:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
