---
title: Стратегии обнаружения версий для процессов с глубоким мониторингом
source: https://docs.dynatrace.com/managed/deliver/release-monitoring/version-detection-strategies
scraped: 2026-05-12T11:38:23.226591
---

# Version detection strategies for deep-monitored processes

# Version detection strategies for deep-monitored processes

* How-to guide
* 3-min read
* Updated on Aug 11, 2025

Dynatrace поддерживает несколько стратегий обнаружения и приёма информации о версии релиза.
Эти стратегии помогают обогащать данные наблюдаемости контекстом релиза, обеспечивая лучшую трассируемость, фильтрацию и анализ.
На обнаружение версий можно влиять через переменные окружения, метки Kubernetes, приём событий и атрибуты ресурсов OpenTelemetry.

## Переменные окружения

Используйте переменные окружения для предоставления метаданных релиза непосредственно Dynatrace OneAgent.

* `DT_RELEASE_VERSION` для **Version**
* `DT_RELEASE_STAGE` для **Stage**
* `DT_RELEASE_PRODUCT` для **Product**
* `DT_RELEASE_BUILD_VERSION` для **Build version**

### Пример

1. Задайте переменную окружения, заменив `<YOUR_VERSION>` информацией о вашей версии.

Windows

Linux

`$env:DT_RELEASE_VERSION='<YOUR_VERSION>'`

`export DT_RELEASE_VERSION='<YOUR_VERSION>'`

2. Запустите процесс. Через некоторое время версия этого процесса появится в Dynatrace.

## Метки Kubernetes

Рекомендуемый подход

Рекомендуется передавать метки Kubernetes в переменные окружения в конфигурации развёртывания.

### Пример

![K8s best practice](https://dt-cdn.net/images/k8s-labels-env-1-662-06080041a8.png)

Рекомендуемый подход для Kubernetes

Начиная с версии Dynatrace Operator 0.10.0+, можно настроить распространение меток релиза, установив флаг функции `feature.dynatrace.com/label-version-detection=true` в пользовательском ресурсе DynaKube. Подробнее см. в разделе [Настройка распространения меток сборки](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation "Configure build label propagation").

Можно использовать:

* Метки Pod Kubernetes для предоставления метаданных для:

  + Информации о стейдже (метка: `dynatrace-release-stage`)
* [Рекомендуемые метки Kubernetes](https://dt-url.net/e103qse) для развёрнутых Pod для предоставления метаданных:

  + Информации о версии (метка: `app.kubernetes.io/version`)
  + Связанного продукта (метка: `app.kubernetes.io/part-of`) Необязательно

Обязательно используйте только метки Pod, а не метки Kubernetes workload.

Соответствие рекомендуемых меток Kubernetes метаданным релиза:

![Recommended labels](https://dt-cdn.net/images/k8s-recommended-labels-1982-5e4ca55659.png)

Рекомендуемые метки

Dynatrace OneAgent с [разрешениями viewer на пространство имён](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.") может автоматически обнаруживать метки, прикреплённые к Pod Kubernetes.

* **Version** и **Product** отображаются в инвентаре релизов.
* Пространства имён Kubernetes или настроенные имена групп хостов Dynatrace отображаются как **Stages** в инвентаре релизов.

Если нужно обновить информацию о версии, обновите конфигурацию развёртывания, включив обновлённую метку, и повторно разверните Pod. Это гарантирует, что переменная окружения `DT_RELEASE_VERSION` будет корректно задана при запуске Pod. Подробнее см. в разделе [Настройка распространения меток сборки](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation "Configure build label propagation").

Команда ниже не распространит обновлённую метку в переменную окружения `DT_RELEASE_VERSION`, используемую OneAgent.

```
kubectl label --overwrite pod yourPodId -n yourNamespace app.kubernetes.io/version=42
```

## Приём событий

Используйте Dynatrace Events API для отправки [пользовательских событий развёртывания](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/info-events "Learn more about informational events and the logic behind raising them.") с метаданными релиза.

* Информация о версии, отправленная через события, не может использоваться для фильтрации трассировок или метрик.
  Всегда задавайте переменные окружения, отражающие текущую развёрнутую версию, для обеспечения точной фильтрации и анализа.
  Убедитесь, что переменные окружения всегда указывают на текущую развёрнутую версию.

  + Поскольку процессы сопоставляются с использованием тегов, для каждого процесса генерируется отдельное событие.
    В результате любой [рабочий процесс](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), подписанный на эти события, может быть запущен несколько раз.
    Для избежания избыточных запусков рекомендуется отправлять отдельное событие непосредственно в рабочий процесс.

Пример JSON ниже показывает, как отправлять пользовательские события развёртывания в [API приёма событий](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

Для обнаружения релиза должны выполняться следующие требования:

* `eventType` должен быть равен `CUSTOM_DEPLOYMENT`
* `entitySelector` является обязательным и должен указывать на экземпляр группы процессов или список экземпляров групп процессов
* `dt.event.deployment.version` является обязательным

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

Dynatrace поддерживает приём метаданных релиза через атрибуты ресурсов OpenTelemetry, что позволяет распространять информацию о версии через телеметрические данные.

Для использования этого метода определите переменную окружения `OTEL_RESOURCE_ATTRIBUTES` в вашем приложении и задайте пары ключ-значение, представляющие метаданные релиза.
Полный список поддерживаемых [атрибутов](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") — так называемых атрибутов развёртывания — см. в [Semantic Dictionary](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
Хотя Dynatrace обогащает телеметрические данные этими атрибутами, они не распространяются на сущности экземпляров групп процессов.
В результате релизы, определённые через атрибуты ресурсов OpenTelemetry, не будут отображаться в [инвентаре релизов](/managed/deliver/release-monitoring/monitor-releases-with-dynatrace#release-inventory "Analyze data related to each release version of your software.").

### Пример

1. Создайте или расширьте переменную окружения `OTEL_RESOURCE_ATTRIBUTES` метаданными релиза.

   Windows

   Linux

   `$env:OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`

   `export OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`
2. После задания переменной окружения Dynatrace автоматически обнаружит атрибуты ресурсов и обогатит трассировки и журналы предоставленными метаданными релиза.