---
title: Интеграция OneAgent в Azure App Service для Windows
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service
scraped: 2026-05-12T11:23:53.114700
---

# Интеграция OneAgent в Azure App Service для Windows

# Интеграция OneAgent в Azure App Service для Windows

* Практическое руководство
* Чтение: 9 мин
* Опубликовано 16 октября 2018 г.

Azure App Service предоставляет множество различных вариантов хостинга для Windows, Linux и контейнеров: с общей инфраструктурой ([App Service Plan](https://dt-url.net/f4031wl)) или с полностью изолированной и выделенной инфраструктурой ([Azure App Service Environment](https://dt-url.net/u0231c3)).

## Возможности

Интеграция App Service с Dynatrace обеспечивает следующие возможности:

* [Интеграция OneAgent на Windows через расширение для простого развёртывания](#install)
* [Интеграция OneAgent на Linux и в контейнерах](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")
* Автоматическая распределённая трассировка и мониторинг для .NET/.NET Core, Java, Node.js, PHP и IIS
* Расширенный захват метаданных Azure App Service, таких как SKU и Website-Name
* Захват метрик на уровне платформы и [дополнительная аналитика по App Service Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Мониторинг Azure App Service (App Service Plan, слот развёртывания Web App) и просмотр доступных метрик.") через [интеграцию с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Захват журналов через [log forwarding](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте log forwarding в Azure для приёма журналов Azure.")

**Ограничения**
Поскольку Azure App Service является полностью управляемой платформой хостинга, приложения развёртываются в изолированной среде (sandbox), которая не предоставляет прямого доступа к базовой операционной системе. Интеграция OneAgent для Azure App Service использует подход только на уровне приложения или универсальную инъекцию, что приводит к некоторым отличиям от установки Full-Stack OneAgent:

* Мониторинг ввода/вывода требует включения [интеграции с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка и конфигурация мониторинга Azure в Dynatrace."), которая также обеспечивает [дополнительную аналитику по App Service Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Мониторинг Azure App Service (App Service Plan, слот развёртывания Web App) и просмотр доступных метрик.")
* Захват журналов требует включения [log forwarding](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте log forwarding в Azure для приёма журналов Azure.")
* Автоматические обновления OneAgent необходимо запускать через [REST API site extension Dynatrace OneAgent](#restapi)
* Настройка группы хостов недоступна

## Установка site extension Dynatrace OneAgent

Только Windows

Dynatrace предоставляет [site extension](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) для установки OneAgent в Azure App Services на Windows.

Для Azure App Service на Linux или в контейнерах см. [Интеграция OneAgent в Azure App Service на Linux и в контейнерах](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.").

Site extension, это встроенный механизм расширений, предоставляемый через [Kudu](https://github.com/projectkudu/kudu), движок управления развёртыванием Azure App Services.

Site extension Dynatrace OneAgent не включает в себя установщик OneAgent. Вместо этого расширение использует Dynatrace REST API для загрузки установщика из кластера в целевой версии, заданной в разделе [Обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Узнайте, как обновить OneAgent.").

Существует несколько способов установки site extension Dynatrace OneAgent:

* [Вручную через Azure Portal](#portal)
* [Автоматически с помощью ARM-шаблона](#arm)
* [Путём автоматизации настройки с помощью пользовательского скрипта PowerShell](#script)

Инструкции приведены ниже.

### Предварительные требования

* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей видимости.").
* Определите [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Познакомьтесь с окружениями мониторинга и научитесь с ними работать.").
* Определите URL-адрес сервера, если требуется.

  URL-адрес сервера требуется только при использовании одного из следующих вариантов:

  + эндпоинт Dynatrace Managed
  + ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS

  (Для Dynatrace SaaS URL-адрес генерируется автоматически из идентификатора окружения.)

  + **URL-адрес сервера ActiveGate:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate можно настроить)
  + **URL-адрес сервера Dynatrace Managed:**
    `https://{your-domain}/e/{your-environment-id}/api`

  При использовании Dynatrace Managed или если трафик кластера должен маршрутизироваться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с основными концепциями, связанными с ActiveGate."), необходимо настроить API-эндпоинт, используемый расширением для загрузки OneAgent.

### Установка вручную через Azure Portal

1. В Azure Portal откройте **App Services** и выберите сервис приложения, в который нужно добавить расширение OneAgent.
2. В левом меню откройте **Development Tools** > **Extensions**.
3. Выберите **Add**.
4. Выберите **Choose an Extension**.
5. В списке расширений выберите Dynatrace OneAgent.
6. Примите условия использования и нажмите **Add**. Через некоторое время расширение **Dynatrace OneAgent** появится в списке.
7. В левом меню откройте **Development Tools** > **Advanced Tools** и нажмите **Go**. Откроется сайт Kudu.

   ![Сайт Kudu](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)

   Сайт Kudu
8. Выберите **Site extensions**.
9. На плитке Dynatrace нажмите **Launch**.
10. На странице **Start monitoring your App Service instance** введите идентификатор окружения, [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей видимости.") и URL-адрес сервера. Подробности см. в разделе [Предварительные требования](#prerequisites).
11. Дополнительно можно выбрать **Accept all self-signed SSL certificates** для автоматического принятия всех самоподписанных TLS-сертификатов.
12. Нажмите **Install OneAgent**.
13. Чтобы проверить статус развёртывания, откройте **Deployment Status**.
14. После завершения установки перейдите на вкладку **Site extension** в Kudu и выберите **Restart Site**.
15. Перезапустите приложение App Service для перезапуска рабочего процесса приложения

После перезапуска OneAgent автоматически начинает мониторинг приложения.

### Автоматическая установка с помощью ARM-шаблона

Как альтернатива установке через Azure Portal можно включить site extension Dynatrace в ARM-шаблоны.

ARM-шаблон

Обратите внимание, что приведённый ниже пример конфигурации является шаблоном, и часть значений необходимо изменить.

Пример конфигурации:

dynatrace-oneagent-site-extension.json

```
{



"$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",



"contentVersion": "1.0.0.0",



"parameters": {



// WebApp Settings



"siteName": {



"type": "string",



"metadata": {



"description": "Web app name where you would like to install extension."



}



},



"location": {



"type": "string",



"metadata": {



"description": "Region of your web app."



}



},



"skuCapacity": {



"type": "int",



"defaultValue": 1,



"minValue": 1,



"metadata": {



"description": "Describes plan's instance count."



}



},



"skuName": {



"type": "string",



"defaultValue": "B1",



"allowedValues": [



"B1",



"B2",



"B3",



"D1",



"F1",



"I1",



"I1v2",



"I2",



"I2v2",



"I3",



"I3v2",



"P1V2",



"P1V3",



"P2V2",



"P2V3",



"P3V2",



"P3V3",



"PC2",



"PC3",



"PC4",



"S1",



"S2",



"S3"



],



"metadata": {



"description": "Describes plan's pricing tier and instance size. Check details at https://azure.microsoft.com/en-us/pricing/details/app-service/."



}



},



"webAppAlwaysOn": {



"type": "bool",



"metadata": {



"description": "If AlwaysOn isn't set to true, installation of OneAgent is triggered on the start-up/first request to Kudu."



},



"defaultValue": true



},



// Dynatrace OneAgent site extension settings



"environmentID": {



"type": "string",



"metadata": {



"description": "The environment ID."



}



},



"APIToken": {



"type": "string",



"metadata": {



"description": "The PaaS token."



}



},



"APIUrl": {



"type": "string",



"metadata": {



"description": "The server URL, if you want to configure an alternative communication endpoint."



}



},



"SSLMode": {



"type": "string",



"metadata": {



"description": "To automatically accept all self-signed TLS certificates, set the value to all."



},



"allowedValues": ["default", "all"],



"defaultValue": "default"



},



"monitoredCLR": {



"type": "string",



"metadata": {



"description": "Your .NET application runtime"



},



"allowedValues": ["both", "coreclr", "clr"],



"defaultValue": "both"



},



"networkZone": {



"type": "string",



"metadata": {



"description": "Your network zone. Set the value you want for your App Service instance. See network zones for more information."



},



"defaultValue": ""



}



},



"resources": [



{



"apiVersion": "2020-12-01",



"name": "[parameters('siteName')]",



"type": "Microsoft.Web/serverfarms",



"location": "[parameters('location')]",



"sku": {



"name": "[parameters('skuName')]",



"capacity": "[parameters('skuCapacity')]"



},



"properties": {



"name": "[parameters('siteName')]"



}



},



{



"apiVersion": "2020-12-01",



"name": "[parameters('siteName')]",



"type": "Microsoft.Web/sites",



"properties": {



"name": "[parameters('siteName')]",



"siteConfig": {



"alwaysOn": "[parameters('webAppAlwaysOn')]",



"appSettings": [



{ "Name": "DT_TENANT", "Value": "[parameters('environmentID')]" },



{ "Name": "DT_API_TOKEN", "Value": "[parameters('APIToken')]" },



{ "Name": "DT_API_URL", "Value": "[parameters('APIUrl')]" },



{ "Name": "DT_SSL_MODE", "Value": "[parameters('SSLMode')]" },



{ "Name": "DT_MONITORED_CLR", "Value": "[parameters('monitoredCLR')]" },



{ "Name": "DT_NETWORK_ZONE", "Value": "[parameters('networkZone')]" }



]



},



"serverFarmId": "[resourceId('Microsoft.Web/serverfarms', parameters('siteName'))]"



},



"dependsOn": ["[concat('Microsoft.Web/serverfarms/', parameters('siteName'))]"],



"location": "[parameters('location')]",



"resources": [



{



"apiVersion": "2020-12-01",



"name": "Dynatrace",



"type": "siteextensions",



"dependsOn": ["[resourceId('Microsoft.Web/sites/', parameters('siteName'))]"]



}



]



}



],



"outputs": {}



}
```

| Параметр WebApp | Обязательность | Описание |
| --- | --- | --- |
| siteName | Обязательный | Имя WebApp, в который устанавливается расширение. |
| location | Обязательный | Регион WebApp. Доступные регионы см. в [документации Azure](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=app-service). |
| skuCapacity | Необязательный | Количество экземпляров в рамках вашего плана. |
| skuName | Необязательный | Ценовой уровень и размер экземпляра плана. Подробности о ценах см. в [документации Azure](https://azure.microsoft.com/en-us/pricing/details/app-service/). |
| webAppAlwaysOn | Необязательный | Если `AlwaysOn` не установлен в `true`, установка OneAgent запускается при старте (при первом запросе к Kudu). |

| Параметр Dynatrace | Обязательность | Описание |
| --- | --- | --- |
| environmentID | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |
| APIToken | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
| APIUrl | Необязательный | URL-адрес сервера для настройки альтернативного коммуникационного эндпоинта, описанный в разделе [Предварительные требования](#prerequisites). |
| SSLMode | Необязательный | Для автоматического принятия всех самоподписанных TLS-сертификатов установите значение `all`. |
| networkZone | Необязательный | Сетевая зона. Укажите нужное значение для экземпляра App Service. Подробнее о [сетевых зонах](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace."). |
| monitoredCLR | Необязательный | Установите `clr` для приложений на .NET или `coreclr` для .NET Core, значение по умолчанию: `both` |

Чтобы проверить статус развёртывания, откройте **Deployment Status**.

После завершения установки перезапустите приложение App Service для перезапуска рабочего процесса приложения. После перезапуска OneAgent автоматически начинает мониторинг приложения.

### Автоматизация установки с помощью скрипта PowerShell

Установку можно автоматизировать с помощью скрипта PowerShell, использующего [Kudu REST API](https://dt-url.net/0h031rk), [REST API site extension OneAgent](#restapi), а также [Azure CLI](https://dt-url.net/4j2318w). Пример реализации доступен в [репозитории Dynatrace на GitHub](https://dt-url.net/9s031v4).

## REST API site extension Dynatrace OneAgent

Site extension Dynatrace OneAgent предоставляет REST API для автоматизации установки, настройки и обновления OneAgent.

Корневой URL-адрес для доступа к REST API: `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, где `<Your-AppService-Subdomain>` необходимо заменить своим значением. Для аутентификации можно использовать учётные данные публикации пользователя или учётные данные на уровне сайта. Подробности см. в разделе [Доступ к сервису Kudu](https://dt-url.net/em4316d).

| Метод | Эндпоинт | Описание | Ответ |
| --- | --- | --- | --- |
| GET | /api/status | Возвращает текущий статус установки OneAgent. Возвращаемое поле `state` может принимать значения: - `NotInstalled` - `Downloading` - `Installing` - `Installed` - `Failed`  Для автоматизации используйте поля **isAgentInstalled** и **isUpgradeAvailable**, чтобы проверить, установлен ли OneAgent и доступно ли обновление. | `{`  `"state": "Installed",`  `"message": "OneAgent installed",`  `"version": "1.157",`  `"isAgentInstalled": true,`  `"isUpgradeAvailable": false,`  `"isFunction": false,`  `"functionAppSettings": null` `}` |
| GET | /api/settings | Возвращает текущие настройки, включая учётные данные Dynatrace. | `{` `"apiUrl": "",` `"apiToken": "<your-api-token>",` `"environmentId": "<your-environment-id>",` `"sslMode": "Default"` `}` |
| PUT | /api/settings | Запускает установку OneAgent с указанными настройками. Настройки сохраняются только при успешном завершении установки.  В теле запроса данные передаются в том же формате, что и в ответе на запрос `GET /dynatrace/api/settings`.  Если в статусе доступно обновление, этот `PUT`-запрос можно использовать для его запуска. **Примечания:** \* Значение `apiUrl` может быть пустым для среды SaaS. \* Для `sslMode`: чтобы проверить HTTPS-соединение, оставьте значение `Default`; если проверка не нужна, установите `AcceptAll`. | Пустой ответ |

## Использование нескольких слотов развёртывания

Поскольку слоты развёртывания Azure App Service рассматриваются как полноценные экземпляры сервиса приложения, необходимо включить site extension для OneAgent на каждом слоте развёртывания, который нужно мониторить с помощью Dynatrace.

Подробности настройки слотов развёртывания см. в [документации Microsoft](https://dt-url.net/uo631ry).

Если для дополнительной настройки параметров OneAgent используются настройки приложения, убедитесь, что дополнительные настройки также применяются к слотам развёртывания.

## Использование встроенной аутентификации и авторизации App Service

При использовании [встроенных возможностей аутентификации и авторизации](https://dt-url.net/m2831x1) App Service (также называемых "Easy Auth") App Service запускает дополнительный экземпляр .NET CLR, из-за чего OneAgent инструментирует модуль Easy Auth вместо экземпляра приложения в качестве ведущего.

В этом случае, если процесс приложения не инструментирован, необходимо установить переменную среды `DT_MONITORED_CLR` в значение, соответствующее среде выполнения приложения: `clr` или `coreclr`.
Эту переменную можно задать в Azure Portal (**Settings** > **Configuration** > **Application Settings**).

## Переопределение конфигурации OneAgent

Для переопределения конфигурации по умолчанию можно использовать следующие параметры.

| Параметр | Описание |
| --- | --- |
| DT\_CONNECTION\_POINT | Список коммуникационных эндпоинтов, разделённых точкой с запятой |
| DT\_MONITORED\_CLR | Переменная для инструментирования конкретного экземпляра CLR .NET/.NET Core |

Добавление параметра `DT_CONNECTION_POINT` в Azure Portal

1. В Azure Portal выберите веб-приложение, которое нужно мониторить.
2. Выберите **Settings** > **Configuration** > **Application Settings**.
3. Нажмите **New application setting**.
4. Введите пару ключ/значение конфигурации в следующем формате.

   * Имя: `DT_CONNECTION_POINT`
   * Значение: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication` (замените `<YOUR_ACTIVEGATE_ADDRESS>` своим значением).

   ![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)

   Подключение DT
5. Нажмите **OK** для сохранения конфигурации.

## Использование Application Insights

OneAgent может быть не в состоянии инструментировать приложение .NET/.NET Core при включённом инструментировании во время выполнения Application Insights. Это происходит потому, что OneAgent и Application Insights используют один и тот же интерфейс для инъекции во время выполнения.

Проверьте конфигурацию Application Insights для Asp.Net: можно [отключить инструментирование во время выполнения](https://dt-url.net/z1a31yy) или [автоинструментирование Asp.Net Core](https://dt-url.net/ikc31s6).

Использование Application Insights в базовом режиме или SDK параллельно с Dynatrace OneAgent допускается, однако это может вызывать другие проблемы или существенно увеличивать накладные расходы на мониторинг приложений, поэтому не рекомендуется.

## Обновление site extension Dynatrace OneAgent

Порядок обновления site extension Dynatrace OneAgent

1. В Azure Portal откройте свой Azure App Service с установленным site extension Dynatrace OneAgent.
2. Если доступно обновление, нажмите **Update**.

При обновлении расширения с версии 1.x до версии 2.x: если на App Service включён **Always On**, обновление OneAgent запускается автоматически или при первом запросе к UI-расширению. Если **Always On** не включён, необходимо перезапустить App Service, чтобы процесс расширения стартовал.

Обновление site extension Dynatrace OneAgent не принудительно обновляет OneAgent. Для обновления OneAgent см. [Dynatrace OneAgent](#update-oa).

### Обновление OneAgent

Site extension Dynatrace OneAgent не обновляет Dynatrace OneAgent автоматически. Порядок обновления Dynatrace OneAgent в Azure App Service

1. В Azure Portal откройте свой Azure App Service с установленным site extension Dynatrace OneAgent.
2. В разделе **Development Tools** выберите **Advanced Tools** и нажмите **Go**. Откроется сайт KUDU.
3. Откройте **Site extensions** > **Installed** > **Dynatrace**.
4. Если доступно обновление, нажмите **Upgrade OneAgent**.

Можно отслеживать ход обновления до его завершения, после чего перезапустить App Service для перезапуска рабочего процесса приложения.

## Автоматизация обновлений OneAgent

Для автоматизации обновления OneAgent site extension Dynatrace OneAgent предоставляет REST API, с помощью которого можно инициировать обновления. Подробности см. в разделе [REST API](#restapi).

## Удаление site extension Dynatrace OneAgent

Удаление site extension Dynatrace OneAgent также удаляет Dynatrace OneAgent.
Если приложение работает в момент удаления, site extension обнаруживает запущенное приложение и, во избежание проблем, не удаляет артефакты Dynatrace. Удаляется только само расширение вместе с конфигурацией, так что Dynatrace OneAgent перестаёт работать при следующем запуске приложения.

## Потребление при мониторинге

Для Azure App Service потребление при мониторинге основано на хост-юнитах. Подробности см. в разделе [Мониторинг приложений и инфраструктуры (хост-юниты)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе хост-юнитов.").

## Устранение неполадок

* [Нет зарегистрированного маршрута для /dynatrace/ при обращении к site extension](https://dt-url.net/44038l8)
* [503 Service Unavailable для Web App и Kudu](https://dt-url.net/o62387e)
* [Приложение Node.js не инструментируется](https://dt-url.net/n7238ds)
* [Site extension переопределяет JAVA\_OPTS](https://dt-url.net/rt438wk)
* [Ошибка установки: файл не найден](https://dt-url.net/wr438gk)

Расположение файлов журналов

* Файлы журналов расширения находятся в папке расширений: `D:\home\SiteExtensions\Dynatrace\`.
* Файлы журналов OneAgent расположены в `D:\home\SiteExtensions\Dynatrace.Agent\x.xxx.xxx.xxxxxxxx-xxxxxx\log`. Может быть несколько подкаталогов `D:\home\SiteExtensions\Dynatrace.Agent\` вследствие обновлений агента.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")