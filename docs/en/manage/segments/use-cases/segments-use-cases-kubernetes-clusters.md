---
title: Segment data by Kubernetes clusters
source: https://www.dynatrace.com/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters
scraped: 2026-02-17T21:18:59.753974
---

# Segment data by Kubernetes clusters

# Segment data by Kubernetes clusters

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Mar 29, 2023

Configure a segment for signals and monitored entities related to multiple Kubernetes clusters in a common stack.

## Who this is for

This article is intended for administrators and Kubernetes operators who need to organize and logically structure workloads on Kubernetes clusters.

## What you will learn

In this article, you'll learn how to create a segment to conveniently filter observability signals and monitored entities in the Kubernetes domain.

## Before you begin

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes "Learn how data of different types can be included in segments.")
* [Segments in DQL queries](/docs/manage/segments/concepts/segments-concepts-queries "Learn how Grail evaluates segments during query execution to return matching results only.")
* [Getting started with Kubernetes experience](/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience "Enable Kubernetes experience for existing clusters or start monitoring new clusters.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have both `storage:filter-segments:write` and `storage:filter-segments:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
* You have licensed and set up [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a segment for clusters of a common stack**](/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters#create "Configure a segment for signals and monitored entities related to Kubernetes clusters")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Include observability signals and monitored entities**](/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters#include "Configure a segment for signals and monitored entities related to Kubernetes clusters")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Analyze performance and health of entire stack**](/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters#analyze "Configure a segment for signals and monitored entities related to Kubernetes clusters")

### Step 1 Create a segment for clusters of a common stack

In our example, a set of a few individual Kubernetes clusters make up a common stack. Together, these clusters form a stack we'll refer to as `dtp-dev3`.

1. Go to ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments") **Segments** and select  **Segment** to add a new segment
2. Give your segment a name and description

   * Select and edit **Untitled segment** to give your segment a name useful in you context  
     For this example, enter `dtp-dev3`
   * Select  **Description** and describe the segment  
     For this example, enter `Signals and entities of K8s clusters of dtp-dev3 deployment`
3. Select **Visibility** and set it to `Anyone in the environment` so others can find and use this segment
4. Select **Save**

At this point, the segment doesn't specify what data it should include. In the next section, we will reference data to be filtered with this segment.

### Step 2 Include observability signals and monitored entities

Since Kubernetes observability signals are consistently labelled with `k8s.*` dimensions and fields, our segment will make use of that by referencing them directly.

1. Select  **Add from data types** > **All data types**
2. Select **Type to filter** to include all data matching `k8s.cluster.name = dtp-dev3*`
3. Select  **Run query** to get a preview of matching data
4. Select **Save** to save your changes

   ![Signals of K8s clusters](https://dt-cdn.net/images/segments-k8s-signals-2090-2e33448917.png)

Including observability signals directly doesn't automatically include their emitting monitored entities. In the next section, we will include those entities specifically.

1. Select  **Add from entities and topology** > **Kubernetes cluster (dt.entity.kubernetes\_cluster)**
2. Select **Type to filter** to include all clusters matching `entity.name = dtp-dev3*`
3. Select  **Run query** to get a preview of matching clusters

   ![K8s clusters](https://dt-cdn.net/images/segments-k8s-clusters-2090-36fbc5501d.png)
4. Select  **Related entity** > **Kubernetes namespace**
5. Select  **Run query** for the newly added include block to get a preview of namespaces related to our clusters from above

   ![K8s namespaces of clusters](https://dt-cdn.net/images/segments-k8s-namespaces-2090-9f4067597b.png)
6. Select  **Related entity** and select all further related entities of Kubernetes clusters the segment is built around

   * Kubernetes namespace (already included)
   * Kubernetes node
   * Kubernetes pod
   * Kubernetes workload
   * Kubernetes service
   * Container group instance
   * Service
   * Host

Currently, monitored entities are included by their individual type. In future, we'll make this more flexible and allow including monitored entities of any type with a single condition.

### Step 3 Analyze health and performance of entire stack

In this step, we show how to

* Analyze general health of our stack in ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**
* Analyze health and performance of services of our stack in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**
* Analyze Kubernetes workloads of our stack in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

#### Problems

To analyze general health of our stack in ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**

1. Go to ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**
2. Open the segment selector  and, in **Filter by segments**, select the previously created segment `dtp-dev3`
3. Select **Apply** to finish segment selection
4. Select **Update** to refresh the problems list

   ![Problems affecting entities in dtp-dev3](https://dt-cdn.net/images/segments-k8s-problems-2140-1a51ddfe51.png)

By applying our segment, we get a filtered list of problems affecting any monitored entity of any type in our stack.

#### Services

To analyze health and performance of services of our stack in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**
2. Open the segment selector  and, in **Filter by segments**, select the previously created segment `dtp-dev3`
3. Select **Apply** to finish segment selection

   ![Services in dtp-dev3](https://dt-cdn.net/images/segments-k8s-services-2140-f351191c33.png)

By applying our segment, we get a filtered list of services related to any cluster of our stack.

#### Dashboards

To analyze Kubernetes workloads of our stack in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**
2. Select **Ready-made dashboards**
3. Select **Search documents** and type `Kubernetes`
4. Select **Kubernetes Namespaces - Workloads** to open the ready-made dashboard
5. Open the segment selector  and, in **Filter by segments**, select the previously created segment `dtp-dev3`
6. Open the dashboard filter **Cluster** to find clusters filtered for selected segment

   ![Dashboard: Kubernetes workloads in namespaces](https://dt-cdn.net/images/segments-k8s-dashboard-workloads-2640-c406e3c410.png)

By applying our segment, we narrow the context of a dashboard, making it possible to block out all other noise with a single click.

Applying a segment to dashboards will filter for data explicitly included in segment. Some tiles may no longer show results because queried data isn't included in the applied segment.

## Conclusion

Youâve configured a segment for a set of Kubernetes clusters that form a common stack. Youâve learned how segments can be applied to conveniently filter data in different apps. You've seen an example how to analyze health and performance of a monitoring environment wihtout having to write or understand a single line of DQL yourself.

Just as for Kubernetes clusters, segments can also be built with the context of Kubernetes namespaces. Simply use `k8s.namespace.name` and select all related entities of **Kubernetes namespaces (dt.entity.cloud\_application\_namespace)** instead.