---
title: Как понять и управлять расходом Full-Stack Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/full-stack-monitoring
---

# Как понять и управлять расходом Full-Stack Monitoring (DPS)

# Как понять и управлять расходом Full-Stack Monitoring (DPS)

* Пояснение
* 5 мин на чтение
* Обновлено 09 июня 2026 г.

Full-Stack Monitoring для хостов и контейнеров предоставляет комплексный мониторинг производительности приложений.
Мониторинг производительности приложений включает: распределённую трассировку, видимость на уровне кода, профилирование CPU, профилирование памяти и глубокий мониторинг процессов для хостов и контейнеров.

* Full-Stack Monitoring на базе хостов:

  + Расход рассчитывается на основе объёма памяти хоста, см. [ГиБ-часы](#gib-hour).
  + Дополнительно предоставляет все возможности [Infrastructure Monitoring](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring "Узнайте, как рассчитывается расход Infrastructure Monitoring, как отслеживать и анализировать использование и как оптимизировать затраты.").

  + Dynatrace Extensions можно включить на хостах с Full-Stack Monitoring на базе хостов, и это может расходовать [точки данных пользовательских метрик Full-Stack](#full-stack-metrics) и [Log Analytics](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").
* Full-Stack Monitoring на базе контейнеров, только для приложений: расход рассчитывается на основе объёма памяти контейнера, см. [Расчёт ГиБ-часов для мониторинга контейнеров только для приложений](#app-only-gib-hour)[1](#fn-1-1-def).

Подробнее о поддерживаемых платформах см. [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.").

1

Full-Stack Monitoring на базе контейнеров, только для приложений, не включает Infrastructure Monitoring или Kubernetes Platform Monitoring.

## ГиБ-часы

Dynatrace использует ГиБ-часы (в прайс-листе обозначаются как «memory-gibibyte-hours») в качестве единицы измерения для расчёта расхода мониторинга хостов вашей организации в режиме Full-Stack Monitoring.
Чем больше памяти у хоста и чем дольше хост находится под мониторингом, тем выше число ГиБ-часов, которое расходует хост.

Преимущество подхода ГиБ-часов к расходу мониторинга, это его простота и прозрачность.
Технологические особенности (например, число JVM или число микросервисов, размещённых на сервере) не влияют на расход.
Неважно, работает ли на хосте Kubernetes или другие контейнеризированные приложения, приложения на .NET, приложения на Java или что-то ещё.
На хосте может быть 10 или 1000 JVM, такие факторы не влияют на расход мониторинга среды.

### Гранулярность биллинга для расхода ГиБ-часов

Dynatrace создан для динамических cloud-native сред, где хосты и сервисы быстро создаются и уничтожаются.
Поэтому гранулярность биллинга для расхода ГиБ-часов рассчитывается с интервалом в 15 минут.
Если хост или контейнер находится под мониторингом менее 15 минут в течение интервала, расход ГиБ-часов округляется до 15 минут перед расчётом.

### Расчёт ГиБ-часов для физических хостов и виртуальных машин (ВМ)

Каждый установленный экземпляр Dynatrace OneAgent, работающий на экземпляре операционной системы (развёрнутой, например, на физической или виртуальной машине) в режиме Full-Stack Monitoring, расходует ГиБ-часы на основе физической или виртуальной оперативной памяти отслеживаемого хоста, рассчитываемой с интервалом в 15 минут (см. пример диаграммы ниже).

Объём оперативной памяти каждой ВМ или хоста округляется до следующего кратного 0,25 ГиБ (что соответствует 256 МиБ) перед расчётом расхода мониторинга.
К расходу ГиБ-часов для физических и виртуальных хостов применяется минимум 4 ГиБ.
Например, хост с 8,3 ГиБ памяти учитывается как хост с 8,5 ГиБ, это следующее кратное 0,25 ГиБ, а хост с 2 ГиБ памяти учитывается как хост с 4 ГиБ (округление не требуется, но применяется минимум 4 ГиБ).

### Расчёт ГиБ-часов для мониторинга контейнеров только для приложений

В cloud-native средах сервисы и хосты часто недолговечны.
Поэтому расчёт расхода мониторинга с интервалом в 15 минут, а не по полным часам, лучше отражает фактическое использование.
Контейнеры, важный механизм в cloud-native средах, обычно используют меньше памяти, чем хосты.
Поэтому минимальный порог памяти для контейнеров составляет 256 МиБ, а не 4 ГиБ, минимальный порог памяти для хостов.

К контейнерам применяется то же округление, что и к хостам, до следующего кратного 0,25 ГиБ.
Например, контейнер с 780 МиБ памяти учитывается как контейнер с 1 ГиБ (780 МиБ, что равно 0,78 ГиБ, округляется до следующего кратного 0,25 ГиБ).

На рисунке ниже показано, как учитывается память при расчёте расхода ГиБ-часов с интервалом в 15 минут.
Каждый интервал делится на четыре, чтобы получить единицу измерения расхода ГиБ-часов.

![Расход Full-Stack Monitoring](https://cdn.bfldr.com/B686QPH3/as/24t96b8x58jjvgphb4xg5cvh/Full-Stack_Monitoring_Consumption-Light_Mode?auto=webp&format=png&position=1)

Расход Full-Stack Monitoring

#### Расчёт размера памяти

Расчёт размера памяти для контейнеров, отслеживаемых по подходу только для приложений, основан либо на:

* Используемой памяти контейнера.

  + OneAgent версии 1.275+ (для контейнеров Kubernetes)
  + OneAgent версии 1.297+ (для бессерверных контейнеров)
* Лимитах памяти, заданных для контейнера.
  Если лимит памяти не задан, вместо этого используется память базовой виртуальной машины.

  + OneAgent версии <1.275 (для контейнеров Kubernetes)
  + OneAgent версии <1.297 (для бессерверных контейнеров)

Для существующих тенантов необходимо включить [автоматическое обнаружение контейнеров](/managed/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection#automatic-container-detection "Обнаруживайте облачные приложения и рабочие нагрузки и определяйте правила для объединения похожих рабочих нагрузок Kubernetes в группы процессов.").

Для некоторых сценариев мониторинга действуют собственные расчёты расхода ГиБ-часов, как описано в таблице ниже.

| Сценарий | Описание |
| --- | --- |
| Azure App Services (работающие по плану App Service (dedicated) для Windows) | Расход рассчитывается на основе числа и объёма памяти экземпляров плана. Не имеет значения, сколько приложений работает на этих экземплярах. Минимальный тарифицируемый объём памяти составляет 256 МиБ (вместо 4 ГиБ). |
| Azure App Service (работающий на Linux OS или в Linux-контейнерах), OneAgent версии 1.297+ | Если автоматическое обнаружение контейнеров включено: расход рассчитывается на основе используемой памяти контейнера. Если автоматическое обнаружение контейнеров не включено: расход рассчитывается на основе памяти экземпляра плана, умноженной на число работающих контейнеров. |
| Azure App Service (работающий на Linux OS или в Linux-контейнерах), OneAgent версии <1.297 | Расход рассчитывается на основе памяти экземпляра плана, умноженной на число работающих контейнеров, независимо от того, включено автоматическое обнаружение контейнеров или нет. |
| Oracle Solaris Zones | Solaris Zones учитываются как хосты. |
| Отслеживаемые контейнеры, не распознанные как контейнеры | Такие контейнеры учитываются как хосты. |

## Metrics

В этом разделе предполагается, что рекомендованные Dynatrace варианты развертывания уже выполнены, особенно в части обогащения телеметрии.
При использовании нестандартного развертывания начисление включённых метрик может по-прежнему работать так, как описано, но Dynatrace этого не гарантирует.

Подробнее см. [Поддерживаемые варианты развертывания](#deployment-options).

Full-Stack Monitoring включает все метрики Infrastructure Monitoring, метрики мониторинга производительности приложений и [другие встроенные метрики](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.").
Эти метрики включены в тариф и никогда не тарифицируются отдельно.

Full-Stack Monitoring также включает определённый объём точек данных пользовательских метрик.
Каждый учитываемый ГиБ памяти хоста или приложения добавляет 900 точек данных пользовательских метрик на каждый 15-минутный интервал.
Включённые точки данных метрик, не использованные в течение 15-минутного интервала, в котором они были предоставлены, не переносятся на последующие интервалы.
Включённые точки данных метрик среды применяются автоматически к метрикам, источником которых являются хосты и контейнеры, отслеживаемые OneAgent в режиме Full-Stack Monitoring.

Все ключи метрик, начинающиеся с `dt.service.*`, относятся к [мониторингу сервисов](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") и расходуют включённые точки данных метрик Full-Stack, если сами данные span получены от хостов и контейнеров, отслеживаемых OneAgent в режиме Full-Stack Monitoring.
Если данные span получены из любого другого источника, такие метрики тарифицируются как [Metrics powered by Grail](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
К таким ключам метрик относятся, например:

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

Точки данных метрик, превышающие включённый объём точек данных метрик, тарифицируются как [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

Включённые точки данных метрик среды применяются автоматически к метрикам, источником которых являются хосты и контейнеры, отслеживаемые OneAgent в режиме Full-Stack Monitoring.
Это относится к пользовательским метрикам, как описано в таблице ниже.

| Источник | Примеры (в том числе, но не только) |
| --- | --- |
| Хост с Full-Stack мониторингом, отправляющий метрики через [API метрик OneAgent](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | * метрики OpenTelemetry * Spring Micrometer * StatsD * JMX * Extensions, запущенный локально на хосте через OneAgent * локальный на хосте Telegraf |
| Приложение, отслеживаемое с помощью Container-based application-only Full-Stack Monitoring через код-модуль OneAgent | * метрики OpenTelemetry * Spring Micrometer * JMX |
| Узел Kubernetes с Full-Stack мониторингом, через Cloud Native Full-Stack или Classic Full-Stack | * метрики OpenTelemetry * Spring Micrometer * JMX * Prometheus (через ActiveGate). * Сюда не входят метрики, собираемые через коллектор OpenTelemetry. |
| [Мониторинг сервисов](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") | * `dt.service.request.count` * `dt.service.request.failure_count` * `dt.service.request.response_time` * `dt.service.request.service_mesh.count` * `dt.service.request.service_mesh.failure_count` * `dt.service.request.service_mesh.response_time` |

### Пример расчёта включённых точек данных метрик

Рассматривая пример, показанный на Рисунке 1, вот расчёты объёмов включённых точек данных метрик для каждого из четырёх 15-минутных интервалов, при условии объёма 900 включённых точек данных метрик на каждый 15-минутный интервал.

* Первый 15-минутный интервал: `900 (включённых точек данных метрик) × 13.5 (ГиБ памяти) = 12 150 включённых точек данных метрик`
* Второй 15-минутный интервал: `900 (включённых точек данных метрик) × 9.5 (ГиБ памяти) = 8 550 включённых точек данных метрик`
* Третий 15-минутный интервал: `900 (включённых точек данных метрик) × 8.75 (ГиБ памяти) = 7 875 включённых точек данных метрик`
* Четвёртый 15-минутный интервал: `900 (включённых точек данных метрик) × 0.25 (ГиБ памяти) = 225 включённых точек данных метрик`

### Как расходуются точки данных метрик в режиме Full-Stack Monitoring

Расход точек данных метрик принимает разные формы.
Одинаковое количество точек данных может быть израсходовано:

* небольшим числом высокоточных метрик или множеством низкоточных метрик;
* равномерно в течение нескольких 15-минутных интервалов или целиком за одну минуту;
* всеми отслеживаемыми хостами, частью хостов с Full-Stack мониторингом или одним хостом.

### Профилирование CPU, памяти и потоков

Full-Stack Monitoring включает профилирование [CPU](/managed/observe/application-observability/profiling-and-optimization/cpu-profiling "Learn how you can use Dynatrace to perform enhanced code analysis."), [памяти](/managed/observe/application-observability/profiling-and-optimization/memory-profiling "Analyze memory allocation with Dynatrace.") и потоков для таких технологий, как Java, .NET, Go, Node.js и PHP.
OneAgent использует интеллектуальный запатентованный механизм для управления объёмом данных профилирования.
Dynatrace [хранит общий объём поступивших данных профилирования](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.") из вашей среды в течение 10 дней.

## Поддерживаемые варианты развертывания

Чтобы ваши пользовательские метрики учитывались во включённых объёмах трасс и метрик, нужно включить обогащение телеметрии согласно рекомендованным Dynatrace вариантам развертывания.

Автоматическое обогащение телеметрии включено для:

* Пользовательских метрик, источником которых является любой из следующих вариантов:

  + хост или контейнер с Full-Stack мониторингом, при использовании OneAgent или выполнении шагов, описанных в разделе [Обогащение поступающих данных специфичными для Dynatrace полями](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.");
  + контейнер Kubernetes с Full-Stack мониторингом, при использовании Dynatrace Operator и [включённом обогащении метаданными](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Configure metadata enrichment in Dynatrace Operator to attach Kubernetes metadata to telemetry signals using OneAgent, OTLP exporter, or standalone enrichment.");
  + узел Kubernetes с cloud-native Full-Stack мониторингом, при использовании Dynatrace Operator и [включённом обогащении метаданными](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Configure metadata enrichment in Dynatrace Operator to attach Kubernetes metadata to telemetry signals using OneAgent, OTLP exporter, or standalone enrichment.").
    Сюда входят любые контейнеры, работающие на отслеживаемом узле Kubernetes.
* Пользовательских метрик, отправляемых с любого хоста с Full-Stack мониторингом через локальный API метрик OneAgent. Подробнее см. [API метрик OneAgent](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

При использовании нестандартного развертывания начисление метрик может по-прежнему работать так, как описано, но Dynatrace этого не гарантирует.

## Детали потребления: Full-Stack

Dynatrace предоставляет встроенные метрики использования, которые помогают понять и проанализировать потребление организацией Full-Stack Monitoring.
Чтобы использовать эти метрики, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите `DPS` в поле **Search**.
Эти метрики также доступны через Environment API и в Account Management (**Usage summary** > **Full-Stack Monitoring** > **Actions** > **View details**).

Ниже перечислены метрики, которые можно использовать для отслеживания потребления Dynatrace Full-Stack Monitoring.

(DPS) Full-Stack Monitoring billing usage
:   Ключ: `builtin:billing.full_stack_monitoring.usage`

    Измерение: count

    Разрешение: 15 мин

    Описание: суммарный объём памяти в ГиБ всех хостов, отслеживаемых в режиме Full-Stack Monitoring, подсчитанный за 15-минутные интервалы.

(DPS) Full-Stack Monitoring billing usage per host
:   Ключ: `builtin:billing.full_stack_monitoring.usage_per_host`

    Измерение: Host (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: объём памяти в ГиБ на хост, отслеживаемый в режиме Full-Stack Monitoring, подсчитанный за 15-минутные интервалы.

(DPS) Full-stack usage by container type
:   Ключ: `builtin:billing.full_stack_monitoring.usage_per_container`

    Измерение: application\_only\_type; k8s.cluster.uid; k8s.namespace.name

    Разрешение: 15 мин

    Описание: объём памяти в ГиБ на контейнер, отслеживаемый в режиме Full-Stack application-only Monitoring, подсчитанный за 15-минутные интервалы.

(DPS) Total metric data points reported by Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.ingested`

    Измерение: Count

    Разрешение: 15 мин

    Описание: количество переданных точек данных метрик, агрегированных по всем хостам, отслеживаемым в Full-Stack.

(DPS) Metric data points reported and split by Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.ingested_by_host`

    Измерение: Host (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: количество переданных точек данных метрик в разбивке по хостам, отслеживаемым в Full-Stack.

(DPS) Available included metric data points for Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.included`

    Измерение: Count

    Разрешение: 15 мин

    Описание: общее число включённых точек данных метрик, которые можно вычесть из потреблённых точек данных метрик, переданных хостами, отслеживаемыми в Full-Stack.

(DPS) Used included metric data points for Full-Stack monitored hosts
:   Ключ: `builtin:billing.full_stack_monitoring.metric_data_points.included_used`

    Измерение: Count

    Разрешение: 15 мин

    Описание: количество потреблённых включённых точек данных метрик для хостов, отслеживаемых в Full-Stack.

### Мониторинг потребления памяти в ГиБ-часах для хостов, отслеживаемых в Full-Stack

С помощью метрики "(DPS) Full-Stack Monitoring billing usage" можно отслеживать суммарное потребление памяти в ГиБ-часах, агрегированное по всем хостам, отслеживаемым в Full-Stack, с разными интервалами (15 мин, час, день или неделя) для любого выбранного периода времени.
В примере ниже показан объём памяти в ГиБ, отслеживаемый с интервалом в 1 час.
С 11:00 до 14:00 каждый час отслеживалось 523 ГиБ памяти.
В результате потреблено 523 ГиБ-часа памяти.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image001-1183-79f381ccb1.png)

Full-Stack Monitoring (DPS)

С помощью метрики "(DPS) Full-Stack Monitoring billing usage per host" можно детализировать суммарное потребление памяти в ГиБ-часах.
В примере ниже показан список всех хостов, которые внесли вклад в потребление 523 ГиБ-часов памяти с 13:00 до 14:00.
Также отображается соответствующее число ГиБ-часов памяти по каждому хосту.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image004-905-f0e44ad601.png)

Full-Stack Monitoring (DPS)

### Мониторинг потребления памяти в ГиБ-часах для контейнеров, отслеживаемых в Full-Stack

Владельцы приложений могут использовать контейнерный Full-Stack Monitoring для отслеживания приложений, работающих в кластерах Kubernetes.

Чтобы получить сведения о потреблении для отслеживаемых кластеров или пространств имён Kubernetes, можно запросить потребление памяти в ГиБ-часах с помощью метрики "(DPS) Full-Stack Monitoring billing usage per container", как показано в следующем запросе:

`builtin:billing.full_stack_monitoring.usage_per_container:filter(eq("application_only_type","kubernetes")):splitBy()`

В примере ниже за последние 30 дней кластером Kubernetes было потреблено 1,58 ТиБ памяти.

![Kubernetes Platform Monitoring](https://dt-cdn.net/images/billing-full-stack-monitoring-usage-per-container-1025-3019577b21.png)

Kubernetes Platform Monitoring

Разумеется, анализ можно фильтровать для более глубокого понимания (например, добавить разбивку по пространствам имён Kubernetes).

![Kubernetes Platform Monitoring](https://dt-cdn.net/images/billing-full-stack-monitoring-usage-per-container-by-namespace-1023-c5e1c10583.png)

Kubernetes Platform Monitoring

### Мониторинг потребления метрик для хостов, отслеживаемых в Full-Stack

Чтобы отслеживать бюджет метрик для всего пула точек данных метрик в среде, можно сравнивать доступные включённые точки данных метрик с общим числом переданных точек данных метрик, используя эти две метрики: "(DPS) Available included metric data points for Full-Stack monitored hosts" и "(DPS) Total metric data points reported by Full-Stack monitored hosts".
В примере ниже показаны данные за целые сутки.
Ни в один момент число включённых метрик для пула метрик этой среды (фиолетовая линия) не было превышено.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image005-1212-35369921df.png)

Full-Stack Monitoring (DPS)

В случаях, когда число включённых метрик для пула метрик среды превышено, следующий анализ поможет определить хосты, которые вносят вклад в перерасход.
Для этого анализа используйте метрику "(DPS) Metric data points reported and split by Full-Stack monitored hosts".

В примере ниже показано, что с 10:45 до 11:00 каждый из первых 3 хостов в списке передал значительно больше 2000 точек данных метрик.
В этот же период каждый из этих 3 хостов показывает потребление памяти 2 ГиБ-часа.
Dynatrace предоставляет 900 включённых точек данных пользовательских метрик на каждый ГиБ памяти хоста, рассчитанных с интервалом в 15 минут.
Это значит, что первые 3 хоста вносят в пул доступных точек данных среды 1800 (2\*900) точек данных метрик.
Однако эти хосты потребили за тот же период времени больше точек данных, чем внесли.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image008-905-929928d644.png)

Full-Stack Monitoring (DPS)

При использовании метрики "(DPS) Total metric data points billed for Full-Stack monitored hosts" из Custom Metrics Classic видно, что с 10:45 до 11:00 перерасхода пула метрик Full-Stack Monitoring этой среды не произошло, поскольку ни одна точка данных метрик не была тарифицирована.

![Full-Stack Monitoring (DPS)](https://dt-cdn.net/images/image009-1210-914bc4742c.png)

Full-Stack Monitoring (DPS)

## Похожие темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Ознакомьтесь с важными концепциями, связанными с OneAgent, и узнайте, как устанавливать и эксплуатировать OneAgent на разных платформах.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Узнайте о разных вариантах Application & Infrastructure Observability, доступных с лицензией Dynatrace Platform Subscription (DPS).")
* [Тарификация Dynatrace﻿](https://www.dynatrace.com/pricing/)