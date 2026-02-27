---
title: Private synthetic locations
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations
scraped: 2026-02-27T21:29:57.423075
---

# Private synthetic locations

# Private synthetic locations

* Latest Dynatrace
* How-to guide
* Updated on Feb 11, 2026

The goal of private locations is to execute synthetic monitors. You need to use private locations to monitor applications and endpoints within corporate networks, which are unavailable from the public internet. Also, private locations are obligatory for executing [NAM](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-a-nam-monitor-synthetic-app "Learn how to set up a NAM monitor to check the performance and availability of your site.") monitors.

With monitors executed from a private location, you can bring the testing capabilities available in public locations right into your own environment. With private locations you can:

* Measure internal webpage performance and availability.
* Measure complex internal applications with browser clickpaths.
* Measure external resources with synthetic monitors run from internal locations.
* Monitor APIs, both internal and external.

You can create only classic locations using ![Synthetic Classic](https://dt-cdn.net/images/synthetic-512-83ec796e54.png "Synthetic Classic") **Synthetic**, although the locations list displays classic and containerized (for example, Kubernetes and OpenShift) locations. If you still need to create a containerized location, you can do it in [Settings Classic](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#add "Learn how to create a private location for synthetic monitoring.").

The **Private locations** tab in ![Synthetic Classic](https://dt-cdn.net/images/synthetic-512-83ec796e54.png "Synthetic Classic") **Synthetic** shows the list of all private locations available within a given environment. For each private location, there's information about how many synthetic monitors are assigned to it, with links to those monitors.

If you created a private location in previous Dynatrace, it remains available in latest Dynatraceâthere's no need to redeploy it.

## System and hardware requirements for private locations

Make sure the target host you plan to use for running synthetic monitors complies with [system and hardware requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/requirements-for-private-synthetic "Check system and hardware requirements for private Synthetic locations."). Note that Synthetic-enabled ActiveGates have more demanding hardware and system requirements than a regular Environment or Cluster ActiveGate.

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
* Until version 1.329 Synthetic-enabled ActiveGates on Ubuntu 20 and Ubuntu 22 use Chromium snap. When customizing the [default temporary directory for private Synthetic files](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories--linux "Find out where ActiveGate files are stored on Windows and Linux systems.")â`/var/tmp/dynatrace/synthetic`, the path must begin with `/var/tmp`, for example, `TEMP=/var/tmp/syn`. Dynatrace requires write access to `/var/tmp` for the installation of Chromium snap packages.
  Since version 1.331, these restrictions no longer apply. The latest ActiveGate version on Ubuntu 20 and Ubuntu 22 uses Chrome for Testing, just like Ubuntu 24.

### Before you begin

* You cannot execute synthetic monitors using an Environment ActiveGate configured for [multi-environment support](/docs/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.").
* You can create a private location using a clean-installed Synthetic-enabled Environment ActiveGate version 1.169+ or Cluster ActiveGate with Dynatrace Managed version 1.176+. If you want to use an existing ActiveGate host, [uninstall ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Learn how to remove ActiveGate from Windows or Linux-based systems.") first.
* Synthetic-enabled ActiveGate is used exclusively to run synthetic monitors. A clean ActiveGate installation for the purpose of synthetic monitoring disables all other ActiveGate features, including communication with OneAgents.
* Make sure that the ActiveGate can connect to other [Dynatrace components](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") as well as the resource you want to test. See [Set up a proxy for private synthetic monitoring](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.").
* Only IPv4 and DNS UDP are supported for network configuration.
* Synthetic-enabled ActiveGate needs access to the Amazon S3 service to upload and access browser monitor screenshots from private locations. Ensure that your firewall configuration allows connections to `*.s3-accelerate.amazonaws.com` on port `443`. You can also [set up your proxy](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.") to connect to the Amazon S3 service. (Screenshots are stored in a different folder for each monitoring environment, but the S3 Bucket is the same (`ruxit-synth-screencap`). Data is encrypted by [Amazon S3-managed keyï»¿](https://dt-url.net/4a02xvx).)
* Both manual and automatic browser updates require access to `https://synthetic-packages.s3.amazonaws.com`. For security reasons, public access to the S3 bucket is enabled only for specific files; trying anything else will result in a 403 error.

## Create a private location



To add a classic private location

1. Go to the **Private locations** tab in the upper-left corner of the ![Synthetic Classic](https://dt-cdn.net/images/synthetic-512-83ec796e54.png "Synthetic Classic") **Synthetic** home page.
2. Select  **New private locations**  > **Classic**.
3. Name your location.
4. Map it from an existing geographic location or add a custom location defined by **Country**, **Region**, **City**, **Latitude**, and **Longitude**.
5. Select **Existing ActiveGate** to add an existing Synthetic-enabled Activegate to the location or **Deploy new ActiveGate** to deploy a new one (deploying a new ActiveGate will redirect you to [![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**](/docs/ingest-from/discovery-coverage-app "Discover and remediate monitoring coverage gaps at scale.") from where you can [install an ActiveGate](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/active-gate-for-private-locations-install "Learn how to install Synthetic-enabled ActiveGates.")).

   Add multiple ActiveGates if you plan to run a large number of synthetic monitors.
   Additional ActiveGates are used for failover and load balancing.

   * We recommend using at least two ActiveGates for a location.
   * You can't use one ActiveGate for multiple locations.

6. Optional Turn on **Enable Chrome(-ium) auto-update**âit will be triggered during the Synthetic engine updates at this location.

   You can **Enable Chrome(-ium) auto-update** at the location level, that is, for all ActiveGates assigned to a private location. Chromium autoupdate takes place during manual as well as automatic ActiveGate and Synthetic engine updates.

   As we recommend using the [latest supported Chromium version](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/requirements-for-private-synthetic#browser-linux "Check system and hardware requirements for private Synthetic locations.") for the smooth and secure execution of browser monitors from your private location, Chromium autoupdate is turned on by default for locations with Linux-based ActiveGates. If you don't want Chromium to be updated automatically, for example, to use a specific version of Chromium, or if you have offline environments, turn off the switch **before triggering an ActiveGate update**.

   This setting only applies to Linux-based ActiveGates; on Windows-based ActiveGates, Chromium is always updated during Synthetic engine updates. If your location has only Windows-based ActiveGates, the toggle is turned on but grayed out.

   Successful Chromium autoupdate requires access to OS (system) repositories for Chromium dependencies and access to `https://synthetic-packages.s3.amazonaws.com` for Chromium components. If you've enabled a [custom local repository](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#custom-repo "Learn how to install Chromium for Linux manually and from custom repositories."), Chromium components (but not dependencies) need to be available at the specified HTTP server address. See [Chromium autoupdate from a custom repository](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#autoupdate-custom-repo "Learn how to install Chromium for Linux manually and from custom repositories.").

   You will see a message if Chromium autoupdate fails for this or other reasonsâwe recommend either meeting the requirements for autoupdate (such as access to repositories) or disabling Chromium autoupdate for your private location.

   * We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and Chromium versions updatedâDynatrace supports Chromium versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/requirements-for-private-synthetic#browser-linux "Check system and hardware requirements for private Synthetic locations.") for a specific ActiveGate release. If you don't opt for Chromium autoupdate, you can [update Chromium manually](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#browser-manual "Learn how to install Chromium for Linux manually and from custom repositories.").
   * If you disable Chromium autoupdate, you can [manually update Chromium](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#browser-manual "Learn how to install Chromium for Linux manually and from custom repositories.") per ActiveGate. However, Chromium autoupdate is required when using [custom repositories](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#custom-repo "Learn how to install Chromium for Linux manually and from custom repositories."). See [Chromium autoupdate from a custom repository](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#autoupdate-custom-repo "Learn how to install Chromium for Linux manually and from custom repositories.").
   * Autoupdate works to update Chromium to the latest version that Dynatrace provides for an ActiveGate release. In some cases, this might be different from the [latest Dynatrace-supported Chromium version](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/requirements-for-private-synthetic#browser-linux "Check system and hardware requirements for private Synthetic locations.") for the ActiveGate release.

   Also, check our information on [installing Chromium and other dependencies manually (Linux only)](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux#manual "Learn how to install Chromium for Linux manually and from custom repositories.").
7. Optional If you have outage issues with your private location, use the **Location outage handling** options to receive related notifications. See the on-screen instructions for details.

   * You can configure the location to generate a problem when the entire private location is unavailable (all ActiveGates are offline), or if the location lacks the capability required for the monitor type to be executed.
   * You can configure the location to generate a problem when a single ActiveGate at this location is offline.

   For example, suppose your location has two ActiveGates, and you enable both problem switches. You will see three problems when your location is unavailableâone for the entire location and one for each ActiveGate that's offline.

   Containerized locations

   For containerized locations, you can only generate a problem when the entire private location is unavailable (all ActiveGates are offline), or if the location lacks the capability required for the monitor type to be executed.
8. Select **Save**.

## Additional deployment modes

Additional deployment modes available to you

* Browserless
* Kerberos
* FIPS compliant

### Browserless Synthetic-enabled ActiveGate

In general, we recommend the deployment of a Synthetic-enabled ActiveGate to support the execution of all types of synthetic monitors (HTTP, browser, NAM).

If you donât need to run browser monitors, consider deploying your node in browserless mode. This mode deploys the node without a browser, reducing hardware requirements. However, browser monitors canât run on a browserless node.

Consider browserless nodes as an alternative to nodes with browser monitor support when you're focused purely on:

* Network and infrastructure use cases (using NAM monitors)
* API monitoring (using HTTP monitors)

### Kerberos client setup

If you want to run browser monitors using Kerberos authentication, the private location should be configured to be able to get a ticket from the Kerberos Key Distribution Center.

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

### Synthetic FIPS compliance



ActiveGate version 1.315+

#### Installation

To install Synthetic-enabled ActiveGate in FIPS compliant mode, you need to add the `--fips-mode` flag. See also [customize ActiveGate installation for FIPS compliance](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

```
/bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic --fips-mode
```

Please note that FIPS-compliant mode cannot be changed after installation. To change the mode, you need to uninstall ActiveGate and reinstall it with the desired settings.
Additionally, if you intend to execute browser monitors, additional setup will be required as described in [Proxy configuration for FIPS mode](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/proxy-for-private-locations#fips-proxy "Learn how to manage proxies for private Synthetic locations.") and [Proxy configuration for FIPS mode with corporate proxy](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/proxy-for-private-locations#fips-corporate-proxy "Learn how to manage proxies for private Synthetic locations.").

#### Requirements and limitations

* We require operating system with FIPS-compliant mode enabled, see also [ActiveGate FIPS compliance](/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance "Learn about ActiveGate FIPS compliance").
* Following operating systems are currently supported:

  + Ubuntu Pro 22.04
  + Red Hat Enterprise Linux 9
* Private Synthetic locations on Kubernetes are not supported at the moment.

#### Ensuring compliance

To ensure the browser monitor traffic is FIPS compliant, it must be routed through a local intercepting proxy that encrypts traffic with a FIPS-certified crypto library. See [Proxy configuration for FIPS mode](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/proxy-for-private-locations#fips-proxy "Learn how to manage proxies for private Synthetic locations.") for details.

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

   You can also get the exact timestamp of a signature. Download the `*.tgz.sig.tsr` file from the same location as the installation packages and signature, and then run the following command:

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

With ActiveGate version 1.175+, an ActiveGate executing synthetic monitors can connect through the proxy to both the Dynatrace Cluster and the tested resource. For more information, see [Setting up proxy for private synthetic monitoring](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/proxy-for-private-locations "Learn how to manage proxies for private Synthetic locations.").

Can I update an earlier ActiveGate to version 1.169+ and configure it to use with private synthetic monitors?

No, you need to run a clean installation specifically for the purpose of synthetic monitoring to enable your ActiveGate to execute monitors from private locations.

Can I turn on Synthetic on an existing ActiveGate installation?

Private Synthetic locations require a clean installation of ActiveGate specifically for the purpose of synthetic monitoring.

Manually editing the `custom.properties` file is not enough to enable the ActiveGate to execute synthetic monitors.

## Troubleshooting

[Can't see screenshots in browser monitor resultsï»¿](https://dt-url.net/mfw2xmb)

Visit the [Troubleshooting forum in the Dynatrace Communityï»¿](https://dt-url.net/dy122xtf) for more troubleshooting information.