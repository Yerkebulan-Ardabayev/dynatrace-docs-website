---
title: Custom tags API - DELETE tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/custom-tags/del-tags
---

# Custom tags API - DELETE tags

# Custom tags API - DELETE tags

* Справочник
* Опубликовано 29 мая 2020

Удаляет указанный пользовательский тег с указанных отслеживаемых сущностей.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tags` |
| DELETE | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tags` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `entities.write`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| key | string | Ключ тега, который нужно удалить.  Если **deleteAllWithKey** равен `true`, удаляются все теги с этим ключом. В противном случае удаляются только теги с точным совпадением ключа **и** значения.  Для тегов только со значением здесь нужно указывать значение. | query | Обязательный |
| value | string | Значение тега, который нужно удалить. Значение игнорируется, если **deleteAllWithKey** равен `true`.  Для тегов только со значением значение нужно указывать в параметре **key**. | query | Опциональный |
| deleteAllWithKey | boolean | * Если `true`, удаляются все теги с указанным ключом независимо от значения. * Если `false`, удаляются только теги с точным совпадением ключа **и** значения.  Если не задан, используется значение `false`. | query | Опциональный |
| entitySelector | string | Определяет сущности, у которых нужно удалить теги.  Нужно задать один из этих критериев:  * Тип сущности: `type("TYPE")` * Dynatrace ID сущности: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрошенные сущности должны быть одного типа.  Можно добавить один или несколько из следующих критериев. Значения чувствительны к регистру, и, если не указано иное, используется оператор `EQUALS`.  * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` определяются и разбираются автоматически. Любые двоеточия (`:`), входящие в ключ или значение, нужно экранировать обратным слэшем (`\`). Иначе они будут интерпретированы как разделитель между ключом и значением. Все значения тегов чувствительны к регистру. * ID management zone: `mzId(123)` * Имя management zone: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет запрос `EQUALS` без учёта регистра.   + `entityName.startsWith`: меняет оператор на `BEGINS WITH`.   + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`.   + `caseSensitive(entityName.equals("value"))`: принимает в качестве аргумента любой критерий имени сущности и делает значение чувствительным к регистру. * Состояние работоспособности (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * Метка времени первого обнаружения: `firstSeenTms.<operator>(now-3h)`. Можно использовать любой формат меток времени из параметров **from**/**to**.   Доступны следующие операторы: + `lte`: раньше указанного времени или в это время   + `lt`: раньше указанного времени   + `gte`: позже указанного времени или в это время   + `gt`: позже указанного времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Чтобы получить список доступных атрибутов, выполните запрос [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) и проверьте поле **properties** в ответе. * Связи: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Этот критерий принимает в качестве атрибута селектор сущностей. Чтобы получить список доступных связей, выполните запрос [GET entity type﻿](https://dt-url.net/2ka3ivt?dt=m) и проверьте поля **fromRelationships** и **toRelationships** в ответе. * Отрицание: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**.  Подробнее см. [Entity selector﻿](https://dt-url.net/apientityselector?dt=m) в документации Dynatrace.  Чтобы задать несколько критериев, разделяйте их запятой (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ попадают только результаты, соответствующие **всем** критериям.  Максимальная длина строки, 2000 символов. | query | Обязательный |
| from | string | Начало запрашиваемого периода времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Понятный человеку формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды указывать не обязательно. * Относительный период времени, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это один год назад с выравниванием по неделе.   Также можно указывать относительный период времени без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного периода: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задан, используется относительный период в 24 часа (`now-24h`). | query | Опциональный |
| to | string | Конец запрашиваемого периода времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Понятный человеку формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды указывать не обязательно. * Относительный период времени, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N`, это количество времени, `U`, это единица времени, а `A`, это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это один год назад с выравниванием по неделе.   Также можно указывать относительный период времени без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного периода: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задан, используется текущая метка времени. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DeletedEntityTags](#openapi-definition-DeletedEntityTags) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `DeletedEntityTags`

Удалённый пользовательский тег.

| Элемент | Тип | Описание |
| --- | --- | --- |
| matchedEntitiesCount | integer | Количество отслеживаемых сущностей, у которых тег был удалён. |

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

### Модели тела ответа JSON

```
{



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

В этом примере запрос удаляет пользовательский тег **REST-test**, созданный в примере [POST-запроса](/managed/dynatrace-api/environment-api/custom-tags/post-tags#example "Assign custom tags to monitored entities via Dynatrace API.") (`key=REST-test`). Параметр запроса **entitySelector** снова задан как `type("HOST"),tag("easyTravel")`.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X DELETE 'https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22HOST%22)%2Ctag(%22easyTrave%22)&key=REST-test' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/tags?entitySelector=type(%22HOST%22)%2Ctag(%22easyTrave%22)&key=REST-test
```

#### Тело ответа

```
{



"matchedEntitiesCount": 3



}
```

#### Код ответа

200

## Похожие темы

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")