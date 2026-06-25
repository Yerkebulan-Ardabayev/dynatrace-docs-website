---
title: Как масштабировать OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/scaling
scraped: 2026-05-12T12:34:53.654534
---

# Как масштабировать OTel Collector

# Как масштабировать OTel Collector

* Практическое руководство
* Чтение: 10 мин
* Опубликовано 30 сентября 2025 г.

Когда загрузка CPU или памяти OTel Collector превышает порог, при котором Collector
рискует оказаться перегруженным при всплеске трафика, рекомендуется либо
увеличить ресурсы, выделенные Collector, либо
распределить обработку между несколькими экземплярами Collector. Здесь рассматриваются
преимущественно решения, доступные в Kubernetes. Обратите внимание: рекомендации и примеры
в данной документации носят общий характер и могут не обеспечить оптимальную производительность
в вашем конкретном случае. Для определения наилучшего способа
масштабирования следует проанализировать собственные системы.

Дополнительные общие сведения в документации OpenTelemetry см. на странице
[Scaling the OTel Collector](https://opentelemetry.io/docs/collector/scaling/)
на сайте OpenTelemetry.

## Когда следует масштабировать

Масштабирование следует рассматривать, когда вы начинаете приближаться к пределам
ресурсов, выделенных вашему Collector. Метрики самодиагностики,
доступные через Collector, а также метрики хостовой среды
(например, Kubernetes) помогут отслеживать это.
Ниже перечислены несколько метрик, заслуживающих внимания:

* `otelcol_processor_refused_spans`: если включён [Memory Limiter
  Processor](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/processor/memorylimiterprocessor)
  (или аналогичная метрика для других сигналов), это означает,
  что Collector требуется дополнительная память для обработки текущей нагрузки.
* `otelcol_exporter_queue_capacity` и `otelcol_exporter_queue_size`: когда размер
  очереди exporter приближается к ёмкости очереди или превышает её, это
  означает, что Collector испытывает трудности с отправкой данных в бэкенд. Причиной
  может быть отсутствие свободных воркеров для отправки данных или
  перегрузка самого бэкенда. Может потребоваться увеличить вычислительную мощность,
  доступную Collector, для продолжения обработки такого объёма данных.
* `k8s.resource_quota.used`: при мониторинге кластера Kubernetes с помощью
  [Kubernetes Cluster
  Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver)
  эта метрика позволяет определить объём
  квоты CPU/памяти, использованной вашим Collector.
* `container.cpu.usage` и `container.memory.usage`: при мониторинге
  кластера с помощью [Kubelet Stats
  Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver),
  они позволяют узнать, приближается ли контейнер Collector к своим
  лимитам квоты или уже достиг их.

## Масштабирование Collector

Kubernetes предоставляет несколько типов объектов, позволяющих масштабировать Collector
в соответствии с требованиями конкретных сценариев. Для простого масштабирования можно
использовать Deployments или ReplicaSets для создания пула Collector, которыми Kubernetes
может управлять без особой предварительной настройки. Дополнительные общие сведения об
архитектурах развёртывания Collector см. в руководстве [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.").

Большинство рекомендаций в данном документе касаются горизонтального масштабирования
Collector путём создания дополнительных экземпляров или распределения экземпляров
по разным узлам. Однако если текущее развёртывание использует один экземпляр Collector
для всей обработки, сначала следует определить, достаточно ли вертикального масштабирования
для ожидаемой нагрузки. Вертикальное масштабирование
Collector имеет более низкий верхний предел по вычислительной мощности и памяти,
доступным Collector, но является более простым. В Kubernetes это
выполняется путём увеличения лимитов CPU и памяти для пода Collector.

### Масштабирование stateless Collectors

Масштабировать stateless Collector сравнительно просто: поскольку не важно,
какие данные поступают в какой Collector, решение о том, в какой Collector отправить
полезную нагрузку, принимается независимо от содержимого данных. В результате
подойдёт любой стандартный балансировщик нагрузки для заданного протокола передачи.

Простейший способ балансировки нагрузки: объект Kubernetes Service,
указывающий на несколько реплик пода Collector, развёрнутого с помощью любого стандартного
типа рабочей нагрузки Kubernetes, такого как Deployment, ReplicaSet, StatefulSet или
DaemonSet. Для кратковременных соединений это распределит нагрузку между
экземплярами Collector, доступными через сервис, достаточно равномерно. Обратите внимание: длительные
соединения, например по HTTP/2 или gRPC, удерживают открытое соединение
с одним Collector и поэтому могут приводить к неравномерному распределению нагрузки между экземплярами Collector.

Для более сложных случаев, например при работе с соединениями gRPC, Service с типом
`LoadBalancer` обеспечивает более тонкое управление балансировкой нагрузки. LoadBalancer
Services могут использовать отдельный балансировщик нагрузки для определения того, в какой
Collector маршрутизируется соединение. Сервисные сети, такие как Istio или Linkerd,
также могут помочь с балансировкой нагрузки, поскольку обеспечивают детальное управление сетевыми
соединениями внутри кластера.

Если топология развёртывания имеет значение, например при шлюзовых
экземплярах Collector, развёрнутых через DaemonSet, можно использовать объект Service со
специализированными настройками маршрутизации, чтобы отправлять данные только тем экземплярам Collector,
которые работают на том же узле, что и источник данных. В Kubernetes версии 1.26+ это
выполняется путём настройки сервиса на [приём только внутреннего трафика узла
](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/).

### Масштабирование stateful-обработки с использованием non-pooled Collectors

При использовании Collector для stateful-обработки важно, чтобы одни и те же
данные всегда направлялись в один и тот же Collector. Можно увеличить пропускную способность
конвейера, соблюдая это правило, путём выбора определённых экземпляров Collector
для обработки определённых данных. Это достигается выбором конкретного шаблона
развёртывания для экземпляров Collector или назначением источников данных экземплярам Collector:

* **Sidecar Collectors**: если Collector развёрнут как sidecar и связан
  с приложением, то все данные из этого приложения будут проходить через
  sidecar Collector и могут обрабатываться с применением stateful-операций.
* **DaemonSet Collectors**: агентский Collector, развёрнутый на узле Kubernetes
  (например, через DaemonSet), можно использовать для stateful-обработки, если
  приложение на этом узле всегда отправляет данные в Collector. Обратите внимание: это
  предполагает наличие только одного Collector на узел.
* **Single Collector**: если требуется запустить
  только один Collector для заданного набора источников данных, этот Collector
  можно использовать для stateful-обработки, так как все данные будут проходить через него.
  Это может быть уместно, если нужно отправлять определённый сигнал или данные из
  выбранного набора приложений в конкретный Collector. Обратите внимание: для
  обеспечения высокой доступности резервные экземпляры Collector должны находиться в режиме
  горячего резерва и не получать данные, пока основной Collector работает. Кроме того,
  при активации резервного Collector обработка будет сброшена.

### Масштабирование pooled stateful Collectors с помощью Load Balancing Exporter

Масштабирование горизонтально масштабируемого пула экземпляров stateful Collector, как правило,
требует использования [Load Balancing
Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter).
Load Balancing Exporter превращает
Collector в OTLP-совместимый балансировщик нагрузки, позволяющий маршрутизировать данные в
конкретный нижестоящий Collector на основе информации внутри OTLP-полезной нагрузки,
например по имени метрики.

Обратите внимание: для метрик компонент Load Balancing Exporter имеет [уровень стабильности
Development
](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/docs/component-stability.md).
На данный момент его использование в продакшне не рекомендуется.

#### Stateful processors

Использование exporter следует рассмотреть при масштабировании с применением любого
из перечисленных ниже stateful-компонентов. Здесь рассматриваются только компоненты,
включённые в Dynatrace Collector;
для любых других используемых stateful-компонентов необходимо самостоятельно определить
наилучшее значение по умолчанию. Также можно настроить, какая часть данных используется для маршрутизации. Наилучший
ключ зависит от вашего сценария использования; рекомендации приведены ниже.

* [Cumulative to Delta
  Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor):
  Точки данных для одной метрики должны отправляться в один и тот же Collector
  в течение периода сбора метрики. Поэтому ключ `metric_name` является
  хорошим значением по умолчанию для маршрутизации.
* [Tail Sampling
  Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/tailsamplingprocessor):
  Чтобы принять решение о сэмплировании трассировки, processor
  должен видеть все спаны в рамках трассировки. Поэтому все спаны должны
  отправляться в один Collector; рекомендуется маршрутизация по ключу `traceID`,
  чтобы обеспечить это.
* [Span Metrics
  Connector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/connector/spanmetricsconnector):
  Connector должен видеть все спаны сервиса, чтобы генерировать метрики
  о его производительности. Поэтому настоятельно рекомендуется маршрутизация по ключу `service`.
  

#### Настройка Load Balancing Exporter

Настройка [Load Balancing
Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter)
предполагает два важных элемента: ключ для маршрутизации данных и метод, используемый exporter для поиска
экземпляров Collector в пуле.

Настройка ключа маршрутизации выполняется с помощью параметра `routing_key`. Значения по умолчанию для каждого сигнала:

* Traces: `traceID`
* Metrics: `service`
* Logs: `traceID`, если присутствует; иначе случайный trace ID. Параметр `routing_key`
  не переопределяет это поведение и не влияет на маршрутизацию логов.
  

Рекомендуется оставить эти значения по умолчанию или задать их на основе
рекомендаций из раздела [Stateful processors](#stateful-processors)
выше.

Другой важный параметр конфигурации: ключ `resolver`, используемый
exporter для определения доступных экземпляров Collector, которым можно пересылать данные.
В Kubernetes рекомендуется использовать резолвер `k8s`, так как он является
нативным для Kubernetes. В частности, он поддерживает динамическое обновление пула на основе
запущенных подов Collector и добавляет или удаляет экземпляры Collector при изменении
числа реплик. Он также удаляет экземпляры Collector, которые становятся
неработоспособными, обеспечивая выполнение требований высокой доступности при условии, что повторные попытки тоже
настроены с помощью параметра `retry_on_failure`.

Обратите внимание: настройка резолвера `static` с фиксированным пулом экземпляров Collector может
привести к потере данных, если Collector выходит из строя и не заменяется до исчерпания
лимита повторных попыток. Экземпляры Collector, настроенные в пуле, фиксируются на время жизни
load-balancing Collector.

#### Отказоустойчивость

Load balancing exporter оснащён параметрами отказоустойчивости для снижения
риска потери данных. Эти параметры охватывают как изменяющееся число нижестоящих
экземпляров Collector, так и проблемы при отправке данных в конкретный Collector.
[Документация upstream
](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/exporter/loadbalancingexporter#resilience-and-scaling-considerations)
содержит подробное описание этих параметров и объясняет, как и когда их применять.

#### Масштабирование load balancer Collectors

Поскольку Load Balancing Exporter использует детерминированный хеш для определения,
в какой нижестоящий Collector отправлять данные, экземпляры load-balancing Collector
можно считать stateless и масштабировать с помощью подходов, описанных
в разделе [Масштабирование stateless Collectors](#scaling-stateless-collectors).
Обратите внимание: если резолверы load-balancing Collector обновляют свои
нижестоящие пулы в разное время, это может привести к тому, что данные, предназначенные для одного экземпляра
Collector, на короткое время будут отправляться на несколько экземпляров Collector.

## Демонстрационная конфигурация

```
extensions:



health_check:



endpoint: 0.0.0.0:13133



receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



exporters:



loadbalancing/traces:



protocol:



otlp:



resolver:



k8s:



service: traces-receiver.default



ports:



- 4317



loadbalancing/logs:



protocol:



otlp:



resolver:



k8s:



service: logs-receiver.default



ports:



- 4317



loadbalancing/metrics:



retry_on_failure:



enabled: true



initial_interval: 5s



max_interval: 30s



max_elapsed_time: 300s



sending_queue:



enabled: true



num_consumers: 10



queue_size: 1000



sizer: requests



protocol:



otlp:



resolver:



k8s:



service: metrics-receiver.default



ports:



- 4317



service:



extensions: [health_check]



pipelines:



metrics:



receivers: [otlp]



processors: []



exporters:



- loadbalancing/metrics



traces:



receivers: [otlp]



processors: []



exporters:



- loadbalancing/traces



logs:



receivers: [otlp]



processors: []



exporters:



- loadbalancing/logs
```

Проверка конфигурации

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы используем следующие компоненты.

### Receivers

В разделе `receivers` мы настраиваем [receiver `otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver) для приёма данных по gRPC и HTTP.

### Exporters

В разделе `exporters` мы настраиваем три [exporter `loadbalancing`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/exporter/loadbalancingexporter),
по одному на каждый сигнал. Все exporters настроены на использование резолвера `k8s`,
который использует Kubernetes service для определения пула экземпляров Collector, в который отправляются данные.
Одна из причин разделить дальнейшую обработку по сигналам: каждый сигнал, вероятно,
получает разный объём трафика. Например, может поступать большой
объём логов, некоторое количество трассировок и сравнительно мало метрик. Поэтому
пул экземпляров Collector для обработки логов должен быть больше пула для обработки
метрик; дополнительные экземпляры Collector, выделенные на обработку меньшего числа метрик, могут
нерационально использовать ресурсы.

### Сервисные конвейеры

В наших конвейерах мы принимаем данные по OTLP и экспортируем их через Load
Balancing Exporter для конкретного сигнала без какой-либо дополнительной
обработки. Поскольку данный Collector предназначен исключительно для балансировки нагрузки,
необходимо выполнять как можно меньше обработки, чтобы он справлялся с максимальным объёмом данных.

## Связанные темы

* [Группирование OTLP-запросов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Настройте OpenTelemetry Collector для отправки данных группами в бэкенд Dynatrace.")
* [Применение ограничений памяти к OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Настройте OpenTelemetry Collector для соблюдения ограничений памяти и предотвращения чрезмерного использования системных ресурсов.")