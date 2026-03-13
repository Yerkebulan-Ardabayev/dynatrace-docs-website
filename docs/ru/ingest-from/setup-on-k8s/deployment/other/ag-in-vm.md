---
title: Deploy ActiveGate in a VM
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm
scraped: 2026-03-05T21:33:23.286611
---

# Развёртывание ActiveGate в виртуальной машине

# Развёртывание ActiveGate в виртуальной машине

* Последняя версия Dynatrace
* Чтение: 5 мин
* Обновлено 22 января 2026 г.

Если вы хотите мониторить несколько кластеров Kubernetes с помощью одного ActiveGate и вам не нужно разделять сети для административного или операционного трафика, вы можете установить ActiveGate на виртуальную машину с помощью стандартного установщика для подключения ваших кластеров к Dynatrace, как описано ниже.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Начало установки**](ag-in-vm.md#start-installation "Настройка и конфигурация ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Загрузка установщика**](ag-in-vm.md#download-installer "Настройка и конфигурация ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запуск установщика**](ag-in-vm.md#run-installer "Настройка и конфигурация ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Подключение кластеров Kubernetes к Dynatrace**](ag-in-vm.md#connect-clusters-to-dynatrace "Настройка и конфигурация ActiveGate для мониторинга платформы Kubernetes в виртуальной машине.")

## Шаг 1 Начало установки

1. В Dynatrace Hub выберите **ActiveGate**.
2. Выберите **Set up**.

3. На странице **Install Environment ActiveGate** выберите **Linux**.

## Шаг 2 Загрузка установщика

Способ загрузки установщика зависит от вашей конфигурации и потребностей. Вы можете загрузить установщик непосредственно на сервер, на котором планируете установить Environment ActiveGate, или загрузить его на другую машину и затем перенести на сервер.

1. Выберите [Маршрутизация трафика OneAgent](../../../dynatrace-activegate/capabilities/routing-monitoring-purpose.md "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.") в качестве [назначения ActiveGate](../../../dynatrace-activegate.md#purposes "Основные концепции, связанные с ActiveGate.").
2. Укажите токен доступа с областью действия [`PaaS Integration - InstallerDownload`](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия."). Этот токен необходим для загрузки установщика ActiveGate из вашей среды. Если у вас нет токена доступа, вы можете создать его прямо в интерфейсе. Токен автоматически добавляется к командам загрузки и установки, которые вы будете использовать позже.
3. Выберите **Download installer**. Доступны два варианта:

   * Загрузка через команду оболочки. Скопируйте и выполните команду `wget`.
   * Нажмите на ссылку для загрузки установщика ActiveGate.
4. Проверьте подпись.
   Дождитесь завершения загрузки, а затем проверьте подпись, скопировав команду из второго текстового поля **Verify signature** и вставив её в окно терминала.

## Шаг 3 Запуск установщика

Параметр установки (определяемый выбранным вами назначением ActiveGate) автоматически устанавливается для команды запуска установщика. Убедитесь, что вы используете команду, отображаемую в Dynatrace, которая отражает назначение ActiveGate.
Скопируйте команду установочного скрипта из шага **Run the installer with root rights** и вставьте её в терминал.

### Добавление сертификата ЦС Kubernetes в хранилище доверенных сертификатов Рекомендуется

Инструкции по добавлению сертификата в файл хранилища доверенных сертификатов см. в разделе [Доверенные корневые сертификаты для ActiveGate](../../../dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate.md "Узнайте, как указать пользовательский файл хранилища доверенных сертификатов.").

### Настройка установки

Вы можете добавить дополнительные [параметры](../../../dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate.md "Узнайте о параметрах командной строки для ActiveGate на Linux.") к команде установки для настройки. Например, чтобы установить ActiveGate в другой каталог, используйте параметр `INSTALL=<path>`:

```
[root@host]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh INSTALL=/hosted_app/dynatrace
```

### Параметры установки по умолчанию

Информацию о параметрах по умолчанию, включая каталоги по умолчанию, см. в разделе [Параметры по умолчанию ActiveGate для Linux](../../../dynatrace-activegate/installation/linux/linux-default-settings.md "Узнайте о параметрах по умолчанию, с которыми ActiveGate устанавливается на Linux").

## Шаг 4 Подключение кластеров Kubernetes к Dynatrace

Для подключения API Kubernetes к Dynatrace следуйте инструкциям, соответствующим вашей версии Kubernetes.

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
3. Получите URL-адрес API Kubernetes.

   ```
   $ kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```
4. Kubernetes версии 1.24+ Создайте файл с именем `token-secret.yaml` со следующим содержимым.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: dynatrace-monitoring



   annotations:



   kubernetes.io/service-account.name: "dynatrace-monitoring"



   type: kubernetes.io/service-account-token
   ```
5. Kubernetes версии 1.24+ Примените файл для создания секрета `dynatrace-monitoring`.

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```
6. Получите bearer-токен.

   Kubernetes версии 1.24+

   ```
   kubectl get secret dynatrace-monitoring -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Kubernetes версии 1.23 и ниже

   ```
   kubectl get secret $(kubectl get sa dynatrace-monitoring -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Специальные инструкции для дистрибутивов Rancher для получения URL-адреса API и bearer-токена

   Для **дистрибутивов Rancher** Kubernetes необходимо использовать bearer-токен и URL-адрес API **сервера Rancher**, поскольку этот сервер управляет трафиком к серверу API Kubernetes и обеспечивает его безопасность. Выполните следующие шаги.

   1. Получите **URL-адрес API Kubernetes**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Настройте пользователя.

      В веб-интерфейсе Rancher создайте нового пользователя или используйте существующего для привязки к токену. Рекомендуется создать нового пользователя.
   3. Установите разрешения.

      Убедитесь, что у пользователя есть разрешения **Owner** или **Custom** для кластера, который вы хотите мониторить.

      **Рекомендуется**: выберите разрешения **Custom** и обязательно выберите эти две роли: **View all Projects** и **View Nodes**.
   4. Создайте API-ключ.

      Перейдите в **API & Keys** и создайте ключ для вашей конкретной учётной записи (введите имя кластера) или для всех кластеров (введите **No scope**). По соображениям безопасности рекомендуется первый вариант.

      Для вновь созданных ключей отображаются четыре поля. Обязательно используйте содержимое поля **Bearer token** для настройки подключения к API Kubernetes, описанного в следующем разделе.
7. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
8. Выберите **Connect manually**.
9. Укажите **Name**, **Kubernetes API URL target** и **Kubernetes bearer token** для кластера Kubernetes.
10. Убедитесь, что **Monitor events** и **Monitor Kubernetes namespaces, services, workloads, and pods** включены.

Отключение проверки сертификатов не рекомендуется, так как это создаёт угрозу безопасности. Однако, если вы всё же хотите отключить проверку сертификатов для тестовых сред, убедитесь, что вы отключили **Require valid certificates for communication with the API server (recommended)** и **Verify hostname in certificate against Kubernetes API URL**.

11. Выберите **Save changes** для сохранения конфигурации.

Для обновления ActiveGate см. [Обновление ActiveGate](../../../dynatrace-activegate/operation/update-activegate.md "Узнайте, как определить установленную версию ActiveGate и загрузить и установить последнюю версию.").
