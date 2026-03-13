---
title: Логи Azure
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure
scraped: 2026-03-06T21:17:36.115344
---

# Логи Azure

# Логи Azure

* Последняя версия Dynatrace
* Практическое руководство
* 17 минут чтения
* Обновлено 17 октября 2025 г.

Потребление DDU для Log Monitoring

Ценообразование DDU применяется к облачному Log Monitoring. Подробности см. в разделе [DDU для Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

Перенаправление логов Azure позволяет передавать логи Azure из Azure Event Hubs в логи Dynatrace через экземпляр Azure Function App. Поддерживаются логи ресурсов Azure, логи активности и логи входа Entra ID.

## Ресурсы для развёртывания

Перенаправление логов Azure выполняется непосредственно через Cluster API. Если вы не хотите использовать прямой приём через Cluster API, необходимо использовать существующий ActiveGate для приёма логов.

В результате развёртывания инструмента перенаправления логов Azure создаются следующие ресурсы:

* Учётная запись хранения (`Microsoft.Storage/storageAccounts`)
* Служба BLOB-объектов учётной записи хранения (`Microsoft.Storage/storageAccounts/blobServices`)
* План Azure App Service (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Инструмент перенаправления логов Azure по умолчанию использует функцию Azure на базе Linux. Функция на базе Windows не поддерживается.

Подробности о созданных ресурсах см. в [файле Azure Resource Manager на GitHub](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json).

## Ограничения

Логи старше 24 часов отклоняются (считаются устаревшими конечной точкой приёма логов Dynatrace), поэтому рекомендуется не устанавливать время хранения Azure Event Hubs более 24 часов.

Инструмент перенаправления логов Azure поддерживает максимальную скорость 70 МБ в минуту (~4 ГБ в час) в конфигурации по умолчанию. Пропускная способность измеряется с помощью метрики Event Hubs `Outgoing Bytes` для экземпляра концентраторов событий, подключённого к функции. Инструкции по масштабированию см. в разделе [Руководство по масштабированию](#scalingguide).

## Предварительные требования

Ниже приведён список требований для настройки перенаправления логов Azure. Одни требования необходимы до начала развёртывания, другие — в процессе.

### Dynatrace

Если вы используете более раннюю версию Dynatrace, см. раздел [Альтернативные варианты развёртывания](#alternative).

* Dynatrace версии 1.217+

* [Включить универсальный приём логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Передавайте данные логов в Dynatrace через API и позвольте Dynatrace преобразовать их в понятные сообщения логов.")
* [Включить мониторинг логов (последняя версия)](/docs/analyze-explore-automate/logs "Log Management and Analytics обеспечивает единый подход к управлению и изучению данных логов в Dynatrace.")

* [Создать токен API](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях.") и включить разрешение **Ingest logs**. Токен API применяется к обеим версиям.

### Azure

1. В каждом регионе Azure, из которого вы хотите получать логи, [создайте группу ресурсов и настройте экземпляр Azure Event Hubs](https://dt-url.net/8w03rs3).

   Для отправки логов:

   * Экземпляры концентраторов событий и группа ресурсов, в которой будет выполняться развёртывание, должны находиться в одном регионе.
   * Убедитесь, что в пространстве имён концентраторов событий в разделе **Публичный доступ** > **Доступ к публичной сети** параметр **Отключено** НЕ выбран. В противном случае логи не будут отправляться в Dynatrace.
2. Создайте правило авторизации с разрешением **listen** для экземпляра концентраторов событий, настроенного для получения логов:

   ```
   az eventhubs eventhub authorization-rule create --resource-group <your_resource_group> --namespace-name <your_event_hub_namespace> --eventhub-name <your_event_hub_instance> --name <authorization_rule_name> --rights Listen
   ```
3. Получите строку подключения концентраторов событий для созданного выше правила авторизации:

   ```
   az eventhubs eventhub authorization-rule keys list --resource-group <your_resource_group> --namespace-name <your_event_hub_namespace> --eventhub-name <your_event_hub_instance> --name <your_authorization_rule_name>
   ```
4. Настройте [параметры диагностики](https://dt-url.net/se83r02) для передачи как логов ресурсов, так и логов входа Entra ID в экземпляры Azure Event Hub.

### CLI

Развёртывание перенаправления логов Azure можно выполнить с помощью Azure Portal Cloud Shell (Bash) или с любой машины с установленным [Azure CLI](https://dt-url.net/cf63rl6) и оболочкой Bash (Linux или Windows WSL).

## Развёртывание

1. Задайте следующие переменные среды, заменив заполнители (`<...>`) своими значениями.

   * Для `DEPLOYMENT_NAME` введите имя развёртывания длиной от 3 до 20 символов. Можно использовать строчные буквы и цифры.

     **Примечание:** Имя должно быть глобально уникальным — оно добавляется к именам создаваемых ресурсов Azure.

* Для `TARGET_URL` введите URL вашей среды: `https://<your_environment_ID>.live.dynatrace.com`. Чтобы узнать, как определить идентификатор среды для развёртывания SaaS, см. [идентификатор среды](/docs/discover-dynatrace/get-started/monitoring-environment "Понимание и работа со средами мониторинга.").

* Для `TARGET_API_TOKEN` введите ваш токен API. Подробности см. в разделе [Требования Dynatrace](#dynatrace).
* Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробности см. в разделе [Требования Azure](#azure).
* Для `EVENT_HUB_CONNECTION_STRING` введите строку подключения для экземпляров Azure Event Hubs, настроенных для получения логов. Подробности см. в разделе [Требования Azure](#azure).

Опционально Вы можете включить [самомониторинг](#sfm) и/или [фильтрацию логов](#filter) во время или после развёртывания.

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

## Просмотр логов Azure

После развёртывания скрипта вы можете просматривать и анализировать логи Azure в Dynatrace:
Перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** и в фильтре атрибутов выполните поиск по **Azure**.

* Если логи поступают, значит инструмент перенаправления логов Azure успешно развёрнут.
* Если в течение 10 минут логи не поступают, ознакомьтесь с разделом руководства **Проверка**.

Вы можете использовать [DQL](/docs/platform/grail/dynatrace-query-language "Как использовать язык запросов Dynatrace.") для фильтрации логов Azure.
В качестве примера можно добавить следующую строку в запрос DQL:

```
fetch logs



| filter matchesValue(dt.openpipeline.source, "/api/v2/logs/ingest") AND matchesValue(cloud.provider, "Azure")



| sort timestamp desc
```

Если у вас уже настроено несколько интеграций, вы можете дополнительно использовать значения `cloud.log_forwarder` и `dt.auth.origin` для уточнения фильтров.

## Самомониторинг (опционально)

Самомониторинг позволяет быстро диагностировать, правильно ли ваша функция обрабатывает и отправляет логи в Dynatrace.

### Включение самомониторинга

Для включения самомониторинга есть два варианта:

* **Во время развёртывания:** Установите параметр [`--enable-self-monitoring`](#par) (или [переменную среды `SFM_ENABLED`](#var)) в значение `true`.
* **После развёртывания:** В портале Azure перейдите в конфигурацию развёрнутого экземпляра Function App и установите `SELF_MONITORING_ENABLED` в значение `true`.

Включение управляемого удостоверения

После включения самомониторинга необходимо включить [управляемое удостоверение](https://dt-url.net/qj23rie) для экземпляра Function App, созданного во время развёртывания, и настроить его для разрешения отправки метрик в ресурс.

Настройка управляемого удостоверения

1. В портале Azure перейдите в раздел **Настройки** вашего экземпляра Function App, созданного во время развёртывания, и выберите **Идентификатор**.
2. Выберите **Да** для **Включить управляемое удостоверение, назначенное системой**.
3. Перейдите в группу ресурсов, где развёрнут Function App, и выберите **Управление доступом (IAM)**.
4. Нажмите **Добавить** для добавления назначения роли.
5. Установите роль **Monitoring Metrics Publisher**.
6. Нажмите **Сохранить** для сохранения конфигурации.

### Метрики самомониторинга

После включения самомониторинга вы можете просматривать следующие метрики в пространстве имён `dynatrace_logs_self_monitoring` вашего нового экземпляра Function App.

| Название метрики | Описание | Измерение |
| --- | --- | --- |
| `all_requests` | Все запросы, отправленные в Dynatrace. |  |
| `dynatrace_connectivity_failures` | Фиксируется при возникновении проблем с подключением к Dynatrace. | `connectivity_status` |
| `parsing_errors` | Фиксируется при возникновении ошибок синтаксического анализа в процессе обработки логов. |  |
| `processing_time` | Время, необходимое для обработки всех логов. |  |
| `sending_time` | Время, необходимое для отправки всех запросов. |  |
| `too_long_content_size` | Фиксируется, когда содержимое лога слишком длинное. Содержимое будет усечено. |  |
| `too_old_records` | Фиксируется, когда логи, полученные из Event Hubs, устарели. |  |

## Фильтрация логов (опционально)

Для уменьшения количества логов, отправляемых в Dynatrace, можно применять фильтры.
Для применения фильтров есть два варианта:

* **Во время развёртывания:** Установите переменную среды `FILTER_CONFIG` в Azure Portal Cloud Shell (Bash) перед запуском скрипта развёртывания.

  1. Добавьте переменную среды `FILTER_CONFIG` в список переменных среды для скрипта развёртывания.

     Обязательно замените заполнители своими значениями. Подробности о параметрах фильтра см. в разделе [Параметры фильтра](#options).

     ```
     FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>;FILTER.GLOBAL.CONTAINS_PATTERN=<pattern>;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>;FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<pattern>;FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>;FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<pattern>"
     ```
  2. Задайте переменные среды.
  3. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.
* **После развёртывания:** Добавьте `FILTER_CONFIG` в портале Azure.

  1. В портале Azure перейдите в **Переменные среды** вашего развёрнутого экземпляра Function App.
  2. В разделе **Настройки приложения** найдите и выберите **FILTER\_CONFIG**.

     **FILTER\_CONFIG** появится в Azure после запуска скрипта развёртывания.
  3. Нажмите **Изменить** для добавления **значения** фильтра.

     Пример редактирования

     ![Редактирование](https://dt-cdn.net/images/image-36-3759-7bc37dfe3c.png)

     Альтернативно можно нажать **Расширенное редактирование** для ввода значения в JSON.

     Пример расширенного редактирования

     ![Расширенное](https://dt-cdn.net/images/image-37-3804-dffe41ec79.png)
  4. Нажмите **OK**.
  5. Перезапустите экземпляр Function App.

### Параметры фильтра

`FILTER_CONFIG` — переменная в формате пар ключ-значение. Можно задать два типа фильтров (`MIN_LOG_LEVEL` и/или `CONTAINS_PATTERN`) для трёх групп фильтров (`GLOBAL`, `RESOURCE_TYPE` и/или `RESOURCE_ID`).

#### Тип фильтра: `MIN_LOG_LEVEL`

Этот тип фильтра позволяет отфильтровать логи с нежелательными уровнями. Возможные уровни логов:

* **Critical** (или `1`)
* **Error** (или `2`)
* **Warning** (или `3`)
* **Informational** (или `4`)

Пример:
`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Warning"`
В приведённом примере логи уровня **Informational** будут пропускаться, а в Dynatrace будут отправляться только логи уровней **Warning**, **Error** и **Critical**.

Варианты синтаксиса:

* `FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>`
* `FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>`
* `FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>`

Можно задать один глобальный фильтр и дополнительные фильтры для конкретного типа/идентификатора ресурса.

Пример:
`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Error;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.MICROSOFT.WEB/SITES=Informational"`
В приведённом примере все логи из экземпляров с типом ресурса `MICROSOFT.WEB/SITES` будут отправляться в Dynatrace, тогда как для всех остальных ресурсов логи уровней **Informational** и **Warning** будут отфильтрованы.

#### Тип фильтра: `CONTAINS_PATTERN`

Этот тип фильтра позволяет собирать логи, содержащие определённый текст. Используется fnmatch с поддержкой подстановочных знаков в стиле Unix. Подробности см. в документации по [сопоставлению шаблонов имён файлов Unix](https://docs.python.org/3/library/fnmatch.html).

Варианты синтаксиса:

* `FILTER.GLOBAL.CONTAINS_PATTERN=<log_pattern>`
* `FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<log_pattern>`
* `FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<log_pattern>`

#### Группа фильтров: `GLOBAL`

Этот фильтр применяется ко всем логам.

#### Группа фильтров: `RESOURCE_TYPE`

Этот фильтр применяется только к логам, поступающим из ресурсов заданного типа ресурсов Azure, например `Microsoft.Compute/virtualMachines`.

Тип ресурса можно найти в портале Azure, в разделе **Свойства** вашего ресурса.

Если поле **Тип** не отображается в разделе **Свойства**, его можно извлечь из строки идентификатора ресурса.

Синтаксис строки идентификатора ресурса:
`/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/<resourceType>/<resourceName>`
Тип ресурса — это часть между `/providers/` и `/resourceName/`.

#### Группа фильтров: `RESOURCE_ID`

Этот фильтр применяется только к логам, поступающим из конкретного ресурса, идентифицированного по идентификатору ресурса Azure.

Идентификатор ресурса можно найти в портале Azure, в разделе **Свойства** вашего ресурса.

### Правила фильтров

* Если для одной группы заданы два типа фильтров, оба условия должны выполняться, то есть второй фильтр должен соответствовать первому.

  Например, если вы задали `MIN_LOG_LEVEL` в значение **Warning** и `CONTAINS_PATTERN` в значение `<some_important_message>`, вы получите только логи уровня **Warning**, содержащие `<some_important_message>`, а все остальные предупреждения без этого конкретного сообщения будут отфильтрованы.
* Если для одной группы задан один тип фильтра, а для другой группы — другой тип фильтра, два условия не перекрываются.

  Например, если вы задали `MIN_LOG_LEVEL` в значение **Warning** для `GLOBAL` и `CONTAINS_PATTERN` в значение `<some_important_message>` для `RESOURCE_TYPE`, вы получите все логи уровней **Warning**, **Error** и **Critical** из `GLOBAL`, а также все логи, содержащие `<some_important_message>`, из `RESOURCE_TYPE`.
* Если для одной и той же группы (глобальной или типа/идентификатора ресурса) задано более одной пары типов фильтров (`MIN_LOG_LEVEL` и `CONTAINS_PATTERN`), применяется только последняя пара; все остальные игнорируются.

## Обновление перенаправления логов Azure

Для обновления перенаправления логов Azure

1. Вам понадобится пакет с исходным кодом инструмента перенаправления логов Azure — загрузите последнюю версию Dynatrace.

   ```
   wget https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-log-forwarder.zip
   ```
2. Разверните новую версию, заменив заполнители необходимыми значениями.

   ```
   az webapp deployment source config-zip -g <your_resource_group_name> -n <application_name> --src <zip_file_path>
   ```

Некоторые версии инструмента перенаправления логов Azure включают изменения, требующие полной переустановки. Подробности см. на [странице релизов GitHub](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases).

## Альтернативные варианты развёртывания

### Использование существующего ActiveGate

Если вы не хотите использовать прямой приём через Cluster API, необходимо использовать существующий ActiveGate для приёма логов.

Инструкции приведены ниже.

#### Предварительные требования

Dynatrace версии 1.217+

* [Требования Dynatrace](#dynatrace), перечисленные выше
* [Требования Azure](#azure), перечисленные выше
* [Требования CLI](#cli), перечисленные выше

#### Конфигурация

1. Задайте следующие переменные среды, заменив заполнители (`<...>`) своими значениями.

   * Для `DEPLOYMENT_NAME` введите имя развёртывания (только строчные буквы).
   * Для `TARGET_URL` введите URL API конечной точки вашего ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. Чтобы узнать, как определить идентификатор среды, см. [идентификатор среды](/docs/discover-dynatrace/get-started/monitoring-environment "Понимание и работа со средами мониторинга.").
   * Для `TARGET_API_TOKEN` введите ваш токен API. Подробности см. в предварительных требованиях выше.
   * Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробности см. в разделе [Требования Azure](#azure).
   * Для `EVENT_HUB_CONNECTION_STRING` введите строку подключения для экземпляров Azure Event Hubs, настроенных для получения логов. Подробности см. в разделе [Требования Azure](#azure).
   * Для `USE_EXISTING_ACTIVE_GATE` введите `true`.
   * Опционально Для `REQUIRE_VALID_CERTIFICATE` введите `true` или `false`. Этот параметр указывает инструменту перенаправления логов проверять SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются.

   Опционально Вы можете включить [самомониторинг](#sfm) и/или [фильтрацию логов](#filter) во время или после развёртывания.

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

   Убедитесь, что вы хотите задать другие опциональные параметры. Все параметры в скобках (`[...]`) являются опциональными. Подробности см. в [таблице развёртывания](#table).

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-connection-string $EVENT_HUB_CONNECTION_STRING --require-valid-certificate $REQUIRE_VALID_CERTIFICATE
   ```

### Использование управляемого удостоверения, назначенного пользователем

Существует два типа управляемых удостоверений: назначенные системой и назначенные пользователем. По умолчанию используется управляемое удостоверение, назначенное системой. Если вы предпочитаете использовать управляемое удостоверение, назначенное пользователем, ознакомьтесь с инструкциями ниже.

#### Предварительные требования

Dynatrace версии 1.217+

* [Требования Dynatrace](#dynatrace), перечисленные выше
* [Требования Azure](#azure), перечисленные выше
* [Требования CLI](#cli), перечисленные выше

В дополнение к [требованиям Azure](#azure), перечисленным выше, необходимо создать управляемое удостоверение, назначенное пользователем, в портале Azure.

Добавьте роли для концентраторов событий в управляемое удостоверение, назначенное пользователем. Для привязки триггера концентраторов событий необходимо назначить соответствующие встроенные роли: **Azure Event Hubs Data Receiver** и **Azure Event Hubs Data Owner**.

#### Конфигурация

1. Задайте следующие переменные среды, заменив заполнители (`<...>`) своими значениями.

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

   * Для `DEPLOYMENT_NAME` введите имя развёртывания (только строчные буквы).

* Для `TARGET_URL` введите URL вашей среды: `https://<your_environment_ID>.live.dynatrace.com`. Чтобы узнать, как определить идентификатор среды для развёртывания SaaS, см. [идентификатор среды](/docs/discover-dynatrace/get-started/monitoring-environment "Понимание и работа со средами мониторинга.").

* Для `TARGET_API_TOKEN` введите ваш токен API. Подробности см. в предварительных требованиях выше.
* Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробности см. в разделе [Требования Azure](#azure).
* Для `EVENT_HUB_NAME` введите имя экземпляра Azure Event Hubs, настроенного для получения логов. Подробности см. в разделе [Требования Azure](#azure).
* Опционально Для `REQUIRE_VALID_CERTIFICATE` введите `true` или `false`. Этот параметр указывает инструменту перенаправления логов проверять SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются.
* Для `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` введите `true`. Этот параметр указывает, используется ли управляемое удостоверение, назначенное пользователем, вместо назначенного системой.
* Для `EVENT_HUB_CONNECTION_CLIENT_ID` введите `Client ID` созданного управляемого удостоверения.
* Для `MANAGED_IDENTITY_RESOURCE_NAME` введите имя ресурса созданного управляемого удостоверения.
* Для `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` введите:

  + **Имя хоста** пространства имён концентраторов событий.
  + Пользовательское имя группы потребителей по умолчанию.

Опционально Вы можете включить [самомониторинг](#sfm) и/или [фильтрацию логов](#filter) во время или после развёртывания.

2. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.

   Убедитесь, что вы хотите задать другие опциональные параметры. Все параметры в скобках (`[...]`) являются опциональными. Подробности см. в [таблице развёртывания](#table).

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-name $EVENT_HUB_NAME --require-valid-certificate $REQUIRE_VALID_CERTIFICATE --enable-user-assigned-managed-identity $ENABLE_USER_ASSIGNED_MANAGED_IDENTITY --eventhub-connection-client-id $EVENT_HUB_CONNECTION_CLIENT_ID --managed-identity-resource-name $MANAGED_IDENTITY_RESOURCE_NAME --eventhub-connection-fully-qualified-namespace $EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE --custom-consumer-group $CONSUMER_GROUP
   ```

### Таблица развёртывания

Полный список параметров представлен в таблице развёртывания ниже.

| **Параметр командной строки** | **Переменная среды** | **Описание** |  |
| --- | --- | --- | --- |
| `--deployment-name` | `DEPLOYMENT_NAME` | Обязательный. Имя развёртывания. Только строчные буквы. |  |
| `--target-url` | `TARGET_URL` | Обязательный. Среда Dynatrace, в которой вы хотите настроить универсальный приём логов. |  |
| `--target-api-token` | `TARGET_API_TOKEN` | Обязательный. Ваш токен API. |  |
| `--resource-group` | `RESOURCE_GROUP` | Обязательный. Имя группы ресурсов Azure, в которой будет выполняться развёртывание. |  |
| `--event-hub-connection-string` | `EVENT_HUB_CONNECTION_STRING` | Обязательный. Строка подключения для экземпляра Azure Event Hubs, настроенного для получения логов. (Имя Azure Event Hubs, настроенного для получения логов.) |  |
| `--event-hub-name` | `EVENT_HUB_NAME` | Опциональный по умолчанию. Если в качестве метода аутентификации используется управляемое удостоверение, назначенное пользователем, то Обязательный. |  |
| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Опциональный. Если установлено значение `true`, инструмент перенаправления логов проверяет SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются. |  |
| `--enable-self-monitoring` | `SFM_ENABLED` | Опциональный. Если установлено значение `true`, Dynatrace отправляет пользовательские метрики в Azure. Подробности см. в разделе [Включение самомониторинга](#sfm). По умолчанию пользовательские метрики в Azure не отправляются. |  |
| `--filter-config` | `FILTER_CONFIG` | Опциональный. Применяйте фильтры для уменьшения количества логов, отправляемых в Dynatrace. Подробности см. в разделе [Фильтрация логов](#filter). |  |
| `--tags` | `TAGS` | Опциональный. Применяйте теги Azure к вновь созданным ресурсам в формате пар ключ:значение через запятую (например, `"tag:value,tag2:value2"`). Следующие символы не поддерживаются в ключе тега: `,:<>%&\?/` |  |
| `--enable-user-assigned-managed-identity` | `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` | Опциональный. Если установлено значение `true`, параметры `--eventhub-connection-client-id`, `--managed-identity-resource-name`, `--eventhub-connection-fully-qualified-namespace`, `--event-hub-name` становятся Обязательными. Включает использование управляемого удостоверения, назначенного пользователем, вместо назначенного системой. |  |
| `--custom-consumer-group` | `CONSUMER_GROUP` | Опциональный. Если указано, это значение будет использоваться как имя группы потребителей по умолчанию. Оставьте пустым для применения значения Azure по умолчанию. |  |
| `--eventhub-connection-client-id` | `EVENT_HUB_CONNECTION_CLIENT_ID` | Опциональный. `Client ID` созданного управляемого удостоверения. Пример значения: `d8916c27-4c4r-482o-895b-doe0b48c76f7` |  |
| `--managed-identity-resource-name` | `MANAGED_IDENTITY_RESOURCE_NAME` | Опциональный. Имя ресурса созданного управляемого удостоверения. Пример значения: `test-managed-identity` |  |
| `--eventhub-connection-fully-qualified-namespace` | `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` | Опциональный. `Имя хоста` пространства имён Azure Event Hubs. Пример значения: `sample-eventhub-namespace.servicebus.windows.net` |  |

## Проверка

Для проверки успешности развёртывания в Dynatrace перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** и убедитесь, что присутствует следующая строка лога:

![Строка лога](https://dt-cdn.net/images/screenshot-2022-08-11-at-11-49-52-928-5957a24948.png)

Примерно через 10 минут должны начать поступать дополнительные логи. Если логи не поступают, убедитесь в следующем:

* Экземпляры концентраторов событий и группа ресурсов, в которой выполняется развёртывание, находятся в одном регионе
* Вы точно выполнили шаги по [настройке параметров диагностики](https://dt-url.net/se83r02)

Кроме того, вы можете читать логи функции Azure, в которой выполняется инструмент перенаправления логов Azure. [Включение журналов потокового выполнения в Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/streaming-logs)

Исчерпание портов SNAT: у функций Azure ограничено количество портов, которые можно открыть одновременно (128). На количество открытых соединений влияют количество экземпляров, количество рабочих процессов и количество одновременных вызовов. При достижении лимита см. [руководство по масштабированию](#scalingguide) ниже.

## Проверка версии

Для проверки версии текущего развёрнутого инструмента перенаправления логов Azure

1. Откройте портал Azure и перейдите в раздел **Подписки**.
2. Выберите вашу подписку.
3. Перейдите в **Группы ресурсов**.
4. Выберите группу ресурсов, содержащую функцию.
5. Выберите ваше развёрнутое приложение-функцию.
6. Выберите **log\_ingest** на вкладке **Функции**.
7. В меню **Разработчик** слева выберите **Код + тест**.
8. Выберите раскрывающийся список файлов (по умолчанию выбран `main.py`).
9. Выберите `version.txt`.
10. Откройте файл для проверки текущей развёрнутой версии.

## Руководство по масштабированию

Рекомендуемый способ увеличения пропускной способности по умолчанию (70 МБ/мин) — обновление плана App Service, соответствующее увеличение количества экземпляров App Service, увеличение `FUNCTIONS_WORKER_PROCESS_COUNT` (по умолчанию 1), увеличение `NUMBER_OF_CONCURRENT_SEND_CALLS` (по умолчанию 2). Вы можете добавить `FUNCTIONS_WORKER_PROCESS_COUNT` и `NUMBER_OF_CONCURRENT_SEND_CALLS` как **Новую настройку приложения** в портале Azure (**Функция Azure** > **Конфигурация** > **Новая настройка приложения**).

Обратите внимание, что производительность инструмента перенаправления логов может варьироваться в зависимости от содержимого логов (размер / сложность обработки).

| **Максимальная пропускная способность** | **План App Service** | **Количество экземпляров** | **Конфигурация** |
| --- | --- | --- | --- |
| до `70 МБ/мин` (до 4 ГБ/ч) | `S1` | `1` | без конфигурации |
| до `580 МБ/мин` (до 32 ГБ/ч) | `P1V3` | `1` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 4, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |
| до `1 ГБ/мин` (до 60 ГБ/ч) | `P2V3` | `1` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 8, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |
| до `2,3 ГБ/мин` (до 138 ГБ/ч) | `P2V3` | `3` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 8, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |

В крайнем случае выполните горизонтальное масштабирование: разверните больше интеграций и распределите нагрузку по логам между различными экземплярами концентраторов событий.

## Удаление перенаправления логов Azure

Для удаления инструмента перенаправления логов Dynatrace Azure

1. В портале Azure перейдите в группу ресурсов, использованную для установки.
2. Фильтруйте ресурсы по тегу.

   Скрипт развёртывания помечает все созданные ресурсы тегом `LogsForwarderDeployment = <your_deployment_name>`.
3. Удалите ресурсы.

## Связанные темы

* [Интеграции Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations "Настройте глубокий мониторинг кода Dynatrace на Azure с помощью OneAgent или OpenTelemetry.")
* [Устранение неполадок с инструментом перенаправления логов Azure](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)
