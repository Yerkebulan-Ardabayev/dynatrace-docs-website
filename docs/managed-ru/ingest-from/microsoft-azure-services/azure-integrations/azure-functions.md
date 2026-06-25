---
title: Мониторинг Azure Functions через Azure App Service (встроенный)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions
scraped: 2026-05-12T11:09:42.705369
---

# Мониторинг Azure Functions через Azure App Service (встроенный)

# Мониторинг Azure Functions через Azure App Service (встроенный)

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 20 апреля 2022 г.

Azure Functions предлагает широкий спектр вариантов для различных [сценариев и случаев использования](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios) Azure Functions:

* Использование предпочтительного языка программирования
* Автоматизация развёртывания
* Использование гибкого [хостинга](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)

## Распределённая трассировка

Для различных вариантов хостинга функций Dynatrace предоставляет оптимальные способы включения распределённой трассировки.

* Dynatrace предлагает простую интеграцию для **Azure Functions, работающих на плане Appservice- (Dedicated)**, с использованием [site extension](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions через Azure site extension.").
* Трассировка Azure Functions на плане **Consumption- или Premium-Plan** сопряжена с дополнительными ограничениями, обусловленными природой бессерверного сервиса, такими как использование агентов инструментирования для полностью автоматического инструментирования кода во время выполнения.

Dynatrace обеспечивает распределённую трассировку для этих изолированных окружений на основе [OpenTelemetry](https://opentelemetry.io/). Если OpenTelemetry уже используется для инструментирования функций, данные трассировки можно принять через [Dynatrace Trace Ingest API](/managed/ingest-from/opentelemetry/otlp-api "Информация об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace."), однако рекомендуется использовать [Dynatrace exporter](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions на бессерверных планах хостинга"), который предоставляет дополнительные преимущества для полноценного использования возможностей автоматического анализа на базе ИИ в Dynatrace.

Для упрощения работы с OpenTelemetry Dynatrace предоставляет [библиотечные пакеты для Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions на бессерверных планах хостинга"), которые сокращают необходимый шаблонный код OpenTelemetry для распространения трассировки, применения атрибутов ресурсов и кода инициализации, а также обеспечивают соответствие семантическим соглашениям.

Используя такие продвинутые концепции, как [аспектно-ориентированное программирование (AOP)](https://en.wikipedia.org/wiki/Aspect-oriented_programming), можно реализовать полностью автоматическое инструментирование без изменения единой строки кода, что продемонстрировано в сообществном проекте на GitHub для [Azure Functions .NET](https://github.com/dtPaTh/Azure.Functions.Tracing).

## Расширенная видимость с помощью логов и платформенных метрик

Для повышения видимости при мониторинге работоспособности Azure Functions рекомендуется [включить сбор метрик сервиса из Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin "Мониторинг Function Services Azure и просмотр доступных метрик."), а также [настроить приём логов](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Использование log forwarding Azure для приёма логов Azure.").

![Azure Function Service](https://dt-cdn.net/images/azure-function-service-1397-ee1fed5f77.png)

Azure Function Service

## Связанные темы

* [Бессерверный мониторинг](/managed/discover-dynatrace/get-started/serverless-monitoring "Бессерверная наблюдаемость с Dynatrace")