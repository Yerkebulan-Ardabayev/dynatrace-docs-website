---
title: Аналитика базы данных Oracle
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/database-services-classic/database-insights
---

# Аналитика базы данных Oracle

# Аналитика базы данных Oracle

* Практическое руководство
* Чтение 13 мин.
* Обновлено 10 апр. 2026 г.
* Будет устаревшим

Аналитика базы данных Oracle будет заменена расширениями на основе источника данных SQL. Подробнее:

* Запись в блоге о новостях продукта: [Intelligent observability for Oracle and SQL databases﻿](https://www.dynatrace.com/news/blog/intelligent-observability-for-oracle-and-sql-databases/)
* Загрузка расширения [Oracle Database﻿](https://www.dynatrace.com/hub/detail/oracle-database/) в Dynatrace Hub
* Как [управлять расширениями Oracle Database](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")
* Как расширить мониторинг Oracle SQL с помощью [источника данных SQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.") Extensions 2.0

Аналитика базы данных добавляет к мониторингу базы данных инфраструктурную перспективу. С дополнительными данными, полученными с уровня базы данных, можно решать проблемы производительности, коренящиеся глубоко в базе данных, например, понимать, почему конкретный запрос выполняется медленно.

## Как это работает

Аналитика базы данных работает на Environment ActiveGate и удалённо подключается к базам данных Oracle. При таком подходе платформа системы базы данных может быть любого типа, Dynatrace поддерживает все операционные системы, используя драйвер JDBC для подключения к базам данных.

![Oracle insights architecture](https://cdn.bfldr.com/B686QPH3/as/6r7qkpgpjzfbhxhqhjtb8mq6/Oracle_database_insights_-_Light_Mode?auto=webp&format=png&position=1)

Архитектура Oracle insights

## Предварительные требования

Для начала работы с аналитикой базы данных Oracle нужно следующее:

* Установленный Environment ActiveGate версии 1.173+ в режиме по умолчанию. Аналитика базы данных не поддерживает ActiveGate, настроенный для [поддержки нескольких сред](/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.").
* Аналитике базы данных требуется 2,5 МБ ОЗУ на каждую конечную точку базы данных Oracle, что даёт возможность мониторить несколько сотен баз данных при установке ActiveGate на инстансе EC2 micro.
* Dynatrace Server версии 1.173+.
* Сетевое взаимодействие между ActiveGate и Oracle Server.
* Oracle версии от 11g до 19c, включая поддержку:

  + **Oracle Multitenant**  
    Результаты мониторинга могут отличаться между конечными точками на основе SID и на основе ServiceName. Для конечных точек на основе SID Dynatrace мониторит подключения к многопользовательской контейнерной базе данных (CDB). Для конечных точек на основе ServiceName Dynatrace мониторит подключения к связанным подключаемым базам данных (PDB).
  + **Oracle RAC**  
    Dynatrace мониторит только отдельные экземпляры узлов (SID). Аналитику базы данных нельзя использовать для мониторинга кластера или мониторинга отдельных узлов на основе связанной с ними службы базы данных.
  + **AWS Oracle RDS**
* Опционально установленный OneAgent на хосте Oracle.
* Пользователь базы данных Oracle с правами доступа, перечисленными ниже.

## Права доступа Oracle

Для аналитики базы данных Oracle на сервере Oracle нужно выполнить следующие требования по правам доступа:

* Пользователю, который подключается к экземпляру БД, нужно предоставить права `CREATE SESSION` и `SELECT_CATALOG_ROLE`. Это также означает доступ к [Dynamic Performance Views﻿](https://docs.oracle.com/database/122/CNCPT/data-dictionary-and-dynamic-performance-views.htm#CNCPT1220), который входит в право `SELECT_CATALOG_ROLE`.
* Для получения планов выполнения нужен пакет `DBMS_XPLAN` с предоставленным правом `EXECUTE`.

Чтобы создать пользователя для аналитики базы данных Oracle:

```
CREATE USER oracleinsights IDENTIFIED BY password



default tablespace users



temporary tablespace temp;



GRANT CREATE SESSION, SELECT_CATALOG_ROLE TO <oracleinsights>;
```

## Настройка аналитики базы данных Oracle

Настройка аналитики базы данных Oracle не представляет сложности. Всё, что нужно сделать, это определить конечную точку, базу данных Oracle, к которой будет подключаться ActiveGate. Можно добавить сколько угодно баз данных с одного сервера Oracle.

1. Опционально: [установить OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") на хосте Oracle.
2. Выбрать или установить и [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") версии 1.173+, который будет получать данные с сервера Oracle. Этот ActiveGate можно использовать и для других целей. Перейти в **Settings** > **Deployment status**, чтобы проверить, работает ли ActiveGate. Аналитика базы данных включена по умолчанию.
3. Перейти в **Settings > Monitoring > Monitored Technologies**.
4. Найти строку **Database Insights: Oracle** и нажать значок карандаша для редактирования.
5. Определить конечную точку базы данных Oracle. Все поля обязательны:

   * **Oracle host**
   * **Port**: значение по умолчанию — `1521`
   * **Connection type**: `Service` или `SID`
   * **Service/SID**: идентификатор базы данных
   * **Database user** и **Database password**: подробнее см. раздел [Права доступа Oracle](#oracle-permissions).
   * **Monitored database name**: имя базы данных, которую нужно мониторить
6. Установить флажок, чтобы принять лицензионное соглашение о распространении для драйвера Oracle JDBC. Dynatrace использует его для получения данных с сервера Oracle. Данные защищены.
7. Выбрать **Add database**. Если Dynatrace сможет установить соединение по указанным данным, Dynatrace начнёт мониторить базу данных Oracle.

## Включение и отключение аналитики базы данных Oracle

Чтобы отключить или включить аналитику базы данных Oracle для отдельной мониторимой базы данных

1. Перейти в **Settings > Monitoring > Monitored Technologies**.
2. Найти строку **Database Insights: Oracle** и нажать значок карандаша для редактирования.
3. Установить переключатель **Monitoring off/on** для каждой базы данных.

## Модель мониторинга аналитики базы данных Oracle

Установка OneAgent на хосте Oracle для аналитики базы данных опциональна. Независимо от того, установлен он или нет, все метрики отражаются в разделе **Custom device**, чтобы показать логическую структуру экземпляра сервера БД, работающих служб, контейнеров и подключённых баз данных.

Однако установка OneAgent на хосте Oracle дополняет анализ производительности сервера всеми метриками процессов ОС, которые отражаются в группе процессов и их экземплярах с разбивкой по экземплярам сервера (SID) и процессам listener.

## Возможности аналитики базы данных Oracle

### Наиболее затратные по времени операторы Oracle

Чтобы понять и проанализировать, какие операторы Oracle наиболее затратны и наиболее часто вызываются, выбрать **View statements** в разделе **Most time-consuming Oracle statements**. На странице перечислены 100 наиболее затратных по времени операторов. Одним щелчком можно увидеть операторы, потребляющие больше всего CPU, памяти или дискового пространства, либо генерирующие наибольшее время ожидания. Анализ можно настроить, используя до трёх метрик, доступных для анализа TopN.

### Загрузка планов выполнения

При анализе характеристик производительности оператора SQL часто возникает необходимость сформировать и отобразить план выполнения этого оператора SQL. План выполнения Oracle можно загрузить прямо из интерфейса Dynatrace.

### Метрики памяти и кэша

Аналитика базы данных Oracle предоставляет дополнительные метрики Oracle, связанные с памятью и кэшами, что позволяет точно определять операторы, интенсивно использующие ОЗУ.

### Data Explorer

Все метрики Oracle, получаемые аналитикой базы данных Oracle, доступны в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

### Метрики ожидания и табличного пространства

Также можно обращаться к метрикам ожидания и табличного пространства, которые доступны для использования в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

### Группы процессов Oracle

Dynatrace связывает данные, полученные аналитикой базы данных Oracle, с процессами Oracle, обнаруженными OneAgent. Начиная с версии OneAgent 1.173, каждая группа процессов Oracle представляет один SID Oracle (уникальный идентификатор для каждого экземпляра БД Oracle). SID входит в имя группы процессов и извлекается из имён процессов (Unix) или описания службы (Windows). Процессы Oracle, не связанные ни с одним SID, образуют группу прочих процессов Oracle. Сюда входит процесс взаимодействия TNS Listener, поэтому весь входящий и исходящий трафик связан с этой группой.

Опционально можно изменить группы процессов базы данных Oracle и listener, разбив их по SID Oracle для баз данных или по имени для listener'ов.

Разбить группы процессов по SID Oracle

1. Перейти в **Settings** > **Processes and containers** > **Built-in detection rules**.
2. Версия OneAgent 1.231+: выбрать **Group Oracle database processes by SID**.

Группа процессов базы данных Oracle будет разбита на несколько групп процессов с именем в формате `Oracle Database <SID>`.

Разбить группы процессов по listener Oracle

1. Перейти в **Settings** > **Processes and containers** > **Built-in detection rules**.
2. Версия OneAgent 1.243+: выбрать **Group Oracle listener processes by name**.

Группа процессов listener Oracle будет разбита на несколько групп процессов с именем в формате `Oracle Listener <listener-name>`.

## Метрики

В этом разделе описываются метрики базы данных Oracle, доступные через Dynatrace:

* [Графики производительности](#performance)
* [Графики разбивки по времени](#time-breakdown)
* [Графики памяти PGA](#pga-memory)
* [Графики памяти SGA](#sga-memory)
* [Наиболее затратные по времени операторы Oracle](#most-time-consuming-oracle-statements-1)
* Метрики только для API, эти метрики не отображаются на графиках в Dynatrace, но доступны через API Dynatrace.

### Производительность

Метрики, касающиеся производительности системы.

Примеры графиков

![Oracle database insights metrics charts: Performance](https://dt-cdn.net/images/oracle-database-insights-charts-performance-844-78a438cd44.png)

Oracle database insights metrics charts: Performance

#### Пропускная способность

* **Total user calls** (количество)  
  Общее количество входов в систему, разборов запросов или вызовов выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.userCalls`
* **Active sessions** (количество)  
  Общее количество активных сессий, не отнесённых к классу ожидания Idle.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.active`

#### ЦП

* **CPU background usage** (%)  
  Среднее использование ЦП фоновыми процессами на один ЦП.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.background`
* **CPU foreground usage** (%)  
  Среднее использование ЦП процессами переднего плана на один ЦП.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.foreground`
* **CPU other processes** (%)  
  Среднее использование ЦП другими процессами на один ЦП (за исключением процессов переднего плана и фоновых процессов).  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.other`
* **CPU idle** (%)  
  Средняя доступность ЦП хоста на один ЦП.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.idle`

#### Диск

* **Read** (Б/мин)  
  Общий объём в байтах всех операций чтения с диска для экземпляра базы данных, включая обращения приложений, резервное копирование и восстановление, а также другие утилиты.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.bytesRead`
* **Write** (Б/мин)  
  Общий объём в байтах всех операций записи на диск для экземпляра базы данных, включая активность приложений, резервное копирование и восстановление, а также другие утилиты.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.bytesWritten`

#### Табличное пространство

* **Total space** (Б)  
  Общий размер табличного пространства.  
  Ключ метрики: `builtin:tech.oracleDb.cd.tablespaces.totalSpace`
* **Used space** (Б)  
  Общий объём используемого пространства.  
  Ключ метрики: `builtin:tech.oracleDb.cd.tablespaces.usedSpace`

#### Попадания в буферный кэш

* **Buffer cache hit** (%)  
  Отражает эффективность буферного кэша блоков данных, как долю блоков данных, требуемых в памяти.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.bufferCacheHit`

#### Сортировки в памяти

* **Sorts in memory** (%)  
  Процент сортировок (из предложений ORDER BY или построения индексов), выполняемых в памяти (в отличие от сортировок на диске).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sortsInMemory`

### Разбивка по времени

Метрики, касающиеся времени, затраченного на различные операции.

Примеры графиков

![Oracle database insights metrics charts: Time breakdown](https://dt-cdn.net/images/oracle-database-insights-charts-time-845-1424994dec.png)

Oracle database insights metrics charts: Time breakdown

#### Общее время ожидания (все сессии)

* **Total wait time** (мкс/мин)  
  Общее время, проведённое во всех состояниях ожидания, кроме класса Idle.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.wait`

#### Разбивка затраченного времени (все сессии)

* **SQL parse** (мкс/мин)  
  Объём времени, затраченного на разбор SQL-операторов.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.sqlParse`
* **SQL execution** (мкс/мин)  
  Объём времени, затраченного на выполнение SQL-операторов.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.sqlExec`
* **PL/SQL execution** (мкс/мин)  
  Объём времени, затраченного на работу интерпретатора PL/SQL.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.plSqlExec`
* **Connection management** (мкс/мин)  
  Объём времени, затраченного на выполнение вызовов подключения и отключения сессий.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.connMgmt`
* **Other** (мкс/мин)  
  Объём времени, затраченного на выполнение всех прочих операций.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.other`

### Память PGA

Метрики, касающиеся памяти Program Global Area (PGA).

Примеры графиков

![Oracle database insights metrics charts: PGA](https://dt-cdn.net/images/oracle-database-insights-charts-pga-840-156d0580a0.png)

Oracle database insights metrics charts: PGA

#### PGA, используемая для рабочих областей

* **PGA used for work areas** (%)  
  Объём выделенной памяти PGA, который в текущий момент потребляется рабочими областями. Может использоваться для определения того, сколько памяти потребляется другими потребителями памяти PGA (например, PL/SQL или Java).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.usedForWorkAreas`

#### Размер PGA

* **Allocated PGA** (Б)  
  Текущий объём памяти PGA, выделенной экземпляром. Oracle Database стремится удерживать это значение ниже значения параметра инициализации **PGA aggregate target** (см. ниже). Однако возможно, что выделенная PGA превысит целевое значение на небольшой процент и на короткий период времени, когда нагрузка на рабочую область растёт очень быстро или когда целевое значение низкое.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.allocated`
* **PGA aggregate target** (Б)  
  Целевой совокупный объём памяти PGA, доступный всем серверным процессам, подключённым к экземпляру.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateTarget`
* **PGA aggregate limit** (Б)  
  Ограничение на совокупный объём памяти PGA, потребляемый экземпляром.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateLimit`

### Память SGA

Метрики, касающиеся памяти System Global Area (SGA).

Примеры графиков

![Oracle database insights metrics charts: SGA](https://dt-cdn.net/images/oracle-database-insights-charts-sga-840-2bcd165f8e.png)

Oracle database insights metrics charts: SGA

#### Общий пул (shared pool)

* **Shared pool free** (%)  
  Объём свободной памяти системной глобальной области (SGA), доступной в общем пуле (shared pool).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.cacheBuffer.sharedPoolFree`

#### Буфер журнала повторного выполнения (redo log)

* **Redo size increase** (Б/мин)  
  Общий объём сгенерированного redo в байтах.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoSizeIncrease`

#### Время, затраченное на буфер журнала повторного выполнения

* **Redo log space wait time** (мкс/мин)  
  Общее прошедшее время ожидания запроса на пространство журнала повторного выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoLogSpaceWaitTime`
* **Redo write time** (мкс/мин)  
  Общее прошедшее время записи из буфера журнала повторного выполнения в текущий файл журнала повторного выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoWriteTime`

### Наиболее затратные по времени операторы Oracle

Метрики, касающиеся операторов, выполнение которых занимает больше всего времени.

Чтобы просмотреть графики этих метрик по каждому оператору Oracle, нужно выбрать **View statements** в разделе **Most time consuming Oracle statements**, а затем выбрать **Details** для нужного оператора.

#### Statements performance

Пример графика

![Oracle database insights metrics charts: Time-consuming metrics: Statements performance](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-statements-performance-1149-2fff80eba5.png)

Oracle database insights metrics charts: Time-consuming metrics: Statements performance

* **Elapsed time** (мкс)
  Время, затраченное во время выполнения запроса на разбор, выполнение и извлечение данных.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.elapsed`
* **Execution count** (количество)
  Общее число выполнений, суммированное по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.executions`
* **CPU time** (мкс)
  Время процессора, затраченное во время выполнения запроса на разбор, выполнение и извлечение данных.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.cpu`
* **Wait time** (мкс)
  Общее время ожидания события.
  Ключ метрики: `builtin:tech.oracleDb.cd.wait.time`

#### Waits

Пример графика

![Oracle database insights metrics charts: Time-consuming metrics: Waits](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-waits-1229-ab8923f437.png)

Oracle database insights metrics charts: Time-consuming metrics: Waits

* **Application wait time** (мкс)
  Время выполнения запроса, затраченное в классе ожидания application.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.application`
* **Concurrency wait time** (мкс)
  Время выполнения запроса, затраченное в классе ожидания concurrency.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.concurrency`
* **Cluster wait time** (мкс)
  Время выполнения запроса, затраченное в классе ожидания cluster.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.cluster`
* **User IO wait time** (мкс)
  Время выполнения запроса, затраченное в классе ожидания user I/O.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.userIo`

#### Execution details

Пример графика

![Oracle database insights metrics charts: Time-consuming metrics: Execution details](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-execution-details-1325-02c6a82dba.png)

Oracle database insights metrics charts: Time-consuming metrics: Execution details

* **All sessions** (количество)
  Общее число всех сессий независимо от их состояния и класса ожидания.
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.all`
* **Executions** (количество)
  Общее число выполнений, суммированное по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.executions`
* **Processed rows** (количество)
  Общее число строк, обработанных запросом.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.rowsProcessed`
* **Buffer gets** (количество)
  Сумма обращений к буферу по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.bufferGets`
* **Disk reads** (количество)
  Сумма числа операций чтения с диска по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.diskReads`
* **Direct writes** (количество)
  Сумма числа прямых операций записи по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.directWrites`
* **Parse SQL calls** (количество)
  Сумма всех вызовов разбора по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.parseCalls`
* **Number of wait events** (количество)
  Общее число ожиданий события.
  Ключ метрики: `builtin:tech.oracleDb.cd.wait.count`

## FAQ

Нужен ли плагин для использования Oracle database insights?

Нет, database insights, это функция Dynatrace по умолчанию начиная с версии 1.173.

Какая модель лицензирования?

Текущий Early Access релиз database insights бесплатный, доступен с каждой версией сервера ActiveGate и Dynatrace 1.173+. В будущем цена будет зависеть от количества потребляемых метрик.

Можно ли использовать Cluster ActiveGate для Oracle database insights?

Нет. Можно использовать только Environment ActiveGate, который удалённо подключается к серверу Oracle и получает метрики и свойства каждую минуту. Поскольку Environment ActiveGate устанавливается в локальном окружении, это усиливает безопасность и минимизирует нагрузку на трафик в сети. Нужно учитывать, что основное назначение Cluster ActiveGate, это маршрутизация трафика OneAgent.

Нужно ли устанавливать OneAgent на хост Oracle?

Нет, но это рекомендуется, потому что это даёт более полную картину базы данных, сервера и всех процессов, выполняющихся на нём, а также мониторинг логов. Так можно быстрее реагировать на потенциальные проблемы и лучше понимать первопричину.