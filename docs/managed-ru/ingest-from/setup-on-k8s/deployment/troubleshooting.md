---
title: Устранение неполадок
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/troubleshooting
---

# Устранение неполадок

# Устранение неполадок

* 7 мин чтения
* Обновлено 10 июля 2026 г.

Этот раздел содержит полное руководство, которое поможет диагностировать и устранить типовые проблемы.

[#### Устранение неполадок мониторинга

Устранение типовых проблем, которые могут возникать при мониторинге Kubernetes с помощью Dynatrace.

Устранение неполадок мониторинга](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting)[#### Проблемы подключения между Dynatrace и кластером Kubernetes

Устранение типовых проблем подключения между Dynatrace и кластером Kubernetes.

Проблемы подключения между Dynatrace и кластером Kubernetes](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/connectivity-issues)

## Начальные шаги устранения неполадок

Перед переходом к конкретным разделам устранения неполадок важно чётко понимать текущее состояние кластера Kubernetes. Описанные ниже начальные шаги помогут собрать основную информацию о состоянии кластера и статусе его компонентов.

1. Проверить статус DynaKube, выполнив команду `kubectl get dynakubes -n dynatrace`.
2. [Использовать подкоманду `troubleshoot`](#troubleshoot).
3. Проверить статус подов Dynatrace  
   Команда `kubectl -n dynatrace get pods` используется для проверки статуса подов Dynatrace Operator, OneAgent или CSI driver (количество подов зависит от выбранного режима развёртывания).
4. Просмотреть логи  
   Команда `kubectl logs` используется для просмотра логов конкретных подов. Например, `kubectl logs <pod-name>` выведет логи конкретного пода.
5. Описать ресурс  
   Команда `kubectl describe` предоставляет подробную информацию о конкретном ресурсе. Например, `kubectl describe pod <pod-name>` выведет подробную информацию о конкретном поде.

## Общее устранение неполадок

Общие шаги и рекомендации по устранению неполадок, встречающихся при использовании Dynatrace с Kubernetes. Раздел описывает, как получить доступ к отладочным логам, использовать подкоманду `troubleshoot` или сформировать архив поддержки.

### Устранение типовых проблем настройки Dynatrace Operator с помощью подкоманды `troubleshoot`

Dynatrace Operator версии 0.9.0+

Выполнить команду ниже, чтобы получить базовый вывод о статусе DynaKube, включающий:

* **Namespace:** существует ли пространство имён `dynatrace` (имя можно переопределить параметром)
* **DynaKube:**

  + существует ли `CustomResourceDefinition`
  + существует ли `CustomResource` с указанным именем (имя можно переопределить параметром)
  + заканчивается ли URL API на `/api`
  + совпадает ли имя secret с именем DynaKube (или используется `.spec.tokens`, если задан)
  + заданы ли в secret токены Dynatrace Operator и Data Ingest
  + определён ли secret для `customPullSecret`
* **Environment:** доступно ли окружение из пода Dynatrace Operator с теми же параметрами, что и у бинарника Dynatrace Operator (такими как прокси и сертификат).
* **Образ OneAgent и ActiveGate:** доступен ли registry; доступен ли образ из пода Dynatrace Operator, используя registry из окружения с (кастомным) pull secret.

```
kubectl exec deploy/dynatrace-operator -n dynatrace -- dynatrace-operator troubleshoot
```

Если используется другое имя DynaKube, нужно добавить к команде аргумент `--dynakube <your_dynakube_name>`.

Пример вывода при отсутствии ошибок по указанным выше полям:

```
{"level":"info","ts":"2022-09-12T08:45:21.437Z","logger":"dynatrace-operator-version","msg":"dynatrace-operator","version":"<operator version>","gitCommit":"<commithash>","buildDate":"<release date>","goVersion":"<go version>","platform":"<platform>"}



[namespace ]     --- checking if namespace 'dynatrace' exists ...



[namespace ]      √  using namespace 'dynatrace'



[dynakube  ]     --- checking if 'dynatrace:dynakube' Dynakube is configured correctly



[dynakube  ]         CRD for Dynakube exists



[dynakube  ]         using 'dynatrace:dynakube' Dynakube



[dynakube  ]         checking if api url is valid



[dynakube  ]         api url is valid



[dynakube  ]         checking if secret is valid



[dynakube  ]         'dynatrace:dynakube' secret exists



[dynakube  ]         secret token 'apiToken' exists



[dynakube  ]         customPullSecret not used



[dynakube  ]         pull secret 'dynatrace:dynakube-pull-secret' exists



[dynakube  ]         secret token '.dockerconfigjson' exists



[dynakube  ]         proxy secret not used



[dynakube  ]      √  'dynatrace:dynakube' Dynakube is valid



[dtcluster ]     --- checking if tenant is accessible ...



[dtcluster ]      √  tenant is accessible
```

### Отладочные логи

По умолчанию логи OneAgent находятся в `/var/log/dynatrace/oneagent`.

Для отладки проблем Dynatrace Operator нужно выполнить

Kubernetes

OpenShift

```
kubectl -n dynatrace logs -f deployment/dynatrace-operator
```

```
oc -n dynatrace logs -f deployment/dynatrace-operator
```

Также может понадобиться проверить логи подов OneAgent, развёрнутых через Dynatrace Operator.

Kubernetes

OpenShift

```
kubectl get pods -n dynatrace



NAME                                           READY     STATUS    RESTARTS   AGE



dynatrace-operator-64865586d4-nk5ng   1/1       Running   0          1d



dynakube-oneagent-<id>                             1/1       Running   0          22h
```

```
kubectl logs dynakube-oneagent-<id> -n dynatrace
```

```
oc get pods -n dynatrace



NAME                                           READY     STATUS    RESTARTS   AGE



dynatrace-operator-64865586d4-nk5ng            1/1       Running   0          1d



dynakube-classic-8r2kq                         1/1       Running   0          22h
```

```
oc logs oneagent-66qgb -n dynatrace
```

### Создание архива поддержки с помощью подкоманды `support-archive`

Dynatrace Operator версии 0.11.0+

Подкоманда `support-archive` используется для создания архива файлов, которые могут пригодиться при расследовании обращений в поддержку:

* `kubernetes-version.txt` (версия сервера Kubernetes кластера)
* `operator-version.txt` (информация о версии Dynatrace Operator)
* `logs` (логи всех контейнеров подов Dynatrace Operator и компонентов Dynatrace, развёрнутых Dynatrace Operator в пространстве имён Dynatrace Operator, обычно `dynatrace`; сюда также входят логи предыдущих контейнеров, если они доступны):

  + `activegate` (если развёрнут [ActiveGate](/managed/ingest-from/dynatrace-activegate "Понять базовые концепции, связанные с ActiveGate."))
  + `dynakube-logmonitoring` (если Log Monitoring использует [Kubernetes Log Module](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed."))
  + `dynatrace-oneagent` (если в [DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") используется `cloudNativeFullStack` или `hostMonitoring`)
  + `dynatrace-operator`
  + `dynatrace-webhook`
  + `dynatrace-oneagent-csi-driver` (если развёрнут [CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Компоненты Dynatrace Operator"))

    - `liveness-probe`
    - `provisioner`
    - `registrar`
    - `server`
  + `extension-controller` (если включены Extensions)
  + `sql-ext-exec` (если включены SQL Extensions)
  + `otel-collector` (если включён [telemetryIngest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включить эндпоинты приёма телеметрии Dynatrace в Kubernetes для локального в рамках кластера приёма данных."))
  + `node-config-collector` (если включён [KSPM](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed."))
* `manifests` (манифесты Kubernetes для компонентов Dynatrace Operator и развёрнутых DynaKube в пространстве имён Dynatrace Operator)
* `troubleshoot.txt` (вывод команды диагностики, которая автоматически выполняется подкомандой `support-archive`)
* `supportarchive_console.log` (полный вывод подкоманды `support-archive`)
* Диагностические файлы Extension Controller

  + все файлы, найденные в `/var/lib/dynatrace/remotepluginmodule/log/extensions` внутри пода Extension Controller

#### Использование

Чтобы создать архив поддержки, выполните следующую команду:

```
kubectl exec -n dynatrace deployment/dynatrace-operator -- dynatrace-operator support-archive --stdout > operator-support-archive.zip
```

Содержимое архива поддержки записывается в `stdout`, что позволяет перенаправить его в ZIP-файл. Остальной вывод отправляется в `stderr`, чтобы не нарушать целостность файла архива.

Windows PowerShell не поддерживается

На Windows нужно использовать командную строку (`cmd.exe`); PowerShell не поддерживается.

#### Запуск `support-archive` в отдельном поде

Dynatrace Operator версии 1.0.0+

Если под `operator` не функционирует из-за серьёзных проблем при запуске или неожиданно завершает работу, можно выполнить команду `support-archive` в отдельном поде с помощью следующей команды. Стоит учитывать, что запуск этой команды в отдельном поде рекомендуется только как крайняя мера.

```
kubectl run -n dynatrace support-archive --rm -i --overrides='{ "spec": { "serviceAccount": "dynatrace-operator" }  }' --restart Never --image <operator-image> -- support-archive --delay 10 --stdout > support-archive.zip
```

* Нужно использовать тот же образ, что и под `operator`.
* Параметр `--delay 10` важен, поскольку `kubectl run` часто пропускает несколько первых строк вывода, что может привести к повреждению архива поддержки.
* В команде нужно указать `serviceAccount` как `dynatrace-operator`, поскольку это даёт отдельному поду доступ ко всем логам и манифестам Kubernetes, необходимым для сборки архива поддержки. Стоит учитывать, что этот способ полагается на то, что ресурсы Dynatrace Operator по-прежнему установлены и доступны в кластере.

На больших кластерах, где объём собираемых данных подов приводит к превышению Dynatrace Operator лимита памяти, может происходить остановка из-за нехватки памяти (OOM). Это более вероятно, если Dynatrace Operator не рассчитан по размеру на данный кластер. В этом случае описанный выше способ с отдельным подом поможет собрать архив.

#### Пример вывода

Ниже приведён пример вывода при запуске `support-archive` с параметром `--stdout`.

```
kubectl exec -n dynatrace deployment/dynatrace-operator -- dynatrace-operator support-archive --stdout > operator-support-archive.zip
```

```
[support-archive]       dynatrace-operator      {"version": "v0.11.0", "gitCommit": "...", "buildDate": "...", "goVersion": "...", "platform": "linux/amd64"}



[support-archive]       Storing operator version into operator-version.txt



[support-archive]       Starting log collection



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/server.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/provisioner.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/registrar.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/liveness-probe.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/server.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/provisioner.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/registrar.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/liveness-probe.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/server.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/provisioner.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/registrar.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/liveness-probe.log



[support-archive]       Successfully collected logs logs/dynatrace-operator-6d9fd9b9fc-sw5ll/dynatrace-operator.log



[support-archive]       Successfully collected logs logs/dynatrace-webhook-7d84599455-bfkmp/webhook.log



[support-archive]       Successfully collected logs logs/dynatrace-webhook-7d84599455-vhkrh/webhook.log



[support-archive]       Successfully collected logs logs/<dynakube name>-node-config-collector-dmg2b/node-config-collector.log



[support-archive]       Successfully collected logs logs/<dynakube name>-node-config-collector-kgscf/node-config-collector.log



[support-archive]       Successfully collected logs logs/<dynakube name>-node-config-collector-wstzt/node-config-collector.log



[support-archive]       Successfully collected logs logs/<dynakube name>-activegate-0/activegate.log



[support-archive]       Successfully collected logs logs/<dynakube name>-extension-controller-0/extension-controller.log



[support-archive]       Successfully collected logs logs/<dynakube name>-oneagent-6bhpx/dynatrace-oneagent.log



[support-archive]       Successfully collected logs logs/<dynakube name>-oneagent-9f7mm/dynatrace-oneagent.log



[support-archive]       Successfully collected logs logs/<dynakube name>-oneagent-hq4ks/dynatrace-oneagent.log



[support-archive]       Successfully collected logs logs/<dynakube name>-otel-collector-0/collector.log



[support-archive]       Successfully collected EEC diagnostic logs logs/<dynakube name>-extension-controller-0/var/lib/dynatrace/remotepluginmodule/log/extensions/ruxitagent_extensionsmodule_1.0.log



[support-archive]       Successfully collected EEC diagnostic logs logs/<dynakube name>-extension-controller-0/var/lib/dynatrace/remotepluginmodule/log/extensions/diagnostics/diag_executor.log



[support-archive]       Starting K8S object collection



[support-archive]       Collected manifest for manifests/injected_namespaces/namespace-default.yaml



[support-archive]       Collected manifest for manifests/dynatrace/namespace-dynatrace.yaml



[support-archive]       Collected manifest for manifests/dynatrace/deployment/dynatrace-operator.yaml



[support-archive]       Collected manifest for manifests/dynatrace/deployment/dynatrace-webhook.yaml



[support-archive]       Collected manifest for manifests/dynatrace/daemonset/dynatrace-oneagent-csi-driver.yaml



[support-archive]       Collected manifest for manifests/dynatrace/daemonset/<dynakube name>-node-config-collector.yaml



[support-archive]       Collected manifest for manifests/dynatrace/statefulset/<dynakube name>-activegate.yaml



[support-archive]       Collected manifest for manifests/dynatrace/statefulset/<dynakube name>-extension-controller.yaml



[support-archive]       Collected manifest for manifests/dynatrace/statefulset/<dynakube name>-otel-collector.yaml



[support-archive]       Collected manifest for manifests/dynatrace/daemonset/<dynakube name>-oneagent.yaml



[support-archive]       Collected manifest for manifests/dynatrace/dynakube/<dynakube name>.yaml



[support-archive]       Collected manifest for manifests/dynatrace/configmap/dynatrace-node-cache.yaml



[support-archive]       Collected manifest for manifests/webhook_configurations/mutatingwebhookconfiguration.yaml



[support-archive]       Collected manifest for manifests/webhook_configurations/validatingwebhookconfiguration.yaml



[support-archive]       Collected manifest for manifests/crds/customresourcedefinition-edgeconnects.yaml



[support-archive]       Collected manifest for manifests/crds/customresourcedefinition-dynakubes.yaml
```

### Отладка проблем с конфигурацией и мониторингом с помощью расширения Kubernetes Monitoring Statistics

[Расширение Kubernetes Monitoring Statistics﻿](https://dt-url.net/n903xmb) помогает:

* устранять неполадки настройки Kubernetes Monitoring;
* устранять неполадки настройки интеграции Prometheus;
* получать детальную информацию о запросах от Dynatrace к Kubernetes API;
* получать оповещения при возникновении проблем с настройкой платформенного мониторинга Kubernetes;
* получать оповещения о медленном времени отклика Kubernetes API.

### Возможные проблемы при изменении режима мониторинга

* Изменение режима мониторинга с `classicFullStack` на `cloudNativeFullStack` влияет на расчёт host ID для отслеживаемых хостов, из-за чего назначаются новые ID и связь между старыми и новыми сущностями отсутствует.
* Если нужно изменить метод мониторинга с `applicationMonitoring` или `cloudNativeFullstack` на `classicFullstack` или `hostMonitoring`, нужно перезапустить все Pod, которые ранее были инструментированы с помощью `applicationMonitoring` или `cloudNativeFullstack`.

### Устранение проблем внедрения в под с помощью аннотаций пода

Если OneAgent, metadata enrichment или конфигурация экспортера OTLP не внедряются как ожидается, нужно проверить аннотации на затронутом поде, чтобы выяснить, почему внедрение было пропущено.

Следующие аннотации указывают на то, что webhook Dynatrace Operator намеренно пропустил внедрение для пода:

```
oneagent.dynatrace.com/injected: "false"



metadata-enrichment.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/injected: "false"
```

Соответствующая аннотация `reason` объясняет причину:

```
oneagent.dynatrace.com/reason: "MissingTenantUUID"



metadata-enrichment.dynatrace.com/reason: "OwnerLookupFailed"



otlp-exporter-configuration.dynatrace.com/reason: "IngestEndpointUnavailable"
```

#### Причины пропуска внедрения

Следующие значения `reason` помогают сузить первопричину.

| Reason | Затронутые компоненты | Описание | Подробности |
| --- | --- | --- | --- |
| `NoBootstrapperConfig` | * OneAgent * Metadata enrichment | Webhook не может найти или создать Secret конфигурации bootstrapper в пространстве имён пода на момент внедрения. | Обычно это происходит, когда согласование DynaKube не завершено или проблемы конфигурации препятствуют согласованию. Secret конфигурации bootstrapper содержит необходимую конфигурацию (например, токены) для внедрения CodeModule и metadata enrichment.  Существует два варианта:  * `<dynakube name>-bootstrapper-config` в пространстве имён Dynatrace Operator (обычно `dynatrace`), которое копируется при необходимости. * `dynatrace-bootstrapper-config` в пространстве имён пода, в который выполняется внедрение, которое монтируется в под и используется во время внедрения. |
| `NoMutationNeeded` | * OneAgent * Metadata enrichment | Webhook определяет, что поду не требуется внедрение. | Обычно это происходит, когда внедрение отключено с помощью аннотаций. |
| `OwnerLookupFailed` | * OneAgent * Metadata enrichment * OTLP exporter configuration | Webhook не может определить владельца пода (имя и вид), что необходимо для внедрения. | Обычно это происходит, когда Kubernetes API временно недоступен или медленно отвечает. |
| `MissingTenantUUID` | OneAgent | Согласование DynaKube не завершено, и UUID окружения не был проверен на момент внедрения. | Это может происходить во время первоначальной настройки Dynatrace Operator или когда проблемы конфигурации препятствуют согласованию. |
| `DynaKubeStatusNotReady` | OneAgent | Согласование DynaKube не завершено, и статус, связанный с CodeModules, не готов на момент внедрения. | Поскольку статус недоступен, webhook не может определить, какой CodeModule внедрять. |
| `NoOTLPExporterConfigSecret` | OTLP exporter configuration | Webhook не может найти или создать Secret конфигурации экспортера OTLP в пространстве имён пода на момент внедрения. | Обычно это происходит, когда согласование DynaKube не завершено или проблемы конфигурации препятствуют согласованию.  Существует два варианта:  * `<dynakube name>-otlp-exporter-config` в пространстве имён Dynatrace Operator (исходный Secret). * `dynatrace-otlp-exporter-config` в пространстве имён пода, в который выполняется внедрение, которое монтируется в под. |
| `NoOTLPExporterActiveGateCertSecret` | OTLP exporter configuration | Webhook не может найти или создать Secret сертификата ActiveGate в пространстве имён пода на момент внедрения. | Обычно это происходит, когда согласование DynaKube не завершено или проблемы конфигурации препятствуют согласованию. Этот Secret требуется только тогда, когда экспортер OTLP взаимодействует с ActiveGate через TLS.  Существует два варианта:  * `<dynakube name>-otlp-exporter-certs` в пространстве имён Dynatrace Operator (исходный Secret). * `dynatrace-otlp-exporter-certs` в пространстве имён пода, в который выполняется внедрение, которое монтируется в под. |
| `IngestEndpointUnavailable` | OTLP exporter configuration | Webhook не может построить корректный URL ingest endpoint на момент внедрения. | Без корректного URL ingest endpoint конфигурация экспортера OTLP не может быть внедрена. |

### Поды с внедрением завершаются ошибкой `ImagePullBackOff` в приватном реестре

Если поды приложений с внедрением не запускаются с ошибкой `ImagePullBackOff` при извлечении образа init-контейнера из приватного реестра, у подов отсутствуют действительные учётные данные реестра.

`customPullSecret` DynaKube аутентифицирует только компоненты, управляемые оператором, в пространстве имён `dynatrace`. Он не распространяется на поды приложений с внедрением. Каждый под с внедрением запускает init-контейнер Dynatrace (образ Dynatrace Operator или образ code modules OneAgent для [node image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.")), который узел Kubernetes должен извлечь, поэтому pull secret нужно предоставить самостоятельно.

Часто это проявляется после обновления до Kubernetes 1.35, где по умолчанию включён feature gate [`KubeletEnsureSecretPulledImages`﻿](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification). После этого kubelet проверяет учётные данные для извлечения по каждому поду, даже для образов, уже кэшированных на узле, поэтому поды, ранее использовавшие кэшированный образ повторно, теперь завершаются ошибкой без собственных учётных данных.

Чтобы решить эту проблему, распространите pull secret на пространства имён приложений, узлы или поды. Подробности см. в разделе [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").