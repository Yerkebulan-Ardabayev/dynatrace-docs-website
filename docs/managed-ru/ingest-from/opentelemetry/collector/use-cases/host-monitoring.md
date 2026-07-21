---
title: Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring
---

# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace

# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace

* Практическое руководство
* Чтение за 2 минуты
* Обновлено 01 апреля 2026 г.

OpenTelemetry Host Monitoring, это функция Dynatrace, которая преобразует необработанные телеметрические данные от OTel Collector'ов в полезные аналитические сведения.
Вместо простого приёма метрик, логов и трассировок, Dynatrace автоматически выстраивает содержательный контекст вокруг инфраструктуры.
Она создаёт сущности хостов и процессов, устанавливает топологические связи и представляет данные на специально разработанных экранах анализа.

С этим расширением можно:

* использовать автоматически сгенерированные сущности (на основе извлечённых метаданных) для сопоставления метрик, логов и спанов и получения единого контекста во всей среде мониторинга.

Этот сценарий использования и его эталонная конфигурация рассчитаны в первую очередь на виртуальные машины и физические (bare-metal) хосты с ОС Linux.

* Если нужно запустить мониторинг хостов на узлах Kubernetes, требования к развёртыванию и ограничения см. в разделе [Мониторинг хостов на узлах Kubernetes](#kubernetes-considerations).
* Если нужно запустить мониторинг хостов на Windows OS или macOS, удали все упоминания `journald` из пайплайна, `journald` доступен только для ОС Linux.

## Предварительные требования

Этот сценарий использования предполагает, что уже есть:

* один из следующих дистрибутивов Collector с ресиверами [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver) и [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver), а также процессорами [`resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/resourcedetectionprocessor), [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) и [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнай, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнай, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [собственный (custom-built) OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнай, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* активировано расширение OpenTelemetry Host Monitoring.
  Подробнее о расширении см. в разделе [Расширение OpenTelemetry Host Monitoring](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Мониторь хосты с инструментацией OpenTelemetry с автоматически сгенерированной топологией сущностей, визуализациями метрик и алертами для более быстрого анализа инфраструктуры.").

## Эталонная конфигурация

Эталонная конфигурация доступна в GitHub-репозитории Dynatrace OTel Collector, см. [`host-metrics.yaml`﻿](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).

Эту конфигурацию можно использовать как есть или изменить под конкретные нужды.

## Компоненты

Для нашей конфигурации настроены следующие компоненты, специфичные для этого расширения.

### Ресиверы

В разделе `receivers` указаны следующие ресиверы:

* [`hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver)
* [`journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver)

#### hostmetrics

[Ресивер `hostmetrics`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/hostmetricsreceiver) собирает метрики уровня хоста.
Он настроен с тремя интервалами сбора: 10 секунд, 5 минут и 1 час.

* используй короткие интервалы для самых важных метрик, чтобы Dynatrace обеспечивал быстрые алерты о важных изменениях;
* отправляй некритичные метрики реже, чтобы помочь контролировать потребление и, соответственно, затраты.

#### journald

[Ресивер `journald`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/journaldreceiver) собирает журналы systemd journal с хоста и добавляет их в пайплайн логов наряду с метриками.
Он настроен на чтение из `/var/log/journal` (путь постоянного журнала по умолчанию на хостах Linux) и применяет операторы `move` для переименования полей журнала в соответствии с семантическими соглашениями OpenTelemetry.

* `body._PID` переименовывается в `body.pid`
* `body._EXE` переименовывается в `attributes["process.executable.name"]`
* `body.MESSAGE` переименовывается в `body.message`

Это обеспечивает связь логов хоста с теми же сущностями процессов, что и данные `hostmetrics`, что позволяет сопоставлять метрики и логи в Dynatrace.

Ресивер `journald` поддерживается только для ОС Linux и требует наличия на хосте бинарного файла `journalctl`.
Процесс Collector должен иметь право на чтение журнала systemd.

На хостах Linux добавь пользователя, от имени которого запускается Collector, в группу `systemd-journal`.

Подробности см. в разделе [Использование journald для приёма журналов systemd journal с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Настрой OpenTelemetry Collector для приёма журналов systemd journal с хостов Linux в Dynatrace.").

### Процессоры

В разделе `processors` указаны следующие процессоры:

* [процессор `resource_detection`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/resourcedetectionprocessor), который можно использовать для определения информации о ресурсе с хоста в формате, соответствующем семантическим соглашениям о ресурсах OpenTelemetry, и добавления или переопределения значения ресурса в телеметрических данных этой информацией;
* [`filter`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/filterprocessor) используется дважды: сначала для очистки ненужных измерений метрик, а затем (опционально) для отфильтровывания ненужных метрик процессов;
* [`transform`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/transformprocessor).

### Экспортёры

В разделе `exporters` указан [экспортёр `otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), настроенный с URL нашего Dynatrace API и необходимым токеном аутентификации.

Для этого задаются следующие две переменные окружения, на которые есть ссылки в значениях конфигурации для `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL конечной точки Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнай о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнай о конечных точках OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

## Как это сделать

### Топология

Это расширение автоматически генерирует топологию для инфраструктуры, отслеживаемой через Collector.
В частности, оно создаёт следующие типы сущностей на основе метаданных, извлечённых из метрик, логов и трассировок:

| Тип сущности | ID сущности |
| --- | --- |
| OpenTelemetry Host | dt.entity.otel:host |
| OpenTelemetry Process | dt.entity.otel:process |

Эти сущности позволяют Dynatrace сопоставлять метрики, логи и спаны и обеспечивать единый контекст во всей отслеживаемой среде.

### Обогащение телеметрии приложений

Если телеметрия приложения отправляется на локальный Collector хоста, он автоматически обогатит данные необходимыми атрибутами хоста, чтобы сигналы корректно привязывались к сущности OpenTelemetry-хоста.

Чтобы обогатить телеметрию приложения соответствующей сущностью процесса, все сигналы (метрики, логи и спаны) должны иметь атрибут ресурса `process.executable.name`.
Чтобы логи и спаны имели этот атрибут, нужно инициализировать OTel SDK с [детектором ресурса процесса﻿](https://opentelemetry.io/docs/languages/go/resources/).

Если это не реализовано для OTel SDK используемой технологии, атрибут `process.executable.name` всегда можно задать через [переменную окружения﻿](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration) `OTEL_RESOURCE_ATTRIBUTES`.

### Ограничение отправки метрик процессов

По умолчанию все метрики процессов отправляются в Dynatrace.

Также можно исключить определённые метрики процессов, чтобы контролировать объём OTel process entities и улучшить кардинальность.
Например, может понадобиться отфильтровать незначительные процессы, использующие менее 1 МиБ памяти.

Для этого можно фильтровать по объёму используемой процессом памяти или через allow list.

* Чтобы фильтровать по объёму используемой процессом памяти, используй следующие конфигурации процессоров `transform` и `filter` в конфигурации мониторинга хоста YAML.
  Скорректируй значение `datapoint.value_int` (в байтах) в соответствии со своим случаем использования.

  Если использование памяти процессом колеблется около заданного лимита, метрики могут поступать и отбрасываться с перебоями.
  Такие пробелы в данных повлияют на кумулятивные данные, например, счётчики или суммы.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - set(resource.attributes["low-memory-process"], "true") where metric.name == "process.memory.usage" and datapoint.value_int < 1048576 and resource.attributes["process.executable.name"] != nil



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```
* Чтобы создать allowlist, используй следующие процессоры `transform` и `filter` в конфигурации мониторинга хоста YAML.
  Скорректируй значения `ContainsValue()` и имена переменных `resource.attributes[]` в соответствии со своим случаем использования.

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

Эталонная конфигурация и данный сценарий использования оптимизированы для виртуальных машин и физических серверов (bare-metal).
OTel host monitoring можно запускать на узлах Kubernetes, но при этом есть дополнительные требования к развёртыванию и важные оговорки, которые нужно учитывать.

### Развёртывание

Чтобы собирать метрики уровня хоста с каждого узла кластера, разверни Collector как **DaemonSet**.
Это гарантирует, что на каждом узле работает один pod Collector, отчитывающийся по метрикам этого узла.

Receiver `hostmetrics` работает без какой-либо дополнительной конфигурации на Kubernetes.
Та же конфигурация receiver, что используется на виртуальных машинах, применима и к контейнеризированным развёртываниям.

### journald на Kubernetes

Чтобы собирать логи journald на узлах Kubernetes, Collector должен работать от root (`runAsUser: 0`), поскольку изоляция контейнера не позволяет получить доступ к журналу через группу.
Также нужно смонтировать каталог журнала с хоста и скорректировать настройку `directory`, указав смонтированный путь.

На Kubernetes путь к журналу в памяти обычно `/run/log/journal`, а не постоянный `/var/log/journal`, используемый на виртуальных машинах.
Полную конфигурацию развёртывания для Kubernetes, включая необходимый security context и монтирование томов хоста, смотри в [Use journald to ingest systemd journal logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Configure the OpenTelemetry Collector to ingest systemd journal logs from Linux hosts into Dynatrace.").

### Пересечение метрик с мониторингом Kubernetes

Если на одних и тех же узлах одновременно работают и OTel host monitoring, и [кластерный мониторинг Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters."), учитывай, что некоторые метрики пересекаются: одни и те же измерения могут поступать в виде двух отдельных ключей метрик.
Это связано с тем, что у них разные имена метрик, следующие разным семантическим соглашениям, поэтому Dynatrace принимает их как отдельные ключи метрик.

В следующей таблице показаны распространённые пересекающиеся метрики:

| receiver `hostmetrics` | receiver `kubelet_stats` | Что измеряют |
| --- | --- | --- |
| `system.cpu.*` | `k8s.node.cpu.*` | Использование CPU узла |
| `system.memory.*` | `k8s.node.memory.*` | Использование памяти узла |
| `system.filesystem.*` | `k8s.node.filesystem.*` | Использование файловой системы узла |
| `system.network.*` | `k8s.node.network.*` | Сетевой ввод-вывод узла |

Это пересечение возникает потому, что сценарий использования мониторинга Kubernetes использует [receiver `kubelet_stats`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/kubeletstatsreceiver), который отчитывается по метрикам ресурсов на уровне узла, представляющим те же исходные данные, что и receiver `hostmetrics`.

Чтобы избежать ненужного дублирования на Kubernetes, по возможности используй только мониторинг Kubernetes либо только OTel host monitoring:

* Используй только мониторинг Kubernetes, если не требуется детализация на уровне процессов и топология host entity.
  [Кластерный мониторинг Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.") предоставляет метрики уровня узла через receiver `kubelet_stats`. Добавление `hostmetrics` поверх дублирует метрики ресурсов уровня узла.
* Используй только host monitoring, если не требуются специфичные для Kubernetes метрики объектов, такие как поды и deployments.
  OTel host monitoring предоставляет host- и process-сущности с топологией в Dynatrace.
* Если нужны оба сценария использования, используй процессор `filter`, чтобы отбросить пересекающиеся метрики уровня узла из одного из двух пайплайнов.
  Например, отфильтруй `system.cpu.*`, `system.memory.*`, `system.filesystem.*` и `system.network.*` из пайплайна host monitoring, если пайплайн мониторинга Kubernetes уже их покрывает.

## Ограничения

* Метрика `system.processes.created` доступна только на Linux.
* Метрика `process.disk.io` требует запуска Collector с привилегированным доступом.
  Если этого не сделать, сбор метрики будет невозможен.
* Receiver `journald` поддерживается только на Linux. Попытка использовать receiver `journald` на другой операционной системе приведёт к тому, что Collector вернёт ошибку и завершит работу при запуске.