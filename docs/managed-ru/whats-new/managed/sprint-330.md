---
title: Что нового в Dynatrace Managed версии 1.330
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-330
---

# Что нового в Dynatrace Managed версии 1.330

# Что нового в Dynatrace Managed версии 1.330

* Примечания к выпуску
* Опубликовано 09 января 2026
* Начало развёртывания 19 января 2026

Новые версии развёртываются в настраиваемых [окнах обслуживания](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.").

|  | Начало развёртывания | Поддерживается в настоящее время |
| --- | --- | --- |
| [Версия 1.342](/managed/whats-new/managed/sprint-342 "New features, changes, and resolved issues in Dynatrace Managed 1.342") | 18 июня 2026 | Да |
| [Версия 1.340](/managed/whats-new/managed/sprint-340 "New features, changes, and resolved issues in Dynatrace Managed 1.340") | 08 июня 2026 | Да |
| [Версия 1.338](/managed/whats-new/managed/sprint-338 "New features, changes, and resolved issues in Dynatrace Managed 1.338") | 11 мая 2026 | Да |
| [Версия 1.336](/managed/whats-new/managed/sprint-336 "New features, changes, and resolved issues in Dynatrace Managed 1.336") | 13 апреля 2026 | Только с [Enterprise Success and Support﻿](https://dt-url.net/qt03zwg) |

Эта страница описывает новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.330. Она содержит:

* [Обновления функций](#updates): 8
* [Критические изменения](#breaking): 3
* [Исправления и обслуживание](#fixes): 5

## Обновления функций

Account Management

### Отслеживание использования лицензии кластера

В локальную среду самомониторинга кластера добавлена панель, позволяющая отслеживать использование лицензии по host units, Davis data units (DD) и Digital Experience Monitoring (DEM) units при классическом лицензировании.

Также добавлены отдельные метрики биллинга для каждой единицы лицензии, что позволяет настраивать оповещения о событиях лицензии (например, когда единицы вот-вот закончатся) с помощью metric events. Подробнее о метриках биллинга и о том, как определять события лицензии, см. [классическое лицензирование Dynatrace](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.").

![Cluster license usage dashboard](https://dt-cdn.net/images/managed330-cluster-license-usage-2335-1d3ae4be6a.png)

Панель использования лицензии кластера

Application Observability | Distributed Tracing

### Настройка и переопределение маскирования OneAgent на уровне host group

[Маскирование OneAgent](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") позволяет маскировать данные при первом контакте, ещё до того как они покинут отслеживаемый процесс. Чтобы упростить настройку в средах с несколькими командами и отделами, теперь можно задавать и переопределять маскирование на уровне host group, в дополнение к уже существующим уровням environment, Kubernetes cluster/namespace и process group. Это особенно удобно при управлении сотнями приложений.

Platform

### Интуитивно понятный зум для графиков Data Explorer

Добавлена возможность увеличивать и уменьшать масштаб прямо на графиках в Data Explorer. Чтобы увеличить участок графика, нужно выбрать нужную начальную точку, удерживать кнопку мыши и потянуть до нужной конечной точки. После отпускания кнопки мыши появится диалог подтверждения интервала масштабирования.

После увеличения масштаба можно воспользоваться кнопкой отмены, чтобы вернуться к предыдущему периоду времени.

![Zoom functionality on Data Explorer charts](https://dt-cdn.net/images/screenshot-2026-01-16-at-15-20-42-1617-0a636a5632.png)

Функция масштабирования на графиках Data Explorer

Platform

### Повышенная точность контроля лимита измерений для метрик

Использование пользовательских метрик с постоянным потоком новых значений измерений (например, Kubernetes pod UID) могло приводить к некорректным паттернам в самомониторинге, включая резкие всплески с последующими падениями.

С этим обновлением лимиты измерений теперь рассчитываются точно, что даёт более ясное и надёжное представление об использовании метрик.

Platform

### Подсказки для entity selector в Settings

Автоматически применяемые теги, management zones и определения SLO теперь поддерживают подсказки для entity selector. Вместо того чтобы вручную набирать entity selector, можно использовать эту функцию автозаполнения, которая предлагает доступные фильтры, операторы и значения.

![entity selector suggestions](https://dt-cdn.net/images/auto-complete-1337-525ba3065b.png)

подсказки entity selector

Platform

### Новый эндпоинт Metrics API v2 для удаления устаревших метрик

[Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") теперь включает новый эндпоинт, позволяющий удалять метрики, которые не записывались указанное число дней. Вот что можно сделать:

* Использовать `DELETE /api/v2/metrics` для удаления полученных метрик.
* Использовать параметр `metricSelector`, чтобы выбрать конкретные метрики.
* Использовать подстановочные знаки для удаления метрик с определённым префиксом или всех метрик через `*`.
* Использовать параметр `minUnusedDays`, чтобы задать, сколько дней метрика должна быть неиспользуемой перед удалением.

Пример: чтобы удалить все метрики, не записывавшиеся последние 60 дней:

`DELETE /api/v2/metrics?metricSelector=<your-selector>&minUnusedDays=60`

Platform | OneAgent

### Проверка совместимости версий OneAgent

[OneAgent Health](/managed/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems.") теперь показывает минимальную и максимальную версии OneAgent, совместимые с этим Managed кластером. Кроме того, выдаётся предупреждение, если версия OneAgent слишком низкая или слишком высокая, что позволяет быстро отреагировать и подключить OneAgent совместимой версии.

## Критические изменения

Infrastructure Observability | Extensions

### Эндпоинты, связанные с событиями, удалены из Extensions Environment API v2

Из Environment API v2 удалены следующие устаревшие эндпоинты:

* `/extensions/{extensionName}/environmentConfiguration/events`
* `/extensions/{extensionName}/monitoringConfigurations/{configurationId}/events`.

Platform

### Встроенный чат заменён внешней ссылкой

Встроенный чат в продукте заменён внешней ссылкой на [Dynatrace Support Center﻿](https://support.dynatrace.com). В Dynatrace Support Center можно в любое время связаться с нашими специалистами по продукту по вопросам, связанным с Dynatrace.

Platform

### Метрика fileDescriptorsPercentUsed больше не разбивается по PID

По соображениям производительности измерение PID удалено из метрики fileDescriptorsPercentUsed. Это означает, что метрику больше нельзя разбивать по PID.

Ключ метрики: `builtin:tech.generic.handles.fileDescriptorsPercentUsed`

## Исправления и обслуживание

### Исправленные проблемы в этом релизе

* В случае [классического мониторинга логов K8s](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes.") модули мониторинга логов не входят в лицензию host units и не тарифицируются. Однако они некорректно учитывались при проверке квоты host unit, что могло приводить к недостоверной информации об использовании квоты. Поэтому модули мониторинга логов исключены из проверки квоты host unit (MGD-8983)
* Исправлены пакеты установщика, которые некорректно синхронизировались между узлами, если в папке установщика сервера Dynatrace Managed присутствовал файл скрипта без семантической версии в имени файла. (MGD-8354)
* Устранена проблема с развёртываниями application-only, при которой несколько кодовых модулей могли перезаписывать версию OneAgent друг друга на одном хосте. (MGD-6868)
* Надёжный автовход в браузерный монитор: исправлена ошибка в шаге JavaScript браузерного монитора с автовходом, из-за которой происходил сбой при отказе монитора, для более плавного мониторинга. (DEM-18430)
* Согласованная обработка эндпоинтов с пробелами: спаны service detection v2 теперь обрабатывают эндпоинты, состоящие только из пробельных символов, так же как пустые эндпоинты, в результате чего `endpoint.name` не назначается. Это обновление обеспечивает согласованное поведение спанов без влияния на генерацию метрик. (APPOBS-30130)

### Исправленные проблемы (обновление 1.330.29.20251229-0916101)

* Исправлена проблема с модулем проверки состояния NGINX, отвечающим за перенаправление трафика между узлами кластера. (MGD-9000)

## Поддержка операционных систем

* Добавлена поддержка [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 10.1

### Будущие изменения в поддержке операционных систем Dynatrace Managed

##### Следующие операционные системы больше не будут поддерживаться начиная с 01 ноября 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление вендора﻿](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление вендора﻿](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы больше не будут поддерживаться начиная с 01 января 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление вендора﻿](https://aws.amazon.com/linux/)

### Прошлые Dynatrace Managed изменения поддержки операционных систем

##### Следующие операционные системы больше не поддерживаются с 01 декабря 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление производителя﻿](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление производителя﻿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление производителя﻿](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 января 2026

* Linux: Debian 10

  + x86-64
  + [Объявление производителя﻿](https://wiki.debian.org/DebianReleases)

##### Следующие операционные системы больше не поддерживаются с 01 июня 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление производителя﻿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление производителя﻿](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 июля 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление производителя﻿](https://www.suse.com/lifecycle/)

## Dynatrace API

Об изменениях в Dynatrace API в этом релизе можно узнать здесь:

* [Список изменений Dynatrace API версии 1.330](/managed/whats-new/dynatrace-api/sprint-330 "Список изменений для Dynatrace API версии 1.330")
* [Список изменений Dynatrace API версии 1.329](/managed/whats-new/dynatrace-api/sprint-329 "Список изменений для Dynatrace API версии 1.329")