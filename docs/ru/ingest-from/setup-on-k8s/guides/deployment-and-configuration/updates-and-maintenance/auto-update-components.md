---
title: Configure auto-update for Dynatrace Operator managed components
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components
scraped: 2026-03-04T21:31:59.293255
---

# Configure auto-update for Dynatrace Operator managed components

# Configure auto-update for Dynatrace Operator managed components

* Latest Dynatrace
* 2-min read
* Updated on Sep 05, 2025

Dynatrace Operator управляет развёртыванием и обновлениями следующих компонентов в Kubernetes:

* OneAgent: настраивается в DynaKube
* ActiveGate: настраивается в DynaKube
* EdgeConnect: настраивается через Custom Resource (CR) EdgeConnect

Настройки по умолчанию для OneAgent и ActiveGate автоматически применяют обновления по мере их появления. DynaKube также по умолчанию обновляет все поды при автоматическом обнаружении обновлений. Обратите внимание, что обновления могут занимать до 15 минут, поскольку Dynatrace Operator проверяет наличие обновлений с интервалом в 15 минут. Если задать пользовательское значение `image` или `version`, автоматические обновления будут отключены.

## Настройка автоматического обновления OneAgent

Установите целевую версию на сервере Dynatrace как относительную версию, например `Latest stable version`. Dynatrace Operator будет периодически проверять наличие обновлений и применять их в среде Kubernetes. Обновление версии OneAgent всегда приводит к перезапуску подов OneAgent.

Минимальная конфигурация DynaKube, использующая автоматическое обновление:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



cloudNativeFullStack: {}
```

Окна обновлений в настоящее время не применяются в средах Kubernetes.

Если в DynaKube параметр `autoUpdate` установлен в значение `false`, OneAgent не будет получать обновления версий на основе целевой версии среды Dynatrace после первоначального развёртывания OneAgent.

Не рекомендуется задавать `autoUpdate: false` напрямую. Для управления обновлениями версий OneAgent рекомендуется выполнить одно из следующих действий:

* Задать `autoUpdate: true` и установить целевую версию в веб-интерфейсе среды Dynatrace
* Настроить поле `image` в DynaKube
* Настроить поле `version` в DynaKube

## Настройка автоматического обновления кодового модуля отслеживаемых приложений

Пока загружаются новые образы, приложения обновляются только при перезапуске. Имейте в виду, что при автомасштабировании также внедряется самый последний CodeModule.

## Настройка автоматического обновления ActiveGate

Аналогично OneAgent, обновление ActiveGate можно настроить в пользовательском интерфейсе, что приводит к изменению образа ActiveGate, видимому для Dynatrace Operator.

## Настройка автоматического обновления EdgeConnect

Dynatrace Operator можно настроить на отключение автоматических обновлений, установив поле `autoUpdate` в разделе [спецификации EdgeConnect](../../../reference/edgeconnect-parameters.md#spec "List of configuration parameters for EdgeConnect.") в значение `false`.

```
apiVersion: dynatrace.com/v1alpha2



kind: EdgeConnect



metadata:



name: edgeconnect



namespace: dynatrace



spec:



autoUpdate: false
```
