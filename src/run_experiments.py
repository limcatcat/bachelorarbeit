from fetch_prompts import fetch_prompts
from langfuse.openai import openai
from langfuse import observe, propagate_attributes
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
import argparse
from utils import load_jsonl, save_jsonl, get_unique_path

load_dotenv()

@observe(name="qa_execution")
def execute_qa(
        row: dict,
        i: int,
        variant: str,
        dataset_name: str,
        model_name: str,
        temperature: float,
        output_name: str,
) -> dict:
       
    VARIANT_DICT = {
        "AF": "answer_first_system_prompt",
        "RF": "reasoning_first_system_prompt",
        "NR": "no_reasoning_system_prompt",
    }
     
    context = row["context"]
    question = row["question"]

    system_prompt, user_prompt = fetch_prompts(
        system_prompt_name=VARIANT_DICT[variant],
        user_prompt_name="user_prompt",
        context=context,
        question=question,
    )

    with propagate_attributes(
        tags=[f"{output_name}"],
        metadata={
            "row_index": str(i),
            "sample_id": row.get("id"),
            "variant": variant,
            "dataset_name": dataset_name,
            "model_name": model_name,
            "temperature": str(temperature),
        },
    ):
        response = openai.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
        )

        llm_response = response.choices[0].message.content

        result_row = {
            "row_index": i,
            "id": row.get("id"),
            "dataset": row.get("dataset"),
            "variant": variant,
            "expected_answer": row.get("answer"),
            "context": context,
            "question": question,
            "system_prompt_name": VARIANT_DICT[variant],
            "user_prompt_name": "user_prompt",
            "model_name": model_name,
            "temperature": temperature,
            "llm_response": llm_response
        }

        return result_row



def run_experiment(
        dataset_path: str,
        variant: str,
        model_name: str,
        temperature: float = 0,
) -> tuple[pd.DataFrame, str]:
        
    data = load_jsonl(dataset_path)

    results = []

    dataset_name = Path(dataset_path).stem.split("_")[0]
    model_name_clean = model_name.replace("/", "_")

    output_name = f"{variant}_{dataset_name}_{model_name_clean}"


    for i, row in enumerate(data):
        result_row = execute_qa(
            row=row,
            i=i,
            variant=variant,
            dataset_name=dataset_name,
            model_name=model_name,
            temperature=temperature,
            output_name=output_name,
        )

        results.append(result_row)

        print(f"Processed row {i+1}/{len(data)}")

    return pd.DataFrame(results), output_name


def main():
    parser = argparse.ArgumentParser(description="Run LLM experiments on a processed dataset.")

    parser.add_argument("--dataset_path", required=True, help="Path to the processed JSONL dataset")
    parser.add_argument("--variant", required=True, help="Prompt variant label, e.g. AF, RF, NR")
    parser.add_argument("--model_name", required=True, help="OpenAI model name")
    parser.add_argument("--temperature", type=float, default=0.0, help="Sampling temperature")

    args = parser.parse_args()

    df, output_name = run_experiment(
        dataset_path=args.dataset_path,
        variant=args.variant,
        model_name=args.model_name,
        temperature=args.temperature,
    )

    Path("results/tables").mkdir(parents=True, exist_ok=True)
    Path("results/raw_runs").mkdir(parents=True, exist_ok=True)

    csv_path = get_unique_path(f"results/tables/{output_name}.csv")
    jsonl_path = get_unique_path(f"results/raw_runs/{output_name}.jsonl")

    df.to_csv(csv_path, index=False)

    records = df.to_dict(orient="records")
    save_jsonl(jsonl_path, records)

    print(f"Saved CSV to {csv_path}")
    print(f"Saved JSONL to {jsonl_path}")

if __name__ == "__main__":
    main()