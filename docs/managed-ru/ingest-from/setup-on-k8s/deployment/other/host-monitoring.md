---
title: Начало работы с мониторингом хостов
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/host-monitoring
---

# Начало работы с мониторингом хостов

# Начало работы с мониторингом хостов

* 6 минут чтения
* Обновлено 05 сент. 2025

На этой странице приведены инструкции по развёртыванию Dynatrace Operator в конфигурации мониторинга хостов на кластере Kubernetes.

Если нужно получить более полное представление о среде с учётом таких аспектов, как наблюдаемость приложений и пользовательский опыт, стоит рассмотреть подход полной наблюдаемости Kubernetes: например, [cloud-native full-stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме cloud-native full-stack на Kubernetes") или [classic full-stack](/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Развёртывание Dynatrace Operator в режиме classic full-stack на Kubernetes").

Предварительные требования

Перед установкой Dynatrace на кластер Kubernetes нужно убедиться, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно отслеживать.
* На контролируемом кластере есть достаточно прав для выполнения команд `kubectl` или `oc`. Если роль кластера `cluster-admin` не используется, см. раздел [разрешения для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице представлен обзор компонентов Dynatrace, их конфигураций по умолчанию и необходимых разрешений") с перечнем требуемых прав.

### Настройка и конфигурация кластера

* Нужно разрешить исходящий трафик для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm: используйте [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

Поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Поддержка Dynatrace версий Kubernetes и Red Hat OpenShift и известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") описаны на соответствующих страницах.

Одновременное использование `hostMonitoring` и `applicationMonitoring` в кластере Kubernetes в одной среде не поддерживается.

## Варианты установки

Выберите **один из методов установки**, наиболее подходящий для ваших задач.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

1. Установите Dynatrace Operator

   При использовании Helm версии 4.0+ нужно использовать `--rollback-on-failure` вместо флага `--atomic`.

   Следующая команда подходит как для стандартных установок, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной конфигурацией чарта Helm

   Отредактируйте пример [`values.yaml`﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/config/helm/chart/default/values.yaml) из GitHub, затем выполните команду установки, передав файл YAML как аргумент:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Если `installCRD` установлено в `false`, нужно вручную создать определение пользовательского ресурса перед началом установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```
2. Создайте секрет для токена доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Примените пользовательский ресурс DynaKube

   Скачайте [пример пользовательского ресурса DynaKube для мониторинга хостов из GitHub﻿](https://dt-url.net/qx8363l). Также можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и конфигурации для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube под свои требования.

   Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` фактическим именем файла пользовательского ресурса DynaKube. Validation webhook выведет полезные сообщения об ошибках при наличии проблем.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно: Проверьте развёртывание

   Убедитесь, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В стандартной конфигурации DynaKube с CSI-драйвером Dynatrace Operator должны отображаться следующие поды:

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

1. Создайте namespace `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes-csi.yaml
   ```

   Выполните следующую команду, чтобы дождаться завершения инициализации компонентов Dynatrace Operator:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте secret для access token

   Создайте secret с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Примените DynaKube custom resource

   Скачайте [образец DynaKube custom resource для host monitoring из GitHub﻿](https://dt-url.net/qx8363l). Также можно изучить [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать DynaKube custom resource под свои требования.

   Чтобы сократить количество оплачиваемых units, включите режим Infrastructure Monitoring в конфигурации DynaKube.

   ```
   oneAgent:



   hostMonitoring:



   args:



   - --set-monitoring-mode=infra-only
   ```

   Выполните команду ниже, чтобы применить DynaKube custom resource, заменив `<your-DynaKube-CR>` фактическим именем файла вашего DynaKube custom resource. Если возникнет проблема, validation webhook выдаст понятное сообщение об ошибке.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверьте развёртывание

   Убедитесь, что DynaKube запущен и все Pods в namespace Dynatrace находятся в состоянии running и ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver Dynatrace Operator должны отображаться следующие Pods:

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

   Поскольку OneAgent и CSI driver развёртываются как DaemonSet, на каждом узле должен быть Pod OneAgent и Pod CSI driver.

1. Добавьте проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift-csi.yaml
   ```

   Выполните следующую команду, чтобы дождаться завершения инициализации компонентов Dynatrace Operator:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте secret для access token

   Создайте secret с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Примените DynaKube custom resource

   Скачайте [образец DynaKube custom resource для host monitoring из GitHub﻿](https://dt-url.net/qx8363l). Также можно изучить [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать DynaKube custom resource под свои требования.

   Выполните команду ниже, чтобы применить DynaKube custom resource, заменив `<your-DynaKube-CR>` фактическим именем файла вашего DynaKube custom resource. Если возникнет проблема, validation webhook выдаст понятное сообщение об ошибке.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверьте развёртывание

   Убедитесь, что DynaKube запущен и все Pods в namespace Dynatrace находятся в состоянии running и ready.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI driver Dynatrace Operator должны отображаться следующие Pods:

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

   Поскольку OneAgent и CSI driver развёртываются как DaemonSet, на каждом узле должен быть Pod OneAgent и Pod CSI driver.

## Дополнительные материалы

После успешной установки Dynatrace Operator могут быть полезны следующие ресурсы для дальнейшего изучения и решения проблем.

[#### Guides

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting

Эта страница поможет справиться с трудностями, которые могут возникнуть при работе с Dynatrace Operator и его компонентами.

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

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")