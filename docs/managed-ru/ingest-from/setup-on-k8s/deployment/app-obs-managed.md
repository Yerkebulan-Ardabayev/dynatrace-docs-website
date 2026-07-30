---
title: Начало работы с Application observability
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed
---

# Начало работы с Application observability

# Начало работы с Application observability

* Опубликовано 28 июл. 2023

На этой странице описана установка Dynatrace Operator в конфигурации мониторинга приложений на кластер Kubernetes.

Предварительные требования

Перед установкой Dynatrace на кластер Kubernetes нужно убедиться, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* На мониторируемом кластере достаточно привилегий для выполнения команд `kubectl` или `oc`. Если роль `cluster-admin` не используется, нужные разрешения описаны в разделе [deployment permissions](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице представлен обзор компонентов Dynatrace, их настроек по умолчанию и необходимых разрешений").

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL окружения Dynatrace.

  + Для Dynatrace Managed можно дополнительно использовать Cluster ActiveGate URL.
* Для OpenShift Dedicated нужна роль [cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm: использовать [Helm version 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

Поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

[Настройка SCC](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Dynatrace Operator в окружениях OpenShift.") обязательна для OpenShift при развёртывании `cloudNativeFullStack` и `applicationMonitoring` с CSI driver.

Одновременное использование `hostMonitoring` и `applicationMonitoring` в одном кластере Kubernetes в одном окружении не поддерживается.

## Варианты установки

Выбрать **один из методов установки**, который лучше всего подходит для конкретных задач.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению через Helm используют чарт Helm из OCI registry. Если репозиторий Dynatrace добавлен в локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки одинаков для Kubernetes и OpenShift. Платформа определяется автоматически во время установки.

1. Установить Dynatrace Operator

   Доступно два варианта:

   Стандартная установка / Установка через OCI registry

   Следующая команда подходит как для стандартной установки, так и для установки через OCI registry.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной настройкой чарта Helm

   Отредактировать пример файла [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, затем выполнить команду установки, передав файл YAML в качестве аргумента:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Если `installCRD` установлено в `false`, нужно вручную создать custom resource definition перед запуском установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").
2. Создать secret для токенов доступа

   Создать secret с именем `dynakube` для Dynatrace Operator token и data ingest token, полученных в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Применить DynaKube custom resource

   Скачать [пример DynaKube custom resource для мониторинга приложений из GitHub﻿](https://dt-url.net/0w036dz). Дополнительно можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание параметров установки и настройки для конкретных сценариев использования") и адаптировать DynaKube custom resource под свои требования.

   Выполнить команду ниже для применения DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. При наличии ошибок validation webhook выдаст соответствующие сообщения.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Опционально: проверить развёртывание

   Убедиться, что DynaKube запущен и все поды в пространстве имён Dynatrace находятся в состоянии Running и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

В стандартной конфигурации DynaKube с CSI driver ожидаются следующие поды:

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

CSI driver опционален (см. шаг 2). При включении разворачивается как DaemonSet, создавая по одному CSI-driver поду на каждом узле.

## Манифест

Kubernetes

OpenShift

1. Создать namespace `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes-csi.yaml
   ```

   Без CSI driver

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

   Следующая команда покажет, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать secret для токенов доступа

   Создать secret с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить DynaKube custom resource

   Загрузить [пример DynaKube custom resource для мониторинга приложений из GitHub﻿](https://dt-url.net/0w036dz). Дополнительно можно изучить [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [руководства](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать DynaKube custom resource под свои требования.

   Выполнить приведённую ниже команду для применения DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. Validation webhook выдаст полезные сообщения об ошибках при возникновении проблем.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен и все pod'ы в namespace Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В стандартной конфигурации DynaKube с CSI driver должны отображаться следующие pod'ы:

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

   CSI driver является необязательным (см. шаг 2). Если он включён, разворачивается как DaemonSet и создаёт pod CSI-driver на каждом узле.

1. Добавить проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift-csi.yaml
   ```

   Без CSI driver

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift.yaml
   ```

   Следующая команда покажет, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать secret для токенов доступа

   Создать secret с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить DynaKube custom resource

   Загрузить [пример DynaKube custom resource для мониторинга приложений из GitHub﻿](https://dt-url.net/0w036dz). Дополнительно можно изучить [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [руководства](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать DynaKube custom resource под свои требования.

   Выполнить приведённую ниже команду для применения DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. Validation webhook выдаст полезные сообщения об ошибках при возникновении проблем.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен и все pod'ы в namespace Dynatrace работают и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В стандартной конфигурации DynaKube с CSI driver должны отображаться следующие pod'ы:

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

   CSI driver является необязательным (см. шаг 2). Если он включён, разворачивается как DaemonSet и создаёт pod CSI-driver на каждом узле.

## Дополнительные материалы

После успешной установки Dynatrace Operator следующие ресурсы могут оказаться полезными для дальнейшего изучения и устранения неполадок.

[#### Guides

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting

Эта страница поможет преодолеть трудности, которые могут возникнуть при работе с Dynatrace Operator и его компонентами.

Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### How it works

Подробное описание принципа работы развёртывания в Kubernetes.

How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference

Страница справки с параметрами настройки для каждого компонента Dynatrace

Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace Operator release notes

Примечания к выпуску Dynatrace Operator

Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)[#### Update or uninstall Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Size Dynatrace ActiveGates in Kubernetes

Рекомендации по ресурсам CPU и памяти для Dynatrace ActiveGates, развёрнутых в Kubernetes, с учётом масштаба кластера и типа нагрузки.

Size Dynatrace ActiveGates in Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")