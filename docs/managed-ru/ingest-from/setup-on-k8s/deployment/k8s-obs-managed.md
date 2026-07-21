---
title: Начало работы с наблюдаемостью Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed
---

# Начало работы с наблюдаемостью Kubernetes

# Начало работы с наблюдаемостью Kubernetes

* Опубликовано 28 июля 2023 г.

На этой странице приведены инструкции по развёртыванию Dynatrace Operator для наблюдаемости Kubernetes.

Чтобы получить более полное представление о среде, включающее такие аспекты, как наблюдаемость приложений и пользовательский опыт, стоит рассмотреть сочетание наблюдаемости Kubernetes с [Application Observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развернуть Dynatrace Operator в режиме мониторинга приложений в Kubernetes"), если используется [Dynatrace Platform Subscription (DPS)](/managed/license "Dynatrace Platform Subscription, тарифные карты возможностей, гибридное лицензирование и предыдущие модели лицензирования."), или режим [cloud native full stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развернуть Dynatrace Operator в режиме cloud-native full-stack в Kubernetes"), если используется классическое лицензирование Dynatrace.

Предварительные требования

Перед установкой Dynatrace в кластере Kubernetes убедись, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* На отслеживаемом кластере есть достаточные привилегии для выполнения команд `kubectl` или `oc`. Если не используется роль кластера `cluster-admin`, см. [права для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "Эта страница содержит обзор компонентов Dynatrace, их конфигураций по умолчанию и необходимых им прав") для необходимых прав.

### Настройка кластера и конфигурация

* Нужно разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL кластера ActiveGate.
* Для OpenShift Dedicated требуется [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используй [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформы](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, и известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

## Варианты установки

Выбери **один из способов установки**, который лучше всего подходит.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Kubernetes

OpenShift

1. Установить Dynatrace Operator

Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Установка с дополнительной конфигурацией чарта Helm

Отредактируй пример [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, а затем выполни команду установки, передав файл YAML в качестве аргумента:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \



-f values.yaml
```

Если `installCRD` установлен в `false`, перед началом установки Helm нужно вручную создать определение пользовательского ресурса:

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/dynatrace-operator-crd.yaml
```

2. Создать секрет для токена доступа

Создай секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и права](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настроить токены и права для мониторинга кластера Kubernetes").

```
kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

3. Применить пользовательский ресурс DynaKube

Скачай [пример пользовательского ресурса DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [руководствами по настройке](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования"), и адаптировать пользовательский ресурс DynaKube согласно требованиям.

Выполни приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Вебхук валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

4. Проверить развёртывание

Опционально

Убедись, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В этой конфигурации DynaKube должны быть видны следующие поды:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

1. Установить Dynatrace Operator

Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Установка с дополнительной конфигурацией чарта Helm

Отредактируй пример [`values.yaml`﻿](https://dt-url.net/helm-values) из GitHub, а затем выполни команду установки, передав файл YAML в качестве аргумента:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \



-f values.yaml
```

Если `installCRD` установлен в `false`, перед началом установки Helm нужно вручную создать определение пользовательского ресурса:

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/dynatrace-operator-crd.yaml
```

2. Создать секрет для токена доступа

Создай секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и права](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настроить токены и права для мониторинга кластера Kubernetes").

```
oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

3. Применить пользовательский ресурс DynaKube

Скачай [пример пользовательского ресурса DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [руководствами по настройке](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования"), и адаптировать пользовательский ресурс DynaKube согласно требованиям.

Выполни приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Вебхук валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

```
oc apply -f <your-DynaKube-CR>.yaml
```

4. Проверить развёртывание

Опционально#

Убедись, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

В этой конфигурации DynaKube должны быть видны следующие поды:

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

1. Создать namespace `dynatrace`

```
kubectl create namespace dynatrace
```

2. Установить Dynatrace Operator

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/kubernetes.yaml
```

Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

```
kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
```

3. Создать секрет для токена доступа

Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

```
kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

4. Применить пользовательский ресурс DynaKube

Скачать [пример пользовательского ресурса DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube под свои требования.

Выполнить команду ниже, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Webhook валидации выведет полезные сообщения об ошибках, если возникнет проблема.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

5. Проверить развёртывание

Необязательно

Проверить, что DynaKube запущен и все поды в namespace Dynatrace работают и готовы.

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

1. Добавить проект `dynatrace`

```
oc adm new-project --node-selector="" dynatrace
```

2. Установить Dynatrace Operator

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/openshift.yaml
```

Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

```
oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
```

3. Создать секрет для токена доступа

Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

```
oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

4. Применить пользовательский ресурс DynaKube

Скачать [пример пользовательского ресурса DynaKube для наблюдаемости Kubernetes﻿](https://dt-url.net/sa038nu) из GitHub. Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube под свои требования.

Выполнить команду ниже, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Webhook валидации выведет полезные сообщения об ошибках, если возникнет проблема.

```
oc apply -f <your-DynaKube-CR>.yaml
```

5. Проверить развёртывание

Необязательно

Проверить, что DynaKube запущен и все поды в namespace Dynatrace работают и готовы.

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

## Дополнительные материалы

После успешной установки Dynatrace Operator следующие материалы могут быть полезны для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет разобраться с любыми трудностями, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами.

Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### Как это работает

Подробное описание того, как работает развёртывание на Kubernetes.

Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник

Содержит справочную страницу с параметрами конфигурации для каждого компонента Dynatrace

Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### Обновление или удаление Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по подбору размеров для Dynatrace ActiveGate в сценарии использования мониторинга Kubernetes

Установка лимитов ресурсов для Dynatrace ActiveGate

Руководство по подбору размеров для Dynatrace ActiveGate в сценарии использования мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Похожие темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")