---
title: Начало работы с мониторингом хостов
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/host-monitoring
---

# Начало работы с мониторингом хостов

# Начало работы с мониторингом хостов

* Время чтения: 6 минут
* Обновлено 05 сентября 2025 г.

На этой странице приведены инструкции по развёртыванию оператора Dynatrace в конфигурации мониторинга хостов в кластере Kubernetes.

Если нужен более полный обзор среды, включающий такие аспекты, как наблюдаемость приложений и пользовательский опыт, стоит рассмотреть подход полной облачно-нативной наблюдаемости Kubernetes, например [cloud-native full-stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развернуть оператор Dynatrace в режиме cloud-native full-stack в Kubernetes") или [classic full-stack](/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Развернуть оператор Dynatrace в режиме classic full-stack в Kubernetes").

Предварительные требования

Перед установкой Dynatrace в кластере Kubernetes нужно убедиться, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* Есть достаточные привилегии в мониторируемом кластере для выполнения команд `kubectl` или `oc`. Если роль кластера `cluster-admin` не используется, см. [права для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых прав") для получения информации о необходимых правах.

### Настройка и конфигурация кластера

* Нужно разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Использовать [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

Сочетание `hostMonitoring` и `applicationMonitoring` в кластере Kubernetes в одной и той же среде не поддерживается.

## Варианты установки

Выберите **один из способов установки**, наиболее подходящий для ваших задач.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Манифест**](#manifest)

## Helm

Оператор Dynatrace версии 0.8.0 и выше

1. Установка оператора Dynatrace

   При использовании Helm версии 4.0 и выше нужно использовать флаг `--rollback-on-failure` вместо `--atomic`.

   Следующая команда подходит как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной конфигурацией чарта Helm

   Отредактируйте образец [`values.yaml`﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/config/helm/chart/default/values.yaml) из GitHub, а затем выполните команду установки, передав файл YAML в качестве аргумента:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Если для `installCRD` установлено значение `false`, нужно вручную создать определение пользовательского ресурса перед началом установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/dynatrace-operator-crd.yaml
   ```
2. Создание секрета для токена доступа

   Создайте секрет с именем `dynakube` для токена оператора Dynatrace, полученного в разделе [Требуемые токены и права](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и прав для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Применение пользовательского ресурса DynaKube

   Скачайте [образец пользовательского ресурса DynaKube для мониторинга хостов из GitHub﻿](https://dt-url.net/qx8363l). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки оператора Dynatrace в Kubernetes.") или [руководствами по настройке](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и конфигурации для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии со своими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. Веб-хук проверки предоставит полезные сообщения об ошибках при возникновении проблем.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Опционально Проверка развёртывания

   Убедитесь, что DynaKube запущен и все поды в пространстве имён Dynatrace выполняются и готовы к работе.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI-драйвером оператора Dynatrace должны отображаться следующие поды:

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

   Поскольку OneAgent и CSI-драйвер развёрнуты как DaemonSet, на каждом узле должен быть под OneAgent и CSI-драйвера.

## Манифест

Kubernetes

OpenShift

1. Создать пространство имён `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установить Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/kubernetes-csi.yaml
   ```

   Выполнить следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создать секрет для токена доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Токены и необходимые разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Применить пользовательский ресурс DynaKube

   Скачать [пример пользовательского ресурса DynaKube для мониторинга хостов из GitHub﻿](https://dt-url.net/qx8363l). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии со своими требованиями.

   Если нужно снизить количество тарифицируемых единиц, включить режим Infrastructure Monitoring в конфигурации DynaKube.

   ```
   oneAgent:



   hostMonitoring:



   args:



   - --set-monitoring-mode=infra-only
   ```

   Выполнить приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. При наличии проблемы validation webhook выдаст понятные сообщения об ошибке.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен и все Pod'ы в пространстве имён Dynatrace работают и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI-драйвером Dynatrace Operator должны отображаться следующие Pod'ы:

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

   Поскольку OneAgent и CSI-драйвер развёрнуты как DaemonSet, на каждом узле должны присутствовать Pod OneAgent и Pod CSI-драйвера.

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
3. Создать секрет для токена доступа

   Создать секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Токены и необходимые разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Применить пользовательский ресурс DynaKube

   Скачать [пример пользовательского ресурса DynaKube для мониторинга хостов из GitHub﻿](https://dt-url.net/qx8363l). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") или [пошаговыми руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптировать пользовательский ресурс DynaKube в соответствии со своими требованиями.

   Выполнить приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла пользовательского ресурса DynaKube. При наличии проблемы validation webhook выдаст понятные сообщения об ошибке.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно Проверить развёртывание

   Убедиться, что DynaKube запущен и все Pod'ы в пространстве имён Dynatrace работают и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI-драйвером Dynatrace Operator должны отображаться следующие Pod'ы:

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

   Поскольку OneAgent и CSI-драйвер развёрнуты как DaemonSet, на каждом узле должны присутствовать Pod OneAgent и Pod CSI-драйвера.

## Узнать больше

После успешной установки Dynatrace Operator следующие ресурсы могут быть полезны для дальнейшего изучения и устранения неполадок.

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

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по подбору размера ActiveGate Dynatrace для сценария мониторинга Kubernetes

Настройка лимитов ресурсов для ActiveGate Dynatrace

Руководство по подбору размера ActiveGate Dynatrace для сценария мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")