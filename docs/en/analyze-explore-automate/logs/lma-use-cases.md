---
title: Log Management and Analytics use cases
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases
scraped: 2026-03-06T21:15:16.527467
---

# Log Management and Analytics use cases

# Log Management and Analytics use cases

* Latest Dynatrace
* Overview
* 2-min read
* Updated on Jan 28, 2026

The following use cases show just some of the ways you can use Log Management and Analytics to leverage your log data.

### Observe cloud network traffic with logs

In this use case, you need to use VPC Flow logs to monitor and analyze incoming HTTP(S) traffic to your Virtual Private Cloud (VPC) in Amazon Web Services (AWS).

* [Observe cloud network traffic with logs](lma-use-cases/lma-e2e-observability.md "Observability using logs, metrics and dashboards.")

### Use logs in context to troubleshoot issues

In this use case, you need to do proactive health and performance check of the apps running on maintained cluster and learns about errors in logs that are caused by another component.

* [Use logs in context to troubleshoot Kubernetes (K8s) issues](lma-use-cases/lma-e2e-troubleshooting.md "Faster troubleshooting with logs, metrics and traces on Kubernetes.")

### Investigate security incidents in Kubernetes clusters Threat hunting

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze unauthorized requests in your Kubernetes audit logs. See how you can manage and reuse the evidence gathered during the investigation, navigate between executed queries while maintaining investigation in context, and get a detailed overview of your results in the original format.

* [Threat hunting and forensics](../../secure/use-cases/threat-hunting.md "Use case scenario for threat hunting and forensics with Investigations.")

### Analyze AWS CloudTrail logs

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze CloudTrail event data, monitor and identify your AWS account activity against security threats and potential deviations from normal activities.

* [Analyze AWS CloudTrail logs with Investigations](../../secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator.md "Analyze CloudTrail logs and find potential security issues with Dynatrace.")

### Analyze Amazon API Gateway access logs

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to monitor and identify errors in your Amazon API Gateway access logs.

* [Analyze Amazon API Gateway access logs with Investigations](../../secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator.md "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")

### Detect threats against your AWS Secrets

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to monitor and identify potential threats against your AWS Secrets by analyzing CloudTrail logs.

* [Detect threats against your AWS Secrets with Investigations](../../secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator.md "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")

### Resolve team dependencies

In this use case, you create a Log Analysis Dashboard that takes care of identifying bugs from logs, as well as grouping, triaging, and distributing to a bug tracker that clarifies ambiguous responsibilities and interdependencies.

* [Automated bug triaging and ticketing](lma-use-cases/lma-e2e-resolve-dependencies.md "Explore a Log Management and Analytics use case for resolving team dependencies.")

### Real-time advanced observability with logs and DQL

In this use case, you want to observe mission-critical information over time found in your logs that are sent using log ingest API.

* [Observe your logs in real time](lma-use-cases/lma-e2e-real-time-observability-logs-dql.md "Explore the Log Management and Analytics use case for real-time observability with logs.")

### Control log query costs using Retention with Included Queries

In this use case, you use the DPS capability **Retain with Included Queries** to control and predict log consumption.

* [Take control of log query costs using Retain with Included Queries](lma-use-cases/lma-e2e-included-log-queries.md "How to use the Retain with Included Queries capability to control and predict log consumption.")

### Set up custom alerts based on events extracted from logs

Using Davis events based on logs you will get immediate alerts once the log record you define is ingested.

* [Set up alerts based on events extracted from logs](lma-use-cases/lma-alert-log-based-events.md "How to create and configure Davis problems and alerts with events based on logs.")

### Set up custom alerts based on metrics extracted from logs

Using a combination of metrics based on logs and [custom alerts](../../dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app."), you can use the power of different Dynatrace Intelligence data analyzers to address use cases from simple threshold-based alerting to seasonal baselines.

* [Set up custom alerts based on metrics extracted from logs](lma-use-cases/lma-alert-log-based-metrics.md "How to create and configure Davis problems and custom alerts with metrics based on logs.")

## Related topics

* [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.")