---
title: Анализ веб-запросов для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/analyze-web-requests-custom
---

# Анализ веб-запросов для пользовательских приложений в RUM Classic

# Анализ веб-запросов для пользовательских приложений в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Опубликовано 30 января 2023 г.

С помощью мониторинга на стороне клиента Dynatrace можно оценить производительность собственных и сторонних сервисов с точки зрения доступности, времени отклика и количества ошибок.

Чтобы отслеживать веб-запросы приложения

1. Перейти в **Frontend**.
2. Выбрать приложение, которое нужно проанализировать.
3. На странице обзора приложения выбрать плитку **Web requests**.

Плитка **Web requests** показывает общее количество веб-запросов и частоту ошибок веб-запросов за выбранный период времени.

![Web requests tile on the application overview page](https://dt-cdn.net/images/web-requests-tile-mobile-app-2-852-01bbe5846b.png)

Плитка Web requests на странице обзора приложения

Информация о частоте запросов, длительности запросов и основных провайдерах доступна в разделах **Web requests** и **Top providers**.

## Web requests - Error rate

На этой диаграмме частота веб-запросов (количество веб-запросов в минуту) сравнивается с частотой [ошибок](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") за выбранный период времени.

![Web requests - Error rate tab](https://dt-cdn.net/images/web-requests-error-rate-790-fb758ee8a4.png)

Вкладка Web requests - Error rate

## Web requests - Request time

На этой диаграмме частота веб-запросов сравнивается с временем запроса за выбранный период времени.

![Web requests - Request time tab](https://dt-cdn.net/images/web-requests-request-time-790-aa8db1c006.png)

Вкладка Web requests - Request time

## Top providers

Этот список включает HTTP-домены, содержащие наибольшее количество исходящих запросов, инициированных приложением за выбранный период времени.

![Top providers list](https://dt-cdn.net/images/top-providers-mobile-app-790-bb9125360d.png)

Список Top providers

Чтобы просмотреть дополнительную информацию о провайдере, нужно выбрать его из списка. Откроется страница сведений о провайдере, где доступны данные о частоте запросов, времени запроса и частоте ошибок для выбранного провайдера.

* Перейти на вкладку **Web requests**, чтобы изучить информацию о конкретном веб-запросе, такую как частота запросов, длительность и размер, а также частоту ошибок и некоторые другие сведения.
* Перейти на вкладку **Errors**, чтобы просмотреть список ошибок веб-запросов для этого провайдера. Нужно выбрать ошибку, которую требуется проанализировать, чтобы открыть [страницу сведений об ошибке веб-запроса](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#error-details-page "Learn about user session segmentation and filtering attributes.").

![Provider details page opened on the Errors tab](https://dt-cdn.net/images/provider-detail-page-2131-734cbce65b.png)

Страница сведений о провайдере, открытая на вкладке Errors