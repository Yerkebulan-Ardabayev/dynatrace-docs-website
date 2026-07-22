---
title: OneAgent on a host - GET a list of hosts with OneAgent details
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents
---

# OneAgent on a host - GET a list of hosts with OneAgent details

# OneAgent on a host - GET a list of hosts with OneAgent details

* Справка
* Опубликовано 03 февраля 2020 г.

Запрос **OneAgent on a host** API позволяет проверить конфигурацию экземпляров OneAgent на хостах.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/oneagents` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/oneagents` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с одной из следующих областей действия:

* `oneAgents.read`
* `DataExport`

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые из связанных сущностей.  Исключение деталей может ускорить выполнение запросов.  Если не задано, используется `true`. | query | Опционально |
| startTimestamp | integer | Начальная метка времени запрашиваемого временного интервала, в миллисекундах (UTC).  Если не задано, используется значение 72 часа назад от текущего момента. | query | Опционально |
| endTimestamp | integer | Конечная метка времени запрашиваемого временного интервала, в миллисекундах (UTC).  Если не задано, используется текущая метка времени.  Временной интервал не должен превышать 7 месяцев (214 дней). | query | Опционально |
| relativeTime | string | Относительный временной интервал, отсчитываемый от текущего момента.  Если нужно указать относительный временной интервал, отсутствующий в списке возможных значений, укажи **startTimestamp** (до 214 дней назад от текущего момента) и оставь **endTimestamp** и **relativeTime** пустыми. Элемент может содержать следующие значения * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Опционально |
| tag | string[] | Фильтрует результирующий набор хостов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам.  В случае тегов ключ-значение, таких как импортированные AWS или теги CloudFoundry, используй следующий формат: `tag=[context]key:value`. Для пользовательских тегов ключ-значение контекст опускается: `tag=key:value`. | query | Опционально |
| entity | string[] | Фильтрует результат только по указанным хостам.  Чтобы указать несколько хостов, используй следующий формат: `entity=ID1&entity=ID2`. | query | Опционально |
| managementZoneId | integer | Возвращает только хосты, входящие в указанную management zone.  Здесь укажи ID management zone. | query | Опционально |
| managementZone | string | Возвращает только хосты, входящие в указанную management zone.  Здесь укажи название management zone.  Если задан параметр **managementZoneId**, этот параметр игнорируется. | query | Опционально |
| networkZoneId | string | Фильтрует результирующий набор хостов по указанной network zone.  Укажи Dynatrace ID сущности нужной network zone. Список доступных network zones можно получить вызовом [GET all network zones﻿](https://dt-url.net/u4o3r7z?dt=m). | query | Опционально |
| hostGroupId | string | Фильтрует результирующий набор хостов по указанной host group.  Укажи Dynatrace ID сущности нужной host group. | query | Опционально |
| hostGroupName | string | Фильтрует результирующий набор хостов по указанной host group.  Укажи название нужной host group. | query | Опционально |
| osType | string | Фильтрует результирующий набор хостов по типу ОС. Элемент может содержать следующие значения * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` | query | Опционально |
| cloudType | string | Фильтрует результирующий набор хостов по типу облака. Элемент может содержать следующие значения * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` | query | Опционально |
| autoInjection | string | Фильтрует результирующий набор хостов по статусу автоматического внедрения. Элемент может содержать следующие значения * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` | query | Опционально |
| availabilityState | string | Фильтрует результирующий набор хостов по состоянию доступности OneAgent.  * `MONITORED`: хосты, на которых OneAgent включён и активен. * `UNMONITORED`: хосты, на которых OneAgent отключён и неактивен. * `CRASHED`: хосты, на которых OneAgent вернул код статуса аварийного завершения. * `LOST`: хосты, с которыми невозможно установить соединение через OneAgent. * `PRE_MONITORED`: хосты, на которых OneAgent инициализируется для мониторинга. * `SHUTDOWN`: хосты, на которых OneAgent завершает работу в управляемом процессе. * `UNEXPECTED_SHUTDOWN`: хосты, на которых OneAgent завершает работу в неуправляемом процессе. * `UNKNOWN`: хосты, на которых состояние OneAgent неизвестно. Элемент может содержать следующие значения * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` | query | Опционально |
| detailedAvailabilityState | string | Фильтрует результирующий набор хостов по детализированному состоянию доступности OneAgent.  * `UNKNOWN`: хосты, на которых состояние OneAgent неизвестно. * `PRE_MONITORED`: хосты, на которых OneAgent инициализируется для мониторинга. * `CRASHED_UNKNOWN`: хосты, на которых OneAgent аварийно завершился по неизвестной причине. * `CRASHED_FAILURE`: хосты, на которых OneAgent вернул код статуса аварийного завершения. * `LOST_UNKNOWN`: хосты, с которыми невозможно установить соединение через OneAgent по неизвестной причине. * `LOST_CONNECTION`: хосты, на которых OneAgent был распознан как неактивный. * `LOST_AGENT_UPGRADE_FAILED`: хосты, на которых у OneAgent возможна проблема обновления из-за неактивности после обновления. * `SHUTDOWN_UNKNOWN_UNEXPECTED`: хосты, на которых OneAgent завершает работу в неуправляемом процессе. * `SHUTDOWN_UNKNOWN`: хосты, на которых OneAgent завершил работу по неизвестной причине. * `SHUTDOWN_GRACEFUL`: хосты, на которых OneAgent завершил работу из-за выключения хоста. * `SHUTDOWN_STOPPED`: хосты, на которых OneAgent завершил работу из-за остановки хоста. * `SHUTDOWN_AGENT_LOST`: хосты, на которых модуль PaaS был распознан как неактивный. * `SHUTDOWN_SPOT_INSTANCE`: хосты, на которых завершение работы OneAgent было вызвано прерыванием AWS Spot Instance. * `SHUTDOWN_K8S_NODE_SHUTDOWN`: хосты, на которых завершение работы OneAgent было вызвано плановым завершением работы узла k8s. * `UNMONITORED_UNKNOWN`: хосты, на которых OneAgent отключён и неактивен по неизвестной причине. * `UNMONITORED_TERMINATED`: хосты, на которых OneAgent был завершён. * `UNMONITORED_DISABLED`: хосты, на которых OneAgent был отключён в конфигурации. * `UNMONITORED_AGENT_STOPPED`: хосты, на которых OneAgent остановлен. * `UNMONITORED_AGENT_RESTART_TRIGGERED`: хосты, на которых OneAgent перезапускается. * `UNMONITORED_AGENT_UNINSTALLED`: хосты, на которых OneAgent удалён. * `UNMONITORED_AGENT_DISABLED`: хосты, на которых OneAgent сообщил, что был отключён. * `UNMONITORED_AGENT_UPGRADE_FAILED`: хосты, на которых у OneAgent возможна проблема обновления. * `UNMONITORED_ID_CHANGED`: хосты, на которых OneAgent возможно изменил ID во время обновления. * `UNMONITORED_AGENT_LOST`: хосты, на которых OneAgent был распознан как недоступный из-за проблем связи с сервером. * `UNMONITORED_AGENT_UNREGISTERED`: хосты, на которых модуль кода был распознан как недоступный из-за завершения работы. * `UNMONITORED_AGENT_VERSION_REJECTED`: хосты, на которых OneAgent был отклонён, поскольку версия не соответствует минимальным требованиям к версии агента. * `UNMONITORED_AGENT_MIGRATED`: хосты, на которых OneAgent был перенесён в другую среду. * `MONITORED`: хосты, на которых OneAgent включён и активен. * `MONITORED_ENABLED`: хосты, на которых OneAgent был включён в конфигурации. * `MONITORED_AGENT_REGISTERED`: хосты, на которых был распознан новый OneAgent. * `MONITORED_AGENT_UPGRADE_STARTED`: хосты, на которых OneAgent завершил работу из-за обновления. * `MONITORED_AGENT_ENABLED`: хосты, на которых OneAgent сообщил, что был включён. * `MONITORED_AGENT_VERSION_ACCEPTED`: хосты, на которых OneAgent был принят, поскольку версия соответствует минимальным требованиям к версии агента. Элемент может содержать следующие значения * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` | query | Опционально |
| monitoringType | string | Фильтрует результирующий набор хостов по режиму мониторинга OneAgent, развёрнутого на хосте. Элемент может содержать следующие значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` | query | Опционально |
| agentVersionIs | string | Фильтрует результирующий набор хостов до тех, на которых развёрнута определённая версия OneAgent.  Здесь укажи оператор сравнения. Элемент может содержать следующие значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Опционально |
| agentVersionNumber | string | Фильтрует результирующий набор хостов до тех, на которых развёрнута определённая версия OneAgent.  Укажи версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить вызовом [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m). | query | Опционально |
| autoUpdateSetting | string | Фильтрует результирующий набор хостов по фактическому состоянию настройки автообновления развёрнутых OneAgent. Элемент может содержать следующие значения * `ENABLED` * `DISABLED` | query | Опционально |
| updateStatus | string | Фильтрует результирующий набор хостов по статусу обновления OneAgent, развёрнутого на хосте. Элемент может содержать следующие значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Опционально |
| faultyVersion | boolean | Фильтрует результирующий набор хостов до тех, на которых работает версия OneAgent, отмеченная как неисправная. | query | Опционально |
| unlicensed | boolean | Фильтрует результирующий набор хостов до тех, на которых работает нелицензированный OneAgent.  Пример: в лицензии Dynatrace отсутствует необходимая возможность DPS "Foundation & Discovery" для режима Discovery. | query | Опционально |
| activeGateId | string | Фильтрует результирующий набор хостов до тех, что в данный момент подключены к ActiveGate с указанным ID.  Используй ключевое слово **DIRECT_COMMUNICATION**, чтобы найти хосты, не подключённые ни к одному ActiveGate. | query | Опционально |
| technologyModuleType | string | Фильтрует результирующий набор хостов до тех, на которых работает указанный модуль кода OneAgent.  Если указано несколько фильтров модулей кода, модуль кода должен соответствовать **всем** фильтрам. Элемент может содержать следующие значения * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` | query | Опционально |
| technologyModuleVersionIs | string | Фильтрует результирующий набор хостов до тех, на которых развёрнута определённая версия модуля кода.  Здесь укажи оператор сравнения.  Если указано несколько фильтров модулей кода, модуль кода должен соответствовать **всем** фильтрам. Элемент может содержать следующие значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Опционально |
| technologyModuleVersionNumber | string | Фильтрует результирующий набор хостов до тех, на которых развёрнута определённая версия модуля кода.  Укажи версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить вызовом [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m).  Если указано несколько фильтров модулей кода, модуль кода должен соответствовать **всем** фильтрам. | query | Опционально |
| technologyModuleFaultyVersion | boolean | Фильтрует результирующий набор хостов до тех, на которых работает версия модуля кода, отмеченная как неисправная.  Если указано несколько фильтров модулей кода, модуль кода должен соответствовать **всем** фильтрам. | query | Опционально |
| pluginName | string | Фильтрует результирующий набор хостов до тех, на которых работает плагин с указанным именем.  К указанному значению применяется оператор **CONTAINS**.  Если указано несколько фильтров плагинов, плагин должен соответствовать **всем** фильтрам. | query | Опционально |
| pluginVersionIs | string | Фильтрует результирующий набор хостов до тех, на которых развёрнута определённая версия плагина.  Здесь укажи оператор сравнения.  Если указано несколько фильтров плагинов, плагин должен соответствовать **всем** фильтрам. Элемент может содержать следующие значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Опционально |
| pluginVersionNumber | string | Фильтрует результирующий набор хостов до тех, на которых развёрнута определённая версия плагина.  Укажи версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить вызовом [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m).  Части версии `<minor>` и `<revision>` необязательны.  Если указано несколько фильтров плагинов, плагин должен соответствовать **всем** фильтрам. | query | Опционально |
| pluginState | string | Фильтрует результирующий набор хостов до тех, на которых работает плагин с указанным состоянием. Элемент может содержать следующие значения * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Опционально |
| nextPageKey | string | Курсор для следующей страницы результатов, если результаты не помещаются на одной странице. Значение курсора можно найти на текущей странице ответа, в поле **nextPageKey**.  Чтобы получить последующие страницы, нужно указать это значение курсора в запросе и сохранить все остальные параметры запроса такими же, какими они были в исходном запросе.  Если курсор не указан, всегда возвращается первая страница. | query | Опционально |
## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostsListPage](#openapi-definition-HostsListPage) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `HostsListPage`

Список хостов с информацией о развёртывании OneAgent на каждом хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hosts | [HostAgentInfo](#openapi-definition-HostAgentInfo)[] | Список хостов с информацией о развёртывании OneAgent на каждом хосте. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`. Следующая страница результатов может существовать, даже если текущая страница пуста. |
| percentageOfEnvironmentSearched | number | Прогресс поиска по окружению, в процентах. |

#### Объект `HostAgentInfo`

Развёртывание OneAgent на хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | OneAgent активен (`true`) или неактивен (`false`). |
| autoUpdateSetting | string | Действующая настройка автообновления OneAgent. Для хоста с унаследованной конфигурацией вычисляется из конфигурации родителя. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| availabilityState | string | Состояние доступности OneAgent. Элемент может принимать следующие значения * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` |
| availableVersions | string[] | Список версий, до которых можно обновить OneAgent. |
| configuredMonitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`) в конфигурации OneAgent. |
| configuredMonitoringMode | string | Настроенный режим мониторинга OneAgent. Элемент может принимать следующие значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |
| ~~currentActiveGateId~~ | integer | УСТАРЕЛО  Это поле устарело и предоставляется для обратной совместимости.  Используй вместо него поле **currentActiveGateIds**. |
| currentActiveGateIds | string[] | Список ID ActiveGate, к которым в данный момент подключён OneAgent. |
| currentNetworkZoneId | string | ID сетевой зоны, которую использует OneAgent. |
| detailedAvailabilityState | string | Детальное состояние доступности OneAgent. Элемент может принимать следующие значения * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` |
| faultyVersion | boolean | Версия OneAgent неисправна (`true`) или нет (`false`). |
| hostInfo | [Host](#openapi-definition-Host) | Информация о хосте. |
| modules | [ModuleInfo](#openapi-definition-ModuleInfo)[] | Список модулей кода, развёрнутых на хосте. |
| monitoringType | string | Режим мониторинга OneAgent. Элемент может принимать следующие значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` |
| plugins | [PluginInfo](#openapi-definition-PluginInfo)[] | Список плагинов, развёрнутых на хосте. |
| unlicensed | boolean | OneAgent не лицензирован. |
| updateStatus | string | Текущий статус обновления OneAgent. Элемент может принимать следующие значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |

#### Объект `Host`

Информация о хосте.

| Element | Type | Description |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Определяет версию агента, работающего в данный момент на сущности. |
| amiId | string | - |
| autoInjection | string | Статус auto-injection. Элемент может принимать следующие значения * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | Имя, унаследованное от AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -Элемент может принимать следующие значения * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -Элемент может принимать следующие значения * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -Элемент может принимать следующие значения * `32bit` * `64bit` |
| boshAvailabilityZone | string | Зона доступности Cloud Foundry BOSH. |
| boshDeploymentId | string | ID развёртывания Cloud Foundry BOSH. |
| boshInstanceId | string | ID инстанса Cloud Foundry BOSH. |
| boshInstanceName | string | Имя инстанса Cloud Foundry BOSH. |
| boshName | string | Имя Cloud Foundry BOSH. |
| boshStemcellVersion | string | Версия stemcell Cloud Foundry BOSH. |
| cloudPlatformVendorVersion | string | Определяет версию вендора облачной платформы. |
| cloudType | string | -Элемент может принимать следующие значения * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Использованные Host Unit. Применимо только для [классического лицензирования Dynatrace﻿](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | Настроенное имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в UI. |
| entityId | string | ID сущности Dynatrace для требуемой сущности. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | Временная метка, когда сущность была впервые обнаружена, в миллисекундах UTC |
| fromRelationships | object | - |
| gceInstanceId | string | ID инстанса Google Compute Engine. |
| gceInstanceName | string | Имя инстанса Google Compute Engine. |
| gceMachineType | string | Тип машины Google Compute Engine. |
| gceProject | string | Проект Google Compute Engine. |
| gceProjectId | string | Числовой ID проекта Google Compute Engine. |
| gcePublicIpAddresses | string[] | Публичные IP-адреса Google Compute Engine. |
| gcpZone | string | Зона Google Cloud Platform. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -Элемент может принимать следующие значения * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | Кластер kubernetes, в котором находится сущность. |
| kubernetesLabels | object | Метки kubernetes, определённые для сущности. |
| kubernetesNode | string | Узел kubernetes, в котором находится сущность. |
| lastSeenTimestamp | integer | Временная метка, когда сущность была обнаружена последний раз, в миллисекундах UTC |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | Количество логических CPU инстанса AIX. |
| managementZones | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation)[] | Management zones, к которым относится сущность. |
| monitoringMode | string | -Элемент может принимать следующие значения * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | ID network zone, в которой находится сущность. |
| oneAgentCustomHostName | string | Пользовательское имя, определённое в конфигурации OneAgent. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -Элемент может принимать следующие значения * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -Элемент может принимать следующие значения * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion](#openapi-definition-AgentVersion)[] | Версии PaaS-агентов, работающих в данный момент на сущности. |
| paasMemoryLimit | integer | - |
| paasType | string | -Элемент может принимать следующие значения * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | Количество одновременных потоков инстанса AIX. |
| softwareTechnologies | [TechnologyInfo](#openapi-definition-TechnologyInfo)[] | - |
| tags | [TagInfo](#openapi-definition-TagInfo)[] | Список тегов сущности. |
| toRelationships | object | - |
| userLevel | string | -Элемент может принимать следующие значения * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | Количество виртуальных CPU инстанса AIX. |
| vmwareName | string | - |
| zosCPUModelNumber | string | Номер модели CPU. |
| zosCPUSerialNumber | string | Серийный номер CPU. |
| zosLpaName | string | Имя LPAR. |
| zosSystemName | string | Имя системы. |
| zosTotalGeneralPurposeProcessors | integer | Количество назначенных процессоров для этого LPAR. |
| zosTotalPhysicalMemory | integer | Память, назначенная хосту (терабайт). |
| zosTotalZiipProcessors | integer | Количество назначенных вспомогательных процессоров для этого LPAR. |
| zosVirtualization | string | Тип виртуализации на мейнфрейме. |


#### Объект `AgentVersion`


Определяет версию агента, работающего в данный момент на сущности.


| Element | Type | Description |
| --- | --- | --- |
| major | integer | Номер основной версии. |
| minor | integer | Номер минорной версии. |
| revision | integer | Номер редакции. |
| sourceRevision | string | Строковое представление номера редакции SVN. |
| timestamp | string | Строка временной метки: формат "yyyymmdd-hhmmss |


#### Объект `HostGroup`


| Element | Type | Description |
| --- | --- | --- |
| meId | string | ID сущности Dynatrace группы хостов. |
| name | string | Имя сущности Dynatrace, отображаемое в UI. |


#### Объект `EntityShortRepresentation`


Краткое представление сущности Dynatrace.


| Element | Type | Description |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |


#### Объект `TechnologyInfo`


| Element | Type | Description |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |


#### Объект `TagInfo`


Тег сущности Dynatrace.


| Element | Type | Description |
| --- | --- | --- |
| context | string | Источник происхождения тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов значение тега находится здесь. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |


#### Объект `ModuleInfo`


Модуль кода OneAgent.


| Element | Type | Description |
| --- | --- | --- |
| instances | [ModuleInstance](#openapi-definition-ModuleInstance)[] | Список инстансов модуля кода. |
| moduleType | string | Тип модуля кода. Элемент может принимать следующие значения * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` |


#### Объект `ModuleInstance`


Инстанс модуля кода OneAgent.


| Element | Type | Description |
| --- | --- | --- |
| active | boolean | Инстанс модуля кода активен (`true`) или неактивен (`false`). |
| faultyVersion | boolean | Версия модуля кода неисправна (`true`) или нет (`false`). |
| instanceName | string | Имя инстанса. |
| moduleVersion | string | Версия модуля кода. |


#### Объект `PluginInfo`


Плагин OneAgent.


| Element | Type | Description |
| --- | --- | --- |
| instances | [PluginInstance](#openapi-definition-PluginInstance)[] | Список инстансов плагина. |
| pluginName | string | Имя плагина. |


#### Объект `PluginInstance`


Инстанс плагина OneAgent.


| Element | Type | Description |
| --- | --- | --- |
| pluginVersion | string | Версия плагина. |
| state | string | Состояние инстанса плагина. |


#### Объект `ErrorEnvelope`


| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |


#### Объект `Error`


| Element | Type | Description |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`


Список нарушений ограничений


| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Тело ответа JSON моделей

```
{



"hosts": [



{



"active": true,



"autoUpdateSetting": "ENABLED",



"availabilityState": "CRASHED",



"availableVersions": [



"string"



],



"configuredMonitoringEnabled": true,



"configuredMonitoringMode": "CLOUD_INFRASTRUCTURE",



"currentActiveGateId": 1,



"currentActiveGateIds": [



"string"



],



"currentNetworkZoneId": "string",



"detailedAvailabilityState": "CRASHED_FAILURE",



"faultyVersion": true,



"hostInfo": {



"agentVersion": {



"major": 1,



"minor": 1,



"revision": 1,



"sourceRevision": "string",



"timestamp": "string"



},



"amiId": "string",



"autoInjection": "DISABLED_MANUALLY",



"autoScalingGroup": "string",



"awsInstanceId": "string",



"awsInstanceType": "string",



"awsNameTag": "string",



"awsSecurityGroup": [



"string"



],



"azureComputeModeName": "DEDICATED",



"azureEnvironment": "string",



"azureHostNames": [



"string"



],



"azureResourceGroupName": "string",



"azureResourceId": "string",



"azureSiteNames": [



"string"



],



"azureSku": "BASIC",



"azureVmName": "string",



"azureVmScaleSetName": "string",



"azureVmSizeLabel": "string",



"azureZone": "string",



"beanstalkEnvironmentName": "string",



"bitness": "32bit",



"boshAvailabilityZone": "string",



"boshDeploymentId": "string",



"boshInstanceId": "string",



"boshInstanceName": "string",



"boshName": "string",



"boshStemcellVersion": "string",



"cloudPlatformVendorVersion": "string",



"cloudType": "AZURE",



"consumedHostUnits": "string",



"cpuCores": 1,



"customizedName": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esxiHostName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"isNetworkClientOfHost": [



"string"



]



},



"gceInstanceId": "string",



"gceInstanceName": "string",



"gceMachineType": "string",



"gceProject": "string",



"gceProjectId": "string",



"gcePublicIpAddresses": [



"string"



],



"gcpZone": "string",



"hostGroup": {



"meId": "string",



"name": "string"



},



"hypervisorType": "AHV",



"ipAddresses": [



"string"



],



"isMonitoringCandidate": true,



"kubernetesCluster": "string",



"kubernetesLabels": {},



"kubernetesNode": "string",



"lastSeenTimestamp": 1,



"localHostName": "string",



"localIp": "string",



"logicalCpuCores": 1,



"logicalCpus": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"monitoringMode": "FULL_STACK",



"networkZoneId": "string",



"oneAgentCustomHostName": "string",



"openStackInstaceType": "string",



"openstackAvZone": "string",



"openstackComputeNodeName": "string",



"openstackProjectName": "string",



"openstackSecurityGroups": [



"string"



],



"openstackVmName": "string",



"osArchitecture": "ARM",



"osType": "AIX",



"osVersion": "string",



"paasAgentVersions": [



{}



],



"paasMemoryLimit": 1,



"paasType": "AWS_ECS_EC2",



"publicHostName": "string",



"publicIp": "string",



"scaleSetName": "string",



"simultaneousMultithreading": 1,



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"isNetworkClientOfHost": [



"string"



],



"isProcessOf": [



"string"



],



"isSiteOf": [



"string"



],



"runsOn": [



"string"



]



},



"userLevel": "NON_SUPERUSER",



"virtualCpus": 1,



"vmwareName": "string",



"zosCPUModelNumber": "string",



"zosCPUSerialNumber": "string",



"zosLpaName": "string",



"zosSystemName": "string",



"zosTotalGeneralPurposeProcessors": 1,



"zosTotalPhysicalMemory": 1,



"zosTotalZiipProcessors": 1,



"zosVirtualization": "string"



},



"modules": [



{



"instances": [



{



"active": true,



"faultyVersion": true,



"instanceName": "string",



"moduleVersion": "string"



}



],



"moduleType": "APACHE"



}



],



"monitoringType": "CLOUD_INFRASTRUCTURE",



"plugins": [



{



"instances": [



{



"pluginVersion": "string",



"state": "string"



}



],



"pluginName": "string"



}



],



"unlicensed": true,



"updateStatus": "INCOMPATIBLE"



}



],



"nextPageKey": "string",



"percentageOfEnvironmentSearched": 1



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Похожие темы

* [конфигурация OneAgent на хосте API](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Управляйте конфигурацией экземпляров OneAgent на хостах через Dynatrace API.")