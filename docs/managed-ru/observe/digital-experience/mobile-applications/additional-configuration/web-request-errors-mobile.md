---
title: Игнорирование ошибок веб-запросов для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/web-request-errors-mobile
scraped: 2026-05-12T11:32:54.781930
---

# Игнорирование ошибок веб-запросов для мобильных приложений

# Игнорирование ошибок веб-запросов для мобильных приложений

* How-to guide
* 1-min read
* Published Aug 30, 2021

По умолчанию Dynatrace помечает все коды состояния ответа `4xx` и `5xx` как [ошибки](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Узнайте о событиях пользователей и ошибок, а также о типах событий, захватываемых Dynatrace.") веб-запросов. Однако некоторые неуспешные HTTP-коды на самом деле могут не указывать на проблему с вашим приложением. Например, код состояния `401 Unauthorized` иногда просто означает, что пользователь решил не выполнять вход. Другой пример — код `429 Too Many Requests`, который может указывать на проблемы с регулированием, не вызванные вашим приложением.

Чтобы игнорировать определённые HTTP-коды состояния, настройте, какие коды не должны помечаться как ошибки. При создании правила исключения можно указывать отдельные HTTP-коды состояния, например `401`, или диапазоны кодов, например `400-499`.

Чтобы создать правило исключения:

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Request errors**.
5. Нажмите **Add exclusion rule** и укажите HTTP-код состояния или диапазон кодов, которые должны считаться успешными.

   ![Configure an exclusion rule](https://dt-cdn.net/images/mobile-exclusion-rules-2124-75133d34c8.png)

   Configure an exclusion rule

После настройки правила исключения веб-запросы с ранее ошибочными кодами состояния будут считаться успешными при расчёте частоты ошибок. Это повлияет на рейтинг Apdex приложения, частоту ошибок запросов и список ошибок веб-запросов, а также на некоторые метрики пользовательских действий и пользовательские метрики.

Например, посмотрите на скриншоты страницы обзора приложения ниже и обратите внимание на снижение частоты ошибок веб-запросов. Это произошло после настройки правила игнорирования кода ответа `401 Unauthorized` для данного приложения. Также обратите внимание на снижение частоты ошибок для ведущих поставщиков приложения, а также на более высокий рейтинг Apdex и меньшую частоту ошибок для одного из пользовательских действий.

#### Страница обзора приложения

До

После

![Application overview page - before configuring exclusion rules](https://dt-cdn.net/images/app-overview-page-web-requests-before-2134-3ceead505c.png)

Application overview page - before configuring exclusion rules

![Application overview page - after configuring exclusion rules](https://dt-cdn.net/images/app-overview-page-web-requests-after-2134-0dc0ca7d48.png)

Application overview page - after configuring exclusion rules

#### Список ведущих поставщиков

До

После

![Top providers - before configuring exclusion rules](https://dt-cdn.net/images/top-providers-before-2134-0f17ca6d01.png)

Top providers - before configuring exclusion rules

![Top providers - after configuring exclusion rules](https://dt-cdn.net/images/top-providers-after-2134-283506ceaf.png)

Top providers - after configuring exclusion rules

#### Страница с подробностями пользовательского действия

До

После

![User action detail page - before configuring exclusion rules](https://dt-cdn.net/images/user-action-detail-page-before-2132-f989f87e3b.png)

User action detail page - before configuring exclusion rules

![User action detail page - after configuring exclusion rules](https://dt-cdn.net/images/user-action-detail-page-after-2132-8e9e2e559c.png)

User action detail page - after configuring exclusion rules