# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-functions"

TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_PAAS = "Изучите концепцию токена доступа и его областей видимости."
TT_ENV_ID = "Познакомьтесь с окружениями мониторинга и научитесь с ними работать."
TT_ACTIVEGATE = "Ознакомьтесь с основными концепциями, связанными с ActiveGate."
TT_ONEAGENT_UPDATE = "Узнайте, как обновить OneAgent."
TT_AZURE_MONITORING = "Настройка и конфигурация мониторинга Azure в Dynatrace."
TT_NETZONES = "Узнайте, как работают сетевые зоны в Dynatrace."
TT_SERVERLESS = "Узнайте, как рассчитывается потребление при бессерверном мониторинге."
TT_ONEAGENT_MATRIX = "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."
TT_OTEL_FUNCTIONS = "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace."

TRANS = {
    "title: Monitor Azure Functions on App Service Plan for Windows": "title: Мониторинг Azure Functions на App Service Plan для Windows",
    "# Monitor Azure Functions on App Service Plan for Windows": "# Мониторинг Azure Functions на App Service Plan для Windows",
    "* How-to guide": "* Практическое руководство",
    "* 6-min read": "* Чтение: 6 мин",
    "* Published Oct 16, 2018": "* Опубликовано 16 октября 2018 г.",
    "## Capabilities": "## Возможности",
    "* Full-stack monitoring powered by OneAgent": "* Мониторинг полного стека на базе OneAgent",
    "* [Extension for easy deployment of OneAgent](#install-dynatrace-oneagent-site-extension-via-azure-portal)": "* [Расширение для простого развёртывания OneAgent](#install-dynatrace-oneagent-site-extension-via-azure-portal)",
    "* Support for Azure Functions that are written in .NET (in-process) and hosted on an **App Service Plan on Windows**": "* Поддержка Azure Functions, написанных на .NET (in-process) и размещённых на **App Service Plan для Windows**",
    "* Enhanced support for Azure App Service metadata such as compute mode, SKU, and more": "* Расширенная поддержка метаданных Azure App Service, таких как режим вычислений, SKU и другие",
    "* Automatic service detection for functions written in any language for Azure Function Runtime v2+": "* Автоматическое обнаружение сервисов для функций на любом языке для Azure Function Runtime v2+",
    "* Automatic tracing and code-profiling for .NET/.NET Core based functions": "* Автоматическая трассировка и профилирование кода для функций на .NET/.NET Core",
    "* End-to-end tracing across multiple functions for http-based triggers and other instrumented services and applications. Other triggers such as QueueTriggers require custom trace propagation.": "* Сквозная трассировка нескольких функций для триггеров на основе HTTP и других инструментированных сервисов и приложений. Другие триггеры, такие как QueueTriggers, требуют пользовательского распространения трассировки.",
    f"Dynatrace provides an [Azure Site Extension](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) to install OneAgent on Azure Functions. Azure Site Extensions are the native extension mechanism provided via [Kudu](https://github.com/projectkudu/kudu), which is the deployment management engine behind Azure App Services.": f"Dynatrace предоставляет [Azure Site Extension](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) для установки OneAgent в Azure Functions. Azure Site Extensions, это встроенный механизм расширений, предоставляемый через [Kudu](https://github.com/projectkudu/kudu), движок управления развёртыванием Azure App Services.",
    f'The Dynatrace OneAgent site extension doesn\'t include the OneAgent installer. Instead, the extension uses the Dynatrace REST API to download the installer from the cluster in the target version as set in [OneAgent updates](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent.").': f'Site extension Dynatrace OneAgent не включает в себя установщик OneAgent. Вместо этого расширение использует Dynatrace REST API для загрузки установщика из кластера в целевой версии, заданной в разделе [Обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "{TT_ONEAGENT_UPDATE}").',
    "Limitations": "Ограничения",
    "Since Azure Functions are a fully managed hosting platform built on top of Azure App Services, functions/applications are deployed into a sandboxed environment that doesn't allow direct access to the underlying operating system. This results in some restrictions for OneAgent:": "Поскольку Azure Functions являются полностью управляемой платформой хостинга, построенной на основе Azure App Services, функции/приложения развёртываются в изолированной среде (sandbox), которая не предоставляет прямого доступа к базовой операционной системе. Это влечёт ряд ограничений для OneAgent:",
    f'* Enhanced I/O monitoring requires [Azure Monitor integration](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.").': f'* Расширенный мониторинг ввода/вывода требует [интеграции с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "{TT_AZURE_MONITORING}").',
    "* Dynatrace Log Monitoring isn't supported for Azure Functions.": "* Dynatrace Log Monitoring не поддерживается для Azure Functions.",
    "* Network zones aren't supported.": "* Сетевые зоны не поддерживаются.",
    "## Prerequisites": "## Предварительные требования",
    f'* Create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").': f'* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "{TT_PAAS}").',
    f'* Determine your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Определите [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENV_ID}").',
    "* Determine your server URL if required.": "* Определите URL-адрес сервера, если требуется.",
    "The server URL is required only if you use either of the following:": "URL-адрес сервера требуется только при использовании одного из следующих вариантов:",
    "+ a Dynatrace Managed endpoint": "+ эндпоинт Dynatrace Managed",
    "+ an ActiveGate for a Dynatrace Managed or Dynatrace SaaS endpoint": "+ ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS",
    "(For Dynatrace SaaS, the URL is automatically generated from the environment ID.)": "(Для Dynatrace SaaS URL-адрес генерируется автоматически из идентификатора окружения.)",
    "+ **ActiveGate server URL:**": "+ **URL-адрес сервера ActiveGate:**",
    "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)": "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate можно настроить)",
    "+ **Dynatrace Managed server URL:**": "+ **URL-адрес сервера Dynatrace Managed:**",
    "`https://{your-domain}/e/{your-environment-id}/api`": "`https://{your-domain}/e/{your-environment-id}/api`",
    f'If you\'re using Dynatrace Managed, or if your cluster traffic should be routed through an [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), you need to configure the API endpoint used by the extension for downloading OneAgent.': f'При использовании Dynatrace Managed или если трафик кластера должен маршрутизироваться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "{TT_ACTIVEGATE}"), необходимо настроить API-эндпоинт, используемый расширением для загрузки OneAgent.',
    "## Install Dynatrace OneAgent site extension": "## Установка site extension Dynatrace OneAgent",
    "There are two ways to install the Dynatrace OneAgent site extension: via Azure Portal or using an ARM template. Follow the steps below for instructions.": "Существует два способа установки site extension Dynatrace OneAgent: через Azure Portal или с помощью ARM-шаблона. Инструкции приведены ниже.",
    "### Install Dynatrace OneAgent site extension via Azure Portal": "### Установка site extension Dynatrace OneAgent через Azure Portal",
    "1. In Azure Portal, go to the **App Services** and select an app service where you want to add the OneAgent extension.": "1. В Azure Portal откройте **App Services** и выберите сервис приложения, в который нужно добавить расширение OneAgent.",
    "2. In the left menu, go to to **Development Tools** > **Extensions**.": "2. В левом меню откройте **Development Tools** > **Extensions**.",
    "3. Select **Add**.": "3. Выберите **Add**.",
    "4. Select **Choose an Extension**.": "4. Выберите **Choose an Extension**.",
    "5. From the list of extensions, select Dynatrace OneAgent.": "5. В списке расширений выберите Dynatrace OneAgent.",
    "6. Accept legal terms and select **Add**. It should take a moment until you see the **Dynatrace OneAgent** extension on the list.": "6. Примите условия использования и нажмите **Add**. Через некоторое время расширение **Dynatrace OneAgent** появится в списке.",
    "7. In the left menu, go to to **Development Tools** > **Advanced Tools** and select **Go**. This will redirect you to the Kudu site.": "7. В левом меню откройте **Development Tools** > **Advanced Tools** и нажмите **Go**. Откроется сайт Kudu.",
    "![Kudu site](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)": "![Сайт Kudu](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)",
    "Kudu site": "Сайт Kudu",
    "8. Select **Site extensions**.": "8. Выберите **Site extensions**.",
    "9. Select **Launch** on the Dynatrace tile.": "9. На плитке Dynatrace нажмите **Launch**.",
    f'10. On the **Start monitoring your App Service instance** page, enter your environment ID, [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes."), and server URL. See [Prerequisites](#prerequisites) section for details.': f'10. На странице **Start monitoring your App Service instance** введите идентификатор окружения, [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "{TT_PAAS}") и URL-адрес сервера. Подробности см. в разделе [Предварительные требования](#prerequisites).',
    "11. Optional You can select **Accept all self-signed SSL certificates** to automatically accept all self-signed TLS certificates.": "11. Дополнительно можно выбрать **Accept all self-signed SSL certificates** для автоматического принятия всех самоподписанных TLS-сертификатов.",
    "12. Select **Install OneAgent**.": "12. Нажмите **Install OneAgent**.",
    "13. To check the deployment status, go to **Deployment Status**.": "13. Чтобы проверить статус развёртывания, откройте **Deployment Status**.",
    "14. After installation is complete, go to **Site extension** tab in Kudu and select **Restart Site**.": "14. После завершения установки перейдите на вкладку **Site extension** в Kudu и выберите **Restart Site**.",
    "15. Restart the App Service application to recycle the application's worker process": "15. Перезапустите приложение App Service для перезапуска рабочего процесса приложения",
    "After restart, OneAgent starts monitoring your application automatically.": "После перезапуска OneAgent автоматически начинает мониторинг приложения.",
    "### Install Dynatrace OneAgent site extension using an ARM template": "### Установка site extension Dynatrace OneAgent с помощью ARM-шаблона",
    "Alternatively to the main installation method via Azure Portal, you can make the Dynatrace site extension part of your ARM templates.": "Как альтернатива основному методу установки через Azure Portal, можно включить site extension Dynatrace в ARM-шаблоны.",
    "Example configuration:": "Пример конфигурации:",
    "| Parameter | Requirement | Description |": "| Параметр | Обязательность | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| DT\\_TENANT | Required | The environment ID as described in [Prerequisites](#prerequisites). |": "| DT\\_TENANT | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| DT\\_API\\_TOKEN | Required | The PaaS token as described in [Prerequisites](#prerequisites). |": "| DT\\_API\\_TOKEN | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| DT\\_API\\_URL | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |": "| DT\\_API\\_URL | Необязательный | URL-адрес сервера для настройки альтернативного коммуникационного эндпоинта, описанного в разделе [Предварительные требования](#prerequisites). |",
    "| DT\\_SSL\\_MODE | Optional | To automatically accept all self-signed TLS certificates, set the value to `all`. |": "| DT\\_SSL\\_MODE | Необязательный | Для автоматического принятия всех самоподписанных TLS-сертификатов установите значение `all`. |",
    "If `AlwaysOn` isn't set to `true`, the installation of OneAgent is triggered on the start-up/first request to Kudu.": "Если `AlwaysOn` не установлен в `true`, установка OneAgent запускается при старте или при первом запросе к Kudu.",
    "To check the deployment status, go to **Deployment Status**.": "Чтобы проверить статус развёртывания, откройте **Deployment Status**.",
    "After installation is complete, go to Azure Portal and restart the App Function application to recycle the application's worker process. Immediately after restart, OneAgent will begin monitoring your application.": "После завершения установки перейдите в Azure Portal и перезапустите приложение App Function для перезапуска рабочего процесса приложения. Сразу после перезапуска OneAgent начнёт мониторинг приложения.",
    "## Automate the installation and update of Dynatrace OneAgent site extension with Kudu REST API": "## Автоматизация установки и обновления site extension Dynatrace OneAgent с помощью Kudu REST API",
    f"After you install the Dynatrace OneAgent site extension, you can use the **Kudu REST API** to automate installation and update of the Dynatrace OneAgent site extension. See the [automation setup page on GitHub](https://github.com/Dynatrace/snippets/tree/master/technologies/azure/automate-appservice-siteextension-setup) for details.": f"После установки site extension Dynatrace OneAgent можно использовать **Kudu REST API** для автоматизации установки и обновления. Подробности см. на [странице настройки автоматизации на GitHub](https://github.com/Dynatrace/snippets/tree/master/technologies/azure/automate-appservice-siteextension-setup).",
    f"The root URL to access the REST API is `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, where you need to replace `<Your-AppService-Subdomain>` with your own value. To authenticate, you can use either the user publishing credentials or the site-level credentials. See [Accessing the Kudu service](https://github.com/projectkudu/kudu/wiki/Accessing-the-kudu-service) for details.": f"Корневой URL-адрес для доступа к REST API: `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, где `<Your-AppService-Subdomain>` необходимо заменить своим значением. Для аутентификации можно использовать учётные данные публикации пользователя или учётные данные на уровне сайта. Подробности см. в разделе [Доступ к сервису Kudu](https://github.com/projectkudu/kudu/wiki/Accessing-the-kudu-service).",
    "| Method | Endpoint | Description | Response |": "| Метод | Эндпоинт | Описание | Ответ |",
    "| --- | --- | --- | --- |": "| --- | --- | --- | --- |",
    '| GET | `/api/status` | Returns the current status of the OneAgent installation.  The returned "state" field can be:  * `NotInstalled` * `Downloading` * `Installing` * `Installed` * `Failed`  For automation, use **isAgentInstalled** and **isUpgradeAvailable** to determine whether OneAgent is installed and whether an upgrade is available. | ```  {  "state": "Installed",  "message": "OneAgent installed",  "version": "1.157",  "isAgentInstalled": true,  "isUpgradeAvailable": false,  "isFunction": false,  "functionAppSettings": null  } ``` |': '| GET | `/api/status` | Возвращает текущий статус установки OneAgent. Возвращаемое поле "state" может принимать значения:  * `NotInstalled` * `Downloading` * `Installing` * `Installed` * `Failed`  Для автоматизации используйте **isAgentInstalled** и **isUpgradeAvailable**, чтобы проверить, установлен ли OneAgent и доступно ли обновление. | ```  {  "state": "Installed",  "message": "OneAgent installed",  "version": "1.157",  "isAgentInstalled": true,  "isUpgradeAvailable": false,  "isFunction": false,  "functionAppSettings": null  } ``` |',
    '| GET | `/api/settings` | Returns the current settings, including Dynatrace credentials.  The value for `apiUrl` can be left empty for a SaaS environment. | ```  {  "apiUrl": "",  "apiToken": "<your-api-token>",  "environmentId": "<your-environment-id>",  "sslMode": "Default"  } ``` |': '| GET | `/api/settings` | Возвращает текущие настройки, включая учётные данные Dynatrace. Значение `apiUrl` может быть пустым для среды SaaS. | ```  {  "apiUrl": "",  "apiToken": "<your-api-token>",  "environmentId": "<your-environment-id>",  "sslMode": "Default"  } ``` |',
    "| PUT | `/api/settings` | Starts OneAgent installation with the given settings. These settings are stored only if the installation finishes successfully.  In the payload, you need to send the data in the format received by the `GET /dynatrace/api/settings` request.  If an update is available in the status request, this `PUT` request can be used to start the upgrade. | Empty response |": "| PUT | `/api/settings` | Запускает установку OneAgent с указанными настройками. Настройки сохраняются только при успешном завершении установки. В теле запроса данные передаются в формате, полученном в ответ на запрос `GET /dynatrace/api/settings`. Если в статусе доступно обновление, этот `PUT`-запрос можно использовать для его запуска. | Пустой ответ |",
    "## Override OneAgent configuration": "## Переопределение конфигурации OneAgent",
    "To override the default configuration, you can use the following parameters.": "Для переопределения конфигурации по умолчанию можно использовать следующие параметры.",
    "| Parameter | Description |": "| Параметр | Описание |",
    "| --- | --- |": "| --- | --- |",
    "| DT\\_CONNECTION\\_POINT | Semicolon-separated list of communication-endpoints |": "| DT\\_CONNECTION\\_POINT | Список коммуникационных эндпоинтов, разделённых точкой с запятой |",
    "How to add the DT\\_CONNECTION\\_POINT parameter in Azure Portal": "Добавление параметра DT\\_CONNECTION\\_POINT в Azure Portal",
    "To add the DT\\_CONNECTION\\_POINT parameter": "Порядок добавления параметра DT\\_CONNECTION\\_POINT",
    "1. In Azure Portal, select the web function you want to monitor.": "1. В Azure Portal выберите веб-функцию, которую нужно мониторить.",
    "2. Select **Settings** > **Configuration** > **Application Settings**.": "2. Выберите **Settings** > **Configuration** > **Application Settings**.",
    "3. Select **New application setting**.": "3. Нажмите **New application setting**.",
    "4. Enter the following key/value pair:": "4. Введите следующую пару ключ/значение:",
    "* Name: `DT_CONNECTION_POINT`": "* Имя: `DT_CONNECTION_POINT`",
    "* Value: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` with your own value.": "* Значение: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication` (замените `<YOUR_ACTIVEGATE_ADDRESS>` своим значением).",
    "![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)": "![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)",
    "DT connection": "Подключение DT",
    "5. Select **OK** to save the configuration.": "5. Нажмите **OK** для сохранения конфигурации.",
    "## Update OneAgent": "## Обновление OneAgent",
    "Dynatrace doesn't provide OneAgent updates on Azure Functions automatically. To update OneAgent on Azure Functions, go to Azure Portal, browse to your site extension, and, if an update is available, select **Update**. You can monitor the progress until the update is finished.": "Dynatrace не предоставляет автоматические обновления OneAgent для Azure Functions. Для обновления OneAgent в Azure Functions перейдите в Azure Portal, откройте site extension и, если доступно обновление, нажмите **Update**. Можно отслеживать ход обновления до его завершения.",
    "Then restart Azure Functions to recycle the application worker process.": "Затем перезапустите Azure Functions для перезапуска рабочего процесса приложения.",
    "The extension provides its own REST API for automating OneAgent updates. See [REST API](#restapi) for details.": "Расширение предоставляет собственный REST API для автоматизации обновлений OneAgent. Подробности см. в разделе [REST API](#restapi).",
    "### Update the site extension": "### Обновление site extension",
    "To update the site extension on Azure App Service, go to the Azure Portal, browse to your site extension, and, if an update is available, select **Update**.": "Для обновления site extension в Azure App Service перейдите в Azure Portal, откройте site extension и, если доступно обновление, нажмите **Update**.",
    "An update to the site extension doesn't force an update to OneAgent.": "Обновление site extension не принудительно обновляет OneAgent.",
    "When upgrading the extension from version 1.x to version 2.x, if you have **Always On** selected on your App Service, the upgrade of OneAgent is either triggered automatically, or on the first request to the UI extension. If you don't have **Always On** selected, you must restart App Service, so that the extension process starts.": "При обновлении расширения с версии 1.x до версии 2.x: если на App Service включён **Always On**, обновление OneAgent запускается автоматически или при первом запросе к UI-расширению. Если **Always On** не включён, необходимо перезапустить App Service, чтобы процесс расширения стартовал.",
    "## Uninstall OneAgent": "## Удаление OneAgent",
    "Removing the extension also removes OneAgent.": "Удаление расширения также удаляет OneAgent.",
    "If the application is running at the time of removal, the extension recognizes the running application, taking care to not remove any Dynatrace artifacts to prevent issues with the application. Instead, only the extension including the configuration is removed, so that, on the next restart of the application, OneAgent is no longer active.": "Если приложение работает в момент удаления, расширение обнаруживает запущенное приложение и, во избежание проблем, не удаляет артефакты Dynatrace. Удаляется только само расширение вместе с конфигурацией, так что OneAgent перестаёт работать при следующем запуске приложения.",
    "## Monitoring consumption": "## Потребление при мониторинге",
    f'See [Serverless monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details on monitoring consumption for Azure Functions.': f'Подробности о потреблении при мониторинге Azure Functions см. в разделе [Бессерверный мониторинг](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "{TT_SERVERLESS}").',
    "## Related topics": "## Связанные темы",
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    f'* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': f'* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "{TT_ONEAGENT_MATRIX}")',
    f'* [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")': f'* [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "{TT_OTEL_FUNCTIONS}")',
}

PASS = {
    "| --- | --- |",
    "| --- | --- | --- |",
    "| --- | --- | --- | --- |",
}

if __name__ == "__main__":
    build_one(REL, "integrate-oneagent-on-azure-functions.md", TRANS, PASS)
    qa_one(REL, "integrate-oneagent-on-azure-functions.md")
