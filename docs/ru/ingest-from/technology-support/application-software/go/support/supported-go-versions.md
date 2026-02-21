---
title: Supported Go versions
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/go/support/supported-go-versions
scraped: 2026-02-21T21:12:39.776352
---

# Supported Go versions

# Supported Go versions

* Latest Dynatrace
* 7-min read
* Updated on Feb 06, 2026

Whenever a new Go major version is released, Dynatrace adds support for that version. Support for each minor version is
added tooâsee [Version matrix](#go-version-matrix) for more details.

The [Go release policyï»¿](https://dt-url.net/uos3rmi) supports the last two major Go versions. However, Dynatrace decided
to support each Go version at least half a year longer so that you have enough time for upgrades.

### Official [Golang toolchainï»¿](https://dt-url.net/go)

Go version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

1.25

2025-08-12

2026-08-12

1.325

-

2027-08-12

Supported

1.24

2025-02-11

2026-02-11

1.311

-

2027-02-11

Supported

1.23

2024-08-13

2025-08-13

1.301

-

2026-08-13

Supported

1.22

2024-02-06

2025-02-06

1.287

-

2026-02-28

Supported

### Golang toolchain with FIPS ([openssl-fipsï»¿](https://dt-url.net/golang-fips)) modifications

Prerequisites

* **Go FIPS** OneAgent feature.

  To enable the feature, go to **Settings** > **Preferences** > **OneAgent features** and turn on **Go FIPS**.

Go version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

1.25.3

2025-08-12

2026-08-12

1.331

-

2027-08-12

Supported

1.24.6

2025-02-11

2026-02-11

1.325

-

2027-02-11

Supported

1.24.4

2025-02-11

2026-02-11

1.323

-

2027-02-11

Supported

1.23.9

2024-08-13

2025-08-13

1.323

-

2026-08-13

Supported

1.23.6

2024-08-13

2025-08-13

1.315

-

2026-08-13

Supported

1.22.9

2024-02-06

2025-02-06

1.309

-

2026-02-28

Supported

1.22.7

2024-02-06

2025-02-06

1.307

-

2026-02-28

Supported

## Version matrix

Each version range defines Go versions for which OneAgent has built-in support. The upper bound in parentheses specifies
the latest version that may be supported via [external metadata](#external-metadata).

| OneAgent versions | Go 1.22 | Go 1.23 | Go 1.24 | Go 1.25 |
| --- | --- | --- | --- | --- |
| v1.287 | 1.22.0 (1.22.5) |  |  |  |
| v1.289 | 1.22.0 - 1.22.1 (1.22.6) |  |  |  |
| v1.291 | 1.22.0 - 1.22.2 (1.22.6) |  |  |  |
| v1.293 | 1.22.0 - 1.22.3 (1.22.8) |  |  |  |
| v1.295 | 1.22.0 - 1.22.4 (1.22.8) |  |  |  |
| v1.297 | 1.22.0 - 1.22.5 (1.22.10) |  |  |  |
| v1.299 | 1.22.0 - 1.22.5 (1.22.12) |  |  |  |
| v1.301 | 1.22.0 - 1.22.6 (1.22.12) | 1.23.0 (1.23.6) |  |  |
| v1.303 | 1.22.0 - 1.22.8 (1.22.12) | 1.23.0 - 1.23.2 (1.23.8) |  |  |
| v1.305 | 1.22.0 - 1.22.8 (1.22.12) | 1.23.0 - 1.23.2 (1.23.8) |  |  |
| v1.307 | 1.22.0 - 1.22.10 (1.22.12) | 1.23.0 - 1.23.4 (1.23.9) |  |  |
| v1.309 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.6 (1.23.10) |  |  |
| v1.311 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.6 (1.23.11) | 1.24.0 (1.24.5) |  |
| v1.313 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.8 (1.23.12) | 1.24.0 - 1.24.2 (1.24.6) |  |
| v1.315 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.8 (1.23.12) | 1.24.0 - 1.24.2 (1.24.7) |  |
| v1.317 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.9 (1.23.12) | 1.24.0 - 1.24.3 (1.24.9) |  |
| v1.319 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.10 (1.23.12) | 1.24.0 - 1.24.4 (1.24.10) |  |
| v1.321 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.11 (1.23.12) | 1.24.0 - 1.24.5 (1.24.11) |  |
| v1.323 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.6 (1.24.12) |  |
| v1.325 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.7 (1.24.13) | 1.25.0 - 1.25.1 (1.25.7) |
| v1.327 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.9 (1.24.13) | 1.25.0 - 1.25.3 (1.25.7) |
| v1.329 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.10 (1.24.13) | 1.25.0 - 1.25.4 (1.25.7) |
| v1.331 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.11 (1.24.13) | 1.25.0 - 1.25.5 (1.25.7) |

### Older versions

| OneAgent versions | Go 1.18 | Go 1.19 | Go 1.20 | Go 1.21 |
| --- | --- | --- | --- | --- |
| v1.239 | 1.18.0 (1.18.5) |  |  |  |
| v1.241 | 1.18.0 - 1.18.1 (1.18.5) |  |  |  |
| v1.243 | 1.18.0 - 1.18.2 (1.18.7) |  |  |  |
| v1.245 | 1.18.0 - 1.18.3 (1.18.8) |  |  |  |
| v1.247 | 1.18.0 - 1.18.3 (1.18.10) |  |  |  |
| v1.249 | 1.18.0 - 1.18.5 (1.18.10) | 1.19.0 (1.19.5) |  |  |
| v1.251 | 1.18.0 - 1.18.5 (1.18.10) | 1.19.0 (1.19.5) |  |  |
| v1.253 | 1.18.0 - 1.18.7 (1.18.10) | 1.19.0 - 1.19.2 (1.19.7) |  |  |
| v1.255 | 1.18.0 - 1.18.7 (1.18.10) | 1.19.0 - 1.19.2 (1.19.7) |  |  |
| v1.257 | 1.18.0 - 1.18.8 (1.18.10) | 1.19.0 - 1.19.3 (1.19.8) |  |  |
| v1.259 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.5 (1.19.9) |  |  |
| v1.261 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.5 (1.19.10) |  |  |
| v1.263 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.7 (1.19.11) | 1.20.0 - 1.20.2 (1.20.6) |  |
| v1.265 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.7 (1.19.12) | 1.20.0 - 1.20.2 (1.20.7) |  |
| v1.267 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.8 (1.19.13) | 1.20.0 - 1.20.3 (1.20.8) |  |
| v1.269 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.9 (1.19.13) | 1.20.0 - 1.20.4 (1.20.10) |  |
| v1.271 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.10 (1.19.13) | 1.20.0 - 1.20.5 (1.20.11) |  |
| v1.273 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.11 (1.19.13) | 1.20.0 - 1.20.6 (1.20.12) |  |
| v1.275 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.12 (1.19.13) | 1.20.0 - 1.20.7 (1.20.13) |  |
| v1.277 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.8 (1.20.14) | 1.21.0 - 1.21.1 (1.21.7) |
| v1.279 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.10 (1.20.14) | 1.21.0 - 1.21.3 (1.21.8) |
| v1.281 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.11 (1.20.14) | 1.21.0 - 1.21.4 (1.21.9) |
| v1.283 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.12 (1.20.14) | 1.21.0 - 1.21.5 (1.21.10) |
| v1.285 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.13 (1.20.14) | 1.21.0 - 1.21.6 (1.21.11) |
| v1.287 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.7 (1.21.12) |
| v1.289 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.8 (1.21.13) |
| v1.291 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.9 (1.21.13) |
| v1.293 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.10 (1.21.13) |
| v1.295 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.11 (1.21.13) |
| v1.297 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.12 (1.21.13) |
| v1.299 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.12 (1.21.13) |
| from v1.301 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.13 |

## External metadata

OneAgent can support newer Go versions by requesting external metadata from the Dynatrace Cluster. After OneAgent has
received the external metadata, it can instrument an application that is based on a Go version for which OneAgent
doesn't have built-in support. A restart of the Go process is required.

The [version matrix](#go-version-matrix), therefore, has two different upper bounds in each version range. The built-in
Go versions are always supported, while the upper bound in parentheses may be supported if OneAgent can get the required
external metadata from the Dynatrace Cluster.

External metadata is published independently of the OneAgent release cycle and OneAgent will always receive the latest
available external metadata from the Dynatrace Cluster. This also means that in a staged environment, applications may
be instrumented in a later stage that were not instrumented in an earlier stage, because new metadata became available
in the meantime. If this behavior is undesirable, disable the OneAgent feature **Go external metadata** so that external
metadata is not used. You can find OneAgent features at **Settings** > **Preferences** > **OneAgent features**.