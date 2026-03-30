---
title: Использование OneAgent с данными OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel
scraped: 2026-03-06T21:16:25.986356
---

* Latest Dynatrace
* How-to guide
* 3-min read

Существует два способа использования OneAgent с OpenTelemetry:

* Отправлять трассировки OpenTelemetry на конечные точки Dynatrace OTLP API.
* Обнаруживать спаны OpenTelemetry из данных трассировки с помощью сенсора спанов OpenTelemetry в кодовом модуле OneAgent.

![OneAgent send data to Dynatrace](https://dt-cdn.net/images/screenshot-2025-09-30-at-12-44-35-2430-bc1bd03d62.png)

Для большинства сценариев использования Dynatrace рекомендует экспортировать OTLP напрямую в Dynatrace без развёртывания OneAgent.

## Отправка трассировок OpenTelemetry на конечную точку OTLP, предоставляемую OneAgent

Dynatrace OneAgent предоставляет локальную конечную точку OTLP для трассировок.
Это показано на рисунке выше, где приложение использует локальную конечную точку OTLP.

* Локальная означает, что OneAgent предоставляет конечную точку исключительно на `127.0.0.1` (localhost).
* Только трассировки означает, что OneAgent принимает только информацию о трассировке, но не метрики или логи.

Поддержка кодирования содержимого

OneAgent пока не поддерживает сжатие содержимого с использованием HTTP-заголовка [`Content-Encoding`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Encoding). Обратите на это особое внимание при инструментировании приложения на Ruby, так как SDK OpenTelemetry для Ruby по умолчанию использует `Content-Encoding: gzip`.

Если вам необходимо использовать сжатие содержимого, пожалуйста, экспортируйте данные , Collector или ActiveGate.

Для отправки трассировок в OneAgent сначала необходимо включить **Extension Execution Controller**. Это можно сделать глобально для всей среды, для групп хостов или только для определённых хостов.

Включение на уровне среды

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включение для группы хостов

1. Перейдите в ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group**, а затем выберите нужную группу хостов из раскрывающегося списка.

   Список хостов теперь отфильтрован по выбранной группе хостов. У каждого хоста в списке есть ссылка **Host group:** `<group name>`, где `<group name>` — имя группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни одной группе хостов.
4. Выберите имя группы хостов в любой строке.

   Поскольку вы отфильтровали по группе хостов, все отображаемые хосты относятся к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

Включение для отдельного хоста

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Найдите и выберите нужный хост для отображения страницы обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**...**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

При включённом EEC установки OneAgent на соответствующих хостах начнут принимать трассировки OTLP по URL `http://localhost:14499/otlp/v1/traces`.

OneAgent использует TCP-порт 14499 в качестве порта по умолчанию для этой конечной точки. Вы можете изменить порт с помощью [`oneagentctl`](../../extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api.md#communication-port "Use the Dynatrace API to retrieve the metrics of monitored entities.").

EEC недоступен в контейнерных окружениях

Конечная точка приёма EEC доступна только при развёртывании Full-Stack и Infrastructure Monitoring. Она **недоступна** в контейнерных окружениях. Пожалуйста, используйте [ActiveGate](#export-to-saas-and-activegate) в качестве конечной точки экспорта для контейнерных приложений.

### Детали экспорта

Вызовы к этим конечным точкам API должны соответствовать следующим требованиям протокола:

* Использование HTTP — gRPC пока не поддерживается
* Использование бинарного формата Protocol Buffers — JSON пока не поддерживается
* Сжатие содержимого с использованием заголовка `Content-Encoding` не поддерживается

### Аутентификация

Поскольку это локальная конечная точка, OneAgent не требует аутентификации.

### Сетевые требования

* Убедитесь, что нет локальных ограничений для используемого TCP-порта (по умолчанию: 14499)

  Поскольку обмен данными по OTLP является исключительно локальным, особых сетевых настроек не требуется, если только вы не ограничили локальное сетевое взаимодействие. В этом случае убедитесь, что нет локальных ограничений для используемого TCP-порта (по умолчанию: 14499).

## Обнаружение спанов OpenTelemetry с помощью сенсора спанов OpenTelemetry в кодовом модуле OneAgent

Кодовый модуль OneAgent включает сенсор спанов OpenTelemetry, который может создавать новые спаны на основе вызовов API OpenTelemetry.
Это показано на рисунке выше, где кодовый модуль (с сенсором спанов OpenTelemetry) отправляет данные по протоколу OpenTelemetry.

Используйте этот подход

* Для сервисов, которые уже автоматически инструментированы OneAgent.
* Для расширения видимости фреймворков и библиотек, инструментированных с помощью OpenTelemetry.
* Для настройки распределённых трассировок.

Эта функция предназначена только для опытных пользователей, которые хотят создавать пользовательские спаны с помощью вызовов API OpenTelemetry.

Функция, описанная на этой странице, предоставляет ту же функциональность, что и SDK OneAgent для обнаружения спанов, но использует OpenTelemetry вместо него.

Если вы включите эту функцию одновременно с экспортом данных OTLP, вы создадите дублирующиеся спаны.

Данные спанов OpenTelemetry можно захватывать для Java, Go, Node.js, PHP и .NET на всех платформах, поддерживаемых OneAgent.
Для настройки и конфигурации сенсора спанов OneAgent см. Enable the OpenTelemetry Span Sensor for OneAgent.

Когда сенсор спанов OpenTelemetry OneAgent включён, вызовы API, подобные следующему примеру, автоматически обнаруживаются и включаются в представление водопада трассировки.
Поскольку OneAgent захватывает эти спаны автоматически, их экспорт на конечную точку OTLP создаст дублирующиеся трассировки.

Следующий пример показывает, что OneAgent обнаружит и встроит в трассировку OneAgent без сложности ручного распространения контекста.

```
GET /calculate-price/ABC123  # OneAgent


├── SELECT FROM products     # OneAgent


├── calculate-discount       # OpenTelemetry


│   ├── seasonal-rules       # OpenTelemetry


│   └── loyalty-calculation  # OpenTelemetry


└── INSERT INTO prices       # OneAgent
```

Эти автоматически инструментированные спаны объединяются с вашими ручными спанами OpenTelemetry в единую трассировку.

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
