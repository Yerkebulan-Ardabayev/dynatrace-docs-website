---
title: Oracle database insights
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/database-services-classic/database-insights
---

# Oracle database insights

# Oracle database insights

* Практическое руководство
* Чтение 13 мин
* Обновлено 10 апр. 2026 г.
* Будет объявлено устаревшим

Oracle database insights заменяется расширениями на основе SQL data source. Подробнее см.:

* Блог о новостях продукта: [Intelligent observability for Oracle and SQL databases﻿](https://www.dynatrace.com/news/blog/intelligent-observability-for-oracle-and-sql-databases/)
* Загрузка расширения [Oracle Database﻿](https://www.dynatrace.com/hub/detail/oracle-database/) в Dynatrace Hub
* Как [управлять расширениями Oracle Database](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")
* Как расширить мониторинг Oracle SQL с помощью [SQL data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.") Extensions 2.0

Database insights добавляет инфраструктурный ракурс к мониторингу базы данных. С дополнительными данными, получаемыми с уровня базы данных, можно устранять проблемы производительности, коренящиеся глубоко в базе данных, например, понять, почему конкретный оператор выполняется медленно.

## Как это работает

Database insights работает на Environment ActiveGate и подключается удалённо к базам данных Oracle. При таком подходе платформа системы базы данных может быть любого типа: Dynatrace поддерживает все операционные системы, используя JDBC-драйвер для подключения к базам данных.

![Oracle insights architecture](https://cdn.bfldr.com/B686QPH3/as/6r7qkpgpjzfbhxhqhjtb8mq6/Oracle_database_insights_-_Light_Mode?auto=webp&format=png&position=1)

Архитектура Oracle insights

## Предварительные требования

Для начала работы с database insights для базы данных Oracle нужно следующее:

* Environment ActiveGate версии 1.173+, установленный в режиме по умолчанию. Database insights не поддерживает ActiveGate, настроенный для [поддержки нескольких сред](/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.").
* Database insights требует 2,5 МБ ОЗУ на каждую конечную точку базы данных Oracle, что соответствует возможности мониторинга нескольких сотен баз данных при установке ActiveGate на инстансе EC2 micro.
* Dynatrace Server версии 1.173+.
* Сетевое взаимодействие между ActiveGate и Oracle Server.
* Oracle версии от 11g до 19c, включая поддержку:

  + **Oracle Multitenant**  
    Результаты мониторинга могут отличаться для конечных точек на основе SID и на основе ServiceName. Для конечных точек на основе SID Dynatrace отслеживает подключения к многоарендной контейнерной базе данных (CDB). Для конечных точек на основе ServiceName Dynatrace отслеживает подключения к связанным подключаемым базам данных (PDB).
  + **Oracle RAC**  
    Dynatrace отслеживает только отдельные экземпляры узлов (SID). Database insights нельзя использовать для мониторинга кластера или для мониторинга отдельных узлов на основе службы базы данных, с которой они связаны.
  + **AWS Oracle RDS**
* Опционально OneAgent, установленный на хосте Oracle.
* Пользователь базы данных Oracle с разрешениями, перечисленными ниже.

## Разрешения Oracle

Для Oracle database insights на сервере Oracle нужно выполнить следующие требования по разрешениям:

* Пользователю, который подключается к экземпляру БД, нужно предоставить разрешения `CREATE SESSION` и `SELECT_CATALOG_ROLE`. Это также означает доступ к [Dynamic Performance Views﻿](https://docs.oracle.com/database/122/CNCPT/data-dictionary-and-dynamic-performance-views.htm#CNCPT1220), который является частью разрешения `SELECT_CATALOG_ROLE`.
* Для получения планов выполнения требуется пакет `DBMS_XPLAN` с предоставленным разрешением `EXECUTE`.

Чтобы создать пользователя для Oracle database insights:

```
CREATE USER oracleinsights IDENTIFIED BY password



default tablespace users



temporary tablespace temp;



GRANT CREATE SESSION, SELECT_CATALOG_ROLE TO <oracleinsights>;
```

## Настройка Oracle database insights

Настройка Oracle database insights несложная. Всё, что нужно сделать, это определить конечную точку, базу данных Oracle, к которой будет подключаться ActiveGate. Можно добавить сколько угодно баз данных с одного сервера Oracle.

1. Опционально [установить OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") на хосте Oracle.
2. Выбрать или установить и [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") версии 1.173+, который будет получать данные с сервера Oracle. Этот ActiveGate можно использовать и для других целей. Перейти в **Settings** > **Deployment status**, чтобы проверить, работает ли ActiveGate. Database insights по умолчанию включён.
3. Перейти в **Settings > Monitoring > Monitored Technologies**.
4. Найти строку **Database Insights: Oracle** и нажать значок карандаша, чтобы её редактировать.
5. Определить конечную точку базы данных Oracle. Все поля обязательны:

   * **Oracle host**
   * **Port**: по умолчанию = `1521`
   * **Connection type**: `Service` или `SID`
   * **Service/SID**: идентификатор базы данных
   * **Database user** и **Database password**: подробнее см. раздел [Разрешения Oracle](#oracle-permissions).
   * **Monitored database name**: имя базы данных, которую нужно отслеживать
6. Установить флажок, чтобы принять лицензионное соглашение о распространении для JDBC-драйвера Oracle. Dynatrace использует его для получения данных с сервера Oracle. Данные защищены.
7. Выбрать **Add database**. Если Dynatrace сможет установить соединение по указанным данным, Dynatrace начнёт отслеживать базу данных Oracle.

## Включение и отключение Oracle database insights

Чтобы отключить или включить Oracle database insights для каждой отслеживаемой базы данных

1. Перейти в **Settings > Monitoring > Monitored Technologies**.
2. Найти строку **Database Insights: Oracle** и нажать значок карандаша, чтобы её редактировать.
3. Установить переключатель **Monitoring off/on** для каждой базы данных.

## Модель мониторинга Oracle database insights

Установка OneAgent на хосте Oracle для database insights опциональна. Независимо от того, установлен он или нет, все метрики отображаются под **Custom device**, отражая логическую структуру инстанса сервера БД, работающих служб, контейнеров и подключённых баз данных.

Однако установка OneAgent на хосте Oracle дополняет анализ производительности сервера всеми метриками процессов ОС, которые сообщаются для группы процессов и их экземпляров, разделённых по экземплярам сервера (SID) и процессам listener.

## Возможности Oracle database insights

### Самые затратные по времени операторы Oracle

Чтобы понять и проанализировать, какие операторы Oracle являются самыми затратными и наиболее часто вызываемыми, выбрать **View statements** в разделе **Most time-consuming Oracle statements**. На странице перечислены 100 самых затратных по времени операторов. Одним щелчком можно увидеть операторы, потребляющие больше всего CPU, памяти или дискового хранилища, или создающие наибольшее время ожидания. Анализ можно настраивать, используя до трёх метрик, доступных для TopN-анализа.

### Загрузка планов выполнения

При анализе характеристик производительности SQL-оператора часто возникает необходимость сформировать и отобразить план выполнения этого SQL-оператора. План выполнения Oracle можно скачать прямо из интерфейса Dynatrace.

### Метрики памяти и кэша

Oracle database insights предоставляет дополнительные метрики Oracle, связанные с памятью и кэшами, что позволяет точно определить операторы, интенсивно использующие ОЗУ.

### Data Explorer

Все метрики Oracle, получаемые Oracle database insights, доступны в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

### Метрики ожидания и табличного пространства

Также можно обращаться к метрикам ожидания и табличного пространства, доступным для использования в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

### Группы процессов Oracle

Dynatrace связывает данные, получаемые Oracle database insights, с процессами Oracle, обнаруженными OneAgent. Начиная с версии OneAgent 1.173, каждая группа процессов Oracle представляет один Oracle SID (уникальный идентификатор для каждого инстанса БД Oracle). SID является частью имени группы процессов и извлекается из имён процессов (Unix) или описания службы (Windows). Процессы Oracle, не связанные ни с одним SID, образуют группу прочих процессов Oracle. Сюда входит процесс связи TNS Listener, поэтому весь входящий и исходящий трафик связан с этой группой.

Опционально можно изменить группы процессов базы данных Oracle и listener, разделив их по Oracle SID для баз данных или по имени для listener.

Разделение групп процессов по Oracle SID

1. Перейти в **Settings** > **Processes and containers** > **Built-in detection rules**.
2. Версия OneAgent 1.231+ Выбрать **Group Oracle database processes by SID**.

Группа процессов базы данных Oracle будет разделена на несколько групп процессов с именем в формате `Oracle Database <SID>`.

Разделение групп процессов по Oracle listener

1. Перейти в **Settings** > **Processes and containers** > **Built-in detection rules**.
2. Версия OneAgent 1.243+ Выбрать **Group Oracle listener processes by name**.

Группа процессов listener Oracle будет разделена на несколько групп процессов с именем в формате `Oracle Listener <listener-name>`.

## Метрики

В этом разделе описываются метрики базы данных Oracle, доступные через Dynatrace:

* [Графики производительности](#performance)
* [Графики распределения времени](#time-breakdown)
* [Графики памяти PGA](#pga-memory)
* [Графики памяти SGA](#sga-memory)
* [Наиболее затратные по времени операторы Oracle](#most-time-consuming-oracle-statements-1)
* Метрики только API, эти метрики не отображаются на графиках в Dynatrace, но доступны через API Dynatrace.

### Производительность

Метрики, касающиеся производительности системы.

Примеры графиков

![Oracle database insights metrics charts: Performance](https://dt-cdn.net/images/oracle-database-insights-charts-performance-844-78a438cd44.png)

Oracle database insights metrics charts: Performance

#### Пропускная способность

* **Total user calls** (количество)  
  Общее число входов в систему, разборов запросов или вызовов выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.userCalls`
* **Active sessions** (количество)  
  Общее число активных сессий, не отнесённых к классу ожидания Idle.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.active`

#### CPU

* **CPU background usage** (%)  
  Среднее использование CPU фоновыми процессами на одно ядро CPU.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.background`
* **CPU foreground usage** (%)  
  Среднее использование CPU процессами переднего плана на одно ядро CPU.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.foreground`
* **CPU other processes** (%)  
  Среднее использование CPU прочими процессами на одно ядро CPU (не считая процессов переднего плана и фоновых процессов).  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.other`
* **CPU idle** (%)  
  Средняя доступность CPU хоста на одно ядро CPU.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.idle`

#### Диск

* **Read** (Б/мин)  
  Общий размер в байтах всех операций чтения с диска для экземпляра базы данных, включая чтение приложениями, резервное копирование и восстановление, а также другие утилиты.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.bytesRead`
* **Write** (Б/мин)  
  Общий размер в байтах всех операций записи на диск для экземпляра базы данных, включая активность приложений, резервное копирование и восстановление, а также другие утилиты.  
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
  Отражает эффективность буферного кэша блоков данных, как долю блоков данных, необходимых в памяти.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.bufferCacheHit`

#### Сортировки в памяти

* **Sorts in memory** (%)  
  Процент сортировок (из предложений ORDER BY или построения индексов), выполняемых в памяти (в отличие от сортировок на диске).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sortsInMemory`

### Распределение времени

Метрики, касающиеся времени, затраченного на различные виды деятельности.

Примеры графиков

![Oracle database insights metrics charts: Time breakdown](https://dt-cdn.net/images/oracle-database-insights-charts-time-845-1424994dec.png)

Oracle database insights metrics charts: Time breakdown

#### Общее время ожидания (все сессии)

* **Total wait time** (мкс/мин)  
  Общее время, проведённое во всех состояниях ожидания, кроме класса Idle.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.wait`

#### Распределение затраченного времени (все сессии)

* **SQL parse** (мкс/мин)  
  Время, затраченное на разбор SQL-операторов.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.sqlParse`
* **SQL execution** (мкс/мин)  
  Время, затраченное на выполнение SQL-операторов.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.sqlExec`
* **PL/SQL execution** (мкс/мин)  
  Время, затраченное на работу интерпретатора PL/SQL.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.plSqlExec`
* **Connection management** (мкс/мин)  
  Время, затраченное на выполнение вызовов подключения и отключения сессии.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.connMgmt`
* **Other** (мкс/мин)  
  Время, затраченное на выполнение всех прочих операций.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.other`

### Память PGA

Метрики, касающиеся памяти Program Global Area (PGA).

Примеры графиков

![Oracle database insights metrics charts: PGA](https://dt-cdn.net/images/oracle-database-insights-charts-pga-840-156d0580a0.png)

Oracle database insights metrics charts: PGA

#### PGA, используемая для рабочих областей

* **PGA used for work areas** (%)  
  Объём выделенной памяти PGA, потребляемой в текущий момент рабочими областями. Может использоваться для определения того, сколько памяти потребляется другими потребителями памяти PGA (например, PL/SQL или Java).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.usedForWorkAreas`

#### Размер PGA

* **Allocated PGA** (Б)  
  Текущий объём памяти PGA, выделенной экземпляром. Oracle Database стремится удерживать это значение ниже значения параметра инициализации **PGA aggregate target** (см. ниже). Тем не менее, выделенная PGA может превышать целевое значение на небольшой процент и в течение короткого периода времени, когда нагрузка рабочих областей растёт очень быстро или когда целевое значение низкое.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.allocated`
* **PGA aggregate target** (Б)  
  Целевой суммарный объём памяти PGA, доступный всем серверным процессам, подключённым к экземпляру.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateTarget`
* **PGA aggregate limit** (Б)  
  Предел суммарного объёма памяти PGA, потребляемой экземпляром.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateLimit`

### Память SGA

Метрики, касающиеся памяти System Global Area (SGA).

Примеры графиков

![Oracle database insights metrics charts: SGA](https://dt-cdn.net/images/oracle-database-insights-charts-sga-840-2bcd165f8e.png)

Oracle database insights metrics charts: SGA

#### Общий пул (Shared pool)

* **Shared pool free** (%)  
  Объём свободной памяти системной глобальной области (SGA), доступной в общем пуле.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.cacheBuffer.sharedPoolFree`

#### Буфер журнала повторного выполнения (Redo log buffer)

* **Redo size increase** (Б/мин)  
  Общий объём сгенерированных данных повторного выполнения в байтах.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoSizeIncrease`

#### Время, затраченное на буфер журнала повторного выполнения

* **Redo log space wait time** (мкс/мин)  
  Общее истёкшее время ожидания запроса на пространство журнала повторного выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoLogSpaceWaitTime`
* **Redo write time** (мкс/мин)  
  Общее истёкшее время записи из буфера журнала повторного выполнения в текущий файл журнала повторного выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoWriteTime`

### Наиболее ресурсоёмкие Oracle-выражения

Метрики выражений, требующих наибольшего времени выполнения.

Чтобы посмотреть графики этих метрик по конкретному Oracle-выражению, нужно выбрать **View statements** в разделе **Most time consuming Oracle statements**, а затем выбрать **Details** для нужного выражения.

#### Statements performance

Пример графика

![Oracle database insights metrics charts: Time-consuming metrics: Statements performance](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-statements-performance-1149-2fff80eba5.png)

Oracle database insights metrics charts: Time-consuming metrics: Statements performance

* **Elapsed time** (μs)
  Время, затраченное во время выполнения запроса на разбор (parsing), выполнение и получение данных (fetching).
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.elapsed`
* **Execution count** (count)
  Общее число выполнений, просуммированное по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.executions`
* **CPU time** (μs)
  Время CPU, затраченное во время выполнения запроса на разбор, выполнение и получение данных.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.cpu`
* **Wait time** (μs)
  Суммарное время ожидания события.
  Ключ метрики: `builtin:tech.oracleDb.cd.wait.time`

#### Waits

Пример графика

![Oracle database insights metrics charts: Time-consuming metrics: Waits](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-waits-1229-ab8923f437.png)

Oracle database insights metrics charts: Time-consuming metrics: Waits

* **Application wait time** (μs)
  Время, прошедшее во время выполнения запроса в классе ожидания application.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.application`
* **Concurrency wait time** (μs)
  Время, прошедшее во время выполнения запроса в классе ожидания concurrency.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.concurrency`
* **Cluster wait time** (μs)
  Время, прошедшее во время выполнения запроса в классе ожидания cluster.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.cluster`
* **User IO wait time** (μs)
  Время, прошедшее во время выполнения запроса в классе ожидания user I/O.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.userIo`

#### Execution details

Пример графика

![Oracle database insights metrics charts: Time-consuming metrics: Execution details](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-execution-details-1325-02c6a82dba.png)

Oracle database insights metrics charts: Time-consuming metrics: Execution details

* **All sessions** (count)
  Общее число всех сессий независимо от их состояния и класса ожидания.
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.all`
* **Executions** (count)
  Общее число выполнений, просуммированное по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.executions`
* **Processed rows** (count)
  Общее число строк, обработанных запросом.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.rowsProcessed`
* **Buffer gets** (count)
  Сумма buffer gets по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.bufferGets`
* **Disk reads** (count)
  Сумма числа операций чтения с диска по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.diskReads`
* **Direct writes** (count)
  Сумма числа прямых записей по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.directWrites`
* **Parse SQL calls** (count)
  Сумма всех вызовов разбора (parse calls) по всем дочерним курсорам запроса.
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.parseCalls`
* **Number of wait events** (count)
  Общее число ожиданий события.
  Ключ метрики: `builtin:tech.oracleDb.cd.wait.count`

## FAQ

Нужен ли плагин для использования Oracle database insights?

Нет, database insights, это функция Dynatrace по умолчанию начиная с версии 1.173.

Какая модель лицензирования?

Текущий Early Access релиз database insights бесплатен и доступен с любой версией сервера ActiveGate и Dynatrace 1.173+. В будущем цена будет основана на числе потребляемых метрик.

Можно ли использовать Cluster ActiveGate для Oracle database insights?

Нет. Можно использовать только Environment ActiveGate, который удалённо подключается к серверу Oracle и получает метрики и свойства каждую минуту. Поскольку Environment ActiveGate устанавливается в локальной среде, это усиливает безопасность и минимизирует нагрузку на трафик в сети. Стоит учитывать, что основное назначение Cluster ActiveGate, это маршрутизация трафика OneAgent.

Нужно ли устанавливать OneAgent на хост Oracle?

Нет, но это рекомендуется, поскольку так можно получить более полную картину базы данных, сервера и всех процессов, запущенных на нём, включая мониторинг логов. Благодаря этому реагировать на потенциальные проблемы можно быстрее, а первопричину понимать лучше.