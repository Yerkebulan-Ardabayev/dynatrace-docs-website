---
title: Settings API - Process instance snapshots schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-visibility
scraped: 2026-05-12T11:45:36.988981
---

# Settings API - Process instance snapshots schema table

# Settings API - Process instance snapshots schema table

* Published Dec 05, 2023

### Снимки экземпляров процессов (`builtin:process-visibility)`

Если эта функция включена, Dynatrace исследует наиболее ресурсоёмкие процессы, запущенные на хосте, и процессы, мониторимые через **Process availability**.
Когда происходит триггерное событие, метрики этих процессов за 10 минут до и 10 минут после события отправляются в кластер.

Доступен график потребления ресурсов по процессам.

Если **Process instance snapshots** запускается через **Process availability**, можно увидеть поведение процессов перед их завершением, а также перезапустились ли они в течение 10 минут.

Сообщаемые метрики процесса:

* Использование CPU (%)
* Использование памяти (B)
* Входящий сетевой трафик (KB)
* Исходящий сетевой трафик (KB)

Метрики сообщаются раз в минуту и покрывают количество процессов, заданное в **Reported processes limit**.

Каждый хост может сообщать до 60 минут таких метрик в день. При превышении лимита метрики не отправляются, даже если возникает новое событие.

События, запускающие **Process instance snapshots**:

* Высокое использование CPU хоста
* Высокая нагрузка системы
* Высокое использование памяти хоста
* Высокий процент потери пакетов
* Высокая утилизация NIC
* Большое количество ошибок NIC
* Ручные запросы
* События Process availability

Подробнее см. [Process instance snapshots](https://dt-url.net/yw02uea)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-visibility` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-visibility` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-visibility` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-visibility` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Process instance snapshots `enabled` | boolean | - | Required |
| Лимит сообщаемых процессов `maxProcesses` | integer | Максимальное количество процессов, которое может сообщать хост: **100** | Required |