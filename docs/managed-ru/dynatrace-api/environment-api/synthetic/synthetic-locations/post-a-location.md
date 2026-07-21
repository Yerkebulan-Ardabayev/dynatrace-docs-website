---
title: Synthetic locations API - POST локация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/post-a-location
scraped: 2026-05-12T11:56:55.967195
---

# Synthetic locations API - POST локация

# Synthetic locations API - POST локация

* Справочник
* Опубликовано 13 марта 2019 г.

Доступна новая версия этого API, [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Попробуйте её!

Создаёт новую **приватную** синтетическую локацию. Подробнее о создании синтетической локации смотрите [Создание приватной синтетической локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.").

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `ExternalSyntheticIntegration`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Узнайте о вариациях моделей в Synthetic locations v1 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SyntheticLocation](#openapi-definition-SyntheticLocation) | JSON-тело запроса. Содержит параметры новой приватной синтетической локации. | body | Необязательный |

### Объекты тела запроса

#### Объект `SyntheticLocation`

Конфигурация синтетической локации.

Параметры **countryCode**, **regionCode**, **city** необязательны, так как их можно получить на основе **latitude** и **longitude** локации.

Фактический набор полей зависит от типа локации. Список фактических объектов смотрите в описании поля **type** или в [Synthetic locations API v2 - JSON-модели](https://dt-url.net/3n43szj?dt=m).

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризированной локации. Авто-обновление Chromium включено (`true`) или отключено (`false`). | Необязательный |
| availabilityLocationOutage | boolean | Оповещение о недоступности локации включено (`true`) или отключено (`false`). Поддерживается только для приватных синтетических локаций. | Необязательный |
| availabilityNodeOutage | boolean | Оповещение о недоступности узла включено (`true`) или отключено (`false`). \n\n Если включено, недоступность *любого* узла в локации вызывает алерт. Поддерживается только для приватных синтетических локаций. | Необязательный |
| availabilityNotificationsEnabled | boolean | Уведомления о недоступности локации и узла включены (`true`) или отключены (`false`). Поддерживается только для приватных синтетических локаций. | Необязательный |
| browserExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли браузерные мониторы выполняться на этой локации:  * `false`: выполнение браузерных мониторов отключено. * `true`: выполнение браузерных мониторов включено. | Необязательный |
| deploymentType | string | Тип развёртывания локации:  * `STANDARD`: локация развёрнута на Windows или Linux. * `KUBERNETES`: локация развёрнута на Kubernetes. Поле может принимать значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` | Необязательный |
| fipsMode | string | Свойство контейнеризированной локации, указывающее, включён ли на этой локации режим FIPS:  * `DISABLED`: FIPS не включён на локации. * `ENABLED`: FIPS включён на локации. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS с корпоративным прокси включён на этой локации.   По умолчанию: DISABLED Поле может принимать значения: * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` | Необязательный |
| locationNodeOutageDelayInMinutes | integer | Алерт, если недоступность локации или узла длится дольше *X* минут. \n\n Применимо только если `availabilityLocationOutage` или `availabilityNodeOutage` установлено в `true`. Поддерживается только для приватных синтетических локаций. | Необязательный |
| maxActiveGateCount | integer | Свойство контейнеризированной локации. Максимальное число ActiveGate, развёрнутых для локации (требуется для Kubernetes-локации). | Необязательный |
| minActiveGateCount | integer | Свойство контейнеризированной локации. Минимальное число ActiveGate, развёрнутых для локации (требуется для Kubernetes-локации). | Необязательный |
| namExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли icmp-мониторы выполняться на этой локации:  * `false`: выполнение icmp-мониторов отключено. * `true`: выполнение icmp-мониторов включено. | Необязательный |
| nodeSize | string | Свойство контейнеризированной локации. Размер контейнеризированного узла, развёрнутого для локации (требуется для Kubernetes-локации). Допустимые значения:  * `XS`: extra small * `S`: small * `M`: medium   Размер узла `L` не поддерживается в контейнеризированных локациях. Поле может принимать значения: * `M` * `S` * `UNSUPPORTED` * `XS` | Необязательный |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить вызовом [GET all nodes](https://dt-url.net/miy3rpl?dt=m). | Необязательный |
| useNewKubernetesVersion | boolean | Свойство контейнеризированной локации. Булево значение описывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, более старая чем 1.26 * `true`: версия 1.26+. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"autoUpdateChromium": true,



"availabilityLocationOutage": true,



"availabilityNodeOutage": true,



"availabilityNotificationsEnabled": true,



"browserExecutionSupported": true,



"deploymentType": "KUBERNETES",



"fipsMode": "DISABLED",



"locationNodeOutageDelayInMinutes": 1,



"maxActiveGateCount": 1,



"minActiveGateCount": 1,



"namExecutionSupported": true,



"nodeSize": "M",



"nodes": [



"string"



],



"useNewKubernetesVersion": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EntityIdDto](#openapi-definition-EntityIdDto) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EntityIdDto`

DTO для entity ID.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | Entity ID для передачи |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"entityId": "string"



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

## Пример

В этом примере запрос создаёт новую приватную синтетическую локацию. Эта локация находится в **Linz, Austria**. Она использует синтетический узел с ID **93302281**.

API-токен передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно замените список узлов на узлы, доступные в вашем окружении.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"93302281"



]



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations
```

#### Тело запроса

```
{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["93302281"]



}
```

#### Тело ответа

```
{



"entityId": "SYNTHETIC_LOCATION-8F419D1B53639A45"



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")
* [Создание приватной синтетической локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.")