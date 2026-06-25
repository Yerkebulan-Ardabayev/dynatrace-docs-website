---
title: Начало работы с host monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/host-monitoring
scraped: 2026-05-12T12:04:46.293381
---

# Начало работы с host monitoring

# Начало работы с host monitoring

* Чтение: 6 мин
* Обновлено 5 сентября 2025 г.

На этой странице приведены инструкции по развёртыванию Dynatrace Operator в конфигурации host monitoring в кластере Kubernetes.

Если требуется получить более полное представление о вашем окружении, включающее такие аспекты, как Application observability и пользовательский опыт, следует рассмотреть полный подход к наблюдаемости Kubernetes, например [cloud-native full-stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме cloud-native full-stack в Kubernetes") или [classic full-stack](/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Развёртывание Dynatrace Operator в режиме classic full-stack в Kubernetes").

Предварительные требования

Перед установкой Dynatrace в кластере Kubernetes убедитесь, что выполнены следующие требования:

* Ваш интерфейс командной строки `kubectl` подключён к кластеру Kubernetes, который необходимо отслеживать.
* У вас достаточно прав в отслеживаемом кластере для выполнения команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик от подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL вашего окружения Dynatrace.

  + Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated необходима [роль cluster-admin](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm. Используйте [Helm версии 3](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы") и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.

Сочетание `hostMonitoring` и `applicationMonitoring` в кластере Kubernetes в одном окружении не поддерживается.

## Варианты установки

Выберите **один из методов установки**, который лучше всего подходит для ваших потребностей.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

1. Установите Dynatrace Operator

   Если вы используете Helm версии 4.0+, необходимо использовать `--rollback-on-failure` вместо флага `--atomic`.

   Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной настройкой Helm chart

   Отредактируйте образец [`values.yaml`](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) с GitHub, а затем выполните команду установки, передав YAML-файл в качестве аргумента:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Если для `installCRD` задано значение `false`, необходимо создать определение пользовательского ресурса вручную перед началом установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```
2. Создайте секрет для токена доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для host monitoring с GitHub](https://dt-url.net/qx8363l). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки предоставит полезные сообщения об ошибках при возникновении проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver от Dynatrace Operator должны отобразиться следующие поды:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   Поскольку OneAgent и CSI driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI driver.

## Manifest

Kubernetes

OpenShift

1. Создайте пространство имён `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
   ```

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токена доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для host monitoring с GitHub](https://dt-url.net/qx8363l). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Если необходимо сократить число тарифицируемых единиц, включите режим Infrastructure Monitoring в конфигурации DynaKube.

   ```
   oneAgent:



   hostMonitoring:



   args:



   - --set-monitoring-mode=infra-only
   ```

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки предоставит полезные сообщения об ошибках при возникновении проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver от Dynatrace Operator должны отобразиться следующие поды:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   Поскольку OneAgent и CSI driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI driver.

1. Добавьте проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
   ```

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токена доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для host monitoring с GitHub](https://dt-url.net/qx8363l). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки предоставит полезные сообщения об ошибках при возникновении проблемы.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver от Dynatrace Operator должны отобразиться следующие поды:

   ```
   > oc get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   Поскольку OneAgent и CSI driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI driver.

## Узнать больше

После успешной установки Dynatrace Operator следующие ресурсы могут оказаться полезными для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет справиться с любыми трудностями, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами.

Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### Как это работает

Подробное описание того, как работает развёртывание в Kubernetes.

Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник

Содержит справочную страницу с параметрами настройки для каждого компонента Dynatrace

Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### Обновление или удаление Dynatrace Operator

Процедуры обновления и удаления Dynatrace Operator

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по выбору размера Dynatrace ActiveGate для сценария мониторинга Kubernetes

Задайте лимиты ресурсов для Dynatrace ActiveGate

Руководство по выбору размера Dynatrace ActiveGate для сценария мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")