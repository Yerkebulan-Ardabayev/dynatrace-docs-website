---
title: Начало работы с наблюдаемостью Full Kubernetes (облачно-нативное развёртывание full-stack)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed
---

# Начало работы с наблюдаемостью Full Kubernetes (облачно-нативное развёртывание full-stack)

# Начало работы с наблюдаемостью Full Kubernetes (облачно-нативное развёртывание full-stack)

* Обновлено 06 ноя 2023

На этой странице приведены инструкции по установке Dynatrace Operator с облачно-нативной конфигурацией full-stack в кластер Kubernetes.

Предварительные требования

Перед установкой Dynatrace в кластер Kubernetes убедиться, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* Есть достаточные привилегии в мониторируемом кластере для выполнения команд `kubectl` или `oc`. Если не используется кластерная роль `cluster-admin`, см. [права для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых прав") для необходимых прав.

### Настройка и конфигурация кластера

* Нужно разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию, namespace Dynatrace) к URL окружения Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL кластера ActiveGate.
* Для OpenShift Dedicated требуется [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Использовать [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

По умолчанию Dynatrace Operator инжектирует OneAgent во все namespace, но можно настроить его так, чтобы мониторить только определённые namespace и исключить остальные. Подробнее см. [Настройка мониторинга для namespace и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#monitor-only-specific-namespaces "Настройка мониторинга для namespace и подов").

[Настройка SCC](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Dynatrace Operator в окружениях OpenShift.") обязательна для OpenShift при развёртываниях `cloudNativeFullStack` и `applicationMonitoring` с CSI driver.

## Варианты установки

Выбрать **один из способов установки**, который лучше всего подходит для конкретных задач.

[![Dynatrace UI](https://dt-cdn.net/images/search-color-945bb8b42a.svg "Dynatrace UI")

**С помощью мастера (Dynatrace UI)**](#guided)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Манифест**](#manifest)

## С помощью мастера (Dynatrace UI)

Dynatrace версии 1.290+

1. Перейти в **Kubernetes**.
2. Выбрать **Connect automatically via Dynatrace Operator** в заголовке страницы кластера Kubernetes.

![Quickstart](https://dt-cdn.net/images/quickstart-3574-833bd4c27b.png)

Quickstart

1. Ввести следующие данные.

   * **Name**: задаёт отображаемое имя кластера Kubernetes в Dynatrace. Кроме того, это имя будет использоваться как префикс для именования ресурсов Dynatrace внутри кластера Kubernetes, таких как DynaKube (custom resource), ActiveGate (под), OneAgent (поды), а также как имя для секрета, хранящего токены.
   * Рекомендуется **Group**: задаёт группу, используемую различными настройками Dynatrace, включая network zone, группу ActiveGate и host group. Если не задано, используются значения по умолчанию или пустые значения.
   * **Dynatrace Operator token**: выбрать **Create token** или ввести ранее созданный токен **API**. Подробнее см. [Токены доступа и права](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав для мониторинга кластера Kubernetes").
   * Опционально**Data ingest token**: выбрать **Create token** или ввести ранее созданный токен **API**. Подробнее см. [Токены доступа и права](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав для мониторинга кластера Kubernetes").
2. Опционально Решить, нужно ли, чтобы Dynatrace Operator отключил проверку SSL-сертификата Dynatrace.

   Это актуально при использовании Dynatrace Managed с самоподписанными сертификатами.
3. Выбрать **Download dynakube.yaml**. Скопировать блок кода, созданный Dynatrace, и **выполнить его в терминале**. Выполнять команды нужно в той же директории, куда был загружен YAML, либо адаптировать команду под расположение манифеста YAML.

   Загруженный файл YAML представляет собой базовую версию определения custom resource DynaKube. Чтобы адаптировать значения под конкретные задачи, см. [примеры custom resource DynaKube для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Подробнее обо всех параметрах конфигурации см. [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").
4. Опционально Убедиться, что DynaKube запущен и все поды в namespace Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие поды:

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

   Поскольку OneAgent и CSI-driver развёрнуты как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению Helm используют наш чарт Helm, доступный из реестра OCI. Поэтому, если репозиторий Dynatrace сейчас добавлен в локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используется ли Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установить Dynatrace Operator

   Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной настройкой чарта Helm

   Отредактировать образец [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, а затем выполнить команду установки, передав файл YAML в качестве аргумента:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Для развёртываний cloud native, full stack, CSI driver обязателен. Если `installCRD` установлен в `false`, нужно вручную создать custom resource definition перед началом установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").
2. Создать secret для токенов доступа

   Создать secret с именем `dynakube` для токена Dynatrace Operator и токена ingest данных, полученных в разделе [Требуемые токены и права доступа](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав доступа для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Применить custom resource DynaKube

   Скачать [образец custom resource DynaKube для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать custom resource DynaKube в соответствии со своими требованиями.

   Выполнить приведённую ниже команду, чтобы применить custom resource DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла custom resource DynaKube. Webhook валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно Проверить развёртывание

   Проверить, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие поды:

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

   Так как OneAgent и CSI-driver развёрнуты как DaemonSet, под OneAgent и CSI-driver должен быть на каждом узле.

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

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

   Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токенов доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes.").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить кастомный ресурс DynaKube

   Скачать [образец кастомного ресурса DynaKube для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования"), и адаптировать кастомный ресурс DynaKube в соответствии с требованиями.

   Выполнить приведённую ниже команду для применения кастомного ресурса DynaKube, обязательно заменив `<your-DynaKube-CR>` на фактическое имя файла кастомного ресурса DynaKube. Webhook валидации предоставит полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Опционально Проверить развёртывание

   Проверить, что DynaKube запущен и все поды в namespace Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие поды:

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

   Так как OneAgent и CSI-driver развёрнуты как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

1. Добавить проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/openshift-csi.yaml
   ```

   Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токенов доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes.").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить кастомный ресурс DynaKube

   Скачать [образец кастомного ресурса DynaKube для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования"), и адаптировать кастомный ресурс DynaKube в соответствии с требованиями.

   Выполнить приведённую ниже команду для применения кастомного ресурса DynaKube, обязательно заменив `<your-DynaKube-CR>` на фактическое имя файла кастомного ресурса DynaKube. Webhook валидации предоставит полезные сообщения об ошибках, если возникнет проблема.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Опционально Проверить развёртывание

   Проверить, что DynaKube запущен и все поды в namespace Dynatrace запущены и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие поды:

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

   Так как OneAgent и CSI-driver развёрнуты как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

## Узнать больше

После успешной установки Dynatrace Operator следующие ресурсы могут быть полезны для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет ориентироваться в любых сложностях, с которыми можно столкнуться при работе с Dynatrace Operator и его различными компонентами.

Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### Как это работает

Подробное описание того, как работает развёртывание на Kubernetes.

Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник

Содержит справочную страницу с параметрами настройки для каждого компонента Dynatrace

Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к выпуску Dynatrace Operator

Примечания к выпуску для Dynatrace Operator

Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### Обновление или удаление Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по расчёту размера ActiveGateов Dynatrace для сценария мониторинга Kubernetes

Настройка ограничений ресурсов для ActiveGateов Dynatrace

Руководство по расчёту размера ActiveGateов Dynatrace для сценария мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Похожие темы

* [Гибкая, масштабируемая, самообслуживаемая нативная для Kubernetes observability теперь общедоступна﻿](https://www.dynatrace.com/news/blog/flexible-scalable-self-service-kubernetes-native-observability/)