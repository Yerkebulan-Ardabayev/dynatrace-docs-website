---
title: Settings API - Provider breakdown schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-provider-breakdown
scraped: 2026-05-12T11:41:38.213402
---

# Settings API - Provider breakdown schema table

# Settings API - Provider breakdown schema table

* Published Dec 05, 2023

### Разбивка по провайдерам (`builtin:rum.provider-breakdown)`

Настройте правила, определяющие как загружаемые ресурсы контента приложений (изображения, CSS, сторонние виджеты и т.п.) отображаются и категоризируются для анализа.

Dynatrace использует имена хостов провайдеров загруженных ресурсов, чтобы категоризировать ресурсы контента как сторонние, CDN или first-party.

Dynatrace автоматически определяет более 1000 провайдеров контента «из коробки», включая Google, Amazon, Facebook и многих других. Никаких действий для настройки определения ресурсов не требуется. Если вашего провайдера нет в списке ниже, добавьте его вручную. Подробнее см. [Configure 3rd-party and CDN content detection](https://dt-url.net/on02tdo).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.provider-breakdown` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.content-resources` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.provider-breakdown` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.provider-breakdown` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.provider-breakdown` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя ресурса `resourceName` | text | - | Required |
| Тип ресурса `resourceType` | enum | Возможные значения: * `FirstParty` * `ThirdParty` * `Cdn` | Required |
| Укажите URL иконки бренда провайдера `iconUrl` | text | - | Optional |
| Шаблон доменного имени `domainNamePatternList` | Set<[DomainNamePatternListObject](#DomainNamePatternListObject)> | - | Required |
| Отправить шаблон провайдера для улучшения автоопределения `reportPublicImprovement` | boolean | Отправить шаблоны этого провайдера в Dynatrace, чтобы помочь улучшить 3rd-party-обнаружение. | Required |

##### Объект `DomainNamePatternListObject`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Введите шаблон доменного имени `domainNamePattern` | text | Используйте шаблон ends-with для домена этого провайдера контента | Required |