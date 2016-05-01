Design sketch for workflow submission API.

# Submission
```
POST http://example.com/workflows/submit?tool=http://example.com/tools/bwa/version/1.0/descriptor
Headers: ...

{
  "stringparameter": "value",
  "fileparameter": {
    "class": "File",
    "location": "http://storage.example.com/bucket/file1.fq"
  }
}
```

-> 303 See Other http://example.com/workflows/123

# Workflow status
```
GET http://example.com/workflows/123

-> 200 Ok
{
  "tool": "http://example.com/tools/bwa/version/1.0/descriptor",
  "input": {
    "stringparameter": "value",
    "fileparameter": {
      "class": "File",
      "location": "http://storage.example.com/bucket/file1.fq"
    }
  },
  "output": null,
  "state": "Running",
  "message": "Ok",
  "jobs": [
    {
      "label": "step1",
      "state": "Running"
    },
    {
      "label": "step2",
      "state": "Queued"
      "jobs": [
        {
          "label": "step2.1",
          "state": "Queued"
        },
        {
          "label": "step2.2",
          "state": "Queued"
        }
      ]
    }
  ]
}
```

# Workflow states
States: Queued, Running, Paused, Complete, Error, Canceled

```
POST http://example.com/workflows/123?action=Cancel
```

-> cancel workflow

```
POST http://example.com/workflows/123?action=Pause
```

-> pause workflow
