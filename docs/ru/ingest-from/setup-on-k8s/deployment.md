---
title: Deployment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment
scraped: 2026-02-18T21:18:30.489283
---

# Deployment

# Deployment

* Latest Dynatrace
* 6-min read
* Updated on Jan 28, 2026

Dynatrace provides a flexible approach to Kubernetes observability where you can pick and choose the level of observability you need for your Kubernetes clusters. This page gives an overview and guided path on the recommended options to cover your Kubernetes observability needs.
All deployment options on this page leverage [Dynatrace Operatorï»¿](https://github.com/Dynatrace/dynatrace-operator). For dedicated documentation and options for the major Kubernetes distributions, see [Distributions](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Observability options

**Observability value**

**Kubernetes platform monitoring**

**Kubernetes platform monitoring**  
+ **Application observability**

**Kubernetes platform monitoring**  
+ **Full-Stack observability**

Kubernetes platform

[Kubernetes resources and topology](/docs/observe/infrastructure-observability/kubernetes-app/use-cases "Real-world scenarios and best practices for leveraging the new Dynatrace Kubernetes experience.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Kubernetes metrics (CPU, memory, network, PVCs), events, and alerts](/docs/observe/infrastructure-observability/kubernetes-app/use-cases "Real-world scenarios and best practices for leveraging the new Dynatrace Kubernetes experience.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Applications

[Automatic distributed tracing across containers](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Code-level and service insights](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") in application containers

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Profiling and thread analysis](/docs/observe/application-observability/profiling-and-optimization "Learn how to use Dynatrace diagnostic tools for crash analysis, memory dump analysis, and more.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Live debugging for cloud-native applications](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.")

opt-in

opt-in

Infrastructure

[Host and process level details](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Host network analysis and topology](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Disk analysis and alerting](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Data in context

[Data enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation "Automate and optimize your system's metadata management") for [cost allocation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") and access control

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

License

[DPS pricing/packaging](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")

by [number of Pods](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.")

by [number of Pods](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.") and [sum container memory](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")

by [sum host memory](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")

Additional opt-in values

Log analytics

[Log collection, data filtering, masking, processing and analytics](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.")

opt-out[1](#fn-1-1-def)  
[per GiB ingested](/docs/ingest-from/setup-on-k8s/quickstart "Deploy Dynatrace Operator on Kubernetes")

opt-out[1](#fn-1-1-def)  
[per GiB ingested](/docs/ingest-from/setup-on-k8s/quickstart "Deploy Dynatrace Operator on Kubernetes")

opt-out[1](#fn-1-1-def)  
[per GiB ingested](/docs/license/capabilities/log-analytics/dps-log-ingest "Learn how your consumption of the Log Management & Analytics - Ingest & Process DPS capability is billed and charged.")

Digital experience

[Real user monitoring, synthetic checks and session replay](/docs/observe/digital-experience "Optimize end-user experience with Digital Experience Monitoring to ensure application performance and availability across all channels.")

opt-in  
For details, see [DEM](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
For details, see [DEM](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

Application Security

[Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") and [Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

opt-in  
[by sum container memory](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
[by sum host memory](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

[Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")

opt-in  
[by host-hour](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
[by host-hour](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
[by host-hour](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

1

For new users, the Dynatrace environment is preconfigured to ingest logs, and opting out is managed through [log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

Rollout and permissions overview

This table gives an overview of all the used components and required permissions for your Kubernetes observability needs. Dynatrace Operator manages the lifecycle of all observability components needed for your Kubernetes observability needs.

**Components and permissions**

**Kubernetes platform monitoring**

**Kubernetes platform monitoring**  
+ **Application observability**

**Kubernetes platform monitoring**  
+ **Full-Stack observability**

Components

Dynatrace Operator for managing observability components and lifecycle

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Dynatrace Operator webhook for auto-injection and telemetry enrichment

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Dynatrace Operator CSI driver for resource-friendly management of components

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") (opt-out)

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Observability components

ActiveGate

ActiveGate  
Dynatrace code modules  
Dynatrace Log module (opt-in)

ActiveGate  
Dynatrace code modules  
Dynatrace host module  
Dynatrace Log module

Dynatrace OpenTelemetry collector for extensions

opt-in

opt-in

opt-in

EdgeConnect for automations

opt-in

opt-in

opt-in

Permissions

Principle of least privilege

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Kubernetes permissions [1](#fn-2-1-def)

Kubernetes RBAC

Kubernetes RBAC  
Privileged workload (CSI driver, opt-out)

Kubernetes RBAC  
Privileged workload (CSI driver)  
OS-level permission (Dynatrace host module)

1

Please see [Dynatrace Operator security](/docs/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") for more detailed documentation.

[### Kubernetes platform monitoring

Understand and troubleshoot the health of your Kubernetes clusters.](/docs/ingest-from/setup-on-k8s/deployment/platform-observability "Deploy Dynatrace Operator for Kubernetes platform monitoring.")[### Kubernetes platform monitoring + Application observability

Ensure workload and microservice health and performance with automatic instrumentation.](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")[### Kubernetes platform monitoring + Full-Stack observability

Ensure workload, microservice and infrastructure health and performance throughout your cluster.](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes")



## Leverage the Dynatrace platform value

The Dynatrace platform offers a variety of apps, analytics and automation functionality to cover your use cases for unified observability and security. You can leverage these capabilities for all the Kubernetes observability data you collect with any of the above modes, such as the ability to:

* Explore Kubernetes health and signals in the [Kubernetes app](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")
* Visualize data with [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* Collaborate and conduct custom analysis with [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* Automate with [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* Boost productivity with [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") and [enerative AI](/docs/dynatrace-intelligence/copilot "Learn about Dynatrace Intelligence generative AI.")
* Forecast trends and prevent issues with [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")
* And much moreâ¦

## Deployment from Marketplaces

Dynatrace supports deploying Dynatrace Operator from within the following Marketplaces:

* [OpenShift OperatorHub](/docs/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub "Deploy Dynatrace Operator on OpenShift via OperatorHub.")
* [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplaceï»¿](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplaceï»¿](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Learn more

[### How it works

Familiarize yourself with Dynatrace components that are deployed in your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.")[### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases")[### Reference

API reference and configuration options for all Dynatrace components within your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/reference "Contains a reference page with configuration options for each Dynatrace component")[### Dynatrace Operator release notes

See release notes for Dynatrace Operator.](/docs/whats-new/dynatrace-operator "Release notes for Dynatrace Operator")