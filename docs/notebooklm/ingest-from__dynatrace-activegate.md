# Dynatrace Documentation: ingest-from/dynatrace-activegate

Generated: 2026-02-16

Files combined: 15

---


## Source: activegate-diagnostics.md


---
title: ActiveGate diagnostics
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-diagnostics
scraped: 2026-02-16T09:40:15.019396
---

# ActiveGate diagnostics

# ActiveGate diagnostics

* Latest Dynatrace
* 9-min read
* Updated on Oct 20, 2025

You can run fully automated ActiveGate troubleshooting for Dynatrace SaaS and Managed environments.

The workflow enables you to:

* Automatically pinpoint an ActiveGate-related issue in highly dynamic environments, at a specific point in time
* Easily collect the diagnostic data for a specific entity, and automatically get potential solutions for detected anomalies
* Quickly resolve common issues on your own, reducing the amount of time spent on diagnosing
* Directly provide Dynatrace Support all the details they need to diagnose the issue

If ActiveGate can't connect to the Dynatrace environment or doesn't start, you might need to collect diagnostic data locally from the command line. For details, see [Collect diagnostic data with `agctl`](#collect-diagnostic-data-with-agctl).

## Requirements

* **View sensitive request data** environment permission
* For an ActiveGate configured for multi-environment support, you can run ActiveGate diagnostics only on the main environment, as defined in the [ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.").

## Analyze automatically

This procedure describes the default procedure: Dynatrace collects diagnostics data for an ActiveGate and immediately analyzes it.

If you prefer to collect and review the data before manually submitting it to Dynatrace for analysis, see [Collect and review locally](#collect-and-review-locally).

1. Go to **Deployment Status** > **ActiveGates**.
2. Expand the ActiveGate entry you want to troubleshoot and select **Run ActiveGate diagnostics**.
3. On the **Run Dynatrace ActiveGate diagnostics** page, briefly describe what isnât working as expected from your point of view.
4. Optional By default, 7 days of data is collected for analysis. If you need more data, select the **Advanced options** link, change the number of days, and select **Apply**.
5. Select **Start analysis**.

### What happens next

Dynatrace does the following:

* Collects diagnostic data for the last 7 days (if you didn't change the default) of the affected ActiveGate
* Stores the collected diagnostic data
* Uploads the diagnostic data to an S3 bucket in the AWS region of your environment for further analysis

The **State** column describes the current phase of the process.

**State** does not automatically refresh. Select **Refresh** to check for a state change.

Collecting

Data collection is in progress.
While collecting data, you can:

* **Refresh** the page to update the progress.
* **Cancel** diagnostic data collection.

Collected

Dynatrace has finished collecting diagnostic data.
After collecting data, you can:

* **Analyze** to submit the collected data to Dynatrace for analysis.
* **Download** the collected data locally for your inspection.
* **Delete** the issue, including the collected diagnostic data.

Sending in progress

Diagnostic data is being transferred to Dynatrace for analysis.
While sending data, you can:

* **Refresh** the page to update the progress.
* **Download** the collected diagnostic data.
* **Delete** the issue, including the collected diagnostic data.

Sent to Dynatrace cloud

Diagnostic data has been transferred to Dynatrace for analysis.

Analyzing

Dynatrace is now analyzing the diagnostic data.  
While analyzing data, you can:

* **Refresh** the page to update the progress.
* **Download** the collected diagnostic data.
* **Delete** the issue, including the collected diagnostic data.

Analyzed

The analysis is done. The number of associated alerts is shown in parentheses.  
After an analysis, you can:

* **Download** the collected diagnostic data.
* **Delete** the issue, including the collected diagnostic data.

Delete in progress

The diagnostic data is being deleted. While deleting data, you can:

* **Refresh** the page to update the progress.

Deleted

The diagnostic data has been deleted. Dynatrace keeps only a small set of information about who, when, where, and why the diagnostic data was collected.

Canceled

The diagnostics process was canceled manually before it was finished.

### Review the Dynatrace analysis

When the analysis is complete, Dynatrace sends the results back to your environment. If a potential solution is identified, Dynatrace lists it in the **Alerts section.**

## Collect and review locally

This procedure describes how to collect diagnostics data for the ActiveGate. Use this option if you prefer to collect and review the data before manually submitting it to Dynatrace for analysis.

If you instead want to collect data and submit it to Dynatrace automatically for analysis, see [Analyze automatically](#analyze-automatically).

1. Go to **Deployment Status** > **ActiveGates**.
2. Expand the ActiveGate entry you want to troubleshoot and select **Run ActiveGate diagnostics**.
3. On the **Run Dynatrace ActiveGate diagnostics** page, briefly describe what isnât working as expected from your point of view.
4. Select the **Advanced options** link.
5. Select **and store locally**.

   * While you are here, you can also change the number of days of data to collect (default = `7 days`).
6. Select **Apply**.
7. Select **Start collection** to collect diagnostic data and store it locally.

### What happens next

Dynatrace now:

* Collects diagnostic data for the last 24 hours (if you didn't change the default) of the affected ActiveGate
* Stores the collected diagnostic data

The **State** column describes the current phase of the process.

**State** does not automatically refresh. Select **Refresh** to check for a state change.

Collecting

Data collection is in progress.
While collecting data, you can:

* **Refresh** the page to update the progress.
* **Cancel** diagnostic data collection.

Collected

Dynatrace has finished collecting diagnostic data.
After collecting data, you can:

* **Analyze** to submit the collected data to Dynatrace for analysis.
* **Download** the collected data locally for your inspection.
* **Delete** the issue, including the collected diagnostic data.

### What to do with the collected data

Now that the data is collected, you can:

* **Download** the collected data.

  + You can review the data. See [Contents of diagnostic data](#contents) for an overview of what's in the download.
  + You can add the data to your support ticket.
* **Analyze** the data.
* **Delete** the issue, including the collected diagnostic data.

### ActiveGate diagnostics in Dynatrace Managed air-gapped environments

In a Dynatrace Managed air-gapped environment:

1. Use the **Store locally** option under **Advanced options** as described above.
2. After diagnostic data is collected, you can add the data to your support ticket.
3. Dynatrace can then fetch the diagnostic data from your support ticket, analyze it, and provide automated feedback to Dynatrace Support about detected anomalies.

Stringent data privacy protections are enforced and logged throughout this process.

## Collect diagnostic data with `agctl`

ActiveGate version 1.275+

In cases where ActiveGate cannot connect to the Dynatrace environment or doesn't start, you might need to collect diagnostic data locally from the command line on the ActiveGate host. To do so, use the `agctl` command line tool to collect all the necessary data and create a package that can be analyzed later.

### Use `agctl` on Linux or Windows

Linux

Windows

#### Locations

* `agctl` is located in [ActiveGate install directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."). If you installed ActiveGate in a custom folder, the path to `agctl` will be different.
* The diagnostic package is written in the current working directory by default.

  + To change this, use the `--directory=<path>` parameter.
  + After the successful creation of a diagnostic data file, `agctl` prints the path to this file.

#### Permissions

* `agctl` must be run with [the same user as ActiveGate process](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#user-service "Learn about the command-line parameters that you can use with ActiveGate on Linux.") - by default `dtuserag`.
* Make sure that `dtuserag` has write permission for the target directory.

#### Data collected

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

#### Syntax

To collect diagnostic data, run the `agctl` script with the `create-support-archive` parameter and any optional parameters as described above.

```
sudo -u dtuserag /opt/dynatrace/gateway/agctl create-support-archive [--directory=<path> --days=<days> --modules=<modules-list>]
```

#### Locations

* `agctl.bat` is located in the [ActiveGate install directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."). If you installed ActiveGate in a custom folder, the path to `agctl.bat` will be different.
* The diagnostic package is written in the current working directory by default.

  + To change this, use the `--directory=<path>` parameter.
  + After the successful creation of a diagnostic data file, the tool prints the path to this file.

#### Permissions

* `agctl.bat` must be run with [the same user as ActiveGate process](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#user-service "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or as administrator.

#### Data collected

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

#### Syntax

To collect diagnostic data, run the `agctl.bat` script with the `create-support-archive` parameter and any optional parameters as described above.

```
."C:\Program Files\dynatrace\gateway\agctl.bat" create-support-archive [--directory=<path> --days=<days> --modules=<modules-list>]
```

### Use `agctl` from containerized ActiveGate

ActiveGate version 1.325+

You can use `agctl` to gather diagnostic data from a containerized ActiveGate using the `--stdout` parameter, which outputs the support archive directly and allows you to redirect it to a file on your local machine.

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

Kubernetes

OpenShift

```
kubectl exec -n <namespace> <pod-name> -- /opt/dynatrace/gateway/agctl create-support-archive --stdout > ag-support-archive.zip
```

```
oc exec -n <namespace> <pod-name> [-c <container>] -- /opt/dynatrace/gateway/agctl create-support-archive --stdout > ag-support-archive.zip
```

The contents of the support archive are written to `stdout`, allowing them to be redirected to a zip file. Other output is sent to `stderr` to maintain the integrity of the archive file.

Windows PowerShell not supported

Make sure to use the command prompt (`cmd.exe`) on Windows; PowerShell currently isn't supported.

#### For ActiveGate versions before 1.325

ActiveGate version 1.275 to 1.325

For earlier versions of containerized ActiveGate, use `agctl` with the `--directory` parameter and then transfer the file using base64 encoding.

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

Kubernetes

OpenShift

1. Run the command.

   ```
   kubectl exec <pod-name> -n <namespace> -- /opt/dynatrace/gateway/agctl create-support-archive --directory=<tmp-path> [--days=<days> --modules=<modules-list>]
   ```
2. Move the created file to the host. Use base64 to create an encoded file.

   ```
   kubectl exec <pod-name> -n <namespace> -- base64 --wrap=0 <created-file-path> > <encoded-file-host-path>
   ```

1. Run the command.

   ```
   oc exec <pod-name> [-c <container>] -- /opt/dynatrace/gateway/agctl create-support-archive --directory=<tmp-path> [--days=<days> --modules=<modules-list>]
   ```
2. Move the created file to the host. Use base64 to create an encoded file.

   ```
   oc exec <pod-name> [-c <container>] -- base64 --wrap=0 <created-file-path> > <cenoded-file-host-path>
   ```

3. Decode the encoded file using the appropriate Windows or Linux command.

   Linux

   Windows

   ```
   base64 --decode -i <encoded-file-path> > <decoded-file-path>
   ```

   ```
   $base64Data = Get-Content <encoded-file-path>



   $zipBytes = [Convert]::FromBase64String($base64Data)



   Set-Content -Value $zipBytes -Encoding Byte -Path <decoded-file-path>
   ```

### What to do with the collected data

Now that the data is collected:

* You can review the data. See [Contents of diagnostic data](#contents) for an overview of what's in the download.
* You can add the data to your support ticket.

We recommend that you delete the file after use.

## Contents of diagnostic data

All the collected diagnostic data is compressed into a `SupportArchive<ID number>` (for `agctl` - `support_archive_<timestamp>`) ZIP file that includes the following folders and files:

Folder or file

Description

`details.txt` (file)

Contains general information on when and where the diagnostic data was collected and archive statistics.

`config` (folder)

Contains a snapshot of the ActiveGate [configuration directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

`debugui` (folder)

Contains a snapshot of the internal environment configuration related to the ActiveGate.

`log` (folder)

Contains a snapshot of the ActiveGate [log directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

`autoupdater` (folder)

Contains AutoUpdater service logs and RPM, Synthetic, zRemote installer modules.

`install` (folder)

Contains ActiveGate installer logs.

`zremote` (folder)

Contains zRemote, watchdog logs and agent configuration files.

`synthetic` (folder)

Contains ActiveGate Synthetic monitors configuration files and logs.

`remotepluginmodule` (folder)

Contains logs for Extensions and agent executing them.

## Data privacy

To comply with regional data protection and privacy regulations, Dynatrace automatically deletes all diagnostic data 30 days after its collection. This applies to the data in your Dynatrace environment and on the Dynatrace Cluster.

You can choose to delete collected diagnostic data earlier. To ensure transparency, Dynatrace keeps only a small set of information about who, when, where, and why the diagnostic data was collected.

For related details on Dynatrace data privacy, see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Check retention times for various data types.").

## Troubleshooting

Analyze automatically

agctl

* [Status: 'Collecting of the diagnostic data wasnât possible within 20 minutes.'ï»¿](https://dt-url.net/zl237tu)
* ['State' appears to be frozen.ï»¿](https://dt-url.net/ua437h4)

* [Message: 'Unexpected response status code = 500, cannot create SupportArchive file.'ï»¿](https://dt-url.net/zl037au)

## FAQ

Can I access the S3 directly or use my own S3?

No, you cannot access the S3 directly or use your own.

The diagnostic data is uploaded to the Dynatrace S3 bucket that is configured for the environment/cluster by Dynatrace. The S3 bucket used depends on the location of the environment/cluster.


---


## Source: activegate-fips-compliance.md


---
title: ActiveGate FIPS compliance
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance
scraped: 2026-02-15T21:29:00.883889
---

# ActiveGate FIPS compliance

# ActiveGate FIPS compliance

* Latest Dynatrace
* Updated on Jul 15, 2025

ActiveGate version 1.315+

## What is FIPS?

The Federal Information Processing Standard (FIPS) is "a standard for adoption and use by federal departments and agencies that has been developed within the Information Technology Laboratory and published by NIST, a part of the U.S. Department of Commerce. A FIPS covers some topic in information technology to achieve a common level of quality or some level of interoperability" (source: [NIST glossaryï»¿](https://csrc.nist.gov/glossary/term/federal_information_processing_standard)).

FIPS compliance means that a product adheres to all security requirements imposed by the standard.

## ActiveGate FIPS-compliant mode

ActiveGate deployed in FIPS-compliant mode uses FIPS-certified cryptographic libraries:

* Amazon Corretto Crypto Provider 2.4.1 (which uses AWS-LC-FIPS 2.x as its cryptographic module, see [Certificate #4816ï»¿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.0.0 (see [Certificate #4743ï»¿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4743))

## ActiveGate purposes compatibility

Purpose

x86-64

arm64

[Routing-monitoring](/docs/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")[1](#fn-1-1-def)

[Synthetic monitoring in a private location](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")[2](#fn-1-2-def)

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[z/OS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

1

excluding [Extension Execution Controller module](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Learn about the routing and monitoring capabilities and uses of ActiveGate.") (same as regular, non-FIPS ActiveGate).

2

refer to [Requirements and limitations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#fips-compliat-limitation "Learn how to create a private location for synthetic monitoring.") for Synthetic FIPS compliance.

### Host-based ActiveGate deployment

FIPS-compliant mode can be enabled during ActiveGate installation. For details, see [Customize ActiveGate installation on Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

#### Requirements

* Linux x86-64 or ARM64 (AArch64)
* Operating system with FIPS-compliant mode enabled

  + The ActiveGate installer verifies the configuration of the operating system by checking whether the FIPS-compliant mode status stored in `/proc/sys/crypto/fips_enabled` evaluates to value of `1`
  + If the ActiveGate installer is started in FIPS-compliant mode while the operating system does not have FIPS-compliant mode enabled, the installer stops and exits with an error

### Containerized ActiveGate deployment

Containerized ActiveGate deployments rely on FIPS-compliant images, which are available for the following architectures:

* x86-64
* ARM64 (AArch64)

#### Container registries

FIPS-compliant ActiveGate images are available in our [supported public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry") with the image tag suffix `-fips`.

Example: `public.ecr.aws/dynatrace/dynatrace-activegate:1.315.70.20241127-162512-fips`

See [Configure DynaKube to use images from public registry](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#configure-dynakube-to-use-images-from-public-registry "Use a public registry") for details on how to instruct Dynatrace Operator to use images from the public registry.

### Verification of FIPS-compliant mode

### Web UI

To check whether an ActiveGate is running in FIPS-compliant mode

1. Go to **Deployment Status** > **ActiveGates**.
2. Find the ActiveGate of interest and expand the table row.
3. Search for the **FIPS mode** property.

   * If you find **FIPS mode** with a value of `True`, the ActiveGate is in FIPS-compliant mode.
   * If you don't find **FIPS mode** at all, the ActiveGate is not in FIPS-compliant mode.

To list all ActiveGates running in FIPS-compliant mode

1. Go to **Deployment Status** > **ActiveGates**.
2. In the filter bar, select the **FIPS mode** filter and then select `True`.

### REST API

To use the Dynatrace API to check whether a specific ActiveGate is running in FIPS-compliant mode, use [GET an ActiveGate](/docs/dynatrace-api/environment-api/activegates/activegate-info/get-activegate "View the configuration of the specified ActiveGate via the Dynatrace API.") to check the value of the `fipsMode` field.

To use the Dynatrace API to list all ActiveGates running in FIPS-compliant mode, use [GET all ActiveGates](/docs/dynatrace-api/environment-api/activegates/activegate-info/get-all "List all ActiveGates currently or recently connected to the environment.") with the `fipsMode` query parameter.

### Logs

To verify whether ActiveGate is running in FIPS-compliant mode, look up the following entry in the ActiveGate logs (see below how to access logs depending on the ActiveGate deployment type):

```
2025-06-10 12:16:14 UTC INFO    [<tenant>] [FipsDetector] FIPS mode active: true
```

When `FIPS mode active` is `true`, all libraries and configuration related to FIPS compliance are properly initialized and ActiveGate is running in FIPS-compliant mode.

If ActiveGate was installed in FIPS-compliant mode or a FIPS-compliant image was used, but the initialization of FIPS libraries fails or required configuration is missing, ActiveGate cancels its startup and writes the following entries to the log file:

```
ActiveGate FIPS mode initialization failed
```

Additionally, a log line describes the specific reason causing the initialization failure.

#### Accessing logs in host-based deployment

ActiveGate log files have the pattern `dynatracegateway.0.<number>.log` and can be found in the ActiveGate logs directory (see [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories "Find out where ActiveGate files are stored on Windows and Linux systems.")).

#### Accessing logs in containerized deployment

Logs from containerized ActiveGates can be retrieved using the following command:
`kubectl -n <NAMESPACE> logs statefulset.apps/<DYNAKUBE_NAME>-activegate`
In case there are multiple replicas configured, logs from a single pod will be returned.

To get logs from a specific pod, use the following command:
`kubectl -n <NAMESPACE> logs pod/<DYNAKUBE_NAME>-activegate-<REPLICA_NUMBER>`

## Supported cipher suites

Cipher suite

TLS version

[`TLS_AES_256_GCM_SHA384`ï»¿](https://ciphersuite.info/cs/TLS_AES_256_GCM_SHA384)

TLS1.3

[`TLS_AES_128_GCM_SHA256`ï»¿](https://ciphersuite.info/cs/TLS_AES_128_GCM_SHA256)

TLS1.3

[`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)

TLS1.2, TLS1.3

[`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)

TLS1.2, TLS1.3

[`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384)

TLS1.2, TLS1.3

[`TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256)

TLS1.2, TLS1.3

[`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)

TLS1.2, TLS1.3

[`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)

TLS1.2, TLS1.3

[`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384)

TLS1.2, TLS1.3

[`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`ï»¿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)

TLS1.2, TLS1.3


---


## Source: activegate-group.md


---
title: ActiveGate group
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-group
scraped: 2026-02-16T09:17:53.760261
---

# ActiveGate group

# ActiveGate group

* Latest Dynatrace
* 2-min read
* Published Jul 08, 2022

You can use ActiveGate groups to perform bulk actions on your ActiveGates, such as managing [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on ActiveGates or connecting your [Cloud Foundry foundations](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.").

## Requirements

* The name of an ActiveGate group is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`).
* Dots are used as separators, so you must not use a dot as the first character of a group name.
* The length of the string is limited to 256 characters.

## Assign ActiveGate to a group

An ActiveGate can belong to only one group. By default, an ActiveGate is assigned to the `default` group. You can assign an ActiveGate to a group during or after installation.

### Assign to a group during installation

To assign an ActiveGate to a group, you can use the `--set-group` installation parameter during installation. Note that you can't use this parameter during an ActiveGate update. For example:

Linux

Windows

```
/bin/bash Dynatrace-ActiveGate-Linux-x86-<version>.sh --set-group=my-group
```

```
Dynatrace-ActiveGate-Windows-x86-<version>.exe --set-group=my-group
```

### Assign to a group after installation

To assign ActiveGates to a group, you can use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify ActiveGate group** action).

Alternatively, you can use the `group` ActiveGate configuration property. For example:

```
[collector]



group = mygroup
```

For more information, see [Basic rules for working with ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#basic-rules "Learn which ActiveGate properties you can configure based on your needs and requirements.")

## Extensions

An ActiveGate running a remote extension needs to belong to an ActiveGate group because Dynatrace uses a group to instruct the extension where it should run. If you plan to use a single ActiveGate to run a remote extension, assign it to a dedicated group containing only that ActiveGate.

When activating the extension, you need to specify an ActiveGate group that will run your extension. You can select an ActiveGate group either during the Dynatrace Hub-based activation workflow, or specify an ActiveGate group name in the JSON payload used to activate the extension using the Dynatrace API.

## Cloud Foundry foundations

When connecting Dynatrace to Cloud Foundry foundations, you specify an ActiveGate group responsible for querying Cloud Foundry for data. For more information, see [Connect your Cloud Foundry foundations with Dynatrace](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.")


---


## Source: ag-container-persistence.md


---
title: Containerized ActiveGate volumes
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/ag-container-persistence
scraped: 2026-02-16T09:27:10.136118
---

# Containerized ActiveGate volumes

# Containerized ActiveGate volumes

* Latest Dynatrace
* 3-min read
* Published Sep 01, 2023

While running, the ActiveGate container writes data to certain directories within the root filesystem.

## Writeable directories

Purpose of directory

Default path

ActiveGate configuration

`/var/lib/dynatrace/gateway/config`

ActiveGate SSL directory

`/var/lib/dynatrace/gateway/ssl`

ActiveGate temporary files

`/var/tmp/dynatrace/gateway`

ActiveGate logs

`/var/log/dynatrace/gateway`

Environment data

`/var/lib/dynatrace/gateway/data`

Dump files uploaded to ActiveGate by OneAgent

`/var/lib/dynatrace/gateway/dump`

ActiveGate temporary files

`/var/lib/dynatrace/gateway/temp`

### Size requirements

See [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") for estimated size requirements for each directory.

## Hardened security

The ActiveGate [example deployment](/docs/ingest-from/dynatrace-activegate/activegate-in-container#deployment-example "Deploy a containerized ActiveGate.") has been hardened to minimize potential attacks: `securityContext.readOnlyRootFilesystem` is set to `true`.

This prevents the container from modifying any image content, so [directories](#directories) need to be set up using volumes.

### Security context

```
securityContext:



allowPrivilegeEscalation: false



capabilities:



drop:



- all



privileged: false



readOnlyRootFilesystem: true



runAsNonRoot: true



seccompProfile:



type: RuntimeDefault
```

### Volumes

```
volumeMounts:



- name: server-certs-storage



mountPath: /var/lib/dynatrace/gateway/ssl



- name: ag-lib-gateway-config



mountPath: /var/lib/dynatrace/gateway/config



- name: ag-lib-gateway-temp



mountPath: /var/lib/dynatrace/gateway/temp



- name: ag-lib-gateway-data



mountPath: /var/lib/dynatrace/gateway/data



- name: ag-log-gateway



mountPath: /var/log/dynatrace/gateway



- name: ag-tmp-gateway



mountPath: /var/tmp/dynatrace/gateway
```

Refer to [ActiveGate storage requirements](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#space-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") for volume sizing.


---


## Source: configuration.md


---
title: Containerized ActiveGate configuration
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration
scraped: 2026-02-16T09:33:06.715485
---

# Containerized ActiveGate configuration

# Containerized ActiveGate configuration

* Latest Dynatrace
* 6-min read
* Published Sep 01, 2023

An ActiveGate container can be configured to some degree using container-specific methods via variables or secrets. More advanced settings require providing an ActiveGate `custom.properties` file. See [Advanced configuration](#advanced-configuration) to learn how to use Kubernetes mechanisms such as `ConfigMap` to map it into the `custom.properties`.

Sensitive information

To ensure security, you must pass the sensitive information to an ActiveGate container in a file containing a secret.

## Environment configuration

An ActiveGate container image does not hold any configuration related to your environment.

See below for the mandatory configuration settings to make your ActiveGate container work.

### Communication endpoints

This is a comma-separated list of the communication endpoints to be used by ActiveGate to send data to your Dynatrace environment.

To determine the endpoints, use [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.") in the Dynatrace API.

Environment variable

`DT_SERVER`

Mandatory?

### Environment ID

The Dynatrace [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

Environment variable

`DT_TENANT`

Mandatory?

### Token

The [tenant token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") is used by OneAgents and ActiveGates to report data to Dynatrace. Dynatrace automatically generates the tenant token for your ActiveGate.

To determine the token, use [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.") in the Dynatrace API.

Secret as a file

`/var/lib/dynatrace/secrets/tokens/tenant-token`

Mandatory?

### ActiveGate token

ActiveGate requires a unique ActiveGate token to authorize in the Dynatrace Cluster.

For instructions, see [Generate ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.").

Secret as a file

`/var/lib/dynatrace/secrets/tokens/auth-token`

Mandatory?

## Deployment settings

### Activation group

Defines the ActiveGate group to which the ActiveGate belongs. An ActiveGate can belong to only one group. The name of an ActiveGate group is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a group name. The length of the string is limited to 256 characters. You can use ActiveGate groups to perform bulk actions on your ActiveGates, such as managing [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on ActiveGates. If you want to assign your ActiveGate to a group, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Environment variable

Example

`DT_GROUP`

`myGroup`

### Network zone

Defines the [network zone](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") to which the ActiveGate belongs. An ActiveGate can belong to only one network zone. The name of a network zone is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a network zone name. The length of the string is limited to 256 characters.

Environment variable

Example

`DT_NETWORK_ZONE`

`myNetworkZone`

## Enabled modules

Containerized ActiveGate does not enable any functionalities by default. Enabled modules need to be specified using the `DT_CAPABILITIES` environment variable. Add a comma-separated list of module names as the variable value.

Environment variable

Example

`DT_CAPABILITIES`

`azure_monitoring,MSGrouter`

See [ActiveGate modules](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.") for a complete list. Generally, you should refer to the `custom.properties` section names as the module names, for example, `cloudfoundry_monitoring`.

The exceptions to this rule are the following modules that are stored in the `[collector]` section.

* `MSGrouter`âEnables message routing
* `restInterface`âEnables REST API module
* `java-script-agent-servlet`âEnables JavaScript agent

Not all modules are supported

Not all modules are supported in containerized deployments yet. For more information, see [ActiveGate purposes and functionality](/docs/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.").

## Network settings

### Proxy

The proxy used for communication with the Dynatrace Cluster to which ActiveGate sends data.

Secret as a file

Description

`/var/lib/dynatrace/secrets/internal-proxy/host`

Server address.

`/var/lib/dynatrace/secrets/internal-proxy/port`

Optional Port. If left empty, the default 8080 port is used.

`/var/lib/dynatrace/secrets/internal-proxy/scheme`

ActiveGate version 1.289+

Optional Scheme. If left empty, the default `http` scheme is used. This applies the most common setup, where the connection to the proxy is initiated using HTTP and automatically upgraded to a secure one. All further ActiveGate communication through the proxy is secured by SSL/TLS.

Must be set to `https` for proxies that do not support HTTP at all.

`/var/lib/dynatrace/secrets/internal-proxy/username`

Optional User name.

`/var/lib/dynatrace/secrets/internal-proxy/password`

Optional Password, see [Proxy password requirements](#proxy-password-requirements).

#### Advanced scenarios

For more advanced scenarios where one or more proxies are used for means other than communication with the Dynatrace Cluster, see [Proxy for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy."). Once you have crafted the required configuration, you can provide it to the ActiveGate container as a [custom.properties](#advanced-configuration) file.

#### Rules for the proxy password

The proxy password needs to meet the following requirements.

| Requirements | Corresponding characters |
| --- | --- |
| Characters allowed | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
| Characters not allowed | blank space ' ` , & = + % \ |

### Load balancer between ActiveGate and OneAgents

Dynatrace OneAgent accesses the ActiveGate via an auto-detected endpoint list. If a load balancer is placed on the path from OneAgent to the ActiveGate, such as Kubernetes [Serviceï»¿](https://kubernetes.io/docs/concepts/services-networking/service/), you need to explicitly set the endpoint to be used by OneAgents.

Environment variable

Example value

`DT_DNS_ENTRY_POINT`

`https://sg1.mydomain.com:9999`

### Load balancer between ActiveGate and the Dynatrace Cluster

A reverse proxy or a load balancer can be placed on the path from an ActiveGate to the Dynatrace Cluster. This allows your ActiveGate to connect to any available node of the Cluster, spreading the load between the nodes.  
To do this, you need to:

* Provide the address of the reverse proxy/load balancer.
* Ensure that ActiveGate will ignore any further target address information sent from the Dynatrace Cluster, and will thus connect only to the address you have specified.

![ActiveGate connecting to Dynatrace Cluster via reverse proxy/load balancer](https://dt-cdn.net/images/rev-proxy-001-1000-f7d875625b.png)

In this scenario, you need to set the following environment variables.

Environment variable

Example value

`DT_SERVER`

`https://load.balancer.com:9999`

`DT_IGNORE_CLUSTER_RUNTIME_INFO`

`true`

## SSL settings

### Custom SSL certificate

ActiveGate will serve a custom certificate instead of the default one. To configure this, you need a file in `PKCS#12` format that contains a private key and its corresponding certificate chain. For more information, see [Custom SSL certificate for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

Secret as a file

Description

`/var/lib/dynatrace/secrets/tls/server.p12`

Certificate file

`/var/lib/dynatrace/secrets/tls/password`

Optional Certificate password

`/var/lib/dynatrace/secrets/tls/alias`

Optional Certificate alias. The value must be specified in lower case.

### Trusted root certificates

Additional trusted root certificates can be used by ActiveGate. To configure this, you need a file in the `PEM` format that contains a list of certificates to be included in the trust store. For more information, see [Trusted root certificates for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to specify a custom truststore file that is merged with Java's root certificates and used as a default on all connections.").

Secret as a file

Description

`/var/lib/dynatrace/secrets/rootca/rootca.pem`

Certificate file

### HTTP port

An ActiveGate container by default opens HTTPS port `9999`. If you require your ActiveGate to communicate over plain HTTP, you need to explicitly specify the HTTP port.

Environment variable

Example

`DT_HTTP_PORT`

`8888`

## Advanced configuration

In addition to the configuration settings passed via environment variables or files, you can configure all other [configuration settings](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") by providing the contents of the `custom.properties` file.

1. Define `ConfigMap`.

   ```
   kind: ConfigMap



   apiVersion: v1



   data:



   custom.properties: |-



   [vmware_monitoring]



   vmware_monitoring_enabled = true



   metadata:



   name: vmware-config



   namespace: dynatrace
   ```
2. Reference `ConfigMap` in your deployment file.

   ```
   [...]



   volumeMounts:



   [...]



   - name: ag-conf



   mountPath: /var/lib/dynatrace/gateway/config_template/custom.properties



   subPath: custom.properties



   [...]



   volumes:



   - name: ag-conf



   configMap:



   name: vmware-config



   items:



   - key: custom.properties



   path: custom.properties
   ```


---


## Source: differences.md


---
title: Differences between containerized and host-based ActiveGates
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/differences
scraped: 2026-02-15T21:22:23.110313
---

# Differences between containerized and host-based ActiveGates

# Differences between containerized and host-based ActiveGates

* Latest Dynatrace
* 1-min read
* Published Sep 01, 2023

ActiveGate deployed on a host using an installerâdepending on a selected [purpose](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.")âconsists of multiple processes delivering several functionalities. The container image covers only a subset of that, provided by the core ActiveGate process.

## Purposes

An ActiveGate container image currently supports only a subset of [routing and monitoring](/docs/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.") as well as [private synthetic](/docs/ingest-from/dynatrace-activegate/capabilities#synthetic "Learn the capabilities and uses of ActiveGate.").

For a complete overview, see [ActiveGate purposes and functionality](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

**Installer**

**Container**

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

API

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")  
![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") Logs

Infrastructure Monitoring  
(VMware, CloudFoundry, DBInsights, Kubernetes)

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Cloud monitoring

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Azure  
![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") AWS

Extensions

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Synthetic monitors

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

ZRemote

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

## Auto-update

[ActiveGate auto-update](/docs/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.") is supported only for host-based ActiveGates deployed using an installer.

In Kubernetes environments, ActiveGate updates are managed by the container runtime.

ActiveGate is updated automatically on pod restart whenever there is a new version available, unless the image already specifies a certain version.

## Remote configuration management

[Remote configuration management](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") doesn't support containerized ActiveGates.

A containerized ActiveGate configuration is not persistently stored. It is declarative, using the Kubernetes native means of configuration, so any changes triggered by the remote configuration management mechanism would be lost upon container restart.


---


## Source: activegate-in-container.md


---
title: ActiveGate container image
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container
scraped: 2026-02-16T09:18:43.541842
---

# ActiveGate container image

# ActiveGate container image

* Latest Dynatrace
* 2-min read
* Updated on May 09, 2025

Dynatrace supports running ActiveGate in a container. As an example of a container-based deployment, this page describes how to deploy container-based ActiveGate using a StatefulSet on Kubernetes/OpenShift.

## Prerequisites

1. [Create an access token with `InstallerDownload`](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope
2. [Create an authentication token](/docs/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.")
3. Determine the ActiveGate communication endpoints and authentication. Use the [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.") API.
4. Get your kube-system namespace UUID
   How to extract the kube-system namespace UUID

   Run the command below and save the UUID from the output for later use.

   Kubernetes

   OpenShift

   ```
   kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

   ```
   oc get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

## System requirements

A Dynatrace ActiveGate image is supported on a variety of Kubernetes and OpenShift versions. For a complete list, see [Technology support - Kubernetes](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

Images are available for the following architectures:

* x86-64
* ARM64 (AArch64)
* s390x
* PPC64le

## Container registries

To prioritize seamless integration with your tooling and adaptability to your needs, we offer our container images in various ways to maximize flexibility:

* [Dynatrace built-in registry](/docs/ingest-from/setup-on-k8s/guides/container-registries#default "Manage container registries with Dynatrace") default
* [Public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry")
* [Bring your own private registry](/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries") Recommended

Please note that multi-arch Dynatrace container images, ensuring compatibility across various platforms are available from [public registries only](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry"). Dynatrace built-in registry provides only x86-64 images.

## Deployment

Dynatrace provides signed container images to ensure authenticity and integrity, along with SBOMs that list all included software components.
Verifying the signatures and reviewing the SBOMs enables effective vulnerability management and risk mitigation.
For verification details, see [Verify Software Bill of Materials (SBOM) Attestation](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature#sbom-attestation-verification "Verify Dynatrace image signatures").

Private or public registry

Dynatrace built-in registry

1. Create a dedicated namespace.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Create a secret that holds the authentication details to the Dynatrace server used by ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   ```
   oc -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   You need to replace

   * `<YOUR_TENANT_TOKEN>` with the `tenantToken` value obtained in [Prerequisites](#prereq) from the connectivity information.
   * `<YOUR_AUTH_TOKEN>` with the individual ActiveGate token obtained in [Prerequisites](#prereq).
3. Create an `ag-deployment-example.yaml` file with the following content:

   ag-deployment-example.yaml

   ```
   apiVersion: v1



   kind: Service



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   spec:



   type: ClusterIP



   selector:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   ports:



   - protocol: TCP



   port: 443



   targetPort: ag-https



   ---



   apiVersion: apps/v1



   kind: StatefulSet



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   podManagementPolicy: Parallel



   serviceName: ""



   selector:



   matchLabels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   template:



   metadata:



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   affinity:



   nodeAffinity:



   requiredDuringSchedulingIgnoredDuringExecution:



   nodeSelectorTerms:



   - matchExpressions:



   - key: kubernetes.io/arch



   operator: In



   values:



   - <CPU_ARCHITECTURE>



   - key: kubernetes.io/os



   operator: In



   values:



   - linux



   containers:



   - name: activegate



   image: <REPOSITORY_URL>/dynatrace-activegate:<IMAGE_TAG>



   imagePullPolicy: Always



   ports:



   - containerPort: 9999



   name: ag-https



   protocol: TCP



   env:



   - name: DT_TENANT



   value: <YOUR_ENVIRONMENT_ID>



   - name: DT_SERVER



   value: <YOUR_COMMUNICATION_ENDPOINTS>



   - name: DT_ID_SEED_NAMESPACE



   value: dynatrace



   - name: DT_ID_SEED_K8S_CLUSTER_ID



   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>



   - name: DT_CAPABILITIES



   value: restInterface,kubernetes_monitoring,MSGrouter,metrics_ingest



   - name: DT_DEPLOYMENT_METADATA



   value: orchestration_tech=handcrated-ag-sts;script_version=none;orchestrator_id=none



   - name: DT_DNS_ENTRY_POINT



   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication



   volumeMounts:



   - name: dynatrace-tokens



   mountPath: /var/lib/dynatrace/secrets/tokens



   - name: truststore-volume



   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts



   readOnly: true



   subPath: k8s-local.jks



   - name: server-certs-storage



   mountPath: /var/lib/dynatrace/gateway/ssl



   - name: ag-lib-gateway-config



   mountPath: /var/lib/dynatrace/gateway/config



   - name: ag-lib-gateway-temp



   mountPath: /var/lib/dynatrace/gateway/temp



   - name: ag-lib-gateway-data



   mountPath: /var/lib/dynatrace/gateway/data



   - name: ag-log-gateway



   mountPath: /var/log/dynatrace/gateway



   - name: ag-tmp-gateway



   mountPath: /var/tmp/dynatrace/gateway



   livenessProbe:



   failureThreshold: 2



   httpGet:



   path: /rest/state



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 30



   successThreshold: 1



   timeoutSeconds: 1



   readinessProbe:



   failureThreshold: 3



   httpGet:



   path: /rest/health



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 15



   successThreshold: 1



   timeoutSeconds: 1



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi



   securityContext:



   allowPrivilegeEscalation: false



   capabilities:



   drop:



   - all



   privileged: false



   readOnlyRootFilesystem: true



   runAsNonRoot: true



   seccompProfile:



   type: RuntimeDefault



   initContainers:



   - name: certificate-loader



   image: <REPOSITORY_URL>/dynatrace-activegate:<IMAGE_TAG>



   workingDir: /var/lib/dynatrace/gateway



   command: ['/bin/bash']



   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']



   volumeMounts:



   - mountPath: /var/lib/dynatrace/gateway/ssl



   name: truststore-volume



   volumes:



   - name: truststore-volume



   emptyDir: {}



   - name: dynatrace-tokens



   secret:



   secretName: dynatrace-tokens



   - name: server-certs-storage



   emptyDir: {}



   - name: ag-lib-gateway-config



   emptyDir: {}



   - name: ag-lib-gateway-temp



   emptyDir: {}



   - name: ag-lib-gateway-data



   emptyDir: {}



   - name: ag-log-gateway



   emptyDir: {}



   - name: ag-tmp-gateway



   emptyDir: {}



   updateStrategy:



   type: RollingUpdate
   ```
4. Modify your deployment YAML file.

   Add environment configuration details to the `ag-deployment-example.yaml` file, making sure to replace:

   * `CPU_ARCHITECTURE` with your CPU architecture. Possible values are `amd64`, `arm64`, `s390x`, and `ppcle64`
   * `<REPOSITORY_URL>` with one of the [supported registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry")
   * `<IMAGE_TAG>` with correct image tag ([examples](/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#image-tags "Store Dynatrace images in private registries"))
   * `<YOUR_ENVIRONMENT_ID>` with your environment ID

     To determine your environment ID, see the syntax below.

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` with the value of `communicationEndpoints` obtained in [Prerequisites](#prereq) from the connectivity information

     The list of server communication endpoints (`communicationEndpoints`) may change over time.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` with the kube-system namespace UUID obtained in [Prerequisites](#prereq)

     For PPC64le architecture, additional configuration is required. For details, see [ActiveGate container image](/docs/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Deploy a containerized ActiveGate.").

   Options:

   * Optional Enable AppArmor if available.

     AppArmor profile

     To maintain compatibility with a wider array of Kubernetes clusters, the AppArmor profile is not specified in `ag-deployment-example.yaml`. If AppArmor is available on your Kubernetes cluster, we recommend that you additionally annotate StatefulSet with a `runtime/default` profile.

     ```
     spec:



     template:



     metadata:



     annotations:



     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Optional Apply resource limits according to sizing hints.

     K8S monitoring and agent routing sizing hints

     The table below lists suggested ActiveGate CPU and memory sizes according to the number of pods:

     | Number of pods | CPU | Memory |
     | --- | --- | --- |
     | Up to 100 pods | 500 millicores (mCores) | 512 mebibytes (MiB) |
     | Up to 1,000 pods | 1,000 millicores (mCores) | 1 gibibyte (GiB) |
     | Up to 5,000 pods | 1,500 millicores (mCores) | 2 gibibytes (GiB) |
     | Over 5,000 pods | over 1,500 millicores (mCores)[1](#fn-1-1-def) | over 2 gibibytes (GiB)[1](#fn-1-1-def) |

     1

     Actual figures depend on your environment.

     These limits should be taken as a guideline. They're designed to prevent ActiveGate startup process slowdown and excessive node resource usage. The default values cover a large range of different cluster sizes; you can modify them according to your needs, based on the ActiveGate [self-monitoring metrics](/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.").

   For additional configuration options, see [Containerized ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").
5. Deploy ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
6. To verify that ActiveGate has successfully connected to the Dynatrace server, go to **Deployment Status** > **ActiveGates**.

1. Create a dedicated namespace.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Create a secret that holds the environment URL and authentication details for this registry.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret docker-registry dynatrace-docker-registry \



   --docker-server=<YOUR_ENVIRONMENT_URL> \



   --docker-username=<YOUR_ENVIRONMENT_ID> \



   --docker-password=<YOUR_INSTALLER_DOWNLOAD_TOKEN>
   ```

   ```
   oc -n dynatrace create secret docker-registry dynatrace-docker-registry \



   --docker-server=<YOUR_ENVIRONMENT_URL> \



   --docker-username=<YOUR_ENVIRONMENT_ID> \



   --docker-password=<YOUR_INSTALLER_DOWNLOAD_TOKEN> -n dynatrace
   ```

   You need to replace

   * `<YOUR_ENVIRONMENT_URL>` with your environment URL (without `https://`). Example: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` with the Docker account username (the same as the ID in your environment URL above).

     To determine your environment ID, see the syntax below.

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_INSTALLER_DOWNLOAD_TOKEN>` with the access token with `InstallerDownload` scope you created in [Prerequisites](#prereq)
3. Create a secret that holds the authentication details to the Dynatrace server used by ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   ```
   oc -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   You need to replace

   * `<YOUR_TENANT_TOKEN>` with the `tenantToken` value obtained in [Prerequisites](#prereq) from the connectivity information.
   * `<YOUR_AUTH_TOKEN>` with the individual ActiveGate token obtained in [Prerequisites](#prereq).
4. Create an `ag-deployment-example.yaml` file with the following content:

   ag-deployment-example.yaml

   ```
   apiVersion: v1



   kind: Service



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   spec:



   type: ClusterIP



   selector:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   ports:



   - protocol: TCP



   port: 443



   targetPort: ag-https



   ---



   apiVersion: apps/v1



   kind: StatefulSet



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   podManagementPolicy: Parallel



   serviceName: ""



   selector:



   matchLabels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   template:



   metadata:



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   affinity:



   nodeAffinity:



   requiredDuringSchedulingIgnoredDuringExecution:



   nodeSelectorTerms:



   - matchExpressions:



   - key: kubernetes.io/arch



   operator: In



   values:



   - amd64



   - key: kubernetes.io/os



   operator: In



   values:



   - linux



   containers:



   - name: activegate



   image: <YOUR_ENVIRONMENT_URL>/linux/activegate:raw



   imagePullPolicy: Always



   ports:



   - containerPort: 9999



   name: ag-https



   protocol: TCP



   env:



   - name: DT_TENANT



   value: <YOUR_ENVIRONMENT_ID>



   - name: DT_SERVER



   value: <YOUR_COMMUNICATION_ENDPOINTS>



   - name: DT_ID_SEED_NAMESPACE



   value: dynatrace



   - name: DT_ID_SEED_K8S_CLUSTER_ID



   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>



   - name: DT_CAPABILITIES



   value: restInterface,kubernetes_monitoring,MSGrouter,metrics_ingest



   - name: DT_DEPLOYMENT_METADATA



   value: orchestration_tech=handcrated-ag-sts;script_version=none;orchestrator_id=none



   - name: DT_DNS_ENTRY_POINT



   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication



   volumeMounts:



   - name: dynatrace-tokens



   mountPath: /var/lib/dynatrace/secrets/tokens



   - name: truststore-volume



   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts



   readOnly: true



   subPath: k8s-local.jks



   - name: server-certs-storage



   mountPath: /var/lib/dynatrace/gateway/ssl



   - name: ag-lib-gateway-config



   mountPath: /var/lib/dynatrace/gateway/config



   - name: ag-lib-gateway-temp



   mountPath: /var/lib/dynatrace/gateway/temp



   - name: ag-lib-gateway-data



   mountPath: /var/lib/dynatrace/gateway/data



   - name: ag-log-gateway



   mountPath: /var/log/dynatrace/gateway



   - name: ag-tmp-gateway



   mountPath: /var/tmp/dynatrace/gateway



   livenessProbe:



   failureThreshold: 2



   httpGet:



   path: /rest/state



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 30



   successThreshold: 1



   timeoutSeconds: 1



   readinessProbe:



   failureThreshold: 3



   httpGet:



   path: /rest/health



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 15



   successThreshold: 1



   timeoutSeconds: 1



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi



   securityContext:



   allowPrivilegeEscalation: false



   capabilities:



   drop:



   - all



   privileged: false



   readOnlyRootFilesystem: true



   runAsNonRoot: true



   seccompProfile:



   type: RuntimeDefault



   initContainers:



   - name: certificate-loader



   image: <YOUR_ENVIRONMENT_URL>/linux/activegate:raw



   workingDir: /var/lib/dynatrace/gateway



   command: ['/bin/bash']



   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']



   volumeMounts:



   - mountPath: /var/lib/dynatrace/gateway/ssl



   name: truststore-volume



   imagePullSecrets:



   - name: dynatrace-docker-registry



   volumes:



   - name: truststore-volume



   emptyDir: {}



   - name: dynatrace-tokens



   secret:



   secretName: dynatrace-tokens



   - name: server-certs-storage



   emptyDir: {}



   - name: ag-lib-gateway-config



   emptyDir: {}



   - name: ag-lib-gateway-temp



   emptyDir: {}



   - name: ag-lib-gateway-data



   emptyDir: {}



   - name: ag-log-gateway



   emptyDir: {}



   - name: ag-tmp-gateway



   emptyDir: {}



   updateStrategy:



   type: RollingUpdate
   ```
5. Modify your deployment YAML file.

   Add environment configuration details to the `ag-deployment-example.yaml` file, making sure to replace:

   * `<YOUR_ENVIRONMENT_URL>` with your environment URL (without `https://`). Example: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` with the Docker account username (the same as the ID in your environment URL above)

     To determine your environment ID, see the syntax below.

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` with the value of `communicationEndpoints` obtained in [Prerequisites](#prereq) from the connectivity information

     The list of server communication endpoints (`communicationEndpoints`) may change over time.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` with the kube-system namespace UUID obtained in [Prerequisites](#prereq)

   Options:

   * Optional You can change the image version by using different version tag
     Versions

     + `raw`âThe latest available image
     + `1.sprint.patchlevel-raw`âAn image for a particular ActiveGate version (for example, `1.297.0-raw`)

   * Optional Enable AppArmor if available.

     AppArmor profile

     To maintain compatibility with a wider array of Kubernetes clusters, the AppArmor profile is not specified in `ag-deployment-example.yaml`. If AppArmor is available on your Kubernetes cluster, we recommend that you additionally annotate StatefulSet with a `runtime/default` profile.

     ```
     spec:



     template:



     metadata:



     annotations:



     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Optional Apply resource limits according to sizing hints.

     K8S monitoring and agent routing sizing hints

     The table below lists suggested ActiveGate CPU and memory sizes according to the number of pods:

     | Number of pods | CPU | Memory |
     | --- | --- | --- |
     | Up to 100 pods | 500 millicores (mCores) | 512 mebibytes (MiB) |
     | Up to 1,000 pods | 1,000 millicores (mCores) | 1 gibibyte (GiB) |
     | Up to 5,000 pods | 1,500 millicores (mCores) | 2 gibibytes (GiB) |
     | Over 5,000 pods | over 1,500 millicores (mCores)[1](#fn-2-1-def) | over 2 gibibytes (GiB)[1](#fn-2-1-def) |

     1

     Actual figures depend on your environment.

     These limits should be taken as a guideline. They're designed to prevent ActiveGate startup process slowdown and excessive node resource usage. The default values cover a large range of different cluster sizes; you can modify them according to your needs, based on the ActiveGate [self-monitoring metrics](/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.").

   For additional configuration options, see [Containerized ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").
6. Deploy ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
7. To verify that ActiveGate has successfully connected to the Dynatrace server, go to **Deployment Status** > **ActiveGates**.

### Additional configuration for PPC64le architecture

To finish setup of containerized ActiveGate on PPC64le architecture, two more steps are needed:

1. Increase the number of CPU cores: To match the performance of the x86-64 architecture, the CPU core count should be increased by a factor of four.
2. Reduce the number of ActiveGate threads:

   * Create custom properties as described in [Advanced configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration#advanced-configuration "Learn how to configure containerized ActiveGate.")
   * Add the following lines to custom.properties:

     ```
     [com.compuware.apm.webserver]



     threadpool-max-size=30



     async-worker-pool-coresize=60
     ```

To achieve better performance, we highly recommend applying the steps above.

## Dedicated deployments

* To monitor Kubernetes/Openshift, select one of the following:

  + Use [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")
  + Deploy [ActiveGate directly as a StatefulSet](/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.")
* To collect logs from Kubernetes, use [Log Monitoring](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.").

## FIPS-compliant images

ActiveGate version 1.315+

There is a dedicated, FIPS-compliant ActiveGate image available. See [ActiveGate FIPS compliance](/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance "Learn about ActiveGate FIPS compliance") for information on requirements, limitations, where to get the image, and how to verify the deployment.


---


## Source: synthetic-purpose.md


---
title: Execute synthetic monitors from private locations
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose
scraped: 2026-02-16T09:18:39.835793
---

# Execute synthetic monitors from private locations

# Execute synthetic monitors from private locations

* Latest Dynatrace
* 2-min read
* Updated on Jun 01, 2022

**Synthetic-enabled ActiveGates** enable you to set up private Synthetic locations from which you can execute synthetic monitors to monitor your internal as well as external resources.

## Private synthetic monitoring functionality and Synthetic module

(module: [Synthetic](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))

ActiveGates purposed for Dynatrace Synthetic Monitoring have the [Synthetic module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") enabled.

Synthetic-enabled ActiveGates, along with the [Synthetic engine and Chromium](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."), are elements of private Synthetic locations, which are locations in your private network infrastructure.

A private location may consist of one or more Synthetic-enabled ActiveGates. See the [requirements](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") and [process](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for setting up private locations. Once set up, you can use the Dynatrace-based [management interface for private locations and monitors](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations.").

### Important hardware and software notes

Synthetic-enabled ActiveGates are more demanding in terms of hardware requirements. See [Requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

**If an ActiveGate runs the Synthetic module, it cannot have any other functional modules enabled**. If you were to run any other modules on the same ActiveGate, you might run into a situation where synthetic monitors are executed but other processes overloading the machine have a significant impact on monitor performance metrics, setting off false-positive alerts about performance degradation.

## Execute monitors

Any Synthetic-enabled ActiveGate is able to execute **both [browser as well as HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.")**.

Additionally on private locations, capacity usage is tracked separately for high-resource HTTP monitorsâthese monitors have special resource-intensive features.

To run browser monitors from a private location, you must first satisfy the engine dependencies before you install the Environment or Cluster ActiveGate. See [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for detailed instructions.

### Use cases

Private locations enable you to run monitors in your internal network when you cannot use Dynatrace [public Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") for synthetic monitoring. With private locations you can:

* Measure internal web page performance and availability.
* Measure complex internal applications with browser clickpath monitors.

Additionally, you can also:

* Measure external resources with synthetic monitors run from internal locations.
* Monitor APIs, both internal and external.


---


## Source: zremote-purpose.md


---
title: Install the zRemote module for z/OS monitoring
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose
scraped: 2026-02-16T09:18:53.723851
---

# Install the zRemote module for z/OS monitoring

# Install the zRemote module for z/OS monitoring

* Latest Dynatrace
* 1-min read
* Updated on Jul 25, 2020

The zRemote module processes binary data received from the [zLocal](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.") and routes that data, compressed and encrypted, via its local ActiveGate to Dynatrace. Hence, the zRemote module offloads much of the processing work from the [CICS, IMS, and z/OS Java code modules](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.") incurred in instrumenting subsystems and applications to an open system.

## zRemote functionality and module

If the [zRemote module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") is enabled on an ActiveGate, no other functional module can be enabled. Note that the zRemote module is more demanding in terms of [hardware and system requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring.").

## z/OS monitoring

To monitor a z/OS LPAR, including technologies such as CICS, IMS, and Java, you need an ActiveGate with the zRemote module enabled. You can install this ActiveGate on any [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.") operating system that is supported by ActiveGate.

We recommend installing the zRemote module on an IBM Z or LinuxONE mainframe, on an supported [Linux operating system](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes."), to avoid performance or security issues in z/OS monitoring.

For more details and configuration options, see [Install the zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.").


---


## Source: capabilities.md


---
title: ActiveGate purposes and functionality
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities
scraped: 2026-02-16T09:18:45.295410
---

# ActiveGate purposes and functionality

# ActiveGate purposes and functionality

* Latest Dynatrace
* 4-min read
* Updated on May 10, 2023

An ActiveGate can be used for three different use cases, which we refer to as **purposes**:

* [Route OneAgent traffic to Dynatrace, monitor cloud environments, or monitor remote technologies using extensions](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.")
* [Run Synthetic monitors from a private location](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")
* [Install the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")

Each purpose comes with a different subset of functional [modules](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). Modules should not be mixed between purposesâsuch re-configuration is not supported.

## Functionality available for the routing-monitoring ActiveGates

Functionality

Module name

x86-64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

s390 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

arm64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

Containerized deployment

[Message Routing](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#msg_routing "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Buffering and compression](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#buff_compr "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Authentication](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#auth "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Accessing sealed networks](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#sealed_net "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Memory dumps](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#mem_dump "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Memory dumps

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[AWS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#aws_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

AWS

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[Cloud Foundry monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#cf_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Cloud Foundry

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Kubernetes/OpenShift monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#k8s_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Kubernetes

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Azure monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#azure_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Azure

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Monitoring using an ActiveGate extension](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Extensions

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[Oracle database insights](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#oracle_ins "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Database insights

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Monitoring virtualized infrastructure](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#vmware "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

VMware

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Dynatrace API](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

REST API

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Log Monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#log_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Log Monitoring

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Metric ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#metric_ing "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

HTTP Metric API

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[OpenTelemetry metric ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OTLP Ingest

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[OpenTelemetry trace ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OTLP Ingest

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[OpenTelemetry log ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Log Monitoring

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[Real User Monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#rum_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Beacon forwarder

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Live Debugging](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.")

Debugging

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

## Functionality available for ActiveGates running synthetic monitors from a private location

Functionality

Module name

x86-64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

s390 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

arm64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

Containerized deployment

[Execute private HTTP monitors](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

Synthetic

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")[1](#fn-1-1-def)

[Execute private browser monitors](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

Synthetic

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")[1](#fn-1-1-def)

1

See [Containerized, auto-scalable private Synthetic locations on Kubernetes](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.").

## Functionality available for ActiveGates with the zRemote module

Functionality

Module name

x86-64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

s390 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

arm64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

Containerized deployment

[zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose#zos_mon "Learn about installing the zRemote module for z/OS monitoring.")

zRemote

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")


---


## Source: linux-activegate-hardware-and-system-requirements.md


---
title: Hardware and system requirements for routing/monitoring ActiveGates on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements
scraped: 2026-02-16T09:18:38.052575
---

# Hardware and system requirements for routing/monitoring ActiveGates on Linux

# Hardware and system requirements for routing/monitoring ActiveGates on Linux

* Latest Dynatrace
* 4-min read
* Updated on Nov 20, 2025

### Hardware and system requirements: Routing OneAgent traffic to Dynatrace, monitoring cloud environments, or monitoring remote technologies with extensions

For hardware and system requirements for other ActiveGate purposes, see:

* [Hardware and system requirements for Synthetic-enabled ActiveGates](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"), which support a subset of operating systems and are more demanding in terms of hardware and system requirements than ActiveGates that are used for routing and monitoring.
* [Hardware and system requirements for the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring."). ActiveGates running the zRemote module are more demanding in terms of hardware and system requirements than are ActiveGates that are used for routing and monitoring purposes.

Run ActiveGate on dedicated system

For optimal performance and enhanced security, we recommend installing and running ActiveGate on a dedicated system.
Utilizing ActiveGate on a dedicated system not only minimizes the risk of compromising ActiveGate authentication data but also reduces the potential for malicious configuration manipulation.

Refer to the [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") doc page for detailed log throughput characteristics on Environmental Active Gate for logs ingest API.

## Hardware requirements

You need a machine dedicated to ActiveGate that has:

* 4 GB free disk space for ActiveGate and Extensions installation, configuration, and logs for auto update purposes.
* 4 GB for ActiveGate and OneAgent cached installers and container imagesâif such will need to be stored.
* Space for dump filesâif such will need to be stored. This functionality is turned off by default, but can be turned on in ActiveGate configuration. The maximum size of the storage space is [configurable](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.")â100 GB by default.
* 600 MB + 1.5 GB (buffer) of free disk space for Extension Execution Controller logs retransmission persistence file.
* Space for extension uploadsâdepending on extensions used.
* 2 GB RAM (4 GB recommended).
* 1 dual core processor.

For large environments, you may need to use a machine with additional CPU and memory.

## Space requirements per directory

**Space allocation per directory, for installation purposes:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater executable files, libraries, and related files  
default: `/opt/dynatrace`  
relative to installation parameter: `<INSTALL>`

300 MB

ActiveGate configuration and related directories  
For Environment ActiveGate, it also contains Extensions configuration  
default: `/var/lib/dynatrace`  
relative to installation parameter: `<CONFIG>`

2 MB

For Environment ActiveGate only: Extensions executable files, libraries, and related files
default: `/opt/dynatrace/remotepluginmodule`  
relative to installation parameter: `<INSTALL>/remotepluginmodule`

1.2 GB

**Space allocation per directory, for ActiveGate operation:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater logs  
default: `/var/log/dynatrace`  
installation parameter: `<LOG>`

700 MB

ActiveGate packages directory for auto-update installer downloads  
default: `/var/lib/dynatrace/packages`  
installation parameter: `<PACKAGES_DIR>`

500 MB

ActiveGate temporary files  
default: `/var/tmp/dynatrace/gateway`  
path relative to installation parameter TEMP: `<TEMP>/gateway`

4 GB (including 3 GB for cached OneAgent installers and container images)

Dump files uploaded to ActiveGate by OneAgent  
`/var/lib/dynatrace/gateway/dump`

Functionality off by default, not configurable at installation time.  
When activated, can take configurable maximum size: default 100 GB.

For Environment ActiveGate only: ActiveGate Extensions logs, cache, run-time work area  
default: `/var/lib/dynatrace/remotepluginmodule`  
path relative to installation parameter CONFIG: `<CONFIG>/remotepluginmodule`

2 GB

For Environment ActiveGate only: ActiveGate extensions upload directory  
default: `/opt/dynatrace/remotepluginmodule/plugin_deployment`  
path relative to installation parameter INSTALL: `<INSTALL>/remotepluginmodule/plugin_deployment`

Depending on uploaded extensions

Extension Execution Controller logs retransmission persistence directory
`/var/lib/dynatrace/remotepluginmodule/agent/runtime/extensions/persistence`

Up to 600 MB by default. [1](#fn-1-1-def)

1

The reliability mechanism does not work if the requirement is not met. Extra 1.5 GB required as a buffer. For more information see [Persistence details](#persistence).

## Persistence details

The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.

### General information

* Persistent storage of data requires 2136 MB of free disk space:

  + 600 MB of free disk space to be used by the reliability mechanism
  + 1.5 GB of free disk space to be used as a buffer
* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.
* The volume is used proportionally to the load of logs ingest.
* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).

### Configuration

Windows configuration file: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

**Variable**

**Description**

`persistence.reliable_mode`

`true` - reliable mode turned on; SFM logs genereted if space requirement not met
`false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism

`persistence.total_limit_kb`

Maximum volume limit for Extensions Log Persistence in kilobytes.
By default: 600 MB
Can be modified manually if the requirement can't be met on the host.

## Supported operating systems

### Routing-monitoring ActiveGates

| Linux distribution | Versions | CPU architectures |
| --- | --- | --- |
| Amazon Linux | 2, 2023[1](#fn-linux-distribution-1-def) | ARM64 (AArch64), x86-64 |
| Oracle Linux | 8.10, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), s390, x86-64 |
| Rocky Linux | 8.10, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), x86-64 |
| SUSE Enterprise Linux | 15.6, 15.7 | ARM64 (AArch64), s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04 | ARM64 (AArch64), s390 |

1

To run ActiveGate extensions on Amazon Linux 2023, versions 315 and earlier require manual installation of the 'libcrypt.so.1' library from the 'libxcrypt-compat.rpm' package, which is not installed by default.

ActiveGate installed on the x86-64 architecture supports all functionalities. Other architectures provide only partial support. For details, see [ActiveGate purposes and functionality](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

### ActiveGates running synthetic monitors from a private location

For ActiveGates running synthetic monitors from a private location, see [Requirements for private Synthetic location: Linux: Supported operating systems](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

### ActiveGates with the zRemote module

For ActiveGates with the zRemote module, see [Install the zRemote module: System requirements: Supported operating systems](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#supported-operating-systems "Prepare and install the zRemote for z/OS monitoring.").

## System requirements

* Ensure that you have proper [network port configuration](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").
* Your operating system must handle at least 500,000 open files for the `dtuserag` user.  
  To view the system limit, execute the following command:

  ```
  [user@host]# cat /proc/sys/fs/file-max
  ```

  Also, it may be that you've checked out [too many open files in Linux](/docs/ingest-from/dynatrace-activegate#too-many-open-files-in-linux "Understand the basic concepts related to ActiveGate.").
* Your operating system must have at least 20,000 processes available to the `dtuserag` user.  
  To view the system limit, execute the following command:

  ```
  [user@host]# cat /proc/sys/kernel/pid_max
  ```
* The ActiveGate Linux installer doesn't support ACL (Access Control List). ACL rules may prohibit access to installer-created directories and files, making the ActiveGate fail to start. If you use the ACL, rules related to the installation directories defined in the following parameters should be disabled:

  ```
  INSTALL=



  CONFIG=



  LOG=



  TEMP=



  PACKAGES_DIR=
  ```

## Sizing guide

The following table represents the machine instance size requirement based on number of OneAgents communicating with the ActiveGate. On each host, OneAgent is performing eight monitoring tasks:

* Infrastructure monitoring
* Log monitoring
* Full-stack monitoring of 3 Apache Tomcat instances
* Full-stack monitoring of 2 Apache HTTP Server instances
* Extension monitoring

The real number of hosts may be different depending on the monitored technologies in your environment. It is recommended that the machine on which ActiveGate is running should not exceed 50% CPU and 80% memory. Additionally, it must be assumed that ActiveGates may be inoperable during updates, restarts or short communication problems. In order to ensure high availability, operating ActiveGates should be able to takeover traffic of the unavailable ActiveGates

### x86-64 architecture

The C6i machine instances and the estimates:

Instance

vCPU

Mem (GiB)

Storage

Dedicated EBS bandwidth (Mbps)

Network performance

Estimated number of hosts

c6i.large

2

3.75

EBS-Only

500

Moderate

800

c6i.xlarge

4

7.5

EBS-Only

750

High

1800

c6i.2xlarge

8

15

EBS-Only

1,000

High

2500

### ARM64 (AArch64) architecture

The C7g machine instances and the estimates:

Instance

vCPU

Mem (GiB)

Storage

Dedicated EBS bandwidth (Mbps)

Network performance

Estimated number of hosts

c7g.large

2

3.75

EBS-Only

500

Moderate

1300

c7g.xlarge

4

7.5

EBS-Only

750

High

2700

c7g.2xlarge

8

15

EBS-Only

1,000

High

5500

### s390 architecture

Machine sizes and estimates:

Machine size

CPU

Mem (GiB)

Estimated number of hosts

S

2

4

800

M

4

8

1500


---


## Source: linux.md


---
title: ActiveGate on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/installation/linux
scraped: 2026-02-16T09:18:41.414843
---

# ActiveGate on Linux

# ActiveGate on Linux

* Latest Dynatrace
* 1-min read
* Published Apr 09, 2021

Dynatrace supports ActiveGate installation on Linux.

### Requirements

[ActiveGate hardware and system requirements for Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

### Defaults

[Default installation settings](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux")

### Installation

[Install an Environment ActiveGate on Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Linux.")

### Customization of installation

[Customize ActiveGate installation on Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.")


---


## Source: windows-activegate-hardware-and-system-requirements.md


---
title: Hardware and system requirements for routing/monitoring ActiveGates on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements
scraped: 2026-02-16T09:18:50.391933
---

# Hardware and system requirements for routing/monitoring ActiveGates on Windows

# Hardware and system requirements for routing/monitoring ActiveGates on Windows

* Latest Dynatrace
* 2-min read
* Published Oct 09, 2018

### Hardware and system requirements: Routing OneAgent traffic to Dynatrace, monitoring cloud environments, or monitoring remote technologies with extensions

For hardware and system requirements for other ActiveGate purposes, see:

* [Hardware and system requirements for Synthetic-enabled ActiveGates](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"), which support a subset of operating systems and are more demanding in terms of hardware and system requirements than are ActiveGates that are used for routing and monitoring.
* [Hardware and system requirements for the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring."). ActiveGates running the zRemote module are more demanding in terms of hardware and system requirements than are ActiveGates that are used for routing and monitoring.

Run ActiveGate on dedicated system

For optimal performance and enhanced security, we recommend installing and running ActiveGate on a dedicated system.
Utilizing ActiveGate on a dedicated system not only minimizes the risk of compromising ActiveGate authentication data but also reduces the potential for malicious configuration manipulation.

## Hardware requirements

You need a machine dedicated to ActiveGate that has:

* 4 GB free disk space for ActiveGate and Extensions installation, configuration, and logs for auto update purposes.
* 4 GB for ActiveGate and OneAgent cached installers and container imagesâif such will need to be stored.
* Space for dump filesâif such will need to be stored. This functionality is turned off by default, but can be turned on in ActiveGate configuration. The maximum size of the storage space is [configurable](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.")â100 GB by default.
* 600 MB + 1.5 GB (buffer) of free disk space for Extension Execution Controller logs retransmission persistence file.
* Space for extension uploadsâdepending on extensions used.
* 2 GB RAM (4 GB recommended).
* 1 dual core processor.

For large environments, you may need to use a machine with additional CPU and memory.

## Space requirements per directory

**Space allocation per directory, for installation purposes:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater executable files, libraries, and related files  
`%PROGRAMFILES%\dynatrace\gateway`  
relative to installation parameter: `<INSTALL>\gateway`  
also configurable in GUI during installation

300 MB

ActiveGate configuration and related directories  
For Environment ActiveGate, it also contains Extensions configuration  
`%PROGRAMDATA%\dynatrace`

2 MB

For Environment ActiveGate only: Extensions executable files, libraries, and related files
`%PROGRAMFILES%\dynatrace\remotepluginmodule`  
relative to installation parameter: `<INSTALL>\remotepluginmodule`  
also configurable in GUI during installation

850 MB

**Space allocation per directory, for ActiveGate operation:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater logs  
ActiveGate packages directory for auto-update installer downloads  
`%PROGRAMDATA%\dynatrace`

1.2 GB

ActiveGate temporary files  
`%PROGRAMDATA%\dynatrace\gateway\tmp`

4 GB (including 3 GB for cached OneAgent installers and container images)

Dump files uploaded to ActiveGate by OneAgent  
`%PROGRAMDATA%\dynatrace\gateway\dump`

Functionality off by default.
When activated, can take configurable maximum size: default 100 GB.

For Environment ActiveGate only: ActiveGate Extensions logs, cache, run-time work area  
`%PROGRAMDATA%\dynatrace\remotepluginmodule`

2 GB

For Environment ActiveGate only: ActiveGate extensions upload directory  
`%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment`

Depending on uploaded extensions

Extension Execution Controller logs retransmission persistence directory
`%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\runtime\extensions\persistence`

Up to 600 MB by default. [1](#fn-1-1-def)

1

The reliability mechanism does not work if the requirement is not met. Extra 1.5 GB required as a buffer. For more information see [Persistence details](#persistence).

## Persistence details

The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.

### General information

* Persistent storage of data requires 2136 MB of free disk space:

  + 600 MB of free disk space to be used by the reliability mechanism
  + 1.5 GB of free disk space to be used as a buffer
* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.
* The volume is used proportionally to the load of logs ingest.
* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).

### Configuration

Windows configuration file: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

**Variable**

**Description**

`persistence.reliable_mode`

`true` - reliable mode turned on; SFM logs genereted if space requirement not met
`false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism

`persistence.total_limit_kb`

Maximum volume limit for Extensions Log Persistence in kilobytes.
By default: 600 MB
Can be modified manually if the requirement can't be met on the host.

## Supported operating systems

Supported operating systems:

| Windows OS | Versions | CPU architectures |
| --- | --- | --- |
| Windows | 10, 11 | x86-64 |
| Windows Server | 2016, 2019, 2022, 2025 | x86-64 |

## System requirements

* ActiveGate supports only operating systems running on the x86-64 architecture (64-bit Intel/AMD).
* Ensure that you have proper [network port configuration](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").
* ActiveGate installation is not supported on Windows with a disabled `NT AUTHORITY\LocalService` account.

## AWS sizing guide

The following table represents the machine instance size requirement based on number of OneAgents communicating with the ActiveGate. On each host, OneAgent is performing eight monitoring tasks:

* Infrastructure monitoring
* Log monitoring
* Full-stack monitoring of 3 Apache Tomcat instances
* Full-stack monitoring of 2 Apache HTTP Server instances
* Extension monitoring

The real number of hosts may be different depending on the monitored technologies in your environment. It is recommended that the machine on which ActiveGate is running should not exceed 50% CPU and 80% memory. Additionally, it must be assumed that ActiveGates may be inoperable during updates, restarts or short communication problems. In order to ensure high availability, operating ActiveGates should be able to takeover traffic of the unavailable ActiveGates

### x86-64 architecture

The C6i machine instances and the estimates:

Instance

vCPU

Mem (GiB)

Storage

Dedicated EBS bandwidth (Mbps)

Network performance

Estimated number of hosts

c6i.large

2

3.75

EBS-Only

500

Moderate

800

c6i.xlarge

4

7.5

EBS-Only

750

High

1800

c6i.2xlarge

8

15

EBS-Only

1,000

High

2500


---


## Source: windows.md


---
title: ActiveGate on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/installation/windows
scraped: 2026-02-16T09:18:55.317096
---

# ActiveGate on Windows

# ActiveGate on Windows

* Latest Dynatrace
* 1-min read
* Updated on Feb 26, 2025

Dynatrace supports ActiveGate installation on Windows.

### Requirements

[ActiveGate hardware and system requirements for Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

### Defaults

[Default installation settings](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Learn about the default settings with which ActiveGate is installed on Windows.")

### Installation

[Install an Environment ActiveGate on Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Windows.")

### Customization of installation

[Customize ActiveGate installation on Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Learn about the parameters that you can use with ActiveGate on Windows.")


---


## Source: supported-connectivity-schemes-for-activegates.md


---
title: Supported connectivity schemes for ActiveGates
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates
scraped: 2026-02-16T09:18:48.737869
---

# Supported connectivity schemes for ActiveGates

# Supported connectivity schemes for ActiveGates

* Latest Dynatrace
* 4-min read
* Published Jul 17, 2018

Dynatrace requires certain ports and paths to be opened and accessible through the monitored infrastructure, firewalls and other components. The ports are [configurable](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#com-compuware-apm-webserver "Learn which ActiveGate properties you can configure based on your needs and requirements.") and the default values are shown here.

## Dynatrace SaaS connectivity scheme

All possible connections for the SaaS connectivity scheme, with preferred and alternative paths are shown below.

The **solid arrows** indicate the preferred paths. For example, OneAgent will connect to an Environment ActiveGate, if one is present. It will, however, connect to a the Dynatrace Saas Cluster directly, if no connection to an Environment ActiveGate is possible.
The **direction of arrows** in the diagrams indicates which component initiates the connection.

![Dynatrace SaaS connectivity scheme](https://dt-cdn.net/images/connectivity-saas-003-1200-822497778d.png)

## Port usage

* Environment ActiveGate receives connections on port 9999.

* Dynatrace SaaS Cluster receives connections on port 443.

If you run [Browser monitors](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") or [HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") from private Synthetic locations, you need to make sure the Synthetic-enabled ActiveGate has access to the tested resource. If you use ActiveGate extensions, you need to make sure the ActiveGate executing the extensions has access to the monitored technology.

Connection

**[Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")** configuration means that OneAgents will prefer to communicate with ActiveGates from the same zone, before connecting to ActiveGates outside of the active zone.

## Proxy and load balancer configuration

All Dynatrace components (OneAgents, ActiveGates, Dynatrace Cluster) detect their hostnames and distribute them as communication endpoints among each other to achieve the highest possible connection robustness.  
This works automatically, unless there are networking devices (proxies, load balancers) in your environment, which should be taken into account, and of which Dynatrace is not aware.

The diagram below shows all possible proxy and load balancer (reverse proxy) placements for an ActiveGate deployment. For simplicity, direct connectionsâthose that are not through proxies or load balancersâare not shown in this diagram. Alternative connections (those that connect through one or more proxies or load balancers), are shown as dashed lines.

* If there is a load balancer between OneAgents and an ActiveGate, you should specify the load balancer's address as the [`dnsEntryPoint`](/docs/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Configure ActiveGate properties to set up a reverse proxy or a load balancer for OneAgent.") property in the ActiveGate configuration.
* If there is a load balancer between ActiveGate and the next communication endpoint that traffic should be routed through, configure [`seedServerUrl` and `ignoreClusterRuntimeInfo`](/docs/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.")
* If a proxy is used to reach the Dynatrace Cluster or any of the monitored clouds, [configure a proxy](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.").

![Proxy and load balancer placements for ActiveGate deployments](https://dt-cdn.net/images/proxy-rev-proxy-005-1018-c916f384ca.png)

## ActiveGate headers

You can configure the ActiveGate headers in your firewall.

Header

Value

`User-Agent`

* Environment ActiveGate:

  `ruxit/<dynatrace-version> <activegate-instance-id> <environment-id>`

  Example values

  Environment and Multi-environment ActiveGate:  
  `ruxit/1.229.163.20211109-103203 0x37badd8e c04442b4-7ea6-4ec4-a5c4-7f94c7cf25fa`

  Cluster ActiveGate:  
  `ruxit/1.229.163.20211109-103203 0x37badd8e`
* HTTP monitors:

  `DynatraceSynthetic/<dynatrace-version>`

  Example value

  `DynatraceSynthetic/1.258.0.20221207-142354`
* Browser monitors:

  `RuxitSynthetic/<dynatrace-version>`

  Example value

  `Mozilla/5.0 (Windows NT 6.3;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36 RuxitSynthetic/1.258.0.20221207-142354`

`dynatrace-gateway-type`

* Environment ActiveGate: `PRIVATE`
* Managed or SaaS ActiveGate: `PUBLIC`

* Multi-environment ActiveGate: `MULTI_TENANT`

`Authorization`

`Basic <TOKEN>`

## Related topics

* [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")


---
