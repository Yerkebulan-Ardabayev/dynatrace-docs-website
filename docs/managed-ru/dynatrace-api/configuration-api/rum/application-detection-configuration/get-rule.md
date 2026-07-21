---
title: Applications detection rules API - GET a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-rule
---

# Applications detection rules API - GET a rule

# Applications detection rules API - GET a rule

* Справка
* Опубликовано 30 авг. 2019 г.

Получает параметры указанного правила обнаружения приложения.

Запрос выдаёт полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного правила обнаружения приложения. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | Успех |

### Объекты тела ответа

#### Объект `ApplicationDetectionRuleConfig`

Правило обнаружения приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace приложения, например `APPLICATION-4A3B43`.  Нужно использовать существующий ID. Если нужно создать правило для приложения, которое ещё не существует, сначала [создай приложение﻿](https://dt-url.net/vt03khh?dt=m), а затем настрой для него правила обнаружения. |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | Условие правила обнаружения приложения. |
| id | string | ID правила. |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Метаданные, полезные для отладки. |
| name | string | Уникальное имя правила обнаружения приложения. |
| order | string | Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое совпавшее правило. |

#### Объект `ApplicationFilter`

Условие правила обнаружения приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationMatchTarget | string | Где искать значение **pattern**. Элемент может содержать эти значения * `DOMAIN` * `URL` |
| applicationMatchType | string | Оператор сопоставления. Элемент может содержать эти значения * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` |
| pattern | string | Значение для поиска. |

#### Объект `ConfigurationMetadataDtoImpl`

Метаданные, полезные для отладки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

### Модели JSON тела ответа

```
{



"applicationIdentifier": "APPLICATION-123456",



"filterConfig": {



"applicationMatchTarget": "DOMAIN",



"applicationMatchType": "EQUALS",



"pattern": "myapp.example.com"



},



"id": "12345678-abcd-1234-abcd-1234567890ab",



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"name": "uniqueName"



}
```

## Пример

В этом примере запрос получает свойства правила **easyTravel** с ID **95b22afb-4e3d-4f9f-a37d-81bc3d388a33**.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/95b22afb-4e3d-4f9f-a37d-81bc3d388a33 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/95b22afb-4e3d-4f9f-a37d-81bc3d388a33
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.188.0.20200203-155649"



},



"id": "95b22afb-4e3d-4f9f-a37d-81bc3d388a33",



"applicationIdentifier": "APPLICATION-900C1E36674F607D",



"filterConfig": {



"pattern": "easyTravel",



"applicationMatchType": "EQUALS",



"applicationMatchTarget": "DOMAIN"



}



}
```

#### Код ответа

200

## Похожие темы

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Узнай о Real User Monitoring Classic, ключевых показателях производительности, мониторинге мобильных приложений и многом другом.")
* [Проверка правил обнаружения приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/application-detection-rules "Легко разберись в правилах обнаружения твоего RUM-приложения.")
* [Определение приложений для Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнай, как определить свои приложения, следуя предложенному, ручному подходу или подходу с правилами обнаружения приложений.")