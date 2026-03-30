---
title: Monitor vulnerabilities in Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes
scraped: 2026-03-06T21:22:01.751523
---

# Monitor vulnerabilities in Kubernetes/OpenShift


* Classic
* 1-min read
* Published Aug 24, 2022

You can keep track of security vulnerabilities in your Kubernetes environments on the cluster and workload pages.

## Prerequisites

* In Dynatrace, go to your Kubernetes cluster settings page and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.
* Activate and enable Application Security
* To view code-level vulnerabilities Activate and enable Runtime Application Protection

## Vulnerability section

The **Vulnerabilities** section is displayed on the Kubernetes

* Cluster details page
* Workloads page

It shows the five most severe related third-party vulnerabilities and code-level vulnerabilities.

* Select a vulnerability to view the details and understand the severity and impact of a vulnerability within your environment.
* For a complete list of the detected vulnerabilities for your Kubernetes environment, select **Show all third-party vulnerabilities**/**Show all code-level vulnerabilities**.

Example third-party vulnerabilities:

![Kubernetes workload: TPV](https://dt-cdn.net/images/workload-tpv-766-510d3cb4aa.png)

Example code-level vulnerabilities:

![Kubernetes workload: CLV](https://dt-cdn.net/images/workload-clv-767-ba23d97d54.png)

If you're missing the [security permissions](../../../../secure/application-security.md#permissions "Access the Dynatrace Application Security functionalities.") for the selected management zone,

* On the **Kubernetes cluster** page, the **Vulnerabilities** section is not displayed.
* On the **Kubernetes workload** page, the **Vulnerabilities** tab on the notification bar shows `Not analyzed`.

## Related topics

* Set up Dynatrace on Kubernetes