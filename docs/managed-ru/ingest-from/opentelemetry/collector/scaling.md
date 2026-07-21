---
title: Как масштабировать OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/scaling
---

# Как масштабировать OTel Collector

# Как масштабировать OTel Collector

* Практическое руководство
* Чтение 10 мин
* Опубликовано 30 сентября 2025

Когда потребление CPU или памяти OTel Collector превышает порог, при котором всплеск трафика может привести к перегрузке, рекомендуется либо увеличить ресурсы, выделенные Collector, либо распределить обработку на несколько экземпляров Collector. Здесь речь пойдёт в первую очередь о решениях, доступных в Kubernetes. Обрати внимание: рекомендации и примеры в этой документации носят обобщённый характер и могут не давать оптимальной производительности в конкретном случае, нужно проанализировать свои системы, чтобы определить лучший способ их масштабирования.

Более общие сведения приведены в документации OpenTelemetry, на странице [Scaling the OTel Collector﻿](https://opentelemetry.io/docs/collector/scaling/) на сайте OpenTelemetry.

## Когда стоит масштабировать

Масштабирование стоит рассмотреть при приближении к пределу ресурсов, выделенных Collector. Отслеживать это помогут метрики самомониторинга, доступные через Collector, и метрики среды хоста (например, Kubernetes).
Вот несколько метрик, на которые стоит обратить внимание:

* `otelcol_processor_refused_spans`: если включён [Memory Limiter
  Processor﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.156.0/processor/memorylimiterprocessor), эта метрика (или её аналог для других типов сигналов) укажет, что Collector требуется больше памяти для продолжения обработки текущей нагрузки.
* `otelcol_exporter_queue_capacity` и `otelcol_exporter_queue_size`: когда размер очереди экспортёра начинает приближаться к её ёмкости или превышать её, это говорит о том, что у Collector возникают проблемы с отправкой данных в бэкенд. Причина либо в том, что воркеры не освобождаются для отправки данных, либо в перегрузке самого бэкенда. Возможно, потребуется увеличить вычислительную мощность, доступную Collector, чтобы он продолжал обрабатывать такой объём данных.
* `k8s.resource_quota.used`: при мониторинге кластера Kubernetes с помощью [Kubernetes Cluster
  Receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/k8sclusterreceiver) эту метрику можно использовать, чтобы определить объём квоты CPU/памяти, использованной Collector.
* `container.cpu.usage` и `container.memory.usage`: при мониторинге кластера с помощью [Kubelet Stats
  Receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver) эти метрики покажут, приближается ли конкретный контейнер Collector к своим лимитам квоты или уже достиг их.

## Масштабирование Collector

В Kubernetes есть несколько типов объектов, способных масштабировать Collector в зависимости от потребностей конкретного сценария. Для простого масштабирования можно использовать Deployments или ReplicaSets, чтобы создать пул Collector'ов, которые Kubernetes сможет планировать без особых сложностей. Более общие сведения об архитектурах развёртывания Collector приведены в руководстве [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.").

Большая часть рекомендаций в этом документе касается горизонтального масштабирования Collector путём создания дополнительных экземпляров Collector или их распределения по разным машинам. Однако, если в текущем развёртывании вся обработка выполняется одним экземпляром Collector, сначала стоит определить, достаточно ли вертикального масштабирования Collector для ожидаемой нагрузки. Вертикальное масштабирование Collector имеет более низкий предел по вычислительной мощности и памяти, которые можно выделить Collector, но при этом проще. В Kubernetes это делается путём увеличения лимитов CPU и памяти для пода Collector.

Для масштабирования сбора метрик Prometheus рекомендуется использовать [стандартное развёртывание Prometheus с Target Allocator](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector."), чтобы обрабатывать большие объёмы метрик.

### Масштабирование stateless-Collector'ов

Масштабировать stateless-Collector'ы сравнительно легко: поскольку неважно, какие данные попадают в какой Collector, решение о том, какому Collector отправить payload, можно принимать независимо от содержимого данных. Благодаря этому подойдёт любой стандартный балансировщик нагрузки для данного протокола передачи.

Самый простой способ балансировки нагрузки, это объект Service Kubernetes, указывающий на несколько реплик пода Collector, развёрнутого через любой стандартный тип нагрузки Kubernetes, например Deployment, ReplicaSet, StatefulSet или DaemonSet. Для короткоживущих соединений это распределит нагрузку между Collector'ами, доступными через сервис, довольно равномерно. Обрати внимание: долгоживущие соединения, например по HTTP/2 или gRPC, будут удерживать соединение открытым с одним Collector, и поэтому нагрузка между Collector'ами может распределяться неравномерно.

Для более сложных случаев, например при обработке соединений gRPC, Service с типом `LoadBalancer` может дать больше контроля над тем, как балансируется нагрузка. Сервисы LoadBalancer могут использовать отдельный балансировщик нагрузки, чтобы определять, на какой Collector направляется соединение. Service mesh, такие как Istio или Linkerd, тоже помогают с балансировкой нагрузки, поскольку у них есть детальный контроль над сетевыми соединениями внутри кластера.

Для случаев, когда важна топология развёртывания, например при gateway-Collector'ах, развёрнутых через DaemonSet, можно использовать объект Service со специализированными настройками маршрутизации, чтобы отправлять данные только тем Collector'ам, которые работают на том же узле, что и источник данных. Начиная с версии Kubernetes 1.26+, это делается настройкой сервиса на [приём только трафика, внутреннего для узла﻿](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/).

### Масштабирование stateful-обработки с помощью непулированных Collector'ов

При использовании Collector для stateful-обработки важно, чтобы одни и те же данные всегда отправлялись на один и тот же Collector. Пропускную способность конвейера можно увеличить, соблюдая при этом это правило, выбрав определённые Collector'ы для обработки определённых данных. Это можно сделать, выбрав конкретный паттерн развёртывания для Collector'ов или назначив источники данных Collector'ам:

* **Sidecar Collector'ы**: если Collector развёрнут как sidecar и связан с приложением, то все данные этого приложения будут проходить через sidecar-Collector и могут обрабатываться операциями с состоянием.
* **DaemonSet Collector'ы**: агент-Collector, развёрнутый на узле Kubernetes (например, через DaemonSet), можно использовать для stateful-обработки, если данное приложение на узле всегда отправляет свои данные этому Collector. Обрати внимание: это предполагает, что на узле работает только один Collector.
* **Единственный Collector**: если для заданного набора источников данных нужно запускать только один Collector, этот Collector можно использовать для stateful-обработки, поскольку все данные будут проходить через один и тот же Collector. Такой вариант можно выбрать, если принято решение отправлять определённый сигнал или данные от выбранного набора приложений на конкретный Collector. Обрати внимание: для высокой доступности избыточные экземпляры Collector нужно держать в резерве и они не должны получать данные, пока первый Collector не выйдет из строя. Кроме того, при активации резервного Collector обработка сбрасывается.

### Масштабирование пула stateful-Collector'ов с помощью Load Balancing Exporter

Масштабирование горизонтально-масштабируемого пула stateful-Collector'ов, скорее всего, требует использования [Load Balancing Exporter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/exporter/loadbalancingexporter). Load Balancing Exporter превращает Collector в OTLP-совместимый балансировщик нагрузки, позволяющий маршрутизировать данные к конкретному нижестоящему Collector'у на основе информации внутри OTLP payload, например имени метрики.

Обрати внимание, что для метрик компонент Load Balancing Exporter имеет уровень стабильности [Development﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.156.0/docs/component-stability.md). На данный момент он не рекомендуется для использования в production.

#### Stateful-процессоры

Стоит рассмотреть использование этого экспортёра при масштабировании, если применяется любой из следующих stateful-компонентов. Здесь рассматриваются только компоненты, входящие в Dynatrace Collector, для остальных используемых stateful-компонентов нужно самостоятельно определить оптимальные настройки по умолчанию. Также можно настроить, какая часть данных используется для маршрутизации. Оптимальный ключ зависит от конкретного сценария использования, но ниже приведены рекомендации.

* [Cumulative to Delta Processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor): точки данных одной и той же метрики должны отправляться на один и тот же Collector в течение периода сбора метрики. Поэтому ключ `metric_name`, это хороший вариант по умолчанию для маршрутизации.
* [Tail Sampling Processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/tailsamplingprocessor): чтобы принять решение о том, сэмплировать ли трассировку, процессор должен видеть все спаны внутри трассировки. Поэтому все спаны нужно отправлять на один и тот же Collector, и для этого рекомендуется маршрутизировать по ключу `traceID`.
* [Span Metrics Connector﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/connector/spanmetricsconnector): коннектору нужно видеть все спаны сервиса, чтобы формировать метрики о его производительности. Поэтому настоятельно рекомендуется маршрутизировать по ключу `service`.

#### Настройка Load Balancing Exporter

При настройке [Load Balancing Exporter﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/exporter/loadbalancingexporter) важны два элемента: ключ, используемый для маршрутизации данных, и метод, который экспортёр применяет для поиска Collector'ов в пуле.

Ключ маршрутизации настраивается через параметр `routing_key`. Значения по умолчанию для каждого сигнала:

* Traces: `traceID`
* Metrics: `service`
* Logs: `traceID`, если он присутствует, иначе случайный trace ID. Параметр `routing_key` не переопределяет это поведение и никак не влияет на маршрутизацию логов.

Рекомендуется оставить эти значения по умолчанию или задать их согласно рекомендациям из раздела [Stateful-процессоры](#stateful-processors) выше.

Ещё один важный параметр конфигурации, ключ `resolver`, который экспортёр использует для определения того, какие Collector'ы доступны для пересылки данных. В Kubernetes рекомендуется использовать resolver `k8s`, поскольку он нативен для Kubernetes. В частности, он поддерживает динамическое обновление пула на основе того, какие поды Collector'а запущены, и добавляет или удаляет Collector'ы при изменении числа реплик. Он также удаляет Collector'ы, ставшие неисправными, обеспечивая соблюдение требований высокой доступности, если через параметр `retry_on_failure` также настроены повторные попытки.

Обрати внимание, что настройка resolver'а `static` с фиксированным набором Collector'ов может привести к потере данных, если Collector выходит из строя и не заменяется до достижения лимита повторных попыток. Collector'ы, настроенные в пуле, заданы на весь срок жизни балансирующего Collector'а.

#### Отказоустойчивость

Load balancing exporter предоставляет параметры отказоустойчивости, помогающие снизить риск потери данных. Эти параметры относятся как к колебаниям количества нижестоящих Collector'ов, так и к проблемам при отправке данных на конкретный Collector. [Документация проекта﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/loadbalancingexporter#resilience-and-scaling-considerations) подробно описывает их и объясняет, как и когда их использовать.

#### Масштабирование Collector'ов балансировщика нагрузки

Поскольку Load Balancing Exporter использует детерминированный хеш для определения, на какой нижестоящий Collector отправлять данные, балансирующие Collector'ы можно считать stateless, и поэтому их можно масштабировать с помощью подходов, описанных в разделе [Масштабирование stateless OTel Collector'ов](#scaling-stateless-collectors). Обрати внимание, что если resolver'ы балансирующих Collector'ов обновляют свои нижестоящие пулы в разное время, это может привести к тому, что данные, предназначенные для одного Collector'а, на мгновение окажутся отправлены сразу нескольким Collector'ам.

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



load_balancing/traces:



protocol:



otlp:



resolver:



k8s:



service: traces-receiver.default



ports:



- 4317



load_balancing/logs:



protocol:



otlp:



resolver:



k8s:



service: logs-receiver.default



ports:



- 4317



load_balancing/metrics:



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



- load_balancing/metrics



traces:



receivers: [otlp]



processors: []



exporters:



- load_balancing/traces



logs:



receivers: [otlp]



processors: []



exporters:



- load_balancing/logs
```

Проверка конфигурации

[Проверь свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В нашей конфигурации используются следующие компоненты.

### Receivers

В разделе `receivers` настраивается [`otlp` receiver﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/receiver/otlpreceiver) для приёма данных по gRPC и HTTP.

### Exporters

В разделе `exporters` настраиваются три [`load_balancing exporters`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.156.0/exporter/loadbalancingexporter), по одному на каждый сигнал. Все экспортёры настроены на использование resolver'а `k8s`, который использует Kubernetes-сервис для определения пула Collector'ов, на которые отправлять данные. Одна из причин дальнейшего разделения обработки по сигналам в том, что каждый сигнал, вероятно, получает разный объём трафика: например, может поступать большой объём логов, некоторое количество трассировок и относительно немного метрик. Поэтому желательно, чтобы пул Collector'ов, обрабатывающий логи, был больше пула, обрабатывающего метрики: лишние Collector'ы, выделенные для обработки меньшего объёма метрик, могут впустую расходовать ресурсы.

### Service pipelines

В наших pipeline'ах данные принимаются по OTLP и экспортируются через Load Balancing Exporter для соответствующего сигнала, без какой-либо дополнительной обработки. Поскольку этот Collector предназначен исключительно для балансировки нагрузки, желательно выполнять как можно меньше обработки, чтобы он мог обрабатывать как можно больше данных.

## Связанные темы

* [Пакетная отправка запросов OTLP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")
* [Применение ограничений памяти к OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")