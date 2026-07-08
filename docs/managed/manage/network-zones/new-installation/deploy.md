---
title: Deploy network zones (new installation)
source: https://docs.dynatrace.com/managed/manage/network-zones/new-installation/deploy
---

# Deploy network zones (new installation)

# Deploy network zones (new installation)

* 1-min read
* Published Jan 28, 2020

When your [plan](/managed/manage/network-zones/new-installation/plan "Plan network zones that reflect your network topology.") for network zones is ready, it's time to implement them.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install ActiveGates**](/managed/manage/network-zones/new-installation/deploy#install-activegates "Find out how to deploy network zones for an existing Dynatrace environment.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Install OneAgents**](/managed/manage/network-zones/new-installation/deploy#install-oneagents "Find out how to deploy network zones for an existing Dynatrace environment.")

## Prerequisites

To proceed with the procedure below, you need:

* Planned network zones with defined names.
* Activated network zones feature. To learn how to activate it, see [Activate network zones](/managed/manage/network-zones/network-zones-basic-info#activate "Learn how to get started with network zones.").

## Step 1 Install ActiveGates

1. Zone by zone, install the ActiveGates responsible for message routing.
2. During installation, use the `--set-network-zone=<name>` installation parameter to specify the network zone. For more on how to customize your ActiveGate installation, see [ActiveGate installation information](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").
3. In the demilitarized zone, install ActiveGates for RUM with [`MSGrouter` parameter](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collector "Learn which ActiveGate properties you can configure based on your needs and requirements.") set to `false`.

   You can also specify the network zone after installation of an ActiveGate
4. Specify the network zone in the [ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") of the ActiveGate.
5. [Restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

## Step 2 Install OneAgents

Zone by zone, install your OneAgents. Be sure to specify the network zone installation parameter. See [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") for more information.

For instructions on cloud deployments, select the appropriate link in the expandable section.

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

## Setting up z/OS monitoring

1. Set up [zLocal](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.").
2. Set up [zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.").
3. Add a network zone to the configuration of the ActiveGate that runs zRemote.

   1. Specify that Activate's network zone in the [ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
   2. [Restart](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") the ActiveGate.
4. Connect zLocal with zRemote.