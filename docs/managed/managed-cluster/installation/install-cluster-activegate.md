---
title: Install a Cluster ActiveGate
source: https://docs.dynatrace.com/managed/managed-cluster/installation/install-cluster-activegate
scraped: 2026-05-12T11:06:45.807451
---

# Install a Cluster ActiveGate

# Install a Cluster ActiveGate

* How-to guide
* 4-min read
* Updated on May 08, 2026

To install a Cluster ActiveGate on Linux or Windows, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review requirements**](/managed/managed-cluster/installation/install-cluster-activegate#review-requirements "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Download installer**](/managed/managed-cluster/installation/install-cluster-activegate#download-installer "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run installer**](/managed/managed-cluster/installation/install-cluster-activegate#run-installer "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Finalize**](/managed/managed-cluster/installation/install-cluster-activegate#finalize "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")

## Step 1 Review requirements

Before you install, decide on the purpose of the ActiveGate and review the corresponding requirements:

* **Route OneAgent traffic**âsee [routing/monitoring requirements](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.").
* **Run Synthetic monitors from a private location**âSynthetic-enabled ActiveGates support a subset of operating systems and have higher [hardware and system requirements](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") than routing ActiveGates.

In most cases, you can install an ActiveGate at any time following OneAgent installation. In some cases, however, the installation order matters, because the OneAgent installer needs to know about your ActiveGate installation before the OneAgent can be installed.

If you've already installed OneAgent

In such instances, first install the ActiveGate and then download the OneAgent installer.
For example, if you download the OneAgent installer and use it to install Dynatrace in a DMZ or network segment that has no internet access and then subsequently install an ActiveGate, youâll need to download and install OneAgent again to ensure that the installer provides the proper configuration between OneAgent and ActiveGate. This is because OneAgent needs to be automatically configured during installation to connect to your monitored environment and send monitoring data back to the Dynatrace Cluster via your ActiveGate.

## Step 2 Download installer

1. Log in to the **Cluster Management Console**.
2. Go to **Home**, select the browse **[â¦]** button, and choose **Add new Cluster ActiveGate**.
3. Select **Windows** or **Linux**, depending on your operating system, and choose a purpose:

   * **Route traffic**âroutes OneAgent, public synthetic, mobile, Real User Monitoring, and REST API traffic.
   * **Run synthetic monitors from a private location**âruns synthetic monitors exclusively. Installing ActiveGate with this purpose disables all other ActiveGate features, including communication with OneAgents.

   The selected purpose automatically sets the corresponding installer parameter (`--enable-synthetic` on Linux, `ENABLE_SYNTHETIC=true` on Windows).
4. Download or copy the installer command for your platform.

   Windows

   Linux

   Select the ActiveGate purpose and select **Download installer** to download it to the target machine.

   Select the ActiveGate purpose, copy the `wget` command from the **Run this command on the target host** field, and paste it into your terminal. Copy the command directly from your Clusterâit contains your cluster's main address.

## Step 3 Run installer

An install parameter (determined by the ActiveGate purpose you selected) is automatically set for the command to run the installer. Make sure you use the command displayed in the Dynatrace web UI that reflects the ActiveGate purpose.

Windows

Linux

Run the installer on the target host. If your purpose is **Run synthetic monitors from a private location**, copy the installation script command from the **Run the installer via Command Prompt** step and paste it into your terminal.

Copy the installation script command from the **Run the installer script with root rights** step and run it in your terminal.

### Customize installation

You can append additional [parameters](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.") to the installation command. For example, to turn off the self-monitoring OneAgent:

```
[root@localhost]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh --install-agent off
```

### FIPS-compliant mode

Linux only

ActiveGate version 1.315+

To install Cluster ActiveGate in FIPS-compliant mode, see [FIPS-compliant mode](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Learn about the command-line parameters that you can use with ActiveGate on Linux.") for prerequisites and setup instructions.

### Default installation settings

For default directories and other defaults, see [ActiveGate default settings for Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux").

## Step 4 Finalize

After the Cluster ActiveGate connects to Dynatrace, installation is complete and Dynatrace reconfigures OneAgent to send monitoring data through the Cluster ActiveGate.

* To verify the installation, select **Show deployment status** and go to the **Dynatrace ActiveGates** tab.
* For troubleshooting, see [Troubleshoot ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").