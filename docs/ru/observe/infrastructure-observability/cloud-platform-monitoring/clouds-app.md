---
title: Clouds app
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app
scraped: 2026-03-06T21:12:43.905190
---

# Приложение Clouds

# Приложение Clouds

* Последняя версия Dynatrace
* Приложение
* Чтение — 4 мин
* Обновлено 27 февраля 2026 г.

Новый [облачный интерфейсï»¿](https://www.dynatrace.com/platform/cloud-monitoring/) оптимизирован для команд облачных (платформенных) операций и инженеров по надёжности (SRE) и ориентирован на сценарии мониторинга состояния, устранения неполадок и оптимизации производительности (мульти-)облачных сред.

Центральный элемент этого интерфейса — ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

* Подключите свои облачные учётные записи и начните анализировать полный инвентарь облачных ресурсов за считанные минуты.
* Анализируйте метрики, события, логи, трассировки, метаданные и топологию виртуальных машин, бессерверных функций, баз данных, очередей, хранилищ, сетей и многого другого — в одном представлении.
* Используйте оповещения о состоянии для обеспечения оптимальной работоспособности и производительности. Сокращайте время устранения неполадок с помощью оповещений на основе ИИ.
* Используйте свои (существующие) облачные теги для маршрутизации уведомлений, определения владельцев или распределения затрат.
* Воспользуйтесь готовыми дашбордами для экономии времени и мгновенного получения аналитических данных.

Базовые данные наблюдаемости обеспечиваются [Grail](../../../platform/grail/dynatrace-grail.md "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), который поддерживает гибкую аналитику с помощью [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.") в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** и ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

![Получите полное представление о ваших мультиоблачных средах и просмотрите полный инвентарь облачных ресурсов](https://cdn.hub.central.dynatrace.com/hub/console/drafts/170/media/clouds-app-overview-aws-and-azure.png)![Детали проблем, связанных с выбранными облачными ресурсами, легко анализировать](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/8822a738-a2bf-4d75-bdfa-beabbb150a0e.png)![Просмотр полных деталей конфигурации облачных сервисов](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/b96f7374-5a8e-4c7a-b256-d79f469803a4.png)![Начните работу сразу с готовыми дашбордами. Настройте их в соответствии с вашими потребностями.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/170/media/08-ready-made-dashboard-aws-lambda.png)![Используйте готовые оповещения о состоянии и предупреждающие сигналы, а также пользовательские шаблоны оповещений для оценки работоспособности облачных сервисов.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/d7350ea9-6129-4818-8798-27514232ca8f.png)![Легко и быстро настройте новое подключение AWS. Новые облачные подключения упрощают процесс подключения для пользователей.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/170/media/06-clouds-app-new-aws-connection_2.png)![Вы по-прежнему можете использовать Explorer (Classic connections) для классических облачных подключений](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.clouds/media/f743e7e6-ec1d-488c-b0ae-5d5a3a8c98e5.png)

1 из 7 — Получите полное представление о ваших мультиоблачных средах и просмотрите полный инвентарь облачных ресурсов

## Предварительные требования

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** автоматически устанавливается как основное приложение, управляемое Dynatrace.

### Подключения

Новые облачные подключения (AWS, Azure)

Классические облачные подключения (AWS, Azure, GCP)

* SaaS-среда Dynatrace на базе Grail и AppEngine, размещённая в любом регионе AWS или подходящем регионе Azure
* Требуется [лицензия DPS](../../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") со следующими возможностями:

  + [Metrics powered by Grail](../../../license/capabilities/metrics.md "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")
  + [Logs powered by Grail](../../../license/capabilities/log-analytics.md "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")
  + [Events powered by Grail](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

* SaaS-среда Dynatrace на базе Grail и AppEngine
* Доступно для [лицензии DPS](../../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") и [классической лицензии](../../../license/monitoring-consumption-classic.md "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

См. [концепции](#concepts) для сравнения классических и новых облачных подключений.

### Разрешения

В следующей таблице описаны необходимые разрешения.

settings:objects:read

Чтение настроек владения (settings:schemaIds = builtin:ownership.config) — требуется для вкладки «Владение» в панели деталей.

unified-analysis:screen-definition:read

Чтение конфигурации экрана деталей. Необходимо для отображения панели деталей.

davis:analyzers:execute

Выполнение анализаторов Davis. Необходимо для отображения деталей проблем на вкладке «Проблемы» в панели деталей.

hub:catalog:read

Чтение каталога Hub.

app-settings:objects:read

Чтение объектов настроек приложения. Требуется для подключения логов в контексте.

app-settings:objects:write

Запись объектов настроек приложения.

slo:slos:read

Чтение для вкладки SLO.

state:user-app-states:read

Чтение состояния пользовательского приложения. Необходимо для отображения событий на вкладке «События» в панели деталей.

state:user-app-states:write

Сохранение состояния приложения для каждого пользователя.

document:documents:read

Чтение документов. Требуется для функции предустановленных фильтров. Требуется для готовых дашбордов (Обзор).

## Начало работы

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** имеет встроенный процесс подключения, который проведёт вас через все необходимые шаги для начала работы. Конкретные шаги зависят от вашего облачного провайдера и типа облачного подключения (нового или классического).

Если вы только начинаете работу с Dynatrace AWS Cloud Platform Monitoring, мы рекомендуем использовать новые подключения AWS вместо классических.

Новые облачные подключения (AWS, предварительная версия для Azure)

Классические облачные подключения (AWS, Azure, GCP)

Новые облачные подключения (AWS, предварительная версия для Azure)

Классические облачные подключения (AWS, Azure, GCP)

Используйте следующее руководство для настройки нового облачного подключения в Dynatrace.

[01Создание нового подключения AWS

* Руководство
* Узнайте, как создать новое подключение AWS в приложении Clouds.](clouds-app/create-aws-connection.md)[02Создание нового подключения Azure

* Руководство
* Узнайте, как создать новое подключение Azure в приложении Clouds.](clouds-app/create-azure-connection.md)

В ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** используйте панель заголовка приложения и выберите  **Create connection** > **AWS (Classic connections)** или  **Create connection** > **Azure (Classic connections)** или  **Create connection** > **GCP (Classic connections)**.

Все данные, поступающие от классических подключений, можно анализировать на вкладке **Explorer (Classic connections)**.

### Обзор (Новые подключения)

Вкладка **Overview New** — это начальная страница, на которой вы можете начать знакомство с ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**, получить данные в Dynatrace и увидеть сводку состояния работоспособности ваших сервисов AWS и/или Azure на основе новых облачных подключений. На этой странице вы можете:

* Выбрать плитку **AWS services** или **Azure services**, выбрать определённую категорию сервисов или нажать на счётчик в правом верхнем углу плитки, чтобы перейти на вкладку **Explorer New** со списком выбранных сервисов.
* Просмотреть состояние работоспособности облачных сервисов в зависимости от настроек оповещений. Чтобы отобразить нездоровые сервисы в **Explorer New**, нажмите на красный счётчик (при наличии) в правом верхнем углу плитки.
* Открыть готовые дашборды для наиболее популярных сервисов (например, AWS Lambda) или выбрать **Browse all dashboards**, чтобы просмотреть все готовые дашборды для AWS и/или Azure.

  ![Clouds app | Обзор](https://dt-cdn.net/images/clouds-app-overview-3840-c1c071fe6a.png)

### Обозреватель (Новые подключения)

Используйте вкладку **Explorer New** для анализа ваших облачных сервисов и сред AWS. Вы можете изучать, фильтровать и анализировать данные с помощью различных функций в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

* На боковой панели слева вы можете выбрать определённую категорию сервисов (например,  **Containers** или  **Functions**) или проанализировать все сервисы. Кроме того, вы можете быстро отфильтровать данные по предопределённым атрибутам, актуальным для выбранной категории. Выберите любой атрибут на боковой панели фасетов и нажмите **Update**, чтобы получить результаты. Поле фильтра обновится в соответствии с вашим выбором.
* Также вы можете выбрать поле фильтра вверху для просмотра предложений и ввода параметров фильтрации. Добавьте дополнительные условия для сужения результатов. Критерии одного типа группируются по логике `OR`. Критерии разных типов группируются по логике `AND`. Вы можете фильтровать сервисы по тегам, статусу оповещений и атрибутам, таким как имя или регион. Это помогает сосредоточиться на конкретных подмножествах сервисов на основе ваших критериев.

  Подробнее о синтаксисе поля фильтра см. в разделе [Поле фильтра](../../../discover-dynatrace/get-started/dynatrace-ui/ui-filter-field.md "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").
* Вы можете изучать данные в таблице, используя доступные перспективы:

  + **Health**
  + **Utilization** (для вычислительных сервисов)
  + **Metadata**
  + Чтобы настроить отображаемые детали результатов в таблице, выберите **Column settings** и укажите столбцы, которые хотите отобразить.

  ![Clouds app | Explorer — фильтрация — использование](https://dt-cdn.net/images/clouds-app-explorer-filtering-utilization-3840-2ec09e9078.png)
* Выберите конкретный облачный сервис в таблице, чтобы проанализировать все данные в контексте: метрики, логи, события, метаданные, конфигурацию и топологию.

  Нажмите ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Go to dashboard**, чтобы перейти к соответствующему готовому дашборду с сохранением выбранного временного интервала и фильтров.

  ![Clouds app | Explorer — просмотр деталей](https://dt-cdn.net/images/clouds-app-explorer-details-view-3840-1790feeb80.png)

### Оповещения (Новые подключения)

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** предоставляет готовые оповещения о состоянии и предупреждающие сигналы для ваших облачных сервисов, а также шаблоны оповещений для настройки дополнительных пользовательских оповещений для популярных сервисов AWS.

#### Оповещения о состоянии и предупреждающие сигналы

Оповещения о состоянии и предупреждающие сигналы предоставляются и поддерживаются Dynatrace из коробки.

* Оповещение о состоянии создаёт проблему Dynatrace, которая запускает анализ первопричин в Dynatrace.
* Предупреждение создаётся для ресурса, когда наблюдение не является критическим и не должно создавать проблему.

  Оповещения о состоянии и предупреждающие сигналы отображаются в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

Вы можете легко активировать готовые оповещения о состоянии и предупреждающие сигналы для своих учётных записей AWS либо при [подключении AWS](../../../ingest-from/amazon-web-services/create-an-aws-connection/aws-connection-app-settings.md "Onboard your AWS environments and create AWS connections via the Settings app."), либо в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

Если вы хотите создать новые или обновить готовые оповещения о состоянии и предупреждающие сигналы, перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Alerts** > **Cloud services**, где вы можете создавать, обновлять и включать/отключать оповещения для ваших подключений.

* Область действия оповещения

  + **Actor** (сервисный пользователь): укажите сервисного пользователя Dynatrace, от имени которого будет выполняться оценка оповещений (и, соответственно, запросы). Сервисный пользователь должен иметь как минимум следующие разрешения:

    - `storage:metrics:read`
    - `storage:buckets:read`
    - `davis:analyzers:execute`
  + **Alert scope** (регион): позволяет фильтровать оценку оповещений только для определённых регионов. Например, фильтр по `us-east-1` обеспечит получение оповещений и предупреждений только для облачных сервисов, размещённых в этом регионе.
  + Условия оповещений
  + В зависимости от модели обнаружения настроенного оповещения вы можете настроить различные параметры, такие как порог и количество колебаний сигнала.

![Settings | Готовые оповещения](https://dt-cdn.net/images/settings-ready-made-alerts-3840-d19f21a2a8.png)![Settings | Детали оповещения о состоянии](https://dt-cdn.net/images/settings-health-alert-details-3840-f4fc0982c7.png)

1 из 2

#### Шаблоны оповещений

Dynatrace предоставляет предопределённые шаблоны оповещений для настройки дополнительных пользовательских оповещений для популярных облачных сервисов. Эти шаблоны дополняют готовые оповещения о состоянии и предупреждающие сигналы.

Вы можете легко создать новые [пользовательские оповещения](../../../dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app.") непосредственно в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**, выбрав шаблон и нажав  **New Alert**.

Далее вы можете либо настроить оповещение в мастере обнаружения аномалий, либо создать оповещение одним нажатием.

![Clouds app | Пользовательские шаблоны оповещений](https://dt-cdn.net/images/clouds-app-custom-alerts-template-3840-e1a42bda6c.png)

Все пользовательские оповещения и дополнительную информацию о возможностях и ограничениях вы найдёте в [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](../../../dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app.").

### Обозреватель (Классические подключения)

Вкладка **Explorer (Classic connections)** отображает данные, поступающие от классических облачных подключений, и позволяет анализировать облачные сервисы AWS, Azure и GCP.

Если вы уже использовали Dynatrace для мониторинга облачных платформ, классические подключения и **Explorer (Classic connections)** продолжают предоставлять те же возможности.

![Clouds app | Explorer (Classic connections)](https://dt-cdn.net/images/clouds-app-explorer-classic-connections-3840-a96bf1622d.png)

## Концепции

### Новые облачные подключения и классические облачные подключения

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** предоставляет полное представление о ваших (мульти-)облачных средах, позволяя оптимизировать состояние, производительность и использование ресурсов ваших облачных сервисов.

В настоящее время ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** поддерживает два типа облачных подключений:

Новые облачные подключения (AWS, предварительная версия для Azure)

Новейшие облачные платформенные подключения от Dynatrace предоставляют более простой, гибкий и мощный способ подключения учётных записей AWS и Azure к Dynatrace. Поддержка GCP будет добавлена в ближайшее время.

Все данные нативно хранятся в Grail и отображаются на вкладках **Overview New** и **Explorer New** в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

Классические подключения

Классические облачные подключения доступны для AWS, Azure и GCP в предыдущей (**AWS Classic**, **Azure Classic**, **GCP Classic**) и последней версии Dynatrace.

Классические подключения отображаются на вкладке **Explorer (Classic connection)** в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** и не имеют специальных лицензионных требований.

Если вы только начинаете работу с Dynatrace AWS Cloud Platform Monitoring, мы рекомендуем использовать новые подключения AWS вместо классических.

Вкладки **Explorer** New и **Overview** New работают только с данными, поступающими от новых облачных подключений AWS.

Поддержка Azure и GCP будет добавлена в будущем.

### Перспективы: Health, Utilization и Metadata (Новые подключения)

Каждую перспективу мониторинга ваших облачных сервисов можно настроить под ваши потребности, показывая или скрывая столбцы в таблице.

* **Health** — предоставляет информацию о состоянии работоспособности
* **Utilization** (доступно для вычислительных сервисов) — фокусируется на операционной эффективности
* **Metadata** — отображает дополнительную информацию, например облачные теги

#### Оповещения о состоянии и пользовательские оповещения

В перспективе **Health** вы можете видеть состояние работоспособности каждого облачного сервиса и пользовательские оповещения. При наведении курсора на значок оповещения о состоянии или пользовательского оповещения вы увидите проблемы и дополнительные варианты анализа.

* Нажмите  **View event**, чтобы перейти непосредственно к деталям, например к соответствующим метрикам для данной проблемы.
* Нажмите  **Investigate problem**, чтобы перейти в **режим проблемы**.

**Режим проблемы** обеспечивает точное исследование и анализ любых проблем, связанных с работоспособностью.

* Этот режим выделяет наиболее релевантные метрики, связанные с оповещением, и сужает временной интервал до времени начала и окончания выбранной проблемы.
* Кроме того, он обеспечивает быстрый доступ к базовой проблеме, позволяя эффективно диагностировать и устранять неполадки.
* Вы можете использовать [агентный и генеративный ИИ Dynatrace Intelligence](../../../dynatrace-intelligence/copilot.md "Learn about Dynatrace Intelligence agentic and generative AI.") для получения дополнительных сведений о проблеме и возможных шагах по её устранению.

**Режим проблемы** всегда активен, когда вы переходите от конкретной проблемы в [![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**](../../../dynatrace-intelligence/davis-problems-app.md "Use the Problems app to quickly get to the root cause of incidents in your environment.") в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.

![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** работает в **режиме проблемы** всякий раз, когда проблема выделена рядом с панелью фильтров в верхней части приложения.

### Готовые дашборды (Новые подключения)

Вам доступны готовые дашборды для нового AWS Cloud Platform Monitoring и Azure Cloud Platform Monitoring (предварительная версия).

Доступ к готовым дашбордам можно получить через:

* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

  Откройте ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, выберите [Готовые дашборды](../../../analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-dashboards.md "Use ready-made dashboards to visualize your data right out of the box.") в левом меню и выполните поиск по запросу `aws`.
* ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**

  + Откройте ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** и выберите вкладку **Overview New**. Затем вы можете выбрать один из наиболее популярных дашбордов (например, AWS Lambda) или нажать **Browse all dashboards**.
  + ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** позволяет перейти от конкретного сервиса к соответствующему дашборду в контексте ( ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Go to dashboard**). Выбранный временной интервал, сегмент и применённые фильтры будут перенесены из ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** в дашборд.

![Clouds app | Навигация по дашбордам](https://dt-cdn.net/images/clouds-app-dashboard-navigation-3840-d0998aa51b.png)

### Сегменты (Новые подключения)

[Сегменты](../../../manage/segments.md "Use segments to logically structure and conveniently filter observability data across apps.") позволяют логически структурировать и удобно фильтровать данные наблюдаемости в приложениях на платформе Dynatrace. Сегменты доступны на новой вкладке **Explorer New** и могут быть легко определены для новых облачных подключений, поскольку все данные (включая [узлы Smartscape](../../../platform/grail/smartscape-on-grail.md "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.")) хранятся в Grail.

Пошаговое руководство по определению сегментов для узлов Smartscape см. в разделе [Фильтрация узлов Smartscape с помощью сегментов](../../../manage/segments/getting-started/segments-getting-started-filter-smartscape-nodes.md "Learn how to filter Smartscape nodes by using segments in Dashboards."). Вы можете использовать любое первичное поле Grail (а в будущем также теги) для удобного определения простых сегментов для **всех данных**:

* [Первичные поля Grail](../../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.") (например, `aws.account.id`, `aws.region`)
* Первичные теги Grail (в будущем)

Пример определения сегмента по идентификатору учётной записи AWS:

![Сегмент — учётная запись AWS](https://dt-cdn.net/images/simple-segment-aws-account-3840-1b8915174b.png)

В ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** (или любом другом приложении, поддерживающем сегменты) вы можете выбрать сегмент `AWS account` и указать один или несколько `awsAccountIDs` для фильтрации.

## Сценарии использования

* Понимание архитектуры и зависимостей ваших (мульти-)облачных сред
* Оценка работоспособности ваших облачных сервисов
* Устранение неполадок в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**
* Анализ производительности и использования ресурсов

## Часто задаваемые вопросы

### Что делать, если у меня уже есть облачные подключения?

Существующие классические облачные подключения остаются без изменений и не обновляются и не удаляются автоматически.

Чтобы воспользоваться новым AWS Cloud Platform Monitoring, необходимо создать новое облачное подключение для ваших учётных записей AWS.

Одна и та же учётная запись AWS для классического и нового облачных подключений

Мы не рекомендуем настраивать классическое и новое облачные подключения для одной и той же учётной записи AWS. Для разнородного набора учётных записей AWS классические и новые облачные подключения могут сосуществовать.

### Как присоединиться к предварительной версии Azure?

Дополнительную информацию и возможность присоединиться к предварительной версии Cloud Platform Monitoring для Azure вы найдёте на нашей [странице программы предварительных версий](../../../../common/whats-new/preview-releases.md#new-cloud-platform-monitoring-for-azure "Learn about our Preview releases and how you can participate in them.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучите в Dynatrace Hub

[Подключите ваши новые мультиоблачные среды и мониторьте их ресурсы.](https://www.dynatrace.com/hub/detail/clouds/?internal_source=doc&internal_medium=link&internal_campaign=cross)
