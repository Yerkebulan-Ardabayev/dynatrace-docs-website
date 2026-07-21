---
title: Загрузка и управление файлами символов для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files
---

# Загрузка и управление файлами символов для мобильных приложений в RUM Classic

# Загрузка и управление файлами символов для мобильных приложений в RUM Classic

* Практическое руководство
* 8 мин чтения
* Обновлено 12 нояб. 2025 г.

Android iOS tvOS

Подробнее об исходных картах (source maps) для веб-приложений см. [Поддержка исходных карт для анализа ошибок JavaScript в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как исходные карты упрощают анализ, воспроизведение и исправление ошибок JavaScript.").

Деобфускация (Android) или символикация (iOS и tvOS), это процесс преобразования классов и методов в трассировке стека отчёта об аварийном завершении в удобочитаемый вид.

Ниже приведён пример трассировки стека Android до и после деобфускации:

![Трассировка стека Android до и после деобфускации](https://dt-cdn.net/images/symbolication-1638-f52b7612e0.png)

Трассировка стека Android до и после деобфускации

Dynatrace позволяет управлять файлами сопоставления Android и файлами извлечения символов iOS или tvOS, необходимыми для интерпретации мобильных трассировок стека, которые получает Dynatrace.

Dynatrace поддерживает три различных способа загрузки этих файлов:

* Через сервис символикации, известный как "Deobfuscation and Symbolication Service" (DSS)
* Через Dynatrace REST API
* Через плагин Fastlane Dynatrace
* Через веб-интерфейс Dynatrace

В настоящее время Dynatrace поддерживает символикацию строк трассировки стека только для приложений и сторонних библиотек на iOS и tvOS, для которых были предоставлены файлы dSYM. Символикация строк трассировки стека системных библиотек не поддерживается.

Файл символов можно загрузить в любом поддерживаемом формате (сжатом или несжатом). Учитывайте следующие ограничения:

* Загружаемый файл, не должен превышать 100 МиБ.
* Несжатый файл, не должен превышать 500 МиБ после распаковки (если файл сжат).

Если файл слишком большой, попробуйте сжать его, чтобы уложиться в лимит загрузки 100 МиБ.

Для загрузки исходных карт и файлов символов на уровне окружения требуется [разрешение](/managed/manage/identity-access-management/permission-management/role-based-permissions "Разрешения на основе ролей") **Change monitoring settings**.

## Загрузка файлов сопоставления для Android

Для Android загружайте файлы сопоставления приложения в их исходном виде. Предварительная обработка этих файлов не требуется.

Подробнее о файлах сопоставления и о том, где их найти, см. в [официальной документации Android﻿](https://developer.android.com/studio/build/shrink-code#decode-stack-trace).

Загрузка файлов сопоставления через DSSClient

DSSClient позволяет деобфусцировать отчёты об аварийном завершении мобильного приложения или обработанные исключения.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получить DSSClient**](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#get-dssclient "Узнайте о деобфускации (Android) и символикации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Загрузить файлы сопоставления через DSSClient**](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#upload-mapping-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.")

DSSClient можно использовать только на компьютерах под управлением macOS.

### Шаг 1 Получить DSSClient

DSSClient можно скачать из веб-интерфейса Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем приложения.
4. В настройках приложения выберите **Symbol files**.
5. Прокрутите страницу до конца и перейдите по ссылке **DSSClient**.
6. Запустите DSSClient.

   В macOS Catalina система при первом запуске отказывает в запуске DSSClient и отображает предупреждающее диалоговое окно. Отмените предупреждающее окно, перейдите в **System Preferences** > **Security & Privacy** и выберите **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient ссылается на фреймворк LLDB Xcode, который не принимается Gatekeeper, независимо от того, что DSSClient нотаризован.

### Шаг 2 Загрузить файлы сопоставления через DSSClient

Загрузите файл сопоставления приложения в Dynatrace в исходном виде. Выполните следующую команду в DSSClient:

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 file=/usr/local/mapping.txt server=https://server.com
```

| Параметр | Определение | Где найти |
| --- | --- | --- |
| -upload | Флаг команды. | — |
| appId | ID приложения, который Dynatrace использует для идентификации приложения. | Веб-интерфейс Dynatrace > **Mobile** > настройки приложения > **Instrumentation wizard** |
| apitoken | Приватный токен, используемый для безопасной связи REST API. | Веб-интерфейс Dynatrace > **Access Tokens** |
| os | ОС, которую нужно обработать (`android`). | — |
| bundleId | Имя пакета приложения, например `com.yourcompany.app`. | — |
| versionStr | Имя версии приложения. | Файл `build.gradle` |
| version | Код версии приложения. | Файл `build.gradle` |
| file | Путь к файлу сопоставления, который нужно загрузить. | `build/outputs/mapping/release/mapping.txt` |
| server | URL сервера Dynatrace, например `xyz.dynatrace.com`. | — |

Подробный обзор всех возможных параметров можно получить, запустив бинарный файл `DTXDssClient` с флагом `-h`.

Если нужно удалить файлы сопоставления, используйте следующую команду:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Загрузка файлов сопоставления через REST API

[Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управление файлами символов мобильных приложений через API Dynatrace.") позволяет автоматизировать загрузку файлов сопоставления Android.

Чтобы загрузить файлы сопоставления приложения в Dynatrace, используйте метод [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Загрузите файлы символов для конкретной версии мобильного приложения через API Dynatrace.").

Загрузка файлов сопоставления через плагин Fastlane

Плагин Fastlane Dynatrace можно использовать для автоматизации всего процесса передачи файлов сопоставления Android в Dynatrace.

Подробнее и пошаговые инструкции см. в [документации плагина﻿](https://github.com/Dynatrace/fastlane-plugin-dynatrace) на GitHub.

Загрузка файлов сопоставления через веб-интерфейс Dynatrace

Веб-интерфейс Dynatrace также можно использовать для загрузки файлов сопоставления приложения либо через настройки окружения, либо через настройки приложения.

Настройки Environment

Настройки приложения

1. В Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. В разделе **Android** выберите **Upload files**.
3. Выберите приложение из выпадающего списка.
4. Укажите **Package name**, имя пакета приложения, например `com.yourcompany.app`.
5. Введите **Version code** и **Version name**, их можно найти в файле `build.gradle`.
6. Выберите **Select the file you want to upload** и укажите файл сопоставления.
7. Выберите **Upload**.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем приложения.
4. В настройках приложения выберите **Symbol files**.
5. В разделе **Android** выберите **Upload files**.
6. Укажите **Package name**, имя пакета приложения, например `com.yourcompany.app`.
7. Введите **Version code** и **Version name**, их можно найти в файле `build.gradle`.
8. Выберите **Select the file you want to upload** и укажите файл сопоставления.
9. Выберите **Upload**.

## Загрузка файлов символов для iOS и tvOS

Для символикации iOS или tvOS файлы dSYM необходимо предварительно обработать с помощью DSSClient, прежде чем загружать их в Dynatrace.

Загрузка файлов символов через DSSClient

DSSClient позволяет символицировать отчёты об аварийном завершении мобильного приложения или обработанные исключения.

![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получить файлы dSYM**

![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Получить DSSClient**

![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Предварительно обработать файлы dSYM**

![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Загрузить файлы извлечения символов через DSSClient**

Для iOS нужно получить файлы dSYM, предварительно обработать их с помощью DSSClient, а затем загрузить полученные файлы в Dynatrace.

### Шаг 1 Получить файлы dSYM

Используйте файлы dSYM из `.xcarchive` приложения или из директории сборки.

Скачивание файлов dSYM через архив приложения Xcode

1. В меню Xcode выберите **Window** > **Organizer** > **Archives** > ваше мобильное приложение.
2. Выберите архив с нужной версией приложения и номером сборки.
3. Выберите **Download Debug Symbols**.
4. Щёлкните правой кнопкой мыши по загруженному архиву и выберите **Show in Finder**. Используйте раскрытый файл `.xcarchive` как входные данные в DSSClient (см. следующий шаг).

### Шаг 2 Получить DSSClient

DSSClient можно использовать только на компьютерах с macOS.

DSSClient можно скачать из веб-интерфейса Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с названием приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. Прокрутить страницу до конца и перейти по ссылке **DSSClient**.
6. Запустить DSSClient.

   В macOS Catalina система запрещает запуск DSSClient при первом запуске и показывает предупреждающий диалог. Нужно отменить предупреждающий диалог, перейти в **System Preferences** > **Security & Privacy** и выбрать **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient обращается к фреймворку LLDB из Xcode, который Gatekeeper не принимает, независимо от того, что DSSClient нотаризован.

### Шаг 3 Предварительная обработка файлов dSYM

Перед загрузкой файлов dSYM в Dynatrace их нужно предварительно обработать. Выполнить одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4 Загрузка файлов извлечения символов через DSSClient

Загрузить обработанные файлы в Dynatrace с помощью DSSClient.

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app bundleName=App versionStr=1.0 version=1 symbolsfile=/usr/local/app.xcarchive/dSYMs server=https://server.com
```

| Опция | Определение | Где найти |
| --- | --- | --- |
| -upload | Флаг команды. | — |
| appId | ID приложения, который Dynatrace использует для идентификации приложения. | Веб-интерфейс Dynatrace > **Mobile** > настройки приложения > **Instrumentation wizard** |
| apitoken | Приватный токен, который используется для защищённой коммуникации REST API. | Веб-интерфейс Dynatrace > **Access Tokens** |
| os | ОС, которая должна быть обработана, `tvOS` или `iOS`. | — |
| bundleId | BundleId приложения. | Target приложения > General > Bundle Identifier |
| bundleName | BundleName приложения. | Target приложения > General > Display Name |
| versionStr | Строка версии приложения. | Target приложения > General > Version |
| version | Версия приложения. | Target приложения > General > Build |
| symbolsFile | Путь к папке, содержащей файлы dSYM приложения. | `your_app_name.xcarchive/dSYMs` |
| server | URL сервера Dynatrace, например `xyz.dynatrace.com`. | — |

Подробный обзор всех возможных параметров можно получить, запустив бинарник `DTXDssClient` с флагом `-h`.

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

Для iOS нужно получить файлы dSYM, предварительно обработать их с помощью DSSClient, а затем загрузить полученные файлы в Dynatrace.

### Шаг 1 Получение файлов dSYM

Использовать файлы dSYM из `.xcarchive` приложения или директории сборки.

Скачивание файлов dSYM с помощью app archive в Xcode

1. В меню Xcode выбрать **Window** > **Organizer** > **Archives** > нужное мобильное приложение.
2. Выбрать архив с нужной версией приложения и номером сборки.
3. Выбрать **Download Debug Symbols**.
4. Нажать правой кнопкой мыши на скачанный архив и выбрать **Show in Finder**. Использовать открывшийся файл `.xcarchive` как входные данные в DSSClient (см. следующий шаг).

### Шаг 2 Получение DSSClient

DSSClient можно использовать только на компьютерах с macOS.

DSSClient можно скачать из веб-интерфейса Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с названием приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. Прокрутить страницу до конца и перейти по ссылке **DSSClient**.
6. Запустить DSSClient.

   В macOS Catalina система запрещает запуск DSSClient при первом запуске и показывает предупреждающий диалог. Нужно отменить предупреждающий диалог, перейти в **System Preferences** > **Security & Privacy** и выбрать **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient обращается к фреймворку LLDB из Xcode, который Gatekeeper не принимает, независимо от того, что DSSClient нотаризован.

### Шаг 3 Предварительная обработка файлов dSYM

Перед загрузкой файлов dSYM в Dynatrace их нужно предварительно обработать. Выполнить одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4 Загрузка обработанных файлов в Dynatrace через API

Загрузить обработанные файлы символов с помощью метода [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Upload symbol files for a specific version of your mobile app via the Dynatrace API.").

Загрузка файлов символов через плагин Fastlane

Плагин Fastlane для Dynatrace можно использовать для автоматизации всего процесса, включая получение файлов dSYM из App Store Connect, предварительную обработку файлов и загрузку файлов в Dynatrace.

Подробнее и пошаговые инструкции можно найти в [документации плагина﻿](https://github.com/Dynatrace/fastlane-plugin-dynatrace) на GitHub.

Загрузка файлов символов через веб-интерфейс Dynatrace

Веб-интерфейс Dynatrace также можно использовать для загрузки файлов символов в Dynatrace.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получение файлов dSYM**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Получение DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Предварительная обработка файлов dSYM**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Загрузка обработанных файлов через веб-интерфейс Dynatrace**

Для iOS нужно получить файлы dSYM, предварительно обработать их с помощью DSSClient, а затем загрузить полученные файлы в Dynatrace.

### Шаг 1 Получение файлов dSYM

Использовать файлы dSYM из `.xcarchive` приложения или директории сборки.

Скачивание файлов dSYM с помощью app archive в Xcode

1. В меню Xcode выбрать **Window** > **Organizer** > **Archives** > нужное мобильное приложение.
2. Выбрать архив с нужной версией приложения и номером сборки.
3. Выбрать **Download Debug Symbols**.
4. Нажать правой кнопкой мыши на скачанный архив и выбрать **Show in Finder**. Использовать открывшийся файл `.xcarchive` как входные данные в DSSClient (см. следующий шаг).

### Шаг 2 Получение DSSClient

DSSClient можно использовать только на компьютерах с macOS.

DSSClient можно скачать из веб-интерфейса Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с названием приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Symbol files**.
5. Прокрутить страницу до конца и перейти по ссылке **DSSClient**.
6. Запустить DSSClient.

   В macOS Catalina система запрещает запуск DSSClient при первом запуске и показывает предупреждающий диалог. Нужно отменить предупреждающий диалог, перейти в **System Preferences** > **Security & Privacy** и выбрать **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Такое поведение вызвано тем, что DSSClient обращается к фреймворку LLDB из Xcode, который Gatekeeper не принимает, независимо от того, что DSSClient нотаризован.

### Шаг 3 Предварительная обработка файлов dSYM

Перед загрузкой файлов dSYM в Dynatrace их нужно предварительно обработать. Выполнить одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4 Загрузка обработанных файлов через веб-интерфейс Dynatrace

Также можно использовать веб-интерфейс Dynatrace для загрузки файлов символов через настройки среды или настройки приложения.

Environment настройки

Настройки приложения

1. В Dynatrace перейти в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. В разделе **iOS** или **tvOS** выбрать **Upload files**.
3. Выбрать приложение из выпадающего списка.
4. Указать **Bundle identifier**, это `bundleId` приложения, который находится в **App's target** > **General** > **Bundle Identifier**.
5. Ввести **Bundle version** из **App's target** > **General** > **Version** и **Bundle version string** из **App's target** > **General** > **Build**.
6. Выбрать **Select the file you want to upload** и открыть файл символов.
7. Выбрать **Upload**.

1. Перейти в **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. Выбрать **More** (**…**) > **Edit** в верхнем правом углу плитки с названием приложения.
4. В настройках приложения выбрать **Symbol files**.
5. В разделе **iOS** или **tvOS** выбрать **Upload files**.
6. Указать **Bundle identifier**, это `bundleId` приложения, который находится в **App's target** > **General** > **Bundle Identifier**.
7. Ввести **Bundle version** из **App's target** > **General** > **Version** и **Bundle version string** из **App's target** > **General** > **Build**.
8. Выбрать **Select the file you want to upload** и открыть файл символов.
9. Выбрать **Upload**.

## Управление загруженными файлами символов

Веб-интерфейс Dynatrace можно использовать для управления ранее загруженными файлами mapping для Android и файлами symbol extract для iOS или tvOS.

Чтобы просмотреть список загруженных файлов символов для конкретного приложения

1. Перейти в **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. Выбрать **More** (**…**) > **Edit** в верхнем правом углу плитки с названием приложения.
4. В настройках приложения выбрать **Symbol files**.

Чтобы просмотреть список загруженных source map и файлов символов для всех приложений

1. Перейти в **Settings**.
2. Выбрать **Web and mobile monitoring** > **Source maps and symbol files**.

На странице отображается объём хранилища, используемый в данный момент, и лимит хранилища. При достижении лимита хранилища Dynatrace начинает удалять source map и файлы символов, начиная с самых старых.

Для Dynatrace Managed размер хранилища для файлов символов и mapping по умолчанию составляет 1 GiB. Размер хранилища можно изменить в соответствии со своими требованиями.

Чтобы освободить место, можно вручную удалить файлы, которые больше не нужны. Выбрать **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") в строке файла, который нужно удалить.

Чтобы файлы не удалялись автоматически при достижении лимита хранилища, включить **Pinned** для source map и файлов символов, которые нужно сохранить.

Также можно использовать [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.") для просмотра, закрепления или удаления файлов символов.