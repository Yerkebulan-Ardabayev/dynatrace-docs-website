---
title: Мониторинг сервисов Azure с помощью метрик Azure Monitor
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide
scraped: 2026-03-06T21:17:39.229286
---

# Мониторинг сервисов Azure с помощью метрик Azure Monitor

# Мониторинг сервисов Azure с помощью метрик Azure Monitor

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 13 мин
* Обновлено 28 января 2026 г.

Следуйте этому руководству, чтобы начать удалённый сбор данных из Azure Monitor.

Это руководство посвящено мониторингу инфраструктуры сервисов Azure, в частности мониторингу облачных сервисов Azure через Azure Monitor. См. раздел [Что дальше](#next) для получения информации о полном мониторинге стека и мониторинге логов ваших сервисов Azure.

В качестве альтернативы вы можете настроить среду Dynatrace SaaS с помощью [Azure Marketplace](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Настройка и конфигурация среды Dynatrace SaaS с помощью Azure Marketplace.").

После установления начального мониторинга вы можете добавлять, удалять или изменять мониторинг сервисов через веб-интерфейс Dynatrace или, в масштабе, с помощью Dynatrace API.

Подробности о собираемых измерениях

Чтобы узнать, какие измерения собираются для каждого из сервисов Azure, см.:

* [Облачные сервисы Azure, включённые по умолчанию, и метрики](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "Список классических метрик, которые Dynatrace собирает по умолчанию для мониторинга Azure.")
* [Облачные сервисы Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.")

Мониторинг инфраструктуры сервисов Azure предоставляет метрики из Azure Monitor и данные инфраструктуры, доступные через публичный Azure API. Данные собираются с интервалом в пять минут.

## Стоимость мониторинга

Факторы, влияющие на стоимость мониторинга Azure с помощью Dynatrace через Azure Monitor:

* Каждый сервис, отслеживаемый Dynatrace через Azure Monitor, а также обработка и анализ логов, приводят к потреблению [единиц данных Davis](/docs/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).").
* Microsoft может взимать дополнительную плату за запросы метрик Azure Monitor, если вы превысите 1 миллион вызовов API в месяц. Подробнее о дополнительных расходах см. в [документации Microsoft](https://dt-url.net/ie03w85).
* Подробнее о стоимости сбора метрик см. [Обзор метрик на основе Grail (DPS)](/docs/license/capabilities/metrics "Узнайте, как рассчитывается потребление метрик Dynatrace на основе Grail в модели подписки Dynatrace Platform.").

## Предварительные требования для мониторинга

Для настройки мониторинга Azure необходимо выполнить три предварительных условия:

Права администратора Dynatrace

Для управления конфигурацией мониторинга Azure необходимо разрешение **Изменение настроек мониторинга** в Dynatrace. Вы можете настроить разрешение **Изменение настроек мониторинга** на уровне [разрешений](/docs/manage/identity-access-management/permission-management/role-based-permissions "Разрешения на основе ролей") среды или зоны управления.

ActiveGate с поддержкой мониторинга Azure

Для мониторинга сервисов Azure Dynatrace необходимо подключаться к Azure Monitor API и опрашивать его каждые 5 минут. Как минимум один ActiveGate должен иметь возможность подключения к Azure Monitor для выполнения задач мониторинга.

Чтобы проверить наличие подходящего ActiveGate

1. Перейдите в **Состояние развёртывания** > **ActiveGates**.
2. Установите фильтр `С модулями: Azure`.

   * Если результирующий список пуст, необходимо добавить хотя бы один ActiveGate с включённым модулем облачного мониторинга.
   * Если список не пуст, вы готовы к активации мониторинга Azure.

Чтобы добавить ActiveGate с поддержкой облачного мониторинга, следуйте [руководству по установке ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate") и вернитесь к этому руководству после завершения.

#### Разрешение доступа ActiveGate к URL-адресам Azure

Интеграция обращается к следующим конечным точкам Azure API, поэтому они должны быть доступны с вашего ActiveGate:

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

Наиболее частой причиной проблем с сертификатами при использовании прокси с перехватом TLS является отсутствие сертификата CA прокси в хранилище доверенных сертификатов ActiveGate.
Если проблемы с прокси сохраняются, см.:

* [Прокси для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Узнайте, как настроить свойства ActiveGate для использования прокси.")
* [Доверенные корневые сертификаты для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как указать пользовательское хранилище доверенных сертификатов, которое объединяется с корневыми сертификатами Java и используется по умолчанию для всех подключений.")
* [Пользовательский SSL-сертификат для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.")

«Ошибка связи.»

Убедитесь, что URL-адреса добавлены в белый список. В противном случае вы можете получить ошибки связи или тайм-ауты.

Роли и разрешения Azure

Для выполнения этих шагов необходимы права администратора Azure.

Мониторинг Azure выполняется удалённо через API Azure Monitor, которые создаются и предоставляются Microsoft. Dynatrace необходимо иметь доступ к этим API, поэтому вам нужно настроить Azure для предоставления такого доступа. Вам потребуется:

* Достаточные разрешения для регистрации приложения в вашем клиенте Azure AD и назначения приложению роли в вашей подписке Azure.
* [Субъект-служба](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) Azure для доступа к Azure API.

Для мониторинга сервисов Dynatrace необходимы как минимум разрешения на чтение. Приведённые ниже шаги описывают добавление разрешений на чтение для субъекта-службы и относятся к распространённому подходу с одним клиентом. Перед этим мы рекомендуем ознакомиться с нашими рекомендациями по [настройке субъекта-службы Azure для предотвращения ограничения Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure#service-principal "Руководство по ограничению вызовов Azure API для предотвращения троттлинга").

Интеграция Dynatrace для Azure поддерживает **Azure Lighthouse**, что позволяет Dynatrace иметь мультитенантный доступ к Azure.

1. Перейдите к терминалу [Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
2. Выполните следующую команду, чтобы вывести список всех подписок и выбрать ту, для которой вы хотите добавить разрешения.

   ```
   az account list --output table
   ```
3. Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.

   ```
   az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID1> /subscriptions/<YourSubscriptionID2> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
   ```

   Обязательно замените заполнители (`<...>`) вашими значениями:

   * `<YourServicePrincipalName>` — имя субъекта-службы, который будет создан для доступа Dynatrace к Azure.
   * `<YourSubscriptionID1>`, `<YourSubscriptionID2>` — имена подписок, указанных на предыдущем шаге, к которым вы хотите предоставить доступ Dynatrace.
4. Выполните отредактированную команду.
5. Скопируйте учётные данные, полученные в результате выполнения команды, и сохраните их для последующего использования.

#### Другие варианты необходимых разрешений

Создание пользовательской роли через Azure CLI 2.0

Другой способ получить разрешения на чтение — создать пользовательскую роль для Dynatrace с предопределённым набором разрешений для детального контроля.

1. Создайте пользовательскую роль, следуя [руководству Microsoft](https://docs.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-cli#create-a-custom-role). Вы можете использовать следующий JSON-шаблон в качестве основы для разрешений:

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
2. Перейдите к терминалу [Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
3. Выполните следующую команду, чтобы вывести список всех подписок и выбрать ту, для которой вы хотите добавить разрешения.

   ```
   az account list --output table
   ```
4. Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.

   ```
   az ad sp create-for-rbac --name <YourServicePrincipalName> --role <YourCustomRole> --scopes /subscriptions/<YourSubscriptionID1> /subscriptions/<YourSubscriptionID2> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
   ```

   Замените заполнители (`<...>`) вашими значениями:

   * `<YourServicePrincipalName>` — имя субъекта-службы, который будет создан для доступа Dynatrace к Azure.
   * `<YourCustomRole>` — имя роли, которую вы создали для Dynatrace.
   * `<YourSubscriptionID1>`, `<YourSubscriptionID2>` — имена подписок, указанных на предыдущем шаге (подписки, к которым вы хотите предоставить доступ Dynatrace).
5. Выполните отредактированную команду.
6. Скопируйте учётные данные, полученные в результате выполнения команды, и сохраните их для последующего использования.

Создание субъекта-службы через Azure Portal

Чтобы создать субъекта-службу в Azure Portal, необходимо зарегистрировать приложение в Microsoft Entra ID и предоставить разрешения доступа для субъекта-службы.

Чтобы зарегистрировать приложение

1. Перейдите в портал управления Azure и выберите **Microsoft Entra ID**.
2. Скопируйте значение **Tenant ID** и сохраните его как `Tenant ID` для последующего использования. Это необходимо для [настройки подключения Dynatrace к вашей учётной записи Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide#azureconfig-connect "Настройка и конфигурация мониторинга Azure в Dynatrace.").
3. Выберите **Регистрация приложений** на панели навигации выбранного Active Directory.
4. Нажмите **Новая регистрация** в верхней части панели регистрации приложений и введите имя вашего приложения.
5. Оставьте все остальные настройки со значениями по умолчанию и нажмите **Зарегистрировать**.
6. Скопируйте значение **Application (client) ID** и сохраните его как `Client ID` для последующего использования.
7. Выберите **Сертификаты и секреты** > **Новый секрет клиента**, чтобы создать новый ключ безопасности.
8. Введите описание ключа, выберите желаемый срок действия ключа, затем нажмите **Добавить**, чтобы сохранить новый ключ.
9. Скопируйте значение **Value** и сохраните его как `Secret Key` для последующего использования.

   Вы не сможете получить значение ключа после того, как покинете панель **Ключ**.

Чтобы предоставить разрешения доступа для субъекта-службы

1. В Azure Portal выберите **Все сервисы** > **Общие** > **Подписки**.
2. На странице **Подписки** выберите вашу подписку, затем выберите **Управление доступом (IAM)**.

Настройка при назначении разрешений на чтение

Настройка при создании пользовательской роли

1. Нажмите **Добавить назначение роли** и выберите **Reader**.
2. Нажмите **Далее**.
3. В разделе **Участники** введите следующие данные:

   * Для **Назначить доступ** выберите `Пользователь`, `группа` или `субъект-служба`.
   * Для **Участники** нажмите **Выбрать участников** и затем выберите субъекта-службу из списка слева.
4. Нажмите **Далее**, затем нажмите **Просмотр + назначение**.

1. В разделе **Добавить пользовательскую роль** нажмите **Добавить**.
2. В разделе **Основные** введите имя роли и затем выберите **Начать с нуля**.
3. В разделе **JSON** вы можете использовать шаблон ниже в качестве основы для разрешений, которые можно выбрать.

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
4. Нажмите **Просмотр + создание** для проверки конфигурации, затем нажмите **Создать**.

Создание субъекта-службы через PowerShell

Чтобы создать нового субъекта-службу и предоставить ему разрешения доступа в PowerShell, см. [Создание субъекта-службы Azure с помощью Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/create-azure-service-principal-azureps?view=azps-7.5.0&viewFallbackFrom=azps-2.0.0).

Если вы решите создать пользовательскую [роль](https://docs.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-powershell), см. [Создание пользовательской роли через Azure CLI 2.0](#cli).

## Создание конфигурации мониторинга

Вы можете создавать, активировать и управлять несколькими подключениями мониторинга. Каждое подключение определяется учётными данными и/или токенами доступа, необходимыми Dynatrace для получения данных, а также фактической областью мониторинга.

Почему конфигурация выполняется для каждого подключения?

Поддержка нескольких подключений и конфигураций позволяет мониторить даже чрезвычайно сложные среды. При таком подходе вам не нужно настраивать всё сразу. Вместо этого вы можете постепенно добавлять конфигурации мониторинга к существующей настройке. Такая архитектура также позволяет легко реагировать на динамические изменения отслеживаемой среды без необходимости перенастройки незатронутых элементов.

Добавление нового подключения Azure

Если вы выполнили все предыдущие шаги, вы готовы к настройке мониторинга Azure.

Чтобы добавить новое подключение Azure

1. Перейдите в **Настройки** > **Облако и виртуализация** > **Azure**. На странице отображаются уже настроенные подключения Azure.

   Если вы не предоставили ActiveGate, необходимый для мониторинга Azure (см. [Предварительные требования](#capable-activegate)), соответствующая информация будет отображена на экране, и вы не сможете продолжить процесс настройки.

   Изменение или удаление существующих подключений

   Вы можете вернуться и изменить уже настроенные подключения позже.

   1. Перейдите в **Настройки** > **Облако и виртуализация** > **Azure**. На странице отображается список существующих подключений.
   2. Отредактируйте подключения по необходимости.

      * Чтобы отредактировать существующее подключение или отслеживаемые в нём сервисы, нажмите **Редактировать** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать") в соответствующей строке.
      * Чтобы удалить существующее подключение, нажмите **Удалить** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Удалить") в соответствующей строке.
2. Нажмите **Подключить новый экземпляр** и заполните поля конфигурации.

   * **Идентификатор подключения** — введите описательное имя для подключения.
   * **Client ID** и **Tenant ID** — введите значения, полученные при создании субъекта-службы Azure.

     Если вы создали субъекта-службу Azure в PowerShell, установите **Client ID** в значение `ApplicationId`.
   * **Secret Key** — получен при создании субъекта-службы Azure.

     Ограничение сбора данных

     Вы можете ограничить данные, собираемые из Azure Monitor, определив фильтр конкретных ресурсов на основе тегов.

     Вы можете выбрать мониторинг ресурсов на основе существующих тегов Azure, так как Dynatrace автоматически импортирует их из экземпляров сервисов.
     Чтобы мониторить ресурсы на основе тегов

     1. Перейдите в **Настройки** > **Облако и виртуализация** > **Azure**.
     2. На странице обзора Azure нажмите значок **Редактировать** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать") для экземпляра Azure.
     3. Установите **Отслеживаемые ресурсы** в **Мониторить ресурсы, выбранные по тегам**.
     4. Введите пары ключ/значение для идентификации ресурсов, которые нужно исключить из мониторинга или включить в мониторинг.
        Вы можете ввести несколько пар ключ/значение: каждый раз при вводе пары отображается новая пустая строка для редактирования.
     5. Нажмите **Сохранить** для сохранения конфигурации.

        Для автоматического импорта тегов Azure в Dynatrace включите **Автоматический захват тегов Azure**.

     Автоматический импорт тегов

     При необходимости вы можете отключить автоматический импорт тегов. Если функция включена, теги ресурсов будут импортированы, но теги групп ресурсов не будут импортированы.
3. Нажмите **Подключить**, чтобы добавить информацию о подключении в список подключений Azure.

Мониторинг ресурсов на основе тегов

Существует ограничение в 20 записей для тегов `Include` или `Exclude`.

Вы можете выбрать мониторинг ресурсов на основе существующих тегов Azure, так как Dynatrace автоматически импортирует их из экземпляров сервисов.
Чтобы мониторить ресурсы на основе тегов

1. Перейдите в **Настройки** > **Облако и виртуализация** > **Azure**.
2. На странице обзора Azure нажмите значок **Редактировать** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать") для экземпляра Azure.
3. Установите **Отслеживаемые ресурсы** в **Мониторить ресурсы, выбранные по тегам**.
4. Введите пары ключ/значение для идентификации ресурсов, которые нужно исключить из мониторинга или включить в мониторинг.
   Вы можете ввести несколько пар ключ/значение: каждый раз при вводе пары отображается новая пустая строка для редактирования.
5. Нажмите **Сохранить** для сохранения конфигурации.

   Для автоматического импорта тегов Azure в Dynatrace включите **Автоматический захват тегов Azure**.

Сервисы Azure, отслеживаемые по умолчанию

После подключения Dynatrace к вашей среде Azure он немедленно начинает мониторинг встроенных сервисов Azure для определённого субъекта-службы. [Классические (ранее «встроенные») метрики Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "Список классических метрик, которые Dynatrace собирает по умолчанию для мониторинга Azure.") содержат список метрик облачных сервисов Azure, отслеживаемых по умолчанию.

Другие сервисы Azure

Помимо облачных сервисов Azure, отслеживаемых по умолчанию, можно также мониторить все другие облачные сервисы Azure. Облачные сервисы Azure включаются для мониторинга для каждого подключения Azure.

Чтобы добавить сервис в мониторинг

1. Перейдите в **Настройки** > **Облако и виртуализация** > **Azure**.
2. На странице обзора Azure найдите подключение, которое хотите изменить, и нажмите **Редактировать** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать") в соответствующей строке.
3. В разделе **Сервисы** нажмите **Управление сервисами**.
4. Нажмите **Добавить сервис**.
5. Выберите сервис из списка и затем нажмите **Добавить сервис**.
6. Нажмите **Сохранить изменения** для сохранения конфигурации.

Вы можете добавить несколько облачных сервисов, повторив шаги выше.

Настройка собираемых метрик для каждого сервиса

После добавления сервиса Dynatrace автоматически начинает сбор набора метрик для данного сервиса.

Рекомендуемые метрики:

* Включены по умолчанию
* Не могут быть отключены
* Могут включать рекомендуемые измерения (включены по умолчанию, не могут быть отключены)
* Могут включать необязательные измерения (отключены по умолчанию, могут быть включены)

Помимо рекомендуемых метрик, для большинства сервисов есть возможность включения **необязательных** метрик, которые можно добавить и настроить вручную.

Список облачных сервисов Azure и собираемых метрик

Чтобы увидеть полный список облачных сервисов Azure и узнать о метриках, собираемых для каждого из них, см. [Все облачные сервисы Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.").

Вы можете проверить список поддерживаемых сервисов Azure в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=azure). Вы также можете получить доступ к Dynatrace Hub из вашей среды мониторинга и выполнить поиск по запросу «Azure».

Чтобы добавить и настроить метрики

1. Перейдите в **Настройки** > **Облако и виртуализация** > **Azure**.
2. На странице обзора Azure найдите подключение, которое хотите изменить, и нажмите **Редактировать** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать") в соответствующей строке.
3. В разделе **Сервисы** нажмите **Управление сервисами**.
4. Выберите сервис, для которого хотите добавить метрики. На странице деталей сервиса отображаются метрики, которые вы мониторите для этого сервиса.
5. Нажмите **Добавить метрику**.
6. В списке **Добавить новую метрику** выберите метрику и затем нажмите **Добавить метрику**.
7. Нажмите ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Развернуть строку"), чтобы развернуть детали метрики и настроить метрику.
8. Нажмите **Применить** для сохранения конфигурации.

После выбора облачных сервисов и сохранения изменений мониторинг вновь добавленных сервисов запускается автоматически.

## Что дальше?

В течение нескольких минут вы увидите данные на ваших дашбордах.

Чтобы увидеть основные измерения для каждого из ваших подключений Azure

1. Перейдите в ![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure") **Azure (классический вид)**.
2. Выберите подключение, для которого хотите увидеть обзор инфраструктуры Azure.

Вы также можете создать собственный дашборд из метрик, собранных для ваших экземпляров Azure. Подробнее о создании дашбордов см. [Дашборды (классический вид)](/docs/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать классические дашборды Dynatrace.").

Виртуальные машины, контейнеры и глубокий мониторинг кода с помощью Dynatrace OneAgent

Dynatrace OneAgent обеспечивает непревзойдённую глубину анализа хостов, контейнеров и кода. Подробнее см. [Интеграции Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.").

Дополнительная настройка уведомлений и оповещений

После настройки мониторинга Azure вы можете:

* [Настроить уведомления мониторинга с помощью Azure Alerts](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts "Интеграция с оповещениями Azure Monitor и поддерживаемые типы оповещений Azure Monitor"). Это позволяет применять оповещения и автоматически преобразовывать их в события, которые используются Dynatrace Intelligence для более глубокого анализа.
* [Настроить события метрик для оповещений](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting "Настройка и конфигурация событий метрик для оповещений."). Это позволяет создавать, включать/отключать и настраивать рекомендуемые правила оповещений.

Мониторинг логов Azure

Вы также можете мониторить логи Azure. Подробнее см. [Логи Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку логов Azure для сбора логов Azure.").