---
title: Определение размеров Dynatrace ActiveGates в Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits
---

# Определение размеров Dynatrace ActiveGates в Kubernetes

# Определение размеров Dynatrace ActiveGates в Kubernetes

* Практическое руководство
* 5 минут чтения
* Обновлено 15 июля 2026 г.

Правильно заданные resource requests (и limits, если нужно) обеспечивают стабильную и предсказуемую работу экземпляров ActiveGate. Стабильный, исправный ActiveGate гарантирует непрерывный поток данных мониторинга без пропусков.

В руководстве приведены рекомендации по выбору размеров в зависимости от типа развёртывания, его масштаба и предполагаемой нагрузки.

## Рекомендации по развёртыванию

### Используйте отдельные ActiveGates

Для продуктивных развёртываний рекомендуется запускать два набора ActiveGates:

* Первый набор должен обеспечивать мониторинг платформы Kubernetes, включая интеграцию с Prometheus и функциональность Kubernetes Security Posture Management (KSPM).
* Второй набор должен обеспечивать маршрутизацию трафика OneAgent и приём телеметрии (включая приём логов по OTLP).

Использование двух наборов ActiveGates даёт несколько преимуществ:

* **Isolation**: всплеск трафика OneAgent не замедлит сбор метрик Kubernetes, и наоборот.
* **Independent scaling**: маршрутизация трафика OneAgent и мониторинг платформы имеют принципиально разные характеристики масштабирования, см. [Как масштабировать ActiveGates](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits#how-to-scale "Рекомендации по ресурсам CPU и памяти для Dynatrace ActiveGates, развёрнутых в Kubernetes, в зависимости от масштаба кластера и типа нагрузки.").
  Отдельные ActiveGates позволяют масштабировать каждое измерение независимо, не выделяя лишних ресурсов.
* **Easier troubleshooting**: при возникновении проблем сразу видно, связаны ли они с мониторингом платформы или с трафиком OneAgent, что сокращает время диагностики.

### Как масштабировать ActiveGates

Когда трафик превышает возможности текущего развёртывания ActiveGate, можно масштабировать двумя способами:

* **Scale horizontally**: увеличить количество реплик ActiveGate в конфигурации DynaKube. Это позволяет сервису Kubernetes распределять входящий трафик между несколькими экземплярами ActiveGate.
* **Scale vertically**: увеличить resource requests по CPU и памяти для реплик ActiveGate. Таблицы рекомендаций по ресурсам выше служат отправной точкой; корректировать нужно исходя из фактических требований к пропускной способности. Сначала корректируются requests, затем, при необходимости, limits. CPU limits применяются только при наличии соответствующего требования в политике.

## Рекомендации по выбору размеров

В следующих разделах рассмотрены четыре основных типа развёртывания: Kubernetes Platform Monitoring, маршрутизация и проксирование трафика OneAgent, приём логов по OTLP и совместный приём логов и маршрутизация трафика OneAgent. Определите свой тип развёртывания и примените соответствующие рекомендации.

Для каждого типа развёртывания рекомендации сгруппированы по размеру кластера: small (малый), medium (средний) и large (крупный).

| Размер кластера | Поды | Узлы |
| --- | --- | --- |
| Small | <1 000 | До 25 |
| Medium | 1 000–5 000 | До 100 |
| Large | 5 000–20 000 | До 500 |

Данное руководство не охватывает среды с более чем 20 000 подами; в качестве отправной точки используйте рекомендации для крупного кластера и постепенно увеличивайте ресурсы до достижения стабильного мониторинга без пропусков.

Количество узлов является второстепенным фактором при выборе размеров. Для кластеров свыше 500 узлов обратитесь в службу поддержки Dynatrace Support за индивидуальными рекомендациями.

### Kubernetes Platform Monitoring

В этом разделе приведены рекомендации по выбору размеров для ActiveGate, обрабатывающего Kubernetes Platform Monitoring, отдельно или в сочетании с Application Observability и Full-Stack Observability.

| Размер кластера | CPU requests | CPU limits | Memory requests | Memory limits |
| --- | --- | --- | --- | --- |
| Small | 200m | 1000m | 6 GiB | 6 GiB |
| Medium | 1000m | 2000m | 10 GiB | 10 GiB |
| Large | 2000m | 4000m | 12 GiB | 12 GiB |

### Маршрутизация и проксирование трафика OneAgent

В этом разделе приведены рекомендации по выбору размеров для ActiveGate, обрабатывающего маршрутизацию и проксирование трафика OneAgent.
Если данный ActiveGate также должен обрабатывать приём логов через API, см. [Совместный приём логов и маршрутизация трафика OneAgent](#ag-log-oa).

| Размер кластера | CPU requests | CPU limits | Memory requests | Memory limits | Реплики |
| --- | --- | --- | --- | --- | --- |
| Small | 250m | 1000m | 2 GiB | 2 GiB | 3 |
| Medium | 500m | 2000m | 4 GiB | 4 GiB | 3 |
| Large | 1000m | 4000m | 6 GiB | 6 GiB | 6 |

Рекомендации по выбору размеров основаны на тестировании с репрезентативной нагрузкой:

* **Workload**: маршрутизация трафика OneAgent, включая метрики, трассировки, события и данные модуля логов.
* **Log traffic assumption**: средняя продуктивная нагрузка 100 КБ/мин на один отслеживаемый под.

### Приём логов по OTLP

В этом разделе приведены рекомендации по выбору размеров и показатели пропускной способности для ActiveGates, обрабатывающих приём логов через конечную точку OTLP API.

| Размер кластера | CPU requests | CPU limits | Memory requests | Memory limits | Пропускная способность OTLP-логов на реплику |
| --- | --- | --- | --- | --- | --- |
| Small | 250m | 1000m | 2 GiB | 2 GiB | 350 MB/min |
| Medium | 500m | 2000m | 4 GiB | 4 GiB | 650 MB/min |
| Large | 1000m | 4000m | 6 GiB | 6 GiB | 1 200 MB/min |

Рекомендации по выбору размеров основаны на тестировании с репрезентативной нагрузкой:

* **Workload**: длительный приём логов через OTLP по HTTP (без сжатия).
* **Message sizes**: 5% extra-small (1,5 КБ), 20% small (1,5 КБ), 50% medium (2,2 КБ), 20% large (3 КБ), 5% extra-large (7,8 КБ).
* **Attribute counts**: от 5 до 100 атрибутов на запись лога.
* **Batch sizes**: от 10 до 100 сообщений на вызов API.
* **Test environment**: кластер Kubernetes на Google Cloud Platform с машинами e2-standard-8 (`x86_64`).
* **Deployment configuration**: ActiveGate подготовлен с выделением ресурсов согласно рекомендациям из таблицы выше.

Данные конфигурации ресурсов оставляют запас для пиковых всплесков трафика и отказоустойчивости реплик при обновлениях.

Значения длительной пропускной способности соответствуют производительности, прошедшей все проверки качества. Пиковая пропускная способность при всплесках может быть выше на короткое время.

### Совместный приём логов и маршрутизация трафика OneAgent

В этом разделе приведены рекомендации по выбору размеров для ActiveGate, обрабатывающего в едином развёртывании как приём логов, так и маршрутизацию трафика OneAgent.
Если ActiveGate не принимает логи через API, см. [Маршрутизация и проксирование трафика OneAgent](#activegate-for-oneagent-traffic-routing-and-proxying).

1. **Determine base configuration**: возьмите базовую конфигурацию ActiveGate для своего размера кластера из раздела [Маршрутизация и проксирование трафика OneAgent](#activegate-for-oneagent-traffic-routing-and-proxying).
2. **Calculate additional replicas for OTLP log traffic**: используйте значения пропускной способности на реплику из раздела [Приём логов по OTLP](#activegate-for-otlp-log-ingestion), чтобы рассчитать необходимое количество дополнительных реплик: `additional replicas = ceil(expected log traffic (MB/min) ÷ throughput per replica)`.
   Добавьте эти реплики к базовой конфигурации, рассчитанной на шаге 1.

Например, если кластер генерирует 1 500 МБ/мин трафика логов OTLP и используется конфигурация ресурсов medium (650 МБ/мин на реплику): `ceil(1,500 ÷ 650) = 3 additional replicas`.

При систематическом исчерпании ресурсов (загрузка CPU >80%, памяти >85% или частые паузы GC) рекомендуется разделить нагрузку на отдельные развёртывания ActiveGate вместо постоянного увеличения ресурсов одного развёртывания. Отдельные развёртывания обеспечивают лучшую изоляцию и независимое масштабирование.
Подробнее см. в разделе [Рекомендации по развёртыванию](#ag-for-k8s-platform-monitoring).

### Контрольные показатели пропускной способности маршрутизации трафика Log Agent

В этом разделе приведены контрольные показатели пропускной способности ActiveGate при маршрутизации трафика Log Agent. Указанные значения пропускной способности соответствуют объёму сжатых данных логов и отражают рекомендуемый максимум при длительной нагрузке.

Как использовать эти показатели:

* **Calculate your log traffic volume**: оцените общий объём трафика логов OneAgent (в МБ/мин). Это зависит от поведения и объёма логирования в приложении, а не только от количества подов.
* **Scale resources proportionally**: пропускная способность масштабируется приблизительно линейно по CPU и памяти. Используйте контрольные значения из таблицы выше как ориентир и корректируйте ресурсы исходя из ожидаемого объёма трафика логов.
* **Headroom is included**: указанные значения уже включают резерв на пиковые всплески трафика и отказоустойчивость реплик. При систематическом превышении рекомендованной пропускной способности добавьте реплики или увеличьте ресурсы на реплику. Подробнее см. в разделе [Как масштабировать ActiveGates](#how-to-scale).

| CPU requests | CPU limits | Memory resource requests | Memory resource limits | Максимальная устойчивая пропускная способность на реплику |
| --- | --- | --- | --- | --- |
| 500m | 2000m | 4Gi | 4Gi | 750 MB/min |

Фактическая пропускная способность может варьироваться в зависимости от инфраструктуры, версии OneAgent и состава нагрузки. Отслеживайте экземпляры ActiveGate и корректируйте ресурсы по фактическим показателям.

## Мониторинг и проверка

Отслеживайте экземпляры ActiveGate, чтобы убедиться в правильном распределении нагрузки, и корректируйте стратегию масштабирования по фактическим показателям производительности и потреблению ресурсов.

В этом разделе описано, как отслеживать ActiveGates и убедиться, что они работают в соответствии с ожиданиями.

### Признаки неработоспособного ActiveGate

Эти симптомы указывают на исчерпание ресурсов и возможную потерю данных:

* **Пробелы в данных мониторинга**: ActiveGate собирает различные типы данных независимо друг от друга (например, метрики Prometheus, события Kubernetes, сущности). Если одна задача сбора занимает более одной минуты, пробел возникает только в данных этого типа за данный интервал. Остальные задачи сбора продолжают работать в штатном режиме.

  + В метриках будет отсутствовать точка данных за соответствующую минуту.
  + События за соответствующий период сбора полностью недоступны.
  + Сущности могут не отражать последние обновления или отсутствовать полностью, если они короткоживущие.
* **Сильный CPU throttling**: устойчивый высокий throttling означает нехватку CPU. Сильный throttling может приводить к пробелам. Незначительный throttling обычно безвреден.
  Если throttling затрагивает под, обслуживающий мониторинговый ActiveGate, это может вызывать пробелы в данных.
* **Out‑of‑memory kills**: если ActiveGate завершается по OOM, данные становятся недоступны до его перезапуска. После перезапуска повторные OOM kills весьма вероятны.

### Наблюдение за работоспособностью с помощью платформенных метрик

Dynatrace предоставляет два [готовых дашборда](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") для наблюдения за работоспособностью ActiveGate: **ActiveGate diagnostic overview** и **Kubernetes Monitoring Statistics**. Чтобы перейти к ним, откройте ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** > **Ready-made** и выполните поиск дашборда по названию.

Также можно использовать [DQL](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") для запроса приведённых ниже платформенных метрик и построения собственных дашбордов или ноутбуков.

| Индикатор | Когда действовать | Классические метрики для проверки | Уровень детализации |
| --- | --- | --- | --- |
| CPU usage | Утилизация стабильно превышает 85%: увеличить CPU request. | `builtin:kubernetes.node.cpu_usage`, `builtin:kubernetes.workload.cpu_usage` | Под ActiveGate |
| CPU requests | Утилизация стабильно превышает 85%: увеличить CPU request. | `builtin:kubernetes.node.requests_cpu`, `builtin:kubernetes.workload.requests_cpu` | Под ActiveGate |
| CPU throttling | Throttling стабильно превышает 10%: увеличить CPU request. Вычисляется делением `container_cpu_cfs_throttled_periods_total` на количество периодов. | `builtin:kubernetes.workload.cpu_throttled`, `builtin:kubernetes.node.cpu_throttled` | Под ActiveGate |
| Memory working set | Потребление стабильно превышает 80%: увеличить memory requests. | `builtin:kubernetes.node.memory_working_set`, `builtin:kubernetes.workload.memory_working_set` | Под ActiveGate |
| Memory requests | Потребление стабильно превышает 80%: увеличить memory requests. | `builtin:kubernetes.node.requests_memory` `builtin:kubernetes.workload.requests_memory` | Под ActiveGate |
| Restart count | При перезапуске из-за OOM незамедлительно увеличить выделенную память во избежание повторения. | `builtin:kubernetes.container.restarts` | Под ActiveGate |
| OOM kills | Любые OOM kills: увеличить memory limits, чтобы исключить циклические перезапуски. | `builtin:kubernetes.container.oom_kills` | Под ActiveGate |
| Processing duration | Выполнение pipeline стабильно превышает 50–60 секунд: увеличить CPU request. Зависит также от объёма принимаемых данных и других факторов. | `dsfm:active_gate.kubernetes.pipeline_duration` | ID ActiveGate |
| Garbage collection times | Рост времени GC указывает на недостаточно выделенные ресурсы для ActiveGate. | `dsfm:active_gate.jvm.gc.major_collection_time` | ID ActiveGate |

### Факторы, увеличивающие потребление ресурсов

Фактически необходимые ресурсы растут вместе с:

* **Количеством подов**: основной фактор выбора размеров, количество отслеживаемых подов. Потребление ресурсов (CPU и памяти) компонентами Dynatrace ActiveGate масштабируется вместе с количеством подов прежде всего из-за возросших потребностей в обработке и хранении данных. По мере роста числа отслеживаемых подов ActiveGate обрабатывает больше данных о сущностях, событий и метрик, что приводит к более высокой нагрузке на CPU при приёме и обработке, а также к увеличению потребления памяти для кеширования информации о подах. Это основной фактор выбора размеров, а потребление масштабируется пропорционально количеству подов.
* **Объёмом трафика логов**: для ActiveGateов, обрабатывающих приём логов (через OTLP endpoints или log modules OneAgent), объём трафика логов является важным фактором выбора размеров. Требования к ресурсам масштабируются с объёмом данных логов (в МБ/мин), а не только с количеством подов. Небольшое число подов с подробным логированием может генерировать больший трафик, чем множество подов с минимальным логированием.
* **Объёмом метрик Prometheus**: количество подов с аннотациями Prometheus напрямую коррелирует с возросшими требованиями к ресурсам Dynatrace ActiveGate, прежде всего через повышенное потребление CPU. По мере роста числа аннотированных подов увеличивается объём скрейпируемых метрик, что требует больше циклов CPU для задач сбора, агрегации и пересылки. Влияние на память вторично: метрики пересылаются в тенант Dynatrace без длительного хранения на ActiveGate, однако потребление памяти пропорционально масштабируется с пиковыми скоростями приёма.
* **Количеством узлов**: потребление ресурсов (CPU и памяти) компонентами Dynatrace ActiveGate масштабируется с количеством узлов прежде всего из-за возросших накладных расходов на мониторинг и нагрузки от системных подов на уровне узлов. По мере роста числа узлов ActiveGate вынужден обрабатывать больше данных системного уровня, выполнять обработку сущностей и принимать события, что увеличивает вычислительные требования. Это вторичный фактор по сравнению с количеством подов, однако он пропорционально вносит вклад в общую потребность в ресурсах, особенно в крупных кластерах, где мониторинг на уровне узлов даёт кумулятивную нагрузку.

### Скрейпинг метрик Prometheus

Dynatrace поддерживает до 1 000 pod exporter'ов, каждый из которых может предоставлять до 1 000 метрик. Если окружение приближается к этим лимитам, нужно увеличить ресурсы, выделенные ActiveGate, для обеспечения надёжной работы.

Для высоконагруженного скрейпинга Prometheus и для новых развёртываний рекомендуется [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape Prometheus endpoints and ingest the data into Dynatrace.").

## Примеры ресурсов DynaKube

В этом разделе приведён пример манифеста с двумя ресурсами DynaKube для настройки ActiveGateов.

Манифест соответствует рекомендации по развёртыванию с использованием двух наборов ActiveGateов: одного для Kubernetes Platform Monitoring и одного для маршрутизации трафика OneAgent и приёма телеметрии.
Можно применить один или оба манифеста в зависимости от конфигурации развёртывания.

* Ресурс DynaKube `k8s-monitoring` обеспечивает платформенный мониторинг Kubernetes и рассчитан на средний кластер (1 000–5 000 узлов).
  Он содержит опциональную (закомментированную) конфигурацию Kubernetes Security Posture Management.
* Ресурс DynaKube `agents` обеспечивает маршрутизацию трафика OneAgent и рассчитан на большой кластер (5 000–20 000 узлов).
  Он содержит опциональную (закомментированную) конфигурацию для приёма логов OTLP, мониторинга логов, приёма телеметрии и OTel Collector.

Requests (и limits при необходимости) нужно скорректировать под своё окружение.

CPU limits закомментированы. Рекомендуется задавать только requests, чтобы ActiveGate мог использовать дополнительный CPU при его наличии. Если limits необходимы, устанавливать их равными requests или выше.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: k8s-monitoring



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



tokens: <SECRET NAME>



# Link to api reference for further information: https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



activeGate:



capabilities:



- kubernetes-monitoring



resources:



requests:



cpu: 1000m



memory: 10Gi



limits:



# cpu: 2000m



memory: 10Gi



#kspm:



#mappedHostPaths:



#- /boot



#- /etc



#- /proc/sys/kernel



#- /sys/fs



#- /sys/kernel/security/apparmor



#- /usr/lib/systemd/system



#- /var/lib



#templates:



#kspmNodeConfigurationCollector:



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



#tag: 1.5.2



---



apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: agents



namespace: dynatrace



# Link to api reference for further information: https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



tokens: <SECRET NAME>



metadataEnrichment:



enabled: true



oneAgent:



applicationMonitoring: {}



activeGate:



capabilities:



- routing



- debugging



resources:



requests:



cpu: 1000m



memory: 6Gi



limits:



# cpu: 4000m



memory: 6Gi



replicas: 6



#customProperties:



#value: |



#[otlp_ingest]



#otlp_ingest_enabled = true



#logMonitoring: {}



#telemetryIngest:



#protocols:



#- jaeger



#- otlp



#- statsd



#- zipkin



#serviceName: telemetry-ingest



templates:



#logMonitoring:



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-logmodule



#tag: <>



#tolerations:



#- effect: NoSchedule



#  key: node-role.kubernetes.io/master



#  operator: Exists



#- effect: NoSchedule



#  key: node-role.kubernetes.io/control-plane



#  operator: Exists



#otelCollector:



#replicas: 1



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-otel-collector



#tag: <tag>
```