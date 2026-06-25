---
title: О расширениях
source: https://docs.dynatrace.com/managed/ingest-from/extensions/concepts
scraped: 2026-05-12T12:02:16.435697
---

# О расширениях

# О расширениях

* Пояснение
* Чтение: 2 мин
* Обновлено 28 января 2026 г.

Концепции

Источники данных

### Extension Execution Controller (EEC)

Extension Execution Controller (EEC) является компонентом Dynatrace, запускающим расширения. EEC опрашивает локальные источники данных при работе в OneAgent или удалённые источники данных при работе в ActiveGate. EEC автоматически устанавливается и управляется при каждой конфигурации OneAgent и ActiveGate. EEC также преобразует все принятые данные для [каузального анализа Dynatrace Intelligence](/managed/dynatrace-intelligence/ai-models/causal-correlation-analysis "Узнайте, как каузальный корреляционный анализ Davis® находит связанные метрики в вашей среде."). Дополнительные сведения см. в разделе [Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.").

Чтобы запускать локальные расширения, убедитесь, что EEC включён на уровне окружения, хоста или группы хостов.

Включение на уровне окружения

1. Откройте **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включение для отдельного хоста

1. Откройте **Hosts**.
2. Найдите и выберите нужный хост, чтобы открыть страницу обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**…**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

Включение для группы хостов

1. Откройте **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group**, затем выберите нужную группу хостов из раскрывающегося списка.

   Список хостов теперь отфильтрован по выбранной группе. У каждого хоста есть ссылка **Host group:** `<group name>`, где `<group name>` является названием настраиваемой группы хостов.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни одной группе хостов.
4. Выберите название группы хостов в любой строке.

   Поскольку список отфильтрован по группе хостов, все отображаемые хосты относятся к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

### Группа ActiveGate

Dynatrace использует группы ActiveGate для определения места запуска расширений. Каждый ActiveGate, запускающий расширение, должен входить в группу. Если планируется использование одного ActiveGate, назначьте его в выделенную группу. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

Расширения можно запускать с помощью Environment ActiveGate, установленного для [маршрутизации трафика OneAgent в Dynatrace и мониторинга облачных сред и удалённых технологий с помощью расширений](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate и их применении.").

Cluster ActiveGate и multi-environment ActiveGate не поддерживаются платформой Extensions framework.

### Профиль производительности

OneAgent версии 1.243+ Ограничение потребления ресурсов задаётся в параметре **Performance profile**. По умолчанию один процесс источника данных использует до 2% ЦП и 100 МБ ОЗУ в OneAgent и до 5% ЦП и 500 МБ ОЗУ в ActiveGate.

Ограничения ЦП и ОЗУ применяются к суммарному потреблению ресурсов EEC и всех процессов источников данных. Существуют два уровня:

* Мягкий предел: каждый входящий тест отклоняется, если потребление превышает ограничение. Этот уровень применяется только для ActiveGate.
* Жёсткий предел: последняя запущенная задача останавливается и отклоняется первой.

  + Для OneAgent задачи останавливаются и перезапускаются с задержкой. Время задержки увеличивается с каждым перезапуском процесса.
  + Для ActiveGate задачи останавливаются и отклоняются до тех пор, пока потребление не опустится ниже ограничения.

Изменение профиля производительности на уровне окружения

1. Откройте **Settings** > **Preferences** > **Extension Execution Controller**.
2. Установите **Performance profile** в значение `Default` или `High limits`.

Изменение профиля производительности на уровне хоста

1. Откройте **Hosts**.
2. Найдите и выберите нужный хост, чтобы открыть страницу обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**…**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Установите **Performance profile** в значение `Default` или `High limits`.

Изменение профиля производительности для ActiveGate

1. Откройте **Deployment Status** и выберите **ActiveGates**.
2. Разверните ![Развернуть строку](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Развернуть строку") раздел **Details** нужного ActiveGate и выберите **Settings**.
3. На странице **Settings** перейдите в **Extension Execution Controller**.
4. Установите **Performance profile** в значение `Default`, `High limits` или `Dedicated limits`.

   Значение `Dedicated limits` можно включить только после настройки ActiveGate, описанной в разделе [Настройка выделенного профиля производительности](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Настройте режим выделенного профиля производительности для оптимизации производительности хоста ActiveGate.").

### Конфигурация окружения

Конфигурация окружения представляет собой универсальный набор определений мониторинга, адаптированных к особенностям источника данных, например SNMP. Конфигурация окружения хранится в файле `extension.yaml`, который загружается в Dynatrace в составе пакета расширения в формате ZIP. Конфигурация окружения определяет:

* Область собираемых данных: какие метрики принимаются и какие измерения им назначаются.
* Источник, из которого извлекаются измерения и значения измерений.
* Категоризацию данных по наборам функций, которые можно выбирать при определении конфигурации мониторинга.
* Способ формирования метрик в контексте протокола приёма метрик.
* Способ обработки и представления данных, собранных расширением, в Dynatrace.

В окружении можно хранить до 10 конфигураций на расширение. В любой момент времени может быть активна только одна конфигурация. Чтобы активировать конкретную конфигурацию, включите переключатель **Enabled**.

Без конфигурации окружения расширение не отображается на платформе Dynatrace.

### Конфигурация мониторинга

Конфигурация мониторинга привязана к типу источника данных, который требуется отслеживать. Она определяет:

* Откуда запускается расширение.
* Для удалённых расширений: эндпоинты, к которым обращается расширение для сбора данных, а также учётные данные для доступа к ним.
* Свойства подключения: таймаут и количество повторных попыток при неудачном соединении.
* Значения переменных, которые передаются в конфигурацию окружения, когда необходимо адаптировать расширение к особенностям конкретного экземпляра источника данных.

На основе одной конфигурации окружения можно создать до 100 конфигураций мониторинга, каждая из которых выполняется параллельно.

Чтобы начать мониторинг с помощью расширения, необходимо добавить конфигурацию мониторинга через вызов API, которая укажет Dynatrace, как собирать данные из источника.

Без конфигурации мониторинга расширение отображается на платформе Dynatrace, но не собирает данные.

* Сведения о создании конфигурации мониторинга для Oracle Database см. в разделе [Конфигурация мониторинга Oracle Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Создайте и активируйте конфигурацию мониторинга для расширения на основе источника данных SQL для Oracle Database.").
* Сведения о создании конфигурации мониторинга для Microsoft SQL Server см. в разделе [Конфигурация мониторинга Microsoft SQL Server](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Расширения Microsoft SQL в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для IBM Database см. в разделе [Конфигурация мониторинга IBM Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "Расширения IBM DB2 в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для MySQL см. в разделе [Конфигурация мониторинга MySQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "Расширения MySQL в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для PostgreSQL см. в разделе [Конфигурация мониторинга PostgreSQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "Расширения PostgreSQL в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для SAP Hana Database см. в разделе [Конфигурация мониторинга SAP Hana Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "Расширения SAP Hana в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для Snowflake Database см. в разделе [Конфигурация мониторинга базы данных Snowflake](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Расширения Snowflake Database в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для JDBC см. в разделе [Конфигурация мониторинга JDBC](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "Расширения JDBC в платформе Extensions framework.").

### Пакет расширения

Расширения поставляются в виде ZIP-пакета, содержащего только:

| Файл | Описание |
| --- | --- |
| `extension.zip` | Архив с определением расширения и всеми его ресурсами. |
| `extension.zip.sig` | Файл подписи: цифровая подпись ZIP-архива. Гарантирует целостность и подлинность содержимого ZIP-файла, проверяя, что он не был изменён и подписан доверенным источником. Подробнее см. в разделе [Подписание расширений](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework."). |
| `extension.zip.sig.tsr` | Файл метки времени подписи, обеспечивающий актуальность подписи с течением времени (обрабатывается только для официальных расширений). |

Пакеты расширений с иным составом содержимого не принимаются для загрузки. Максимальный размер пакета расширения составляет 25 МБ.

```
bundle.zip



│   extension.zip



│   extension.zip.sig



│   extension.zip.sig.tsr
```

### Dynatrace CLI

Dynatrace CLI (`dt-cli`) является утилитой командной строки для разработки, подписания и сборки расширений в платформе Dynatrace Extensions framework.

С помощью Dynatrace CLI можно:

* Собирать и подписывать расширения из исходного кода
* Создавать разработческие сертификаты для подписания расширений
* Создавать CA-сертификаты для разработки

Подробнее см. в разделе [Подписание расширений](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.") и в проекте [dt-cli](https://github.com/dynatrace-oss/dt-cli) на GitHub.

### Наборы функций

Набор функций представляет собой группу ключей метрик, определённых в конфигурации расширения. Группы функций можно активировать или деактивировать в интерфейсе или в JSON-файле. При активации набора функций отчётность формируется по всем метрикам этого набора. Метрика, не включённая ни в один набор функций, всегда входит в отчётность.
Например, расширение SNMP отслеживает сетевые устройства и собирает метрики о состоянии сетевых карт, транспортном уровне и SNMP-трапах. Наборы функций позволяют настроить мониторинг, например активировав только наборы, относящиеся к конкретным устройствам или ActiveGate. Расширение продолжает отслеживать другие устройства, но не формирует отчётность по их метрикам.

![Наборы функций расширения F5](https://dt-cdn.net/images/screenshot-2025-07-03-at-14-59-40-858-61f4357458.png)

Наборы функций расширения F5

### Конфигурации и ограничения

Перед развёртыванием расширений ознакомьтесь с текущими [ограничениями](/managed/ingest-from/extensions/extension-limits "Узнайте об ограничениях расширений."), чтобы эффективно достичь целей мониторинга.

### Управление доступом и необходимые разрешения

Работа с расширениями требует специальных разрешений для управления жизненным циклом расширений, настройки мониторинга и защиты конфиденциальных данных.

* При использовании Dynatrace Hub необходимо классическое разрешение **Manage monitoring settings** в вашей группе для изменения конфигурации мониторинга.
* При аутентификации API с помощью токена тенанта токен должен иметь разрешения `extensions.read` и `extensions.write`.

[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Расширьте наблюдаемость данных с сетевых устройств с помощью декларативных метрик на основе SNMP OID.](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Узнайте, как создать расширение SNMP с помощью платформы Extensions framework.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Расширьте наблюдаемость данных устройств с интерфейсом Windows Management Instrumentation.](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Узнайте, как создать расширение WMI с помощью платформы Extensions framework.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Дополните данные приложений и сервисов метриками, полученными из эндпоинта Prometheus за пределами Kubernetes.](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью платформы Extensions framework.")[![Источник данных SQL](https://dt-cdn.net/images/sql-logo-036ab75f37.svg "Источник данных SQL")

### SQL

Расширьте наблюдаемость данных уровня базы данных с помощью SQL-запросов.](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Узнайте, как создать расширение на основе источника данных SQL с помощью платформы Extensions framework.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Расширьте наблюдаемость данных, полученных из JMX MBeans.](/managed/ingest-from/extensions/develop-your-extensions/data-sources/jmx "Узнайте, как создать расширение JMX с помощью платформы Extensions framework.")[### Python

Расширьте наблюдаемость данных любой технологии, предоставляющей данные через интерфейс, с помощью пользовательских расширений на основе Python SDK от Dynatrace.](/managed/ingest-from/extensions/develop-your-extensions/data-sources/python "Библиотека Python и набор инструментов для создания расширений Python для Dynatrace Extensions.")