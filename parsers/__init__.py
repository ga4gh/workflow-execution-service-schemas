

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict, Any
from enum import Enum


class State(str, Enum):
    """
    Workflow/Task execution states from WES API spec.
    """
    UNKNOWN = "UNKNOWN"
    QUEUED = "QUEUED"
    INITIALIZING = "INITIALIZING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETE = "COMPLETE"
    EXECUTOR_ERROR = "EXECUTOR_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"
    CANCELED = "CANCELED"
    CANCELING = "CANCELING"
    PREEMPTED = "PREEMPTED"


class Log(BaseModel):
    """
    Base log information (matches WES API Log schema).
    """
    name: str = Field(..., description="The task or workflow name")
    cmd: Optional[List[str]] = Field(None, description="The command line that was executed")
    start_time: Optional[str] = Field(None, description="ISO 8601 format: %Y-%m-%dT%H:%M:%SZ")
    end_time: Optional[str] = Field(None, description="ISO 8601 format: %Y-%m-%dT%H:%M:%SZ")
    stdout: Optional[str] = Field(None, description="URL to stdout logs")
    stderr: Optional[str] = Field(None, description="URL to stderr logs")
    exit_code: Optional[int] = Field(None, description="Exit code of the program")
    system_logs: Optional[List[str]] = Field(default_factory=list, description="System-relevant logs")


class TaskLog(Log):
    """
    Runtime information for a given task (matches WES API TaskLog schema).
    Extends Log with task-specific fields.
    """
    id: str = Field(..., description="Unique identifier for the task")
    tes_uri: Optional[str] = Field(None, description="Optional URL to TES task definition")


class RunRequest(BaseModel):
    """
    Workflow run request parameters (matches WES API RunRequest schema).
    """
    workflow_params: Optional[Dict[str, Any]] = None
    workflow_type: str
    workflow_type_version: str
    tags: Optional[Dict[str, str]] = Field(default_factory=dict)
    workflow_engine_parameters: Optional[Dict[str, str]] = None
    workflow_engine: Optional[str] = None
    workflow_engine_version: Optional[str] = None
    workflow_url: str


class RunLog(BaseModel):
    """
    Complete workflow run information (matches WES API RunLog schema).
    """
    run_id: str
    request: Optional[RunRequest] = None
    state: State
    run_log: Optional[Log] = None
    task_logs_url: Optional[str] = None
    task_logs: Optional[List[TaskLog]] = Field(default_factory=list, deprecated=True)
    outputs: Optional[Dict[str, Any]] = None
