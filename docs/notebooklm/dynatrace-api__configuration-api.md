# Dynatrace Documentation: dynatrace-api/configuration-api

Generated: 2026-02-17

Files combined: 12

---


## Source: aws-privatelink.md


---
title: AWS PrivateLink API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/aws-privatelink
scraped: 2026-02-15T21:24:45.349664
---

# AWS PrivateLink API

# AWS PrivateLink API

* Reference
* Published Nov 19, 2020

[### View configuration

Get an overview of AWS PrivateLink.](/docs/dynatrace-api/configuration-api/aws-privatelink/get-configuration "Read the configuration of AWS PrivateLink via Dynatrace API.")[### Update configuration

Update configuration of AWS PrivateLink.](/docs/dynatrace-api/configuration-api/aws-privatelink/put-configuration "Update the configuration of AWS PrivateLink via Dynatrace API.")

[### View allowlist

View accounts in the AWS PrivateLink allowlist.](/docs/dynatrace-api/configuration-api/aws-privatelink/get-allowlist "View the AWS PrivateLink allowlist via Dynatrace API.")[### Add to allowlist

Add an account to the AWS PrivateLink allowlist.](/docs/dynatrace-api/configuration-api/aws-privatelink/put-allowlist "Add your AWS account to the AWS PrivateLink allowlist via Dynatrace API.")[### Remove from allowlist

Remove and account from the AWS PrivateLink allowlist.](/docs/dynatrace-api/configuration-api/aws-privatelink/delete-allowlist "Remove your AWS account from the AWS PrivateLink allowlist via Dynatrace API.")


---


## Source: calculated-metrics.md


---
title: Calculated metrics API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/calculated-metrics
scraped: 2026-02-16T21:13:44.153244
---

# Calculated metrics API

# Calculated metrics API

* Reference
* Published Apr 16, 2020

### Mobile apps

* [View all mobile apps metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-all "View all calculated mobile apps metrics of your environment via the Dynatrace API.")
* [View a mobile apps metric](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-metric "View a calculated mobile apps metric via the Dynatrace API.")
* [Edit a mobile apps metric](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/put-metric "Edit a calculated mobile apps metric via the Dynatrace API.")
* [Delete a mobile apps metric](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/del-metric "Delete a calculated mobile apps metric via the Dynatrace API.")

### Service

* [View all service metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/get-all "View all calculated service metrics of your environment via the Dynatrace API.")
* [View a service metric](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/get-calculated-metric "View a calculated service metric via the Dynatrace API.")
* [Create a service metric](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/post-calculated-metric "Create a calculated service metric via the Dynatrace API.")
* [Edit a service metric](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/put-calculated-metric "Update a calculated service metric via the Dynatrace API.")
* [Delete a service metric](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/del-calculated-metric "Delete a calculated service metric via the Dynatrace API.")

#### Metrics on Grail

* [View all metrics on Grail](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/get-metrics-on-grail "View calculated service metrics enabled on Grail via the Dynatrace API.")
* [Edit a metric on Grail](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics/put-metric-on-grail "Enable or disable a calculated service metric via the Dynatrace API.")

### Synthetic

* [View all synthetic metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/get-all "View all calculated synthetic metrics of your environment via the Dynatrace API.")
* [View a synthetic metric](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/get-metric "View a calculated synthetic metric via the Dynatrace API.")
* [Create a synthetic metric](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/post-metric "Create a calculated synthetic metric via the Dynatrace API.")
* [Edit a synthetic metric](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/put-metric "Edit a calculated synthetic metric via the Dynatrace API.")
* [Delete a synthetic metric](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/del-metric "Delete a calculated synthetic metric via the Dynatrace API.")

### Web application

* [View all web application metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/get-all "View all calculated web application metrics of your environment via the Dynatrace API.")
* [View a web application metric](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/get-metric "View a calculated web application metric via the Dynatrace API.")
* [Edit a web application metric](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/put-metric "Edit a calculated web application metric via the Dynatrace API.")
* [Delete a web application metric](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/del-metric "Delete a calculated web application metric via the Dynatrace API.")


---


## Source: put-monitoring-configuration.md


---
title: OneAgent monitoring configuration API - PUT configuration
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration
scraped: 2026-02-06T16:31:13.607418
---

# OneAgent monitoring configuration API - PUT configuration

# OneAgent monitoring configuration API - PUT configuration

* Reference
* Updated on Jun 23, 2022
* Deprecated

This API is deprecated. Use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Monitoring** (`builtin:host.monitoring`) schema instead.

Updates the monitoring configuration of OneAgent on the specified host.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/config/v1/hosts/{id}/monitoring` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required host. | path | Required |
| body | [MonitoringConfig](#openapi-definition-MonitoringConfig) | The JSON body of the request. Contains OneAgent monitoring parameters. | body | Optional |

### Request body objects

#### The `MonitoringConfig` object

Monitoring configuration of OneAgent.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| autoInjectionEnabled | boolean | Code modules will be injected automatically into monitored applications if this setting is enabled. This setting won't apply if auto-injection is disabled via oneagentctl (see https://dt-url.net/oneagentctl). | Optional |
| id | string | The Dynatrace entity ID of the host where OneAgent is deployed. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| monitoringEnabled | boolean | The monitoring is enabled (`true`) or disabled (`false`). | Required |
| monitoringMode | string | The monitoring mode for the host: full stack or infrastructure only. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"autoInjectionEnabled": true,



"id": "HOST-0123456789ABCDE",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"monitoringEnabled": true,



"monitoringMode": "FULL_STACK"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/config/v1/hosts/{id}/monitoring/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/config/v1/hosts/{id}/monitoring/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```


---


## Source: allowed-beacon-cors.md


---
title: Allowed beacon domains API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/allowed-beacon-cors
scraped: 2026-02-17T05:10:02.712198
---

# Allowed beacon domains API

# Allowed beacon domains API

* Reference
* Published Sep 23, 2020

The **Allowed beacon domains** API enables you to manage the list of RUM beacon origins that must be accepted by OneAgent and ActiveGate.

To manage the RUM beacon origins list in the Dynatrace web UI, go to **Settings** > **Web and mobile monitoring** > **Beacon origins for CORS**.

[### View configuration

Get an overview of allowed beacon origins.](/docs/dynatrace-api/configuration-api/rum/allowed-beacon-cors/get-configuration "Read allowed beacon domains list via the Dynatrace API.")[### Update configuration

Update configuration of allowed beacon origins.](/docs/dynatrace-api/configuration-api/rum/allowed-beacon-cors/put-configuration "Update allowed beacon domains list via the Dynatrace API.")

## Related topics

* [Configure beacon origin allowlist for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.")


---


## Source: content-resources.md


---
title: Content resources API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/content-resources
scraped: 2026-02-15T21:23:03.229016
---

# Content resources API

# Content resources API

* Reference
* Published Sep 23, 2020

The **Content resources** API enables you to manage the configuration of content providers. You can also manage the same configuration in the Dynatrace UI at **Settings > Web and mobile monitoring > Content resources**.

[### View configuration

Get an overview of content providers configuration.](/docs/dynatrace-api/configuration-api/rum/content-resources/get-configuration "Read the configuration of content providers via the Dynatrace API.")[### Update configuration

Update configuration of content providers.](/docs/dynatrace-api/configuration-api/rum/content-resources/put-configuration "Update the configuration of content providers via the Dynatrace API.")

## Related topics

* [Configure first-party, third-party, and CDN resource detection for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")
* [Configure first-party, third-party, and CDN resource detection for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Manually define third-party and CDN providers along with auto-detected providers for your mobile applications.")
* [Configure first-party, third-party, and CDN resource detection for custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Manually define third-party and CDN providers along with auto-detected providers for your custom applications.")


---


## Source: geographic-regions-ip-address.md


---
title: Geographic regions - IP address mapping rules API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-address
scraped: 2026-02-15T09:06:33.210172
---

# Geographic regions - IP address mapping rules API

# Geographic regions - IP address mapping rules API

* Reference
* Published Sep 24, 2020

The **Geographic regions - IP address mapping rules** API enables you to manage the configuration of IP address mapping to geographic locations. You can also manage the same configuration in the Dynatrace UI at **Settings > Web and mobile monitoring > Map IP addresses to locations**.

[### View configuration

Get an overview of IP address mappings.](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration "Read the configuration of IP address mapping via the Dynatrace API.")[### Update configuration

Update configuration of IP address mappings.](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Update the configuration of IP address mapping via the Dynatrace API.")

## Related topics

* [Map internal IP addresses to locations for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Map internal IP addresses to locations for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")
* [Map internal IP addresses to locations for custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")


---


## Source: geographic-regions-ip-header.md


---
title: Geographic regions - IP mapping headers API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-header
scraped: 2026-02-17T04:58:20.014133
---

# Geographic regions - IP mapping headers API

# Geographic regions - IP mapping headers API

* Reference
* Published Sep 24, 2020

The **Geographic regions - IP mapping headers** API enables you to manage the configuration of IP address mapping to geographic locations. You can also manage the same configuration in the Dynatrace UI at **Settings > Web and mobile monitoring > IP determination**.

[### View configuration

Get an overview of IP address mappings.](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/get-configuration "Read the configuration of IP mapping headers via the Dynatrace API.")[### Update configuration

Update configuration of IP address mappings.](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/put-configuration "Update the configuration of IP mapping headers via the Dynatrace API.")

## Related topics

* [Customize IP address detection for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications.")
* [Customize IP address detection for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Change the way Dynatrace determines client IP addresses for your mobile applications.")
* [Customize IP address detection for custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Change the way Dynatrace determines client IP addresses for your custom applications.")


---


## Source: mobile-custom-app-configuration.md


---
title: Mobile and custom app API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration
scraped: 2026-02-15T21:28:59.613866
---

# Mobile and custom app API

# Mobile and custom app API

* Reference
* Published Nov 05, 2020

[### List all apps

Get an overview of all mobile and custom apps.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-all "List all mobile and custom apps applications via the Dynatrace API.")[### View an app

Get parameters of an app by its ID.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/get-app "View parameters of a mobile or custom app via the Dynatrace API.")

[### Create an app

Create a new mobile or custom app with the exact parameters you need.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/post-app "Create a mobile or custom app via the Dynatrace API.")[### Edit an app

Update an existing mobile or custom application or create a new app with the specified ID.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/put-app "Update parameters of a mobile or custom app via the Dynatrace API.")[### Delete an app

Delete an app you don't need anymore.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/delete-app "Delete a mobile or custom app via the Dynatrace API.")

[### View key user actions

Get the list of key user actions in the specified application.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/get-configuration "View key user actions of a mobile or custom app via the Dynatrace API.")[### Edit key user actions list

Mark a user action as the key action in the specified application.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/post-configuration "Add a key user action to a mobile or custom app via the Dynatrace API.")[### Delete a key user action

Remove a user action from the list of key actions in the specified application.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/del-configuration "Remove a key user action from a mobile or custom app via the Dynatrace API.")

[### List all user session properties

Get an overview of all session properties of an app.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-all "View all user session properties a mobile or custom app via the Dynatrace API.")[### View a user session property

Get parameters of a session property its ID.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-property "View user session property a mobile or custom app via the Dynatrace API.")

[### Create a user session property

Create a new user session property for your mobile or custom app.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/post-property "Create user session property a mobile or custom app via the Dynatrace API.")[### Edit a user session property

Update an existing user session property for your mobile or custom app.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/put-property "Update user session property a mobile or custom app via the Dynatrace API.")[### Delete a user session property

Delete a user session property you don't need anymore.](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/delete-property "Delete user session property a mobile or custom app via the Dynatrace API.")


---


## Source: web-application-configuration-api.md


---
title: Web application configuration API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-02-17T05:03:08.675443
---

# Web application configuration API

# Web application configuration API

* Reference
* Published Jan 24, 2019

The **Web application configuration** API enables you to manage configuration of [web applications](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.").

This API only supports web applications. For mobile and custom applications, see [Mobile and custom app API](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

[### List all

Get an overview of all web applications.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-all "List all web applications via the Dynatrace API.")[### View a web application

Get parameters of a web application by its ID.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application "View parameters of a web application via the Dynatrace API.")

[### Create a web application

Create a new web application with the exact parameters you need.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.")[### Edit a web application

Update an existing web application or create a new application with the specified ID.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application "Update a web application via the Dynatrace API.")[### Delete a web application

Delete a web application you don't need anymore.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application "Delete a web application via the Dynatrace API.")

Default application is pre-configured in your Dynatrace environment. By default all traffic goes to this application. After you configure your own [applications](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology."), all the traffic, which doesn't fit to any of your applications, goes to the default one.

[### View configuration

Get the parameters of the default web application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/get-configuration "View configuration of the default web application via the Dynatrace API.")[### Update configuration

Update the parameters of the default web application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration "Update configuration of the default web application via the Dynatrace API.")

### Check data privacy

View the data privacy parameters for

* [All applications](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps "View data privacy configuration of all applications via the Dynatrace API.")
* [A specific application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-web-app "View data privacy configuration of an application via the Dynatrace API.")
* [The default application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app "View data privacy configuration of the default application via the Dynatrace API.")

### Update data privacy

View the data privacy parameters for

* [A specific application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-web-app "Edit data privacy configuration of an application via the Dynatrace API.")
* [The default application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app "Edit data privacy configuration of the default application via the Dynatrace API.")

[### View key user actions

Get the list of key user actions in an application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration "View key user actions of a web application via the Dynatrace API.")[### Edit key user actions list

Mark a user action as the key action in an application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/post-configuration "Add a key user action to a web application via the Dynatrace API.")[### Delete a key user action

Remove a user action from the list of key actions in an application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration "Remove a key user action from a web application via the Dynatrace API.")

[### View error rules

Get an overview of error rules configuration.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration "Read error rules of an application via the Dynatrace API.")[### Update error rules

Update configuration of configuration.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration "Update error rules of an application via the Dynatrace API.")


---


## Source: detection-rules.md


---
title: Service detection API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/detection-rules
scraped: 2026-02-16T21:13:13.986496
---

# Service detection API

# Service detection API

* Reference
* Published Jun 19, 2019

The **Rule-based service detection** API enables you to manage the configuration of service detection rules.

### List all

Get an overview of all service detection rules for:

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-all "View all service detection rules for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-all "View all service detection rules for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-all "View all service detection rules for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-all "View all service detection rules for external and opaque web services via the Dynatrace API.")

### View a rule

Get parameters of a service detection rule for:

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-a-rule "View a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-a-rule "View a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-a-rule "View a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-rule "View a service detection rule for external and opaque web services via the Dynatrace API.")

### Reorder rules

Service detection rules are evaluated one after another. The first matching rule is applied and further processing stops. Reorder service detection rules to achieve the order of evaluation you need.

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/reorder-rules "Reorder service detection rules for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/reorder-rules "Reorder service detection rules for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/reorder-rules "Reorder service detection rules for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/reorder-rules "Reorder service detection rules for external and opaque web services via the Dynatrace API.")

### Create a rule

Create a new service detection rule for:

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/post-a-rule "Create a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/post-a-rule "Create a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/post-a-rule "Create a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/post-rule "Create a service detection rule for external and opaque web services via the Dynatrace API.")

### Edit a rule

Update an existing service detection rule or create a new rule with the specified ID.

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/put-a-rule "Edit a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/put-a-rule "Edit a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/put-a-rule "Edit a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/put-rule "Edit a service detection rule for external and opaque web services via the Dynatrace API.")

### Delete a rule

Delete a service detection rule you don't need anymore.

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/del-a-rule "Delete a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/del-a-rule "Delete a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/del-a-rule "Delete a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/delete-rule "Delete a service detection rule for external and opaque web services via the Dynatrace API.")

## Related topics

* [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")


---


## Source: failure-detection.md


---
title: Failure detection API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/failure-detection
scraped: 2026-02-17T05:12:01.107001
---

# Failure detection API

# Failure detection API

* Reference
* Published Jan 11, 2021

[### List all parameter sets

Get an overview of all parameter sets for failure detection rules.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/get-all "View all failure detection parameter sets of your monitoring environment via the Dynatrace API.")[### View a parameter set

View the configuration of all parameter sets for failure detection rules.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/get-parameter-set "View a failure detection parameter set via the Dynatrace API.")

[### Create a parameter set

Create a new parameter set for failure detection rules.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/post-parameter-set "Create a failure detection parameter set via the Dynatrace API.")

### Edit a parameter set

* [Update an existing parameter set](/docs/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/put-parameter-set "Edit a failure detection parameter set via the Dynatrace API.") for failure detection rules.
* [Change the ID](/docs/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/change-id "Change the ID of a failure detection parameter set via the Dynatrace API.") of a parameter set.

[### Delete a parameter set

Delete a parameter set for failure detection rules.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/delete-parameter-set "Delete a failure detection parameter set via the Dynatrace API.")

[### List all rules

Get an overview of all failure detection rules.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/get-all "View all failure detection rules of your monitoring environment via the Dynatrace API.")[### View a rule

View the configuration of a failure detection rule.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/get-rule "View a failure detection rule via the Dynatrace API.")[### Reorder rules

Failure detection rules are evaluated one after another. The first matching rule is applied, and further processing stops.

Reorder the rules to achieve the order of evaluation you need.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Change the order of failure detection rules via the Dynatrace API.")[### Create a rule

Create a new failure detection rule.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/post-rule "Create a failure detection rule via the Dynatrace API.")

### Edit a rule

* [Update an existing](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/put-rule "Edit a failure detection rule via the Dynatrace API.") failure detection rule.
* [Change the ID](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/change-id "Change the ID of a failure detection rule via the Dynatrace API.") of a rule.

[### Delete a rule

Delete a failure detection rule you don't need anymore.](/docs/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/delete-rule "Delete a failure detection rule via the Dynatrace API.")

## Related topics

* [Configure service failure detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")


---


## Source: request-attributes-api.md


---
title: Request attributes API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/request-attributes-api
scraped: 2026-02-16T21:13:40.162888
---

# Request attributes API

# Request attributes API

* Reference
* Published Dec 05, 2018

The **Request attributes** API enables you to manage the configuration of [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

[### List all

Get an overview of all request attributes.](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api/get-all "View all request attributes of your environment via the Dynatrace API.")[### View a request attribute

Get parameters of a request attribute by its ID.](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api/get-request-attribute "View a request attribute via the Dynatrace API.")

[### Create a request attribute

Create a new request attribute with the exact parameters you need.](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api/post-request-attribute "Create a request attribute via the Dynatrace API.")[### Edit a request attribute

Update an existing request attribute or create a new request attribute with the specified ID.](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api/put-request-attribute "Update a request attribute via the Dynatrace API.")[### Delete a request attribute

Delete a request attribute you don't need anymore.](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api/del-request-attribute "Delete a request attribute via the Dynatrace API.")

## Related topics

* [Request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")


---
