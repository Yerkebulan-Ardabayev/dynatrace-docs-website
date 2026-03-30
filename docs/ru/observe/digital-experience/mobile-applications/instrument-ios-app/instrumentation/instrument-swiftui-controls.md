---
title: Инструментирование элементов управления SwiftUI
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls
scraped: 2026-03-05T21:25:19.171690
---

* 13 мин чтения

OneAgent для iOS версии 8.249+

После инструментирования вашего мобильного приложения с помощью OneAgent для iOS, вы также можете захотеть инструментировать элементы управления SwiftUI вашего приложения. Эта страница предоставляет дополнительную информацию о том, как настроить ваш проект, обновить инструментор SwiftUI, преодолеть известные ограничения и многое другое.

Для инструментирования элементов управления SwiftUI наш инструментор SwiftUI добавляет дополнительный код в исходный код вашего проекта (файлы `*.swift`) в процессе сборки. Этот код отслеживает состояние элементов пользовательского интерфейса и уведомляет OneAgent для iOS о любых обновлениях. После завершения процесса сборки все изменения в исходном коде вашего проекта отменяются.

Для получения подробной информации о действиях, выполняемых инструментором SwiftUI, и копии изменённых файлов кода проверьте каталог `dynatrace_instrumented`. Инструментор SwiftUI создаёт резервные копии инструментированных файлов и сгенерированных журналов в формате ZIP-архива.

## Требования

* SwiftUI версии 2.0+
* iOS 14+
* OneAgent для iOS

## Поддерживаемые элементы управления

Мы поддерживаем инструментирование следующих элементов управления и представлений SwiftUI.

OneAgent для iOS версии 8.249+

* [`Button`](https://developer.apple.com/documentation/swiftui/button)
* [`Stepper`](https://developer.apple.com/documentation/swiftui/stepper)
* [`Picker`](https://developer.apple.com/documentation/swiftui/picker)
* [`Toggle`](https://developer.apple.com/documentation/swiftui/toggle)
* [`Slider`](https://developer.apple.com/documentation/swiftui/slider)

OneAgent для iOS версии 8.265+

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

OneAgent для iOS версии 8.269+

* [`Menu`](https://developer.apple.com/documentation/swiftui/menu)

При необходимости вы можете [глобально](#exclude-controls-global) или [локально исключить определённые элементы управления из процесса инструментирования SwiftUI](#exclude-controls-local).

## Поддерживаемые методы

OneAgent для iOS версии 8.265+

Мы поддерживаем инструментирование следующих методов SwiftUI:

* [`onTapGesture(count:perform:)`](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:))
* [`onTapGesture(count:coordinateSpace:perform:)`](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:))
* [`refreshable(action:)`](https://developer.apple.com/documentation/swiftui/view/refreshable(action:))
* [`sheet(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))
* [`sheet(item:onDismiss:content:)`](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:))
* [`popover(isPresented:attachmentAnchor:arrowEdge:content:)`](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:))
* [`popover(item:attachmentAnchor:arrowEdge:content:)`](https://developer.apple.com/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))

При каждом выполнении замыкания одного из поддерживаемых методов сообщаются следующие данные:

* Имя метода
* Тип представления, к которому прикреплён метод
* Имя родительского представления

## Мониторинг жизненного цикла

OneAgent для iOS версии 8.265+

Инструментор SwiftUI собирает данные о следующих событиях:

* **Запуск приложения**
* **Отображение**: [`onAppear`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) любого представления SwiftUI, отображённого из элемента управления [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink) или [`TabView`](https://developer.apple.com/documentation/swiftui/tabview)
* **Повторное отображение**: [`onAppear`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) любого представления SwiftUI, отображённого из элемента управления [`NavigationLink`](https://developer.apple.com/documentation/swiftui/navigationlink) или [`TabView`](https://developer.apple.com/documentation/swiftui/tabview)

## Необходимые шаги

Чтобы инструментировать элементы управления SwiftUI вашего приложения, убедитесь, что вы выполнили следующие шаги:

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте приложение в Dynatrace**](dynatrace-auto-instrumentation-for-ios.md#create-app-in-ui "Настройте мониторинг пользовательского опыта для приложений iOS в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте OneAgent для вашего проекта**](dynatrace-auto-instrumentation-for-ios.md#set-up-oneagent "Настройте мониторинг пользовательского опыта для приложений iOS в Dynatrace.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Установите наш инструментор SwiftUI**](instrument-swiftui-controls.md#install-instrumentor "Используйте инструментор Dynatrace SwiftUI для мониторинга ваших приложений SwiftUI.")

## Управление инструментором SwiftUI

### Установка инструментора

Чтобы инструментировать элементы управления SwiftUI вашего приложения, установите инструментор Dynatrace SwiftUI. Это можно сделать через Homebrew или вручную.

OneAgent для iOS должен быть уже настроен для вашего проекта. Также не забудьте сделать резервную копию проекта перед установкой инструментора.

Homebrew

Вручную

1. Выполните `brew tap dynatrace/tools`, чтобы добавить один из тапов Dynatrace.
2. Выполните `brew install DTSwiftInstrumentor`, чтобы установить наш инструментор SwiftUI.
3. Закройте Xcode и выполните `DTSwiftInstrumentor install`.

   * Необязательно Дополнительно можно указать `<PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`. Если данные проекта не указаны, инструмент попытается автоматически определить доступные цели и схемы и запустить интерактивный выбор.

1. Загрузите и извлеките ZIP-файл, содержащий наш инструментор SwiftUI. Ссылка доступна в мастере инструментирования мобильных приложений.
2. Создайте папку `.dynatrace` в корне вашего проекта — на том же уровне, что и файл `*.xcodeproj`.

   Если вы получаете системное предупреждение о том, что невозможно создать папку с именем, начинающимся с точки, выполните одно из следующих действий:

   * В Terminal выполните `mkdir .dynatrace` внутри корня проекта, чтобы создать папку `.dynatrace`.
   * В Terminal выполните `defaults write com.apple.finder AppleShowAllFiles true` и `killall Finder`, чтобы показать скрытые папки и файлы. Затем создайте папку `.dynatrace` в Finder.

     Вы также можете выполнить `defaults write com.apple.finder AppleShowAllFiles false` и `killall Finder`, чтобы снова скрыть скрытые папки и файлы.
3. Скопируйте загруженный `DTSwiftInstrumentor` в папку `.dynatrace` и убедитесь, что файл является исполняемым.
4. Закройте Xcode и выполните `.dynatrace/DTSwiftInstrumentor install <PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`.

Если во время реализации возникает ошибка, проверьте журнал сборки Xcode или журнал инструментирования для получения подробной информации об ошибке. Дополнительные подсказки можно найти в [Мобильные приложения: проблемы с инструментированием SwiftUI](https://dt-url.net/yh638kl) в сообществе Dynatrace.

При сборке приложения следует использовать схему, которую вы инструментировали.

### Обновление инструментора

Когда доступна новая версия инструментора SwiftUI, вы можете обновить его через Homebrew или вручную.

Homebrew

Вручную

После выпуска новые версии инструментора загружаются через добавленный тап.

Выполните `brew update` и `brew upgrade DTSwiftInstrumentor`, чтобы обновить наш инструментор SwiftUI.

1. Загрузите и извлеките ZIP-файл, содержащий новую версию инструментора SwiftUI. Ссылка доступна в мастере инструментирования мобильных приложений.
2. Скопируйте загруженный `DTSwiftInstrumentor` в папку `.dynatrace`, заменив существующий файл.

Если вы видите следующее предупреждение сборки, вам также необходимо обновить скрипты сборки, которые были интегрированы во время установки инструментора Dynatrace SwiftUI.

```
Dynatrace: There is an upgrade for your project instrumentation. Please execute "DTSwiftInstrumentor project-upgrade <PROJECT.xcodeproj>" to upgrade your project
```

Выполните предложенную команду для обновления скриптов сборки, а затем сохраните изменения, внесённые в файл проекта.

### Удаление инструментора

Если инструментор Dynatrace SwiftUI вам больше не нужен, вы можете удалить его из системы через Homebrew или вручную удалить из вашего проекта.

Homebrew

Вручную

Выполните `brew remove DTSwiftInstrumentor` и `brew untap dynatrace/tools`, чтобы удалить наш инструментор SwiftUI из вашей системы.

1. Выполните `DTSwiftInstrumentor uninstall`, чтобы удалить инструментор SwiftUI из вашего проекта.

   * Необязательно Дополнительно можно указать `<PROJECT.xcodeproj>`. Если данные проекта не указаны, инструмент попытается автоматически определить и запустить интерактивный выбор.
2. Необязательно Удалите папки `.dynatrace` и `dynatrace_instrumented` из вашего проекта.

   Эти папки содержат кэш, данные журналов и, при необходимости, бинарный файл инструментора, установленный вручную.
   Эти папки содержат кэш инструментора, данные журналов и, при необходимости, бинарные файлы инструментора.

## Проверка различий инструментирования SwiftUI

OneAgent для iOS версии 8.257+

Чтобы проверить разницу между вашим оригинальным кодом и кодом, изменённым инструментором SwiftUI, выполните одну из следующих команд:

* Из корня проекта:

  + `DTSwiftInstrumentor diff`, если вы установили инструментор через Homebrew
  + `.dynatrace/DTSwiftInstrumentor diff`, если вы установили инструментор вручную
* Из любого каталога

  + `DTSwiftInstrumentor diff <root-project-dir-path>`

## Известные ограничения

### Инструментирование пользовательских элементов управления SwiftUI не поддерживается

В настоящее время Dynatrace не поддерживает инструментирование пользовательских элементов управления SwiftUI. Список элементов управления SwiftUI, которые можно инструментировать, см. в разделе [Поддерживаемые элементы управления](#supported-controls).

### Проблема с предпросмотром в Xcode

Когда сборка симулятора включала инструментирование SwiftUI, предпросмотры не загружались в Xcode. В качестве обходного решения мы отключили инструментирование SwiftUI для сборок симулятора. Если вы хотите добавить инструментирование SwiftUI в сборки симулятора, см. раздел [Инструментирование сборок симулятора](#instrument-simulator-builds).

### Только SwiftUI 2.0+

Dynatrace поддерживает инструментирование SwiftUI 2.0+, поскольку прослушиватель `onChange` недоступен в более ранних версиях SwiftUI. По этой причине цель развёртывания должна быть iOS 14+.

### Более длительное время сборки

В отличие от OneAgent для iOS, который изменяет ваше мобильное приложение в памяти во время выполнения, инструментор SwiftUI изменяет исходный код вашего проекта во время сборки. По этой причине процесс инструментирования SwiftUI заметно влияет на время сборки.

Чтобы сократить время сборки

* Собирайте только для **Device**. Если вы решили [инструментировать сборки симулятора](#instrument-simulator-builds), отключите эту функцию.
* Не запускайте инструментирование SwiftUI при каждой возможной сборке. Мы рекомендуем запускать инструментирование SwiftUI в ветках, таких как `main` или `release`.

### Несовместимость с watchOS

Невозможно скомпилировать проект, содержащий файлы, добавленные в целевую платформу watchOS, поскольку нет OneAgent для watchOS. В этом случае [вручную исключите](#exclude-swift-files) все файлы, общие с целевой платформой watchOS или являющиеся её частью.

### tvOS не поддерживается

В настоящее время нет официальной поддержки сборок tvOS SwiftUI.

## Метки элементов управления SwiftUI

Если не указано иное, инструментор Dynatrace SwiftUI пытается получить имя каждого элемента управления, рекурсивно ища строковые литералы или переменные, предоставленные в качестве заголовка.
В примере ниже инструментор извлечёт `"Login"` в качестве метки для кнопки:

```
Button("Login", action: {


/* perform login */


})
```

Извлечённая метка будет использована для сообщения об автоматическом действии `"Touch on Login"`, когда пользователь взаимодействует с кнопкой.

В следующем примере взаимодействие пользователя с этой кнопкой будет отображено как `"Touch on bookmark"`:

```
Button(action: {


print("Hello world!")


}) {


Image("bookmark")


}
```

### Использование имени элемента управления по умолчанию

Используйте модификатор `withCustomInstrumentationConfig(.useDefaultControlName)`, чтобы установить метку элемента управления в формат `<Control type>_<index>`:

```
Button("Login", action: {


/* perform login */


}).withCustomInstrumentationConfig(.useDefaultControlName)
```

Когда модификатор применяется, инструментор будет сообщать о действии касания как `"Touch on Button_0"`.

### Использование пользовательского имени элемента управления

Используйте модификатор `withCustomInstrumentationConfig(.useControlName(<Name>)`, чтобы указать пользовательскую метку для определённого элемента управления следующим образом:

```
Button("Login", action: {


/* perform login */


}).withCustomInstrumentationConfig(.useControlName("Login Button"))
```

В этом случае каждое касание кнопки будет отображаться как `"Touch on Login Button"`.

## Настройка инструментирования SwiftUI

### Включение Session Replay при сбоях

Session Replay при сбоях может захватывать и визуально воспроизводить действия, которые пользователь вашего приложения выполнял до [сбоя](../../../rum-concepts/user-and-error-events.md#crash "Узнайте о событиях пользователя и ошибках, а также о типах событий пользователя и ошибок, захватываемых Dynatrace.").

Чтобы включить эту функцию, см. [Включение Session Replay для приложений SwiftUI](../../../session-replay/session-replay-ios.md#sr-swiftui "Предварительные требования и процедура включения Session Replay для ваших приложений iOS.").

### Глобальное исключение элементов управления из инструментирования SwiftUI

OneAgent для iOS версии 8.263+

Инструментор Dynatrace SwiftUI инструментирует все элементы пользовательского интерфейса, перечисленные в разделе [Поддерживаемые элементы управления](#supported-controls). При необходимости вы можете глобально исключить определённые элементы управления из процесса инструментирования SwiftUI.

Чтобы глобально исключить элементы управления из инструментирования SwiftUI, добавьте [ключ конфигурации `DTXSwiftUIExcludedControls`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist` вашего проекта.

```
<key>DTXExcludedSwiftUIFiles</key>


<array>


<string>Button</string>


<string>Slider</string>


</array>
```

### Локальное исключение элементов управления из инструментирования SwiftUI

OneAgent для iOS версии 8.263+

С помощью функции `withCustomInstrumentationConfig(.skipInstrumentation)` вы можете локально исключать элементы управления из инструментирования SwiftUI.

В отличие от [ключа конфигурации `DTXSwiftUIExcludedControls`](#exclude-controls-global), который позволяет предотвратить инструментирование всех экземпляров указанного типа элемента управления, функция `withCustomInstrumentationConfig(.skipInstrumentation)` может использоваться для исключения конкретного экземпляра типа элемента управления. Эту функцию можно применить непосредственно к элементу управления или, чтобы исключить несколько экземпляров элементов управления, к контейнеру.

Соблюдайте следующие рекомендации при применении функции `withCustomInstrumentationConfig(.skipInstrumentation)`:

* Чтобы использовать функцию, сначала добавьте оператор импорта `import Dynatrace`.
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


…


Button("Login", action: { /* perform login */ })


.withCustomInstrumentationConfig(.skipInstrumentation)
```

#### Исключение нескольких элементов управления

Чтобы локально исключить группу элементов управления, примените функцию `withCustomInstrumentationConfig(.skipInstrumentation)` к их родительскому контейнеру.

```
import Dynatrace


…


HStack {


Button("Login", action: { /* perform login */ })


Button("Register", action: { /* perform registration */ })


}.withCustomInstrumentationConfig(.skipInstrumentation)
```

### Исключение файлов из инструментирования SwiftUI

По умолчанию инструментор Dynatrace SwiftUI обрабатывает все файлы с расширением `.swift`, но инструментирует только файлы, содержащие [поддерживаемые элементы управления](#supported-controls). При необходимости вы можете исключить определённые файлы и каталоги из процесса инструментирования SwiftUI.

Чтобы исключить файлы и каталоги из инструментирования SwiftUI

1. Добавьте [ключ конфигурации `DTXExcludedSwiftUIFiles`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist` вашего проекта.
2. Перечислите относительные пути всех файлов и каталогов, которые вы не хотите инструментировать. Пути должны быть относительно корня проекта — каталога, в котором расположен файл `.xcodeproj`.

   ```
   <key>DTXExcludedSwiftUIFiles</key>


   <array>


   <string>relative/file/path/</string>


   <string>relative/file.swift</string>


   </array>
   ```

Журнал инструментирования, доступный после каждой сборки, содержит список файлов и каталогов, которые должны быть исключены из инструментирования SwiftUI. Журнал инструментирования также показывает, был ли файл или каталог исключён в процессе инструментирования.

### Инструментирование сборок симулятора

Мы отключили инструментирование SwiftUI для сборок симулятора, чтобы преодолеть [проблему с предпросмотром в Xcode](#issue-preview-xcode).

Чтобы включить инструментирование SwiftUI для сборок симулятора, добавьте [ключ конфигурации `DTXSwiftUIInstrumentSimulatorBuilds`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist` вашего проекта и установите этот ключ в значение `true`.

```
<key>DTXSwiftUIInstrumentSimulatorBuilds</key>


<true/>
```

### Создание сборок для неподдерживаемых целей развёртывания

Наш инструментор SwiftUI генерирует код, совместимый с SwiftUI 2.0+, который работает только на устройствах с iOS 14+. Попытка генерации сборок для целей развёртывания iOS 13 и более ранних версий завершится неудачей.

Чтобы переопределить эту проверку, добавьте [ключ конфигурации `DTXSwiftUIIgnoreDeploymentTarget`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist` вашего проекта и установите этот ключ в значение `true`.

```
<key>DTXSwiftUIIgnoreDeploymentTarget</key>


<true/>
```

### Включение сопоставления номеров строк для проектов Objective-C

Отчёты о сбоях, доступные в Dynatrace, не основаны на исходном коде вашего проекта. Эти отчёты основаны на изменённом коде, который Dynatrace генерирует в процессе инструментирования. Вот почему сопоставление номеров строк добавляется в ваш проект во время инструментирования и впоследствии передаётся в Dynatrace при запуске приложения. В противном случае номера строк в отчётах о сбоях были бы неверными.

По умолчанию инструментор Dynatrace SwiftUI генерирует сопоставление номеров строк и вставляет его в основной класс вашего проекта. Это происходит автоматически для проектов с основным классом Swift, но не для устаревших проектов Objective-C. Для таких проектов вы получите ошибку, и наш инструментор SwiftUI не будет инструментировать ваше мобильное приложение.

Чтобы включить сопоставление номеров строк для проектов Objective-C

1. Добавьте [ключ конфигурации `DTXSwiftUIManualPlaceholder`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist` вашего проекта и установите этот ключ в значение `true`.

   ```
   <key>DTXSwiftUIManualPlaceholder</key>


   <true/>
   ```
2. Добавьте специальный заполнитель `AppDelegate.m` в основной класс.
3. Добавьте строку `[Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];` в основной класс либо в метод `init`, либо в метод `didFinishLaunchingWithOptions` (но не в оба).

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

   Во время сборки инструментор SwiftUI заменит часть этой строки сгенерированным сопоставлением номеров строк.

### Включение автоматической очистки журналов

OneAgent для iOS версии 8.257+

После каждой сборки инструментор SwiftUI создаёт резервные копии инструментированных файлов и сгенерированных журналов, которые хранятся в `dynatrace_instrumented`. По умолчанию эти файлы не удаляются, и общий размер каталога будет увеличиваться со временем. По этой причине мы рекомендуем включить автоматическую очистку журналов.

* Чтобы удалять журналы инструментора SwiftUI после определённого количества сборок, добавьте [ключ конфигурации `DTXCleanSwiftUILogsByCount`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist` вашего проекта.

  ```
  <key>DTXCleanSwiftUILogsByCount</key>


  <number>10</number>
  ```
* Чтобы удалять журналы по истечении определённого количества дней, добавьте [ключ конфигурации `DTXCleanSwiftUILogsByAgeDays`](../customization/ios-configuration-keys.md#swiftui "С помощью ключей конфигурации вы можете тонко настроить автоматическое инструментирование ваших приложений iOS.") в файл `Info.plist`.

  ```
  <key>DTXCleanSwiftUILogsByAgeDays</key>


  <number>5</number>
  ```

Если вы добавляете оба ключа в файл `Info.plist`, ключ `DTXCleanSwiftUILogsByAgeDays` имеет приоритет.

## Устранение неполадок

Мы продолжаем работу над улучшением процесса инструментирования SwiftUI. Если у вас возникают проблемы при инструментировании элементов управления SwiftUI, обратитесь к разделу [Мобильные приложения: проблемы с инструментированием SwiftUI](https://dt-url.net/yh638kl) в сообществе Dynatrace.
