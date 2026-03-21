---
title: Развертывание Dynatrace совместно с Istio
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment
scraped: 2026-03-06T21:18:03.469401
---

# Развёртывание Dynatrace совместно с Istio


* Актуальная версия Dynatrace

Это руководство объясняет, как компоненты Dynatrace могут быть развёрнуты совместно с Istio. Развёртывание Dynatrace в Kubernetes включает несколько компонентов, которым необходимо взаимодействовать друг с другом, с кластером Dynatrace и другими внешними ресурсами.

Для получения дополнительной информации о сетевом взаимодействии Dynatrace Operator и его управляемых компонентов см. справочную страницу [сетевой трафик](../../reference/network.md "Требования к сетевому трафику для компонентов Dynatrace Operator в кластере Kubernetes.").

## Ограничения

* Инъекция Istio в пространство имён Dynatrace Operator не поддерживается.
* Производные Istio в настоящее время не поддерживаются (например, Maistra или OpenShift Service Mesh).
* Развёртывание Istio East-West (sidecar в сочетании с ambient) не поддерживается.

## Аспекты настройки

Это руководство охватывает две предопределённые конфигурации Istio, выбранные за их простоту и распространённые сценарии использования. Хотя Istio предлагает обширные возможности настройки, эти конфигурации служат отправной точкой. В этом разделе объясняются сценарии конфигурации и даются рекомендации по выбору настройки Dynatrace, которая лучше всего соответствует вашим потребностям. Обратите внимание, что Dynatrace не накладывает ограничений на способ настройки Istio.

* **Конфигурация Istio по умолчанию** Рекомендуется
  Это представляет развёртывание Istio по умолчанию, то есть без специальной конфигурации mesh. По сути, это результат следования официальному [руководству по установке Istio](https://dt-url.net/hm03u3r).
  Это означает, что Istio установлен через Helm или `istioctl` в режиме sidecar с CNI node agent.

  Следуйте [руководству по настройке для конфигурации Istio по умолчанию](#setup-guide-for-default-istio-configuration), если Istio развёрнут соответствующим образом.
* **Безопасная конфигурация Istio**
  Это представляет «безопасную» конфигурацию Istio. Однако это не означает, что мы считаем её лучшей практикой для настройки безопасности в Istio или что это должно рассматриваться как руководство по обеспечению безопасности Istio. Эта настройка основана на параметрах, которые с наибольшей вероятностью повлияют на развёрнутые компоненты Dynatrace и их соединения. Этот сценарий предполагает, что Istio развёрнут со строгим mTLS и `outboundTrafficPolicy`, установленным в `REGISTRY_ONLY`. Эти параметры существенно ограничивают входящие и исходящие соединения для рабочих нагрузок в mesh.

  Выберите эту конфигурацию, если применимо любое из следующих условий:

  + Вы включили mTLS в строгом режиме.
  + У вас `outboundTrafficPolicy` установлен в `REGISTRY_ONLY`.

  Если ни одно из вышеперечисленных условий не применимо, выберите [конфигурацию Istio по умолчанию](#setup-guide-for-default-istio-configuration).
  Следуйте [руководству по настройке для безопасной конфигурации Istio](#setup-guide-for-secure-istio-configuration), если Istio развёрнут соответствующим образом.

### Другие аспекты развёртывания

Отключение инъекции CNI-подов

#### Отключение инъекции CNI-подов

Это актуально для вас, если все следующие условия применимы к вашему развёртыванию:

* Не поддерживается Dynatrace Operator развёрнут внутри mesh.
* Istio развёрнут с использованием sidecar-контейнеров.
* Istio настроен на использование компонента CNI.
* Вы не настроили селектор пространства имён в DynaKube, который исключал бы пространство имён `istio-system`.

Во всех сценариях следует исключить CNI-поды Istio из инъекции Dynatrace Operator. В противном случае при добавлении нового узла в кластер может возникнуть ситуация взаимной блокировки.

CSI-драйвер и CNI-агент Istio являются DaemonSet-ами и поэтому будут развёрнуты на каждом (новом) узле кластера.

* Под CSI-драйвера будет инъецирован Istio с init-контейнером, который ожидает правильной настройки правил перенаправления, необходимых для работы прокси-sidecar.
* CNI-под будет инъецирован Dynatrace для включения необходимых бинарных файлов OneAgent для инструментации, которые предоставляются через том, обеспеченный CSI-драйвером на данном узле.

Это приводит к ситуации, когда оба пода не могут запуститься:

* CNI-под ожидает готовности CSI-драйвера для предоставления тома.
* CSI-под ожидает, когда CNI-агент предоставит перенаправления для прокси.

Также все другие рабочие нагрузки, являющиеся целью инъекции Istio или Dynatrace и запланированные на этом узле, будут затронуты и не смогут запуститься.

Самый простой способ исключить CNI-поды из инъекции Dynatrace Operator — добавить аннотацию `oneagent.dynatrace.com/inject: "false"`. Например, для развёртывания Istio через Helm добавьте следующее в значения чарта `cni`:

```
cni:


podAnnotations:


oneagent.dynatrace.com/inject: "false"
```

Поддержка нативных sidecar-контейнеров

#### Поддержка нативных sidecar-контейнеров

Istio 1.28, развёрнутый на совместимом кластере Kubernetes (>=1.29), будет использовать нативные sidecar-контейнеры. Этот новый тип sidecar-контейнеров в настоящее время не поддерживается Dynatrace Operator. Отключите нативные sidecar-контейнеры в развёртывании Istio, добавив следующую переменную окружения к развёртыванию pilot.

Пример значений для Helm-чарта Istio:

```
pilot:


...


env:


ENABLE_NATIVE_SIDECARS: false


...
```

## Руководство по настройке для конфигурации Istio по умолчанию

Поскольку Dynatrace поддерживает Istio в конфигурации по умолчанию, вам нужно только включить параметр `enableIstio` в [DynaKube](../../reference/dynakube-parameters.md "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Однако устанавливать этот параметр не нужно, если вы не планируете использовать ограничительную `outboundTrafficPolicy`.

Когда этот параметр включён, Dynatrace Operator развернёт `ServiceEntries` и `VirtualServices` для обеспечения связи изнутри mesh со всеми необходимыми компонентами Dynatrace и окружением Dynatrace. `ServiceEntries` и `VirtualServices` работают независимо от того, является ли пространство имён Dynatrace Operator частью mesh (если в Istio не установлен `discoveryfilter`).

Это позволяет всем рабочим нагрузкам и OneAgent подключаться к экземпляру ActiveGate и выполнять все необходимые подключения к окружению Dynatrace. Поэтому ожидается, что все функции Dynatrace будут работать.

`ServiceEntries` приводят к дополнительным DNS-запросам, выполняемым каждым sidecar-прокси. Это может создать дополнительную нагрузку на ваш DNS-сервер.

Для минимизации количества URL-адресов и, соответственно, DNS-запросов убедитесь, что сетевые зоны в вашем окружении Dynatrace настроены правильно. Подробное описание настройки см. в [документации по сетевым зонам Kubernetes](../networking-security-compliance/network-configurations/network-zones.md#kubernetes-cluster-with-restricted-egress "Настройка и использование сетевых зон в окружениях Kubernetes с Dynatrace Operator.").

Если это невозможно или недостаточно в вашем окружении, см. [проксирование DNS Istio](https://dt-url.net/ab23uvy) для другого возможного решения.

### Как работает `enableIstio`

Атрибут `enableIstio` — это удобная функция, которая автоматически создаёт `ServiceEntries` и `VirtualServices` для конечных точек подключения, необходимых для:

* Dynatrace Operator: использует `apiUrl`, определённый в DynaKube.
* ActiveGate: использует конечную точку `/v1/deployment/installer/gateway/connectioninfo`.
* OneAgent, инъецированный в пользовательские контейнеры: использует `/v1/deployment/installer/agent/connectioninfo`, который учитывает атрибут `networkZone` для маршрутизации.

Обратите внимание, что атрибут `enableIstio` не учитывает ранее существующие `ServiceEntries` и `VirtualServices`. Преждевременное использование этого атрибута может привести к конфликтам в конфигурациях Istio. В сложных конфигурациях ручная настройка может дать лучшие результаты.

Изменения атрибута `enableIstio` требуют удаления и повторного применения DynaKube для вступления обновления в силу.

Ручная настройка

Ручная настройка `ServiceEntries` и `VirtualServices` может потребоваться в следующих случаях:

#### ActiveGate

* **Требование**: необходимо, если под ActiveGate является частью mesh.
* **Настройка**: вручную настройте `ServiceEntries` и `VirtualServices` на основе вывода конечной точки `/v1/deployment/installer/gateway/connectioninfo`.

#### `cloudNativeFullstack` и `applicationMonitoring`

* **Требование**: необходимо, если инъецированные пользовательские приложения являются частью mesh.
* **Настройка**: вручную настройте `ServiceEntries` и `VirtualServices` на основе вывода конечной точки `/v1/deployment/installer/agent/connectioninfo`.

## Руководство по настройке для безопасной конфигурации Istio

В таком ограниченном окружении, в зависимости от необходимых функций Dynatrace и других аспектов, может потребоваться создание нескольких дополнительных правил конфигурации для Istio. Есть несколько моментов, которые следует учитывать в отношении компонентов Dynatrace при принятии решения о развёртывании Dynatrace Operator.

* Даже если маршрутизация включена на ActiveGate, OneAgent будет использовать прямое подключение к окружению Dynatrace, если ActiveGate недоступен (например, потому что он находится внутри mesh). Это означает, что данные мониторинга не теряются, если некоторые OneAgent не могут подключиться к ActiveGate из-за выбранной стратегии развёртывания.
* Режимы мониторинга `classicFullStack` или `cloudNativeFullStack` создают поды с включённой сетью хоста. Это означает, что такие поды никогда не могут быть частью mesh, так как Istio не поддерживает поды с сетью хоста. Для `classicFullStack` эти поды обрабатывают все метрики приложений, тогда как для `cloudNativeFullStack` затрагивается только мониторинг хоста.
* Некоторые функции ActiveGate могут требовать прямых подключений к подам (например, сбор метрик). При включённом mTLS в Istio прямые подключения к IP-адресам подов невозможны. Обходное решение для сбора метрик см. в разделе [Сбор метрик с использованием слияния метрик Istio](#metric-scraping-using-istio-metric-merging).

### Развёртывание вне mesh

В этом сценарии наименее сложное развёртывание — вне mesh. Вам по-прежнему необходимо включить параметр `enableIstio` в DynaKube. Возможные недостатки этого развёртывания могут включать:

* Связь изнутри mesh к ActiveGate не будет защищена mTLS. Однако связь по-прежнему шифруется через HTTPS.
* ActiveGate не может подключиться к любому поду или сервису внутри mesh. Если сбор метрик — единственная ваша забота, см. обходное решение [Сбор метрик с использованием слияния метрик Istio](#metric-scraping-using-istio-metric-merging) (не применимо для Istio ambient).

В зависимости от того, находится ли большинство ваших отслеживаемых рабочих нагрузок внутри mesh или большинство целей для сбора метрик внутри mesh, развёртывание только ActiveGate внутри mesh может быть более подходящим вариантом.

### Развёртывание ActiveGate внутри mesh

Наиболее совместимый вариант развёртывания — размещение только ActiveGate внутри mesh. Этот вариант развёртывания имеет наибольший смысл, если большинство ваших отслеживаемых рабочих нагрузок также являются частью mesh или если вам нужно, чтобы ActiveGate напрямую подключался к подам внутри mesh (например, для сбора метрик Prometheus).

1. Убедитесь, что пространство имён Dynatrace Operator не помечено для инъекции Istio (метки `istio-injection` или `istio.io/dataplane-mode` не установлены).
2. Пометьте поды ActiveGate для Istio, добавив следующее в DynaKube:

   Sidecar

   Ambient

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: your-dynakube-name


   spec:


   enableIstio: true


   activeGate:


   labels:


   sidecar.istio.io/inject: "true"
   ```

   Перезапустите поды ActiveGate для запуска инъекции.

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: your-dynakube-name


   spec:


   enableIstio: true


   activeGate:


   labels:


   istio.io/dataplane-mode: "ambient"
   ```
3. Необязательно. Вы можете включить связь от OneAgent вне mesh к ActiveGate, развернув следующий ресурс `PeerAuthentication`:

   ```
   apiVersion: security.istio.io/v1


   kind: PeerAuthentication


   metadata:


   name: ag-no-mtls # <yourname>


   namespace: dynatrace-operator # <operator namespace>


   spec:


   mtls:


   mode: PERMISSIVE


   selector:


   matchLabels:


   app.kubernetes.io/managed-by: dynatrace-operator


   app.kubernetes.io/name: activegate
   ```

Вся связь с ActiveGate по-прежнему будет шифроваться через HTTPS.

Настройка CSI-драйвера Dynatrace Operator с Istio в режиме registry-only и пользовательским codeModulesImage

### Настройка CSI-драйвера Dynatrace Operator с Istio в режиме registry-only

При использовании Istio, настроенного в режиме `REGISTRY_ONLY`, с полем `codeModulesImage` для CSI-драйвера необходимо применить дополнительную конфигурацию для обеспечения надлежащей связи с реестром образов.

#### Предварительные требования

* Istio установлен и настроен в режиме `REGISTRY_ONLY`.
* Не поддерживается CSI-драйвер Dynatrace Operator инъецирован Istio.
* Поле `codeModulesImage` указано в конфигурации CSI-драйвера.

#### Настройка `ServiceEntry` для CSI-драйвера

1. Создайте `ServiceEntry`.

   Конфигурация `ServiceEntry` позволяет CSI-драйверу Dynatrace Operator взаимодействовать с указанным реестром образов. Без этой конфигурации процесс загрузки образа завершится неудачей. Ниже приведён пример `ServiceEntry` для `docker.io`.

   ```
   apiVersion: networking.istio.io/v1


   kind: ServiceEntry


   metadata:


   name: codemodules-docker-io


   namespace: dynatrace


   spec:


   hosts:


   - index.docker.io


   - auth.docker.io


   - production.cloudflare.docker.com


   location: MESH_EXTERNAL


   ports:


   - name: https-443


   number: 443


   protocol: HTTPS


   resolution: DNS
   ```
2. Примените `ServiceEntry`.

   Сохраните и примените вышеуказанную конфигурацию в файл.

   ```
   kubectl apply -f serviceentry.yaml
   ```

## Сбор метрик с использованием слияния метрик Istio

[Сбор метрик Dynatrace](../../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics.md "Приём метрик из конечных точек Prometheus в Kubernetes, оповещения по метрикам и мониторинг потребления.") выполняется через ActiveGate и настраивается с помощью аннотаций. Это приводит к тому, что ActiveGate подключается напрямую к подам на настроенной конечной точке для сбора метрик. Как отмечалось ранее, это прямое подключение не работает со строгим mTLS.

Режим ambient Istio не поддерживает слияние метрик, так как для этого требуется sidecar-прокси. Однако в режиме ambient ActiveGate может напрямую подключаться к IP-адресам подов и собирать метрики с настроенных целей. В зависимости от вашей политики mTLS это может быть возможно только для подов внутри mesh, если ActiveGate также является частью mesh.

Istio предоставляет функцию, называемую [слияние метрик](https://dt-url.net/5y43ufx), которая использует (широко принятые) аннотации `prometheus.io/...` для настройки дополнительной конечной точки в sidecar-прокси, которая предоставляет метрики Istio и Envoy, а также метрики приложения, определённые аннотациями. Эта вновь созданная конечная точка исключена из mTLS и поэтому доступна извне mesh, несмотря на mTLS в строгом режиме.

Теперь вы можете направить аннотации Dynatrace на эту конечную точку для сбора метрик Istio и приложения. Если вы не хотите собирать дополнительные метрики Istio и Envoy, вы можете исключить их с помощью аннотации `metrics.dynatrace.com/filter`, исключив метрики `istio_*` и `envoy_*`.

Таким образом, ActiveGate вне (или внутри) mesh может собирать метрики с подов внутри mesh.

Пример всех необходимых аннотаций:

```
apiVersion: v1


kind: Pod


metadata:


annotations:


...


metrics.dynatrace.com/path: /stats/prometheus # Endpoint created by Istio


metrics.dynatrace.com/port: "15020" # Port of the Envoy sidecar


metrics.dynatrace.com/scrape: "true"


prometheus.io/path: /metrics # Metric endpoint of the application


prometheus.io/port: "8080" # Metric port of the application


prometheus.io/scrape: "true"


...
```

Имейте в виду, что Istio перезапишет аннотации `prometheus.io/...` на сгенерированную конечную точку и порт при применении вышеуказанного пода. Это означает, что результирующий под в кластере не будет соответствовать применённому YAML.

## Устранение неполадок

Реестр сервисов Istio

Вы можете получить все сервисы, известные Istio (реестр сервисов), выполнив следующую команду внутри контейнера `pilot` пода `istiod`.

```
curl localhost:8080/debug/registryz
```

Эта команда выводит все известные сервисы в формате JSON. Он должен содержать записи для тенанта Dynatrace и ActiveGate в кластере.

Если нет, проверьте, установлен ли `enableIstio` в `true` в DynaKube.

## Связанные темы

* [Настройка трассировки OpenTelemetry с Istio](../../../opentelemetry/integrations/istio.md "Узнайте, как настроить Istio в Kubernetes для развёртывания предварительно настроенных прокси-сервисов для трассировки OpenTelemetry.")
