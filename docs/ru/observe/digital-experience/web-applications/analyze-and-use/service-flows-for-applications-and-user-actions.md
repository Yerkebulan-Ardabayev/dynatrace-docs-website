---
title: Потоки сервисов для приложений и действий пользователя
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions
scraped: 2026-03-05T21:27:38.698380
---

# Сервисные потоки для приложений и пользовательских действий


* Classic
* How-to guide
* 1-min read
* Published Oct 04, 2017

Dynatrace позволяет легко понять цепочку сервисного потока в контексте вашего приложения и даже в контексте отдельных пользовательских действий. [**Сервисный поток**](../../../application-observability/services-classic/service-flow.md "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") показывает, какие сервисы вызываются каждым приложением или отдельным пользовательским действием, и помогает понять, как эти сервисы взаимодействуют друг с другом.

## Доступ к сервисному потоку приложения

Чтобы перейти к сервисному потоку приложения:

1. Перейдите в раздел **Web**.
2. Выберите приложение, которое хотите проанализировать.
3. Выберите плитку **Services** в правом нижнем углу инфографики анализа производительности.
4. В разделе **Called services** ниже выберите **View service flow**.

   ![Serviceflow app 1](https://dt-cdn.net/images/01-serviceflow-app-1607-f0becdb963.png)

   ![Serviceflow app 2](https://dt-cdn.net/images/02-serviceflow-app-1434-ec6bb8c89f.png)

## Доступ к сервисному потоку пользовательского действия

Чтобы перейти к сервисному потоку пользовательского действия:

1. Перейдите в раздел **Web**.
2. Выберите приложение, содержащее пользовательское действие, которое вы хотите проанализировать.
3. Прокрутите вниз до раздела **Top 3 user actions** и выберите **View full details**.
4. На странице **User actions** выберите нужное пользовательское действие из списков **Top 100 user actions** или **Key user actions**.
5. На странице **User action** прокрутите вниз до раздела **Top 3 web request contributors** и выберите **View full details**.
6. Выберите **View service flow**.

   ![Useraction serviceflow 1](https://dt-cdn.net/images/01-useraction-serviceflow-1607-63b0e6352a.png)

   ![Useraction serviceflow 2](https://dt-cdn.net/images/02-useraction-serviceflow-1613-8fcb6f87cc.png)
