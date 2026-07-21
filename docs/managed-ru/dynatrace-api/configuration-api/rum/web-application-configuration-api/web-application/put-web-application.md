---
title: Web application configuration API - PUT a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application
---

# Web application configuration API - PUT a web application

# Web application configuration API - PUT a web application

* Справка
* Опубликовано 03 сентября 2019 г.

Обновляет указанное веб-приложение.

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

Запрос принимает и возвращает содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |

## Authentication

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | ID веб-приложения, которое нужно обновить. Если ID указан также в теле запроса, он должен совпадать с этим ID. | path | Required |
| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON тело запроса, содержащее обновлённую конфигурацию веб-приложения. | body | Optional |

### Request body objects


#### Объект `WebApplicationConfig`


Конфигурация веб-приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conversionGoals | [ConversionGoal](#openapi-definition-ConversionGoal)[] | Список целей конверсии приложения. | Опциональный |
| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. | Обязательный |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Обязательный |
| identifier | string | Dynatrace ID сущности веб-приложения. | Опциональный |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Обязательный |
| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности load-действий. Элемент может содержать следующие значения: * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` | Обязательный |
| metaDataCaptureSettings | [MetaDataCapturing](#openapi-definition-MetaDataCapturing)[] | Настройки захвата метаданных JavaScript-агентом. | Опциональный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки мониторинга реальных пользователей. | Обязательный |
| name | string | Название веб-приложения, отображаемое в UI. | Обязательный |
| realUserMonitoringEnabled | boolean | Мониторинг реальных пользователей включён/выключен. | Обязательный |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки session replay | Опциональный |
| type | string | Тип веб-приложения. Элемент может содержать следующие значения: * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` | Опциональный |
| urlInjectionPattern | string | Шаблон внедрения url для веб-приложения ручного типа. | Опциональный |
| userActionAndSessionProperties | [UserActionAndSessionProperties](#openapi-definition-UserActionAndSessionProperties)[] | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений | Опциональный |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. | Опциональный |
| userTags | [UserTag](#openapi-definition-UserTag)[] | Настройки пользовательских тегов. | Опциональный |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, получаемые для ресурсов сторонних поставщиков, CDN и первичных ресурсов. | Обязательный |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Обязательный |
| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности XHR-действий. Элемент может содержать следующие значения: * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` | Обязательный |


#### Объект `ConversionGoal`


Цель конверсии приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. | Опциональный |
| id | string | ID цели конверсии.  Не указывать при создании новой цели конверсии. | Опциональный |
| name | string | Название цели конверсии. | Обязательный |
| type | string | Тип цели конверсии. Элемент может содержать следующие значения: * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` | Опциональный |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. | Опциональный |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. | Опциональный |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе числа пользовательских действий. | Опциональный |


#### Объект `DestinationDetails`


Конфигурация цели конверсии на основе назначения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| caseSensitive | boolean | Совпадение с учётом регистра (`true`) или без учёта (`false`). | Опциональный |
| matchType | string | Оператор совпадения. Элемент может содержать следующие значения: * `Begins` * `Contains` * `Ends` | Опциональный |
| urlOrPath | string | Путь, который нужно достичь для выполнения цели конверсии. | Обязательный |


#### Объект `UserActionDetails`


Конфигурация цели конверсии на основе пользовательского действия.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionType | string | Тип действия, к которому применяется правило. Элемент может содержать следующие значения: * `Custom` * `Load` * `Xhr` | Опциональный |
| caseSensitive | boolean | Совпадение с учётом регистра (`true`) или без учёта (`false`). | Опциональный |
| matchEntity | string | Тип сущности, к которой применяется правило. Элемент может содержать следующие значения: * `ActionName` * `PageUrl` | Опциональный |
| matchType | string | Оператор совпадения. Элемент может содержать следующие значения: * `Begins` * `Contains` * `Ends` | Опциональный |
| value | string | Значение, которое должно совпасть для выполнения цели конверсии. | Опциональный |


#### Объект `VisitDurationDetails`


Конфигурация цели конверсии на основе длительности визита.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| durationInMillis | integer | Длительность сессии для выполнения цели конверсии, в миллисекундах. | Обязательный |


#### Объект `VisitNumActionDetails`


Конфигурация цели конверсии на основе числа пользовательских действий.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| numUserActions | integer | Число пользовательских действий для выполнения цели конверсии. | Опциональный |


#### Объект `Apdex`


Определяет настройки Apdex приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| frustratingFallbackThreshold | number | Резервный порог XHR-действия, определяющий приемлемый пользовательский опыт, когда настроенный KPM недоступен. | Опциональный |
| frustratingThreshold | number | Максимальное значение apdex, считающееся приемлемым пользовательским опытом. | Опциональный |
| toleratedFallbackThreshold | number | Резервный порог XHR-действия, определяющий удовлетворительный пользовательский опыт, когда настроенный KPM недоступен. | Опциональный |
| toleratedThreshold | number | Максимальное значение apdex, считающееся удовлетворительным пользовательским опытом. | Опциональный |


#### Объект `MetaDataCapturing`


Конфигурация захвата метаданных с помощью Javascript-агента. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capturingName | string | Название захватываемых метаданных. | Обязательный |
| name | string | Название для отображения захваченных значений в Dynatrace. | Обязательный |
| publicMetadata | boolean | True, если эти метаданные нужно захватывать независимо от настроек приватности | Опциональный |
| type | string | Тип захватываемых метаданных. Элемент может содержать следующие значения: * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` | Обязательный |
| uniqueId | integer | Уникальный id захватываемых метаданных. | Опциональный |
| useLastValue | boolean | True, если для этих метаданных нужно использовать последнее захваченное значение. По умолчанию используется первое значение. | Опциональный |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |


#### Объект `MonitoringSettings`


Настройки мониторинга реальных пользователей.

| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Добавляет атрибут cross origin = anonymous для захвата сообщений об ошибках JavaScript и таймингов ресурсов W3C. | Опционально |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Расширенные настройки JavaScript-тега. | Обязательно |
| angularPackageName | string | Название пакета angular. | Опционально |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки ограничения по типу браузера, версии, платформе и компаратору. Также ограничивает режим. | Опционально |
| cacheControlHeaderOptimizations | boolean | Оптимизация значения заголовков cache control для использования с Dynatrace real user monitoring, включено/выключено. | Обязательно |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки захвата содержимого. | Обязательно |
| cookiePlacementDomain | string | Домен для размещения cookie. | Опционально |
| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, нужно задать регулярное выражение, соответствующее этим вызовам, тогда Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим конечным точкам в AWS.  Важно: эти конечные точки должны принимать заголовок x-dtc, иначе запросы завершатся ошибкой. | Опционально |
| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для приложения. Для этого нужно указать пары ключ=значение, разделённые символом (|). | Обязательно |
| excludeXhrRegex | string | Можно исключить некоторые действия из преобразования в XHR-действия.  Здесь указывается регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. | Обязательно |
| fetchRequests | boolean | Захват запросов `fetch()`, включено/выключено. | Обязательно |
| injectionMode | string | Режим внедрения JavaScript. Элемент может принимать следующие значения * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` | Обязательно |
| instrumentedWebServer | boolean | Инструментированный веб- или app-сервер. | Опционально |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки ограничения по определённым IP-адресам и для указания маски подсети. Также ограничивает режим. | Опционально |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. | Обязательно |
| javaScriptInjectionRules | [JavaScriptInjectionRules](#openapi-definition-JavaScriptInjectionRules)[] | Правила внедрения JavaScript. | Опционально |
| libraryFileFromCdn | boolean | Получать файл библиотеки JavaScript из CDN.  Не поддерживается для agentless-приложений и считается false для приложений с авто-внедрением, если не указано. | Опционально |
| libraryFileLocation | string | Расположение пользовательского файла библиотеки JavaScript приложения.  Если ничего не указано, используется корневой каталог веб-сервера.  **Обязательно** для приложений с авто-внедрением, не поддерживается для agentless-приложений. | Опционально |
| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Нужно указать относительный или абсолютный URL. При использовании абсолютного URL данные отправляются через CORS.  **Обязательно** для приложений с авто-внедрением, опционально для agentless-приложений. | Опционально |
| sameSiteCookieAttribute | string | Атрибут same site cookie. Элемент может принимать следующие значения * `LAX` * `NONE` * `STRICT` | Опционально |
| scriptTagCacheDurationInHours | integer | Длительность для настроек кэширования. | Опционально |
| secureCookieAttribute | boolean | Использование атрибута secure для Dynatrace cookie, включено/выключено. | Обязательно |
| serverRequestPathId | string | Путь для идентификации ID запроса сервера. | Обязательно |
| useCors | boolean | Отправлять данные beacon через CORS. | Опционально |
| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest`, включено/выключено. | Обязательно |


#### Объект `AdvancedJavaScriptTagSettings`


Расширенные настройки JavaScript-тега.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики событий и обёртки. | Обязательно |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | Помимо обработчиков событий, можно захватывать события, вызванные через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице. | Обязательно |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. | Обязательно |
| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков, включено/выключено. | Обязательно |
| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения от 5 до 10000. | Обязательно |
| maxErrorsToCapture | integer | Максимальное число ошибок, захватываемых на страницу. Допустимые значения от 0 до 50. | Обязательно |
| proxyWrapperEnabled | boolean | Прокси-обёртка, включено/выключено. | Опционально |
| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать неалфавитно-цифровыми символами в формате HTML escape. | Обязательно |
| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest в Firefox, включено/выключено. | Опционально |
| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest в Internet Explorer, включено/выключено. | Опционально |
| userActionNameAttribute | string | Атрибут имени пользовательского действия. | Опционально |


#### Объект `AdditionalEventHandlers`


Дополнительные обработчики событий и обёртки.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| blurEventHandler | boolean | Обработчик события blur, включено/выключено. | Обязательно |
| changeEventHandler | boolean | Обработчик события change, включено/выключено. | Обязательно |
| clickEventHandler | boolean | Обработчик события click, включено/выключено. | Обязательно |
| maxDomNodesToInstrument | integer | Максимальное число инструментируемых DOM-узлов. Допустимые значения от 0 до 100000. | Обязательно |
| mouseupEventHandler | boolean | Обработчик события mouseup, включено/выключено. | Обязательно |
| toStringMethod | boolean | Метод toString, включено/выключено. | Обязательно |
| userMouseupEventForClicks | boolean | Использование события mouseup для кликов, включено/выключено. | Обязательно |


#### Объект `EventWrapperSettings`


Помимо обработчиков событий, можно захватывать события, вызванные через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| blur | boolean | Blur, включено/выключено. | Обязательно |
| change | boolean | Change, включено/выключено. | Обязательно |
| click | boolean | Click, включено/выключено. | Обязательно |
| mouseUp | boolean | MouseUp, включено/выключено. | Обязательно |
| touchEnd | boolean | TouchEnd, включено/выключено. | Обязательно |
| touchStart | boolean | TouchStart, включено/выключено. | Обязательно |


#### Объект `GlobalEventCaptureSettings`


Настройки глобального захвата событий.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Дополнительные события, захватываемые глобально как пользовательский ввод.  Например, DragStart или DragEnd. | Обязательно |
| change | boolean | Change, включено/выключено. | Опционально |
| click | boolean | Click, включено/выключено. | Обязательно |
| doubleClick | boolean | DoubleClick, включено/выключено. | Обязательно |
| keyDown | boolean | KeyDown, включено/выключено. | Обязательно |
| keyUp | boolean | KeyUp, включено/выключено. | Обязательно |
| mouseDown | boolean | MouseDown, включено/выключено. | Обязательно |
| mouseUp | boolean | MouseUp, включено/выключено. | Обязательно |
| scroll | boolean | Scroll, включено/выключено. | Обязательно |
| touchEnd | boolean | TouchEnd, включено/выключено. | Опционально |
| touchStart | boolean | TouchStart, включено/выключено. | Опционально |


#### Объект `WebApplicationConfigBrowserRestrictionSettings`


Настройки ограничения по типу браузера, версии, платформе и компаратору. Также ограничивает режим.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction](#openapi-definition-WebApplicationConfigBrowserRestriction)[] | Список ограничений браузера. | Опционально |
| mode | string | Режим списка ограничений браузера. Элемент может принимать следующие значения * `EXCLUDE` * `INCLUDE` | Обязательно |


#### Объект `WebApplicationConfigBrowserRestriction`


Правила исключения браузеров для тех браузеров, которые нужно исключить.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| browserType | string | Тип используемого браузера. Элемент может принимать следующие значения * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` | Обязательно |
| browserVersion | string | Версия используемого браузера. | Опционально |
| comparator | string | Сравнивает разные браузеры между собой. Элемент может принимать следующие значения * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` | Опционально |
| platform | string | Платформа, на которой используется браузер. Элемент может принимать следующие значения * `ALL` * `DESKTOP` * `MOBILE` | Опционально |


#### Объект `ContentCapture`


Настройки захвата содержимого.

| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| javaScriptErrors | boolean | Мониторинг ошибок JavaScript включён/выключен. | Обязательно |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки для захвата resource timings. | Обязательно |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки для захвата timed action. | Обязательно |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки для VisuallyComplete2 | Опционально |
| visuallyCompleteAndSpeedIndex | boolean | Поддержка Visually complete и Speed index включена/выключена. | Обязательно |


#### Объект `ResourceTimingSettings`


Настройки для захвата resource timings.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| nonW3cResourceTimings | boolean | Таймингы для файлов JavaScript и изображений в браузерах без поддержки W3C включены/выключены. | Обязательно |
| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и изображений в браузерах, не предоставляющих W3C resource timings. Допустимые значения от 0 до 9999. Действует только если включён параметр **nonW3cResourceTimings**. | Обязательно |
| resourceTimingCaptureType | string | Определяет, насколько детально захватываются resource timings. Действует только если включён параметр **w3cResourceTimings** или **nonW3cResourceTimings**. Элемент может принимать следующие значения * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` | Опционально |
| resourceTimingsDomainLimit | integer | Ограничивает число доменов, для которых захватываются W3C resource timings. Действует только если **resourceTimingCaptureType** равен `CAPTURE_LIMITED_SUMMARIES`. | Опционально |
| w3cResourceTimings | boolean | W3C resource timings для сторонних доменов/CDN включены/выключены. | Обязательно |


#### Объект `TimeoutSettings`


Настройки для захвата timed action.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Определяет, насколько глубоко могут каскадироваться временные действия (temporary actions). 0 полностью отключает временные действия. Рекомендуемое значение при включении, 3. | Обязательно |
| temporaryActionTotalTimeout | integer | Общий таймаут всех каскадных таймаутов, при котором ещё возможно создание временного действия | Обязательно |
| timedActionSupport | boolean | Поддержка timed action включена/выключена. Включить для обнаружения действий, инициирующих отправку XHR через методы *setTimout*. | Обязательно |


#### Объект `VisuallyComplete2Settings`


Настройки для VisuallyComplete2


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. | Опционально |
| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при расчёте VC и SI | Опционально |
| inactivityTimeout | integer | Время в мс, в течение которого модуль VC ожидает отсутствия мутаций на странице после действия загрузки. По умолчанию 1000. | Опционально |
| mutationTimeout | integer | Определяет время в мс, которое VC ожидает после закрытия действия перед началом расчёта. По умолчанию 50. | Опционально |
| threshold | integer | Минимальная видимая область в пикселях для элементов, учитываемых в VC и SI. По умолчанию 50. | Опционально |


#### Объект `WebApplicationConfigIpAddressRestrictionSettings`


Настройки для ограничения определённых IP-адресов и задания маски подсети. Также определяет режим.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange](#openapi-definition-IpAddressRange)[] | - | Опционально |
| mode | string | Режим списка ограничений IP-адресов. Элемент может принимать следующие значения * `EXCLUDE` * `INCLUDE` | Обязательно |


#### Объект `IpAddressRange`


IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| address | string | Сопоставляемый IP-адрес. Для диапазона IP-адресов это начальный адрес (**from**). | Обязательно |
| addressTo | string | Конечный адрес (**to**) диапазона IP-адресов. | Опционально |
| subnetMask | integer | Маска подсети диапазона IP-адресов. | Опционально |


#### Объект `JavaScriptFrameworkSupport`


Поддержка различных фреймворков JavaScript.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| activeXObject | boolean | Поддержка обнаружения ActiveXObject включена/выключена. | Обязательно |
| angular | boolean | Поддержка AngularJS и Angular включена/выключена. | Обязательно |
| dojo | boolean | Поддержка Dojo включена/выключена. | Обязательно |
| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/выключена. | Обязательно |
| icefaces | boolean | Поддержка ICEfaces включена/выключена. | Обязательно |
| jQuery | boolean | Поддержка jQuery, Backbone.js включена/выключена. | Обязательно |
| mooTools | boolean | Поддержка MooTools включена/выключена. | Обязательно |
| prototype | boolean | Поддержка Prototype включена/выключена. | Обязательно |


#### Объект `JavaScriptInjectionRules`


Правила для внедрения javascript


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| enabled | boolean | Правило включения или отключения внедрения javascript. | Обязательно |
| htmlPattern | string | HTML-паттерн внедрения javascript. | Опционально |
| rule | string | Правило url для внедрения javascript. Элемент может принимать следующие значения * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` | Обязательно |
| target | string | Цель, с которой должно сопоставляться правило внедрения javascript. Элемент может принимать следующие значения * `PAGE_QUERY` * `URL` | Опционально |
| urlOperator | string | Оператор url для внедрения javascript. Элемент может принимать следующие значения * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Обязательно |
| urlPattern | string | Паттерн url для внедрения javascript. | Опционально |


#### Объект `SessionReplaySetting`


Настройки session replay


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| costControlPercentage | integer | Процент сэмплирования session replay. | Обязательно |
| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата CSS-ресурсов. | Опционально |
| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) CSS-ресурсы сессии. | Опционально |
| enabled | boolean | SessionReplay включён. | Обязательно |


#### Объект `UserActionAndSessionProperties`

Определяет настройки пользовательских свойств userAction и session для приложения.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства. Определяет, как агрегируются несколько значений свойства. Элемент может принимать следующие значения * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Опционально |
| cleanupRule | string | Правило очистки свойства. Определяет, как извлечь нужные данные из строкового значения. Укажите там [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для нужных данных. | Опционально |
| displayName | string | Отображаемое имя свойства. | Опционально |
| ignoreCase | boolean | Если true, значение этого свойства всегда будет храниться в нижнем регистре. По умолчанию false. | Опционально |
| key | string | Ключ свойства | Обязательно |
| longStringLength | integer | Если тип LONG\_STRING, максимальная длина для этого свойства. Должна быть кратна 100. По умолчанию 200. | Опционально |
| metadataId | integer | Ссылка на uniqueId MetadataCapturingConfig. Должна быть задана, если "origin" имеет тип META\_DATA. | Опционально |
| origin | string | Источник свойства. Элемент может принимать следующие значения * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Обязательно |
| serverSideRequestAttribute | string | ID атрибута запроса. Применимо только если **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Опционально |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство сессии | Опционально |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство пользовательского действия | Опционально |
| type | string | Тип данных свойства. Элемент может принимать следующие значения * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` | Обязательно |
| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения | Обязательно |


#### Объект `UserActionNamingSettings`


Настройки именования пользовательских действий.


| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования пользовательских действий для custom actions. | Опционально |
| ignoreCase | boolean | Именование без учёта регистра. | Опционально |
| loadActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования пользовательских действий для действий загрузки. | Опционально |
| placeholders | [UserActionNamingPlaceholder](#openapi-definition-UserActionNamingPlaceholder)[] | Плейсхолдеры именования пользовательских действий. | Опционально |
| queryParameterCleanups | string[] | Список параметров, которые следует удалить из запроса перед использованием запроса в имени пользовательского действия. | Опционально |
| splitUserActionsByDomain | boolean | Отключить эту настройку, если разные домены не должны приводить к отдельным пользовательским действиям. | Опционально |
| useFirstDetectedLoadAction | boolean | Если true, используется первое найденное действие загрузки под XHR-действием. Иначе используется самое глубокое под xhr-действием | Опционально |
| xhrActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования пользовательских действий для xhr-действий. | Опционально |


#### Объект `UserActionNamingRule`


Настройки правила именования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditions | [UserActionNamingRuleCondition](#openapi-definition-UserActionNamingRuleCondition)[] | Определяет условия, при которых применяется правило именования. | Опционально |
| template | string | Шаблон именования. Фигурные скобки `{}` используются для выбора плейсхолдеров. | Обязательно |
| useOrConditions | boolean | Если задано значение `true`, условия объединяются логическим ИЛИ вместо логического И. | Опционально |


#### Объект `UserActionNamingRuleCondition`


Настройки условий для именования пользовательских действий.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| operand1 | string | Должен быть определённым плейсхолдером в фигурных скобках | Обязательно |
| operand2 | string | Должно быть null, если оператор "IS\_EMPTY", regex, если оператор "MATCHES\_REGULAR\_ERPRESSION". Во всех остальных случаях значение может быть произвольным текстом или плейсхолдером в фигурных скобках | Опционально |
| operator | string | Оператор условия. Элемент может принимать следующие значения * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` | Обязательно |


#### Объект `UserActionNamingPlaceholder`


Настройки плейсхолдера.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| input | string | Входные данные. Элемент может принимать следующие значения * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` | Обязательно |
| metadataId | integer | Ссылка на uniqueId элемента MetadataCapturingConfig. Должно быть задано, если "Input" имеет тип METADATA. | Опционально |
| name | string | Имя плейсхолдера. | Обязательно |
| processingPart | string | Часть. Элемент может принимать следующие значения * `ALL` * `ANCHOR` * `PATH` | Обязательно |
| processingSteps | [UserActionNamingPlaceholderProcessingStep](#openapi-definition-UserActionNamingPlaceholderProcessingStep)[] | Действия обработки. | Опционально |
| useGuessedElementIdentifier | boolean | Использовать идентификатор элемента, выбранный Dynatrace. | Обязательно |


#### Объект `UserActionNamingPlaceholderProcessingStep`


Настройки шага обработки.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| fallbackToInput | boolean | Если задано значение true: возвращает входное значение, если **patternBefore** или **patternAfter** не найдены, а **type** равен `SUBSTRING`.  Возвращает входное значение, если **regularExpression** не совпадает и **type** равен `EXTRACT_BY_REGULAR_EXPRESSION`.  В остальных случаях возвращается null. | Опционально |
| patternAfter | string | Паттерн после нужного значения. Он будет удалён. | Опционально |
| patternAfterSearchType | string | Нужное вхождение **patternAfter**. Элемент может принимать следующие значения * `FIRST` * `LAST` | Опционально |
| patternBefore | string | Паттерн перед нужным значением. Он будет удалён. | Опционально |
| patternBeforeSearchType | string | Нужное вхождение **patternBefore**. Элемент может принимать следующие значения * `FIRST` * `LAST` | Опционально |
| patternToReplace | string | Паттерн для замены.  Применимо только если **type** равен `REPLACE_WITH_PATTERN`. | Опционально |
| regularExpression | string | Регулярное выражение для извлекаемой или заменяемой строки.  Применимо только если **type** равен `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. | Опционально |
| replacement | string | Замена для исходного значения. | Опционально |
| type | string | Действие, выполняемое обработкой:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанное **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанное **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, соответствующую **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, соответствующие **regularExpression**, на указанное **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанное **replacement**. Элемент может принимать следующие значения * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` | Обязательно |


#### Объект `UserTag`


Определяет настройки UserTags для приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| cleanupRule | string | Выражение правила очистки userTag | Опционально |
| ignoreCase | boolean | Если true, значение этого тега всегда будет храниться в нижнем регистре. По умолчанию false. | Опционально |
| metadataId | integer | Ссылка на uniqueId элемента MetadataCapturingConfig. Должно быть задано, если UserTag основан на метаданных, захваченных JavaScript-агентом (например, JavaScript-переменная, CSS-селектор и т. д.) | Опционально |
| serverSideRequestAttribute | string | Идентификатор серверного атрибута запроса для userTag. Должно быть задано, если UserTag основан на серверном атрибуте запроса. | Опционально |
| uniqueId | integer | uniqueId, уникальный среди всех userTags и свойств этого приложения | Обязательно |


#### Объект `WaterfallSettings`


Эти настройки влияют на данные мониторинга, получаемые для сторонних, CDN и собственных ресурсов.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с более низким показателем кэширования браузера выше *X*%. | Обязательно |
| resourcesThreshold | integer | Предупреждать о ресурсах размером более *X* байт. | Обязательно |
| slowCdnResourcesThreshold | integer | Предупреждать о медленных CDN-ресурсах со временем ответа выше *X* мс. | Обязательно |
| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных собственных ресурсах со временем ответа выше *X* мс. | Обязательно |
| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных сторонних ресурсах со временем ответа выше *X* мс. | Обязательно |
| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X*% от Visually complete. | Обязательно |
| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах размером более *X* байт. | Обязательно |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая конфигурация создана. Тело ответа содержит ID и имя нового веб-приложения. |
| **204** | - | Успех. Конфигурация обновлена. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её в реальном запросе. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать его, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

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

#### Модели тела ответа JSON

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