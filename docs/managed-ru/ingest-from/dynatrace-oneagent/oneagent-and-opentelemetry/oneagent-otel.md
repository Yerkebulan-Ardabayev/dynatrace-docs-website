---
title: Использование OneAgent с данными OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel
scraped: 2026-05-12T11:05:18.873836
---

# Использование OneAgent с данными OpenTelemetry

# Использование OneAgent с данными OpenTelemetry

* Практическое руководство
* 3-min read
* Published Sep 30, 2025

Существует два способа использования OneAgent с OpenTelemetry:

* Отправка трассировок OpenTelemetry на [OTLP API endpoints Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").
* Обнаружение спанов OpenTelemetry из данных трассировки с помощью OpenTelemetry Span Sensor кодового модуля OneAgent.

![OneAgent отправляет данные в Dynatrace](https://dt-cdn.net/images/screenshot-2025-09-30-at-12-44-35-2430-bc1bd03d62.png)

OneAgent отправляет данные в Dynatrace

Для большинства сценариев Dynatrace рекомендует экспортировать OTLP напрямую в Dynatrace без развёртывания OneAgent.

## Отправка трассировок OpenTelemetry на OTLP endpoint OneAgent

Dynatrace OneAgent предоставляет локальный OTLP endpoint только для трассировок.
Это показано на рисунке выше: приложение использует локальный OTLP endpoint.

* Локальный (local-only) означает, что OneAgent предоставляет endpoint исключительно по адресу `127.0.0.1` (localhost).
* Только трассировки (traces-only) означает, что OneAgent принимает только информацию трассировки, но не метрики и не логи.

Поддержка сжатия содержимого

OneAgent пока не поддерживает сжатие содержимого через HTTP-заголовок [`Content-Encoding`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Encoding). Обратите на это особое внимание при [инструментировании Ruby-приложения](/managed/ingest-from/opentelemetry/walkthroughs/ruby "Узнайте, как инструментировать Ruby-приложение с помощью OpenTelemetry и Dynatrace."), поскольку OpenTelemetry SDK для Ruby по умолчанию использует `Content-Encoding: gzip`.

Если вам необходимо использовать сжатие содержимого, выполняйте экспорт через SaaS, Collector или ActiveGate.

Чтобы отправить трассировки в OneAgent, сначала необходимо включить **Extension Execution Controller**. Это можно сделать глобально для всего окружения, для групп хостов или только для отдельных хостов.

Включение на уровне окружения

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включение для группы хостов

1. Перейдите в **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group** и выберите нужную группу хостов из выпадающего списка.

   Список хостов будет отфильтрован по выбранной группе. У каждого хоста в списке есть ссылка **Host group:** `<название группы>`, где `<название группы>` — имя группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни одной группе хостов.
4. Выберите название группы хостов в любой строке.

   Поскольку вы отфильтровали по группе хостов, все отображаемые хосты относятся к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

Включение для отдельного хоста

1. Перейдите в **Hosts**.
2. Найдите и выберите нужный хост для отображения страницы обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**...**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

После включения EEC установки OneAgent на соответствующих хостах начнут принимать OTLP-трассировки по URL `http://localhost:14499/otlp/v1/traces`.

OneAgent использует TCP-порт 14499 в качестве порта по умолчанию для этого endpoint. Вы можете изменить порт с помощью [`oneagentctl`](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api#communication-port "Используйте Dynatrace API для получения метрик мониторируемых сущностей.").

EEC недоступен в контейнерных окружениях

Endpoint для приёма данных EEC доступен только при развёртывании [Full-Stack и Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте подробнее о доступных режимах мониторинга при использовании OneAgent."). Он **недоступен** при [контейнерных развёртываниях](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes"). Для контейнерных приложений используйте [ActiveGate](#export-to-saas-and-activegate) в качестве endpoint экспорта.

### Детали экспорта

Вызовы к этим API endpoints должны соответствовать следующим требованиям протокола:

* HTTP/gRPC пока не поддерживается
* Бинарный формат Protocol Buffers/JSON пока не поддерживается
* Сжатие содержимого через заголовок `Content-Encoding` не поддерживается

### Аутентификация

Поскольку endpoint является только локальным, OneAgent не требует аутентификации.

### Сетевые требования

* Убедитесь, что нет локальных ограничений для используемого TCP-порта (по умолчанию: 14499)

  Поскольку OTLP-коммуникация является исключительно локальной, особой сетевой конфигурации не требуется, если только у вас не ограничена локальная сетевая коммуникация. В таком случае убедитесь, что нет локальных ограничений для используемого TCP-порта (по умолчанию: 14499).

## Обнаружение спанов OpenTelemetry с помощью OpenTelemetry Span Sensor кодового модуля OneAgent

Кодовый модуль OneAgent включает OpenTelemetry Span Sensor, который может создавать новые спаны на основе вызовов OpenTelemetry API.
Это показано на рисунке выше: кодовый модуль (с OpenTelemetry Span Sensor) отправляет данные по протоколу OpenTelemetry.

Используйте этот подход

* Для сервисов, которые уже инструментированы OneAgent автоматически.
* Для расширения видимости фреймворков и библиотек, инструментированных с помощью OpenTelemetry.
* Для настройки распределённых трассировок.

Эта функция предназначена только для опытных пользователей, которые хотят создавать пользовательские спаны с использованием вызовов OpenTelemetry API.

Описанная на этой странице функция предоставляет ту же функциональность, что и OneAgent SDK для обнаружения спанов, но использует OpenTelemetry вместо него.

Если вы включите эту функцию, одновременно экспортируя данные OTLP, это приведёт к созданию дублирующихся спанов.

Данные спанов OpenTelemetry можно захватить для Java, Go, Node.js, PHP и .NET на всех платформах, поддерживаемых OneAgent.
Инструкции по настройке и конфигурации OneAgent Span Sensor смотрите в разделе [Включение OpenTelemetry Span Sensor для OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

Когда OneAgent OpenTelemetry Span Sensor включён, такие вызовы API автоматически обнаруживаются и включаются в представление waterfall трассировки.
Поскольку OneAgent захватывает эти спаны автоматически, их экспорт на OTLP endpoint создаст дублирующиеся трассировки.

Следующий пример показывает, что OneAgent будет обнаруживать и встраивать в трассировку OneAgent без сложностей ручного распространения.

```
GET /calculate-price/ABC123  # OneAgent



--- SELECT FROM products     # OneAgent



--- calculate-discount       # OpenTelemetry



|   --- seasonal-rules       # OpenTelemetry



|   --- loyalty-calculation  # OpenTelemetry



--- INSERT INTO prices       # OneAgent
```

Эти автоматически инструментированные спаны соединяются с вашими ручными спанами OpenTelemetry в единую трассировку.

```
@RestController



public class PricingController {



private static final Tracer tracer = GlobalOpenTelemetry.getTracer("pricing-service");



@GetMapping("/calculate-price/{productId}")



public PriceResponse calculatePrice(@PathVariable String productId) {



Product product = productRepository.findById(productId);



Span calcSpan = tracer.spanBuilder("calculate-discount")



.setAttribute("product.category", product.getCategory())



.startSpan();



double discount;



try (Scope scope = calcSpan.makeCurrent()) {



discount = applySeasonalRules(product);



discount += applyCustomerLoyalty(product);



} finally {



calcSpan.end();



}



return priceRepository.save(new PriceResponse(product, discount));



}



private double applySeasonalRules(Product product) {



Span span = tracer.spanBuilder("seasonal-rules")



.setAttribute("season", "winter-sale")



.startSpan();



try (Scope scope = span.makeCurrent()) {



return calculateSeasonalDiscount();



} finally {



span.end();



}



}



private double applyCustomerLoyalty(Product product) {



Span span = tracer.spanBuilder("loyalty-calculation").startSpan();



try (Scope scope = span.makeCurrent()) {



return calculateLoyaltyDiscount();



} finally {



span.end();



}



}



}
```