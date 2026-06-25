---
title: Prometheus data source reference
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference
scraped: 2026-05-12T12:08:18.392397
---

# Prometheus data source reference

# Prometheus data source reference

* Reference
* 13-min read
* Updated on Nov 10, 2025

This is a general description of Prometheus data source-based extension YAML file and ways to declare metrics and dimensions you would like to collect using your extension.

## Data scope

Create an inventory of Prometheus endpoints you'd like to reference in your extension, as well as metrics and dimension values.

In our example, we create a simple extension collecting Rabbit MQ metrics.

```
name: com.dynatrace.extension.prometheus-rabbitmq



version: 1.0.0



minDynatraceVersion: '1.236'



author:



name: Dynatrace



dashboards:



- path: 'dashboards/dashboard_exporter.json'



alerts:



- path: 'alerts/alert_socket_usage.json'



# Extension based on official rabbitmq prometheus exporter available metrics



# list of metrics visible here https://github.com/rabbitmq/rabbitmq-server/blob/master/deps/rabbitmq_prometheus/metrics.md



prometheus:



- group: rabbitmq metrics



interval:



minutes: 1



featureSet: all



dimensions:



- key: rabbitmq



value: const:rabbitmq



subgroups:



# global counters



- subgroup: rabbitmq global counter



dimensions:



- key: global_counters



value: const:global_counters



metrics:



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_acknowledged_total



value: metric:rabbitmq_global_messages_acknowledged_total



type: count



featureSet: global



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_confirmed_total



value: metric:rabbitmq_global_messages_confirmed_total



type: count



featureSet: global



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_delivered_consume_auto_ack_total



value: metric:rabbitmq_global_messages_delivered_consume_auto_ack_total



type: count



featureSet: global
```

Your Prometheus monitoring scope definition starts with the `prometheus` YAML node. All the settings under the node pertain to the declared [data source type](/managed/ingest-from/extensions/concepts#data-source-type "Learn more about the concept of Dynatrace Extensions.") (in this case, Prometheus).

## Dimensions

For each level (group, subgroup), you can define up to 25 dimensions (which gives you a total of 50 dimensions per metric).

### Dimension key

The dimension key string must conform to the [metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

### Dimension value

You can use the following methods to define dimensions for your metrics:

* Plain text. Prefix with `const:` or simply add the required text

  ```
  dimensions:



  - key: extension.owner



  value: const:Joe.Doe@somedomain.com
  ```

  or

  ```
  dimensions:



  - key: extension.owner



  value: Joe.Doe@somedomain.com
  ```
* [Prometheus labelï»¿](https://prometheus.io/docs/practices/naming/#metric-and-label-naming)

  ```
  dimensions:



  - key: customdimension.job



  value: label:job



  filter: const:$eq(prometheus)
  ```

  All the labels exposed by Prometheus are created as dimensions automatically. You only need to explicitly define a label-based dimension if you want to:

  + apply filtering on the values,
  + define a custom dimension key.

### Filter extracted metric lines

When extracting metric lines, you can add filtering logic that will result in reporting only the lines for which the dimension value matches the filtering criteria.

Define the filter based on a condition as follows:

* **Starts with** â use a `const:$prefix` qualifier. Example:

  ```
  filter: const:$prefix(xyz)
  ```
* **Ends with** â use a `const:$suffix` qualifier. Example:

  ```
  filter: const:$suffix(xyz)
  ```
* **Contains** â use a `const:$contains` qualifier. Example:

  ```
  filter: const:$contains(xyz)
  ```
* **Equals** â use a `const:$eq` qualifier. Example:

  ```
  filter: const:$eq(xyz)
  ```

  For the expressions mentioned above, you can also use qualifiers:

  + `const:$and` â to chain two or more expressions with AND operator. Example:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + a `const:$or` â to chain two or more expressions with OR operator. Example:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + a `const:$not` â to negate an expression. Example:

    ```
    filter: const:$not(<expr>)
    ```

You can create complex filters by combining two or more filters separated by commas using logical expressions:

```
dimensions:



- key: technology



value: other



- key: job



value: label:job



filter: const:$or($eq(),$not($or($eq(prometheus),$eq(rabbitmq-server),$eq(redis_exporter),$eq(node_exporter)))
```

## Metrics

For each level (group, subgroup), you can define up to 100 metrics. Note, however, that there is a hard limit of 1,000 metrics per extension applied at runtime. This limit is lower than the combined limits of allowed groups and subgroups.

For example:

```
prometheus:



- group: rabbitmq metrics



interval: 1m



featureSet: all



dimensions:



- key: instance



value: $reference(metric:rabbitmq_identity_info, ref:rabbitmq_node)



subgroups:



# global counters



- subgroup: rabbitmq global counter



metrics:



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_acknowledged_total



value: metric:rabbitmq_global_messages_acknowledged_total



type: count



featureSet: global



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_confirmed_total



value: metric:rabbitmq_global_messages_confirmed_total



type: count



featureSet: global
```

### Metric key

The metric key string must conform to the [metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

For Dynatrace versions 1.215 and 1.217, a metric node requires the `id` parameter in place of `key`. Starting with Dynatrace version 1.219, we recommend that you use the `key` parameter, as `id` will be deprecated.

#### Best practices for metric keys

The metrics you ingest into Dynatrace using your extension are just some of the thousands of metrics, built-in and custom, processed by Dynatrace. To make your metrics keys unique and easy to identify in Dynatrace, the best practice is to prefix the metric name with the extension name. This guarantees that the metric key is unique and you can easily appoint a metric to a particular extension in your environment.

### Metric value

The Prometheus metric key from which you want to extract the metric value prefixed with `metric:`.

### Type

The Dynatrace Extensions framework supports all original Prometheus metric payload formats. For details, see [Metric payload](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Learn how the data ingestion protocol for Dynatrace Metrics API works."). To indicate the metric type, use the `type` attribute.

| Prometheus exposed type | Dynatrace ingest |
| --- | --- |
| [Counterï»¿](https://dt-url.net/hq634n9) | `count` |
| [Gaugeï»¿](https://dt-url.net/a2434zx) | `gauge` |
| [Histogramï»¿](https://dt-url.net/5x034gl) | **Note**: The [timeseries percentile](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") is only available to DPS customers with the **Metrics powered by Grail** rate card. The function calculates the requested percentile of the expression value in each bucket, so it naturally used with histograms.  * Count part as `<metric-key>_count` * Total sum part as `<metric-key>_sum.count` * Individual buckets split by the `le` dimension indicating the bucket identifier as `<metric-key>_bucket.count`  Individual bucket metrics ingestion is disabled by default. For details on how to enable it, refer to the [advanced extension monitoring configuration description](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#advanced "Learn about Prometheus extensions in the Extensions framework."). Histogram code samples A standard Prometheus histogram metric includes:  * `HELP` and `TYPE` * Bucket data and summary metrics for `sum` and `count`  ```  # HELP http_response_time_seconds Time to respond to request  # TYPE http_response_time_seconds histogram  http_response_time_seconds_bucket{code="200",method="GET",path="/banners/post-auth",service="platform",le="0.005"} 1  ...  http_response_time_seconds_sum{code="404",method="POST",path="/revoke",service="platform"} 0.016945976  http_response_time_seconds_count{code="404",method="POST",path="/revoke",service="platform"} 1 ```  You can define metric metadata in the `extensions.yaml` file as shown below:  ```  metrics:  - key: http_response_time_seconds_count  metadata:  displayName: HTTP response time (Histogram count of observed events)  description: Time to respond to request  - key: http_response_time_seconds_sum.count  metadata:  displayName: HTTP response time (Histogram total sum of all observed values)  description: Time to respond to request  unit: Second  - key: http_response_time_seconds_bucket.count  metadata:  displayName: HTTP response time (Histogram buckets split by le)  description: Time to respond to request  unit: Second ```  To ingest histogram metrics in the Prometheus data source section of the `extensions.yaml` file:  * Use the base name of the metric without any summary suffix * Specify the type as `histogram`  ```  prometheus:  - group: CipherTrust Metrics  subgroups:  - subgroup: HTTP Traffic  featureSet: HTTP_Traffic  metrics:  - key: http_response_time_seconds  value: metric:http_response_time_seconds  type: histogram ``` |
| [Summaryï»¿](https://dt-url.net/7g234n1) | * Count part as `<metric-key>_count` * Total sum part as `<metric-key>_sum.count` * Individual quantiles split by the quantile dimension indicating the quantile as `<metric-key>` |

## Metric metadata

An Extension can define metadata for each metric available in Dynatrace. For example, you might want to add the metric display name and the unit, both of which can be used for filtering in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

Define all metric metadata in the `metrics` section of the extension's YAML file to ensure it's correctly associated with the metric configuration.

```
name: custom:example-extension-name



version: 1.0.0



minDynatraceVersion: "1.236"



author:



name: Dynatrace



metrics:



- key: your.metric.name



metadata:



displayName: Display name of the metric visible in Metrics browser



unit: Count
```

## Feature set

Feature sets are categories into which you organize the data collected by the extension. You can define feature sets at the group, subgroup, or metric level. In this example, we create a Prometheus extension collecting application and network metrics. This is reflected by metrics organization into related feature sets `prometheus_app_metrics` and `prometheus_net_metrics`.

```
prometheus:



- group: prometheus metrics



interval: 1m



metrics:



- key: com.dynatrace.extension.prometheus.app



value: prometheus.app



featureSet: prometheus_app_metrics



- key: com.dynatrace.extension.prometheus.net



value: prometheus.net



featureSet: prometheus_net_metrics
```

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

## Interval

The interval at which the data measurement will be taken. You can define intervals at the group, subgroup, or individual metric level. You can define intervals with the granularity of one minute. The maximum interval is 2880 minutes (2 days, 48 hours).

Setting the interval is not possible for JMX data sources.

For example:

```
interval:



minutes: 5
```

The above format is supported starting with schema version 1.217. For earlier schema versions, use the following format (supported up to schema version 1.251):

```
interval: 5m
```

```
prometheus:



- group: prometheus metrics



interval: 1m



dimensions:



- key: technology



value: prometheus



metrics:



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_delivered_get_auto_ack_total



value: metric:rabbitmq_global_messages_delivered_get_auto_ack_total



type: count
```

A metric inherits the interval of a subgroup, which in turn inherits the interval of a group. Also, the interval defined on the metric level overrides the interval defined on the subgroup level, which in turn overrides the interval defined on the group level.

## Monitoring configuration

After you define the scope of your configuration, you need to identify the Prometheus endpoints from which to collect data.

The monitoring configuration is a JSON payload defining the connection details, credentials, and feature sets that you want to monitor. For details, see [Start monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Example payload to activate a Prometheus extension:

```
[



{



"scope": "ag_group-default",



"value": {



"version": "1.0.0",



"description": "name",



"enabled": true,



"activationContext": "REMOTE",



"prometheusRemote": {



"endpoints": [



{



"url": "https://myPrometheusServer/metrics",



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



}



"autoDiscovery": [



{



"autoDiscoveryType": "dns_sd_config",



"dnsType": "a",



"dnsPort": 1111,



"refreshInterval": "30"



}



]



}



]



},



"featureSets": [



"myFeatureSet"



]



}



}



]
```

When you have your initial extension YAML ready, package it, sign it, and upload it to your Dynatrace environment. For details, see [Manage extension lifecyle](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

The Dynatrace Hub-based extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration.

You can also use the Dynatrace API to download the schema for your extension that will help you create the JSON payload for your monitoring configuration.

Use the [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint.

Issue the following request:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Make sure to replace `{extension-name}` and `{extension-version}` with values from your extension YAML file. A successful call returns the JSON schema.

### Scope

Note that each OneAgent or ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

For a remote extension, the scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.

#### Local extension

For a local extension, the scope is a host, host group, or management zone for which you will execute the extension. You can also select to monitor your whole environment (optionally, limited by tags).

* When defining a host as the scope, use this format:

  ```
  "scope": "<HOST_ID>",
  ```

  Replace `<HOST_ID>` with the entity ID of the host as in this example:

  ```
  "scope": "HOST-A1B2345678C9D001",
  ```
* When defining a host group as the scope, use this format:

  ```
  "scope": "HOST_GROUP-<HOST_GROUP_ID>",
  ```

  Replace `<HOST_GROUP_ID>` with the entity ID of the host group as in this example:

  ```
  "scope": "HOST_GROUP-AB123C4D567E890",
  ```

  You can find the host group ID on the [host group settings page](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") URL. For example:

  ```
  https://{your-environment-id}.live.dynatrace.com/#settings/hostgroupconfiguration;id=HOST_GROUP-AB123C4D567E890;hostGroupName=my-host-group
  ```
* When defining a management zone as the scope, use this format:

  ```
  "scope": "management_zone-<MANAGEMENT-ZONE>",
  ```

  Replace `<MANAGEMENT-ZONE>` with the management zone name as in this example:

  ```
  "scope": "management_zone-sampleManagementZone",
  ```

  You can find the management zone on the [**Management zones settings** page](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Apply management zones to organize your Dynatrace environment and control user access to specific data.").
* When defining an environment as the scope, use this format:

  ```
  "scope": "environment",
  ```

  You can also add tags to filter the hosts this configuration will run on:

  ```
  "activationTags": [



  "dt.owner:lama"



  ]
  ```

If you activate a local Prometheus extension and define the [endpoint](#url) of a Prometheus Server running on the same host, the metrics gathered from that server may come from various endpoints, not only from the endpoint on that host, but all the metrics will be enriched with the OneAgent-installed host context.

### Version

The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Description

A human-readable description of the specifics of this monitoring configuration.

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Activation context

* For remote extensions, set `activationContext` to `REMOTE`
* For local extensions, set `activationContext` to `LOCAL`

### URL

The URL is the Prometheus endpoint from which your extension pulls the metrics. The maximum URL length is 500 characters.

* For local extensions, define the Prometheus endpoint in the `prometheusLocal` node.
* For remote extensions, define the Prometheus endpoint in the `prometheusRemote` node.

You can define the following endpoint types:

* `/metrics` â returns metrics in plain text Prometheus format.
* `/api/v1/` â API path that could be followed directly by a `query` or `metadata` endpoint.

If you gather the same metrics from different endpoints (either Prometheus server or data exporter), some metrics could be overwritten, as the keys would be identical regardless of the endpoint. To avoid this, we automatically add an extra `activation_endpoint` dimension to each metric.

### Authentication

Authentication details passed to Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

#### No authentication

By default, supported only for HTTP endpoints.

```
"authentication": {



"scheme": "none"



}
```

#### Bearer

Bearer authentication requires the token only.

```
"authentication": {



"scheme": "bearer",



"token": "myToken"



}
```

#### Basic

Basic authentication requires only a username and password.

```
"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



}
```

#### AWS - requires AWS access key, secret key, and region.

AWS authentication requires AWS access key, secret key, and region.

```
"authentication": {



"scheme": "aws",



"accessKey": "accessKey",



"secretKey": "secretKey",



"region": "us-east-2"



}
```

If you try to use an HTTP endpoint with a bearer, basic, or AWS schema, the extension framework throws an error to avoid sending sensitive data over an unsafe connection. If, however, you're sure you can do so, set the `skipVerifyHttps` property to `true`.

```
"authentication": {



"scheme": "basic",



"username": "user",



"password": "password",



"skipVerifyHttps": "true"



}
```

#### Credential vault

Remote monitoring only

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"skipVerifyHttps": false,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

For SSL communication between Prometheus and Prometheus exporters, the certificate from the Prometheus host must be added to the operating system trust store on the ActiveGate machines running the extension.

Refer to your operating system-specific documentation on how to add certificate to your operating system trust store.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Advanced

Optionally, you can define advanced settings controlling the HTTP connection to your Prometheus endpoints:

* `timeoutSecs`  
  An integer between 0 and 50. The number of seconds to wait for a response from the Prometheus endpoint.
* `retries`  
  The number of connection retries. The maximum number of retries is 3.
* `collectHistogramBuckets`  
  Enable or disable ingestion of [Prometheus histogram metrics buckets](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#type "Learn about Prometheus extensions in the Extensions framework.").

It is possible to have a maximum of 3 connection retries of 50 seconds each.

Make sure the total waiting time is never longer than the [interval](#interval) you set for your metrics.

### Auto Discovery

Remote monitoring only

Autodiscovery is a feature that automatically resolves the DNS endpoints. If autodiscovery is defined, the URL becomes the DNS name.

```
"configuration": [



{



"configurationType": "dns_sd_config",



"dnsType": "a",



"dnsPort": 1111,



"refreshInterval": "30m"



}



]
```

* **Auto discovery type**: Only the `DNS` type available.
* **DNS type**: The type of DNS query to perform. Only the `A` type is available, which corresponds to IPv4 addresses.
* **DNS port**: Specifies the port assigned to all IPs resolved by the DNS.
* **DNS refresh interval (s)**: Sets interval time in seconds to the frequently changing IP addresses.

## Resource consumption

Resource consumption depends on the number of Prometheus endpoints. The first endpoint consumes 25 MB of RAM and 0.2%â0.5% of CPU. Every following endpoint consumes 0.5 MB of RAM and ~0.2% of CPU.

| Endpoints | Average CPU | Max CPU | RAM (MB) | Host (EC2 instance type) |
| --- | --- | --- | --- | --- |
| 100 | 1.0% | 2.5% (spike at beginning) | 60 | XS (`c5.large`) |
| 1 | 0.2% | 0.5% (spike at beginning) | 25 | XS (`c5.large`) |