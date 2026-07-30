---
title: Начало работы с наблюдаемостью Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed
---

# Начало работы с наблюдаемостью Kubernetes

# Начало работы с наблюдаемостью Kubernetes

* Опубликовано 28 июл. 2023 г.

На этой странице приведены инструкции по развёртыванию Dynatrace Operator для наблюдаемости Kubernetes.

Для получения более полного представления о среде, включая наблюдаемость приложений и пользовательский опыт, рекомендуется сочетать наблюдаемость Kubernetes с [Application Observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), если используется [Dynatrace Platform Subscription (DPS)](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models."), или применять режим [cloud native full stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes"), если используется классическое лицензирование Dynatrace.

Предварительные требования

Перед установкой Dynatrace в кластер Kubernetes нужно убедиться, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который требуется мониторить.
* На мониторируемом кластере есть достаточно прав для выполнения команд `kubectl` или `oc`. Если роль `cluster-admin` не используется, см. [deployment permissions](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") для получения информации о необходимых правах.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать Cluster ActiveGate URL.
* Для OpenShift Dedicated необходима роль [cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm: используйте [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

Поддерживаемые версии платформы Kubernetes/OpenShift см. в разделах [platform versions](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") и [distributions](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Варианты установки

Нужно выбрать **один из методов установки**, наиболее подходящий для конкретной ситуации.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator version 0.8.0+

Kubernetes

OpenShift

1. Установите Dynatrace Operator

Следующая команда подходит как для стандартных установок, так и для установок с использованием реестра OCI.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Установка с дополнительной настройкой чарта Helm

Отредактируйте пример [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, затем выполните команду установки, передав файл YAML в качестве аргумента:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \



-f values.yaml
```

Если `installCRD` установлен в `false`, перед началом установки Helm нужно вручную создать определение custom resource:

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
```

2. Создайте secret для токена доступа

Создайте secret с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

```
kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

3. Примените custom resource DynaKube

Скачайте [пример custom resource DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Также можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать custom resource DynaKube под свои требования.

Выполните приведённую ниже команду для применения custom resource DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла custom resource DynaKube. Если возникнет проблема, validation webhook выдаст понятные сообщения об ошибках.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

4. Проверьте развёртывание

Необязательно

Убедитесь, что DynaKube запущен, а все поды в пространстве имён Dynatrace работают и готовы.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В данной конфигурации DynaKube должны отображаться следующие поды:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

1. Установите Dynatrace Operator

Следующая команда подходит как для стандартных установок, так и для установок с использованием реестра OCI.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Установка с дополнительной настройкой чарта Helm

Отредактируйте пример [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, затем выполните команду установки, передав файл YAML в качестве аргумента:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \



-f values.yaml
```

Если `installCRD` установлен в `false`, перед началом установки Helm нужно вручную создать определение custom resource:

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
```

2. Создайте secret для токена доступа

Создайте secret с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

```
oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

3. Примените custom resource DynaKube

Скачайте [пример custom resource DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Также можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать custom resource DynaKube под свои требования.

Выполните приведённую ниже команду для применения custom resource DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла custom resource DynaKube. Если возникнет проблема, validation webhook выдаст понятные сообщения об ошибках.

```
oc apply -f <your-DynaKube-CR>.yaml
```

4. Проверьте развёртывание

Необязательно#

Убедитесь, что DynaKube запущен, а все поды в пространстве имён Dynatrace работают и готовы.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В данной конфигурации DynaKube должны отображаться следующие поды:

```
> oc get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

## Manifest

Kubernetes

OpenShift

1. Создайте namespace `dynatrace`

```
kubectl create namespace dynatrace
```

2. Установите Dynatrace Operator

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes.yaml
```

Выполните следующую команду, чтобы дождаться завершения инициализации компонентов Dynatrace Operator:

```
kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
```

3. Создайте секрет для токена доступа

Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

```
kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

4. Примените custom resource DynaKube

Скачайте [образец custom resource DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Дополнительно можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать custom resource DynaKube под свои требования.

Выполните команду ниже, чтобы применить custom resource DynaKube. Замените `<your-DynaKube-CR>` на фактическое имя файла вашего custom resource DynaKube. Webhook валидации выведет полезные сообщения об ошибках при возникновении проблем.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

5. Проверьте развёртывание

Необязательно

Убедитесь, что DynaKube запущен, а все поды в namespace Dynatrace находятся в состоянии Running и Ready.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В данной конфигурации DynaKube должны присутствовать следующие поды:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

1. Добавьте проект `dynatrace`

```
oc adm new-project --node-selector="" dynatrace
```

2. Установите Dynatrace Operator

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift.yaml
```

Выполните следующую команду, чтобы дождаться завершения инициализации компонентов Dynatrace Operator:

```
oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
```

3. Создайте секрет для токена доступа

Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

```
oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

4. Примените custom resource DynaKube

Скачайте [образец custom resource DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Дополнительно можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать custom resource DynaKube под свои требования.

Выполните команду ниже, чтобы применить custom resource DynaKube. Замените `<your-DynaKube-CR>` на фактическое имя файла вашего custom resource DynaKube. Webhook валидации выведет полезные сообщения об ошибках при возникновении проблем.

```
oc apply -f <your-DynaKube-CR>.yaml
```

5. Проверьте развёртывание

Необязательно

Убедитесь, что DynaKube запущен, а все поды в namespace Dynatrace находятся в состоянии Running и Ready.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В данной конфигурации DynaKube должны присутствовать следующие поды:

```
> oc get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

## Learn more

После успешной установки Dynatrace Operator следующие ресурсы помогут в дальнейшем изучении и диагностике проблем.

[#### Guides

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting

Страница поможет справиться с трудностями, возникающими при работе с Dynatrace Operator и его компонентами.

Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### How it works

Подробное описание того, как работает развёртывание в Kubernetes.

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

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")