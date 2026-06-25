---
title: Интеграция OneAgent в Azure App Service для Linux и контейнеров
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers
scraped: 2026-05-12T12:03:55.451751
---

# Интеграция OneAgent в Azure App Service для Linux и контейнеров

# Интеграция OneAgent в Azure App Service для Linux и контейнеров

* Практическое руководство
* Чтение: 11 мин
* Обновлено 22 апреля 2026 г.

Только Linux

App Service на Linux поддерживает два сценария.

* **Принесите собственный код**

  В сценарии с кодом App Service предоставляет базовый контейнер, обслуживаемый платформой.

  Этот контейнер ориентирован на:

  + фреймворк разработки, например .NET Core, PHP или Node.js;
  + версию этого фреймворка, например .NET Core 3.0 или .NET Core 3.1.

  Следуйте инструкциям на вкладке **Built-in image**.
* **Принесите собственный контейнер**

  В сценарии с контейнером App Service предоставляет хост, на котором может выполняться пользовательский контейнер клиента.

  Подробности о различиях между двумя сценариями см. в разделе [Что нужно знать: Web Apps на Linux](https://dt-url.net/jm039gu).

  Для мониторинга App Services на Linux необходимо интегрировать OneAgent в контейнеризированное приложение.

  Следуйте инструкциям на вкладке **Custom image**.

Встроенный образ

Пользовательский образ

## Интеграция Dynatrace в встроенный образ

Azure App Service для Linux позволяет настраивать базовый контейнер во время выполнения с помощью [скрипта запуска или команды](https://dt-url.net/z2234qa), которые должны выполняться в bash-оболочке или [Azure Cloud Shell](https://dt-url.net/at034yy). Скрипт можно настроить несколькими способами.

### Настройка команды/файла скрипта запуска при создании с помощью Azure CLI

```
az webapp create -n <my-app> -g <my-resourcegroup> -p <my-appservice-plan> --runtime <runtime-tag> --startup-file <startup-script/command>
```

### Настройка команды/файла скрипта для существующего App Service

```
az webapp config set -n <my-app> -g <my-resourcegroup> --startup-file <startup-script/command>
```

### Настройка команды/файла скрипта с помощью ARM-шаблона

Используйте свойство [appCommandLine](https://docs.microsoft.com/en-us/azure/templates/microsoft.web/sites/config-web?pivots=deployment-language-arm-template#siteconfig-1) ARM-шаблона для задания скрипта/команды запуска.

```
{



"acrUseManagedIdentityCreds": false,



"acrUserManagedIdentityId": null,



"alwaysOn": false,



"apiDefinition": null,



"apiManagementConfig": null,



"appCommandLine": "<startup-script/command>",



"appSettings": null,



"autoHealEnabled": false,



"autoHealRules": null,



"autoSwapSlotName": null,



...
```

### Настройка команды/файла скрипта запуска на портале Azure

![AppService Linux Portal Startup](https://dt-cdn.net/images/screenshot-2022-12-13-at-13-42-44-1109-8955530cdd.png)

Запуск AppService Linux Portal

### Скрипт или команда?

Скрипт запуска, это то же самое, что и команда запуска, то есть команда, выполняющая скрипт (не забудьте указать путь к скрипту). Однако для этого требуется упаковать скрипт вместе с приложением. Чтобы избежать этой зависимости, используйте команды запуска.

Скрипт/команда выполняется в рамках скрипта инициализации контейнера, который реализован по-разному для каждого технологического стека.

Подробности о командах запуска см. в документации Azure App Service для Linux: [Какие значения ожидаются в разделе Startup File при настройке стека выполнения?](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

### Интеграция Dynatrace с помощью скрипта/команды запуска

Для интеграции Dynatrace скрипту/команде запуска необходим доступ к нескольким переменным.

| Параметр | Описание |
| --- | --- |
| `$DT_ENDPOINT` | Эндпоинт API-сервера Dynatrace: используйте [эндпоинт кластера](/managed/discover-dynatrace/get-started/monitoring-environment "Познакомьтесь с окружениями мониторинга и научитесь с ними работать.") окружения или [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с основными концепциями, связанными с ActiveGate."). |
| `$DT_API_TOKEN` | API-токен для доступа к Dynatrace REST API. [Создайте API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с областью видимости **InstallerDownload**. |
| `$DT_INCLUDE` | Настройте необходимые модули кода в зависимости от используемого технологического стека.  * `all` включает все доступные модули кода OneAgent (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), но увеличивает размер пакета загрузки. * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.  Подробности см. в [документации API](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузите последнюю версию установщика OneAgent через Dynatrace API."). |
| `$START_APP_CMD` | Команда для запуска приложения.  [Какие значения ожидаются в разделе Startup File при настройке стека выполнения?](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-) |

При использовании оболочки, отличной от bash, адаптируйте скрипт с учётом требований экранирования символов этой оболочки.

Это можно сделать двумя способами.

* Настройки App Service (рекомендуется)
* Установка значений непосредственно в команде

#### Мониторинг PHP на NGINX

Для мониторинга PHP-FPM и NGINX одновременно

1. Установите `DT_INCLUDE` в `all`.
2. Используйте скрипт запуска с двумя дополнительными командами в конце.

   ```
   echo '/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so' >> /etc/ld.so.preload



   /etc/init.d/nginx restart
   ```

#### Настройки App Service

Задайте значения указанных выше параметров через [App Settings](https://dt-url.net/da239ts): это эквивалентно установке переменных среды. Затем выполните следующую команду.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && sh /tmp/installer-wrapper.sh
```

Стек выполнения Java

Для приложений, работающих в стеке Java Runtime на Azure App Service, этот метод установки может работать не так, как ожидается, в некоторых случаях. Например, поступали сообщения о проблемах с образами на основе Alpine, где приведённая команда интерпретировалась как единая строка, а не выполнялась как команда оболочки. Это приводило к тому, что оператор `&&` воспринимался как часть входных данных `wget`, а не как разделитель команд.

При возникновении такого поведения рассмотрите альтернативный способ выполнения скрипта (например, пользовательский скрипт запуска или изменение [пользовательского образа](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#install--custom-image "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")).

Также можно использовать приведённый ниже скрипт-вызыватель, который работает для всех образов Linux.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



sh $installerWrapperInstallationPath
```

#### Установка значений непосредственно в команде

Нужные переменные можно задать только для команды, запускающей установщик OneAgent.

Для этого задайте значения перед командой, как показано ниже.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh
```

Также можно использовать файл запуска, как показано ниже.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh $installerWrapperInstallationPath
```

### Пример: интеграция в приложение Node.js с помощью Azure CLI в bash-оболочке

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настройте команду запуска**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-1 "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Перезапустите веб-приложение дважды**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-2 "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")

#### Шаг 1. Настройка команды запуска

```
RESOURCE_GROUP="my-appservice-test"



APPSVC="my-linux-webapp"



DT_ENDPOINT="https://XXXXXX.live.dynatrace.com"



DT_API_TOKEN="XXXXXX"



DT_INCLUDE="nodejs"



START_APP_CMD="pm2 start index.js --no-daemon"



STARTUP_CMD="wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh"



az webapp config set --resource-group $RESOURCE_GROUP --name $APPSVC --startup-file "$STARTUP_CMD"
```

#### Шаг 2. Двойной перезапуск веб-приложения

После настройки команды запуска перезапустите веб-приложение **дважды**.

* Перезапустите один раз для инициализации установки OneAgent.
* Перезапустите повторно, чтобы OneAgent начал инструментирование приложения.

## Интеграция Dynatrace в пользовательский образ

Для интеграции OneAgent с образом приложения доступны два варианта:

* [Интеграция слоя образа OneAgent, предоставляемого Dynatrace](#layer)
* [Загрузка артефактов OneAgent во время сборки образа из Dynatrace REST API](#api)

### Вариант 1: интеграция с использованием слоя образа OneAgent от Dynatrace

Для этого варианта необходимо установить Docker v17.05+ на компьютере.

1. Войдите в Docker, используя идентификатор окружения Dynatrace в качестве имени пользователя и PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Добавьте следующие строки в Dockerfile образа приложения после последней команды `FROM`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Замените следующие заполнители в шаблоне.

   | Параметр | Описание |
   | --- | --- |
   | `<ADDRESS>` | Эндпоинт реестра Dynatrace: используйте [эндпоинт кластера](/managed/discover-dynatrace/get-started/monitoring-environment "Познакомьтесь с окружениями мониторинга и научитесь с ними работать.") окружения или [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с основными концепциями, связанными с ActiveGate."). |
   | `<TECHNOLOGY>` | Настройте необходимые модули кода в зависимости от используемого технологического стека.  * `all` включает все доступные модули кода OneAgent (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), но увеличивает размер пакета загрузки. * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.  Подробности см. в [документации API](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузите последнюю версию установщика OneAgent через Dynatrace API."). |

   **Что делать, если образ Docker основан на Alpine Linux?**

   Dynatrace OneAgent поддерживает среды на основе Alpine Linux. Для использования совместимого с Alpine Linux OneAgent используйте имя образа `oneagent-codemodules-musl` (как показано в адаптированном шаблоне ниже) вместо `oneagent-codemodules`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
3. Соберите образ приложения.

   Соберите образ Docker из Dockerfile для использования в среде Kubernetes.

   ```
   docker build -t yourapp .
   ```
4. Перезапустите веб-приложение **дважды**.

   * Перезапустите один раз для инициализации скрипта установки OneAgent.
   * Перезапустите повторно для запуска OneAgent на хосте.

### Вариант 2: интеграция с использованием скрипта установщика из Dynatrace REST API

1. Добавьте следующие две строки в Dockerfile.

   ```
   RUN wget -O /tmp/installer.sh -q "<DT_ENDPOINT>/api/v1/deployment/installer/agent/unix/paas-sh/latest?Api-Token=<DT_API_TOKEN>&flavor=<DT_FLAVOR>&include=<DT_INCLUDE>" && sh /tmp/installer.sh



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Замените следующие параметры в приведённом выше шаблоне.

   | Параметр | Описание |
   | --- | --- |
   | `<DT_ENDPOINT>` | Эндпоинт Dynatrace API: используйте [эндпоинт кластера](/managed/discover-dynatrace/get-started/monitoring-environment "Познакомьтесь с окружениями мониторинга и научитесь с ними работать.") окружения или [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с основными концепциями, связанными с ActiveGate."). |
   | `<DT_API_TOKEN>` | API-токен для доступа к Dynatrace REST API. [Создайте API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с областью видимости **InstallerDownload**. |
   | `<DT_FLAVOR>` | Настройте необходимую архитектуру.  * `default` для стандартных образов Linux на основе glibc * `musl` для образов на основе Alpine Linux |
   | `<DT_INCLUDE>` | Настройте необходимые модули кода в зависимости от используемого технологического стека.  * `all` включает все доступные модули кода OneAgent (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), но увеличивает размер пакета загрузки. * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.  Подробности см. в [документации API](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузите последнюю версию установщика OneAgent через Dynatrace API."). |
2. Соберите образ приложения.

   Соберите образ Docker из Dockerfile для использования в среде Kubernetes.

   ```
   docker build -t yourapp .
   ```
3. Перезапустите веб-приложение **дважды**.

   * Перезапустите один раз для инициализации скрипта установки OneAgent.
   * Перезапустите повторно для запуска OneAgent на хосте.

## Дополнительная настройка

Используйте дополнительные переменные среды для настройки OneAgent при устранении неполадок или для расширенных сетевых конфигураций. Их можно задать через настройки приложения App Service или, при использовании пользовательского образа контейнера, в Dockerfile образа приложения.

### Сетевые переменные (необязательно)

| Параметр | Описание |
| --- | --- |
| `DT_NETWORK_ZONE` | Указывает используемую сетевую зону. Подробнее см. в разделе [Сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace."). |
| `DT_PROXY` | При использовании прокси-сервера используйте эту переменную среды для передачи учётных данных прокси. Подробнее см. в разделе [Настройка OneAgent в контейнерах для мониторинга только на уровне приложения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установите, обновите и удалите OneAgent в контейнерах для мониторинга только на уровне приложения."). |

### Дополнительные метаданные для группировки процессов и обнаружения сервисов (необязательно)

При перечислении нескольких тегов заключайте их в двойные кавычки, например: DT\_TAGS="Tag1=Value1 Tag2=Value2".

| Параметр | Описание |
| --- | --- |
| `DT_LOCALTOVIRTUALHOSTNAME` | Несколько контейнеров иногда определяются как один экземпляр (localhost), что приводит к различным проблемам, например при обнаружении сервисов или оповещениях о доступности. Используйте эту переменную среды для определения уникального имени экземпляра контейнера. Подробности см. в разделе [Обнаружение сервисов v1](/managed/observe/application-observability/services/service-detection/service-detection-v1#adjusting-service-detection "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.") |
| `DT_APPLICATIONID` | Некоторые технологии не предоставляют уникальных имён приложений. В таких случаях используйте эту переменную среды для задания уникального имени. Подробнее см. в разделе [Проблемы именования веб-сервера](/managed/observe/application-observability/services/service-detection/service-detection-v1#web-server-naming-issues "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов."). |
| `DT_TAGS` | Применяет [пользовательские теги](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Узнайте, как Dynatrace позволяет определять теги на основе переменных среды.") к группе процессов. |
| `DT_CUSTOM_PROP` | Применяет [пользовательские метаданные](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Настройте собственные метаданные, связанные с процессами, исходя из уникальных потребностей вашей организации или среды.") к группе процессов. |
| `DT_CLUSTER_ID` | Если [правила обнаружения групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения группы процессов") не подходят для вашего случая, используйте эту переменную среды, чтобы **сгруппировать все процессы с одинаковым значением**. |
| `DT_NODE_ID` | Если [правила обнаружения групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения группы процессов") не подходят для вашего случая, используйте эту переменную среды, чтобы **разделить экземпляры группы процессов**. |

### Проверочные переменные (необязательно)

| Параметр | Описание |
| --- | --- |
| `DT_LOGSTREAM` | Установите значение `stdout`, чтобы настроить OneAgent на запись ошибок в консоль. Для просмотра дополнительных журналов OneAgent задайте уровень журналирования с помощью `DT_LOGLEVELCON`, как описано ниже. |
| `DT_LOGLEVELCON` | Используйте эту переменную среды для определения уровня журналирования консоли. Допустимые значения: `NONE`, `SEVERE` и `INFO`. |

### Переменные для .NET

Этот раздел содержит переменные, относящиеся только к **средам .NET**.

| Параметр | Описание |
| --- | --- |
| `DT_AGENTACTIVE` | Переменная для .NET для настройки мониторинга приложений .NET Framework и .NET Core с помощью OneAgent. Мониторинг OneAgent для .NET активен по умолчанию (`true`). Для его отключения установите `DT_AGENTACTIVE` в `false`. Если мониторинг .NET настроен с помощью переменных среды профилировщика .NET, установите `DT_AGENTACTIVE` в `true` для его активации. |

## Обновление OneAgent

Встроенный образ

Пользовательский образ

При появлении обновления перезапустите приложение для обновления OneAgent.

Каждый раз при необходимости использовать новую версию Dynatrace OneAgent требуется пересобрать локальные модули кода OneAgent и образ приложения. Все вновь запущенные поды из этого образа приложения будут мониториться с последней версией OneAgent.

Если для новых хостов и приложений задана версия OneAgent по умолчанию с помощью [настроек обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent на Linux."), веб-приложения будут автоматически мониториться заданной версией OneAgent по умолчанию.

## Удаление OneAgent

Встроенный образ

Пользовательский образ

Порядок удаления OneAgent

1. На портале Azure откройте веб-приложение и перейдите в **Configuration** > **General settings**.
2. Удалите команду запуска (оставьте поле **Startup Command** пустым).
3. Нажмите **Save**.

Для удаления OneAgent уберите ссылки на описанную выше интеграцию Dynatrace из образа приложения и повторно разверните приложение.

## Возможный конфликт с Application Insights

OneAgent может конфликтовать с агентами Azure Application Insights, уже инструментирующими приложение. Если данные мониторинга не поступают, проверьте, включён ли Application Insights, и повторите попытку с отключённым Application Insights.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")