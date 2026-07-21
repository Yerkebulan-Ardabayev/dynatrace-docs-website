---
title: OneAgent для ключей конфигурации iOS в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys
---

# OneAgent для ключей конфигурации iOS в RUM Classic

# OneAgent для ключей конфигурации iOS в RUM Classic

* Практическое руководство
* 11 минут на чтение
* Обновлено 27 февраля 2026 г.

Ключи конфигурации, это, по сути, свойства, которые можно настроить под свои предпочтения для авто-инструментирования. Добавь ключи в [файл `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификацию приложения и ключи конфигурации. Используй его для тонкой настройки конфигурации инструментирования.") приложения, если требуется точная настройка авто-инструментирования.

В следующих таблицах перечислены все ключи конфигурации для авто-инструментирования iOS.

## Общие

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXApplicationID`  Обязательный | строка | Идентифицирует мобильное приложение. Авто-инструментирование сообщает об ошибке, если ключ отсутствует. |  |
| `DTXBeaconURL`  Обязательный | строка | Значение этого ключа используется для идентификации окружения в Dynatrace. Авто-инструментирование сообщает об ошибке, если ключ отсутствует. |  |
| `DTXAutoStart` | логический | При значении `false` OneAgent не запускается автоматически, поэтому его нужно [запустить вручную](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#start-oneagent "Улучши мониторинг пользовательского опыта в мобильном приложении с помощью OneAgent SDK для iOS."). | `true` |
| `DTXStartupLoadBalancing` | логический | При значении `true` включает балансировку нагрузки на стороне агента при запуске, что позволяет избежать неравномерной нагрузки на сервер, когда несколько OneAgent одновременно устанавливают соединение с ActiveGate. | `false` |
| `DTXLogLevel` | строка | Если этот ключ присутствует с корректным значением, [логирование OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios "Включи отладочное логирование для OneAgent.") автоматически включается с указанным значением. Если ключ отсутствует или не содержит корректного значения, автоматическое логирование выключено и его нужно включить вручную вызовом API.  **Возможные значения**: `OFF`, `SEVERE`, `WARNING`, `INFO`, `ALL` | `OFF` |
| `DTXStartupWithGrailEnabled` | логический | При значении `true` RUM на последнем Dynatrace включается при первом запуске приложения, до получения конфигурации кластера. Эта настройка не действует после первого запуска приложения. После получения конфигурации кластера она навсегда переопределяет этот флаг. | `false` |

## Пользовательские действия

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXInstrumentAutoUserAction` | логический | Включает возможность автоматического [создания пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#user-actions "Ознакомься со списком функций, доступных после инструментирования приложения с помощью OneAgent.") для взаимодействий пользователя с приложением, таких как нажатия кнопок. Установи значение `false`, чтобы отключить автоматическое создание пользовательских действий. | `true` |
| `DTXExcludedControlClasses` | массив | Массив элементов, где каждый элемент содержит имя класса (или подкласса) элемента UI, который нужно исключить из автоматического инструментирования элементов управления. Каждый элемент массива, это строка с учётом регистра, которая должна точно совпадать с именем исключаемого класса. |  |
| `DTXExcludedControls` | массив | Определяет массив элементов, где каждый элемент содержит тип представления или элемента управления, который нужно исключить из автоматического создания пользовательских действий. Каждый элемент массива, это строка без учёта регистра.  **Возможные значения**: `Button`, `DatePicker`, `Slider`, `Stepper`, `Switch`, `RefreshControl`, `ToolBar`, `SegmentedControl`, `TableView`, `TabBar`, `AlertView`, `AlertAction`, `PageView`, `NavigationController`, `CollectionView`, `ActionSheet`, `PickerView` |  |
| `DTXUIActionNamePrivacy`[1](#fn-1-1-def) | логический | При значении `true` включает [маскирование пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Улучши мониторинг пользовательского опыта в мобильном приложении с помощью OneAgent SDK для iOS.").  * **Приложения на основе UIKit**. OneAgent заменяет заголовки элементов управления в именах пользовательских действий на общие типы элементов управления. * **Приложения на основе SwiftUI**. OneAgent не сообщает о дочерних событиях, содержащих заголовки элементов управления действий "touch".  В результате все имена пользовательских действий вида `Touch on <заголовок элемента управления>` меняются на `Touch on <общий тип элемента управления>`. Например, `Touch on Account 123456` становится `Touch on Button`. | `false` |
| `DTXDetectRageTaps` | логический | Определяет, включено ли [обнаружение яростных нажатий (rage tap)](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#rage-taps "Ознакомься со списком функций, доступных после инструментирования приложения с помощью OneAgent."). Используй эту функцию как меру раздражения пользователя. Установи значение `false`, чтобы отключить обнаружение яростных нажатий. | `true` |
| `DTXSendEmptyAutoAction` | логический | Определяет, отправлять ли автоматические пользовательские действия, не содержащие веб-запросов или действий жизненного цикла. | `true` |
| `DTXAutoActionMaxDurationMilliseconds` | число | Задаёт время удержания автоматического пользовательского действия перед удалением. Цель, обнаружить все веб-запросы, происходящие пока автоматическое пользовательское действие активно. Если у автоматического пользовательского действия есть незавершённые веб-запросы, выполнение которых занимает больше времени, OneAgent ожидает завершения веб-запросов в течение этого времени, прежде чем покинуть пользовательское действие.  **Возможные значения**: от `100` мс (= 0,1 секунды) до `540000` мс (= 9 минут) | `60000` мс |
| `DTXAutoActionTimeoutMilliseconds` | число | Задаёт значение того, как долго конкретное автоматическое пользовательское действие остаётся активным. Цель, обнаружить все веб-запросы, происходящие пока автоматическое пользовательское действие активно. Если веб-запросы автоматического пользовательского действия завершены, OneAgent покидает действие по истечении этого времени.  **Возможные значения**: от `100` мс (= 0,1 секунды) до `5000` мс (= 5 секунд) | `500` мс |

1

Доступно для OneAgent для iOS версии 8.249+

## Веб-запросы

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXInstrumentWebRequestTiming` | логический | Включает автоматическое [измерение времени и тегирование веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests "Ознакомься со списком функций, доступных после инструментирования приложения с помощью OneAgent."). Чтобы [отключить автоматическое измерение времени и тегирование веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Улучши мониторинг пользовательского опыта в мобильном приложении с помощью OneAgent SDK для iOS."), установи значение `false`. | `true` |
| `DTXURLFilters` | массив | Массив элементов, где каждый элемент содержит фильтры URL для исключения веб-запросов из мониторинга. Каждый элемент массива должен быть строкой URL или регулярным выражением, соответствующим URL, который нужно отфильтровать. |  |
| `DTXFilterURLProtocolDuplicates` | логический | Требуется, если используется подклассирование NSURLProtocol и могут появляться дублирующиеся веб-запросы. | `false` |

## Мониторинг жизненного цикла

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXInstrumentLifecycleMonitoring` | логический | Включает автоматическое [обнаружение жизненного цикла](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#lifecycle "Ознакомься со списком функций, доступных после инструментирования приложения с помощью OneAgent.") для классов `ViewController` в iOS. Чтобы отключить автоматический мониторинг жизненного цикла, установи значение `false`. | `true` |
| `DTXInstrumentFrameworks`[1](#fn-2-1-def)  устарело | логический | Включает автоматическое инструментирование жизненного цикла классов UI из сторонних фреймворков, входящих в состав приложения. Установи значение `true`, чтобы включить автоматическое инструментирование жизненного цикла сторонних фреймворков. Эта конфигурация требует, чтобы OneAgent для iOS сканировал все фреймворки, входящие в состав приложения, что может привести к заметному снижению производительности при запуске приложения. | `false` |
| `DTXExcludedLifecycleClasses` | массив | Массив элементов, где каждый элемент содержит имя класса, который нужно исключить из автоматического инструментирования жизненного цикла. Каждый элемент массива, это строка с учётом регистра, которая должна точно совпадать с именем исключаемого класса. |  |

1

Устарело начиная с OneAgent для iOS версии 8.331

## Гибридные приложения

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXHybridApplication` | boolean | Для [гибридных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") установить значение `true`. Это нужно для того, чтобы пользовательские действия, созданные с помощью RUM JavaScript, использовали один и тот же визит. | `false` |
| `DTXSetCookiesForDomain` | array[string] | Для гибридных приложений, использующих RUM JavaScript, [нужно установить cookie](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app#set-up-oneagent "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") для каждого инструментированного домена или сервера, с которым взаимодействует приложение. Можно указать домены, хост или IP-адреса. Домены и поддомены должны начинаться с точки. |  |
| `DTXSetSecureCookiesForDomain` | array[string] | Для гибридных приложений, использующих RUM JavaScript, [нужно установить cookie](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app#set-up-oneagent "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") для каждого инструментированного домена или сервера, с которым взаимодействует приложение. Можно указать домены, хост или IP-адреса. Домены и поддомены должны начинаться с точки. Этот ключ конфигурации похож на `DTXSetCookiesForDomain`, но для cookie, устанавливаемых Dynatrace, добавляется атрибут `Secure`. Это гарантирует, что браузер отправляет такие cookie только по защищённым соединениям. |  |
| `DTXInstrumentWebViewTiming` | boolean | Включает автоматическое [измерение времени и тегирование веб-запросов, передаваемых в `WKWebView`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#web-requests-wkwebview "Explore the list of features that are available after you instrument your application with OneAgent."). Это не работает для запросов, отправляемых из JavaScript внутри `WKWebView`. Чтобы отключить автоматическое измерение времени и тегирование веб-запросов, установить значение `false`. | `true` |
| `DTXWebViewStandInDelegate`[1](#fn-3-1-def)  устарел | boolean | Использовать другой режим инструментирования для делегатов `WKWebView`, чтобы предотвратить циклическое инструментирование при переключении делегатов, затрагивающем подкласс. | `false` |

1

Устарело начиная с OneAgent для iOS версии 8.257

## Privacy and security

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXUserOptIn` | boolean | При значении `true` активирует [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."). Когда режим opt-in включён, нужно запрашивать у каждого пользователя разрешение на сбор его данных, а затем сохранять его настройки конфиденциальности данных. Подробности см. в разделе [Настройка конфиденциальности данных](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#privacy "Enrich mobile user experience monitoring using OneAgent SDK for iOS."). | `false` |
| `DTXCrashReportingEnabled` | boolean | Включает [отчёты о сбоях](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Explore the list of features that are available after you instrument your application with OneAgent."). Чтобы отключить отчёты о сбоях, установить значение `false`. | `true` |
| `DTXInstrumentGPSLocation` | boolean | При значении `true` включает [мониторинг местоположения](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Explore the list of features that are available after you instrument your application with OneAgent."). Местоположение фиксируется, когда приложение использует `CLLocationManager`, и отправляется на сервер как метрика. OneAgent SDK для iOS не выполняет захват GPS-местоположения самостоятельно, для защиты конфиденциальности конечного пользователя он фиксирует значение с точностью только до трёх знаков после запятой. | `false` |
| `DTXPublicKeyPins` | array[string] | Включает результаты работы скрипта `getPKHashFromCertificate.py`, используемые для включения функции [закрепления хешей открытых ключей (Public Key Hash Pinning)](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/configuration-settings#pkh-pinning "Configure auto-instrumentation for iOS apps using advanced settings.") для мобильного приложения. |  |
| `DTXAgentCertificatePath` | string | Определяет путь к (самоподписанному) сертификату в формате `DER`, используемому в качестве дополнительного якоря для проверки HTTPS-соединения. Этот ключ нужен, если `DTXAllowAnyCert` имеет значение `false` и на сервере используется самоподписанный сертификат. | `null` |
| `DTXAllowAnyCert` | boolean | Разрешает использование самоподписанных сертификатов. При значении `true` OneAgent для iOS принимает самоподписанные сертификаты (сертификаты, не подписанные `root-CA`). Этот ключ конфигурации не влияет на соединения мобильного приложения. Он используется только для коммуникации OneAgent, но не отменяет проверку имени хоста. | `false` |
| `DTXWriteLogsToFile` | boolean | При значении `true` разрешает OneAgent записывать логи в локальное хранилище устройства. Этот флаг обязательно должен иметь значение `true` для использования API [`shareLogsFile`](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#log-sharing "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data."), которая позволяет передавать логи через iOS-меню общего доступа (`UIActivityViewController`). Эта функция недоступна на tvOS. | `false` |
| `DTXANRReportingEnabled` | boolean | Включает отчёты об ошибках «Application Not Responding» (ANR). Чтобы отключить отчёты ANR, установить значение `false`. | `true` |
| `DTXANRTimeout` | number | Задаёт таймаут обнаружения «Application Not Responding» (ANR). Изменить это значение, чтобы настроить таймаут, требуемый для обнаружения ANR.  **Допустимые значения**: от `1` секунды до `20` секунд | `2` |

## SwiftUI

| Ключ | Тип ключа | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `DTXSwiftUIEnableSessionReplayInstrumentation`[1](#fn-4-1-def) | boolean | Если задано значение `true`, включает [Session Replay для SwiftUI-приложений](/managed/observe/digital-experience/session-replay/session-replay-ios#sr-swiftui "Предварительные условия и порядок включения Session Replay Classic для iOS-приложений."). | `false` |
| `DTXExcludedSwiftUIFiles`[1](#fn-4-1-def) | array[string] | Содержит относительные пути файлов и каталогов, которые [исключены из SwiftUI-инструментирования](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#exclude-swift-files "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений."). Пути указываются относительно корня проекта, то есть каталога, в котором находится файл `.xcodeproj`. |  |
| `DTXSwiftUIExcludedControls`[3](#fn-4-3-def) | array[string] | Задаёт элементы управления SwiftUI, которые [глобально исключены из SwiftUI-инструментирования](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#exclude-controls-global "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений.").  **Возможные значения**: все значения из раздела [Поддерживаемые элементы управления](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#supported-controls "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений.") |  |
| `DTXSwiftUIInstrumentSimulatorBuilds`[1](#fn-4-1-def) | boolean | Если задано значение `true`, включает [SwiftUI-инструментирование для сборок симулятора](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#instrument-simulator-builds "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений."). |  |
| `DTXSwiftUIIgnoreDeploymentTarget`[1](#fn-4-1-def) | boolean | Если задано значение `true`, позволяет [генерировать сборки для целевых версий iOS 13 и более ранних](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#builds-for-unsupported-deployment-targets "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений."). |  |
| `DTXSwiftUIManualPlaceholder`[1](#fn-4-1-def) | boolean | Если задано значение `true`, [включает сопоставление номеров строк](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#line-number-mapping-objective-c "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений.") для устаревших проектов на Objective-C. Обрати внимание, что требуется дополнительная настройка. |  |
| `DTXCleanSwiftUILogsByCount`[2](#fn-4-2-def) | number | Задаёт количество сборок, после которого [логи инструментатора SwiftUI удаляются](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#enable-log-cleanup "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений.").  **Возможные значения**: от `1` до `1000` |  |
| `DTXCleanSwiftUILogsByAgeDays`[2](#fn-4-2-def) | number | Задаёт количество дней, после которого [логи инструментатора SwiftUI удаляются](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#enable-log-cleanup "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений.").  **Возможные значения**: от `1` до `500` |  |
| `DTXSwiftUIEnableUserInteractionsInstrumentation`[1](#fn-4-1-def) | boolean | Если задано значение `false`, отключает инструментирование пользовательских взаимодействий для элементов управления SwiftUI. По умолчанию включено. | `true` |
| `DTXUIAdvancedLabelDetection`[1](#fn-4-1-def) | boolean | Если задано значение `false`, отключает расширенное определение меток для элементов управления SwiftUI. При включении инструментатор анализирует структуру кода SwiftUI, чтобы извлечь метки элементов управления из параметров `label:` и `title:`, замыкающих closures, выражений доступа к членам и тернарных операторов. При отключении инструментатор возвращается к поиску первого простого строкового литерала внутри элемента управления. По умолчанию включено. | `true` |
| `DTXSkipUnnamedArgClosures`[1](#fn-4-1-def) | boolean | Если задано значение `true`, инструментатор SwiftUI пропускает инструментирование замыканий, использующих сокращённый синтаксис аргументов (`$0`, `$1` и так далее) вместо именованных параметров. По умолчанию инструментатор переименовывает такие сокращённые аргументы в именованные параметры, чтобы иметь возможность внедрить код инструментирования. Включи этот ключ, чтобы оставить такие замыкания неинструментированными. | `false` |

1

Доступно для OneAgent для iOS версии 8.249+

2

Доступно для OneAgent для iOS версии 8.257+

3

Доступно для OneAgent для iOS версии 8.263+