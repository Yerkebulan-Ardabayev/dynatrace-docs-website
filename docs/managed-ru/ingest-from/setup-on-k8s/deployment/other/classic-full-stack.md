---
title: Начало работы с полной наблюдаемостью (развёртывание classic full-stack)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack
scraped: 2026-05-12T11:52:48.667887
---

# Начало работы с полной наблюдаемостью (развёртывание classic full-stack)

# Начало работы с полной наблюдаемостью (развёртывание classic full-stack)

* Чтение: 8 мин
* Обновлено 5 сентября 2025 г.

Этот режим развёртывания поддерживается Dynatrace, но больше не рекомендуется для большинства окружений.

На этой странице приведены инструкции по развёртыванию Dynatrace Operator в конфигурации classic full-stack в кластере Kubernetes.

Предварительные требования

Перед установкой Dynatrace в вашем кластере Kubernetes убедитесь, что вы соответствуете следующим требованиям:

* Ваш `kubectl` CLI подключён к кластеру Kubernetes, который требуется отслеживать.
* У вас достаточно привилегий в отслеживаемом кластере для выполнения команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL-адресу вашего окружения Dynatrace.

  + Для Dynatrace Managed можно дополнительно использовать URL-адрес Cluster ActiveGate.
* Для OpenShift Dedicated необходима [роль cluster-admin](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm. Используйте [Helm version 3](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы") и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.

## Варианты установки

Выберите **один из методов установки**, который лучше всего соответствует вашим потребностям.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению Helm используют наш Helm chart, доступный из реестра OCI. Поэтому, если репозиторий Dynatrace в настоящее время добавлен в ваши локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используете ли вы Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установите Dynatrace Operator

   Если вы используете Helm версии 4.0+, необходимо использовать `--rollback-on-failure` вместо флага `--atomic`.

   Следующая команда работает как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --set csidriver.enabled="false" \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной настройкой Helm chart

   Отредактируйте пример [`values.yaml`](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) из GitHub, а затем выполните команду установки, передав YAML-файл как аргумент:

   Убедитесь, что развёртывание Dynatrace Operator CSI driver отключено, так как он не используется в classic full-stack.

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

   Если для `installCRD` задано значение `false`, необходимо создать определение пользовательского ресурса вручную перед началом установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```
2. Создайте секрет для токена доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Примените пользовательский ресурс DynaKube

   Загрузите [пример пользовательского ресурса DynaKube для classic full-stack из GitHub](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/assets/samples/dynakube/v1beta5/classicFullStack.yaml). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптируйте пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук предоставит полезные сообщения об ошибках при наличии проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно. Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [пример пользовательского ресурса DynaKube для classic full-stack из GitHub](https://dt-url.net/ei436pt). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптируйте пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук предоставит полезные сообщения об ошибках при наличии проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно. Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator, полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [пример пользовательского ресурса DynaKube для classic full-stack из GitHub](https://dt-url.net/ei436pt). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования") и адаптируйте пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук предоставит полезные сообщения об ошибках при наличии проблемы.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно. Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен и все поды в вашем проекте Dynatrace запущены и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

## Узнать больше

После успешной установки Dynatrace Operator следующие ресурсы могут оказаться полезными для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев использования

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет вам справиться с любыми трудностями, с которыми можно столкнуться при работе с Dynatrace Operator и его различными компонентами.

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

Задайте лимиты ресурсов для Dynatrace ActiveGate

Руководство по выбору размера для Dynatrace ActiveGate в сценарии мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")