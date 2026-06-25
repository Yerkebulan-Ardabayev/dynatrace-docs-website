---
title: Deploy network zones (migration)
source: https://docs.dynatrace.com/managed/manage/network-zones/migration/deploy
scraped: 2026-05-12T11:52:30.729913
---

# Deploy network zones (migration)

# Deploy network zones (migration)

* 1-min read
* Published Jan 28, 2020

When your [plan](/managed/manage/network-zones/migration/plan "Find out how to plan network zones that reflect your network topology.") for network zones is ready, it's time to implement them.

## Prerequisites

To proceed with the procedure below, you need:

* Planned network zones with defined names.
* Enough ActiveGates in every network zone to deal with the planned load.

## Procedure

1. Activate the network zones feature in your environment. To learn how, see [Activate network zones](/managed/manage/network-zones/network-zones-basic-info#activate "Learn how to get started with network zones.").
2. Add a network zone to the configuration of every ActiveGate.

   1. Specify the ActiveGate's network zone in the [ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
   2. [Restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
3. Add a network zone to the configuration of every OneAgent. Go zone by zone, editing the configuration of every OneAgent in one network zone before moving on to another This will assure transition without failovers.

   1. Specify the network zone [via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."). For instructions on cloud deployments, select the appropriate link in the expandable section.
      Deploy network zones in a cloud

      #### Kubernetes

      [Deploy OneAgent on Kubernetes](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Install and uninstall OneAgent on Kubernetes using kubectl or Helm.")

      [Deploy OneAgent on Kubernetes via DaemonSet](/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset "Deploy, update, and uninstall OneAgent DaemonSet on Kubernetes.")

      [Deploy OneAgent on Kubernetes for application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")

      #### OpenShift

      [Deploy OneAgent on OpenShift](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy "Install OneAgent on OpenShift using kubectl or Helm.")

      [Deploy OneAgent on OpenShift via DaemonSet](/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset "Deploy, update, and uninstall OneAgent DaemonSet on Kubernetes.")

      [Deploy OneAgent on OpenShift for application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")

      #### Amazon Web Services

      [Deploy OneAgent on AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.")

      [Deploy OneAgent on Elastic Container Service](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Monitor ECS clusters as a daemon service, with the EC2 launch type.")

      [Deploy OneAgent on AWS Elastic Beanstalk](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk "Install OneAgent on AWS Elastic Beanstalk.")

      [Deploy OneAgent on Elastic Kubernetes Service](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Install and uninstall OneAgent on Kubernetes using kubectl or Helm.")

      #### Azure

      [Deploy OneAgent on Azure Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm "Learn how to install and configure OneAgent for monitoring Azure Virtual Machines using a VM extension.")

      [Deploy OneAgent on Azure Kubernetes Service](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Install and uninstall OneAgent on Kubernetes using kubectl or Helm.")

      #### Cloud Foundry

      [Deploy OneAgent on BOSH](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.")

      [Deploy OneAgent on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")

      #### Google Cloud

      [Deploy OneAgent on Google Kubernetes Engine](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Install and uninstall OneAgent on Kubernetes using kubectl or Helm.")

      #### Heroku

      [Deploy OneAgent on Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")
   2. Restart your OneAgents in the following order

      1. Restart the services of OneAgents performing the full-stack monitoring.
      2. Restart OneAgent monitored applications, so that they pick up the new instrumentation.
      3. Restart application-only OneAgent deployments.
      4. Restart zRemote on ActiveGates.