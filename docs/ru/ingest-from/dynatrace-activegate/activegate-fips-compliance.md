---
title: ActiveGate FIPS compliance
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance
scraped: 2026-02-26T21:29:26.721520
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

1

excluding [Extension Execution Controller module](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Learn about the routing and monitoring capabilities and uses of ActiveGate.") (same as regular, non-FIPS ActiveGate).

2

refer to [Requirements and limitations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#fips-compliant-limitation "Learn how to create a private location for synthetic monitoring.") for Synthetic FIPS compliance.

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