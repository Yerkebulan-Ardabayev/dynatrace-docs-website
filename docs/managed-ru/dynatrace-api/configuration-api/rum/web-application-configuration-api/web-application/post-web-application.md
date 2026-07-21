---
title: Web application configuration API - POST a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application
---

# Web application configuration API - POST a web application

# Web application configuration API - POST a web application

* Справка
* Обновлено 18 авг. 2025 г.

Создаёт новое веб-приложение.

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON тело запроса, содержащее параметры конфигурации нового веб-приложения. | body | Необязательный |

### Объекты тела запроса


#### Объект `WebApplicationConfig`


Конфигурация веб-приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conversionGoals | [ConversionGoal](#openapi-definition-ConversionGoal)[] | Список целей конверсии приложения. | Опционально |
| costControlUserSessionPercentage | number | Анализировать *X*% пользовательских сессий. | Обязательно |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Обязательно |
| identifier | string | Dynatrace ID сущности веб-приложения. | Опционально |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Обязательно |
| loadActionKeyPerformanceMetric | string | Ключевая метрика производительности load-действий. Элемент может принимать следующие значения * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` | Обязательно |
| metaDataCaptureSettings | [MetaDataCapturing](#openapi-definition-MetaDataCapturing)[] | Настройки захвата метаданных Java script агента. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Настройки Real User Monitoring. | Обязательно |
| name | string | Имя веб-приложения, отображаемое в UI. | Обязательно |
| realUserMonitoringEnabled | boolean | Real User Monitoring включен/выключен. | Обязательно |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Настройки session replay | Опционально |
| type | string | Тип веб-приложения. Элемент может принимать следующие значения * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` | Опционально |
| urlInjectionPattern | string | Паттерн внедрения URL для веб-приложения с ручным внедрением. | Опционально |
| userActionAndSessionProperties | [UserActionAndSessionProperties](#openapi-definition-UserActionAndSessionProperties)[] | Настройки свойств пользовательских действий и сессий. Пустой список означает отсутствие изменений | Опционально |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | Настройки именования пользовательских действий. | Опционально |
| userTags | [UserTag](#openapi-definition-UserTag)[] | Настройки пользовательских тегов. | Опционально |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | Эти настройки влияют на данные мониторинга, получаемые для ресурсов сторонних поставщиков, CDN и собственных ресурсов. | Обязательно |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Определяет настройки Apdex приложения. | Обязательно |
| xhrActionKeyPerformanceMetric | string | Ключевая метрика производительности XHR-действий. Элемент может принимать следующие значения * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` | Обязательно |


#### Объект `ConversionGoal`


Цель конверсии приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Конфигурация цели конверсии на основе назначения. | Опционально |
| id | string | ID цели конверсии.  Не указывать при создании новой цели конверсии. | Опционально |
| name | string | Имя цели конверсии. | Обязательно |
| type | string | Тип цели конверсии. Элемент может принимать следующие значения * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` | Опционально |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Конфигурация цели конверсии на основе пользовательского действия. | Опционально |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Конфигурация цели конверсии на основе длительности визита. | Опционально |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Конфигурация цели конверсии на основе количества пользовательских действий. | Опционально |


#### Объект `DestinationDetails`


Конфигурация цели конверсии на основе назначения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| caseSensitive | boolean | Совпадение чувствительно (`true`) или нечувствительно (`false`) к регистру. | Опционально |
| matchType | string | Оператор совпадения. Элемент может принимать следующие значения * `Begins` * `Contains` * `Ends` | Опционально |
| urlOrPath | string | Путь, который нужно достичь для срабатывания цели конверсии. | Обязательно |


#### Объект `UserActionDetails`


Конфигурация цели конверсии на основе пользовательского действия.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionType | string | Тип действия, к которому применяется правило. Элемент может принимать следующие значения * `Custom` * `Load` * `Xhr` | Опционально |
| caseSensitive | boolean | Совпадение чувствительно (`true`) или нечувствительно (`false`) к регистру. | Опционально |
| matchEntity | string | Тип сущности, к которой применяется правило. Элемент может принимать следующие значения * `ActionName` * `PageUrl` | Опционально |
| matchType | string | Оператор совпадения. Элемент может принимать следующие значения * `Begins` * `Contains` * `Ends` | Опционально |
| value | string | Значение, которое должно совпасть для срабатывания цели конверсии. | Опционально |


#### Объект `VisitDurationDetails`


Конфигурация цели конверсии на основе длительности визита.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| durationInMillis | integer | Длительность сессии для срабатывания цели конверсии, в миллисекундах. | Обязательно |


#### Объект `VisitNumActionDetails`


Конфигурация цели конверсии на основе количества пользовательских действий.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| numUserActions | integer | Количество пользовательских действий для срабатывания цели конверсии. | Опционально |


#### Объект `Apdex`


Определяет настройки Apdex приложения.


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| frustratingFallbackThreshold | number | Резервный порог XHR-действия, определяющий терпимый пользовательский опыт, когда настроенный KPM недоступен. | Опционально |
| frustratingThreshold | number | Максимальное значение apdex, которое считается терпимым пользовательским опытом. | Опционально |
| toleratedFallbackThreshold | number | Резервный порог XHR-действия, определяющий удовлетворительный пользовательский опыт, когда настроенный KPM недоступен. | Опционально |
| toleratedThreshold | number | Максимальное значение apdex, которое считается удовлетворительным пользовательским опытом. | Опционально |


#### Объект `MetaDataCapturing`


Конфигурация захвата метаданных с помощью Javascript агента. На захваченные метаданные можно ссылаться по их uniqueId в UserTags, UserActionAndSessionProperties или UserActionNamingPlaceholder


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capturingName | string | Имя метаданных для захвата. | Обязательно |
| name | string | Имя для отображения захваченных значений в Dynatrace. | Обязательно |
| publicMetadata | boolean | True, если эти метаданные должны захватываться независимо от настроек приватности | Опционально |
| type | string | Тип метаданных для захвата. Элемент может принимать следующие значения * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` | Обязательно |
| uniqueId | integer | Уникальный id метаданных для захвата. | Опционально |
| useLastValue | boolean | True, если для этих метаданных должно использоваться последнее захваченное значение. По умолчанию используется первое значение. | Опционально |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |


#### Объект `MonitoringSettings`


Настройки Real User Monitoring.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Добавляет атрибут cross origin = anonymous для захвата сообщений об ошибках JavaScript и W3C resource timings. | Optional |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Расширенные настройки JavaScript-тега. | Required |
| angularPackageName | string | Имя angular-пакета. | Optional |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивает режим. | Optional |
| cacheControlHeaderOptimizations | boolean | Оптимизирует значение заголовков cache control для использования с включённым/выключенным Dynatrace real user monitoring. | Required |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Настройки захвата содержимого. | Required |
| cookiePlacementDomain | string | Домен для размещения cookie. | Optional |
| correlationHeaderInclusionRegex | string | Чтобы включить RUM для XHR-вызовов к AWS Lambda, нужно задать регулярное выражение, соответствующее этим вызовам, тогда Dynatrace сможет автоматически добавлять пользовательский заголовок (x-dtc) к каждому такому запросу к соответствующим конечным точкам в AWS.  Важно: эти конечные точки должны принимать заголовок x-dtc, иначе запросы завершатся ошибкой. | Optional |
| customConfigurationProperties | string | Дополнительные свойства JavaScript-тега, специфичные для приложения. Для этого нужно указать пары key=value, разделённые символом (|). | Required |
| excludeXhrRegex | string | Можно исключить некоторые действия из превращения в XHR-действия.  Здесь нужно указать регулярное выражение, соответствующее всем нужным URL.  Если ничего не указано, функция отключена. | Required |
| fetchRequests | boolean | Захват запросов `fetch()` включён/выключен. | Required |
| injectionMode | string | Режим внедрения JavaScript. Элемент может принимать следующие значения * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` | Required |
| instrumentedWebServer | boolean | Инструментированный веб- или app-сервер. | Optional |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Настройки для ограничения определённых IP-адресов и для указания маски подсети. Также ограничивает режим. | Optional |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Поддержка различных JavaScript-фреймворков. | Required |
| javaScriptInjectionRules | [JavaScriptInjectionRules](#openapi-definition-JavaScriptInjectionRules)[] | Правила внедрения JavaScript. | Optional |
| libraryFileFromCdn | boolean | Получает файл JavaScript-библиотеки из CDN.  Не поддерживается для agentless-приложений и считается равным false для автоматически внедряемых приложений, если не указано. | Optional |
| libraryFileLocation | string | Расположение пользовательского файла JavaScript-библиотеки приложения.  Если ничего не указано, используется корневой каталог веб-сервера.  **Обязательно** для автоматически внедряемых приложений, не поддерживается для agentless-приложений. | Optional |
| monitoringDataPath | string | Расположение для отправки данных мониторинга из JavaScript-тега.  Нужно указать относительный или абсолютный URL. При использовании абсолютного URL данные отправляются через CORS.  **Обязательно** для автоматически внедряемых приложений, необязательно для agentless-приложений. | Optional |
| sameSiteCookieAttribute | string | Атрибут same site cookie. Элемент может принимать следующие значения * `LAX` * `NONE` * `STRICT` | Optional |
| scriptTagCacheDurationInHours | integer | Продолжительность для настроек кеширования. | Optional |
| secureCookieAttribute | boolean | Использование атрибута secure для cookie Dynatrace включено/выключено. | Required |
| serverRequestPathId | string | Путь для идентификации ID запроса сервера. | Required |
| useCors | boolean | Отправка данных beacon через CORS. | Optional |
| xmlHttpRequest | boolean | Поддержка `XmlHttpRequest` включена/выключена. | Required |


#### Объект `AdvancedJavaScriptTagSettings`


Расширенные настройки JavaScript-тега.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Дополнительные обработчики событий и обёртки. | Required |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | Помимо обработчиков событий, можно захватывать события, вызванные через `addEventListener` или `attachEvent`. С этой опцией нужно быть осторожным! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице. | Required |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Настройки глобального захвата событий. | Required |
| instrumentUnsupportedAjaxFrameworks | boolean | Инструментирование неподдерживаемых Ajax-фреймворков включено/выключено. | Required |
| maxActionNameLength | integer | Максимальная длина имени действия в символах. Допустимые значения от 5 до 10000. | Required |
| maxErrorsToCapture | integer | Максимальное количество ошибок, захватываемых на страницу. Допустимые значения от 0 до 50. | Required |
| proxyWrapperEnabled | boolean | Прокси-обёртка включена/выключена. | Optional |
| specialCharactersToEscape | string | Дополнительные специальные символы, которые нужно экранировать неалфавитно-цифровыми символами в формате HTML escape. | Required |
| syncBeaconFirefox | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest при использовании Firefox включена/выключена. | Optional |
| syncBeaconInternetExplorer | boolean | Отправка сигнала beacon как синхронного XMLHttpRequest при использовании Internet Explorer включена/выключена. | Optional |
| userActionNameAttribute | string | Атрибут имени пользовательского действия. | Optional |


#### Объект `AdditionalEventHandlers`


Дополнительные обработчики событий и обёртки.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| blurEventHandler | boolean | Обработчик события blur включён/выключен. | Required |
| changeEventHandler | boolean | Обработчик события change включён/выключен. | Required |
| clickEventHandler | boolean | Обработчик события click включён/выключен. | Required |
| maxDomNodesToInstrument | integer | Макс. число DOM-узлов для инструментирования. Допустимые значения от 0 до 100000. | Required |
| mouseupEventHandler | boolean | Обработчик события mouseup включён/выключен. | Required |
| toStringMethod | boolean | Метод toString включён/выключен. | Required |
| userMouseupEventForClicks | boolean | Использование события mouseup для кликов включено/выключено. | Required |


#### Объект `EventWrapperSettings`


Помимо обработчиков событий, можно захватывать события, вызванные через `addEventListener` или `attachEvent`. С этой опцией нужно быть осторожным! Обёртки событий могут конфликтовать с JavaScript-кодом на веб-странице.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| blur | boolean | Blur включён/выключен. | Required |
| change | boolean | Change включён/выключен. | Required |
| click | boolean | Click включён/выключен. | Required |
| mouseUp | boolean | MouseUp включён/выключен. | Required |
| touchEnd | boolean | TouchEnd включён/выключен. | Required |
| touchStart | boolean | TouchStart включён/выключен. | Required |


#### Объект `GlobalEventCaptureSettings`


Настройки глобального захвата событий.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Дополнительные события, захватываемые глобально как пользовательский ввод.  Например, DragStart или DragEnd. | Required |
| change | boolean | Change включён/выключен. | Optional |
| click | boolean | Click включён/выключен. | Required |
| doubleClick | boolean | DoubleClick включён/выключен. | Required |
| keyDown | boolean | KeyDown включён/выключен. | Required |
| keyUp | boolean | KeyUp включён/выключен. | Required |
| mouseDown | boolean | MouseDown включён/выключен. | Required |
| mouseUp | boolean | MouseUp включён/выключен. | Required |
| scroll | boolean | Scroll включён/выключен. | Required |
| touchEnd | boolean | TouchEnd включён/выключен. | Optional |
| touchStart | boolean | TouchStart включён/выключен. | Optional |


#### Объект `WebApplicationConfigBrowserRestrictionSettings`


Настройки для ограничения определённого типа, версии, платформы браузера и компаратора. Также ограничивает режим.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction](#openapi-definition-WebApplicationConfigBrowserRestriction)[] | Список ограничений браузера. | Optional |
| mode | string | Режим списка ограничений браузера. Элемент может принимать следующие значения * `EXCLUDE` * `INCLUDE` | Required |


#### Объект `WebApplicationConfigBrowserRestriction`


Правила исключения для браузеров, которые нужно исключить.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| browserType | string | Тип используемого браузера. Элемент может принимать следующие значения * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` | Required |
| browserVersion | string | Версия используемого браузера. | Optional |
| comparator | string | Сравнивает разные браузеры между собой. Элемент может принимать следующие значения * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` | Optional |
| platform | string | Платформа, на которой используется браузер. Элемент может принимать следующие значения * `ALL` * `DESKTOP` * `MOBILE` | Optional |


#### Объект `ContentCapture`


Настройки захвата содержимого.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| javaScriptErrors | boolean | Мониторинг ошибок JavaScript включен/выключен. | Required |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Настройки захвата тайминга ресурсов. | Required |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Настройки захвата timed action. | Required |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Настройки для VisuallyComplete2 | Optional |
| visuallyCompleteAndSpeedIndex | boolean | Поддержка Visually complete и Speed index включена/выключена. | Required |


#### Объект `ResourceTimingSettings`


Настройки захвата тайминга ресурсов.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| nonW3cResourceTimings | boolean | Тайминг для файлов JavaScript и изображений в браузерах, не поддерживающих W3C, включен/выключен. | Required |
| nonW3cResourceTimingsInstrumentationDelay | integer | Задержка инструментирования для мониторинга влияния ресурсов и изображений в браузерах, не предоставляющих W3C resource timings.  Допустимые значения от 0 до 9999.  Действует только если включён **nonW3cResourceTimings**. | Required |
| resourceTimingCaptureType | string | Определяет, насколько подробно захватывается тайминг ресурсов.  Действует только если включён **w3cResourceTimings** или **nonW3cResourceTimings**. Элемент может содержать следующие значения * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` | Optional |
| resourceTimingsDomainLimit | integer | Ограничивает количество доменов, для которых захватывается W3C resource timings.  Действует только если **resourceTimingCaptureType** равен `CAPTURE_LIMITED_SUMMARIES`. | Optional |
| w3cResourceTimings | boolean | W3C resource timings для сторонних сервисов/CDN включен/выключен. | Required |


#### Объект `TimeoutSettings`


Настройки захвата timed action.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Определяет глубину каскадирования временных actions. 0 полностью отключает временные actions. Рекомендуемое значение при включении, 3. | Required |
| temporaryActionTotalTimeout | integer | Общий таймаут всех каскадных таймаутов, при котором ещё возможно создание временного action | Required |
| timedActionSupport | boolean | Поддержка timed action включена/выключена.  Включить для обнаружения actions, инициирующих отправку XHR через методы *setTimout*. | Required |


#### Объект `VisuallyComplete2Settings`


Настройки для VisuallyComplete2


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| excludeUrlRegex | string | Регулярное выражение, используемое для исключения изображений и iframe из обнаружения модулем VC. | Optional |
| ignoredMutationsList | string | Селектор запроса для узлов мутаций, игнорируемых при расчёте VC и SI | Optional |
| inactivityTimeout | integer | Время в мс, в течение которого модуль VC ожидает отсутствия мутаций на странице после действия load. По умолчанию 1000. | Optional |
| mutationTimeout | integer | Определяет время в мс, которое VC ожидает после завершения action перед началом расчёта. По умолчанию 50. | Optional |
| threshold | integer | Минимальная видимая площадь элементов в пикселях, учитываемая для VC и SI. По умолчанию 50. | Optional |


#### Объект `WebApplicationConfigIpAddressRestrictionSettings`


Настройки для ограничения определённых IP-адресов и указания маски подсети. Также определяет режим ограничения.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange](#openapi-definition-IpAddressRange)[] | - | Optional |
| mode | string | Режим списка ограничений IP-адресов. Элемент может содержать следующие значения * `EXCLUDE` * `INCLUDE` | Required |


#### Объект `IpAddressRange`


IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| address | string | IP-адрес, который нужно сопоставить.  Для диапазона IP-адресов, это адрес **from**. | Required |
| addressTo | string | Адрес **to** диапазона IP-адресов. | Optional |
| subnetMask | integer | Маска подсети диапазона IP-адресов. | Optional |


#### Объект `JavaScriptFrameworkSupport`


Поддержка различных JavaScript-фреймворков.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeXObject | boolean | Поддержка обнаружения ActiveXObject включена/выключена. | Required |
| angular | boolean | Поддержка AngularJS и Angular включена/выключена. | Required |
| dojo | boolean | Поддержка Dojo включена/выключена. | Required |
| extJS | boolean | Поддержка ExtJS, Sencha Touch включена/выключена. | Required |
| icefaces | boolean | Поддержка ICEfaces включена/выключена. | Required |
| jQuery | boolean | Поддержка jQuery, Backbone.js включена/выключена. | Required |
| mooTools | boolean | Поддержка MooTools включена/выключена. | Required |
| prototype | boolean | Поддержка Prototype включена/выключена. | Required |


#### Объект `JavaScriptInjectionRules`


Правила для внедрения javascript


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | Правило включения или отключения внедрения java script. | Required |
| htmlPattern | string | Html-паттерн внедрения java script. | Optional |
| rule | string | Правило url для внедрения java script. Элемент может содержать следующие значения * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` | Required |
| target | string | Цель, с которой должно сопоставляться правило внедрения java script. Элемент может содержать следующие значения * `PAGE_QUERY` * `URL` | Optional |
| urlOperator | string | Оператор url для внедрения java script. Элемент может содержать следующие значения * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Required |
| urlPattern | string | Url-паттерн внедрения java script. | Optional |


#### Объект `SessionReplaySetting`


Настройки session replay


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| costControlPercentage | integer | Доля сэмплирования session replay в процентах. | Required |
| cssResourceCapturingExclusionRules | string[] | Список URL, исключаемых из захвата CSS-ресурсов. | Optional |
| enableCssResourceCapturing | boolean | Захватывать (`true`) или не захватывать (`false`) CSS-ресурсы из сессии. | Optional |
| enabled | boolean | SessionReplay включен. | Required |


#### Объект `UserActionAndSessionProperties`


Определяет настройки пользовательских свойств userAction и session для приложения.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Элемент может содержать следующие значения * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Optional |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите там [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для нужных данных. | Optional |
| displayName | string | Отображаемое имя свойства. | Optional |
| ignoreCase | boolean | Если true, значение этого свойства всегда сохраняется в нижнем регистре. По умолчанию false. | Optional |
| key | string | Ключ свойства | Required |
| longStringLength | integer | Если тип LONG\_STRING, максимальная длина для этого свойства. Должна быть кратна 100. По умолчанию 200. | Optional |
| metadataId | integer | Ссылка на uniqueId MetadataCapturingConfig. Должна быть указана, если "origin" имеет тип META\_DATA. | Optional |
| origin | string | Происхождение свойства Элемент может содержать следующие значения * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Required |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Optional |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство session | Optional |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство user action | Optional |
| type | string | Тип данных свойства. Элемент может содержать следующие значения * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` | Required |
| uniqueId | integer | Уникальный id среди всех userTags и свойств этого приложения | Required |


#### Объект `UserActionNamingSettings`


Настройки именования user action.


| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования user action для custom actions. | Optional |
| ignoreCase | boolean | Именование без учёта регистра. | Optional |
| loadActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования user action для loading actions. | Optional |
| placeholders | [UserActionNamingPlaceholder](#openapi-definition-UserActionNamingPlaceholder)[] | Плейсхолдеры именования user action. | Optional |
| queryParameterCleanups | string[] | Список параметров, которые нужно удалить из запроса перед использованием запроса в имени user action. | Optional |
| splitUserActionsByDomain | boolean | Отключить эту настройку, если разные домены не должны приводить к раздельным user actions. | Optional |
| useFirstDetectedLoadAction | boolean | Если true, используется первый найденный load action под XHR action. Иначе используется самый глубокий под xhr action | Optional |
| xhrActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | Правила именования user action для xhr actions. | Optional |


#### Объект `UserActionNamingRule`


Настройки правила именования.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| conditions | [UserActionNamingRuleCondition](#openapi-definition-UserActionNamingRuleCondition)[] | Определяет условия, при которых применяется правило именования. | Опционально |
| template | string | Шаблон именования. Фигурные скобки `{}` используются для выбора плейсхолдеров. | Обязательно |
| useOrConditions | boolean | Если задано значение `true`, условия объединяются логическим ИЛИ вместо логического И. | Опционально |


#### Объект `UserActionNamingRuleCondition`


Настройки условий для именования пользовательских действий.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| operand1 | string | Должен быть определённым плейсхолдером, заключённым в фигурные скобки | Обязательно |
| operand2 | string | Должно быть null, если оператор "IS\_EMPTY", регулярным выражением, если оператор "MATCHES\_REGULAR\_ERPRESSION". Во всех остальных случаях значение может быть произвольным текстом или плейсхолдером, заключённым в фигурные скобки | Опционально |
| operator | string | Оператор условия. Элемент может принимать следующие значения * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` | Обязательно |


#### Объект `UserActionNamingPlaceholder`


Настройки плейсхолдера.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| input | string | Входные данные. Элемент может принимать следующие значения * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` | Обязательно |
| metadataId | integer | Ссылка на uniqueId конфигурации MetadataCapturingConfig. Должно быть задано, если "Input" имеет тип METADATA. | Опционально |
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
| patternToReplace | string | Паттерн для замены.  Применимо только если **type** имеет значение `REPLACE_WITH_PATTERN`. | Опционально |
| regularExpression | string | Регулярное выражение для строки, которую нужно извлечь или заменить.  Применимо только если **type** имеет значение `EXTRACT_BY_REGULAR_EXPRESSION` или `REPLACE_WITH_REGULAR_EXPRESSION`. | Опционально |
| replacement | string | Замена для исходного значения. | Опционально |
| type | string | Действие, выполняемое обработкой:  * `SUBSTRING`: извлекает строку между **patternBefore** и **patternAfter**. * `REPLACEMENT`: заменяет строку между **patternBefore** и **patternAfter** на указанное значение **replacement**. * `REPLACE_WITH_PATTERN`: заменяет **patternToReplace** на указанное значение **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: извлекает часть строки, соответствующую **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: заменяет все вхождения, соответствующие **regularExpression**, на указанное значение **replacement**. * `REPLACE_IDS`: заменяет все ID и UUID на указанное значение **replacement**. Элемент может принимать следующие значения * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` | Обязательно |


#### Объект `UserTag`


Определяет настройки UserTags для приложения.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| cleanupRule | string | Выражение правила очистки userTag | Опционально |
| ignoreCase | boolean | Если true, значение этого тега всегда будет храниться в нижнем регистре. По умолчанию false. | Опционально |
| metadataId | integer | Ссылка на uniqueId конфигурации MetadataCapturingConfig. Должно быть задано, если UserTag основан на метаданных, захваченных Javascript-агентом (например, переменная Javascript, CSS-селектор и т.д.) | Опционально |
| serverSideRequestAttribute | string | Идентификатор серверного атрибута запроса (request attribute) для userTag. Должно быть задано, если UserTag основан на серверном атрибуте запроса. | Опционально |
| uniqueId | integer | uniqueId, уникальный среди всех userTags и свойств данного приложения | Обязательно |


#### Объект `WaterfallSettings`


Эти настройки влияют на данные мониторинга, получаемые для ресурсов сторонних сервисов, CDN и собственных (1st party) ресурсов.


| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Предупреждать о ресурсах с более низкой частотой кэширования браузером выше *X*%. | Обязательно |
| resourcesThreshold | integer | Предупреждать о ресурсах размером больше *X* байт. | Обязательно |
| slowCdnResourcesThreshold | integer | Предупреждать о медленных ресурсах CDN со временем отклика выше *X* мс. | Обязательно |
| slowFirstPartyResourcesThreshold | integer | Предупреждать о медленных собственных (1st party) ресурсах со временем отклика выше *X* мс. | Обязательно |
| slowThirdPartyResourcesThreshold | integer | Предупреждать о медленных сторонних (3rd party) ресурсах со временем отклика выше *X* мс. | Обязательно |
| speedIndexVisuallyCompleteRatioThreshold | integer | Предупреждать, если Speed index превышает *X* % от Visually complete. | Обязательно |
| uncompressedResourcesThreshold | integer | Предупреждать о несжатых ресурсах размером больше *X* байт. | Обязательно |

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Тело ответа содержит ID и имя нового веб-приложения. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление Dynatrace сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание Dynatrace сущности. |
| id | string | ID Dynatrace сущности. |
| name | string | Имя Dynatrace сущности. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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

## Проверка payload

Рекомендуется проверять payload перед отправкой его в составе реального запроса. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `WriteConfig`.

Подробнее о том, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

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
| code | integer | HTTP-код состояния |
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