---
title: Settings API - GitLab Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-gitlab-connector-connection
scraped: 2026-05-12T11:41:04.635860
---

# Settings API - GitLab Connections schema table

# Settings API - GitLab Connections schema table

* Published Jul 31, 2024

### Подключения GitLab (`app:dynatrace.gitlab.connector:connection)`

Подключения, содержащие access-токены для платформы GitLab

(подробнее в [документации по GitLab API](https://docs.gitlab.com/ee/api/rest/ "Открыть документ GitLab"))

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.gitlab.connector:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.gitlab.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.gitlab.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.gitlab.connector:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Уникальное и однозначно идентифицируемое имя подключения к вашему инстансу GitLab. | Required |
| URL GitLab `url` | text | Инстанс GitLab по URL, к которому нужно подключиться. Например, https://gitlab.com  Укажите префикс http(s):// | Required |
| Токен GitLab `token` | secret | Токен GitLab, используемый для аутентификации. Обратите внимание, что этот токен не обновляется и может истечь.  Токен GitLab в виде `******`. Пока не secret из-за проблем с его получением через функции API | Required |