# Dynatrace Documentation: analyze-explore-automate/metrics

Generated: 2026-02-17

Files combined: 6

---


## Source: built-in-metrics-on-grail.md


---
title: Built-in Metrics on Grail
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/built-in-metrics-on-grail
scraped: 2026-02-17T21:26:34.831577
---

# Built-in Metrics on Grail

# Built-in Metrics on Grail

* Latest Dynatrace
* Reference
* 39-min read
* Updated on Feb 10, 2026

Metrics on Grail supports many of the existing [built-in metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.") as identified below.

The expandable sections below describe differences in built-in metrics on Grail when compared to similar Metrics Classic metrics.

Renamed metric keys

Metrics on Grail introduces guidelines to improve clarity, consistency, and readability for Dynatrace-provided metrics, dimensions, and entities across the Dynatrace Platform:

* Replacing the `builtin:` prefix with `dt.` to clearly denote Dynatrace-provided metrics and entities.
* Preferring snake case (`capacity_units`) to camel case (`capacityUnits`) to improve readability.
* Improving specificity to reflect underlying measurements.

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.uptime | builtin:host.uptime |
| dt.host.disk.used.percent | builtin:host.disk.usedPct |
| dt.process.network.sessions.reset\_local | builtin:tech.generic.network.sessions.resetLocal |

New and missing metric keys

By taking advantage of the improved scalability in Grail, it's no longer necessary to split, distribute, or pre-aggregate your data.

The Metrics Classic metric `builtin:host.net.bytesRx` represents bytes received by hosts in your environment, measured in bytes per second. It's a pre-aggregated metric based on `builtin:host.net.nic.bytesRx`, which measures bytes received by host-network interface pairs. Pre-aggregating the metric helps you to optimize queries and helps classic metrics distribute query load.

Consequently, the following two metric selectors return equivalent results with Metrics Classic metrics, but the query on `builtin:host.net.bytesRx` is faster (especially in large environments) because the host-level aggregation has already taken place.

```
// queries pre-aggregated host-level data



builtin:host.net.bytesRx:splitBy("dt.entity.host"):avg
```

```
// queries host- and network interface-level data



builtin:host.net.nic.bytesRx:splitBy("dt.entity.host"):avg
```

Grail, however, is already optimized for such high cardinality queries. Since the pre-aggregated metric `builtin:host.net.bytesRx` is no longer necessary, only `builtin:host.net.nic.bytesRx` is supported by metrics on Grail, and it can be queried as

```
timeseries avg(dt.host.net.nic.bytes_rx), by:{dt.entity.host}
```

Querying extension metrics in Grail

There are three kinds of Metrics Classic extension metrics to consider:

1. Extensions with a `builtin:tech` prefix
2. Extensions with an `ext:` prefix
3. Extensions with no common prefix

For details, see below.

#### Type 1: Extension metrics with the `builtin:tech` prefix

[Extension 1.0](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") metrics appear in Metrics Classic metrics with the prefix `builtin:tech`. These metrics appear in Grail instead with a `legacy` prefix. For example:

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| legacy.cassandra.KeyCache.Hit.Rate | builtin:tech.cassandra.KeyCache.Hit.Rate |

This renaming applies to all [Extension 1.0](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") metrics with the prefix `builtin:tech`, except for the following:

* [Generic process metrics](#processes), including all metrics with the prefix `builtin:tech.generic`.
* [WebSphere metrics](#websphere-application-server), including all metrics with the prefix `builtin:tech.websphere`.

This renaming does not apply to Metrics Classic technology metrics, which can be upgraded to Grail [runtime metrics](#runtimes), including metrics prefixed with `builtin:tech.jvm`, `builtin:tech.go`, and more.

#### Type 2: Extension metrics with the `ext:` prefix

Extension metrics with the `ext:` prefix are either provided by OneAgent or ActiveGate extensions, or are [classic metrics for AWS integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.").
Regardless of the source, they behave the same way.

These can be found in Grail according to the following renaming rules:

1. Remove the `ext:` prefix.
2. Convert `camelCase` to `snake_case`.

As shown in the following examples, snake case renaming depends on the context. AWS's `route53resolver` and other components are proper nouns and are not renamed:

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| cloud.aws.dx.connection\_error\_count | ext:cloud.aws.dx.connectionErrorCount |
| cloud.aws.route53resolver.inbound\_query\_volume\_sum | ext:cloud.aws.route53resolver.inboundQueryVolumeSum |

#### Type 3: Extension metrics with no common prefix

These have no special renaming and can be queried as is in many cases.

```
cloud.gcp.cloudfunctions_googleapis_com.function.active_instances:splitBy():avg
```

```
timeseries avg(cloud.gcp.cloudfunctions_googleapis_com.function.active_instances)
```

Extension metrics with [special characters](/docs/platform/grail/dynatrace-query-language/dql-reference#field-naming-rules "Dynatrace Query Language syntax reference.") are an exception. Escape these metrics with backticks (``` `` ```) to use them in DQL.

```
com.dynatrace.extension.snmp-generic-cisco-device.cpm.cpu.loadavg."5min":splitBy():avg
```

```
timeseries avg(`com.dynatrace.extension.snmp-generic-cisco-device.cpm.cpu.loadavg.5min`)
```

Querying custom metrics on Grail

If you can't find your custom metric in Grail, try querying your metric key without the `.count` suffix.

You can query custom metrics with both [metric selectors](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") and DQL. However, your custom metric key might have a different name in DQL queries. For example, if you ingest a count metric with the `coffees.brewed` key, as shown below using the [metric ingest protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

```
coffees.brewing count,delta=2
```

Dynatrace creates and stores two metrics:

* Classic metric `coffees.brewing.count`
* Grail metric `coffees.brewing`

You can query the Grail metric via DQL using the original metric key:

```
timeseries sum(coffees.brewing)
```

This is different from Metrics Classic, [which automatically appends count metrics with the `.count` suffix](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#format "Learn how the data ingestion protocol for Dynatrace Metrics API works."). You still need to use the `coffees.brewing.count` metric key to query the Metrics Classic metric.

```
coffees.brewing.count:splitBy():value
```

Querying calculated metrics in Grail

While [calculated service metrics](#calc-service) are supported, other calculated metrics are not yet supported on Grail.

* [Calculated RUM metrics](/docs/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") (metrics with the prefix `calc:apps`) are not supported on Grail.
* Calculated Log v1 metrics (metrics with the prefix `calc:log`) are not supported on Grail. See [Upgrade Log Monitoring Classic to Log Management and Analytics](/docs/analyze-explore-automate/logs/logs-upgrade/logs-upgrade-to-lma "Log Management and Analytics is the latest Dynatrace log monitoring solution. We encourage you to upgrade to this latest log monitoring offer.").

## Billing

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.billing.foundation\_and\_discovery.usage | builtin:billing.foundation\_and\_discovery.usage |
| dt.billing.full\_stack\_monitoring.usage | builtin:billing.full\_stack\_monitoring.usage |
| dt.billing.infrastructure\_monitoring.usage | builtin:billing.infrastructure\_monitoring.usage |
| dt.billing.runtime\_application\_protection.usage | builtin:billing.runtime\_application\_protection.usage |
| dt.billing.runtime\_vulnerability\_analytics.usage | builtin:billing.runtime\_vulnerability\_analytics.usage |

## Cloud

### AWS

Which Metrics Classic AWS metrics are not supported on Grail?

* builtin:cloud.aws.cloudwatch.asg.errors.connect
* builtin:cloud.aws.cloudwatch.asg.errors.lostData
* builtin:cloud.aws.cloudwatch.asg.errors.notauth
* builtin:cloud.aws.cloudwatch.asg.errors.service
* builtin:cloud.aws.cloudwatch.asg.errors.throttling
* builtin:cloud.aws.cloudwatch.asg.number
* builtin:cloud.aws.cloudwatch.az.errors.connect
* builtin:cloud.aws.cloudwatch.az.errors.lostData
* builtin:cloud.aws.cloudwatch.az.errors.notauth
* builtin:cloud.aws.cloudwatch.az.errors.service
* builtin:cloud.aws.cloudwatch.az.errors.throttling
* builtin:cloud.aws.cloudwatch.az.number
* builtin:cloud.aws.cloudwatch.beanstalk.errors.connect
* builtin:cloud.aws.cloudwatch.beanstalk.errors.lostData
* builtin:cloud.aws.cloudwatch.beanstalk.errors.notauth
* builtin:cloud.aws.cloudwatch.beanstalk.errors.service
* builtin:cloud.aws.cloudwatch.beanstalk.errors.throttling
* builtin:cloud.aws.cloudwatch.beanstalk.number
* builtin:cloud.aws.cloudwatch.billing
* builtin:cloud.aws.cloudwatch.cloudwatch.errors.connect
* builtin:cloud.aws.cloudwatch.cloudwatch.errors.lostData
* builtin:cloud.aws.cloudwatch.cloudwatch.errors.notauth
* builtin:cloud.aws.cloudwatch.cloudwatch.errors.service
* builtin:cloud.aws.cloudwatch.cloudwatch.errors.throttling
* builtin:cloud.aws.cloudwatch.cloudwatch.latedata
* builtin:cloud.aws.cloudwatch.dynamoDb.errors.connect
* builtin:cloud.aws.cloudwatch.dynamoDb.errors.lostData
* builtin:cloud.aws.cloudwatch.dynamoDb.errors.notauth
* builtin:cloud.aws.cloudwatch.dynamoDb.errors.service
* builtin:cloud.aws.cloudwatch.dynamoDb.errors.throttling
* builtin:cloud.aws.cloudwatch.dynamoDb.number
* builtin:cloud.aws.cloudwatch.ebs.api.failed
* builtin:cloud.aws.cloudwatch.ebs.api.ok
* builtin:cloud.aws.cloudwatch.ebs.errors.connect
* builtin:cloud.aws.cloudwatch.ebs.errors.lostData
* builtin:cloud.aws.cloudwatch.ebs.errors.notauth
* builtin:cloud.aws.cloudwatch.ebs.errors.service
* builtin:cloud.aws.cloudwatch.ebs.errors.throttling
* builtin:cloud.aws.cloudwatch.ebs.number
* builtin:cloud.aws.cloudwatch.ec2.api.failed
* builtin:cloud.aws.cloudwatch.ec2.api.ok
* builtin:cloud.aws.cloudwatch.ec2.errors.connect
* builtin:cloud.aws.cloudwatch.ec2.errors.lostData
* builtin:cloud.aws.cloudwatch.ec2.errors.notauth
* builtin:cloud.aws.cloudwatch.ec2.errors.service
* builtin:cloud.aws.cloudwatch.ec2.errors.throttling
* builtin:cloud.aws.cloudwatch.ec2.number
* builtin:cloud.aws.cloudwatch.elb.api.failed
* builtin:cloud.aws.cloudwatch.elb.api.ok
* builtin:cloud.aws.cloudwatch.elb.errors.connect
* builtin:cloud.aws.cloudwatch.elb.errors.lostData
* builtin:cloud.aws.cloudwatch.elb.errors.notauth
* builtin:cloud.aws.cloudwatch.elb.errors.service
* builtin:cloud.aws.cloudwatch.elb.errors.throttling
* builtin:cloud.aws.cloudwatch.elb.number
* builtin:cloud.aws.cloudwatch.lambda.errors.connect
* builtin:cloud.aws.cloudwatch.lambda.errors.lostData
* builtin:cloud.aws.cloudwatch.lambda.errors.notauth
* builtin:cloud.aws.cloudwatch.lambda.errors.service
* builtin:cloud.aws.cloudwatch.lambda.errors.throttling
* builtin:cloud.aws.cloudwatch.lambda.number
* builtin:cloud.aws.cloudwatch.polling.failures
* builtin:cloud.aws.cloudwatch.polling.infrastructure
* builtin:cloud.aws.cloudwatch.polling.metrics
* builtin:cloud.aws.cloudwatch.rds.api.failed
* builtin:cloud.aws.cloudwatch.rds.api.ok
* builtin:cloud.aws.cloudwatch.rds.errors.connect
* builtin:cloud.aws.cloudwatch.rds.errors.lostData
* builtin:cloud.aws.cloudwatch.rds.errors.notauth
* builtin:cloud.aws.cloudwatch.rds.errors.service
* builtin:cloud.aws.cloudwatch.rds.errors.throttling
* builtin:cloud.aws.cloudwatch.rds.number
* builtin:cloud.aws.cloudwatch.s3.errors.connect
* builtin:cloud.aws.cloudwatch.s3.errors.lostData
* builtin:cloud.aws.cloudwatch.s3.errors.notauth
* builtin:cloud.aws.cloudwatch.s3.errors.service
* builtin:cloud.aws.cloudwatch.s3.errors.throttling
* builtin:cloud.aws.cloudwatch.s3.number

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.cloud.aws.alb.bytes | builtin:cloud.aws.alb.bytes |
| dt.cloud.aws.alb.connections.active | builtin:cloud.aws.alb.connections.active |
| dt.cloud.aws.alb.connections.new | builtin:cloud.aws.alb.connections.new |
| dt.cloud.aws.alb.errors.alb.http4xx | builtin:cloud.aws.alb.errors.alb.http4xx |
| dt.cloud.aws.alb.errors.alb.http5xx | builtin:cloud.aws.alb.errors.alb.http5xx |
| dt.cloud.aws.alb.errors.rej\_con | builtin:cloud.aws.alb.errors.rejCon |
| dt.cloud.aws.alb.errors.targ\_conn | builtin:cloud.aws.alb.errors.targConn |
| dt.cloud.aws.alb.errors.target.http4xx | builtin:cloud.aws.alb.errors.target.http4xx |
| dt.cloud.aws.alb.errors.target.http5xx | builtin:cloud.aws.alb.errors.target.http5xx |
| dt.cloud.aws.alb.errors.tls\_neg | builtin:cloud.aws.alb.errors.tlsNeg |
| dt.cloud.aws.alb.lcus | builtin:cloud.aws.alb.lcus |
| dt.cloud.aws.alb.requests | builtin:cloud.aws.alb.requests |
| dt.cloud.aws.alb.resp\_time | builtin:cloud.aws.alb.respTime |
| dt.cloud.aws.asg.running | builtin:cloud.aws.asg.running |
| dt.cloud.aws.asg.stopped | builtin:cloud.aws.asg.stopped |
| dt.cloud.aws.asg.terminated | builtin:cloud.aws.asg.terminated |
| dt.cloud.aws.az.running | builtin:cloud.aws.az.running |
| dt.cloud.aws.az.stopped | builtin:cloud.aws.az.stopped |
| dt.cloud.aws.az.terminated | builtin:cloud.aws.az.terminated |
| dt.cloud.aws.dynamo.capacity\_units.consumed.read | builtin:cloud.aws.dynamo.capacityUnits.consumed.read |
| dt.cloud.aws.dynamo.capacity\_units.consumed.write | builtin:cloud.aws.dynamo.capacityUnits.consumed.write |
| dt.cloud.aws.dynamo.capacity\_units.provisioned.read | builtin:cloud.aws.dynamo.capacityUnits.provisioned.read |
| dt.cloud.aws.dynamo.capacity\_units.provisioned.write | builtin:cloud.aws.dynamo.capacityUnits.provisioned.write |
| dt.cloud.aws.dynamo.capacity\_units.read | builtin:cloud.aws.dynamo.capacityUnits.read |
| dt.cloud.aws.dynamo.capacity\_units.write | builtin:cloud.aws.dynamo.capacityUnits.write |
| dt.cloud.aws.dynamo.errors.system | builtin:cloud.aws.dynamo.errors.system |
| dt.cloud.aws.dynamo.errors.user | builtin:cloud.aws.dynamo.errors.user |
| dt.cloud.aws.dynamo.requests.latency | builtin:cloud.aws.dynamo.requests.latency |
| dt.cloud.aws.dynamo.requests.returned\_items | builtin:cloud.aws.dynamo.requests.returnedItems |
| dt.cloud.aws.dynamo.requests.throttled | builtin:cloud.aws.dynamo.requests.throttled |
| dt.cloud.aws.dynamo.tables | builtin:cloud.aws.dynamo.tables |
| dt.cloud.aws.dynamo.throttled\_events.read | builtin:cloud.aws.dynamo.throttledEvents.read |
| dt.cloud.aws.dynamo.throttled\_events.write | builtin:cloud.aws.dynamo.throttledEvents.write |
| dt.cloud.aws.ebs.idle\_time | builtin:cloud.aws.ebs.idleTime |
| dt.cloud.aws.ebs.latency.read | builtin:cloud.aws.ebs.latency.read |
| dt.cloud.aws.ebs.latency.write | builtin:cloud.aws.ebs.latency.write |
| dt.cloud.aws.ebs.ops.consumed | builtin:cloud.aws.ebs.ops.consumed |
| dt.cloud.aws.ebs.ops.read | builtin:cloud.aws.ebs.ops.read |
| dt.cloud.aws.ebs.ops.write | builtin:cloud.aws.ebs.ops.write |
| dt.cloud.aws.ebs.queue | builtin:cloud.aws.ebs.queue |
| dt.cloud.aws.ebs.throughput.percent | builtin:cloud.aws.ebs.throughput.percent |
| dt.cloud.aws.ebs.throughput.read | builtin:cloud.aws.ebs.throughput.read |
| dt.cloud.aws.ebs.throughput.write | builtin:cloud.aws.ebs.throughput.write |
| dt.cloud.aws.ec2.cpu.usage | builtin:cloud.aws.ec2.cpu.usage |
| dt.cloud.aws.ec2.disk.read\_ops | builtin:cloud.aws.ec2.disk.readOps |
| dt.cloud.aws.ec2.disk.read\_rate | builtin:cloud.aws.ec2.disk.readRate |
| dt.cloud.aws.ec2.disk.write\_ops | builtin:cloud.aws.ec2.disk.writeOps |
| dt.cloud.aws.ec2.disk.write\_rate | builtin:cloud.aws.ec2.disk.writeRate |
| dt.cloud.aws.ec2.net.rx | builtin:cloud.aws.ec2.net.rx |
| dt.cloud.aws.ec2.net.tx | builtin:cloud.aws.ec2.net.tx |
| dt.cloud.aws.elb.errors.frontend | builtin:cloud.aws.elb.errors.frontend |
| dt.cloud.aws.elb.errors.backend.connection | builtin:cloud.aws.elb.errors.backend.connection |
| dt.cloud.aws.elb.errors.backend.http2xx | builtin:cloud.aws.elb.errors.backend.http2xx |
| dt.cloud.aws.elb.errors.backend.http3xx | builtin:cloud.aws.elb.errors.backend.http3xx |
| dt.cloud.aws.elb.errors.backend.http4xx | builtin:cloud.aws.elb.errors.backend.http4xx |
| dt.cloud.aws.elb.errors.backend.http5xx | builtin:cloud.aws.elb.errors.backend.http5xx |
| dt.cloud.aws.elb.errors.elb.http4xx | builtin:cloud.aws.elb.errors.elb.http4xx |
| dt.cloud.aws.elb.errors.elb.http5xx | builtin:cloud.aws.elb.errors.elb.http5xx |
| dt.cloud.aws.elb.hosts.healthy | builtin:cloud.aws.elb.hosts.healthy |
| dt.cloud.aws.elb.hosts.unhealthy | builtin:cloud.aws.elb.hosts.unhealthy |
| dt.cloud.aws.elb.latency | builtin:cloud.aws.elb.latency |
| dt.cloud.aws.elb.req\_compl | builtin:cloud.aws.elb.reqCompl |
| dt.cloud.aws.lambda.conc\_executions | builtin:cloud.aws.lambda.concExecutions |
| dt.cloud.aws.lambda.duration | builtin:cloud.aws.lambda.duration |
| dt.cloud.aws.lambda.errors | builtin:cloud.aws.lambda.errors |
| dt.cloud.aws.lambda.errors\_rate | builtin:cloud.aws.lambda.errorsRate |
| dt.cloud.aws.lambda.invocations | builtin:cloud.aws.lambda.invocations |
| dt.cloud.aws.lambda.prov\_conc\_executions | builtin:cloud.aws.lambda.provConcExecutions |
| dt.cloud.aws.lambda.prov\_conc\_invocations | builtin:cloud.aws.lambda.provConcInvocations |
| dt.cloud.aws.lambda.prov\_conc\_spillover\_invocations | builtin:cloud.aws.lambda.provConcSpilloverInvocations |
| dt.cloud.aws.lambda.throttlers | builtin:cloud.aws.lambda.throttlers |
| dt.cloud.aws.nlb.bytes | builtin:cloud.aws.nlb.bytes |
| dt.cloud.aws.nlb.flow.active | builtin:cloud.aws.nlb.flow.active |
| dt.cloud.aws.nlb.flow.new | builtin:cloud.aws.nlb.flow.new |
| dt.cloud.aws.nlb.lcus | builtin:cloud.aws.nlb.lcus |
| dt.cloud.aws.nlb.tcp.reset.client | builtin:cloud.aws.nlb.tcp.reset.client |
| dt.cloud.aws.nlb.tcp.reset.elb | builtin:cloud.aws.nlb.tcp.reset.elb |
| dt.cloud.aws.nlb.tcp.reset.target | builtin:cloud.aws.nlb.tcp.reset.target |
| dt.cloud.aws.rds.connections | builtin:cloud.aws.rds.connections |
| dt.cloud.aws.rds.cpu.usage | builtin:cloud.aws.rds.cpu.usage |
| dt.cloud.aws.rds.free | builtin:cloud.aws.rds.free |
| dt.cloud.aws.rds.latency.read | builtin:cloud.aws.rds.latency.read |
| dt.cloud.aws.rds.latency.write | builtin:cloud.aws.rds.latency.write |
| dt.cloud.aws.rds.memory.freeable | builtin:cloud.aws.rds.memory.freeable |
| dt.cloud.aws.rds.memory.swap | builtin:cloud.aws.rds.memory.swap |
| dt.cloud.aws.rds.net.rx | builtin:cloud.aws.rds.net.rx |
| dt.cloud.aws.rds.net.tx | builtin:cloud.aws.rds.net.tx |
| dt.cloud.aws.rds.ops.read | builtin:cloud.aws.rds.ops.read |
| dt.cloud.aws.rds.ops.write | builtin:cloud.aws.rds.ops.write |
| dt.cloud.aws.rds.restarts | builtin:cloud.aws.rds.restarts |
| dt.cloud.aws.rds.throughput.read | builtin:cloud.aws.rds.throughput.read |
| dt.cloud.aws.rds.throughput.write | builtin:cloud.aws.rds.throughput.write |

### Azure

Which Metrics Classic Azure metrics are not supported on Grail?

* builtin:cloud.azure.AzureStatistics.amountOfAzureResourceType
* builtin:cloud.azure.azureEventsWebhook.invalidRequests
* builtin:cloud.azure.azureEventsWebhook.okRequests
* builtin:cloud.azure.azureEventsWebhook.throttledRequests
* builtin:cloud.azure.azureEventsWebhook.unauthorizedRequests
* builtin:cloud.azure.azureEventsWebhook.unsupportedRequests

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.cloud.azure.api\_mgmt.capacity | builtin:cloud.azure.apiMgmt.capacity |
| dt.cloud.azure.api\_mgmt.duration | builtin:cloud.azure.apiMgmt.duration |
| dt.cloud.azure.api\_mgmt.requests.failed | builtin:cloud.azure.apiMgmt.requests.failed |
| dt.cloud.azure.api\_mgmt.requests.other | builtin:cloud.azure.apiMgmt.requests.other |
| dt.cloud.azure.api\_mgmt.requests.successful | builtin:cloud.azure.apiMgmt.requests.successful |
| dt.cloud.azure.api\_mgmt.requests.total | builtin:cloud.azure.apiMgmt.requests.total |
| dt.cloud.azure.api\_mgmt.requests.unauth | builtin:cloud.azure.apiMgmt.requests.unauth |
| dt.cloud.azure.app\_gateway.backend.settings.pool.host.healthy | builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy |
| dt.cloud.azure.app\_gateway.backend.settings.pool.host.unhealthy | builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy |
| dt.cloud.azure.app\_gateway.backend.settings.traffic.requests.failed | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed |
| dt.cloud.azure.app\_gateway.backend.settings.traffic.requests.total | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total |
| dt.cloud.azure.app\_gateway.http.status.response | builtin:cloud.azure.appGateway.http.status.response |
| dt.cloud.azure.app\_gateway.network.connections.count | builtin:cloud.azure.appGateway.network.connections.count |
| dt.cloud.azure.app\_gateway.network.throughput | builtin:cloud.azure.appGateway.network.throughput |
| dt.cloud.azure.app\_service.application\_queue.requests | builtin:cloud.azure.appService.applicationQueue.requests |
| dt.cloud.azure.app\_service.functions.application\_queue.requests | builtin:cloud.azure.appService.functions.applicationQueue.requests |
| dt.cloud.azure.app\_service.functions.execution.count | builtin:cloud.azure.appService.functions.execution.count |
| dt.cloud.azure.app\_service.functions.execution.units\_count | builtin:cloud.azure.appService.functions.execution.unitsCount |
| dt.cloud.azure.app\_service.functions.http.status.http5xx | builtin:cloud.azure.appService.functions.http.status.http5xx |
| dt.cloud.azure.app\_service.functions.io.operations.other | builtin:cloud.azure.appService.functions.io.operations.other |
| dt.cloud.azure.app\_service.functions.io.operations.read | builtin:cloud.azure.appService.functions.io.operations.read |
| dt.cloud.azure.app\_service.functions.io.operations.write | builtin:cloud.azure.appService.functions.io.operations.write |
| dt.cloud.azure.app\_service.functions.io.other | builtin:cloud.azure.appService.functions.io.other |
| dt.cloud.azure.app\_service.functions.io.read | builtin:cloud.azure.appService.functions.io.read |
| dt.cloud.azure.app\_service.functions.io.write | builtin:cloud.azure.appService.functions.io.write |
| dt.cloud.azure.app\_service.functions.traffic.bytes\_received | builtin:cloud.azure.appService.functions.traffic.bytesReceived |
| dt.cloud.azure.app\_service.functions.traffic.bytes\_sent | builtin:cloud.azure.appService.functions.traffic.bytesSent |
| dt.cloud.azure.app\_service.http.status.http2xx | builtin:cloud.azure.appService.http.status.http2xx |
| dt.cloud.azure.app\_service.http.status.http403 | builtin:cloud.azure.appService.http.status.http403 |
| dt.cloud.azure.app\_service.http.status.http5xx | builtin:cloud.azure.appService.http.status.http5xx |
| dt.cloud.azure.app\_service.io.operations.other | builtin:cloud.azure.appService.io.operations.other |
| dt.cloud.azure.app\_service.io.operations.read | builtin:cloud.azure.appService.io.operations.read |
| dt.cloud.azure.app\_service.io.operations.write | builtin:cloud.azure.appService.io.operations.write |
| dt.cloud.azure.app\_service.io.other | builtin:cloud.azure.appService.io.other |
| dt.cloud.azure.app\_service.io.read | builtin:cloud.azure.appService.io.read |
| dt.cloud.azure.app\_service.io.write | builtin:cloud.azure.appService.io.write |
| dt.cloud.azure.app\_service.response.avg | builtin:cloud.azure.appService.response.avg |
| dt.cloud.azure.app\_service.traffic.bytes\_received | builtin:cloud.azure.appService.traffic.bytesReceived |
| dt.cloud.azure.app\_service.traffic.bytes\_sent | builtin:cloud.azure.appService.traffic.bytesSent |
| dt.cloud.azure.app\_service.traffic.requests | builtin:cloud.azure.appService.traffic.requests |
| dt.cloud.azure.cosmos.available\_storage | builtin:cloud.azure.cosmos.availableStorage |
| dt.cloud.azure.cosmos.data\_usage | builtin:cloud.azure.cosmos.dataUsage |
| dt.cloud.azure.cosmos.document\_count | builtin:cloud.azure.cosmos.documentCount |
| dt.cloud.azure.cosmos.document\_quota | builtin:cloud.azure.cosmos.documentQuota |
| dt.cloud.azure.cosmos.index\_usage | builtin:cloud.azure.cosmos.indexUsage |
| dt.cloud.azure.cosmos.metadata\_requests | builtin:cloud.azure.cosmos.metadataRequests |
| dt.cloud.azure.cosmos.normalized\_ruconsumption | builtin:cloud.azure.cosmos.normalizedRUConsumption |
| dt.cloud.azure.cosmos.provisioned\_throughput | builtin:cloud.azure.cosmos.provisionedThroughput |
| dt.cloud.azure.cosmos.replication\_latency | builtin:cloud.azure.cosmos.replicationLatency |
| dt.cloud.azure.cosmos.request\_units | builtin:cloud.azure.cosmos.requestUnits |
| dt.cloud.azure.cosmos.requests | builtin:cloud.azure.cosmos.requests |
| dt.cloud.azure.cosmos.service\_availability | builtin:cloud.azure.cosmos.serviceAvailability |
| dt.cloud.azure.event\_hub.capture.backlog | builtin:cloud.azure.eventHub.capture.backlog |
| dt.cloud.azure.event\_hub.capture.bytes | builtin:cloud.azure.eventHub.capture.bytes |
| dt.cloud.azure.event\_hub.capture.msg | builtin:cloud.azure.eventHub.capture.msg |
| dt.cloud.azure.event\_hub.errors.quota\_exceeded | builtin:cloud.azure.eventHub.errors.quotaExceeded |
| dt.cloud.azure.event\_hub.errors.server | builtin:cloud.azure.eventHub.errors.server |
| dt.cloud.azure.event\_hub.errors.user | builtin:cloud.azure.eventHub.errors.user |
| dt.cloud.azure.event\_hub.requests.incoming | builtin:cloud.azure.eventHub.requests.incoming |
| dt.cloud.azure.event\_hub.requests.successful | builtin:cloud.azure.eventHub.requests.successful |
| dt.cloud.azure.event\_hub.requests.throttled | builtin:cloud.azure.eventHub.requests.throttled |
| dt.cloud.azure.event\_hub.traffic.bytes\_in | builtin:cloud.azure.eventHub.traffic.bytesIn |
| dt.cloud.azure.event\_hub.traffic.bytes\_out | builtin:cloud.azure.eventHub.traffic.bytesOut |
| dt.cloud.azure.event\_hub.traffic.msg\_in | builtin:cloud.azure.eventHub.traffic.msgIn |
| dt.cloud.azure.event\_hub.traffic.msg\_out | builtin:cloud.azure.eventHub.traffic.msgOut |
| dt.cloud.azure.event\_hub\_namespace.connections.active | builtin:cloud.azure.eventHubNamespace.connections.active |
| dt.cloud.azure.event\_hub\_namespace.connections.closed | builtin:cloud.azure.eventHubNamespace.connections.closed |
| dt.cloud.azure.event\_hub\_namespace.connections.opened | builtin:cloud.azure.eventHubNamespace.connections.opened |
| dt.cloud.azure.iot\_hub.command.abandoned | builtin:cloud.azure.iotHub.command.abandoned |
| dt.cloud.azure.iot\_hub.command.completed | builtin:cloud.azure.iotHub.command.completed |
| dt.cloud.azure.iot\_hub.command.rejected | builtin:cloud.azure.iotHub.command.rejected |
| dt.cloud.azure.iot\_hub.device.connected | builtin:cloud.azure.iotHub.device.connected |
| dt.cloud.azure.iot\_hub.device.daily\_throughput\_throttling | builtin:cloud.azure.iotHub.device.dailyThroughputThrottling |
| dt.cloud.azure.iot\_hub.device.data\_usage | builtin:cloud.azure.iotHub.device.dataUsage |
| dt.cloud.azure.iot\_hub.device.registered | builtin:cloud.azure.iotHub.device.registered |
| dt.cloud.azure.iot\_hub.event\_hub.average\_latency\_ms | builtin:cloud.azure.iotHub.eventHub.averageLatencyMs |
| dt.cloud.azure.iot\_hub.event\_hub.built\_in\_event\_hub.average\_latency\_ms | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs |
| dt.cloud.azure.iot\_hub.event\_hub.built\_in\_event\_hub.messages.delivered | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered |
| dt.cloud.azure.iot\_hub.event\_hub.messages.delivered | builtin:cloud.azure.iotHub.eventHub.messages.delivered |
| dt.cloud.azure.iot\_hub.messages.dropped | builtin:cloud.azure.iotHub.messages.dropped |
| dt.cloud.azure.iot\_hub.messages.invalid\_for\_all\_endpoints | builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints |
| dt.cloud.azure.iot\_hub.messages.orphaned | builtin:cloud.azure.iotHub.messages.orphaned |
| dt.cloud.azure.iot\_hub.messages.send\_attempts | builtin:cloud.azure.iotHub.messages.sendAttempts |
| dt.cloud.azure.iot\_hub.messages.sent | builtin:cloud.azure.iotHub.messages.sent |
| dt.cloud.azure.iot\_hub.messages.sent\_to\_fallback | builtin:cloud.azure.iotHub.messages.sentToFallback |
| dt.cloud.azure.iot\_hub.service\_bus.queues.average\_latency\_ms | builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs |
| dt.cloud.azure.iot\_hub.service\_bus.queues.messages\_delivered | builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered |
| dt.cloud.azure.iot\_hub.service\_bus.topics.average\_latency\_ms | builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs |
| dt.cloud.azure.iot\_hub.service\_bus.topics.messages\_delivered | builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered |
| dt.cloud.azure.iot\_hub.storage\_endpoints.avg\_latency\_ms | builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs |
| dt.cloud.azure.iot\_hub.storage\_endpoints.blobs\_written | builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten |
| dt.cloud.azure.iot\_hub.storage\_endpoints.bytes\_written | builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten |
| dt.cloud.azure.iot\_hub.storage\_endpoints.message\_delivered | builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered |
| dt.cloud.azure.loadbalancer.availability.dip\_tcp | builtin:cloud.azure.loadbalancer.availability.dipTcp |
| dt.cloud.azure.loadbalancer.availability.dip\_udp | builtin:cloud.azure.loadbalancer.availability.dipUdp |
| dt.cloud.azure.loadbalancer.availability.vip | builtin:cloud.azure.loadbalancer.availability.vip |
| dt.cloud.azure.loadbalancer.snat\_connection.est | builtin:cloud.azure.loadbalancer.snatConnection.est |
| dt.cloud.azure.loadbalancer.snat\_connection.pending | builtin:cloud.azure.loadbalancer.snatConnection.pending |
| dt.cloud.azure.loadbalancer.snat\_connection.rej | builtin:cloud.azure.loadbalancer.snatConnection.rej |
| dt.cloud.azure.loadbalancer.traffic.byte\_in | builtin:cloud.azure.loadbalancer.traffic.byteIn |
| dt.cloud.azure.loadbalancer.traffic.byte\_out | builtin:cloud.azure.loadbalancer.traffic.byteOut |
| dt.cloud.azure.loadbalancer.traffic.packet\_in | builtin:cloud.azure.loadbalancer.traffic.packetIn |
| dt.cloud.azure.loadbalancer.traffic.packet\_out | builtin:cloud.azure.loadbalancer.traffic.packetOut |
| dt.cloud.azure.loadbalancer.traffic.packet\_syn\_in | builtin:cloud.azure.loadbalancer.traffic.packetSynIn |
| dt.cloud.azure.loadbalancer.traffic.packet\_syn\_out | builtin:cloud.azure.loadbalancer.traffic.packetSynOut |
| dt.cloud.azure.redis.cache.hits | builtin:cloud.azure.redis.cache.hits |
| dt.cloud.azure.redis.cache.misses | builtin:cloud.azure.redis.cache.misses |
| dt.cloud.azure.redis.cache.read | builtin:cloud.azure.redis.cache.read |
| dt.cloud.azure.redis.cache.write | builtin:cloud.azure.redis.cache.write |
| dt.cloud.azure.redis.commands.get | builtin:cloud.azure.redis.commands.get |
| dt.cloud.azure.redis.commands.set | builtin:cloud.azure.redis.commands.set |
| dt.cloud.azure.redis.commands.total | builtin:cloud.azure.redis.commands.total |
| dt.cloud.azure.redis.connected | builtin:cloud.azure.redis.connected |
| dt.cloud.azure.redis.keys.evicted | builtin:cloud.azure.redis.keys.evicted |
| dt.cloud.azure.redis.keys.expired | builtin:cloud.azure.redis.keys.expired |
| dt.cloud.azure.redis.keys.total | builtin:cloud.azure.redis.keys.total |
| dt.cloud.azure.redis.load | builtin:cloud.azure.redis.load |
| dt.cloud.azure.redis.memory.used | builtin:cloud.azure.redis.memory.used |
| dt.cloud.azure.redis.memory.used\_rss | builtin:cloud.azure.redis.memory.usedRss |
| dt.cloud.azure.redis.processor\_time | builtin:cloud.azure.redis.processorTime |
| dt.cloud.azure.region.vms.initializing | builtin:cloud.azure.region.vms.initializing |
| dt.cloud.azure.region.vms.running | builtin:cloud.azure.region.vms.running |
| dt.cloud.azure.region.vms.stopped | builtin:cloud.azure.region.vms.stopped |
| dt.cloud.azure.service\_bus.namespace.connections.active | builtin:cloud.azure.serviceBus.namespace.connections.active |
| dt.cloud.azure.service\_bus.namespace.cpu | builtin:cloud.azure.serviceBus.namespace.cpu |
| dt.cloud.azure.service\_bus.namespace.errors.server | builtin:cloud.azure.serviceBus.namespace.errors.server |
| dt.cloud.azure.service\_bus.namespace.errors.user | builtin:cloud.azure.serviceBus.namespace.errors.user |
| dt.cloud.azure.service\_bus.namespace.memory | builtin:cloud.azure.serviceBus.namespace.memory |
| dt.cloud.azure.service\_bus.namespace.messages.count | builtin:cloud.azure.serviceBus.namespace.messages.count |
| dt.cloud.azure.service\_bus.namespace.messages.count\_active | builtin:cloud.azure.serviceBus.namespace.messages.countActive |
| dt.cloud.azure.service\_bus.namespace.messages.count\_dead\_lettered | builtin:cloud.azure.serviceBus.namespace.messages.countDeadLettered |
| dt.cloud.azure.service\_bus.namespace.messages.count\_scheduled | builtin:cloud.azure.serviceBus.namespace.messages.countScheduled |
| dt.cloud.azure.service\_bus.namespace.messages.incoming | builtin:cloud.azure.serviceBus.namespace.messages.incoming |
| dt.cloud.azure.service\_bus.namespace.messages.outgoing | builtin:cloud.azure.serviceBus.namespace.messages.outgoing |
| dt.cloud.azure.service\_bus.namespace.requests.incoming | builtin:cloud.azure.serviceBus.namespace.requests.incoming |
| dt.cloud.azure.service\_bus.namespace.requests.successful | builtin:cloud.azure.serviceBus.namespace.requests.successful |
| dt.cloud.azure.service\_bus.namespace.requests.throttled | builtin:cloud.azure.serviceBus.namespace.requests.throttled |
| dt.cloud.azure.service\_bus.namespace.size | builtin:cloud.azure.serviceBus.namespace.size |
| dt.cloud.azure.service\_bus.queue.errors.server | builtin:cloud.azure.serviceBus.queue.errors.server |
| dt.cloud.azure.service\_bus.queue.errors.user | builtin:cloud.azure.serviceBus.queue.errors.user |
| dt.cloud.azure.service\_bus.queue.messages.count | builtin:cloud.azure.serviceBus.queue.messages.count |
| dt.cloud.azure.service\_bus.queue.messages.count\_active | builtin:cloud.azure.serviceBus.queue.messages.countActive |
| dt.cloud.azure.service\_bus.queue.messages.count\_dead\_lettered | builtin:cloud.azure.serviceBus.queue.messages.countDeadLettered |
| dt.cloud.azure.service\_bus.queue.messages.count\_scheduled | builtin:cloud.azure.serviceBus.queue.messages.countScheduled |
| dt.cloud.azure.service\_bus.queue.messages.incoming | builtin:cloud.azure.serviceBus.queue.messages.incoming |
| dt.cloud.azure.service\_bus.queue.messages.outgoing | builtin:cloud.azure.serviceBus.queue.messages.outgoing |
| dt.cloud.azure.service\_bus.queue.requests.incoming | builtin:cloud.azure.serviceBus.queue.requests.incoming |
| dt.cloud.azure.service\_bus.queue.requests.successful | builtin:cloud.azure.serviceBus.queue.requests.successful |
| dt.cloud.azure.service\_bus.queue.requests.throttled | builtin:cloud.azure.serviceBus.queue.requests.throttled |
| dt.cloud.azure.service\_bus.queue.size | builtin:cloud.azure.serviceBus.queue.size |
| dt.cloud.azure.service\_bus.topic.errors.server | builtin:cloud.azure.serviceBus.topic.errors.server |
| dt.cloud.azure.service\_bus.topic.errors.user | builtin:cloud.azure.serviceBus.topic.errors.user |
| dt.cloud.azure.service\_bus.topic.messages.count | builtin:cloud.azure.serviceBus.topic.messages.count |
| dt.cloud.azure.service\_bus.topic.messages.count\_active | builtin:cloud.azure.serviceBus.topic.messages.countActive |
| dt.cloud.azure.service\_bus.topic.messages.count\_dead\_lettered | builtin:cloud.azure.serviceBus.topic.messages.countDeadLettered |
| dt.cloud.azure.service\_bus.topic.messages.count\_scheduled | builtin:cloud.azure.serviceBus.topic.messages.countScheduled |
| dt.cloud.azure.service\_bus.topic.messages.incoming | builtin:cloud.azure.serviceBus.topic.messages.incoming |
| dt.cloud.azure.service\_bus.topic.messages.outgoing | builtin:cloud.azure.serviceBus.topic.messages.outgoing |
| dt.cloud.azure.service\_bus.topic.requests.incoming | builtin:cloud.azure.serviceBus.topic.requests.incoming |
| dt.cloud.azure.service\_bus.topic.requests.successful | builtin:cloud.azure.serviceBus.topic.requests.successful |
| dt.cloud.azure.service\_bus.topic.requests.throttled | builtin:cloud.azure.serviceBus.topic.requests.throttled |
| dt.cloud.azure.service\_bus.topic.size | builtin:cloud.azure.serviceBus.topic.size |
| dt.cloud.azure.sql\_database.connections.blocked\_by\_firewall | builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall |
| dt.cloud.azure.sql\_database.connections.failed | builtin:cloud.azure.sqlDatabase.connections.failed |
| dt.cloud.azure.sql\_database.connections.successful | builtin:cloud.azure.sqlDatabase.connections.successful |
| dt.cloud.azure.sql\_database.cpu\_percent | builtin:cloud.azure.sqlDatabase.cpuPercent |
| dt.cloud.azure.sql\_database.deadlocks | builtin:cloud.azure.sqlDatabase.deadlocks |
| dt.cloud.azure.sql\_database.dtu.consumption\_perc | builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc |
| dt.cloud.azure.sql\_database.dtu.limit.count | builtin:cloud.azure.sqlDatabase.dtu.limit.count |
| dt.cloud.azure.sql\_database.dtu.limit.used | builtin:cloud.azure.sqlDatabase.dtu.limit.used |
| dt.cloud.azure.sql\_database.io.data\_read | builtin:cloud.azure.sqlDatabase.io.dataRead |
| dt.cloud.azure.sql\_database.io.log\_write | builtin:cloud.azure.sqlDatabase.io.logWrite |
| dt.cloud.azure.sql\_database.sessions | builtin:cloud.azure.sqlDatabase.sessions |
| dt.cloud.azure.sql\_database.storage.percent | builtin:cloud.azure.sqlDatabase.storage.percent |
| dt.cloud.azure.sql\_database.storage.total\_bytes | builtin:cloud.azure.sqlDatabase.storage.totalBytes |
| dt.cloud.azure.sql\_database.storage.xtp\_percent | builtin:cloud.azure.sqlDatabase.storage.xtpPercent |
| dt.cloud.azure.sql\_database.workers | builtin:cloud.azure.sqlDatabase.workers |
| dt.cloud.azure.sql\_elastic\_pool.cpu\_percent | builtin:cloud.azure.sqlElasticPool.cpuPercent |
| dt.cloud.azure.sql\_elastic\_pool.dtu.consumption | builtin:cloud.azure.sqlElasticPool.dtu.consumption |
| dt.cloud.azure.sql\_elastic\_pool.dtu.storage.limit\_bytes | builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes |
| dt.cloud.azure.sql\_elastic\_pool.dtu.storage.percent | builtin:cloud.azure.sqlElasticPool.dtu.storage.percent |
| dt.cloud.azure.sql\_elastic\_pool.dtu.storage.used\_bytes | builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes |
| dt.cloud.azure.sql\_elastic\_pool.dtu.storage.xtp\_percent | builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent |
| dt.cloud.azure.sql\_elastic\_pool.edtu.limit | builtin:cloud.azure.sqlElasticPool.edtu.limit |
| dt.cloud.azure.sql\_elastic\_pool.edtu.used | builtin:cloud.azure.sqlElasticPool.edtu.used |
| dt.cloud.azure.sql\_elastic\_pool.io.data\_read | builtin:cloud.azure.sqlElasticPool.io.dataRead |
| dt.cloud.azure.sql\_elastic\_pool.io.log\_write | builtin:cloud.azure.sqlElasticPool.io.logWrite |
| dt.cloud.azure.sql\_elastic\_pool.sessions | builtin:cloud.azure.sqlElasticPool.sessions |
| dt.cloud.azure.sql\_elastic\_pool.workers | builtin:cloud.azure.sqlElasticPool.workers |
| dt.cloud.azure.storage.blob.capacity | builtin:cloud.azure.storage.blob.capacity |
| dt.cloud.azure.storage.blob.containers | builtin:cloud.azure.storage.blob.containers |
| dt.cloud.azure.storage.blob.entities | builtin:cloud.azure.storage.blob.entities |
| dt.cloud.azure.storage.blob.transactions | builtin:cloud.azure.storage.blob.transactions |
| dt.cloud.azure.storage.blob.transactions.network.egress | builtin:cloud.azure.storage.blob.transactions.network.egress |
| dt.cloud.azure.storage.blob.transactions.network.ingress | builtin:cloud.azure.storage.blob.transactions.network.ingress |
| dt.cloud.azure.storage.blob.transactions.network.latency.success.e2e | builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e |
| dt.cloud.azure.storage.blob.transactions.network.latency.success.server | builtin:cloud.azure.storage.blob.transactions.network.latency.success.server |
| dt.cloud.azure.storage.file.capacity | builtin:cloud.azure.storage.file.capacity |
| dt.cloud.azure.storage.file.containers | builtin:cloud.azure.storage.file.containers |
| dt.cloud.azure.storage.file.entities | builtin:cloud.azure.storage.file.entities |
| dt.cloud.azure.storage.file.transactions | builtin:cloud.azure.storage.file.transactions |
| dt.cloud.azure.storage.file.transactions.network.egress | builtin:cloud.azure.storage.file.transactions.network.egress |
| dt.cloud.azure.storage.file.transactions.network.ingress | builtin:cloud.azure.storage.file.transactions.network.ingress |
| dt.cloud.azure.storage.file.transactions.network.latency.success.e2e | builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e |
| dt.cloud.azure.storage.file.transactions.network.latency.success.server | builtin:cloud.azure.storage.file.transactions.network.latency.success.server |
| dt.cloud.azure.storage.queue.capacity | builtin:cloud.azure.storage.queue.capacity |
| dt.cloud.azure.storage.queue.containers | builtin:cloud.azure.storage.queue.containers |
| dt.cloud.azure.storage.queue.entities | builtin:cloud.azure.storage.queue.entities |
| dt.cloud.azure.storage.queue.transactions | builtin:cloud.azure.storage.queue.transactions |
| dt.cloud.azure.storage.queue.transactions.network.egress | builtin:cloud.azure.storage.queue.transactions.network.egress |
| dt.cloud.azure.storage.queue.transactions.network.ingress | builtin:cloud.azure.storage.queue.transactions.network.ingress |
| dt.cloud.azure.storage.queue.transactions.network.latency.success.e2e | builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e |
| dt.cloud.azure.storage.queue.transactions.network.latency.success.server | builtin:cloud.azure.storage.queue.transactions.network.latency.success.server |
| dt.cloud.azure.storage.table.capacity | builtin:cloud.azure.storage.table.capacity |
| dt.cloud.azure.storage.table.containers | builtin:cloud.azure.storage.table.containers |
| dt.cloud.azure.storage.table.entities | builtin:cloud.azure.storage.table.entities |
| dt.cloud.azure.storage.table.transactions | builtin:cloud.azure.storage.table.transactions |
| dt.cloud.azure.storage.table.transactions.network.egress | builtin:cloud.azure.storage.table.transactions.network.egress |
| dt.cloud.azure.storage.table.transactions.network.ingress | builtin:cloud.azure.storage.table.transactions.network.ingress |
| dt.cloud.azure.storage.table.transactions.network.latency.success.server | builtin:cloud.azure.storage.table.transactions.network.latency.success.server |
| dt.cloud.azure.storage.table.transactions.network.latency.success.server.e2e | builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e |
| dt.cloud.azure.vm.cpu\_usage | builtin:cloud.azure.vm.cpuUsage |
| dt.cloud.azure.vm.disk.read | builtin:cloud.azure.vm.disk.read |
| dt.cloud.azure.vm.disk.read\_ops | builtin:cloud.azure.vm.disk.readOps |
| dt.cloud.azure.vm.disk.write | builtin:cloud.azure.vm.disk.write |
| dt.cloud.azure.vm.disk.write\_ops | builtin:cloud.azure.vm.disk.writeOps |
| dt.cloud.azure.vm.network.bytes\_in | builtin:cloud.azure.vm.network.bytesIn |
| dt.cloud.azure.vm.network.bytes\_out | builtin:cloud.azure.vm.network.bytesOut |
| dt.cloud.azure.vm\_scale\_set.cpu\_usage | builtin:cloud.azure.vmScaleSet.cpuUsage |
| dt.cloud.azure.vm\_scale\_set.disk.read | builtin:cloud.azure.vmScaleSet.disk.read |
| dt.cloud.azure.vm\_scale\_set.disk.read\_ops | builtin:cloud.azure.vmScaleSet.disk.readOps |
| dt.cloud.azure.vm\_scale\_set.disk.write | builtin:cloud.azure.vmScaleSet.disk.write |
| dt.cloud.azure.vm\_scale\_set.disk.write\_ops | builtin:cloud.azure.vmScaleSet.disk.writeOps |
| dt.cloud.azure.vm\_scale\_set.network.bytes\_in | builtin:cloud.azure.vmScaleSet.network.bytesIn |
| dt.cloud.azure.vm\_scale\_set.network.bytes\_out | builtin:cloud.azure.vmScaleSet.network.bytesOut |
| dt.cloud.azure.vm\_scale\_set.vms.initializing | builtin:cloud.azure.vmScaleSet.vms.initializing |
| dt.cloud.azure.vm\_scale\_set.vms.running | builtin:cloud.azure.vmScaleSet.vms.running |
| dt.cloud.azure.vm\_scale\_set.vms.stopped | builtin:cloud.azure.vmScaleSet.vms.stopped |

### Cloud Foundry

Which Metrics Classic Cloud Foundry metrics are not supported on Grail?

* builtin:cloud.cloudfoundry.auctioneer.lprFailed
* builtin:cloud.cloudfoundry.auctioneer.lprStarted

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.cloud.cloudfoundry.auctioneer.fetch\_duration | builtin:cloud.cloudfoundry.auctioneer.fetchDuration |
| dt.cloud.cloudfoundry.auctioneer.task\_failed | builtin:cloud.cloudfoundry.auctioneer.taskFailed |
| dt.cloud.cloudfoundry.http.bad\_gateways | builtin:cloud.cloudfoundry.http.badGateways |
| dt.cloud.cloudfoundry.http.latency | builtin:cloud.cloudfoundry.http.latency |
| dt.cloud.cloudfoundry.http.responses5xx | builtin:cloud.cloudfoundry.http.responses5xx |
| dt.cloud.cloudfoundry.http.total\_requests | builtin:cloud.cloudfoundry.http.totalRequests |

### VMware

Which Metrics Classic VMware metrics are not supported on Grail?

* builtin:cloud.vmware.hypervisor.availability

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.cloud.vmware.hypervisor.cpu.usage | builtin:cloud.vmware.hypervisor.cpu.usage |
| dt.cloud.vmware.hypervisor.disk.usage | builtin:cloud.vmware.hypervisor.disk.usage |
| dt.cloud.vmware.hypervisor.hostdisk.commands\_aborted | builtin:cloud.vmware.hypervisor.hostdisk.commandsAborted |
| dt.cloud.vmware.hypervisor.hostdisk.queue\_latency | builtin:cloud.vmware.hypervisor.hostdisk.queueLatency |
| dt.cloud.vmware.hypervisor.hostdisk.r\_iops | builtin:cloud.vmware.hypervisor.hostdisk.rIops |
| dt.cloud.vmware.hypervisor.hostdisk.read\_latency | builtin:cloud.vmware.hypervisor.hostdisk.readLatency |
| dt.cloud.vmware.hypervisor.hostdisk.read\_rate | builtin:cloud.vmware.hypervisor.hostdisk.readRate |
| dt.cloud.vmware.hypervisor.hostdisk.w\_iops | builtin:cloud.vmware.hypervisor.hostdisk.wIops |
| dt.cloud.vmware.hypervisor.hostdisk.write\_latency | builtin:cloud.vmware.hypervisor.hostdisk.writeLatency |
| dt.cloud.vmware.hypervisor.hostdisk.write\_rate | builtin:cloud.vmware.hypervisor.hostdisk.writeRate |
| dt.cloud.vmware.hypervisor.mem.compression\_rate | builtin:cloud.vmware.hypervisor.mem.compressionRate |
| dt.cloud.vmware.hypervisor.mem.consumed | builtin:cloud.vmware.hypervisor.mem.consumed |
| dt.cloud.vmware.hypervisor.mem.decompression\_rate | builtin:cloud.vmware.hypervisor.mem.decompressionRate |
| dt.cloud.vmware.hypervisor.mem.swap\_in | builtin:cloud.vmware.hypervisor.mem.swapIn |
| dt.cloud.vmware.hypervisor.mem.swap\_out | builtin:cloud.vmware.hypervisor.mem.swapOut |
| dt.cloud.vmware.hypervisor.net.rx | builtin:cloud.vmware.hypervisor.net.rx |
| dt.cloud.vmware.hypervisor.net.tx | builtin:cloud.vmware.hypervisor.net.tx |
| dt.cloud.vmware.hypervisor.nic.data\_rx | builtin:cloud.vmware.hypervisor.nic.dataRx |
| dt.cloud.vmware.hypervisor.nic.data\_tx | builtin:cloud.vmware.hypervisor.nic.dataTx |
| dt.cloud.vmware.hypervisor.nic.packets\_rx\_dropped | builtin:cloud.vmware.hypervisor.nic.packetsRxDropped |
| dt.cloud.vmware.hypervisor.nic.packets\_tx\_dropped | builtin:cloud.vmware.hypervisor.nic.packetsTxDropped |
| dt.cloud.vmware.hypervisor.vms.count | builtin:cloud.vmware.hypervisor.vms.count |
| dt.cloud.vmware.hypervisor.vms.power\_off | builtin:cloud.vmware.hypervisor.vms.powerOff |
| dt.cloud.vmware.hypervisor.vms.suspended | builtin:cloud.vmware.hypervisor.vms.suspended |
| dt.cloud.vmware.vm.cpu.ready\_perc | builtin:cloud.vmware.vm.cpu.readyPerc |
| dt.cloud.vmware.vm.cpu.swap\_wait | builtin:cloud.vmware.vm.cpu.swapWait |
| dt.cloud.vmware.vm.cpu.usage | builtin:cloud.vmware.vm.cpu.usage |
| dt.cloud.vmware.vm.cpu.usage\_perc | builtin:cloud.vmware.vm.cpu.usagePerc |
| dt.cloud.vmware.vm.disk.usage | builtin:cloud.vmware.vm.disk.usage |
| dt.cloud.vmware.vm.mem.active | builtin:cloud.vmware.vm.mem.active |
| dt.cloud.vmware.vm.mem.compression\_rate | builtin:cloud.vmware.vm.mem.compressionRate |
| dt.cloud.vmware.vm.mem.consumed | builtin:cloud.vmware.vm.mem.consumed |
| dt.cloud.vmware.vm.mem.decompression\_rate | builtin:cloud.vmware.vm.mem.decompressionRate |
| dt.cloud.vmware.vm.mem.swap\_in | builtin:cloud.vmware.vm.mem.swapIn |
| dt.cloud.vmware.vm.mem.swap\_out | builtin:cloud.vmware.vm.mem.swapOut |
| dt.cloud.vmware.vm.net.rx | builtin:cloud.vmware.vm.net.rx |
| dt.cloud.vmware.vm.net.tx | builtin:cloud.vmware.vm.net.tx |

## Containers

New container metrics are now available for [DPS](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")-enabled customers. The new metrics are subject to a new licensing model, as distinct from the current full-stack host units model.

Metric availability:

* The Metrics Classic metrics have been discontinued.
* The new metrics are immediately available with OneAgent deployment.

More information:

* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Unlock the Power of DevSecOps with Newly Released Kubernetes Experience for Platform Engineeringï»¿](https://dt-url.net/c7038ec)
* [Dynatrace Launches New Kubernetes Experience for Platform Engineering Teamsï»¿](https://dt-url.net/882385r)

Which Metrics Classic container metrics are not supported on Grail?

* builtin:containers.cpu.limit
* builtin:containers.cpu.throttledMilliCores
* builtin:containers.cpu.usageMilliCores
* builtin:containers.cpu.usagePercent
* builtin:containers.cpu.usageSystemMilliCores
* builtin:containers.cpu.usageTime
* builtin:containers.cpu.usageUserMilliCores
* builtin:containers.memory.limitPercent
* builtin:containers.memory.outOfMemoryKills
* builtin:containers.memory.usagePercent

Additionally, the following Classic [Extension 1.0](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") metrics are deprecated and likewise not supported on Grail:

* builtin:containers.bytes\_rx2
* builtin:containers.bytes\_tx2
* builtin:containers.cpu\_usage2
* builtin:containers.devicemapper\_data\_space\_available
* builtin:containers.devicemapper\_data\_space\_used
* builtin:containers.devicemapper\_metadata\_space\_available
* builtin:containers.devicemapper\_metadata\_space\_used
* builtin:containers.memory\_percent
* builtin:containers.memory\_usage2
* builtin:containers.no\_of\_containers\_launched
* builtin:containers.no\_of\_containers\_per\_pgi
* builtin:containers.no\_of\_containers\_running
* builtin:containers.no\_of\_containers\_terminated
* builtin:containers.throttled\_time2

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.containers.cpu.logical\_cores | builtin:containers.cpu.logicalCores |
| dt.containers.cpu.shares | builtin:containers.cpu.shares |
| dt.containers.cpu.throttled\_time | builtin:containers.cpu.throttledTime |
| dt.containers.cpu.throttling\_ratio | builtin:containers.cpu.throttlingRatio |
| dt.containers.cpu.usage\_system\_time | builtin:containers.cpu.usageSystemTime |
| dt.containers.cpu.usage\_user\_time | builtin:containers.cpu.usageUserTime |
| dt.containers.memory.cache\_bytes | builtin:containers.memory.cacheBytes |
| dt.containers.memory.limit\_bytes | builtin:containers.memory.limitBytes |
| dt.containers.memory.physical\_total\_bytes | builtin:containers.memory.physicalTotalBytes |
| dt.containers.memory.resident\_set\_bytes | builtin:containers.memory.residentSetBytes |

## Infrastructure

For a detailed list of the host metrics and their availability, refer to [Host metrics](/docs/observe/infrastructure-observability/hosts/reference/metrics "Metrics and metrics classic measured for host monitoring").

### CPU

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.cpu.ent\_config | builtin:host.cpu.entConfig |
| dt.host.cpu.entc | builtin:host.cpu.entc |
| dt.host.cpu.idle | builtin:host.cpu.idle |
| dt.host.cpu.iowait | builtin:host.cpu.iowait |
| dt.host.cpu.load | builtin:host.cpu.load |
| dt.host.cpu.load15m | builtin:host.cpu.load15m |
| dt.host.cpu.load5m | builtin:host.cpu.load5m |
| dt.host.cpu.other | builtin:host.cpu.other |
| dt.host.cpu.physc | builtin:host.cpu.physc |
| dt.host.cpu.steal | builtin:host.cpu.steal |
| dt.host.cpu.system | builtin:host.cpu.system |
| dt.host.cpu.usage | builtin:host.cpu.usage |
| dt.host.cpu.user | builtin:host.cpu.user |
| dt.host.kernel\_threads.blocked | builtin:host.kernelThreads.blocked |
| dt.host.kernel\_threads.io\_event\_wait | builtin:host.kernelThreads.ioEventWait |
| dt.host.kernel\_threads.io\_message\_wait | builtin:host.kernelThreads.ioMessageWait |
| dt.host.kernel\_threads.running | builtin:host.kernelThreads.running |

### DNS

Which Metrics Classic DNS metrics are not supported on Grail?

* builtin:host.dns.singleQueryTime
* builtin:host.dns.singleQueryTimeByDnsIp
* builtin:host.dns.singleQueryTimeByHost

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.dns.errors | builtin:host.dns.errorCount |
| dt.host.dns.queries | builtin:host.dns.queryCount |
| dt.host.dns.query\_time | builtin:host.dns.queryTime |
| dt.host.dns.orphan\_count | builtin:host.dns.orphanCount |

### Disk

Which Metrics Classic disk metrics are not supported on Grail?

* builtin:host.disk.throughput.read
* builtin:host.disk.throughput.write

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.disk.avail | builtin:host.disk.avail |
| dt.host.disk.bytes\_read | builtin:host.disk.bytesRead |
| dt.host.disk.bytes\_written | builtin:host.disk.bytesWritten |
| dt.host.disk.free | builtin:host.disk.free |
| dt.host.disk.inodes\_avail | builtin:host.disk.inodesAvail |
| dt.host.disk.inodes\_total | builtin:host.disk.inodesTotal |
| dt.host.disk.queue\_length | builtin:host.disk.queueLength |
| dt.host.disk.read\_ops | builtin:host.disk.readOps |
| dt.host.disk.read\_time | builtin:host.disk.readTime |
| dt.host.disk.used | builtin:host.disk.used |
| dt.host.disk.used.percent | builtin:host.disk.usedPct |
| dt.host.disk.util\_time | builtin:host.disk.utilTime |
| dt.host.disk.write\_ops | builtin:host.disk.writeOps |
| dt.host.disk.write\_time | builtin:host.disk.writeTime |

### Memory

Which Metrics Classic memory metrics are not supported on Grail?

* builtin:host.mem.total

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.memory.avail.bytes | builtin:host.mem.avail.bytes |
| dt.host.memory.avail.percent | builtin:host.mem.avail.pct |
| dt.host.memory.avail.pfps | builtin:host.mem.avail.pfps |
| dt.host.memory.kernel | builtin:host.mem.kernel |
| dt.host.memory.recl | builtin:host.mem.recl |
| dt.host.memory.swap.avail | builtin:host.mem.swap.avail |
| dt.host.memory.swap.total | builtin:host.mem.swap.total |
| dt.host.memory.swap.used | builtin:host.mem.swap.used |
| dt.host.memory.usage | builtin:host.mem.usage |
| dt.host.memory.used | builtin:host.mem.used |

### Network

Which Metrics Classic network metrics are not supported on Grail?

Many Classic host-level network metrics can be reproduced using Grail NIC-level network metrics. Learn more in the above [section on new and missing metric keys](#new-and-missing-metric-keys).

The following Classic network metrics are planned but not yet supported on Grail:

* builtin:host.net.nic.connectivity
* builtin:host.net.nic.retransmission
* builtin:host.net.nic.retransmissionIn
* builtin:host.net.nic.retransmissionOut
* builtin:host.net.packets.lossRate

The following Classic network metrics are not supported on Grail:

* builtin:host.net.nic.packets.dropped
* builtin:host.net.nic.packets.errors
* builtin:host.net.nic.packets.traffic
* builtin:host.net.nic.traffic
* builtin:host.net.nic.trafficIn
* builtin:host.net.nic.trafficOut
* builtin:host.net.sessions.connFail

* builtin:host.net.bytesRx
* builtin:host.net.bytesTx
* builtin:host.net.packets.rxBaseReceived
* builtin:host.net.packets.rxBaseSent
* builtin:host.net.packets.rxReceived
* builtin:host.net.packets.rxSent
* builtin:host.net.sessions.errRst
* builtin:host.net.sessions.errTmout
* builtin:host.net.sessions.local.errRst
* builtin:host.net.sessions.local.errTmout
* builtin:host.net.sessions.local.new
* builtin:host.net.sessions.new

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.net.nic.bytes\_rx | builtin:host.net.nic.bytesRx |
| dt.host.net.nic.bytes\_tx | builtin:host.net.nic.bytesTx |
| dt.host.net.nic.link\_util\_rx | builtin:host.net.nic.linkUtilRx |
| dt.host.net.nic.link\_util\_tx | builtin:host.net.nic.linkUtilTx |
| dt.host.net.nic.packets.dropped\_rx | builtin:host.net.nic.packets.droppedRx |
| dt.host.net.nic.packets.dropped\_tx | builtin:host.net.nic.packets.droppedTx |
| dt.host.net.nic.packets.errors\_rx | builtin:host.net.nic.packets.errorsRx |
| dt.host.net.nic.packets.errors\_tx | builtin:host.net.nic.packets.errorsTx |
| dt.host.net.nic.packets.rx | builtin:host.net.nic.packets.rx |
| dt.host.net.nic.packets.tx | builtin:host.net.nic.packets.tx |

### Availability

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.availability | builtin:host.availability.state |
| dt.host.uptime | builtin:host.uptime |
| dt.osservice.availability | builtin:osservice.availability |

### Other

What remaining Metrics Classic infrastructure metrics are not supported on Grail?

The following Metrics Classic infrastructure metrics are planned but not yet supported on Grail:

* builtin:host.osProcessStats.osProcessCount
* builtin:host.osProcessStats.pgiCount
* builtin:host.osProcessStats.pgiReportedCount

The following Classic infrastructure metrics are not supported on Grail:

* builtin:host.availability
* builtin:host.la.growth
* builtin:host.la.po
* builtin:host.la.to
* builtin:host.osService.availability
* builtin:host.processVisibility.topProcessesRecognizedCount
* builtin:host.processVisibility.topProcessesSentCount
* builtin:host.processVisibility.triggerCount

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.handles.file\_descriptors\_max | builtin:host.handles.fileDescriptorsMax |
| dt.host.handles.file\_descriptors\_used | builtin:host.handles.fileDescriptorsUsed |

## Kubernetes

ActiveGate version 1.279+

New Kubernetes metrics are now available for [DPS](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")-enabled customers with the launch of the new Kubernetes app. The new metrics are subject to a new licensing model, as distinct from the current full-stack host units model.

Metric availability:

* The old Kubernetes metrics are not available on Grail.
* The new Kubernetes metrics are available as soon as you start monitoring your cluster with the [new Kubernetes app](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads."). For more information on enabling this for your Kubernetes clusters, see [Getting started with Kubernetes experience](/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience "Enable Kubernetes experience for existing clusters or start monitoring new clusters.").
* Some of the new Kubernetes metrics are only available on Grail. They have no equivalent as Classic metrics.

More information:

* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Unlock the Power of DevSecOps with Newly Released Kubernetes Experience for Platform Engineeringï»¿](https://dt-url.net/c7038ec)
* [Dynatrace Launches New Kubernetes Experience for Platform Engineering Teamsï»¿](https://dt-url.net/882385r)
* [Kubernetes metric migration guide](/docs/analyze-explore-automate/metrics/upgrade/kubernetes-metric-migration "Learn more about Kubernetes metrics migration from Classic to Grail.")

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.kubernetes.container.requests\_cpu | builtin:kubernetes.workload.requests\_cpu, builtin:kubernetes.node.requests\_cpu |
| dt.kubernetes.container.limits\_cpu | builtin:kubernetes.workload.limits\_cpu, builtin:kubernetes.node.limits\_cpu |
| dt.kubernetes.container.requests\_memory | builtin:kubernetes.workload.requests\_memory, builtin:kubernetes.node.requests\_memory |
| dt.kubernetes.container.limits\_memory | builtin:kubernetes.workload.limits\_memory, builtin:kubernetes.node.limits\_memory |
| dt.kubernetes.container.cpu\_usage | builtin:kubernetes.workload.cpu\_usage, builtin:kubernetes.node.cpu\_usage |
| dt.kubernetes.container.cpu\_throttled | builtin:kubernetes.workload.cpu\_throttled, builtin:kubernetes.node.cpu\_throttled |
| dt.kubernetes.container.memory\_working\_set | builtin:kubernetes.workload.memory\_working\_set, builtin:kubernetes.node.memory\_working\_set |
| dt.kubernetes.nodes | builtin:kubernetes.nodes |
| dt.kubernetes.workloads | builtin:kubernetes.workloads |
| dt.kubernetes.pods | builtin:kubernetes.pods, builtin:kubernetes.node.pods |
| dt.kubernetes.containers | builtin:kubernetes.containers |
| dt.kubernetes.workload.pods\_desired | builtin:kubernetes.workload.pods\_desired |
| dt.kubernetes.pod.containers\_desired | builtin:kubernetes.workload.containers\_desired |
| dt.kubernetes.events | builtin:kubernetes.events |
| dt.kubernetes.node.cpu\_allocatable | builtin:kubernetes.node.cpu\_allocatable |
| dt.kubernetes.node.memory\_allocatable | builtin:kubernetes.node.memory\_allocatable |
| dt.kubernetes.node.pods\_allocatable | builtin:kubernetes.node.pods\_allocatable |
| dt.kubernetes.node.conditions | builtin:kubernetes.node.conditions |
| dt.kubernetes.workload.conditions | builtin:kubernetes.workload.conditions |
| dt.kubernetes.cluster.readyz | builtin:kubernetes.cluster.readyz |
| dt.kubernetes.resourcequota.requests\_cpu | builtin:kubernetes.resourcequota.requests\_cpu |
| dt.kubernetes.resourcequota.requests\_cpu\_used | builtin:kubernetes.resourcequota.requests\_cpu\_used |
| dt.kubernetes.resourcequota.limits\_cpu | builtin:kubernetes.resourcequota.limits\_cpu |
| dt.kubernetes.resourcequota.limits\_cpu\_used | builtin:kubernetes.resourcequota.limits\_cpu\_used |
| dt.kubernetes.resourcequota.requests\_memory | builtin:kubernetes.resourcequota.requests\_memory |
| dt.kubernetes.resourcequota.requests\_memory\_used | builtin:kubernetes.resourcequota.requests\_memory\_used |
| dt.kubernetes.resourcequota.limits\_memory | builtin:kubernetes.resourcequota.limits\_memory |
| dt.kubernetes.resourcequota.limits\_memory\_used | builtin:kubernetes.resourcequota.limits\_memory\_used |
| dt.kubernetes.resourcequota.pods | builtin:kubernetes.resourcequota.pods |
| dt.kubernetes.resourcequota.pods\_used | builtin:kubernetes.resourcequota.pods\_used |
| dt.kubernetes.container.oom\_kills | builtin:kubernetes.container.oom\_kills |
| dt.kubernetes.container.restarts | builtin:kubernetes.container.restarts |
| dt.kubernetes.persistentvolumeclaim.available | builtin:kubernetes.persistentvolumeclaim.available |
| dt.kubernetes.persistentvolumeclaim.capacity | builtin:kubernetes.persistentvolumeclaim.capacity |
| dt.kubernetes.persistentvolumeclaim.used | builtin:kubernetes.persistentvolumeclaim.used |

The following Kubernetes-related metrics are only available on Grail.

| Metric key (Grail) |
| --- |
| dt.kubernetes.pod.network\_received\_data |
| dt.kubernetes.pod.network\_received\_errors |
| dt.kubernetes.pod.network\_received\_packets\_dropped |
| dt.kubernetes.pod.network\_transmitted\_data |
| dt.kubernetes.pod.network\_transmitted\_errors |
| dt.kubernetes.pod.network\_transmitted\_packets\_dropped |

## Mainframe

### Host (Logical partition)

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.zos.gcp\_time | builtin:host.zos.gcpu\_time |
| dt.host.zos.gcp\_usage | builtin:host.cpu.gcpu.usage |
| dt.host.zos.msu\_capacity | builtin:host.cpu.msu.capacity |
| dt.host.zos.msu\_hours | builtin:host.zos.msu\_hours |
| dt.host.zos.msu\_r4ha | builtin:host.cpu.msu.avg |
| dt.host.zos.ziip\_eligible\_time | builtin:host.cpu.ziip.eligible |
| dt.host.zos.ziip\_time | builtin:host.zos.ziip\_time |
| dt.host.zos.ziip\_usage | builtin:host.zos.ziip\_usage |

### Process (Subsystem)

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.process.zos.gcp\_time | builtin:tech.generic.gcpu.time |
| dt.process.zos.gcp\_usage | builtin:tech.generic.gcpu.usage |
| dt.process.zos.service\_units | builtin:tech.zos.consumed\_service\_units |
| dt.process.zos.ziip\_eligible\_time | builtin:tech.generic.ziipEligible |
| dt.process.zos.ziip\_time | builtin:tech.generic.ziip |

### JVM

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.jvm.classes.loaded | builtin:tech.jvm.classes.loaded |
| dt.runtime.jvm.classes.total | builtin:tech.jvm.classes.total |
| dt.runtime.jvm.classes.unloaded | builtin:tech.jvm.classes.unloaded |
| dt.runtime.jvm.gc.collection\_count | builtin:tech.jvm.memory.pool.collectionCount |
| dt.runtime.jvm.gc.collection\_time | builtin:tech.jvm.memory.pool.collectionTime |
| dt.runtime.jvm.gc.suspension\_time | builtin:tech.jvm.memory.gc.suspensionTime |
| dt.runtime.jvm.gc.total\_activation\_count | builtin:tech.jvm.memory.gc.activationCount |
| dt.runtime.jvm.gc.total\_collection\_time | builtin:tech.jvm.memory.gc.collectionTime |
| dt.runtime.jvm.memory.free | builtin:tech.jvm.memory.runtime.free |
| dt.runtime.jvm.memory.max | builtin:tech.jvm.memory.runtime.max |
| dt.runtime.jvm.memory\_pool.committed | builtin:tech.jvm.memory.pool.committed |
| dt.runtime.jvm.memory\_pool.max | builtin:tech.jvm.memory.pool.max |
| dt.runtime.jvm.memory\_pool.used | builtin:tech.jvm.memory.pool.used |
| dt.runtime.jvm.memory.total | builtin:tech.jvm.memory.runtime.total |
| dt.runtime.jvm.pgi.cpu\_time\_suspension | builtin:tech.generic.cpu.groupSuspensionTime |
| dt.runtime.jvm.threads.count | builtin:tech.jvm.threads.count |

### WebSphere Application Server

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.websphere.connectionpool.concurrent\_waiters | builtin:tech.websphere.connectionPool.connectionPoolModule.WaitingThreadCount |
| dt.runtime.websphere.connectionpool.free\_pool\_size | builtin:tech.websphere.connectionPool.connectionPoolModule.FreePoolSize |
| dt.runtime.websphere.connectionpool.in\_use\_time | builtin:tech.websphere.connectionPool.connectionPoolModule.UseTime |
| dt.runtime.websphere.connectionpool.percent\_used | builtin:tech.websphere.connectionPool.connectionPoolModule.PercentUsed |
| dt.runtime.websphere.connectionpool.pool\_size | builtin:tech.websphere.connectionPool.connectionPoolModule.PoolSize |
| dt.runtime.websphere.connectionpool.wait\_time | builtin:tech.websphere.connectionPool.connectionPoolModule.WaitTime |
| dt.runtime.websphere.threadpool.active\_threads | builtin:tech.websphere.threadPoolModule.ActiveCount |
| dt.runtime.websphere.threadpool.pool\_size | builtin:tech.websphere.threadPoolModule.PoolSize |
| dt.runtime.websphere.servlet.live\_sessions | builtin:tech.websphere.servletSessionsModule.LiveCount |
| dt.runtime.websphere.servlet.requests | builtin:tech.websphere.webAppModule.RequestCountV2 |

### WebSphere Liberty / z/OS Connect

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.websphere.connectionpool.in\_use\_time | builtin:tech.liberty.connectionPool.InUseTime |
| dt.runtime.websphere.connectionpool.liberty.connection\_handles | builtin:tech.liberty.connectionPool.ConnectionHandleCount |
| dt.runtime.websphere.connectionpool.liberty.free\_connections | builtin:tech.liberty.connectionPool.FreeConnectionCount |
| dt.runtime.websphere.connectionpool.liberty.managed\_connections | builtin:tech.liberty.connectionPool.ManagedConnectionCount |
| dt.runtime.websphere.connectionpool.wait\_time | builtin:tech.liberty.connectionPool.WaitTime |
| dt.runtime.websphere.threadpool.active\_threads | builtin:tech.liberty.ActiveThreads |
| dt.runtime.websphere.threadpool.pool\_size | builtin:tech.liberty.poolsize |
| dt.runtime.websphere.servlet.requests | builtin:tech.liberty.RequestCount |

## Runtimes

OneAgent version 1.283+

We modified the availability of technology-specific metrics in Grail, which might affect the direct relation between Metrics Classic and Grail metric keys. Select  to learn more about the change.

### Apache

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.apache.connections.socket\_waiting\_time | builtin:tech.webserver.connections.socketWaitingTime |
| dt.runtime.apache.requests | builtin:tech.webserver.requests |
| dt.runtime.apache.threads.active | builtin:tech.webserver.threads.active |
| dt.runtime.apache.threads.idle | builtin:tech.webserver.threads.idle |
| dt.runtime.apache.threads.max | builtin:tech.webserver.threads.max |
| dt.runtime.apache.traffic | builtin:tech.webserver.traffic |

### Go

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.go.cf.auctioneer\_fetch\_states\_duration | builtin:cloud.cloudfoundry.auctioneer.fetchDuration (filtered by process type Go) |
| dt.runtime.go.cf.auctioneer\_lrp\_auctions | builtin:cloud.cloudfoundry.auctioneer.lprFailed (filtered by process type Go)   builtin:cloud.cloudfoundry.auctioneer.lprStarted (filtered by process type Go) |
| dt.runtime.go.cf.auctioneer\_task\_auctions\_failed | builtin:cloud.cloudfoundry.auctioneer.taskFailed (filtered by process type Go) |
| dt.runtime.go.gc.collection\_count | builtin:tech.go.memory.gcCount |
| dt.runtime.go.gc.collection\_time | builtin:tech.jvm.memory.gc.collectionTime |
| dt.runtime.go.gc.suspension\_time | builtin:tech.jvm.memory.gc.suspensionTime |
| dt.runtime.go.http.latency | builtin:tech.go.http.latency |
| dt.runtime.go.http.requests | builtin:tech.go.http.badGateways   builtin:tech.go.http.responses5xx   builtin:tech.go.http.totalRequests |
| dt.runtime.go.memory.committed | builtin:tech.go.memory.pool.committed |
| dt.runtime.go.memory.heap | builtin:tech.go.memory.heap.idle   builtin:tech.go.memory.heap.live |
| dt.runtime.go.memory.heap.object\_count | builtin:tech.go.memory.heap.objCount |
| dt.runtime.go.memory.used | builtin:tech.go.memory.pool.used |
| dt.runtime.go.cgo\_calls | builtin:tech.go.native.cgoCalls |
| dt.runtime.go.sys\_calls | builtin:tech.go.native.sysCalls |
| dt.process.go.scheduling.g.avg\_num\_of\_active\_routines | builtin:tech.go.scheduling.g.avgNumOfActiveRoutines |
| dt.process.go.scheduling.g.avg\_num\_of\_inactive\_routines | builtin:tech.go.scheduling.g.avgNumOfInactiveRoutines |
| dt.runtime.go.scheduler.context.idle\_count | builtin:tech.go.scheduling.p.idleCount |
| dt.runtime.go.scheduler.goroutine\_count | builtin:tech.go.scheduling.g.runningCount   builtin:tech.go.scheduling.g.systemCount |
| dt.runtime.go.scheduler.queue\_size | builtin:tech.go.scheduling.globalQSize |
| dt.runtime.go.scheduler.worker\_thread\_count | builtin:tech.go.scheduling.m.count   builtin:tech.go.scheduling.m.idlingCount   builtin:tech.go.scheduling.m.spinningCount |

### IIS

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.iis.connections.socket\_waiting\_time | builtin:tech.webserver.connections.socketWaitingTime |
| dt.runtime.iis.requests | builtin:tech.webserver.requests |
| dt.runtime.iis.threads.active | builtin:tech.webserver.threads.active |
| dt.runtime.iis.threads.idle | builtin:tech.webserver.threads.idle |
| dt.runtime.iis.threads.idle | builtin:tech.webserver.threads.max |
| dt.runtime.iis.traffic | builtin:tech.webserver.traffic |

### Java

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.jvm.classes.loaded | builtin:tech.jvm.classes.loaded |
| dt.runtime.jvm.classes.total | builtin:tech.jvm.classes.total |
| dt.runtime.jvm.classes.unloaded | builtin:tech.jvm.classes.unloaded |
| dt.runtime.jvm.gc.collection\_count | builtin:tech.jvm.memory.pool.collectionCount |
| dt.runtime.jvm.gc.collection\_time | builtin:tech.jvm.memory.pool.collectionTime |
| dt.runtime.jvm.gc.suspension\_time | builtin:tech.jvm.memory.gc.suspensionTime |
| dt.runtime.jvm.gc.total\_activation\_count | builtin:tech.jvm.memory.gc.activationCount |
| dt.runtime.jvm.gc.total\_collection\_time | builtin:tech.jvm.memory.gc.collectionTime |
| dt.profiling.jvm.memory.allocation\_bytes | builtin:tech.jvm.memory.memAllocationBytes |
| dt.profiling.jvm.memory.allocation\_count | builtin:tech.jvm.memory.memAllocationCount |
| dt.profiling.jvm.memory.survivor\_bytes | builtin:tech.jvm.memory.memSurvivorsBytes |
| dt.profiling.jvm.memory.survivor\_count | builtin:tech.jvm.memory.memSurvivorsCount |
| dt.profiling.jvm.threads.active | builtin:tech.jvm.threads.avgActiveThreadCount |
| dt.runtime.jvm.memory\_pool.committed | builtin:tech.jvm.memory.pool.committed |
| dt.runtime.jvm.memory.free | builtin:tech.jvm.memory.runtime.free |
| dt.runtime.jvm.memory.max | builtin:tech.jvm.memory.runtime.max |
| dt.runtime.jvm.memory\_pool.max | builtin:tech.jvm.memory.pool.max |
| dt.runtime.jvm.memory\_pool.used | builtin:tech.jvm.memory.pool.used |
| dt.runtime.jvm.memory.total | builtin:tech.jvm.memory.runtime.total |
| dt.runtime.jvm.pgi.cpu\_time\_suspension | builtin:tech.generic.cpu.groupSuspensionTime |
| dt.profiling.jvm.threads.inactive | builtin:tech.jvm.threads.avgInactiveThreadCount |
| dt.runtime.jvm.threads.count | builtin:tech.jvm.threads.count |
| dt.profiling.jvm.threads.cpu\_time | builtin:tech.jvm.threads.totalCpuTime |

### NGINX

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.nginx.connections.dropped | builtin:tech.webserver.connections.dropped |
| dt.runtime.nginx.connections.handled | builtin:tech.webserver.connections.handled |
| dt.runtime.nginx.connections.reading | builtin:tech.webserver.connections.reading |
| dt.runtime.nginx.connections.waiting | builtin:tech.webserver.connections.waiting |
| dt.runtime.nginx.connections.writing | builtin:tech.webserver.connections.writing |
| dt.runtime.nginx.plus.cache.hits | builtin:tech.nginx.cache.hits |
| dt.runtime.nginx.plus.cache.max\_space | builtin:tech.nginx.cache.freeSpace |
| dt.runtime.nginx.plus.cache.misses | builtin:tech.nginx.cache.misses |
| dt.runtime.nginx.plus.cache.used\_space | builtin:tech.nginx.cache.usedSpace |
| dt.runtime.nginx.plus.server\_zones.requests | builtin:tech.nginx.serverZones.requests |
| dt.runtime.nginx.plus.server\_zones.traffic\_in | builtin:tech.nginx.serverZones.trafficIn |
| dt.runtime.nginx.plus.server\_zones.traffic\_out | builtin:tech.nginx.serverZones.trafficOut |
| dt.runtime.nginx.plus.upstream.healthy | builtin:tech.nginx.upstream.healthy |
| dt.runtime.nginx.plus.upstream.requests | builtin:tech.nginx.upstream.requests |
| dt.runtime.nginx.plus.upstream.traffic\_in | builtin:tech.nginx.upstream.trafficIn |
| dt.runtime.nginx.plus.upstream.traffic\_out | builtin:tech.nginx.upstream.trafficOut |
| dt.runtime.nginx.plus.upstream.unhealthy | builtin:tech.nginx.upstream.unhealthy |
| dt.runtime.nginx.requests | builtin:tech.webserver.requests |
| dt.runtime.nginx.traffic | builtin:tech.webserver.traffic |

### .NET

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.clr.gc.collection\_count | builtin:tech.dotnet.gc.gen0Collections   builtin:tech.dotnet.gc.gen1Collections   builtin:tech.dotnet.gc.gen2Collections |
| dt.runtime.clr.gc.collection\_time | builtin:tech.jvm.memory.gc.collectionTime |
| dt.runtime.clr.gc.suspension\_time | builtin:tech.jvm.memory.gc.suspensionTime |
| dt.runtime.clr.gc.time\_percentage | builtin:tech.dotnet.gc.timePercentage |
| dt.runtime.clr.jit.time\_percentage | builtin:tech.dotnet.jit.timePercentage |
| dt.profiling.clr.threads.count | builtin:tech.dotnet.managedThreads.avgNumOfActiveThreads |
| dt.runtime.clr.memory.consumption | builtin:tech.dotnet.memory.gen0Consumption   builtin:tech.dotnet.memory.gen1Consumption   builtin:tech.dotnet.memory.gen2Consumption   builtin:tech.dotnet.memory.LOHConsumption |
| dt.runtime.clr.threadpool.queued\_work\_items | builtin:tech.dotnet.threadpool.queuedWorkItems |
| dt.runtime.clr.threadpool.threads | builtin:tech.dotnet.threadpool.ioCompletionThreads   builtin:tech.dotnet.threadpool.workerThreads |

### Node.js

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.process.nodejs.avg\_number\_of\_active\_threads | builtin:tech.nodejs.avgNumberOfActiveThreads |
| dt.runtime.nodejs.eventloop.active\_handles | builtin:tech.nodejs.uvLoop.activeHandles |
| dt.runtime.nodejs.eventloop.utilization | builtin:tech.nodejs.uvLoop.utilization |
| dt.runtime.nodejs.gc.collection\_time | builtin:tech.jvm.memory.pool.collectionTime |
| dt.runtime.nodejs.gc.suspension\_time | builtin:tech.jvm.memory.gc.suspensionTime |
| dt.runtime.nodejs.memory.used | builtin:tech.nodejs.v8heap.used |
| dt.runtime.nodejs.memory.total | builtin:tech.nodejs.v8heap.total |

### PHP

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.runtime.php.gc.collected\_count | builtin:tech.php.phpGc.collectedCount |
| dt.runtime.php.gc.duration\_ms | builtin:tech.php.phpGc.durationMs |
| dt.runtime.php.gc.effectiveness | builtin:tech.php.phpGc.effectiveness |
| dt.runtime.php.jit.buffer\_free | builtin:tech.php.phpOpcache.jit.bufferFree |
| dt.runtime.php.jit.buffer\_size | builtin:tech.php.phpOpcache.jit.bufferSize |
| dt.runtime.php.opcache.blocklist\_misses | builtin:tech.php.phpOpcache.statistics.blocklistMisses |
| dt.runtime.php.opcache.cached\_keys | builtin:tech.php.phpOpcache.statistics.cachedKeys |
| dt.runtime.php.opcache.cached\_scripts | builtin:tech.php.phpOpcache.statistics.cachedScripts |
| dt.runtime.php.opcache.hits | builtin:tech.php.phpOpcache.statistics.hits |
| dt.runtime.php.opcache.max\_cached\_keys | builtin:tech.php.phpOpcache.statistics.maxCachedCachedKeys |
| dt.runtime.php.opcache.memory.free | builtin:tech.php.phpOpcache.memory.free |
| dt.runtime.php.opcache.memory.used | builtin:tech.php.phpOpcache.memory.used |
| dt.runtime.php.opcache.memory.wasted | builtin:tech.php.phpOpcache.memory.wasted |
| dt.runtime.php.opcache.misses | builtin:tech.php.phpOpcache.statistics.misses |
| dt.runtime.php.opcache.number\_of\_strings | builtin:tech.php.phpOpcache.strings.numberOfStrings |
| dt.runtime.php.opcache.restarts\_hash | builtin:tech.php.phpOpcache.restarts.hash |
| dt.runtime.php.opcache.restarts\_manual | builtin:tech.php.phpOpcache.restarts.manual |
| dt.runtime.php.opcache.restarts\_out\_of\_memory | builtin:tech.php.phpOpcache.restarts.outOfMemory |
| dt.runtime.php.opcache.strings\_buffer\_size | builtin:tech.php.phpOpcache.strings.bufferSize |
| dt.runtime.php.opcache.strings\_used\_memory | builtin:tech.php.phpOpcache.strings.usedMemory |
| dt.process.php.threads.avg\_num\_of\_active\_threads | builtin:tech.php.threads.avgNumOfActiveThreads |
| dt.process.php.threads.avg\_num\_of\_inactive\_threads | builtin:tech.php.threads.avgNumOfInactiveThreads |

## Processes

Process metrics replace Metrics Classic generic technology metrics with the prefix `builtin:tech.generic`.

Which Metrics Classic generic technology metrics are not supported on Grail?

The following Metrics Classic generic technology metrics are planned but not yet supported on Grail:

* builtin:tech.generic.network.packets.retransmission
* builtin:tech.generic.network.packets.retransmissionIn
* builtin:tech.generic.network.packets.retransmissionOut
* builtin:tech.generic.network.sessions.connectivity

The following Metrics Classic generic technology metrics are not supported on Grail:

* builtin:tech.generic.network.traffic.traffic
* builtin:tech.generic.network.traffic.trafficIn
* builtin:tech.generic.network.traffic.trafficOut

* builtin:process.bytesReceived
* builtin:process.bytesSent
* builtin:process.cpu
* builtin:process.memory
* builtin:tech.customDevice.count

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.process.availability | builtin:pgi.availability.state |
| dt.process.cpu.usage | builtin:tech.generic.cpu.usage |
| dt.process.handles.file\_descriptors\_max | builtin:tech.generic.handles.fileDescriptorsMax |
| dt.process.handles.file\_descriptors\_percent\_used | builtin:tech.generic.handles.fileDescriptorsPercentUsed |
| dt.process.handles.file\_descriptors\_used | builtin:tech.generic.handles.fileDescriptorsUsed |
| dt.process.io.bytes\_read | builtin:tech.generic.io.bytesRead |
| dt.process.io.bytes\_written | builtin:tech.generic.io.bytesWritten |
| dt.process.io.bytes\_total | builtin:tech.generic.io.bytesTotal |
| dt.process.io.req\_bytes\_read | builtin:tech.generic.io.reqBytesRead |
| dt.process.io.req\_bytes\_write | builtin:tech.generic.io.reqBytesWrite |
| dt.process.memory.exhausted\_memory | builtin:tech.generic.mem.exhaustedMem |
| dt.process.memory.page\_faults | builtin:tech.generic.mem.pageFaults |
| dt.process.memory.usage | builtin:tech.generic.mem.usage |
| dt.process.memory.working\_set\_size | builtin:tech.generic.mem.workingSetSize |
| dt.process.network.bytes\_rx | builtin:tech.generic.network.bytesRx |
| dt.process.network.bytes\_tx | builtin:tech.generic.network.bytesTx |
| dt.process.network.latency | builtin:tech.generic.network.latency |
| dt.process.network.load | builtin:tech.generic.network.load |
| dt.process.network.packets.base\_re\_rx | builtin:tech.generic.network.packets.baseReRx |
| dt.process.network.packets.base\_re\_rx\_aggr | builtin:tech.generic.network.packets.baseReRxAggr |
| dt.process.network.packets.base\_re\_tx | builtin:tech.generic.network.packets.baseReTx |
| dt.process.network.packets.base\_re\_tx\_aggr | builtin:tech.generic.network.packets.baseReTxAggr |
| dt.process.network.packets.re\_rx | builtin:tech.generic.network.packets.reRx |
| dt.process.network.packets.re\_rx\_aggr | builtin:tech.generic.network.packets.reRxAggr |
| dt.process.network.packets.re\_tx | builtin:tech.generic.network.packets.reTx |
| dt.process.network.packets.re\_tx\_aggr | builtin:tech.generic.network.packets.reTxAggr |
| dt.process.network.packets.rx | builtin:tech.generic.network.packets.rx |
| dt.process.network.packets.tx | builtin:tech.generic.network.packets.tx |
| dt.process.network.round\_trip | builtin:tech.generic.network.roundTrip |
| dt.process.network.sessions.new | builtin:tech.generic.network.sessions.new |
| dt.process.network.sessions.new\_aggr | builtin:tech.generic.network.sessions.newAggr |
| dt.process.network.sessions.new\_local | builtin:tech.generic.network.sessions.newLocal |
| dt.process.network.sessions.reset | builtin:tech.generic.network.sessions.reset |
| dt.process.network.sessions.reset\_aggr | builtin:tech.generic.network.sessions.resetAggr |
| dt.process.network.sessions.reset\_local | builtin:tech.generic.network.sessions.resetLocal |
| dt.process.network.sessions.timeout | builtin:tech.generic.network.sessions.timeout |
| dt.process.network.sessions.timeout\_aggr | builtin:tech.generic.network.sessions.timeoutAggr |
| dt.process.network.sessions.timeout\_local | builtin:tech.generic.network.sessions.timeoutLocal |
| dt.process.network.throughput | builtin:tech.generic.network.throughput |
| dt.process.threads\_exhausted | builtin:tech.generic.threadsExhausted |
| dt.process.process\_count | builtin:tech.generic.processCount |

### Nettracer

Which Metrics Classic nettracer metrics are not supported on Grail?

The following Metrics Classic nettracer metrics are planned but not yet supported on Grail:

* builtin:tech.nettracer.retr\_percentage

The following Metrics Classic nettracer metrics are not supported on Grail:

* builtin:tech.nettracer.traffic
* builtin:tech.nettracer.traffic\_rx
* builtin:tech.nettracer.traffic\_tx

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.process.nettracer.bytes\_rx | builtin:tech.nettracer.bytes\_rx |
| dt.process.nettracer.bytes\_tx | builtin:tech.nettracer.bytes\_tx |
| dt.process.nettracer.pkts\_retr | builtin:tech.nettracer.pkts\_retr |
| dt.process.nettracer.pkts\_rx | builtin:tech.nettracer.pkts\_rx |
| dt.process.nettracer.pkts\_tx | builtin:tech.nettracer.pkts\_tx |
| dt.process.nettracer.rtt | builtin:tech.nettracer.rtt |

## Security

Security metrics have been replaced with [security events](/docs/secure/threat-observability/concepts#security-events "Basic concepts related to Threat Observability"). Consequently, security metrics are not supported on Grail. This affects all metrics with the prefix `builtin:security`.

## Services

We modified the availability of service metrics in Grail, which might affect the direct relation between Metrics Classic and Grail metric keys. Select  to learn more about the change.

### Calculated service metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| service.`<my_calculated_service_metric>` | calc:service:`<my_calculated_service_metric>` |

Dimensions in Grail

With the upgrade of calculated service metrics to Grail, the existing dimension is mantained and any placeholders used in the dimension value are separated into additional distinct metric dimensions, that allow you to do querying in a simplified and more powerful way. The following sections list the availability of dimensions once you enable a calculated service metric in Grail.

#### New dimensions

The following dimensions are added to calculated service metrics in Grail. They apply only to full requests, unless specified differently.

* aws.tags.\*
* azure.tags.\*
* dt.cost.costcenter [1](#fn-1-1-def)
* dt.cost.product [1](#fn-1-1-def)
* dt.entity.kubernetes\_cluster
* dt.entity.process\_group [1](#fn-1-1-def)
* dt.host\_group.id
* dt.security\_context [1](#fn-1-1-def)
* dt.service.name [1](#fn-1-1-def)
* failed (`true` or `false`) [1](#fn-1-1-def)
* gcp.tags.\*
* k8s.cluster.name
* k8s.cluster.uid
* k8s.namespace.annotation.\*
* k8s.namespace.label.\*
* k8s.namespace.name
* k8s.pod.annotation.\*
* k8s.pod.label.\*
* k8s.workload.name
* k8s.workload.annotation.\*
* k8s.workload.kind
* k8s.workload.label.\*
* primary\_tags.\*
* service.name

1

Applicable to both full and external requests. To learn more about requests types, see [Glossary - request](/docs/discover-dynatrace/get-started/glossary#request "Get acquainted with Dynatrace terminology.").

#### Dimensions automatically converted from Classic metric placeholders

In Grail, placeholders used in the [**Dimension value pattern**](/docs/observe/application-observability/services/calculated-service-metric#create "Learn how to create a calculated metric based on web requests.") are mapped to distinct dimension keys, allowing more flexibility and powerful querying. The following Grail dimension keys are automatically created from the placeholders contained in your Classic dimension, according to [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

**Metric dimension (Grail)**: **Metric placeholder (Classic)**

* cics.transaction.system\_id: CICS:SystemId
* cics.transaction.task\_id: CICS:TaskId (INTEGER)
* cics.transaction.user\_id: CICS:UserId
* code.function: RMI:Method
* code.namespace: RMI:Class
* ctg.request.gateway\_url: CTG:GatewayURL
* ctg.request.server\_id: CTG:ServerName
* custom\_service.method: CustomService:Method
* custom\_service.name: CustomService:Class
* db.connection\_string: Database:URL
* db.namespace: Database:Name
* db.query.text: Database-Statement
* db.system: Database:Type
* deployment.release\_build\_version: Request:ApplicationBuildVersion
* deployment.release\_product: Request:ApplicationProduct
* deployment.release\_stage: Request:ApplicationStage
* deployment.release\_version: Request:ApplicationReleaseVersion
* endpoint.name: Request:Name
* exception.message: Exception:Message
* exception.type: Exception:Class
* http.request.method: HTTP-Method
* http.response.status\_code: HTTP-Status
* http.server\_name: Service:WebServerName
* ibm.cics.program: CICS:ProgramName
* messaging.akka.actor.path: AKKA:ActorPath
* messaging.akka.actor.system: AKKA:ActorSystem
* messaging.akka.actor.type: AKKA:ActorClassName
* messaging.akka.message.type: AKKA:ActorMessageType
* messaging.source.kind: Messaging:DestinationType
* messaging.source.name: Messaging:QueueName
* messaging.source.temporary: Messaging:IsTemporary
* messaging.system: Messaging:QueueVendor
* request\_attribute.**attribute\_name**: RequestAttribute:, BEGINS\_WITH
* rpc.method: Remote:Method
* rpc.namespace: Service:WebServiceNamespace
* rpc.service: Service:WebServiceName
* server.address: Database:Host
* servlet.context.name: Service:WebApplicationId
* servlet.context.path: Service:WebContextRoot
* url.domain: URL:Host
* url.full: URL
* url.path: URL:Path
* url.port: URL:Port
* url.query: URL:Query
* zos.transaction.id: CICS:TransactionId
* zos.transaction.id: CTG:TransactionId
* zos.transaction.id: IMS:TransactionId

#### Unsupported placeholders

The following placeholders are not mapped to distinct Grail metric dimension keys because they either do not align with the Dynatrace Semantic Dictionary used in Grail or represent concepts that are no longer relevant within the context of Grail metrics. Placeholder values remain accessible through the dimension created when the calculated service metric was initially defined. If needed, you can use string operations to extract and work with the specific placeholder values.

* AzureFunctions:FunctionName
* AzureFunctions:SiteName
* ESB:ApplicationName
* ESB:LibraryName
* ESB:MessageFlowName
* HTTP-StatusClass

  Go to **Settings Classic** and modify the metric definition to use `HTTP-Status` instead. These placeholders are then automatically converted.
* IMS:ProgramName
* IMS:UserId
* Remote:Endpoint
* Request:Failure
* Request:IsKeyRequest
* Request:Type
* Relative-URL

  Go to **Settings Classic** and modify the metric definition to use `URL:Path` and `URL:Query` instead. These placeholders are then automatically converted.
* Service:Istance
* Service:Name

  In **Notebooks**, use `entityName(dt.entity.service)` to obtain comparable results.
* Service:Port
* Service:PublicDomainName
* WebService:Endpoint

  In **Notebooks**, use `entityName(dt.entity.service)` to obtain comparable results.
* WebService:Method

  Go to **Settings Classic** and modify the metric definition to use `Request:Name` instead. This placeholder is then automatically converted.

### Message processing

| Metric key (Grail) | Metric key (Classic) | Description | Unit |
| --- | --- | --- | --- |
| dt.service.messaging.publish.count | None | The number of messages sent to queues or topics. | count |
| dt.service.messaging.receive.count | None | The number of messages received from queues or topics. | count |
| dt.service.messaging.process.count | None | The number of messages successfully processed. | count |
| dt.service.messaging.process.failure\_count | None | The number of messages that failed processing. | count |

### Dimensions in Grail

The new metrics for queues support the following dimensions.

| Dimension | Description | Example values |
| --- | --- | --- |
| messaging.destination.name | The name of the queue or topic | `authorQueue`, `orderEvents` |
| dt.entity.service | The service identifier | `spring-kafka-producer` |
| messaging.system | The messaging platform | `kafka`, `rabbitmq`, `aws_sqs` |
| aws.account.id | The AWS account identifier | `123456789012` |
| aws.region | The AWS region | `us-east-1` |
| k8s.cluster.name | The name of the Kubernetes cluster | `prod-cluster` |
| k8s.namespace.name | The name of the Kubernetes namespace | `payment-services` |

### Endpoints

Metric key (Grail)

Metric key (Classic)

dt.service.request.count

builtin:service.errors.client.successCount   
builtin:service.errors.fivexx.count   
builtin:service.errors.fivexx.rate   
builtin:service.errors.fivexx.successCount   
builtin:service.errors.fourxx.count   
builtin:service.errors.fourxx.rate   
builtin:service.errors.fourxx.successCount   
builtin:service.errors.server.count   
builtin:service.errors.server.rate   
builtin:service.errors.server.successCount   
builtin:service.errors.total.rate   
builtin:service.errors.total.successCount   
builtin:service.keyRequest.count.client   
builtin:service.keyRequest.count.server   
builtin:service.keyRequest.count.total   
builtin:service.keyRequest.errors.client.successCount   
builtin:service.keyRequest.errors.fivexx.count   
builtin:service.keyRequest.errors.fivexx.rate   
builtin:service.keyRequest.errors.fivexx.successCount   
builtin:service.keyRequest.errors.fourxx.count   
builtin:service.keyRequest.errors.fourxx.rate   
builtin:service.keyRequest.errors.fourxx.successCount   
builtin:service.keyRequest.errors.server.count   
builtin:service.keyRequest.errors.server.rate   
builtin:service.keyRequest.errors.server.successCount   
builtin:service.keyRequest.successes.server.rate   
builtin:service.request.count  
builtin:service.request.count\_chart  
builtin:service.request.count\_service\_aggregation  
builtin:service.requestCount.client  
builtin:service.requestCount.server  
builtin:service.requestCount.total  
builtin:service.successes.server.rate

dt.service.request.failure\_count

builtin:service.errors.client.count  
builtin:service.errors.client.rate  
builtin:service.errors.total.count  
builtin:service.keyRequest.errors.client.count   
builtin:service.keyRequest.errors.client.rate   
builtin:service.request.failure\_count  
builtin:service.request.failure\_count\_chart  
builtin:service.request.failure\_count\_service\_aggregation

dt.service.request.response\_time

builtin:service.keyRequest.response.client  
builtin:service.keyRequest.response.server  
builtin:service.keyRequest.response.time  
builtin:service.request.response\_time  
builtin:service.request.response\_time\_chart  
builtin:service.request.response\_time\_service\_aggregation  
builtin:service.response.client  
builtin:service.response.server  
builtin:service.response.time

### Message processing

| Metric key (Grail) | Metric key (Classic) | Description | Unit |
| --- | --- | --- | --- |
| dt.service.messaging.publish.count | None | The number of messages sent to queues or topics. | count |
| dt.service.messaging.receive.count | None | The number of messages received from queues or topics. | count |
| dt.service.messaging.process.count | None | The number of messages successfully processed. | count |
| dt.service.messaging.process.failure\_count | None | The number of messages that failed processing. | count |

### Dimensions in Grail

The new metrics for queues support the following dimensions.

| Dimension | Description | Example values |
| --- | --- | --- |
| messaging.destination.name | The name of the queue or topic | `authorQueue`, `orderEvents` |
| dt.entity.service | The service identifier | `spring-kafka-producer` |
| messaging.system | The messaging platform | `kafka`, `rabbitmq`, `aws_sqs` |
| aws.account.id | The AWS account identifier | `123456789012` |
| aws.region | The AWS region | `us-east-1` |
| k8s.cluster.name | The name of the Kubernetes cluster | `prod-cluster` |
| k8s.namespace.name | The name of the Kubernetes namespace | `payment-services` |

### Service mesh

Metric key (Grail)

Metric key (Classic)

dt.service.request.service\_mesh.count

builtin:service.request.service\_mesh.count  
builtin:service.request.service\_mesh.count\_service\_aggregation

dt.service.request.service\_mesh.failure\_count

builtin:service.request.service\_mesh.failure\_count  
builtin:service.request.service\_mesh.failure\_count\_service\_aggregation

dt.service.request.service\_mesh.response\_time

builtin:service.request.service\_mesh.response\_time  
builtin:service.request.service\_mesh.response\_time\_service\_aggregation

## Synthetic Monitoring

### HTTP monitor metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.http.response\_size | builtin:synthetic.http.responseSize.geo |
| dt.synthetic.http.duration | builtin:synthetic.http.duration.geo |
| dt.synthetic.http.dns | builtin:synthetic.http.dns.geo |
| dt.synthetic.http.tcp\_connect\_time | builtin:synthetic.http.tcpConnectTime.geo |
| dt.synthetic.http.tls\_handshake\_time | builtin:synthetic.http.tlsHandshakeTime.geo |
| dt.synthetic.http.time\_to\_first\_byte | builtin:synthetic.http.timeToFirstByte.geo |
| dt.synthetic.http.redirects\_count | builtin:synthetic.http.redirectsCount.geo |
| dt.synthetic.http.redirects\_time | builtin:synthetic.http.redirectsTime.geo |
| dt.synthetic.http.executions | builtin:synthetic.http.execution.status |
| dt.synthetic.http.duration\_threshold | builtin:synthetic.http.durationThreshold |
| dt.synthetic.http.request.duration | builtin:synthetic.http.request.duration.geo |
| dt.synthetic.http.request.response\_size | builtin:synthetic.http.request.responseSize.geo |
| dt.synthetic.http.request.tcp\_connect\_time | builtin:synthetic.http.request.tcpConnectTime.geo |
| dt.synthetic.http.request.tls\_handshake\_time | builtin:synthetic.http.request.tlsHandshakeTime.geo |
| dt.synthetic.http.request.time\_to\_first\_byte | builtin:synthetic.http.request.timeToFirstByte.geo |
| dt.synthetic.http.request.dns | builtin:synthetic.http.request.dns.geo |
| dt.synthetic.http.request.redirects\_count | builtin:synthetic.http.request.redirectsCount.geo |
| dt.synthetic.http.request.redirects\_time | builtin:synthetic.http.request.redirectsTime.geo |
| dt.synthetic.http.request.duration\_threshold | builtin:synthetic.http.request.durationThreshold |
| dt.synthetic.http.request.executions | N/A |
| dt.synthetic.http.availability | N/A |
| dt.synthetic.http.waiting\_time | N/A |
| dt.synthetic.http.request.waiting\_time | N/A |

### Browser monitor metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.browser.executions | N/A |
| dt.synthetic.browser.event.executions | N/A |
| dt.synthetic.browser.availability | N/A |
| dt.synthetic.browser.event.duration | N/A |
| dt.synthetic.browser.duration | N/A |

### Third party metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.third\_party.response\_time | builtin:synthetic.external.responseTime.geo |
| dt.synthetic.third\_party.quality | builtin:synthetic.external.quality.geo |
| dt.synthetic.third\_party.step.response\_time | builtin:synthetic.external.step.responseTime.geo |
| dt.synthetic.third\_party.executions | N/A |
| dt.synthetic.third\_party.step.executions | N/A |
| dt.synthetic.third\_party.availability | N/A |

### Network availability monitors metrics

#### Common monitor metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.multi\_protocol.execution\_time | builtin:synthetic.multiProtocol.executionTime |
| dt.synthetic.multi\_protocol.success\_rate | builtin:synthetic.multiProtocol.successRate |
| dt.synthetic.multi\_protocol.availability | builtin:synthetic.multiProtocol.availability |
| dt.synthetic.multi\_protocol.executions | builtin:synthetic.multiProtocol.executions |

#### Common step metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.multi\_protocol.step.execution\_time | builtin:synthetic.multiProtocol.step.executionTime |
| dt.synthetic.multi\_protocol.step.success\_rate | builtin:synthetic.multiProtocol.step.successRate |
| dt.synthetic.multi\_protocol.step.availability | builtin:synthetic.multiProtocol.step.availability |
| dt.synthetic.multi\_protocol.step.executions | builtin:synthetic.multiProtocol.step.executions |

#### Common request metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.multi\_protocol.request.availability | builtin:synthetic.multiProtocol.request.availability |
| dt.synthetic.multi\_protocol.request.executions | builtin:synthetic.multiProtocol.request.executions |

#### ICMP metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.multi\_protocol.icmp.success\_rate | builtin:synthetic.multiProtocol.icmp.successRate |
| dt.synthetic.multi\_protocol.icmp.packets\_sent | builtin:synthetic.multiProtocol.icmp.packetsSent |
| dt.synthetic.multi\_protocol.icmp.packets\_received | builtin:synthetic.multiProtocol.icmp.packetsReceived |
| dt.synthetic.multi\_protocol.icmp.round\_trip\_time | builtin:synthetic.multiProtocol.icmp.roundTripTime |
| dt.synthetic.multi\_protocol.icmp.request\_execution\_time | builtin:synthetic.multiProtocol.icmp.requestExecutionTime |

#### TCP metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.multi\_protocol.tcp.connection\_time | builtin:synthetic.multiProtocol.tcp.connectionTime |

#### DNS metrics

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.synthetic.multi\_protocol.dns.resolution\_time | builtin:synthetic.multiProtocol.dns.resolutionTime |

## Unsupported metrics

The following categories of Metrics Classic metrics are not supported on Grail:

* **A2TM** metrics, including all metrics with the prefix `builtin:a2tm`.
* **Lima** metrics, including all metrics with the prefix `builtin:lima`.
* **Classic Logs** metrics, including all metrics with the prefix `builtin:log`.
* **NAM** metrics, including all metrics with the prefix `builtin:nam`.
* **Span** metrics, including all metrics with the prefix `builtin:span`.
* **RUM Classic** metrics, including all metrics with the prefix `builtin:apps`. For details, see [RUM metrics migration](/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration "See how RUM Classic metrics map to their logical equivalents in Grail.").


---


## Source: dql-examples.md


---
title: DQL timeseries examples
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/dql-examples
scraped: 2026-02-17T21:16:18.388813
---

# DQL timeseries examples

# DQL timeseries examples

* Latest Dynatrace
* 8-min read
* Updated on Oct 17, 2025

Metrics on Grail enable you to pinpoint and retrieve any metric data with the help of [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). After reviewing the [fundamentals of DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide#metrics "Find out how DQL works and what are DQL key concepts.") and the [timeseries command](/docs/platform/grail/dynatrace-query-language/commands/metric-commands "DQL metric commands"), use the examples on this page to start getting answers from your metrics.

### Example 1: Average CPU usage across all hosts

In this example, you'll query the average CPU usage across all monitored hosts in your environment.

OneAgent collects CPU measurements from its host machine. These metrics are accessible through metric keys beginning with `dt.host.cpu`.

Observing the aggregate CPU usage across all hosts can help you visually confirm how your infrastructure responds to and recovers from usage spikes or slow, imperceptible growth trends over time.

```
timeseries usage=avg(dt.host.cpu.usage)
```

### Example 2: Average CPU usage by host, limit to top 3 hosts

In this example, you get every monitored host's average CPU usage and focus on the three hosts with the highest usage.

OneAgent collects CPU measurements from its host machine. These metrics are accessible through metric keys beginning with `dt.host.cpu`.

Charting individual hosts' CPU usage helps to visualize normal and outlier usage. By focusing on the three hosts with highest CPU usage, you can begin investigating under-provisioned applications. Likewise, focusing on hosts with the lowest CPU usage may reveal over-provisioning and lead to cost-saving opportunities.

1. Query the data.

   ```
   timeseries usage=avg(dt.host.cpu.usage), usage_summary=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



   | fieldsAdd entityName(dt.entity.host)



   | sort usage_summary desc



   | limit 3
   ```
2. Simplify results.

   A table can be easier to read than a line chart in some situations. Let's query data that works best with table output by focusing on the columns we most care about: `dt.entity.host` and `usage`.

   ```
   timeseries usage=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



   | fieldsAdd entityName(dt.entity.host)



   | sort usage desc



   | limit 3



   | fields dt.entity.host, dt.entity.host.name, usage
   ```

   This is essentially the same query as above, without the series.

### Example 3: Average CPU usage by host IP Address

In this example, you'll use an `in` condition to query hosts based on their IP address.

By using the `in` operator with `classicEntitySelector`, you can filter on `ipAddress` and other host attributes.

Using the timeseries `filter` parameter is more performant than chaining `timeseries` with the `filter` command.

```
timeseries usage=avg(dt.host.cpu.usage),



filter: {in(



dt.entity.host,



classicEntitySelector("type(host),ipAddress(\"10.102.39.126\")")



)}
```

### Example 4: Number of hosts sending CPU usage data

In this example, you'll learn how to chain `timeseries` with `summarize`. You'll first query hosts sending CPU usage data, and then count the number of hosts in the result.

Other DQL commands can also be chained with `timeseries` as demonstrated in previous examples, but unlike those examples, `summarize` further aggregates the dataset returned by `timeseries`. You'll find this two-step aggregation helpful as your questions become more complex and nuanced.

```
timeseries usage=avg(dt.host.cpu.usage), by:{dt.entity.host}



| summarize count()
```

### Example 5: Top hosts by bytes read with corresponding bytes written

In this example, you'll enrich a single result with context from another metric.

Even when focused on disk read operations, the corresponding disk writes can provide helpful context.

```
timeseries by:{dt.entity.host}, {



bytes_read=sum(dt.host.disk.bytes_read, scalar:true),



bytes_written=sum(dt.host.disk.bytes_written, scalar:true)



}



| sort bytes_read desc



| limit 3



| fields



dt.entity.host,



entityName(dt.entity.host),



bytes_read,



bytes_written
```

### Example 6: Available CPU by Kubernetes Node

In this example, you'll calculate the available CPU on all nodes of your hypothetical "openfeature" cluster.

To return a timeseries instead of a single value, we use the `[]` operator to take the difference of individual timeseries values. The result is another timeseries that you can visualize with a line chart.

The available CPU is integral for efficient resource utilization and avoiding resource contention. A timeseries visualized with a line chart is one way to show how the available CPU changes over time.

```
timeseries {



cpu_allocatable = min(dt.kubernetes.node.cpu_allocatable),



requests_cpu = max(dt.kubernetes.container.requests_cpu)



},



by:{dt.entity.kubernetes_cluster, dt.entity.kubernetes_node}



| fieldsAdd  // add friendly names



entityName(dt.entity.kubernetes_cluster),



entityName(dt.entity.kubernetes_node)



| fieldsAdd result = cpu_allocatable[] - requests_cpu[]



| fieldsRemove cpu_allocatable, requests_cpu
```

### Example 7: Average host CPU usage by host size

In this example, you'll learn how to use a [`entityAttr` command](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-attr "A list of DQL general functions.") to analyze host CPU usage by host size.

OneAgent collects local context from its host: information such as how many CPUs are installed and how much memory it has. You can add this information to your query with the `entityAttr` function.

Host-level information can sometimes be too fine-grained and difficult to interpret. In these situations, a well-chosen entity attribute can help you explore and analyze how individual hosts contribute to broader trends.

```
timeseries usage=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



| fieldsAdd cpuCores = entityAttr(dt.entity.host, "cpuCores")



| summarize by:{cpuCores}, avg(usage), count_hosts=count()
```

### Example 8: Query multiple CPU usage metrics with a single query

In this example, you'll learn how to use the [`append` command](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append "DQL correlation and join commands") to return multiple CPU metrics with a single query.

Combining queries into one command can be useful for comparing measurements from different contexts, as they will be charted together.

As you query many metrics from a single host and perform no arithmetic, the `append` command here is preferred to querying multiple metrics with a single `timeseries` command. The `append` command is a comparatively more flexible option, as it doesn't require equivalent `by` or `filter` arguments, for example. Additionally, chaining `append` is more efficient from a DQL perspective.

```
timeseries idle=avg(dt.host.cpu.idle),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



| append [



timeseries system=avg(dt.host.cpu.system),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



]



| append [



timeseries user=avg(dt.host.cpu.user),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



]
```

### Example 9: Connection failure rate by host

In this example, you'll apply what you've learned from previous examples to calculate the failure rate and find hosts running processes with many failed connections.

This example uses the `default` parameter to control for the case where there are no failures. It inserts a `0` value anywhere data is missing.

Failure rate calculations are common and critical for monitoring service-level objectives. Spotting persistent or recurring high failure rates in testing environments could indicate a deployment problem before the application reaches production.

```
timeseries {



new = sum(dt.process.network.sessions.new),



reset = sum(dt.process.network.sessions.reset, default:0),



timeout = sum(dt.process.network.sessions.timeout, default:0)



},



by:{dt.entity.host}



| fieldsAdd result = 100 * (reset[] + timeout[]) / new[]



| filter arrayAvg(result) > 0



| sort arrayAvg(result) desc
```

### Example 10: Monitoring host availability

In this example you will monitor the availability of hosts and count those that are currently up.

You can use the timeseries command with the [`nonempty` parameter](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#expand--nonempty-parameter--1 "DQL metric commands") to calculate host availability. This parameter ensures that you get a result even when no data match the filterâsuch as when no hosts are up. This provides a more accurate representation of host availability.

```
timeseries availability = sum(dt.host.availability, default:0),



nonempty:true,



filter:{availability.state == "up"}
```

### Example 11: Readiness probe

In this example you'll query [log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.") to count successful and failed readiness probes by host.

You can use the [`union` parameter](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#union "DQL metric commands") to capture all hosts, including those with no failures or no successes.

```
timeseries



failure_count=sum(log.readiness_probe.failure_count, default:0),



success_count=sum(log.readiness_probe.success_count, default:0),



by:{dt.entity.host},



union:true
```

The `union:true` argument captures all hosts, even if they had no failures or no successes.

### Example 12: Failure rate

In this example, you will query the per-second failure rate for a specific endpoint ("/api/accounts"). By using the [`rate` parameter](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#rate "DQL metric commands"), you can normalize the timeseries data to a specific duration.

Monitoring request failure rates is crucial for understanding application performance, identifying bottlenecks, and ensuring optimal user experience.

Dynatrace shows the per-minute request count by default, as Dynatrace service metrics collect one-minute granularity request data.

```
timeseries sum(dt.service.request.failure_count, rate:1s),



filter:{startsWith(endpoint.name, "/api/accounts")}
```

### Example 13: Capacity planning

In this example, you will query current host-disk availability and use the [`shift`](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#shift "DQL metric commands") parameter to compare it to usage 7 days ago.

Monitoring host-disk availability helps with capacity planning. If today's disk space usage is consistently higher than 7 days ago, it may signal the need for additional storage resources. Conversely, a decrease in usage might allow for resource optimization.

```
timeseries avail=avg(dt.host.disk.avail), by:{dt.entity.host}, from:-24h



| append [



timeseries avail.yesterday=avg(dt.host.disk.avail), by:{dt.entity.host}, shift:-168h



]



| filter startsWith(entityName(dt.entity.host), "prod-")
```

### Example 14: Verify host availability and redundance

In this example you'll use the [`count` aggregation](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries-count "DQL metric commands") to track the number of hosts monitored in each AZ of AWS region us-east-1.

Applications frequently deploy hosts across multiple availability zones (AZs) to ensure high availability. Counting hosts in each AZ helps verify that the distribution is balanced and, should one AZ experience network disruptions or other issues, the workload can fail over to another AZ.

```
timeseries num_hosts = count(dt.host.cpu.usage),



by:{aws.availability_zone},



filter:{startsWith(aws.availability_zone, "us-east-1")}
```

### Example 15: Performance optimization

In this example you'll use the [`percentile` aggregation](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries-percentile "DQL metric commands") to track the 90th percentile response time of the contrived /api/accounts endpoint.

Tracking the service response time [percentilesï»¿](https://www.dynatrace.com/news/blog/why-averages-suck-and-percentiles-are-great/) helps identify bottlenecks and areas for improvement. If a specific transaction consistently exceeds this threshold, you can decide if it warrants investigation and additional optimization.

```
timeseries p90 = percentile(dt.service.request.response_time, 90),



filter:{startsWith(endpoint.name, "/api/accounts")}
```

### Example 16: Right-sizing deployments

In this example you'll use the [`if` function](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions#if "A list of DQL conditional functions.") to label underused host-disk pairs.

Identifying overprovisioned deployments helps reduce operating costs. By removing overprovisioned infrastructure, you can determine the right size deployment for your application.

```
timeseries avail=avg(dt.host.disk.avail, scalar:true),



by:{dt.entity.disk, dt.entity.host},



filter:{startsWith(dt.entity.host, "my-app-")}



| fieldsAdd disk_usage=if(avail>450000000000, "underused", else: "optimal")



| limit 3
```

### Example 17: Split CPU usage by kubernetes annotations

In this example you'll split CPU usage by kubernetes annotation.

You can use kubernetes annotation `app.kubernetes.io/component` to evaluate the performance of your application components. Annotations are cloud application attributes and aren't typically ingested with a metric. You should split by the cloud application and look up the relevant annotation.

Many [`summarize` command functions](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") accept iterative expressions like `cpu_usage[]` to preserve the timeseries.

```
timeseries cpu_usage = sum(dt.kubernetes.container.cpu_usage, rollup:max),



by:{dt.entity.cloud_application}



| fieldsAdd annotations = entityAttr(dt.entity.cloud_application, "kubernetesAnnotations")



| fieldsAdd component = annotations[`app.kubernetes.io/component`]



| summarize cpu_usage = sum(cpu_usage[]),



by:{timeframe, interval, component}
```


---


## Source: histograms.md


---
title: Histogram metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/histograms
scraped: 2026-02-17T04:58:53.880551
---

# Histogram metrics

# Histogram metrics

* Latest Dynatrace
* Explanation
* 7-min read
* Published Jul 09, 2025

Histogram metrics are a powerful way to capture the distribution of values for a given measurement, such as response times, request sizes, or durations. Compared to a counter that measures the overall total in a single value, a histogram counts the number of occurrences at different thresholds (called buckets). It is a multi-value counter, aggregating data into buckets, allowing you to analyze percentiles, averages, and the overall shape of your data.

## Histogram metrics use cases

* Measure response time distributions for services or endpoints
* Track request or payload sizes
* Analyze latency or duration metrics in distributed systems

For a deeper dive into histograms and their advantages, see the following series of the OpenTelemetry blog posts:

* [Why histograms?ï»¿](https://opentelemetry.io/blog/2023/why-histograms/)
* [Histograms vs. summariesï»¿](https://opentelemetry.io/blog/2023/histograms-vs-summaries/)
* [Exponential histogramsï»¿](https://opentelemetry.io/blog/2023/exponential-histograms/)

## Ingest histogram metrics

No special configuration is needed to ingest histograms from OpenTelemetry (OTLP ingest API) or Prometheus sources (Dynatrace Operator). Histogram metrics are sent automatically when your environment receives OpenTelemetry or Kubernetes data.

The OpenTelemetry Exponential Histogram is not supported as a histogram: the histogram's `min|max|sum|count` are ingested but the buckets aren't.

If any of below happens, the OpenTelemetry ingest API returns the `400` or `200 with partial success` responses.

* Cumulative histograms aren't ingested (similarly to cumulative counters).
* Histogram data points without `sum` aren't ingested. This happens when negative values are recorded.
* Histogram buckets are not sorted.
* Histogram bucket boundary values of `NaN` or `Infinite` are invalid.

## Query percentiles using DQL

Dynatrace Query Language (DQL) allows you to analyze histogram metrics using the percentile aggregation. It calculates the requested percentile across all the buckets for each time slot.

For example:

```
timeseries percentile(http_request_duration_seconds_bucket, 99)
```

The query calculates the 99th percentile of values based on the ingested histogram buckets.

Histograms represent data as a series of buckets, each containing the count of values that fall within a specific range. For example, `http_request_duration_seconds_bucket` contains counts of request durations grouped by predefined ranges (`le` dimension).

The `percentile` function uses the bucket data to estimate the requested percentile (for example, the 99th percentile). It interpolates the value at which 99% of the observed data points fall below, based on the cumulative counts in the histogram buckets.

This query is particularly useful for analyzing latency or performance metrics, as percentiles provide insights into the worst-case scenarios experienced by users.

## Visualization examples and important warnings

You can visualize histogram metrics in Dynatrace Notebooks or Dashboards using DQL queries. However, be aware of the following limitations:

* Dynatrace currently visualizes histogram metrics **as percentiles with line charts over time** (using the `timeseries` command). Visualizing the distribution of occurrences across buckets for a given period of time (typically using a bar chart visualization) is **NOT** supported at this time.

For more information, see [Edit visualizations for Notebooks and Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

## Licensing and billing

The [timeseries percentile](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries_percentile "DQL metric commands") function, which is necessary to query histograms, is only available to DPS customers with the **Metrics powered by Grail** rate card. For more information, see [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").


---


## Source: metrics-security-context.md


---
title: Set up Grail permissions for Metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/metrics-security-context
scraped: 2026-02-17T05:08:00.015559
---

# Set up Grail permissions for Metrics

# Set up Grail permissions for Metrics

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as `department-A/department-AB/team-C`.

To use `dt.security_context` and other attributes for permissions, make sure these attributes are present in your telemetry data.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](/docs/ingest-from/opentelemetry/opentelemetry-security-context "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Set up the security context in OpenPipeline

You can define a security context based on existing resource attributes for your data within OpenPipeline. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Metrics** > **Pipelines** and after configuring your pipeline, on the **Permission** tab, use the **Set Security Context processors** option.

To define the `dt.security_context` attribute

1. Define a matching condition to filter metric records to assign the security context, such as:

   ```
   matchesValue(metric.key, "http.server.request.duration_bucket") and matchesValue(http.route, "/basket")
   ```
2. Add the `dt.security_context` for those metric records. The value of this attribute can be a literal value such as `TeamA`, or a value copied from another field present on the metric record.
3. Verify your security context is set correctly.

When new metric data arrives, the OpenPipeline security context processors add a `dt.security_context` attribute with the value `TeamA` to the matching metric records. To confirm that your security context processors handled the metric records, open ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and run a DQL query such as:

```
timeseries median(http.server.request.duration_bucket), by:{http.route, dt.security_context} | filter matchesValue(dt.security_context, "TeamA")
```

Based on the created attribute, you can enforce security-related user and group policies.

## Related topics

* [Set up Grail permissions for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Metadata enrichment of all telemetry originating from Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Set up Grail permissions for Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")


---


## Source: kubernetes-metric-migration.md


---
title: Kubernetes metrics migration guide
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/kubernetes-metric-migration
scraped: 2026-02-17T21:31:41.871469
---

# Kubernetes metrics migration guide

# Kubernetes metrics migration guide

* Latest Dynatrace
* 5-min read
* Updated on Jun 24, 2025

This guide provides insights into migrating Kubernetes metrics to Grail. Typically, a Grail metric is equivalent to a Metrics Classic metric. In some cases, however, there's no one-to-one relation:

* Convergent: a single Grail metric represents multiple Metrics Classic metrics of a similar scope or an increased level of detail.
* Replacement: a different Grail metric represents the Metrics Classic metric.
* Divergent/Calculated: the Classic metric is not represented 1:1 as Grail metric but can be calculated from other Grail metrics

## Identity

Classic Metrics and Grail Metrics have the same level of detail and dimensions available. The only difference is the metric key.

Metric key (Grail)

Metric key (Classic)

dt.kubernetes.cluster.readyz

builtin:kubernetes.cluster.readyz

dt.kubernetes.container.oom\_kills

builtin:kubernetes.container.oom\_kills

dt.kubernetes.container.restarts

builtin:kubernetes.container.restarts

dt.kubernetes.node.conditions

builtin:kubernetes.node.conditions

dt.kubernetes.node.cpu\_allocatable

builtin:kubernetes.node.cpu\_allocatable

dt.kubernetes.node.memory\_allocatable

builtin:kubernetes.node.memory\_allocatable

dt.kubernetes.node.pods\_allocatable

builtin:kubernetes.node.pods\_allocatable

dt.kubernetes.nodes

builtin:kubernetes.nodes

dt.kubernetes.persistentvolumeclaim.available

builtin:kubernetes.persistentvolumeclaim.available

dt.kubernetes.persistentvolumeclaim.capacity

builtin:kubernetes.persistentvolumeclaim.capacity

dt.kubernetes.persistentvolumeclaim.used

builtin:kubernetes.persistentvolumeclaim.used

dt.kubernetes.resourcequota.limits\_cpu

builtin:kubernetes.resourcequota.limits\_cpu

dt.kubernetes.resourcequota.limits\_cpu\_used

builtin:kubernetes.resourcequota.limits\_cpu\_used

dt.kubernetes.resourcequota.limits\_memory

builtin:kubernetes.resourcequota.limits\_memory

dt.kubernetes.resourcequota.limits\_memory\_used

builtin:kubernetes.resourcequota.limits\_memory\_used

dt.kubernetes.resourcequota.pods

builtin:kubernetes.resourcequota.pods

dt.kubernetes.resourcequota.pods\_used

builtin:kubernetes.resourcequota.pods\_used

dt.kubernetes.resourcequota.requests\_cpu

builtin:kubernetes.resourcequota.requests\_cpu

dt.kubernetes.resourcequota.requests\_cpu\_used

builtin:kubernetes.resourcequota.requests\_cpu\_used

dt.kubernetes.resourcequota.requests\_memory

builtin:kubernetes.resourcequota.requests\_memory

dt.kubernetes.resourcequota.requests\_memory\_used

builtin:kubernetes.resourcequota.requests\_memory\_used

dt.kubernetes.workload.conditions

builtin:kubernetes.workload.conditions

dt.kubernetes.workload.pods\_desired

builtin:kubernetes.workload.pods\_desired

dt.kubernetes.workloads

builtin:kubernetes.workloads

## Convergent metrics

The following metrics have been consolidated. The Grail metrics that supersede the Classic metrics offer an increased level of detail compared to the Classic metrics.

To achieve this decreased level of detail, the Grail metrics are first aggregated to the granularity of the Classic metric. From there the same set of filters can be applied and the output between Classic metrics and Grail metrics is identical.

The following list of metrics contains the pod and container count metrics and the Kubernetes event count metric that was available at a lower level of detail as Classic metric.

Kubernetes events and container/pod count metrics

Metric key (Grail)

Metric key (Classic)

dt.kubernetes.containers

builtin:kubernetes.containers

dt.kubernetes.pod.containers\_desired

builtin:kubernetes.workload.containers\_desired

dt.kubernetes.events

builtin:kubernetes.events

dt.kubernetes.pods

builtin:kubernetes.node.pods  
builtin:kubernetes.pods

The following table contains the workload and node resource metrics that have been available as separate workload- and node- level Classic metrics.
With Grail, there is a single metric at the container level.

**Example:** The following DQL query returns the amount of memory consumed on the workload level based on aggregated container-level data.

```
timeseries memory_working_set = sum(dt.kubernetes.container.memory_working_set)



by: {



k8s.cluster.name,



k8s.namespace.name,



k8s.workload.name



}
```

Workload- and node- level resource consumption metrics

Metric key (Grail)

Metric key (Classic)

dt.kubernetes.container.cpu\_usage

builtin:kubernetes.node.cpu\_usage  
builtin:kubernetes.workload.cpu\_usage

dt.kubernetes.container.cpu\_throttled

builtin:kubernetes.node.cpu\_throttled  
builtin:kubernetes.workload.cpu\_throttled

dt.kubernetes.container.requests\_cpu

builtin:kubernetes.node.requests\_cpu  
builtin:kubernetes.workload.requests\_cpu

dt.kubernetes.container.limits\_cpu

builtin:kubernetes.node.limits\_cpu  
builtin:kubernetes.workload.limits\_cpu

dt.kubernetes.container.memory\_working\_set

builtin:kubernetes.node.memory\_working\_set  
builtin:kubernetes.workload.memory\_working\_set

dt.kubernetes.container.requests\_memory

builtin:kubernetes.node.requests\_memory  
builtin:kubernetes.workload.requests\_memory

dt.kubernetes.container.limits\_memory

builtin:kubernetes.node.limits\_memory  
builtin:kubernetes.workload.limits\_memory

## Replaced metrics

This group of metrics consists of Classic metric keys that have never been made available as Grail metrics.
Instead the most similar Classic metric is used to then determine the Grail metric replacement for these deprecated metrics.
The reason for the deprecation is a cleanup of duplicate metric keys. In the case of the following metrics, a complete identity of the values between the Classic Metric and Grail Metric is not feasible, but they are closely related and do not deviate very much.

Metric key (Grail)

Metric key (Classic)

Superseding Classic Metric

dt.kubernetes.container.limits\_cpu

builtin:containers.cpu.limit

n.a.

dt.kubernetes.container.oom\_kills

builtin:kubernetes.container.outOfMemoryKills

builtin:kubernetes.container.oom\_kills

## Calculated metrics

The following set of Classic container metrics is superseded by Grail container metrics.
For most of the CPU metrics in this section the Classic metrics have the unit millicores, while the Grail metrics have the unit nanoseconds/minute. To get
to the same values, the Grail metric needs to be divided by the number of nanoseconds in a minute.
(The number of nanoseconds per minute is 60 \* 1000 \* 1000 \* 1000)

This is the case for the following Grail metrics.

builtin:containers.cpu.throttledMilliCores

```
timeseries {



throttled_time = avg(dt.containers.cpu.throttled_time, rollup: sum, rate: 1m)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



throttled_milli_cores = throttled_time[] * milli_core_per_core / ns_per_min



| summarize {



throttled_milli_cores = sum(throttled_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usageUserMilliCores

```
timeseries { usage_user_time = avg(dt.containers.cpu.usage_user_time)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



usage_user_milli_cores = usage_user_time[] * milli_core_per_core / ns_per_min



| summarize { usage_user_milli_cores = sum(usage_user_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usageSystemMilliCores

```
timeseries {



usage_system_time = avg(dt.containers.cpu.usage_system_time)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



usage_system_milli_cores = usage_system_time[] * milli_core_per_core / ns_per_min



| summarize {



usage_system_milli_cores = sum(usage_system_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usageMilliCores

```
timeseries {



usage_user_time = avg(dt.containers.cpu.usage_user_time)



, usage_system_time = avg(dt.containers.cpu.usage_system_time)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



usage_milli_cores = (usage_user_time[] + usage_system_time[] )



* milli_core_per_core / ns_per_min



| summarize {



usage_milli_cores = sum(usage_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usagePercent

```
timeseries {



// for total usage, user and system cpu usage are added



userCpuUsage = avg(dt.containers.cpu.usage_user_time)



, systemCpuUsage = avg(dt.containers.cpu.usage_system_time)



// cpu logical counts are the fallback, if the throttling ratio doesn't exist



, cpuLogicalCount = avg(dt.containers.cpu.logical_cores)



}



// filter statement ...



// leftOuter join allows the throttling ratio to be null



| join [



timeseries {



throttlingRatio = avg(dt.containers.cpu.throttling_ratio)



// same filter statement as above ...



}



], on: { interval, timeframe}, fields: { throttlingRatio}, kind:leftOuter



| fieldsAdd



// sum of system and user cpu usage



numerator = userCpuUsage[] + systemCpuUsage[]



// throttling ratio, or as a fallback cpu logical count.



, denominator = coalesce(throttlingRatio, cpuLogicalCount)



, nanoseconds_per_minute  = 60 * 1000 * 1000 * 1000



| fields



interval, timeframe



, cpuUsagePercent = 100.0 * numerator[] / ( denominator[] * nanoseconds_per_minute)
```

builtin:containers.cpu.usageTime

```
timeseries {



usageUserTime = avg(dt.containers.cpu.usage_user_time)



, usageSystemTime = avg(dt.containers.cpu.usage_system_time)



}



, by: { dt.entity.container_group_instance},



| fields



interval, timeframe



, usageTime = usageSystemTime[] + usageUserTime[]
```

builtin:containers.memory.limitPercent

```
timeseries {



limit_bytes = avg(dt.containers.memory.limit_bytes),



physical_total_bytes = avg(dt.containers.memory.physical_total_bytes)



}



| fieldsAdd



limit_percent = (limit_bytes[] / physical_total_bytes[] ) * 100



| summarize {



limit_percent = sum(limit_percent[] )



}, by: { timeframe, interval }
```

builtin:containers.memory.usagePercent

```
timeseries {



memoryLimits = avg(dt.containers.memory.limit_bytes)



, totalPhysicalMemory = avg(dt.containers.memory.physical_total_bytes)



, residentSetBytes = avg(dt.containers.memory.resident_set_bytes)



}



, by: { dt.entity.container_group_instance}



| fieldsAdd



denominator = if (



arrayFirst(memoryLimits) > 0,



then: memoryLimits,



else: totalPhysicalMemory



)



| fields



dt.entity.container_group_instance



, interval, timeframe



, memoryUsagePercent = 100 * residentSetBytes[] / denominator[]
```

## Related topics

* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")


---


## Source: rum-metric-migration.md


---
title: RUM metrics migration
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration
scraped: 2026-02-17T05:04:02.517331
---

# RUM metrics migration

# RUM metrics migration

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Jan 23, 2026

Looking for the New RUM Experience metrics documentation?

You can access the full list of available metrics and their details directly in the latest Dynatrace. Press **CTRL**/**CMD**+**K**, type `dt.frontend` and select **Show more**.

The [New RUM Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance."), which brings RUM to Grail, introduces numerous built-in metrics with the prefix `dt.frontend`. Because it uses a different data model than RUM Classic, there are no direct equivalents for [RUM Classic metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#applications "Explore the complete list of built-in Dynatrace metrics."), which use the prefix `builtin:apps`. However, many metrics have replacements that serve an analogous purpose, as shown in the table below. Note that metrics with the prefix `builtin:apps` that do not appear in the table have no replacement.

Differences in metric values between the `builtin:apps` metrics and their replacements are expected and result from underlying data model changes.

RUM Classic metric

Replacement in the New RUM Experience

builtin:apps.web.actionCount.\*

builtin:apps.other.uaCount.\*

dt.frontend.user\_action.count

builtin:apps.web.actionDuration.\*

builtin:apps.other.uaDuration.\*

dt.frontend.user\_action.duration

builtin:apps.other.crashCount.\*

builtin:apps.web.countOfErrors\*

builtin:apps.web.jsErrors\*

builtin:apps.other.requestErrorCount.\*

builtin:apps.web.countOfStandaloneErrors

builtin:apps.mobile.reportedErrorCount

dt.frontend.error.count

builtin:apps.other.requestErrorRate.\*

dt.frontend.error.count

dt.frontend.request.count

builtin:apps.web.cumulativeLayoutShift.load.\*

dt.frontend.web.page.cumulative\_layout\_shift

builtin:apps.web.domInteractive.load.\*

dt.frontend.web.navigation.dom\_interactive

builtin:apps.web.firstInputDelay.load.\*

dt.frontend.web.page.first\_input\_delay

builtin:apps.web.interactionToNextPaint

dt.frontend.web.page.interaction\_to\_next\_paint

builtin:apps.web.largestContentfulPaint.load.\*

dt.frontend.web.page.largest\_contentful\_paint

builtin:apps.web.loadEventEnd.\*

dt.frontend.web.navigation.load\_event\_end

builtin:apps.other.requestCount.\*

dt.frontend.request.count

builtin:apps.other.requestTimes.\*

dt.frontend.request.duration

builtin:apps.web.activeSessions

builtin:apps.mobile.sessionCount

builtin:apps.other.sessionCount.\*

dt.frontend.session.active.estimated\_count

builtin:apps.web.firstByte.load.\*

dt.frontend.web.navigation.time\_to\_first\_byte

builtin:apps.other.userCount.\*

builtin:apps.web.activeUsersEst

dt.frontend.user.active.estimated\_count

## Related topics

* [New Real User Monitoring Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance.")


---
