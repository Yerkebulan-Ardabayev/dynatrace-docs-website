---
title: Настройка трассировки OpenTelemetry с Istio
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/integrations/istio
scraped: 2026-03-06T21:37:43.997109
---

# Настройка трассировки OpenTelemetry с Istio

# Настройка трассировки OpenTelemetry с Istio

* Latest Dynatrace
* Практическое руководство
* Чтение: 3 мин.
* Обновлено 22 октября 2025 г.

Заявление о поддержке

Эта интеграция основана на открытом исходном коде, управляемом соответствующими сообществами, и не покрывается политикой поддержки Dynatrace. Хотя мы стремимся помочь, проблемы и запросы на функции следует направлять непосредственно в соответствующий проект. Dynatrace не может гарантировать исправления/функции из-за независимой природы проектов с открытым исходным кодом.

Всегда используйте самую последнюю версию выпуска, чтобы убедиться, что у вас развёрнуты последние исправления и патчи.

На этой странице описывается, как использовать Istio версии 1.22+ с [провайдером расширения Istio OpenTelemetry](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider) и как настроить его для экспорта трассировок OpenTelemetry в Dynatrace.

### Системные требования

Для настройки конфигурации трассировки Istio OpenTelemetry, включая обнаружение ресурсов и сэмплирование Dynatrace, необходимы следующие предварительные условия:

* Istio версии 1.22+ (т.е. выпуски Istio, которые поставляются с Envoy 1.30+)

Istio версии 1.21 и более ранние

Istio версий 1.21 и более ранних поставляется с Envoy версий 1.29 и более ранних, который основан на OpenTracing.
Для использования этих выпусков Istio включите кодовый модуль Dynatrace Envoy, как описано в разделе [Настройка трассировки OpenTelemetry с Envoy](envoy.md#envoy-code-module "Узнайте, как настроить Envoy для отправки трассировок OpenTelemetry в Dynatrace.").

## Влияние на лицензирование

В определённых конфигурациях развёртывания трассировка с Istio версии 1.22+ приводит к потреблению следующих возможностей [тарифной карты](https://www.dynatrace.com/pricing/):

* При использовании детектора ресурсов и сэмплера Dynatrace:

  + Классическое Full-Stack или облачно-нативное Full-Stack развёртывание: использование включено в [Full-Stack Monitoring (DPS)](../../../license/capabilities/app-infra-observability/full-stack-monitoring.md "Узнайте, как тарифицируется и взимается плата за потребление возможности Dynatrace Full-Stack Monitoring DPS.") и [Host Units (Dynatrace Classic License)](../../../license/monitoring-consumption-classic/application-and-infrastructure-monitoring.md "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе единиц хостов.").
  + Для развёртываний только с Application-Observability: использование влечёт потребление [Custom Traces Classic (DPS)](../../../license/capabilities/platform-extensions.md "Узнайте, как рассчитывается потребление расширений платформы Dynatrace с использованием модели подписки Dynatrace Platform.") или [DDU для пользовательских трассировок (Dynatrace Classic License)](../../../license/monitoring-consumption-classic/davis-data-units/custom-traces.md "Узнайте, как рассчитывается потребление DDU для спанов, принятых через Trace API.").
* Без детектора ресурсов и сэмплера Dynatrace: использование влечёт потребление [Custom Traces Classic (DPS)](../../../license/capabilities/platform-extensions.md "Узнайте, как рассчитывается потребление расширений платформы Dynatrace с использованием модели подписки Dynatrace Platform.") или [DDU для пользовательских трассировок (Dynatrace Classic License)](../../../license/monitoring-consumption-classic/davis-data-units/custom-traces.md "Узнайте, как рассчитывается потребление DDU для спанов, принятых через Trace API.").

## Рекомендации по развёртыванию

Возможна настройка трассировки Istio OpenTelemetry в автономном развёртывании или в сочетании с Dynatrace Operator.

### Развёртывание в сочетании с Dynatrace Operator (рекомендуется)

Мы рекомендуем использовать интеграцию Istio OpenTelemetry в сочетании с развёртыванием Dynatrace Operator с включёнными [обогащением метаданных](../../setup-on-k8s/guides/metadata-automation/metadata-enrichment.md "Обогащение метаданных в Dynatrace Operator добавляет контекст к подам Kubernetes путём привязки соответствующих метаданных к сущностям, таким как поды, хосты и процессы, для улучшения наблюдаемости.") и [конечными точками приёма телеметрии](../../setup-on-k8s/extend-observability-k8s/telemetry-ingest.md "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера."). Другие функции, такие как OneAgent или ActiveGate, не требуются.

Это обеспечивает следующие преимущества по сравнению с автономным использованием:

* Устойчивая и более эффективная доставка трассировок благодаря возможностям повторных попыток и пакетной обработки.
* Опциональная маршрутизация через ActiveGate.
* Не требуется дополнительный токен доступа.
* Не требуются дополнительные `ServiceEntries`.
* Совместимость с опцией `enableIstio` Dynatrace Operator.

### Автономное развёртывание

Можно принимать трассировки Istio без развёрнутого экземпляра Dynatrace Operator, однако это сопряжено с существенными недостатками и должно использоваться только в случае невозможности развёртывания Dynatrace Operator.

Ограничения автономного развёртывания:

* Метаданные Kubernetes не будут доступны для трассировок. Это означает, что трассировки не будут автоматически коррелироваться с рабочими нагрузками или сервисами Kubernetes в Dynatrace.
* Потенциально ненадёжная доставка трассировок. Текущая реализация OTLP HTTP-экспортёра в Envoy не предусматривает механизмов повторных попыток или обработки ошибок при проблемах с подключением или других проблемах при отправке трассировок в Dynatrace, что может привести к потере трассировок.
* Необходимый `ServiceEntry` несовместим с опцией `enableIstio` Dynatrace Operator.

### Другие рекомендации по развёртыванию

Ambient-режим Istio

#### Поддержка ambient-режима Istio

Istio в ambient-режиме не использует прокси-серверы Envoy для маршрутизации трафика, поэтому трассировка трафика Istio с использованием интеграции OpenTelemetry невозможна. Если используются прокси waypoint, они по-прежнему будут генерировать трассировки, но метаданные будут вводящими в заблуждение или некорректными. В настоящее время решение для сквозной трассировки в ambient-режиме Istio отсутствует.

## Шаги

### 1. Требования

Проверьте следующие требования перед началом развёртывания трассировки для Istio.

Dynatrace Operator

Автономно

1. Dynatrace Operator [развёрнут](../../setup-on-k8s/deployment.md "Развёртывание Dynatrace Operator в Kubernetes").

   * Для оптимальной конфигурации следуйте руководству по [развёртыванию совместно с Istio](../../setup-on-k8s/guides/deployment-and-configuration/istio-deployment.md "Развёртывание Dynatrace Operator совместно с Istio в различных сценариях").
2. [Конечные точки приёма телеметрии](../../setup-on-k8s/extend-observability-k8s/telemetry-ingest.md "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.") включены.

Либо Dynatrace Operator не развёрнут, либо `enableIstio` установлен в `false` в DynaKube.

### 2. Получение записей конфигурации

Dynatrace Operator

Автономно

1. В Dynatrace Hub выполните поиск `Istio`.
2. Отфильтруйте по категории **Technology**.
3. Выберите запись Hub **Istio Service Mesh**.
4. Выберите **Set up**.
5. Используйте предоставленные и предварительно настроенные фрагменты для развёртывания следующих элементов на следующих шагах:

   * Конфигурация mesh
   * Telemetry API

1. В Dynatrace Hub выполните поиск `Istio`.
2. Отфильтруйте по категории **Technology**.
3. Выберите запись Hub **Istio Service Mesh**.
4. Выберите **Set up**.
5. Настройте токен API.
6. Используйте предоставленные и предварительно настроенные фрагменты для развёртывания следующих элементов на следующих шагах:

   * Конфигурация mesh
   * Service entry
   * Telemetry API

### 3. Применение конфигурации mesh к вашей установке Istio

Dynatrace Operator

Автономно

Чтобы использовать конечные точки приёма телеметрии, предоставляемые коллектором Dynatrace OpenTelemetry, необходимо изменить фрагмент, полученный на шаге 2, удалив заголовок токена API и изменив целевой сервис.

Результирующая конфигурация должна выглядеть следующим образом, при условии использования имени сервиса приёма по умолчанию:

```
apiVersion: install.istio.io/v1alpha1



kind: IstioOperator



spec:



meshConfig:



extensionProviders:



- name: dynatrace-otel



opentelemetry:



port: 4318



service: "<dynakube-name>-telemetry-ingest.<dynatrace-operator-namespace>.svc.cluster.local" # <-- Please fill in your ingest endpoint service



http:



path: "/v1/traces"



timeout: 10s



resource_detectors:



dynatrace: {}



dynatrace_sampler:



tenant: "<your-tenant-id>"  # <-- This must not be changed from step 2



cluster_id: <cluster-id>    # <-- This must not be changed from step 2
```

Сохраните файл как `meshconfig.yaml` и примените конфигурацию с помощью следующей команды.

```
istioctl install -f meshconfig.yaml
```

Сохраните фрагмент конфигурации mesh, полученный на шаге 2, как `meshconfig.yaml` и настройте Istio с помощью следующей команды:

```
istioctl install -f meshconfig.yaml
```

Существующая конфигурация Mesh

Если вы уже используете собственную пользовательскую конфигурацию Mesh, вам необходимо объединить её содержимое с предоставленным фрагментом. В противном случае вы можете использовать фрагмент как есть.

### 4. Развёртывание service entry

Dynatrace Operator

Автономно

Этот шаг необходим только для автономного развёртывания.
При использовании Dynatrace Operator никаких действий не требуется.

Далее необходимо развернуть манифест [Istio service entry](https://istio.io/latest/docs/reference/config/networking/service-entry/), полученный на шаге 1, с помощью `kubectl`. Сохраните его как `dt-serviceentry.yaml` и выполните следующую команду:

```
kubectl apply -n istio-system -f dt-serviceentry.yaml
```

### 5. Включение провайдера трассировки

В качестве последнего шага конфигурации используйте Istio Telemetry API для включения провайдера трассировки.

Сохраните манифест Telemetry API, полученный на шаге 2, как `dt-telemetry.yaml` и используйте `kubectl` для применения конфигурации к нужному пространству имён.

```
kubectl apply -n istio-system -f dt-telemetry.yaml
```

Несколько ресурсов телеметрии

Не развёртывайте более одного ресурса телеметрии в пределах одного пространства имён, так как это может привести к конфликтам конфигурации и неполной информации о трассировке.

Если вам требуются разные ресурсы телеметрии, развёртывайте их в разных пространствах имён или с использованием разных селекторов.

Перезапуск подов

Обязательно перезапустите все соответствующие поды Kubernetes, чтобы изменения конфигурации mesh вступили в силу.

### 6. Проверка настройки

После завершения настройки и приёма первых данных вы можете проверить, отображаются ли трассировки в Dynatrace.

![трассировка](https://dt-cdn.net/images/istio-otel-tracing-2513-5da62a325b.png)