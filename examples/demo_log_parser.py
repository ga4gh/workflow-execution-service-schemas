#!/usr/bin/env python3
"""
Demo script showing how to use the log line parser
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from parsers.utils.log_line_parser import parse_log_line

def main():
    """Demo the log line parser"""
    
    print("=" * 60)
    print("Log Line Parser Demo")
    print("=" * 60)
    print()
    
    # Sample lines
    sample_lines = [
        "[Mon Jan 15 10:23:45 2025] rule process_data: input: data.txt output: results.txt",
        "[Mon Jan 15 10:24:15 2025] Error in rule process_data: CalledProcessError",
        "Jan-15 10:23:45.123 [Task monitor] INFO  nextflow.processor.TaskRun - Submitted process > analyze_results",
        "2025-01-15 10:24:12 [step process_data] completed success"
    ]
    
    for i, line in enumerate(sample_lines, 1):
        print(f"Example {i}:")
        print(f"Input:  {line}")
        
        # Parse the line
        result = parse_log_line(line)
        
        # Show parsed result
        print(f"Parsed: {result}")
        print(f"JSON:   {json.dumps(result.to_dict(), indent=2)}")
        print()
    
    print("=" * 60)
    print("Try it with your own log lines!")
    print("=" * 60)

if __name__ == "__main__":
    main()
