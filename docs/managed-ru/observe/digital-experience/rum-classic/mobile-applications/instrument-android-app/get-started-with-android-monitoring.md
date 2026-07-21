---
title: Начало работы с мониторингом Android в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring
---

# Начало работы с мониторингом Android в RUM Classic

# Начало работы с мониторингом Android в RUM Classic

* Практическое руководство
* Чтение: 2 мин
* Обновлено 06 сентября 2023 г.

Чтобы отслеживать своё Android-приложение, нужно сначала создать мобильное приложение в Dynatrace, а затем инструментировать сам Android-приложение.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создать мобильное приложение в Dynatrace**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#create-app-ui "Узнайте, какие шаги нужно выполнить, чтобы инструментировать своё Android-приложение для мониторинга с Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Инструментировать своё Android-приложение**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrument-app "Узнайте, какие шаги нужно выполнить, чтобы инструментировать своё Android-приложение для мониторинга с Dynatrace.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Донастроить инструментацию**](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#adjust-instrumentation "Узнайте, какие шаги нужно выполнить, чтобы инструментировать своё Android-приложение для мониторинга с Dynatrace.")

## Шаг 1. Создание мобильного приложения в Dynatrace

Прежде чем инструментировать своё Android-приложение, нужно создать [мобильное приложение](/managed/observe/digital-experience/rum-classic/rum-concepts/applications#mobile "Узнайте о отслеживаемых приложениях в Real User Monitoring Classic и о разных типах приложений, поддерживаемых Dynatrace.") в Dynatrace. Это приложение будет использоваться для мониторинга и анализа Android-приложения.

Чтобы создать мобильное приложение в Dynatrace

1. В Dynatrace перейти в раздел **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести название приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.

## Шаг 2. Инструментирование Android-приложения

После создания мобильного приложения в Dynatrace нужно инструментировать своё Android-приложение с помощью плагина Dynatrace Android Gradle или OneAgent SDK для Android.

[### Плагин Dynatrace Android Gradle

Для автоматической инструментации Android-проекта используется плагин Dynatrace Android Gradle. Он встраивает процесс автоматической инструментации в сборку Android-приложения.](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать проект вашего Android-приложения.")[### OneAgent SDK для Android

Если плагин нельзя использовать из-за технических ограничений, можно попробовать автономную ручную инструментацию с помощью OneAgent SDK.](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK для Android, чтобы вручную инструментировать своё Android-приложение.")

## Шаг 3. Донастройка инструментации

После инструментирования Android-приложения может понадобиться настроить дополнительные параметры:

* [Настроить взаимодействие с OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте взаимодействие с OneAgent для передачи данных о пользовательском опыте в Dynatrace.")
* [Настроить процесс автоматической инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities "Настройте плагин Dynatrace Android Gradle, чтобы скорректировать возможности мониторинга OneAgent.")
* Создавайте пользовательские действия, отправляйте отчёты об ошибках, помечайте конкретных пользователей и многое другое с помощью [OneAgent SDK для Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как обогатить мониторинг пользовательского опыта в Android с помощью OneAgent SDK.")
* Включите и настройте [Session Replay при сбоях](/managed/observe/digital-experience/session-replay/session-replay-android "Настройте Session Replay Classic для своих Android-приложений, чтобы узнавать, какие действия выполняют пользователи.")
* [Настроить параметры конфиденциальности данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте настройки конфиденциальности, которые предоставляет Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о конфиденциальности данных вашего региона.")
* Узнайте, какие [данные Dynatrace собирает для вашего Android-приложения](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Информация о типах данных, которые собирает OneAgent для Android. Эту страницу можно использовать при заполнении формы Data safety в Google Play Console."), чтобы заполнить или обновить форму Data safety в Google Play Console

## Доступ к мастеру инструментации мобильных приложений

Мастер инструментации мобильных приложений в Dynatrace предоставляет инструкции по началу инструментирования мобильных приложений. Мастер также содержит фрагменты кода с ключами идентификации приложения, которые нужно добавить в файл сборки проекта. Ключи идентификации приложения, `applicationId` и `beaconUrl`, необходимы для того, чтобы приложение могло отправлять данные мониторинга в Dynatrace.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. Выбрать **More** (**…**) > **Edit** в верхнем правом углу плитки с названием приложения.
4. В настройках приложения выбрать **Instrumentation wizard**.
5. Выбрать **Android**.

## Похожие темы

* [Плагин Dynatrace Android Gradle в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать проект вашего Android-приложения.")
* [Ручная инструментация приложения с помощью OneAgent SDK для Android в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK для Android, чтобы вручную инструментировать своё Android-приложение.")