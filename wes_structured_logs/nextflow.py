from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import Any

from wes_structured_logs._common import parse_nextflow_log_line, structured_content, structured_line

_STATUS_TO_STATE: dict[str, str] = {
    "COMPLETED": "COMPLETE",
    "FAILED": "EXECUTOR_ERROR",
    "ABORTED": "CANCELED",
    "CACHED": "COMPLETE",
}


def parse_nextflow_log_text(text: str, *, year: int | None = None, name: str | None = None) -> dict[str, Any]:
    """Parse a Nextflow ``.nextflow.log``-style text into WES ``Log`` fields."""
    lines_out: list[dict[str, Any]] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        parsed = parse_nextflow_log_line(line, year=year)
        if parsed:
            lines_out.append(parsed)
        else:
            lines_out.append(structured_line(line))

    out: dict[str, Any] = {
        "structured_stdout": structured_content(lines_out, content_encoding="utf-8"),
        "engine_metadata": {"engine": "nextflow", "source": "nextflow.log"},
    }
    if name is not None:
        out["name"] = name
    return out


def parse_nextflow_trace_tsv(
    path: str | Path | None = None,
    *,
    text: str | None = None,
) -> list[dict[str, Any]]:
    """
    Parse Nextflow ``trace.txt`` (tab-separated, header row) into WES ``TaskLog``-shaped dicts.

    Column names follow Nextflow's trace report; unknown columns are ignored.
    """
    if (path is None) == (text is None):
        raise ValueError("Provide exactly one of path= or text=")
    raw = text if text is not None else Path(path).read_text(encoding="utf-8", errors="replace")
    f = io.StringIO(raw)
    reader = csv.DictReader(f, delimiter="\t")
    tasks: list[dict[str, Any]] = []
    for row in reader:
        task_id = (row.get("task_id") or row.get("taskId") or "").strip()
        proc = (row.get("process") or "").strip()
        tag = (row.get("tag") or "").strip()
        native = (row.get("native_id") or "").strip()
        hsh = (row.get("hash") or "").strip()
        name = (row.get("name") or proc or "task").strip()
        status_raw = (row.get("status") or "").strip().upper()
        exit_s = (row.get("exit") or "").strip()

        tl: dict[str, Any] = {
            "id": task_id or native or hsh or name,
            "name": name,
            "engine_metadata": {
                "engine": "nextflow",
                "process": proc,
                "tag": tag,
                "native_id": native,
                "hash": hsh,
            },
        }

        if status_raw:
            tl["execution_state"] = _STATUS_TO_STATE.get(status_raw, "UNKNOWN")
        if exit_s != "":
            try:
                tl["exit_code"] = int(float(exit_s))
            except ValueError:
                pass
            if tl.get("exit_code", 0) != 0:
                tl["failure_code"] = "NONZERO_EXIT"

        realtime = (row.get("realtime") or row.get("duration") or "").strip()
        pct_cpu = (row.get("%cpu") or row.get("cpu") or "").strip().rstrip("%")
        rss = (row.get("peak_rss") or row.get("rss") or "").strip()

        usage: dict[str, Any] = {}
        seconds = _parse_nextflow_duration_seconds(realtime)
        if seconds is not None:
            usage["wall_time_seconds"] = seconds
        cpu_pct = _parse_float(pct_cpu)
        if cpu_pct is not None and seconds is not None:
            usage["cpu_time_seconds"] = round(seconds * (cpu_pct / 100.0), 3)
        rss_bytes = _parse_memory_to_bytes(rss)
        if rss_bytes is not None:
            usage["peak_memory_bytes"] = rss_bytes
        if usage:
            tl["resource_usage"] = usage

        submit = (row.get("submit") or "").strip()
        complete = (row.get("complete") or "").strip()
        if submit:
            tl["start_time"] = submit
        if complete:
            tl["end_time"] = complete

        tasks.append(tl)
    return tasks


def _parse_float(s: str) -> float | None:
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def _parse_nextflow_duration_seconds(s: str) -> float | None:
    if not s:
        return None
    s = s.strip().lower()
    if s.endswith("ms"):
        return _parse_float(s[:-2].strip()) / 1000.0
    if s.endswith("s"):
        return _parse_float(s[:-1])
    if s.endswith("m"):
        return _parse_float(s[:-1]) * 60.0
    if s.endswith("h"):
        return _parse_float(s[:-1]) * 3600.0
    if ":" in s:
        parts = s.split(":")
        try:
            nums = [float(p) for p in parts]
        except ValueError:
            return None
        if len(nums) == 3:
            return nums[0] * 3600 + nums[1] * 60 + nums[2]
        if len(nums) == 2:
            return nums[0] * 60 + nums[1]
    return _parse_float(s)


def _parse_memory_to_bytes(s: str) -> int | None:
    if not s:
        return None
    s0 = s.strip().upper().replace(" ", "")
    mult = 1
    s = s0
    if s.endswith("KB"):
        mult = 1024
        s = s[:-2]
    elif s.endswith("MB"):
        mult = 1024**2
        s = s[:-2]
    elif s.endswith("GB"):
        mult = 1024**3
        s = s[:-2]
    elif s.endswith("B") and not s.endswith("KB") and not s.endswith("MB") and not s.endswith("GB"):
        s = s[:-1]
    v = _parse_float(s)
    if v is None:
        return None
    return int(v * mult)
