---
title: Использование journald для приёма журналов systemd journal с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/journald
---

# Использование journald для приёма журналов systemd journal с помощью OTel Collector

# Использование journald для приёма журналов systemd journal с помощью OTel Collector

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 12 марта 2026 г.

Приёмник journald читает записи журнала из [systemd journal﻿](https://wiki.archlinux.org/title/Systemd/Journal), запуская `journalctl` как подпроцесс и передавая его вывод потоком в конвейер OTel Collector.

Каждая запись журнала становится записью журнала OTLP, где поля journal сопоставляются с атрибутами журнала.
Для переименования или преобразования этих атрибутов в соответствии с семантическими соглашениями OpenTelemetry можно использовать [операторы](#operators).

Приёмник journald стоит использовать, если:

* Сервисы на базе Linux записывают журналы в systemd journal, а не в отдельные файлы журналов.
* Нужно централизовать журналы системных сервисов уровня хоста (например, `ssh`, `kubelet` или `docker`) в Dynatrace без управления дополнительными путями к файлам журналов.
* Нужно фильтровать приём по конкретным модулям (units) systemd и уровням приоритета для контроля объёма данных.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [приёмником journald﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver).

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#collector-distro "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), на которую нужно экспортировать данные.

* ОС Linux на хосте или в контейнере, где выполняется Collector.
* Бинарный файл `journalctl` должен присутствовать на хосте или в контейнере, где выполняется Collector.
  Это необходимо, поскольку приёмник полагается на `journalctl` для всего доступа к journal.

  + Для развёртываний в контейнерах используй образ, включающий `systemd`, и монтируй каталог journal с хоста.
  + Требования, специфичные для Kubernetes, см. в разделе [Развёртывание в Kubernetes](#kubernetes-deployment).
* Процесс Collector должен иметь права на чтение systemd journal через `journalctl`.

  + На хосте с ОС Linux добавь пользователя, от имени которого запускается Collector, в группу `systemd-journal`, чтобы предоставить доступ на чтение к journal.
    Collector не обязательно запускать от имени root.
  + Для Kubernetes Collector должен запускаться от имени root, поскольку изоляция контейнеров препятствует доступу к journal на основе групп.
    Подробнее см. в разделе [Развёртывание в Kubernetes](#kubernetes-deployment).

## Демонстрационная конфигурация

Следующий пример конфигурации показывает, как:

* Настроить экземпляр Collector для чтения журналов из конкретных модулей systemd.
* Сопоставить поля journald с семантическими соглашениями OpenTelemetry.
* Отправить записи в Dynatrace.

```
extensions:



health_check:



endpoint: 0.0.0.0:13133



receivers:



journald:



directory: /var/log/journal



priority: info



start_at: end



operators:



# Move (rename) _PID to pid



- type: move



from: body._PID



to: body.pid



# Promote _EXE to a semantic convention attribute



- type: move



from: body._EXE



to: attributes["process.executable.name"]



# Rename MESSAGE to a consistently named body field



- type: move



from: body.MESSAGE



to: body.message



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



extensions: [health_check]



pipelines:



logs:



receivers: [journald]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверь свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

В этой конфигурации настраиваются следующие компоненты.

### Приёмники

В разделе `receivers` настраивается приёмник `journald` со следующими параметрами.

#### Фильтрация по модулю systemd

Параметр `units` ограничивает приём записями, принадлежащими перечисленным модулям systemd.
Удали его, чтобы собирать журналы со всех модулей на хосте.

Для более детальной фильтрации вместо этого используй параметр `matches`.
Например, можно комбинировать имена модулей с конкретными значениями полей journal.

Полный справочник по параметрам, примеры фильтрации и рекомендации по производительности для `start_at` и `priority` см. в [документации приёмника journald﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver#configuration).

#### Операторы

Параметр `operators` принимает массив [операторов stanza﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/pkg/stanza/docs/operators/README.md), применяемых к каждой записи журнала при её поступлении в конвейер.

В этой конфигурации используются [операторы `move`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/pkg/stanza/docs/operators/move.md) для переименования конкретных полей journal и продвижения `_EXE` до атрибута журнала, соответствующего [семантическим соглашениям OpenTelemetry для процессов﻿](https://opentelemetry.io/docs/specs/semconv/registry/attributes/process/).

* `body._PID` переименовывается в `body.pid`.
* `body._EXE` переименовывается в `attributes["process.executable.name"]`.
* `body.MESSAGE` переименовывается в `body.message`.

### Экспортёры

В разделе `exporters` указывается экспортёр [`otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter) по умолчанию, который настраивается с URL Dynatrace API и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые даются ссылки в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

### Конвейеры сервиса

В разделе `service` приёмник и экспортёр собираются в конвейер журналов.
Конвейер читает записи journal, применяет преобразования полей на основе операторов и передаёт результаты в Dynatrace.

## Особенности для развёртываний в Kubernetes

При запуске приёмника journald в Kubernetes разворачивай Collector как DaemonSet, чтобы один под Collector выполнялся на каждом узле.

Deployment не подходит, поскольку каждый под может иметь доступ только к systemd journal того узла, на котором он запланирован.
Масштабирование Deployment до нескольких реплик может привести к дублированию приёма журналов, если несколько реплик окажутся на одном узле.
DaemonSet обеспечивает полное покрытие журналов на уровне всего кластера и гарантирует ровно один привилегированный под с доступом к хосту на каждом узле.
Это ограничивает область воздействия на безопасность при запуске Collector от имени root.

### Требования к образу

Как указано в разделе [Предварительные требования](#prerequisites), контейнер Collector должен включать `journalctl` для доступа к systemd journal.

Подробнее см. в [документации проекта OTel﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver/examples/container).

### Контекст безопасности

Чтение из systemd journal требует определённых возможностей (capabilities) Linux.

Примени следующий `securityContext` (показанный в блоке кода ниже) к контейнеру Collector.
В таблице далее описано назначение соответствующих атрибутов в определении контекста безопасности.

```
securityContext:



allowPrivilegeEscalation: false



readOnlyRootFilesystem: true



seccompProfile:



type: RuntimeDefault



runAsUser: 0



capabilities:



drop:



- ALL



add:



- DAC_READ_SEARCH



- SYS_PTRACE
```

| Настройка | Причина |
| --- | --- |
| `allowPrivilegeEscalation: false` | Предотвращает получение процессом дополнительных привилегий сверх заявленных возможностей. |
| `readOnlyRootFilesystem: true` | Делает корневую файловую систему контейнера доступной только для чтения, чтобы уменьшить поверхность атаки. |
| `seccompProfile: RuntimeDefault` | Применяет профиль seccomp по умолчанию для ограничения разрешённых системных вызовов. |
| `runAsUser: 0` | Процесс Collector запускается от имени root для доступа к сокету journal.  При запуске от имени root повышается риск предоставления доступа уровня root к узлу. Подробнее см. в разделе [Запуск от имени root](#collector-root). |
| `DAC_READ_SEARCH` | Обходит проверки прав доступа файловой системы при чтении файлов journal. |
| `SYS_PTRACE` | Требуется для интроспекции процессов, используемой приёмником journald. |

### Запуск от root

Приёмник journald не требует запуска от root, но это самый простой способ получить необходимые Linux capabilities в контейнеризированной среде.

Если Collector запускается от root, не размещайте вместе с ним в одном инстансе сетевые приёмники (например, `otlp`, привязанный к `0.0.0.0`).
Уязвимость в сетевом приёмнике, эксплуатируемая удалённо, даст злоумышленнику доступ к узлу на уровне root.

Чтобы снизить риск, используйте отдельный инстанс Collector исключительно для сбора логов journald.
Если нужно включить в этот же инстанс дополнительные приёмники, привязывайте их к `127.0.0.1` (loopback), а не к `0.0.0.0`, чтобы предотвратить доступ извне.

### Монтирование томов

Смонтируйте каталог journal хоста в контейнер в режиме только для чтения.

Установите `directory: /run/log/journal` в конфигурации приёмника `journald`, чтобы путь совпадал с этим монтированием.

* В традиционных (неконтейнеризированных) Linux-системах персистентный journal хранится в `/var/log/journal`.
* В контейнеризированных Linux-средах journal обычно записывается в `/run/log/journal`.
  Это временное хранилище в памяти.

```
volumeMounts:



- name: run-journal



mountPath: /run/log/journal



readOnly: true



volumes:



- name: run-journal



hostPath:



path: /run/log/journal
```

## Ограничения

Логи принимаются по протоколу OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") и подчиняются ограничениям и лимитам API.
Подробнее см. [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Похожие темы

* [Ingest logs from files with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")
* [Ingest syslog data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")
* [Ingest Kubernetes pod logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs "Configure the OpenTelemetry Collector to ingest Kubernetes pod log files into Dynatrace.")
* [Transform and filter data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")