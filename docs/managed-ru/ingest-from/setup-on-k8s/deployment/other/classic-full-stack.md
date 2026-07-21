---
title: Начало работы с полной наблюдаемостью (классическое full-stack развёртывание)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack
---

# Начало работы с полной наблюдаемостью (классическое full-stack развёртывание)

# Начало работы с полной наблюдаемостью (классическое full-stack развёртывание)

* 8 минут чтения
* Обновлено 05 сентября 2025 г.

Этот режим развёртывания поддерживается Dynatrace, но больше не рекомендуется для большинства сред.

Режим Classic Full-Stack не поддерживается при использовании [platform token](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

На этой странице приведены инструкции по развёртыванию Dynatrace Operator в конфигурации classic full-stack в кластере Kubernetes.

Предварительные требования

Перед установкой Dynatrace в кластере Kubernetes убедись, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* На мониторируемом кластере достаточно прав для выполнения команд `kubectl` или `oc`. Если роль кластера `cluster-admin` не используется, см. [права доступа для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых прав доступа") для нужных прав.

### Настройка и конфигурация кластера

* Нужно разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию, namespace Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используй [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

## Варианты установки

Выбери **один из способов установки**, наиболее подходящий для твоих задач.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению Helm используют наш чарт Helm, доступный в реестре OCI. Поэтому, если репозиторий Dynatrace в данный момент добавлен в локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используется Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установи Dynatrace Operator

   Если используется Helm версии 4.0+, нужно использовать флаг `--rollback-on-failure` вместо `--atomic`.

   Следующая команда подходит как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --set csidriver.enabled="false" \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной конфигурацией чарта Helm

   Отредактируй пример [`values.yaml`﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/config/helm/chart/default/values.yaml) из GitHub, а затем выполни команду установки, передав файл YAML в качестве аргумента:

   Обязательно отключи развёртывание CSI-драйвера Dynatrace Operator, поскольку он не используется в classic full-stack.

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

   Если для `installCRD` установлено значение `false`, перед началом установки Helm нужно вручную создать определение пользовательского ресурса:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/dynatrace-operator-crd.yaml
   ```
2. Создай секрет для токена доступа

   Создай секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и права доступа](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав доступа для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Примени пользовательский ресурс DynaKube

   Скачай [пример пользовательского ресурса DynaKube для classic full-stack из GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/assets/samples/dynakube/v1beta5/classicFullStack.yaml). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования"), и адаптировать пользовательский ресурс DynaKube под свои требования.

   Выполни приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Webhook валидации предоставит полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Опционально Проверь развёртывание

   Убедись, что твой DynaKube запущен и все поды в namespace Dynatrace запущены и готовы.

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

   Поскольку OneAgent развёрнут как DaemonSet, на каждом узле должен быть под OneAgent.

## Манифест

Kubernetes

OpenShift

1. Создать пространство имён `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/kubernetes.yaml
   ```

   Чтобы узнать, когда компоненты Dynatrace Operator завершат инициализацию, выполнить команду:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токена доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и права доступа](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав доступа для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Применить пользовательский ресурс DynaKube

   Скачать [образец пользовательского ресурса DynaKube для classic full-stack из GitHub﻿](https://dt-url.net/ei436pt). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии со своими требованиями.

   Выполнить приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Webhook валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен и все поды в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   При конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Поскольку OneAgent развёртывается как DaemonSet, на каждом узле должен быть под OneAgent.

1. Добавить проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/openshift.yaml
   ```

   Чтобы узнать, когда компоненты Dynatrace Operator завершат инициализацию, выполнить команду:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токена доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Требуемые токены и права доступа](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав доступа для мониторинга кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Применить пользовательский ресурс DynaKube

   Скачать [образец пользовательского ресурса DynaKube для classic full-stack из GitHub﻿](https://dt-url.net/ei436pt). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии со своими требованиями.

   Выполнить приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Webhook валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен и все поды в проекте Dynatrace работают и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   При конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Поскольку OneAgent развёртывается как DaemonSet, на каждом узле должен быть под OneAgent.

## Дополнительные материалы

После успешной установки Dynatrace Operator следующие ресурсы могут пригодиться для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет разобраться с трудностями, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами.

Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### Как это работает

Подробное описание того, как работает развёртывание на Kubernetes.

Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справка

Содержит справочную страницу с параметрами настройки для каждого компонента Dynatrace

Справка](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### Обновление или удаление Dynatrace Operator

Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по определению размера ActiveGate Dynatrace для сценария мониторинга Kubernetes

Настройка лимитов ресурсов для ActiveGate Dynatrace

Руководство по определению размера ActiveGate Dynatrace для сценария мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")