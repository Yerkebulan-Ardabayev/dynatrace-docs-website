---
title: Устранение неполадок
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/troubleshooting
scraped: 2026-05-12T12:03:26.248401
---

# Устранение неполадок

# Устранение неполадок

* Чтение: 7 мин
* Обновлено 23 февраля 2026 г.

На этой странице приведено подробное руководство, помогающее диагностировать и устранять распространённые проблемы.

[#### Устранение неполадок мониторинга

Устранение распространённых проблем, которые могут возникнуть при мониторинге Kubernetes с помощью Dynatrace.

Устранение неполадок мониторинга](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting)[#### Проблемы связи между Dynatrace и кластером Kubernetes

Устранение распространённых проблем связи между Dynatrace и вашим кластером Kubernetes.

Проблемы связи между Dynatrace и кластером Kubernetes](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/connectivity-issues)

## Начальные шаги по устранению неполадок

Прежде чем переходить к конкретным разделам по устранению неполадок, важно иметь чёткое представление о текущем состоянии вашего кластера Kubernetes. Описанные ниже начальные шаги помогут собрать важную информацию о работоспособности кластера и состоянии его компонентов.

1. Проверьте состояние вашего DynaKube, выполнив команду `kubectl get dynakubes -n dynatrace`.
2. [Используйте подкоманду `troubleshoot`](#troubleshoot).
3. Проверьте состояние подов Dynatrace
   Используйте команду `kubectl -n dynatrace get pods`, чтобы проверить состояние подов Dynatrace Operator, OneAgent или CSI driver (количество подов зависит от выбранного режима развёртывания).
4. Изучите логи
   Используйте команду `kubectl logs`, чтобы изучить логи конкретных подов. Например, `kubectl logs <pod-name>` отобразит логи конкретного пода.
5. Опишите ресурс
   Команда `kubectl describe` может предоставить подробную информацию о конкретном ресурсе. Например, `kubectl describe pod <pod-name>` отобразит подробную информацию о конкретном поде.

## Общее устранение неполадок

Общие шаги и рекомендации по устранению распространённых проблем, возникающих при использовании Dynatrace с Kubernetes. Здесь описано, как получить доступ к отладочным логам, использовать подкоманду `troubleshoot` или создать архив поддержки.

### Устранение распространённых проблем настройки Dynatrace Operator с помощью подкоманды `troubleshoot`

Dynatrace Operator версии 0.9.0+

Выполните команду ниже, чтобы получить базовый вывод о состоянии DynaKube, например:

* **Namespace:** существует ли пространство имён `dynatrace` (имя можно переопределить через параметр)
* **DynaKube:**

  + существует ли `CustomResourceDefinition`
  + существует ли `CustomResource` с заданным именем (имя можно переопределить через параметр)
  + заканчивается ли URL API на `/api`
  + совпадает ли имя секрета с DynaKube (или `.spec.tokens`, если используется)
  + заданы ли в секрете токены Dynatrace Operator и Data Ingest
  + определён ли секрет для `customPullSecret`
* **Environment:** доступно ли ваше окружение из пода Dynatrace Operator с использованием тех же параметров, что и у бинарного файла Dynatrace Operator (таких как proxy и сертификат).
* **OneAgent and ActiveGate image:** доступен ли реестр; доступен ли образ из пода Dynatrace Operator с использованием реестра из окружения с (пользовательским) pull-секретом.

```
kubectl exec deploy/dynatrace-operator -n dynatrace -- dynatrace-operator troubleshoot
```

Если используется другое имя DynaKube, добавьте к команде аргумент `--dynakube <your_dynakube_name>`.

Пример вывода, если для перечисленных выше полей нет ошибок:

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

Чтобы отладить проблемы Dynatrace Operator, выполните

Kubernetes

OpenShift

```
kubectl -n dynatrace logs -f deployment/dynatrace-operator
```

```
oc -n dynatrace logs -f deployment/dynatrace-operator
```

Также может потребоваться проверить логи подов OneAgent, развёрнутых через Dynatrace Operator.

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

Используйте `support-archive`, чтобы создать архив файлов, которые могут быть полезны для расследований службы поддержки:

* `kubernetes-version.txt` (версия сервера Kubernetes кластера)
* `operator-version.txt` (информация о версии Dynatrace Operator)
* `logs` (логи из всех контейнеров подов Dynatrace Operator и компонентов Dynatrace, развёрнутых Dynatrace Operator в пространстве имён Dynatrace Operator, обычно `dynatrace`; сюда также входят логи предыдущих контейнеров, если они доступны):

  + `activegate` (если развёрнут [ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate."))
  + `dynakube-logmonitoring` (если Log Monitoring использует [Kubernetes Log Module](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."))
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
  + `otel-collector` (если включён [telemetryIngest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включение конечных точек приёма телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере."))
  + `node-config-collector` (если включён [KSPM](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."))
* `manifests` (манифесты Kubernetes для компонентов Dynatrace Operator и развёрнутых DynaKube в пространстве имён Dynatrace Operator)
* `troubleshoot.txt` (вывод команды устранения неполадок, которая автоматически выполняется подкомандой `support-archive`)
* `supportarchive_console.log` (полный вывод подкоманды `support-archive`)
* Диагностические файлы Extension Controller

  + все файлы, находящиеся внутри `/var/lib/dynatrace/remotepluginmodule/log/extensions` в поде Extension Controller

#### Использование

Чтобы создать архив поддержки, выполните следующую команду:

```
kubectl exec -n dynatrace deployment/dynatrace-operator -- dynatrace-operator support-archive --stdout > operator-support-archive.zip
```

Содержимое архива поддержки записывается в `stdout`, что позволяет перенаправить его в ZIP-файл. Прочий вывод отправляется в `stderr` для сохранения целостности файла архива.

Windows PowerShell не поддерживается

В Windows обязательно используйте командную строку (`cmd.exe`); PowerShell не поддерживается.

#### Запуск `support-archive` в отдельном поде

Dynatrace Operator версии 1.0.0+

Если под `operator` не функционирует из-за серьёзных проблем при запуске, можно выполнить команду `support-archive` в отдельном поде с помощью следующей команды. Учтите, что запуск этой команды в отдельном поде рекомендуется только как крайняя мера.

```
kubectl run -n dynatrace support-archive --rm -i --overrides='{ "spec": { "serviceAccount": "dynatrace-operator" }  }' --restart Never --image <operator-image> -- support-archive --delay 10 --stdout > support-archive.zip
```

* Убедитесь, что используете тот же образ, что и под `operator`.
* Параметр `--delay 10` важен, поскольку `kubectl run` обычно пропускает первые несколько строк вывода, что может привести к повреждению архива поддержки.
* Укажите в команде `serviceAccount` как `dynatrace-operator`, так как это позволяет отдельному поду получить доступ ко всем необходимым логам и манифестам Kubernetes, требуемым для сборки архива поддержки. Обратите внимание, что этот метод полагается на то, что ресурсы Dynatrace Operator всё ещё установлены и доступны в кластере.

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

### Отладка проблем конфигурации и мониторинга с помощью расширения Kubernetes Monitoring Statistics

Расширение [Kubernetes Monitoring Statistics](https://dt-url.net/n903xmb) может помочь:

* Устранить неполадки настройки Kubernetes Monitoring
* Устранить неполадки настройки интеграции Prometheus
* Получить подробную аналитику по запросам от Dynatrace к Kubernetes API
* Получать оповещения, когда в настройке мониторинга платформы Kubernetes возникают проблемы
* Получать оповещения о медленном времени отклика вашего Kubernetes API

### Возможные проблемы при изменении режима мониторинга

* Изменение режима мониторинга с `classicFullStack` на `cloudNativeFullStack` влияет на вычисление идентификаторов хостов для отслеживаемых хостов, что приводит к назначению новых идентификаторов и отсутствию связи между старыми и новыми сущностями.
* Чтобы изменить метод мониторинга с `applicationMonitoring` или `cloudNativeFullstack` на `classicFullstack` или `hostMonitoring`, необходимо перезапустить все поды, которые ранее были инструментированы с помощью `applicationMonitoring` или `cloudNativeFullstack`.

### Устранение проблем инъекции в поды с помощью аннотаций пода

Если OneAgent, обогащение метаданными или конфигурация экспортёра OTLP внедряются не так, как ожидалось, проверьте аннотации на затронутом поде, чтобы выяснить, почему инъекция была пропущена.

Следующие аннотации указывают, что вебхук Dynatrace Operator намеренно пропустил инъекцию для пода:

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

#### Причины пропущенной инъекции

См. следующие значения причин, чтобы сузить первопричину.

| Причина | Затронутые компоненты | Описание | Подробности |
| --- | --- | --- | --- |
| `NoBootstrapperConfig` | * OneAgent * Metadata enrichment | Вебхук не может найти или создать секрет конфигурации bootstrapper в пространстве имён пода во время инъекции. | Обычно это происходит, когда согласование DynaKube не завершено или проблемы конфигурации препятствуют согласованию. Секрет конфигурации bootstrapper содержит необходимую конфигурацию (такую как токены) для инъекции CodeModule и обогащения метаданными.  Существует два варианта:  * `<dynakube name>-bootstrapper-config` в пространстве имён Dynatrace Operator (обычно `dynatrace`), который копируется при необходимости. * `dynatrace-bootstrapper-config` в пространстве имён внедрённого пода, который монтируется в под и используется во время инъекции. |
| `NoMutationNeeded` | * OneAgent * Metadata enrichment | Вебхук определяет, что под не требует инъекции. | Обычно это происходит, когда инъекция отключена через аннотации. |
| `OwnerLookupFailed` | * OneAgent * Metadata enrichment * OTLP exporter configuration | Вебхук не может определить владельца пода (имя и тип), который необходим для инъекции. | Обычно это происходит, когда Kubernetes API временно недоступен или медленно отвечает. |
| `MissingTenantUUID` | OneAgent | Согласование DynaKube не завершено, и UUID окружения не был проверен во время инъекции. | Это может произойти во время первоначальной настройки Dynatrace Operator или когда проблемы конфигурации препятствуют согласованию. |
| `DynaKubeStatusNotReady` | OneAgent | Согласование DynaKube не завершено, и статус, связанный с CodeModules, не готов во время инъекции. | Поскольку статус недоступен, вебхук не может определить, какой CodeModule внедрять. |
| `NoOTLPExporterConfigSecret` | OTLP exporter configuration | Вебхук не может найти или создать секрет конфигурации экспортёра OTLP в пространстве имён пода во время инъекции. | Обычно это происходит, когда согласование DynaKube не завершено или проблемы конфигурации препятствуют согласованию.  Существует два варианта:  * `<dynakube name>-otlp-exporter-config` в пространстве имён Dynatrace Operator (исходный секрет). * `dynatrace-otlp-exporter-config` в пространстве имён внедрённого пода, который монтируется в под. |
| `NoOTLPExporterActiveGateCertSecret` | OTLP exporter configuration | Вебхук не может найти или создать секрет сертификата ActiveGate в пространстве имён пода во время инъекции. | Обычно это происходит, когда согласование DynaKube не завершено или проблемы конфигурации препятствуют согласованию. Этот секрет требуется только когда экспортёр OTLP взаимодействует с ActiveGate по TLS.  Существует два варианта:  * `<dynakube name>-otlp-exporter-certs` в пространстве имён Dynatrace Operator (исходный секрет). * `dynatrace-otlp-exporter-certs` в пространстве имён внедрённого пода, который монтируется в под. |
| `IngestEndpointUnavailable` | OTLP exporter configuration | Вебхук не может сформировать корректный URL конечной точки приёма во время инъекции. | Без корректного URL конечной точки приёма конфигурация экспортёра OTLP не может быть внедрена. |