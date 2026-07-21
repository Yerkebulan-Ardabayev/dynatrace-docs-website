---
title: Расширение Dynatrace (Davis data units)
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units
---

# Расширение Dynatrace (Davis data units)

# Расширение Dynatrace (Davis data units)

* 8 минут на чтение
* Опубликовано 30 марта 2020

Davis data units (DDU), это простой способ лицензирования отдельных возможностей (custom metrics, log monitoring и custom events) на платформе Dynatrace. DDU можно считать своего рода валютой Dynatrace. Так же, как расход лицензии для Dynatrace RUM и Synthetic Monitoring рассчитывается на основе [Digital Experience Monitoring (DEM) units](/managed/license/classic-licensing/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), DDU обеспечивают единую, общую модель потребления для custom metrics, Log Monitoring и custom events.

Поскольку DDU основаны на потреблении, приобретается определённый объём, а доступная квота расходуется со временем в зависимости от того, сколько мониторинга потребляет среда. Такой подход к лицензированию значительно упрощает контроль и отслеживание расхода метрик (например, в случае неправильно настроенных метрик) и помогает определить главных потребителей в среде. Подробнее о том, как метрики лицензируются с помощью DDU, см. в разделе [Расчёт стоимости метрик](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

Полную информацию о том, как рассчитывается расход мониторинга Dynatrace, см. в разделе [Расчёт расхода мониторинга Dynatrace](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.").

## Объёмы Davis data units

DDU приобретаются объёмами по 1 миллиону единиц на основе контрактов сроком на 1-3 года, при этом полный объём лицензированных единиц обновляется в начале каждого года. Например, если приобрести 100 миллионов DDU на срок 3 года, можно расходовать 100 миллионов DDU ежегодно в течение 3 лет.

Дополнительные DDU можно приобрести в любой момент, если объём заканчивается. За подробностями нужно обратиться к торговому представителю Dynatrace. Чтобы помочь скорректировать расход мониторинга и избежать перерасхода, пользователям среды Dynatrace показываются уведомления в продукте, когда израсходовано `90%` и `100%` лицензированных DDU.

### Davis data units, бесплатный уровень

Каждая новая среда Dynatrace SaaS и каждая лицензия Dynatrace Managed получают бесплатно 200 000 DDU. Это соответствует 381 метрике, собираемой с частотой 1 минута. Этот бесплатный уровень позволяет опробовать функции и оценить ценность мониторинга Dynatrace до оплаты. Бесплатный уровень в 200 000 DDU автоматически обновляется ежегодно в начале каждого нового срока лицензии для каждого аккаунта. Эта льгота недоступна для оффлайн-аккаунтов и аккаунтов с оплатой по факту потребления (pay-as-you-go).

## Просмотр деталей расхода DDU по средам

Для доступа к этой странице нужно разрешение **Manage monitoring settings** или учётная запись администратора. Подробности см. в разделе [Разрешения управления аккаунтом](/managed/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management").

Чтобы увидеть, сколько DDU израсходовала среда, нужно перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**. Там можно просмотреть расход DDU и определить главных потребителей DDU.

Эта страница даёт обзор расхода DDU по пулам, а также детальное представление по каждому отслеживаемому объекту (хост, служба, группа процессов, приложение и другие). Навигация второго уровня позволяет углубиться в детальный расход по каждому пулу DDU (например, Metrics, Log Monitoring, Events).

### Получение деталей расхода DDU через API

Также можно [получить детали расхода DDU через API](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API."). Через API для получения деталей расхода DDU по каждому пулу доступны следующие метрики:

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

### Получение расхода DDU по management zone

Упомянутые выше метрики напрямую не поддерживают фильтрацию по management zone, однако для этого можно использовать API и таким образом решить задачи распределения затрат между подразделениями, а также создать отчёт о расходе отслеживаемых объектов с разбивкой по management zone.

Пример скрипта отчётности по management zone см. в [репозитории сниппетов Dynatrace на GitHub﻿](https://github.com/Dynatrace/snippets/tree/master/api/ddu/management-zone-calculation)
Скрипт обращается к метрике `builtin:billing.ddu.metrics.byEntity` и позволяет запрашивать расход пула Metrics DDU для всех или для одной конкретной management zone за заданный период времени.

## Пулы DDU

С помощью пулов DDU можно задавать месячные или годовые лимиты расхода DDU в рамках отдельной среды. По умолчанию лимиты пулов не применяются. Чтобы задать лимиты расхода DDU, нужно перейти в **Settings** > **Consumption** > **Davis data unit pools**

![DDU pools](https://dt-cdn.net/images/davis-data-unit-pools-3356-11d216da22.png)

Пулы DDU

Для ограничения расхода DDU доступны следующие пулы:

* Metrics
* Log Monitoring
* Serverless
* Events
* Traces

Для доступа к странице **Davis data unit pools** нужно разрешение **Manage monitoring settings** или учётная запись администратора.

Для каждого пула можно задать месячный или годовой лимит общего расхода DDU. Как и в случае с [уведомлениями об объёме DDU](/managed/license/classic-licensing/davis-data-units#davis-data-unit-volumes "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."), все пользователи среды увидят баннерные уведомления при расходе 90% и 100% лимита пула.

Лимиты пулов оцениваются по календарным месяцам/годам и не привязаны к датам продления лицензии.

## Часто задаваемые вопросы

Как это повлияет на мою учётную запись и окружения?

Dynatrace автоматически запустит миграцию существующей лицензионной квоты. После завершения миграции придёт уведомление, и можно будет начать использовать подход DDU.

Привязаны ли квоты DDU к потреблению host units?

Нет, потребление DDU не привязано к потреблению host units. DDU используются для измерения потребления окружением custom metrics, log lines, custom events и third-party traces, а не мониторинга хостов.

Доступен ли бесплатный уровень DDU для каждого окружения?

Да, для каждого окружения (SaaS) или лицензии (Managed/Offline) доступно 200 000 DDU. То же самое верно и для клиентов на бесплатном пробном периоде. Бесплатный уровень сбрасывается ежегодно (для клиентов Offline это не так).

Есть ли разница между развёртываниями SaaS, Managed и Offline?

Разницы между развёртываниями Dynatrace SaaS и Dynatrace Managed нет. В развёртываниях Offline ежегодного сброса DDU не происходит.

Где можно отслеживать/контролировать потребление DDU?

Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

Какое разрешение нужно, чтобы видеть обзор потребления DDU?

Для доступа к странице **DDU consumption overview** нужно разрешение **Manage monitoring settings** или учётная запись администратора. Подробнее о разрешениях см. [Manager user groups and permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Какое разрешение нужно, чтобы видеть уведомления о потреблении DDU?

Для получения уведомлений о потреблении DDU нужно разрешение **Manage monitoring settings** или учётная запись администратора. Подробнее о разрешениях см. [Manager user groups and permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Можно ли получить сведения о потреблении DDU через API?

Да, сведения о потреблении DDU можно получить через [Environment API v2](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

* `builtin:billing.ddu`
* `builtin:billing.ddu.metrics.byEntity`
* `builtin:billing.ddu.metrics.byMetric`

Можно ли как-то заблокировать/отложить конвертацию в DDU?

Нет, поскольку DDU предназначены для расчёта потребления мониторинга custom metrics, log lines, custom events и т. д. Немедленная конвертация в DDU даёт более точное представление о потреблении.

Переносятся ли неиспользованные DDU на следующий срок действия лицензии?

Нет. Квота DDU сбрасывается в каждую годовщину срока действия договора, так же как это происходит с единицами DEM.

Потеряем ли мы какой-либо функционал или гибкость?

Нет, с DDU появится больше гибкости, прозрачности и других преимуществ.

Сколько DDU входит в лицензионный объём?

* Один объём содержит 1 миллион DDU, что соответствует 1903 метрикам (с частотой 1 минута).
* Если у метрики несколько измерений (например, использование пула в разрезе имени пула базы данных), то каждое измерение производит по 1 точке данных метрики в минуту и, соответственно, расходует несколько DDU в минуту.

Каков минимальный объём для покупки?

Минимальное количество объёмов DDU, которое можно приобрести, равно 1 (то есть 1 миллион DDU). Это соответствует 1903 метрикам (с частотой 1 минута).

Можно ли включить overages для DDU?

Да, overages для DDU доступны.

Как будет проходить миграция, если она приходится на середину срока действия договора?

Все оставшиеся в лицензии custom metrics будут конвертированы в DDU. При этом учитывается длительность срока действия договора. Например, если прошло шесть месяцев из годового срока (то есть израсходовано 50% срока и 50% custom metrics), оставшиеся 50% custom metrics будут конвертированы в эквивалентное количество DDU.

Можно ли распределять DDU между окружениями SaaS?

В будущем, да. Однако сейчас это недоступно.

Придёт ли уведомление, когда квота DDU будет исчерпана?

Да, пользователи окружения Dynatrace увидят уведомление внутри продукта при достижении `90%` и `100%` лицензированных DDU.

Поддерживается ли предыдущая лицензия «non-host unit»?

Нет, такие старые лицензии больше не поддерживаются. Если используется одна из таких лицензий, команда Dynatrace должна была уже связаться по этому поводу. Если этого не произошло, нужно обратиться к нам, чтобы получить помощь с конвертацией.

Что такое «monitored entity»?

Monitored entity, это всё, что Dynatrace обнаруживает и отслеживает в окружении. Сюда входят хосты, службы, группы процессов, приложения и другое.

Что означает «Not related to a monitored entity»?

Обзор **Davis data units overview** иногда отображает запись **Not related to a monitored entity** в столбце **Name** таблицы **Monitored entities**.

В зависимости от пула, вот потенциальные источники потребления, учитываемые по записи **Not related to a monitored entity**:

| Pool | Источники без привязки к сущности |
| --- | --- |
| Metrics | См. [раздел Metrics](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation#no-monitored-entity "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") |
| Log | [Generic log ingestion](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") |
| Serverless | Нет |
| Events | [Event API v2](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.") |
| Traces | Traces, у которых в конфигурации generic entity отсутствует `span:service` или в данных span нет ресурсного атрибута `service.name`. |

Можно ли разделить потребление по подписке Azure?

Для потребления, связанного с monitored entity, где существует связь `entitySelector`, использовать запрос [Metrics API](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."):

```
builtin:billing.ddu.metrics.byEntity:filter(



and(in("dt.entity.monitored_entity",



entitySelector("type(AZURE_STORAGE_ACCOUNT), fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),



entityName.startsWith(~"myPrefix~"))"))



)



)



:splitBy():fold
```

## Related topics

* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)