---
title: События пользователей и ошибок
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-concepts/user-and-error-events
scraped: 2026-05-12T11:31:34.906833
---

# События пользователей и ошибок

# События пользователей и ошибок

* Explanation
* 6-min read
* Updated on Mar 05, 2026

Помимо фиксации [пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в вашем приложении."), Dynatrace также захватывает дополнительные события — события пользователей и события ошибок. Эти события происходят в рамках [сессии пользователя](/managed/observe/digital-experience/rum-concepts/user-session "Узнайте, как определяется сессия пользователя, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое."), но не генерируются напрямую через взаимодействие пользователя с элементами управления интерфейса.

## События пользователей

События пользователей включают изменения страниц, rage-клики, rage-тапы и события тегирования пользователей.

### Изменение страницы

Событие изменения страницы сигнализирует о том, что пользователь перешёл на другую страницу сайта. Например, если пользователь перешёл на страницу «payment» сайта, в сессии пользователя отобразятся следующие события:

* `Load: loading of page /payment`
* `Page change: /payment`

Подробнее см. [Страницы и группы страниц](/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Узнайте, как использовать и определять страницы и группы страниц в Dynatrace Real User Monitoring.").

### Rage-событие

Когда приложение не реагирует быстро или возникает проблема с интерфейсом, пользователи могут несколько раз подряд нажимать на экран или элемент управления в раздражении. Dynatrace определяет такое поведение как rage-событие: rage-клик для веб-приложения и rage-тап для мобильного приложения.

Три или более быстрых клика или тапа в одной и той же области считаются rage-событием. Rage-события часто отражают медленное время загрузки или проблемы с ресурсами. Обнаруженные rage-события влияют на [оценку пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying."), однако при необходимости вы можете исключить rage-клики и rage-тапы из расчёта оценки. Подробнее см. [Настройка порогов оценки пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#configure "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying.").

Вы также можете полностью отключить обнаружение rage-событий.

* Веб-приложения. В настройках приложения выберите **Behavior analytics** > **Usability analytics** и отключите **Detect rage clicks**.
* Android. См. [Обнаружение rage tap](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#rage-tap-detection "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.").
* iOS. Установите [ключ конфигурации](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации можно точно настроить автоматическое инструментирование iOS-приложений.") `DTXDetectRageTaps` в значение `false`.

В Dynatrace вы также можете [проверить сессии с rage-событиями](/managed/observe/digital-experience/session-segmentation/new-user-sessions#rage-events "Узнайте о сегментации и фильтрации сессий пользователей.") для просмотра деталей rage-клика или rage-тапа.

Также см. [Обнаружение неудовлетворительного пользовательского опыта с помощью автоматического определения rage-кликов](https://www.dynatrace.com/news/blog/discover-frustrating-user-experiences-with-automatic-rage-click-detection/).

### Тегирование пользователей

Одна из ключевых возможностей мониторинга реальных пользователей — способность уникально идентифицировать отдельных пользователей в разных браузерах, устройствах и сессиях. Это достигается путём присвоения пользовательского тега (username, псевдонима или email) сессии пользователя. Когда пользователь тегируется в вашем приложении, Dynatrace фиксирует событие тегирования пользователя.

Вы можете тегировать пользователей при входе в систему или при использовании уже авторизованной сессии при перезапуске приложения (поскольку пользовательский тег не сохраняется при перезапуске приложения).

Для веб-приложений вы можете [настроить тегирование пользователей](/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Тегируйте отдельных пользователей через JavaScript API для анализа сессий.") с помощью RUM JavaScript API или метаданных страницы вашего приложения.

Для мобильных и пользовательских приложений Dynatrace предоставляет вариант метода «тегирования пользователей».

[Android SDK](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users) [iOS SDK](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#tag-specific-users) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user) [Xamarin](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#identify-user) [.NET MAUI](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#identify-user) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#tag-specific-users)

С помощью пользовательских тегов вы можете анализировать поведение и опыт конкретного пользователя через анализ сессий. Подробнее см. [Фокус на сессиях отдельного пользователя](/managed/observe/digital-experience/session-segmentation/new-user-sessions#individual-user "Узнайте о сегментации и фильтрации сессий пользователей.") и [Данные пользователя](/managed/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Узнайте о поведении пользователей через анализ профиля пользователя (оценка пользовательского опыта) и активности сессий.").

## События ошибок

События ошибок включают ошибки и сбои.

Карты источников и файлы символов

Для помощи в определении источника обнаруженных JavaScript-ошибок и мобильных сбоев в коде Dynatrace использует карты источников и файлы символов. Для веб-приложений см. [Поддержка карт источников для анализа JavaScript-ошибок](/managed/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как карты источников упрощают анализ, воспроизведение и исправление JavaScript-ошибок."); для мобильных приложений см. [Загрузка и управление файлами символов для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте об обфускации (Android) и символикации (iOS и tvOS), а также о вариантах загрузки и управления файлами символов в Dynatrace.").

### Ошибка

Dynatrace фиксирует ошибку каждый раз, когда браузер выбрасывает JavaScript-исключение, веб-запрос завершается ошибкой, через API отправляется пользовательская ошибка, а также в других случаях.

Следующие типы ошибок захватываются в зависимости от типа приложения.

| Тип ошибки | Описание | Web | Mobile | Custom |
| --- | --- | --- | --- | --- |
| Request error | Обнаруживается браузером и OneAgent на ваших серверах | Применимо | Применимо | Применимо |
| Reported error | Сообщается вручную через специальный метод API «report an error» | Не применимо | Применимо | Применимо |
| Custom error | Сообщается вручную через RUM JavaScript API | Применимо | Не применимо | Не применимо |
| JavaScript error | JavaScript-исключения, выбрасываемые браузером | Применимо | Не применимо | Не применимо |

Для сообщения о пользовательской ошибке в веб-приложении или об ошибке (reported error) в мобильном или пользовательском приложении используйте специальный API-метод.

[Web](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror) [Android SDK](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-errors) [iOS SDK](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-error) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#report-error) [Xamarin](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-errors) [.NET MAUI](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-errors) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#reportValues) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#report-values) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-errors)

Dynatrace предлагает многочисленные варианты конфигурации, связанные с ошибками. Для веб-приложений вы можете [детально настроить обнаружение ошибок для каждого типа](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors "Настройте захват или игнорирование ошибок запросов, пользовательских и JavaScript-ошибок."), например, настроить правила ошибок запросов, добавить пользовательские правила ошибок или игнорировать JavaScript-ошибки. Для [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/web-request-errors-mobile "Перестаньте рассматривать определённые HTTP-коды ответа как ошибки в мобильных приложениях.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/web-request-errors-custom "Перестаньте рассматривать определённые HTTP-коды ответа как ошибки в пользовательских приложениях.") можно настроить игнорирование ошибок веб-запросов.

Учтите, что ошибки влияют как на [оценку пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying."), так и на [рейтинг Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения."). Однако вы можете [изменить пороги оценки пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#configure "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying."), [скорректировать параметры Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#adjust-apdex "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") и [исключить ошибки из расчётов Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#error-impact "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") в настройках приложения.

Для получения информации об ошибках в приложении вы можете использовать анализ производительности, многомерный анализ и анализ сессий пользователей. Вы можете проверить различные детали ошибок: расчётное количество ошибок, провайдер, технология и другое. Подробнее см. следующие страницы.

* [Анализ производительности | Top errors](/managed/observe/digital-experience/web-applications/analyze-and-use/performance-analysis#top-errors "Ознакомьтесь с доступными типами анализа производительности в Dynatrace.")
* [Многомерный анализ по типу ошибки](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis#by-error-type "Узнайте, как Dynatrace Real User Monitoring позволяет детально анализировать пользовательские действия по многим измерениям.")
* [Анализ отдельных пользовательских действий | Ошибки](/managed/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions#errors "Узнайте, как получить доступ к страницам деталей пользовательских действий и анализировать их.")
* [Анализ сессий пользователей | Просмотр деталей ошибок](/managed/observe/digital-experience/session-segmentation/new-user-sessions#errors "Узнайте о сегментации и фильтрации сессий пользователей.")

### Сбой

Мобильные и пользовательские приложения

При сбое вашего приложения Dynatrace автоматически фиксирует событие сбоя. Dynatrace захватывает сбои и отправляет отчёт о сбое на сервер. Отчёт о сбое включает время возникновения и полную трассировку стека исключения.

Для пользовательских приложений Dynatrace не фиксирует сбои автоматически. Их необходимо [сообщать вручную](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash "Ознакомьтесь с использованием Dynatrace OpenKit с точки зрения разработчика.").

В Dynatrace сбой — это фатальная проблема, прерывающая работу приложения. Нефатальные проблемы, такие как перехваченные исключения и [ошибки](#error), не считаются сбоями. Дисфункции ANR (Application Not Responding) не мониторируются Dynatrace.

Некоторые сбои могут не фиксироваться, например, когда у пользователя приложения возникают проблемы с сетью (нестабильное или отсутствующее интернет-соединение). Это связано с тем, что Dynatrace не отправляет отчёты о сбоях, старше 10 минут (такие отчёты уже не могут быть скоррелированы на кластере Dynatrace).

#### Отключение отчётов о сбоях

Отчёты о сбоях включены по умолчанию, но вы можете деактивировать эту функцию.

* Android. Подробнее для [Dynatrace Android Gradle plugin](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.") или [OneAgent SDK для Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#crash-reporting "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK.").
* iOS. Подробнее см. [Отчёты о сбоях](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#crashes "Ознакомьтесь со списком функций, доступных после инструментирования приложения с помощью OneAgent.").
* Кроссплатформенные фреймворки. Отредактируйте файл конфигурации (`dynatrace.config.<extension>`), добавив строку `crashReporting false` (Android) или `"DTXCrashReportingEnabled": false` (iOS). Это отключает только мониторинг нативных сбоев.

  Подробнее для следующих фреймворков:

  [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#2-configuration-with-dynatrace) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#configurationStructure) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#structure-of-the-dynatracejs-file) [Xamarin](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#config-file) [.NET MAUI](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#config-file)

#### Ручная отправка отчёта о сбое

Для некоторых технологий можно отправить отчёт о сбое вручную.

[Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#crashReporting) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#manually-report-a-crash) [Xamarin](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-crash) [.NET MAUI](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-crash) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-crash)

#### Анализ и использование данных о сбоях

Для просмотра полной последовательности пользовательских действий, предшествовавших сбою, используйте анализ сессий пользователей. Вы также можете открыть отчёт о сбое, чтобы получить всю информацию на уровне кода и быстро установить первопричину сбоя. Подробнее см. следующие страницы.

* [Анализ сессий пользователей | Анализ сбоев](/managed/observe/digital-experience/session-segmentation/new-user-sessions#crashes "Узнайте о сегментации и фильтрации сессий пользователей.")
* [Просмотр отчётов о сбоях для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Проверьте последние отчёты о сбоях для ваших мобильных приложений.")
* [Просмотр отчётов о сбоях для пользовательских приложений](/managed/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Проверьте последние отчёты о сбоях для ваших пользовательских приложений.")

С Session Replay для сбоев вы получаете дополнительный контекст для анализа сбоев. Вы можете просматривать видеозаписи, воспроизводящие пользовательские действия непосредственно перед обнаруженным сбоем. Эта функция доступна для [Android](/managed/observe/digital-experience/session-replay/session-replay-android "Настройте Session Replay для Android-приложений, чтобы узнать, какие действия выполняют пользователи.") и [iOS](/managed/observe/digital-experience/session-replay/session-replay-ios "Предварительные условия и процедура включения Session Replay для iOS-приложений.").

Обратите внимание, что сбои существенно влияют на [оценку пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying."). См. [Расчёт оценки пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score#calculate "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying."), чтобы понять, почему сессии со сбоями обычно оцениваются как **Frustrating**.