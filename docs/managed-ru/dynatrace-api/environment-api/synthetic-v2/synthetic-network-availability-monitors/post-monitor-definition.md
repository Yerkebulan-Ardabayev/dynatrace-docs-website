---
title: Synthetic monitors API v2 - Create Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/post-monitor-definition
---

# Synthetic monitors API v2 - Create Synthetic monitor definition

# Synthetic monitors API v2 - Create Synthetic monitor definition

* Справка
* Обновлено 05 мая 2026 г.

Создаёт новый Synthetic monitor.

* Метод доступен только для browser- и NAM-мониторов. Подробнее о создании browser- или NAM-монитора в UI см. [Browser monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors "Learn about browser monitors.") и [Configure a NAM monitor](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/configure-nam-managed "Learn how to set up and manage a NAM monitor to check the performance and availability of your site.").
* HTTP-монитор можно создать только в UI. Подробнее см. [Create an HTTP monitor in Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.").

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `settings.write`.

О том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

Чтобы найти все варианты модели, зависящие от её типа, см. [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SyntheticMultiProtocolMonitorRequest](#openapi-definition-SyntheticMultiProtocolMonitorRequest) | [SyntheticBrowserMonitorRequest](#openapi-definition-SyntheticBrowserMonitorRequest) | [SyntheticHttpMonitorRequest](#openapi-definition-SyntheticHttpMonitorRequest) | Тело JSON запроса. Содержит параметры монитора. | body | Обязательный |

### Объекты тела запроса


#### Объект `SyntheticMultiProtocolMonitorRequest`


Монитор доступности сети.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Описание монитора | Опциональный |
| enabled | boolean | Если true, монитор включён. | Опциональный |
| frequencyMin | integer | Частота выполнения монитора, в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI_PROTOCOL и HTTP, 15 минут для BROWSER). | Опциональный |
| locations | string[] | Локации, к которым привязан монитор. | Обязательный |
| name | string | Имя монитора. | Обязательный |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. | Опциональный |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Основные теги Grail в виде списка пар «ключ, значение». До 10 тегов. Эти поля доступны только для SaaS, для Managed недоступны. | Опциональный |
| securityContext | string[] | [ФУНКЦИЯ ОТКЛЮЧЕНА] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS, для Managed недоступны. | Опциональный |
| steps | [SyntheticMultiProtocolMonitorStepDto](#openapi-definition-SyntheticMultiProtocolMonitorStepDto)[] | Шаги монитора. | Обязательный |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки простоев. | Опциональный |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, при этом контекст `CONTEXTLESS` и источник 'USER' добавляются автоматически. Однако предпочтительный вариант, использование модели SyntheticTagWithSourceDto. | Опциональный |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Обязательный |


#### Объект `SyntheticMonitorPerformanceThresholdsDto`


Конфигурация пороговых значений производительности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Пороговое значение производительности включено (`true`) или отключено (`false`). | Обязательный |
| thresholds | [SyntheticMonitorPerformanceThresholdDto](#openapi-definition-SyntheticMonitorPerformanceThresholdDto)[] | Список правил пороговых значений производительности. | Опциональный |


#### Объект `SyntheticMonitorPerformanceThresholdDto`


Правило порогового значения производительности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации. Элемент может принимать следующие значения * `AVG` * `MAX` * `MIN` | Опциональный |
| dealertingSamples | integer | Количество последних выполнений запросов без нарушений, после которого проблема закрывается. | Опциональный |
| samples | integer | Количество выполнений запросов в анализируемом скользящем окне (размер скользящего окна). | Опциональный |
| stepIndex | integer | Указывает индекс шага, к которому применяется пороговое значение. Если пороговое значение относится к монитору в целом, индекс не требуется. | Опциональный |
| threshold | number | Уведомлять, если выполнение запроса монитора занимает больше *X* единиц времени. Для мониторов доступности сети единица времени, миллисекунды, для мониторов браузера и HTTP, секунды. | Обязательный |
| type | string | Тип порогового значения производительности. Элемент может принимать следующие значения * `STEP` * `MONITOR` | Опциональный |
| violatingSamples | integer | Количество выполнений запросов с нарушениями в анализируемом скользящем окне. | Опциональный |


#### Объект `SyntheticMonitorPrimaryGrailTagDto`


Пара «ключ, значение» основного grail-тега.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| key | string | Ключ тега. | Обязательный |
| value | string | Значение тега. | Обязательный |


#### Объект `SyntheticMultiProtocolMonitorStepDto`


Шаг монитора доступности сети.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Список ограничений, применяемых ко всем запросам в шаге. | Обязательный |
| name | string | Имя шага. | Обязательный |
| properties | object | Свойства, применяемые ко всем запросам в шаге. | Обязательный |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto)[] | Конфигурации запросов. | Обязательный |
| requestType | string | Тип запроса. Элемент может принимать следующие значения * `ICMP` * `TCP` * `DNS` | Обязательный |
| targetFilter | string | Фильтр цели. | Опциональный |
| targetList | string[] | Список целей. | Опциональный |


#### Объект `SyntheticMonitorConstraintDto`


Ограничение синтетического монитора. Допустимый тип и свойства зависят от контекста монитора и шага/запроса.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| properties | object | Свойства ограничения. Большинство типов ограничений используют ключи operator и value. Некоторые специфичные для протокола ограничения могут использовать дополнительные ключи, например DNS_STATUS_CODE может использовать status. | Обязательный |
| type | string | Тип ограничения. Допустимые значения зависят от типа монитора и контекста шага/запроса. Ограничения шага HTTP-монитора: HTTP_STATUSES, HTTP_RESPONSE_PATTERN, HTTP_RESPONSE_REGEX. Ограничения шага монитора доступности сети (MULTI_PROTOCOL): SUCCESS_RATE_PERCENT. Ограничения конфигурации запроса монитора доступности сети (MULTI_PROTOCOL) специфичны для типа запроса, например ICMP_SUCCESS_RATE_PERCENT (ICMP) и DNS_STATUS_CODE (DNS). | Обязательный |


#### Объект `SyntheticMultiProtocolRequestConfigurationDto`


Конфигурация запроса монитора доступности сети.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Ограничения запроса. | Обязательный |


#### Объект `SyntheticMonitorOutageHandlingSettingsDto`


Конфигурация обработки простоев.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев для всех локаций. | Опциональный |
| globalOutages | boolean | Создавать проблему и отправлять уведомление, когда монитор недоступен во всех настроенных локациях. | Обязательный |
| localConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев. | Опциональный |
| localLocationOutageCountThreshold | integer | Количество локаций со сбоем. | Опциональный |
| localOutages | boolean | Создавать проблему и отправлять уведомление, когда монитор недоступен в течение одного или нескольких последовательных запусков в любой локации. | Обязательный |
| origin | string | Указывает источник этих настроек. Элемент может принимать следующие значения * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Опциональный |
| retryOnError | boolean | Только свойство Browser Monitor. Если установлено значение true, при сбое монитора выполняется повторная попытка. | Опциональный |


#### Объект `SyntheticTagWithSourceDto`


Тег с источником отслеживаемого объекта.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. | Опциональный |
| key | string | Ключ тега. | Обязательный |
| source | string | Источник тега, например USER, RULE_BASED или AUTO. Элемент может принимать следующие значения * `AUTO` * `RULE_BASED` * `USER` | Опциональный |
| value | string | Значение тега. | Опциональный |


#### Объект `SyntheticBrowserMonitorRequest`


Обновление монитора браузера.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| configuration | [SyntheticBrowserMonitorConfigurationDto](#openapi-definition-SyntheticBrowserMonitorConfigurationDto) | Конфигурация Browser Monitor. | Обязательный |
| description | string | Описание монитора | Опциональный |
| enabled | boolean | Если true, монитор включён. | Опциональный |
| frequencyMin | integer | Частота выполнения монитора, в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI_PROTOCOL и HTTP, 15 минут для BROWSER). | Опциональный |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | Конфигурация ключевых метрик производительности. | Опциональный |
| locations | string[] | Локации, к которым привязан монитор. | Обязательный |
| manuallyAssignedEntities | string[] | Вручную назначенные сущности. | Опциональный |
| name | string | Имя монитора. | Обязательный |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. | Опциональный |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Первичные Grail теги в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS, но не для Managed. | Опциональный |
| securityContext | string[] | [FEATURE DISABLED] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS, но не для Managed. | Опциональный |
| steps | [SyntheticBrowserMonitorStepDto](#openapi-definition-SyntheticBrowserMonitorStepDto)[] | Шаги монитора. | Обязательный |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки простоев. | Опциональный |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, а контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. | Опциональный |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Обязательный |


#### Объект `SyntheticBrowserMonitorConfigurationDto`


Конфигурация Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| blockedRequests | string[] | Все запросы, соответствующие указанным шаблонам, будут заблокированы во время выполнения монитора. | Опциональный |
| browserPermissions | [BrowserPermissionsDto](#openapi-definition-BrowserPermissionsDto) | Настройки разрешений для браузера. | Опциональный |
| bypassCSP | boolean | Обход Content Security Policy для отслеживаемых страниц. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| chromiumStartupFlags | [ChromiumStartupFlagsDto](#openapi-definition-ChromiumStartupFlagsDto) | Флаги запуска Chromium для Browser Monitor. | Опциональный |
| clientCertificates | [ClientCertificateDto](#openapi-definition-ClientCertificateDto)[] | Идентификатор сохранённого клиентского сертификата. | Опциональный |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Список cookie. | Опциональный |
| device | [TestDeviceDto](#openapi-definition-TestDeviceDto) | Тестовое устройство Browser Monitor. | Обязательный |
| enablement | [EnablementDto](#openapi-definition-EnablementDto) | Настройки включения browser monitor. | Опциональный |
| experimentalProperties | [MonitorPropertyDto](#openapi-definition-MonitorPropertyDto)[] | Список экспериментальных свойств. | Опциональный |
| filteredRequests | [FilteredRequestsDto](#openapi-definition-FilteredRequestsDto) | Отфильтрованные запросы Browser Monitor. | Опциональный |
| ignoredErrorCodes | [IgnoredErrorCodesDto](#openapi-definition-IgnoredErrorCodesDto) | Игнорируемые коды ошибок Browser Monitor. | Опциональный |
| javaScriptSettings | [JavaScriptAgentSettingsDto](#openapi-definition-JavaScriptAgentSettingsDto) | Настройки JavaScript Agent. | Опциональный |
| monitorFrames | boolean | Сбор метрик производительности для страниц, загруженных во фреймах. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| networkThrottling | [NetworkThrottlingDto](#openapi-definition-NetworkThrottlingDto) | Троттлинг сети Browser Monitor. | Опциональный |
| proxy | [ProxyDto](#openapi-definition-ProxyDto) | Прокси Browser Monitor. | Опциональный |
| requestHeaderOptions | [RequestHeaderOptionsDto](#openapi-definition-RequestHeaderOptionsDto) | Опции заголовков Browser Monitor. | Опциональный |
| useIESupportedAgent | boolean | Флаг useIESupportedAgent. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| userAgent | string | User agent | Опциональный |


#### Объект `BrowserPermissionsDto`


Настройки разрешений для браузера.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| camera | boolean | Разрешение на камеру. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| location | boolean | Разрешение на местоположение. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| microphone | boolean | Разрешение на микрофон. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| notifications | boolean | Разрешение на уведомления. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |


#### Объект `ChromiumStartupFlagsDto`


Флаги запуска Chromium для Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoplay-policy | string | Тип autoplay-policy. Элемент может принимать следующие значения * `no-user-gesture-required` * `document-user-activation-required` | Опциональный |
| disable-features | object | Карта disable-features | Опциональный |
| disable-site-isolation-trials | boolean | Флаг disable-site-isolation-trials. | Опциональный |
| disable-web-security | boolean | Флаг disable-web-security. Если значение не передано, по умолчанию будет установлено false. | Опциональный |
| host-resolver-rules | string | host-resolver-rules. | Опциональный |
| ignore-certificate-errors | boolean | Флаг ignore-certificate-errors. | Опциональный |
| ssl-version-max | string | ssl-version-max. | Опциональный |
| ssl-version-min | string | ssl-version-min. | Опциональный |
| test-type | boolean | Флаг test-type. | Опциональный |


#### Объект `ClientCertificateDto`


Клиентский сертификат.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| credentialId | string | Идентификатор CV сертификата. | Обязательный |
| domain | string | Домен, к которому будет применён сертификат. | Обязательный |


#### Объект `SyntheticMonitorCookieDto`


Dto cookie для шага Synthetic Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| domain | string | Домен cookie. | Обязательный |
| name | string | Имя cookie. | Обязательный |
| path | string | Путь cookie. | Опциональный |
| value | string | Значение cookie. | Обязательный |


#### Объект `TestDeviceDto`


Тестовое устройство Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| height | integer | Высота устройства в px. | Обязательный |
| mobile | boolean | Устройство является мобильным. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| name | string | Имя устройства. | Обязательный |
| touchEnabled | boolean | Устройство поддерживает touch. Если не задано в запросе, по умолчанию будет установлено значение false. | Опциональный |
| width | integer | Ширина устройства в px. | Обязательный |


#### Объект `EnablementDto`


Настройки включения browser monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enableOnGrail | boolean | Включить отправку данных JS agent 3-го поколения. Актуально только для сред SaaS с включённым grail. | Обязательный |
| origin | string | Указывает источник этих настроек. Элемент может принимать следующие значения * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Опциональный |


#### Объект `MonitorPropertyDto`


Свойство Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя свойства. | Обязательный |
| value | string | Значение свойства. | Обязательный |


#### Объект `FilteredRequestsDto`


Отфильтрованные запросы Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| mode | string | Режим фильтрации для отфильтрованных запросов. Элемент может принимать следующие значения * `BLOCK` * `ALLOW` | Обязательный |
| requests | [RequestFilterDto](#openapi-definition-RequestFilterDto)[] | Запросы, подлежащие фильтрации. | Обязательный |


#### Объект `RequestFilterDto`


Фильтр запросов для Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| matchingPattern | string | Регулярное выражение для запроса, к которому будет применён фильтр. | Обязательный |
| type | string | Тип фильтра. Элемент может принимать следующие значения * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` * `REGEX` | Обязательный |


#### Объект `IgnoredErrorCodesDto`


Игнорируемые коды ошибок Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| matchingDocumentRequests | string | Игнорирование кодов состояния будет применяться к запросам, соответствующим шаблону. | Опциональный |
| statusCodes | string | Коды состояния, подлежащие игнорированию. | Опциональный |


#### Объект `JavaScriptAgentSettingsDto`


Настройки JavaScript Agent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customProperties | string | Пользовательские свойства конфигурации | Опционально |
| experimentalValues | boolean | Поддержка экспериментальных значений. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| fetchRequests | boolean | Захват запросов fetch(). Если не задано в запросе, по умолчанию устанавливается в true. | Опционально |
| javaScriptErrors | boolean | Включи эту настройку для мониторинга ошибок JavaScript. Для захвата ошибок JavaScript используется обработчик window.onError. Если не задано в запросе, по умолчанию устанавливается в true. | Опционально |
| javaScriptFrameworkSupport | [FrameworkOptionsDto](#openapi-definition-FrameworkOptionsDto) | Опции JS-фреймворков JS Agent. | Опционально |
| timedActions | boolean | В JavaScript-фреймворках XHR-запросы часто отправляются через методы setTimeout. Включи эту настройку для обнаружения действий, вызывающих такие XHR. Если не задано в запросе, по умолчанию устанавливается в true. | Опционально |
| timeoutSettings | [TimeoutSettingsDto](#openapi-definition-TimeoutSettingsDto) | Настройки таймаута Browser Monitor. | Опционально |
| visuallyCompleteOptions | [VisuallyCompleteOptionsDto](#openapi-definition-VisuallyCompleteOptionsDto) | Опции Visually Complete Browser Monitor. | Опционально |
| xmlHttpRequests | boolean | Захват xml Http requests (XHR). Если не задано в запросе, по умолчанию устанавливается в true. | Опционально |


#### Объект `FrameworkOptionsDto`


Опции JS-фреймворков JS Agent.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| activeXObject | boolean | Поддержка activeXObject. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| angular | boolean | Поддержка Angular. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| dojo | boolean | Поддержка Dojo. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| extJs | boolean | Поддержка extJs. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| icefaces | boolean | Поддержка icefaces. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| jQuery | boolean | Поддержка jquery. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| mooTools | boolean | Поддержка mooTools. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |
| prototype | boolean | Поддержка prototype. Если не задано в запросе, по умолчанию устанавливается в false. | Опционально |


#### Объект `TimeoutSettingsDto`


Настройки таймаута Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Лимит числа каскадных вызовов setTimeout. Если не задано в запросе, по умолчанию устанавливается в 1. | Опционально |
| temporaryActionTotalTimeout | integer | После достижения этого лимита времени дополнительные действия с таймаутом создаваться не будут. Значение должно быть больше 0 мс. Если не задано в запросе, по умолчанию устанавливается в 100. | Опционально |


#### Объект `VisuallyCompleteOptionsDto`


Опции Visually Complete Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| excludedElements | string[] | CSS-селекторы запроса для указания узлов мутации (изменяющихся элементов), которые нужно игнорировать при вычислении Visually complete и Speed index. | Опционально |
| excludedUrls | string[] | Регулярные выражения для определения URL изображений и iFrame, которые нужно исключить из обнаружения модулем Visually complete. | Опционально |
| imageSizeThreshold | integer | Эта настройка определяет минимальную видимую область на элемент (в пикселях), при которой элемент учитывается для Visually complete и Speed index. Если не задано в запросе, по умолчанию устанавливается в 50. | Опционально |
| inactivityTimeout | integer | Время, в течение которого модуль Visually complete ожидает бездействия и отсутствия дальнейших мутаций на странице после действия загрузки. Если не задано в запросе, по умолчанию устанавливается в 1000. | Опционально |
| mutationTimeout | integer | Время, в течение которого модуль Visually complete ожидает после завершения XHR или пользовательского действия перед началом вычисления. Если не задано в запросе, по умолчанию устанавливается в 50. | Опционально |


#### Объект `NetworkThrottlingDto`


Ограничение пропускной способности сети (network throttling) Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| download | integer | Пропускная способность загрузки. Если не задано в запросе, по умолчанию устанавливается в -1. | Опционально |
| latency | integer | Задержка. Если не задано в запросе, по умолчанию устанавливается в 0. | Опционально |
| name | string | Предопределённый тип сети. Если не задано в запросе, по умолчанию устанавливается в "". | Опционально |
| upload | integer | Пропускная способность отдачи. Если не задано в запросе, по умолчанию устанавливается в -1. | Опционально |


#### Объект `ProxyDto`


Прокси Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| pacUrl | string | pacUrl | Обязательно |


#### Объект `RequestHeaderOptionsDto`


Опции заголовков Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| matchingPatterns | string[] | Применять заголовки к запросам, соответствующим шаблону. | Обязательно |
| requestHeaders | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Список заголовков запроса. | Обязательно |


#### Объект `MonitorRequestHeader`


Заголовок Http-запроса


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Имя заголовка. | Обязательно |
| value | string | Значение заголовка. | Обязательно |


#### Объект `KeyPerformanceMetrics`


Конфигурация ключевых метрик производительности.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| loadActionKpm | string | Ключевая метрика производительности действия загрузки. Элемент может принимать следующие значения * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Опционально |
| xhrActionKpm | string | Ключевая метрика производительности XHR-действия. Элемент может принимать следующие значения * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` | Опционально |


#### Объект `SyntheticBrowserMonitorStepDto`


Базовый шаг Browser Monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| entityId | string | Id сущности. | Опционально |
| name | string | Название шага Browser Monitor. | Обязательно |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `NAVIGATE` -> NavigateStepDto * `CLICK` -> InteractionStepDto * `TAP` -> InteractionStepDto * `KEYSTROKES` -> KeyStrokesStepDto * `JAVASCRIPT` -> JavaScriptStepDto * `SELECT_OPTION` -> SelectOptionStepDto * `COOKIE` -> CookieStepDto Элемент может принимать следующие значения * `CLICK` * `COOKIE` * `JAVASCRIPT` * `KEYSTROKES` * `NAVIGATE` * `SELECT_OPTION` * `TAP` | Обязательно |


#### Объект `SyntheticHttpMonitorRequest`


Настройки Http monitor.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| advancedSettings | [SyntheticHttpMonitorAdvancedDto](#openapi-definition-SyntheticHttpMonitorAdvancedDto) | Настройки Http monitor. | Опционально |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Куки монитора. | Опционально |
| description | string | Описание монитора | Опционально |
| enabled | boolean | Если true, монитор включён. | Опционально |
| frequencyMin | integer | Частота работы монитора в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI\_PROTOCOL и HTTP, 15 минут для BROWSER). | Опционально |
| locations | string[] | Локации, к которым привязан монитор. | Обязательно |
| manuallyAssignedEntities | string[] | Вручную назначенные сущности. | Опционально |
| name | string | Название монитора. | Обязательно |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. | Опционально |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail теги в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS, но не для Managed. | Опционально |
| securityContext | string[] | [FEATURE DISABLED] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS, но не для Managed. | Опционально |
| steps | [SyntheticHttpMonitorStepDto](#openapi-definition-SyntheticHttpMonitorStepDto)[] | Шаги монитора. | Обязательно |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки простоя. | Опционально |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору.  Здесь можно указать только значение тега, при этом контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Однако предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. | Опционально |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Обязательно |


#### Объект `SyntheticHttpMonitorAdvancedDto`


Настройки Http monitor.

| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| connectTimeout | integer | Таймаут подключения на запрос, в мс. | Опционально |
| dnsQueryTimeout | integer | Таймаут DNS-запроса, в мс. | Опционально |
| maxCustomScriptSize | integer | Максимальный размер каждого скрипта до или после выполнения, в байтах. | Опционально |
| maxHeaderSize | integer | Максимальный размер каждого заголовка запроса, в байтах. | Опционально |
| maxRequestBodySize | integer | Максимальный размер тела запроса, в байтах. | Опционально |
| maxResponseBodyReadByScriptSize | integer | Максимальный размер тела ответа, читаемого скриптом после выполнения, в байтах. | Опционально |
| maxResponseBodySize | integer | Максимальный размер тела ответа, в байтах. | Опционально |
| monitorExecutionTimeout | integer | Таймаут выполнения монитора, в мс. | Опционально |
| requestTimeout | integer | Таймаут запроса, в мс. | Опционально |
| scriptExecutionTimeout | integer | Таймаут скрипта до или после выполнения, в мс. | Опционально |


#### Объект `SyntheticHttpMonitorStepDto`


Шаг Http-монитора.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| authentication | [SyntheticHttpAuthenticationDto](#openapi-definition-SyntheticHttpAuthenticationDto) | Аутентификация Http-шага. | Опционально |
| configuration | [SyntheticHttpConfigurationDto](#openapi-definition-SyntheticHttpConfigurationDto) | Конфигурация Http-шага. | Опционально |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Список ограничений. | Обязательно |
| entityId | string | Id сущности. | Опционально |
| methodType | string | Тип метода. Элемент может принимать следующие значения * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `OPTIONS` * `PATCH` | Обязательно |
| name | string | Название шага. | Обязательно |
| postScript | string | PostScript. | Опционально |
| preScript | string | PreScript. | Опционально |
| requestBody | string | Тело запроса. | Опционально |
| requestTimeout | integer | Таймаут запроса, в с. | Опционально |
| url | string | Url шага. | Обязательно |


#### Объект `SyntheticHttpAuthenticationDto`


Аутентификация Http-шага.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| credentials | string | Идентификатор в хранилище учётных данных. | Обязательно |
| kdcIp | string | IP KDC, если выбран тип аутентификации KERBEROS. | Опционально |
| realmName | string | Имя realm, если выбран тип KERBEROS. | Опционально |
| type | string | Тип аутентификации. Элемент может принимать следующие значения * `BASIC_AUTHENTICATION` * `NTLM` * `KERBEROS` | Обязательно |


#### Объект `SyntheticHttpConfigurationDto`


Конфигурация Http-шага.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| acceptAnyCertificate | boolean | Если true, принимать любой сертификат. | Опционально |
| clientCertificateId | string | Идентификатор сохранённого сертификата клиента. | Опционально |
| doNotPersistSensitiveData | boolean | Если true, данные шага не сохраняются и не отображаются. | Опционально |
| followRedirects | boolean | Если true, следовать перенаправлениям. | Опционально |
| headers | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Заголовки. | Опционально |
| sslCertificateExpirationDaysToAlert | integer | Число дней до истечения срока действия SSL-сертификата, при котором оповещать. | Опционально |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **200** | [MonitorEntityIdDto](#openapi-definition-MonitorEntityIdDto) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MonitorEntityIdDto`

DTO для ID сущности монитора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | string | ID сущности монитора. |

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



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1"



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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор с одним URL, браузерный clickpath или HTTP-монитор.")