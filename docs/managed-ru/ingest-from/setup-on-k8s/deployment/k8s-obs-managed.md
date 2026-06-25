---
title: Начало работы с наблюдаемостью Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed
scraped: 2026-05-12T11:52:50.677236
---

# Начало работы с наблюдаемостью Kubernetes

# Начало работы с наблюдаемостью Kubernetes

* Опубликовано 28 июля 2023 г.

На этой странице приведены инструкции по развёртыванию Dynatrace Operator для наблюдаемости Kubernetes.

Чтобы получить более полное представление о вашем окружении, включающее такие аспекты, как наблюдаемость приложений и пользовательский опыт, стоит рассмотреть объединение наблюдаемости Kubernetes с [Application Observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме application monitoring в Kubernetes"), если у вас [Dynatrace Platform Subscription (DPS)](/managed/license "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace"), или использовать режим [cloud native full stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме cloud-native full-stack в Kubernetes"), если у вас классическое лицензирование Dynatrace.

Предварительные требования

Перед установкой Dynatrace на ваш кластер Kubernetes убедитесь, что выполнены следующие требования:

* Ваш `kubectl` CLI подключён к кластеру Kubernetes, который требуется отслеживать.
* У вас достаточно прав на отслеживаемом кластере для выполнения команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL вашего окружения Dynatrace.

  + Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated требуется [роль cluster-admin](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используйте [Helm версии 3](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы") и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.

## Варианты установки

Выберите **один из методов установки**, который лучше всего соответствует вашим потребностям.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Kubernetes

OpenShift

1. Установите Dynatrace Operator

Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Установка с дополнительной настройкой Helm chart

Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) с GitHub, а затем выполните команду установки, передав YAML-файл как аргумент:

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

Скачайте [образец пользовательского ресурса DynaKube для наблюдаемости Kubernetes](https://dt-url.net/sa038nu) с GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, не забыв заменить `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Проверяющий вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

4. Проверьте развёртывание

Необязательно

Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В этой конфигурации DynaKube должны отображаться следующие поды:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

1. Установите Dynatrace Operator

Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Установка с дополнительной настройкой Helm chart

Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) с GitHub, а затем выполните команду установки, передав YAML-файл как аргумент:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \



-f values.yaml
```

Если для `installCRD` задано значение `false`, необходимо создать определение пользовательского ресурса вручную перед началом установки Helm:

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
```

2. Создайте секрет для токена доступа

Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").

```
oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

3. Примените пользовательский ресурс DynaKube

Скачайте [образец пользовательского ресурса DynaKube для наблюдаемости Kubernetes](https://dt-url.net/sa038nu) с GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, не забыв заменить `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Проверяющий вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

```
oc apply -f <your-DynaKube-CR>.yaml
```

4. Проверьте развёртывание

Необязательно#

Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В этой конфигурации DynaKube должны отображаться следующие поды:

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

1. Создайте пространство имён `dynatrace`

```
kubectl create namespace dynatrace
```

2. Установите Dynatrace Operator

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
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

Скачайте [образец пользовательского ресурса DynaKube для наблюдаемости Kubernetes](https://dt-url.net/sa038nu) с GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, не забыв заменить `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Проверяющий вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

5. Проверьте развёртывание

Необязательно

Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В этой конфигурации DynaKube должны отображаться следующие поды:

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
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
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

Скачайте [образец пользовательского ресурса DynaKube для наблюдаемости Kubernetes](https://dt-url.net/sa038nu) с GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, не забыв заменить `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Проверяющий вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

```
oc apply -f <your-DynaKube-CR>.yaml
```

5. Проверьте развёртывание

Необязательно

Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В этой конфигурации DynaKube должны отображаться следующие поды:

```
> oc get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

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

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по выбору размера для Dynatrace ActiveGate в сценарии мониторинга Kubernetes

Установка лимитов ресурсов для Dynatrace ActiveGate

Руководство по выбору размера для Dynatrace ActiveGate в сценарии мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")