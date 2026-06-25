---
title: Мониторинг Azure Functions на App Service Plan для Windows
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions
scraped: 2026-05-12T11:23:31.901409
---

# Мониторинг Azure Functions на App Service Plan для Windows

# Мониторинг Azure Functions на App Service Plan для Windows

* Практическое руководство
* Чтение: 6 мин
* Опубликовано 16 октября 2018 г.

## Возможности

* Мониторинг полного стека на базе OneAgent
* [Расширение для простого развёртывания OneAgent](#install-dynatrace-oneagent-site-extension-via-azure-portal)
* Поддержка Azure Functions, написанных на .NET (in-process) и размещённых на **App Service Plan для Windows**
* Расширенная поддержка метаданных Azure App Service, таких как режим вычислений, SKU и другие
* Автоматическое обнаружение сервисов для функций на любом языке для Azure Function Runtime v2+
* Автоматическая трассировка и профилирование кода для функций на .NET/.NET Core
* Сквозная трассировка нескольких функций для триггеров на основе HTTP и других инструментированных сервисов и приложений. Другие триггеры, такие как QueueTriggers, требуют пользовательского распространения трассировки.

Dynatrace предоставляет [Azure Site Extension](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) для установки OneAgent в Azure Functions. Azure Site Extensions, это встроенный механизм расширений, предоставляемый через [Kudu](https://github.com/projectkudu/kudu), движок управления развёртыванием Azure App Services.

Site extension Dynatrace OneAgent не включает в себя установщик OneAgent. Вместо этого расширение использует Dynatrace REST API для загрузки установщика из кластера в целевой версии, заданной в разделе [Обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Узнайте, как обновить OneAgent.").

Ограничения

Поскольку Azure Functions являются полностью управляемой платформой хостинга, построенной на основе Azure App Services, функции/приложения развёртываются в изолированной среде (sandbox), которая не предоставляет прямого доступа к базовой операционной системе. Это влечёт ряд ограничений для OneAgent:

* Расширенный мониторинг ввода/вывода требует [интеграции с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка и конфигурация мониторинга Azure в Dynatrace.").
* Dynatrace Log Monitoring не поддерживается для Azure Functions.
* Сетевые зоны не поддерживаются.

## Предварительные требования

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

## Установка site extension Dynatrace OneAgent

Существует два способа установки site extension Dynatrace OneAgent: через Azure Portal или с помощью ARM-шаблона. Инструкции приведены ниже.

### Установка site extension Dynatrace OneAgent через Azure Portal

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

### Установка site extension Dynatrace OneAgent с помощью ARM-шаблона

Как альтернатива основному методу установки через Azure Portal, можно включить site extension Dynatrace в ARM-шаблоны.
Пример конфигурации:

```
{



"apiVersion": "2016-08-01",



"name": "[parameters('resourceName')]",



"type": "Microsoft.Web/sites",



"properties": {



"name": "[parameters('resourceName')]",



"siteConfig": {



"alwaysOn": true,



"appSettings": [



{ "Name": "DT_TENANT", "Value": "<Environment-ID>" },



{ "Name": "DT_API_TOKEN", "Value": "<PaaS-Token>" },



{ "Name": "DT_API_URL", "Value": "<Server-Url>" },



{ "Name": "DT_SSL_MODE", "Value": "default" }



]



},



"serverFarmId": "[resourceId('Microsoft.Web/serverfarms', parameters('resourceName'))]"



},



"dependsOn": [



"[concat('Microsoft.Web/serverfarms/', parameters('resourceName'))]"



],



"location": "[parameters('location')]",



"resources": [



{



"apiVersion": "2016-08-01",



"name": "Dynatrace",



"type": "siteextensions",



"dependsOn": [



"[resourceId('Microsoft.Web/sites', parameters('resourceName'))]"



],



"properties": { }



}



]



}
```

| Параметр | Обязательность | Описание |
| --- | --- | --- |
| DT\_TENANT | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |
| DT\_API\_TOKEN | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
| DT\_API\_URL | Необязательный | URL-адрес сервера для настройки альтернативного коммуникационного эндпоинта, описанного в разделе [Предварительные требования](#prerequisites). |
| DT\_SSL\_MODE | Необязательный | Для автоматического принятия всех самоподписанных TLS-сертификатов установите значение `all`. |

Если `AlwaysOn` не установлен в `true`, установка OneAgent запускается при старте или при первом запросе к Kudu.

Чтобы проверить статус развёртывания, откройте **Deployment Status**.

После завершения установки перейдите в Azure Portal и перезапустите приложение App Function для перезапуска рабочего процесса приложения. Сразу после перезапуска OneAgent начнёт мониторинг приложения.

## Автоматизация установки и обновления site extension Dynatrace OneAgent с помощью Kudu REST API

После установки site extension Dynatrace OneAgent можно использовать **Kudu REST API** для автоматизации установки и обновления. Подробности см. на [странице настройки автоматизации на GitHub](https://github.com/Dynatrace/snippets/tree/master/technologies/azure/automate-appservice-siteextension-setup).

Корневой URL-адрес для доступа к REST API: `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, где `<Your-AppService-Subdomain>` необходимо заменить своим значением. Для аутентификации можно использовать учётные данные публикации пользователя или учётные данные на уровне сайта. Подробности см. в разделе [Доступ к сервису Kudu](https://github.com/projectkudu/kudu/wiki/Accessing-the-kudu-service).

| Метод | Эндпоинт | Описание | Ответ |
| --- | --- | --- | --- |
| GET | `/api/status` | Возвращает текущий статус установки OneAgent. Возвращаемое поле "state" может принимать значения:  * `NotInstalled` * `Downloading` * `Installing` * `Installed` * `Failed`  Для автоматизации используйте **isAgentInstalled** и **isUpgradeAvailable**, чтобы проверить, установлен ли OneAgent и доступно ли обновление. | ```  {  "state": "Installed",  "message": "OneAgent installed",  "version": "1.157",  "isAgentInstalled": true,  "isUpgradeAvailable": false,  "isFunction": false,  "functionAppSettings": null  } ``` |
| GET | `/api/settings` | Возвращает текущие настройки, включая учётные данные Dynatrace. Значение `apiUrl` может быть пустым для среды SaaS. | ```  {  "apiUrl": "",  "apiToken": "<your-api-token>",  "environmentId": "<your-environment-id>",  "sslMode": "Default"  } ``` |
| PUT | `/api/settings` | Запускает установку OneAgent с указанными настройками. Настройки сохраняются только при успешном завершении установки. В теле запроса данные передаются в формате, полученном в ответ на запрос `GET /dynatrace/api/settings`. Если в статусе доступно обновление, этот `PUT`-запрос можно использовать для его запуска. | Пустой ответ |

## Переопределение конфигурации OneAgent

Для переопределения конфигурации по умолчанию можно использовать следующие параметры.

| Параметр | Описание |
| --- | --- |
| DT\_CONNECTION\_POINT | Список коммуникационных эндпоинтов, разделённых точкой с запятой |

Добавление параметра DT\_CONNECTION\_POINT в Azure Portal

Порядок добавления параметра DT\_CONNECTION\_POINT

1. В Azure Portal выберите веб-функцию, которую нужно мониторить.
2. Выберите **Settings** > **Configuration** > **Application Settings**.
3. Нажмите **New application setting**.
4. Введите следующую пару ключ/значение:

   * Имя: `DT_CONNECTION_POINT`
   * Значение: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication` (замените `<YOUR_ACTIVEGATE_ADDRESS>` своим значением).

   ![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)

   Подключение DT
5. Нажмите **OK** для сохранения конфигурации.

## Обновление OneAgent

Dynatrace не предоставляет автоматические обновления OneAgent для Azure Functions. Для обновления OneAgent в Azure Functions перейдите в Azure Portal, откройте site extension и, если доступно обновление, нажмите **Update**. Можно отслеживать ход обновления до его завершения.
Затем перезапустите Azure Functions для перезапуска рабочего процесса приложения.

Расширение предоставляет собственный REST API для автоматизации обновлений OneAgent. Подробности см. в разделе [REST API](#restapi).

### Обновление site extension

Для обновления site extension в Azure App Service перейдите в Azure Portal, откройте site extension и, если доступно обновление, нажмите **Update**.

Обновление site extension не принудительно обновляет OneAgent.

При обновлении расширения с версии 1.x до версии 2.x: если на App Service включён **Always On**, обновление OneAgent запускается автоматически или при первом запросе к UI-расширению. Если **Always On** не включён, необходимо перезапустить App Service, чтобы процесс расширения стартовал.

## Удаление OneAgent

Удаление расширения также удаляет OneAgent.

Если приложение работает в момент удаления, расширение обнаруживает запущенное приложение и, во избежание проблем, не удаляет артефакты Dynatrace. Удаляется только само расширение вместе с конфигурацией, так что OneAgent перестаёт работать при следующем запуске приложения.

## Потребление при мониторинге

Подробности о потреблении при мониторинге Azure Functions см. в разделе [Бессерверный мониторинг](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление при бессерверном мониторинге.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")
* [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.")