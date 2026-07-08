---
title: Managed Cluster configuration
source: https://docs.dynatrace.com/managed/managed-cluster/configuration
---

# Managed Cluster configuration

# Managed Cluster configuration

* 2-min read
* Updated on Jun 18, 2026

Configure your Managed Cluster settings for network access, security, user administration, notifications, and operational behavior.

## Cluster settings

[### Cluster properties

Preserve custom configuration changes across upgrades and service restarts.](/managed/managed-cluster/configuration/configure-cluster-properties "Configure properties for Dynatrace Managed with the custom.settings file to preserve custom changes across upgrades and service restarts.")[### Cluster capabilities

Control OneAgent data processing and web UI traffic on individual Managed Cluster nodes.](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.")[### Cluster preferences

Configure proactive support reporting, remote access, privacy, domain name, and community settings.](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences to manage proactive support reporting, remote access, data privacy, domain name, and community settings for your Managed Cluster.")[### Cluster event notifications

Configure notification recipients, emergency contacts, and the Managed Cluster events that trigger email notifications.](/managed/managed-cluster/configuration/configure-cluster-event-notifications "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")

## Access and security

[### Cluster remote access

Configure remote access permissions for Dynatrace product experts.](/managed/managed-cluster/configuration/configure-cluster-remote-access "Configure remote access permissions for your Managed Cluster, including scope options and role assignments for Dynatrace product experts.")[### Manage user sessions

Define concurrent user session limits, terminate active sessions, and configure automatic sign-out.](/managed/managed-cluster/configuration/manage-user-sessions "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[### Password complexity rules

Review password policy defaults, configurable values, and best practices.](/managed/managed-cluster/configuration/password-complexity-rules "Configure password complexity rules for Dynatrace Managed, including minimum length, character categories, default policy values, and best practices.")[### Customize Login page

Customize the sign-in page with system information, legal notices, or administrator contact details.](/managed/managed-cluster/configuration/customize-login-page "Learn how to customize the sign-in page in Dynatrace Managed to display system information, authentication details, legal notices, or an administrator contact.")[### Configure elevated permissions in Dynatrace Managed

Configure sudo, pbrun, or another command for maintenance operations that need elevated permissions.](/managed/managed-cluster/configuration/configure-elevated-permissions "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")

## Network and endpoints

[### Add an SSL certificate to Dynatrace Managed Cluster truststore

Import a custom SSL certificate when the Managed Cluster can't verify SSL connections for email or webhook notifications.](/managed/managed-cluster/configuration/add-ssl-certificate-to-cluster-truststore "Import a custom SSL certificate into the Dynatrace Managed truststore when the Managed Cluster can't verify SSL connections for email or webhook notifications.")[### Configure internet proxy

Configure a proxy connection for your Managed Cluster if you don't have direct internet access.](/managed/managed-cluster/configuration/configure-internet-proxy "Configure a proxy connection for your Managed Cluster if you don't have direct internet access. Supported protocols include Basic and NTLMv1.")[### Configure an SMTP server connection

Configure how your Managed Cluster delivers email to users and administrators.](/managed/managed-cluster/configuration/configure-smtp-server-connection "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.")[### Configure Cluster DNS entries

Create a domain name, set a public endpoint, and add DNS records for each node.](/managed/managed-cluster/configuration/configure-cluster-dns-entries "Configure DNS entries for your Dynatrace Managed deployment by creating a domain name, setting a public endpoint, and adding DNS A records for each node.")[### Set up a load balancer for Dynatrace Managed

Set up an external load balancer for web UI, OneAgent, and RUM/Mobile/Synthetic traffic.](/managed/managed-cluster/configuration/set-up-load-balancer "Learn how to set up an external load balancer in front of your Dynatrace Managed Cluster to handle web UI, OneAgent, and RUM/Mobile/Synthetic traffic.")