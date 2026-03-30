---
title: Настройка Dynatrace в Cloud Foundry
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/cloud-foundry
scraped: 2026-03-06T21:15:45.746356
---

# Настройка Dynatrace на Cloud Foundry


* Latest Dynatrace
* 1-min read

Dynatrace поддерживает полноуровневый мониторинг для Cloud Foundry через Dynatrace OneAgent BOSH Release, что позволяет развёртывать OneAgent на виртуальных машинах кластера Cloud Foundry, включая Diego cells, Cloud Controller, router и другие компоненты.

## Интеграции

Существует два подхода к развёртыванию релиза OneAgent BOSH: неизменяемый и облегчённый. Различия между этими подходами описаны ниже.

Неизменяемый релиз

Облегчённый релиз

Неизменяемый релиз OneAgent BOSH загружается с помощью Dynatrace Environment API. Этот релиз содержит полные пакеты, бинарные файлы и установочные файлы в одном архиве. Такой полностью автономный подход является неизменяемым, поскольку предоставляет операторам полный контроль над тем, что и когда развёртывается.

![Immutable release](https://dt-cdn.net/images/bosh-cludfoundry-immutable-500-fbf72def36.png)

Облегчённый релиз OneAgent BOSH загружает и устанавливает предварительно настроенный OneAgent во время развёртывания, что гарантирует использование последних бинарных файлов OneAgent и обеспечивает полностью автоматизированное обновление версий под управлением OneAgent.

![Lightweight release](https://dt-cdn.net/images/bosh-cloudfoundry-lightweight-500-4ff8ba068b.png)

Если у вас нет доступа к BOSH, Dynatrace предлагает два различных подхода для мониторинга только приложений:

* OneAgent на Cloud Foundry
* OneAgent на SAP Business Technology Platform

## Конфигурация

Подключение кластеров Cloud Foundry к Dynatrace

Установка плитки дашборда Dynatrace Service Broker для Cloud Foundry

## Обслуживание

Обновление OneAgent на Cloud Foundry

Удаление OneAgent с Cloud Foundry.

## Устранение неполадок

Устранение проблем при развёртывании OneAgent на Cloud Foundry

## Связанные темы

* [Мониторинг Cloud Foundry](https://www.dynatrace.com/technologies/cloud-foundry-monitoring/)
* Мониторинг Cloud Foundry
