---
title: Delete a network zone
source: https://docs.dynatrace.com/managed/manage/network-zones/delete-network-zones
---

# Delete a network zone

# Delete a network zone

* How-to guide
* 1-min read
* Published Apr 14, 2020

To delete a network zone, first make sure no OneAgent or ActiveGate is using that zone. You can only delete an empty network zone. If the network zone is used as an alternative zone for any OneAgent, it will be automatically removed from the list of possible alternatives.

Follow these steps:

1. Identify the OneAgents in the zone to be deleted.
2. Identify a different zone to put these OneAgents in.
3. Check whether the ActiveGates in the target zone have enough capacity to add these OneAgents. If needed, install additional ActiveGates.
4. Change the network zone for every OneAgent in the zone to be deleted [via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."). For instructions on cloud deployments, select the appropriate link in the expandable section.

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
5. [Uninstall the ActiveGates](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Learn how to remove ActiveGate from Windows or Linux-based systems.") responsible for message routing in the network zone to be deleted.  
   Alternatively, you can re-assign these ActiveGates to other network zones. Change the network zone in the [ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") and [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
6. Delete the network zone. Use the [DELETE a network zone](/managed/dynatrace-api/environment-api/network-zones/del-network-zone "Delete a network zone via the Dynatrace API.") API call.

## Related topics

* [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")