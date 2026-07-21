---
title: Synthetic monitors API v2 - GET Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-monitor-definition
---

# Synthetic monitors API v2 - GET Synthetic monitor definition

# Synthetic monitors API v2 - GET Synthetic monitor definition

* Справочник
* Обновлено 05 мая 2026 г.

Получение определения Synthetic-монитора по идентификатору монитора.

Метод доступен только для браузерных мониторов и мониторов NAM.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `settings.read`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| monitorId | string | Идентификатор монитора. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticMultiProtocolMonitorResponse](#openapi-definition-SyntheticMultiProtocolMonitorResponse) | [SyntheticBrowserMonitorResponse](#openapi-definition-SyntheticBrowserMonitorResponse) | [SyntheticHttpMonitorResponse](#openapi-definition-SyntheticHttpMonitorResponse) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа


#### Объект `SyntheticMultiProtocolMonitorResponse`


Монитор доступности сети.


| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание монитора |
| enabled | boolean | Если `true`, монитор включён. |
| entityId | string | ID сущности монитора. |
| frequencyMin | integer | Частота работы монитора, в минутах. |
| locations | string[] | Локации, к которым назначен монитор. |
| modificationTimestamp | integer | Метка времени последнего изменения |
| name | string | Имя монитора. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Первичные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS, но не для Managed. |
| securityContext | string[] | [ФУНКЦИЯ ОТКЛЮЧЕНА] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS, но не для Managed. |
| steps | [SyntheticMultiProtocolMonitorStepDto](#openapi-definition-SyntheticMultiProtocolMonitorStepDto)[] | Шаги монитора. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки сбоев. |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` |


#### Объект `SyntheticMonitorPerformanceThresholdsDto`


Конфигурация пороговых значений производительности.


| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Порог производительности включён (`true`) или отключён (`false`). |
| thresholds | [SyntheticMonitorPerformanceThresholdDto](#openapi-definition-SyntheticMonitorPerformanceThresholdDto)[] | Список правил пороговых значений производительности. |


#### Объект `SyntheticMonitorPerformanceThresholdDto`


Правило порогового значения производительности.


| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации. Элемент может принимать следующие значения * `AVG` * `MAX` * `MIN` |
| dealertingSamples | integer | Количество последних неконфликтующих (не нарушающих порог) выполнений запросов, которые закрывают проблему. |
| samples | integer | Количество выполнений запросов в анализируемом скользящем окне (размер скользящего окна). |
| stepIndex | integer | Указывает индекс шага, к которому применяется порог. Если порог задан на уровне монитора, индекс не нужен. |
| threshold | number | Уведомлять, если выполнение запроса монитора занимает больше времени, чем *X* единиц времени. Для мониторов доступности сети единица времени, это миллисекунды, для мониторов Browser и HTTP, секунды. |
| type | string | Тип порогового значения производительности. Элемент может принимать следующие значения * `STEP` * `MONITOR` |
| violatingSamples | integer | Количество выполнений запросов с нарушением порога в анализируемом скользящем окне. |


#### Объект `SyntheticMonitorPrimaryGrailTagDto`


Пара ключ-значение первичного тега grail.


| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ тега. |
| value | string | Значение тега. |


#### Объект `SyntheticMultiProtocolMonitorStepDto`


Шаг монитора доступности сети.


| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Список ограничений, которые применяются ко всем запросам в шаге. |
| name | string | Имя шага. |
| properties | object | Свойства, которые применяются ко всем запросам в шаге. |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto)[] | Конфигурации запросов. |
| requestType | string | Тип запроса. Элемент может принимать следующие значения * `ICMP` * `TCP` * `DNS` |
| targetFilter | string | Фильтр цели. |
| targetList | string[] | Список целей. |


#### Объект `SyntheticMonitorConstraintDto`


Ограничение синтетического монитора. Допустимый тип и свойства зависят от контекста монитора и шага/запроса.


| Элемент | Тип | Описание |
| --- | --- | --- |
| properties | object | Свойства ограничения. Большинство типов ограничений используют ключи operator и value. Некоторые ограничения, специфичные для протокола, могут использовать дополнительные ключи, например DNS\_STATUS\_CODE может использовать status. |
| type | string | Тип ограничения. Допустимые значения зависят от типа монитора и контекста шага/запроса. Ограничения шага монитора HTTP: HTTP\_STATUSES, HTTP\_RESPONSE\_PATTERN, HTTP\_RESPONSE\_REGEX. Ограничения шага монитора доступности сети (MULTI\_PROTOCOL): SUCCESS\_RATE\_PERCENT. Ограничения конфигурации запроса монитора доступности сети (MULTI\_PROTOCOL) специфичны для типа запроса, например ICMP\_SUCCESS\_RATE\_PERCENT (ICMP) и DNS\_STATUS\_CODE (DNS). |


#### Объект `SyntheticMultiProtocolRequestConfigurationDto`


Конфигурация запроса монитора доступности сети.


| Элемент | Тип | Описание |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Ограничения запроса. |


#### Объект `SyntheticMonitorOutageHandlingSettingsDto`


Конфигурация обработки сбоев.


| Элемент | Тип | Описание |
| --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев для всех локаций. |
| globalOutages | boolean | Создавать проблему и отправлять оповещение, когда монитор недоступен во всех настроенных локациях. |
| localConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев. |
| localLocationOutageCountThreshold | integer | Количество сбойных локаций. |
| localOutages | boolean | Создавать проблему и отправлять оповещение, когда монитор недоступен при одном или нескольких последовательных запусках в любой локации. |
| origin | string | Указывает источник этих настроек. Элемент может принимать следующие значения * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` |
| retryOnError | boolean | Свойство только для Browser Monitor. Если установлено в `true`, при сбое монитора будет выполнена повторная попытка. |


#### Объект `SyntheticTagWithSourceDto`


Тег с источником отслеживаемой сущности.


| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник происхождения тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO. Элемент может принимать следующие значения * `AUTO` * `RULE_BASED` * `USER` |
| value | string | Значение тега. |


#### Объект `SyntheticBrowserMonitorResponse`


Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| automaticallyAssignedEntities | string[] | Автоматически назначенные сущности. |
| configuration | [SyntheticBrowserMonitorConfigurationDto](#openapi-definition-SyntheticBrowserMonitorConfigurationDto) | Конфигурация Browser Monitor. |
| description | string | Описание монитора |
| enabled | boolean | Если `true`, монитор включён. |
| entityId | string | ID сущности монитора. |
| frequencyMin | integer | Частота работы монитора, в минутах. |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | Конфигурация ключевых метрик производительности. |
| locations | string[] | Локации, к которым назначен монитор. |
| manuallyAssignedEntities | string[] | Вручную назначенные сущности. |
| modificationTimestamp | integer | Метка времени последнего изменения |
| name | string | Имя монитора. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Первичные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS, но не для Managed. |
| securityContext | string[] | [ФУНКЦИЯ ОТКЛЮЧЕНА] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS, но не для Managed. |
| steps | [SyntheticBrowserMonitorStepDto](#openapi-definition-SyntheticBrowserMonitorStepDto)[] | Шаги монитора. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки сбоев. |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору. Здесь можно указать только значение тега, контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` |


#### Объект `SyntheticBrowserMonitorConfigurationDto`


Конфигурация Browser Monitor.

| Элемент | Тип | Описание |
| --- | --- | --- |
| blockedRequests | string[] | Все запросы, соответствующие указанным паттернам, будут блокироваться во время выполнения монитора. |
| browserPermissions | [BrowserPermissionsDto](#openapi-definition-BrowserPermissionsDto) | Настройки разрешений для браузера. |
| bypassCSP | boolean | Обход Content Security Policy для отслеживаемых страниц. Если не задано в запросе, по умолчанию устанавливается значение false. |
| chromiumStartupFlags | [ChromiumStartupFlagsDto](#openapi-definition-ChromiumStartupFlagsDto) | Флаги запуска Chromium для Browser Monitor. |
| clientCertificates | [ClientCertificateDto](#openapi-definition-ClientCertificateDto)[] | Идентификатор сохранённого клиентского сертификата. |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Список cookie. |
| device | [TestDeviceDto](#openapi-definition-TestDeviceDto) | Тестовое устройство для Browser Monitor. |
| enablement | [EnablementDto](#openapi-definition-EnablementDto) | Настройки включения Browser Monitor. |
| experimentalProperties | [MonitorPropertyDto](#openapi-definition-MonitorPropertyDto)[] | Список экспериментальных свойств. |
| filteredRequests | [FilteredRequestsDto](#openapi-definition-FilteredRequestsDto) | Отфильтрованные запросы для Browser Monitor. |
| ignoredErrorCodes | [IgnoredErrorCodesDto](#openapi-definition-IgnoredErrorCodesDto) | Игнорируемые коды ошибок для Browser Monitor. |
| javaScriptSettings | [JavaScriptAgentSettingsDto](#openapi-definition-JavaScriptAgentSettingsDto) | Настройки JavaScript Agent. |
| monitorFrames | boolean | Сбор метрик производительности для страниц, загруженных во фреймах. Если не задано в запросе, по умолчанию устанавливается значение false. |
| networkThrottling | [NetworkThrottlingDto](#openapi-definition-NetworkThrottlingDto) | Ограничение пропускной способности сети для Browser Monitor. |
| proxy | [ProxyDto](#openapi-definition-ProxyDto) | Прокси Browser Monitor. |
| requestHeaderOptions | [RequestHeaderOptionsDto](#openapi-definition-RequestHeaderOptionsDto) | Параметры заголовков для Browser Monitor. |
| useIESupportedAgent | boolean | Флаг useIESupportedAgent. Если не задано в запросе, по умолчанию устанавливается значение false. |
| userAgent | string | User agent |


#### Объект `BrowserPermissionsDto`


Настройки разрешений для браузера.


| Элемент | Тип | Описание |
| --- | --- | --- |
| camera | boolean | Разрешение на использование камеры. Если не задано в запросе, по умолчанию устанавливается значение false. |
| location | boolean | Разрешение на определение местоположения. Если не задано в запросе, по умолчанию устанавливается значение false. |
| microphone | boolean | Разрешение на использование микрофона. Если не задано в запросе, по умолчанию устанавливается значение false. |
| notifications | boolean | Разрешение на показ уведомлений. Если не задано в запросе, по умолчанию устанавливается значение false. |


#### Объект `ChromiumStartupFlagsDto`


Флаги запуска Chromium для Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| autoplay-policy | string | Тип autoplay-policy. Элемент может принимать следующие значения * `no-user-gesture-required` * `document-user-activation-required` |
| disable-features | object | Карта disable-features |
| disable-site-isolation-trials | boolean | Флаг disable-site-isolation-trials. |
| disable-web-security | boolean | Флаг disable-web-security. Если значение не передано, по умолчанию устанавливается false. |
| host-resolver-rules | string | host-resolver-rules. |
| ignore-certificate-errors | boolean | Флаг ignore-certificate-errors. |
| ssl-version-max | string | ssl-version-max. |
| ssl-version-min | string | ssl-version-min. |
| test-type | boolean | Флаг test-type. |


#### Объект `ClientCertificateDto`


Клиентский сертификат.


| Элемент | Тип | Описание |
| --- | --- | --- |
| credentialId | string | Идентификатор CV сертификата. |
| domain | string | Домен, к которому будет применён сертификат. |


#### Объект `SyntheticMonitorCookieDto`


Dto cookie для шага Synthetic Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| domain | string | Домен cookie. |
| name | string | Имя cookie. |
| path | string | Путь cookie. |
| value | string | Значение cookie. |


#### Объект `TestDeviceDto`


Тестовое устройство для Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| height | integer | Высота устройства в px. |
| mobile | boolean | Устройство является мобильным. Если не задано в запросе, по умолчанию устанавливается значение false. |
| name | string | Название устройства. |
| touchEnabled | boolean | Устройство поддерживает сенсорный ввод. Если не задано в запросе, по умолчанию устанавливается значение false. |
| width | integer | Ширина устройства в px. |


#### Объект `EnablementDto`


Настройки включения Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| enableOnGrail | boolean | Включить отправку данных JS agent 3-го поколения. Актуально только для сред SaaS с включённым Grail. |
| origin | string | Указывает источник данных настроек. Элемент может принимать следующие значения * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` |


#### Объект `MonitorPropertyDto`


Свойство Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя свойства. |
| value | string | Значение свойства. |


#### Объект `FilteredRequestsDto`


Отфильтрованные запросы для Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| mode | string | Режим фильтрации для отфильтрованных запросов. Элемент может принимать следующие значения * `BLOCK` * `ALLOW` |
| requests | [RequestFilterDto](#openapi-definition-RequestFilterDto)[] | Запросы, подлежащие фильтрации. |


#### Объект `RequestFilterDto`


Фильтр запросов для Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| matchingPattern | string | Регулярное выражение для запроса, к которому будет применён фильтр. |
| type | string | Тип фильтра. Элемент может принимать следующие значения * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` * `REGEX` |


#### Объект `IgnoredErrorCodesDto`


Игнорируемые коды ошибок для Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| matchingDocumentRequests | string | Игнорирование кодов состояния будет применяться к запросам, соответствующим паттерну. |
| statusCodes | string | Коды состояния, которые нужно игнорировать. |


#### Объект `JavaScriptAgentSettingsDto`


Настройки JavaScript Agent.


| Элемент | Тип | Описание |
| --- | --- | --- |
| customProperties | string | Пользовательские свойства конфигурации |
| experimentalValues | boolean | Поддержка экспериментальных значений. Если не задано в запросе, по умолчанию устанавливается значение false. |
| fetchRequests | boolean | Сбор данных о запросах fetch(). Если не задано в запросе, по умолчанию устанавливается значение true. |
| javaScriptErrors | boolean | Включить эту настройку для отслеживания ошибок JavaScript. Для перехвата ошибок JavaScript используется обработчик window.onError. Если не задано в запросе, по умолчанию устанавливается значение true. |
| javaScriptFrameworkSupport | [FrameworkOptionsDto](#openapi-definition-FrameworkOptionsDto) | Параметры JS framework для JS Agent. |
| timedActions | boolean | В JS-фреймворках XHR-запросы часто отправляются через методы setTimeout. Включить эту настройку для обнаружения действий, вызывающих такие XHR-запросы. Если не задано в запросе, по умолчанию устанавливается значение true. |
| timeoutSettings | [TimeoutSettingsDto](#openapi-definition-TimeoutSettingsDto) | Настройки таймаута для Browser Monitor. |
| visuallyCompleteOptions | [VisuallyCompleteOptionsDto](#openapi-definition-VisuallyCompleteOptionsDto) | Параметры Visually Complete для Browser Monitor. |
| xmlHttpRequests | boolean | Сбор данных о запросах xml Http (XHR). Если не задано в запросе, по умолчанию устанавливается значение true. |


#### Объект `FrameworkOptionsDto`


Параметры JS framework для JS Agent.


| Элемент | Тип | Описание |
| --- | --- | --- |
| activeXObject | boolean | Поддержка activeXObject. Если не задано в запросе, по умолчанию устанавливается значение false. |
| angular | boolean | Поддержка Angular. Если не задано в запросе, по умолчанию устанавливается значение false. |
| dojo | boolean | Поддержка Dojo. Если не задано в запросе, по умолчанию устанавливается значение false. |
| extJs | boolean | Поддержка extJs. Если не задано в запросе, по умолчанию устанавливается значение false. |
| icefaces | boolean | Поддержка icefaces. Если не задано в запросе, по умолчанию устанавливается значение false. |
| jQuery | boolean | Поддержка jquery. Если не задано в запросе, по умолчанию устанавливается значение false. |
| mooTools | boolean | Поддержка mooTools. Если не задано в запросе, по умолчанию устанавливается значение false. |
| prototype | boolean | Поддержка prototype. Если не задано в запросе, по умолчанию устанавливается значение false. |


#### Объект `TimeoutSettingsDto`


Настройки таймаута для Browser Monitor.


| Элемент | Тип | Описание |
| --- | --- | --- |
| temporaryActionLimit | integer | Ограничение числа каскадных вызовов setTimeout. Если не задано в запросе, по умолчанию устанавливается значение 1. |
| temporaryActionTotalTimeout | integer | После достижения этого лимита времени новые временные действия создаваться не будут. Значение должно быть больше 0 мс. Если не задано в запросе, по умолчанию устанавливается значение 100. |


#### Объект `VisuallyCompleteOptionsDto`


Параметры Visually Complete для Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| excludedElements | string[] | CSS-селекторы для запросов, задающие узлы мутаций (изменяемые элементы), которые нужно игнорировать при расчёте Visually complete и Speed index. |
| excludedUrls | string[] | Регулярные выражения, определяющие URL для изображений и iFrame, которые нужно исключить из обнаружения модулем Visually complete. |
| imageSizeThreshold | integer | Этот параметр задаёт минимальную видимую площадь элемента (в пикселях), при которой элемент учитывается при расчёте Visually complete и Speed index. Если в запросе не задано, по умолчанию устанавливается значение 50. |
| inactivityTimeout | integer | Время, в течение которого модуль Visually complete ожидает бездействия и отсутствия дальнейших мутаций на странице после действия load. Если в запросе не задано, по умолчанию устанавливается значение 1000. |
| mutationTimeout | integer | Время, в течение которого модуль Visually complete ожидает после завершения XHR или пользовательского действия, прежде чем начать расчёт. Если в запросе не задано, по умолчанию устанавливается значение 50. |


#### Объект `NetworkThrottlingDto`


Ограничение пропускной способности сети для Browser Monitor.


| Element | Type | Description |
| --- | --- | --- |
| download | integer | Пропускная способность загрузки. Если в запросе не задано, по умолчанию устанавливается значение -1. |
| latency | integer | Задержка. Если в запросе не задано, по умолчанию устанавливается значение 0. |
| name | string | Предопределённый тип сети. Если в запросе не задано, по умолчанию устанавливается значение "". |
| upload | integer | Пропускная способность отдачи. Если в запросе не задано, по умолчанию устанавливается значение -1. |


#### Объект `ProxyDto`


Прокси Browser Monitor.


| Element | Type | Description |
| --- | --- | --- |
| pacUrl | string | pacUrl |


#### Объект `RequestHeaderOptionsDto`


Настройки заголовков Browser Monitor.


| Element | Type | Description |
| --- | --- | --- |
| matchingPatterns | string[] | Применять заголовки к запросам, соответствующим шаблону. |
| requestHeaders | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Список заголовков запроса. |


#### Объект `MonitorRequestHeader`


Заголовок Http-запроса


| Element | Type | Description |
| --- | --- | --- |
| name | string | Имя заголовка. |
| value | string | Значение заголовка. |


#### Объект `KeyPerformanceMetrics`


Конфигурация ключевых показателей производительности.


| Element | Type | Description |
| --- | --- | --- |
| loadActionKpm | string | Ключевой показатель производительности для действия load. Элемент может принимать следующие значения * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` |
| xhrActionKpm | string | Ключевой показатель производительности для действия XHR. Элемент может принимать следующие значения * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` |


#### Объект `SyntheticBrowserMonitorStepDto`


Базовый шаг Browser Monitor.


| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Id сущности. |
| name | string | Имя шага Browser Monitor. |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `NAVIGATE` -> NavigateStepDto * `CLICK` -> InteractionStepDto * `TAP` -> InteractionStepDto * `KEYSTROKES` -> KeyStrokesStepDto * `JAVASCRIPT` -> JavaScriptStepDto * `SELECT_OPTION` -> SelectOptionStepDto * `COOKIE` -> CookieStepDto Элемент может принимать следующие значения * `CLICK` * `COOKIE` * `JAVASCRIPT` * `KEYSTROKES` * `NAVIGATE` * `SELECT_OPTION` * `TAP` |


#### Объект `SyntheticHttpMonitorResponse`


Http monitor.


| Element | Type | Description |
| --- | --- | --- |
| advancedSettings | [SyntheticHttpMonitorAdvancedDto](#openapi-definition-SyntheticHttpMonitorAdvancedDto) | Настройки Http monitor. |
| automaticallyAssignedEntities | string[] | Автоматически назначенные сущности. |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Cookie монитора. |
| description | string | Описание монитора |
| enabled | boolean | Если true, монитор включён. |
| entityId | string | Id сущности монитора. |
| frequencyMin | integer | Частота работы монитора, в минутах. |
| locations | string[] | Локации, к которым привязан монитор. |
| manuallyAssignedEntities | string[] | Вручную назначенные сущности. |
| modificationTimestamp | integer | Метка времени последнего изменения |
| name | string | Имя монитора. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация пороговых значений производительности. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Основные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS и недоступны для Managed. |
| securityContext | string[] | [FEATURE DISABLED] Контекст безопасности в виде списка строк. До 10 значений, максимум 200 символов на значение. Эти поля доступны только для SaaS и недоступны для Managed. |
| steps | [SyntheticHttpMonitorStepDto](#openapi-definition-SyntheticHttpMonitorStepDto)[] | Шаги монитора. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки простоев. |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | Набор тегов, назначенных монитору.  Здесь можно указать только значение тега, при этом контекст `CONTEXTLESS` и источник 'USER' добавятся автоматически. Но предпочтительный вариант, использование модели SyntheticTagWithSourceDto. |
| type | string | Тип монитора. Элемент может принимать следующие значения * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` |


#### Объект `SyntheticHttpMonitorAdvancedDto`


Настройки Http monitor.


| Element | Type | Description |
| --- | --- | --- |
| connectTimeout | integer | Таймаут подключения на запрос, в мс. |
| dnsQueryTimeout | integer | Таймаут DNS-запроса, в мс. |
| maxCustomScriptSize | integer | Максимальный размер каждого скрипта пред- или пост-выполнения, в байтах. |
| maxHeaderSize | integer | Максимальный размер каждого заголовка запроса, в байтах. |
| maxRequestBodySize | integer | Максимальный размер тела запроса, в байтах. |
| maxResponseBodyReadByScriptSize | integer | Максимальный размер тела ответа, читаемого скриптом пост-выполнения, в байтах. |
| maxResponseBodySize | integer | Максимальный размер тела ответа, в байтах. |
| monitorExecutionTimeout | integer | Таймаут выполнения монитора, в мс. |
| requestTimeout | integer | Таймаут запроса, в мс. |
| scriptExecutionTimeout | integer | Таймаут скрипта пред- или пост-выполнения, в мс. |


#### Объект `SyntheticHttpMonitorStepDto`


Шаг Http monitor.


| Element | Type | Description |
| --- | --- | --- |
| authentication | [SyntheticHttpAuthenticationDto](#openapi-definition-SyntheticHttpAuthenticationDto) | Аутентификация Http-шага. |
| configuration | [SyntheticHttpConfigurationDto](#openapi-definition-SyntheticHttpConfigurationDto) | Конфигурация Http-шага. |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Список ограничений. |
| entityId | string | Id сущности. |
| methodType | string | Тип метода. Элемент может принимать следующие значения * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `OPTIONS` * `PATCH` |
| name | string | Имя шага. |
| postScript | string | PostScript. |
| preScript | string | PreScript. |
| requestBody | string | Тело запроса. |
| requestTimeout | integer | Таймаут запроса, в с. |
| url | string | Url шага. |


#### Объект `SyntheticHttpAuthenticationDto`


Аутентификация Http-шага.


| Element | Type | Description |
| --- | --- | --- |
| credentials | string | Идентификатор credential vault. |
| kdcIp | string | KDC IP, если выбран тип аутентификации KERBEROS. |
| realmName | string | Имя realm, если выбран тип KERBEROS. |
| type | string | Тип аутентификации. Элемент может принимать следующие значения * `BASIC_AUTHENTICATION` * `NTLM` * `KERBEROS` |


#### Объект `SyntheticHttpConfigurationDto`


Конфигурация Http-шага.


| Element | Type | Description |
| --- | --- | --- |
| acceptAnyCertificate | boolean | Если true, флаг принятия любого сертификата. |
| clientCertificateId | string | Идентификатор сохранённого сертификата клиента. |
| doNotPersistSensitiveData | boolean | Если true, данные шага не сохраняются и не отображаются. |
| followRedirects | boolean | Если true, следовать редиректам. |
| headers | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Заголовки. |
| sslCertificateExpirationDaysToAlert | integer | Количество дней до истечения срока действия SSL-сертификата. |


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



"description": "My network availability monitor description",



"enabled": "true",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1",



"frequencyMin": "60",



"locations": [



"SYNTHETIC_LOCATION-D3A5BFD8676A4F20"



],



"modificationTimestamp": "1716448454338l",



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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор для одного URL, браузерный clickpath или HTTP-монитор.")