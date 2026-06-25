---
title: Get a list of available packages and updates
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-available-packages-updates
scraped: 2026-05-12T12:14:13.440214
---

# Get a list of available packages and updates

# Get a list of available packages and updates

* Published Mar 12, 2021

This API call provides all available deployment packages and updates as Offline Bundles.

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

Download available update packages for your cluster.

#### Curl

```
curl -X GET "https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle/published" -H "accept: application/json" -H "Authorization: Bearer eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA"
```

#### Request URL

```
https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle/published
```

#### Response body

```
[



{



"type": "agent",



"version": "1.205.164.20201203-134053",



"downloadLink": "https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle?bundle=agent:1.205.164.20201203-134053&token=AAAAAAaaaaa0a0aaaa-Aa0a-6EIEO37a13xdLw9AvZ7cPYFyJQAAAKAwgZ0GCSqGSIb3DQEHBqCBjzCBjAIBADCBhgYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzJtRSpS5Gsg_g3esQCARCAWTHi9j6cXuo9Gnw2Vlapr8ka5pBTHkYYX5UIUOlI97z5NpYk77c__LcLno1P7HKC_EMqjQK5JwH8CxtsFmEEIGLgMHv8NC3VM46JPUZE-ldPtCVTDlS2jz6c"



},



{



"type": "js",



"version": "1.207.232.20210115-155828",



"downloadLink": "https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle?bundle=js:1.207.232.20210115-155828&token=AAAAAAaaaaa0a0aaaa-Aa0a-6EIEO37a13xdLw9AvZ7cPYFyJQAAAKAwgZ0GCSqGSIb3DQEHBqCBjzCBjAIBADCBhgYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzJtRSpS5Gsg_g3esQCARCAWTHi9j6cXuo9Gnw2Vlapr8ka5pBTHkYYX5UIUOlI97z5NpYk77c__LcLno1P7HKC_EMqjQK5JwH8CxtsFmEEIGLgMHv8NC3VM46JPUZE-ldPtCVTDlS2jz6c"



},



{



"type": "sg",



"version": "1.207.228.20210114-161145",



"downloadLink": "https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle?bundle=sg:1.207.228.20210114-161145&token=AAAAAAaaaaa0a0aaaa-Aa0a-6EIEO37a13xdLw9AvZ7cPYFyJQAAAKAwgZ0GCSqGSIb3DQEHBqCBjzCBjAIBADCBhgYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzJtRSpS5Gsg_g3esQCARCAWTHi9j6cXuo9Gnw2Vlapr8ka5pBTHkYYX5UIUOlI97z5NpYk77c__LcLno1P7HKC_EMqjQK5JwH8CxtsFmEEIGLgMHv8NC3VM46JPUZE-ldPtCVTDlS2jz6c"



}



]
```

#### Response code

`200`