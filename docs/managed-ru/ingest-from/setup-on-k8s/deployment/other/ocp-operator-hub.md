---
title: Настройка мониторинга OpenShift через OperatorHub
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub
scraped: 2026-05-12T11:52:46.602247
---

# Настройка мониторинга OpenShift через OperatorHub

# Настройка мониторинга OpenShift через OperatorHub

* Чтение: 2 мин
* Обновлено 20 марта 2026 г.

OperatorHub, это интерфейс, который администраторы кластера используют для обнаружения и установки операторов; он доступен через веб-консоль OpenShift Container Platform.

## Предварительные требования для OpenShift Dedicated

* Пользователь dedicated-admin для кластера OpenShift Dedicated

Как добавить пользователя в роль dedicated-admin

1. Войдите в [Red Hat OpenShift Cluster Manager](https://cloud.redhat.com/openshift) под вашей учётной записью Red Hat.
2. Выберите кластер OpenShift Dedicated и перейдите в **Access control** > **Cluster administrative users** > **Add user**.
3. Добавьте userid пользователя, который получит доступ dedicated-admin.

Пользователь dedicated-admin должен быть добавлен до того, как OneAgent Operator станет виден в интерфейсе OperatorHub.

## Ограничения

Варианты развёртывания, которые можно установить из OperatorHub:

* [Мониторинг платформы Kubernetes](https://docs.dynatrace.com/docs/shortlink/installation-k8s-platform-only)
* [Мониторинг Classic Full-Stack](https://docs.dynatrace.com/docs/shortlink/installation-k8s-classic-fs)
* [Application observability](https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-monitoring) без CSI driver
* [Full-Stack observability](https://docs.dynatrace.com/docs/shortlink/node-image-pull) без CSI driver

Варианты развёртывания, которые **нельзя** установить из OperatorHub (они требуют установки через Helm или манифест):

* [Full-Stack observability](https://docs.dynatrace.com/docs/shortlink/installation-k8s-cloud-native-fs) с CSI driver
* [Application observability](https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-monitoring) с CSI driver
* [Host monitoring](https://docs.dynatrace.com/docs/shortlink/k8s-host-monitoring)

## Установка

Чтобы установить Dynatrace Operator в OpenShift через OperatorHub

1. На панели OpenShift Container Platform выберите **Operators** > **OperatorHub** в боковом меню.
2. Выберите **Dynatrace Operator** > **Install**.
3. Введите необходимую информацию о подписке Operator.
4. В **Installation Mode** выберите **All namespaces**.
5. Оставьте значения по умолчанию для остальных настроек и выберите **Subscribe**.
6. Перейдите в **Operators** > **Installed Operators** и дождитесь появления **Install Succeeded**.
7. Перейдите в **Workloads** > **Secrets** и создайте новый ключ с именем `dynakube` с двумя значениями:

   * `apiToken`, равный [токену Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes") вашего кластера.
   * `dataIngestToken`, равный [токену Data Ingest](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes") вашего кластера.
8. Перейдите в **Operators** > **Installed Operators** в боковом меню и выберите **Dynatrace Operator**.
9. Выберите **Create instance**.
10. Внесите следующие изменения:

    * Замените значение `apiURL` в соответствии с вашим развёртыванием:

      Dynatrace SaaS

      ```
      spec:



      apiURL: 'https://ENVIRONMENTID.live.dynatrace.com/api'
      ```

      Замените `ENVIRONMENTID` на ваш [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Поймите и узнайте, как работать с окружениями мониторинга.").

      Dynatrace Managed

      ```
      spec:



      apiURL: 'https://<YourDynatraceServerURL>/e/<ENVIRONMENTID>/api'
      ```

      Замените `YourDynatraceServerURL` на адрес вашего Dynatrace Managed Cluster, а `ENVIRONMENTID` на ваш [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Поймите и узнайте, как работать с окружениями мониторинга.").
    * Установите `classicFullStack.enabled` в `true`.
    * Если вы используете файл пользовательского ресурса, установите `namespace` равным пространству имён, в которое установлен Dynatrace Operator.
11. Выберите **Create**.