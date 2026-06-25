---
title: Settings API - AWS Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hyperscaler-authentication-aws-connection
scraped: 2026-05-12T11:46:33.555960
---

# Settings API - AWS Connections schema table

# Settings API - AWS Connections schema table

* Published Oct 14, 2024

### AWS Connections (`builtin:hyperscaler-authentication.aws.connection)`

Доступные подключения для [AWS for Workflows](https://dt-url.net/s803q9r). Подключение используется для аутентификации в AWS-аккаунте. Полученные временные учётные данные AWS применяются для выполнения действий AWS workflow.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hyperscaler-authentication.aws.connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.aws.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hyperscaler-authentication.aws.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.aws.connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Тип учётных данных `type` | enum | Возможные значения: * `webIdentity` | Required |
| `webIdentity` | [WebIdentity](#WebIdentity) | - | Required |

##### Объект `WebIdentity`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Role ARN `roleArn` | secret | ARN AWS-роли, которую следует принять | Required |
| Policy ARNs `policyArns` | list | Опциональный список политик, которыми можно ограничить AWS-роль | Required |