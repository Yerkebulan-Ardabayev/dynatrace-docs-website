---
title: Service monitoring settings
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-settings
---

# Service monitoring settings

# Service monitoring settings

* Reference
* 2-min read
* Updated on Feb 17, 2026

You can modify service settings both globally—across all services in your environment—or for individual services.

Environment

To define service settings globally, go to **Settings** > **Server-side service monitoring**.

Service

To define service settings for an individual service

1. Go to **Services**.
2. Select the service you want to configure.
3. On the service overview page, select **More** (**…**) > **Settings**.

APIs are available for the majority of the settings.

Rules and settings on the service level override the ones defined globally.

| Setting | Global (web UI) | API | Service-level (web UI) |
| --- | --- | --- | --- |
| [Failure detection](/managed/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.") | Applicable | Applicable | Applicable |
| [Key requests](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.") | Applicable | Applicable | Applicable |
| [Mute requests](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers.") | Applicable | Applicable | Applicable |
| [Anomaly detection](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services "Learn how to adapt the sensitivity of problem detection for services.") | Applicable | Applicable | Applicable |
| [Custom service detection rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.") | Applicable | Applicable | Not applicable |
| [Custom service naming rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming "Use naming rules to customize and enhance the automated naming of your services.") | Applicable | Applicable | Not applicable |
| [Custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.") | Applicable | Applicable | Not applicable |
| [Messaging services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Set up custom messaging services to trace message queues.") | Applicable | Applicable | Not applicable |
| [Merged services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Consolidate multiple web-request services of the same process group into one service.") Deprecated [1](#fn-1-1-def) | Applicable | Not applicable | Not applicable |
| [Unified services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Define services on observability signals ingested via Trace ingest APIs.") | Applicable | Applicable | Applicable |
| [Request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") | Applicable | Applicable | Not applicable |
| [Custom API definitions](/managed/observe/application-observability/services/customize-api-definitions "Set detection rules to customize APIs in your environment.") | Applicable | Applicable | Not applicable |
| [Calculated service metric](/managed/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.") | Applicable | Applicable | Not applicable |
| [Request-naming rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") | Not applicable | Applicable | Applicable |
| [Third-party service monitoring](/managed/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Configure how Dynatrace should monitor third-party services.") | Not applicable | Applicable | Applicable |

1

You can create the equivalent of a merged service via [Custom service detection rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services."). Existing merged services can be viewed and edited via the Dynatrace web UI.