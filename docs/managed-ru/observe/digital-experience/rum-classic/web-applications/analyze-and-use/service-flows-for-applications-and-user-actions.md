---
title: Схемы вызовов сервисов для приложений и действий пользователей в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions
---

# Схемы вызовов сервисов для приложений и действий пользователей в RUM Classic

# Схемы вызовов сервисов для приложений и действий пользователей в RUM Classic

* How-to guide
* 1-min read
* Published Oct 04, 2017

Dynatrace позволяет легко понять цепочку вызовов сервисов в контексте приложения и даже в контексте отдельных действий пользователя. [**Service flow**](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") показывает, какие сервисы вызываются каждым приложением или отдельным действием пользователя, и помогает понять, как эти сервисы вызывают друг друга.

## Доступ к service flow для приложения

Чтобы получить доступ к service flow для приложения

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать.
3. Выбрать плитку **Services** в правом нижнем углу инфографики Performance analysis.
4. В разделе **Called services** ниже выбрать **View service flow**.

   ![Serviceflow app 1](https://dt-cdn.net/images/01-serviceflow-app-1607-f0becdb963.png)

   Serviceflow app 1

   ![Serviceflow app 2](https://dt-cdn.net/images/02-serviceflow-app-1434-ec6bb8c89f.png)

   Serviceflow app 2

## Доступ к service flow для действия пользователя

Чтобы получить доступ к service flow для действия пользователя

1. Перейти в **Web**.
2. Выбрать приложение, которое включает действие пользователя, которое нужно проанализировать.
3. Прокрутить вниз до раздела **Top 3 user actions** и выбрать **View full details**.
4. На странице **User actions** выбрать действие пользователя, которое нужно проанализировать, из списков **Top 100 user actions** или **Key user actions**.
5. На странице **User action** прокрутить вниз до раздела **Top 3 web request contributors** и выбрать **View full details**.
6. Выбрать **View service flow**.

   ![Useraction serviceflow 1](https://dt-cdn.net/images/01-useraction-serviceflow-1607-63b0e6352a.png)

   Useraction serviceflow 1

   ![Useraction serviceflow 2](https://dt-cdn.net/images/02-useraction-serviceflow-1613-8fcb6f87cc.png)

   Useraction serviceflow 2