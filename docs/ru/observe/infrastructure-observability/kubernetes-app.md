---
title: Kubernetes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app
scraped: 2026-02-28T21:06:17.917231
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