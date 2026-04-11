from __future__ import annotations

from pathlib import Path

from wes_structured_logs.nextflow import parse_nextflow_log_text, parse_nextflow_trace_tsv

FIX = Path(__file__).resolve().parent / "fixtures" / "nextflow"


def test_parse_nextflow_trace_tsv() -> None:
    tasks = parse_nextflow_trace_tsv(FIX / "trace_sample.tsv")
    assert len(tasks) == 1
    t = tasks[0]
    assert t["id"] == "1"
    assert t["execution_state"] == "COMPLETE"
    assert t["exit_code"] == 0
    assert t["engine_metadata"]["process"] == "sketch"
    assert t["resource_usage"]["wall_time_seconds"] == 4.5
    assert t["resource_usage"]["peak_memory_bytes"] == 1048576
    assert "cpu_time_seconds" in t["resource_usage"]


def test_parse_nextflow_log_text() -> None:
    text = (FIX / "nextflow_log_sample.txt").read_text(encoding="utf-8")
    out = parse_nextflow_log_text(text, year=2024, name="run1")
    assert out["name"] == "run1"
    lines = out["structured_stdout"]["lines"]
    info = [x for x in lines if x.get("level") == "INFO"]
    assert info and "Launching" in info[0]["message"]
    assert "ts" in info[0]
