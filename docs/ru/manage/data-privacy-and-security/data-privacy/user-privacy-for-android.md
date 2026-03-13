---
title: Data safety guidance for Android
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android
scraped: 2026-03-02T21:23:37.193494
---

# Руководство по безопасности данных для Android

# Руководство по безопасности данных для Android

* Latest Dynatrace
* 5-min read
* Updated on Sep 15, 2025

Начиная с 20 июля 2022 года Google обязывает вас предоставлять пользователям информацию о том, как ваше мобильное приложение собирает, защищает и передаёт их данные. Это также распространяется на данные, собираемые сторонними партнёрами, такими как Dynatrace.

Эта страница поможет вам заполнить [форму безопасности данныхï»¿](https://support.google.com/googleplay/android-developer/answer/10787469#complete_form_steps) в Google Play Console. Вопросы и типы данных соответствуют форме безопасности данных, однако обратите внимание, что ответы отражают стандартное состояние по умолчанию.

OneAgent может собирать дополнительные данные через вашу [ручную инструментацию](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Learn what OneAgent SDK for Android is."). Если вы инструментируете приложение для сбора дополнительных данных, убедитесь, что это отражено в разделе **Data safety** в Google Play Console.

Чтобы заполнить форму безопасности данных

1. Войдите в Google Play Console и выберите нужное мобильное приложение.
2. В меню слева перейдите в раздел **Policy** > **App content**.
3. В разделе **Data safety** выберите **Manage**.
4. Заполните форму безопасности данных, используя информацию, представленную на этой странице.

## Сбор данных и безопасность

Используйте таблицу ниже для ответа на вопросы этого раздела.

## Типы данных

Выберите все типы данных, которые ваше мобильное приложение собирает или передаёт.

Таблица ниже содержит все данные, которые OneAgent собирает по умолчанию.

## Использование и обработка данных

Вам также необходимо предоставить информацию об использовании и обработке данных для каждого типа данных, выбранного в разделе **Data types**. Выберите **Start** для продолжения.

Используйте таблицу ниже для всех типов данных, захватываемых OneAgent.

## Связанные темы

* [Preparing for Google Play's new safety sectionï»¿](https://android-developers.googleblog.com/2021/07/new-google-play-safety-section.html)
* [Provide information for Google Play's Data safety sectionï»¿](https://support.google.com/googleplay/android-developer/answer/10787469)
* [Configure data privacy settings for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")
