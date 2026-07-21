---
title: Version detection strategies for deep-monitored processes
source: https://docs.dynatrace.com/managed/deliver/release-monitoring-classic/version-detection-strategies
---

# Version detection strategies for deep-monitored processes

# Version detection strategies for deep-monitored processes

* Практическое руководство
* Чтение 3 мин
* Обновлено 11 авг. 2025 г.

Dynatrace поддерживает несколько стратегий для обнаружения и приёма информации о версии релиза.
Эти стратегии помогают обогащать данные наблюдаемости контекстом релиза, обеспечивая лучшую трассируемость, фильтрацию и анализ.
На обнаружение версии могут влиять переменные окружения, метки Kubernetes, приём событий и атрибуты ресурсов из OpenTelemetry.

## Переменные Environment

Используй переменные окружения, чтобы передавать метаданные релиза напрямую в Dynatrace OneAgent.

* `DT_RELEASE_VERSION` для **Version**
* `DT_RELEASE_STAGE` для **Stage**
* `DT_RELEASE_PRODUCT` для **Product**
* `DT_RELEASE_BUILD_VERSION` для **Build version**

### Пример

1. Задай переменную окружения, обязательно заменив `<YOUR_VERSION>` на информацию о своей версии.

Windows

Linux

`$env:DT_RELEASE_VERSION='<YOUR_VERSION>'`

`export DT_RELEASE_VERSION='<YOUR_VERSION>'`

2. Запусти процесс. Через непродолжительное время версия этого процесса появится в Dynatrace.

## Метки Kubernetes

Рекомендация

Рекомендуется передавать метки Kubernetes в переменные окружения в конфигурации развёртывания.

### Пример

![K8s best practice](https://dt-cdn.net/images/k8s-labels-env-1-662-06080041a8.png)

K8s best practice

Начиная с версии Dynatrace Operator 0.10.0+, можно настроить передачу release-меток, установив флаг функции `feature.dynatrace.com/label-version-detection=true` в пользовательском ресурсе DynaKube. Подробнее см. [Настройка передачи build-меток](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation "Configure build label propagation").

Можно использовать:

* метки подов Kubernetes для предоставления метаданных о:

  + информации об этапе (метка: `dynatrace-release-stage`)
* [рекомендуемые метки Kubernetes﻿](https://dt-url.net/e103qse) для развёрнутых подов, чтобы предоставить метаданные о:

  + информации о версии (метка: `app.kubernetes.io/version`)
  + связанном продукте (метка: `app.kubernetes.io/part-of`), опционально

Важно использовать только метки подов, а не метки workload Kubernetes.

Рекомендуемые метки Kubernetes, сопоставленные с метаданными релиза:

![Recommended labels](https://dt-cdn.net/images/k8s-recommended-labels-1982-5e4ca55659.png)

Recommended labels

Dynatrace OneAgent с [правами viewer на namespace](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.") может автоматически обнаруживать метки, присвоенные подам Kubernetes.

* **Version** и **Product** отображаются в инвентаре релизов.
* Пространства имён Kubernetes или настроенные имена групп хостов Dynatrace отображаются как **Stages** в инвентаре релизов.

Если нужно обновить информацию о версии, обнови конфигурацию развёртывания, включив в неё обновлённую метку, и переразверни поды. Это гарантирует, что переменная окружения `DT_RELEASE_VERSION` будет корректно установлена при запуске пода. Подробнее см. [Настройка передачи build-меток](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation "Configure build label propagation").

Приведённая ниже команда не передаст обновлённую метку в переменную окружения `DT_RELEASE_VERSION`, используемую OneAgent.

```
kubectl label --overwrite pod yourPodId -n yourNamespace app.kubernetes.io/version=42
```

## Приём событий

Используй Dynatrace Events API, чтобы отправлять [пользовательские события развёртывания](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/info-events "Learn more about informational events and the logic behind raising them.") с метаданными релиза.

* Информацию о версии, отправленную через события, нельзя использовать для фильтрации трасс или метрик.
  Всегда задавай переменные окружения так, чтобы они отражали актуально развёрнутую версию, для точной фильтрации и анализа.
  Убедись, что переменные окружения всегда указывают на актуально развёрнутую версию.

  + Поскольку процессы сопоставляются по тегам, для каждого процесса генерируется отдельное событие.
    В результате любой [workflow](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), подписанный на эти события, может запускаться несколько раз.
    Чтобы избежать избыточных запусков, рекомендуется отправлять в workflow отдельное выделенное событие.

Пример JSON ниже показывает, как отправлять пользовательские события развёртывания в [API приёма событий](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

Чтобы релиз был обнаружен, должны быть выполнены следующие требования:

* `eventType` установлен в `CUSTOM_DEPLOYMENT`
* `entitySelector` обязателен и должен указывать на экземпляр группы процессов или список экземпляров группы процессов
* `dt.event.deployment.version` обязателен

### Пример

```
{



"eventType": "CUSTOM_DEPLOYMENT",



"title": "Easytravel 1.1",



"entitySelector": "type(PROCESS_GROUP_INSTANCE),tag(easytravel)",



"properties": {



"dt.event.deployment.name":"Easytravel 1.1",



"dt.event.deployment.version": "1.1",



"dt.event.deployment.release_stage": "production" ,



"dt.event.deployment.release_product": "frontend",



"dt.event.deployment.release_build_version": "123",



"approver": "Jason Miller",



"dt.event.deployment.ci_back_link": "https://pipelines/easytravel/123",



"gitcommit": "e5a6baac7eb",



"change-request": "CR-42",



"dt.event.deployment.remediation_action_link": "https://url.com",



"dt.event.is_rootcause_relevant": true



}



}
```

## Атрибуты ресурсов OpenTelemetry

Dynatrace поддерживает приём метаданных релиза через атрибуты ресурсов OpenTelemetry, что позволяет передавать информацию о версии через данные телеметрии.

Чтобы использовать этот метод, определи переменную окружения `OTEL_RESOURCE_ATTRIBUTES` в своём приложении и задай пары ключ-значение, представляющие метаданные релиза.
Полный список поддерживаемых [атрибутов](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), называемых атрибутами развёртывания, см. в [Semantic Dictionary](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
Хотя Dynatrace обогащает данные телеметрии этими атрибутами, они не передаются в сущности экземпляров группы процессов.
В результате релизы, определённые через атрибуты ресурсов OpenTelemetry, не будут отображаться в [инвентаре релизов](/managed/deliver/release-monitoring-classic/monitor-releases-with-dynatrace#release-inventory "Analyze data related to each release version of your software.").

### Пример

1. Создай или дополни переменную окружения `OTEL_RESOURCE_ATTRIBUTES` метаданными релиза.

   Windows

   Linux

   `$env:OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`

   `export OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`
2. После того как переменная окружения задана, Dynatrace автоматически обнаруживает атрибуты ресурсов и обогащает трассы и логи предоставленными метаданными релиза.