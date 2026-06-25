---
title: Settings API - Remote environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-remote-environment
scraped: 2026-05-12T11:45:35.130966
---

# Settings API - Remote environments schema table

# Settings API - Remote environments schema table

* Published Dec 05, 2023

### Удалённые окружения (`builtin:remote.environment)`

Настройте подключения к другим окружениям Dynatrace для межсредовых возможностей (например, дашбордов)

О работе с удалёнными окружениями см. [Remote environment API documentation](https://dt-url.net/lc5n0p4z)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:remote.environment` | * `group:integration.external` * `group:integration` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:remote.environment` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:remote.environment` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:remote.environment` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| URI удалённого окружения `uri` | text | Укажите полный URI удалённого окружения. Локальное окружение должно иметь возможность сетевого подключения к этому URI. | Required |
| Сетевая область `networkScope` | enum | * External: удалённое окружение находится в другой сети. * Internal: удалённое окружение находится в той же сети. * Cluster: удалённое окружение находится в том же кластере.  Dynatrace SaaS поддерживает только External. Возможные значения: * `EXTERNAL` * `INTERNAL` * `CLUSTER` | Required |
| Токен `token` | secret | Укажите валидный токен, созданный в удалённом окружении. | Required |