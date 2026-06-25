---
title: Settings API - Manual insertion schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-manual-insertion
scraped: 2026-05-12T11:39:14.492588
---

# Settings API - Manual insertion schema table

# Settings API - Manual insertion schema table

* Published Aug 04, 2025

### Ручная вставка (`builtin:rum.web.manual-insertion)`

Вручную вставьте один из приведённых ниже форматов сниппета на страницы вашего приложения. Подробнее о разных [snippet formats](https://dt-url.net/vx5g0ptn). Все форматы также доступны через [API](https://dt-url.net/oz43wab), что позволяет автоматизировать их вставку в рамках процесса сборки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.manual-insertion` | * `group:rum-injection` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.manual-insertion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.manual-insertion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.manual-insertion` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Javascript-тег `javascriptTag` | [javascriptTag](#javascriptTag) | JavaScript-тег ссылается на внешний файл с monitoring-кодом и конфигурацией. Благодаря механизму динамического обновления он рекомендуется для большинства случаев. | Required |
| OneAgent JavaScript-тег `oneagentJavascriptTag` | [oneagentJavascriptTag](#oneagentJavascriptTag) | OneAgent JavaScript-тег содержит конфигурацию и ссылку на внешний файл с monitoring-кодом. Его нужно обновлять после изменений конфигурации и обновлений monitoring-кода. | Required |
| OneAgent JavaScript-тег с SRI `oneagentJavascriptTagSRI` | [oneagentJavascriptTagSRI](#oneagentJavascriptTagSRI) | OneAgent JavaScript-тег с SRI содержит конфигурацию, ссылку на внешний файл с monitoring-кодом и хеш, позволяющий браузеру проверить целостность monitoring-кода до его выполнения. Его нужно обновлять после изменений конфигурации и обновлений monitoring-кода. | Required |
| Code Snippet `codeSnippet` | [codeSnippet](#codeSnippet) | Code snippet, это фрагмент inline-кода, реализующий базовый функционал и загружающий полный функционал синхронно или отложенно. Даже несмотря на встроенный механизм обновлений, регулярные обновления нужны для гарантии совместимости. | Required |

##### Объект `javascriptTag`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Кэшировать monitoring-код и конфигурацию на `cacheDuration` | enum | Возможные значения: * `1` * `3` * `6` * `12` * `24` * `72` * `144` | Required |
| Атрибут выполнения скрипта `scriptExecutionAttribute` | enum | Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его сразу по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы. Возможные значения: * `async` * `defer` * `none` | Optional |
| Добавить атрибут crossorigin=anonymous `crossoriginAnonymous` | boolean | Добавьте атрибут `crossorigin=anonymous`, чтобы захватывать сообщения JavaScript-ошибок и W3C resource timings | Required |

##### Объект `oneagentJavascriptTag`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут выполнения скрипта `scriptExecutionAttribute` | enum | Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его сразу по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы Возможные значения: * `async` * `defer` * `none` | Optional |

##### Объект `oneagentJavascriptTagSRI`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут выполнения скрипта `scriptExecutionAttribute` | enum | Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его сразу по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы Возможные значения: * `async` * `defer` * `none` | Optional |

##### Объект `codeSnippet`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Загружать monitoring-код `codeSnippetType` | enum | Возможные значения: * `SYNCHRONOUSLY` * `DEFERRED` | Required |