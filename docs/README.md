View the full [Reference Documentation](https://ga4gh.github.io/workflow-execution-service-schemas/docs/) for the Workflow Execution Service API.


## Filtering Workflow Runs

WES supports filtering the `GET /runs` endpoint to efficiently query specific workflows without retrieving all runs.

**Quick examples:**

```bash
# Get running workflows
GET /runs?state=RUNNING

# Get failed workflows from last 24 hours
GET /runs?state=EXECUTOR_ERROR&since=2025-01-08T00:00:00Z

# Search by workflow name
GET /runs?workflow_name=alignment

# Filter by tags
GET /runs?tag=batch:12345&tag=project:cancer
