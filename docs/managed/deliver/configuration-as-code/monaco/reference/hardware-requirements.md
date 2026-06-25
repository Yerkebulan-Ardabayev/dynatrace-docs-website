---
title: Hardware requirements for Dynatrace Monaco CLI
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/reference/hardware-requirements
scraped: 2026-05-12T12:02:56.741394
---

# Hardware requirements for Dynatrace Monaco CLI

# Hardware requirements for Dynatrace Monaco CLI

* Reference
* 5-min read
* Updated on Sep 12, 2023

This page provides an overview of the hardware requirements for Dynatrace Configuration as Code via Monaco.

## Required memory

The main hardware requirement of the Dynatrace Monaco CLI is memory.

When executing in a container with a hard memory limit or limited physical hardware, make sure to set a reasonably high memory limit or ensure that swap space is available.

The required memory is mostly defined by the number of configurations and the size of their JSON template files. The following tables give you an idea of memory requirements for sample project sizes; your project might need more or less memory.

Note that the CLI in version 2.9.0 and earlier has higher memory requirements.

CLI version 2.9.1+

CLI version 2.9.0 or earlier

Dynatrace Monaco CLI version 2.9.1+

| Project size / Number of configurations | Storage size on disk | Required memory (RAM+swap) |
| --- | --- | --- |
| 125 | 800 kB | 5 MB |
| 625 | 3.2 MB | 15 MB |
| 2500 | 12.8 MB | 40 MB |
| 5000 | 25.5 MB | 80 MB |
| 10000 | 50.9 MB | 160 MB |
| 25000 | 127.3 MB | 310 MB |
| 50000 | 254.5 MB | 600 MB |
| 100000 | 509 MB | 1200 MB |

For larger projects, follow these rules for estimating the required memory for a deployment:

1. Available memory should be around 2.5 times larger than the storage required by your configurations on disk.
2. Around 15kB of memory is required per configuration in your project.

Both of these measures are better applicable for larger projects, where memory needs unrelated to configuration are less noticeable.

Dynatrace Monaco CLI version 2.9.0 or earlier

| Project size / Number of configurations | Storage size on disk | Required memory (RAM+swap) |
| --- | --- | --- |
| 125 | 800 kB | 5 MB |
| 625 | 3.2 MB | 20 MB |
| 2500 | 12.8 MB | 76.2 MB |
| 5000 | 25.5 MB | 152 MB |
| 10000 | 50.9 MB | 303 MB |
| 25000 | 127.3 MB | 757 MB |
| 50000 | 254.5 MB | 1500 MB |
| 100000 | 509 MB | 3000 MB |

### Memory limits

You can configure a soft memory limit for the Dynatrace Monaco CLI by setting the `GOMEMLIMIT` [environment variableï»¿](https://pkg.go.dev/runtime#hdr-Environment_Variables).

`GOMEMLIMIT` is a numeric value with an optional unit suffix of `B`, `KiB`, `MiB`, `GiB`, or `TiB`.
If no suffix is supplied, the value is assumed to be in bytes (`B`).

For example, to set a limit of 3 gibibytes, set the environment variable as `GOMEMLIMIT=3GiB`.

Linux/macOS

Windows

```
GOMEMLIMIT=3GiB monaco deploy manifest.yaml
```

```
$env:GOMEMLIMIT=3GiB



monaco deploy manifest.yaml
```

As a soft limit, this limit can be exceeded if your deployment needs more memory. Setting too low a limit, however, will result in increased runtime, as more time is spent to free memory when the limit is exceeded. See the table above for estimated memory requirements.

#### Differences in CLI versions

* Dynatrace Monaco CLI version 2.8.0+ A default memory limit of 2GiB is applied. To change it, set `GOMEMLIMIT`.
* Dynatrace Monaco CLI version 2.7.0 or earlier No default memory limit is applied. The Dynatrace Monaco CLI may consume excessive memory. To apply a memory limit, set `GOMEMLIMIT`.

## CPU impact on deployment times

Available CPU mostly impacts deployment time needed and, unlike memory, doesn't impose hard limits; on more limited hardware, deployments simply take more time.

For example, deploying from a container limited to a single vCPU takes significantly longer than one with several available vCPUs or running directly on a system with a multi-core processor.

The following tables give a rough overview of how the number of configurations impacts deployment times. This merely illustrates the relationship between project size and deployment time and probably won't match deployment time on your specific hardware.

* With Dynatrace Monaco CLI version 2.7.0+, the deployment times are measured for parallel deployments, which are available by default.
* With Dynatrace Monaco CLI version 2.6.0 or earlier, deployment is fully sequential and therefore notably slower than with newer versions.

CLI version 2.7.0+

CLI version 2.6.0 or earlier

Dynatrace Monaco CLI version 2.7.0+

This table demonstrates that deployment time doesn't grow linearly with the size of your projects. This is because of the behavior of the Dynatrace API as the number of requests and existing configurations increasesâthis causes increased rate limiting and processing time when adding configurations.

| Project size / Number of configurations | Estimated deployment time |
| --- | --- |
| 125 | 20 s |
| 625 | 35 s |
| 2500 | 2 min 30 s |
| 5000 | 3 min 45 s |
| 10000 | 10 min |
| 25000 | 50 min |

Dynatrace Monaco CLI version 2.6.0 or earlier

| Project size / Number of configurations | Estimated deployment time |
| --- | --- |
| 125 | 20 s |
| 625 | 2 min |
| 2500 | 8 min 20 s |
| 5000 | 18 min 20 s |