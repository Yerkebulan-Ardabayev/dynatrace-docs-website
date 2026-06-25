---
title: Автоматическое инструментирование Python-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/python/python-auto
scraped: 2026-05-12T12:04:13.507851
---

# Автоматическое инструментирование Python-приложения с OpenTelemetry

# Автоматическое инструментирование Python-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 2 мин
* Опубликовано: 20 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Python-приложение с помощью автоматического инструментирования для OpenTelemetry Python.

Обогащение через OneAgent

В настоящее время невозможно [обогатить](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.") автоматически инструментированные сервисы информацией, относящейся к хосту. Для этого потребуется перейти на ручное инструментирование.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Инструментирование приложения

В следующем примере используется `opentelemetry-distro` для автоматической настройки всех доступных и применимых библиотек инструментирования. Вместо этого можно также пропустить шаги 1 и 2 и выборочно добавить библиотеки инструментирования, [установив `opentelemetry-instrumentation`](https://pypi.org/project/opentelemetry-instrumentation/) и применимые [библиотеки инструментирования](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/README.md) вручную.

1. С помощью [pip](https://pypi.org/project/pip/) установите следующие пакеты.

   ```
   pip install opentelemetry-distro



   pip install opentelemetry-exporter-otlp
   ```
2. Выполните следующую команду, чтобы инициализировать и развернуть автоматическое инструментирование.

   ```
   opentelemetry-bootstrap -a install
   ```
3. Настройте следующие переменные окружения, чтобы задать сведения о сервисе и экспорте, подставив вместо `[URL]` и `[TOKEN]` значения для [базового URL](#base-url) и [токена доступа](#access-token).

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token%20[TOKEN]"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta



   OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf



   OTEL_SERVICE_NAME="python-quickstart"
   ```

   Кодирование URL в переменных окружения

   Обратите внимание, что пробел в `OTEL_EXPORTER_OTLP_HEADERS` кодируется как `%20`, поскольку эта переменная [следует соглашению correlation context](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#specifying-headers-via-environment-variables) и её [значение должно быть percent-encoded](https://github.com/w3c/baggage/blob/main/baggage/HTTP_HEADER_FORMAT.md#value).
4. Запустите приложение с агентом `opentelemetry-instrument`.

   ```
   opentelemetry-instrument python myapp.py
   ```

## Шаг 3 (необязательно) Добавление сигналов телеметрии вручную (необязательно)

Поскольку автоматическое инструментирование на Python не предоставляет предварительно настроенных провайдеров tracer и meter, потребуется выполнить шаги [инициализации](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual#instrument "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace.") и [инструментирования](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual#add-telemetry-signals-manually "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace.") из раздела [Ручное инструментирование Python-приложения с OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace."), если вы хотите вручную добавить пользовательские сигналы (такие как трассировки и метрики) поверх автоматического инструментирования.

## Шаг 4 Обеспечьте context propagation

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

При автоматическом инструментировании это должно автоматически обрабатываться библиотеками инструментирования. Если используемые сетевые библиотеки не охвачены этим, потребуется вместо этого перейти на [ручное инструментирование](/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace.") и обрабатывать propagation вручную.

## Шаг 5 (необязательно) Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 6 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")