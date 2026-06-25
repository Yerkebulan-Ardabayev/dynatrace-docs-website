# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one

TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_JOURNALD = "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace."
RU_JOURNALD = "Настройте OpenTelemetry Collector для приёма логов журнала systemd с хостов Linux в Dynatrace."

TRANS = {
    # --- frontmatter / title ---
    "title: Monitor hosts that send OpenTelemetry data to Dynatrace": "title: Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace",
    "# Monitor hosts that send OpenTelemetry data to Dynatrace": "# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace",
    # --- metadata ---
    "* Updated on Apr 01, 2026": "* Обновлено 01 апреля 2026 г.",
    # --- intro ---
    "OpenTelemetry Host Monitoring is a Dynatrace feature that transforms raw telemetry data from OTel Collectors into actionable insights.": "OpenTelemetry Host Monitoring, это функция Dynatrace, которая преобразует необработанные данные телеметрии от OTel Collector в практические сведения.",
    "Rather than simply ingesting metrics, logs, and traces, Dynatrace automatically builds meaningful context around your infrastructure.": "Вместо простого приёма метрик, логов и трассировок Dynatrace автоматически выстраивает значимый контекст вокруг вашей инфраструктуры.",
    "It creates host and process entities, establishes topology relationships, and presents data through purpose-built analysis screens.": "Она создаёт сущности хостов и процессов, устанавливает топологические связи и представляет данные через специально предназначенные экраны анализа.",
    "With the extension, you can:": "С помощью расширения можно:",
    "* Use auto-generated entities (based on extracted metadata) to correlate metrics, logs, and spans and provide unified context across your monitoring environment.": "* Использовать автоматически создаваемые сущности (на основе извлечённых метаданных) для корреляции метрик, логов и спанов и обеспечения единого контекста во всей вашей среде мониторинга.",
    "This use case and its reference configuration are designed primarily for VMs and bare-metal hosts with a Linux OS.": "Этот сценарий использования и его эталонная конфигурация предназначены прежде всего для виртуальных машин и физических хостов с ОС Linux.",
    "* If you want to run host monitoring on Kubernetes nodes, see [Host monitoring on Kubernetes nodes](#kubernetes-considerations) for deployment requirements and limitations.": "* Если требуется запустить мониторинг хостов на узлах Kubernetes, см. требования к развёртыванию и ограничения в разделе [Мониторинг хостов на узлах Kubernetes](#kubernetes-considerations).",
    "* If you want to run host monitoring on Windows OS or macOS, remove all references to `journald` from the pipeline"
    + "â"
    + "`journald` is only available for Linux OS.": "* Если требуется запустить мониторинг хостов в ОС Windows или macOS, удалите из конвейера все ссылки на `journald`: `journald` доступен только для ОС Linux.",
    # --- Prerequisites ---
    "This use case assumes that you have:": "Этот сценарий использования предполагает, что у вас есть:",
    "* One of the following Collector distributions with the [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver) and [`journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver) receivers, and the [`resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/resourcedetectionprocessor), [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor), and [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) processors.": "* Один из следующих дистрибутивов Collector с receiver [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver) и [`journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver), а также processor [`resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/resourcedetectionprocessor), [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) и [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor).",
    '+ [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % TT_LEARN: '+ [специально собранный OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % RU_LEARN,
    "* Activated the OpenTelemetry Host Monitoring extension.": "* Активированное расширение OpenTelemetry Host Monitoring.",
    'For more information about the extension, see [OpenTelemetry Host Monitoring extension](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Generate topology and screens for your OpenTelemetry host data for quicker display and easier analysis of the data.").': 'Дополнительные сведения о расширении см. в разделе [Расширение OpenTelemetry Host Monitoring](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Создавайте топологию и экраны для данных ваших хостов OpenTelemetry для более быстрого отображения и более простого анализа данных.").',
    # --- Reference configuration ---
    "## Reference configuration": "## Эталонная конфигурация",
    "A reference configuration is available in the Dynatrace OTel Collector's GitHub repo, see [`host-metrics.yaml`](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).": "Эталонная конфигурация доступна в репозитории GitHub для Dynatrace OTel Collector, см. [`host-metrics.yaml`](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).",
    "You can use this configuration as-is, or modify it to meet your specific needs.": "Эту конфигурацию можно использовать как есть или изменить её под ваши конкретные потребности.",
    # --- Components ---
    "For our configuration, we configured the following components that are specific to this extension.": "Для нашей конфигурации мы настроили следующие компоненты, специфичные для этого расширения.",
    # Receivers
    "Under `receivers`, we specify the following receivers:": "В разделе `receivers` мы указываем следующие receiver:",
    "* [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver)": "* [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver)",
    "* [`journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver)": "* [`journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver)",
    "The [`hostmetrics` receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver) collects host-level metrics.": "[receiver `hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver) собирает метрики уровня хоста.",
    "It is configured with three collection intervals: 10 seconds, 5 minutes, and 1 hour.": "Он настроен с тремя интервалами сбора: 10 секунд, 5 минут и 1 час.",
    "* Use short intervals for the most important metrics to ensure that Dynatrace provides fast alerts for important changes.": "* Используйте короткие интервалы для самых важных метрик, чтобы Dynatrace обеспечивал быстрые оповещения о важных изменениях.",
    "* Send non-critical metrics less frequently to help control consumption and therefore costs.": "* Отправляйте некритичные метрики реже, чтобы помочь контролировать потребление и, следовательно, затраты.",
    "The [`journald` receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver) collects systemd journal logs from the host and ingests them into the logs pipeline alongside your metrics.": "[receiver `journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver) собирает логи журнала systemd с хоста и принимает их в конвейер логов вместе с вашими метриками.",
    "It is configured to read from `/var/log/journal` (the default persistent journal path on Linux hosts) and applies `move` operators to rename journal fields to OpenTelemetry semantic conventions.": "Он настроен на чтение из `/var/log/journal` (путь к постоянному журналу по умолчанию на хостах Linux) и применяет операторы `move` для переименования полей журнала в соответствии с семантическими соглашениями OpenTelemetry.",
    "* `body._PID` is renamed to `body.pid`": "* `body._PID` переименовывается в `body.pid`",
    '* `body._EXE` is renamed to `attributes["process.executable.name"]`': '* `body._EXE` переименовывается в `attributes["process.executable.name"]`',
    "* `body.MESSAGE` is renamed to `body.message`": "* `body.MESSAGE` переименовывается в `body.message`",
    "This ensures that host logs are linked to the same process entities as the `hostmetrics` data, enabling correlation between metrics and logs in Dynatrace.": "Это гарантирует, что логи хоста связываются с теми же сущностями процессов, что и данные `hostmetrics`, обеспечивая корреляцию между метриками и логами в Dynatrace.",
    "The `journald` receiver is supported on Linux OS only, and requires the `journalctl` binary on the host.": "receiver `journald` поддерживается только в ОС Linux и требует наличия на хосте двоичного файла `journalctl`.",
    "The Collector process must have permission to read the systemd journal.": "Процесс Collector должен иметь разрешение на чтение журнала systemd.",
    "On Linux hosts, add the user running the Collector to the `systemd-journal` group.": "На хостах Linux добавьте пользователя, запускающего Collector, в группу `systemd-journal`.",
    'For full details, see [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "%s").'
    % TT_JOURNALD: 'Все подробности см. в разделе [Использование journald для приёма логов журнала systemd с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "%s").'
    % RU_JOURNALD,
    # Processors
    "Under `processors`, we specify the following processors:": "В разделе `processors` мы указываем следующие processor:",
    "* [`resourcedetection` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/resourcedetectionprocessor), which can be used to detect resource information from the host, in a format that conforms to the OpenTelemetry resource semantic conventions, and append or override the resource value in telemetry data with this information.": "* [processor `resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/resourcedetectionprocessor), который можно использовать для обнаружения информации о ресурсе на хосте в формате, соответствующем семантическим соглашениям ресурса OpenTelemetry, и добавления этой информации к значению ресурса в данных телеметрии либо его переопределения.",
    "* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) is used twice: once to clean up unnecessary metrics dimensions, and secondly to (optionally) filter out unneeded process metrics.": "* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) используется дважды: первый раз для очистки ненужных измерений метрик и второй раз для (необязательной) фильтрации ненужных метрик процессов.",
    "* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor).": "* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor).",
    # Exporters
    "Under `exporters`, we specify the [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.": "В разделе `exporters` мы указываем [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.",
    '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).'
    % TT_OTLP: '* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).'
    % RU_OTLP,
    '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s").'
    % TT_OTLP: '* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s").'
    % RU_OTLP,
    # --- How-to ---
    "## How-to": "## Практическое руководство",
    "### Topology": "### Топология",
    "This extension automatically generates topology for infrastructure monitored via the Collector.": "Это расширение автоматически создаёт топологию для инфраструктуры, отслеживаемой через Collector.",
    "Specifically, it creates the following entity types based on metadata extracted from metrics, logs, and traces:": "В частности, оно создаёт следующие типы сущностей на основе метаданных, извлечённых из метрик, логов и трассировок:",
    "| Entity type | Entity ID |": "| Тип сущности | ID сущности |",
    "| OpenTelemetry Host | dt.entity.otel:host |": "| OpenTelemetry Host | dt.entity.otel:host |",
    "| OpenTelemetry Process | dt.entity.otel:process |": "| OpenTelemetry Process | dt.entity.otel:process |",
    "These entities enable Dynatrace to correlate your metrics, logs, and spans and provide unified context across your monitored environment.": "Эти сущности позволяют Dynatrace коррелировать ваши метрики, логи и спаны и обеспечивать единый контекст во всей отслеживаемой среде.",
    "### Enrich application telemetry": "### Обогащение телеметрии приложений",
    "If you send your application telemetry to your local host Collector, it will automatically enrich the data with the required host attributes so that the signals are correctly attached to the OpenTelemetry host entity.": "Если вы отправляете телеметрию приложения в локальный Collector хоста, он автоматически обогатит данные необходимыми атрибутами хоста, чтобы сигналы были корректно привязаны к сущности хоста OpenTelemetry.",
    "To enrich application telemetry with the corresponding process entity, all signals (metrics, logs, and spans) need to have the `process.executable.name` resource attribute.": "Чтобы обогатить телеметрию приложения соответствующей сущностью процесса, все сигналы (метрики, логи и спаны) должны иметь атрибут ресурса `process.executable.name`.",
    "For logs and spans to have this attribute, you need to initialize your OTel SDK with the [process resource detector](https://opentelemetry.io/docs/languages/go/resources/).": "Чтобы логи и спаны имели этот атрибут, необходимо инициализировать ваш OTel SDK с помощью [детектора ресурсов процесса](https://opentelemetry.io/docs/languages/go/resources/).",
    "If this is not implemented for your technology's OTel SDK, you can always set the `process.executable.name` attribute through the `OTEL_RESOURCE_ATTRIBUTES` [environment variable](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration).": "Если это не реализовано для OTel SDK вашей технологии, всегда можно задать атрибут `process.executable.name` через переменную окружения `OTEL_RESOURCE_ATTRIBUTES` ([переменную окружения](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration)).",
    "### Limit sending of process metrics": "### Ограничение отправки метрик процессов",
    "By default, all process metrics are sent to Dynatrace.": "По умолчанию в Dynatrace отправляются все метрики процессов.",
    "You can also exclude certain process metrics to control the amount of OTel process entities and improve cardinality.": "Также можно исключить определённые метрики процессов, чтобы контролировать количество сущностей процессов OTel и улучшить кардинальность.",
    "For example, you might want to filter out insignificant processes that use less than 1 MiB of memory.": "Например, может потребоваться отфильтровать незначительные процессы, использующие менее 1 МиБ памяти.",
    "To do this, you can filter via the process memory usage or an allow list.": "Для этого можно выполнить фильтрацию по использованию памяти процессом или по списку разрешений.",
    "* To filter via process memory usage, use the following `transform` and `filter` processor configurations in your host monitoring configuration YAML.": "* Для фильтрации по использованию памяти процессом используйте в вашем YAML-файле конфигурации мониторинга хостов следующие конфигурации processor `transform` и `filter`.",
    "Adjust the `datapoint.value_int` value (in bytes) according to your use case.": "Скорректируйте значение `datapoint.value_int` (в байтах) в соответствии с вашим сценарием использования.",
    "If the memory usage of the process fluctuates around the configured limit, metrics could be ingested and dropped intermittently.": "Если использование памяти процессом колеблется вокруг заданного предела, метрики могут приниматься и отбрасываться с перерывами.",
    "These data gaps would affect cumulative data like counts or sums.": "Такие пропуски в данных повлияли бы на кумулятивные данные, например на счётчики или суммы.",
    "* To create an allowlist, use the following `transform` and `filter` processors in your host monitoring configuration YAML.": "* Для создания списка разрешений используйте в вашем YAML-файле конфигурации мониторинга хостов следующие processor `transform` и `filter`.",
    "Adjust the `ContainsValue()` and `resource.attributes[]` variable names according to your use case.": "Скорректируйте имена переменных `ContainsValue()` и `resource.attributes[]` в соответствии с вашим сценарием использования.",
    # --- Host monitoring on Kubernetes nodes ---
    "## Host monitoring on Kubernetes nodes": "## Мониторинг хостов на узлах Kubernetes",
    "The reference configuration and this use case are optimized for VMs and bare-metal hosts.": "Эталонная конфигурация и этот сценарий использования оптимизированы для виртуальных машин и физических хостов.",
    "You can run OTel host monitoring on Kubernetes nodes, but there are additional deployment requirements and important caveats to consider.": "Мониторинг хостов OTel можно запустить на узлах Kubernetes, но при этом следует учитывать дополнительные требования к развёртыванию и важные оговорки.",
    "### Deployment": "### Развёртывание",
    "To collect host-level metrics from every node in your cluster, deploy the Collector as a **DaemonSet**.": "Для сбора метрик уровня хоста с каждого узла вашего кластера разверните Collector как **DaemonSet**.",
    "This ensures one Collector pod runs on each node and reports that node's metrics.": "Это гарантирует, что на каждом узле работает один под Collector и сообщает метрики этого узла.",
    "The `hostmetrics` receiver works without any additional configuration on Kubernetes.": "receiver `hostmetrics` работает в Kubernetes без какой-либо дополнительной конфигурации.",
    "The same receiver configuration you use on VMs applies to containerized deployments.": "Та же конфигурация receiver, которую вы используете на виртуальных машинах, применяется и к контейнеризированным развёртываниям.",
    "### journald on Kubernetes": "### journald в Kubernetes",
    "To collect journald logs on Kubernetes nodes, the Collector must run as root (`runAsUser: 0`) because container isolation prevents group-based journal access.": "Для сбора логов journald на узлах Kubernetes Collector должен работать от имени root (`runAsUser: 0`), поскольку изоляция контейнеров препятствует доступу к журналу на основе групп.",
    "You also need to mount the journal directory from the host and adjust the `directory` setting to the mounted path.": "Вам также нужно смонтировать каталог журнала с хоста и задать в параметре `directory` смонтированный путь.",
    "On Kubernetes, the in-memory journal path is typically `/run/log/journal` rather than the persistent `/var/log/journal` used on VMs.": "В Kubernetes путь к журналу в памяти обычно `/run/log/journal`, а не постоянный `/var/log/journal`, используемый на виртуальных машинах.",
    'See [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "%s") for the full Kubernetes deployment configuration, including the required security context and host volume mounts.'
    % TT_JOURNALD: 'Полную конфигурацию развёртывания в Kubernetes, включая необходимый контекст безопасности и монтирование томов хоста, см. в разделе [Использование journald для приёма логов журнала systemd с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "%s").'
    % RU_JOURNALD,
    "### Metric overlap with Kubernetes monitoring": "### Перекрытие метрик с мониторингом Kubernetes",
    'If you run both OTel host monitoring and [Kubernetes cluster monitoring](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") on the same nodes, be aware that some metrics overlap: the same measurements may be ingested as two separate metric keys.': 'Если вы запускаете на одних и тех же узлах одновременно мониторинг хостов OTel и [мониторинг кластеров Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Настройте OpenTelemetry Collector для мониторинга ваших кластеров Kubernetes."), учтите, что некоторые метрики перекрываются: одни и те же измерения могут приниматься как два отдельных ключа метрик.',
    "This is because they have different metric names that follow different semantic conventions, so Dynatrace ingests them as separate metric keys.": "Это происходит потому, что они имеют разные имена метрик, следующие разным семантическим соглашениям, поэтому Dynatrace принимает их как отдельные ключи метрик.",
    "The following table shows common overlapping metrics:": "В следующей таблице показаны типичные перекрывающиеся метрики:",
    "| `hostmetrics` receiver | `kubeletstats` receiver | What they measure |": "| receiver `hostmetrics` | receiver `kubeletstats` | Что они измеряют |",
    "| `system.cpu.*` | `k8s.node.cpu.*` | Node CPU usage |": "| `system.cpu.*` | `k8s.node.cpu.*` | Использование CPU узла |",
    "| `system.memory.*` | `k8s.node.memory.*` | Node memory usage |": "| `system.memory.*` | `k8s.node.memory.*` | Использование памяти узла |",
    "| `system.filesystem.*` | `k8s.node.filesystem.*` | Node filesystem usage |": "| `system.filesystem.*` | `k8s.node.filesystem.*` | Использование файловой системы узла |",
    "| `system.network.*` | `k8s.node.network.*` | Node network I/O |": "| `system.network.*` | `k8s.node.network.*` | Сетевой ввод-вывод узла |",
    "This overlapp occurs because the Kubernetes monitoring use case uses the [`kubeletstats` receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver), which reports node-level resource metrics that represent the same underlying data as the `hostmetrics` receiver.": "Это перекрытие возникает потому, что в сценарии использования мониторинга Kubernetes применяется [receiver `kubeletstats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver), который сообщает метрики ресурсов уровня узла, представляющие те же базовые данные, что и receiver `hostmetrics`.",
    "To avoid unnecessary duplication on Kubernetes, use only Kubernetes monitoring or only OTel host monitoring, if possible:": "Чтобы избежать ненужного дублирования в Kubernetes, по возможности используйте только мониторинг Kubernetes или только мониторинг хостов OTel:",
    "* Use Kubernetes monitoring only if you don't require process-level detail and host entity topology.": "* Используйте только мониторинг Kubernetes, если вам не требуется детализация на уровне процессов и топология сущностей хостов.",
    '[Kubernetes cluster monitoring](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") provides node-level metrics through the `kubeletstats` receiver. Adding `hostmetrics` on top duplicates the node-level resource metrics.': '[Мониторинг кластеров Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Настройте OpenTelemetry Collector для мониторинга ваших кластеров Kubernetes.") предоставляет метрики уровня узла через receiver `kubeletstats`. Добавление `hostmetrics` поверх этого дублирует метрики ресурсов уровня узла.',
    "* Use host monitoring only if you don't require Kubernetes-specific object metrics such as pods and deployments.": "* Используйте только мониторинг хостов, если вам не требуются специфичные для Kubernetes метрики объектов, такие как поды и развёртывания.",
    "OTel host monitoring provides host and process entities with topology in Dynatrace.": "Мониторинг хостов OTel предоставляет сущности хостов и процессов с топологией в Dynatrace.",
    "* If you require both use cases, use the `filter` processor to drop overlapping node-level metrics from one of the two pipelines.": "* Если вам нужны оба сценария использования, используйте processor `filter`, чтобы отбрасывать перекрывающиеся метрики уровня узла из одного из двух конвейеров.",
    "For example, filter out `system.cpu.*`, `system.memory.*`, `system.filesystem.*`, and `system.network.*` from the host monitoring pipeline if the Kubernetes monitoring pipeline already covers them.": "Например, отфильтруйте `system.cpu.*`, `system.memory.*`, `system.filesystem.*` и `system.network.*` из конвейера мониторинга хостов, если конвейер мониторинга Kubernetes уже их охватывает.",
    # --- Limitations ---
    "## Limitations": "## Ограничения",
    "* The `system.processes.created` metric is only available on Linux.": "* Метрика `system.processes.created` доступна только в Linux.",
    "* The `process.disk.io` metric requires running the Collector with privileged access.": "* Метрика `process.disk.io` требует запуска Collector с привилегированным доступом.",
    "If you don't do this, the metric will be prevented from being captured.": "Если этого не сделать, захват метрики будет заблокирован.",
    "* The `journald` receiver is only supported on Linux. Attempting to use the `journald` receiver on a different operating system will cause the Collector to return an error and exit on startup.": "* receiver `journald` поддерживается только в Linux. Попытка использовать receiver `journald` в другой операционной системе приведёт к тому, что Collector вернёт ошибку и завершит работу при запуске.",
    **S,
}

PASS = {
    "### Receivers",
    "### Processors",
    "### Exporters",
    "#### hostmetrics",
    "#### journald",
    "| --- | --- |",
    "| --- | --- | --- |",
}

if __name__ == "__main__":
    build_one(SUB, "host-monitoring.md", TRANS, PASS)
    qa_one(SUB, "host-monitoring.md")
