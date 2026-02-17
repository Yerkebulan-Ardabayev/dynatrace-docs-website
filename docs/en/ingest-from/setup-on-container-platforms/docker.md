---
title: Set up Dynatrace on Docker
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/docker
scraped: 2026-02-17T21:19:34.584579
---

# Set up Dynatrace on Docker

# Set up Dynatrace on Docker

* Latest Dynatrace
* 1-min read
* Published Jun 25, 2021

Dynatrace offers full-featured Docker monitoring, as well as generic container monitoring for containerd and CRI-O, giving you all the same deep monitoring capabilities for containerized applications that are available for non-containerized applications.

## Integrations

If you want to use Docker outside a container platform, there are two methods to monitor applications using OneAgent:

* [Set up OneAgent for application-only](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.")
* [Set up Dynatrace as a Docker container](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.")

In a typical scenario, container orchestration and management tools such as Kubernetes, OpenShift, and Cloud Foundry use Docker, containerd, or CRI-O as a container runtime. If you're running one of these platforms, follow the appropriate deployment instructions: [Kubernetes](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), [OpenShift](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH."), or [Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate."). Any platform that uses containers can also be monitored using the [application-only approach](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

## Related topics

* [Monitor container groups](/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups "Overview on container groups monitoring")