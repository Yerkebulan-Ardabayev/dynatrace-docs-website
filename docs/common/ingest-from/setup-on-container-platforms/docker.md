---
title: "Set up Dynatrace on Docker"
source: https://docs.dynatrace.com/docs/ingest-from/setup-on-container-platforms/docker
updated: 2026-02-09
---

# Set up Dynatrace on Docker


* Latest Dynatrace
* 1-min read
* Published Jun 25, 2021

Dynatrace offers full-featured Docker monitoring, as well as generic container monitoring for containerd and CRI-O, giving you all the same deep monitoring capabilities for containerized applications that are available for non-containerized applications.

## Integrations

If you want to use Docker outside a container platform, there are two methods to monitor applications using OneAgent:

* [Set up OneAgent for application-only](docker/set-up-oneagent-on-containers-for-application-only-monitoring.md "Install, update, and uninstall OneAgent on containers for application-only monitoring.")
* [Set up Dynatrace as a Docker container](docker/set-up-dynatrace-oneagent-as-docker-container.md "Install and update Dynatrace OneAgent as a Docker container.")

In a typical scenario, container orchestration and management tools such as Kubernetes, OpenShift, and Cloud Foundry use Docker, containerd, or CRI-O as a container runtime. If you're running one of these platforms, follow the appropriate deployment instructions: [Kubernetes](../../../ru/ingest-from/setup-on-k8s/deployment.md "Deploy Dynatrace Operator on Kubernetes"), [OpenShift](../../../ru/ingest-from/setup-on-k8s/deployment.md "Deploy Dynatrace Operator on Kubernetes"), [Cloud Foundry](cloud-foundry/deploy-oneagent-on-cloud-foundry.md "Install OneAgent on Cloud Foundry with BOSH."), or [Fargate](../../../ru/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md "Install OneAgent on AWS Fargate."). Any platform that uses containers can also be monitored using the [application-only approach](docker/set-up-oneagent-on-containers-for-application-only-monitoring.md "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

## Related topics

* [Monitor container groups](../../observe/infrastructure-observability/container-platform-monitoring/container-groups.md "Overview on container groups monitoring")
