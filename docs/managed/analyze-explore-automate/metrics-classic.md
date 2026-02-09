---
title: "Metrics"
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic
updated: 2026-02-09
---

# Metrics

# Metrics

* Overview
* 2-min read
* Updated on Nov 09, 2023

In Dynatrace, you have various types of metrics at your disposal:

* Built-in metrics provided by OneAgent. These have the `builtin:` prefix in the metric key.

* Extension metrics provided by OneAgent or ActiveGate extensions. These have the `ext:` prefix in the metric key.

  The `ext:` prefix is used by metrics from [OneAgent extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") and [ActiveGate extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace."), and also by [classic metrics for AWS integration](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.").

  Despite the naming similarities, AWS integration metrics are **not** based on extensions.
* Calculated metrics you create. These have the `calc:` prefix in the metric key.
* USQL custom metrics you create: user session custom metrics (`uscm.` prefix) and user action custom metrics (`uacm.` prefix). These metrics are based on metadata extracted from user session and user action data.
* Custom metrics you can feed to Dynatrace via metric ingestion. These don't have any fixed prefix, as the [ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.") is completely flexible.

Metrics frequency

* Infrastructure metrics and other periodic metrics are captured every 10 seconds and stored as 1-minute aggregates. Typically, this includes a min/max/count/sum/average of the measured metric.
* Service and web request metrics do not have a frequency. Dynatrace captures the transactions and displays medians and 90th percentiles. RUM and service analysis pages are based on this data.
* For custom metrics ingestion, the standard resolution is 1 minute, but you can also get [statistic summaries](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

[### Ingestion

Push custom data to Dynatrace.](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")[### Built-in metrics

Get an overview of metrics available out of the box.](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.")[### Self-monitoring metrics

Get an overview of self-monitoring metrics available out of the box.](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics "Explore the complete list of self-monitoring Dynatrace metrics.")[### Metric browser

Get an overview of all metrics available in your environment.](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.")

### Calculated metrics

[Log Monitoring](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")

[Service](/managed/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")

[Synthetic](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#calculated-metrics "Learn how to analyze browser-monitor data points.")

[RUM - web applications](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")

[RUM - mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.")

[RUM - custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")

### USQL custom metrics

[RUM - web applications](/managed/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications.")

[RUM - mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for mobile applications.")

[RUM - custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for custom applications.")

### Metric sources

[Metric open ingest](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")

[OpenTelemetry metrics](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")

[AWS service metrics](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.")

[Azure service metrics](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.")

[Metrics for Dynatrace Runtime Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics/app-sec-metrics "View available Application Security metrics for Dynatrace Runtime Vulnerability Analytics.")

[Log metrics (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")

### See also

[Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")

[Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")

[Calculated metrics API](/managed/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

[Metric events for alerting](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
