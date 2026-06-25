---
title: Анализ веб-запросов мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/analyze-and-use/analyze-web-requests-mobile
scraped: 2026-05-12T11:33:14.912222
---

# Анализ веб-запросов мобильных приложений

# Анализ веб-запросов мобильных приложений

* How-to guide
* 1-min read
* Published Jul 19, 2017

С помощью мониторинга на стороне клиента Dynatrace вы можете оценить производительность собственных и сторонних сервисов с точки зрения доступности, времени отклика и возникновения ошибок.

Чтобы отслеживать веб-запросы приложения:

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно проанализировать.
3. На странице обзора приложения выберите плитку **Web requests**.

Плитка **Web requests** показывает общее количество веб-запросов и частоту ошибок веб-запросов за выбранный период.

![Web requests tile on the application overview page](https://dt-cdn.net/images/web-requests-tile-mobile-app-2-852-01bbe5846b.png)

Web requests tile on the application overview page

Информация о частоте запросов, продолжительности запросов и ведущих поставщиках доступна в разделах **Web requests** и **Top providers**.

## Web requests — Error rate

Этот график сравнивает частоту веб-запросов (количество запросов в минуту) с частотой [ошибок](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Узнайте о событиях пользователей и ошибок, а также о типах событий, захватываемых Dynatrace.") за выбранный период.

![Web requests - Error rate tab](https://dt-cdn.net/images/web-requests-error-rate-790-fb758ee8a4.png)

Web requests - Error rate tab

## Web requests — Request time

Этот график сравнивает частоту веб-запросов со временем запроса за выбранный период.

![Web requests - Request time tab](https://dt-cdn.net/images/web-requests-request-time-790-aa8db1c006.png)

Web requests - Request time tab

## Top providers

Этот список включает HTTP-домены с наибольшим количеством исходящих запросов, инициированных вашим приложением за выбранный период.

![Top providers list](https://dt-cdn.net/images/top-providers-mobile-app-790-bb9125360d.png)

Top providers list

Чтобы просмотреть дополнительную информацию о поставщике, выберите его из списка. Откроется страница с подробными сведениями о поставщике, где доступны данные о частоте запросов, времени запроса и частоте ошибок для выбранного поставщика.

* Перейдите на вкладку **Web requests**, чтобы изучить информацию о конкретном веб-запросе: частоту, продолжительность и размер запроса, а также частоту ошибок и другие детали.
* Перейдите на вкладку **Errors**, чтобы просмотреть список ошибок веб-запросов для данного поставщика. Выберите ошибку, которую нужно проанализировать, чтобы открыть [страницу с подробными сведениями об ошибке веб-запроса](/managed/observe/digital-experience/session-segmentation/new-user-sessions#error-details-page "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации.").

![Provider details page opened on the Errors tab](https://dt-cdn.net/images/provider-detail-page-2131-734cbce65b.png)

Provider details page opened on the Errors tab