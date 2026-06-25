---
title: Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring
scraped: 2026-05-12T12:10:50.254912
---

# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace

# Мониторинг хостов, отправляющих данные OpenTelemetry в Dynatrace

* Практическое руководство
* Чтение: 2 мин
* Обновлено 01 апреля 2026 г.

OpenTelemetry Host Monitoring, это функция Dynatrace, которая преобразует необработанные данные телеметрии от OTel Collector в практические сведения.
Вместо простого приёма метрик, логов и трассировок Dynatrace автоматически выстраивает значимый контекст вокруг вашей инфраструктуры.
Она создаёт сущности хостов и процессов, устанавливает топологические связи и представляет данные через специально предназначенные экраны анализа.

С помощью расширения можно:

* Использовать автоматически создаваемые сущности (на основе извлечённых метаданных) для корреляции метрик, логов и спанов и обеспечения единого контекста во всей вашей среде мониторинга.

Этот сценарий использования и его эталонная конфигурация предназначены прежде всего для виртуальных машин и физических хостов с ОС Linux.

* Если требуется запустить мониторинг хостов на узлах Kubernetes, см. требования к развёртыванию и ограничения в разделе [Мониторинг хостов на узлах Kubernetes](#kubernetes-considerations).
* Если требуется запустить мониторинг хостов в ОС Windows или macOS, удалите из конвейера все ссылки на `journald`: `journald` доступен только для ОС Linux.

## Предварительные требования

Этот сценарий использования предполагает, что у вас есть:

* Один из следующих дистрибутивов Collector с receiver [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver) и [`journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver), а также processor [`resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/resourcedetectionprocessor), [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) и [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor).

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [специально собранный OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* Активированное расширение OpenTelemetry Host Monitoring.
  Дополнительные сведения о расширении см. в разделе [Расширение OpenTelemetry Host Monitoring](/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring "Создавайте топологию и экраны для данных ваших хостов OpenTelemetry для более быстрого отображения и более простого анализа данных.").

## Эталонная конфигурация

Эталонная конфигурация доступна в репозитории GitHub для Dynatrace OTel Collector, см. [`host-metrics.yaml`](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).

Эту конфигурацию можно использовать как есть или изменить её под ваши конкретные потребности.

## Компоненты

Для нашей конфигурации мы настроили следующие компоненты, специфичные для этого расширения.

### Receivers

В разделе `receivers` мы указываем следующие receiver:

* [`hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver)
* [`journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver)

#### hostmetrics

[receiver `hostmetrics`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/hostmetricsreceiver) собирает метрики уровня хоста.
Он настроен с тремя интервалами сбора: 10 секунд, 5 минут и 1 час.

* Используйте короткие интервалы для самых важных метрик, чтобы Dynatrace обеспечивал быстрые оповещения о важных изменениях.
* Отправляйте некритичные метрики реже, чтобы помочь контролировать потребление и, следовательно, затраты.

#### journald

[receiver `journald`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver) собирает логи журнала systemd с хоста и принимает их в конвейер логов вместе с вашими метриками.
Он настроен на чтение из `/var/log/journal` (путь к постоянному журналу по умолчанию на хостах Linux) и применяет операторы `move` для переименования полей журнала в соответствии с семантическими соглашениями OpenTelemetry.

* `body._PID` переименовывается в `body.pid`
* `body._EXE` переименовывается в `attributes["process.executable.name"]`
* `body.MESSAGE` переименовывается в `body.message`

Это гарантирует, что логи хоста связываются с теми же сущностями процессов, что и данные `hostmetrics`, обеспечивая корреляцию между метриками и логами в Dynatrace.

receiver `journald` поддерживается только в ОС Linux и требует наличия на хосте двоичного файла `journalctl`.
Процесс Collector должен иметь разрешение на чтение журнала systemd.

На хостах Linux добавьте пользователя, запускающего Collector, в группу `systemd-journal`.

Все подробности см. в разделе [Использование journald для приёма логов журнала systemd с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Настройте OpenTelemetry Collector для приёма логов журнала systemd с хостов Linux в Dynatrace.").

### Processors

В разделе `processors` мы указываем следующие processor:

* [processor `resourcedetection`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/resourcedetectionprocessor), который можно использовать для обнаружения информации о ресурсе на хосте в формате, соответствующем семантическим соглашениям ресурса OpenTelemetry, и добавления этой информации к значению ресурса в данных телеметрии либо его переопределения.
* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) используется дважды: первый раз для очистки ненужных измерений метрик и второй раз для (необязательной) фильтрации ненужных метрик процессов.
* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor).

### Exporters

В разделе `exporters` мы указываем [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

## Практическое руководство

### Топология

Это расширение автоматически создаёт топологию для инфраструктуры, отслеживаемой через Collector.
В частности, оно создаёт следующие типы сущностей на основе метаданных, извлечённых из метрик, логов и трассировок:

| Тип сущности | ID сущности |
| --- | --- |
| OpenTelemetry Host | dt.entity.otel:host |
| OpenTelemetry Process | dt.entity.otel:process |

Эти сущности позволяют Dynatrace коррелировать ваши метрики, логи и спаны и обеспечивать единый контекст во всей отслеживаемой среде.

### Обогащение телеметрии приложений

Если вы отправляете телеметрию приложения в локальный Collector хоста, он автоматически обогатит данные необходимыми атрибутами хоста, чтобы сигналы были корректно привязаны к сущности хоста OpenTelemetry.

Чтобы обогатить телеметрию приложения соответствующей сущностью процесса, все сигналы (метрики, логи и спаны) должны иметь атрибут ресурса `process.executable.name`.
Чтобы логи и спаны имели этот атрибут, необходимо инициализировать ваш OTel SDK с помощью [детектора ресурсов процесса](https://opentelemetry.io/docs/languages/go/resources/).

Если это не реализовано для OTel SDK вашей технологии, всегда можно задать атрибут `process.executable.name` через переменную окружения `OTEL_RESOURCE_ATTRIBUTES` ([переменную окружения](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration)).

### Ограничение отправки метрик процессов

По умолчанию в Dynatrace отправляются все метрики процессов.

Также можно исключить определённые метрики процессов, чтобы контролировать количество сущностей процессов OTel и улучшить кардинальность.
Например, может потребоваться отфильтровать незначительные процессы, использующие менее 1 МиБ памяти.

Для этого можно выполнить фильтрацию по использованию памяти процессом или по списку разрешений.

* Для фильтрации по использованию памяти процессом используйте в вашем YAML-файле конфигурации мониторинга хостов следующие конфигурации processor `transform` и `filter`.
  Скорректируйте значение `datapoint.value_int` (в байтах) в соответствии с вашим сценарием использования.

  Если использование памяти процессом колеблется вокруг заданного предела, метрики могут приниматься и отбрасываться с перерывами.
  Такие пропуски в данных повлияли бы на кумулятивные данные, например на счётчики или суммы.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - set(resource.attributes["low-memory-process"], "true") where metric.name == "process.memory.usage" and datapoint.value_int < 1048576 and resource.attributes["process.executable.name"] != nil



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```
* Для создания списка разрешений используйте в вашем YAML-файле конфигурации мониторинга хостов следующие processor `transform` и `filter`.
  Скорректируйте имена переменных `ContainsValue()` и `resource.attributes[]` в соответствии с вашим сценарием использования.

  ```
  transform:



  error_mode: ignore



  metric_statements:



  - delete_key(resource.attributes, "low-memory-process") where ContainsValue(["my-process", "another-process"], resource.attributes["process.executable.name"])



  filter/delete-metrics:



  metric_conditions:



  - resource.attributes["low-memory-process"] != nil
  ```

## Мониторинг хостов на узлах Kubernetes

Эталонная конфигурация и этот сценарий использования оптимизированы для виртуальных машин и физических хостов.
Мониторинг хостов OTel можно запустить на узлах Kubernetes, но при этом следует учитывать дополнительные требования к развёртыванию и важные оговорки.

### Развёртывание

Для сбора метрик уровня хоста с каждого узла вашего кластера разверните Collector как **DaemonSet**.
Это гарантирует, что на каждом узле работает один под Collector и сообщает метрики этого узла.

receiver `hostmetrics` работает в Kubernetes без какой-либо дополнительной конфигурации.
Та же конфигурация receiver, которую вы используете на виртуальных машинах, применяется и к контейнеризированным развёртываниям.

### journald в Kubernetes

Для сбора логов journald на узлах Kubernetes Collector должен работать от имени root (`runAsUser: 0`), поскольку изоляция контейнеров препятствует доступу к журналу на основе групп.
Вам также нужно смонтировать каталог журнала с хоста и задать в параметре `directory` смонтированный путь.

В Kubernetes путь к журналу в памяти обычно `/run/log/journal`, а не постоянный `/var/log/journal`, используемый на виртуальных машинах.
Полную конфигурацию развёртывания в Kubernetes, включая необходимый контекст безопасности и монтирование томов хоста, см. в разделе [Использование journald для приёма логов журнала systemd с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/journald "Настройте OpenTelemetry Collector для приёма логов журнала systemd с хостов Linux в Dynatrace.").

### Перекрытие метрик с мониторингом Kubernetes

Если вы запускаете на одних и тех же узлах одновременно мониторинг хостов OTel и [мониторинг кластеров Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Настройте OpenTelemetry Collector для мониторинга ваших кластеров Kubernetes."), учтите, что некоторые метрики перекрываются: одни и те же измерения могут приниматься как два отдельных ключа метрик.
Это происходит потому, что они имеют разные имена метрик, следующие разным семантическим соглашениям, поэтому Dynatrace принимает их как отдельные ключи метрик.

В следующей таблице показаны типичные перекрывающиеся метрики:

| receiver `hostmetrics` | receiver `kubeletstats` | Что они измеряют |
| --- | --- | --- |
| `system.cpu.*` | `k8s.node.cpu.*` | Использование CPU узла |
| `system.memory.*` | `k8s.node.memory.*` | Использование памяти узла |
| `system.filesystem.*` | `k8s.node.filesystem.*` | Использование файловой системы узла |
| `system.network.*` | `k8s.node.network.*` | Сетевой ввод-вывод узла |

Это перекрытие возникает потому, что в сценарии использования мониторинга Kubernetes применяется [receiver `kubeletstats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver), который сообщает метрики ресурсов уровня узла, представляющие те же базовые данные, что и receiver `hostmetrics`.

Чтобы избежать ненужного дублирования в Kubernetes, по возможности используйте только мониторинг Kubernetes или только мониторинг хостов OTel:

* Используйте только мониторинг Kubernetes, если вам не требуется детализация на уровне процессов и топология сущностей хостов.
  [Мониторинг кластеров Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Настройте OpenTelemetry Collector для мониторинга ваших кластеров Kubernetes.") предоставляет метрики уровня узла через receiver `kubeletstats`. Добавление `hostmetrics` поверх этого дублирует метрики ресурсов уровня узла.
* Используйте только мониторинг хостов, если вам не требуются специфичные для Kubernetes метрики объектов, такие как поды и развёртывания.
  Мониторинг хостов OTel предоставляет сущности хостов и процессов с топологией в Dynatrace.
* Если вам нужны оба сценария использования, используйте processor `filter`, чтобы отбрасывать перекрывающиеся метрики уровня узла из одного из двух конвейеров.
  Например, отфильтруйте `system.cpu.*`, `system.memory.*`, `system.filesystem.*` и `system.network.*` из конвейера мониторинга хостов, если конвейер мониторинга Kubernetes уже их охватывает.

## Ограничения

* Метрика `system.processes.created` доступна только в Linux.
* Метрика `process.disk.io` требует запуска Collector с привилегированным доступом.
  Если этого не сделать, захват метрики будет заблокирован.
* receiver `journald` поддерживается только в Linux. Попытка использовать receiver `journald` в другой операционной системе приведёт к тому, что Collector вернёт ошибку и завершит работу при запуске.