---
title: Аппаратные требования для облачных развёртываний
source: https://docs.dynatrace.com/managed/managed-cluster/installation/managed-cloud-requirements
scraped: 2026-05-12T11:53:34.447682
---

# Аппаратные требования для облачных развёртываний

# Аппаратные требования для облачных развёртываний

* Reference
* 3-min read
* Updated on May 08, 2026

В следующих таблицах указаны необходимые размеры виртуальных машин для развёртывания Dynatrace Managed у наиболее популярных облачных провайдеров. Для оптимальной производительности поддерживайте соотношение vCPU к RAM 1:8.

## Amazon Web Services

Подробнее о типах экземпляров, перечисленных ниже, см. в разделе [Amazon EC2 R6i Instances](https://aws.amazon.com/ec2/instance-types/r6i/).

| **Тип узла** | **Размер** | **vCPU** | **Память** (ГиБ) |
| --- | --- | --- | --- |
| Micro | r6i.xlarge | 4 | 32 |
| Small | r6i.2xlarge | 8 | 64 |
| Medium | r6i.4xlarge | 16 | 128 |
| Large | r6i.8xlarge | 32 | 256 |
| Xlarge | r6i.16xlarge | 64 | 512 |

## Microsoft Azure

Подробнее о типах экземпляров, перечисленных ниже, см. в разделе [Linux Virtual Machines pricing](https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/linux/).

| **Тип узла** | **Размер** | **vCPU** | **Память** (ГиБ) |
| --- | --- | --- | --- |
| Micro | E4as v6 | 4 | 32 GiB |
| Small | E8as v6 | 8 | 64 GiB |
| Medium | E16as v6 | 16 | 128 GiB |
| Large | E32as v6 | 32 | 256 GiB |
| Xlarge | E64as v6 | 64 | 512 GiB |

## Google Cloud

Подробнее о типах экземпляров, перечисленных ниже, см. в разделе [Google Compute Products](https://cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family).

| **Тип узла** | **Размер** | **vCPU** | **Память** (ГиБ) |
| --- | --- | --- | --- |
| Micro | n4-highmem-4 | 4 | 32 GB |
| Small | n4-highmem-8 | 8 | 64 GB |
| Medium | n4-highmem-16 | 16 | 128 GB |
| Large | n4-highmem-32 | 32 | 256 GB |
| Xlarge | n4-highmem-64 | 64 | 512 GB |