---
title: Настройка мониторинга OpenShift через OperatorHub
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub
scraped: 2026-03-06T21:32:57.570952
---

* 2 минуты на чтение

OperatorHub — это интерфейс, с помощью которого администраторы кластера обнаруживают и устанавливают операторы. Он доступен через веб-консоль OpenShift Container Platform.

## Предварительные требования для OpenShift Dedicated

* Пользователь с ролью dedicated-admin для кластера OpenShift Dedicated

Как добавить пользователя в роль dedicated-admin:

1. Войдите в [Red Hat OpenShift Cluster Manager](https://cloud.redhat.com/openshift) с учётной записью Red Hat.
2. Выберите кластер OpenShift Dedicated и перейдите в **Access control** > **Cluster administrative users** > **Add user**.
3. Добавьте идентификатор пользователя, которому будет предоставлен доступ dedicated-admin.

Пользователь с ролью dedicated-admin должен быть добавлен до того, как оператор OneAgent станет видимым в пользовательском интерфейсе OperatorHub.

## Ограничения

Варианты развёртывания, которые можно установить через OperatorHub:

* Мониторинг платформы Kubernetes
* Классический мониторинг Full-Stack
* Наблюдаемость приложений без CSI-драйвера

Варианты развёртывания, которые **нельзя** установить через OperatorHub (для них требуется установка с помощью Helm или манифестов):

* Полная наблюдаемость Full-Stack
* Наблюдаемость приложений с CSI-драйвером
* Мониторинг хоста

## Установка

Чтобы установить Dynatrace Operator на OpenShift через OperatorHub:

1. На панели управления OpenShift Container Platform выберите **Operators** > **OperatorHub** в боковом меню.
2. Выберите **Dynatrace Operator** > **Install**.
3. Введите необходимые сведения о подписке на оператор.
4. В разделе **Installation Mode** выберите **All namespaces**.
5. Оставьте значения по умолчанию для остальных настроек и нажмите **Subscribe**.
6. Перейдите в **Operators** > **Installed Operators** и дождитесь появления сообщения **Install Succeeded**.
7. Перейдите в **Workloads** > **Secrets** и создайте новый ключ с именем `dynakube`, содержащий два значения:

   * `apiToken` — равен токену Dynatrace Operator вашего кластера.
   * `dataIngestToken` — равен токену приёма данных вашего кластера.
8. Перейдите в **Operators** > **Installed Operators** в боковом меню и выберите **Dynatrace Operator**.
9. Нажмите **Create instance**.
10. Внесите следующие изменения:

    * Замените значение `apiURL` в соответствии с вашим развёртыванием:

      Dynatrace

      ```
      spec:


      apiURL: 'https://ENVIRONMENTID.live.dynatrace.com/api'
      ```

      Замените `ENVIRONMENTID` на ваш идентификатор среды.
    * Установите `classicFullStack.enabled` в значение `true`.
    * Если вы используете файл пользовательского ресурса, задайте `namespace` — пространство имён, в котором установлен Dynatrace Operator.
11. Нажмите **Create**.
