---
title: Начало работы с Application observability
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed
---

# Начало работы с Application observability

# Начало работы с Application observability

* Опубликовано 28 июля 2023 г.

На этой странице приведены инструкции по развёртыванию Operator Dynatrace в конфигурации мониторинга приложений в кластер Kubernetes.

Предварительные требования

Перед установкой Dynatrace в кластер Kubernetes убедись, что выполняются следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* На отслеживаемом кластере достаточно прав для выполнения команд `kubectl` или `oc`. Если роль кластера `cluster-admin` не используется, см. [права доступа для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и необходимых им прав доступа") для необходимых разрешений.

### Настройка и конфигурация кластера

* Нужно разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используй [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформы](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

[Настройка SCC](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Operator Dynatrace в средах OpenShift.") обязательна для OpenShift при развёртываниях `cloudNativeFullStack` и `applicationMonitoring` с CSI driver.

Сочетание `hostMonitoring` и `applicationMonitoring` в кластере Kubernetes в одной и той же среде не поддерживается.

## Варианты установки

Выбери **один из способов установки**, который лучше всего подходит под твои задачи.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Operator Dynatrace версии 0.8.0+

Новые инструкции по установке и обновлению Helm используют наш чарт Helm, доступный из реестра OCI. Поэтому, если репозиторий Dynatrace сейчас добавлен в локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используется Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установка Operator Dynatrace

   Есть два варианта:

   Установка по умолчанию / установка через реестр OCI

   Следующая команда подходит как для установки по умолчанию, так и для установки через реестр OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной конфигурацией чарта Helm

   Отредактируй пример [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, а затем выполни команду установки, передав файл YAML как аргумент:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Если для `installCRD` установлено значение `false`, перед началом установки Helm нужно вручную создать определение пользовательского ресурса:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной конфигурации](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").
2. Создание секрета для токенов доступа

   Создай секрет с именем `dynakube` для токена Operator Dynatrace и токена приёма данных, полученных в разделе [Требуемые токены и права доступа](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав доступа для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Применение пользовательского ресурса DynaKube

   Скачай [пример пользовательского ресурса DynaKube для мониторинга приложений из GitHub﻿](https://dt-url.net/0w036dz). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Operator Dynatrace на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube под свои требования.

   Выполни приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` на имя файла своего пользовательского ресурса DynaKube. Веб-хук валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Опционально Проверка развёртывания

   Проверь, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

В конфигурации DynaKube по умолчанию с CSI driver должны отображаться следующие поды:

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

CSI driver опционален (см. шаг 2). Если включён, он развёртывается как DaemonSet и создаёт под CSI-driver на каждом узле.

## Манифест

Kubernetes

OpenShift

1. Создать namespace `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/kubernetes-csi.yaml
   ```

   Без CSI driver

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/kubernetes.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной конфигурации](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

   Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токенов доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить кастомный ресурс DynaKube

   Скачать [пример кастомного ресурса DynaKube для мониторинга приложений с GitHub﻿](https://dt-url.net/0w036dz). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать кастомный ресурс DynaKube под свои требования.

   Выполнить команду ниже, чтобы применить кастомный ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла кастомного ресурса DynaKube. Validation webhook выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Опционально Проверить развёртывание

   Проверить, что DynaKube запущен и все поды в namespace Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В стандартной конфигурации DynaKube с CSI driver должны отображаться следующие поды:

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

   CSI driver опционален (см. шаг 2). Если включён, он развёртывается как DaemonSet и на каждом узле появляется под CSI driver.

1. Добавить проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/openshift-csi.yaml
   ```

   Без CSI driver

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/openshift.yaml
   ```

   Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токенов доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить кастомный ресурс DynaKube

   Скачать [пример кастомного ресурса DynaKube для мониторинга приложений с GitHub﻿](https://dt-url.net/0w036dz). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать кастомный ресурс DynaKube под свои требования.

   Выполнить команду ниже, чтобы применить кастомный ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла кастомного ресурса DynaKube. Validation webhook выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Опционально Проверить развёртывание

   Проверить, что DynaKube запущен и все поды в namespace Dynatrace работают и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В стандартной конфигурации DynaKube с CSI driver должны отображаться следующие поды:

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

   CSI driver опционален (см. шаг 2). Если включён, он развёртывается как DaemonSet и на каждом узле появляется под CSI driver.

## Узнать больше

После успешной установки Dynatrace Operator следующие ресурсы могут пригодиться для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет разобраться с проблемами, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами.

Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### Как это работает

Подробное описание того, как работает развёртывание на Kubernetes.

Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник

Содержит справочную страницу с параметрами настройки для каждого компонента Dynatrace

Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### Обновление или удаление Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по определению размеров Dynatrace ActiveGate для сценария использования мониторинга Kubernetes

Задать ограничения ресурсов для Dynatrace ActiveGate

Руководство по определению размеров Dynatrace ActiveGate для сценария использования мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Похожие темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")