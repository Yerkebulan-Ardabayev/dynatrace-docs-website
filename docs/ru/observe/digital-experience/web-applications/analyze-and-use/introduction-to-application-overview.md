---
title: Introduction to application overview page
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview
scraped: 2026-03-05T21:27:35.018091
---

# Введение в страницу обзора приложения

# Введение в страницу обзора приложения

* Classic
* Explanation
* 2-min read
* Published Jul 11, 2019

Страница обзора приложения, организованная в понятные и интуитивно понятные разделы, позволяет проводить тщательный анализ как производительности приложения, так и поведения пользователей.

Переход на страницу обзора приложения

1. Перейдите в раздел **Web**.
2. Выберите приложение.

## Фильтрация

Вы можете проводить анализ на основе определённого измерения, выбранного из фильтра в верхней части страницы обзора приложения. Например, если выбрать **User type**, можно указать, хотите ли вы проводить анализ на основе данных, собранных от пользователей типа **Synthetic**, **Real users** или **Robots**.

## Теги и JavaScript-фреймворки

Непосредственно под названием приложения вы можете просмотреть назначенные [теги](/docs/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашей среде Dynatrace.") и [JavaScript-фреймворки](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Узнайте, почему необходимо активировать определённые JavaScript-фреймворки для поддержки XHR-действий, и узнайте, как настроить Real User Monitoring для XHR-действий."), которые отображаются в раскрывающейся области **Tags and JavaScript frameworks**. Здесь легко добавить новые теги — просто нажмите **Add tag**. Также есть кнопка **Framework settings**, которая ведёт к настройкам, связанным с [JavaScript-фреймворками](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Узнайте, почему необходимо активировать определённые JavaScript-фреймворки для поддержки XHR-действий, и узнайте, как настроить Real User Monitoring для XHR-действий.").

## Анализ производительности

В разделе [**Performance analysis**](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Ознакомьтесь с доступными типами анализа производительности, предоставляемыми Dynatrace.") отображается ряд метрик производительности вашего приложения. Чтобы просмотреть разделы, относящиеся к анализу производительности, разверните часть **Performance analysis** инфографики.

![Performance analysis](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

## Поведение пользователей

В разделе [**User behavior**](/docs/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis "Ознакомьтесь с параметрами анализа поведения пользователей, предоставляемыми Dynatrace.") отображается ряд метрик поведения пользователей для вашего приложения. Чтобы просмотреть разделы, связанные с поведением пользователей, разверните часть **User behavior** инфографики.

![User behavior](https://dt-cdn.net/images/user-behaviour-2360-e98d95092b.png)

## Анализ пользовательских сессий

Нажмите **Analyze user sessions** в правом верхнем углу для тщательного [анализа пользовательской сессии с разных измерений](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте о сегментации и атрибутах фильтрации пользовательских сессий.").

## Закрепление на панели управления

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.")

Нажмите **Pin to dashboard** в правом верхнем углу, чтобы добавить плитку для анализа производительности или поведения пользователей (в зависимости от того, какая часть развёрнута) на классическую панель управления по вашему выбору для быстрого просмотра анализа. Для получения подробной информации см. [Закрепление плиток на панели управления](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Узнайте, как закреплять плитки на панелях управления.").

## Настройки приложения

Нажмите **More** (**...**) в правом верхнем углу страницы, затем выберите **Edit** для доступа к настройкам приложения.

## Ключевые выводы

Для доступа к [Hyperlyzer](/docs/observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer помогает визуально запрашивать различные измерения приложения, например геолокацию, браузер, операционную систему, пропускную способность и действия пользователей."), выберите **More** (**...**) > **Show top findings**. Здесь вы можете увидеть ключевые выводы о местонахождении ваших пользователей, используемой версии браузера, их операционной системе и действиях пользователей, полученных приложением, отсортированных по длительности действия в порядке убывания (самые медленные действия считаются ключевыми выводами, поскольку это проблемные действия, требующие вашего внимания).

## Вид Smartscape

Для доступа к [виду Smartscape](/docs/analyze-explore-automate/smartscape-classic "Узнайте, как Smartscape Classic визуализирует все сущности и зависимости в вашей среде."), выберите **More** (**...**) > **Smartscape view**. Smartscape предлагает быстрый, но вместе с тем детальный обзор всех топологических зависимостей вашего приложения.
