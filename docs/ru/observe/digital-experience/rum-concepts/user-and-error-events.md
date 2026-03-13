---
title: User and error events
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-and-error-events
scraped: 2026-03-06T21:26:34.294869
---

# Пользовательские события и события ошибок

# Пользовательские события и события ошибок

* Classic
* Пояснение
* Чтение: 6 мин
* Обновлено 5 марта 2026 г.

Помимо обнаружения [действий пользователя](/docs/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое действия пользователя и как они помогают понять, что пользователи делают с вашим приложением."), Dynatrace также фиксирует дополнительные события, известные как пользовательские события и события ошибок. Эти события происходят в рамках [пользовательской сессии](/docs/observe/digital-experience/rum-concepts/user-session "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её длительность и другие подробности."), но они не генерируются непосредственно взаимодействием пользователя с элементами управления интерфейса.

## Пользовательские события

Пользовательские события включают смену страницы, клики от раздражения, нажатия от раздражения и события тегирования пользователей.

### Смена страницы

Событие смены страницы означает, что пользователь перешёл на другую страницу веб-сайта. Например, если вы перешли на страницу «оплата» сайта, в пользовательской сессии отобразятся следующие события:

* `Load: loading of page /payment`
* `Page change: /payment`

Подробности см. в разделах [RUM web: события смены страницы](/docs/whats-new/saas/sprint-218#page-change "Примечания к выпуску Dynatrace SaaS, версия 1.218") и [Страницы и группы страниц](/docs/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Узнайте, как использовать и определять страницы и группы страниц в Dynatrace Real User Monitoring.").

### Событие раздражения

Когда ваше приложение не реагирует быстро или возникает проблема с пользовательским интерфейсом, пользователи могут многократно нажимать на экран или элемент управления от раздражения. Dynatrace обнаруживает такое поведение как событие раздражения: клик от раздражения для веб-приложения и нажатие от раздражения для мобильного приложения.

Три или более быстрых клика или нажатия в одной и той же области считаются событием раздражения. События раздражения обычно отражают медленную загрузку или проблемы с ресурсами. Обнаруженные события раздражения влияют на [оценку пользовательского опыта](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий как Раздражающих, Допустимых или Удовлетворительных."), но при необходимости вы можете исключить клики и нажатия от раздражения из расчёта оценки. Подробнее см. в разделе [Настройка пороговых значений оценки пользовательского опыта](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#configure "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий.").

Вы также можете полностью отключить обнаружение событий раздражения.

* Веб-приложения: в настройках приложения выберите **Behavior analytics** > **Usability analytics** и отключите **Detect rage clicks**.
* Android: см. [Обнаружение нажатий от раздражения](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Настройка плагина Dynatrace Android Gradle.").
* iOS: установите [ключ конфигурации](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации вы можете точно настроить автоматическую инструментацию приложений iOS.") `DTXDetectRageTaps` в значение `false`.

В Dynatrace вы также можете [проверить сессии с событиями раздражения](/docs/observe/digital-experience/session-segmentation/new-user-sessions#rage-events "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации."), чтобы просмотреть детали клика или нажатия от раздражения.

См. также [Обнаружение раздражающего пользовательского опыта с помощью автоматического определения кликов от раздражения](https://www.dynatrace.com/news/blog/discover-frustrating-user-experiences-with-automatic-rage-click-detection/).

### Тегирование пользователей

Одна из ключевых возможностей Real User Monitoring — это способность уникально идентифицировать отдельных пользователей в различных браузерах, на различных устройствах и в различных пользовательских сессиях. Это достигается путём назначения тега пользователя, который состоит из имени пользователя, псевдонима или адреса электронной почты, к пользовательской сессии. Когда пользователь тегирован в вашем приложении, Dynatrace регистрирует событие тегирования пользователя.

Вы можете тегировать пользователей при входе в систему или при использовании или восстановлении уже авторизованной сессии при перезапуске приложения, так как тег пользователя не сохраняется при перезапуске приложения.

Для веб-приложений вы можете [настроить тегирование пользователей](/docs/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Тегирование отдельных пользователей через JavaScript API для анализа сессий."), используя RUM JavaScript API или метаданные страниц приложения.

Для мобильных и пользовательских приложений Dynatrace предлагает вариант метода «тегирования пользователей».

[Android SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users) [iOS SDK](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#tag-specific-users) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#identify-user) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#identify-user) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#tag-specific-users)

С помощью тегов пользователей вы можете анализировать поведение и опыт конкретного пользователя через анализ пользовательских сессий. Подробности см. в разделах [Фокусировка на сессиях отдельного пользователя](/docs/observe/digital-experience/session-segmentation/new-user-sessions#individual-user "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.") и [Профиль пользователя](/docs/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Узнайте о поведении пользователя путём анализа профиля (оценки пользовательского опыта) и активности в сессиях.").

## События ошибок

События ошибок включают ошибки и сбои.

Карты исходного кода и файлы символов

Чтобы помочь вам определить источник обнаруженных ошибок JavaScript и сбоев мобильных приложений в вашем коде, Dynatrace использует карты исходного кода и файлы символов. См. [Поддержка карт исходного кода для анализа ошибок JavaScript](/docs/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как карты исходного кода упрощают анализ, воспроизведение и исправление ошибок JavaScript.") для веб-приложений и [Загрузка и управление файлами символов для мобильных приложений](/docs/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символизации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.").

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

[Web](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror) [Android SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-errors) [iOS SDK](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-error) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#report-error) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-errors) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-errors) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-errors)

Dynatrace предлагает множество параметров конфигурации, связанных с ошибками. Для веб-приложений вы можете [точно настроить обнаружение ошибок для каждого типа](/docs/observe/digital-experience/web-applications/additional-configuration/configure-errors "Настройте приложение для фиксации или игнорирования ошибок запросов, пользовательских ошибок и ошибок JavaScript."), например, настроить правила ошибок запросов, добавить правила пользовательских ошибок или игнорировать ошибки JavaScript. Для [мобильных](/docs/observe/digital-experience/mobile-applications/additional-configuration/web-request-errors-mobile "Прекратите считать определённые HTTP-коды ответов ошибками для мобильных приложений.") и [пользовательских приложений](/docs/observe/digital-experience/custom-applications/additional-configuration/web-request-errors-custom "Прекратите считать определённые HTTP-коды ответов ошибками для пользовательских приложений.") вы можете выбрать игнорирование ошибок веб-запросов.

Обратите внимание, что ошибки влияют как на [оценку пользовательского опыта](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."), так и на [рейтинг Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения."). Однако вы можете [изменить пороговые значения оценки пользовательского опыта](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#configure "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."), [скорректировать настройки Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#adjust-apdex "Узнайте, как Dynatrace использует Apdex.") и [исключить ошибки из расчётов Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#error-impact "Узнайте, как Dynatrace использует Apdex.") в настройках приложения.

Вы можете использовать анализ производительности, многомерный анализ и анализ пользовательских сессий для получения информации об ошибках, возникающих в вашем приложении. Вы можете проверить различные детали ошибок, такие как примерное количество ошибок, провайдер, технология и многое другое. Подробности см. на следующих страницах.

* [Анализ производительности | Основные ошибки](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis#top-errors "Ознакомьтесь с доступными типами анализа производительности в Dynatrace.")
* [Многомерный анализ по типам ошибок](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis#by-error-type "Узнайте, как Dynatrace Real User Monitoring позволяет глубоко анализировать действия пользователей по множеству измерений.")
* [Анализ отдельных действий пользователя | Ошибки](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions#errors "Узнайте, как получить доступ к страницам деталей действий пользователя и анализировать действия.")
* [Анализ пользовательских сессий | Просмотр деталей ошибок](/docs/observe/digital-experience/session-segmentation/new-user-sessions#errors "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.")

### Сбой

Мобильные и пользовательские приложения

Когда ваше приложение аварийно завершается, Dynatrace автоматически регистрирует событие сбоя. Dynatrace фиксирует сбои и отправляет отчёт о сбое на сервер. Отчёт о сбое включает время возникновения и полный стек вызовов исключения.

Для пользовательских приложений Dynatrace не регистрирует сбои автоматически. Вам необходимо [сообщить о них вручную](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash "Узнайте, как Dynatrace OpenKit можно использовать с точки зрения разработчика.").

В Dynatrace сбой — это фатальная проблема, приводящая к завершению приложения. Нефатальные проблемы, такие как перехваченные исключения и [ошибки](#error), не считаются сбоями. ANR (Application Not Responding — приложение не отвечает) не отслеживаются Dynatrace.

Некоторые сбои могут не быть зафиксированы — например, когда у пользователя приложения возникают проблемы с сетью, такие как нестабильное или недоступное интернет-соединение. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (поскольку такие отчёты уже не могут быть сопоставлены в кластере Dynatrace).

#### Отключение отчётов о сбоях

Отчёты о сбоях включены по умолчанию, но вы можете деактивировать эту функцию.

* Android: см. подробности для [плагина Dynatrace Android Gradle](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Настройка плагина Dynatrace Android Gradle.") или [OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#crash-reporting "Узнайте, как улучшить мониторинг мобильного пользовательского опыта в Android с помощью OneAgent SDK.").
* iOS: см. [Отчёты о сбоях](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Ознакомьтесь со списком функций, доступных после инструментации приложения с помощью OneAgent.").
* Кросс-платформенные фреймворки: измените файл конфигурации (`dynatrace.config.<extension>`), добавив строку `crashReporting false` (Android) или `"DTXCrashReportingEnabled": false` (iOS). Обратите внимание, что это отключает мониторинг только нативных сбоев.

  Подробности см. для следующих фреймворков:

  [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#2-configuration-with-dynatrace) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#configurationStructure) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#structure-of-the-dynatracejs-file) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#config-file) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#config-file)

#### Ручная отправка отчёта о сбое

Для некоторых технологий вы можете отправить отчёт о сбое вручную.

[Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#crashReporting) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#manually-report-a-crash) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-crash) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-crash) [OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash)

#### Анализ и использование данных о сбоях

Чтобы просмотреть полную последовательность действий пользователя, предшествовавших сбою, используйте анализ пользовательских сессий. Вы также можете открыть отчёт о сбое, чтобы получить всю информацию на уровне кода и быстро определить причину сбоя. Подробности см. на следующих страницах.

* [Анализ пользовательских сессий | Исследование сбоев](/docs/observe/digital-experience/session-segmentation/new-user-sessions#crashes "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.")
* [Просмотр отчётов о сбоях для мобильных приложений](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Проверьте последние отчёты о сбоях для мобильных приложений.")
* [Просмотр отчётов о сбоях для пользовательских приложений](/docs/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Проверьте последние отчёты о сбоях для пользовательских приложений.")

С помощью Session Replay для сбоев вы получаете дополнительный контекст для анализа сбоев. Вы можете просматривать видеоподобные записи экрана, воспроизводящие действия пользователя непосредственно перед обнаруженным сбоем. Эта функция доступна для [Android](/docs/observe/digital-experience/session-replay/session-replay-android "Настройте Session Replay для приложений Android.") и [iOS](/docs/observe/digital-experience/session-replay/session-replay-ios "Предварительные требования и процедура включения Session Replay для приложений iOS.").

Обратите внимание, что сбои значительно влияют на [оценку пользовательского опыта](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."). См. [Расчёт оценки пользовательского опыта](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#calculate "Оценка пользовательского опыта — это метрика для категоризации пользовательских сессий."), чтобы узнать, почему сессии со сбоями обычно оцениваются как **Раздражающие**.
