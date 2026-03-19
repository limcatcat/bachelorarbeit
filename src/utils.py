import json
from pathlib import Path

def load_jsonl(path: str) -> list[dict]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def save_jsonl(path: str, rows: list[dict]) -> None:
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")

def get_unique_path(path: str) -> Path:
    base_path = Path(path)

    if not base_path.exists():
        return base_path
    
    i = 1
    while True:
        new_path = base_path.with_name(f"{base_path.stem}_{i}{base_path.suffix}")
        if not new_path.exists():
            return new_path
        i += 1
