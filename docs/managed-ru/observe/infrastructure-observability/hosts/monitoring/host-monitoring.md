---
title: Мониторинг хостов с помощью Dynatrace
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring
scraped: 2026-05-12T11:37:30.789664
---

# Host monitoring with Dynatrace

# Мониторинг хостов с помощью Dynatrace

* Explanation
* 1-min read
* Updated on Jun 15, 2022

Как только данные о хостах начинают поступать, искусственный интеллект Dynatrace Davis® AI мгновенно формирует базовые показатели. Каждая метрика, отображаемая на странице обзора хоста, входит в источник данных Davis AI, используемый для автоматического выявления потенциальных проблем производительности на уровне инфраструктуры или полного стека.

Как перейти:

1. Перейдите в **Hosts**, чтобы просмотреть список всех хостов (физических и виртуальных) в вашей среде, на которых установлен OneAgent.
2. Выберите имя хоста в списке, чтобы перейти на страницу обзора этого хоста.

Все актуальные метрики хоста отображаются на одной странице, разделённой на несколько логических разделов.

## Панель уведомлений

Панель уведомлений хоста даёт быстрый обзор состояния хоста. Выберите элемент уведомления для отображения дополнительной информации.

### Properties and tags

Выберите **Properties and tags** на панели уведомлений, чтобы открыть панель **Properties and tags**, отображающую метаданные выбранного хоста:

* **Tags** — список тегов, применённых к хосту. Выберите **Add Tag**, чтобы добавить тег к метаданным хоста.
* **Properties** — список различных свойств хоста: версия OneAgent, версия ОС, режим мониторинга, IP-адреса и зоны управления.

### Проблемы

* На панели уведомлений **Problems** показывает активные и закрытые проблемы, связанные с выбранным хостом.
* Выберите **Problems** на панели уведомлений, чтобы открыть панель **Problems** со списком проблем.

  + Выберите проблему для просмотра подробностей.
  + Выберите **Go to problems**, чтобы перейти на страницу [Problems](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI."), отфильтрованную по выбранному хосту.

### Уязвимости

* На панели уведомлений **Vulnerabilities** показывает наиболее серьёзные обнаруженные [уязвимости](/managed/secure/application-security "Access the Dynatrace Application Security functionalities."), затрагивающие выбранный хост.
* Выберите **Vulnerabilities** на панели уведомлений, чтобы открыть панель **Vulnerabilities**, в которой перечислены наиболее серьёзные [уязвимости сторонних компонентов](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.") и [уязвимости на уровне кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities "Monitor the code-level vulnerabilities in your environment."), связанные с данным хостом.

  + Выберите уязвимость в списке, чтобы просмотреть подробности и оценить степень её серьёзности и влияние на вашу среду.
  + Для просмотра полного списка обнаруженных уязвимостей, затрагивающих данный хост, выберите **Show all third-party vulnerabilities** / **Show all code-level vulnerabilities**.

  Пример уязвимостей сторонних компонентов:

  ![Host overview: TPV](https://dt-cdn.net/images/host-tlv-764-ef67c680cf.png)

  Host overview: TPV

  Пример уязвимостей на уровне кода:

  ![Host overview: CLV](https://dt-cdn.net/images/host-clv-769-ed43f5e602.png)

  Host overview: CLV

Если у вас недостаточно [прав на просмотр](/managed/secure/application-security#permissions "Access the Dynatrace Application Security functionalities.") для выбранной зоны управления, вкладка **Vulnerabilities** на панели уведомлений показывает `Not analyzed`.

### Доступность

* На панели уведомлений **Availability** показывает процент времени, в течение которого хост был онлайн и реагировал на запросы. Dynatrace обнаруживает и отображает завершения работы ОС (включая перезагрузки) и периоды недоступности хоста (например, при его неожиданном отключении).
* Выберите **Availability** на панели уведомлений, чтобы открыть панель **Host availability** с графиком доступности хоста во времени.

  ![Host page detail - online availability](https://dt-cdn.net/images/screenshot-2023-07-04-at-4-54-15-pm-1210-837a6b0515.png)

  Host page detail - online availability

Подробнее см. в разделе [Host availability](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability "Check host availability, interpret host availability states, and see how maintenance windows are reflected in host availability charts.").

### SLO

* На панели уведомлений **SLOs** показывает текущее количество [SLO](/managed/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic."), связанных с выбранным хостом.
* Выберите **SLOs** на панели уведомлений, чтобы открыть панель **Service-level objectives** со списком SLO, напрямую или косвенно связанных с хостом.

#### Напрямую связанные SLO

* SLO считается напрямую связанным с хостом, если [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") данного SLO соответствует следующим критериям:

  + Тип сущности установлен как `"HOST"`.
  + Идентификатор сущности совпадает с ID хоста.
* Чтобы отображать только SLO, напрямую связанные с хостом, убедитесь, что параметр **Show only directly connected SLOs** включён.

#### Косвенно связанные SLO

* SLO не является напрямую связанным с хостом, если в [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") данного SLO не указан конкретный идентификатор сущности.

  Пример: если указаны общие значения, например `type("HOST"),tag("slo")`, запрос возвращает все SLO для всех хостов, включая текущий.
* Чтобы отображать SLO, не связанные с хостом напрямую, отключите параметр **Show only directly connected SLOs**.

#### Действия

* Выберите **Details** для просмотра графика соответствующих метрик SLO.
* В разделе **Actions** выберите:

  + **View in Data Explorer** — [просмотр метрик SLO в Data Explorer](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** — [закрепление SLO на панели мониторинга](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace."). Подробнее см. в разделе [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
  + **SLO definition** — редактирование SLO в **Service-level objective definitions**.
  + **Clone** — [клонирование SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** — [создание оповещения для SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

#### SLO не найдены

Если SLO не обнаружены, вы можете:

* Выбрать другой временной диапазон в правом верхнем углу.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

  Timeframe selector: menu bar
* Выбрать **Add SLO** для создания SLO с помощью [мастера SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

#### Пример панели SLO

![slo-card-hosts](https://dt-cdn.net/images/slo-card-756-c16ec34294.png)

slo-card-hosts

## Производительность

### Входящие соединения

Раздел **Incoming connections** отображает таблицу хостов, являющихся вышестоящими по отношению к выбранному хосту.

* Выберите любой хост для перехода на его страницу обзора.
* Выберите > **Analyze process connections** для перехода на страницу **Process connections**, где можно просмотреть входящие и исходящие соединения.

### Исходящие соединения

Раздел **Outgoing connections** отображает таблицу хостов, являющихся нижестоящими по отношению к выбранному хосту.

* Выберите любой хост для перехода на его страницу обзора.
* Выберите > **Analyze process connections** для перехода на страницу **Process connections**, где можно просмотреть входящие и исходящие соединения.

### Производительность хоста

Раздел **Host performance** предоставляет быстрый доступ к ключевым метрикам: CPU, памяти и сети с различными агрегациями за выбранный временной диапазон. Просмотр временной шкалы позволяет одновременно определять выбранные аномалии на всех графиках метрик, что упрощает понимание взаимосвязей между различными компонентами инфраструктуры в конкретный момент времени.

Максимальные и минимальные пики потребления ресурсов легко отслеживать, поскольку каждый график метрики позволяет выбрать разную агрегацию. Также можно отображать пользовательские метрики вместо метрик по умолчанию, что позволяет анализировать конкретные взаимосвязи между метриками, критически важными для той или иной конфигурации хоста.

Использование графиков

Выберите в правом верхнем углу графика, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для соответствующего запроса, просмотреть запрос, выполнить более детальный анализ, настроить параметры графика и закрепить его на панели мониторинга.
* **Pin to dashboard** — закрепить копию выбранного графика на любой доступной для редактирования классической панели мониторинга. Подробнее см. в разделе [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

![Host overview: host performance](https://dt-cdn.net/images/host-performance-1597-05b7f2365c.png)

Host overview: host performance

### Анализ процессов

Для лучшего понимания поведения процессов перейдите в раздел **Process analysis**, который содержит графики и список процессов, выполняющихся на выбранном хосте. Выберите процесс для получения подробной информации о нём на данном хосте.

Использование графиков

Выберите в правом верхнем углу графика, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для соответствующего запроса.
* **Pin to dashboard** — закрепить копию выбранного графика на любой доступной для редактирования классической панели мониторинга. Подробнее см. в разделе [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

![Host overview: process analysis](https://dt-cdn.net/images/process-analysis-1599-d637b524c6.png)

Host overview: process analysis

### Анализ служб ОС

Эта функция доступна только для операционных систем Linux и Windows.

Раздел **OS services analysis** содержит список служб операционной системы, отслеживаемых на предмет доступности. Для мониторинга службы необходимо наличие хотя бы одной политики с правилами, соответствующими свойствам данной службы. Подробнее о создании политик мониторинга для служб ОС см. в разделе [OS services monitoring](/managed/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.").

* Выберите любой хост для перехода на его страницу обзора, затем перейдите в раздел **OS services analysis**.
* Выберите имя службы из списка, чтобы открыть страницу **Service overview** со свойствами выбранной службы и графиком её доступности.

Чтобы настроить политики для служб ОС в Windows и Linux, выберите > **OS services monitoring settings** для перехода на страницу [OS services monitoring](/managed/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.").

### Моментальные снимки экземпляров процессов

OneAgent version 1.237+

Раздел **Process instance snapshots** предоставляет дополнительные сведения о наиболее ресурсоёмких процессах, выполняющихся на хосте, а также о процессах, определённых для мониторинга [доступности процессов](/managed/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts.").

![Process instance snapshot](https://dt-cdn.net/images/process-instance-snapshot-1404-c1bcee55de.png)

Process instance snapshot

Отдельный снимок экземпляра процесса представляет собой набор данных мониторинга для процессов. Он содержит данные о **CPU usage (%)**, **Memory usage (B)**, **Incoming network traffic (KB)** и **Outgoing network traffic (KB)**, измеряемых с интервалом в одну минуту. Один снимок содержит 20 минут данных мониторинга: 10 минут до события и 10 минут после. Каждый хост может передавать не более 60 минут таких метрик в сутки. Процесс включается в снимок, если его потребление CPU, памяти или сети превышает 1%.

Снимок экземпляра процесса создаётся при высоком потреблении CPU, памяти или сети на хосте. Также можно запросить снимок процесса вручную. Выберите в правом верхнем углу раздела и нажмите **Request process snapshot now**. Дождитесь сообщения об успешном запуске снимка. Данные снимка процесса должны появиться после перезагрузки страницы в течение 90 секунд.

Кроме того, для процессов, определённых для мониторинга [доступности процессов](/managed/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts."), снимок показывает поведение процессов перед их завершением и факт их повторного появления в течение 10 минут.

#### Включение снимков экземпляров процессов

Снимки экземпляров процессов можно включить на уровне хоста или среды.

* Для включения на уровне среды перейдите в **Settings**, выберите **Processes and containers** > **Process instance snapshots** и включите **Enable process instance snapshots**.
* Для определения правила на уровне хоста перейдите на страницу обзора хоста, выберите , перейдите в **Settings**, выберите **Process instance snapshots** и включите **Enable process instance snapshots**.
* Для определения правила на уровне группы хостов перейдите на страницу группы хостов по адресу `https://your-environment/ui/settings/HOST_GROUP-NAME`, выберите **Process instance snapshots** и включите **Enable process instance snapshots**.

На той же странице настроек можно также уменьшить максимальное количество процессов, включаемых в один снимок. Максимальное/стандартное значение — 100 процессов.

### Анализ дисков

Для выявления узких мест производительности дисков перейдите в раздел **Disk analysis**, в котором отображаются все точки монтирования для Linux и все тома для Windows. Здесь можно оценить использование дискового пространства и метрики пропускной способности, а также другие выбранные метрики дисков для быстрого обнаружения проблем.

* На странице хоста можно отфильтровать диски по имени для фокусировки на выбранном диске.
* Раскройте запись диска для просмотра подробных сведений о выбранном диске. Каждый экземпляр диска отображает отдельные детальные метрики производительности, что упрощает обнаружение неоптимально работающих ресурсов.

Каждая точка монтирования (Linux) или том (Windows) имеет собственные метрики производительности в дополнение к совокупным метрикам. Это позволяет легче обнаружить медленный или нестабильный диск. Оповещения можно настроить для отдельных дисков так же, как для совокупных графиков.

Использование графиков

Выберите в правом верхнем углу графика, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для соответствующего запроса.
* **Pin to dashboard** — закрепить копию выбранного графика на любой доступной для редактирования классической панели мониторинга. Подробнее см. в разделе [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

![Host overview: disk analysis](https://dt-cdn.net/images/disk-analysis-1599-236d782165.png)

Host overview: disk analysis

### Мониторинг дисков

Мониторинг дисков — это плановая задача, которая собирает метрики дисков от агента. Она запускается автоматически, когда агент ОС обнаруживает диск.

Доступные параметры для дисков:

* **Disk options**: можно создавать правила исключений для удаления определённых дисков из списка мониторинга и обнаружения дубликатов дисков. Подробнее см. в разделе [Disk options](/managed/observe/infrastructure-observability/hosts/configuration#disk-options "Host-level settings").
* **Disk anomaly detection rules**: можно настроить обнаружение аномалий хостов, включая пороги проблем и событий. Подробнее см. в разделе [Host anomaly detection](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.").
* **Anomaly detection for infrastructure: Disk**: с помощью этих параметров можно настроить чувствительность обнаружения, задать пороги оповещений или отключить оповещения для дисков. Подробнее см. в разделе [Anomaly detection](/managed/observe/infrastructure-observability/hosts/configuration#anomaly-detection "Host-level settings").

#### Ограничения

* Поддерживаемые метрики дисков

  ## Инфраструктура

  ### Диск

  | Ключ метрики | Название и описание | Единица | Агрегации | Потребление мониторинга |
  | --- | --- | --- | --- | --- |
  | builtin:host.disk.throughput.read | Disk throughput read — пропускная способность чтения файловой системы в битах в секунду | bit/s | auto avg max min | Host units |
  | builtin:host.disk.throughput.write | Disk throughput write — пропускная способность записи файловой системы в битах в секунду | bit/s | auto avg max min | Host units |
  | builtin:host.disk.avail | Disk available — объём свободного места, доступного пользователю в файловой системе. В Linux и AIX — место для непривилегированного пользователя без резервируемой для root части | Byte | auto avg max min | Host units |
  | builtin:host.disk.bytesRead | Disk read bytes per second — скорость чтения из файловой системы в байтах в секунду | Byte/second | auto avg max min | Host units |
  | builtin:host.disk.bytesWritten | Disk write bytes per second — скорость записи в файловую систему в байтах в секунду | Byte/second | auto avg max min | Host units |
  | builtin:host.disk.free | Disk available % — процент свободного места, доступного пользователю в файловой системе | Percent (%) | auto avg max min | Host units |
  | builtin:host.disk.inodesAvail | Inodes available % — процент свободных inodes, доступных непривилегированному пользователю. Недоступна в Windows | Percent (%) | auto avg max min | Host units |
  | builtin:host.disk.inodesTotal | Inodes total — общее количество inodes, доступных непривилегированному пользователю. Недоступна в Windows | Count | auto avg max min | Host units |
  | builtin:host.disk.queueLength | Disk average queue length — среднее число операций чтения и записи в очереди диска | Count | auto avg max min | Host units |
  | builtin:host.disk.readOps | Disk read operations per second — число операций чтения из файловой системы в секунду | Per second | auto avg max min | Host units |
  | builtin:host.disk.readTime | Disk read time — среднее время чтения из файловой системы; показывает среднюю задержку диска при чтении | Millisecond | auto avg count max min sum | Host units |
  | builtin:host.disk.used | Disk used — объём используемого пространства в файловой системе | Byte | auto avg max min | Host units |
  | builtin:host.disk.usedPct | Disk used % — процент используемого пространства в файловой системе | Percent (%) | auto avg max min | Host units |
  | builtin:host.disk.utilTime | Disk utilization time — процент времени, затраченного на операции дискового ввода-вывода | Percent (%) | auto avg max min | Host units |
  | builtin:host.disk.writeOps | Disk write operations per second — число операций записи в файловую систему в секунду | Per second | auto avg max min | Host units |
  | builtin:host.disk.writeTime | Disk write time — среднее время записи в файловую систему; показывает среднюю задержку диска при записи | Millisecond | auto avg count max min sum | Host units |

* Развёртывание через установщик OneAgent

  + Сетевые диски поддерживаются для хостов Linux и AIX; начиная с OneAgent version 1.277 мониторинг сетевых дисков также включён для Windows.
  + SMB 1.0 поддерживается начиная с OneAgent version 1.263.
* Развёртывание только для приложений (application-only OneAgent)

  + Application-only OneAgent предоставляет ограниченный набор метрик дискового ввода-вывода:

    - `Disk read bytes per second`
    - `Disk write bytes per second`
    - `Disk read operations per second`
    - `Write operations per second`
  + Linux использует файл `/proc/diskstats`, предоставляющий информацию об активности дискового ввода-вывода. `/proc/diskstats` не содержит сведений о сетевых монтированиях.
  + Solaris не предоставляет информацию о дисковом вводе-выводе.
  + AIX сообщает только метрики `Disk read bytes per second` и `Disk write bytes per second`.

Только Windows: страница дисков отображает только локальные диски с буквой и/или точкой монтирования. Для удалённых дисков система распознаёт и отображает только общие ресурсы по протоколу CIFS.

#### Отключение мониторинга для отдельных дисков

Задайте фильтр исключений, чтобы избежать проблем с особыми точками монтирования:

1. Перейдите в **Settings** > **Preferences** > **Disk options**.
2. Выберите **Add item**, чтобы исключить диск из списка мониторинга.
3. Укажите операционную систему, путь к диску и тип файловой системы.
4. Выберите **Save changes**.

#### Дедупликация дисков

Дедупликация дисков помогает устранить избыточность в NFS-монтированиях на хосте. В некоторых случаях один и тот же NFS-ресурс может быть смонтирован несколько раз в разных точках монтирования или с разными параметрами. Это может привести к появлению дубликатов, влияющих на точность мониторинга. Дедупликация дисков выявляет и удаляет такие избыточные монтирования для получения более чистых и точных данных.

Система обнаруживает дубликаты дисков путём сравнения их IP-адресов и объёма доступного/используемого пространства. Если два или более дисков имеют одинаковые IP и метрики использования, они считаются дубликатами и подлежат дедупликации.

Дедупликацию дисков можно включить или отключить в **Settings** > **Preferences** > **Disk options**.

#### Олицетворение пользователей в Windows

В Windows агент ОС выполняет олицетворение вошедшего в систему пользователя для сбора метрик дисков с NFS-ресурсов. Агент использует олицетворённый контекст безопасности для запроса метрик дисков у NFS-сервера.

### Disk Edge alerting

OneAgent version 1.293+

Используйте **Disk Edge** для настройки оповещений автоматического обнаружения аномалий производительности, связанных с дисковой инфраструктурой.

Disk Edge обеспечивает автоматическое обнаружение аномалий производительности дисковой инфраструктуры. Эти настройки позволяют адаптировать чувствительность обнаружения к конкретному имени диска и/или пользовательским метаданным. Определение пользовательских свойств может помочь при последующей обработке события.

Политики можно определять на уровне хоста, группы хостов и среды.

1. Перейдите в **Settings** > **Anomaly detection** > **Infrastructure** > **Disk Edge**.
2. Нажмите **Add policy**.
3. Определите политику.

   * **Policy name**: имя, под которым будет отображаться политика.
   * **Operating system**: правила обнаружения можно задавать для выбранных ОС (если ни одна не выбрана, настройки не применяются).
   * **Alerts**: одно правило может содержать до семи оповещений — по одному для каждого типа события (см. таблицу ниже).
   * **Disk name filters**: правила можно фильтровать по имени диска.
   * **Host custom metadata conditions**: правила можно фильтровать по [пользовательским метаданным хоста](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.").
   * **Properties**: к отправляемому событию можно добавить свойства с использованием поддерживаемых заменителей:

     + `disk.all_mountpoints`
     + `disk.device_name`
     + `disk.mountpoint`
     + `dt.entity_host`
     + `dt.host_group.id`
     + `host.name`

| Событие | Серьёзность | Связанная метрика OneAgent |
| --- | --- | --- |
| Available disk space (%) below | Меньшее значение — более серьёзное | DiskStats object field: `availPercentage`   Mintv2 metric: `dt.host.disk.free`   Timeseries: `builtin:host.disk.free` |
| Available disk space (MiB) below | Меньшее значение — более серьёзное | DiskStats object field: `avail`   Mintv2 metric: `dt.host.disk.avail`   Timeseries: `builtin:host.disk.avail` |
| Available inodes (%) below | Меньшее значение — более серьёзное | DiskStats object field: `availINodesPercentag`   Mintv2 metric: `dt.host.disk.inodes_avail`   Timeseries: `builtin:host.disk.inodesAvail` |
| Available inodes (number) below | Меньшее значение — более серьёзное | Calculated from Diskstats: `totalINodes` \* `availINodesPercentage`   Mintv2 metric: `dt.host.disk.inodes_avail` \* `dt.host.disk.inodes_total`   Timeseries: `builtin:host.disk.inodesTotal` \* `builtin:host.disk.inodesAvail` |
| Is read only file system | N/A | Disk object field: `readOnly`   Mintv2 metric: N/A   Timeseries: N/A |
| Read time (ms) exceeding | Большее значение — более серьёзное | Disk object field: `readTime`   Mintv2 metric: `dt.host.disk.read_time`   Timeseries: `builtin:host.disk.readTime` |
| Write time (ms) exceeding | Большее значение — более серьёзное | Disk object field: `writeTime`   Mintv2 metric: `dt.host.disk.write_time`   Timeseries: `builtin:host.disk.writeTime` |

## Инфраструктура

### Анализ сети

Для быстрого выявления сетевых проблем перейдите в раздел **Network analysis**, в котором перечислены все сетевые интерфейсы с совокупными метриками и отдельными метриками для каждого интерфейса.

Используйте этот раздел, чтобы:

* Выявлять потери пакетов, пакеты с ошибками и другие сетевые проблемы
* Искать сетевые интерфейсы по имени сети
* Определять сетевые узкие места вплоть до конкретного адаптера

Использование графиков

Выберите в правом верхнем углу графика, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для соответствующего запроса.
* **Pin to dashboard** — закрепить копию выбранного графика на любой доступной для редактирования классической панели мониторинга. Подробнее см. в разделе [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

![Host overview: network analysis](https://dt-cdn.net/images/network-analysis-1597-a3306f3237.png)

Host overview: network analysis

### Анализ памяти

Используйте раздел **Memory analysis** для анализа:

* Использования памяти — общий объём памяти, используемая и восстанавливаемая память
* Ошибок страниц — ошибки страниц в секунду
* Использования swap — общий объём и используемый объём swap

Использование графиков

Выберите в правом верхнем углу графика, чтобы:

* **Show in Data Explorer** — открыть [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для соответствующего запроса.
* **Pin to dashboard** — закрепить копию выбранного графика на любой доступной для редактирования классической панели мониторинга. Подробнее см. в разделе [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

### События

Раздел событий отображает недавние события хоста, сгенерированные Davis AI, с наглядным представлением временной шкалы для быстрого выявления критических событий. Временная шкала интерактивна: она фильтрует события вокруг выбранного момента, что упрощает изоляцию конкретного события. Кроме того, различные типы событий обозначены цветом для удобства идентификации и навигации.

* **Show single card** — открывает карточку **Events** для выбранного хоста.

### Журналы

Временная шкала средства просмотра журналов интерактивна и позволяет выбирать глобальный временной диапазон. Используйте её для выявления проблем вокруг конкретного события журнала и оценки его связи с производительностью хоста или процессов.

* Весь временной диапазон страницы хоста синхронизируется с выбором в средстве просмотра журналов. Таким образом, можно легко сравнить запись об ошибке в журнале с метриками производительности хоста или процессов в момент её появления. Тот же временной диапазон будет применён к карточке событий.
* Журналы можно фильтровать по группе процессов, статусу, уровню журнала и другим параметрам, что позволяет, например, искать только журналы ошибок или журналы определённого процесса.

Использование этого раздела

Выберите в правом верхнем углу раздела **Logs**, чтобы:

* **Go to Log Viewer** — открыть страницу **Log Viewer**, отфильтрованную по выбранному хосту.
* **Create metric** — открыть страницу **Log metrics** со значением **Query**, заданным для выбранного хоста.