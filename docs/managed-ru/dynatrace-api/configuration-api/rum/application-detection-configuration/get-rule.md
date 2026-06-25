---
title: Applications detection rules API - GET a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-rule
scraped: 2026-05-12T11:16:04.817144
---

# Applications detection rules API - GET a rule

# Applications detection rules API - GET a rule

* Reference
* Published Aug 30, 2019

Возвращает параметры указанного правила обнаружения приложений.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного правила обнаружения приложений. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | Успех |

### Объекты тела ответа

#### Объект `ApplicationDetectionRuleConfig`

Правило обнаружения приложений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace для приложения, например `APPLICATION-4A3B43`.  Нужно использовать существующий ID. Если нужно создать правило для ещё не существующего приложения, [сначала создайте приложение](https://dt-url.net/vt03khh), а затем настройте для него правила обнаружения. |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | Условие правила обнаружения приложений. |
| id | string | ID правила. |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Метаданные для отладки. |
| name | string | Уникальное имя правила обнаружения приложений. |
| order | string | Порядок правила в списке правил.  Правила оцениваются сверху вниз. Применяется первое подходящее правило. |

#### Объект `ApplicationFilter`

Условие правила обнаружения приложений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationMatchTarget | string | Где искать значение **pattern**. Возможные значения: * `DOMAIN` * `URL` |
| applicationMatchType | string | Оператор сопоставления. Возможные значения: * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` |
| pattern | string | Значение для поиска. |

#### Объект `ConfigurationMetadataDtoImpl`

Метаданные для отладки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

### JSON-модели тела ответа

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

API-токен передаётся в заголовке **Authorization**.

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

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Проверка правил обнаружения приложений](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Легко разберитесь в правилах обнаружения вашего RUM-приложения.")
* [Определение приложений для Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определять приложения с использованием предложенного, ручного подхода или правил обнаружения приложений.")