---
title: Settings API - Red Hat Ansible Automation Controller Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-redhat-ansible-automation-controller-connection
scraped: 2026-05-12T11:44:30.489253
---

# Settings API - Red Hat Ansible Automation Controller Connections schema table

# Settings API - Red Hat Ansible Automation Controller Connections schema table

* Published Feb 26, 2024

### Подключения Red Hat Ansible Automation Controller (`app:dynatrace.redhat.ansible:automation-controller.connection)`

Подключения, содержащие access-токены для приложения Red Hat Ansible. Это подключение можно использовать для подключения к Red Hat Ansible Automation Controller, а также к проекту с открытым исходным кодом AWX.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.redhat.ansible:automation-controller.connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:automation-controller.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.redhat.ansible:automation-controller.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.redhat.ansible:automation-controller.connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Уникальное и однозначно идентифицируемое имя подключения. | Required |
| URL API `url` | text | URL эндпоинта API Ansible Automation Controller. Например, https://ansible.yourdomain.com/api/v2/ | Required |
| Тип `type` | enum | Тип используемого метода аутентификации. Возможные значения: * `api-token` | Required |
| Access-токен API `token` | secret | Access-токен API для Ansible Automation Controller. Обратите внимание, что этот токен не обновляется и может истечь. | Required |