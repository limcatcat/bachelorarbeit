from datasets import load_dataset
from pathlib import Path

def main():

    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    # boolq = load_dataset("google/boolq")
    # boolq["train"].to_json(raw_dir / "boolq_train.jsonl")
    # boolq["validation"].to_json(raw_dir / "boolq_validation.jsonl")

    # gsm8k = load_dataset("openai/gsm8k", "main")
    # gsm8k["train"].to_json(raw_dir / "gsm8k_train.jsonl")
    # gsm8k["test"].to_json(raw_dir / "gsm8k_test.jsonl")

    strategyqa = load_dataset("ChilleD/StrategyQA")
    strategyqa["train"].to_json(raw_dir / "strategyqa_train.jsonl")
    strategyqa["test"].to_json(raw_dir / "strategyqa_test.jsonl")

if __name__ == "__main__":
    main()