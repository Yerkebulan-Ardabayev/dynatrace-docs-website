---
title: OneAgent на хосте — GET-запрос списка хостов с информацией о OneAgent
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents
scraped: 2026-02-06T16:31:11.346773
---

# OneAgent на хосте — GET-запрос списка хостов с информацией о OneAgent


* Справочник
* Опубликовано 3 февраля 2020

API **OneAgent на хосте** позволяет проверять конфигурацию экземпляров OneAgent на ваших хостах.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/oneagents` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/oneagents` |

## Аутентификация

Для выполнения этого запроса вам нужен токен доступа с одной из следующих областей видимости:

* `oneAgents.read`
* `DataExport`

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, которые запрашиваются из связанных сущностей. Исключение деталей может ускорить запросы. Если не задано, используется `true`. | query | Необязательный |
| startTimestamp | integer | Начальная временная метка запрашиваемого временного интервала, в миллисекундах (UTC). Если не задана, используется значение 72 часа назад от текущего момента. | query | Необязательный |
| endTimestamp | integer | Конечная временная метка запрашиваемого временного интервала, в миллисекундах (UTC). Если не задана, используется текущая временная метка. Временной интервал не должен превышать 7 месяцев (214 дней). | query | Необязательный |
| relativeTime | string | Относительный временной интервал, отсчитываемый назад от текущего момента. Если вам нужно указать относительный интервал, отсутствующий в списке допустимых значений, укажите **startTimestamp** (до 214 дней назад от текущего момента) и оставьте **endTimestamp** и **relativeTime** пустыми. Элемент может содержать следующие значения: * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Необязательный |
| tag | string[] | Фильтрует результирующий набор хостов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам. Для тегов типа «ключ-значение», таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов «ключ-значение» опустите контекст: `tag=key:value`. | query | Необязательный |
| entity | string[] | Фильтрует результат только по указанным хостам. Для указания нескольких хостов используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательный |
| managementZoneId | integer | Возвращает только хосты, входящие в указанную зону управления. Укажите здесь ID зоны управления. | query | Необязательный |
| managementZone | string | Возвращает только хосты, входящие в указанную зону управления. Укажите здесь имя зоны управления. Если задан параметр **managementZoneId**, этот параметр игнорируется. | query | Необязательный |
| networkZoneId | string | Фильтрует результирующий набор хостов по указанной сетевой зоне. Укажите ID сущности Dynatrace необходимой сетевой зоны. Список доступных сетевых зон можно получить с помощью вызова [GET all network zones](https://dt-url.net/u4o3r7z). | query | Необязательный |
| hostGroupId | string | Фильтрует результирующий набор хостов по указанной группе хостов. Укажите ID сущности Dynatrace необходимой группы хостов. | query | Необязательный |
| hostGroupName | string | Фильтрует результирующий набор хостов по указанной группе хостов. Укажите имя необходимой группы хостов. | query | Необязательный |
| osType | string | Фильтрует результирующий набор хостов по типу ОС. Элемент может содержать следующие значения: * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` | query | Необязательный |
| cloudType | string | Фильтрует результирующий набор хостов по типу облака. Элемент может содержать следующие значения: * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` | query | Необязательный |
| autoInjection | string | Фильтрует результирующий набор хостов по статусу автоинъекции. Элемент может содержать следующие значения: * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` | query | Необязательный |
| availabilityState | string | Фильтрует результирующий набор хостов по состоянию доступности OneAgent. * `MONITORED`: Хосты, на которых OneAgent включён и активен. * `UNMONITORED`: Хосты, на которых OneAgent отключён и неактивен. * `CRASHED`: Хосты, на которых OneAgent вернул код состояния аварийного завершения. * `LOST`: Хосты, с которыми невозможно установить соединение с OneAgent. * `PRE_MONITORED`: Хосты, на которых OneAgent инициализируется для мониторинга. * `SHUTDOWN`: Хосты, на которых OneAgent завершает работу в управляемом процессе. * `UNEXPECTED_SHUTDOWN`: Хосты, на которых OneAgent завершает работу в неуправляемом процессе. * `UNKNOWN`: Хосты, на которых состояние OneAgent неизвестно. Элемент может содержать следующие значения: * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` | query | Необязательный |
| detailedAvailabilityState | string | Фильтрует результирующий набор хостов по детальному состоянию доступности OneAgent. * `UNKNOWN`: Хосты, на которых состояние OneAgent неизвестно. * `PRE_MONITORED`: Хосты, на которых OneAgent инициализируется для мониторинга. * `CRASHED_UNKNOWN`: Хосты, на которых OneAgent аварийно завершил работу по неизвестной причине. * `CRASHED_FAILURE`: Хосты, на которых OneAgent вернул код состояния аварийного завершения. * `LOST_UNKNOWN`: Хосты, с которыми невозможно установить соединение с OneAgent по неизвестной причине. * `LOST_CONNECTION`: Хосты, на которых OneAgent был распознан как неактивный. * `LOST_AGENT_UPGRADE_FAILED`: Хосты, на которых OneAgent имеет потенциальную проблему обновления из-за неактивности после обновления. * `SHUTDOWN_UNKNOWN_UNEXPECTED`: Хосты, на которых OneAgent завершает работу в неуправляемом процессе. * `SHUTDOWN_UNKNOWN`: Хосты, на которых OneAgent завершил работу по неизвестной причине. * `SHUTDOWN_GRACEFUL`: Хосты, на которых OneAgent завершил работу из-за выключения хоста. * `SHUTDOWN_STOPPED`: Хосты, на которых OneAgent завершил работу из-за остановки хоста. * `SHUTDOWN_AGENT_LOST`: Хосты, на которых модуль PaaS был распознан как неактивный. * `SHUTDOWN_SPOT_INSTANCE`: Хосты, на которых завершение работы OneAgent было вызвано прерыванием спотового экземпляра AWS. * `SHUTDOWN_K8S_NODE_SHUTDOWN`: Хосты, на которых завершение работы OneAgent было вызвано плавным завершением работы узла k8s. * `UNMONITORED_UNKNOWN`: Хосты, на которых OneAgent отключён и неактивен по неизвестной причине. * `UNMONITORED_TERMINATED`: Хосты, на которых OneAgent завершил работу. * `UNMONITORED_DISABLED`: Хосты, на которых OneAgent был отключён в конфигурации. * `UNMONITORED_AGENT_STOPPED`: Хосты, на которых OneAgent остановлен. * `UNMONITORED_AGENT_RESTART_TRIGGERED`: Хосты, на которых OneAgent перезапускается. * `UNMONITORED_AGENT_UNINSTALLED`: Хосты, на которых OneAgent удалён. * `UNMONITORED_AGENT_DISABLED`: Хосты, на которых OneAgent сообщил, что он отключён. * `UNMONITORED_AGENT_UPGRADE_FAILED`: Хосты, на которых OneAgent имеет потенциальную проблему обновления. * `UNMONITORED_ID_CHANGED`: Хосты, на которых OneAgent потенциально изменил ID при обновлении. * `UNMONITORED_AGENT_LOST`: Хосты, на которых OneAgent был распознан как недоступный из-за проблем связи с сервером. * `UNMONITORED_AGENT_UNREGISTERED`: Хосты, на которых кодовый модуль был распознан как недоступный из-за завершения работы. * `UNMONITORED_AGENT_VERSION_REJECTED`: Хосты, на которых OneAgent был отклонён, поскольку версия не соответствует требованию минимальной версии агента. * `UNMONITORED_AGENT_MIGRATED`: Хосты, на которых OneAgent был перенесён в другое окружение. * `MONITORED`: Хосты, на которых OneAgent включён и активен. * `MONITORED_ENABLED`: Хосты, на которых OneAgent был включён в конфигурации. * `MONITORED_AGENT_REGISTERED`: Хосты, на которых новый OneAgent был распознан. * `MONITORED_AGENT_UPGRADE_STARTED`: Хосты, на которых OneAgent завершил работу из-за обновления. * `MONITORED_AGENT_ENABLED`: Хосты, на которых OneAgent сообщил, что он включён. * `MONITORED_AGENT_VERSION_ACCEPTED`: Хосты, на которых OneAgent был принят, поскольку версия соответствует требованию минимальной версии агента. Элемент может содержать следующие значения: * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` | query | Необязательный |
| monitoringType | string | Фильтрует результирующий набор хостов по режиму мониторинга OneAgent, развёрнутого на хосте. Элемент может содержать следующие значения: * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` | query | Необязательный |
| agentVersionIs | string | Фильтрует результирующий набор хостов по определённой версии OneAgent, развёрнутой на хосте. Укажите здесь оператор сравнения. Элемент может содержать следующие значения: * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| agentVersionNumber | string | Фильтрует результирующий набор хостов по определённой версии OneAgent, развёрнутой на хосте. Укажите версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить с помощью вызова [GET available versions](https://dt-url.net/fo23rb5). | query | Необязательный |
| autoUpdateSetting | string | Фильтрует результирующий набор хостов по текущему состоянию настройки автообновления развёрнутых OneAgent. Элемент может содержать следующие значения: * `ENABLED` * `DISABLED` | query | Необязательный |
| updateStatus | string | Фильтрует результирующий набор хостов по статусу обновления OneAgent, развёрнутого на хосте. Элемент может содержать следующие значения: * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Необязательный |
| faultyVersion | boolean | Фильтрует результирующий набор хостов по тем, которые используют версию OneAgent, отмеченную как неисправная. | query | Необязательный |
| unlicensed | boolean | Фильтрует результирующий набор хостов по тем, которые используют нелицензированный OneAgent. Пример: в вашей лицензии Dynatrace отсутствует требуемая возможность DPS "Foundation & Discovery" для режима Discovery. | query | Необязательный |
| activeGateId | string | Фильтрует результирующий набор хостов по тем, которые в настоящее время подключены к ActiveGate с указанным ID. Используйте ключевое слово **DIRECT\_COMMUNICATION** для поиска хостов, не подключённых ни к какому ActiveGate. | query | Необязательный |
| technologyModuleType | string | Фильтрует результирующий набор хостов по тем, которые используют указанный кодовый модуль OneAgent. Если указано несколько фильтров кодовых модулей, кодовый модуль должен соответствовать **всем** фильтрам. Элемент может содержать следующие значения: * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` | query | Необязательный |
| technologyModuleVersionIs | string | Фильтрует результирующий набор хостов по определённой версии кодового модуля, развёрнутой на хосте. Укажите здесь оператор сравнения. Если указано несколько фильтров кодовых модулей, кодовый модуль должен соответствовать **всем** фильтрам. Элемент может содержать следующие значения: * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| technologyModuleVersionNumber | string | Фильтрует результирующий набор хостов по определённой версии кодового модуля, развёрнутой на хосте. Укажите версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить с помощью вызова [GET available versions](https://dt-url.net/fo23rb5). Если указано несколько фильтров кодовых модулей, кодовый модуль должен соответствовать **всем** фильтрам. | query | Необязательный |
| technologyModuleFaultyVersion | boolean | Фильтрует результирующий набор хостов по тем, которые используют версию кодового модуля, отмеченную как неисправная. Если указано несколько фильтров кодовых модулей, кодовый модуль должен соответствовать **всем** фильтрам. | query | Необязательный |
| pluginName | string | Фильтрует результирующий набор хостов по тем, которые используют плагин с указанным именем. К указанному значению применяется оператор **CONTAINS**. Если указано несколько фильтров плагинов, плагин должен соответствовать **всем** фильтрам. | query | Необязательный |
| pluginVersionIs | string | Фильтрует результирующий набор хостов по определённой версии плагина, развёрнутой на хосте. Укажите здесь оператор сравнения. Если указано несколько фильтров плагинов, плагин должен соответствовать **всем** фильтрам. Элемент может содержать следующие значения: * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| pluginVersionNumber | string | Фильтрует результирующий набор хостов по определённой версии плагина, развёрнутой на хосте. Укажите версию в формате `<major>.<minor>.<revision>`, например `1.182.0`. Список доступных версий можно получить с помощью вызова [GET available versions](https://dt-url.net/fo23rb5). Части `<minor>` и `<revision>` номера версии являются необязательными. Если указано несколько фильтров плагинов, плагин должен соответствовать **всем** фильтрам. | query | Необязательный |
| pluginState | string | Фильтрует результирующий набор хостов по тем, которые используют плагин с указанным состоянием. Элемент может содержать следующие значения: * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов, если результаты не помещаются на одной странице. Значение курсора можно найти на текущей странице ответа в поле **nextPageKey**. Для получения последующих страниц необходимо указать это значение курсора в запросе и сохранить все остальные параметры запроса без изменений. Если курсор не указан, всегда возвращается первая страница. | query | Необязательный |

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
| nextPageKey | string | Курсор для следующей страницы результатов. Имеет значение `null` на последней странице. Следующая страница результатов может существовать, даже если текущая страница пуста. |
| percentageOfEnvironmentSearched | number | Прогресс поиска по окружению, в процентах. |

#### Объект `HostAgentInfo`

Развёртывание OneAgent на хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | OneAgent активен (`true`) или неактивен (`false`). |
| autoUpdateSetting | string | Эффективная настройка автообновления OneAgent. Для хоста с унаследованной конфигурацией рассчитывается из конфигурации родителя. Элемент может содержать следующие значения: * `ENABLED` * `DISABLED` |
| availabilityState | string | Состояние доступности OneAgent. Элемент может содержать следующие значения: * `CRASHED` * `LOST` * `MONITORED` * `PRE_MONITORED` * `SHUTDOWN` * `UNEXPECTED_SHUTDOWN` * `UNKNOWN` * `UNMONITORED` |
| availableVersions | string[] | Список версий, до которых OneAgent может быть обновлён. |
| configuredMonitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`) в конфигурации OneAgent. |
| configuredMonitoringMode | string | Настроенный режим мониторинга OneAgent. Элемент может содержать следующие значения: * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |
| ~~currentActiveGateId~~ | integer | УСТАРЕЛО. Это поле устарело и предоставляется для обратной совместимости. Используйте поле **currentActiveGateIds** вместо него. |
| currentActiveGateIds | string[] | Список ID ActiveGate, к которым OneAgent в настоящее время подключён. |
| currentNetworkZoneId | string | ID сетевой зоны, которую использует OneAgent. |
| detailedAvailabilityState | string | Детальное состояние доступности OneAgent. Элемент может содержать следующие значения: * `CRASHED_FAILURE` * `CRASHED_UNKNOWN` * `LOST_AGENT_UPGRADE_FAILED` * `LOST_CONNECTION` * `LOST_UNKNOWN` * `MONITORED` * `MONITORED_AGENT_ENABLED` * `MONITORED_AGENT_REGISTERED` * `MONITORED_AGENT_UPGRADE_STARTED` * `MONITORED_AGENT_VERSION_ACCEPTED` * `MONITORED_ENABLED` * `PRE_MONITORED` * `SHUTDOWN_AGENT_LOST` * `SHUTDOWN_GRACEFUL` * `SHUTDOWN_K8S_NODE_SHUTDOWN` * `SHUTDOWN_SPOT_INSTANCE` * `SHUTDOWN_STOPPED` * `SHUTDOWN_UNKNOWN` * `SHUTDOWN_UNKNOWN_UNEXPECTED` * `UNKNOWN` * `UNMONITORED_AGENT_DISABLED` * `UNMONITORED_AGENT_LOST` * `UNMONITORED_AGENT_MIGRATED` * `UNMONITORED_AGENT_RESTART_TRIGGERED` * `UNMONITORED_AGENT_STOPPED` * `UNMONITORED_AGENT_UNINSTALLED` * `UNMONITORED_AGENT_UNREGISTERED` * `UNMONITORED_AGENT_UPGRADE_FAILED` * `UNMONITORED_AGENT_VERSION_REJECTED` * `UNMONITORED_DISABLED` * `UNMONITORED_ID_CHANGED` * `UNMONITORED_TERMINATED` * `UNMONITORED_UNKNOWN` |
| faultyVersion | boolean | Версия OneAgent неисправна (`true`) или нет (`false`). |
| hostInfo | [Host](#openapi-definition-Host) | Информация о хосте. |
| modules | [ModuleInfo[]](#openapi-definition-ModuleInfo) | Список кодовых модулей, развёрнутых на хосте. |
| monitoringType | string | Режим мониторинга OneAgent. Элемент может содержать следующие значения: * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` * `STANDALONE` |
| plugins | [PluginInfo[]](#openapi-definition-PluginInfo) | Список плагинов, развёрнутых на хосте. |
| unlicensed | boolean | OneAgent нелицензирован. |
| updateStatus | string | Текущий статус обновления OneAgent. Элемент может содержать следующие значения: * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |

#### Объект `Host`

Информация о хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentVersion | [AgentVersion](#openapi-definition-AgentVersion) | Определяет версию агента, работающего в данный момент на сущности. |
| amiId | string | - |
| autoInjection | string | Статус автоинъекции. Элемент может содержать следующие значения: * `DISABLED_MANUALLY` * `DISABLED_ON_INSTALLATION` * `DISABLED_ON_SANITY_CHECK` * `ENABLED` * `FAILED_ON_INSTALLATION` |
| autoScalingGroup | string | - |
| awsInstanceId | string | - |
| awsInstanceType | string | - |
| awsNameTag | string | Имя, унаследованное от AWS. |
| awsSecurityGroup | string[] | - |
| azureComputeModeName | string | - Элемент может содержать следующие значения: * `DEDICATED` * `SHARED` |
| azureEnvironment | string | - |
| azureHostNames | string[] | - |
| azureResourceGroupName | string | - |
| azureResourceId | string | - |
| azureSiteNames | string[] | - |
| azureSku | string | - Элемент может содержать следующие значения: * `BASIC` * `DYNAMIC` * `FREE` * `PREMIUM` * `SHARED` * `STANDARD` |
| azureVmName | string | - |
| azureVmScaleSetName | string | - |
| azureVmSizeLabel | string | - |
| azureZone | string | - |
| beanstalkEnvironmentName | string | - |
| bitness | string | - Элемент может содержать следующие значения: * `32bit` * `64bit` |
| boshAvailabilityZone | string | Зона доступности Cloud Foundry BOSH. |
| boshDeploymentId | string | ID развёртывания Cloud Foundry BOSH. |
| boshInstanceId | string | ID экземпляра Cloud Foundry BOSH. |
| boshInstanceName | string | Имя экземпляра Cloud Foundry BOSH. |
| boshName | string | Имя Cloud Foundry BOSH. |
| boshStemcellVersion | string | Версия stemcell Cloud Foundry BOSH. |
| cloudPlatformVendorVersion | string | Определяет версию поставщика облачной платформы. |
| cloudType | string | - Элемент может содержать следующие значения: * `AZURE` * `EC2` * `GOOGLE_CLOUD_PLATFORM` * `OPENSTACK` * `ORACLE` * `UNRECOGNIZED` |
| consumedHostUnits | string | Потреблённые единицы хоста. Применимо только для [классического лицензирования Dynatrace](https://www.dynatrace.com/support/help/shortlink/application-and-infrastructure-host-units) |
| cpuCores | integer | - |
| customizedName | string | Пользовательское имя сущности |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | ID сущности Dynatrace требуемой сущности. |
| esxiHostName | string | - |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности, в миллисекундах UTC |
| fromRelationships | object | - |
| gceInstanceId | string | ID экземпляра Google Compute Engine. |
| gceInstanceName | string | Имя экземпляра Google Compute Engine. |
| gceMachineType | string | Тип машины Google Compute Engine. |
| gceProject | string | Проект Google Compute Engine. |
| gceProjectId | string | Числовой ID проекта Google Compute Engine. |
| gcePublicIpAddresses | string[] | Публичные IP-адреса Google Compute Engine. |
| gcpZone | string | Зона Google Cloud Platform. |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | - |
| hypervisorType | string | - Элемент может содержать следующие значения: * `AHV` * `AWS_NITRO` * `GVISOR` * `HYPERV` * `KVM` * `LPAR` * `QEMU` * `UNRECOGNIZED` * `VIRTUALBOX` * `VMWARE` * `WPAR` * `XEN` |
| ipAddresses | string[] | - |
| isMonitoringCandidate | boolean | - |
| kubernetesCluster | string | Кластер Kubernetes, в котором находится сущность. |
| kubernetesLabels | object | Метки Kubernetes, определённые для сущности. |
| kubernetesNode | string | Узел Kubernetes, на котором находится сущность. |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности, в миллисекундах UTC |
| localHostName | string | - |
| localIp | string | - |
| logicalCpuCores | integer | - |
| logicalCpus | integer | Количество логических CPU экземпляра AIX. |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, в которые входит сущность. |
| monitoringMode | string | - Элемент может содержать следующие значения: * `FULL_STACK` * `INFRASTRUCTURE` * `OFF` |
| networkZoneId | string | ID сетевой зоны, в которой находится сущность. |
| oneAgentCustomHostName | string | Пользовательское имя, определённое в конфигурации OneAgent. |
| openStackInstaceType | string | - |
| openstackAvZone | string | - |
| openstackComputeNodeName | string | - |
| openstackProjectName | string | - |
| openstackSecurityGroups | string[] | - |
| openstackVmName | string | - |
| osArchitecture | string | - Элемент может содержать следующие значения: * `ARM` * `IA64` * `PARISC` * `PPC` * `PPCLE` * `S390` * `SPARC` * `X86` * `ZOS` |
| osType | string | - Элемент может содержать следующие значения: * `AIX` * `DARWIN` * `HPUX` * `LINUX` * `SOLARIS` * `WINDOWS` * `ZOS` |
| osVersion | string | - |
| paasAgentVersions | [AgentVersion[]](#openapi-definition-AgentVersion) | Версии агентов PaaS, работающих в данный момент на сущности. |
| paasMemoryLimit | integer | - |
| paasType | string | - Элемент может содержать следующие значения: * `AWS_ECS_EC2` * `AWS_ECS_FARGATE` * `AWS_LAMBDA` * `AZURE_FUNCTIONS` * `AZURE_WEBSITES` * `CLOUD_FOUNDRY` * `GOOGLE_APP_ENGINE` * `GOOGLE_CLOUD_RUN` * `HEROKU` * `KUBERNETES` * `OPENSHIFT` |
| publicHostName | string | - |
| publicIp | string | - |
| scaleSetName | string | - |
| simultaneousMultithreading | integer | Количество одновременных потоков экземпляра AIX. |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| userLevel | string | - Элемент может содержать следующие значения: * `NON_SUPERUSER` * `NON_SUPERUSER_STRICT` * `SUPERUSER` |
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

Определяет версию агента, работающего в данный момент на сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| major | integer | Номер основной версии. |
| minor | integer | Номер минорной версии. |
| revision | integer | Номер ревизии. |
| sourceRevision | string | Строковое представление номера ревизии SVN. |
| timestamp | string | Строка временной метки: формат "yyyymmdd-hhmmss |

#### Объект `HostGroup`

| Элемент | Тип | Описание |
| --- | --- | --- |
| meId | string | ID сущности Dynatrace группы хостов. |
| name | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |

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
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Пользовательские теги содержат значение тега здесь. |
| value | string | Значение тега. Не применимо к пользовательским тегам. |

#### Объект `ModuleInfo`

Кодовый модуль OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| instances | [ModuleInstance[]](#openapi-definition-ModuleInstance) | Список экземпляров кодового модуля. |
| moduleType | string | Тип кодового модуля. Элемент может содержать следующие значения: * `APACHE` * `DOT_NET` * `DUMPPROC` * `GO` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `Z_OS` |

#### Объект `ModuleInstance`

Экземпляр кодового модуля OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Экземпляр кодового модуля активен (`true`) или неактивен (`false`). |
| faultyVersion | boolean | Версия кодового модуля неисправна (`true`) или нет (`false`). |
| instanceName | string | Имя экземпляра. |
| moduleVersion | string | Версия кодового модуля. |

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
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

* [API конфигурации OneAgent на хосте](../../configuration-api/oneagent-configuration/oneagent-on-host.md "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")