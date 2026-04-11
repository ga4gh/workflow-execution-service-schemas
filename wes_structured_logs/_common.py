from __future__ import annotations

import re
from datetime import datetime
from typing import Any


def structured_line(
    message: str,
    *,
    ts: str | None = None,
    level: str | None = None,
) -> dict[str, Any]:
    line: dict[str, Any] = {"message": message}
    if ts is not None:
        line["ts"] = ts
    if level is not None:
        line["level"] = level
    return line


def structured_content(
    lines: list[dict[str, Any]],
    *,
    truncated: bool | None = None,
    total_bytes: int | None = None,
    content_encoding: str | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {"lines": lines}
    if truncated is not None:
        out["truncated"] = truncated
    if total_bytes is not None:
        out["total_bytes"] = total_bytes
    if content_encoding is not None:
        out["content_encoding"] = content_encoding
    return out


_SNAKEMAKE_BRACKET_TS = re.compile(
    r"^\[(?P<ts>[A-Za-z]{3}\s+[A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4})\]\s*$"
)


def parse_snakemake_bracket_timestamp(line: str) -> str | None:
    m = _SNAKEMAKE_BRACKET_TS.match(line.strip())
    if not m:
        return None
    raw = m.group("ts")
    try:
        dt = datetime.strptime(raw, "%a %b %d %H:%M:%S %Y")
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return raw


_NEXTFLOW_LOG_LINE = re.compile(
    r"^(?P<mon>[A-Za-z]{3})-(?P<day>\d{1,2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2}\.\d+)\s+"
    r"\[[^\]]+\]\s+"
    r"(?P<level>DEBUG|INFO|WARN|WARNING|ERROR|TRACE)\s+"
    r"(?P<rest>.+)$"
)


def parse_nextflow_log_line(line: str, *, year: int | None = None) -> dict[str, Any] | None:
    m = _NEXTFLOW_LOG_LINE.match(line.rstrip())
    if not m:
        return None
    mon, day, time_s, level, rest = (
        m.group("mon"),
        m.group("day"),
        m.group("time"),
        m.group("level"),
        m.group("rest").strip(),
    )
    y = year if year is not None else datetime.now().year
    if "." in time_s:
        hms, frac = time_s.split(".", 1)
        frac = (frac + "000000")[:6]
        time_norm = f"{hms}.{frac}"
    else:
        time_norm = f"{time_s}.000000"
    try:
        dt = datetime.strptime(f"{mon} {int(day)} {time_norm} {y}", "%b %d %H:%M:%S.%f %Y")
        ts = dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    except ValueError:
        ts = f"{y}-{mon}-{day}T{time_s}Z"
    if level == "WARNING":
        level = "WARN"
    return structured_line(rest, ts=ts, level=level)
