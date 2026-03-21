---
title: Пользовательские запросы, сегментация и агрегирование данных сессий
source: https://www.dynatrace.com/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data
scraped: 2026-03-06T21:23:09.934912
---

* How-to guide
* 37-min read

Dynatrace захватывает подробные [данные пользовательских сессий](new-user-sessions.md "Learn about user session segmentation and filtering attributes.") каждый раз, когда пользователь взаимодействует с вашим отслеживаемым приложением. Эти данные включают все действия пользователя и высокоуровневые данные о производительности. Используя Dynatrace API или User Sessions Query Language (USQL), вы можете легко выполнять мощные запросы, сегментацию и агрегирование по этим данным. В данном разделе приведены подробности о ключевых словах и функциях, синтаксисе, работе с таблицами Real User Monitoring, автоматических запросах и многом другом.

User Sessions Query Language — это не [SQL](https://en.wikipedia.org/wiki/SQL), и Dynatrace не хранит данные пользовательских сессий в реляционной базе данных. User Sessions Query Language — это специфичный для Dynatrace язык запросов, хотя он опирается на некоторые концепции SQL и имеет схожий синтаксис, что упрощает начало работы.

Выберите предпочтительный подход:

Запросы к пользовательским сессиям через веб-интерфейс Dynatrace

1. Перейдите в раздел ![Query user sessions](https://dt-cdn.net/images/query-user-sessions-512-77c5a8da9f.png "Query user sessions") **Query User Sessions**.
2. Введите запрос и нажмите **Run query**.

### Выбор временного диапазона в USQL

С помощью селектора временного диапазона данные пользовательских сессий можно фильтровать в соответствии с выбранным периодом анализа. Выберите новый временной диапазон.

![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

#### Элементы управления селектором временного диапазона

Глобальный селектор временного диапазона служит фильтром времени, который в большинстве случаев позволяет выбрать конкретный период анализа, сохраняющийся на всех страницах и представлениях при навигации.

![Timeframe selector: presets](https://dt-cdn.net/images/timeframe-selector-basic-355-f0a835da1e.png)

* Вкладка **Presets** содержит список всех стандартных временных диапазонов. Выберите один из них, чтобы установить этот период.
* Вкладка **Custom** отображает календарь. Нажмите на начальный день, затем на конечный день и нажмите **Apply**, чтобы выбрать этот диапазон дней.

  + Выбранные в календаре интервалы устанавливаются так, чтобы заканчиваться в начале следующего дня (со временем `00:00`). Например, если вы выбираете с 3 по 4 сентября, временной диапазон начинается 3 сентября в `00:00` и заканчивается **5** сентября в `00:00`, чтобы вы не пропустили последнюю минуту диапазона. Отображаемое время можно редактировать.
* Вкладка **Recent** отображает недавно использованные временные диапазоны. Выберите один из них, чтобы вернуться к нему.
* Элементы управления **<** и **>** сдвигают диапазон вперёд или назад. Шаг равен длине исходного диапазона. Например, если текущий диапазон — `Last 2 hours` (двухчасовой диапазон, заканчивающийся сейчас), нажмите **<**, чтобы сдвинуть диапазон на два часа назад — к `-4h to -2h`.
* Наведите курсор на временной диапазон, чтобы увидеть время начала, длительность и время окончания.

  ![Timeframe selector: hover](https://dt-cdn.net/images/timeframe-selector-hover-168-cfb13dc777.png)

#### Выражения селектора временного диапазона

При выборе текущего временного диапазона в строке меню отображается редактируемое выражение временного диапазона.

* Читая слева направо, выражение временного диапазона содержит время начала, оператор `to` и время окончания.
* Если явное время окончания отсутствует, подразумеваются `to` и `now`. Например, `-2h` эквивалентно `-2h to now`.
* Поддерживаемые единицы: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (можно также использовать полные слова, например `minutes` и `quarter`)

### Автодополнение в USQL

Автодополнение доступно для операторов запроса на основе введённого текста. Оно контекстно-зависимо и определяется текущим положением курсора, интеллектуально предугадывая следующий ввод.

Информация автодополнения, возвращаемая из API, содержит список предложений с наиболее вероятными значениями вверху списка, а также необходимые корректировки текста запроса и результирующее положение курсора после корректировки. Это позволяет поместить курсор в более удобную позицию после добавления текста, например, внутри скобок при выборе функции.

Список полей содержит только допустимые поля или функции для выбранной таблицы; контекстность проявляется в том, что показываются только числовые поля, когда курсор находится внутри вызова функции, работающей только с числовыми данными, например `SUM()` или `AVG()`.

Значения полей предлагаются только для полей с перечислением. Реальный запрос к Elasticsearch для автодополнения не выполняется.

Dynatrace Environment API

Вы можете выполнять вызовы API с помощью предпочтительного клиента. Соответствующую документацию по API см. в разделе [User sessions API](../../../dynatrace-api/environment-api/rum/user-sessions.md "Learn what the Dynatrace User Sessions Query language API offers.").

Для выполнения этих вызовов вам необходимо разрешение **User sessions** (`DTAQLAccess`), назначенное вашему токену API. Сведения о получении и использовании токена см. в разделе [Dynatrace API — Tokens and authentication](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.").

### Временные диапазоны в Environment API

Доступ к данным пользовательских сессий всегда следует осуществлять с указанием временного диапазона. Доступ к большим временным диапазонам может быть ресурсоёмким из-за большого числа потенциальных совпадений по запросам.

Временной диапазон обычно не является частью самого запроса, а передаётся в отдельных параметрах вызова API. Подробности см. в документации API.

Однако вы можете использовать поля времени, такие как `starttime` и `endtime`, для выбора временного диапазона. Эти поля можно также использовать в функциях, например, чтобы узнать, в какое время суток чаще всего начинаются пользовательские сессии, как в `HOUR(starttime)`.

## Ключевые слова и функции

Для доступа к данным пользовательских сессий определены следующие ключевые слова:

`AND`, `AS`, `ASC`, `BETWEEN`, `BY`, `DESC`, `DISTINCT`, `FALSE`, `FROM`, `GROUP`, `IN`, `IS`, `JSON`, `LIMIT`, `NOT`, `NULL`, `OR`, `ORDER`, `SELECT`, `STARTSWITH`, `TRUE`, `WHERE`, `LIKE`, `FILTER`

Для доступа к данным пользовательских сессий определены следующие функции:

`SUM`, `MAX`, `MIN`, `AVG`, `MEDIAN`, `COUNT`, `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `DATETIME`, `TOP`, `PERCENTILE`, `KEYS`

Ключевые слова, функции и имена столбцов не чувствительны к регистру. Сопоставление строк в условиях `WHERE` чувствительно к регистру.

## Синтаксис

Типичный запрос строится из следующих ключевых слов:

`SELECT <columns> FROM <table> WHERE <condition> GROUP BY <grouping> ORDER BY <ordering>`

Однако единственными обязательными элементами являются `SELECT <columns>` и `FROM <table>`.

Пример

```
SELECT browserType, userId, city, AVG(userActionCount) AS "Average user action count", AVG(duration) AS "Average duration", count(*) AS "Sessions", SUM(totalErrorCount) AS "Errors" FROM usersession WHERE ip between '52.179.11.1' and '52.179.11.255' GROUP BY browserType, userId, city
```

### Часто используемые ключевые слова

#### SELECT `<columns>`

Выбирает один или несколько столбцов из указанной таблицы данных или выполняет функции агрегирования из набора поддерживаемых функций.

```
columns: [DISTINCT] <column>, <column>, ... | function(<parameter>) |


<column> AS <alias> | JSON
```

Пример

```
SELECT country, city, browserfamily FROM usersession


SELECT DISTINCT country, city, useractioncount FROM usersession


SELECT country, city, avg(duration) AS average FROM usersession GROUP BY country, city
```

#### FUNNEL

Позволяет использовать предопределённый формат воронки для запроса. Может применяться для отображения потока определённых действий пользователя. Также может сочетаться с пользовательскими свойствами сессий и другими условиями.

Изменяет синтаксис любого запроса следующим образом:

```
SELECT FUNNEL (<condition> AS <alias>, <condition>, ...) FROM <table> WHERE <condition>
```

* Для запросов `FUNNEL` не используйте функции или ключевые слова `SELECT *`, такие как `JSON`.
* В настоящее время операторы `GROUP BY`, `ORDER BY` и `LIMIT` не поддерживаются в воронках.
* `FUNNEL` не поддерживает упорядочивание. Нет гарантии, что `useraction1` произошло до `useraction2` для запроса `SELECT FUNNEL (useraction.name = "useraction1", useraction.name = "useraction2") FROM usersession`. Этот запрос является эквивалентом двух операторов `SELECT`, как объяснено в примерах ниже.

Пример 1

Вместо выполнения следующих трёх запросов:

```
SELECT COUNT(*) FROM usersession where useraction.name = "AppStart"


SELECT COUNT(*) FROM usersession where useraction.name = "AppStart" AND useraction.name = "searchJourney"


SELECT COUNT(*) FROM usersession where useraction.name = "AppStart" AND useraction.name = "searchJourney"  AND useraction.name = "bookJourney"
```

Следующий единственный запрос возвращает тот же результат:

```
SELECT FUNNEL (useraction.name = "AppStart", useraction.name = "searchJourney", useraction.name = "bookJourney")


FROM usersession
```

Пример 2

Чтобы получить количество пользователей, успешно завершивших бронирование:

```
SELECT FUNNEL (useraction.name="login", useraction.name = "searchJourney", useraction.name = "bookJourney")


FROM usersession
```

#### FROM `<table>`

Можно указать только одну таблицу. Таблицы для данных пользовательских сессий:

* `usersession` содержит информацию о [пользовательских сессиях](../rum-concepts/user-session.md "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
* `useraction` хранит данные о [действиях пользователей](../rum-concepts/user-actions.md "Learn what user actions are and how they help you understand what users do with your application.").
* `userevent` предоставляет информацию о [событиях пользователей](../rum-concepts/user-and-error-events.md#user-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), таких как изменения страниц или события ярости.
* `usererror` содержит дополнительные данные о [событиях ошибок](../rum-concepts/user-and-error-events.md#error-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), то есть об ошибках и сбоях.

Пример

```
SELECT country, city, browserfamily FROM usersession


SELECT name, starttime, endtime, duration FROM useraction ORDER BY duration DESC
```

#### WHERE `<condition>`

Вы можете комбинировать несколько условий с помощью булевой логики и скобок в предложении `WHERE`, например `WHERE (city = 'Barcelona' AND country = 'Spain')`, чтобы включить только города с именем Barcelona, находящиеся в Испании.

```
condition: (condition AND condition) | (condition OR condition) | field IN(...) |


field IS <value> | field IS NULL | field = <value> | field > <value> | field < <value> |


field <> <value> | field IS NOT <value> | field BETWEEN <value> AND <value> | ...
```

Однако только правая часть условий может содержать значение, поэтому сравнение двух полей между собой невозможно.

Примеры

```
SELECT country, city, browserfamily FROM usersession WHERE country = 'Albania' AND screenWidth > 1000


SELECT TOP(country, 20), TOP(city, 20), TOP(duration, 10), AVG(duration) AS average


FROM usersession


WHERE duration BETWEEN 1000 AND 2000


GROUP BY TOP(country, 20), TOP(city, 20), TOP(duration, 10)
```

#### GROUP BY `<grouping>`

Когда поля агрегируются, необходимо указывать соответствующие ключевые слова `GROUP BY`, чтобы указать, как выполняется агрегирование.

```
grouping: <column>, ...
```

Пример

```
SELECT city, count(*) FROM usersession GROUP BY city


SELECT MONTH(starttime) as month, count (*) FROM usersession


GROUP BY month
```

#### LIMIT `<limit>`

Позволяет ограничить количество возвращаемых результатов. Например, вы можете выбрать только первые 10 результатов в сочетании с упорядочиванием.

Система всегда применяет верхний предел для предотвращения перегрузки. Если `LIMIT` не используется, по умолчанию возвращаются 50 результатов.

Пример

```
SELECT city, starttime FROM usersession ORDER BY starttime DESC LIMIT 10
```

`LIMIT` также можно использовать для увеличения числа результатов, когда предложение `LIMIT` отсутствует, поскольку тогда применяется ограничение по умолчанию.

#### ORDER BY `<ordering>`

Позволяет упорядочивать результаты по столбцам в порядке возрастания или убывания. Если порядок не указан, используется возрастающий.

Упорядочивание выполняется по частоте. Например, 5 лучших возвращённых городов — это наиболее часто встречающиеся. Указав поле в предложении `ORDER BY`, можно добавить сортировку по значению для строк, дат и чисел.

Упорядочивание по `enums` или по `значениям функций`, таким как `AVG` и `SUM`, упорядочивает возвращённые результаты, но вы можете не получить верхние элементы. Например, если запрашиваете 5 лучших результатов по `AVG(duration)`, запрашивая только 10, могут добавиться результаты даже в верхней части.

```
ordering: <column> ASC | <column> DESC | <column>, ...
```

Пример 1

```
SELECT useraction.name, starttime FROM usersession ORDER BY starttime DESC
```

Пример 2

Упорядочивание по счётчикам можно достичь, добавив ключевое слово `DISTINCT`.

```
SELECT DISTINCT city, COUNT(*) FROM usersession ORDER BY COUNT(*) DESC
```

Пример 3

Упорядочивание по значениям функций из списка выборки можно достичь, указав только имя столбца или псевдоним, определённый в `SELECT`.

```
SELECT avg(duration) AS average, count(*) as number, day(startTime) as startDay


FROM usersession where duration < 2000


GROUP BY startTime


ORDER BY average
```

или

```
SELECT avg(duration) AS average, count(*) as number, day(startTime) as startDay


FROM usersession where duration < 2000


GROUP BY startTime


ORDER BY number DESC, average ASC
```

#### LIKE

Позволяет сравнивать данные с выражением, используя подстановочные символы для соответствия указанному шаблону. Можно использовать следующие символы:

* `%` или `*`: совпадает с любой строкой из 0 и более символов
* `?`: совпадает с любым одиночным символом

Строковые значения чувствительны к регистру. Например, `SELECT city FROM usersession WHERE userId LIKE "*dynatrace*"` совпадёт с `me@dynatrace.com`, но не с `me@dynaTrace.com`. Чтобы избежать этого, используйте подстановочный символ `?`, как в примере: `SELECT city FROM usersession WHERE userId LIKE "*dyna?race*"`

Экранирование подстановочных символов

Чтобы экранировать подстановочный символ, добавьте перед ним обратную косую черту `\`. Например, `\%`, `\*` и `\?` обрабатываются как стандартные строковые литералы `%`, `*` и `?`.

Чтобы экранировать саму обратную косую черту `\`, добавьте перед ней ещё одну `\`. Результирующая запись `\\` обрабатывается как одиночная обратная косая черта `\`.

Если добавить две обратные косые черты `\\` перед подстановочным символом (что даёт записи вида `\\%`, `\\*` или `\\?`), такая запись обрабатывается как одна экранированная обратная косая черта `\` и один подстановочный символ. Например, запись `\\*` совпадёт с `\abc`, `\123ABC` или `\`.

Сводка по экранированию подстановочных символов:

| Запись | Обрабатывается как | Совпадает с |
| --- | --- | --- |
| `\%` | `%` | `%` |
| `\*` | `*` | `*` |
| `\?` | `?` | `?` |
| `\\` | `\` | `\` |
| `\\%` | `\` и любая строка из нуля или более символов | `\abc`, `\123ABC`, `\` и т.д. |
| `\\*` | `\` и любая строка из нуля или более символов | `\abc`, `\123ABC`, `\` и т.д. |
| `\\?` | `\` и любой одиночный символ | `\a`, `\1`, `\A` и т.д. |

Примеры экранирования подстановочных символов:

```
SELECT userId FROM usersession WHERE userId LIKE "AU\%40KWM"
```

Запрос совпадает с `userId`, равным `AU%40KWM`.

```
SELECT userId FROM usersession WHERE userId like "AU\*40KWM"
```

Запрос совпадает с `userId`, равным `AU*40KWM`.

```
SELECT userId FROM usersession WHERE userId LIKE "AU\?40KWM"
```

Запрос ищет `userId`, равный `AU?40KWM`.

```
SELECT userId FROM usersession WHERE userId LIKE "AU\\%40KWM"
```

Запрос содержит одну экранированную обратную косую черту `\` и один подстановочный символ `%`, поэтому совпадёт с `userId` вида `AU\40KWM`, `AU\abcd40KWM`, `AU\ab12340KWM` или `AU\777_12340KWM`.

Запросы с 11+ условиями LIKE с непостфиксными подстановочными символами отклоняются

Запросы USQL, содержащие 11 и более условий `LIKE` с символами `*` или `%` в начале или середине шаблона поиска (но не в конце), отклоняются от выполнения.

Обычно просто считается количество условий `LIKE` в запросе. Например, в приведённом ниже запросе пять условий `LIKE` — каждое вхождение `LIKE` в предложении `WHERE` и в функции `CONDITION` считается.

```
SELECT CONDITION(COUNT(userSessionId), WHERE useraction.name LIKE '*search.html'),


CONDITION(COUNT(userSessionId), WHERE useraction.name LIKE '*booking-payment1.html')


FROM usersession


WHERE city LIKE "%York"


OR city LIKE "S*Francisco"


AND city LIKE "L*inz"
```

Однако при использовании [функции `FUNNEL`](#funnel) подсчёт становится сложнее. Для этой функции запрос внутренне преобразуется в несколько запросов. После этого преобразования подсчитывается количество условий `LIKE` во внутренних запросах.

Например, следующий запрос:

```
SELECT FUNNEL (useraction.name LIKE "*start", useraction.name LIKE "Jou%rney", useraction.name LIKE "bookJourn*ey") FROM usersession
```

преобразуется в следующие три запроса:

```
SELECT COUNT(*) FROM usersession where useraction.name LIKE "*start"


SELECT COUNT(*) FROM usersession where useraction.name LIKE "*start" AND useraction.name LIKE "Jou%rney"


SELECT COUNT(*) FROM usersession where useraction.name LIKE "*start" AND useraction.name LIKE "Jou%rney" AND useraction.name LIKE "bookJourn*ey"
```

Таким образом, в приведённом выше запросе `FUNNEL` на самом деле шесть условий `LIKE`.

#### FILTER

Позволяет фильтровать функции, возвращающие числовые значения, тем самым отображая только определённые результаты из агрегирований.

Пример

```
SELECT useraction.application,


AVG(usersession.doubleProperties.bookings)


FILTER > 1500


FROM usersession


WHERE usersession.doubleProperties.bookings IS NOT NULL


GROUP BY useraction.application
```

Функции `WHERE` и `FILTER` не взаимозаменяемы. В то время как предложение `WHERE` можно использовать только для абсолютных значений, функция `FILTER` работает и с агрегированными значениями.

### Часто используемые функции

#### MIN(field)

Запрашивает минимальное значение числового поля или поля даты.

Пример

```
SELECT MIN(duration), MAX(duration), AVG(duration), MEDIAN(duration)


FROM usersession
```

#### MAX(field)

Запрашивает максимальное значение числового поля или поля даты.

Пример

```
SELECT MIN(duration), MAX(duration), AVG(duration), MEDIAN(duration)


FROM usersession
```

#### AVG(field)

Запрашивает среднее значение числового поля или поля даты. Может возвращать `NaN`, если поле всегда равно `null`.

Пример

```
SELECT MIN(duration), MAX(duration), AVG(duration), MEDIAN(duration)


FROM usersession
```

#### MEDIAN(field)

Запрашивает медианное значение числового поля или поля даты.

Пример

```
SELECT MIN(duration), MAX(duration), AVG(duration), MEDIAN(duration)


FROM usersession
```

#### SUM(field)

Вычисляет сумму числового поля.

Пример

```
SELECT TOP(name, 20), SUM(duration) FROM useraction


GROUP BY name
```

#### COUNT(field), COUNT(\*), COUNT(DISTINCT field)

Подсчитывает количество совпадающих строк.

* `COUNT(*)`: подсчитывает количество совпадающих элементов.
* `COUNT(<field>)`: подсчитывает количество совпадающих элементов, где `<field>` не равно null.
* `COUNT(DISTINCT <field>)`: подсчитывает количество различных значений `<field>` среди выбранных элементов.

Пример

```
SELECT country, COUNT(*), COUNT(city), COUNT(DISTINCT city)


FROM usersession


GROUP BY country
```

Результаты, возвращаемые функцией `COUNT(DISTINCT <field>)`, являются приблизительными во избежание высокого потребления памяти. Если `COUNT(DISTINCT <field>)` используется для поля с высокой кардинальностью, результаты могут быть ещё менее точными. Поля с высокой кардинальностью — это поля, содержащие мало дубликатов.

Результаты, основанные на экстраполированных данных, могут быть ещё более обобщёнными; см. раздел [Ограничения](#limitations) для получения дополнительной информации.

Поля с высокой кардинальностью

| Таблица | Поля |
| --- | --- |
| `usersession` | `ip` , `userSessionId` , `internalUserId` , `userId` |

Dynatrace отклоняет и не выполняет запросы с `COUNT(DISTINCT <field>)`, которые могут потреблять много памяти. Это происходит для всех полей с чрезвычайно высокой кардинальностью, например для полей `dateTime`, таких как `usersession.startTime`, `usersession.endTime` или `useraction.networkTime`.

Поля с чрезвычайно высокой кардинальностью

| Таблица | Поля |
| --- | --- |
| `usersession` | `startTime` , `endTime` , `replayEnd` , `clientTimeOffset`, `duration` , `replayStart` |
| `useraction` | `domContentLoadedTime` , `startTime` , `firstPartyBusyTime` , `documentInteractiveTime` , `navigationStart` , `totalBlockingTime` Deprecated, `largestContentfulPaint` , `visuallyCompleteTime` , `cdnBusyTime` , `endTime` , `domCompleteTime` , `networkTime` , `loadEventStart` , `serverTime` , `firstInputDelay` , `responseStart` , `thirdPartyBusyTime` , `duration` , `loadEventEnd` , `responseEnd` , `frontendTime` , `requestStart` |
| `userevent` | `startTime` |
| `usererror` | `startTime` |

Пример

```
SELECT country, COUNT(*), COUNT(city), COUNT(DISTINCT city)


FROM usersession


GROUP BY country
```

#### TOP(field, n)

Возвращает первые `<n>` результатов из поля. По умолчанию `1` (верхнее значение), если `n` не указано.

Пример

```
SELECT TOP(name, 20), SUM(duration)


FROM useraction


GROUP BY name
```

Если выбрано `TOP(<field>, n)` и результаты сгруппированы, но `<field>` не входит в группировку, первые n элементов возвращаются как список в одном поле.

```
SELECT TOP(country, 20), TOP(city, 3), COUNT(*)


FROM usersession


GROUP BY country
```

#### YEAR(datefield), MONTH(datefield), DAY(datefield), HOUR(datefield), MINUTE(datefield)

Возвращает указанный элемент, извлечённый из поля даты.

* `YEAR`: четырёхзначный год.
* `MONTH`: номер месяца от 1 до 12.
* `DAY`: день месяца от 1 до 31.
* `HOUR`: значение часа от 0 до 23.
* `MINUTE`: значение минуты от 0 до 59.

Пример

```
SELECT starttime,


DATETIME(starttime), YEAR(starttime), MONTH(starttime), DAY(starttime), HOUR(starttime), MINUTE(starttime)


FROM usersession


ORDER BY starttime DESC
```

#### DATETIME(datefield [, format [, interval]])

Форматирует выбранное поле даты по указанной строке формата. Формат по умолчанию — `yyyy-MM-dd HH:mm`.

Допустимые буквы в строке формата:

* `y`: год
* `M`: месяц
* `d`: день месяца
* `H`: час (0–23)
* `h`: час (1–12)
* `m`: минута
* `s`: секунда
* `E`: день недели (Mon–Sun)

Интервалы `year`|`month`|`week` предназначены для одного `interval`. Для `d` (дней), `h` (часов), `m` (минут) или `s` (секунд) можно использовать число с буквой, например `5m`. Например, `SELECT DISTINCT DATETIME(starttime, 'HH:mm', '5m'), COUNT(*) FROM usersession` подсчитывает сессии в пятиминутных блоках.

Пример

```
SELECT DATETIME(starttime, 'yyyy-MM') FROM usersession


SELECT DISTINCT DATETIME(starttime, 'HH:mm', '5m'), COUNT(*) FROM usersession
```

Аналогично другим функциям дат (`YEAR`, `MONTH`, `DAY`, `HOUR` и `MINUTE`), `DATETIME` можно использовать для форматирования результата (даже результата других функций, таких как `MAX`, `MIN`, `AVG` или `CONDITION`), создания гистограмм или получения списка временных меток с результатами, например дней недели, когда использовалось приложение.

Примеры

```
SELECT application, DATETIME(MAX(starttime)) AS LastUsedTime FROM useraction GROUP BY application


SELECT DATETIME(starttime, "HH") AS hourOfDay, COUNT(*) FROM usersession GROUP BY hourOfDay


SELECT application, DATETIME(starttime, "E") AS daysOfWeek FROM useraction GROUP BY application


SELECT DATETIME(CONDITION(MAX(startTime), WHERE name = "index.jsp")) FROM useraction
```

#### CONDITION(function, condition)

Позволяет комбинировать несколько функций с различными условиями.

Допустимые функции в строке формата:

* `MIN()`
* `MAX()`
* `AVG()`
* `SUM()`
* `PERCENTILE()`
* `MEDIAN()`
* `COUNT()`

Можно комбинировать несколько условий с помощью булевой логики и скобок в функции `CONDITION`, например `CONDITION(COUNT(*), WHERE city = 'Barcelona' AND country = 'Spain')`, чтобы включить только города с именем Barcelona, находящиеся в Испании.

```
CONDITION(function, condition)


condition:


(condition AND condition) | (condition OR condition) | field IN(...) |


field IS <value> | field IS NULL | field = <value> | field > <value> | field < <value> |


field <> <value> | field IS NOT <value> | field BETWEEN <value> AND <value> | ...
```

Также можно использовать предложение `FILTER` для фильтрации функций с числовыми значениями, отображая только определённые результаты из агрегирований.

```
SELECT CONDITION(COUNT(usersessionId), WHERE userActionCount > 2 AND useraction.name = "search.jsp") FILTER > 1000, city FROM usersession GROUP BY city
```

Пример

```
SELECT CONDITION(COUNT(usersessionId), WHERE userActionCount > 2 AND useraction.name = "search.jsp") FROM usersession


SELECT CONDITION(SUM(usersession.duration), WHERE name = "index.jsp") AS c1, CONDITION(SUM(usersession.duration), WHERE name = "search.jsp") AS c2, CONDITION(SUM(usersession.duration), WHERE name IS NOT "index.jsp" AND name IS NOT "search.jsp") AS c3 FROM useraction WHERE (duration > 1000 OR usersession.userActionCount > 4)


SELECT CONDITION(SUM(usersession.duration), WHERE name = "index.jsp") AS c1 FROM useraction WHERE (duration > 1000 OR usersession.userActionCount > 4) ORDER BY c1


SELECT DATETIME(CONDITION(MIN(startTime ), WHERE useraction.application = "RUM Default Application" ), "yyyy-MM-dd" ) FROM usersession
```

#### PERCENTILE

Представляет значение, ниже которого находится определённый процент точек данных. Полезно для определения скорости вашего приложения для клиентов, получающих наибольшее время ответа.

Пример

```
SELECT name, usersession.country, usersession.browserFamily,


AVG(duration),


MEDIAN(duration),


PERCENTILE(duration, 99)


FROM useraction


WHERE useraction.name = "easytravel/rest/login"


GROUP BY usersession.country, usersession.browserFamily, name


ORDER BY usersession.continent
```

#### KEYS(customProperty)

Возвращает ключи [свойств действий пользователя или свойств пользовательской сессии](../web-applications/analyze-and-use/action-and-session-properties.md "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.") в соответствии с типом данных свойства, определённым в аргументе.

Изучите таблицу ниже, чтобы понять, какие ключи возвращаются — ключи свойств действий пользователя или ключи свойств пользовательской сессии.

| KEYS(customProperty) | Таблица | Свойства действий | Свойства сессий |
| --- | --- | --- | --- |
| `KEYS(<dataType>Properties)` | `useraction` | Применимо |  |
| `KEYS(<dataType>Properties)` | `usersession` |  | Применимо |
| `KEYS(useraction.<dataType>Properties)` | `useraction` | Применимо |  |
| `KEYS(useraction.<dataType>Properties)` | `usersession` | Применимо |  |
| `KEYS(usersession.<dataType>Properties)` | `useraction` |  | Применимо |
| `KEYS(usersession.<dataType>Properties)` | `usersession` |  | Применимо |

Часть `<dataType>` функции может принимать следующие значения:

* `string`
* `long`
* `double`
* `date`

Пример 1

```
SELECT KEYS(stringProperties) FROM useraction WHERE application = "easyTravel demo application"


SELECT KEYS(useraction.longProperties) FROM usersession WHERE applicationType="WEB_APPLICATION" ORDER BY keys(useraction.longProperties)


SELECT KEYS(usersession.stringProperties) FROM useraction WHERE usersession.city ="Berlin"
```

Для получения различных ключей свойств действий или сессий используйте `DISTINCT KEYS(customProperty)`.

Пример 2

```
SELECT DISTINCT KEYS(stringProperties) FROM useraction WHERE useraction.application = "easyTravel demo application" ORDER BY keys(stringProperties)


SELECT DISTINCT KEYS(doubleProperties) FROM usersession
```

## Математические операции

В запросах поддерживаются следующие операции:

* операции над числами
* операции над числовыми полями и полями типа dateTime
* операции над определёнными функциями, такими как `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`
* операции над числовыми значениями с отображением в различных единицах измерения

### Синтаксис

`Number/NumericField/DateTimeField/Function OPERATOR Number/NumericField/DateTimeField/Function`

Функция: `YEAR`, `MONTH`, `DAY`, `HOUR` или `MINUTE`
Оператор: `+`, `-`, `*`, `/`, `%` или `MOD`

Пример

```
SELECT 7 + 80 * 100, duration + startTime, MONTH(startTime) - 1


FROM usersession
```

## Условия

Все условия должны начинаться с идентификатора, например имени поля, и должны сравниваться со значением. Сравнение двух полей между собой невозможно.

Текст в кавычках всегда чувствителен к регистру.

### Базовые операторы

Базовые операторы сравнения: `=`, `!=`, `<>`, `<`, `>`, `<=`, `>=`, `IS` и `IS NOT`.

Чтобы проверить наличие значения в поле, сравните поле с `NULL`.

Пример

```
SELECT userId FROM usersession WHERE userActionCount > 3
```

### Диапазоны

Диапазоны обрабатываются ключевыми словами `BETWEEN` или `NOT BETWEEN`, `<lowerLimit>` и `<upperLimit>`.

Пример 1

```
SELECT DISTINCT ip FROM usersession


WHERE ip BETWEEN '192.168.0.0' AND '192.168.255.255'
```

Пример 2

```
SELECT startTime FROM useraction


WHERE NOT startTime BETWEEN $NOW - DURATION("2h") AND $NOW
```

Пример 3

```
SELECT ip, browserType, userId, city


FROM usersession


WHERE NOT ip BETWEEN '52.179.11.1' AND '52.179.11.255'
```

### Множества

Ключевое слово `IN` позволяет сократить запись `"WHERE" <field> = val1 OR <field> = val2 OR <field> = val3`.

Пример

```
SELECT userId FROM usersession WHERE city IN ("NEW YORK", "San Francisco")
```

### Строковые условия

Строковое условие `"STARTSWITH"` проверяет, начинается ли строка или поле перечисления с указанного текста.

Пример

```
SELECT city FROM usersession WHERE userId STARTSWITH "dynatrace"
```

### Значения типа datetime

Когда условия применяются к полю типа datetime, поддерживаются следующие форматы значений:

| Формат | Описание | Пример |
| --- | --- | --- |
| — | Временная метка Unix в миллисекундах (число) | `1514152800000` |
| `yyyy-MM-dd'T'HH:mm:ssZ` | ISO datetime с часовым поясом | `2017-12-24T21:00:00+01:00` |
| `yyyy-MM-dd HH:mm:ss` | Дата с необязательным временем | `2017-12-24 21:00` |
| `yyyy/MM/dd HH:mm:ss` | Дата с необязательным временем | `2017/12/24 21` |
| `MM/dd/yyyy HH:mm:ss` | Дата с необязательным временем | `12/24/2017` |
| `dd.MM.yyyy HH:mm:ss` | Дата с необязательным временем | `24.12.2017 21:00:00` |

Для форматов, где время необязательно, поддерживаются следующие форматы времени:

| Формат | Пример |
| --- | --- |
| `HH:mm:ss` | `08:20:59` |
| `H:mm:ss` | `8:20:59` |
| `HH:mm` | `08:20` |
| `H:mm` | `8:20` |
| `HH` | `08` |
| `H` | `8` |

Если время отсутствует, по умолчанию используется `00:00:00`.

Иногда запросы со значениями datetime могут давать некорректные результаты из-за перехода на летнее время. Если дата в запросе предшествует дате окончания летнего времени (например, до 7 ноября 2021 года 02:00), попробуйте использовать ISO datetime со смещением по времени, например `2021-10-05T17:30:00+03:00`.

Пример

```
SELECT starttime FROM usersession WHERE starttime > "8.8.2018 8:00"
```

### Оптимизация условий

#### IN

Если запрос содержит несколько условий равенства для одного и того же поля через `OR`, используйте функцию `IN` — она более производительна. Например, следующий запрос можно переписать с использованием `IN`.

**До**

```
SELECT COUNT(*) FROM userevent


WHERE pageReferrer = "/some/page/referrer/1"


OR pageReferrer = "/some/page/referrer/2"


OR pageReferrer = "/some/page/referrer/3"


OR pageReferrer = "/some/page/referrer/4"


OR pageReferrer = "/some/page/referrer/5"
```

**После**

```
SELECT COUNT(*) FROM userevent


WHERE pageReferrer IN ("/some/page/referrer/1",


"/some/page/referrer/2",


"/some/page/referrer/3",


"/some/page/referrer/4",


"/some/page/referrer/5")
```

#### NOT IN

Для ускорения запросов используйте массивы: вместо нескольких операторов `NOT`, `<>` или `!=` используйте оператор `NOT IN`.

**До**

```
SELECT useraction.name, usersession.userId


FROM useraction


WHERE name = "loading of page /"


AND usersession.userId IS NOT NULL


AND usersession.userId <> "Speed Travel Agency"


AND usersession.userId <> "some user"


AND usersession.userId <> "easyTravel - One step to happiness"


AND usersession.userId <> "easyTravel - Booking - Finish"
```

**После**

```
SELECT useraction.name, usersession.userId


FROM useraction


WHERE name = "loading of page /"


AND usersession.userId IS NOT NULL


AND NOT usersession.userId IN ("Speed Travel Agency",


"some user",


"easyTravel - One step to happiness",


"easyTravel - Booking - Finish")
```

## Расширенные синтаксические конструкции

### Запрос диапазонов IP

Поле IP можно запрашивать по диапазонам адресов. Работают оба варианта: `BETWEEN ip > <lower ipaddress range> AND ip < <upper ipaddress range>` или `BETWEEN <lower ipaddress range> AND <lower ipaddress range>`.

Пример

```
SELECT * FROM usersession WHERE ip > '211.44.94.0' AND ip < '212.113.5.0'


SELECT * FROM usersession WHERE ip BETWEEN '211.44.94.0' AND '212.113.5.0'
```

### Запрос с использованием селектора временного диапазона

Вы можете использовать следующие ключевые слова для выбора времени начала и окончания, определённых в селекторе временного диапазона.

* `TIME_FRAME_START`
* `TIME_FRAME_END`

Пример

```
SELECT * FROM usersession WHERE startTime >= $TIME_FRAME_START AND endTime < $TIME_FRAME_END
```

Селекторы временного диапазона можно использовать для ограничения временного диапазона в запросах, выполняемых для вторичных таблиц (`useraction`). По умолчанию фильтр временного диапазона применяется к таблице `usersession`, даже если запрос выполняется для любой вторичной таблицы. Чтобы применить фильтр и к вторичной таблице, используйте селектор временного диапазона для добавления условия на поле `startTime` вторичной таблицы. Смотрите следующий пример для получения `name` и `duration` действий пользователя, произошедших только в рамках временного диапазона запроса:

Пример

```
SELECT name, duration FROM useraction


WHERE startTime BETWEEN $TIME_FRAME_START and $TIME_FRAME_END
```

### Запрос с относительным временным диапазоном

Вы можете выбрать временной диапазон относительно момента выполнения запроса. Текущее время выражается переменной `$NOW`.

`$NOW [+/-] DURATION("[number]TIME_UNIT")`

Поддерживаются следующие единицы времени для выражения длительности:

* `y`: год
* `q`: квартал
* `M`: месяц
* `d`: день
* `w`: неделя
* `h`: час
* `m`: минута
* `s`: секунда

Пример

```
SELECT * FROM usersession WHERE startTime >= $NOW - DURATION("1q") AND endTime <= $NOW


SELECT * FROM useraction WHERE startTime BETWEEN $NOW - DURATION("2h") AND $NOW


SELECT * FROM useraction WHERE usersession.startTime >= $TIME_FRAME_START - DURATION("2h") AND $NOW - DURATION("1h")
```

Временной диапазон, выбранный в веб-интерфейсе Dynatrace или Dynatrace API, по-прежнему применяется к результатам, даже если в запросе используется фильтрация по временным меткам.

### Вторичные таблицы для `usersession`, `useraction`, `userevent` и `usererror`

При использовании `SELECT` с `usersession`, `useraction`, `userevent` или `usererror` можно получить доступ к столбцам из другой таблицы и включить их в результаты, добавив к именам столбцов префикс с именем таблицы.

Пример 1

Выборка логического представления таблицы `usersession` или `useraction`. При добавлении информации из `useraction` в запрос к `usersession` несколько значений объединяются в результирующем столбце.

```
SELECT city, useraction.name FROM usersession


SELECT usersession.city, name FROM useraction
```

Вторичные таблицы `userevent` и `usererror` можно использовать аналогичным образом.

```
SELECT usersession.country, name, page FROM userevent


SELECT usersession.country, name, type FROM usererror


SELECT country, userevent.name, usererror.name FROM usersession
```

При запросе из первичной таблицы `usersession` можно комбинировать поля из других вторичных таблиц (`useraction`, `userevent` и `usererror`). Поля из вторичных таблиц можно также использовать в условии `WHERE`.

Пример 2

```
SELECT city, useraction.name, userevent.page, usererror.type FROM usersession


SELECT city, usererror.name, userevent.page, useraction.duration FROM usersession WHERE usererror.name IS NOT NULL
```

Пример 3

Вывод всех пользовательских сессий, содержащих событие пользователя или действие пользователя из одного приложения.

```
SELECT * FROM usersession


WHERE userevent.application = "a" OR useraction.application="a"
```

При запросе из любой из вторичных таблиц (`useraction`, `userevent` или `usererror`) можно использовать поля только из первичной таблицы `usersession`; поля из других вторичных таблиц недоступны. Например, следующий запрос завершится ошибкой, так как выбранная таблица — `userevent`, что означает возможность выбора только полей из `userevent` или `usersession`.

```
SELECT usersession.city, useraction.name, userevent.page, usererror.type FROM userevent
```

Та же ограничение применяется к другим вторичным таблицам — `useraction` и `usererror`.

Пример 4

Следующие запросы не завершатся ошибкой, поскольку в них используются только поля из выбранной вторичной таблицы и из первичной таблицы.

```
SELECT usersession.userId, name, duration FROM useraction


SELECT usersession.userId, name, type FROM usererror
```

Нет возможности связать вторичные таблицы между собой и определить какие-либо отношения между таблицами `useraction`, `userevent` и `usererror` или порядок их возникновения. Поэтому невозможно определить, какое `useraction` вызвало какое `usererror`. Единственная связь — это принадлежность к одной и той же `usersession`.

Применяемые условия имеют разное значение в зависимости от таблицы. Например, чтобы вывести все пользовательские сессии, содержащие действия пользователя с именами `a` и `b`:

```
SELECT * FROM usersession


WHERE useraction.name = "a" AND useraction.name = "b"
```

Это означает, что сессия должна содержать действие пользователя с именем `"a"` и действие пользователя с именем `"b"`. Выполнение того же запроса к таблице `useraction` вернёт пустой результат, так как одно и то же действие пользователя не может иметь два разных значения имени.

Если вы хотите выбрать данные пользовательской сессии для конкретного действия пользователя, соответствующего нескольким критериям, выполните следующий запрос к таблице `useraction`.

```
SELECT usersession.*, * FROM useraction


WHERE useraction.name = "a" AND useraction.duration > 1000
```

В этом случае каждое действие пользователя в результате удовлетворяет обоим условиям.

Рассмотрим ещё один запрос.

```
SELECT COUNT(usersession.userSessionId)


FROM usersession


WHERE userevent.name = 'Page change'


AND userevent.pageGroup = '/Booking'


AND userevent.type = 'UserTag'
```

Поскольку запрос выполняется к таблице `usersession`, условия применяются ко всему набору событий пользователя, принадлежащих одной сессии. Это означает, что любая пользовательская сессия с событиями пользователя, удовлетворяющими условиям, учитывается в счётчике. Например, если пользовательская сессия содержит три события пользователя, каждое из которых удовлетворяет одному из заданных условий, эта сессия учитывается в счётчике.

Если выполнить тот же запрос к таблице `userevent`, условия применяются к каждому отдельному событию пользователя. Это означает, что в счётчике учитываются только пользовательские сессии, содержащие хотя бы одно событие пользователя, удовлетворяющее **всем** условиям.

```
SELECT COUNT(usersession.userSessionId)


FROM userevent


WHERE userevent.name = 'Page change'


AND userevent.pageGroup = '/Booking'


AND userevent.type = 'UserTag'
```

### Фильтрация по полям вторичной таблицы

Будьте осторожны при фильтрации по полям одной из вторичных таблиц. Рассмотрите примеры ниже.

**Пример 1**

```
SELECT useraction.name FROM usersession WHERE useraction.name="abc"
```

Этот запрос возвращает список всех пользовательских сессий, содержащих хотя бы одно действие пользователя с именем `abc`. Результат содержит список всех действий пользователя для каждой сессии, поскольку запрос выполняется на уровне `usersession`.

**Пример 2**

```
SELECT name FROM useraction WHERE name="abc"
```

Этот запрос возвращает список только тех действий пользователя, которые названы `abc`.

### SELECT \* FROM table

Пример

```
SELECT * FROM usersession


SELECT useraction.* FROM usersession


SELECT city, useraction.* FROM usersession


SELECT *, useraction.* FROM usersession
```

Звёздочка `*` сама по себе выбирает столбцы из основной таблицы, а не из вторичной. Например, поля из `useraction` не включаются в `SELECT * FROM usersession`, если вы не включили `useraction.*`.

### Экспорт в JSON

Ключевое слово `JSON` добавляет дополнительный столбец, содержащий данные о запрошенной записи (пользовательская сессия, действие пользователя, событие пользователя или ошибка пользователя) в формате JSON.

Если выбрана первичная таблица `usersession`, возвращаются полные строки JSON для совпадающих пользовательских сессий, независимо от выбранных столбцов.

Пример 1

Следующий запрос возвращает совпадающие пользовательские сессии в виде JSON в дополнительном столбце, включая данные из всех вторичных таблиц.

```
SELECT usersessionId, browserFamily, useraction.name, useraction.duration, JSON


FROM usersession LIMIT 5
```

Если выбрана [вторичная таблица](#usql-secondarytables) (`useraction`, `userevent` или `usererror`), возвращаются полные строки JSON для совпадающих подзаписей (действие пользователя, событие пользователя или ошибка пользователя).

Пример 2

Следующий запрос возвращает совпадающие действия пользователя в виде JSON в дополнительном столбце, без данных из таблицы `usersession` или других вторичных таблиц.

```
SELECT name, duration, JSON


FROM useraction LIMIT 5
```

См. также [Экспорт пользовательских сессий](export-session-data.md "Set up Dynatrace to export user session data to a provided webhook endpoint.").

### Экранирование строк

Строковые литералы можно заключать в одинарные или двойные кавычки. Однако если нужно использовать тот же символ кавычки внутри строки, просто удвойте его.

Пример

```
SELECT * FROM usersession WHERE userId = "some 'custom' name for ""my user"""


SELECT * FROM usersession WHERE userId = 'some ''custom'' name for "my user"'
```

### Воронковые диаграммы

Воронковые диаграммы позволяют отслеживать шаги в вашем цифровом сервисе и исследовать проблемные места для ваших пользователей. В сочетании с Session Replay эта функциональность позволяет видеть, на каком этапе пользователь испытывает трудности в вашем приложении.

Пример

```
SELECT FUNNEL(


useraction.name = "AppStart (easyTravel)" AS "Open easytravel",


useraction.name = "searchJourney" AS "Search journey",


useraction.name = "bookJourney" AS "Book journey",


useraction.matchingConversionGoals = "Payment" OR useraction.matchingConversionGoals = "booking-finished" AS "Booked")


FROM usersession
```

Также можно фильтровать по конкретному сегменту. Например, использовать свойства сессии для извлечения списка приоритетных клиентов.

Пример

```
SELECT FUNNEL(


useraction.name = "AppStart (easyTravel)" AS "Open easytravel",


useraction.name = "searchJourney" AS "Search journey",


useraction.name = "bookJourney" AS "Book journey",


useraction.matchingConversionGoals = "Payment" OR useraction.matchingConversionGoals = "booking-finished" AS "Booked")


FROM usersession


WHERE stringProperties.memberstatus="GOLD"
```

`FUNNEL` не поддерживает упорядочивание. Нет гарантии, что `useraction1` произошло до `useraction2` для запроса `SELECT FUNNEL (useraction.name = "useraction1", useraction.name = "useraction2") FROM usersession`. Этот запрос является эквивалентом двух операторов `SELECT`.

## Доступные таблицы и поля данных пользовательских сессий

Для данных пользовательских сессий доступны следующие таблицы.

* `usersession` содержит информацию о [пользовательских сессиях](../rum-concepts/user-session.md "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
* `useraction` хранит данные о [действиях пользователей](../rum-concepts/user-actions.md "Learn what user actions are and how they help you understand what users do with your application.").
* `userevent` предоставляет информацию о [событиях пользователей](../rum-concepts/user-and-error-events.md#user-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), таких как изменения страниц или события ярости.
* `usererror` содержит дополнительные данные о [событиях ошибок](../rum-concepts/user-and-error-events.md#error-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), то есть об ошибках и сбоях.

[Вторичные таблицы для `usersession`, `useraction`, `userevent` и `usererror`](#usql-secondarytables) содержат описание того, как данные одной таблицы доступны в другой.

Поля описаны в [User sessions API — User session structure](../../../dynatrace-api/environment-api/rum/user-sessions/user-session-structure.md "Learn the structure of a user session in the Dynatrace User Session Query language API.").

Также можно проверить объект **UserSession** в [API Explorer](../../../dynatrace-api.md#api-explorer "Find out what you need to use the Dynatrace API.").

## Выполнение запросов USQL для пользовательских отчётов

Интерфейс REST позволяет получать результаты пользовательских запросов. Всё, что нужно — создать уникальный [токен API](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.") с привилегией **User session query language**. Возможность запрашивать данные пользовательских сессий таким образом полезна в автоматизированном тестировании, верификации данных и других автоматизированных функциях. Доступны следующие конечные точки:

`/table`: возвращает данные в виде плоской таблицы, даже при группировке по различным элементам и выполнении иерархических агрегирований по данным пользовательских сессий.

`/tree`: возвращает данные в виде полного иерархического дерева на основе входных данных.

Доступны следующие параметры запроса:

`query`: необходимо кодировать при включении в URL, например `%20` вместо пробелов.
`startTimestamp/endTimestamp`: позволяет задавать точки времени в виде числа миллисекунд с эпохи Unix. Если не указаны, по умолчанию используются последние два часа.

Примеры

Следующий код:

```
curl --location --insecure -H "Content-Type: application/json" -H "Authorization: Api-Token _token_" \


-XGET "https://{your-environment-id}.live.dynatrace.com/api/v1/userSessionQueryLanguage/table?query=select%20city,count(*)%20from%20usersession%20group%20by%20city"
```

возвращает следующий результат:

```
{


"columnNames": ["city",    "count(*)"],


"values": [


["Dublin",    23],


["N. Virginia (Amazon)",    80],


["Portland",    56]


]


}
```

Следующий код:

```
curl --location --insecure -H "Content-Type: application/json" -H "Authorization: Api-Token _token_" \


-XGET "https://{your-environment-id}.live.dynatrace.com/api/v1/userSessionQueryLanguage/tree?query=select%20country,city,count(*)%20from%20usersession%20group%20by%20country,city"
```

возвращает следующий результат:

```
{


"branchNames": ["country",    "city"],


"leafNames": ["count(*)"],


"values": {


"United States": {


"Portland": [56],


"N. Virginia (Amazon)": [83]


},


"Ireland": {


"Dublin": [24]


}


}


}
```

Подробнее о [user sessions API](../../../dynatrace-api/environment-api/rum/user-sessions.md "Learn what the Dynatrace User Sessions Query language API offers.").

## Преобразование запросов в пользовательские метрики USQL

Некоторые запросы можно преобразовать в пользовательские метрики USQL для [веб-](../web-applications/additional-configuration/custom-metrics-from-user-sessions.md "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications."), [мобильных](../mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps.md "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for mobile applications.") и [пользовательских приложений](../custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps.md "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for custom applications.").

Пользовательские метрики USQL доступны как пользовательские метрики сессий (USCM) и пользовательские метрики действий (UACM). Пользовательские метрики действий поддерживаются начиная с версии Dynatrace 1.260.

1. Перейдите в раздел ![Query user sessions](https://dt-cdn.net/images/query-user-sessions-512-77c5a8da9f.png "Query user sessions") **Query User Sessions**.
2. Введите запрос и выберите **Run query**.
   Список поддерживаемых полей см. в подробных руководствах для [веб-](../web-applications/additional-configuration/custom-metrics-from-user-sessions.md#properties-and-supported-values "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications."), [мобильных](../mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps.md#properties-and-supported-values "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for mobile applications.") и [пользовательских приложений](../custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps.md#properties-and-supported-values "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for custom applications.").
3. Выберите **Create custom metric**.
4. Введите имя метрики и проверьте предложенные настройки.

## Ограничения

* Dynatrace хранит данные Real User Monitoring (действия и сессии пользователей) в течение ограниченного периода. Подробности см. в разделе [Сроки хранения данных](../../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md "Check retention times for various data types.").
* Набор результатов по умолчанию — 50, но количество результатов можно увеличить до максимума 5000 с помощью ключевого слова `LIMIT`.
* Максимальное количество сегментированных результатов ограничено 100 000. По умолчанию — 10 000.
  Это влияет на применение `TOP()` при использовании `DISTINCT` или `GROUP BY`. Если `TOP()` не указан, 10 000 возможных результатов равномерно распределяются по указанным столбцам. Эти значения по умолчанию можно переопределить, указав `TOP()` для каждого столбца. Произведение значений `TOP()` не может превышать 100 000 результатов.

  Дополнительные ограничения

  + Функцию `TOP()` можно использовать для увеличения числа различных значений на агрегирование.
  + Максимальное количество различных результатов на агрегирование ограничено 1000.
  + Следующий запрос использует не более 10 000 теоретически возможных результатов:
    `select browserFamily, city, count * FROM usersession group by browserFamily, city`
  + Следующий запрос содержит `TOP()` и поэтому может использовать до 100 000 (100 × 1000) теоретически возможных результатов:
    `select TOP(browserFamily, 1000), TOP(city, 100), count * FROM usersession group by browserFamily, city`
* Объединения (JOIN) не допускаются.
* В одном `SELECT` допускается только одна таблица.
* Поиск строковых значений с помощью регулярных выражений не поддерживается.
* Нельзя сравнивать два разных поля. Например, `WHERE field1 = field2` не работает.
* Условия `WHERE` работают только с полями, поэтому ни `WHERE true`, ни `WHERE COUNT(*) > 3` не поддерживаются.
* Можно запрашивать только завершённые пользовательские сессии. Активные пользовательские сессии не учитываются.
* Упорядочивание поддерживается частично.

  Например, упорядочивание по математической операции не поддерживается.

  ```
  SELECT endTime - startTime AS duration FROM usersession ORDER BY duration
  ```
* При широких временных диапазонах и высокой нагрузке данные могут быть экстраполированы из выборки (уровень экстраполяции). Это происходит независимо от того, используете ли вы Dynatrace API или веб-интерфейс Dynatrace. Если требуются точные данные на 100%, сократите временной диапазон или добавьте дополнительные условия для более точной фильтрации данных.
* Функции не допускаются в предложении `GROUP BY`. Поэтому, если нужно группировать по месяцу, задайте псевдоним.
* `FUNNEL` нельзя использовать с функциями `SELECT *`, ключевыми словами типа `JSON`, а также с операторами `GROUP BY`, `ORDER` и `LIMIT`.
* Для математических операций поддержка `GROUP BY`, `ORDER BY` и других операций над функциями отсутствует.
* К `FUNNEL` можно применить не более 10 условий.
* Некоторые поля, такие как `duration`, всегда возвращают целые значения вместо десятичных при выполнении математических операций, например деления, поскольку эти поля хранятся и отображаются как целые числа. Например, `SELECT duration FROM usersession` возвращает длительность `4800`, а `SELECT duration/1000 FROM usersession` возвращает длительность `5`.
