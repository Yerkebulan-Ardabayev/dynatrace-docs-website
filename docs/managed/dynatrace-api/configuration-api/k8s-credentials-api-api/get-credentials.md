---
title: Kubernetes credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-credentials
---

# Kubernetes credentials API - GET credentials

# Kubernetes credentials API - GET credentials

* Reference
* Published Jul 22, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:cloud.kubernetes`) and the [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`) schemas instead.

Gets the configuration of the specified Kubernetes credentials.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required Kubernetes credentials configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [KubernetesCredentials](#openapi-definition-KubernetesCredentials) | Success |

### Response body objects

#### The `KubernetesCredentials` object

Configuration for specific Kubernetes credentials.

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | The monitoring is enabled (`true`) or disabled (`false`) for given credentials configuration.  If not set on creation, the `true` value is used.  If the field is omitted during an update, the old value remains unaffected. |
| activeGateGroup | string | Active Gate group to filter active gates for this credentials. |
| authToken | string | The service account bearer token for the Kubernetes API server.  Submit your token on creation or update of the configuration. For security reasons, GET requests return this field as `null`.  If the field is omitted during an update, the old value remains unaffected. |
| certificateCheckEnabled | boolean | The check of SSL certificates is enabled (`true`) or disabled (`false`) for the Kubernetes cluster.  If not set on creation, the `true` value is used.  If the field is omitted during an update, the old value remains unaffected. |
| davisEventsIntegrationEnabled | boolean | Inclusion of all Davis relevant events is enabled (`true`) or disabled (`false`) for the Kubernetes cluster. If the field is omitted during an update, the old value remains unaffected. |
| endpointStatus | string | The status of the configured endpoint.  ASSIGNED: The credentials are assigned to an ActiveGate which is responsible for processing. UNASSIGNED: The credentials are not yet assigned to an ActiveGate so there is currently no processing. DISABLED: The credentials have been disabled by the user. FASTCHECK\_AUTH\_ERROR: The credentials are invalid. FASTCHECK\_TLS\_ERROR: The endpoint TLS certificate is invalid. FASTCHECK\_NO\_RESPONSE: The endpoint did not return a result until the timeout was reached. FASTCHECK\_INVALID\_ENDPOINT: The endpoint URL was invalid. FASTCHECK\_AUTH\_LOCKED: The credentials seem to be locked. UNKNOWN: An unknown error occured. The element can hold these values * `ASSIGNED` * `DISABLED` * `FASTCHECK_AUTH_ERROR` * `FASTCHECK_AUTH_LOCKED` * `FASTCHECK_INVALID_ENDPOINT` * `FASTCHECK_LOW_MEMORY_ERROR` * `FASTCHECK_MISCONFIGURED_AWS_ROLE` * `FASTCHECK_MISSING_AWS_ROLE` * `FASTCHECK_NO_RESPONSE` * `FASTCHECK_TLS_ERROR` * `FASTCHECK_TOO_BIG_ENVIRONMENT` * `FASTCHECK_TOO_MANY_SUBSCRIPTIONS` * `UNASSIGNED` * `UNKNOWN` |
| endpointStatusInfo | string | The detailed status info of the configured endpoint. |
| endpointUrl | string | The URL of the Kubernetes API server.  It must be unique within a Dynatrace environment.  The URL must valid according to RFC 2396. Leading or trailing whitespaces are not allowed. |
| eventAnalysisAndAlertingEnabled | boolean | [Deprecated] With 1.240 the EA events monitoring has been deprecated and replaced by the events GA version which obsoletes this property.  Corresponds to the value of `eventsIntegrationEnabled`.  The field is ignored during an update, the old value remains unaffected. |
| eventsFieldSelectors | [KubernetesEventPattern](#openapi-definition-KubernetesEventPattern)[] | Kubernetes event filters based on field-selectors. If set to `null` on creation, no events field selectors are subscribed. If set to `null` on update, no change of stored events field selectors is applied. Set an empty list to clear all events field selectors. |
| eventsIntegrationEnabled | boolean | The monitoring of events is enabled (`true`) or disabled (`false`) for the Kubernetes cluster. Event monitoring depends on the active state of this configuration to be true.  If not set on creation, the `false` value is used.  If the field is omitted during an update, the old value remains unaffected. |
| id | string | The ID of the given credentials configuration. |
| label | string | The name of the Kubernetes credentials configuration.  Allowed characters are letters, numbers, whitespaces, and the following characters: `.+-_`. Leading or trailing whitespace is not allowed. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| prometheusExportersIntegrationEnabled | boolean | Prometheus exporters integration is enabled (`true`) or disabled (`false`) for the Kubernetes cluster. If the field is omitted during an update, the old value remains unaffected. |
| workloadIntegrationEnabled | boolean | Workload and cloud application processing is enabled (`true`) or disabled (`false`) for the Kubernetes cluster. If the field is omitted during an update, the old value remains unaffected. |

#### The `KubernetesEventPattern` object

Represents a single Kubernetes events field selector (=event filter based on the K8s field selector).

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | Whether subscription to this events field selector is enabled (value set to `true`). If disabled (value set to `false`), Dynatrace will stop fetching events from the Kubernetes API for this events field selector |
| fieldSelector | string | The field selector string (url decoding is applied) when storing it. |
| label | string | A label of the events field selector. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

### Response body JSON models

```
{



"active": true,



"activeGateGroup": "group-1",



"authToken": "abcd9876",



"certificateCheckEnabled": true,



"davisEventsIntegrationEnabled": true,



"endpointUrl": "https://k8s-api.sample.org",



"eventAnalysisAndAlertingEnabled": true,



"eventsFieldSelectors": [



{



"active": true,



"fieldSelector": "involvedObject.kind=Node",



"label": "Node events"



}



],



"eventsIntegrationEnabled": true,



"hostnameVerificationEnabled": true,



"id": "KUBERNETES_CLUSTER-CC06304728FC9396",



"label": "K8s credentials - REST example",



"prometheusExportersIntegrationEnabled": true,



"workloadIntegrationEnabled": true



}
```

## Related topics

* [Explore Kubernetes in Dynatrace Hub﻿](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)