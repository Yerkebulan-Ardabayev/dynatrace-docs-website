---
title: Install and update Chromium for Linux
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux
scraped: 2026-02-26T21:31:06.624231
---

# Install and update Chromium for Linux

# Install and update Chromium for Linux

* Latest Dynatrace
* How-to guide
* Updated on Feb 11, 2026

If the [web UIâguided installation](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/active-gate-for-private-locations-install#ui-guided-browser-installation "Learn how to install Synthetic-enabled ActiveGates.") fails or you prefer to prepare the host for the Synthetic engine yourself, you can install Chromium and other dependencies [manually](#manual) or from a [custom repository](#custom-repo).

## Install the browser and dependencies manually from S3

This section is not relevant for browserless locations.

Amazon Linux 2023, Ubuntu and Oracle Linux 9

Amazon Linux 2023, Ubuntu and Oracle Linux 9 use Chrome for Testing instead of Chromium. For manual installation of Chrome for Testing on these operating systems, see [Amazon Linux 2023, Ubuntu and Oracle Linux 9 (Chrome for Testing)](#chrome-for-testing).

Ensure that you can connect to `https://synthetic-packages.s3.amazonaws.com` to access the browser packages. For security reasons, public access to the S3 bucket is enabled only for specific files; trying anything else will result in a 403 error.

Also see [Install the browser from a custom repository](#custom-repo) below.

See [how to update the browser manually](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Analyze and manage capacity usage at your private Synthetic locations.") in [Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations."). We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and browser versions updatedâDynatrace supports browser versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for a specific ActiveGate release.

### Ubuntu Server 20.04 and 22.04

This section is only relevant for releases 1.329 and earlier.

1. Install Synthetic engine dependencies:

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

   * Download the snap (Ubuntu Server 20.04 and 22.04) package archive. This is a safe and verified archive hosted by Dynatrace.

     ActiveGate version 1.329

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-142.0.7444.175-3313.tgz
     ```

     ActiveGate version 1.327

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-141.0.7390.122-3285.tgz
     ```

     ActiveGate version 1.325

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-140.0.7339.185-3251.tgz
     ```

     ActiveGate version 1.323

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-139.0.7258.138-3235.tgz
     ```

     ActiveGate version 1.321

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.157-3203.tgz
     ```

     ActiveGate version 1.319

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.100-3199.tgz
     ```

     ActiveGate version 1.317

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-137.0.7151.103-3169.tgz
     ```

     ActiveGate version 1.315

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-136.0.7103.59-3121.tgz
     ```

     ActiveGate version 1.313

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-135.0.7049.95-3110.tgz
     ```

     ActiveGate version 1.311

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-134.0.6998.35-3060.tgz
     ```

     ActiveGate version 1.309

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-132.0.6834.159-3036.tgz
     ```

     ActiveGate version 1.307

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-131.0.6778.85-3002.tgz
     ```

     You can [verify the authenticity of the packages](#verify) using the signature files stored together with the package archives.
   * Extract the installation packages. Go to the directory where you saved the archive and run the following command:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     This creates a `/tmp/chromium` directory and extracts the packages into it.
   * Install the extracted packages.

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

You can [verify the authenticity of the packages](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#verify "Learn how to manage private locations in the Synthetic app.") using the signature files stored together with the package archives.

### Red Hat Enterprise Linux, Oracle Linux 8, and Rocky Linux

* Chromium development for Red Hat/CentOS 7 and Amazon Linux 2 stopped at version 126.

  + Since Red Hat Enterprise Linux 7 reached [End of Maintenanceï»¿](https://dt-url.net/af03uea) support on June 30, 2024, all of its packages have been archived. This means that it may not be possible to find the required dependencies for update. For more details, see the [Red Hat Enterprise Linux 7 statusï»¿](https://dt-url.net/e623zr1)
* Chromium installation when a proxy is required for internet access.

  + If you need to download and install Chromium, and your system requires a proxy for internet access, you should configure `curl` to use the correct proxy. Specify your proxy and port details by running the commands as in this example:

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

     ActiveGate version 1.331

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-143.0.7499.192-1.el9.tgz
     ```

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

     You can [verify the authenticity of the packages](#verify) using the signature files stored together with the package archives.
   * Extract the installation packages. Go to the directory where you saved the archive and run the following command:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     This creates a `/tmp/chromium` directory and extracts the packages into it.
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

You can [verify the authenticity of the packages](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#verify "Learn how to manage private locations in the Synthetic app.") using the signature files stored together with the package archives.

### Amazon Linux 2023, Ubuntu, and Oracle Linux 9 (Chrome for Testing)

Unlike Chromium on other distributions, Chrome for Testing updates do not use package managers. You manually manage the Chrome binaries while dependencies are managed by the system package manager.

On Ubuntu Server 20.04 and 22.04 Chrome for Testing is supported since 1.331

1. Set up repositories and install dependencies.

   Ubuntu

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

     ActiveGate version 1.331

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip
     ```

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

* Custom Chrome for Testing directory: If you want to use a different directory than the default `/usr/lib/chrome_for_testing`, specify it by setting the `synthetic_chrome_for_testing_path` property in the `custom.properties` file after installation. The new directory will be used after the upgrade of Synthetic module.
* Chrome for Testing files are preserved during ActiveGate uninstallation. If you uninstall the ActiveGate, the Chrome for Testing directory and its contents will remain on the system and can be reused during reinstallation.
* You can [verify the authenticity of the packages](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#verify "Learn how to manage private locations in the Synthetic app.") using the signature files stored together with the package archives.

## Update the browser manually from S3

If you have an offline environment or you installed an ActiveGate manually for dependency management or due to limited access to Amazon S3, you need to update the browser and dependencies manually.

You need to update the browser manually per ActiveGate, and the process varies slightly based on the operating system. Note that manual update of the browser only applies to Linux-based ActiveGates; on Windows-based ActiveGates, the browser is automatically updated during Synthetic engine updates.

Prerequisites:

* Ensure that [**Enable Chrome(-ium) auto-update**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#browser-autoupdate "Learn how to manage private locations in the Synthetic app.") is turned off for your private location. If you disable autoupdate for a location, you need to update the browser manually on every ActiveGate assigned to that location.
* Ensure that you can connect to `https://synthetic-packages.s3.amazonaws.com` to access the browser packages.

* The Synthetic engine will use the new browser version after the update is completeânote that the status is updated once every hour, so it may take up to an hour to refresh the browser version displayed for your ActiveGate in **Deployment Status**.
* We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and browser versions updatedâDynatrace supports browser versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/requirements-for-private-synthetic#browser-linux "Check system and hardware requirements for private Synthetic locations.") for a specific ActiveGate release.
* We strongly recommend updating all ActiveGates per location to the same version.
* See also [Browser autoupdate from a custom repository](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#autoupdate-custom-repo "Learn how to install Chromium for Linux manually and from custom repositories.").

Since ActiveGate 1.331, on Ubuntu Server 20.04 and 22.04 we use Chrome for Testing. Chromium snap distribution is no longer supported.
If you are using any automation for updating the browser, convert it to use Chrome for Testing. Please refer to [community guideï»¿](https://dt-url.net/il0363p) for details.

Ubuntu (snap)

Red Hat Enterprise Linux and CentOS

Amazon Linux 2023, Ubuntu, and Oracle Linux 9 (Chrome for Testing)

This section is only relevant for releases 1.329 and earlier for Ubuntu Server 20.04 and 22.04.

1. If your ActiveGate and Chromium versions are out of support or have not been updated for several releases, review the Synthetic Engine and Chromium dependencies, and reinstall them if necessary. See the [manual installation instructions for Ubuntu Server](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#ubuntu "Learn how to install Chromium for Linux manually and from custom repositories.").
2. Download the snap (Ubuntu Server 20.04 and 22.04) package archive. This is a safe and verified archive hosted by Dynatrace at `https://synthetic-packages.s3.amazonaws.com`. Be sure to use the specific command provided for your ActiveGate and Ubuntu Server versions in the [manual installation instructions for Ubuntu Server](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#ubuntu "Learn how to install Chromium for Linux manually and from custom repositories.").
3. Extract and install the downloaded packages. Be sure to use the correct installation command for your Ubuntu Server version (check the [manual installation instructions for Ubuntu Server](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#ubuntu "Learn how to install Chromium for Linux manually and from custom repositories.")).
4. Verify Chromium update by running the following command from the default installation directory. Command output should match the Chromium version you installed.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Updating Chromium manually is identical on Red Hat Enterprise Linux and CentOS, the only difference being the downloaded packages for Red Hat/CentOS version 7 and version 8.

If you've installed Chromium manually, there's no need at the time of the update to register the Red Hat instance in the subscription manager or to enable the Red Hat repositories or EPEL packages.

1. If your ActiveGate and Chromium versions haven't been updated in a while, you might want to install Synthetic engine dependencies again. See the [manual installation instructions for Red Hat Enterprise Linux and CentOS](#redhat).
2. Download the rpm package archive. This is a safe and verified archive hosted by Dynatrace at `https://synthetic-packages.s3.amazonaws.com`. Be sure to use the specific command provided for your ActiveGate and OS versions in the [manual installation instructions for Red Hat Enterprise Linux and CentOS](#redhat).
3. Extract and install the downloaded packages. Check the [manual installation instructions for Red Hat Enterprise Linux and CentOS](#redhat).
4. If necessary, disable the automatic update of Chromium packages. Note that for Red Hat Enterprise Linux and CentOS, packing locking, once performed, remains persistent across all future updates.

   ```
   sudo yum -y install yum-plugin-versionlock



   sudo yum versionlock chromium



   sudo yum versionlock chromium-common
   ```
5. Verify Chromium update by running the following command from the default installation directory. Command output should match the Chromium version you installed.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Chrome for Testing is managed differently from Chromium. To update manually, download the new version and extract it to the Chrome for Testing directory.

Unlike Chromium on other distributions, Chrome for Testing updates do not use package managers. You manually manage the Chrome binaries while dependencies are managed by the system package manager.

Ubuntu Server 20.04 and 22.04

When migrating from Chromium snap, first update the ActiveGate, then install Chrome for Testing and optionally remove Chromium snap files.

1. If your ActiveGate and Chrome for Testing versions haven't been updated in a while, you might want to check and install Synthetic engine and Chrome for Testing dependencies again. See the [manual installation instructions for Chrome for Testing](#chrome-for-testing).
2. Download the Chrome for Testing package archive to a temporary location. This is a safe and verified archive hosted by Dynatrace at `https://synthetic-packages.s3.amazonaws.com`. Be sure to use the specific command provided for your ActiveGate version in the [manual installation instructions for Chrome for Testing](#chrome-for-testing), but modify the output path to `/tmp/chrome.zip`.
3. Remove the old Chrome for Testing directory, extract the new version, and clean up:

   ```
   sudo rm -rf /usr/lib/chrome_for_testing/chrome-linux64



   sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing



   rm /tmp/chrome.zip
   ```

   If you configured a custom Chrome for Testing directory via the `synthetic_chrome_for_testing_path` property in `custom.properties`, replace `/usr/lib/chrome_for_testing` with your custom path in the commands above.
4. Verify Chrome for Testing update by running the following command. Command output should match the Chrome version you installed.

   ```
   /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
   ```

   The Synthetic engine will use the new Chrome for Testing version immediately. Note that the status is updated once every hour, so it may take up to an hour to refresh the Chrome version displayed for your ActiveGate in **Deployment Status**.

## Install the browser from a custom repository

ActiveGate version 1.243+ In addition to [web UI-guided ActiveGate installation](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/active-gate-for-private-locations-install "Learn how to install Synthetic-enabled ActiveGates.") and [manual installation of the browser and dependencies](#manual), you can also **install ActiveGate by pointing to a custom, local repository for browser components**. As this repository is an HTTP server that you set up within your network, the advantage of this method is that it can be used in environments with intranet-only or limited network access.

This method of installing the browser broadly consists of:

* Downloading the required Dynatrace-hosted deb, snap, or rpm package archives and their corresponding signature files.
* Installing and running a locally hosted web server where the downloaded browser components reside.
* Downloading and running the ActiveGate installer on the target host with an environment variable pointing to the location of the custom repository on the HTTP server.

* A custom browser repository can be used only for browser components, not their dependencies. Installing the browser from a custom repository will only work if all dependencies have been resolved before installation.
* Custom repositories can only be used for **browser installation and autoupdate**âsee [Browser autoupdate from a custom repository](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#autoupdate-custom-repo "Learn how to install Chromium for Linux manually and from custom repositories.") for details.

1. Download the browser componentsâthe package archive and signature fileâfrom the safe and verified archive hosted by Dynatrace. See [Requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/requirements-for-private-synthetic "Check system and hardware requirements for private Synthetic locations.") for links to the latest supported and provided browser versions.

   We recommend keeping your Linux-based Synthetic-enabled ActiveGates and browser versions up to date; choose the latest provided browser version for ActiveGate.

   For example, for ActiveGate version 1.331 on Ubuntu 24 the required files are:

   * Package archiveâ`https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip`
   * Signature fileâ`https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig`

   The corresponding download commands are:

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip
   ```

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip.sig https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig
   ```
2. Install a web server of your choice and create a directory, for example, `chromium-repo`, to serve the Chromium components to the ActiveGate host. Copy the downloaded browser components to this directory.
3. Download the ActiveGate installer from Dynatrace Hub.
4. Resolve all dependencies and enable repositories as required as shown in [Install the browser and dependencies manually from S3](#manual) above. The custom repository can be used only for browser packages, not their dependencies.
5. Install the ActiveGate with the Synthetic module enabled (`--enable-synthetic`) and the `DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO` environment variable pointing to the location of the custom repository (`https://172.18.0.100/chromium-repo` in this example).

   ```
   sudo DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
   ```

   You can use the hostname of the HTTP server instead of the IP address so long as the ActiveGate host can resolve the hostname.

Once you've installed the browser in this way from a custom repository, it can only be autoupdated. See [Browser autoupdate from a custom repository in Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Analyze and manage capacity usage at your private Synthetic locations.") for details and update alternatives.

## Browser autoupdate from a custom repository

If you've enabled a [custom, local repository for the browser installation](#custom-repo), the browser can only be autoupdated. Follow this procedure to autoupdate the browser via the same custom repository.

1. After ActiveGate installation, specify the custom repository of the ActiveGate in the [`[synthetic]` section of the `custom.properties` file](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") in the `/var/lib/dynatrace/gateway/config` directory. This allows for automatic browser updates from the custom repository during manual or automatic Synthetic engine updates.

   ```
   [synthetic]



   chromium_repo = https://172.18.0.100/chromium-repo
   ```
2. Turn on [**Enable Chrome(-ium) auto-update**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#browser-autoupdate "Learn how to manage private locations in the Synthetic app.") for your private location.

   Note that the browser autoupdate UI setting applies to all ActiveGates assigned to your private location.
3. Ensure that the browser components required for update are available at the custom repository location. The browser is then automatically updated from the custom repository during ActiveGate and Synthetic engine updates.

Browser autoupdate option

If you do not specify the custom repository in `custom.properties`, the browser is downloaded and updated from S3 during a manual or automatic ActiveGate and Synthetic engine update.

## Custom browser version

You can install a custom browser version, that is, override the browser version that the ActiveGate installer looks for. This is applicable for manual ActiveGate installation, as described in [Browser installation via S3](#manual) or via a [custom repository](#custom-repo).

In this command for manual ActiveGate installation via S3, an environment variable points to an explicit browser version number `143.0.7499.192`, which is part of the Chrome for Testing package archive.

```
sudo /bin/bash -c "export DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192; /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic"
```

This command searches for the browser version `143.0.7499.192` in the custom repository `https://172.18.0.100/chromium-repo`.

```
sudo DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192 DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
```