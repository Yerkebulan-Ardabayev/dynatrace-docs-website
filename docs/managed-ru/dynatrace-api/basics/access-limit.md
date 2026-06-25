---
title: Dynatrace API - Лимит доступа
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/access-limit
scraped: 2026-05-12T11:03:51.159313
---

# Dynatrace API - Лимит доступа

# Dynatrace API - Лимит доступа

* Reference
* Updated on Jan 09, 2026

Чтение через Dynatrace API бесплатно при условии разумного использования (fair use). Плата взимается за определение и отправку новых пользовательских метрик через Dynatrace API, тариф рассчитывается по каждой метрике в месяц.

Подробнее о приёме пользовательских метрик и о том, как это влияет на потребление мониторинга Dynatrace, смотрите страницу для вашей модели лицензирования.

* Dynatrace Platform Subscription: [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")
* Dynatrace classic license: [DDU для метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Расчёт потребления Davis data units и расходов на отслеживаемые метрики.")

## Лимит payload

Размер payload ограничен 1 МБ. Исключения:

* Configuration API [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление файлами символов мобильных приложений через Dynatrace API.") — можно загрузить файл символов до 100 МиБ в сжатом виде; распакованный файл не должен превышать 500 МиБ.
* Configuration API [Extensions API](/managed/dynatrace-api/configuration-api/extensions-api "Возможности Dynatrace Extension API.") — можно загрузить ZIP-файлы расширений до 50 МБ.
* Configuration API [Plugins API](/managed/dynatrace-api/configuration-api/plugins-api "Управление плагинами через Dynatrace configuration API.") — можно загрузить ZIP-файлы плагинов до 50 МБ.
* Log Ingestion API [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Возможности Log Monitoring API v2.") — максимальный размер payload одного запроса 10 МБ.
* OpenTelemetry trace ingest API [Ingestion API](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry (traces, metrics, logs) в Dynatrace.") — максимальный размер payload одного запроса 8 МБ.
* OpenTelemetry metrics ingest API [Ingestion API](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry (traces, metrics, logs) в Dynatrace.") — максимальный размер payload одного запроса 4 МБ.
* OpenTelemetry logs ingest API [Ingestion API](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry (traces, metrics, logs) в Dynatrace.") — максимальный размер payload одного запроса 2 МБ.

## Дросселирование запросов (Request throttling)

В каждом окружении есть ограниченный пул потоков (с очередью) для обработки запросов. Лимит достигается, когда заполнены и пул, и очередь, или когда запрос превышает время ожидания в очереди (тайм-аут 10 секунд). При достижении лимита запросы возвращают код ответа 429.

Такой подход позволяет выполнять большое количество «дешёвых» запросов, не упираясь в лимит, и одновременно защищает ваше окружение от перегрузки множеством «дорогих» запросов.

### Проверка оставшегося лимита

Чтобы узнать остаток лимитов, посмотрите заголовки ответа на ваши запросы.

| Заголовок | Описание |
| --- | --- |
| X-RateLimit-Limit | Лимит запросов в минуту для этого endpoint. |
| X-RateLimit-Remaining | Оставшееся количество запросов. |
| X-RateLimit-Reset | Метка времени в **микросекундах**, когда лимит будет сброшен. |