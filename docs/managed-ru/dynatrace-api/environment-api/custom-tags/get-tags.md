---
title: Custom tags API - GET tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/custom-tags/get-tags
---

# Custom tags API - GET tags

# Custom tags API - GET tags

* Справка
* Опубликовано 29 мая 2020 г.

Выводит список всех пользовательских тегов, назначенных указанным отслеживаемым сущностям. Автоматически применяемые теги и импортированные теги не включаются.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tags` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tags` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `entities.read`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| entitySelector | string | Задаёт сущности, теги которых нужно прочитать.  Нужно задать один из следующих критериев:  * Тип сущности: `type("TYPE")` * Dynatrace ID сущности: `entityId("id")`. Можно указать несколько ID, разделённых запятой (`entityId("id-1","id-2")`). Все запрашиваемые сущности должны быть одного типа.  Можно добавить один или несколько из следующих критериев. Значения чувствительны к регистру, используется оператор `EQUALS`, если не указано иное.  * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` определяются и разбираются автоматически. Любые двоеточия (`:`), являющиеся частью ключа или значения, нужно экранировать обратной косой чертой (`\`). Иначе они будут интерпретированы как разделитель между ключом и значением. Все значения тегов чувствительны к регистру. * ID management zone: `mzId(123)` * Имя management zone: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет запрос `EQUALS`, нечувствительный к регистру.   + `entityName.startsWith`: меняет оператор на `BEGINS WITH`.   + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`.   + `caseSensitive(entityName.equals("value"))`: принимает в качестве аргумента любой критерий имени сущности и делает значение чувствительным к регистру. * Состояние работоспособности (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * Метка времени первого обнаружения: `firstSeenTms.<operator>(now-3h)`. Можно использовать любой формат метки времени из параметров **from**/**to**.   Доступны следующие операторы: + `lte`: раньше указанного времени или в это время   + `lt`: раньше указанного времени   + `gte`: позже указанного времени или в это время   + `gt`: позже указанного времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Чтобы получить список доступных атрибутов, выполните запрос [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) и проверьте поле **properties** в ответе. * Отношения: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Этот критерий принимает в качестве атрибута селектор сущности. Чтобы получить список доступных отношений, выполните запрос [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) и проверьте поля **fromRelationships** и **toRelationships** в ответе. * Отрицание: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**.  Подробнее см. [Entity selector﻿](https://dt-url.net/apientityselector?dt=m) в документации Dynatrace.  Чтобы задать несколько критериев, разделите их запятой (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ включаются только результаты, соответствующие **всем** критериям.  Максимальная длина строки составляет 2000 символов. | query | Обязательный |
| from | string | Начало запрашиваемого периода времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Понятный человеку формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный период времени, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе.   Также можно указать относительный период времени без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного периода: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный период в 24 часа (`now-24h`). | query | Необязательный |
| to | string | Конец запрашиваемого периода времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Понятный человеку формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный период времени, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе.   Также можно указать относительный период времени без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного периода: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CustomEntityTags](#openapi-definition-CustomEntityTags) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CustomEntityTags`

Список пользовательских тегов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| tags | [METag](#openapi-definition-METag)[] | Список пользовательских тегов. |
| totalCount | integer | Общее количество тегов в ответе. |

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
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

```
{



"tags": [



{



"context": "CONTEXTLESS",



"key": "mainApp",



"stringRepresentation": "mainApp"



},



{



"context": "CONTEXTLESS",



"key": "bookings",



"stringRepresentation": "bookings"



}



],



"totalCount": 2



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

В этом примере запрос выводит список пользовательских тегов, применённых к сервисам, принадлежащим management zone с ID **229130632296508575249**. Для этого параметр запроса **entitySelector** задан как `type("SERVICE"),mzId("9130632296508575249")`.

Токен API передаётся в заголовке **Authorization**.

Поскольку полный результат довольно объёмный, он сокращён до трёх записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22SERVICE%22),mzId(%229130632296508575249%22)
```

#### Тело ответа

```
{



"totalCount": 31,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Billing",



"stringRepresentation": "Billing"



},



{



"context": "CONTEXTLESS",



"key": "Booking",



"stringRepresentation": "Booking"



},



{



"context": "CONTEXTLESS",



"key": "easytravel",



"value": "backend",



"stringRepresentation": "easytravel:backend"



}



]



}
```

#### Код ответа

200

## Похожие темы

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте больше об Dynatrace Monitored entities API.")