---
title: Мониторинг Kubernetes API
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring
scraped: 2026-05-12T12:06:19.162713
---

# Мониторинг Kubernetes API

# Мониторинг Kubernetes API

* Чтение: 8 мин
* Обновлено 9 декабря 2025 г.

Dynatrace получает информацию о сущностях и метаданных Kubernetes, запрашивая Kubernetes API. Эта информация используется для [готового оповещения для Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Настройка оповещений на уровне кластера, узла, пространства имён или рабочей нагрузки Kubernetes/OpenShift.") и для предоставления всех сигналов наблюдаемости в правильном контексте Kubernetes на платформе Dynatrace, например, путём создания связей между приложениями, (микро)сервисами, базами данных и сущностями Kubernetes, такими как поды, пространства имён и узлы.

Dynatrace Operator управляет жизненным циклом всех компонентов Dynatrace в кластере Kubernetes и может быть настроен путём развёртывания пользовательского ресурса DynaKube. Dynatrace ActiveGate, компонент Dynatrace, необходимый для мониторинга Kubernetes API, предоставляет возможность мониторинга Kubernetes API.

Чтобы включить мониторинг Kubernetes API, выполните приведённые ниже шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установка Dynatrace Operator**](#install-dto)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка DynaKube**](#configure-dynakube)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Подключение ActiveGate к Kubernetes API**](#connect-ag)

## Шаг 1. Установка Dynatrace Operator

[Установите Dynatrace Operator в любом режиме развёртывания](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes")

## Шаг 2. Настройка DynaKube

Настройте значения **ActiveGate** для DynaKube в соответствии со [списком параметров](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#ag "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") и добавьте `kubernetes-monitoring` в возможности ActiveGate.

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

Инструкции для обоих вариантов приведены ниже.

### Подключение к локальной конечной точке Kubernetes API

Включить мониторинг можно, подключив контейнеризованный ActiveGate к локальной конечной точке Kubernetes API.

Существует два способа подключения к локальной конечной точке Kubernetes API:

* Рекомендуется [позволить Dynatrace Operator автоматически управлять подключением](#auto)
* [Настроить подключение вручную](#manual)

Подробности об обоих методах приведены ниже.

Connect automatically

Connect manually

Этот флаг функции устарел и включён по умолчанию начиная с версии Dynatrace Operator 0.13.0.

Чтобы подключиться автоматически к локальной конечной точке Kubernetes API

1. Обязательно включите разрешения **Read entities**, **Read settings** и **Write settings** (API v2) для своего токена доступа (см. [Токены доступа и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes")).
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

   После добавления этой аннотации имя кластера, отображаемое в Dynatrace, будет совпадать с пользовательским ресурсом DynaKube, в котором настроена аннотация. Имя кластера, отображаемое в Dynatrace, можно изменить, также добавив аннотацию `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"`.

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

Чтобы подключиться к локальной конечной точке Kubernetes API вручную, вам нужно только указать уникальный идентификатор кластера Kubernetes (uuid пространства имён kube-system). Контейнеризованный ActiveGate затем определяет уникальный идентификатор кластера и отправляет его в Dynatrace.

#### Шаг 1. Получение идентификатора кластера Kubernetes

Выполните приведённую ниже команду и возьмите UID из вывода.

Kubernetes

OpenShift

```
kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
```

```
oc get namespace kube-system -o jsonpath='{.metadata.uid}'
```

#### Шаг 2. Указание идентификатора кластера Kubernetes в Dynatrace

1. Перейдите в **Kubernetes**.
2. Выберите **Connect manually**.
3. На странице настроек подключения кластера Kubernetes укажите **Name**, а затем включите **Connect containerized ActiveGate to local Kubernetes API endpoint**.
4. В поле **Kubernetes cluster ID** введите UID, полученный ранее.
5. Выберите **Save changes**, чтобы сохранить вашу конфигурацию.

   Конфигурацию можно сохранить, даже если ActiveGate не готов к подключению, и завершить настройку позже. Чтобы проверить готовность, выберите **Test configuration**.

### Подключение к публичному Kubernetes API

Чтобы подключиться к публичному Kubernetes API, следуйте инструкциям, которые применимы к вашей версии Kubernetes:

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

   Если вы задали для `enableIstio` значение `true` в [пользовательском ресурсе DynaKube](https://dt-url.net/dynakube-samples), используйте приведённую ниже команду, чтобы получить URL Kubernetes API:

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
3. Примените файл, чтобы создать секрет `dynatrace-activegate`.

   Kubernetes

   OpenShift

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```

   ```
   oc apply -n dynatrace -f token-secret.yaml
   ```
4. Получите токен bearer.

   Kubernetes

   OpenShift

   ```
   kubectl get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```
5. Перейдите в **Kubernetes** и выберите **Connect manually**.
6. На странице настроек подключения кластера Kubernetes укажите **Name**, **Kubernetes API URL** и **Bearer token** для кластера Kubernetes.
7. Выберите **Save changes**.

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

   Если вы задали для `enableIstio` значение `true` в [пользовательском ресурсе DynaKube](https://dt-url.net/dynakube-samples), используйте приведённую ниже команду, чтобы получить URL Kubernetes API:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Получите токен bearer.

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

   Особые инструкции для дистрибутивов Rancher по получению URL API и токена bearer

   Для **дистрибутивов Rancher** Kubernetes необходимо использовать токен bearer и URL API **сервера Rancher**, поскольку этот сервер управляет трафиком к серверу Kubernetes API и защищает его. Выполните приведённые ниже шаги.

   1. Получите **Kubernetes API URL**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Настройте пользователя.

      В веб-интерфейсе Rancher создайте нового пользователя или используйте существующего, чтобы связать его с токеном. Рекомендуем создать нового пользователя.
   3. Задайте разрешения.

      Убедитесь, что у пользователя есть разрешения **Owner** или **Custom** для кластера, который нужно отслеживать.

      **Рекомендуется:** выберите разрешения **Custom** и обязательно выберите эти две роли: **View all Projects** и **View Nodes**.
   4. Создайте ключ API.

      Перейдите в **API & Keys** и создайте ключ либо для вашей конкретной учётной записи (введите имя вашего кластера), либо для всех кластеров (введите **No scope**). По соображениям безопасности рекомендуем выбрать первый вариант.

      Вновь созданные ключи отображают четыре поля. Обязательно используйте содержимое поля под названием **Bearer token** для настройки подключения к Kubernetes API, описанной в следующем разделе.
3. Перейдите в **Kubernetes** и выберите **Connect manually**.
4. На странице настроек подключения кластера Kubernetes укажите **Name**, **Kubernetes API URL** и **Bearer token** для кластера Kubernetes.

   Для дистрибутивов Rancher необходим токен bearer, созданный в веб-интерфейсе Rancher, как описано в разделе **Особые инструкции для дистрибутивов Rancher по получению URL API и токена bearer** выше.
5. Выберите **Save changes**.

## Другие варианты

* Если использовать Dynatrace Operator невозможно, можно [развернуть ActiveGate напрямую как StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet.") (не рекомендуется).
* Если требуется отслеживать несколько кластеров Kubernetes с помощью одного ActiveGate и при этом не нужно разделять сети для административного или операционного трафика, можно [установить ActiveGate на виртуальной машине с помощью обычного установщика](/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm "Настройка и конфигурирование ActiveGate для мониторинга платформы Kubernetes на виртуальной машине.").

Dynatrace рекомендует использовать контейнеризованный ActiveGate для мониторинга Kubernetes API

## Часто задаваемые вопросы

Можно ли изменить настройки мониторинга Kubernetes API?

Настройки подключения и мониторинга кластера Kubernetes можно изменить в любое время на странице сведений о кластере Kubernetes.

1. Перейдите в **Kubernetes**.
2. Найдите ваш кластер Kubernetes, а затем выберите **Actions** > **Settings**.
3. Скорректируйте свои настройки, а затем выберите **Save changes**.

Как удалить конфигурацию Kubernetes Platform Monitoring для кластера Kubernetes?

Чтобы удалить подключение к локальной конечной точке Kubernetes API

1. Перейдите в **Kubernetes**.
2. Найдите ваш кластер Kubernetes, а затем выберите **Actions** > **Settings**.
3. Выберите **Use defaults**, а затем выберите **Save changes**.

Когда обновляется ActiveGate?

ActiveGate обновляется автоматически при перезапуске пода всякий раз, когда доступна новая версия, если только версия образа не указана в `cr.yaml`.