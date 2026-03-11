import json
import random
import re
from pathlib import Path

SEED = 42
N = 300

def extract_final_answer(answer_text: str) -> str:
    match = re.search(r"####\s*(.*)", answer_text)
    if match:
        return match.group(1).strip()
    return answer_text.strip()

def split_question_and_context(question_text: str):
    sentences = re.split(r'(?<=[.!?])\s+', question_text.strip())

    if len(sentences) == 1:
        return "", sentences[0]
    
    context = " ".join(sentences[:-1])
    question = sentences[-1]

    return context, question

def main():

    raw_path = Path("data/raw/gsm8k_test.jsonl")

    # Load raw gsm8k dataset
    with open(raw_path) as f:
        rows = [json.loads(line) for line in f]

    # Shuffle reproducibly
    random.seed(SEED)
    random.shuffle(rows)

    subset = rows[:N]

    # Normalize schema
    processed = []

    for i, row in enumerate(subset):
        context, question = split_question_and_context(row["question"])
        processed.append({
            "id": f"gsm8k_{i}",
            "dataset": "gsm8k",
            "question": question,
            "context": context,
            "answer": extract_final_answer(row["answer"])
        })

    # Save processed dataset
    output_path = Path("data/processed/gsm8k_test_seed42_n300.jsonl")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        for item in processed:
            f.write(json.dumps(item) + "\n")

if __name__ == "__main__":
    main()