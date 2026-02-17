# Dynatrace Documentation: observe/infrastructure-observability

Generated: 2026-02-17

Files combined: 86

---


## Source: aws-monitoring.md


---
title: Amazon Web Services monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring
scraped: 2026-02-06T16:29:00.184458
---

# Amazon Web Services monitoring

# Amazon Web Services monitoring

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 28, 2026

Dynatrace automatically discovers, baselines, and intelligently monitors Amazon Web Services cloud environments.

## Monitoring and problem detection

Dynatrace AWS monitoring performs AI-based automatic business impact, problem detection, and root cause analysis for all AWS services based on all metrics published to Amazon CloudWatch. This analysis can be additionally extended by full-stack monitoring provided by OneAgent deployed on compute resources such as Amazon EC2, AWS Lambda, and Kubernetes. All of the entities can also be subject to comprehensive log analysis.

In addition to the above, Dynatrace enables the understanding of workload applied AWS resources and environment dynamics per region.

The AWS monitoring is available for all Dynatrace customers, regardless of whether their Dynatrace cluster is SaaS-based or Managed.

## Ease of use and convenient visualization

Amazon Web Services monitoring comes with consistent out-of-the-box metrics, dashboards, and alerts immediately after monitoring is enabled.

The measurements and analysis of core AWS services are visualized on a purpose-built infographics dashboard (see the gallery). Convenient reports and dashboards are also available for business impact analysis and topology maps.

## Flexibility

The Dynatrace users can select which services and instances are monitored and how this process is performed. This selection can be done as part of the initial monitoring setup or at any later point. This also applies to new services enabled on the AWS cloud or added by Amazon.

It is possible to choose monitoring metrics for each of the supporting services. Equally, all the dashboards for AWS monitoring can be cloned and easily customized as needed.

## Hybrid environments

Tracking of services and dependencies is not limited to AWS. Thanks to Dynatrace Intelligence and its ability to process data from all types of environments, Dynatrace is optimized for monitoring hybrid environments, including business applications spanning across multiple cloud and virtualization platforms such as Microsoft Azure, Google Cloud, VMware, Kubernetes, Openshift, and on-premises infrastructure.

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").


---


## Source: azure-monitoring.md


---
title: Microsoft Azure monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring
scraped: 2026-02-06T16:29:13.189649
---

# Microsoft Azure monitoring

# Microsoft Azure monitoring

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 28, 2026

Dynatrace automatically discovers, baselines, and intelligently monitors Microsoft Azure cloud environments.

## Monitoring and problem detection

Dynatrace Azure monitoring performs AI-based automatic business impact, problem detection, and root cause analysis for all Azure services based on all metrics published to Azure Monitor. This analysis can be additionally extended by full-stack monitoring provided by OneAgent deployed on compute resources such as Azure Virtual Machines, Azure App Service, and Azure Kubernetes Service. All of the entities can also be subject to comprehensive log analysis.

In addition to the above, Dynatrace enables the understanding of workload applied Azure resources and environment dynamics per region.

Azure monitoring is available for all Dynatrace customers, regardless of whether their Dynatrace cluster is SaaS-based or Managed.

## Ease of use and convenient visualization

Azure monitoring comes with consistent out-of-the-box metrics, dashboards, and alerts immediately after monitoring is enabled.

The measurements and analysis of core Azure services are visualized on a purpose-built infographics dashboard (see the gallery). Convenient reports and dashboards are also available for business impact analysis and topology maps.

## Flexibility

Dynatrace users can select which services and instances are monitored and how this process is performed. This selection can be done as part of the initial monitoring setup or at any later point. This also applies to new services enabled on the Azure cloud or added by Microsoft.

It is possible to choose monitoring metrics for each of the supporting services. Equally, all the dashboards for Azure monitoring can be cloned and easily customized as needed.

## Hybrid environments

Tracking of services and dependencies is not limited to Azure. Thanks to Dynatrace Intelligence and its ability to process data from all types of environments, Dynatrace is optimized for monitoring hybrid environments, including business applications spanning across multiple cloud and virtualization platforms such as AWS, Google Cloud, VMware, Kubernetes, Openshift, and on-premises infrastructure.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")


---


## Source: create-aws-connection.md


---
title: Create a new AWS connection
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app/create-aws-connection
scraped: 2026-02-17T21:17:01.128157
---

# Create a new AWS connection

# Create a new AWS connection

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 19, 2025
* Preview

If this is the first time you are creating a connection, first see the [onboarding instructions](/docs/ingest-from/amazon-web-services/create-an-aws-connection "See the differences between creating your AWS connections via API or ::app-settings::.") and its prerequisites.

If you have an existing classic connection and want to start the new cloud platform monitoring, delete the classic connection first and only then create a new cloud connection for the respective AWS Account or Azure subscription.

To set up a new AWS connection

1. Go to ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
2. In the upper-right corner of the page, select  **Create connection** > **AWS New**.

   Note: If it's your first cloud connection, you can also select **Create connection** > **AWS New** on the Overview page.
3. Follow the steps outlined in **New connection** to start the onboarding process for a new AWS cloud connection.

   ![Clouds app | Create a new AWS connection](https://dt-cdn.net/images/clouds-app-create-an-aws-connection-3840-485c4caab2.png)
4. After youâve successfully deployed the CloudFormation stack within AWS, it takes up to 15 minutes to see your cloud inventory on the new **Explorer New** tab view within ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
5. Optional Check the state and health of your cloud connection in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization**.
   2. Select **AWS**.
6. Optional Set up and configure health alerts and warning signals in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Alerts** > **Cloud services**.
   2. Select **New Alerts**.
   3. Follow the steps in the wizard to create health alerts for your newly onboarded AWS Account.

   ![Settings | Ready-made alerts](https://dt-cdn.net/images/settings-ready-made-alerts-3840-d19f21a2a8.png)![Settings | Health alert details](https://dt-cdn.net/images/settings-health-alert-details-3840-f4fc0982c7.png)

   1 of 2


---


## Source: clouds-app.md


---
title: Clouds app
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app
scraped: 2026-02-17T21:13:47.855169
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


---


## Source: gcp-monitoring.md


---
title: Google Cloud monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/gcp-monitoring
scraped: 2026-02-06T16:29:02.800414
---

# Google Cloud monitoring

# Google Cloud monitoring

* Latest Dynatrace
* Explanation
* 1-min read
* Published Jan 27, 2023

Dynatrace automatically discovers, baselines, and intelligently monitors dynamic Google Cloud workloads.

## Full-stack monitoring

Dynatrace OneAgent provides full-stack monitoring for core compute resources such as Google Kubernetes Engine (GKE), Google Compute Engine (GCE), and Google Application Engine (GAE). This gives you deep code-level visibility and end-to-end traces for everything thatâs running on compute services.

## Google Cloud services monitoring

All metrics published to the Operations API (formerly Stackdriver) can be automatically ingested into Dynatrace to provide data for AI-powered problem detection and automatic root cause analysis. Our Google Cloud integration helps you stay on top of the dynamics of your hybrid cloud by providing a high-level overview of the Google Cloud services in your account, distinguishing between healthy and unhealthy services.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")


---


## Source: use-cases.md


---
title: Use cases
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/use-cases
scraped: 2026-02-16T21:24:20.165678
---

# Use cases

# Use cases

* Latest Dynatrace
* Overview
* 1-min read
* Published Nov 26, 2024

[### Data-driven cloud tuning

Manage your cloud deployment using Grail and your cloud vendor-provided data in context.](/docs/observe/infrastructure-observability/cloud-platform-monitoring/use-cases/cloud-costs "Manage your cloud deployment using Grail and your cloud vendor-provided data in context.")[![Threat hunting](https://cdn.bfldr.com/B686QPH3/at/5zkt85btt85svwwb79495t3j/DT0080.svg?auto=webp&width=72&height=72 "Threat hunting")

### Threat hunting and forensics

Search for indicators of compromise (IoC) and perform forensic investigations and threat hunting activities.](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")[### Analyze AWS CloudTrail logs

Analyze CloudTrail logs and find potential security issues with Dynatrace Investigations.](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")[### Analyze Amazon API Gateway access logs

Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace Investigations.](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")[### Detect threats against your AWS Secrets

Monitor and identify potential threats against your AWS Secrets with Dynatrace Investigations.](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")


---


## Source: cloud-foundry-monitoring.md


---
title: Cloud Foundry monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring
scraped: 2026-02-06T16:28:51.845671
---

# Cloud Foundry monitoring

# Cloud Foundry monitoring

* Latest Dynatrace
* 1-min read
* Published Aug 12, 2021

Dynatrace supports full-stack monitoring for Cloud Foundry, from the application down to the infrastructure layer.

## Prerequisites

1. [Set up and configure Dynatrace integration on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.")
2. [Connect your cluster to Dynatrace](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.")

See [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.") for further options and details.

## Monitoring configuration options

[Organize deployments by tags](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/organize-cf-deployments-by-tags "Automatically organize and filter all your monitored applications by applying tags from your Cloud Foundry environment.").

[Define process group metadata for Cloud Foundry applications](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/define-process-group-metadata-for-cloud-foundry-applications "Define Cloud Foundry service metadata and reuse it for multiple applications.").

## View monitoring results

To learn how to analyze monitoring results in Dynatrace, see [Cloud Foundry metrics overview](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics "Available metrics for monitoring your Cloud Foundry clusters with Dynatrace").

## Related topics

* [Set up Dynatrace on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")


---


## Source: container-groups.md


---
title: Monitor container groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups
scraped: 2026-02-17T21:21:57.649991
---

# Monitor container groups

# Monitor container groups

* How-to guide
* 3-min read
* Updated on Apr 21, 2024

The **Container groups** overview page allows you to list all the containers in your environment and filter them by the process group, container group, or Kubernetes properties.

1. Go to **Containers** to list all container groups in your environment.

   ![Container groups overview](https://dt-cdn.net/images/screenshot-2022-09-12-at-10-13-25-1737-8388b7f687.png)

   The **Container groups** table shows the properties of individual container groups. You can filter this table by:

   * **Name**: the container group name.
   * **Image name**: the image name assigned to the specific Docker container group. Docker containers only
   * **K8s namespace**: the Kubernetes namespace to which the containers are assigned. Kubernetes containers only
   * **K8s container name**: the name of the Kubernetes container. Kubernetes containers only
   * **K8s pod name**: the full name of the Kubernetes pod to which the container belongs. Kubernetes containers only
2. Select a container group from the table to go to the container group overview page.

   ![Container group overview](https://dt-cdn.net/images/screenshot-2022-09-12-at-10-34-05-1728-233f3fccd3.png)

## Container analysis

To get a better understanding of container behavior, go to the **Container analysis** section. Youâll see all the containers assigned to the selected container group.

Provided metrics include:

* **CPU usage, mCores**: CPU usage per container in millicores.
* **CPU throttling, mCores**: CPU throttling per container in millicores.
* **Memory usage, bytes**: resident set size (Linux) or private working set size (Windows) per container in bytes.

Select the container to access the container overview page, where you can view the details and available metrics for the selected container.

Leverage these charts

Select  in the upper-right corner of a chart to:

* **Show in Data Explorer**âOpens [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") for the associated query, so you can view the associated query, explore the data more in-depth, adjust the chart settings, and pin the chart to your own dashboard.
* **Create metric event**âOpens the [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") for the selected metric.
* **Pin to dashboard**âPins a copy of the selected chart to any classic dashboard you can edit. For example, if certain hosts are particularly important to your business, create a dashboard designated to monitoring only those hosts, and then pin charts from their host overview pages to that dashboard, all with almost no typing. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Process groups

The **Process groups** section shows all process groups for the selected container group. Select a process group from the table to go to the dedicated overview page. For more information, see [Overview of all technologies running in your environment](/docs/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Get a summary of the performance of all the technologies in your environment.").

## Events

The **Events** tile charts the distribution of [events](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page."), such as service deployments, process crash details, and memory dumps. Expand the tile to list events.

## Logs

The log viewer timeline is interactive, allowing a global timeline selection. Use it to identify issues around a specific log event and see how it relates to the container performance.

Leverage these charts

Select  in the upper-right corner of a chart to:

* **Go to Log Viewer**âOpens the [Log Viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.") page filtered by the selected container group.
* **Create metric**âOpens the [Log metrics](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.") page with the **Query** value set to the selected container group.


---


## Source: container-monitoring-rules.md


---
title: Container monitoring rules
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/container-monitoring-rules
scraped: 2026-02-17T21:21:56.449109
---

# Container monitoring rules

# Container monitoring rules

* How-to guide
* 2-min read
* Published Jun 25, 2021

To manage all container-related settings, follow the instructions below.

## Define container monitoring rules

The container monitoring rules define if deep monitoring is enabled for processes running in containers.

**To add a monitoring rule**

1. Go to **Settings** > **Processes and containers** > **Container monitoring rules**.
2. Select **Add item**.
3. Select the **Mode**: whether you want Dynatrace to monitor the container.
4. Select the **Container property** to compare against your rule.
5. Select the condition operator (for example `begins with`)
6. Set the condition value.
7. Select **Save changes** to save your configuration and the new rule to your list of container monitoring rules.

**To edit a custom monitoring rule**

1. Go to **Settings** > **Processes and containers** > **Container monitoring rules**.
2. Find the rule and make your changes.

   * To change the rule conditions, display the **Details** and make changes as needed
   * To delete the rule, select in the **Delete** column
   * To disable or enable the rule, change the switch setting in the **Enabled** column
   * To move the rule up or down in the list, in the **Order** column, select and drag the rule to a new position

     Container monitoring rules are executed in the order in which they appear on the list.
3. Select **Save changes**.

## Enable or disable container monitoring rules

There are two categories of container monitoring rules that you can enable or disable by default:

* Custom rulesâcreated by you
* Built-in rulesâdefined by Dynatrace

**To enable/disable a custom monitoring rule**

1. Go to **Settings** > **Processes and containers** > **Container monitoring rules**.
2. Find the rule and change the switch setting in the **Enabled** column.
3. Select **Save changes** to save your configuration.

**To enable/disable built-in monitoring rules**

1. Go to **Settings** > **Processes and containers** > **Built-in container monitoring rules**.
2. Turn these rules on or off as needed:

   * Do not monitor containers where Kubernetes container name equals `POD`
   * Do not monitor containers where Docker stripped image name contains `pause-amd64`
   * Do not monitor containers where Kubernetes namespaces equals `openshift-sdn`
3. Select **Save changes** to save your configuration.

Built-in rules are enabled by default. You can choose to disable them, but you can't edit them.

## Limitations

* Container monitoring rules are effective only when you install OneAgent on your hosts.
* Application-only integrations without a full OneAgent installation donât support monitoring rules. However, in such situations, the integrations themselves effectively provide the same level of control over your container monitoring setup.
* In Kubernetes, container monitoring rules apply only to the `classicFullStack` injection mode.

  Container monitoring rules are ignored for webhook-based injection modes (`cloudNativeFullStack` or `applicationMonitoring`). For these modes, use the annotation-based configuration option as described in [Configure monitoring for namespaces and pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods").


---


## Source: heroku.md


---
title: Heroku monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/heroku
scraped: 2026-02-06T16:28:55.999404
---

# Heroku monitoring

# Heroku monitoring

* Reference
* 2-min read
* Published May 22, 2019

With Dynatrace cloud-native monitoring enabled for your Heroku applications, you get

* Deep application monitoring and code-level details for Java, PHP, Node.js and more â with just a single, language-independent buildpack
* [Automatic root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") of your Heroku web applications
* Insights into how your Heroku applications use [databases](/docs/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.")âincluding detailed metrics for each database statement
* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") data on customersâ web browser and mobile device behavior
* Automated external and third-party service monitoring (for example, calls to external REST APIs)

## Prerequisites

[Set up and configure Dynatrace integration on Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## View monitoring results

After linking your Dynatrace account with your Heroku application, youâll receive the full range of application and service monitoring visibility that Dynatrace provides (for example, **Smartscape** and service-level insights with **Service flow**). Dynatrace automatically detects that your application is running on Heroku as well as services related to you Heroku application.

![Heroku monitoring](https://dt-cdn.net/images/heroku1-2874-778cc74486.png)

Dynatrace automatically initiates deep application monitoring for your Heroku applications and provides code-level visibility into your applicationsâ services. Dynatrace **Service flow** allows you to track how requests to services provided by your Heroku application are propagated through a system. Service tracing also helps to identify performance bottlenecks and failed requests in the service-to-service communication chain. With Dynatrace, itâs never been easier to pinpoint the root cause of poor performance in heterogeneous microservices stacks.

![Heroku monitoring](https://dt-cdn.net/images/heroku2-2884-8bad582082.png)

## Tag your Heroku applications

You can use the Dynatrace powerful [tagging mechanism](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to automatically organize and filter all monitored Heroku application components. Dynatrace allows you to apply tags to processes and hosts based on environment variables.

`heroku config:set DT_TAGS=owner=team-easytravel`

## Related topics

* [Set up Dynatrace on Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")


---


## Source: existing-clusters.md


---
title: Enable Kubernetes experience for existing clusters
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/enable-k8s-experience/existing-clusters
scraped: 2026-02-06T16:19:46.615282
---

# Enable Kubernetes experience for existing clusters

# Enable Kubernetes experience for existing clusters

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 19, 2024

You have the option to enable all or specific Kubernetes clusters to benefit from the new Kubernetes experience.

You could accomplish this using the Settings API with the [Kubernetes app schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes "View builtin:app-transition.kubernetes settings schema table of your monitoring environment via the Dynatrace API."), or alternatively, by configuring the setting as described next.

## Enable all clusters

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Turn on **New Kubernetes experience**.

## Enable specific clusters

1. In ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, select **Activation pending** in the top menu bar.
2. Select **Activate** for your desired cluster.

   ![Activation pending](https://dt-cdn.net/images/activation-pending-3718-f43bc57878.png)
3. Turn on **New Kubernetes experience**.

When you enable Kubernetes clusters for the new Kubernetes experience, Dynatrace starts to report observability data to the Dynatrace platform, including Grail as a data lakehouse.


---


## Source: enhanced-object-vis-preview.md


---
title: Kubernetes Enhanced Object Visibility Preview
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/preview/enhanced-object-vis-preview
scraped: 2026-02-06T16:19:47.983316
---

# Kubernetes Enhanced Object Visibility Preview

# Kubernetes Enhanced Object Visibility Preview

* Latest Dynatrace
* Overview
* Updated on Jan 28, 2026

Completed preview

The Kubernetes Enhanced Object Visibility Preview introduces a new way to explore Kubernetes environments in Dynatrace, offering deeper visibility, improved performance, and powerful troubleshooting capabilities. **The preview is completed since December 2025**.

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine

  + There is a very small exception for a few specific tenants that won't be able to access the preview. More information on that will be available within the product.
* [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") with the **Kubernetes Platform Monitoring** capability on your Rate Card
* [Sufficient permissions](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/reference/permissions "Overview of user and tailoring permissions.") to use ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** within your Dynatrace environment
* Dynatrace version 1.324+
* ActiveGate version 1.323+
* Dynatrace Operator version 1.7.0+
* Kubernetes app version 1.33.0+

Overview

Setup

FAQ

By enabling this preview, youâll gain:

* Visibility into additional Kubernetes objects: Ingress, NetworkPolicies, CRDs, PVCs, PVs, ConfigMaps, and more.
* Access to YAML definitions to debug and validate configurations in real time.
* Ability to query YAMLs across all clusters and namespaces using Dynatrace Query Language (DQL) to instantly surface misconfigurations, missing references, or policy violations across your Kubernetes environment

Specifically, this preview unlocks visibility into:

* Storage: Persistent Volumes (PV), Persistent Volume Claims (PVC)
* Networking: Ingress, Network Policies
* Custom Resources: CRDs and selected CRs
* Optional Configuration: ConfigMaps and Secrets

  + Secrets and ConfigMaps are not ingested by default due to their potentially sensitive content. To monitor these Kubernetes objects, you can manually grant the necessary permissions. For instructions on how to enable ConfigMaps and Secrets, see the [Setup tab](#setup).

This preview also adds insights into the YAML files of all Kubernetes objects, allowing you to inspect object configurations directly in Dynatrace. Turn on **Watch** to stream updates of these configurations within a few seconds to the web UI, allowing for fast validation of recent changes. The YAML is currently limited to a size of 32 kb, and we automatically strip less important fields (for example, `/metadata/managedFields` and `kubectl.kubernetes.io/last-applied-configuration` annotation).

These additions are available upon opt-in on the additional **Explorer (Preview)** tab in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

![Enhanced object visibility preview in the Kubernetes app.](https://dt-cdn.net/images/k8s-enhanced-object-visibility-preview-1920-7aa7863ffb.png)

A variety of further use-cases are unlocked, by allowing users to query all YAML files also via DQL. You can find a notebook with different examples within our [communityï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132).

To opt in to this preview, go to **Settings** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**. This setting is available within the scope of your tenant or within the scope a monitored Kubernetes cluster.

We recommend getting started by enabling the preview only for a single Kubernetes cluster first, as this new functionality might increase the load on the ActiveGate monitoring this cluster. To enable this only for one cluster, go to the Settings of a selected cluster within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and select  > **Connection settings** in the upper-right corner of the cluster's detail page.

![Enable Kubernetes Enhanced Object Visibility](https://dt-cdn.net/images/k8s-enable-public-preview-7e45dfe3d5.gif)

If you've set tight resource constraints (CPU and memory limits) on the ActiveGate monitoring this cluster, this might cause interruptions in your monitoring. You can easily remedy that by increasing the configured limits, or by removing them temporarly to find a good fit for new limits. While the ingest of additional data can be controlled on a cluster-by-cluster basis, the additional **Explorer (Preview)** tab within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** is available as soon as any cluster is enabled for the preview.

## Unlocking ConfigMaps and Secrets

To gain visibility into ConfigMaps and Secrets, you need to grant additional permissions to the ActiveGate, allowing it to access these objects. By default, this functionality is disabled because these objects might contain sensitive data. For Secrets, ActiveGate automatically applies data masking.

Apply the following YAML with `kubectl` to enable these objects:

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: dynatrace-kubernetes-monitoring-sensitive



subjects:



- kind: ServiceAccount



name: dynatrace-kubernetes-monitoring



namespace: dynatrace



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



labels:



rbac.dynatrace.com/aggregate-to-monitoring: "true"



rules:



- apiGroups:



- ""



resources:



- configmaps



- secrets



verbs:



- list



- watch



- get
```

## Does this preview increase my DPS consumption?

The preview builds upon the existing ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and the corresponding license based on [pod-hours](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged."). The consumed pod-hours include insights into all newly added Kubernetes objects, meaning there won't be any increase in DPS consumption specific to this preview.

## What happens technically by joining this preview?

Dynatrace starts to ingest Kubernetes objects additionally into the new Smartscape. The newly unlocked objects (for example, Ingress, Network Policies) will only be available in the new Smartscape. This unlocks easier DQL access, faster queries, and access to the YAML of these objects. We will continue to write the existing entities into the old storage. In our [communityï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132), you also find a notebook that helps you get started working with Kubernetes objects stored in the new Smartscape using DQL. Within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, the new **Explorer (Preview)** automatically leverages the new Smartscape in the background, while the already existing **Explorer** continues to operate on data stored in our old storage.

## Where will this preview go from here?

The **Explorer (Preview)** will incrementally improve over the next months until it includes all the same features as the existing **Explorer**. With the GA of this new functionality, **Explorer (Preview)** will replace the existing **Explorer** for everyone, and we also plan to include more custom resources. We would be happy to hear [your feedbackï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132) on which ones would be most important to you.
We will continue for some time to offer the entities that powered the former **Explorer** via DQL (for example, fetch dt.entity.cloud\_application).

## What observability option do I need for this preview? Do I need Full-Stack observability?

This preview is based on **Kubernetes platform monitoring**, which is included in all [observability options](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

## What are top-level workloads?

A top-level workload is the topmost controlling owner of a Pod.
Possible top-level workload types are: Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, CronJob, ReplicationController, DeploymentConfig.
A list of those workloads can be found in the `Top-level workloads` menu entry.

## What do I see in the `Definition (YAML)` view?

When first opening this view you see a reduced version of the original YAML as available from the Kubernetes API. When you activate the live mode, you get full YAML directly streamed from the Kubernetes API.

The reduced version of the YAML is also available in json format via DQL in the `k8s.object` field of the respective Smartscape node.
Please note, that labels and annotation are not part of this field, but are stored as `tags`.

## How can I fix missing `ClusterRole` permissions?

The newly added Kubernetes object types require additional ActiveGate permissions. These permissions (except for ConfigMaps and Secrets [1](#fn-1-1-def)) are automatically granted when Dynatrace Operator is updated to [version 1.7.0](/docs/whats-new/dynatrace-operator/dto-fix-1-7-0 "Release notes for Dynatrace Operator, version 1.7.0"). Customers using older Dynatrace Operator versions, or those who manually have overwritten the ActiveGate permissions, may lack access to the new Kubernetes endpoints. If permissions are missing, a warning message appears above the table (for example `Missing "ConfigMap" ClusterRole permission for cluster(s): aks-playground-dev.`):

![How can I fix missing ClusterRole permissions?](https://dt-cdn.net/images/image-20250909-123859-2305-e1ca79056f.png)

To fix this, [update your Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#update "Upgrade and uninstallation procedures for Dynatrace Operator") to version 1.7.0+.

1

ConfigMaps and Secrets can contain sensitive information. Therefore, Dynatrace Operator version 1.7.0 does not grant permissions to these endpoints by default. To enable access to these objects, follow the guidance provided in [Unlocking ConfigMaps and Secrets](#setup).

## Learn more

Dive deeper into ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** with the following resources:

[### Feedback channel for Kubernetes Enhanced Object Visibility Preview

You can find a notebook with different examples within our community.](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132)

[### Playground environment

Test the app in a sandbox environment.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.kubernetes)[### 0 to Full Observability in Kubernetes in under 3 minutes

A quick video tutorial on how to install Dynatrace Operator.](https://dt-cdn.net/resources/product/videos/k8s-0-to-full-observability.mp4)[### Blog post: Unlock the Power of DevSecOps with Newly Released Kubernetes Experience for Platform Engineering](https://www.dynatrace.com/news/blog/kubernetes-platform-engineering/)


---


## Source: permissions.md


---
title: Permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/reference/permissions
scraped: 2026-02-06T16:19:43.850239
---

# Permissions

# Permissions

* Latest Dynatrace
* Reference
* 1-min read
* Published Jan 19, 2024

This guide outlines the necessary permissions for ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and describes how to tailor them to fit specific roles and requirements.

## User permissions

To fully utilize all use cases of ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, a specific set of permissions is required. You can find the complete list of these permissions via Dynatrace Hub.

In Dynatrace Hub, select **Kubernetes** ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") to view the necessary permissions.

To manage permissions within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, you can assign default policies to different roles assigned to user groups (such as **AppEngine User**, **Storage All Grail Data Read**).

## Tailoring permissions/policies

Dynatrace IAM allows for a highly detailed and flexible definition and assignment of permissions. These permissions can be grouped into policies and then assigned to users or groups. Additionally, permissions can be targeted to specific subsets of Kubernetes objects by using conditions, such as for particular clusters and/or namespaces.

For more information, see [Identity and access management (IAM)](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Example policy

```
ALLOW hub:catalog:read;



ALLOW storage:buckets:read, storage:entities:read, storage:events:read, storage:logs:read, storage:metrics:read;



ALLOW environment-api:api-tokens:write, environment-api:entities:read, environment-api:entities:write, environment-api:metrics:read, environment-api:security-problems:read, environment-api:slo:read;



ALLOW settings:objects:read, settings:objects:write, state:user-app-states:read, state:user-app-states:write;



ALLOW davis:analyzers:execute, unified-analysis:screen-definition:read;
```


---


## Source: kubernetes-app.md


---
title: Kubernetes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app
scraped: 2026-02-06T16:18:49.950622
---

# Kubernetes

# Kubernetes

* Latest Dynatrace
* App
* 7-min read
* Updated on Jan 28, 2026

The new [Kubernetes experienceï»¿](https://dt-url.net/k1038uw) is optimized for DevOps Platform Engineers and Site Reliability Engineers (SREs), focusing on the health and performance optimization of multicloud Kubernetes environments. The centerpiece of this experience is the ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

The underlying metrics, events, and logs are all powered by [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), which supports flexible analytics through the [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, and ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

## Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine
* [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") with the **Kubernetes Platform Monitoring** capability on your Rate Card
* [Sufficient permissions](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/reference/permissions "Overview of user and tailoring permissions.") to use the ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** within your Dynatrace environment
* ActiveGate version 1.327+ is a prerequisite for [Kubernetes Enhanced Object Visibility](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/preview/enhanced-object-vis-preview "Accelerate root cause analysis with deeper Kubernetes object visibility.").

  + Older ActiveGate versions are supported in backward compatibility mode; in that mode, an additional **Explorer (Classic)** tab appears in the UI.

For more details, see [getting started FAQ](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/enable-k8s-experience#k8s-app-getting-started-faq "Enable Kubernetes experience for existing clusters or start monitoring new clusters.").

The new Kubernetes experience is not available for Managed or SaaS on non-Grail environmentsâyou can continue to use [**Kubernetes Classic**](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.") (accessible from the previous Dynatrace via **Kubernetes**).

## Get started

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** provides a comprehensive view of your environment, enabling you to automate monitoring and optimize the health and performance of your Kubernetes clusters and workloads. This page walks you through the main concepts underlying ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

With ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, you can:

* Set up Kubernetes monitoring with Dynatrace.
* Explore cluster, node, and workload insights.
* Analyze health status with Dynatrace Intelligence.
* Detect and troubleshoot Kubernetes issues.

![High-level overview of all your Kubernetes clusters, independent of the cloud service they run on.](https://dt-cdn.net/hub/highleveloverview2.png)![Detailed view of a single cluster showing all health-relevant signals of contained resources, including nodes, namespaces, and workloads.â](https://dt-cdn.net/hub/detailedviewofsinglecluster.png)![View the health state of a particular workload and get further details, so you can quickly decide on the next course of action.](https://dt-cdn.net/hub/healthofworkload.png)![Customize your Kubernetes monitoring using ready-made dashboards.](https://dt-cdn.net/hub/inx16596.sprint.apps.dynatracelabs.com_uiFull-HD_1oyEkuF.png)![Onboard new Kubernetes clusters in just five minutes, no matter the cloud service they run on. No docs are required.](https://dt-cdn.net/hub/NewWelcomeScreenK8s_RxlAOrb.png)

1 of 5High-level overview of all your Kubernetes clusters, independent of the cloud service they run on.

### Setup and reference

Use the following guide to set up and configure Kubernetes monitoring in Dynatrace.

[01Enable Kubernetes experience for existing clusters

* How-to guide
* Enable existing clusters for the new Kubernetes experience.](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/enable-k8s-experience/existing-clusters)

## Explorer

Explorer is the shared Dynatrace interface for monitoring and analyzing different technology domains. It defines a common layout (sidebar, list, filter bar, health indicators, and detail panels) with consistent filtering, perspectives, drillâdown navigation, and unified analysis.

The sections below describe how Explorer appears in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

### Basic structure

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** offers insights into your entire Kubernetes environment, presenting valuable information across primary areas as indicated in the picture below.

![An overview of the Clusters page in the Kubernetes app.](https://dt-cdn.net/images/k8s-clusters-page-overview-1920-faadf96144.png)

* **Sidebar (1)**

  Located on the left side, the sidebar groups all [Kubernetes objectsï»¿](https://dt-url.net/q0038e6) by type, including clusters, nodes, namespaces, workloads, pods, services, and containers.
* **Object list (2)**

  The central table displays all objects of the selected type, serving as the starting point for analysis and drill-down for your observability use cases.
* **Aggregated health bar (3)**

  Located above the object list, this bar provides an aggregated [health status](#health-status) of the displayed objects and their child objects.
* **Filter bar (4)**

  The filter bar below the app header allows you to narrow down the object list view, focusing on specific objects or health statuses.

### Detail view

Select a Kubernetes object from the list to open a detail view and focus on the specific object.

![An example of the cluster health details page in the Kubernetes app.](https://dt-cdn.net/images/k8s-cluster-health-details-example-1920-4a19911c0d.png)

* **Top summary section (1)**

  The top pane provides a quick summary of the health and security status of the selected object and its child objects.
* **Main detail section (2)**

  The main section provides detailed insights of the given object, featuring tabs for analyzing health and utilization, as well as for exploring logs, events, ownership, and vulnerabilities. The data presented in the detailed view remains consistent regardless of any filters applied in the main interface.

### Perspectives

Perspectives are located under the aggregated health bar. They support various use cases, such as health monitoring or resource optimization.

![An example of the clusters page in the Kubernetes app.](https://dt-cdn.net/images/k8s-clusters-health-example-1920-463f1b6358.png)

* **Selecting a perspective (1)**

  Choosing a perspective changes which columns are displayed in the table. For example:

  + **Health**âshows health-related information and alerts.
  + **Utilization**âfocuses on CPU, memory, and other resource usage metrics.
* **Customizing columns (2)**

  You can add or remove columns within a selected perspective to match your analysis needs. Your personal configuration persists in your browser, and you can reset to the default layout at any time by selecting ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") next to the list of available perspectives (1).

### Dynatrace Intelligence health status

The health status is based on the Kubernetes-focused custom alerts. Health indicators aggregate the states of these custom alerts per resource.

A Kubernetes object (such as a cluster) is considered unhealthy if any of its associated custom alert configurations are in an unhealthy state. By selecting a specific health indicator, you can gain further insights into the underlying reasons for this status.

![Example of Dynatrace Intelligence health status for a Kubernetes cluster.](https://dt-cdn.net/images/k8s-dynatrace-intelligence-cluster-health-status-1920-4200846da4.png)

Example

In this example, you can see that 8 nodes out of 24 are currently considered unhealthy.

1. Select the red numbers displayed within the health status area to drill down to the list of currently unhealthy nodes.

   ![An example of a Dynatrace Intelligence warning signal in the Kubernetes app.](https://dt-cdn.net/images/k8s-dynatrace-intelligence-warning-signals-1393-cb95af4862.png)
2. Select any node to open the details view of the problematic node, including key metrics and events that led to their current state.

   ![Warning events 2](https://dt-cdn.net/images/warning-events-2-1914-c65669ad3d.png)

   The **Recommendations** tab presents best-practice Kubernetes health alerts for clusters, nodes, namespaces, persistent volume claims, and workloads. It highlights which alerts are active, partially active, or inactive across your environment.

   Select **Activate** or **Configure** to open the settings where you can apply the recommended alert configuration.

   ![Recommendations](https://dt-cdn.net/images/recommendations-1909-f9f2da2e1a.png)

### Health alerts and warning signals

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

While they may not always represent active health issues at the moment, frequent **Unhealthy** signals, for instance, might indicate misconfigured readiness probes, inappropriate CPU limits, or unusually high workload.

Sorting and filtering of warning signals

There are two types of warning signals. They're organized as follows:

* Problematic conditions affect the health of the node or workload (for example, `DiskPressure`, `MemoryPressure`).

  + Listed first
  + Sorted alphabetically within each category
* Warning events are less critical, and often signal temporary issues (for example, `OOMKilled`, `PodEviction`).

  + Listed after problematic conditions
  + Sorted by their frequency

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** provides several interaction options:

* Context menu actions:

  + **Go to affected nodes** or **Go to affected workloads**: Navigates directly to the nodes or workloads experiencing the selected condition. This opens a filtered view displaying only the affected nodes or workloads.
  + **Explore events**: Opens a detailed log view showing the events associated with the warning signal.
  + **Filter for**: Automatically applies a filter to show only the entities impacted by the specific condition or event.
* Filtering from the menu bar:
  You can apply filters directly from the menu bar by selecting either general categories such as **Any problematic condition** or individual signals like `MemoryPressure:True` or `FailedMount`. Once filtered, the view updates to focus on the entities affected by the selected filter.

![Dynatrace Intelligence warning signals for Nodes in the Kubernetes app.](https://dt-cdn.net/images/k8s-nodes-warning-signals-1920-47b6aa9589.png)

| Column | Content | Examples |
| --- | --- | --- |
| Node warning signals | [Combines events emitted by nodes and problematic node conditions](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues#node "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") | `DiskPressure`, `MemoryPressure`, `NodeNotReady` |
| Pod warning signals | [Combines events emitted by pods and conditions affecting pods](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues#workload "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") | `BackOff`, `PodEviction`, `OOMKilled` |
| Workload warning signals | [Combines events emitted by namespaces, workloads, and pods, along with workload conditions](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues#workload "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") | `CPUThrottlingHigh`, `ContainerRestarts`, `PodsPending` |

## Use cases

## Reference

Go to the following reference pages for more information about permissions, available alerts, and default settings for new environments.

## Related topics

Dive deeper into ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** with the following resources:

* [Playground environmentï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.kubernetes): Test the app in a sandbox environment.
* [0 to Full Observability in Kubernetes in under 3 minutesï»¿](https://dt-cdn.net/resources/product/videos/k8s-0-to-full-observability.mp4): A quick video tutorial on how to install Dynatrace Operator.
* [Blog post: Unlock the Power of DevSecOps with Newly Released Kubernetes Experience for Platform Engineeringï»¿](https://www.dynatrace.com/news/blog/kubernetes-platform-engineering/)

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Automated change impact analysis for your deployment and release processes.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=kubernetes&internal_source=doc&internal_medium=link&internal_campaign=cross)


---


## Source: alert-on-kubernetes-issues.md


---
title: Alert on common Kubernetes/OpenShift issues
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues
scraped: 2026-02-17T21:16:38.449776
---

# Alert on common Kubernetes/OpenShift issues

# Alert on common Kubernetes/OpenShift issues

* 18-min read
* Updated on Feb 21, 2025

Dynatrace version 1.254+

ActiveGate version 1.253+

To [alert on common Kubernetes platform issuesï»¿](https://dt-url.net/zg034mg), follow the instructions below.

## Configure

There are three ways to configure alerts for common Kubernetes/OpenShift issues.

Configuring an alert on a different level is only intended to simplify the configuration of multiple entities at once. It does not change the behavior of an alert.

For example, enabling a workload CPU usage saturation alert will still evaluate and raise problems for each Kubernetes workload separately, even if it has been configured on the Kubernetes cluster level.

For further details on the settings hierarchy, see [Settings documentation](/docs/manage/settings/settings-20#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework").

Per tenant level

Per cluster level

Per namespace level

* Settings apply to all clusters, nodes, namespaces, or workloads in the Kubernetes/OpenShift tenant.
* To configure settings, go to **Settings** > **Anomaly detection** and select any page under the **Kubernetes** section.

**Example:**

![Kubernetes anomaly detection settings tenant](https://dt-cdn.net/images/k8s-anomaly-settings-tenant-899-e99e56395b.png)

* Settings apply to a selected cluster, or to nodes, namespaces, and workloads from a selected cluster.
* To configure settings, go to the settings of a selected Kubernetes cluster and select any page under **Anomaly detection**.

**Example:**

![Kubernetes anomaly detection settings cluster](https://dt-cdn.net/images/k8s-anomaly-settings-cluster-948-0650f7b0a9.png)

* Settings apply to selected namespaces or workloads.
* To configure settings, go to the settings of a selected namespace and select any page under **Anomaly detection**.

**Example:**

![Kubernetes anomaly detection settings namespace](https://dt-cdn.net/images/k8s-anomaly-settings-namespace-899-1870ebd4ea.png)

## View alerts

Manually closed problems will show up again after 60 days if their root cause remains unresolved.

You can view alerts

* On the **Problems** page.

  **Example problem:**

  ![k8s-alert-view-in-problems](https://dt-cdn.net/images/image-12-1416-df0a0171a6.png)
* In the **Events** section of a cluster details page.

  **Example event:**

  ![k8s-alert-view-in-events](https://dt-cdn.net/images/image-13-799-41970d77a3.png)

  Select the event to navigate to Data Explorer for more information about the metric that generated the event.

## Available alerts

See below for a list of available alerts.

### Cluster alerts

Alert name

Dynatrace version

Problem type

Problem title

Problem description

De-alerts after

Calculation

Supported in

[Detect cluster CPU-request saturation](#detect-cluster-cpu-request-saturation)

1.254

Resource

CPU-request saturation on cluster

CPU-request saturation exceeds the specified threshold.

10 minutes

Node CPU requests / Node CPU allocatable

Kubernetes Classic, Kubernetes app

[Detect cluster memory-request saturation](#detect-cluster-memory-request-saturation)

1.254

Resource

Memory-request saturation on cluster

Memory-request saturation exceeds the specified threshold.

10 minutes

Node memory requests / Node memory allocatable

Kubernetes Classic, Kubernetes app

[Detect cluster pod-saturation](#detect-cluster-pod-saturation)

1.258

Resource

Pod saturation on cluster

Cluster pod-saturation exceeds the specified threshold.

10 minutes

Sum of ready pods / Sum of allocatable pods

Kubernetes Classic, Kubernetes app

[Detect cluster readiness issues](#detect-cluster-readiness-issues)

1.254

Availability

Cluster not ready

Readyz endpoint indicates that this cluster is not ready.

10 minutes

Cluster readyz metric

Kubernetes Classic, Kubernetes app

[Detect monitoring issues](#detect-monitoring-issues)

1.258

Availability

Monitoring not available

Dynatrace API monitoring is not available.

10 minutes

Kubernetes Classic, Kubernetes app

Cluster metric and DQL expressions

#### Detect cluster CPU-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_cpu:splitBy():sum/builtin:kubernetes.node.cpu_allocatable:splitBy():sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_cpu, rollup: avg), o2=sum(dt.kubernetes.node.cpu_allocatable, rollup: avg)}, by: {}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect cluster memory-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_memory:splitBy():sum/builtin:kubernetes.node.memory_allocatable:splitBy():sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_memory, rollup: avg), o2=sum(dt.kubernetes.node.memory_allocatable, rollup: avg)}, by: {}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect cluster pod-saturation

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.node.pods:filter(and(eq(pod_condition,Ready))):splitBy():sum/builtin:kubernetes.node.pods_allocatable:splitBy():sum):default(0.0)*100.0` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), nonempty:true, filter: {((pod_condition=="Ready"))}, by: {}| join [timeseries operand=sum(dt.kubernetes.node.pods_allocatable, rollup: avg), nonempty:true, by: {}], on: {interval}, fields: {o2=operand}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect cluster readiness issues

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.cluster.readyz:splitBy():sum` |
| DQL | `timeseries {sum(dt.kubernetes.cluster.readyz, rollup: avg)}, by: {}` |

#### Detect monitoring issues

| Type | Expression |
| --- | --- |
| Metric expression | `(no metric expression)` |
| DQL | `(no DQL)` |

Default alerts for new tenants

Alert

Setting

Value

Readiness Issues

sample period in minutes

3

Readiness Issues

observation period in minutes

5

Monitoring Issues

sample period in minutes

15

Monitoring Issues

observation period in minutes

30

### Namespace alerts

Alert name

Dynatrace version

Problem type

Problem title

Problem description

De-alerts after

Calculation

Supported in

[Detect namespace CPU-limit quota saturation](#detect-namespace-cpu-limit-quota-saturation)

1.254

Resource

CPU-limit quota saturation

CPU-limit quota saturation exceeds the specified threshold.

10 minutes

Sum of resource quota CPU used / Sum of resource quota CPU limits

Kubernetes Classic, Kubernetes app

[Detect namespace CPU-request quota saturation](#detect-namespace-cpu-request-quota-saturation)

1.254

Resource

CPU-request quota saturation

CPU-request quota saturation exceeds the specified threshold.

10 minutes

Sum of resource quota CPU used / Sum of resource quota CPU requests

Kubernetes Classic, Kubernetes app

[Detect namespace memory-limit quota saturation](#detect-namespace-memory-limit-quota-saturation)

1.254

Resource

Memory-limit quota saturation

Memory-limit quota saturation exceeds the specified threshold.

10 minutes

Sum of resource quota memory used / Sum of resource quota memory limits

Kubernetes Classic, Kubernetes app

[Detect namespace memory-request quota saturation](#detect-namespace-memory-request-quota-saturation)

1.254

Resource

Memory-request quota saturation

Memory-request quota saturation exceeds the specified threshold.

10 minutes

Sum of resource quota memory used / Sum of resource quota memory requests

Kubernetes Classic, Kubernetes app

[Detect namespace pod quota saturation](#detect-namespace-pod-quota-saturation)

1.254

Resource

Pod quota saturation

Pod quota saturation exceeds the specified threshold.

10 minutes

Sum of resource quota pods used / Sum of resource quota pods limit

Kubernetes Classic, Kubernetes app

Namespace metric and DQL expressions

#### Detect namespace CPU-limit quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.limits_cpu_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.limits_cpu:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.limits_cpu_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.limits_cpu, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace CPU-request quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.requests_cpu_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.requests_cpu:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.requests_cpu_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.requests_cpu, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace memory-limit quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.limits_memory_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.limits_memory:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.limits_memory_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.limits_memory, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace memory-request quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.requests_memory_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.requests_memory:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.requests_memory_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.requests_memory, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect namespace pod quota saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.resourcequota.pods_used:splitBy(k8s.namespace.name):sum/builtin:kubernetes.resourcequota.pods:splitBy(k8s.namespace.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.resourcequota.pods_used, rollup: avg), o2=sum(dt.kubernetes.resourcequota.pods, rollup: avg)}, by: {k8s.namespace.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

### Node alerts

Alert name

Dynatrace version

Problem type

Problem title

Problem description

De-alerts after

Calculation

Supported in

[Detect node CPU-request saturation](#detect-node-cpu-request-saturation)

1.254

Resource

CPU-request saturation on node

CPU-request saturation exceeds the specified threshold.

10 minutes

Sum of node CPU requests / Sum of node CPU allocatable

Kubernetes Classic, Kubernetes app

[Detect node memory-request saturation](#detect-node-memory-request-saturation)

1.254

Resource

Memory-request saturation on node

Memory-request saturation exceeds the specified threshold.

10 minutes

Sum of node memory requests / Sum of node memory allocatable

Kubernetes Classic, Kubernetes app

[Detect node pod-saturation](#detect-node-pod-saturation)

1.254

Resource

Pod saturation on node

Pod saturation exceeds the specified threshold.

10 minutes

Sum of running pods on node / Node pod limit

Kubernetes Classic, Kubernetes app

[Detect node readiness issues](#detect-node-readiness-issues)

1.254

Availability

Node not ready

Node is not ready.

10 minutes

Node condition metric filtered by 'not ready'

Kubernetes Classic, Kubernetes app

[Detect problematic node conditions](#detect-problematic-node-conditions)

1.264

Error

Problematic node condition

Node has one or more problematic conditions out of the following: `ContainerRuntimeProblem`, `ContainerRuntimeUnhealthy`, `CorruptDockerOverlay2`, `DiskPressure`, `FilesystemCorruptionProblem`, `FrequentContainerdRestart`, `FrequentDockerRestart`, `FrequentGcfsSnapshotterRestart`, `FrequentGcfsdRestart`, `FrequentKubeletRestart`, `FrequentUnregisterNetDevice`, `GcfsSnapshotterMissingLayer`, `GcfsSnapshotterUnhealthy`, `GcfsdUnhealthy`, `KernelDeadlock`, `KubeletProblem`, `KubeletUnhealthy`, `MemoryPressure`, `NetworkUnavailable`, `OutOfDisk`, `PIDPressure`, `ReadonlyFilesystem`

10 minutes

Nodes condition metric

Kubernetes Classic, Kubernetes app

Node metric and DQL expressions

#### Detect node CPU-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_cpu:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum/builtin:kubernetes.node.cpu_allocatable:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_cpu, rollup: avg), o2=sum(dt.kubernetes.node.cpu_allocatable, rollup: avg)}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect node memory-request saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.requests_memory:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum/builtin:kubernetes.node.memory_allocatable:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.requests_memory, rollup: avg), o2=sum(dt.kubernetes.node.memory_allocatable, rollup: avg)}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect node pod-saturation

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.pods:filter(and(eq(pod_phase,Running))):splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum/builtin:kubernetes.node.pods_allocatable:splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum*100.0` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), nonempty:true, filter: {((pod_phase=="Running"))}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}| join [timeseries operand=sum(dt.kubernetes.node.pods_allocatable, rollup: avg), nonempty:true, by: {dt.kubernetes.node.system_uuid,k8s.node.name}], on: {interval}, fields: {o2=operand}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect node readiness issues

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.conditions:filter(and(eq(node_condition,Ready),ne(condition_status,True))):splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.node.conditions, rollup: avg)}, filter: {((node_condition=="Ready")AND(condition_status!=true))}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}` |

#### Detect problematic node conditions

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.node.conditions:filter(and(or(eq(node_condition,ContainerRuntimeProblem),eq(node_condition,ContainerRuntimeUnhealthy),eq(node_condition,CorruptDockerOverlay2),eq(node_condition,DiskPressure),eq(node_condition,FilesystemCorruptionProblem),eq(node_condition,FrequentContainerdRestart),eq(node_condition,FrequentDockerRestart),eq(node_condition,FrequentGcfsSnapshotterRestart),eq(node_condition,FrequentGcfsdRestart),eq(node_condition,FrequentKubeletRestart),eq(node_condition,FrequentUnregisterNetDevice),eq(node_condition,GcfsSnapshotterMissingLayer),eq(node_condition,GcfsSnapshotterUnhealthy),eq(node_condition,GcfsdUnhealthy),eq(node_condition,KernelDeadlock),eq(node_condition,KubeletProblem),eq(node_condition,KubeletUnhealthy),eq(node_condition,MemoryPressure),eq(node_condition,NetworkUnavailable),eq(node_condition,OutOfDisk),eq(node_condition,PIDPressure),eq(node_condition,ReadonlyFilesystem)),eq(condition_status,True))):splitBy(dt.kubernetes.node.system_uuid,k8s.node.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.node.conditions, rollup: avg)}, filter: {(((node_condition=="ContainerRuntimeProblem")OR(node_condition=="ContainerRuntimeUnhealthy")OR(node_condition=="CorruptDockerOverlay2")OR(node_condition=="DiskPressure")OR(node_condition=="FilesystemCorruptionProblem")OR(node_condition=="FrequentContainerdRestart")OR(node_condition=="FrequentDockerRestart")OR(node_condition=="FrequentGcfsSnapshotterRestart")OR(node_condition=="FrequentGcfsdRestart")OR(node_condition=="FrequentKubeletRestart")OR(node_condition=="FrequentUnregisterNetDevice")OR(node_condition=="GcfsSnapshotterMissingLayer")OR(node_condition=="GcfsSnapshotterUnhealthy")OR(node_condition=="GcfsdUnhealthy")OR(node_condition=="KernelDeadlock")OR(node_condition=="KubeletProblem")OR(node_condition=="KubeletUnhealthy")OR(node_condition=="MemoryPressure")OR(node_condition=="NetworkUnavailable")OR(node_condition=="OutOfDisk")OR(node_condition=="PIDPressure")OR(node_condition=="ReadonlyFilesystem"))AND(condition_status==true))}, by: {dt.kubernetes.node.system_uuid,k8s.node.name}` |

Default alerts for new tenants

Alert

Setting

Value

Readiness Issues

Readiness Issues

sample period in minutes

3

observation period in minutes

5

Node Problematic Condition

Node Problematic Condition

sample period in minutes

3

observation period in minutes

5

### Persistent volume claims alerts

Alert name

Dynatrace version

Problem type

Problem title

Problem description

De-alerts after

Calculation

Supported in

[Detect low disk space (%)](#detect-low-disk-space)

1.262

Resource

Kubernetes PVC: Low disk space %

Available disk space for a persistent volume claim is below the threshold.

10 minutes

Volume stats available bytes / Volume stats capacity bytes

Kubernetes Classic, Kubernetes app

[Detect low disk space (MiB)](#detect-low-disk-space-mb)

1.262

Resource

Kubernetes PVC: Low disk space

Available disk space for a persistent volume claim is below the threshold.

10 minutes

Kubelet volume stats available bytes metric

Kubernetes Classic, Kubernetes app

Persistent volume claims metric and DQL expressions

#### Detect low disk space (%)

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.persistentvolumeclaim.available:splitBy(k8s.namespace.name,k8s.persistent_volume_claim.name):avg/builtin:kubernetes.persistentvolumeclaim.capacity:splitBy(k8s.namespace.name,k8s.persistent_volume_claim.name):avg*100.0` |
| DQL | `timeseries {o1=avg(dt.kubernetes.persistentvolumeclaim.available), o2=avg(dt.kubernetes.persistentvolumeclaim.capacity)}, by: {k8s.namespace.name,k8s.persistent_volume_claim.name}| fieldsAdd result=o1[]/o2[]* 100.0| fieldsRemove {o1,o2}` |

#### Detect low disk space (MiB)

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.persistentvolumeclaim.available:splitBy(k8s.namespace.name,k8s.persistent_volume_claim.name):avg` |
| DQL | `timeseries {avg(dt.kubernetes.persistentvolumeclaim.available)}, by: {k8s.namespace.name,k8s.persistent_volume_claim.name}` |

### Workload alerts

Alert name

Dynatrace version

Problem type

Problem title

Problem description

De-alerts after

Calculation

Supported in

[Detect CPU usage saturation](#detect-cpu-usage-saturation)

1.264

Resource

CPU usage close to limits

The CPU usage exceeds the threshold in terms of the defined CPU limit.

10 minutes

Sum of workload CPU usage / Sum of workload CPU limits

Kubernetes Classic, Kubernetes app

[Detect container restarts](#detect-container-restarts)

1.254

Error

Container restarts

Observed container restarts exceed the specified threshold.

15 minutes

Container restarts metric

Kubernetes Classic, Kubernetes app

[Detect high CPU throttling](#detect-high-cpu-throttling)

1.264

Resource

High CPU throttling

The CPU throttling to limits ratio exceeds the specified threshold.

10 minutes

Sum of workload CPU throttled / Sum of workload CPU limits

Kubernetes Classic, Kubernetes app

[Detect job failure events](#detect-job-failure-events)

1.268

Error

Job failure event

Events with reason 'BackoffLimitExceeded', 'DeadlineExceeded', or 'PodFailurePolicy' have been detected.

60 minutes

Event metric filtered by reason and workload kind

Kubernetes Classic, Kubernetes app

[Detect memory usage saturation](#detect-memory-usage-saturation)

1.264

Resource

Memory usage close to limits

The memory usage (working set memory) exceeds the threshold in terms of the defined memory limit.

10 minutes

Sum of workload working set memory / Sum of workload memory limits

Kubernetes Classic, Kubernetes app

[Detect out-of-memory kills](#detect-out-of-memory-kills)

1.268

Error

Out-of-memory kills

Out-of-memory kills have been observed for pods of this workload.

15 minutes

Out-of-memory kills metric

Kubernetes Classic, Kubernetes app

[Detect pod backoff events](#detect-pod-backoff-events)

1.268

Error

Backoff event

Events with reason 'BackOff' have been detected for pods of this workload. Check for pods with status 'ImagePullBackOff' or 'CrashLoopBackOff'.

15 minutes

Event metric filtered by reason

Kubernetes Classic, Kubernetes app

[Detect pod eviction events](#detect-pod-eviction-events)

1.268

Error

Pod eviction event

Events with reason 'Evicted' have been detected for pods of this workload.

60 minutes

Event metric filtered by reason

Kubernetes Classic, Kubernetes app

[Detect pod preemption events](#detect-pod-preemption-events)

1.268

Error

Preemption event

Events with reasons 'Preempted' or 'Preempting' have been detected for pods of this workload.

60 minutes

Event metric filtered by reason

Kubernetes Classic, Kubernetes app

[Detect pods stuck in pending](#detect-pods-stuck-in-pending)

1.254

Resource

Pods stuck in pending

Workload has pending pods.

10 minutes

Pods metric filtered by phase 'Pending'

Kubernetes Classic, Kubernetes app

[Detect pods stuck in terminating](#detect-pods-stuck-in-terminating)

1.260

Resource

Pods stuck in terminating

Workload has pods stuck in terminating.

10 minutes

Pods metric filtered by status 'Terminating'

Kubernetes Classic, Kubernetes app

[Detect stuck deployments](#detect-stuck-deployments)

1.260

Error

Deployment stuck

Deployment is stuck and therefore is no longer progressing.

10 minutes

Workload condition metric filtered by 'not progressing'

Kubernetes Classic, Kubernetes app

[Detect workloads with non-ready pods](#detect-workloads-with-non-ready-pods)

1.258

Error

Not all pods ready

Workload has pods that are not ready.

10 minutes

Sum of all pending or running pods â Sum of ready pending or running pods. Pods of Jobs and CronJob are excluded.

Kubernetes Classic, Kubernetes app

[Detect workloads without ready pods](#detect-workloads-without-ready-pods)

1.254

Error

No pod ready

Workload does not have any ready pods.

10 minutes

Sum of all pending or running pods â Sum of non-ready pending or running pods. Pods of Jobs and CronJob are excluded.

Kubernetes Classic, Kubernetes app

Workload metric and DQL expressions

#### Detect CPU usage saturation

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.workload.cpu_usage:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum/builtin:kubernetes.workload.limits_cpu:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum):default(0.0)*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.cpu_usage, rollup: avg), o2=sum(dt.kubernetes.container.limits_cpu, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect container restarts

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.container.restarts:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.container.restarts, default:0.0, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect high CPU throttling

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.workload.cpu_throttled:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum/builtin:kubernetes.workload.limits_cpu:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum):default(0.0)*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.cpu_throttled, rollup: avg), o2=sum(dt.kubernetes.container.limits_cpu, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect job failure events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(and(or(eq(k8s.event.reason,BackoffLimitExceeded),eq(k8s.event.reason,DeadlineExceeded),eq(k8s.event.reason,PodFailurePolicy)),or(eq(k8s.workload.kind,job),eq(k8s.workload.kind,cronjob)))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {(((k8s.event.reason=="BackoffLimitExceeded")OR(k8s.event.reason=="DeadlineExceeded")OR(k8s.event.reason=="PodFailurePolicy"))AND((k8s.workload.kind=="job")OR(k8s.workload.kind=="cronjob")))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect memory usage saturation

| Type | Expression |
| --- | --- |
| Metric expression | `(builtin:kubernetes.workload.memory_working_set:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum/builtin:kubernetes.workload.limits_memory:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum):default(0.0)*100.0` |
| DQL | `timeseries {o1=sum(dt.kubernetes.container.memory_working_set, rollup: avg), o2=sum(dt.kubernetes.container.limits_memory, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| fieldsAdd result=if(isNull(o1[]/o2[]), 0.0, else: o1[]/o2[])* 100.0| fieldsRemove {o1,o2}` |

#### Detect out-of-memory kills

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.container.oom_kills:splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.container.oom_kills, default:0.0, rollup: avg)}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pod backoff events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(and(eq(k8s.event.reason,BackOff))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {((k8s.event.reason=="BackOff"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pod eviction events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(and(eq(k8s.event.reason,Evicted))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {((k8s.event.reason=="Evicted"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pod preemption events

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.events:filter(or(eq(k8s.event.reason,Preempted),eq(k8s.event.reason,Preempting))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries {sum(dt.kubernetes.events, default:0.0, rollup: avg)}, filter: {((k8s.event.reason=="Preempted")OR(k8s.event.reason=="Preempting"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pods stuck in pending

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(eq(pod_phase,Pending))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.pods, rollup: avg)}, filter: {((pod_phase=="Pending"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect pods stuck in terminating

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(eq(pod_status,Terminating))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.pods, rollup: avg)}, filter: {((pod_status=="Terminating"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect stuck deployments

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.workload.conditions:filter(and(eq(workload_condition,Progressing),eq(condition_status,False))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum` |
| DQL | `timeseries {sum(dt.kubernetes.workload.conditions, rollup: avg)}, filter: {((workload_condition=="Progressing")AND(condition_status==false))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}` |

#### Detect workloads with non-ready pods

The following expression returns the number of pending and running pods in the non-ready condition. Pods of Jobs and CronJobs are excluded.

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob),ne(pod_status,Terminating))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum-builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob),eq(pod_condition,Ready),ne(pod_status,Terminating))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob")AND(pod_status!="Terminating"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| join [timeseries operand=sum(dt.kubernetes.pods, default:0.0, rollup: avg), nonempty:true, filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob")AND(pod_condition=="Ready")AND(pod_status!="Terminating"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}], on: {interval}, fields: {o2=operand}| fieldsAdd result=o1[]-o2[]| fieldsRemove {o1,o2}` |

#### Detect workloads without ready pods

The following expression returns the number of pending and running pods in the ready condition. Pods of Jobs and CronJobs are excluded.

| Type | Expression |
| --- | --- |
| Metric expression | `builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum-builtin:kubernetes.pods:filter(and(ne(pod_phase,Failed),ne(pod_phase,Succeeded),ne(k8s.workload.kind,job),ne(k8s.workload.kind,cronjob),ne(pod_condition,Ready))):splitBy(k8s.namespace.name,k8s.workload.kind,k8s.workload.name):sum:default(0.0)` |
| DQL | `timeseries o1=sum(dt.kubernetes.pods, rollup: avg), filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}| join [timeseries operand=sum(dt.kubernetes.pods, default:0.0, rollup: avg), nonempty:true, filter: {((pod_phase!="Failed")AND(pod_phase!="Succeeded")AND(k8s.workload.kind!="job")AND(k8s.workload.kind!="cronjob")AND(pod_condition!="Ready"))}, by: {k8s.namespace.name,k8s.workload.kind,k8s.workload.name}], on: {interval}, fields: {o2=operand}| fieldsAdd result=o1[]-o2[]| fieldsRemove {o1,o2}` |

#### Default alerts for new tenants

Alert

Setting

Value

Container Restarts

threshold

1

Container Restarts

sample period in minutes

3

Container Restarts

observation period in minutes

5

Deployment Stuck

sample period in minutes

3

Deployment Stuck

observation period in minutes

5

Pending Pods

threshold

1

Pending Pods

sample period in minutes

10

Pending Pods

observation period in minutes

15

Pod Stuck In Terminating

sample period in minutes

10

Pod Stuck In Terminating

observation period in minutes

15

Workload Without Ready Pods

sample period in minutes

10

Workload Without Ready Pods

observation period in minutes

15

Oom Kills

alert

always

Job Failure Events

alert

always

Pod Backoff Events

alert

always

Pod Eviction Events

alert

always

Pod Preemption Events

alert

always

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: default-monitoring-settings.md


---
title: Global default monitoring settings for Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/default-monitoring-settings
scraped: 2026-02-17T21:16:40.915637
---

# Global default monitoring settings for Kubernetes/OpenShift

# Global default monitoring settings for Kubernetes/OpenShift

* 2-min read
* Updated on Jun 15, 2023

Dynatrace version 1.270+

You can configure default monitoring settings for Kubernetes/OpenShift clusters. These default values are used for all new clusters unless monitoring settings are specified during their creation.

## Configuration via web UI

The monitoring settings can be configured either per cluster or for the whole environment.

### Configure environment-level settings

To configure the default settings for the whole environment

1. Go to **Settings** and select **Cloud and virtualization** > **Kubernetes**.
2. On the **Monitoring settings** page, change settings as needed.
3. Select **Save changes**.

![Kubernetes monitoring settings on tenant](https://dt-cdn.net/images/tenant-monitoring-settings-1425-ab644e8cd0.png)

These environment-level settings will be used as default values for all clusters that do not explicitly override them.

### List overriding clusters

To see which clusters are currently overriding these settings

1. On the environment-level **Monitoring settings** page, select **More** (**â¦**) > **Hierarchy and overrides** in the upper-right corner.
2. Review the **Hierarchy and overrides** table.

For details on the settings hierarchy, see [Settings documentation](/docs/manage/settings/settings-20#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework").

![Kubernetes monitoring settings overrides](https://dt-cdn.net/images/tenant-monitoring-settings-overrides-2058-db713cf077.png)

### Remove cluster-level overrides

If you want to remove an override from a specific cluster

1. In the **Hierarchy and overrides** table, select the name of the cluster.

   This opens the **Monitoring settings** page for the selected cluster. The message "These settings are overriding Environment settings" is displayed.
2. In the message box, select **Remove override**. If no override is set, the values set on the environment will be used.

![Kubernetes monitoring settings on cluster](https://dt-cdn.net/images/cluster-monitoring-settings-override-929-a45970ae1e.png)

## Configuration via API

You can also configure monitoring settings via the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") using the [Monitoring settings schema](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.").

To change the default values for the environment, set the `scope` property in the request to `environment`.

To use the default settings when connecting a cluster, the [Connection settings schema](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") should be version `3.0.0` or higher. Using older versions will automatically override the default monitoring settings for this cluster.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: leverage-tags-defined-in-kubernetes-deployments.md


---
title: Organize Kubernetes/OpenShift deployments by tags
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments
scraped: 2026-02-17T21:16:47.385294
---

# Organize Kubernetes/OpenShift deployments by tags

# Organize Kubernetes/OpenShift deployments by tags

* How-to guide
* 6-min read
* Updated on Nov 09, 2023

Dynatrace automatically derives tags from your Kubernetes/OpenShift labels. This enables you to automatically organize and filter all your monitored Kubernetes/OpenShift application components.

## Recommendations

We recommend that you define additional metadata at the deployed system. For Kubernetes-based applications, you can simply use [Kubernetes annotationsï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/). Dynatrace automatically detects and retrieves all Kubernetes and OpenShift annotations for pods that are monitored with a OneAgent code module. This enables you to use [automated tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), based on existing or custom metadata, to define your filter sets for charts, alerting, and more. These tags and rules can be changed and adapted any time and will apply almost immediately without any change to the monitored environment or applications.

In Dynatrace, you can specify [entity ownership](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") for different Kubernetes objects such as Deployments, Pods, Services, or namespaces. We recommend providing ownership information via Kubernetes labels or annotations (you can use either labels or annotations to attach metadata to Kubernetes objects). This ensures that Kubernetes objects have adequate ownership coverage, which is especially important for short-lived entities like Pods. See [Assign ownership teams to monitored entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") for more on the correct format and examples of providing ownership information in key-value pairs in the deployment specification file.

We recommend defining ownership for the Deployment and all other objects for which you want ownership coverage. See also [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage"). You can assign more than one team to a Kubernetes object, provided that the keys in the key-value pairs are unique.

While you can also use tags (manual, automated, and via API) to apply ownership information to Kubernetes objects, this approach has its limitationsâread more in [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

## Automatic detection of Kubernetes properties and annotations

Dynatrace detects Kubernetes properties and annotations. Such [properties and annotations](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") can be used when specifying [automated rule-based tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

Additionally Dynatrace detects the following properties that can be used for [automated rule-based tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") and [property-based process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection#detection-rules "Ways to customize process-group detection").

* Kubernetes base pod name: User-provided name of the pod the container belongs to.
* Kubernetes container: Name of the container that runs the process.
* Kubernetes full pod name: Full name of the pod the container belongs to.
* Kubernetes namespace: Namespace to which the containerized process is assigned.
* Kubernetes pod UID: Unique ID of the related pod.

## Leverage Kubernetes labels in Dynatrace

Kubernetes-based tags are searchable via Dynatrace search. This allows you to easily find and inspect the monitoring results of related processes running in your Kubernetes or OpenShift environment. You can also leverage Kubernetes tags to set up fine-grained [problem alerting profiles](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles."). Kubernetes tags also integrate perfectly with [Dynatrace filters](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.").

## Import your labels and annotations

Requirements

For OneAgent to detect Kubernetes annotations and properties, make sure that

* Pods are monitored with a code module
* `automountServiceAccountToken: false` isn't set in your pod's `spec`

Kubernetes

OpenShift

You can specify [Kubernetes labelsï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) in the [deployment definitionï»¿](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment) of your application or you can update the labels of your Kubernetes resources using the command `kubectl label`.

You can specify [OpenShift labelsï»¿](https://docs.openshift.com/enterprise/3.0/architecture/core_concepts/pods_and_services.html#labels) in the [Pod object definitionï»¿](https://docs.openshift.com/container-platform/3.10/architecture/core_concepts/pods_and_services.html) of your application or you can update the labels of your OpenShift resources using the command [oc labelï»¿](https://docs.openshift.com/enterprise/3.0/cli_reference/basic_cli_operations.html#application-modification-cli-operations).

Dynatrace automatically detects all labels attached to pods at application deployment time. All you have to do is grant sufficient privileges to the pods that allow for reading the metadata from the Kubernetes REST API endpoint. This way, the OneAgent code modules can read these labels directly from the pod.

### Grant viewer role to service accounts

Kubernetes

OpenShift

In Kubernetes, every pod is associated with a service account which is used to authenticate the pod's requests to the Kubernetes API. If not otherwise specified the pod uses the `default` service account of its namespace.

Every namespace has its own set of service accounts and thus also its own namespace-scoped `default` service account. The labels of each pod for which the service account has view permissions will be imported into Dynatrace automatically.

The following steps show you how to add view privileges to the `default` service account in the `namespace1` namespace. You need to repeat these steps for all service accounts and namespaces you want to enable for Dynatrace.

Create the following `Role` and `RoleBinding`, which allow the `default` service account to view the necessary metadata about your namespace `namespace1` via the Kubernetes REST API:

```
# dynatrace-oneagent-metadata-viewer.yaml



kind: Role



apiVersion: rbac.authorization.k8s.io/v1



metadata:



namespace: namespace1



name: dynatrace-oneagent-metadata-viewer



rules:



- apiGroups: [""]



resources: ["pods"]



verbs: ["get"]



---



kind: RoleBinding



apiVersion: rbac.authorization.k8s.io/v1



metadata:



name: dynatrace-oneagent-metadata-viewer-binding



namespace: namespace1



subjects:



- kind: ServiceAccount



name: default



apiGroup: ""



roleRef:



kind: Role



name: dynatrace-oneagent-metadata-viewer



apiGroup: ""
```

```
kubectl -n namespace1 create -f dynatrace-oneagent-metadata-viewer.yaml
```

In OpenShift, every pod is associated with a service account that's used to authenticate the pod's requests to the Kubernetes API. If not otherwise specified, the pod uses the `default` service account of its OpenShift project.

Each OpenShift project has its own set of service accounts and thus also its own project-scoped `default` service account. The labels of every pod whose service account has view permissions will be imported to Dynatrace automatically.

The following steps show you how to add view privileges to the `default` service account in the `project1` project. You need to repeat these steps for all service accounts and projects you want to enable for Dynatrace.

Create the following `Role`, which will allow a service account to view the necessary metadata about your namespace `project1` via the Kubernetes REST API:

```
# dynatrace-oneagent-metadata-viewer.yaml



kind: Role



apiVersion: rbac.authorization.k8s.io/v1



metadata:



namespace: project1



name: dynatrace-oneagent-metadata-viewer



rules:



- apiGroups: [""]



resources: ["pods"]



verbs: ["get"]
```

```
oc -n project1 create -f dynatrace-oneagent-metadata-viewer.yaml
```

Bind the `Role` to the `default` service account for the `Role` to take effect:

```
oc -n project1 policy add-role-to-user dynatrace-oneagent-metadata-viewer --role-namespace="project1" -z default
```

Alternatively, OpenShift also allows you to bind the `Role` to all service accounts in a project.

```
oc -n project1 policy add-role-to-group dynatrace-oneagent-metadata-viewer --role-namespace="project1" system:serviceaccounts:project1
```

As a result, Kubernetes [processes](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") monitored in your Dynatrace environment will have Kubernetes labels attached as Kubernetes tags. For namespaces, pods, and workloads, Kubernetes tags are not evaluated.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Assign ownership teams to monitored entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.")


---


## Source: monitor-cluster-utilization-kubernetes.md


---
title: Monitor Kubernetes/OpenShift cluster utilization
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes
scraped: 2026-02-06T16:26:39.711082
---

# Monitor Kubernetes/OpenShift cluster utilization

# Monitor Kubernetes/OpenShift cluster utilization

* 2-min read
* Updated on Apr 29, 2024

Dynatrace version 1.232+

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

## Kubernetes page

After enabling access to the Kubernetes overview page for a specific Kubernetes cluster, the specific cluster will appear on the **Kubernetes** page. The Kubernetes page provides an overview of all Kubernetes clusters showing monitoring data like the clustersâ sizing and utilization.  
To access this page, go to **Kubernetes** (previous Dynatrace) or ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.

![Cluster utilization](https://dt-cdn.net/images/cluster-list-3710-4c21475cfb.png)

## Utilization of cluster resources over time

As Kubernetes can run any containerized workloads and allow for horizontal pod autoscaling, the actual utilization of cluster resources will likely be very volatile. That is why Dynatrace offers a single pane of glass for the most important utilization and performance metrics on a cluster level. These metrics are:

* Percentage of CPU resources used out of the total allocatable CPU resources.
* Percentage of CPU resources requested/limited out of the total allocatable CPU resources.
* Percentage of memory resources requested/used out of the total allocatable memory resources.
* Percentage of memory resources limited out of the total allocatable memory resources.
* Total CPU/Memory usage.
* CPU/Memory resources requested/limited.
* CPU/Memory resources allocatable to pods.
* Total number of pods running/allocatable on cluster nodes.
* Number of times containers have been restarted.

![Monitor k8](https://dt-cdn.net/images/cluster-1-3700-55f0edc5fe.png)

## View available resources on your Kubernetes nodes

You can get detailed insights of the Kubernetes node metrics on a per-node level to understand how individual nodes are utilized. The **Node analysis** page also provides information about how much workload can still be deployed on nodes.

![View resource k8](https://dt-cdn.net/images/cluster-2-3700-209833d1e0.png)

By selecting a specific node, you can access the host details at the top of the node overview page. From there, you can delve into code-level insights on currently deployed containers, along with relevant cloud-specific host properties and Kubernetes node labels.

![View host k8](https://dt-cdn.net/images/cluster-3-3700-0d7e54a3e8.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-events-kubernetes.md


---
title: Monitor Kubernetes/OpenShift events
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes
scraped: 2026-02-17T21:16:44.645210
---

# Monitor Kubernetes/OpenShift events

# Monitor Kubernetes/OpenShift events

* 8-min read
* Updated on Jul 05, 2024

## Prerequisites

* ActiveGate version 1.265+
* In Dynatrace, go to **Monitoring settings** > **Kubernetes** and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.
* [Enable the latest version of Dynatrace log monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")

## Kubernetes events monitoring for analysis and alerting

For full observability into your Kubernetes events, automatic Davis analysis, and custom alerting, you need to enable Kubernetes event monitoring.

To enable event monitoring for specific Kubernetes clusters

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster and, in the **Actions** column, select **More** (**â¦**) > **Settings**.
3. On the **Monitoring Settings** tab, turn on **Monitor events**.
4. Select **Save changes**.

When you enable **Monitor events**, all events are ingested and all [important events](#important-events) are considered in the Davis root-cause detection. Alternatively, for maximum flexibility and fine-grained control over the events you want to ingest from Kubernetes, you can [filter events](#filter).

### Inferred Kubernetes events

Even if **Monitor events** is disabled, the so-called *inferred* Kubernetes events are still ingested. These inferred events aren't native Kubernetes events but are created by ActiveGate based on the information from the Kubernetes API server.

Examples of inferred events:

* cgroup OOM kill events
* Workload specification changes (replicas, images, environment variables, resources, probes) for

  + Deployments
  + StatefulSets
  + DaemonSets

These events aren't billed and are relevant for Davis root-cause analysis.

### View events

After enabling the Kubernetes event monitoring, you can view and analyze events from the Kubernetes cluster.

On your Kubernetes cluster details page, go to **Events**.

You can filter events by:

* Timeframe: select one of the timeframes in the chart to view open events for that timeframe
* Specific events: select one of the group labels below the chart to view specific events

For more information about an event, select **Details** for the event.

Kubernetes events are associated with Kubernetes entities. An event is displayed on the respective entity page and on related entity pages. For example, pod events are displayed on the cluster, namespace, workload, and pod details page.

You can also view events on the **Log viewer** page (in Dynatrace, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**), which allows for advanced search and filtering.

If the environment is platform enabled the events are stored in Grail. The following DQL query can be used as a template to query for specific events in [**Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [**Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

```
fetch events



| filter event.provider == "KUBERNETES_EVENT"
```

[Inferred Kubernetes events](#inferred) are not shown in **Log viewer**. They are directly ingested as events.

## Filter events to be monitored

Filtering is turned off by default, which means that all events are ingested. To set up monitoring only for certain events

1. Turn on **Filter events**.

   If you don't see the **Filter events** switch, make sure that **Monitor events** is turned on first.
2. [Set up multiple field selectors for every Kubernetes environment](#set-up-event-field-selectors).
3. Optional [Have Davis perform root cause analysis on all important Kubernetes events](#important-events).
4. Select **Save changes**.

### Set up event field selectors

Filtering follows the [Kubernetes-established syntax of field selectorsï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/), so events can be chosen based on event resource fields such as `source.component`, `type`, or `involvedObject`.

A field selector expression must meet the following requirements:

* It must conform to the following regular expression: `^[\w\.]{1,1024}((=){1,2}|(!=))[^,!=]{0,256}(,[\w\.]{1,1024}?((=){1,2}|(!=))[^,!=]{0,256}){0,9}$`.
* It can have up to 10 selectors separated by commas. Events matching all comma-separated selectors will be ingested. The logical operator is `AND`.
* A selector consists of three parts:

  + **Key:** Contains up to 1,024 alphanumerical characters, underscores, and dots.
  + **Operator:** Is either `=` , `==` or `!=`.
  + Optional **Value:** Can contain up to 256 characters. Cannot contain exclamation marks, equal signs, or commas.

For example,

* If you set a field selector expression to `involvedObject.namespace=hipster-shop,type=Warning`, the expression will store all the events related to the namespace `hipster-shop` that are of type `Warning`.
* If you separate the expression into two independent field selectors, you'll get all events for namespace `hipster-shop` and all events of type `Warning`. The logical operator in this case is `OR`.

**Example event field selectors:**

| **Event field selectors** | **Field selector expression** |
| --- | --- |
| Get all `Node` events | `involvedObject.kind=Node` |
| Get all `Warning` events | `type=Warning` |
| Get all `Pod` events | `involvedObject.kind=Pod` |
| Get all events of objects related to a specific namespace | `involvedObject.namespace=<your_namespace>` (Make sure to replace `<your_namespace>` with the name of your own namespace) |
| Get all `BackOff` events for pods across all namespaces | `reason=BackOff` |
| Get all events with non-empty type field | `type!=` |
| Get all nginx container events | `involvedObject.fieldPath==spec.containers{nginx}` |

To set up event field selectors, select one of the options below:

Via web UI

Via CLI

Via API

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster and, in the **Actions** column, select **More** (**â¦**) > **Settings**.
3. On the **Monitoring Settings** tab

   * Turn on **Filter events**.
   * Select **Add events field selector**.
   * Enter a **Field selector name** and **Field selector expression**.
4. Select **Save changes**.

Example command:

```
kubectl get events --all-namespaces --field-selector involvedObject.namespace=hipster-shop,type=Warning
```

You can define the event field selectors via [Dynatrace API](/docs/dynatrace-api/configuration-api/k8s-credentials-api-api "Manage Kubernetes credentials via the Dynatrace configuration API.").

You can create a maximum of 20 event filter rules per Kubernetes cluster.

### Monitor important events

When problems with applications, microservices, or infrastructure are detected, Davis performs root cause analysis on all important Kubernetes events for nodes, namespaces, workloads, and pods.

A Kubernetes event is important (relevant for Davis root cause analysis) when at least one of the following two conditions is true.

* The event reason is in the predefined list of [important reasons](#important-event-reasons).
* The event type is `Warning`.

Important event reasons

`BackOff`,
`DeadlineExceeded`,
`Killing`,
`NodeNotSchedulable`,
`OutOfDisk`,
`Preempting`

By default, all these events are monitored when [**Monitor events**](#monitor-events) is turned on. If you choose to [Filter events](#filter), either predefined important events filter or custom events filters can be applied. If multiple filters are set, they are combined using a logical `OR`. The event is ingested, once a Kubernetes event matches any of the filters.

To enable monitoring of important events, when event filtering is turned on

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster and, in the **Actions** column, select **More** (**â¦**) > **Settings**.
3. On the **Monitoring Settings** tab, turn on **Include important events**.

   If you don't see the **Include important events** switch, make sure that **Monitor events** and **Filter events** are turned on first.
4. Select **Save changes**.

## Charting and alerting

Kubernetes events are made available in the **Kubernetes: Event count** (`builtin:kubernetes.events`) metric. To filter the events count metric for the relevant events, use the `k8s.event.reason` and `k8s.event.type` dimensions.

* To help you understand the distribution and development of Kubernetes events over time, use [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to create charts. You can use the charts to compare different timeframes, different entities, event filters, and the use of complex expressions.
* To trigger alerts whenever Kubernetes events occur (for example, always alert in case of an `Evicted` event), define [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") based on the **Kubernetes: Event count** metric.

## Licensing

To estimate the number of events that consume DDUs, you can query the `dsfm:active_gate.kubernetes.events.processed` metric, which provides information about the number of events that are being ingested into Dynatrace per Kubernetes cluster.

Example query for a 24-hour timeframe:

`dsfm:active_gate.kubernetes.events.processed:splitBy("dt.entity.kubernetes_cluster"):sum:auto:sort(value(sum,descending)):limit(10)`

DDU consumption applies to Kubernetes event monitoring. For details, see [DDUs for custom Davis events](/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.").

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-istio-metrics.md


---
title: Istio/Envoy proxy metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics
scraped: 2026-02-17T21:16:51.175834
---

# Istio/Envoy proxy metrics

# Istio/Envoy proxy metrics

* 1-min read
* Updated on May 08, 2023

Dynatrace version 1.255+

Istio is a platform-independent service mesh that is very popular in the Kubernetes community. Dynatrace OneAgent and ActiveGate can monitor Istio with the following observability options:

* Distributed tracing and service-level metrics: OneAgent with [code modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* Istio metrics and topology: ActiveGate
* Istio logs: OneAgent [log module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")

Alternatively, [Unified services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Define services on observability signals ingested via Trace ingest APIs.") provide agentless support for Istio service meshes.

## How it works

ActiveGate ingests Istio metrics and sends them to Dynatrace. Because Istio exposes metrics as Prometheus exporters, you just need to [provide annotations](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

Based on the labels of ingested metrics, Dynatrace also detects the Istio topology without OneAgent. This is supported with ActiveGate version 1.261+.

See [Istio Service Meshï»¿](https://www.dynatrace.com/hub/detail/istio-and-envoy-service-mesh-prometheus/) in Dynatrace Hub for details on activating the Istio extension in your environment. The recommended version is 1.1.0 or later.

## Prerequisites

### ActiveGate

* See [Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.") for ingestion prerequisites
* Topology detection: ActiveGate version 1.261+
* Sum and count extraction from histogram metrics: ActiveGate version 1.261+

### Dynatrace

* Istio metrics card on Kubernetes services, workload, and namespace pages: Dynatrace version 1.255+
* Topology (calling and called corresponding entities) on Kubernetes services, workload, and namespace pages: Dynatrace version 1.263+

Istio monitoring by OneAgent is supported for the classic full-stack, cloud-native full-stack, and application-only [deployment options](/docs/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.") since Operator version 0.11.0+. Earlier versions support classic full-stack only.

## Related topics

* [Monitor Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")


---


## Source: monitor-metrics-kubernetes.md


---
title: Monitor Kubernetes/OpenShift metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-metrics-kubernetes
scraped: 2026-02-17T21:16:42.139402
---

# Monitor Kubernetes/OpenShift metrics

# Monitor Kubernetes/OpenShift metrics

* 2-min read
* Updated on Mar 14, 2023

Dynatrace version 1.232+

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

## View Kubernetes metrics

* For details on container metrics, see [Built-in metrics - Containers/CPU](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#containers-cpu "Explore the complete list of built-in Dynatrace metrics.") and [Built-in metrics - Containers/Memory](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#containers-memory "Explore the complete list of built-in Dynatrace metrics.").

* For details on Kubernetes metrics, see [Built-in metrics - Cloud/Kubernetes](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#cloud-kubernetes "Explore the complete list of built-in Dynatrace metrics.").

![K8 dash](https://dt-cdn.net/images/2021-03-12-08-54-46-1668-d24182ddd2.png)

### Workload resource metrics

Dynatrace version 1.264+ ActiveGate version 1.263+

Workload resource metrics rely on cAdvisor, which is only available on POSIX-based Kubernetes nodes. These metrics are not available on Windows.

For clusters with more than 50 nodes or 5,000 pods, resource consumption of the ActiveGate is considerably increased.

The workload and node resource metrics feature aggregates container resource metrics (CPU usage, CPU throttling, and memory consumption) to the workload and node level. Workload and node resource metrics are based on the container metrics exposed by the Kubernetes cAdvisor. This feature does not require OneAgentâan ActiveGate with Kubernetes API monitoring turned on is sufficient.

To enable monitoring of workload and node resource metrics

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** and select the cluster name to open the Kubernetes cluster overview page.
2. In the upper-right corner, select **More** (**â¦**) > **Settings**, select **Monitoring settings**, and turn on **Monitor workload and node resource metrics**.

   Monitoring **node resource metrics** requires ActiveGate version 1.271+.
3. Optional Select **Test connection** to verify that the feature has been successfully activated.

For a list of all available metrics, see [Workload metrics](/docs/analyze-explore-automate/metrics-classic/all-metrics#workload "Explore the complete list of Dynatrace metrics.") or [Node](/docs/analyze-explore-automate/metrics-classic/all-metrics#node "Explore the complete list of Dynatrace metrics.") for node resource metrics.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-prometheus-metrics.md


---
title: Monitor Prometheus metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics
scraped: 2026-02-17T21:16:35.455838
---

# Monitor Prometheus metrics

# Monitor Prometheus metrics

* 14-min read
* Updated on Jan 29, 2026

Prometheus is an open-source monitoring and alerting toolkit which is popular in the Kubernetes community. Prometheus scrapes metrics from a number of HTTP(s) endpoints that expose metrics in the OpenMetrics format.
See the list of available [exportersï»¿](https://dt-url.net/vd03n1m) in the Prometheus documentation.

## Prometheus Metric Type Ingest

Dynatrace is able to ingest Prometheus metrics [Counter](#counter), [Gauge](#gauge), [Histogram](#histogram) and [Summary](#summary)
in Kubernetes using [Prometheus exportersï»¿](https://dt-url.net/lw02ror) and makes them available for charting, alerting and analysis.

### Counter

The Prometheus counter metric[1](#fn-1-1-def) is a monotonically increasing value typically used for measurements that can only increase or remain constant.
Dynatrace uses its [`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") metric type, which uses **delta encoding**[2](#fn-1-2-def) in order to reduce data redundancy, for data ingestion.
As such, the value displayed in Dynatrace does not reflect the actual counter value, but instead its change, or delta, over observations.

This method results in a counter metric appearing one minute delayed in contrast to a [Gauge](#gauge) metric if scraping for both metrics started simultaneously.
For details, see the [metric ingestion protocol reference](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Ingesting Counter metrics

The **delta encoding** used by the Dynatrace [`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") ingestion type means that the ingested value *does not* reflect the actual value, but the difference between measurements.

1

[Prometheus official documentation: Counterï»¿](https://dt-url.net/cd02rce)

2

Delta encoding, also known as delta-compression, stores data by computing the difference between two observations or target values. Primarily used
for seldomly changing data, the method avoids data redundancy.

### Gauge

In contrast to [Counter](#counter), the gauge metric[1](#fn-2-1-def) stores a single numerical value which can increase and decrease and is typically used for measured values such as
current memory usage or number of users online. In Dynatrace, the [`GAUGE`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") metric type will be used for data ingest.

1

[Prometheus official documentation: Gaugeï»¿](https://dt-url.net/lb22r1o)

### Histogram

Histograms[1](#fn-3-1-def) provide visual insights into the distribution and frequency of numerical data.
For a base metric name of `<basename>`, Dynatrace will ingest the data according to the
following table.

Prometheus Metric

Dynatrace Ingest Type

`<basename>_bucket{le="<upper inclusive bound>"}`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_bucket_sum`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_bucket_count`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

Additional flexibility and control is provided via the [`builtin:histogram-metrics`ï»¿](https://dt-url.net/ne02rlq) settings schema.
This schema allows to configure the ingestion of `<basename>_bucket{le="<upper inclusive bound>"}` metrics.

1

[Prometheus official documentation: Histogramï»¿](https://dt-url.net/vc02rmb)

### Summary

Like a [Histogram](#histogram), the summary metric[1](#fn-4-1-def) samples observations. In contrast to the histogram metric, a summary's buckets are
represented by Ï-quantiles where 0 â¤ Ï â¤ 1. For a base metric name of `<basename>`, Dynatrace will ingest the data according to the
following table.

Prometheus Metric

Dynatrace Ingest Type

`<basename>{quantile="<Ï>"}`

[`GAUGE`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_sum`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_count`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

1

[Prometheus official documentation: Summaryï»¿](https://dt-url.net/7g234n1).

### Unsupported

The following types are currently not supported by Dynatrace:

* info, gaugehistogram or stateset metrics
* exemplars

## Prerequisites

We recommend using an ActiveGate that is running inside the Kubernetes cluster which you want to scrape Prometheus metrics from. If the ActiveGate is running outside the monitored cluster (for example, in a virtual machine or in a different Kubernetes cluster), it won't be able to scrape any Prometheus endpoints on pods which require authentication (such as [RBAC](#rbac) or [client authentication](#client)). ActiveGates running inside the clusters will also provide performance improvements.

* In Dynatrace, go to your Kubernetes cluster monitoring settings page and enable

  + **Monitor Kubernetes namespaces, services, workloads, and pods**
  + **Monitor annotated Prometheus exporters**
* Annotated pod definitions. For details, see below.
* Verify that your network policies allow the ActiveGate to connect to the exporters.

  For example, if you deployed the ActiveGate in your Kubernetes cluster using the Dynatrace Operator and you have annotated Prometheus exporters in the namespace `online-boutique`, and you also have a network policy defined for this namespace, you need to make sure that the ActiveGate pod, located in the `dynatrace` namespace, can connect to the annotated Prometheus exporters in the `online-boutique` namespace.

## Annotate Prometheus exporter pods

Dynatrace collects metrics from any pods that are annotated with a `metrics.dynatrace.com/scrape` property set to `true` in the pod definition. This functionality applies to all pods across the entire Kubernetes cluster, regardless of whether the pod is running in a namespace that matches the Dynakube's namespace selector.

Depending on the actual exporter in a pod, you might need to set additional annotations to the pod definition in order to allow Dynatrace to properly ingest those metrics.

### Enable metrics scraping Required

Set `metrics.dynatrace.com/scrape` to `true` to enable Dynatrace to collect Prometheus metrics exposed for this pod.

### Metrics port Required

By default, Prometheus metrics are available at the first exposed TCP port of the pod. Set `metrics.dynatrace.com/port` to the respective port.

To determine the port value, see [Default port allocationsï»¿](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) for a list of common ports for known exporters.

### Path to metrics endpoint Optional

Use `metrics.dynatrace.com/path` to override the default (`/metrics`) Prometheus endpoint.

### HTTP/HTTPS Optional

Set `metrics.dynatrace.com/secure` to `true` if you want to collect metrics that are exposed by an exporter via HTTPS. The default value is `false`, because most exporters expose their metrics via HTTP.

If you want to skip verification of the TLS certificate (for example, if you use self-signed certificates), you can set the annotation
`metrics.dynatrace.com/insecure_skip_verify` to `true`. This annotation, however, is only considered when using an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### Filter metrics Optional

Use `metrics.dynatrace.com/filter` to define a filter that allows you to include (`"mode": "include"`) or exclude (`"mode": "exclude"`) a list of metrics. If no filter annotation is defined, all metrics are collected.
The filter syntax also supports the asterisk (`*`). This symbol allows you to filter metrics keys that begin with, end with, or contain a particular sequence, such as:

* `redis_db*` filters all metrics starting with `redis_db`
* `*insights*` filters all metrics containing `insights`
* `*bytes` filters all metrics ending with `bytes`

Using the `*` symbol within a filter, such as `redis_*_bytes`, is not supported.

The filter is applied to the raw metric key, so it's important to know that Dynatrace automatically appends suffixes to some metric keys, depending on the original metric key and metric type.
For details, see [Payload](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

For summary and histogram, the filter is applied to the whole metric family, as stated in the `#TYPE` line of OpenMetrics format.
For example, if the summary metric family `foo_seconds` is filtered, all the metric points, including `foo_seconds_count` and `foo_seconds_sum`, are filtered.
Conversely, if `foo_seconds_count` is stated as a filter, nothing is filtered because there's no such metric family.

This example shows how to use the filter syntax in a pod definition with annotations:

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/filter: |



{



"mode": "include",



"names": [



"redis_db_keys",



"*insights*",



"*bytes"



]



}



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

The values of `metrics.dynatrace.com/path`, `metrics.dynatrace.com/port`, and `metrics.dynatrace.com/secure` depend on the exporter being used; adapt them to your requirements. To determine the port value, see [Default port allocationsï»¿](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) for a list of common ports for known exporters.

### Client authentication Optional

**Requirements:** Add the permissions to access `secrets` and `configmaps` for the `dynatrace-kubernetes-monitoring` ClusterRole.

Some systems require extra authentication before Dynatrace can scrape them. For such cases, you can set the following additional annotations:

* `metrics.dynatrace.com/tls.ca.crt`
* `metrics.dynatrace.com/tls.crt`
* `metrics.dynatrace.com/tls.key`

The required certificates/keys are automatically loaded from `secret`/`configmaps` specified in the annotation value.  
The schema for the annotation values is `<configmap|secret>:<namespace>:<resource_name>:<field_name_in_data_section>`.

For example, the annotations could look as follows:

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/tls.ca.crt: 'configmap:kubernetes-config:etcd-metric-serving-ca:ca-bundle.crt'



metrics.dynatrace.com/tls.crt: 'secret:kubernetes-config:etcd-metric-client:tls.crt'



metrics.dynatrace.com/tls.key: 'secret:kubernetes-config:etcd-metric-client:tls.key'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Ingesting metrics from exporters requiring client authentication is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### HTTP - Basic authentication Optional

**Requirements:** Add the permissions to access `secrets` for the `dynatrace-kubernetes-monitoring` ClusterRole.

For systems that require basic HTTP authentication before scraping, you can apply the following additional annotations.

* `metrics.dynatrace.com/http.auth.basic.username`
* `metrics.dynatrace.com/http.auth.basic.password`

The following example shows two secrets created in the `default` namespace â one for a username and one for a password.
The aforementioned annotations are then used on a pod, with the secrets referenced in the annotation values.

```
apiVersion: v1



kind: Secret



metadata:



name: user-secret



data:



username: bXktdXNlcm5hbWUtc2VjcmV0Cg==



---



apiVersion: v1



kind: Secret



metadata:



name: password-secret



data:



password: bXktcGFzc3dvcmQtc2VjcmV0Cg==
```

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/http.auth.basic.username: 'secret:default:user-secret:username'



metrics.dynatrace.com/http.auth.basic.password: 'secret:default:password-secret:password'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Ingesting metrics from exporters requiring basic HTTP authentication is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### HTTP - Bearer token authentication Optional

**Requirements:**

* ActiveGate version 1.317+
* Add the permissions to access `secrets` for the `dynatrace-kubernetes-monitoring` ClusterRole.

For systems that require Bearer token authentication before scraping, you can apply the additional annotation `metrics.dynatrace.com/http.auth`.

The following example shows a secret called `token-secret` created in the `default` namespace. The required Bearer token is stored under the key `bearer`.

```
apiVersion: v1



kind: Secret



metadata:



name: token-secret



data:



bearer: bXktYmVhcmVyLXRva2VuCg==
```

The annotation is then used on a pod, with the secret referenced in the annotation values.

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/http.auth: 'secret:default:token-secret:bearer'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Ingesting metrics from exporters requiring Bearer token authentication is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### Role-based access control (RBAC) authorization for metric ingestion

Exporter pods such as `node-exporter`, `kube-state-metrics`, and `openshift-state-metrics` require [RBAC authorizationï»¿](https://dt-url.net/n721pt6). For these pods, add the annotation:

`metrics.dynatrace.com/http.auth: 'builtin:default'`

This annotation applies the token from the `dynatrace-activegate` service account as an authorization header for requests to the exporter.

Ingesting metrics from exporters requiring RBAC authorization is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

For more information on how to annotate pods, see [Annotation best practices](#best).

## Annotate Kubernetes services

**Requirements:** Add the permission to access **services** for the `dynatrace-kubernetes-monitoring` ClusterRole (not needed for Dynatrace Operator users, as this is enabled by default in [clusterrole-kubernetes-monitoring.yamlï»¿](https://dt-url.net/gl027s4)).

You can also annotate services instead of pods. Pods corresponding to the Kubernetes services are automatically discovered via the service label selector, causing scraping of all pods belonging to the service.

* The service and its corresponding pods must be located in the same namespace.
* The `metrics.dynatrace.com/port` annotation should specify the target port of the container pod within the service, not the service's own port, since the service is not used for proxying the scraping process.

For more information on how to annotate services, see [Annotation best practices](#best).

## Annotation best practices

There are multiple ways to place annotations on pods or services. See below to decide which approach fits your scenario best.

### Recommended if you have full control

If you have full control over the pod template or service definition, we recommend adding the annotations by editing these files. This is the most reliable way to ensure persistency of annotations. We recommend editing the pod template over editing the service definition, as this requires fewer permissions (for example, if you don't have access to services).  
**Pro:** Annotations are persistent, so they don't need to be recreated if a pod is removed.

### Options if you don't have full control

If you don't have full control over the pod template, you have the following options:

* Annotate an existing service (in YAML)  
  **Requirements:** Have control over an existing YAML and permission to edit the existing Kubernetes service object.  
  **Pro:** Annotations are persistent.  
  **Con:** None.  
  **Example:**

  ```
  kind: Service



  apiVersion: v1



  metadata:



  name: dynatrace-monitoring-node-exporter



  namespace: kubernetes-monitoring



  annotations:



  metrics.dynatrace.com/port: '12071'



  metrics.dynatrace.com/scrape: 'true'



  metrics.dynatrace.com/secure: 'true'



  metrics.dynatrace.com/path: '/metrics'



  spec:



  ports:



  - name: dynatrace-monitoring-node-exporter-port



  port: 9100



  targetPort: 12071



  selector:



  app.kubernetes.io/name: node-exporter
  ```
* Create a new service (in YAML)  
  **Requirements**: The new service should be created with a name that preferably starts with the `dynatrace-monitoring-` prefix. This service must be in the same namespace as the pods, and have permission to create a Kubernetes service object. The service is preferably headless (`clusterIP` is set to `None`) since it emphasizes that the service is not used for proxying.

  **Pro:** You have control over the original workload/service.  
  **Con:** A label selector sync is required. We support only the label selector.  
  **Example:**

  ```
  kind: Service



  apiVersion: v1



  metadata:



  name: dynatrace-monitoring-node-exporter



  namespace: kubernetes-monitoring



  annotations:



  metrics.dynatrace.com/port: '12071'



  metrics.dynatrace.com/scrape: 'true'



  metrics.dynatrace.com/secure: 'true'



  metrics.dynatrace.com/path: '/metrics'



  spec:



  ports:



  - name: dynatrace-monitoring-node-exporter-port



  port: 12071



  selector:



  app.kubernetes.io/name: node-exporter



  clusterIP: None
  ```
* Annotate an existing service (in CLI)  
  **Requirements:** Have permission to edit the existing Kubernetes service object.  
  **Pro:** No label selector sync is required.  
  **Con:** Annotations aren't persistent, so changes will overwrite the annotations. We support only the label selector.
* Annotate existing pods (in CLI)  
  **Requirements:** None.  
  **Pro:** You can quickly test metric ingestion.  
  **Con:** Annotations aren't persistent, so changes will overwrite the annotations.

## View metrics on a dashboard

Metrics from Prometheus exporters are available in Data Explorer for custom charting. Select **Create custom chart** and select **Try it out** in the top banner. For more information, see [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

You can simply search for metric keys of all available metrics and define how youâd like to analyze and chart your metrics. After that you can pin your charts on a dashboard.

## Metric alerts

You can also create custom alerts based on the Prometheus scraped metrics. Go to **Settings** > **Anomaly detection** > **Metric events** and select **Add metric event**. In the **Add metric event** page, search for a Prometheus metric using its key and define your alert. For more information, see [Metric events for alerting](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Limitations

The current limitations of the Prometheus metrics integration are as follows:

### Multiple exporters in a pod

Only one port and path can be specified in the annotations. However, it is possible to scrape multiple exporters in a pod by [annotating
additional services](#annotate-kubernetes-services) that select the same pod.

For example, if you want to scrape two endpoints in a pod, you could annotate the pod and the service
that selects the pod. If no such service exists, you can create a new service just for this purpose.

Alternatively, you could also annotate two different services that select the same pod. For more information, see [Annotation best practices](#best).

### Number of pods, metrics, and metric data points

Per Kubernetes cluster, this integration supports a maximum of:

* 1,000 exporter pods
* 1,000 metrics per pod
* 500,000 metric data points per pod

  Even though larger datasets are allowed, these can lead to ingestion gaps, as Dynatrace collects all metrics every minute before sending them to the cluster.

### Monitoring methods

There are two distinct methods of monitoring technologies:

* The first method involves using the [Extensions 2.0ï»¿](https://dt-url.net/9t036yh) framework, which supports a handful of extensions for Prometheus exporters out of the box.

  This method provides comprehensive monitoring features, including technology-specific dashboards, alerting capabilities, topology visualization, and entity pages. However, this method operates outside of Kubernetes.
* The second method involves annotating Prometheus pods within Kubernetes to scrape Prometheus exporters.

  While this method provides a more Kubernetes-native approach, it currently offers minimal functional overlap with the features provided by the Extensions 2.0 framework.

These two methods serve different contexts, work independently from each other, and don't share the same metrics.

## Monitoring consumption

If you have DPS licensing, you can get more information about your environment's custom metric consumption from our [licensing documentation](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

* Full-Stack Monitoring [includes a fixed number of custom metric data points](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-metrics "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") for each GiB that contributes to your environment's GiB-hour consumption for containers with code-modules.

If you have Dynatrace classic licensing, Prometheus metrics in Kubernetes environments are subject to [DDU consumption](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

* Prometheus metrics from exporters running on hosts monitored by OneAgent are first deducted from your quota of [included metrics per host unit](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). After this quota is exceeded, any additional metrics consume [DDUs](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").
* Prometheus metrics from exporters running on hosts not monitored by OneAgent always consume [DDUs](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Troubleshoot

To troubleshoot Prometheus integration issues, download the [Kubernetes Monitoring Statistics extensionï»¿](https://dt-url.net/n903xmb). For more information, see the community article on [How to troubleshoot missing Prometheus metricsï»¿](https://dt-url.net/3m02ozr).

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")
* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-pvc-metrics.md


---
title: Monitor persistent volume claims on Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-pvc-metrics
scraped: 2026-02-17T21:16:49.919459
---

# Monitor persistent volume claims on Kubernetes/OpenShift

# Monitor persistent volume claims on Kubernetes/OpenShift

* 2-min read
* Updated on Jul 09, 2024

This page outlines the minimum version requirements for basic persistent volume claims monitoring capabilities.

Dynatrace version 1.294 +

ActiveGate version 1.289+

In Kubernetes, persistent data is stored in [persistent volume claims (PVCs)ï»¿](https://dt-url.net/n403y11). Dynatrace provides you the needed insights into your persistent volume claims capacity.

* Dynatrace provides **Kubernetes persistent volume claims** preset dashboards that allow you to analyze your persistent volume claims based on total capacity, usage, remaining free space, and growth rates.
* Templates for custom alerts enable you to alert on related issues, such as persistent volume claims running out of free space or growing in an unusual manner.

To start monitoring persistent volume claims, see below.

## Enablement

PVC monitoring is a built-in feature and does not need to be enabled manually.

## Permissions

Make sure that the `get` rule and the `nodes/metrics` resources are enabled in the Kubernetes ClusterRole. If you're monitoring PVCs with an ActiveGate running outside of the cluster, you'll also need the `nodes/proxy` permission.

Example:

![Example PVC permissions](https://dt-cdn.net/images/screenshot-1-1215-23c529f37c.png)

## Dashboarding

Dynatrace provides a pre-configured dashboard that covers the following use-cases:

* Show namespaces with most / least free space
* Show namespaces with biggest growth rate
* Show top 10 list of the biggest PVCs
* Show capacity / usage per namespace

![Example PVC dashboard](https://dt-cdn.net/images/kubernetes-persistent-volume-claims-dashboard-1357-3d62f7e8b3.png)

## Limitations

This feature is available only if your Kubernetes cluster is [connected to a local Kubernetes API endpoint](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-services-kubernetes.md


---
title: Monitor Kubernetes/OpenShift services
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-services-kubernetes
scraped: 2026-02-17T21:16:43.370786
---

# Monitor Kubernetes/OpenShift services

# Monitor Kubernetes/OpenShift services

* 3-min read
* Published Sep 28, 2022

Dynatrace version 1.251+

The unified analysis view for Kubernetes services enables you to examine port definitions and IP addresses for Kubernetes services, and it provides valuable details about the set of pods that are served by a specific Kubernetes service, including events and logs.

![k8s-services](https://dt-cdn.net/images/screenshot-2022-09-28-at-10-20-34-1409-0007e0fe8d.png)

The Kubernetes services from Infrastructure Monitoring and the services from Applications & Microservices are two fundamentally different concepts.

* A [Kubernetes serviceï»¿](https://dt-url.net/x3034x8) (entity type: `KUBERNETES_SERVICE`) is a Kubernetes-specific concept. It usually exposes a set of pods on the network level. Pods can be served by multiple Kubernetes services.
* A [service](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")(entity type: `SERVICE`) is automatically detected by Dynatrace based on the properties of your application deployment and configuration. Depending on technologies and configuration, Dynatrace can either detect multiple services per pod, or services that span across multiple pods.

## Prerequisites

* ActiveGate version 1.251+ with Kubernetes API monitoring enabled
* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

If you're not using Dynatrace Operator, you also need to enable the `list services` and `get services` permissions on your [service accountï»¿](https://dt-url.net/ov034vn) used to connect to the Kubernetes API.

## Access Kubernetes services

You can access Kubernetes services in Dynatrace via:

* Kubernetes cluster/namespace overview page (see the **Kubernetes services** column)
* Kubernetes namespace/workload/pod details page (see the **Kubernetes services** card)

On the Kubernetes service/workload/pod overview pages, you can filter by:

* Kubernetes service
* Kubernetes service name
* Kubernetes service type (`ClusterIP`, `NodePort`, `LoadBalancer`, and `ExternalName`)

## Types of Kubernetes services

* **Cluster IP:** A stable, cluster-internal IP address that can be used within the cluster.
* **Node port:** An extension of the cluster IP type. Clients can send requests to the IP address of a node on one or more node ports. These requests are routed to the cluster IP of the Kubernetes service.

  Dynatrace provides the cluster IP as well as the port and protocol definitions next to the list of served pods on the Kubernetes service details screen.
* **Load balancer:** Clients can send requests to the IP address of a network load balancer. Node port and cluster IP services, to which the external load balancer will route, are automatically created.

  In addition to the cluster IP, Dynatrace provides the external IP address, as well as the port and protocol definitions next to the list of served pods on the Kubernetes service details page.
* **External name:** Internal clients use the DNS name of a service as an alias for an external DNS name.

  Dynatrace provides the external name as a property on the Kubernetes service details page
* **Headless service:** Can be used when you don't need a stable IP address, but still want a pod grouping.

  Dynatrace provides the port and protocol definitions, as well as the list of served pods for headless services with selectors.

## Configure management zones

To configure management zones for Kubernetes services, you need to create a monitored entity rule for the Kubernetes service. Example: `Kubernetes service` on **Hosts** where `Kubernetes cluster name` equals `GKE CP KLU`.

![kubernetes-service-management-zones](https://dt-cdn.net/images/2022-12-09-08-26-56-1042-192ab170ec.png)

The rule for Kubernetes services is automatically included when you select **Create management zone** in the Kubernetes cluster context menu.

Existing management zones need to be manually updated to cover Kubernetes services.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-slos-kubernetes.md


---
title: Monitor service-level objectives in Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes
scraped: 2026-02-17T21:16:48.660133
---

# Monitor service-level objectives in Kubernetes/OpenShift

# Monitor service-level objectives in Kubernetes/OpenShift

* 2-min read
* Published Jan 19, 2023

You can keep track of current [service-level objectives](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") related to a Kubernetes/OpenShift workload on the **Kubernetes workload** details pages.

* Select **SLOs** on the notifications bar to display the **Service-level objectives** panel, which lists SLOs that are directly or indirectly connected to the workload.

## Directly connected SLOs

* An SLO is directly connected to a workload when the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO meets the following criteria:

  + The entity type is set to `"CLOUD_APPLICATION"`.
  + The entity ID is set to the workload ID.
* To see only SLOs that are directly connected to the workload, make sure that **Show only directly connected SLOs** is turned on.

## Indirectly connected SLOs

* An SLO isn't directly connected to a workload when, in the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO, no entity ID is provided.

  Example: When generic values such as `type("CLOUD_APPLICATION"),tag("slo")` are provided, the query results in all SLOs for all workloads, including the current workload.
* To see SLOs that are not directly connected to the workload, turn off **Show only directly connected SLOs**.

## Options

* Select **Details** to view a chart of the respective SLO metrics.
* In **Actions**, select

  + **View in Data Explorer** to [see SLO metrics in Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** to [pin the SLO to your dashboard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace."). For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
  + **SLO definition** to edit the SLO in **Service-level objective definitions**.
  + **Clone** to [clone the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** to [create an alert for the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

## No SLOs

If no SLOs are found, you can

* Select a different timeframe in the upper-right corner.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Select **Add SLO** to create an SLO in the [SLO wizard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

## Example SLO panel

![slo-card-workloads](https://dt-cdn.net/images/slo-card-754-ec31947bef.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-vulnerabilities-kubernetes.md


---
title: Monitor vulnerabilities in Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes
scraped: 2026-02-17T21:16:54.965331
---

# Monitor vulnerabilities in Kubernetes/OpenShift

# Monitor vulnerabilities in Kubernetes/OpenShift

* 1-min read
* Published Aug 24, 2022

You can keep track of security vulnerabilities in your Kubernetes environments on the cluster and workload pages.

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.
* [Activate and enable Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* To view code-level vulnerabilities [Activate and enable Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

## Vulnerability section

The **Vulnerabilities** section is displayed on the Kubernetes

* Cluster details page
* Workloads page

It shows the five most severe related [third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.") and [code-level vulnerabilities](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.").

* Select a vulnerability to view the details and understand the severity and impact of a vulnerability within your environment.
* For a complete list of the detected vulnerabilities for your Kubernetes environment, select **Show all third-party vulnerabilities**/**Show all code-level vulnerabilities**.

Example third-party vulnerabilities:

![Kubernetes workload: TPV](https://dt-cdn.net/images/workload-tpv-766-510d3cb4aa.png)

Example code-level vulnerabilities:

![Kubernetes workload: CLV](https://dt-cdn.net/images/workload-clv-767-ba23d97d54.png)

If you're missing the [security permissions](/docs/secure/application-security#permissions "Access the Dynatrace Application Security functionalities.") for the selected management zone,

* On the **Kubernetes cluster** page, the **Vulnerabilities** section is not displayed.
* On the **Kubernetes workload** page, the **Vulnerabilities** tab on the notification bar shows `Not analyzed`.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: monitor-workloads-kubernetes.md


---
title: Monitor Kubernetes/OpenShift workloads
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-workloads-kubernetes
scraped: 2026-02-17T21:16:39.681574
---

# Monitor Kubernetes/OpenShift workloads

# Monitor Kubernetes/OpenShift workloads

* 5-min read
* Updated on Nov 02, 2023

Dynatrace version 1.232+

When deployed in application-only mode, OneAgent monitors the memory, disk, CPU, and networking of processes within the container only. Host metrics aren't monitored.

## Prerequisites

* ActiveGate with the Kubernetes API monitoring enabled
* [Latest OneAgent image from Docker Hub with tag 1.38.1000+ï»¿](https://hub.docker.com/r/dynatrace/oneagent)
* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.

## Get an instant overview of your Kubernetes environment

Once you enable Kubernetes workload monitoring support, you can easily see how many cluster resources have been allocated through the workloads that are running on the cluster.

To display the Kubernetes workloads, go to ![Kubernetes Workloads](https://dt-cdn.net/images/kubernetes-workloads-512-c5f749c651.png "Kubernetes Workloads") **Kubernetes Workloads Classic**.

## Unified analysis view on your workloads, namespaces, and pods

The unified analysis view enables you to examine all the namespace-related data on the overview page of a specific Kubernetes namespace, all workload-related data on the overview page of a specific Kubernetes workload, and all the pod-related data on the overview page of a specific Kubernetes pod.

Customized unified analysis

To customize the information you receive on the unified analysis page, select **More** (**â¦**) in the upper-right corner of any section. The different selections on the unified analysis page (**View all namespaces**, **View all workloads**, **View all pods**, and so on) enable you to jump directly to any specific section or subsection you want to customize.

### Namespaces

It's common for organizations using Kubernetes to split applications into namespaces in order to isolate different business units. For example, a human resources group might have applications in the `hr` namespace, while a finance group deploys to the `finance` namespace.

The namespace unified analysis page provides a valuable view for business units like these to track the amount of resources they are allocated and compare this to their utilization rates.

On the namespace unified analysis page, you can examine properties, potential problems, resource requests and limits, workloads analysis, quotas, and events, and see all the workloads that belong to that namespace (with links to them). You can filter namespaces by metric dimension filters.

To display the namespace unified analysis page, in Dynatrace, go to ![Kubernetes Workloads](https://dt-cdn.net/images/kubernetes-workloads-512-c5f749c651.png "Kubernetes Workloads") **Kubernetes Workloads Classic** and select a namespace.

### Workloads

A workload consists of one or more pods. It's a way of describing a type of microservice that comprises an application. For instance, an application might have a frontend workload and a backend workload made up of a dozen pods, each across a Kubernetes cluster.

The workload unified analysis page provides insights into resource utilization, problem detection, [vulnerabilities](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes "Keep track of vulnerabilities in Kubernetes/OpenShift."), number of pods in the respective workload, number of services that are sending traffic to the pods, and events for all of the pods in a given workload. This information is valuable for analyzing the overall performance of a microservice rather than looking at specific problems in a pod instance.

To display the workload unified analysis page, in Dynatrace, go to ![Kubernetes Workloads](https://dt-cdn.net/images/kubernetes-workloads-512-c5f749c651.png "Kubernetes Workloads") **Kubernetes Workloads Classic** and select a workload.

Taking a closer look at the applications deployed in one of the namespaces, you can learn about their most important resource usage metrics. The workloads view covers workloads such as `Deployment`, `DeploymentConfig`, `ReplicaSet`, `DaemonSet`, `StatefulSet`, `StaticPod`, and `ReplicationController`.

The CPU throttling metric tells you how long the application was throttled, so you can determine where more CPU time would have been needed for processing. This usually happens when the containers don't have enough CPU resources (limits) in the workload definition. This might affect the performance of the processes and applications running inside the containers.

You can also see the number of running pods versus desired pods for every cloud application.

### Pods

Pods are the smallest unit of concern in Kubernetes and are the actual instances of a workload. The pod unified analysis page is where specific problems can be analyzed when a pod is crashing or slowing down due to memory or CPU saturation.

On the pod unified analysis page, you can examine properties, potential problems, utilization and resources, and events, and you can see the container to which the pod belongs (with a link to it).

To view the overview page of a Kubernetes pod

1. Go to ![Kubernetes Workloads](https://dt-cdn.net/images/kubernetes-workloads-512-c5f749c651.png "Kubernetes Workloads") **Kubernetes Workloads Classic** and select a workload.
2. Select **Pods**.
3. Select the pod you want.

### Limitations on fetching annotations

ActiveGate version 1.277 Dynatrace version 1.277

Kubernetes annotations are retrieved by the ActiveGate and displayed on the entity detail pages for Kubernetes nodes, namespaces, workloads, pods, and services. However, there are certain limitations to be aware of:

* The annotation `kubectl.kubernetes.io/last-applied-configuration` is not ingested.
* A maximum of 100 annotations per entity is allowed.
* The maximum length of any ingested annotation value is 1,024 characters. Annotation values exceeding this length are truncated.

## Find out if your applications are getting enough CPU resources

In addition to the auto-discovery and auto-tracing capabilities, OneAgent captures low-level container metrics to reflect the effect of container resource limits.  
Generic resource metrics for all supported container runtimes on Linux are available in custom charting and grouped in **Containers** > **CPU and Containers** > **Memory**.  
Metrics for the number of running and desired pods are also available under the **Cloud Platform** section.

![Kubernetes dashboard](https://dt-cdn.net/images/kubernetes-dashboard-1920-97799f0ea5.png)

The CPU throttled time and memory usage percentage shows if the resource limits in the Kubernetes pod specs are set correctly. If memory usage reaches 100%, containers or applications will crash (out of memory) and need to be restarted.

## Fine-grained control of visibility into namespaces and workloads via management zones

You can use management zones to control user access to the monitoring data of specific Kubernetes objects in your environment. For example, you can limit the access to specific workloads and namespaces to specific user groups. With this approach, you can control user access to specific Dynatrace Kubernetes pages, custom charts, and dashboards.

![Managementzone](https://dt-cdn.net/images/managementzone-1280-23030a6dc2.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: kubernetes-monitoring.md


---
title: Kubernetes Classic
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring
scraped: 2026-02-17T21:13:44.301295
---

# Kubernetes Classic

# Kubernetes Classic

* 1-min read
* Updated on Sep 28, 2022

Dynatrace provides full-stack monitoring for Kubernetes, covering everything from the application layer down to the infrastructure layer.

## Prerequisites

1. [Set up and configure Dynatrace integration on Kubernetes](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")
2. [Connect your cluster to Dynatrace](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace")

See [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") for further options and details.

## Default monitoring features

To learn how to configure default monitoring features for Kubernetes/OpenShift clusters, see [Global default monitoring settings for Kubernetes/OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/default-monitoring-settings "Configure default monitoring settings for all new Kubernetes/OpenShift clusters in your environment.")

## View monitoring results

To learn how to analyze monitoring results in Dynatrace, see:

* [Monitor Kubernetes/OpenShift cluster utilization](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes "Monitor the health and utilization of your Kubernetes/OpenShift cluster resources.")
* [Monitor Kubernetes/OpenShift events](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes "Extend visibility into Kubernetes/OpenShift events.")
* [Monitor Kubernetes/OpenShift workloads](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-workloads-kubernetes "Enable Kubernetes/OpenShift workloads integration for Dynatrace monitoring.")
* [Monitor Kubernetes/OpenShift services](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-services-kubernetes "Enable Kubernetes/OpenShift service integration for Dynatrace monitoring.")
* [Monitor Kubernetes/OpenShift metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-metrics-kubernetes "Available metrics for monitoring Kubernetes/OpenShift clusters")
* [Monitor Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")
* [Organize Kubernetes/OpenShift deployments by tags](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.")
* [Monitor persistent volume claims on Kubernetes/OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-pvc-metrics "Enable Kubernetes/OpenShift monitoring for persistent volume claims metrics.")
* [Alert on common Kubernetes/OpenShift issues](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.")
* [Monitor vulnerabilities in Kubernetes/OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes "Keep track of vulnerabilities in Kubernetes/OpenShift.")
* [Monitor service-level objectives in Kubernetes/OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes "Keep track of SLOs for Kubernetes/OpenShift.")
* [Istio/Envoy proxy metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection")
* [Global default monitoring settings for Kubernetes/OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/default-monitoring-settings "Configure default monitoring settings for all new Kubernetes/OpenShift clusters in your environment.")

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")


---


## Source: use-cases.md


---
title: Use cases
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/use-cases
scraped: 2026-02-06T16:29:09.689987
---

# Use cases

# Use cases

* Latest Dynatrace
* 1-min read
* Published Oct 11, 2023

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** enhances the management and monitoring of your Kubernetes environment. It enables a range of functionalities.

* Health and performance monitoring

  + Access detailed views of your clusters that display all critical health signals for resources such as nodes, namespaces, and workloads.
  + Automatically discover, and track the status and performance of, nodes and pods.
  + View metrics, events, and logs from the pods and nodes in a single interface.
  + Gain a high-level overview of all your clusters, regardless of the cloud services they're hosted on.
* Resource efficiency and optimization

  + Understand the overall utilization of resources across your clusters.
  + Identify workloads that are consuming the most resources.
  + Analyze workloads to determine which ones are under-resourced and adjust resource allocations.

Find detailed descriptions of various use cases below.

[### Assess and troubleshoot cluster health

Understand and manage the health of your Kubernetes clusters.](/docs/observe/infrastructure-observability/container-platform-monitoring/use-cases/cluster-health "Understand and manage the health of your Kubernetes clusters with Dynatrace.")[### Optimize workload resource usage with Kubernetes (new) **Kubernetes** and Notebooks **Notebooks**

Efficiently utilize your cluster's resources.](/docs/observe/infrastructure-observability/container-platform-monitoring/use-cases/resource-optimization "Efficiently utilize your cluster's resources by identifying workloads that don't fully utilize their allocated resources.")[### Troubleshooting common health problems of Kubernetes workloads

Identify and resolve health problems in Kubernetes workloads.](/docs/observe/infrastructure-observability/container-platform-monitoring/use-cases/troubleshoot-health-problems "Identify and resolve health problems in Kubernetes workloads.")[### Predictive Kubernetes operations

Manage disk space within Kubernetes environments.](/docs/observe/infrastructure-observability/container-platform-monitoring/use-cases/predictive-operations "Proactively manage disk space within Kubernetes environments")[### Alert on common misconfigurations and detect anomalies

Address Kubernetes issues using out-of-the-box alerting mechanisms.](/docs/observe/infrastructure-observability/container-platform-monitoring/use-cases/alert-use-case "Proactively address Kubernetes issues using out-of-the-box alerting mechanisms.")


---


## Source: container-platform-monitoring.md


---
title: Container platform monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring
scraped: 2026-02-17T21:21:58.873916
---

# Container platform monitoring

# Container platform monitoring

* Explanation
* 1-min read
* Published Jun 25, 2021

[![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes")

### Kubernetes Classic

Available metrics for monitoring Kubernetes clusters.](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")

### Cloud Foundry

Monitor Cloud Foundry with Dynatrace.](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")[![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")

### Docker

Deploy OneAgent on Docker.](/docs/ingest-from/setup-on-container-platforms/docker "Deploy OneAgent on Docker.")[![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")

### Heroku

Monitor Heroku with Dynatrace.](/docs/observe/infrastructure-observability/container-platform-monitoring/heroku "Monitor Heroku with Dynatrace.")

## Related topics

* [Set up Dynatrace on container and PaaS platforms](/docs/ingest-from/setup-on-container-platforms "Deploy Dynatrace on various container and PaaS platforms.")
* [Monitor container groups](/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups "Overview on container groups monitoring")
* [Container monitoring rules](/docs/observe/infrastructure-observability/container-platform-monitoring/container-monitoring-rules "Define, enable and disable container monitoring rules")


---


## Source: data-collected.md


---
title: Data collected with Dynatrace database monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/data-collected
scraped: 2026-02-17T21:17:14.612732
---

# Data collected with Dynatrace database monitoring

# Data collected with Dynatrace database monitoring

* Latest Dynatrace
* Reference
* Published Jan 20, 2026

When you enable a DB Extension, it automatically collects all metrics defined in the corresponding integration documentation. These include metrics related to database configuration, activity, uptime, connections, buffer pools, query performance, and many others used by the Databases app.

All collected data can also be used in dashboards, alerts, notebooks, and any other metric-based workflows within Dynatrace.

For a complete list of metrics collected, select your database vendor from the list below.

* [IBM DB2](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#feature-sets "Remotely collect monitoring metrics from your DB2 databases.")
* [MariaDB](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1#feature-sets "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details")
* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql#feature-sets "How to set up monitoring for Microsoft SQL databases in Dynatrace.")
* [MySQL](/docs/observe/infrastructure-observability/databases/extensions/mysql-remote-monitoring-v2#feature-sets "Monitor your MySQL instances remotely, collect key KPIs, and slow query details.")
* [Oracle](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your database.")
* [PostgreSQL](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.")
* [SAP HANA](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#feature-sets "Monitor SAP HANA databases remotely to analyze SQL performance and database health.")
* [Snowflake](/docs/observe/infrastructure-observability/databases/extensions/snowflake#feature-sets "Expand visibility to improve health and performance monitoring of your Snowflake database.")

## Data collection details

### Normalized queries

To protect sensitive information and improve analysis, queries are normalized before storage. This process replaces literal parameter values with placeholders, ensuring that Personally Identifiable Information (PII) is removed.

For example:

**Before normalization**

```
SELECT * FROM customers WHERE email = 'john.doe@example.com';



SELECT * FROM customers WHERE email = 'J.I.Jane@other_example.com';
```

**After normalization**

```
SELECT * FROM customers WHERE email = ?;
```

This approach also applies to execution plans, where parameter values are stripped out to prevent exposure of sensitive data.

### Monitored database instances

Database monitoring supports multiple database technologies through Extensions. However, only the first 70 databases discovered or configured are actively monitored. This limit ensures optimal performance and resource usage.

### Monitored database queries

Monitoring focuses on the top 200 queries based on resource consumption and execution time. Since data is sampled every 1 minute, the list of top queries may vary between samples. However, over time, clear trends emerge, making it easy to analyze overall usage patterns and identify consistently expensive queries.

### Control feature sets and data collection frequency

You can control certain feature sets, which determine what data is collected. For example:

* **Query metrics**: Enable or disable query-level monitoring.
* **Execution plans**: Enable or disable the collection of query plans.
* **Activity metrics**: Control instance-level data frequency.

For selected feature sets, you can adjust the collection frequency to balance detail and overhead. For example:

* Collect query metrics every 1 minute or every 5 minutes.
* Adjust instance activity polling intervals.

However, not all feature sets can be disabled, as some are essential for core functionality.

### Remove PII

To comply with privacy standards:

* Query parameters are replaced with placeholders during normalization.
* Execution plans are sanitized to remove sensitive values.

This ensures that no PII is stored or exposed in monitoring data.

### Data retention

Collected data is retained based on the configuration of the data bucket. By default, data is stored for 35 days, after which it is automatically purged. You can adjust retention settings according to your organizationâs compliance and storage requirements.

## Supported database vendors

The Dynatrace ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** is designed to minimize impact on monitored database instances and follows industry best practices for low-overhead observability.

To ensure efficient data collection:

* Database instance metrics are collected every 1 minute and use lightweight system tables that avoid performance penalties.
* Host metrics are sourced from the operating system or cloud monitoring services. This approach doesn't require direct polling from the database.
* Database-level metrics are also gathered every 1 minute, but only display for a limited number of databases to reduce load.
* Query metrics are collected every 1 minute, but only for a limited set of queries, selected to balance insight with performance.
* Slow query log collection is optional (only for Postgres and MySQL). To minimize overhead, configure a high threshold and enable sampling to limit the number of queries logged as slow.
* Configuration data (only for Postgres and MySQL) is retrieved every 24 hours to ensure visibility without frequent access.

This architecture ensures that monitoring remains lightweight and scalable, even in environments with multiple databases per instance.


---


## Source: ibm-db2.md


---
title: Monitor IBM DB2 database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/ibm-db2
scraped: 2026-02-17T21:27:58.145525
---

# Monitor IBM DB2 database

# Monitor IBM DB2 database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Use Dynatrace Extension framework to extend your application observability into data acquired directly from your IBM Database layer and monitor how database server tasks impact your app. To learn more, see [Get started with IBM DB2 database extension](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#get-started "Remotely collect monitoring metrics from your DB2 databases.").

## Prerequisites

Ensure your system meets these [requirements](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#requirements "Remotely collect monitoring metrics from your DB2 databases.") for full feature support.

## Set up IBM DB2 extension for monitoring

To set up and activate the extension, follow these [detailed activation steps](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#activation-and-setup "Remotely collect monitoring metrics from your DB2 databases.").

1. Install the IBM DB2 extension.
2. Define endpoints.
3. Select an ActiveGate group.
4. Activate the extension.

## FAQ

For complete details, go to the [FAQ](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#faq "Remotely collect monitoring metrics from your DB2 databases.").

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#feature-sets "Remotely collect monitoring metrics from your DB2 databases.") restrict which metrics are collected when you activate the extension.

## Related topics

* [IBM DB2 for LUW (remote monitoring) extension](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring "Remotely collect monitoring metrics from your DB2 databases.")


---


## Source: mariadb.md


---
title: Monitor MariaDB database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/mariadb
scraped: 2026-02-17T05:00:06.228604
---

# Monitor MariaDB database

# Monitor MariaDB database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Use Dynatrace Extension framework to extend your application observability into data acquired directly from your MariaDB database layer and monitor how database server tasks impact your app.

## Prerequisites

Ensure your system meets these [requirements](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1#requirements "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details") for full feature support.

## Set up MariaDB extension for monitoring

To set up and activate the extension, follow these [detailed activation steps](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1#activation-and-setup "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details").

1. Add the database instance.
2. Select the hosting type.
3. Select an ActiveGate group.
4. Create a database connection.
5. Install the extension.

## FAQ

For complete details, go to the [FAQ](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1#faq "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details") section.

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1#feature-sets "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details") restrict which metrics are collected when you activate the extension.

## Related topics

* [MariaDB extension](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1 "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details")


---


## Source: microsoft-sql.md


---
title: Monitor Microsoft SQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql
scraped: 2026-02-17T21:30:51.478857
---

# Monitor Microsoft SQL database

# Monitor Microsoft SQL database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

There are three Microsoft SQL extensions supported in Dynatrace:

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#overview "Improve the health and performance monitoring of your Microsoft SQL Servers."): Uses a modern extension architecture with AIOps capabilities to simplify database monitoring and improve cross-team collaboration. This extension provides real-time and automatic insights into database performance metrics and business KPIs.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#overview "Improve the health and performance monitoring of your Microsoft SQL Servers."): Uses WMI queries to collect key performance and health metrics from the SQL Server instance running on the host, extending your visibility.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#overview "Improve the health and performance monitoring of your Microsoft SQL Servers."): Uses Windows Performance Counters to collect key performance and health metrics for all SQL Server instances on the host.

Depending on your particular use case, such as the environmentâs access restrictions, performance needs, and monitoring goals, you might choose one or both extensions to get complete visibility.

## Prerequisites

Ensure your system meets the requirements and has the necessary compatibility information for full feature support.

* For Microsoft SQL Server, refer to the [requirements](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#requirements "Improve the health and performance monitoring of your Microsoft SQL Servers.") and [compatibility information](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#compatibility-information "Improve the health and performance monitoring of your Microsoft SQL Servers.") information.
* For Microsoft SQL Server (local), refer to [compatibility information](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#compatibility-information "Improve the health and performance monitoring of your Microsoft SQL Servers.") information.
* For Microsoft SQL Server local counters, refer to the [requirements and compatibility](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#requirements "Improve the health and performance monitoring of your Microsoft SQL Servers.") information.

## Set up Microsoft SQL extension for monitoring

To set up and activate the extension:

* For Microsoft SQL Server, refer to [Microsoft SQL Server activation and setup](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#activation-and-setup "Improve the health and performance monitoring of your Microsoft SQL Servers.").
* For Microsoft SQL Server (local) and Microsoft SQL Server local counters, follow these steps.

  1. Install OneAgent on the SQL Server host.
  2. Enable log monitoring.
  3. Activate the extension from the Hub.

  To learn more, refer to [Microsoft SQL Server (local) activation steps](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#activation-and-setup "Improve the health and performance monitoring of your Microsoft SQL Servers.") and [Microsoft SQL Server local counters activation steps](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#activation-and-setup "Improve the health and performance monitoring of your Microsoft SQL Servers.").

## Feature sets

Feature sets restrict which metrics are collected when you activate the extension.
Refer to the sections below to learn more about each feature set.

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#feature-sets "Improve the health and performance monitoring of your Microsoft SQL Servers.") feature sets.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#feature-sets "Improve the health and performance monitoring of your Microsoft SQL Servers.") feature sets.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#feature-sets "Improve the health and performance monitoring of your Microsoft SQL Servers.") feature sets.

## Use cases

Check these use case scenarios for more details.

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#use-cases "Improve the health and performance monitoring of your Microsoft SQL Servers.") use cases.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#use-cases "Improve the health and performance monitoring of your Microsoft SQL Servers.") use cases.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#use-cases "Improve the health and performance monitoring of your Microsoft SQL Servers.") use cases.

## Related topics

* [Microsoft SQL Server extension](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2 "Improve the health and performance monitoring of your Microsoft SQL Servers.")
* [Microsoft SQL Server local counters extension](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters "Improve the health and performance monitoring of your Microsoft SQL Servers.")
* [Microsoft SQL Server (local) extension](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local "Improve the health and performance monitoring of your Microsoft SQL Servers.")


---


## Source: mysql.md


---
title: Monitor MySQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/mysql
scraped: 2026-02-16T09:34:19.748586
---

# Monitor MySQL database

# Monitor MySQL database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Use Dynatrace Extension framework to extend your application observability into data acquired directly from your MySQL database layer and monitor how database server tasks impact your app.

## Prerequisites

Ensure that your system meets the [requirements](/docs/observe/infrastructure-observability/databases/extensions/mysql-remote-monitoring-v2#requirements "Monitor your MySQL instances remotely, collect key KPIs, and slow query details.") for full feature support.

## Set up the MySQL extension for monitoring

To set up and activate the extension, follow these [detailed activation steps](/docs/observe/infrastructure-observability/databases/extensions/mysql-remote-monitoring-v2#activation-and-setup "Monitor your MySQL instances remotely, collect key KPIs, and slow query details.").

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/mysql-remote-monitoring-v2#feature-sets "Monitor your MySQL instances remotely, collect key KPIs, and slow query details.") restrict which metrics are collected when you activate the extension.

## FAQ and troubleshooting

For complete details, go to the [FAQ](/docs/observe/infrastructure-observability/databases/extensions/mysql-remote-monitoring-v2#faq "Monitor your MySQL instances remotely, collect key KPIs, and slow query details.") section.


---


## Source: oracle.md


---
title: Monitor Oracle database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/oracle
scraped: 2026-02-17T21:27:02.912057
---

# Monitor Oracle database

# Monitor Oracle database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Use Dynatrace Extension framework to extend your application observability into data acquired directly from your Oracle database layer and monitor how database server tasks impact your app.

## Prerequisites

Ensure that your system meets the [requirements](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#requirements "Observe, analyze, and optimize the usage, health, and performance of your database.") for full feature support.

## Set up Oracle extension for monitoring

To set up and activate the extension, follow these [detailed activation steps](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#activation-and-setup "Observe, analyze, and optimize the usage, health, and performance of your database.").

## FAQ and troubleshooting

Refer to the Oracle database extension [FAQ](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#faq "Observe, analyze, and optimize the usage, health, and performance of your database.") and [troubleshooting](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#troubleshooting "Observe, analyze, and optimize the usage, health, and performance of your database.") sections.

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your database.") restrict which metrics are collected when you activate the extension.

## Use cases

Oracle Database monitoring helps you understand your application's database interactions, performance bottlenecks, and resource impact by monitoring executed statements, query patterns, and server health. To learn more, see [Oracle database monitoring use cases](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#use-cases "Observe, analyze, and optimize the usage, health, and performance of your database.").

## Related topics

* [Oracle Database extension](/docs/observe/infrastructure-observability/databases/extensions/oracle-database "Observe, analyze, and optimize the usage, health, and performance of your database.")


---


## Source: sap-hana.md


---
title: Monitor SAP HANA database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/sap-hana
scraped: 2026-02-17T21:28:33.944931
---

# Monitor SAP HANA database

# Monitor SAP HANA database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Use Dynatrace Extension framework to extend your application observability into data acquired directly from your SAP HANA database layer and monitor how database server tasks impact your app.

## Prerequisites

Ensure your system meets these [requirements](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#requirements "Monitor SAP HANA databases remotely to analyze SQL performance and database health.") for full feature support.

## Set up SAP HANA extension for monitoring

To set up and activate the extension, follow these [detailed activation steps](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#activation-and-setup "Monitor SAP HANA databases remotely to analyze SQL performance and database health.").

1. Add the database instance.
2. Select the hosting type.
3. Select an ActiveGate group.
4. Create a database connection.
5. Install the extension.

## Use cases

You can benefit from SAP HANA monitoring in these [use cases](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#use-cases "Monitor SAP HANA databases remotely to analyze SQL performance and database health.").

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#feature-sets "Monitor SAP HANA databases remotely to analyze SQL performance and database health.") restrict which metrics are collected when you activate the extension.

## FAQ and troubleshooting

For complete details, go to the [FAQ](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#faq "Monitor SAP HANA databases remotely to analyze SQL performance and database health.") section.

## Related topics

* [SAP HANA Database (remote monitoring) extension](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring "Monitor SAP HANA databases remotely to analyze SQL performance and database health.")


---


## Source: snowflake.md


---
title: Monitor Snowflake database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/snowflake
scraped: 2026-02-17T21:32:25.098490
---

# Monitor Snowflake database

# Monitor Snowflake database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Use Dynatrace Extension framework to extend your application observability into data acquired directly from your Snowflake database layer and monitor how database server tasks impact your app.

## Prerequisites

Ensure your system meets these [requirements](/docs/observe/infrastructure-observability/databases/extensions/snowflake#requirements "Expand visibility to improve health and performance monitoring of your Snowflake database.") for full feature support.

## Set up Snowflake extension for monitoring

To set up and activate the extension, follow the [detailed activation steps](/docs/observe/infrastructure-observability/databases/extensions/snowflake#activation-and-setup "Expand visibility to improve health and performance monitoring of your Snowflake database.").

1. Add the database instance.
2. Select the hosting type.
3. Select an ActiveGate group.
4. Create a database connection.
5. Install the extension.

## Use cases

You can benefit from Snowflake monitoring in these [use cases](/docs/observe/infrastructure-observability/databases/extensions/snowflake#use-cases "Expand visibility to improve health and performance monitoring of your Snowflake database.").

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/snowflake#feature-sets "Expand visibility to improve health and performance monitoring of your Snowflake database.") restrict which metrics are collected when you activate the extension.

## Related topics

* [Snowflake extension](/docs/observe/infrastructure-observability/databases/extensions/snowflake "Expand visibility to improve health and performance monitoring of your Snowflake database.")


---


## Source: get-started.md


---
title: Get started with database monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started
scraped: 2026-02-17T21:17:13.500714
---

# Get started with database monitoring

# Get started with database monitoring

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Dynatrace database monitoring starts with installing the ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** app from the  **Hub**. You can then use SQL extensions to collect performance metrics, query insights, and custom SQL data by adding monitoring configurations to each instance.

## Install the Databases app

1. Go to the  **Hub**.
2. Locate the ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** app, open the app overview, and select **Open**.
3. Ensure your environment meets the required [permissions](/docs/observe/infrastructure-observability/databases/database-app#permissions "The Databases app gives you an overview of all your Extensions Framework 2.0-monitored databases.").

## Set up Dynatrace database monitoring

Explore the available SQL extensions below to learn how to configure each one for database monitoring. These extensions provide performance metrics, query insights, and custom SQL monitoring without requiring agents on database hosts. To start monitoring your database instances, follow the activation and configuration steps for each extension.

[### Oracle Database

Monitor Oracle Database instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/oracle "How to set up monitoring for Oracle databases in Dynatrace.")[![Microsoft SQL Server](https://dt-cdn.net/images/techn-icon-microsoft-sqlserver-60740bd3fa.svg "Microsoft SQL Server")

### Microsoft SQL Server Database

Monitor Microsoft SQL Server Database instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql "How to set up monitoring for Microsoft SQL databases in Dynatrace.")[### PostgreSQL

Monitor PostgreSQL instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/postgres "How to set up monitoring for PostgreSQL databases in Dynatrace.")[### MySQL

Monitor MySQL instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/mysql "How to set up monitoring for MySQL databases in Dynatrace.")[![Snowflake](https://dt-cdn.net/images/snowflake-for-workflows-256-3d9ba2057b.png "Snowflake")

### Snowflake

Monitor Snowflake instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/snowflake "How to set up monitoring for Snowflake databases in Dynatrace.")[![SAP Hana DB](https://dt-cdn.net/images/sap-hana-768x256-removebg-preview-768-7c1d985abf.png "SAP Hana DB")

### SAP HANA DB

Monitor SAP HANA DB instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/sap-hana "How to set up monitoring for SAP HANA databases in Dynatrace.")[![IBM DB2](https://dt-cdn.net/images/png-clipart-ibm-db2-logo-ibm-db2-database-computer-software-sql-ibm-text-rectangle-thumbnail-removebg-preview-348-4dff315301.png "IBM DB2")

### IBM DB2

Monitor IBM DB2 instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/ibm-db2 "How to set up monitoring for IBM DB2 databases in Dynatrace.")[![MariaDB](https://dt-cdn.net/hub/mariadb-logo-vert_blue-transparent-icon_1_UyPQzsq_99Xr62T.png "MariaDB")

### MariaDB

Monitor MariaDB instances with performance metrics and query insights.](/docs/observe/infrastructure-observability/databases/database-app/get-started/mariadb "How to set up monitoring for MariaDB databases in Dynatrace.")


---


## Source: troubleshooting.md


---
title: Troubleshooting
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/troubleshooting
scraped: 2026-02-17T21:27:32.852683
---

# Troubleshooting

# Troubleshooting

* Latest Dynatrace
* Troubleshooting
* Published Jan 15, 2026


---


## Source: database-app.md


---
title: Databases app
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app
scraped: 2026-02-17T21:13:49.141083
---

# Databases app

# Databases app

* Latest Dynatrace
* App
* 4-min read
* Updated on Jan 28, 2026

The Dynatrace ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** enables you to monitor, analyze, and optimize database environments with clarity and control. It offers detailed insights into performance, health, and configuration, helping you identify issues early and maintain reliable operations.

By integrating with Dynatrace observability ecosystem, ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** connects database metrics with application and infrastructure data, supporting faster troubleshooting and smarter decision-making.

## Prerequisites

Before you begin, ensure the following:

* ActiveGate configuration

  + Assign one or more [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") to connect to the target database servers remotely.
* Required components

  + For databases requiring additional components (for example, JDBC drivers), install them on all designated ActiveGates according to the [extension guidelines](/docs/ingest-from/extensions/concepts#ag "Learn more about the concept of Dynatrace Extensions.").
* Network and [permissions](/docs/observe/infrastructure-observability/databases/database-app#permissions "The Databases app gives you an overview of all your Extensions Framework 2.0-monitored databases.")

  + Validate network connectivity and firewall rules for each database type. ActiveGate should be able to establish a direct network connection to the database host.
  + Create a monitoring user account with appropriate permissions (for example, access to system views, performance metrics, and schemas).

### Permissions

The following table describes the required permissions.

Permission

Description

davis:analyzers:execute

Execute Davis analyzer for entity problems

settings:objects:read

Read settings objects from settings V2 for Ownership and SLOs

settings:objects:write

Write settings objects from settings V2 for Ownership and SLOs

state:user-app-states:read

Read user app state

state:user-app-states:write

Store UI state

storage:buckets:read

Read buckets from Grail buckets

storage:entities:read

Read entities from Grail

storage:events:read

Read events from Grail

storage:logs:read

Read logs from Grail

storage:metrics:read

Read metrics from Grail

10

rows per page

Page

1

of 1

### Installation steps

1. Install ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** from the Dynatrace  **Hub**.
2. Configure the app to monitor supported database instances. For vendor-specific setup instructions, see [Get started with database monitoring](/docs/observe/infrastructure-observability/databases/database-app/get-started "Set up database monitoring and learn how to extend Dynatrace Databases monitoring.").
3. Add the required monitoring configurations (for example, credentials, endpoints) for each instance.

## Get started

Use ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** to monitor, analyze, and optimize your database environments. The app integrates with the Dynatrace observability ecosystem and delivers actionable insights to help you ensure reliability, improve performance, and reduce downtime.

![Get an overview of your entire database fleet](https://cdn.hub.central.dynatrace.com/hub/console/drafts/171/media/DB_Overview.png)![Get an overview of what's happening across your entire database fleet](https://cdn.hub.central.dynatrace.com/hub/console/drafts/196/media/Overview_4.jpg)![See a full view of activity metrics](https://cdn.hub.central.dynatrace.com/hub/console/drafts/196/media/Activity_metrics_3.jpg)

1 of 3Get an overview of your entire database fleet

### Databases app overview

#### Centralized dashboard

The **Overview** tab provides a high-level summary of your database landscape:

* **Database health**: Visualize healthy and unhealthy database instances to identify problem areas quickly.
* **Host metrics**: Access data from hosts running OneAgent for deeper analysis of resource dependencies.

#### Explore database instances

Select the **Explorer** tab to view a list of all your monitored instances. The **Database instances** table displays these instances.

* **Health**: Unified statuses and Davis-detected problems help you quickly identify critical issues.
* **Utilization**: Metrics such as CPU usage, memory consumption, user calls, and active sessions provide insights into resource efficiency.
* **Host details**: Drill down into host metrics or access the **Infrastructure and Operations** view for a comprehensive analysis.

##### Entity details panel

For an overview of a single instance, do one of the following:

* Go to the **Explorer** tab and select the instance name in the **Database instances** table.
* In the rightmost column, select the  (**Statement performance**) icon.

From here, you can access the **Entity details** panel and analyze all the metrics collected by the extension.

#### Statement performance analysis

Analyze resource-intensive queries to optimize performance:

* Filter queries by time, CPU, disk, or wait metrics.
* Access execution plans to understand query interactions and identify optimization opportunities.

##### Statement performance

If the extension provides related information, you can display **Statement performance analysis** to track the performance of statements that consume the most resources.

To focus your analysis:

* Set the **Filter statements** to a search string.
* Set **Contextual analysis** to the context of predefined metrics (**Time**, **CPU**, **Disk**, or **Waits**), or select the  column settings icon to customize columns and adapt the context to your needs.
* Select the **Request execution plan** to understand how the database executes the statement for optimization.

### Advanced features

The app helps you proactively address potential issues before they affect operations, reduce downtime, and improve reliability.

* Detect and resolve anomalies that use AI-powered analysis.
* Pinpoint root causes of performance degradation or failures.
* Receive actionable recommendations for query and configuration optimizations.

### Benefits

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** helps you maintain reliable, efficient, and optimized database operations. The app addresses issues proactively and provides actionable insights, allowing you to focus on strategic priorities.

* **Minimize downtime:** Detect and resolve issues before they impact operations.
* **Improve performance:** Optimize queries, schemas, and configurations for better efficiency.
* **Ensure reliability:** Support stable database operations across diverse environments.
* **Enhance productivity:** Automate observability tasks and reduce manual troubleshooting.

## Concepts

### Health score

A predefined, non-configurable metric evaluates availability, performance, configuration, and resource usage.

#### Health alerts and warning signals

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

You can set up the ready-made health alerts and warning signals through the **Alert templates** tab.

In the **Alert templates** tab, we provide pre-defined alert templates for the most popular DB vendors. Easily create a new alert by selecting a template and **New Alert**. Next, either customize the alert in the **Anomaly Detection** wizard or create the alert with one step.

Find all the custom alerts, more details of capabilities, and limits in [Anomaly Detection](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

### Insights

Insights highlight patterns, anomalies, and trends based on built-in domain expertise. They go beyond raw metrics to surface meaningful findings such as performance degradation, resource bottlenecks, and violations of best practices. These insights help you focus on what matters most and take informed, corrective actions quickly.

### Deployment flexibility

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** supports diverse deployment models:

* **On-premises**: Monitor traditional database setups.
* **Cloud**: Gain visibility into cloud-hosted databases (for example, AWS RDS).
* **Hybrid**: Ensure consistent observability across mixed environments.

## Use cases

### Understand database health

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** provides a real-time overview of your database's health. The app continuously evaluates key metrics to provide a health score that reflects the current state of your database environment. This health score helps you quickly identify areas that might require attention.

* Tracks performance indicators such as query execution times, resource utilization, and connection issues.
* Highlights anomalies and potential risks affecting database reliability.

### Analyze and optimize query performance

Queries are often the root cause of database inefficiencies. The app provides tools to analyze query execution and identify areas for improvement. This ensures that your databases can handle workloads effectively.

* Detects slow or inefficient queries that impact database performance.
* Provides recommendations for query optimizations, such as rewriting queries or adding indexes to improve performance.
* Offers detailed execution plans to help you understand how queries interact with your database.

### Detect and resolve database issues

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** helps you address problems before they affect your database operations. The app uses Dynatrace AI capabilities to identify issues, analyze their root causes, and suggest actionable solutions.

* Detects anomalies in database behavior using AI-powered analysis.
* Pinpoints root causes of performance degradation or failures.
* Recommends remediation steps, such as configuration changes or query optimizations, based on actionable insights.

### Integrate with Dynatrace for end-to-end observability

![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** is part of the Dynatrace ecosystem and provides comprehensive observability across your entire technology stack. The app integrates with other Dynatrace tools to provide a unified view of your database and its dependencies.

* **Grail**: Processes large volumes of data for scalable analytics.
* **Smartscape**: Maps real-time dependencies for context-aware analysis.
* **Davis AI**: Detects anomalies and provides intelligent recommendations.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Get an overview of all your extension-monitored databases.](https://www.dynatrace.com/hub/detail/database-overview/?utm_source=doc&utm_medium=link&utm_campaign=cross)

## Databases documentation overview

[01Get started with database monitoring

* How-to guide](/docs/observe/infrastructure-observability/databases/database-app/get-started)[02Data collected with Dynatrace database monitoring

* Reference](/docs/observe/infrastructure-observability/databases/database-app/data-collected)


---


## Source: analyze-database-services-new.md


---
title: Analyze database services (new page)
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services-new
scraped: 2026-02-17T21:29:24.017830
---

# Analyze database services (new page)

# Analyze database services (new page)

* Explanation
* 5-min read
* Published Jun 20, 2023

We have redesigned the database overview page.

* This documentation describes the new design.
* If you want to revert to the classic database page, on the database overview page select **More** (**â¦**) > **Return to classic page** and then refer to the [documentation for the classic database page](/docs/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services "Analyze your database services with Dynatrace (classic page).").

All databases detected by Dynatrace in your environment are displayed on the **Databases** page. You can analyze each database and drill down to code-level information.

How to get there:

1. Go to ![Databases Services Classic](https://dt-cdn.net/images/databases-512-6aa6fff194.png "Databases Services Classic") **Database Services Classic**.
2. Select a database name in the list to go to that database's overview page.

Each **Database** page lists the most important information for that database.

![Database overview | Unified analysis](https://dt-cdn.net/images/database-ua-overview-3502-2a520ae771.png)

All relevant database metrics are shown on a single page, which is divided into several logical sections. Other panes of the database overview page show database performance and serve as entry points to deeper analysis.

## Notifications bar

The database notifications bar gives you a quick overview of the database state. Select a notification item to display more information.

### Properties and tags

Select **Properties and tags** on the notifications bar to display the **Properties and tags** panel, which displays metadata about the selected database:

* **Tags** lists tags currently applied to the database.  
  Select **Add Tag** to add a tag to the database metadata.
* **Properties** lists various database properties, such as application name, database type, technologies, and management zones.

### Problems

* On the notifications bar, **Problems** indicates active and closed problems related to the selected database.
* Select **Problems** on the notifications bar to display the **Problems** panel, which lists the problems.

  + Select a problem to display details.
  + Select **Go to problems** to go to the [Problems](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") page filtered by the selected database.

### SLOs

* On the notifications bar, **SLOs** indicates the current number of [SLOs](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") related to the selected database.
* Select **SLOs** on the notifications bar to display the **Service-level objectives** panel, which lists SLOs that are directly or indirectly connected to the database.

#### Directly connected SLOs

* An SLO is directly connected to a service when the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO meets the following criteria:

  + The entity type is set to `"DATABASE"`.
  + The entity ID is set to the database ID.
* To see only SLOs that are directly connected to the database, make sure that **Show only directly connected SLOs** is turned on.

#### Indirectly connected SLOs

* An SLO isn't directly connected to a database when, in the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") of an SLO, no entity ID is provided.

  Example: When generic values such as `type("DATABASE"),tag("slo")` are provided, the query results in all SLOs for all databases, including the current database.
* To see SLOs that are not directly connected to the database, turn off **Show only directly connected SLOs**.

#### Options

* Expand **Details** to view a chart of the respective SLO metrics.
* In **Actions**, select

  + **View in Data Explorer** to [see SLO metrics in Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** to [pin the SLO to your dashboard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **SLO definition** to edit the SLO in **Service-level objective definitions**.
  + **Clone** to [clone the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** to [create an alert for the SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

#### No SLOs

If no SLOs are found, you can

* Select a different timeframe in the upper-right corner.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Select **Add SLO** to create an SLO in the [SLO wizard](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

### Database availability

Select **Database availability** on the notifications bar to display a chart summarizing any detected availability issue for the database in the selected timeframe.

### Owners

Select **Owners** on the notifications bar to display the **Ownership** panel, which lists [owners](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") of the selected database.

* Select  to learn more about the current ownership.
* To add an ownership tag, select **Add Ownership tag**.

## Performance

### Database service overview

You can configure the **Database service overview** section to focus on various metrics of the database performance. For each metric, you can select **More** (**â¦**) and

* Analyze the metric in Data Explorer.
* Create a metric event.
* Pin the metric to a classic dashboard. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

### Topology

In the **Topology** section, you can learn

* The services that are calling the database and the services that are called by the database.  
  Select **Related services** to understand the service relation. Expand **Details** to view a chart of the respective service metrics. To proceed with your analysis, you can select [**View backtrace**](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").
* The processes and hosts on which the service is running.  
  Expand **Details** to view a chart of the respective process metrics. Select the name of the process to analyze it.

### Statement types

Contains an overview of statement types found for the database in the selected timeframe.

* Expand **Details** to view a chart of the respective statement.
* Select the name of a statement type to analyze the database statements filtered by the selected type.
* Select **View all statements** to analyze all statements for the database.

### Distributed traces

The **Distributed traces** section provides an overview of the most recent traces for the selected timeframe. Select **Full search** to go to the [distributed traces overview for the database](/docs/observe/application-observability/distributed-traces/analysis/get-started "Get started with distributed trace analysis in Dynatrace.").

### Events

Lists [events](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.") that affect the database in the current timeframe.

### Related logs

Lists [logs](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") related to the database in the current timeframe.

* To analyze all the logs for the related database, select **Go to logs** .
* To analyze a specific log, expand **Details**. If a trace or a user session is found for the log line, you can directly access it from this view.

## Related topics

* [Unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")


---


## Source: improve-database-performance.md


---
title: Improve database performance
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance
scraped: 2026-02-17T21:34:29.060112
---

# Improve database performance

# Improve database performance

* How-to guide
* 6-min read
* Published Mar 20, 2019

Databases are sophisticated applications, and database access is a core feature of many applications. To avoid failures or poor performance, it's important that your databases be hosted securely and resourced well enough to perform at their best.

You can optimize your databases with:

* Server data that supports host health monitoring
* Hypervisor and virtual machine metrics that support monitoring of your virtualization layer
* Application data that optimizes database access
* Network data that provides insight into the network impact of database communications

With the following few steps for simple database performance tuning, you can significantly speed up most applications.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Check the health of your database**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#database-health "Boost your database performance in a few practical steps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Understand how your database is accessed**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#database-access "Boost your database performance in a few practical steps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Understand the load and individual response time of each service instance**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#load-and-response-time "Boost your database performance in a few practical steps.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Check the number of database connections**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#database-connections "Boost your database performance in a few practical steps.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Check your network**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#check-network "Boost your database performance in a few practical steps.")

## Step 1 Check the health of your database

The first step is to ensure that the host serving your database process has sufficient resources such as CPU, memory, and disk space.

### CPU

* Equip each host with a minimum of two CPU cores. Matching the CPU count of your host helps with:

  + Ensuring host responsiveness, because database servers induce a continuous base load on machines.
  + Preventing overspending or hardware limitations, because database-server licensing is affected by the number of CPUs.
* When monitoring virtual machines, monitor the host that the virtual machines run on as well. This provides a more complete picture than the CPU metrics of individual virtual machines, which generate insights only on the respective CPU time availability.

  ![CPU metrics](https://dt-cdn.net/images/cpu-1198-a20fe73396.png)

### Memory

* In addition to monitoring the **Memory usage** metric, monitor **Page faults** per second to learn how much additional memory is required. Having thousands of page faults per second indicates that your host is out of memory.

  ![Host memory usage](https://dt-cdn.net/images/host-memory-analysis-page-faults-2372-02f34bdaa5.png)

### Disk space

* Ensure that storage availability for your database server is higher than the disk space required for the data.

  Because of indices and other performance improvements, databases might use more disk space than required by the data itself. For example, NoSQL databases (such as Cassandra and MongoDB) consume a lot more disk space than expected. Compared to common SQL databases, MongoDB databases might consume less RAM but more disk space.
* Ensure that your database runs on dedicated hard drives to reduce disk fragmentation caused by other processes.
* Check **Disk latency**.

  Depending on the hard drive load, disk latency can increase, leading to a reduction in database performance. You can prevent high disk latency by leveraging the caching mechanisms of your application and database as much as possible.

  ![Disk latency](https://dt-cdn.net/images/host-disk-latency-2060-80803a8edc.png)
* If the results of the measures above aren't satisfactory, consider the following.

  1. Add additional hard drives.

     Read performance can be multiplied by simply mirroring hard drives. Write performance benefits from using RAID 1 or RAID 10 instead of RAID 6.
  2. Try solid-state drives.

     Ensure that you select a model designed for database usage, because databases apply more read/write cycles to storage than most common applications. Solid-state drives are more expensive than traditional hard disks but offer a substantial boost in performance.

## Step 2 Understand how your database is accessed

Once your database resides on healthy hardware, take a look at the applications that access it. If you know of an application or service that has bad database performance, donât assume that it's the application that's affecting the performance of your databaseâit may be another application or service entirely.

![Database overview | Unified analysis](https://dt-cdn.net/images/database-ua-overview-3502-2a520ae771.png)

Reduction in database performance can affect the entire database or a single client.

* If all clients experience bad performance, check if the host is healthy. In most cases, the cause is hardware that isn't capable of handling the work.
* If only a single service suffers from poor response times, dig deeper into the serviceâs metrics to find the root cause of the problem.

## Step 3 Understand the load and individual response time of each service instance

When a service has poor database performance, you can analyze its communication with the database via **database statements**. You can gain insights into the number of executed queries, the query execution frequency per request, the number of rows each query returns, and so on.

![Database details page](https://dt-cdn.net/images/database-details-page-1293-85e42be938.png)

* If you're running multiple **service instances**, check if all the instances are affected rather than a single service instance.

* Check how often the queries are called per request. You might be able to reduce the number of database queries by improving the database cache of your service. If a single query is executed more than once per request, you can unlock potential performance by applying smart caching strategies.

## Step 4 Check the number of database connections

You might continue to face poor database performance even when database queries are correctly configured. In such cases, check that the applicationâs database connection pool is correctly sized.

When configuring a connection pool, consider the following:

* The maximum number of connections the database can handle
* The correct size connection pool required for the application

Because your application may not be the only client connected to the database, ensure that the connection pool size isn't set to the maximum. If the application takes up all the connections, the database server wonât perform as expected.

How to determine the maximum number of connections

The maximum number of connections to the database is a function of the resources in the database. To find the maximum number of connections, gradually increase the load and the number of allowed connections to your database.

While doing this, keep an eye on your database serverâs metrics: CPU, memory, and disk performance. Once any of these maxes out, youâve reached the limit. If the number of available connections isn't enough for your application, consider upgrading your hardware.

To learn more about the database connection pool size, see [About Pool Sizingï»¿](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing).

How to determine the correct size for your application connection pool

The number of allowed concurrent connections to your database is equivalent to the amount of parallel load that your application applies to the database server. There are certain tools that you can use to determine the right number.

Increasing the load leads to higher transaction response times, even if your database server is healthy. Measure the transaction response time from end-to-end to see if **Connection acquisition** time increases under heavy load. If that's the case, your connection pool may be exhausted. If not, review your database server metrics to determine the maximum number of connections that your database can handle.

A connection poolâs size should be constant. Therefore, set the minimum and maximum pool sizes to the same value.

## Step 5 Check your network

Physical constraints of your virtualized infrastructure can affect database performance; cables can fail and routers can break. Network metrics generate insights into non-virtual problems. For example, if problems appear after months or even years of flawless operation, your infrastructure might be suffering physical problems. Check your routers, cables, and network interfaces.

![Host process analysis](https://dt-cdn.net/images/host-process-analysis-1922-6b4f5157a1.png)

Most often, over-stressed processes start dropping packets when resources are depleted. If your network issue isn't hardware based, process-level visibility can help you identify any failing component.

## Related topics

* [Host monitoring with Dynatrace](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.")


---


## Source: support-for-sql-bind-variables.md


---
title: Support for SQL bind variables
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-services-classic/support-for-sql-bind-variables
scraped: 2026-02-17T21:32:41.030668
---

# Support for SQL bind variables

# Support for SQL bind variables

* How-to guide
* 4-min read
* Updated on Apr 26, 2023

Bind variables are a means of parameterizing SQL statements so that the statements have question marks or parameters in their **where** clauses, such as:

* SQL server: `select count (*) from report where tenant = @tenant`
* Java JDBC: `select count (*) from report where tenant = ?`

Bind variables allow the database server to prepare the statement once and execute it multiple times without reparsing or reanalyzing it.

Bind variables aren't applicable to statements that use literals, such as:

```
select count (*) from report where tenant = âxxxxâ
```

These statements can't be parameterized and are reparsed and reanalyzed by the database server with each execution.

Bind variables generate high network and storage demands. To learn more about bind variables support and its availability, see [FAQ](#faq) below.

## Enable capture of SQL bind variables

To enable SQL bind value capture

1. Go to **Settings** > **Server-side service monitoring** > **Deep monitoring**.
2. Expand **Database** and turn on/off **Capture SQL bind values** on the global level.
3. Optional To override the global setup, go to **Process group override**.

   1. To add an override, select **Add process group override** and select the affected process group.
   2. Optional To select a specific process from the selected process group, select the process from the dropdown list.
   3. Select **Add**.
4. Select **Save changes**.

![Capture SQL bind values](https://dt-cdn.net/images/capture-sql-bind-values-942-067033b12f.png)

Whether you enable this setting site-wide or for individual process groups, you can use Dynatrace OneAgent to capture the values of bind variables. This is applicable to the following technologies:

* ADO.net
* JDBC
* PHP database frameworks

If the array returned by `executeBatch()` contains more than one element, indicating multiple commands were executed, Dynatrace masks the values of the bind variables to ensure data privacy. This is because different executions of `executeBatch()` may aggregate multiple commands, necessitating the masking of bind variable values to prevent the exposure of sensitive information.

## Example of masked and unmasked SQL bind values

A sample result of this feature is distributed tracing. The following webpage illustrates the masking of bind variables.

![Purepath example](https://dt-cdn.net/images/purepath-example-1413-383ad7b07c.png)

Bind variables are considered confidential as they can contain IDs and other sensitive values. [Learn how to ensure the data privacy of your customers](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

Only users who have permission to view a specific entity or management zone can view the bind variables within that entity or zone.

![Purepath example for authorized users](https://dt-cdn.net/images/purepath-example-for-authorized-users-1413-46e0584d5a.png)

## FAQ

Bind variables are not available in my Dynatrace environment. How do I get this feature?

This feature is available in Dynatrace environments that are licensed via [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."). If you have a Dynatrace classic license, change your subscription plan to a Dynatrace Platform Subscription (DPS) license to use bind variables.

Does capturing bind variables have negative consequences?

This feature can capture a lot of sensitive data, so you should consider its usage carefully.
You might also choose to mask or drop parts of the captured data via [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.").

Additionally, this feature can capture a lot of data in the absolute sense.
Heavy usage of this feature means that you will run out of the included trace volume for your Full-Stack monitored applications faster.
In other words, heavy usage can lower your trace capture rate.
To mitigate this, you should either use this feature for troubleshooting only or you can opt into [Extended trace ingest](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#extend-trace-ingest "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") to accommodate the increased data volume.


---


## Source: varnish-cache-1.md


---
title: Varnish Cache extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/extensions/varnish-cache-1
scraped: 2026-02-17T04:51:15.178455
---

# Varnish Cache extension

# Varnish Cache extension

* Latest Dynatrace
* Extension
* Updated on Dec 04, 2025

Monitor Varnish Cache performance to optimize content delivery and reduce response times.

## Get started

### Overview

Monitor the statistics of Varnish Cache instances.

### Use cases

* Monitor the health and state of Varnish cache instances.
* Detect and alert on anomalous behavior.
* Understand the load and operational performance of the cache.

### Requirements

* OneAgent must be installed on the host with the Varnish Cache instance to be monitored.
* `varnishstat` binary must be present on the host.
* OneAgent user must be able to execute the binary on the host.
* Before running the `sudo varnishstat` command, make sure `dtuser` has sudo permissions and is set up for passwordless access in the `sudoers` file.

### Compatibility information

Varnish version 6.2.1+.

## Details

* Out-of-the-box metrics

Varnish Cache system performance metrics (CPU, memory, and more) are available with no additional configuration when using OneAgent on a server running Dynatrace OneAgent.

You also get details about network traffic, TCP requests, and connectivity, along with quality metrics such as retransmissions, round-trip time, and throughput.

* Advanced Varnish Cache server metrics such as

  + Cache performance
  + Backend metrics
  + Client metrics
  + Thread metrics are **not** available out of the box in Dynatrace.

This extension collects the above advanced Varnish Cache server metrics by executing the `varnishstat` command and then sending the resulting output back to Dynatrace.

### Licensing and cost

* DPS:

`((20 * #_of_backends) + (7 * #_of_malloc_stevedores) + (7 * #_of_umem_stevedores) + (10 * #_of_file_stevedores) + 198)`

* DDUs:

`((20 * #_of_backends) + (7 * #_of_malloc_stevedores) + (7 * #_of_umem_stevedores) + (10 * #_of_file_stevedores) + 198) * 0.001`

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

mempool

| Metric name | Metric key | Description |
| --- | --- | --- |
| In use | varnish.cache.mempool.live | In use |
| In Pool | varnish.cache.mempool.pool | In Pool |
| Size requested | varnish.cache.mempool.sz\_wanted | Size requested |
| Size allocated | varnish.cache.mempool.sz\_actual | Size allocated |
| Allocations | varnish.cache.mempool.allocs.count | Allocations |
| Frees | varnish.cache.mempool.frees.count | Frees |
| Recycled from pool | varnish.cache.mempool.recycle.count | Recycled from pool |
| Timed out from pool | varnish.cache.mempool.timeout.count | Timed out from pool |
| Too small to recycle | varnish.cache.mempool.toosmall.count | Too small to recycle |
| Too many for pool | varnish.cache.mempool.surplus.count | Too many for pool |
| Pool ran dry | varnish.cache.mempool.randry.count | Pool ran dry |

lck

| Metric name | Metric key | Description |
| --- | --- | --- |
| Created locks | varnish.cache.lck.creat.count | Created locks |
| Destroyed locks | varnish.cache.lck.destroy.count | Destroyed locks |
| Lock Operations | varnish.cache.lck.locks.count | Lock Operations |
| Contended lock operations | varnish.cache.lck.dbg\_busy.count | If the lck debug bit is set: Lock operations which returned EBUSY on the first locking attempt. If the lck debug bit is unset, this counter will never be incremented even if lock operations are contended. |
| Contended trylock operations | varnish.cache.lck.dbg\_try\_fail.count | If the lck debug bit is set: Trylock operations which returned EBUSY. If the lck debug bit is unset, this counter will never be incremented even if lock operations are contended. |

vbe

| Metric name | Metric key | Description |
| --- | --- | --- |
| Happy health probes | varnish.cache.vbe.happy | Represents the last probe results as a bitmap. Happy probes are bits set to 1, and the unhappy ones are set to 0. The highest bits represent the oldest probes. |
| Request header bytes | varnish.cache.vbe.bereq\_hdrbytes.count | Total backend request header bytes sent |
| Request body bytes | varnish.cache.vbe.bereq\_bodybytes.count | Total backend request body bytes sent |
| Response header bytes | varnish.cache.vbe.beresp\_hdrbytes.count | Total backend response header bytes received |
| Response body bytes | varnish.cache.vbe.beresp\_bodybytes.count | Total backend response body bytes received |
| Pipe request header bytes | varnish.cache.vbe.pipe\_hdrbytes.count | Total request bytes sent for piped sessions |
| Piped bytes to backend | varnish.cache.vbe.pipe\_out.count | Total number of bytes forwarded to backend in pipe sessions |
| Piped bytes from backend | varnish.cache.vbe.pipe\_in.count | Total number of bytes forwarded from backend in pipe sessions |
| Concurrent connections used | varnish.cache.vbe.conn | The number of currently used connections to the backend. This number is always less or equal to the number of connections to the backend (as, for example shown as ESTABLISHED for TCP connections in netstat) due to connection pooling. |
| Backend requests sent | varnish.cache.vbe.req.count | Backend requests sent |
| Fetches not attempted due to backend being unhealthy | varnish.cache.vbe.unhealthy.count | Fetches not attempted due to backend being unhealthy |
| Fetches not attempted due to backend being busy | varnish.cache.vbe.busy.count | Number of times the max\_connections limit was reached .. === Anything below is actually per VCP entry, but collected per === backend for simplicity |
| Connections failed | varnish.cache.vbe.fail.count | Counter of failed opens. Detailed reasons are given in the fail\_\* counters (DIAG level) and in the log under the FetchError tag. This counter is the sum of all detailed fail\_\* counters. All fail\_\* counters may be slightly inaccurate for efficiency. |
| Connections failed with EACCES or EPERM | varnish.cache.vbe.fail\_eacces.count | Connections failed with EACCES or EPERM |
| Connections failed with EADDRNOTAVAIL | varnish.cache.vbe.fail\_eaddrnotavail.count | Connections failed with EADDRNOTAVAIL |
| Connections failed with ECONNREFUSED | varnish.cache.vbe.fail\_econnrefused.count | Connections failed with ECONNREFUSED |
| Connections failed with ENETUNREACH | varnish.cache.vbe.fail\_enetunreach.count | Connections failed with ENETUNREACH |
| Connections failed ETIMEDOUT | varnish.cache.vbe.fail\_etimedout.count | Connections failed ETIMEDOUT |
| Connections failed for other reason | varnish.cache.vbe.fail\_other.count | Connections failed for other reason |
| Connection opens not attempted | varnish.cache.vbe.helddown.count | Connections not attempted during the backend\_local\_error\_holddown or backend\_remote\_error\_holddown interval after a fundamental connection issue. |

mgt

| Metric name | Metric key | Description |
| --- | --- | --- |
| Management process uptime | varnish.cache.mgt.uptime.count | Uptime in seconds of the management process |
| Child process started | varnish.cache.mgt.child\_start.count | Number of times the child process has been started |
| Child process normal exit | varnish.cache.mgt.child\_exit.count | Number of times the child process has been cleanly stopped |
| Child process unexpected exit | varnish.cache.mgt.child\_stop.count | Number of times the child process has exited with an unexpected return code |
| Child process died (signal) | varnish.cache.mgt.child\_died.count | Number of times the child process has died due to signals |
| Child process core dumped | varnish.cache.mgt.child\_dump.count | Number of times the child process has produced core dumps |
| Child process panic | varnish.cache.mgt.child\_panic.count | Number of times the management process has caught a child panic |

default

| Metric name | Metric key | Description |
| --- | --- | --- |
| Return code | varnish.cache.returncode | Return code of the varnishstat command |

smf

| Metric name | Metric key | Description |
| --- | --- | --- |
| Allocator requests | varnish.cache.smf.c\_req.count | Number of times the storage has been asked to provide a storage segment. |
| Allocator failures | varnish.cache.smf.c\_fail.count | Number of times the storage has failed to provide a storage segment. |
| Bytes allocated | varnish.cache.smf.c\_bytes.count | Number of total bytes allocated by this storage. |
| Bytes freed | varnish.cache.smf.c\_freed.count | Number of total bytes returned to this storage. |
| Allocations outstanding | varnish.cache.smf.g\_alloc | Number of storage allocations outstanding. |
| Bytes outstanding | varnish.cache.smf.g\_bytes | Number of bytes allocated from the storage. |
| Bytes available | varnish.cache.smf.g\_space | Number of bytes left in the storage. |
| N struct smf | varnish.cache.smf.g\_smf | N struct smf |
| N small free smf | varnish.cache.smf.g\_smf\_frag | N small free smf |
| N large free smf | varnish.cache.smf.g\_smf\_large | N large free smf |

smu

| Metric name | Metric key | Description |
| --- | --- | --- |
| Allocator requests | varnish.cache.smu.c\_req.count | Number of times the storage has been asked to provide a storage segment. |
| Allocator failures | varnish.cache.smu.c\_fail.count | Number of times the storage has failed to provide a storage segment. |
| Bytes allocated | varnish.cache.smu.c\_bytes.count | Number of total bytes allocated by this storage. |
| Bytes freed | varnish.cache.smu.c\_freed.count | Number of total bytes returned to this storage. |
| Allocations outstanding | varnish.cache.smu.g\_alloc | Number of storage allocations outstanding. |
| Bytes outstanding | varnish.cache.smu.g\_bytes | Number of bytes allocated from the storage. |
| Bytes available | varnish.cache.smu.g\_space | Number of bytes left in the storage. |

sma

| Metric name | Metric key | Description |
| --- | --- | --- |
| Allocator requests | varnish.cache.sma.c\_req.count | Number of times the storage has been asked to provide a storage segment. |
| Allocator failures | varnish.cache.sma.c\_fail.count | Number of times the storage has failed to provide a storage segment. |
| Bytes allocated | varnish.cache.sma.c\_bytes.count | Number of total bytes allocated by this storage. |
| Bytes freed | varnish.cache.sma.c\_freed.count | Number of total bytes returned to this storage. |
| Allocations outstanding | varnish.cache.sma.g\_alloc | Number of storage allocations outstanding. |
| Bytes outstanding | varnish.cache.sma.g\_bytes | Number of bytes allocated from the storage. |
| Bytes available | varnish.cache.sma.g\_space | Number of bytes left in the storage. |

main

| Metric name | Metric key | Description |
| --- | --- | --- |
| stat summ operations | varnish.cache.main.summs.count | Number of times per-thread statistics were summed into the global counters. |
| Child process uptime | varnish.cache.main.uptime.count | How long the child process has been running. |
| Sessions accepted | varnish.cache.main.sess\_conn.count | Count of sessions successfully accepted |
| Session accept failures | varnish.cache.main.sess\_fail.count | Count of failures to accept TCP connection. This counter is the sum of the sess\_fail\_\* counters, which give more detailed information. |
| Session accept failures: connection aborted | varnish.cache.main.sess\_fail\_econnaborted.count | Detailed reason for sess\_fail: Connection aborted by the client, usually harmless. |
| Session accept failures: interrupted system call | varnish.cache.main.sess\_fail\_eintr.count | Detailed reason for sess\_fail: The accept() call was interrupted, usually harmless |
| Session accept failures: too many open files | varnish.cache.main.sess\_fail\_emfile.count | Detailed reason for sess\_fail: No file descriptor was available. Consider raising RLIMIT\_NOFILE (see ulimit -n). |
| Session accept failures: bad file descriptor | varnish.cache.main.sess\_fail\_ebadf.count | Detailed reason for sess\_fail: The listen socket file descriptor was invalid. Should never happen. |
| Session accept failures: not enough memory | varnish.cache.main.sess\_fail\_enomem.count | Detailed reason for sess\_fail: Most likely insufficient socket buffer memory. Should never happen |
| Session accept failures: other | varnish.cache.main.sess\_fail\_other.count | Detailed reason for sess\_fail: neither of the above, see SessError log (varnishlog -g raw -i SessError). |
| Client requests received, subject to 400 errors | varnish.cache.main.client\_req\_400.count | 400 means we couldn't make sense of the request, it was malformed in some drastic way. |
| Client requests received, subject to 417 errors | varnish.cache.main.client\_req\_417.count | 417 means that something went wrong with an Expect: header. |
| Good client requests received | varnish.cache.main.client\_req.count | The count of parseable client requests seen. |
| ESI subrequests | varnish.cache.main.esi\_req.count | Number of ESI subrequests made. |
| Cache hits | varnish.cache.main.cache\_hit.count | Count of cache hits. A cache hit indicates that an object has been delivered to a client without fetching it from a backend server. |
| Cache grace hits | varnish.cache.main.cache\_hit\_grace.count | Count of cache hits with grace. A cache hit with grace is a cache hit where the object is expired. Note that such hits are also included in the cache\_hit counter. |
| Cache hits for pass. | varnish.cache.main.cache\_hitpass.count | Count of hits for pass. A cache hit for pass indicates that Varnish is going to pass the request to the backend and this decision has been cached in it self. This counts how many times the cached decision is being used. |
| Cache hits for miss. | varnish.cache.main.cache\_hitmiss.count | Count of hits for miss. A cache hit for miss indicates that Varnish is going to proceed as for a cache miss without request coalescing, and this decision has been cached. This counts how many times the cached decision is being used. |
| Cache misses | varnish.cache.main.cache\_miss.count | Count of misses. A cache miss indicates the object was fetched from the backend before delivering it to the client. |
| Uncacheable backend responses | varnish.cache.main.beresp\_uncacheable.count | Count of backend responses considered uncacheable. |
| Shortlived objects | varnish.cache.main.beresp\_shortlived.count | Count of objects created with ttl+grace+keep shorter than the 'shortlived' runtime parameter. |
| Backend conn. success | varnish.cache.main.backend\_conn.count | How many backend connections have successfully been established. |
| Backend conn. not attempted | varnish.cache.main.backend\_unhealthy.count | Backend conn. not attempted |
| Backend conn. too many | varnish.cache.main.backend\_busy.count | Backend conn. too many |
| Backend conn. failures | varnish.cache.main.backend\_fail.count | Backend conn. failures |
| Backend conn. reuses | varnish.cache.main.backend\_reuse.count | Count of backend connection reuses. This counter is increased whenever we reuse a recycled connection. |
| Backend conn. recycles | varnish.cache.main.backend\_recycle.count | Count of backend connection recycles. This counter is increased whenever we have a keep-alive connection that is put back into the pool of connections. It has not yet been used, but it might be, unless the backend closes it. |
| Backend conn. retry | varnish.cache.main.backend\_retry.count | Backend conn. retry |
| Fetch no body (HEAD) | varnish.cache.main.fetch\_head.count | beresp with no body because the request is HEAD. |
| Fetch with Length | varnish.cache.main.fetch\_length.count | beresp.body with Content-Length. |
| Fetch chunked | varnish.cache.main.fetch\_chunked.count | beresp.body with Chunked. |
| Fetch EOF | varnish.cache.main.fetch\_eof.count | beresp.body with EOF. |
| Fetch bad T-E | varnish.cache.main.fetch\_bad.count | beresp.body length/fetch could not be determined. |
| Fetch no body | varnish.cache.main.fetch\_none.count | beresp.body empty |
| Fetch no body (1xx) | varnish.cache.main.fetch\_1xx.count | beresp with no body because of 1XX response. |
| Fetch no body (204) | varnish.cache.main.fetch\_204.count | beresp with no body because of 204 response. |
| Fetch no body (304) | varnish.cache.main.fetch\_304.count | beresp with no body because of 304 response. |
| Fetch failed (all causes) | varnish.cache.main.fetch\_failed.count | beresp fetch failed. |
| Background fetch failed (no thread) | varnish.cache.main.bgfetch\_no\_thread.count | A bgfetch triggered by a grace hit failed, no thread available. |
| Number of thread pools | varnish.cache.main.pools | Number of thread pools. See also parameter thread\_pools. NB: Presently pools cannot be removed once created. |
| Total number of threads | varnish.cache.main.threads | Number of threads in all pools. See also parameters thread\_pools, thread\_pool\_min and thread\_pool\_max. |
| Threads hit max | varnish.cache.main.threads\_limited.count | Number of times more threads were needed, but limit was reached in a thread pool. See also parameter thread\_pool\_max. |
| Threads created | varnish.cache.main.threads\_created.count | Total number of threads created in all pools. |
| Threads destroyed | varnish.cache.main.threads\_destroyed.count | Total number of threads destroyed in all pools. |
| Thread creation failed | varnish.cache.main.threads\_failed.count | Number of times creating a thread failed. See VSL::Debug for diagnostics. See also parameter thread\_fail\_delay. |
| Length of session queue | varnish.cache.main.thread\_queue\_len | Length of session queue waiting for threads. NB: Only updates once per second. See also parameter thread\_queue\_limit. |
| Number of requests sent to sleep on busy objhdr | varnish.cache.main.busy\_sleep.count | Number of requests sent to sleep without a worker thread because they found a busy object. |
| Number of requests woken after sleep on busy objhdr | varnish.cache.main.busy\_wakeup.count | Number of requests taken off the busy object sleep list and rescheduled. |
| Number of requests killed after sleep on busy objhdr | varnish.cache.main.busy\_killed.count | Number of requests killed from the busy object sleep list due to lack of resources. |
| Sessions queued for thread | varnish.cache.main.sess\_queued.count | Number of times session was queued waiting for a thread. See also parameter thread\_queue\_limit. |
| Sessions dropped for thread | varnish.cache.main.sess\_dropped.count | Number of times an HTTP/1 session was dropped because the queue was too long already. See also parameter thread\_queue\_limit. |
| Requests dropped | varnish.cache.main.req\_dropped.count | Number of times an HTTP/2 stream was refused because the queue was too long already. See also parameter thread\_queue\_limit. |
| object structs made | varnish.cache.main.n\_object | Approximate number of HTTP objects (headers + body, if present) in the cache. |
| unresurrected objects | varnish.cache.main.n\_vampireobject | Number of unresurrected objects |
| objectcore structs made | varnish.cache.main.n\_objectcore | Approximate number of object metadata elements in the cache. Each object needs an objectcore, extra objectcores are for hit-for-miss, hit-for-pass and busy objects. |
| objecthead structs made | varnish.cache.main.n\_objecthead | Approximate number of different hash entries in the cache. |
| Number of backends | varnish.cache.main.n\_backend | Number of backends known to us. |
| Number of expired objects | varnish.cache.main.n\_expired.count | Number of objects that expired from cache because of old age. |
| Number of LRU nuked objects | varnish.cache.main.n\_lru\_nuked.count | How many objects have been forcefully evicted from storage to make room for a new object. |
| Number of LRU moved objects | varnish.cache.main.n\_lru\_moved.count | Number of move operations done on the LRU list. |
| Reached nuke\_limit | varnish.cache.main.n\_lru\_limited.count | Number of times more storage space were needed, but limit was reached in a nuke\_limit. See also parameter nuke\_limit. |
| HTTP header overflows | varnish.cache.main.losthdr.count | HTTP header overflows |
| Total sessions seen | varnish.cache.main.s\_sess.count | Total sessions seen |
| Number of ongoing pipe sessions | varnish.cache.main.n\_pipe | Number of ongoing pipe sessions |
| Pipes hit pipe\_sess\_max | varnish.cache.main.pipe\_limited.count | Number of times more pipes were needed, but the limit was reached. See also parameter pipe\_sess\_max. |
| Total pipe sessions seen | varnish.cache.main.s\_pipe.count | Total pipe sessions seen |
| Total pass-ed requests seen | varnish.cache.main.s\_pass.count | Total pass-ed requests seen |
| Total backend fetches initiated | varnish.cache.main.s\_fetch.count | Total backend fetches initiated, including background fetches. |
| Total backend background fetches initiated | varnish.cache.main.s\_bgfetch.count | Total backend background fetches initiated |
| Total synthetic responses made | varnish.cache.main.s\_synth.count | Total synthetic responses made |
| Request header bytes | varnish.cache.main.s\_req\_hdrbytes.count | Total request header bytes received |
| Request body bytes | varnish.cache.main.s\_req\_bodybytes.count | Total request body bytes received |
| Response header bytes | varnish.cache.main.s\_resp\_hdrbytes.count | Total response header bytes transmitted |
| Response body bytes | varnish.cache.main.s\_resp\_bodybytes.count | Total response body bytes transmitted |
| Pipe request header bytes | varnish.cache.main.s\_pipe\_hdrbytes.count | Total request bytes received for piped sessions |
| Piped bytes from client | varnish.cache.main.s\_pipe\_in.count | Total number of bytes forwarded from clients in pipe sessions |
| Piped bytes to client | varnish.cache.main.s\_pipe\_out.count | Total number of bytes forwarded to clients in pipe sessions |
| Session Closed | varnish.cache.main.sess\_closed.count | Session Closed |
| Session Closed with error | varnish.cache.main.sess\_closed\_err.count | Total number of sessions closed with errors. See sc\_\* diag counters for detailed breakdown |
| Session Read Ahead | varnish.cache.main.sess\_readahead.count | Session Read Ahead |
| Session herd | varnish.cache.main.sess\_herd.count | Number of times the timeout\_linger triggered |
| Session OK REM\_CLOSE | varnish.cache.main.sc\_rem\_close.count | Number of session closes with REM\_CLOSE (Client Closed) |
| Session OK REQ\_CLOSE | varnish.cache.main.sc\_req\_close.count | Number of session closes with REQ\_CLOSE (Client requested close) |
| Session Err REQ\_HTTP10 | varnish.cache.main.sc\_req\_http10.count | Number of session closes with Error REQ\_HTTP10 (Proto < HTTP/1.1) |
| Session Err RX\_BAD | varnish.cache.main.sc\_rx\_bad.count | Number of session closes with Error RX\_BAD (Received bad req/resp) |
| Session Err RX\_BODY | varnish.cache.main.sc\_rx\_body.count | Number of session closes with Error RX\_BODY (Failure receiving req.body) |
| Session Err RX\_JUNK | varnish.cache.main.sc\_rx\_junk.count | Number of session closes with Error RX\_JUNK (Received junk data) |
| Session Err RX\_OVERFLOW | varnish.cache.main.sc\_rx\_overflow.count | Number of session closes with Error RX\_OVERFLOW (Received buffer overflow) |
| Session Err RX\_TIMEOUT | varnish.cache.main.sc\_rx\_timeout.count | Number of session closes with Error RX\_TIMEOUT (Receive timeout) |
| Session Err RX\_CLOSE\_IDLE | varnish.cache.main.sc\_rx\_close\_idle.count | Number of session closes with Error RX\_CLOSE\_IDLE: timeout\_idle has been exceeded while waiting for a client request. |
| Session OK TX\_PIPE | varnish.cache.main.sc\_tx\_pipe.count | Number of session closes with TX\_PIPE (Piped transaction) |
| Session Err TX\_ERROR | varnish.cache.main.sc\_tx\_error.count | Number of session closes with Error TX\_ERROR (Error transaction) |
| Session OK TX\_EOF | varnish.cache.main.sc\_tx\_eof.count | Number of session closes with TX\_EOF (EOF transmission) |
| Session OK RESP\_CLOSE | varnish.cache.main.sc\_resp\_close.count | Number of session closes with RESP\_CLOSE (Backend/VCL requested close) |
| Session Err OVERLOAD | varnish.cache.main.sc\_overload.count | Number of session closes with Error OVERLOAD (Out of some resource) |
| Session Err PIPE\_OVERFLOW | varnish.cache.main.sc\_pipe\_overflow.count | Number of session closes with Error PIPE\_OVERFLOW (Session pipe overflow) |
| Session Err RANGE\_SHORT | varnish.cache.main.sc\_range\_short.count | Number of session closes with Error RANGE\_SHORT (Insufficient data for range) |
| Session Err REQ\_HTTP20 | varnish.cache.main.sc\_req\_http20.count | Number of session closes with Error REQ\_HTTP20 (HTTP2 not accepted) |
| Session Err VCL\_FAILURE | varnish.cache.main.sc\_vcl\_failure.count | Number of session closes with Error VCL\_FAILURE (VCL failure) |
| Delivery failed due to insufficient workspace. | varnish.cache.main.client\_resp\_500.count | Number of times we failed a response due to running out of workspace memory during delivery. |
| workspace\_backend overflows | varnish.cache.main.ws\_backend\_overflow.count | Number of times we ran out of space in workspace\_backend. |
| workspace\_client overflows | varnish.cache.main.ws\_client\_overflow.count | Number of times we ran out of space in workspace\_client. |
| workspace\_thread overflows | varnish.cache.main.ws\_thread\_overflow.count | Number of times we ran out of space in workspace\_thread. |
| workspace\_session overflows | varnish.cache.main.ws\_session\_overflow.count | Number of times we ran out of space in workspace\_session. |
| SHM records | varnish.cache.main.shm\_records.count | Number of log records written to the shared memory log. |
| SHM writes | varnish.cache.main.shm\_writes.count | Number of individual writes to the shared memory log. A single write may batch multiple records for bufferred tasks. |
| SHM flushes due to overflow | varnish.cache.main.shm\_flushes.count | Number of writes performed before the end of a bufferred task because adding a record to a batch would exceed vsl\_buffer. |
| SHM lock contention | varnish.cache.main.shm\_cont.count | Number of times a write had to wait for the lock. |
| SHM cycles through VSL space | varnish.cache.main.shm\_cycles.count | Number of times a write of log records would reach past the end of the shared memory log, cycling back to the beginning. |
| SHM bytes | varnish.cache.main.shm\_bytes.count | Number of bytes written to the shared memory log. |
| Backend requests made | varnish.cache.main.backend\_req.count | Backend requests made |
| Number of loaded VCLs in total | varnish.cache.main.n\_vcl | Number of loaded VCLs in total |
| Number of VCLs available | varnish.cache.main.n\_vcl\_avail | Number of VCLs available |
| Number of discarded VCLs | varnish.cache.main.n\_vcl\_discard | Number of discarded VCLs |
| VCL failures | varnish.cache.main.vcl\_fail.count | Count of failures which prevented VCL from completing. |
| Count of bans | varnish.cache.main.bans | Number of all bans in system, including bans superseded by newer bans and bans already checked by the ban-lurker. |
| Number of bans marked 'completed' | varnish.cache.main.bans\_completed | Number of bans which are no longer active, either because they got checked by the ban-lurker or superseded by newer identical bans. |
| Number of bans using obj.\* | varnish.cache.main.bans\_obj | Number of bans which use obj.\* variables. These bans can possibly be washed by the ban-lurker. |
| Number of bans using req.\* | varnish.cache.main.bans\_req | Number of bans which use req.\* variables. These bans can not be washed by the ban-lurker. |
| Bans added | varnish.cache.main.bans\_added.count | Counter of bans added to ban list. |
| Bans deleted | varnish.cache.main.bans\_deleted.count | Counter of bans deleted from ban list. |
| Bans tested against objects (lookup) | varnish.cache.main.bans\_tested.count | Count of how many bans and objects have been tested against each other during hash lookup. |
| Objects killed by bans (lookup) | varnish.cache.main.bans\_obj\_killed.count | Number of objects killed by bans during object lookup. |
| Bans tested against objects (lurker) | varnish.cache.main.bans\_lurker\_tested.count | Count of how many bans and objects have been tested against each other by the ban-lurker. |
| Ban tests tested against objects (lookup) | varnish.cache.main.bans\_tests\_tested.count | Count of how many tests and objects have been tested against each other during lookup. 'ban req.url == foo && req.http.host == bar' counts as one in 'bans\_tested' and as two in 'bans\_tests\_tested' |
| Ban tests tested against objects (lurker) | varnish.cache.main.bans\_lurker\_tests\_tested.count | Count of how many tests and objects have been tested against each other by the ban-lurker. 'ban req.url == foo && req.http.host == bar' counts as one in 'bans\_tested' and as two in 'bans\_tests\_tested' |
| Objects killed by bans (lurker) | varnish.cache.main.bans\_lurker\_obj\_killed.count | Number of objects killed by the ban-lurker. |
| Objects killed by bans for cutoff (lurker) | varnish.cache.main.bans\_lurker\_obj\_killed\_cutoff.count | Number of objects killed by the ban-lurker to keep the number of bans below ban\_cutoff. |
| Bans superseded by other bans | varnish.cache.main.bans\_dups.count | Count of bans replaced by later identical bans. |
| Lurker gave way for lookup | varnish.cache.main.bans\_lurker\_contention.count | Number of times the ban-lurker had to wait for lookups. |
| Bytes used by the persisted ban lists | varnish.cache.main.bans\_persisted\_bytes | Number of bytes used by the persisted ban lists. |
| Extra bytes in persisted ban lists due to fragmentation | varnish.cache.main.bans\_persisted\_fragmentation | Number of extra bytes accumulated through dropped and completed bans in the persistent ban lists. |
| Number of purge operations executed | varnish.cache.main.n\_purges.count | Number of purge operations executed |
| Number of purged objects | varnish.cache.main.n\_obj\_purged.count | Number of purged objects |
| Number of objects mailed to expiry thread | varnish.cache.main.exp\_mailed.count | Number of objects mailed to expiry thread for handling. |
| Number of objects received by expiry thread | varnish.cache.main.exp\_received.count | Number of objects received by expiry thread for handling. |
| HCB Lookups without lock | varnish.cache.main.hcb\_nolock.count | HCB Lookups without lock |
| HCB Lookups with lock | varnish.cache.main.hcb\_lock.count | HCB Lookups with lock |
| HCB Inserts | varnish.cache.main.hcb\_insert.count | HCB Inserts |
| ESI parse errors (unlock) | varnish.cache.main.esi\_errors.count | ESI parse errors (unlock) |
| ESI parse warnings (unlock) | varnish.cache.main.esi\_warnings.count | ESI parse warnings (unlock) |
| Loaded VMODs | varnish.cache.main.vmods | Loaded VMODs |
| Gzip operations | varnish.cache.main.n\_gzip.count | Gzip operations |
| Gunzip operations | varnish.cache.main.n\_gunzip.count | Gunzip operations |
| Test gunzip operations | varnish.cache.main.n\_test\_gunzip.count | Those operations occur when Varnish receives a compressed object from a backend. They are done to verify the gzip stream while it's inserted in storage. |
| Premature iovec flushes | varnish.cache.main.http1\_iovs\_flush.count | Number of additional writes performed on HTTP1 connections because the number of IO vectors was too small to submit all possible IO in one go. This number is configured through the http1\_iovs parameter for client connections and implicitly defined by the amount of free workspace for backend connections. |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Monitor the statistics of your Varnish Cache instances.](https://www.dynatrace.com/hub/detail/varnish-cache-1/)


---


## Source: disk-analytics.md


---
title: Disk Analytics extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/disk-analytics
scraped: 2026-02-17T21:23:54.840752
---

# Disk Analytics extension

# Disk Analytics extension

* Latest Dynatrace
* Extension
* Updated on Dec 18, 2025

Gain detailed visibility into Linux host local datastores where OneAgent is installed.

## Get started

### Overview

The Disk Analytics extension enables you to inspect and analyze physical and logical local data storage devices such as disks, partitions, volumes, and software or hardware raids on Linux machines where OneAgent is installed.

* Inspect disk hardware beyond just the mount points
* Detect disk-related problems directly from Dynatrace
* Detailed metrics for all partitions, software or hardware raid instances, and logical volumes. The details include mount points, file system type, partition sizes, and encryption status
* For devices with an assigned mountpoint, file system stats are presented

### Requirements

* OneAgent 1.233+
* Linux hosts only; see [OneAgent Linux supported technologies](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* Local disks only (network disks are not supported)
* Full-stack OneAgent deployments only. PaaS OneAgent deployments do not support the Disk Analytics extension

## Activation and setup

Before you can enable the extension, you need to install it: In Dynatrace Hub, select and install **Disk Analytics**.

After adding this extension to your environment, you also need to enable data collection in settings either at the host or host group level. The settings name is **Disk Analytics Extension**. This ensures full control of custom metrics and DDU consumption.

Once data collection is enabled on the target Linux hosts, you can view key metrics for all local disk instances and further inspect any of the disk instances on the selected hosts using the host page.

The classic host page does not display this information, but the information is also available using Data Explorer.

### Enable for host group

If you enable the extension for a host group, this setting overrides any setting on the environment level, but could in turn be overridden by a setting on the host level for any host in the host group.

To enable or disable the extension for all Linux hosts in a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Disk Analytics Extension**.
6. On the **Disk Analytics extension** page for the selected host group, turn the extension on or off as needed.

### Enable for host

If you enable the extension for a host, this overrides any setting on the host group or environment level.

To enable or disable the extension on one Linux host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Disk Analytics Extension** and turn the extension on or off as needed for the selected host.

## Details

### Metrics

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host on which you want to analyze local storage devices.
2. Select the **Linux disks** tab to scroll the page down to the **Linux disks** section.

### Licensing and costs

Disk Analytics extension metrics consume Davis data units (DDUs) for the selected hosts. For each disk device, one data point is sent per minute. A disk device includes each mount point, volume, partition, or raid instance.

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Gain detailed visibility into Linux host local datastores where OneAgent is installed.](https://www.dynatrace.com/hub/detail/disk-analytics/)


---


## Source: radware-alteon-load-balancer.md


---
title: Radware Alteon Load Balancer extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/radware-alteon-load-balancer
scraped: 2026-02-17T05:08:52.124642
---

# Radware Alteon Load Balancer extension

# Radware Alteon Load Balancer extension

* Latest Dynatrace
* Extension
* Published Dec 15, 2025

Monitor your Radware Alteon Network Load Balancers through SNMP.

## Get started

### Overview

Monitor your Radware Alteon Network Load Balancer devices and interfaces through SNMP.

This extension collects infrastructure metrics to monitor the health and performance of your Radware Alteon Load Balancer devices.

![radware-1](https://dt-cdn.net/images/radware-dashboard-resized-2107-7e41f877d2.png)

![radware-2](https://dt-cdn.net/images/radware-device-resized-2085-dbb5255a5b.png)

### Use cases

* Monitor important device metrics such as uptime, CPU and memory usage, as well as additional hardware status metrics for temperature, fan, and power supply.
* Monitor device interfaces to report metrics including bytes, discards, and errors in/out.
* Collect additional device data, including virtual server utilization, HTTP and SSL statistics, throughput, and session counts. The full list of monitored metrics can be viewed under **Feature Sets**.
* Detect device anomalies and avoid outages.

### Compatibility information

* SNMP v2c or SNMP v3
* Dynatrace version 1.318+

## Activation and setup

Activate the extension in your environment using the in-product Hub, provide the necessary device configuration, and you're all set up.

For details, see the [SNMP extension data source documentation](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.").

## Details

The extension package contains:

* SNMP Data Source configuration
* Overview dashboard (Classic & Platform)
* Unified analysis screens
* Custom topology types extracted from metric dimensions:

  + Radware Alteon Device
  + Radware Alteon Interface
* SNMP MIB files used for monitoring:

  + IF-MIB
  + ALTEON-CHEETAH-LAYER4-MIB
  + ALTEON-CHEETAH-NETWORK-MIB
  + ALTEON-CHEETAH-SWITCH-MIB
  + ALTEON-ROOT-MIB

### Licensing and costs

Calculations are based on the assumption that you monitor all metrics for every feature set every minute:

DDUs: `(60 + (8 * Interfaces)) * 525.6 DDUs/year, per device`

DPS (Metric data points): `(60 + (8 * Interfaces)) * 525,600 metric data points/year, per device`


---


## Source: stonebranch-uac.md


---
title: Stonebranch Universal Automation Center extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/stonebranch-uac
scraped: 2026-02-16T21:26:44.934793
---

# Stonebranch Universal Automation Center extension

# Stonebranch Universal Automation Center extension

* Latest Dynatrace
* Extension
* Published Dec 12, 2025

Monitor Stonebranch Universal Automation Center (UAC) via OpenTelemetry.

## Get started

### Overview

This extension collects UAC metrics via Dynatrace ActiveGate and turns them into a UC-aware view inside Dynatrace. It discovers Universal Controllers, OMS servers, Universal Agents, workflows, and business services from metric labels and maps them into a topology with dedicated Unified Analysis Screens and example dashboards.

IT Ops, SREs, and platform teams can use this extension to:

* Track task execution and workflow outcomes.
* Monitor controller, JVM, and process health.
* Watch UAC license consumption and capacity limits.
* Receive UAC-specific alerts when OMS, agents, or licenses are in trouble.

All of this is done through metric scrapingâno custom scripting is required.

### Use cases

* Overview of your entire UAC environment: Get an overview of one or more Universal Controllers with an all-in-one view inside of Dynatrace.
* Controller and OMS health monitoring: Detect controller node or OMS issues early using status and connection metrics.
* Automation workload visibility: Monitor execution counts, active instances, and outcome distributions across workflows and task types.
* License and capacity management: Track usage of agents, nodes, executions, and tasks against license quotas to avoid overages.
* Workflow- and agent-centric views: Use workflow and Universal Agent entity screens to understand where tasks run, how they perform, and which business services they belong to.
* Integrated troubleshooting inside Dynatrace: Use dashboards, entity screens, and alerts to quickly isolate whether a problem is in the automation logic, the controller, the agents, or the underlying infrastructure.

### Compatibility information

* Universal Controller: 7.9.0.0+
* Universal Agent: 7.9.0.0+

## Activation and setup

1. Install and activate the extension from the Dynatrace Hub.
2. Configure the metric endpoint. Point the extension to your Universal Controller Prometheus metrics endpoint.
3. Configure authentication. Make sure that the UC user (or the equivalent service user) has the `ops_service` role.
4. recommended Enable workflow and business context labels. For deeper insights into workflows, agents, and business services, configure additional labels in `uc.properties` so they appear in metrics such as `uc_history_total`.

   For example

   * `task_name` (workflow/task name)
   * `security_business_services` (business service names)
   * `agent_id`
   * `cluster_node_id`

   These labels are used in topology mapping (Workflows, Business Services, Universal Agents), workflow/agent dashboards, and entity screens.

   For more details, see:

   * The Stonebranch documentation for properties: [Propertiesï»¿](https://stonebranchdocs.atlassian.net/wiki/spaces/UC79/pages/1614542260/Properties).
   * Implementation details and examples: [Dynatrace Observability for UAC â Implementation Guideï»¿](https://stonebranchdocs.atlassian.net/wiki/spaces/UE/pages/1949892609/Dynatrace+Observability+for+UAC+-+Implementation+Guide).

## Details

### Metric ingestion

The extension uses Dynatrace ActiveGate to scrape Prometheus-format metrics from one or more Universal Controllers. Metrics are grouped into feature sets, including

* Universal Controller metrics

  + Workload and history
  + Database connection pool
* Standard process metrics

  These are based on metrics like `process_cpu_seconds_total`, `process_virtual_memory_bytes`.
  Examples include

  + CPU time
  + Virtual and resident memory
  + Process start time
  + Open/max file descriptors
* JVM metrics

  + Heap and non-heap memory usage and pools
  + Buffer pool usage and capacity
  + GC collection time
  + Thread counts and states
  + Class loading statistics
  + JVM runtime info
* Universal Agent and OMS metrics

  + Agent Status
  + OMS Status
  + Server Session
  + Last Connection Time
* License and capacity metrics

  + Distributed agents currently used
  + Maximum number of distributed agents that can be used
  + z/OS agents used / max
  + Cluster nodes used / max
  + Monthly executions used / max
  + Task definitions used / max
  + `uc_monthly_executions` for current-month execution count

These metrics provide a high-level view of the UAC.

### Topology and entity model

The extension maps metric dimensions into Dynatrace entities and relationships, allowing you to navigate your automation landscape visually. For example, you can navigate from a controller to the workflows running on it, down to the agents executing them.

Entity types

* Universal Controller
* OMS
* Workflows
* Business Services
* Universal Agent

### Unified Analysis Screens and dashboards

The extension ships with

* Universal Controller Overview dashboard for high-level monitoring
* Unified Analysis Screens for

  + Universal Controller
  + Workflow
  + Universal Agent

Example views include

* UC-wide history distribution by task type and task name
* Active task instances by status
* Monthly execution counts
* Workflow instance status and business service grouping
* Universal Agent task distributions by type and status

### Built-in alerts

The extension includes predefined alert configurations, which are saved as alert templates. These are available for

* OMS server availability
* UC cluster node availability
* Database connection pool health
* Various alerts relating to the UC license

These alerts are based purely on metrics and can be adjusted or extended in Dynatrace as needed.

### Licensing and cost

There is no charge to use the extension. You are only charged for the data that the extension ingests. The license consumption details depend on which licensing model you're using. This can either be [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") or the [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") model.

#### Metrics

License consumption is based on the number of metric data points ingested. A rough annual estimate, assuming all feature sets are enabled, is shown below.

```
(



(



( 1 * number of UC Cluster Nodes )



+ ( 46 * number of Universal Controllers )



+ ( 1 * number of OMS )



+ ( 4 * number of Universal Agents )



+ ( 5 * number of unique Task Names )



)



) * 60 minutes * 24 hours * 365 days per year
```

#### Classic licensing

In the Dynatrace classic licensing model, metric ingestion consumes [Davis Data Units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") at the rate of .001 DDUs per metric data point.
To estimate annual DDU usage, take the result of the above formula for annual data points and multiply it by .001.

## FAQ

Does this extension collect traces or logs?

No. This extension focuses on metrics-based monitoring and topology. Traces and logs can be added separately using UAC's OpenTelemetry or log forwarding capabilities.

Can I customize dashboards and alerts?

Yes. The shipped examples and alert templates are meant as a starting point. You can clone and adapt them in Dynatrace.

Why are some tiles not working?

If some tiles do not show data, check if the user has access to read the metrics endpoint of the Universal Controller or if you have the optional metrics enabled in your `uc.properties`.


---


## Source: extensions.md


---
title: Extensions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions
scraped: 2026-02-17T21:21:55.232615
---

# Extensions

# Extensions

* Latest Dynatrace
* Reference
* 5-min read
* Published Nov 28, 2025

Extensions help you gain deeper insights into your environment and enhance your monitoring capabilities.

Explore available extensions, narrow results using the filters (data source, category, technology, and vendor), and select an extension to view its detailed documentation, configuration steps, and use cases.

Filter by

Select an option

Type to filter

Unable to render DataTable. Check configuration.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Unlock the full potential of Dynatrace by finding, activating, and running extensions that address your specific observability needs.

Use the top search bar to find an extension by entering its name, technology, or words related to it. Then, select an extension tile to view its details.](https://www.dynatrace.com/hub/?filter=all&type=extension)[![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extensions app

Latest Dynatrace

With ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, Dynatrace allows you to manage your extensions, including installation, configuration, and monitoring.](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.")


---


## Source: exclude-disks-and-network-traffic.md


---
title: Exclude disks and network traffic from host monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic
scraped: 2026-02-17T21:32:26.385516
---

# Exclude disks and network traffic from host monitoring

# Exclude disks and network traffic from host monitoring

* How-to guide
* 4-min read
* Updated on Jul 08, 2024

OneAgent automatically detects and monitors the mount points and network traffic of a host, but you can exclude selected mount points or network traffic from monitoring.

## Exclude disks

Use the **Disk options** settings to create exception rules to remove disks from monitoring.

* Certain file systems (for example, `autofs`, `proc`, `cgroup`, `tmpfs`) are always excluded because monitoring them is not useful.
* You can create disk exclusion rules on the environment, host group, or host level. Exclusions set at a lower level override exclusions set at a higher level (for example, host-level exclusions override environment-level exclusions).

To create a disk exclusion rule

1. Go to the **Disk options** page for the correct level:

   * Environment

     Go to **Settings** > **Preferences** > **Disk options**.
   * Host group

     1. Go to **Deployment Status** > **OneAgents**.
     2. Filter the table by `Host group` and select the host group for which you want to create a disk exclusion rule.
     3. For any listed host (they are all in the selected host group), select the **Host group** link.
     4. Select **Disk options**.
   * Host

     1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host for which you want to create a disk exclusion rule.
     2. On the host overview page, select  > **Settings**.
     3. Select **Disk options**.

   After you are on the **Disk options** page, the steps for creating a disk exclusion rule are the same. The important difference is in the level to which the rule applies: environment, host group, or host.
2. Select **Add item**.
3. Select the **Operating system** of the excluded disk.
4. Set **Disk or mount point path** to the path to where the disk to be excluded from monitoring is mounted.

   **Examples:**

   * `/mnt/my_disk`
   * `/staff/emp1`
   * `C:\`
   * `/staff/*`
   * `/disk*`

   * Mount point paths are case-sensitive
   * The wildcard in `/staff/*` means to exclude every child folder of `/staff`
   * The wildcard in `/disk*` means to exclude every mount point starting with `/disk` (for example, `/disk1`, `/disk99`, and `/diskabc`)
5. Set **File system type** to the type of the file system to be excluded from monitoring.

   **Examples:**

   * `ext4`
   * `ext3`
   * `btrfs`
   * `ext*`

   * File system types are case-sensitive
   * The wildcard in `ext*` means to exclude matching file systems (for example, types `ext4` and `ext3`)
6. Select **Save changes**.

## Exclude network traffic

Use the **Exclude network traffic** settings to exclude traffic on specific network interfaces or hosts from monitoring.

### Exclude NIC

All network traffic from all selected NICs is excluded from monitoring.

1. On the **Exclude network traffic** page, under **Exclude NIC**, select **Add item**.
2. Set **Operating system** to the operating system of the network interface.
3. Set **Name** to the selected operating system's name for the network interface.
4. Select **Save changes**.

### Exclude IP

All network traffic from all selected host IP addresses is excluded from calculating connectivity (other metrics are still calculated). This can be useful, for example, to avoid false connectivity alerts.

To exclude an IP address from connectivity calculations

1. On the **Exclude network traffic** page, under **Exclude IP**, select **Add item**.
2. Enter an IP address whose traffic you want to exclude from connectivity calculations. Wildcards and ranges are not allowed.
3. Select **Save changes**.

## Disks not monitored by OneAgent

The following disks are not monitored by OneAgent. To exclude an additional filesystem type or mount point name, see [Exclude disks](#disk-options).

Operating system

Type

Excluded disks

All supported OS

File systems

`hsfs`

`devtmpfs`

`sysfs`

`rootfs`

`ramfs`

`proc`

`procfs`

`devpts`

`securityfs`

`cgroup`

`cpuset`

`pstore`

`mqueue`

`debugfs`

`autofs`

`hugetlbfs`

`fusectl`

`fuse.gvfsd-fuse`

`binfmt_misc`

`iso9660`

`none`

`rpc_pipefs`

Linux

File systems

`tmpfs`

`udf`

`squashfs`

Linux

Mount point

`/dev`

AIX

File systems

`cdrfs`

Solaris

Network interface

`mac`


---


## Source: organize-your-environment-using-host-groups.md


---
title: Organize your environment using host groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups
scraped: 2026-02-17T21:19:13.008951
---

# Organize your environment using host groups

# Organize your environment using host groups

* How-to guide
* 3-min read
* Updated on Aug 21, 2023

Host groups enable you to categorize and manage multiple hosts that share similar characteristics or purposes within your environment.

## Check host group assignment

To determine the host group to which a host belongs

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

## List all hosts in a host group

To list all hosts in a host group

1. Go to **Deployment Status** and select **OneAgents**.  
   This lists all hosts in your deployment.
2. In the filter bar, select **Host group** and the name of the host group.  
   This lists all hosts in the selected host group.

## Assign a host to a host group

You can assign a host to a host group during or after [OneAgent installation](/docs/ingest-from "Learn how to install and configure ActiveGate and OneAgent on various platforms.").

* **During** OneAgent installation

  To assign a host to a host group when you install OneAgent, use the `--set-host-group` parameter, shown in the example below.

  `/bin/sh Dynatrace-OneAgent-Linux-1.177.65.sh --set-host-group=MyHostGroup`

  On Windows, you can also type the group name in the installer UI.
* **After** OneAgent installation

  To assign a host to a host group after you install OneAgent

  CLI

  Dynatrace UI

  Use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command-line tool.

  1. Go to **Deployment Status** and check the box next to the desired host.
  2. Select **modify host group** at the bottom of the page.
  3. Select **Run action**.
  4. Now you can either choose **Specify host group to be assigned** or **Remove current host group assignment**.
  5. Select **Next**.
  6. Review your changes and select **Apply changes**.

  Note that OneAgent will automatically restart after the changes are applied.

Host group string requirements

* Can contain only alphanumeric characters, hyphens, underscores, and periods.
* Must not start with `dt.`.
* Maximum length is 100 characters.

The host group is statically assigned to the host. Each host belongs to at most one host group and the host group can be changed by using the 'oneagentctl' command, [remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API."), or by re-installing OneAgent. Host groups are displayed, for example, on the **Hosts** page from the [**Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations#hosts "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.") app, and on the **Monitoring overview** page, where you can select the **Host group** link to edit the settings for all hosts in a host group.

![Host groups](https://dt-cdn.net/images/host-groups-1200-d314d1729f.png)

## How host groups affect your monitoring environment

Host groups are sets of hosts. Each group can be configured on the host-group level. This makes it easy to change the settings for a large number of hosts. You can define alerting thresholds and OneAgent update settings on a per-host-group basis. In the example below, the host group accepts the globally-configured anomaly thresholds without overriding them.

![Host groups](https://dt-cdn.net/images/host-groups2-1422-845f78e968.png)

You can also define the OneAgent update settings and trigger the update for all the OneAgent installations of a single host group, as shown in the example below. Here the global settings are overridden and all OneAgent installations are automatically updated whenever a new version is released.

![Host groups](https://dt-cdn.net/images/host-groups3-1426-aa75a3847f.png)

Additionally, host groups affect how process groups are detected. When the same process is running in two different host groups, Dynatrace will create one process group for each host group. This means you can also configure process groups differently depending on which host group they run in. Consequently, services are also grouped per host group. So you can configure services differently per host group.

Host groups can also be used in [tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") and for defining [management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") so you can apply additional context information to the different entities in Dynatrace, based on host groups. As shown in the example below, you can tag entities based on the host group they belong to.

![Host groups](https://dt-cdn.net/images/host-groups4-1414-8039d74ee9.png)


---


## Source: configuration.md


---
title: Host-level settings
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/configuration
scraped: 2026-02-17T21:15:18.501141
---

# Host-level settings

# Host-level settings

* How-to guide
* 2-min read
* Updated on Mar 28, 2024

In many cases, you can configure monitoring settings at the environment, host group, or host level.

* Settings at the host level override settings at the host group and environment levels.
* Settings at the host group level override settings at the environment level.

To configure settings at the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

From here, select items in the left panel to navigate through the host-level settings pages. In this example, you would display the **General** settings page for HOST-001.

![General section in the host settings](https://dt-cdn.net/images/select-host-settings-286-abb08ad1d1.png)

Hierarchy navigation

Changes to settings at the host level override settings at the host group and environment levels.

* If no settings have been changed at the host level, a message box offers a link up from the host-level settings to the equivalent settings on the host group level. If no settings are configured for the host group either, a similar message box offers a link up from the host group settings to the environment settings.
* If host-level settings have been changed, a message box states that "These settings are overriding [host group name] (Host group) settings." You can select the host group name to go to those settings or select **Remove override** if you want to remove the host-level settings and use the host group settings.

## General

The **General** page of **Host settings** displays a table of monitored technologies.

1. On the host-level **Host settings** page, select **General**.

   The **Monitored technologies** table lists monitoring technologies on the selected host:

   * **Technology**âthe name of the technology
   * **Type**âthe type of monitoring, such as `JMX monitoring`, `OneAgent extension`, `Custom extension`, and `Service insights`
   * **Configuration**âthe current configuration level for the selected host.
   * **Monitoring**âthe monitoring state of this technology on the selected host.
2. Select in the **Edit** column to see configuration options:

   * **Use host configuration** determines whether to use host-level monitoring settings, overriding the equivalent environment and host group settings.
   * When you turn on **Use host configuration**, technology-specific settings become available.

To manage host monitoring settings, go to [Host monitoring](#host-monitoring).

## Host monitoring

OneAgent automatically monitors a host and its processes, services, and applications, but you can turn off monitoring, full-stack monitoring, or auto-injection at the host level.

1. On the **Host settings** page, select **Host monitoring**.
   There are three tabs on this page:

   * **Monitoring**
   * **Monitoring Mode**
   * **Advanced Settings**
2. Go to **Monitoring** and set **Monitor this host** to turn monitoring on or off for the selected host.
3. Go to **Monitoring Mode** and set **Full-Stack**, **Infrastructure**, or **Discovery** to turn the selected monitoring mode on or off for the selected host.

   * For details, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * The OneAgent's monitoring mode will automatically overwrite this setting whenever it is changed with oneagentctl or the OneAgent comes online.
4. Go to **Advanced settings** and set **ProcessAgent injection** or **CodeModule injection** to turn the automatic injection on or off for the selected host.
5. Select **Save changes**.

## Container technologies

Dynatrace OneAgent automatically monitors all processes that are running on your monitored hosts. Within container environments (for example, Kubernetes, OpenShift, Cloud Foundry, or Docker), OneAgent automatically injects code modules into containerized processes to provide out-of-the-box full-stack visibility into applications running within containers.

1. On the **Host settings** page, select **Container technologies**.
2. For each container type, turn **Enabled** on or off to determine whether code modules are automatically injected.

   * If turned on, auto-injection provides deep monitoring for all processes within containers, at both the request- and distributed trace levels, for the selected host.
   * If turned off, OneAgent will not inject into a container of the selected type on the selected host.

## Disk options

OneAgent automatically detects and monitors all your mount points, but you can create exception rules to remove certain disks from the monitoring list.

1. On the **Host settings** page, select **Disk options**.
2. Set host-specific disk options as needed.

   * **Show all NFS disks** Linux

     When disabled, OneAgent attempts to deduplicate NFS disks. Disabled by default.
   * **Exclude disks**

     You can create exception rules to remove disks from monitoring.

     For details, see [Exclude disks and network traffic from host monitoring](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic#disk-options "Learn how to exclude selected disks and network traffic from host monitoring.").

## Disk Analytics Extension

Linux

Install the Disk Analytics extension to gain more detailed visibility into local data stores and their volumes, partitions, and raid instances on Linux hosts.

1. On the **Host settings** page, select **Disk Analytics Extension**.
2. Turn **Enable Disk Analytics data collection** on or off to determine whether Disk Analytics data is collected on the selected host.

   If you enable data collection without adding the extension, the data is visible only in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

For details on installing and using the Disk Analytics extension, see [Disk Analytics extension](/docs/observe/infrastructure-observability/extensions/disk-analytics "Gain detailed visibility into Linux host local datastores where OneAgent is installed.").

## NetTracer traffic

Linux

NetTracer is an open-source tool for tracing TCP events and collecting network connection metrics on Linux.

1. On the **Host settings** page, select **NetTracer traffic**.
2. Turn **Enable NetTracer traffic network monitoring** on or off to determine whether NetTracer monitors network traffic on the selected host.
3. Select **Save changes**.

For details, see [Extended network monitoring](/docs/observe/infrastructure-observability/networks/network-monitoring-with-nettracer "Extend network monitoring with network traffic metrics in containerized Linux hosts using NetTracer.").

## Exclude network traffic

OneAgent automatically detects and monitors all of your network traffic, but you can exclude traffic on specific network interfaces or hosts from monitoring.

1. On the **Host settings** page, select **Exclude network traffic**.

   There are two sections on this page:

   * **Exclude NIC**âThis section lists all network interfaces excluded from network traffic monitoring on a particular interface.

     + To add an entry, select **Add item**
     + To delete an entry, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") **Delete row**
     + To edit an entry, expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") **Details**
   * **Exclude IP**âThis section lists all host IP addresses to exclude when calculating connectivity (other metrics will still be calculated).

     + To add an entry, select **Add item**
     + To delete an entry, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") **Delete row**
     + To edit an entry, expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") **Details**
2. Select **Save changes**.

For details, see [Exclude disks and network traffic from host monitoring](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic#exclude-network-traffic "Learn how to exclude selected disks and network traffic from host monitoring.").

## Detected processes

The **Detected processes** page is a read-only table of processes detected on the selected host.

* To manage your process monitoring settings, select the **Process group monitoring** link.
* To enable or disable deep monitoring for certain process groups on the host, select the **Process group deep monitoring** link.

For details, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Process group monitoring

To enable or disable deep monitoring for a certain process group on a host

1. On the **Host settings** page, select **Process group monitoring**.

   The table lists process groups that have host-specific monitoring settings.

   * To add an entry, select **Add process group**, select a **Process group**, and set **Monitoring state** for the selected processing group.
   * To delete an entry, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") **Delete row**
   * To edit an entry, expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") **Details** and change the settings.
2. Select **Save changes**.

For details, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Process group detection flags

The **Built-in detection rules** page lists process group detection flag settings for the selected host.

To enable or disable process group detection flags

1. On the **Host settings** page, select **Process group detection flags**.

   If no host-level settings are configured, a message box offers a link to the equivalent settings on the host group level and, from there, up to the environment level.
2. Turn detection rules on or off as needed to set host-specific process group detection flags.

   Hover over the information icon for a rule to view rule details.
3. Select **Save changes**.

For details, see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

## Declarative process grouping

Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With declarative process grouping, you can automatically monitor additional technologies.

The **Declarative process grouping** page lists all process groups defined through declarative process grouping.

To add a declarative process group to the table

1. On the **Host settings** page, select **Declarative process grouping**.
2. Select **Add process group**.
3. Enter a name, identifier, and reporting setting.
4. Select **Add detection rule** to describe how to detect the process group: property and condition. See the on-screen instructions for help with conditions.
5. Select **Save changes**.

For details, see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection#declare "Ways to customize process-group detection").

## Process availability

Use **Process availability** to monitor if at least one process matching the specified monitoring rule exists on your host. If no process running on your host matches the rule, you receive an alert. If you also enable [process instance snapshots](#process-instance-snapshots), you receive a detailed report on the activity of the most resource-consuming processes, as well as on the latest activity of the processes matching the rule.

To add a process monitoring rule

1. On the **Host settings** page, select **Process availability**.
2. Select **Add monitoring rule**.
3. Enter a rule name.
4. Select **Add detection rule** to describe how to detect the process: property and condition. See the on-screen instructions for help with conditions.
5. Select **Add property** to define additional key-value properties to be attached to the triggered event.
6. Select **Save changes**.

For details, see [Process availability](/docs/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts.").

## Process instance snapshots

If you enable process instance snapshots, Dynatrace examines the most resource-consuming processes running on your host and the processes monitored by [Process availability](#process-availability). When a triggering event occurs, metrics reported 10 minutes before and 10 minutes after the event for those processes are sent to the cluster.

To turn on process instance snapshots

1. On the **Host settings** page, select **Process instance snapshots**.
2. Turn on **Enable Process instance snapshots**.
3. Set **Reported processes limit** to the maximum number of processes that the host will report.
4. Select **Save changes**.

## Business Observability

OneAgent can capture business events from incoming HTTP requests based on capture rules that tell OneAgent to capture business events when specific web services or endpoints are called.

* A capture rule consists of trigger rules, mandatory business event information (for example, type and provider), and optional event data fields.
* A trigger defines the criteria that, when met, cause a business event to be captured (for example, endpoint â/api/buyâ is called).

To configure a capture rule on the host level

1. On the **Host settings** page, select **Business Observability** > **OneAgent**.
2. Select **Add new capture rule**.
3. Define a rule. For details, see [Business event capture](/docs/observe/business-observability/bo-events-capturing "Capture business events for Dynatrace Business Observability.").
4. Select **Save changes**.

For details, see [Business event capture](/docs/observe/business-observability/bo-events-capturing#report-business-event-oneagent "Capture business events for Dynatrace Business Observability.").

## Anomaly detection

Use the host-level anomaly detection pages to configure detection sensitivity, set alert thresholds, or disable alerting for the selected host.

To configure anomaly detection for the host

1. On the **Host settings** page, select **Anomaly detection** > **Infrastructure**.
2. Adjust the host-specific thresholds as needed.
3. Select **Save changes**.

To configure anomaly detection for host disks

1. On the **Host settings** page, select **Anomaly detection** > **Disks**.
2. Adjust the host-specific thresholds as needed.
3. Select **Save changes**.

For details, see [Adjust the sensitivity of anomaly detection for infrastructure](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.").

## OneAgent updates

Use **OneAgent updates** to configure the selected host's OneAgent update behavior.

* Automatic updates at earliest convenience
* Automatic updates during update windows
* No automatic updates

Manually triggered environment updates override individual host update settings. To learn more about environment updates, see [One Agent Updates](/docs/ingest-from/dynatrace-oneagent/oneagent-update#oneagent-environment-settings "Learn how to update OneAgent.").

To set automatic OneAgent update behavior on the selected host

1. On the **Host settings** page, select **OneAgent updates**.
2. Set **Update mode**.
3. Select **Save changes**.

To manually update OneAgent on the selected host

1. Set **Update OneAgent to a specific version** to the OneAgent version you want to put on the selected host.
2. Select **Update now**.

## OS services monitoring

Use **OS services monitoring** to set up alerts for OS services in undesirable states.

1. On the **Host settings** page, select **OS services monitoring**.
2. Select **Add policy**.
3. Set **System** (Linux or Windows).
4. Set **Rule name**.
5. Define the alerting conditions.
6. Select **Save changes**.

For details, see [OS services monitoring](/docs/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.").

## Extension Execution Controller

Use **Extension Execution Controller** to configure the Extension Execution Controller (EEC) for OneAgent deployment.

1. On the **Host settings** page, select **Extension Execution Controller**.
2. Configure EEC settings:

   * Set **Enable Extension Execution Controller**.
   * Set **Enable local HTTP Metric, Log and Event Ingest API**.
   * Set **Enable Dynatrace StatsD**.
   * Set **Performance profile**. For details, see [Performance profile - resource consumption](#resource-consumption).
3. Select **Save changes**.

For EEC details, see [About Extensions](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").

## Log Monitoring

Use the **Log Monitoring** page to configure host-specific settings for log monitoring.

1. On the **Host settings** page, select **Log Monitoring**.
2. Open the configuration page for the settings you want to configure on this host.

   * OneAgent configuration

* Custom log source configurationâfor details, see [Custom log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source "Configure custom log sources to manually add log data sources that have not been autodetected.")
* Log storage configurationâfor details, see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.")
* Sensitive data maskingâfor details, see [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.")
* Timestamp configurationâfor details, see [Timestamp/splitting configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.")
* Select **Save changes**.

## Crash dump analytics

Use **Crash dump analytics** to manage the automatic detection of application crashes.

1. On the **Host settings** page, select **Crash dump analytics**.
2. Turn on/off **Crash dump analytics** to determine whether Dynatrace automatically detects application crashes on the selected host.
3. Select **Save changes**.

For details on Linux and Windows core crash dumps, see [Crash analysis](/docs/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes.").


---


## Source: host-availability.md


---
title: Host availability
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability
scraped: 2026-02-17T21:34:12.432908
---

# Host availability

# Host availability

* How-to guide
* 5-min read
* Updated on Nov 26, 2024

You can track host availability on the overview page for a selected host. The **Host availability** tile displays the percentage of the selected time range in which the host was online and responsive to requests.

## Check host availability state

To check a host's availability state

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** to list all the machines (physical and virtual) in your environment that have OneAgent installed.
2. Select a host to go to the host overview page, where you can view host details, including all available metrics for the host.
3. On the notifications bar, **Availability** indicates the percentage of time that the host was online and responsive to requests. Dynatrace detects and shows operating system shutdowns (including reboots) and periods when a host is offline (for example, if the host is down unexpectedly).

   When the connection to the host is lost, OneAgent caches all the collected data in a 55-minute buffer. Once the connection is reestablished, the data for the host is collected from the buffer's content and updated.

   In this example, the notifications bar displays an availability rate of 99.74% for the selected host during the selected timeframe.

   ![Host availability on the notifications bar](https://dt-cdn.net/images/notifications-bar-availability-854-e927dcebcb.png)
4. Select **Availability** on the notifications bar to display the **Host availability** panel, which charts host availability over time.

   In this example, the legend indicates the three different host availability states that occurred during the selected timeframe.

   ![Host page detail - online availability](https://dt-cdn.net/images/image-3-757-d2642a2b5d.png)

## Host availability states

Availability state

Description

**up**

The host is working; OneAgent is active and sending data. If the connectivity to the host is lost, OneAgent sends all cached metrics when the connection is restored.

**no\_data**

The host is working and OneAgent is active, but no data is being sent. This state is also set when collecting monitoring data takes too long (for example, OneAgent freezes).

**no\_data\_agent\_inactive**

The host is working, OneAgent is inactive, and no data is being sent because OneAgent has been manually disabled in the configuration.

**shutdown\_host**

The host has been shut down due to an expected operating system shutdown or reboot.

**unmonitored\_agent\_stopped**

The host is not monitored because OneAgent is inactive. For details, refer to [Check OneAgent monitoring settings per host](#check-monitoring-settings).

**unmonitored\_agent\_upgrade**

The host is not monitored because OneAgent is being upgraded.

**unmonitored\_agent\_uninstalled**

The host is not monitored because OneAgent has been uninstalled.

**reboot\_graceful**

The host was rebooted following a graceful shutdown, which means an expected operating system shutdown has occurred.

**reboot\_ungraceful**

The host was rebooted following an ungraceful shutdown, which means an unexpected operating system shutdown has occurred. This may be caused by events, such as power loss or a system crash.

### Check OneAgent monitoring settings per host

To check or change the monitoring settings per host:

1. Go to **Settings** > **Monitoring** > **Monitoring overview**.
2. Select the **Hosts** tab.
3. Find the host and check the **Summary** column to see if it's being monitored.
4. Select the edit button ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") and check the settings in the **Monitoring** tab.

## Host availability events

When the availability state changes (for example, when the host is shut down), OneAgent sends availability events. To check all events for a specific host, go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**, select the desired host, and then go to the **Events** tile.

The event types are:

* Reboot graceful
* Reboot ungraceful
* Graceful shutdown

  + K8s node termination (a subelement of Graceful shutdown, specific to Kubernetes environments)

### Reboot graceful/ungraceful

After a system restart, OneAgent checks system-specific log files or events to determine if the host was shut down gracefully or ungracefully.

* Graceful reboot indicates that the host is rebooted following an expected operating system shutdown.

  ![Host availability event - graceful reboot](https://dt-cdn.net/images/host-availability-graceful-reboot-1027-9c5a256356.png)
* Ungraceful reboot indicates that the host is rebooted following an unexpected operating system shutdown caused by events, such as power loss or a system crash.

  ![Host availability event - ungraceful reboot](https://dt-cdn.net/images/host-availability-ungraceful-reboot-1007-a3958d05f4.png)

The reboot graceful and reboot ungraceful events are supported on Linux, AIX, and Windows operating systems.

### Graceful shutdown

When the host is about to shut down, OneAgent sends the appropriate host shutdown event.

![Host availability event - graceful shutdown](https://dt-cdn.net/images/host-availability-graceful-shutdown-compact-1450-1488a61897.png)

The graceful shutdown event is supported on Linux, AIX, and Windows operating systems.

### K8s node termination

K8s node termination is supported on the Linux operating system. This event is generated on hosts where the Kubernetes engine is detected. OneAgent creates an inhibitor lock to get more time during shutdown.

Make sure OneAgent has sufficient rights to register the inhibitor lock.

If your Linux distribution experiences connections problems or the network manager is turned off faster than the event is sent, the shutdown event might not be sent on time.

![Host availability event - Kubernetes node shutdown](https://dt-cdn.net/images/host-availability-k8s-node-shutdown-969-3fd821c153.png)

## Maintenance windows

Maintenance windows are periods of time during which maintenance activities are scheduled to be performed in monitored environments. These maintenance windows can be used to prevent alerting, log file collection, system profiling, and other activities from taking place. For details, see [Maintenance windows](/docs/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.").

Maintenance windows are displayed as gray bars at the top of the **Host availability** and **Host performance** tiles on the host overview page.

![Availability tile maintenance window](https://dt-cdn.net/images/image-938-c6ad83866e.png)

![Host performance maintenance window](https://dt-cdn.net/images/image-1923-d376018fd7.png)


---


## Source: os-services.md


---
title: OS services monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring/os-services
scraped: 2026-02-17T21:23:45.196485
---

# OS services monitoring

# OS services monitoring

* How-to guide
* 14-min read
* Updated on Jan 14, 2026

Dynatrace provides out-of-the-box availability monitoring of OS services.

You can monitor hosts in full-stack monitoring mode or use lightweight monitoring modes. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

## Requirements

* Linux systemd version 230+ is required on the monitored host to monitor relations between processes and OS services.
* Linux systemd version 250+ is required on the monitored host for improved OS service detection performance by less frequent refreshes.

## OS services alerting options

Depending on your monitoring requirements, you can choose between basic or advanced alerting of OS services. The Discovery mode allows only basic alerting, while the Full-Stack and Infrastructure monitoring modes also allow advanced alerting.

### 1. Basic alerting (Service status)

Basic alerting provides insight only into the service status. The system will monitor an OS service's current status and alert you when it changes from running to failed.

With the service status property in ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment."), you can query the current status of the service.

#### Example

```
fetch `dt.entity.os:service`



| fieldsAdd status
```

![Service status - Basic monitoring](https://dt-cdn.net/images/os-service-status-dashboard-example-light-919-5bd9bbe242.png)

If the alert is enabled, events and problems are created when a service status changes, such as when a service goes from running to failed. For more details, refer to [Host availability](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability "Check host availability, interpret host availability states, and see how maintenance windows are reflected in host availability charts.").

#### Failed service alert

![Failed service alert](https://dt-cdn.net/images/os-service-failed-1486-77d0ea5343.png)

### Advanced alerting (Service availability metric)

Advanced alerting provides access to the service status and the service availability metric. In addition to OS service status changes, you get more granular information about service availability on a per-minute basis. This enables more complex business logic, for example, if you want to be notified if a service is stopped for longer than 10 minutes. You can create alerting rules to monitor availability and trigger an alert when needed.

#### Example

```
timeseries count(dt.osservice.availability),



by:{dt.osservice.display_name, dt.osservice.status}



| filter dt.osservice.display_name=="apache2"
```

![Service status - Advanced monitoring](https://dt-cdn.net/images/os-service-availability-dashboard-example-light-1148-5dde972c54.png)

## Monitor a service

To monitor an OS service, perform the following steps.

1. Access OS services monitoring

In Dynatrace, go to **OS services monitoring** for the level you are configuring.

* Settings are defined at the environment level.
* The host group level inherits all settings from the environment.
  Additionally, you can add configurations for specific host groups.
* The host level inherits all settings from the host group.
  Additionally, you can add configurations for specific hosts.

### Environment level

Go to **Settings** > **Collect and capture** > **Infrastructure** > **OS** > **OS services monitoring**.

### Host-group level

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **OS services monitoring**.

### Host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **OS services monitoring**.

2. Add service monitoring policy

Based on the service state and the rules, the service monitoring policy defines the way Dynatrace is monitoring your service. By default, Dynatrace comes with `Auto-start Windows OS Services` and `Auto-start Linux OS Services` policies for auto-started Windows and Linux services with failed status.

Limits

Note that the default limit of OS Service entities is 100,000 per cluster.
In larger environments with many hosts, we recommend creating precise rules that match only the important services for your infrastructure. Creating rules that are too general (for example, matching all services on thousands of hosts) may result in reaching the limit (entity explosion), leading to the disappearance of OS services from Dynatrace.
Also, `Auto-start Windows OS Services` and `Auto-start Linux OS Services` can be used as a starting point for further refining the policies.

The order of service monitoring policies is important. Policies that are higher on the list will proceed before those on lower positions until they are fulfilled. This allows for the creation of selective alerts or monitoring with minimal policies. For example, if you want to monitor all auto-started services and not just those created by Microsoft, you need to add a policy with disabled alerting and/or monitoring that will verify if the manufacturer is Microsoft.

1. On **OS services monitoring** for the level you are configuring based on your OS, select **Add policy** and define the policy, which is a collection of rules.
2. **System**: select your operating system.
3. **Rule name**: enter the name that will be displayed in the **Summary** field.
4. **Monitor**: decide whether you want to monitor service availability using the **OS service availability** (`builtin:osservice.availability`) metric. If available, the metric sends the service status every 10 seconds. The status is carried by the [**Service status**](#service-status) (`dt.osservice.status`) dimension.  
   Note that the metric consumes data points. For more information, see [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
5. **Alert**: decide whether you want alerting for your policy.
6. OneAgent version 1.257+ **Alert if service is not installed**: whether you want to receive alerts about OS services that are not installed on the host.
7. **Service status**: set the service status for which an alert should be triggered.

   Windows

   Linux

   You can use logic operations to monitor the service status. For example, `$eq(running)` monitors the running service state.

   Available logic operations:

   * `$not($eq(paused))` â Matches services that are in state different from paused.
   * `$or($eq(paused),$eq(running))` â Matches services that are either in paused or running state.

   These are the service statuses you can monitor. Use one of the following values as a parameter for this condition:

   * `running`
   * `stopped`
   * `start_pending`
   * `stop_pending`
   * `continue_pending`
   * `pause_pending`
   * `paused`

   You can use logic operations to monitor the service status. For example, `$eq(active)` monitors the active service state.

   Available logic operations:

   * `$not($eq(active))` â Matches services with state different from active.
   * `$or($eq(inactive),$eq(failed))` â Matches services that are either in inactive or failed state.

   These are the service statuses you can monitor. Use one of the following values as a parameter for this condition:

   * `reloading`
   * `activating`
   * `deactivating`
   * `failed`
   * `inactive`
   * `active`
8. Optional OneAgent version 1.257+ **Alerting delay**: the number of 10-second measurement cycles for a service to be in configured state before an event is generated. This doesn't apply to alerts for services that are not installed.

Next, you need to select which services you want to monitor based on service properties.

3. Select services you want to monitor

1. Select **Add rule**.
2. Optional **Rule scope**: select either **OS Service** or **Host**. By default, the **OS Service** option is selected.

If you selected **Host**:

* OneAgent version 1.277+ **Custom metadata** used for matching:

  + **Key** specifies the metadata key you want to match
  + **Condition** in which you can define a string that:

    - Dynatrace version 1.310+ `$match(ver*_1.2.?)` â Matches string with wildcards. Use `*` for any number of characters (including zero) and `?` for exactly one character.
    - `$contains(production)` â Matches if production appears anywhere in the host metadata value.
    - `$eq(production)` â Matches if production matches the host metadata value exactly.
    - `$prefix(production)` â Matches if production matches the prefix of the host metadata value.
    - `$suffix(production)` â Matches if production matches the suffix of the host metadata value.

    Available logic operations:

    - `$not($eq(production))` â Matches if the host metadata value is different from production.
    - `$and($prefix(production),$suffix(main))` â Matches if host metadata value starts with production and ends with main.
    - `$or($prefix(production),$suffix(main))` â Matches if host metadata value starts with production or ends with main.

    When including special characters such as brackets `(` and `)` within your matching expressions, escape these characters with a tilde `~`. For example, to match a metadata value that includes brackets, like `my(amazing)property`, you would write `$eq(my~(amazing~)property)`.

    Conditions are case insensitive.

If you selected **OS Service**, proceed according to your operating system.

Windows

Linux

* **Service property** used for matching:

  + **Display name** visible for system user.
  + **Path** to the binary used by OS service.
  + **Manufacturer** from the binary file of the service.
  + **Service Name**
  + **Startup Type**

A monitoring rule may consist of multiple detection rules. All detection rules must be satisfied for the OS Service to match, as a logical `AND` operation is applied across all specified conditions.

Additional information on Display name, Path, Manufacturer, and Service Name

With these properties, we define the services to be monitored based on:

* Display name visible to a system user
* Path to the service binary
* Manufacturer of the service
* Service name representing the name or ID under which OS service is recognized
* **Condition** in which you can define a string that:

  + Starts with â use `$prefix` qualifier, for example `$prefix(ss)`.
  + Ends with â use `$suffix` qualifier, for example `$suffix(hd)`.
  + Equals â use `$eq` qualifier, for example `$eq(sshd)`.
  + Contains â use `$contains` qualifier, for example `$contains(ssh)`.
  + Dynatrace version 1.310+ Matches â use `$match` qualifier, for example `$match(ip?tables*)`, where `*` matches any number of characters (including zero) and `?` matches exactly one character.

  Available logic operations:

  + `$not($eq(sshd))` â Matches if the service's property value is different from `sshd`.
  + `$and($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` and ends with `hd`.
  + `$or($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` or ends with `hd`.

  When including special characters such as brackets `(` and `)` within your matching expressions, escape these characters with a tilde `~`. For example, to match a property value that includes brackets, like `my(amazing)property`, you would write `$eq(my~(amazing~)property)`.

  Conditions are case insensitive.

Additional information on Startup Type

With this property we define the services to be monitored based on their startup type.

* **Condition** in which you can define a string that:

  + Equals â use `$eq` qualifier, for example `$eq(manual)`.

  Available logic operations:

  + `$not($eq(auto))` â Matches services with startup type different from Automatic.
  + `$or($eq(auto),$eq(manual))` â Matches if service's startup type is either Automatic or Manual.

  Use one of the following values as a parameter for this condition:

  + `manual` for Manual - the service starts only if needed or if you invoke something to start the service.
  + `manual_trigger` for Manual (Trigger Start) - the service starts along with the startup of another service.
  + `auto` for Automatic - the service starts automatically.
  + `auto_delay` for Automatic (Delayed Start) - the service startup is delayed until the system has finished booting.
  + `auto_trigger` for Automatic (Trigger Start) - the service starts automatically on startup and may be started or stopped due to certain operating system events.
  + `auto_delay_trigger` for Automatic (Delayed Start, Trigger Start)
  + `disabled` for Disabled

**Service property** used for matching:

* **Service Name**
* **Startup Type**

Additional information on Service Name

With this property we define the services to be monitored based on the service name.

**Condition** in which you can define a string that:

* Dynatrace version 1.310+ `$match(ip?tables*)` â Matches string with wildcards. Use `*` for any number of characters (including zero) and `?` for exactly one character.
* `$contains(ssh)` â Matches if `ssh` appears anywhere in the service's property value.
* `$eq(sshd)` â Matches if `sshd` matches the service's property value exactly.
* `$prefix(ss)` â Matches if `ss` matches the prefix of the service's property value.
* `$suffix(hd)` â Matches if `hd` matches the suffix of the service's property value.

Available logic operations:

* `$not($eq(sshd))` â Matches if the service's property value is different from `sshd`.
* `$and($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` and ends with `hd`.
* `$or($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` or ends with `hd`.

Additional information on Startup Type

With this property, we define the services to be monitored based on their startup type.

**Condition** in which you can define a string that:

* `$eq(enabled)` â Matches services with startup type equal to enabled.

Available logic operations:

* `$not($eq(enabled))` â Matches services with startup type different from enabled.
* `$or($eq(enabled),$eq(disabled))` - Matches services that are either enabled or disabled.

Use one of the following values as a parameter for this condition:

`enabled`, `enabled-runtime`

The service is marked as ready for startup.

`static`

The unit file is not enabled and has no provisions for enabling in the install unit file section. Static units are installed as dependencies and can only be masked, but are not always executed. They will be executed only if another unit depends on them or if they're manually started.

`disabled`

The unit file is not enabled, but it contains an install section with installation instructions.

4. Add custom properties

OneAgent version 1.247+

Dynatrace version 1.247+

Optional

1. Select **Add property** to specify a custom key-value property for the policy.

   Custom message in the Event details

   For example, a property with a **Key** set to `custom.message` and **Value** set to `The {dt.osservice.name} is with status {dt.osservice.status}` (including placeholders `{dt.osservice.name}` and `{dt.osservice.status}`) will extract the OS service name and status values once the rule is triggered. If the placeholder substitution fails, both the key and the value will be unavailable.

   ![os-service-custom-message](https://dt-cdn.net/images/screenshot-2022-09-02-at-11-00-08-665-79313a8bcc.png)

   ![os-service-custom-message-in-event](https://dt-cdn.net/images/screenshot-2022-09-02-at-11-45-39-991-335a005b28.png)

   For OneAgent version 1.255+, the `{dt.osservice.display_name}` placeholder is available.

   Additionally, you can utilize specific dt flags in the **Key** field to tailor the behavior of problem notifications and Davis AI analysis:

   * `dt.event.title`: Customizes the title of the problem.
   * `dt.event.description`: Provides a detailed description for the problem.
   * `dt.event.allow_davis_merge`: Controls how Davis AI decides to merge events, based on your settings.
2. Select **Save changes**.

## Manage monitored OS services

To manage the OS services

1. In Dynatrace, go to **OS services monitoring** for the level you are configuring.

   Host level

   1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
   2. Find and select your host to display the host overview page.
   3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

   4. In the host settings, select **OS services monitoring**.

   Host-group level

   1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
   2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
   3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

      The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

      The **Host group** property is not displayed when the selected host doesn't belong to any host group.
   4. Select the host group name in any row.

      As you have filtered by host group, all displayed hosts go to the same host group.

   5. In the host group settings, select **OS services monitoring**.

   Environment level

   Go to **Settings** > **Monitoring** > **OS services monitoring**.
2. The OS services you monitor are displayed in a table under the **Add policy** button.

   * To stop monitoring a listed service, turn the **Enabled** setting off.
   * To delete a service from the table, select the delete button in the **Delete** column
   * To view and edit details, select the expand control in the **Details** column.

## Monitor service availability

Dynatrace version 1.243+

OneAgent version 1.243+

The [Host overview](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") page contains the **OS services analysis** section listing the OS services for which any policy (with active alerting or monitoring) is fulfilled.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Select any host to go to its overview page.
3. In the **OS services analysis** section, select the service name to open the **Service overview** page.

For more information, see [OS services analysis](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#os-services "Monitor hosts with Dynatrace.").

## Configure at scale using Settings API

You can use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure your service availability monitoring at scale.

1. To learn the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:os-services-monitoring` as the schemaId.
2. Based on the `builtin:os-services-monitoring` schema, create your configuration object.
3. To create your configuration, use [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

## Limitations

On Linux, systemd OS services with the following startup types are supported:

* `enabled`
* `enabled-runtime`
* `static`
* `disabled`
* `indirect`


---


## Source: process-availability.md


---
title: Process availability
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring/process-availability
scraped: 2026-02-17T21:23:51.046866
---

# Process availability

# Process availability

* How-to guide
* 5-min read
* Updated on Jan 21, 2026

OneAgent version 1.237+

To monitor the availability of key processes on your hosts, you need to define monitoring rules. After you create a rule, when a matching process is missing on a host, Dynatrace issues an alerting event.

You can analyze the latest activity of the processes defined for process availability in the [Process instance snapshots](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#snapshots "Monitor hosts with Dynatrace.") section on the host overview page.

## Determine scope

You can create rules to apply at the environment, host group, and host levels. Lower-level rules override higher-level rules. For example, a rule created on the host level overrides a rule with the same name created on the environment level.

## Define monitoring rule

1. Go to the **Process availability** page for the level on which you want the rule to apply:

   * **Environment**: go to **Settings** and select **Processes and containers** > **Process availability**.
   * **Host group**: go to the host group page at `https://your-environment/ui/settings/HOST_GROUP-NAME` and select **Process availability**.
   * **Host**: go to the host overview page, select **More** (**â¦**), go to **Settings**, and select **Process availability**.
2. On the **Process availability** page, select **Add monitoring rule**. Process availability can comprise multiple individual detection rules. A process is identified if all of the individual detection rules match.
3. In **Monitoring rule name**, enter the name under which the rule will be listed.
4. Under **Operating system** (OneAgent version 1.287+), select the operating systems on which the monitoring rule should be applied. You can select more than one.

   * Windows
   * Linux
   * AIX
5. Set **Minimum number of matching processes** (OneAgent version 1.287+) to the minimum number of processes that should match this rule. If fewer processes match this rule on any individual host, an alert is triggered.
6. Select **Add detection rule** to define a detection rule.

   A single monitoring rule can have multiple detection rules. If you add more than one detection rule, a process is identified if all the detection rules match (AND relation).

   * **Rule scope**âYour selection of **Process** or **Host** determines the subsequent configuration details. Expand below for more.

     Process

     + **Select process property**âThe object against which your detection rule will be tested:

       - **Command line - single argument**âEach command line parameter is evaluated individually. Evaluation is case-sensitive.
       - **Command line**âOneAgent version 1.333+ The entire command line is evaluated. Evaluation is case-sensitive.
       - **Executable path**âRules are not case-sensitive
       - **User**âOneAgent version 1.287+ User is case-sensitive for Linux and AIX, not case-sensitive for Windows.

     The comparators evaluate each command line parameter individually for the **Command line - single argument** property (referred to as **Command line** in versions prior to 1.333). For example, a process `python my.py -ab -cd -ef` will be matched with a condition `$contains(cd)`, `$eq(-ab)`, but won't be matched with `$suffix(-cd -ef)` because `-cd` and `-ef` are distinct arguments, which are processed separately.

     OneAgent version 1.307+ The executable is also treated as a part of the command line as its the first argument.

     + **Condition**âDepending on what you want your rule to match, you can define a string that uses:

       - `$contains` matches if the property contains the specified value. For example, `$contains(keepalived)` matches if `keepalived` occurs anywhere in the property.
       - `$eq` matches if the property exactly matches the specified value. For example, `$eq(-d)` matches if `-d` exactly matches the property.
       - `$prefix` matches if the property starts with the specified value. For example, `$prefix(/usr/sbin/keepalived)` matches a property that starts with `/usr/sbin/keepalived`.
       - `$suffix` matches if the property ends with the specified value. For example,`$suffix(keepalived)` matches a property that ends with `keepalived`.

     Host

     OneAgent version 1.287+

     **Custom metadata** is user-defined key-value pairs that you can assign to hosts monitored by Dynatrace.

     By defining custom metadata, you can enrich the monitoring data with context specific to your organization's needs, such as environment names, team ownership, application versions, or any other relevant details.

     + **Key** specifies the metadata key you want to match
     + **Condition** in which you can define a string that:

       - `$contains(production)` â Matches if `production` appears anywhere in the host metadata value.
       - `$eq(production)` â Matches if `production` matches the host metadata value exactly.
       - `$prefix(production)` â Matches if `production` matches the prefix of the host metadata value.
       - `$suffix(production)` â Matches if `production` matches the suffix of the host metadata value.

       Available logic operations:

       - `$not($eq(production))` â Matches if the host metadata value is different from production.
       - `$and($prefix(production),$suffix(main))` â Matches if host metadata value starts with production and ends with main.
       - `$or($prefix(production),$suffix(main))` â Matches if host metadata value starts with production or ends with main.

       **Escape special characters**: When including special characters such as `(` and `)` within your matching expressions, escape these characters with a tilde `~`. For example, to match the metadata value `my(amazing)property`, enter `$eq(my~(amazing~)property)`.
7. If you need to add another detection rule to this monitoring rule, repeat the previous step.
8. Select **Add property** (OneAgent version 1.249+ Dynatrace version 1.249+) to specify a custom key-value property for the event.

   * **Key**: Type `dt.` in the **Key** field for hints.
   * **Value**: Type `{` in the **Value** field for hints.

   You can use only the values that are suggested as hints.

   Example custom message in the event details:

   * **Key** = `custom.message`
   * **Value** = `The {dt.entity.host} is deployed on: {dt.os.type}`

   In this example, note that **Value** includes two keys:

   * `{dt.entity.host}`
   * `{dt.os.type}`

   The entity host and OS type values will be extracted when the rule is triggered. If the key substitution fails, both the key and the value will be unavailable.
9. When you finish defining the monitoring rule, including all detection rules that are a part of the monitoring rule, select **Save changes**.

After you save your changes:

* Your monitoring rule is added to the list of monitoring rules on the **Process availability** page. The displayed name is what you entered in **Monitoring rule name**.
* Your monitoring rule is applied at the level you selected in the first step: environment, host group, or host.

## Manage rules

Monitoring rules are listed on the **Process availability** page. Each monitoring rule in turn contains a list of one or more detection rules.

* To view or edit the details of any listed monitoring or detection rule, select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column for that rule.
* To change rule order, drag ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") any rule to a different place in the list.
* To delete a rule, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Delete** column and then confirm your action.
* To enable or disable a rule (monitoring rules only), use the toggle in the **Enabled** column.


---


## Source: monitoring-modes.md


---
title: Infrastructure and Discovery monitoring modes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring-modes
scraped: 2026-02-06T16:20:45.488376
---

# Infrastructure and Discovery monitoring modes

# Infrastructure and Discovery monitoring modes

* Explanation
* 12-min read
* Updated on Oct 16, 2025

If you don't need your OneAgent to run in the full-stack monitoring mode, you can also use one of the two lightweight modes that provide you with the subset of OneAgent metrics, focusing on your host infrastructure:

* Infrastructure Monitoring mode
* Discovery mode

The table below shows an overview of available monitoring options for each of the monitoring modes.

|  | Discovery | Infrastructure | Full stack |
| --- | --- | --- | --- |
| Topology discovery (hybrid cloud discovery and Smartscape) | GA | GA | GA |
| Host criticality (detection of external services and app dependencies) | GA | GA | GA |
| Basic monitoring (host health, filesystem, OS Services) | GA | GA | GA |
| Host process details |  | GA | GA |
| Detailed disk analysis |  | GA | GA |
| Network analysis |  | GA | GA |
| Memory analysis |  | GA | GA |
| Extensions |  | opt-in | opt-in |
| Custom metrics |  | 100 / host | 15 / 256 MiB |
| Log Management | opt-in | opt-in | opt-in |
| Tracing and profiling |  |  | GA |
| Process injection |  | opt-out | GA |
| Application Security[1](#fn-1-1-def) | opt-in | opt-in | opt-in |
| Live Debugger | opt-in | opt-in | opt-in |

1

For more information on Infrastructure Monitoring and Discovery modes for Application Security, see [Monitoring modes for Application Security](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").

## Default monitoring mode

You can define a default monitoring mode before installing OneAgent. This will change the default **Full-Stack** monitoring mode on the OneAgent deployment page (for Linux, Windows, and AIX operating systems) and in the **Discovery & Coverage** app (when deploying OneAgent from the **Install OneAgent** page).

To define a default monitoring mode

1. Go to **Settings** > **Preferences** > **OneAgent default mode**.
2. Select a **OneAgent default monitoring mode** from the dropdown list.
3. Select **Save changes**.

The selected value will be set as a default value for the chosen OneAgent deployment mode.

## Discovery mode

OneAgent version 1.281+

OneAgent Discovery mode provides basic metrics enabling you to discover your hosts and processes and learn the potential to extend your monitoring.

We recommend that you deploy OneAgent in Full-Stack Monitoring mode to monitor your business-critical applications. Similarly, we recommend that you monitor critical infrastructure, like databases, queues, and messaging systems with Infrastructure Monitoring. OneAgent in Discovery mode can be deployed across the remainder of your infrastructure for full visibility thanks to its relatively low cost.

Discovery mode is available only if you're using the Dynatrace Platform Subscription model. License consumption is via the **Foundation & Discovery** capability. To learn more, see [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability#discovery "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

The following built-in metrics are available in Discovery mode:

### CPU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.cpu.entConfig | AIX Entitlement configured Capacity Entitlement is the number of virtual processors assigned to the AIX partition. It's measured in fractions of processor equal to 0.1 or 0.01. For more information about entitlement, see [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz) in official IBM documentation. | Ratio | autoavgmaxmin |
| builtin:host.cpu.entc | AIX Entitlement used Percentage of entitlement used. Capacity Entitlement is the number of virtual cores assigned to the AIX partition. See for more information about entitlement, see [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz) in official IBM documentation. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.idle | CPU idle Average CPU time, when the CPU didn't have anything to do | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.iowait | CPU I/O wait Percentage of time when CPU was idle during which the system had an outstanding I/O request. It is not available on Windows. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.load | System load The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last minute | Ratio | autoavgmaxmin |
| builtin:host.cpu.load15m | System load15m The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last 15 minutes | Ratio | autoavgmaxmin |
| builtin:host.cpu.load5m | System load5m The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last 5 minutes | Ratio | autoavgmaxmin |
| builtin:host.cpu.other | CPU other Average CPU time spent on other tasks: servicing interrupt requests (IRQ), running virtual machines under the control of the host's kernel (meaning the host is a hypervisor for VMs). It's available only for Linux hosts | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.physc | AIX Physical consumed Total CPUs consumed by the AIX partition | Ratio | autoavgmaxmin |
| builtin:host.cpu.steal | CPU steal Average CPU time, when a virtual machine waits to get CPU cycles from the hypervisor. In a virtual environment, CPU cycles are shared across virtual machines on the hypervisor server. If your virtualized host displays a high CPU steal, it means CPU cycles are being taken away from your virtual machine to serve other purposes. It may indicate an overloaded hypervisor. It's available only for Linux hosts | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.system | CPU system Average CPU time when CPU was running in kernel mode | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.usage | CPU usage % Percentage of CPU time when CPU was utilized. A value close to 100% means most host processing resources are in use, and host CPUs can't handle additional work | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.user | CPU user Average CPU time when CPU was running in user mode | Percent (%) | autoavgmaxmin |
| builtin:host.kernelThreads.blocked | AIX Kernel threads blocked Length of the swap queue. The swap queue contains the threads ready to run but swapped out with the currently running threads | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioEventWait | AIX Kernel threads I/O event wait Number of threads that are waiting for file system direct (cio) + Number of processes that are asleep waiting for buffered I/O | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioMessageWait | AIX Kernel threads I/O message wait Number of threads that are sleeping and waiting for raw I/O operations at a particular time. Raw I/O operation allows applications to direct write to the Logical Volume Manager (LVM) layer | Count | autoavgmaxmin |
| builtin:host.kernelThreads.running | AIX Kernel threads runnable Number of runnable threads (running or waiting for run time) (threads ready). The average number of runnable threads is seen in the first column of the vmstat command output | Count | autoavgmaxmin |

### Memory

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Memory available The amount of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. | Byte | autoavgmaxmin |
| builtin:host.mem.avail.pct | Memory available % The percentage of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. Shows available memory as percentages. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.kernel | Kernel memory The memory used by the system kernel. It includes memory used by core components of OS along with any device drivers. Typically, the number will be very small. | Byte | autoavgmaxmin |
| builtin:host.mem.recl | Memory reclaimable The memory usage for specific purposes. Reclaimable memory is calculated as available memory (estimation of how much memory is available for use without swapping) minus free memory (amount of memory that is currently not used for anything). For more information on reclaimable memory, see [this blog post](https://www.dynatrace.com/news/blog/improved-host-memory-metrics-now-include-reclaimable-memory/). | Byte | autoavgmaxmin |
| builtin:host.mem.total | Memory total The amount of memory (RAM) installed on the system. | Byte | autovalue |
| builtin:host.mem.usage | Memory used % Shows percentage of memory currently used. Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. Note: Calculated by taking 100% - "Memory available %". | Percent (%) | autoavgmaxmin |
| builtin:host.mem.used | Memory used Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. | Byte | autoavgmaxmin |

### Availability

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.availability.state | Host availability Host availability state metric reported in 1 minute intervals | Count | autovalue |
| builtin:host.uptime | Host uptime Time since last host boot up. Requires OneAgent 1.259+. The metric is not supported for application-only OneAgent deployments. | Second | autoavgmaxmin |

### Disk

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.disk.avail | Disk available Amount of free space available for user in file system. On Linux and AIX it is free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Byte | autoavgmaxmin |
| builtin:host.disk.bytesRead | Disk read bytes per second Speed of read from file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Disk write bytes per second Speed of write to file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.free | Disk available % Percentage of free space available for user in file system. On Linux and AIX it is % of free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Percent (%) | autoavgmaxmin |
| builtin:host.disk.used | Disk used Amount of used space in file system | Byte | autoavgmaxmin |

### Network

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.net.nic.bytesRx | NIC bytes received Network interface bytes received on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | NIC bytes sent on host Network interface bytes sent on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | NIC receive link utilization Network interface receive link utilization on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | NIC transmit link utilization Network interface transmit link utilization on the host | Percent (%) | autoavgmaxmin |

### Enable Discovery mode

You turn on Discovery mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Discovery mode during OneAgent installation, use the `--set-monitoring-mode=discovery` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Discovery mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Discovery**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=discovery` parameter.

### Code-module injection

For [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") and [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.") to work in Discovery mode, code-module injection is required. Code-module injection is disabled by default.

After [turning on Discovery mode](#enable-discovery-mode), you can turn on the code-module injection for a single host.

1. Go to the settings page of the desired host and select **Host monitoring**.
2. Go to **Advanced settings**.
3. Turn on **CodeModule Injection**, then select **Save changes**.
4. Restart the monitored processes on the host.

For details on how Application Security works in Discovery mode, see [Application Security: Discovery mode](/docs/secure/application-security#discovery "Access the Dynatrace Application Security functionalities.").

## Infrastructure Monitoring mode

OneAgent auto-injection

OneAgent in Infrastructure Monitoring mode automatically injects into processes to be able to monitor backing services written in Java and runtime metrics for supported languages. Learn how to [turn off auto-injection](#disable-auto-injection).

While Full-Stack mode provides complete application performance monitoring, code-level visibility, deep process monitoring, and Infrastructure Monitoring (including PaaS platforms) for use cases where less visibility is required, OneAgent can be configured for Infrastructure Monitoring mode, which provides physical and virtual infrastructure-centric monitoring, along with log monitoring and AIOps.

### Enable Infrastructure Monitoring mode

You turn on Infrastructure Monitoring mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Infrastructure Monitoring mode during OneAgent installation, use the `--set-monitoring-mode=infra-only` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Infrastructure Monitoring mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Infrastructure**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=infra-only` parameter.
* Use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to turn on Infrastructure Monitoring mode at scale.
* To download the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:host.monitoring` as the schemaId and create your configuration object using [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

### Process injection

Process injection provides you with additional data for Infrastructure Monitoring. Process injection is enabled by default.

If you run your OneAgent as a container with Infrastructure Monitoring mode enabled, process injection will not be performed.

Infrastructure Monitoring mode enables you to monitor any infrastructure component and backing service written in Java. You can monitor backing services supported by default (for example, Kafka or ActiveMQ), and you can also build your own custom [JMX and PMI extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.") for infrastructure components and use them in Infrastructure Monitoring mode.

Additionally, with process injection, Infrastructure Monitoring mode provides runtime metrics for:

* Java
* .NET
* Node.js
* Golang
* PHP
* Web servers such as Apache HTTP, NGINX, or Microsoft IIS.

### Disable process auto-injection

We don't recommend turning off auto-injection, but if you're required to do so due to strict security requirements, you can choose among various options. Turning off auto-injection also prevents Dynatrace from discovering vulnerabilities or live debugging in your environment, even if you enable [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") or [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace."). You can turn off automatic injection at the host or environment level.

#### Disable auto-injection for a single host

After OneAgent installation with UI

1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
3. Select **Host Monitoring**.
4. Go to **Advanced settings**.
5. Turn off **ProcessAgent Injection**, then select **Save changes**.
6. Restart the monitored processes on the host.

After OneAgent installation with command line

Use the [OneAgent command line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-auto-injection-enabled=false` parameter.

If you use oneagentctl to turn off automatic injection, you won't be able to control auto-injection in Infrastructure Monitoring mode using the Dynatrace web UI at **Settings > Monitoring > Monitored technologies** or [OneAgent monitoring configuration API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.").

#### Disable auto-injection for an environment

Define custom process monitoring rules

You can turn off process injection for particular process groups using custom process monitoring rules.

Custom process monitoring rules give you fine-grained control over which processes OneAgent injects into, with an approach that scales easily within large environments. You donât need to adjust your system configuration, and a few rules can cover thousands of processes.

For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").

Disable runtime metrics

You can disable the collection on JMX/PMI and runtime metrics, which will result in disabling auto-injection in Infrastructure Monitoring mode.

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. In the list of supported technologies, search for the **Java/.NET/Node.js/Golang/PHP runtime metrics + WebServer metrics in Infrastructure Mode** entry.
3. Select the pencil icon ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit it and then disable it.
4. Restart all processes on your infrastructure-monitored hosts.

Disable selected extensions

You can also turn off selected extensions collecting the metrics at the environment level.

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Supported technologies

   Custom extensions

   1. In the list of supported technologies, search for technologies marked as **JMX monitoring** in the **Type** column.
   2. Select the pencil icon ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit an extension of your choice.
   3. Turn off **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   1. In the list of custom extensions, search for extensions marked as **JMX** or **PMI** in the **Extension type** column.
   2. Select the extension name of your choice.
   3. Turn off **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   The setting at the host level takes precedence over environment settings. If a host is configured to **Use host configuration** for the extension and the extension isn't activated on this host, the environment configuration won't be applied. To make sure an extension is active on a single host level:

   1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and find an infrastructure-monitored host. You can filter by **Monitoring mode: Infrastructure only**.
   2. Open the host page.
   3. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
   4. In the **Monitored technologies** table, search for extensions of type **JMX extension**, **JMX monitoring**, or **PMI extension**.
   5. Select **Edit**. Use the **Activate `<extension name>` on this host** control.

### Filter hosts by injection status

When you turn off auto-injection, you can find such hosts using the **Auto-injection** filter on the **Deployment Status** page or [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Use Dynatrace web UI

1. Go to **Deployment Status** and then select the **OneAgents** tab.
2. Select the **Filter by** box, select **Auto-injection**, and select **Disabled manually**. You can also use one of the filters below to check other reasons. Note that a filter appears only if a host with a respective status is available in your deployment.

* **Enabled**  
  Auto-injection was successfully enabled.
* **Disabled manually**  
  Auto-injection was disabled [after OneAgent installation](#after-install), either using the Dynatrace web UI or `oneagentctl`.
* **Disabled on installation**  
  Auto-injection was disabled [during OneAgent installation](#during-install).
* **Disabled on sanity check**  
  Auto-injection wasn't enabled due to a failed test performed by the OneAgent installer before OneAgent installation started. Check the OneAgent installer log for details.
* **Failed on installation**  
  Auto-injection failed due to an error during OneAgent installation. Check the OneAgent installer log for details.

Use Dynatrace API

Run the [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") call with the `autoInjection` parameter set to `DISABLED_MANUAL`. The returned payload contains the list of OneAgents with auto-injection disabled [after OneAgent installation](#after-install) via either the Dynatrace web UI or `oneagentctl`.

## Virtualization monitoring

Dynatrace supports [virtualization monitoring](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace."). To monitor the virtual components in your environment, you need to complete an extra step beyond the initial setup. For full details, see [Set up virtualization monitoring](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.").

## FAQ

What happens when OneAgent injects itself into the monitored technology?

Along with injection, the injected module becomes dynamically linked to the monitored technology. Consequently, it becomes an integral part of the monitored process and can only be removed with a process restart. Depending on the OS (Windows/Linux/AIX), injection is performed in slightly different ways, but the outcome is quite similar.

I have turned off injection, but I can see that the Dynatrace deep code modules are still injected into monitored technologies.

The injection rules refer to the point in time when the process of a supported technology is started. After it is started, the deep-code monitoring module of OneAgent remains dynamically linked to the monitored technology and can be unloaded only by restarting the monitored process.

I have restarted/disabled/stopped OneAgent, but the injected modules remain active. What's going on?

With injection, the injected module becomes dynamically linked to the monitored technology. Consequently, it becomes an integral part of the monitored process and can be removed only by restarting the monitored process.

How does OneAgent monitor processes?

OneAgent injects into a process each time a new process is started in the system. OneAgent identifies the launched process (by name, location, user space, and so on) and, if it's supported for injection and if the injection rules don't exclude it, OneAgent sets up a dynamic link between the monitored process and one of the OneAgent deep-code monitoring modules.

I have disabled OneAgent in the web UI, but I still see the process active on the host and some form of network traffic is still going on between OneAgent and the Dynatrace cluster. I thought that disabled OneAgents would stop all activity.

Disabled OneAgents effectively stop monitoring your environment. However, the core of OneAgent, which is responsible for communication with the Dynatrace cluster, remains active. Because communication between OneAgent and Dynatrace clusters is always invoked on the OneAgent side, OneAgent needs to keep sending its status and asking the cluster if it needs to start monitoring again.


---


## Source: metrics.md


---
title: Host metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/reference/metrics
scraped: 2026-02-16T21:25:20.701450
---

# Host metrics

# Host metrics

* Reference
* 7-min read
* Published Nov 04, 2024

This is a reference list of the metrics used for hosts, with details of their availability on Windows, Linux, and AIX operating systems.

You can also check if the metrics are available in the Discovery monitoring mode. For more details, refer to [Discovery mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.").

## CPU and Memory metrics

Metrics representing the usage of CPU and RAM.

### CPU

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Idle | builtin:host.cpu.idle | dt.host.cpu.idle |  |  |  |  |
| User | builtin:host.cpu.user | dt.host.cpu.user |  |  |  |  |
| IO wait | builtin:host.cpu.iowait | dt.host.cpu.iowait |  |  |  |  |
| Other | builtin:host.cpu.other | dt.host.cpu.other |  |  |  |  |
| Steal | builtin:host.cpu.steal | dt.host.cpu.steal |  |  |  |  |
| System | builtin:host.cpu.system | dt.host.cpu.system |  |  |  |  |
| System Load | builtin:host.cpu.load | dt.host.cpu.load |  |  |  |  |
| System load 5 minutes | builtin:host.cpu.load5m | dt.host.cpu.load5m |  |  |  |  |
| System load 15 minutes | builtin:host.cpu.load15m | dt.host.cpu.load15m |  |  |  |  |
| CPU Usage % | builtin:host.cpu.usage | dt.host.cpu.usage |  |  |  |  |
| Logical / Physical CPU cores |  |  |  |  |  |  |
| entc | builtin:host.cpu.entc | dt.host.cpu.entc |  |  |  |  |
| physc | builtin:host.cpu.physc | dt.host.cpu.physc |  |  |  |  |
| entConfigured | builtin:host.cpu.entConfig | dt.host.cpu.ent\_config |  |  |  |  |
| AIX Kernel threads running | builtin:host.kernelThreads.running | dt.host.kernel\_threads.running |  |  |  |  |
| AIX Kernel threads blocked | builtin:host.kernelThreads.blocked | dt.host.kernel\_threads.blocked |  |  |  |  |
| AIX Kernel threads blocked I/O message wait | builtin:host.kernelThreads.ioMessageWait | dt.host.kernel\_threads.io\_message\_wait |  |  |  |  |
| AIX Kernel threads blocked I/O event wait | builtin:host.kernelThreads.ioEventWait | dt.host.kernel\_threads.io\_event\_wait |  |  |  |  |

### Memory

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Total | builtin:host.mem.total | Unsupported |  |  |  |  |
| Used | builtin:host.mem.used | dt.host.memory.used |  |  |  |  |
| Available | builtin:host.mem.avail.bytes | dt.host.memory.avail.bytes |  |  |  |  |
| Memory available % | builtin:host.mem.avail.pct | dt.host.memory.avail.percent |  |  |  |  |
| Memory used % | builtin:host.mem.usage | dt.host.memory.usage |  |  |  |  |
| Kernel | builtin:host.mem.kernel | dt.host.memory.kernel |  |  |  |  |
| memoryReclaimable | builtin:host.mem.recl | dt.host.memory.recl |  |  |  |  |
| Page Faults | builtin:host.mem.avail.pfps | dt.host.memory.avail.pfps |  |  |  |  |
| Swap Used | builtin:host.mem.swap.used | dt.host.memory.swap.used |  |  |  |  |
| Swap Total | builtin:host.mem.swap.total | dt.host.memory.swap.total |  |  |  |  |
| Swap Available | builtin:host.mem.swap.avail | dt.host.memory.swap.avail |  |  |  |  |

### File descriptors/handles

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| File descriptors used | builtin:host.handles.fileDescriptorsUsed | dt.host.handles.file\_descriptors\_used |  |  |  |  |
| File descriptors max | builtin:host.handles.fileDescriptorsMax | dt.host.handles.file\_descriptors\_max |  |  |  |  |

## Disk metrics

Metrics representing the disk usage. Note that there's a separation between network and local drives on Linux.

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Total[1](#fn-1-1-def) |  |  |  |  | [2](#fn-1-2-def) |  |
| Disk used | builtin:host.disk.used | dt.host.disk.used |  |  | [2](#fn-1-2-def) |  |
| Disk used % | builtin:host.disk.usedPct | dt.host.disk.used.percent |  |  | [2](#fn-1-2-def) |  |
| Disk available[1](#fn-1-1-def) | builtin:host.disk.avail | dt.host.disk.avail |  |  | [2](#fn-1-2-def) |  |
| Disk available %[1](#fn-1-1-def) | builtin:host.disk.free | dt.host.disk.free |  |  | [2](#fn-1-2-def) |  |
| Read (Bytes/s) | builtin:host.disk.bytesRead | dt.host.disk.bytes\_read | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Write (Bytes/s) | builtin:host.disk.bytesWritten | dt.host.disk.bytes\_written | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Inodes total | builtin:host.disk.inodesTotal | dt.host.disk.inodes\_total |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Inodes available % | builtin:host.disk.inodesAvail | dt.host.disk.inodes\_avail |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Reads (IOPS) | builtin:host.disk.readOps | dt.host.disk.read\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Writes (IOPS) | builtin:host.disk.writeOps | dt.host.disk.write\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Disk read time | builtin:host.disk.readTime | dt.host.disk.read\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Disk write time | builtin:host.disk.writeTime | dt.host.disk.write\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Disk utilization time | builtin:host.disk.utilTime | dt.host.disk.util\_time | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |
| Disk average queue length | builtin:host.disk.queueLength | dt.host.disk.queue\_length | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |

1

OneAgent version 1.313+ The disk available and disk total metrics are not sent when the total disk size exceeds 1024 petabytes (1024 PB).

2

Local only

3

Excluding GPFS

4

Since OneAgent 1.307

5

Excluding CIFS

6

GPFS only

7

Excluding CIFS/GPFS

8

Excluding NFS/CIFS/GPFS

## Network metrics per network interface controller (NIC)

Metrics representing the usage of network interface controllers on the host. They're collected by OneAgent network module.

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Bytes Received / s | builtin:host.net.nic.bytesRx | dt.host.net.nic.bytes\_rx |  |  |  |  |
| Bytes Sent / s | builtin:host.net.nic.bytesTx | dt.host.net.nic.bytes\_tx |  |  |  |  |
| Packets Received / s | builtin:host.net.nic.packets.rx | dt.host.net.nic.packets.rx |  |  |  |  |
| Packets Sent / s | builtin:host.net.nic.packets.tx | dt.host.net.nic.packets.tx |  |  |  |  |
| Dropped Packets Out / s | builtin:host.net.nic.packets.droppedTx | dt.host.net.nic.packets.dropped\_tx |  |  |  |  |
| Dropped Packets In / s | builtin:host.net.nic.packets.droppedRx | dt.host.net.nic.packets.dropped\_rx |  |  |  |  |
| Errors Out / s | builtin:host.net.nic.packets.errorsTx | dt.host.net.nic.packets.errors\_tx |  |  |  |  |
| Errors In / s | builtin:host.net.nic.packets.errorsRx | dt.host.net.nic.packets.errors\_rx |  |  |  |  |
| Send Utilization | builtin:host.net.nic.linkUtilTx | dt.host.net.nic.link\_util\_tx |  |  |  |  |
| Received Utilization | builtin:host.net.nic.linkUtilRx | dt.host.net.nic.link\_util\_rx |  |  |  |  |

## Availability

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Host availability | builtin:host.availability.state | dt.host.availability |  |  |  |  |
| Host uptime | builtin:host.uptime | builtin:host.uptime |  |  |  |  |

## Other

| Metric name | Metrics classic key | Metrics on Grail key |
| --- | --- | --- |
| Host Time Offset | builtin:host.la.to | unsupported |


---


## Source: hosts.md


---
title: Hosts
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts
scraped: 2026-02-06T16:29:11.779328
---

# Hosts

# Hosts

* Latest Dynatrace
* Overview
* 3-min read
* Published Sep 25, 2018

Host performance is tracked across multiple Dynatrace pages, beginning with high-level health metrics on dashboard tiles and extending down to dedicated pages for each of your hosts. Full-stack infrastructure monitoring begins automatically as soon as Dynatrace OneAgent starts operation and begins capturing performance and event-related information on your hosts.

Brief overview

### Host groups

With many Dynatrace-monitored environments growing larger and more complex all the time, often spanning different data centers and multiple applications, [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") are increasingly important. Host groups enable you to configure hosts per group, roll out OneAgent versions selectively per group, and track service metrics differently depending on the platform they run on.

### Virtualization performance insights

Dynatrace tells you how the virtual machines in your environment affect the performance of your applications and services. Once you include virtualization in your Dynatrace performance monitoring, you gain insight into your complete infrastructure stack and its behavior.

### Tags in a host-based configuration file

Within dynamic or large environments, manual host tagging can be impractical. For dynamic deployments that include frequently changing host instances and names (for example, AWS or MS Azure), you can [use a dedicated configuration file to programmatically apply tags to your hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.").

### Custom host names

Dynatrace generally names the detected hosts in your environment based on their DNS names, exactly as they are detected by Dynatrace OneAgent. To improve readability, you may want to [create custom host names](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.") to display instead of the detected host names.

## Basic concepts

[![Infrastructure Monitoring](https://cdn.bfldr.com/B686QPH3/at/jftqtgccnb2wt3h4ngf6z/Infrastructure_Observability.svg?auto=webp&width=72&height=72 "Infrastructure Monitoring")

### Monitoring modes

Find out what's included and how to enable Infrastructure Monitoring and Discovery modes.](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Find out what's included in Dynatrace Infrastructure Monitoring mode.")[### How effective is infrastructure monitoring on its own?

Learn how monitoring only the infrastructure layer of your environment can lead to an incomplete picture of the health of your applications and customer experience.](/docs/observe/infrastructure-observability/hosts/monitoring-modes/how-effective-is-infrastructure-monitoring-on-its-own "Learn how monitoring only the infrastructure layer of your environment can lead to an incomplete picture of the health of your applications and customer experience.")

## Configuration

[### Host anomaly detection

Configure host anomaly detection, including problem and event thresholds.](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.")[### Define tags and metadata for hosts

Tag and set additional properties for a monitored host.](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")[### Exclude disks and network traffic from host monitoring

Exclude selected disks and network traffic from host monitoring.](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic "Learn how to exclude selected disks and network traffic from host monitoring.")[### Organize your environment using host groups

Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.")[### Set custom host names

Change a monitored host name.](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.")

## Monitoring

[### Host monitoring with Dynatrace

Monitor hosts with Dynatrace.](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.")[### OS services monitoring

Improve the visibility of your infrastructure by monitoring the availability of operating system services.](/docs/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.")[### Classic Windows services monitoring

Improve the visibility of your infrastructure by monitoring the availability of Windows services.](/docs/observe/infrastructure-observability/hosts/monitoring/windows-services "Learn how to improve the visibility of your infrastructure by monitoring the availability of Windows services.")[### Process availability

Monitor availability and performance of the key processes on your hosts.](/docs/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts.")

## Diagnostics

[![OneAgent](https://cdn.bfldr.com/B686QPH3/at/g8mmkkpfmgwbxcjz54pvfsx/OneAgent.svg?auto=webp&width=72&height=72 "OneAgent")

### OneAgent diagnostics

Learn how to run OneAgent diagnostics.](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics")


---


## Source: containers.md


---
title: Containers
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/containers
scraped: 2026-02-17T21:17:51.612493
---

# Containers

# Containers

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 25, 2025

The  **Containers** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides a dedicated inventory for viewing, filtering, and inspecting containers independently or in relation to hosts and processes. Navigate between entities to see how they are interconnected.

This view supports containerized workloads orchestrated by ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** or running on a standalone host. Each container displays detailed information, including metadata, logs, events, and time-series charts for CPU, memory, and network traffic.

## Overview

The  **Containers** view provides different perspectives for viewing your containers (**Health**, **Utilization**, and **Metadata**).

The **Health** perspective includes the following default columns:

* **Container**: The container's unique name or identifier. Select the name for a comprehensive, full-page view with detailed metadata, logs, events, and time-series charts.
* **Container group name**: The group or deployment to which the container is assigned.
* **Custom alerts**: Lists any active custom alerts associated with the container.

Other perspectives provide additional columns, including **Containerization type** (the containerization technology in use) and **Container host name** (the host machine on which the container operates).

## Use cases

* View containers within a host

  Navigate from a host to see all containers running on it and the containerized workload distribution.
* Access detailed container information

  Select a container to access a full-page view with detailed metadata, logs, events, and time-series charts (for example, CPU, memory, network traffic) for deeper analysis and troubleshooting.
* Navigate between related entities

  Navigate between hosts, containers, and processes to see how they are interconnected and view the full infrastructure context.
* Group and filter containers

  Filter containers by container group, containerization type, and other metadata to organize and analyze containers based on operational or logical groupings.
* Identify critical issues

  Use the **Custom alerts** column and the **Critical alert** filter to quickly identify containers with problems. Select an alert to investigate it.
* Monitor resource usage

  Analyze and compare CPU and memory usage metrics across containers to optimize resource allocation.
* Drill down into container details

  Select a container name to view detailed graphs, processes, logs, and events for troubleshooting.
* Analyze trends

  Use the time selector and resource usage graphs to identify patterns or anomalies over time.


---


## Source: data-centers.md


---
title: Data centers
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/data-centers
scraped: 2026-02-17T21:17:46.756167
---

# Data centers

# Data centers

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 26, 2025

The  **Data centers** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** monitors the health and performance of your data centers and availability zones.

Select a data center to view all monitored hosts within it.

## Overview

Here's what each column in the  **Data centers** view stands for.

* **Data center**: The name or identifier of the data center or availability zone.
* **Type**: The type of data center, such as:

  + AWS Availability Zone
  + GCP zone
  + Azure Region
  + Geo Location Site
* **Hosts**:

  + **Total**: The total number of hosts in the data center.
  + **Unhealthy**: The number of hosts experiencing issues. Critical hosts are marked with red emphasis.
  + **Monitored**: The percentage of hosts actively monitored within the data center. Lower than 100% means Dynatrace identified unmonitored instances based on host connections.
* **Location**: The geographic name of the data center location.

## Use cases

* Identify critical issues

  Check the **Unhealthy** column and apply the Critical alert filter to quickly find data centers with problems. Selecting the alert indicator will take you to a filtered host list, focusing on the affected systems.
* Monitor coverage

  Review the **Monitored** column to ensure comprehensive tracking of all hosts. If you notice gaps in monitoring, you can use ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** to extend your oversight and achieve full coverage.


---


## Source: hosts.md


---
title: Hosts
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/hosts
scraped: 2026-02-17T21:17:44.421542
---

# Hosts

# Hosts

* Latest Dynatrace
* Explanation
* 3-min read
* Published Nov 25, 2025

The  **Hosts** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides comprehensive monitoring of your infrastructure hosts across physical machines, virtual machines, and cloud instances. Use this tool to track host health, performance metrics, and resource utilization to ensure optimal infrastructure operation.

Full-stack infrastructure monitoring begins automatically as soon as Dynatrace OneAgent starts operation and begins capturing performance and event-related information on your hosts.

## Overview

Here's what each column in the  **Hosts** view stands for.

* **Host**: The host's unique name or identifier. Select the name for a comprehensive, full-page view with in-depth details.
* **Monitoring mode**: The OneAgent monitoring mode configured for the host (Full-Stack, Infrastructure, or Discovery).
* **Health status**: Current health state of the host based on detected anomalies and alerts.
* **Custom alerts**: Lists any active custom alerts associated with the host.
* **Resource usage**: Provides metrics on CPU, memory, disk, and network consumption.
* **Host groups**: The logical grouping assigned to organize hosts across data centers and applications.

## Use cases

* Identify critical issues

  Use the **Custom alerts** column and health status filters to quickly identify hosts with problems. Selecting the alert takes you directly to the investigation view.
* Monitor resource utilization

  Analyze and compare CPU, memory, disk, and network usage metrics across hosts to optimize resource allocation.
* Organize environments

  Use [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to configure hosts per group, roll out OneAgent versions selectively, and track service metrics differently depending on the platform they run on.
* Drill down into host details

  Select a host name to view detailed graphs, processes, logs, events, and connected services for troubleshooting.

## Host monitoring with OneAgent

[#### OneAgent monitoring modes

Find out more about the available monitoring modes when using OneAgent.

* Explanation

Read this explanation](/docs/platform/oneagent/monitoring-modes/monitoring-modes)[#### Enable OneAgent monitoring modes

Learn how to enable monitoring modes when using OneAgent.

* How-to guide

Read this guide](/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes)


---


## Source: networks.md


---
title: Networks
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/networks
scraped: 2026-02-17T21:17:47.974243
---

# Networks

# Networks

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 25, 2025

The  **Network devices** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides insights into networking components and their availability, with analytics powered by [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence."). Dynatrace offers flexible network device observability, allowing you to choose the level of monitoring and onboarding process that fits your needs.

## Overview

The  **Network devices** view provides different perspectives for viewing your network devices (**Health**, **Utilization**, and **Metadata**).

The **Health** perspective includes the following default columns:

* **Network device**: The name or identifier of the network device. Select the name for a comprehensive, full-page view with detailed metadata and metrics.
* **Network area**: The logical grouping of network devices. Network areas are configured in the [SNMP Autodiscovery extension](/docs/observe/infrastructure-observability/extensions/snmp-autodiscovery "Scan through your subnets and build an inventory of SNMP-enabled network devices.").
* **Problems**: Lists any problems detected by Dynatrace Intelligence causal AI. Select a problem to access affected entities and investigate specific issues.
* **Reachability**: Indicates whether the device is reachable and responsive over the network.
* **Uptime**: The duration the device has been operational since the last restart.
* **Interface status**: The availability status of network interfaces.
* **Saturated interfaces**: Interfaces experiencing high utilization or congestion.

## Use cases

* Monitor device health

  Monitor health status, interface availability, network utilization, and hardware metrics such as CPU and memory usage.
* Identify and resolve issues

  View all problems detected by Dynatrace Intelligence causal AI and access affected entities to investigate and resolve specific issues.
* Filter and analyze devices

  Sort and filter network devices by name, type, problems, IP address, uptime, interface status, saturated interfaces, traffic volume, and reachability.


---


## Source: processes.md


---
title: Processes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/processes
scraped: 2026-02-17T21:17:43.194643
---

# Processes

# Processes

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 25, 2025

The  **Processes** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides a dedicated inventory for viewing, filtering, and inspecting processes independently or in relation to hosts and containers. Navigate between entities to see how they are interconnected.

Filter processes by host, container, process group, and other fields to analyze and compare across your environment. Each process displays detailed insights, including CPU and memory usage trends, logs, events, and time-series charts.

## Overview

The  **Processes** view provides different perspectives for viewing your processes (**Health**, **Utilization**, and **Metadata**).

The **Health** perspective includes the following default columns:

* **Process**: The process name or identifier. Select the name for a comprehensive, full-page view with detailed metadata, logs, events, and time-series charts.
* **Process group name**: The group to which the process belongs.
* **Health alerts**: Displays health alerts and warning signals powered by [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence."). For details, see [View health alerts and warning signals](/docs/observe/infrastructure-observability/infrastructure-and-operations#health-alerts "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.").
* **Custom alerts**: Lists any active custom alerts associated with the process.
* **Availability**: Shows the current availability status of the process.
* **Technologies**: The technologies detected for this process.

## Use cases

* Filter and inspect processes across multiple hosts and containers

  Use filters to view processes by host, container, process group, and other relevant fields, enabling broader analysis across your entire environment.
* Access detailed metrics and charts

  Select a process to access a full-page view with detailed metadata, logs, events, and time-series charts (for example, CPU, memory, network traffic) for deeper analysis and troubleshooting.
* Navigate between related entities

  Navigate between hosts, containers, and processes to see how they are interconnected and view the full infrastructure context.
* Identify problematic processes

  Use the **Health alerts** and **Custom alerts** columns with status filters to quickly identify processes with problems.
* Visualize resource trends

  Visualize CPU and memory usage trends across all processes using the graph view to compare performance and identify anomalies.
* Organize with tags

  Add technology-type tags at the process or process group level for simplified filtering and automation.
* Deep monitoring insights

  Drill down to detailed process-level insights, including versioning and release information, when deep monitoring is activated.


---


## Source: infrastructure-and-operations.md


---
title: Infrastructure & Operations
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations
scraped: 2026-02-17T21:13:51.746139
---

# Infrastructure & Operations

# Infrastructure & Operations

* Latest Dynatrace
* App
* 13-min read
* Updated on Jan 29, 2026

The ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** app simplifies infrastructure health monitoring and facilitates root cause analysis for problems.

* Health indicators powered by Dynatrace Intelligence help you detect early signs of performance degradation to quickly see which areas of your environment need attention.
* Check infrastructure host health metrics, logs, and events for all infrastructure entities.
* Drill down from ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** to any infrastructure entity metrics, logs, or events.

## Prerequisites

1. Deploy [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") on your hostsâit's the optimal choice to collect the most granular metrics and network insights.
2. If you are using cloud services, integrate your cloud infrastructure with Dynatrace. Follow the specific integration guides for AWS, Azure, Google Cloud, or other cloud providers.

### Permissions

The following table describes the required permissions.

Permission

Description

storage:logs:read

Query logs from GRAIL

storage:events:read

Query events from GRAIL

storage:buckets:read

Read buckets

storage:metrics:read

Query metrics from GRAIL

storage:entities:read

Query entities from GRAIL

storage:fieldsets:read

Read masked/sensitive fields

state:user-app-states:read

Read user-state

state:user-app-states:write

Write user-state

settings:objects:read

Read settings configurations from Settings 2.0

settings:objects:write

Write settings configurations to Settings 2.0

10

rows per page

Page

1

of 1

## Get started

![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides an up-to-date and comprehensive view of your monitored environments. Use the app to quickly identify areas that require attention and drill down to the exact root cause of issues.

![List view of all data centers, automatically sorted by Davis Intelligence identified problems.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.47.23.png)![Hosts view for a selected data center helps to quickly identify the most problematic hosts within the data center.  Drill down to host details.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.48.54.png)![View host health overview, properties, tags, and ownership information. Drill down to all host details.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.51.12.png)![Host health overview, technologies and all host entities such as disks and network interfaces. Drill down to process details and entity metrics.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.51.24.png)![Detailed process analysis. Drill down to process details.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.52.09.png)![Network device metrics overview.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_13.52.34.png)

1 of 6List view of all data centers, automatically sorted by Davis Intelligence identified problems.

### Navigation

The ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** app presents the data for your data centers, hosts, and network devices in lists.

Use the table options to navigate to the details that you need.

* To sort the table by a particular column, select the column header.
* To show or hide columns, select  **Column settings** and then select the columns you want to display.

#### Access details of entities

To get the details about an entity

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** and select  **Hosts** ,  **Containers**,  **Processes** or  **Network devices**.
2. Select an entity from the list. You can sort and filter the list as needed.

### Filtering

You can filter the tables in the app by using the filter field with listed suggestions. Currently, you can use basic syntax (grouping filter statements and using logical operators is not supported). As you type, the relevant options are displayed.

You can add several statements to narrow down the filter results. For example, `"Alert status" = Critical` `name != *1b*`. In this case, you narrow the search to hosts with more than 4 problems and names that don't include `1b`.

For more details on using filters, see [Filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").

### Segments

You can use segments in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** to logically structure observability data for your devices.

Some of the advantages of using segments are

* **Flexibility**: Segments can be used across different apps that support that feature.
* **Ease of use**: You can create and use complex filters quickly.
* **Option to share**: You can share filters across different users.

#### Apply a segment

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** >  **Segments**.
2. Select the segment name from the drop-down menu. If needed, select parameters for the selected segment.
3. Select **Apply** to activate the segment.

#### Add a segment

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** >  **Segments**.
2. Select  **Manage segments** >  **Segment**.
3. Add a name for the segment.
4. Optional Add a description.
5. Use one of the available options for filtering data

   * Add a variable. This requires creating a query.
   * Add data types. Select from the available options in the menu.
   * Add entities and topology. Select from the available options in the menu.
6. Select **Save**.

For more details on managing segments, refer to [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.").

### Analyze overview charts

You can define which metrics are displayed in the charts by selecting ![Expand menu](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Expand menu") in the upper left corner of each graph or chart.

#### Export data to Notebooks

To further analyze the data from ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.
2. Select an entity to see its details.
3. Select the graph or chart you want to analyze and select  > **Open in Notebooks** ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with").
4. Choose whether to open the graph in a new or existing notebook.

### View host processes

The **Processes** tab in the host full-page view displays the **CPU usage** and **Memory usage** charts with a table showing 5 contributors.

To view processes on a host

1. Open the full-page view of a host.
2. Select the **Processes** tab.

The **CPU usage** and **Memory usage** charts display with a table showing 5 contributors. Change the contributors by selecting other metrics, such as health alerts, custom warnings, and CPU usage.

To view all processes across your environment, switch to the [Processes](#processes) inventory.

Note that processes can run directly on hosts or in containers running on hosts.

### Display code-module metrics

You can inject code modules and display the injected data in the app. For more details, see [Universal injection of code modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#universal-injection "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

After selecting a process from the list, the data is presented in a dedicated tab.

### Monitor incoming and outgoing connections

In the full-page view of a host, under **Connections**, you can see a quick overview of each type of connection, the total number of connected entities, and the number of problems. Expand the panel to see a list of connected entities and possible problems for each of them. You can also see which processes from the current host communicate with other processes or services that aren't part of the host.

The **Connections** table allows you to identify potential sources of problems that don't happen directly on the host. Select the connected entity marked with  to navigate to its details page and investigate the issue.

The incoming and outgoing process connections in the table display processes with the most issues based on network and CPU usage.

### Measure the reachability of a host or device

The **Reachability** column on the **Hosts** and **Network devices** pages shows how easily you can access a device or a host over the network from a remote location. For more details, see [Synthetic Monitoring](/docs/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

The value presents the ratio of fully available Network Availability Monitors (NAM) (with 100% availability over the selected time period) to all configured monitors for the given host or network device.

To use this feature, you need to configure NAM for the desired device or host. For details, refer to [Configure a NAM monitor](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor "Learn how to set up a NAM monitor to check the performance and availability of your site.").

### View health alerts and warning signals

In ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, you can view health alerts and warning signals.

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

To take advantage of this feature in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, you need to enable it. Once enabled, certain alerts that were previously classified as critical will be reclassified as warnings, as they are not considered critical enough to require immediate attention.

To enable this option

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. Select  **Analyze and alert** > **Alerts**.
3. Under **Category update**, select **Ready-made alerts category update**.
4. Enable **Updated classification for select ready-made alerts**.

Once you enable the option, these alerts will be converted to warnings:

| Entity type | Event type[1](#fn-1-1-def) | Description |
| --- | --- | --- |
| HOST | OSI\_HIGH\_CPU | CPU Usage |
| HOST | OSI\_NIC\_DROPPED\_PACKETS\_HIGH | High rate of dropped packets |
| HOST | RESOURCE\_CONTENTION | Slow disk |
| PGI | PROCESS\_RESTART | Process restart |

1

Once converted into warnings, the events with the `event.type` listed here, will be marked as `event.type = WARNING`. Their former value is removed.

### View data from imported technologies

![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** detects installed extensions and displays them in the **Technologies** inventory. Extensions are organized by category, making it easy to explore and analyze your technology stack.

To view installed technologies

1. Go to ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** > **Technologies**.
2. Select an extension from the list to view more details.

For details on setting up extensions, see [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

Minimum required versions of extensions

Ensure your system has these minimum versions of the installed extensions to avoid any issues with displaying the data in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.

This list concerns extensions for supporting network devices and is not exhaustive. Each network device can have more extensions.

| Extension | Minimum version |
| --- | --- |
| SNMP Autodiscovery | 2.2.8 |
| Generic Cisco Device | 2.1.4 |
| F5 BIG-IP | 2.10.0 |
| Palo Alto firewalls | 2.7.0 |
| Juniper Networks (SNMP) | 1.5.0 |
| Generic network device | 2.0.0 |
| Fortigate | 1.2.21 |

See our detailed [Generic network topology](/docs/ingest-from/extend-dynatrace/extend-topology/network-topology "Use the generic network topology model available in Dynatrace extensions.") guide on how to make your custom extensions appear in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**.

## Concepts

![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** has the following core components:

[#### Data centers

Monitor the health and performance of your data centers and availability zones to detect and resolve critical issues.

Data centers](/docs/observe/infrastructure-observability/infrastructure-and-operations/data-centers)[#### Hosts

Monitor infrastructure hosts across physical machines, VMs, and cloud instances to track health, performance, and resource utilization.

Hosts](/docs/observe/infrastructure-observability/infrastructure-and-operations/hosts)[#### Containers

Monitor and troubleshoot containerized workloads across Kubernetes and standalone hosts.

Containers](/docs/observe/infrastructure-observability/infrastructure-and-operations/containers)[#### Processes

Monitor processes running on hosts and containers with detailed insights into CPU and memory usage trends and key metrics.

Processes](/docs/observe/infrastructure-observability/infrastructure-and-operations/processes)[#### Networks

Monitor network devices and gain insights into networking components with Dynatrace Intelligence-powered analytics and flexible observability options.

Networks](/docs/observe/infrastructure-observability/infrastructure-and-operations/networks)

### Relation between hosts, containers, and processes

Hosts, containers, and processes are interconnected, and you can navigate between them to understand dependencies and troubleshoot issues.

#### Hosts

* The host full-page view includes **Processes** and **Containers** tabs showing related processes and containers. Select an entity to navigate to its details.

#### Containers

* Containers run on hosts. The container metadata displays the host name.
* The container full-page view includes an **Overview** tab with links to the host and container group. Selecting the host navigates to the host details. Selecting the container group filters the container list to show all containers in that group.
* The **Processes** tab shows related processes. Select a process to navigate to its details.

#### Processes

* Processes run directly on hosts or in containers. The process metadata displays the related host and container name (if applicable).
* The process side panel shows information about technologies, host, process group, container (if applicable), and deep monitoring details.
* The process full-page view includes an **Overview** tab with links to the host, process group, and container (if applicable). Selecting the host navigates to the host details. Selecting the process group filters the process list to show all processes in that group. Selecting the container navigates to the container details.

## Use cases

* View and identify the status of all data centers, hosts and network devices.
* Quickly identify the root cause of infrastructure problems
* Gain awareness of infrastructure performance and optimize it

  + See data center health at a glance and identify problematic data centers
  + Quickly see host health and identify problematic hosts, network devices, technologies, processes, disks, containers, and networks
  + See infrastructure host health metrics, logs, and events for all infrastructure entities
  + See network devices health metrics, traps, and events.
  + Assess the network reachability of hosts and network devices by integrating with synthetic Network Availability Monitors (NAM).

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

View the status of all data centers and hosts and identify the root cause of infrastructure problems.](https://www.dynatrace.com/hub/?filter=infrastructure-monitoring&internal_source=doc&internal_medium=link&internal_campaign=cross)


---


## Source: existing-clusters.md


---
title: Enable Kubernetes experience for existing clusters
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience/existing-clusters
scraped: 2026-02-17T21:13:43.078386
---

# Enable Kubernetes experience for existing clusters

# Enable Kubernetes experience for existing clusters

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 19, 2024

You have the option to enable all or specific Kubernetes clusters to benefit from the new Kubernetes experience.

You could accomplish this using the Settings API with the [Kubernetes app schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes "View builtin:app-transition.kubernetes settings schema table of your monitoring environment via the Dynatrace API."), or alternatively, by configuring the setting as described next.

## Enable all clusters

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Turn on **New Kubernetes experience**.

## Enable specific clusters

1. In ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, select **Activation pending** in the top menu bar.
2. Select **Activate** for your desired cluster.

   ![Activation pending](https://dt-cdn.net/images/activation-pending-3718-f43bc57878.png)
3. Turn on **New Kubernetes experience**.

When you enable Kubernetes clusters for the new Kubernetes experience, Dynatrace starts to report observability data to the Dynatrace platform, including Grail as a data lakehouse.


---


## Source: enhanced-object-vis-preview.md


---
title: Kubernetes Enhanced Object Visibility Preview
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/preview/enhanced-object-vis-preview
scraped: 2026-02-17T05:01:28.825038
---

# Kubernetes Enhanced Object Visibility Preview

# Kubernetes Enhanced Object Visibility Preview

* Latest Dynatrace
* Explanation
* Updated on Jan 28, 2026

Completed preview

The Kubernetes Enhanced Object Visibility Preview introduces a new way to explore Kubernetes environments in Dynatrace, offering deeper visibility, improved performance, and powerful troubleshooting capabilities. **The preview is completed since December 2025**.

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine

  + There is a very small exception for a few specific tenants that won't be able to access the preview. More information on that will be available within the product.
* [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") with the **Kubernetes Platform Monitoring** capability on your Rate Card
* [Sufficient permissions](/docs/observe/infrastructure-observability/kubernetes-app/reference/permissions "Overview of user and tailoring permissions.") to use ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** within your Dynatrace environment
* Dynatrace version 1.324+
* ActiveGate version 1.323+
* Dynatrace Operator version 1.7.0+
* Kubernetes app version 1.33.0+

Overview

Setup

FAQ

By enabling this preview, youâll gain:

* Visibility into additional Kubernetes objects: Ingress, NetworkPolicies, CRDs, PVCs, PVs, ConfigMaps, and more.
* Access to YAML definitions to debug and validate configurations in real time.
* Ability to query YAMLs across all clusters and namespaces using Dynatrace Query Language (DQL) to instantly surface misconfigurations, missing references, or policy violations across your Kubernetes environment

Specifically, this preview unlocks visibility into:

* Storage: Persistent Volumes (PV), Persistent Volume Claims (PVC)
* Networking: Ingress, Network Policies
* Custom Resources: CRDs and selected CRs
* Optional Configuration: ConfigMaps and Secrets

  + Secrets and ConfigMaps are not ingested by default due to their potentially sensitive content. To monitor these Kubernetes objects, you can manually grant the necessary permissions. For instructions on how to enable ConfigMaps and Secrets, see the [Setup tab](#setup).

This preview also adds insights into the YAML files of all Kubernetes objects, allowing you to inspect object configurations directly in Dynatrace. Turn on **Watch** to stream updates of these configurations within a few seconds to the web UI, allowing for fast validation of recent changes. The YAML is currently limited to a size of 32 kb, and we automatically strip less important fields (for example, `/metadata/managedFields` and `kubectl.kubernetes.io/last-applied-configuration` annotation).

These additions are available upon opt-in on the additional **Explorer (Preview)** tab in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

![Enhanced object visibility preview in the Kubernetes app.](https://dt-cdn.net/images/k8s-enhanced-object-visibility-preview-1920-7aa7863ffb.png)

A variety of further use-cases are unlocked, by allowing users to query all YAML files also via DQL. You can find a notebook with different examples within our [communityï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132).

To opt in to this preview, go to **Settings** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**. This setting is available within the scope of your tenant or within the scope a monitored Kubernetes cluster.

We recommend getting started by enabling the preview only for a single Kubernetes cluster first, as this new functionality might increase the load on the ActiveGate monitoring this cluster. To enable this only for one cluster, go to the Settings of a selected cluster within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and select  > **Connection settings** in the upper-right corner of the cluster's detail page.

![Enable Kubernetes Enhanced Object Visibility](https://dt-cdn.net/images/k8s-enable-public-preview-7e45dfe3d5.gif)

If you've set tight resource constraints (CPU and memory limits) on the ActiveGate monitoring this cluster, this might cause interruptions in your monitoring. You can easily remedy that by increasing the configured limits, or by removing them temporarly to find a good fit for new limits. While the ingest of additional data can be controlled on a cluster-by-cluster basis, the additional **Explorer (Preview)** tab within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** is available as soon as any cluster is enabled for the preview.

## Unlocking ConfigMaps and Secrets

To gain visibility into ConfigMaps and Secrets, you need to grant additional permissions to the ActiveGate, allowing it to access these objects. By default, this functionality is disabled because these objects might contain sensitive data. For Secrets, ActiveGate automatically applies data masking.

Apply the following YAML with `kubectl` to enable these objects:

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: dynatrace-kubernetes-monitoring-sensitive



subjects:



- kind: ServiceAccount



name: dynatrace-kubernetes-monitoring



namespace: dynatrace



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



labels:



rbac.dynatrace.com/aggregate-to-monitoring: "true"



rules:



- apiGroups:



- ""



resources:



- configmaps



- secrets



verbs:



- list



- watch



- get
```

## Does this preview increase my DPS consumption?

The preview builds upon the existing ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and the corresponding license based on [pod-hours](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged."). The consumed pod-hours include insights into all newly added Kubernetes objects, meaning there won't be any increase in DPS consumption specific to this preview.

## What happens technically by joining this preview?

Dynatrace starts to ingest Kubernetes objects additionally into the new Smartscape. The newly unlocked objects (for example, Ingress, Network Policies) will only be available in the new Smartscape. This unlocks easier DQL access, faster queries, and access to the YAML of these objects. We will continue to write the existing entities into the old storage. In our [communityï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132), you also find a notebook that helps you get started working with Kubernetes objects stored in the new Smartscape using DQL. Within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, the new **Explorer (Preview)** automatically leverages the new Smartscape in the background, while the already existing **Explorer** continues to operate on data stored in our old storage.

## Where will this preview go from here?

The **Explorer (Preview)** will incrementally improve over the next months until it includes all the same features as the existing **Explorer**. With the GA of this new functionality, **Explorer (Preview)** will replace the existing **Explorer** for everyone, and we also plan to include more custom resources. We would be happy to hear [your feedbackï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132) on which ones would be most important to you.
We will continue for some time to offer the entities that powered the former **Explorer** via DQL (for example, fetch dt.entity.cloud\_application).

## What observability option do I need for this preview? Do I need Full-Stack observability?

This preview is based on **Kubernetes platform monitoring**, which is included in all [observability options](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

## What are top-level workloads?

A top-level workload is the topmost controlling owner of a Pod.
Possible top-level workload types are: Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, CronJob, ReplicationController, DeploymentConfig.
A list of those workloads can be found in the `Top-level workloads` menu entry.

## What do I see in the `Definition (YAML)` view?

When first opening this view you see a reduced version of the original YAML as available from the Kubernetes API. When you activate the live mode, you get full YAML directly streamed from the Kubernetes API.

The reduced version of the YAML is also available in json format via DQL in the `k8s.object` field of the respective Smartscape node.
Please note, that labels and annotation are not part of this field, but are stored as `tags`.

## How can I fix missing `ClusterRole` permissions?

The newly added Kubernetes object types require additional ActiveGate permissions. These permissions (except for ConfigMaps and Secrets [1](#fn-1-1-def)) are automatically granted when Dynatrace Operator is updated to [version 1.7.0](/docs/whats-new/dynatrace-operator/dto-fix-1-7-0 "Release notes for Dynatrace Operator, version 1.7.0"). Customers using older Dynatrace Operator versions, or those who manually have overwritten the ActiveGate permissions, may lack access to the new Kubernetes endpoints. If permissions are missing, a warning message appears above the table (for example `Missing "ConfigMap" ClusterRole permission for cluster(s): aks-playground-dev.`):

![How can I fix missing ClusterRole permissions?](https://dt-cdn.net/images/image-20250909-123859-2305-e1ca79056f.png)

To fix this, [update your Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#update "Upgrade and uninstallation procedures for Dynatrace Operator") to version 1.7.0+.

1

ConfigMaps and Secrets can contain sensitive information. Therefore, Dynatrace Operator version 1.7.0 does not grant permissions to these endpoints by default. To enable access to these objects, follow the guidance provided in [Unlocking ConfigMaps and Secrets](#setup).

## Learn more

Dive deeper into ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** with the following resources:

[### Feedback channel for Kubernetes Enhanced Object Visibility Preview

You can find a notebook with different examples within our community.](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132)

[### Playground environment

Test the app in a sandbox environment.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.kubernetes)[### 0 to Full Observability in Kubernetes in under 3 minutes

A quick video tutorial on how to install Dynatrace Operator.](https://dt-cdn.net/resources/product/videos/k8s-0-to-full-observability.mp4)[### Blog post: Unlock the Power of DevSecOps with Newly Released Kubernetes Experience for Platform Engineering](https://www.dynatrace.com/news/blog/kubernetes-platform-engineering/)


---


## Source: permissions.md


---
title: Permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/reference/permissions
scraped: 2026-02-17T21:13:39.650171
---

# Permissions

# Permissions

* Latest Dynatrace
* Reference
* 1-min read
* Published Jan 19, 2024

This guide outlines the necessary permissions for ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and describes how to tailor them to fit specific roles and requirements.

## User permissions

To fully utilize all use cases of ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, a specific set of permissions is required. You can find the complete list of these permissions via Dynatrace Hub.

In Dynatrace Hub, select **Kubernetes** ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") to view the necessary permissions.

To manage permissions within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, you can assign default policies to different roles assigned to user groups (such as **AppEngine User**, **Storage All Grail Data Read**).

## Tailoring permissions/policies

Dynatrace IAM allows for a highly detailed and flexible definition and assignment of permissions. These permissions can be grouped into policies and then assigned to users or groups. Additionally, permissions can be targeted to specific subsets of Kubernetes objects by using conditions, such as for particular clusters and/or namespaces.

For more information, see [Identity and access management (IAM)](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Example policy

```
ALLOW hub:catalog:read;



ALLOW storage:buckets:read, storage:entities:read, storage:events:read, storage:logs:read, storage:metrics:read;



ALLOW environment-api:api-tokens:write, environment-api:entities:read, environment-api:entities:write, environment-api:metrics:read, environment-api:security-problems:read, environment-api:slo:read;



ALLOW settings:objects:read, settings:objects:write, state:user-app-states:read, state:user-app-states:write;



ALLOW davis:analyzers:execute, unified-analysis:screen-definition:read;
```


---


## Source: alert-use-case.md


---
title: Alert on common Kubernetes misconfigurations and detect anomalies with Kubernetes metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/use-cases/alert-use-case
scraped: 2026-02-17T04:57:19.343982
---

# Alert on common Kubernetes misconfigurations and detect anomalies with Kubernetes metrics

# Alert on common Kubernetes misconfigurations and detect anomalies with Kubernetes metrics

* Latest Dynatrace
* Tutorial
* 2-min read
* Published Sep 28, 2023

Kubernetes is an integral part of many organizations' infrastructure. With the vast number of nodes and pods in a typical Kubernetes infrastructure, it's important to have a scalable alerting solution.

## Real-world scenario

One of the primary applications of Kubernetes alerts is to detect anomalies in your infrastructure immediately.

For instance, consider a scenario where pods failed to start up in a production environment, but everything worked seamlessly in staging. While there was no immediate impact on production (no traffic routed to unready pods), Dynatrace alerted on a deployment that couldn't progress (deployment stuck), meaning the latest version couldnât be rolled out.

Using a combination of Kubernetes events and application logs in Dynatrace, it was determined that a DNS issue was the root cause. By adjusting the Kubernetes network policies, the problem was resolved.

![Use case problem](https://dt-cdn.net/images/screenshot-2023-09-28-at-6-02-41-pm-1168-994dc600da.png)

## Benefits

Kubernetes out-of-the-box (OOTB) alerts can be easily configured within the global anomaly-detection settings. With this feature, you can achieve:

* **Quick setup**: OOTB alerts, including those for Kubernetes, come preconfigured, which ensures that monitoring setups often take less than 5 minutes.
* **Streamlined monitoring**: OOTB alerts automate the oversight of multiple metrics, centralizing the monitoring process and reducing the need for frequent manual checks.
* **Responsive adaptability**: The feature adjusts alerting thresholds based on real-time cluster loads, ensuring relevant monitoring and minimizing potential human errors.
* **Direct navigation**: Navigate to the settings related to your namespace directly from Dynatrace and adapt everything to your needs without the need for external configurations.
* **Default configurations**: Set up default alert configurations for all active and future Kubernetes clusters, namespaces, and workloads, ensuring consistent monitoring as your infrastructure grows.
* **Granular customization**: Customize alert settings at various levels, allowing you to handle alerts differently for production and development clusters and adjust node alerts within each.
* **Automation with Dynatrace API**: Leverage the Dynatrace API to automate configurations, ensuring that your alerting system evolves smoothly with your infrastructure changes. Moreover, with the Dynatrace API, you can adopt the [Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") approach to configure alerts, integrating them into a GitOps workflow.

## Getting started

Alerts for common Kubernetes issues can be configured on three levels:

* **Environment**: Settings apply to all clusters, nodes, namespaces, or workloads in the Kubernetes environment.
* **Cluster**: Settings specific to individual clusters.
* **Namespace**: Settings specific to individual namespaces.

To configure these settings

1. Go to **Settings** > **Anomaly detection**.
2. Under **Kubernetes**, select any option.

For complete details on this feature, see [Alert on common Kubernetes/OpenShift issues](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.").


---


## Source: predictive-operations.md


---
title: Predictive Kubernetes operations
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/use-cases/predictive-operations
scraped: 2026-02-17T21:28:38.888434
---

# Predictive Kubernetes operations

# Predictive Kubernetes operations

* Latest Dynatrace
* Tutorial
* 9-min read
* Updated on Feb 04, 2026

In today's dynamic IT landscape, managing disk space effectively in Kubernetes-based services is crucial for maintaining optimal performance and avoiding potential data loss.

This best practice guide demonstrates how teams can utilize Dynatrace workflows for automated disk resizing to proactively manage disk space within Kubernetes environments.

Designed for ease of understanding by both technical and non-technical audiences, this guide highlights the value of automating disk space management. By implementing this practice, teams can significantly reduce manual intervention, ensure smooth operations of their Kubernetes services, and maintain system efficiency. The approach focuses on preemptively addressing disk space issues before they escalate, thereby safeguarding data integrity and enhancing overall service performance.

## Target audience

This use case is intended for system administrators, DevOps engineers, and site reliability engineers (SREs) who manage Kubernetes-based services and infrastructure.

You should have a basic understanding of Kubernetes environments, including concepts like nodes, pods, and disk utilization.

Familiarity with Dynatrace, particularly its AI capabilities like Dynatrace Intelligence for predictive analytics and automated workflows, is beneficial but not mandatory. The content is also relevant for teams looking to automate and improve their Kubernetes infrastructure management, ensuring optimal performance and resource utilization without the need for deep technical expertise in Dynatrace.

This guide aims to provide practical steps for those responsible for maintaining the stability and efficiency of Kubernetes services, especially in scenarios of dynamic resource requirements.

## Scenario

In a large-scale Kubernetes environment, an operations team is responsible for managing multiple nodes and critical services that require constant and efficient disk space management. They face a challenge: ensuring optimal disk utilization for each service without manual intervention. The team needs a scalable solution that can proactively manage disk space to prevent service disruptions and data loss, especially during unexpected spikes in traffic or resource demand.

The current process of manually monitoring and resizing disks is time-consuming and prone to errors, leading to either over-provisioning (wasting resources) or under-provisioning (risking service disruption). The team seeks an automated approach to dynamically adjust disk space based on real-time usage and projected needs.

By implementing the automated disk resizing feature in Dynatrace, the team aims to:

* Automatically detect and address disk space shortages within the Kubernetes environment.
* Use predictive analytics to calculate required disk space adjustments in real time.
* Ensure consistent application of configuration changes across all Kubernetes clusters.
* Reduce manual monitoring and intervention, thus saving time and resources.

This scenario illustrates a common challenge in managing Kubernetes-based services at scale and how Dynatrace automation capabilities can provide an efficient solution. The goal is to maintain uninterrupted service and optimal performance through intelligent, automated disk management.

This particular case is an example on how to make sure that on a sudden spike in traffic, an immediate need for extra disk space for Kafka is allocated to accommodate the increased message queue.

## Prerequisites

Make sure all of these are true before you start.

### Permissions

* You have access to a Dynatrace environment with the necessary permissions for configuration and monitoring.
* You have access to Kubernetes Configurations and you're able to retrieve and modify Kubernetes service configurations for disk size adjustments.

### Knowledge

* You have basic knowledge of Kubernetes architecture, including nodes, pods, and services.
* You have experience with Kubernetes Disk Management: Understanding of disk utilization in Kubernetes and the challenges associated with managing disk space in dynamic environments.
* You know how to set up automated workflows in Dynatrace for responding to disk space alerts. See [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* You know how to set up monitoring and alerting mechanisms within Dynatrace for Kubernetes environments.
* You understand GitOps principles, particularly for managing Kubernetes configurations through repository-based approaches.

## Steps

To keep the internal systems up and running, create an automated workflow for Kubernetes (K8s) disk management. This process is tailored to ensure critical internal services maintain optimal performance, even when unexpected disk utilization spikes occur. By leveraging continuous monitoring and automated remediation steps, downtime is minimized and maintains the consistency of the operations.

### 1. Set up continuous monitoring

[Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") to continuously monitor all services within the Kubernetes infrastructure. When your monitoring is providing you with data, [set up an alert](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") for disk utilization exceeding a 60% threshold to ensure optimal performance without resource wastage. With this alert, you'll be able to model a workflow for solving a disk size shortage issue.

### 2. Set up configuration file retrieval through ownership

With [ownership](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") assigned to objects, you can store the repository information. On detecting an anomaly, the system identifies the impacted service and fetches its associated configuration file. This step ensures that any adaptation made aligns directly with the specific service configuration.

### 3. Set up a workflow

Use the configuration retrieval on the alert to trigger the workflow. The workflow is composed of the following steps:

1. Identify the host with the disk that needs your attention.
   Use DQL as your workflow input.

   ```
   fetch dt.entity.host | filter like(entity.name, "%-grail kafka") | limit 1
   ```
2. Identify the disk.
   Use DQL as your workflow input.

   ```
   fetch dt.entity.disk  | fieldsAdd belongs_to[dt.entity.host] | filter belongs_to[dt.entity.host] == "{{result('query_grail_kafka_hosts').records[0].id}}"
   ```
3. Use Dynatrace Intelligence to calculate the necessary disk size.

   Dynatrace Intelligence analyzes the current disk usage compared to expected inflows, determining the appropriate disk size adjustment. This calculated response ensures both immediate and future needs are addressed.

   Use the Run Javascript workflow action to extract the prediction using the Dynatrace SDK [Automation utils packageï»¿](https://developer.dynatrace.com/reference/sdks/automation-utils/).

   Show me code

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function ({ executionId }) {



   const ex = await execution(executionId);



   // In this demo workflow we use a previous grail query to get a valid host ID.



   // Usually this would come from a Davis Event



   const res = await ex.result("analyze_with_davis_1");



   let prediction = 0.0;



   let validPrediction = true;



   try {



   const points = res.result.output[0].timeSeriesDataWithPredictions.records[0]["dt.davis.forecast:point"];



   console.log("Got these prediction: %s", points);



   const floatPoints = points.map(p => Number(p));



   prediction = Math.max(...floatPoints);



   console.log("Max value is: %s", prediction);



   } catch (e) {



   console.error("Unable to predict: %s", e instanceof Error ? e.message : JSON.stringify(e));



   validPrediction = false;



   }



   return {



   prediction,



   validPrediction,



   };



   }
   ```
4. Determine the ownership.
   Knowing the ownership will enable you to pick the right repository to apply the new disk size configuration.

   * Use the Ownership action to identify the owners of the disk entity you identified earlier.
   * With the ownership information, in the next step, you'll be able to identify the right repository to apply the change:

     Show me code

     ```
     import {



     monitoredEntitiesClient



     } from "@dynatrace-sdk/client-classic-environment-v2";



     import {



     execution



     } from '@dynatrace-sdk/automation-utils';



     async function getEntityName(entityId) {



     const data = await monitoredEntitiesClient.getEntity({



     entityId: entityId,



     });



     return data.displayName;



     }



     function isKafkaEntity(entityName) {



     return entityName.match(/(\[a-z0-9-]+)-grail kafka/) !== null;



     }



     async function getKafkaConfigURL(ex, entityName) {



     const owners = (await ex.result("get\_owners")).owners;



     let repoLink = undefined;



     // Go though all the owners and figure out which one as a REPOSITORY link type set.



     // We assume that is the correct one and will just use it later for building the URL



     for (const owner of owners) {



     for (const link of owner.links) {



     if (link.linkType === "REPOSITORY") {



     repoLink = link.url;



     break;



     }



     }



     if (repoLink !== undefined) {



     break;



     }



     }



     // "Gracefully" fail and tell the user that no owner had the required link type set;



     // Helps with debugging since otherwise we would build a URL undefined/... which can



     // cause more problems down the line.



     if (repoLink === undefined) {



     throw new Error('No REPOSITORY link was provided for any tagged owner!')



     }



     const baseUrl = repoLink;



     const file = "app//kafka-worker/kafka-configuration/values-scoped.yaml";



     const cluster = entityName.match(/(\[a-z0-9-]+)-grail kafka/)\[1];



     return `${baseUrl}/${cluster}/${file}`;



     }



     export default async function({



     execution\ _id



     }) {



     const ex = await execution(execution\ _id);



     // In this demo workflow we use a previous grail query to get a valid host ID.



     // Usually this would come from a Davis Event



     const queryResults = await ex.result("query\_grail\_kafka\_hosts");



     const records = queryResults.records;



     // Only have a look at the first element because an event likely only



     // contains one element:



     const {



     id



     } = records\[0];



     // Use the following DQL to query host IDs for grail kafka entities



     // >>> fetch dt.entity.host | filter like(entity.name, "%-grail kafka")



     const name = await getEntityName(id);



     // name should be used here, but only if isKafkaEntity is true!



     return {



     isKafkaHost: isKafkaEntity(name),



     url: await getKafkaConfigURL(ex, name)



     };
     ```
5. Commit and create pull request/merge file.

   Use the Kubernetes workflow action to apply the new configuration. With the desired disk size identified, the workflow automatically creates a pull request. This pull request adapts the service configuration file to reflect the newly determined disk size.

   Show me code

   ```
   apiVersion: batch/v1



   kind: Job



   metadata:



   name: {{ "demo-job-resize-%s" % result('disk_from_host').records[0].id | lower }}



   labels:



   joblabel: "test"



   spec:



   ttlSecondsAfterFinished: 300



   backoffLimit: 0



   activeDeadlineSeconds: 60



   podFailurePolicy:



   rules:



   - action: FailJob



   onExitCodes:



   operator: NotIn



   values: [0]



   template:



   spec:



   restartPolicy: Never



   containers:



   - name: main



   image: docker.io/library/bash:5



   command: ["bash"]



   args:



   - -c



   - echo "Computing..."; sleep 10; echo $PATH_URL; echo $IS_KAFKA_HOST; echo $PREDICTION; echo $VALID_PREDICTION; test $VALID_PREDICTION = 'True'; exit $?



   resources:



   limits:



   memory: 10Mi



   cpu: 1m



   env:



   - name: PATH_URL



   value: "{{result('repository_url').url}}"



   - name: IS_KAFKA_HOST



   value: "{{result('repository_url').isKafkaHost}}"



   - name: PREDICTION



   value: "{{result('extract_prediction').prediction}}"



   - name: VALID_PREDICTION



   value: "{{result('extract_prediction').validPrediction}}"
   ```
6. Deploy.
   The modified configurations are deployed into the service through ArgoCD and ArgoWorkflows. This quick deployment minimizes service disruption and ensures that the adjustments are immediately effective.
7. Post-Deployment validation.
   After the configuration rollout, there's a validation phase where the system checks if the disk resize was successful and if the initial anomaly has been resolved.

If any issue arises during the workflow, the Dynatrace alerting system ensures that potential complications get immediate attention. The workflow also incorporates the Ownership feature that determines the responsible entity for a given issue, ensuring efficient communication, for example using the Slack workflow action.

## Conclusion

By implementing automated disk resizing in Kubernetes environments with Dynatrace, teams can effectively manage disk space, ensuring their services run smoothly and efficiently. This guide has provided a comprehensive approach to setting up continuous monitoring, automating configuration updates, and ensuring effective deployment and validation. The integration of Dynatraceâs AI capabilities allows for predictive adjustments, reducing manual efforts and enhancing system reliability.

With these steps in place, teams can focus more on strategic tasks rather than constant monitoring and manual interventions. The ability to proactively manage resources in a Kubernetes environment is a significant step towards optimizing infrastructure performance and minimizing potential disruptions or data loss.

To fully leverage these benefits, you're encouraged to try implementing these practices in your Kubernetes environments. Experiment with the settings, monitor the results and adjust as necessary to fit your specific needs.

Explore further how Dynatrace can transform your approach to Kubernetes management, bringing efficiency and predictability to your operational workflows.

## Related topics

* [AI in Workflows - Predictive maintenance of cloud disks](/docs/dynatrace-intelligence/use-cases/davis-for-workflows "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")
* [Dynatrace Intelligence DQL examples](/docs/dynatrace-intelligence/use-cases/davis-dql-examples "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")


---


## Source: kubernetes-app.md


---
title: Kubernetes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app
scraped: 2026-02-17T21:13:24.516340
---

# Kubernetes

# Kubernetes

* Latest Dynatrace
* App
* 7-min read
* Updated on Jan 30, 2026

The latest [Kubernetes experienceï»¿](https://dt-url.net/k1038uw) is optimized for DevOps Platform Engineers and Site Reliability Engineers (SREs), focusing on the health and performance optimization of multicloud Kubernetes environments. The centerpiece of this experience is [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**ï»¿](https://dt-url.net/mx238j5).

The underlying metrics, events, and logs are all powered by [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), which supports flexible analytics through the [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, and ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

## Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine
* [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") with the **Kubernetes Platform Monitoring** capability on your Rate Card
* [Sufficient permissions](/docs/observe/infrastructure-observability/kubernetes-app/reference/permissions "Overview of user and tailoring permissions.") to use the ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** within your Dynatrace environment
* ActiveGate version 1.327+ is a prerequisite for [Kubernetes Enhanced Object Visibility](#enhanced-object-visibility).

  + Older ActiveGate versions are supported in backward compatibility mode; in that mode, an additional **Explorer (Classic)** tab appears in the UI.

For more details, see [getting started FAQ](/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience#k8s-app-getting-started-faq "Enable Kubernetes experience for existing clusters or start monitoring new clusters.").

The new Kubernetes experience is not available for Managed or SaaS on non-Grail environmentsâyou can continue to use [**Kubernetes Classic**](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.") (accessible from the previous Dynatrace via **Kubernetes**).

## Get started

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** provides a comprehensive view of your environment, enabling you to automate monitoring and optimize the health and performance of your Kubernetes clusters and workloads. This page walks you through the main concepts underlying ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

With ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, you can:

* Set up Kubernetes monitoring with Dynatrace.
* Explore cluster, node, and workload insights.
* Analyze health status with Dynatrace Intelligence.
* Detect and troubleshoot Kubernetes issues.

![High-level overview of all your Kubernetes clusters, independent of the cloud service they run on.](https://dt-cdn.net/hub/highleveloverview2.png)![Detailed view of a single cluster showing all health-relevant signals of contained resources, including nodes, namespaces, and workloads.â](https://dt-cdn.net/hub/detailedviewofsinglecluster.png)![View the health state of a particular workload and get further details, so you can quickly decide on the next course of action.](https://dt-cdn.net/hub/healthofworkload.png)![Customize your Kubernetes monitoring using ready-made dashboards.](https://dt-cdn.net/hub/inx16596.sprint.apps.dynatracelabs.com_uiFull-HD_1oyEkuF.png)![Onboard new Kubernetes clusters in just five minutes, no matter the cloud service they run on. No docs are required.](https://dt-cdn.net/hub/NewWelcomeScreenK8s_RxlAOrb.png)

1 of 5High-level overview of all your Kubernetes clusters, independent of the cloud service they run on.

### Setup and reference

Use the following guide to set up and configure Kubernetes monitoring in Dynatrace.

[01Enable Kubernetes experience for existing clusters

* How-to guide
* Enable existing clusters for the new Kubernetes experience.](/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience/existing-clusters)

## Explorer

Explorer is the shared Dynatrace interface for monitoring and analyzing different technology domains. It defines a common layout (sidebar, list, filter bar, health indicators, and detail panels) with consistent filtering, perspectives, drillâdown navigation, and unified analysis.

The sections below describe how Explorer appears in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

### Basic structure

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** offers insights into your entire Kubernetes environment, presenting valuable information across primary areas as indicated in the picture below.

![An overview of the Clusters page in the Kubernetes app.](https://dt-cdn.net/images/k8s-clusters-page-overview-1920-faadf96144.png)

* **Sidebar (1)**

  Located on the left side, the sidebar groups all [Kubernetes objectsï»¿](https://dt-url.net/q0038e6) by type, including clusters, nodes, namespaces, workloads, pods, services, and containers.
* **Object list (2)**

### Perspectives

* **Aggregated health bar (3)**

  Located above the object list, this bar provides an aggregated [health status](#health-status) of the displayed objects and their child objects.
* **Filter bar (4)**

### Davis AI health status

### Detail view

Select a Kubernetes object from the list to open a detail view and focus on the specific object.

![An example of the cluster health details page in the Kubernetes app.](https://dt-cdn.net/images/k8s-cluster-health-details-example-1920-4a19911c0d.png)

* **Top summary section (1)**

  The top pane provides a quick summary of the health and security status of the selected object and its child objects.
* **Main detail section (2)**

  The main section provides detailed insights of the given object, featuring tabs for analyzing health and utilization, as well as for exploring logs, events, ownership, and vulnerabilities. The data presented in the detailed view remains consistent regardless of any filters applied in the main interface.

### Perspectives

Perspectives are located under the aggregated health bar. They support various use cases, such as health monitoring or resource optimization.

![An example of the clusters page in the Kubernetes app.](https://dt-cdn.net/images/k8s-clusters-health-example-1920-463f1b6358.png)

* **Selecting a perspective (1)**

  Choosing a perspective changes which columns are displayed in the table. For example:

  + **Health**âshows health-related information and alerts.
  + **Utilization**âfocuses on CPU, memory, and other resource usage metrics.
* **Customizing columns (2)**

  You can add or remove columns within a selected perspective to match your analysis needs. Your personal configuration persists in your browser, and you can reset to the default layout at any time by selecting ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") next to the list of available perspectives (1).

### Dynatrace Intelligence health status

The health status is based on the Kubernetes-focused custom alerts. Health indicators aggregate the states of these custom alerts per resource.

A Kubernetes object (such as a cluster) is considered unhealthy if any of its associated custom alert configurations are in an unhealthy state. By selecting a specific health indicator, you can gain further insights into the underlying reasons for this status.

![Example of Dynatrace Intelligence health status for a Kubernetes cluster.](https://dt-cdn.net/images/k8s-dynatrace-intelligence-cluster-health-status-1920-4200846da4.png)

Example

In this example, you can see that 8 nodes out of 24 are currently considered unhealthy.

1. Select the red numbers displayed within the health status area to drill down to the list of currently unhealthy nodes.

   ![An example of a Dynatrace Intelligence warning signal in the Kubernetes app.](https://dt-cdn.net/images/k8s-dynatrace-intelligence-warning-signals-1393-cb95af4862.png)
2. Select any node to open the details view of the problematic node, including key metrics and events that led to their current state.

   ![Warning events 2](https://dt-cdn.net/images/warning-events-2-1914-c65669ad3d.png)

   The **Recommendations** tab presents best-practice Kubernetes health alerts for clusters, nodes, namespaces, persistent volume claims, and workloads. It highlights which alerts are active, partially active, or inactive across your environment.

   Select **Activate** or **Configure** to open the settings where you can apply the recommended alert configuration.

   ![Recommendations](https://dt-cdn.net/images/recommendations-1909-f9f2da2e1a.png)

### Health alerts and warning signals

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

While they may not always represent active health issues at the moment, frequent **Unhealthy** signals, for instance, might indicate misconfigured readiness probes, inappropriate CPU limits, or unusually high workload.

Sorting and filtering of warning signals

There are two types of warning signals. They're organized as follows:

* Problematic conditions affect the health of the node or workload (for example, `DiskPressure`, `MemoryPressure`).

  + Listed first
  + Sorted alphabetically within each category
* Warning events are less critical, and often signal temporary issues (for example, `OOMKilled`, `PodEviction`).

  + Listed after problematic conditions
  + Sorted by their frequency

![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** provides several interaction options:

* Context menu actions:

  + **Go to affected nodes** or **Go to affected workloads**: Navigates directly to the nodes or workloads experiencing the selected condition. This opens a filtered view displaying only the affected nodes or workloads.
  + **Explore events**: Opens a detailed log view showing the events associated with the warning signal.
  + **Filter for**: Automatically applies a filter to show only the entities impacted by the specific condition or event.
* Filtering from the menu bar:
  You can apply filters directly from the menu bar by selecting either general categories such as **Any problematic condition** or individual signals like `MemoryPressure:True` or `FailedMount`. Once filtered, the view updates to focus on the entities affected by the selected filter.

![Dynatrace Intelligence warning signals for Nodes in the Kubernetes app.](https://dt-cdn.net/images/k8s-nodes-warning-signals-1920-47b6aa9589.png)

| Column | Content | Examples |
| --- | --- | --- |
| Node warning signals | [Combines events emitted by nodes and problematic node conditions](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues#node "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") | `DiskPressure`, `MemoryPressure`, `NodeNotReady` |
| Pod warning signals | [Combines events emitted by pods and conditions affecting pods](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues#workload "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") | `BackOff`, `PodEviction`, `OOMKilled` |
| Workload warning signals | [Combines events emitted by namespaces, workloads, and pods, along with workload conditions](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues#workload "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") | `CPUThrottlingHigh`, `ContainerRestarts`, `PodsPending` |

## Kubernetes Enhanced Object Visibility

### Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine
* [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") with the **Kubernetes Platform Monitoring** capability on your Rate Card
* [Sufficient permissions](/docs/observe/infrastructure-observability/kubernetes-app/reference/permissions "Overview of user and tailoring permissions.") to use the ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** within your Dynatrace environment
* ActiveGate version 1.327+

Starting January 19, 2026, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** offers insights into more Kubernetes objects and their YAML definitions:

* Visibility into additional Kubernetes objects: Ingress, NetworkPolicies, CRDs, PVCs, PVs, ConfigMaps, and more.
* Access to YAML definitions to debug and validate configurations in real time.
* Ability to query YAMLs across all clusters and namespaces using Dynatrace Query Language (DQL) to instantly surface misconfigurations, missing references, or policy violations across your Kubernetes environment.

## Use cases

## Reference

Go to the following reference pages for more information about permissions, available alerts, and default settings for new environments.

## Learn more

Dive deeper into ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** with the following resources:

* [Playground environmentï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.kubernetes): Test the app in a sandbox environment.
* [0 to Full Observability in Kubernetes in under 3 minutesï»¿](https://dt-cdn.net/resources/product/videos/k8s-0-to-full-observability.mp4): A quick video tutorial on how to install Dynatrace Operator.
* [Blog post: Unlock the Power of DevSecOps with Newly Released Kubernetes Experience for Platform Engineeringï»¿](https://www.dynatrace.com/news/blog/kubernetes-platform-engineering/)

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Automated change impact analysis for your deployment and release processes.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=kubernetes&internal_source=doc&internal_medium=link&internal_campaign=cross)


---


## Source: ingest-netflow-records.md


---
title: Ingest NetFlow records into Dynatrace
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks/ingest-netflow-records
scraped: 2026-02-16T09:36:22.194791
---

# Ingest NetFlow records into Dynatrace

# Ingest NetFlow records into Dynatrace

* How-to guide
* 2-min read
* Updated on Jan 19, 2026

Network observability provides the necessary visibility to understand how applications interact with the underlying network. It allows teams to identify and address issues more effectively by starting with device health monitoring and extending to flow data collectionâsuch as NetFlowâto track network usage. This approach actively supports performance optimization, enhances security, and streamlines troubleshooting efforts.

This guide shows you how to ingest NetFlow records into Dynatrace by setting up the collector and using ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to analyze flow data.

## Why monitor network flow with Dynatrace?

Ingesting network flows into Dynatrace immediately puts this data in context. The data contained in the network flows complements supported network use cases by linking flow volume and directions to devices and interfaces. The network flow data can be compared with process-to-process data to help solve network-induced application problems.

## How does Dynatrace as a platform support NetFlow ingestion?

Dynatrace supports network flow protocols such as NetFlow, sFlow, and IPFIX through a fully supported version of the [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector."). A dedicated network flow receiver enables seamless ingestion of flow data into the Dynatrace platform for analysis and visualization.

## Prerequisites

* A [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.") distribution with [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver).
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the **Ingest logs** (`logs.ingest`) and **Ingest metrics** (`metrics.ingest`) scopes. For details, see [OpenTelemetry Collector self-monitoring](/docs/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with Dynatrace dashboards.").

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Steps

In this example, we deploy using Docker to keep the demonstration simple. For production use cases, we recommend deploying as a gateway on a Kubernetes cluster. For details, see [Configure OpenTelemetry Collector for Kubernetes monitoring](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.").

1. To configure a Dynatrace Collector instance, create a file called `otel-collector-config.yaml` and add the following configuration:

   ```
   receivers:



   netflow:



   scheme: netflow



   port: 2055



   sockets: 16



   workers: 32



   netflow/sflow:



   scheme: sflow



   port: 6343



   sockets: 16



   workers: 32



   processors:



   batch:



   send_batch_size: 2000



   timeout: 30s



   exporters:



   otlp_http:



   endpoint: "${env:DT_ENDPOINT}"



   headers:



   Authorization: "Api-Token ${env:DT_API_TOKEN}"



   service:



   pipelines:



   logs:



   receivers: [netflow, netflow/sflow]



   processors: [batch]



   exporters: [otlp_http]



   telemetry:



   logs:



   level: debug
   ```

   Check the [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver#netflow-receiver) documentation for the available configuration options.
2. Create an `.env` file to add the `DT_ENDPOINT` and `DT_API_TOKEN` variables.

   * `DT_ENDPOINT` is the Dynatrace API server endpoint. It contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). For example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`. For more details, see [Integrate OneAgent on Azure App Service for Linux and containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.").
   * `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

   Ensure your `.env` file is properly secured and not exposed to unauthorized access, as it contains sensitive information.
3. Create an access token by going to **Access Tokens** > **Generate new token** and selecting **Ingest logs** as a scope.
4. Run the Collector image in Docker using the following command:

   ```
   docker run -p 2055:2055 --env-file ./.dt_token.env -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.33.0 --config=/etc/otelcol/otel-collector-config.yaml
   ```

   Once the process is completed, you can start running and processing data.

   If you want the process to run in the background, you can kill it and run again with the `-d` option.
5. Direct your network devices to send NetFlow records to the Collector.

   The network device configuration is vendor-specific. It must indicate the Dynatrace endpoint's IP address and the matching UDP port.

## Data visualization and analysis

### Log analysis

NetFlow data is ingested as log records, which can be queried and visualized using DQL. You can use [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**ï»¿](https://www.dynatrace.com/hub/detail/logs/) to look for container logs captured by OneAgent for the Collector:

![OpenTelemetry errors displayed in the Logs app](https://dt-cdn.net/images/open-telemetry-errors-2163-955bbf8cf3.png)

Similarly, ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** can help you see that traffic is indeed flowing:

![Traffic flow with NetFlow in the Logs app](https://dt-cdn.net/images/logs-netflow-trafic-flow-2022-d387c3206a.png)

### Dashboards

![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** provides a ready-made **NetFlow Overview** dashboard as an entry point to explore and visualize NetFlow data. It includes pre-configured charts and metrics to analyze network traffic, such as top sources, destinations, conversations, and port usage.

![Dashboards NetFlow Overview](https://dt-cdn.net/images/dashboards-netflow-overview-1619-1e3c5ca7d8.png)

The dashboard can be used as a base for further customizations. You can also create custom dashboards to visualize NetFlow data using various chart types.

### Notebooks

![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** allows you to run queries and visualize NetFlow data interactively. You can open a new notebook from ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** by going to **Open with** and selecting ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

DQL query example

Using this DQL query, you can get a summary of the bytes by destination IP and port:

```
fetch logs



| filter matchesValue(flow.type, "netflow_v9")



| summarize {totalBytes= sum(toLong(flow.io.bytes)),totalPackets=sum(toLong(flow.io.packets))}, by: {destination.address,destination.port}



| sort totalBytes desc



| limit 10
```

![Summary of bytes by destination IP and port in Notebooks](https://dt-cdn.net/images/notebooks-netflow-bytes-by-dest-id-and-port-1310-aa7ceb24fe.png)

## Related topics

* [Ingest NetFlow with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")


---


## Source: network-monitoring-with-nettracer.md


---
title: Extended network monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks/network-monitoring-with-nettracer
scraped: 2026-02-17T21:23:53.599896
---

# Extended network monitoring

# Extended network monitoring

* How-to guide
* 5-min read
* Updated on Oct 03, 2025

Extend network monitoring with network traffic metrics in containerized Linux hosts.

With network metrics added to your containerized hosts, DavisÂ® root cause analysis will leverage them and extend analysis to provide visibility into network-related issues. Extensive network traffic on particular nodes is a sign that you should consider scaling up the cluster.

## NetTracer

NetTracer is an open source tool for tracing TCP events and collecting network connection metrics on Linux. It consists of two parts:

* BPF program used for collecting data
* Binary that presents the data in a structured or semi-structured format

Advantages:

* It can trace TCP events: **connect**, **accept**, and **close**
* It can collect metrics about each traced connection
* It's a high performance applicaton (written in C and C++)
* It's independent from kernel version and configuration (Linux kernel 4.15 and higher)
* It's an open source project ([NetTracerï»¿](https://github.com/dynatrace-oss/nettracer-bpf))

NetTracer defines an IPv4 and IPv6 TCP connection by source address and port, destination address and port, PID of the communicating process, and network namespace.

Using this TCP connection definition, it collects the following metrics:

* Bytes sent
* Bytes received
* Packets sent
* Packets received
* Packets retransmitted
* Round-Trip Time (in microseconds)
* Round-Trip Time variance (not used in Dynatrace analysis)

By default, NetTracer is included as the binary `oneagentnettracer` with every OneAgent installation, and it can be enabled via the Dynatrace web UI.

## NetTracer supported platforms

NetTracer officially supports Linux kernel versions 4.15 and higher, but other Dynatrace components that coexist with NetTracer on a particular host have specific requirements and are supported on particular Linux distributions. The following table lists the tested and safest Linux distributions to use when planning to use NetTracer with Dynatrace.

Distribution

Architecture

Release

RedHat Enterprise Linux

x86\_64

8.0 and higher

CentOS

x86\_64

8.0 and higher

Ubuntu

x86\_64

18.04 LTS and higher

## Enable NetTracer

When enabled, OneAgent will use NetTracer to collect network data from containers, but only for Linux hosts.

To enable NetTracer on a specific Linux host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your Linux host.
2. On the host overview page, select **More** (**â¦**) > **Settings** in the upper-right corner of the page.
3. On the **Host settings** page, select **NetTracer traffic** and turn on **Enable NetTracer traffic network monitoring**.

To enable NetTracer globally on all your Linux hosts

1. Go to **Settings** > **Network & Discovery** > **NetTracer traffic**.
2. Turn on **Enable NetTracer traffic network monitoring**.

To ensure NetTracer works correctly, OneAgent must be installed in either Full-Stack or Infrastructure monitoring mode, as these modes enable the network monitoring feature. If OneAgent is installed in a limited mode (for example, Discovery monitoring mode), NetTracer may not function as intended. For more details, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

## Built-in metrics for NetTracer

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.nettracer.bytes\_rx | Bytes received Number of bytes received | Byte | autoavgcountmaxminsum |
| builtin:tech.nettracer.bytes\_tx | Bytes transmitted Number of bytes transmitted | Byte | autoavgcountmaxminsum |
| builtin:tech.nettracer.pkts\_retr | Retransmitted packets Number of retransmitted packets | Count | autovalue |
| builtin:tech.nettracer.pkts\_rx | Packets received Number of packets received | Count | autovalue |
| builtin:tech.nettracer.pkts\_tx | Packets transmitted Number of packets transmitted | Count | autovalue |
| builtin:tech.nettracer.retr\_percentage | Retransmission Percentage of retransmitted packets | Percent (%) | autoavgmaxmin |
| builtin:tech.nettracer.rtt | Round trip time Round trip time in milliseconds. Aggregates data from active sessions | Millisecond | autoavgcountmaxminsum |
| builtin:tech.nettracer.traffic | Network traffic Summary of incoming and outgoing network traffic in bits per second | bit/s | autovalue |
| builtin:tech.nettracer.traffic\_rx | Incoming traffic Incoming network traffic in bits per second | bit/s | autovalue |
| builtin:tech.nettracer.traffic\_tx | Outgoing traffic Outgoing network traffic in bits per second | bit/s | autovalue |

### Calculated metrics for NetTracer

The following metrics available for NetTracer are calculated:

* `builtin:tech.nettracer.retr_percentage` (Retransmission)

  Retransmission = retransmitted packets / (retransmitted packets + packets transmitted) Ã 100
* `builtin:tech.nettracer.traffic_rx` (Incoming traffic)

  Incoming traffic = (sum of bytes received \* 8) per second
* `builtin:tech.nettracer.traffic_tx` (Outgoing traffic)

  Outgoing traffic = (sum of bytes transmitted:sum \* 8) per second
* `builtin:tech.nettracer.traffic` (Network traffic)

  Network traffic = ((sum of bytes received + sum of bytes transmitted) \* 8) per second

## Dimensions for NetTracer

Metric key

Dimension

Value

Unit

`builtin:tech.nettracer.bytes_rx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Gauge, where:

sum = number of bytes from all sessions in the given timeframe

avg/min/max = average/minimal/maximal bytes per session in the given timeframe

count = number of sessions in the given timeframe

Bytes

`builtin:tech.nettracer.bytes_tx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Gauge, where:

sum = number of bytes from all sessions in the given timeframe

avg/min/max = average/minimal/maximal bytes per session in the given timeframe

count = number of sessions in the given timeframe

Bytes

`builtin:tech.nettracer.pkts_rx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Count, sending deltas/resetting counter

Count

`builtin:tech.nettracer.pkts_tx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Count, sending deltas/resetting counter

Count

`builtin:tech.nettracer.pkts_retr`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Count, sending deltas/resetting counter

Count

`builtin:tech.nettracer.rtt`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Gauge

Miliseconds

### Container dimensions for NetTracer

If the process is running in a container, the following dimensions are added:

* `dt.entity.container_group_instance`
* `dt.entity.container_group`

Additional container dimensions are added depending on the deployment type.

Kubernetes

Docker (no Kubernetes)

`container.image.name` (if it's available)  
`k8s.container.name`  
`k8s.namespace.name`  
`k8s.pod.name`  
`k8s.pod.uid`

`container.image.name`  
`container.name`

## Where can I see NetTracer data?

After it's collected, NetTracer data is available as metrics throughout Dynatrace.

* **Data Explorer**: You can use the metrics in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to create charts and dashboards that display data that interests you.
* **Process group instance page**: Go to process group instance page and select **Networking** tab.

  ![Process group instance page - Networking details](https://dt-cdn.net/images/pgi-page-networking-details-2172-bcb6d64191.png)
* **Host overview**: Go to host overview page and scroll down to the **Network analysis** section.

  ![Network analysis](https://dt-cdn.net/images/lde68092-dev-apps-dynatracelabs-com-ui-apps-dynatrace-classic-hosts-ui-entity-host-b8ec70b7dc022ec8-gtf-2h-gf-all-sessionid-4aquod8c7d1hqbf8-2-2913-bca5600276.png)

**Networking** and **Network analysis** sections contain NetTracer data combined with other network data analysed for this host. NetTracer gathers data for containerized processes, meanwhile Network Agent for native (i.e., non-containerized) processes.

## NetTracer characteristics

* Only 4096 TCP connections are tracked from the NetTracer `ebpf` module.
* Information about listen ports requires an active TCP connection.


---


## Source: troubleshoot-network-monitoring.md


---
title: Troubleshooting network monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring
scraped: 2026-02-17T21:33:11.269992
---

# Troubleshooting network monitoring

# Troubleshooting network monitoring

* Troubleshooting
* 1-min read
* Published May 06, 2022

Some messages you get during network monitoring might require actions from your side while some are just informational and do not need any reaction.

* [Network monitoring: Potential network disruption during OneAgent installation on Windowsï»¿](https://dt-url.net/hw038ii)
* [Network monitoring: OneAgent page allocation failure message on Linuxï»¿](https://dt-url.net/84238ov)
* [Network monitoring: Network Agent initialization failure on Windowsï»¿](https://dt-url.net/7c438ee)
* [Network monitoring: Why OneAgent's retransmissions metric can diverge when comparing to other toolsï»¿](https://dt-url.net/0203wlh)


---


## Source: networks.md


---
title: Networks
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks
scraped: 2026-02-06T16:29:04.150090
---

# Networks

# Networks

* Overview
* 2-min read
* Updated on Apr 19, 2022

Dynatrace infrastructure monitoring extends beyond hosts and processes to include network communication. It provides insight into how well processes communicate, access required resources, and use network bandwidth. This helps you detect issues that aren't caused by resource limits or slow response times, but by poor connectivity or misused network capacity. By monitoring data packets exchanged between processes and hosts, you gain deeper visibility into performance and reliability across your environment.

## Network monitoring overhead

Network monitoring in Dynatrace introduces minimal overhead, which varies depending on traffic volume. Dynatrace automatically tracks this overhead and applies throttling if it exceeds 5% of available CPU. When throttling is triggered, the network module pauses for just under 3 minutes. If the threshold is still exceeded after reactivation, the pause duration doubles each time, up to a maximum of 45 minutes, until resource usage returns to acceptable levels.

## Data privacy

* Dynatrace analyzes the network packets in memory in real time.
* Dynatrace doesn't store the packets on a drive, either on monitored hosts or in the Dynatrace cluster.
* Dynatrace analyzes packet headers only, not the payload.

[#### Monitor network communications

Learn the basics of Dynatrace network monitoring, including how to analyze network health and recognize common network issues.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/how-to-monitor-network-communication)[#### Detect network errors

Learn how errors such as dropped packets and retransmissions on the network level can affect the performance and connectivity of your services.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/detect-network-errors)[#### Extended network monitoring

Extend network monitoring with network traffic metrics in containerized Linux hosts using NetTracer.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/network-monitoring-with-nettracer)[#### Troubleshooting network monitoring

Learn more about troubleshooting network monitoring.

* Troubleshooting

Read this troubleshooting guide](/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring)[#### Ingest NetFlow records into Dynatrace

Learn how to ingest NetFlow records into Dynatrace.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/ingest-netflow-records)

## Related topics

* [Network monitoringï»¿](https://www.dynatrace.com/platform/network-monitoring/)


---


## Source: which-are-the-most-important-processes.md


---
title: Which are the most important processes?
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes
scraped: 2026-02-17T21:16:00.877174
---

# Which are the most important processes?

# Which are the most important processes?

* How-to guide
* 2-min read
* Updated on Jan 16, 2025

To view the most important processes running on a specific host, go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select a host to go to the host overview page. Locate the **Process analysis** section, where you'll find charts and lists of the processes running on the selected host.

Within the **Process analysis** section, you can also see various process group instances categorized by technology type.

For more details, refer to [Process analysis](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#process-analysis "Monitor hosts with Dynatrace.").

For processes to be visible in this section, they have to meet at least one of the following criteria:

* Processes that are [supported applications](/docs/ingest-from/technology-support#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Processes with an open TCP listening port
* Processes for which one of the following conditions is met for at least 3 of the last 5 one-minute intervals:

  + **Avg(CPU) > 5%**
  + **Max(Memory) > 5%**
  + **Network Traffic > 5%**.
* Processes that have been defined by a user as important, for example, by enabling Log Monitoring for a process.

Dynatrace provides also the option of [monitoring specific processes that fall into neither of these categories](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

Any processes that do not meet the above criteria, and therefore are not considered important processes, are aggregated and labeled as **Other processes**.

## Process group details

The process list provides basic information about system and network resources that are consumed by the process.

| Resource | Description |
| --- | --- |
| CPU usage | CPU percentage consumed by the process. |
| Memory usage | System memory percentage consumed by the process. |
| Traffic | Network traffic to and from the process. |
| Retransmissions | Retransmitted (either direction). |
| Connectivity | Connectivity is a percentage of successfully established TCP sessions minus the sum of TCP connection refused (as percentage) and TCP connection timeouts (as percentage). |

## Why does Dynatrace not show worker processes?

If you run Apache HTTP Server, for example, you may be accustomed to seeing long lists of worker processes (see example below). Here you see numerous Apache HTTP Server processes listed on a Linux terminal. For the sake of clarity and manageability however, Dynatrace consolidates such lists into process group instances. We do this across hosts but also on individual hosts.

![Processgroup apache2](https://dt-cdn.net/images/processgroup-apache2-460-e9af3aa576.png)


---


## Source: pg-detection.md


---
title: Process group detection
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection
scraped: 2026-02-17T21:19:16.824862
---

# Process group detection

# Process group detection

* How-to guide
* 10-min read
* Updated on Aug 07, 2023

Dynatrace detects which processes are part of the same [process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") by means of a default set of detection rules.

You can change the structure of default process groups by modifying the default process-group detection logic in:

* **Settings** > **Processes and containers** > **Process group detection** section, which has the following pages:

  + On the **Built-in detection rules** page, you can enable or disable specific process group detection toggles. Hover over the **info** icon to the right of each toggle for details.
  + On the [**Simple detection rules**](#simple) and [**Advanced detection rules**](#advanced) pages, you can add your own process group detection rules, which will override the default ones.
  + On the [Declarative process grouping](/docs/observe/infrastructure-observability/process-groups/configuration/declarative-process-grouping "Monitor specific processes using the declarative process grouping.") page, you can monitor specific processes of a technology that is unknown to Dynatrace.
* **Settings** > **Processes and containers** > **Containers** > **Cloud application and workload detection**, where you can define rules to merge similar Kubernetes workloads into process groups.

* Process group detection settings and rules require a restart of your processes to affect how processes are identified and grouped.
* Process group detection settings and rules only affect the composition of process groups. If you want to change how a process group is named, you have to use the [process group naming rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming") instead.
* It's also possible to use [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to separate clusters into different process groups.

## Simple detection rules

Simple process group detection rules enable you to adapt the default process-group detection logic for deep monitored processes via [**Java system properties**](#java) or [**environment variables**](#env). You can create a simple detection rule using the Dynatrace web UI or the [Settings API](#api) - see [Example JSON payload for a simple detection rule](#eg1).

Simple process-group detection rules are only effective when OneAgent is installed on your hosts or images for processes that can be deep monitored.

This feature can only split a process group into multiple parts. Use it if you have different deployments into the same process group.

To create a simple detection rule in the Dynatrace web UI

1. Go to **Settings**.
2. Select **Processes and containers** > **Simple detection rules**.
3. Select **Add item**.
4. Set **Property source** to **Java system property** or **Environment variable**.
5. Set **Group identifier** to a value that Dynatrace will use to identify process groups.
6. Optional Set **Instance identifier** to a value that Dynatrace will use to identify specific cluster nodes within a process group.

   This setting is useful if your process group setup has specific names per node. If you're not sure, leave the field empty. The default setting is one node per host.
7. Optional Set **Restrict this rule to specific process types** to the type of process to which you want to apply the rule.
8. Select **Save changes**.

### Java system properties

With this option, you can create more fine-grained groups of Java processes.
The Java system property needs to be part of the Java command line to be detected by OneAgent. It can either be an existing system property that your application already uses (for example, three different `jetty.home` values for three different Solr clusters), or you can add a new system property. As long as the system property is available on the command line, Dynatrace can use it.

### Environment variables

This option covers both Java and non-Java processes like NGINX, Apache HTTPserver, FPM/PHP, Node.js, IIS, and .NET.
The environment variables that you select as process group identifiers must exist within the scope of the detected processes and be visible at application startup.

* For WebSphere, you can do this in the WebSphere console in the JVM section.
* For Tomcat and others, simply define the environment variable as part of the startup script.

We recommend creating environment variables specific to process detection. Environment variables that serve other scopes, such as [`DT_TAGS`](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables#variables "Find out how Dynatrace enables you to define tags based on environment variables.") or [`DT_CUSTOM_PROP`](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment."), might cause incorrect or unintentional splits because all values of environment variables are evaluated for process-group detection.

Identifiers also serve as the default name for the detected process groups. See [Define your own process group metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") for details on how to define an environment variable for IIS or for Windows services.

**Example:**

Suppose you have two nearly identical Apache HTTP server deployments that reside within the same deployment directory but on different hosts. By default, Dynatrace can't distinguish between the two deployments because they don't have any unique characteristics that can be used for identification. Now consider the following rule: `Apache process identified by environment variable MY_PG_NAME`.

Any Apache HTTP process that includes the environment variable `MY_PG_NAME` within its scope will use the content of "MY\_PG\_NAME" as both its identifier and its default name. In this scenario, you can have Dynatrace separately identify and name each deployment by assigning the environment variable `MY_PG_NAME=dynatrace.com-production` to one deployment, and `MY_PG_NAME=dynatrace.com-staging` to the other deployment.

## Advanced detection rules

Advanced process group detection rules allow you to create a process group by merging processes from different groups, and enable you to adapt the detection logic for deep monitored processes by leveraging properties that are automatically detected by OneAgent during the startup of a process. You can create an advanced detection rule using the Dynatrace web UI or the [Settings API](#api) - see [Example JSON payload for an advanced detection rule](#eg2).

Advanced process-group detection rules are only effective when OneAgent is installed on your hosts or images for processes that can be deep monitored.

To create an advanced detection rule in the Dynatrace web UI

1. Go to **Settings**.
2. Select **Processes and containers** > **Advanced detection rules**.
3. Select **Add item**.
4. In the **Process group detection** section, define to which processes this rule should be applied. For example, to a Java JAR file that contains `ws-server.jar`.
5. In the **Process group extraction** section, select which property value should be used within the process group detection.
6. Select whether you want the rule to be a **standalone rule**.

   This option is not recommended in containerized environments, as out-of-the-box detection should take care of everything. For details, see [Standalone rules](#stand).
7. In the **Process instance extraction** section, select if specific properties should be used to extract single process instances (nodes).
8. Select **Save changes**.

### Standalone rules

#### When to enable this option

Suppose you have a process group with multiple processes. Each process simultaneously performs the same function for different customers who are using your application at the same time. While each process instance has the same name, each instance runs off a unique customer-specific configuration about which Dynatrace doesnât have any information. Dynatrace therefore aggregates all related processes into a single process group in order to facilitate monitoring.

For cases where such grouping is inadequate, you have the option to define process-group detection rules that take into account customer-specific details. Such details can be drawn from your unique deployment scheme. If you have a directory structure that includes a customer ID (for example, `/opt/MyCustomerBasedApp/<CustomerId>/Service/MyService`), and the directory structure is the same across all your hosts, you can create a customer-specific process-group detection rule that works across all process instances.

**Example:**

You can create a rule that applies to processes with executable paths containing the phrase `MyCustomerBasedApp`. For processes that match this requirement, the string between `/MyCustomerBasedApp/` and `/Service` in the **Executable path** is extracted and used to uniquely identify each process instance.

![pg-standalone](https://dt-cdn.net/images/image-2-1284-3249e27cb7.png)

#### When to disable this option

You can disable the **Standalone rules** option when, within the same environment, you want to differentiate between separate entities (for example, production vs. testing). In this case, you may want to use the default detection by Dynatrace, but enhance it with your own knowledge of the deployment setup.

You have the option to define a second property that identifies specific process instances (or cluster nodes) within a process group. This is useful if your process group setup has specific names per instance. If you're not sure, leave the field empty. The default setting is one node per host.

**Example:**

![pg-no-standalone](https://dt-cdn.net/images/image-1-1194-857811a02c.png)

* If none of the above process group detection options works, you can use the environment variable **DT\_CLUSTER\_ID** to group all processes that have the same value for this variable. All processes found in a monitoring environment that share the same cluster ID are treated as members of the same process group, and are separated only by the hosts they run on (for example, clusters of Apache web servers that belong together and host the same site). Make sure you set the **DT\_CLUSTER\_ID** variable only on a process-by-process basis, not system wide! If you set this variable system-wide, all processes may be grouped into a single process group for monitoring. This is undesirable and unsupported.
* To identify nodes within a process cluster that run on the same host, use the **DT\_NODE\_ID** environment variable. This tells Dynatrace which processes should be taken as separate process group instances.

## Declarative process grouping

Dynatrace automatically monitors process groups that are of known technology types or that consume significant resources. With declarative process grouping, you can automatically monitor additional technologies by overriding the default behavior and customizing the grouping of processes into process groups (PGs) and process group instances (PGIs). For more details, refer to [Declarative process grouping](/docs/observe/infrastructure-observability/process-groups/configuration/declarative-process-grouping "Monitor specific processes using the declarative process grouping.").

## Easy configuration with Settings API

Using the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), you can easily

* Change the definition of your process groups
* Set up a simple or an advanced detection rule
* Configure a declarative process group detection

To use the Settings API

1. [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and enable the **Write settings** (`settings.write`) permission.
2. Use the [Get a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration.

   Example JSON payload for a simple detection rule

   * SchemaID: `builtin:process-group.simple-detection-rule`

     ```
     [



     {



     "schemaId": "builtin:process-group.simple-detection-rule"



     "scope": "environment"



     "value": {



     "enabled": true,



     "ruleType": "env",



     "groupIdentifier": "MY_PG_NAME",



     "instanceIdentifier": "MY_INSTANCE_NAME",



     "processType": "PROCESS_TYPE_APACHE_HTTPD"



     }



     }



     ]
     ```

   Example JSON payload for an advanced detection rule

   * SchemaID: `builtin:process-group.advanced-detection-rule`

     ```
     [



     {



     "schemaId": "builtin:process-group.advanced-detection-rule"



     "scope": "environment"



     "value": {



     "enabled": true,



     "processDetection": {



     "property": "JBOSS_SERVER_NAME",



     "containedString": "MyJBossServer",



     "restrictToProcessType": "PROCESS_TYPE_JBOSS"



     },



     "groupExtraction": {



     "property": "COMMAND_LINE_ARGS",



     "delimiter": {



     "from": "-environment=",



     "to": "-",



     "removeIds": true



     },



     "standaloneRule": false



     },



     "instanceExtraction": {}



     }



     }



     ]
     ```

   Example JSON payload for a declarative process group configuration

   * SchemaID: `builtin:declarativegrouping`

     ```
     [



     {



     "schemaId": "builtin:declarativegrouping"



     "scope": "environment"



     "value": {



     "name": "keepalived",



     "detection": [



     {



     "id": "keepalived",



     "processGroupName": "keepalived",



     "rules": [



     {



     "property": "executable",



     "condition": "$eq(keepalived)"



     },



     {



     "property": "executablePath",



     "condition": "$prefix(/usr/sbin/keepalived)"



     },



     {



     "property": "commandLine",



     "condition": "$eq(-d)"



     }



     ]



     }



     ]



     }



     }



     ]
     ```
3. Use the [Post an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

## Add your configuration to Extensions 2.0

You can also attach your current configuration to your [Extensions 2.0](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") extension so that your custom extension comes with predefined process grouping rules. Add your definition to the [Extension YAML](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.") file as in this example:

```
---



name: custom:my-extension



version: 1.0.0



minDynatraceVersion: "1.218"



author:



name: Joe Doe



processes:



- name: keepalived



detection:



- id: ext.keepalived



processGroupName: keepalived



rules:



- property: executable



condition: "$eq(keepalived)"



- property: executablePath



condition: "$prefix(/usr/sbin/keepalived)"



- property: commandLine



condition: "$eq(-d)"
```


---


## Source: pg-monitoring.md


---
title: Process deep monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring
scraped: 2026-02-17T21:23:42.359536
---

# Process deep monitoring

# Process deep monitoring

* How-to guide
* 6-min read
* Updated on Aug 07, 2023

Installing OneAgent provides you with process group monitoring capabilities such as:

* Automatic monitoring of all process groups that are detected in your environment after you restart all processes that have been running during the OneAgent installation.
* End-to-end visibility into requests of all auto-detected server-side services, including database services.
* A fully automated monitoring process with no configuration required, thus simplifying monitoring of large-scale environments with hundreds of hosts and thousands of processes, where manual monitoring configuration of all entities isn't feasible.

Optionally, you can set up monitoring rules to selectively specify which processes Dynatrace monitors. For example, consider the following common scenarios:

* You have a number of unimportant or short-lived processes that you donât want to monitor at the code level.
* You aren't able to run deep monitoring on applications that belong to your customers and are out of your control.
* You want to have better control over which processes are monitored.
* You want to perform deep monitoring on .NET and Go processes (Dynatrace doesn't automatically perform deep monitoring on them, as there are many arbitrary processes that rely on these processes). For instance you want to monitor all ASP.NET applications and all Go and .NET core applications running on Cloud Foundry or Kubernetes.

You can set up monitoring states in **Settings** > **Processes and containers** > **Process group monitoring**.

## Enable automatic deep monitoring

* By default, automatic deep monitoring is set to **On** to enable Dynatrace OneAgent to run deep monitoring on all detected processes (unless you specify exceptions for specific processes or create rules that define exceptions). Disable this setting only if your company policies require it.
* Set to **Off** if you want Dynatrace OneAgent to run deep monitoring only for processes that are specified explicitly or that are covered by a deep monitoring rule. You can then manually enable monitoring at the process level or process group level, or choose to define rules about what you want to monitor.

To disable automatic deep monitoring

1. Go to **Settings**.
2. Select **Processes and containers** > **Process group monitoring**.
3. Turn off **Enable automatic deep monitoring**.
4. Select **Save changes**.

How process monitoring rules are applied

**Enable automatic deep monitoring** doesnât take precedence over any [individual process monitoring rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") you may have set up. If a process monitoring rule indicates that Dynatrace should monitor a certain process, and **Enable automatic deep monitoring** is **Off**, the individual rule will take precedence and Dynatrace will monitor the respective process. Therefore, **each process monitoring rule is an exception to the general monitoring policy**.

## Define custom process monitoring rules

Custom process monitoring rules give you fine-grained control over which processes OneAgent monitors with an approach that scales easily within large environments. You donât need to adjust your system configuration, and a few rules can cover thousands of processes.

To add a custom monitoring rule

1. Go to **Settings**.
2. Select **Processes and containers** > **Custom process monitoring rules**.
3. Select **Add item**.
4. Set the **Mode** to determine the basic condition:

   * **Monitor** the process if the condition is met
   * **Do not monitor** the process if the condition is met
5. Define the **Condition**:

   * The condition target (see [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection")).
   * The condition operator (for example, `contains`).
   * The condition value.
6. Select **Save changes** to save your configuration and add the new rule to your list of custom process monitoring rules.

For example, you can create a rule that OneAgent shouldn't be injected into any process in Cloud Foundry spaces that contain the string `customer`.

![Custom monitoring rules](https://dt-cdn.net/images/2021-11-03-10-52-56-1875-b5cf45ace8.png)

To edit an existing rule

1. Select the rule you want to configure.
2. Select **Details** to edit the rule.
3. Select **Save changes**.

To delete a rule

1. Select the rule you want to delete.
2. Select **Delete**.
3. Select **Save changes**.

## Enable or disable built-in process monitoring rules

Built-in rules apply to processes that Dynatrace monitors by default:

* All .NET and Go Kubernetes applications
* All .NET and Go Cloud Foundry applications
* All .NET and Go applications deployed in Docker containers
* ASP.NET Core applications started by IIS
* Core components of Cloud Foundry written in Go
* Caddyâa web server written in Go
* InfluxDBâa timeseries database written in Go

To list all built-in rules

1. Go to **Settings**.
2. Select **Processes and containers** > **Built-in process monitoring rules**.

All built-in rules are enabled by default. You can disable them, but you can't edit the rules.

These built-in rules don't cover your own .NET and Go applications unless those applications are deployed in containers, Cloud Foundry, or Kubernetes. If this is not the case for your .NET and Go applications, you should add your own .NET and Go applications as [custom monitoring rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

Dynatrace doesnât automatically carry out deep monitoring of **all** .NET and Go processes. Many popular applications such as Microsoft Office make use of .NET, and many common infrastructure components are written in Go, so Dynatrace performs deep monitoring of .NET and Go processes only if you explicitly enable it or if they are covered by monitoring rules.

## Set monitoring states at the host-group level

You can set the process group monitoring states at the host-group level.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, expand **Process monitoring** and then select one of the options available to configure monitoring rules.

The process group settings on host groups override the environment-wide process group settings.

## Set monitoring states at the host level

You can add a process group and define its monitoring states at the host level.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Process group monitoring**.
5. Select **Add process group** and choose a process group from the dropdown list.
6. Set the **Monitoring state** (`Monitor`, `Do not monitor`, or `Default`).

   Monitoring state option

   Description

   **Monitor**

   Process group settings at the host level override the corresponding settings at the host group and environment levels.

   **Do not monitor**

   Process group settings at the host level override the corresponding settings at the host group and environment levels.

   **Default**

   Monitoring state is inherited from the previous level settings.

## Limitations

* Deep monitoring rules only affect service- and code-level monitoring.
* Deep monitoring rules are only effective when you install OneAgent on your hosts or images.
* Application-only integrations without a full OneAgent installation donât support monitoring rules. However, in such situations, the integrations themselves effectively provide the same level of control over your process monitoring setup.
* Rules may work on earlier versions of OneAgent, but theyâre only supported for OneAgent version 1.151+.

## Enable or disable short-lived process monitoring

Short-lived processes are processes that are not detected by OneAgent in its default 10-second cycle. We are able to partially monitor them and assign them to specific process groups using the information about their parent process.

To turn monitoring of short-lived processes on or off via the OneAgent host monitoring:

1. Go to **Settings** > **Processes and containers** > **Built-in detection rules**.
2. Turn **Monitor short lived processes** on or off.

Additionally, short-lived processes that frequently restart and are injected by OneAgent automatic injection can be overly burdened by the injection overhead. This can lead to potential delays in these processes, with limited data collection benefits due to their short run times.

If short-lived processes that start up frequently are being injected, disable them for deep monitoring to prevent delays caused by our process injection logic.


---


## Source: process-groups.md


---
title: Process groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/process-groups
scraped: 2026-02-17T21:22:00.112773
---

# Process groups

# Process groups

* Explanation
* 3-min read
* Published Jan 08, 2019

Dynatrace automatically merges related processes into process groups. A âprocess groupâ is a logical cluster of processes that belong to the same application or deployment unit and perform the same function across multiple hosts. Process groups are key building blocks of most modern web-based applications.

Show moreâ¦

Dynatrace automatically [detects application types](/docs/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "The technologies and versions behind a process") such as Tomcat, JBoss, Apache HTTP Server, MongoDB, and many others technologies. To create process groups, Dynatrace uses specific process properties. For Tomcat, Dynatrace uses `CATALINA_HOME` and `CATALINA_BASE` to distinguish between different Tomcat clusters. For JBoss, Dynatrace uses `JBOSS_HOME` and the JBoss cluster configuration. For generic Java processes, Dynatrace uses the JAR file or the main class used to start the process. There are also many specialized detection mechanisms. For example, Dynatrace can detect:

* IBM WebSphere clusters and domains
* Oracle WebLogic clusters and domains
* Cassandra clusters
* Tibco BusinessWorks engines
* Kubernetes apps
* OpenShift apps
* Cloud Foundry apps
* Azure Web Apps
* And moreâ¦

On each process overview page you'll find the properties if you expand **Properties and tags**.

### What does this mean for services?

Process groups are the basis for service detection, because each process group is considered to be a logical cluster or single deployment. When Dynatrace detects the "same" service in separate process groups, it treats them as separate services (for example, one process might be used in staging and the other in production).

If you instruct Dynatrace to merge two separate process groups into a single process group, this will result in the services running on those processes to also be merged.

### Customize process groups

To serve your particular needs when monitoring your processes, Dynatrace allows you to:

* [Customize the name of process groups](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming").
* [Adapt the composition of default process groups](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").
* [Create new process groups in cases where the technology of processes isn't recognized by Dynatrace](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

## Basic concepts

[![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies")

### What technologies underlie individual processes?

Technologies and versions behind a process.](/docs/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "The technologies and versions behind a process")[### Which are the most important processes?

Display the most important processes for monitoring and process grouping.](/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.")

## Configuration

[### Cloud application and workload detection

Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.](/docs/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection "Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.")[### Define your own process group metadata

Configure your own process-related metadata based on the unique needs of your organization or environment.](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")[### Process group detection

Customize process-group detection.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection")[### Process deep monitoring

Customize process-group monitoring.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring")[### Process group naming

Customize process-group naming.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming")

## Monitoring

[### Analyze process responsiveness

Leverage responsiveness to assess process performance.](/docs/observe/infrastructure-observability/process-groups/monitoring/analyze-process-responsiveness "Use responsiveness to assess process performance.")[### Analyze processes

Analyze processes, including information on process metrics, vulnerabilities, and availability.](/docs/observe/infrastructure-observability/process-groups/monitoring/analyze-processes "The Dynatrace approach to process monitoring and process grouping")[### Monitor process-specific network connections

Analyze process-specific network connections.](/docs/observe/infrastructure-observability/process-groups/monitoring/monitor-process-specific-network-connections "Analyze process-specific network connections.")[### Overview of all technologies running in your environment

Get a performance summary of all the technologies in your environment.](/docs/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Get a summary of the performance of all the technologies in your environment.")[### Process group availability monitoring and alerting

Enable process-group availability monitoring to get alerts if processes go offline or crash.](/docs/observe/infrastructure-observability/process-groups/monitoring/process-group-availability-monitoring-and-alerting "Enable process-group availability monitoring to get alerts if processes go offline or crash.")


---


## Source: analyze-queues.md


---
title: Analyze queues
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/analyze-queues
scraped: 2026-02-17T21:25:29.877640
---

# Analyze queues

# Analyze queues

* How-to guide
* 5-min read
* Updated on Dec 28, 2022

Use Dynatrace to gain full visibility into producer and consumer services that are connected to queues and topics, and to simplify troubleshooting efforts in asynchronous communication flows.

To analyze queues and topics

1. Go to **Message Queues**.

   The **Queues and topics** table provides an overview of all queues and topics detected as part of distributed traces, including their technology and the corresponding numbers of incoming and outgoing messages.

   ![Message queues table](https://dt-cdn.net/images/queues-table-1857-49308cb749.png)

   By monitoring the incoming and outgoing messages, you can identify unbalanced message processing. Causes of unbalanced message processing include:

   * Producer services sending more messages to the queue than consumer services can process.
   * Some consumer services exhibiting availability issues or response-time degradation.

   To prevent severe problems caused by an unbalanced message processing (for example, a queue overflow), you can scale queues quickly or maintain failover processes.

   Message counts

   The number of incoming and outgoing messages per queue or topic is calculated based on the data provided by monitored producer and consumer services. If a producer or consumer service isn't monitored, the number of messages per queue or per topic reported in Dynatrace might be lower than the actual number of processed messages.
2. Select the **Name** of a queue or topic from the table to access its analytics view with additional details related to anomalies.

   In each analytics view, you'll find information about anomalies detected by DavisÂ® AI. It also displays the message throughput per queue or topic, along with the connected producer and consumer services. Events highlight any availability changes of your message queue, while logs can reveal internal problems.

   ![Analytics view](https://dt-cdn.net/images/ibm-mq-1748-8930daa8a4.png)

   Different service metricsâsuch as response time, failure rate, throughput, and CPU consumptionâallow you to draw detailed conclusions about the root cause of asynchronous service-to-service communication anomalies. You can switch quickly between the available metrics, apply different aggregation functions, or define metric-specific alerts.

   To define an alert for a metric, select **Set alert** from the **More** (**â¦**) menu in the upper-right corner of the chart.

   To view details at the service and code levels, select a specific service from the producer or consumer list.

   Example: Service flow

   This example shows a service flow with a producer service, queue entity, listener service, and consumer service.

   ![Queue service flow](https://dt-cdn.net/images/queues-service-flow-1941-d21a293780.png)

   Example: Distributed trace

   In this example, you see a distributed trace with a producer service, queue entity, listener service, and consumer service.

   ![Queue distributed traces](https://dt-cdn.net/images/queue-distributed-traces-1939-2ca7ac0044.png)

## DavisÂ® AI for queues

Dynatrace version 1.243+ DavisÂ® AI considers queues and topics during its fault domain isolation, and applies its anomaly detection to producer and consumer services.

### Automatic fault domain isolation

While monitoring individual queues or topics with custom alerts works for specific use cases, enterprise environments with hundreds or thousands of different queues and topics must rely on automatic fault domain isolation to quickly determine the root-cause of a problem.

DavisÂ® AI baselines all incoming and outgoing messages and checks all queue-related events of the underlying infrastructure. In case of detected problems, the respective queues or topics are immediately flagged, and a problem card is opened.

![Problem card for queues](https://dt-cdn.net/images/queue-problem-1768-5913af60a4.png)

### Automatic anomaly detection

Decoupled service-to-service communications are challenging to troubleshoot due to their asynchronous behavior, especially during load drops or load spikes. Example causes for unexpected load scenarios include:

* When the producer service can't send messages to a queue, resulting in an **Unexpected low load** on the consumer service.
* When the producer service sends more messages to a queue, resulting in an **Unexpected high load** on the consumer service.

DavisÂ® AI anomaly detection can automatically detect unexpected load scenarios of asynchronous services.

To automatically detect load drops or load spikes

1. Go to **Settings** > **Anomaly detection** > **Services**.
2. Find **[Service load drops](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services#load-drops "Learn how to adapt the sensitivity of problem detection for services.")** and/or **[Service load spikes](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services#load-spikes "Learn how to adapt the sensitivity of problem detection for services.")**, turn on the dedicated switch and specify the observed load threshold.

![Problem for unexpected low load](https://dt-cdn.net/images/producer-issue-1577-b431cc74e8.png)


---


## Source: ibm-mq-tracing.md


---
title: IBM MQ tracing
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing
scraped: 2026-02-16T09:33:37.740595
---

# IBM MQ tracing

# IBM MQ tracing

* How-to guide
* 6-min read
* Updated on Jun 21, 2022

Dynatrace can automatically create a continuous [service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") for IBM MQ when the producer and consumer services use the same queue or topic name. If the producer and consumer services refer to different queue or topic names, IBM MQ configuration might be required to create a continuous service flow.

Without IBM MQ configuration, Dynatrace can still trace all messages, but the service flow will be broken.

Technology

IBM MQ message

IBM MQ configuration required

z/OS Java .NET

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

IBM App Connect EnterpriseIBM Integration Bus

`MQRFH2.usr` folder not present

`MQRFH2.usr` folder present

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

IBM MQ continuous service flow example

![IBM MQ service flow](https://dt-cdn.net/images/ibm-mq-service-flow-1938-06750bfc7d.png)

IBM MQ distributed trace example

![IMB MQ distributed trace](https://dt-cdn.net/images/ibmmq-distributed-traces-3772-59101a2b00.png)

### FAQ

Should I create the MQRFH2 header when it is not present in my IBM MQ messages?

We recommend that you create the `MQRFH2` header for IBM MQ messages. The presence of the `MQRFH2` header in your IBM MQ messages allows Dynatrace to use [identifiers instead of unique keys](/docs/observe/infrastructure-observability/queues/queue-concepts#producer-consumer-service "Basic concepts of message queue monitoring in Dynatrace.") to trace messages across queues and topics of IBM App Connect Enterprise and IBM Integration Bus.

Benefits of creating the `MQRFH2` header for IBM MQ messages include:

* Consistent [Adaptive Traffic Management](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.") across your monitoring environment, lowering the volume on IBM MQ traces.
* An accurate and continuous service flow without the need to configure IBM MQ mapping when the messages are solely processed by IBM App Connect Enterprise and IBM Integration Bus.

How can I create the MQRFH2 header when it is not present in my IBM MQ messages?

When the `MQRFH2` header is present in your messages before an `MQOutput` node is called by IBM App Connect Enterprise or IBM Integration Bus, Dynatrace uses [identifiers instead of unique keys](/docs/observe/infrastructure-observability/queues/queue-concepts#producer-consumer-service "Basic concepts of message queue monitoring in Dynatrace.") to trace IBM MQ messages.

If this isn't the case in your environment, you can create an empty `MQRFH2` header by, for example, executing the following ESQL command by a preceding `Compute` node

```
CREATE LASTCHILD of OutputRoot DOMAIN 'MQRFH2';
```

For Dynatrace, an empty `MQRFH2` header is enough to automatically create the `usr` folder and to add Dynatrace identifiers to it. If a `usr` folder is already present, Dynatrace reuses it.

Specifications

* Dynatrace creates the `usr` folder within the existing `MQRFH2` header, not the `MQRFH2` header itself.
* When creating the `usr` folder, Dynatrace adds it at the beginning of the `MQRFH2` header.
* If the `usr` folder exists, Dynatrace adds its identifiers at the beginning of the `usr` folder.

## Manage IBM MQ configuration

You can manage an IBM MQ configuration automatically by installing an [IBM MQ extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") and activating **Retrieve topology for improved transaction tracing** to retrieve the IBM MQ configuration of your environment and send it to the Settings API. This can also be done manually via the web UI or the Settings API.

### Manual configuration via web UI

To manage the IBM MQ configuration via the Dynatrace web UI, go to **Settings** > **Mainframe** to find the following menu options:

* IBM MQ queue managers
* IBM MQ queue sharing groups
* IBM MQ IMS bridges

### Manual configuration via Settings API

You can manage the IBM MQ configuration via the Dynatrace [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

## Configuration items

The table lists the available IBM MQ configuration items for queues and topics.

Item

Description

Your action

Queue manager

Queue manager with its queues

Define your queue managers, including alias queues, remote queues, and cluster queues within a single configuration item.

z/OS Queue sharing group

Group of queue managers that access the same shared queues

Specify which queue managers and shared queues belong to a queue-sharing group within a single configuration item.

z/OS IMS bridge

The IBM MQ component that allows direct access to the IMS system

Specify which queue managers and queues belong to an IMS bridge within a single configuration item.

Follow the procedures below to create or update a configuration item. Note that the scope of these items is always an environment. Before starting, learn the format of the settings object by querying its schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call.

Create a configuration item

Update an existing configuration item

### New queue manager

The ID of the queue manager schema is `builtin:ibmmq.queue-managers`.

1. Create the JSON object for your settings.

   The `aliasQueues` object can be a local queue owned by this queue manager, a local definition of a remote queue, or a cluster queue visible by this queue manager but owned by another queue manager.

   Example JSON

   ```
   [



   {



   "schemaId": "builtin:ibmmq.queue-managers",



   "scope": "environment",



   "value": {



   "name": "Queue Manager 1",



   "clusters": [



   "Name of the cluster this Queue Manager 1 is part of"



   ],



   "aliasQueues": [



   {



   "aliasQueue": "Alias Queue",



   "baseQueue": "Base queue which the Alias Queue should point to",



   "clusterVisibility": [



   "Name of a cluster this Alias Queue should be visible in (the queue manager must be part of this cluster)"



   ]



   }



   ],



   "remoteQueues": [



   {



   "localQueue": "Local definition of the Remote Queue",



   "remoteQueue": "Remote Queue",



   "remoteQueueManager": "Remote Queue Manager",



   "clusterVisibility": [



   "Name of a cluster this local definition of the Remote Queue should be visible in (the queue manager must be part of this cluster)"



   ]



   }



   ],



   "clusterQueues": [



   {



   "localQueue": "Local Queue",



   "clusterVisibility": [



   "Name of a cluster this Local Queue should be visible in (the queue manager must be part of this cluster)"



   ]



   }



   ]



   }



   }



   ]
   ```
2. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### New queue sharing group

The ID of the queue sharing group schema is `builtin:ibmmq.queue-sharing-group`.

1. Create the JSON object for your settings.

   Example JSON

   ```
   [



   {



   "schemaId": "builtin:ibmmq.queue-sharing-group",



   "scope": "environment",



   "value": {



   "name": "Queue Sharing Group",



   "queueManagers": [



   "Queue Manager 1",



   "Queue Manager 2"



   ],



   "sharedQueues": [



   "Shared Queue 1",



   "Shared Queue 2"



   ]



   }



   }



   ]
   ```
2. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### New IMS bridge

The ID of the IMS bridge schema is `builtin:ibmmq.ims-bridges`.

1. Create the JSON object for your settings.

   Example JSON

   ```
   [



   {



   "schemaId": "builtin:ibmmq.ims-bridges",



   "scope": "environment",



   "value": {



   "name": "IMS Bridge",



   "queueManagers": [



   {



   "name": "Queue Manager",



   "queueManagerQueue": [



   "Queue 1",



   "Queue 2"



   ]



   }



   ]



   }



   }



   ]
   ```
2. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update queue manager

The ID of the queue manager schema is `builtin:ibmmq.queue-managers`.

The `aliasQueues` object can be a local queue owned by this queue manager, a local definition of a remote queue, or a cluster queue visible by this queue manager but owned by another queue manager.

1. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
2. Create the JSON for your update.

   * Use the **updateToken** value from the previous step.
   * Modify the values as needed.

     Example JSON

     ```
     {



     "updateToken": "vu9U3hXY3q0ATAAkMG",



     "value": {



     "name": "Queue Manager A",



     "clusters": [



     "Name of a cluster this Queue Manager A is part of"



     ],



     "aliasQueues": [



     {



     "aliasQueue": "Alias Queue",



     "baseQueue": "Base queue which the Alias Queue should point to",



     "clusterVisibility": [



     "Name of a cluster this Alias Queue should be visible in (the queue manager must be part of this cluster)"



     ]



     }



     ],



     "remoteQueues": [



     {



     "localQueue": "Local definition of the Remote Queue",



     "remoteQueue": "Remote Queue",



     "remoteQueueManager": "Remote Queue Manager",



     "clusterVisibility": [



     "Name of a cluster this local definition of the Remote Queue should be visible in (the queue manager must be part of this cluster)"



     ]



     }



     ],



     "clusterQueues": [



     {



     "localQueue": "Local Queue",



     "clusterVisibility": [



     "Name of a cluster this Local Queue should be visible in (the queue manager must be part of this cluster)"



     ]



     }



     ]



     }



     }
     ```
3. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update sharing group

The ID of the queue sharing group schema is `builtin:ibmmq.queue-sharing-group`.

1. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
2. Create the JSON for your update.

   * Use the **updateToken** value from the previous step.
   * Modify the values as needed.
     Example JSON

     ```
     {



     "updateToken": "vu9U3hXY3q0ATAAkMG",



     "value": {



     "name": "Queue Sharing Group",



     "queueManagers": [



     "Queue Manager A",



     "Queue Manager B"



     ],



     "sharedQueues": [



     "Shared Queue A",



     "Shared Queue B"



     ]



     }



     }
     ```
3. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update IMS bridge

The ID of the IMS bridge schema is `builtin:ibmmq.ims-bridges`.

1. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
2. Create the JSON for your update.

   * Use the **updateToken** value from the previous step.
   * Modify the values as needed.

     Example JSON

     ```
     {



     "updateToken": "vu9U3hXY3q0ATAAkMG",



     "value": {



     "name": "IMS Bridge",



     "queueManagers": [



     {



     "name": "Queue Manager",



     "queueManagerQueue": [



     "Queue A",



     "Queue B"



     ]



     }



     ]



     }



     }
     ```
3. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

## Related topics

* [Set up IBM MQ tracing on z/OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring "Trace IBM MQ messages with Dynatrace on z/OS.")


---


## Source: tags-and-management-zones.md


---
title: Queue tags and management zones
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones
scraped: 2026-02-15T09:12:05.482467
---

# Queue tags and management zones

# Queue tags and management zones

* How-to guide
* 2-min read
* Published May 16, 2022

You can use tags and management zones to organize queue entities in your environment and simplify searches for them. Tags and management zones are applied to queue entities just as they are for other entities, but they must be applied via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Define an automatically applied tag

Follow the steps below to automatically apply a tag to queue entities. To learn more about tags, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

1. Go to **Settings** > **Tags** > **Automatically applied tags**.
2. Select **Create tag** and type a name for the new tag in the **Tag name** field.
3. Select **Add a new rule**.
4. Optional Specify an **Optional tag value**. This value will appear next to the tag name after a `:` and is used to provide more precise information about the queue entity.
5. From the **Rule type** list, choose the **Entity selector** type.
6. Use one of the following code snippets to apply tags from a service, process group, host, or host group entity to a queue entity via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."). Replace `yourKey:yourValue` with your own tag values.

   Producer services

   Consumer services

   Process groups

   Hosts

   Host groups

   ```
   type(QUEUE),toRelationships.indirectlySendsToQueue(type(SERVICE),tag("yourKey:yourValue "))
   ```

   ```
   type(QUEUE),toRelationships.listensOnQueue(type(SERVICE),fromRelationships.calls(type(SERVICE),tag("yourKey:yourValue")))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isInstanceOf(type(PROCESS_GROUP),tag("yourKey:yourValue"))))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),tag("yourKey:yourValue"))))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.isInstanceOf(type(HOST_GROUP),tag(("yourKey:yourValue")))))
   ```
7. Select **Preview** to verify the results returned by the specific entity selector.
8. Select **Save changes**.

Example of a rule-based entity selector

![Queue entity selector](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Add queue entities to existing management zones

Follow the steps below to add queue entities to existing management zones. To learn more about management zones, see [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.").

1. Go to **Settings** > **Preferences** > **Management zones**.
2. Edit an existing management zone and select **Add a new rule**.
3. In the **Rule applies to** list, choose the **Entity selector**.
4. Use one of the following code snippets to add a queue entity based on tags from a service, process group, host, or host group entity to a management zone via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."). Replace `yourKey:yourValue` with your own tag values.

Producer services

Consumer services

Process groups

Hosts

Host groups

```
type(QUEUE),toRelationships.indirectlySendsToQueue(type(SERVICE),tag("yourKey:yourValue "))
```

```
type(QUEUE),toRelationships.listensOnQueue(type(SERVICE),fromRelationships.calls(type(SERVICE),tag("yourKey:yourValue")))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isInstanceOf(type(PROCESS_GROUP),tag("yourKey:yourValue"))))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),tag("yourKey:yourValue"))))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.isInstanceOf(type(HOST_GROUP),tag(("yourKey:yourValue")))))
```

5. Select **Preview** to verify the results returned by the specific entity selector.
6. To save your management zone configuration, select **Save changes** at the bottom right corner of the page.

Example of a management zone based on the entity selector

![Management zone for queues](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Related topics

* [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")


---


## Source: configuration.md


---
title: Configure message queue monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration
scraped: 2026-02-17T05:10:54.917096
---

# Configure message queue monitoring

# Configure message queue monitoring

* How-to guide
* 3-min read
* Updated on Dec 28, 2022

Dynatrace automatically detects how messages are processed within your environment. Under certain circumstances, however, some manual configuration is needed to allow Dynatrace to detect how messages are processed.

## Manual configuration

Review the following table to determine whether some manual configuration is needed.

If this is trueâ¦

â¦then this manual configuration is needed

The application uses non-standard or non-event-based message queue handlers.

Define a [custom messaging service](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Set up custom messaging services to trace message queues.").

You're using IBM MQ.

Define your [IBM MQ](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing "Configure Dynatrace for IBM MQ tracing.") configuration in Dynatrace to get a continuous service flow.

The messaging client isn't compatible with Dynatrace, or you're using an unsupported protocol.

Extend the traces with [OpenTelemetry](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.") or [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") (see also [OneAgent SDK on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK#trace-messaging)).

## Process group detection

OneAgent version 1.250+ Dynatrace uses the IBM MQ queue manager name to detect and group IBM MQ processes. To manage the IBM MQ process group detection

* Go to **Settings** > **Processes and containers** > **Built-in detection rules** and find **Group IBM MQ processes by queue manager name**.
* Via [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), use the `builtin:process-group.detection-flags` schema ID.

  To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

The process group detection requires a restart of the IBM MQ process.

## Related topics

* [Custom messaging services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Set up custom messaging services to trace message queues.")


---


## Source: queue-concepts.md


---
title: Queue concepts
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/queue-concepts
scraped: 2026-02-17T21:27:17.335325
---

# Queue concepts

# Queue concepts

* Explanation
* 4-min read
* Updated on Jan 26, 2023

Message queues provide lightweight storage for messages. They're typically implemented with a client-server architecture. In such an architecture, applications connect to queues or topics via messaging clients, while the queues and topics themselves are operated by the messaging server (for example, by a queue manager or a broker).

Message queues take the form of either a queue or a topic. They offer endpoints that allow applications to send messages to them and endpoints that allow applications to retrieve messages from them asynchronously or to subscribe to topics.

* Queue: A single message is retrieved by exactly one consumer even when more consumers are connected to the queue (**point-to-point model**).
* Topics: A single message is published to all subscribers of the topic (**publish-subscribe model**).

![Difference between queues and topics](https://dt-cdn.net/images/queue-topic-difference-1295-f5e81189ca.png)

## Prerequisites

OneAgent must run in [Full-Stack Monitoring](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") mode to detect queues and topics as part of distributed traces. Only in Full-Stack Monitoring mode does Dynatrace create a continuous service flow across connected producer and consumer services.

## Queue entity types: queues and topics

OneAgent automatically detects queues and topics when monitored applications interact with them by instrumenting compatible messaging clients. When queues and topics aren't used by applications, OneAgent can't access them even if they're available on the messaging server. To check the compatible clients, see [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Dynatrace creates **Queue** entities for all detected queues and topics that are part of distributed traces. These entities are shown in the **Queues and topics** table on the **Queues** page.

Entity

Type

Naming schema

Queue

Queue

`<queue-name>`

Queue

Topic

`<topic-name>`

Queue

IBM MQ queue

`<queue-manager-name>.<queue-name>`

Queue

IBM MQ topic

`<queue-manager-name>.<topic-name>`

Limitation

Dynatrace extensions can detect queues and topics that are available on the messaging server, but they don't result in **Queue** entities in Dynatrace. Hence, they aren't visible in the **Queues and topics** table. Dynatrace extensions can only add technology-specific metrics to entities created by OneAgent.

## Messaging services

### Producer and consumer services

* A producer service represents an application that sends messages to a queue or a topic via a messaging client.
* A consumer service represents

  + An application that asynchronously retrieves messages from a queue via a [listener](#listener-service)
  + Or an application that is subscribed to a topic via a [listener](#listener-service).
* In a JMS-based application (Java message service), there can be also a synchronous consumer service. In this scenario, a client can request the next message from a `MessageConsumer` synchronously by using one of its [receive methodsï»¿](https://docs.oracle.com/javaee/7/api/javax/jms/MessageConsumer.html) (for example, the client can poll or wait for the next message).

To provide you with a continuous view of service flows, Dynatrace uses the following identifiers to trace messages across queues and topics

Identifier

Type

`traceparent` and `tracestate`

HTTP request header

`x-dynatrace`

Custom HTTP header

`dtdTraceTagInfo`

Custom message property

Unique key (generated based on message properties)

-

### Listener services

A listener service, or queue listener service, represents your queue listener or topic listener. It counts how many messages have been dequeued, but it doesn't give you insight into the message processing itself.

Dynatrace automatically detects an event-based message queue handler based on its class name and creates a queue listener service for it. A listener service is always followed by a consumer service, which gives you insight into the message processing details.

If you're just monitoring a queue or topic, and not looking into the message processing, the listener service can exist on its own.

Because of their properties,

* Listener services aren't visible on the analytics pages available from the **Queues** page, but you can find details in the [**Service analysis**](/docs/observe/application-observability/services-classic "Learn about Dynatrace's classic service monitoring"), [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment."), and [**Distributed traces**](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") pages.
* Listener service requests can't be renamed or pinned to a dashboard.

  Note that a listener service is always followed by a messaging service on which you can perform such actions. For example, you can rename the messaging service requests via (global) [request naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") using the message queue name as a placeholder, and then [pin the request to a dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles#tile-service-or-request "Find out how to configure your dashboard to track business-critical user-actions and conversion goals.").

### Examples

The following is a service flow example with a producer service, queue entity, listener service, and consumer service.

![Queue service flow](https://dt-cdn.net/images/queues-service-flow-1941-d21a293780.png)

The following is a distributed trace example with a producer service, queue entity, listener service, and consumer service.

![Queue distributed traces](https://dt-cdn.net/images/queue-distributed-traces-1939-2ca7ac0044.png)

## Related topics

* [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")
* [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")


---


## Source: queues.md


---
title: Message queues
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues
scraped: 2026-02-17T21:22:02.484237
---

# Message queues

# Message queues

* Explanation
* 4-min read
* Updated on Jul 15, 2022

Message queues in the form of a queue or a topic provide lightweight storage for messages. They offer endpoints that allow applications to send messages to them and endpoints that allow applications to retrieve messages from them asynchronously or to subscribe to topics. For full details, see [Queue concepts](/docs/observe/infrastructure-observability/queues/queue-concepts "Basic concepts of message queue monitoring in Dynatrace.").

Decoupled services are standard in applications built with microservices, and events are used to communicate between services, making it essential to observe the performance of message queues. With Dynatrace, you can get full observability into your producer and consumer services and simplify troubleshooting in asynchronous communication flows.

[### Queue concepts

Learn the most important concepts of queue monitoring.](/docs/observe/infrastructure-observability/queues/queue-concepts "Basic concepts of message queue monitoring in Dynatrace.")[### Configuration

Configure monitoring, tracing for IBM MQ, tags, and management zones.](/docs/observe/infrastructure-observability/queues/configuration "Configure Dynatrace to monitor message queues.")[### Analysis

Analyze queues and topics in your environment.](/docs/observe/infrastructure-observability/queues/analyze-queues "Get insight into message queue-related anomalies with analytics views.")

## Queues and topics in Dynatrace

OneAgent automatically detects queues and topics as part of distributed traces when monitored applications use the endpoints of compatible messaging clients to send or retrieve messages. To check the compatible clients, see [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To get an overview of all detected queues and topics, go to **Message Queues**.

* For all queues and topics, OneAgent measures the number of **Incoming messages** and **Outgoing messages**.  
  By monitoring these metrics, you can catch unbalanced message processing that could result in severe problems (such as queue overflows) and prevent them by scaling queues quickly or maintaining failover processes.
* Select the **Name** of a specific queue or topic to display its [analytic view](/docs/observe/infrastructure-observability/queues/analyze-queues "Get insight into message queue-related anomalies with analytics views."), with enhanced troubleshooting capabilities to gain additional insight into related anomalies.

![Message queues table](https://dt-cdn.net/images/queues-table-1857-49308cb749.png)

## Extensions

Unable to render DataTable. Check configuration.

## FAQ

What is the difference between a queue and a topic?

* Queue: a single message is retrieved by exactly one consumer (point-to-point model) even when more consumers are connected to the queue.
* Topic: a single message is published to all subscribers of that topic (publish-subscribe model).

In Dynatrace, both a queue and a topic result in a **Queue** entity.

Is a specific license required for OneAgent to detect queues and topics?

No. Queues and topics are detected as part of distributed traces when OneAgent is running in [Full-Stack Monitoring](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") mode.

Can OneAgent detect queues and topics in Infrastructure Monitoring mode?

No. Queues and topics are detected as part of distributed traces only when OneAgent is running in [Full-Stack Monitoring](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") mode.

When are queues and topics visible?

After queues and topics are detected by OneAgent on the messaging client-side, the **Queues and topics** table lists the ones that are part of distributed traces. Keep in mind that all queues and topics might not be used by the monitored applications or be accessed by OneAgent.

Can Dynatrace extensions detect queues and topics?

Yes, but the queues and topics detected by Dynatrace extensions don't result in **Queue** entities in your environment. Extensions can only add technology-specific metrics to **Queue** entities created by OneAgent. This is why queues and topics detected by extensions aren't visible in the **Queues and topics** table.

Why is there sometimes a difference between the number of queues or topics detected by OneAgent and by Dynatrace extensions?

While Dynatrace extensions detect queues and topics on the messaging server side, OneAgent detects them exclusively on the messaging client side. Additionally, not all queues and topics might be used by the monitored application or be accessed by OneAgent.

Why are the numbers of incoming and outgoing messages sometimes lower in Dynatrace?

The numbers of incoming and outgoing messages per queue or topic are calculated based on the data provided by monitored producer and consumer services. If a producer or consumer service is not monitored, the number of messages per queue or topic could be lower in Dynatrace than the actual number of processed messages.

Why are certain permanent queues or topics marked as temporary?

If a queue name or topic name contains four consecutive digits, Dynatrace automatically considers it to be a temporary queue or topic. For example, the queue name `A4214QA` contains four consecutive digits (`4214`), which will result in a temporary queue.

Dynatrace applies this logic to prevent monitoring of too many queues or topics. If this limit presents a problem in your environment, you can request an increase from four consecutive digits. To do so, Please contact a Dynatrace product expert via live chat within your environment.

Which messaging clients are compatible with OneAgent?

OneAgent supports various messaging clients. To find out the compatible clients, see [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Why is my ActiveMQ broker not detected?

The [ActiveMQ transport configurationï»¿](https://activemq.apache.org/components/classic/documentation/activemq-classic-connection-uris) of a broker with the IP address 0.0.0.0 is not supported.

This configuration allows the broker to accept incoming messages on all network interfaces, while a broker IP address configured on a specific network interface is required for Dynatrace to establish a connection between the broker and its queues and to capture related metrics.

How can I define an automatically applied tag for queue entities?

Visit the related section on the [Tags and management zone page](/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones#tags "Automatically apply tags to queues and organize them into management zones.").

How can I add queue entities to existing management zones?

Visit the related section on the [Tags and management zone page](/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones#management-zones "Automatically apply tags to queues and organize them into management zones.").


---


## Source: limit-infrastructure-monitoring-using-permissions.md


---
title: Limit VMware infrastructure monitoring using permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/vmware-vsphere-monitoring/limit-infrastructure-monitoring-using-permissions
scraped: 2026-02-17T21:33:30.633786
---

# Limit VMware infrastructure monitoring using permissions

# Limit VMware infrastructure monitoring using permissions

* How-to guide
* Published Feb 10, 2021

The following applies to VMware only. For other virtualization platforms, you only need to install OneAgent for virtualized host monitoring, as the monitoring of virtualization management layers is supported only for VMware.

When you set up VMware monitoring, you can manage the infrastructural elements (such as hosts and VMs) that you want Dynatrace to monitor by setting or adjusting permissions in vCenter.

See the examples below for details on how to manage user permissions for your VMs.

## Prerequisites

* Administrator role with access to permissions management in vCenter

## Monitor all VMs in a resource pool

To monitor all VMs in a resource pool (or any other "parent" in VMware infrastructure hierarchy), you need to

Assign users read-only permissions to your VMware hosts

To assign users read-only permission to your VMware hosts

1. In vCenter, go to the host view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select the **Read-only** role.
4. Select **OK** to save your changes.

Because a VM might migrate to a different host at a later time, we recommend that you enable Dynatrace monitoring (add read-only permissions) on all hosts to which your VM might migrate.

Assign users read-only permissions to the resource pool

To assign users read-only permission to the resource pool

1. In vCenter, go to the resource pool view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select the **Read-only** role.
4. Select **Propagate to children**.
5. Select **OK** to save your changes.

After assigning users read-only permission to your VMware hosts and to the resource pool, the hosts and VMs to which you granted permissions will be visible in Dynatrace.

Example cluster view

![Dyna vmware01](https://dt-cdn.net/images/dyna-vmware01-1506-10eee7374d.png)

Example host view

![Host view](https://dt-cdn.net/images/2021-02-11-14-43-16-1521-d78906c12f.png)

## Exclude a single VM from monitoring

To exclude a single VM from Dynatrace monitoring, such as a VM that inherited read-only permissions from its parent, you need to remove user read permissions for the respective VM.

To remove a user's read permissions for a VM

1. In vCenter go to the VM view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select **No access** for the role.
4. Select **OK** to save your changes.

## Add a single VM to monitoring

To add a single VM to Dynatrace monitoring, you need to assign users read-only permission to the respective VM.

To assign users read-only permission to a VM

1. In vCenter go to the VM view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select the **Read-only** role.
4. Select **OK** to save your changes.

## Related topics

* [VMware vSphere monitoring](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.")


---


## Source: vmware-vsphere-monitoring.md


---
title: VMware vSphere monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/vmware-vsphere-monitoring
scraped: 2026-02-06T16:29:07.626668
---

# VMware vSphere monitoring

# VMware vSphere monitoring

* Overview
* Published Aug 12, 2021

Setting up Dynatrace monitoring of a VMware platform is easy using ActiveGate as a communication gateway.

* ActiveGate receives the data from VMware and sends it to the Dynatrace Cluster.
* OneAgent, which is installed on each virtual machine, provides complementary data about your infrastructure health.

**Flow of monitoring data from your VMware platform to Dynatrace:**

![Virtualization data flow](https://dt-cdn.net/images/virtualization-flow-1280-93a1053e89.png)

The following applies to VMware only. For other virtualization platforms, you only need to install OneAgent for virtualized host monitoring, as the monitoring of virtualization management layers is supported only for VMware.

Once Dynatrace OneAgent is installed and process monitoring is activated on a virtual machine, you can see what's happening in your operating systemâspecifically, how your host-based processes behave and communicate.

Dynatrace collects information related to virtualized CPU usage, memory consumption, and storage-related activities. Dynatrace also detects virtual machine migrations (vMotion) and the creation of new virtual machines.

Follow the steps below to set up monitoring on the virtualization management layer of your VMware vCenter or standalone ESXi hosts.

## Prerequisites

* Read-only access to vCenter server, or access to the standalone ESXi host.

## Install and configure ActiveGate

[Install an Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") in your data center before connecting Dynatrace to your VMware platform.  
For **Dynatrace Managed** you can use the embedded ActiveGate running on the cluster node. However, the Cluster ActiveGate is typically used to forward RUM and/or Synthetic monitoring data to the Dynatrace Cluster. We recommend that you don't overutilize this ActiveGate with another type of monitoring data. Depending on the VMware size, you might consider using a dedicated ActiveGate per environment.

For virtualization monitoring, the `vmware_monitoring_enabled` property in `custom.properties` must be set to `true` (default value).

See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#vmware "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details.

## Connect Dynatrace to your VMware platform

To connect Dynatrace to your VMware platform

1. Go to **Settings** > **Cloud and virtualization** > **VMware**, and select **Connect new instance**.
2. Select the IP address or name of the vCenter server or standalone ESXi host you want to monitor (skip the `http://` or `https://` protocol prefix).
3. Check the network/proxy settings.  
   If you get a communication error even though the data provided is correct, it might be because of your network/proxy settings. We recommend that you revise the network/proxy settings when adding a new VMware integration.

   Optional You can also bypass the proxy for connecting with vCenter or ESXi when configuring the VMware integration. Modify [ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#exclude-hosts "Learn how to configure ActiveGate properties to set up a proxy.") to exclude a specific host from the proxy.
4. Enter the associated user credentials so that ActiveGate can sign in and collect monitoring data. The required privileges for this user are **view and read-only access**. Administrator-level access isn't required to enable monitoring (no changes to your VMware settings are required).

   You donât need to add ESXi hosts individually if they're managed by a vCenter server.
5. ActiveGate version 1.268+ Specify a filter condition to limit the number of monitored clusters:

   * `$prefix(parameter)`âproperty value starts with `parameter`
   * `$eq(parameter)`âproperty value exactly matches `parameter`
   * `$suffix(parameter)`âproperty value ends with `parameter`
   * `$contains(parameter)`âproperty value contains `parameter`
6. Select **Test connection** to verify that the entered data has successfully connected to your vCenter.

   Credentials

   The credentials are no longer validated automatically, so it's important to provide valid credentials that connect to your vCenter. If you provide invalid credentials, Dynatrace will still attempt to connect to your vCenter, which can create unnecessary network traffic.

   If your credentials for a particular vCenter change over time and you forget to update them in the settings, Dynatrace will detect five failed attempts to connect to your vCenter. After this, this setting will be disabled to prevent your VMware account from being blocked.
7. Select **Save changes**.

   Time synchronization

   Differences in system time can lead to missing VMware metrics. For Dynatrace to properly display monitoring data, synchronize time settings on all monitored host environments and vCenters with an NTP server.

To cover your entire virtual infrastructure, repeat these steps for all other vCenter servers or standalone ESXi hosts in your environment.

## Limit VMware infrastructure monitoring

After you set up VMware monitoring, you might want to limit which infrastructural elements (such as hosts and VMs) should actually be monitored by Dynatrace. To do this, you can use the permissions mechanism available in VMware. For more information, see [Limit VMware infrastructure monitoring using permissions](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring/limit-infrastructure-monitoring-using-permissions "Limit the size of your monitored VMware infrastructure using the VMware permissions mechanism.").

## Troubleshoot VMware connection

* Option 1 - [vCentre Event Consoleï»¿](https://dt-url.net/mh238c4)
* Option 2 - [VMware PowerCLIï»¿](https://dt-url.net/ni038yh) Windows only
* [Monitoring invalid credentialsï»¿](https://dt-url.net/fi038fn)

## Configure vSphere monitoring using Settings API

You can use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure VMware vSphere monitoring.

1. To learn the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:virtualization.vmware` as the schemaId.
2. Based on the `builtin:virtualization.vmware` schema, create your configuration object.
3. To create your configuration, use [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").


---
