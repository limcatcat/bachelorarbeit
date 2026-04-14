import pandas as pd
import re
import argparse
from pathlib import Path


# Matches:
# _1
# _how_1
# _other_1
# _how
# _other
_ABCD_SUFFIX = re.compile(r"(?:_(?:how|other)(?:_\d+)?|_\d+)$")


def strip_suffix(label: str) -> str:
    """Remove _digit, _how_digit, _other_digit suffixes."""
    return _ABCD_SUFFIX.sub("", label.strip())


def clean_expected_answer(text: str) -> str:
    """
    Cleans expected_answer:
    - handles both "flow: subflow" and single labels
    """
    if pd.isna(text) or str(text).strip() == "":
        return ""

    text = str(text).strip()

    if ":" in text:
        flow, sub = text.split(":", 1)
        flow = flow.strip()
        sub = strip_suffix(sub.strip())
        return f"{flow}: {sub}"
    else:
        return strip_suffix(text)


def main():
    parser = argparse.ArgumentParser(description="Clean expected_answer column in CSV")
    parser.add_argument("--input_csv", required=True, help="Path to input CSV")
    parser.add_argument("--output_csv", help="Path to output CSV (optional)")

    args = parser.parse_args()

    input_path = Path(args.input_csv)

    if not input_path.exists():
        raise FileNotFoundError(f"{input_path} not found")

    df = pd.read_csv(input_path)

    if "expected_answer" not in df.columns:
        raise ValueError("Column 'expected_answer' not found in CSV")

    # 1. Rename original column
    df = df.rename(columns={"expected_answer": "expected_answer_suffix"})

    # 2. Create cleaned column with original name
    df["expected_answer"] = df["expected_answer_suffix"].apply(clean_expected_answer)

    # Output path
    if args.output_csv:
        output_path = Path(args.output_csv)
    else:
        output_path = input_path.parent / f"{input_path.stem}_cleaned.csv"

    df.to_csv(output_path, index=False)

    print(f"Saved cleaned CSV to: {output_path}")

    # Show sample
    print("\nSample:")
    print(df[["expected_answer_suffix", "expected_answer"]].head(10))


if __name__ == "__main__":
    main()