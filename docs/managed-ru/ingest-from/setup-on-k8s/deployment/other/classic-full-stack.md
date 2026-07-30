---
title: Начало работы с полной наблюдаемостью (классическое развёртывание full-stack)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack
---

# Начало работы с полной наблюдаемостью (классическое развёртывание full-stack)

# Начало работы с полной наблюдаемостью (классическое развёртывание full-stack)

* 8 мин чтения
* Обновлено 05 сентября 2025

Этот режим развёртывания поддерживается Dynatrace, но больше не рекомендуется для большинства сред.

Classic Full-Stack режим не поддерживается при использовании [platform token](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

На этой странице приведены инструкции по развёртыванию Dynatrace Operator в конфигурации classic full-stack на кластере Kubernetes.

Предварительные требования

Перед установкой Dynatrace на кластер Kubernetes убедитесь, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* На мониторируемом кластере достаточно привилегий для выполнения команд `kubectl` или `oc`. Если роль `cluster-admin` кластера не используется, см. [deployment permissions](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице приведён обзор компонентов Dynatrace, их конфигурации по умолчанию и необходимых разрешений") для получения информации о необходимых разрешениях.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated требуется [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используйте [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы") и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.

## Варианты установки

Выберите **один из методов установки**, наиболее подходящий для ваших задач.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению Helm используют Helm chart из OCI registry. Если репозиторий Dynatrace добавлен в локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используется Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установка Dynatrace Operator

   При использовании Helm версии 4.0+ нужно использовать `--rollback-on-failure` вместо флага `--atomic`.

   Следующая команда подходит как для стандартных установок, так и для установок с использованием OCI registry.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --set csidriver.enabled="false" \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной конфигурацией Helm chart

   Отредактируйте образец [`values.yaml`﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/config/helm/chart/default/values.yaml) из GitHub, затем выполните команду установки, передав файл YAML в качестве аргумента:

   Нужно отключить развёртывание CSI driver Dynatrace Operator, так как он не используется в classic full-stack.

   ```
   csidriver:



   enabled: false
   ```

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Если `installCRD` установлено в `false`, нужно создать custom resource definition вручную перед началом установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```
2. Создание секрета для токена доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Применение DynaKube custom resource

   Скачайте [образец DynaKube custom resource для classic full-stack из GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/assets/samples/dynakube/v1beta5/classicFullStack.yaml). Также можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и конфигурации для конкретных случаев использования") и настроить DynaKube custom resource под свои требования.

   Выполните приведённую ниже команду для применения DynaKube custom resource, заменив `<your-DynaKube-CR>` на фактическое имя файла DynaKube custom resource. При наличии проблем validation webhook выдаст полезные сообщения об ошибках.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Optional Проверка развёртывания

   Убедитесь, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие поды:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-2wnbb               1/1     Running   0               50s



   dynakube-oneagent-wp2bt               1/1     Running   0               50s



   dynakube-oneagent-pxdv4               1/1     Running   0               50s



   dynatrace-operator-8445c87f87-qhc5t   1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-ws7gg    1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-xkxkd    1/1     Running   0               3m02s
   ```

   Поскольку OneAgent развёртывается как DaemonSet, на каждом узле должен присутствовать под OneAgent.

## Manifest

Kubernetes

OpenShift

1. Создать пространство имён `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes.yaml
   ```

   Выполнить следующую команду, чтобы отследить завершение инициализации компонентов Dynatrace Operator:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токена доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Применить custom resource DynaKube

   Скачать [пример custom resource DynaKube для classic full-stack из GitHub﻿](https://dt-url.net/ei436pt). Дополнительно можно изучить [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать custom resource DynaKube под свои требования.

   Выполнить команду ниже для применения custom resource DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла custom resource DynaKube. Validation webhook выдаст понятные сообщения об ошибках при наличии проблем.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Проверить развёртывание

   Убедиться, что DynaKube запущен и все Pod'ы в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие Pod'ы:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-2wnbb               1/1     Running   0               50s



   dynakube-oneagent-wp2bt               1/1     Running   0               50s



   dynakube-oneagent-pxdv4               1/1     Running   0               50s



   dynatrace-operator-8445c87f87-qhc5t   1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-ws7gg    1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-xkxkd    1/1     Running   0               3m02s
   ```

   Поскольку OneAgent развёртывается как DaemonSet, на каждом узле должен присутствовать Pod OneAgent.

1. Добавить проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift.yaml
   ```

   Выполнить следующую команду, чтобы отследить завершение инициализации компонентов Dynatrace Operator:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токена доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Применить custom resource DynaKube

   Скачать [пример custom resource DynaKube для classic full-stack из GitHub﻿](https://dt-url.net/ei436pt). Дополнительно можно изучить [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать custom resource DynaKube под свои требования.

   Выполнить команду ниже для применения custom resource DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла custom resource DynaKube. Validation webhook выдаст понятные сообщения об ошибках при наличии проблем.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Проверить развёртывание

   Убедиться, что DynaKube запущен и все Pod'ы в проекте Dynatrace работают и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отображаться следующие Pod'ы:

   ```
   > oc get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-2wnbb               1/1     Running   0               50s



   dynakube-oneagent-wp2bt               1/1     Running   0               50s



   dynakube-oneagent-pxdv4               1/1     Running   0               50s



   dynatrace-operator-8445c87f87-qhc5t   1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-ws7gg    1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-xkxkd    1/1     Running   0               3m02s
   ```

   Поскольку OneAgent развёртывается как DaemonSet, на каждом узле должен присутствовать Pod OneAgent.

## Подробнее

После успешной установки Dynatrace Operator следующие материалы помогут в дальнейшем изучении и устранении неполадок.

[#### Guides

Подробное описание параметров установки и настройки для конкретных сценариев использования

Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting

Эта страница помогает в решении проблем, возникающих при работе с Dynatrace Operator и его компонентами.

Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### How it works

Подробное описание принципов работы развёртывания на Kubernetes.

How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference

Справочная страница с параметрами конфигурации для каждого компонента Dynatrace

Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace Operator release notes

Release notes для Dynatrace Operator

Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)[#### Update or uninstall Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Size Dynatrace ActiveGates in Kubernetes

Рекомендации по ресурсам CPU и памяти для Dynatrace ActiveGates, развёрнутых в Kubernetes, с учётом масштаба кластера и типа рабочей нагрузки.

Size Dynatrace ActiveGates in Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")