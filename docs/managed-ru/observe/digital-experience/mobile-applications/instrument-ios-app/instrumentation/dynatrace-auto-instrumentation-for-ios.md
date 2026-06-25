---
title: Настройка OneAgent для iOS-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios
scraped: 2026-05-12T11:32:40.786706
---

# Настройка OneAgent для iOS-приложений

# Настройка OneAgent для iOS-приложений

* How-to guide
* 8-min read
* Updated on Jan 19, 2026

iOS tvOS

Для мониторинга мобильного приложения с помощью Dynatrace необходимо создать приложение в Dynatrace и настроить OneAgent для мобильного приложения.

После этого вы можете [инструментировать элементы управления SwiftUI](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений."), настроить [функции авто-инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent.") через [конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") или захватывать дополнительные данные через [ручное инструментирование](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.").

## Создание приложения в Dynatrace

Чтобы создать мобильное приложение в Dynatrace:

1. В Dynatrace перейдите в **Mobile**.
2. Нажмите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница настроек приложения.

## Настройка OneAgent

Используйте [CocoaPods](#cocoapods) или [Swift Package Manager](#swift-pm) для настройки Real User Monitoring для приложения. Также можно воспользоваться [ручным подходом](#manual), хотя предпочтительнее использовать один из автоматизированных способов.

OneAgent можно настроить как динамический XCFramework, статический XCFramework (доступно для OneAgent for iOS версии 8.237+), традиционный фреймворк или статическую библиотеку.

Нельзя одновременно использовать статический Dynatrace XCFramework и динамический Session Replay XCFramework. Для [Session Replay](/managed/observe/digital-experience/session-replay/session-replay-ios "Требования и процедура включения Session Replay для iOS-приложений.") оба XCFramework должны быть динамическими.

При использовании статического XCFramework, традиционного фреймворка или статической библиотеки для инструментирования iOS-приложения потребуются некоторые дополнительные шаги.

### Настройка OneAgent с помощью CocoaPods

1. Добавьте Dynatrace OneAgent в качестве зависимости в спецификации CocoaPods `Podfile`. Это можно сделать, настроив OneAgent как динамический XCFramework, статический XCFramework, традиционный фреймворк или статическую библиотеку.

   Динамический XCFramework

   Статический XCFramework

   Традиционный фреймворк

   Статическая библиотека

   Для настройки Dynatrace как динамического XCFramework добавьте только **один** pod в `Podfile`.

   * Pod `Dynatrace` для добавления только OneAgent
   * Pod `Dynatrace/SessionReplay` для добавления OneAgent и модуля [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Требования и процедура включения Session Replay для iOS-приложений.")

   Убедитесь, что строка `use_frameworks!` раскомментирована.

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

   Для настройки Dynatrace как статического XCFramework добавьте pod `Dynatrace/xcframeworkStatic` в `Podfile`. Убедитесь, что строка `use_frameworks!` раскомментирована.

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

   Для настройки Dynatrace как традиционного фреймворка добавьте pod `Dynatrace/framework` в `Podfile`. Убедитесь, что строка `use_frameworks!` раскомментирована.

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

   Для настройки Dynatrace как статической библиотеки добавьте pod `Dynatrace/lib` в `Podfile`. Убедитесь, что строка `use_frameworks!` закомментирована.

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

   Традиционный фреймворк и статическая библиотека устарели, так как не поддерживают архитектуру ARM64 Simulator. Эта архитектура требуется для сборки приложений на компьютерах Mac с Apple silicon.
2. Добавьте ключи идентификации приложения в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования."). Точные значения можно проверить в [мастере инструментирования](#instrumentation-wizard) в Dynatrace.
3. Выполните сборку проекта один раз перед использованием OneAgent SDK или любых операторов импорта в Xcode.

CocoaPods автоматически добавляет OneAgent в iOS-проект в процессе сборки.

Подробнее о Podfiles см. в [Podfile Syntax Reference](https://guides.cocoapods.org/syntax/podfile.html#podfile).

Начиная с декабря 2026 года репозиторий CocoaPods Specs будет переведён в режим «только для чтения».

После этого изменения Dynatrace больше не сможет публиковать новые версии OneAgent SDK for iOS в CocoaPods, включая исправления и критические обновления.
Для продолжения получения обновлений выполните миграцию на [Swift Package Manager](#swift-pm).

Подробнее о сроках см. в официальном [блоге CocoaPods](https://blog.cocoapods.org/CocoaPods-Specs-Repo/).

### Настройка OneAgent с помощью Swift Package Manager

1. В Xcode выберите **File** > **Swift Packages** > **Add Package Dependency**.
2. Добавьте `https://github.com/Dynatrace/swift-mobile-sdk.git` в качестве URL репозитория пакета.
3. Выберите только **один** продукт пакета:

   * `Dynatrace` для добавления только OneAgent
   * `DynatraceSessionReplay` для добавления OneAgent и модуля [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Требования и процедура включения Session Replay для iOS-приложений.")

     Не выбирайте `DynatraceSessionReplay` для tvOS, так как Session Replay недоступен для этой операционной системы.
   * `Dynatrace-Static` для добавления только OneAgent в виде статического XCFramework
4. Выполните дополнительные шаги в зависимости от используемого фреймворка.

   Статический XCFramework: добавьте флаг линковщика

   1. В Xcode перейдите на вкладку **Build Settings** целевого объекта приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг `-ObjC` в **Other Linker Flags**.

   Статический XCFramework: сделайте Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в приложении нет кода Swift или нет необходимости в доступе к фреймворку Dynatrace.

   Предполагается, что вы уже создали файл Objective-C bridging header для кода Swift в Xcode.

   1. Убедитесь, что файл bridging header указан в настройках сборки целевого объекта приложения.
   2. Добавьте следующую строку импорта в файл bridging header:

      ```
      #import <DynatraceStatic/Dynatrace.h>
      ```

   Статическая библиотека: добавьте флаг линковщика

   1. В Xcode перейдите на вкладку **Build Settings** целевого объекта приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг `-ObjC` в **Other Linker Flags**.

   Статическая библиотека: сделайте Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в приложении нет кода Swift или нет необходимости в доступе к библиотеке Dynatrace.

   Предполагается, что вы уже создали файл Objective-C bridging header для кода Swift в Xcode.

   1. Убедитесь, что файл bridging header указан в настройках сборки целевого объекта приложения.
   2. Добавьте следующую строку импорта в файл bridging header:

      ```
      #import Dynatrace.h
      ```
5. Добавьте ключи идентификации приложения в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования."). Точные значения можно проверить в [мастере инструментирования](#instrumentation-wizard) в Dynatrace.
6. Выполните сборку проекта один раз перед использованием OneAgent SDK или любых операторов импорта в Xcode.

Для обновления правила версии пакета дважды щёлкните запись продукта на вкладке **Swift Packages** в настройках проекта Xcode. Чтобы изменить выбор продукта, удалите пакет и добавьте его снова.

Для обновления пакета выберите **File** > **Swift Packages** > **Update to Latest Package Versions** в Xcode.

При переходе с Carthage на Swift Package Manager удалите скрипт, ранее добавленный в Xcode для удаления архитектуры iOS Simulator из бинарного файла релиза. В противном случае могут возникнуть проблемы при сборке проекта в Xcode 15+.

### Настройка OneAgent вручную

1. Откройте [мастер инструментирования](#instrumentation-wizard).
2. Выберите **iOS**, затем перейдите на вкладку **Developer**.
3. Следуйте предоставленным инструкциям.

   Добавьте `Dynatrace.xcframework` для OneAgent.
   Добавьте `Dynatrace.xcframework` и `DynatraceSessionReplay.xcframework` для OneAgent и модуля [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Требования и процедура включения Session Replay для iOS-приложений.").

   Не добавляйте `DynatraceSessionReplay.xcframework` для tvOS, так как Session Replay недоступен для этой операционной системы.
4. Выполните дополнительные шаги в зависимости от используемого фреймворка.

   Статический XCFramework: добавьте флаг линковщика

   1. В Xcode перейдите на вкладку **Build Settings** целевого объекта приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг `-ObjC` в **Other Linker Flags**.

   Статический XCFramework: добавьте связанную библиотеку

   1. В Xcode перейдите на вкладку **General** целевого объекта приложения.
   2. Разверните **Frameworks, Libraries, and Embedded Content**.
   3. Добавьте библиотеку `libc++.tbd`.

   Возможно, библиотеку придётся добавить дважды. Во внутренних тестах библиотека связывалась с деревом проекта только после повторного добавления.

   Статический XCFramework: сделайте Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в приложении нет кода Swift или нет необходимости в доступе к фреймворку Dynatrace.

   Предполагается, что вы уже создали файл Objective-C bridging header для кода Swift в Xcode.

   1. Убедитесь, что файл bridging header указан в настройках сборки целевого объекта приложения.
   2. Добавьте следующую строку импорта в файл bridging header:

      ```
      #import <DynatraceStatic/Dynatrace.h>
      ```

   Традиционный фреймворк: удалите архитектуру iOS Simulator из бинарного файла релиза

   1. В Xcode добавьте фазу **Run Script** в качестве последней **Build Phase** целевого объекта приложения.
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

   Это удаляет архитектуру iOS Simulator из бинарного файла релиза, используемого для загрузки в App Store Connect.

   Статическая библиотека: добавьте флаг линковщика

   1. В Xcode перейдите на вкладку **Build Settings** целевого объекта приложения.
   2. Разверните **Linking**.
   3. Добавьте флаг `-ObjC` в **Other Linker Flags**.

   Статическая библиотека: сделайте Dynatrace доступным для кода Swift

   Этот шаг можно пропустить, если в приложении нет кода Swift или нет необходимости в доступе к библиотеке Dynatrace.

   Предполагается, что вы уже создали файл Objective-C bridging header для кода Swift в Xcode.

   1. Убедитесь, что файл bridging header указан в настройках сборки целевого объекта приложения.
   2. Добавьте следующую строку импорта в файл bridging header:

      ```
      #import Dynatrace.h
      ```
5. Выполните сборку проекта один раз перед использованием OneAgent SDK или любых операторов импорта в Xcode.

## Доступ к мастеру инструментирования

Мастер инструментирования в Dynatrace предоставляет инструкции по началу работы с инструментированием iOS-приложений. Более подробные инструкции см. в разделе [Настройка OneAgent](#set-up-oneagent) на этой странице.

Мастер также содержит фрагменты кода с ключами идентификации приложения, которые необходимо добавить в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.").

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с именем приложения нажмите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Instrumentation wizard**.

## Известные ограничения

* Не рекомендуется одновременно использовать несколько инструментов мониторинга с включёнными функциями отчётов о сбоях или инструментирования веб-запросов. Это может вызвать проблемы совместимости, сообщение некорректной информации и потерю данных мониторинга и сбоев. Тем не менее если вы всё же решите это сделать, убедитесь посредством ручного тестирования, что эти инструменты совместимы.
* Для одновременного использования Dynatrace и Firebase выполните одно из следующих действий.

  + [Полностью деактивируйте Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon/disable-sdk?platform=ios).
  + [Отключите автоматическое инструментирование веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.") в OneAgent for iOS.

  Следуйте только одному из вышеперечисленных подходов; не выполняйте оба действия одновременно.
* Для одновременного использования Dynatrace и [mPaaS](https://dt-url.net/mPaaS) выполните одно из следующих действий.

  + [Отключите автоматическое инструментирование веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK for iOS.") в OneAgent for iOS.
  + Не используйте [фреймворк MPNebulaAdapter](https://dt-url.net/MPNebulaAdapter).

  Следуйте только одному из вышеперечисленных подходов; не выполняйте оба действия одновременно.
* Авто-инструментированное приложение не может выполнять такие функции, как `Dynatrace.shutdown()` или `Dynatrace.flushEvents()`. Эти методы и другие пользовательские действия и события можно вставить вручную перед выполнением авто-инструментирования.
* Следующие элементы управления не могут использоваться для создания автоматически генерируемых действий:

  + Жесты
  + Некоторые элементы `UIBarButton`, в том числе пользовательские `UIBarButton`, добавленные на панель навигации через storyboard (например, `info`) и использующие segue для перехода к другим представлениям.

### Совместимость с шифрованием файлов

Шифрование на уровне файлов или строгая защита данных iOS могут помешать OneAgent for Mobile получить доступ к файлам базы данных, что приведёт к прекращению сбора данных.

**Проблема:**
OneAgent for iOS хранит данные в файлах SQLite (`DTEvents_*.sqlite`, `DTX*`) в директории Application Support. Если эти файлы зашифрованы или строго защищены, OneAgent for iOS не сможет читать/записывать данные, что приводит к:

* отсутствию новых сессий или событий;
* ошибкам повреждения базы данных в журналах;
* частому пересозданию базы данных.

**Решения:**

* **Рекомендуется**: исключите файлы OneAgent из шифрования файлов мобильного приложения
* **Альтернатива**: используйте `FileProtectionType.completeUntilFirstUserAuthentication` для файлов OneAgent
* Применяйте шифрование после инициализации OneAgent for iOS

Для отладки см. [Отладочное журналирование OneAgent for iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Включите отладочное журналирование для OneAgent.").