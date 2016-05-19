Design sketch for workflow submission API.  Proof of concept implementation at
https://github.com/common-workflow-language/cwltool-service

# Submission
```
POST http://example.com/run?wf=http://example.com/tools/bwa/version/1.0/descriptor
Headers: ...

{
  "stringparameter": "value",
  "fileparameter": {
    "class": "File",
    "location": "http://storage.example.com/bucket/file1.fq"
  }
}
```

-> 303 See Other http://example.com/jobs/123

# Workflow status
```
GET http://example.com/jobs/123

-> 200 Ok
{
  "run": "http://example.com/tools/bwa/version/1.0/descriptor",
  "input": {
    "stringparameter": "value",
    "fileparameter": {
      "class": "File",
      "location": "http://storage.example.com/bucket/file1.fq"
    }
  },
  "output": null,
  "state": "Running",
  "log": "http://example.com/jobs/123/log"
}
```

```
GET http://example.com/jobs/123
->
(...job log as multipart streaming http response...)
```

# Workflow states
States: Running, Paused, Success, Failed, Canceled

```
POST http://example.com/jobs/123?action=Cancel
```

-> cancel workflow

```
POST http://example.com/jobs/123?action=Pause
```

-> pause workflow

```
POST http://example.com/jobs/123?action=Resume
```

-> resume paused workflow
