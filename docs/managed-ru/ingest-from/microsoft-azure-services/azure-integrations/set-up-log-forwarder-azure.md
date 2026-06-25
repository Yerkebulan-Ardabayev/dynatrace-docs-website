---
title: Журналы Azure
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure
scraped: 2026-05-12T11:09:44.541233
---

# Журналы Azure

# Журналы Azure

* Практическое руководство
* Чтение: 17 мин
* Обновлено 17 октября 2025 г.

Потребление DDU для Log Monitoring

Тарификация DDU распространяется на облачный Log Monitoring. Подробнее см. в разделе [DDU для Log Monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU в Dynatrace Log Monitoring Classic.").

Azure log forwarding позволяет передавать журналы Azure из Azure Event Hubs в Dynatrace через экземпляр Azure Function App. Поддерживаются журналы ресурсов Azure, журналы действий и журналы входа Entra ID.

## Разворачиваемые ресурсы

Azure log forwarding выполняется напрямую через Cluster API. Если прямой приём через Cluster API не нужен, для приёма журналов необходимо использовать существующий ActiveGate.

Развёртывание Azure log forwarder создаёт следующие ресурсы:

* Storage account (`Microsoft.Storage/storageAccounts`)
* Storage Account Blob Service (`Microsoft.Storage/storageAccounts/blobServices`)
* Azure App Service plan (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Azure log forwarder по умолчанию использует Azure function на базе Linux. Функции на базе Windows не поддерживаются.

Подробнее о создаваемых ресурсах см. в [файле Azure Resource Manager на GitHub](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json)

## Ограничения

Журналы старше 24 часов отклоняются (эндпоинт приёма журналов Dynatrace считает их устаревшими), поэтому рекомендуется не устанавливать время хранения в Azure Event Hubs более 24 часов.

Azure log forwarder поддерживает максимум 70 МБ в минуту (~4 ГБ в час) в конфигурации по умолчанию. Пропускная способность измеряется метрикой Event Hubs `Outgoing Bytes` экземпляра Event Hubs, привязанного к функции. Инструкции по масштабированию см. в разделе [Руководство по масштабированию](#scalingguide).

## Предварительные требования

Ниже приведён список требований для настройки Azure log forwarding. Часть из них необходима до начала развёртывания, остальные нужны в процессе.

### Dynatrace

Если используется более ранняя версия Dynatrace, инструкции см. в разделе [Альтернативные варианты развёртывания](#alternative).

* Dynatrace версии 1.217+

* [Включите универсальный приём журналов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов и каковы возможные ограничения.")

* [Создайте токен API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях применения.") и включите разрешение **Ingest logs**. Токен API применяется к обеим версиям.

### Azure

1. В каждом регионе Azure, откуда требуется получать журналы, [создайте группу ресурсов и настройте экземпляр Azure Event Hubs](https://dt-url.net/8w03rs3).

   Чтобы иметь возможность отправлять журналы,

   * Экземпляры Event Hubs и группа ресурсов, в которой будет выполняться развёртывание, должны находиться в одном регионе.
   * Убедитесь, что в разделе Event Hubs Namespace > Public access > Public network access кнопка **Disabled** НЕ выбрана. В противном случае журналы не будут отправлены в Dynatrace.
2. Создайте правило авторизации с разрешением **listen** для экземпляра Event Hubs, настроенного для приёма журналов:

   ```
   az eventhubs eventhub authorization-rule create --resource-group <your_resource_group> --namespace-name <your_event_hub_namespace> --eventhub-name <your_event_hub_instance> --name <authorization_rule_name> --rights Listen
   ```
3. Получите строку подключения Event Hubs для созданного выше правила авторизации:

   ```
   az eventhubs eventhub authorization-rule keys list --resource-group <your_resource_group> --namespace-name <your_event_hub_namespace> --eventhub-name <your_event_hub_instance> --name <your_authorization_rule_name>
   ```
4. Настройте [параметры диагностики](https://dt-url.net/se83r02), чтобы передавать как журналы ресурсов, так и журналы входа Entra ID в экземпляры Azure Event Hub.

### CLI

Развёртывание Azure log forwarding можно выполнить с помощью Azure Portal Cloud Shell (Bash) или с любого компьютера с установленным [Azure CLI](https://dt-url.net/cf63rl6) и оболочкой Bash (Linux или Windows WSL).

## Развёртывание

1. Задайте следующие переменные среды, заменив заполнители (`<...>`) собственными значениями.

   * Для `DEPLOYMENT_NAME` укажите имя развёртывания длиной от 3 до 20 символов. Допускаются строчные буквы и цифры.

     **Примечание:** Имя должно быть глобально уникальным, так как оно добавляется к создаваемым ресурсам Azure.

* Для `TARGET_URL` укажите URL среды: `https://{your-domain}/e/{your-environment-id}/e/{your-environment-id}/`. Чтобы узнать, как определить идентификатор среды для развёртывания Managed, см. [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как определить идентификатор среды мониторинга и работать с ней.").

* Для `TARGET_API_TOKEN` введите токен API. Подробнее см. в разделе [Требования Dynatrace](#dynatrace).
* Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробнее см. в разделе [Требования Azure](#azure).
* Для `EVENT_HUB_CONNECTION_STRING` введите строку подключения для экземпляров Azure Event Hubs, настроенных для приёма журналов. Подробнее см. в разделе [Требования Azure](#azure).

Дополнительно Можно включить [самомониторинг](#sfm) и/или [фильтрацию журналов](#filter) во время или после развёртывания.

```
DEPLOYMENT_NAME=<your_deployment_name>



TARGET_URL=<your_environment_URL>



TARGET_API_TOKEN=<your_API_token>



RESOURCE_GROUP=<your_resource_group>



EVENT_HUB_CONNECTION_STRING="<your_Event_Hub_connection_string>"
```

2. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-connection-string $EVENT_HUB_CONNECTION_STRING  --require-valid-certificate true
   ```

## Просмотр журналов Azure

После развёртывания скрипта можно просматривать и анализировать журналы Azure в Dynatrace:
Откройте **Logs** и в фильтре атрибутов выполните поиск по **Azure**.

* Если журналы поступают, Azure log forwarder развёрнут успешно.
* Если журналы не появились в течение 10 минут, обратитесь к разделу **Verification** на этой странице.

Для фильтрации журналов Azure можно использовать [DQL](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").
Например, в DQL-запрос можно добавить следующую строку:

```
fetch logs



| filter matchesValue(dt.openpipeline.source, "/api/v2/logs/ingest") AND matchesValue(cloud.provider, "Azure")



| sort timestamp desc
```

При наличии нескольких интеграций для уточнения фильтров можно дополнительно использовать значения `cloud.log_forwarder` и `dt.auth.origin`.

## Самомониторинг Дополнительно

Самомониторинг позволяет быстро диагностировать, правильно ли функция обрабатывает и отправляет журналы в Dynatrace.

### Включение самомониторинга

Для включения самомониторинга существует два варианта:

* **Во время развёртывания:** Задайте параметр [`--enable-self-monitoring`](#par) (или переменную среды [`SFM_ENABLED`](#var)) в значение `true`.
* **После развёртывания:** В Azure Portal откройте конфигурацию развёрнутого экземпляра Function App и задайте `SELF_MONITORING_ENABLED` в значение `true`.

Включение managed identity

После включения самомониторинга необходимо включить [managed identity](https://dt-url.net/qj23rie) для
экземпляра Function App, созданного во время развёртывания, и настроить его для отправки метрик ресурсу.

Настройка managed identity

1. В Azure Portal откройте **Settings** экземпляра Function App, созданного во время развёртывания, и выберите **Identity**.
2. Выберите **Yes** для **Enable system assigned managed identity**.
3. Перейдите в группу ресурсов, где развёрнут Function App, и выберите **Access control (IAM)**.
4. Нажмите **Add** для добавления назначения роли.
5. Задайте роль **Monitoring Metrics Publisher**.
6. Нажмите **Save** для сохранения конфигурации.

### Метрики самомониторинга

После включения самомониторинга в пространстве имён `dynatrace_logs_self_monitoring` нового экземпляра Function App будут доступны следующие метрики.

| Название метрики | Описание | Измерение |
| --- | --- | --- |
| `all_requests` | Все запросы, отправленные в Dynatrace. |  |
| `dynatrace_connectivity_failures` | Фиксируется при возникновении проблем с подключением к Dynatrace. | `connectivity_status` |
| `parsing_errors` | Фиксируется при возникновении ошибок разбора в процессе обработки журналов. |  |
| `processing_time` | Время, необходимое для обработки всех журналов. |  |
| `sending_time` | Время, необходимое для отправки всех запросов. |  |
| `too_long_content_size` | Фиксируется, когда содержимое журнала слишком велико. Содержимое будет обрезано. |  |
| `too_old_records` | Фиксируется, когда журналы, полученные из Event Hubs, устарели. |  |

## Фильтрация журналов Дополнительно

Чтобы сократить количество журналов, отправляемых в Dynatrace, можно применить фильтры.
Для применения фильтров существует два варианта:

* **Во время развёртывания:** Задайте переменную среды `FILTER_CONFIG` в Azure Portal Cloud Shell (Bash) перед запуском скрипта развёртывания.

  1. Добавьте переменную среды `FILTER_CONFIG` в список переменных среды, необходимых для скрипта развёртывания.

     Обязательно замените заполнители собственными значениями. Подробнее см. в разделе [Параметры фильтра](#options).

     ```
     FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>;FILTER.GLOBAL.CONTAINS_PATTERN=<pattern>;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>;FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<pattern>;FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>;FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<pattern>"
     ```
  2. Задайте переменные среды.
  3. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.
* **После развёртывания:** Добавьте `FILTER_CONFIG` в Azure Portal.

  1. В Azure Portal откройте **Environment variables** развёрнутого экземпляра Function App.
  2. В разделе **App settings** найдите и выберите **FILTER\_CONFIG**.

     **FILTER\_CONFIG** появится в Azure после запуска скрипта развёртывания.
  3. Нажмите **Edit**, чтобы задать **Value** для фильтра.

     Пример редактирования

     ![Редактирование](https://dt-cdn.net/images/image-36-3759-7bc37dfe3c.png)

     Редактирование

     В качестве альтернативы можно нажать **Advanced edit** и ввести значение в формате JSON.

     Пример расширенного редактирования

     ![Расширенный режим](https://dt-cdn.net/images/image-37-3804-dffe41ec79.png)

     Расширенный режим
  4. Нажмите **OK**.
  5. Перезапустите экземпляр Function App.

### Параметры фильтра

`FILTER_CONFIG`: переменная в формате пар «ключ-значение». Можно задать два типа фильтров (`MIN_LOG_LEVEL` и/или `CONTAINS_PATTERN`) для трёх групп фильтров (`GLOBAL`, `RESOURCE_TYPE` и/или `RESOURCE_ID`).

#### Тип фильтра: `MIN_LOG_LEVEL`

Данный тип фильтра позволяет исключать журналы с нежелательными уровнями. Возможные уровни журналов:

* **Critical** (или `1`)
* **Error** (или `2`)
* **Warning** (или `3`)
* **Informational** (или `4`)

Пример:
`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Warning"`
В приведённом примере журналы уровня **Informational** будут пропущены, и в Dynatrace будут отправлены только журналы **Warning**, **Error** и **Critical**.

Варианты синтаксиса:

* `FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>`
* `FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>`
* `FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>`

Можно задать один глобальный фильтр и дополнительные фильтры для конкретного типа ресурса или идентификатора ресурса.

Пример:
`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Error;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.MICROSOFT.WEB/SITES=Informational"`
В приведённом примере все журналы от экземпляров с типом ресурса `MICROSOFT.WEB/SITES` будут отправлены в Dynatrace, а для всех остальных ресурсов журналы **Informational** и **Warning** будут отфильтрованы.

#### Тип фильтра: `CONTAINS_PATTERN`

Данный тип фильтра позволяет собирать журналы, содержащие определённый текст. Используется fnmatch с поддержкой подстановочных знаков в стиле Unix-оболочки. Подробнее см. в разделе [Сопоставление шаблонов имён файлов Unix](https://docs.python.org/3/library/fnmatch.html).

Варианты синтаксиса:

* `FILTER.GLOBAL.CONTAINS_PATTERN=<log_pattern>`
* `FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<log_pattern>`
* `FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<log_pattern>`

#### Группа фильтров: `GLOBAL`

Этот фильтр применяется ко всем журналам.

#### Группа фильтров: `RESOURCE_TYPE`

Данный фильтр применяется только к журналам от ресурсов указанного типа ресурса Azure, например `Microsoft.Compute/virtualMachines`.

Тип ресурса можно найти в Azure Portal в разделе **Properties** ресурса.

Если поле **Type** не отображается в **Properties**, его можно извлечь из строки идентификатора ресурса.

Синтаксис строки идентификатора ресурса:
`/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/<resourceType>/<resourceName>`
Тип ресурса: часть строки между `/providers/` и `/resourceName/`.

#### Группа фильтров: `RESOURCE_ID`

Данный фильтр применяется только к журналам от конкретного ресурса, идентифицируемого по идентификатору ресурса Azure.

Тип ресурса можно найти в Azure Portal в разделе **Properties** ресурса.

### Правила фильтрации

* Если для одной группы заданы два типа фильтров, оба условия должны выполняться, поэтому второй фильтр должен соответствовать первому.

  Например, если задать `MIN_LOG_LEVEL` равным **Warning** и `CONTAINS_PATTERN` равным `<some_important_message>`, будут получены только журналы **Warning**, содержащие `<some_important_message>`, а все прочие журналы предупреждений без этого сообщения будут отфильтрованы.
* Если задан один тип фильтра для одной группы и другой тип для другой группы, два условия не пересекаются.

  Например, если задать `MIN_LOG_LEVEL` равным **Warning** для `GLOBAL` и `CONTAINS_PATTERN` равным `<some_important_message>` для `RESOURCE_TYPE`, будут получены все журналы **Warning**, **Error** и **Critical** из `GLOBAL`, а также все журналы из `RESOURCE_TYPE`, содержащие `<some_important_message>`.
* Если для одной группы (глобальной или типа/идентификатора ресурса) задано несколько пар типов фильтров (`MIN_LOG_LEVEL` и `CONTAINS_PATTERN`), применяется только последняя пара; остальные игнорируются.

## Обновление Azure log forwarding

Обновление Azure log forwarding

1. Потребуется пакет с исходным кодом Azure log forwarder: загрузите последнюю версию Dynatrace.

   ```
   wget https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-log-forwarder.zip
   ```
2. Разверните новую версию, заменив заполнители требуемыми значениями.

   ```
   az webapp deployment source config-zip -g <your_resource_group_name> -n <application_name> --src <zip_file_path>
   ```

Некоторые выпуски Azure log forwarder содержат изменения, требующие полной переустановки. Подробнее см. на [странице выпусков GitHub](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases).

## Альтернативные варианты развёртывания

### Использование существующего ActiveGate

Если прямой приём через Cluster API не нужен, для приёма журналов необходимо использовать существующий ActiveGate.

Инструкции приведены ниже.

#### Предварительные требования

Dynatrace версии 1.217+

* [Требования Dynatrace](#dynatrace), перечисленные выше
* [Требования Azure](#azure), перечисленные выше
* [Требования CLI](#cli), перечисленные выше

#### Настройка

1. Задайте следующие переменные среды, заменив заполнители (`<...>`) собственными значениями.

   * Для `DEPLOYMENT_NAME` укажите имя развёртывания (только строчные буквы).
   * Для `TARGET_URL` введите URL API вашего эндпоинта ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. Чтобы узнать, как определить идентификатор среды, см. [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как определить идентификатор среды мониторинга и работать с ней.").
   * Для `TARGET_API_TOKEN` введите токен API. Подробнее см. в предварительных требованиях выше.
   * Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробнее см. в разделе [Требования Azure](#azure).
   * Для `EVENT_HUB_CONNECTION_STRING` введите строку подключения для экземпляров Azure Event Hubs, настроенных для приёма журналов. Подробнее см. в разделе [Требования Azure](#azure).
   * Для `USE_EXISTING_ACTIVE_GATE` введите `true`.
   * Дополнительно Для `REQUIRE_VALID_CERTIFICATE` введите `true` или `false`. Этот параметр указывает log forwarder проверять SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются.

   Дополнительно Можно включить [самомониторинг](#sfm) и/или [фильтрацию журналов](#filter) во время или после развёртывания.

   ```
   DEPLOYMENT_NAME=<your_deployment_name>



   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   RESOURCE_GROUP=<your_resource_group>



   EVENT_HUB_CONNECTION_STRING="<your_Event_Hub_connection_string>"



   USE_EXISTING_ACTIVE_GATE=true



   REQUIRE_VALID_CERTIFICATE=true
   ```
2. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.

   Проверьте, нужно ли задать другие дополнительные параметры. Все параметры в скобках (`[...]`) являются необязательными. Подробнее см. в разделе [Таблица развёртывания](#table).

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-connection-string $EVENT_HUB_CONNECTION_STRING --require-valid-certificate $REQUIRE_VALID_CERTIFICATE
   ```

### Использование user-assigned managed identity

Существует два типа managed identity: system-assigned и user-assigned. По умолчанию используется system-assigned managed identity. Если предпочтительнее использовать user-assigned managed identity, инструкции приведены ниже.

#### Предварительные требования

Dynatrace версии 1.217+

* [Требования Dynatrace](#dynatrace), перечисленные выше
* [Требования Azure](#azure), перечисленные выше
* [Требования CLI](#cli), перечисленные выше

Помимо [требований Azure](#azure), перечисленных выше, необходимо создать user-assigned managed identity в Azure Portal.

Добавьте роли Event Hubs в user-assigned managed identity. Для привязки триггера концентратора событий необходимо назначить соответствующие встроенные роли: **Azure Event Hubs Data Receiver** и **Azure Event Hubs Data Owner**.

#### Настройка

1. Задайте следующие переменные среды, заменив заполнители (`<...>`) собственными значениями.

   ```
   DEPLOYMENT_NAME=<your_deployment_name>



   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   RESOURCE_GROUP=<your_resource_group>



   EVENT_HUB_NAME=<your_Event_Hub_name>



   REQUIRE_VALID_CERTIFICATE=true



   ENABLE_USER_ASSIGNED_MANAGED_IDENTITY=true



   EVENT_HUB_CONNECTION_CLIENT_ID=<your_user_assigned_MI_client_id>



   MANAGED_IDENTITY_RESOURCE_NAME=<your_user_assigned_MI_resource_name>



   EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE="<your_eventhub_namespace_host_name>"



   CONSUMER_GROUP ="<Your_custom_default_consumer_group_name>"
   ```

   * Для `DEPLOYMENT_NAME` укажите имя развёртывания (только строчные буквы).

* Для `TARGET_URL` укажите URL среды: `https://{your-domain}/e/{your-environment-id}/e/{your-environment-id}/`. Чтобы узнать, как определить идентификатор среды для развёртывания Managed, см. [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как определить идентификатор среды мониторинга и работать с ней.").

* Для `TARGET_API_TOKEN` введите токен API. Подробнее см. в предварительных требованиях выше.
* Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробнее см. в разделе [Требования Azure](#azure).
* Для `EVENT_HUB_NAME` введите имя экземпляров Azure Event Hubs, настроенных для приёма журналов. Подробнее см. в разделе [Требования Azure](#azure).
* Дополнительно Для `REQUIRE_VALID_CERTIFICATE` введите `true` или `false`. Этот параметр указывает log forwarder проверять SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются.
* Для `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` введите `true`. Этот параметр определяет, используется ли user-assigned managed identity вместо system-assigned.
* Для `EVENT_HUB_CONNECTION_CLIENT_ID` введите `Client ID` созданного managed identity.
* Для `MANAGED_IDENTITY_RESOURCE_NAME` введите имя ресурса созданного managed identity.
* Для `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` введите:

  + `Host name` пространства имён Event Hubs.
  + Пользовательское имя группы потребителей по умолчанию.

Дополнительно Можно включить [самомониторинг](#sfm) и/или [фильтрацию журналов](#filter) во время или после развёртывания.

2. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.

   Проверьте, нужно ли задать другие дополнительные параметры. Все параметры в скобках (`[...]`) являются необязательными. Подробнее см. в разделе [Таблица развёртывания](#table).

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-name $EVENT_HUB_NAME --require-valid-certificate $REQUIRE_VALID_CERTIFICATE --enable-user-assigned-managed-identity $ENABLE_USER_ASSIGNED_MANAGED_IDENTITY --eventhub-connection-client-id $EVENT_HUB_CONNECTION_CLIENT_ID --managed-identity-resource-name $MANAGED_IDENTITY_RESOURCE_NAME --eventhub-connection-fully-qualified-namespace $EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE --custom-consumer-group $CONSUMER_GROUP
   ```

### Таблица развёртывания

Полный список параметров см. в таблице развёртывания ниже.

| **Параметр командной строки** | **Переменная среды** | **Описание** |  |
| --- | --- | --- | --- |
| `--deployment-name` | `DEPLOYMENT_NAME` | Обязательно Имя развёртывания. Только строчные буквы. |  |
| `--target-url` | `TARGET_URL` | Обязательно Среда Dynatrace, в которой требуется настроить универсальный приём журналов. |  |
| `--target-api-token` | `TARGET_API_TOKEN` | Обязательно Ваш токен API. |  |
| `--resource-group` | `RESOURCE_GROUP` | Обязательно Имя группы ресурсов Azure, в которой будет выполняться развёртывание. |  |
| `--event-hub-connection-string` | `EVENT_HUB_CONNECTION_STRING` | Обязательно Строка подключения для экземпляра Azure Event Hubs, настроенного для приёма журналов. (Имя Azure Event Hubs, настроенного для приёма журналов.) |  |
| `--event-hub-name` | `EVENT_HUB_NAME` | Дополнительно По умолчанию необязательно. Обязательно, если для аутентификации используется user-assigned managed identity. |  |
| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Дополнительно При значении `true` log forwarder проверяет SSL-сертификат ActiveGate. По умолчанию сертификаты проверяются. |  |
| `--enable-self-monitoring` | `SFM_ENABLED` | Дополнительно При значении `true` Dynatrace отправляет пользовательские метрики в Azure. Подробнее см. в разделе [Включение самомониторинга](#sfm). По умолчанию пользовательские метрики в Azure не отправляются. |  |
| `--filter-config` | `FILTER_CONFIG` | Дополнительно Применение фильтров для сокращения числа журналов, отправляемых в Dynatrace. Подробнее см. в разделе [Фильтрация журналов](#filter). |  |
| `--tags` | `TAGS` | Дополнительно Применение тегов Azure к новым ресурсам в формате пар «ключ:значение» через запятую (например, `"tag:value,tag2:value2"`). Следующие символы не поддерживаются в ключе тега: `,:<>%&\?/` |  |
| `--enable-user-assigned-managed-identity` | `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` | Дополнительно При значении `true` параметры `--eventhub-connection-client-id`, `--managed-identity-resource-name`, `--eventhub-connection-fully-qualified-namespace`, `--event-hub-name` становятся обязательными. Включает использование user-assigned managed identity вместо system-assigned managed identity. |  |
| `--custom-consumer-group` | `CONSUMER_GROUP` | Дополнительно Если указано, это значение будет использоваться как имя группы потребителей по умолчанию. Оставьте пустым для применения значения Azure по умолчанию. |  |
| `--eventhub-connection-client-id` | `EVENT_HUB_CONNECTION_CLIENT_ID` | Дополнительно `Client ID` созданного managed identity. Пример значения: `d8916c27-4c4r-482o-895b-doe0b48c76f7` |  |
| `--managed-identity-resource-name` | `MANAGED_IDENTITY_RESOURCE_NAME` | Дополнительно Имя ресурса созданного managed identity. Пример значения: `test-managed-identity` |  |
| `--eventhub-connection-fully-qualified-namespace` | `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` | Дополнительно `Host name` пространства имён Azure Event Hubs. Пример значения: `sample-eventhub-namespace.servicebus.windows.net` |  |

## Проверка

Чтобы убедиться в успешном развёртывании, откройте в Dynatrace **Logs** и убедитесь, что присутствует следующая строка журнала:

![Строка журнала](https://dt-cdn.net/images/screenshot-2022-08-11-at-11-49-52-928-5957a24948.png)

Строка журнала

Примерно через 10 минут должны начать поступать дополнительные журналы. Если журналы не поступают, проверьте следующее:

* Экземпляры Event Hubs и группа ресурсов, в которой выполняется развёртывание, находятся в одном регионе
* Тщательно выполнены шаги по [настройке параметров диагностики](https://dt-url.net/se83r02)

Кроме того, можно просмотреть журналы Azure Function, в которой запущен Azure-log-forwarder. [Включение потокового вывода журналов выполнения в Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/streaming-logs)

Исчерпание портов SNAT: Azure Functions имеют ограниченное количество портов, которые можно открыть одновременно (128). Число экземпляров, рабочих процессов и параллельных вызовов влияет на количество открытых соединений. При достижении лимита см. [руководство по масштабированию](#scalingguide) ниже.

## Проверка версии

Проверка версии текущего развёрнутого Azure log forwarder

1. Откройте Azure Portal и перейдите в раздел **Subscriptions**.
2. Выберите вашу подписку.
3. Перейдите в **Resource groups**.
4. Выберите группу ресурсов, содержащую функцию.
5. Выберите развёрнутое приложение-функцию.
6. Выберите **log\_ingest** на вкладке **Functions**.
7. Выберите **Code + Test** в меню **Developer** слева.
8. Откройте раскрывающийся список выбора файла (по умолчанию выбран `main.py`).
9. Выберите `version.txt`.
10. Откройте файл для просмотра текущей развёрнутой версии.

## Руководство по масштабированию

Рекомендуемый способ увеличения пропускной способности по умолчанию (70 МБ/мин): перейдите на более высокий App Service plan, увеличьте число экземпляров App Service, увеличьте `FUNCTIONS_WORKER_PROCESS_COUNT` (по умолчанию 1), увеличьте `NUMBER_OF_CONCURRENT_SEND_CALLS` (по умолчанию 2). Параметры `FUNCTIONS_WORKER_PROCESS_COUNT` и `NUMBER_OF_CONCURRENT_SEND_CALLS` можно добавить как **New application setting** в Azure Portal (**Azure function** > **Configuration** > **New application setting**).

Обратите внимание, что производительность log forwarder может варьироваться в зависимости от содержимого журналов (размера и сложности обработки).

| **Максимальная пропускная способность** | **App Service Plan** | **Число экземпляров** | **Конфигурация** |
| --- | --- | --- | --- |
| до `70 МБ/мин` (до 4 ГБ/ч) | `S1` | `1` | без конфигурации |
| до `580 МБ/мин` (до 32 ГБ/ч) | `P1V3` | `1` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 4, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |
| до `1 ГБ/мин` (до 60 ГБ/ч) | `P2V3` | `1` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 8, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |
| до `2,3 ГБ/мин` (до 138 ГБ/ч) | `P2V3` | `3` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 8, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |

В крайнем случае выполните горизонтальное масштабирование: разверните дополнительные интеграции и распределите нагрузку журналов между разными экземплярами Event Hubs.

## Удаление Azure log forwarding

Удаление Dynatrace Azure log forwarder

1. В Azure Portal перейдите в группу ресурсов, использовавшуюся при установке.
2. Отфильтруйте ресурсы по тегу.

   Скрипт развёртывания помечает все созданные ресурсы тегом `LogsForwarderDeployment = <your_deployment_name>`.
3. Удалите ресурсы.

## Связанные темы

* [Интеграции с Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода в Azure с помощью OneAgent или OpenTelemetry.")
* [Устранение неполадок Azure Log Forwarder](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)