---
title: Мониторинг Amazon Elastic Compute Cloud (EC2)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2
scraped: 2026-03-06T21:17:42.722106
---

* How-to guide
* 1-min read

## Возможности

* Полностековый мониторинг на базе OneAgent
* Расширенная поддержка метаданных EC2, включая регионы и другое
* Пакет AWS Systems Manager Distributor для упрощённого развёртывания OneAgent
* Интеграция с CloudWatch для получения метрик, свойств и тегов из AWS

## Интеграция OneAgent для полностекового мониторинга

Мониторинг экземпляров Amazon EC2 работает сразу из коробки. Просто запустите стандартные установщики OneAgent для Linux и Windows.

Кроме того, вы можете использовать любой инструмент управления инфраструктурой, например Terraform, для интеграции OneAgent на ваших виртуальных машинах. Dynatrace также предоставляет интеграцию с AWS Systems Manager Distributor, позволяющую распространять и автоматически развёртывать OneAgent на экземплярах EC2.
