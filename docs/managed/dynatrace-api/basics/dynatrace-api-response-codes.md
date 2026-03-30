---
title: "Dynatrace API - Response codes"
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/dynatrace-api-response-codes
updated: 2026-02-09
---

Unless otherwise specified, the following response codes are used:

| Code | Description |
| --- | --- |
| 200 | **OK**. The request is successful. |
| 400 | **Bad request**. The request has failed. The body of the response provides additional details. |
| 401 | **Unauthorized.** The token authentication has failed. Check to see if your token has the required scopes. |
| 404 | **Not found**. The requested resource is not found in your environment. Check if your input is correct. |
| 429 | **Too many requests**. You have reached the limit of API usage. |

## Configuration API

The Configuration API uses slightly different set of response codes. The following response codes are used:

| Code | Description |
| --- | --- |
| 200 | **OK**. The GET request is successful. |
| 201 | **Created**. The POST or PUT request has successfully created a new resource. |
| 204 | **No content**. The PUT or DELETE request has successfully updated or deleted a resource. |
| 400 | **Bad request**. The request has failed. The body of the response provides additional details. |
| 401 | **Unauthorized.** The token authentication has failed. Check to see if your token has the required scopes. |
| 404 | **Not found**. The requested resource is not found in your environment. Check if your input is correct. |
| 429 | **Too many requests**. You have reached the limit of API usage. |

In case when a successful request may return different codes, it is specified in the description of the request.
