---
title: Что нового в Dynatrace Managed 1.334
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-334
scraped: 2026-05-12T11:07:40.093176
---

# Что нового в Dynatrace Managed 1.334

# Что нового в Dynatrace Managed 1.334

* Заметки о выпуске
* 4-min read
* Updated on Mar 09, 2026
* Rollout start on Mar 16, 2026

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.334. Содержимое:

* [Обновления функций](#updates): 6
* [Несовместимые изменения](#breaking): 1
* [Исправления и обслуживание](#fixes): 1

Platform | Dashboards

### Интуитивная функция масштабирования диаграмм дашборда

Добавлена возможность увеличения и уменьшения масштаба непосредственно на диаграммах. Для увеличения диаграммы:

1. Выберите желаемую начальную точку.
2. Продлите диапазон до желаемой конечной точки.

   После отпускания появится диалог подтверждения, отображающий интервал масштабирования.
3. Нажмите **Zoom in**.

Можно отменить действие и вернуться к предыдущему временному диапазону.

![Функция масштабирования дашборда](https://dt-cdn.net/images/dashboard-1616-9e090c3172.png)

Функция масштабирования дашборда

## Обновления функций

Platform

### Унифицированная подсветка синтаксиса для выражений

Подсветка синтаксиса выражений (в **Data explorer**, **Entity selector** и **Metric selector**) теперь унифицирована для обеспечения единого внешнего вида и улучшения читаемости.

![Селектор сущностей](https://dt-cdn.net/images/screenshot-2026-02-12-at-14-56-21-1932-d5730ef8f4.png)

Селектор сущностей

Application Observability | Log Analytics

### Обновлённые строки замены для встроенных правил маскировки

Введены новые строки замены для встроенных правил маскировки. Паттерны сопоставления не изменились. Во избежание проблем с обратной совместимостью предыдущие правила сохраняются и переименовываются с префиксом `[Outdated-Built-in]`. Предыдущие правила можно изменить или удалить в любое время.

Application Security | Vulnerabilities

### Сканирование уязвимостей библиотек и Kubernetes теперь использует фид уязвимостей Dynatrace

Сканирование уязвимостей библиотек и Kubernetes теперь основано на фиде уязвимостей Dynatrace. Это обновление обеспечивает более точные, прозрачные и учитывающие угрозы данные об уязвимостях при сохранении широкого охвата критических рисков. В рамках этого изменения небольшой процент ранее обнаруженных уязвимостей больше не будет охвачен и будет помечен как **Deprecated**. Их можно просмотреть с помощью фильтра **Status** > **Deprecated**.

Digital Experience | Synthetic

### Изменены разрешения в шаблоне Kubernetes для адаптера метрик Synthetic Monitoring

Шаблон Kubernetes для адаптера метрик Synthetic Monitoring обновлён: разрешения метрик Cluster Role установлены только на чтение.

Platform

### Страницы Kubernetes Workload и Pods теперь отображают все события

Страницы **Kubernetes Workload** и **Pods** теперь отображают все события, связанные с конкретной рабочей нагрузкой или подом, в карточке **Events**.

![Карточка событий](https://dt-cdn.net/images/events-card-1742-00eb8751d1.png)

Карточка событий

Platform

### Настройка сетевых зон через Settings API

Теперь можно настраивать сетевые зоны через фреймворк Settings API с новой схемой `builtin:networkzones.zones`. Используйте следующие конечные пункты для доступа к параметрам:

* Уровень окружения: `GET /api/v2/settings/schemas/builtin:networkzones.zones`
* Уровень кластера: `GET /api/cluster/v2/settings/schemas/builtin:networkzones.zones`

Подробнее см. в разделе [Settings API](/managed/manage/settings/settings-20 "Introduction to the Settings 2.0 framework").

Существующий [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.") остаётся без изменений и продолжает работать параллельно с новыми возможностями Settings API.

## Несовместимые изменения

Account Management | Cost Management

### Переход на новый конечный пункт уведомлений Account Management

Для получения единого потока доступных уведомлений (бюджет, прогноз и стоимость) перейдите на новый конечный пункт уведомлений `NotificationsController_listNotifications`. Новый конечный пункт может возвращать дополнительные типы уведомлений и незначительные отличия в схеме метаданных.

`SubscriptionsController_getEvents` объявлен устаревшим начиная с Dynatrace версии 1.333. Он продолжит работать до объявленной даты прекращения поддержки, но не будет возвращать дополнительные типы уведомлений, доступные через новый конечный пункт.

Сроки:

* Выпуск нового конечного пункта `NotificationsController_listNotifications`: Dynatrace версия 1.333
* Заголовки об устаревании запланированы на 23 февраля 2026 года. Ответы будут включать `deprecation: true` и `sunset: 2026-04-06`.
* Дата прекращения поддержки `SubscriptionsController_getEvents`: 6 апреля 2026 года.

## Исправления и обслуживание

### Исправленные ошибки в этом выпуске

* Исправлен граничный случай, при котором начало события (начало окна анализа) не входило в расписание окна обслуживания, но конец окна анализа входил в него. Это в основном влияло на события обнаружения аномалий на уровне сервиса или приложения, а также на пользовательские детекторы аномалий (метрические события). (DI-25641)

## Поддержка операционных систем

* Добавлена поддержка [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.7

### Предстоящие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы перестанут поддерживаться с 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление поставщика](https://www.suse.com/lifecycle/)

##### Следующие операционные системы перестанут поддерживаться с 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление поставщика](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы перестанут поддерживаться с 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление поставщика](https://aws.amazon.com/linux/)

### Прошедшие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы больше не поддерживаются с 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Объявление поставщика](https://wiki.debian.org/DebianReleases)

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.334](/managed/whats-new/dynatrace-api/sprint-334 "Changelog for Dynatrace API version 1.334")
* [Журнал изменений Dynatrace API версии 1.333](/managed/whats-new/dynatrace-api/sprint-333 "Changelog for Dynatrace API version 1.333")