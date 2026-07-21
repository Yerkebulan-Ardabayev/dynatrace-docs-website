---
title: Real User Monitoring Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview
---

# Real User Monitoring Classic

# Real User Monitoring Classic

* Пояснение
* 1 минута на чтение
* Обновлено 20 октября 2023 г.

Dynatrace Real User Monitoring Classic (RUM Classic) даёт возможность узнать своих клиентов, предоставляя анализ производительности в реальном времени. Сюда входят все действия пользователей и то, как разные действия влияют на производительность. Также можно легко выявлять проблемы или ошибки, оценки пользовательского опыта, разбивку по геолокации и многое другое. Кроме того, можно получить представление о поведении пользователей, в том числе о количестве клиентов, возвращающихся на сайт. С Dynatrace RUM доступен контекст во времени и мгновенный анализ полной картины пользовательского опыта.

Базовые концепции RUM строятся вокруг [пользовательских сессий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") и [пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application."). Пользовательская сессия, это, по сути, «визит пользователя» в приложении. Dynatrace фиксирует пользовательские сессии [веб-приложений](/managed/observe/digital-experience/web-applications "Learn how to configure and use Real User Monitoring for your web applications."), [мобильных приложений](/managed/observe/digital-experience/mobile-applications "Configure and use Real User Monitoring for your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications "Learn how to configure and use Real User Monitoring for your custom applications."). Одна пользовательская сессия может охватывать несколько приложений.

![User session structure for individual user](https://dt-cdn.net/images/sus-6343-user-session-structure-2500-594cf1dae0.png)

Структура пользовательской сессии для отдельного пользователя

Dynatrace может отслеживать активность одного пользователя на разных устройствах. Это значит, что если пользователь начинает работать с приложением на мобильном телефоне, а позже продолжает через десктопный браузер, Dynatrace может связать все эти пользовательские сессии с этим конкретным пользователем.

Лицензирование Dynatrace Real User Monitoring Classic основано на потреблении пользовательских сессий. Подробнее см. [Обзор Real User и Synthetic Monitoring (DPS)](/managed/license/capabilities/real-user-synthetic-monitoring "Learn how Dynatrace Real User and Synthetic Monitoring consumption is calculated using the Dynatrace Platform Subscription model.").

## Похожие темы

* [Что такое Real User Monitoring (RUM)?﻿](https://www.dynatrace.com/news/blog/what-is-real-user-monitoring/)
* [Real User Monitoring﻿](https://www.dynatrace.com/platform/real-user-monitoring/)