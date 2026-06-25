---
title: Справочник по источнику данных SQL
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference
scraped: 2026-05-12T12:08:31.052886
---

# Справочник по источнику данных SQL

# Справочник по источнику данных SQL

* Справочник
* Чтение: 9 мин
* Обновлено 18 марта 2026 г.

Это общее описание YAML-файла расширения на основе источника данных SQL и способов объявления метрик и измерений, которые нужно собирать с помощью расширения.

## Безопасность расширений

Несмотря на то что платформа Extensions является безопасной, безопасность расширений также зависит от того, как вы их разрабатываете и управляете ими в среде Dynatrace.

При разработке пользовательских SQL-расширений рекомендуется следующее:

* Используйте выделенного пользователя базы данных с разрешениями только на чтение в конфигурации мониторинга, чтобы предотвратить непреднамеренные изменения в базе данных. Пользователю не должны предоставляться права администратора или системные права.

### Меры безопасности

* Доступны только запросы `SELECT`

  + Запросы MySQL также могут начинаться с `SHOW GLOBAL STATUS`
* Одновременно может выполняться только один запрос
* Запросы, содержащие комментарии, отклоняются
* Чтобы предотвратить нарушения целостности данных (манипулирование, изменение или удаление данных), источник данных SQL выполняет запросы в транзакциях с откатом. По этой причине базы данных, не поддерживающие транзакции, не поддерживаются в качестве источника данных SQL.
* Убедитесь, что строка подключения в конфигурации мониторинга JDBC не раскрывает конфиденциальные данные. Дополнительные сведения см. в разделе [Конфигурация мониторинга JDBC](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "Расширения JDBC в платформе Extensions framework.").

## Область данных

Составьте перечень данных, которые нужно запрашивать из базы данных в качестве источника значений метрик и измерений.

В этом примере создаётся простое расширение, собирающее основные сведения о производительности ЦП из Oracle Database.

```
name: com.dynatrace.extension.sql-oracle



version: 1.0



minDynatraceVersion: '1.239'



author:



name: Dynatrace



sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query: >



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge



- group: Background CPU Usage Per CPU Per Sec



featureSet: cpu



query: >



SELECT



DECODE(metric_name, 'Background CPU Usage Per Sec',



v$metric.value) AS background_cpu_usage,



DECODE(metric_name, 'CPU Usage Per Sec',



v$metric.value) AS foreground_cpu_usage,



DECODE(metric_name, 'Host CPU Usage Per Sec',



v$metric.value) AS host_cpu_usage



FROM v$metric,



v$metricgroup



WHERE v$metric.group_id = v$metricgroup.group_id



AND v$metric.metric_name IN ('Background CPU Usage Per Sec',



'CPU Usage Per Sec', 'Host CPU Usage Per Sec')



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.backgroundTotal



value: col:background_cpu_usage



type: gauge



- key: com.dynatrace.extension.sql-oracle.cpu.foregroundTotal



value: col:foreground_cpu_usage



type: gauge



- key: com.dynatrace.extension.sql-oracle.cpu.hostTotal



value: col:host_cpu_usage



type: gauge
```

В зависимости от провайдера определение области мониторинга SQL начинается с выделенного YAML-узла. Для Oracle Database это `sqloracle`. Все параметры под этим узлом относятся к объявленному [типу источника данных](/managed/ingest-from/extensions/concepts#data-source-type "Подробнее о концепции Dynatrace Extensions.") (в данном случае SQL).

## Коннектор JDBC

Источник данных SQL платформы Dynatrace Extensions позволяет запрашивать любую базу данных, поддерживающую подключения через драйвер JDBC, в дополнение ко всем поставщикам баз данных, поддерживаемым по умолчанию. Для таких баз данных требуются дополнительные шаги.

### Объявление подключения JDBC в YAML-файле расширения

1. Начните определение расширения с узла `jdbc`.
2. Объявите имя класса драйвера. Например, `org.mariadb.jdbc.Driver`.
3. Укажите шаблон строки подключения и сообщение проверки. Они будут использоваться для проверки строки подключения, указанной пользователем в конфигурации мониторинга.
4. Укажите самый простой запрос, который расширение будет выполнять для проверки подключения.

```
jdbc:



driverClassName: “org.mariadb.jdbc.Driver”



connectionStringPattern: “jdbc:mariadb:(. |\\s)+$"



connectionStringPatternErrorMessage: “This isn't a correct connection string, please start with jdbc:mariadb."



validationQuery: “SELECT 1”
```

Пользователям, запускающим расширение, также потребуется загрузить соответствующий драйвер JDBC на ActiveGate, входящий в группу, предназначенную для запуска расширения. Дополнительные сведения см. в разделе [Конфигурация мониторинга JDBC](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring#upload "Расширения JDBC в платформе Extensions framework.").

## SQL-запросы

SQL-расширения основаны на SQL-запросах. Запросы, объявленные в расширении, извлекают значения для метрик и измерений. Чтобы сопоставить результаты запроса с метрикой, тип столбца должен быть числовым. Если он не числовой, необходимо привести его к числовому типу.

Например, следующий SQL-запрос возвращает количество ядер ЦП.

```
SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'
```

Его можно использовать в расширении и передавать значение, возвращаемое запросом, как метрику `com.dynatrace.extension.sql-oracle.cpu.cores` в Dynatrace.

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

По соображениям безопасности источник данных поддерживает только подмножество языка SQL. Подробные сведения см. в разделе [Меры безопасности](#security-controls).

## SQL-запросы с версионированием

ActiveGate версии 1.335+

Некоторые SQL-запросы допустимы только для определённых версий баз данных. Чтобы расширение было совместимо с различными версиями баз данных, можно объявить запросы для конкретных версий.

Версионированные запросы объявляются в узле `queriesVersioned`. Для каждого версионированного запроса можно определить `query` и требуемый `minDBVersion`. Если версия базы данных соответствует нескольким запросам для конкретной версии, будет выполнен запрос с наибольшим значением `minDBVersion`, которое не превышает версию базы данных (или равно ей).

Если ни один версионированный запрос не соответствует версии базы данных или версионированные запросы не объявлены, для всех версий баз данных выполняется обычный `query`, определённый для группы.

```
sqlOracle:



- group: Data Guard processes



featureSet: dataguard



query:



SELECT PROCESS, STATUS



FROM V$MANAGED_STANDBY



queriesVersioned:



- minDBVersion: "12.2"



query: |



SELECT NAME, TYPE, PID, STATUS



FROM V$DATAGUARD_PROCESS



- minDBVersion: "10.0"



query: |



SELECT PROCESS, STATUS



FROM V$MANAGED_STANDBY
```

## Частота запросов

Можно задать частоту, с которой выполняется опрос поставщика базы данных. Если частота не задана, поставщик базы данных опрашивается каждую минуту по умолчанию.

Для управления временем опроса поставщика базы данных можно использовать одно из двух взаимоисключающих свойств: `interval` или `schedule`. Их можно определить на уровне группы или подгруппы.

### Interval

ActiveGate версии 1.253+

Значение интервала принимает целое число, выражающее минуты. Например, чтобы опрашивать поставщик базы данных каждые 10 минут, добавьте следующую запись:

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



interval:



minutes: 10



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

### Schedule

ActiveGate версии 1.301+

Для опроса поставщика базы данных по выбранному расписанию можно использовать выражение cron.

Выражение должно соответствовать формату cron Unix:

```
# * * * * *



# | | | | |



# | | | | day of the week (1–7) (Sunday to Saturday)



# | | | month (1–12)



# | | day of the month (1–31)



# | hour (0–23)



# minute (0–59)
```

Значения также поддерживают списки (`1,2,3,4`), шаги (`0-23/2`) и диапазоны (`2-5`).

Формат не поддерживает одновременное указание дня недели и дня месяца. В одном из этих полей необходимо использовать символ «?».

Например, чтобы выполнять запрос в 12:00 каждый рабочий день (с понедельника по пятницу), используйте следующую запись:

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



schedule: "0 12 ? * 2-6"



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

### Предоставление пользователям расширения управления частотой

ActiveGate версии 1.303+

Если нужно разрешить пользователям расширения управлять частотой опроса поставщика базы данных, можно использовать переменные вместо фиксированных значений. Пользователи смогут задать значение переменной при активации расширений.

Подробно опишите контекст переменной, чтобы пользователи понимали, как правильно задать её значение. Также можно задать шаблон для проверки введённых пользователями значений.

Например, чтобы предоставить пользователю управление интервалом:

1. Сначала объявите переменную в YAML-файле расширения:

   ```
   vars:



   - id: myInterval



   displayName: Interval



   description: Interval at which your database provider is queried in minutes. 10 minutes by default.



   defaultValue: "10"



   pattern: ^[0-9]+$



   type: text
   ```
2. Затем укажите ссылку на переменную вместо фиксированного значения в YAML-файле расширения:

   ```
   sqlOracle:



   - group: Number of CPU cores



   interval:



   minutes: var:myInterval



   featureSet: cpu



   query:



   SELECT value AS cpu_count



   FROM v$parameter



   WHERE name = 'cpu_count'



   metrics:



   - key: com.dynatrace.extension.sql-oracle.cpu.cores



   value: col:cpu_count



   type: gauge
   ```

   Дополнительные сведения об использовании переменных см. в разделе [YAML-файл расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#variables "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.")

## Тайм-ауты

При разработке расширения для заданного запроса можно указать значение тайм-аута как на уровне группы, так и на уровне подгруппы. Тайм-ауты указываются в секундах; значение по умолчанию: `10`. Указанное значение должно быть строкой, например: `20`, `60`, `120` и т. д.

Также для указания тайм-аута можно использовать ссылку на переменную. Дополнительные сведения об использовании переменных см. в разделе [YAML-файл расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#variables "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.").

```
sqlOracle:



- group: Number of CPU cores



timeout: "20"



featureSet: cpu



query: |



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

Важные аспекты при настройке тайм-аутов

Указание пользовательского тайм-аута для запроса изменяет способ его выполнения источником данных. По умолчанию все запросы выполняются последовательно, поэтому источнику данных требуется только одно подключение к базе данных. При определённом пользовательском тайм-ауте запрос будет выполняться параллельно, открывая дополнительное подключение к базе данных. Это означает, что при добавлении пользовательских тайм-аутов необходимо следить за тем, чтобы расширение не открывало слишком много подключений.

## Измерения

Для каждого уровня (расширение, группа, подгруппа) можно определить до 25 измерений.

Подгруппа наследует измерения родительской группы. Чтобы обеспечить распространение данных, при наличии определённого запроса в родительской группе подгруппа выполнит свой запрос после завершения первого выполнения запроса родительской группы.

### Ключ измерения

Строка ключа измерения должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

### Значение измерения

Для получения значения измерения используется SQL-запрос (с префиксом `col:`) или фиксированная строка (с префиксом `const:`). Например:

```
query: >



SELECT event, wait_class



FROM v$system_event



dimensions:



- key: event



value: col:event



- key: wait_class



value: col:wait_class



- key: stage



value: const:dev
```

### Фильтрация извлечённых строк метрик

ActiveGate версии 1.311+

На уровне измерения можно добавить логику фильтрации. В результате будет передаваться только та метрика, значение измерения которой соответствует критериям фильтрации.
Если фильтры установлены для нескольких измерений, для создания строки метрики все фильтры должны совпасть. Логика фильтрации не изменяет выполняемый запрос.

Фильтры можно задать как константное значение или как [переменную](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#variables "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.").

```
dimensions:



- key: event



value: col:event



filter: var:event_filter



- key: wait_class



value: col:wait_class



filter: const:$not(0)



- key: stage



value: const:dev
```

Определите фильтр на основе условия следующим образом:

* **Starts with**: используйте квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Ends with**: используйте квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Contains**: используйте квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Equals**: используйте квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для перечисленных выше выражений также можно использовать следующие квалификаторы:

  + `const:$and`: объединение двух или более выражений с помощью оператора AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or`: объединение двух или более выражений с помощью оператора OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not`: отрицание выражения. Пример:

    ```
    filter: const:$not(<expr>)
    ```

## Метрики

Для каждого уровня (расширение, группа, подгруппа) можно определить до 100 метрик.

Например:

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

### Ключ метрики

Строка ключа метрики должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

Для Dynatrace версий 1.215 и 1.217 узел метрики требует параметра `id` вместо `key`. Начиная с Dynatrace версии 1.219 следует использовать параметр `key`, поскольку `id` считается устаревшим.

#### Рекомендации по ключам метрик

Метрики, принимаемые в Dynatrace с помощью расширения, являются лишь частью тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Чтобы ключи метрик были уникальными и легко идентифицировались в Dynatrace, рекомендуется добавлять к имени метрики имя расширения в качестве префикса. Это гарантирует уникальность ключа метрики и возможность легко связать метрику с конкретным расширением в среде.

### Значение метрики

Значение столбца, запрошенное из базы данных.

### Тип

Платформа Dynatrace Extensions поддерживает полезные нагрузки метрик в форматах gauge (`gauge`) или count (`count`). Подробные сведения см. в разделе [Полезная нагрузка метрики](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API."). Для указания типа метрики используйте атрибут `type`.

## Метаданные метрики

Расширение может определять метаданные для каждой метрики, доступной в Dynatrace. Например, можно добавить отображаемое имя метрики и единицу измерения, которые можно использовать для фильтрации в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в обозревателе метрик Dynatrace.").

Определите все метаданные метрик в разделе `metrics` YAML-файла расширения, чтобы они были правильно связаны с конфигурацией метрики.

```
name: custom:example-extension-name



version: 1.0.0



minDynatraceVersion: "1.236"



author:



name: Dynatrace



metrics:



- key: your.metric.name



metadata:



displayName: Display name of the metric visible in Metrics browser



unit: Count
```

## Набор функций

Наборы функций, это категории, по которым организуются данные, собираемые расширением. В этом примере создаётся расширение Oracle SQL, собирающее метрики, связанные с производительностью ЦП и операций ввода/вывода. Это отражено в организации метрик по соответствующим наборам функций `cpu` и `io`.

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge



- group: Physical read bytes



featureSet: io



query: >



SELECT



DECODE(name, 'physical read total bytes', value) AS bytes_written,



DECODE(name, 'physical write total bytes', value) AS bytes_read



FROM v$sysstat



WHERE name IN ('physical read total bytes', 'physical write total bytes')



metrics:



- key: com.dynatrace.extension.sql-oracle.io.bytesRead



value: col:bytes_read



type: count



- key: com.dynatrace.extension.sql-oracle.io.bytesWritten



value: col:bytes_written



type: count
```

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) мониторинг можно ограничить одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут отражать сегменты среды. Затем при создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, которая может подключиться к этому конкретному сегменту.

Все метрики, не отнесённые ни к одному набору функций, считаются заданными по умолчанию и всегда передаются.

Метрика наследует набор функций подгруппы, которая, в свою очередь, наследует набор функций группы. Кроме того, набор функций, определённый на уровне метрики, переопределяет набор функций, определённый на уровне подгруппы, который, в свою очередь, переопределяет набор функций, определённый на уровне группы.

## Конфигурация мониторинга Oracle SQL

После определения области конфигурации необходимо указать сетевые устройства, из которых нужно собирать данные, и ActiveGate, которые будут выполнять расширение и подключаться к устройствам.

Формат конфигурации мониторинга зависит от поставщика базы данных. Дополнительные сведения см. в разделе [Конфигурация мониторинга Oracle Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Создайте и активируйте конфигурацию мониторинга для расширения на основе источника данных SQL для Oracle Database.").