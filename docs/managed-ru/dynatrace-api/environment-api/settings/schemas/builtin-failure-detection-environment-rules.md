---
title: Settings API - Failure detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-environment-rules
scraped: 2026-05-12T11:42:47.155668
---

# Settings API - Failure detection rules schema table

# Settings API - Failure detection rules schema table

* Published Dec 05, 2023

### Правила обнаружения сбоев (`builtin:failure-detection.environment.rules)`

Настройте правила, к каким сервисам должны применяться конкретные параметры обнаружения сбоев (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.parameters`). Подробнее см. [Failure detection settings](https://dt-url.net/7v034gp).

Эти настройки не применяются к [Unified services](https://dt-url.net/gy03cmt).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.environment.rules` | * `group:service-monitoring` * `group:failure-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.environment.rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя правила `name` | text | - | Required |
| Описание правила `description` | text | - | Optional |
| Включено `enabled` | boolean | - | Required |
| Параметры обнаружения сбоев `parameterId` | setting | - | Required |
| Условия `conditions` | Set<[condition](#condition)> | - | Required |

##### Объект `condition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут `attribute` | enum | Проверяемый атрибут. Возможные значения: * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONE` * `SERVICE_NAME` * `SERVICE_TYPE` * `SERVICE_TAG` | Required |
| Условие проверки атрибута `predicate` | [predicate](#predicate) | - | Required |

##### Объект `predicate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип предиката `predicateType` | text | - | Required |
| Имена `textValues` | set | - | Required |
| С учётом регистра `caseSensitive` | boolean | - | Required |
| Типы сервисов `serviceType` | Set<[serviceTypes](#serviceTypes)> | Возможные значения: * `WebRequest` * `WebService` * `Database` * `Method` * `WebSite` * `Messaging` * `Mobile` * `Process` * `RMI` * `External` * `QueueListener` * `QueueInteraction` * `RemoteCall` * `SaasVendor` * `CustomApplication` * `CICS` * `IMS` * `CICSInteraction` * `IMSInteraction` * `EnterpriseServiceBus` * `zOSConnect` | Required |
| Management zones `managementZones` | set | - | Required |
| Теги (точное совпадение) `tags` | set | - | Required |
| Ключи тегов `tagKeys` | set | - | Required |