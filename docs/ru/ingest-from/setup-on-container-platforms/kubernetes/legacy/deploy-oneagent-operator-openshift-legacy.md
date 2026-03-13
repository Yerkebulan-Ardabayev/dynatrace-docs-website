---
title: Развёртывание OneAgent Operator на OpenShift (устарело)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy
scraped: 2026-03-06T21:32:01.892064
---

# Развёртывание OneAgent Operator на OpenShift (устарело)

# Развёртывание OneAgent Operator на OpenShift (устарело)

* Последняя Dynatrace
* 10 мин. чтения
* Опубликовано 26 мая 2020 г.

Эта процедура устарела.

* Если вы выполняете новую установку, следует [настроить мониторинг OpenShift с помощью Dynatrace Operator](../../../setup-on-k8s/deployment.md "Развёртывание Dynatrace Operator на Kubernetes").
* Если у вас уже установлен OneAgent с помощью OneAgent Operator, см. [инструкции по миграции на Dynatrace Operator](../../../setup-on-k8s/guides/migration/migrate-to-dto.md "Подробные инструкции по миграции с устаревшего OneAgent Operator на Dynatrace Operator с помощью kubectl/oc").

Инструкции ниже также применимы к **OpenShift Dedicated**. Для OpenShift Dedicated вам потребуются [привилегии cluster-admin](https://docs.openshift.com/dedicated/4/administering_a_cluster/cluster-admin-role.html).

## Установка

Ниже описано, как установить и настроить OneAgent.

Развёртывание с oc

Развёртывание с Helm

Предварительные требования

* Сгенерируйте [API-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях.") и [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях.") в вашей среде Dynatrace.

  Убедитесь, что для API-токена включена настройка **Access problem and event feed, metrics, and topology**.
* Поды должны разрешать исходящий трафик к вашей среде Dynatrace или к вашему Environment ActiveGate для корректной маршрутизации метрик.
* См. [Жизненный цикл поддержки](../../../technology-support/support-model-and-issues.md "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, и известные проблемы") для поддерживаемых версий OpenShift.

1. Добавьте новый проект.

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. OCP версии 3.11 Предоставьте секреты для доступа к образам.
   Пропустите этот шаг, если используете более позднюю версию.
   Для использования сертифицированных образов [OneAgent Operator](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/dynatrace-oneagent-operator) и [OneAgent](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) из [Red Hat Container Catalog](https://access.redhat.com/containers/) (RHCC) необходимо [предоставить секреты для доступа к образам](https://access.redhat.com/documentation/en-us/openshift_container_platform/3.9/html/developer_guide/dev-guide-managing-images#pulling-private-registries-delegated-auth). ServiceAccount'ы в манифесте `openshift.yaml` уже имеют ссылки на создаваемые ниже секреты.

   ```
   # Для OCP 3.11



   oc -n dynatrace create secret docker-registry redhat-connect --docker-server=registry.connect.redhat.com --docker-username=REDHAT_CONNECT_USERNAME --docker-password=REDHAT_CONNECT_PASSWORD --docker-email=unused



   oc -n dynatrace create secret docker-registry redhat-connect-sso --docker-server=sso.redhat.com --docker-username=REDHAT_CONNECT_USERNAME --docker-password=REDHAT_CONNECT_PASSWORD --docker-email=unused
   ```
3. OCP версии 4.x OCP версии 3.11 Примените манифест `openshift.yaml` для развёртывания OneAgent Operator.

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/openshift.yaml



   oc -n dynatrace logs -f deployment/dynatrace-oneagent-operator
   ```

   Для версий OpenShift **ранее 3.11.188** необходимо **удалить строку** `type: object` **под обязательной валидацией spec в** `openshift.yaml` **перед развёртыванием** `CustomResourceDefinition` ([известная ошибка OpenShift](https://github.com/openshift/origin/pull/24540)).

   ```
   required:



   -  spec



   type: object  # удалите эту строку — это правило валидации
   ```
4. Создайте секрет с API- и PaaS-токенами для аутентификации в Dynatrace Cluster.
   Имя секрета понадобится на более позднем этапе при настройке пользовательского ресурса (`.spec.tokens`). В следующем примере имя — `oneagent`. Обязательно замените `API_TOKEN` и `PAAS_TOKEN` значениями из предварительных требований.

   ```
   oc -n dynatrace create secret generic oneagent --from-literal="apiToken=API_TOKEN" --from-literal="paasToken=PAAS_TOKEN"
   ```
5. Сохраните пользовательский ресурс.
   Развёртывание Dynatrace OneAgent управляется пользовательским ресурсом типа `OneAgent`. Загрузите файл `cr.yaml` из репозитория GitHub.

   ```
   curl -o cr.yaml https://raw.githubusercontent.com/Dynatrace/dynatrace-oneagent-operator/master/deploy/cr.yaml
   ```
6. Адаптируйте пользовательский ресурс.

   Если вы хотите отменить аргумент, нужно **установить его в пустое значение**, а не удалять из пользовательского ресурса.
   Пример:

   ```
   args:



   - "--set-proxy="
   ```

### Параметры

| **Параметр** | **Описание** | **Значение по умолчанию** |
| --- | --- | --- |
| `apiUrl` | Обязательный Для **Dynatrace SaaS**, где OneAgent может подключиться к интернету, замените `ENVIRONMENTID` в `https://ENVIRONMENTID.live.dynatrace.com/api`. Для **Environment ActiveGates** (SaaS или Managed) используйте: `https://YourActiveGateIP` или `FQDN:9999/e/<ENVIRONMENTID>/api`. |  |
| `useUnprivilegedMode` | Необязательный Установите `false`, если хотите пометить под как привилегированный. По умолчанию используются [возможности Linux для пода OneAgent](../../../dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged.md "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux.") | `true` |
| `tokens` | Необязательный Имя секрета с API- и PaaS-токенами. | Имя пользовательского ресурса (`.metadata.name`), если не задано |
| `useImmutableImage` | Необязательный Установите `true`, если хотите загружать образ Docker OneAgent из вашей среды Dynatrace. Используйте вместе с `agentVersion`. | `false` |
| `agentVersion` | Необязательный Версия OneAgent в семантическом формате (`major.minor.patch`). Пример: `1.203.0` | последняя версия |
| `args` | Необязательный Параметры для установщика OneAgent. Поддерживаются все [параметры командной строки установщика](../../../dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux.md "Узнайте, как использовать установщик Linux с параметрами командной строки."), за исключением `INSTALL_PATH`. |  |
| `env` | Необязательный Переменные среды для контейнера OneAgent. |  |
| `skipCertCheck` | Необязательный Отключить проверку сертификатов для загрузки установщика и коммуникации с API. Установите `true` для пропуска проверок. | `false` |
| `nodeSelector` | Необязательный Оставьте пустым. Если хотите развернуть OneAgent на определённых узлах, укажите `nodeSelectors` здесь. См. [документацию Kubernetes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector). |  |
| `tolerations` | Необязательный Оставьте по умолчанию для развёртывания OneAgent на мастер-узлах. Для дополнительных tolerations для tainted-узлов укажите их здесь. См. [документацию Kubernetes](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/). |  |
| `image` | Необязательный Образ OneAgent. По умолчанию — общедоступный образ на [Docker Hub](https://hub.docker.com/r/dynatrace/oneagent/). Для сертифицированного [образа OneAgent](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) из [Red Hat Container Catalog](https://access.redhat.com/containers/) установите `.spec.image` как `registry.connect.redhat.com/dynatrace/oneagent` и предоставьте секреты доступа. | `docker.io/dynatrace/oneagent:latest`, если не задано |
| `resources` | Необязательный Запросы/лимиты ресурсов для подов OneAgent. Зависят от размера рабочих узлов и нагрузок. Настройте под свои потребности. |  |
| `priorityClassName` | Необязательный Класс приоритета для пода OneAgent. См. [документацию Kubernetes](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/). |  |
| `disableAgentUpdate` | Необязательный Отключить автообновление OneAgent. | `false` |
| `enableIstio` | Необязательный Включить управление записями сервисов Istio и виртуальными сервисами для конечных точек Dynatrace | `false` |
| `trustedCAs` | Необязательный Имя ConfigMap с пользовательскими CA-сертификатами. ConfigMap должен содержать поле `certs` с содержимым PEM-пакета. | Если не задано, используются встроенные сертификаты образов. |

7. Создайте пользовательский ресурс.

   ```
   oc apply -f cr.yaml
   ```
8. Необязательно Настройте прокси.

   * Вы можете настроить дополнительные параметры, такие как прокси, в файле `cr.yaml` для:

     + загрузки установщика OneAgent
     + обеспечения коммуникации между OneAgent и вашей средой Dynatrace
     + обеспечения коммуникации между Dynatrace OneAgent Operator и Dynatrace API.

   Есть два способа указать прокси, в зависимости от того, использует ли ваш прокси учётные данные.

   Без учётных данных

   Если у вас прокси без учётных данных, введите URL прокси непосредственно в поле `value`.

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

   1. Создайте секрет с полем `proxy`, содержащим зашифрованный URL прокси с учётными данными.
      Пример.

      ```
      oc -n dynatrace create secret generic myproxysecret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
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
9. Необязательно Настройте сетевые зоны.

   Вы можете настроить сетевые зоны, установив следующий аргумент:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   См. [сетевые зоны](../../../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.") для получения дополнительной информации.

Предварительные требования

* Сгенерируйте [API-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях.") и [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях.") в вашей среде Dynatrace.

  Убедитесь, что для API-токена включена настройка **Access problem and event feed, metrics, and topology**.
* Поды должны разрешать исходящий трафик к вашей среде Dynatrace или к вашему Environment ActiveGate для корректной маршрутизации метрик.
* См. [Жизненный цикл поддержки](../../../technology-support/support-model-and-issues.md "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, и известные проблемы") для поддерживаемых версий OpenShift.
* [Установите Helm версии 3](https://helm.sh/docs/intro/install/).
* Мы рекомендуем устанавливать **последнюю версию** Helm chart.

1. Добавьте новый проект `dynatrace`.

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Добавьте Helm-репозиторий Dynatrace OneAgent.

   ```
   helm repo add dynatrace \



   https://raw.githubusercontent.com/Dynatrace/helm-charts/master/repos/stable
   ```
3. Создайте определения пользовательских ресурсов (CRD).

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagents.yaml



   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagentapms.yaml
   ```

   Для OCP версии 3.11 выполните следующие команды.

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagents-v1beta1.yaml



   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagentapms-v1beta1.yaml
   ```
4. Создайте файл `values.yaml` со следующим содержимым.

   ```
   platform: "openshift"



   operator:



   image: ""



   oneagent:



   name: "oneagent"



   apiUrl: "https://ENVIRONMENTID.live.dynatrace.com/api"



   image: ""



   args: []



   env: []



   nodeSelector: []



   labels: []



   skipCertCheck: false



   disableAgentUpdate: false



   enableIstio: false



   dnsPolicy: ""



   resources: []



   waitReadySeconds: null



   priorityClassName: ""



   serviceAccountName: ""



   proxy: ""



   trustedCAs: ""



   secret:



   apiToken: "DYNATRACE_API_TOKEN"



   paasToken: "PLATFORM_AS_A_SERVICE_TOKEN"
   ```
5. Необязательно Настройте сетевые зоны.

   Вы можете настроить сетевые зоны, установив следующий аргумент:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   См. [сетевые зоны](../../../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.") для получения дополнительной информации.

   Для версий OpenShift **ранее 3.11.188** необходимо **удалить строку** `type: object` **под обязательной валидацией spec в** `openshift.yaml` **перед развёртыванием** `CustomResourceDefinition` ([известная ошибка OpenShift](https://github.com/openshift/origin/pull/24540)).

   ```
   required:



   -  spec



   type: object  # удалите эту строку — это правило валидации
   ```
6. Для применения параметров YAML выполните следующую команду:

   ```
   helm install dynatrace-oneagent-operator \



   dynatrace/dynatrace-oneagent-operator -n\



   dynatrace --disable-openapi-validation --values values.yaml
   ```

После развёртывания необходимо перезапустить поды, чтобы OneAgent мог внедриться в них.

## Разрешения уровня кластера

В следующей таблице показаны разрешения, необходимые для OneAgent Operator.

| **Ресурсы** | **Используемые API** | **Имена ресурсов** |
| --- | --- | --- |
| `Nodes` | Get/List/Watch | - |
| `Namespaces` | Get/List/Watch | - |
| `Secrets` | Create | - |
| `Secrets` | Get/Update/Delete | `dynatrace-oneagent-config`, `dynatrace-oneagent-pull-secret` |

## Ограничения

См. [ограничения Docker](../../docker/set-up-dynatrace-oneagent-as-docker-container.md#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker.") для подробностей.

## Устранение неполадок

Узнайте, как [устранить неполадки](../../../setup-on-k8s/deployment/troubleshooting.md#deploy "Эта страница поможет вам справиться с проблемами при развёртывании Dynatrace Operator."), которые могут возникнуть при развёртывании OneAgent на OpenShift.

## Развёртывание ActiveGate и подключение Kubernetes API к Dynatrace

Теперь, когда OneAgent работает на узлах OpenShift, вы можете мониторить эти узлы и приложения, работающие в OpenShift. Следующий шаг — развернуть ActiveGate и подключить Kubernetes API к Dynatrace для получения нативных метрик Kubernetes, таких как лимиты запросов и разница между запрошенными и работающими подами.
Для дальнейших инструкций см. [Развёртывание ActiveGate в OpenShift как StatefulSet](../../../setup-on-k8s/deployment/other/ag-statefulset.md "Установка и настройка ActiveGate в Kubernetes как StatefulSet.").

## Обновление OneAgent Operator с помощью oc

OneAgent Operator для OpenShift версии 3.9+ автоматически управляет жизненным циклом развёрнутых OneAgent, поэтому вам не нужно обновлять поды OneAgent самостоятельно.

Ознакомьтесь с [примечаниями к выпуску](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases) Operator на предмет критических изменений пользовательского ресурса.

Для обновления OneAgent Operator выполните следующую команду:

```
oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/openshift.yaml
```

## Обновление OneAgent Operator с помощью Helm

1. Обновите ваши Helm-репозитории.

   ```
   helm repo update
   ```

   Альтернативный метод: добавьте заново. Это перезапишет старую версию.
2. Обновите OneAgent до последней версии.

   Не пропускайте флаг `--reuse-values` в команде, чтобы сохранить вашу конфигурацию.

   ```
   helm upgrade dynatrace-oneagent-operator dynatrace/\



   dynatrace-oneagent-operator -n dynatrace --reuse-values
   ```

## Удаление OneAgent Operator

Удаление с kubectl

Удаление с Helm

Для удаления OneAgent Operator из OpenShift версии 3.9+

1. Удалите пользовательские ресурсы OneAgent и очистите все оставшиеся объекты OneAgent Operator.

   ```
   oc delete -n dynatrace oneagent --all



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/openshift.yaml
   ```
2. Необязательно После удаления OneAgent Operator бинарник OneAgent остаётся на узле в неактивном состоянии. Для полного удаления запустите скрипт `uninstall.sh` и удалите логи и конфигурационные файлы.
   См. [информацию по Linux](../../../dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux.md "Узнайте, как удалить OneAgent из вашей системы на базе Linux.").

Удалите пользовательские ресурсы OneAgent и очистите все оставшиеся объекты OneAgent Operator:

```
helm uninstall dynatrace-oneagent-operator -n dynatrace
```

## Связанные темы

* [Kubernetes Classic](../../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring.md "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")
* [Хранение образов Dynatrace в частных реестрах](../../../setup-on-k8s/guides/container-registries/prepare-private-registry.md "Хранение образов Dynatrace в частных реестрах")
* [Миграция Dynatrace Operator в новую среду](../../../setup-on-k8s/guides/migration/migrate-dto-to-tenant.md "Миграция мониторинга в новую среду Dynatrace на кластерах Kubernetes.")