---
title: Hardware requirements for cloud deployments
source: https://docs.dynatrace.com/managed/managed-cluster/installation/managed-cloud-requirements
---

# Hardware requirements for cloud deployments

# Hardware requirements for cloud deployments

* Reference
* 3-min read
* Updated on May 08, 2026

The following tables list the required virtual machine sizes for deploying Dynatrace Managed on the most popular cloud providers. Maintain a vCPU to RAM (random access memory) ratio of 1:8 to optimize performance.

## Amazon Web Services

For details on the instance types listed below, see [Amazon EC2 R6i Instances﻿](https://aws.amazon.com/ec2/instance-types/r6i/).

| **Node type** | **Size** | **vCPU** | **Memory** (GiB) |
| --- | --- | --- | --- |
| Micro | r6i.xlarge | 4 | 32 |
| Small | r6i.2xlarge | 8 | 64 |
| Medium | r6i.4xlarge | 16 | 128 |
| Large | r6i.8xlarge | 32 | 256 |
| Xlarge | r6i.16xlarge | 64 | 512 |

## Microsoft Azure

For details on the instance types listed below, see [Linux Virtual Machines pricing﻿](https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/linux/).

| **Node type** | **Size** | **vCPU** | **Memory** (GiB) |
| --- | --- | --- | --- |
| Micro | E4as v6 | 4 | 32 GiB |
| Small | E8as v6 | 8 | 64 GiB |
| Medium | E16as v6 | 16 | 128 GiB |
| Large | E32as v6 | 32 | 256 GiB |
| Xlarge | E64as v6 | 64 | 512 GiB |

## Google Cloud

For details on the instance types listed below, see [Google Compute Products﻿](https://cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family).

| **Node type** | **Size** | **vCPU** | **Memory** (GiB) |
| --- | --- | --- | --- |
| Micro | n4-highmem-4 | 4 | 32 GB |
| Small | n4-highmem-8 | 8 | 64 GB |
| Medium | n4-highmem-16 | 16 | 128 GB |
| Large | n4-highmem-32 | 32 | 256 GB |
| Xlarge | n4-highmem-64 | 64 | 512 GB |