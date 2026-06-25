---
title: Удаление OneAgent с Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/uninstall-oneagent-from-cloud-foundry
scraped: 2026-05-12T11:09:26.977333
---

# Удаление OneAgent с Cloud Foundry

# Удаление OneAgent с Cloud Foundry

* 1-min read
* Published Apr 17, 2020

Ниже описан порядок удаления OneAgent в зависимости от используемой стратегии развёртывания. Обзор всех вариантов развёртывания см. в разделе [Стратегии развёртывания Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка Dynatrace на Cloud Foundry.").

## Удаление OneAgent Operator для BOSH release

1. Обновите конфигурацию среды выполнения.
   Для удаления OneAgent в BOSH add-ons необходимо обновить конфигурацию среды выполнения с «пустым» манифестом и выполнить повторное развёртывание всех BOSH-развёртываний, управляемых add-ons.

   Пример пустой конфигурации среды выполнения:

   ```
   releases:



   - name: dynatrace-oneagent



   version: 1.1.0



   #укажите версию последнего release
   ```

   Обновите конфигурацию среды выполнения без задач, связанных с Dynatrace.

   ```
   bosh -e my-env update-runtime-config PATH/runtime-config-uninstall-dynatrace.yml
   ```

2. Примените изменения и удалите Dynatrace.

   ```
   bosh -e my-env -d deployment deploy
   ```

## Удаление OneAgent для мониторинга только приложений

OneAgent внедряется при привязке сервиса Dynatrace к приложению. При отвязке сервиса OneAgent больше не будет внедряться (и, таким образом, будет удалён).

1. Отвяжите сервис.

   ```
   cf unbind-service <app-name> <service-instance-name>
   ```

2. Перезапустите (restage) приложение.

   ```
   cf restage <app-name>
   ```

Необязательно: для удаления сервиса, если он больше не нужен (применимо как для CUPS, так и для service broker):

```
cf delete-service <service-instance-name>
```

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")