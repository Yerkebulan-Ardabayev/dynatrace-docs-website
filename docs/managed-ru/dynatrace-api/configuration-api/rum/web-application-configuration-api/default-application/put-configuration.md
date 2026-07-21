---
title: Web application configuration API - PUT default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration
---

# Web application configuration API - PUT default application

# Web application configuration API - PUT default application

* Справочник
* Опубликовано 03 сен. 2019 г.

Обновляет веб-приложение по умолчанию в среде Dynatrace.

Запрос принимает содержимое `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | Тело JSON запроса, содержащее новые параметры веб-приложения по умолчанию. | body | Нет |

### Объекты тела запроса


#### Объект `WebApplicationConfig`


Конфигурация веб-приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conversionGoals | [ConversionGoal](#openapi-definition-ConversionGoal)[] | Список целей конверсии приложения. | Опционально |
| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. | Обязательно |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex для приложения. | Обязательно |
| identifier | string | Dynatrace ID сущности веб-приложения. | Опционально |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex для приложения. | Обязательно |
| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности для load actions. Элемент может принимать следующие значения * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` | Обязательно |
| metaDataCaptureSettings | [MetaDataCapturing](#openapi-definition-MetaDataCapturing)[] | Настройки захвата метаданных JavaScript-агентом. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки мониторинга реальных пользователей. | Обязательно |
| name | string | Имя веб-приложения, отображаемое в UI. | Обязательно |
| realUserMonitoringEnabled | boolean | Мониторинг реальных пользователей включен/выключен. | Обязательно |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки session replay | Опционально |
| type | string | Тип веб-приложения. Элемент может принимать следующие значения * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` | Опционально |
| urlInjectionPattern | string | Шаблон внедрения URL для веб-приложения с ручной установкой. | Опционально |
| userActionAndSessionProperties | [UserActionAndSessionProperties](#openapi-definition-UserActionAndSessionProperties)[] | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений | Опционально |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. | Опционально |
| userTags | [UserTag](#openapi-definition-UserTag)[] | Настройки пользовательских тегов. | Опционально |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, получаемые для сторонних, CDN и собственных ресурсов. | Обязательно |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex для приложения. | Обязательно |
| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности для XHR actions. Элемент может принимать следующие значения * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` | Обязательно |


#### Объект `ConversionGoal`


Цель конверсии приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. | Опционально |
| id | string | ID цели конверсии. При создании новой цели конверсии его нужно опустить. | Опционально |
| name | string | Имя цели конверсии. | Обязательно |
| type | string | Тип цели конверсии. Элемент может принимать следующие значения * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` | Опционально |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. | Опционально |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. | Опционально |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе количества пользовательских действий. | Опционально |


#### Объект `DestinationDetails`


Конфигурация цели конверсии на основе назначения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| caseSensitive | boolean | Совпадение чувствительно к регистру (`true`) или нет (`false`). | Опционально |
| matchType | string | Оператор сравнения. Элемент может принимать следующие значения * `Begins` * `Contains` * `Ends` | Опционально |
| urlOrPath | string | Путь, который нужно достичь для выполнения цели конверсии. | Обязательно |


#### Объект `UserActionDetails`


Конфигурация цели конверсии на основе пользовательского действия.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionType | string | Тип действия, к которому применяется правило. Элемент может принимать следующие значения * `Custom` * `Load` * `Xhr` | Опционально |
| caseSensitive | boolean | Совпадение чувствительно к регистру (`true`) или нет (`false`). | Опционально |
| matchEntity | string | Тип сущности, к которой применяется правило. Элемент может принимать следующие значения * `ActionName` * `PageUrl` | Опционально |
| matchType | string | Оператор сравнения. Элемент может принимать следующие значения * `Begins` * `Contains` * `Ends` | Опционально |
| value | string | Значение, которое должно совпасть для выполнения цели конверсии. | Опционально |


#### Объект `VisitDurationDetails`


Конфигурация цели конверсии на основе длительности визита.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| durationInMillis | integer | Длительность сессии для выполнения цели конверсии, в миллисекундах. | Обязательно |


#### Объект `VisitNumActionDetails`


Конфигурация цели конверсии на основе количества пользовательских действий.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| numUserActions | integer | Количество пользовательских действий для выполнения цели конверсии. | Опционально |


#### Объект `Apdex`


Определяет настройки Apdex для приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| frustratingFallbackThreshold | number | Резервный порог XHR action, определяющий терпимый пользовательский опыт, когда настроенный KPM недоступен. | Опционально |
| frustratingThreshold | number | Максимальное значение apdex, которое считается терпимым пользовательским опытом. | Опционально |
| toleratedFallbackThreshold | number | Резервный порог XHR action, определяющий удовлетворительный пользовательский опыт, когда настроенный KPM недоступен. | Опционально |
| toleratedThreshold | number | Максимальное значение apdex, которое считается удовлетворительным пользовательским опытом. | Опционально |


#### Объект `MetaDataCapturing`


Конфигурация захвата метаданных с помощью Javascript-агента. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capturingName | string | Имя метаданных для захвата. | Обязательно |
| name | string | Имя для отображения захваченных значений в Dynatrace. | Обязательно |
| publicMetadata | boolean | True, если эти метаданные нужно захватывать независимо от настроек приватности | Опционально |
| type | string | Тип метаданных для захвата. Элемент может принимать следующие значения * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` | Обязательно |
| uniqueId | integer | Уникальный ID метаданных для захвата. | Опционально |
| useLastValue | boolean | True, если для этих метаданных нужно использовать последнее захваченное значение. По умолчанию используется первое значение. | Опционально |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |


#### Объект `MonitoringSettings`


Настройки мониторинга реальных пользователей.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Добавляет атрибут cross origin = anonymous для перехвата сообщений об ошибках JavaScript и таймингов ресурсов W3C. | Опционально |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Дополнительные настройки JavaScript-тега. | Обязательно |
| angularPackageName | string | Имя пакета angular. | Опционально |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивает режим. | Опционально |
| cacheControlHeaderOptimizations | boolean | Оптимизирует значение заголовков cache control для использования с Dynatrace real user monitoring, включено/выключено. | Обязательно |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки для захвата контента. | Обязательно |
| cookiePlacementDomain | string | Домен для размещения cookie. | Опционально |
| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, нужно задать регулярное выражение, соответствующее этим вызовам, тогда Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим эндпоинтам в AWS.  Важно: эти эндпоинты должны принимать заголовок x-dtc, иначе запросы завершатся ошибкой. | Опционально |
| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для приложения. Для этого нужно указать пары key=value, разделённые символом (|). | Обязательно |
| excludeXhrRegex | string | Некоторые действия можно исключить из становления XHR-действиями.  Здесь нужно указать регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. | Обязательно |
| fetchRequests | boolean | Захват запросов `fetch()`, включено/выключено. | Обязательно |
| injectionMode | string | Режим внедрения JavaScript. Элемент может принимать следующие значения * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` | Обязательно |
| instrumentedWebServer | boolean | Инструментированный веб- или app-сервер. | Опционально |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки для ограничения определённых IP-адресов и введения маски подсети. Также ограничивает режим. | Опционально |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. | Обязательно |
| javaScriptInjectionRules | [JavaScriptInjectionRules](#openapi-definition-JavaScriptInjectionRules)[] | Правила внедрения JavaScript. | Опционально |
| libraryFileFromCdn | boolean | Получать файл библиотеки JavaScript из CDN.  Не поддерживается agentless-приложениями, а для приложений с авто-внедрением при отсутствии значения принимается как false. | Опционально |
| libraryFileLocation | string | Расположение пользовательского файла библиотеки JavaScript приложения.  Если ничего не указано, используется корневой каталог веб-сервера.  **Обязательно** для приложений с авто-внедрением, не поддерживается agentless-приложениями. | Опционально |
| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Нужно указать относительный или абсолютный URL. При использовании абсолютного URL данные отправляются через CORS.  **Обязательно** для приложений с авто-внедрением, опционально для agentless-приложений. | Опционально |
| sameSiteCookieAttribute | string | Атрибут same site cookie. Элемент может принимать следующие значения * `LAX` * `NONE` * `STRICT` | Опционально |
| scriptTagCacheDurationInHours | integer | Продолжительность для настроек кэширования. | Опционально |
| secureCookieAttribute | boolean | Использование атрибута secure для cookie Dynatrace, включено/выключено. | Обязательно |
| serverRequestPathId | string | Путь для идентификации ID запроса сервера. | Обязательно |
| useCors | boolean | Отправлять данные beacon через CORS. | Опционально |
| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest`, включена/выключена. | Обязательно |


#### Объект `AdvancedJavaScriptTagSettings`


Дополнительные настройки JavaScript-тега.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики событий и обёртки. | Обязательно |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | В дополнение к обработчикам событий можно захватывать события, вызванные через `addEventListener` или `attachEvent`. С этой опцией нужно быть осторожным! Обёртки событий могут конфликтовать с JavaScript-кодом веб-страницы. | Обязательно |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. | Обязательно |
| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков, включено/выключено. | Обязательно |
| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения от 5 до 10000. | Обязательно |
| maxErrorsToCapture | integer | Максимальное количество ошибок для захвата на странице. Допустимые значения от 0 до 50. | Обязательно |
| proxyWrapperEnabled | boolean | Прокси-обёртка, включена/выключена. | Опционально |
| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать буквенно-цифровыми символами в формате HTML escape. | Обязательно |
| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest в Firefox, включено/выключено. | Опционально |
| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest в Internet Explorer, включено/выключено. | Опционально |
| userActionNameAttribute | string | Атрибут имени пользовательского действия. | Опционально |


#### Объект `AdditionalEventHandlers`


Дополнительные обработчики событий и обёртки.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| blurEventHandler | boolean | Обработчик события blur, включён/выключен. | Обязательно |
| changeEventHandler | boolean | Обработчик события change, включён/выключен. | Обязательно |
| clickEventHandler | boolean | Обработчик события click, включён/выключен. | Обязательно |
| maxDomNodesToInstrument | integer | Макс. количество DOM-узлов для инструментирования. Допустимые значения от 0 до 100000. | Обязательно |
| mouseupEventHandler | boolean | Обработчик события mouseup, включён/выключен. | Обязательно |
| toStringMethod | boolean | Метод toString, включён/выключен. | Обязательно |
| userMouseupEventForClicks | boolean | Использование события mouseup для кликов, включено/выключено. | Обязательно |


#### Объект `EventWrapperSettings`


В дополнение к обработчикам событий можно захватывать события, вызванные через `addEventListener` или `attachEvent`. С этой опцией нужно быть осторожным! Обёртки событий могут конфликтовать с JavaScript-кодом веб-страницы.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| blur | boolean | Blur, включён/выключен. | Обязательно |
| change | boolean | Change, включён/выключен. | Обязательно |
| click | boolean | Click, включён/выключен. | Обязательно |
| mouseUp | boolean | MouseUp, включён/выключен. | Обязательно |
| touchEnd | boolean | TouchEnd, включён/выключен. | Обязательно |
| touchStart | boolean | TouchStart, включён/выключен. | Обязательно |


#### Объект `GlobalEventCaptureSettings`


Настройки глобального захвата событий.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Дополнительные события для глобального захвата как пользовательский ввод.  Например, DragStart или DragEnd. | Обязательно |
| change | boolean | Change, включён/выключен. | Опционально |
| click | boolean | Click, включён/выключен. | Обязательно |
| doubleClick | boolean | DoubleClick, включён/выключен. | Обязательно |
| keyDown | boolean | KeyDown, включён/выключен. | Обязательно |
| keyUp | boolean | KeyUp, включён/выключен. | Обязательно |
| mouseDown | boolean | MouseDown, включён/выключен. | Обязательно |
| mouseUp | boolean | MouseUp, включён/выключен. | Обязательно |
| scroll | boolean | Scroll, включён/выключен. | Обязательно |
| touchEnd | boolean | TouchEnd, включён/выключен. | Опционально |
| touchStart | boolean | TouchStart, включён/выключен. | Опционально |


#### Объект `WebApplicationConfigBrowserRestrictionSettings`


Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивает режим.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction](#openapi-definition-WebApplicationConfigBrowserRestriction)[] | Список ограничений браузера. | Опционально |
| mode | string | Режим списка ограничений браузера. Элемент может принимать следующие значения * `EXCLUDE` * `INCLUDE` | Обязательно |


#### Объект `WebApplicationConfigBrowserRestriction`


Правила исключения браузеров для тех браузеров, которые нужно исключить.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| browserType | string | Тип используемого браузера. Элемент может принимать следующие значения * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` | Обязательно |
| browserVersion | string | Версия используемого браузера. | Опционально |
| comparator | string | Сравнивает разные браузеры между собой. Элемент может принимать следующие значения * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` | Опционально |
| platform | string | Платформа, на которой используется браузер. Элемент может принимать следующие значения * `ALL` * `DESKTOP` * `MOBILE` | Опционально |


#### Объект `ContentCapture`


Настройки для захвата контента.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| javaScriptErrors | boolean | Мониторинг JavaScript-ошибок включён/выключен. | Обязательный |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки для захвата resource timings. | Обязательный |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки для захвата timed action. | Обязательный |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки для VisuallyComplete2 | Опциональный |
| visuallyCompleteAndSpeedIndex | boolean | Поддержка visually complete и speed index включена/выключена. | Обязательный |


#### Объект `ResourceTimingSettings`


Настройки для захвата resource timings.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| nonW3cResourceTimings | boolean | Тайминг для JavaScript-файлов и изображений в браузерах без поддержки W3C включён/выключен. | Обязательный |
| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и изображений в браузерах, не предоставляющих W3C resource timings. Допустимые значения от 0 до 9999. Действует, только если включён параметр **nonW3cResourceTimings**. | Обязательный |
| resourceTimingCaptureType | string | Определяет, насколько подробно захватываются resource timings. Действует, только если включён **w3cResourceTimings** или **nonW3cResourceTimings**. Элемент может принимать следующие значения: * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` | Опциональный |
| resourceTimingsDomainLimit | integer | Ограничивает число доменов, для которых захватываются W3C resource timings. Действует, только если **resourceTimingCaptureType** имеет значение `CAPTURE_LIMITED_SUMMARIES`. | Опциональный |
| w3cResourceTimings | boolean | W3C resource timings для стороннего контента/CDN включены/выключены. | Обязательный |


#### Объект `TimeoutSettings`


Настройки для захвата timed action.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Определяет, насколько глубоко могут каскадироваться временные actions. 0 полностью отключает временные actions. Рекомендуемое значение при включении, 3. | Обязательный |
| temporaryActionTotalTimeout | integer | Общий таймаут всех каскадных таймаутов, при котором ещё должна быть возможность создать временный action | Обязательный |
| timedActionSupport | boolean | Поддержка timed action включена/выключена. Включить для обнаружения actions, инициирующих отправку XHR через методы *setTimout*. | Обязательный |


#### Объект `VisuallyComplete2Settings`


Настройки для VisuallyComplete2


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. | Опциональный |
| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при вычислении VC и SI | Опциональный |
| inactivityTimeout | integer | Время в мс, в течение которого модуль VC ожидает отсутствия мутаций на странице после load action. По умолчанию 1000. | Опциональный |
| mutationTimeout | integer | Определяет время в мс, в течение которого VC ждёт после закрытия action, прежде чем начать вычисление. По умолчанию 50. | Опциональный |
| threshold | integer | Минимальная видимая область в пикселях для элементов, учитываемых при подсчёте VC и SI. По умолчанию 50. | Опциональный |


#### Объект `WebApplicationConfigIpAddressRestrictionSettings`


Настройки для ограничения определённых IP-адресов и указания маски подсети. Также определяет режим.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange](#openapi-definition-IpAddressRange)[] | - | Опциональный |
| mode | string | Режим списка ограничений по IP-адресам. Элемент может принимать следующие значения: * `EXCLUDE` * `INCLUDE` | Обязательный |


#### Объект `IpAddressRange`


IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| address | string | IP-адрес, который нужно сопоставить. Для диапазона IP-адресов это начальный адрес (**from**). | Обязательный |
| addressTo | string | Конечный адрес (**to**) диапазона IP-адресов. | Опциональный |
| subnetMask | integer | Маска подсети диапазона IP-адресов. | Опциональный |


#### Объект `JavaScriptFrameworkSupport`


Поддержка различных JavaScript-фреймворков.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| activeXObject | boolean | Поддержка обнаружения ActiveXObject включена/выключена. | Обязательный |
| angular | boolean | Поддержка AngularJS и Angular включена/выключена. | Обязательный |
| dojo | boolean | Поддержка Dojo включена/выключена. | Обязательный |
| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/выключена. | Обязательный |
| icefaces | boolean | Поддержка ICEfaces включена/выключена. | Обязательный |
| jQuery | boolean | Поддержка jQuery, Backbone.js включена/выключена. | Обязательный |
| mooTools | boolean | Поддержка MooTools включена/выключена. | Обязательный |
| prototype | boolean | Поддержка Prototype включена/выключена. | Обязательный |


#### Объект `JavaScriptInjectionRules`


Правила для внедрения javascript


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Правило включения или отключения внедрения java script. | Обязательный |
| htmlPattern | string | HTML-паттерн внедрения java script. | Опциональный |
| rule | string | Правило url для внедрения java script. Элемент может принимать следующие значения: * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` | Обязательный |
| target | string | Цель, с которой должно сопоставляться правило внедрения java script. Элемент может принимать следующие значения: * `PAGE_QUERY` * `URL` | Опциональный |
| urlOperator | string | Оператор url для внедрения java script. Элемент может принимать следующие значения: * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Обязательный |
| urlPattern | string | URL-паттерн внедрения java script. | Опциональный |


#### Объект `SessionReplaySetting`


Настройки session replay


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| costControlPercentage | integer | Ставка сэмплирования session replay в процентах. | Обязательный |
| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата CSS-ресурсов. | Опциональный |
| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) CSS-ресурсы сессии. | Опциональный |
| enabled | boolean | SessionReplay включён. | Обязательный |


#### Объект `UserActionAndSessionProperties`


Определяет настройки пользовательских свойств userAction и session, заданных для приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства. Определяет, как агрегируются несколько значений свойства. Элемент может принимать следующие значения: * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Опциональный |
| cleanupRule | string | Правило очистки свойства. Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для нужных данных. | Опциональный |
| displayName | string | Отображаемое имя свойства. | Опциональный |
| ignoreCase | boolean | Если true, значение этого свойства всегда будет сохраняться в нижнем регистре. По умолчанию false. | Опциональный |
| key | string | Ключ свойства | Обязательный |
| longStringLength | integer | Если тип LONG\_STRING, максимальная длина для этого свойства. Должна быть кратна 100. По умолчанию 200. | Опциональный |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должна быть задана, если "origin" имеет тип META\_DATA. | Опциональный |
| origin | string | Источник свойства. Элемент может принимать следующие значения: * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Обязательный |
| serverSideRequestAttribute | string | ID атрибута запроса. Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Опциональный |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство сессии | Опциональный |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство user action | Опциональный |
| type | string | Тип данных свойства. Элемент может принимать следующие значения: * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` | Обязательный |
| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения | Обязательный |


#### Объект `UserActionNamingSettings`


Настройки именования user action.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования user action для custom actions. | Опциональный |
| ignoreCase | boolean | Именование без учёта регистра. | Опциональный |
| loadActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования user action для loading actions. | Опциональный |
| placeholders | [UserActionNamingPlaceholder](#openapi-definition-UserActionNamingPlaceholder)[] | Плейсхолдеры для именования user action. | Опциональный |
| queryParameterCleanups | string[] | Список параметров, которые нужно удалить из query перед использованием query в имени user action. | Опциональный |
| splitUserActionsByDomain | boolean | Отключить эту настройку, если разные домены не должны приводить к отдельным user action. | Опциональный |
| useFirstDetectedLoadAction | boolean | Если true, используется первый найденный load action под XHR action. Иначе используется самый глубокий из них под xhr action | Опциональный |
| xhrActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования user action для xhr actions. | Опциональный |


#### Объект `UserActionNamingRule`


Настройки правила именования.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| conditions | [UserActionNamingRuleCondition](#openapi-definition-UserActionNamingRuleCondition)[] | Определяет условия применения правила именования. | Опционально |
| template | string | Шаблон именования. Фигурные скобки `{}` используются для выбора плейсхолдеров. | Обязательно |
| useOrConditions | boolean | Если задано значение `true`, условия объединяются логическим ИЛИ вместо логического И. | Опционально |


#### Объект `UserActionNamingRuleCondition`


Настройки условий для именования пользовательских действий.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| operand1 | string | Должен быть определённым плейсхолдером в фигурных скобках | Обязательно |
| operand2 | string | Должен быть null, если оператор "IS\_EMPTY", регулярным выражением, если оператор "MATCHES\_REGULAR\_ERPRESSION". Во всех остальных случаях значением может быть произвольный текст или плейсхолдер в фигурных скобках | Опционально |
| operator | string | Оператор условия. Элемент может принимать следующие значения * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` | Обязательно |


#### Объект `UserActionNamingPlaceholder`


Настройки плейсхолдера.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| input | string | Входные данные. Элемент может принимать следующие значения * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` | Обязательно |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должно быть задано, если "Input" имеет тип METADATA. | Опционально |
| name | string | Название плейсхолдера. | Обязательно |
| processingPart | string | Часть. Элемент может принимать следующие значения * `ALL` * `ANCHOR` * `PATH` | Обязательно |
| processingSteps | [UserActionNamingPlaceholderProcessingStep](#openapi-definition-UserActionNamingPlaceholderProcessingStep)[] | Действия обработки. | Опционально |
| useGuessedElementIdentifier | boolean | Использовать идентификатор элемента, выбранный Dynatrace. | Обязательно |


#### Объект `UserActionNamingPlaceholderProcessingStep`


Настройки шага обработки.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| fallbackToInput | boolean | Если задано значение true: возвращает входное значение, если **patternBefore** или **patternAfter** не найдены и **type** имеет значение `SUBSTRING`.  Возвращает входное значение, если **regularExpression** не совпадает и **type** имеет значение `EXTRACT_BY_REGULAR_EXPRESSION`.  В остальных случаях возвращается null. | Опционально |
| patternAfter | string | Паттерн после нужного значения. Будет удалён. | Опционально |
| patternAfterSearchType | string | Требуемое вхождение **patternAfter**. Элемент может принимать следующие значения * `FIRST` * `LAST` | Опционально |
| patternBefore | string | Паттерн перед нужным значением. Будет удалён. | Опционально |
| patternBeforeSearchType | string | Требуемое вхождение **patternBefore**. Элемент может принимать следующие значения * `FIRST` * `LAST` | Опционально |
| patternToReplace | string | Паттерн для замены.  Применимо, только если **type** имеет значение `REPLACE_WITH_PATTERN`. | Опционально |
| regularExpression | string | Регулярное выражение для извлекаемой или заменяемой строки.  Применимо, только если **type** имеет значение `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. | Опционально |
| replacement | string | Замена для исходного значения. | Опционально |
| type | string | Действие, выполняемое обработкой:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанное значение **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанное значение **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, соответствующую **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, соответствующие **regularExpression**, на указанное значение **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанное значение **replacement**. Элемент может принимать следующие значения * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` | Обязательно |


#### Объект `UserTag`


Определяет настройки UserTags приложения.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| cleanupRule | string | Выражение правила очистки userTag | Опционально |
| ignoreCase | boolean | Если true, значение этого тега всегда сохраняется в нижнем регистре. По умолчанию false. | Опционально |
| metadataId | integer | Ссылка на uniqueId объекта MetadataCapturingConfig. Должно быть задано, если UserTag основан на метаданных, захваченных Javascript-агентом (например, переменная Javascript, CSS-селектор и т. д.) | Опционально |
| serverSideRequestAttribute | string | Идентификатор серверного атрибута запроса userTag. Должен быть задан, если UserTag основан на серверном атрибуте запроса. | Опционально |
| uniqueId | integer | uniqueId, уникальный среди всех userTags и свойств данного приложения | Обязательно |


#### Объект `WaterfallSettings`


Эти настройки влияют на данные мониторинга, которые вы получаете для сторонних, CDN и собственных ресурсов.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с более низкой долей кеширования браузером выше *X*%. | Обязательно |
| resourcesThreshold | integer | Предупреждать о ресурсах размером более *X* байт. | Обязательно |
| slowCdnResourcesThreshold | integer | Предупреждать о медленных CDN-ресурсах со временем отклика выше *X* мс. | Обязательно |
| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных собственных ресурсах со временем отклика выше *X* мс. | Обязательно |
| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных сторонних ресурсах со временем отклика выше *X* мс. | Обязательно |
| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X*% от Visually complete. | Обязательно |
| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах размером более *X* байт. | Обязательно |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой в реальном запросе. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
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