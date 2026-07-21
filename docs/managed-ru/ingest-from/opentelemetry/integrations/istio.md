---
title: Настройка трассировки OpenTelemetry с Istio
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/integrations/istio
---

# Настройка трассировки OpenTelemetry с Istio

# Настройка трассировки OpenTelemetry с Istio

* Практическое руководство
* Чтение 3 мин
* Обновлено 07 апреля 2026 г.

Заявление о поддержке

Данная интеграция основана на исходном коде с открытым кодом, который регулируется соответствующими сообществами, и не покрывается политикой поддержки Dynatrace. Мы стараемся оказывать содействие, но о проблемах и запросах на новые функции нужно сообщать напрямую в соответствующий проект. Dynatrace не может гарантировать исправления или новые функции ввиду независимой природы OSS-проектов.

Всегда используй самую свежую версию релиза, чтобы иметь развёрнутыми последние патчи и исправления.

На этой странице описано, как использовать Istio версии 1.22+ с [Istio OpenTelemetry extension provider﻿](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider) и как настроить его для экспорта трейсов OpenTelemetry в Dynatrace.

### Системные требования

Для настройки конфигурации трассировки Istio OpenTelemetry, включая обнаружение ресурсов и сэмплирование Dynatrace, требуется Istio версии 1.22+ (то есть релизы Istio, поставляемые с Envoy 1.30+).

## Влияние на лицензирование

В некоторых сценариях развёртывания трассировка с Istio версии 1.22+ приводит к потреблению следующих возможностей [rate card﻿](https://www.dynatrace.com/pricing/):

* При использовании детектора ресурсов и сэмплера Dynatrace:

  + Развёртывания Classic Full-Stack или cloud-native Full-Stack: потребление включено в [Full-Stack Monitoring (DPS)](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Узнай, как рассчитывается и оплачивается потребление возможности Dynatrace Full-Stack Monitoring DPS.") и [Host Units (классическая лицензия Dynatrace)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Разберись, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").
  + Для развёртываний только с Application-Observability: потребление приводит к расходу [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "Узнай, как рассчитывается потребление платформенных расширений Dynatrace по модели Dynatrace Platform Subscription.") или [DDU для custom traces (классическая лицензия Dynatrace)](/managed/license/classic-licensing/davis-data-units/custom-traces "Разберись, как рассчитывается потребление DDU для спанов, поступающих через Trace API.").
* Без детектора ресурсов и сэмплера Dynatrace: потребление приводит к расходу [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "Узнай, как рассчитывается потребление платформенных расширений Dynatrace по модели Dynatrace Platform Subscription.") или [DDU для custom traces (классическая лицензия Dynatrace)](/managed/license/classic-licensing/davis-data-units/custom-traces "Разберись, как рассчитывается потребление DDU для спанов, поступающих через Trace API.").

## Особенности развёртывания

Настроить трассировку Istio OpenTelemetry можно в автономном развёртывании или в сочетании с Dynatrace Operator.

### Развёртывание в сочетании с Dynatrace Operator Рекомендуется

Рекомендуется использовать интеграцию Istio OpenTelemetry в сочетании с развёртыванием Dynatrace Operator с включёнными [обогащением метаданных](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Настрой обогащение метаданных в Dynatrace Operator, чтобы прикреплять метаданные Kubernetes к сигналам телеметрии с помощью OneAgent, OTLP-экспортёра или автономного обогащения.") и [эндпоинтами приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включи эндпоинты приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера."). Другие функции, такие как OneAgent или ActiveGate, не требуются.

Это даёт следующие преимущества по сравнению с автономным использованием:

* Надёжная и более эффективная доставка трейсов за счёт возможностей повторных попыток и батчинга.
* Опциональная маршрутизация через ActiveGate.
* Не требуется дополнительный токен доступа.
* Не требуются дополнительные `ServiceEntries`.
* Совместимость с параметром `enableIstio` Dynatrace Operator.

### Автономное развёртывание

Можно принимать трейсы Istio без развёрнутого экземпляра Dynatrace Operator, но это связано с серьёзными недостатками, и такой вариант стоит использовать только если развернуть Dynatrace Operator невозможно.

Особенности при автономном развёртывании:

* Метаданные Kubernetes для трейсов недоступны. Это означает, что трейсы не будут автоматически сопоставляться с рабочими нагрузками или сервисами Kubernetes в Dynatrace.
* Потенциально ненадёжная доставка трейсов. Текущая реализация OTLP HTTP-экспортёра в Envoy не предоставляет никаких средств повторных попыток или обработки ошибок в случае проблем с подключением или других сбоев при отправке трейсов в Dynatrace, что может приводить к потере трейсов.
* Требуемый `ServiceEntry` несовместим с опцией `enableIstio` Dynatrace Operator.

### Прочие особенности развёртывания

Ambient-режим Istio

#### Поддержка ambient-режима Istio

Istio в ambient-режиме не полагается на прокси Envoy для маршрутизации трафика, поэтому трассировка трафика Istio с помощью интеграции OpenTelemetry невозможна. При использовании waypoint-прокси они всё же будут генерировать трейсы, но метаданные будут вводящими в заблуждение или неверными. На данный момент решения для сквозной трассировки в ambient-режиме Istio нет.

## Шаги

### 1. Требования

Перед развёртыванием трассировки для Istio проверь следующие требования.

Dynatrace Operator

Автономно

1. Dynatrace Operator [развёрнут](/managed/ingest-from/setup-on-k8s/deployment "Разверни Dynatrace Operator в Kubernetes").

   * Для оптимальной конфигурации следуй руководству по [развёртыванию вместе с Istio](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "Развёртывание Dynatrace Operator вместе с Istio в различных сценариях").
2. Включены эндпоинты [приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включи эндпоинты приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.").

Либо Dynatrace Operator не развёрнут, либо в DynaKube параметру `enableIstio` присвоено значение `false`.

### 2. Получение конфигурационных записей

Dynatrace Operator

Автономно

1. В Dynatrace Hub найди `Istio`.
2. Отфильтруй по категории **Technology**.
3. Выбери запись Hub **Istio Service Mesh**.
4. Выбери **Set up**.
5. Используй предоставленные и заранее настроенные сниппеты, чтобы развернуть следующие элементы на следующих шагах:

   * Конфигурацию mesh
   * API телеметрии

1. В Dynatrace Hub найди `Istio`.
2. Отфильтруй по категории **Technology**.
3. Выбери запись Hub **Istio Service Mesh**.
4. Выбери **Set up**.
5. Настрой токен API.
6. Используй предоставленные и заранее настроенные сниппеты, чтобы развернуть следующие элементы на следующих шагах:

   * Конфигурацию mesh
   * Service entry
   * API телеметрии

### 3. Применение конфигурации mesh к установке Istio

Dynatrace Operator

Автономно

Чтобы использовать эндпоинты приёма телеметрии, предоставляемые Dynatrace OTel Collector, нужно изменить сниппет, полученный на шаге 2, убрав заголовок токена API и изменив целевой сервис.

Итоговая конфигурация должна выглядеть так, при условии стандартного имени сервиса приёма:

```
apiVersion: install.istio.io/v1alpha1



kind: IstioOperator



spec:



meshConfig:



extensionProviders:



- name: dynatrace-otel



opentelemetry:



port: 4318



service: "<dynakube-name>-telemetry-ingest.<dynatrace-operator-namespace>" # <-- Please fill in your ingest endpoint service



http:



path: "/v1/traces"



timeout: 10s



resource_detectors:



dynatrace: {}



dynatrace_sampler:



tenant: "<your-tenant-id>"  # <-- This must not be changed from step 2



cluster_id: <cluster-id>    # <-- This must not be changed from step 2
```

Сохрани файл под именем `meshconfig.yaml` и примени конфигурацию следующей командой.

```
istioctl install -f meshconfig.yaml
```

Сохрани сниппет конфигурации mesh, полученный на шаге 2, под именем `meshconfig.yaml` и настрой Istio следующей командой:

```
istioctl install -f meshconfig.yaml
```

Существующая конфигурация Mesh

Если уже используется собственная, кастомная конфигурация Mesh, нужно объединить её содержимое с предоставленным сниппетом. В противном случае сниппет можно использовать как есть.

### 4. Развёртывание service entry

Dynatrace Operator

Автономно

Этот шаг требуется только для автономного развёртывания.
При использовании Dynatrace Operator никаких действий не требуется.

Далее нужно развернуть манифест [Istio service entry﻿](https://istio.io/latest/docs/reference/config/networking/service-entry/), полученный на шаге 1, с помощью `kubectl`. Сохрани его как `dt-serviceentry.yaml` и выполни следующую команду:

```
kubectl apply -n istio-system -f dt-serviceentry.yaml
```

### 5. Включение провайдера трассировки

В качестве последнего шага настройки используй API телеметрии Istio, чтобы включить провайдера трассировки.

Сохрани манифест API телеметрии, полученный на шаге 2, под именем `dt-telemetry.yaml` и примени конфигурацию к нужному пространству имён с помощью `kubectl`.

```
kubectl apply -n istio-system -f dt-telemetry.yaml
```

Несколько ресурсов телеметрии

Не разворачивай более одного ресурса телеметрии в рамках одного пространства имён, так как это может привести к конфликтам конфигурации и неполной информации трассировки.

Если требуются разные ресурсы телеметрии, разворачивай их в разных пространствах имён или используя разные селекторы.

Перезапуск подов

Обязательно перезапусти все применимые поды Kubernetes, чтобы изменения конфигурации mesh вступили в силу.

### 6. Проверка настройки

После завершения настройки и приёма первых данных можно проверить, отображаются ли трейсы на странице **Distributed traces**.