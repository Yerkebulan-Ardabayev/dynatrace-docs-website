---
title: User sessions API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/user-sessions
scraped: 2026-05-12T11:12:44.786409
---

# User sessions API

# User sessions API

* Reference
* Updated on May 02, 2022

API **User Sessions** позволяет получать данные о пользовательских сессиях. API использует [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как обращаться к данным пользовательских сессий и запрашивать их с помощью ключевых слов, синтаксиса, функций и многого другого.") для запроса требуемых данных. Оба вызова возвращают одни и те же данные, отличаясь только их представлением.

[### GET table

Запрос GET table выполняет USQL-запрос и возвращает результаты в виде табличной структуры запрошенных столбцов.](/managed/dynatrace-api/environment-api/rum/user-sessions/table "Просмотр данных пользовательских сессий в табличной форме через Dynatrace API.")[### GET tree

Запрос GET tree выполняет USQL-запрос и возвращает результаты в виде древовидной структуры запрошенных столбцов: плоского списка, содержащего запрошенные столбцы.](/managed/dynatrace-api/environment-api/rum/user-sessions/tree "Просмотр данных пользовательских сессий в древовидной форме через Dynatrace API.")[### Структура пользовательской сессии

Изучите структуру пользовательской сессии, содержащую все возможные поля.](/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure "Изучите структуру пользовательской сессии в Dynatrace User Session Query language API.")

## Связанные темы

* [Пользовательские запросы, сегментация и агрегация данных сессий](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как обращаться к данным пользовательских сессий и запрашивать их с помощью ключевых слов, синтаксиса, функций и многого другого.")