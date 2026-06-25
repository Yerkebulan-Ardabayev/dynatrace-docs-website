---
title: Настройка мониторинга очередей сообщений
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/queues/configuration
scraped: 2026-05-12T11:38:01.028253
---

# Настройка мониторинга очередей сообщений

# Настройка мониторинга очередей сообщений

* How-to guide
* 3-min read
* Updated on Dec 28, 2022

Dynatrace автоматически обнаруживает, как сообщения обрабатываются в вашей среде. Однако при определённых обстоятельствах для обеспечения корректного обнаружения Dynatrace требуется ручная настройка.

## Ручная настройка

Ознакомьтесь с приведённой таблицей, чтобы определить, требуется ли ручная настройка.

| Если это верно... | ...то требуется следующая ручная настройка |
| --- | --- |
| Приложение использует нестандартные или не основанные на событиях обработчики очередей сообщений. | Определите [пользовательский сервис обмена сообщениями](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Настройте пользовательские сервисы обмена сообщениями для трассировки очередей сообщений."). |
| Используется IBM MQ. | Определите конфигурацию [IBM MQ](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing "Настройте Dynatrace для трассировки IBM MQ.") в Dynatrace для получения непрерывного потока сервисов. |
| Клиент обмена сообщениями несовместим с Dynatrace, или используется неподдерживаемый протокол. | Расширьте трассировки с помощью [OpenTelemetry](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.") или [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение для расширения сквозной видимости фреймворков и технологий, для которых ещё нет кодового модуля.") (см. также [OneAgent SDK на GitHub](https://github.com/Dynatrace/OneAgent-SDK#trace-messaging)). |

## Обнаружение групп процессов

OneAgent версии 1.250+ Dynatrace использует имя менеджера очередей IBM MQ для обнаружения и группировки процессов IBM MQ. Для управления обнаружением групп процессов IBM MQ:

* Перейдите в **Settings** > **Processes and containers** > **Built-in detection rules** и найдите **Group IBM MQ processes by queue manager name**.
* Через [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."), используйте идентификатор схемы `builtin:process-group.detection-flags`.

  Для использования API необходим токен доступа с областями действия **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. раздел [Создание токена доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

Обнаружение групп процессов требует перезапуска процесса IBM MQ.

## Связанные темы

* [Пользовательские сервисы обмена сообщениями](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Настройте пользовательские сервисы обмена сообщениями для трассировки очередей сообщений.")