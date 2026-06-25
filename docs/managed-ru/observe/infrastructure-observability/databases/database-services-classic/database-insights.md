---
title: Аналитика базы данных Oracle
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/databases/database-services-classic/database-insights
scraped: 2026-05-12T12:06:09.060504
---

# Аналитика базы данных Oracle

# Аналитика базы данных Oracle

* How-to guide
* 13-min read
* Updated on Apr 10, 2026

Аналитика базы данных Oracle будет заменена расширениями на основе источника данных SQL. Для получения дополнительной информации см.:

* Пост в блоге о новостях продукта: [Intelligent observability for Oracle and SQL databases](https://www.dynatrace.com/news/blog/intelligent-observability-for-oracle-and-sql-databases/)
* Загрузка расширения [Oracle Database](https://www.dynatrace.com/hub/detail/oracle-database/) в Dynatrace Hub
* Как [управлять расширениями Oracle Database](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, принимаемых из Oracle Database.")
* Как расширить мониторинг Oracle SQL с помощью Extensions 2.0 [источник данных SQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Узнайте, как создать расширение на основе источника данных SQL с помощью фреймворка Extensions.")

Аналитика баз данных добавляет инфраструктурную перспективу к мониторингу баз данных. Благодаря дополнительным данным, извлечённым с уровня базы данных, можно решать проблемы производительности, уходящие корнями глубоко в базу данных, например понимать, почему конкретный оператор работает медленно.

## Принцип работы

Аналитика баз данных работает на Environment ActiveGate и подключается удалённо к базам данных Oracle. При таком подходе платформа СУБД может быть любого типа — Dynatrace поддерживает все операционные системы, используя драйвер JDBC для подключения к базам данных.

![Архитектура Oracle insights](https://cdn.bfldr.com/B686QPH3/as/6r7qkpgpjzfbhxhqhjtb8mq6/Oracle_database_insights_-_Light_Mode?auto=webp&format=png&position=1)

Архитектура Oracle insights

## Предварительные требования

Для начала работы с аналитикой баз данных для базы данных Oracle необходимо следующее:

* Environment ActiveGate версии 1.173+ установленный в режиме по умолчанию. Аналитика баз данных не поддерживает ActiveGate, настроенный для [поддержки нескольких окружений](/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Пошаговая инструкция по настройке одного Environment ActiveGate для поддержки нескольких окружений.").
* Аналитика баз данных требует 2,5 МБ оперативной памяти на конечную точку Oracle, что соответствует возможности мониторинга нескольких сотен баз данных при установке ActiveGate на экземпляр EC2 micro.
* Dynatrace Server версии 1.173+.
* Сетевое взаимодействие между ActiveGate и сервером Oracle.
* Oracle версии от 11g до 19c, включая поддержку:

  + **Oracle Multitenant**  
    Результаты мониторинга могут различаться для конечных точек на основе SID и ServiceName. Для конечных точек на основе SID Dynatrace мониторит подключения к мультитенантной контейнерной базе данных (CDB). Для конечных точек на основе ServiceName Dynatrace мониторит подключения к связанным подключаемым базам данных (PDB).
  + **Oracle RAC**  
    Dynatrace мониторит только отдельные экземпляры узлов (SID). Нельзя использовать аналитику баз данных для мониторинга кластера или отдельных узлов на основе связанного с ними сервиса базы данных.
  + **AWS Oracle RDS**
* Необязательно: OneAgent, установленный на хосте Oracle.
* Пользователь базы данных Oracle с разрешениями, перечисленными ниже.

## Разрешения Oracle

Для аналитики баз данных Oracle необходимо обеспечить следующие разрешения на сервере Oracle:

* Пользователю, подключающемуся к экземпляру БД, необходимо предоставить разрешения `CREATE SESSION` и `SELECT_CATALOG_ROLE`. Это также включает доступ к [Dynamic Performance Views](https://docs.oracle.com/database/122/CNCPT/data-dictionary-and-dynamic-performance-views.htm#CNCPT1220), который является частью разрешения `SELECT_CATALOG_ROLE`.
* Для получения планов выполнения требуется пакет `DBMS_XPLAN` с предоставленным разрешением `EXECUTE`.

Для создания пользователя для аналитики баз данных Oracle:

```
CREATE USER oracleinsights IDENTIFIED BY password



default tablespace users



temporary tablespace temp;



GRANT CREATE SESSION, SELECT_CATALOG_ROLE TO <oracleinsights>;
```

## Настройка аналитики баз данных Oracle

Настройка аналитики баз данных Oracle проста. Нужно только определить конечную точку — базу данных Oracle, к которой будет подключаться ActiveGate. Можно добавить столько баз данных с одного сервера Oracle, сколько необходимо.

1. Необязательно [Установите OneAgent](/managed/ingest-from/dynatrace-oneagent "Ознакомьтесь с важными концепциями, связанными с OneAgent, и узнайте, как установить и эксплуатировать OneAgent на различных платформах.") на хосте Oracle.
2. Выберите или установите [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate") версии 1.173+, который будет получать данные с вашего сервера Oracle. Этот ActiveGate можно использовать и для других целей. Перейдите в **Settings** > **Deployment status**, чтобы убедиться, что ActiveGate запущен и работает. Аналитика баз данных включена по умолчанию.
3. Перейдите в **Settings > Monitoring > Monitored Technologies**.
4. Найдите строку **Database Insights: Oracle** и нажмите значок карандаша для редактирования.
5. Определите конечную точку базы данных Oracle. Все поля обязательны:

   * **Oracle host**
   * **Port**: по умолчанию `1521`
   * **Connection type**: `Service` или `SID`
   * **Service/SID**: идентификатор базы данных
   * **Database user** и **Database password**: подробности см. в разделе [Разрешения Oracle](#oracle-permissions).
   * **Monitored database name**: имя базы данных, которую нужно мониторить
6. Установите флажок, чтобы принять лицензионное соглашение о перераспределении для драйвера Oracle JDBC. Dynatrace использует его для получения данных с сервера Oracle. Ваши данные защищены.
7. Нажмите **Add database**. Если Dynatrace может установить соединение, используя предоставленные данные, мониторинг базы данных Oracle начнётся автоматически.

## Включение и отключение аналитики баз данных Oracle

Для отключения или включения аналитики баз данных Oracle для каждой мониторируемой базы данных:

1. Перейдите в **Settings > Monitoring > Monitored Technologies**.
2. Найдите строку **Database Insights: Oracle** и нажмите значок карандаша для редактирования.
3. Установите переключатель **Monitoring off/on** для каждой базы данных.

## Модель мониторинга аналитики баз данных Oracle

Установка OneAgent на хосте Oracle необязательна для аналитики баз данных. Независимо от того, установлен OneAgent или нет, все метрики отображаются в разделе **Custom device**, чтобы отразить логическую структуру экземпляра сервера БД, запущенных сервисов, контейнеров и подключаемых баз данных.

Однако установка OneAgent на хосте Oracle дополняет анализ производительности сервера всеми метриками процессов ОС, отображаемых в группе процессов, разделённых по экземплярам сервера (SID) и процессам-слушателям.

## Возможности аналитики баз данных Oracle

### Наиболее ресурсоёмкие операторы Oracle

Чтобы понять и проанализировать, какие операторы Oracle наиболее затратны и наиболее часто вызываются, нажмите **View statements** в разделе **Most time-consuming Oracle statements**. На странице перечислены 100 наиболее ресурсоёмких операторов. Одним кликом можно увидеть операторы, потребляющие больше всего CPU, памяти или дискового пространства, или генерирующие наибольшее время ожидания. Анализ можно настраивать, используя до трёх метрик для анализа TopN.

### Загрузка планов выполнения

При анализе характеристик производительности SQL-оператора часто возникает необходимость сгенерировать и отобразить план выполнения SQL-оператора. Можно загрузить план выполнения Oracle прямо из пользовательского интерфейса Dynatrace.

### Метрики памяти и кэша

Аналитика баз данных Oracle предоставляет дополнительные метрики Oracle, связанные с памятью и кэшами, что позволяет определить операторы, активно использующие оперативную память.

### Data Explorer

Все метрики Oracle, получаемые аналитикой баз данных Oracle, доступны в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных аналитических данных.").

### Метрики ожидания и табличного пространства

Также доступны метрики ожидания и табличного пространства для использования в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных аналитических данных.").

### Группы процессов Oracle

Dynatrace связывает данные, полученные аналитикой баз данных Oracle, с процессами Oracle, обнаруженными OneAgent. Начиная с OneAgent версии 1.173, каждая группа процессов Oracle представляет один Oracle SID (уникальный идентификатор для каждого экземпляра Oracle DB). SID является частью имени группы процессов и извлекается из имён процессов (Unix) или описания сервиса (Windows). Процессы Oracle, не связанные с каким-либо SID, образуют группу других процессов Oracle. В неё входит процесс связи TNS Listener, поэтому весь входящий и исходящий трафик связан с этой группой.

По желанию можно изменить группы процессов базы данных Oracle и слушателей, разделив их по Oracle SID для баз данных или по имени для слушателей.

Разделение групп процессов с использованием Oracle SID

1. Перейдите в **Settings** > **Processes and containers** > **Built-in detection rules**.
2. OneAgent версии 1.231+ Выберите **Group Oracle database processes by SID**.

Группа процессов базы данных Oracle будет разделена на несколько групп процессов с именем в формате `Oracle Database <SID>`.

Разделение групп процессов по слушателю Oracle

1. Перейдите в **Settings** > **Processes and containers** > **Built-in detection rules**.
2. OneAgent версии 1.243+ Выберите **Group Oracle listener processes by name**.

Группа процессов слушателя Oracle будет разделена на несколько групп процессов с именем в формате `Oracle Listener <listener-name>`.

## Метрики

В этом разделе описаны метрики баз данных Oracle, доступные в Dynatrace:

* [Графики производительности](#performance)
* [Графики разбивки по времени](#time-breakdown)
* [Графики памяти PGA](#pga-memory)
* [Графики памяти SGA](#sga-memory)
* [Наиболее ресурсоёмкие операторы Oracle](#most-time-consuming-oracle-statements-1)
* Метрики только для API — эти метрики не отображаются в виде графиков в Dynatrace, но доступны через Dynatrace API.

### Производительность

Метрики, связанные с производительностью системы.

Примеры графиков

![Графики метрик аналитики баз данных Oracle: Производительность](https://dt-cdn.net/images/oracle-database-insights-charts-performance-844-78a438cd44.png)

Графики метрик аналитики баз данных Oracle: Производительность

#### Пропускная способность

* **Total user calls** (количество)  
  Общее количество операций входа в систему, разборов или вызовов выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.userCalls`
* **Active sessions** (количество)  
  Общее количество активных сессий, не назначенных классу ожидания Idle.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.active`

#### CPU

* **CPU background usage** (%)  
  Среднее фоновое использование CPU на ядро.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.background`
* **CPU foreground usage** (%)  
  Среднее использование CPU в режиме переднего плана на ядро.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.foreground`
* **CPU other processes** (%)  
  Среднее использование CPU другими процессами на ядро (за исключением процессов переднего и фонового планов).  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.other`
* **CPU idle** (%)  
  Средняя доступность CPU хоста на ядро.  
  Ключ метрики: `builtin:tech.oracleDb.cd.cpu.idle`

#### Диск

* **Read** (Б/мин)  
  Общий объём в байтах всех дисковых операций чтения для экземпляра базы данных, включая операции чтения приложением, резервного копирования и восстановления, а также другими утилитами.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.bytesRead`
* **Write** (Б/мин)  
  Общий объём в байтах всех дисковых операций записи для экземпляра базы данных, включая активность приложения, резервное копирование и восстановление, а также другие утилиты.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.bytesWritten`

#### Табличное пространство

* **Total space** (Б)  
  Общий размер табличного пространства.  
  Ключ метрики: `builtin:tech.oracleDb.cd.tablespaces.totalSpace`
* **Used space** (Б)  
  Общий объём использованного пространства.  
  Ключ метрики: `builtin:tech.oracleDb.cd.tablespaces.usedSpace`

#### Попадание в буферный кэш

* **Buffer cache hit** (%)  
  Представляет эффективность буферного кэша блоков данных в виде доли блоков данных, запрошенных из памяти.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.bufferCacheHit`

#### Сортировки в памяти

* **Sorts in memory** (%)  
  Процент сортировок (из предложений ORDER BY или построения индексов), выполняемых в памяти (в отличие от сортировок на диске).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sortsInMemory`

### Разбивка по времени

Метрики, связанные со временем, затраченным на различные виды деятельности.

Примеры графиков

![Графики метрик аналитики баз данных Oracle: Разбивка по времени](https://dt-cdn.net/images/oracle-database-insights-charts-time-845-1424994dec.png)

Графики метрик аналитики баз данных Oracle: Разбивка по времени

#### Общее время ожидания (все сессии)

* **Total wait time** (мкс/мин)  
  Общее время, проведённое в состоянии ожидания, за исключением класса Idle.  
  Ключ метрики: `builtin:tech.oracleDb.cd.io.wait`

#### Разбивка времени (все сессии)

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
  Время, затраченное на выполнение вызовов подключения и отключения сессий.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.connMgmt`
* **Other** (мкс/мин)  
  Время, затраченное на выполнение всех прочих видов деятельности.  
  Ключ метрики: `builtin:tech.oracleDb.cd.queries.other`

### Память PGA

Метрики, связанные с памятью Program Global Area (PGA).

Примеры графиков

![Графики метрик аналитики баз данных Oracle: PGA](https://dt-cdn.net/images/oracle-database-insights-charts-pga-840-156d0580a0.png)

Графики метрик аналитики баз данных Oracle: PGA

#### PGA, используемая для рабочих областей

* **PGA used for work areas** (%)  
  Объём выделенной памяти PGA, используемой в настоящее время рабочими областями. Позволяет определить, сколько памяти потребляют другие потребители PGA (например, PL/SQL или Java).  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.usedForWorkAreas`

#### Размер PGA

* **Allocated PGA** (Б)  
  Текущий объём памяти PGA, выделенной экземпляром. Oracle Database стремится поддерживать это значение ниже значения параметра инициализации **PGA aggregate target** (см. ниже). Однако при быстро возрастающей нагрузке на рабочие области или при низком значении целевого показателя выделенная PGA может незначительно превысить целевое значение на короткое время.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.allocated`
* **PGA aggregate target** (Б)  
  Совокупная целевая память PGA, доступная всем серверным процессам, подключённым к экземпляру.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateTarget`
* **PGA aggregate limit** (Б)  
  Ограничение совокупной памяти PGA, потребляемой экземпляром.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateLimit`

### Память SGA

Метрики, связанные с памятью System Global Area (SGA).

Примеры графиков

![Графики метрик аналитики баз данных Oracle: SGA](https://dt-cdn.net/images/oracle-database-insights-charts-sga-840-2bcd165f8e.png)

Графики метрик аналитики баз данных Oracle: SGA

#### Общий пул

* **Shared pool free** (%)  
  Объём свободной памяти системной глобальной области (SGA), доступной в общем пуле.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.cacheBuffer.sharedPoolFree`

#### Буфер журнала повторного выполнения

* **Redo size increase** (Б/мин)  
  Общий объём сгенерированных данных повторного выполнения в байтах.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoSizeIncrease`

#### Время, затраченное на буфер журнала повторного выполнения

* **Redo log space wait time** (мкс/мин)  
  Общее затраченное время ожидания запроса пространства журнала повторного выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoLogSpaceWaitTime`
* **Redo write time** (мкс/мин)  
  Общее затраченное время записи из буфера журнала повторного выполнения в текущий файл журнала повторного выполнения.  
  Ключ метрики: `builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoWriteTime`

### Наиболее ресурсоёмкие операторы Oracle

Метрики, связанные с операторами, выполнение которых занимает больше всего времени.

Чтобы просмотреть графики этих метрик для каждого оператора Oracle, нажмите **View statements** в разделе **Most time consuming Oracle statements**, затем нажмите **Details** для выбранного оператора.

#### Производительность операторов

Пример графика

![Графики метрик аналитики баз данных Oracle: Ресурсоёмкие метрики: Производительность операторов](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-statements-performance-1149-2fff80eba5.png)

Графики метрик аналитики баз данных Oracle: Ресурсоёмкие метрики: Производительность операторов

* **Elapsed time** (мкс)  
  Время, затраченное на разбор, выполнение и выборку данных при выполнении запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.elapsed`
* **Execution count** (количество)  
  Общее количество выполнений, суммированное по всем дочерним курсорам запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.executions`
* **CPU time** (мкс)  
  Время CPU, затраченное на разбор, выполнение и выборку данных при выполнении запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.cpu`
* **Wait time** (мкс)  
  Общее время ожидания события.  
  Ключ метрики: `builtin:tech.oracleDb.cd.wait.time`

#### Ожидания

Пример графика

![Графики метрик аналитики баз данных Oracle: Ресурсоёмкие метрики: Ожидания](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-waits-1229-ab8923f437.png)

Графики метрик аналитики баз данных Oracle: Ресурсоёмкие метрики: Ожидания

* **Application wait time** (мкс)  
  Затраченное время, проведённое в классе ожидания Application при выполнении запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.application`
* **Concurrency wait time** (мкс)  
  Затраченное время, проведённое в классе ожидания Concurrency при выполнении запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.concurrency`
* **Cluster wait time** (мкс)  
  Затраченное время, проведённое в классе ожидания Cluster при выполнении запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.cluster`
* **User IO wait time** (мкс)  
  Затраченное время, проведённое в классе ожидания User I/O при выполнении запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.time.userIo`

#### Сведения о выполнении

Пример графика

![Графики метрик аналитики баз данных Oracle: Ресурсоёмкие метрики: Сведения о выполнении](https://dt-cdn.net/images/oracle-database-insights-charts-consuming-execution-details-1325-02c6a82dba.png)

Графики метрик аналитики баз данных Oracle: Ресурсоёмкие метрики: Сведения о выполнении

* **All sessions** (количество)  
  Общее количество всех сессий независимо от их состояния и класса ожидания.  
  Ключ метрики: `builtin:tech.oracleDb.cd.sessions.all`
* **Executions** (количество)  
  Общее количество выполнений, суммированное по всем дочерним курсорам запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.executions`
* **Processed rows** (количество)  
  Общее количество строк, обработанных запросом.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.rowsProcessed`
* **Buffer gets** (количество)  
  Сумма буферных чтений по всем дочерним курсорам запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.bufferGets`
* **Disk reads** (количество)  
  Сумма количества дисковых чтений по всем дочерним курсорам запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.diskReads`
* **Direct writes** (количество)  
  Сумма количества прямых записей по всем дочерним курсорам запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.directWrites`
* **Parse SQL calls** (количество)  
  Сумма всех вызовов разбора для всех дочерних курсоров запроса.  
  Ключ метрики: `builtin:tech.oracleDb.cd.slow.parseCalls`
* **Number of wait events** (количество)  
  Общее количество ожиданий события.  
  Ключ метрики: `builtin:tech.oracleDb.cd.wait.count`

## Часто задаваемые вопросы

Нужен ли плагин для использования аналитики баз данных Oracle?

Нет, аналитика баз данных является стандартной функцией Dynatrace начиная с версии 1.173.

Какова модель лицензирования?

Текущий выпуск аналитики баз данных в режиме раннего доступа является бесплатным и доступен с каждым ActiveGate и сервером Dynatrace версии 1.173+. В будущем цена будет основана на количестве потребляемых метрик.

Можно ли использовать Cluster ActiveGate для аналитики баз данных Oracle?

Нет. Можно использовать только Environment ActiveGate, который удалённо подключается к серверу Oracle и получает метрики и свойства каждую минуту. Поскольку Environment ActiveGate устанавливается в локальной среде, это повышает безопасность и минимизирует нагрузку на трафик в сети. Обратите внимание, что основным назначением Cluster ActiveGate является маршрутизация трафика OneAgent.

Нужно ли устанавливать OneAgent на хосте Oracle?

Нет, но это рекомендуется, поскольку это даёт более полную картину базы данных, сервера и всех запущенных на нём процессов, а также мониторинга журналов. Так можно быстрее реагировать на потенциальные проблемы и лучше понимать их первопричины.