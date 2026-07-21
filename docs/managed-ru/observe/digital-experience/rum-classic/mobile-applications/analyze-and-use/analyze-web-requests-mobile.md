---
title: Анализ веб-запросов для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/analyze-web-requests-mobile
---

# Анализ веб-запросов для мобильных приложений в RUM Classic

# Анализ веб-запросов для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение 1 мин
* Опубликовано 19 июля 2017 г.

С клиентским мониторингом Dynatrace можно оценить производительность собственных и сторонних сервисов по доступности, времени отклика и количеству ошибок.

Мониторинг веб-запросов приложения

1. Перейти в **Frontend**.
2. Выбрать приложение для анализа.
3. На странице обзора приложения выбрать плитку **Web requests**.

Плитка **Web requests** показывает общее количество веб-запросов и долю ошибок веб-запросов за выбранный период.

![Web requests tile on the application overview page](https://dt-cdn.net/images/web-requests-tile-mobile-app-2-852-01bbe5846b.png)

Плитка Web requests на странице обзора приложения

Информация о частоте запросов, времени выполнения запросов и основных провайдерах доступна в разделах **Web requests** и **Top providers**.

## Web requests, доля ошибок

Этот график сравнивает частоту веб-запросов, количество веб-запросов в минуту, с долей [ошибок](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") за выбранный период.

![Web requests - Error rate tab](https://dt-cdn.net/images/web-requests-error-rate-790-fb758ee8a4.png)

Вкладка Web requests, доля ошибок

## Web requests, время запроса

Этот график сравнивает частоту веб-запросов со временем запроса за выбранный период.

![Web requests - Request time tab](https://dt-cdn.net/images/web-requests-request-time-790-aa8db1c006.png)

Вкладка Web requests, время запроса

## Top providers

Этот список включает HTTP-домены с наибольшим количеством исходящих запросов, инициированных приложением за выбранный период.

![Top providers list](https://dt-cdn.net/images/top-providers-mobile-app-790-bb9125360d.png)

Список Top providers

Чтобы просмотреть дополнительную информацию о провайдере, нужно выбрать его в списке. Откроется страница сведений о провайдере, на которой доступны данные о частоте запросов, времени запроса и доле ошибок для выбранного провайдера.

* Перейти на вкладку **Web requests**, чтобы изучить информацию по конкретному веб-запросу: частоту, длительность, размер, а также долю ошибок и другие сведения.
* Перейти на вкладку **Errors**, чтобы просмотреть список ошибок веб-запросов для этого провайдера. Выбрать ошибку для анализа, чтобы открыть [страницу сведений об ошибке веб-запроса](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#error-details-page "Learn about user session segmentation and filtering attributes.").

![Provider details page opened on the Errors tab](https://dt-cdn.net/images/provider-detail-page-2131-734cbce65b.png)

Страница сведений о провайдере, открытая на вкладке Errors