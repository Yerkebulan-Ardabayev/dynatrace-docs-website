---
title: Загрузка и управление файлами символов для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files
---

# Загрузка и управление файлами символов для мобильных приложений в RUM Classic

# Загрузка и управление файлами символов для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение: 8 мин
* Обновлено 12 нояб. 2025 г.

Android iOS tvOS

Подробнее об source maps для веб-приложений: [Поддержка source map для анализа ошибок JavaScript в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как source maps упрощают анализ, воспроизведение и исправление ошибок JavaScript.").

Деобфускация (Android) или символикация (iOS и tvOS), это процесс, который делает классы и методы читаемыми для человека в трассировке стека отчёта о сбое.

Ниже приведён пример трассировки стека Android до и после деобфускации:

![Трассировка стека Android до и после деобфускации](https://dt-cdn.net/images/symbolication-1638-f52b7612e0.png)

Трассировка стека Android до и после деобфускации

Dynatrace позволяет управлять файлами mapping для Android и файлами извлечения символов iOS или tvOS, необходимыми для интерпретации трассировок стека мобильных приложений, которые получает Dynatrace.

Dynatrace поддерживает три способа загрузки этих файлов:

* Через сервис символикации, известный как "Deobfuscation and Symbolication Service" (DSS)
* Через Dynatrace REST API
* Через плагин Fastlane Dynatrace
* Через веб-интерфейс Dynatrace

В настоящее время Dynatrace поддерживает символикацию только тех строк трассировки стека из приложений и сторонних библиотек на iOS и tvOS, для которых были предоставлены файлы dSYM. Символикация строк трассировки стека системных библиотек не поддерживается.

Файл символов можно загрузить в любом поддерживаемом формате (сжатом или несжатом). Учитывайте следующие ограничения:

* Загружаемый файл, не должен превышать 100 МиБ.
* Несжатый файл, после распаковки (если он был сжат) не должен превышать 500 МиБ.

Если файл слишком большой, попробуйте сжать его, чтобы уложиться в лимит загрузки 100 МиБ.

Для загрузки source maps и файлов символов на уровне окружения нужно [право доступа](/managed/manage/identity-access-management/permission-management/role-based-permissions "Права доступа на основе ролей") **Change monitoring settings**.

## Загрузка файлов mapping для Android

Для Android загружайте файлы mapping приложения в исходном виде. Предварительная обработка этих файлов не требуется.

Подробнее о файлах mapping и о том, где их найти, см. в [официальной документации Android﻿](https://developer.android.com/studio/build/shrink-code#decode-stack-trace).

Загрузка файлов mapping через DSSClient

DSSClient позволяет деобфусцировать отчёты о сбоях мобильного приложения или обработанные исключения.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получение DSSClient**](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#get-dssclient "Узнайте о деобфускации (Android) и символикации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Загрузка файлов mapping через DSSClient**](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#upload-mapping-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.")

DSSClient можно использовать только на машинах под управлением macOS.

### Шаг 1 Получение DSSClient

DSSClient можно скачать в веб-интерфейсе Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем приложения.
4. В настройках приложения выберите **Symbol files**.
5. Прокрутите страницу до конца и перейдите по ссылке **DSSClient**.
6. Запустите DSSClient.

   В macOS Catalina система при первом запуске отказывает в запуске DSSClient и показывает предупреждающий диалог. Отмените диалог с предупреждением, перейдите в **System Preferences** > **Security & Privacy** и выберите **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Это поведение вызвано тем, что DSSClient обращается к фреймворку LLDB из Xcode, который не принимается Gatekeeper, независимо от того, что DSSClient нотаризован.

### Шаг 2 Загрузка файлов mapping через DSSClient

Загрузите файл mapping приложения в Dynatrace в исходном виде. Выполните в DSSClient следующую команду:

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 file=/usr/local/mapping.txt server=https://server.com
```

| Параметр | Определение | Где найти |
| --- | --- | --- |
| -upload | Флаг команды. |, |
| appId | ID приложения, который Dynatrace использует для его идентификации. | Веб-интерфейс Dynatrace > **Mobile** > настройки вашего приложения > **Instrumentation wizard** |
| apitoken | Приватный токен, используемый для защищённой коммуникации REST API. | Веб-интерфейс Dynatrace > **Access Tokens** |
| os | ОС, которую нужно обработать (`android`). |, |
| bundleId | Имя пакета приложения, например, `com.yourcompany.app`. |, |
| versionStr | Имя версии приложения. | Файл `build.gradle` |
| version | Код версии приложения. | Файл `build.gradle` |
| file | Путь к файлу mapping, который нужно загрузить. | `build/outputs/mapping/release/mapping.txt` |
| server | URL сервера Dynatrace, например, `xyz.dynatrace.com`. |, |

Полный обзор всех возможных параметров можно получить, запустив бинарный файл `DTXDssClient` с флагом `-h`.

Если нужно удалить файлы mapping, используйте следующую команду:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Загрузка файлов mapping через REST API

[Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление файлами символов мобильных приложений через API Dynatrace.") позволяет автоматизировать загрузку файлов mapping для Android.

Для загрузки файлов mapping приложения в Dynatrace используйте метод [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Загрузите файлы символов для конкретной версии мобильного приложения через API Dynatrace.").

Загрузка файлов mapping через плагин Fastlane

Можно использовать плагин Fastlane Dynatrace, чтобы автоматизировать весь процесс доставки файлов mapping Android в Dynatrace.

Дополнительную информацию и подробные инструкции см. в [документации плагина﻿](https://github.com/Dynatrace/fastlane-plugin-dynatrace) на GitHub.

Загрузка файлов mapping через веб-интерфейс Dynatrace

Также можно использовать веб-интерфейс Dynatrace для загрузки файлов mapping приложения через настройки окружения либо через настройки приложения.

Настройки Environment

Настройки приложения

1. В Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. В разделе **Android** выберите **Upload files**.
3. Выберите приложение из выпадающего списка.
4. Укажите **Package name**, имя пакета приложения, например, `com.yourcompany.app`.
5. Введите **Version code** и **Version name**, их можно найти в файле `build.gradle`.
6. Выберите **Select the file you want to upload** и укажите файл mapping.
7. Выберите **Upload**.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем приложения.
4. В настройках приложения выберите **Symbol files**.
5. В разделе **Android** выберите **Upload files**.
6. Укажите **Package name**, имя пакета приложения, например, `com.yourcompany.app`.
7. Введите **Version code** и **Version name**, их можно найти в файле `build.gradle`.
8. Выберите **Select the file you want to upload** и укажите файл mapping.
9. Выберите **Upload**.

## Загрузка файлов символов для iOS и tvOS

Для символикации iOS или tvOS файлы dSYM необходимо предварительно обработать с помощью DSSClient, прежде чем загружать их в Dynatrace.

Загрузка файлов символов через DSSClient

DSSClient позволяет символизировать отчёты о сбоях мобильного приложения или обработанные исключения.

![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получение файлов dSYM**

![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Получение DSSClient**

![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Предварительная обработка файлов dSYM**

![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Загрузка файлов извлечения символов через DSSClient**

Для iOS нужно получить файлы dSYM, обработать их с помощью DSSClient, а затем загрузить полученные файлы в Dynatrace.

### Шаг 1 Получение файлов dSYM

Используйте файлы dSYM из `.xcarchive` приложения или из каталога сборки.

Загрузка файлов dSYM через архив приложения Xcode

1. В меню Xcode выберите **Window** > **Organizer** > **Archives** > ваше мобильное приложение.
2. Выберите архив с нужной версией приложения и номером сборки.
3. Выберите **Download Debug Symbols**.
4. Щёлкните правой кнопкой мыши по загруженному архиву и выберите **Show in Finder**. Используйте открывшийся файл `.xcarchive` как входные данные в DSSClient (см. следующий шаг).

### Шаг 2 Получение DSSClient

DSSClient можно использовать только на компьютерах под управлением macOS.

DSSClient можно скачать в веб-интерфейсе Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с названием приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. Прокрутить страницу до конца и перейти по ссылке **DSSClient**.
6. Запустить DSSClient.

   В macOS Catalina система блокирует запуск DSSClient при первом старте и показывает предупреждающее окно. Отменить это окно, перейти в **System Preferences** > **Security & Privacy** и выбрать **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient обращается к LLDB-фреймворку Xcode, который Gatekeeper не принимает, независимо от того, нотаризован DSSClient или нет.

### Шаг 3 Предварительная обработка файлов dSYM

Файлы dSYM приложения нужно предварительно обработать перед загрузкой в Dynatrace. Выполнить одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4 Загрузка файлов извлечения символов через DSSClient

Обработанные файлы нужно загрузить в Dynatrace с помощью DSSClient.

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app bundleName=App versionStr=1.0 version=1 symbolsfile=/usr/local/app.xcarchive/dSYMs server=https://server.com
```

| Параметр | Определение | Где найти |
| --- | --- | --- |
| -upload | Флаг команды. |, |
| appId | ID приложения, по которому Dynatrace идентифицирует приложение. | Веб-интерфейс Dynatrace > **Mobile** > настройки приложения > **Instrumentation wizard** |
| apitoken | Приватный токен, используемый для защищённого обмена данными с REST API. | Веб-интерфейс Dynatrace > **Access Tokens** |
| os | ОС, которую нужно обработать: `tvOS` или `iOS`. |, |
| bundleId | bundleId приложения. | Target приложения > General > Bundle Identifier |
| bundleName | bundleName приложения. | Target приложения > General > Display Name |
| versionStr | Строка версии приложения. | Target приложения > General > Version |
| version | Версия приложения. | Target приложения > General > Build |
| symbolsFile | Путь к папке, содержащей файлы dSYM приложения. | `your_app_name.xcarchive/dSYMs` |
| server | URL сервера Dynatrace, например `xyz.dynatrace.com`. |, |

Подробное описание всех возможных параметров можно получить, запустив бинарный файл `DTXDssClient` с флагом `-h`.

Если нужно удалить файлы символов, использовать следующую команду:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Загрузка файлов символов через REST API

[Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.") позволяет автоматизировать загрузку файлов символов.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получение файлов dSYM**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Получение DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Предварительная обработка файлов dSYM**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Загрузка обработанных файлов в Dynatrace через API**

Для iOS нужно получить файлы dSYM, обработать их с помощью DSSClient, а затем загрузить полученные файлы в Dynatrace.

### Шаг 1 Получение файлов dSYM

Использовать файлы dSYM из `.xcarchive` приложения или из папки сборки.

Загрузка файлов dSYM с помощью app archive Xcode

1. В меню Xcode выбрать **Window** > **Organizer** > **Archives** > нужное мобильное приложение.
2. Выбрать архив с требуемой версией приложения и номером сборки.
3. Выбрать **Download Debug Symbols**.
4. Щёлкнуть правой кнопкой мыши по загруженному архиву и выбрать **Show in Finder**. Использовать открывшийся файл `.xcarchive` в качестве входных данных в DSSClient (см. следующий шаг).

### Шаг 2 Получение DSSClient

DSSClient можно использовать только на компьютерах под управлением macOS.

DSSClient можно скачать в веб-интерфейсе Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с названием приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. Прокрутить страницу до конца и перейти по ссылке **DSSClient**.
6. Запустить DSSClient.

   В macOS Catalina система блокирует запуск DSSClient при первом старте и показывает предупреждающее окно. Отменить это окно, перейти в **System Preferences** > **Security & Privacy** и выбрать **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient обращается к LLDB-фреймворку Xcode, который Gatekeeper не принимает, независимо от того, нотаризован DSSClient или нет.

### Шаг 3 Предварительная обработка файлов dSYM

Файлы dSYM приложения нужно предварительно обработать перед загрузкой в Dynatrace. Выполнить одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4 Загрузка обработанных файлов в Dynatrace через API

Обработанные файлы символов нужно загрузить с помощью метода [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Upload symbol files for a specific version of your mobile app via the Dynatrace API.").

Загрузка файлов символов через плагин Fastlane

Плагин Fastlane для Dynatrace позволяет автоматизировать весь процесс, включая получение файлов dSYM из App Store Connect, предварительную обработку файлов и их загрузку в Dynatrace.

Дополнительную информацию и подробные инструкции можно найти в [документации по плагину﻿](https://github.com/Dynatrace/fastlane-plugin-dynatrace) на GitHub.

Загрузка файлов символов через веб-интерфейс Dynatrace

Файлы символов также можно загрузить в Dynatrace через веб-интерфейс Dynatrace.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получение файлов dSYM**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Получение DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Предварительная обработка файлов dSYM**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Загрузка обработанных файлов через веб-интерфейс Dynatrace**

Для iOS нужно получить файлы dSYM, обработать их с помощью DSSClient, а затем загрузить полученные файлы в Dynatrace.

### Шаг 1 Получение файлов dSYM

Использовать файлы dSYM из `.xcarchive` приложения или из папки сборки.

Загрузка файлов dSYM с помощью app archive Xcode

1. В меню Xcode выбрать **Window** > **Organizer** > **Archives** > нужное мобильное приложение.
2. Выбрать архив с требуемой версией приложения и номером сборки.
3. Выбрать **Download Debug Symbols**.
4. Щёлкнуть правой кнопкой мыши по загруженному архиву и выбрать **Show in Finder**. Использовать открывшийся файл `.xcarchive` в качестве входных данных в DSSClient (см. следующий шаг).

### Шаг 2 Получение DSSClient

DSSClient можно использовать только на компьютерах под управлением macOS.

DSSClient можно скачать в веб-интерфейсе Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с названием приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. Прокрутить страницу до конца и перейти по ссылке **DSSClient**.
6. Запустить DSSClient.

   В macOS Catalina система блокирует запуск DSSClient при первом старте и показывает предупреждающее окно. Отменить это окно, перейти в **System Preferences** > **Security & Privacy** и выбрать **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient обращается к LLDB-фреймворку Xcode, который Gatekeeper не принимает, независимо от того, нотаризован DSSClient или нет.

### Шаг 3 Предварительная обработка файлов dSYM

Файлы dSYM приложения нужно предварительно обработать перед загрузкой в Dynatrace. Выполнить одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4. Загрузка обработанных файлов через веб-интерфейс Dynatrace

Веб-интерфейс Dynatrace также можно использовать для загрузки файлов символов через настройки окружения или настройки приложения.

Настройки Environment

Настройки приложения

1. В Dynatrace перейти в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. В разделе **iOS** или **tvOS** выбрать **Upload files**.
3. Выбрать своё приложение из выпадающего списка.
4. Указать **Bundle identifier**, это `bundleId` приложения, его можно найти в **App's target** > **General** > **Bundle Identifier**.
5. Ввести **Bundle version** из **App's target** > **General** > **Version** и **Bundle version string** из **App's target** > **General** > **Build**.
6. Выбрать **Select the file you want to upload** и открыть файл символов.
7. Выбрать **Upload**.

1. Перейти в **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В верхнем правом углу плитки с именем приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. В разделе **iOS** или **tvOS** выбрать **Upload files**.
6. Указать **Bundle identifier**, это `bundleId` приложения, его можно найти в **App's target** > **General** > **Bundle Identifier**.
7. Ввести **Bundle version** из **App's target** > **General** > **Version** и **Bundle version string** из **App's target** > **General** > **Build**.
8. Выбрать **Select the file you want to upload** и открыть файл символов.
9. Выбрать **Upload**.

## Управление загруженными файлами символов

Веб-интерфейс Dynatrace можно использовать для управления ранее загруженными файлами Android mapping и файлами извлечения символов iOS или tvOS.

Чтобы получить список загруженных файлов символов для конкретного приложения

1. Перейти в **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В верхнем правом углу плитки с именем приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.

Чтобы получить список загруженных source maps и файлов символов для всех приложений

1. Перейти в **Settings**.
2. Выбрать **Web and mobile monitoring** > **Source maps and symbol files**.

На странице отображается объём хранилища, используемый в данный момент, и лимит хранилища. При достижении лимита хранилища Dynatrace начинает удалять source maps и файлы символов, начиная с самых старых.

Для Dynatrace Managed размер хранилища по умолчанию для файлов символов и mapping составляет 1 GiB. Размер хранилища можно изменить в соответствии со своими требованиями.

Чтобы освободить место, можно вручную удалить файлы, которые больше не нужны. Выбрать **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") в строке файла, который нужно удалить.

Чтобы файлы не удалялись автоматически при достижении лимита хранилища, нужно включить **Pinned** для source maps и файлов символов, которые нужно сохранить.

Также можно использовать [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.") для просмотра, закрепления или удаления файлов символов.