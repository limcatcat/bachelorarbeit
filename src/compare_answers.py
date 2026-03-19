import re
import pandas as pd
from utils import save_jsonl, get_unique_path
import argparse

DELIMITER = "###"

def extract_llm_answer(llm_response: str, variant: str, delimiter: str = DELIMITER) -> str:
    """
    Extract the final answer from llm_response based on the prompt variant.

    AF: answer ### reasoning   -> take part before delimiter
    RF: reasoning ### answer   -> take part after delimiter
    NR: answer only            -> take whole response
    """
    if pd.isna(llm_response) or str(llm_response).strip() == "":
        return ""
    
    text = str(llm_response).strip()

    if variant == "AF":
        if delimiter in text:
            return text.split(delimiter, 1)[0].strip()
        return text.strip()
        
    if variant == "RF":
        if delimiter in text:
            return text.split(delimiter, 1)[1].strip()
        return text.strip()
    
    if variant == "NR":
        return text.strip()
    
    raise ValueError(f"Unknown variant: {variant}")


def normalize_answer(answer: str) -> str:
    """
    Normalize answers for comparison.
    - strip whitespace
    - lowercase
    - collapse repeated spaces
    - remove surrounding punctuation/newlines
    - normalize simple numeric formats like '36.0' -> '36'
    """

    if pd.isna(answer) or str(answer).strip() == "":
        return ""
    
    text = str(answer).strip().lower()
    text = re.sub(r"\s+", " ", text)

    # Remove surrounding punctuation/spaces
    text = text.strip(" \n\r\t.,;:!?\"'`()[]{}")

    # Normalize numbers like 52.0 -> 52
    if re.fullmatch(r"-?\d+(\.\d+)?", text):
        num = float(text)
        if num.is_integer():
            return str(int(num))
        return str(num)

    return text


def compare_answers(expected_answer: str, llm_answer: str) -> bool:
    return normalize_answer(expected_answer) == normalize_answer(llm_answer)


def add_answer_comparison_to_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a new dataframe with:
    - llm_answer
    - answer_match
    and saves both CSV and JSONL outputs.
    """
    required_cols = {"id", "dataset", "variant", "model_name", "context", "question", "expected_answer", "llm_response"}
    missing = required_cols - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    result_df = df.copy()

    result_df["llm_answer"] = result_df.apply(
        lambda row: extract_llm_answer(row["llm_response"], row["variant"]),
        axis=1,
    )

    result_df["answer_match"] = result_df.apply(
        lambda row: compare_answers(row["expected_answer"], row["llm_answer"]),
        axis=1,
    )

    if result_df.empty:
        raise ValueError("The dataframe is empty.")

    variant = str(result_df.iloc[0]["variant"])
    dataset_name = str(result_df.iloc[0]["dataset"])
    model_name_clean = str(result_df.iloc[0]["model_name"]).replace("/", "_")

    csv_path = get_unique_path(f"comparisons/tables/{variant}_{dataset_name}_{model_name_clean}_comparison.csv")
    jsonl_path = get_unique_path(f"comparisons/raw_comparisons/{variant}_{dataset_name}_{model_name_clean}_comparison.jsonl")

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)

    result_df.to_csv(csv_path, index=False)
    save_jsonl(jsonl_path, result_df.to_dict(orient="records"))

    print(f"Saved CSV to {csv_path}")
    print(f"Saved JSONL to {jsonl_path}")

    return result_df


def main():
    parser = argparse.ArgumentParser(description="Compare the LLM-generated answers to the expected answers")
    parser.add_argument("--csv_path", required=True, help="Path to the CSV file containing LLM responses")

    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    comparison_df = add_answer_comparison_to_df(df)

    print("=== Comparison completed ===")
    print(comparison_df[["expected_answer", "llm_answer", "answer_match"]].head())


if __name__ == "__main__":
    main()