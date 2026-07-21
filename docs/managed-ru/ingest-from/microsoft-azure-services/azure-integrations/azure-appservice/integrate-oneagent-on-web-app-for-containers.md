---
title: Интеграция OneAgent на Azure App Service for Linux и контейнерах
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers
---

# Интеграция OneAgent на Azure App Service for Linux и контейнерах

# Интеграция OneAgent на Azure App Service for Linux и контейнерах

* Практическое руководство
* Время чтения: 11 мин
* Обновлено 20 мая 2026 г.

Только Linux

App Service on Linux поддерживает два сценария.

* **Использование собственного кода**

  В сценарии с кодом App Service предоставляет базовый контейнер, который поддерживается платформой.

  Этот контейнер ориентирован на:

  + Фреймворк разработки, например .NET Core, PHP или Node.js.
  + Версию этого фреймворка, например .NET Core 3.0 или .NET Core 3.1.

  Следуй процедуре на вкладке **Built-in image**.
* **Использование собственного контейнера**

  В сценарии с контейнером App Service предоставляет хост, на котором может выполняться пользовательский контейнер, предоставленный клиентом.

  Подробнее о различиях между этими двумя сценариями см. [Things you should know: Web Apps on Linux﻿](https://dt-url.net/jm039gu).

  Для мониторинга App Services on Linux нужно интегрировать OneAgent с контейнеризированной средой приложения.

  Следуй процедуре на вкладке **Bootstrapper sidecar** (рекомендуется) или на вкладке **Custom image**. Метод Bootstrapper sidecar рекомендуется, поскольку он не требует изменений в образе приложения.

Bootstrapper sidecar

Built-in image

Custom image

## Интеграция Dynatrace с помощью bootstrapper sidecar

Рекомендуется OneAgent 1.333+

Публичный образ `dynatrace/dynatrace-codemodules` запускается как sidecar-контейнер рядом с веб-приложением. Он копирует OneAgent в постоянное общее хранилище по пути `/home/dynatrace/oneagent`, а `LD_PRELOAD` загружает его в приложение при перезапуске. Такой подход не требует изменений в образе приложения.

### Предварительные требования

* Linux Web App, настроенное с параметрами **Operating System: Linux** и **Publish: Container**
* Включено постоянное общее хранилище: нужно установить `WEBSITES_ENABLE_APP_SERVICE_STORAGE` в значение `true`. Bootstrapper записывает OneAgent по пути `/home/dynatrace/oneagent`; без подключённого хранилища OneAgent не сохранится после перезапуска.

### 1. Портал Azure: настройка переменных окружения

В портале Azure перейди в веб-приложение > **Settings** > **Environment variables** и добавь следующее:

| Переменная | Описание |
| --- | --- |
| `DT_CONNECTION_POINT` | Адрес конечной точки подключения Dynatrace. |
| `DT_TENANT` | ID окружения (тенанта). |
| `DT_TENANTTOKEN` | PaaS-токен для окружения Dynatrace. |
| `LD_PRELOAD` | `/home/dynatrace/oneagent/active/agent/lib64/liboneagentproc.so` |

### 2. Портал Azure: добавление контейнера bootstrapper sidecar

1. В портале Azure перейди в веб-приложение > **Deployment** > **Deployment Center**.
2. Выбери **Add** > **Custom container** и настрой следующее:

   | Параметр | Значение |
   | --- | --- |
   | Image source | Other container registries |
   | Image type | Public |
   | Registry server URL | `index.docker.io` |
   | Image and Tag | `dynatrace/dynatrace-codemodules:<version>`  (например, `dynatrace/dynatrace-codemodules:1.327.64.20260122-030637`) |
   | Startup command | `serverless --keep-alive --target /home/dynatrace/` |
3. Выбери **Save**.

#### Рекомендуется: разворачивать только нужные технологии

По умолчанию bootstrapper разворачивает все доступные технологии CodeModule. Чтобы сократить время запуска контейнера, нужно разворачивать только ту технологию, которую использует приложение, добавив флаг `--technology` к команде запуска.

Например, чтобы развернуть только CodeModule для Go:

```
serverless --keep-alive --target /home/dynatrace/ --technology=go
```

### 3. Портал Azure: проверка развёртывания и перезапуск

1. В Deployment Center выбери **View logs** для контейнера bootstrapper. Нужно дождаться записи в журнале `"msg":"OneAgent has been successfully deployed"`, периодически обновляя журнал, поскольку развёртывание может занять несколько минут.
2. Перейди в **Overview** и выбери **Restart**, чтобы перезапустить веб-приложение.

### Известные ограничения

**Требуется постоянное общее хранилище**: `WEBSITES_ENABLE_APP_SERVICE_STORAGE` должен быть установлен в значение `true`, чтобы bootstrapper мог записать OneAgent по пути `/home/dynatrace/oneagent`. Если установлено значение `false`, bootstrapper полностью пропускает развёртывание.

**Отсутствие автоматической очистки старых версий**: после обновления старые версии OneAgent остаются в общем хранилище. Их нужно удалять вручную.

## Интеграция Dynatrace на встроенном образе

Azure App Service for Linux позволяет настраивать базовый контейнер во время выполнения с помощью [startup script or script command﻿](https://dt-url.net/z2234qa), который должен выполняться в оболочке bash или в [Azure Cloud Shell﻿](https://dt-url.net/at034yy). Скрипт можно настроить несколькими способами.

### Задание команды/файла запуска при создании через Azure CLI

```
az webapp create -n <my-app> -g <my-resourcegroup> -p <my-appservice-plan> --runtime <runtime-tag> --startup-file <startup-script/command>
```

### Задание команды/файла скрипта при создании для существующего App Service

```
az webapp config set -n <my-app> -g <my-resourcegroup> --startup-file <startup-script/command>
```

### Задание команды/файла скрипта через ARM-шаблон

Используй свойство [appCommandLine﻿](https://docs.microsoft.com/en-us/azure/templates/microsoft.web/sites/config-web?pivots=deployment-language-arm-template#siteconfig-1) в ARM-шаблоне, чтобы задать скрипт/команду запуска.

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

### Задание команды/файла запуска в портале Azure

![AppService Linux Portal Startup](https://dt-cdn.net/images/screenshot-2022-12-13-at-13-42-44-1109-8955530cdd.png)

AppService Linux Portal Startup

### Скрипт или команда?

Startup script, это то же самое, что и startup command: это команда, которая выполняет скрипт (не забудь указать путь к скрипту). Однако для этого нужно упаковать скрипт вместе с приложением. Если такая зависимость нежелательна, используй startup commands.

Скрипт/команда выполняется в рамках init-скрипта контейнера, который реализован по-разному для каждого технологического стека.

Подробнее о startup commands см. в документации Azure App Service for Linux в разделе [What are the expected values for the Startup File section when I configure the runtime stack?﻿](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

### Интеграция Dynatrace с помощью скрипта/команды запуска

Для интеграции Dynatrace скрипту/команде запуска нужен доступ к нескольким переменным.

| Параметр | Описание |
| --- | --- |
| `$DT_ENDPOINT` | Конечная точка сервера API Dynatrace, используется либо [конечная точка кластера](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти идентификатор среды, а также как настроить и подключить несколько сред.") среды, либо [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные концепции, связанные с ActiveGate."). |
| `$DT_API_TOKEN` | Токен API для доступа к REST API Dynatrace, [создать токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования API Dynatrace.") с областью **InstallerDownload**. |
| `$DT_INCLUDE` | Настройка необходимых модулей кода в зависимости от используемого технологического стека.  * `all` включает все доступные модули кода OneAgent (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), но увеличивает размер загружаемого пакета. * Либо можно выбрать идентификаторы, соответствующие стеку приложения, например `java`, `dotnet`, `nodejs` или `php`.  Подробности в [документации API](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузка последнего установщика OneAgent через API Dynatrace."). |
| `$START_APP_CMD` | Команда для запуска приложения  [Какие значения ожидаются в разделе Startup File при настройке стека среды выполнения?﻿](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-) |

Если используется оболочка, отличная от bash, скрипт нужно адаптировать под требования экранирования символов этой оболочки.

Это можно сделать двумя способами.

* Настройки App service Рекомендуется
* Указание значений в строке

#### Мониторинг PHP на NGINX

Для мониторинга PHP-FPM и NGINX одновременно

1. Установить `DT_INCLUDE` в значение `all`.
2. Использовать скрипт запуска с двумя дополнительными командами в конце.

   ```
   echo '/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so' >> /etc/ld.so.preload



   /etc/init.d/nginx restart
   ```

#### Настройки App service

Указать значения перечисленных выше параметров через [App Settings﻿](https://dt-url.net/da239ts) (это эквивалентно заданию переменных среды), а затем выполнить эту команду.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && sh /tmp/installer-wrapper.sh
```

Стек Java Runtime

Для приложений, работающих на стеке Java Runtime в App Service Azure, этот способ установки в некоторых случаях может работать не так, как ожидается. Например, клиенты сообщали о проблемах с образами на базе Alpine, когда указанная выше команда интерпретировалась как единая строка, а не выполнялась как команда оболочки. Из-за этого оператор `&&` воспринимался как часть входных данных `wget`, а не как объединение команд.

При возникновении такого поведения стоит рассмотреть альтернативный способ выполнения скрипта (например, пользовательский скрипт запуска или изменение [пользовательского образа](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#install--custom-image "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")).

Также можно использовать приведённый ниже скрипт только для вызова, который работает для всех образов Linux.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



sh $installerWrapperInstallationPath
```

#### Указание значений в строке

Необходимые переменные можно задать только для команды, которая запускает установщик OneAgent.

Для этого значения нужно указать перед командой, как показано ниже.

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

### Пример: интеграция в приложение node.js с помощью CLI Azure в оболочке bash

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настройка команды запуска**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-1 "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Дважды перезапустить веб-приложение**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-2 "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")

#### Шаг 1 Настройка команды запуска

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

#### Шаг 2 Дважды перезапустить веб-приложение

После настройки команды запуска нужно перезапустить веб-приложение **дважды**.

* Первый перезапуск инициализирует установку OneAgent.
* Второй перезапуск запускает инструментирование приложения OneAgent.

## Интеграция Dynatrace на пользовательском образе

Для интеграции OneAgent с образом приложения есть два варианта:

* [Интеграция слоя образа OneAgent, предоставляемого Dynatrace](#layer)
* [Загрузка артефактов OneAgent во время сборки образа из REST API Dynatrace](#api)

### Вариант 1: интеграция с помощью слоя образа OneAgent от Dynatrace

Для этого варианта на компьютере должен быть установлен Docker версии 17.05 и выше.

1. Войти в Docker, используя идентификатор среды Dynatrace в качестве имени пользователя и PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Добавить следующие строки в Dockerfile образа приложения после последней команды `FROM`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Заменить в шаблоне следующие плейсхолдеры.

   | Параметр | Описание |
   | --- | --- |
   | `<ADDRESS>` | Конечная точка реестра Dynatrace, используется либо [конечная точка кластера](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти идентификатор среды, а также как настроить и подключить несколько сред.") среды, либо [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные концепции, связанные с ActiveGate."). |
   | `<TECHNOLOGY>` | Настройка необходимых модулей кода в зависимости от используемого технологического стека.  * `all` включает все доступные модули кода OneAgent (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), но увеличивает размер загружаемого пакета. * Либо можно выбрать идентификаторы, соответствующие стеку приложения, например `java`, `dotnet`, `nodejs` или `php`.  Подробности в [документации API](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузка последнего установщика OneAgent через API Dynatrace."). |

   **Что делать, если образ Docker основан на Alpine Linux?**

   OneAgent Dynatrace поддерживает среды на базе Alpine Linux. Чтобы использовать совместимый с Alpine Linux OneAgent, нужно указать имя образа `oneagent-codemodules-musl` (как показано в адаптированном шаблоне ниже) вместо `oneagent-codemodules`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
3. Собрать образ приложения.

   Собрать образ Docker из Dockerfile, чтобы использовать его в среде Kubernetes.

   ```
   docker build -t yourapp .
   ```
4. Перезапустить веб-приложение **дважды**.

   * Первый перезапуск инициализирует установочный скрипт OneAgent.
   * Второй перезапуск запускает OneAgent на хосте.

### Вариант 2: интеграция с использованием скрипта установки из Dynatrace REST API

1. Добавить следующие две строки в Dockerfile.

   ```
   RUN wget -O /tmp/installer.sh -q "<DT_ENDPOINT>/api/v1/deployment/installer/agent/unix/paas-sh/latest?Api-Token=<DT_API_TOKEN>&flavor=<DT_FLAVOR>&include=<DT_INCLUDE>" && sh /tmp/installer.sh



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Заменить следующие параметры в шаблоне выше.

   | Параметр | Описание |
   | --- | --- |
   | `<DT_ENDPOINT>` | Конечная точка Dynatrace API: использовать либо [конечную точку кластера](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") среды, либо [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."). |
   | `<DT_API_TOKEN>` | Токен API для доступа к Dynatrace REST API: [создать токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") с областью действия **InstallerDownload**. |
   | `<DT_FLAVOR>` | Настроить требуемую архитектуру.  * `default` для стандартных образов Linux на базе glibc * `musl` для образов на базе Alpine Linux |
   | `<DT_INCLUDE>` | Настроить требуемые модули кода в зависимости от используемого стека технологий.  * `all` включает все доступные модули кода OneAgent (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), но это увеличивает размер загружаемого пакета. * В качестве альтернативы выбрать идентификаторы, соответствующие стеку приложения, например `java`, `dotnet`, `nodejs` или `php`.  Подробности см. в [документации API](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API."). |
2. Собрать образ приложения.

   Собрать образ Docker из Dockerfile, чтобы использовать его в среде Kubernetes.

   ```
   docker build -t yourapp .
   ```
3. Перезапустить веб-приложение **дважды**.

   * Первый перезапуск инициализирует скрипт установки OneAgent.
   * Второй перезапуск запускает OneAgent на хосте.

## Дополнительная настройка

Использовать дополнительные переменные окружения для настройки OneAgent в целях устранения неполадок или расширенной сетевой конфигурации. Их можно задать либо через настройки приложения App Service, либо, при использовании пользовательского образа контейнера, настроить в Dockerfile образа приложения.

### Сетевые переменные Необязательно

| Параметр | Описание |
| --- | --- |
| `DT_NETWORK_ZONE` | Указывает на использование зоны сети. Подробнее см. [зоны сети](/managed/manage/network-zones "Find out how network zones work in Dynatrace."). |
| `DT_PROXY` | При использовании прокси эта переменная окружения передаёт учётные данные прокси. Подробнее см. [Настройка OneAgent на контейнерах для мониторинга уровня приложений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring."). |

### Дополнительные метаданные для группировки процессов и обнаружения сервисов Необязательно

При перечислении нескольких тегов их нужно заключить в двойные кавычки, например: DT\_TAGS="Tag1=Value1 Tag2=Value2".

| Параметр | Описание |
| --- | --- |
| `DT_LOCALTOVIRTUALHOSTNAME` | Иногда несколько контейнеров обнаруживаются как единый экземпляр (localhost), что приводит к различным проблемам, например, при обнаружении сервисов или оповещениях о доступности. Эта переменная окружения задаёт уникальное имя для экземпляра контейнера. Подробности см. в [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1#adjusting-service-detection "Find out how Dynatrace Service Detection v1 detects and names different types of services.") |
| `DT_APPLICATIONID` | Некоторые технологии не предоставляют уникальные имена приложений. В таких случаях эта переменная окружения задаёт уникальное имя. Подробнее см. [Проблемы именования веб-сервера](/managed/observe/application-observability/services/service-detection/service-detection-v1#web-server-naming-issues "Find out how Dynatrace Service Detection v1 detects and names different types of services."). |
| `DT_TAGS` | Применяет [пользовательские теги](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") к группе процессов. |
| `DT_CUSTOM_PROP` | Применяет [пользовательские метаданные](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") к группе процессов. |
| `DT_CLUSTER_ID` | Если [правила обнаружения групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") не подходят для конкретного случая, эта переменная окружения позволяет **сгруппировать все процессы с одинаковым значением**. |
| `DT_NODE_ID` | Если [правила обнаружения групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") не подходят для конкретного случая, эта переменная окружения позволяет **разделить экземпляры группы процессов**. |

### Валидационные переменные Необязательно

| Параметр | Описание |
| --- | --- |
| `DT_LOGSTREAM` | Задать эту переменную со значением `stdout`, чтобы настроить OneAgent на запись ошибок в консоль. Чтобы увидеть дополнительные логи OneAgent, задать уровень логирования с помощью `DT_LOGLEVELCON`, как указано ниже. |
| `DT_LOGLEVELCON` | Эта переменная окружения задаёт уровень логирования консоли. Допустимые значения: `NONE`, `SEVERE` и `INFO`. |

### Переменные, специфичные для .NET

Этот раздел содержит переменные, актуальные только для **сред .NET**.

| Параметр | Описание |
| --- | --- |
| `DT_AGENTACTIVE` | Переменная, специфичная для .NET, для настройки мониторинга OneAgent приложений .NET Framework и .NET Core. Мониторинг OneAgent .NET по умолчанию активен (`true`). Чтобы деактивировать его, задать `DT_AGENTACTIVE` значение `false`. При настройке мониторинга .NET с использованием переменных окружения профилировщика .NET нужно задать `DT_AGENTACTIVE` значение `true`, чтобы активировать его. |

## Обновление OneAgent

Bootstrapper sidecar

Встроенный образ

Пользовательский образ

1. В портале Azure перейти к веб-приложению > **Deployment** > **Deployment Center**.
2. Выбрать контейнер bootstrapper.
3. Обновить тег в поле **Image and Tag** до новой версии OneAgent и выбрать **Apply**.
4. Проверить развёртывание и перезапустить веб-приложение, как описано в шаге 3 вкладки **Bootstrapper sidecar** раздела Install.

Когда доступно обновление, перезапустить приложение, чтобы обновить OneAgent.

Каждый раз, когда нужно использовать новую версию Dynatrace OneAgent, нужно пересобрать локальные модули кода OneAgent и образ приложения. Любые новые поды, запущенные из этого образа приложения, будут отслеживаться последней версией OneAgent.

Если для новых хостов и приложений указана версия установки OneAgent по умолчанию с помощью [настроек обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), веб-приложения будут автоматически отслеживаться заданной по умолчанию версией OneAgent.

## Удаление OneAgent

Встроенный образ

Пользовательский образ

Чтобы удалить OneAgent

1. В портале Azure перейти к веб-приложению > **Configuration** > **General settings**.
2. Удалить команду запуска (оставить поле **Startup Command** пустым).
3. Выбрать **Save**.

Чтобы удалить OneAgent, удалить ссылки на описанную выше интеграцию Dynatrace из образа приложения и повторно развернуть приложение.

## Возможный конфликт с Application Insights

OneAgent может конфликтовать с агентами Azure Application Insights, уже инструментирующими приложение. Если данные мониторинга не поступают, проверить, включён ли Application Insights, и повторить попытку с отключённым Application Insights.

## Похожие темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")