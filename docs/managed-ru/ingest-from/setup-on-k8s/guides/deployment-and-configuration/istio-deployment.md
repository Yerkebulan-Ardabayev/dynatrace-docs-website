---
title: Развёртывание Dynatrace вместе с Istio
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment
scraped: 2026-05-12T12:09:20.464446
---

# Развёртывание Dynatrace вместе с Istio

# Развёртывание Dynatrace вместе с Istio

* Чтение: 10 мин
* Обновлено 22 октября 2025 г.

В этом руководстве описано, как компоненты Dynatrace можно развернуть вместе с Istio. Развёртывание Dynatrace в Kubernetes содержит несколько компонентов, которым необходимо взаимодействовать друг с другом, с кластером Dynatrace и другими внешними ресурсами.

Дополнительную информацию о взаимодействии Dynatrace Operator и управляемых им компонентов см. на справочной странице [Сетевой трафик](/managed/ingest-from/setup-on-k8s/reference/network "Требования к сетевому трафику для компонентов Dynatrace Operator в кластере Kubernetes.").

## Ограничения

* Инъекция Istio в пространство имён Dynatrace Operator не поддерживается.
* Производные сборки Istio в настоящее время не поддерживаются (например, Maistra или OpenShift Service Mesh).
* Развёртывание Istio East-West (sidecar в сочетании с ambient) не поддерживается.

## Вопросы для рассмотрения при настройке

В этом руководстве рассматриваются две предопределённые конфигурации Istio, выбранные за их простоту и распространённость сценариев использования. Хотя Istio предлагает обширные возможности настройки, эти конфигурации служат отправной точкой. В этом разделе описаны сценарии конфигурации и приводятся рекомендации по выбору подходящей настройки Dynatrace, наиболее соответствующей вашим потребностям. Обратите внимание, что Dynatrace не накладывает никаких ограничений на то, как вы настраиваете Istio.

* **Конфигурация Istio по умолчанию** Рекомендуется
  Это стандартное развёртывание Istio, то есть без особой конфигурации сетки. По сути, это результат следования официальному [руководству по установке Istio](https://dt-url.net/hm03u3r).
  Это означает, что Istio устанавливается через Helm или `istioctl` в режиме sidecar с узловым агентом CNI.

  Следуйте [руководству по настройке конфигурации Istio по умолчанию](#setup-guide-for-default-istio-configuration), если Istio развёрнут соответствующим образом.
* **Защищённая конфигурация Istio**
  Это «защищённая» конфигурация Istio. Однако это не означает, что мы считаем её лучшей практикой настройки безопасности в Istio или что её следует рассматривать как руководство по защите Istio. Эта настройка основана на параметрах, которые с наибольшей вероятностью влияют на развёрнутые компоненты Dynatrace и их соединения. Этот сценарий предполагает, что Istio развёрнут со строгим mTLS и `outboundTrafficPolicy`, установленным в `REGISTRY_ONLY`. Эти параметры существенно ограничивают входящие и исходящие соединения для рабочих нагрузок в сетке.

  Выберите эту конфигурацию, если применим любой из приведённых ниже пунктов:

  + Если вы включили mTLS в строгом режиме.
  + Если у вас `outboundTrafficPolicy` установлен в `REGISTRY_ONLY`.

  Если ни один из приведённых выше пунктов не применим, выберите [Конфигурацию Istio по умолчанию](#setup-guide-for-default-istio-configuration).
  Следуйте [руководству по настройке защищённой конфигурации Istio](#setup-guide-for-secure-istio-configuration), если Istio развёрнут соответствующим образом.

### Другие вопросы для рассмотрения при развёртывании

Отключение инъекции в поды CNI

#### Отключение инъекции в поды CNI

Это актуально для вас, если к вашему развёртыванию применимо всё следующее:

* Не поддерживается Dynatrace Operator развёрнут внутри сетки.
* Istio развёрнут с использованием sidecar.
* Istio настроен на использование компонента CNI.
* Вы не настроили в DynaKube ни одного селектора пространств имён, который исключал бы пространство имён `istio-system`.

Во всех сценариях следует исключить поды Istio CNI из инъекции Dynatrace Operator. В противном случае при добавлении нового узла в кластер возможно возникновение взаимоблокировки.

И CSI driver, и агент CNI Istio являются DaemonSets, поэтому будут развёрнуты на любом (новом) узле кластера.

* В под CSI driver Istio внедрит init-контейнер, который ожидает корректной настройки правил перенаправления, необходимых для работы proxy sidecar.
* В под CNI Dynatrace внедрит необходимые для инструментирования бинарные файлы OneAgent, которые предоставляются через том, подготавливаемый CSI driver на этом узле.

Это приводит к ситуации, когда оба пода не могут запуститься:

* Под CNI ожидает, пока CSI driver не будет готов предоставить том.
* Под CSI ожидает, пока агент CNI не предоставит перенаправления для proxy.

Кроме того, это затронет все остальные рабочие нагрузки, которые являются целью инъекции Istio или Dynatrace и планируются на этот узел, и они не смогут запуститься.

Самый простой способ исключить поды CNI из инъекции Dynatrace Operator, это добавить аннотацию `oneagent.dynatrace.com/inject: "false"`. Например, для развёртывания Istio через Helm добавьте следующее в значения чарта `cni`:

```
cni:



podAnnotations:



oneagent.dynatrace.com/inject: "false"
```

Поддержка нативных sidecar

#### Поддержка нативных sidecar

Istio 1.28, развёрнутый на совместимом кластере Kubernetes (>=1.29), будет использовать нативные контейнеры sidecar. Этот новый тип контейнера sidecar в настоящее время не поддерживается Dynatrace Operator. Отключите нативные sidecar в вашем развёртывании Istio, добавив следующую переменную окружения в развёртывание pilot.

Пример значений для helm-чарта Istio:

```
pilot:



...



env:



ENABLE_NATIVE_SIDECARS: false



...
```

## Руководство по настройке конфигурации Istio по умолчанию

Поскольку Dynatrace поддерживает Istio в конфигурации по умолчанию, вам нужно лишь включить параметр `enableIstio` в [DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Однако задавать этот параметр не требуется, если вы не планируете использовать ограничительный `outboundTrafficPolicy`.

Когда этот параметр включён, Dynatrace Operator развернёт `ServiceEntries` и `VirtualServices`, чтобы обеспечить взаимодействие изнутри сетки со всеми соответствующими компонентами Dynatrace и окружением Dynatrace. `ServiceEntries` и `VirtualServices` работают независимо от того, является ли само пространство имён Dynatrace Operator частью сетки (если в Istio не задан `discoveryfilter`).

Это позволяет всем рабочим нагрузкам и экземплярам OneAgent подключаться к экземпляру ActiveGate и устанавливать все необходимые соединения с окружением Dynatrace. Поэтому ожидается, что все функции Dynatrace будут работать.

`ServiceEntries` приводят к дополнительным DNS-запросам, выполняемым каждым proxy sidecar. Это может создать дополнительную нагрузку на ваш DNS-сервер.

Чтобы минимизировать количество URL-адресов и, соответственно, DNS-запросов, убедитесь, что network zones в вашем окружении Dynatrace настроены правильно. Подробное описание настройки см. в [документации по network zone для Kubernetes](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones#kubernetes-cluster-with-restricted-egress "Настройка и использование network zones в окружениях Kubernetes с Dynatrace Operator.").

Если это невозможно или недостаточно в вашем окружении, см. [Istio DNS proxying](https://dt-url.net/ab23uvy) как ещё один возможный способ смягчения.

### Как работает `enableIstio`

Атрибут `enableIstio`, это функция для удобства, которая автоматически создаёт `ServiceEntries` и `VirtualServices` для конечных точек соединения, необходимых:

* Dynatrace Operator: использует `apiUrl`, определённый в DynaKube.
* ActiveGate: использует конечную точку `/v1/deployment/installer/gateway/connectioninfo`.
* OneAgent, внедрённый в пользовательские контейнеры: использует `/v1/deployment/installer/agent/connectioninfo`, который учитывает атрибут `networkZone` для маршрутизации.

Обратите внимание, что атрибут `enableIstio` не учитывает уже существующие `ServiceEntries` и `VirtualServices`. Преждевременное использование этого атрибута может привести к конфликтам в конфигурациях Istio. В сложных настройках ручная настройка может дать лучшие результаты.

Изменения атрибута `enableIstio` требуют удаления и повторного применения вашего DynaKube, чтобы обновление вступило в силу.

Ручная настройка

Ручная настройка `ServiceEntries` и `VirtualServices` может потребоваться в следующих случаях:

#### ActiveGate

* **Требование**: необходимо, если под ActiveGate является частью сетки.
* **Конфигурация**: вручную настройте `ServiceEntries` и `VirtualServices` на основе вывода конечной точки `/v1/deployment/installer/gateway/connectioninfo`.

#### `cloudNativeFullstack` и `applicationMonitoring`

* **Требование**: необходимо, если внедрённые пользовательские приложения являются частью сетки.
* **Конфигурация**: вручную настройте `ServiceEntries` и `VirtualServices` на основе вывода конечной точки `/v1/deployment/installer/agent/connectioninfo`.

## Руководство по настройке защищённой конфигурации Istio

В таком ограниченном окружении и в зависимости от необходимых вам функций Dynatrace и других соображений может потребоваться создать несколько дополнительных правил конфигурации для Istio. Принимая решение о том, как развернуть Dynatrace Operator, следует учесть ряд моментов, касающихся компонентов Dynatrace.

* Даже если на ActiveGate включена маршрутизация, экземпляры OneAgent вернутся к прямому подключению к окружению Dynatrace, если ActiveGate недоступен (например, потому что он находится внутри сетки). Это означает, что данные мониторинга не теряются, если некоторые экземпляры OneAgent не могут подключиться к ActiveGate из-за выбранной стратегии развёртывания.
* Режимы мониторинга `classicFullStack` или `cloudNativeFullStack` создают поды с включённым host networking. Это означает, что такие поды никогда не могут быть частью сетки, поскольку Istio не поддерживает поды с host networking. Для `classicFullStack` такие поды обрабатывают все метрики приложения, тогда как для `cloudNativeFullStack` затрагивается только мониторинг хоста.
* Некоторые функции ActiveGate могут требовать прямых соединений с подами (например, сбор метрик (scraping)). При включённом в Istio mTLS прямые соединения с IP-адресами подов невозможны. Обходной путь для сбора метрик см. в разделе [Объединение метрик Istio](#metric-scraping-using-istio-metric-merging).

### Развёртывание вне сетки

В этом сценарии наименее сложным является развёртывание вне сетки. Вам по-прежнему необходимо включить параметр `enableIstio` в DynaKube. Возможные недостатки такого развёртывания могут включать:

* Взаимодействие изнутри сетки с ActiveGate не будет защищено mTLS. Однако взаимодействие по-прежнему шифруется через HTTPS.
* ActiveGate не может подключиться к какому-либо поду или сервису внутри сетки. Если вас беспокоит только сбор метрик, см. обходной путь [Сбор метрик с использованием объединения метрик Istio](#metric-scraping-using-istio-metric-merging) (неприменимо для Istio ambient).

В зависимости от того, является ли большая часть ваших отслеживаемых рабочих нагрузок частью сетки или большая часть ваших целей для сбора метрик находится внутри сетки, развёртывание внутри сетки только ActiveGate может быть более подходящим вариантом.

### Развёртывание ActiveGate внутри сетки

Наиболее совместимый вариант развёртывания, это развернуть внутри сетки только ActiveGate. Этот вариант развёртывания наиболее целесообразен, если большая часть ваших отслеживаемых рабочих нагрузок также является частью сетки или если вам нужно, чтобы ActiveGate напрямую подключался к подам внутри сетки (например, для сбора (scraping) Prometheus).

1. Убедитесь, что пространство имён Dynatrace Operator не помечено для инъекции Istio (метка `istio-injection` или `istio.io/dataplane-mode` не задана).
2. Пометьте поды ActiveGate для Istio, добавив следующее в ваш DynaKube:

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

   Перезапустите поды ActiveGate, чтобы запустить инъекцию.

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
3. Необязательно. Можно включить взаимодействие экземпляров OneAgent вне сетки с ActiveGate, развернув следующий ресурс `PeerAuthentication`:

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

Всё взаимодействие с ActiveGate по-прежнему будет шифроваться с использованием HTTPS.

Настройка Dynatrace Operator CSI driver с Istio в режиме registry-only и пользовательским codeModulesImage

### Настройка Dynatrace Operator CSI driver с Istio в режиме registry-only

При использовании Istio, настроенного в режим `REGISTRY_ONLY`, с полем `codeModulesImage` для CSI driver необходимо применить дополнительную конфигурацию для обеспечения надлежащего взаимодействия с реестром образов.

#### Предварительные требования

* Istio установлен и настроен в режиме `REGISTRY_ONLY`.
* Не поддерживается Dynatrace Operator CSI driver внедрён с помощью Istio.
* Поле `codeModulesImage` указано в конфигурации CSI driver.

#### Настройка `ServiceEntry` для CSI driver

1. Создайте `ServiceEntry`.

   Конфигурация `ServiceEntry` позволяет Dynatrace Operator CSI driver взаимодействовать с указанным реестром образов. Без этой конфигурации процесс загрузки образа завершится сбоем. См. пример `ServiceEntry` для `docker.io` ниже.

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

   Сохраните приведённую выше конфигурацию в файл и примените её.

   ```
   kubectl apply -f serviceentry.yaml
   ```

## Сбор метрик с использованием объединения метрик Istio

[Сбор метрик Dynatrace](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Прием метрик из конечных точек Prometheus в Kubernetes, оповещения по метрикам и потребление мониторинга.") выполняется через ActiveGate и настраивается с помощью аннотаций. В результате ActiveGate подключается напрямую к подам на настроенной конечной точке для сбора метрик. Как указано ранее, такое прямое соединение не работает со строгим mTLS.

Режим Istio ambient не поддерживает объединение метрик, поскольку для него требуется proxy sidecar. Однако в режиме ambient ActiveGate может напрямую подключаться к IP-адресам подов и собирать данные с настроенных целей. В зависимости от вашей политики mTLS это может быть возможно только для подов внутри сетки, если ActiveGate также является частью сетки.

Istio предоставляет функцию под названием [объединение метрик](https://dt-url.net/5y43ufx), которая использует (широко применяемые) аннотации `prometheus.io/...` для настройки дополнительной конечной точки в proxy sidecar, которая предоставляет метрики Istio и Envoy, а также метрики приложения, определённые аннотациями. Эта вновь созданная конечная точка исключена из mTLS и поэтому доступна извне сетки, несмотря на наличие mTLS в строгом режиме.

Теперь можно направить аннотации Dynatrace на эту конечную точку, чтобы собирать метрики Istio и приложения. Если собирать дополнительные метрики Istio и Envoy не требуется, их можно исключить с помощью аннотации `metrics.dynatrace.com/filter`, исключив метрики `istio_*` и `envoy_*`.

Таким образом, ActiveGate вне сетки (или внутри неё) может собирать метрики с подов внутри сетки.

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

Имейте в виду, что Istio перепишет аннотации `prometheus.io/...` на сгенерированные конечную точку и порт при применении приведённого выше пода. Это означает, что итоговый под в кластере не будет соответствовать применённому YAML.

## Устранение неполадок

Реестр сервисов Istio

Получить все известные сервисы Istio (реестр сервисов) можно, выполнив следующую команду внутри контейнера `pilot` пода `istiod`.

```
curl localhost:8080/debug/registryz
```

Это выводит все известные сервисы в формате JSON. Он должен содержать записи для тенанта Dynatrace и ActiveGate в кластере.

Если нет, проверьте, установлен ли `enableIstio` в `true` в DynaKube.

## Связанные темы

* [Настройка трассировки OpenTelemetry с Istio](/managed/ingest-from/opentelemetry/integrations/istio "Узнайте, как настроить Istio в Kubernetes для развёртывания предварительно настроенных proxy-сервисов для трассировки OpenTelemetry.")