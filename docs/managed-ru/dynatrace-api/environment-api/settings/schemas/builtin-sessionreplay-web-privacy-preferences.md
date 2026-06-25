---
title: Settings API - Session replay data privacy schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-sessionreplay-web-privacy-preferences
scraped: 2026-05-12T11:45:53.572444
---

# Settings API - Session replay data privacy schema table

# Settings API - Session replay data privacy schema table

* Published Dec 05, 2023

### Приватность данных Session Replay (`builtin:sessionreplay.web.privacy-preferences)`

[Configure Session Replay](https://dt-url.net/2i3t0pju), чтобы ограничить сбор данных и защитить приватность данных конечных пользователей.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:sessionreplay.web.privacy-preferences` | * `group:preferences` * `group:rum-settings` * `group:privacy-settings` | `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.privacy-preferences` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:sessionreplay.web.privacy-preferences` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.privacy-preferences` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить opt-in режим для Session Replay `enableOptInMode` | boolean | Когда [opt-in режим Session Replay](https://dt-url.net/sr-opt-in-mode) включён, Session Replay деактивирован до явной активации через вызов API. | Required |
| URL exclusion `urlExclusionPatternList` | set | Исключайте веб-страницы или views из записи Session Replay с помощью [URL exclusion rules](https://dt-url.net/sr-url-exclusion) | Required |
| Параметры маскирования контента `maskingPresets` | [MaskingPresetConfig](#MaskingPresetConfig) | Чтобы защитить приватность конечных пользователей, выберите или настройте [предопределённые опции маскирования](https://dt-url.net/sr-masking-preset-options), подходящие под ваши требования к записи и воспроизведению контента. | Required |

##### Объект `MaskingPresetConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Параметры маскирования при записи `recordingMaskingPreset` | enum | Параметры маскирования при записи применяются во время записи. При выборе более ограничительной опции та же опция включается и для параметров маскирования при воспроизведении. Возможные значения: * `MASK_ALL` * `MASK_USER_INPUT` * `ALLOW_LIST` * `BLOCK_LIST` | Required |
| Правила allow list `recordingMaskingAllowListRules` | Set<[AllowListRule](#AllowListRule)> | Элементы задаются CSS-селектором или именем атрибута. | Required |
| Правила block list `recordingMaskingBlockListRules` | Set<[BlockListRule](#BlockListRule)> | Элементы задаются CSS-селектором или именем атрибута. | Required |
| Параметры маскирования при воспроизведении `playbackMaskingPreset` | enum | Параметры маскирования при воспроизведении применяются во время воспроизведения записанных сессий, включая воспроизведение сессий, записанных до применения этих параметров. Возможные значения: * `MASK_ALL` * `MASK_USER_INPUT` * `ALLOW_LIST` * `BLOCK_LIST` | Required |
| Правила allow list `playbackMaskingAllowListRules` | Set<[AllowListRule](#AllowListRule)> | Элементы задаются CSS-селектором или именем атрибута. | Required |
| Правила block list `playbackMaskingBlockListRules` | Set<[BlockListRule](#BlockListRule)> | Элементы задаются CSS-селектором или именем атрибута. | Required |

##### Объект `AllowListRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Цель `target` | enum | Выберите тип цели правила маскирования Возможные значения: * `ELEMENT` * `ATTRIBUTE` | Required |
| CSS-селектор для идентификации элемента контента `cssExpression` | text | Маскирование контента применимо к веб-страницам с отображением персональных данных. Когда маскирование контента применяется к родительским элементам, все child-элементы маскируются по умолчанию. | Required |
| Имя атрибута (выражение) `attributeExpression` | text | Маскирование атрибутов применимо к веб-приложениям, хранящим данные внутри атрибутов, обычно атрибутов data-NAME в HTML5. При задании атрибутов их значения маскируются во время записи, но не удаляются. | Required |

##### Объект `BlockListRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Цель `target` | enum | Выберите тип цели правила маскирования Возможные значения: * `ELEMENT` * `ATTRIBUTE` | Required |
| CSS-селектор для идентификации элемента контента `cssExpression` | text | Маскирование контента применимо к веб-страницам с отображением персональных данных. Когда маскирование контента применяется к родительским элементам, все child-элементы маскируются по умолчанию. | Required |
| Имя атрибута (выражение) `attributeExpression` | text | Маскирование атрибутов применимо к веб-приложениям, хранящим данные внутри атрибутов, обычно атрибутов data-NAME в HTML5. При задании атрибутов их значения маскируются во время записи, но не удаляются. | Required |
| Скрыть пользовательское взаимодействие `hideUserInteraction` | boolean | Скрыть пользовательские взаимодействия с этими элементами, включая клики, разворачивающие элементы, подсветку при наведении курсора и выбор конкретных опций формы. | Required |