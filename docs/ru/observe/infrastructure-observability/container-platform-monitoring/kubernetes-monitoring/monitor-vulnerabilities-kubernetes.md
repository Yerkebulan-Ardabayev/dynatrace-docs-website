---
title: Monitor vulnerabilities in Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes
scraped: 2026-02-28T21:34:17.763683
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