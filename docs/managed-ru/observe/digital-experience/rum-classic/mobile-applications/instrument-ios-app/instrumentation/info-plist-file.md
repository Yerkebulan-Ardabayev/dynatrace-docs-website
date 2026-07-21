---
title: Файл Info.plist в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file
---

# Файл Info.plist в RUM Classic

# Файл Info.plist в RUM Classic

* Объяснение
* Чтение 2 мин.
* Обновлено 26 апр. 2024 г.

При использовании Dynatrace файл `Info.plist` хранит ключи идентификации приложения и конфигурации. Ниже приведена информация об этом файле.

* Файл `Info.plist` доступен в навигаторе проекта Xcode в разделе **Supporting Files**. Для более старых проектных файлов `Info.plist` находится в разделе **Resources**.
* Независимо от выбранного подхода к настройке RUM для приложения, добавь ключи идентификации приложения (app ID и beacon URL) в файл `Info.plist` проекта: [ключи `DTXApplicationID` и `DTXBeaconURL`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") требуются всегда. Без ключей идентификации приложения мобильное приложение не сможет отправлять данные мониторинга в Dynatrace.

  Чтобы проверить ключи идентификации приложения, открой [мастер настройки мобильной инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
* Также можно использовать `Info.plist` для включения или отключения дополнительных функций мониторинга, добавляя в этот файл [ключи конфигурации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").
* Чтобы файл `Info.plist` приложения оставался чистым, можно перенести все связанные с OneAgent ключи `DTX` в файл `Dynatrace.plist` и добавить `Dynatrace.plist` на этап сборки `Copy Bundle Resources`. Файл `Dynatrace.plist` должен находиться в корне бандла ресурсов, поэтому создавать этот файл нужно в том же месте, что и `Info.plist`.
* В некоторых случаях при использовании Xcode файл `Info.plist` не создаётся. Например, при создании нового проекта SwiftUI можно заметить, что в проекте отсутствует этот файл. Подробнее см. [Xcode Release Notes; issue 68254857﻿](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes#Templates).

  Если файла `Info.plist` нет, добавь ключи идентификации приложения и [ключи конфигурации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") вручную как **Custom iOS Target Properties** на вкладке **Info** таргета приложения. После этого изменения Xcode добавит файл `Info.plist` в проект, но всё равно лучше обновлять конфигурацию через вкладку **Info** таргета приложения.