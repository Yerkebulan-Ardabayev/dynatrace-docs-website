---
title: Rename a network zone
source: https://docs.dynatrace.com/managed/manage/network-zones/rename-network-zone
scraped: 2026-05-12T11:10:42.650724
---

# Rename a network zone

# Rename a network zone

* How-to guide
* 1-min read
* Published Apr 08, 2020

To rename a network zone, create a new network zone with the new name and move all ActiveGates and OneAgents to the new zone.

Moving ActiveGates from an existing network zone means reduced capacity in that zone. To maintain full capacity at all times and ensure smooth movement, we recommend that you install new ActiveGates for the new network zone so OneAgents can start using the new ActiveGates as they are moved to the new zone.

1. Create a new [name](/managed/manage/network-zones/network-zones-basic-info#naming "Learn how to get started with network zones.") for the network zone.
2. Install ActiveGates for the new network zone.  
   Be sure to specify the network zone installation parameter. See [Customize ActiveGate installation](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") for more information.
3. Change the network zone for every OneAgent in the old zone [via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."). For instructions on cloud deployments, select the appropriate link in the expandable section.

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

1. Restart your OneAgents in the following order.

   1. OS code modules
   2. Technology code modules
   3. Application-only deployments
   4. zRemote code module
2. [Uninstall the ActiveGates](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Learn how to remove ActiveGate from Windows or Linux-based systems.") in the old network zone.
3. Delete the old network zone. Use the [DELETE a network zone](/managed/dynatrace-api/environment-api/network-zones/del-network-zone "Delete a network zone via the Dynatrace API.") API call.

## Related topics

* [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")