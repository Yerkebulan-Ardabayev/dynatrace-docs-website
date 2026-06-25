---
title: Заметки о выпуске Dynatrace Managed версии 1.304
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-304
scraped: 2026-05-12T11:07:53.370436
---

# Заметки о выпуске Dynatrace Managed версии 1.304

# Заметки о выпуске Dynatrace Managed версии 1.304

* Заметки о выпуске
* Updated on Dec 09, 2024

Начало развёртывания: Nov 11, 2024

## Несовместимые изменения

### Прекращение поддержки (EOL) AWS log forwarder

Как было объявлено ранее, [AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Use AWS log forwarding to ingest AWS logs.") Dynatrace является устаревшим.

Несовместимое изменение: прекращение поддержки Dynatrace AWS log forwarder запланировано на 31 декабря 2024 года. Этот момент приближается.

Если вы всё ещё используете устаревший AWS log forwarder, рекомендуется перейти на новый вариант до 31 декабря 2024 года.

### Блокировка обновлений и новых установок для операционных систем

Следующие операционные системы заблокированы:

* Red Hat Enterprise Linux (RHEL), Oracle Linux 8.6
* Red Hat Enterprise Linux (RHEL), Oracle Linux 8.9

Если вы используете одну из этих систем, необходимо обновить ОС перед применением данного обновления Dynatrace Managed.

## Новые функции и улучшения

### NAM targetFilter с поддержкой пользовательских устройств и экземпляров группы процессов

Digital Experience | Synthetic

NAM улучшен за счёт добавления поддержки пользовательских устройств и других параметров в `targetFilter`. Доступны новые фильтры:

* `type`
* `entityId`
* `processGroupInstance`
* `interfacesOf`
* `extensionName`
* `tags`

Примеры использования см. в разделе [Фильтр цели](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/configure-nam-managed#target-filter "Learn how to set up and manage a NAM monitor to check the performance and availability of your site.").

### Развёртывание Kubernetes: дополнительные области действия

Infrastructure Observability | Kubernetes

В дополнение к области действия `metrics.ingest` токен приёма данных теперь включает `logs.ingest` и `openTelemetryTrace.ingest`.

* На странице **Start monitoring your Kubernetes clusters**, в разделе **Install Dynatrace Operator**, опция **Data ingest token** > **Generate token** создаёт токен, включающий области действия:

  + `logs.ingest`
  + `metrics.ingest`
  + `openTelemetryTrace.ingest`
* Страница **Generate access token** теперь включает шаблон **Kubernetes: Data Ingest** с теми же областями действия.
* **Data ingest token**, создаваемый страницей развёртывания Kubernetes, теперь содержит те же области действия.

### Дашборд рабочего процесса тегирования (Dashboards Classic)

Рабочий процесс тегирования отвечает за назначение тегов, управленческих зон и имён сущностям на основе определённых правил. Теперь можно использовать новый предустановленный дашборд **Tagging worker** для Dashboards Classic, чтобы:

* Проверять время выполнения этого рабочего процесса с разбивкой по правилам тегирования, управленческих зон и именования.
* Просматривать наиболее медленные применённые правила в ходе работы рабочего процесса, что важно для масштабирования правил.

Подробнее о тегировании см. в разделе [Лучшие практики масштабирования правил тегирования и управленческих зон](/managed/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").

### Улучшение производительности CPU Cassandra в некоторых развёртываниях

Скорректированы параметры настройки Cassandra для устранения высокой нагрузки на CPU Cassandra в некоторых развёртываниях Dynatrace Managed.

### Новый источник атрибутов запроса для Group ID транзакций CICS

Application Observability | Distributed Traces

Добавлена поддержка источника атрибутов запроса Group ID транзакций CICS.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.303](/managed/whats-new/dynatrace-api/sprint-303 "Changelog for Dynatrace API version 1.303")
* [Журнал изменений Dynatrace API версии 1.304](/managed/whats-new/dynatrace-api/sprint-304 "Changelog for Dynatrace API version 1.304")

## Поддержка операционных систем

### Текущие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 December 2024

* Linux: Red Hat Enterprise Linux 8.6, 8.9, 9.0, 9.3

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
  + Последняя совместимая версия: 1.304
* Linux: Oracle Linux 8.6

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
  + Последняя совместимая версия: 1.304

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

## Исправленные ошибки

* [Общая доступность (сборка 1.304.85)](#managed-sprint-304-ga)
* [Обновление 87 (сборка 1.304.87)](#managed-sprint-304-87)
* [Обновление 114 (сборка 1.304.114)](#managed-sprint-304-114)

### Общая доступность (сборка 1.304.85)

Выпуск 1.304 GA содержит 4 исправленные ошибки.

| Компонент | Исправленные ошибки |
| --- | --- |
| [Cluster](#managed-sprint-304-ga-Cluster) | 1 |
| [Infrastructure Monitoring](#managed-sprint-304-ga-Infrastructure Monitoring) | 1 |
| [Service-Level Objectives](#managed-sprint-304-ga-Service-Level Objectives) | 1 |
| [Session Replay](#managed-sprint-304-ga-Session Replay) | 1 |

#### Cluster

* Устранена проблема, вызванная новыми настройками по умолчанию в Firewalld в Red Hat Enterprise Linux 9.5, которые блокировали правила брандмауэра Dynatrace. (MGD-1220)

#### Infrastructure Monitoring

* Добавлены новые параметры для снижения уровня проверки SSL-сертификатов для MySQL и PostgreSQL. (DAQ-2021)

#### Service-Level Objectives

* Устранена возможная ошибочная миграция SLO из Managed в SaaS-окружения при использовании SaaS Upgrade Assistant. (CA-13239)

#### Session Replay

* Исправлена ошибка в Session Replay, при которой элементы INPUT и TEXTAREA не маскировались, если их значения были заполнены по умолчанию. (SR-6411)

### Обновление 87 (сборка 1.304.87)

Это накопительное обновление содержит 19 исправленных ошибок и все ранее выпущенные обновления для выпуска 1.304.

| Компонент | Исправленные ошибки |
| --- | --- |
| [Cluster](#managed-sprint-304-87-Cluster) | 16 |
| [Infrastructure Monitoring](#managed-sprint-304-87-Infrastructure Monitoring) | 1 |
| [Service-Level Objectives](#managed-sprint-304-87-Service-Level Objectives) | 1 |
| [Session Replay](#managed-sprint-304-87-Session Replay) | 1 |

#### Cluster

* Устранена проблема, которая не позволяла приложениям со схемами настроек завершить установку в новых окружениях. (PS-28636)
* Формат времени последнего пульса OneAgent теперь корректен в веб-интерфейсе. (TI-14367)
* На унифицированной странице анализа больше не отображаются маркеры метрик для удалённых проблем. (DI-16748)
* Детекторы аномалий, созданные через Settings API и использующие параметры анализатора по умолчанию, теперь работают корректно. (DI-16920)
* Устранена проблема, при которой необязательный фильтр селектора метрик с условиями `or` учитывал только один тип условия на ключ метрики. (GRAIL-33751)
* Исправлена проблема, при которой HTTP-вызовы кластера в серверную часть лицензирования не работали при определённых конфигурациях брандмауэра/прокси. (LIMA-23301)
* Устранена проблема, при которой специфические для плиток временные диапазоны в дашбордах не включали часовой пояс, в котором они были заданы. Временной диапазон всегда интерпретировался как местное время, из-за чего пользователи в разных часовых поясах видели разные данные для одних и тех же плиток. (PAPA-20786)
* Кнопки «Create metric» и «Create processing rule» в приложении Logs & Events отключены, если фильтры в запросе слишком длинные. (LOG-8167)
* Исправлена проблема, которая могла приводить к увеличению нагрузки на CPU и память при запусках менеджера проблем, если управленческие зоны очень часто изменялись для сущностей событий. (DI-17430)
* Исправлена обработка данных span-датчиков для старых версий OneAgent. (APPOBS-2567)
* Data Explorer, предыдущий Dynatrace: исправлено значение сопоставителя столбцов для таблицы. (PAPA-21298)
* Количество поддерживаемых (обрабатываемых) событий на span ограничено до 128. (APPOBS-2454)
* Исправлены сбои подключений к AWS и Azure из-за проблем с сертификатами, вызванных отсутствием записи SNI в TLS-соединениях. (CLD-12351)
* В плитке дашборда «Runtime Application Protection (RAP)» / «Top RAP hosts» некорректная метрика `builtin:billing.runtime_vulnerability_analytics.usage_per_host` заменена на корректную `builtin:billing.runtime_application_protection.usage_per_host`. (LIMA-22028)
* Файл `dynakube.yaml` теперь использует последнюю версию API: `dynatrace.com/v1beta2`. (K8S-11176)
* Фильтры взаимосвязей на странице Services Classic теперь объединяют несколько значений с помощью логического оператора OR. (TI-14422)

#### Infrastructure Monitoring

* Добавлены новые параметры для снижения уровня проверки SSL-сертификатов для MySQL и PostgreSQL. (DAQ-2021)

#### Service-Level Objectives

* Устранена возможная ошибочная миграция SLO из Managed в SaaS-окружения при использовании SaaS Upgrade Assistant. (CA-13239)

#### Session Replay

* Исправлена ошибка в Session Replay, при которой элементы INPUT и TEXTAREA не маскировались, если их значения были заполнены по умолчанию. (SR-6411)

### Обновление 114 (сборка 1.304.114)

Это накопительное обновление содержит 1 исправленную ошибку и все ранее выпущенные обновления для выпуска 1.304.

#### Cluster

* Увеличены периоды снятия оповещений для проблем Davis, обнаруженных через определение аномалий Kubernetes, чтобы снизить частоту случаев, когда проблемы с одной первопричиной часто закрываются и открываются повторно. Оповещения «Container restarts» и «Out-of-memory kills» теперь снимаются через 15 минут. Все остальные оповещения с ранее установленным периодом снятия в 5 минут теперь снимаются через 10 минут. (INFOBS-903)