---
title: Расчёт потребления Full-Stack Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/full-stack-monitoring
scraped: 2026-05-12T11:06:26.918934
---

# Расчёт потребления Full-Stack Monitoring (DPS)

# Расчёт потребления Full-Stack Monitoring (DPS)

* Explanation
* 5-min read
* Updated on Jan 26, 2026

Full-Stack Monitoring для хостов и контейнеров обеспечивает всесторонний мониторинг производительности приложений.
Мониторинг производительности приложений включает: распределённую трассировку, видимость на уровне кода, профилирование CPU, профилирование памяти и глубокий мониторинг процессов для хостов и контейнеров.

* Full-Stack Monitoring на основе хоста:

  + Потребление основано на памяти хоста, см. [GiB-часы](#gib-hour).
  + Дополнительно включает все функции [Infrastructure Monitoring](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring "Learn how your consumption of the Dynatrace Infrastructure Monitoring DPS capability is billed and charged.").

  + На хостах с Full-Stack Monitoring на основе хоста можно включать расширения Dynatrace Extensions, которые могут потреблять [точки данных пользовательских метрик Full-Stack](#full-stack-metrics) и [Log Analytics](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
* Full-Stack Monitoring только для приложений в контейнерах: потребление основано на памяти контейнера, см. [расчёт GiB-часов для мониторинга только приложений в контейнерах](#app-only-gib-hour)[1](#fn-1-1-def).

Дополнительные сведения о поддерживаемых платформах см. в [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

1

Full-Stack Monitoring только для приложений в контейнерах не включает Infrastructure Monitoring или Kubernetes Platform Monitoring.

## GiB-часы

Dynatrace использует GiB-часы (в тарифной карте именуются «memory-gibibyte-hours») в качестве единицы измерения для расчёта потребления мониторинга хостов в режиме Full-Stack Monitoring.
Чем больше памяти у хоста и чем дольше он мониторируется, тем выше число потребляемых GiB-часов.

Преимущество подхода GiB-часов к потреблению мониторинга — его простота и прозрачность.
Специфические для технологий факторы (например, количество JVM или микросервисов на сервере) не влияют на потребление.
Неважно, работает ли хост под управлением Kubernetes или других контейнеризированных приложений, .NET- или Java-приложений.
Можно иметь 10 или 1 000 JVM — такие факторы не влияют на потребление мониторинга окружением.

### Детализация тарификации потребления GiB-часов

Dynatrace создан для динамичных облачных сред, где хосты и сервисы быстро запускаются и уничтожаются.
Поэтому детализация тарификации потребления GiB-часов рассчитывается в 15-минутных интервалах.
Если хост или контейнер отслеживается менее 15 минут в интервале, потребление GiB-часов округляется до 15 минут перед расчётом.

### Расчёт GiB-часов для физических хостов и виртуальных машин (ВМ)

Каждый установленный экземпляр Dynatrace OneAgent, запущенный на экземпляре операционной системы (например, на физической или виртуальной машине) в режиме Full-Stack Monitoring, потребляет GiB-часы на основе физической или виртуальной оперативной памяти мониторируемого хоста, рассчитанной в 15-минутных интервалах (см. пример диаграммы ниже).

ОЗУ каждой ВМ или хоста округляется до следующего кратного 0,25 GiB (что соответствует 256 MiB) перед расчётом потребления мониторинга.
К потреблению GiB-часов для физических и виртуальных хостов применяется минимум 4 GiB.
Например, хост с 8,3 GiB памяти считается как 8,5 GiB (следующее кратное 0,25 GiB), а хост с 2 GiB памяти считается как 4 GiB (округления не требуется, но применяется минимум 4 GiB).

### Расчёт GiB-часов для мониторинга только приложений в контейнерах

В облачных средах сервисы и хосты часто кратковременны.
Поэтому расчёт потребления мониторинга в 15-минутных интервалах, а не в полных часах, лучше отражает фактическое использование.
Контейнеры, являющиеся ключевым механизмом в облачных средах, как правило, используют меньше памяти, чем хосты.
Поэтому минимальный порог памяти для контейнеров составляет 256 MiB, а не 4 GiB, как для хостов.

То же правило округления до следующего кратного 0,25 GiB применяется и к контейнерам.
Например, контейнер с 780 MiB памяти считается как 1 GiB контейнер (780 MiB = 0,78 GiB, округляется до следующего кратного 0,25 GiB).

На рисунке ниже показан расчёт потребления GiB-часов в 15-минутных интервалах.
Каждый интервал делится на четыре для получения единицы измерения потребления GiB-часов.

![Full-Stack consumption](https://dt-cdn.net/images/fullstack-monitoring-consumption-5584-2d3c737d8b.jpg)

Потребление Full-Stack

#### Расчёты размера памяти

Расчёты размера памяти для контейнеров, отслеживаемых в режиме только приложений, основаны на:

* Использованной памяти контейнера.

  + OneAgent версии 1.275+ (для контейнеров Kubernetes)
  + OneAgent версии 1.297+ (для serverless-контейнеров)
* Ограничениях памяти контейнера.
  Если ограничение памяти не задано, используется память базовой виртуальной машины.

  + OneAgent версии <1.275 (для контейнеров Kubernetes)
  + OneAgent версии <1.297 (для serverless-контейнеров)

[Автоматическое обнаружение контейнеров](/managed/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection#automatic-container-detection "Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.") необходимо включить для существующих тенантов.

Для некоторых сценариев мониторинга предусмотрены собственные расчёты потребления GiB-часов, как описано в таблице ниже.

| Сценарий | Описание |
| --- | --- |
| Azure App Services (запущенные по выделенному плану App Service для Windows) | Потребление основано на числе и памяти экземпляров плана. Не важно, сколько приложений работает на экземплярах. Минимальная тарифицируемая память составляет 256 MiB (вместо 4 GiB). |
| Azure App Service (работающий на Linux или в Linux-контейнерах) OneAgent версии 1.297+ | При включённом автоматическом обнаружении контейнеров: потребление основано на использованной памяти контейнера. Если автоматическое обнаружение не включено: потребление основано на памяти экземпляра плана, умноженной на количество запущенных контейнеров. |
| Azure App Service (работающий на Linux или в Linux-контейнерах) OneAgent версии <1.297 | Потребление основано на памяти экземпляра плана, умноженной на количество запущенных контейнеров, независимо от того, включено ли автоматическое обнаружение контейнеров. |
| Oracle Solaris Zones | Зоны Solaris считаются хостами. |
| Мониторируемые контейнеры, не обнаруженные как контейнеры | Эти контейнеры считаются хостами. |

## Метрики

Этот раздел предполагает, что вы следовали рекомендуемым Dynatrace вариантам развёртывания, особенно в отношении обогащения телеметрии.
При реализации пользовательского развёртывания тарификация включённых метрик может работать так, как описано, — но это не гарантируется Dynatrace.

Дополнительные сведения см. в [Поддерживаемые варианты развёртывания](#deployment-options).

Full-Stack Monitoring включает все метрики Infrastructure Monitoring, метрики мониторинга производительности приложений и [другие встроенные метрики](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.").
Эти метрики включены и никогда не тарифицируются.

Full-Stack Monitoring также включает определённый объём точек данных пользовательских метрик.
Каждый Contributing GiB памяти хоста или приложения добавляет 900 точек данных пользовательских метрик в каждом 15-минутном интервале.
Включённые точки данных метрик, не использованные в 15-минутном интервале предоставления, не переносятся на последующие интервалы.
Включённые точки данных метрик окружения автоматически применяются к метрикам, происходящим с хостов и контейнеров, мониторируемых OneAgent в режиме Full-Stack Monitoring.

Все ключи метрик, начинающиеся с `dt.service.*`, предназначены для [мониторинга сервисов](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") и потребляют включённые точки данных метрик Full-Stack, если данные спанов происходят с хостов и контейнеров, мониторируемых OneAgent в режиме Full-Stack Monitoring.
Если данные спанов происходят из другого источника, эти метрики тарифицируются как [Metrics powered by Grail](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
Такие ключи метрик включают, например:

* `dt.service.request.count`
* `dt.service.request.failure_count`
* `dt.service.request.response_time`
* `dt.service.request.service_mesh.count`
* `dt.service.request.service_mesh.failure_count`
* `dt.service.request.service_mesh.response_time`
* `dt.service.messaging.process.count`
* `dt.service.messaging.process.failure_count`
* `dt.service.messaging.publish.count`
* `dt.service.messaging.receive.count`

Точки данных метрик, превышающие включённый объём, тарифицируются как [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

Включённые точки данных метрик окружения автоматически применяются к метрикам, происходящим с хостов и контейнеров, мониторируемых OneAgent в режиме Full-Stack Monitoring.
Это применяется к пользовательским метрикам, как описано в таблице ниже.

| Источник | Примеры (включая, но не ограничиваясь) |
| --- | --- |
| Хост с Full-Stack, отправляющий метрики через [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | * OpenTelemetry метрики * Spring Micrometer * StatsD * JMX * Расширения, запущенные локально на хосте OneAgent * локальный на хосте Telegraf |
| Приложение, мониторируемое с Full-Stack только для приложений в контейнерах через кодовый модуль OneAgent | * OpenTelemetry метрики * Spring Micrometer * JMX |
| Узел Kubernetes с Full-Stack мониторингом — Cloud Native Full-Stack или Classic Full-Stack | * OpenTelemetry метрики * Spring Micrometer * JMX * Prometheus (через ActiveGate). * Не включает метрики, собранные через OpenTelemetry collector. |
| [Мониторинг сервисов](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") | * `dt.service.request.count` * `dt.service.request.failure_count` * `dt.service.request.response_time` * `dt.service.request.service_mesh.count` * `dt.service.request.service_mesh.failure_count` * `dt.service.request.service_mesh.response_time` |

### Пример расчёта включённых точек данных метрик

На основе примера, показанного на Рисунке 1, приведены расчёты включённых объёмов точек данных метрик для каждого из четырёх 15-минутных интервалов, предполагая 900 включённых точек данных метрик за каждый 15-минутный интервал.

* Первый 15-минутный интервал: `900 (включённые точки данных) × 13,5 (GiB памяти) = 12 150 включённых точек данных`
* Второй 15-минутный интервал: `900 (включённые точки данных) × 9,5 (GiB памяти) = 8 550 включённых точек данных`
* Третий 15-минутный интервал: `900 (включённые точки данных) × 8,75 (GiB памяти) = 7 875 включённых точек данных`
* Четвёртый 15-минутный интервал: `900 (включённые точки данных) × 0,25 (GiB памяти) = 225 включённых точек данных`

### Как потребляются точки данных метрик в режиме Full-Stack Monitoring

Потребление точек данных метрик может принимать различные формы.
Одинаковое число точек данных может потребляться:

* Несколькими метриками с высоким разрешением или многочисленными метриками с низким разрешением.
* Равномерно в нескольких 15-минутных интервалах или всё сразу за одну минуту.
* Всеми мониторируемыми хостами, частью Full-Stack-хостов или единственным хостом.

### Профилирование CPU, памяти и потоков

Full-Stack Monitoring включает профилирование [CPU](/managed/observe/application-observability/profiling-and-optimization/cpu-profiling "Learn how you can use Dynatrace to perform enhanced code analysis."), [памяти](/managed/observe/application-observability/profiling-and-optimization/memory-profiling "Analyze memory allocation with Dynatrace.") и потоков для таких технологий, как Java, .NET, Go, Node.js и PHP.
OneAgent использует интеллектуальный запатентованный механизм для управления объёмом данных профилирования.
Dynatrace [сохраняет общий объём принятых данных профилирования](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.") из вашего окружения в течение 10 дней.

## Поддерживаемые варианты развёртывания

Чтобы гарантировать, что пользовательские метрики получают преимущество от включённых объёмов трасс и метрик, необходимо включить обогащение телеметрии в соответствии с рекомендуемыми Dynatrace вариантами развёртывания.

Автоматическое обогащение телеметрии включено для:

* Пользовательских метрик, происходящих с:

  + Любого хоста или контейнера с Full-Stack Monitoring — при использовании OneAgent или следовании шагам из [Обогащение поступающих данных полями Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").
  + Любого контейнера Kubernetes с Full-Stack Monitoring — при использовании Dynatrace Operator с [включённым обогащением метаданных](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.").
  + Любого узла Kubernetes с Cloud-Native Full-Stack Monitoring — при использовании Dynatrace Operator с [включённым обогащением метаданных](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.").
    Включает все контейнеры, работающие на мониторируемом узле Kubernetes.
* Пользовательских метрик, отправляемых с любого хоста с Full-Stack Monitoring через локальный metric API OneAgent. Дополнительные сведения см. в [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

При реализации пользовательского развёртывания тарификация метрик может работать так, как описано, — но это не гарантируется Dynatrace.

## Детали потребления: Full-Stack

Dynatrace предоставляет встроенные метрики использования, помогающие понять и анализировать потребление Full-Stack Monitoring в вашей организации.
Чтобы использовать эти метрики, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите `DPS` в поле **Search**.
Эти метрики также доступны через Environment API и в Account Management (**Usage summary** > **Full-Stack Monitoring** > **Actions** > **View details**).

Ниже перечислены метрики для мониторинга потребления Dynatrace Full-Stack Monitoring.

(DPS) Full-Stack Monitoring billing usage
:   Ключ: `builtin:billing.full_stack_monitoring.usage`

    Измерение: count

    Разрешение: 15 мин

    Описание: Суммарная память GiB всех хостов в режиме Full-Stack Monitoring, подсчитанная в 15-минутных интервалах.

(DPS) Full-Stack Monitoring billing usage per host
:   Ключ: `builtin:billing.full_stack_monitoring.usage_per_host`

    Измерение: Хост (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: Память GiB на хост в режиме Full-Stack Monitoring, подсчитанная в 15-минутных интервалах.

(DPS) Full-stack usage by container type
:   Ключ: `builtin:billing.full_stack_monitoring.usage_per_container`

    Измерение: application\_only\_type; k8s.cluster.uid; k8s.namespace.name

    Разрешение: 15 мин

    Описание: Память GiB на контейнер в режиме Full-Stack только для приложений, подсчитанная в 15-минутных интервалах.

(DPS) Total metric data points reported by Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.ingested`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Число зафиксированных точек данных метрик, агрегированных по всем хостам с Full-Stack Monitoring.

(DPS) Metric data points reported and split by Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.ingested_by_host`

    Измерение: Хост (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: Число зафиксированных точек данных метрик с разбивкой по хостам с Full-Stack Monitoring.

(DPS) Available included metric data points for Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.included`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Общее число включённых точек данных метрик, вычитаемых из потреблённых точек данных метрик хостов с Full-Stack Monitoring.

(DPS) Used included metric data points for Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.included_used`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Число использованных включённых точек данных метрик хостов с Full-Stack Monitoring.

### Мониторинг потребления memory-GiB-часов для хостов с Full-Stack Monitoring

Вы можете отслеживать суммарное потребление memory-GiB-часов, агрегированное по всем хостам с Full-Stack Monitoring, для различных интервалов (15 мин, час, день или неделя) и любого выбранного временного диапазона, используя метрику «(DPS) Full-Stack Monitoring billing usage».
В примере ниже показаны мониторируемые GiB памяти в 1-часовых интервалах.
Между 11:00 и 14:00 каждый час мониторировалось 523 GiB памяти.
Это означает потребление 523 memory-GiB-часов.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image001-1183-79f381ccb1.png)

Full-Stack Monitoring (DPS)

Можно детализировать суммарное потребление memory-GiB-часов с помощью метрики «(DPS) Full-Stack Monitoring billing usage per host».
В примере ниже показан список всех хостов, внёсших вклад в потребление 523 memory-GiB-часов между 13:00 и 14:00.
Также отображается соответствующее число memory-GiB-часов на хост.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image004-905-f0e44ad601.png)

Full-Stack Monitoring (DPS)

### Мониторинг потребления memory-GiB-часов для контейнеров с Full-Stack Monitoring

Владельцы платформы и кластеров могут мониторировать кластеры Kubernetes с помощью [Kubernetes Platform Monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
Владельцы приложений могут использовать Full-Stack Monitoring на основе контейнеров для мониторинга приложений в кластерах Kubernetes.

Для получения аналитики потребления по мониторируемым кластерам или пространствам имён Kubernetes можно запросить потребление memory-GiB-часов с помощью метрики «(DPS) Full-Stack Monitoring billing usage per container», как показано в следующем запросе:

`builtin:billing.full_stack_monitoring.usage_per_container:filter(eq("application_only_type","kubernetes")):splitBy()`

В примере ниже кластером Kubernetes за последние 30 дней было потреблено 1,58 TiB памяти.

![Kubernetes Platform Monitoring](https://dt-cdn.net/images/billing-full-stack-monitoring-usage-per-container-1025-3019577b21.png)

Kubernetes Platform Monitoring

Конечно, анализ можно детализировать (например, добавить разбивку по пространствам имён Kubernetes).

![Kubernetes Platform Monitoring](https://dt-cdn.net/images/billing-full-stack-monitoring-usage-per-container-by-namespace-1023-c5e1c10583.png)

Kubernetes Platform Monitoring

### Мониторинг потребления метрик для хостов с Full-Stack Monitoring

Для мониторинга бюджета метрик по всему пулу точек данных метрик в окружении можно сравнивать доступные включённые точки данных с общим числом зафиксированных точек данных метрик, используя метрики «(DPS) Available included metric data points for Full-Stack monitored hosts» и «(DPS) Total metric data points reported by Full-Stack monitored hosts».
В примере ниже показаны данные за полный день.
Число включённых метрик пула метрик этого окружения (фиолетовая линия) ни разу не было превышено.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image005-1212-35369921df.png)

Full-Stack Monitoring (DPS)

В случаях, когда число включённых метрик пула метрик окружения превышено, следующий анализ поможет выявить хосты, ответственные за превышение.
Используйте метрику «(DPS) Metric data points reported and split by Full-Stack monitored hosts».

В примере ниже показано, что между 10:45 и 11:00 каждый из первых 3 хостов в списке зафиксировал значительно больше 2 000 точек данных метрик.
За тот же период каждый из этих 3 хостов показывает потребление memory-GiB-часов в размере 2 GiB.
Dynatrace предлагает 900 включённых пользовательских точек данных метрик на каждый GiB памяти хоста, рассчитанных в 15-минутных интервалах.
Это означает, что первые 3 хоста вносят 1 800 (2×900) точек данных в пул доступных точек данных окружения.
Однако за тот же период эти хосты потребили больше точек данных, чем внесли.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image008-905-929928d644.png)

Full-Stack Monitoring (DPS)

При использовании метрики «(DPS) Total metric data points billed for Full-Stack monitored hosts» из Custom Metrics Classic можно видеть, что между 10:45 и 11:00 превышения пула метрик Full-Stack Monitoring для этого окружения не было, поскольку тарифицируемых точек данных метрик не зафиксировано.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image009-1210-914bc4742c.png)

Full-Stack Monitoring (DPS)

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)