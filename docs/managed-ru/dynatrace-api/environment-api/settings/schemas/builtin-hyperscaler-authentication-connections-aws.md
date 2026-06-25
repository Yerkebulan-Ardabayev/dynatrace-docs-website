---
title: Settings API - Connections to AWS environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hyperscaler-authentication-connections-aws
scraped: 2026-05-12T11:40:20.576212
---

# Settings API - Connections to AWS environments schema table

# Settings API - Connections to AWS environments schema table

* Published Sep 25, 2025

### Подключения к AWS-окружениям (`builtin:hyperscaler-authentication.connections.aws)`

Подключения к AWS для интеграций Dynatrace

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hyperscaler-authentication.connections.aws` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.aws` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.aws` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.aws` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Имя подключения | Required |
| Тип подключения `type` | enum | Механизм аутентификации AWS, используемый подключением Возможные значения: * `awsRoleBasedAuthentication` * `awsWebIdentity` | Required |
| `awsRoleBasedAuthentication` | [AwsRoleBasedAuthenticationConfig](#AwsRoleBasedAuthenticationConfig) | - | Required |
| `awsWebIdentity` | [AwsWebIdentity](#AwsWebIdentity) | - | Required |

##### Объект `AwsRoleBasedAuthenticationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ARN роли AWS IAM `roleArn` | text | ARN роли AWS, которую следует принять | Required |
| Потребители `consumers` | [ConsumersOfAwsRoleBasedAuthentication](#ConsumersOfAwsRoleBasedAuthentication)[] | Интеграции Dynatrace, которые могут использовать это подключение Возможные значения: * `DA` * `SVC:com.dynatrace.da` * `APP:dynatrace.biz.carbon` * `SVC:com.dynatrace.bo` * `SVC:com.dynatrace.openpipeline` * `SVC:com.dynatrace.grail` * `NONE` | Required |

##### Объект `AwsWebIdentity`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ARN роли AWS IAM `roleArn` | text | ARN роли AWS, которую следует принять | Required |
| Потребители `consumers` | [ConsumersOfAwsWebIdentity](#ConsumersOfAwsWebIdentity)[] | Интеграции Dynatrace, которые могут использовать это подключение Возможные значения: * `APP:dynatrace.aws.connector` * `APP:dynatrace.biz.carbon` | Required |