---
title: Mobile Symbolication API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api
scraped: 2026-05-12T11:04:53.894186
---

# Mobile Symbolication API

# Mobile Symbolication API

* Reference
* Published Dec 05, 2018

Сервис символикации (также известный как DSS, или Deobfuscation and Symbolication Service) позволяет выполнять символикацию (iOS и tvOS) или деобфускацию (Android) отчётов о сбоях мобильных приложений или обработанных исключений. Это позволяет просматривать классы и методы в трассировке стека в виде обычного текста.

API **Mobile Symbolication** позволяет управлять файлами Android mapping и iOS/tvOS symbol extract, которые нужны для интерпретации мобильных трассировок стека при их поступлении в Dynatrace.

[### Список всех файлов символов

Получить обзор всех имеющихся у вас файлов символов.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-all "Просмотр всех файлов символов вашего окружения мониторинга через Dynatrace API.")[### Просмотр информации о хранилище

Проверить состояние хранилища файлов символов.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-storage-info "Просмотр информации о хранилище файлов символов вашего окружения мониторинга через Dynatrace API.")[### Просмотр поддерживаемых версий

Просмотр поддерживаемой версии файлов символов iOS.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-supported-versions "Просмотр поддерживаемой версии файлов символов iOS через Dynatrace API.")

[### Просмотр файлов приложения

Получить обзор файлов символов приложения.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app "Просмотр файлов символов вашего мобильного приложения через Dynatrace API.")[### Удаление файлов приложения

Удалить все файлы символов приложения.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app "Удаление всех файлов символов вашего мобильного приложения через Dynatrace API.")

### Просмотр файлов версии

[Получить обзор](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app-version "Просмотр файлов символов конкретной версии вашего мобильного приложения через Dynatrace API.") файлов символов версии приложения.

[### Загрузка файлов для версии

Загрузить файл символов для версии приложения.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Загрузка файлов символов конкретной версии вашего мобильного приложения через Dynatrace API.")[### Закрепление файлов для версии

Закрепить или открепить файлы символов версии приложения.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version-pin "Предотвращение удаления мобильных файлов символов через Dynatrace API.")[### Удаление файлов для версии

Удалить файлы символов, относящиеся к версии приложения.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app-version "Удаление файлов символов конкретной версии вашего мобильного приложения через Dynatrace API.")

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")