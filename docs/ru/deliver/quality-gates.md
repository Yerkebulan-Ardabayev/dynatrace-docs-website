---
title: Валидация выпуска
source: https://www.dynatrace.com/docs/deliver/quality-gates
scraped: 2026-03-06T21:30:00.295299
---

# Валидация релизов

Критически важные сервисы требуют автоматической валидации перед продакшеном. Основные инструменты Dynatrace:

* **Site Reliability Guardian** — автоматизирует проверку доступности, производительности, ёмкости и безопасности.
* **Workflows** — последовательность действий с триггерами (события, расписание, ручной запуск).

С помощью AutomationEngine и бизнес-событий в Grail вы автоматизируете валидацию, ускоряете развёртывание и повышаете качество.

> **Предупреждение:** Текущий подход использует бизнес-события. В будущем их заменит новый тип событий для жизненного цикла разработки.

## Шаги

### 1. Настройте CI/CD

CI/CD-инструмент (например, Jenkins) отправляет бизнес-события в Dynatrace через API бизнес-событий.

Показать код

```
#!groovy

/**
* Sends biz_event to a given Dynatrace environment.
* @param monitoringTenant url to monitoring environment
* @param oauthClientId OAuth client id
* @param oauthClientSecret OAuth client secret
* @param payload biz_event payload
* @return
*/
def call(
def monitoringTenant,
def oauthClientId,
def oauthClientSecret,
def payload
) {
// Get Access Token via OAuth
def ssoResponse = sh(script: """
set +x
curl --location --request POST 'https://sso.dynatrace.com/sso/oauth2/token' \\
--header 'Content-Type: application/x-www-form-urlencoded' \\
--data-urlencode 'grant_type=client_credentials' \\
--data-urlencode 'client_id=${oauthClientId}' \\
--data-urlencode 'client_secret=${oauthClientSecret}' \\
--data-urlencode 'scope=storage:events:write'
set -x
""", returnStdout: true).trim()

def ssoResponseJSON = readJSON(text: ssoResponse)
if (ssoResponseJSON.errorCode) {
error(message: "Authentication failed: ${ssoResponse}")
}
def accessToken = ssoResponseJSON.access_token

println("Sending BizEvent: ${payload}")
sh(script: """
set +x
curl --location --request POST '${monitoringTenant}/platform/classic/environment-api/v2/bizevents/ingest' \\
--header 'Content-Type: application/json' \\
--header 'Authorization: Bearer ${accessToken}' \\
--data-raw '${payload}'
set -x
""")
}
```

### 2. Отправьте бизнес-событие

Событие должно содержать контекст версии ПО и поле `execution_context`:

```
{
"timeframe.to": "2023-03-08T06:29:08.809Z",
"timeframe.from": "2023-03-08T05:29:08.809Z",
"event.id": "d08a70d8-f6de-4d0d-bd34-5d416a20ba6a",
"timestamp": 1678256963078000000,
"event.kind": "BIZ_EVENT",
"event.type": "guardian.validation.triggered",
"stage": "hardening",
"event.provider": "Jenkins",
"dt.system.bucket": "default_bizevents_short"
"execution_context": {
"buildId": "4711",
"version": "0.1.0"
}
```

### 3. Создайте guardian

Guardian запрашивает результаты из Grail и валидирует по целевым показателям. Подробнее: Create a Site Reliability guardian.

### 4. Создайте рабочий процесс

Настройте Workflow с триггером по событию:

```
((event.type == "guardian.validation.triggered") and stage == "dev")
```

Добавьте действие guardian, указывающее на созданный guardian.

### 5. Проверьте результаты

Запросите результаты из бизнес-событий:

```
query: fetch bizevents, from:now() - 5m, to:now()
| filter event.type == "guardian.validation.finished"
| filter event.provider == "dynatrace.site.reliability.guardian"
| filter guardian.name == "validation-guardian"
| filter matchesPhrase(execution_context, "1.286.0.0.20240129-160934")
| sort timestamp desc
limit 1 ,"timezone": "Europe/Warsaw", "enablePreview": true
```

### 6. Уведомление

При успехе запустите рабочий процесс с уведомлением через Slack, Microsoft Teams или Jira для одобрения продвижения.
