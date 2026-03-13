---
title: Info.plist file
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file
scraped: 2026-03-06T21:38:07.966569
---

# Info.plist file

# Info.plist file

* Classic
* Explanation
* 2-min read
* Updated on Apr 26, 2024

При использовании Dynatrace файл `Info.plist` хранит ключи идентификации и конфигурации вашего приложения. Ниже приведена некоторая информация об этом файле.

* Файл `Info.plist` доступен в навигаторе проекта Xcode в разделе **Supporting Files**. Для более старых файлов проекта `Info.plist` расположен в разделе **Resources**.
* Независимо от выбранного подхода к настройке RUM для вашего приложения, добавьте ключи идентификации приложения (идентификатор приложения и URL-адрес маяка) в файл `Info.plist` вашего проекта; ключи [`DTXApplicationID` и `DTXBeaconURL`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") всегда обязательны. Без ключей идентификации приложения ваше мобильное приложение не сможет отправлять данные мониторинга в Dynatrace.

  Для проверки ключей идентификации приложения используйте [мастер инструментирования мобильных приложений](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
* Вы также можете использовать `Info.plist` для включения или отключения дополнительных функций мониторинга, добавив [ключи конфигурации](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в этот файл.
* Чтобы сохранить файл `Info.plist` вашего приложения в чистоте, вы можете переместить все ключи `DTX`, связанные с OneAgent, в файл `Dynatrace.plist` и добавить `Dynatrace.plist` в фазу сборки `Copy Bundle Resources`. Файл `Dynatrace.plist` должен находиться в корне пакета ресурсов, поэтому создайте этот файл в том же месте, что и файл `Info.plist`.
* В некоторых случаях файл `Info.plist` не создаётся при использовании Xcode. Например, при создании нового проекта SwiftUI вы можете заметить, что в проекте отсутствует этот файл. Дополнительные сведения см. в [примечаниях к выпуску Xcode; проблема 68254857ï»¿](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes#Templates).

  Если у вас нет файла `Info.plist`, добавьте ключи идентификации приложения и [ключи конфигурации](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") вручную как **Custom iOS Target Properties** на вкладке **Info** целевого объекта вашего приложения. После внесения этого изменения Xcode добавит файл `Info.plist` в проект, однако по-прежнему рекомендуется обновлять конфигурацию через вкладку **Info** целевого объекта приложения.
