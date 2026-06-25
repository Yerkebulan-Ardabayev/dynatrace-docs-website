---
title: Заметки о выпуске Dynatrace Managed версии 1.306
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-306
scraped: 2026-05-12T11:07:45.555091
---

# Заметки о выпуске Dynatrace Managed версии 1.306

# Заметки о выпуске Dynatrace Managed версии 1.306

* Заметки о выпуске
* Updated on Apr 30, 2025

Начало развёртывания: Jan 20, 2025

## Несовместимые изменения

### Прекращение поддержки (EOL) AWS log forwarder

Как было объявлено ранее, [AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Use AWS log forwarding to ingest AWS logs.") Dynatrace является устаревшим.

Несовместимое изменение: поддержка Dynatrace AWS log forwarder прекращена 31 декабря 2024 года.

Если вы всё ещё используете устаревший AWS log forwarder, рекомендуется перейти на новый вариант.

### Ключи пользовательских атрибутов в Logs Classic теперь чувствительны к регистру

Несовместимое изменение

Данный выпуск завершает переходный период для изменений чувствительности к регистру пользовательских атрибутов.

Начиная с данного выпуска (Dynatrace Managed версии 1.306):

* Пользовательские атрибуты допускают символы верхнего регистра.
* Атрибуты обрабатываемых событий лога строго сопоставляются с определениями атрибутов (включая верхний или нижний регистр).

Ключи пользовательских атрибутов должны быть уникальны с учётом регистра, что означает, что пользовательские атрибуты, отличающиеся только регистром букв, больше не считаются одинаковыми атрибутами. Например, теперь можно определить два разных пользовательских атрибута с именами **MyAttribute** и **myattribute**.

Поиск становится чувствительным к регистру (кроме атрибутов только для фильтрации). Например, если вы определили пользовательский атрибут `MyAttribute`, то поиск `MyAttribute="SEARCH"` вернёт события лога с этим конкретным атрибутом, установленным в значение `SEARCH`, а `myattribute="SEARCH"` — нет.

Значения запросов по-прежнему нечувствительны к регистру. Например, `MyAttribute="SEARCH"` эквивалентно `MyAttribute="search"`.

## Новые функции и улучшения

### Дополнительные атрибуты для правил «Request naming»

Application Observability | Distributed Traces

Любой атрибут, перечисленный в классическом представлении трасс, на вкладке **Summary**, в разделе **OneAgent attributes**, можно использовать для пользовательских имён запросов.

### Лимит для сложных фильтров событий в профилях оповещения

Platform | Problems

Введён новый лимит по умолчанию в 1 000 уникальных сложных фильтров по заголовку/описанию событий, суммарно по всем профилям оповещения.

Фильтр по заголовку/описанию события считается сложным, если он использует оператор `contains` с отключённой чувствительностью к регистру или оператор `contains regex`.

Профиль оповещения, содержащий только один уникальный сложный фильтр по заголовку/описанию события, не учитывается в максимальном лимите.

### Минимизированы перезапуски мониторинга Kubernetes

Infrastructure Observability | Kubernetes

Перезапуски мониторинга Kubernetes минимизированы при обновлении настроек Kubernetes без фактического изменения содержимого.

### Удалён переключатель «Monitor persistent volume claims» в настройках Kubernetes

Infrastructure Observability | Kubernetes

Переключатель **Monitor persistent volume claims** удалён, так как метрики постоянных томов теперь по умолчанию принимаются как встроенные метрики. Подробнее см. в [Introducing built-in Persistent Volume Claim Monitoring for Kubernetes](https://community.dynatrace.com/t5/Dynatrace-tips/Introducing-built-in-Persistent-Volume-Claim-Monitoring-for/td-p/244902).

### Новые атрибуты в журналах событий Windows

Infrastructure Observability | Log Analytics

Добавлены два новых атрибута — `User name` и `Keywords` — из журналов событий Windows: в Log Viewer и в качестве сопоставителей в конфигурации приёма данных.

### Унифицированы описания метрик Infrastructure

Infrastructure Observability | Hosts

Описания метрик Infrastructure на странице браузера метрик и в Metric selector в последнем Dynatrace унифицированы.

### Расширен список разрешённых атрибутов по умолчанию для приёма метрик OTLP (OpenTelemetry Protocol)

Metrics Ingestion Protocol

В приёме метрик OTLP (OpenTelemetry Protocol) расширен список разрешённых атрибутов ресурсов и областей видимости для передачи в качестве измерений метрик.

Добавлены несколько атрибутов в пространствах имён `k8s.*` и `dt.*`, а также `service.instance.id`.

Если новые атрибуты нежелательны, отдельные переключатели можно отключить в **Settings** > **Metrics** > **OpenTelemetry metrics** > **Allow list: resource and scope attributes** (или соответствующую запись можно полностью удалить).

### Новый параметр приложения для анонимизации пользовательских сессий

[Anonymization API — PUT anonymization job](/managed/dynatrace-api/environment-api/anonymization/put-job "Start anonymization job to remove user data via Dynatrace API.") поддерживает анонимизацию пользовательских сессий на основе внутреннего идентификатора приложения через параметр `requestId` (или `clusterRequestIds` для кластеров Premium High-Availability).

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.305](/managed/whats-new/dynatrace-api/sprint-305 "Changelog for Dynatrace API version 1.305")
* [Журнал изменений Dynatrace API версии 1.306](/managed/whats-new/dynatrace-api/sprint-306 "Changelog for Dynatrace API version 1.306")

## Поддержка операционных систем

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