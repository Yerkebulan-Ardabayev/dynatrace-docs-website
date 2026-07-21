---
title: Введение в страницу обзора приложения в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/introduction-to-application-overview
---

# Введение в страницу обзора приложения в RUM Classic

# Введение в страницу обзора приложения в RUM Classic

* Пояснение
* 2 минуты на чтение
* Опубликовано 11 июля 2019 г.

Страница обзора приложения организована в логичные и интуитивно понятные разделы и позволяет провести полноценный анализ как производительности приложения, так и поведения пользователей.

Доступ к странице обзора приложения

1. Перейти в **Web**.
2. Выбрать приложение.

## Фильтрация

Анализ можно проводить на основе конкретного измерения, выбранного в фильтре в верхней части страницы обзора приложения. Например, при выборе **User type** можно указать, на основе каких данных проводить анализ: **Synthetic**, **Real users** или **Robots**.

## Теги и JavaScript-фреймворки

Прямо под названием приложения отображаются присвоенные [теги](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") и [JavaScript-фреймворки](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions."), которые показаны в раскрывающейся области **Tags and JavaScript frameworks**. Добавить новый тег здесь просто: нужно выбрать **Add tag**. Также есть кнопка **Framework settings**, которая ведёт к настройкам, связанным с [JavaScript-фреймворками](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions.").

## Анализ производительности

[Раздел **Performance analysis**](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/performance-analysis "Understand the available types of performance analysis that are provided by Dynatrace.") отображает ряд метрик производительности приложения. Чтобы просмотреть разделы, относящиеся к анализу производительности, нужно развернуть часть инфографики **Performance analysis**.

![Анализ производительности](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

Анализ производительности

## Поведение пользователей

[Раздел **User behavior**](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/user-behavior-analysis "Understand the user behavior analysis options that are provided by Dynatrace.") отображает ряд метрик поведения пользователей приложения. Чтобы просмотреть разделы, относящиеся к поведению пользователей, нужно развернуть часть инфографики **User behavior**.

![Поведение пользователей](https://dt-cdn.net/images/user-behaviour-2360-e98d95092b.png)

Поведение пользователей

## Анализ пользовательских сессий

Нужно выбрать **Analyze user sessions** в правом верхнем углу, чтобы провести полноценный [анализ пользовательской сессии по разным измерениям](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.").

## Закрепление на дашборде

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

Нужно выбрать **Pin to dashboard** в правом верхнем углу, чтобы добавить плитку для анализа производительности или поведения пользователей (в зависимости от того, какая часть развёрнута) на выбранный классический дашборд для быстрого просмотра анализа. Подробности см. в разделе [Закрепление плиток на дашборде](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Настройки приложения

Нужно выбрать **More** (**…**) в правом верхнем углу страницы, а затем выбрать **Edit**, чтобы получить доступ к настройкам приложения.

## Основные находки

Чтобы получить доступ к [Hyperlyzer](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer helps you visually query different application dimensions, for example, geolocation, browser, operating system, bandwidth, and user actions."), нужно выбрать **More** (**…**) > **Show top findings**. Здесь можно увидеть основные находки о том, где расположены пользователи, какую версию браузера они используют, какая у них операционная система, а также пользовательские действия, полученные приложением, отсортированные по длительности действия по убыванию (самые медленные действия считаются основными находками, поскольку они проблемные и требуют внимания).

## Представление Smartscape

Чтобы получить доступ к [представлению Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment."), нужно выбрать **More** (**…**) > **Smartscape view**. Smartscape предлагает быстрый, но при этом детальный обзор всех топологических зависимостей приложения.