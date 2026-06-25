---
title: Set up Dynatrace on container and PaaS platforms
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms
scraped: 2026-05-12T11:38:06.711760
---

# Set up Dynatrace on container and PaaS platforms

# Set up Dynatrace on container and PaaS platforms

* 3-min read
* Updated on Mar 02, 2023

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")

### Cloud Foundry

Set up and configure Dynatrace on Cloud Foundry.](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")[![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")

### Docker

Set up and configure Dynatrace on Docker.](/managed/ingest-from/setup-on-container-platforms/docker "Deploy OneAgent on Docker.")[![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")

### Heroku

Deploy OneAgent to monitor applications running on Heroku.](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")[![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")

### Mesos

Set up and configure Dynatrace on Mesos/Marathon.](/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon "Learn how to deploy OneAgent on Mesos/Marathon.")

The method you choose to monitor containers with Dynatrace depends on the following:

* The type of container runtime, such as Docker, containerd, or CRI-O
* The orchestration platform, such as Kubernetes, OpenShift, Cloud Foundry, or Fargate
* The level of access you have to the underlying host

See below for details.

## Full-stack injection

The most comprehensive option for monitoring containers with Dynatrace is to deploy OneAgent to your container platform, which gives you full-stack visibility into your complete containerized environment.

This assumes full access to the underlying host.

For most OneAgent deployments and Container runtimes, injection will be performed by the `oneagenthelper` process that runs as part of the OneAgent service on the host or within the OA container. However some runtimes will start the OneAgentHelper process directly or need assistance from the OneAgentâs process auto injection logic.

If you continue to see the `oneagenthelper` processes active on your hosts even after stopping the OneAgent Service, you may need to disable Automatic injection as outlined within our documentation here before stopping the oneagent service / container: [Infrastructure and Discovery monitoring modes](/managed/platform/oneagent/monitoring-modes/monitoring-modes#disable-auto-injection "Find out more about the available monitoring modes when using OneAgent.") or ensure that you using OneAgent version 1.281+ within your Classic Full Stack deployment.

### Cloud Foundry

Dynatrace supports full-stack monitoring for Cloud Foundry through the Dynatrace OneAgent BOSH Release.

See [Set up Dynatrace on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.").

### Docker outside container platform

You can deploy OneAgent directly on the Docker host or you can run OneAgent as a Docker container.

* [Deploy OneAgent on the Docker host](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* [Deploy OneAgent as a Docker container](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.")

### Heroku

Dynatrace supports full-stack monitoring for Heroku through the Dynatrace Heroku buildpack.

See [Set up Dynatrace on Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## Application-only injection

Use application-only injection if you don't have access to underlying hosts. Your options depend on the container platform you are using.

### Automated injection

The most efficient option is automated application-only injection for Kubernetes-based platforms. This injects OneAgent code modules using Kubernetes-native admission controllers.

* For Kubernetes, see [Get started with Application observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#automatic "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").
* For AWS Fargate, see [Monitor AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#autoinjection "Install OneAgent on AWS Fargate.")

### Runtime injection

Inject OneAgent code modules into a container as it is deployed.

* For Kubernetes/OpenShift, see [Get started with Application observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#runtime "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")
* For Cloud Foundry, see [Deploy OneAgent on Cloud Foundry for application-only monitoring](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")
* For AWS Fargate, see [Monitor AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#runtime "Install OneAgent on AWS Fargate.")

### Build-time injection

Inject OneAgent code modules into a container as it builds.

* For Docker outside container platforms, see [Set up OneAgent on containers for application-only monitoring](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.")
* For Kubernetes/OpenShift, see [Kubernetes container build-time application-only injection](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#build-time "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")
* For AWS Fargate, see [Monitor AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#buildtime "Install OneAgent on AWS Fargate.")

## Related topics

* [Container platform monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring "The container platforms Dynatrace can monitor")