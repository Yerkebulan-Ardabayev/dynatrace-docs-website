---
title: Начало работы с полной observability Kubernetes (развёртывание cloud-native full-stack)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed
scraped: 2026-05-12T11:52:52.580162
---

# Начало работы с полной observability Kubernetes (развёртывание cloud-native full-stack)

# Начало работы с полной observability Kubernetes (развёртывание cloud-native full-stack)

* Обновлено 06 ноября 2023 г.

На этой странице приведены инструкции по установке Dynatrace Operator с конфигурацией cloud-native full-stack в кластер Kubernetes.

Предварительные требования

Перед установкой Dynatrace в кластере Kubernetes убедитесь, что выполнены следующие требования:

* Ваш CLI `kubectl` подключён к кластеру Kubernetes, который требуется мониторить.
* На отслеживаемом кластере достаточно прав для запуска команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL вашего окружения Dynatrace.

  + Для Dynatrace Managed дополнительно можно использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated необходима [роль cluster-admin](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm: используйте [Helm версии 3](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.

По умолчанию Dynatrace Operator внедряет OneAgent во все пространства имён, но его можно настроить на мониторинг только определённых пространств имён и исключение остальных. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#monitor-only-specific-namespaces "Настройка мониторинга для пространств имён и подов").

[Настройка SCC](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Dynatrace Operator в окружениях OpenShift.") требуется для OpenShift при развёртываниях `cloudNativeFullStack` и `applicationMonitoring` с CSI driver.

## Варианты установки

Выберите **один из методов установки**, который лучше всего подходит под ваши потребности.

[![Dynatrace UI](https://dt-cdn.net/images/search-color-945bb8b42a.svg "Dynatrace UI")

**С помощью мастера (Dynatrace UI)**](#guided)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## С помощью мастера (Dynatrace UI)

Dynatrace версии 1.290+

1. Перейдите в **Kubernetes**.
2. Выберите **Connect automatically via Dynatrace Operator** в заголовке страницы кластера Kubernetes.

![Quickstart](https://dt-cdn.net/images/quickstart-3574-833bd4c27b.png)

Quickstart

1. Введите следующие сведения.

   * **Name**: задаёт отображаемое имя вашего кластера Kubernetes в Dynatrace. Кроме того, это имя используется как префикс для именования ресурсов, специфичных для Dynatrace, внутри вашего кластера Kubernetes, таких как DynaKube (пользовательский ресурс), ActiveGate (под), OneAgents (поды), а также как имя секрета, хранящего ваши токены.
   * Рекомендуется **Group**: задаёт группу, используемую различными настройками Dynatrace, включая network zone, группу ActiveGate и группу хостов. Если не задано, используются значения по умолчанию или пустые значения.
   * **Dynatrace Operator token**: выберите **Create token** или введите **API token**, созданный ранее. Подробнее см. [Токены доступа и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").
   * Необязательно**Data ingest token**: выберите **Create token** или введите **API token**, созданный ранее. Подробнее см. [Токены доступа и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").
2. Необязательно. Решите, должен ли Dynatrace Operator отключить проверку SSL-сертификата Dynatrace.

   Это актуально при использовании Dynatrace Managed с самоподписанными сертификатами.
3. Выберите **Download dynakube.yaml**. Скопируйте блок кода, созданный Dynatrace, и **запустите его в терминале**. Убедитесь, что команды выполняются в том же каталоге, куда был загружен YAML, либо адаптируйте команду так, чтобы она ссылалась на расположение YAML-манифеста.

   Загруженный файл YAML является базовой версией определения пользовательского ресурса DynaKube. Чтобы скорректировать значения под ваши конкретные нужды, обратитесь к [образцам пользовательского ресурса DynaKube для cloud-native full-stack на GitHub](https://dt-url.net/9n636jg). Подробнее обо всех вариантах конфигурации см. [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").
4. Необязательно. Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению через Helm используют наш Helm chart, доступный из реестра OCI. Поэтому если репозиторий Dynatrace в данный момент добавлен в ваши локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используете вы Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установите Dynatrace Operator

   Следующая команда подходит как для установок по умолчанию, так и для установок с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Установка с дополнительной настройкой Helm chart

   Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) с GitHub, затем выполните команду установки, передав файл YAML как аргумент:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Для развёртываний cloud native full stack CSI driver обязателен. Если `installCRD` установлен в `false`, необходимо создать определение пользовательского ресурса вручную перед запуском установки Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").
2. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для cloud-native full-stack с GitHub](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук выдаст полезные сообщения об ошибках при наличии проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Необязательно. Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

## Manifest

Kubernetes

OpenShift

1. Создайте пространство имён `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют [дополнительной настройки](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для cloud-native full-stack с GitHub](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук выдаст полезные сообщения об ошибках при наличии проблемы.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно. Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

1. Добавьте проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
   ```

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Требуемые токены и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените пользовательский ресурс DynaKube

   Загрузите [образец пользовательского ресурса DynaKube для cloud-native full-stack с GitHub](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев") и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук выдаст полезные сообщения об ошибках при наличии проблемы.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Необязательно. Проверьте развёртывание

   Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён Dynatrace запущены и готовы.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:

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

   Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на каждом узле должен быть под OneAgent и под CSI-driver.

## Узнать больше

После успешной установки Dynatrace Operator следующие ресурсы могут оказаться полезными для дальнейшего изучения и устранения неполадок.

[#### Руководства

Подробное описание вариантов установки и настройки для конкретных сценариев

Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок

Эта страница поможет справиться с любыми трудностями, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами.

Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### Как это работает

Подробное описание того, как работает развёртывание в Kubernetes.

Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник

Содержит справочную страницу с вариантами конфигурации для каждого компонента Dynatrace

Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Release notes Dynatrace Operator

Release notes для Dynatrace Operator

Release notes Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### Обновление или удаление Dynatrace Operator

Процедуры обновления и удаления Dynatrace Operator

Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Руководство по выбору размера для Dynatrace ActiveGates в сценарии мониторинга Kubernetes

Задайте лимиты ресурсов для Dynatrace ActiveGates

Руководство по выбору размера для Dynatrace ActiveGates в сценарии мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Связанные темы

* [Гибкая, масштабируемая, самообслуживаемая нативная observability Kubernetes теперь в General Availability](https://www.dynatrace.com/news/blog/flexible-scalable-self-service-kubernetes-native-observability/)