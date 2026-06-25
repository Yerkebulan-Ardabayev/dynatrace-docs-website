---
title: Settings API - Issue-tracking for releases schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-issue-tracking-integration
scraped: 2026-05-12T11:46:09.191739
---

# Settings API - Issue-tracking for releases schema table

# Settings API - Issue-tracking for releases schema table

* Published Dec 05, 2023

### Issue-tracking для релизов (`builtin:issue-tracking.integration)`

Опрашивайте любую issue-tracking-систему, чтобы загружать статистику по issue для мониторимых сущностей в Dynatrace для анализа релизов. Подробнее см. [Issue-tracking integration](https://dt-url.net/releasesissuetracker).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:issue-tracking.integration` | * `group:cloud-automation.releases` * `group:cloud-automation` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:issue-tracking.integration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:issue-tracking.integration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:issue-tracking.integration` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Метка issue `issuelabel` | text | Задайте метку для идентификации этих issue, например `release_blocker` или `non-critical` | Required |
| Запрос issue `issuequery` | text | Можно использовать следующие placeholder'ы, чтобы автоматически подставлять значения со страницы **Release monitoring** в запрос: `{NAME}`, `{VERSION}`, `{STAGE}`, `{PRODUCT}`. | Required |
| Тип issue `issuetheme` | enum | Выберите тип отображаемой issue. Возможные значения: * `INFO` * `ERROR` * `RESOLVED` | Required |
| Issue-tracking-система `issuetrackersystem` | enum | Выберите issue-tracking-систему, которую хотите опрашивать. Возможные значения: * `JIRA` * `GITHUB` * `GITLAB` * `SERVICENOW` * `JIRA_ON_PREMISE` * `JIRA_CLOUD` | Required |
| Целевой URL `url` | text | Для Jira используйте базовый URL (например, https://jira.yourcompany.com); для GitHub URL репозитория (например, https://github.com/org/repo); для GitLab project-specific API для одного проекта (например, https://gitlab.com/api/v4/projects/:projectId) и group-specific API для нескольких проектов (например, https://gitlab.com/api/v4/groups/:groupId); для ServiceNow URL вашего инстанса (например, https://yourinstance.service-now.com/) | Required |
| Имя пользователя `username` | text | - | Required |
| Пароль `password` | secret | - | Optional |
| Токен `token` | secret | - | Optional |