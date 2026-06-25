---
title: Что нового в Dynatrace Managed версии 1.330
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-330
scraped: 2026-05-12T11:08:03.789275
---

# Что нового в Dynatrace Managed версии 1.330

# Что нового в Dynatrace Managed версии 1.330

* Заметки о выпуске
* Published Jan 09, 2026
* Rollout start on Jan 19, 2026

Новые версии развёртываются в рамках настраиваемых [окон обслуживания](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.").

|  | Начало развёртывания | Поддерживается в настоящее время |
| --- | --- | --- |
| [Версия 1.338](/managed/whats-new/managed/sprint-338 "New features, changes, and resolved issues in Dynatrace Managed 1.338") | May 11, 2026 | Да |
| [Версия 1.336](/managed/whats-new/managed/sprint-336 "New features, changes, and resolved issues in Dynatrace Managed 1.336") | Apr 13, 2026 | Да |
| [Версия 1.334](/managed/whats-new/managed/sprint-334 "New features, changes, and resolved issues in Dynatrace Managed 1.334") | Mar 16, 2026 | Да |
| [Версия 1.332](/managed/whats-new/managed/sprint-332 "Release notes for Dynatrace Managed, version 1.332") | Feb 16, 2026 | Только с [Enterprise Success and Support](https://dt-url.net/qt03zwg) |

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.330. Содержимое:

* [Обновления функций](#updates): 8
* [Несовместимые изменения](#breaking): 3
* [Исправления и обслуживание](#fixes): 5

## Обновления функций

Account Management

### Мониторинг использования лицензии кластера

Добавлен дашборд в локальное окружение самомониторинга кластера, позволяющий отслеживать использование лицензии для единиц хоста, единиц данных Davis (DD) и единиц мониторинга цифрового опыта (DEM) при классическом лицензировании.

Также добавлены специальные метрики тарификации для каждой единицы лицензии, что позволяет настраивать оповещения о лицензионных событиях (например, когда единицы заканчиваются) с помощью метрических событий. Подробнее о метриках тарификации и настройке лицензионных событий см. в разделе [Классическое лицензирование Dynatrace](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

![Дашборд использования лицензии кластера](https://dt-cdn.net/images/managed330-cluster-license-usage-2335-1d3ae4be6a.png)

Дашборд использования лицензии кластера

Application Observability | Distributed Tracing

### Настройка и переопределение маскировки OneAgent на уровне группы хостов

[Маскировка OneAgent](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") может маскировать данные при первом контакте до их выхода из отслеживаемого процесса. Чтобы обеспечить возможность настройки в многокомандных и многодепартаментных средах, добавлена возможность задавать и переопределять маскировку на уровне группы хостов в дополнение к уже существующим уровням: окружения, кластера/пространства имён Kubernetes и группы процессов. Это особенно удобно при управлении сотнями приложений.

Platform

### Интуитивная функция масштабирования диаграмм Data Explorer

Добавлена возможность увеличения и уменьшения масштаба непосредственно на диаграммах в Data Explorer. Для увеличения диаграммы выберите желаемую начальную точку, удерживайте кнопку мыши и перетащите до желаемой конечной точки. Отпустите кнопку мыши — появится диалог подтверждения интервала масштабирования.

После увеличения можно использовать кнопку возврата для возврата к предыдущему временному диапазону.

![Функция масштабирования диаграмм Data Explorer](https://dt-cdn.net/images/screenshot-2026-01-16-at-15-20-42-1617-0a636a5632.png)

Функция масштабирования диаграмм Data Explorer

Platform

### Улучшена точность мониторинга лимита измерений для метрик

Использование пользовательских метрик с постоянным потоком новых значений измерений (например, UID подов Kubernetes) могло отображать некорректные паттерны в самомониторинге: внезапные увеличения с последующими спадами.

С этим обновлением лимиты измерений вычисляются точно, обеспечивая более чёткое и надёжное представление об использовании метрик.

Platform

### Подсказки для селекторов сущностей в Settings

Автоматически применяемые теги, управленческие зоны и определения SLO теперь поддерживают подсказки для селекторов сущностей. Вместо ручного ввода селекторов сущностей можно использовать функцию автодополнения, которая предлагает доступные фильтры, операторы и значения.

![Подсказки для селекторов сущностей](https://dt-cdn.net/images/auto-complete-1337-525ba3065b.png)

Подсказки для селекторов сущностей

Platform

### Новый конечный пункт Metrics API v2 для удаления устаревших метрик

[Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") теперь включает новый конечный пункт, позволяющий удалять метрики, которые не записывались в течение заданного количества дней:

* Используйте `DELETE /api/v2/metrics` для удаления ingested-метрик.
* Используйте параметр `metricSelector` для выбора конкретных метрик.
* Используйте символ подстановки для удаления метрик с определённым префиксом или всех метрик, указав `*`.
* Используйте параметр `minUnusedDays` для определения минимального количества дней бездействия метрики перед удалением.

Пример: Для удаления всех метрик, не записывавшихся последние 60 дней:

`DELETE /api/v2/metrics?metricSelector=<your-selector>&minUnusedDays=60`

Platform | OneAgent

### Проверка совместимости версий OneAgent

[OneAgent Health](/managed/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems.") теперь отображает минимальную и максимальную совместимые версии OneAgent с данным кластером Managed. Кроме того, выдаётся предупреждение, если версия OneAgent слишком низкая или слишком высокая, что позволяет оперативно подключить OneAgent совместимой версии.

## Несовместимые изменения

Infrastructure Observability | Extensions

### Конечные пункты, связанные с событиями, удалены из Extensions Environment API v2

Следующие устаревшие конечные пункты удалены из Environment API v2:

* `/extensions/{extensionName}/environmentConfiguration/events`
* `/extensions/{extensionName}/monitoringConfigurations/{configurationId}/events`

Platform

### Встроенный онлайн-чат заменён внешней ссылкой

Встроенный онлайн-чат заменён внешней ссылкой на [Dynatrace Support Center](https://support.dynatrace.com). В Dynatrace Support Center вы можете в любое время обратиться к специалистам по продукту с вопросами о Dynatrace.

Platform

### Метрика fileDescriptorsPercentUsed больше не разбивается по PID

По соображениям производительности измерение PID удалено из метрики fileDescriptorsPercentUsed. Это означает, что метрику больше нельзя разбивать по PID.

Ключ метрики: `builtin:tech.generic.handles.fileDescriptorsPercentUsed`

## Исправления и обслуживание

### Исправленные ошибки в этом выпуске

* В случае [классического мониторинга логов K8s](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes.") модули мониторинга логов не входят в лицензию на единицы хоста и не тарифицируются. Однако они ошибочно включались в проверку квоты единиц хоста, что могло приводить к вводящей в заблуждение информации об использовании квоты. Поэтому модули мониторинга логов исключены из проверки квоты единиц хоста. (MGD-8983)
* Исправлены пакеты установщика, которые некорректно синхронизировались между узлами при наличии файла сценария без семантической версии в имени в папке установщика сервера Dynatrace Managed. (MGD-8354)
* Исправлена проблема с развёртываниями только для приложений, при которой несколько кодовых модулей могли перезаписывать версию OneAgent друг друга на одном хосте. (MGD-6868)
* Надёжный автовход в браузерный монитор: исправлена ошибка в шаге JavaScript автоматического входа, предотвращающая сбои при отказе монитора, что обеспечивает более стабильный мониторинг. (DEM-18430)
* Согласованная обработка конечных пунктов с пробелами: span обнаружения сервисов v2 теперь обрабатывают конечные пункты, состоящие только из пробелов, так же как пустые конечные пункты, — без назначения `endpoint.name`. Это обеспечивает согласованное поведение span без влияния на генерацию метрик. (APPOBS-30130)

### Исправленные ошибки (обновление 1.330.29.20251229-0916101)

* Исправлена проблема с модулем проверки работоспособности NGINX, отвечающим за перенаправление трафика между узлами кластера. (MGD-9000)

## Поддержка операционных систем

* Добавлена поддержка [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 10.1

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

* [Журнал изменений Dynatrace API версии 1.330](/managed/whats-new/dynatrace-api/sprint-330 "Changelog for Dynatrace API version 1.330")
* [Журнал изменений Dynatrace API версии 1.329](/managed/whats-new/dynatrace-api/sprint-329 "Changelog for Dynatrace API version 1.329")