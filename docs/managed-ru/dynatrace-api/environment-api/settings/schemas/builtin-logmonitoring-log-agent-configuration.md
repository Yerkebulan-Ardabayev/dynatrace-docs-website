---
title: Settings API - Advanced log settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-agent-configuration
---

# Settings API - Advanced log settings schema table

# Settings API - Advanced log settings schema table

* Опубликовано 05 дек. 2023

### Advanced log settings (`builtin:logmonitoring.log-agent-configuration`)

Настройка OneAgent параметров для Dynatrace Log Monitoring

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-agent-configuration` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Хост  `KUBERNETES_CLUSTER` - Kubernetes кластер  `HOST_GROUP` - Host Group  `environment` |

Получить схему через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с правами **Read settings** (`settings.read`). Порядок получения и использования описан в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Detect open log files `LAConfigOpenLogFilesDetectionEnabled` | boolean | Автоматически обнаруживать журналы, записываемые важными процессами. Подробнее в [документации﻿](https://dt-url.net/7v02z76) | Обязательный |
| Detect system logs `LAConfigSystemLogsDetectionEnabled` | boolean | Linux: syslog, журнал сообщений. Windows: системные, прикладные журналы и журналы событий безопасности | Обязательный |
| Detect logs of containerized applications `LAConfigContainersLogsDetectionEnabled` | boolean | Позволяет обнаруживать сообщения журнала, записываемые в потоки stdout/stderr контейнеризированного приложения. | Обязательный |
| Detect IIS logs `LAConfigIISDetectionEnabled` | boolean | Позволяет обнаруживать журналы и журналы событий, записываемые сервером IIS. | Обязательный |
| Detect logs on network file systems `LAConfigLogScannerLinuxNfsEnabled` | boolean | Позволяет обнаруживать журналы, записываемые на подключённые сетевые хранилища. Применяется только к Linux-хостам. Для Windows всегда включено. | Обязательный |
| Allow OneAgent to monitor Dynatrace logs `LAConfigMonitorOwnLogsEnabled` | boolean | Включение этого параметра может повлиять на стоимость лицензии. Подробнее в [документации﻿](https://dt-url.net/7v02z76). | Обязательный |
| Detect container time zones `LAConfigContainerTimezoneHeuristicEnabled` | boolean | Включает автоматическое определение часового пояса в журналах контейнера, если он не задан явно в содержимом или конфигурации. | Обязательный |
| Default timezone for agents `LAConfigDefaultTimezone` | text | Часовой пояс по умолчанию для агента, если не задана более точная конфигурация. | Обязательный |
| Timestamp search limit `LAConfigDateSearchLimit_Bytes` | integer | Задаёт количество символов в каждой строке журнала (начиная с первого символа), в пределах которых выполняется поиск метки времени. | Обязательный |
| Severity search chars limit `LAConfigSeverityDetectionLimit_Bytes` | integer | Задаёт количество символов в каждой строке журнала (начиная с первого символа), в пределах которых выполняется поиск уровня серьёзности. | Обязательный |
| Severity search lines limit `LAConfigSeverityDetectionLinesLimit` | integer | Задаёт количество первых строк каждой записи журнала, в пределах которых выполняется поиск уровня серьёзности. | Обязательный |
| Maximum number of log sources per process group instance `LAConfigMaxLgisPerEntityCount` | integer | Задаёт максимальное количество экземпляров группы журналов на объект, после достижения которого новые автоматические экземпляры не добавляются. | Обязательный |
| Windows Event Log query timeout `LAConfigEventLogQueryTimeout_Sec` | integer | Задаёт максимальное значение тайм-аута в секундах для запроса, извлекающего журналы событий Windows. | Обязательный |
| Minimal log file size to perform binary detection. `LAConfigMinBinaryDetectionLimit_Bytes` | integer | Задаёт минимальное количество байт в файле журнала, необходимое для обнаружения бинарного содержимого. | Обязательный |
| Binary detection mode `BinaryDetectionMode` | enum | Задаёт степень детализации обнаружения бинарных файлов журналов. 'Per log source' применяет обнаружение на уровне источника журнала, 'Per log file' оценивает каждый файл журнала отдельно. Элемент имеет следующие перечисляемые значения: * `BinaryPerLogSource` * `BinaryPerLogFile` | Обязательный |