---
title: Settings API - Resource types schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-resource-types
scraped: 2026-05-12T11:44:37.343622
---

# Settings API - Resource types schema table

# Settings API - Resource types schema table

* Published Dec 05, 2023

### Типы ресурсов (`builtin:rum.web.resource-types)`

Dynatrace определяет типы ресурсов по расширениям файлов. Однако в некоторых случаях загруженные ресурсы могут не иметь корректных расширений. Для таких случаев можно задать правила, определяющие правильные типы этих ресурсов. Правила гарантируют, что разбивка по типам ресурсов рендерится корректно и типы ресурсов в waterfall-диаграмме отображаются правильно.

Dynatrace поддерживает синтаксис регулярных выражений Java. Типы ресурсов с URL-фрагментами, совпадающими с заданными регулярными выражениями, переопределяются значением из поля *Primary resource type* и могут дополнительно категоризироваться через *Secondary resource type*.

Введите *^.\*\.od.{1}$* в поле **Regular expression field**, выберите *Other* в качестве **Primary resource type** и введите *OpenDocument* в поле **Secondary resource type**, чтобы переопределить тип ресурса по умолчанию для ресурсов с расширением *.od*\*.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.resource-types` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.content-resources` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-types` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.resource-types` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-types` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Регулярное выражение `regularExpression` | text | Регулярное выражение для определения ресурса. | Required |
| Основной тип ресурса. `primaryResourceType` | enum | Возможные значения: * `CSS` * `IMAGE` * `SCRIPT` * `OTHER` | Required |
| Вторичный тип ресурса. `secondaryResourceType` | text | - | Optional |