---
title: Инструментирование элементов управления SwiftUI
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls
scraped: 2026-05-12T11:23:05.676450
---

# Инструментирование элементов управления SwiftUI

# Инструментирование элементов управления SwiftUI

* How-to guide
* 13-min read
* Updated on Feb 27, 2026

OneAgent for iOS версии 8.249+

После [инструментирования мобильного приложения с помощью OneAgent for iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.") вы также можете инструментировать элементы управления SwiftUI приложения. На этой странице представлена дополнительная информация о настройке проекта, обновлении SwiftUI instrumentor, обходе известных ограничений и других аспектах.

Для инструментирования элементов управления SwiftUI наш SwiftUI instrumentor добавляет дополнительный код в исходный код проекта (файлы `*.swift`) в процессе сборки. Этот код отслеживает состояние элементов UI и уведомляет OneAgent for iOS об изменениях. После завершения сборки все изменения исходного кода проекта отменяются.

Подробную информацию о действиях SwiftUI instrumentor и копии изменённых файлов кода можно найти в директории `dynatrace_instrumented`. SwiftUI instrumentor создаёт резервные копии инструментированных файлов и сгенерированные журналы в формате ZIP-архива.

## Требования

* SwiftUI версии 2.0+
* iOS 14+
* [OneAgent for iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.")

## Поддерживаемые элементы управления

Поддерживается инструментирование следующих элементов управления и представлений SwiftUI.

OneAgent for iOS версии 8.249+

* [`Button`](https://developer.apple.com/documentation/swiftui/button)
* [`Stepper`](https://developer.apple.com/documentation/swiftui/stepper)
* [`Picker`](https://developer.apple.com/documentation/swiftui/picker)
* [`Toggle`](https://developer.apple.com/documentation/swiftui/toggle)
* [`Slider`](https://developer.apple.com/documentation/swiftui/slider)

OneAgent for iOS версии 8.265+

* [`PasteButton`](https://developer.apple.com/documentation/swiftui/pastebutton)
* [`EditButton`](https://developer.apple.com/documentation/swiftui/editbutton)
* [`RenameButton`](https://developer.apple.com/documentation/swiftui/renamebutton)
* [`Link`](https://developer.apple.com/documentation/swiftui/link)
* [`ShareLink`](https://developer.apple.com/documentation/swiftui/sharelink)
* [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink)
* [`DatePicker`](https://developer.apple.com/documentation/swiftui/datepicker)
* [`MultiDatePicker`](https://developer.apple.com/documentation/swiftui/multidatepicker)
* [`ColorPicker`](https://developer.apple.com/documentation/swiftui/colorpicker)
* [`TabView`](https://developer.apple.com/documentation/swiftui/tabview)
* [`List`](https://developer.apple.com/documentation/swiftui/list)

OneAgent for iOS версии 8.269+

* [`Menu`](https://developer.apple.com/documentation/swiftui/menu)
* [`WindowGroup`](https://developer.apple.com/documentation/swiftui/windowgroup)

При необходимости можно [глобально](#exclude-controls-global) или [локально исключить определённые элементы управления из процесса инструментирования SwiftUI](#exclude-controls-local).

## Поддерживаемые методы

OneAgent for iOS версии 8.265+

Поддерживается инструментирование следующих методов SwiftUI:

* [`onTapGesture(count:perform:)`](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:))
* [`onTapGesture(count:coordinateSpace:perform:)`](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:))
* [`refreshable(action:)`](https://developer.apple.com/documentation/swiftui/view/refreshable(action:))
* [`sheet(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))
* [`sheet(item:onDismiss:content:)`](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:))
* [`popover(isPresented:attachmentAnchor:arrowEdge:content:)`](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:))
* [`popover(item:attachmentAnchor:arrowEdge:content:)`](https://developer.apple.com/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))
* [`navigationDestination(for:destination:)`](https://developer.apple.com/documentation/swiftui/view/navigationdestination(for:destination:))
* [`renameAction(_:)`](https://developer.apple.com/documentation/swiftui/view/renameaction(_:))

При каждом выполнении замыкания одного из поддерживаемых методов сообщаются следующие данные:

* Имя метода
* Тип представления, к которому прикреплён метод
* Имя родительского представления

## Мониторинг жизненного цикла

OneAgent for iOS версии 8.265+

SwiftUI instrumentor собирает данные о следующих событиях:

* **Application start**
* **Display**: [`onAppear`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) любого представления SwiftUI, открытого из элемента управления [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink) или [`TabView`](https://developer.apple.com/documentation/swiftui/tabview)
* **Redisplay**: [`onAppear`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) любого представления SwiftUI, открытого из элемента управления [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink) или [`TabView`](https://developer.apple.com/documentation/swiftui/tabview)

## Обязательные шаги

Для инструментирования элементов управления SwiftUI приложения убедитесь, что выполнены следующие шаги:

1. **Создайте приложение в Dynatrace**
2. **Настройте OneAgent для проекта**
3. **Установите SwiftUI instrumentor**

## Управление SwiftUI instrumentor

### Установка instrumentor

Для инструментирования элементов управления SwiftUI приложения установите Dynatrace SwiftUI instrumentor. Это можно сделать через Homebrew или вручную.

[OneAgent for iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.") должен быть уже настроен для проекта. Также не забудьте создать резервную копию проекта перед установкой instrumentor.

Homebrew

Вручную

1. Выполните `brew tap dynatrace/tools`, чтобы добавить один из Dynatrace tap.
2. Выполните `brew install DTSwiftInstrumentor`, чтобы установить SwiftUI instrumentor.
3. Закройте Xcode и выполните `DTSwiftInstrumentor install`.

   * Опционально. Также можно указать `<PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`. Если данные проекта не указаны, инструмент попытается автоматически определить доступные цели и схемы и запустит интерактивный выбор.

1. Загрузите и распакуйте ZIP-файл с нашим SwiftUI instrumentor. Ссылка доступна в [мастере инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.").
2. Создайте папку `.dynatrace` в корне проекта, на том же уровне, что и файл `*.xcodeproj`.

   Если система предупреждает о невозможности создать папку с именем, начинающимся с точки, выполните одно из следующих действий:

   * В Terminal выполните `mkdir .dynatrace` внутри корня проекта.
   * В Terminal выполните `defaults write com.apple.finder AppleShowAllFiles true` и `killall Finder`, чтобы отобразить скрытые папки и файлы. Затем создайте папку `.dynatrace` в Finder.

     Для скрытия скрытых папок и файлов обратно выполните `defaults write com.apple.finder AppleShowAllFiles false` и `killall Finder`.
3. Скопируйте загруженный `DTSwiftInstrumentor` в папку `.dynatrace` и убедитесь, что файл является исполняемым.
4. Закройте Xcode и выполните `.dynatrace/DTSwiftInstrumentor install <PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`.

При возникновении ошибки во время установки проверьте журнал сборки Xcode или журнал инструментирования для получения подробной информации. Дополнительные подсказки см. в разделе [Mobile applications: Issues with SwiftUI instrumentation](https://dt-url.net/yh638kl) сообщества Dynatrace.

При сборке приложения используйте схему, для которой выполнялось инструментирование.

### Обновление instrumentor

При выходе новой версии SwiftUI instrumentor её можно установить через Homebrew или вручную.

Homebrew

Вручную

После выпуска новые версии instrumentor загружаются через добавленный tap.

Выполните `brew update` и `brew upgrade DTSwiftInstrumentor`, чтобы обновить SwiftUI instrumentor.

1. Загрузите и распакуйте ZIP-файл с новой версией SwiftUI instrumentor. Ссылка доступна в [мастере инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.").
2. Скопируйте загруженный `DTSwiftInstrumentor` в папку `.dynatrace`, заменив существующий файл.

Если отображается следующее предупреждение сборки, необходимо также обновить скрипты сборки, интегрированные при установке Dynatrace SwiftUI instrumentor.

```
Dynatrace: There is an upgrade for your project instrumentation. Please execute "DTSwiftInstrumentor project-upgrade <PROJECT.xcodeproj>" to upgrade your project
```

Выполните предложенную команду для обновления скриптов сборки, а затем сохраните изменения в файле проекта.

### Удаление instrumentor

Если Dynatrace SwiftUI instrumentor больше не нужен, его можно удалить через Homebrew или вручную из проекта.

Homebrew

Вручную

Выполните `brew remove DTSwiftInstrumentor` и `brew untap dynatrace/tools`, чтобы удалить SwiftUI instrumentor из системы.

1. Выполните `DTSwiftInstrumentor uninstall`, чтобы удалить SwiftUI instrumentor из проекта.

   * Опционально. Также можно указать `<PROJECT.xcodeproj>`. Если данные проекта не указаны, инструмент попытается автоматически определить и запустит интерактивный выбор.
2. Опционально. Удалите папки `.dynatrace` и `dynatrace_instrumented` из проекта.

   Эти папки содержат кэш, данные журналов и, если применимо, вручную настроенный бинарный файл instrumentor.

## Просмотр разницы инструментирования SwiftUI

OneAgent for iOS версии 8.257+

Для проверки разницы между оригинальным кодом и кодом, изменённым SwiftUI instrumentor, выполните одну из следующих команд:

* Из корня проекта:

  + `DTSwiftInstrumentor diff` при установке instrumentor через Homebrew
  + `.dynatrace/DTSwiftInstrumentor diff` при ручной установке
* Из любой директории:

  + `DTSwiftInstrumentor diff <root-project-dir-path>`

## Известные ограничения

### Инструментирование пользовательских элементов управления SwiftUI не поддерживается

В настоящее время Dynatrace не поддерживает инструментирование пользовательских элементов управления SwiftUI. Список поддерживаемых элементов см. в разделе [Поддерживаемые элементы управления](#supported-controls).

### Проблема с превью в Xcode

При включении инструментирования SwiftUI в сборку для симулятора превью не загружались в Xcode. В качестве обходного решения инструментирование SwiftUI для сборок симулятора отключено. Для добавления инструментирования SwiftUI в сборки симулятора см. раздел [Инструментирование сборок симулятора](#instrument-simulator-builds).

### Только SwiftUI 2.0+

Dynatrace поддерживает инструментирование SwiftUI 2.0+, так как listener `onChange` недоступен в более ранних версиях SwiftUI. По этой причине цель развёртывания должна быть iOS 14+.

### Увеличенное время сборки

В отличие от OneAgent for iOS, который модифицирует мобильное приложение в памяти во время выполнения, SwiftUI instrumentor изменяет исходный код проекта во время сборки. По этой причине процесс инструментирования SwiftUI заметно влияет на время сборки.

Для уменьшения времени сборки:

* Выполняйте сборку только для **Device**. Если вы решили [инструментировать сборки симулятора](#instrument-simulator-builds), отключите эту функцию.
* Не запускайте инструментирование SwiftUI при каждой возможной сборке. Рекомендуется запускать инструментирование SwiftUI на ветках типа `main` или `release`.

### Несовместимость с watchOS

Невозможно скомпилировать проект, содержащий файлы, добавленные в цель watchOS, поскольку OneAgent for watchOS не существует. В этом случае [вручную исключите](#exclude-swift-files) все файлы, общие с целью watchOS или являющиеся её частью.

### tvOS не поддерживается

В настоящее время официальная поддержка сборок SwiftUI для tvOS отсутствует.

## Метки элементов управления SwiftUI

Если не указано иное, Dynatrace SwiftUI instrumentor пытается получить имя каждого элемента управления, рекурсивно ища строковые литералы или переменные, указанные в качестве заголовка.
В примере ниже instrumentor извлечёт `"Login"` в качестве метки кнопки:

```
Button("Login", action: {



/* perform login */



})
```

Извлечённая метка будет использована для сообщения автоматического действия `"Touch on Login"` при взаимодействии пользователя с кнопкой.

В следующем примере взаимодействие пользователя с кнопкой будет сообщено как `"Touch on bookmark"`:

```
Button(action: {



print("Hello world!")



}) {



Image("bookmark")



}
```

### Использование имени элемента управления по умолчанию

Используйте модификатор `withCustomInstrumentationConfig(.useDefaultControlName)`, чтобы задать метку элемента управления в формате `<Control type>_<index>`:

```
Button("Login", action: {



/* perform login */



}).withCustomInstrumentationConfig(.useDefaultControlName)
```

При применении модификатора instrumentor сообщит о действии касания как `"Touch on Button_0"`.

### Подавление сообщения о переменных состояния

Используйте модификатор `withCustomInstrumentationConfig(.doNotReportStateVariable)`, чтобы запретить instrumentor сообщать об изменениях переменных `@State` для конкретного элемента управления:

```
Toggle("Dark mode", isOn: $isDarkMode)



.withCustomInstrumentationConfig(.doNotReportStateVariable)
```

При применении модификатора instrumentor не будет сообщать об изменениях переменных состояния для этого элемента управления.

### Использование пользовательского имени элемента управления

Используйте модификатор `withCustomInstrumentationConfig(.useControlName(<Name>)`, чтобы указать пользовательскую метку для определённого элемента управления:

```
Button("Login", action: {



/* perform login */



}).withCustomInstrumentationConfig(.useControlName("Login Button"))
```

При таком подходе каждое касание кнопки будет сообщаться как `"Touch on Login Button"`.

## Настройка инструментирования SwiftUI

### Включение Session Replay on crashes

Session Replay on crashes может захватывать и визуально воспроизводить действия пользователя приложения, выполненные до [сбоя](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий, захватываемых Dynatrace.").

Для включения этой функции см. [Включение Session Replay для SwiftUI-приложений](/managed/observe/digital-experience/session-replay/session-replay-ios#sr-swiftui "Требования и процедура включения Session Replay для iOS-приложений.").

### Глобальное исключение элементов управления из инструментирования SwiftUI

OneAgent for iOS версии 8.263+

Dynatrace SwiftUI instrumentor инструментирует все элементы UI, перечисленные в разделе [Поддерживаемые элементы управления](#supported-controls). При необходимости можно глобально исключить определённые элементы управления из процесса инструментирования SwiftUI.

Для глобального исключения элементов управления из инструментирования SwiftUI добавьте [конфигурационный ключ `DTXSwiftUIExcludedControls`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") проекта.

```
<key>DTXSwiftUIExcludedControls</key>



<array>



<string>Button</string>



<string>Slider</string>



</array>
```

### Локальное исключение элементов управления из инструментирования SwiftUI

OneAgent for iOS версии 8.263+

С помощью функции `withCustomInstrumentationConfig(.skipInstrumentation)` можно локально исключить элементы управления из инструментирования SwiftUI.

В отличие от [конфигурационного ключа `DTXSwiftUIExcludedControls`](#exclude-controls-global), позволяющего исключить инструментирование всех экземпляров указанного типа элемента управления, функция `withCustomInstrumentationConfig(.skipInstrumentation)` может использоваться для исключения конкретного экземпляра типа элемента управления. Эту функцию можно применять непосредственно к элементу управления или, для исключения нескольких экземпляров, к контейнеру.

Следуйте этим рекомендациям при применении функции `withCustomInstrumentationConfig(.skipInstrumentation)`:

* Для использования функции сначала добавьте оператор импорта `import Dynatrace`.
* Добавьте `withCustomInstrumentationConfig(.skipInstrumentation)` в качестве последнего модификатора в список модификаторов представления. Например:

  ```
  Button("Login", action: { /* perform login */ })



  .padding()



  .background(Color.red)



  .frame(width: 40)



  .withCustomInstrumentationConfig(.skipInstrumentation)
  ```

#### Исключение одного элемента управления

Используйте следующий код для локального исключения одного элемента управления из инструментирования SwiftUI:

```
import Dynatrace



...



Button("Login", action: { /* perform login */ })



.withCustomInstrumentationConfig(.skipInstrumentation)
```

#### Исключение нескольких элементов управления

Для локального исключения группы элементов управления примените функцию `withCustomInstrumentationConfig(.skipInstrumentation)` к их родительскому контейнеру.

```
import Dynatrace



...



HStack {



Button("Login", action: { /* perform login */ })



Button("Register", action: { /* perform registration */ })



}.withCustomInstrumentationConfig(.skipInstrumentation)
```

### Исключение файлов из инструментирования SwiftUI

По умолчанию Dynatrace SwiftUI instrumentor обрабатывает все файлы с расширением `.swift`, но инструментирует только файлы, содержащие [поддерживаемые элементы управления](#supported-controls). При необходимости можно исключить определённые файлы и директории из процесса инструментирования SwiftUI.

Для исключения файлов и директорий из инструментирования SwiftUI:

1. Добавьте [конфигурационный ключ `DTXExcludedSwiftUIFiles`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") проекта.
2. Перечислите относительные пути всех файлов и директорий, которые не нужно инструментировать. Пути должны быть относительными к корню проекта, то есть директории с файлом `.xcodeproj`.

   ```
   <key>DTXExcludedSwiftUIFiles</key>



   <array>



   <string>relative/file/path/</string>



   <string>relative/file.swift</string>



   </array>
   ```

Журнал инструментирования, доступный после каждой сборки, содержит список файлов и директорий, которые следует исключить из инструментирования SwiftUI. В журнале также указывается, был ли файл или директория исключены в процессе инструментирования.

### Инструментирование сборок симулятора

Инструментирование SwiftUI для сборок симулятора отключено во избежание [проблемы с превью в Xcode](#issue-preview-xcode).

Для включения инструментирования SwiftUI в сборках симулятора добавьте [конфигурационный ключ `DTXSwiftUIInstrumentSimulatorBuilds`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") проекта и установите этот ключ в значение `true`.

```
<key>DTXSwiftUIInstrumentSimulatorBuilds</key>



<true/>
```

### Создание сборок для неподдерживаемых целевых версий развёртывания

Наш SwiftUI instrumentor генерирует код, совместимый с SwiftUI 2.0+, который работает только на устройствах с iOS 14+. Попытка создать сборки для целевых версий развёртывания iOS 13 и более ранних завершится ошибкой.

Для переопределения этой проверки добавьте [конфигурационный ключ `DTXSwiftUIIgnoreDeploymentTarget`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") проекта и установите его в значение `true`.

```
<key>DTXSwiftUIIgnoreDeploymentTarget</key>



<true/>
```

### Включение маппинга номеров строк для проектов на Objective-C

Отчёты о сбоях в Dynatrace основаны не на исходном коде проекта, а на изменённом коде, генерируемом Dynatrace в процессе инструментирования. Поэтому в проект добавляется маппинг номеров строк, который передаётся в Dynatrace при запуске приложения. В противном случае номера строк в отчётах о сбоях будут некорректными.

По умолчанию Dynatrace SwiftUI instrumentor генерирует маппинг номеров строк и вставляет его в главный класс проекта. Это происходит автоматически для проектов с главным классом на Swift, но не для устаревших проектов на Objective-C. Для таких проектов возникнет ошибка, и SwiftUI instrumentor не выполнит инструментирование мобильного приложения.

Для включения маппинга номеров строк в проектах на Objective-C:

1. Добавьте [конфигурационный ключ `DTXSwiftUIManualPlaceholder`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") проекта и установите его в значение `true`.

   ```
   <key>DTXSwiftUIManualPlaceholder</key>



   <true/>
   ```
2. Добавьте специальный плейсхолдер `AppDelegate.m` в главный класс.
3. Добавьте строку `[Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];` в главный класс в метод `init` или `didFinishLaunchingWithOptions` (не в оба).

   didFinishLaunchingWithOptions

   init

   ```
   - (BOOL)application:(UIApplication *)application



   didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {



   [Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];



   // ... your existing setup code



   return YES;



   }
   ```

   ```
   - (instancetype)init {



   self = [super init];



   if (self) {



   [Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];



   }



   return self;



   }
   ```

   В процессе сборки SwiftUI instrumentor заменяет часть этой строки сгенерированным маппингом номеров строк.

### Включение автоматической очистки журналов

OneAgent for iOS версии 8.257+

После каждой сборки SwiftUI instrumentor создаёт резервные копии инструментированных файлов и сгенерированные журналы, хранящиеся в директории `dynatrace_instrumented`. По умолчанию эти файлы не удаляются, и общий размер директории будет со временем увеличиваться. По этой причине рекомендуется включить автоматическую очистку журналов.

* Для удаления журналов SwiftUI instrumentor после определённого количества сборок добавьте [конфигурационный ключ `DTXCleanSwiftUILogsByCount`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") проекта.

  ```
  <key>DTXCleanSwiftUILogsByCount</key>



  <number>10</number>
  ```
* Для удаления журналов через определённое количество дней добавьте [конфигурационный ключ `DTXCleanSwiftUILogsByAgeDays`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл `Info.plist`.

  ```
  <key>DTXCleanSwiftUILogsByAgeDays</key>



  <number>5</number>
  ```

При добавлении обоих ключей в файл `Info.plist` приоритет имеет ключ `DTXCleanSwiftUILogsByAgeDays`.

## Устранение неполадок

Мы продолжаем совершенствовать процесс инструментирования SwiftUI. При возникновении проблем с инструментированием элементов управления SwiftUI обратитесь к разделу [Mobile applications: Issues with SwiftUI instrumentation](https://dt-url.net/yh638kl) сообщества Dynatrace.