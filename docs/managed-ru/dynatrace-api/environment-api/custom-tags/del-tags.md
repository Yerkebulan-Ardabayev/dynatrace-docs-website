---
title: Custom tags API - DELETE tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/custom-tags/del-tags
scraped: 2026-05-12T11:58:00.146964
---

# Custom tags API - DELETE tags

# Custom tags API - DELETE tags

* Reference
* Published May 29, 2020

Удаляет указанный пользовательский тег у указанных отслеживаемых сущностей.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/tags` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/tags` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `entities.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| key | string | Ключ удаляемого тега.  Если **deleteAllWithKey** = `true`, удаляются все теги с этим ключом. Иначе удаляются только теги с точным совпадением ключа **и** значения.  Для тегов без ключа (только значение) укажите значение здесь. | query | Required |
| value | string | Значение удаляемого тега. Значение игнорируется, если **deleteAllWithKey** = `true`.  Для тегов без ключа (только значение) указывайте значение в параметре **key**. | query | Optional |
| deleteAllWithKey | boolean | * Если `true`, удаляются все теги с указанным ключом, независимо от значения. * Если `false`, удаляются только теги с точным совпадением ключа **и** значения.  Если не задано, используется `false`. | query | Optional |
| entitySelector | string | Указывает сущности, у которых нужно удалить теги.  Должен быть задан один из критериев:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрашиваемые сущности должны быть одного типа.  Можно добавить один или несколько следующих критериев. Значения чувствительны к регистру, по умолчанию применяется оператор `EQUALS`, если не указано иное.  * Tag: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` обнаруживаются и парсятся автоматически. Двоеточия (`:`), входящие в ключ или значение, нужно экранировать обратным слэшем (`\`). Иначе они интерпретируются как разделитель между ключом и значением. Все значения тегов чувствительны к регистру. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: выполняет нечувствительный к регистру `EQUALS`-запрос.   + `entityName.startsWith`: меняет оператор на `BEGINS WITH`.   + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`.   + `caseSensitive(entityName.equals("value"))`: принимает любой критерий entity name как аргумент и делает значение чувствительным к регистру. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Используйте любой формат таймстампа из параметров **from**/**to**.   Доступны следующие операторы: + `lte`: раньше или в указанное время   + `lt`: раньше указанного времени   + `gte`: позже или в указанное время   + `gt`: позже указанного времени * Entity attribute: `<attribute>("value1","value2")` и `<attribute>.exists()`. Чтобы получить список доступных атрибутов, выполните запрос [GET entity type](https://dt-url.net/2ka3ivt) и проверьте поле **properties** в ответе. * Relationships: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Этот критерий принимает entity selector как атрибут. Чтобы получить список доступных связей, выполните запрос [GET entity type](https://dt-url.net/2ka3ivt) и проверьте поля **fromRelationships** и **toRelationships**. * Negation: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**.  Подробнее см. [Entity selector](https://dt-url.net/apientityselector) в документации Dynatrace.  Для задания нескольких критериев разделяйте их запятыми (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ включаются только результаты, соответствующие **всем** критериям.  Максимальная длина строки: 2000 символов. | query | Required |
| from | string | Начало запрашиваемого таймфрейма.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный таймфрейм 24 часа (`now-24h`). | query | Optional |
| to | string | Конец запрашиваемого таймфрейма.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущий таймстамп. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DeletedEntityTags](#openapi-definition-DeletedEntityTags) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

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
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

В этом примере запрос удаляет пользовательский тег **REST-test**, созданный в примере [POST-запроса](/managed/dynatrace-api/environment-api/custom-tags/post-tags#example "Назначение пользовательских тегов отслеживаемым сущностям через Dynatrace API.") (`key=REST-test`). Снова в query-параметре **entitySelector** задано `type("HOST"),tag("easyTravel")`.

API-токен передаётся в заголовке **Authorization**.

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

## Связанные темы

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.")