---
title: Settings API - Network connection monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-network-connection-monitoring
---

# Settings API - Network connection monitoring schema table

# Settings API - Network connection monitoring schema table

* Опубликовано 25 сентября 2025 г.

### Network connection monitoring (`builtin:network-connection-monitoring)`

OneAgent автоматически отслеживает критический сетевой трафик на хостах. Эти настройки можно переопределить на уровне группы хостов и хоста.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:network-connection-monitoring` | * `group:network-and-discovery` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получение схемы через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:network-connection-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:network-connection-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:network-connection-monitoring` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия **Read settings** (`settings.read`). О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable OneAgent network connection monitoring `enabled` | boolean | Если отключено, OneAgent не будет собирать сетевые данные о критическом трафике. По умолчанию включено. Расходует лицензирование Events powered by Grail. Требует OneAgent версии 1.337+ | Required |
| IP Filter `ipFilterMode` | enum | Выбор IP-адресов, которые будут включены в мониторинг сетевых подключений. Доступные варианты: все, только публичный трафик (все глобально маршрутизируемые адреса), только приватный трафик (адреса в пределах приватных диапазонов IPv4 или IPv6: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, fd00::/8), пользовательское исключение или пользовательское включение. Элемент имеет следующие enum-значения: * `all` * `private` * `public` * `inclusion` * `exclusion` | Required |
| IP addresses: `IPaddresses` | text | Используй CIDR-нотацию через запятую, например 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16  IP-адреса для включения или исключения | Required |
| Reported connections `reportedConnections` | enum | Определяет, какие подключения должны передаваться в отчётах. По умолчанию используются Critical connections, при этом передаются только отказы подключения (connection refused) для новых подключений и сброс подключения (connection reset) для существующих. Опционально можно передавать все подключения или задать пользовательские пороги. Элемент имеет следующие enum-значения: * `all` * `auto` * `custom` | Required |
| Reported connections thresholds `reportedConnectionsThresholds` | [reportedConnectionsThresholds](#reportedConnectionsThresholds) | Если превышен любой из порогов, подключение передаётся в отчёте. | Required |
| Aggregation `aggregation` | [aggregationParams](#aggregationParams) | - | Required |
| Enable classic OneAgent process connection monitoring `enabledClassic` | boolean | Классический мониторинг подключений процессов OneAgent несовместим с Grail и в дальнейшем будет удалён. Эти метрики используются только на экране Process Connections в рамках Classic Host Networking. По умолчанию отключено. | Required |

##### Объект `reportedConnectionsThresholds`

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Bytes threshold [bytes] `bytesThreshold` | integer | - | Required |
| Connectivity threshold [%] `connectivityThreshold` | float | - | Required |
| Retransmissions threshold [%] `retransmissionsThreshold` | float | - | Required |
| RTT (round trip time) threshold [ms] `rttThreshold` | integer | - | Required |

##### Объект `aggregationParams`

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Aggregation interval [min.] `interval` | integer | Агрегирует похожие записи о подключениях в пределах интервала. Допустимый диапазон: 1-10 мин.  Агрегирует похожие записи о подключениях в пределах интервала. Например, 20 подключений от одного и того же процесса-источника к одному и тому же IP-адресу и порту назначения будут агрегированы в одну запись лога со значением count=20. 1 минута используется по умолчанию и рекомендуется. | Required |
| Rate limit `rateLimit` | integer | Лимит частоты для подключений, передаваемых в отчётах, на хост в минуту. По умолчанию 100. | Required |