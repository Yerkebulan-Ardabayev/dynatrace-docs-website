---
title: Развёртывание OneAgent Operator на Kubernetes (устаревшее)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy
scraped: 2026-05-12T11:52:16.378423
---

# Развёртывание OneAgent Operator на Kubernetes (устаревшее)

# Развёртывание OneAgent Operator на Kubernetes (устаревшее)

* Чтение: 10 мин
* Опубликовано 26 мая 2020 г.

Эта процедура устарела.

* При новой установке используйте [настройку мониторинга Kubernetes с помощью Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").
* Если OneAgent уже установлен с помощью OneAgent Operator, см. [инструкции по миграции на Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Подробные инструкции по миграции с устаревшего OneAgent Operator на Dynatrace Operator с помощью kubectl/oc").

## Установка

Ниже описано, как установить и настроить OneAgent.

Развёртывание с kubectl

Развёртывание с Helm

Предварительные требования

* Создайте [токен API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях видимости.") и [токен PaaS](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.") в среде Dynatrace.

  Убедитесь, что для токена API включён параметр **Access problem and event feed, metrics, and topology**.
* Поды должны разрешать исходящий трафик к среде Dynatrace или к Environment ActiveGate, чтобы маршрутизация метрик работала корректно.
* Поддерживаемые версии Kubernetes см. в разделе [Жизненный цикл поддержки](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы").

1. Создайте необходимые объекты для OneAgent Operator.

   OneAgent Operator работает в отдельном пространстве имён `dynatrace`. В нём хранятся развёртывание оператора и все зависимые объекты: разрешения, пользовательские ресурсы и соответствующий DaemonSet. Там же доступны журналы OneAgent Operator.

   ```
   kubectl create namespace dynatrace
   ```

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
   ```

   ```
   kubectl -n dynatrace logs -f deployment/dynatrace-oneagent-operator
   ```
2. Создайте секрет с токенами API и PaaS для аутентификации в кластере Dynatrace.

   Имя секрета понадобится позднее при настройке пользовательского ресурса (`.spec.tokens`). В приведённом фрагменте кода имя секрета `oneagent`. Замените `API_TOKEN` и `PAAS_TOKEN` на значения, указанные в предварительных требованиях.

   ```
   kubectl -n dynatrace create secret generic oneagent --from-literal="apiToken=API_TOKEN" --from-literal="paasToken=PAAS_TOKEN"
   ```
3. Сохраните пользовательский ресурс.

   Развёртывание Dynatrace OneAgent управляется пользовательским ресурсом типа `OneAgent`. Получите файл `cr.yaml` из репозитория GitHub.

   ```
   curl -o cr.yaml https://raw.githubusercontent.com/Dynatrace/dynatrace-oneagent-operator/master/deploy/cr.yaml
   ```
4. Настройте значения пользовательского ресурса согласно описанию ниже.

   Чтобы отменить аргумент, необходимо **задать ему пустое значение**, а не удалять его из пользовательского ресурса.
   Пример:

   ```
   args:



   - "--set-proxy="
   ```

   ### Параметры

   | **Параметр** | **Описание** | **Значение по умолчанию** |
   | --- | --- | --- |
   | `apiUrl` | Обязательный. Для **Dynatrace SaaS**, где OneAgent подключается к интернету, замените `ENVIRONMENTID` в строке `https://ENVIRONMENTID.live.dynatrace.com/api`. Для **Environment ActiveGate** (SaaS или Managed) используйте следующий адрес для загрузки OneAgent и передачи трафика через ActiveGate: `https://YourActiveGateIP` или `FQDN:9999/e/<ENVIRONMENTID>/api`. |  |
   | `useUnprivilegedMode` | Необязательный. Установите `false`, чтобы назначить поду привилегированный режим. По умолчанию используются [возможности Linux для пода OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux.") | `true` |
   | `tokens` | Необязательный. Имя секрета с токенами API и PaaS, указанными выше. | Имя пользовательского ресурса (`.metadata.name`), если не задано |
   | `useImmutableImage` | Необязательный. Установите `true`, чтобы загружать образ Docker для OneAgent из среды Dynatrace. Используйте вместе с параметром `agentVersion` для управления версией OneAgent. | `false` |
   | `agentVersion` | Необязательный. Укажите версию OneAgent в формате семантического версионирования (`major.minor.patch`). Пример: `1.203.0` | последняя версия |
   | `args` | Необязательный. Параметры, передаваемые установщику OneAgent. Поддерживаются все [параметры командной строки установщика](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки."), за исключением `INSTALL_PATH`. |  |
   | `env` | Необязательный. Переменные среды для контейнера OneAgent. |  |
   | `skipCertCheck` | Необязательный. Отключает проверку сертификатов при загрузке установщика и взаимодействии по API. Установите `true`, чтобы пропустить проверку. | `false` |
   | `nodeSelector` | Необязательный. Оставьте пустое значение по умолчанию. Чтобы развернуть OneAgent только на определённых узлах, укажите здесь `nodeSelectors`. Подробнее см. в [документации Kubernetes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector). |  |
   | `tolerations` | Необязательный. Оставьте значение по умолчанию, чтобы при возможности развернуть OneAgent на основных узлах. Чтобы добавить tolerations для подов OneAgent на узлах с taint, укажите их здесь. Подробнее см. в [документации Kubernetes](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/). |  |
   | `image` | Необязательный. Задаёт образ OneAgent. По умолчанию используется публично доступный образ на [Docker Hub](https://hub.docker.com/r/dynatrace/oneagent/). Чтобы использовать сертифицированный [образ OneAgent](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) из [Red Hat Container Catalog](https://access.redhat.com/containers/), задайте `.spec.image` значение `registry.connect.redhat.com/dynatrace/oneagent` в пользовательском ресурсе и укажите секреты для загрузки образа, как показано в следующем шаге. | `docker.io/dynatrace/oneagent:latest`, если не задано |
   | `resources` | Необязательный. Запросы и ограничения ресурсов для подов OneAgent. Значения существенно зависят от размера рабочих узлов и нагрузки. Настройте под свои требования. |  |
   | `priorityClassName` | Необязательный. Класс приоритета для пода OneAgent. Подробнее см. в [документации Kubernetes](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/). |  |
   | `disableAgentUpdate` | Необязательный. Отключает автоматическое обновление подов OneAgent оператором. | `false` |
   | `enableIstio` | Необязательный. Включает управление записями сервисов и виртуальными сервисами Istio для конечных точек Dynatrace, чтобы разрешить исходящий трафик мониторинга OneAgent к среде Dynatrace. | `false` |
   | `trustedCAs` | Необязательный. Добавляет указанные CA-сертификаты в Operator и OneAgent; укажите имя ConfigMap, в котором ваш PEM хранится в поле `certs`. | Если не задано, используются встроенные сертификаты образов. |

   Конфигурация для Anthos, SUSE CaaS, GKE, IKS и TKGI

   Для Anthos, SUSE CaaS, Google Kubernetes Engine и VMware Tanzu Kubernetes Grid Integrated Edition (ранее PKE) необходимо добавить следующие дополнительные параметры в раздел `env` файла `cr.yaml`:

   Anthos и GKE

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"
   ```

   TKGI

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /var/vcap/store
   ```

   IKS

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /opt
   ```

   SUSE CaaS

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"
   ```
5. Создайте пользовательский ресурс.

   ```
   kubectl apply -f cr.yaml
   ```
6. Необязательно. Настройте прокси.

   * В файле `cr.yaml` можно настроить дополнительные параметры, например настройки прокси, чтобы:

     + загрузить установщик OneAgent;
     + обеспечить связь между OneAgent и средой Dynatrace;
     + обеспечить связь между Dynatrace OneAgent Operator и Dynatrace API.

   Существует два способа задать прокси в зависимости от того, требует ли прокси аутентификации.

   Без учётных данных

   Если прокси не требует аутентификации, укажите URL прокси непосредственно в поле `value`.

   **Пример**

   ```
   apiVersion: dynatrace.com/v1alpha1



   kind: OneAgent



   metadata:



   name: oneagent



   namespace: dynatrace



   spec:



   apiUrl: https://environmentid.dynatrace.com/api



   tolerations:



   - effect: NoSchedule



   key: node-role.kubernetes.io/master



   operator: Exists



   args: []



   enableIstio: true



   proxy:



   value: http://mysuperproxy
   ```

   С учётными данными

   Если прокси требует аутентификации

   1. Создайте секрет с полем `proxy`, содержащим зашифрованный URL прокси с учётными данными.
      Пример.

      ```
      kubectl -n dynatrace create secret generic myproxysecret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
      ```
   2. Укажите имя секрета в разделе `valueFrom`.
      Пример.

      ```
      apiVersion: dynatrace.com/v1alpha1



      kind: OneAgent



      metadata:



      name: oneagent



      namespace: dynatrace



      spec:



      apiUrl: https://environmentid.dynatrace.com/api



      tolerations:



      - effect: NoSchedule



      key: node-role.kubernetes.io/master



      operator: Exists



      args: []



      enableIstio: true



      proxy:



      valueFrom: myproxysecret
      ```
7. Необязательно. Настройте сетевые зоны.

   Сетевые зоны настраиваются с помощью следующего аргумента:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

Предварительные требования

* Создайте [токен API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях видимости.") и [токен PaaS](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.") в среде Dynatrace.

  Убедитесь, что для токена API включён параметр **Access problem and event feed, metrics, and topology**.
* Поды должны разрешать исходящий трафик к среде Dynatrace или к Environment ActiveGate, чтобы маршрутизация метрик работала корректно.
* Поддерживаемые версии Kubernetes см. в разделе [Жизненный цикл поддержки](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы").
* [Установите Helm версии 3](https://helm.sh/docs/intro/install/).

1. Добавьте репозиторий Helm для Dynatrace OneAgent.

   ```
   helm repo add dynatrace \



   https://raw.githubusercontent.com/Dynatrace/helm-charts/master/repos/stable
   ```
2. Создайте пространство имён Dynatrace.

   Dynatrace OneAgent Operator работает в отдельном пространстве имён **dynatrace**, в котором хранятся развёртывание оператора и все зависимые объекты: разрешения, пользовательские ресурсы и соответствующие DaemonSet.

   ```
   kubectl create namespace dynatrace
   ```
3. Создайте определения пользовательских ресурсов.

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagents.yaml



kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagentapms.yaml
```

4. Создайте файл `values.yaml` со следующим содержимым.

   ```
   platform: "kubernetes"



   operator:



   image: ""



   oneagent:



   name: "oneagent"



   apiUrl: "https://ENVIRONMENTID.live.dynatrace.com/api"



   image: ""



   args: {}



   env: {}



   nodeSelector: {}



   labels: {}



   skipCertCheck: false



   disableAgentUpdate: false



   enableIstio: false



   dnsPolicy: ""



   resources: {}



   waitReadySeconds: null



   priorityClassName: ""



   serviceAccountName: ""



   proxy: ""



   trustedCAs: ""



   secret:



   apiToken: "DYNATRACE_API_TOKEN"



   paasToken: "PLATFORM_AS_A_SERVICE_TOKEN"
   ```

   Настройка прокси для OneAgent используется как оператором, так и контейнерами OneAgent при взаимодействии со средой Dynatrace.

   Конфигурация для Anthos, SUSE CaaS, GKE, IKS и TKGI

   Для Anthos, SUSE CaaS, Google Kubernetes Engine и VMware Tanzu Kubernetes Grid Integrated Edition (ранее PKE) необходимо добавить следующие дополнительные параметры в раздел `env` файла `values.yaml`:

   Anthos, SUSE CaaS и GKE

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"
   ```

   TKGI

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /var/vcap/store
   ```

   IKS

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /opt
   ```
5. Необязательно. Настройте сетевые зоны.

   Сетевые зоны настраиваются с помощью следующего аргумента:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").
6. Чтобы применить параметры YAML, выполните следующую команду:

   ```
   helm install dynatrace-oneagent-operator \



   dynatrace/dynatrace-oneagent-operator -n\



   dynatrace --values values.yaml
   ```

После развёртывания необходимо перезапустить поды, чтобы OneAgent мог внедриться в них.

## Разрешения на уровне кластера

В следующей таблице показаны разрешения, необходимые для OneAgent Operator.

| **Доступные ресурсы** | **Используемые API** | **Имена ресурсов** |
| --- | --- | --- |
| `Nodes` | Get/List/Watch | - |
| `Namespaces` | Get/List/Watch | - |
| `Secrets` | Create | - |
| `Secrets` | Get/Update/Delete | `dynatrace-oneagent-config`, `dynatrace-oneagent-pull-secret` |

## Известные ограничения

Подробнее см. в разделе [Ограничения Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker.").

## Устранение неполадок

Узнайте, как [устранять проблемы](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting#deploy "Эта страница поможет вам справиться с трудностями, которые могут возникнуть при работе с Dynatrace Operator и его компонентами."), которые могут возникнуть при развёртывании OneAgent на Kubernetes.

## Развёртывание ActiveGate и подключение Kubernetes API к Dynatrace

Теперь, когда OneAgent запущен на узлах Kubernetes, можно отслеживать эти узлы и приложения, работающие в Kubernetes. Следующий шаг: развернуть ActiveGate и подключить Kubernetes API к Dynatrace, чтобы получать нативные метрики Kubernetes, например ограничения запросов и расхождение между запрошенными и работающими подами.
Дополнительные инструкции см. в разделе [Развёртывание ActiveGate в Kubernetes как StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet.").

## Обновление OneAgent Operator с помощью kubectl

OneAgent Operator (для Kubernetes версии 1.9+) автоматически управляет жизненным циклом развёрнутых экземпляров OneAgent, поэтому обновлять поды OneAgent вручную не требуется.

Изучите [примечания к выпуску](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases) оператора на предмет несовместимых изменений в пользовательском ресурсе.

Если пользовательский ресурс новой версии совместим с уже развёрнутой, достаточно указать новый тегированный образ для OneAgent Operator. Замените `vX.Y.Z` на новую версию в следующей команде:

```
kubectl -n dynatrace set image deployment \



dynatrace-oneagent-operator *=quay.io/dynatrace/\



dynatrace-oneagent-operator:vX.Y.Z
```

Версия образа OneAgent Operator не зависит от версии OneAgent. Доступные версии оператора см. в [выпусках OneAgent Operator](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases).

Для обновления OneAgent Operator выполните следующую команду:

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
```

## Обновление OneAgent Operator с помощью Helm

1. Обновите репозитории Helm.

   ```
   helm repo update
   ```

   Альтернативный способ обновления репозитория Helm для Dynatrace OneAgent: добавить его повторно, что перезапишет устаревшую версию.
2. Обновите OneAgent до последней версии.

   Не опускайте флаг `--reuse-values` в команде, чтобы сохранить текущую конфигурацию.

   ```
   helm upgrade dynatrace-oneagent-operator dynatrace/\



   dynatrace-oneagent-operator -n dynatrace --reuse-values
   ```

## Удаление OneAgent Operator

Удаление с помощью kubectl

Удаление с помощью Helm

Для удаления OneAgent Operator из Kubernetes версии 1.9+

1. Удалите пользовательские ресурсы OneAgent и очистите все оставшиеся объекты OneAgent Operator.

   ```
   kubectl delete -n dynatrace oneagent --all



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
   ```
2. Необязательно. После удаления OneAgent Operator бинарный файл OneAgent остаётся на узле в неактивном состоянии. Для полного удаления выполните скрипт `uninstall.sh` и удалите журналы и файлы конфигурации.
   См. раздел [Информация для Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Узнайте, как удалить OneAgent из вашей системы на базе Linux.").

Удалите пользовательские ресурсы OneAgent и очистите все оставшиеся объекты OneAgent Operator:

```
helm uninstall dynatrace-oneagent-operator -n dynatrace
```

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")
* [Хранение образов Dynatrace в приватных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах")
* [Миграция Dynatrace Operator в новую среду](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant "Перенесите мониторинг в новое окружение Dynatrace в кластерах Kubernetes.")