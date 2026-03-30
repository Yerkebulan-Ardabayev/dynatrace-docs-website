---
title: Мониторинг Azure Functions на App Service Plan для Windows
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions
scraped: 2026-03-05T21:25:48.203441
---

# Мониторинг Azure Functions на плане App Service для Windows


* Latest Dynatrace
* How-to guide
* 6 мин. чтения

## Возможности

* Полностековый мониторинг на базе OneAgent
* [Расширение для простого развёртывания OneAgent](#install-dynatrace-oneagent-site-extension-via-azure-portal)
* Поддержка Azure Functions, написанных на .NET (in-process) и размещённых на **плане App Service для Windows**
* Расширенная поддержка метаданных Azure App Service, таких как режим вычислений, SKU и другие
* Автоматическое обнаружение сервисов для функций, написанных на любом языке для Azure Function Runtime v2+
* Автоматическая трассировка и профилирование кода для функций на основе .NET/.NET Core
* Сквозная трассировка между несколькими функциями для триггеров на основе HTTP и других инструментированных сервисов и приложений. Другие триггеры, такие как QueueTriggers, требуют пользовательского распространения трассировки.

Dynatrace предоставляет [расширение Azure Site Extension](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) для установки OneAgent на Azure Functions. Расширения Azure Site Extensions — это нативный механизм расширения, предоставляемый через [Kudu](https://github.com/projectkudu/kudu), который является движком управления развёртыванием Azure App Services.

Расширение Dynatrace OneAgent site extension не включает установщик OneAgent. Вместо этого расширение использует Dynatrace REST API для загрузки установщика из кластера в целевой версии, как указано в обновлениях OneAgent.

Ограничения

Поскольку Azure Functions — это полностью управляемая платформа размещения, построенная на основе Azure App Services, функции/приложения развёртываются в изолированной среде, которая не позволяет прямой доступ к базовой операционной системе. Это приводит к некоторым ограничениям для OneAgent:

* Расширенный мониторинг ввода-вывода требует интеграции Azure Monitor.
* Мониторинг логов Dynatrace не поддерживается для Azure Functions.
* Сетевые зоны не поддерживаются.

## Предварительные требования

* Создайте [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Определите ваш идентификатор среды.
* Определите URL вашего сервера, если это необходимо.

  URL сервера требуется только если вы используете ActiveGate для конечной точки Dynatrace SaaS. URL автоматически генерируется из идентификатора среды.

  + **URL сервера ActiveGate:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)

## Установка расширения Dynatrace OneAgent site extension

Существует два способа установки расширения Dynatrace OneAgent site extension: через портал Azure или с помощью ARM-шаблона. Следуйте инструкциям ниже.

### Установка расширения Dynatrace OneAgent site extension через портал Azure

1. На портале Azure перейдите в **App Services** и выберите службу приложений, в которую вы хотите добавить расширение OneAgent.
2. В левом меню перейдите в **Development Tools** > **Extensions**.
3. Выберите **Add**.
4. Выберите **Choose an Extension**.
5. Из списка расширений выберите Dynatrace OneAgent.
6. Примите условия лицензии и выберите **Add**. Через некоторое время вы увидите расширение **Dynatrace OneAgent** в списке.
7. В левом меню перейдите в **Development Tools** > **Advanced Tools** и выберите **Go**. Это перенаправит вас на сайт Kudu.

   ![Сайт Kudu](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)
8. Выберите **Site extensions**.
9. Выберите **Launch** на плитке Dynatrace.
10. На странице **Start monitoring your App Service instance** введите ваш идентификатор среды, [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.") и URL сервера. Подробнее см. раздел [Предварительные требования](#prerequisites).
11. Необязательно. Вы можете выбрать **Accept all self-signed SSL certificates** для автоматического принятия всех самоподписанных TLS-сертификатов.
12. Выберите **Install OneAgent**.
13. Для проверки статуса развёртывания перейдите в **Deployment Status**.
14. После завершения установки перейдите на вкладку **Site extension** в Kudu и выберите **Restart Site**.
15. Перезапустите приложение App Service для перезагрузки рабочего процесса приложения.

После перезапуска OneAgent автоматически начнёт мониторинг вашего приложения.

### Установка расширения Dynatrace OneAgent site extension с помощью ARM-шаблона

В качестве альтернативы основному методу установки через портал Azure вы можете включить расширение Dynatrace site extension в ваши ARM-шаблоны.
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

| Параметр | Требование | Описание |
| --- | --- | --- |
| DT\_TENANT | Обязательный | Идентификатор среды, как описано в [Предварительных требованиях](#prerequisites). |
| DT\_API\_TOKEN | Обязательный | PaaS-токен, как описано в [Предварительных требованиях](#prerequisites). |
| DT\_API\_URL | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в [Предварительных требованиях](#prerequisites). |
| DT\_SSL\_MODE | Необязательный | Для автоматического принятия всех самоподписанных TLS-сертификатов установите значение `all`. |

Если `AlwaysOn` не установлен в `true`, установка OneAgent запускается при запуске/первом запросе к Kudu.

Для проверки статуса развёртывания перейдите в **Deployment Status**.

После завершения установки перейдите на портал Azure и перезапустите приложение App Function для перезагрузки рабочего процесса приложения. Сразу после перезапуска OneAgent начнёт мониторинг вашего приложения.

## Автоматизация установки и обновления расширения Dynatrace OneAgent site extension с помощью Kudu REST API

После установки расширения Dynatrace OneAgent site extension вы можете использовать **Kudu REST API** для автоматизации установки и обновления расширения Dynatrace OneAgent site extension. Подробнее см. [страницу настройки автоматизации на GitHub](https://github.com/Dynatrace/snippets/tree/master/technologies/azure/automate-appservice-siteextension-setup).

Корневой URL для доступа к REST API: `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, где необходимо заменить `<Your-AppService-Subdomain>` вашим собственным значением. Для аутентификации вы можете использовать учётные данные публикации пользователя или учётные данные уровня сайта. Подробнее см. [Доступ к сервису Kudu](https://github.com/projectkudu/kudu/wiki/Accessing-the-kudu-service).

## Переопределение конфигурации OneAgent

Для переопределения конфигурации по умолчанию вы можете использовать следующие параметры.

| Параметр | Описание |
| --- | --- |
| DT\_CONNECTION\_POINT | Список конечных точек связи, разделённых точкой с запятой |

Как добавить параметр DT\_CONNECTION\_POINT на портале Azure

Чтобы добавить параметр DT\_CONNECTION\_POINT

1. На портале Azure выберите веб-функцию, которую хотите мониторить.
2. Выберите **Settings** > **Configuration** > **Application Settings**.
3. Выберите **New application setting**.
4. Введите следующую пару ключ/значение:

   * Name: `DT_CONNECTION_POINT`
   * Value: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication`, убедившись, что вы заменили `<YOUR_ACTIVEGATE_ADDRESS>` вашим собственным значением.

   ![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)
5. Выберите **OK** для сохранения конфигурации.

## Обновление OneAgent

Dynatrace не предоставляет автоматические обновления OneAgent на Azure Functions. Для обновления OneAgent на Azure Functions перейдите на портал Azure, откройте ваше расширение site extension и, если обновление доступно, выберите **Update**. Вы можете отслеживать прогресс до завершения обновления.
Затем перезапустите Azure Functions для перезагрузки рабочего процесса приложения.

Расширение предоставляет собственный REST API для автоматизации обновлений OneAgent. Подробнее см. [REST API](#restapi).

### Обновление расширения site extension

Для обновления расширения site extension на Azure App Service перейдите на портал Azure, откройте ваше расширение site extension и, если обновление доступно, выберите **Update**.

Обновление расширения site extension не принуждает к обновлению OneAgent.

При обновлении расширения с версии 1.x до версии 2.x, если у вас выбран параметр **Always On** для App Service, обновление OneAgent запускается автоматически или при первом запросе к расширению UI. Если **Always On** не выбран, вам необходимо перезапустить App Service, чтобы процесс расширения запустился.

## Удаление OneAgent

Удаление расширения также удаляет OneAgent.

Если приложение работает в момент удаления, расширение распознаёт работающее приложение и не удаляет артефакты Dynatrace, чтобы предотвратить проблемы с приложением. Вместо этого удаляется только расширение, включая конфигурацию, так что при следующем перезапуске приложения OneAgent больше не будет активен.

## Потребление мониторинга

Подробнее о потреблении мониторинга для Azure Functions см. Бессерверный мониторинг.

## Связанные темы

* Настройка Dynatrace на Microsoft Azure
* Матрица поддержки платформ и возможностей OneAgent
* Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption