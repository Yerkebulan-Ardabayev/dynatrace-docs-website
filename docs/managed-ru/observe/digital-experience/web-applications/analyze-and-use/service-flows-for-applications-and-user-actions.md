---
title: Потоки сервисов для приложений и пользовательских действий
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions
scraped: 2026-05-12T11:35:14.082179
---

# Потоки сервисов для приложений и пользовательских действий

# Потоки сервисов для приложений и пользовательских действий

* How-to guide
* 1-min read
* Published Oct 04, 2017

Dynatrace позволяет легко понять цепочку потока сервисов в контексте приложения и даже в контексте отдельных пользовательских действий. [**Service flow**](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") показывает, какие сервисы вызываются каждым приложением или отдельным пользовательским действием, и помогает понять, как эти сервисы вызывают друг друга.

## Доступ к потоку сервисов для приложения

Чтобы открыть поток сервисов для приложения:

1. Перейдите в **Web**.
2. Выберите приложение для анализа.
3. Выберите плитку **Services** в нижнем правом углу инфографики Performance analysis.
4. В разделе **Called services** ниже выберите **View service flow**.

   ![Serviceflow app 1](https://dt-cdn.net/images/01-serviceflow-app-1607-f0becdb963.png)

   Serviceflow app 1

   ![Serviceflow app 2](https://dt-cdn.net/images/02-serviceflow-app-1434-ec6bb8c89f.png)

   Serviceflow app 2

## Доступ к потоку сервисов для пользовательского действия

Чтобы открыть поток сервисов для пользовательского действия:

1. Перейдите в **Web**.
2. Выберите приложение, включающее пользовательское действие для анализа.
3. Прокрутите страницу вниз до раздела **Top 3 user actions** и выберите **View full details**.
4. На странице **User actions** выберите нужное пользовательское действие из списков **Top 100 user actions** или **Key user actions**.
5. На странице **User action** прокрутите страницу вниз до раздела **Top 3 web request contributors** и выберите **View full details**.
6. Выберите **View service flow**.

   ![Useraction serviceflow 1](https://dt-cdn.net/images/01-useraction-serviceflow-1607-63b0e6352a.png)

   Useraction serviceflow 1

   ![Useraction serviceflow 2](https://dt-cdn.net/images/02-useraction-serviceflow-1613-8fcb6f87cc.png)

   Useraction serviceflow 2