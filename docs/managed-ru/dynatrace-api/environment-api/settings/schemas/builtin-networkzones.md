---
title: Settings API - Network zones settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-networkzones
scraped: 2026-05-12T11:47:57.743992
---

# Settings API - Network zones settings schema table

# Settings API - Network zones settings schema table

* Published Dec 05, 2023

### Настройки network zones (`builtin:networkzones)`

В сочетании с ActiveGate, network zones экономят полосу пропускания и затраты на инфраструктуру за счёт:

* Сжатия трафика
* Оптимизации маршрутизации трафика
* Предотвращения нерелевантного трафика между ЦОД и регионами

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:networkzones` | * `group:preferences` | `environment`  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:networkzones` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:networkzones` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:networkzones` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить network zones в этом окружении.  `enabled` | boolean | Подробнее см. [Network zones](https://www.dynatrace.com/support/help/shortlink/network-zones).  â  Внимание: при резком отключении network zones в окружении с большим числом OneAgent, имеющих конфигурацию network zone, возможен сетевой дисбаланс. Чтобы избежать этого и обеспечить плавное внедрение network zones, следуйте практикам по планированию и правильному именованию, описанным в [Network zones](https://www.dynatrace.com/support/help/shortlink/network-zones). | Required |