---
title: Clouds app
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app
scraped: 2026-02-20T21:08:59.158348
---

# Clouds app

# Clouds app

* Latest Dynatrace
* App
* 4-min read
* Updated on Jan 21, 2026

The new [cloud experienceï»¿](https://www.dynatrace.com/platform/cloud-monitoring/) is optimized for Cloud (Platform) Operation teams and Site Reliability Engineers (SREs) and focuses on health, troubleshooting, and performance optimization use cases of (multi-)cloud environments.

The centerpiece of this experience is ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

* Onboard your cloud accounts and start to analyze your full cloud inventory within minutes.
* Analyze metrics, events, logs, traces, metadata and topology from virtual machines, serverless functions, databases, queues, storage, networking, and many moreâin one view.
* Use health alerts to ensure optimal health and performance. Reduce troubleshooting and remediation time with AI-powered alerting.
* Leverage your (existing) cloud tags to route notifications, define ownership, or allocate costs.
* Take advantage of ready-made dashboards to save time and get instant insights.

The underlying observability data is all powered by [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), which supports flexible analytics through the [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, and ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

![Get a comprehensive view of your multi-cloud environments and see your full cloud inventory](https://cdn.hub.central.dynatrace.com/hub/console/drafts/170/media/clouds-app-overview-aws-and-azure.png)![Details of problems associated with selected cloud resources are easy to analyze](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/8822a738-a2bf-4d75-bdfa-beabbb150a0e.png)![See full configuration details of cloud services](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/b96f7374-5a8e-4c7a-b256-d79f469803a4.png)![Get started immediately with ready-made dashboards. Customize them according to your needs.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/170/media/08-ready-made-dashboard-aws-lambda.png)![Use ready-made health alerts and warning signals and custom alert templates to assess health of your cloud services.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/d7350ea9-6129-4818-8798-27514232ca8f.png)![Easily and seamlessly set up a new AWS connection. New Cloud Connections simplifies the onboarding experience for customers.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/170/media/06-clouds-app-new-aws-connection_2.png)![You can still use Explorer Classic for classic cloud connections](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/f743e7e6-ec1d-488c-b0ae-5d5a3a8c98e5.png)

1 of 7Get a comprehensive view of your multi-cloud environments and see your full cloud inventory

## Prerequisites

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** is automatically installed as a core app managed by Dynatrace.

### Connections

New cloud connections (AWS, Azure)

Classic cloud connections (AWS, Azure, GCP)

* Dynatrace SaaS environment powered by Grail and AppEngine hosted in any AWS region or an eligible Azure region
* [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") is required with the following capabilities:

  + [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")
  + [Logs powered by Grail](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")
  + [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

* Dynatrace SaaS environment powered by Grail and AppEngine
* Available for [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") and [classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

See [concepts](#concepts) for the comparison between classic and new cloud connections.

### Permissions

The following table describes the required permissions.

Permission

Description

settings:objects:read

Read settings of ownership (settings:schemaIds = builtin:ownership.config) - required by Ownership tab in details panel.

unified-analysis:screen-definition:read

Read details screen config. Necessary for displaying details panel.

davis:analyzers:execute

Execute Davis analyzers. Necessary for presenting problems details in Problems tab in details panel.

hub:catalog:read

Read Hub catalog.

app-settings:objects:read

Read app settings objects. Required for onboarding logs in context.

app-settings:objects:write

Write app settings objects.

slo:slos:read

Read for SLOs tab.

state:user-app-states:read

Read user app state. Necessary for presenting events in Events tab in details panel.

state:user-app-states:write

Storing per-user app state.

document:documents:read

Read documents. Required by filter presets feature. Required for ready-made dashboards (Overview).

10

rows per page

Page

1

of 1

## Get started

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** has an integrated onboarding flow that guides you through all the required steps to get started. The exact steps you need to take depend on your cloud provider and the type of cloud connection (new or classic).

If you're new to Dynatrace AWS Cloud Platform Monitoring, we recommend starting with the new AWS connections instead of the classic ones.

New cloud connections (AWS, Preview for Azure)

Classic cloud connections (AWS, Azure, GCP)

New cloud connections (AWS, Preview for Azure)

Classic cloud connections (AWS, Azure, GCP)

Use the following guide to set up and configure a new AWS cloud connection in Dynatrace.

[01Create a new AWS connection

* How-to guide
* Learn how to create a new AWS connection in the Clouds app.](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app/create-aws-connection)

In ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**, use the app header bar and select  **Create connection** > **AWS (Classic connections)** or  **Create connection** > **Azure (Classic connections)** or  **Create connection** > **GCP (Classic connections)**.

All data originating from classic connections can be analyzed in the **Explorer (Classic connections)** tab.

### Overview (New connections)

The **Overview New** tab is the landing page, where you can start discovering ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**, get data into Dynatrace, and see a summary of the health state of your AWS and/or Azure services based on new cloud connections at a glance. On that page, you can:

* Select the **AWS services** or **Azure services** tile, choose a specific service category, or select the counter in the upper-right corner of the tile to access the **Explorer New** tab with a list of selected services.
* Review the health state of cloud services, depending on your alert setup. To list the unhealthy services in **Explorer New**, select the red counter (if any) in the upper-right corner of the tile.
* Open ready-made dashboards for the most popular services (for example, AWS Lambda) or select **Browse all dashboards** to list all ready-made dashboards for AWS and/or Azure.

  ![Clouds app | Overview](https://dt-cdn.net/images/clouds-app-overview-3840-c1c071fe6a.png)

### Explorer (New connections)



Use the **Explorer New** tab to analyze your AWS cloud services and environments. You can explore, filter, and analyze data using various features in ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

* In the sidebar on the left, you can select a specific service category (such as  **Containers** or  **Functions**) or analyze all services. In addition, you can quickly filter by predefined attributes that are relevant for the selected category. Select any attribute in the facets sidebar and select **Update** to get results. The filter field is updated with your selection.
* Alternatively, select the filter field at the top to view suggestions and enter filtering options. Add more statements to narrow down the results. Criteria of the same type are grouped by `OR` logic. Criteria of different types are grouped by `AND` logic. You can filter services using tags, alert status, and attributes like name or region. This helps you focus on specific subsets of services based on your criteria.

  For more details on the filter field syntax, see [Filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").
* You can explore data in the table using the available perspectives:

  + **Health**
  + **Utilization** (for compute services)
  + **Metadata**
  + To tailor the results details that you see in the table, select **Column settings** and select the columns you want to display.

  ![Clouds app | Explorer - filtering - utilization](https://dt-cdn.net/images/clouds-app-explorer-filtering-utilization-3840-2ec09e9078.png)
* Select a specific cloud service in the table to analyze all data in context: metrics, logs, events, metadata, configuration, and topology.

  Select ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Go to dashboard** to navigate to the respective ready-made dashboard while maintaining the selected timeframe and filters.

  ![Clouds app | Explorer - details view](https://dt-cdn.net/images/clouds-app-explorer-details-view-3840-1790feeb80.png)

### Alerting (New connections)

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** provides ready-made health alerts and warning signals for your cloud services, as well as alert templates for setting up additional custom alerts for popular AWS services.

#### Health alerts and warning signals

Health alerts and warning signals are provided and maintained out of the box by Dynatrace.

* A health alert creates a Dynatrace problem that triggers root-cause analysis in Dynatrace.
* A warning is created for a resource when the observation is not critical and shouldn't raise a problem.

  Health alerts and warning signals are both surfaced in ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

You can easily adopt ready-made health alerts and warning signals for your AWS accounts either upon your [AWS connection onboarding](/docs/ingest-from/amazon-web-services/create-an-aws-connection/aws-connection-app-settings "Onboard your AWS environments and create AWS connections via the Settings app.") or in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

If you want to create new or update ready-made health alerts and warning signals, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Alerts** > **Cloud services**, where you can create, update, and enable/disable alerts for your connections.

* Alert scope

  + **Actor** (service user): Provide a Dynatrace service user on whose behalf the alert evaluation (and thus queries) are executed. The service user requires at least the following permissions:

    - `storage:metrics:read`
    - `storage:buckets:read`
    - `davis:analyzers:execute`
  + **Alert scope** (region): Allows you to filter alert evaluations only for specific regions. For example, filter for `us-east-1` to get alerts and warnings only for cloud services hosted in that region.
  + Alert conditions
  + Depending on the detection model of the configured alert, you can customize different parameters such as threshold and number of signal fluctuations.

![Settings | Ready-made alerts](https://dt-cdn.net/images/settings-ready-made-alerts-3840-d19f21a2a8.png)![Settings | Health alert details](https://dt-cdn.net/images/settings-health-alert-details-3840-f4fc0982c7.png)

1 of 2

#### Alert templates

Dynatrace provides predefined alert templates to allow for additional custom alerts on popular cloud services. These alert templates are complementary to ready-made health alerts and warning signals.

You can easily create new [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") directly in ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** by selecting a template and  **New Alert**.

Next, you can either customize the alert in the Anomaly Detection wizard or create the alert with one click.

![Clouds app | Custom alert templates](https://dt-cdn.net/images/clouds-app-custom-alerts-template-3840-e1a42bda6c.png)

You can find all custom alerts and more information around capabilities and limits in [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

### Explorer (Classic connections)

The **Explorer (Classic connections)** tab surfaces data coming from classic cloud connections and allows for the analysis of cloud services across AWS, Azure, and GCP.

If you've already used Dynatrace for cloud platform monitoring, the classic connections and **Explorer (Classic connections)** continue to provide the same value.

![Clouds app | Explorer (Classic connections)](https://dt-cdn.net/images/clouds-app-explorer-classic-connections-3840-a96bf1622d.png)

## Concepts

### New cloud connections vs classic cloud connections

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** provides a comprehensive view of your (multi-)cloud environments, enabling you to optimize the health, performance, and resource utilization of your cloud services.

Currently, ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** supports two types of cloud connections:

New cloud connections (AWS, Preview for Azure)

The newest cloud platform connections by Dynatrace provide an easier, more flexible, and more powerful way to connect AWS and Azure cloud accounts with Dynatrace. Support for GCP will follow soon.

All data is natively stored in Grail and surfaced on the **Overview New** and **Explorer New** tabs within ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

Classic connections

The classic cloud connections are available for AWS, Azure, and GCP within the previous (**AWS Classic**, **Azure Classic**, **GCP Classic**) and latest Dynatrace.

Classic connections are surfaced on the **Explorer (Classic connection)** tab in ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** and have no specific licensing requirements.

The **Explorer** New and **Overview** New tabs only operate upon data originating from new AWS cloud connections.

Azure and GCP will follow in the future.

### Perspectives: Health, Utilization, and Metadata (New connections)

Each perspective on monitoring your cloud services can be tailored to your needs by showing or hiding columns in the table.

* **Health**âprovides health-related information
* **Utilization** (available for compute services)âprovides perspective focuses on operational efficiency
* **Metadata**âsurfaces additional information, such as cloud tags

#### Health and custom alerts

In the **Health** perspective, you can see each cloud service's health and custom alerts. When you hover over a health or custom alert badge, you see the problems and further analysis options.

* Select  **View event** to directly navigate to the details, such as relevant metrics for the respective problem.
* Select  **Investigate problem** to enter **Problem mode**.

**Problem mode** enables precise investigation and analysis of any health-related issues.

* This mode highlights the most relevant metrics associated with the alert and narrows down the timeframe to the start and end times of the selected problem.
* Additionally, it offers quick access to the underlying problem, allowing you to efficiently diagnose and resolve issues.
* You can use [Davis Intelligence](/docs/dynatrace-intelligence/copilot "Learn about Dynatrace Intelligence generative AI.") to get additional insights about the problem and potential remediation steps.

**Problem mode** is always active when you navigate from a specific problem in [![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") to ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** operates in **Problem mode** whenever a problem is highlighted next to the filter bar at the top of the app.

### Ready-made dashboards (New connections)



You have access to the following ready-made dashboards for the new AWS Cloud Platform Monitoring:

* AWS Overview
* AWS API (API Gateway and REST APIs)
* AWS Bedrock
* AWS Dynamo DB
* AWS EC2 (EC2, EBS, AutoScaling)
* AWS ECS (including ECS Container Insights)
* AWS Edge Networking (Route 53, CloudFront)
* AWS EFS
* AWS ElastiCache (Redis, Memcached)
* AWS ELB (Application, Classic, Network Load Balancing)
* AWS EventBridge
* AWS Foundation Networking (NAT Gateway, PrivateLink)
* AWS Health Events
* AWS Lambda
* AWS MSK (Kafka)
* AWS RDS (including Aurora)
* AWS S3
* AWS SNS
* AWS SQS

The ready-made dashboards can be accessed through:

* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

  Open ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select [Ready-made dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-dashboards "Use ready-made dashboards to visualize your data right out of the box.") in the left menu, and search for `aws`.
* ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**

  + Open ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** and select the **Overview New** tab. You can then either select one of the more popular dashboards directly (for example, AWS Lambda) or select **Browse all dashboards**.
  + ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** allows you to navigate from a specific service to the respective dashboard in context ( ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Go to dashboard**). The selected timeframe, segment, and applied filters will be carried over from ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** to the dashboard.

![Clouds app | Dashboard navigation](https://dt-cdn.net/images/clouds-app-dashboard-navigation-3840-d0998aa51b.png)

### Segments (New connections)

[Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") allow you to logically structure and conveniently filter observability data across apps on the Dynatrace platform. Segments are available within the new **Explorer New** tab and can be defined easily for new cloud connections, since all data (including [Smartscape nodes](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.")) is stored in Grail.

For a step-by-step guide on how to define segments for Smartscape nodes, see [Filter Smartscape nodes with segments](/docs/manage/segments/getting-started/segments-getting-started-filter-smartscape-nodes "Learn how to filter Smartscape nodes by using segments in Dashboards."). You can use any primary Grail field (and, in the future, also tags) to conveniently define simple segments across **All data**:

* [Primary Grail fields](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.") (for example, `aws.account.id`, `aws.region`)
* Primary Grail tags (future)

Example segment definition by AWS Account ID:

![Segment - AWS account](https://dt-cdn.net/images/simple-segment-aws-account-3840-1b8915174b.png)

In ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** (or any other app that supports segments), you can then choose the segment `AWS account` and select one or more `awsAccountIDs` for filtering.

## Use cases

* Understand your (multi-)cloud architectures and dependencies
* Assess health of your cloud services
* Troubleshoot problems in ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**
* Analyze performance and resource utilization

## FAQ

### What if I already have existing cloud connections?

The existing, classic cloud connections stay as they are and are not automatically upgraded or removed.

To benefit from the new AWS Cloud Platform Monitoring, you need to create a new cloud connection for your AWS accounts.

The same AWS Account for the classic and new cloud connections

We do not recommend setting up the classic and new cloud connections for the same AWS account. For a heterogeneous set of AWS accounts, classic and new cloud connections can co-exist.

### How can I join the Azure Preview?

You can find more information and join the Cloud Platform Monitoring for Azure Preview through our [Preview program page](/docs/whats-new/preview-releases#new-cloud-platform-monitoring-for-azure "Learn about our Preview releases and how you can participate in them.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Onboard your new multicloud environments and monitor their resources.](https://www.dynatrace.com/hub/detail/clouds/?internal_source=doc&internal_medium=link&internal_campaign=cross)