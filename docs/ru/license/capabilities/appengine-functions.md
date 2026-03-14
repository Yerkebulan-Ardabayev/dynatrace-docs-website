---
title: Обзор AppEngine Functions (Serverless Functions) (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/appengine-functions
scraped: 2026-03-04T21:37:03.569424
---

# Обзор AppEngine Functions (бессерверных функций) (DPS)


* Latest Dynatrace
* Explanation
* 6-min read
* Updated on May 22, 2025

AppEngine Functions — это серверная часть вашего приложения.
Они написаны на TypeScript и выполняются в [среде выполнения Dynatrace JavaScript](https://developer.dynatrace.com/reference/javascript-runtime/).

Существует три типа AppEngine Functions:

* Функции приложения (App functions):
  Эти функции представляют собой серверную часть приложения и собираются, упаковываются и развёртываются вместе с вашим пользовательским приложением.
* Разовые функции (Ad-hoc functions):
  Пользовательский код, предназначенный для решения конкретной задачи, называется разовой функцией.
  Эти функции могут быть вызваны из ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** или непосредственно через API.
* Пользовательские действия (Custom actions):
  Специальный тип функции приложения, который вместе с компонентом пользовательского интерфейса может быть объявлен как пользовательское действие рабочего процесса для расширения ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
  Пользовательские действия можно затем выбрать в качестве задачи в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** и выполнять в рамках рабочего процесса.

Все AppEngine Functions развёртываются в среде с 256 МиБ оперативной памяти.

AppEngine Functions работают без дополнительной настройки: внешний хостинг не требуется, и нет необходимости заботиться о поддержке среды выполнения для исполнения логики или кода.

## Связанные темы

* [AppEngine](../../platform/appengine.md "Разрабатывайте многофункциональные Dynatrace-приложения для себя и всего мира!")
* [Функции приложений](https://developer.dynatrace.com/develop/functions/ "Основные концепции функций приложений, представляющих серверную часть приложения")
* [Лицензирование Dynatrace](../../license.md "О подписке Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace.")
* [Цены Dynatrace](https://www.dynatrace.com/pricing/)
