---
title: Просмотр отчётов о сбоях для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/crash-reports-custom
---

# Просмотр отчётов о сбоях для пользовательских приложений в RUM Classic

# Просмотр отчётов о сбоях для пользовательских приложений в RUM Classic

* Практическое руководство
* 1 минута чтения
* Обновлено 20 марта 2024 г.

Анализ и устранение [сбоев](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") жизненно важны для улучшения пользовательского опыта приложения. Dynatrace фиксирует сбои и их трассировки стека, что позволяет оценить критичность сбоя и определить первопричину проблемы. С помощью рабочего процесса анализа сбоев можно увидеть влияние сбоев, определить затронутые группы пользователей и быстро добраться до первопричины. Проактивное устранение проблем помогает гарантировать, что приложения стабильно соответствуют бизнес-целям.

При работе с конфигурацией клиент-сервер первопричина некоторых сбоев кроется на стороне сервера. Dynatrace использует технологию PurePath® и OneAgent® для сопоставления действий пользователей с веб-запросами, обеспечивая полную видимость: от отдельных действий пользователя до конкретных серверных операторов базы данных, приводящих к сбоям.

Чтобы просмотреть базовую информацию о сбоях для приложения

1. Перейти в **Frontend**.
2. Выбрать приложение, которое нужно проанализировать.
3. На странице обзора приложения выбрать плитку **Crashes & Errors**.

Плитка **Crashes & Errors** показывает количество случаев сбоев, процент пользователей без сбоев и частоту сбоев за выбранный период времени. Диаграмма **Crashes by version** отображает общее количество сбоев по версиям за выбранный период времени.

![Плитка сбоев на странице обзора приложения](https://dt-cdn.net/images/crashes-tile-mobile-app-852-77531749a6.png)

Плитка сбоев на странице обзора приложения

Чтобы получить доступ к отчётам о сбоях для приложения

1. На странице обзора приложения выбрать плитку **Crashes & Errors**.
2. Под диаграммой **Crashes by version** выбрать **Analyze crashes**. Откроется страница **Crash analysis**.

![Страница анализа сбоев](https://dt-cdn.net/images/crash-analysis-mobile-app-2519-daa9f932f4.png)

Страница анализа сбоев

## Страница анализа сбоев

Страница **Crash analysis** даёт обзор всех групп сбоев, произошедших за выбранный период времени, и позволяет сосредоточиться на ряде свойств и измерений, специфичных для конкретного паттерна сбоя. Таким образом, можно анализировать сбои по версии операционной системы, версии приложения, региону пользователя, длительности сессии, типу подключения и другим измерениям.

### Latest app versions

Раздел **Latest app versions** содержит информацию о сбоях для четырёх последних версий приложения. Для каждой версии приложения можно проверить процент пользователей без сбоев, количество затронутых пользователей и количество сбоев на определённое число сессий.

### Crash statistics

В разделе **Crash statistics** можно проверить общее количество сбоев, количество групп сбоев и количество затронутых версий за выбранный период времени. В разделе **Latest app versions** выбрать **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") рядом с интересующей версией, чтобы получить эту информацию для конкретной версии.

Также можно использовать другие фильтры, такие как **Connection type**, **Country** или **Manufacturer**.

### Crash groups

Dynatrace группирует сбои по схожести трассировки стека и месту возникновения в исходном коде. Обычно это работает и между разными версиями приложения, поэтому легко узнать, присутствует ли сбой ещё и в последнем релизе.

## Страница сведений о группе сбоев

В разделе **Crash groups** на странице **Crash analysis** выбрать интересующую группу сбоев, чтобы получить доступ ко всем случаям сбоя. Отфильтровать их, чтобы изучить конкретную часть группы сбоев.

![Информация о группе сбоев](https://dt-cdn.net/images/crash-group-mobile-app-2518-9324fa74b5.png)

Информация о группе сбоев

На странице сведений о группе сбоев выбрать **Next / previous crash occurrence** ![Left and right arrows](https://dt-cdn.net/images/analysisarrowbuttons-49-c49391e1bc.png "Left and right arrows"), чтобы просмотреть все случаи сбоя. Выбрать интересующий случай сбоя, а затем переключаться между вкладками для просмотра подробной информации о выбранном случае сбоя.

Stack trace

Device information

Session information

На вкладке **Stack trace** изучить трассировку стека или скачать её, чтобы поделиться с командой.

![Трассировка стека для случая сбоя](https://dt-cdn.net/images/crash-occurence-stack-trace-tab-2520-f9c5b285f0.png)

Трассировка стека для случая сбоя

На вкладке **Device information** просмотреть подробную информацию об устройстве, на котором произошёл текущий случай сбоя. Например, можно проверить геолокацию устройства, версию ОС, язык пользователя и многое другое.

![Информация об устройстве для случая сбоя](https://dt-cdn.net/images/crash-occurence-device-info-tab-2520-8e77ca1904.png)

Информация об устройстве для случая сбоя

На вкладке **Session information** выбрать **View full session**, чтобы перейти на страницу сведений о пользовательской сессии, где можно получить больше информации о сессии со сбоем, изучить список всех действий пользователя и событий, произошедших до сбоя, или выбрать конкретный случай сбоя. Подробнее см. [Анализ пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.").

![Информация о сессии для случая сбоя](https://dt-cdn.net/images/crash-occurence-session-info-tab-2520-e40fca17fd.png)

Информация о сессии для случая сбоя

## Похожие темы

* [Анализ сбоев](/managed/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes.")
* [Пользовательские и ошибочные события в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [Анализ пользовательских сессий в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.")