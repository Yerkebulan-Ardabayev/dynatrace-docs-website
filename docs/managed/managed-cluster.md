---
title: "Set up Dynatrace Managed cluster"
source: https://docs.dynatrace.com/managed/managed-cluster
updated: 2026-02-09
---

# Set up Dynatrace Managed cluster

# Set up Dynatrace Managed cluster

* Updated on Dec 09, 2025

In this section, you will learn how to install, configure, and operate a Dynatrace Managed cluster. You will also learn how the [Dynatrace Mission Control team](/managed/managed-cluster/data-privacy/mission-control-proactive-support "Learn about how Mission Control proactive support works.") can support you with proactive assistance.

### Basic concepts

* [Dynatrace Managed components](/managed/managed-cluster/basic-concepts/managed-components "Learn about the high-level architecture of Dynatrace Managed.")
* [Managed deployments](/managed/managed-cluster/basic-concepts/managed-deployments "Find out about your options for deploying Dynatrace Managed.")
* [Managed failover mechanism](/managed/managed-cluster/basic-concepts/managed-failover-mechanism "Read about how cluster failover works and what happens during the switch.")

### Installation

* [Managed hardware requirements](/managed/managed-cluster/installation/dynatrace-managed-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing your Dynatrace Managed cluster.")
* [Managed system requirements](/managed/managed-cluster/installation/managed-system-requirements "Learn what operating system requirements need to be taken into account before installing your Dynatrace Managed cluster.")
* [Cluster node ports](/managed/managed-cluster/installation/which-network-ports-does-dynatrace-server-use "Know which ports are used for inbound and outbound communications in your environment.")
* [Enable or disable SELinux](/managed/managed-cluster/installation/dynatrace-managed-on-selinux "Find out how to configure Dynatrace Managed services to run on a SELinux system.")
* [Managed hardware recommendations for cloud deployments](/managed/managed-cluster/installation/managed-hardware-requirements-for-clouds "Learn what hardware recommendations need to be taken into account before deploying Dynatrace Managed to specific cloud services.")
* [Set up a cluster](/managed/managed-cluster/installation/set-up-a-cluster "Learn how to download and install Dynatrace Managed in order to set up your Dynatrace Managed cluster.")
* [Add a new cluster node](/managed/managed-cluster/installation/add-a-new-cluster-node "Understand the steps required to add a new Dynatrace Managed cluster node.")
* [Customize installation for Dynatrace Managed](/managed/managed-cluster/installation/customize-installation-for-dynatrace-managed "See the complete list of parameters you can use for command line installation of Dynatrace Managed.")
* [Install a Cluster ActiveGate](/managed/managed-cluster/installation/how-to-install-a-cluster-activegate "Download and install a Cluster ActiveGate in a Dynatrace Managed deployment.")
* [Install your own SSL certificate for a cluster node](/managed/managed-cluster/installation/install-your-own-ssl-certificate "Learn how to install your own SSL certificate in case you don't want Dynatrace to create the domain and SSL certificate for you.")
* [Configure SSL certificate for a Cluster ActiveGate](/managed/managed-cluster/installation/install-your-own-ssl-certificate-cluster-ag "Learn how to install your own SSL certificate on a Cluster ActiveGate, in case you don't want Dynatrace to create the domain and SSL certificate for you.")
* [Dynatrace Managed in offline mode](/managed/managed-cluster/installation/dynatrace-offline "Learn how to obtain your license, install, and set up Dynatrace Managed in offline mode.")

### Data privacy

* [Data privacy and exchange in Managed](/managed/managed-cluster/data-privacy/managed-data-privacy-and-exchange "Learn what data is exchanged between your Managed cluster and Mission Control.")
* [Monitored technologies and feature usage](/managed/managed-cluster/data-privacy/monitored-technologies "Learn how Dynatrace sends information about monitored technologies and feature usage.")
* [Mission Control proactive support](/managed/managed-cluster/data-privacy/mission-control-proactive-support "Learn about how Mission Control proactive support works.")

### Configuration

* [Configurable properties of Dynatrace Managed](/managed/managed-cluster/configuration/configurable-properties-of-dynatrace-managed "Learn about the Dynatrace Managed properties that you can configure based on your requirements.")
* [Add an SSL certificate to Dynatrace Managed cluster TrustStore](/managed/managed-cluster/configuration/how-to-add-a-certificate-to-server-trust-store "Learn how to import a custom SSL certificate when a Dynatrace Managed cluster cannot verify SSL connection.")
* [Configure internet proxy for cluster](/managed/managed-cluster/configuration/internet-proxy "Configure a proxy connection for your Managed cluster if you do not have direct internet access.")
* [Configure an SMTP server connection](/managed/managed-cluster/configuration/configure-smtp-server-connection "Learn how to configure an SMTP server connection and why this is recommended.")
* [DNS configuration for Dynatrace Managed](/managed/managed-cluster/configuration/dns-configuration-in-managed "Learn how to configure DNS entries for Dynatrace Managed.")
* [Cluster node capabilities](/managed/managed-cluster/configuration/cluster-node-capabilities "Find out how to enable/disable a cluster node via the Web UI or API call")
* [Cluster remote access](/managed/managed-cluster/configuration/cluster-remote-access "Learn how to grant permission for remote access.")
* [Configure and manage user sessions](/managed/managed-cluster/configuration/configure-manage-user-sessions "Learn how to define the maximum number of concurrent user sessions for Dynatrace Managed.")
* [Password complexity rules](/managed/managed-cluster/configuration/password-complexity-rules "Learn how to configure password complexity rules for Dynatrace Managed.")
* [Sign-in page customization](/managed/managed-cluster/configuration/sign-in-customization "Learn how to customize the sign-in page in Dynatrace Managed.")
* [Cluster preferences settings](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences and privacy settings")
* [Cluster event notifications](/managed/managed-cluster/configuration/cluster-event-notifications "Manage cluster notifications")
* [Configure emergency contacts in Dynatrace Managed](/managed/managed-cluster/configuration/configure-emergency-contacts-managed "Learn how to configure emergency contacts in Dynatrace Managed.")
* [Set up a load balancer for Dynatrace Managed](/managed/managed-cluster/configuration/set-up-load-balancer "Read about how set up a load balancer for your Dynatrace Managed deployment.")
* [Configure elevated permissions in Dynatrace Managed](/managed/managed-cluster/configuration/managed-elevated-permissions "Learn how to configure Dynatrace Managed elevated permissions (sudo, pbrun, dtrun).")

### Operation

* [Migrate a cluster](/managed/managed-cluster/operation/migrate-a-cluster "Learn how to migrate a cluster from one data center to another.")
* [Manage your monitoring environments](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.")
* [Change storage location](/managed/managed-cluster/operation/change-storage-location "Learn how to change the location of datastores defined during the install of Dynatrace Managed.")
* [Apply operating system patches to a node](/managed/managed-cluster/operation/apply-operating-system-patches-to-a-node "Find out how to perform a graceful server shut down and apply OS patches to a node.")
* [Update Dynatrace Managed](/managed/managed-cluster/operation/update-dynatrace-managed "Learn how to schedule automatic updates or perform manual updates of Dynatrace Managed.")
* [Update Cluster ActiveGate](/managed/managed-cluster/operation/update-dynatrace-managed-activegate "Learn about manual and one-click cluster ActiveGate updates.")
* [Backup and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.")
* [Estimate cluster backup size](/managed/managed-cluster/operation/estimating-cluster-backup-size "Learn how to estimate the cluster backup size for metrics storage and Elasticsearch storage.")
* [Reconfigure the IP address of a cluster node](/managed/managed-cluster/operation/ip-reconfiguration "Learn how to reconfigure your node's IP address.")
* [Remove a cluster node](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console.")
* [Remove a cluster](/managed/managed-cluster/operation/remove-a-cluster "Learn how to remove a cluster and release the associated license.")
* [Diagnostic archives for Dynatrace Managed installations](/managed/managed-cluster/operation/diagnostic-archives-for-managed-installations "Learn how you can download a support archive that contains configuration and log files from all installed Dynatrace Managed components of a cluster node.")
* [Start/stop/restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.")
* [Start/stop/restart a cluster](/managed/managed-cluster/operation/start-stop-restart-cluster "Properly shut down and restart Dynatrace Managed deployments containing three or more nodes.")
* [Export license data](/managed/managed-cluster/operation/export-license-data "Learn how to export license data from the Cluster Management Console.")

### API references

* [Cluster API](/managed/managed-cluster/api-references/cluster-api)
* [Mission Control API](/managed/managed-cluster/api-references/mission-control-api "Find out about Mission Control API for managing cluster updates and tokens.")

### Fault domain awareness

* [Premium HA for multi-data centers](/managed/managed-cluster/fault-domain-awareness/premium-high-availability "Read about the concepts behind multi-data center configurations in Managed deployments.")
* [Premium HA - Replicate nodes across DCs](/managed/managed-cluster/fault-domain-awareness/replicate-nodes-across-dcs "Understand the steps required to mirror your cluster nodes across two data centers.")
* [Premium HA - Rebuild data center](/managed/managed-cluster/fault-domain-awareness/rebuild-data-center "Learn how to rebuild data center in a multiple data center deployment.")
* [Premium HA multi-datacenter failover](/managed/managed-cluster/fault-domain-awareness/auto-repair)
* [Premium HA - Data center disaster recovery from backup](/managed/managed-cluster/fault-domain-awareness/data-center-disaster-recovery-from-backup "Learn how to recover lost data center from backup in a multiple data center deployment.")
* [Premium HA - Data center disaster recovery from data center](/managed/managed-cluster/fault-domain-awareness/data-center-disaster-recovery-from-data-center "Understand the steps required to spread your cluster to two data centers.")
* [Rack aware managed deployment](/managed/managed-cluster/fault-domain-awareness/rack-awareness "Understand the steps required to create a rack aware Dynatrace Managed deployment")
* [Rack aware conversion using replication](/managed/managed-cluster/fault-domain-awareness/rack-aware-conversion-using-replication "Learn how to download and convert Dynatrace Managed cluster to rack aware using the expansion method.")
* [Rack aware conversion using restore](/managed/managed-cluster/fault-domain-awareness/rack-aware-conversion-using-restore "Learn how to download and convert a Dynatrace Managed cluster to rack aware using the restore method.")

### Self-monitoring

* [Local self-monitoring environment](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.")
* [Hosted self-monitoring environment](/managed/managed-cluster/self-monitoring/hosted-self-monitoring "Learn how to use hosted self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.")
* [Private self-monitoring environment](/managed/managed-cluster/self-monitoring/private-self-monitoring "Learn how to set up and configure a private self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.")
