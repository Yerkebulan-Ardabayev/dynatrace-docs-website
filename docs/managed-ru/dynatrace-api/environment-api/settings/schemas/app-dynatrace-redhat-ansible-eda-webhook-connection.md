---
title: Settings API - Red Hat Event-Driven Ansible Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-redhat-ansible-eda-webhook-connection
scraped: 2026-05-12T11:40:02.821777
---

# Settings API - Red Hat Event-Driven Ansible Connections schema table

# Settings API - Red Hat Event-Driven Ansible Connections schema table

* Published Apr 22, 2024

### Подключения Red Hat Event-Driven Ansible (`app:dynatrace.redhat.ansible:eda-webhook.connection)`

Подключения, содержащие access-токены для приложения Red Hat Ansible. Это подключение можно использовать для подключения к плагину DT Event-Driven в составе Red Hat Event-Driven Ansible.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.redhat.ansible:eda-webhook.connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:eda-webhook.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.redhat.ansible:eda-webhook.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:eda-webhook.connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Уникальное и однозначно идентифицируемое имя подключения. | Required |
| Использовать Red Hat Event Streams `eventStreamEnabled` | boolean | Флаг, используется ли Red Hat Event Stream для Event-Driven Ansible | Optional |
| URL API `url` | text | URL вебхука плагина-источника Event-Driven Ansible. Например, https://eda.yourdomain.com:5010 | Required |
| Тип `type` | enum | Тип используемого метода аутентификации. Возможные значения: * `api-token` | Required |
| Access-токен API `token` | secret | Access-токен API для Event-Driven Ansible Controller. Обратите внимание, что этот токен не обновляется и может истечь. | Required |