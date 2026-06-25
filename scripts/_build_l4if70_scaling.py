# -*- coding: utf-8 -*-
from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/collector"
FNAME = "scaling.md"

TRANS = {
    # --- frontmatter ---
    "title: How to scale the OTel Collector": "title: Как масштабировать OTel Collector",
    # --- h1 (duplicated in source) ---
    "# How to scale the OTel Collector": "# Как масштабировать OTel Collector",
    # --- metadata bullets ---
    "* How-to guide": "* Практическое руководство",
    "* 10-min read": "* Чтение: 10 мин",
    "* Published Sep 30, 2025": "* Опубликовано 30 сентября 2025 г.",
    # --- intro paragraph (8 lines) ---
    "When the OTel Collector's CPU or memory usage exceeds a threshold that would put it": "Когда загрузка CPU или памяти OTel Collector превышает порог, при котором Collector",
    "at risk of being overloaded if there were a burst of traffic, it is recommended": "рискует оказаться перегруженным при всплеске трафика, рекомендуется либо",
    "to find ways to either increase the resources allotted to the Collector, or to": "увеличить ресурсы, выделенные Collector, либо",
    "scale processing to multiple Collector instances. We will primarily focus on": "распределить обработку между несколькими экземплярами Collector. Здесь рассматриваются",
    "solutions available in Kubernetes here. Note that the guidance and examples in": "преимущественно решения, доступные в Kubernetes. Обратите внимание: рекомендации и примеры",
    "this documentation are generalized and may not give optimal performance for your": "в данной документации носят общий характер и могут не обеспечить оптимальную производительность",
    "specific case; you will need to analyze your systems to determine the best way": "в вашем конкретном случае. Для определения наилучшего способа",
    "to scale them.": "масштабирования следует проанализировать собственные системы.",
    # --- "For more general information" (3 lines) ---
    "For more general information in the OpenTelemetry documentation, please see the": "Дополнительные общие сведения в документации OpenTelemetry см. на странице",
    "[Scaling the OTel Collectorï»¿](https://opentelemetry.io/docs/collector/scaling/) page": "[Scaling the OTel Collector](https://opentelemetry.io/docs/collector/scaling/)",
    "on the OpenTelemetry website.": "на сайте OpenTelemetry.",
    # --- section h2 ---
    "## Determining when to scale": "## Когда следует масштабировать",
    # --- "You will want..." paragraph (5 lines) ---
    "You will want to consider scaling when you begin to approach the limits of the": "Масштабирование следует рассматривать, когда вы начинаете приближаться к пределам",
    "resources that have been allotted to your Collector. Self-monitoring metrics": "ресурсов, выделенных вашему Collector. Метрики самодиагностики,",
    "available through the Collector and metrics available from the host environment": "доступные через Collector, а также метрики хостовой среды",
    "(e.g. Kubernetes) will be helpful to track this.": "(например, Kubernetes) помогут отслеживать это.",
    "The following are a few metrics worth paying attention to:": "Ниже перечислены несколько метрик, заслуживающих внимания:",
    # --- bullet: otelcol_processor_refused_spans (4 lines) ---
    # keys are STRIPPED (no leading spaces) — engine restores indent from ln
    "* `otelcol_processor_refused_spans`: If you have the [Memory Limiter": "* `otelcol_processor_refused_spans`: если включён [Memory Limiter",
    "Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/memorylimiterprocessor)": "Processor](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/memorylimiterprocessor)",
    "enabled, this metric (or the equivalent for other signals) will indicate that": "(или аналогичная метрика для других сигналов), это означает,",
    "the Collector needs more memory to continue processing its current load.": "что Collector требуется дополнительная память для обработки текущей нагрузки.",
    # --- bullet: otelcol_exporter_queue (6 lines) ---
    "* `otelcol_exporter_queue_capacity` and `otelcol_exporter_queue_size`: Once the": "* `otelcol_exporter_queue_capacity` и `otelcol_exporter_queue_size`: когда размер",
    "exporter queue size starts to get close to or exceed the queue capacity, that": "очереди exporter приближается к ёмкости очереди или превышает её, это",
    "indicates the Collector is having trouble sending data to the backend. This is": "означает, что Collector испытывает трудности с отправкой данных в бэкенд. Причиной",
    "either because workers are not becoming available to send the data, or the": "может быть отсутствие свободных воркеров для отправки данных или",
    "backend itself is overloaded. You may need to increase the processing power": "перегрузка самого бэкенда. Может потребоваться увеличить вычислительную мощность,",
    "available to the Collector to continue processing this volume of data.": "доступную Collector, для продолжения обработки такого объёма данных.",
    # --- bullet: k8s.resource_quota.used (5 lines) ---
    "* `k8s.resource_quota.used`: If you are monitoring your Kubernetes cluster with": "* `k8s.resource_quota.used`: при мониторинге кластера Kubernetes с помощью",
    "the [Kubernetes Cluster": "[Kubernetes Cluster",
    "Receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver),": "Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver)",
    "this can be used to determine the amount of": "эта метрика позволяет определить объём",
    "CPU/memory quota your Collector has used.": "квоты CPU/памяти, использованной вашим Collector.",
    # --- bullet: container.cpu.usage / container.memory.usage (5 lines) ---
    "* `container.cpu.usage` and `container.memory.usage`: If you are monitoring your": "* `container.cpu.usage` и `container.memory.usage`: при мониторинге",
    "cluster with the [Kubelet Stats": "кластера с помощью [Kubelet Stats",
    "Receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver),": "Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver),",
    "these can tell you if a given Collector container is nearing or hitting its": "они позволяют узнать, приближается ли контейнер Collector к своим",
    "quota limits.": "лимитам квоты или уже достиг их.",
    # --- h2: Scaling the Collector ---
    "## Scaling the Collector": "## Масштабирование Collector",
    # --- Kubernetes object types paragraph (5 lines) ---
    "Kubernetes comes with multiple object types capable of scaling the Collector": "Kubernetes предоставляет несколько типов объектов, позволяющих масштабировать Collector",
    "based on the needs of specific scenarios. For simple scaling, Deployments or": "в соответствии с требованиями конкретных сценариев. Для простого масштабирования можно",
    "ReplicaSets can be used to create a pool of Collectors that can be scheduled by": "использовать Deployments или ReplicaSets для создания пула Collector, которыми Kubernetes",
    "Kubernetes without too much forethought. For more general information on": "может управлять без особой предварительной настройки. Дополнительные общие сведения об",
    'Collector deployment architectures, see our guide on [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.").': 'архитектурах развёртывания Collector см. в руководстве [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.").',
    # --- horizontal vs vertical paragraph (8 lines) ---
    "Most of the advice in this document applies to horizontally scaling the": "Большинство рекомендаций в данном документе касаются горизонтального масштабирования",
    "Collector by creating more Collector instances or spreading instances across": "Collector путём создания дополнительных экземпляров или распределения экземпляров",
    "machines. However, if your current deployment uses a single Collector instance": "по разным узлам. Однако если текущее развёртывание использует один экземпляр Collector",
    "to do all your processing, you should first determine if vertically scaling the": "для всей обработки, сначала следует определить, достаточно ли вертикального масштабирования",
    "Collector is sufficient for your anticipated load. Vertically scaling the": "для ожидаемой нагрузки. Вертикальное масштабирование",
    "Collector has a lower cap on the amount of processing power and memory that can": "Collector имеет более низкий верхний предел по вычислительной мощности и памяти,",
    "be given to the Collector, but is also simpler. In Kubernetes, you can do this": "доступным Collector, но является более простым. В Kubernetes это",
    "by raising the CPU and memory limits on the Collector pod.": "выполняется путём увеличения лимитов CPU и памяти для пода Collector.",
    # --- h3: Scaling stateless Collectors ---
    "### Scaling stateless Collectors": "### Масштабирование stateless Collectors",
    # --- stateless paragraph 1 (4 lines) ---
    "It's comparatively easy to scale stateless Collectors: since it doesn't matter": "Масштабировать stateless Collectors сравнительно просто: поскольку не важно,",
    "which data goes to which Collector, the decision about which Collector to send a": "какие данные поступают в какой Collector, решение о том, в какой Collector отправить",
    "payload to can be made regardless of the contents of the data. As a result,": "полезную нагрузку, принимается независимо от содержимого данных. В результате",
    "any standard load balancer for a given transmission protocol should work.": "подойдёт любой стандартный балансировщик нагрузки для заданного протокола передачи.",
    # --- stateless paragraph 2 (7 lines) ---
    "The simplest way to balance load is through a Kubernetes Service object that": "Простейший способ балансировки нагрузки: объект Kubernetes Service,",
    "points to multiple replicas of an Collector pod deployed through any standard": "указывающий на несколько реплик пода Collector, развёрнутого с помощью любого стандартного",
    "type of Kubernetes workload such as a Deployment, ReplicaSet, StatefulSet, or": "типа рабочей нагрузки Kubernetes, такого как Deployment, ReplicaSet, StatefulSet или",
    "DaemonSet. For short-lived connections, this will distribute load among the": "DaemonSet. Для кратковременных соединений это распределит нагрузку между",
    "Collectors accessible through the service fairly evenly. Note that long-lived": "Collectors, доступными через сервис, достаточно равномерно. Обратите внимание: длительные",
    "connections, such as those over HTTP/2 or gRPC, will keep a connection open": "соединения, например по HTTP/2 или gRPC, удерживают открытое соединение",
    "to a single Collector and therefore may make the load between Collectors uneven.": "с одним Collector и поэтому могут приводить к неравномерному распределению нагрузки между Collectors.",
    # --- stateless paragraph 3 (6 lines) ---
    "For more complex cases, such as handling gRPC connections, a Service with type": "Для более сложных случаев, например при работе с соединениями gRPC, Service с типом",
    "`LoadBalancer` can offer more control over how load is balanced. LoadBalancer": "`LoadBalancer` обеспечивает более тонкое управление балансировкой нагрузки. LoadBalancer",
    "Services are able to leverage a separate load balancer to determine which": "Services могут использовать отдельный балансировщик нагрузки для определения того, в какой",
    "Collector a connection is routed to. Service meshes such as Istio or Linkerd can": "Collector маршрутизируется соединение. Сервисные сети, такие как Istio или Linkerd,",
    "also help with load balancing, as they have detailed control over network": "также могут помочь с балансировкой нагрузки, поскольку обеспечивают детальное управление сетевыми",
    "connections inside the cluster.": "соединениями внутри кластера.",
    # --- stateless paragraph 4 (5 lines) ---
    "For cases where your deployment topology matters, for example with gateway": "Если топология развёртывания имеет значение, например при шлюзовых",
    "Collectors deployed through a DaemonSet, you can use a Service object with": "Collectors, развёрнутых через DaemonSet, можно использовать объект Service со",
    "specialized routing settings to only send data to Collectors running on the same": "специализированными настройками маршрутизации, чтобы отправлять данные только тем Collectors,",
    "node as the source of the data. On Kubernetes version 1.26+, this is done by": "которые работают на том же узле, что и источник данных. В Kubernetes версии 1.26+ это",
    "configuring a service to [only accept traffic internal to a": "выполняется путём настройки сервиса на [приём только внутреннего трафика узла",
    "nodeï»¿](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/).": "](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/).",
    # --- h3: Scaling stateful processing using non-pooled Collectors ---
    "### Scaling stateful processing using non-pooled Collectors": "### Масштабирование stateful-обработки с использованием non-pooled Collectors",
    # --- stateful non-pooled intro (5 lines) ---
    "When using the Collector to do stateful processing, it's important that the same": "При использовании Collector для stateful-обработки важно, чтобы одни и те же",
    "data is always sent to the same Collector. You can increase the throughput of": "данные всегда направлялись в один и тот же Collector. Можно увеличить пропускную способность",
    "your pipeline while still following this rule by choosing certain Collectors to": "конвейера, соблюдая это правило, путём выбора определённых Collectors",
    "handle certain data. This can be done by choosing a particular deployment": "для обработки определённых данных. Это достигается выбором конкретного шаблона",
    "pattern for Collectors, or by assigning data sources to Collectors:": "развёртывания Collectors или назначением источников данных Collectors:",
    # --- bullet: Sidecar Collectors (3 lines) ---
    "* **Sidecar Collectors**: If an Collector is deployed as a sidecar and is coupled": "* **Sidecar Collectors**: если Collector развёрнут как sidecar и связан",
    "to an application, then all the data from that application will go through the": "с приложением, то все данные из этого приложения будут проходить через",
    "sidecar Collector and can be processed with stateful operations.": "sidecar Collector и могут обрабатываться с применением stateful-операций.",
    # --- bullet: DaemonSet Collectors (4 lines) ---
    "* **DaemonSet Collectors**: An agent Collector deployed to a Kubernetes node": "* **DaemonSet Collectors**: агентский Collector, развёрнутый на узле Kubernetes",
    "(such as through a DaemonSet) can be used for stateful processing if a given": "(например, через DaemonSet), можно использовать для stateful-обработки, если",
    "application on the node always sends its data to the Collector. Note that this": "приложение на этом узле всегда отправляет данные в Collector. Обратите внимание: это",
    "assumes there is only a single Collector per node.": "предполагает наличие только одного Collector на узел.",
    # --- bullet: Single Collector (8 lines) ---
    "* **Single Collector**: If you only need to run a": "* **Single Collector**: если требуется запустить",
    "single Collector for a given set of data sources, this Collector can be used": "только один Collector для заданного набора источников данных, этот Collector",
    "for stateful processing since all data will flow through the same Collector.": "можно использовать для stateful-обработки, так как все данные будут проходить через него.",
    "You may choose this if you decide to send a particular signal or data from a": "Это может быть уместно, если нужно отправлять определённый сигнал или данные из",
    "chosen set of applications to a given Collector. Note that for": "выбранного набора приложений в конкретный Collector. Обратите внимание: для",
    "high-availability, redundant Collector instances must be kept as backups and": "обеспечения высокой доступности резервные экземпляры Collector должны находиться в режиме",
    "not receive data unless the first Collector goes down. Additionally,": "горячего резерва и не получать данные, пока основной Collector работает. Кроме того,",
    "processing will be reset if a redundant Collector is activated.": "при активации резервного Collector обработка будет сброшена.",
    # --- h3: Scaling pooled stateful Collectors with the Load Balancing Exporter ---
    "### Scaling pooled stateful Collectors with the Load Balancing Exporter": "### Масштабирование pooled stateful Collectors с помощью Load Balancing Exporter",
    # --- load balancing exporter intro (7 lines) ---
    "Scaling a horizontally-scaled pool of stateful Collectors likely necessitates": "Масштабирование горизонтально масштабируемого пула stateful Collectors, как правило,",
    "using the [Load Balancing": "требует использования [Load Balancing",
    "Exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter).": "Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter).",
    "The Load Balancing Exporter turns the": "Load Balancing Exporter превращает",
    "Collector into an OTLP-aware load balancer that allows you to route data to a": "Collector в OTLP-совместимый балансировщик нагрузки, позволяющий маршрутизировать данные в",
    "specific downstream Collector based on information inside an OTLP payload such": "конкретный нижестоящий Collector на основе информации внутри OTLP-полезной нагрузки,",
    "as a metric name.": "например по имени метрики.",
    # --- development stability note (4 lines) ---
    "Note that for metrics, the Load Balancing Exporter component has a [Development": "Обратите внимание: для метрик компонент Load Balancing Exporter имеет [уровень стабильности",
    "stability": "Development",
    "levelï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/docs/component-stability.md).": "](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/docs/component-stability.md).",
    "It is not recommended for production use at this time.": "На данный момент его использование в продакшне не рекомендуется.",
    # --- h4: Stateful processors (PASS) ---
    # --- stateful processors intro (6 lines) ---
    "You will want to consider using the exporter if you are scaling and using any": "Использование exporter следует рассмотреть при масштабировании с применением любого",
    "of the following stateful components. We only cover components": "из перечисленных ниже stateful-компонентов. Здесь рассматриваются только компоненты,",
    "included in the Dynatrace Collector here, you": "включённые в Dynatrace Collector;",
    "will need to determine the best default for any other stateful components you": "для любых других используемых stateful-компонентов необходимо самостоятельно определить",
    "use. You can also configure which part of the data is used for routing. The best": "наилучшее значение по умолчанию. Также можно настроить, какая часть данных используется для маршрутизации. Наилучший",
    "key to use depends on your use-case, but we give recommendations below.": "ключ зависит от вашего сценария использования; рекомендации приведены ниже.",
    # --- bullet: Cumulative to Delta Processor (5 lines) ---
    "* The [Cumulative to Delta": "* [Cumulative to Delta",
    "Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor):": "Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor):",
    "Data points for the same metric are required to be sent to the same Collector": "Точки данных для одной метрики должны отправляться в один и тот же Collector",
    "for the collection period of the metric. The `metric_name` key is therefore a": "в течение периода сбора метрики. Поэтому ключ `metric_name` является",
    "good default for routing.": "хорошим значением по умолчанию для маршрутизации.",
    # --- bullet: Tail Sampling Processor (6 lines) ---
    "* The [Tail Sampling": "* [Tail Sampling",
    "Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/tailsamplingprocessor):": "Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/tailsamplingprocessor):",
    "In order to make a decision about whether to sample a trace, the processor": "Чтобы принять решение о сэмплировании трассировки, processor",
    "must be able to see all spans within the trace. Therefore, all spans must be": "должен видеть все спаны в рамках трассировки. Поэтому все спаны должны",
    "sent to the same Collector, and we recommend routing by the `traceID` key to": "отправляться в один Collector; рекомендуется маршрутизация по ключу `traceID`,",
    "accomplish this.": "чтобы обеспечить это.",
    # --- bullet: Span Metrics Connector (4 lines) ---
    "* The [Span Metrics": "* [Span Metrics",
    "Connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector):": "Connector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector):",
    "The connector needs to see all spans from a service in order to emit metrics": "Connector должен видеть все спаны сервиса, чтобы генерировать метрики",
    "about its performance. Therefore we highly recommend routing by the `service`": "о его производительности. Поэтому настоятельно рекомендуется маршрутизация по ключу `service`.",
    "key.": "",
    # --- h4: Configuring the Load Balancing Exporter ---
    "#### Configuring the Load Balancing Exporter": "#### Настройка Load Balancing Exporter",
    # --- config intro (4 lines) ---
    "There are two important elements involved with configuring the [Load Balancing": "Настройка [Load Balancing",
    "Exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter):": "Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter)",
    "the key used to route the data, and the method the exporter uses to find": "предполагает два важных элемента: ключ для маршрутизации данных и метод, используемый exporter для поиска",
    "Collectors in the pool.": "Collectors в пуле.",
    # --- routing_key paragraph ---
    "Configuring the routing key is done by setting the `routing_key` option. The defaults for each signal are:": "Настройка ключа маршрутизации выполняется с помощью параметра `routing_key`. Значения по умолчанию для каждого сигнала:",
    # --- routing key bullets (5 lines) ---
    "* Traces: `traceID`": "* Traces: `traceID`",
    "* Metrics: `service`": "* Metrics: `service`",
    "* Logs: `traceID` if present, otherwise a random trace ID. The `routing_key`": "* Logs: `traceID`, если присутствует; иначе случайный trace ID. Параметр `routing_key`",
    "option will not override this behavior and will have no effect on how logs are": "не переопределяет это поведение и не влияет на маршрутизацию логов.",
    "routed.": "",
    # --- recommendation after routing key (3 lines) ---
    "We recommend you leave these as the default or set them based on the": "Рекомендуется оставить эти значения по умолчанию или задать их на основе",
    "recommendations in the [Stateful processors](#stateful-processors) section": "рекомендаций из раздела [Stateful processors](#stateful-processors)",
    "above.": "выше.",
    # --- resolver paragraph (8 lines) ---
    "The other important configuration option is the `resolver` key, which is used": "Другой важный параметр конфигурации: ключ `resolver`, используемый",
    "by the exporter to determine which Collectors are available to forward data to.": "exporter для определения доступных Collectors, которым можно пересылать данные.",
    "In Kubernetes, we recommend using the `k8s` resolver since it is": "В Kubernetes рекомендуется использовать резолвер `k8s`, так как он является",
    "Kubernetes-native. Specifically, it supports dynamically updating the pool based": "нативным для Kubernetes. В частности, он поддерживает динамическое обновление пула на основе",
    "on which Collector pods are running, and will add or remove Collectors if the": "запущенных подов Collector и добавляет или удаляет Collectors при изменении",
    "number of replicas changes. It will also remove Collectors that become": "числа реплик. Он также удаляет Collectors, которые становятся",
    "unhealthy, ensuring high-availability requirements are met if retries are also": "неработоспособными, обеспечивая выполнение требований высокой доступности при условии, что повторные попытки тоже",
    "configured through the `retry_on_failure` option.": "настроены с помощью параметра `retry_on_failure`.",
    # --- static resolver note (4 lines) ---
    "Note that configuring the `static` resolver with a set pool of Collectors can": "Обратите внимание: настройка резолвера `static` с фиксированным пулом Collectors может",
    "cause data loss if an Collector goes down and is not replaced before the retry": "привести к потере данных, если Collector выходит из строя и не заменяется до исчерпания",
    "limit is met. The Collectors configured in the pool are set for the lifetime of": "лимита повторных попыток. Collectors, настроенные в пуле, фиксируются на время жизни",
    "the load-balancing Collector.": "load-balancing Collector.",
    # --- h4: Resiliency ---
    "#### Resiliency": "#### Отказоустойчивость",
    # --- resiliency paragraph (6 lines) ---
    "The load balancing exporter comes with resiliency options to help mitigate the": "Load balancing exporter оснащён параметрами отказоустойчивости для снижения",
    "risk of data loss. These options are both for dealing with a fluctuating number of downstream": "риска потери данных. Эти параметры охватывают как изменяющееся число нижестоящих",
    "Collectors as well as issues sending data to a particular Collector. The": "Collectors, так и проблемы при отправке данных в конкретный Collector.",
    "[upstream": "[Документация upstream",
    "docsï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/loadbalancingexporter#resilience-and-scaling-considerations)": "](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/loadbalancingexporter#resilience-and-scaling-considerations)",
    "cover these in detail and explain how and when to use them.": "содержит подробное описание этих параметров и объясняет, как и когда их применять.",
    # --- h4: Scaling load balancer Collectors ---
    "#### Scaling load balancer Collectors": "#### Масштабирование load balancer Collectors",
    # --- scaling load balancer paragraph (7 lines) ---
    "Since the Load Balancing Exporter uses a deterministic hash to determine which": "Поскольку Load Balancing Exporter использует детерминированный хеш для определения,",
    "downstream Collector to send data to, load-balancing Collectors can be": "в какой нижестоящий Collector отправлять данные, load-balancing Collectors",
    "considered stateless and can therefore be scaled using the approaches outlined": "можно считать stateless и масштабировать с помощью подходов, описанных",
    "in the [Scaling stateless OTel Collectors](#scaling-stateless-collectors) section.": "в разделе [Масштабирование stateless Collectors](#scaling-stateless-collectors).",
    "Note that if the resolver for the load-balancing Collectors update their": "Обратите внимание: если резолверы load-balancing Collectors обновляют свои",
    "downstream pools at different times, this may result in data meant for a single": "нижестоящие пулы в разное время, это может привести к тому, что данные, предназначенные для одного",
    "Collector momentarily being sent to multiple Collectors.": "Collector, на короткое время будут отправляться в несколько Collectors.",
    # --- h2: Demo configuration (in S) ---
    # --- h2: Components (in S) ---
    # --- "For our configuration, we use..." (in S) ---
    # --- h3: Receivers (PASS) ---
    # --- receiver description ---
    "Under `receivers`, we configure the [`otlp` receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) to receive data over gRPC and HTTP.": "В разделе `receivers` мы настраиваем [receiver `otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) для приёма данных по gRPC и HTTP.",
    # --- h3: Exporters (PASS) ---
    # --- exporters description (9 lines) ---
    "In the `exporters` section, we configure three [`loadbalancing exporters`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter),": "В разделе `exporters` мы настраиваем три [exporter `loadbalancing`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter),",
    "one for each signal. The exporters are all configured to use the `k8s` resolver,": "по одному на каждый сигнал. Все exporters настроены на использование резолвера `k8s`,",
    "which uses a Kubernetes service to determine the pool of Collectors to send data": "который использует Kubernetes service для определения пула Collectors, в который отправляются данные.",
    "to. One reason to split further processing by signal is that each signal likely": "Одна из причин разделить дальнейшую обработку по сигналам: каждый сигнал, вероятно,",
    "receives different amounts of traffic: for example, you may receive a large": "получает разный объём трафика. Например, может поступать большой",
    "amount of logs, some traces, and relatively few metrics. Therefore, you would": "объём логов, некоторое количество трассировок и сравнительно мало метрик. Поэтому",
    "want the Collector pool that processes logs to be bigger than the one that processes": "пул Collectors для обработки логов должен быть больше пула для обработки",
    "metrics; extra Collectors allocated for processing fewer metrics may waste": "метрик; дополнительные Collectors, выделенные на обработку меньшего числа метрик, могут",
    "resources.": "нерационально использовать ресурсы.",
    # --- h3: Service pipelines (in S) ---
    # --- service pipelines description (4 lines) ---
    "In our pipelines, we receive data over OTLP and export it through the Load": "В наших конвейерах мы принимаем данные по OTLP и экспортируем их через Load",
    "Balancing Exporter for the particular signal, without doing any additional": "Balancing Exporter для конкретного сигнала без какой-либо дополнительной",
    "processing. Since this Collector is exclusively for load balancing, we want to": "обработки. Поскольку данный Collector предназначен исключительно для балансировки нагрузки,",
    "do as little processing as possible so it can handle as much data as possible.": "необходимо выполнять как можно меньше обработки, чтобы он справлялся с максимальным объёмом данных.",
    # --- h2: Related topics (in S) ---
    # --- related topics bullets ---
    '* [Batch OTLP requests with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")': '* [Группирование OTLP-запросов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.")',
    '* [Apply memory limits to the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")': '* [Применение ограничений памяти к OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")',
    **S,
}

PASS = {
    "### Receivers",
    "### Exporters",
    "#### Stateful processors",
}

# --- Post-build polish (critical review) -----------------------------------
# The borrowed Latin noun "Collector" is number-invariant in Russian; the English
# plural "Collectors" is wrong, and after a quantifier/count it needs a Russian
# support word ("экземпляров Collector"), per the corpus norm (L4-IF.67). These
# fixes run on the built RU file (no EN keys there, so replacement is safe) and
# survive a rebuild. Headings and the bold pattern-labels (Sidecar/DaemonSet
# Collectors) mirror the EN section structure and are intentionally left as-is.
FIX = [
    (
        "Масштабировать stateless Collectors сравнительно",
        "Масштабировать stateless Collector сравнительно",
    ),
    (
        "Collectors, доступными через сервис",
        "экземплярами Collector, доступными через сервис",
    ),
    (
        "распределению нагрузки между Collectors.",
        "распределению нагрузки между экземплярами Collector.",
    ),
    (
        "Collectors, развёрнутых через DaemonSet",
        "экземплярах Collector, развёрнутых через DaemonSet",
    ),
    ("только тем Collectors,", "только тем экземплярам Collector,"),
    ("выбора определённых Collectors", "выбора определённых экземпляров Collector"),
    (
        "развёртывания Collectors или назначением источников данных Collectors:",
        "развёртывания для экземпляров Collector или назначением источников данных экземплярам Collector:",
    ),
    ("пула stateful Collectors,", "пула экземпляров stateful Collector,"),
    ("Collectors в пуле.", "экземпляров Collector в пуле."),
    (
        "определения доступных Collectors, которым",
        "определения доступных экземпляров Collector, которым",
    ),
    (
        "добавляет или удаляет Collectors при изменении",
        "добавляет или удаляет экземпляры Collector при изменении",
    ),
    (
        "также удаляет Collectors, которые становятся",
        "также удаляет экземпляры Collector, которые становятся",
    ),
    (
        "с фиксированным пулом Collectors может",
        "с фиксированным пулом экземпляров Collector может",
    ),
    (
        "попыток. Collectors, настроенные в пуле,",
        "попыток. Экземпляры Collector, настроенные в пуле,",
    ),
    ("Collectors, так и проблемы", "экземпляров Collector, так и проблемы"),
    (
        "данные, load-balancing Collectors",
        "данные, экземпляры load-balancing Collector",
    ),
    (
        "резолверы load-balancing Collectors обновляют",
        "резолверы load-balancing Collector обновляют",
    ),
    ("предназначенные для одного", "предназначенные для одного экземпляра"),
    (
        "отправляться в несколько Collectors.",
        "отправляться на несколько экземпляров Collector.",
    ),
    (
        "определения пула Collectors, в который",
        "определения пула экземпляров Collector, в который",
    ),
    (
        "пул Collectors для обработки логов",
        "пул экземпляров Collector для обработки логов",
    ),
    (
        "дополнительные Collectors, выделенные",
        "дополнительные экземпляры Collector, выделенные",
    ),
]

if __name__ == "__main__":
    import os as _os

    build_one(REL, FNAME, TRANS, PASS)
    _ru = _os.path.join(
        _os.path.dirname(__file__), "..", "docs", "managed-ru", REL, FNAME
    )
    with open(_ru, encoding="utf-8", newline="\n") as _f:
        _t = _f.read()
    for _a, _b in FIX:
        if _a == _b:
            continue
        assert _a in _t, f"FIX target missing: {_a!r}"
        _t = _t.replace(_a, _b)
    with open(_ru, "w", encoding="utf-8", newline="\n") as _f:
        _f.write(_t)
    qa_one(REL, FNAME)
