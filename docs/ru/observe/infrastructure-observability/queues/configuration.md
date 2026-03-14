---
title: Настройка мониторинга очередей сообщений
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration
scraped: 2026-03-05T21:32:36.644435
---

# Настройка мониторинга очередей сообщений


* Classic
* How-to guide
* 3-min read
* Updated on Dec 28, 2022

Dynatrace автоматически определяет способ обработки сообщений в вашей среде. Однако в некоторых случаях требуется ручная настройка, чтобы Dynatrace мог корректно обнаруживать обработку сообщений.

## Ручная настройка

Ознакомьтесь со следующей таблицей, чтобы определить, требуется ли ручная настройка.

## Обнаружение группы процессов

OneAgent версии 1.250+ Dynatrace использует имя менеджера очередей IBM MQ для обнаружения и группировки процессов IBM MQ. Для управления обнаружением группы процессов IBM MQ:

* Перейдите в **Settings** > **Processes and containers** > **Built-in detection rules** и найдите параметр **Group IBM MQ processes by queue manager name**.
* Через [Settings API](../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.") используйте идентификатор схемы `builtin:process-group.detection-flags`.

  Для использования API вам потребуется токен доступа с областями **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Сведения о его получении см. в разделе [Create an access token](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.").

Обнаружение группы процессов требует перезапуска процесса IBM MQ.

## Связанные разделы

* [Custom messaging services](../../application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services.md "Set up custom messaging services to trace message queues.")
