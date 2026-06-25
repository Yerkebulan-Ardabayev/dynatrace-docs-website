---
title: Пользовательские запросы, сегментация и агрегация данных сессий
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data
scraped: 2026-05-12T11:31:21.306423
---

# Пользовательские запросы, сегментация и агрегация данных сессий

# Пользовательские запросы, сегментация и агрегация данных сессий

* How-to guide
* 37-min read
* Updated on Apr 23, 2024

Dynatrace фиксирует подробные [данные о сессиях пользователей](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте о сегментации и атрибутах фильтрации сессий пользователей.") при каждом взаимодействии пользователя с вашим мониторируемым приложением. Эти данные включают все действия пользователя и высокоуровневые данные о производительности. Используя Dynatrace API или User Sessions Query Language (USQL), вы можете легко выполнять мощные запросы, сегментацию и агрегацию собранных данных.

User Sessions Query Language не является SQL, а Dynatrace не хранит данные сессий пользователей в реляционной базе данных. USQL — это специфичный для Dynatrace язык запросов, хотя он опирается на некоторые концепции SQL, а синтаксис схож, что упрощает начало работы.

Выберите предпочтительный подход:

**Запросы через интерфейс Dynatrace**

1. Перейдите в **Query User Sessions**.
2. Введите запрос и нажмите **Run query**.

### Выбор временного интервала в USQL

С помощью выбора временного интервала данные сессий пользователей можно фильтровать по выбранному периоду анализа. Выберите новый временной интервал.

#### Управление выбором временного интервала

Глобальный селектор временного интервала служит фильтром времени, который в большинстве случаев позволяет выбрать конкретный период анализа, сохраняющийся на всех страницах и представлениях при навигации.

* Вкладка **Presets** содержит все стандартные временные интервалы. Выберите один, чтобы переключить временной интервал.
* Вкладка **Custom** отображает календарь. Нажмите на день начала, нажмите на день окончания, затем нажмите **Apply** для выбора этого диапазона дней.

  + Выбранные интервалы в календаре заканчиваются в начале следующего дня (время `00:00`). Например, если выбрать 3 сентября по 4 сентября, временной интервал начнётся 3 сентября в `00:00` и закончится **5** сентября в `00:00`, чтобы не пропустить последнюю минуту диапазона. Отображаемое время можно редактировать.
* Вкладка **Recent** отображает недавно использованные временные интервалы. Выберите один для возврата к нему.
* Кнопки **<** и **>** сдвигают временной диапазон вперёд или назад. Шаг равен длине исходного диапазона. Например, если текущий диапазон `Last 2 hours`, нажатие **<** сдвинет диапазон на 2 часа назад.
* Наведите указатель мыши на временной интервал, чтобы увидеть время начала, продолжительность и время окончания.

#### Выражения для выбора временного интервала

Если выбрать текущий временной интервал в строке меню, отображается редактируемое выражение.

* Слева направо выражение содержит время начала, оператор `to` и время окончания.
* Если явное время окончания не указано, `to` и `now` подразумеваются. Например, `-2h` эквивалентно `-2h to now`.
* Поддерживаемые единицы: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (также допускаются полные слова, такие как `minutes` и `quarter`)

| **Пример выражения** | **Значение** |
| --- | --- |
| `today` | От начала сегодняшнего дня до начала завтрашнего. |
| `yesterday` | От начала вчерашнего дня до начала сегодняшнего. Аналогично `-1d/d to today`. |
| `yesterday to now` | От начала вчерашнего дня до текущего момента. |
| `previous week` | Предыдущие семь полных дней. |
| `this year` | Текущий календарный год, с 1 января по 1 января следующего года. |
| `last 6 weeks` | Последние 42 дня (6 недель × 7 дней), заканчивающихся сейчас. Эквивалентно `-6w to now`. |
| `-2h` | От 2 часов назад до текущего момента (`now` подразумевается). Эквивалентно `Last 2 hours` и `-2h to now`. |
| `-4d to -1h30m` | От 4 дней назад до 1,5 часа назад. |
| `-1w` | Последние 7 дней (168 часов). Эквивалентно `-7d` и `-168h`. |
| `-1w/w` | От начала предыдущей календарной недели до текущего момента. `/` вместе с единицей означает округление вниз до начала указанной единицы времени. |
| `-1w/w + 8h` | От начала прошлой недели плюс 8 часов (8:00 утра понедельника). |
| `-1d/d+9h00m to -1d/d+17h00m` | Рабочие часы вчера, с 09:00 до 17:00. |
| `2020-08-16 21:28 to 2020-08-19 10:02` | Абсолютный диапазон с датами и временем в формате `YYYY-MM-DD hh:mm`. |
| `1598545932346 to 1598837052346` | Временные метки Unix epoch в миллисекундах. |

### Автодополнение в USQL

Автодополнение доступно для операторов запроса на основе введённого текста. Автодополнение контекстно-зависимое и работает с учётом текущего положения курсора. Список полей содержит только допустимые поля или функции для выбранной таблицы. Значения полей предлагаются только для полей перечислимого типа.

**Dynatrace Environment API**

Выполнять вызовы API можно через предпочтительный клиент. Соответствующую документацию API см. в [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает API языка запросов сессий пользователей Dynatrace.").

Для выполнения этих вызовов необходимо разрешение **User sessions** (`DTAQLAccess`), назначенное токену API.

### Временные интервалы в Environment API

Данные сессий пользователей всегда следует запрашивать с указанием временного интервала. Временной интервал обычно не является частью самого запроса, а передаётся в отдельных параметрах вызова API.

Тем не менее можно использовать поля времени, такие как `starttime` и `endtime`, для выбора временного интервала. Эти поля также можно использовать в функциях, например `HOUR(starttime)`.

## Ключевые слова и функции

Следующие ключевые слова определены для доступа к данным сессий пользователей:

`AND`, `AS`, `ASC`, `BETWEEN`, `BY`, `DESC`, `DISTINCT`, `FALSE`, `FROM`, `GROUP`, `IN`, `IS`, `JSON`, `LIMIT`, `NOT`, `NULL`, `OR`, `ORDER`, `SELECT`, `STARTSWITH`, `TRUE`, `WHERE`, `LIKE`, `FILTER`

Следующие функции определены для доступа к данным сессий пользователей:

`SUM`, `MAX`, `MIN`, `AVG`, `MEDIAN`, `COUNT`, `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `DATETIME`, `TOP`, `PERCENTILE`, `KEYS`

Ключевые слова, функции и имена столбцов нечувствительны к регистру. Сравнение строк в условиях `WHERE` чувствительно к регистру.

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

Выбирает один или несколько столбцов из указанной таблицы данных или выполняет функции агрегации.

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

Позволяет использовать предопределённый формат воронки для запроса. Может использоваться для отображения потока определённых действий пользователя. Также может сочетаться с пользовательскими свойствами сессии и другими условиями.

Изменяет синтаксис запроса следующим образом:

```
SELECT FUNNEL (<condition> AS <alias>, <condition>, ...) FROM <table> WHERE <condition>
```

* Для запросов `FUNNEL` не используйте функции `SELECT *` или ключевые слова, такие как `JSON`.
* В настоящее время операторы `GROUP BY`, `ORDER BY` и `LIMIT` не допускаются в воронках.
* `FUNNEL` не поддерживает упорядочивание. Нет гарантии, что `useraction1` произошло раньше `useraction2`.

Пример 1. Вместо трёх отдельных запросов:

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

Пример 2. Для получения числа пользователей, успешно забронировавших поездку:

```
SELECT FUNNEL (useraction.name="login", useraction.name = "searchJourney", useraction.name = "bookJourney")

FROM usersession
```

#### FROM `<table>`

Можно указать только одну таблицу. Таблицы для данных сессий пользователей:

* `usersession` содержит информацию о [сессиях пользователей](/managed/observe/digital-experience/rum-concepts/user-session "Узнайте, как определяется сессия пользователя.").
* `useraction` хранит данные о [действиях пользователя](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое действия пользователя.").
* `userevent` предоставляет информацию о [событиях пользователя](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-events "Узнайте о событиях пользователей и ошибках."), таких как смена страниц или rage events.
* `usererror` содержит дополнительные данные о [событиях ошибок](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error-events "Узнайте о событиях пользователей и ошибках."), то есть об ошибках и сбоях.

Пример

```
SELECT country, city, browserfamily FROM usersession

SELECT name, starttime, endtime, duration FROM useraction ORDER BY duration DESC
```

#### WHERE `<condition>`

Вы можете комбинировать несколько условий с помощью булевой логики и скобок.

```
condition: (condition AND condition) | (condition OR condition) | field IN(...) |
field IS <value> | field IS NULL | field = <value> | field > <value> | field < <value> |
field <> <value> | field IS NOT <value> | field BETWEEN <value> AND <value> | ...
```

Правая часть условий всегда может содержать только значение, а не поле.

Примеры

```
SELECT country, city, browserfamily FROM usersession WHERE country = 'Albania' AND screenWidth > 1000

SELECT TOP(country, 20), TOP(city, 20), TOP(duration, 10), AVG(duration) AS average

FROM usersession

WHERE duration BETWEEN 1000 AND 2000

GROUP BY TOP(country, 20), TOP(city, 20), TOP(duration, 10)
```

#### GROUP BY `<grouping>`

При агрегации полей необходимо указать соответствующие ключевые слова `GROUP BY`.

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

Позволяет ограничить количество возвращаемых результатов. Если `LIMIT` не используется, по умолчанию возвращается 50 результатов. Также позволяет увеличить количество результатов при необходимости.

Пример

```
SELECT city, starttime FROM usersession ORDER BY starttime DESC LIMIT 10
```

#### ORDER BY `<ordering>`

Позволяет упорядочить результаты по столбцам в порядке возрастания или убывания. По умолчанию порядок возрастающий.

```
ordering: <column> ASC | <column> DESC | <column>, ...
```

Пример 1

```
SELECT useraction.name, starttime FROM usersession ORDER BY starttime DESC
```

Пример 2. Упорядочивание по счётчикам с ключевым словом `DISTINCT`:

```
SELECT DISTINCT city, COUNT(*) FROM usersession ORDER BY COUNT(*) DESC
```

Пример 3. Упорядочивание по функциям через псевдоним:

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

Позволяет сравнивать данные с выражением с использованием символов подстановки:

* `%` или `*`: совпадение с любой строкой из 0 и более символов
* `?`: совпадение с любым одним символом

Строковые значения чувствительны к регистру.

Экранирование символов подстановки

Для экранирования символа подстановки добавьте обратную косую черту `\` перед ним. Например, `\%`, `\*` и `\?` трактуются как стандартные строковые литералы.

| Запись | Интерпретация | Совпадения |
| --- | --- | --- |
| `\%` | `%` | `%` |
| `\*` | `*` | `*` |
| `\?` | `?` | `?` |
| `\\` | `\` | `\` |
| `\\%` | `\` и любая строка | `\abc`, `\123ABC`, `\` и т.д. |
| `\\*` | `\` и любая строка | `\abc`, `\123ABC`, `\` и т.д. |
| `\\?` | `\` и любой один символ | `\a`, `\1`, `\A` и т.д. |

Запросы с 11 и более условиями `LIKE` с нетрейлинговыми символами подстановки отклоняются.

#### FILTER

Позволяет фильтровать функции с числовыми значениями, отображая только определённые результаты из агрегаций.

Пример

```
SELECT useraction.application,

AVG(usersession.doubleProperties.bookings)

FILTER > 1500

FROM usersession

WHERE usersession.doubleProperties.bookings IS NOT NULL

GROUP BY useraction.application
```

`WHERE` и `FILTER` не являются взаимозаменяемыми: `WHERE` работает только с абсолютными значениями, а `FILTER` работает и с агрегированными значениями.

### Часто используемые функции

#### MIN(field)

Запрашивает минимальное значение числового поля или поля даты.

#### MAX(field)

Запрашивает максимальное значение числового поля или поля даты.

#### AVG(field)

Запрашивает среднее значение числового поля или поля даты. Может быть `NaN`, если поле всегда имеет значение `null`.

#### MEDIAN(field)

Запрашивает медианное значение числового поля или поля даты.

Пример для MIN/MAX/AVG/MEDIAN

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

Подсчитывает количество строк, соответствующих условию.

* `COUNT(*)`: подсчёт количества совпадающих элементов.
* `COUNT(<field>)`: подсчёт элементов, где `<field>` не равно null.
* `COUNT(DISTINCT <field>)`: подсчёт различных значений `<field>`.

Результаты `COUNT(DISTINCT <field>)` являются приближёнными для предотвращения высокого потребления памяти. Для полей с высокой кардинальностью результаты могут быть ещё более приближёнными.

Поля с высокой кардинальностью:

| Таблица | Поля |
| --- | --- |
| `usersession` | `ip`, `userSessionId`, `internalUserId`, `userId` |

Dynatrace отклоняет запросы с `COUNT(DISTINCT <field>)` для полей с чрезвычайно высокой кардинальностью, например полей `dateTime`, таких как `usersession.startTime`, `usersession.endTime`.

Пример

```
SELECT country, COUNT(*), COUNT(city), COUNT(DISTINCT city)

FROM usersession

GROUP BY country
```

#### TOP(field, n)

Возвращает первые `<n>` результатов из поля. По умолчанию `n = 1`.

Пример

```
SELECT TOP(name, 20), SUM(duration)

FROM useraction

GROUP BY name
```

#### YEAR/MONTH/DAY/HOUR/MINUTE(datefield)

Возвращает указанный элемент, извлечённый из поля даты:

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

Форматирует выбранное поле даты с заданной строкой формата. Формат по умолчанию: `yyyy-MM-dd HH:mm`.

Допустимые символы в строке формата: `y` (год), `M` (месяц), `d` (день), `H` (час 0-23), `h` (час 1-12), `m` (минута), `s` (секунда), `E` (день недели Mon-Sun).

Примеры

```
SELECT DATETIME(starttime, 'yyyy-MM') FROM usersession

SELECT DISTINCT DATETIME(starttime, 'HH:mm', '5m'), COUNT(*) FROM usersession

SELECT application, DATETIME(MAX(starttime)) AS LastUsedTime FROM useraction GROUP BY application

SELECT DATETIME(starttime, "HH") AS hourOfDay, COUNT(*) FROM usersession GROUP BY hourOfDay

SELECT application, DATETIME(starttime, "E") AS daysOfWeek FROM useraction GROUP BY application

SELECT DATETIME(CONDITION(MAX(startTime), WHERE name = "index.jsp")) FROM useraction
```

#### CONDITION(function, condition)

Позволяет комбинировать несколько функций с различными условиями.

Допустимые функции: `MIN()`, `MAX()`, `AVG()`, `SUM()`, `PERCENTILE()`, `MEDIAN()`, `COUNT()`.

Также можно использовать условие `FILTER` для функций с числовыми значениями.

Примеры

```
SELECT CONDITION(COUNT(usersessionId), WHERE userActionCount > 2 AND useraction.name = "search.jsp") FROM usersession

SELECT CONDITION(SUM(usersession.duration), WHERE name = "index.jsp") AS c1, CONDITION(SUM(usersession.duration), WHERE name = "search.jsp") AS c2, CONDITION(SUM(usersession.duration), WHERE name IS NOT "index.jsp" AND name IS NOT "search.jsp") AS c3 FROM useraction WHERE (duration > 1000 OR usersession.userActionCount > 4)

SELECT CONDITION(SUM(usersession.duration), WHERE name = "index.jsp") AS c1 FROM useraction WHERE (duration > 1000 OR usersession.userActionCount > 4) ORDER BY c1
```

#### PERCENTILE

Представляет значение, ниже которого находится определённый процент точек данных. Полезен для обнаружения скорости приложения для пользователей, получающих наибольшее время отклика.

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

Возвращает ключи [свойств действий пользователя или сессий пользователя](/managed/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "Свойства действий и сессий — пары ключ-значение, предоставляющие дополнительную видимость и более глубокий анализ опыта конечных пользователей.") в соответствии с типом данных свойства, указанным в аргументе.

| KEYS(customProperty) | Таблица | Свойства действий | Свойства сессий |
| --- | --- | --- | --- |
| `KEYS(<dataType>Properties)` | `useraction` | Применимо |  |
| `KEYS(<dataType>Properties)` | `usersession` |  | Применимо |
| `KEYS(useraction.<dataType>Properties)` | `useraction` | Применимо |  |
| `KEYS(useraction.<dataType>Properties)` | `usersession` | Применимо |  |
| `KEYS(usersession.<dataType>Properties)` | `useraction` |  | Применимо |
| `KEYS(usersession.<dataType>Properties)` | `usersession` |  | Применимо |

`<dataType>` может принимать значения: `string`, `long`, `double`, `date`.

Пример 1

```
SELECT KEYS(stringProperties) FROM useraction WHERE application = "easyTravel demo application"

SELECT KEYS(useraction.longProperties) FROM usersession WHERE applicationType="WEB_APPLICATION" ORDER BY keys(useraction.longProperties)

SELECT KEYS(usersession.stringProperties) FROM useraction WHERE usersession.city ="Berlin"
```

Пример 2 (с использованием `DISTINCT`)

```
SELECT DISTINCT KEYS(stringProperties) FROM useraction WHERE useraction.application = "easyTravel demo application" ORDER BY keys(stringProperties)

SELECT DISTINCT KEYS(doubleProperties) FROM usersession
```

## Математические операции

Поддерживаются следующие операции:

* операции над числами;
* операции над числовыми полями и полями dateTime;
* операции над определёнными функциями, такими как `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`;
* операции над числовыми значениями для отображения в разных единицах измерения.

### Синтаксис

`Number/NumericField/DateTimeField/Function OPERATOR Number/NumericField/DateTimeField/Function`

Функции: `YEAR`, `MONTH`, `DAY`, `HOUR` или `MINUTE`
Операторы: `+`, `-`, `*`, `/`, `%` или `MOD`

Пример

```
SELECT 7 + 80 * 100, duration + startTime, MONTH(startTime) - 1

FROM usersession
```

## Условия

Все условия должны начинаться с идентификатора, такого как имя поля, и сравниваться со значением. Два поля не могут сравниваться друг с другом.

Текст в кавычках всегда чувствителен к регистру.

### Базовые операторы

Базовые операторы сравнения: `=`, `!=`, `<>`, `<`, `>`, `<=`, `>=`, `IS` и `IS NOT`.

Для проверки наличия значения в поле сравните поле с `NULL`.

Пример

```
SELECT userId FROM usersession WHERE userActionCount > 3
```

### Диапазоны

Диапазоны обрабатываются ключевыми словами `BETWEEN` или `NOT BETWEEN`.

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

Условие `"STARTSWITH"` проверяет, начинается ли строка или поле перечисления с указанного текста.

Пример

```
SELECT city FROM usersession WHERE userId STARTSWITH "dynatrace"
```

### Значения datetime

При работе с полем datetime поддерживаются следующие форматы:

| Формат | Описание | Пример |
| --- | --- | --- |
|  | Временная метка Unix в миллисекундах | `1514152800000` |
| `yyyy-MM-dd'T'HH:mm:ssZ` | ISO datetime с часовым поясом | `2017-12-24T21:00:00+01:00` |
| `yyyy-MM-dd HH:mm:ss` | Дата с необязательным временем | `2017-12-24 21:00` |
| `yyyy/MM/dd HH:mm:ss` | Дата с необязательным временем | `2017/12/24 21` |
| `MM/dd/yyyy HH:mm:ss` | Дата с необязательным временем | `12/24/2017` |
| `dd.MM.yyyy HH:mm:ss` | Дата с необязательным временем | `24.12.2017 21:00:00` |

Если время не указано, предполагается `00:00:00`.

Пример

```
SELECT starttime FROM usersession WHERE starttime > "8.8.2018 8:00"
```

### Оптимизация условий

#### IN

Когда запрос содержит несколько условий равенства для одного поля через `OR`, используйте функцию `IN`, так как она эффективнее.

До:

```
SELECT COUNT(*) FROM userevent

WHERE pageReferrer = "/some/page/referrer/1"

OR pageReferrer = "/some/page/referrer/2"

OR pageReferrer = "/some/page/referrer/3"
```

После:

```
SELECT COUNT(*) FROM userevent

WHERE pageReferrer IN ("/some/page/referrer/1",

"/some/page/referrer/2",

"/some/page/referrer/3")
```

#### NOT IN

Вместо нескольких операторов `NOT`, `<>` или `!=` используйте оператор `NOT IN`.

До:

```
SELECT useraction.name, usersession.userId

FROM useraction

WHERE name = "loading of page /"

AND usersession.userId IS NOT NULL

AND usersession.userId <> "Speed Travel Agency"

AND usersession.userId <> "some user"
```

После:

```
SELECT useraction.name, usersession.userId

FROM useraction

WHERE name = "loading of page /"

AND usersession.userId IS NOT NULL

AND NOT usersession.userId IN ("Speed Travel Agency",

"some user")
```

## Расширенные конструкции синтаксиса

### Запрос диапазонов IP

Поле IP можно запрашивать для диапазонов адресов. Работает как `BETWEEN ip > <нижняя граница> AND ip < <верхняя граница>`, так и `BETWEEN <нижняя граница> AND <верхняя граница>`.

Пример

```
SELECT * FROM usersession WHERE ip > '211.44.94.0' AND ip < '212.113.5.0'

SELECT * FROM usersession WHERE ip BETWEEN '211.44.94.0' AND '212.113.5.0'
```

### Запрос с выбором временного интервала

Вы можете использовать следующие ключевые слова для выбора времени начала и окончания, определённых в выборе временного интервала:

* `TIME_FRAME_START`
* `TIME_FRAME_END`

Пример

```
SELECT * FROM usersession WHERE startTime >= $TIME_FRAME_START AND endTime < $TIME_FRAME_END
```

Выборы временного интервала можно использовать для ограничения временного интервала в запросах, выполняемых на вторичных таблицах (`useraction`).

Пример

```
SELECT name, duration FROM useraction

WHERE startTime BETWEEN $TIME_FRAME_START and $TIME_FRAME_END
```

### Запрос относительного временного интервала

Вы можете выбрать временной интервал относительно времени выполнения запроса. Текущее время выражается переменной `$NOW`.

`$NOW [+/-] DURATION("[number]TIME_UNIT")`

Поддерживаемые единицы времени: `y` (год), `q` (квартал), `M` (месяц), `d` (день), `w` (неделя), `h` (час), `m` (минута), `s` (секунда).

Пример

```
SELECT * FROM usersession WHERE startTime >= $NOW - DURATION("1q") AND endTime <= $NOW

SELECT * FROM useraction WHERE startTime BETWEEN $NOW - DURATION("2h") AND $NOW

SELECT * FROM useraction WHERE usersession.startTime >= $TIME_FRAME_START - DURATION("2h") AND $NOW - DURATION("1h")
```

### Вторичные таблицы для `usersession`, `useraction`, `userevent` и `usererror`

При использовании `SELECT` с `usersession`, `useraction`, `userevent` или `usererror` столбцы из другой таблицы можно включить в результаты, добавив имя таблицы в качестве префикса к именам столбцов.

Пример 1

```
SELECT city, useraction.name FROM usersession

SELECT usersession.city, name FROM useraction
```

Вторичные таблицы `userevent` и `usererror` используются аналогично:

```
SELECT usersession.country, name, page FROM userevent

SELECT usersession.country, name, type FROM usererror

SELECT country, userevent.name, usererror.name FROM usersession
```

При запросе из первичной таблицы `usersession` можно комбинировать поля из других вторичных таблиц:

Пример 2

```
SELECT city, useraction.name, userevent.page, usererror.type FROM usersession

SELECT city, usererror.name, userevent.page, useraction.duration FROM usersession WHERE usererror.name IS NOT NULL
```

Пример 3. Все сессии пользователей, содержащие событие или действие из одного приложения:

```
SELECT * FROM usersession

WHERE userevent.application = "a" OR useraction.application="a"
```

При запросе из вторичной таблицы можно использовать только поля из первичной таблицы `usersession`; нельзя использовать поля из других вторичных таблиц.

Пример 4. Корректные запросы:

```
SELECT usersession.userId, name, duration FROM useraction

SELECT usersession.userId, name, type FROM usererror
```

Применяемые условия различаются по смыслу в зависимости от таблицы. Запрос к `usersession` означает, что сессия должна содержать действие с именем `"a"` и действие с именем `"b"`. Запрос к `useraction` вернёт пустой результат, так как одно действие не может одновременно иметь два разных имени.

Если нужно выбрать данные для конкретного действия, соответствующего нескольким критериям, выполните запрос к таблице `useraction`:

```
SELECT usersession.*, * FROM useraction

WHERE useraction.name = "a" AND useraction.duration > 1000
```

### Фильтрация с использованием полей вторичной таблицы

**Пример 1**

```
SELECT useraction.name FROM usersession WHERE useraction.name="abc"
```

Этот запрос возвращает список всех сессий, содержащих хотя бы одно действие с именем `abc`. Результат содержит все действия для каждой сессии, так как запрос выполняется на уровне `usersession`.

**Пример 2**

```
SELECT name FROM useraction WHERE name="abc"
```

Этот запрос извлекает список только тех действий пользователя, которые называются `abc`.

### SELECT \* FROM table

Пример

```
SELECT * FROM usersession

SELECT useraction.* FROM usersession

SELECT city, useraction.* FROM usersession

SELECT *, useraction.* FROM usersession
```

Звёздочка `*` сама по себе выбирает столбцы из основной таблицы, но не из вторичной. Поля `useraction` не включаются в `SELECT * FROM usersession`, если только не указать `useraction.*`.

### Экспорт в JSON

Ключевое слово `JSON` добавляет дополнительный столбец с данными о запрошенной записи (сессии, действии, событии или ошибке) в формате JSON.

Пример 1. Запрос возвращает совпадающие сессии в JSON в дополнительном столбце:

```
SELECT usersessionId, browserFamily, useraction.name, useraction.duration, JSON

FROM usersession LIMIT 5
```

Пример 2. Запрос возвращает совпадающие действия в JSON без данных из `usersession`:

```
SELECT name, duration, JSON

FROM useraction LIMIT 5
```

### Экранирование строк

Строковые литералы могут быть заключены в одинарные или двойные кавычки. Для использования того же знака кавычек внутри строки просто продублируйте его.

Пример

```
SELECT * FROM usersession WHERE userId = "some 'custom' name for ""my user"""

SELECT * FROM usersession WHERE userId = 'some ''custom'' name for "my user"'
```

### Построение воронок

Построение воронок позволяет отслеживать шаги в вашем цифровом сервисе и исследовать проблемные зоны. В сочетании с Session Replay эта функция позволяет видеть, на каком этапе пользователь испытывает затруднения.

Пример

```
SELECT FUNNEL(

useraction.name = "AppStart (easyTravel)" AS "Open easytravel",

useraction.name = "searchJourney" AS "Search journey",

useraction.name = "bookJourney" AS "Book journey",

useraction.matchingConversionGoals = "Payment" OR useraction.matchingConversionGoals = "booking-finished" AS "Booked")

FROM usersession
```

Пример с фильтрацией по свойству сессии:

```
SELECT FUNNEL(

useraction.name = "AppStart (easyTravel)" AS "Open easytravel",

useraction.name = "searchJourney" AS "Search journey",

useraction.name = "bookJourney" AS "Book journey",

useraction.matchingConversionGoals = "Payment" OR useraction.matchingConversionGoals = "booking-finished" AS "Booked")

FROM usersession

WHERE stringProperties.memberstatus="GOLD"
```

`FUNNEL` не поддерживает упорядочивание.

## Доступные таблицы и поля данных сессий пользователей

Доступны следующие таблицы:

* `usersession` — информация о [сессиях пользователей](/managed/observe/digital-experience/rum-concepts/user-session "Узнайте, как определяется сессия пользователя.").
* `useraction` — данные о [действиях пользователя](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое действия пользователя.").
* `userevent` — информация о [событиях пользователя](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-events "Узнайте о событиях пользователей и ошибках.").
* `usererror` — дополнительные данные о [событиях ошибок](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error-events "Узнайте о событиях пользователей и ошибках.").

Поля описаны в [User sessions API — структура сессии пользователя](/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure "Узнайте о структуре сессии пользователя в API Dynatrace User Session Query language.").

## Выполнение USQL-запросов для пользовательских отчётов

REST-интерфейс позволяет получать результаты пользовательских запросов. Для этого необходимо создать уникальный [токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с привилегией **User session query language**. Доступны следующие конечные точки:

`/table`: Возвращает данные в виде плоской таблицы.

`/tree`: Возвращает данные в виде полного иерархического дерева на основе входных данных.

Следующие параметры запроса доступны:

`query`: должен быть закодирован при включении в URL.
`startTimestamp/endTimestamp`: позволяет определять временные точки, передаваемые как количество миллисекунд с эпохи Unix. По умолчанию — последние два часа.

Пример

```
curl --location --insecure -H "Content-Type: application/json" -H "Authorization: Api-Token _token_" \

-XGET "https://{your-environment-id}.live.dynatrace.com/api/v1/userSessionQueryLanguage/table?query=select%20city,count(*)%20from%20usersession%20group%20by%20city"
```

Результат:

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

Подробнее см. [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнайте, что предлагает API языка запросов сессий пользователей Dynatrace.").

## Преобразование запросов в пользовательские метрики USQL

Вы можете преобразовывать некоторые запросы в пользовательские метрики USQL для [веб](/managed/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions "Узнайте, как настраивать и использовать пользовательские метрики USQL для веб-приложений."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps "Узнайте, как настраивать и использовать пользовательские метрики USQL для мобильных приложений.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps "Узнайте, как настраивать и использовать пользовательские метрики USQL для пользовательских приложений.").

Пользовательские метрики USQL доступны как пользовательские метрики сессий (USCM) и пользовательские метрики действий (UACM). UACM поддерживается начиная с Dynatrace версии 1.260.

1. Перейдите в **Query User Sessions**.
2. Введите запрос и нажмите **Run query**.
3. Выберите **Create custom metric**.
4. Введите имя метрики и проверьте предложенные настройки.

## Ограничения

* Dynatrace хранит данные Real User Monitoring в течение ограниченного периода времени. Подробнее см. [Периоды хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Проверьте сроки хранения для различных типов данных.").
* По умолчанию возвращается 50 результатов, максимум через `LIMIT` — 5000.
* Максимальное количество возможных результатов в бакетах — 100 000. По умолчанию — 10 000.
* Объединения (joins) не допускаются.
* В одном `SELECT` допускается только одна таблица.
* Поиск строковых значений с использованием регулярных выражений не поддерживается.
* Два разных поля не могут сравниваться. Например, `WHERE field1 = field2` не работает.
* Условия `WHERE` работают только с полями, а не с `WHERE true` или `WHERE COUNT(*) > 3`.
* Можно запрашивать только завершённые сессии пользователей. Текущие (live) сессии не учитываются.
* Упорядочивание частично поддерживается. Например, упорядочивание по математическим операциям не поддерживается.
* При обширных временных интервалах и высокой нагрузке данные могут быть экстраполированы из выборки.
* Функции не допускаются в предложении `GROUP BY`.
* `FUNNEL` нельзя использовать с функциями `SELECT *`, ключевыми словами `JSON`, а также операторами `GROUP BY`, `ORDER` и `LIMIT`.
* Для математических операций поддержка `GROUP BY`, `ORDER BY` и других операций с функциями недоступна.
* Максимальное количество условий в `FUNNEL` — 10.
* Некоторые поля, такие как `duration`, всегда возвращают целые значения вместо десятичных при выполнении математических операций.