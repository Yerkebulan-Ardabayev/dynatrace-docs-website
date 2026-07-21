---
title: Custom tags API - POST tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/custom-tags/post-tags
---

# Custom tags API - POST tags

# Custom tags API - POST tags

* Справочная информация
* Опубликовано 29 мая 2020 г.

Добавление пользовательских тегов к указанным отслеживаемым сущностям.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tags` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tags` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `entities.write`.

Как получить и использовать такой токен, описано в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| entitySelector | string | Указывает сущности, для которых нужно обновить теги.  Нужно задать один из следующих критериев:  * Тип сущности: `type("TYPE")` * ID сущности Dynatrace: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрошенные сущности должны быть одного типа.  Можно добавить один или несколько следующих критериев. Значения чувствительны к регистру, и, если не указано иное, используется оператор `EQUALS`.  * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` определяются и разбираются автоматически. Любые двоеточия (`:`), входящие в состав ключа или значения, нужно экранировать обратной косой чертой (`\`). Иначе символ будет интерпретирован как разделитель между ключом и значением. Все значения тегов чувствительны к регистру. * ID management zone: `mzId(123)` * Имя management zone: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет запрос `EQUALS`, нечувствительный к регистру.   + `entityName.startsWith`: меняет оператор на `BEGINS WITH`.   + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`.   + `caseSensitive(entityName.equals("value"))`: принимает в качестве аргумента любой критерий по имени сущности и делает значение чувствительным к регистру. * Состояние работоспособности (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * Метка времени первого обнаружения: `firstSeenTms.<operator>(now-3h)`. Можно использовать любой формат метки времени из параметров **from**/**to**.   Доступны следующие операторы: + `lte`: раньше указанного времени или в это время   + `lt`: раньше указанного времени   + `gte`: позже указанного времени или в это время   + `gt`: позже указанного времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Чтобы получить список доступных атрибутов, выполните запрос [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) и проверьте поле **properties** в ответе. * Связи: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Этот критерий принимает в качестве атрибута селектор сущности. Чтобы получить список доступных связей, выполните запрос [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) и проверьте поля **fromRelationships** и **toRelationships** в ответе. * Отрицание: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**.  Подробнее см. [Entity selector﻿](https://dt-url.net/apientityselector?dt=m) в документации Dynatrace.  Чтобы задать несколько критериев, разделите их запятой (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ попадают только результаты, соответствующие **всем** критериям.  Максимальная длина строки, 2000 символов. | query | Обязательный |
| from | string | Начало запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Читаемый формат, например `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный временной диапазон, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N`, это количество единиц времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это один год назад с выравниванием по неделе.   Также можно указать относительный временной диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный диапазон 24 часа (`now-24h`). | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Читаемый формат, например `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный временной диапазон, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N`, это количество единиц времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это один год назад с выравниванием по неделе.   Также можно указать относительный временной диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| body | [AddEntityTags](#openapi-definition-AddEntityTags) | JSON-тело запроса. Содержит теги, которые нужно добавить к соответствующим сущностям. | body | Необязательный |

### Объекты тела запроса

#### Объект `AddEntityTags`

Список тегов, которые нужно добавить к отслеживаемым сущностям.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| tags | [AddEntityTag](#openapi-definition-AddEntityTag)[] | Список тегов, которые нужно добавить к отслеживаемым сущностям. | Обязательный |

#### Объект `AddEntityTag`

Пользовательский тег, который нужно добавить к отслеживаемым сущностям.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| key | string | Ключ пользовательского тега, который нужно добавить к отслеживаемым сущностям. | Обязательный |
| value | string | Значение пользовательского тега, который нужно добавить к отслеживаемым сущностям. Может быть null | Необязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"tags": [



{



"key": "mainApp"



},



{



"key": "bookings",



"value": "42"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AddedEntityTags](#openapi-definition-AddedEntityTags) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AddedEntityTags`

Список пользовательских тегов, добавленных к отслеживаемым сущностям.

| Элемент | Тип | Описание |
| --- | --- | --- |
| appliedTags | [METag](#openapi-definition-METag)[] | Список добавленных пользовательских тегов. |
| matchedEntitiesCount | integer | Количество отслеживаемых сущностей, к которым были добавлены теги. |

#### Объект `METag`

Тег отслеживаемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник происхождения тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

```
{



"appliedTags": [



{



"context": "CONTEXTLESS",



"key": "mainApp",



"stringRepresentation": "mainApp"



},



{



"context": "CONTEXTLESS",



"key": "booking",



"stringRepresentation": "booking"



}



],



"matchedEntitiesCount": 2



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

В этом примере запрос добавляет пользовательские теги **REST-test** и **RESTexample** к хостам, у которых уже есть тег **easyTravel**. Для этого параметр запроса **entitySelector** задан как `type("HOST"),tag("easyTravel")`.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22HOST%22),tag(%22easyTravel%22)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"tags": [



{



"key": "REST-test"



},



{



"key": "RESTexample"



}



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22HOST%22),tag(%22easyTravel%22)
```

#### Request body

```
{



"tags": [



{



"key": "REST-test"



},



{



"key": "RESTexample"



}



]



}
```

#### Response body

```
{



"matchedEntitiesCount": 3,



"appliedTags": [



{



"context": "CONTEXTLESS",



"key": "REST-test",



"stringRepresentation": "REST-test"



},



{



"context": "CONTEXTLESS",



"key": "RESTexample",



"stringRepresentation": "RESTexample"



}



]



}
```

#### Response code

200

## Смежные темы

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")