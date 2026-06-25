---
title: Third-party synthetic API - POST сторонние мониторы в Dynatrace
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic/post-third-party-monitors
scraped: 2026-05-12T11:54:34.790803
---

# Third-party synthetic API - POST сторонние мониторы в Dynatrace

# Third-party synthetic API - POST сторонние мониторы в Dynatrace

* Справочник
* Опубликовано 15 мая 2020 г.

Отправляет сторонние синтетические мониторы, локации и результаты выполнения мониторов в Dynatrace.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/ext/tests` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/ext/tests` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `ExternalSyntheticIntegration`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [3rdPartySyntheticTests](#openapi-definition-3rdPartySyntheticTests) | JSON-тело запроса. Содержит сторонние синтетические мониторы, локации и результаты. | body | Обязательный |

### Объекты тела запроса

#### Объект `3rdPartySyntheticTests`

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| locations | [3rdPartySyntheticLocation[]](#openapi-definition-3rdPartySyntheticLocation) | Список сторонних синтетических локаций. | Обязательный |
| messageTimestamp | integer | Метка времени создания сообщения, в миллисекундах UTC. | Обязательный |
| syntheticEngineIconUrl | string | URL иконки стороннего синтетического монитора. | Необязательный |
| syntheticEngineName | string | Тип стороннего синтетического монитора. | Обязательный |
| testResults | [3rdPartySyntheticTestResult[]](#openapi-definition-3rdPartySyntheticTestResult) | Список результатов выполнения стороннего синтетического монитора. | Необязательный |
| tests | [3rdPartySyntheticMonitor[]](#openapi-definition-3rdPartySyntheticMonitor) | Список сторонних синтетических мониторов. | Обязательный |

#### Объект `3rdPartySyntheticLocation`

Сторонняя синтетическая локация.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID локации. | Обязательный |
| ip | string | IP-адрес локации. | Необязательный |
| name | string | Имя локации, отображаемое в UI. | Обязательный |

#### Объект `3rdPartySyntheticTestResult`

Результаты выполнения стороннего синтетического монитора.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID стороннего синтетического монитора. | Обязательный |
| locationResults | [3rdPartySyntheticLocationTestResult[]](#openapi-definition-3rdPartySyntheticLocationTestResult) | Результаты выполнения сторонних мониторов по локациям. | Обязательный |
| totalStepCount | integer | Число шагов в мониторе. По умолчанию равно числу SyntheticTestSteps. | Необязательный |

#### Объект `3rdPartySyntheticLocationTestResult`

Результаты выполнения сторонних мониторов по локациям.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID локации. | Обязательный |
| responseTimeMillis | integer | Общее время отклика монитора из этой локации, в миллисекундах.  Если отсутствует, вычисляется как сумма времён отклика всех шагов. | Необязательный |
| startTimestamp | integer | Метка времени начала выполнения текста, в миллисекундах UTC. | Обязательный |
| stepResults | [SyntheticMonitorStepResult[]](#openapi-definition-SyntheticMonitorStepResult) | Результаты отдельных шагов монитора. | Обязательный |
| success | boolean | Был ли тест успешным (`true`) или завершился неудачей (`false`), повлияет на временной ряд доступности. | Обязательный |
| successRate | number | Общая доступность монитора из этой локации, в процентах.  Если отсутствует, вычисляется как число успешных шагов по отношению к общему числу шагов. | Необязательный |

#### Объект `SyntheticMonitorStepResult`

Результат отдельного шага синтетического монитора.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| error | [SyntheticMonitorError](#openapi-definition-SyntheticMonitorError) | Сообщение об ошибке шага синтетического монитора. | Необязательный |
| id | integer | ID шага. Уникален в пределах определения теста. | Обязательный |
| responseTimeMillis | integer | Время отклика шага, в миллисекундах.  Отсутствует, когда осмысленное время отклика недоступно (как может быть в случае определённых ошибочных состояний, например неправильно настроенного скрипта шага). | Необязательный |
| startTimestamp | integer | Метка времени выполнения шага теста, миллисекунды UTC. | Обязательный |

#### Объект `SyntheticMonitorError`

Сообщение об ошибке шага синтетического монитора.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| code | integer | Код ошибки. | Обязательный |
| message | string | Сообщение об ошибке. | Обязательный |

#### Объект `3rdPartySyntheticMonitor`

Сторонний синтетический монитор.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| deleted | boolean | Флаг удалённого монитора. По умолчанию `false`.  Если `true`, установите параметр **enabled** в `false`. | Необязательный |
| description | string | Описание монитора. | Необязательный |
| drilldownLink | string | URL к результатам выполнения монитора. | Необязательный |
| editLink | string | URL для редактирования монитора в исходном UI. | Необязательный |
| enabled | boolean | Монитор включён (`true`) или отключён (`false`). По умолчанию `true`.  Если `true`, установите параметр **deleted** в `false`. | Необязательный |
| expirationTimestamp | integer | Метка времени истечения монитора, в миллисекундах UTC. | Необязательный |
| id | string | ID монитора. | Обязательный |
| locations | [SyntheticTestLocation[]](#openapi-definition-SyntheticTestLocation) | Локации, из которых выполняется синтетический монитор. | Обязательный |
| noDataTimeout | integer | Таймаут монитора, в секундах. Если в течение этого времени не сообщается результат, состояние доступности переключается на unmonitored. По умолчанию, удвоенная частота монитора. | Необязательный |
| scheduleIntervalInSeconds | integer | Частота монитора, в секундах. Монитор повторяется с указанным интервалом в стороннем источнике.  Dynatrace ожидает результаты выполнения монитора с указанным интервалом. Если вы сообщаете результаты в Dynatrace реже, соответственно скорректируйте значение **noDataTimeout**. | Обязательный |
| steps | [SyntheticTestStep[]](#openapi-definition-SyntheticTestStep) | Шаги стороннего монитора. | Необязательный |
| testSetup | string | Информация о настройке монитора, например `browser`. | Необязательный |
| title | string | Имя монитора. | Обязательный |

#### Объект `SyntheticTestLocation`

Локация синтетического теста.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Локация включена/отключена. По умолчанию `true`, включая локацию. | Необязательный |
| id | string | ID локации. | Обязательный |

#### Объект `SyntheticTestStep`

Шаг синтетического монитора.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | integer | ID шага. | Обязательный |
| title | string | Имя шага, отображаемое в UI. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"locations": [



{



"id": "string",



"ip": "string",



"name": "string"



}



],



"messageTimestamp": 1,



"syntheticEngineIconUrl": "string",



"syntheticEngineName": "string",



"testResults": [



{



"id": "string",



"locationResults": [



{



"id": "string",



"responseTimeMillis": 1,



"startTimestamp": 1,



"stepResults": [



{



"error": {



"code": 1,



"message": "string"



},



"id": 1,



"responseTimeMillis": 1,



"startTimestamp": 1



}



],



"success": true,



"successRate": 1



}



],



"totalStepCount": 1



}



],



"tests": [



{



"deleted": true,



"description": "string",



"drilldownLink": "string",



"editLink": "string",



"enabled": true,



"expirationTimestamp": 1,



"id": "string",



"locations": [



{



"enabled": true,



"id": "string"



}



],



"noDataTimeout": 1,



"scheduleIntervalInSeconds": 1,



"steps": [



{



"id": 1,



"title": "string"



}



],



"testSetup": "string",



"title": "string"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Информация принята и сохранена. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не удалось. Входные данные недействительны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

В этом примере запрос отправляет следующие данные из стороннего синтетического движка **My third-party synthetic** в Dynatrace:

* Три локации: **Linz1**, **Linz2** и **Linz3**.
* Два монитора: **example of synthetic monitor - 1** и **example of synthetic monitor - 2**, каждый содержит три шага и выполняется из двух локаций.
* Один результат на шаг, на локацию, для каждого монитора.

Мониторы имеют следующие параметры:

|  | example of synthetic monitor - 1 | example of synthetic monitor - 2 |
| --- | --- | --- |
| Частота | 300 секунд (5 минут) | 300 секунд (5 минут) |
| Локации | Linz1 Linz2 | Linz2 Linz3 |
| Шаги | Step1-1 Step1-2 Step1-3 | Step2-1 Step2-2 Step3-3 |

Монитор **example of synthetic monitor - 1** имеет следующие времена отклика в миллисекундах:

|  | Linz1 | Linz2 |
| --- | --- | --- |
| Step1-1 | 7790 | 2075 |
| Step1-2 | 2073 | 4079 |
| Step1-3 | 8650 | 3937 |

Монитор **example of synthetic monitor - 2** имеет следующие времена отклика в миллисекундах:

|  | Linz2 | Linz3 |
| --- | --- | --- |
| Step2-1 | 2200 | 9123 |
| Step2-2 | 6903 | 9722 |
| Step2-3 | 4821 | 1717 |

API-токен передаётся в заголовке **Authorization**.

Поскольку тело запроса объёмное, в этом примере оно усечено в секции **Curl**. Полное тело смотрите в секции **Request body**. Можно скачать JSON тела запроса, чтобы выполнить пример запроса в вашем окружении. Обязательно замените метки времени на недавние, иначе результаты будут слишком старыми.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/tests \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section >}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/ext/tests
```

#### Тело запроса

```
{



"syntheticEngineName": "My third-party synthetic",



"syntheticEngineIconUrl": "https://static.thenounproject.com/png/1745-200.png",



"messageTimestamp": 1543572265528,



"locations": [



{



"id": "Linz1",



"ip": "127.0.0.1",



"name": "Linz1"



},



{



"id": "Linz2",



"ip": "127.0.0.2",



"name": "Linz2"



},



{



"id": "Linz3",



"ip": "127.0.0.3",



"name": "Linz3"



}



],



"tests": [



{



"id": "3rdPartySyntheticMonitor1",



"title": "example of synthetic monitor - 1",



"scheduleIntervalInSeconds": 300,



"locations": [



{



"id": "Linz1"



},



{



"id": "Linz2"



}



],



"steps": [



{



"id": 1,



"title": "Step1-1"



},



{



"id": 2,



"title": "Step1-2"



},



{



"id": 3,



"title": "Step1-3"



}



]



},



{



"id": "3rdPartySyntheticMonitor2",



"title": "example of synthetic monitor - 2",



"scheduleIntervalInSeconds": 300,



"locations": [



{



"id": "Linz2"



},



{



"id": "Linz3"



}



],



"steps": [



{



"id": 1,



"title": "Step2-1"



},



{



"id": 2,



"title": "Step2-2"



},



{



"id": 3,



"title": "Step2-3"



}



]



}



],



"testResults": [



{



"id": "3rdPartySyntheticMonitor1",



"totalStepCount": 3,



"locationResults": [



{



"id": "Linz1",



"startTimestamp": 1543572262538,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262538,



"responseTimeMillis": 7790



},



{



"id": 2,



"startTimestamp": 1543572262538,



"responseTimeMillis": 2073



},



{



"id": 3,



"startTimestamp": 1543572262538,



"responseTimeMillis": 8650



}



]



},



{



"id": "Linz2",



"startTimestamp": 1543572262548,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262548,



"responseTimeMillis": 2075



},



{



"id": 2,



"startTimestamp": 1543572262548,



"responseTimeMillis": 4079



},



{



"id": 3,



"startTimestamp": 1543572262548,



"responseTimeMillis": 3937



}



]



}



]



},



{



"id": "3rdPartySyntheticMonitor2",



"totalStepCount": 3,



"locationResults": [



{



"id": "Linz2",



"startTimestamp": 1543572262548,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262548,



"responseTimeMillis": 2200



},



{



"id": 2,



"startTimestamp": 1543572262548,



"responseTimeMillis": 6903



},



{



"id": 3,



"startTimestamp": 1543572262548,



"responseTimeMillis": 4821



}



]



},



{



"id": "Linz3",



"startTimestamp": 1543572262558,



"success": true,



"stepResults": [



{



"id": 1,



"startTimestamp": 1543572262558,



"responseTimeMillis": 9123



},



{



"id": 2,



"startTimestamp": 1543572262558,



"responseTimeMillis": 9722



},



{



"id": 3,



"startTimestamp": 1543572262558,



"responseTimeMillis": 1717



}



]



}



]



}



]



}
```

#### Код ответа

204

#### Результат

Выделение показывает параметры, переданные в запросе.

![Внешние синтетические мониторы](https://dt-cdn.net/images/ext-monitors-1340-4aaf90d700.png)

Внешние синтетические мониторы

![Детали внешнего синтетического монитора](https://dt-cdn.net/images/ext-monitor-details-1850-2d6cb27a83.png)

Детали внешнего синтетического монитора