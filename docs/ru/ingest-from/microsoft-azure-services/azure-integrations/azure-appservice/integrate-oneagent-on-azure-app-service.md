---
title: Интеграция OneAgent на Azure App Service для Windows
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service
scraped: 2026-03-05T21:25:31.997001
---

* 9 минут чтения

Azure App Service предоставляет множество вариантов размещения для Windows, Linux и контейнеров с общей инфраструктурой ([тарифный план App Service](https://dt-url.net/f4031wl)) или полностью изолированной и выделенной инфраструктурой ([Azure App Service Environment](https://dt-url.net/u0231c3)).

## Возможности

Интеграция App Service с Dynatrace предоставляет следующие возможности:

* [Интеграция OneAgent для Windows через расширение для простого развёртывания](#install)
* Интеграция OneAgent для Linux и контейнеров
* Автоматическая распределённая трассировка и мониторинг для .NET/.NET Core, Java, Node.js, PHP и IIS
* Расширенный сбор метаданных Azure App Service, таких как SKU или Website-Name
* Сбор метрик на уровне платформы и дополнительная информация о вашем плане App Service и просмотр доступных метрик.") через интеграцию Azure Monitor
* Сбор логов через перенаправление логов

**Ограничения**
Поскольку Azure App Service является полностью управляемой платформой для размещения приложений, они развёртываются в изолированной среде, которая не предоставляет прямого доступа к базовой операционной системе. Интеграция OneAgent для Azure App Service использует подход внедрения только на уровне приложения, что влечёт некоторые отличия от полной установки Full-Stack OneAgent:

* Мониторинг ввода/вывода требует включения интеграции Azure Monitor, которая также предоставляет дополнительную информацию о вашем плане App Service и просмотр доступных метрик.")
* Сбор логов требует включения перенаправления логов
* Автоматические обновления OneAgent необходимо инициировать через [REST API расширения сайта Dynatrace OneAgent](#restapi)
* Настройка группы хостов недоступна

## Установка расширения сайта Dynatrace OneAgent

Только для Windows

Dynatrace предоставляет [расширение сайта](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) для установки OneAgent на Azure App Services в Windows.

Для Azure App Service на Linux или в контейнерах см. Интеграция OneAgent на Azure App Service для Linux и контейнеров.

Расширение сайта — это встроенный механизм расширений, предоставляемый через [Kudu](https://github.com/projectkudu/kudu), который является движком управления развёртыванием Azure App Services.

Расширение сайта Dynatrace OneAgent не включает установщик OneAgent. Вместо этого расширение использует REST API Dynatrace для загрузки установщика из кластера в целевой версии, установленной в разделе Обновления OneAgent.

Существует несколько способов установить расширение сайта Dynatrace OneAgent:

* [Вручную, через портал Azure](#portal)
* [Автоматически, с помощью шаблона ARM](#arm)
* [Автоматизируя установку с помощью пользовательского скрипта PowerShell](#script)

Инструкции см. ниже.

### Предварительные требования

* Создайте [токен PaaS](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях.").
* Определите ваш идентификатор среды.
* При необходимости определите URL сервера.

  URL сервера требуется только в случае использования ActiveGate для конечной точки Dynatrace. URL автоматически генерируется из идентификатора среды.

  + **URL сервера ActiveGate:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)

### Ручная установка через портал Azure

1. В портале Azure перейдите в раздел **App Services** и выберите службу приложений, в которую нужно добавить расширение OneAgent.
2. В левом меню перейдите в **Средства разработки** > **Расширения**.
3. Выберите **Добавить**.
4. Выберите **Выбрать расширение**.
5. Из списка расширений выберите Dynatrace OneAgent.
6. Примите условия лицензии и нажмите **Добавить**. Потребуется некоторое время, пока расширение **Dynatrace OneAgent** не появится в списке.
7. В левом меню перейдите в **Средства разработки** > **Дополнительные инструменты** и выберите **Перейти**. Вы будете перенаправлены на сайт Kudu.

   ![Сайт Kudu](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)
8. Выберите **Расширения сайта**.
9. Нажмите **Запустить** на плитке Dynatrace.
10. На странице **Начать мониторинг экземпляра App Service** введите идентификатор среды, [токен PaaS](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях.") и URL сервера. Подробности см. в разделе [Предварительные требования](#prerequisites).
11. Опционально Вы можете выбрать **Принять все самоподписанные SSL-сертификаты** для автоматического принятия всех самоподписанных TLS-сертификатов.
12. Нажмите **Установить OneAgent**.
13. Для проверки статуса развёртывания перейдите в раздел **Статус развёртывания**.
14. После завершения установки перейдите на вкладку **Расширение сайта** в Kudu и нажмите **Перезапустить сайт**.
15. Перезапустите приложение App Service для перезапуска рабочего процесса приложения.

После перезапуска OneAgent автоматически начнёт мониторинг вашего приложения.

### Автоматическая установка с помощью шаблона ARM

В качестве альтернативы установке через портал Azure вы можете включить расширение сайта Dynatrace в свои шаблоны ARM.

Шаблон ARM

Обратите внимание, что приведённая ниже конфигурация является шаблоном, и некоторые значения необходимо изменить.

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
| siteName | Обязательный | Имя WebApp, в который вы хотите установить расширение. |
| location | Обязательный | Регион вашего WebApp. Доступные регионы см. в [документации Azure](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=app-service). |
| skuCapacity | Опциональный | Количество экземпляров, которые вы можете запустить в своём плане. |
| skuName | Опциональный | Ценовой уровень и размер экземпляра плана. Подробности о ценах см. в [документации Azure](https://azure.microsoft.com/en-us/pricing/details/app-service/). |
| webAppAlwaysOn | Опциональный | Если `AlwaysOn` не установлен в `true`, установка OneAgent инициируется при запуске (при первом запросе к Kudu). |

| Параметр Dynatrace | Обязательность | Описание |
| --- | --- | --- |
| environmentID | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |
| APIToken | Обязательный | Токен PaaS, как описано в разделе [Предварительные требования](#prerequisites). |
| APIUrl | Опциональный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в разделе [Предварительные требования](#prerequisites). |
| SSLMode | Опциональный | Для автоматического принятия всех самоподписанных TLS-сертификатов установите значение `all`. |
| networkZone | Опциональный | Ваша сетевая зона. Укажите желаемое значение для вашего экземпляра App Service. Подробнее см. сетевые зоны. |
| monitoredCLR | Опциональный | Установите значение `clr`, если ваше приложение работает на .NET, или `coreclr`, если на .NET Core. Значение по умолчанию — `both`. |

Для проверки статуса развёртывания перейдите в раздел **Статус развёртывания**.

После завершения установки перезапустите приложение App Service для перезапуска рабочего процесса приложения. После перезапуска OneAgent автоматически начнёт мониторинг вашего приложения.

### Автоматизация установки с помощью скрипта PowerShell

Вы можете автоматизировать установку с помощью скрипта PowerShell, который использует [REST API Kudu](https://dt-url.net/0h031rk), [REST API расширения сайта OneAgent](#restapi), а также [Azure CLI](https://dt-url.net/4j2318w). Пример реализации доступен в [репозитории Dynatrace на GitHub](https://dt-url.net/9s031v4).

## REST API расширения сайта Dynatrace OneAgent

Расширение сайта Dynatrace OneAgent предоставляет REST API для автоматизации установки, настройки и обновления OneAgent.

Корневой URL для доступа к REST API: `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, где необходимо заменить `<Your-AppService-Subdomain>` своим значением. Для аутентификации можно использовать учётные данные для публикации на уровне пользователя или учётные данные на уровне сайта. Подробности см. в разделе [Доступ к сервису Kudu](https://dt-url.net/em4316d).

| Метод | Конечная точка | Описание | Ответ |
| --- | --- | --- | --- |
| GET | /api/status | Возвращает текущий статус установки OneAgent. Возвращаемое поле `state` может принимать значения: - `NotInstalled` - `Downloading` - `Installing` - `Installed` - `Failed`  В целях автоматизации используйте поля **isAgentInstalled** и **isUpgradeAvailable** для проверки, установлен ли OneAgent и доступно ли обновление. | `{`  `"state": "Installed",`  `"message": "OneAgent installed",`  `"version": "1.157",`  `"isAgentInstalled": true,`  `"isUpgradeAvailable": false,`  `"isFunction": false,`  `"functionAppSettings": null` `}` |
| GET | /api/settings | Возвращает текущие настройки, включая учётные данные Dynatrace. | `{` `"apiUrl": "",` `"apiToken": "<your-api-token>",` `"environmentId": "<your-environment-id>",` `"sslMode": "Default"` `}` |
| PUT | /api/settings | Запускает установку OneAgent с заданными настройками. Эти настройки сохраняются только в случае успешного завершения установки.  В теле запроса необходимо отправить данные в том же формате, который возвращает запрос `GET /dynatrace/api/settings`.  Если в запросе статуса доступно обновление, этот запрос `PUT` можно использовать для запуска обновления. **Примечания:** \* Значение `apiUrl` можно оставить пустым для среды Dynatrace. \* Для `sslMode`: если нужно проверять HTTPS-соединение, оставьте значение `Default`. Если проверка не нужна, установите `AcceptAll`. | Пустой ответ |

## Использование нескольких слотов развёртывания

Поскольку слоты развёртывания Azure App Service рассматриваются как полноценные экземпляры службы приложений, необходимо включить расширение сайта для OneAgent в каждом слоте развёртывания, который вы хотите мониторить с помощью Dynatrace.

Подробности о настройке слотов развёртывания см. в [документации Microsoft](https://dt-url.net/uo631ry).

Если вы используете настройки приложения для дополнительной конфигурации отдельных параметров OneAgent, убедитесь, что дополнительные настройки также применяются к слотам развёртывания.

## Использование встроенной аутентификации и авторизации App Service

Если вы используете [встроенные возможности аутентификации и авторизации App Service](https://dt-url.net/m2831x1) (также называемые "Easy Auth"), App Service запускает дополнительный экземпляр .NET CLR, из-за чего OneAgent инструментирует модуль Easy Auth, а не экземпляр вашего приложения, как ведущий.

В этом случае, если процесс вашего приложения не инструментирован, необходимо установить переменную среды `DT_MONITORED_CLR` в значение, соответствующее среде выполнения вашего приложения: `clr` или `coreclr`.
Эту переменную можно задать в портале Azure (**Настройки** > **Конфигурация** > **Настройки приложения**).

## Переопределение конфигурации OneAgent

Для переопределения конфигурации по умолчанию можно использовать следующие параметры.

| Параметр | Описание |
| --- | --- |
| DT\_CONNECTION\_POINT | Список конечных точек связи, разделённых точкой с запятой |
| DT\_MONITORED\_CLR | Переменная для инструментирования конкретного экземпляра .NET/.NET Core CLR |

Как добавить параметр `DT_CONNECTION_POINT` в портале Azure

1. В портале Azure выберите веб-приложение, которое хотите мониторить.
2. Выберите **Настройки** > **Конфигурация** > **Настройки приложения**.
3. Выберите **Новая настройка приложения**.
4. Введите пару ключ/значение конфигурации следующим образом.

   * Имя: `DT_CONNECTION_POINT`
   * Значение: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication` — обязательно замените `<YOUR_ACTIVEGATE_ADDRESS>` своим значением.

   ![Соединение DT](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)
5. Выберите **OK** для сохранения конфигурации.

## Использование Application Insights

OneAgent может не иметь возможности инструментировать ваше приложение .NET/.NET Core, если вы используете Application Insights с включённым инструментированием во время выполнения. Это связано с тем, что OneAgent и Application Insights пытаются использовать один и тот же интерфейс для внедрения во время выполнения.

Пожалуйста, проверьте конфигурацию Application Insights для Asp.Net, где вы можете [отключить инструментирование во время выполнения](https://dt-url.net/z1a31yy) или [автоинструментирование Asp.Net Core](https://dt-url.net/ikc31s6).

Хотя вы всё ещё можете использовать Application Insights в базовом режиме или SDK параллельно с Dynatrace OneAgent, обратите внимание, что это может вызвать другие проблемы или значительные накладные расходы на мониторинг ваших приложений, что не рекомендуется.

## Обновление расширения сайта Dynatrace OneAgent

Для обновления расширения сайта Dynatrace OneAgent

1. В портале Azure перейдите в ваш Azure App Service с расширением сайта Dynatrace OneAgent.
2. Если доступно обновление, выберите **Обновить**.

При обновлении расширения с версии 1.x до версии 2.x, если у вас включён режим **Always On** для вашего App Service, обновление OneAgent инициируется автоматически или при первом обращении к расширению пользовательского интерфейса. Если режим **Always On** не включён, необходимо перезапустить App Service, чтобы процесс расширения запустился.

Обновление расширения сайта Dynatrace OneAgent не принуждает к обновлению OneAgent. Для обновления OneAgent см. раздел [Dynatrace OneAgent](#update-oa).

### Обновление OneAgent

Расширение сайта Dynatrace OneAgent не предоставляет автоматического обновления Dynatrace OneAgent. Для обновления Dynatrace OneAgent на Azure App Service

1. В портале Azure перейдите в ваш Azure App Service с расширением сайта Dynatrace OneAgent.
2. В разделе **Средства разработки** выберите **Дополнительные инструменты** и нажмите **Перейти**. Вы будете перенаправлены на сайт KUDU.
3. Перейдите в **Расширения сайта** > **Установленные** > **Dynatrace**.
4. Если доступно обновление, нажмите **Обновить OneAgent**.

Вы можете отслеживать прогресс до завершения обновления, а затем перезапустить App Service для перезапуска рабочего процесса приложения.

## Автоматизация обновлений OneAgent

Для автоматизации обновления OneAgent расширение сайта Dynatrace OneAgent предоставляет REST API, который можно использовать для инициирования обновлений. Подробности см. в разделе [REST API](#restapi).

## Удаление расширения сайта Dynatrace OneAgent

Удаление расширения сайта Dynatrace OneAgent также удаляет Dynatrace OneAgent.
Если приложение работает в момент удаления, расширение сайта обнаруживает работающее приложение и во избежание проблем не удаляет никакие артефакты Dynatrace. Вместо этого удаляется только расширение сайта вместе с его конфигурацией, поэтому Dynatrace OneAgent больше не будет активен при следующем перезапуске приложения.

## Потребление ресурсов мониторинга

Для Azure App Service потребление ресурсов мониторинга рассчитывается на основе единиц хостов. Подробности см. в разделе Мониторинг приложений и инфраструктуры (единицы хостов).

## Устранение неполадок

* [Маршрут /dynatrace/ не зарегистрирован при доступе к расширению сайта](https://dt-url.net/44038l8)
* [503 Service Unavailable для веб-приложения и Kudu](https://dt-url.net/o62387e)
* [Приложение Node.js не инструментируется](https://dt-url.net/n7238ds)
* [Расширение сайта переопределяет JAVA\_OPTS](https://dt-url.net/rt438wk)
* [Ошибка установки: файл не найден](https://dt-url.net/wr438gk)

Расположение файлов логов

* Файлы логов расширения находятся в папке расширений: `D:\home\SiteExtensions\Dynatrace\`.
* Файлы логов OneAgent расположены в `D:\home\SiteExtensions\Dynatrace.Agent\x.xxx.xxx.xxxxxxxx-xxxxxx\log`. Возможно наличие нескольких подпапок `D:\home\SiteExtensions\Dynatrace.Agent\`, вызванных обновлениями агента.

## Связанные темы

* Настройка Dynatrace на Microsoft Azure
* Матрица поддержки платформ и возможностей OneAgent
