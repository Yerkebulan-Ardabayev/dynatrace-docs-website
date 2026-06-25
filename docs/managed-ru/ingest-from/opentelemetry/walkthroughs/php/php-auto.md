---
title: Автоматическое инструментирование PHP-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/php/php-auto
scraped: 2026-05-12T12:15:16.706329
---

# Автоматическое инструментирование PHP-приложения с OpenTelemetry

# Автоматическое инструментирование PHP-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 2 мин
* Опубликовано: 20 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше PHP-приложение с помощью библиотек и инструментов OpenTelemetry PHP.

Обогащение через OneAgent

В настоящее время невозможно [обогатить](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.") автоматически инструментированные сервисы информацией, относящейся к хосту. Для этого потребуется перейти на ручное инструментирование.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Инструментирование приложения

1. Убедитесь, что для вашей системы настроена подходящая среда сборки, включающая GCC, Make и Autoconfig.
2. Соберите и установите библиотеку инструментирования с помощью [pickle](https://github.com/FriendsOfPHP/pickle).

   ```
   php pickle.phar install opentelemetry
   ```
3. Добавьте только что скомпилированную библиотеку как расширение в ваш `php.ini`.

   ```
   extension=opentelemetry.so
   ```
4. Перезапустите PHP и убедитесь, что расширение загружено.

   * Из командной строки, с помощью `php -m`
   * В составе веб-сервера, вызвав `phpinfo()`
5. Установите SDK и другие зависимости.

   * Обязательно Установите [SDK для OpenTelemetry PHP](https://dt-url.net/41039bh).
   * Необязательно В зависимости от библиотек, которые использует ваше приложение, возможно, вы захотите добавить в зависимости другие библиотеки инструментирования. Список поддерживаемых библиотек находится в [OpenTelemetry Registry](https://dt-url.net/zf239yc).
   * Обязательно Необходимо использовать [автозагрузку composer](https://dt-url.net/s2439p5), так как именно этот механизм используют все пакеты автоматического инструментирования для своей регистрации.
6. Настройте следующие переменные окружения.

   ```
   OTEL_PHP_AUTOLOAD_ENABLED=true



   OTEL_SERVICE_NAME=php-quickstart



   OTEL_PROPAGATORS=baggage,tracecontext



   OTEL_EXPORTER=otlp



   OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf



   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```

   Подставьте вместо `[URL]` и `[TOKEN]` [соответствующие значения](#dynatrace-docs--otlp-export).

## Шаг 3 Обеспечьте context propagation

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

При автоматическом инструментировании это должно автоматически обрабатываться библиотеками инструментирования. Если используемые сетевые библиотеки не охвачены этим, потребуется вместо этого перейти на [ручное инструментирование](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace.") и обрабатывать передачу контекста вручную.

## Шаг 4 (необязательно) Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 5 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")