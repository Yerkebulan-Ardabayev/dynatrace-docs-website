---
title: Events API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1
scraped: 2026-05-12T12:05:46.151224
---

# Events API v1

# Events API v1

* Reference
* Updated on Jun 13, 2022
* Deprecated

Этот API устарел. Используйте [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2.") вместо него.

API **Events** возвращает детали обо всех некоррелированных событиях, которые Dynatrace собирает в вашем окружении. Возвращаемая информация по каждому событию включает атрибуты источника события, сущности, на которой событие было собрано, и другие специфичные для события сведения.

### Лента событий

[Получить глобальную ленту](/managed/dynatrace-api/environment-api/events-v1/get-events-feed "Список ленты событий через Dynatrace API.") **всех** некоррелированных событий в окружении.

### Просмотр события

[Получить параметры](/managed/dynatrace-api/environment-api/events-v1/get-event "Просмотр параметров события через Events API v1.") конкретного события по его ID.

### Отправка событий

[Отправить внешние события](/managed/dynatrace-api/environment-api/events-v1/post-event "Создание пользовательского события через Dynatrace API.") в ваше Dynatrace-окружение.

### Отправка событий Jenkins

[Настройте автоматический экспорт](/managed/dynatrace-api/environment-api/events-v1/push-deployment-events-from-jenkins "Отправка событий развёртывания Jenkins в Dynatrace.") событий развёртывания из Jenkins в Dynatrace.

## Связанные темы

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий, поддерживаемых типах событий, уровнях критичности и логике их формирования.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Понимание секции Events на странице обзора хостов, процессов и сервисов.")
* [Creating a deployment event via the Dynatrace API](https://www.youtube.com/watch?v=LDAiUMdrtvA)