---
title: Stream logs to Dynatrace with Fluentd on Kubernetes
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s
scraped: 2026-02-28T21:14:28.871446
---

# Stream logs to Dynatrace with Fluentd on Kubernetes

# Stream logs to Dynatrace with Fluentd on Kubernetes

* Latest Dynatrace
* Explanation
* 1-min read
* Published Dec 02, 2021

[Dynatrace Log Management and Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") uses OneAgent DaemonSet, which includes a log module. This is the recommended way of streaming logs from nodes and pods to Dynatrace.

Alternatively, you can use the [Dynatrace Fluentd pluginï»¿](https://dt-url.net/gb23475), which is an open-source module, to stream logs.

The architecture is illustrated below.

![fluentd](https://dt-cdn.net/images/image-2022-03-04-09-25-59-449-925-faa9522baf.png)

## Capabilities

* Supports streaming logs to different Dynatrace environments from the same Kubernetes cluster. For example, you can send application pod logs to a different environment than the Kubernetes node logs.
* Supports streaming logs for [application-only integrations](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").
* Can be configured to stream logs directly to Dynatrace.

## Limitations

Logs coming from Fluentd aren't linked with the Kubernetes workloads. Consequently, you can't search for logs by Kubernetes workload on the **Log viewer** page in Dynatrace. However, you can still see logs on the corresponding **Kubernetes workloads** pages.

## Deploy integration

For instructions on how to deploy Fluentd integration, see the [documentation on GitHubï»¿](https://github.com/dynatrace-oss/fluent-plugin-dynatrace/tree/main/example).

## Related topics

* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")