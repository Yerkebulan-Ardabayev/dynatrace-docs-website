---
title: Content resources API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/content-resources/get-configuration
scraped: 2026-05-12T11:18:56.999603
---

# Content resources API - GET configuration

# Content resources API - GET configuration

* Reference
* Published Sep 23, 2020

Возвращает конфигурацию провайдеров контента в вашем окружении Dynatrace.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/contentResources` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/contentResources` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ContentResources](#openapi-definition-ContentResources) | Успех |

### Объекты тела ответа

#### Объект `ContentResources`

Конфигурация ресурсов контента.

| Элемент | Тип | Описание |
| --- | --- | --- |
| resourceProviders | [ResourceProvider[]](#openapi-definition-ResourceProvider) | Упорядоченный список вручную добавленных провайдеров контента.  Правила оцениваются сверху вниз; применяется первое подходящее правило. |
| resourceTypes | [ResourceType[]](#openapi-definition-ResourceType) | Упорядоченный список вручную заданных типов ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило. |
| resourceUrlCleanupRules | [ResourceUrlCleanupRule[]](#openapi-definition-ResourceUrlCleanupRule) | Упорядоченный список правил очистки URL ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило. |

#### Объект `ResourceProvider`

Правило для провайдера контента.

| Элемент | Тип | Описание |
| --- | --- | --- |
| brandIconUrl | string | URL иконки провайдера. |
| domainNamePatterns | string[] | Список доменных шаблонов провайдера. |
| resourceName | string | Имя провайдера. |
| resourceType | string | Тип провайдера. Возможные значения: * `CDN_RESOURCES` * `FIRST_PARTY_RESOURCES` * `THIRD_PARTY_RESOURCES` |

#### Объект `ResourceType`

Правило для типа ресурса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| primaryResourceType | string | Основной тип ресурса. Возможные значения: * `CSS` * `IMAGE` * `OTHER` * `SCRIPT` |
| regularExpression | string | Регулярное выражение для обнаружения ресурса. |
| secondaryResourceType | string | Вторичный тип ресурса. |

#### Объект `ResourceUrlCleanupRule`

Правило очистки URL.

| Элемент | Тип | Описание |
| --- | --- | --- |
| regularExpression | string | Шаблон (регулярное выражение) для поиска. |
| replaceWith | string | Текст для замены найденного шаблона. |
| resourceName | string | Имя правила. |

### JSON-модели тела ответа

```
{



"resourceProviders": [



{



"brandIconUrl": "string",



"domainNamePatterns": [



"string"



],



"resourceName": "string",



"resourceType": "CDN_RESOURCES"



}



],



"resourceTypes": [



{



"primaryResourceType": "CSS",



"regularExpression": "string",



"secondaryResourceType": "string"



}



],



"resourceUrlCleanupRules": [



{



"regularExpression": "string",



"replaceWith": "string",



"resourceName": "string"



}



]



}
```

## Связанные темы

* [Настройка обнаружения ресурсов первой, сторонних сторон и CDN для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших веб-приложений.")
* [Настройка определения собственных, сторонних ресурсов и ресурсов CDN для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших мобильных приложений.")
* [Настройка обнаружения ресурсов первой стороны, сторонних ресурсов и CDN в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших пользовательских приложений.")