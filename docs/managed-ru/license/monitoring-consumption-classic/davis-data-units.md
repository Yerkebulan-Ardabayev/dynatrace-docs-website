---
title: Расширение Dynatrace (единицы Davis data units)
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units
scraped: 2026-05-12T11:27:40.659227
---

# Расширение Dynatrace (единицы Davis data units)

# Расширение Dynatrace (единицы Davis data units)

* 8-min read
* Published Mar 30, 2020

Davis data units (DDU) — простое средство лицензирования определённых возможностей (пользовательских метрик, мониторинга логов и пользовательских событий) на платформе Dynatrace. DDU можно рассматривать как своеобразную валюту Dynatrace. Подобно тому, как потребление Dynatrace RUM и Synthetic Monitoring основано на [единицах Digital Experience Monitoring (DEM)](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), DDU обеспечивают единую модель потребления для пользовательских метрик, Log Monitoring и пользовательских событий.

Поскольку DDU основаны на потреблении, вы приобретаете определённый объём, и доступная квота расходуется со временем в зависимости от объёма мониторинга в вашей среде. Этот подход существенно упрощает контроль и мониторинг потребления метрик (например, при некорректно настроенных метриках) и выявление основных потребителей в среде. Подробнее о лицензировании метрик с помощью DDU см. в [Расчёт стоимости метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

Для получения полной информации о расчёте потребления мониторинга Dynatrace см. [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

## Объёмы Davis data units

DDU приобретаются объёмами по 1 миллиону единиц на срок контракта 1–3 года, при этом полный объём лицензированных единиц восстанавливается в начале каждого года. Например, при покупке 100 миллионов DDU на 3 года вы можете потреблять 100 миллионов DDU ежегодно в течение 3 лет.

Вы можете приобрести дополнительные DDU в любое время при исчерпании квоты. Обратитесь к своему представителю по продажам Dynatrace. Для удобства управления потреблением и предотвращения перерасходов в продукте отображаются уведомления, когда потреблено `90%` и `100%` лицензированных DDU.

### Бесплатный уровень Davis data units

Каждая новая среда Dynatrace SaaS и каждая лицензия Dynatrace Managed получают 200 000 DDU бесплатно. Это соответствует 381 метрике с частотой захвата 1 раз в минуту. Бесплатный уровень позволяет тестировать функции и оценивать ценность мониторинга Dynatrace до начала оплаты. Бесплатные 200 000 DDU автоматически обновляются ежегодно в начале нового периода лицензии для каждого аккаунта. Это преимущество недоступно для аккаунтов Offline или с оплатой по факту использования.

## Просмотр деталей потребления DDU по среде

Для доступа к этой странице необходимо разрешение **Manage monitoring settings** или учётная запись администратора. См. [Разрешения управления аккаунтом](/managed/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management").

Чтобы узнать, сколько DDU потреблено в вашей среде, перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**. Там можно просмотреть потребление DDU и определить основных потребителей.

На этой странице представлен обзор потребления DDU по пулам, а также детальный вид по мониторируемым сущностям (хост, сервис, группа процессов, приложение и другие). Вторичная навигация позволяет углубиться в детали потребления по пулу DDU (например, метрики, Log Monitoring, события).

### Получение деталей потребления DDU через API

Детали потребления DDU можно также [получить через API](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API."). Для получения деталей по пулам через API доступны следующие метрики:

* `builtin:billing.ddu.metrics.total`
* `builtin:billing.ddu.metrics.byEntity`
* `builtin:billing.ddu.metrics.byMetric`
* `builtin:billing.ddu.log.total`
* `builtin:billing.ddu.log.byEntity`
* `builtin:billing.ddu.log.byDescription`
* `builtin:billing.ddu.serverless.total`
* `builtin:billing.ddu.serverless.byEntity`
* `builtin:billing.ddu.serverless.byDescription`
* `builtin:billing.ddu.events.total`
* `builtin:billing.ddu.events.byEntity`
* `builtin:billing.ddu.events.byDescription`
* `builtin:billing.ddu.traces.total`
* `builtin:billing.ddu.traces.byEntity`
* `builtin:billing.ddu.traces.byDescription`

### Получение потребления DDU по зоне управления

Приведённые метрики не поддерживают фильтрацию по зоне управления напрямую, однако API можно использовать для этой цели, что позволяет решать требования межведомственного учёта и создавать отчёты о потреблении мониторируемых сущностей с разбивкой по зонам управления.

Пример скрипта для отчётности по зонам управления приведён в [репозитории Dynatrace snippets на GitHub](https://github.com/Dynatrace/snippets/tree/master/api/ddu/management-zone-calculation).
Скрипт обращается к метрике `builtin:billing.ddu.metrics.byEntity` и позволяет запрашивать потребление пула метрик DDU для всех или конкретной зоны управления за заданный период.

## Пулы DDU

С помощью пулов DDU можно задавать ежемесячные или ежегодные лимиты потребления DDU на уровне среды. По умолчанию лимиты пулов не применяются. Чтобы задать лимиты, перейдите в **Settings** > **Consumption** > **Davis data unit pools**.

![DDU pools](https://dt-cdn.net/images/davis-data-unit-pools-3356-11d216da22.png)

DDU pools

Доступны следующие пулы для ограничения потребления DDU:

* Metrics (Метрики)
* Log Monitoring (Мониторинг логов)
* Serverless (Бессерверные функции)
* Events (События)
* Traces (Трассировки)

Для доступа к странице **Davis data unit pools** необходимо разрешение **Manage monitoring settings** или учётная запись администратора.

Для каждого пула можно задать ежемесячный или ежегодный лимит суммарного потребления DDU. Аналогично [уведомлениям об объёме DDU](/managed/license/monitoring-consumption-classic/davis-data-units#davis-data-unit-volumes "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."), все пользователи среды увидят баннерные уведомления при достижении 90% и 100% лимита пула.

Лимиты пулов оцениваются по календарному месяцу/году и не привязаны к датам обновления лицензии.

## Часто задаваемые вопросы

Как это повлияет на мой аккаунт и среды?

Dynatrace автоматически выполнит миграцию вашей текущей лицензионной квоты. После завершения миграции вы получите уведомление и сможете начать использовать DDU.

Привязано ли потребление DDU к потреблению хост-единиц?

Нет, потребление DDU не привязано к потреблению хост-единиц. DDU используются для измерения потребления средой пользовательских метрик, строк логов, пользовательских событий и сторонних трассировок, а не мониторинга хостов.

Есть ли бесплатный уровень DDU для каждой среды?

Да, 200 000 DDU доступны для каждой среды (SaaS) или лицензии (Managed/Offline). То же верно для клиентов бесплатного пробного периода. Бесплатный уровень сбрасывается ежегодно (не применяется для клиентов Offline).

Есть ли различия между SaaS, Managed и Offline-развёртываниями?

Различий между Dynatrace SaaS и Dynatrace Managed нет. Для Offline-развёртываний ежегодный сброс DDU не выполняется.

Где можно отслеживать/мониторировать потребление DDU?

Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

Какое разрешение нужно для просмотра обзора потребления DDU?

Необходимо разрешение **Manage monitoring settings** или учётная запись администратора. Подробнее о разрешениях см. в [Управление группами пользователей и разрешениями](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Какое разрешение нужно для получения уведомлений о потреблении DDU?

Необходимо разрешение **Manage monitoring settings** или учётная запись администратора. Подробнее о разрешениях см. в [Управление группами пользователей и разрешениями](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Можно ли получить детали потребления DDU через API?

Да, детали потребления DDU можно получить через [Environment API v2](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

* `builtin:billing.ddu`
* `builtin:billing.ddu.metrics.byEntity`
* `builtin:billing.ddu.metrics.byMetric`

Можно ли заблокировать/отложить конвертацию DDU?

Нет, поскольку DDU предназначены для расчёта потребления пользовательских метрик, строк логов, пользовательских событий и т.д. Немедленная конвертация в DDU даёт более точную аналитику потребления.

Переносятся ли неиспользованные DDU на следующий период лицензии?

Нет. Квота DDU сбрасывается на каждую годовщину срока контракта — аналогично единицам DEM.

Потеряем ли мы какие-либо функции или гибкость?

Нет, с DDU вы получаете больше гибкости, прозрачности и других преимуществ.

Сколько DDU содержится в одном лицензионном объёме?

* Один объём содержит 1 миллион DDU и соответствует 1 903 метрикам (с частотой 1 раз в минуту).
* Если метрика имеет несколько измерений (например, загрузка пула по имени пула базы данных), каждое измерение генерирует 1 точку данных метрики в минуту и соответственно вычитает несколько DDU в минуту.

Каков минимальный объём для покупки?

Минимальный объём DDU — 1 (то есть 1 миллион DDU). Это соответствует 1 903 метрикам (с частотой 1 раз в минуту).

Можно ли включить превышения для DDU?

Да, превышения доступны для DDU.

Как будет работать миграция, если она происходит в середине срока?

Все оставшиеся пользовательские метрики в вашей лицензии будут конвертированы в DDU с учётом длительности оставшегося срока. Например, если вы находитесь на шестом месяце годового срока (то есть 50% истёкло и пользовательские метрики были потреблены), оставшиеся 50% пользовательских метрик будут конвертированы в эквивалентное количество DDU.

Можно ли разделить DDU между средами SaaS?

В будущем да. Однако сейчас это недоступно.

Получу ли я уведомление, когда квота DDU будет исчерпана?

Да, пользователи вашей среды Dynatrace увидят внутрипродуктовое уведомление при достижении `90%` и `100%` лицензированных DDU.

Есть ли поддержка предыдущей лицензии «не на хост-единицах»?

Нет, поддержка таких устаревших лицензий невозможна. Если вы всё ещё используете подобную лицензию, команда Dynatrace должна была уже связаться с вами. Если этого не произошло, пожалуйста, свяжитесь с нами для содействия в конвертации.

Что такое «мониторируемая сущность»?

Мониторируемая сущность — всё, что Dynatrace обнаруживает и мониторирует в вашей среде: хосты, сервисы, группы процессов, приложения и другое.

Что означает «Не связано с мониторируемой сущностью»?

Запись **Not related to a monitored entity** в столбце **Name** таблицы **Monitored entities** на странице **Davis data units overview** появляется из-за следующих источников потребления в зависимости от пула:

| Пул | Источники без сущностей |
| --- | --- |
| Metrics | См. [раздел Metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#no-monitored-entity "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") |
| Log | [Универсальный приём логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") |
| Serverless | Нет |
| Events | [Event API v2](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.") |
| Traces | Трассировки, где в конфигурации универсальной сущности отсутствует `span:service` или в данных спана нет атрибута ресурса `service.name`. |

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)