---
title: Настройка уведомлений о событиях кластера
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-event-notifications
---

# Настройка уведомлений о событиях кластера

# Настройка уведомлений о событиях кластера

* Практическое руководство
* Чтение занимает 11 минут
* Обновлено 18 июня 2026 г.

В Managed Cluster можно управлять следующими уведомлениями:

* **Недостаточно места на диске узла Managed Cluster**  
  Срабатывает, когда на дисковом разделе узла Managed Cluster остаётся меньше свободного места, чем требуется для данного типа хранилища. В этом случае нужно расширить диск или пересмотреть настройки кластера. Иначе период хранения данных может сократиться.
* **Недостаточно аппаратных ресурсов узла Managed Cluster**  
  Срабатывает, когда на узле не хватает ядер CPU и оперативной памяти для соответствия рекомендуемым требованиям. Подробнее см. [Системные требования](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").
* **Хранилище метрик превышает поддерживаемый размер (4 ТиБ)**  
  Срабатывает, когда хранилище метрик узла становится слишком большим. В этом случае нужно пересмотреть настройки мониторинга или добавить дополнительные узлы в Managed Cluster.
* **Сокращение периода хранения данных транзакций**  
  Срабатывает, когда период хранения данных был автоматически сокращён для сохранения новых данных. В этом случае Dynatrace рекомендует скорректировать целевое время хранения, пересмотреть настройки мониторинга или расширить диск.
* **Активность Adaptive Load Reduction**  
  Срабатывает, когда узел считается перегруженным и не справляется с обработкой входящих запросов. В этом случае нужно пересмотреть настройки мониторинга или увеличить количество ядер CPU и объём оперативной памяти на узле. Подробнее см. [Adaptive Load Reduction](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed#alr "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").

## Рабочие процессы UI

Используй Cluster Management Console (CMC) для настройки того, кто получает уведомления о событиях кластера и экстренные уведомления.

### Настройка получателей email-уведомлений

Настройка того, кто получает email-уведомления о событиях кластера, в CMC:

1. В CMC перейди в **Settings** > **Emails** > **Email notifications**.
2. В поле **Notifications recipients** укажи адреса электронной почты, которые должны получать уведомления, связанные с кластером, окружением и аккаунтом. Раздели несколько адресов запятыми.
3. Опционально: включи **Also notify all active users with cluster admin rights**.

### Настройка экстренных контактов

Экстренные контакты получают уведомления от экспертов по продуктам Dynatrace в случае катастрофических состояний Managed Cluster или критических уязвимостей безопасности, которые требуют устранения.

1. В CMC перейди в **Settings** > **Emails** > **Email notifications**.
2. На странице **Email notifications**, в разделе **Emergency notifications recipients**, укажи один или несколько адресов электронной почты, разделённых запятыми.
3. Выбери **Save changes**.

## Рабочие процессы API

Используй [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") для настройки того, какие события кластера вызывают email-уведомления, и для управления объектом настроек уведомлений.

[**Аутентификация запросов API**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#token-authentication "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")[**Настройка параметров уведомлений о событиях**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#configure-event-notification-settings "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")[**Чтение схемы конфигурации**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#read-config-schema "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")[**Чтение текущей конфигурации**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#read-current-config "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")[**Создание объекта настроек уведомлений**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#create-settings-object "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")[**Обновление настроек уведомлений**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#update-settings-object "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")[**Удаление настроек уведомлений**](/managed/managed-cluster/configuration/configure-cluster-event-notifications#delete-settings-object "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.")

### Аутентификация запросов API

Чтобы сгенерировать токен кластера с областями доступа **Write settings** и **Read settings**, выполни следующие шаги.

1. Перейди в **Settings** > **API tokens**.
2. В разделе **Cluster tokens** выбери **Generate token**.
3. Введи имя для токена и определи области доступа **Write settings** и **Read settings** для токена API кластера.
4. Нажми **Save**, а затем **Copy**, чтобы сохранить токен в надёжном месте.

### Настройка параметров уведомлений о событиях

Чтобы настроить, какие события кластера вызывают email-уведомления, отправь свою конфигурацию в виде JSON payload. Используй эндпоинт [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication):

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

### Чтение схемы конфигурации

Чтобы узнать формат JSON, необходимый для отправки конфигурации, используй эндпоинт [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") с cluster token, обладающим соответствующими [областями доступа](#token-authentication). Идентификатор схемы конфигурации (`schemaId`), это `builtin:cluster-events-notification-settings`.

Детали схемы ответа

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

### Чтение текущей конфигурации

Чтобы проверить текущую конфигурацию, используй эндпоинт [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") (`/api/cluster/v2/settings/objects?schemaIds=builtin:cluster-events-notification-settings&scopes=cluster`) с cluster token, обладающим соответствующими [областями доступа](#token-authentication).

* Если эти настройки уже были изменены ранее, список items содержит один объект. Используй `objectId` из списка при последующих обновлениях.
* Если список items пуст, используется значение по умолчанию (не отображается в Dynatrace API):

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

### Создание объекта настроек уведомлений

Чтобы создать объект настроек уведомлений о событиях кластера, используй эндпоинт [POST objects](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") с cluster token, обладающим соответствующими [областями доступа](#token-authentication). Используй ID вновь созданного объекта (настройки уведомлений о событиях) для последующих обновлений настроек уведомлений.

Пример создания объекта настроек уведомлений

В этом примере, используя вызов API `POST` к эндпоинту `/api/cluster/v2/settings/objects` и схему `builtin:cluster-events-notification-settings`, создаётся объект настроек уведомлений в настройках кластера:

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

### Обновление настроек уведомлений

Есть два метода, которые можно использовать для обновления настроек уведомлений о событиях кластера после создания объекта настроек уведомлений. В любом случае убедись, что есть cluster token с соответствующими [областями доступа](#token-authentication).

* Можно использовать тот же метод `POST`, который применялся для создания объекта настроек ([Создание объекта настроек уведомлений](#create-settings-object)). Схема не допускает дублирующихся объектов настроек, поэтому при попытке создать ещё один объект настроек существующий будет перезаписан.
* Можно изменить существующий объект настроек, выполнив вызов API `PUT` к эндпоинту `/api/cluster/v2/settings/objects/<objectId>` и указав `objectId`, полученный при создании исходного объекта настроек уведомлений о событиях.

  Пример обновления объекта настроек уведомлений о событиях

  Выполни вызов API `PUT` к `/api/cluster/v2/settings/objects/<objectId>`

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

### Удаление настроек уведомлений

Чтобы удалить существующий объект настроек уведомлений, выполни вызов API [`DELETE`](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") к эндпоинту `/api/cluster/v2/settings/objects/<objectId>`. Используй cluster token с соответствующими [областями доступа](#token-authentication) и укажи `objectId`, полученный при создании исходного объекта настроек уведомлений о событиях. После удаления поведение уведомлений возвращается к значению по умолчанию: все уведомления вызывают отправку письма настроенным получателям.

## События кластера и email-уведомления

В следующих таблицах перечислены уведомления о событиях Managed Cluster по категориям событий.

### `ACTIVE_GATE_TOKENS`

| Severity | Summary | Email notification | MC notification |
| --- | --- | --- | --- |
| WARNING | "ActiveGate Token(s) will expire soon." | Yes | No |

### `CASSANDRA`

| Severity | Summary | Email notification | MC notification |
| --- | --- | --- | --- |
| WARNING | "Cassandra node connection lost (`%d` times in the last hour)." | No | Yes |
| WARNING / INFO | "Cassandra node connection `ADDED/LOST/REACTIVATED`, host ." | No | Yes |
| INFO | "Cassandra node connection added (`%d` times in the last hour)." | No | Yes |
| INFO | "Cassandra node connection reestablished (`%d` times in the last hour)." | No | Yes |

### `CLUSTER_LIFECYCLE`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| SEVERE | «Срок действия лицензии `'%s'` истекает через один день.» | Да | Да |
| SEVERE | «Срок действия лицензии `'%s'` истёк.» | Да | Да |
| SEVERE | «Узел кластера Dynatrace Managed `{0}` недостаточно ресурсный!» | Настраивается [1](#fn-1-1-def) | Да |
| SEVERE | «Место в хранилище для файлов журналов Dynatrace Managed заканчивается на `{0}`.» | Да | Да |
| SEVERE | «Кластер Dynatrace Managed следует масштабировать!» | Да | Да |
| SEVERE | «Не удалось обнаружить активность `%s` на `%s%s`.» | Нет | Да |
| SEVERE | «Недостаточно системных привилегий на `%s`.» | Нет | Да |
| SEVERE | «Немедленно обновите кластер `ActiveGate{0}`. Используется `{1}` `ActiveGate{0}`, которая `{2}` больше не поддерживается!» | Да | Да |
| SEVERE | «Не удалось выполнить миграцию данных после обновления, обратитесь в поддержку Dynatrace.» | Нет | Да |
| SEVERE | «Не удалось загрузить обновление `%s` Dynatrace.» | Нет | Да |
| SEVERE | «Проблема резервного копирования Cassandra.» | Нет | Да |
| SEVERE | «Dynatrace Managed прекратил сбор отслеживаемых данных…» | Нет | Да |
| SEVERE | «Срок действия SSL-сертификата истёк.» | Нет | Да |
| SEVERE | «Лицензия `'%s'` неактивна. Пока это не исправлено, настроить какой-либо мониторинг нельзя. Активируйте лицензию на странице Licensing.» | Нет | Да |
| SEVERE | «Не удалось импортировать сторонние ленты уязвимостей версии `%s` в Dynatrace Application Security кластера.» | Нет | Да |
| SEVERE | «Не удалось импортировать файл метаданных `%s`.» | Нет | Да |
| SEVERE | «Функции кластера по умолчанию были изменены для лицензии не gov-типа.» | Нет | Да |
| SEVERE | «Контроль трафика кластера: мониторинг OneAgent был отключён на недавно подключённых хостах во избежание перегрузки кластера.» | Нет | Да |
| WARNING / SEVERE | «Хост недоступен.» | Да | Да |
| WARNING / SEVERE | «Проблема резервного копирования ElasticSearch.» | Нет | Да |
| WARNING / SEVERE | «Не удалось выполнить обновление кластера `'%s'` (`'%s'`).» | Нет | Да |
| WARNING | «Не удалось изменить настройки узлов WebUI.» | Нет | Да |
| WARNING | «Ошибка соединения LDAP.» | Да | Да |
| WARNING | «Предстоящее обновление до версии `%s` приостановлено для кластера `'%s'` (`'%s'`).» | Да | Да |
| WARNING | «Узел недоступен, `%s`.» | Да, если произошло вне процедуры обновления | Да |
| WARNING | «Отсутствует соединение с Dynatrace Mission Control.» | Да | Да |
| WARNING | «Резервное копирование отключено, так как конфигурация больше не поддерживается.» | Да | Да |
| WARNING | «Получение учётных данных клиента OAuth завершилось с кодом статуса `{0}`.» | Нет | Да |
| WARNING | «Не удалось определить статус обновления кластера `'%s'` (`'%s'`).» | Нет | Да |
| WARNING | «Не удалось загрузить данные самомониторинга на кластере `'%s'`.» | Нет | Да |
| WARNING | «Ошибка проверки лицензии.» | Нет | Да |
| WARNING | «Не удалось обновить SSL-сертификат (`%s`).» | Нет | Да |
| WARNING | «Не удалось войти.» | Нет | Да |
| WARNING | «Не для всех арендаторов из MultiTenant-ActiveGate `%s` настроены AuthTokens.» | Нет | Да |
| WARNING | «Не удалось получить SSL-сертификат Let's Encrypt.» | Нет | Да |
| WARNING | «Срок действия SSL-сертификата скоро истечёт.» | Нет | Да |
| WARNING | «Не удалось войти.» | Нет | Да |
| WARNING | «Приветственное письмо пользователю не отправлено.» | Нет | Да |
| WARNING | «Не удалось импортировать ленту уязвимостей Snyk.» | Нет | Да |
| WARNING | «Не удалось импортировать ленту уязвимостей NVD CVE.» | Нет | Да |
| WARNING | «Проблемы соединения LDAP.» | Нет | Да |
| WARNING / INFO | «Проверка подписи Oidc.» | Нет | Да |
| WARNING / INFO | «Архив биллинга успешно загружен/загружен с предупреждением/не удалось загрузить.» | Нет | Да |
| INFO | «Настройки узлов WebUI успешно изменены.» | Нет | Да |
| INFO | «Запланированное обновление возобновлено для кластера `'%s'` (`'%s'`).» | Да | Да |
| INFO | «Аппаратные рекомендации выполнены на `{0}`.» | Настраивается [1](#fn-1-1-def) | Да |
| INFO | «Места в хранилище для файлов журналов Dynatrace Managed достаточно на `{0}`.» | Да | Да |
| INFO | «Кластер соответствует минимальному требованию по количеству узлов.» | Да | Да |
| INFO | «Узел доступен, `%s`.» | Да | Да |
| INFO | «Хост доступен.» | Да | Да |
| INFO | «Соединение с Dynatrace Mission Control восстановлено.» | Да | Да |
| INFO | «`<processName>` запущен на `<hostName>`.» | Нет | Да |
| INFO | «Узел восстановлен на .» | Нет | Да |
| INFO | «Обновление `%s` Dynatrace успешно загружено.» | Нет | Да |
| INFO | «Кластер `'%s'` (`'%s'`) начал обновление.» | Нет | Да |
| INFO | «Загрузка обновления кластера завершена.» | Нет | Да |
| INFO | «Обновление кластера `'%s'` до версии `%s` завершено.» | Нет | Да |
| INFO | «Запрос на удалённый доступ.» | Нет | Да |
| INFO | «Успешный вход в DebugUI.» | Нет | Да |
| INFO | «SSL-сертификат (`%s`) успешно обновлён.» | Нет | Да |
| INFO | «SSL-сертификат Let's Encrypt успешно получен.» | Нет | Да |
| INFO | «База данных конфигурации кластера `'%s'` успешно инициализирована.» | Нет | Да |
| INFO | «Сервер `%d` присоединился к кластеру `'%s'` (`'%s'`).» | Нет | Да |
| INFO | «Сервер `%d` покинул кластер `'%s'` (`'%s'`).» | Нет | Да |
| INFO | «Сервер `%d` присоединялся к кластеру `'%s'` (`'%s'`) `%d` раз(а) за последний час.» | Нет | Да |
| INFO | «Сервер `%d` покидал кластер `'%s'` (`'%s'`) `%d` раз(а) за последний час.» | Нет | Да |
| INFO | «Успешный вход.» | Нет | Да |
| INFO | «Сторонние ленты уязвимостей версии `%s` успешно импортированы в Dynatrace Application Security кластера.» | Нет | Да |
| INFO | «Не удалось импортировать сторонние ленты уязвимостей версии `%s` в Dynatrace Application Security кластера.» | Нет | Да |

### `CLUSTER_RUNTIME_SETTING`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| SEVERE | «Установлено переопределение ответственных узлов кластера на узле: `%d`.» | Нет | Да |

### `CONFIGURATION_AUDIT`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| INFO | «Min Agent Version обновлена до `%d` пользователем Session Replay.» | Нет | Да |
| INFO | «Session State Version обновлена до `v%d` пользователем Session Replay.» | Нет | Да |

### `ELASTICSEARCH`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| INFO | «Служба хранения Elasticsearch на кластере Dynatrace Managed может быть перегружена!» | Нет | Да |

### `ERROR`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| WARNING | «Не удалось обновить временные настройки ElasticSearch.» | Нет | Да |
| INFO | «Временные настройки ElasticSearch успешно обновлены.» | Нет | Да |

### `LOG_EVENT_DROP`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| WARNING | «Поступившие данные журнала обрезаны.» | Нет | Да |
| WARNING | «Очередь приёма журналов заполнена.» | Нет | Да |
| WARNING | «Очередь журналов Elasticsearch заполнена.» | Нет | Да |
| WARNING | «Не удалось сохранить журнал Elasticsearch.» | Нет | Да |

### `MANAGED_INTERNAL`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| INFO | «Внутреннее: у Cassandra есть устаревшие файлы.» | Нет | Да |

### `MANAGED_NODE_ADD`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| WARNING | «Добавление нового узла занимает больше времени, чем ожидалось.» | Нет | Да |
| INFO | «Операция добавления нового узла запущена.» | Нет | Да |
| INFO | «Статус проверки предварительных условий добавления нового узла.» | Нет | Да |
| INFO | «Добавление нового узла успешно завершено.» | Нет | Да |
| WARNING | «Сбой добавления нового узла.» | Нет | Да |

### `MANAGED_NODE_REMOVAL`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| WARNING | «Удаление узла завершилось с ошибкой `%s` (id=`%d`).» | Нет | Да |
| INFO | «Операция удаления узла не разрешена `%s` (id=`%d`).» | Нет | Да |
| INFO | «Процесс удаления узла успешно запущен `%s` (id=`%d`).» | Нет | Да |
| INFO | «Процесс удаления узла успешно запущен `%s`.» | Нет | Да |
| INFO | «Удаление узла успешно завершено.» | Нет | Да |
| INFO | «Сбой удаления узла.» | Нет | Да |

### `SECURITY_GATEWAY_LIFECYCLE`

| Серьёзность | Сводка | Уведомление по email | Уведомление MC |
| --- | --- | --- | --- |
| INFO | «ActiveGate (host=`%s`) зарегистрирован в кластере.» | Нет | Да |
| INFO | «ActiveGate (host=`%s`) снят с регистрации в кластере.» | Нет | Да |
| INFO | «ActiveGate (host=`%s`) потерял соединение с кластером.» | Нет | Да |
| INFO | «ActiveGate (environment=`%s`, host=`%s`) зарегистрирован в кластере.» | Нет | Да |
| INFO | «ActiveGate (environment=`%s`, host=`%s`) снят с регистрации в кластере.» | Нет | Да |
| INFO | «ActiveGate (environment=`%s`, host=`%s`) потерял соединение с кластером.» | Нет | Да |

### `SERVER_LIFECYCLE`

| Severity | Summary | Email notification | MC notification |
| --- | --- | --- | --- |
| SEVERE | «Transaction storage retention period truncated.» | Configurable [1](#fn-1-1-def) | Yes |
| SEVERE | «Insufficient disk space on `%s` on `%s`.» | Configurable [1](#fn-1-1-def) | Yes |
| SEVERE | «Long-term Metrics Store size exceeds the maximum acceptable 4 TB on `%s`.» | Configurable [1](#fn-1-1-def) | Yes |
| SEVERE | «`<component name>` is down.» | No | Yes |
| SEVERE | «Heap memory: Server `%d` started memory emergency mode.» | No | Yes |
| SEVERE | «Heap memory: Server `%d` triggered a hard memory cleanup action.» | No | Yes |
| SEVERE | «A cluster node can't receive OneAgent traffic.» | No | Yes |
| WARNING | «Server `%d` activated Adaptive Load Reduction.» | Configurable [1](#fn-1-1-def) | Yes |
| WARNING | «Long-term Metrics Store size exceeds recommended 2 TB on `%s`.» | No | Yes |
| WARNING | «Node cannot read and write to directory: `'%s'`.» | No | Yes |
| WARNING | «Heap memory: Server `%d` triggered a soft memory cleanup action.» | No | Yes |
| WARNING / INFO | «Disabling OneAgent traffic at » | No | Yes |
| WARNING / INFO | «Enabling OneAgent traffic at » | No | Yes |
| INFO | «Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security.» | Configurable [1](#fn-1-1-def) | Yes |
| INFO | «Server `%d` deactivated Adaptive Load Reduction.» | Configurable [1](#fn-1-1-def) | Yes |
| INFO | «Server `%d` shutdown initiated.» | No | Yes |
| INFO | «`<component name>` is up.» | No | Yes |
| INFO | «Server `%d` startup completed. (Version: `%s`).» | No | Yes |
| INFO | «Heap memory: Server `%d` ended memory emergency mode.» | No | Yes |
| ? | «Server time of server `%d` is out of sync. Time difference `%d` milliseconds. Please enable NTP on all cluster nodes.» | No | Yes |

### `TENANT_LIFECYCLE`

| Severity | Summary | Email notification | MC notification |
| --- | --- | --- | --- |
| SEVERE | «Trial environment expired.» | No | Yes |
| SEVERE | «The node with id `%s` is not properly configured.» | No | Yes |
| SEVERE | «Environment `'%s'` with id `%s` failed to start on server `%d`. See server logs for details.» | No | Yes |
| INFO | «Environment `'%s'` with id `%s` created.» | No | Yes |
| INFO | «Environment `'%s'` with id `%s` updated.» | No | Yes |
| INFO | «Environment `'%s'` with id `%s` removed.» | No | Yes |

1

Configurable означает, что уведомления можно настроить через Settings API. Setting id: `builtin:cluster-events-notification-settings`. Чтобы использовать этот REST API, нужно авторизоваться с помощью специального токена настроек с правами `settings.read` и `settings.write`.