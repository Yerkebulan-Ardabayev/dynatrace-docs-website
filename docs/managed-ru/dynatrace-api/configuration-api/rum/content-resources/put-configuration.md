---
title: Content resources API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/content-resources/put-configuration
scraped: 2026-05-12T11:18:55.563947
---

# Content resources API - PUT configuration

# Content resources API - PUT configuration

* Reference
* Published Sep 23, 2020

Обновляет конфигурацию провайдеров контента в вашем окружении Dynatrace.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/contentResources` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/contentResources` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ContentResources](#openapi-definition-ContentResources) | JSON-тело запроса. Содержит конфигурацию ресурсов контента. | body | Optional |

### Объекты тела запроса

#### Объект `ContentResources`

Конфигурация ресурсов контента.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| resourceProviders | [ResourceProvider[]](#openapi-definition-ResourceProvider) | Упорядоченный список вручную добавленных провайдеров контента.  Правила оцениваются сверху вниз; применяется первое подходящее правило. | Optional |
| resourceTypes | [ResourceType[]](#openapi-definition-ResourceType) | Упорядоченный список вручную заданных типов ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило. | Optional |
| resourceUrlCleanupRules | [ResourceUrlCleanupRule[]](#openapi-definition-ResourceUrlCleanupRule) | Упорядоченный список правил очистки URL ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило. | Optional |

#### Объект `ResourceProvider`

Правило для провайдера контента.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| brandIconUrl | string | URL иконки провайдера. | Optional |
| domainNamePatterns | string[] | Список доменных шаблонов провайдера. | Required |
| resourceName | string | Имя провайдера. | Required |
| resourceType | string | Тип провайдера. Возможные значения: * `CDN_RESOURCES` * `FIRST_PARTY_RESOURCES` * `THIRD_PARTY_RESOURCES` | Required |

#### Объект `ResourceType`

Правило для типа ресурса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| primaryResourceType | string | Основной тип ресурса. Возможные значения: * `CSS` * `IMAGE` * `OTHER` * `SCRIPT` | Required |
| regularExpression | string | Регулярное выражение для обнаружения ресурса. | Required |
| secondaryResourceType | string | Вторичный тип ресурса. | Optional |

#### Объект `ResourceUrlCleanupRule`

Правило очистки URL.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| regularExpression | string | Шаблон (регулярное выражение) для поиска. | Required |
| replaceWith | string | Текст для замены найденного шаблона. | Required |
| resourceName | string | Имя правила. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/contentResources/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/contentResources/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Настройка обнаружения ресурсов первой, сторонних сторон и CDN для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших веб-приложений.")
* [Настройка определения собственных, сторонних ресурсов и ресурсов CDN для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших мобильных приложений.")
* [Настройка обнаружения ресурсов первой стороны, сторонних ресурсов и CDN в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших пользовательских приложений.")