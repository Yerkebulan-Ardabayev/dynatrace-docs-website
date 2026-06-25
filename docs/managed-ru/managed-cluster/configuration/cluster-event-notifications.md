---
title: Уведомления о событиях кластера
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/cluster-event-notifications
scraped: 2026-05-12T11:53:00.554794
---

# Уведомления о событиях кластера

# Уведомления о событиях кластера

* Updated on Oct 07, 2025

В кластере Dynatrace Managed можно управлять следующими уведомлениями:

* **Недостаточно дискового пространства на узле кластера**  
  Срабатывает, когда на дисковом разделе узла кластера свободного места меньше, чем требуется для данного типа хранилища. В таком случае необходимо расширить диск или пересмотреть настройки кластера. В противном случае срок хранения данных может быть сокращён.
* **Недостаточно оборудования на узле кластера**  
  Срабатывает, когда у узла кластера не хватает ядер CPU и оперативной памяти для соответствия рекомендуемым требованиям. Подробнее см. в разделе [Требования к оборудованию](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").
* **Хранилище метрик превышает поддерживаемый размер (4 ТиБ)**  
  Срабатывает, когда хранилище метрик для узла кластера слишком велико. В таком случае необходимо пересмотреть настройки мониторинга или добавить дополнительные узлы в кластер.
* **Сокращение срока хранения в хранилище транзакций**  
  Срабатывает, когда срок хранения данных был автоматически уменьшен для размещения новых данных. В таком случае рекомендуется скорректировать целевое время хранения, пересмотреть настройки мониторинга или расширить диск.
* **Активность Adaptive Load Reduction**  
  Срабатывает, когда узел кластера считается перегруженным и не справляется с обработкой входящих запросов. В таком случае необходимо пересмотреть настройки мониторинга или увеличить количество ядер CPU и объём RAM на узле кластера. Подробнее см. в разделе [Adaptive Traffic Management для Dynatrace Managed](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed#alr "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").
  Настройка параметров уведомлений о событиях кластера

Для работы с [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") и управления уведомлениями о событиях кластера выполните следующие действия:

* [Аутентификация](#authentication-token-authentication)
* [Настройка email-уведомлений](#configure-email-notifications-config-emails)
* [Чтение схемы конфигурации](#read-configuration-schema-read-config-schema)
* [Чтение текущей конфигурации](#read-current-configuration-read-current-config)
* [Создание объекта настроек уведомлений](#create-notification-settings-object-create-settings-object)
* [Обновление настроек уведомлений](#update-notification-settings-update-settings-object)
* [Удаление настроек уведомлений](#delete-notification-settings-delete-settings-object)
* [События кластера и email-уведомления](#cluster-events-and-email-notifications-cluster-notifications-reference)

## Аутентификация

Для создания токена кластера с областями доступа **Write settings** и **Read settings**

1. Перейдите в **Settings** > **API tokens**.
2. В разделе **Cluster tokens** выберите **Generate token**.
3. Введите имя токена и задайте области доступа **Write settings** и **Read settings** для токена Cluster API.
4. Нажмите **Save**, затем **Copy** и сохраните токен в надёжном месте.

## Настройка email-уведомлений

Для отправки конфигурации в виде JSON-payload используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication):

```
[



{



"schemaId": "builtin:cluster-events-notification-settings",



"scope": "cluster",



"value": {



"insufficientDiskSpace": {



"sendEmail": true



},



"insufficientHardware": {



"sendEmail": true



},



"insufficientMetricStorage": {



"sendEmail": false



},



"transactionStorageTruncation": {



"sendEmail": false



},



"adaptiveLoadReductionActivated": {



"sendEmail": false



}



}



}



]
```

## Чтение схемы конфигурации

Чтобы узнать JSON-формат, необходимый для отправки конфигурации, используйте конечную точку [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication). Идентификатор схемы конфигурации (`schemaId`) — `builtin:cluster-events-notification-settings`.

Подробности схемы ответа

```
{



"dynatrace": "1",



"schemaId": "builtin:cluster-events-notification-settings",



"displayName": "Cluster events notification settings",



"description": "Configuration of emails notifications for cluster events.",



"documentation": "Email notifications are sent to recipients defined in Settings - Emails - Email notifications.",



"version": "0",



"multiObject": false,



"maxObjects": 1,



"allowedScopes": [



"cluster"



],



"enums": {},



"types": {



"SingleEventSettings": {



"version": "0",



"versionInfo": "",



"displayName": "Single event settings",



"summaryPattern": "",



"description": "Settings for a single cluster event",



"documentation": "",



"properties": {



"sendEmail": {



"displayName": "Send email",



"description": "",



"documentation": "",



"type": "boolean",



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT",



"default": true



}



},



"type": "object"



}



},



"properties": {



"insufficientDiskSpace": {



"displayName": "Insufficient disk space on a cluster node",



"description": "Triggered when a disk partition on a cluster node has less disk space than required for a given storage type. In that case, you need to extend your disk or review cluster settings. Otherwise, data retention might be reduced.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"insufficientHardware": {



"displayName": "Insufficient hardware on a cluster node",



"description": "Triggered when a cluster node doesn't have enough CPU cores and RAM to meet recommended requirements.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"insufficientMetricStorage": {



"displayName": "Metrics storage exceeds supported size (4TiB)",



"description": "Triggered when Metrics storage a cluster node is too high. In that case, you need to review your monitoring settings or add additional nodes to the cluster.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"transactionStorageTruncation": {



"displayName": "Transaction storage retention period truncation",



"description": "Triggered when data retention has been automatically reduced to store new data. In that case, it is recommended to adjust target retention time, review monitoring settings or extend a disk.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"adaptiveLoadReductionActivated": {



"displayName": "Adaptive Load Reduction activity",



"description": "Triggered when a cluster node has been considered as overloaded and not able to keep up with processing incoming requests. In that case, you need to review monitoring settings or increase CPU cores and RAM on the cluster node.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



}



}



}
```

## Чтение текущей конфигурации

Для проверки текущей конфигурации используйте конечную точку [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") (`/api/cluster/v2/settings/objects?schemaIds=builtin:cluster-events-notification-settings&scopes=cluster`) с токеном кластера, имеющим соответствующие [области доступа](#token-authentication).

* Если эти настройки ранее изменялись, список items содержит один объект. Используйте `objectId` из списка для последующих обновлений.
* Если список items пуст, применяется значение по умолчанию (не отображается в Dynatrace API):

  ```
  {



  "value": {



  "insufficientDiskSpace": {



  "sendEmail": true



  },



  "insufficientHardware": {



  "sendEmail": true



  },



  "insufficientMetricStorage": {



  "sendEmail": true



  },



  "transactionStorageTruncation": {



  "sendEmail": false



  },



  "adaptiveLoadReductionActivated": {



  "sendEmail": false



  }



  }



  }
  ```

## Создание объекта настроек уведомлений

Для создания объекта настроек уведомлений о событиях кластера используйте конечную точку [POST objects](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication). Используйте ID созданного объекта (настроек уведомлений) для последующих обновлений.

Пример создания объекта настроек уведомлений

В данном примере с помощью вызова `POST` к конечной точке `/api/cluster/v2/settings/objects` и схемы `builtin:cluster-events-notification-settings` создаётся объект настроек уведомлений в параметрах кластера:

```
[



{



"schemaId": "builtin:cluster-events-notification-settings",



"scope": "cluster",



"value": {



"insufficientDiskSpace": {



"sendEmail": true



},



"insufficientHardware": {



"sendEmail": true



},



"insufficientMetricStorage": {



"sendEmail": false



},



"transactionStorageTruncation": {



"sendEmail": false



},



"adaptiveLoadReductionActivated": {



"sendEmail": false



}



}



}



]
```

## Обновление настроек уведомлений

После создания объекта настроек уведомлений существует два способа обновления настроек уведомлений о событиях кластера. В обоих случаях убедитесь, что у вас есть токен кластера с соответствующими [областями доступа](#token-authentication).

* Можно использовать тот же метод `POST`, что применялся при создании объекта настроек ([Создание объекта настроек уведомлений](#create-settings-object)). Схема не допускает дублирование объектов настроек, поэтому при попытке создать новый объект настроек существующий будет перезаписан.
* Можно изменить существующий объект настроек, выполнив вызов `PUT` API к конечной точке `/api/cluster/v2/settings/objects/<objectId>` и передав `objectId`, полученный при создании объекта настроек уведомлений.

  Пример обновления объекта настроек уведомлений

  Выполните вызов `PUT` API к `/api/cluster/v2/settings/objects/<objectId>`

  ```
  {



  "value": {



  "insufficientDiskSpace": {



  "sendEmail": true



  },



  "insufficientHardware": {



  "sendEmail": true



  },



  "insufficientMetricStorage": {



  "sendEmail": false



  },



  "transactionStorageTruncation": {



  "sendEmail": false



  },



  "adaptiveLoadReductionActivated": {



  "sendEmail": false



  }



  }



  }
  ```

## Удаление настроек уведомлений

Можно удалить существующий объект настроек уведомлений, выполнив вызов [`DELETE`](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") API к конечной точке `/api/cluster/v2/settings/objects/<objectId>` (с токеном кластера, имеющим соответствующие [области доступа](#token-authentication)) и передав `objectId`, полученный при создании объекта настроек уведомлений. После удаления объекта поведение уведомлений возвращается к значениям по умолчанию: все уведомления отправляют письмо настроенным получателям.

## События кластера и email-уведомления

В таблице ниже приведены типы событий кластера, соответствующие уровни серьёзности и сведения о том, отправляются ли уведомления — по электронной почте или непосредственно в Mission Control.

| Тип | Серьёзность | Описание | Email-уведомление | Уведомление в MC |
| --- | --- | --- | --- | --- |
| `ACTIVE_GATE_TOKENS` | WARNING | "ActiveGate Token(s) will expire soon." | Да | Нет |
| `CASSANDRA` | WARNING | "Cassandra node connection lost (`%d` times in the last hour)." | Нет | Да |
|  | WARNING / INFO | "Cassandra node connection `ADDED/LOST/REACTIVATED`, host ." | Нет | Да |
|  | INFO | "Cassandra node connection added (`%d` times in the last hour)." | Нет | Да |
|  | INFO | "Cassandra node connection reestablished (`%d` times in the last hour)." | Нет | Да |
| `CLUSTER_LIFECYCLE` | SEVERE | "License `'%s'` will expire within one day." | Да | Да |
|  | SEVERE | "License `'%s'` has expired." | Да | Да |
|  | SEVERE | "Your Dynatrace Managed cluster node `{0}` is undersized!" | Настраиваемо [1](#fn-1-1-def) | Да |
|  | SEVERE | "Storage volume for Dynatrace Managed log files is running out of space on `{0}`." | Да | Да |
|  | SEVERE | "Your Dynatrace Managed cluster should be scaled-out!" | Да | Да |
|  | SEVERE | "Could not detect `%s` activity on `%s%s`." | Нет | Да |
|  | SEVERE | "Insufficient system privileges on `%s`." | Нет | Да |
|  | SEVERE | "Update your Cluster `ActiveGate{0}` immediately. You're using `{1}` `ActiveGate{0}` that `{2}` no longer supported!" | Да | Да |
|  | SEVERE | "Post-Update data migration failed, please contact Dynatrace Support." | Нет | Да |
|  | SEVERE | "Dynatrace update `%s` download failed." | Нет | Да |
|  | SEVERE | "Cassandra backup problem." | Нет | Да |
|  | SEVERE | "Dynatrace Managed has stopped collecting monitored data…" | Нет | Да |
|  | SEVERE | "SSL certificate expired." | Нет | Да |
|  | SEVERE | "License `'%s'` is inactive. Until it is done, you cannot set up any monitoring. Activate your license on Licensing page." | Нет | Да |
|  | SEVERE | "Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security." | Нет | Да |
|  | SEVERE | "Failed to import metadata file `%s`." | Нет | Да |
|  | SEVERE | "Default cluster features were changed for non-gov license." | Нет | Да |
|  | SEVERE | "Cluster traffic control: OneAgent monitoring was disabled on recently connected hosts to avoid cluster overload." | Нет | Да |
|  | WARNING / SEVERE | "Host is down." | Да | Да |
|  | WARNING / SEVERE | "ElasticSearch backup problem." | Нет | Да |
|  | WARNING / SEVERE | "Cluster `'%s'` (`'%s'`) update failed." | Нет | Да |
|  | WARNING | "WebUI nodes settings change failed." | Нет | Да |
|  | WARNING | "LDAP connection error." | Да | Да |
|  | WARNING | "Upcoming update to version `%s` is suspended for the cluster `'%s'` (`'%s'`)." | Да | Да |
|  | WARNING | "Node is down - `%s`." | Да, если произошло за пределами процедуры обновления | Да |
|  | WARNING | "There is lack of connection to Dynatrace Mission Control." | Да | Да |
|  | WARNING | "Backup has been disabled because the configuration is no longer supported." | Да | Да |
|  | WARNING | "Fetching OAuth client credentials failed with status code `{0}`." | Нет | Да |
|  | WARNING | "Cluster `'%s'` (`'%s'`) failed to determine update status." | Нет | Да |
|  | WARNING | "Self monitoring download failed on cluster `'%s'`." | Нет | Да |
|  | WARNING | "License check error." | Нет | Да |
|  | WARNING | "SSL certificate (`%s`) refresh failed." | Нет | Да |
|  | WARNING | "Login failed." | Нет | Да |
|  | WARNING | "Not all tenants from MultiTenant-ActiveGate `%s` are configured with AuthTokens." | Нет | Да |
|  | WARNING | "Let's Encrypt SSL certificate fetching failure." | Нет | Да |
|  | WARNING | "Your SSL certificate will expire soon." | Нет | Да |
|  | WARNING | "Login failed." | Нет | Да |
|  | WARNING | "User welcome e-mail was not sent." | Нет | Да |
|  | WARNING | "The Snyk vulnerability feed import failed." | Нет | Да |
|  | WARNING | "The NVD CVE vulnerability feed import failed." | Нет | Да |
|  | WARNING | "LDAP connection problems." | Нет | Да |
|  | WARNING / INFO | "Oidc signature check." | Нет | Да |
|  | WARNING / INFO | "Billing archive has been successfully downloaded/downloaded with warning/failed." | Нет | Да |
|  | INFO | "WebUI nodes settings changed successfully." | Нет | Да |
|  | INFO | "Scheduled update has been resumed for the cluster `'%s'` (`'%s'`)." | Да | Да |
|  | INFO | "Hardware recommendation are fulfilled on `{0}`." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | INFO | "Storage space for Dynatrace Managed log files is sufficient on `{0}`." | Да | Да |
|  | INFO | "Cluster meets the minimum requirement for the number of nodes." | Да | Да |
|  | INFO | "Node is up - `%s`." | Да | Да |
|  | INFO | "Host is up." | Да | Да |
|  | INFO | "Connection to Dynatrace Mission Control is back again." | Да | Да |
|  | INFO | "`<processName>` is up on `<hostName>`." | Нет | Да |
|  | INFO | "Node was restored on ." | Нет | Да |
|  | INFO | "Dynatrace update `%s` was successfully downloaded." | Нет | Да |
|  | INFO | "Cluster `'%s'` (`'%s'`) started updating." | Нет | Да |
|  | INFO | "Cluster update download finished." | Нет | Да |
|  | INFO | "Cluster `'%s'` update to version `%s` finished." | Нет | Да |
|  | INFO | "Request for remote access." | Нет | Да |
|  | INFO | "Successful login to DebugUI." | Нет | Да |
|  | INFO | "SSL certificate (`%s`) refresh succeeded." | Нет | Да |
|  | INFO | "Let's Encrypt SSL certificate fetching succeeded." | Нет | Да |
|  | INFO | "Cluster `'%s'` configuration database initialized successfully." | Нет | Да |
|  | INFO | "Server `%d` joined cluster `'%s'` (`'%s'`)." | Нет | Да |
|  | INFO | "Server `%d` left cluster `'%s'` (`'%s'`)." | Нет | Да |
|  | INFO | "Server `%d` joined cluster `'%s'` (`'%s'`) `%d` times last hour." | Нет | Да |
|  | INFO | "Server `%d` left cluster `'%s'` (`'%s'`) `%d` times last hour." | Нет | Да |
|  | INFO | "Successful login." | Нет | Да |
|  | INFO | "The third-party vulnerability feeds version `%s` were successfully imported into the cluster's Dynatrace Application Security." | Нет | Да |
|  | INFO | "Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security." | Нет | Да |
| `CLUSTER_RUNTIME_SETTING` | SEVERE | "Responsibility cluster nodes override set on node: `%d`." | Нет | Да |
| `CONFIGURATION_AUDIT` | INFO | "Min Agent Version updated to `%d` by Session Replay." | Нет | Да |
|  | INFO | "Session State Version updated to `v%d` by Session Replay." | Нет | Да |
| `ELASTICSEARCH` | INFO | "Elasticsearch storage service on your Dynatrace Managed cluster might be overloaded!" | Нет | Да |
| `ERROR` | WARNING | "ElasticSearch update transient settings failed." | Нет | Да |
|  | INFO | "ElasticSearch update transient settings succeeded." | Нет | Да |
| `LOG_EVENT_DROP` | WARNING | "Ingested log data is trimmed." | Нет | Да |
|  | WARNING | "Log ingest queue is full." | Нет | Да |
|  | WARNING | "Elasticsearch log queue is full." | Нет | Да |
|  | WARNING | "Elasticsearch log storing failed." | Нет | Да |
| `MANAGED_INTERNAL` | INFO | "Internal: Cassandra has old files." | Нет | Да |
| `MANAGED_NODE_ADD` | WARNING | "Adding new node is taking more than expected." | Нет | Да |
|  | INFO | "Adding new node operation has been started." | Нет | Да |
|  | INFO | "Adding new node precondition check status." | Нет | Да |
|  | INFO | "Adding new node finished successfully." | Нет | Да |
|  | WARNING | "Adding new node failure." | Нет | Да |
| `MANAGED_NODE_REMOVAL` | WARNING | "Node removal finished with error `%s` (id=`%d`)." | Нет | Да |
|  | INFO | "Node removal operation is not allowed `%s` (id=`%d`)." | Нет | Да |
|  | INFO | "Node removal process started successfully `%s` (id=`%d`)." | Нет | Да |
|  | INFO | "Node removal process started successfully `%s`." | Нет | Да |
|  | INFO | "Node removal finished successfully." | Нет | Да |
|  | INFO | "Node removal failure." | Нет | Да |
| `SECURITY_GATEWAY_LIFECYCLE` | INFO | "ActiveGate (host=`%s`) registered on cluster." | Нет | Да |
|  | INFO | "ActiveGate (host=`%s`) unregistered on cluster." | Нет | Да |
|  | INFO | "ActiveGate (host=`%s`) lost connection to cluster." | Нет | Да |
|  | INFO | "ActiveGate (environment=`%s`, host=`%s`) registered on cluster." | Нет | Да |
|  | INFO | "ActiveGate (environment=`%s`, host=`%s`) unregistered on cluster." | Нет | Да |
|  | INFO | "ActiveGate (environment=`%s`, host=`%s`) lost connection to cluster." | Нет | Да |
| `SERVER_LIFECYCLE` | SEVERE | "Transaction storage retention period truncated." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | SEVERE | "Insufficient disk space on `%s` on `%s`." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | SEVERE | "Long-term Metrics Store size exceeds the maximum acceptable 4 TB on `%s`." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | SEVERE | "`<component name>` is down." | Нет | Да |
|  | SEVERE | "Heap memory: Server `%d` started memory emergency mode." | Нет | Да |
|  | SEVERE | "Heap memory: Server `%d` triggered a hard memory cleanup action." | Нет | Да |
|  | SEVERE | "A cluster node can't receive OneAgent traffic." | Нет | Да |
|  | WARNING | "Server `%d` activated Adaptive Load Reduction." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | WARNING | "Long-term Metrics Store size exceeds recommended 2 TB on `%s`." | Нет | Да |
|  | WARNING | "Node cannot read and write to directory: `'%s'`." | Нет | Да |
|  | WARNING | "Heap memory: Server `%d` triggered a soft memory cleanup action." | Нет | Да |
|  | WARNING / INFO | "Disabling OneAgent traffic at " | Нет | Да |
|  | WARNING / INFO | "Enabling OneAgent traffic at " | Нет | Да |
|  | INFO | "Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | INFO | "Server `%d` deactivated Adaptive Load Reduction." | Настраиваемо [1](#fn-1-1-def) | Да |
|  | INFO | "Server `%d` shutdown initiated." | Нет | Да |
|  | INFO | "`<component name>` is up." | Нет | Да |
|  | INFO | "Server `%d` startup completed. (Version: `%s`)." | Нет | Да |
|  | INFO | "Heap memory: Server `%d` ended memory emergency mode." | Нет | Да |
|  | ? | "Server time of server `%d` is out of sync. Time difference `%d` milliseconds. Please enable NTP on all cluster nodes." | Нет | Да |
| `TENANT_LIFECYCLE` | SEVERE | "Trial environment expired." | Нет | Да |
|  | SEVERE | "The node with id `%s` is not properly configured." | Нет | Да |
|  | SEVERE | "Environment `'%s'` with id `%s` failed to start on server `%d`. See server logs for details." | Нет | Да |
|  | INFO | "Environment `'%s'` with id `%s` created." | Нет | Да |
|  | INFO | "Environment `'%s'` with id `%s` updated." | Нет | Да |
|  | INFO | "Environment `'%s'` with id `%s` removed." | Нет | Да |

1

«Настраиваемо» означает, что уведомления можно настраивать через Settings API. Идентификатор настройки: `builtin:cluster-events-notification-settings`. Для использования этого REST API необходимо авторизоваться с помощью токена с разрешениями `settings.read` и `settings.write`.