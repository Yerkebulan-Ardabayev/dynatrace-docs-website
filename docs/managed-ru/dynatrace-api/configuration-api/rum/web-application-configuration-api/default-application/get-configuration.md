---
title: Web application configuration API - GET default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/get-configuration
scraped: 2026-05-12T11:17:08.157862
---

# Web application configuration API - GET default application

# Web application configuration API - GET default application

* Reference
* Published Sep 03, 2019

Возвращает параметры веб-приложения по умолчанию вашего окружения Dynatrace.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

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
| conversionGoals | [ConversionGoal[]](#openapi-definition-ConversionGoal) | Список целей конверсии приложения. |
| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. |
| identifier | string | ID сущности Dynatrace для веб-приложения. |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. |
| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности действий загрузки. Возможные значения: * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` |
| metaDataCaptureSettings | [MetaDataCapturing[]](#openapi-definition-MetaDataCapturing) | Настройки захвата метаданных JavaScript-агентом. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки мониторинга реальных пользователей. |
| name | string | Имя веб-приложения, отображаемое в UI. |
| realUserMonitoringEnabled | boolean | Мониторинг реальных пользователей включён/отключён. |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки Session Replay |
| type | string | Тип веб-приложения. Возможные значения: * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` |
| urlInjectionPattern | string | Шаблон внедрения URL для ручного веб-приложения. |
| userActionAndSessionProperties | [UserActionAndSessionProperties[]](#openapi-definition-UserActionAndSessionProperties) | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. |
| userTags | [UserTag[]](#openapi-definition-UserTag) | Настройки пользовательских тегов. |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов. |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. |
| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности XHR-действий. Возможные значения: * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` |

#### Объект `ConversionGoal`

Цель конверсии приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. |
| id | string | ID цели конверсии.  Не указывайте его при создании новой цели конверсии. |
| name | string | Имя цели конверсии. |
| type | string | Тип цели конверсии. Возможные значения: * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе количества пользовательских действий. |

#### Объект `DestinationDetails`

Конфигурация цели конверсии на основе назначения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| caseSensitive | boolean | Сопоставление чувствительно к регистру (`true`) или нет (`false`). |
| matchType | string | Оператор сопоставления. Возможные значения: * `Begins` * `Contains` * `Ends` |
| urlOrPath | string | Путь, который нужно достичь для выполнения цели конверсии. |

#### Объект `UserActionDetails`

Конфигурация цели конверсии на основе пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| actionType | string | Тип действия, к которому применяется правило. Возможные значения: * `Custom` * `Load` * `Xhr` |
| caseSensitive | boolean | Сопоставление чувствительно к регистру (`true`) или нет (`false`). |
| matchEntity | string | Тип сущности, к которой применяется правило. Возможные значения: * `ActionName` * `PageUrl` |
| matchType | string | Оператор сопоставления. Возможные значения: * `Begins` * `Contains` * `Ends` |
| value | string | Значение для сопоставления, чтобы выполнить цель конверсии. |

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
| frustratingFallbackThreshold | number | Резервный порог XHR-действия, определяющий приемлемый пользовательский опыт, когда настроенная KPM недоступна. |
| frustratingThreshold | number | Максимальное значение Apdex, которое считается приемлемым пользовательским опытом. |
| toleratedFallbackThreshold | number | Резервный порог XHR-действия, определяющий удовлетворительный пользовательский опыт, когда настроенная KPM недоступна. |
| toleratedThreshold | number | Максимальное значение Apdex, которое считается удовлетворительным пользовательским опытом. |

#### Объект `MetaDataCapturing`

Конфигурация захвата метаданных JavaScript-агентом. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder

| Элемент | Тип | Описание |
| --- | --- | --- |
| capturingName | string | Имя захватываемых метаданных. |
| name | string | Имя для отображения захваченных значений в Dynatrace. |
| publicMetadata | boolean | True, если эти метаданные нужно захватывать независимо от настроек конфиденциальности |
| type | string | Тип захватываемых метаданных. Возможные значения: * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` |
| uniqueId | integer | Уникальный id захватываемых метаданных. |
| useLastValue | boolean | True, если для этих метаданных нужно использовать последнее захваченное значение. По умолчанию используется первое значение. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `MonitoringSettings`

Настройки мониторинга реальных пользователей.

| Элемент | Тип | Описание |
| --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Добавить атрибут cross origin = anonymous для захвата сообщений об ошибках JavaScript и таймингов ресурсов W3C. |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Расширенные настройки JavaScript-тега. |
| angularPackageName | string | Имя пакета angular. |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивают режим. |
| cacheControlHeaderOptimizations | boolean | Оптимизация значения заголовков cache control для использования с мониторингом реальных пользователей Dynatrace включена/отключена. |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки захвата контента. |
| cookiePlacementDomain | string | Домен для размещения cookie. |
| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, задайте регулярное выражение, соответствующее этим вызовам, после чего Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим эндпоинтам в AWS.  Важно: эти эндпоинты должны принимать заголовок x-dtc, иначе запросы будут завершаться ошибкой. |
| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для вашего приложения. Для этого введите пары key=value, разделённые символом (|). |
| excludeXhrRegex | string | Вы можете исключить некоторые действия из числа XHR-действий.  Укажите здесь регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. |
| fetchRequests | boolean | Захват запросов `fetch()` включён/отключён. |
| injectionMode | string | Режим внедрения JavaScript. Возможные значения: * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` |
| instrumentedWebServer | boolean | Инструментированный веб-сервер или сервер приложений. |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки для ограничения определённых IP-адресов и для ввода маски подсети. Также ограничивают режим. |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. |
| javaScriptInjectionRules | [JavaScriptInjectionRules[]](#openapi-definition-JavaScriptInjectionRules) | Правила внедрения JavaScript. |
| libraryFileFromCdn | boolean | Получать файл библиотеки JavaScript из CDN.  Не поддерживается безагентными приложениями и считается false для авто-внедряемых приложений, если опущено. |
| libraryFileLocation | string | Расположение пользовательского файла библиотеки JavaScript вашего приложения.  Если ничего не указано, используется корневой каталог вашего веб-сервера.  **Required** для авто-внедряемых приложений, не поддерживается безагентными приложениями. |
| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Укажите относительный или абсолютный URL. Если вы используете абсолютный URL, данные будут отправляться через CORS.  **Required** для авто-внедряемых приложений, опционально для безагентных приложений. |
| sameSiteCookieAttribute | string | Атрибут cookie SameSite Возможные значения: * `LAX` * `NONE` * `STRICT` |
| scriptTagCacheDurationInHours | integer | Длительность для настроек кэша. |
| secureCookieAttribute | boolean | Использование атрибута secure для cookie Dynatrace включено/отключено. |
| serverRequestPathId | string | Путь для идентификации ID запроса сервера. |
| useCors | boolean | Отправлять данные beacon через CORS. |
| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest` включена/отключена. |

#### Объект `AdvancedJavaScriptTagSettings`

Расширенные настройки JavaScript-тега.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики и обёртки событий. |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | Помимо обработчиков событий, можно захватывать события, вызываемые через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице. |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. |
| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков включено/отключено. |
| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения: от `5` до `10000`. |
| maxErrorsToCapture | integer | Максимальное число ошибок, захватываемых на страницу. Допустимые значения: от `0` до `50`. |
| proxyWrapperEnabled | boolean | Обёртка прокси включена/отключена. |
| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать с использованием не-алфавитно-цифровых символов в формате HTML escape. |
| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest через Firefox включена/отключена. |
| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest через Internet Explorer включена/отключена. |
| userActionNameAttribute | string | Атрибут имени пользовательского действия. |

#### Объект `AdditionalEventHandlers`

Дополнительные обработчики и обёртки событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| blurEventHandler | boolean | Обработчик события blur включён/отключён. |
| changeEventHandler | boolean | Обработчик события change включён/отключён. |
| clickEventHandler | boolean | Обработчик события click включён/отключён. |
| maxDomNodesToInstrument | integer | Макс. число DOM-узлов для инструментирования. Допустимые значения: от `0` до `100000`. |
| mouseupEventHandler | boolean | Обработчик события mouseup включён/отключён. |
| toStringMethod | boolean | Метод toString включён/отключён. |
| userMouseupEventForClicks | boolean | Использование события mouseup для кликов включено/отключено. |

#### Объект `EventWrapperSettings`

Помимо обработчиков событий, можно захватывать события, вызываемые через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице.

| Элемент | Тип | Описание |
| --- | --- | --- |
| blur | boolean | Blur включён/отключён. |
| change | boolean | Change включён/отключён. |
| click | boolean | Click включён/отключён. |
| mouseUp | boolean | MouseUp включён/отключён. |
| touchEnd | boolean | TouchEnd включён/отключён. |
| touchStart | boolean | TouchStart включён/отключён. |

#### Объект `GlobalEventCaptureSettings`

Настройки глобального захвата событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Дополнительные события, захватываемые глобально как пользовательский ввод.  Например, DragStart или DragEnd. |
| change | boolean | Change включён/отключён. |
| click | boolean | Click включён/отключён. |
| doubleClick | boolean | DoubleClick включён/отключён. |
| keyDown | boolean | KeyDown включён/отключён. |
| keyUp | boolean | KeyUp включён/отключён. |
| mouseDown | boolean | MouseDown включён/отключён. |
| mouseUp | boolean | MouseUp включён/отключён. |
| scroll | boolean | Scroll включён/отключён. |
| touchEnd | boolean | TouchEnd включён/отключён. |
| touchStart | boolean | TouchStart включён/отключён. |

#### Объект `WebApplicationConfigBrowserRestrictionSettings`

Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивают режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction[]](#openapi-definition-WebApplicationConfigBrowserRestriction) | Список ограничений браузеров. |
| mode | string | Режим списка ограничений браузеров. Возможные значения: * `EXCLUDE` * `INCLUDE` |

#### Объект `WebApplicationConfigBrowserRestriction`

Правила исключения для браузеров, которые нужно исключить.

| Элемент | Тип | Описание |
| --- | --- | --- |
| browserType | string | Тип используемого браузера. Возможные значения: * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` |
| browserVersion | string | Версия используемого браузера. |
| comparator | string | Сравнивает разные браузеры между собой. Возможные значения: * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` |
| platform | string | Платформа, на которой используется браузер. Возможные значения: * `ALL` * `DESKTOP` * `MOBILE` |

#### Объект `ContentCapture`

Настройки захвата контента.

| Элемент | Тип | Описание |
| --- | --- | --- |
| javaScriptErrors | boolean | Мониторинг ошибок JavaScript включён/отключён. |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки захвата таймингов ресурсов. |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки захвата отложенных действий. |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки VisuallyComplete2 |
| visuallyCompleteAndSpeedIndex | boolean | Поддержка Visually complete и Speed index включена/отключена. |

#### Объект `ResourceTimingSettings`

Настройки захвата таймингов ресурсов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nonW3cResourceTimings | boolean | Тайминги для файлов JavaScript и изображений в браузерах без поддержки W3C включены/отключены. |
| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и ресурсов-изображений в браузерах, не предоставляющих тайминги ресурсов W3C.  Допустимые значения: от `0` до `9999`.  Действует только если **nonW3cResourceTimings** включён. |
| resourceTimingCaptureType | string | Определяет, насколько детально захватываются тайминги ресурсов.  Действует только если включён **w3cResourceTimings** или **nonW3cResourceTimings**. Возможные значения: * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` |
| resourceTimingsDomainLimit | integer | Ограничивает число доменов, для которых захватываются тайминги ресурсов W3C.  Действует только если **resourceTimingCaptureType** равен `CAPTURE_LIMITED_SUMMARIES`. |
| w3cResourceTimings | boolean | Тайминги ресурсов W3C для сторонних/CDN включены/отключены. |

#### Объект `TimeoutSettings`

Настройки захвата отложенных действий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| temporaryActionLimit | integer | Определяет, насколько глубоко могут каскадироваться временные действия. 0 полностью отключает временные действия. Рекомендуемое значение при включении равно 3. |
| temporaryActionTotalTimeout | integer | Суммарный таймаут всех каскадированных таймаутов, при котором ещё можно создать временное действие |
| timedActionSupport | boolean | Поддержка отложенных действий включена/отключена.  Включите, чтобы обнаруживать действия, которые инициируют отправку XHR через методы *setTimout*. |

#### Объект `VisuallyComplete2Settings`

Настройки VisuallyComplete2

| Элемент | Тип | Описание |
| --- | --- | --- |
| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. |
| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при расчёте VC и SI |
| inactivityTimeout | integer | Время в мс, которое модуль VC ожидает отсутствия мутаций на странице после действия загрузки. По умолчанию 1000. |
| mutationTimeout | integer | Определяет время в мс, которое VC ожидает после закрытия действия перед началом расчёта. По умолчанию 50. |
| threshold | integer | Минимальная видимая площадь элементов в пикселях, учитываемая для VC и SI. По умолчанию 50. |

#### Объект `WebApplicationConfigIpAddressRestrictionSettings`

Настройки для ограничения определённых IP-адресов и для ввода маски подсети. Также ограничивают режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange[]](#openapi-definition-IpAddressRange) | - |
| mode | string | Режим списка ограничений IP-адресов. Возможные значения: * `EXCLUDE` * `INCLUDE` |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов, сопоставляемый с локацией.

| Элемент | Тип | Описание |
| --- | --- | --- |
| address | string | Сопоставляемый IP-адрес.  Для диапазона IP-адресов это адрес **from**. |
| addressTo | string | Адрес **to** диапазона IP-адресов. |
| subnetMask | integer | Маска подсети диапазона IP-адресов. |

#### Объект `JavaScriptFrameworkSupport`

Поддержка различных JavaScript-фреймворков.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeXObject | boolean | Поддержка обнаружения ActiveXObject включена/отключена. |
| angular | boolean | Поддержка AngularJS и Angular включена/отключена. |
| dojo | boolean | Поддержка Dojo включена/отключена. |
| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/отключена. |
| icefaces | boolean | Поддержка ICEfaces включена/отключена. |
| jQuery | boolean | Поддержка jQuery, Backbone.js включена/отключена. |
| mooTools | boolean | Поддержка MooTools включена/отключена. |
| prototype | boolean | Поддержка Prototype включена/отключена. |

#### Объект `JavaScriptInjectionRules`

Правила внедрения JavaScript

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Правило включения или отключения внедрения JavaScript. |
| htmlPattern | string | HTML-шаблон внедрения JavaScript. |
| rule | string | Правило URL внедрения JavaScript. Возможные значения: * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` |
| target | string | Цель, по которой сопоставляется правило внедрения JavaScript. Возможные значения: * `PAGE_QUERY` * `URL` |
| urlOperator | string | URL-оператор внедрения JavaScript. Возможные значения: * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| urlPattern | string | URL-шаблон внедрения JavaScript. |

#### Объект `SessionReplaySetting`

Настройки Session Replay

| Элемент | Тип | Описание |
| --- | --- | --- |
| costControlPercentage | integer | Частота сэмплирования Session Replay в процентах. |
| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата CSS-ресурсов. |
| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) CSS-ресурсы из сессии. |
| enabled | boolean | Session Replay включён. |

#### Объект `UserActionAndSessionProperties`

Определяет настройки пользовательски заданных свойств пользовательских действий и сессий приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Возможные значения: * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение](https://dt-url.net/k9e0iaq) для нужных вам данных. |
| displayName | string | Отображаемое имя свойства. |
| ignoreCase | boolean | Если true, значение этого свойства всегда сохраняется в нижнем регистре. По умолчанию false. |
| key | string | Ключ свойства |
| longStringLength | integer | Если тип LONG\_STRING, максимальная длина для этого свойства. Должна быть кратна 100. По умолчанию 200. |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig.Должна быть задана, если "origin" имеет тип META\_DATA. |
| origin | string | Источник свойства Возможные значения: * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. |
| storeAsSessionProperty | boolean | Если `true`, свойство хранится как свойство сессии |
| storeAsUserActionProperty | boolean | Если `true`, свойство хранится как свойство пользовательского действия |
| type | string | Тип данных свойства. Возможные значения: * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` |
| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения |

#### Объект `UserActionNamingSettings`

Настройки именования пользовательских действий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для пользовательских действий. |
| ignoreCase | boolean | Именование без учёта регистра. |
| loadActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для действий загрузки. |
| placeholders | [UserActionNamingPlaceholder[]](#openapi-definition-UserActionNamingPlaceholder) | Плейсхолдеры пользовательских действий. |
| queryParameterCleanups | string[] | Список параметров, которые нужно удалить из запроса перед использованием запроса в имени пользовательского действия. |
| splitUserActionsByDomain | boolean | Отключите эту настройку, если разные домены не должны приводить к отдельным пользовательским действиям. |
| useFirstDetectedLoadAction | boolean | Если true, используется первое действие загрузки, найденное под XHR-действием. Иначе используется самое глубокое под XHR-действием |
| xhrActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для XHR-действий. |

#### Объект `UserActionNamingRule`

Настройки правила именования.

| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [UserActionNamingRuleCondition[]](#openapi-definition-UserActionNamingRuleCondition) | Определяет условия, при которых должно применяться правило именования. |
| template | string | Шаблон именования. Используйте фигурные скобки `{}` для выбора плейсхолдеров. |
| useOrConditions | boolean | Если установлено `true`, условия соединяются логическим OR вместо логического AND. |

#### Объект `UserActionNamingRuleCondition`

Настройки условий именования пользовательских действий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operand1 | string | Должен быть определённым плейсхолдером в фигурных скобках |
| operand2 | string | Должен быть null, если оператор "IS\_EMPTY", регулярным выражением, если оператор "MATCHES\_REGULAR\_ERPRESSION". Во всех остальных случаях значение может быть произвольным текстом или плейсхолдером в фигурных скобках |
| operator | string | Оператор условия Возможные значения: * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` |

#### Объект `UserActionNamingPlaceholder`

Настройки плейсхолдера.

| Элемент | Тип | Описание |
| --- | --- | --- |
| input | string | Ввод. Возможные значения: * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если "Input" имеет тип METADATA. |
| name | string | Имя плейсхолдера. |
| processingPart | string | Часть. Возможные значения: * `ALL` * `ANCHOR` * `PATH` |
| processingSteps | [UserActionNamingPlaceholderProcessingStep[]](#openapi-definition-UserActionNamingPlaceholderProcessingStep) | Действия обработки. |
| useGuessedElementIdentifier | boolean | Использовать идентификатор элемента, выбранный Dynatrace. |

#### Объект `UserActionNamingPlaceholderProcessingStep`

Настройки шага обработки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| fallbackToInput | boolean | Если установлено true: возвращает ввод, если **patternBefore** или **patternAfter** не найдены и **type** равен `SUBSTRING`.  Возвращает ввод, если **regularExpression** не совпадает и **type** равен `EXTRACT_BY_REGULAR_EXPRESSION`.  Иначе возвращается null. |
| patternAfter | string | Шаблон после нужного значения. Он будет удалён. |
| patternAfterSearchType | string | Нужное вхождение **patternAfter**. Возможные значения: * `FIRST` * `LAST` |
| patternBefore | string | Шаблон перед нужным значением. Он будет удалён. |
| patternBeforeSearchType | string | Нужное вхождение **patternBefore**. Возможные значения: * `FIRST` * `LAST` |
| patternToReplace | string | Заменяемый шаблон.  Применимо только если **type** равен `REPLACE_WITH_PATTERN`. |
| regularExpression | string | Регулярное выражение для извлекаемой или заменяемой строки.  Применимо только если **type** равен `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. |
| replacement | string | Замена для исходного значения. |
| type | string | Действие, выполняемое при обработке:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанную **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанную **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, соответствующую **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, соответствующие **regularExpression**, на указанную **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанную **replacement**. Возможные значения: * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` |

#### Объект `UserTag`

Определяет настройки UserTags приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| cleanupRule | string | Выражение правила очистки userTag |
| ignoreCase | boolean | Если true, значение этого тега всегда сохраняется в нижнем регистре. По умолчанию false. |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если UserTag основан на метаданных, захваченных JavaScript-агентом (например, переменная JavaScript, CSS-селектор и т. д.) |
| serverSideRequestAttribute | string | ID серверного атрибута запроса userTag. Должен быть задан, если UserTag основан на серверном атрибуте запроса. |
| uniqueId | integer | uniqueId, уникальный среди всех userTags и свойств этого приложения |

#### The `WaterfallSettings` object

Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с более низкой частотой кэширования браузером выше *X*%. |
| resourcesThreshold | integer | Предупреждать о ресурсах больше *X* байт. |
| slowCdnResourcesThreshold | integer | Предупреждать о медленных CDN-ресурсах со временем отклика выше *X* мс. |
| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных собственных ресурсах со временем отклика выше *X* мс. |
| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных сторонних ресурсах со временем отклика выше *X* мс. |
| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X* % от Visually complete. |
| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах больше *X* байт. |

### JSON-модели тела ответа

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