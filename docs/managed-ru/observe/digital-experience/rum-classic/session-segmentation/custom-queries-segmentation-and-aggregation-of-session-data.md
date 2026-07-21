---
title: Пользовательские запросы, сегментация и агрегация данных сессий в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data
---

# Пользовательские запросы, сегментация и агрегация данных сессий в RUM Classic

# Пользовательские запросы, сегментация и агрегация данных сессий в RUM Classic

* Практическое руководство
* Время чтения: 37 мин
* Обновлено 23 апреля 2024 г.

Dynatrace фиксирует подробные [данные пользовательских сессий](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Узнать о сегментации и атрибутах фильтрации пользовательских сессий.") каждый раз, когда пользователь взаимодействует с отслеживаемым приложением. Эти данные включают все действия пользователя и данные о производительности на высоком уровне. С помощью Dynatrace API или языка запросов пользовательских сессий Dynatrace (USQL) можно легко выполнять мощные запросы, сегментацию и агрегацию над этими собранными данными. Чтобы помочь в этом, данный раздел содержит подробные сведения о ключевых словах и функциях, синтаксисе, работе с таблицами Real User Monitoring, автоматизированных запросах и многом другом.

Язык запросов пользовательских сессий, это не [SQL﻿](https://en.wikipedia.org/wiki/SQL), и Dynatrace не хранит данные пользовательских сессий в реляционной базе данных. Язык запросов пользовательских сессий, это специфический для Dynatrace язык запросов, хотя он и опирается на некоторые концепции SQL, а синтаксис похож, что упрощает начало работы.

Выберите предпочитаемый подход:

Запросы пользовательских сессий через веб-интерфейс Dynatrace

1. Перейдите в **Query User Sessions**.
2. Введите запрос и выберите **Run query**.

### Селектор временного диапазона с USQL

С помощью селектора временного диапазона данные пользовательских сессий можно фильтровать на основе выбранного периода анализа. Выберите новый временной диапазон.

![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

Селектор временного диапазона: строка меню

#### Элементы управления селектора временного диапазона

Глобальный селектор временного диапазона служит фильтром по времени, который в большинстве случаев позволяет выбрать конкретный период анализа, сохраняющийся на всех страницах и представлениях продукта в ходе анализа.

![Timeframe selector: presets](https://dt-cdn.net/images/timeframe-selector-basic-355-f0a835da1e.png)

Селектор временного диапазона: пресеты

* На вкладке **Presets** перечислены все доступные стандартные временные диапазоны. Выберите один из них, чтобы изменить временной диапазон на этот пресет.
* На вкладке **Custom** отображается календарь. Нажмите на день начала, затем на день окончания и выберите **Apply**, чтобы задать этот диапазон дней в качестве временного диапазона.

  + Выбранные интервалы календаря устанавливаются так, чтобы заканчиваться в начале следующего дня (время устанавливается на `00:00`). Например, если выбрать в календаре период с 3 по 4 сентября, временной диапазон начинается 3 сентября в `00:00` и заканчивается **5** сентября в `00:00`, чтобы не пропустить последнюю минуту диапазона. Отображаемое время можно редактировать.
* На вкладке **Recent** отображаются недавно использованные временные диапазоны. Выберите один из них, чтобы вернуться к этому диапазону.
* Элементы управления **<** и **>** сдвигают временной диапазон вперёд или назад во времени. Шаг сдвига равен длине исходного временного диапазона. Например, если текущий диапазон, это `Last 2 hours` (двухчасовой диапазон, заканчивающийся сейчас), выбор **<** сдвигает диапазон на два часа назад, до `-4h to -2h` (двухчасовой диапазон, закончившийся два часа назад).
* Наведите курсор на временной диапазон, чтобы увидеть время начала, длительность и время окончания.

  ![Timeframe selector: hover](https://dt-cdn.net/images/timeframe-selector-hover-168-cfb13dc777.png)

  Селектор временного диапазона: наведение курсора

#### Выражения селектора временного диапазона

При выборе текущего временного диапазона в строке меню отображается редактируемое выражение временного диапазона.

* При чтении слева направо выражение временного диапазона состоит из времени начала, оператора `to` и времени окончания.
* Если явное время окончания отсутствует, подразумеваются `to` и `now`. Например, `-2h` равнозначно `-2h to now`.
* Поддерживаемые единицы измерения: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (можно также использовать полные слова, например `minutes` и `quarter`)

| **Примеры выражений временного диапазона** | **Значение** |
| --- | --- |
| `today` | С начала сегодняшнего дня до начала завтрашнего. |
| `yesterday` | С начала вчерашнего дня до начала сегодняшнего. Аналогично `-1d/d to today`. |
| `yesterday to now` | С начала вчерашнего дня до текущего момента сегодня. |
| `previous week` | Предыдущие семь полных дней. Если сегодня понедельник, диапазон охватывает предыдущий понедельник по предыдущее воскресенье (вчера). |
| `this year` | Текущий календарный год, с 1 января этого года в `00:00` по 1 января следующего года в `00:00`. |
| `last 6 weeks` | Последние 42 дня (6 недель \* 7 дней), заканчивающиеся сейчас. Эквивалентно `-6w to now`. |
| `-2h` | От 2 часов (120 минут) назад до текущего момента (`now` подразумевается). Эквивалентно `Last 2 hours` и `-2h to now`. |
| `-4d to -1h30m` | От 4 дней (96 часов) назад до 1,5 часа назад. |
| `-1w` | Последние 7 дней (168 часов), от этого времени 7 дней назад до текущего момента (`now`). Эквивалентно `-7d` и `-168h`. |
| `-1w/w` | От начала предыдущей календарной недели до текущего момента (now).  * Если использовать `-1w/w` в пятницу днём в 15:00, получится диапазон в 11 дней 15 часов, начинающийся с начала понедельника предыдущей недели, поскольку `/w` округляет вниз до начала недели. * Если использовать `-1w` без `/w` в пятницу днём в 15:00, время начала будет ровно на 7 дней (168 часов) раньше: предыдущая пятница в 15:00.  В общем случае `/`, используемый в сочетании с единицей измерения (например, `/d`, `/w`, `/M` и `/y`), означает округление даты или времени вниз до начала указанной единицы времени. Например, `-3d` означает ровно 72 часа назад, тогда как `-3d/d` означает три дня назад, округлённые вниз до ближайшего дня (начиная с `00:00`, начала дня). Используйте `now/d`, чтобы обозначить начало сегодняшнего дня. |
| `-1w/w + 8h` | Начиная с начала прошлой недели плюс 8 часов (8:00 утра понедельника).  * Обратите внимание, что операторы `+` и `-` можно использовать с единицами измерения, временными метками и `now`. |
| `-1d/d+9h00m to -1d/d+17h00m` | Рабочие часы вчерашнего дня, с 09:00 до 17:00 (с 9 утра до 5 вечера). |
| `2020-08-16 21:28 to 2020-08-19 10:02` | Абсолютный диапазон, состоящий из абсолютных дат и времени начала и окончания в формате `YYYY-MM-DD hh:mm`.  * Если указана дата, но время опущено (например, просто `2020-08-16`), время принимается за начало дня (`00:00`) * Если указано время, но дата опущена (например, просто `21:28`), датой считается сегодняшний день |
| `1598545932346 to 1598837052346` | Временные метки Unix epoch в миллисекундах. |

### Автозавершение с USQL

Автозавершение доступно для операторов запроса на основе введённого на данный момент текста. Автозавершение чувствительно к контексту и основывается на текущем контексте положения курсора. Оно интеллектуально предугадывает, какой текст может понадобиться ввести дальше.

Информация об автозавершении, возвращаемая API, содержит список предложений, где наиболее вероятные значения отсортированы в начале списка, вместе с необходимой корректировкой текста запроса и итоговой позицией курсора после этой корректировки. Это позволяет разместить курсор в более удобной позиции после добавления текста, например внутри скобок при выборе функции.

Список полей содержит только допустимые поля или функции для выбранной таблицы, а его контекстная чувствительность показывает только числовые поля, когда курсор находится внутри вызова функции, работающей только с числовыми данными, например `SUM()` или `AVG()`.

Значения полей предлагаются только для полей, основанных на перечислениях. Для автозавершения не выполняется никакого реального запроса к Elasticsearch.

Dynatrace Environment API

Вызовы API можно выполнять с помощью предпочитаемого клиента. Соответствующую документацию API можно найти в разделе [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Узнать, что предлагает язык запросов User Sessions Dynatrace API.").

Для выполнения этих вызовов токену API нужно назначить разрешение **User sessions** (`DTAQLAccess`). Сведения о том, как получить и использовать токен, см. в разделе [Dynatrace API — токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнать, как пройти аутентификацию для использования Dynatrace API.").

### Временные диапазоны в Environment API

Доступ к данным пользовательских сессий всегда должен осуществляться с указанием временного диапазона. Доступ к большим временным диапазонам может быть затратным из-за большого числа потенциальных отдельных совпадений с запросами.

Временной диапазон обычно не является частью самого запроса, а передаётся в отдельных параметрах вызова API. Подробности можно найти в документации API.

Тем не менее для выбора временного диапазона можно использовать временные поля, такие как `starttime` и `endtime`. Эти поля можно также использовать в функциях, например, чтобы узнать, в какое время суток начинается больше всего пользовательских сессий, как в `HOUR(starttime)`.

## Ключевые слова и функции

Для доступа к данным пользовательских сессий определены следующие ключевые слова:

`AND`, `AS`, `ASC`, `BETWEEN`, `BY`, `DESC`, `DISTINCT`, `FALSE`, `FROM`, `GROUP`, `IN`, `IS`, `JSON`, `LIMIT`, `NOT`, `NULL`, `OR`, `ORDER`, `SELECT`, `STARTSWITH`, `TRUE`, `WHERE`, `LIKE`, `FILTER`

Для доступа к данным пользовательских сессий определены следующие функции:

`SUM`, `MAX`, `MIN`, `AVG`, `MEDIAN`, `COUNT`, `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `DATETIME`, `TOP`, `PERCENTILE`, `KEYS`

Ключевые слова, функции и названия столбцов нечувствительны к регистру. Сравнение строк в условиях `WHERE` чувствительно к регистру.

## Синтаксис

Типичный запрос строится из следующих ключевых слов:

`SELECT <columns> FROM <table> WHERE <condition> GROUP BY <grouping> ORDER BY <ordering>`

Однако единственные обязательные элементы, это `SELECT <columns>` и `FROM <table>`.

Пример

```
SELECT browserType, userId, city, AVG(userActionCount) AS "Average user action count", AVG(duration) AS "Average duration", count(*) AS "Sessions", SUM(totalErrorCount) AS "Errors" FROM usersession WHERE ip between '52.179.11.1' and '52.179.11.255' GROUP BY browserType, userId, city
```

### Часто используемые ключевые слова

#### SELECT `<columns>`

Выбирает один или несколько столбцов из указанной таблицы данных или выполняет агрегатные функции из набора поддерживаемых функций.

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

Позволяет использовать предопределённый формат воронки для запроса. Можно применять для построения графика потока конкретных пользовательских действий. Также можно комбинировать с пользовательскими свойствами сессии и другими условиями.

Это меняет синтаксис любого запроса на следующий:

```
SELECT FUNNEL (<condition> AS <alias>, <condition>, ...) FROM <table> WHERE <condition>
```

* Для запросов `FUNNEL` не используются функции `SELECT *` или ключевые слова вроде `JSON`.
* На данный момент операторы `GROUP BY`, `ORDER BY` или `LIMIT` в воронках не допускаются.
* `FUNNEL` не поддерживает упорядочивание. Нет гарантии, что `useraction1` произошло раньше `useraction2` для запроса `SELECT FUNNEL (useraction.name = "useraction1", useraction.name = "useraction2") FROM usersession`. Этот запрос это лишь эквивалент двух операторов `SELECT`, как показано в примерах ниже.

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

Чтобы получить список числа пользователей, успешно забронировавших поездку:

```
SELECT FUNNEL (useraction.name="login", useraction.name = "searchJourney", useraction.name = "bookJourney")



FROM usersession
```

#### FROM `<table>`

Можно указать только одну таблицу. Таблицы для данных пользовательской сессии следующие.

* `usersession` содержит информацию о [пользовательских сессиях](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
* `useraction` хранит данные о [пользовательских действиях](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.").
* `userevent` предоставляет информацию о [пользовательских событиях](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), таких как смена страниц или события раздражения (rage events).
* `usererror` содержит более подробные данные о [событиях ошибок](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), то есть ошибках и сбоях.

Пример

```
SELECT country, city, browserfamily FROM usersession



SELECT name, starttime, endtime, duration FROM useraction ORDER BY duration DESC
```

#### WHERE `<condition>`

Можно комбинировать несколько условий с помощью булевой логики и скобок внутри выражения `WHERE`, например `WHERE (city = 'Barcelona' AND country = 'Spain')`, чтобы включить только города с названием Barcelona, находящиеся в Spain.

```
condition: (condition AND condition) | (condition OR condition) | field IN(...) |



field IS <value> | field IS NULL | field = <value> | field > <value> | field < <value> |



field <> <value> | field IS NOT <value> | field BETWEEN <value> AND <value> | ...
```

Однако значение может содержаться только в правой части условий, поэтому сравнение между двумя полями невозможно.

Примеры

```
SELECT country, city, browserfamily FROM usersession WHERE country = 'Albania' AND screenWidth > 1000



SELECT TOP(country, 20), TOP(city, 20), TOP(duration, 10), AVG(duration) AS average



FROM usersession



WHERE duration BETWEEN 1000 AND 2000



GROUP BY TOP(country, 20), TOP(city, 20), TOP(duration, 10)
```

#### GROUP BY `<grouping>`

Всякий раз, когда поля агрегируются, нужно указывать соответствующее ключевое слово `GROUP BY`, чтобы обозначить, как должна выполняться агрегация.

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

Позволяет ограничить число возвращаемых результатов. Например, можно выбрать только 10 лучших результатов, если это скомбинировано с упорядочиванием.

Фреймворк всегда применяет верхний предел, чтобы не допустить перегрузки системы. Если `LIMIT` не используется, по умолчанию возвращается 50 результатов.

Пример

```
SELECT city, starttime FROM usersession ORDER BY starttime DESC LIMIT 10
```

`LIMIT` также можно использовать для увеличения числа результатов в случаях, когда оператор `LIMIT` отсутствует, поскольку тогда применяется предел по умолчанию.

#### ORDER BY `<ordering>`

Позволяет упорядочивать результаты по столбцам, в порядке возрастания или убывания. По умолчанию порядок возрастающий, если не указано иное.

Упорядочивание выполняется по частоте. Например, 5 лучших возвращаемых городов, это города, встречающиеся чаще всего. Указав поле в выражении `ORDER BY`, можно добавить значение сортировки для строк, дат и чисел.

Упорядочивание по `enums` или по `значениям функций`, таким как `AVG` и `SUM`, упорядочивает возвращаемые результаты, но лучшие элементы можно и не получить. Например, если запросить 5 лучших результатов по `AVG(duration)`, запрос только 10 может добавить результаты даже в верхней части.

```
ordering: <column> ASC | <column> DESC | <column>, ...
```

Пример 1

```
SELECT useraction.name, starttime FROM usersession ORDER BY starttime DESC
```

Пример 2

Упорядочивания по количеству можно добиться, добавив ключевое слово `DISTINCT`.

```
SELECT DISTINCT city, COUNT(*) FROM usersession ORDER BY COUNT(*) DESC
```

Пример 3

Упорядочивания функций в списке выбора можно добиться, указав только имя столбца или псевдоним, определённый в `SELECT`.

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

Позволяет сравнивать данные с выражением с помощью подстановочных символов для соответствия указанному шаблону. Можно использовать следующие символы:

* `%` или `*`: соответствует любой строке из 0 или более символов
* `?`: соответствует любому одному символу

Строковые значения чувствительны к регистру. Например, `SELECT city FROM usersession WHERE userId LIKE "*dynatrace*"` соответствует `me@dynatrace.com`, но не `me@dynaTrace.com`. Чтобы этого избежать, используется подстановочный символ `?`, как в этом примере: `SELECT city FROM usersession WHERE userId LIKE "*dyna?race*"`

Экранирование подстановочных символов

Чтобы экранировать подстановочный символ, перед ним добавляется обратный слэш `\`. Например, `\%`, `\*` и `\?` рассматриваются как обычные строковые литералы `%`, `*` и `?`.

Чтобы экранировать сам обратный слэш `\`, перед ним добавляется ещё один обратный слэш `\`. Полученная запись `\\` рассматривается как один обратный слэш `\`.

Если добавить два обратных слэша `\\` перед подстановочным символом (получаются записи вроде `\\%`, `\\*` или `\\?`), такая запись рассматривается как один экранированный обратный слэш `\` и один подстановочный символ. Например, запись `\\*` соответствует `\abc`, `\123ABC` или `\`.

Сводка по экранированию подстановочных символов:

| Запись | Рассматривается как | Соответствует |
| --- | --- | --- |
| `\%` | `%` | `%` |
| `\*` | `*` | `*` |
| `\?` | `?` | `?` |
| `\\` | `\` | `\` |
| `\\%` | `\` и любая строка из нуля или более символов | `\abc`, `\123ABC`, `\` и т. д. |
| `\\*` | `\` и любая строка из нуля или более символов | `\abc`, `\123ABC`, `\` и т. д. |
| `\\?` | `\` и любой один символ | `\a`, `\1`, `\A` и т. д. |

Примеры экранирования подстановочных символов:

```
SELECT userId FROM usersession WHERE userId LIKE "AU\%40KWM"
```

Запрос соответствует `userId`, равному `AU%40KWM`.

```
SELECT userId FROM usersession WHERE userId like "AU\*40KWM"
```

Запрос соответствует `userId`, равному `AU*40KWM`.

```
SELECT userId FROM usersession WHERE userId LIKE "AU\?40KWM"
```

Запрос ищет `userId`, равный `AU?40KWM`.

```
SELECT userId FROM usersession WHERE userId LIKE "AU\\%40KWM"
```

Запрос содержит один экранированный обратный слэш `\` и один подстановочный символ `%`, поэтому запрос соответствует `userId` вроде `AU\40KWM`, `AU\abcd40KWM`, `AU\ab12340KWM` или `AU\777_12340KWM`.

Запросы с 11+ условиями LIKE с нехвостовыми подстановочными символами отклоняются

Запросы USQL, содержащие 11 или более условий `LIKE` с `*` или `%` в начале или внутри шаблона поиска (но не в конце), отклоняются от выполнения.

Обычно просто подсчитывается количество условий `LIKE`, используемых в запросе. Например, в приведённом ниже запросе пять условий `LIKE`, при этом считается каждое вхождение `LIKE` в выражении `WHERE` и в функции `CONDITION`.

```
SELECT CONDITION(COUNT(userSessionId), WHERE useraction.name LIKE '*search.html'),



CONDITION(COUNT(userSessionId), WHERE useraction.name LIKE '*booking-payment1.html')



FROM usersession



WHERE city LIKE "%York"



OR city LIKE "S*Francisco"



AND city LIKE "L*inz"
```

Однако при использовании [функции `FUNNEL`](#funnel) вычисление усложняется. Для этой функции запрос внутренне преобразуется в несколько запросов. После этого преобразования подсчитывается число условий `LIKE` в этих внутренне преобразованных запросах.

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

Это значит, что в запросе `FUNNEL` выше на самом деле шесть условий `LIKE`.

#### FILTER

Позволяет фильтровать функции с числовыми значениями, отображая тем самым только определённые результаты агрегаций.

Пример

```
SELECT useraction.application,



AVG(usersession.doubleProperties.bookings)



FILTER > 1500



FROM usersession



WHERE usersession.doubleProperties.bookings IS NOT NULL



GROUP BY useraction.application
```

Функции `WHERE` и `FILTER` не взаимозаменяемы. Если предложение `WHERE` можно использовать только для абсолютных значений, то функция `FILTER` работает и с агрегированными значениями.

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

Запрашивает среднее значение числового поля или поля даты. Может быть `NaN`, если поле всегда `null`.

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

Подсчитывает число строк, удовлетворяющих условию.

* `COUNT(*)`: подсчитывает число подходящих элементов.
* `COUNT(<field>)`: подсчитывает число подходящих элементов, у которых `<field>` не равно null.
* `COUNT(DISTINCT <field>)`: подсчитывает число разных значений `<field>` среди выбранных элементов.

Пример

```
SELECT country, COUNT(*), COUNT(city), COUNT(DISTINCT city)



FROM usersession



GROUP BY country
```

Результаты, возвращаемые функцией `COUNT(DISTINCT <field>)`, приблизительные, чтобы избежать высокого потребления памяти. Если `COUNT(DISTINCT <field>)` используется на поле с высокой кардинальностью, результаты могут быть ещё более грубыми. Поля с высокой кардинальностью, это поля, у которых мало дубликатов.

Результаты, основанные на экстраполированных данных, могут быть ещё более обобщёнными, подробнее см. [Ограничения](#limitations).

Поля с высокой кардинальностью

| Таблица | Поля |
| --- | --- |
| `usersession` | `ip` , `userSessionId` , `internalUserId` , `userId` |

Dynatrace отклоняет и не выполняет запросы с `COUNT(DISTINCT <field>)`, которые могут потреблять много памяти. Это происходит для всех полей с чрезвычайно высокой кардинальностью, например для полей `dateTime`, таких как `usersession.startTime`, `usersession.endTime` или `useraction.networkTime`.

Поля с чрезвычайно высокой кардинальностью

| Таблица | Поля |
| --- | --- |
| `usersession` | `startTime` , `endTime` , `replayEnd` , `clientTimeOffset`, `duration` , `replayStart` |
| `useraction` | `domContentLoadedTime` , `startTime` , `firstPartyBusyTime` , `documentInteractiveTime` , `navigationStart` , `totalBlockingTime` Устарело, `largestContentfulPaint` , `visuallyCompleteTime` , `cdnBusyTime` , `endTime` , `domCompleteTime` , `networkTime` , `loadEventStart` , `serverTime` , `firstInputDelay` , `responseStart` , `thirdPartyBusyTime` , `duration` , `loadEventEnd` , `responseEnd` , `frontendTime` , `requestStart` |
| `userevent` | `startTime` |
| `usererror` | `startTime` |

Пример

```
SELECT country, COUNT(*), COUNT(city), COUNT(DISTINCT city)



FROM usersession



GROUP BY country
```

#### TOP(field, n)

Возвращает верхние `<n>` результатов по полю. Значение по умолчанию `1` (верхнее значение), если `n` не указано.

Пример

```
SELECT TOP(name, 20), SUM(duration)



FROM useraction



GROUP BY name
```

Если выбрано `TOP(<field>, n)` и результаты сгруппированы, но `<field>` не входит в группировку, top-n элементов возвращаются в виде списка в одном поле.

```
SELECT TOP(country, 20), TOP(city, 3), COUNT(*)



FROM usersession



GROUP BY country
```

#### YEAR(datefield), MONTH(datefield), DAY(datefield), HOUR(datefield), MINUTE(datefield)

Возвращает заданный элемент, извлечённый из поля даты.

* `YEAR`: год из четырёх цифр.
* `MONTH`: номер месяца, от 1 до 12
* `DAY`: день месяца, от 1 до 31.
* `HOUR`: значение часа, от 0 до 23.
* `MINUTE`: значение минуты, от 0 до 59.

Пример

```
SELECT starttime,



DATETIME(starttime), YEAR(starttime), MONTH(starttime), DAY(starttime), HOUR(starttime), MINUTE(starttime)



FROM usersession



ORDER BY starttime DESC
```

#### DATETIME(datefield [, format [, interval]])

Форматирует выбранное поле даты согласно заданной строке формата. Формат по умолчанию: `yyyy-MM-dd HH:mm`.

Допустимые буквы в строке формата:

* `y`: год
* `M`: месяц
* `d`: день месяца
* `H`: час (0-23)
* `h`: час (1-12)
* `m`: минута
* `s`: секунда
* `E`: день недели (Mon-Sun)

Интервалы `year`|`month`|`week` предназначены для одного `interval`. Для `d` (дни), `h` (часы), `m` (минуты) или `s` (секунды) можно использовать число, за которым следует буква формата, например `5m`. Например, `SELECT DISTINCT DATETIME(starttime, 'HH:mm', '5m'), COUNT(*) FROM usersession` подсчитывает сессии по пятиминутным временным блокам.

Пример

```
SELECT DATETIME(starttime, 'yyyy-MM') FROM usersession



SELECT DISTINCT DATETIME(starttime, 'HH:mm', '5m'), COUNT(*) FROM usersession
```

Как и другие функции даты (`YEAR`, `MONTH`, `DAY`, `HOUR` и `MINUTE`), `DATETIME` можно использовать для форматирования результата (даже результата других функций, таких как `MAX`, `MIN`, `AVG` или `CONDITION`), построения гистограмм или получения списка временных меток, для которых есть результаты, например дней недели, когда использовалось приложение.

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

Несколько условий можно комбинировать с помощью булевой логики и скобок функцией `CONDITION`, например `CONDITION(COUNT(*), WHERE city = 'Barcelona' AND country = 'Spain')`, чтобы включить только города с названием Barcelona, находящиеся в Spain.

```
CONDITION(function, condition)



condition:



(condition AND condition) | (condition OR condition) | field IN(...) |



field IS <value> | field IS NULL | field = <value> | field > <value> | field < <value> |



field <> <value> | field IS NOT <value> | field BETWEEN <value> AND <value> | ...
```

Также можно использовать оператор `FILTER` для функций с числовыми значениями, тем самым отображая только определённые результаты агрегаций.

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

Представляет значение, ниже которого находится определённый процент точек данных. Полезно для определения скорости работы приложения для клиентов, получающих самое медленное время отклика.

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

Возвращает ключи [свойств пользовательского действия или пользовательской сессии](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/action-and-session-properties "Свойства пользовательского действия и пользовательской сессии, это метаданные в формате пар ключ-значение, которые обеспечивают дополнительную видимость и более глубокий анализ пользовательского опыта конечных пользователей. Используя эти свойства для веб-приложений, можно фильтровать пользовательские сессии, добавлять вычисляемые метрики, создавать диаграммы и многое другое.") согласно типу данных свойства, заданному в аргументе.

В таблице ниже указано, возвращаются ли ключи свойств пользовательского действия или ключи свойств пользовательской сессии.

| KEYS(customProperty) | Таблица | Свойства действия | Свойства сессии |
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

Для получения различающихся ключей свойств действия или сессии используется `DISTINCT KEYS(customProperty)`.

Пример 2

```
SELECT DISTINCT KEYS(stringProperties) FROM useraction WHERE useraction.application = "easyTravel demo application" ORDER BY keys(stringProperties)



SELECT DISTINCT KEYS(doubleProperties) FROM usersession
```

## Математические операции

Следующие операции поддерживаются в составе запросов:

* операции над числами
* операции над числовыми полями и полями типа dateTime
* операции над определёнными функциями, такими как `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`
* операции над числовыми значениями с отображением их в разных единицах измерения

### Синтаксис

`Number/NumericField/DateTimeField/Function OPERATOR Number/NumericField/DateTimeField/Function`

Function: `YEAR`, `MONTH`, `DAY`, `HOUR` или `MINUTE`
Operator: `+`, `-`, `*`, `/`, `%` или `MOD`

Пример

```
SELECT 7 + 80 * 100, duration + startTime, MONTH(startTime) - 1



FROM usersession
```

## Условия

Все условия должны начинаться с идентификатора, например с имени поля, и сравниваться со значением. Два поля нельзя сравнивать между собой.

Текст в кавычках всегда чувствителен к регистру.

### Базовые операторы

Базовые операторы сравнения: `=`, `!=`, `<>`, `<`, `>`, `<=`, `>=`, `IS` и `IS NOT`.

Чтобы проверить, задано ли значение поля, нужно сравнить поле с `NULL`.

Пример

```
SELECT userId FROM usersession WHERE userActionCount > 3
```

### Диапазоны

Диапазоны обрабатываются с помощью ключевых слов `BETWEEN` или `NOT BETWEEN`, `<lowerLimit>` и `<upperLimit>`.

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

Строковое условие `"STARTSWITH"` проверяет, начинается ли строка или поле типа enum с указанного текста.

Пример

```
SELECT city FROM usersession WHERE userId STARTSWITH "dynatrace"
```

### Значения datetime

При выполнении условий над полем типа datetime поддерживаются следующие форматы значений:

| Формат | Описание | Пример |
| --- | --- | --- |
| — | Unix-время в виде числа в миллисекундах | `1514152800000` |
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

Если время не указано, по умолчанию используется `00:00:00`.

Иногда запросы со значениями datetime могут давать неверные результаты из-за перевода на летнее/зимнее время (Daylight Saving Time). Если дата в запросе предшествует дате окончания Daylight Saving Time (например, дате до 7 ноября 2021, 02:00), стоит использовать ISO datetime со смещением времени, например `2021-10-05T17:30:00+03:00`.

Пример

```
SELECT starttime FROM usersession WHERE starttime > "8.8.2018 8:00"
```

### Оптимизация условий

#### IN

Если запрос содержит несколько условий на равенство для одного и того же поля через `OR`, вместо них лучше использовать функцию `IN`, поскольку она более производительна. Например, следующий запрос можно переписать с помощью функции `IN`.

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

Чтобы ускорить выполнение запросов, для запросов лучше использовать массивы: вместо нескольких операторов `NOT`, `<>` или `!=` использовать оператор `NOT IN`.

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

Поле IP можно запрашивать по диапазонам адресов. Работают оба варианта: `BETWEEN ip > <lower ipaddress range> AND ip < <upper ipaddress range>` и `BETWEEN <lower ipaddress range> AND <lower ipaddress range>`.

Пример

```
SELECT * FROM usersession WHERE ip > '211.44.94.0' AND ip < '212.113.5.0'



SELECT * FROM usersession WHERE ip BETWEEN '211.44.94.0' AND '212.113.5.0'
```

### Запрос селектора временного диапазона

Можно использовать следующие ключевые слова для выбора начального и конечного времени, заданных в селекторе временного диапазона.

* `TIME_FRAME_START`
* `TIME_FRAME_END`

Пример

```
SELECT * FROM usersession WHERE startTime >= $TIME_FRAME_START AND endTime < $TIME_FRAME_END
```

Селекторы временного диапазона можно использовать для ограничения временного диапазона в запросах, выполняемых для вторичных таблиц (`useraction`). По умолчанию фильтр временного диапазона применяется к таблице `usersession`, даже если запрос выполняется для любой вторичной таблицы. Чтобы применить фильтр также и к вторичной таблице, можно использовать селектор временного диапазона и добавить условие на поле `startTime` вторичной таблицы. В следующем примере показано, как получить `name` и `duration` пользовательских действий, произошедших только в пределах временного диапазона запроса:

Пример

```
SELECT name, duration FROM useraction



WHERE startTime BETWEEN $TIME_FRAME_START and $TIME_FRAME_END
```

### Запрос относительного временного диапазона

Можно выбрать временной диапазон относительно времени выполнения запроса. Текущее время выражается переменной `$NOW`.

`$NOW [+/-] DURATION("[number]TIME_UNIT")`

Для выражения продолжительности поддерживаются следующие единицы времени:

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

Временной диапазон, выбранный в Dynatrace веб-интерфейсе или API API, по-прежнему применяется к результатам, даже если в запросе используется фильтрация на основе временных меток.

### Вторичные таблицы для `usersession`, `useraction`, `userevent` и `usererror`

При использовании `SELECT` с `usersession`, `useraction`, `userevent` или `usererror` столбцы из другой таблицы можно получить и включить в результаты, указав перед именем столбца имя таблицы.

Пример 1

Выбор логического представления таблицы `usersession` или `useraction`. Несколько значений объединяются в результирующем столбце при добавлении информации из `useraction` в запрос к `usersession`.

```
SELECT city, useraction.name FROM usersession



SELECT usersession.city, name FROM useraction
```

Другие вторичные таблицы, `userevent` и `usererror`, используются таким же образом.

```
SELECT usersession.country, name, page FROM userevent



SELECT usersession.country, name, type FROM usererror



SELECT country, userevent.name, usererror.name FROM usersession
```

При запросе к первичной таблице `usersession` можно объединять поля из других вторичных таблиц (`useraction`, `userevent` и `usererror`). Поля из вторичных таблиц можно использовать и в условии `WHERE`.

Пример 2

```
SELECT city, useraction.name, userevent.page, usererror.type FROM usersession



SELECT city, usererror.name, userevent.page, useraction.duration FROM usersession WHERE usererror.name IS NOT NULL
```

Пример 3

Список всех пользовательских сессий, содержащих пользовательское событие или пользовательское действие из одного и того же приложения.

```
SELECT * FROM usersession



WHERE userevent.application = "a" OR useraction.application="a"
```

При запросе к любой из вторичных таблиц (`useraction`, `userevent` или `usererror`) можно использовать поля только из первичной таблицы `usersession`, поля из других вторичных таблиц использовать нельзя. Например, запрос ниже завершится с ошибкой, поскольку выбранная таблица, это `userevent`, а значит, можно выбирать только поля из `userevent` или `usersession`.

```
SELECT usersession.city, useraction.name, userevent.page, usererror.type FROM userevent
```

То же ограничение действует и для других вторичных таблиц, `useraction` и `usererror`.

Пример 4

Следующие запросы не завершатся с ошибкой, поскольку используются только поля из выбранной вторичной таблицы и из первичной таблицы.

```
SELECT usersession.userId, name, duration FROM useraction



SELECT usersession.userId, name, type FROM usererror
```

Нет способа связать вторичные таблицы между собой и вывести какие-либо отношения между таблицами `useraction`, `userevent` или `usererror`, а также определить, в каком порядке они произошли. Поэтому невозможно сказать, какое `useraction` вызвало какую `usererror`. Единственная связь, которую можно установить, это связь с `usersession`, к которой они относятся.

Применяемые условия имеют разный смысл в зависимости от таблицы. Например, предположим, что нужно вывести список всех пользовательских сессий, содержащих пользовательские действия с именами `a` и `b`:

```
SELECT * FROM usersession



WHERE useraction.name = "a" AND useraction.name = "b"
```

Это означает, что сессия должна содержать пользовательское действие с именем `"a"` и пользовательское действие с именем `"b"`. Выполнение того же запроса к таблице `useraction` вернёт пустой результат, поскольку одно и то же пользовательское действие не может иметь два разных значения для имени.

Если нужно выбрать данные пользовательской сессии для конкретного пользовательского действия, соответствующего нескольким критериям, выполните следующий запрос к таблице `useraction`.

```
SELECT usersession.*, * FROM useraction



WHERE useraction.name = "a" AND useraction.duration > 1000
```

В этом случае каждое пользовательское действие в результате удовлетворяет обоим условиям.

Рассмотрим ещё один запрос.

```
SELECT COUNT(usersession.userSessionId)



FROM usersession



WHERE userevent.name = 'Page change'



AND userevent.pageGroup = '/Booking'



AND userevent.type = 'UserTag'
```

Поскольку запрос выполняется к таблице `usersession`, условия применяются к общему набору пользовательских событий, относящихся к одной сессии. Это означает, что любая пользовательская сессия, содержащая пользовательские события, удовлетворяющие условиям, отражается в подсчёте. Например, если пользовательская сессия содержит три пользовательских события, каждое из которых удовлетворяет одному из заданных условий, эта пользовательская сессия отражается в подсчёте.

Если выполнить тот же запрос к таблице `userevent`, условия применяются к каждому отдельному пользовательскому событию. Это означает, что в подсчёте отражаются только те пользовательские сессии, у которых есть хотя бы одно пользовательское событие, удовлетворяющее **всем** условиям.

```
SELECT COUNT(usersession.userSessionId)



FROM userevent



WHERE userevent.name = 'Page change'



AND userevent.pageGroup = '/Booking'



AND userevent.type = 'UserTag'
```

### Фильтрация с использованием полей вторичной таблицы

Нужно быть внимательным при фильтрации с использованием полей одной из вторичных таблиц. Рассмотрим примеры ниже.

**Пример 1**

```
SELECT useraction.name FROM usersession WHERE useraction.name="abc"
```

Этот запрос возвращает список всех пользовательских сессий, содержащих хотя бы одно пользовательское действие с именем `abc`. Результат содержит список всех пользовательских действий для каждой сессии, поскольку запрос выполняется на уровне `usersession`.

**Пример 2**

```
SELECT name FROM useraction WHERE name="abc"
```

Этот запрос извлекает список только тех пользовательских действий, которые названы `abc`.

### SELECT \* FROM table

Пример

```
SELECT * FROM usersession



SELECT useraction.* FROM usersession



SELECT city, useraction.* FROM usersession



SELECT *, useraction.* FROM usersession
```

Звёздочка `*` сама по себе выбирает столбцы из основной таблицы, а не из вторичной. Например, поля из `useraction` не включаются в `SELECT * FROM usersession`, если не указать `useraction.*`.

### JSON export

Ключевое слово `JSON` добавляет дополнительный столбец, содержащий данные о запрошенной записи (пользовательской сессии, пользовательском действии, пользовательском событии или пользовательской ошибке) в формате JSON.

Если выбрана первичная таблица `usersession`, для соответствующих пользовательских сессий возвращаются полные строки JSON, независимо от выбранных столбцов.

Пример 1

Запрос ниже возвращает соответствующие пользовательские сессии в виде JSON в дополнительном столбце, включая данные из всех вторичных таблиц.

```
SELECT usersessionId, browserFamily, useraction.name, useraction.duration, JSON



FROM usersession LIMIT 5
```

Если выбрана [вторичная таблица](#usql-secondarytables) (`useraction`, `userevent` или `usererror`), возвращаются полные строки JSON для соответствующей подзаписи (пользовательского действия, пользовательского события или пользовательской ошибки).

Пример 2

Запрос ниже возвращает соответствующие пользовательские действия в виде JSON в дополнительном столбце, без данных из таблицы `usersession` или других вторичных таблиц.

```
SELECT name, duration, JSON



FROM useraction LIMIT 5
```

См. также [Export user sessions in RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/export-session-data "Настройка Dynatrace для экспорта данных пользовательских сессий на предоставленную конечную точку webhook.").

### Экранирование строк

Строковые литералы можно заключать в одинарные или двойные кавычки. Однако, если нужно использовать ту же кавычку внутри строки, её просто нужно продублировать.

Пример

```
SELECT * FROM usersession WHERE userId = "some 'custom' name for ""my user"""



SELECT * FROM usersession WHERE userId = 'some ''custom'' name for "my user"'
```

### Построение воронки

Построение воронки позволяет отслеживать шаги в цифровом сервисе и исследовать области, в которых пользователи сталкиваются со сложностями. В сочетании с Session Replay Classic эта функциональность позволяет увидеть, на каком этапе пользователь испытывает сложности в приложении.

Пример

```
SELECT FUNNEL(



useraction.name = "AppStart (easyTravel)" AS "Open easytravel",



useraction.name = "searchJourney" AS "Search journey",



useraction.name = "bookJourney" AS "Book journey",



useraction.matchingConversionGoals = "Payment" OR useraction.matchingConversionGoals = "booking-finished" AS "Booked")



FROM usersession
```

Также можно фильтровать по конкретному сегменту. Пример этого, использование свойств сессии для извлечения списка приоритетных клиентов.

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

`FUNNEL` не поддерживает упорядочивание. Нет гарантии, что `useraction1` произошло раньше `useraction2` для запроса `SELECT FUNNEL (useraction.name = "useraction1", useraction.name = "useraction2") FROM usersession`. Этот запрос эквивалентен всего лишь двум операторам `SELECT`.

## Доступные таблицы и поля данных пользовательских сессий

Для данных пользовательских сессий доступны следующие таблицы.

* `usersession` содержит информацию о [пользовательских сессиях](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
* `useraction` хранит данные о [действиях пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.").
* `userevent` предоставляет информацию о [событиях пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), таких как смена страниц или rage-события.
* `usererror` содержит дополнительные данные о [событиях ошибок](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error-events "Learn about user and error events and the types of user and error events captured by Dynatrace."), то есть об ошибках и сбоях.

[Вторичные таблицы для `usersession`, `useraction`, `userevent` и `usererror`](#usql-secondarytables) описывают, как данные из одной из этих таблиц доступны в другой.

Поля описаны в разделе [User sessions API, структура пользовательской сессии](/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure "Learn the structure of a user session in the Dynatrace User Session Query language API.").

Также можно проверить объект **UserSession** в [API Explorer](/managed/dynatrace-api#api-explorer "Find out what you need to use the Dynatrace API.").

## Выполнение запросов USQL для пользовательских отчётов

REST-интерфейс позволяет получать результаты для пользовательских запросов. Для этого нужен только уникальный [токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") с правом **User session query language**. Возможность запрашивать данные пользовательских сессий таким способом полезна в автоматизированном тестировании, проверке данных и других автоматизированных функциях. Доступны следующие эндпоинты:

`/table`: возвращает данные в виде плоской таблицы, даже при группировке по различным элементам и выполнении иерархических агрегаций по данным пользовательских сессий.

`/tree`: возвращает данные в виде полного иерархического дерева на основе входных данных.

Доступны следующие параметры запроса:

`query`: нужно кодировать при передаче в URL, например `%20` вместо пробелов.
`startTimestamp/endTimestamp`: позволяют задать моменты времени, передаваемые как количество миллисекунд с начала эпохи Unix. Если не указано, по умолчанию используются последние два часа.

Примеры

Этот код:

```
curl --location --insecure -H "Content-Type: application/json" -H "Authorization: Api-Token _token_" \



-XGET "https://{your-environment-id}.live.dynatrace.com/api/v1/userSessionQueryLanguage/table?query=select%20city,count(*)%20from%20usersession%20group%20by%20city"
```

даёт следующий результат:

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

Этот код:

```
curl --location --insecure -H "Content-Type: application/json" -H "Authorization: Api-Token _token_" \



-XGET "https://{your-environment-id}.live.dynatrace.com/api/v1/userSessionQueryLanguage/tree?query=select%20country,city,count(*)%20from%20usersession%20group%20by%20country,city"
```

даёт следующий результат:

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

Подробнее о [user sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.").

## Преобразование запросов в пользовательские метрики USQL

Некоторые запросы можно преобразовать в пользовательские метрики USQL для [веб](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/custom-metrics-from-user-sessions "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications."), [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for custom applications.").

Пользовательские метрики USQL доступны как
пользовательские метрики сессий (USCM) и пользовательские метрики действий (UACM). Пользовательские метрики действий поддерживаются начиная с версии Dynatrace 1.260.

1. Перейти в **Query User Sessions**.
2. Ввести запрос, затем выбрать **Run query**.  
   Список поддерживаемых полей см. в подробных руководствах для [веб](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/custom-metrics-from-user-sessions#properties-and-supported-values "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications."), [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps#properties-and-supported-values "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps#properties-and-supported-values "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for custom applications.").
3. Выбрать **Create custom metric**.
4. Ввести имя метрики, затем просмотреть предложенные настройки.

## Ограничения

* Dynatrace хранит Real User Monitoring (действия пользователя и пользовательские сессии) ограниченный период времени. Подробности см. в разделе [Периоды хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.").
* Набор результатов по умолчанию составляет 50, но количество результатов можно увеличить максимум до 5000 с помощью ключевого слова `LIMIT`.
* Максимальное количество потенциальных сгруппированных результатов ограничено 100 000. Значение по умолчанию, 10 000.  
  Это влияет на применение `TOP()` при использовании `DISTINCT` или `GROUP BY`. Если `TOP()` не указан, 10 000 возможных результатов равномерно распределяются по указанным столбцам. Эти значения по умолчанию можно переопределить, указав `TOP()` для каждого столбца. Перемноженные значения `TOP()` не могут превышать 100 000 результатов.

  Дополнительные ограничения

  + Функцию `TOP()` можно использовать для увеличения количества различных значений на агрегацию.
  + Максимальное количество различных результатов на агрегацию ограничено 1000.
  + Следующий запрос использует не более 10 000 теоретически возможных результатов:
    `select browserFamily, city, count * FROM usersession group by browserFamily, city`
  + Следующий запрос включает `TOP()` и поэтому может использовать до 100 000 (100 × 1000) теоретически возможных результатов:
    `select TOP(browserFamily, 1000), TOP(city, 100), count * FROM usersession group by browserFamily, city`
* Соединения (joins) не допускаются.
* На один `SELECT` допускается только одна таблица.
* Поиск строковых значений с помощью регулярных выражений не поддерживается.
* Сравнивать два разных поля нельзя. Например, `WHERE field1 = field2` не работает.
* Условия `WHERE` работают только с полями, поэтому ни `WHERE true`, ни `WHERE COUNT(*) > 3` не поддерживаются.
* Запрашивать можно только закрытые пользовательские сессии. Активные пользовательские сессии не учитываются.
* Сортировка поддерживается частично.

  Например, сортировка по результату математической операции не поддерживается.

  ```
  SELECT endTime - startTime AS duration FROM usersession ORDER BY duration
  ```
* Для больших временных диапазонов и сред с высокой нагрузкой данные могут экстраполироваться на основе выборочного подмножества (уровень экстраполяции). Это происходит независимо от того, используется ли API Dynatrace или веб-интерфейс Dynatrace. Если нужны стопроцентно точные данные, следует сократить временной диапазон или добавить дополнительные условия для более точной фильтрации запрашиваемых данных.
* Функции не допускаются в предложении `GROUP BY`. Поэтому, если нужна группировка по месяцу, следует указать псевдоним.
* `FUNNEL` нельзя использовать с функциями `SELECT *`, ключевыми словами вроде `JSON`, а также с операторами `GROUP BY`, `ORDER` и `LIMIT`.
* Для математических операций поддержка `GROUP BY`, `ORDER BY` и других операций с функциями недоступна.
* К `FUNNEL` можно применить не более 10 условий.
* Некоторые поля, например `duration`, при выполнении над ними математических операций, таких как деление, всегда возвращают целочисленные значения вместо десятичных. Это связано с тем, что такие поля хранятся и отображаются как целочисленные значения. Например, `SELECT duration FROM usersession` возвращает значение duration `4800`, а `SELECT duration/1000 FROM usersession` возвращает значение duration `5`.