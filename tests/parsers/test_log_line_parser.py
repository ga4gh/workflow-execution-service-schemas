import pytest
from datetime import datetime
from parsers.utils.log_line_parser import LogLineParser, LogLine, LogLevel, WorkflowEngine

class TestLogLineParser:
    
    def setup_method(self):
        """Set up test fixtures"""
        self.parser = LogLineParser()
    
    def test_parse_snakemake_rule_line(self):
        """Test parsing Snakemake rule line"""
        line = "[Mon Jan 15 10:23:45 2025] rule process_data: input: data.txt output: results.txt"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.SNAKEMAKE
        assert result.task_name == "process_data"
        assert result.timestamp.year == 2025
        assert result.timestamp.month == 1
        assert result.timestamp.day == 15
    
    def test_parse_snakemake_error_line(self):
        """Test parsing Snakemake error line"""
        line = "[Mon Jan 15 10:24:15 2025] Error in rule process_data: CalledProcessError"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.SNAKEMAKE
        assert result.level == LogLevel.ERROR
        assert result.task_name == "process_data"
    
    def test_parse_snakemake_finished_line(self):
        """Test parsing Snakemake finished job line"""
        line = "[Mon Jan 15 10:24:12 2025] Finished job 0."
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.SNAKEMAKE
        assert "completed" in result.message.lower()
    
    def test_parse_nextflow_submitted_line(self):
        """Test parsing Nextflow submitted line"""
        line = "Jan-15 10:23:45.123 [Task monitor] INFO  nextflow.processor.TaskRun - [a1/b2c3d4] Submitted process > process_data"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.NEXTFLOW
        assert result.level == LogLevel.INFO
        assert result.task_name == "process_data"
        assert result.timestamp is not None
    
    def test_parse_nextflow_completed_line(self):
        """Test parsing Nextflow completed line"""
        line = "Jan-15 10:24:12.456 [Task monitor] INFO  nextflow.processor.TaskRun - [a1/b2c3d4] Completed process > process_data"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.NEXTFLOW
        assert result.task_name == "process_data"
    
    def test_parse_cwl_start_line(self):
        """Test parsing CWL start line"""
        line = "2025-01-15 10:23:45 [workflow] start"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.CWL
        assert result.timestamp.year == 2025
    
    def test_parse_cwl_step_completed_line(self):
        """Test parsing CWL step completed line"""
        line = "2025-01-15 10:24:12 [step process_data] completed success"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.CWL
        assert result.task_name == "process_data"
        assert result.level == LogLevel.INFO
        assert "success" in result.message.lower()
    
    def test_parse_unknown_line(self):
        """Test parsing unknown format line"""
        line = "Some random log line that doesn't match any pattern"
        result = self.parser.parse_line(line)
        
        assert result.engine == WorkflowEngine.UNKNOWN
        assert result.raw_line == line
    
    def test_to_dict(self):
        """Test converting LogLine to dictionary"""
        line = "[Mon Jan 15 10:23:45 2025] rule process_data: input: data.txt"
        result = self.parser.parse_line(line)
        
        data = result.to_dict()
        assert isinstance(data, dict)
        assert 'timestamp' in data
        assert 'engine' in data
        assert 'task_name' in data
        assert data['engine'] == 'snakemake'
        assert data['task_name'] == 'process_data'
