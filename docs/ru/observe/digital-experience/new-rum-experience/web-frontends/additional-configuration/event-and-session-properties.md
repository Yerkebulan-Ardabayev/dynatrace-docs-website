---
title: Capture event and session properties for web frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties
scraped: 2026-03-05T21:32:50.462070
---

# Сбор свойств событий и сессий для веб-фронтендов

# Сбор свойств событий и сессий для веб-фронтендов

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

Свойства событий и сессий позволяют прикреплять пользовательские пары ключ-значение к пользовательским событиям и пользовательским сессиям с помощью пространств имён [`event_properties`](/docs/semantic-dictionary/model/rum/user-events#event-properties "Пользовательские события обеспечивают глубокую видимость и понимание опыта, поведения, производительности и ошибок ваших клиентов и конечных пользователей в режиме реального времени.") и [`session_properties`](/docs/semantic-dictionary/model/rum/user-sessions#user-session-properties "Пользовательские сессии предоставляют сводку пользовательских событий одного клиента или конечного пользователя вашего приложения за ограниченный период времени.").

## Перед началом отправки свойств событий или сессий

Свойства событий и сессий необходимо настроить перед использованием. Входящие свойства событий и сессий, которые не настроены, отбрасываются во время приёма событий.

Чтобы настроить свойство события или сессии:

1. В ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** выберите фронтенд, для которого вы хотите добавить свойство.
2. На вкладке **Settings** выберите **Event and session properties**.
3. В зависимости от того, хотите ли вы настроить свойство события или сессии, выберите **Add** в разделе **Defined event properties** или **Defined session properties**.
4. В поле **Field name** укажите имя, например `cart.total_value`.
5. Если вы хотите, чтобы валидация имени поля была нечувствительна к регистру, включите **Field name validation should be case-insensitive**.
6. В разделе **Datatype** выберите один из доступных типов — `string`, `boolean` или `number`.

Обратите внимание, что имя поля всегда имеет префикс `event_properties.` или `session_properties.` в зависимости от выбранного типа, например `event_properties.cart.total_value`.

## Как отправлять свойства

Свойства событий и сессий можно отправлять через JavaScript API:

* Для добавления свойств события используйте [`addEventModifier`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.addEventModifier.html).
* Для отправки свойства сессии используйте [`sendSessionPropertyEvent`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.sendSessionPropertyEvent.html).

## Ограничения

* **Именование**

  + Максимальная длина имени поля: 100 символов (включая префикс `event_properties.` / `session_properties.`).
  + Допустимые символы в имени поля: A–Z, a–z, 0–9, символ подчёркивания `_` и точка `.`.
* **Количество**

  + Может быть настроено максимум 20 свойств событий и сессий.
* **Значения**

  + Для свойств событий и сессий с типом данных string длина ограничена 1000 символами.
