---
title: Развертывание OneAgent Operator в Kubernetes (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy
scraped: 2026-03-06T21:29:44.845264
---

# Развёртывание OneAgent Operator на Kubernetes (устарело)


* Latest Dynatrace
* 10-min read

Эта процедура устарела.

* Если вы выполняете новую установку, вам следует настроить мониторинг Kubernetes с помощью Dynatrace Operator.
* Если у вас уже установлен OneAgent с использованием OneAgent Operator, см. инструкции по миграции на Dynatrace Operator.

## Установка

Ниже описано, как установить и настроить OneAgent.

Развёртывание с помощью kubectl

Развёртывание с помощью Helm

Предварительные требования

* Сгенерируйте [API-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") и [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.") в вашей среде Dynatrace.

  Убедитесь, что для API-токена включена настройка **Access problem and event feed, metrics, and topology**.
* Поды должны разрешать исходящий трафик к вашей среде Dynatrace или Environment ActiveGate для корректной маршрутизации метрик.
* См. Жизненный цикл поддержки для поддерживаемых версий Kubernetes.

1. Создайте необходимые объекты для OneAgent Operator.

   OneAgent Operator работает в отдельном пространстве имён `dynatrace`. Оно содержит развёртывание оператора и все зависимые объекты, такие как разрешения, пользовательские ресурсы и соответствующий DaemonSet. Вы также можете просматривать логи OneAgent Operator.

   ```
   kubectl create namespace dynatrace
   ```

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
   ```

   ```
   kubectl -n dynatrace logs -f deployment/dynatrace-oneagent-operator
   ```
2. Создайте секрет, содержащий API- и PaaS-токены для аутентификации в Dynatrace Cluster.

   Имя секрета важно на последующем этапе при настройке пользовательского ресурса (`.spec.tokens`). В следующем фрагменте кода имя -- `oneagent`. Обязательно замените `API_TOKEN` и `PAAS_TOKEN` значениями, описанными в предварительных требованиях.

   ```
   kubectl -n dynatrace create secret generic oneagent --from-literal="apiToken=API_TOKEN" --from-literal="paasToken=PAAS_TOKEN"
   ```
3. Сохраните пользовательский ресурс.

   Развёртывание Dynatrace OneAgent управляется пользовательским ресурсом типа `OneAgent`. Загрузите файл `cr.yaml` из репозитория GitHub.

   ```
   curl -o cr.yaml https://raw.githubusercontent.com/Dynatrace/dynatrace-oneagent-operator/master/deploy/cr.yaml
   ```
4. Адаптируйте значения пользовательского ресурса, как указано ниже.

   Если вы хотите отменить аргумент, вам нужно **установить его в пустое значение** вместо удаления из пользовательского ресурса.
   Пример:

   ```
   args:


   - "--set-proxy="
   ```

   ### Параметры

   | **Параметр** | **Описание** | **Значение по умолчанию** |
   | --- | --- | --- |
   | `apiUrl` | Обязательно. Для **Dynatrace SaaS**, где OneAgent может подключаться к интернету, замените `ENVIRONMENTID` Dynatrace в `https://ENVIRONMENTID.live.dynatrace.com/api`. Для **Environment ActiveGates** (SaaS или Managed) используйте следующее для загрузки OneAgent, а также для маршрутизации трафика OneAgent через ActiveGate: `https://YourActiveGateIP` или `FQDN:9999/e/<ENVIRONMENTID>/api`. |  |
   | `useUnprivilegedMode` | Опционально. Установите `false`, если хотите пометить под как привилегированный. По умолчанию используются Linux capabilities для пода OneAgent | `true` |
   | `tokens` | Опционально. Имя секрета, содержащего API- и PaaS-токены из предыдущего шага. | Имя пользовательского ресурса (`.metadata.name`), если не задано |
   | `useImmutableImage` | Опционально. Установите `true`, если хотите загрузить Docker-образ OneAgent из вашей среды Dynatrace. Используйте этот параметр вместе с параметром `agentVersion` для управления версией OneAgent. | `false` |
   | `agentVersion` | Опционально. Установите это значение на версию OneAgent в формате семантического версионирования (`major.minor.patch`). Пример: `1.203.0` | последняя версия |
   | `args` | Опционально. Параметры, передаваемые установщику OneAgent. Поддерживаются все параметры командной строки установщика, за исключением `INSTALL_PATH`. |  |
   | `env` | Опционально. Переменные окружения для контейнера OneAgent. |  |
   | `skipCertCheck` | Опционально. Отключение проверки валидации сертификатов для загрузки установщика и коммуникации с API. Установите `true`, если хотите пропустить все проверки валидации сертификатов. | `false` |
   | `nodeSelector` | Опционально. Оставьте пустое значение по умолчанию. Если вы хотите развернуть OneAgent только на определённых узлах, укажите `nodeSelectors` здесь. Подробнее в [документации Kubernetes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector). |  |
   | `tolerations` | Опционально. Оставьте значение по умолчанию для развёртывания OneAgent также на основных узлах, если это возможно. Если вы хотите применить дополнительные tolerations к подам OneAgent для узлов с taint, укажите их здесь. Подробнее в [документации Kubernetes](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/). |  |
   | `image` | Опционально. Определите образ OneAgent. По умолчанию используется общедоступный образ OneAgent на [Docker Hub](https://hub.docker.com/r/dynatrace/oneagent/). Для использования сертифицированного [образа OneAgent](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) из [Red Hat Container Catalog](https://access.redhat.com/containers/) необходимо установить `.spec.image` в `registry.connect.redhat.com/dynatrace/oneagent` в пользовательском ресурсе и указать секреты для извлечения образа, как показано на следующем шаге. | `docker.io/dynatrace/oneagent:latest`, если не задано |
   | `resources` | Опционально. Запросы/лимиты ресурсов для подов OneAgent. Эти настройки сильно зависят от размера рабочих узлов и нагрузок. Настройте в соответствии с вашими потребностями. |  |
   | `priorityClassName` | Опционально. Класс приоритета для пода OneAgent. См. [документацию Kubernetes](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/). |  |
   | `disableAgentUpdate` | Опционально. Отключение функции автообновления OneAgent подов оператором. | `false` |
   | `enableIstio` | Опционально. Включение управления записями Istio service entries и virtual services для эндпоинтов Dynatrace, чтобы разрешить исходящий трафик мониторинга OneAgent к вашей среде Dynatrace. | `false` |
   | `trustedCAs` | Опционально. Добавление предоставленных CA-сертификатов к оператору и OneAgent; укажите имя configmap, содержащей ваш PEM в поле с именем `certs`. | Если не задано, используются встроенные сертификаты по умолчанию в образах. |

   Конфигурация для Anthos, SUSE CaaS, GKE, IKS и TKGI

   Для Anthos, SUSE CaaS, Google Kubernetes Engine и VMware Tanzu Kubernetes Grid Integrated Edition (ранее PKE) необходимо добавить следующие дополнительные параметры в секцию `env` файла `cr.yaml`:

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
6. Опционально. Настройте прокси.

   * Вы можете настроить дополнительные параметры, такие как настройки прокси, в файле `cr.yaml` для:

     + загрузки установщика OneAgent
     + обеспечения коммуникации между OneAgent и вашей средой Dynatrace
     + обеспечения коммуникации между Dynatrace OneAgent Operator и API Dynatrace.

   Есть два способа указать прокси, в зависимости от того, использует ли ваш прокси учётные данные или нет.

   Без учётных данных

   Если у вас есть прокси, который не использует учётные данные, введите URL прокси напрямую в поле `value`.

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

   Если ваш прокси использует учётные данные

   1. Создайте секрет с полем `proxy`, содержащим ваш зашифрованный URL прокси с учётными данными.
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
7. Опционально. Настройте сетевые зоны.

   Вы можете настроить сетевые зоны, установив следующий аргумент:

   ```
   args:


   - --set-network-zone=<your.network.zone>
   ```

   Подробнее см. Сетевые зоны.

Предварительные требования

* Сгенерируйте [API-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") и [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.") в вашей среде Dynatrace.

  Убедитесь, что для API-токена включена настройка **Access problem and event feed, metrics, and topology**.
* Поды должны разрешать исходящий трафик к вашей среде Dynatrace или Environment ActiveGate для корректной маршрутизации метрик.
* См. Жизненный цикл поддержки для поддерживаемых версий Kubernetes.
* [Установите Helm версии 3](https://helm.sh/docs/intro/install/).

1. Добавьте Helm-репозиторий Dynatrace OneAgent.

   ```
   helm repo add dynatrace \


   https://raw.githubusercontent.com/Dynatrace/helm-charts/master/repos/stable
   ```
2. Создайте пространство имён Dynatrace.

   Dynatrace OneAgent Operator работает в отдельном пространстве имён под названием **dynatrace**, которое содержит развёртывание оператора и все зависимые объекты, такие как разрешения, пользовательские ресурсы и соответствующие DaemonSets.

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

   Настройка прокси OneAgent используется как оператором, так и контейнерами OneAgent при коммуникации со средой Dynatrace.

   Конфигурация для Anthos, SUSE CaaS, GKE, IKS и TKGI

   Для Anthos, SUSE CaaS, Google Kubernetes Engine и VMware Tanzu Kubernetes Grid Integrated Edition (ранее PKE) необходимо добавить следующие дополнительные параметры в секцию `env` файла `values.yaml`:

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
5. Опционально. Настройте сетевые зоны.

   Вы можете настроить сетевые зоны, установив следующий аргумент:

   ```
   args:


   - --set-network-zone=<your.network.zone>
   ```

   Подробнее см. Сетевые зоны.
6. Для применения параметров YAML выполните следующую команду:

   ```
   helm install dynatrace-oneagent-operator \


   dynatrace/dynatrace-oneagent-operator -n\


   dynatrace --values values.yaml
   ```

После развёртывания необходимо перезапустить ваши поды, чтобы OneAgent мог внедриться в них.

## Разрешения на уровне кластера

В следующей таблице показаны разрешения, необходимые для OneAgent Operator.

| **Доступные ресурсы** | **Используемые API** | **Имена ресурсов** |
| --- | --- | --- |
| `Nodes` | Get/List/Watch | - |
| `Namespaces` | Get/List/Watch | - |
| `Secrets` | Create | - |
| `Secrets` | Get/Update/Delete | `dynatrace-oneagent-config`, `dynatrace-oneagent-pull-secret` |

## Ограничения

Подробнее см. Ограничения Docker.

## Устранение неполадок

Узнайте, как устранить проблемы, которые могут возникнуть при развёртывании OneAgent на Kubernetes.

## Развёртывание ActiveGate и подключение Kubernetes API к Dynatrace

Теперь, когда у вас есть OneAgent, работающий на ваших узлах Kubernetes, вы можете мониторить эти узлы и приложения, работающие в Kubernetes. Следующий шаг -- развернуть ActiveGate и подключить Kubernetes API к Dynatrace, чтобы получать нативные метрики Kubernetes, такие как лимиты запросов и разницу между запрошенными и работающими подами.
Дальнейшие инструкции см. в Развёртывание ActiveGate в Kubernetes как StatefulSet.

## Обновление OneAgent Operator с помощью kubectl

OneAgent Operator (для Kubernetes версии 1.9+) автоматически управляет жизненным циклом развёрнутых OneAgents, поэтому вам не нужно обновлять поды OneAgent самостоятельно.

Просмотрите [примечания к выпуску](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases) оператора на предмет критических изменений в пользовательском ресурсе.

Если пользовательский ресурс новой версии совместим с уже развёрнутой версией, вы можете просто установить образ OneAgent Operator на новую версию с тегом. Обязательно замените `vX.Y.Z` на новую версию в следующей команде:

```
kubectl -n dynatrace set image deployment \


dynatrace-oneagent-operator *=quay.io/dynatrace/\


dynatrace-oneagent-operator:vX.Y.Z
```

Версия образа OneAgent Operator не зависит от версии OneAgent. Чтобы проверить доступные версии оператора, см. [Выпуски OneAgent Operator](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases).

Для обновления OneAgent Operator выполните следующую команду:

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
```

## Обновление OneAgent Operator с помощью Helm

1. Обновите ваши Helm-репозитории.

   ```
   helm repo update
   ```

   Другой способ обновления Helm-репозитория Dynatrace OneAgent -- добавить его повторно, что перезапишет старую версию.
2. Обновите OneAgent до последней версии.

   Не пропускайте флаг `--reuse-values` в команде, чтобы сохранить вашу конфигурацию.

   ```
   helm upgrade dynatrace-oneagent-operator dynatrace/\


   dynatrace-oneagent-operator -n dynatrace --reuse-values
   ```

## Удаление OneAgent Operator

Удаление с помощью kubectl

Удаление с помощью Helm

Чтобы удалить OneAgent Operator из Kubernetes версии 1.9+

1. Удалите пользовательские ресурсы OneAgent и очистите все оставшиеся объекты, специфичные для OneAgent Operator.

   ```
   kubectl delete -n dynatrace oneagent --all


   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
   ```
2. Опционально. После удаления OneAgent Operator бинарный файл OneAgent остаётся на узле в неактивном состоянии. Чтобы полностью его удалить, запустите скрипт `uninstall.sh` и удалите логи и файлы конфигурации.
   См. Информация по Linux.

Удалите пользовательские ресурсы OneAgent и очистите все оставшиеся объекты, специфичные для OneAgent Operator:

```
helm uninstall dynatrace-oneagent-operator -n dynatrace
```

## Связанные темы

* Kubernetes Classic
* Хранение образов Dynatrace в частных реестрах
* Миграция Dynatrace Operator в новую среду
