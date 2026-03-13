---
title: OpenPipeline limits
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/limits
scraped: 2026-03-06T21:16:07.099440
---

# Лимиты OpenPipeline

# Лимиты OpenPipeline

* Последняя версия Dynatrace
* Справочник
* Чтение: 4 мин
* Обновлено 26 февраля 2026 г.

На этой странице перечислены лимиты Dynatrace OpenPipeline по умолчанию.

## Лимиты области конфигурации

Ограничения, специфичные для областей конфигурации, могут переопределять общие лимиты OpenPipeline. Для получения информации о лимитах, специфичных для области конфигурации, см.

* [Лимиты по умолчанию для Log Management and Analytics](../../../analyze-explore-automate/logs/lma-limits.md "Default limits for the latest version of Dynatrace Log Management and Analytics.") и [Валидация схемы для логов](#schema-validation-logs)
* [Поля с лимитами для метрик](#fields-metrics)
* [Поля с лимитами для спанов](#fields-spans)

## Лимиты для отдельных полей

### Поля с лимитами для всех областей конфигурации

* Следующие поля доступны только для просмотра; редактирование через OpenPipeline не поддерживается.

  + `dt.ingest.*`
  + `dt.openpipeline.*`
  + `dt.retain.*`
  + `dt.system.*`
* Следующие поля добавляются после этапа **Processing**, когда Dynatrace выполняет обнаружение сущностей. Вы можете использовать их только на этапах после Processing, но не на этапах предварительной обработки, маршрутизации или на самом этапе Processing.

  + `dt.entity.aws_lambda_function`
  + `dt.entity.cloud_application`
  + `dt.entity.cloud_application_instance`
  + `dt.entity.cloud_application_names`
  + `dt.entity.custom_device`
  + `dt.entity.<genericEntityType>`
  + `dt.entity.kubernetes_cluster`
  + `dt.entity.kubernetes_node`
  + `dt.entity.kubernetes_service`
  + `dt.entity.service`
  + `dt.env_vars.dt_tags`
  + `dt.kubernetes.cluster.id`
  + `dt.kubernetes.cluster.name`
  + `dt.loadtest.custom_entity.enriched_custom_device_name`
  + `dt.process.name`[1](#fn-1-1-def)
  + `dt.source_entity`
  + `k8s.cluster.name`[2](#fn-1-2-def)

  1

  Для получения эквивалентных результатов до этапа Processing можно использовать `dt.process_group.detected_name`.

  2

  OneAgent версии 1.309+, Dynatrace Operator версии 1.4.2+. Поле доступно до этапа Processing, если [модуль логов OneAgent](../../../analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes.md "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") работает в автономном режиме.

### Поля с лимитами для метрик

Использование следующих полей для метрик в OpenPipeline ограничено.

* Поля, исключённые из условий динамической маршрутизации и из этапа **Processing**

  + `dt.entity.*`
* Поля, исключённые из этапа **Processing**

  + `dt.system.monitoring_source`
  + `metric.key`
  + `metric.type`
  + `timestamp`
  + `value`

### Поля с лимитами для спанов

Использование следующих полей для спанов в OpenPipeline ограничено.

* Поля, исключённые из условий динамической маршрутизации и из этапа **Processing**

  + `dt.entity.service`
  + `endpoint.name`
  + `failure_detection.*`
  + `request.is_failed`
  + `request.is_root_span`
  + `service_mesh.is_proxy`
  + `service_mesh.is_failed`
  + `supportability.*`
* Поля, исключённые из этапа **Processing**

  + `dt.ingest.size`
  + `dt.retain.size`
  + `duration`
  + `end_time`
  + `span.id`
  + `start_time`
  + `trace.id`

## Приём данных

### Максимальная метка времени записи

Если метка времени опережает текущее время более чем на 10 минут, она корректируется до времени сервера приёма плюс 10 минут.

### Минимальная метка времени записи

Записи за пределами указанных временных диапазонов отбрасываются.

## API приёма данных

### Значение метки времени

Поддерживаются числовые и строковые значения меток времени. OpenPipeline разбирает метку времени следующим образом.

* Числовые значения

  + До `100_000_000_000` разбираются как `SECONDS` (секунды).
  + До `100_000_000_000_000` разбираются как `MILLISECONDS` (миллисекунды).
  + До `9_999_999_999_999_999` разбираются как `MICROSECONDS` (микросекунды).
* Строковые значения разбираются как

  + Миллисекунды или секунды `UNIX epoch`
  + Форматы `RFC3339`
  + Форматы `RFC3164`
* Для других значений, которые не удаётся разобрать, поле `timestamp` перезаписывается временем приёма.

Если запись не содержит поля `timestamp`, полю `timestamp` присваивается время приёма.

## Обработка

### Исчерпание памяти обработки

Память обработки ограничена. Каждое изменение записи, например разбор поля, уменьшает доступную память обработки. При исчерпании доступной памяти обработки запись отбрасывается. Это отражается в метрике `dt.sfm.openpipeline.not_stored.records` с измерением `reason` со значением `buffer_overflow`.

### Размер записи после обработки

Максимальный размер записи после обработки составляет 16 МБ.

### Размер извлечённых атрибутов логов

Атрибуты логов могут иметь размер до 32 КБ.
Когда атрибуты логов добавляются в шаблон событий, размер каждого атрибута усекается до 4 096 байт.

### Количество извлечений для одной записи

Вы можете извлекать данные из одной записи максимум в пяти различных конвейерах (`dt.openpipeline.pipelines`). При превышении порогового значения извлечение данных из этой записи больше не выполняется. Запись продолжает обрабатываться и сохраняться.

### Валидация схемы для логов

Обработанный лог сохраняется, если выполнены следующие условия.

| Поле | Существует | Допустимые типы | Ограничения значений |
| --- | --- | --- | --- |
| `timestamp` | Да | `String`, `Numerical` | В пределах [диапазона приёма](#ingestion) |
| `content` | Да | `String` | Не проверяется |

Если схема недействительна, лог отбрасывается.

### Процессор узлов Smartscape

Вычисление идентификатора Smartscape поддерживает только тип `string`. Компоненты идентификатора должны иметь тип `string`.

[Предварительно обработайте](../concepts/data-flow.md#pre-processing "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.") записи для преобразования необходимых значений в тип данных `string`.

## Конфигурация

### Допустимые символы в пути эндпоинта

Путь эндпоинта — это уникальное имя, начинающееся с литерала, которое определяет эндпоинт. Оно нечувствительно к регистру и поддерживает буквенно-цифровые символы и точку (`.`). Например: `Endpoint.1`.

Путь эндпоинта не поддерживает:

* Точку (`.`) в качестве последнего символа
* Пробелы
* Последовательные точки (`..`)
* Значение `Null` или пустой ввод

## Группы конвейеров

* Максимальное количество составных конвейеров в группе конвейеров — 10.
* Максимальное количество конвейеров-участников в группе конвейеров — 100.
* Роль конвейера является постоянной.
  Преобразование ролей — из участника в составной или из составного в участника — не поддерживается.