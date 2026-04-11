from __future__ import annotations

import csv
import io
import re
from pathlib import Path
from typing import Any

from wes_structured_logs._common import parse_snakemake_bracket_timestamp, structured_content, structured_line

_RULE_LINE = re.compile(r"^rule\s+(\S+)\s*:\s*$")


def parse_snakemake_run_log_text(text: str, *, name: str | None = None) -> dict[str, Any]:
    """Parse Snakemake workflow log text (e.g. under ``.snakemake/log/``) into WES ``Log`` fields."""
    lines_out: list[dict[str, Any]] = []
    current_ts: str | None = None
    current_rule: str | None = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        ts = parse_snakemake_bracket_timestamp(line)
        if ts is not None:
            current_ts = ts
            lines_out.append(structured_line(line, ts=ts, level="INFO"))
            continue
        rm = _RULE_LINE.match(line.strip())
        if rm:
            current_rule = rm.group(1)
            lines_out.append(structured_line(line, ts=current_ts, level="INFO"))
            continue
        if line.startswith("Finished jobid:") or line.startswith("Error in rule"):
            lvl = "ERROR" if "Error" in line else "INFO"
            lines_out.append(structured_line(line, ts=current_ts, level=lvl))
            continue
        lines_out.append(structured_line(line, ts=current_ts))

    meta: dict[str, Any] = {"engine": "snakemake"}
    if current_rule:
        meta["last_rule"] = current_rule

    out: dict[str, Any] = {
        "structured_stdout": structured_content(lines_out, content_encoding="utf-8"),
        "engine_metadata": meta,
    }
    if name is not None:
        out["name"] = name
    return out


def _float_or_none(s: str) -> float | None:
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def parse_snakemake_benchmark_tsv(
    path: str | Path | None = None,
    *,
    text: str | None = None,
) -> dict[str, Any]:
    """
    Parse a Snakemake ``benchmark`` TSV into WES ``LogResourceUsage``-shaped dict.

    Snakemake benchmark columns commonly include ``s`` (wall seconds), ``cpu_time``, ``max_rss`` (MB).
    """
    if (path is None) == (text is None):
        raise ValueError("Provide exactly one of path= or text=")
    raw = text if text is not None else Path(path).read_text(encoding="utf-8", errors="replace")

    f = io.StringIO(raw)
    reader = csv.DictReader(f, delimiter="\t")
    row = next(reader, None)
    if not row:
        return {}

    usage: dict[str, Any] = {}
    if "s" in row and row["s"]:
        w = _float_or_none(row["s"])
        if w is not None:
            usage["wall_time_seconds"] = w
    if "cpu_time" in row and row["cpu_time"]:
        c = _float_or_none(row["cpu_time"])
        if c is not None:
            usage["cpu_time_seconds"] = c
    if "max_rss" in row and row["max_rss"]:
        v = _float_or_none(row["max_rss"])
        if v is not None:
            # Snakemake records ``max_rss`` in megabytes in recent versions.
            usage["peak_memory_bytes"] = int(v * 1024 * 1024)
    return usage
