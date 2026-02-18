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

OneAgent версия 1.283+

Мы изменили доступность технологических метрик в Grail, что может повлиять на прямую связь между Metrics Classic и метрическими ключами Grail. Выберите, чтобы узнать больше об изменении.

### Apache

| Метрический ключ (Grail) | Метрический ключ (Classic) |
| --- | --- |
| dt.runtime.apache.connections.socket\_waiting\_time | builtin:tech.webserver.connections.socketWaitingTime |
| dt.runtime.apache.requests | builtin:tech.webserver.requests |
| dt.runtime.apache.threads.active | builtin:tech.webserver.threads.active |
| dt.runtime.apache.threads.idle | builtin:tech.webserver.threads.idle |
| dt.runtime.apache.threads.max | builtin:tech.webserver.threads.max |
| dt.runtime.apache.traffic | builtin:tech.webserver.traffic |

### Go

| Метрический ключ (Grail) | Метрический ключ (Classic) |
| --- | --- |
| dt.runtime.go.cf.auctioneer\_fetch\_states\_duration | builtin:cloud.cloudfoundry.auctioneer.fetchDuration (фильтруется по типу процесса Go) |
| dt.runtime.go.cf.auctioneer\_lrp\_auctions | builtin:cloud.cloudfoundry.auctioneer.lprFailed (фильтруется по типу процесса Go)   builtin:cloud.cloudfoundry.auctioneer.lprStarted (фильтруется по типу процесса Go) |
| dt.runtime.go.cf.auctioneer\_task\_auctions\_failed | builtin:cloud.cloudfoundry.auctioneer.taskFailed (фильтруется по типу процесса Go) |
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

| Метрический ключ (Grail) | Метрический ключ (Classic) |
| --- | --- |
| dt.runtime.iis.connections.socket\_waiting\_time | builtin:tech.webserver.connections.socketWaitingTime |
| dt.runtime.iis.requests | builtin:tech.webserver.requests |
| dt.runtime.iis.threads.active | builtin:tech.webserver.threads.active |
| dt.runtime.iis.threads.idle | builtin:tech.webserver.threads.idle |
| dt.runtime.iis.threads.idle | builtin:tech.webserver.threads.max |
| dt.runtime.iis.traffic | builtin:tech.webserver.traffic |

### Java

| Метрический ключ (Grail) | Метрический ключ (Classic) |
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

| Метрический ключ (Grail) | Метрический ключ (Classic) |
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

| Метрический ключ (Grail) | Метрический ключ (Classic) |
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

| Метрический ключ (Grail) | Метрический ключ (Classic) |
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