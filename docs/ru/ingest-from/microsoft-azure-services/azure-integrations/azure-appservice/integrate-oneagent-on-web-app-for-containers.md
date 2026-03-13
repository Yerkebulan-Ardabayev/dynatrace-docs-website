---
title: Integrate OneAgent on Azure App Service for Linux and containers
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers
scraped: 2026-03-06T21:26:42.608656
---

# Интеграция OneAgent в Azure App Service для Linux и контейнеров

# Интеграция OneAgent в Azure App Service для Linux и контейнеров

* Latest Dynatrace
* Практическое руководство
* 11 мин. чтения
* Обновлено 17 декабря 2025

Только Linux

App Service на Linux поддерживает два сценария.

* **Принесите свой код (Bring your own code)**

  В сценарии с кодом App Service предоставляет базовый контейнер, который поддерживается платформой.

  Этот контейнер ориентирован на:

  + Фреймворк разработки, например .NET Core, PHP или Node.js.
  + Версию этого фреймворка, например .NET Core 3.0 или .NET Core 3.1.

  Следуйте процедуре на вкладке **Built-in image**.
* **Принесите свой контейнер (Bring your own container)**

  В сценарии с контейнером App Service предоставляет хост, на котором может выполняться пользовательский контейнер, предоставленный клиентом.

  Подробнее о различиях между двумя сценариями см. [Что нужно знать: Web Apps на Linux](https://dt-url.net/jm039gu).

  Для мониторинга App Services на Linux необходимо интегрировать OneAgent в ваше контейнеризированное приложение.

  Следуйте процедуре на вкладке **Custom image**.

Built-in image

Custom image

## Интеграция Dynatrace со встроенным образом

Azure App Service для Linux позволяет настраивать базовый контейнер во время выполнения с помощью [стартового скрипта или команды](https://dt-url.net/z2234qa), которая должна выполняться в оболочке bash или [Azure Cloud Shell](https://dt-url.net/at034yy). Скрипт можно настроить несколькими способами.

### Установка стартового скрипта/команды при создании с помощью Azure CLI

```
az webapp create -n <my-app> -g <my-resourcegroup> -p <my-appservice-plan> --runtime <runtime-tag> --startup-file <startup-script/command>
```

### Установка скрипта/команды для существующего App Service

```
az webapp config set -n <my-app> -g <my-resourcegroup> --startup-file <startup-script/command>
```

### Установка скрипта/команды с помощью шаблона ARM

Используйте свойство [appCommandLine](https://docs.microsoft.com/en-us/azure/templates/microsoft.web/sites/config-web?pivots=deployment-language-arm-template#siteconfig-1) вашего шаблона ARM для установки стартового скрипта/команды.

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

### Установка стартового скрипта/команды через портал Azure

![Стартовый скрипт Linux AppService в портале](https://dt-cdn.net/images/screenshot-2022-12-13-at-13-42-44-1109-8955530cdd.png)

### Скрипт или команда?

Стартовый скрипт — это то же самое, что и стартовая команда: это команда, которая выполняет скрипт (не забудьте указать путь к скрипту). Однако для этого необходимо упаковать скрипт вместе с вашим приложением. Если вы не хотите иметь эту зависимость, используйте стартовые команды.

Скрипт/команда выполняется внутри скрипта инициализации контейнера, который реализован по-разному в каждом технологическом стеке.

Подробнее о стартовых командах см. документацию Azure App Service для Linux [Какие ожидаемые значения для раздела Startup File при настройке стека среды выполнения?](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

### Интеграция Dynatrace с помощью стартового скрипта/команды

Для интеграции Dynatrace стартовый скрипт/команда должен иметь доступ к нескольким переменным.

Если вы используете оболочку, отличную от bash, убедитесь, что скрипт адаптирован в соответствии с требованиями к экранированию символов данной оболочки.

Это можно сделать двумя способами.

* Настройки App Service (рекомендуется)
* Установка значений встроенным образом

#### Мониторинг PHP на NGINX

Для мониторинга как PHP-FPM, так и NGINX

1. Установите `DT_INCLUDE` в значение `all`.
2. Используйте стартовый скрипт с двумя дополнительными командами в конце.

   ```
   echo '/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so' >> /etc/ld.so.preload



   /etc/init.d/nginx restart
   ```

#### Настройки App Service

Установите значения вышеуказанных параметров с помощью [App Settings](https://dt-url.net/da239ts) — это эквивалентно установке переменных окружения — а затем выполните эту команду.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && sh /tmp/installer-wrapper.sh
```

Стек среды выполнения Java

Для приложений, работающих на стеке среды выполнения Java в Azure App Service, этот метод установки может работать не так, как ожидается, в некоторых случаях. Например, пользователи сообщали о проблемах с образами на основе Alpine, где указанная выше команда интерпретировалась как единая строка, а не выполнялась как команда оболочки. Это приводило к тому, что оператор `&&` обрабатывался как часть ввода `wget`, а не как связующий элемент команд.

Если вы столкнулись с таким поведением, рассмотрите альтернативный подход к выполнению скрипта (например, пользовательский стартовый скрипт или модификация [пользовательского образа](integrate-oneagent-on-web-app-for-containers.md#install--custom-image "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent в контейнеризированных приложениях на Linux.")).

В качестве альтернативы вы можете использовать приведённый ниже скрипт вызова, который работает для всех образов Linux.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



sh $installerWrapperInstallationPath
```

#### Установка значений встроенным образом

Вы можете установить необходимые переменные только для команды, запускающей установщик OneAgent.

Для этого необходимо задать значения перед командой, как показано ниже.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh
```

В качестве альтернативы вы можете использовать стартовый файл, как показано ниже.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh $installerWrapperInstallationPath
```

### Пример: Интеграция в приложение Node.js с помощью Azure CLI в оболочке bash

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настройте стартовую команду**](integrate-oneagent-on-web-app-for-containers.md#step-1 "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent в контейнеризированных приложениях на Linux.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Перезапустите веб-приложение дважды**](integrate-oneagent-on-web-app-for-containers.md#step-2 "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent в контейнеризированных приложениях на Linux.")

#### Шаг 1 Настройте стартовую команду

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

#### Шаг 2 Перезапустите веб-приложение дважды

После настройки стартовой команды перезапустите веб-приложение **дважды**.

* Перезапустите один раз для инициализации установки OneAgent.
* Перезапустите ещё раз, чтобы OneAgent начал инструментирование вашего приложения.

## Интеграция Dynatrace с пользовательским образом

Для интеграции OneAgent с образом приложения у вас есть два варианта:

* [Интеграция слоя образа OneAgent, предоставленного Dynatrace](#layer)
* [Загрузка артефактов OneAgent во время сборки образа из Dynatrace REST API](#api)

### Вариант 1: Интеграция с использованием предоставленного Dynatrace слоя образа OneAgent

Для этого варианта требуется Docker v17.05+ на вашем компьютере.

1. Войдите в Docker, используя идентификатор вашей среды Dynatrace в качестве имени пользователя и PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Добавьте следующие строки в Dockerfile вашего образа приложения после последней команды `FROM`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /

   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Замените заполнители в шаблоне.

   **Что если мой Docker-образ основан на Alpine Linux?**

   Dynatrace OneAgent поддерживает среды на основе Alpine Linux. Для использования совместимого с Alpine Linux агента OneAgent используйте имя образа `oneagent-codemodules-musl` (как показано в адаптированном шаблоне ниже) вместо `oneagent-codemodules`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /

   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
3. Соберите образ приложения.

   Соберите Docker-образ из вашего Dockerfile для использования в среде Kubernetes.

   ```
   docker build -t yourapp .
   ```
4. Перезапустите веб-приложение **дважды**.

   * Перезапустите один раз для инициализации скрипта установки OneAgent.
   * Перезапустите ещё раз, чтобы запустить OneAgent на хосте.

### Вариант 2: Интеграция с использованием скрипта установки из Dynatrace REST API

1. Добавьте следующие две строки в ваш Dockerfile.

   ```
   RUN wget -O /tmp/installer.sh -q "<DT_ENDPOINT>/api/v1/deployment/installer/agent/unix/paas-sh/latest?Api-Token=<DT_API_TOKEN>&flavor=<DT_FLAVOR>&include=<DT_INCLUDE>" && sh /tmp/installer.sh

   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Замените следующие параметры в шаблоне выше.
2. Соберите образ приложения.

   Соберите Docker-образ из вашего Dockerfile для использования в среде Kubernetes.

   ```
   docker build -t yourapp .
   ```
3. Перезапустите веб-приложение **дважды**.

   * Перезапустите один раз для инициализации скрипта установки OneAgent.
   * Перезапустите ещё раз, чтобы запустить OneAgent на хосте.

## Дополнительная настройка (необязательно)

Используйте дополнительные переменные окружения для настройки OneAgent для устранения неполадок или расширенной сетевой конфигурации. Вы можете установить их через настройки приложения App Service или, при использовании пользовательского образа контейнера, настроить их в Dockerfile вашего образа приложения.

### Сетевые переменные

### Дополнительные метаданные для группировки процессов и обнаружения сервисов

При указании нескольких тегов необходимо заключать их в двойные кавычки, например: DT\_TAGS="Tag1=Value1 Tag2=Value2".

### Проверка переменных

## Обновление OneAgent

Built-in image

Custom image

При наличии обновления перезапустите приложение для обновления OneAgent.

Каждый раз, когда вы хотите использовать новую версию Dynatrace OneAgent, необходимо пересобрать локальные модули кода OneAgent и образ приложения. Все вновь запущенные поды из этого образа приложения будут мониториться с последней версией OneAgent.

Если вы указали версию OneAgent по умолчанию для установки на новых хостах и в приложениях с помощью [настроек обновления OneAgent](../../../dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux.md "Узнайте о различных способах обновления OneAgent на Linux."), ваши веб-приложения будут автоматически мониториться указанной версией OneAgent по умолчанию.

## Удаление OneAgent

Built-in image

Custom image

Чтобы удалить OneAgent

1. В портале Azure перейдите к вашему веб-приложению > **Configuration** > **General settings**.
2. Удалите стартовую команду (оставьте поле **Startup Command** пустым).
3. Выберите **Save**.

Для удаления OneAgent удалите описанные выше ссылки на интеграцию Dynatrace из образа приложения и повторно разверните приложение.

## Возможный конфликт с Application Insights

OneAgent может конфликтовать с агентами Azure Application Insights, которые уже инструментируют приложение. Если вы не видите поступающих данных мониторинга, проверьте, включён ли Application Insights, и повторите попытку с выключенным Application Insights.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](../../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")