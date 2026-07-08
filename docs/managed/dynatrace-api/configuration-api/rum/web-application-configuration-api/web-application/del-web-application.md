---
title: Web application configuration API - DELETE a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application
---

# Web application configuration API - DELETE a web application

# Web application configuration API - DELETE a web application

* Reference
* Published Sep 03, 2019

Deletes the specified web application.

This API only supports web applications. For mobile and custom applications, see [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the web application to delete. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The application has been deleted. The response does not have a body. |

## Related topics

* [Delete a web application in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.")