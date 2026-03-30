# Filtering Examples

This document provides example HTTP requests and responses for the filtering capabilities of the WES API.

## Example 1: Filter by State (Single)

**Request:**
```http
GET /ga4gh/wes/v1/runs?state=RUNNING HTTP/1.1
Host: wes.example.com
Authorization: Bearer <token>
