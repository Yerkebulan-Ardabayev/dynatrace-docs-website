---
title: Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring
---

# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace

# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace

* Практическое руководство
* 2 мин. чтения
* Обновлено 20 июл. 2026

OpenTelemetry Host Monitoring, это функция Dynatrace, которая преобразует необработанные данные телеметрии от OTel Collectors в практически полезные сведения.
Вместо простого приёма метрик, логов и трейсов Dynatrace автоматически формирует значимый контекст вокруг инфраструктуры.
Создаются сущности хостов и процессов, устанавливаются топологические связи, а данные отображаются на специализированных экранах анализа.

С расширением можно:

* Использовать автоматически создаваемые сущности (на основе извлечённых метаданных) для корреляции метрик, логов и спанов и получения единого контекста в среде мониторинга.

Этот сценарий использования и его эталонная конфигурация рассчитаны прежде всего на виртуальные машины и bare-metal хосты под управлением Linux OS.

* Чтобы запустить мониторинг хостов на нодах Kubernetes, см. [Мониторинг хостов на нодах Kubernetes](#kubernetes-considerations): требования к развёртыванию и ограничения.
* Чтобы запустить мониторинг хостов на Windows OS или macOS, нужно убрать из пайплайна все упоминания `journald`: `journald` доступен только для Linux OS.

## Предварительные требования

В этом сценарии использования предполагается наличие:

* Одного из следующих дистрибутивов Collector с ресиверами [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver) и [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver), а также процессорами [`resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/resourcedetectionprocessor), [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) и [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor).

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [Пользовательский OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Активированного расширения OpenTelemetry Host Monitoring.
  Подробнее о расширении: [OpenTelemetry Host Monitoring extension](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Мониторинг хостов с инструментацией OpenTelemetry с помощью автоматически созданной топологии сущностей, визуализаций метрик и предупреждений для ускоренного анализа инфраструктуры.").

## Эталонная конфигурация

Эталонная конфигурация доступна в репозитории GitHub коллектора Dynatrace OTel Collector, см. [`host-metrics.yaml`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).

Конфигурацию можно использовать в готовом виде или изменить под конкретные задачи.

## Компоненты

В этой конфигурации настроены следующие компоненты, специфичные для данного расширения.

### Ресиверы

В разделе `receivers` указаны следующие ресиверы:

* [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver)
* [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver)

#### hostmetrics

Ресивер [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver) собирает метрики уровня хоста.
Он настроен с тремя интервалами сбора: 10 секунд, 5 минут и 1 час.

* Для наиболее важных метрик нужно использовать короткие интервалы, чтобы Dynatrace быстро оповещал об изменениях.
* Некритические метрики стоит отправлять реже: это помогает контролировать потребление ресурсов и снизить затраты.

#### journald

Ресивер [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver) собирает журнальные логи systemd с хоста и передаёт их в пайплайн логов вместе с метриками.
Он настроен на чтение из `/var/log/journal` (путь по умолчанию для постоянного журнала на Linux-хостах) и применяет операторы `move` для переименования полей журнала в соответствии с семантическими соглашениями OpenTelemetry.

* `body._PID` переименовывается в `body.pid`
* `body._EXE` переименовывается в `attributes["process.executable.name"]`
* `body.MESSAGE` переименовывается в `body.message`

Это гарантирует, что логи хоста будут связаны с теми же сущностями процессов, что и данные `hostmetrics`, обеспечивая корреляцию метрик и логов в Dynatrace.

Ресивер `journald` поддерживается только на Linux OS и требует наличия бинарного файла `journalctl` на хосте.
Процесс Collector должен иметь разрешение на чтение журнала systemd.

На Linux-хостах нужно добавить пользователя, запускающего Collector, в группу `systemd-journal`.

Подробнее: [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Настройка OpenTelemetry Collector для приёма журнальных логов systemd с Linux-хостов в Dynatrace.").

### Процессоры

В разделе `processors` указаны следующие процессоры:

* [`resource_detection` processor﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/resourcedetectionprocessor): определяет информацию о ресурсах хоста в формате, соответствующем семантическим соглашениям ресурсов OpenTelemetry, и добавляет или переопределяет значение ресурса в данных телеметрии.
* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) используется дважды: первый раз для удаления лишних измерений метрик, второй раз (опционально) для исключения ненужных метрик процессов.
* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor).

### Экспортёры

В разделе `exporters` указан [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL API Dynatrace и необходимым токеном аутентификации.

Для этого задаются две переменные среды, на которые ссылаются в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые используются для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые используются для экспорта данных OpenTelemetry в Dynatrace.").

## Инструкции

### Топология

Расширение автоматически формирует топологию инфраструктуры, отслеживаемой через Collector.
В частности, создаются типы сущностей на основе метаданных, извлечённых из метрик, логов и трейсов.

| Тип сущности | Entity ID |
| --- | --- |
| OpenTelemetry host | `dt.entity.otel:host` |
| OpenTelemetry process | `dt.entity.otel:process` |

Эти сущности позволяют Dynatrace коррелировать метрики, логи и спаны и обеспечивать единый контекст в отслеживаемой среде.

Обязательные атрибуты для извлечения сущностей

Чтобы Dynatrace мог извлекать сущности хостов и процессов, в данных телеметрии должны присутствовать следующие атрибуты ресурса.
При использовании эталонной конфигурации они включаются автоматически.
При использовании пользовательской конфигурации Collector, отличающейся от эталонной, нужно убедиться, что эти атрибуты включены.

| Сигнал | `otel:host` | `otel:process` |
| --- | --- | --- |
| Метрики | * `host.id` * `host.name` * `dt.metrics.source` должен быть `opentelemetry` | * Все атрибуты ресурса из `otel:host` * Дополнительно `process.executable.name` |
| Логи | * `host.id` * `host.name` * `dt.openpipeline.source` должен быть `/api/v2/otlp/v1/logs`   Устанавливается автоматически OpenPipeline; если это значение изменено или удалено, извлечение сущностей перестаёт работать корректно. | * Все атрибуты ресурса из `otel:host` * Дополнительно `process.executable.name` |
| Спаны | * `host.id` * `host.name` * `telemetry.sdk.name` должен быть `opentelemetry`, `odin` или `otel` | * Все атрибуты ресурса из `otel:host` * Дополнительно `process.executable.name` |

### Обогащение телеметрии приложений

Если отправлять телеметрию приложения на локальный Collector, он автоматически дополнит данные необходимыми атрибутами хоста, чтобы сигналы корректно привязались к OpenTelemetry-сущности хоста.

Для обогащения телеметрии приложения соответствующей сущностью процесса все сигналы (метрики, логи и спаны) должны содержать атрибут ресурса `process.executable.name`.
Чтобы логи и спаны получали этот атрибут, нужно инициализировать OTel SDK с [детектором ресурса process](https://opentelemetry.io/docs/languages/go/resources/).

Если для используемой технологии это в OTel SDK не реализовано, атрибут `process.executable.name` всегда можно задать через [переменную окружения](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration) `OTEL_RESOURCE_ATTRIBUTES`.

### Ограничение отправки метрик процессов

По умолчанию все метрики процессов отправляются в Dynatrace.

Часть метрик процессов можно исключить, чтобы контролировать количество OTel-сущностей процессов и улучшить кардинальность.
Например, можно отфильтровать незначительные процессы, потребляющие менее 1 МиБ памяти.

Для этого применяется фильтрация по потреблению памяти процессом или по списку разрешённых процессов.

* Для фильтрации по потреблению памяти процессом используй следующие конфигурации процессоров `transform` и `filter` в конфигурации мониторинга хоста YAML.
  Значение `datapoint.value_int` (в байтах) подбирается под конкретный сценарий.

  Если потребление памяти процессом колеблется около заданного лимита, метрики могут периодически поступать и отбрасываться.
  Такие пробелы в данных влияют на накопительные данные, например счётчики или суммы.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - set(resource.attributes["low-memory-process"], "true") where metric.name == "process.memory.usage" and datapoint.value_int < 1048576 and resource.attributes["process.executable.name"] != nil



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```
* Для создания списка разрешённых процессов используй следующие процессоры `transform` и `filter` в конфигурации мониторинга хоста YAML.
  Имена переменных `ContainsValue()` и `resource.attributes[]` подбираются под конкретный сценарий.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - delete_key(resource.attributes, "low-memory-process") where ContainsValue(["my-process", "another-process"], resource.attributes["process.executable.name"])



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```

## Мониторинг хоста на узлах Kubernetes

Референсная конфигурация и данный сценарий оптимизированы для виртуальных машин и физических серверов.
OTel-мониторинг хоста можно запускать на узлах Kubernetes, однако при этом есть дополнительные требования к развёртыванию и важные оговорки.

### Развёртывание

Для сбора метрик уровня хоста с каждого узла кластера разверни Collector как **DaemonSet**.
Это обеспечит запуск одного пода Collector на каждом узле с отчётностью по метрикам этого узла.

Ресивер `hostmetrics` работает на Kubernetes без дополнительной настройки.
Та же конфигурация ресивера, что используется для виртуальных машин, применима и к контейнеризованным развёртываниям.

### journald на Kubernetes

Для сбора journald-логов на узлах Kubernetes Collector должен запускаться от root (`runAsUser: 0`), так как изоляция контейнеров препятствует групповому доступу к журналу.
Также потребуется смонтировать директорию журнала с хоста и скорректировать параметр `directory` на путь монтирования.

На Kubernetes путь к журналу в оперативной памяти обычно `/run/log/journal`, а не постоянный `/var/log/journal`, используемый на виртуальных машинах.
Полная конфигурация развёртывания на Kubernetes, включая необходимый security context и монтирование томов хоста, приведена в разделе [Использование journald для приёма логов systemd через OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.").

### Пересечение метрик с мониторингом Kubernetes

При одновременном запуске OTel-мониторинга хоста и [мониторинга кластера Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") на одних и тех же узлах следует учитывать, что часть метрик пересекается: одни и те же измерения могут поступать как два отдельных ключа метрик.
Это происходит потому, что метрики имеют разные имена, следующие разным семантическим соглашениям, поэтому Dynatrace принимает их как отдельные ключи метрик.

В таблице ниже показаны часто пересекающиеся метрики:

| Ресивер `hostmetrics` | Ресивер `kubelet_stats` | Что измеряют |
| --- | --- | --- |
| `system.cpu.*` | `k8s.node.cpu.*` | Использование CPU узла |
| `system.memory.*` | `k8s.node.memory.*` | Использование памяти узла |
| `system.filesystem.*` | `k8s.node.filesystem.*` | Использование файловой системы узла |
| `system.network.*` | `k8s.node.network.*` | Сетевой ввод/вывод узла |

Это пересечение возникает из-за того, что сценарий мониторинга Kubernetes использует [ресивер `kubelet_stats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver), который передаёт метрики ресурсов уровня узла, представляющие те же базовые данные, что и ресивер `hostmetrics`.

Во избежание ненужного дублирования на Kubernetes рекомендуется по возможности использовать только один вариант мониторинга: либо мониторинг Kubernetes, либо OTel-мониторинг хоста.

* Используй только мониторинг Kubernetes, если детализация до уровня процессов и топология сущностей хоста не требуются.
  [Мониторинг кластера Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") предоставляет метрики уровня узла через ресивер `kubelet_stats`. Добавление `hostmetrics` поверх дублирует метрики ресурсов уровня узла.
* Используй только мониторинг хоста, если метрики объектов, специфичных для Kubernetes, такие как поды и деплойменты, не нужны.
  OTel-мониторинг хоста предоставляет сущности хоста и процессов с топологией в Dynatrace.
* Если требуются оба сценария, используй процессор `filter`, чтобы удалить пересекающиеся метрики уровня узла из одного из двух пайплайнов.
  Например, можно отфильтровать `system.cpu.*`, `system.memory.*`, `system.filesystem.*` и `system.network.*` из пайплайна мониторинга хоста, если пайплайн мониторинга Kubernetes уже охватывает их.

## Ограничения

* Метрика `system.processes.created` доступна только на Linux.
* Метрика `process.disk.io` требует запуска Collector с привилегированным доступом.
  Без этого сбор метрики будет заблокирован.
* Ресивер `journald` поддерживается только на Linux. При попытке использовать ресивер `journald` на другой операционной системе Collector вернёт ошибку и завершит работу при запуске.