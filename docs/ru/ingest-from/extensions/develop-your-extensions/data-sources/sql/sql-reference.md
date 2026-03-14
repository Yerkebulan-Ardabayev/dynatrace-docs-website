---
title: Справочник источника данных SQL
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference
scraped: 2026-03-01T21:14:57.566228
---

# Справочник по источнику данных SQL


* Latest Dynatrace
* Справочник
* Время чтения: 9 мин
* Обновлено 10 ноября 2025 г.

Это общее описание YAML-файла расширения на основе источника данных SQL и способов объявления метрик и измерений, которые вы хотите собирать с помощью вашего расширения.

## Безопасность расширений

Хотя фреймворк расширений безопасен, безопасность ваших расширений также зависит от того, как вы их разрабатываете и управляете ими в среде Dynatrace.

При разработке пользовательских SQL-расширений мы рекомендуем следующее:

* Используйте выделенного пользователя базы данных с правами только на чтение в конфигурации мониторинга, чтобы предотвратить непреднамеренные изменения в базе данных. Администраторские или системные привилегии не должны предоставляться пользователю.

### Средства контроля безопасности

* Доступны только запросы `SELECT`

  + Запросы MySQL также могут начинаться с `SHOW GLOBAL STATUS`
* Одновременно может выполняться только один запрос
* Запросы, содержащие комментарии, отклоняются
* Для предотвращения нарушений целостности данных (манипулирование, изменение или удаление данных) источник данных SQL выполняет запросы в откатываемых транзакциях. По этой причине базы данных, не поддерживающие транзакции, не поддерживаются в качестве источника данных SQL.
* Убедитесь, что строка подключения, используемая в конфигурации мониторинга JDBC, не раскрывает конфиденциальных данных. Подробнее см. [Конфигурация мониторинга JDBC](jdbc-monitoring.md "Расширения JDBC в фреймворке расширений.").

## Область данных

Создайте инвентаризацию данных, которые вы хотите запрашивать из базы данных, в качестве источника значений метрик и измерений.

В нашем примере мы создаём простое расширение, собирающее основные данные о производительности CPU из базы данных Oracle Database.

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

В зависимости от провайдера, определение области мониторинга SQL начинается с выделенного узла YAML. Для Oracle Database это `sqloracle`. Все настройки под этим узлом относятся к объявленному [типу источника данных](../../../concepts.md#data-source-type "Узнайте больше о концепции расширений Dynatrace.") (в данном случае SQL).

## Коннектор JDBC

Источник данных SQL расширений Dynatrace позволяет запрашивать любую базу данных, допускающую подключения через драйвер JDBC, помимо всех поставщиков баз данных, поддерживаемых по умолчанию. Для таких баз данных требуются дополнительные шаги.

### Объявление JDBC-подключения в YAML-файле расширения

1. Начните определение расширения с узла `jdbc`.
2. Объявите имя класса драйвера. Например, `org.mariadb.jdbc.Driver`.
3. Укажите шаблон строки подключения и сообщение валидации. Они будут использоваться для проверки строки подключения, предоставленной пользователем в конфигурации мониторинга.
4. Предоставьте самый простой запрос, который расширение выполнит для проверки подключения.

```
jdbc:


driverClassName: "org.mariadb.jdbc.Driver"


connectionStringPattern: "jdbc:mariadb:(. |\\s)+$"


connectionStringPatternErrorMessage: "This isn't a correct connection string, please start with jdbc:mariadb."


validationQuery: "SELECT 1"
```

Пользователи, запускающие ваше расширение, также должны будут загрузить соответствующий драйвер JDBC на ActiveGate, принадлежащий группе, назначенной для запуска вашего расширения. Подробнее см. [Конфигурация мониторинга JDBC](jdbc-monitoring.md#upload "Расширения JDBC в фреймворке расширений.").

## SQL-запросы

SQL-расширения основаны на SQL-запросах. Запросы, объявленные в расширении, извлекают значения для метрик и измерений. Для сопоставления результатов запроса с метрикой тип столбца должен быть числовым. Если он не числовой, необходимо привести его к числовому типу.

Например, следующий SQL-запрос возвращает количество ядер CPU.

```
SELECT value AS cpu_count


FROM v$parameter


WHERE name = 'cpu_count'
```

Вы можете использовать его в расширении и передавать значение, возвращаемое запросом, как метрику `com.dynatrace.extension.sql-oracle.cpu.cores` в Dynatrace.

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

По соображениям безопасности источник данных поддерживает только подмножество языка SQL. Подробнее см. [Средства контроля безопасности](#security-controls).

## Частота запросов

Вы можете задать частоту, с которой опрашивается поставщик базы данных. Если не задано, поставщик базы данных опрашивается каждую минуту по умолчанию.

Для управления временем опроса поставщика базы данных можно использовать одно из двух взаимоисключающих свойств: `interval` или `schedule`. Их можно определить на уровне группы или подгруппы.

### Интервал

ActiveGate версии 1.253+

Значение интервала принимает целое число, выражающее минуты. Например, для опроса поставщика базы данных каждые 10 минут добавьте следующую запись:

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

### Расписание

ActiveGate версии 1.301+

Вы можете использовать cron-выражение для опроса поставщика базы данных по выбранному расписанию.

Выражение должно соответствовать формату Unix cron:

```
# * * * * *


# | | | | |


# | | | | day of the week (1-7) (Sunday to Saturday)


# | | | month (1-12)


# | | day of the month (1-31)


# | hour (0-23)


# minute (0-59)
```

Значения также поддерживают списки (`1,2,3,4`), шаги (`0-23/2`) и диапазоны (`2-5`).

Формат не поддерживает одновременное указание дня недели и дня месяца. В одном из этих полей необходимо использовать символ `?`.

Например, для выполнения запроса в 12:00 каждый рабочий день (понедельник-пятница) используйте следующую запись:

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

### Управление частотой пользователями расширения

ActiveGate версии 1.303+

Если вы хотите позволить пользователям расширения управлять частотой опроса поставщика базы данных, можно использовать переменные вместо фиксированных значений. Пользователи смогут определить значение переменной при активации расширения.

Обязательно подробно опишите контекст переменной, чтобы пользователи понимали, как правильно задать значение. Также можно установить шаблон для помощи в валидации вводимых данных.

Например, чтобы позволить пользователю управлять интервалом:

1. Сначала объявите переменную в YAML-файле расширения

   ```
   vars:


   - id: myInterval


   displayName: Interval


   description: Interval at which your database provider is queried in minutes. 10 minutes by default.


   defaultValue: "10"


   pattern: ^[0-9]+$


   type: text
   ```
2. Затем используйте ссылку на переменную вместо фиксированного значения в YAML-файле расширения

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

   Подробнее об использовании переменных см. [YAML-файл расширения](../../extension-yaml.md#variables "Узнайте, как создать YAML-файл расширения с помощью фреймворка расширений.")

## Таймауты

При разработке расширения можно указать значение таймаута для заданного запроса на уровне группы или подгруппы. Таймауты указываются в секундах; значение по умолчанию — `10`. Указанное значение должно быть строкой, например: `20`, `60`, `120` и т.д.

Вы также можете использовать ссылку на переменную для указания таймаута. Подробнее об использовании переменных см. [YAML-файл расширения](../../extension-yaml.md#variables "Узнайте, как создать YAML-файл расширения с помощью фреймворка расширений.").

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

Важные замечания при настройке таймаутов

Указание пользовательского таймаута для запроса изменяет способ его выполнения источником данных. Все запросы выполняются последовательно по умолчанию, поэтому источнику данных необходимо использовать только одно подключение к базе данных. При определении пользовательского таймаута запрос будет выполняться параллельно, открывая дополнительное подключение к базе данных. Это означает, что при добавлении пользовательских таймаутов необходимо соблюдать осторожность, чтобы расширение не открывало слишком много подключений.

## Измерения

Для каждого уровня (расширение, группа, подгруппа) можно определить до 25 измерений.

Подгруппа наследует измерения родительской группы. Для обеспечения распространения данных, когда у родительской группы есть определённый запрос, подгруппа выполнит свой запрос после завершения первого выполнения запроса родительской группой.

### Ключ измерения

Строка ключа измерения должна соответствовать [протоколу приёма метрик](../../../../extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#dimension-optional "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

### Значение измерения

Вы используете SQL-запрос для получения значения измерения (с префиксом `col:`) или используете фиксированную строку (с префиксом `const:`). Например:

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

Вы можете добавить логику фильтрации на уровне измерения. Это приведёт к передаче только тех метрик, значение измерения которых соответствует критериям фильтрации.
Если фильтры установлены для нескольких измерений, все фильтры должны совпасть для создания строки метрики. Логика фильтрации не изменяет выполняемый запрос.

Фильтры могут быть заданы как константное значение или как [переменная](../../extension-yaml.md#variables "Узнайте, как создать YAML-файл расширения с помощью фреймворка расширений.").

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

* **Начинается с** — используйте квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Заканчивается на** — используйте квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Содержит** — используйте квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Равно** — используйте квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для вышеперечисленных выражений также можно использовать квалификаторы:

  + `const:$and` — для объединения двух или более выражений оператором AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or` — для объединения двух или более выражений оператором OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not` — для отрицания выражения. Пример:

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

Строка ключа метрики должна соответствовать [протоколу приёма метрик](../../../../extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#metric-key-required "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

Для версий Dynatrace 1.215 и 1.217 узел метрики требует параметра `id` вместо `key`. Начиная с версии Dynatrace 1.219 следует использовать параметр `key`, так как `id` будет считаться устаревшим.

#### Лучшие практики для ключей метрик

Метрики, которые вы отправляете в Dynatrace с помощью расширения, — это лишь часть тысяч метрик (встроенных и пользовательских), обрабатываемых Dynatrace. Чтобы сделать ключи метрик уникальными и легко идентифицируемыми в Dynatrace, лучшей практикой является добавление имени расширения в качестве префикса к имени метрики. Это гарантирует уникальность ключа метрики и позволяет легко привязать метрику к конкретному расширению в вашей среде.

### Значение метрики

Значение столбца, запрашиваемое из базы данных.

### Тип

Фреймворк расширений Dynatrace поддерживает форматы полезной нагрузки метрик gauge (`gauge`) и count (`count`). Подробнее см. [Полезная нагрузка метрики](../../../../extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#payload-required "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API."). Для указания типа метрики используйте атрибут `type`.

## Метаданные метрик

Расширение может определять метаданные для каждой метрики, доступной в Dynatrace. Например, вы можете добавить отображаемое имя метрики и единицу измерения, которые можно использовать для фильтрации в [Обозревателе метрик](../../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью обозревателя метрик Dynatrace.").

Определите все метаданные метрик в разделе `metrics` YAML-файла расширения, чтобы обеспечить их правильную связь с конфигурацией метрики.

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

Наборы функций — это категории, в которые вы организуете данные, собираемые расширением. В этом примере мы создаём расширение Oracle SQL, собирающее метрики, связанные с производительностью CPU и ввода/вывода. Это отражается в организации метрик в соответствующие наборы функций `cpu` и `io`.

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

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) можно ограничить мониторинг одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут отражать сегменты вашей среды. Тогда при создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, которая может подключаться к этому конкретному сегменту.

Все метрики, не отнесённые ни к одному набору функций, считаются набором по умолчанию и всегда передаются.

Метрика наследует набор функций подгруппы, которая, в свою очередь, наследует набор функций группы. Также набор функций, определённый на уровне метрики, переопределяет набор функций подгруппы, который, в свою очередь, переопределяет набор функций группы.

## Конфигурация мониторинга Oracle SQL

После определения области конфигурации необходимо определить сетевые устройства, с которых вы хотите собирать данные, и идентифицировать ActiveGate, которые будут выполнять расширение и подключаться к вашим устройствам.

Формат конфигурации мониторинга зависит от поставщика базы данных. Подробнее см. [Конфигурация мониторинга Oracle Database](oracle-monitoring.md "Создание и активация конфигурации мониторинга для расширения на основе источника данных SQL для Oracle Database.").
