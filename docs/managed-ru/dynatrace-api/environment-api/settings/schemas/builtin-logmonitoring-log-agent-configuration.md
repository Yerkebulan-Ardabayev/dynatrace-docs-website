---
title: Settings API - Advanced log settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-agent-configuration
scraped: 2026-05-12T11:48:26.729030
---

# Settings API - Advanced log settings schema table

# Settings API - Advanced log settings schema table

* Published Dec 05, 2023

### Расширенные параметры логов (`builtin:logmonitoring.log-agent-configuration)`

Настройте параметры OneAgent для Dynatrace Log Monitoring

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-agent-configuration` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать открытые лог-файлы `LAConfigOpenLogFilesDetectionEnabled` | boolean | Автоматически обнаруживать логи, записываемые важными процессами. Подробнее см. в [documentation](https://dt-url.net/7v02z76) | Required |
| Обнаруживать системные логи `LAConfigSystemLogsDetectionEnabled` | boolean | Linux: syslog, message log Windows: system, application, security event logs | Required |
| Обнаруживать логи контейнеризованных приложений `LAConfigContainersLogsDetectionEnabled` | boolean | Позволяет обнаруживать сообщения логов, записываемые в потоки stdout/stderr контейнеризованного приложения. | Required |
| Обнаруживать IIS-логи `LAConfigIISDetectionEnabled` | boolean | Позволяет обнаруживать логи и event logs, записываемые IIS-сервером. | Required |
| Обнаруживать логи на сетевых файловых системах `LAConfigLogScannerLinuxNfsEnabled` | boolean | Позволяет обнаруживать логи, записываемые на смонтированные сетевые накопители. Применяется только к Linux-хостам. Для Windows-систем включено всегда. | Required |
| Разрешить OneAgent мониторить Dynatrace-логи `LAConfigMonitorOwnLogsEnabled` | boolean | Включение этой опции может повлиять на лицензионные затраты. Подробнее см. в [documentation](https://dt-url.net/7v02z76). | Required |
| Обнаруживать часовые пояса контейнеров `LAConfigContainerTimezoneHeuristicEnabled` | boolean | Включает автоматическое обнаружение часового пояса в логах контейнера, если он не задан явно в контенте или в конфигурации. | Required |
| Часовой пояс по умолчанию для агентов `LAConfigDefaultTimezone` | text | Часовой пояс по умолчанию для агента, если не задана более конкретная конфигурация. | Required |
| Лимит поиска временной метки `LAConfigDateSearchLimit_Bytes` | integer | Задаёт количество символов в каждой строке лога (начиная с первого символа), в которых ищется временная метка. | Required |
| Лимит поиска severity по символам `LAConfigSeverityDetectionLimit_Bytes` | integer | Задаёт количество символов в каждой строке лога (начиная с первого символа), в которых ищется severity. | Required |
| Лимит поиска severity по строкам `LAConfigSeverityDetectionLinesLimit` | integer | Задаёт количество первых строк каждой записи лога, в которых ищется severity. | Required |
| Максимальное число источников логов на один process group instance `LAConfigMaxLgisPerEntityCount` | integer | Задаёт максимальное число log group instances на одну сущность, после которого новые автоматические instances не добавляются. | Required |
| Таймаут запроса Windows Event Log `LAConfigEventLogQueryTimeout_Sec` | integer | Задаёт максимальное значение таймаута (в секундах) для запроса, извлекающего Windows Event Logs | Required |
| Минимальный размер лог-файла для бинарного обнаружения. `LAConfigMinBinaryDetectionLimit_Bytes` | integer | Задаёт минимальное число байт в лог-файле, необходимое для бинарного обнаружения. | Required |