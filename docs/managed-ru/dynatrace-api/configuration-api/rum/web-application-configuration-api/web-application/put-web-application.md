---
title: Web application configuration API - PUT a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application
scraped: 2026-05-12T11:16:44.314635
---

# Web application configuration API - PUT a web application

# Web application configuration API - PUT a web application

* Reference
* Published Sep 03, 2019

Обновляет указанное веб-приложение.

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений смотрите [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace mobile и custom app config API.").

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID обновляемого веб-приложения.  Если вы также укажете ID в теле, он должен совпадать с этим ID. | path | Required |
| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON-тело запроса, содержащее обновлённую конфигурацию веб-приложения. | body | Optional |

### Объекты тела запроса

#### Объект `WebApplicationConfig`

Конфигурация веб-приложения.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| conversionGoals | [ConversionGoal[]](#openapi-definition-ConversionGoal) | Список целей конверсии приложения. | Optional |
| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. | Required |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Required |
| identifier | string | ID сущности Dynatrace для веб-приложения. | Optional |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Required |
| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности действий загрузки. Возможные значения: * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` | Required |
| metaDataCaptureSettings | [MetaDataCapturing[]](#openapi-definition-MetaDataCapturing) | Настройки захвата метаданных JavaScript-агентом. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки мониторинга реальных пользователей. | Required |
| name | string | Имя веб-приложения, отображаемое в UI. | Required |
| realUserMonitoringEnabled | boolean | Мониторинг реальных пользователей включён/отключён. | Required |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки Session Replay | Optional |
| type | string | Тип веб-приложения. Возможные значения: * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` | Optional |
| urlInjectionPattern | string | Шаблон внедрения URL для ручного веб-приложения. | Optional |
| userActionAndSessionProperties | [UserActionAndSessionProperties[]](#openapi-definition-UserActionAndSessionProperties) | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений | Optional |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. | Optional |
| userTags | [UserTag[]](#openapi-definition-UserTag) | Настройки пользовательских тегов. | Optional |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов. | Required |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Required |
| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности XHR-действий. Возможные значения: * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` | Required |

#### Объект `ConversionGoal`

Цель конверсии приложения.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. | Optional |
| id | string | ID цели конверсии.  Не указывайте его при создании новой цели конверсии. | Optional |
| name | string | Имя цели конверсии. | Required |
| type | string | Тип цели конверсии. Возможные значения: * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` | Optional |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. | Optional |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. | Optional |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе количества пользовательских действий. | Optional |

#### Объект `DestinationDetails`

Конфигурация цели конверсии на основе назначения.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| caseSensitive | boolean | Сопоставление чувствительно к регистру (`true`) или нет (`false`). | Optional |
| matchType | string | Оператор сопоставления. Возможные значения: * `Begins` * `Contains` * `Ends` | Optional |
| urlOrPath | string | Путь, который нужно достичь для выполнения цели конверсии. | Required |

#### Объект `UserActionDetails`

Конфигурация цели конверсии на основе пользовательского действия.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| actionType | string | Тип действия, к которому применяется правило. Возможные значения: * `Custom` * `Load` * `Xhr` | Optional |
| caseSensitive | boolean | Сопоставление чувствительно к регистру (`true`) или нет (`false`). | Optional |
| matchEntity | string | Тип сущности, к которой применяется правило. Возможные значения: * `ActionName` * `PageUrl` | Optional |
| matchType | string | Оператор сопоставления. Возможные значения: * `Begins` * `Contains` * `Ends` | Optional |
| value | string | Значение для сопоставления, чтобы выполнить цель конверсии. | Optional |

#### Объект `VisitDurationDetails`

Конфигурация цели конверсии на основе длительности визита.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| durationInMillis | integer | Длительность сессии для выполнения цели конверсии, в миллисекундах. | Required |

#### Объект `VisitNumActionDetails`

Конфигурация цели конверсии на основе количества пользовательских действий.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| numUserActions | integer | Количество пользовательских действий для выполнения цели конверсии. | Optional |

#### Объект `Apdex`

Определяет настройки Apdex приложения.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| frustratingFallbackThreshold | number | Резервный порог XHR-действия, определяющий приемлемый пользовательский опыт, когда настроенная KPM недоступна. | Optional |
| frustratingThreshold | number | Максимальное значение Apdex, которое считается приемлемым пользовательским опытом. | Optional |
| toleratedFallbackThreshold | number | Резервный порог XHR-действия, определяющий удовлетворительный пользовательский опыт, когда настроенная KPM недоступна. | Optional |
| toleratedThreshold | number | Максимальное значение Apdex, которое считается удовлетворительным пользовательским опытом. | Optional |

#### Объект `MetaDataCapturing`

Конфигурация захвата метаданных JavaScript-агентом. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| capturingName | string | Имя захватываемых метаданных. | Required |
| name | string | Имя для отображения захваченных значений в Dynatrace. | Required |
| publicMetadata | boolean | True, если эти метаданные нужно захватывать независимо от настроек конфиденциальности | Optional |
| type | string | Тип захватываемых метаданных. Возможные значения: * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` | Required |
| uniqueId | integer | Уникальный id захватываемых метаданных. | Optional |
| useLastValue | boolean | True, если для этих метаданных нужно использовать последнее захваченное значение. По умолчанию используется первое значение. | Optional |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `MonitoringSettings`

Настройки мониторинга реальных пользователей.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Добавить атрибут cross origin = anonymous для захвата сообщений об ошибках JavaScript и таймингов ресурсов W3C. | Optional |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Расширенные настройки JavaScript-тега. | Required |
| angularPackageName | string | Имя пакета angular. | Optional |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивают режим. | Optional |
| cacheControlHeaderOptimizations | boolean | Оптимизация значения заголовков cache control для использования с мониторингом реальных пользователей Dynatrace включена/отключена. | Required |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки захвата контента. | Required |
| cookiePlacementDomain | string | Домен для размещения cookie. | Optional |
| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, задайте регулярное выражение, соответствующее этим вызовам, после чего Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим эндпоинтам в AWS.  Важно: эти эндпоинты должны принимать заголовок x-dtc, иначе запросы будут завершаться ошибкой. | Optional |
| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для вашего приложения. Для этого введите пары key=value, разделённые символом (|). | Required |
| excludeXhrRegex | string | Вы можете исключить некоторые действия из числа XHR-действий.  Укажите здесь регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. | Required |
| fetchRequests | boolean | Захват запросов `fetch()` включён/отключён. | Required |
| injectionMode | string | Режим внедрения JavaScript. Возможные значения: * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` | Required |
| instrumentedWebServer | boolean | Инструментированный веб-сервер или сервер приложений. | Optional |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки для ограничения определённых IP-адресов и для ввода маски подсети. Также ограничивают режим. | Optional |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. | Required |
| javaScriptInjectionRules | [JavaScriptInjectionRules[]](#openapi-definition-JavaScriptInjectionRules) | Правила внедрения JavaScript. | Optional |
| libraryFileFromCdn | boolean | Получать файл библиотеки JavaScript из CDN.  Не поддерживается безагентными приложениями и считается false для авто-внедряемых приложений, если опущено. | Optional |
| libraryFileLocation | string | Расположение пользовательского файла библиотеки JavaScript вашего приложения.  Если ничего не указано, используется корневой каталог вашего веб-сервера.  **Required** для авто-внедряемых приложений, не поддерживается безагентными приложениями. | Optional |
| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Укажите относительный или абсолютный URL. Если вы используете абсолютный URL, данные будут отправляться через CORS.  **Required** для авто-внедряемых приложений, опционально для безагентных приложений. | Optional |
| sameSiteCookieAttribute | string | Атрибут cookie SameSite Возможные значения: * `LAX` * `NONE` * `STRICT` | Optional |
| scriptTagCacheDurationInHours | integer | Длительность для настроек кэша. | Optional |
| secureCookieAttribute | boolean | Использование атрибута secure для cookie Dynatrace включено/отключено. | Required |
| serverRequestPathId | string | Путь для идентификации ID запроса сервера. | Required |
| useCors | boolean | Отправлять данные beacon через CORS. | Optional |
| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest` включена/отключена. | Required |

#### Объект `AdvancedJavaScriptTagSettings`

Расширенные настройки JavaScript-тега.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики и обёртки событий. | Required |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | Помимо обработчиков событий, можно захватывать события, вызываемые через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице. | Required |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. | Required |
| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков включено/отключено. | Required |
| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения: от `5` до `10000`. | Required |
| maxErrorsToCapture | integer | Максимальное число ошибок, захватываемых на страницу. Допустимые значения: от `0` до `50`. | Required |
| proxyWrapperEnabled | boolean | Обёртка прокси включена/отключена. | Optional |
| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать с использованием не-алфавитно-цифровых символов в формате HTML escape. | Required |
| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest через Firefox включена/отключена. | Optional |
| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest через Internet Explorer включена/отключена. | Optional |
| userActionNameAttribute | string | Атрибут имени пользовательского действия. | Optional |

#### Объект `AdditionalEventHandlers`

Дополнительные обработчики и обёртки событий.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| blurEventHandler | boolean | Обработчик события blur включён/отключён. | Required |
| changeEventHandler | boolean | Обработчик события change включён/отключён. | Required |
| clickEventHandler | boolean | Обработчик события click включён/отключён. | Required |
| maxDomNodesToInstrument | integer | Макс. число DOM-узлов для инструментирования. Допустимые значения: от `0` до `100000`. | Required |
| mouseupEventHandler | boolean | Обработчик события mouseup включён/отключён. | Required |
| toStringMethod | boolean | Метод toString включён/отключён. | Required |
| userMouseupEventForClicks | boolean | Использование события mouseup для кликов включено/отключено. | Required |

#### Объект `EventWrapperSettings`

Помимо обработчиков событий, можно захватывать события, вызываемые через `addEventListener` или `attachEvent`. Будьте осторожны с этой опцией! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| blur | boolean | Blur включён/отключён. | Required |
| change | boolean | Change включён/отключён. | Required |
| click | boolean | Click включён/отключён. | Required |
| mouseUp | boolean | MouseUp включён/отключён. | Required |
| touchEnd | boolean | TouchEnd включён/отключён. | Required |
| touchStart | boolean | TouchStart включён/отключён. | Required |

#### Объект `GlobalEventCaptureSettings`

Настройки глобального захвата событий.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Дополнительные события, захватываемые глобально как пользовательский ввод.  Например, DragStart или DragEnd. | Required |
| change | boolean | Change включён/отключён. | Optional |
| click | boolean | Click включён/отключён. | Required |
| doubleClick | boolean | DoubleClick включён/отключён. | Required |
| keyDown | boolean | KeyDown включён/отключён. | Required |
| keyUp | boolean | KeyUp включён/отключён. | Required |
| mouseDown | boolean | MouseDown включён/отключён. | Required |
| mouseUp | boolean | MouseUp включён/отключён. | Required |
| scroll | boolean | Scroll включён/отключён. | Required |
| touchEnd | boolean | TouchEnd включён/отключён. | Optional |
| touchStart | boolean | TouchStart включён/отключён. | Optional |

#### Объект `WebApplicationConfigBrowserRestrictionSettings`

Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивают режим.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction[]](#openapi-definition-WebApplicationConfigBrowserRestriction) | Список ограничений браузеров. | Optional |
| mode | string | Режим списка ограничений браузеров. Возможные значения: * `EXCLUDE` * `INCLUDE` | Required |

#### Объект `WebApplicationConfigBrowserRestriction`

Правила исключения для браузеров, которые нужно исключить.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| browserType | string | Тип используемого браузера. Возможные значения: * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` | Required |
| browserVersion | string | Версия используемого браузера. | Optional |
| comparator | string | Сравнивает разные браузеры между собой. Возможные значения: * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` | Optional |
| platform | string | Платформа, на которой используется браузер. Возможные значения: * `ALL` * `DESKTOP` * `MOBILE` | Optional |

#### Объект `ContentCapture`

Настройки захвата контента.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| javaScriptErrors | boolean | Мониторинг ошибок JavaScript включён/отключён. | Required |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки захвата таймингов ресурсов. | Required |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки захвата отложенных действий. | Required |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки VisuallyComplete2 | Optional |
| visuallyCompleteAndSpeedIndex | boolean | Поддержка Visually complete и Speed index включена/отключена. | Required |

#### Объект `ResourceTimingSettings`

Настройки захвата таймингов ресурсов.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| nonW3cResourceTimings | boolean | Тайминги для файлов JavaScript и изображений в браузерах без поддержки W3C включены/отключены. | Required |
| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и ресурсов-изображений в браузерах, не предоставляющих тайминги ресурсов W3C.  Допустимые значения: от `0` до `9999`.  Действует только если **nonW3cResourceTimings** включён. | Required |
| resourceTimingCaptureType | string | Определяет, насколько детально захватываются тайминги ресурсов.  Действует только если включён **w3cResourceTimings** или **nonW3cResourceTimings**. Возможные значения: * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` | Optional |
| resourceTimingsDomainLimit | integer | Ограничивает число доменов, для которых захватываются тайминги ресурсов W3C.  Действует только если **resourceTimingCaptureType** равен `CAPTURE_LIMITED_SUMMARIES`. | Optional |
| w3cResourceTimings | boolean | Тайминги ресурсов W3C для сторонних/CDN включены/отключены. | Required |

#### Объект `TimeoutSettings`

Настройки захвата отложенных действий.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Определяет, насколько глубоко могут каскадироваться временные действия. 0 полностью отключает временные действия. Рекомендуемое значение при включении равно 3. | Required |
| temporaryActionTotalTimeout | integer | Суммарный таймаут всех каскадированных таймаутов, при котором ещё можно создать временное действие | Required |
| timedActionSupport | boolean | Поддержка отложенных действий включена/отключена.  Включите, чтобы обнаруживать действия, которые инициируют отправку XHR через методы *setTimout*. | Required |

#### Объект `VisuallyComplete2Settings`

Настройки VisuallyComplete2

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. | Optional |
| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при расчёте VC и SI | Optional |
| inactivityTimeout | integer | Время в мс, которое модуль VC ожидает отсутствия мутаций на странице после действия загрузки. По умолчанию 1000. | Optional |
| mutationTimeout | integer | Определяет время в мс, которое VC ожидает после закрытия действия перед началом расчёта. По умолчанию 50. | Optional |
| threshold | integer | Минимальная видимая площадь элементов в пикселях, учитываемая для VC и SI. По умолчанию 50. | Optional |

#### Объект `WebApplicationConfigIpAddressRestrictionSettings`

Настройки для ограничения определённых IP-адресов и для ввода маски подсети. Также ограничивают режим.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange[]](#openapi-definition-IpAddressRange) | - | Optional |
| mode | string | Режим списка ограничений IP-адресов. Возможные значения: * `EXCLUDE` * `INCLUDE` | Required |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов, сопоставляемый с локацией.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| address | string | Сопоставляемый IP-адрес.  Для диапазона IP-адресов это адрес **from**. | Required |
| addressTo | string | Адрес **to** диапазона IP-адресов. | Optional |
| subnetMask | integer | Маска подсети диапазона IP-адресов. | Optional |

#### Объект `JavaScriptFrameworkSupport`

Поддержка различных JavaScript-фреймворков.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| activeXObject | boolean | Поддержка обнаружения ActiveXObject включена/отключена. | Required |
| angular | boolean | Поддержка AngularJS и Angular включена/отключена. | Required |
| dojo | boolean | Поддержка Dojo включена/отключена. | Required |
| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/отключена. | Required |
| icefaces | boolean | Поддержка ICEfaces включена/отключена. | Required |
| jQuery | boolean | Поддержка jQuery, Backbone.js включена/отключена. | Required |
| mooTools | boolean | Поддержка MooTools включена/отключена. | Required |
| prototype | boolean | Поддержка Prototype включена/отключена. | Required |

#### Объект `JavaScriptInjectionRules`

Правила внедрения JavaScript

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| enabled | boolean | Правило включения или отключения внедрения JavaScript. | Required |
| htmlPattern | string | HTML-шаблон внедрения JavaScript. | Optional |
| rule | string | Правило URL внедрения JavaScript. Возможные значения: * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` | Required |
| target | string | Цель, по которой сопоставляется правило внедрения JavaScript. Возможные значения: * `PAGE_QUERY` * `URL` | Optional |
| urlOperator | string | URL-оператор внедрения JavaScript. Возможные значения: * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Required |
| urlPattern | string | URL-шаблон внедрения JavaScript. | Optional |

#### Объект `SessionReplaySetting`

Настройки Session Replay

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| costControlPercentage | integer | Частота сэмплирования Session Replay в процентах. | Required |
| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата CSS-ресурсов. | Optional |
| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) CSS-ресурсы из сессии. | Optional |
| enabled | boolean | Session Replay включён. | Required |

#### Объект `UserActionAndSessionProperties`

Определяет настройки пользовательски заданных свойств пользовательских действий и сессий приложения.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Возможные значения: * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Optional |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение](https://dt-url.net/k9e0iaq) для нужных вам данных. | Optional |
| displayName | string | Отображаемое имя свойства. | Optional |
| ignoreCase | boolean | Если true, значение этого свойства всегда сохраняется в нижнем регистре. По умолчанию false. | Optional |
| key | string | Ключ свойства | Required |
| longStringLength | integer | Если тип LONG\_STRING, максимальная длина для этого свойства. Должна быть кратна 100. По умолчанию 200. | Optional |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig.Должна быть задана, если "origin" имеет тип META\_DATA. | Optional |
| origin | string | Источник свойства Возможные значения: * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Required |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Optional |
| storeAsSessionProperty | boolean | Если `true`, свойство хранится как свойство сессии | Optional |
| storeAsUserActionProperty | boolean | Если `true`, свойство хранится как свойство пользовательского действия | Optional |
| type | string | Тип данных свойства. Возможные значения: * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` | Required |
| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения | Required |

#### Объект `UserActionNamingSettings`

Настройки именования пользовательских действий.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для пользовательских действий. | Optional |
| ignoreCase | boolean | Именование без учёта регистра. | Optional |
| loadActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для действий загрузки. | Optional |
| placeholders | [UserActionNamingPlaceholder[]](#openapi-definition-UserActionNamingPlaceholder) | Плейсхолдеры пользовательских действий. | Optional |
| queryParameterCleanups | string[] | Список параметров, которые нужно удалить из запроса перед использованием запроса в имени пользовательского действия. | Optional |
| splitUserActionsByDomain | boolean | Отключите эту настройку, если разные домены не должны приводить к отдельным пользовательским действиям. | Optional |
| useFirstDetectedLoadAction | boolean | Если true, используется первое действие загрузки, найденное под XHR-действием. Иначе используется самое глубокое под XHR-действием | Optional |
| xhrActionNamingRules | [UserActionNamingRule[]](#openapi-definition-UserActionNamingRule) | Правила именования пользовательских действий для XHR-действий. | Optional |

#### Объект `UserActionNamingRule`

Настройки правила именования.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| conditions | [UserActionNamingRuleCondition[]](#openapi-definition-UserActionNamingRuleCondition) | Определяет условия, при которых должно применяться правило именования. | Optional |
| template | string | Шаблон именования. Используйте фигурные скобки `{}` для выбора плейсхолдеров. | Required |
| useOrConditions | boolean | Если установлено `true`, условия соединяются логическим OR вместо логического AND. | Optional |

#### Объект `UserActionNamingRuleCondition`

Настройки условий именования пользовательских действий.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| operand1 | string | Должен быть определённым плейсхолдером в фигурных скобках | Required |
| operand2 | string | Должен быть null, если оператор "IS\_EMPTY", регулярным выражением, если оператор "MATCHES\_REGULAR\_ERPRESSION". Во всех остальных случаях значение может быть произвольным текстом или плейсхолдером в фигурных скобках | Optional |
| operator | string | Оператор условия Возможные значения: * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` | Required |

#### Объект `UserActionNamingPlaceholder`

Настройки плейсхолдера.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| input | string | Ввод. Возможные значения: * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` | Required |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если "Input" имеет тип METADATA. | Optional |
| name | string | Имя плейсхолдера. | Required |
| processingPart | string | Часть. Возможные значения: * `ALL` * `ANCHOR` * `PATH` | Required |
| processingSteps | [UserActionNamingPlaceholderProcessingStep[]](#openapi-definition-UserActionNamingPlaceholderProcessingStep) | Действия обработки. | Optional |
| useGuessedElementIdentifier | boolean | Использовать идентификатор элемента, выбранный Dynatrace. | Required |

#### Объект `UserActionNamingPlaceholderProcessingStep`

Настройки шага обработки.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| fallbackToInput | boolean | Если установлено true: возвращает ввод, если **patternBefore** или **patternAfter** не найдены и **type** равен `SUBSTRING`.  Возвращает ввод, если **regularExpression** не совпадает и **type** равен `EXTRACT_BY_REGULAR_EXPRESSION`.  Иначе возвращается null. | Optional |
| patternAfter | string | Шаблон после нужного значения. Он будет удалён. | Optional |
| patternAfterSearchType | string | Нужное вхождение **patternAfter**. Возможные значения: * `FIRST` * `LAST` | Optional |
| patternBefore | string | Шаблон перед нужным значением. Он будет удалён. | Optional |
| patternBeforeSearchType | string | Нужное вхождение **patternBefore**. Возможные значения: * `FIRST` * `LAST` | Optional |
| patternToReplace | string | Заменяемый шаблон.  Применимо только если **type** равен `REPLACE_WITH_PATTERN`. | Optional |
| regularExpression | string | Регулярное выражение для извлекаемой или заменяемой строки.  Применимо только если **type** равен `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. | Optional |
| replacement | string | Замена для исходного значения. | Optional |
| type | string | Действие, выполняемое при обработке:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанную **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанную **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, соответствующую **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, соответствующие **regularExpression**, на указанную **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанную **replacement**. Возможные значения: * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` | Required |

#### Объект `UserTag`

Определяет настройки UserTags приложения.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| cleanupRule | string | Выражение правила очистки userTag | Optional |
| ignoreCase | boolean | Если true, значение этого тега всегда сохраняется в нижнем регистре. По умолчанию false. | Optional |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если UserTag основан на метаданных, захваченных JavaScript-агентом (например, переменная JavaScript, CSS-селектор и т. д.) | Optional |
| serverSideRequestAttribute | string | ID серверного атрибута запроса userTag. Должен быть задан, если UserTag основан на серверном атрибуте запроса. | Optional |
| uniqueId | integer | uniqueId, уникальный среди всех userTags и свойств этого приложения | Required |

#### The `WaterfallSettings` object

Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов.

| Элемент | Тип | Описание | Required |
| --- | --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с более низкой частотой кэширования браузером выше *X*%. | Required |
| resourcesThreshold | integer | Предупреждать о ресурсах больше *X* байт. | Required |
| slowCdnResourcesThreshold | integer | Предупреждать о медленных CDN-ресурсах со временем отклика выше *X* мс. | Required |
| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных собственных ресурсах со временем отклика выше *X* мс. | Required |
| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных сторонних ресурсах со временем отклика выше *X* мс. | Required |
| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X* % от Visually complete. | Required |
| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах больше *X* байт. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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