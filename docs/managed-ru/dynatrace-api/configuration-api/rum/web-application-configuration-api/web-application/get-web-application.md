---
title: Web application configuration API - GET a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application
---

# Web application configuration API - GET a web application

# Web application configuration API - GET a web application

* Справочник
* Опубликовано 03 сентября 2019 г.

Возвращает параметры указанного веб-приложения.

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

Запрос возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID запрашиваемого веб-приложения. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | Успех |

### Объекты тела ответа


#### Объект `WebApplicationConfig`


Конфигурация веб-приложения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| conversionGoals | [ConversionGoal](#openapi-definition-ConversionGoal)[] | Список целей конверсии приложения. |
| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. |
| identifier | string | Dynatrace ID сущности веб-приложения. |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. |
| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности load-действий. Элемент может принимать значения * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` |
| metaDataCaptureSettings | [MetaDataCapturing](#openapi-definition-MetaDataCapturing)[] | Настройки захвата метаданных Java script agent. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки real user monitoring. |
| name | string | Имя веб-приложения, отображаемое в UI. |
| realUserMonitoringEnabled | boolean | Real user monitoring включён/выключен. |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки session replay |
| type | string | Тип веб-приложения. Элемент может принимать значения * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` |
| urlInjectionPattern | string | Паттерн внедрения URL для веб-приложения с ручной установкой. |
| userActionAndSessionProperties | [UserActionAndSessionProperties](#openapi-definition-UserActionAndSessionProperties)[] | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. |
| userTags | [UserTag](#openapi-definition-UserTag)[] | Настройки пользовательских тегов. |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, получаемые для ресурсов сторонних поставщиков, CDN и ресурсов первой стороны. |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. |
| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности XHR-действий. Элемент может принимать значения * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` |


#### Объект `ConversionGoal`


Цель конверсии приложения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. |
| id | string | ID цели конверсии.  Не указывать при создании новой цели конверсии. |
| name | string | Имя цели конверсии. |
| type | string | Тип цели конверсии. Элемент может принимать значения * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе количества пользовательских действий. |


#### Объект `DestinationDetails`


Конфигурация цели конверсии на основе назначения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| caseSensitive | boolean | Совпадение чувствительно к регистру (`true`) или нет (`false`). |
| matchType | string | Оператор совпадения. Элемент может принимать значения * `Begins` * `Contains` * `Ends` |
| urlOrPath | string | Путь, который нужно достичь для выполнения цели конверсии. |


#### Объект `UserActionDetails`


Конфигурация цели конверсии на основе пользовательского действия.


| Элемент | Тип | Описание |
| --- | --- | --- |
| actionType | string | Тип действия, к которому применяется правило. Элемент может принимать значения * `Custom` * `Load` * `Xhr` |
| caseSensitive | boolean | Совпадение чувствительно к регистру (`true`) или нет (`false`). |
| matchEntity | string | Тип сущности, к которой применяется правило. Элемент может принимать значения * `ActionName` * `PageUrl` |
| matchType | string | Оператор совпадения. Элемент может принимать значения * `Begins` * `Contains` * `Ends` |
| value | string | Значение, которое должно совпасть для выполнения цели конверсии. |


#### Объект `VisitDurationDetails`


Конфигурация цели конверсии на основе длительности визита.


| Элемент | Тип | Описание |
| --- | --- | --- |
| durationInMillis | integer | Длительность сессии для выполнения цели конверсии, в миллисекундах. |


#### Объект `VisitNumActionDetails`


Конфигурация цели конверсии на основе количества пользовательских действий.


| Элемент | Тип | Описание |
| --- | --- | --- |
| numUserActions | integer | Количество пользовательских действий для выполнения цели конверсии. |


#### Объект `Apdex`


Определяет настройки Apdex приложения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| frustratingFallbackThreshold | number | Резервный порог XHR-действия, определяющий приемлемый пользовательский опыт, когда настроенный KPM недоступен. |
| frustratingThreshold | number | Максимальное значение apdex, которое считается приемлемым пользовательским опытом. |
| toleratedFallbackThreshold | number | Резервный порог XHR-действия, определяющий удовлетворительный пользовательский опыт, когда настроенный KPM недоступен. |
| toleratedThreshold | number | Максимальное значение apdex, которое считается удовлетворительным пользовательским опытом. |


#### Объект `MetaDataCapturing`


Конфигурация захвата метаданных с помощью Javascript agent. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder


| Элемент | Тип | Описание |
| --- | --- | --- |
| capturingName | string | Имя метаданных для захвата. |
| name | string | Имя для отображения захваченных значений в Dynatrace. |
| publicMetadata | boolean | True, если эти метаданные нужно захватывать независимо от настроек приватности |
| type | string | Тип метаданных для захвата. Элемент может принимать значения * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` |
| uniqueId | integer | Уникальный идентификатор метаданных для захвата. |
| useLastValue | boolean | True, если для этих метаданных нужно использовать последнее захваченное значение. По умолчанию используется первое значение. |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |


#### Объект `MonitoringSettings`


Настройки real user monitoring.

| Элемент | Тип | Описание |
| --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Добавляет атрибут cross origin = anonymous для захвата сообщений об ошибках JavaScript и W3C resource timings. |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Расширенные настройки JavaScript-тега. |
| angularPackageName | string | Имя пакета angular. |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки ограничения по определённому типу браузера, версии, платформе и компаратору. Также ограничивает режим. |
| cacheControlHeaderOptimizations | boolean | Оптимизация значения заголовков cache control для использования с Dynatrace, real user monitoring включён/выключен. |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки захвата содержимого. |
| cookiePlacementDomain | string | Домен для размещения cookie. |
| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, нужно задать регулярное выражение, соответствующее этим вызовам, тогда Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим эндпоинтам в AWS.  Важно: эти эндпоинты должны принимать заголовок x-dtc, иначе запросы завершатся ошибкой. |
| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для конкретного приложения. Для этого нужно указать пары key=value, разделённые символом (|). |
| excludeXhrRegex | string | Некоторые действия можно исключить из превращения в XHR-действия.  Здесь нужно указать регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. |
| fetchRequests | boolean | Захват запросов `fetch()` включён/выключен. |
| injectionMode | string | Режим внедрения JavaScript. Элемент может принимать следующие значения * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` |
| instrumentedWebServer | boolean | Инструментированный веб- или app-сервер. |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки ограничения по определённым IP-адресам и для указания маски подсети. Также ограничивает режим. |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. |
| javaScriptInjectionRules | [JavaScriptInjectionRules](#openapi-definition-JavaScriptInjectionRules)[] | Правила внедрения JavaScript. |
| libraryFileFromCdn | boolean | Получение файла JavaScript-библиотеки из CDN.  Не поддерживается для agentless-приложений, для приложений с авто-внедрением по умолчанию считается false, если не указано. |
| libraryFileLocation | string | Расположение пользовательского файла JavaScript-библиотеки приложения.  Если ничего не указано, используется корневой каталог веб-сервера.  **Обязательно** для приложений с авто-внедрением, не поддерживается для agentless-приложений. |
| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Нужно указать относительный или абсолютный URL. При использовании абсолютного URL данные будут отправляться через CORS.  **Обязательно** для приложений с авто-внедрением, необязательно для agentless-приложений. |
| sameSiteCookieAttribute | string | Атрибут same site cookie. Элемент может принимать следующие значения * `LAX` * `NONE` * `STRICT` |
| scriptTagCacheDurationInHours | integer | Длительность для настроек кеша. |
| secureCookieAttribute | boolean | Использование атрибута secure для Dynatrace cookie включено/выключено. |
| serverRequestPathId | string | Путь для идентификации ID запроса сервера. |
| useCors | boolean | Отправка данных beacon через CORS. |
| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest` включена/выключена. |


#### Объект `AdvancedJavaScriptTagSettings`


Расширенные настройки JavaScript-тега.


| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики событий и обёртки. |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | Помимо обработчиков событий, можно захватывать события, вызванные через `addEventListener` или `attachEvent`. С этой опцией нужно быть осторожным! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице. |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. |
| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков включено/выключено. |
| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения от 5 до 10000. |
| maxErrorsToCapture | integer | Максимальное число ошибок, захватываемых на страницу. Допустимые значения от 0 до 50. |
| proxyWrapperEnabled | boolean | Прокси-обёртка включена/выключена. |
| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать не буквенно-цифровыми символами в формате HTML escape. |
| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest в Firefox включена/выключена. |
| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest в Internet Explorer включена/выключена. |
| userActionNameAttribute | string | Атрибут имени пользовательского действия. |


#### Объект `AdditionalEventHandlers`


Дополнительные обработчики событий и обёртки.


| Элемент | Тип | Описание |
| --- | --- | --- |
| blurEventHandler | boolean | Обработчик события blur включён/выключен. |
| changeEventHandler | boolean | Обработчик события change включён/выключен. |
| clickEventHandler | boolean | Обработчик события click включён/выключен. |
| maxDomNodesToInstrument | integer | Макс. число DOM-узлов для инструментирования. Допустимые значения от 0 до 100000. |
| mouseupEventHandler | boolean | Обработчик события mouseup включён/выключен. |
| toStringMethod | boolean | Метод toString включён/выключен. |
| userMouseupEventForClicks | boolean | Использование события mouseup для кликов включено/выключено. |


#### Объект `EventWrapperSettings`


Помимо обработчиков событий, можно захватывать события, вызванные через `addEventListener` или `attachEvent`. С этой опцией нужно быть осторожным! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице.


| Элемент | Тип | Описание |
| --- | --- | --- |
| blur | boolean | Blur включён/выключен. |
| change | boolean | Change включён/выключен. |
| click | boolean | Click включён/выключен. |
| mouseUp | boolean | MouseUp включён/выключен. |
| touchEnd | boolean | TouchEnd включён/выключен. |
| touchStart | boolean | TouchStart включён/выключен. |


#### Объект `GlobalEventCaptureSettings`


Настройки глобального захвата событий.


| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Дополнительные события, захватываемые глобально как пользовательский ввод.  Например, DragStart или DragEnd. |
| change | boolean | Change включён/выключен. |
| click | boolean | Click включён/выключен. |
| doubleClick | boolean | DoubleClick включён/выключен. |
| keyDown | boolean | KeyDown включён/выключен. |
| keyUp | boolean | KeyUp включён/выключен. |
| mouseDown | boolean | MouseDown включён/выключен. |
| mouseUp | boolean | MouseUp включён/выключен. |
| scroll | boolean | Scroll включён/выключен. |
| touchEnd | boolean | TouchEnd включён/выключен. |
| touchStart | boolean | TouchStart включён/выключен. |


#### Объект `WebApplicationConfigBrowserRestrictionSettings`


Настройки ограничения по определённому типу браузера, версии, платформе и компаратору. Также ограничивает режим.


| Элемент | Тип | Описание |
| --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction](#openapi-definition-WebApplicationConfigBrowserRestriction)[] | Список ограничений браузера. |
| mode | string | Режим списка ограничений браузера. Элемент может принимать следующие значения * `EXCLUDE` * `INCLUDE` |


#### Объект `WebApplicationConfigBrowserRestriction`


Правила исключения браузеров для тех браузеров, которые нужно исключить.


| Элемент | Тип | Описание |
| --- | --- | --- |
| browserType | string | Тип используемого браузера. Элемент может принимать следующие значения * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` |
| browserVersion | string | Версия используемого браузера. |
| comparator | string | Сравнивает разные браузеры между собой. Элемент может принимать следующие значения * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` |
| platform | string | Платформа, на которой используется браузер. Элемент может принимать следующие значения * `ALL` * `DESKTOP` * `MOBILE` |


#### Объект `ContentCapture`


Настройки захвата содержимого.


| Элемент | Тип | Описание |
| --- | --- | --- |
| javaScriptErrors | boolean | Мониторинг ошибок JavaScript включён/выключен. |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки захвата resource timings. |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки захвата timed action. |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки для VisuallyComplete2 |
| visuallyCompleteAndSpeedIndex | boolean | Поддержка visually complete и speed index включена/выключена. |


#### Объект `ResourceTimingSettings`


Настройки захвата resource timings.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nonW3cResourceTimings | boolean | Хронометраж файлов JavaScript и изображений в браузерах без поддержки W3C включён/выключен. |
| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и изображений в браузерах, не предоставляющих W3C resource timings. Допустимые значения от 0 до 9999. Действует только если включён параметр **nonW3cResourceTimings**. |
| resourceTimingCaptureType | string | Определяет уровень детализации при захвате хронометража ресурсов. Действует только если включён параметр **w3cResourceTimings** или **nonW3cResourceTimings**. Элемент может принимать следующие значения: * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` |
| resourceTimingsDomainLimit | integer | Ограничивает число доменов, для которых захватывается хронометраж ресурсов W3C. Действует только если параметр **resourceTimingCaptureType** имеет значение `CAPTURE_LIMITED_SUMMARIES`. |
| w3cResourceTimings | boolean | Хронометраж ресурсов W3C для сторонних доменов/CDN включён/выключен. |


#### Объект `TimeoutSettings`


Настройки для захвата действий по таймауту.


| Элемент | Тип | Описание |
| --- | --- | --- |
| temporaryActionLimit | integer | Определяет, насколько глубоко могут каскадироваться временные действия. Значение 0 полностью отключает временные действия. Рекомендуемое значение при включении, 3. |
| temporaryActionTotalTimeout | integer | Суммарный таймаут всех каскадных таймаутов, при котором ещё может создаваться временное действие |
| timedActionSupport | boolean | Поддержка действий по таймауту включена/выключена. Включить для обнаружения действий, инициирующих отправку XHR через методы *setTimout*. |


#### Объект `VisuallyComplete2Settings`


Настройки для VisuallyComplete2


| Элемент | Тип | Описание |
| --- | --- | --- |
| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. |
| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при расчёте VC и SI |
| inactivityTimeout | integer | Время в мс, в течение которого модуль VC ожидает отсутствия мутаций на странице после действия загрузки. По умолчанию 1000. |
| mutationTimeout | integer | Определяет время в мс, которое VC ожидает после закрытия действия перед началом расчёта. По умолчанию 50. |
| threshold | integer | Минимальная видимая площадь элементов в пикселях, учитываемая при расчёте VC и SI. По умолчанию 50. |


#### Объект `WebApplicationConfigIpAddressRestrictionSettings`


Настройки для ограничения определённых ip-адресов и указания маски подсети. Также определяет режим ограничения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange](#openapi-definition-IpAddressRange)[] | - |
| mode | string | Режим списка ограничений ip-адресов. Элемент может принимать следующие значения: * `EXCLUDE` * `INCLUDE` |


#### Объект `IpAddressRange`


IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением.


| Элемент | Тип | Описание |
| --- | --- | --- |
| address | string | IP-адрес, который сопоставляется с местоположением. Для диапазона IP-адресов, это начальный адрес (**from**). |
| addressTo | string | Конечный адрес (**to**) диапазона IP-адресов. |
| subnetMask | integer | Маска подсети для диапазона IP-адресов. |


#### Объект `JavaScriptFrameworkSupport`


Поддержка различных фреймворков JavaScript.


| Элемент | Тип | Описание |
| --- | --- | --- |
| activeXObject | boolean | Обнаружение ActiveXObject включено/выключено. |
| angular | boolean | Поддержка AngularJS и Angular включена/выключена. |
| dojo | boolean | Поддержка Dojo включена/выключена. |
| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/выключена. |
| icefaces | boolean | Поддержка ICEfaces включена/выключена. |
| jQuery | boolean | Поддержка jQuery, Backbone.js включена/выключена. |
| mooTools | boolean | Поддержка MooTools включена/выключена. |
| prototype | boolean | Поддержка Prototype включена/выключена. |


#### Объект `JavaScriptInjectionRules`


Правила для внедрения javascript


| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Правило включения или отключения внедрения javascript. |
| htmlPattern | string | Html-паттерн внедрения javascript. |
| rule | string | Правило url для внедрения javascript. Элемент может принимать следующие значения: * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` |
| target | string | Цель, с которой сопоставляется правило внедрения javascript. Элемент может принимать следующие значения: * `PAGE_QUERY` * `URL` |
| urlOperator | string | Оператор url для внедрения javascript. Элемент может принимать следующие значения: * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| urlPattern | string | Паттерн url для внедрения javascript. |


#### Объект `SessionReplaySetting`


Настройки Session Replay


| Элемент | Тип | Описание |
| --- | --- | --- |
| costControlPercentage | integer | Процент сэмплирования session replay. |
| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата ресурсов CSS. |
| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) ресурсы CSS из сессии. |
| enabled | boolean | Session Replay включён. |


#### Объект `UserActionAndSessionProperties`


Определяет настройки пользовательских свойств userAction и session, заданных для приложения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации свойства. Определяет, как агрегируются несколько значений свойства. Элемент может принимать следующие значения: * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` |
| cleanupRule | string | Правило очистки свойства. Определяет, как извлечь нужные данные из строкового значения. Нужно указать [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для требуемых данных. |
| displayName | string | Отображаемое имя свойства. |
| ignoreCase | boolean | Если true, значение этого свойства всегда сохраняется в нижнем регистре. По умолчанию false. |
| key | string | Ключ свойства |
| longStringLength | integer | Если тип LONG\_STRING, максимальная длина этого свойства. Должна быть кратна 100. По умолчанию 200. |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Обязателен, если "origin" имеет тип META\_DATA. |
| origin | string | Источник свойства. Элемент может принимать следующие значения: * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` |
| serverSideRequestAttribute | string | Идентификатор атрибута запроса. Применимо только если параметр **origin** имеет значение `SERVER_SIDE_REQUEST_ATTRIBUTE`. |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство сессии |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство пользовательского действия |
| type | string | Тип данных свойства. Элемент может принимать следующие значения: * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` |
| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения |


#### Объект `UserActionNamingSettings`


Настройки именования пользовательских действий.


| Элемент | Тип | Описание |
| --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования пользовательских действий для custom-действий. |
| ignoreCase | boolean | Именование без учёта регистра. |
| loadActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования пользовательских действий для действий загрузки. |
| placeholders | [UserActionNamingPlaceholder](#openapi-definition-UserActionNamingPlaceholder)[] | Плейсхолдеры пользовательских действий. |
| queryParameterCleanups | string[] | Список параметров, которые нужно удалить из строки запроса перед использованием запроса в имени пользовательского действия. |
| splitUserActionsByDomain | boolean | Отключить эту настройку, если разные домены не должны приводить к отдельным пользовательским действиям. |
| useFirstDetectedLoadAction | boolean | Если true, используется первое найденное действие загрузки под XHR-действием. Иначе используется самое глубокое действие под xhr-действием |
| xhrActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования пользовательских действий для xhr-действий. |


#### Объект `UserActionNamingRule`


Настройки правила именования.


| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [UserActionNamingRuleCondition](#openapi-definition-UserActionNamingRuleCondition)[] | Определяет условия применения правила именования. |
| template | string | Шаблон именования. Фигурные скобки `{}` используются для выбора плейсхолдеров. |
| useOrConditions | boolean | Если установлено значение `true`, условия соединяются логическим ИЛИ вместо логического И. |


#### Объект `UserActionNamingRuleCondition`


Настройки условий для именования пользовательских действий.


| Элемент | Тип | Описание |
| --- | --- | --- |
| operand1 | string | Должен быть определённым плейсхолдером, заключённым в фигурные скобки |
| operand2 | string | Должен быть null, если оператор "IS\_EMPTY", регулярным выражением, если оператор "MATCHES\_REGULAR\_ERPRESSION". Во всех остальных случаях значение может быть произвольным текстом или плейсхолдером, заключённым в фигурные скобки |
| operator | string | Оператор условия. Элемент может принимать следующие значения: * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` |


#### Объект `UserActionNamingPlaceholder`


Настройки плейсхолдера.

| Элемент | Тип | Описание |
| --- | --- | --- |
| input | string | Input. Элемент может принимать следующие значения * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` |
| metadataId | integer | Ссылка на uniqueId MetadataCapturingConfig. Нужно задать, если "Input" имеет тип METADATA. |
| name | string | Имя плейсхолдера. |
| processingPart | string | Part. Элемент может принимать следующие значения * `ALL` * `ANCHOR` * `PATH` |
| processingSteps | [UserActionNamingPlaceholderProcessingStep](#openapi-definition-UserActionNamingPlaceholderProcessingStep)[] | Действия обработки. |
| useGuessedElementIdentifier | boolean | Использовать идентификатор элемента, выбранный Dynatrace. |


#### Объект `UserActionNamingPlaceholderProcessingStep`


Настройки шага обработки.


| Элемент | Тип | Описание |
| --- | --- | --- |
| fallbackToInput | boolean | Если задано значение true: возвращается входное значение, если **patternBefore** или **patternAfter** не найдены и **type** имеет значение `SUBSTRING`.  Возвращается входное значение, если **regularExpression** не совпадает и **type** имеет значение `EXTRACT_BY_REGULAR_EXPRESSION`.  В остальных случаях возвращается null. |
| patternAfter | string | Паттерн после нужного значения. Будет удалён. |
| patternAfterSearchType | string | Нужное вхождение **patternAfter**. Элемент может принимать следующие значения * `FIRST` * `LAST` |
| patternBefore | string | Паттерн перед нужным значением. Будет удалён. |
| patternBeforeSearchType | string | Нужное вхождение **patternBefore**. Элемент может принимать следующие значения * `FIRST` * `LAST` |
| patternToReplace | string | Паттерн, подлежащий замене.  Применимо только если **type** имеет значение `REPLACE_WITH_PATTERN`. |
| regularExpression | string | Регулярное выражение для строки, подлежащей извлечению или замене.  Применимо только если **type** имеет значение `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. |
| replacement | string | Замена исходного значения. |
| type | string | Действие, выполняемое обработкой:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанное значение **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанное значение **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, совпадающую с **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, совпадающие с **regularExpression**, на указанное значение **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанное значение **replacement**. Элемент может принимать следующие значения * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` |


#### Объект `UserTag`


Определяет настройки UserTags приложения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| cleanupRule | string | Выражение правила очистки userTag |
| ignoreCase | boolean | Если true, значение этого тега всегда сохраняется в нижнем регистре. По умолчанию false. |
| metadataId | integer | Ссылка на uniqueId MetadataCapturingConfig. Нужно задать, если UserTag основан на метаданных, захваченных Javascript-агентом (например, переменная Javascript, CSS-селектор и т. д.) |
| serverSideRequestAttribute | string | Идентификатор серверного атрибута запроса userTag. Нужно задать, если UserTag основан на серверном атрибуте запроса. |
| uniqueId | integer | uniqueId, уникальный среди всех userTags и properties этого приложения |


#### Объект `WaterfallSettings`


Эти настройки влияют на данные мониторинга, получаемые для ресурсов сторонних поставщиков, CDN и ресурсов первой стороны.


| Элемент | Тип | Описание |
| --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с частотой кэширования браузером ниже *X*%. |
| resourcesThreshold | integer | Предупреждать о ресурсах размером более *X* байт. |
| slowCdnResourcesThreshold | integer | Предупреждать о медленных ресурсах CDN со временем отклика выше *X* мс. |
| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных ресурсах первой стороны со временем отклика выше *X* мс. |
| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных ресурсах сторонних поставщиков со временем отклика выше *X* мс. |
| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X* % от Visually complete. |
| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах размером более *X* байт. |

### Тело ответа JSON модели

```
{



"conversionGoals": [



{



"destinationDetails": {



"caseSensitive": false,



"matchType": "Begins",



"urlOrPath": "url or path"



},



"name": "conversionGoalName",



"type": "UserAction",



"userActionDetails": {



"actionType": "Load",



"caseSensitive": true,



"matchEntity": "ActionName",



"matchType": "Ends",



"value": "value to match"



},



"visitDurationDetails": {



"durationInMillis": 1



},



"visitNumActionDetails": {



"numUserActions": 2



}



}



],



"costControlUserSessionPercentage": 100,



"customActionApdexSettings": {



"frustratingFallbackThreshold": 12000,



"frustratingThreshold": 12000,



"toleratedFallbackThreshold": 3000,



"toleratedThreshold": 3000



},



"loadActionApdexSettings": {



"frustratingFallbackThreshold": 12000,



"frustratingThreshold": 12000,



"toleratedFallbackThreshold": 3000,



"toleratedThreshold": 3000



},



"loadActionKeyPerformanceMetric": "VISUALLY_COMPLETE",



"metaDataCaptureSettings": [



{



"capturingName": "variableName",



"name": "display name",



"type": "JAVA_SCRIPT_VARIABLE"



}



],



"monitoringSettings": {



"advancedJavaScriptTagSettings": {



"additionalEventHandlers": {



"blurEventHandler": false,



"changeEventHandler": false,



"clickEventHandler": false,



"maxDomNodesToInstrument": 5000,



"mouseupEventHandler": false,



"toStringMethod": false,



"userMouseupEventForClicks": false



},



"eventWrapperSettings": {



"blur": false,



"change": false,



"click": false,



"mouseUp": false,



"touchEnd": false,



"touchStart": false



},



"globalEventCaptureSettings": {



"additionalEventCapturedAsUserInput": "",



"click": true,



"doubleClick": true,



"keyDown": true,



"keyUp": true,



"mouseDown": true,



"mouseUp": true,



"scroll": true



},



"instrumentUnsupportedAjaxFrameworks": false,



"maxActionNameLength": 100,



"maxErrorsToCapture": 10,



"specialCharactersToEscape": "",



"syncBeaconFirefox": false,



"syncBeaconInternetExplorer": false



},



"browserRestrictionSettings": {



"browserRestrictions": [



{



"browserType": "INTERNET_EXPLORER",



"browserVersion": "0",



"comparator": "EQUALS",



"platform": "ALL"



}



],



"mode": "EXCLUDE"



},



"cacheControlHeaderOptimizations": true,



"contentCapture": {



"javaScriptErrors": true,



"resourceTimingSettings": {



"nonW3cResourceTimings": false,



"nonW3cResourceTimingsInstrumentationDelay": 50,



"w3cResourceTimings": true



},



"timeoutSettings": {



"temporaryActionLimit": 0,



"temporaryActionTotalTimeout": 100,



"timedActionSupport": false



},



"visuallyCompleteAndSpeedIndex": true



},



"cookiePlacementDomain": "",



"correlationHeaderInclusionRegex": "",



"customConfigurationProperties": "",



"excludeXhrRegex": "",



"fetchRequests": true,



"injectionMode": "JAVASCRIPT_TAG",



"ipAddressRestrictionSettings": {



"ipAddressRestrictions": [



{



"address": "10.0.0.1",



"subnetMask": 3



},



{



"address": "10.0.0.1",



"addressTo": "10.0.0.2"



}



],



"mode": "EXCLUDE"



},



"javaScriptFrameworkSupport": {



"activeXObject": false,



"angular": true,



"dojo": false,



"extJS": false,



"icefaces": false,



"jQuery": true,



"mooTools": false,



"prototype": true



},



"javaScriptInjectionRules": [



{



"enabled": true,



"htmlPattern": "</title>",



"rule": "AFTER_SPECIFIC_HTML",



"urlOperator": "CONTAINS",



"urlPattern": "/lorem/ipsum.jsp"



}



],



"libraryFileLocation": "",



"monitoringDataPath": "",



"secureCookieAttribute": false,



"serverRequestPathId": "",



"xmlHttpRequest": true



},



"name": "application name",



"realUserMonitoringEnabled": true,



"sessionReplayConfig": {



"costControlPercentage": 100,



"cssResourceCapturingExclusionRules": [



"rule"



],



"enableCssResourceCapturing": true,



"enabled": true



},



"type": "AUTO_INJECTED",



"userActionNamingSettings": {



"ignoreCase": true,



"loadActionNamingRules": [



{



"conditions": [



{



"operand1": "{myPlaceholder}",



"operand2": "foo",



"operator": "CONTAINS"



}



],



"template": "Loading of {myPlaceholder}"



}



],



"placeholders": [



{



"input": "PAGE_URL",



"name": "myPlaceholder",



"processingPart": "ALL",



"processingSteps": [



{



"patternAfter": ".*a",



"patternAfterSearchType": "LAST",



"patternBefore": ".*b",



"patternBeforeSearchType": "FIRST",



"replacement": "value",



"type": "SUBSTRING"



}



],



"useGuessedElementIdentifier": false



}



],



"splitUserActionsByDomain": true,



"xhrActionNamingRules": [



{



"conditions": [



{



"operand1": "{myPlaceholder}",



"operand2": "foo",



"operator": "CONTAINS"



}



],



"template": "Loading of {myPlaceholder}"



}



]



},



"waterfallSettings": {



"resourceBrowserCachingThreshold": 50,



"resourcesThreshold": 100000,



"slowCdnResourcesThreshold": 200000,



"slowFirstPartyResourcesThreshold": 200000,



"slowThirdPartyResourcesThreshold": 200000,



"speedIndexVisuallyCompleteRatioThreshold": 50,



"uncompressedResourcesThreshold": 860



},



"xhrActionApdexSettings": {



"frustratingFallbackThreshold": 12000,



"frustratingThreshold": 10000,



"toleratedFallbackThreshold": 3000,



"toleratedThreshold": 2500



},



"xhrActionKeyPerformanceMetric": "ACTION_DURATION"



}
```