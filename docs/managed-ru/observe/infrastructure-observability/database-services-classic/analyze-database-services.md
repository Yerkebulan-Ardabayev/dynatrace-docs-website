---
title: Анализ служб баз данных (классический)
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/database-services-classic/analyze-database-services
---

# Анализ служб баз данных (классический)

# Анализ служб баз данных (классический)

* Пояснение
* Чтение за 6 мин
* Обновлено 20 июня 2023 г.

Начиная с Dynatrace 1.269, страница обзора базы данных полностью переработана.

* Чтобы перейти на [новую страницу обзора базы данных](/managed/observe/infrastructure-observability/database-services-classic/analyze-database-services-new "Analyze your database services with Dynatrace (new page)."), нужно включить **Try it out** в верхней части страницы обзора базы данных. При желании можно вернуться к классическому дизайну.
* В документации ниже описан классический дизайн.

Dynatrace отслеживает время отклика, частоту сбоев, пропускную способность и другие показатели каждого оператора базы данных, выполняемого приложениями.

Как проанализировать производительность базы данных

1. Перейти в **Database Services**.
2. Чтобы открыть страницу обзора службы базы данных, выбрать нужную для анализа базу данных.

![Database overview](https://dt-cdn.net/images/database-overview-1297-02a737c3d3.png)

Database overview

Инфографика на странице обзора службы базы данных даёт представление о различных аспектах производительности базы данных, включая **SQL queries or procedures**, **SQL modifications**, **SQL transactions**, обнаруженные проблемы или сбои доступности, точки перегрузки и другое. Точный список включённых плиток зависит от технологии базы данных, которая отслеживается. Каждая плитка содержит показатели **Response time**, **Failure rate** и **Throughput**.

Чтобы проанализировать отдельные операторы, из которых складывается оператор базы данных, на странице обзора базы данных нужно выбрать **View database statements**.

## Детали базы данных

В нижней части страницы **Details** находится список всех **Database statements**, выполненных за выбранный период времени. По умолчанию они отсортированы по медианному времени отклика, но список можно отсортировать по общему времени, времени отклика или по самым медленным 10%, а также отфильтровать по оператору, имени базы данных, поставщику, процессу или имени хоста.

![Database details page](https://dt-cdn.net/images/database-details-page-1293-85e42be938.png)

Database details page

Нужно выбрать любой оператор, чтобы посмотреть его полные детали. Для каждого оператора Dynatrace показывает число **Executions**/мин, **Total executions**, **Total time**, медианное **Response time** и время отклика самых медленных 10% выполнений, а также **Failure rate**.

Ограничения оператора

По умолчанию длина операторов базы данных ограничена 4 КБ (килобайтами). Этот параметр не настраивается. Операторы базы данных, превышающие это ограничение, обрезаются до 4 КБ.

### Обратная трассировка службы базы данных

Как открыть анализ обратной трассировки для определённого оператора

1. В списке операторов базы данных перейти к строке оператора, который нужно проанализировать.
2. Выбрать **More** (**…**) > **Service backtrace**.

![Database service-level backtrace - application](https://dt-cdn.net/images/database-service-level-backtrace-application-1490-89f24b7b0f.png)

Database service-level backtrace - application

Страница **Backtrace** предоставляет подробные сведения о кликах, которые вызвали выбранную перестановку SQL-оператора, и позволяет увидеть, какая цепочка служб и какой код приводит к конкретному оператору. Выбрав определённое приложение в обратной трассировке, можно найти все действия пользователя из этого приложения, которые вызывают анализируемый оператор базы данных.

Пример

На изображении выше в столбце **Incoming requests** видно, что **1200** запросов к базе данных на `easyTravelBusiness` происходят из **668** действий пользователя.

При выборе `www.easyTravelBusiness.com` выделяется строка, показывающая, что **668** действий пользователя привели к **1150** запросам на `easyTravel Customer Frontend`. При этом выборе видно, что три разных действия пользователя из `www.easytravel.com` вызывают этот оператор. Также видна цепочка служб, которая его вызывает. Чтобы исследовать дальнейшие приращения числа запросов в цепочке, нужно выбрать любой из последующих операторов в цепочке вызовов служб.

![Database service-level backtrace - chain](https://dt-cdn.net/images/database-service-level-backtrace-chain-1490-b807b8f624.png)

Database service-level backtrace - chain

При новом выборе (`easyTravel Customer Frontend` на изображении выше) нижняя часть страницы обратной трассировки службы адаптируется, и теперь видно, что **668** действий пользователя из `www.easyTravelBusiness.com` вызывают два запроса на `easyTravel Customer Frontend` (`/orange-booking-payment.jsf` и `/orange-booking-finish.jsf`). Если некоторые из этих запросов завершились сбоем, их можно проанализировать на соответствующей вкладке, **Reasons for failed requests**. В этом примере больше интересует код, приводящий к вызовам базы данных, поэтому нужно выбрать вкладку **Stacktrace**, чтобы посмотреть выполняемый код в контексте.

### Распределение времени отклика

Чтобы понять распределение времени отклика команды, нужно выбрать **Analyze outliers** на странице **Details**.

Страница **Response time distribution** показывает число запросов, попавших в различные диапазоны времени отклика. Нужно выбрать любой столбец на графике, чтобы проанализировать запросы, попавшие в этот конкретный диапазон времени отклика. Это позволяет увидеть, вызываются ли определённые операторы часто и вносят ли они относительно значимый вклад во время отклика.

![Outliers - response time distribution](https://dt-cdn.net/images/database-response-time-distribution-1309-417be68a11.png)

Outliers - response time distribution

## Анализ снижения производительности

С мониторингом баз данных Dynatrace можно анализировать снижение производительности. Операторы, ответственные за обнаруженное замедление, выделяются в списке операторов в нижней части страницы **Details**.

![Database - response time degradation](https://dt-cdn.net/images/database-4-1090-03b012cb2e.png)

Database - response time degradation

В примере ниже обнаруженное снижение времени отклика было вызвано двумя операторами (`Aggregations in BookingCollection` и `Aggregations in JourneyCollection`).

Чтобы увидеть, какая служба выполнила конкретный оператор, приведший к замедлению базы данных, нужно перейти к обратной трассировке оператора.

![Slow database statements](https://dt-cdn.net/images/mysql-7-966-2c43e07703.png)

Slow database statements

Здесь `easyTravel-Business`, это служба, выполняющая оператор, вызывающий замедление.

![Database service - slow statements](https://dt-cdn.net/images/database-6-1286-28bedc7573.png)

Database service - slow statements

## Анализ ошибок базы данных

Каждая плитка на странице обзора службы базы данных содержит график **Failure rate** (1).

![Database - analyze failures](https://dt-cdn.net/images/database-analyze-failures-1755-bca922ddef.png)

Database - analyze failures

Нужно выбрать график **Failure rate** (1), чтобы открыть вкладку сбоев на странице **Details**.

Таблица неудачных **database statements** в нижней части страницы сразу показывает, какие операторы завершились сбоем, вместе с их частотой сбоев.

1. Нужно выбрать **View details of failures**, чтобы понять первопричину сбоев.  
   Dynatrace определяет причины высокой частоты сбоев, давая информацию для устранения проблем базы данных и предотвращения будущих ошибок.

   ![Failure rate - database details](https://dt-cdn.net/images/failure-rate-database-details-1753-9ba03aabd4.png)

   Failure rate - database details
2. Для дальнейшего анализа проблемы нужно выбрать **Distributed traces** ![Distributed traces](https://dt-cdn.net/images/purepaths-icon-790bea38ba.svg "Distributed traces") или **Backtrace** ![Backtrace](https://dt-cdn.net/images/backtrace-icon-69e2c66211.svg "Backtrace").

   ![Failure analysis](https://dt-cdn.net/images/failure-analysis-1925-81fd9dc157.png)

   Failure analysis

### Быстрый обзор проблемы

На странице обзора службы базы данных раздел **Current hotspots** (2) даёт быстрый обзор проблемы, выделяя оператор с наивысшей частотой сбоев. Выбрав оператор в этом разделе (2), можно сразу перейти на вкладку сбоев его страницы **Details**.

![View of the statement with the highest failure rate from current hotspots.png](https://dt-cdn.net/images/failure-rate-current-hotspots-1760-57af484dd4.png)

View of the statement with the highest failure rate from current hotspots.png

## Поток служб для анализа SQL

[**Service flow**](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") визуализирует последовательность вызовов служб, которые запускаются каждым запросом службы в среде. С помощью service flow видна цепочка вызовов служб, включая вызовы служб баз данных, с точки зрения отдельной службы, запроса или их отфильтрованного подмножества. Хотя SQL-анализ доступен в нескольких местах в рамках анализа служб, именно представление **Service flow** служит основным видом анализа для баз данных.

Чтобы просмотреть service flow, запущенный конкретной службой базы данных

1. Перейти в **Services**.
2. Выбрать службу, которую нужно проанализировать.
3. На странице обзора службы, в разделе **Understand dependencies**, выбрать **View service flow**.

![Service flow - SQL analysis](https://dt-cdn.net/images/service-flow-sql-analysis-1759-f706b49d27.png)

Service flow - SQL analysis

Пример

В примере выше поток вызовов служб баз данных отфильтрован, чтобы сосредоточиться на конкретной цепочке вызовов. Каждый раз, когда `easyTravel Customer Frontend` вызывает `JourneyService`, **0.01%** от **response time contribution** можно отнести к службе MongoDB `EasyTravelBusiness`.

Чтобы просмотреть операторы базы данных, выполненные выбранным потоком в течение анализируемого периода времени, нужно выбрать **View database statements**. Это может оказаться крайне полезным, поскольку помогает понять, почему база данных дала определённый вклад во время выполнения.

![Multidimesional analysis of top dimensions](https://dt-cdn.net/images/multidimesional-analysis-sql-analysis-1752-aa2f7307ab.png)

Multidimesional analysis of top dimensions

Для одного из **top dimensions** нужно выбрать **More** (**…**), а затем

* Выбрать **Outliers**, чтобы понять разброс времени отклика.
* Выбрать **Statement details**, чтобы понять изменение каждого SQL-оператора со временем, вместе со средним значением количества **Rows returned**.
* Выбрать **Service backtrace**, чтобы увидеть, какие клики пользователя привели к самым медленным выполнениям этого оператора MongoDB.

Как видно, представления анализа операторов баз данных Dynatrace предоставляют мощные возможности анализа, ориентированного на использование базы данных.

## Related topics

* [Top database statements](/managed/observe/application-observability/multidimensional-analysis/top-database-statements "Understand the database activity across your environment with Dynatrace.")
* [Service backtrace](/managed/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.")