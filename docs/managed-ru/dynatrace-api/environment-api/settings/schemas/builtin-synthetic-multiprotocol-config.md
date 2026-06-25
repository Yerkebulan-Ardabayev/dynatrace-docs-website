---
title: Settings API - Network Availability monitor config schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-config
scraped: 2026-05-12T11:40:04.728920
---

# Settings API - Network Availability monitor config schema table

# Settings API - Network Availability monitor config schema table

* Published Jul 31, 2024

### Конфигурация Network Availability-монитора (`builtin:synthetic.multiprotocol.config)`

Network Availability-монитор

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.config` | * `group:synthetic.multiprotocol` | `MULTIPROTOCOL_MONITOR` - Network availability monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.config` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.config` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.config` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Монитор включён `enabled` | boolean | - | Required |
| Описание монитора `description` | text | - | Required |
| Шаги `steps` | [Step](#Step)[] | - | Required |
| Свойства монитора `properties` | Set<[Property](#Property)> | Опция пока не поддерживается | Required |

##### Объект `Step`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя шага `name` | text | - | Required |
| Тип запроса `requestType` | enum | Все шаги монитора должны быть одного типа запроса. Подробнее о типах запросов см. в [Dynatrace documentation](https://dt-url.net/0803zt8 "Visit Dynatrace documentation") Возможные значения: * `ICMP` * `TCP` * `DNS` | Required |
| Список целей `targetList` | set | - | Required |
| Фильтр целей `targetFilter` | text | Синтаксис и примеры см. в [Dynatrace documentation](https://dt-url.net/3443zor "Visit Dynatrace documentation") | Optional |
| Свойства конфигурации `properties` | Set<[Property](#Property)> | Возможные свойства конфигурации см. в [Dynatrace documentation](https://dt-url.net/gq83z4l "Visit Dynatrace documentation") | Required |
| Ограничения уровня шага `constraints` | Set<[Constraint](#Constraint)> | Возможные ограничения уровня шага см. в [Dynatrace documentation](https://dt-url.net/x3a3zev "Visit Dynatrace documentation") | Required |
| Конфигурация уровня запроса `requestConfigurations` | Set<[RequestConfiguration](#RequestConfiguration)> | Возможные конфигурации уровня запроса см. в [Dynatrace documentation](https://dt-url.net/b803zmi "Visit Dynatrace documentation") | Required |
| Скрипт перед выполнением `preScript` | text | Опция пока не поддерживается | Optional |
| Скрипт после выполнения `postScript` | text | Опция пока не поддерживается | Optional |

##### Объект `Property`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ свойства `key` | text | - | Required |
| Значение свойства `value` | text | - | Required |

##### Объект `Constraint`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип ограничения `type` | text | - | Required |
| Свойства `properties` | Set<[Property](#Property)> | - | Required |

##### Объект `RequestConfiguration`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ограничения запроса `constraints` | Set<[Constraint](#Constraint)> | - | Required |
| Свойства `properties` | Set<[Property](#Property)> | Опция пока не поддерживается | Required |
| Сопоставитель шаблона `patternMatcher` | text | Опция пока не поддерживается | Optional |