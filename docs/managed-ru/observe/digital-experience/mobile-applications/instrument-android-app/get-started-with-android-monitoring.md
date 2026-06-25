---
title: Начало работы с мониторингом Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring
scraped: 2026-05-12T12:04:43.909111
---

# Начало работы с мониторингом Android

# Начало работы с мониторингом Android

* How-to guide
* 2-min read
* Updated on Sep 06, 2023

Для мониторинга Android-приложения необходимо сначала создать мобильное приложение в Dynatrace, а затем инструментировать само Android-приложение.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте мобильное приложение в Dynatrace**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#create-app-ui "Узнайте, какие шаги необходимо выполнить для инструментирования Android-приложения для мониторинга с Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Инструментируйте Android-приложение**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrument-app "Узнайте, какие шаги необходимо выполнить для инструментирования Android-приложения для мониторинга с Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройте инструментирование**](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#adjust-instrumentation "Узнайте, какие шаги необходимо выполнить для инструментирования Android-приложения для мониторинга с Dynatrace.")

## Шаг 1 Создание мобильного приложения в Dynatrace

Перед инструментированием самого Android-приложения создайте [мобильное приложение](/managed/observe/digital-experience/rum-concepts/applications#mobile "Узнайте о monitored-приложениях в Real User Monitoring и типах приложений, поддерживаемых Dynatrace.") в Dynatrace. Это приложение будет использоваться для мониторинга и анализа Android-приложения.

Чтобы создать мобильное приложение в Dynatrace:

1. В Dynatrace перейдите в **Mobile**.
2. Нажмите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница настроек приложения.

## Шаг 2 Инструментирование Android-приложения

Когда мобильное приложение создано в Dynatrace, инструментируйте само Android-приложение с помощью Dynatrace Android Gradle plugin или OneAgent SDK for Android.

[### Dynatrace Android Gradle plugin

Для автоматического инструментирования Android-проекта используйте Dynatrace Android Gradle plugin. Он встраивает процесс авто-инструментирования в сборку Android.](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle plugin может автоматически инструментировать ваш Android-проект.")[### OneAgent SDK for Android

Если из-за технических ограничений вы не можете использовать plugin, воспользуйтесь автономным ручным инструментированием с помощью OneAgent SDK.](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.")

## Шаг 3 Настройка инструментирования

После инструментирования Android-приложения вы можете настроить дополнительные параметры:

* [Настройте взаимодействие с OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте коммуникацию с OneAgent для отправки данных о пользовательском опыте в Dynatrace.")
* [Настройте процесс авто-инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")
* Создавайте пользовательские действия, фиксируйте ошибки, тегируйте конкретных пользователей и многое другое с помощью [OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK.")
* Включите и настройте [Session Replay для сбоев](/managed/observe/digital-experience/session-replay/session-replay-android "Настройте Session Replay для Android-приложений, чтобы узнать, какие действия выполняют пользователи.")
* [Настройте параметры конфиденциальности данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.")
* Ознакомьтесь с тем, [какие данные Dynatrace собирает для вашего Android-приложения](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Информация о типах данных, которые собирает OneAgent for Android. Используйте эту страницу при заполнении формы Data safety в Google Play Console."), чтобы заполнить или обновить форму Data safety в Google Play Console.

## Доступ к мастеру инструментирования мобильных приложений

Мастер инструментирования мобильных приложений в Dynatrace содержит инструкции по началу работы с инструментированием мобильных приложений, а также фрагменты кода с ключами идентификации приложения, которые нужно добавить в файл сборки проекта. Ключи идентификации приложения — `applicationId` и `beaconUrl` — необходимы для отправки данных мониторинга в Dynatrace.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с именем приложения нажмите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Instrumentation wizard**.
5. Выберите **Android**.

## Связанные темы

* [Dynatrace Android Gradle plugin](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle plugin может автоматически инструментировать ваш Android-проект.")
* [Ручное инструментирование приложения с помощью OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.")