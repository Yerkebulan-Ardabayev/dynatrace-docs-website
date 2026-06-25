---
title: Settings API - Disk Analytics Extension schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-disk-analytics-extension
scraped: 2026-05-12T11:39:48.861679
---

# Settings API - Disk Analytics Extension schema table

# Settings API - Disk Analytics Extension schema table

* Published Dec 05, 2023

### Расширение Disk Analytics (`builtin:disk.analytics.extension)`

Это расширение даёт более детальную видимость локальных хранилищ данных, их томов, разделов и raid-устройств на Linux-хостах.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:disk.analytics.extension` | * `group:preferences` | `HOST` - Host  `HOST_GROUP` - Host Group |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.analytics.extension` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:disk.analytics.extension` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.analytics.extension` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить сбор данных Disk Analytics `diskDeviceMonitoringExtensionActive` | boolean | Функция Disk Analytics требует добавления расширения в окружение. Расширение Disk Analytics можно добавить из Dynatrace Hub (`<your-dynatrace-url>//ui/hub/ext/com.dynatrace.extension.disk-devices#information`). Расширение Disk Analytics расходует пользовательские метрики и [Davis data units](https://www.dynatrace.com/support/help/shortlink/metric-cost-calculation).  После добавления расширения Disk Analytics можно включить Data Collection в настройках уровня host или host-group. Если включить Data Collection без добавления расширения, данные будут видны только в data explorer.  Подробнее см. [Disk Analytics extension documentation](https://dt-url.net/3a03v9v). | Required |