---
title: Настройка Dynatrace на Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry
scraped: 2026-05-12T11:03:26.590087
---

# Настройка Dynatrace на Cloud Foundry

# Настройка Dynatrace на Cloud Foundry

* 1-min read
* Published Aug 03, 2018

Dynatrace поддерживает полный стековый мониторинг Cloud Foundry через BOSH Release OneAgent, что позволяет развернуть OneAgent на всех виртуальных машинах Cloud Foundry, включая Diego cells, Cloud Controller, маршрутизаторы и другие компоненты.

## Интеграции

Существует два подхода к развёртыванию BOSH Release OneAgent: [immutable](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#immutable "Установка OneAgent на Cloud Foundry с помощью BOSH.") и [lightweight](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#lightweight "Установка OneAgent на Cloud Foundry с помощью BOSH."). Различия между этими подходами описаны ниже.

Immutable release

Lightweight release

Immutable release OneAgent BOSH загружается через Dynatrace Environment API. Этот релиз содержит полные пакеты, бинарные файлы и файлы установки в одном архиве. Данный подход является неизменяемым (immutable), так как предоставляет операторам полный контроль над тем, что и когда развёртывается.

![Immutable release](https://dt-cdn.net/images/bosh-cludfoundry-immutable-500-fbf72def36.png)

Immutable release

Lightweight release OneAgent BOSH загружает и устанавливает предварительно настроенный OneAgent во время развёртывания, что гарантирует актуальность бинарных файлов OneAgent и позволяет выполнять полностью автоматизированные обновления версий.

![Lightweight release](https://dt-cdn.net/images/bosh-cloudfoundry-lightweight-500-4ff8ba068b.png)

Lightweight release

Если у вас нет доступа к BOSH, Dynatrace предоставляет два варианта мониторинга только приложений:

* [OneAgent на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.")
* [OneAgent на SAP Business Technology Platform](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Установка OneAgent на SAP Business Technology Platform.")

## Конфигурация

[Подключение Cloud Foundry к Dynatrace](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Включение мониторинга в Cloud Foundry foundations.")

[Установка плитки Dynatrace Service Broker для Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile "Установка и настройка плитки Dynatrace Service Broker для VMware Tanzu Platform.")

## Обслуживание

[Обновление OneAgent на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/update-oneagent-on-cloud-foundry "Обновление OneAgent на Cloud Foundry по различным стратегиям развёртывания.")

[Удаление OneAgent с Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/uninstall-oneagent-from-cloud-foundry "Удаление OneAgent с Cloud Foundry для BOSH add-ons.").

## Устранение неполадок

[Устранение проблем развёртывания OneAgent на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/troubleshoot-cf "Устранение проблем развёртывания на Cloud Foundry.")

## Связанные темы

* [Мониторинг Cloud Foundry](https://www.dynatrace.com/technologies/cloud-foundry-monitoring/)
* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")