---
title: Обновление OneAgent на Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/update-oneagent-on-cloud-foundry
scraped: 2026-05-12T11:09:22.027268
---

# Обновление OneAgent на Cloud Foundry

# Обновление OneAgent на Cloud Foundry

* 1-min read
* Published Apr 17, 2020

Ниже описан порядок обновления OneAgent в зависимости от используемой стратегии развёртывания. Обзор всех вариантов развёртывания см. в разделе [Стратегии развёртывания Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка Dynatrace на Cloud Foundry.").

## Обновление lightweight BOSH release OneAgent

Для виртуальных машин Cloud Foundry в Dynatrace OneAgent встроен [механизм автообновления](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Способы обновления OneAgent на Linux."). Это означает, что ручное обновление OneAgent, запущенного на виртуальных машинах Cloud Foundry, не требуется.

После любого автообновления необходимо вручную перезапустить платформенные процессы и процессы/приложения Cloud Foundry, чтобы они стали отслеживаться с последней версией Dynatrace OneAgent.

```
cf restart <app_name>
```

## Обновление immutable BOSH release OneAgent

Для обновления immutable BOSH release следуйте [инструкциям по развёртыванию](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#immutable "Установка OneAgent на Cloud Foundry с помощью BOSH.") по загрузке последнего release, его загрузке в BOSH blobstore и изменению версий в конфигурации среды выполнения.

## Обновление OneAgent для мониторинга только приложений

При появлении новой версии Dynatrace OneAgent необходимо выполнить restage вашего приложения Cloud Foundry.

```
cf restage <app_name>
```

Cloud Foundry buildpack автоматически загрузит последнюю версию Dynatrace OneAgent. После restage ваши приложения Cloud Foundry будут отслеживаться с последней версией Dynatrace OneAgent.

Если в [настройках обновлений OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Способы обновления OneAgent на Linux.") указана версия OneAgent по умолчанию для новых хостов и приложений, Cloud Foundry buildpack автоматически загрузит указанную версию Dynatrace OneAgent.

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")