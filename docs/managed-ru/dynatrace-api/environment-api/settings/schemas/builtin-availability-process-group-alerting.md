---
title: Settings API - Process group availability monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-availability-process-group-alerting
scraped: 2026-05-12T11:48:48.857494
---

# Settings API - Process group availability monitoring schema table

# Settings API - Process group availability monitoring schema table

* Published Dec 05, 2023

### Мониторинг доступности process group (`builtin:availability.process-group-alerting)`

Dynatrace непрерывно мониторит доступность этой process group. Используйте настройки ниже, чтобы определить подход Dynatrace к мониторингу доступности этой process group.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:availability.process-group-alerting` | - | `PROCESS_GROUP` - Process Group |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:availability.process-group-alerting` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:availability.process-group-alerting` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:availability.process-group-alerting` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить мониторинг доступности process group `enabled` | boolean | - | Required |
| Открывать новую проблему `alertingMode` | enum | **если любой процесс становится недоступным:** Dynatrace откроет новую проблему, если один процесс в этой группе остановится или упадёт.  **если минимальный порог не достигнут:** Dynatrace отслеживает количество инстансов процесса, составляющих эту process group, и рассматривает группу как кластер. Эта настройка позволяет задать минимальное количество инстансов процесса, которые должны быть доступны. Проблема будет открыта, если в этой process group меньше требуемого минимального количества инстансов процесса.  Детали влияния на сервисные запросы будут включены в сводку проблемы.  **Примечание:** если процесс намеренно остановлен или выведен из эксплуатации при активной настройке, вам нужно вручную закрыть проблему. Возможные значения: * `ON_PGI_UNAVAILABILITY` * `ON_INSTANCE_COUNT_VIOLATION` | Required |
| Открыть новую проблему, если количество активных инстансов процесса в группе меньше чем: `minimumInstanceThreshold` | integer | - | Required |