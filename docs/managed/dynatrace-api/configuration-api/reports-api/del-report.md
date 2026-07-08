---
title: Reports API - DELETE a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/del-report
---

# Reports API - DELETE a report

# Reports API - DELETE a report

* Reference
* Published Jan 16, 2020

Deletes the specified report. Deletion cannot be undone!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the report to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The report has been deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the report from the [POST request example](/managed/dynatrace-api/configuration-api/reports-api/post-report#example "Create a report configuration via the Dynatrace API."). The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73 \



-H 'Authorization: Api-token abcdefghij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73
```

#### Response code

204

## Related topics

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.")