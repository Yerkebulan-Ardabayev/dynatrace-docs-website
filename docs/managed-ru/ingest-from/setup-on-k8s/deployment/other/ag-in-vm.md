---
title: Развёртывание ActiveGate в виртуальной машине
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm
scraped: 2026-05-12T12:13:44.494502
---

# Развёртывание ActiveGate в виртуальной машине

# Развёртывание ActiveGate в виртуальной машине

* Чтение: 5 мин
* Обновлено 22 января 2026 г.

Если необходимо отслеживать несколько кластеров Kubernetes с помощью одного ActiveGate и нет необходимости разделять сети для административного или эксплуатационного трафика, можно установить ActiveGate на виртуальной машине с помощью обычного установщика, чтобы подключить ваши кластеры к Dynatrace, как описано ниже.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Начало установки**](/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#start-installation "Установка и настройка ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Загрузка установщика**](/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#download-installer "Установка и настройка ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Запуск установщика**](/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#run-installer "Установка и настройка ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Подключение ваших кластеров Kubernetes к Dynatrace**](/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#connect-clusters-to-dynatrace "Установка и настройка ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")

## Шаг 1 Начало установки

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Install ActiveGate**.

3. На странице **Install Environment ActiveGate** выберите **Linux**.

## Шаг 2 Загрузка установщика

Способ загрузки установщика зависит от вашей конфигурации и потребностей. Можно загрузить установщик непосредственно на сервер, где планируется установить Environment ActiveGate, либо загрузить установщик на другую машину, а затем перенести его на сервер.

1. Выберите [Route OneAgent traffic](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга и применении ActiveGate.") в качестве [назначения ActiveGate](/managed/ingest-from/dynatrace-activegate#purposes "Изучите основные концепции, связанные с ActiveGate.").
2. Предоставьте токен доступа с областью [`PaaS Integration - InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей."). Этот токен требуется для загрузки установщика ActiveGate из вашего окружения. Если у вас нет токена доступа, можно создать его прямо в интерфейсе. Токен автоматически добавляется к командам загрузки и установки, которые вы будете использовать далее.
3. Выберите **Download installer**. Доступны два варианта:

   * Загрузка через команду оболочки. Скопируйте и выполните команду `wget`.
   * Выберите ссылку для загрузки установщика ActiveGate.
4. Проверьте подпись.
   Дождитесь завершения загрузки, а затем проверьте подпись, скопировав команду из второго текстового поля **Verify signature** и вставив её в окно терминала.

## Шаг 3 Запуск установщика

Параметр установки (определяемый выбранным вами назначением ActiveGate) автоматически задаётся для команды запуска установщика. Убедитесь, что вы используете отображаемую в Dynatrace команду, которая отражает назначение ActiveGate.
Скопируйте команду скрипта установки из шага **Run the installer with root rights** и вставьте её в терминал.

### Добавьте сертификат CA Kubernetes в хранилище доверенных сертификатов Рекомендуется

Инструкции по добавлению сертификата в файл хранилища доверенных сертификатов см. в разделе [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate для установления защищённых соединений SSL/TLS.").

### Настройка установки

В команду установки можно добавить дополнительные [параметры](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate в Linux.") для настройки установки. Например, чтобы установить ActiveGate в другой каталог, используйте параметр `INSTALL=<path>`:

```
[root@host]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh INSTALL=/hosted_app/dynatrace
```

### Настройки установки по умолчанию

Сведения о значениях установки по умолчанию, включая каталоги по умолчанию, см. в разделе [Настройки ActiveGate по умолчанию для Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Узнайте о настройках по умолчанию, с которыми ActiveGate устанавливается в Linux").

## Шаг 4 Подключение ваших кластеров Kubernetes к Dynatrace

Чтобы подключить Kubernetes API к Dynatrace, следуйте инструкциям, применимым к вашей версии Kubernetes.

1. Создайте сервисную учётную запись и роль кластера.

   Создайте файл `kubernetes-monitoring-service-account.yaml` со следующим содержимым.

   kubernetes-monitoring-service-account.yaml

   ```
   apiVersion: v1



   kind: ServiceAccount



   metadata:



   name: dynatrace-monitoring



   namespace: dynatrace



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   name: dynatrace-monitoring-cluster



   rules:



   - apiGroups:



   - ""



   resources:



   - nodes



   - pods



   - namespaces



   - replicationcontrollers



   - events



   - resourcequotas



   - pods/proxy



   - nodes/proxy



   - nodes/metrics



   - services



   - persistentvolumeclaims



   - persistentvolumes



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - batch



   resources:



   - jobs



   - cronjobs



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apps



   resources:



   - deployments



   - replicasets



   - statefulsets



   - daemonsets



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apps.openshift.io



   resources:



   - deploymentconfigs



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - config.openshift.io



   resources:



   - clusterversions



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - dynatrace.com



   resources:



   - dynakubes



   - edgeconnects



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apiextensions.k8s.io



   resources:



   - customresourcedefinitions



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - networking.k8s.io



   resources:



   - ingresses



   - networkpolicies



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - discovery.k8s.io



   resources:



   - endpointslices



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - autoscaling



   resources:



   - horizontalpodautoscalers



   verbs:



   - list



   - watch



   - get



   - nonResourceURLs:



   - /metrics



   - /version



   - /readyz



   - /livez



   verbs:



   - get



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRoleBinding



   metadata:



   name: dynatrace-monitoring-cluster



   roleRef:



   apiGroup: rbac.authorization.k8s.io



   kind: ClusterRole



   name: dynatrace-monitoring-cluster



   subjects:



   - kind: ServiceAccount



   name: dynatrace-monitoring



   namespace: dynatrace
   ```
2. Примените файл.

   ```
   kubectl apply -f kubernetes-monitoring-service-account.yaml
   ```
3. Получите URL Kubernetes API.

   ```
   $ kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```
4. Версия Kubernetes 1.24+ Создайте файл с именем `token-secret.yaml` со следующим содержимым.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: dynatrace-monitoring



   annotations:



   kubernetes.io/service-account.name: "dynatrace-monitoring"



   type: kubernetes.io/service-account-token
   ```
5. Версия Kubernetes 1.24+ Примените файл, чтобы создать секрет `dynatrace-monitoring`.

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```
6. Получите токен носителя.

   Версия Kubernetes 1.24+

   ```
   kubectl get secret dynatrace-monitoring -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Версии Kubernetes 1.23 и ниже

   ```
   kubectl get secret $(kubectl get sa dynatrace-monitoring -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Специальные инструкции для дистрибутивов Rancher по получению URL API и токена носителя

   Для **дистрибутивов Rancher** Kubernetes необходимо использовать токен носителя и URL API **сервера Rancher**, поскольку этот сервер управляет трафиком к серверу Kubernetes API и обеспечивает его безопасность. Выполните приведённые ниже шаги.

   1. Получите **URL Kubernetes API**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Настройте пользователя.

      В веб-интерфейсе Rancher создайте нового пользователя или используйте существующего пользователя для связывания с токеном. Рекомендуется создать нового пользователя.
   3. Задайте разрешения.

      Убедитесь, что у пользователя есть разрешения **Owner** или **Custom** для кластера, который необходимо отслеживать.

      **Рекомендуется**: выберите разрешения **Custom** и обязательно выберите эти две роли: **View all Projects** и **View Nodes**.
   4. Создайте ключ API.

      Перейдите в **API & Keys** и создайте ключ либо для вашей конкретной учётной записи (введите имя вашего кластера), либо для всех кластеров (введите **No scope**). Из соображений безопасности рекомендуется выбрать первый вариант.

      Вновь созданные ключи отображают четыре поля. Обязательно используйте содержимое поля с именем **Bearer token** для настройки подключения к Kubernetes API, описанного в следующем разделе.
7. Перейдите в **Kubernetes**.
8. Выберите **Connect manually**.
9. Укажите **Name**, **Kubernetes API URL target** и **Kubernetes bearer token** для кластера Kubernetes.
10. Убедитесь, что **Monitor events** и **Monitor Kubernetes namespaces, services, workloads, and pods** включены.

Отключать проверку сертификатов не рекомендуется, поскольку это создаёт риски безопасности. Тем не менее, если вы всё же хотите отключить проверку сертификатов для тестовых окружений, обязательно отключите **Require valid certificates for communication with the API server (recommended)** и **Verify hostname in certificate against Kubernetes API URL**.

11. Выберите **Save changes**, чтобы сохранить вашу конфигурацию.

Сведения об обновлении ActiveGate см. в разделе [Обновление ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Узнайте, как определить, какая версия ActiveGate у вас установлена, и как загрузить и установить последнюю версию.").