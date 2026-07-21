---
title: Просмотр отчётов о сбоях для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/crash-reports-mobile
---

# Просмотр отчётов о сбоях для мобильных приложений в RUM Classic

# Просмотр отчётов о сбоях для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение за 2 мин
* Обновлено 20 марта 2024 г.

Анализ и устранение [сбоев](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") жизненно важны для улучшения пользовательского опыта приложения. Dynatrace фиксирует сбои и их трассировки стека, что позволяет оценить критичность сбоя и определить первопричину проблемы. С помощью workflow анализа сбоев можно увидеть влияние сбоев, определить затронутые группы пользователей и быстро дойти до первопричины. Проактивное устранение проблем помогает обеспечить, чтобы приложения стабильно соответствовали бизнес-целям.

При работе с клиент-серверной архитектурой первопричина некоторых сбоев кроется на стороне сервера. Dynatrace использует технологию PurePath® и OneAgent® для сопоставления действий пользователя с веб-запросами, обеспечивая полную видимость от отдельных действий пользователя до конкретных серверных операторов базы данных, способствующих сбоям.

Чтобы просмотреть базовую информацию о сбоях для приложения

1. Перейти в **Frontend**.
2. Выбрать приложение для анализа.
3. На странице обзора приложения выбрать плитку **Crashes & Errors**.

Плитка **Crashes & Errors** показывает количество случаев сбоев, процент пользователей без сбоев и частоту сбоев за выбранный период времени. Диаграмма **Crashes by version** отображает общее количество сбоев по версиям за выбранный период времени.

![Плитка Crashes на странице обзора приложения](https://dt-cdn.net/images/crashes-tile-mobile-app-852-77531749a6.png)

Плитка Crashes на странице обзора приложения

Чтобы получить доступ к отчётам о сбоях для приложения

1. На странице обзора приложения выбрать плитку **Crashes & Errors**.
2. Под диаграммой **Crashes by version** выбрать **Analyze crashes**. Откроется страница **Crash analysis**.

![Страница Crash analysis](https://dt-cdn.net/images/crash-analysis-mobile-app-2519-daa9f932f4.png)

Страница Crash analysis

## Страница Crash analysis

Страница **Crash analysis** даёт обзор всех групп сбоев, произошедших за выбранный период времени, и позволяет сосредоточиться на ряде свойств и измерений, характерных для конкретного паттерна сбоя. Таким образом, можно анализировать сбои по версии операционной системы, версии приложения, региону пользователя, длительности сессии, типу подключения и другим измерениям.

### Последние версии приложения

Раздел **Latest app versions** предоставляет информацию о сбоях для четырёх последних версий приложения. Для каждой версии приложения можно проверить процент пользователей без сбоев, число затронутых пользователей и число сбоев на определённое количество сессий.

### Статистика сбоев

В разделе **Crash statistics** можно проверить общее число сбоев, число групп сбоев и число затронутых версий за выбранный период времени. В разделе **Latest app versions** выбрать **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") рядом с нужной версией, чтобы получить эту информацию для конкретной версии.

Можно также использовать другие фильтры, такие как **Connection type**, **Country** или **Manufacturer**.

### Группы сбоев

Dynatrace группирует сбои по схожести трассировки стека и месту возникновения в исходном коде. Обычно это работает и между разными версиями приложения, поэтому легко узнать, присутствует ли сбой всё ещё в последнем релизе.

## Страница сведений о группе сбоев

В разделе **Crash groups** на странице **Crash analysis** выбрать интересующую группу сбоев, чтобы получить доступ ко всем экземплярам сбоев. Отфильтровать их для изучения конкретной части группы сбоев.

![Информация о группе сбоев](https://dt-cdn.net/images/crash-group-mobile-app-2518-9324fa74b5.png)

Информация о группе сбоев

На странице сведений о группе сбоев выбрать **Next / previous crash occurrence** ![Left and right arrows](https://dt-cdn.net/images/analysisarrowbuttons-49-c49391e1bc.png "Left and right arrows"), чтобы просмотреть все случаи сбоя. Выбрать интересующий случай сбоя, а затем переключаться между вкладками для просмотра подробной информации о выбранном случае сбоя.

Stack trace

Device information

Session information

На вкладке **Stack trace** изучить трассировку стека, проверить, доступен ли [файл сопоставления](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace."), или скачать трассировку стека, чтобы поделиться ею с командой.

![Трассировка стека для случая сбоя](https://dt-cdn.net/images/crash-occurence-stack-trace-tab-2520-f9c5b285f0.png)

Трассировка стека для случая сбоя

На вкладке **Device information** просмотреть подробную информацию об устройстве, на котором произошёл текущий случай сбоя. Например, можно проверить геолокацию устройства, версию ОС, язык пользователя и многое другое.

![Информация об устройстве для случая сбоя](https://dt-cdn.net/images/crash-occurence-device-info-tab-2520-8e77ca1904.png)

Информация об устройстве для случая сбоя

На вкладке **Session information** просмотреть запись сессии или перейти к сведениям о сессии.

* Если пользовательская сессия была записана с помощью Session Replay для [Android](/managed/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay Classic for your Android apps to learn which actions your users perform.") или [iOS](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps."), выбрать **Play** ![Replay](https://dt-cdn.net/images/replay-button-optimized-41ad05863e.svg "Replay"), чтобы посмотреть, что происходило на экране пользователя непосредственно перед сбоем приложения. Последнее событие сессии, это сбой, обозначенный красной точкой на временной шкале. Использовать элементы управления Session Replay для детального анализа сбоя.
* Выбрать **View full session**, чтобы перейти на страницу сведений о пользовательской сессии, где можно получить больше информации о сессии со сбоем, изучить список всех действий пользователя и событий, произошедших перед сбоем, или выбрать конкретный экземпляр сбоя. Подробнее см. [Анализ пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.").

![Информация о сессии для случая сбоя](https://dt-cdn.net/images/crash-occurence-session-info-tab-2520-e40fca17fd.png)

Информация о сессии для случая сбоя

## Символизация

Символизация или деобфускация преобразует шестнадцатеричные коды и трассировки стека, зафиксированные Dynatrace, в удобочитаемый формат. Загружая файлы символов, можно видеть в трассировке стека понятные имена методов вместо шестнадцатеричных кодов или неразборчивых имён, предоставленных обфускатором.

Подробные инструкции см. в разделе [Загрузка и управление файлами символов для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.").

## Смежные темы

* [Анализ сбоев](/managed/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes.")
* [События пользователей и ошибок в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [Анализ пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.")