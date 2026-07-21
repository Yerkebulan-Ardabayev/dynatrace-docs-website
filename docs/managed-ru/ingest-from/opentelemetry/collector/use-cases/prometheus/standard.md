---
title: Сбор метрик Prometheus с помощью OTel Collector (стандартная схема)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard
---

# Сбор метрик Prometheus с помощью OTel Collector (стандартная схема)

# Сбор метрик Prometheus с помощью OTel Collector (стандартная схема)

* Практическое руководство
* Чтение: 12 мин
* Опубликовано 23 июня 2026 г.

Эта страница описывает сбор и обработку данных с эндпоинтов Prometheus с помощью стандартного развёртывания промышленного уровня.
Такая схема использует архитектуру с [Target Allocator﻿](https://github.com/Dynatrace/otel-target-allocator) и отдельными пулами Collector для сбора и обработки данных.
Это рекомендуемый подход для большинства промышленных развёртываний, он подходит для кластеров Kubernetes, которым нужны автомасштабирование, избыточность и обработка больших объёмов данных Prometheus.

## Когда использовать этот подход

Используй эту архитектуру, если применим один или несколько следующих сценариев.

* Нагрузка превышает возможности одного Collector или небольшого набора дублированных Collector.
* Собираются данные с тысяч подов или сотен различных эндпоинтов.
* Общий объём поступающих данных, это миллионы точек данных в минуту.
* Нужно горизонтальное масштабирование пулов scraper и gateway вместо ручного разделения целей.

Если собираются данные с небольшого или статического набора эндпоинтов и автомасштабирование или избыточность не нужны, вместо этого можно использовать упрощённое развёртывание с одним Collector.
Подробнее см. [Сбор метрик Prometheus с помощью OTel Collector (упрощённая схема)](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads.").

## Предварительные требования

Для этого сценария предполагается наличие следующего:

Устанавливать всё перечисленное ниже заранее не нужно. Пошаговое руководство [Развёртывание многоуровневой архитектуры](#deploy-the-tiered-architecture) устанавливает CRD, Target Allocator и оба уровня Collector по шагам. Этот список стоит воспринимать как справку о том, что нужно для развёртывания: единственные настоящие предварительные требования, это кластер Kubernetes и доступ к Dynatrace API.

* Кластер Kubernetes с установленными Custom Resource Definitions (CRD) Prometheus Operator, это `ServiceMonitor`, `PodMonitor` и `ScrapeConfig`. Нужны только эти CRD, а не весь [Prometheus Operator﻿](https://prometheus-operator.dev/docs/getting-started/installation/). [Шаг 1](#deploy-the-tiered-architecture) руководства устанавливает пакет, содержащий только CRD.
* Один из следующих дистрибутивов Collector для уровня scraper, с [ресивером `prometheus`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/prometheusreceiver) и [экспортёром `loadbalancing`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/exporter/loadbalancingexporter):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Собственная сборка OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Один из следующих дистрибутивов Collector для уровня gateway, с процессорами [`metric_start_time`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/metricstarttimeprocessor), [`cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor), [`k8sattributes`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/k8sattributesprocessor) и [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor), а также [экспортёром `otlphttp`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Собственная сборка OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* Один из следующих дистрибутивов Target Allocator, развёрнутый через исходный Helm-чарт `opentelemetry-target-allocator`:

  + [Dynatrace Target Allocator﻿](https://github.com/Dynatrace/otel-target-allocator)
  + [Исходный OpenTelemetry Target Allocator﻿](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/)
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на который должны экспортироваться данные.
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с нужной областью доступа (требуется только для SaaS и ActiveGate).

## Обзор архитектуры

![Обзор архитектуры стандартного сценария сбора метрик OTel Prometheus](https://dt-cdn.net/images/prometheus-large-scale-arch-40e1b468cb.svg)

Обзор архитектуры стандартного сценария сбора метрик OTel Prometheus

Эта схема состоит из следующих компонентов:

* Target Allocator: Target Allocator (TA) обнаруживает цели Prometheus через Custom Resource Definition (CRD) `ServiceMonitor`, `PodMonitor` или `ScrapeConfig` и распределяет их по пулу scraper с помощью согласованного хеширования.

  Алгоритм хеширования детерминированный, поэтому каждая реплика независимо получает одинаковое распределение целей по scraper. Для отказоустойчивости стоит запускать несколько реплик.
* Scraper: развёртывание Collector. Каждый scraper опрашивает TA, собирает данные с назначенных ему целей Prometheus и передаёт данные в пул gateway через экспортёр `loadbalancing`.

  Экспортёр `loadbalancing` направляет данные по хешу ресурса, поэтому все данные от конкретного исходного пода стабильно попадают на один и тот же gateway, что сохраняет согласованность состояния по каждой серии.
* Gateway: StatefulSet из Collector. Принимает OTLP от scraper, запускает состояние процессоров `metric_start_time` и `cumulativetodelta`, применяет обогащение данными Kubernetes через `k8sattributes` и `transform`, экспортирует данные в Dynatrace.

  Процессоры `metric_start_time` и `cumulativetodelta` хранят состояние и должны видеть каждый последовательный отсчёт серии в одном месте, чтобы корректно вычислять дельты. Они работают на уровне gateway, а не на scraper, потому что экспортёр `loadbalancing` стабильно направляет все данные от конкретного источника на один и тот же gateway, поэтому полный поток отсчётов каждой серии сходится там же, даже при автомасштабировании пула scraper.
  Запуск gateway как StatefulSet даёт каждой реплике устойчивую идентичность и упорядоченный выкат, что делает набор эндпоинтов пула gateway предсказуемым во время событий масштабирования.

## Эталонная конфигурация

Эталонная конфигурация доступна в GitHub-репозитории Dynatrace OTel Collector, см.
[`config_examples/prometheus-large-scale/`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/tree/main/config_examples/prometheus-large-scale).

Набор включает следующие файлы YAML.

* `allocator.values.yaml`: значения Helm для TA
* `tier1-scraper.values.yaml`: значения Helm для развёртывания scraper
* `tier2-gateway.values.yaml`: значения Helm для StatefulSet gateway
* `rbac.yaml`: ServiceAccount, ClusterRole и привязки для всех уровней
* `scrapeconfig.yaml`: пример CRD `ScrapeConfig` для обнаружения на основе аннотаций
* `selfmon-scraper.yaml`: значения Helm для отдельного Collector самомониторинга, который собирает метрики самомониторинга со всех уровней и экспортирует их напрямую в Dynatrace, независимо от основного конвейера

Значения можно применить как есть или адаптировать под собственный кластер, см. [Настройка конфигурации](#customize-configuration).

## Развёртывание многоуровневой архитектуры

Ниже приведён обзор графиков и манифестов Helm, на которые ссылается эталонная конфигурация.

В этом обзоре используются значения Helm, но это не единственный вариант.
Также можно развернуть оба уровня Collector и Target Allocator через [OpenTelemetry Operator﻿](https://github.com/open-telemetry/opentelemetry-operator), используя его пользовательские ресурсы `OpenTelemetryCollector` и `TargetAllocator`.
Оба пути требуют одинакового RBAC.

1. Установить CRD Prometheus Operator (`ServiceMonitor`, `PodMonitor`, `ScrapeConfig`), чтобы TA мог обнаруживать цели.

   ```
   kubectl apply -f https://github.com/prometheus-operator/prometheus-operator/releases/download/v0.91.0/stripped-down-crds.yaml
   ```
2. Применить RBAC для ServiceAccount TA и Collector.

   ```
   kubectl apply -f rbac.yaml
   ```
3. Развернуть TA с помощью chart'а Helm `opentelemetry-target-allocator` из upstream и предоставленных values. При необходимости запустить несколько реплик для отказоустойчивости.

   ```
   helm install otel-allocator open-telemetry/opentelemetry-target-allocator \



   --values allocator.values.yaml
   ```
4. Применить CRD `ServiceMonitor` и `PodMonitor` для рабочих нагрузок, которые нужно опрашивать. По желанию применить `ScrapeConfig` для обнаружения на основе аннотаций. Примеры каждого варианта смотри в разделе [Настройка Target Allocator](#configure-the-target-allocator). Если выполняется переход с одного Collector, смотри раздел [Миграция с одного Collector](#migrate).
5. Развернуть пул gateway перед скраперами, чтобы у экспортера `loadbalancing` были доступные назначения при первом запуске.

   ```
   helm install otel-gateway open-telemetry/opentelemetry-collector \



   --values tier2-gateway.values.yaml
   ```
6. Развернуть пул скраперов.

   ```
   helm install otel-scraper open-telemetry/opentelemetry-collector \



   --values tier1-scraper.values.yaml
   ```

## Настройка Target Allocator

TA обнаруживает цели опроса Prometheus из CRD `ServiceMonitor`, `PodMonitor` и `ScrapeConfig` и распределяет их по пулу скраперов, используя consistent hashing. Он поддерживает единое авторитетное представление о том, какой скрапер отвечает за какую цель.

Настройка того, какие CRD отслеживает TA, задаётся через селекторы меток в values Helm. Эталонная конфигурация использует метку `prometheus.dynatrace.com: "true"`:

```
prometheus_cr:



enabled: true



scrapeInterval: 15s



service_monitor_selector:



matchlabels:



prometheus.dynatrace.com: "true"



pod_monitor_selector:



matchlabels:



prometheus.dynatrace.com: "true"



scrape_config_selector:



matchlabels:



prometheus.dynatrace.com: "true"
```

### Миграция с одного Collector

Если выполняется переход с [упрощённого развёртывания](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads."), цели заданы как статические `scrape_configs` в Prometheus receiver. Target Allocator вместо этого обнаруживает цели через CRD, поэтому каждое задание опроса нужно преобразовать в `ServiceMonitor` (рекомендуется) или `PodMonitor`.

Для самого быстрого перехода от `scrape_configs` с минимальными изменениями можно вместо этого обернуть существующие статические цели в CRD `ScrapeConfig` (смотри раздел [ScrapeConfig](#scrapeconfig)). Это сохраняет статический список целей, поэтому такой вариант не получает преимуществ обнаружения сервисов на основе меток. В долгосрочной перспективе рекомендуется перейти на `ServiceMonitor` или `PodMonitor`.

Следующий пример показывает, как преобразовать одно статическое задание в эквивалентный `ServiceMonitor`.

* До, на одном Collector:

  ```
  receivers:



  prometheus:



  config:



  scrape_configs:



  - job_name: my-app



  scrape_interval: 60s



  metrics_path: /metrics



  static_configs:



  - targets: ['my-app.my-namespace.svc:8080']
  ```
* После, в виде `ServiceMonitor` (полную схему смотри в разделе [ServiceMonitor](#servicemonitor)):

  ```
  apiVersion: monitoring.coreos.com/v1



  kind: ServiceMonitor



  metadata:



  name: my-app



  labels:



  prometheus.dynatrace.com: "true"



  spec:



  selector:



  matchLabels:



  app: my-app



  endpoints:



  - port: metrics



  interval: 60s



  path: /metrics
  ```

Конфигурация `metric_start_time`, `cumulativetodelta` и `otlp_http` с одного Collector переносится в пул gateway без изменений. Меняется только форма обнаружения целей.

### ServiceMonitor

`ServiceMonitor` выбирает Service Kubernetes по метке. TA обнаруживает endpoint'ы за каждым Service и распределяет их по скраперам.

Добавь метку `prometheus.dynatrace.com: "true"` к `ServiceMonitor`:

```
apiVersion: monitoring.coreos.com/v1



kind: ServiceMonitor



metadata:



name: my-service



labels:



prometheus.dynatrace.com: "true"



spec:



selector:



matchLabels:



app: my-service



endpoints:



- port: metrics



interval: 60s
```

### PodMonitor

`PodMonitor` выбирает поды напрямую по метке, минуя абстракцию Service. Используй его, если поды предоставляют метрики, но не находятся за Service.

```
apiVersion: monitoring.coreos.com/v1



kind: PodMonitor



metadata:



name: my-pods



labels:



prometheus.dynatrace.com: "true"



spec:



selector:



matchLabels:



app: my-app



podMetricsEndpoints:



- port: metrics



interval: 60s
```

### ScrapeConfig

`ScrapeConfig` предоставляет нативную конфигурацию опроса Prometheus. Он полезен как путь миграции для конфигураций, которые уже используют аннотации подов `metrics.dynatrace.com/scrape` из модуля ActiveGate Kubernetes.

Следующий `ScrapeConfig` обнаруживает все поды в кластере и оставляет только те, у которых есть аннотация `metrics.dynatrace.com/scrape: "true"`. Он считывает аннотации `port`, `path` и `secure`, чтобы построить цель опроса. Чтобы ограничить объём памяти, потребляемый TA, стоит ограничить `kubernetesSDConfigs` конкретными пространствами имён вместо обнаружения по всему кластеру.

```
apiVersion: monitoring.coreos.com/v1alpha1



kind: ScrapeConfig



metadata:



name: dynatrace-annotations



labels:



prometheus.dynatrace.com: "true"



spec:



jobName: dynatrace-annotations



scrapeInterval: 60s



kubernetesSDConfigs:



- role: Pod



relabelings:



- sourceLabels:



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_scrape



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_scrape



action: keep



regex: true;true



- sourceLabels:



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_secure



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_secure



action: replace



regex: true;true



targetLabel: __scheme__



replacement: https



- sourceLabels:



- __address__



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_port



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_port



action: replace



regex: (.+?)(?::\d+)?;(\d+);true



targetLabel: __address__



replacement: $1:$2



- sourceLabels:



- __meta_kubernetes_pod_annotation_metrics_dynatrace_com_path



- __meta_kubernetes_pod_annotationpresent_metrics_dynatrace_com_path



action: replace



regex: (.+);true



targetLabel: __metrics_path__



replacement: $1



- sourceLabels:



- __meta_kubernetes_pod_phase



action: drop



regex: (Failed|Succeeded)
```

Этот подход не требует изменений на стороне приложения. Для новых рабочих нагрузок предпочтительнее использовать `ServiceMonitor` или `PodMonitor` для стандартной настройки Prometheus Operator.

### Масштабирование Target Allocator

TA хранит все метаданные обнаружения сервисов Prometheus (метки подов, аннотации, информацию об узлах) в памяти. На больших кластерах это может занимать несколько гигабайт.

Запускай несколько реплик TA для отказоустойчивости. Поскольку алгоритм consistent hashing детерминирован, все реплики независимо друг от друга формируют одинаковые назначения целей скраперам без координации.

Когда память становится узким местом, можно:

* Масштабироваться вертикально. Увеличить лимит памяти TA в values Helm. По желанию можно использовать [Vertical Pod Autoscaler﻿](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) для автоматизации этого.
* Сократить область обнаружения. Ужесточить правила relabeling в CRD `ScrapeConfig` или ограничить `kubernetesSDConfigs` конкретными пространствами имён, чтобы уменьшить объём метаданных, которые хранит TA.
* Использовать шардированные TA. Запускать несколько независимых экземпляров TA, каждый из которых отслеживает отдельное подмножество пространств имён. Каждый шард требует собственного выделенного пула скраперов, поскольку скрапер может опрашивать только один endpoint TA. Нижестоящие Collector'ы gateway можно использовать совместно для нескольких шардов.

## Настройка конфигурации

Эталонная конфигурация, это отправная точка. Скорректируй следующие параметры под свою рабочую нагрузку.

### Устаревание `cumulativetodelta`

Процессор `cumulativetodelta` преобразует счётчики Prometheus в дельта-метрики, отслеживая предыдущее значение каждой серии в памяти. `max_staleness` определяет, как долго процессор хранит состояние по каждой серии после последней полученной точки данных. Как только это окно истекает без обновления, процессор удаляет серию из кэша. Следующий отсчёт для этой серии рассматривается как новая начальная точка, поэтому одна дельта теряется.

Установи `cumulativetodelta.max_staleness` на gateway примерно в 10 раз больше значения `scrape_interval` Prometheus receiver. Коэффициент 10 покрывает случайные пропущенные опросы (перезапуски цели, сетевые сбои, медленные endpoint'ы), не сохраняя при этом состояние для серий, которые действительно исчезли.

Более высокие значения дольше сохраняют состояние для неактивных серий, поэтому память gateway может расти без ограничений по мере смены серий со временем (перезапуски подов, автомасштабируемые рабочие нагрузки, изменения меток). Более низкие значения вытесняют ещё активные серии между опросами, что создаёт заметные пробелы и сбрасывает текущую дельту для каждой затронутой серии.

### Горизонтальное автомасштабирование подов

Deployment scraper и StatefulSet gateway поддерживают Kubernetes [Horizontal Pod Autoscalers​](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA). Эталонная конфигурация включает настройки HPA для обоих уровней. Полную конфигурацию можно найти в следующих файлах YAML в репозитории Dynatrace Collector GitHub.

* [`tier1-scraper.values.yaml`​](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/prometheus-large-scale/tier1-scraper.values.yaml)
* [`tier2-gateway.values.yaml`​](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/prometheus-large-scale/tier2-gateway.values.yaml)

Оба уровня используют одинаковые целевые проценты утилизации: при достижении 50% памяти или 70% CPU HPA начинает масштабирование вширь и автоматически добавляет поды. Значения `minReplicas` и `maxReplicas` нужно подстраивать под ожидаемый диапазон нагрузки. Память обычно является главным ограничением для scraper'ов, потому что Prometheus receiver буферизует собранные данные в памяти. Gateway потребляют и CPU, и память, при этом использование памяти статичным процессором `cumulativetodelta` растёт пропорционально числу отслеживаемых серий.

#### Поведение Target Allocator при масштабировании

Target Allocator автоматически обнаруживает изменения в подах Collector. Когда HPA добавляет или удаляет поды scraper'ов, Target Allocator перераспределяет цели по обновлённому пулу. Согласованное хеширование сводит перетасовку к минимуму: большинство целей остаются на том же scraper'е, и только часть переходит на новые или оставшиеся поды.

#### Настройка окна стабилизации

Сборы Prometheus вызывают периодические всплески CPU и памяти. Без окна стабилизации для уменьшения масштаба эти всплески могут вызвать преждевременное уменьшение масштаба после временных провалов между сборами. Окна стабилизации HPA нужно устанавливать относительно `scrape_interval` Prometheus.

* Увеличение масштаба управляется параметром `stabilizationWindowSeconds`. Установить `stabilizationWindowSeconds: 0` (значение по умолчанию для Kubernetes), чтобы HPA увеличивал масштаб немедленно при превышении целевой утилизации, это позволяет парку поглощать рост нагрузки без задержки.
* Уменьшение масштаба управляется параметром `stabilizationWindowSeconds`. Установить `stabilizationWindowSeconds: <scrape_interval * 5>`, чтобы HPA уменьшал масштаб только после стабилизации нагрузки.

Пример YAML ниже показывает подходящую конфигурацию для интервала сбора 60 секунд.

```
behavior:



scaleUp:



stabilizationWindowSeconds: 0



scaleDown:



stabilizationWindowSeconds: 300
```

Немедленное увеличение масштаба гарантирует, что парк быстро реагирует на устойчивый рост нагрузки. Более длинное окно уменьшения масштаба предотвращает преждевременное уменьшение масштаба во время временных провалов между сборами.

## Справка по подбору размера ресурсов

В следующей таблице показано приблизительное количество реплик при разных уровнях нагрузки, измеренных в точках данных в минуту (DPM) с интервалом сбора 60 секунд. Эти значения нужно использовать как ориентир для первоначального подбора размера. Фактическое количество реплик зависит от числа серий на цель, кардинальности меток и конфигурации процессора.

Эталонная конфигурация использует следующие лимиты ресурсов на под.

* Scraper: 1 CPU, 6 ГиБ памяти
* Gateway: 2 CPU, 8 ГиБ памяти

Эти лимиты включают запас сверх типичного использования в устойчивом состоянии. Prometheus receiver буферизует весь ответ сбора в памяти перед обработкой, что вызывает резкие всплески на каждом цикле сбора. Из-за такого буферизующего поведения scraper'ы ограничены памятью, поэтому лимит ресурсов scraper'а поглощает эти периодические всплески без завершений процессов из-за нехватки памяти (OOM). Gateway нуждаются в запасе для процессора `cumulativetodelta`, память которого растёт пропорционально числу отслеживаемых серий, а использование CPU масштабируется вместе с объёмом входящих данных. Лимит ресурсов gateway учитывает как отслеживание в устойчивом состоянии, так и пакетную обработку, когда несколько scraper'ов одновременно сбрасывают данные.

| Нагрузка | Цели сбора | Реплики scraper | Реплики gateway |
| --- | --- | --- | --- |
| 1M DPM | 5 | 2 | 2 |
| 5M DPM | 30 | 6 | 2 |
| 10M DPM | 60 | 13 | 4 |
| 30M DPM | 334 | 38 | 8 |
| 60M DPM | 667 | 74 | 18 |
| 90M DPM | 1 000 | 102 | 23 |

Запросы ресурсов и `minReplicas` в HPA нужно устанавливать так, чтобы они справлялись с базовой нагрузкой, а дальше позволить HPA увеличивать масштаб. Другие лимиты ресурсов на под меняют количество реплик.

Общую информацию о масштабировании Collector можно найти в разделе [Scale OpenTelemetry Collector deployments](/managed/ingest-from/opentelemetry/collector/scaling "How to scale the OpenTelemetry Collector.").

### Подбор размера под конкретные задачи и вертикальное масштабирование

Если нужно настроить распределение ресурсов подов Collector под конкретный сценарий использования, рекомендуется начать со следующих лимитов для каждого уровня, при условии одного экземпляра на каждом уровне, на 1 миллион точек данных в минуту (DPM):

* Scraper Collector: 1 ядро CPU, 6 ГиБ памяти
* Gateway Collector: 500 миллиядер CPU, 2 ГиБ памяти

Хотя одного пода на каждом уровне должно быть достаточно для такого уровня нагрузки, всё же рекомендуется запускать как минимум один дополнительный Collector для избыточности, чтобы предотвратить потерю данных.

При такой настройке требования к ресурсам масштабируются линейно вместе с нагрузкой, поэтому кратные этим лимитам значения также можно использовать как ориентир для определения нужного размера в конкретной ситуации.

Вертикальное масштабирование понадобится при обработке особо крупных целей, которые нельзя разделить между несколькими scraper'ами. Раздел про [устранение неполадок с точками перегрузки](#hotspots-from-uneven-load) содержит больше информации о том, как определить, что возникла именно такая ситуация.

### Изменение распределения ресурсов для Target Allocator

Target Allocator очень эффективен даже при высоких нагрузках. Поскольку он сам не обрабатывает данные, он масштабируется не со скоростью приёма метрик, а с числом подов, экспонирующих метрики Prometheus. Он работает как синглтон и в большинстве случаев не требует настройки.

В следующей таблице показаны рекомендуемые лимиты ресурсов Target Allocator, которые можно использовать как ориентир для подбора подходящего размера для кластера. Требования к ресурсам не масштабируются линейно с количеством целей scraper'а, они растут относительно медленно.

| Цели сбора | Лимит CPU | Лимит памяти |
| --- | --- | --- |
| 200 | 10m | 256 МиБ |
| 5000 | 100m | 512 МиБ |
| 20000 | 1 (1000m) | 1 ГиБ |

## Ограничения распределения нагрузки на основе хеширования

Target Allocator и экспортёр `loadbalancing` распределяют работу по хешу, а не по фактическому потреблению ресурсов. HPA масштабирует парк на основе средней утилизации, но ни один из компонентов не перераспределяет работу в сторону экземпляров с меньшей нагрузкой.

* Уровень scraper: Target Allocator назначает цели scraper'ам, хешируя идентичность цели, при этом не учитывается, сколько серий производит каждая цель. Цель с 500 000 серий и цель со 100 сериями обрабатываются одинаково. Экспортёр `loadbalancing` на scraper'е затем направляет данные к gateway, хешируя идентичность ресурса, что закрепляет все данные от заданного исходного пода за одним gateway.
* Уровень gateway: gateway, получающий данные от тяжёлого исходного пода, несёт больше нагрузки, чем его соседи, независимо от того, сколько реплик gateway добавляет HPA.
* Одна цель должна помещаться в один под. Target Allocator назначает каждую цель ровно одному scraper'у, и этот scraper буферизует весь ответ сбора в памяти. Лимиты ресурсов пода являются жёстким потолком для любой отдельной цели. HPA может добавлять больше подов в парк, но не может разделить одну цель между несколькими подами. Если одна цель производит больше данных, чем может обработать один под, добавление реплик не поможет.
* Добавление реплик не перемещает существующие назначения. HPA может увеличивать или уменьшать парк, но тяжёлая цель остаётся на том же scraper'е, а её данные остаются закреплёнными за тем же gateway.

Чтобы смягчить это поведение, можно:

* Разделить тяжёлые нагрузки на отдельные цели сбора. Если приложение может экспонировать метрики на нескольких портах или путях, каждый из них становится отдельной целью, которую Target Allocator может назначить разным scraper'ам. Аналогично можно использовать отдельные CRD `ServiceMonitor` или `ScrapeConfig` с узкими селекторами меток, чтобы тяжёлые поды воспринимались как отдельные цели, а не группировались вместе.
* Масштабировать вертикально под самую тяжёлую цель. Установить лимиты ресурсов на под достаточно высокими, чтобы обрабатывать самую крупную отдельную цель, которую может получить любой scraper. Поскольку HPA не может разделить цель между подами, лимиты на под определяют максимальный размер цели, который поддерживает архитектура.
* Принять дисбаланс. Если тяжёлых целей немного, а разделение непрактично, стоит слегка резервировать ресурсы в пуле с запасом.

## Проверка развёртывания

После развёртывания всех уровней нужно проверить, что данные проходят от собираемых целей через конвейер Collector в Dynatrace.

### Проверка метрик самомониторинга

Самомониторинг включён по умолчанию на всех Collector'ах. Нужно убедиться, что ключевые метрики показывают здоровые значения на каждом Collector в архитектуре. Инструкции по настройке см. в [Enable OpenTelemetry Collector self-monitoring](/managed/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with self-monitoring features.").

Нужно установить самомониторинг `level: detailed`, чтобы были доступны все метрики, перечисленные ниже. Референсная конфигурация уже включает экспортер телеметрии самомониторинга в значениях Helm каждого уровня.

Проверь следующие метрики на каждом уровне.

#### Уровень scraper

| Метрика | На что обратить внимание |
| --- | --- |
| `otelcol_receiver_accepted_metric_points` | Увеличивается после каждого цикла сбора. Если остаётся постоянной или на нуле, receiver Prometheus не собирает данные ни с одной цели. |
| `otelcol_processor_incoming_items` / `otelcol_processor_outgoing_items` | Количество входящих и исходящих значений должно совпадать. Разрыв между ними указывает, что processor отбрасывает данные (например, срабатывает `memory_limiter`). |
| `otelcol_exporter_send_failed_metric_points` | Должно быть равно нулю или близко к нулю. Ненулевые значения означают, что exporter `loadbalancing` не может достучаться до пула gateway. |
| `otelcol_loadbalancer_num_resolutions` | Увеличивается каждый раз, когда exporter повторно разрешает DNS gateway. Частые всплески в стабильном состоянии указывают на нестабильность DNS или на частую смену подов gateway. |

#### Уровень gateway

| Метрика | На что обратить внимание |
| --- | --- |
| `otelcol_receiver_accepted_metric_points` | Должно соответствовать общему объёму, отправленному всеми scraper. Значительное расхождение означает потерю данных между уровнями. |
| `otelcol_processor_incoming_items` / `otelcol_processor_outgoing_items` | Количество входящих и исходящих значений должно совпадать. Разрыв указывает, что processor (обычно `memory_limiter`) отбрасывает данные на gateway. |
| `otelcol_exporter_sent_metric_points` | Стабильно увеличивается. Если отстаёт от количества receiver, проверь ошибки exporter и размер очереди. |

### Проверка назначений Target Allocator

Запроси HTTP API Target Allocator, чтобы убедиться, что он обнаружил цели и распределил их по пулу scraper.

1. Настрой port-forward к поду Target Allocator.

   ```
   kubectl port-forward svc/otel-allocator 8080:80
   ```
2. Получи список всех обнаруженных задач сбора (scrape job).

   ```
   curl -s http://localhost:8080/jobs | jq .
   ```
3. Получи список целей и назначенный им Collector для конкретной задачи. Замени `<job-name>` на имя задачи из предыдущего шага.

   ```
   curl -s http://localhost:8080/jobs/<job-name>/targets | jq .
   ```

Ответ группирует цели по Collector ID. Каждый ключ, это collector, а его значение содержит цели, назначенные этому collector'у. Проверь, что:

* Все ожидаемые цели присутствуют в ответе.
* Цели распределены между несколькими Collector ID (не все назначены одному scraper).
* Ни одна цель не числится неназначенной.

Для визуального обзора назначений цель-Collector используй скрипт [`ta-visualize.py`﻿](https://bitbucket.lab.dynatrace.org/users/bernhard.aichinger/repos/k8s-monitoring/browse/phase-2-tiered/ta-visualize.py). Он запрашивает API Target Allocator и строит наглядное отображение того, какие цели назначены каким scraper.

## Устранение распространённых проблем

### Отсутствующие метрики

Если ожидаемые метрики не появляются в Dynatrace, проверь следующие причины.

* **Несовпадение label selector в CRD**: Target Allocator обнаруживает цели через CRD `ServiceMonitor`, `PodMonitor` или `ScrapeConfig`. Если метки на целевой нагрузке не совпадают, Target Allocator её так и не обнаружит. Используй `kubectl get servicemonitor -o yaml` и сравни `matchLabels` с фактическими метками на целевом Service или Pod.
* **Отсутствует RBAC для Target Allocator**: ServiceAccount Target Allocator нужны права `get`, `list` и `watch` на `ServiceMonitor`, `PodMonitor`, `ScrapeConfig`, Pods, Services, Endpoints и Nodes. Отсутствие прав приводит к незаметным сбоям обнаружения. Проверь логи Target Allocator на ошибки прав доступа.
* **Цель недоступна с подов scraper**: scraper должен иметь возможность достучаться до конечной точки метрик цели по сети. Убедись, что ни один `NetworkPolicy` не блокирует трафик из namespace scraper в namespace цели, и что порт цели указан верно.
* **Selector Service или Pod не совпадает ни с одной нагрузкой**: `ServiceMonitor` может ссылаться на Service, у которого нет подходящих Endpoints, а у `PodMonitor` `selector` может совпадать с нулём Pod. Используй `kubectl get endpoints <service-name>`, чтобы убедиться, что у Service есть активные endpoints.

### Дублирование данных

Если в Dynatrace видны дублирующиеся значения метрик, проверь следующие сценарии.

* **Несколько scraper с одинаковым `collector_id`**: каждый scraper должен регистрироваться в Target Allocator под уникальным Collector ID. Если два scraper используют один и тот же ID, оба получают одинаковые назначения целей и опрашивают одни и те же endpoint'ы. Референсная конфигурация задаёт `collector_id: ${K8S_POD_NAME}` в блоке `target_allocator` receiver'а Prometheus, что гарантирует регистрацию каждого пода под собственным именем. Используй шаги из [Проверка назначений Target Allocator](#inspect-target-allocator-assignments), чтобы проверить, какие Collector ID присутствуют и не назначены ли одни и те же цели нескольким scraper.
* **Collector'ы вне `collector_selector` Target Allocator**: если запущены дополнительные Collector'ы, которые опрашивают endpoint'ы Prometheus независимо (не управляются Target Allocator), они могут пересекаться со scraper, управляемыми Target Allocator. Убедись, что цели, назначенные Target Allocator, опрашивают только scraper, управляемые Target Allocator.

### Target Allocator не распределяет цели

Если API `/targets` не возвращает записей или все цели назначены одному scraper, проверь следующее.

* **CRD не подхвачены**: Target Allocator отслеживает ресурсы `ServiceMonitor`, `PodMonitor` и `ScrapeConfig`. Если эти CRD находятся в namespace, который Target Allocator не настроен отслеживать, они игнорируются. Проверь конфигурацию `prometheus_cr` Target Allocator: поля `service_monitor_selector`, `pod_monitor_selector` и `scrape_config_selector` фильтруют, какие CRD подхватывает Target Allocator по метке.
* **Под Target Allocator не запущен**: используй `kubectl get pods`, чтобы убедиться, что под Target Allocator запущен и готов. Проверь его логи на ошибки.
* **`collector_selector` отсутствует или указан неверно**: Target Allocator использует `collector_selector`, чтобы определить, каким подам Collector распределять цели. Если этот selector не совпадает с метками подов scraper, у Target Allocator нет пула для распределения. Убедись, что label selector в `collector_selector` Target Allocator совпадает с метками на шаблоне пода Deployment scraper.

### Хотспоты из-за неравномерной нагрузки

Если некоторые поды scraper или gateway показывают заметно более высокое потребление ресурсов, чем остальные, дисбаланс вызван распределением на основе хэша. См. [Ограничения распределения нагрузки на основе хэша](#limitations-of-hash-based-load-distribution) с объяснением причины.

Признаки дисбаланса в метриках самомониторинга:

* У одного scraper значительно выше скорость `otelcol_receiver_accepted_metric_points`, чем у остальных.
* У одного gateway выше использование памяти или CPU, чем у остальных, что видно по метрикам `otelcol_process_memory_rss` или `otelcol_process_cpu_seconds`.

Чтобы смягчить хотспоты, масштабируй вертикально, увеличив лимиты ресурсов на под для перегруженного уровня.

### OOM kills на scraper или gateway

Если поды scraper или gateway убиваются со статусом `OOMKilled`, лимит памяти пода слишком низок для нагрузки.

* **OOM kills на scraper**: receiver Prometheus буферизует весь ответ сбора в памяти. Одна цель, экспонирующая большое количество series, может вызвать всплеск потребления памяти, превышающий лимит пода. Увеличь лимит памяти пода scraper или уменьши количество series на цель, разделив тяжёлые цели.
* **OOM kills на gateway**: processor `cumulativetodelta` отслеживает состояние по каждой series в памяти. Высокая кардинальность series или большое значение `max_staleness` со временем увеличивает использование памяти. Уменьши `max_staleness`, чтобы быстрее вытеснять устаревшие series, либо увеличь лимит памяти пода gateway.
* **Processor `memory_limiter`**: если настроен, processor `memory_limiter` отбрасывает данные до того, как под достигнет лимита памяти. Сравни `otelcol_processor_incoming_items` и `otelcol_processor_outgoing_items` на затронутом уровне. Разрыв между ними означает, что `memory_limiter` отбрасывает данные. Если он срабатывает часто, под недостаточно обеспечен ресурсами для данной нагрузки.

### Проблемы маршрутизации exporter'а load-balancing

Экспортер `loadbalancing` на уровне scraper направляет данные в gateway, хешируя ключ, полученный из данных OTLP.

* **`routing_key: resource` против `routing_key: streamID`**: ключ маршрутизации `resource` (используется по умолчанию) хеширует все атрибуты ресурса, поэтому все метрики от заданного исходного пода попадают на один и тот же gateway. Это эффективно, поскольку экспортер вычисляет один хеш на ресурс, но может создавать точки перегрузки, когда один исходный под генерирует много серий. Ключ маршрутизации `streamID` хеширует полную идентичность потока (ресурс, область видимости, имя метрики и атрибуты точки данных), что распределяет отдельные потоки метрик по gateway для более равномерной нагрузки. Процессор `cumulativetodelta` по-прежнему работает корректно с `streamID`, поскольку каждый уникальный поток стабильно направляется на один и тот же gateway. Однако `streamID` вычисляет хеш для каждого отдельного потока точек данных, а не один раз на ресурс, что заметно повышает нагрузку на CPU на уровне scraper. Процессор `cumulativetodelta` на уровне gateway отслеживает состояние по идентичности потока независимо от ключа маршрутизации, поэтому суммарное использование памяти на всех gateway остаётся тем же. Меняется только распределение этого состояния между gateway.
* **Актуальность кеша резолвера при частой смене подов**: экспортер `loadbalancing` использует резолвер `k8s` для обнаружения IP-адресов подов gateway путём отслеживания объектов `EndpointSlice` Kubernetes. Отслеживание API реагирует быстрее, чем опрос DNS, но всё равно остаётся короткое окно во время перезапуска подов gateway или событий масштабирования, когда представление резолвера не соответствует фактической топологии. В течение этого окна экспортер может направить данные в под, который завершает работу, или пропустить только что запущенный под, что приводит к сбоям отправки. Нужно отслеживать `otelcol_loadbalancer_num_resolutions` и `otelcol_exporter_send_failed_metric_points` во время событий масштабирования. Резолверу `k8s` требуется, чтобы у ServiceAccount коллектора были права `get`, `list` и `watch` на объекты `discovery.k8s.io/v1` `EndpointSlice` в пространстве имён gateway. Без этих прав кеш резолвера остаётся пустым, и экспортер не может маршрутизировать данные ни на один бэкенд.

## Related topics

* [Scrape Prometheus metrics with the OTel Collector (simplified)](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads.")