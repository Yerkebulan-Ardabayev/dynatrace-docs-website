---
title: Стратегии обнаружения версий для глубоко контролируемых процессов
source: https://www.dynatrace.com/docs/deliver/release-monitoring/version-detection-strategies
scraped: 2026-03-06T21:32:40.181980
---

# Стратегии определения версий для процессов с глубоким мониторингом


* How-to guide
* 3-min read

Dynatrace поддерживает несколько стратегий для определения и получения информации о версиях релизов.
Эти стратегии помогают обогащать данные наблюдаемости контекстом релизов, обеспечивая лучшую прослеживаемость, фильтрацию и анализ.
На определение версий можно влиять с помощью переменных среды, меток Kubernetes, приёма событий и атрибутов ресурсов из OpenTelemetry.

## Переменные среды

Используйте переменные среды для передачи метаданных релизов напрямую в Dynatrace OneAgent.

* `DT_RELEASE_VERSION` для **Version** (версия)
* `DT_RELEASE_STAGE` для **Stage** (стадия)
* `DT_RELEASE_PRODUCT` для **Product** (продукт)
* `DT_RELEASE_BUILD_VERSION` для **Build version** (версия сборки)

### Пример

1. Установите переменную среды, заменив `<YOUR_VERSION>` на информацию о вашей версии.

Windows

Linux

`$env:DT_RELEASE_VERSION='<YOUR_VERSION>'`

`export DT_RELEASE_VERSION='<YOUR_VERSION>'`

2. Запустите процесс. Через некоторое время версия этого процесса появится в Dynatrace.

## Метки Kubernetes

Рекомендация

Рекомендуется передавать метки Kubernetes в переменные среды в конфигурации развёртывания.

### Пример

![K8s best practice](https://dt-cdn.net/images/k8s-labels-env-1-662-06080041a8.png)

Начиная с версии 0.10.0+ Dynatrace Operator, вы можете настроить передачу меток релизов, установив флаг функции `feature.dynatrace.com/label-version-detection=true` в пользовательском ресурсе DynaKube. Подробности см. в разделе [Настройка передачи меток сборки](../../ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation.md "Configure build label propagation").

Вы можете использовать:

* Метки подов Kubernetes для передачи метаданных:

  + Информации о стадии (метка: `dynatrace-release-stage`)
* [Рекомендуемые метки Kubernetes](https://dt-url.net/e103qse) для развёрнутых подов для передачи метаданных:

  + Информации о версии (метка: `app.kubernetes.io/version`)
  + Связанного продукта (метка: `app.kubernetes.io/part-of`) Необязательно

Используйте только метки подов, а не метки рабочих нагрузок Kubernetes.

Рекомендуемые метки Kubernetes, сопоставленные с метаданными релизов:

![Recommended labels](https://dt-cdn.net/images/k8s-recommended-labels-1982-5e4ca55659.png)

Dynatrace OneAgent с [правами просмотра пространства имён](../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments.md#viewer "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.") может автоматически обнаруживать метки, прикреплённые к подам Kubernetes.

* **Version** и **Product** отображаются в реестре релизов.
* Пространства имён Kubernetes или настроенные имена хост-групп Dynatrace отображаются как **Stages** в реестре релизов.

Если вам нужно обновить информацию о версии, обновите конфигурацию развёртывания, включив обновлённую метку, и выполните повторное развёртывание подов. Это обеспечит правильную установку переменной среды `DT_RELEASE_VERSION` при запуске пода. Дополнительную информацию см. в разделе [Настройка передачи меток сборки](../../ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation.md "Configure build label propagation").

Приведённая ниже команда не передаст обновлённую метку в переменную среды `DT_RELEASE_VERSION`, используемую OneAgent.

```
kubectl label --overwrite pod yourPodId -n yourNamespace app.kubernetes.io/version=42
```

## Приём событий

Используйте Dynatrace Events API для отправки [пользовательских событий развёртывания](../../dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/info-events.md "Learn more about informational events and the logic behind raising them.") с метаданными релизов.

* Информация о версиях, отправленная через события, не может использоваться для фильтрации трассировок или метрик.
  Всегда устанавливайте переменные среды для отражения текущей развёрнутой версии, чтобы обеспечить точную фильтрацию и анализ.
  Убедитесь, что переменные среды всегда указывают на текущую развёрнутую версию.

  + Поскольку процессы сопоставляются с помощью тегов, для каждого процесса создаётся отдельное событие.
    В результате любой [рабочий процесс](../../analyze-explore-automate/workflows/quickstart.md "Build and run your first workflow."), подписанный на эти события, может быть запущен несколько раз.
    Чтобы избежать повторных выполнений, рекомендуется отправлять выделенное событие в рабочий процесс.

В приведённом ниже примере JSON показано, как отправлять пользовательские события развёртывания в [API приёма событий](../../dynatrace-api/environment-api/events-v2/post-event.md "Ingests an event via the Dynatrace API.").

Для обнаружения релиза должны быть выполнены следующие требования:

* `eventType` установлен в `CUSTOM_DEPLOYMENT`
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

Dynatrace поддерживает приём метаданных релизов через атрибуты ресурсов OpenTelemetry, позволяя передавать информацию о версиях через данные телеметрии.

Чтобы использовать этот метод, определите переменную среды `OTEL_RESOURCE_ATTRIBUTES` в вашем приложении и задайте пары ключ-значение, представляющие метаданные релиза.
Полный список поддерживаемых [атрибутов](../../semantic-dictionary/fields.md#deployment-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), называемых атрибутами развёртывания, см. в [Семантическом словаре](../../semantic-dictionary/fields.md "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").
Хотя Dynatrace обогащает данные телеметрии этими атрибутами, они не передаются сущностям экземпляров групп процессов.
В результате релизы, определённые через атрибуты ресурсов OpenTelemetry, не будут отображаться в [реестре релизов](monitor-releases-with-dynatrace.md#release-inventory "Analyze data related to each release version of your software.").

### Пример

1. Создайте или дополните переменную среды `OTEL_RESOURCE_ATTRIBUTES` метаданными релиза.

   Windows

   Linux

   `$env:OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`

   `export OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`
2. После установки переменной среды Dynatrace автоматически обнаруживает атрибуты ресурсов и обогащает трассировки и журналы предоставленными метаданными релиза.