---
title: Пользовательские события и события ошибок в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events
---

# Пользовательские события и события ошибок в RUM Classic

# Пользовательские события и события ошибок в RUM Classic

* Пояснение
* Чтение 6 мин
* Обновлено 05 марта 2026 г.

Помимо обнаружения [пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в приложении."), Dynatrace также фиксирует дополнительные события, известные как пользовательские события и события ошибок. Эти события происходят в рамках [пользовательской сессии](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её длительность и многое другое."), но не создаются напрямую через взаимодействие пользователя с элементами интерфейса.

## Пользовательские события

К пользовательским событиям относятся смена страницы, гневные клики, гневные тапы и события пользовательских тегов.

### Смена страницы

Событие смены страницы означает, что пользователь перешёл на другую страницу сайта. Например, если пользователь перешёл на страницу «payment» сайта, в пользовательской сессии отобразятся следующие события.

* `Load: loading of page /payment`
* `Page change: /payment`

Подробнее см. в разделе [Страницы и группы страниц в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/pages-and-pagegroups "Узнайте, как использовать и определять страницы и группы страниц в Dynatrace Real User Monitoring Classic.").

### Гневное событие

Когда приложение не отвечает быстро или возникает проблема с пользовательским интерфейсом, пользователи могут в раздражении многократно кликать по экрану или элементу интерфейса. Dynatrace распознаёт такое поведение как гневное событие: гневный клик для веб-приложения и гневный тап для мобильного приложения.

Три или более быстрых клика или тапа в одной и той же области считаются гневным событием. Гневные события обычно отражают медленную загрузку или сбой при загрузке ресурсов. Обнаруженные гневные события влияют на [показатель пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score "Показатель пользовательского опыта, это метрика, используемая для классификации пользовательских сессий как Frustrating, Tolerable или Satisfying."), но при необходимости можно исключить гневные клики и гневные тапы из расчёта показателя. Подробнее см. в разделе [Настройка пороговых значений показателя пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score#configure "Показатель пользовательского опыта, это метрика, используемая для классификации пользовательских сессий как Frustrating, Tolerable или Satisfying.").

Также есть возможность полностью отключить обнаружение гневных событий.

* Веб-приложения В настройках приложения выберите **Behavior analytics** > **Usability analytics** и отключите **Detect rage clicks**.
* Android См. раздел [Обнаружение гневных тапов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Настройте плагин Dynatrace Android Gradle для регулировки возможностей мониторинга OneAgent.").
* iOS Установите [ключ конфигурации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации можно точно настроить автоматическую инструментацию iOS-приложений.") `DTXDetectRageTaps` в значение `false`.

В Dynatrace также можно [просмотреть сессии с гневными событиями](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#rage-events "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации."), чтобы увидеть подробности события гневного клика или гневного тапа.

См. также [Discover frustrating user experiences with automatic rage click detection﻿](https://www.dynatrace.com/news/blog/discover-frustrating-user-experiences-with-automatic-rage-click-detection/).

### Пользовательские теги

Одна из ключевых возможностей Real User Monitoring, это способность однозначно идентифицировать отдельных пользователей в разных браузерах, устройствах и пользовательских сессиях. Это достигается путём присвоения пользовательской сессии тега, состоящего из имени пользователя, никнейма или email. Когда пользователь помечен тегом в приложении, Dynatrace регистрирует событие пользовательского тегирования.

Пользователей можно помечать тегом при входе в систему или когда уже вошедшая в систему сессия используется или восстанавливается при повторном запуске приложения, поскольку пользовательский тег не сохраняется при перезапуске приложения.

Для веб-приложений можно [настроить пользовательское тегирование](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Пометьте отдельных пользователей тегом через JavaScript API для анализа сессий.") с помощью JavaScript API RUM или метаданных страниц приложения.

Для мобильных и пользовательских приложений Dynatrace предлагает вариант метода «пользовательского тегирования».

[Android SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users) [iOS SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#tag-specific-users) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user) [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#identify-user) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#identify-user) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#tag-specific-users) 

С помощью пользовательских тегов можно анализировать поведение и опыт конкретного пользователя через анализ пользовательской сессии. Подробнее см. в разделах [Фокус на сессиях отдельного пользователя](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#individual-user "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.") и [Данные о пользователе в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/analyze-all-sessions-of-a-single-user "Узнайте о поведении пользователя через анализ профиля пользователя (показатель пользовательского опыта) и активности сессии.").

## События ошибок

К событиям ошибок относятся ошибки и сбои.

Карты исходного кода и файлы символов

Чтобы помочь определить источник обнаруженных ошибок JavaScript и сбоев мобильных приложений в коде, Dynatrace использует карты исходного кода (source maps) и файлы символов. См. раздел [Поддержка карт исходного кода для анализа ошибок JavaScript в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как карты исходного кода упрощают анализ, воспроизведение и исправление ошибок JavaScript.") для веб-приложений и [Загрузка и управление файлами символов для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.") для мобильных приложений.

### Ошибка

Dynatrace регистрирует ошибку в любом из случаев: браузер выдаёт исключение JavaScript, веб-запрос завершается ошибкой, произвольная ошибка отправлена через API, а также по другим причинам.

В зависимости от типа приложения фиксируются следующие типы ошибок.

| Тип ошибки | Описание | Web | Mobile | Custom |
| --- | --- | --- | --- | --- |
| Ошибка запроса | Обнаруживается браузером и OneAgent на серверах | Применимо | Применимо | Применимо |
| Зарегистрированная ошибка | Отправляется вручную через специальный метод API "report an error" | Не применимо | Применимо | Применимо |
| Произвольная ошибка | Отправляется вручную через RUM JavaScript API | Применимо | Не применимо | Не применимо |
| Ошибка JavaScript | Исключения JavaScript, выдаваемые браузером | Применимо | Не применимо | Не применимо |

Чтобы отправить произвольную ошибку для веб-приложения или зарегистрированную ошибку для мобильного или произвольного приложения, используется специальный метод API.

[Web](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror) [Android SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-errors) [iOS SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-error) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#report-error) [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-errors) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#report-errors) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-errors) 

Dynatrace предлагает множество опций конфигурации, связанных с ошибками. Для веб-приложений можно [точно настроить обнаружение ошибок для каждого типа ошибок](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors."), например настроить правила ошибок запроса, добавить правила произвольных ошибок или игнорировать ошибки JavaScript. Для [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/web-request-errors-mobile "Stop treating certain response HTTP codes as errors for your mobile applications.") и [произвольных приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/web-request-errors-custom "Stop treating certain HTTP response codes as errors for your custom applications.") можно выбрать игнорирование ошибок веб-запросов.

Обрати внимание, что ошибки влияют как на [оценку пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."), так и на [рейтинг Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."). Однако можно [изменить пороговые значения оценки пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score#configure "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."), [настроить параметры Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings#adjust-apdex "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") и [исключить ошибки из расчётов Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings#error-impact "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") в настройках приложения.

Можно использовать анализ производительности, многомерный анализ и анализ пользовательских сессий, чтобы получить информацию об ошибках, возникающих в приложении. Можно проверить различные детали ошибок, такие как оценочное количество ошибок, провайдер, технология и другое. Подробности см. на следующих страницах.

* [Анализ производительности | Основные ошибки](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/performance-analysis#top-errors "Understand the available types of performance analysis that are provided by Dynatrace.")
* [Многомерный анализ по типу ошибки](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis#by-error-type "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions.")
* [Анализ отдельных пользовательских действий | Ошибки](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/analyze-individual-user-actions#errors "Understand how you can access user action detail pages and analyze user actions.")
* [Анализ пользовательских сессий | Просмотр деталей ошибок](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#errors "Learn about user session segmentation and filtering attributes.")

### Crash

Мобильные и пользовательские приложения

Когда приложение аварийно завершает работу, Dynatrace автоматически регистрирует событие сбоя. Dynatrace фиксирует сбои и отправляет отчёт о сбое на сервер. Отчёт о сбое включает время возникновения и полный стек вызовов исключения.

Для пользовательских приложений Dynatrace не сообщает о сбоях автоматически. Их нужно [регистрировать вручную](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash "Read how Dynatrace OpenKit can be used from the developer's point of view.").

В Dynatrace сбой, это критическая проблема, которая завершает работу приложения. Некритические проблемы, такие как перехваченные исключения и [ошибки](#error), сбоями не считаются. ANR (Application Not Responding) не отслеживаются Dynatrace.

Некоторые сбои могут не регистрироваться, например когда пользователь приложения испытывает проблемы с сетью, такие как нестабильное или недоступное интернет-соединение. Это происходит потому, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты уже нельзя сопоставить в кластере Dynatrace).

#### Отключение отчётов о сбоях

Отчёты о сбоях включены по умолчанию, но эту функцию можно отключить.

* Android Подробности см. в [Dynatrace Android Gradle plugin](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") или [OneAgent SDK for Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#crash-reporting "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").
* iOS См. [Crash reporting](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Explore the list of features that are available after you instrument your application with OneAgent.").
* Кроссплатформенные фреймворки Измените файл конфигурации (`dynatrace.config.<extension>`), добавив строку `crashReporting false` (Android) или `"DTXCrashReportingEnabled": false` (iOS). Обратите внимание, что это отключает только мониторинг нативных сбоев.

  Подробности для следующих фреймворков.

  [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#2-configuration-with-dynatrace) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#configurationStructure) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#structure-of-the-dynatracejs-file) [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#config-file) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#config-file)

#### Регистрация сбоя вручную

Для некоторых технологий сбой можно регистрировать вручную.

[Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#crashReporting) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#manually-report-a-crash) [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-crash) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#report-crash) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash) 

#### Анализ и использование данных о сбоях

Чтобы просмотреть полную последовательность действий пользователя, предшествовавших сбою, используйте анализ пользовательских сессий. Также можно открыть отчёт о сбое, чтобы получить всю информацию на уровне кода и быстро найти первопричину сбоя. Дополнительные сведения приведены на следующих страницах.

* [Анализ пользовательских сессий | Изучение сбоев](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#crashes "Learn about user session segmentation and filtering attributes.")
* [Просмотр отчётов о сбоях для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")
* [Просмотр отчётов о сбоях для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/crash-reports-custom "Check the latest crash reports for your custom applications.")

С помощью Session Replay по сбоям можно получить дополнительный контекст для анализа сбоев. Можно просматривать видеозаписи экрана, воспроизводящие действия пользователя непосредственно перед обнаруженным сбоем. Эта функция доступна для [Android](/managed/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay Classic for your Android apps to learn which actions your users perform.") и [iOS](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.").

Обратите внимание, что сбои резко влияют на [оценку пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."). См. [Расчёт оценки пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score#calculate "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."), чтобы узнать, почему сессии со сбоями обычно получают оценку **Frustrating**.