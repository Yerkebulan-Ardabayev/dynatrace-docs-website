---
title: Настройка трассировки OpenTelemetry с Envoy
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/integrations/envoy
scraped: 2026-05-12T11:23:45.595247
---

# Настройка трассировки OpenTelemetry с Envoy

# Настройка трассировки OpenTelemetry с Envoy

* Практическое руководство
* Чтение: 4 мин
* Обновлено 07 апреля 2026 г.

Заявление о поддержке

Данная интеграция основана на коде с открытым исходным кодом, регулируемом соответствующими сообществами, и не подпадает под политику поддержки Dynatrace. Мы стремимся оказывать помощь, однако проблемы и запросы функций следует сообщать непосредственно в соответствующий проект. Dynatrace не может гарантировать исправления или функции ввиду независимой природы OSS-проектов.

Всегда используйте самую последнюю версию релиза, чтобы иметь актуальные патчи и исправления.

На этой странице описано, как настроить экземпляр Envoy версии 1.30+ для экспорта трассировок в Dynatrace.

### Предварительные требования

* [URL для трассировок OTLP](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для экспорта.
* Кодовый модуль OneAgent для Envoy отключён.
  Для этого:

  1. Перейдите на соответствующую страницу конфигурации:

     + Для всей среды перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
     + Для отдельного хоста перейдите в **Your host** > **Host settings** > **General**.
  2. Найдите **Envoy** в списке отслеживаемых технологий и выберите **Edit**.
  3. Выберите переключатель **Monitor Envoy** при необходимости, чтобы отключить кодовый модуль OneAgent для Envoy.

### Шаги

1. Получить записи конфигурации

1. В Dynatrace Hub выполните поиск `Envoy`.
2. Выберите запись Hub для Envoy.
3. Выберите **Set up**.
4. Настройте API-токен.
5. Выполните следующие шаги и используйте (при необходимости скорректировав) два предоставленных фрагмента конфигурации там, где применимо.

2. Добавить запись кластера Dynatrace для экспорта OpenTelemetry

Чтобы Envoy мог отправлять трассировки в Dynatrace, сначала нужно настроить запись [cluster](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) для Dynatrace в файле конфигурации Envoy. Для этого добавьте [запись конфигурации cluster, полученную на шаге 2](#snippets), под ключом верхнего уровня `clusters`.

3. Конфигурация, специфичная для Dynatrace, для tracer OpenTelemetry

Затем нужно добавить провайдер трассировки к [фильтру HTTP connection manager](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management#http-connection-management) в [файле конфигурации Envoy](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static#listeners).

Используйте [запись конфигурации tracer, полученную на шаге 2](#snippets), настройте [API-токен](#prerequisites) в разделе `tracing` - `provider` - `typed_config` - `http_service` - `request_headers_to_add` - `header` - `value` (правильный синтаксис: `value: "Api-Token YOUR_API_TOKEN_HERE"`), и добавьте конфигурацию tracer в упомянутую выше запись `filters`.

4. Проверить настройку

После завершения настройки и приёма первых данных можно проверить, отображаются ли трассировки в Dynatrace.

![trace](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)

trace

## Связанные темы

* [Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Узнайте, как расширить наблюдаемость в Dynatrace с помощью метрик Prometheus.")
* [Метрики прокси Istio/Envoy](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Приём метрик Istio и обнаружение топологии")