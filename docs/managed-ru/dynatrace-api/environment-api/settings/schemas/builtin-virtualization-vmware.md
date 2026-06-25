---
title: Settings API - VMware schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-virtualization-vmware
scraped: 2026-05-12T11:48:53.597597
---

# Settings API - VMware schema table

# Settings API - VMware schema table

* Published Dec 05, 2023

### VMware (`builtin:virtualization.vmware)`

На этой странице подключите к Dynatrace VMware vCenter и отдельные ESXi-хосты для мониторинга. Для VMware-инстансов подключите все vCenter-серверы, управляющие виртуальными машинами, на которых установлен Dynatrace OneAgent. ESXi-хосты добавлять не нужно, если ими управляет vCenter-сервер, подключённый к Dynatrace.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:virtualization.vmware` | * `group:cloud-and-virtualization` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:virtualization.vmware` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:virtualization.vmware` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:virtualization.vmware` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя подключения `label` | text | - | Required |
| Укажите IP-адрес или имя vCenter или отдельного ESXi-хоста: `ipaddress` | text | - | Required |
| Укажите учётные данные пользователя для vCenter или отдельного ESXi-хоста: `username` | text | - | Required |
| `password` | secret | - | Required |
| Задайте условие фильтра, чтобы ограничить количество мониторимых кластеров: `filter` | text | Строка должна иметь один из форматов:  * $prefix(parameter) - значение свойства начинается с 'parameter' * $eq(parameter) - значение свойства точно совпадает с 'parameter' * $suffix(parameter) - значение свойства заканчивается на 'parameter' * $contains(parameter) - значение свойства содержит 'parameter' | Optional |