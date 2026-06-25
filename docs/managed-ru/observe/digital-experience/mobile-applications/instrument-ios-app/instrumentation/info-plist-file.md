---
title: Файл Info.plist
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file
scraped: 2026-05-12T11:32:57.778729
---

# Файл Info.plist

# Файл Info.plist

* Explanation
* 2-min read
* Updated on Apr 26, 2024

При использовании Dynatrace файл `Info.plist` хранит ключи идентификации и конфигурации приложения. Ниже приведена информация об этом файле.

* Файл `Info.plist` доступен в навигаторе проекта Xcode в разделе **Supporting Files**. Для более старых файлов проекта `Info.plist` находится в разделе **Resources**.
* Независимо от выбранного способа настройки RUM для приложения добавьте ключи идентификации приложения (ID приложения и beacon URL) в файл `Info.plist` проекта; ключи [`DTXApplicationID` и `DTXBeaconURL`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") всегда обязательны. Без ключей идентификации приложения мобильное приложение не сможет отправлять данные мониторинга в Dynatrace.

  Чтобы проверить ключи идентификации приложения, откройте [мастер инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Настройте мониторинг пользовательского опыта для iOS-приложений в Dynatrace.").
* Также можно использовать `Info.plist` для включения или отключения дополнительных функций мониторинга, добавив в этот файл [конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.").
* Чтобы сохранить чистоту файла `Info.plist`, можно перенести все связанные с OneAgent ключи `DTX` в файл `Dynatrace.plist` и добавить `Dynatrace.plist` в фазу сборки `Copy Bundle Resources`. Файл `Dynatrace.plist` должен находиться в корне пакета ресурсов, поэтому создайте его в том же месте, что и файл `Info.plist`.
* В некоторых случаях файл `Info.plist` не создаётся при использовании Xcode. Например, при создании нового проекта SwiftUI файл `Info.plist` может отсутствовать. Подробнее см. в [Xcode Release Notes; issue 68254857](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes#Templates).

  Если файл `Info.plist` отсутствует, добавьте ключи идентификации и [конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") вручную как **Custom iOS Target Properties** на вкладке **Info** цели приложения. После внесения изменений Xcode добавит файл `Info.plist` в проект, однако обновлять конфигурацию по-прежнему лучше через вкладку **Info** цели приложения.