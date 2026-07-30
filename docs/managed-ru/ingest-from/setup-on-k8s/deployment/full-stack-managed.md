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

В новых инструкциях по установке и обновлению Helm используется chart из OCI-реестра. Поэтому, если репозиторий Dynatrace уже добавлен в локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используется Kubernetes или OpenShift. Платформа определяется автоматически в ходе установки.

1. Установка Dynatrace Operator

   Следующая команда работает как при стандартной установке, так и при установке через OCI-реестр.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной конфигурацией chart Helm

   Отредактируй образец [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, затем запусти команду установки, передав файл YAML в качестве аргумента:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Для cloud native и full stack развёртываний CSI-драйвер обязателен. Если `installCRD` установлен в `false`, нужно создать custom resource definition вручную до начала установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной конфигурации](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").
2. Создание секрета для токенов доступа

   Создай секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Применение DynaKube custom resource

   Скачай [образец DynaKube custom resource для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Дополнительно можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать DynaKube custom resource под свои требования.

   Выполни команду ниже, чтобы применить DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. Если возникнет проблема, validation webhook выдаст полезные сообщения об ошибках.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно: проверка развёртывания

   Убедись, что DynaKube запущен и все поды в пространстве имён Dynatrace находятся в состоянии Running и готовы к работе.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   При стандартной конфигурации DynaKube должны отображаться следующие поды:

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

   Поскольку OneAgent и CSI-драйвер развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-драйвера.

## Manifest

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

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

   Следующая команда позволяет отследить завершение инициализации компонентов Dynatrace Operator:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать secret для токенов доступа

   Создать secret с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить DynaKube custom resource

   Скачать [образец DynaKube custom resource для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Дополнительно можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать DynaKube custom resource под свои требования.

   Выполнить команду ниже для применения DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. Validation webhook выдаст информативные сообщения об ошибках при наличии проблем.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен, а все поды в namespace Dynatrace работают и готовы к работе.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В стандартной конфигурации DynaKube должны присутствовать следующие поды:

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

   Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на каждом узле должен присутствовать под OneAgent и под CSI-driver.

1. Добавить проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift-csi.yaml
   ```

   Следующая команда позволяет отследить завершение инициализации компонентов Dynatrace Operator:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать secret для токенов доступа

   Создать secret с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Применить DynaKube custom resource

   Скачать [образец DynaKube custom resource для cloud-native full-stack из GitHub﻿](https://dt-url.net/9n636jg). Дополнительно можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать DynaKube custom resource под свои требования.

   Выполнить команду ниже для применения DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. Validation webhook выдаст информативные сообщения об ошибках при наличии проблем.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен, а все поды в namespace Dynatrace работают и готовы к работе.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В стандартной конфигурации DynaKube должны присутствовать следующие поды:

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

   Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на каждом узле должен присутствовать под OneAgent и под CSI-driver.

## Learn more

После успешной установки Dynatrace Operator следующие ресурсы помогут в дальнейшем изучении и устранении неполадок.

[#### Guides

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting

Эта страница поможет справиться с любыми трудностями при работе с Dynatrace Operator и его компонентами.

Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### How it works

Подробное описание принципов развёртывания на Kubernetes.

How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference

Справочная страница с параметрами конфигурации для каждого компонента Dynatrace

Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace Operator release notes

Примечания к выпускам Dynatrace Operator

Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)[#### Update or uninstall Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Size Dynatrace ActiveGates in Kubernetes

Рекомендации по ресурсам CPU и памяти для Dynatrace ActiveGates, развёрнутых в Kubernetes, с учётом масштаба кластера и типа нагрузки.

Size Dynatrace ActiveGates in Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Related topics

* [Flexible, scalable, self-service Kubernetes native observability now in General Availability﻿](https://www.dynatrace.com/news/blog/flexible-scalable-self-service-kubernetes-native-observability/)