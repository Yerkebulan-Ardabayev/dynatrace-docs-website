---
title: Начало работы с Application observability
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed
scraped: 2026-05-12T11:22:23.592993
---

# Начало работы с Application observability

# Начало работы с Application observability

* Опубликовано 28 июля 2023 г.

На этой странице приведены инструкции по развёртыванию Dynatrace Operator в конфигурации application monitoring в кластере Kubernetes.

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

[Настройка SCC](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Dynatrace Operator в окружениях OpenShift.") требуется для OpenShift при развёртываниях `cloudNativeFullStack` и `applicationMonitoring` с CSI driver.

Сочетание `hostMonitoring` и `applicationMonitoring` в кластере Kubernetes в одном окружении не поддерживается.

## Варианты установки

Выберите **один из методов установки**, который лучше всего подходит для ваших потребностей.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению Helm используют наш Helm chart, доступный из реестра OCI. Поэтому, если репозиторий Dynatrace в настоящее время добавлен в ваши локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используете ли вы Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установите Dynatrace Operator

   Доступны два варианта:

   Установка по умолчанию / установка из реестра OCI

   Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной настройкой Helm chart

   Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) с GitHub, а затем выполните команду установки, передав YAML-файл в качестве аргумента:

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

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").
2. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для application monitoring с GitHub](https://dt-url.net/0w036dz). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки предоставит полезные сообщения об ошибках при возникновении проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

В конфигурации DynaKube по умолчанию с CSI driver должны отобразиться следующие поды:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

CSI driver является необязательным (см. шаг 2). Если он включён, он развёртывается как DaemonSet, в результате чего на каждом узле появляется под CSI-драйвера.

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

   Без CSI driver

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для application monitoring с GitHub](https://dt-url.net/0w036dz). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки предоставит полезные сообщения об ошибках при возникновении проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver должны отобразиться следующие поды:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI driver является необязательным (см. шаг 2). Если он включён, он развёртывается как DaemonSet, в результате чего на каждом узле появляется под CSI-драйвера.

1. Добавьте проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
   ```

   Без CSI driver

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
   ```

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для application monitoring с GitHub](https://dt-url.net/0w036dz). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки предоставит полезные сообщения об ошибках при возникновении проблемы.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver должны отобразиться следующие поды:

   ```
   > oc get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI driver является необязательным (см. шаг 2). Если он включён, он развёртывается как DaemonSet, в результате чего на каждом узле появляется под CSI-драйвера.

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