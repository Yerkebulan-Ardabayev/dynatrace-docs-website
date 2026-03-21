---
title: События пользователя и ошибки
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-and-error-events
scraped: 2026-03-06T21:26:34.294869
---

# Пользовательские события и события ошибок


* Пояснение

Помимо обнаружения [действий пользователя](user-actions.md "Узнайте, что такое действия пользователя и как они помогают понять, что пользователи делают с вашим приложением."), Dynatrace также фиксирует дополнительные события, известные как пользовательские события и события ошибок. Эти события происходят в рамках [пользовательской сессии](user-session.md "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её длительность и другие подробности."), но они не генерируются непосредственно взаимодействием пользователя с элементами управления интерфейса.

## Пользовательские события

Пользовательские события включают смену страницы, клики от раздражения, нажатия от раздражения и события тегирования пользователей.

### Смена страницы

Событие смены страницы означает, что пользователь перешёл на другую страницу веб-сайта. Например, если вы перешли на страницу «оплата» сайта, в пользовательской сессии отобразятся следующие события:

* `Load: loading of page /payment`
* `Page change: /payment`

Подробности см. в разделах [RUM web: события смены страницы](../../../whats-new/saas/sprint-218.md#page-change "Примечания к выпуску Dynatrace SaaS, версия 1.218") и [Страницы и группы страниц](../web-applications/initial-setup/pages-and-pagegroups.md "Узнайте, как использовать и определять страницы и группы страниц в Dynatrace Real User Monitoring.").

### Событие раздражения

Когда ваше приложение не реагирует быстро или возникает проблема с пользовательским интерфейсом, пользователи могут многократно нажимать на экран или элемент управления от раздражения. Dynatrace обнаруживает такое поведение как событие раздражения: клик от раздражения для веб-приложения и нажатие от раздражения для мобильного приложения.

Три или более быстрых клика или нажатия в одной и той же области считаются событием раздражения. События раздражения обычно отражают медленную загрузку или проблемы с ресурсами. Обнаруженные события раздражения влияют на [оценку пользовательского опыта](scores-and-ratings/user-experience-score.md "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий как Раздражающих, Допустимых или Удовлетворительных."), но при необходимости вы можете исключить клики и нажатия от раздражения из расчёта оценки. Подробнее см. в разделе [Настройка пороговых значений оценки пользовательского опыта](scores-and-ratings/user-experience-score.md#configure "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий.").

Вы также можете полностью отключить обнаружение событий раздражения.

* Веб-приложения: в настройках приложения выберите **Behavior analytics** > **Usability analytics** и отключите **Detect rage clicks**.
* Android: см. [Обнаружение нажатий от раздражения](../mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md#rage-tap-detection "Настройка плагина Dynatrace Android Gradle.").
* iOS: установите [ключ конфигурации](../mobile-applications/instrument-ios-app/customization/ios-configuration-keys.md#user-actions "С помощью ключей конфигурации вы можете точно настроить автоматическую инструментацию приложений iOS.") `DTXDetectRageTaps` в значение `false`.

В Dynatrace вы также можете [проверить сессии с событиями раздражения](../session-segmentation/new-user-sessions.md#rage-events "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации."), чтобы просмотреть детали клика или нажатия от раздражения.

См. также [Обнаружение раздражающего пользовательского опыта с помощью автоматического определения кликов от раздражения](https://www.dynatrace.com/news/blog/discover-frustrating-user-experiences-with-automatic-rage-click-detection/).

### Тегирование пользователей

Одна из ключевых возможностей Real User Monitoring — это способность уникально идентифицировать отдельных пользователей в различных браузерах, на различных устройствах и в различных пользовательских сессиях. Это достигается путём назначения тега пользователя, который состоит из имени пользователя, псевдонима или адреса электронной почты, к пользовательской сессии. Когда пользователь тегирован в вашем приложении, Dynatrace регистрирует событие тегирования пользователя.

Вы можете тегировать пользователей при входе в систему или при использовании или восстановлении уже авторизованной сессии при перезапуске приложения, так как тег пользователя не сохраняется при перезапуске приложения.

Для веб-приложений вы можете [настроить тегирование пользователей](../web-applications/additional-configuration/identify-individual-users-for-session-analysis.md "Тегирование отдельных пользователей через JavaScript API для анализа сессий."), используя RUM JavaScript API или метаданные страниц приложения.

Для мобильных и пользовательских приложений Dynatrace предлагает вариант метода «тегирования пользователей».

[Android SDK](../mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md#tag-specific-users) [iOS SDK](../mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios.md#tag-specific-users) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#identify-user) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#identify-user) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user) [OpenKit](../../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods.md#tag-specific-users)

С помощью тегов пользователей вы можете анализировать поведение и опыт конкретного пользователя через анализ пользовательских сессий. Подробности см. в разделах [Фокусировка на сессиях отдельного пользователя](../session-segmentation/new-user-sessions.md#individual-user "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.") и [Профиль пользователя](../session-segmentation/analyze-all-sessions-of-a-single-user.md "Узнайте о поведении пользователя путём анализа профиля (оценки пользовательского опыта) и активности в сессиях.").

## События ошибок

События ошибок включают ошибки и сбои.

Карты исходного кода и файлы символов

Чтобы помочь вам определить источник обнаруженных ошибок JavaScript и сбоев мобильных приложений в вашем коде, Dynatrace использует карты исходного кода и файлы символов. См. [Поддержка карт исходного кода для анализа ошибок JavaScript](../web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis.md "Узнайте, как карты исходного кода упрощают анализ, воспроизведение и исправление ошибок JavaScript.") для веб-приложений и [Загрузка и управление файлами символов для мобильных приложений](../mobile-applications/analyze-and-use/upload-and-manage-symbol-files.md "Узнайте о деобфускации (Android) и символизации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.").

### Ошибка

Dynatrace регистрирует ошибку каждый раз, когда браузер генерирует исключение JavaScript, веб-запрос завершается ошибкой, отправляется пользовательская ошибка через API и по другим причинам.

Следующие типы ошибок фиксируются в зависимости от типа вашего приложения.

| Тип ошибки | Описание | Веб | Мобильное | Пользовательское |
| --- | --- | --- | --- | --- |
| Ошибка запроса | Обнаруживается браузером и OneAgent на серверах | Применимо | Применимо | Применимо |
| Зарегистрированная ошибка | Передаётся вручную через выделенный API-метод «сообщить об ошибке» | Неприменимо | Применимо | Применимо |
| Пользовательская ошибка | Передаётся вручную через RUM JavaScript API | Применимо | Неприменимо | Неприменимо |
| Ошибка JavaScript | Исключения JavaScript, генерируемые браузером | Применимо | Неприменимо | Неприменимо |

Чтобы сообщить о пользовательской ошибке для веб-приложения или о зарегистрированной ошибке для мобильного или пользовательского приложения, используйте выделенный API-метод.

[Web](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror) [Android SDK](../mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md#report-errors) [iOS SDK](../mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios.md#report-error) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#report-error) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#report-errors) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#report-errors) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [OpenKit](../../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods.md#report-errors)

Dynatrace предлагает множество параметров конфигурации, связанных с ошибками. Для веб-приложений вы можете [точно настроить обнаружение ошибок для каждого типа](../web-applications/additional-configuration/configure-errors.md "Настройте приложение для фиксации или игнорирования ошибок запросов, пользовательских ошибок и ошибок JavaScript."), например, настроить правила ошибок запросов, добавить правила пользовательских ошибок или игнорировать ошибки JavaScript. Для [мобильных](../mobile-applications/additional-configuration/web-request-errors-mobile.md "Прекратите считать определённые HTTP-коды ответов ошибками для мобильных приложений.") и [пользовательских приложений](../custom-applications/additional-configuration/web-request-errors-custom.md "Прекратите считать определённые HTTP-коды ответов ошибками для пользовательских приложений.") вы можете выбрать игнорирование ошибок веб-запросов.

Обратите внимание, что ошибки влияют как на [оценку пользовательского опыта](scores-and-ratings/user-experience-score.md "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."), так и на [рейтинг Apdex](scores-and-ratings/apdex-ratings.md "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения."). Однако вы можете [изменить пороговые значения оценки пользовательского опыта](scores-and-ratings/user-experience-score.md#configure "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."), [скорректировать настройки Apdex](scores-and-ratings/apdex-ratings.md#adjust-apdex "Узнайте, как Dynatrace использует Apdex.") и [исключить ошибки из расчётов Apdex](scores-and-ratings/apdex-ratings.md#error-impact "Узнайте, как Dynatrace использует Apdex.") в настройках приложения.

Вы можете использовать анализ производительности, многомерный анализ и анализ пользовательских сессий для получения информации об ошибках, возникающих в вашем приложении. Вы можете проверить различные детали ошибок, такие как примерное количество ошибок, провайдер, технология и многое другое. Подробности см. на следующих страницах.

* [Анализ производительности | Основные ошибки](../web-applications/analyze-and-use/performance-analysis.md#top-errors "Ознакомьтесь с доступными типами анализа производительности в Dynatrace.")
* [Многомерный анализ по типам ошибок](../web-applications/analyze-and-use/multi-dimensional-analysis.md#by-error-type "Узнайте, как Dynatrace Real User Monitoring позволяет глубоко анализировать действия пользователей по множеству измерений.")
* [Анализ отдельных действий пользователя | Ошибки](../web-applications/analyze-and-use/analyze-individual-user-actions.md#errors "Узнайте, как получить доступ к страницам деталей действий пользователя и анализировать действия.")
* [Анализ пользовательских сессий | Просмотр деталей ошибок](../session-segmentation/new-user-sessions.md#errors "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.")

### Сбой

Мобильные и пользовательские приложения

Когда ваше приложение аварийно завершается, Dynatrace автоматически регистрирует событие сбоя. Dynatrace фиксирует сбои и отправляет отчёт о сбое на сервер. Отчёт о сбое включает время возникновения и полный стек вызовов исключения.

Для пользовательских приложений Dynatrace не регистрирует сбои автоматически. Вам необходимо [сообщить о них вручную](../../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods.md#report-crash "Узнайте, как Dynatrace OpenKit можно использовать с точки зрения разработчика.").

В Dynatrace сбой — это фатальная проблема, приводящая к завершению приложения. Нефатальные проблемы, такие как перехваченные исключения и [ошибки](#error), не считаются сбоями. ANR (Application Not Responding — приложение не отвечает) не отслеживаются Dynatrace.

Некоторые сбои могут не быть зафиксированы — например, когда у пользователя приложения возникают проблемы с сетью, такие как нестабильное или недоступное интернет-соединение. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (поскольку такие отчёты уже не могут быть сопоставлены в кластере Dynatrace).

#### Отключение отчётов о сбоях

Отчёты о сбоях включены по умолчанию, но вы можете деактивировать эту функцию.

* Android: см. подробности для [плагина Dynatrace Android Gradle](../mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md#crash-reporting "Настройка плагина Dynatrace Android Gradle.") или [OneAgent SDK для Android](../mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md#crash-reporting "Узнайте, как улучшить мониторинг мобильного пользовательского опыта в Android с помощью OneAgent SDK.").
* iOS: см. [Отчёты о сбоях](../mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features.md#crashes "Ознакомьтесь со списком функций, доступных после инструментации приложения с помощью OneAgent.").
* Кросс-платформенные фреймворки: измените файл конфигурации (`dynatrace.config.<extension>`), добавив строку `crashReporting false` (Android) или `"DTXCrashReportingEnabled": false` (iOS). Обратите внимание, что это отключает мониторинг только нативных сбоев.

  Подробности см. для следующих фреймворков:

  [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#2-configuration-with-dynatrace) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#configurationStructure) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#structure-of-the-dynatracejs-file) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#config-file) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#config-file)

#### Ручная отправка отчёта о сбое

Для некоторых технологий вы можете отправить отчёт о сбое вручную.

[Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#crashReporting) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#manually-report-a-crash) [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#report-crash) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#report-crash) [OpenKit](../../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods.md#report-crash)

#### Анализ и использование данных о сбоях

Чтобы просмотреть полную последовательность действий пользователя, предшествовавших сбою, используйте анализ пользовательских сессий. Вы также можете открыть отчёт о сбое, чтобы получить всю информацию на уровне кода и быстро определить причину сбоя. Подробности см. на следующих страницах.

* [Анализ пользовательских сессий | Исследование сбоев](../session-segmentation/new-user-sessions.md#crashes "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.")
* [Просмотр отчётов о сбоях для мобильных приложений](../mobile-applications/analyze-and-use/crash-reports-mobile.md "Проверьте последние отчёты о сбоях для мобильных приложений.")
* [Просмотр отчётов о сбоях для пользовательских приложений](../custom-applications/analyze-and-use/crash-reports-custom.md "Проверьте последние отчёты о сбоях для пользовательских приложений.")

С помощью Session Replay для сбоев вы получаете дополнительный контекст для анализа сбоев. Вы можете просматривать видеоподобные записи экрана, воспроизводящие действия пользователя непосредственно перед обнаруженным сбоем. Эта функция доступна для [Android](../session-replay/session-replay-android.md "Настройте Session Replay для приложений Android.") и [iOS](../session-replay/session-replay-ios.md "Предварительные требования и процедура включения Session Replay для приложений iOS.").

Обратите внимание, что сбои значительно влияют на [оценку пользовательского опыта](scores-and-ratings/user-experience-score.md "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."). См. [Расчёт оценки пользовательского опыта](scores-and-ratings/user-experience-score.md#calculate "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."), чтобы узнать, почему сессии со сбоями обычно оцениваются как **Раздражающие**.
