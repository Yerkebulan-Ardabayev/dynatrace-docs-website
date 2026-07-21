---
title: Настройка OneAgent для iOS-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios
---

# Настройка OneAgent для iOS-приложений в RUM Classic

# Настройка OneAgent для iOS-приложений в RUM Classic

* Практическое руководство
* Чтение 8 минут
* Обновлено 19 января 2026 г.

iOS tvOS

Чтобы отслеживать мобильное приложение с помощью Dynatrace, нужно создать приложение в Dynatrace и настроить OneAgent для мобильного приложения.

После этого можно также [инструментировать элементы управления SwiftUI приложения](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Используйте инструментатор SwiftUI Dynatrace для отслеживания приложений на SwiftUI."), настроить [функции автоматической инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Список функций, доступных после инструментации приложения с помощью OneAgent.") через [конфигурационные ключи](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить автоматическую инструментацию iOS-приложений."), или собрать дополнительные данные с помощью [ручной инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Обогатите мониторинг пользовательского опыта на мобильных устройствах с помощью OneAgent SDK для iOS.").

## Создание приложения в Dynatrace

Чтобы создать мобильное приложение в Dynatrace

1. В Dynatrace перейти в раздел **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести имя приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.

## Настройка OneAgent

Используй [CocoaPods](#cocoapods) или [Swift Package Manager](#swift-pm), чтобы настроить Real User Monitoring для приложения. Можно также следовать [ручному подходу](#manual), однако лучше использовать один из автоматизированных вариантов.

OneAgent можно настроить как динамический XCFramework, статический XCFramework (доступен для OneAgent для iOS версии 8.237+), традиционный framework или статическую библиотеку.

Нельзя сочетать статический XCFramework Dynatrace и динамический XCFramework Session Replay. Для [Session Replay](/managed/observe/digital-experience/session-replay/session-replay-ios "Предварительные условия и порядок включения Session Replay Classic для iOS-приложений.") оба XCFramework должны быть динамическими.

Если для инструментации iOS-приложения используется статический XCFramework, традиционный framework или статическая библиотека, потребуется выполнить несколько дополнительных шагов.

### Настройка OneAgent с помощью CocoaPods

1. Добавить OneAgent Dynatrace как зависимость в спецификации CocoaPods `Podfile`. Это можно сделать, настроив OneAgent как динамический XCFramework, статический XCFramework, традиционный framework или статическую библиотеку.

   Dynamic XCFramework

   Static XCFramework

   Traditional framework

   Static library

   Чтобы настроить Dynatrace как динамический XCFramework, добавь в `Podfile` только **один** под.

   * под `Dynatrace` для добавления только OneAgent
   * под `Dynatrace/SessionReplay` для добавления и OneAgent, и модуля [Session Replay при сбоях](/managed/observe/digital-experience/session-replay/session-replay-ios "Предварительные условия и порядок включения Session Replay Classic для iOS-приложений.")

   Убедись, что строка `use_frameworks!` раскомментирована.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   use_frameworks!



   # Pod for DemoApp to add only OneAgent



   pod 'Dynatrace', '~> 8.279'



   # Pod for DemoApp to add both OneAgent and Session Replay



   # pod 'Dynatrace/SessionReplay', '~> 8.279'



   end
   ```

   Чтобы настроить Dynatrace как статический XCFramework, добавь в `Podfile` под `Dynatrace/xcframeworkStatic`. Убедись, что строка `use_frameworks!` раскомментирована.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   use_frameworks!



   # Pods for DemoApp



   pod 'Dynatrace/xcframeworkStatic', '~> 8.279'



   end
   ```

   Чтобы настроить Dynatrace как традиционный framework, добавь в `Podfile` под `Dynatrace/framework`. Убедись, что строка `use_frameworks!` раскомментирована.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   use_frameworks!



   # Pods for DemoApp



   pod 'Dynatrace/framework', '~> 8.279'



   end
   ```

   Чтобы настроить Dynatrace как статическую библиотеку, добавь в `Podfile` под `Dynatrace/lib`. Убедись, что строка `use_frameworks!` закомментирована.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   # use_frameworks!



   # Pods for DemoApp



   pod 'Dynatrace/lib', '~> 8.279'



   end
   ```

   Традиционный framework и статическая библиотека признаны устаревшими, поскольку не поддерживают архитектуру ARM64 Simulator. Эта архитектура требуется для сборки приложений на компьютерах Mac с Apple silicon.
2. Добавь идентификационные ключи приложения в [файл `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификационные и конфигурационные ключи приложения. Используй его для точной настройки конфигурации инструментации."). Точные значения смотри в [мастере инструментации](#instrumentation-wizard) в Dynatrace.
3. Запусти сборку проекта один раз перед использованием OneAgent SDK или любых объявлений импорта в Xcode.

CocoaPods автоматически добавляет OneAgent в iOS-проект в процессе сборки.

Дополнительную информацию о Podfile смотри в [Podfile Syntax Reference﻿](https://guides.cocoapods.org/syntax/podfile.html#podfile).

Начиная с декабря 2026 г. репозиторий CocoaPods Specs станет доступен только для чтения.

После этого изменения Dynatrace больше не сможет публиковать новые версии OneAgent SDK для iOS в CocoaPods, включая хотфиксы и критические обновления.
Чтобы продолжать получать обновления, перейди на [Swift Package Manager](#swift-pm).

Подробности по срокам смотри в официальном [блоге CocoaPods﻿](https://blog.cocoapods.org/CocoaPods-Specs-Repo/).

### Настройка OneAgent с помощью Swift Package Manager

1. В Xcode выберите **File** > **Swift Packages** > **Add Package Dependency**.
2. Добавьте `https://github.com/Dynatrace/swift-mobile-sdk.git` в качестве URL репозитория пакета.
3. Выберите только **один** продукт пакета:

   * `Dynatrace`, чтобы добавить только OneAgent
   * `DynatraceSessionReplay`, чтобы добавить и OneAgent, и модуль [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.")

     Не выбирайте `DynatraceSessionReplay` для tvOS, поскольку Session Replay недоступен для этой операционной системы.
   * `Dynatrace-Static`, чтобы добавить только OneAgent в виде статического XCFramework
4. Выполните дополнительные шаги в зависимости от используемого фреймворка.
   Static XCFramework: добавление флага линковщика

   1. В Xcode перейдите на вкладку **Build Settings** таргета вашего приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг линковщика `-ObjC` в **Other Linker Flags**.

   Static XCFramework: сделать Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в вашем приложении нет кода Swift или доступ к фреймворку Dynatrace не нужен.

   Предполагается, что заголовочный файл Objective-C bridging для вашего кода Swift в Xcode уже создан.

   1. Убедитесь, что заголовочный файл bridging указан в настройках сборки таргета приложения.
   2. Добавьте следующую строку импорта в заголовочный файл bridging:

      ```
      #import <DynatraceStatic/Dynatrace.h>
      ```

   Static library: добавление флага линковщика

   1. В Xcode перейдите на вкладку **Build Settings** таргета вашего приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг линковщика `-ObjC` в **Other Linker Flags**.

   Static library: сделать Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в вашем приложении нет кода Swift или доступ к библиотеке Dynatrace не нужен.

   Предполагается, что заголовочный файл Objective-C bridging для вашего кода Swift в Xcode уже создан.

   1. Убедитесь, что заголовочный файл bridging указан в настройках сборки таргета приложения.
   2. Добавьте следующую строку импорта в заголовочный файл bridging:

      ```
      #import Dynatrace.h
      ```
5. Добавьте идентификационные ключи вашего приложения в [файл `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration."). Точные значения проверьте в [мастере инструментирования](#instrumentation-wizard) в Dynatrace.
6. Перед использованием OneAgent SDK или любых объявлений импорта в Xcode один раз запустите сборку проекта.

Чтобы изменить правило версии пакета, дважды щёлкните запись продукта на вкладке **Swift Packages** в настройках проекта Xcode. Чтобы изменить выбор продукта, удалите пакет и добавьте его снова.

Чтобы обновить пакет, выберите **File** > **Swift Packages** > **Update to Latest Package Versions** в Xcode.

При переходе с [Carthage](#carthage) на Swift Package Manager удалите скрипт, который ранее был добавлен в Xcode для удаления архитектуры iOS Simulator из релизного бинарника. В противном случае возможны проблемы при сборке проекта в Xcode 15+.

### Настройка OneAgent вручную

1. Откройте [мастер мобильного инструментирования](#instrumentation-wizard).
2. Выберите **iOS**, затем перейдите на вкладку **Developer**.
3. Следуйте предоставленным инструкциям.

   Добавьте `Dynatrace.xcframework`, чтобы получить только OneAgent.
   Добавьте и `Dynatrace.xcframework`, и `DynatraceSessionReplay.xcframework`, чтобы получить и OneAgent, и модуль [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.").

   Не добавляйте `DynatraceSessionReplay.xcframework` для tvOS, поскольку Session Replay недоступен для этой операционной системы.
4. Выполните несколько дополнительных шагов в зависимости от используемого фреймворка.

   Static XCFramework: добавление флага линковщика

   1. В Xcode перейдите на вкладку **Build Settings** таргета вашего приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг линковщика `-ObjC` в **Other Linker Flags**.

   Static XCFramework: добавление подключаемой библиотеки

   1. В Xcode перейдите на вкладку **General** таргета вашего приложения.
   2. Разверните **Frameworks, Libraries, and Embedded Content**.
   3. Добавьте библиотеку `libc++.tbd`.

   Возможно, эту библиотеку потребуется добавить дважды. В наших внутренних тестах библиотека привязывалась к дереву проекта только после повторного добавления.

   Static XCFramework: сделать Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в вашем приложении нет кода Swift или доступ к фреймворку Dynatrace не нужен.

   Предполагается, что заголовочный файл Objective-C bridging для вашего кода Swift в Xcode уже создан.

   1. Убедитесь, что заголовочный файл bridging указан в настройках сборки таргета приложения.
   2. Добавьте следующую строку импорта в заголовочный файл bridging:

      ```
      #import <DynatraceStatic/Dynatrace.h>
      ```

   Traditional framework: удаление архитектуры iOS Simulator из релизного бинарника

   1. В Xcode добавьте этап **Run Script** в качестве последней фазы сборки (**Build Phase**) таргета вашего приложения.
   2. Добавьте следующий скрипт:

      ```
      APP_PATH="${TARGET_BUILD_DIR}/${WRAPPER_NAME}"



      find "$APP_PATH" -name '*.framework' -type d | while read -r FRAMEWORK



      do



      FRAMEWORK_EXECUTABLE_NAME=$(defaults read "$FRAMEWORK/Info.plist" CFBundleExecutable)



      FRAMEWORK_EXECUTABLE_PATH="$FRAMEWORK/$FRAMEWORK_EXECUTABLE_NAME"



      EXTRACTED_ARCHS=()



      for ARCH in $ARCHS



      do



      lipo -extract "$ARCH" "$FRAMEWORK_EXECUTABLE_PATH" -o "$FRAMEWORK_EXECUTABLE_PATH-$ARCH"



      EXTRACTED_ARCHS+=("$FRAMEWORK_EXECUTABLE_PATH-$ARCH")



      done



      lipo -o "$FRAMEWORK_EXECUTABLE_PATH-merged" -create "${EXTRACTED_ARCHS[@]}"



      rm "${EXTRACTED_ARCHS[@]}"



      rm "$FRAMEWORK_EXECUTABLE_PATH"



      mv "$FRAMEWORK_EXECUTABLE_PATH-merged" "$FRAMEWORK_EXECUTABLE_PATH"



      done
      ```
   3. Выберите **Run script: For install builds only**.

   Это удаляет архитектуру iOS Simulator из релизного бинарника, используемого для загрузки в AppStore Connect.

   Static library: добавление флага линковщика

   1. В Xcode перейдите на вкладку **Build Settings** таргета вашего приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг линковщика `-ObjC` в **Other Linker Flags**.

   Static library: сделать Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в вашем приложении нет кода Swift или доступ к библиотеке Dynatrace не нужен.

   Предполагается, что заголовочный файл Objective-C bridging для вашего кода Swift в Xcode уже создан.

   1. Убедитесь, что заголовочный файл bridging указан в настройках сборки таргета приложения.
   2. Добавьте следующую строку импорта в заголовочный файл bridging:

      ```
      #import Dynatrace.h
      ```
5. Перед использованием OneAgent SDK или любых объявлений импорта в Xcode один раз запустите сборку проекта.

## Доступ к мастеру мобильного инструментирования

Мастер мобильного инструментирования в Dynatrace предоставляет инструкции для начала работы по инструментированию ваших iOS-приложений. Более подробные инструкции приведены в разделе [Настройка OneAgent](#set-up-oneagent) на этой странице.

Мастер также содержит фрагменты кода с идентификационными ключами вашего приложения, которые нужно добавить в [файл `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Instrumentation wizard**.

## Известные ограничения

* Не рекомендуется одновременно использовать несколько инструментов мониторинга с включённой функцией crash reporting или инструментирования веб-запросов. Это может привести к проблемам совместимости, передаче неверных или недействительных данных, а также к потере данных мониторинга и сбоев. Тем не менее, если принято решение сделать это, нужно проверить совместимость этих инструментов путём ручного тестирования.
* Чтобы использовать одновременно Dynatrace и Firebase, нужно выполнить одно из следующих действий.

  + [Полностью отключить Firebase Performance Monitoring﻿](https://firebase.google.com/docs/perf-mon/disable-sdk?platform=ios).
  + [Отключить автоматическое инструментирование веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Enrich mobile user experience monitoring using OneAgent SDK for iOS.") в OneAgent для iOS.

  Следовать нужно только одному из вышеуказанных подходов, выполнять оба действия нельзя.
* Чтобы использовать одновременно Dynatrace и [mPaaS﻿](https://dt-url.net/mPaaS), нужно выполнить одно из следующих действий.

  + [Отключить автоматическое инструментирование веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Enrich mobile user experience monitoring using OneAgent SDK for iOS.") в OneAgent для iOS.
  + Не использовать [фреймворк MPNebulaAdapter﻿](https://dt-url.net/MPNebulaAdapter).

  Следовать нужно только одному из вышеуказанных подходов, выполнять оба действия нельзя.
* Приложение с автоматическим инструментированием не может выполнять такие функции, как `Dynatrace.shutdown()` или Dynatrace `.flushEvents()`. Эти методы и другие пользовательские действия и события можно вставить вручную перед выполнением автоматического инструментирования.
* Следующие элементы управления нельзя использовать для создания автоматически сгенерированных действий:

  + Жесты
  + Некоторые элементы `UIBarButton`, включая пользовательские элементы `UIBarButton`, добавленные в панель навигации через storyboard (например, `info`), которые используют segues для перехода к другим представлениям.

### Совместимость с шифрованием файлов

Шифрование файлов на уровне файловой системы или строгая защита данных iOS может препятствовать доступу OneAgent for Mobile к файлам своей базы данных, что приводит к прекращению сбора данных.

**Проблема**:
OneAgent для iOS хранит данные в файлах SQLite (`DTEvents_*.sqlite`, `DTX*`) в каталоге Application Support. Если эти файлы зашифрованы или защищены строго, OneAgent для iOS не может читать/записывать данные, что приводит к следующему:

* Не собираются новые сессии или события
* Ошибки повреждения базы данных в журналах
* Частое пересоздание базы данных

**Решения**:

* **Рекомендуется**: исключить файлы OneAgent из шифрования файлов мобильного приложения
* **Альтернатива**: использовать `FileProtectionType.completeUntilFirstUserAuthentication` для файлов OneAgent
* Применять шифрование после инициализации OneAgent для iOS

Для отладки см. [Отладочное логирование OneAgent для iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.").