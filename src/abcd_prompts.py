import json
from pathlib import Path

ONTOLOGY_PATH = Path("data/raw/abcd_ontology.json")


def _load_intents_subflows_dict(path: Path) -> dict[str, list[str]]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    raw = data.get("intents", {}).get("subflows")
    if raw is None:
        raw = data.get("subflows")

    if raw is None:
        raise KeyError(
            f"No subflows map found in {path}: expected intents.subflows or top-level subflows"
        )

    if not isinstance(raw, dict):
        raise TypeError(f"intents.subflows must be a dict, got {type(raw)}")

    return {str(flow): [str(s) for s in subs] for flow, subs in raw.items()}


def load_flat_subflows(ontology_path: str) -> tuple[str, ...]:
    """Sorted unique subflow names (ignores which flow they belong to)."""
    path = Path(ontology_path)
    d = _load_intents_subflows_dict(path)
    labels: list[str] = []
    for subs in d.values():
        labels.extend(subs)
    return tuple(sorted(set(labels)))


def iter_sorted_flow_subflow_pairs(ontology_path: str) -> list[tuple[str, str]]:
    """All (flow, subflow) pairs from the ontology, sorted by flow then subflow."""
    path = Path(ontology_path)
    d = _load_intents_subflows_dict(path)
    pairs: list[tuple[str, str]] = []
    for flow in sorted(d.keys()):
        for sub in sorted(d[flow]):
            pairs.append((flow, sub))
    return pairs


def format_subflows_for_prompt(labels: tuple[str, ...] | list[str]) -> str:
    """One subflow per line, prefixed with '-' for readability in the system prompt."""
    seq = list(labels)
    return "\n".join(f"- {s}" for s in seq)


def get_subflows_block(ontology_path: Path | str | None = None) -> str:
    path_str = str(ONTOLOGY_PATH if ontology_path is None else Path(ontology_path))
    return format_subflows_for_prompt(load_flat_subflows(path_str))


def get_flow_subflow_pairs_block(ontology_path: Path | str | None = None) -> str:
    """
    Bullet list of allowed answers, one per line:
      - flow_name: subflow_name
    """
    path_str = str(ONTOLOGY_PATH if ontology_path is None else Path(ontology_path))
    pairs = iter_sorted_flow_subflow_pairs(path_str)
    return "\n".join(f"- {f}: {s}" for f, s in pairs)


ABCD_VARIANT_PROMPT_NAMES = {
    "AF": "abcd/answer_first_system_prompt",
    "RF": "abcd/reasoning_first_system_prompt",
    "NR": "abcd/no_reasoning_system_prompt",
}