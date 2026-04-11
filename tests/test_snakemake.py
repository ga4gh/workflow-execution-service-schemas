from __future__ import annotations

from pathlib import Path

from wes_structured_logs.snakemake import parse_snakemake_benchmark_tsv, parse_snakemake_run_log_text

FIX = Path(__file__).resolve().parent / "fixtures" / "snakemake"


def test_parse_snakemake_run_log_text() -> None:
    text = (FIX / "run_log_sample.txt").read_text(encoding="utf-8")
    out = parse_snakemake_run_log_text(text, name="wf")
    assert out["name"] == "wf"
    assert out["engine_metadata"]["engine"] == "snakemake"
    assert out["engine_metadata"]["last_rule"] == "align"
    lines = out["structured_stdout"]["lines"]
    assert any("rule align" in x["message"] for x in lines)
    bracket = [x for x in lines if x["message"].startswith("[Wed")]
    assert bracket and "ts" in bracket[0]


def test_parse_snakemake_benchmark_tsv() -> None:
    path = FIX / "benchmark_sample.tsv"
    usage = parse_snakemake_benchmark_tsv(path)
    assert usage["wall_time_seconds"] == 120.5
    assert usage["cpu_time_seconds"] == 118.2
    assert usage["peak_memory_bytes"] == 512 * 1024 * 1024
