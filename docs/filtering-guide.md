# Filtering Workflow Runs

The WES API supports filtering workflow runs via query parameters on the `GET /runs` endpoint.

## Filter Parameters

### By State

Filter by workflow execution state. Multiple states use OR logic.

**Single state:**
```bash
GET /runs?state=RUNNING
