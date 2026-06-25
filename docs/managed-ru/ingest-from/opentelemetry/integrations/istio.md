---
title: Настройка трассировки OpenTelemetry с Istio
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/integrations/istio
scraped: 2026-05-12T12:14:32.687450
---

# Настройка трассировки OpenTelemetry с Istio

# Настройка трассировки OpenTelemetry с Istio

* Практическое руководство
* Чтение: 3 мин
* Обновлено 07 апреля 2026 г.

Заявление о поддержке

Данная интеграция основана на открытом исходном коде, управляемом соответствующими сообществами, и не подпадает под политику поддержки Dynatrace. Хотя мы стремимся оказывать помощь, об ошибках и запросах на добавление функций следует сообщать непосредственно в соответствующий проект. Dynatrace не может гарантировать исправления или новые функции в силу независимой природы проектов с открытым исходным кодом.

Всегда используйте самую последнюю версию выпуска, чтобы гарантировать наличие актуальных исправлений и патчей.

На этой странице описывается, как использовать Istio версии 1.22+ с [провайдером расширения OpenTelemetry для Istio](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider) и как настроить его для экспорта трассировок OpenTelemetry в Dynatrace.

### Системные требования

Для настройки конфигурации трассировки Istio OpenTelemetry, включая обнаружение ресурсов Dynatrace и сэмплирование, требуется Istio версии 1.22+ (то есть выпуски Istio, поставляемые с Envoy 1.30+).

## Влияние на лицензирование

В некоторых конфигурациях развёртывания трассировка с Istio версии 1.22+ приводит к потреблению следующих возможностей [прайс-листа](https://www.dynatrace.com/pricing/):

* При использовании детектора ресурсов и сэмплера Dynatrace:

  + Развёртывания Classic Full-Stack или cloud-native Full-Stack: использование включено в [Full-Stack Monitoring (DPS)](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Узнайте, как тарифицируется и оплачивается ваше потребление возможности Dynatrace Full-Stack Monitoring DPS.") и [Host Units (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").
  + Для развёртываний только с Application Observability: использование приводит к потреблению [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "Узнайте, как рассчитывается потребление расширений платформы Dynatrace с использованием модели Dynatrace Platform Subscription.") или [DDU для пользовательских трассировок (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces "Узнайте, как рассчитывается потребление DDU для спанов, принятых через Trace API.").
* Без детектора ресурсов и сэмплера Dynatrace: использование приводит к потреблению [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "Узнайте, как рассчитывается потребление расширений платформы Dynatrace с использованием модели Dynatrace Platform Subscription.") или [DDU для пользовательских трассировок (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces "Узнайте, как рассчитывается потребление DDU для спанов, принятых через Trace API.").

## Соображения по развёртыванию

Трассировку Istio OpenTelemetry можно настроить в автономном развёртывании или в сочетании с Dynatrace Operator.

### Развёртывание в сочетании с Dynatrace Operator (рекомендуется)

Рекомендуется использовать интеграцию Istio OpenTelemetry в сочетании с развёртыванием Dynatrace Operator с включёнными [обогащением метаданных](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes, присоединяя релевантные метаданные к таким сущностям, как поды, хосты и процессы, для лучшей наблюдаемости.") и [эндпоинтами приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите эндпоинты приёма телеметрии Dynatrace в Kubernetes для приёма данных локально в кластере."). Другие компоненты, такие как OneAgent или ActiveGate, не требуются.

Это обеспечивает следующие преимущества по сравнению с автономным использованием:

* Надёжная и более эффективная доставка трассировок благодаря возможностям повторных попыток и группирования.
* Опциональная маршрутизация через ActiveGate.
* Дополнительный токен доступа не требуется.
* Дополнительные `ServiceEntries` не требуются.
* Совместимость с параметром `enableIstio` Dynatrace Operator.

### Автономное развёртывание

Принимать трассировки Istio можно без развёртывания экземпляра Dynatrace Operator, однако это сопряжено со значительными недостатками и следует прибегать к этому варианту лишь в случае, если развёртывание Dynatrace Operator невозможно.

Предостережения при использовании автономного развёртывания:

* Метаданные Kubernetes будут недоступны для трассировок. Это означает, что трассировки не будут автоматически сопоставляться с рабочими нагрузками или сервисами Kubernetes в Dynatrace.
* Потенциально ненадёжная доставка трассировок. Текущая реализация экспортера OTLP HTTP в Envoy не предусматривает механизмов повторных попыток или обработки ошибок в случае проблем с подключением или иных проблем при отправке трассировок в Dynatrace, что может приводить к потере трассировок.
* Требуемый `ServiceEntry` несовместим с параметром `enableIstio` Dynatrace Operator.

### Прочие соображения по развёртыванию

Istio в режиме ambient

#### Поддержка Istio в режиме ambient

Istio в режиме ambient не использует прокси Envoy для маршрутизации трафика, поэтому трассировка трафика Istio с помощью интеграции OpenTelemetry невозможна. При использовании waypoint-прокси они по-прежнему будут генерировать трассировки, однако метаданные могут быть некорректными или вводящими в заблуждение. В настоящее время решения для сквозной трассировки в режиме ambient Istio не существует.

## Шаги

### 1. Требования

Перед началом развёртывания трассировки для Istio проверьте следующие требования.

Dynatrace Operator

Автономный режим

1. Dynatrace Operator [развёрнут](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").

   * Для оптимальной конфигурации следуйте руководству по [развёртыванию совместно с Istio](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "Развёртывание Dynatrace Operator совместно с Istio в различных сценариях.").
2. [Эндпоинты приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите эндпоинты приёма телеметрии Dynatrace в Kubernetes для приёма данных локально в кластере.") включены.

Dynatrace Operator либо не развёрнут, либо в DynaKube для параметра `enableIstio` установлено значение `false`.

### 2. Получение конфигурационных записей

Dynatrace Operator

Автономный режим

1. В Dynatrace Hub выполните поиск по запросу `Istio`.
2. Отфильтруйте по категории **Technology**.
3. Выберите запись Hub **Istio Service Mesh**.
4. Выберите **Set up**.
5. Используйте предоставленные и предварительно настроенные сниппеты для развёртывания следующих элементов на следующих шагах:

   * Конфигурация сетки
   * Telemetry API

1. В Dynatrace Hub выполните поиск по запросу `Istio`.
2. Отфильтруйте по категории **Technology**.
3. Выберите запись Hub **Istio Service Mesh**.
4. Выберите **Set up**.
5. Настройте API-токен.
6. Используйте предоставленные и предварительно настроенные сниппеты для развёртывания следующих элементов на следующих шагах:

   * Конфигурация сетки
   * Запись сервиса
   * Telemetry API

### 3. Применение конфигурации сетки к установке Istio

Dynatrace Operator

Автономный режим

Для использования эндпоинтов приёма телеметрии, предоставляемых Dynatrace OTel Collector, необходимо изменить сниппет, полученный на шаге 2: удалить заголовок API-токена и изменить целевой сервис.

Результирующая конфигурация должна выглядеть следующим образом при использовании имени сервиса приёма по умолчанию:

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

Сохраните файл как `meshconfig.yaml` и примените конфигурацию с помощью следующей команды.

```
istioctl install -f meshconfig.yaml
```

Сохраните сниппет конфигурации сетки, полученный на шаге 2, в файле `meshconfig.yaml` и настройте Istio следующей командой:

```
istioctl install -f meshconfig.yaml
```

Существующая конфигурация сетки

Если вы уже используете собственную пользовательскую конфигурацию сетки, необходимо объединить её содержимое с предоставленным сниппетом. В противном случае сниппет можно использовать как есть.

### 4. Развёртывание записи сервиса

Dynatrace Operator

Автономный режим

Этот шаг требуется только для автономного развёртывания.
При использовании Dynatrace Operator никаких действий не требуется.

Затем необходимо развернуть манифест [записи сервиса Istio](https://istio.io/latest/docs/reference/config/networking/service-entry/), полученный на шаге 1, с помощью `kubectl`. Сохраните его в файл `dt-serviceentry.yaml` и выполните следующую команду:

```
kubectl apply -n istio-system -f dt-serviceentry.yaml
```

### 5. Включение провайдера трассировки

На последнем шаге конфигурации используйте Istio telemetry API для включения провайдера трассировки.

Сохраните манифест Telemetry API, полученный на шаге 2, в файл `dt-telemetry.yaml` и примените конфигурацию к нужному пространству имён с помощью `kubectl`.

```
kubectl apply -n istio-system -f dt-telemetry.yaml
```

Несколько ресурсов телеметрии

Не развёртывайте более одного ресурса телеметрии в пределах одного пространства имён, так как это может привести к конфликтам конфигурации и неполной информации о трассировке.

Если требуется несколько ресурсов телеметрии, разверните их в разных пространствах имён или с использованием разных селекторов.

Перезапуск подов

Убедитесь, что все применимые поды Kubernetes перезапущены, чтобы изменения конфигурации сетки вступили в силу.

### 6. Проверка настройки

После завершения настройки и приёма первых данных можно проверить, отображаются ли трассировки в Dynatrace.

![trace](https://dt-cdn.net/images/istio-otel-tracing-2513-5da62a325b.png)

trace