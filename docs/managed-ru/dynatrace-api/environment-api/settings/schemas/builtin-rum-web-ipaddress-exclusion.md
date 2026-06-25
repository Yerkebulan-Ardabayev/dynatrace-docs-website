---
title: Settings API - Exclude IP addresses from monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-ipaddress-exclusion
scraped: 2026-05-12T11:39:00.784810
---

# Settings API - Exclude IP addresses from monitoring schema table

# Settings API - Exclude IP addresses from monitoring schema table

* Published Dec 05, 2023

### Исключение IP-адресов из мониторинга (`builtin:rum.web.ipaddress-exclusion)`

Включите переключатель ниже, если IP-адреса должны быть включены. Выключите его, если они должны быть исключены.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.ipaddress-exclusion` | * `group:capturing` * `group:capturing.exclusions` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.ipaddress-exclusion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.ipaddress-exclusion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.ipaddress-exclusion` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Список исключения IP-адресов `ipExclusionList` | [IpAddressExclusionRule](#IpAddressExclusionRule)[] | **Примеры:**  * 84.112.10.5 * fe80::10a1:c6b2:5f68:785d | Required |
| Это единственные IP-адреса, которые должны быть в мониторинге `ipAddressExclusionInclude` | boolean | - | Required |

##### Объект `IpAddressExclusionRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Одиночный IP или начальный адрес диапазона `ip` | text | - | Required |
| Конец диапазона IP `ipTo` | text | - | Optional |