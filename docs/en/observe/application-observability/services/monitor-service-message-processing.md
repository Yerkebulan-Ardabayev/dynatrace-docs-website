---
title: Monitor service message processing
source: https://www.dynatrace.com/docs/observe/application-observability/services/monitor-service-message-processing
scraped: 2026-02-27T21:21:30.089994
---

# Monitor service message processing

# Monitor service message processing

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Jan 15, 2026

Modern distributed systems rely heavily on asynchronous communication through message queues and streaming platforms. Understanding message flow, throughput, and processing failures is critical for maintaining system reliability.

Monitoring service message processing in Dynatrace addresses this need by providing comprehensive visibility into message-based transactions across your microservices architecture, helping you track throughput, identify bottlenecks, and resolve processing issues.

## What is service message processing monitoring?

In Dynatrace, message processing refers to any transaction involving message queues or streaming platforms like Kafka, RabbitMQ, ActiveMQ, and AWS SQS. This includes messages published to topics, received from queues, and processed by consuming services.

Service message processing monitoring helps you understand how messages flow through your distributed systems, detect processing bottlenecks, and identify failures in asynchronous communication patterns.

You can access service message processing directly from ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, or through custom dashboards and alerts configured to monitor messaging metrics.

This feature is designed for SREs, developers, and platform engineers who need visibility into asynchronous communication patterns and message processing health.

Service message processing monitoring provides:

* Real-time visibility into message publish, receive, and process rates
* Identification of processing bottlenecks and queue lag
* Tracking of message flow between producing and consuming services
* Error rate monitoring for failed message processing
* Infrastructure dependency mapping for messaging platforms
* Integration with distributed traces for root cause analysis

## Metrics reference

Dynatrace provides four core metrics for monitoring message processing:

| Metric | Description | Unit |
| --- | --- | --- |
| `dt.service.messaging.publish.count` | Messages sent to queues/topics | count |
| `dt.service.messaging.receive.count` | Messages received from queues/topics | count |
| `dt.service.messaging.process.count` | Messages successfully processed | count |
| `dt.service.messaging.process.failure_count` | Messages that failed processing | count |

### Key dimensions

| Dimension | Description | Example values |
| --- | --- | --- |
| `messaging.destination.name` | Queue or topic name | `authorQueue`, `orderEvents` |
| `dt.entity.service` | Service identifier | `spring-kafka-producer` |
| `messaging.system` | Messaging platform | `kafka`, `rabbitmq`, `aws_sqs` |
| `aws.account.id` | AWS account identifier | `123456789012` |
| `aws.region` | AWS region | `us-east-1` |
| `k8s.cluster.name` | Kubernetes cluster name | `prod-cluster` |
| `k8s.namespace.name` | Kubernetes namespace | `payment-services` |

## Get started

To begin monitoring service message processing

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, select the **Explorer** tab, and select **Message processing**.
2. Select the service and queue/topic you want to monitor.
3. View **Publish rate**, **Receive rate**, and **Process rate** in the time series charts.
4. Identify lag by comparing receive rates to process rates.
5. Drill down to distributed traces to investigate specific message failures.

## Query examples

Monitor service messaging throughput:

```
timeseries throughput = sum(dt.service.messaging.process.count),



by: {dt.smartscape.service}



| lookup [smartscapeNodes "SERVICE" | fields name,id],



sourceField:dt.smartscape.service, lookupField:id



| fieldsAdd `Service` = lookup.name, dt.smartscape.service



| summarize throughput = sum(throughput[]),



by: { timeframe, interval, `Service`, dt.smartscape.service }
```

Calculate service messaging failure rate:

```
timeseries { throughput = sum(dt.service.messaging.process.count),



failure_count = sum(dt.service.messaging.process.failure_count) },



by: {dt.smartscape.service}, nonempty:true, union:true



| lookup [ smartscapeNodes "SERVICE" | fields name, id],



sourceField:dt.smartscape.service, lookupField:id



| fieldsAdd `Service` = lookup.name, dt.smartscape.service



| summarize failure_rate = sum((failure_count[] / throughput[]) * 100),



by: { timeframe, interval, `Service`, dt.smartscape.service }
```