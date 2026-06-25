---
title: Конфигурационные ключи OneAgent for iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys
scraped: 2026-05-12T11:33:04.939987
---

# Конфигурационные ключи OneAgent for iOS

# Конфигурационные ключи OneAgent for iOS

* How-to guide
* 11-min read
* Updated on Feb 27, 2026

Конфигурационные ключи — это свойства, которые можно настраивать для авто-инструментирования. Добавляйте ключи в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") приложения по мере необходимости для точной настройки авто-инструментирования.

В следующих таблицах перечислены все конфигурационные ключи для авто-инструментирования iOS.

## Общие

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXApplicationID` Обязательный | string | Идентифицирует мобильное приложение. Авто-инструментирование сообщает об ошибке, если ключ отсутствует. |  |
| `DTXBeaconURL` Обязательный | string | Значение этого ключа используется для идентификации окружения в Dynatrace. Авто-инструментирование сообщает об ошибке, если ключ отсутствует. |  |
| `DTXAutoStart` | boolean | При значении `false` OneAgent не запускается автоматически, поэтому его нужно [запустить вручную](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS."). | `true` |
| `DTXStartupLoadBalancing` | boolean | При значении `true` включает балансировку нагрузки на стороне агента при запуске, что позволяет избежать неравномерной нагрузки на сервер при одновременном установлении соединения несколькими OneAgent с ActiveGate. | `false` |
| `DTXLogLevel` | string | Если этот ключ присутствует с допустимым значением, [журналирование OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Включите отладочное журналирование для OneAgent.") автоматически включается с указанным значением. Если ключ отсутствует или имеет недопустимое значение, автоматическое журналирование отключается и должно быть включено вручную через вызов API.  **Возможные значения**: `OFF`, `SEVERE`, `WARNING`, `INFO`, `ALL` | `OFF` |
| `DTXStartupWithGrailEnabled` | boolean | При значении `true` New RUM Experience включается при первом запуске приложения, до получения конфигурации кластера. Этот параметр не имеет эффекта после первого запуска. После получения конфигурации кластера она постоянно переопределяет этот флаг. | `false` |

## Пользовательские действия

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXInstrumentAutoUserAction` | boolean | Включает возможность автоматического [создания пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent.") для пользовательских взаимодействий с приложением, например нажатий кнопок. Установите значение `false`, чтобы отключить автоматическое создание пользовательских действий. | `true` |
| `DTXExcludedControlClasses` | array | Массив элементов, каждый из которых содержит имя класса элемента управления UI (или подкласса) для исключения из автоматического инструментирования. Каждый элемент массива является строкой с учётом регистра, которая должна точно совпадать с именем исключаемого класса. |  |
| `DTXExcludedControls` | array | Определяет массив элементов, каждый из которых содержит тип представления или элемента управления для исключения из автоматического создания пользовательских действий. Каждый элемент массива является строкой без учёта регистра.  **Возможные значения**: `Button`, `DatePicker`, `Slider`, `Stepper`, `Switch`, `RefreshControl`, `ToolBar`, `SegmentedControl`, `TableView`, `TabBar`, `AlertView`, `AlertAction`, `PageView`, `NavigationController`, `CollectionView`, `ActionSheet`, `PickerView` |  |
| `DTXUIActionNamePrivacy`[1] | boolean | При значении `true` включает [маскировку пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.").  * **Приложения на UIKit**. OneAgent заменяет заголовки элементов управления в именах пользовательских действий на общие типы элементов. * **Приложения на SwiftUI**. OneAgent не сообщает о дочерних событиях, содержащих заголовки элементов управления пользовательских действий «touch».  В результате все имена пользовательских действий вида `Touch on <control title>` изменяются на `Touch on <generic control type>`. Например, `Touch on Account 123456` становится `Touch on Button`. | `false` |
| `DTXDetectRageTaps` | boolean | Определяет, включено ли [обнаружение rage tap](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#rage-taps "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent."). Используйте эту функцию как меру раздражения пользователя. Установите значение `false`, чтобы прекратить обнаружение rage tap. | `true` |
| `DTXSendEmptyAutoAction` | boolean | Определяет, следует ли отправлять автоматические пользовательские действия, не содержащие веб-запросов или действий жизненного цикла. | `true` |
| `DTXAutoActionMaxDurationMilliseconds` | number | Устанавливает время хранения автоматического пользовательского действия до его удаления. Цель — обнаружить все веб-запросы, происходящие при активном автоматическом пользовательском действии. Если у автоматического пользовательского действия есть незавершённые веб-запросы, OneAgent ожидает истечения этого времени для завершения запросов, прежде чем покинуть действие.  **Возможные значения**: от `100` мс (= 0,1 секунды) до `540000` мс (= 9 минут) | `60000` мс |
| `DTXAutoActionTimeoutMilliseconds` | number | Устанавливает, как долго конкретное автоматическое пользовательское действие остаётся активным. Цель — обнаружить все веб-запросы, происходящие при активном автоматическом пользовательском действии. Если автоматическое пользовательское действие завершило веб-запросы, OneAgent покидает действие по истечении этого времени.  **Возможные значения**: от `100` мс (= 0,1 секунды) до `5000` мс (= 5 секунд) | `500` мс |

1

Доступно для OneAgent for iOS версии 8.249+

## Веб-запросы

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXInstrumentWebRequestTiming` | boolean | Включает автоматический [тайминг и тегирование веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent."). Для [отключения автоматического тайминга и тегирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.") установите значение `false`. | `true` |
| `DTXURLFilters` | array | Массив элементов, каждый из которых содержит URL-фильтры для исключения веб-запросов из мониторинга. Каждый элемент массива должен быть строкой URL или регулярным выражением, совпадающим с нужным URL. |  |
| `DTXFilterURLProtocolDuplicates` | boolean | Необходим при использовании подклассов NSURLProtocol, когда могут появляться дублирующиеся веб-запросы. | `false` |

## Мониторинг жизненного цикла

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXInstrumentLifecycleMonitoring` | boolean | Включает автоматическое [обнаружение жизненного цикла](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#lifecycle "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent.") для классов iOS `ViewController`. Для отключения автоматического мониторинга жизненного цикла установите значение `false`. | `true` |
| `DTXInstrumentFrameworks`[1] устарело | boolean | Включает автоматическое инструментирование жизненного цикла классов UI из сторонних фреймворков, входящих в состав приложения. Установите значение `true`, чтобы включить автоматическое инструментирование жизненного цикла сторонних фреймворков. Для этого OneAgent for iOS требуется сканирование всех фреймворков, входящих в состав приложения, что может заметно повлиять на производительность при запуске. | `false` |
| `DTXExcludedLifecycleClasses` | array | Массив элементов, каждый из которых содержит имя класса для исключения из автоматического инструментирования жизненного цикла. Каждый элемент массива является строкой с учётом регистра, которая должна точно совпадать с именем исключаемого класса. |  |

1

Устарел начиная с OneAgent for iOS версии 8.331

## Гибридные приложения

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXHybridApplication` | boolean | Для [гибридных приложений](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.") установите значение `true`. Это необходимо для общего использования визита для пользовательских действий, создаваемых RUM JavaScript. | `false` |
| `DTXSetCookiesForDomain` | array[string] | Для гибридных приложений, использующих RUM JavaScript, [cookies должны устанавливаться](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app#set-up-oneagent "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.") для каждого инструментированного домена или сервера, с которым взаимодействует приложение. Можно указывать домены, хосты или IP-адреса. Домены и субдомены должны начинаться с точки. |  |
| `DTXSetSecureCookiesForDomain` | array[string] | Для гибридных приложений, использующих RUM JavaScript, [cookies должны устанавливаться](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app#set-up-oneagent "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.") для каждого инструментированного домена или сервера, с которым взаимодействует приложение. Можно указывать домены, хосты или IP-адреса. Домены и субдомены должны начинаться с точки. Этот ключ аналогичен `DTXSetCookiesForDomain`, но атрибут `Secure` добавляется ко всем cookies, устанавливаемым Dynatrace. Это гарантирует отправку браузером этих cookies только через защищённые соединения. |  |
| `DTXInstrumentWebViewTiming` | boolean | Включает автоматический [тайминг и тегирование веб-запросов для запросов, передаваемых в `WKWebView`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests-wkwebview "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent."). Не работает для запросов, инициированных из JavaScript внутри `WKWebView`. Установите значение `false`, чтобы отключить автоматический тайминг и тегирование. | `true` |
| `DTXWebViewStandInDelegate`[1] устарело | boolean | Использует другой режим инструментирования для делегатов `WKWebView`, чтобы предотвратить циклическое инструментирование при переключении делегатов с подклассом. | `false` |

1

Устарел начиная с OneAgent for iOS версии 8.257

## Конфиденциальность и безопасность

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXUserOptIn` | boolean | При значении `true` активирует [режим opt-in для пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.").  При включённом режиме opt-in необходимо запрашивать у каждого пользователя разрешение на сбор данных, а затем сохранять его настройки конфиденциальности. Подробнее см. в разделе [Настройка конфиденциальности данных](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#privacy "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS."). | `false` |
| `DTXCrashReportingEnabled` | boolean | Включает [отчёты о сбоях](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent."). Для отключения отчётов о сбоях установите значение `false`. | `true` |
| `DTXInstrumentGPSLocation` | boolean | При значении `true` включает [мониторинг местоположения](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent."). Местоположение захватывается, когда приложение использует `CLLocationManager`, и отправляется в виде метрики на сервер. OneAgent SDK for iOS не выполняет самостоятельный захват GPS-координат; для защиты конфиденциальности конечного пользователя данные захватываются с точностью до трёх знаков после запятой. | `false` |
| `DTXPublicKeyPins` | array[string] | Содержит выходные данные скрипта `getPKHashFromCertificate.py`, используемые для включения функции [Public Key Hash Pinning](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/configuration-settings#pkh-pinning "Настройте авто-инструментирование для iOS-приложений с помощью расширенных настроек.") для мобильного приложения. |  |
| `DTXAgentCertificatePath` | string | Определяет путь к (самоподписанному) сертификату в формате `DER`, который используется как дополнительный якорь для проверки HTTPS-коммуникации. Этот ключ необходим, если `DTXAllowAnyCert` равно `false` и на сервере используется самоподписанный сертификат. | `null` |
| `DTXAllowAnyCert` | boolean | Разрешает использование самоподписанных сертификатов. При значении `true` OneAgent for iOS принимает самоподписанные сертификаты (сертификаты, не подписанные корневым CA). Этот конфигурационный ключ не влияет на подключения мобильного приложения. Он используется только для коммуникации OneAgent, но не переопределяет проверку имени хоста. | `false` |
| `DTXWriteLogsToFile` | boolean | При значении `true` позволяет OneAgent записывать журналы в локальное хранилище устройства. Этот флаг необходимо установить в `true` для использования API [`shareLogsFile`](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#log-sharing "Узнайте, какие типы данных конечных пользователей могут захватываться при мониторинге Dynatrace."), позволяющего делиться журналами через iOS sharing sheet (`UIActivityViewController`). Эта функция недоступна в tvOS. | `false` |
| `DTXANRReportingEnabled` | boolean | Включает отчёты об ошибках «Application Not Responding» (ANR). Для отключения отчётов ANR установите значение `false`. | `true` |
| `DTXANRTimeout` | number | Устанавливает тайм-аут обнаружения «Application Not Responding» (ANR). Измените это значение, чтобы адаптировать тайм-аут, необходимый для обнаружения ANR.  **Возможные значения**: от `1` до `20` секунд | `2` |

## SwiftUI

| Ключ | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXSwiftUIEnableSessionReplayInstrumentation`[1] | boolean | При значении `true` включает [Session Replay для SwiftUI-приложений](/managed/observe/digital-experience/session-replay/session-replay-ios#sr-swiftui "Требования и процедура включения Session Replay для iOS-приложений."). | `false` |
| `DTXExcludedSwiftUIFiles`[1] | array[string] | Содержит относительные пути к файлам и директориям, [исключённым из инструментирования SwiftUI](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#exclude-swift-files "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений."). Пути указываются относительно корня проекта, то есть директории с файлом `.xcodeproj`. |  |
| `DTXSwiftUIExcludedControls`[3] | array[string] | Указывает элементы управления SwiftUI, [глобально исключённые из инструментирования SwiftUI](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#exclude-controls-global "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений.").  **Возможные значения**: все значения в разделе [Поддерживаемые элементы управления](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#supported-controls "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений.") |  |
| `DTXSwiftUIInstrumentSimulatorBuilds`[1] | boolean | При значении `true` включает [инструментирование SwiftUI для сборок симулятора](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#instrument-simulator-builds "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений."). |  |
| `DTXSwiftUIIgnoreDeploymentTarget`[1] | boolean | При значении `true` позволяет [создавать сборки для целевых версий развёртывания iOS 13 и более ранних](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#builds-for-unsupported-deployment-targets "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений."). |  |
| `DTXSwiftUIManualPlaceholder`[1] | boolean | При значении `true` [включает маппинг номеров строк](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#line-number-mapping-objective-c "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений.") для устаревших проектов на Objective-C. Обратите внимание, что требуется дополнительная настройка. |  |
| `DTXCleanSwiftUILogsByCount`[2] | number | Устанавливает количество сборок, после которого [удаляются журналы SwiftUI instrumentor](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#enable-log-cleanup "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений.").  **Возможные значения**: от `1` до `1000` |  |
| `DTXCleanSwiftUILogsByAgeDays`[2] | number | Устанавливает количество дней, после которого [удаляются журналы SwiftUI instrumentor](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#enable-log-cleanup "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений.").  **Возможные значения**: от `1` до `500` |  |
| `DTXSwiftUIEnableUserInteractionsInstrumentation`[1] | boolean | При значении `false` отключает инструментирование пользовательских взаимодействий для элементов управления SwiftUI. Включено по умолчанию. | `true` |
| `DTXUIAdvancedLabelDetection`[1] | boolean | При значении `false` отключает расширенное обнаружение меток для элементов управления SwiftUI. При включении instrumentor анализирует структуру кода SwiftUI для извлечения меток элементов управления из параметров `label:` и `title:`, trailing closures, выражений доступа к членам и тернарных операторов. При отключении instrumentor переключается на поиск первого простого строкового литерала внутри элемента управления. Включено по умолчанию. | `true` |
| `DTXSkipUnnamedArgClosures`[1] | boolean | При значении `true` SwiftUI instrumentor пропускает инструментирование замыканий, использующих сокращённый синтаксис аргументов (`$0`, `$1` и т.д.) вместо именованных параметров. По умолчанию instrumentor переименовывает эти сокращённые аргументы в именованные параметры для внедрения кода инструментирования. Включите этот ключ, чтобы оставить такие замыкания неинструментированными. | `false` |

1

Доступно для OneAgent for iOS версии 8.249+

2

Доступно для OneAgent for iOS версии 8.257+

3

Доступно для OneAgent for iOS версии 8.263+