import re
from datetime import datetime
from typing import Optional, Dict
from enum import Enum

class LogLevel(Enum):
    """Log severity levels"""
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

class WorkflowEngine(Enum):
    """Supported workflow engines"""
    SNAKEMAKE = "snakemake"
    NEXTFLOW = "nextflow"
    CWL = "cwl"
    UNKNOWN = "unknown"

class LogLine:
    """Represents a parsed log line"""
    
    def __init__(
        self,
        timestamp: Optional[datetime] = None,
        level: LogLevel = LogLevel.INFO,
        engine: WorkflowEngine = WorkflowEngine.UNKNOWN,
        task_name: Optional[str] = None,
        message: str = "",
        raw_line: str = ""
    ):
        self.timestamp = timestamp
        self.level = level
        self.engine = engine
        self.task_name = task_name
        self.message = message
        self.raw_line = raw_line
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "level": self.level.value,
            "engine": self.engine.value,
            "task_name": self.task_name,
            "message": self.message,
            "raw_line": self.raw_line
        }
    
    def __repr__(self):
        return f"LogLine(timestamp={self.timestamp}, task={self.task_name}, level={self.level.value})"


class LogLineParser:
    """Parser for individual workflow log lines"""
    
    # Snakemake patterns
    SNAKEMAKE_TIMESTAMP = r'{{{{\[(.*?)\]}}}}'
    SNAKEMAKE_RULE = r'rule (\w+):'
    SNAKEMAKE_ERROR = r'Error in rule (\w+)'
    SNAKEMAKE_FINISHED = r'Finished job'
    
    # Nextflow patterns
    NEXTFLOW_TIMESTAMP = r'(\w{3}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})'
    NEXTFLOW_PROCESS = r'process > (\w+)'
    NEXTFLOW_LEVEL = r'{{{{\[(.*?)\]}}}}\s+(INFO|ERROR|WARN|DEBUG)'
    
    # CWL patterns
    CWL_TIMESTAMP = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    CWL_STEP = r'{{{{\[step (\w+)\]}}}}'
    
    def parse_line(self, line: str) -> LogLine:
        """
        Parse a single log line and return structured data
        
        Args:
            line: Raw log line string
            
        Returns:
            LogLine object with extracted information
        """
        line = line.strip()
        
        # Try to detect engine and parse accordingly
        if self._is_snakemake(line):
            return self._parse_snakemake(line)
        elif self._is_nextflow(line):
            return self._parse_nextflow(line)
        elif self._is_cwl(line):
            return self._parse_cwl(line)
        else:
            return LogLine(raw_line=line)
    
    def _is_snakemake(self, line: str) -> bool:
        """Check if line is from Snakemake"""
        return line.startswith('[') and 'rule' in line.lower()
    
    def _is_nextflow(self, line: str) -> bool:
        """Check if line is from Nextflow"""
        return 'nextflow' in line.lower() or re.search(self.NEXTFLOW_TIMESTAMP, line) is not None
    
    def _is_cwl(self, line: str) -> bool:
        """Check if line is from CWL"""
        return '[workflow]' in line or '[step' in line
    
    def _parse_snakemake(self, line: str) -> LogLine:
        """Parse Snakemake log line"""
        log_line = LogLine(engine=WorkflowEngine.SNAKEMAKE, raw_line=line)
        
        # Extract timestamp
        timestamp_match = re.search(self.SNAKEMAKE_TIMESTAMP, line)
        if timestamp_match:
            timestamp_str = timestamp_match.group(1)
            try:
                log_line.timestamp = datetime.strptime(timestamp_str, '%a %b %d %H:%M:%S %Y')
            except ValueError:
                pass
        
        # Check for error
        if 'Error' in line or 'error' in line:
            log_line.level = LogLevel.ERROR
            error_match = re.search(self.SNAKEMAKE_ERROR, line)
            if error_match:
                log_line.task_name = error_match.group(1)
        
        # Extract rule name
        rule_match = re.search(self.SNAKEMAKE_RULE, line)
        if rule_match:
            log_line.task_name = rule_match.group(1)
        
        # Check for finished job
        if re.search(self.SNAKEMAKE_FINISHED, line):
            log_line.message = "Job completed"
        
        log_line.message = line
        return log_line
    
    def _parse_nextflow(self, line: str) -> LogLine:
        """Parse Nextflow log line"""
        log_line = LogLine(engine=WorkflowEngine.NEXTFLOW, raw_line=line)
        
        # Extract timestamp
        timestamp_match = re.search(self.NEXTFLOW_TIMESTAMP, line)
        if timestamp_match:
            timestamp_str = timestamp_match.group(1)
            try:
                # Add current year since Nextflow doesn't include it
                timestamp_str = f"{datetime.now().year}-{timestamp_str}"
                log_line.timestamp = datetime.strptime(timestamp_str, '%Y-%b-%d %H:%M:%S.%f')
            except ValueError:
                pass
        
        # Extract log level
        level_match = re.search(self.NEXTFLOW_LEVEL, line)
        if level_match:
            level_str = level_match.group(2)
            log_line.level = LogLevel[level_str] if level_str in LogLevel.__members__ else LogLevel.INFO
        
        # Extract process name
        process_match = re.search(self.NEXTFLOW_PROCESS, line)
        if process_match:
            log_line.task_name = process_match.group(1)
        
        log_line.message = line
        return log_line
    
    def _parse_cwl(self, line: str) -> LogLine:
        """Parse CWL log line"""
        log_line = LogLine(engine=WorkflowEngine.CWL, raw_line=line)
        
        # Extract timestamp
        timestamp_match = re.search(self.CWL_TIMESTAMP, line)
        if timestamp_match:
            timestamp_str = timestamp_match.group(1)
            try:
                log_line.timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                pass
        
        # Extract step name
        step_match = re.search(self.CWL_STEP, line)
        if step_match:
            log_line.task_name = step_match.group(1)
        
        # Check for success/error
        if 'success' in line.lower():
            log_line.level = LogLevel.INFO
            log_line.message = "Step completed successfully"
        elif 'error' in line.lower() or 'failed' in line.lower():
            log_line.level = LogLevel.ERROR
            log_line.message = "Step failed"
        
        log_line.message = line
        return log_line


# Convenience function
def parse_log_line(line: str) -> LogLine:
    """Parse a single log line"""
    parser = LogLineParser()
    return parser.parse_line(line)
