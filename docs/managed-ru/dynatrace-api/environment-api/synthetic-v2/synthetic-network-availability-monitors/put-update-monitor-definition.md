---
title: Synthetic monitors API v2 - Update Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/put-update-monitor-definition
---

# Synthetic monitors API v2 - Update Synthetic monitor definition

# Synthetic monitors API v2 - Update Synthetic monitor definition

* Справка
* Обновлено 05 мая 2026 г.

Обновляет определение Synthetic-монитора для заданного ID монитора.

Метод доступен только для мониторов типа browser и NAM.

Запрос принимает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| PUT | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `settings.write`.

О том, как получить и использовать токен, смотри в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все варианты модели, зависящие от типа модели, перечислены в разделе [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| monitorId | string | Идентификатор монитора. | path | Обязательный |
| body | [SyntheticMultiProtocolMonitorRequest](#openapi-definition-SyntheticMultiProtocolMonitorRequest) | [SyntheticBrowserMonitorRequest](#openapi-definition-SyntheticBrowserMonitorRequest) | [SyntheticHttpMonitorRequest](#openapi-definition-SyntheticHttpMonitorRequest) | Тело запроса в формате JSON. Содержит параметры монитора. | body | Обязательный |

### Объекты тела запроса


#### Объект `SyntheticMultiProtocolMonitorRequest`


Монитор сетевой доступности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Описание монитора | Опционально |
| enabled | boolean | Если true, монитор включён. | Опционально |
| frequencyMin | integer | Частота запуска монитора, в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI\_PROTOCOL и HTTP, 15 минут для BROWSER). | Опционально |
| locations | string[] | Локации, к которым привязан монитор. | Обязательно |
| name | string | Имя монитора. | Обязательно |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. | Опционально |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Основные Grail теги в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS, но не для Managed. | Опционально |
| securityContext | string[] | [ФУНКЦИЯ ОТКЛЮЧЕНА] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS, но не для Managed. | Опционально |
| steps | [SyntheticMultiProtocolMonitorStepDto](#openapi-definition-SyntheticMultiProtocolMonitorStepDto)[] | Шаги монитора. | Обязательно |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки простоев. | Опционально |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, тогда контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. | Опционально |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Обязательно |


#### Объект `SyntheticMonitorPerformanceThresholdsDto`


Конфигурация пороговых значений производительности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Пороговое значение производительности включено (`true`) или отключено (`false`). | Обязательно |
| thresholds | [SyntheticMonitorPerformanceThresholdDto](#openapi-definition-SyntheticMonitorPerformanceThresholdDto)[] | Список правил пороговых значений производительности. | Опционально |


#### Объект `SyntheticMonitorPerformanceThresholdDto`


Правило порогового значения производительности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации. Элемент может принимать следующие значения * `AVG` * `MAX` * `MIN` | Опционально |
| dealertingSamples | integer | Количество последних выполнений запроса без нарушений, которое закрывает проблему. | Опционально |
| samples | integer | Количество выполнений запроса в анализируемом скользящем окне (размер скользящего окна). | Опционально |
| stepIndex | integer | Индекс шага, к которому применяется порог. Если порог задан на уровне монитора, индекс не нужен. | Опционально |
| threshold | number | Уведомлять, если выполнение запроса монитора занимает больше *X* единиц времени. Для мониторов сетевой доступности единица времени, это миллисекунды, для мониторов браузера и HTTP, секунды. | Обязательно |
| type | string | Тип порогового значения производительности. Элемент может принимать следующие значения * `STEP` * `MONITOR` | Опционально |
| violatingSamples | integer | Количество выполнений запроса с нарушением в анализируемом скользящем окне. | Опционально |


#### Объект `SyntheticMonitorPrimaryGrailTagDto`


Пара ключ-значение основного grail-тега.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| key | string | Ключ тега. | Обязательно |
| value | string | Значение тега. | Обязательно |


#### Объект `SyntheticMultiProtocolMonitorStepDto`


Шаг монитора сетевой доступности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Список ограничений, применяемых ко всем запросам в шаге. | Обязательно |
| name | string | Имя шага. | Обязательно |
| properties | object | Свойства, применяемые ко всем запросам в шаге. | Обязательно |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto)[] | Конфигурации запросов. | Обязательно |
| requestType | string | Тип запроса. Элемент может принимать следующие значения * `ICMP` * `TCP` * `DNS` | Обязательно |
| targetFilter | string | Фильтр целей. | Опционально |
| targetList | string[] | Список целей. | Опционально |


#### Объект `SyntheticMonitorConstraintDto`


Ограничение synthetic-монитора. Допустимый тип и свойства зависят от контекста монитора и шага/запроса.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| properties | object | Свойства ограничения. Большинство типов ограничений используют ключи operator и value. Некоторые ограничения, специфичные для протокола, могут использовать дополнительные ключи, например DNS\_STATUS\_CODE может использовать status. | Обязательно |
| type | string | Тип ограничения. Допустимые значения зависят от типа монитора и контекста шага/запроса. Ограничения шага HTTP-монитора: HTTP\_STATUSES, HTTP\_RESPONSE\_PATTERN, HTTP\_RESPONSE\_REGEX. Ограничения шага монитора сетевой доступности (MULTI\_PROTOCOL): SUCCESS\_RATE\_PERCENT. Ограничения конфигурации запроса монитора сетевой доступности (MULTI\_PROTOCOL) специфичны для типа запроса, например ICMP\_SUCCESS\_RATE\_PERCENT (ICMP) и DNS\_STATUS\_CODE (DNS). | Обязательно |


#### Объект `SyntheticMultiProtocolRequestConfigurationDto`


Конфигурация запроса монитора сетевой доступности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Ограничения запроса. | Обязательно |


#### Объект `SyntheticMonitorOutageHandlingSettingsDto`


Конфигурация обработки простоев.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев для всех локаций. | Опционально |
| globalOutages | boolean | Создавать проблему и отправлять оповещение, когда монитор недоступен во всех настроенных локациях. | Обязательно |
| localConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев. | Опционально |
| localLocationOutageCountThreshold | integer | Количество локаций со сбоями. | Опционально |
| localOutages | boolean | Создавать проблему и отправлять оповещение, когда монитор недоступен в течение одного или нескольких последовательных запусков в любой локации. | Обязательно |
| origin | string | Указывает источник этих настроек. Элемент может принимать следующие значения * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Опционально |
| retryOnError | boolean | Свойство только для Browser Monitor. Если установлено в true, при сбое монитора будет выполнена повторная попытка выполнения. | Опционально |


#### Объект `SyntheticTagWithSourceDto`


Тег с источником отслеживаемой сущности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. | Опционально |
| key | string | Ключ тега. | Обязательно |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO. Элемент может принимать следующие значения * `AUTO` * `RULE_BASED` * `USER` | Опционально |
| value | string | Значение тега. | Опционально |


#### Объект `SyntheticBrowserMonitorRequest`


Обновление browser-монитора.

| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| configuration | [SyntheticBrowserMonitorConfigurationDto](#openapi-definition-SyntheticBrowserMonitorConfigurationDto) | Конфигурация Browser Monitor. | Обязательно |
| description | string | Описание монитора | Опционально |
| enabled | boolean | Если true, монитор включён. | Опционально |
| frequencyMin | integer | Частота выполнения монитора в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI\_PROTOCOL и HTTP, 15 минут для BROWSER). | Опционально |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | Конфигурация ключевых показателей производительности. | Опционально |
| locations | string[] | Локации, к которым привязан монитор. | Обязательно |
| manuallyAssignedEntities | string[] | Вручную назначенные сущности. | Опционально |
| name | string | Имя монитора. | Обязательно |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. | Опционально |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Основные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS и недоступны для Managed. | Опционально |
| securityContext | string[] | [ФУНКЦИЯ ОТКЛЮЧЕНА] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS и недоступны для Managed. | Опционально |
| steps | [SyntheticBrowserMonitorStepDto](#openapi-definition-SyntheticBrowserMonitorStepDto)[] | Шаги монитора. | Обязательно |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки простоев. | Опционально |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, а контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, использование модели SyntheticTagWithSourceDto. | Опционально |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Обязательно |


#### Объект `SyntheticBrowserMonitorConfigurationDto`


Конфигурация Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| blockedRequests | string[] | Все запросы, соответствующие указанным шаблонам, будут блокироваться во время выполнения монитора. | Опционально |
| browserPermissions | [BrowserPermissionsDto](#openapi-definition-BrowserPermissionsDto) | Настройки разрешений браузера. | Опционально |
| bypassCSP | boolean | Обход Content Security Policy для отслеживаемых страниц. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| chromiumStartupFlags | [ChromiumStartupFlagsDto](#openapi-definition-ChromiumStartupFlagsDto) | Флаги запуска Chromium для Browser Monitor. | Опционально |
| clientCertificates | [ClientCertificateDto](#openapi-definition-ClientCertificateDto)[] | Идентификатор сохранённого клиентского сертификата. | Опционально |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Список cookie. | Опционально |
| device | [TestDeviceDto](#openapi-definition-TestDeviceDto) | Тестовое устройство Browser Monitor. | Обязательно |
| enablement | [EnablementDto](#openapi-definition-EnablementDto) | Настройки включения browser monitor. | Опционально |
| experimentalProperties | [MonitorPropertyDto](#openapi-definition-MonitorPropertyDto)[] | Список экспериментальных свойств. | Опционально |
| filteredRequests | [FilteredRequestsDto](#openapi-definition-FilteredRequestsDto) | Отфильтрованные запросы Browser Monitor. | Опционально |
| ignoredErrorCodes | [IgnoredErrorCodesDto](#openapi-definition-IgnoredErrorCodesDto) | Игнорируемые коды ошибок Browser Monitor. | Опционально |
| javaScriptSettings | [JavaScriptAgentSettingsDto](#openapi-definition-JavaScriptAgentSettingsDto) | Настройки JavaScript Agent. | Опционально |
| monitorFrames | boolean | Сбор показателей производительности для страниц, загруженных во фреймах. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| networkThrottling | [NetworkThrottlingDto](#openapi-definition-NetworkThrottlingDto) | Ограничение пропускной способности сети для Browser Monitor. | Опционально |
| proxy | [ProxyDto](#openapi-definition-ProxyDto) | Прокси Browser Monitor. | Опционально |
| requestHeaderOptions | [RequestHeaderOptionsDto](#openapi-definition-RequestHeaderOptionsDto) | Параметры заголовков Browser Monitor. | Опционально |
| useIESupportedAgent | boolean | Флаг useIESupportedAgent. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| userAgent | string | User agent | Опционально |


#### Объект `BrowserPermissionsDto`


Настройки разрешений браузера.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| camera | boolean | Разрешение на камеру. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| location | boolean | Разрешение на геолокацию. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| microphone | boolean | Разрешение на микрофон. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| notifications | boolean | Разрешение на уведомления. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |


#### Объект `ChromiumStartupFlagsDto`


Флаги запуска Chromium для Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| autoplay-policy | string | Тип autoplay-policy. Элемент может принимать следующие значения * `no-user-gesture-required` * `document-user-activation-required` | Опционально |
| disable-features | object | Карта disable-features | Опционально |
| disable-site-isolation-trials | boolean | Флаг disable-site-isolation-trials. | Опционально |
| disable-web-security | boolean | Флаг disable-web-security. Если значение не передано, по умолчанию будет установлено false. | Опционально |
| host-resolver-rules | string | host-resolver-rules. | Опционально |
| ignore-certificate-errors | boolean | Флаг ignore-certificate-errors. | Опционально |
| ssl-version-max | string | ssl-version-max. | Опционально |
| ssl-version-min | string | ssl-version-min. | Опционально |
| test-type | boolean | Флаг test-type. | Опционально |


#### Объект `ClientCertificateDto`


Клиентский сертификат.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| credentialId | string | Идентификатор CV сертификата. | Обязательно |
| domain | string | Домен, к которому будет применён сертификат. | Обязательно |


#### Объект `SyntheticMonitorCookieDto`


Dto cookie для шага Synthetic Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| domain | string | Домен cookie. | Обязательно |
| name | string | Имя cookie. | Обязательно |
| path | string | Путь cookie. | Опционально |
| value | string | Значение cookie. | Обязательно |


#### Объект `TestDeviceDto`


Тестовое устройство Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| height | integer | Высота устройства в px. | Обязательно |
| mobile | boolean | Устройство является мобильным. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| name | string | Имя устройства. | Обязательно |
| touchEnabled | boolean | У устройства включён touch. Если не указано в запросе, по умолчанию будет установлено значение false. | Опционально |
| width | integer | Ширина устройства в px. | Обязательно |


#### Объект `EnablementDto`


Настройки включения browser monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| enableOnGrail | boolean | Включить отчётность JS agent 3-го поколения. Актуально только для сред SaaS с включённым grail. | Обязательно |
| origin | string | Указывает источник этих настроек. Элемент может принимать следующие значения * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Опционально |


#### Объект `MonitorPropertyDto`


Свойство Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| name | string | Имя свойства. | Обязательно |
| value | string | Значение свойства. | Обязательно |


#### Объект `FilteredRequestsDto`


Отфильтрованные запросы Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| mode | string | Режим фильтрации отфильтрованных запросов. Элемент может принимать следующие значения * `BLOCK` * `ALLOW` | Обязательно |
| requests | [RequestFilterDto](#openapi-definition-RequestFilterDto)[] | Запросы для фильтрации. | Обязательно |


#### Объект `RequestFilterDto`


Фильтр запросов для Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| matchingPattern | string | Регулярное выражение для запроса, к которому будет применён фильтр. | Обязательно |
| type | string | Тип фильтра. Элемент может принимать следующие значения * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` * `REGEX` | Обязательно |


#### Объект `IgnoredErrorCodesDto`


Игнорируемые коды ошибок Browser Monitor.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| matchingDocumentRequests | string | Игнорирование кодов состояния будет применяться к запросам, соответствующим шаблону. | Опционально |
| statusCodes | string | Коды состояния, которые нужно игнорировать. | Опционально |


#### Объект `JavaScriptAgentSettingsDto`


Настройки JavaScript Agent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customProperties | string | Пользовательские свойства конфигурации | Необязательный |
| experimentalValues | boolean | Поддержка экспериментальных значений. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| fetchRequests | boolean | Захват запросов fetch(). Если не задано в запросе, по умолчанию устанавливается значение true. | Необязательный |
| javaScriptErrors | boolean | Включает этот параметр для мониторинга ошибок JavaScript. Для захвата ошибок JavaScript используется обработчик window.onError. Если не задано в запросе, по умолчанию устанавливается значение true. | Необязательный |
| javaScriptFrameworkSupport | [FrameworkOptionsDto](#openapi-definition-FrameworkOptionsDto) | Параметры JS-фреймворка для JS Agent. | Необязательный |
| timedActions | boolean | В JavaScript-фреймворках XHR часто отправляются через методы setTimeout. Включите этот параметр для обнаружения действий, которые запускают такие XHR. Если не задано в запросе, по умолчанию устанавливается значение true. | Необязательный |
| timeoutSettings | [TimeoutSettingsDto](#openapi-definition-TimeoutSettingsDto) | Настройки тайм-аута Browser Monitor. | Необязательный |
| visuallyCompleteOptions | [VisuallyCompleteOptionsDto](#openapi-definition-VisuallyCompleteOptionsDto) | Параметры Visually Complete для Browser Monitor. | Необязательный |
| xmlHttpRequests | boolean | Захват XML HTTP-запросов (XHR). Если не задано в запросе, по умолчанию устанавливается значение true. | Необязательный |


#### Объект `FrameworkOptionsDto`


Параметры JS-фреймворка для JS Agent.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| activeXObject | boolean | Поддержка activeXObject. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| angular | boolean | Поддержка Angular. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| dojo | boolean | Поддержка Dojo. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| extJs | boolean | Поддержка extJs. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| icefaces | boolean | Поддержка icefaces. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| jQuery | boolean | Поддержка jquery. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| mooTools | boolean | Поддержка mooTools. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |
| prototype | boolean | Поддержка prototype. Если не задано в запросе, по умолчанию устанавливается значение false. | Необязательный |


#### Объект `TimeoutSettingsDto`


Настройки тайм-аута Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Ограничение количества каскадных вызовов setTimeout. Если не задано в запросе, по умолчанию устанавливается значение 1. | Необязательный |
| temporaryActionTotalTimeout | integer | После достижения этого лимита времени дополнительные действия с тайм-аутом создаваться не будут. Значение должно быть больше 0 мс. Если не задано в запросе, по умолчанию устанавливается значение 100. | Необязательный |


#### Объект `VisuallyCompleteOptionsDto`


Параметры Visually Complete для Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| excludedElements | string[] | CSS-селекторы запросов для указания узлов мутации (изменяющихся элементов), которые нужно игнорировать при расчёте Visually complete и Speed index. | Необязательный |
| excludedUrls | string[] | Регулярные выражения для определения URL изображений и iFrame, которые нужно исключить из обнаружения модулем Visually complete. | Необязательный |
| imageSizeThreshold | integer | Этот параметр задаёт минимальную видимую область на элемент (в пикселях), при которой элемент учитывается для Visually complete и Speed index. Если не задано в запросе, по умолчанию устанавливается значение 50. | Необязательный |
| inactivityTimeout | integer | Время, в течение которого модуль Visually complete ожидает бездействия и отсутствия дальнейших мутаций на странице после действия загрузки. Если не задано в запросе, по умолчанию устанавливается значение 1000. | Необязательный |
| mutationTimeout | integer | Время, в течение которого модуль Visually complete ожидает после закрытия XHR или пользовательского действия, прежде чем начать расчёт. Если не задано в запросе, по умолчанию устанавливается значение 50. | Необязательный |


#### Объект `NetworkThrottlingDto`


Ограничение пропускной способности сети Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| download | integer | Пропускная способность загрузки. Если не задано в запросе, по умолчанию устанавливается значение -1. | Необязательный |
| latency | integer | Задержка. Если не задано в запросе, по умолчанию устанавливается значение 0. | Необязательный |
| name | string | Предустановленный тип сети. Если не задано в запросе, по умолчанию устанавливается значение "". | Необязательный |
| upload | integer | Пропускная способность отдачи. Если не задано в запросе, по умолчанию устанавливается значение -1. | Необязательный |


#### Объект `ProxyDto`


Прокси Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| pacUrl | string | pacUrl | Обязательный |


#### Объект `RequestHeaderOptionsDto`


Параметры заголовков Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| matchingPatterns | string[] | Применить заголовки к запросам, соответствующим шаблону. | Обязательный |
| requestHeaders | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Список заголовков запроса. | Обязательный |


#### Объект `MonitorRequestHeader`


Заголовок Http-запроса


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя заголовка. | Обязательный |
| value | string | Значение заголовка. | Обязательный |


#### Объект `KeyPerformanceMetrics`


Конфигурация ключевых показателей производительности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| loadActionKpm | string | Ключевой показатель производительности действия загрузки. Элемент может принимать следующие значения * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Необязательный |
| xhrActionKpm | string | Ключевой показатель производительности действия XHR. Элемент может принимать следующие значения * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` | Необязательный |


#### Объект `SyntheticBrowserMonitorStepDto`


Базовый шаг Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| entityId | string | Id сущности. | Необязательный |
| name | string | Название шага Browser Monitor. | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `NAVIGATE` -> NavigateStepDto * `CLICK` -> InteractionStepDto * `TAP` -> InteractionStepDto * `KEYSTROKES` -> KeyStrokesStepDto * `JAVASCRIPT` -> JavaScriptStepDto * `SELECT_OPTION` -> SelectOptionStepDto * `COOKIE` -> CookieStepDto Элемент может принимать следующие значения * `CLICK` * `COOKIE` * `JAVASCRIPT` * `KEYSTROKES` * `NAVIGATE` * `SELECT_OPTION` * `TAP` | Обязательный |


#### Объект `SyntheticHttpMonitorRequest`


Настройки Http monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| advancedSettings | [SyntheticHttpMonitorAdvancedDto](#openapi-definition-SyntheticHttpMonitorAdvancedDto) | Настройки Http monitor. | Необязательный |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Cookie монитора. | Необязательный |
| description | string | Описание монитора | Необязательный |
| enabled | boolean | Если true, монитор включён. | Необязательный |
| frequencyMin | integer | Частота монитора, в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI\_PROTOCOL и HTTP, 15 минут для BROWSER). | Необязательный |
| locations | string[] | Локации, к которым назначен монитор. | Обязательный |
| manuallyAssignedEntities | string[] | Сущности, назначенные вручную. | Необязательный |
| name | string | Название монитора. | Обязательный |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. | Необязательный |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Основные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS и недоступны для Managed. | Необязательный |
| securityContext | string[] | [ФУНКЦИЯ ОТКЛЮЧЕНА] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS и недоступны для Managed. | Необязательный |
| steps | [SyntheticHttpMonitorStepDto](#openapi-definition-SyntheticHttpMonitorStepDto)[] | Шаги монитора. | Обязательный |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки сбоев. | Необязательный |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, тогда контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительным вариантом является использование модели SyntheticTagWithSourceDto. | Необязательный |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Обязательный |


#### Объект `SyntheticHttpMonitorAdvancedDto`


Настройки Http monitor.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| connectTimeout | integer | Таймаут подключения на запрос в мс. | Опционально |
| dnsQueryTimeout | integer | Таймаут DNS-запроса в мс. | Опционально |
| maxCustomScriptSize | integer | Максимальный размер каждого скрипта pre- или post-выполнения в байтах. | Опционально |
| maxHeaderSize | integer | Максимальный размер каждого заголовка запроса в байтах. | Опционально |
| maxRequestBodySize | integer | Максимальный размер тела запроса в байтах. | Опционально |
| maxResponseBodyReadByScriptSize | integer | Максимальный размер тела ответа, читаемого скриптом post-выполнения, в байтах. | Опционально |
| maxResponseBodySize | integer | Максимальный размер тела ответа в байтах. | Опционально |
| monitorExecutionTimeout | integer | Таймаут выполнения монитора в мс. | Опционально |
| requestTimeout | integer | Таймаут запроса в мс. | Опционально |
| scriptExecutionTimeout | integer | Таймаут скрипта pre- или post-выполнения в мс. | Опционально |


#### Объект `SyntheticHttpMonitorStepDto`


Шаг Http-монитора.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| authentication | [SyntheticHttpAuthenticationDto](#openapi-definition-SyntheticHttpAuthenticationDto) | Аутентификация Http-шага. | Опционально |
| configuration | [SyntheticHttpConfigurationDto](#openapi-definition-SyntheticHttpConfigurationDto) | Конфигурация Http-шага. | Опционально |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Список ограничений. | Обязательно |
| entityId | string | Id сущности. | Опционально |
| methodType | string | Тип метода. Элемент может принимать следующие значения * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `OPTIONS` * `PATCH` | Обязательно |
| name | string | Имя шага. | Обязательно |
| postScript | string | PostScript. | Опционально |
| preScript | string | PreScript. | Опционально |
| requestBody | string | Тело запроса. | Опционально |
| requestTimeout | integer | Таймаут запроса в секундах. | Опционально |
| url | string | Url шага. | Обязательно |


#### Объект `SyntheticHttpAuthenticationDto`


Аутентификация Http-шага.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| credentials | string | Идентификатор хранилища учётных данных. | Обязательно |
| kdcIp | string | IP KDC на случай, если выбран тип аутентификации KERBEROS. | Опционально |
| realmName | string | Имя realm на случай, если выбран тип KERBEROS. | Опционально |
| type | string | Тип аутентификации. Элемент может принимать следующие значения * `BASIC_AUTHENTICATION` * `NTLM` * `KERBEROS` | Обязательно |


#### Объект `SyntheticHttpConfigurationDto`


Конфигурация Http-шага.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| acceptAnyCertificate | boolean | Если true, флаг принятия любого сертификата. | Опционально |
| clientCertificateId | string | Идентификатор сохранённого клиентского сертификата. | Опционально |
| doNotPersistSensitiveData | boolean | Если true, данные шага не сохраняются и не отображаются. | Опционально |
| followRedirects | boolean | Если true, переходить по редиректам. | Опционально |
| headers | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Заголовки. | Опционально |
| sslCertificateExpirationDaysToAlert | integer | Количество дней до истечения срока действия SSL-сертификата. | Опционально |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"description": "My network availability monitor description",



"enabled": "true",



"frequencyMin": "60",



"locations": [



"SYNTHETIC_LOCATION-D3A5BFD8676A4F19"



],



"name": "My network availability monitor",



"performanceThresholds": {



"enabled": "true",



"thresholds": [



{



"aggregation": "AVG",



"dealertingSamples": "5",



"samples": "5",



"stepIndex": "0",



"threshold": "200",



"violatingSamples": "3"



}



]



},



"primaryGrailTags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "another sample key",



"value": "another sample value"



}



],



"securityContext": [



"sample security context",



"another security context"



],



"steps": [



{



"constraints": [



{



"properties": {



"operator": ">=",



"value": "95"



},



"type": "SUCCESS_RATE_PERCENT"



}



],



"name": "Step 1",



"properties": {



"ICMP_IP_VERSION": "4",



"ICMP_NUMBER_OF_PACKETS": "8",



"ICMP_TIMEOUT_FOR_REPLY": "PT1S"



},



"requestConfigurations": [



{



"constraints": [



{



"properties": {



"operator": "=",



"value": "100"



},



"type": "ICMP_SUCCESS_RATE_PERCENT"



}



]



}



],



"requestType": "ICMP",



"targetFilter": "ipMask == 127.0.0.1/24",



"targetList": [



"127.0.0.1",



"127.0.0.2"



]



}



],



"syntheticMonitorOutageHandlingSettings": {



"globalConsecutiveOutageCountThreshold": "1",



"globalOutages": "true",



"localConsecutiveOutageCountThreshold": "3",



"localLocationOutageCountThreshold": "3",



"localOutages": "true"



},



"tags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "sample key"



}



],



"type": "MULTI_PROTOCOL"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Тело ответа отсутствует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать монитор с одним URL для браузера, клик-путь для браузера или HTTP-монитор.")