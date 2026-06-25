---
title: Settings API - Automatic injection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-automatic-injection
scraped: 2026-05-12T11:40:49.056289
---

# Settings API - Automatic injection schema table

# Settings API - Automatic injection schema table

* Published Mar 17, 2025

### Автоматическая инъекция (`builtin:rum.web.automatic-injection)`

Dynatrace OneAgent автоматически инжектит RUM-JavaScript в HTML-head страниц мониторимых приложений. На этой странице можно управлять инъекцией и настраивать её.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.automatic-injection` | * `group:rum-injection` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.automatic-injection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.automatic-injection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.automatic-injection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Источник Real User Monitoring-кода `monitoringCodeSourceSection` | [MonitoringCodeSource](#MonitoringCodeSource) | - | Required |
| Формат сниппета `snippetFormat` | [SnippetFormat](#SnippetFormat) | *Code Snippet:* OneAgent инжектит inline-скрипт, который инициализирует Dynatrace и динамически загружает monitoring-код в ваше приложение. Используйте, если нужно инжектить monitoring-код в deferred-режиме.  *Inline Code:* OneAgent инжектит конфигурацию и monitoring-код inline в ваше приложение. Используйте этот тип инъекции, когда нужно минимизировать число web-запросов.  *OneAgent JavaScript Tag:* OneAgent инжектит в ваше приложение JavaScript-тег, содержащий конфигурацию и ссылку на monitoring-код. Это наш тип инъекции по умолчанию как самый универсальный.  *OneAgent JavaScript tag with SRI:* OneAgent инжектит конфигурацию, ссылку на внешний файл с monitoring-кодом и хеш, позволяющий браузеру проверить целостность monitoring-кода до его выполнения.  Сравните разные [форматы инъекции](https://dt-url.net/vx5g0ptn). | Required |
| Заголовки cache control `cacheControlHeaders` | [CacheControlHeaders](#CacheControlHeaders) | - | Required |

##### Объект `MonitoringCodeSource`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Источник Real User Monitoring-кода `codeSource` | text | - | Required |
| Укажите путь для RUM monitoring-кода `monitoringCodePath` | text | Укажите URL-путь, по которому запрашивается RUM monitoring-код. По умолчанию путь установлен в root или context root. Пользовательский URL-путь может потребоваться, если ваш сервер работает за firewall. | Optional |

##### Объект `SnippetFormat`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Формат сниппета `snippetFormat` | text | - | Required |
| Загружать monitoring-код `codeSnippetType` | enum | Возможные значения: * `SYNCHRONOUSLY` * `DEFERRED` | Required |
| Атрибут выполнения скрипта `scriptExecutionAttribute` | enum | Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его немедленно по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы. Возможные значения: * `async` * `defer` * `none` | Optional |

##### Объект `CacheControlHeaders`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оптимизировать значение заголовков cache control для использования с Dynatrace Real User Monitoring `cacheControlHeaders` | boolean | [Как обеспечить своевременные обновления конфигурации для автоматической инъекции?](https://dt-url.net/m9039ea) | Required |