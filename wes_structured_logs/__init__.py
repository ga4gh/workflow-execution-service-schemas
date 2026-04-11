"""Engine log parsers producing WES-aligned structured Log / TaskLog dictionaries."""

from wes_structured_logs.nextflow import (
    parse_nextflow_log_text,
    parse_nextflow_trace_tsv,
)
from wes_structured_logs.snakemake import (
    parse_snakemake_benchmark_tsv,
    parse_snakemake_run_log_text,
)

__all__ = [
    "parse_nextflow_log_text",
    "parse_nextflow_trace_tsv",
    "parse_snakemake_benchmark_tsv",
    "parse_snakemake_run_log_text",
]
