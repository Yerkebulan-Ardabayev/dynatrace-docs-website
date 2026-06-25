---
title: Мониторинг метрик Prometheus
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics
scraped: 2026-05-12T11:50:05.065392
---

# Monitor Prometheus metrics

# Мониторинг метрик Prometheus

* 14-min read
* Updated on Apr 21, 2026

Prometheus — это набор инструментов мониторинга и оповещений с открытым исходным кодом, широко используемый в сообществе Kubernetes. Prometheus собирает метрики с ряда конечных точек HTTP(s), предоставляющих метрики в формате OpenMetrics.
Список доступных [экспортёров](https://dt-url.net/vd03n1m) см. в документации Prometheus.

## Приём метрик Prometheus по типам

Dynatrace поддерживает приём метрик Prometheus типов [Counter](#counter), [Gauge](#gauge), [Histogram](#histogram) и [Summary](#summary) в Kubernetes с помощью [Prometheus exporters](https://dt-url.net/lw02ror), делая их доступными для построения диаграмм, оповещений и анализа.

### Counter

Метрика Counter[1](#fn-1-1-def) Prometheus — монотонно возрастающее значение, как правило используемое для измерений, которые могут только увеличиваться или оставаться неизменными.
Dynatrace использует тип метрики [`COUNT`](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") с **дельта-кодированием**[2](#fn-1-2-def) для снижения избыточности данных при приёме.
Таким образом, значение, отображаемое в Dynatrace, отражает не фактическое значение счётчика, а его изменение (дельту) за наблюдаемый период.

Этот метод приводит к тому, что метрика Counter появляется с задержкой в одну минуту по сравнению с метрикой [Gauge](#gauge), если сбор данных для обоих типов начался одновременно.
Подробнее см. в [справочнике по протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Приём метрик Counter

**Дельта-кодирование**, используемое типом приёма [`COUNT`](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works."), означает, что принятое значение *не отражает* фактическое значение, а является разностью между измерениями.

1

[Официальная документация Prometheus: Counter](https://dt-url.net/cd02rce)

2

Дельта-кодирование (также известное как дельта-компрессия) хранит данные в виде разности между двумя наблюдениями или целевыми значениями. В первую очередь используется для редко изменяемых данных и позволяет избежать избыточности.

### Gauge

В отличие от [Counter](#counter), метрика Gauge[1](#fn-2-1-def) хранит единственное числовое значение, которое может увеличиваться и уменьшаться; как правило используется для измеренных значений, таких как текущее использование памяти или количество онлайн-пользователей. В Dynatrace для приёма данных используется тип метрики [`GAUGE`](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

1

[Официальная документация Prometheus: Gauge](https://dt-url.net/lb22r1o)

### Histogram

Гистограммы[1](#fn-3-1-def) обеспечивают визуальное представление распределения и частоты числовых данных.
Для базового имени метрики `<basename>` Dynatrace принимает данные согласно следующей таблице.

| Метрика Prometheus | Тип приёма Dynatrace |
| --- | --- |
| `<basename>_bucket{le="<upper inclusive bound>"}` | HISTOGRAM[2](#fn-3-2-def) |
| `<basename>_bucket_sum` | COUNT |
| `<basename>_bucket_count` | COUNT |

1

[Официальная документация Prometheus: Histogram](https://dt-url.net/vc02rmb)

2

Ключ метрики гистограммы получает суффикс `.histogram`. Метрика гистограммы тарифицируется как метрика count или gauge; отдельные бакеты не тарифицируются отдельно. Хранится не более 12 бакетов на точку данных гистограммы. Отрицательные границы бакетов не поддерживаются.

### Summary

Как и [Histogram](#histogram), метрика Summary[1](#fn-4-1-def) производит выборку наблюдений. В отличие от гистограммы, бакеты Summary представлены φ-квантилями, где 0 ≤ φ ≤ 1. Для базового имени метрики `<basename>` Dynatrace принимает данные согласно следующей таблице.

| Метрика Prometheus | Тип приёма Dynatrace |
| --- | --- |
| `<basename>{quantile="<φ>"}` | [`GAUGE`](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") |
| `<basename>_sum` | [`COUNT`](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") |
| `<basename>_count` | [`COUNT`](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") |

1

[Официальная документация Prometheus: Summary](https://dt-url.net/7g234n1).

### Не поддерживается

Следующие типы в настоящее время не поддерживаются Dynatrace:

* Метрики info, gaugehistogram или stateset
* Exemplars

## Предварительные требования

Рекомендуется использовать ActiveGate, работающий внутри кластера Kubernetes, из которого нужно собирать метрики Prometheus. Если ActiveGate работает за пределами отслеживаемого кластера (например, на виртуальной машине или в другом кластере Kubernetes), он не сможет собирать данные с конечных точек Prometheus на подах, требующих аутентификации (например, [RBAC](#rbac) или [аутентификации клиента](#client)). ActiveGates внутри кластеров также обеспечивают лучшую производительность.

* В Dynatrace перейдите на страницу настроек мониторинга кластера Kubernetes и включите:

  + **Monitor Kubernetes namespaces, services, workloads, and pods**
  + **Monitor annotated Prometheus exporters**
* Аннотированные определения подов (подробнее ниже).
* Убедитесь, что ваши сетевые политики разрешают ActiveGate подключаться к экспортёрам.

  Например, если ActiveGate развёрнут в кластере Kubernetes с помощью Dynatrace Operator, аннотированные экспортёры Prometheus находятся в пространстве имён `online-boutique`, а для этого пространства имён определена сетевая политика, необходимо убедиться, что под ActiveGate в пространстве имён `dynatrace` может подключаться к аннотированным экспортёрам Prometheus в пространстве имён `online-boutique`.

## Аннотирование подов с экспортёрами Prometheus

Dynatrace собирает метрики со всех подов, аннотированных свойством `metrics.dynatrace.com/scrape: true` в определении пода. Эта функция применяется ко всем подам во всём кластере Kubernetes, независимо от того, находится ли под в пространстве имён, соответствующем селектору пространства имён Dynakube.

В зависимости от конкретного экспортёра в поде может потребоваться задать дополнительные аннотации, чтобы Dynatrace мог корректно принимать метрики.

### Включение сбора метрик (обязательно)

Задайте `metrics.dynatrace.com/scrape: true`, чтобы Dynatrace мог собирать метрики Prometheus, предоставляемые этим подом.

### Порт метрик (обязательно)

По умолчанию метрики Prometheus доступны на первом открытом TCP-порту пода. Задайте `metrics.dynatrace.com/port` равным соответствующему порту.

Для определения значения порта см. раздел [Default port allocations](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) со списком распространённых портов для известных экспортёров.

### Путь к конечной точке метрик (необязательно)

Используйте `metrics.dynatrace.com/path` для переопределения конечной точки Prometheus по умолчанию (`/metrics`).

### HTTP/HTTPS (необязательно)

Задайте `metrics.dynatrace.com/secure: true`, если нужно собирать метрики, предоставляемые экспортёром через HTTPS. Значение по умолчанию — `false`, так как большинство экспортёров предоставляют метрики через HTTP.

Чтобы пропустить проверку TLS-сертификата (например, при использовании самоподписанных сертификатов), можно задать аннотацию `metrics.dynatrace.com/insecure_skip_verify: true`. Однако эта аннотация учитывается только при использовании ActiveGate, развёрнутого внутри отслеживаемого кластера, и настройках подключения Kubernetes, сконфигурированных для мониторинга локальной конечной точки Kubernetes API.

### Фильтрация метрик (необязательно)

Используйте `metrics.dynatrace.com/filter` для определения фильтра, позволяющего включать (`"mode": "include"`) или исключать (`"mode": "exclude"`) список метрик. Если аннотация фильтра не задана, собираются все метрики.
Синтаксис фильтра поддерживает символ звёздочки (`*`). Этот символ позволяет фильтровать ключи метрик, начинающиеся, заканчивающиеся или содержащие определённую последовательность, например:

* `redis_db*` фильтрует все метрики, начинающиеся с `redis_db`
* `*insights*` фильтрует все метрики, содержащие `insights`
* `*bytes` фильтрует все метрики, заканчивающиеся на `bytes`

Использование символа `*` внутри фильтра, например `redis_*_bytes`, не поддерживается.

Фильтр применяется к исходному ключу метрики, поэтому важно учитывать, что Dynatrace автоматически добавляет суффиксы к некоторым ключам метрик в зависимости от исходного ключа и типа метрики.
Подробнее см. в разделе [Payload](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Для summary и histogram фильтр применяется ко всему семейству метрик, указанному в строке `#TYPE` формата OpenMetrics.
Например, если семейство метрик summary `foo_seconds` отфильтровано, все точки данных метрик, включая `foo_seconds_count` и `foo_seconds_sum`, также фильтруются.
Напротив, если в качестве фильтра задан `foo_seconds_count`, ничего не фильтруется, поскольку такого семейства метрик не существует.

Следующий пример показывает, как использовать синтаксис фильтра в определении пода с аннотациями:

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/filter: |



{



"mode": "include",



"names": [



"redis_db_keys",



"*insights*",



"*bytes"



]



}



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Значения `metrics.dynatrace.com/path`, `metrics.dynatrace.com/port` и `metrics.dynatrace.com/secure` зависят от используемого экспортёра; адаптируйте их под ваши требования. Для определения значения порта см. раздел [Default port allocations](https://github.com/prometheus/prometheus/wiki/Default-port-allocations).

### Аутентификация клиента (необязательно)

**Требования:** добавьте разрешения на доступ к `secrets` и `configmaps` для ClusterRole `dynatrace-kubernetes-monitoring`.

Некоторые системы требуют дополнительной аутентификации перед тем, как Dynatrace сможет собирать с них данные. Для таких случаев можно задать следующие дополнительные аннотации:

* `metrics.dynatrace.com/tls.ca.crt`
* `metrics.dynatrace.com/tls.crt`
* `metrics.dynatrace.com/tls.key`

Необходимые сертификаты/ключи автоматически загружаются из `secret`/`configmaps`, указанных в значении аннотации.
Схема значений аннотаций: `<configmap|secret>:<namespace>:<resource_name>:<field_name_in_data_section>`.

Например, аннотации могут выглядеть следующим образом:

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/tls.ca.crt: 'configmap:kubernetes-config:etcd-metric-serving-ca:ca-bundle.crt'



metrics.dynatrace.com/tls.crt: 'secret:kubernetes-config:etcd-metric-client:tls.crt'



metrics.dynatrace.com/tls.key: 'secret:kubernetes-config:etcd-metric-client:tls.key'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Приём метрик от экспортёров, требующих аутентификации клиента, возможен только при использовании ActiveGate, развёрнутого внутри отслеживаемого кластера, и настройках подключения Kubernetes, сконфигурированных для мониторинга локальной конечной точки Kubernetes API.

### HTTP — базовая аутентификация (необязательно)

**Требования:** добавьте разрешения на доступ к `secrets` для ClusterRole `dynatrace-kubernetes-monitoring`.

Для систем, требующих базовой HTTP-аутентификации перед сбором данных, можно применить следующие дополнительные аннотации:

* `metrics.dynatrace.com/http.auth.basic.username`
* `metrics.dynatrace.com/http.auth.basic.password`

Следующий пример показывает два секрета, созданных в пространстве имён `default` — один для имени пользователя и один для пароля.
Упомянутые аннотации затем применяются к поду со ссылками на секреты в значениях аннотаций.

```
apiVersion: v1



kind: Secret



metadata:



name: user-secret



data:



username: bXktdXNlcm5hbWUtc2VjcmV0



---



apiVersion: v1



kind: Secret



metadata:



name: password-secret



data:



password: bXktcGFzc3dvcmQtc2VjcmV0
```

Значения секретов применяются «как есть» после декодирования из значений в кодировке base64. Распространённая ошибка — непреднамеренное добавление символа новой строки в конец значения, например, при использовании `echo <secret> | base64` вместо `echo -n <secret> | base64` для создания значения секрета.

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/http.auth.basic.username: 'secret:default:user-secret:username'



metrics.dynatrace.com/http.auth.basic.password: 'secret:default:password-secret:password'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Приём метрик от экспортёров, требующих базовой HTTP-аутентификации, возможен только при использовании ActiveGate, развёрнутого внутри отслеживаемого кластера, и настройках подключения Kubernetes, сконфигурированных для мониторинга локальной конечной точки Kubernetes API.

### HTTP — аутентификация Bearer token (необязательно)

**Требования:**

* ActiveGate version 1.317+
* Добавьте разрешения на доступ к `secrets` для ClusterRole `dynatrace-kubernetes-monitoring`.

Для систем, требующих аутентификации Bearer token перед сбором данных, можно применить дополнительную аннотацию `metrics.dynatrace.com/http.auth`.

Следующий пример показывает секрет `token-secret`, созданный в пространстве имён `default`. Необходимый Bearer token хранится под ключом `bearer`.

```
apiVersion: v1



kind: Secret



metadata:



name: token-secret



data:



bearer: bXktYmVhcmVyLXRva2Vu
```

Затем аннотация применяется к поду со ссылкой на секрет в значении аннотации.

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/http.auth: 'secret:default:token-secret:bearer'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Приём метрик от экспортёров, требующих аутентификации Bearer token, возможен только при использовании ActiveGate, развёрнутого внутри отслеживаемого кластера, и настройках подключения Kubernetes, сконфигурированных для мониторинга локальной конечной точки Kubernetes API.

### Авторизация RBAC для приёма метрик

Поды экспортёров, такие как `node-exporter`, `kube-state-metrics` и `openshift-state-metrics`, требуют [авторизации RBAC](https://dt-url.net/n721pt6). Для таких подов добавьте аннотацию:

`metrics.dynatrace.com/http.auth: 'builtin:default'`

Эта аннотация применяет токен из учётной записи сервиса `dynatrace-activegate` в качестве заголовка авторизации для запросов к экспортёру.

Приём метрик от экспортёров, требующих авторизации RBAC, возможен только при использовании ActiveGate, развёрнутого внутри отслеживаемого кластера, и настройках подключения Kubernetes, сконфигурированных для мониторинга локальной конечной точки Kubernetes API.

Подробнее о рекомендациях по аннотированию подов см. в разделе [Рекомендации по аннотированию](#best).

## Аннотирование сервисов Kubernetes

**Требования:** добавьте разрешение на доступ к **services** для ClusterRole `dynatrace-kubernetes-monitoring` (для пользователей Dynatrace Operator не требуется — включено по умолчанию в [clusterrole-kubernetes-monitoring.yaml](https://dt-url.net/gl027s4)).

Вместо подов можно аннотировать сервисы. Поды, соответствующие сервисам Kubernetes, обнаруживаются автоматически через селектор меток сервиса — сбор данных будет выполняться для всех подов, принадлежащих сервису.

* Сервис и соответствующие ему поды должны находиться в одном пространстве имён.
* Аннотация `metrics.dynatrace.com/port` должна указывать целевой порт контейнера пода внутри сервиса, а не собственный порт сервиса, поскольку сервис не используется как прокси в процессе сбора данных.

Подробнее о рекомендациях по аннотированию сервисов см. в разделе [Рекомендации по аннотированию](#best).

## Рекомендации по аннотированию

Существует несколько способов размещения аннотаций на подах или сервисах. Выберите подход, наиболее подходящий для вашего сценария.

### Рекомендуется при полном контроле

Если у вас есть полный контроль над шаблоном пода или определением сервиса, рекомендуется добавлять аннотации путём редактирования этих файлов. Это наиболее надёжный способ обеспечить постоянство аннотаций. Рекомендуется редактировать шаблон пода, а не определение сервиса, поскольку это требует меньше прав (например, если у вас нет доступа к сервисам).
**Достоинство:** аннотации постоянны и не требуют повторного создания при удалении пода.

### Варианты при отсутствии полного контроля

Если у вас нет полного контроля над шаблоном пода, доступны следующие варианты:

* Аннотирование существующего сервиса (в YAML)
  **Требования:** наличие контроля над существующим YAML и прав на редактирование существующего объекта сервиса Kubernetes.
  **Достоинство:** аннотации постоянны.
  **Пример:**

  ```
  kind: Service



  apiVersion: v1



  metadata:



  name: dynatrace-monitoring-node-exporter



  namespace: kubernetes-monitoring



  annotations:



  metrics.dynatrace.com/port: '12071'



  metrics.dynatrace.com/scrape: 'true'



  metrics.dynatrace.com/secure: 'true'



  metrics.dynatrace.com/path: '/metrics'



  spec:



  ports:



  - name: dynatrace-monitoring-node-exporter-port



  port: 9100



  targetPort: 12071



  selector:



  app.kubernetes.io/name: node-exporter
  ```
* Создание нового сервиса (в YAML)
  **Требования:** новый сервис рекомендуется создавать с именем, начинающимся с префикса `dynatrace-monitoring-`. Сервис должен находиться в том же пространстве имён, что и поды, а также иметь права на создание объекта сервиса Kubernetes. Предпочтительно создавать безголовый сервис (`clusterIP: None`), поскольку это подчёркивает, что сервис не используется как прокси.

  **Достоинство:** вы сохраняете контроль над исходной нагрузкой/сервисом.
  **Недостаток:** требуется синхронизация селектора меток. Поддерживается только селектор меток.
  **Пример:**

  ```
  kind: Service



  apiVersion: v1



  metadata:



  name: dynatrace-monitoring-node-exporter



  namespace: kubernetes-monitoring



  annotations:



  metrics.dynatrace.com/port: '12071'



  metrics.dynatrace.com/scrape: 'true'



  metrics.dynatrace.com/secure: 'true'



  metrics.dynatrace.com/path: '/metrics'



  spec:



  ports:



  - name: dynatrace-monitoring-node-exporter-port



  port: 12071



  selector:



  app.kubernetes.io/name: node-exporter



  clusterIP: None
  ```
* Аннотирование существующего сервиса (через CLI)
  **Требования:** наличие прав на редактирование существующего объекта сервиса Kubernetes.
  **Достоинство:** синхронизация селектора меток не требуется.
  **Недостаток:** аннотации непостоянны — изменения перезапишут аннотации. Поддерживается только селектор меток.
* Аннотирование существующих подов (через CLI)
  **Требования:** отсутствуют.
  **Достоинство:** быстрая проверка приёма метрик.
  **Недостаток:** аннотации непостоянны — изменения перезапишут аннотации.

## Просмотр метрик на панели мониторинга

Метрики из экспортёров Prometheus доступны в Data Explorer для пользовательского построения диаграмм. Выберите **Create custom chart** и нажмите **Try it out** в верхнем баннере. Подробнее см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

Можно просто искать ключи метрик среди всех доступных метрик и определять способ анализа и построения диаграмм. После этого диаграммы можно закрепить на панели мониторинга.

## Оповещения по метрикам

На основе метрик Prometheus, собранных с экспортёров, также можно создавать пользовательские оповещения. Перейдите в **Settings** > **Anomaly detection** > **Metric events** и нажмите **Add metric event**. На странице **Add metric event** выполните поиск метрики Prometheus по её ключу и определите оповещение. Подробнее см. в разделе [Metric events для оповещений](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Ограничения

Текущие ограничения интеграции метрик Prometheus:

### Несколько экспортёров в одном поде

В аннотациях можно указать только один порт и путь. Однако можно собирать данные с нескольких экспортёров в поде, [аннотируя дополнительные сервисы](#annotate-kubernetes-services), выбирающие тот же под.

Например, чтобы собирать данные с двух конечных точек в поде, можно аннотировать под и сервис, который его выбирает. Если такого сервиса нет, можно создать новый специально для этой цели.

Кроме того, можно аннотировать два разных сервиса, выбирающих один и тот же под. Подробнее см. в разделе [Рекомендации по аннотированию](#best).

### Количество подов, метрик и точек данных метрик

На один кластер Kubernetes данная интеграция поддерживает не более:

* 1000 подов экспортёров
* 1000 метрик на под
* 500 000 точек данных метрик на под

  Несмотря на то что более крупные наборы данных допустимы, они могут приводить к пробелам при приёме, поскольку Dynatrace собирает все метрики каждую минуту перед их отправкой в кластер.

### Методы мониторинга

Существует два отдельных метода мониторинга технологий:

* Первый метод использует фреймворк [Extensions 2.0](https://dt-url.net/9t036yh), который поддерживает несколько расширений для экспортёров Prometheus «из коробки».

  Этот метод предоставляет комплексные функции мониторинга, включая технологически-специфические панели мониторинга, возможности оповещений, визуализацию топологии и страницы сущностей. Однако этот метод работает за пределами Kubernetes.
* Второй метод предполагает аннотирование подов Prometheus внутри Kubernetes для сбора данных с экспортёров.

  Хотя этот метод обеспечивает более нативный для Kubernetes подход, он в настоящее время имеет минимальное функциональное пересечение с функциями, предоставляемыми фреймворком Extensions 2.0.

Эти два метода обслуживают разные контексты, работают независимо друг от друга и не используют общие метрики.

## Потребление лицензии

При использовании лицензирования DPS дополнительную информацию о потреблении пользовательских метрик в вашей среде можно получить в [документации по лицензированию](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

* Мониторинг Full-Stack [включает фиксированное количество точек данных пользовательских метрик](/managed/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-metrics "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") для каждого GiB, учитываемого в потреблении GiB-часов для контейнеров с кодовыми модулями.

При использовании классического лицензирования Dynatrace метрики Prometheus в средах Kubernetes подлежат [потреблению DDU](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

* Метрики Prometheus из экспортёров, работающих на хостах под управлением OneAgent, сначала вычитаются из квоты [включённых метрик на единицу хоста](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). После превышения квоты дополнительные метрики потребляют [DDU](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").
* Метрики Prometheus из экспортёров, работающих на хостах без OneAgent, всегда потребляют [DDU](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Устранение неполадок

Для устранения проблем с интеграцией Prometheus скачайте [расширение Kubernetes Monitoring Statistics](https://dt-url.net/n903xmb). Подробнее см. в статье сообщества [How to troubleshoot missing Prometheus metrics](https://dt-url.net/3m02ozr).

## Связанные темы

* [Метрики](/managed/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")
* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")