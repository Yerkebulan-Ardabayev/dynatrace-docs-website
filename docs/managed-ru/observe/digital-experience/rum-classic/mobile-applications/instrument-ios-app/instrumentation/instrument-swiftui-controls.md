---
title: Инструментирование элементов управления SwiftUI в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls
---

# Инструментирование элементов управления SwiftUI в RUM Classic

# Инструментирование элементов управления SwiftUI в RUM Classic

* Практическое руководство
* Чтение займёт 13 минут
* Обновлено 10 июля 2026 г.

OneAgent для iOS версии 8.249+

После [инструментирования мобильного приложения с помощью OneAgent для iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.") может также понадобиться инструментировать элементы управления SwiftUI приложения. На этой странице приведена дополнительная информация о том, как настроить проект, обновить инструментатор SwiftUI, обойти некоторые известные ограничения и многое другое.

Для инструментирования элементов управления SwiftUI инструментатор SwiftUI добавляет дополнительный код в исходный код проекта (файлы `*.swift`) во время процесса сборки. Этот код отслеживает состояние элементов UI и уведомляет OneAgent для iOS о любых изменениях. После завершения процесса сборки все изменения в исходном коде проекта отменяются.

Подробную информацию о действиях, выполняемых инструментатором SwiftUI, и копию изменённых файлов кода можно найти в каталоге `dynatrace_instrumented`. Инструментатор SwiftUI создаёт резервные копии инструментированных файлов и сформированных журналов в формате ZIP-архива.

## Требования

* SwiftUI версии 2.0+
* iOS 14+
* [OneAgent для iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.")

## Поддерживаемые элементы управления

Поддерживается инструментирование следующих элементов управления и представлений SwiftUI.

OneAgent для iOS версии 8.249+

* [`Button`﻿](https://developer.apple.com/documentation/swiftui/button)
* [`Stepper`﻿](https://developer.apple.com/documentation/swiftui/stepper)
* [`Picker`﻿](https://developer.apple.com/documentation/swiftui/picker)
* [`Toggle`﻿](https://developer.apple.com/documentation/swiftui/toggle)
* [`Slider`﻿](https://developer.apple.com/documentation/swiftui/slider)

OneAgent для iOS версии 8.265+

* [`PasteButton`﻿](https://developer.apple.com/documentation/swiftui/pastebutton)
* [`EditButton`﻿](https://developer.apple.com/documentation/swiftui/editbutton)
* [`RenameButton`﻿](https://developer.apple.com/documentation/swiftui/renamebutton)
* [`Link`﻿](https://developer.apple.com/documentation/swiftui/link)
* [`ShareLink`﻿](https://developer.apple.com/documentation/swiftui/sharelink)
* [`NavigationLink`﻿](https://developer.apple.com/documentation/swiftui/navigationlink)
* [`DatePicker`﻿](https://developer.apple.com/documentation/swiftui/datepicker)
* [`MultiDatePicker`﻿](https://developer.apple.com/documentation/swiftui/multidatepicker)
* [`ColorPicker`﻿](https://developer.apple.com/documentation/swiftui/colorpicker)
* [`TabView`﻿](https://developer.apple.com/documentation/swiftui/tabview)
* [`List`﻿](https://developer.apple.com/documentation/swiftui/list)

OneAgent для iOS версии 8.269+

* [`Menu`﻿](https://developer.apple.com/documentation/swiftui/menu)
* [`WindowGroup`﻿](https://developer.apple.com/documentation/swiftui/windowgroup)

При необходимости можно [глобально](#exclude-controls-global) или [локально исключить определённые элементы управления из процесса инструментирования SwiftUI](#exclude-controls-local).

## Поддерживаемые методы

OneAgent для iOS версии 8.265+

Поддерживается инструментирование следующих методов SwiftUI:

* [`onTapGesture(count:perform:)`﻿](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:))
* [`onTapGesture(count:coordinateSpace:perform:)`﻿](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:))
* [`refreshable(action:)`﻿](https://developer.apple.com/documentation/swiftui/view/refreshable(action:))
* [`sheet(isPresented:onDismiss:content:)`﻿](https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))
* [`sheet(item:onDismiss:content:)`﻿](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:))
* [`popover(isPresented:attachmentAnchor:arrowEdge:content:)`﻿](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:))
* [`popover(item:attachmentAnchor:arrowEdge:content:)`﻿](https://developer.apple.com/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))
* [`navigationDestination(for:destination:)`﻿](https://developer.apple.com/documentation/swiftui/view/navigationdestination(for:destination:))
* [`renameAction(_:)`﻿](https://developer.apple.com/documentation/swiftui/view/renameaction(_:))

Следующие данные передаются каждый раз при выполнении замыкания одного из поддерживаемых методов:

* Название метода
* Тип представления, к которому был прикреплён метод
* Название родительского представления

## Мониторинг жизненного цикла

OneAgent для iOS версии 8.265+

Инструментатор SwiftUI собирает данные о следующих событиях:

* **Запуск приложения**
* **Отображение**: [`onAppear`﻿](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) любого представления SwiftUI, показанного из элемента управления [`NavigationLink`﻿](https://developer.apple.com/documentation/swiftui/navigationlink) или [`TabView`﻿](https://developer.apple.com/documentation/swiftui/tabview)
* **Повторное отображение**: [`onAppear`﻿](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) любого представления SwiftUI, показанного из элемента управления [`NavigationLink`﻿](https://developer.apple.com/documentation/swiftui/navigationlink) или [`TabView`﻿](https://developer.apple.com/documentation/swiftui/tabview)

## Необходимые шаги

Для инструментирования элементов управления SwiftUI приложения убедитесь, что выполнены следующие шаги:

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создать приложение в Dynatrace**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#create-app-in-ui "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настроить OneAgent для проекта**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#set-up-oneagent "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Установить инструментатор SwiftUI**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#install-instrumentor "Использование инструментатора SwiftUI Dynatrace для мониторинга SwiftUI-приложений.")

## Управление инструментатором SwiftUI

### Установка инструментатора

Чтобы инструментировать элементы управления SwiftUI приложения, нужно установить SwiftUI-инструментатор Dynatrace. Сделать это можно через Homebrew или вручную.

[OneAgent for iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.") уже должен быть настроен для проекта. Также не забудьте сделать резервную копию проекта перед установкой инструментатора.

Homebrew

Вручную

1. Выполните `brew tap dynatrace/tools`, чтобы добавить один из тапов Dynatrace.
2. Требуется **только для Homebrew 6.0.0 и новее.** Выполните `brew trust dynatrace/tools/DTSwiftInstrumentor`, чтобы явно доверять формулам. Начиная с Homebrew 6.0.0, Homebrew требует доверять формулам из неофициальных тапов перед установкой в качестве меры безопасности цепочки поставок. Подробнее см. [Homebrew Tap Trust﻿](https://docs.brew.sh/Tap-Trust). Этот шаг безопасно выполнять и на более ранних версиях Homebrew.
3. Выполните `brew install DTSwiftInstrumentor`, чтобы установить наш SwiftUI-инструментатор.
4. Закройте Xcode и выполните `DTSwiftInstrumentor install`.

   * Необязательно Дополнительно можно указать `<PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`. Если данные проекта не указаны, инструмент пытается автоматически обнаружить доступные таргеты и схемы и запускает интерактивный выбор.

1. Скачайте и распакуйте ZIP-файл, содержащий наш SwiftUI-инструментатор. Ссылка доступна в [мастере мобильной инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
2. Создайте папку `.dynatrace` в корне проекта, на том же уровне, что и файл `*.xcodeproj`.

   Если появляется системное предупреждение о том, что нельзя создать папку с именем, начинающимся с точки, сделайте одно из следующего:

   * В терминале выполните `mkdir .dynatrace` внутри корня проекта, чтобы создать папку `.dynatrace`.
   * В терминале выполните `defaults write com.apple.finder AppleShowAllFiles true` и `killall Finder`, чтобы показать скрытые папки и файлы. Затем создайте папку `.dynatrace` в Finder.

     Также можно выполнить `defaults write com.apple.finder AppleShowAllFiles false` и `killall Finder`, чтобы снова скрыть скрытые папки и файлы.
3. Скопируйте скачанный `DTSwiftInstrumentor` в папку `.dynatrace` и убедитесь, что файл исполняемый.
4. Закройте Xcode и выполните `.dynatrace/DTSwiftInstrumentor install <PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`.

Если во время внедрения возникает ошибка, проверьте лог сборки Xcode или лог инструментации на предмет подробной информации об ошибке. Дополнительные подсказки см. в [Mobile applications: Issues with SwiftUI instrumentation﻿](https://dt-url.net/yh638kl) в сообществе Dynatrace.

При сборке приложения нужно использовать ту схему, которую вы инструментировали.

### Обновление инструментатора

Когда становится доступна новая версия SwiftUI-инструментатора, обновить её можно через Homebrew или вручную.

Homebrew

Вручную

После релиза новые версии инструментатора загружаются через добавленный тап.

Выполните `brew update` и `brew upgrade DTSwiftInstrumentor`, чтобы обновить наш SwiftUI-инструментатор.

1. Скачайте и распакуйте ZIP-файл, содержащий новую версию SwiftUI-инструментатора. Ссылка доступна в [мастере мобильной инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
2. Скопируйте скачанный `DTSwiftInstrumentor` в папку `.dynatrace`, заменив существующий файл.

Если появляется следующее предупреждение сборки, также нужно обновить скрипты сборки, которые были интегрированы во время установки SwiftUI-инструментатора Dynatrace.

```
Dynatrace: There is an upgrade for your project instrumentation. Please execute "DTSwiftInstrumentor project-upgrade <PROJECT.xcodeproj>" to upgrade your project
```

Выполните предложенную команду, чтобы обновить скрипты сборки, а затем сохраните изменения, внесённые в файл проекта.

### Удаление инструментатора

Если SwiftUI-инструментатор Dynatrace больше не нужен, его можно удалить из системы через Homebrew, либо вручную убрать из проекта.

Homebrew

Вручную

Выполните `brew remove DTSwiftInstrumentor` и `brew untap dynatrace/tools`, чтобы удалить наш SwiftUI-инструментатор из системы.

1. Выполните `DTSwiftInstrumentor uninstall`, чтобы удалить SwiftUI-инструментатор из проекта.

   * Необязательно Дополнительно можно указать `<PROJECT.xcodeproj>`. Если данные проекта не указаны, инструмент пытается выполнить автоматическое обнаружение и запускает интерактивный выбор.
2. Необязательно Удалите папки `.dynatrace` и `dynatrace_instrumented` из проекта.

   Эти папки содержат кэш, данные логов и, если применимо, бинарный файл инструментатора, установленный вручную.
   Эти папки содержат кэш инструментатора, данные логов и, если применимо, бинарные файлы инструментатора.

## Проверка diff инструментации SwiftUI

OneAgent for iOS версии 8.257+

Чтобы проверить разницу между исходным кодом и кодом, изменённым SwiftUI-инструментатором, выполните одну из следующих команд:

* Из корня проекта:

  + `DTSwiftInstrumentor diff`, если инструментатор установлен через Homebrew
  + `.dynatrace/DTSwiftInstrumentor diff`, если инструментатор установлен вручную
* Из любого каталога

  + `DTSwiftInstrumentor diff <root-project-dir-path>`

## Известные ограничения

### Инструментация пользовательских элементов управления SwiftUI не поддерживается

В настоящее время Dynatrace не поддерживает инструментацию пользовательских элементов управления SwiftUI. Список элементов управления SwiftUI, которые можно инструментировать, см. в [Поддерживаемые элементы управления](#supported-controls).

### Проблема с превью в Xcode

Когда сборка для симулятора включала инструментацию SwiftUI, превью не загружались в Xcode. В качестве обходного решения мы отключили инструментацию SwiftUI для сборок симулятора. Если нужно добавить инструментацию SwiftUI в сборки симулятора, см. [Инструментация сборок симулятора](#instrument-simulator-builds).

### Только SwiftUI 2.0+

Dynatrace поддерживает инструментацию SwiftUI 2.0+, поскольку слушатель `onChange` недоступен в более ранних релизах SwiftUI. По этой причине целевая версия развёртывания должна быть iOS 14+.

### Более длительное время сборки

В отличие от OneAgent for iOS, который изменяет мобильное приложение в памяти во время выполнения, SwiftUI-инструментатор изменяет исходный код проекта во время сборки. По этой причине процесс инструментации SwiftUI заметно влияет на время сборки.

Чтобы уменьшить время сборки

* Собирайте только для **Device**. Если вы решили [инструментировать сборки симулятора](#instrument-simulator-builds), отключите эту функцию.
* Не запускайте инструментацию SwiftUI при каждой возможной сборке. Рекомендуется запускать инструментацию SwiftUI на ветках вроде `main` или `release`.

### Несовместимость с watchOS

Невозможно скомпилировать проект, содержащий файлы, добавленные в таргет watchOS, поскольку OneAgent for watchOS не существует. В этом случае [вручную исключите](#exclude-swift-files) все файлы, которые являются общими с таргетом watchOS или частью него.

### tvOS не поддерживается

В настоящее время официальная поддержка сборок tvOS SwiftUI отсутствует.

## Метки элементов управления SwiftUI

Если не указано иное, SwiftUI-инструментатор Dynatrace пытается получить имя каждого элемента управления, рекурсивно выполняя поиск строковых литералов или переменных, указанных в качестве заголовка.
В примере ниже инструментатор извлечёт `"Login"` в качестве метки для кнопки:

```
Button("Login", action: {



/* perform login */



})
```

Извлечённая метка будет использована для отправки авто-действия `"Touch on Login"`, когда пользователь взаимодействует с кнопкой.

В следующем примере взаимодействие пользователя с этой кнопкой будет отправлено как `"Touch on bookmark"`:

```
Button(action: {



print("Hello world!")



}) {



Image("bookmark")



}
```

### Использование имени элемента управления по умолчанию

Используйте модификатор `withCustomInstrumentationConfig(.useDefaultControlName)`, чтобы задать метке элемента управления значение `<Control type>_<index>`:

```
Button("Login", action: {



/* perform login */



}).withCustomInstrumentationConfig(.useDefaultControlName)
```

При применении этого модификатора инструментатор отправит действие касания как `"Touch on Button_0"`.

### Подавление отчётности переменной состояния

Используйте модификатор `withCustomInstrumentationConfig(.doNotReportStateVariable)`, чтобы предотвратить отправку инструментатором изменений переменных `@State` для конкретного элемента управления:

```
Toggle("Dark mode", isOn: $isDarkMode)



.withCustomInstrumentationConfig(.doNotReportStateVariable)
```

При применении этого модификатора изменения переменной состояния для этого элемента управления отправляться не будут.

### Использование пользовательского имени элемента управления

Используйте модификатор `withCustomInstrumentationConfig(.useControlName(<Name>)`, чтобы указать пользовательскую метку для определённого элемента управления следующим образом:

```
Button("Login", action: {



/* perform login */



}).withCustomInstrumentationConfig(.useControlName("Login Button"))
```

Таким образом, каждое касание кнопки будет отправлено как `"Touch on Login Button"`.

## Настройка инструментации SwiftUI

### Включение Session Replay при сбоях

Session Replay при сбоях может фиксировать и визуально воспроизводить действия, которые пользователь приложения выполнял перед тем, как произошёл [сбой](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Чтобы включить эту функцию, см. [Включение Session Replay для приложений SwiftUI](/managed/observe/digital-experience/session-replay/session-replay-ios#sr-swiftui "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.").

### Глобальное исключение элементов управления из инструментации SwiftUI

OneAgent для iOS версии 8.263+

Инструментатор SwiftUI Dynatrace инструментирует все элементы UI, перечисленные в разделе [Supported controls](#supported-controls). При необходимости можно глобально исключить определённые элементы управления из процесса инструментирования SwiftUI.

Чтобы глобально исключить элементы управления из инструментирования SwiftUI, добавь ключ конфигурации [`DTXSwiftUIExcludedControls`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") проекта.

```
<key>DTXSwiftUIExcludedControls</key>



<array>



<string>Button</string>



<string>Slider</string>



</array>
```

### Локальное исключение элементов управления из инструментирования SwiftUI

OneAgent для iOS версии 8.263+

С помощью функции `withCustomInstrumentationConfig(.skipInstrumentation)` можно локально исключить элементы управления из инструментирования SwiftUI.

В отличие от [ключа конфигурации `DTXSwiftUIExcludedControls`](#exclude-controls-global), который позволяет предотвратить инструментирование всех экземпляров указанного типа элемента управления, функцию `withCustomInstrumentationConfig(.skipInstrumentation)` можно использовать для исключения конкретного экземпляра типа элемента управления. Эту функцию можно применить напрямую к элементу управления или, для исключения нескольких экземпляров элементов управления, к контейнеру.

При применении функции `withCustomInstrumentationConfig(.skipInstrumentation)` нужно придерживаться следующих указаний:

* Чтобы использовать функцию, сначала добавь инструкцию импорта `import Dynatrace`.
* Добавь `withCustomInstrumentationConfig(.skipInstrumentation)` в качестве последнего модификатора в списке модификаторов представления. Например:

  ```
  Button("Login", action: { /* perform login */ })



  .padding()



  .background(Color.red)



  .frame(width: 40)



  .withCustomInstrumentationConfig(.skipInstrumentation)
  ```

#### Исключение одного элемента управления

Используй следующий код, чтобы локально исключить один элемент управления из инструментирования SwiftUI:

```
import Dynatrace



…



Button("Login", action: { /* perform login */ })



.withCustomInstrumentationConfig(.skipInstrumentation)
```

#### Исключение нескольких элементов управления

Чтобы локально исключить группу элементов управления, примени функцию `withCustomInstrumentationConfig(.skipInstrumentation)` к их родительскому контейнеру.

```
import Dynatrace



…



HStack {



Button("Login", action: { /* perform login */ })



Button("Register", action: { /* perform registration */ })



}.withCustomInstrumentationConfig(.skipInstrumentation)
```

### Исключение файлов из инструментирования SwiftUI

По умолчанию инструментатор SwiftUI Dynatrace обрабатывает все файлы с расширением `.swift`, но инструментирует только те файлы, которые содержат [поддерживаемые элементы управления](#supported-controls). При необходимости можно исключить определённые файлы и каталоги из процесса инструментирования SwiftUI.

Чтобы исключить файлы и каталоги из инструментирования SwiftUI

1. Добавь ключ конфигурации [`DTXExcludedSwiftUIFiles`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") проекта.
2. Перечисли относительные пути ко всем файлам и каталогам, которые не нужно инструментировать. Пути должны быть указаны относительно корня проекта, то есть каталога, в котором находится файл `.xcodeproj`.

   ```
   <key>DTXExcludedSwiftUIFiles</key>



   <array>



   <string>relative/file/path/</string>



   <string>relative/file.swift</string>



   </array>
   ```

Журнал инструментирования, доступный после каждой сборки, содержит список файлов и каталогов, которые следует исключить из инструментирования SwiftUI. Журнал инструментирования также показывает, был ли файл или каталог исключён в процессе инструментирования.

### Инструментирование сборок для симулятора

Инструментирование SwiftUI для сборок симулятора отключено, чтобы избежать [проблемы с превью в Xcode](#issue-preview-xcode).

Чтобы включить инструментирование SwiftUI для сборок симулятора, добавь ключ конфигурации [`DTXSwiftUIInstrumentSimulatorBuilds`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") проекта и установи для этого ключа значение `true`.

```
<key>DTXSwiftUIInstrumentSimulatorBuilds</key>



<true/>
```

### Создание сборок для неподдерживаемых целей развёртывания

Инструментатор SwiftUI генерирует код, совместимый с SwiftUI 2.0+, который работает только на устройствах с iOS 14+. Попытка сгенерировать сборки для целей развёртывания iOS 13 и более ранних версий завершится ошибкой.

Чтобы отменить эту проверку, добавь ключ конфигурации [`DTXSwiftUIIgnoreDeploymentTarget`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") проекта и установи для этого ключа значение `true`.

```
<key>DTXSwiftUIIgnoreDeploymentTarget</key>



<true/>
```

### Включение сопоставления номеров строк для проектов Objective-C

Отчёты о сбоях, доступные в Dynatrace, основаны не на исходном коде проекта. Эти отчёты основаны на изменённом коде, который генерирует Dynatrace во время инструментирования. Поэтому во время инструментирования в проект добавляется сопоставление номеров строк, которое впоследствии передаётся в Dynatrace при запуске приложения. В противном случае номера строк в отчётах о сбоях были бы неверными.

По умолчанию инструментатор SwiftUI Dynatrace генерирует сопоставление номеров строк и вставляет его в главный класс проекта. Это происходит автоматически для проектов с главным классом на Swift, но не для устаревших проектов на Objective-C. Для таких проектов появится ошибка, и инструментатор SwiftUI не будет инструментировать мобильное приложение.

Чтобы включить сопоставление номеров строк для проектов Objective-C

1. Добавь ключ конфигурации [`DTXSwiftUIManualPlaceholder`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") проекта и установи для этого ключа значение `true`.

   ```
   <key>DTXSwiftUIManualPlaceholder</key>



   <true/>
   ```
2. Добавь специальный placeholder `AppDelegate.m` в главный класс.
3. Добавь строку `[Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];` в главный класс либо в метод `init`, либо в метод `didFinishLaunchingWithOptions` (не в оба сразу).

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

   Во время сборки инструментатор SwiftUI заменяет часть этой строки сгенерированным сопоставлением номеров строк.

### Включение автоматической очистки журналов

OneAgent для iOS версии 8.257+

После каждой сборки SwiftUI instrumentor создаёт резервные копии инструментированных файлов и сгенерированные логи, которые хранятся в `dynatrace_instrumented`. По умолчанию эти файлы не удаляются, и общий размер каталога со временем растёт. По этой причине рекомендуется включить автоматическую очистку логов.

* Чтобы удалять логи SwiftUI instrumentor после определённого числа сборок, добавьте [ключ конфигурации `DTXCleanSwiftUILogsByCount`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") вашего проекта.

  ```
  <key>DTXCleanSwiftUILogsByCount</key>



  <number>10</number>
  ```
* Чтобы удалять логи после определённого числа дней, добавьте [ключ конфигурации `DTXCleanSwiftUILogsByAgeDays`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в файл `Info.plist`.

  ```
  <key>DTXCleanSwiftUILogsByAgeDays</key>



  <number>5</number>
  ```

Если добавить оба ключа в файл `Info.plist`, приоритет имеет ключ `DTXCleanSwiftUILogsByAgeDays`.

## Устранение неполадок

Мы всё ещё работаем над улучшением процесса инструментирования SwiftUI. Если при инструментировании элементов управления SwiftUI возникают проблемы, обратитесь к разделу [Mobile applications: Issues with SwiftUI instrumentation﻿](https://dt-url.net/yh638kl) в сообществе Dynatrace.