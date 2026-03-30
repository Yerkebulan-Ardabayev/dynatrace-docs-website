---
title: Мониторинг Kubernetes API
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring
scraped: 2026-03-06T21:21:58.424568
---

* Latest Dynatrace

Dynatrace получает информацию о сущностях и метаданных Kubernetes, опрашивая Kubernetes API. Эта информация используется для предустановленных оповещений Kubernetes и для предоставления всех сигналов наблюдаемости в надлежащем контексте Kubernetes в платформе Dynatrace, например, путём создания связей между приложениями, (микро-)сервисами, базами данных и сущностями Kubernetes, такими как поды, пространства имён и узлы.

Dynatrace Operator управляет жизненным циклом всех компонентов Dynatrace в кластере Kubernetes и может быть настроен путём развёртывания пользовательского ресурса DynaKube. Dynatrace ActiveGate — компонент Dynatrace, необходимый для мониторинга Kubernetes API — предоставляет возможность мониторинга Kubernetes API.

Выполните следующие шаги для включения мониторинга Kubernetes API.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установка Dynatrace Operator**](#install-dto)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка DynaKube**](#configure-dynakube)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Подключение ActiveGate к Kubernetes API**](#connect-ag)

## Шаг 1. Установка Dynatrace Operator

Установите Dynatrace Operator в любом режиме развёртывания

## Шаг 2. Настройка DynaKube

Настройте значения **ActiveGate** в DynaKube в соответствии со [списком параметров](../../../reference/dynakube-parameters.md#ag "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") и добавьте `kubernetes-monitoring` в возможности ActiveGate.

```
...


activeGate:


capabilities:


- routing


- kubernetes-monitoring


...
```

## Шаг 3. Подключение ActiveGate к Kubernetes API

У вас есть два варианта:

* Подключить контейнеризованный ActiveGate к локальной конечной точке Kubernetes API.
* Подключить контейнеризованный ActiveGate к публичному URL Kubernetes API.

Ниже приведены инструкции для обоих вариантов.

### Подключение к локальной конечной точке Kubernetes API

Вы можете включить мониторинг, подключив контейнеризованный ActiveGate к локальной конечной точке Kubernetes API.

Есть два способа подключения к локальной конечной точке Kubernetes API:

* Рекомендуемый: [Позволить Dynatrace Operator автоматически обработать подключение](#auto)
* [Настроить подключение вручную](#manual)

Ниже приведены подробности для обоих методов.

Автоматическое подключение

Ручное подключение

Этот флаг функции устарел и включён по умолчанию начиная с Dynatrace Operator версии 0.13.0.

Для автоматического подключения к локальной конечной точке Kubernetes API

1. Убедитесь, что для вашего токена доступа включены разрешения **Read entities**, **Read settings** и **Write settings** (API v2) (см. Токены доступа и разрешения).
2. Убедитесь, что в вашем пользовательском ресурсе DynaKube включена возможность `kubernetes-monitoring`.
3. Добавьте следующую аннотацию (см. пример ниже).

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: dynakube


   namespace: dynatrace


   annotations:


   feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"


   spec:


   ...


   activeGate:


   capabilities:


   - kubernetes-monitoring
   ```

   После добавления этой аннотации имя кластера, отображаемое в Dynatrace, будет совпадать с именем пользовательского ресурса DynaKube, в котором настроена аннотация. Вы можете изменить имя кластера, отображаемое в Dynatrace, добавив также аннотацию `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"`.

   Пример с пользовательским именем кластера:

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: dynakube


   namespace: dynatrace


   annotations:


   feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"


   feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"


   spec:


   ...


   activeGate:


   capabilities:


   - kubernetes-monitoring
   ```
4. Примените вашу конфигурацию.

   Чтобы отключить конфигурацию, удалите аннотацию.

Для ручного подключения к локальной конечной точке Kubernetes API вам нужно предоставить только уникальный идентификатор кластера Kubernetes (UUID пространства имён kube-system). Контейнеризованный ActiveGate затем определяет уникальный идентификатор кластера и отправляет его в Dynatrace.

#### Шаг 1. Получение идентификатора кластера Kubernetes

Выполните приведённую ниже команду и скопируйте UID из вывода.

Kubernetes

OpenShift

```
kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
```

```
oc get namespace kube-system -o jsonpath='{.metadata.uid}'
```

#### Шаг 2. Указание идентификатора кластера Kubernetes в Dynatrace

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Выберите **Connect manually**.
3. На странице настроек подключения кластера Kubernetes укажите **Name**, затем включите **Connect containerized ActiveGate to local Kubernetes API endpoint**.
4. В поле **Kubernetes cluster ID** введите UID, полученный ранее.
5. Нажмите **Save changes** для сохранения конфигурации.

   Вы можете сохранить конфигурацию, даже если ActiveGate ещё не готов к подключению, и завершить настройку позже. Чтобы проверить готовность, нажмите **Test configuration**.

### Подключение к публичному Kubernetes API

Для подключения к публичному Kubernetes API следуйте инструкциям, соответствующим вашей версии Kubernetes:

* [Kubernetes версии 1.24+](#k8s-new)
* [Kubernetes версии ранее 1.24](#k8s-old)

#### Kubernetes версии 1.24+

1. Получите URL Kubernetes API.

   Kubernetes

   OpenShift

   ```
   kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   ```
   oc config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   Если вы установили `enableIstio` в `true` в [пользовательском ресурсе DynaKube](https://dt-url.net/dynakube-samples), используйте приведённую ниже команду для получения URL Kubernetes API:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Создайте файл с именем `token-secret.yaml` со следующим содержимым:

   ```
   apiVersion: v1


   kind: Secret


   metadata:


   name: dynatrace-activegate


   annotations:


   kubernetes.io/service-account.name: "dynatrace-activegate"


   type: kubernetes.io/service-account-token
   ```
3. Примените файл для создания секрета `dynatrace-activegate`.

   Kubernetes

   OpenShift

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```

   ```
   oc apply -n dynatrace -f token-secret.yaml
   ```
4. Получите bearer-токен.

   Kubernetes

   OpenShift

   ```
   kubectl get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```
5. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** и выберите **Connect manually**.
6. На странице настроек подключения кластера Kubernetes укажите **Name**, **Kubernetes API URL** и **Bearer token** для кластера Kubernetes.
7. Нажмите **Save changes**.

#### Kubernetes версии ранее 1.24

1. Получите URL Kubernetes API.

   Kubernetes

   OpenShift

   ```
   kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   ```
   oc config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   Если вы установили `enableIstio` в `true` в [пользовательском ресурсе DynaKube](https://dt-url.net/dynakube-samples), используйте приведённую ниже команду для получения URL Kubernetes API:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Получите bearer-токен.

   Kubernetes

   OpenShift v3.x

   OpenShift v4.x

   ```
   kubectl get secret $(kubectl get sa dynatrace-activegate -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret $(oc get sa dynatrace-activegate -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret $(oc get sa dynatrace-activegate -o jsonpath='{.secrets[1].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Специальные инструкции для дистрибутивов Rancher для получения URL API и bearer-токена

   Для **дистрибутивов Rancher** Kubernetes необходимо использовать bearer-токен и URL API **сервера Rancher**, поскольку этот сервер управляет трафиком к серверу Kubernetes API и обеспечивает его безопасность. Выполните следующие шаги.

   1. Получите **URL Kubernetes API**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Настройте пользователя.

      В веб-интерфейсе Rancher создайте нового пользователя или используйте существующего для связи с токеном. Рекомендуется создать нового пользователя.
   3. Установите разрешения.

      Убедитесь, что пользователь имеет разрешения **Owner** или **Custom** для кластера, который вы хотите мониторить.

      **Рекомендуется:** выберите разрешения **Custom** и обязательно выберите следующие две роли: **View all Projects** и **View Nodes**.
   4. Создайте API-ключ.

      Перейдите в **API & Keys** и создайте ключ для вашей конкретной учётной записи (введите имя кластера) или для всех кластеров (введите **No scope**). По соображениям безопасности рекомендуется первый вариант.

      Для вновь созданных ключей отображаются четыре поля. Убедитесь, что вы используете содержимое поля **Bearer token** для настройки подключения к Kubernetes API, описанного в следующем разделе.
3. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** и выберите **Connect manually**.
4. На странице настроек подключения кластера Kubernetes укажите **Name**, **Kubernetes API URL** и **Bearer token** для кластера Kubernetes.

   Для дистрибутивов Rancher вам нужен bearer-токен, созданный в веб-интерфейсе Rancher, как описано в разделе **Специальные инструкции для дистрибутивов Rancher для получения URL API и bearer-токена** выше.
5. Нажмите **Save changes**.

## Другие варианты

* Если вы не можете использовать Dynatrace Operator, вы можете развернуть ActiveGate напрямую как StatefulSet (не рекомендуется).
* Если вы хотите мониторить несколько кластеров Kubernetes с одним ActiveGate и вам не нужно разделять сети для административного или операционного трафика, вы можете установить ActiveGate на виртуальной машине с помощью обычного установщика.

Dynatrace рекомендует использовать контейнеризованный ActiveGate для мониторинга Kubernetes API

## Часто задаваемые вопросы

Можно ли изменить настройки мониторинга Kubernetes API?

Вы можете изменить настройки подключения и мониторинга кластера Kubernetes в любое время на странице сведений о кластере Kubernetes.

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Найдите свой кластер Kubernetes, затем выберите **Actions** > **Settings**.
3. Измените настройки, затем нажмите **Save changes**.

Как удалить конфигурацию мониторинга платформы Kubernetes для кластера?

Для удаления подключения к локальной конечной точке Kubernetes API

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Найдите свой кластер Kubernetes, затем выберите **Actions** > **Settings**.
3. Нажмите **Use defaults**, затем нажмите **Save changes**.

Когда обновляется ActiveGate?

ActiveGate обновляется автоматически при перезапуске пода, если доступна новая версия, если только версия образа не указана в `cr.yaml`.
