---
title: Log Monitoring API v2 - POST ingest logs
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs
scraped: 2026-02-20T21:26:56.391694
---

# Log Monitoring API v2 - POST ingest logs

# Log Monitoring API v2 - POST ingest logs

* Reference
* Published May 05, 2021

Pushes custom logs to Dynatrace.

This endpoint is available in your SaaS environment, or as an alternative, you can expose it on an Environmental ActiveGate with the **Log analytics collector** module enabled. This module is enabled by default on all of your ActiveGates.

The request consumes one of the following payload types:

* `text/plain`âlimited to a single log event.
* `application/json`, `application/jsonl`, `application/jsonlines`, `application/jsonlines+json`, `application/x-ndjson`, `application/x-jsonlines`âsupport multiple log events in a single payload.

Be sure to set the correct **Content-Type** header and encode payload with **UTF-8**, for example: `application/json; charset=utf-8`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |

## Authentication

To execute this request, you need an access token with `logs.ingest` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

When using log processing with the custom processing pipeline (OpenPipeline), ingest supports all JSON data types for attribute values. This requires SaaS version 1.295+ when using the SaaS API endpoint or ActiveGate version 1.295+ when using the ActiveGate API endpoint. In all other cases, all ingested values are converted to the string type.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| content-type | string | (Optional) Allows to provide content type with query parameter. Has priority over value provided in Content-Type header. | query | Optional |
| structure | string | (Optional) Data model used for structuring the input into log records. Allowed values: `raw`, `flattened`. For more details, refer to the [documentationï»¿](https://dt-url.net/lyi2yte). The element can hold these values * `raw` * `flattened` | query | Optional |
| X-Dynatrace-Attr | string | (Optional) Contains ampersandâseparated keyâvalue pairs representing additional log attributes to be added to each ingested log record. If the same key appears multiple times, all values are captured as a multiâvalue attribute. Query parameters take precedence over values provided in this header. | header | Optional |
| X-Dynatrace-Options | string | (Optional) Contains ampersand-separated Dynatrace-specific parameters. Query parameter takes precedence over the header value. For more details, refer to the [documentationï»¿](https://dt-url.net/lyi2yte). | header | Optional |
| body | [LogMessageJson](#openapi-definition-LogMessageJson) | The body of the request. Contains one or more log events to be ingested.  The endpoint accepts one of the following payload types, defined by the **Accept** header:  * `text/plain`: supports only one log event. * `application/json`: supports multiple log events in a single JSON array payload. * `application/jsonl`, `application/jsonlines`, `application/x-ndjson`, `application/jsonlines+json`, or `application/x-jsonlines`: supports multiple log events as JSON-lines payload (one JSON object per line). | body | Optional |

### Request body objects

#### The `LogMessageJson` object

A set of one or more log events:

* in JSON format:

  + an array of log events JSON objects, e.g.:

    `[ { "message": "1" }, { "message": "2" } ]`
  + a single log event JSON object, e.g.:

    `{ "message": "1" }`
* in JSON lines format: a sequence of log event JSON objects separated by new lines, e.g.:

  ```
  { "message": "1" }



  { "message": "2" }
  ```

Each log event from the input is mapped to a single Dynatrace log record containing three special attributes: timestamp, loglevel, and content, as well as a map of other attributes. These four properties are set based on keys present in the input JSON object as follows:

* **timestamp**:

  + Set based on the first found key from the following list:

    - `timestamp`
    - `@timestamp`
    - `_timestamp`
    - `eventtime`
    - `date`
    - `published_date`
    - `syslog.timestamp`
    - `time`
    - `epochSecond`
    - `startTime`
    - `datetime`
    - `ts`
    - `timeMillis`
    - `@t`
  + Supported formats: `UTC milliseconds`, `RFC3339`, and `RFC3164`.
  + For unsupported timestamp formats, the current timestamp is used, and the value of the unsupported format is stored in the `unparsed_timestamp` attribute (for Log Monitoring Classic, this attribute isn't indexed).
  + Log events older than the *Log Age* limit are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time. See the **Limitations** section below for details.
  + The default value is the current timestamp and the default timezone is UTC if it's missing in timestamp.
* **loglevel**:

  + Set based on the first found key from the following list:

    - `loglevel`
    - `status`
    - `severity`
    - `level`
    - `syslog.severity`
  + The default value is `NONE`.
* **content**:

  + Set based on the first found key from the following list:

    - `content`
    - `message`
    - `payload`
    - `body`
    - `log`
    - `_raw` (raw data model only)
  + The default value and handling depends on the data model used for processing the input.
* **attributes:**

  + Contains all other keys from the input JSON object except those used for timestamp, loglevel, and content.
  + All attributes should preferably map to **semantic attributes** for Dynatrace to interpret them correctly. See the list of *Supported semantic attribute keys* below. Refer also to the [Semantic Dictionary documentation pageï»¿](https://docs.dynatrace.com/docs/platform/semantic-dictionary) for more details.
  + See the sections below for additional details on attribute processing and limitations.

**Attribute Processing**

Attribute processing differs depending on tenant and environment type:

* Logs on Grail with OpenPipeline custom processing (Dynatrace SaaS version 1.295+, Environment ActiveGate version 1.295+): Supports rich data types, enabling the use of diverse attributes in queries. Keys are case-sensitive.
* Logs on Grail with OpenPipeline routed to Classic Pipeline: All attribute keys are lowercased and all attribute values are stringified. All attributes can be used in queries.
* Log Monitoring Classic: All attribute keys are lowercased and all attribute values are stringified. Custom attributes and semantic attributes can generally be used in queries.

Attribute processing also depends on the data model used for input processing. The effective data model for a specific request depends on the `structure` parameter or the default tenant data model, which is determined by tenant configuration. More details can be found in the [documentationï»¿](https://dt-url.net/lyi2yte).

***Data Model: Raw***

This data model is relevant only for **SaaS** tenants.

1. Attributes with complex (JSON) values are converted to JSON strings. For example:

   *Base JSON:*

   `{"test": {"attribute": {"one": "value 1", "two": "value 2"}}}`

   *Result:*

   `{"test": "{ "attribute": {"one": "value 1", "two": "value 2"}}"}`
2. Content-related behavior:

   * Supported content keys are considered for the special content attribute regardless of their type. If the selected source content attribute (according to the defined priorities) is not a string, it is converted to a string. If it is a complex type, it is converted to a JSON string. For example:

     *Base JSON:*

     `{"message": ["a", 5]}`

     *Result:*

     `{"content": "[\"a\", 5]"}`
   * The selected source content attribute is removed from the attributes map.
   * If no source content attribute is found, the special content attribute is set to an empty string.

***Data Model: Flattened***

For **Managed**, this is the only supported data model.

Complex attribute values are flattened. The following guidelines outline the process:

1. Attributes with complex (JSON) values are flattened, i.e., replaced with keys concatenated using a dot (.) until a simple value is reached in the hierarchy. For example:

   *Base JSON:*

   `{"test": {"attribute": {"one": "value 1", "two": "value 2"}}}`

   *Result:*

   `{"test.attribute.one": "value 1", "test.attribute.two": "value 2"}`
2. Flattening proceeds up to the maximum nesting level specified by the *Nested objects* limit. Attributes nested deeper than this are removed. In such cases, the response code is 200, and the message "Event(s) have attributes that are too nested for records:" is returned along with a list of limited record indexes. See the **Limitations** section below for details.
3. Name conflicts are resolved as follows:

   * In case of a name conflict, where a key is overwritten, it is prefixed with "overwritten". For example:

     *Base JSON:*

     `{"host.name": "abc", "host": {"name": "xyz"}}`

     *Result:*

     `{"host.name": "abc", "overwritten1.host.name": "xyz"}`
   * If a second conflict arises, an index is added starting with 1:

     *Base JSON:*

     `{"service.instance.id": "abc", "service": {"instance.id": "xyz", "instance": {"id": "123"}}}`

     *Result:*

     `{"service.instance.id": "abc", "overwritten1.service.instance.id": "xyz", "overwritten2.service.instance.id": "123"}`
4. Content-related behavior:

   * Supported content keys are considered for the special content attribute (according to the defined priorities) only if they are of type string or a non-null primitive type (such as number or boolean). If the selected source content attribute is not a string, it is converted to a string.
   * The selected source content attribute is removed from the attributes map.
   * If no source content attribute is found, the content attribute is set to the JSON-stringified version of the entire log event.

***Data Model Independent Behavior***

1. Array attribute values are converted to arrays of a uniform type. The target type is chosen according to the following rules:

   * Complex values (such as arrays or objects) are mapped to JSON string values.
   * If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
   * If all values in the source array are numeric, the target array type is numeric.
   * Null values are considered compatible with any type.
2. Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.

**Limitations**

Please refer to the following documentation pages:

* [Grail tenant limitsï»¿](https://docs.dynatrace.com/docs/analyze-explore-automate/logs/lma-limits)
* [LM v2 SaaS tenant limitsï»¿](https://docs.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits)
* [LM v2 Managed tenant limitsï»¿](https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits)

**Supported semantic attribute keys:**

* `audit.action`
* `audit.identity`
* `audit.result`
* `aws.account.id`
* `aws.arn`
* `aws.log_group`
* `aws.log_stream`
* `aws.region`
* `aws.resource.id`
* `aws.resource.type`
* `aws.service`
* `azure.location`
* `azure.resource.group`
* `azure.resource.id`
* `azure.resource.name`
* `azure.resource.type`
* `azure.subscription`
* `cloud.account.id`
* `cloud.availability_zone`
* `cloud.provider`
* `cloud.region`
* `container.image.name`
* `container.image.tag`
* `container.name`
* `db.cassandra.keyspace`
* `db.connection_string`
* `db.hbase.namespace`
* `db.jdbc.driver_classname`
* `db.mongodb.collection`
* `db.mssql.instance_name`
* `db.name`
* `db.operation`
* `db.redis.database_index`
* `db.statement`
* `db.system`
* `db.user`
* `device.address`
* `dt.active_gate.group.name`
* `dt.active_gate.id`
* `dt.code.filepath`
* `dt.code.func`
* `dt.code.lineno`
* `dt.code.ns`
* `dt.ctg.calltype`
* `dt.ctg.extendmode`
* `dt.ctg.gatewayurl`
* `dt.ctg.program`
* `dt.ctg.rc`
* `dt.ctg.requesttype`
* `dt.ctg.serverid`
* `dt.ctg.termid`
* `dt.ctg.transid`
* `dt.ctg.userid`
* `dt.entity.cloud_application`
* `dt.entity.cloud_application_instance`
* `dt.entity.cloud_application_namespace`
* `dt.entity.container_group`
* `dt.entity.container_group_instance`
* `dt.entity.custom_device`
* `dt.entity.host`
* `dt.entity.host_group`
* `dt.entity.kubernetes_cluster`
* `dt.entity.kubernetes_node`
* `dt.entity.process_group`
* `dt.entity.process_group_instance`
* `dt.entity.service`
* `dt.event.group_label`
* `dt.event.key`
* `dt.events.root_cause_relevant`
* `dt.exception.messages`
* `dt.exception.serialized_stacktraces`
* `dt.exception.types`
* `dt.extension.config.id`
* `dt.extension.ds`
* `dt.extension.name`
* `dt.extension.status`
* `dt.host.ip`
* `dt.host.smfid`
* `dt.host.snaid`
* `dt.host_group.id`
* `dt.http.application_id`
* `dt.http.context_root`
* `dt.ingest.debug_messages`
* `dt.ingest.origin`
* `dt.ingest.warnings`
* `dt.kubernetes.cluster.id`
* `dt.kubernetes.cluster.name`
* `dt.kubernetes.config.id`
* `dt.kubernetes.event.involved_object.kind`
* `dt.kubernetes.event.involved_object.name`
* `dt.kubernetes.event.reason`
* `dt.kubernetes.node.name`
* `dt.kubernetes.node.system_uuid`
* `dt.kubernetes.topmost_controller.kind`
* `dt.kubernetes.workload.kind`
* `dt.kubernetes.workload.name`
* `dt.network_zone.id`
* `dt.openpipeline.source`
* `dt.os.description`
* `dt.os.type`
* `dt.process.commandline`
* `dt.process.executable`
* `dt.process.name`
* `dt.security_context`
* `dt.source_entity`
* `dt.source_entity_name`
* `dt.source_entity_type`
* `event.unique_identifier`
* `faas.id`
* `faas.instance`
* `faas.name`
* `faas.version`
* `gcp.instance.id`
* `gcp.instance.name`
* `gcp.project.id`
* `gcp.region`
* `gcp.resource.type`
* `geo.city_name`
* `geo.country_name`
* `geo.name`
* `geo.region_name`
* `host.hostname`
* `host.id`
* `host.image.id`
* `host.image.name`
* `host.image.version`
* `host.name`
* `host.type`
* `http.client_ip`
* `http.flavor`
* `http.host`
* `http.method`
* `http.route`
* `http.scheme`
* `http.server_name`
* `http.status_code`
* `http.status_text`
* `http.target`
* `http.url`
* `journald.unit`
* `k8s.cluster.name`
* `k8s.cluster.uid`
* `k8s.container.name`
* `k8s.cronjob.name`
* `k8s.cronjob.uid`
* `k8s.daemonset.name`
* `k8s.daemonset.uid`
* `k8s.deployment.name`
* `k8s.deployment.uid`
* `k8s.job.name`
* `k8s.job.uid`
* `k8s.namespace.name`
* `k8s.node.name`
* `k8s.pod.name`
* `k8s.pod.uid`
* `k8s.replicaset.name`
* `k8s.replicaset.uid`
* `k8s.service.name`
* `k8s.statefulset.name`
* `k8s.statefulset.uid`
* `k8s.workload.kind`
* `k8s.workload.name`
* `log.source`
* `log.source.origin`
* `net.host.ip`
* `net.host.name`
* `net.host.port`
* `net.peer.ip`
* `net.peer.name`
* `net.peer.port`
* `net.transport`
* `otel.scope.name`
* `process.technology`
* `service.instance.id`
* `service.name`
* `service.namespace`
* `service.version`
* `snmp.trap_oid`
* `span_id`
* `trace_id`
* `winlog.eventid`
* `winlog.keywords`
* `winlog.level`
* `winlog.opcode`
* `winlog.provider`
* `winlog.task`
* `winlog.username`

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
[



{



"content": "Exception: Custom error log sent via Generic Log Ingest",



"log.source": "/var/log/syslog",



"timestamp": "2025-12-17T22:12:31.0000",



"severity": "error",



"custom.attribute": "attribute value",



"complex": {



"key-1": "attribute value-1",



"key-2": 234.2



},



"array.attr": [



"value-1",



1,



null,



true,



[



1,



2,



3



],



{



"key": "value"



}



]



},



{



"message": "User1 logged in successfully",



"log.source": "/var/log/syslog",



"@timestamp": "1765281600"



},



{



"payload": "Exception: Custom error log sent via Generic Log Ingest",



"log.source": "/var/log/syslog"



},



{



"log": "My log message without additional attributes"



}



]
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SuccessEnvelope](#openapi-definition-SuccessEnvelope) | Only a part of input events were ingested due to event invalidity. For details, check the response body. |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **402** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. This is due either to the status of your licensing agreement or because you've exhausted your [DPS licenseï»¿](https://www.dynatrace.com/support/help/shortlink/dynatrace-platform-subscription). |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. This may happen when no ActiveGate is available with the Log Analytics Collector module enabled. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Request payload size is too big. This may happen when the payload byte size exceeds the limit or when the ingested payload is a JSON array with the size exceeding the limit. |
| **429** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Too Many Requests. This may happen when ActiveGate is unable to process more requests at the moment or when log ingest is disabled. Retryable with exponential backoff strategy. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The server either does not recognize the request method, or it lacks the ability to fulfil the request. In Log Monitoring Classic, this may happen when indexed log storage is not enabled. |
| **502** | - | Failed. Bad Gateway. This may happen if an intermediate system (e.g., ActiveGate or a proxy) encounters an issue while forwarding the request. Retryable with exponential backoff strategy. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The server is currently unable to handle the request. This may happen when ActiveGate is overloaded. Retryable with exponential backoff strategy. |
| **504** | - | Failed. Gateway Timeout. This may occur due to an issue in the underlying infrastructure causing a delay in processing the request. Retryable with exponential backoff strategy. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SuccessEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| details | [Success](#openapi-definition-Success) | - |

#### The `Success` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| message | string | Detailed message |

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



"details": {



"code": 1,



"message": "string"



}



}
```

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

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")