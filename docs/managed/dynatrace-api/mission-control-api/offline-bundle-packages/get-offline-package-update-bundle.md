---
title: Get offline bundle
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-offline-package-update-bundle
---

# Get offline bundle

# Get offline bundle

* Published Apr 02, 2020

This API call gets specific deployment package and update as an Offline Bundles.

## Endpoint

`/public/downloads/offline-bundle/published`

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | List of Offline Bundles generated successfully |
| **401** | Invalid credentials |
| **404** | Cluster not found |

## Example

In this example you will download an offline update bundle for OneAgent 1.214.0.20210305-194131 release.

#### Request URL

```
https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle?bundle=agent:1.214.0.20210305-194131&token=aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA
```

#### Response body

A ZIP file containing an update for OneAgent OneAgent 1.214.0.20210305-194131