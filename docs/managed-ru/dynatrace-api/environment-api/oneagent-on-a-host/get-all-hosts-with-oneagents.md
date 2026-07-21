---
title: OneAgent on a host - GET список хостов с деталями OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents
scraped: 2026-05-12T11:12:22.540854
---

# OneAgent on a host - GET список хостов с деталями OneAgent

# OneAgent on a host - GET список хостов с деталями OneAgent

* Справочник
* Опубликовано 03 февраля 2020 г.

API **OneAgent on a host** позволяет проверять конфигурацию экземпляров OneAgent на ваших хостах.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/oneagents` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/oneagents` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `oneAgents.read`
* `DataExport`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Необязательный |
| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задано, используется значение 72 часа назад от текущего момента. | query | Необязательный |
| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задано, используется текущая метка времени.  Диапазон не должен превышать 7 месяцев (214 дней). | query | Необязательный |
| relativeTime | string | Относительный диапазон, назад от текущего момента.  Если нужно указать относительный диапазон, которого нет в списке возможных значений, укажите **startTimestamp** (до 214 дней назад от текущего момента) и оставьте **endTimestamp** и **relativeTime** пустыми. Элемент может принимать значения * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Необязательный |
| tag | string[] | Фильтрует результирующий набор хостов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам.  В случае тегов ключ-значение, таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов ключ-значение опустите context: `tag=key:value`. | query | Необязательный |
| entity | string[] | Фильтрует результат только до указанных хостов.  Чтобы указать несколько хостов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательный |
| managementZoneId | integer | Возвращать только хосты, входящие в указанную management zone.  Укажите здесь ID management zone. | query | Необязательный |
| managementZone | string | Возвращать только хосты, входящие в указанную management zone.  Укажите здесь имя management zone.  Если задан параметр **managementZoneId**, этот параметр игнорируется. | query | Необязательный |
| networkZoneId | string | Фильтрует результирующий набор хостов по указанной network zone.  Укажите ID сущности Dynatrace требуемой network zone. Список доступных network zone можно получить вызовом [GET all network zones](https://dt-url.net/u4o3r7z?dt=m). | query | Необязательный |
| hostGroupId | string | Фильтрует результирующий набор хостов по указанной host group.  Укажите ID сущности Dynatrace требуемой host group. | query | Необязательный |
| hostGroupName | string | Фильтрует результирующий набор хостов по указанной host group.  Укажите имя требуемой host group. | query | Необязательный |
| osType | string | Фильтрует результирующий набор хостов по типу ОС. Элемент может принимать значения * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` | query | Необязательный |
| cloudType | string | Фильтрует результирующий набор хостов по типу облака. Элемент может принимать значения * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` | query | Необязательный |
| autoInjection | string | Фильтрует результирующий набор хостов по статусу авто-инъекции. Элемент может принимать значения * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` | query | Необязательный |
| availabilityState | string | Фильтрует результирующий набор хостов по состоянию доступности OneAgent.  * `MONITORED`: Хосты, где OneAgent включён и активен. * `UNMONITORED`: Хосты, где OneAgent отключён и неактивен. * `CRASHED`: Хосты, где OneAgent вернул код состояния сбоя. * `LOST`: Хосты, где невозможно установить соединение с OneAgent. * `PRE_MONITORED`: Хосты, где OneAgent инициализируется для мониторинга. * `SHUTDOWN`: Хосты, где OneAgent завершает работу в контролируемом процессе. * `UNEXPECTED_SHUTDOWN`: Хосты, где OneAgent завершает работу в неконтролируемом процессе. * `UNKNOWN`: Хосты, где состояние OneAgent неизвестно. Элемент может принимать значения * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` | query | Необязательный |
| detailedAvailabilityState | string | Фильтрует результирующий набор хостов по детальному состоянию доступности OneAgent.  * `UNKNOWN`: Хосты, где состояние OneAgent неизвестно. * `PRE_MONITORED`: Хосты, где OneAgent инициализируется для мониторинга. * `CRASHED_UNKNOWN`: Хосты, где OneAgent дал сбой по неизвестной причине. * `CRASHED_FAILURE`: Хосты, где OneAgent вернул код состояния сбоя. * `LOST_UNKNOWN`: Хосты, где невозможно установить соединение с OneAgent по неизвестной причине. * `LOST_CONNECTION`: Хосты, где OneAgent распознан как неактивный. * `LOST_AGENT_UPGRADE_FAILED`: Хосты, где у OneAgent потенциальная проблема обновления из-за неактивности после обновления. * `SHUTDOWN_UNKNOWN_UNEXPECTED`: Хосты, где OneAgent завершает работу в неконтролируемом процессе. * `SHUTDOWN_UNKNOWN`: Хосты, где OneAgent завершил работу по неизвестной причине. * `SHUTDOWN_GRACEFUL`: Хосты, где OneAgent завершил работу из-за выключения хоста. * `SHUTDOWN_STOPPED`: Хосты, где OneAgent завершил работу из-за остановки хоста. * `SHUTDOWN_AGENT_LOST`: Хосты, где PaaS-модуль распознан как неактивный. * `SHUTDOWN_SPOT_INSTANCE`: Хосты, где завершение работы OneAgent вызвано прерыванием AWS Spot Instance. * `SHUTDOWN_K8S_NODE_SHUTDOWN`: Хосты, где завершение работы OneAgent вызвано штатным выключением k8s-узла. * `UNMONITORED_UNKNOWN`: Хосты, где OneAgent отключён и неактивен по неизвестной причине. * `UNMONITORED_TERMINATED`: Хосты, где OneAgent завершён. * `UNMONITORED_DISABLED`: Хосты, где OneAgent отключён в конфигурации. * `UNMONITORED_AGENT_STOPPED`: Хосты, где OneAgent остановлен. * `UNMONITORED_AGENT_RESTART_TRIGGERED`: Хосты, где OneAgent перезапускается. * `UNMONITORED_AGENT_UNINSTALLED`: Хосты, где OneAgent удалён. * `UNMONITORED_AGENT_DISABLED`: Хосты, где OneAgent сообщил, что он отключён. * `UNMONITORED_AGENT_UPGRADE_FAILED`: Хосты, где у OneAgent потенциальная проблема обновления. * `UNMONITORED_ID_CHANGED`: Хосты, где OneAgent потенциально сменил ID во время обновления. * `UNMONITORED_AGENT_LOST`: Хосты, где OneAgent распознан как недоступный из-за проблем связи с сервером. * `UNMONITORED_AGENT_UNREGISTERED`: Хосты, где модуль кода распознан как недоступный из-за завершения работы. * `UNMONITORED_AGENT_VERSION_REJECTED`: Хосты, где OneAgent отклонён, потому что версия не соответствует требованию минимальной версии агента. * `UNMONITORED_AGENT_MIGRATED`: Хосты, где OneAgent был перенесён в другое окружение. * `MONITORED`: Хосты, где OneAgent включён и активен. * `MONITORED_ENABLED`: Хосты, где OneAgent включён в конфигурации. * `MONITORED_AGENT_REGISTERED`: Хосты, где распознан новый OneAgent. * `MONITORED_AGENT_UPGRADE_STARTED`: Хосты, где OneAgent завершил работу из-за обновления. * `MONITORED_AGENT_ENABLED`: Хосты, где OneAgent сообщил, что он включён. * `MONITORED_AGENT_VERSION_ACCEPTED`: Хосты, где OneAgent принят, потому что версия соответствует требованию минимальной версии агента. Элемент может принимать значения * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` | query | Необязательный |
| monitoringType | string | Фильтрует результирующий набор хостов по режиму мониторинга OneAgent, развёрнутого на хосте. Элемент может принимать значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` | query | Необязательный |
| agentVersionIs | string | Фильтрует результирующий набор хостов до тех, где на хосте развёрнута определённая версия OneAgent.  Укажите здесь оператор сравнения. Элемент может принимать значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| agentVersionNumber | string | Фильтрует результирующий набор хостов до тех, где на хосте развёрнута определённая версия OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5?dt=m). | query | Необязательный |
| autoUpdateSetting | string | Фильтрует результирующий набор хостов по фактическому состоянию настройки авто-обновления развёрнутых OneAgent. Элемент может принимать значения * `ENABLED` * `DISABLED` | query | Необязательный |
| updateStatus | string | Фильтрует результирующий набор хостов по статусу обновления OneAgent, развёрнутого на хосте. Элемент может принимать значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Необязательный |
| faultyVersion | boolean | Фильтрует результирующий набор хостов до тех, где работает версия OneAgent, помеченная как сбойная. | query | Необязательный |
| unlicensed | boolean | Фильтрует результирующий набор хостов до тех, где работает OneAgent без лицензии.  Пример: в вашей лицензии Dynatrace отсутствует требуемая возможность DPS «Foundation & Discovery» для режима Discovery. | query | Необязательный |
| activeGateId | string | Фильтрует результирующий набор хостов до тех, что в данный момент подключены к ActiveGate с указанным ID.  Используйте ключевое слово **DIRECT\_COMMUNICATION**, чтобы найти хосты, не подключённые ни к одному ActiveGate. | query | Необязательный |
| technologyModuleType | string | Фильтрует результирующий набор хостов до тех, где работает указанный модуль кода OneAgent.  Если задано несколько фильтров модуля кода, модуль кода должен соответствовать **всем** фильтрам. Элемент может принимать значения * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` | query | Необязательный |
| technologyModuleVersionIs | string | Фильтрует результирующий набор хостов до тех, где на хосте развёрнута определённая версия модуля кода.  Укажите здесь оператор сравнения.  Если задано несколько фильтров модуля кода, модуль кода должен соответствовать **всем** фильтрам. Элемент может принимать значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| technologyModuleVersionNumber | string | Фильтрует результирующий набор хостов до тех, где на хосте развёрнута определённая версия модуля кода.  Укажите версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5?dt=m).  Если задано несколько фильтров модуля кода, модуль кода должен соответствовать **всем** фильтрам. | query | Необязательный |
| technologyModuleFaultyVersion | boolean | Фильтрует результирующий набор хостов до тех, где работает версия модуля кода, помеченная как сбойная.  Если задано несколько фильтров модуля кода, модуль кода должен соответствовать **всем** фильтрам. | query | Необязательный |
| pluginName | string | Фильтрует результирующий набор хостов до тех, где работает плагин с указанным именем.  К указанному значению применяется оператор **CONTAINS**.  Если задано несколько фильтров плагина, плагин должен соответствовать **всем** фильтрам. | query | Необязательный |
| pluginVersionIs | string | Фильтрует результирующий набор хостов до тех, где на хосте развёрнута определённая версия плагина.  Укажите здесь оператор сравнения.  Если задано несколько фильтров плагина, плагин должен соответствовать **всем** фильтрам. Элемент может принимать значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| pluginVersionNumber | string | Фильтрует результирующий набор хостов до тех, где на хосте развёрнута определённая версия плагина.  Укажите версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5?dt=m).  Части `<minor>` и `<revision>` номера версии необязательны.  Если задано несколько фильтров плагина, плагин должен соответствовать **всем** фильтрам. | query | Необязательный |
| pluginState | string | Фильтрует результирующий набор хостов до тех, где работает плагин с указанным состоянием. Элемент может принимать значения * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов, если результаты не помещаются на одной странице. Значение курсора можно найти на текущей странице ответа, в поле **nextPageKey**.  Чтобы получить последующие страницы, необходимо указать это значение курсора в запросе и сохранить все остальные query-параметры такими же, как в исходном запросе.  Если курсор не указан, всегда возвращается первая страница. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostsListPage](#openapi-definition-HostsListPage) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `HostsListPage`

Список хостов с информацией о развёртывании OneAgent для каждого хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hosts | [HostAgentInfo[]](#openapi-definition-HostAgentInfo) | Список хостов с информацией о развёртывании OneAgent для каждого хоста. |
| nextPageKey | string | Курсор для следующей страницы результатов.  На последней странице имеет значение `null`.  Может существовать следующая страница результатов, даже если текущая страница пуста. |
| percentageOfEnvironmentSearched | number | Прогресс поиска по окружению, в процентах. |

#### Объект `HostAgentInfo`

Развёртывание OneAgent на хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | OneAgent активен (`true`) или неактивен (`false`). |
| autoUpdateSetting | string | Эффективная настройка авто-обновления OneAgent. Для хоста с унаследованной конфигурацией вычисляется из конфигурации его родителя Элемент может принимать значения * `ENABLED` * `DISABLED` |
| availabilityState | string | Состояние доступности OneAgent. Элемент может принимать значения * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` |
| availableVersions | string[] | Список версий, до которых можно обновить OneAgent. |
| configuredMonitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`) в конфигурации OneAgent. |
| configuredMonitoringMode | string | Настроенный режим мониторинга OneAgent. Элемент может принимать значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |
| ~~currentActiveGateId~~ | integer | УСТАРЕЛО  Это поле устарело и предоставлено для обратной совместимости.  Используйте вместо него поле **currentActiveGateIds**. |
| currentActiveGateIds | string[] | Список ID ActiveGate, к которым OneAgent в данный момент подключён. |
| currentNetworkZoneId | string | ID network zone, которую использует OneAgent. |
| detailedAvailabilityState | string | Детальное состояние доступности OneAgent. Элемент может принимать значения * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` |
| faultyVersion | boolean | Версия OneAgent сбойная (`true`) или нет (`false`). |
| hostInfo | [Host](#openapi-definition-Host) | Информация о хосте. |
| modules | [ModuleInfo[]](#openapi-definition-ModuleInfo) | Список модулей кода, развёрнутых на хосте. |
| monitoringType | string | Режим мониторинга OneAgent. Элемент может принимать значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` |
| plugins | [PluginInfo[]](#openapi-definition-PluginInfo) | Список плагинов, развёрнутых на хосте. |
| unlicensed | boolean | OneAgent без лицензии. |
| updateStatus | string | Текущий статус обновления OneAgent. Элемент может принимать значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |

#### Объект `Host`

Информация о хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Определяет версию агента, в данный момент работающего на сущности. |
| amiId | string | - |
| attributes | object | - |
| autoInjection | string | Статус авто-инъекции Элемент может принимать значения * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | Имя, унаследованное от AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | -Элемент может принимать значения * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | -Элемент может принимать значения * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | -Элемент может принимать значения * `32bit` * `64bit` |
| boshAvailabilityZone | string | Зона доступности Cloud Foundry BOSH. |
| boshDeploymentId | string | ID развёртывания Cloud Foundry BOSH. |
| boshInstanceId | string | ID экземпляра Cloud Foundry BOSH. |
| boshInstanceName | string | Имя экземпляра Cloud Foundry BOSH. |
| boshName | string | Имя Cloud Foundry BOSH. |
| boshStemcellVersion | string | Версия stemcell Cloud Foundry BOSH. |
| cloudPlatformVendorVersion | string | Определяет версию вендора облачной платформы. |
| cloudType | string | -Элемент может принимать значения * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Потреблённые Host Units. Применимо только для [Dynatrace classic licensing](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | Настроенное имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в UI. |
| entityId | string | ID сущности Dynatrace требуемой сущности. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | Метка времени, когда сущность была впервые обнаружена, в миллисекундах UTC |
| fromRelationships | object | - |
| gceInstanceId | string | ID экземпляра Google Compute Engine. |
| gceInstanceName | string | Имя экземпляра Google Compute Engine. |
| gceMachineType | string | Тип машины Google Compute Engine. |
| gceProject | string | Проект Google Compute Engine. |
| gceProjectId | string | Числовой ID проекта Google Compute Engine. |
| gcePublicIpAddresses | string[] | Публичные IP-адреса Google Compute Engine. |
| gcpZone | string | Зона Google Cloud Platform. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | -Элемент может принимать значения * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | Кластер kubernetes, в котором находится сущность. |
| kubernetesLabels | object | Метки kubernetes, заданные на сущности. |
| kubernetesNode | string | Узел kubernetes, в котором находится сущность. |
| lastSeenTimestamp | integer | Метка времени, когда сущность была обнаружена в последний раз, в миллисекундах UTC |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | Количество логических CPU экземпляра AIX. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Management zone, в которые входит сущность. |
| monitoringMode | string | -Элемент может принимать значения * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | ID network zone, в которой находится сущность. |
| oneAgentCustomHostName | string | Пользовательское имя, заданное в конфигурации OneAgent. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | -Элемент может принимать значения * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | -Элемент может принимать значения * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии PaaS-агентов, в данный момент работающих на сущности. |
| paasMemoryLimit | integer | - |
| paasType | string | -Элемент может принимать значения * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | Количество одновременных потоков экземпляра AIX. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| userLevel | string | -Элемент может принимать значения * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
| virtualCpus | integer | Количество виртуальных CPU экземпляра AIX. |
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

Определяет версию агента, в данный момент работающего на сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| major | integer | Номер мажорной версии. |
| minor | integer | Номер минорной версии. |
| revision | integer | Номер ревизии. |
| sourceRevision | string | Строковое представление номера SVN-ревизии. |
| timestamp | string | Строка метки времени: формат "yyyymmdd-hhmmss |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `HostGroup`

| Элемент | Тип | Описание |
| --- | --- | --- |
| meId | string | ID сущности Dynatrace для host group. |
| name | string | Имя сущности Dynatrace, отображаемое в UI. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TechnologyInfo`

| Элемент | Тип | Описание |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

#### Объект `ModuleInfo`

Модуль кода OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| instances | [ModuleInstance[]](#openapi-definition-ModuleInstance) | Список экземпляров модуля кода. |
| moduleType | string | Тип модуля кода. Элемент может принимать значения * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` |

#### Объект `ModuleInstance`

Экземпляр модуля кода OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Экземпляр модуля кода активен (`true`) или неактивен (`false`). |
| faultyVersion | boolean | Версия модуля кода сбойная (`true`) или нет (`false`). |
| instanceName | string | Имя экземпляра. |
| moduleVersion | string | Версия модуля кода. |

#### Объект `PluginInfo`

Плагин OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| instances | [PluginInstance[]](#openapi-definition-PluginInstance) | Список экземпляров плагина. |
| pluginName | string | Имя плагина. |

#### Объект `PluginInstance`

Экземпляр плагина OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| pluginVersion | string | Версия плагина. |
| state | string | Состояние экземпляра плагина. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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



"attributes": {



"empty": true



},



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

## Связанные темы

* [OneAgent configuration on a host API](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Управление конфигурацией OneAgent-инстансов на ваших хостах через Dynatrace API.")