---
title: Set up Dynatrace on Docker
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/docker
scraped: 2026-03-06T21:15:44.080621
---

# Set up Dynatrace on Docker


* Latest Dynatrace
* 1-min read
* Published Jun 25, 2021

Dynatrace offers full-featured Docker monitoring, as well as generic container monitoring for containerd and CRI-O, giving you all the same deep monitoring capabilities for containerized applications that are available for non-containerized applications.

## Integrations

If you want to use Docker outside a container platform, there are two methods to monitor applications using OneAgent:

* Set up OneAgent for application-only
* Set up Dynatrace as a Docker container

In a typical scenario, container orchestration and management tools such as Kubernetes, OpenShift, and Cloud Foundry use Docker, containerd, or CRI-O as a container runtime. If you're running one of these platforms, follow the appropriate deployment instructions: Kubernetes, OpenShift, Cloud Foundry, or Fargate. Any platform that uses containers can also be monitored using the application-only approach.

## Related topics

* Monitor container groups