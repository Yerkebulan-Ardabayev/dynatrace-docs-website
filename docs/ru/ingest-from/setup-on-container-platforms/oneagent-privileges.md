---
title: OneAgent privileges for container monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/oneagent-privileges
scraped: 2026-02-23T21:30:27.991568
---

# OneAgent privileges for container monitoring

# OneAgent privileges for container monitoring

* Latest Dynatrace
* 2-min read
* Published Mar 08, 2023

Dynatrace supports Full-Stack Monitoring for container platforms, from the application down to the infrastructure layer. This requires elevated privileges to get container-level metrics and perform deep-code host monitoring, including OneAgent injection into processes.

However, if you don't want to grant elevated privileges to OneAgent, or you don't have access to the infrastructure layer, you can go with application-only monitoring.

For Kubernetes, Dynatrace Operatorâbased application-only monitoring still provides you with a good scope of data, such as node-level insights (basic metrics and alerting) based on data retrieved by the ActiveGate from Kubernetes API, or Prometheus metrics.

## Full-stack injection

The OneAgent container and underlying host share selected Linux namespaces for OneAgent to be able to access data required for full-stack monitoring:

* Shared network namespace enables processes running inside the container to directly access host network interfaces.
* Shared PID namespace enables processes running inside the container to see and work with all the processes from the host process table.
* Mounted host's root filesystem is accessed by all OneAgent modules and allows for log files access, disk metrics, and other full-stack monitoring capabilities.

During monitoring, the scope of required permissions for each process is limited using specific [Linux System Capabilities](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#linux-system-capabilities "Find out when Dynatrace OneAgent requires root privileges on Linux.").

You can achieve full-stack injection using the following deployment modes:

* Dynatrace Operator on Kubernetes/OpenShift

  + [Cloud-native full-stack mode](/docs/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.")
  + [Classic full-stack mode](/docs/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.")
* Docker outside a container platform

  + [OneAgent as a Docker container](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.")

### OneAgent on Docker host

Alternatively, you can also deploy OneAgent on the Docker host on Linux. In this scenario, OneAgent does not run in a container but directly on the host, so there is no Linux namespace isolation. For more information, see [OneAgent on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.").

## Application-only injection

OneAgent deployed in application-only mode doesn't run as a privileged container.

For more information, see:

* [Get started with Kubernetes platform monitoring + Application observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")
* [Deploy OneAgent on Cloud Foundry for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")
* [Set up OneAgent on containers for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.")