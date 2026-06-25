---
title: Настройка мониторинга платформы Kubernetes с помощью DaemonSet
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset
scraped: 2026-05-12T11:52:06.234122
---

# Настройка мониторинга платформы Kubernetes с помощью DaemonSet

# Настройка мониторинга платформы Kubernetes с помощью DaemonSet

* Чтение: 4 мин
* Опубликовано 21 января 2020 г.

Устарело

Ручная настройка daemonset для развёртывания OneAgent в кластере Kubernetes устарела.

Рекомендуется использовать Dynatrace Operator и получить преимущества автоматического управления жизненным циклом и обогащения метаданными. Для наглядного представления всех стратегий развёртывания см. [Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works "Подробное описание того, как работает развёртывание в Kubernetes.").

На этой странице описано, как настроить OneAgent в Kubernetes с помощью OneAgent DaemonSet. DaemonSet, это функция, которая гарантирует, что если копия пода на узле завершает работу, она пересоздаётся, а при добавлении узлов в кластер копии пода также добавляются.

## Предварительные требования

* Поды должны разрешать исходящий трафик к вашему окружению Dynatrace или к вашему Environment ActiveGate, чтобы маршрутизация метрик работала корректно.
* Найдите `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация предоставляется во время установки Dynatrace OneAgent.

Как найти URL вашего установщика

Чтобы получить ваш `ONEAGENT_INSTALLER_SCRIPT_URL`

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Linux**.

3. Определите URL скрипта установщика и токен из команды `wget`, предоставленной в UI:

Версия образа контейнера OneAgent 1.39.1000+

Версия образа контейнера OneAgent 1.38.1000 и более ранние

Это URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

OneAgent URL

* Замените значение параметра `arch` на `<arch>`. Игнорируйте параметр `flavor=default`.
* Для значения `API-Token` требуется [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей действия.").

Ваш URL должен выглядеть так:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

Это ваш URL и токен API.

![OneAgent installation page with URL to be modified](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

OneAgent installation page with URL to be modified

Добавьте токен API к URL с помощью параметра `API-Token`. Ваш URL должен выглядеть так:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Установка DaemonSet

1. Скачайте или скопируйте шаблон Kubernetes `dynatrace-oneagent.yml`.

   dynatrace-oneagent.yml

   ```
   apiVersion: apps/v1



   kind: DaemonSet



   metadata:



   name: dynatrace-oneagent



   spec:



   selector:



   matchLabels:



   name: dynatrace-oneagent



   template:



   metadata:



   labels:



   name: dynatrace-oneagent



   spec:



   hostPID: true



   hostIPC: true



   hostNetwork: true



   nodeSelector:



   beta.kubernetes.io/os: linux



   volumes:



   - name: host-root



   hostPath:



   path: /



   containers:



   - name: dynatrace-oneagent



   image: dynatrace/oneagent



   env:



   - name: ONEAGENT_INSTALLER_SCRIPT_URL



   value: your_URL



   - name: ONEAGENT_INSTALLER_SKIP_CERT_CHECK



   value: 'false'



   - name: ONEAGENT_INSTALLER_DOWNLOAD_TOKEN



   value: '<API-Token>'



   args:



   - '--set-network-zone=<your.network.zone>'



   volumeMounts:



   - name: host-root



   mountPath: /mnt/root



   securityContext:



   privileged: true
   ```

   * `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` требуется только для версий образа контейнера OneAgent 1.39+ и игнорируется для более ранних версий.
   * Параметр `--set-app-log-content-access` передаётся установщику OneAgent и, когда задано значение `true` (или `1`), позволяет OneAgent получать доступ к файлам логов для целей мониторинга логов. Подробнее об этом и других параметрах см. [Настройка установки OneAgent в Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").
   * Сетевые зоны можно настроить, задав параметр `--set-network-zone=<your.network.zone>`. Подробнее см. [network zones](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").
2. Разверните Dynatrace OneAgent с помощью созданного файла `dynatrace-oneagent.yml`.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f dynatrace-oneagent.yml --namespace=kube-system



   daemonset "dynatrace-oneagent" created
   ```

   ```
   oc apply -f dynatrace-oneagent.yml --namespace=kube-system



   daemonset "dynatrace-oneagent" created
   ```
3. Убедитесь, что DaemonSet `dynatrace-oneagent` успешно развернул поды на узлы кластера:

   Kubernetes

   OpenShift

   ```
   kubectl get pods --namespace=kube-system



   NAME                       READY     STATUS              RESTARTS   AGE



   dynatrace-oneagent-abcde   1/1       Running             0          1m
   ```

   ```
   oc get pods --namespace=kube-system



   NAME                       READY     STATUS              RESTARTS   AGE



   dynatrace-oneagent-abcde   1/1       Running             0          1m
   ```

   Kubernetes

   OpenShift

   ```
   kubectl logs -f dynatrace-oneagent-abcde



   09:46:18 Using volume-based storage



   09:46:18 Started agent deployment as a Docker container, PID 1234.



   09:46:18 Downloading agent to /tmp/Dynatrace-OneAgent-Linux.sh via https://EnvironmentID.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=***&arch=x86&flavor=default



   09:46:21 Download complete



   09:46:21 Downloaded version: 1.x



   09:46:21 Validating downloaded agent installer



   09:46:23 Verification successful



   ...
   ```

   ```
   oc logs -f dynatrace-oneagent-abcde



   09:46:18 Using volume-based storage



   09:46:18 Started agent deployment as a Docker container, PID 1234.



   09:46:18 Downloading agent to /tmp/Dynatrace-OneAgent-Linux.sh via https://EnvironmentID.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=***&arch=x86&flavor=default



   09:46:21 Download complete



   09:46:21 Downloaded version: 1.x



   09:46:21 Validating downloaded agent installer



   09:46:23 Verification successful



   ...
   ```

## Ограничения

* При настройке мониторинга Kubernetes/OpenShift с помощью DaemonSet состояние выключения хоста не определяется. Подробнее см. [Состояния доступности хоста](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability#states "Проверьте доступность хоста, интерпретируйте состояния доступности хоста и узнайте, как окна обслуживания отражаются на графиках доступности хоста.").
* См. [Ограничения Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker.").

## Подключение ваших кластеров Kubernetes к Dynatrace

Теперь, когда OneAgent работает на ваших узлах Kubernetes, можно отслеживать эти узлы и приложения, работающие в Kubernetes. Следующий шаг, это подключение Kubernetes API к Dynatrace для получения нативных метрик Kubernetes, таких как лимиты запросов и различия между запрошенными и работающими подами.
Дальнейшие инструкции см. в разделе [Подключение ваших кластеров Kubernetes к Dynatrace](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet.").

## Обновление OneAgent DaemonSet

Каждый раз, когда в Dynatrace становится доступна новая версия OneAgent, можно повторно развернуть OneAgent, как описано в шагах ниже. Контейнер `dynatrace-oneagent` автоматически получит последнюю версию Dynatrace OneAgent.

Если в [настройках обновлений OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent в Linux.") задана версия установки OneAgent по умолчанию для новых хостов и приложений, контейнер `dynatrace-oneagent` автоматически получит заданную версию OneAgent по умолчанию.

1. Удалите DaemonSet `dynatrace-oneagent`.

   Kubernetes

   OpenShift

   ```
   kubectl delete ds/dynatrace-oneagent
   ```

   ```
   oc delete ds/dynatrace-oneagent
   ```
2. Разверните Dynatrace OneAgent с помощью [файла DaemonSet](#install) `dynatrace-oneagent.yml`.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f dynatrace-oneagent.yml --namespace=kube-system
   ```

   ```
   oc apply -f dynatrace-oneagent.yml --namespace=kube-system
   ```

## Удаление OneAgent DaemonSet

1. Удалите DaemonSet `dynatrace-oneagent`.

   Kubernetes

   OpenShift

   ```
   kubectl delete ds/dynatrace-oneagent
   ```

   ```
   oc delete ds/dynatrace-oneagent
   ```
2. Необязательно После удаления DaemonSet `dynatrace-oneagent` бинарный файл OneAgent остаётся на узле в неактивном состоянии. Чтобы удалить его полностью, запустите скрипт `uninstall.sh` и удалите логи и файлы конфигурации.
   См. [Информацию, связанную с Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Узнайте, как удалить OneAgent из вашей системы на базе Linux.").