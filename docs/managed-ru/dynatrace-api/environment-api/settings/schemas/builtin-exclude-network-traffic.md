---
title: Settings API - Exclude network traffic schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-exclude-network-traffic
scraped: 2026-05-12T11:40:31.972455
---

# Settings API - Exclude network traffic schema table

# Settings API - Exclude network traffic schema table

* Published Dec 05, 2023

### Исключение сетевого трафика (`builtin:exclude.network.traffic)`

OneAgent автоматически обнаруживает и мониторит весь сетевой трафик, но трафик на определённых сетевых интерфейсах или хостах можно исключить из мониторинга.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:exclude.network.traffic` | * `group:monitoring` | `HOST` - Host |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:exclude.network.traffic` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:exclude.network.traffic` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:exclude.network.traffic` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Исключить NIC `excludeNic` | [NicForm](#NicForm)[] | Выбирая сетевой интерфейс, вы исключите весь сетевой трафик на этом интерфейсе из мониторинга. Можно выбрать из списка ниже что не мониторить или ввести вручную через опцию "other one". | Required |
| Исключить IP `excludeIp` | [IpAddressForm](#IpAddressForm)[] | При указании IP-адреса хоста сетевой трафик исключается только при расчёте connectivity (другие метрики всё равно рассчитываются). | Required |

##### Объект `NicForm`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Операционная система `os` | enum | Возможные значения: * `OS_TYPE_UNKNOWN` * `OS_TYPE_AIX` * `OS_TYPE_DARWIN` * `OS_TYPE_HPUX` * `OS_TYPE_LINUX` * `OS_TYPE_SOLARIS` * `OS_TYPE_WINDOWS` * `OS_TYPE_ZOS` | Required |
| Сетевой интерфейс `interface` | text | - | Required |

##### Объект `IpAddressForm`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| IP-адрес `ipAddress` | text | - | Required |