---
title: Автоматическое инструментирование Java-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/java/java-auto
scraped: 2026-05-12T12:12:08.020183
---

# Автоматическое инструментирование Java-приложения с OpenTelemetry

# Автоматическое инструментирование Java-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 1 мин
* Опубликовано: 18 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Java-приложение с помощью агента автоматического инструментирования для OpenTelemetry Java.

Обогащение через OneAgent

В настоящее время невозможно [обогатить](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.") автоматически инструментированные сервисы информацией, относящейся к хосту. Для этого потребуется перейти на ручное инструментирование.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Инструментирование приложения

1. Скачайте файл агента [последней версии `opentelemetry-javaagent.jar`](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) и сохраните его в каталог, доступный вашему приложению (например, `libs`).
2. Настройте следующие переменные окружения, чтобы задать сведения о сервисе и протоколе. Если вы экспортируете через OTLP, также задайте переменным URL и токена [соответствующие значения](#dynatrace-docs--otlp-export).

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



   OTEL_RESOURCE_ATTRIBUTES="service.name=java-quickstart,service.version=1.0.1"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```
3. Добавьте параметр `-javaagent` в команду запуска Java и укажите путь к файлу агента. Например, если вы запускаете приложение из командной строки:

   ```
   java -javaagent:/PATH/TO/opentelemetry-javaagent.jar -jar myapplication.jar
   ```

## Шаг 3 Обеспечьте context propagation

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет обработано библиотеками инструментирования автоматически. В противном случае это должен учитывать ваш код.

## Шаг 4 (необязательно) Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 5 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")