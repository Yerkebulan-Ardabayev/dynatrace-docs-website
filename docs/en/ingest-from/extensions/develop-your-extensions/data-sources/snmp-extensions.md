---
title: SNMP data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions
scraped: 2026-02-28T21:27:49.403689
---

# SNMP data source

# SNMP data source

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Mar 22, 2023

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP monitored devices.

We also provide an SNMP traps data source reporting a single metric that counts the number of traps sent by a defined source during a defined interval. For more information, see [SNMP traps data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmptraps-extensions "Create an SNMP traps extension using the Dynatrace Extensions framework.").

We assume the following:

* You possess sufficient SNMP subject matter expertise to create an SNMP extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

Learn the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Supported Dynatrace versions

* Dynatrace version 1.215+
* Environment ActiveGate version 1.215+

## Supported SNMP versions

* SNMP v2c
* SNMP v3

## Supported authentication

### SNMP v2c

Community strings.

### SNMP v3

For SNMP v3, the SNMP data source supports the `NoAuthNoPriv`, `authNoPriv`, and `authPriv` security levels and the following authentication protocols:

#### `authNoPriv`

| Protocol |  | RFC |
| --- | --- | --- |
| MD5 | HMAC-96-MD5 | [rfc3414ï»¿](https://tools.ietf.org/html/rfc3414) |
| SHA | HMAC-96-SHA | [rfc3414ï»¿](https://tools.ietf.org/html/rfc3414) |
| SHA224 | HMAC-128-SHA-224 | [rfc7860ï»¿](https://tools.ietf.org/html/rfc7860) |
| SHA256 | HMAC-192-SHA-256 | [rfc7860ï»¿](https://tools.ietf.org/html/rfc7860) |
| SHA384 | HMAC-256-SHA-384 | [rfc7860ï»¿](https://tools.ietf.org/html/rfc7860) |
| SHA512 | HMAC-384-SHA-512 | [rfc7860ï»¿](https://tools.ietf.org/html/rfc7860) |

#### `authPriv`

| Protocol |  | RFC | Notes |
| --- | --- | --- | --- |
| DES | CBC-DES | [rfc3414ï»¿](https://tools.ietf.org/html/rfc3414) |  |
| AES | CFB128-AES-128 | [rfc3826ï»¿](https://tools.ietf.org/html/rfc3826) |  |
| AES192[1](#fn-1-1-def) |  | n/a | Blumenthal key extension |
| AES256[1](#fn-1-1-def) |  | n/a | Blumenthal key extension |
| AES192C[1](#fn-1-1-def) |  | n/a | Reeder key extension |
| AES256C[1](#fn-1-1-def) |  | n/a | Reeder key extension |

1

These encryption algorithms are not officially specified, but they are often supported by network devices. See [SNMPv3 with AES-256ï»¿](https://www.snmp.com/snmpv3/snmpv3_aes256.shtml).

To learn how to define authentication in your monitoring configuration, see [SNMP authentication](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmp-schema-reference#authentication "Learn about SNMP extensions in the Extensions framework.").

## Hardware requirements

SNMP monitoring with the Extensions framework is performed by an ActiveGate. The requirements for the hosts depend on the following:

* Number of polled devices.
* Number of metric ingestion protocol lines ingested per polling interval (1 minute). A unique metric-dimension combination (tuple) results in a single line.
* Whether you configured the [EEC](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.") performance profile to high limits.

Depending on the number of devices and ingested lines, the ActiveGates performing SNMP monitoring need to meet the following hardware requirements:

| Host (EC2 instance type) | CPUs | RAM (GB) | SNMP devices | Ingested lines |
| --- | --- | --- | --- | --- |
| XS (`c5.large`) | 2 | 4 | 900 | 142,000 |
| S (`c5.xlarge`) | 4 | 8 | 1,800 | 284,000 |
| M (`c5.2xlarge`) | 8 | 16 | 4,000 | 632,000 |
| L (`c5.4xlarge`) | 16 | 32 | 6,000 | 940,000 |

The estimated limits for the numbers of SNMP devices and ingested lines were determined in our internal tests. The actual values might vary depending on the complexity of your monitoring.

For example, the SNMP devices used in our tests were equipped with 20 communication interfaces. The actual number of interfaces has a direct impact on CPU usage and memory consumption.