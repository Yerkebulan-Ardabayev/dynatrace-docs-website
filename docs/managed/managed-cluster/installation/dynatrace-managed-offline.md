---
title: Install Dynatrace Managed in offline mode
source: https://docs.dynatrace.com/managed/managed-cluster/installation/dynatrace-managed-offline
---

# Install Dynatrace Managed in offline mode

# Install Dynatrace Managed in offline mode

* How-to guide
* 8-min read
* Updated on May 08, 2026

Dynatrace Managed is available in an offline version. In offline mode, Dynatrace Managed uses an offline license that disables all features requiring an internet connection—such as connecting to [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") for license reporting and health checks, or receiving automatic cluster updates.

In offline mode, you're responsible for keeping Dynatrace Managed up to date and reporting license usage to Dynatrace.

## Offline vs. online mode

| Installation step | Online mode | Offline mode |
| --- | --- | --- |
| Installation - license[1](#fn-1-1-def) | license key | license file |
| Installation - Mission Control connection checking | Yes (required) | No (skipped) |
| Installation - License verification with Mission Control[2](#fn-1-2-def) | Yes (required) | License usage must be reported manually via [Export license data](/managed/managed-cluster/operation/export-license-data "Learn how to export license data from the Cluster Management Console.") |
| Installation - OneAgent self-monitoring download and installation | Yes (optional) | No (skipped) |
| Server - updates download (including OneAgent, RUM JavaScript, ActiveGate, NGINX offsets)[3](#fn-1-3-def) | Automatic from Mission Control | Manual from update email |
| Server - certificates handling | Automatic from Mission Control | Only self-signed provided by default |
| Network - ports that are required | [Cluster node ports](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.") | Same as for online except for Mission Control connection and hosted self-monitoring |
| Mission Control - updates | Published updates are automatically synchronized with the Managed Cluster | Published update URLs are sent via email to license contacts |
| Mission Control - health check statistics | Health-check is updated every 5 minutes | No health-check statistics available |
| Mission Control - license updates | License updates are synchronized every 5 minutes with the Managed Cluster | License must be updated manually via Cluster Management Console |
| Mission Control - designates one part of the Premium HA cluster as primary (surviving) | Automatic from Mission Control | Not supported |
| Dynatrace support policy | [3 months](/managed/whats-new/managed "Release notes for Dynatrace Managed") + 1 month with Enterprise Success and Support | [3 months](/managed/whats-new/managed "Release notes for Dynatrace Managed") + 1 month with Enterprise Success and Support |

1

To install in offline mode, pass the license file using the `--license-file <license-filename>` parameter. The activation email includes the full installation command with this parameter and the offline license file attached. The installation log confirms offline mode with `offline mode is active` entries.

2

The server verifies the license after startup (not during installation) through a signature (hash) included in the license file. The installer copies the license file to the server's `config` directory. The `license.file` entry in the server's `config.properties` file contains the path to this file.

3

The Dynatrace Cluster doesn't include installation packages for OneAgent or ActiveGate—in online mode these are downloaded automatically from Mission Control. In offline mode, they must be added manually. Download links are provided in the activation email.

## Install Managed Cluster in offline mode

To install a Managed Cluster in offline mode, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review requirements**](/managed/managed-cluster/installation/dynatrace-managed-offline#review-requirements "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Download files**](/managed/managed-cluster/installation/dynatrace-managed-offline#download-files "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Verify installer**](/managed/managed-cluster/installation/dynatrace-managed-offline#verify-installer "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Retrieve software bill of materials file**](/managed/managed-cluster/installation/dynatrace-managed-offline#retrieve-sbom "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Run installer**](/managed/managed-cluster/installation/dynatrace-managed-offline#install-cluster "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Activate license**](/managed/managed-cluster/installation/dynatrace-managed-offline#activate-license "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Upload agents bundle**](/managed/managed-cluster/installation/dynatrace-managed-offline#upload-agents "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")

### Step 1 Review requirements

Ensure that your system meets the [hardware requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") and [system requirements](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.").

Avoid installing the data stores for Dynatrace Managed components on network or remote disks—this can cause performance and stability issues.

### Step 2 Download files

Download the following files from the activation email and copy them to the directory on your Linux host where you want to install Dynatrace Managed:

* License file (**license.lic**).
* Dynatrace Managed installer (**cluster installer**).
* OneAgent, RUM JavaScript, ActiveGate, and Synthetic installation packages (**agents bundle**).

Activation email example

![managed-activation-email](https://dt-cdn.net/images/managed-activation-email-1075-e07fd3fa2f.png)

managed-activation-email

### Step 3 Verify installer

The Dynatrace Managed installer is digitally signed. Use OpenSSL and the [Dynatrace root certificate﻿](https://ca.dynatrace.com/dt-root.cert.pem) to verify the installer's authenticity. The signature file has the same name as the installer with a `.sig` extension.

1. Download the Dynatrace root certificate and the installer signature file using the links provided in the activation email.
2. Verify the installer file signature using this command:

   ```
   openssl cms -inform PEM -binary -verify -CAfile dt-root.cert.pem -in dynatrace-managed-<version>.sh.sig -content dynatrace-managed-<version>.sh > /dev/null
   ```

   Replace `<version>` with your Dynatrace Managed version.
3. A successful verification returns `Verification successful`. On failure, you see `Verification failure` followed by details.

### Step 4 optional Retrieve software bill of materials file

Follow the instructions in step 3 of the cluster installation guide to [retrieve an SBOM file](/managed/managed-cluster/installation/install-managed-cluster#retrieve-sbom "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.").

### Step 5 Run installer

Follow the instructions in [Run installer](/managed/managed-cluster/installation/install-managed-cluster#run-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") (step 4) and [Finalize setup](/managed/managed-cluster/installation/install-managed-cluster#finalize-setup "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") (step 5) of the cluster installation guide. Use the `--license-file` parameter instead of a license key:

```
sudo /bin/sh dynatrace-managed-<version>.sh --license-file license.lic
```

Replace `<version>` with your Dynatrace Managed version.

### Step 6 Activate license

After the installation, activate your license.

1. Log in to **Cluster Management Console**.
2. Go to **Licensing** and select **Activate license**.

   * If you have internet access, you're redirected to an external registration form ([https://mcsvc.dynatrace.com/register.html﻿](https://mcsvc.dynatrace.com/register.html)) with all fields pre-filled. Verify the details and submit.

     + If you don't have internet access, open `https://mcsvc.dynatrace.com/register.html` in a browser with internet access and complete the form manually.
     + Required: **License key** and **Cluster identifier**
     + Optional: **Installed version** (the current cluster version) and **Cluster admin email address** (an email address through which Dynatrace product experts can contact cluster administrators in case of an emergency)
3. Select **Activate license**. The next page confirms that the license has been activated.
4. On the confirmation page, select **Download license file** to download the `license-activated.lic` file.
5. Select **Go to Licensing page**.
6. On the **Licensing** page, select **More** (**…**) > **Apply license** in the upper-right corner.
7. Select the `license-activated.lic` file you downloaded earlier.

   * After applying the license, the license status changes to **Active**.

### Step 7 Upload agents bundle

To upload the agents bundle to the cluster:

1. Log in to **Cluster Management Console**.
2. Go to **Settings** > **Automatic update**.
3. Select **Upload installation package** to upload it to the cluster.

Alternatively, you can manually copy the agents bundle to the following directory on your Linux machine:

```
/var/opt/dynatrace-managed/agents
```

## Update Managed Cluster in offline mode

Follow the [semi-automatic Managed Cluster update](/managed/managed-cluster/operation/update-cluster#semi-automatic-update "Learn how to update a Managed cluster and how to schedule an automatic update.") instructions in the update guide.

## Frequently asked questions

What can you do if an error occurred while uploading the installation package?

An installation package upload error typically occurs when attempting to upload a full package containing a Managed installer, OneAgent, RUM JavaScript, ActiveGate, and Synthetic. In this case, the package size exceeds the 2 GB upload limit.

1. Log in to **Cluster Management Console**.
2. Go to **Settings** > **Automatic update**.
3. Select **Upload installation package** to upload only selected installation packages to the cluster.

Alternatively, you can manually copy installation packages to the following directories on each cluster node.

* For the cluster to:

  ```
  /opt/dynatrace-managed/installer/upgrade
  ```
* For OneAgent, RUM JavaScript, ActiveGate, and Synthetic to:

  ```
  /var/opt/dynatrace-managed/agents
  ```

What can you do if there is a problem with the license?

If the license file is corrupted, the installation completes and the server starts, but it indicates a problem with the license. In this case, upload a new license in **Cluster Management Console**. For details, see [Update offline license](#update-license).

How do you update the license?

To update your license:

1. Download the `license.lic` file from the activation email.
2. Log in to **Cluster Management Console**.
3. Go to **Licensing** and apply the new license.

How do you obtain diagnostic data for further analysis?

In **Cluster Management Console**, you can download diagnostic data. For details, see [Diagnostic archives](/managed/managed-cluster/operation/diagnostic-archives-for-managed-installations "Learn how you can download a support archive that contains configuration and log files from all installed Dynatrace Managed components of a cluster node.").