---
title: Обзор страницы приложения
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview
scraped: 2026-05-12T11:34:35.004446
---

# Обзор страницы приложения

# Обзор страницы приложения

* Explanation
* 2-min read
* Published Jul 11, 2019

Страница обзора приложения, организованная в понятные и интуитивные разделы, позволяет проводить всесторонний анализ как производительности приложения, так и поведения пользователей.

Чтобы перейти на страницу обзора приложения:

1. Перейдите в **Web**.
2. Выберите приложение.

## Фильтрация

Анализ можно выполнять по конкретному измерению, выбранному в фильтре в верхней части страницы обзора приложения. Например, выбрав **User type**, можно указать, следует ли выполнять анализ на основе данных от **Synthetic**, **Real users** или **Robots**.

## Теги и JavaScript-фреймворки

Непосредственно под именем приложения отображаются назначенные [теги](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") и [JavaScript-фреймворки](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.") в разворачиваемой области **Tags and JavaScript frameworks**. Добавить новые теги здесь просто — выберите **Add tag**. Также есть кнопка **Framework settings**, которая ведёт к настройкам [JavaScript-фреймворков](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

## Анализ производительности

В [разделе **Performance analysis**](/managed/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Understand the available types of performance analysis that are provided by Dynatrace.") отображается ряд метрик производительности приложения. Чтобы просмотреть разделы, относящиеся к анализу производительности, разверните часть **Performance analysis** инфографики.

![Performance analysis](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

Performance analysis

## Поведение пользователей

В [разделе **User behavior**](/managed/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis "Understand the user behavior analysis options that are provided by Dynatrace.") отображается ряд метрик поведения пользователей приложения. Чтобы просмотреть разделы, относящиеся к поведению пользователей, разверните часть **User behavior** инфографики.

![User behavior](https://dt-cdn.net/images/user-behaviour-2360-e98d95092b.png)

User behavior

## Анализ пользовательских сессий

Выберите **Analyze user sessions** в правом верхнем углу для всестороннего [анализа пользовательских сессий по различным измерениям](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").

## Закрепление на дашборде

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

Выберите **Pin to dashboard** в правом верхнем углу, чтобы добавить плитку анализа производительности или поведения пользователей (в зависимости от развёрнутой части) на предпочтительный классический дашборд для быстрого анализа. Подробнее см. в разделе [Закрепление плиток на дашборде](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Настройки приложения

Выберите **More** (**…**) в правом верхнем углу страницы, а затем **Edit** для доступа к настройкам приложения.

## Топ результатов

Для доступа к [Hyperlyzer](/managed/observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer helps you visually query different application dimensions, for example, geolocation, browser, operating system, bandwidth, and user actions.") выберите **More** (**…**) > **Show top findings**. Здесь можно просмотреть топ результатов: местоположение пользователей, версию браузера, операционную систему и пользовательские действия приложения, отсортированные по продолжительности действия в порядке убывания (самые медленные действия считаются топ результатами, так как именно они являются проблематичными и требуют внимания).

## Представление Smartscape

Для доступа к [Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.") выберите **More** (**…**) > **Smartscape view**. Smartscape предоставляет быстрый, но детальный обзор всех топологических зависимостей приложения.