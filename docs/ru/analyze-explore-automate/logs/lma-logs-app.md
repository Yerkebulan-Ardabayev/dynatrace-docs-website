---
title: Logs app
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app
scraped: 2026-03-06T21:09:41.161992
---

# Приложение Logs

# Приложение Logs

* Последняя версия Dynatrace
* Приложение
* Чтение: 4 мин
* Обновлено 01 июля 2025 г.

Предварительные требования

### Разрешения

В следующей таблице описаны необходимые разрешения.

storage:spans:read

разрешение на чтение спанов, Segments Variables (необязательно)

storage:bizevents:read

разрешение на чтение бизнес-событий, Segments Variables (необязательно)

storage:metrics:read

разрешение на чтение метрик, Segments Variables (необязательно)

storage:events:read

разрешение на чтение событий, Segments Variables (необязательно)

storage:security.events:read

разрешение на чтение событий безопасности, Segments Variables (необязательно)

storage:logs:read

разрешение на чтение логов

storage:user.sessions:read

разрешение на чтение пользовательских сессий, Segments Variables (необязательно)

storage:user.events:read

разрешение на чтение пользовательских событий

storage:buckets:read

разрешение на чтение логов

storage:files:read

разрешение на выполнение join-операций с таблицами подстановок

### Установка

Убедитесь, что приложение [установлено в вашей среде](/docs/manage/hub#install "Информация о Dynatrace Hub.").

Начало работы

Основные понятия

![Динамическая гистограмма с интуитивно понятным фильтром по нажатию обеспечивает уникальный опыт для упрощённого и своевременного исследования логов.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/3.png)![Функция "Explain Logs" предоставляет практические шаги и аналитику для сокращения анализа первопричин и времени реакции, позволяя быстрее решать проблемы.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/2.png)![Наглядные, наложенные друг на друга тренды по уровням серьёзности с быстрыми и интуитивными опциями фильтрации помогают легко исследовать логи в формате JSON и другие логи.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/1.png)![Сокращайте MTTR, превращая необработанные логи в управляемую аналитику — в контексте трейса или связанных топологических сущностей.](https://dt-cdn.net/hub/logs-hub-4.png)![Детали логов предоставляют богатый контекст в один клик — доступ к связанным трейсам, топологии и многому другому. Мгновенные фильтры превращают аналитику в точные поисковые запросы.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/4.png)

1 из 5 — Динамическая гистограмма с интуитивно понятным фильтром по нажатию обеспечивает уникальный опыт для упрощённого и своевременного исследования логов.

[01Запросы и фильтрация логов

* Практическое руководство
* Исследуйте логи с помощью DQL-запросов и операторов фильтрации в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter)[02Выявление трендов с помощью диаграммы распределения логов

* Практическое руководство
* Получите наглядный обзор записей логов, сгруппированных по статусу, чтобы выявлять тренды, обнаруживать аномалии и выполнять целевые запросы, не покидая визуализацию.](/docs/analyze-explore-automate/logs/lma-logs-app/log-distribution-chart)[03Просмотр окружающих логов

* Практическое руководство
* Используйте окружающие логи для понимания данных в контексте в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs)[04Фильтрация с помощью фасетов

* Практическое руководство
* Фильтрация с помощью фасетов в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/facets)[05Настройка сообщения лога

* Практическое руководство
* Настройка сообщения лога в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/message)[06Ограничения в Logs

* Справочник
* Узнайте об ограничениях, применяемых в приложении Logs, и о том, как их изменить.](/docs/analyze-explore-automate/logs/lma-logs-app/limits)

## О приложении Logs

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** — это отправная точка для поиска нужных записей логов без написания запросов.

* Находите нужные логи.
  Легко фильтруйте логи без написания DQL и находите нужные записи.
* Проактивное расследование.
  Обнаруживайте проблемы и получайте аналитику, исследуя диаграмму распределения логов по времени.
* Определяйте первопричину проблем из контекста.
  Исследуйте окружающие логи, чтобы понять контекст и первопричину ошибок:

  + Находите первопричину и проверяйте, является ли лог лишь симптомом проблемы.
  + На основе трейсов: просматривайте детали транзакций в распределённой среде.
  + На основе источника: анализируйте выбранную запись в контексте отдельного компонента.
* Расширяйте свой анализ.
  Быстро переключайтесь между деталями логов и связанными хостами, кластерами Kubernetes, трейсами или другими сущностями.
  Это помогает понять влияние отдельной записи в контексте связанных метрик и трейсов.
* Делитесь результатами.
  Продолжите работу с логами в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** или автоматизируйте с помощью ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

## Часто задаваемые вопросы

Можно ли редактировать DQL-запрос?

Выберите **Edit DQL query** в меню рядом с кнопкой **Run query**.

Как лицензируются логи?

Запросы к логам работают на основе того же лицензирования, что и другие функции Log Management and Analytics.

* Если в вашем тарифе **Retain** и **Query** являются отдельными позициями, вы потребляете лицензию только за объём запрошенных логов в байтах.
  Подробнее см. в разделе [Calculate your consumption of Log Management & Analytics - Query (DPS)](/docs/license/capabilities/log-analytics/dps-log-query "Узнайте, как рассчитывается потребление ресурсов Log Management & Analytics - Query DPS.").
* Если в вашем тарифе указано **Retain with Included Queries**, включённые запросы не тарифицируются.
  Подробнее см. в разделе [Log Analytics (DPS)](/docs/license/capabilities/log-analytics#log-retain-included-queries "Узнайте, как рассчитывается потребление Dynatrace Log Analytics в модели Dynatrace Platform Subscription.").

Следующие действия бесплатны:

* Фасеты и подсказки в поле фильтра.
* Построение диаграммы распределения логов.
* Поиск по ранее полученным результатам (с помощью строки поиска над таблицей).

Лицензия потребляется только при нажатии кнопки **Run query** или при использовании функции **Surrounding logs**.

Как настроить доступ к Logs?

Пользователи должны иметь доступ к Dynatrace Platform и логам, хранящимся в Grail ([см. встроенные политики доступа](/docs/platform/upgrade#built-in-policies "Используйте возможности Grail, AppEngine и AutomationEngine для улучшения хранения и анализа данных наблюдаемости и безопасности.")). Приложение заменяет экран **Logs and Events**, поэтому пользователи, которые ранее работали с логами, могут использовать ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Откройте в Dynatrace Hub

[Находите нужные записи логов без написания DQL-запросов.](https://www.dynatrace.com/hub/detail/logs/?internal_source=doc&internal_medium=link&internal_campaign=cross/)
