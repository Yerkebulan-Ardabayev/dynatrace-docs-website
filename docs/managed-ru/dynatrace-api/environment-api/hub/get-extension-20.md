---
title: Hub capabilities API - GET расширения 2.0
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-extension-20
scraped: 2026-05-12T11:54:45.089517
---

# Hub capabilities API - GET расширения 2.0

# Hub capabilities API - GET расширения 2.0

* Reference
* Published Feb 07, 2023

Возвращает подробности о расширении 2.0.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `hub.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| extensionName | string | Полное имя (FQN) расширения | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ItemDetails](#openapi-definition-ItemDetails) | OK |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Некорректный запрос |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Недоступно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ItemDetails`

Публичные метаданные элемента.

| Элемент | Тип | Описание |
| --- | --- | --- |
| authorLogo | string | URL логотипа автора. |
| authorName | string | Имя автора элемента. |
| clusterCompatible | boolean | Проверяет, совместим ли элемент с версией кластера. |
| clusterMaxVersion | integer | Максимальная поддерживаемая версия кластера для этого элемента. |
| clusterMinVersion | integer | Минимальная версия кластера, необходимая для использования этого элемента. |
| description | string | Описание элемента. |
| descriptionBlocks | [DescriptionBlock[]](#openapi-definition-DescriptionBlock) | - |
| documentationLink | string | Абсолютная ссылка на страницу документации, описывающую элемент. |
| extension1Details | [Extension1Details](#openapi-definition-Extension1Details) | Дополнительные подробности расширения версии 1. |
| extension2Details | [Extension2Details](#openapi-definition-Extension2Details) | Дополнительные подробности расширения. |
| itemId | string | Уникальный ID элемента. |
| logo | string | Логотип элемента. Может быть URL или Base64-кодировкой. Предназначен для html-тегов. |
| marketingLink | string | Абсолютная ссылка на маркетинговую страницу, рассказывающую о применении элемента с Dynatrace. |
| name | string | Имя элемента. |
| notCompatibleReason | string | Причина, по которой элемент несовместим с версией кластера. |
| relatedItems | [RelatedItem[]](#openapi-definition-RelatedItem) | Связанные элементы. |
| tags | string[] | Группировка элементов по ключевым словам. |
| technologyDetails | [TechnologyDetails](#openapi-definition-TechnologyDetails) | Дополнительные подробности технологии. |
| type | string | Представляет тип элемента. Может быть TECHNOLOGY, EXTENSION1 или EXTENSION2. Элемент может принимать значения * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` |

#### Объект `DescriptionBlock`

Представляет секцию данных, описывающую заданный capability.

| Элемент | Тип | Описание |
| --- | --- | --- |
| images | [Image[]](#openapi-definition-Image) | Коллекция изображений (в случае галереи). |
| source | string | Источник блока описания (в случае markdown). |
| sourceId | string | Опциональный идентификатор специальных блоков описания. |
| title | string | Заголовок блока описания. |
| type | string | Тип данных: markdown или gallery. Элемент может принимать значения * `GALLERY` * `MARKDOWN` |

#### Объект `Image`

Информация о деталях изображения capability.

| Элемент | Тип | Описание |
| --- | --- | --- |
| alt | string | Альтернативный текст для изображения. |
| src | string | URL изображения. |
| title | string | Заголовок изображения. |

#### Объект `Extension1Details`

Дополнительные подробности расширения версии 1.

| Элемент | Тип | Описание |
| --- | --- | --- |
| releases | [Extension1Release[]](#openapi-definition-Extension1Release) | Список версий расширения версии 1. |

#### Объект `Extension1Release`

Подробности релиза расширения версии 1.

| Элемент | Тип | Описание |
| --- | --- | --- |
| artifactSha256 | string | SHA-256-хеш расширения версии 1. |
| artifactTitle | string | Заголовок расширения версии 1. |
| releaseNotes | string | Связанные release notes. |
| version | string | Номер версии релиза расширения версии 1. |

#### Объект `Extension2Details`

Дополнительные подробности расширения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| distributed | boolean | Доступно ли это расширение в центральном каталоге hub. |
| extensionName | string | Полное имя (FQN) расширения. |
| recommendedCatalogVersion | string | Рекомендованная версия этого расширения для использования. Это последний совместимый опубликованный релиз. |
| releases | [ExtensionRelease[]](#openapi-definition-ExtensionRelease) | Релизы расширения. |

#### Объект `ExtensionRelease`

Информация о релизах расширений

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Представляет, является ли эта версия активной |
| artifactSha256 | string | SHA-256-хеш распространяемого расширения. |
| assetsInfo | [AssetInfo[]](#openapi-definition-AssetInfo) | Типы ресурсов и их количество |
| configuredFeatureSets | string[] | Настроенные feature-set'ы для установленного релиза |
| dataSources | string[] | Доступные источники данных для заданного релиза |
| distributed | boolean | Представляет, распространяется ли релиз |
| featureSets | object | Feature-set'ы, содержащиеся в заданном релизе |
| minClusterVersion | integer | Минимальная версия кластера для релиза |
| registered | boolean | Представляет, зарегистрировано ли расширение |
| releaseNotes | string | Release notes расширения. |
| unpublished | boolean | Представляет, снято ли расширение с публикации. |
| unpublishedDescription | string | Описание причины снятия расширения с публикации. |
| unpublishedSeverity | integer | Серьёзность статуса unpublished. 5 указывает на error state |
| version | string | Номер версии расширения. |

#### Объект `AssetInfo`

Типы ресурсов и их количество

| Элемент | Тип | Описание |
| --- | --- | --- |
| assetType | string | - |
| count | integer | - |

#### Объект `FeatureSetDetails`

Дополнительная информация о feature-set

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Опциональное описание feature-set |
| displayName | string | Опциональное отображаемое имя feature-set |
| isRecommended | boolean | Помечает feature-set как рекомендованный (выбранный по умолчанию при активации) |
| metrics | [MetricDto[]](#openapi-definition-MetricDto) | Метрики feature-set |

#### Объект `MetricDto`

Метрика, собираемая расширением

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ метрики |
| metadata | [MetricMetadataDto](#openapi-definition-MetricMetadataDto) | Метаданные метрики |

#### Объект `MetricMetadataDto`

Метаданные метрики

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание метрики |
| displayName | string | Имя метрики в пользовательском интерфейсе |
| unit | string | Единица измерения метрики |

#### Объект `RelatedItem`

Связанные элементы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | - |
| externalLink | string | Внешняя ссылка (marketing/documentation), которая может предоставить дополнительную информацию. |
| hasClusterLink | boolean | Указывает, есть ли страница внутри продукта для активации этого элемента. |
| iconUrl | string | Логотип элемента. Может быть URL или Base64-кодировкой. Предназначен для html-тегов |
| id | string | - |
| name | string | - |
| type | string | Представляет тип элемента. Может быть TECHNOLOGY, EXTENSION1 или EXTENSION2. Элемент может принимать значения * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` |

#### Объект `TechnologyDetails`

Дополнительные подробности технологии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activationLink | string | Представляет ссылку установки / публичной навигации для технологии. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"authorLogo": "string",



"authorName": "string",



"clusterCompatible": true,



"clusterMaxVersion": 1,



"clusterMinVersion": 1,



"description": "string",



"descriptionBlocks": [



{



"images": [



{



"alt": "string",



"src": "string",



"title": "string"



}



],



"source": "string",



"sourceId": "string",



"title": "string",



"type": "GALLERY"



}



],



"documentationLink": "string",



"extension1Details": {



"releases": [



{



"artifactSha256": "string",



"artifactTitle": "string",



"releaseNotes": "string",



"version": "string"



}



]



},



"extension2Details": {



"distributed": true,



"extensionName": "string",



"recommendedCatalogVersion": "string",



"releases": [



{



"active": true,



"artifactSha256": "string",



"assetsInfo": [



{



"assetType": "string",



"count": 1



}



],



"configuredFeatureSets": [



"string"



],



"dataSources": [



"string"



],



"distributed": true,



"featureSets": {},



"minClusterVersion": 1,



"registered": true,



"releaseNotes": "string",



"unpublished": true,



"unpublishedDescription": "string",



"unpublishedSeverity": 1,



"version": "string"



}



]



},



"itemId": "string",



"logo": "string",



"marketingLink": "string",



"name": "string",



"notCompatibleReason": "string",



"relatedItems": [



{



"description": "string",



"externalLink": "string",



"hasClusterLink": true,



"iconUrl": "string",



"id": "string",



"name": "string",



"type": "EXTENSION1"



}



],



"tags": [



"string"



],



"technologyDetails": {



"activationLink": "string"



},



"type": "EXTENSION1"



}
```

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