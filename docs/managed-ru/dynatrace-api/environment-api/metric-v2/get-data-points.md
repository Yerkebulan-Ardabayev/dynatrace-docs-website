---
title: Metrics API - GET точки данных метрики
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/get-data-points
scraped: 2026-05-12T11:10:16.165358
---

# Metrics API - GET точки данных метрики

# Metrics API - GET точки данных метрики

* Справочник
* Опубликовано 14 июня 2019 г.

Возвращает точки данных указанных метрик.

Можно получить либо одну агрегированную точку данных на кортеж (уникальные сочетания «метрика-измерение-значение измерения»), либо список точек данных на кортеж. Подробнее смотрите в описании параметра запроса **resolution**.

Действуют следующие ограничения:

* Количество точек данных ограничено 20 000 000.
* Количество кортежей ограничено 100 000.  
  При превышении обрабатываются только первые 100 000 кортежей (трансформация `:sort` на это не влияет), а остальные игнорируются.
* Количество точек данных на кортеж ограничено 10 080.
* Количество отслеживаемых сущностей ограничено 5 000 на каждый [**entitySelector**](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте entity selector для endpoint-ов Environment API.") в запросе.

Эти ограничения применяются к точкам данных, которые запрос читает в базе данных. Количество точек данных в итоговом результате может отличаться. Например, если используется трансформация `:fold`, запрос читает несколько точек данных, но возвращает лишь одну агрегированную точку данных на кортеж.

В зависимости от значения заголовка запроса **Accept** запрос возвращает один из следующих типов payload:

* `application/json`
* `text/csv; header=present`, CSV-таблица со строкой заголовка
* `text/csv; header=absent`, CSV-таблица без строки заголовка

Если заголовок **Accept** в запросе не указан, возвращается payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/query` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/query` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| metricSelector | string | Выбирает метрики для запроса по их ключам. За один запрос можно выбрать до 10 метрик.  Можно указать несколько ключей метрик через запятую (например, `metrickey1,metrickey2`). Чтобы выбрать несколько метрик с общим родителем, перечислите последнюю часть нужных ключей метрик в скобках через запятую, сохранив общую часть без изменений. Например, чтобы получить метрики `builtin:host.cpu.idle` и `builtin:host.cpu.user`, напишите: `builtin:host.cpu.(idle,user)`.  Если ключ метрики содержит символы, которые нужно экранировать, ключ необходимо взять в кавычки (`"`). Следующие символы внутри ключа метрики в кавычках должны быть экранированы тильдой (`~`):  * Кавычки (`"`) * Тильды (`~`)  Например, чтобы запросить метрику с ключом **ext:selfmonitoring.jmx.Agents: Type "APACHE"**, нужно указать такой селектор:  `"ext:selfmonitoring.jmx.Agents: Type ~"APACHE~""`  Можно задать дополнительные операторы трансформации, разделяя их двоеточием (`:`). Дополнительную информацию о доступных трансформациях результата и синтаксисе смотрите в [Metrics selector transformations](https://dt-url.net/metricSelector) в документации Dynatrace. | query | Необязательный |
| resolution | string | Желаемое разрешение точек данных.  Можно использовать один из следующих вариантов:  * Желаемое количество точек данных. Это вариант по умолчанию. Это ориентировочное число точек, которое не обязательно равно числу возвращённых точек данных. * Желаемый временной промежуток между точками данных. Это ориентировочный промежуток, который не обязательно равен возвращённому промежутку. Чтобы использовать этот вариант, укажите единицу промежутка.  Допустимые единицы промежутка:  * `m`: минуты * `h`: часы * `d`: дни * `w`: недели * `M`: месяцы * `q`: кварталы * `y`: годы  Если не задано, по умолчанию используется **120 точек данных**.  Например:  * Получить точки данных с интервалом 10 минут: `resolution=10m` * Получить точки данных с интервалом 3 недели: `resolution=3w`  Также для одного запроса можно указать **несколько разрешений** с помощью форматирования на основе индекса. Это позволяет каждому выражению метрики в селекторе с несколькими выражениями иметь своё разрешение.  Используйте формат: `<index>:<resolution>(,<index>:<resolution>)*` Где:  * `index`, позиция выражения метрики в списке `metricSelector`, отсчёт от нуля. * `resolution`, либо количество точек данных (например, `120`), либо промежуток с единицей (например, `10m`, `3w`).  Если разрешение для данного индекса не указано, применяется значение по умолчанию **120 точек данных**.  **Примеры:**  * `resolution=0:Inf`: первая метрика использует разрешение `Inf`, вторая метрика использует значение по умолчанию (120 точек данных). * `resolution=0:Inf,1:10`: первая метрика использует `Inf`, вторая метрика использует `10` точек данных. * `resolution=Inf`: все метрики используют разрешение `Inf`.   **Примечание:** если используется несколько разрешений, поле resolution в ответе содержит наименьшее разрешение. | query | Необязательный |
| from | string | Начало запрашиваемого временного интервала.  Можно использовать один из форматов:  * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задан, используется относительный интервал в два часа (`now-2h`). | query | Необязательный |
| to | string | Конец запрашиваемого временного интервала.  Можно использовать один из форматов:  * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задан, используется текущая метка времени. | query | Необязательный |
| entitySelector | string | Задаёт область запроса по сущностям. В ответ попадают только точки данных, доставленные подходящими сущностями.  Необходимо указать один из критериев:  * Тип сущности: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. Можно указать несколько ID через запятую (`entityId("id-1","id-2")`). Все запрашиваемые сущности должны быть одного типа.  Дополнительно можно добавить один или несколько следующих критериев. Значения регистрозависимы, оператор по умолчанию `EQUALS`, если не указано иное.  * Тег: `tag("value")`. Теги в форматах `[context]key:value`, `key:value` и `value` распознаются и разбираются автоматически. Двоеточия (`:`), входящие в состав ключа или значения, должны быть экранированы обратной косой (`\`). Иначе они будут восприняты как разделитель между ключом и значением. Все значения тегов регистрозависимы. * ID зоны управления: `mzId(123)` * Имя зоны управления: `mzName("value")` * Имя сущности: + `entityName.equals`: выполняет регистронезависимый запрос `EQUALS`.   + `entityName.startsWith`: меняет оператор на `BEGINS WITH`.   + `entityName.in`: позволяет указать несколько значений. Применяется оператор `EQUALS`.   + `caseSensitive(entityName.equals("value"))`: принимает любой критерий по имени сущности и делает сравнение регистрозависимым. * Состояние работоспособности (HEALTHY, UNHEALTHY): `healthState("HEALTHY")` * Метка времени первого обнаружения: `firstSeenTms.<operator>(now-3h)`. Используется любой формат timestamp из параметров **from**/**to**.   Доступные операторы: + `lte`: раньше указанного времени или в это же время   + `lt`: раньше указанного времени   + `gte`: позже указанного времени или в это же время   + `gt`: позже указанного времени * Атрибут сущности: `<attribute>("value1","value2")` и `<attribute>.exists()`. Чтобы получить список доступных атрибутов, выполните запрос [GET entity type](https://dt-url.net/2ka3ivt) и посмотрите поле **properties** в ответе. * Связи: `fromRelationships.<relationshipName>()` и `toRelationships.<relationshipName>()`. Этот критерий принимает в качестве аргумента селектор сущностей. Чтобы получить список доступных связей, выполните запрос [GET entity type](https://dt-url.net/2ka3ivt) и посмотрите поля **fromRelationships** и **toRelationships**. * Инверсия: `not(<criterion>)`. Инвертирует любой критерий, кроме **type**.  Подробнее смотрите [Entity selector](https://dt-url.net/apientityselector) в документации Dynatrace.  Чтобы указать несколько критериев, перечислите их через запятую (`,`). Например, `type("HOST"),healthState("HEALTHY")`. В ответ попадут только результаты, соответствующие **всем** критериям.  Максимальная длина строки: 2 000 символов.  Используйте вызов [`GET /metrics/{metricId}`](https://dt-url.net/6z23ifk), чтобы получить список возможных типов сущностей для вашей метрики.  Чтобы задать универсальную область, соответствующую всем сущностям, опустите этот параметр. | query | Необязательный |
| mzSelector | string | Область запроса по зонам управления. В ответ включаются только данные метрик, относящиеся к указанным зонам управления.  Можно задать один или несколько из следующих критериев. Значения регистрозависимы, используется оператор `EQUALS`. Если указано несколько значений, применяется логика **OR**.  * `mzId(123,456)` * `mzName("name-1","name-2")`   Чтобы задать несколько критериев, разделяйте их запятой (`,`). Например, `mzName("name-1","name-2"),mzId(1234)`. В ответ включаются только результаты, соответствующие **всем** критериям. Например, чтобы получить метрики с id **123** ИЛИ **234** И именем **name-1** ИЛИ **name-2**, используйте такой **mzSelector**: `mzId(123,234),mzName("name-1","name-2"). | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MetricData](#openapi-definition-MetricData) | Успех |
| **400** | - | Синтаксическая ошибка или ошибка валидации. Параметры from и to, entitySelector или resolution некорректны по отдельности или в их совокупном смысле. |
| **404** | - | Метрика не найдена. |
| **406** | - | Not acceptable. Запрошенный тип медиа не поддерживается. Проверьте заголовок **Accept** в запросе. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MetricData`

Список метрик и их точек данных.

| Поле | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Устарело. Это поле возвращается из соображений совместимости. Всегда имеет значение `null`. |
| resolution | string | Разрешение таймслотов в результате. |
| result | [MetricSeriesCollection[]](#openapi-definition-MetricSeriesCollection) | Список метрик и их точек данных. |
| totalCount | integer | Общее количество первичных сущностей в результате.  Имеет значение `0`, если ни одна из запрошенных метрик не подходит для пагинации. |
| warnings | string[] | Список предупреждений |

#### Объект `MetricSeriesCollection`

Точки данных метрики.

| Поле | Тип | Описание |
| --- | --- | --- |
| appliedOptionalFilters | [AppliedFilter[]](#openapi-definition-AppliedFilter) | Список отфильтрованных ключей метрик вместе с фильтрами, которые были применены к этим ключам, из параметра `optionalFilter`. |
| data | [MetricSeries[]](#openapi-definition-MetricSeries) | Точки данных метрики. |
| dataPointCountRatio | number | Отношение запрошенных точек данных к максимальному числу точек данных на метрику, допустимому в одном запросе. |
| dimensionCountRatio | number | Отношение запрошенных кортежей измерений к максимальному числу кортежей измерений, допустимому в одном запросе. |
| dql | [MetricQueryDQLTranslation](#openapi-definition-MetricQueryDQLTranslation) | Перевод запроса метрики в DQL. |
| metricId | string | Ключ метрики.  Если применена какая-либо трансформация, она включена сюда. |
| warnings | string[] | Список потенциальных предупреждений, влияющих на этот ID. Например, использование устаревшей функциональности и т. п. |

#### Объект `AppliedFilter`

Необязательные фильтры, которые вступили в силу.

| Поле | Тип | Описание |
| --- | --- | --- |
| appliedTo | string[] | Ключи всех метрик, к которым был применён этот фильтр.  Может содержать несколько метрик для сложных выражений и всегда содержит как минимум один ключ. |
| filter | [Filter](#openapi-definition-Filter) | Фильтр по измерению или по серии для метрики. |

#### Объект `Filter`

Фильтр по измерению или по серии для метрики.

| Поле | Тип | Описание |
| --- | --- | --- |
| operands | [Filter[]](#openapi-definition-Filter) | Если тип `not`, `and` или `or`, содержит вложенные фильтры. |
| referenceInvocation | [Invocation](#openapi-definition-Invocation) | Вызов функции, например функции `entitySelector`. |
| referenceString | string | Для фильтров, сравнивающих измерение со значением, таких как `eq` или `ne`, содержит значение, с которым сравнивается измерение. |
| referenceValue | number | Для операндов фильтров `series`, сравнивающих с числом, содержит число для сравнения. |
| rollup | [Rollup](#openapi-definition-Rollup) | Способ представления серии как одного значения для целей сортировки или фильтров на основе серий. |
| targetDimension | string | Если тип применяется к измерению, содержит целевое измерение. |
| targetDimensions | string[] | Если тип применяется к n измерениям, содержит целевые измерения. В настоящее время используется только для фильтра `remainder`. |
| type | string | Тип этого фильтра, определяет, какие другие поля присутствуют. Может быть любым из:  * `eq`, * `ne`, * `prefix`, * `in`, * `remainder`, * `suffix`, * `contains`, * `existsKey`, * `series`, * `or`, * `and`, * `not`, * `ge`, * `gt`, * `le`, * `lt`, * `otherwise`. Поле может принимать значения: * `and` * `contains` * `eq` * `existsKey` * `ge` * `gt` * `in` * `le` * `lt` * `ne` * `not` * `or` * `otherwise` * `prefix` * `remainder` * `series` * `suffix` |

#### Объект `Invocation`

Вызов функции, например функции `entitySelector`.

| Поле | Тип | Описание |
| --- | --- | --- |
| args | string[] | Аргументы, передаваемые функции, например исходный код entity selector. |
| function | string | Вызываемая функция, например `entitySelector`. |

#### Объект `Rollup`

Способ представления серии как одного значения для целей сортировки или фильтров на основе серий.

| Поле | Тип | Описание |
| --- | --- | --- |
| parameter | number | - |
| type | string | Поле может принимать значения: * `AUTO` * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` * `VALUE` |

#### Объект `MetricSeries`

Точки данных по измерениям метрики.

Данные представлены двумя массивами одинаковой длины: **timestamps** и **values**. Записи с одинаковым индексом из обоих массивов образуют точку данных с меткой времени.

| Поле | Тип | Описание |
| --- | --- | --- |
| dimensionMap | object | - |
| dimensions | string[] | Устарело, используйте `dimensionMap`.  Упорядоченный список измерений, которым принадлежит список точек данных.  Каждая метрика может иметь определённое число измерений. Измерения сверх этого числа агрегируются в одно, которое здесь показано как `null`. |
| timestamps | integer[] | Список меток времени точек данных.  Значение точки данных для каждого времени из этого массива находится в массиве **values** с тем же индексом. |
| values | number[] | Список значений точек данных.  Метка времени точки данных для каждого значения из этого массива находится в массиве **timestamps** с тем же индексом. |

#### Объект `MetricQueryDQLTranslation`

Перевод запроса метрики в DQL.

| Поле | Тип | Описание |
| --- | --- | --- |
| message | string | Сообщение об ошибке, присутствует только если статус `not supported` |
| query | string | DQL-запрос, соответствующий запросу метрики |
| status | string | Статус перевода в DQL, либо `success`, либо `not supported` Поле может принимать значения: * `not supported` * `success` |

### JSON-модели тела ответа

```
{



"nextPageKey": "null",



"resolution": "1h",



"result": [



{



"data": [



{



"dimensionMap": {



"dt.entity.disk": "DISK-F1266E1D0AAC2C3F",



"dt.entity.host": "HOST-F1266E1D0AAC2C3C"



},



"dimensions": [



"HOST-F1266E1D0AAC2C3C",



"DISK-F1266E1D0AAC2C3F"



],



"timestamps": [



3151435100000,



3151438700000,



3151442300000



],



"values": [



11.1,



22.2,



33.3



]



},



{



"dimensions": [



"HOST-F1266E1D0AAC2C3C",



"DISK-F1266E1D0AAC2C3D"



],



"timestamps": [



3151435100000,



3151438700000,



3151442300000



],



"values": [



111.1,



222.2,



333.3



]



}



],



"dataPointCountRatio": "0.1211",



"dimensionCountRatio": "0.0322",



"metricId": "builtin:host.disk.avail"



},



{



"data": [],



"metricId": "builtin:host.cpu.idle:filter(eq(\"dt.entityhost\",HOST-123))",



"warnings": [



"The dimension key `dt.entityhost` has been referenced, but the metric has no such key."



]



}



],



"totalCount": 3,



"warnings": [



"The dimension key `dt.entityhost` has been referenced, but the metric has no such key."



]



}
```

## Замечание о временном интервале

Dynatrace хранит данные во временных слотах. Объект **MetricValue** показывает *конечную* метку времени слота. Если время, заданное в параметрах **from** или **to** вашего запроса, попадает внутрь временного слота данных, этот слот включается в ответ.

Если метка времени последнего слота данных лежит за пределами указанного временного интервала, последняя точка данных в ответе имеет *более позднюю* метку времени, чем указано в query-параметре **to**.

Dynatrace не прогнозирует будущие данные. Метка времени последней точки данных может лежать в будущем из-за принципа слотов данных, описанного выше. В этом случае такой слот данных содержит неполные данные.

![Схема временных слотов](https://dt-cdn.net/images/timestamp-scheme-v2-488-0b302cef3b.png)

Схема временных слотов

## Примеры

В этих примерах запросы запрашивают точки данных метрик **builtin:host.cpu.usage** и **builtin:host.cpu.idle**.

Временной интервал установлен в **последние 5 минут**. Для этого query-параметр **from** установлен в `now-5m`.

В ответ включаются данные только с этих двух хостов (**HOST-0990886B7D39FE29** и **HOST-0956C3557E9109C1**). Для этого query-параметр **entitySelector** установлен в `type("dt.entity.host"),entityId("HOST-0990886B7D39FE29")`.

Поскольку хост, это измерение запрашиваемых метрик, ту же фильтрацию можно получить, применив [трансформацию `:filter`](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Настройте metric selector для Metric v2 API.") к самим метрикам: задав query-параметр **metricSelector** равным `builtin:host.cpu.(usage,idle):filter(or(eq("dt.entity.host","HOST-0990886B7D39FE29"),eq("dt.entity.host","HOST-0956C3557E9109C1")))` и опустив **entitySelector** как избыточный.

Разница между запросами в представлении данных: первый показывает список точек данных, а второй показывает лишь одну агрегированную точку данных для каждой серии (в конце применяется трансформация `:fold`).

API-токен передаётся в заголовке **Authorization**.

Ответ в формате `application/json`.

Список точек данных

Агрегированная точка данных

#### Curl

С нетрансформированными метриками и фильтром **entitySelector**:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle)&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

С трансформацией, применённой непосредственно к метрикам:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22)))&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### URL запроса

С нетрансформированными метриками и фильтром **entitySelector**:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle)&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m
```

С трансформацией, применённой непосредственно к метрикам:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22)))&from=now-5m
```

#### Тело ответа

Результат усечён до трёх точек данных на измерение.

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:host.cpu.idle",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



81.0,



81.0,



79.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



81.0,



79.0,



78.0



]



}



]



},



{



"metricId": "builtin:host.cpu.usage",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



19.0,



19.0,



21.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



19.0,



21.0,



22.0



]



}



]



}



]



}
```

CSV-таблица со строкой заголовка выглядит так. Чтобы получить её, измените заголовок **Accept** на `text/csv; header=present`.

```
metricId,dt.entity.host,time,value



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:35:00,19.0



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:36:00,19.0



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:37:00,21.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:35:00,19.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:36:00,21.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:37:00,22.0
```

#### Код ответа

200

#### Curl

С нетрансформированными метриками и фильтром **entitySelector**:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):fold&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

С трансформацией, применённой непосредственно к метрикам:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22))):fold&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### URL запроса

С нетрансформированными метриками и фильтром **entitySelector**:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):fold&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m
```

С трансформацией, применённой непосредственно к метрикам:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22))):fold&from=now-5m
```

#### Тело ответа

```
{



"totalCount": 2,



"nextPageKey": null,



"resolution": "1m",



"result": [



{



"metricId": "builtin:host.cpu.idle:fold",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589455320000



],



"values": [



79.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589455320000



],



"values": [



78.0



]



}



]



},



{



"metricId": "builtin:host.cpu.usage:fold",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589455320000



],



"values": [



21.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589455320000



],



"values": [



22.0



]



}



]



}



]



}
```

CSV-таблица со строкой заголовка выглядит так. Чтобы получить её, измените заголовок **Accept** на `text/csv; header=present`.

```
metricId,dt.entity.host,time,value



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:22:00,21.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:22:00,22.00
```

#### Код ответа

200