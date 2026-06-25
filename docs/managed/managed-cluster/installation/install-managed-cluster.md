---
title: Install a Managed Cluster
source: https://docs.dynatrace.com/managed/managed-cluster/installation/install-managed-cluster
scraped: 2026-05-12T11:06:43.410216
---

# Install a Managed Cluster

# Install a Managed Cluster

* How-to guide
* 7-min read
* Updated on May 08, 2026

To set up a Managed Cluster and install the first node, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review requirements**](/managed/managed-cluster/installation/install-managed-cluster#review-prerequisites "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Download installer**](/managed/managed-cluster/installation/install-managed-cluster#download-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Verify installer**](/managed/managed-cluster/installation/install-managed-cluster#verify-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Retrieve SBOM file**](/managed/managed-cluster/installation/install-managed-cluster#retrieve-sbom "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Run installer**](/managed/managed-cluster/installation/install-managed-cluster#run-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Finalize**](/managed/managed-cluster/installation/install-managed-cluster#finalize "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")

## Step 1 Review requirements

Ensure that your system meets the specified [hardware requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") and [system requirements](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.").

Don't install Dynatrace Managed data stores on network or remote disks. This can cause performance and stability issues.

## Step 2 Download installer

1. Log in to the Linux machine and navigate to the directory where you want to install Dynatrace Managed.
2. Copy the `wget` command line for the installer from the activation email you've received.
3. Paste the `wget` command line for the installer into your terminal window. Wait for the download to complete.

## Step 3 Verify installer

The Dynatrace Managed installer file is digitally signed. In conjunction with OpenSSL and the [Dynatrace root certificateï»¿](https://ca.dynatrace.com/dt-root.cert.pem), the signature file verifies the authenticity of the installer. The signature file has the same name as the installer, with a `.sig` extension.

1. Copy the `wget` command line for the installer file signature from the activation email you've received.
2. Paste the `wget` command line for the installer file signature into your terminal window. Wait for the download to complete.
3. Verify the installer file signature using this command:

   ```
   openssl cms -inform PEM -binary -verify -CAfile dt-root.cert.pem -in dynatrace-managed-<version>.sh.sig -content dynatrace-managed-<version>.sh > /dev/null
   ```

   Replace `<version>` with your Dynatrace Managed version.
4. If verification succeeds, the response should be `Verification successful`. If the verification fails, the response will be `Verification failure` followed by details.

## Step 4 optional Retrieve software bill of materials

Dynatrace provides a [Software Bill of Materials (SBOM)ï»¿](https://www.dynatrace.com/company/trust-center/customers/reports) that includes a detailed inventory of software components and dependencies. You can retrieve the SBOM in CycloneDX format from the installer archive file.

1. You need root rights to extract the Dynatrace Managed installer archive. You can use `su` or `sudo` to run the extraction command. To do this, type one of the following commands into the directory where you downloaded the installation script.

   Replace `<version>` with your Dynatrace Managed version.

   * Ubuntu Server

     ```
     sudo /bin/sh dynatrace-managed-<version>.sh --extract ARCH
     ```
   * Red Hat Enterprise Linux

     ```
     su -c '/bin/sh dynatrace-managed-<version>.sh --extract ARCH'
     ```
   * Other Linux distributions with root session

     ```
     /bin/sh dynatrace-managed-<version>.sh --extract ARCH
     ```
2. The extraction results in an archive file with the file name `dynatrace-managed-<version>.tar.gz`. Unpack the archive file with the following command.

   ```
   tar -xzvf dynatrace-managed-<version>.tar.gz
   ```
3. The `tar` command results in a folder named `dynatrace-managed-<version>`. You can list the files in the folder with the following command.

   ```
   ls -l dynatrace-managed-<version>
   ```
4. The folder contains the SBOM in CycloneDX format with the file name `dynatrace-managed-sbom.cdx.json`.

## Step 5 Run installer

1. You need root rights to install a Managed Cluster. You can use `su` or `sudo` to run the installation script. To do this, type one of the following commands into the directory where you downloaded the installation script.

   Replace `<version>` with your Dynatrace Managed version.

   * Ubuntu Server

     ```
     sudo /bin/sh dynatrace-managed-<version>.sh
     ```
   * Red Hat Enterprise Linux

     ```
     su -c '/bin/sh dynatrace-managed-<version>.sh'
     ```
   * Other Linux distributions with root session

     ```
     /bin/sh dynatrace-managed-<version>.sh
     ```

   To view a list of all available [installation parameters](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates."), run the installer with the parameter `--help`.
2. Type `Accept` to agree to the Dynatrace Managed [Terms of useï»¿](https://www.dynatrace.com/eula/managed/). Installation won't continue until you complete this step. To quit, press `Ctrl+C`.
3. The Managed installer works in interactive mode. It displays prompts for values like installation path and user account. Accept the default values by pressing `Enter`. To override the values, type your choices in the terminal and press `Enter`.

   Have your Dynatrace Managed license key available. You can't complete installation without it.

   #### Default settings

   * Installation path (binaries): `/opt/dynatrace-managed`
   * Dynatrace Server data files: `/var/opt/dynatrace-managed`
   * The system user that runs Dynatrace processes: `dynatrace`
   * The system group that runs Dynatrace processes: `dynatrace`

   #### Bypass interactive mode

   To bypass all questions and install with default settings, run the installer with the `--install-silent` parameter. Be sure to provide your Dynatrace Managed license key as the `--license` parameter value.

   #### What happens during installation

   A Managed Cluster is a set of specialized components that work together to host your monitoring environment and process-monitoring data.

   The installer sets up the following components in the installation directory (by default, `/opt/dynatrace-managed`):

   * Pre-configured Java Runtime Environment (your operating system settings aren't affected by this). Not visible in your `alternatives` options.
   * Cassandra-based Hypercube storage
   * Elasticsearch-based search engine
   * Dynatrace Server
   * An embedded ActiveGate

   The installer also optimizes operating system settings:

   * Swap is turned off (with `swapoff`).  
     Note that enabling swap can result in undesired behavior and so isn't supported.
   * `iptables` "`PREROUTING`" rules are enhanced to enable forwarding of communication to Dynatrace Server (via HTTPS on port 8021). To see the exact rules, type `iptables -L -vt nat` into your terminal.
   * `readahead` page cache is set to 512.
   * Limits for users are changed globally (unlimited locked-in-memory address space, unlimited address space, increased limit for number of processes and open files). See `/etc/security/limits.conf` for details.
   * `max_map_count` is modified.

   The following system files and directories may be modified during installation of Dynatrace Managed:

   * `/etc/hosts`
   * `/etc/sysctl.conf`
   * `/etc/pam.d/su`
   * `/etc/rc.local`
   * `/etc/security/limits.conf`
   * `/etc/security/limits.d/90-nproc.conf`
   * `/etc/sudoers`
   * `/etc/sudoers.d/`
   * `/etc/init.d/`
   * `/etc/init.d/rc*.d/`
   * `/etc/systemd/system/`

   #### Installation logs

   You can find the Dynatrace Managed installation log file in the `/opt/dynatrace-managed/installer/` directory. To identify the right log file, look for the installation date in the file name. For example, the log file of a successful installation performed on September 30th would be `20160930-173309-success-install-of-managed-installer.log`

## Step 6 Finalize

1. Copy the environment address displayed at the end of the installation process. Paste it into your browser to complete the installation. The following page appears.

   ![After server installation](https://dt-cdn.net/images/after-server-installation-425-705dc79015.png)

   After server installation
2. Give your first monitoring environment a name and set up an administrator account. Then select **Next**. You're logged in and redirected to the Cluster Management Console. A default domain is generated, which you should use instead of the IP address for a secure HTTPS connection.
3. Go to **Environments** to view your newly created environment. Select your environment and then **Go to environment** to access the monitoring environment's web user interface (UI). You can later [create additional monitoring environments](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").

## Frequently asked questions

### Use a privilege management system other than sudo

Yes, you can use `pbrun`, but you must grant the Dynatrace user permission to run `/opt/dtrun/dtrun *`. Specify the user who is installing Dynatrace Managed and the command that replaces `sudo`. Note that `<version>` represents the Dynatrace Managed version number.

```
/bin/sh dynatrace-managed-<version>.sh --system-user dynatrace:dynatrace --sudo-cmd  "/usr/bin/pbrun \$CMD"
```

For maintenance purposes, add the following script paths to your privilege management configuration:

* `/opt/dynatrace-managed/uninstall-dynatrace.sh`
* `/opt/dynatrace-managed/launcher/*`
* `/opt/dynatrace-managed/utils/*`

Run this command to stop all Dynatrace Managed processes on a node:

```
pbrun /opt/dynatrace-managed/launcher/dynatrace.sh stop
```

Do not remove or overwrite `dtrun`, as it is required by installation and update procedures. The installer calls `dtrun` without arguments to validate that the user has administrative privileges, but for normal operation Dynatrace calls `dtrun` with arguments to actually run commands.