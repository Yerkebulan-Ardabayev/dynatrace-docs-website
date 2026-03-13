---
title: Monitor Amazon Elastic Compute Cloud (EC2)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2
scraped: 2026-03-06T21:17:42.722106
---

# Мониторинг Amazon Elastic Compute Cloud (EC2)

# Мониторинг Amazon Elastic Compute Cloud (EC2)

* Classic
* How-to guide
* 1-min read
* Published Jan 16, 2023

## Возможности

* Полностековый мониторинг на базе OneAgent
* Расширенная поддержка метаданных EC2, включая регионы и другое
* [Пакет AWS Systems Manager Distributor](aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor.md "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package.") для упрощённого развёртывания OneAgent
* [Интеграция с CloudWatch](../integrate-with-aws/cloudwatch-metrics.md "Integrate metrics from Amazon CloudWatch.") для получения метрик, свойств и тегов из AWS

## Интеграция OneAgent для полностекового мониторинга

Мониторинг экземпляров Amazon EC2 работает сразу из коробки. Просто запустите стандартные установщики OneAgent для [Linux](../../dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux.md "Learn how to download and install Dynatrace OneAgent on Linux.") и [Windows](../../dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows.md "Learn how to download and install Dynatrace OneAgent on Windows.").

Кроме того, вы можете использовать любой инструмент управления инфраструктурой, например Terraform, для интеграции OneAgent на ваших виртуальных машинах. Dynatrace также предоставляет интеграцию с [AWS Systems Manager Distributor](aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor.md "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package."), позволяющую распространять и автоматически развёртывать OneAgent на экземплярах EC2.
