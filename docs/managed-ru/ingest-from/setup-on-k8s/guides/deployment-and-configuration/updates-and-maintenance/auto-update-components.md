---
title: Настройка автообновления компонентов, управляемых Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components
scraped: 2026-05-12T12:09:16.322846
---

# Настройка автообновления компонентов, управляемых Dynatrace Operator

# Настройка автообновления компонентов, управляемых Dynatrace Operator

* Чтение: 2 мин
* Обновлено 05 сентября 2025 г.

Dynatrace Operator управляет развёртыванием и обновлениями следующих компонентов в Kubernetes:

* OneAgent: настраивается в DynaKube
* ActiveGate: настраивается в DynaKube
* EdgeConnect: настраивается пользовательским ресурсом (CR) EdgeConnect

Настройки по умолчанию для OneAgent и ActiveGate автоматически развёртывают обновления, как только они становятся доступны. DynaKube также по умолчанию обновляет все поды при автоматическом обнаружении обновлений. Обратите внимание, что обновления могут занимать до 15 минут, так как Dynatrace Operator проверяет наличие обновлений с интервалом 15 минут. Если задать пользовательское значение `image` или `version`, автоматические обновления будут отключены.

## Настройка автообновления OneAgent

Задайте целевую версию на Dynatrace Server в виде относительной версии, например `Latest stable version`. Dynatrace Operator будет периодически проверять наличие обновлений и распространять их в окружение Kubernetes. Обновление версии OneAgent всегда вызывает перезапуск подов OneAgent.

Минимальная конфигурация DynaKube, использующая автообновление:

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

Окна обновления в настоящее время не применяются в окружениях Kubernetes.

Если для `autoUpdate` в DynaKube задано значение `false`, OneAgent не будут получать обновления версий на основе целевой версии окружения Dynatrace после первоначального развёртывания OneAgent.

Не рекомендуется задавать `autoUpdate: false` напрямую. Для управления обновлениями версий OneAgent рекомендуется сделать одно из следующего:

* Задать `autoUpdate: true` и указать целевую версию в веб-интерфейсе окружения Dynatrace
* Настроить поле `image` в DynaKube
* Настроить поле `version` в DynaKube

## Настройка автообновления модуля кода отслеживаемых приложений

Хотя новые образы загружаются, приложения обновляются только при перезапуске. Учитывайте, что автомасштабирование также внедряет самый последний CodeModule.

## Настройка автообновления ActiveGate

Как и для OneAgent, обновление ActiveGate можно настроить в интерфейсе, что приводит к изменению образа ActiveGate, видимого для Dynatrace Operator.