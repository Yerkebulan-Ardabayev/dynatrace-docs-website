---
title: Configure OpenTelemetry tracing with Envoy
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/integrations/envoy
scraped: 2026-03-06T21:17:56.336075
---

# Настройка трассировки OpenTelemetry с Envoy

# Настройка трассировки OpenTelemetry с Envoy

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 4 мин
* Обновлено 15 октября 2025 г.

Заявление о поддержке

Данная интеграция основана на коде с открытым исходным кодом, регулируемом соответствующими сообществами, и не подпадает под действие политики поддержки Dynatrace. Мы стремимся оказывать помощь, однако проблемы и запросы на добавление функций следует сообщать непосредственно в соответствующий проект. Dynatrace не может гарантировать исправления или реализацию функций ввиду независимой природы проектов с открытым исходным кодом.

Всегда используйте последнюю версию выпуска, чтобы убедиться, что у вас установлены актуальные исправления.

На этой странице описано, как настроить экземпляр Envoy версии 1.29 и выше для экспорта трассировок в Dynatrace.

Если вы используете Envoy версий 1.28 и ниже, вы по-прежнему можете экспортировать трассировки в Dynatrace через кодовый модуль OneAgent для Envoy.

### Предварительные условия

* [URL OTLP-трассировок](../otlp-api.md "Узнайте об конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для экспорта.
* Кодовый модуль OneAgent для Envoy отключён.
  Для этого:

  1. Перейдите на соответствующую страницу настроек:

     + Для всей среды перейдите в **Настройки** > **Мониторинг** > **Отслеживаемые технологии**.
     + Для конкретного хоста перейдите в **Ваш хост** > **Настройки хоста** > **Общие**.
  2. Найдите **Envoy** в списке отслеживаемых технологий и выберите **Редактировать**.
  3. Выберите переключатель **Отслеживать Envoy**, чтобы отключить кодовый модуль OneAgent для Envoy.

### Шаги

1. Получение записей конфигурации

1. В Dynatrace Hub выполните поиск `Envoy`.
2. Выберите запись Hub для Envoy.
3. Выберите **Настроить**.
4. Настройте токен API.
5. Продолжите выполнение следующих шагов и используйте (при необходимости адаптируя) два предоставленных фрагмента конфигурации.

2. Добавление записи кластера Dynatrace для экспорта OpenTelemetry

Чтобы Envoy отправлял трассировки в Dynatrace, необходимо сначала настроить запись [кластера](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) для Dynatrace в файле конфигурации Envoy. Для этого добавьте [запись конфигурации кластера, полученную на шаге 2](#snippets), в разделе верхнего уровня `clusters`.

3. Специфическая для Dynatrace конфигурация трассировщика OpenTelemetry

Далее необходимо добавить провайдера трассировки в [фильтр менеджера HTTP-соединений](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management#http-connection-management) в [файле конфигурации Envoy](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static#listeners).

Envoy 1.30+

Envoy 1.29

Используйте [запись конфигурации трассировщика, полученную на шаге 2](#snippets), настройте [токен API](#prerequisites) в разделе `tracing` - `provider` - `typed_config` - `http_service` - `request_headers_to_add` - `header` - `value` (правильный синтаксис: `value: "Api-Token YOUR_API_TOKEN_HERE"`), и добавьте конфигурацию трассировщика в упомянутую запись `filters`.

Настройте следующий фрагмент в разделе `filters`.

```
tracing:



provider:



name: envoy.tracers.opentelemetry



typed_config:



"@type": type.googleapis.com/envoy.config.trace.v3.OpenTelemetryConfig



service_name: your-service-name



http_service:



http_uri:



uri: "{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces"



cluster: dynatrace



timeout: 10s



request_headers_to_add:



- header:



key: "Authorization"



value: "Api-Token {API_TOKEN_HERE}"



resource_detectors:



- name: envoy.tracers.opentelemetry.resource_detectors.dynatrace



typed_config:



"@type": type.googleapis.com/envoy.extensions.tracers.opentelemetry.resource_detectors.v3.DynatraceResourceDetectorConfig
```

Следующие значения необходимо скорректировать в соответствии с вашей средой Dynatrace и конфигурацией экспорта:

* `uri` — указывает желаемый [URL экспорта с путём трассировки](../otlp-api.md "Узнайте об конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). Значение не должно содержать схему протокола, а начинаться с имени хоста.
* `cluster` — указывает имя кластера и должно совпадать со значением `cluster_name` предыдущего определения кластера.
* `request_headers_to_add` — содержит HTTP-заголовки, которые необходимо включить в запрос. Обязательно при экспорте через ActiveGate (настраивается для [токена API](#prerequisites)).

4. Проверка настройки

После завершения настройки и приёма первых данных вы можете убедиться, что трассировки отображаются в Dynatrace.

![trace](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)

## Связанные темы

* [Prometheus](../../extend-dynatrace/extend-metrics/ingestion-methods/prometheus.md "Узнайте, как расширить наблюдаемость в Dynatrace с помощью метрик Prometheus.")
* [Метрики прокси Istio/Envoy](../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics.md "Приём метрик Istio и обнаружение топологии")
