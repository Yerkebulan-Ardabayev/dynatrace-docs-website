---
title: Мониторинг метрик Prometheus
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics
scraped: 2026-03-06T21:21:44.712888
---

Prometheus — это набор инструментов мониторинга и оповещения с открытым исходным кодом, широко используемый в сообществе Kubernetes. Prometheus собирает метрики из ряда конечных точек HTTP(S), предоставляющих метрики в формате OpenMetrics.
См. список доступных [экспортёров](https://dt-url.net/vd03n1m) в документации Prometheus.

## Типы метрик Prometheus при приёме данных

Dynatrace поддерживает приём метрик Prometheus типов [Counter](#counter), [Gauge](#gauge), [Histogram](#histogram) и [Summary](#summary)
в Kubernetes с помощью [экспортёров Prometheus](https://dt-url.net/lw02ror) и делает их доступными для построения графиков, оповещения и анализа.

### Counter

Метрика Prometheus типа Counter[1](#fn-1-1-def) — это монотонно возрастающее значение, обычно используемое для измерений, которые могут только увеличиваться или оставаться постоянными.
Dynatrace использует тип метрики [`COUNT`](../../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works."), который применяет **дельта-кодирование**[2](#fn-1-2-def) для снижения избыточности данных при приёме.
Таким образом, значение, отображаемое в Dynatrace, отражает не фактическое значение счётчика, а его изменение (дельту) между наблюдениями.

Этот метод приводит к тому, что метрика типа Counter появляется с задержкой в одну минуту по сравнению с метрикой типа [Gauge](#gauge), если сбор данных для обоих типов начался одновременно.
Подробнее см. в разделе [справочника по протоколу приёма метрик](../../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Приём метрик типа Counter

**Дельта-кодирование**, используемое типом приёма Dynatrace [`COUNT`](../../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works."), означает, что принятое значение *не* отражает фактическое значение, а является разностью между измерениями.

1

[Официальная документация Prometheus: Counter](https://dt-url.net/cd02rce)

2

Дельта-кодирование, также известное как дельта-сжатие, хранит данные, вычисляя разность между двумя наблюдениями или целевыми значениями. Этот метод, применяемый преимущественно для редко изменяющихся данных, позволяет избежать избыточности данных.

### Gauge

В отличие от [Counter](#counter), метрика типа Gauge[1](#fn-2-1-def) хранит одно числовое значение, которое может увеличиваться и уменьшаться. Обычно используется для измеренных значений, таких как текущее использование памяти или количество пользователей онлайн. В Dynatrace для приёма данных используется тип метрики [`GAUGE`](../../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

1

[Официальная документация Prometheus: Gauge](https://dt-url.net/lb22r1o)

### Histogram

Гистограммы[1](#fn-3-1-def) предоставляют наглядное представление о распределении и частоте числовых данных.
Для базового имени метрики `<basename>` Dynatrace принимает данные в соответствии со следующей таблицей.

Дополнительная гибкость и управление обеспечиваются через схему настроек [`builtin:histogram-metrics`](https://dt-url.net/ne02rlq).
Эта схема позволяет настраивать приём метрик `<basename>_bucket{le="<upper inclusive bound>"}`.

1

[Официальная документация Prometheus: Histogram](https://dt-url.net/vc02rmb)

### Summary

Как и [Histogram](#histogram), метрика типа Summary[1](#fn-4-1-def) выполняет выборку наблюдений. В отличие от гистограммы, сегменты summary представлены φ-квантилями, где 0 ≤ φ ≤ 1. Для базового имени метрики `<basename>` Dynatrace принимает данные в соответствии со следующей таблицей.

1

[Официальная документация Prometheus: Summary](https://dt-url.net/7g234n1).

### Неподдерживаемые типы

Следующие типы в настоящее время не поддерживаются Dynatrace:

* метрики типа info, gaugehistogram или stateset
* exemplars

## Предварительные требования

Мы рекомендуем использовать ActiveGate, работающий внутри кластера Kubernetes, из которого вы хотите собирать метрики Prometheus. Если ActiveGate работает за пределами отслеживаемого кластера (например, на виртуальной машине или в другом кластере Kubernetes), он не сможет собирать данные с конечных точек Prometheus на подах, требующих аутентификации (таких как [RBAC](#rbac) или [клиентская аутентификация](#client)). ActiveGate, работающие внутри кластеров, также обеспечивают улучшение производительности.

* В Dynatrace перейдите на страницу настроек мониторинга вашего кластера Kubernetes и включите

  + **Monitor Kubernetes namespaces, services, workloads, and pods**
  + **Monitor annotated Prometheus exporters**
* Аннотированные определения подов. Подробнее см. ниже.
* Убедитесь, что ваши сетевые политики позволяют ActiveGate подключаться к экспортёрам.

  Например, если вы развернули ActiveGate в своём кластере Kubernetes с помощью Dynatrace Operator и у вас есть аннотированные экспортёры Prometheus в пространстве имён `online-boutique`, а также определена сетевая политика для этого пространства имён, необходимо убедиться, что под ActiveGate, расположенный в пространстве имён `dynatrace`, может подключаться к аннотированным экспортёрам Prometheus в пространстве имён `online-boutique`.

## Аннотирование подов с экспортёрами Prometheus

Dynatrace собирает метрики из любых подов, аннотированных свойством `metrics.dynatrace.com/scrape`, установленным в `true` в определении пода. Эта функция применяется ко всем подам в кластере Kubernetes независимо от того, находится ли под в пространстве имён, соответствующем селектору пространства имён Dynakube.

В зависимости от конкретного экспортёра в поде вам может потребоваться добавить дополнительные аннотации к определению пода, чтобы Dynatrace мог правильно принимать эти метрики.

### Включение сбора метрик Обязательно

Установите `metrics.dynatrace.com/scrape` в `true`, чтобы включить сбор метрик Prometheus, предоставляемых для этого пода Dynatrace.

### Порт метрик Обязательно

По умолчанию метрики Prometheus доступны на первом открытом TCP-порту пода. Установите `metrics.dynatrace.com/port` на соответствующий порт.

Для определения значения порта см. [Default port allocations](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) — список общих портов для известных экспортёров.

### Путь к конечной точке метрик Необязательно

Используйте `metrics.dynatrace.com/path` для переопределения конечной точки Prometheus по умолчанию (`/metrics`).

### HTTP/HTTPS Необязательно

Установите `metrics.dynatrace.com/secure` в `true`, если хотите собирать метрики, предоставляемые экспортёром через HTTPS. Значение по умолчанию — `false`, поскольку большинство экспортёров предоставляют свои метрики через HTTP.

Если вы хотите пропустить проверку TLS-сертификата (например, при использовании самоподписанных сертификатов), можно установить аннотацию `metrics.dynatrace.com/insecure_skip_verify` в `true`. Однако эта аннотация учитывается только при использовании ActiveGate, развёрнутого внутри отслеживаемого кластера, и настроек подключения Kubernetes, настроенных для мониторинга локальной конечной точки Kubernetes API.

### Фильтрация метрик Необязательно

Используйте `metrics.dynatrace.com/filter` для определения фильтра, позволяющего включать (`"mode": "include"`) или исключать (`"mode": "exclude"`) список метрик. Если аннотация фильтра не задана, собираются все метрики.
Синтаксис фильтра также поддерживает символ звёздочки (`*`). Этот символ позволяет фильтровать ключи метрик, начинающиеся, заканчивающиеся или содержащие определённую последовательность, например:

* `redis_db*` фильтрует все метрики, начинающиеся с `redis_db`
* `*insights*` фильтрует все метрики, содержащие `insights`
* `*bytes` фильтрует все метрики, заканчивающиеся на `bytes`

Использование символа `*` внутри фильтра, например `redis_*_bytes`, не поддерживается.

Фильтр применяется к исходному ключу метрики, поэтому важно знать, что Dynatrace автоматически добавляет суффиксы к некоторым ключам метрик в зависимости от исходного ключа метрики и её типа.
Подробнее см. в разделе [Payload](../../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Для типов summary и histogram фильтр применяется ко всему семейству метрик, как указано в строке `#TYPE` формата OpenMetrics.
Например, если семейство метрик типа summary `foo_seconds` отфильтровано, все точки метрик, включая `foo_seconds_count` и `foo_seconds_sum`, также фильтруются.
И наоборот, если `foo_seconds_count` указан как фильтр, ничего не фильтруется, поскольку такого семейства метрик не существует.

Следующий пример показывает использование синтаксиса фильтра в определении пода с аннотациями:

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

Значения `metrics.dynatrace.com/path`, `metrics.dynatrace.com/port` и `metrics.dynatrace.com/secure` зависят от используемого экспортёра; адаптируйте их под свои требования. Для определения значения порта см. [Default port allocations](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) — список общих портов для известных экспортёров.

### Клиентская аутентификация Необязательно

**Требования:** Добавьте разрешения на доступ к `secrets` и `configmaps` для `dynatrace-kubernetes-monitoring` ClusterRole.

Некоторые системы требуют дополнительной аутентификации перед тем, как Dynatrace сможет собирать с них данные. Для таких случаев можно установить следующие дополнительные аннотации:

* `metrics.dynatrace.com/tls.ca.crt`
* `metrics.dynatrace.com/tls.crt`
* `metrics.dynatrace.com/tls.key`

Необходимые сертификаты/ключи автоматически загружаются из `secret`/`configmaps`, указанных в значении аннотации.
Схема для значений аннотаций: `<configmap|secret>:<namespace>:<resource_name>:<field_name_in_data_section>`.

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

Приём метрик из экспортёров, требующих клиентской аутентификации, возможен только с ActiveGate, развёрнутым внутри отслеживаемого кластера, и настройками подключения Kubernetes, настроенными для мониторинга локальной конечной точки Kubernetes API.

### HTTP — Базовая аутентификация Необязательно

**Требования:** Добавьте разрешения на доступ к `secrets` для `dynatrace-kubernetes-monitoring` ClusterRole.

Для систем, требующих базовой HTTP-аутентификации перед сбором данных, можно применить следующие дополнительные аннотации.

* `metrics.dynatrace.com/http.auth.basic.username`
* `metrics.dynatrace.com/http.auth.basic.password`

Следующий пример показывает два секрета, созданных в пространстве имён `default` — один для имени пользователя и один для пароля.
Упомянутые аннотации затем используются на поде со ссылками на секреты в значениях аннотаций.

```
apiVersion: v1


kind: Secret


metadata:


name: user-secret


data:


username: bXktdXNlcm5hbWUtc2VjcmV0Cg==


---


apiVersion: v1


kind: Secret


metadata:


name: password-secret


data:


password: bXktcGFzc3dvcmQtc2VjcmV0Cg==
```

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

Приём метрик из экспортёров, требующих базовой HTTP-аутентификации, возможен только с ActiveGate, развёрнутым внутри отслеживаемого кластера, и настройками подключения Kubernetes, настроенными для мониторинга локальной конечной точки Kubernetes API.

### HTTP — Аутентификация с помощью токена Bearer Необязательно

**Требования:**

* ActiveGate версии 1.317+
* Добавьте разрешения на доступ к `secrets` для `dynatrace-kubernetes-monitoring` ClusterRole.

Для систем, требующих аутентификации с помощью токена Bearer перед сбором данных, можно применить дополнительную аннотацию `metrics.dynatrace.com/http.auth`.

Следующий пример показывает секрет с именем `token-secret`, созданный в пространстве имён `default`. Необходимый токен Bearer хранится под ключом `bearer`.

```
apiVersion: v1


kind: Secret


metadata:


name: token-secret


data:


bearer: bXktYmVhcmVyLXRva2VuCg==
```

Аннотация затем используется на поде со ссылкой на секрет в значении аннотации.

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

Приём метрик из экспортёров, требующих аутентификации с помощью токена Bearer, возможен только с ActiveGate, развёрнутым внутри отслеживаемого кластера, и настройками подключения Kubernetes, настроенными для мониторинга локальной конечной точки Kubernetes API.

### Авторизация на основе ролей (RBAC) для приёма метрик

Поды экспортёров, такие как `node-exporter`, `kube-state-metrics` и `openshift-state-metrics`, требуют [авторизации RBAC](https://dt-url.net/n721pt6). Для этих подов добавьте аннотацию:

`metrics.dynatrace.com/http.auth: 'builtin:default'`

Эта аннотация применяет токен из сервисного аккаунта `dynatrace-activegate` в качестве заголовка авторизации для запросов к экспортёру.

Приём метрик из экспортёров, требующих авторизации RBAC, возможен только с ActiveGate, развёрнутым внутри отслеживаемого кластера, и настройками подключения Kubernetes, настроенными для мониторинга локальной конечной точки Kubernetes API.

Для получения дополнительной информации об аннотировании подов см. [Рекомендации по аннотациям](#best).

## Аннотирование сервисов Kubernetes

**Требования:** Добавьте разрешение на доступ к **services** для `dynatrace-kubernetes-monitoring` ClusterRole (не требуется для пользователей Dynatrace Operator, поскольку это включено по умолчанию в [clusterrole-kubernetes-monitoring.yaml](https://dt-url.net/gl027s4)).

Вместо подов можно также аннотировать сервисы. Поды, соответствующие сервисам Kubernetes, автоматически обнаруживаются через селектор меток сервиса, что приводит к сбору данных со всех подов, принадлежащих этому сервису.

* Сервис и соответствующие ему поды должны находиться в одном пространстве имён.
* Аннотация `metrics.dynatrace.com/port` должна указывать целевой порт контейнерного пода внутри сервиса, а не собственный порт сервиса, поскольку сервис не используется для проксирования процесса сбора данных.

Для получения дополнительной информации об аннотировании сервисов см. [Рекомендации по аннотациям](#best).

## Рекомендации по аннотациям

Существует несколько способов размещения аннотаций на подах или сервисах. Изучите информацию ниже, чтобы определить, какой подход лучше всего подходит для вашего сценария.

### Рекомендуется при наличии полного контроля

Если у вас полный контроль над шаблоном пода или определением сервиса, рекомендуется добавлять аннотации путём редактирования этих файлов. Это наиболее надёжный способ обеспечить сохранность аннотаций. Мы рекомендуем редактировать шаблон пода, а не определение сервиса, поскольку это требует меньше прав (например, если у вас нет доступа к сервисам).
**Преимущество:** Аннотации постоянны и не требуют повторного создания при удалении пода.

### Варианты при отсутствии полного контроля

Если у вас нет полного контроля над шаблоном пода, доступны следующие варианты:

* Аннотирование существующего сервиса (в YAML)
  **Требования:** Наличие контроля над существующим YAML и прав на редактирование существующего объекта сервиса Kubernetes.
  **Преимущество:** Аннотации постоянны.
  **Недостатки:** Отсутствуют.
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
  **Требования**: Новый сервис должен быть создан с именем, предпочтительно начинающимся с префикса `dynatrace-monitoring-`. Этот сервис должен находиться в том же пространстве имён, что и поды, а также потребуется разрешение на создание объекта сервиса Kubernetes. Желательно сделать сервис headless (`clusterIP` установлен в `None`), поскольку это подчёркивает, что сервис не используется для проксирования.

  **Преимущество:** У вас есть контроль над исходной рабочей нагрузкой/сервисом.
  **Недостаток:** Требуется синхронизация селектора меток. Поддерживается только селектор меток.
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
  **Требования:** Наличие прав на редактирование существующего объекта сервиса Kubernetes.
  **Преимущество:** Синхронизация селектора меток не требуется.
  **Недостаток:** Аннотации не постоянны, изменения перезапишут аннотации. Поддерживается только селектор меток.
* Аннотирование существующих подов (через CLI)
  **Требования:** Отсутствуют.
  **Преимущество:** Можно быстро протестировать приём метрик.
  **Недостаток:** Аннотации не постоянны, изменения перезапишут аннотации.

## Просмотр метрик на дашборде

Метрики из экспортёров Prometheus доступны в Data Explorer для создания пользовательских графиков. Выберите **Create custom chart** и нажмите **Try it out** в верхнем баннере. Подробнее см. в разделе Data Explorer.

Вы можете просто искать ключи метрик всех доступных метрик и определять способы анализа и построения графиков. После этого можно закрепить графики на дашборде.

## Оповещения на основе метрик

Вы также можете создавать пользовательские оповещения на основе метрик, собираемых Prometheus. Перейдите в **Settings** > **Anomaly detection** > **Metric events** и выберите **Add metric event**. На странице **Add metric event** найдите метрику Prometheus по её ключу и настройте оповещение. Подробнее см. в разделе Metric events for alerting.

## Ограничения

Текущие ограничения интеграции метрик Prometheus следующие:

### Несколько экспортёров в поде

В аннотациях можно указать только один порт и один путь. Однако сбор данных с нескольких экспортёров в поде возможен путём [аннотирования дополнительных сервисов](#annotate-kubernetes-services), которые выбирают тот же под.

Например, если вы хотите собирать данные с двух конечных точек в поде, можно аннотировать под и сервис, выбирающий этот под. Если такой сервис не существует, можно создать новый сервис специально для этой цели.

Также можно аннотировать два разных сервиса, выбирающих один и тот же под. Подробнее см. в разделе [Рекомендации по аннотациям](#best).

### Количество подов, метрик и точек данных метрик

Для каждого кластера Kubernetes эта интеграция поддерживает максимум:

* 1 000 подов с экспортёрами
* 1 000 метрик на под
* 500 000 точек данных метрик на под

  Хотя допускаются более крупные наборы данных, они могут приводить к пробелам в приёме, поскольку Dynatrace собирает все метрики каждую минуту перед их отправкой в кластер.

### Методы мониторинга

Существует два различных метода мониторинга технологий:

* Первый метод предполагает использование фреймворка [Extensions 2.0](https://dt-url.net/9t036yh), который поддерживает ряд расширений для экспортёров Prometheus из коробки.

  Этот метод предоставляет комплексные функции мониторинга, включая технологически-специфичные дашборды, возможности оповещения, визуализацию топологии и страницы сущностей. Однако этот метод работает вне Kubernetes.
* Второй метод предполагает аннотирование подов Prometheus в Kubernetes для сбора данных с экспортёров Prometheus.

  Хотя этот метод обеспечивает более нативный для Kubernetes подход, в настоящее время он имеет минимальное функциональное пересечение с возможностями фреймворка Extensions 2.0.

Эти два метода служат разным контекстам, работают независимо друг от друга и не используют одни и те же метрики.

## Потребление при мониторинге

Если у вас лицензирование DPS, вы можете получить дополнительную информацию о потреблении пользовательских метрик в вашей среде из нашей документации по лицензированию.

* Full-Stack Monitoring [включает фиксированное количество точек данных пользовательских метрик](../../../../license/capabilities/app-infra-observability/full-stack-monitoring.md#full-stack-metrics "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") для каждого ГиБ, учитываемого в потреблении ГиБ-часов вашей среды для контейнеров с кодовыми модулями.

Если у вас классическое лицензирование Dynatrace, метрики Prometheus в средах Kubernetes подпадают под потребление DDU.

* Метрики Prometheus из экспортёров, работающих на хостах, отслеживаемых OneAgent, сначала вычитаются из квоты включённых метрик на единицу хоста. После превышения этой квоты любые дополнительные метрики потребляют DDU.
* Метрики Prometheus из экспортёров, работающих на хостах, не отслеживаемых OneAgent, всегда потребляют DDU.

## Устранение неполадок

Для устранения проблем с интеграцией Prometheus загрузите [расширение Kubernetes Monitoring Statistics](https://dt-url.net/n903xmb). Подробнее см. в статье сообщества [Как устранить проблемы с отсутствующими метриками Prometheus](https://dt-url.net/3m02ozr).

## Связанные темы

* Metrics Classic
* Настройка Dynatrace в Kubernetes
