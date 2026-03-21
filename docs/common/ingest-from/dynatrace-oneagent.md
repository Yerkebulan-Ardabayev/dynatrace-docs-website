---
title: "Dynatrace OneAgent"
source: https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent
updated: 2026-02-09
---

# Dynatrace OneAgent


* Latest Dynatrace
* 2-min read
* Published Oct 09, 2018

OneAgent is responsible for collecting all monitoring data within your monitored environment. A single OneAgent per host is required to collect all relevant monitoring dataâeven if your hosts are deployed within Docker containers, microservices architectures, or cloud-based infrastructure.

A single instance of OneAgent can handle [monitoring for all types of entities](../platform/oneagent/supported-monitoring-types.md "Read an overview of all monitoring capabilities offered by OneAgent."), including servers, applications, services, databases, and more. OneAgent gives you all the operational and business performance metrics you need, from the frontend to the backend and everything in betweenâcloud instances, hosts, network health, processes, and services. OneAgent discovers all the processes you have running on your hosts. Based on what it finds, OneAgent automatically activates instrumentation specifically for your unique application stack. It also injects all tags required for user-experience monitoring into the HTML of your application pages. New components are auto-instrumented on the fly.

OneAgent is comprised of several code modules that enable OneAgent to work for most technologies out-of-the-box. To find out which code modules are supported for each platform, see the [OneAgent platform and capability support matrix](technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms."). To see which versions are supported for each code module, see [OneAgent supported technologies and versions](technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Requirements

[OneAgent requirements](dynatrace-oneagent/oa-requirements.md "OneAgent code module requirements")

### See also

[Adaptive Traffic Management](dynatrace-oneagent/adaptive-traffic-management.md "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.")

### Installation and operation

Cloud platforms

Kubernetes

Other container platforms

Operating systems

[![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS")AWS](amazon-web-services.md) [![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure")Azure](microsoft-azure-services.md) [![Google Cloud](https://dt-cdn.net/images/gcp-512-db85a455ae.webp "Google Cloud")Google Cloud](google-cloud-platform.md)

[![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes")Kubernetes](setup-on-k8s.md)

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")Cloud Foundry](setup-on-container-platforms/cloud-foundry.md) [![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")Docker](setup-on-container-platforms/docker.md) [![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")Heroku](setup-on-container-platforms/heroku.md) [![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")Mesos](setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon.md)

[AIX](dynatrace-oneagent/installation-and-operation/aix.md) [Linux](dynatrace-oneagent/installation-and-operation/linux.md) [Solaris](dynatrace-oneagent/installation-and-operation/solaris.md) [Windows](dynatrace-oneagent/installation-and-operation/windows.md) [zOS](dynatrace-oneagent/installation-and-operation/zos.md)
