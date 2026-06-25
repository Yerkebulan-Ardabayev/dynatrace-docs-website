---
title: User sessions API - GET Table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/user-sessions/table
scraped: 2026-05-12T12:00:04.804287
---

# User sessions API - GET Table

# User sessions API - GET Table

* Reference
* Updated on May 02, 2022

Выполняет USQL-запрос и возвращает результаты в виде табличной структуры запрошенных столбцов.

В табличной структуре сущности, выбранные запросом, формируют столбцы таблицы. Каждый элемент массива **values** формирует строку таблицы.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/userSessionQueryLanguage/table` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/userSessionQueryLanguage/table` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DTAQLAccess`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| query | string | Выполняемый запрос пользовательских сессий. Подробности синтаксиса см. на [странице документации USQL](https://dt-url.net/dtusql).  Доступные столбцы таблицы **usersession** можно найти в объекте `UserSession`.  Пример запроса: `SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city`. | query | Required |
| startTimestamp | integer | Начальная метка времени запроса в миллисекундах UTC.  Если не задана или задана как `0`, используется время на 2 часа раньше текущего.  Если важны точные значения времени, задайте временной диапазон в самом запросе (параметр **query**). | query | Optional |
| endTimestamp | integer | Конечная метка времени запроса в миллисекундах UTC.  Если не задана или задана как `0`, используется текущая метка времени.  Если важны точные значения времени, задайте временной диапазон в самом запросе (параметр **query**). | query | Optional |
| offsetUTC | integer | Необязательное смещение локального времени относительно UTC в минутах. Смещение применяется к полям Date, встречающимся в запросе.  Может быть положительным или отрицательным. Например, если локальное время UTC+02:00, то timeOffset равен 120. Если UTC-05:00, то timeOffset равен -300. | query | Optional |
| pageSize | integer | Необязательное ограничение на количество фактических результатов запроса, возвращаемых в табличном результате. | query | Optional |
| pageOffset | integer | Необязательное смещение запрошенных результатов от начала табличных результатов. Связано с pageSize.  Например, для запроса, который может вернуть 500 результатов, вы можете захотеть получать результаты порциями по 50 строк.  Это можно сделать, используя pageSize=50 и задавая pageOffset в последующих вызовах.В примере добавление pageOffset=50 возвращает строки результата 51-100. | query | Optional |
| addDeepLinkFields | boolean | Добавьте (`true`), чтобы включить глубокие ссылки на дополнительные поля в запросе.  Если не задано, используется `false` | query | Optional |
| explain | boolean | Добавлять (`true`) или не добавлять (`false`) некоторую дополнительную информацию о результате в ответ.  Это помогает понять запрос и то, как был вычислен результат.  Если не задано, используется `false` | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **199** | [UserSession](#openapi-definition-UserSession) | Структура данных пользовательской сессии. Этот код ответа никогда не возвращается. |
| **200** | [UsqlResultAsTable](#openapi-definition-UsqlResultAsTable) | Успех. Ответ содержит результат запроса. |
| **400** | - | Сбой. Запрос отсутствует. |
| **404** | - | Сбой. Запрос некорректен. Подробности см. в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `UsqlResultAsTable`

Результат запроса пользовательских сессий в виде таблицы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalColumnNames | string[] | Список столбцов в таблице additionalValues.  Присутствует только если эндпоинт был вызван с параметром `deepLinkFields=true`. |
| additionalValues | array[] | Список строк данных.  Каждый элемент массива представляет строку в таблице дополнительно связанных полей.  Размер каждой строки данных и порядок элементов соответствуют содержимому **additionalColumnNames**.  Присутствует только если эндпоинт был вызван с параметром `deepLinkFields=true`. |
| columnNames | string[] | Список столбцов в результирующей таблице. |
| explanations | string[] | Дополнительная информация о запросе и результате, помогающая понять запрос и то, как был вычислен результат.  Появляется только когда параметр **explain** установлен в `true`.  Пример: Количество результатов было ограничено значением по умолчанию 50. Используйте оператор `LIMIT`, чтобы увеличить или уменьшить это ограничение. |
| extrapolationLevel | integer | Уровень экстраполяции результата.  Для повышения производительности некоторые результаты могут вычисляться по подмножеству фактических данных. Уровень экстраполяции указывает долю фактических данных в результате.  Число это знаменатель дроби, указывающий объём фактических данных. Значение `1` означает, что результат содержит только фактические данные. Значение `4` означает, что результат вычислен с использованием 1/4 фактических данных.  Если анализ должен быть основан на фактических данных, уменьшите временной диапазон запроса. Например, при уровне экстраполяции `4` попробуйте использовать 1/4 исходного временного диапазона. |
| values | array[] | Список строк данных.  Каждый элемент массива представляет строку в результирующей таблице.  Размер каждой строки данных и порядок элементов соответствуют содержимому **columnNames**. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

### JSON-модели тела ответа

```
{



"columnNames": [



"city",



"avg(duration)",



"max(duration)"



],



"extrapolationLevel": 1,



"values": [



[



"Klagenfurt",



"65996.75",



"129940"



],



[



"Linz",



"57360.86",



"222912"



],



[



"Gdansk",



"22482.2",



"351263"



]



]



}
```

## Пример

В этом примере запрос выполняет запрос `SELECT country, city, avg(duration), max(duration) FROM usersession GROUP BY country, city`.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до 4 записей.

Поскольку временной диапазон не указан, запрос использует временной диапазон по умолчанию: **2 часа** назад от текущего времени.

Результирующая таблица содержит четыре столбца: **country**, **city**, **average duration** и **maximal duration**. Массив **values** содержит строки таблицы.

Значение **extrapolationLevel** равное 4 означает, что значения экстраполированы из 1/4 фактических данных.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/userSessionQueryLanguage/table?query=select%20country,%20city,%20avg%28duration%29,%20max%28duration%29%20from%20usersession%20group%20by%20country,%20city' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890-'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/userSessionQueryLanguage/table?query=select%20country,%20city,%20avg%28duration%29,%20max%28duration%29%20from%20usersession%20group%20by%20country,%20city
```

#### Тело ответа

```
{



"extrapolationLevel": 4,



"columnNames": [



"country",



"city",



"avg(duration)",



"max(duration)"



],



"values": [



[



"Austria",



"Vienna",



64423.908602150535,



557649



],



[



"United States",



"Detroit",



60316.97509339975,



504369



],



[



"Poland",



"GdaÅsk",



24914.196428571428,



445353



],



[



"United States",



"Boston",



65826.70517928287,



434636



]



]



}
```

#### Код ответа

200

## Связанные темы

* [Пользовательские запросы, сегментация и агрегация данных сессий](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как обращаться к данным пользовательских сессий и запрашивать их с помощью ключевых слов, синтаксиса, функций и многого другого.")