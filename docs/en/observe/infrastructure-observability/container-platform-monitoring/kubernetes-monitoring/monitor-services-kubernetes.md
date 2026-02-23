---
title: Monitor Kubernetes/OpenShift services
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-services-kubernetes
scraped: 2026-02-23T21:26:35.911498
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