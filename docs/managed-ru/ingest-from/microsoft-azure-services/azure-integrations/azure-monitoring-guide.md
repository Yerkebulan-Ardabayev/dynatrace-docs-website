---
title: Мониторинг сервисов Azure с метриками Azure Monitor
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide
scraped: 2026-05-12T11:09:41.501338
---

# Мониторинг сервисов Azure с метриками Azure Monitor

# Мониторинг сервисов Azure с метриками Azure Monitor

* Практическое руководство
* Чтение: 13 мин
* Обновлено 28 января 2026 г.

Следуйте этому руководству, чтобы начать удалённую передачу данных из Azure Monitor.

Это руководство посвящено мониторингу инфраструктуры сервисов Azure, а именно мониторингу облачных сервисов Azure через Azure Monitor. См. раздел [Что дальше](#next) для Full-Stack и Log Monitoring ваших сервисов Azure.

Также можно настроить среду Dynatrace SaaS через [Azure Marketplace](/managed/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Настройте и сконфигурируйте среду Dynatrace SaaS через Azure Marketplace.").

После первоначальной настройки мониторинга можно добавлять, удалять или изменять параметры мониторинга сервисов через веб-интерфейс Dynatrace или, при масштабировании, через Dynatrace API.

Подробности о собираемых измерениях

Чтобы узнать о метриках, собираемых для каждого из сервисов Azure, см.:

* [Облачные сервисы Azure, включённые по умолчанию, и их метрики](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "Список классических метрик, собираемых Dynatrace по умолчанию для мониторинга Azure.")
* [Облачные сервисы Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.")

Мониторинг инфраструктуры сервисов Azure предоставляет метрики из Azure Monitor и данные инфраструктуры, доступные через публичный Azure API. Данные собираются с интервалом в пять минут.

## Стоимость мониторинга

Факторы, влияющие на стоимость мониторинга Azure с Dynatrace через Azure Monitor:

* Каждый сервис, отслеживаемый Dynatrace через Azure Monitor, а также обработка и анализ логов приводят к потреблению [Davis data units](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).").
* Microsoft может взимать дополнительную плату за запросы метрик Azure Monitor при превышении 1 миллиона вызовов API в месяц. Подробнее об этих дополнительных расходах см. в [документации Microsoft](https://dt-url.net/ie03w85).
* Подробнее о стоимости приёма метрик см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

## Предварительные требования для мониторинга

Для настройки мониторинга Azure необходимо выполнить три предварительных условия:

Права администратора Dynatrace

Подробнее об управлении и настройке прав доступа см. в разделе [Группы пользователей, права и политики](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Узнайте о поддерживаемых разрешениях и политиках, о том, как назначать их группам и управлять пользователями и группами.").

ActiveGate с поддержкой мониторинга Azure

Для мониторинга сервисов Azure Dynatrace подключается к Azure Monitor API и запрашивает его каждые 5 минут. Как минимум один ActiveGate должен иметь возможность подключиться к Azure Monitor для выполнения задач мониторинга.

Чтобы проверить наличие подходящего ActiveGate

1. Откройте **Deployment Status** > **ActiveGates**.
2. Задайте фильтр `With modules: Azure`.

   * Если список пуст, нужно добавить хотя бы один ActiveGate с включённым модулем облачного мониторинга.
   * Если список не пуст, можно приступать к активации мониторинга Azure.

Чтобы добавить ActiveGate с поддержкой облачного мониторинга, следуйте [руководству по установке ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate") и вернитесь к этому руководству по завершении.

#### Разрешение доступа ActiveGate к URL-адресам Azure

Интеграция обращается к следующим эндпоинтам Azure API, поэтому они должны быть доступны из ActiveGate:

```
https://management.azure.com/
```

```
https://login.microsoftonline.com/
```

```
https://management.core.windows.net/
```

Прокси

Наиболее частая причина проблем с сертификатами при использовании TLS-прокси с перехватом: отсутствие CA-сертификата прокси в хранилище доверенных сертификатов ActiveGate.
Если проблемы с прокси не устранены, см.:

* [Прокси для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Узнайте, как настроить свойства ActiveGate для установки прокси.")
* [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate.")
* [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.")

"Communication error."

Убедитесь, что URL-адреса внесены в список разрешённых. В противном случае возможны ошибки связи или превышение времени ожидания.

Роли и права доступа Azure

Для выполнения этих шагов необходимы привилегии администратора Azure.

Мониторинг Azure выполняется удалённо через Azure Monitor API, созданные и предоставленные Microsoft. Dynatrace должен иметь доступ к этим API, поэтому нужно настроить Azure соответствующим образом. Для этого потребуется:

* Достаточные права для регистрации приложения в тенанте Azure AD и назначения приложению роли в подписке Azure.
* Azure [service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) для доступа к Azure API.

Для мониторинга сервисов Dynatrace необходимы как минимум права на чтение. Шаги ниже описывают добавление прав на чтение для service principal и относятся к стандартному подходу с доступом к одному тенанту. Перед этим рекомендуется ознакомиться с рекомендациями по [настройке Azure service principal для предотвращения ограничений Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure#service-principal "Руководство по ограничению вызовов Azure API во избежание лимитов троттлинга").

Интеграция Dynatrace с Azure поддерживает **Azure Lighthouse**, что позволяет Dynatrace получать доступ к Azure в режиме нескольких тенантов.

1. Откройте терминал [Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
2. Выполните следующую команду для отображения всех подписок, чтобы выбрать нужную для добавления прав.

   ```
   az account list --output table
   ```
3. Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.

   ```
   az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID1> /subscriptions/<YourSubscriptionID2> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
   ```

   Обязательно замените заполнители (`<...>`) своими значениями:

   * `<YourServicePrincipalName>`: имя service principal, который будет создан для доступа Dynatrace к Azure.
   * `<YourSubscriptionID1>`, `<YourSubscriptionID2>`: имена подписок из предыдущего шага, к которым Dynatrace должен иметь доступ.
4. Выполните отредактированную команду.
5. Скопируйте учётные данные, выведенные командой, и сохраните их для дальнейшего использования.

#### Другие варианты получения необходимых прав

Создание пользовательской роли через Azure CLI 2.0

Ещё один способ получить права на чтение: создать пользовательскую роль для Dynatrace с заранее заданным набором прав для детального управления доступом.

1. Создайте пользовательскую роль, следуя [руководству Microsoft](https://docs.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-cli#create-a-custom-role). В качестве основы для прав доступа можно использовать следующий JSON-шаблон:

   ```
   {



   "properties": {



   "roleName": "dynatrace-monitoring-role",



   "description": "",



   "assignableScopes": [],



   "permissions": [



   {



   "actions": [



   "Microsoft.AVS/*/read",



   "Microsoft.Aadiam/*/read",



   "Microsoft.AnalysisServices/*/read",



   "Microsoft.ApiManagement/*/read",



   "Microsoft.App/*/read",



   "Microsoft.AppConfiguration/*/read",



   "Microsoft.AppPlatform/*/read",



   "Microsoft.Automation/*/read",



   "Microsoft.Batch/*/read",



   "Microsoft.Blockchain/*/read",



   "Microsoft.BotService/*/read",



   "Microsoft.Cache/*/read",



   "Microsoft.Cdn/*/read",



   "Microsoft.ClassicCompute/*/read",



   "Microsoft.ClassicStorage/*/read",



   "Microsoft.CognitiveServices/*/read",



   "Microsoft.Compute/*/read",



   "Microsoft.ContainerInstance/*/read",



   "Microsoft.ContainerRegistry/*/read",



   "Microsoft.ContainerService/*/read",



   "Microsoft.CustomProviders/*/read",



   "Microsoft.DBforMariaDB/*/read",



   "Microsoft.DBforMySQL/*/read",



   "Microsoft.DBforPostgreSQL/*/read",



   "Microsoft.DataBoxEdge/*/read",



   "Microsoft.DataCollaboration/*/read",



   "Microsoft.DataFactory/*/read",



   "Microsoft.DataLakeAnalytics/*/read",



   "Microsoft.DataLakeStore/*/read",



   "Microsoft.DataShare/*/read",



   "Microsoft.Devices/*/read",



   "Microsoft.DigitalTwins/*/read",



   "Microsoft.DocumentDB/*/read",



   "Microsoft.EnterpriseKnowledgeGraph/*/read",



   "Microsoft.EventGrid/*/read",



   "Microsoft.EventHub/*/read",



   "Microsoft.HDInsight/*/read",



   "Microsoft.HealthcareApis/*/read",



   "Microsoft.Insights/*/read",



   "Microsoft.IoTCentral/*/read",



   "Microsoft.KeyVault/*/read",



   "Microsoft.Kusto/*/read",



   "Microsoft.Logic/*/read",



   "Microsoft.MachineLearningServices/*/read",



   "Microsoft.Management/*/read/",



   "Microsoft.Maps/*/read",



   "Microsoft.Media/*/read",



   "Microsoft.MixedReality/*/read",



   "Microsoft.NetApp/*/read",



   "Microsoft.Network/*/read",



   "Microsoft.NotificationHubs/*/read",



   "Microsoft.OperationalInsights/*/read",



   "Microsoft.Peering/*/read",



   "Microsoft.PowerBIDedicated/*/read",



   "Microsoft.ProjectBabylon/*/read",



   "Microsoft.Purview/*/read",



   "Microsoft.RecoveryServices/*/read",



   "Microsoft.Relay/*/read",



   "Microsoft.ResourceGraph/*/read/",



   "Microsoft.Search/*/read",



   "Microsoft.SecurityDetonation/*/read",



   "Microsoft.ServiceBus/*/read",



   "Microsoft.ServiceFabricMesh/*/read",



   "Microsoft.SignalRService/*/read",



   "Microsoft.Sql/*/read",



   "Microsoft.StorageCache/*/read",



   "Microsoft.StreamAnalytics/*/read",



   "Microsoft.Synapse/*/read",



   "Microsoft.TimeSeriesInsights/*/read",



   "Microsoft.VMwareCloudSimple/*/read",



   "Microsoft.storagesync/*/read",



   "Microsoft.web/*/read"



   ],



   "notActions": [],



   "dataActions": [],



   "notDataActions": []



   }



   ]



   }



   }
   ```
2. Откройте терминал [Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
3. Выполните следующую команду для отображения всех подписок, чтобы выбрать нужную для добавления прав.

   ```
   az account list --output table
   ```
4. Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.

   ```
   az ad sp create-for-rbac --name <YourServicePrincipalName> --role <YourCustomRole> --scopes /subscriptions/<YourSubscriptionID1> /subscriptions/<YourSubscriptionID2> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
   ```

   Замените заполнители (`<...>`) своими значениями:

   * `<YourServicePrincipalName>`: имя service principal, который будет создан для доступа Dynatrace к Azure.
   * `<YourCustomRole>`: имя роли, созданной для Dynatrace.
   * `<YourSubscriptionID1>`, `<YourSubscriptionID2>`: имена подписок из предыдущего шага (подписки, к которым Dynatrace должен иметь доступ).
5. Выполните отредактированную команду.
6. Скопируйте учётные данные, выведенные командой, и сохраните их для дальнейшего использования.

Создание service principal через Azure Portal

Чтобы создать service principal в Azure Portal, нужно зарегистрировать приложение в Microsoft Entra ID и предоставить права доступа для service principal.

Регистрация приложения

1. Откройте Azure Management Portal и выберите **Microsoft Entra ID**.
2. Скопируйте значение **Tenant ID** и сохраните его как `Tenant ID` для дальнейшего использования. Оно необходимо для [настройки подключения Dynatrace к учётной записи Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide#azureconfig-connect "Настройка и конфигурирование мониторинга Azure в Dynatrace.").
3. В панели навигации выбранного Active Directory выберите **App registrations**.
4. В верхней части раздела App registrations выберите **New registration** и введите имя приложения.
5. Оставьте остальные параметры по умолчанию и нажмите **Register**.
6. Скопируйте значение **Application (client) ID** и сохраните его как `Client ID` для дальнейшего использования.
7. Выберите **Certificates & secrets** > **New client secret** для создания нового ключа безопасности.
8. Введите описание ключа, выберите срок его действия и нажмите **Add** для сохранения.
9. Скопируйте значение поля **Value** и сохраните его как `Secret Key` для дальнейшего использования.

   После выхода из раздела **Key** значение ключа восстановить невозможно.

Предоставление прав доступа для service principal

1. В Azure Portal выберите **All services** > **General** > **Subscriptions**.
2. На странице **Subscriptions** выберите нужную подписку, затем выберите **Access control (IAM)**.

Настройка при назначении прав на чтение

Настройка при создании пользовательской роли

1. Выберите **Add role assignment** и укажите **Reader**.
2. Нажмите **Next**.
3. В разделе **Members** введите следующие данные:

   * В поле **Assign access to** выберите `User`, `group` или `service principal`.
   * В поле **Members** нажмите **Select members** и выберите service principal из списка слева.
4. Нажмите **Next**, затем **Review + assign**.

1. В разделе **Add custom role** нажмите **Add**.
2. В разделе **Basics** введите имя роли и выберите **Start from scratch**.
3. В разделе **JSON** в качестве основы для прав доступа можно использовать шаблон ниже.

   ```
   {



   "properties": {



   "roleName": "dynatrace-monitoring-role",



   "description": "",



   "assignableScopes": [],



   "permissions": [



   {



   "actions": [



   "Microsoft.Aadiam/*/read",



   "Microsoft.AnalysisServices/*/read",



   "Microsoft.ApiManagement/*/read",



   "Microsoft.Automation/*/read",



   "Microsoft.Batch/*/read",



   "Microsoft.BotService/*/read",



   "Microsoft.Cache/*/read",



   "Microsoft.Cdn/*/read",



   "Microsoft.ClassicCompute/*/read",



   "Microsoft.ClassicStorage/*/read",



   "Microsoft.CognitiveServices/*/read",



   "Microsoft.Compute/*/read",



   "Microsoft.ContainerInstance/*/read",



   "Microsoft.ContainerRegistry/*/read",



   "Microsoft.ContainerService/*/read",



   "Microsoft.DataFactory/*/read",



   "Microsoft.DataLakeAnalytics/*/read",



   "Microsoft.DataLakeStore/*/read",



   "Microsoft.DBforMySQL/*/read",



   "Microsoft.DBforPostgreSQL/*/read",



   "Microsoft.Devices/*/read",



   "Microsoft.DocumentDB/*/read",



   "Microsoft.EventGrid/*/read",



   "Microsoft.EventHub/*/read",



   "Microsoft.HDInsight/*/read",



   "Microsoft.Insights/*/read",



   "Microsoft.KeyVault/*/read",



   "Microsoft.Kusto/*/read",



   "Microsoft.Logic/*/read",



   "Microsoft.MachineLearningServices/*/read",



   "Microsoft.Maps/*/read",



   "Microsoft.Media/*/read",



   "Microsoft.NetApp/*/read",



   "Microsoft.Network/*/read",



   "Microsoft.NotificationHubs/*/read",



   "Microsoft.OperationalInsights/*/read",



   "Microsoft.PowerBIDedicated/*/read",



   "Microsoft.RecoveryServices/*/read",



   "Microsoft.Relay/*/read",



   "Microsoft.Search/*/read",



   "Microsoft.ServiceBus/*/read",



   "Microsoft.SignalRService/*/read",



   "Microsoft.Sql/*/read",



   "Microsoft.StreamAnalytics/*/read",



   "microsoft.storagesync/*/read",



   "Microsoft.TimeSeriesInsights/*/read",



   "microsoft.web/*/read",



   "Microsoft.DBforMariaDB/*/read",



   "Microsoft.DataBoxEdge/*/read",



   "Microsoft.IoTCentral/*/read",



   "Microsoft.Blockchain/*/read",



   "Microsoft.MixedReality/*/read",



   "Microsoft.EnterpriseKnowledgeGraph/*/read",



   "Microsoft.AppConfiguration/*/read",



   "Microsoft.DataShare/*/read",



   "Microsoft.ServiceFabricMesh/*/read",



   "Microsoft.VMwareCloudSimple/*/read",



   "Microsoft.Peering/*/read",



   "Microsoft.HealthcareApis/*/read",



   "Microsoft.CustomProviders/*/read",



   "Microsoft.StorageCache/*/read",



   "Microsoft.AppPlatform/*/read",



   "Microsoft.ProjectBabylon/*/read",



   "Microsoft.Synapse/*/read",



   "Microsoft.DigitalTwins/*/read",



   "Microsoft.AVS/*/read",



   "Microsoft.DataCollaboration/*/read",



   "Microsoft.SecurityDetonation/*/read",



   "Microsoft.Purview/*/read",



   "Microsoft.Management/*/read/",



   "Microsoft.ResourceGraph/*/read/"



   ],



   "notActions": [],



   "dataActions": [],



   "notDataActions": []



   }



   ]



   }



   }
   ```
4. Нажмите **Review + create** для проверки конфигурации, затем **Create**.

Создание service principal через PowerShell

Чтобы создать новый service principal и предоставить ему права доступа в PowerShell, см. [Create an Azure service principal with Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/create-azure-service-principal-azureps?view=azps-7.5.0&viewFallbackFrom=azps-2.0.0).

Если нужно создать пользовательскую [роль](https://docs.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-powershell), см. [Создание пользовательской роли через Azure CLI 2.0](#cli).

## Создание конфигурации мониторинга

Можно создавать и активировать несколько подключений мониторинга, а также управлять ими. Каждое подключение определяется учётными данными и/или токенами доступа, необходимыми Dynatrace для получения данных, а также фактическим охватом мониторинга.

Почему конфигурация выполняется для каждого подключения отдельно?

Поддержка нескольких подключений и конфигураций позволяет вести мониторинг даже очень сложных сред. При таком подходе не нужно настраивать всё сразу: можно постепенно добавлять конфигурации мониторинга к существующей настройке. Такая архитектура также упрощает реакцию на динамические изменения в отслеживаемой среде без необходимости перенастройки незатронутых элементов.

Добавление нового подключения Azure

Если выполнены все предыдущие шаги, можно приступать к настройке мониторинга Azure.

Чтобы добавить новое подключение Azure

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**. На странице отображаются уже настроенные подключения Azure.

   Если ActiveGate, необходимый для мониторинга Azure, не был предоставлен (см. [Предварительные требования](#capable-activegate)), соответствующее сообщение будет выведено на экране и продолжить настройку не получится.

   Изменение или удаление существующих подключений

   Ранее настроенные подключения можно изменить в любое время.

   1. Откройте **Settings** > **Cloud and virtualization** > **Azure**. На странице отображаются существующие подключения.
   2. Внесите необходимые изменения.

      * Чтобы изменить существующее подключение или отслеживаемые в нём сервисы, выберите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в этой строке.
      * Чтобы удалить существующее подключение, выберите **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") в этой строке.
2. Выберите **Connect new instance** и заполните поля конфигурации.

   * **Connection ID**: введите описательное имя для подключения.
   * **Client ID** и **Tenant ID**: введите значения, полученные при создании Azure service principal.

     Если Azure service principal был создан в PowerShell, укажите в поле **Client ID** значение `ApplicationId`.
   * **Secret Key**: получен при создании Azure service principal.

     Ограничение захвата данных

     Можно ограничить данные, получаемые из Azure Monitor, задав фильтр по тегам для определённых ресурсов.

     Можно выбрать отслеживаемые ресурсы на основе существующих тегов Azure, которые Dynatrace автоматически импортирует из экземпляров сервисов.
     Мониторинг ресурсов на основе тегов

     1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
     2. На странице обзора Azure выберите значок **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для нужного экземпляра Azure.
     3. Установите для параметра **Resources to be monitored** значение **Monitor resources selected by tags**.
     4. Введите пары ключ/значение для определения ресурсов, которые нужно исключить из мониторинга или включить в него.
        Можно ввести несколько пар ключ/значение: каждый раз при вводе пары появляется новая пустая строка для редактирования.
     5. Нажмите **Save** для сохранения конфигурации.

        Чтобы автоматически импортировать теги Azure в Dynatrace, включите **Capture Azure tags automatically**.

     Автоматический импорт тегов

     При необходимости автоматический импорт тегов можно отключить. При включении импортируются теги ресурсов, но теги групп ресурсов не импортируются.
3. Нажмите **Connect** для добавления информации о подключении в список подключений Azure.

Мониторинг ресурсов на основе тегов

Для тегов `Include` или `Exclude` действует ограничение в 20 записей.

Можно выбрать отслеживаемые ресурсы на основе существующих тегов Azure, которые Dynatrace автоматически импортирует из экземпляров сервисов.
Мониторинг ресурсов на основе тегов

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure выберите значок **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для нужного экземпляра Azure.
3. Установите для параметра **Resources to be monitored** значение **Monitor resources selected by tags**.
4. Введите пары ключ/значение для определения ресурсов, которые нужно исключить из мониторинга или включить в него.
   Можно ввести несколько пар ключ/значение: каждый раз при вводе пары появляется новая пустая строка для редактирования.
5. Нажмите **Save** для сохранения конфигурации.

   Чтобы автоматически импортировать теги Azure в Dynatrace, включите **Capture Azure tags automatically**.

Сервисы Azure, отслеживаемые по умолчанию

После подключения Dynatrace к среде Azure немедленно начинается мониторинг встроенных сервисов Azure для заданного service principal. Метрики облачных сервисов Azure, отслеживаемых по умолчанию, перечислены в разделе [Классические (ранее «встроенные») метрики Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "Список классических метрик, собираемых Dynatrace по умолчанию для мониторинга Azure.").

Другие сервисы Azure

Помимо облачных сервисов Azure, отслеживаемых по умолчанию, можно также мониторить все остальные облачные сервисы Azure. Облачные сервисы Azure включаются для мониторинга отдельно для каждого подключения Azure.

Добавление сервиса в мониторинг

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure найдите нужное подключение и выберите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в его строке.
3. В разделе **Services** выберите **Manage services**.
4. Нажмите **Add service**.
5. Выберите сервис из списка и нажмите **Add service**.
6. Нажмите **Save changes** для сохранения конфигурации.

Можно добавить несколько облачных сервисов, повторив шаги выше.

Настройка собираемых метрик для сервиса

После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для этого сервиса.

Рекомендуемые метрики:

* Включены по умолчанию
* Не могут быть отключены
* Могут сопровождаться рекомендуемыми измерениями (включены по умолчанию, не могут быть отключены)
* Могут сопровождаться дополнительными измерениями (отключены по умолчанию, можно включить)

Помимо рекомендуемых метрик, для большинства сервисов можно включить **дополнительные** метрики, которые добавляются и настраиваются вручную.

Список облачных сервисов Azure и собираемых метрик

Полный список облачных сервисов Azure и информацию о метриках для каждого из них см. в разделе [Все облачные сервисы Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.").

Список поддерживаемых сервисов Azure можно проверить в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=azure). Также можно открыть Dynatrace Hub из среды мониторинга и выполнить поиск по слову "Azure".

Добавление и настройка метрик

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure найдите нужное подключение и выберите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в его строке.
3. В разделе **Services** выберите **Manage services**.
4. Выберите сервис, для которого нужно добавить метрики. На странице сведений о сервисе отображается список отслеживаемых метрик.
5. Нажмите **Add metric**.
6. В списке **Add new metric** выберите метрику и нажмите **Add metric**.
7. Нажмите ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") для разворачивания сведений о метрике и её настройки.
8. Нажмите **Apply** для сохранения конфигурации.

После выбора облачных сервисов и сохранения изменений мониторинг добавленных сервисов начинается автоматически.

## Что дальше?

В течение нескольких минут данные появятся на ваших дашбордах.

Просмотр основных измерений для каждого подключения Azure

1. Откройте **Azure**.
2. Выберите подключение, для которого нужно просмотреть обзор инфраструктуры Azure.

Также можно создать собственный дашборд на основе метрик, собранных для экземпляров Azure. Подробнее о создании дашбордов см. в разделе [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Classic, управлять ими и использовать их.").

Виртуальные машины, контейнеры и глубокий мониторинг кода с Dynatrace OneAgent

Dynatrace OneAgent обеспечивает непревзойдённую глубину анализа хостов, контейнеров и кода. Подробнее см. в разделе [Интеграции Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.").

Дополнительная настройка уведомлений и оповещений

После настройки мониторинга Azure можно:

* [Настроить уведомления мониторинга с Azure Alerts](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts "Интеграция с оповещениями Azure Monitor и поддерживаемые типы оповещений Azure Monitor"). Это позволит применять оповещения и автоматически преобразовывать их в события, используемые ИИ Davis® для более глубокого анализа.
* [Настроить метрические события для оповещений](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting "Настройка и конфигурирование метрических событий для оповещений."). Это позволит создавать, включать/отключать и настраивать рекомендуемые правила оповещений.

Мониторинг журналов Azure

Также можно вести мониторинг журналов Azure. Подробнее см. в разделе [Журналы Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте Azure log forwarding для приёма журналов Azure.").