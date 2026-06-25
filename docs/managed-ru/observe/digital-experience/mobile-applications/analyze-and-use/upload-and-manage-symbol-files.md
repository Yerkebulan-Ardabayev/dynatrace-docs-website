---
title: Загрузка файлов символов и управление ими для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files
scraped: 2026-05-12T11:19:40.061601
---

# Загрузка файлов символов и управление ими для мобильных приложений

# Загрузка файлов символов и управление ими для мобильных приложений

* How-to guide
* 8-min read
* Updated on Nov 12, 2025

Android iOS tvOS

Информацию об исходных картах для веб-приложений см. в разделе [Поддержка исходных карт для анализа ошибок JavaScript](/managed/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как исходные карты упрощают анализ, воспроизведение и исправление ошибок JavaScript.").

Деобфускация (Android) или символикация (iOS и tvOS) — это процесс перевода классов и методов в читаемый формат в трассировке стека отчёта о сбое.

Следующий пример показывает трассировку стека Android до и после деобфускации:

![Android stack trace before and after deobfuscation](https://dt-cdn.net/images/symbolication-1638-f52b7612e0.png)

Android stack trace before and after deobfuscation

Dynatrace позволяет управлять файлами сопоставления Android и файлами извлечения символов iOS или tvOS, необходимыми для интерпретации мобильных трассировок стека, получаемых Dynatrace.

Dynatrace поддерживает три способа загрузки этих файлов:

* Через службу символикации (Deobfuscation and Symbolication Service, DSS)
* Через REST API Dynatrace
* Через плагин Dynatrace Fastlane
* Через веб-интерфейс Dynatrace

В настоящее время Dynatrace поддерживает символикацию только строк трассировки стека из приложений и сторонних библиотек на iOS и tvOS, для которых были предоставлены файлы dSYM. Символикация строк трассировки стека системных библиотек не поддерживается.

Вы можете загружать файлы символов в любом поддерживаемом формате (сжатом или несжатом). Учитывайте следующие ограничения:

* Загружаемый файл не должен превышать 100 МиБ.
* Несжатый файл не должен превышать 500 МиБ после распаковки (если он сжат).

Если файл слишком большой, попробуйте его сжать, чтобы уложиться в лимит загрузки 100 МиБ.

Для загрузки исходных карт и файлов символов вам необходимо разрешение **Change monitoring settings** на уровне окружения ([разрешения на основе ролей](/managed/manage/identity-access-management/permission-management/role-based-permissions "Разрешения на основе ролей")).

## Загрузка файлов сопоставления для Android

Для Android загружайте файлы сопоставления приложения в исходном виде. Предварительная обработка этих файлов не требуется.

Дополнительные сведения о файлах сопоставления и их расположении см. в [официальной документации Android](https://developer.android.com/studio/build/shrink-code#decode-stack-trace).

Загрузка файлов сопоставления через DSSClient

DSSClient позволяет деобфусцировать отчёты о сбоях или обработанные исключения мобильных приложений.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получить DSSClient**](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#get-dssclient "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и вариантах загрузки файлов символов в Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Загрузить файлы сопоставления через DSSClient**](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#upload-mapping-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и вариантах загрузки файлов символов в Dynatrace.")

DSSClient можно использовать только на компьютерах под управлением macOS.

### Шаг 1. Получение DSSClient

Вы можете скачать DSSClient из веб-интерфейса Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.
5. Прокрутите страницу вниз и перейдите по ссылке **DSSClient**.
6. Запустите DSSClient.

   На macOS Catalina система запрещает запуск DSSClient при первом запуске и отображает предупреждение. Закройте предупреждение, перейдите в **System Preferences** > **Security & Privacy** и нажмите **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Это поведение вызвано тем, что DSSClient ссылается на LLDB framework из Xcode, который не принимается Gatekeeper, независимо от наличия нотаризации DSSClient.

### Шаг 2. Загрузка файлов сопоставления через DSSClient

Загрузите файлы сопоставления приложения в Dynatrace в исходном виде. Выполните следующую команду в DSSClient:

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 file=/usr/local/mapping.txt server=https://server.com
```

| Параметр | Определение | Где найти |
| --- | --- | --- |
| -upload | Флаг команды. | — |
| appId | Идентификатор приложения, используемый Dynatrace. | Веб-интерфейс Dynatrace > **Mobile** > настройки приложения > **Instrumentation wizard** |
| apitoken | Приватный токен для защищённой связи через REST API. | Веб-интерфейс Dynatrace > **Access Tokens** |
| os | ОС для обработки (`android`). | — |
| bundleId | Имя пакета приложения, например `com.yourcompany.app`. | — |
| versionStr | Имя версии приложения. | Файл `build.gradle` |
| version | Код версии приложения. | Файл `build.gradle` |
| file | Путь к файлу сопоставления для загрузки. | `build/outputs/mapping/release/mapping.txt` |
| server | URL сервера Dynatrace, например `xyz.dynatrace.com`. | — |

Для получения подробного обзора всех возможных параметров запустите бинарный файл `DTXDssClient` с флагом `-h`.

Для удаления файлов сопоставления используйте следующую команду:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Загрузка файлов сопоставления через REST API

[Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управляйте мобильными файлами символов через Dynatrace API.") позволяет автоматизировать загрузку файлов сопоставления Android.

Для загрузки файлов сопоставления приложения в Dynatrace используйте метод [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Загружайте файлы символов для конкретной версии мобильного приложения через Dynatrace API.").

Загрузка файлов сопоставления через плагин Fastlane

Вы можете использовать плагин Dynatrace Fastlane для автоматизации всего процесса доставки файлов сопоставления Android в Dynatrace.

Дополнительные сведения и подробные инструкции см. в [документации плагина](https://github.com/Dynatrace/fastlane-plugin-dynatrace) на GitHub.

Загрузка файлов сопоставления через веб-интерфейс Dynatrace

Вы также можете использовать веб-интерфейс Dynatrace для загрузки файлов сопоставления через настройки окружения или настройки приложения.

Настройки окружения

Настройки приложения

1. В Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. В разделе **Android** нажмите **Upload files**.
3. Выберите приложение из раскрывающегося списка.
4. Укажите **Package name** — имя пакета приложения, например `com.yourcompany.app`.
5. Введите **Version code** и **Version name** — их можно найти в файле `build.gradle`.
6. Нажмите **Select the file you want to upload** и выберите файл сопоставления.
7. Нажмите **Upload**.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.
5. В разделе **Android** нажмите **Upload files**.
6. Укажите **Package name** — имя пакета приложения, например `com.yourcompany.app`.
7. Введите **Version code** и **Version name** — их можно найти в файле `build.gradle`.
8. Нажмите **Select the file you want to upload** и выберите файл сопоставления.
9. Нажмите **Upload**.

## Загрузка файлов символов для iOS и tvOS

Для символикации iOS или tvOS необходимо предварительно обработать файлы dSYM с помощью DSSClient перед загрузкой в Dynatrace.

Загрузка файлов символов через DSSClient

DSSClient позволяет символицировать отчёты о сбоях или обработанные исключения мобильных приложений.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получение файлов dSYM**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Получение DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Предварительная обработка файлов dSYM**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Загрузка файлов символов через DSSClient**

Для iOS необходимо получить файлы dSYM, обработать их с помощью DSSClient и затем загрузить результирующие файлы в Dynatrace.

### Шаг 1. Получение файлов dSYM

Используйте файлы dSYM из архива приложения `.xcarchive` или директории сборки.

Чтобы скачать файлы dSYM с помощью архива приложения Xcode:

1. В меню Xcode выберите **Window** > **Organizer** > **Archives** > ваше мобильное приложение.
2. Выберите архив с нужной версией приложения и номером сборки.
3. Нажмите **Download Debug Symbols**.
4. Щёлкните правой кнопкой мыши на скачанном архиве и выберите **Show in Finder**. Используйте открытый файл `.xcarchive` в качестве входных данных для DSSClient (см. следующий шаг).

### Шаг 2. Получение DSSClient

DSSClient можно использовать только на компьютерах под управлением macOS.

Вы можете скачать DSSClient из веб-интерфейса Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.
5. Прокрутите страницу вниз и перейдите по ссылке **DSSClient**.
6. Запустите DSSClient.

   На macOS Catalina система запрещает запуск DSSClient при первом запуске и отображает предупреждение. Закройте предупреждение, перейдите в **System Preferences** > **Security & Privacy** и нажмите **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Это поведение вызвано тем, что DSSClient ссылается на LLDB framework из Xcode, который не принимается Gatekeeper, независимо от наличия нотаризации DSSClient.

### Шаг 3. Предварительная обработка файлов dSYM

Обработайте файлы dSYM приложения перед загрузкой в Dynatrace. Выполните одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4. Загрузка файлов символов через DSSClient

Загрузите обработанные файлы в Dynatrace с помощью DSSClient.

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app bundleName=App versionStr=1.0 version=1 symbolsfile=/usr/local/app.xcarchive/dSYMs server=https://server.com
```

| Параметр | Определение | Где найти |
| --- | --- | --- |
| -upload | Флаг команды. | — |
| appId | Идентификатор приложения, используемый Dynatrace. | Веб-интерфейс Dynatrace > **Mobile** > настройки приложения > **Instrumentation wizard** |
| apitoken | Приватный токен для защищённой связи через REST API. | Веб-интерфейс Dynatrace > **Access Tokens** |
| os | ОС для обработки: `tvOS` или `iOS`. | — |
| bundleId | Идентификатор пакета приложения (bundleId). | Target приложения > General > Bundle Identifier |
| bundleName | Имя пакета приложения (bundleName). | Target приложения > General > Display Name |
| versionStr | Строка версии приложения. | Target приложения > General > Version |
| version | Версия приложения. | Target приложения > General > Build |
| symbolsFile | Путь к папке с файлами dSYM приложения. | `your_app_name.xcarchive/dSYMs` |
| server | URL сервера Dynatrace, например `xyz.dynatrace.com`. | — |

Для получения подробного обзора всех возможных параметров запустите бинарный файл `DTXDssClient` с флагом `-h`.

Для удаления файлов символов используйте следующую команду:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Загрузка файлов символов через REST API

[Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управляйте мобильными файлами символов через Dynatrace API.") позволяет автоматизировать загрузку файлов символов.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получение файлов dSYM**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Получение DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Предварительная обработка файлов dSYM**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Загрузка обработанных файлов в Dynatrace через API**

Для iOS необходимо получить файлы dSYM, обработать их с помощью DSSClient и затем загрузить результирующие файлы в Dynatrace.

### Шаг 1. Получение файлов dSYM

Используйте файлы dSYM из архива приложения `.xcarchive` или директории сборки.

Чтобы скачать файлы dSYM с помощью архива приложения Xcode:

1. В меню Xcode выберите **Window** > **Organizer** > **Archives** > ваше мобильное приложение.
2. Выберите архив с нужной версией приложения и номером сборки.
3. Нажмите **Download Debug Symbols**.
4. Щёлкните правой кнопкой мыши на скачанном архиве и выберите **Show in Finder**. Используйте открытый файл `.xcarchive` в качестве входных данных для DSSClient (см. следующий шаг).

### Шаг 2. Получение DSSClient

DSSClient можно использовать только на компьютерах под управлением macOS.

Вы можете скачать DSSClient из веб-интерфейса Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.
5. Прокрутите страницу вниз и перейдите по ссылке **DSSClient**.
6. Запустите DSSClient.

   На macOS Catalina система запрещает запуск DSSClient при первом запуске и отображает предупреждение. Закройте предупреждение, перейдите в **System Preferences** > **Security & Privacy** и нажмите **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Это поведение вызвано тем, что DSSClient ссылается на LLDB framework из Xcode, который не принимается Gatekeeper, независимо от наличия нотаризации DSSClient.

### Шаг 3. Предварительная обработка файлов dSYM

Обработайте файлы dSYM приложения перед загрузкой в Dynatrace. Выполните одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4. Загрузка обработанных файлов в Dynatrace через API

Загрузите обработанные файлы символов с помощью метода [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Загружайте файлы символов для конкретной версии мобильного приложения через Dynatrace API.").

Загрузка файлов символов через плагин Fastlane

Вы можете использовать плагин Dynatrace Fastlane для автоматизации всего процесса: получения файлов dSYM из App Store Connect, их предварительной обработки и загрузки в Dynatrace.

Дополнительные сведения и подробные инструкции см. в [документации плагина](https://github.com/Dynatrace/fastlane-plugin-dynatrace) на GitHub.

Загрузка файлов символов через веб-интерфейс Dynatrace

Вы также можете использовать веб-интерфейс Dynatrace для загрузки файлов символов.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Получение файлов dSYM**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Получение DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Предварительная обработка файлов dSYM**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Загрузка обработанных файлов через веб-интерфейс Dynatrace**

Для iOS необходимо получить файлы dSYM, обработать их с помощью DSSClient и затем загрузить результирующие файлы в Dynatrace.

### Шаг 1. Получение файлов dSYM

Используйте файлы dSYM из архива приложения `.xcarchive` или директории сборки.

Чтобы скачать файлы dSYM с помощью архива приложения Xcode:

1. В меню Xcode выберите **Window** > **Organizer** > **Archives** > ваше мобильное приложение.
2. Выберите архив с нужной версией приложения и номером сборки.
3. Нажмите **Download Debug Symbols**.
4. Щёлкните правой кнопкой мыши на скачанном архиве и выберите **Show in Finder**. Используйте открытый файл `.xcarchive` в качестве входных данных для DSSClient (см. следующий шаг).

### Шаг 2. Получение DSSClient

DSSClient можно использовать только на компьютерах под управлением macOS.

Вы можете скачать DSSClient из веб-интерфейса Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.
5. Прокрутите страницу вниз и перейдите по ссылке **DSSClient**.
6. Запустите DSSClient.

   На macOS Catalina система запрещает запуск DSSClient при первом запуске и отображает предупреждение. Закройте предупреждение, перейдите в **System Preferences** > **Security & Privacy** и нажмите **Open Anyway**, чтобы разрешить запуск DSSClient.  
   Это поведение вызвано тем, что DSSClient ссылается на LLDB framework из Xcode, который не принимается Gatekeeper, независимо от наличия нотаризации DSSClient.

### Шаг 3. Предварительная обработка файлов dSYM

Обработайте файлы dSYM приложения перед загрузкой в Dynatrace. Выполните одну из следующих команд в DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Шаг 4. Загрузка обработанных файлов через веб-интерфейс Dynatrace

Вы также можете использовать веб-интерфейс Dynatrace для загрузки файлов символов через настройки окружения или настройки приложения.

Настройки окружения

Настройки приложения

1. В Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. В разделе **iOS** или **tvOS** нажмите **Upload files**.
3. Выберите приложение из раскрывающегося списка.
4. Укажите **Bundle identifier** — это `bundleId` приложения из **App's target** > **General** > **Bundle Identifier**.
5. Введите **Bundle version** из **App's target** > **General** > **Version** и **Bundle version string** из **App's target** > **General** > **Build**.
6. Нажмите **Select the file you want to upload** и откройте файл символов.
7. Нажмите **Upload**.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.
5. В разделе **iOS** или **tvOS** нажмите **Upload files**.
6. Укажите **Bundle identifier** — это `bundleId` приложения из **App's target** > **General** > **Bundle Identifier**.
7. Введите **Bundle version** из **App's target** > **General** > **Version** и **Bundle version string** из **App's target** > **General** > **Build**.
8. Нажмите **Select the file you want to upload** и откройте файл символов.
9. Нажмите **Upload**.

## Управление загруженными файлами символов

Вы можете использовать веб-интерфейс Dynatrace для управления ранее загруженными файлами сопоставления Android и файлами символов iOS или tvOS.

Чтобы просмотреть загруженные файлы символов для конкретного приложения:

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Symbol files**.

Чтобы просмотреть загруженные исходные карты и файлы символов для всех приложений:

1. Перейдите в **Settings**.
2. Выберите **Web and mobile monitoring** > **Source maps and symbol files**.

На странице отображается текущий объём используемого хранилища и его лимит. При достижении лимита Dynatrace начинает удалять исходные карты и файлы символов, начиная с самых старых.

Для Dynatrace Managed объём хранилища файлов символов и сопоставления по умолчанию составляет 1 ГиБ. Вы можете изменить размер хранилища в соответствии с вашими требованиями.

Для освобождения места вы можете вручную удалять файлы, которые больше не нужны. Нажмите **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") в строке файла, который нужно удалить.

Чтобы предотвратить автоматическое удаление файлов при достижении лимита, включите **Pinned** для исходных карт и файлов символов, которые нужно сохранить.

Также вы можете использовать [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Управляйте мобильными файлами символов через Dynatrace API.") для просмотра, закрепления или удаления файлов символов.