---
title: Подключение Cloud Foundry к Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace
scraped: 2026-05-12T11:09:19.517209
---

# Подключение Cloud Foundry к Dynatrace

# Подключение Cloud Foundry к Dynatrace

* 4-min read
* Updated on Apr 07, 2026

Подключение Cloud Foundry foundations к Dynatrace открывает следующие возможности:

* полный доступ к [странице обзора Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics "Доступные метрики для мониторинга кластеров Cloud Foundry с Dynatrace");
* автоматическое обнаружение организаций Cloud Foundry;
* доступ к другим свойствам процессов Cloud Foundry, таким как **space**, **space ID**, **application**, **application ID** и **instance index**.

Следуйте приведённым ниже инструкциям для подключения foundation к Dynatrace.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Начало установки**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#start-installation "Включение мониторинга в Cloud Foundry foundations.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Загрузка установщика**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#download-installer "Включение мониторинга в Cloud Foundry foundations.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запуск установщика**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#run-installer "Включение мониторинга в Cloud Foundry foundations.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Управление сертификатами**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#certificate "Включение мониторинга в Cloud Foundry foundations.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Подключение foundation к Dynatrace**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace#connect-foundation "Включение мониторинга в Cloud Foundry foundations.")

## Предварительные условия

* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Техническая информация о поддержке платформ и фреймворков в Dynatrace.").
* Diego cells включают [BOSH add-on OneAgent](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с помощью BOSH.").

## Шаг 1. Начало установки

1. Войдите в Dynatrace.
2. Перейдите в **Deploy Dynatrace**.
3. Выберите **Install ActiveGate**.

Подробнее см. в разделе [Установка](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").

## Шаг 2. Загрузка установщика

Способ загрузки установщика зависит от ваших настроек. Можно загрузить установщик непосредственно на сервер, где планируется установка ActiveGate, или загрузить на другую машину и затем перенести на сервер.

1. Выберите [Route OneAgent traffic](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации ActiveGate.") в качестве [назначения ActiveGate](/managed/ingest-from/dynatrace-activegate#purposes "Основные концепции ActiveGate.").
2. Выберите **Download installer**. Доступны два варианта:

   * Загрузка через команду оболочки. Скопируйте и выполните команду `wget`.
   * Перейдите по ссылке для загрузки установщика ActiveGate.

## Шаг 3. Запуск установщика

Параметр установки (определяемый выбранным назначением ActiveGate) автоматически задаётся в команде запуска установщика. Убедитесь, что используете команду, отображённую в веб-интерфейсе Dynatrace.

Скопируйте команду скрипта установки из шага **Run the installer with root rights** и вставьте её в терминал.

### Настройка установки

К команде установки можно добавить дополнительные [параметры](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Параметры командной строки для ActiveGate на Linux."). Например, для установки ActiveGate в другую директорию используйте параметр `INSTALL=<path>`:

```
[root@host]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh INSTALL=/hosted_app/dynatrace
```

### Параметры установки по умолчанию

Параметры по умолчанию, включая директории по умолчанию, см. в разделе [Параметры установки ActiveGate по умолчанию для Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Параметры по умолчанию при установке ActiveGate на Linux").

## Шаг 4. Управление сертификатами

Если для связи с внешними API используются самоподписанные сертификаты, можно добавить сертификат в truststore или отключить проверку сертификатов.

### Добавление сертификата в truststore

1. Получите сертификат от облачного провайдера.
   В следующем примере сертификат извлекается с `google.com` и сохраняется локально как `dt_k8s_api.pem`. Команда одинакова для Windows и Linux при наличии установленного `openssl`.

   ```
   echo Q | openssl s_client -connect google.com:443 | openssl x509 -outform PEM > dt_k8s_api.pem
   ```

   Для Kubernetes используйте следующую последовательность команд:

   ```
   [root@host]# API_ENDPOINT_URL=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')



   [root@host]# if [[ $API_ENDPOINT_URL =~ (https?://.*):(\d*) ]]; then API_SERVER_PORT=$API_ENDPOINT_URL; else API_SERVER_PORT="$(echo $API_ENDPOINT_URL | sed -e "s/https:\/\///"):443"; fi



   [root@host]# echo -e "${YLW} API server:${NC} ${API_SERVER_PORT}"



   [root@host]# echo Q | openssl s_client -connect $API_SERVER_PORT 2>/dev/null | openssl x509 -outform PEM > dt_k8s_api.pem
   ```

2. Добавьте сертификат в keystore.
   Можно указать полный путь к файлу `pem` с помощью параметра `-file` или скопировать файл `pem` в директорию ActiveGate и указать только имя файла.

   ```
   [root@host]# sudo /opt/dynatrace/gateway/jre/bin/keytool -import -file dt_k8s_api.pem -alias dt_k8s_api -keystore /var/lib/dynatrace/gateway/ssl/mytrusted.jks
   ```

   При импорте нескольких сертификатов убедитесь, что для каждого указан уникальный alias. Использование одного alias перезапишет предыдущие сертификаты.

   Для отображения списка alias и описания сертификатов используйте команду `keytool -list`.

3. Добавьте следующие записи в файл `/var/lib/dynatrace/gateway/config/custom.properties`:

   ```
   [collector]



   trustedstore = mytrusted.jks



   # следующие записи необязательны



   trustedstore-password = changeit



   trustedstore-type = JKS
   ```

   Зашифрованный пароль

   Пароль будет удалён и зашифрован при перезапуске службы ActiveGate.

4. [Перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Запуск, остановка и перезапуск ActiveGate на Windows или Linux.").

В качестве альтернативы можно добавить файл truststore с сертификатом Kubernetes CA как параметр установки. Подробнее см. в разделе [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Настройка доверенных корневых сертификатов на ActiveGate.").

### Отключение проверки сертификатов

Отключение проверки сертификатов не рекомендуется, так как создаёт угрозу безопасности. Однако если это необходимо для тестовых окружений, выполните следующее:

1. Перейдите на [страницу обзора Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes#kubernetes-page "Мониторинг ресурсов кластера Kubernetes/OpenShift."), найдите свой кластер и выберите **...** > **Settings** в строке кластера для редактирования настроек.
2. Отключите **Require valid certificates for communication with API server**.
3. Отключите **Verify hostname in certificate against Kubernetes API URL**.
4. Нажмите **Save** для сохранения изменений.
   Эти настройки переопределяют настройки в файле `custom.properties` ActiveGate.

## Шаг 5. Подключение foundation к Dynatrace

Рекомендуется использовать [учётную запись Cloud Foundry admin read-only](https://docs.cloudfoundry.org/uaa/uaa-user-management.html#admin-read-only), которая позволяет просматривать почти все ресурсы Cloud Controller API без возможности их изменения.

```
uaac user add ReadOnlyUser -p SecretPassword --emails something@example.com



uaac member add cloud_controller.admin_read_only ReadOnlyUser



uaac member add scim.read ReadOnlyUser
```

Для подключения Cloud Foundry foundation к Dynatrace:

1. Перейдите в ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") **Hub**, найдите **Cloud Foundry** и выберите **Set up**, чтобы добавить расширение в своё окружение.
2. Добавьте новый эндпоинт мониторинга.

   Введите **API target URL**, **Authentication endpoint**, **Cloud Foundry Username** и **Password**.
3. Необязательно: выберите группу ActiveGate.

   Подробнее о группах ActiveGate см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Основные концепции групп ActiveGate.").
4. Необязательно: протестируйте соединение.
5. Нажмите **Save changes**.

## Управление разрешениями и конфигурацией

* Для тонкой настройки разрешений пользователей см. [Политики IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Работа с политиками").
* Для удобной настройки используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте о Dynatrace Settings API.").

SchemaID для Cloud Foundry: `builtin:cloud.cloudfoundry`.

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")
* [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка Dynatrace на Cloud Foundry.")