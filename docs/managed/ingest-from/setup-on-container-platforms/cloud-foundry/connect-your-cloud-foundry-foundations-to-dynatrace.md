---
title: Connect your Cloud Foundry foundations with Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace
---

# Connect your Cloud Foundry foundations with Dynatrace

# Connect your Cloud Foundry foundations with Dynatrace

* 4-min read
* Updated on Apr 07, 2026

Connecting your Cloud Foundry foundations to Dynatrace enables

* full access to the dedicated [Cloud Foundry overview page](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics "Available metrics for monitoring your Cloud Foundry clusters with Dynatrace")
* automatic detection of your Cloud Foundry organizations
* access to other Cloud Foundry process properties, like **space**, **space ID**, **application**, **application ID**, and **instance index**.

To connect your foundation with Dynatrace, follow the instructions below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Start installation**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#start-installation "Enable monitoring on your Cloud Foundry foundations.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Download the installer**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#download-installer "Enable monitoring on your Cloud Foundry foundations.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run the installer**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#run-installer "Enable monitoring on your Cloud Foundry foundations.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Certificate management**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#certificate "Enable monitoring on your Cloud Foundry foundations.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Connect your foundation to Dynatrace**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#connect-foundation "Enable monitoring on your Cloud Foundry foundations.")

## Prerequisites

* Review the list of [supported applications and versions](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Diego cells include the [OneAgent BOSH add-on](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.").

## Step 1 Start installation

1. Sign in to Dynatrace.

2. Go to **Deploy Dynatrace**.
3. Select **Install ActiveGate**.

For more information, see [Installation](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

## Step 2 Download the installer

How you download your installer depends on your setup and needs. You can choose to download an installer directly to the server where you plan to install an ActiveGate or you can download an installer to a different machine and then transfer the installer to the server.

1. Select [Route OneAgent traffic](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.") as the [ActiveGate purpose](/managed/ingest-from/dynatrace-activegate#purposes "Understand the basic concepts related to ActiveGate.").
2. Select **Download installer**. There are two options:

   * Download via shell command. Copy and run the `wget` command.
   * Select the link to download the ActiveGate installer.

## Step 3 Run the installer

An install parameter (determined by the ActiveGate purpose you selected) is automatically set for the command to run the installer. Make sure you use the command displayed in the Dynatrace web UI that reflects the ActiveGate purpose.

Copy the installation script command from the **Run the installer with root rights** step and paste it into your terminal.

### Customize installation

You can add additional [parameters](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") to the installation command to customize your installation. For example, to install ActiveGate in a different directory, use the `INSTALL=<path>` parameter:

```
[root@host]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh INSTALL=/hosted_app/dynatrace
```

### Default installation settings

For installation defaults, including default directories, see [ActiveGate default settings for Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux").

## Step 4 Certificate management

If you're using self-signed certificates for communication to external APIs, you can either add the certificate to the truststore or disable certificate validation.

### Add the certificate to the truststore

1. Bring in the certificate from your cloud provider.  
   In the following example, we extract the certificate from `google.com` and save it locally as `dt_k8s_api.pem`. The command is the same for Windows and Linux, assuming you have `openssl` installed on Windows.

   ```
   echo Q | openssl s_client -connect google.com:443 | openssl x509 -outform PEM > dt_k8s_api.pem
   ```

   For Kubernetes, you can use the following command sequence to get the certificate:

   ```
   [root@host]# API_ENDPOINT_URL=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')



   [root@host]# if [[ $API_ENDPOINT_URL =~ (https?://.*):(\d*) ]]; then API_SERVER_PORT=$API_ENDPOINT_URL; else API_SERVER_PORT="$(echo $API_ENDPOINT_URL | sed -e "s/https:\/\///"):443"; fi



   [root@host]# echo -e "${YLW} API server:${NC} ${API_SERVER_PORT}"



   [root@host]# echo Q | openssl s_client -connect $API_SERVER_PORT 2>/dev/null | openssl x509 -outform PEM > dt_k8s_api.pem
   ```
2. Add the certificate to the keystore.  
   You can provide a full path to the `pem` file location (including paths to remote locations) using the `-file` parameter, or copy the `pem` file to your ActiveGate and provide only the filename as indicated in the example.

   ```
   [root@host]# sudo /opt/dynatrace/gateway/jre/bin/keytool -import -file dt_k8s_api.pem -alias dt_k8s_api -keystore /var/lib/dynatrace/gateway/ssl/mytrusted.jks
   ```

   If you import multiple certificates, make sure that you provide a unique alias for each certificate that you import. If you use the same alias for each certificate, all previously used certificates will be overwritten.

   You can display the list of aliases and the certificate description using the `keytool -list` command.

   For example:

   ```
   # sudo /opt/dynatrace/gateway/jre/bin/keytool -list -keystore /var/lib/dynatrace/gateway/ssl/mytrusted.jks



   Enter keystore password:



   Keystore type: JKS



   Keystore provider: SUN



   Your keystore contains 1 entry



   dt_k8s_api, Apr 26, 2020,



   trustedCertEntry,



   Certificate fingerprint (SHA-256): 07:28:9A:F2:29:32:0D:64:F0:18:93:A1:CC:2E:49:21:E9:DA:40:82:9B:A8:71:B7:A4:2C:6D:8C:B3:90:31:31
   ```
3. Add the following entries in the `/var/lib/dynatrace/gateway/config/custom.properties` file.

   The entry in the `custom.properties` file may look like this:

   ```
   [collector]



   trustedstore = mytrusted.jks



   # the following entries are optional



   trustedstore-password = changeit



   trustedstore-type = JKS
   ```

   Encrypted password

   The password will be stripped and encrypted when you restart the ActiveGate service.
4. [Restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Alternatively, you can add the truststore file containing the Kubernetes CA certificate as an installation parameter. For details, see [Trusted root certificates for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections.").

### Disable certificate validation

Disabling certificate validation isn't recommended because it imposes security risks. However, if you still want to disable certificate validation for test environments, you need to do the following:

1. Go to [Kubernetes overview page](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes#kubernetes-page "Monitor the health and utilization of your Kubernetes/OpenShift cluster resources."), look for your cluster and select **…** > **Settings** in the cluster row to edit its settings.
2. Disable **Require valid certificates for communication with API server**.
3. Disable **Verify hostname in certificate against Kubernetes API URL**.
4. Select **Save** to save your changes.
   These settings override the settings in the ActiveGate `custom.properties` file.

## Step 5 Connect your foundation to Dynatrace

We recommend using a [Cloud Foundry admin read-only account﻿](https://docs.cloudfoundry.org/uaa/uaa-user-management.html#admin-read-only) that can view almost all Cloud Controller API resources, but can't modify them.

```
uaac user add ReadOnlyUser -p SecretPassword --emails something@example.com



uaac member add cloud_controller.admin_read_only ReadOnlyUser



uaac member add scim.read ReadOnlyUser
```

To connect your Cloud Foundry foundation to Dynatrace

1. Go to ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") **Hub**, search for **Cloud Foundry** and select **Set up** to add the extension to your environment.
2. Add a new monitoring endpoint.

   Enter your Cloud Foundry **API target URL**, your **Authentication endpoint**, your **Cloud Foundry Username**, and your **Password**.
3. Optional Select the ActiveGate group.

   For more information about ActiveGate groups, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").
4. Optional Test your connection.
5. Select **Save changes**.

## Manage permissions and configuration

* For fine-grained user permissions, see [IAM policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").
* For easy configuration, use [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

The schemaID for Cloud Foundry is `builtin:cloud.cloudfoundry`.

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")
* [Set up Dynatrace on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")