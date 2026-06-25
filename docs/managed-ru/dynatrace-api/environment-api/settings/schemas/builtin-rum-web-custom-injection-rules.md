---
title: Settings API - Define custom injection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-injection-rules
scraped: 2026-05-12T11:40:37.172318
---

# Settings API - Define custom injection rules schema table

# Settings API - Define custom injection rules schema table

* Published Aug 26, 2024

### Задание правил пользовательского внедрения (`builtin:rum.web.custom-injection-rules)`

Задайте правила пользовательского внедрения, чтобы контролировать, когда и куда RUM автоматически внедряется в страницы приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-injection-rules` | * `group:rum-injection` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-injection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-injection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-injection-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить правило `enabled` | boolean | - | Required |
| Оператор `operator` | enum | **Пример**:  **Для URL:**  `http://www.example.com:8080/lorem/ipsum.jsp?mode=desktop`  Правило можно задать на URL-шаблоне:  `/lorem/ipsum.jsp`  С использованием оператора:  `URL ends with`  **Результат:**  если URL заканчивается на .jsp, не внедрять JavaScript-библиотеку Возможные значения: * `AllPages` * `Equals` * `Starts` * `Ends` * `Contains` | Required |
| URL-шаблон `urlPattern` | text | - | Required |
| Правило `rule` | enum | Возможные значения: * `Automatic` * `BeforeSpecificHtml` * `AfterSpecificHtml` * `DoNotInject` | Required |
| `htmlPattern` | text | - | Required |