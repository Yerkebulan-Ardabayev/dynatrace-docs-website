---
title: Create a private Synthetic location
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location
scraped: 2026-02-17T21:18:02.865628
---

# Create a private Synthetic location

# Create a private Synthetic location

* How-to guide
* 24-min read
* Updated on Jan 12, 2026

You can run your Dynatrace synthetic monitors from a private Synthetic location, which is a location in your private network infrastructure where you install one or more Synthetic-enabled ActiveGate instances.

With monitors executed from a private location, you can bring the testing capabilities available in public locations right into your own environment. With private locations you can:

* Measure internal webpage performance and availability.
* Measure complex internal applications with browser clickpaths.
* Measure external resources with synthetic monitors run from internal locations.
* Monitor APIs, both internal and external.

Private Synthetic locations support all [types of Dynatrace synthetic monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.").

## System and hardware requirements for private locations

Make sure the target host you plan to use for running synthetic monitors complies with [system and hardware requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"). Note that Synthetic-enabled ActiveGates have more demanding hardware and system requirements than a regular Environment or Cluster ActiveGate.

Synthetic-enabled ActiveGate installed on Ubuntu 20.04 LTS and 22.04 LTS only You can use [`TEMP`](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#temporary "Learn about the command-line parameters that you can use with ActiveGate on Linux.") to customize the [default temporary directory for private Synthetic files](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories--linux "Find out where ActiveGate files are stored on Windows and Linux systems.")â`/var/tmp/dynatrace/synthetic`. However, the path must begin with `/var/tmp`, for example, `TEMP=/var/tmp/syn`. Dynatrace requires write access to `/var/tmp` for the installation of Chromium snap packages.

End-of-support information

* There are no new versions of Chromium for Red Hat/Oracle Linux/Rocky Linux 8 beyond version 133.
  For important security and stability reasons, we've decided to discontinue our support for installing **Synthetic-enabled** ActiveGate on Red Hat/Oracle Linux/Rocky Linux 8 after ActiveGate version 1.325.
  ActiveGate version 1.325 is **the last Synthetic-enabled** ActiveGate supported on Red Hat/Oracle Linux/Rocky Linux 8.
  Additionally, with Dynatrace version 1.326, we plan to introduce mechanisms preventing Synthetic-enabled ActiveGates on Red Hat/Oracle Linux/Rocky Linux 8 from being updated beyond version 1.325.
* Chromium development for Amazon Linux 2 stopped at version 126.
  For important security and stability reasons, we've decided to discontinue our support for installing Synthetic-enabled ActiveGate on Amazon Linux 2 after ActiveGate version 1.307.
  ActiveGate version 1.307 is the last Synthetic-enabled ActiveGate to support Amazon Linux 2.
  Additionally, with Dynatrace version 1.308, we have introduced mechanisms preventing Synthetic-enabled ActiveGates on Amazon Linux 2 from being updated beyond version 1.307.
* Chromium development for Red Hat/CentOS 7 stopped at version 126.
  For important security and stability reasons, we've decided to discontinue our support for installing Synthetic-enabled ActiveGate on Red Hat/CentOS 7 after ActiveGate version 1.305.
  ActiveGate version 1.305 is the last Synthetic-enabled ActiveGate to support Red Hat/CentOS 7.
  Additionally, with Dynatrace version 1.306, we have introduced mechanisms preventing Synthetic-enabled ActiveGates on Red Hat/CentOS 7 from being updated beyond version 1.305.

  + Since Red Hat Enterprise Linux 7 reached [End of Maintenanceï»¿](https://dt-url.net/af03uea) support on June 30, 2024, all of its packages have been archived. This means that it may not be possible to find the required dependencies for update. For more details, see the [Red Hat Enterprise Linux 7 statusï»¿](https://dt-url.net/e623zr1)

### Before you begin

* You cannot execute synthetic monitors using an Environment ActiveGate configured for [multi-environment support](/docs/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.").
* You can create a private location using a clean-installed Synthetic-enabled Environment ActiveGate version 1.169+ or Cluster ActiveGate with Dynatrace Managed version 1.176+. If you want to use an existing ActiveGate host, [uninstall ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Learn how to remove ActiveGate from Windows or Linux-based systems.") first.
* Synthetic-enabled ActiveGate is used exclusively to run synthetic monitors. A clean ActiveGate installation for the purpose of synthetic monitoring disables all other ActiveGate features, including communication with OneAgents.
* Make sure that the ActiveGate can connect to other [Dynatrace components](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") as well as the resource you want to test. See [Set up a proxy for private synthetic monitoring](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.").
* Only **IPv4** and **DNS UDP** are supported for network configuration.
* Synthetic-enabled ActiveGate needs access to the **Amazon S3** service to upload and access browser monitor screenshots from private locations. Ensure that your firewall configuration allows connections to `*.s3-accelerate.amazonaws.com` on port `443`. You can also [set up your proxy](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.") to connect to the Amazon S3 service. (Screenshots are stored in a different folder for each monitoring environment, but the S3 Bucket is the same (`ruxit-synth-screencap`). Data is encrypted by [Amazon S3-managed keyï»¿](https://dt-url.net/4a02xvx).)
* Both manual and automatic Chromium updates require access to `https://synthetic-packages.s3.amazonaws.com`. For security reasons, public access to the S3 bucket is enabled only for specific files; trying anything else will result in a 403 error.

## Install a Synthetic-enabled ActiveGate

Install an ActiveGate in latest Dynatrace

The instructions below describe how to install an ActiveGate in the previous Dynatrace. To learn how to install an ActiveGate in the latest Dynatrace, see [Private synthetic locations on Grail](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#create-a-private-location "Learn how to manage private locations in the Synthetic app.").

Synthetic-enabled ActiveGate is used exclusively to run synthetic monitors. A clean ActiveGate installation for the purpose of synthetic monitoring disables all other ActiveGate features, including communication with OneAgents. Make sure the host on which you install the ActiveGate has access to the internet.

Manual installation

If this web UI-guided installation fails, or you prefer to prepare the host for the Synthetic engine yourself, you can [manually install Chromium and other dependencies via S3](#manual). You can also [install Chromium from a custom, local repository](#custom-repo).

1. For Environment ActiveGate, in Dynatrace Hub, select **ActiveGate** > **Set up**.

   For Cluster ActiveGate, go to the Dynatrace Cluster Management Console and select **More** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Add new Cluster ActiveGate**.
2. Select the operating system to view instructions.
3. Create a [**PaaS Token**](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") or enter an existing token. This token has the **Download OneAgent and ActiveGate installers** `InstallerDownload` token scope, which allows you to download the ActiveGate installer. Once provided, the token is automatically appended to download and installation commands, which are then displayed in the UI.

   You can find existing tokens listed on the **Access tokens** page. Note that a PaaS token is only displayed once upon creation, after which it's stored encrypted and cannot be revealed. We recommend that you store a PaaS token after creation in a password manager so that you can reuse it as needed.
4. Linux only For **Choose installer type**, keep the default selection: `x86/64`.
5. For **What's the purpose of this ActiveGate**, select **Run synthetic monitors from a private location**.
6. Optional Assign the ActiveGate to a private Synthetic locationâselect a location from the dropdown list. You can also [assign the ActiveGate to a location](#add) after installation.
7. Optional You can turn off support for browser monitors. If you do so, the Synthetic ActiveGate will be treated as [browserless](#browserless).

   ![Disabling support for browser monitors](https://dt-cdn.net/images/browserless-deploy-415-1d20a6159c.png)
8. Optional **Set customized options** to assign the ActiveGate to a [**Network zone**](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") and [**ActiveGate group**](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").
9. Download the installer to the target host.
10. Linux only Recommended **Verify signature**ârun the displayed command on the target host to download a certificate file and verify the installer.
11. Linux only Select a Linux distribution.
12. Run the installer and any other commandsâmake sure you use the exact commands displayed in the UI.

    Linux only The installer automatically downloads Chromium and the dependencies required by the Synthetic engine. On Red Hat, Oracle Linux, and Rocky Linux you also need to enable repositories from which the installer downloads the dependencies. As a prerequisite for enabling proprietary repositories on Red Hat, you need to register your Red Hat instance. The web UI provides you with all the required commands for doing so, as shown in the example below.

    ![Commands to install ActiveGate on Red Hat 9](https://dt-cdn.net/images/synth-ag-commands-red-hat-9-2025-11-17-723-eef29810b5.png)
13. Verify the ActiveGate installation (**Show deployment status**).

## Add a private location

Add a private location in latest Dynatrace

The instructions below describe how to add a private location in previous Dynatrace. To learn how to add a private location in latest Dynatrace, see [Private synthetic locations on Grail](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#create-a-private-location "Learn how to manage private locations in the Synthetic app.").

1. Search for and select **Settings**. Then select **Web & mobile monitoring** > **Private synthetic locations**.
2. Select **Create location**.
3. Give your location a custom **Name**, for example `Boston office, 3rd floor`.
4. Map it from an existing geographic location or add a custom geographic location defined by **Country**, **Region**, **City**, and **Geographic coordinates**.
5. Add a Synthetic-enabled ActiveGate to the location. Note that an ActiveGate can only be assigned to a single location.

   You can also leave the location temporarily unassigned and assign it during the [ActiveGate installation process](#install).
6. Select **Add**.
7. Select **Save**.

## Create a synthetic monitor

Now, when you create your HTTP or browser monitor, select the location you've just created from the list of all available locations. For more information, see [Create an HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site."), [Create a single-URL browser monitor](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site."), or [Record a browser clickpath](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.").

## Linux only Install Chromium and dependencies manually from S3

This section is not relevant for Browserless locations.

Amazon Linux 2023, Ubuntu 24, and Oracle Linux 9

Amazon Linux 2023, Ubuntu 24, and Oracle Linux 9 use Chrome for Testing instead of Chromium. For manual installation of Chrome for Testing on these operating systems, see [Amazon Linux 2023, Ubuntu 24, and Oracle Linux 9 (Chrome for Testing)](#chrome-for-testing).

If the [web UI-guided installation](#install) fails or you prefer to prepare the host for the Synthetic engine yourself, you can install Chromium and other dependencies using the procedure below. Ensure that you can connect to `https://synthetic-packages.s3.amazonaws.com` to access Chromium and dependencies. For security reasons, public access to the S3 bucket is enabled only for specific files; trying anything else will result in a 403 error.

Also see [Install Chromium from a custom repository](#custom-repo) below.

See [how to update Chromium manually](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#chromium-manual "Analyze and manage capacity usage at your private Synthetic locations.") in [Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations."). We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and Chromium versions updatedâDynatrace supports Chromium versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#chromium-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for a specific ActiveGate release.

### Ubuntu Server

1. Install Synthetic engine dependencies:

   Ubuntu 20.04 and 22.04

   Synthetic engine dependencies:

   ```
   sudo apt-get update && sudo apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable libnss3-tools auditd
   ```

   Chromium dependencies:

   ```
   sudo apt-get -y install fonts-dejavu-core
   ```

   ```
   sudo snap install gnome-3-38-2004 gtk-common-themes
   ```
2. Download and install Chromium.

   * Download the snap (Ubuntu 20.04 and 22.04) package archive. This is a safe and verified archive hosted by Dynatrace.

     ActiveGate version 1.329

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-142.0.7444.175-3313.tgz
     ```

     ActiveGate version 1.327

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-141.0.7390.122-3285.tgz
     ```

     ActiveGate version 1.325

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-140.0.7339.185-3251.tgz
     ```

     ActiveGate version 1.323

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-139.0.7258.138-3235.tgz
     ```

     ActiveGate version 1.321

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.157-3203.tgz
     ```

     ActiveGate version 1.319

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.100-3199.tgz
     ```

     ActiveGate version 1.317

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-137.0.7151.103-3169.tgz
     ```

     ActiveGate version 1.315

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-136.0.7103.59-3121.tgz
     ```

     ActiveGate version 1.313

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-135.0.7049.95-3110.tgz
     ```

     ActiveGate version 1.311

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-134.0.6998.35-3060.tgz
     ```

     ActiveGate version 1.309

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-132.0.6834.159-3036.tgz
     ```

     ActiveGate version 1.307

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-131.0.6778.85-3002.tgz
     ```

     ActiveGate version 1.305

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-130.0.6723.69-2985.tgz
     ```

     ActiveGate version 1.303

     ##### Ubuntu 20.04 and 22.04

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-129.0.6668.89-2965.tgz
     ```

     You can [verify the authenticity of the packages](#verify) using the signature files stored together with the package archives.
   * Extract the installation packages. Go to the directory where you saved the archive and run the following command:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     This creates a `/tmp/chromium` directory and extracts the packages into it.
   * Install the extracted packages.

     Ubuntu 20.04 and 22.04

     ```
     sudo chown -R root:root /tmp/snap-private-tmp
     ```

     ```
     sudo snap ack /tmp/chromium/chromium.assert
     ```

     ```
     sudo snap install --devmode /tmp/chromium/chromium.snap
     ```

     Substitute `dtuserag` with the names of the ActiveGate service user and group if they differ from the default values.

     ```
     sudo chown -R dtuserag:dtuserag /tmp/snap-private-tmp
     ```

     This installs all the packages extracted to the `/tmp/chromium/` directory. You can delete the `/tmp/chromium/` directory and the downloaded `chromium.tgz` archive after successful Chromium installation.
3. After you satisfy the dependencies, run the ActiveGate installer with root rights with the `--enable-synthetic` parameter set to `manual`. For example:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

### Red Hat Enterprise Linux, Oracle Linux, and Rocky Linux

* Chromium development for Red Hat/CentOS 7 and Amazon Linux 2 stopped at version 126.

  + Since Red Hat Enterprise Linux 7 reached [End of Maintenanceï»¿](https://dt-url.net/af03uea) support on June 30, 2024, all of its packages have been archived. This means that it may not be possible to find the required dependencies for update. For more details, see the [Red Hat Enterprise Linux 7 statusï»¿](https://dt-url.net/e623zr1)
* Chromium installation when a proxy is required for internet access.

  + If you need to download and install Chromium, and your system requires a proxy for internet access, you should configure `curl`to use the correct proxy. Specify your proxy and port details by running the commands as in this example:

    ```
    vi /root/.curlrc



    proxy=http://proxy.example.com:8080
    ```

1. Set up repositories and install dependencies.

   Red Hat 7

   Red Hat 8

   Red Hat 9

   CentOS

   Oracle Linux 8

   Amazon Linux 2

   Rocky Linux 8

   Rocky Linux 9

   Deprecated operating system

   ActiveGate version 1.305 is the last Synthetic-enabled ActiveGate to support Red Hat 7.

   * Register the Red Hat instance.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Enable the Red Hat `Extras` and `Optional` repositories as well as `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-7-server-extras-rpms



     sudo subscription-manager repos --enable rhel-7-server-optional-rpms



     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Deprecated operating system

   ActiveGate version 1.325 is the last Synthetic-enabled ActiveGate to support Red Hat 8.

   * Register the Red Hat instance.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Enable the Red Hat `Extras` and `Optional` repositories as well as `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo subscription-manager repos --enable rhel-8-for-x86_64-baseos-rpms



     sudo subscription-manager repos --enable rhel-8-for-x86_64-appstream-rpms



     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Register the Red Hat instance.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Enable the Red Hat `Extras` and `Optional` repositories as well as `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo subscription-manager repos --enable rhel-9-for-x86_64-baseos-rpms



     sudo subscription-manager repos --enable rhel-9-for-x86_64-appstream-rpms



     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Deprecated operating system

   ActiveGate version 1.305 is the last Synthetic-enabled ActiveGate to support CentOS.

   * Enable `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo yum install epel-release
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Deprecated operating system

   ActiveGate version 1.325 is the last Synthetic-enabled ActiveGate to support Oracle Linux 8.

   * Enable `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo yum install -y oracle-epel-release-el8
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Deprecated operating system

   ActiveGate version 1.307 is the last Synthetic-enabled ActiveGate to support Amazon Linux 2.

   * Enable `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo amazon-linux-extras install epel
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Deprecated operating system

   ActiveGate version 1.325 is the last Synthetic-enabled ActiveGate to support Rocky Linux 8.

   * Enable `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo yum install epel-release
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Enable `EPEL` (Extra Packages for Enterprise Linux ).

     ```
     sudo yum install epel-release
     ```
   * Install Synthetic engine dependencies.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```
2. Download and install Chromium.

   * Download the rpm package archive. This is a safe and verified archive hosted by Dynatrace.

     ActiveGate version 1.329

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-142.0.7444.175-2.el9.tgz
     ```

     ActiveGate version 1.327

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-141.0.7390.122-1.el9.tgz
     ```

     ActiveGate version 1.325

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-140.0.7339.185-1.el9.tgz
     ```

     ActiveGate version 1.323

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-139.0.7258.138-1.el9.tgz
     ```

     ActiveGate version 1.321

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.157-1.el9.tgz
     ```

     ActiveGate version 1.319

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.100-1.el9.tgz
     ```

     ActiveGate version 1.317

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-137.0.7151.103-1.el9.tgz
     ```

     ActiveGate version 1.315

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-136.0.7103.59-1.el9.tgz
     ```

     ActiveGate version 1.313

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-135.0.7049.95-1.el9.tgz
     ```

     ActiveGate version 1.311

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-134.0.6998.35-1.el9.tgz
     ```

     ActiveGate version 1.309

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-132.0.6834.159-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-132.0.6834.159-1.el9.tgz
     ```

     ActiveGate version 1.307

     ##### Amazon Linux 2

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz
     ```

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-131.0.6778.204-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-131.0.6778.204-1.el9.tgz
     ```

     ActiveGate version 1.305

     ##### Red Hat Enterprise Linux/CentOS 7, Amazon Linux 2

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz
     ```

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-130.0.6723.69-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-130.0.6723.116-1.el9.tgz
     ```

     ActiveGate version 1.303

     ##### Red Hat Enterprise Linux/CentOS 7, Amazon Linux 2

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz
     ```

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-129.0.6668.89-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     Requires Chromium 130, previous version `129.0.6668.89-1.el9` cannot be installed anymore, please refer to [troubleshooting guideï»¿](https://dt-url.net/x303x5f) for details.

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-130.0.6723.116-1.el9.tgz
     ```

     You can [verify the authenticity of the packages](#verify) using the signature files stored together with the package archives.
   * Extract the installation packages. Go to the directory where you saved the archive and run the following command:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     This creates a `/tmp/chromium` directory and extract the packages into it.
   * Install extracted packages.

     ```
     sudo yum install -y /tmp/chromium/*.rpm
     ```

     This installs all the packages extracted to the `/tmp/chromium/` directory. You can delete the `/tmp/chromium/` directory and the downloaded `chromium.tgz` archive after successful Chromium installation.
3. Disable automatic update of Chromium packages:

   ```
   sudo yum -y install yum-plugin-versionlock



   sudo yum versionlock chromium



   sudo yum versionlock chromium-common
   ```
4. Optional Install non-Latin TrueType fonts:

   ```
   sudo yum install dejavu-fonts-common.noarch dejavu-sans-fonts.noarch
   ```
5. After you satisfy the dependencies, run the ActiveGate installer with root rights with the `--enable-synthetic` parameter set to `manual`. For example:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

### Amazon Linux 2023, Ubuntu 24, and Oracle Linux 9 (Chrome for Testing)

Unlike Chromium on other distributions, Chrome for Testing updates do not use package managers. You manually manage the Chrome binaries while dependencies are managed by the system package manager.

See [how to update Chrome for Testing manually](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#chromium-manual "Analyze and manage capacity usage at your private Synthetic locations.") in [Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations."). We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and Chrome for Testing versions updatedâDynatrace supports Chrome for Testing versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#chromium-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for a specific ActiveGate release.

1. Set up repositories and install dependencies.

   Ubuntu 24

   Amazon Linux 2023

   Oracle Linux 9

   * Install Synthetic engine dependencies:

     ```
     sudo apt-get update && sudo apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable libnss3-tools auditd unzip
     ```
   * Install Chrome for Testing dependencies:

     ```
     sudo apt-get -y install libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libcairo2 libcups2t64 libgbm1 libnspr4 libnss3 libpango-1.0-0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2
     ```

   * Enable `EPEL` (Extra Packages for Enterprise Linux):

     ```
     sudo yum install -y epel-release
     ```
   * Install Synthetic engine dependencies:

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools unzip
     ```
   * Install Chrome for Testing dependencies:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs dbus-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```

   * Enable `EPEL` (Extra Packages for Enterprise Linux):

     ```
     sudo yum install -y oracle-epel-release-el9
     ```
   * Install Synthetic engine dependencies:

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools unzip
     ```
   * Install Chrome for Testing dependencies:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```
2. Download and set up Chrome for Testing.

   * Create the Chrome for Testing directory:

     ```
     sudo mkdir -p /usr/lib/chrome_for_testing
     ```
   * Download the Chrome for Testing package archive to a temporary location. This is a safe and verified archive hosted by Dynatrace.

     ActiveGate version 1.329

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-142.0.7444.175.zip
     ```

     ActiveGate version 1.327

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-141.0.7390.122.zip
     ```

     You can [verify the authenticity of the packages](#verify) using the signature files stored together with the package archives.
   * Extract the installation package and clean up:

     ```
     sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing



     rm /tmp/chrome.zip
     ```

     This creates a `chrome-linux64` directory inside `/usr/lib/chrome_for_testing` and extracts the Chrome binary and supporting files into it.
   * Verify Chrome for Testing by checking the version:

     ```
     /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
     ```

     Command output should show the Chrome version you downloaded.
3. After you satisfy the dependencies, run the ActiveGate installer with root rights. The installer will automatically detect and validate Chrome for Testing. For example:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

   Custom Chrome for Testing directory: If you want to use a different directory than the default `/usr/lib/chrome_for_testing`, specify it by setting the `synthetic_chrome_for_testing_path` property in the `custom.properties` file after installation. The new directory will be used after the upgrade of Synthetic module.

   Chrome for Testing files are preserved during ActiveGate uninstallation. If you uninstall the ActiveGate, the Chrome for Testing directory and its contents will remain on the system and can be reused during reinstallation.

## Linux only Install Chromium from a custom repository

ActiveGate version 1.243+ In addition to [web UI-guided ActiveGate installation](#install) and [manual installation of Chromium and dependencies](#manual), you can also **install ActiveGate by pointing to a custom, local repository for Chromium components**. As this repository is an HTTP server that you set up within your network, the advantage of this method is that it can be used in environments with intranet-only or limited network access.

This method of installing Chromium broadly consists of:

* Downloading the required Dynatrace-hosted deb, snap, or rpm package archives and their corresponding signature files.
* Installing and running a locally hosted web server where the downloaded Chromium components reside.
* Downloading and running the ActiveGate installer on the target host with an environment variable pointing to the location of the custom repository on the HTTP server.

* A custom Chromium repository can be used only for Chromium components, not their dependencies. Installing Chromium from a custom repository will only work if all dependencies have been resolved before installation.
* Custom repositories can only be used for **Chromium installation and autoupdate**âsee [Chromium autoupdate from a custom repository in Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Analyze and manage capacity usage at your private Synthetic locations.") for details.

1. Download the Chromium componentsâthe package archive and signature fileâfrom the safe and verified archive hosted by Dynatrace. See [Requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for links to the latest supported and provided Chromium versions.

   We recommend keeping your Linux-based Synthetic-enabled ActiveGates and Chromium versions up to date; choose the latest provided Chromium version for ActiveGate.

   For example, for ActiveGate version 1.255 on Ubuntu 22. the required files are:

   * Package archiveâ`https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-107.0.5304.87-2168.tgz`
   * Signature fileâ`https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-107.0.5304.87-2168.tgz.sig`

   The corresponding download commands are:

   ```
   curl -o chromium-107.0.5304.87-2168.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-107.0.5304.87-2168.tgz
   ```

   ```
   curl -o chromium-107.0.5304.87-2168.tgz.sig https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-107.0.5304.87-2168.tgz.sig
   ```
2. Install a web server of your choice and create a directory, for example, `chromium-repo`, to serve the Chromium components to the ActiveGate host. Copy the downloaded Chromium components to this directory.
3. Download the ActiveGate installer from Dynatrace Hub.
4. Resolve all dependencies and enable repositories as required as shown in [Install Chromium and dependencies manually from S3](#manual) above. The custom repository can be used only for Chromium packages, not their dependencies.
5. Install the ActiveGate with the Synthetic module enabled (`--enable-synthetic`) and the `DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO` environment variable pointing to the location of the custom repository (`https://172.18.0.100/chromium-repo` in this example).

   ```
   sudo DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-1.257.0.20221129-155835.sh --enable-synthetic
   ```

   You can use the hostname of the HTTP server instead of the IP address so long as the ActiveGate host can resolve the hostname.

Once you've installed Chromium in this way from a custom repository, it can only be autoupdated. See [Chromium autoupdate from a custom repository in Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Analyze and manage capacity usage at your private Synthetic locations.") for details and update alternatives.

## Custom Chromium version

You can install a custom Chromium version, that is, override the Chromium version that the ActiveGate installer looks for. This is applicable for manual ActiveGate installation, as described in [Chromium installation via S3](#manual) or via a [custom repository](#custom-repo).

In this command for manual ActiveGate installation via S3, an environment variable points to an explicit Chromium version number `107.0.5304.87-2168`, which is part of the package archive for Ubuntu 20 or 22.

```
sudo /bin/bash -c "export DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=107.0.5304.87-2168; /bin/bash Dynatrace-ActiveGate-Linux-x86-1.257.0.20221129-155835.sh --enable-synthetic"
```

This command searches for the Chromium version `107.0.5304.87-2168` in the custom repository `https://172.18.0.100/chromium-repo`.

```
sudo DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=107.0.5304.87-2168 DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-1.257.0.20221129-155835.sh --enable-synthetic
```

## Browserless Synthetic-enabled ActiveGate

In general, we recommend the deployment of Synthetic-enabled ActiveGate to support the execution of all types synthetic monitors (HTTP, browser, NAM).

If you don't need to execute browser monitors, however, you might want to consider deploying your node in a special browserless mode. Such a node will be deployed without the browser. The resulting deployment requires less hardware resources, but browser monitors cannot be executed from such a node.

Consider browserless nodes as an alternative to nodes with browser monitor support when you're focused purely on:

* Network and infrastructure use cases (using NAM monitors)
* API monitoring (using HTTP monitors)

## Kerberos client setup

If you want to run Browser Monitor tests using Kerberos authentication, the private location should be configured to be able to get ticket from the Kerberos Key Distribution Center.

Windows

Linux

1. Each Windows machine using Kerberos has to be properly configured with Active Directory.
2. If you are unable to authenticate with Kerberos on Windows, use the following command to register the machine.

```
ksetup /addkdc DOMAIN.TO.ADD address.of.kerberos.server
```

The `DOMAIN.TO.ADD` is your domain name and `address.of.kerberos.server` is the Kerberos Key Distribution Center (Active Directory Controller if you're using a Microsoft solution). Note that in the credentials used, the domain name must be in uppercase (for example, user@EXAMPLE.COM).

Synthetic uses Kerberos authentication by executing the `kinit` command. For details, see [MIT Kerberos Documentation - kinitï»¿](https://dt-url.net/pr43wj6).

A Linux private location has to be properly configured to be able to get a ticket from the Kerberos Key Distribution Center. Make sure that the location has the following:

* Installed packages for Kerberos client (workstation).
* Properly configured `/etc/krb5.conf` file (or configuration file specified by `KRB5_CONFIG` environment variable).

The configuration is dependent on the Linux distribution. You can find more information in the official documentation.

* Ubuntu:

  + `sudo apt install krb5-user`
  + More information: [Ubuntu Server Documentation - How to set up basic workstation authenticationï»¿](https://dt-url.net/3g03w9p)
* Red Hat/Rocky:

  + `yum install krb5-workstation krb5-libs`
  + More information: [Red Hat Documentation - Configuring a Kerberos Clientï»¿](https://dt-url.net/1u23wq7)

## Synthetic FIPS compliance

ActiveGate version 1.315+

### Installation

To install Synthetic-enabled ActiveGate in FIPS compliant mode you need to add `--fips-mode` flag, see also [customize ActiveGate installation for FIPS compliance](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

```
/bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic --fips-mode
```

Please note that FIPS-compliant mode cannot be changed after installation. To change the mode, you need to uninstall ActiveGate and reinstall it with the desired settings.
Additionally, if you intend to execute browser monitors additional setup will be required as described in [Proxy configuration for FIPS mode](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.") and [Proxy configuration for FIPS mode with corporate proxy](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-corporate-proxy "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")

### Requirements and limitations

* We require operating system with FIPS-compliant mode enabled, see also [ActiveGate FIPS compliance](/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance "Learn about ActiveGate FIPS compliance").
* Following operating systems are currently supported:

  + Ubuntu Pro 22.04
  + Red Hat Enterprise Linux 9
* Private Synthetic locations on Kubernetes are not supported at the moment.

### Ensuring compliance

To ensure the browser monitor traffic is FIPS compliant, it must be routed through a local intercepting proxy that encrypts traffic with a FIPS-certified crypto library. See [Proxy configuration for FIPS mode](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.") for details.

For HTTP monitors, we use the [Amazon Corretto Crypto Providerï»¿](https://github.com/corretto/amazon-corretto-crypto-provider/) FIPS-certified cryptographic library that uses AWS-LC-FIPS 2.x as its cryptographic module. See [Certificate #4816ï»¿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816).

Synthetic-enabled ActiveGate in FIPS compliant mode supports the same set of cipher suites as [regular ActiveGate](/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance#supported-cipher-suites "Learn about ActiveGate FIPS compliance").

## FAQ

How can I verify the authenticity of downloaded Chrome(-ium) packages?

Chromium

Chrome for Testing

Each `tgz` package archive is stored in the S3 bucket together with the `*.tgz.sig` signature file. To verify if the packages on your drive are authentic Dynatrace-provided archives:

1. Download the signature file. The filename is identical to the package archive but has the `sig` filename extension. For example, for Chromium 140, the command is:

   ```
   curl --output chromium.tgz.sig https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-140.0.7339.185-1.el9.tgz.sig
   ```
2. Verify the package:

   ```
   wget https://ca.dynatrace.com/dt-root.cert.pem ; openssl cms



   -verify



   -in chromium.tgz.sig



   -inform PEM



   -content chromium.tgz



   -binary



   -CAfile dt-root.cert.pem > /dev/null
   ```
3. Verify the signature timestamp.

   You can also get the exact timestamp of a signature. Download the `*.tgz.sig.tsr` file from the same location as installation packages and signature and run the following command:

   ```
   openssl ts -reply -in chromium.tgz.sig.tsr -text
   ```

Each `zip` package archive is stored in the S3 bucket together with the `*.zip.sig` signature file. To verify if the packages on your drive are authentic Dynatrace-provided archives:

1. Download the signature file. The filename is identical to the package archive but has the `sig` filename extension. For example, for Chrome for Testing 141.0.7390.122, the command is:

   ```
   curl --output chrome.zip.sig https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-141.0.7390.122.zip.sig
   ```
2. Verify the package:

   ```
   wget https://ca.dynatrace.com/dt-root.cert.pem ; openssl cms



   -verify



   -in chrome.zip.sig



   -inform PEM



   -content chrome.zip



   -binary



   -CAfile dt-root.cert.pem > /dev/null
   ```
3. Verify the signature timestamp.

   You can also get the exact timestamp of a signature. Download the `*.zip.sig.tsr` file from the same location as installation packages and signature and run the following command:

   ```
   openssl ts -reply -in chrome.zip.sig.tsr -text
   ```

Can I use a proxy with the Synthetic-enabled ActiveGate?

With ActiveGate version 1.175+, an ActiveGate executing synthetic monitors can connect through the proxy to both the Dynatrace Cluster and the tested resource. For more information, see [Setting up proxy for private synthetic monitoring](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.").

Can I update an earlier ActiveGate to version 1.169+ and configure it to use with private synthetic monitors?

No, you need to run a clean installation specifically for the purpose of synthetic monitoring to enable your ActiveGate to execute monitors from private locations.

Can I turn on Synthetic on an existing ActiveGate installation?

Private Synthetic locations require a clean installation of ActiveGate specifically for the purpose of synthetic monitoring.

Manually editing the `custom.properties` file is not enough to enable the ActiveGate to execute synthetic monitors.

## Troubleshoot

[Can't see screenshots in browser monitor resultsï»¿](https://dt-url.net/mfw2xmb)

Visit the [Troubleshooting forum in the Dynatrace Communityï»¿](https://dt-url.net/dy122xtf) for more troubleshooting information.

## Related topics

* [Synthetic locations API v2 - POST a location](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location "Create a private synthetic location via the Synthetic v2 API.")