---
title: Settings API - Git On-Premise Servers schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-devobs-debugger-git-on-prem
scraped: 2026-05-12T11:40:16.692916
---

# Settings API - Git On-Premise Servers schema table

# Settings API - Git On-Premise Servers schema table

* Published Mar 17, 2025

### Git-серверы On-Premise (`app:dynatrace.devobs.debugger:git.on.prem)`

Укажите ваши Git-серверы On-Premise, чтобы можно было получать из них исходный код

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.devobs.debugger:git.on.prem` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.devobs.debugger:git.on.prem` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.devobs.debugger:git.on.prem` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.devobs.debugger:git.on.prem` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Провайдер Git `Provider` | enum | Провайдер git-сервиса для этого сервера Возможные значения: * `GithubOnPrem` * `GitlabOnPrem` * `BitbucketOnPrem` * `AzureOnPrem` | Required |
| URL сервера `Url` | text | HTTPS URL вашего сервера (HTTP не поддерживается). Укажите только базовый URL сервера, а не путь к конкретному проекту или репозиторию (например, https://git.example.com) | Required |
| Включить учётные данные `IncludeCredentials` | boolean | Если включено, запросы к вашему серверу Gitlab будут иметь опцию `credentials`, установленную в `include`. Иначе она будет установлена в `omit`. | Required |