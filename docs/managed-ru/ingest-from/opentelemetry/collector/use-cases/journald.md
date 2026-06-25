---
title: Использование journald для приёма логов журнала systemd с помощью OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/journald
scraped: 2026-05-12T12:10:46.344931
---

# Использование journald для приёма логов журнала systemd с помощью OTel Collector

# Использование journald для приёма логов журнала systemd с помощью OTel Collector

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 12 марта 2026 г.

Receiver journald читает записи логов из [журнала systemd](https://wiki.archlinux.org/title/Systemd/Journal), вызывая `journalctl` как подпроцесс и передавая его вывод потоком в конвейер OTel Collector.

Каждая запись журнала становится записью лога OTLP, в которой поля журнала сопоставляются с атрибутами лога.
Чтобы переименовать или преобразовать эти атрибуты в соответствии с семантическими соглашениями OpenTelemetry, можно использовать [операторы](#operators).

Используйте receiver journald, когда:

* Ваши сервисы на базе Linux записывают логи в журнал systemd, а не в отдельные файлы логов.
* Требуется централизовать логи системных сервисов уровня хоста (например, `ssh`, `kubelet` или `docker`) в Dynatrace без управления дополнительными путями к файлам логов.
* Требуется фильтровать приём по конкретным юнитам systemd и уровням приоритета для контроля объёма данных.

## Предварительные требования

* Один из следующих дистрибутивов Collector с [receiver journald](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver).

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#collector-distro "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
  + [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), на который должны экспортироваться данные.

* ОС Linux на хосте или в контейнере, где работает Collector.
* Двоичный файл `journalctl` должен присутствовать на хосте или в контейнере, где работает Collector.
  Это связано с тем, что receiver полагается на `journalctl` для всего доступа к журналу.

  + Для развёртываний в контейнерах используйте образ, включающий `systemd`, и монтируйте каталог журнала с хоста.
  + Сведения о требованиях, специфичных для Kubernetes, см. в разделе [Развёртывание в Kubernetes](#kubernetes-deployment).
* Процессу Collector требуется разрешение на чтение журнала systemd через `journalctl`.

  + На хосте с ОС Linux добавьте пользователя, под которым работает Collector, в группу `systemd-journal`, чтобы предоставить доступ к журналу на чтение.
    Collector не обязательно запускать от имени root.
  + В Kubernetes Collector должен работать от имени root, поскольку изоляция контейнеров препятствует доступу к журналу на основе групп.
    Дополнительные сведения см. в разделе [Развёртывание в Kubernetes](#kubernetes-deployment).

## Демонстрационная конфигурация

В следующем примере конфигурации показано, как:

* Настроить экземпляр Collector для чтения логов из конкретных юнитов systemd.
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

[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

## Компоненты

Для нашей конфигурации мы настраиваем следующие компоненты.

### Receivers

В разделе `receivers` мы настраиваем receiver `journald` со следующими параметрами.

#### Фильтрация по юниту systemd

Параметр `units` ограничивает приём записями, принадлежащими перечисленным юнитам systemd.
Удалите его, чтобы собирать логи со всех юнитов на хосте.

Для более детальной фильтрации используйте вместо него параметр `matches`.
Например, можно сочетать имена юнитов с конкретными значениями полей журнала.

Полный справочник параметров, примеры фильтрации и соображения по производительности для `start_at` и `priority` см. в [документации по receiver journald](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver#configuration).

#### Операторы

Параметр `operators` принимает массив [операторов stanza](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/stanza/docs/operators/README.md), применяемых к каждой записи лога при её поступлении в конвейер.

В этой конфигурации мы используем [операторы `move`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/stanza/docs/operators/move.md) для переименования конкретных полей журнала и повышения `_EXE` до атрибута лога, согласованного с [семантическими соглашениями OpenTelemetry для процессов](https://opentelemetry.io/docs/specs/semconv/registry/attributes/process/).

* `body._PID` переименовывается в `body.pid`.
* `body._EXE` переименовывается в `attributes["process.executable.name"]`.
* `body.MESSAGE` переименовывается в `body.message`.

### Exporters

В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.

Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

### Сервисные конвейеры

В разделе `service` мы собираем receiver и exporter в конвейер логов.
Конвейер читает записи журнала, применяет преобразования полей на основе операторов и принимает результаты в Dynatrace.

## Соображения для развёртываний в Kubernetes

При запуске receiver journald в Kubernetes развёртывайте Collector как DaemonSet, чтобы на каждом узле работал один под Collector.

Deployment не подходит, поскольку каждый под имеет доступ только к журналу systemd того узла, на который он назначен.
Масштабирование Deployment до нескольких реплик может привести к дублированию приёма логов, когда несколько реплик попадают на один и тот же узел.
DaemonSet обеспечивает полный охват логов в масштабе всего кластера и гарантирует ровно один привилегированный под с доступом к хосту на узел.
Это ограничивает влияние на безопасность при запуске Collector от имени root.

### Требования к образу

Как сказано в разделе [Предварительные требования](#prerequisites), контейнер Collector должен включать `journalctl` для доступа к журналу systemd.

Дополнительные сведения см. в [вышестоящей документации OTel](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver/examples/container).

### Контекст безопасности

Чтение из журнала systemd требует определённых возможностей Linux.

Примените к контейнеру Collector следующий `securityContext` (показан в блоке кода ниже).
Затем в таблице описывается назначение соответствующих атрибутов в определении контекста безопасности.

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

| Параметр | Причина |
| --- | --- |
| `allowPrivilegeEscalation: false` | Не позволяет процессу получать дополнительные привилегии сверх объявленных возможностей. |
| `readOnlyRootFilesystem: true` | Делает корневую файловую систему контейнера доступной только для чтения, чтобы уменьшить поверхность атаки. |
| `seccompProfile: RuntimeDefault` | Применяет стандартный профиль seccomp для ограничения разрешённых системных вызовов. |
| `runAsUser: 0` | Процесс Collector работает от имени root для доступа к сокету журнала.  При запуске от имени root повышается риск предоставления доступа к узлу на уровне root. Дополнительные сведения см. в разделе [Запуск от имени root](#collector-root). |
| `DAC_READ_SEARCH` | Обходит проверки разрешений файловой системы при чтении файлов журнала. |
| `SYS_PTRACE` | Требуется для интроспекции процессов, используемой receiver journald. |

### Запуск от имени root

Receiver journald не требует запуска от имени root, но это самый простой способ получить необходимые возможности Linux в контейнеризованной среде.

Если ваш Collector работает от имени root, избегайте размещения в том же экземпляре доступных по сети receiver (таких как `otlp`, привязанный к `0.0.0.0`).
Уязвимость в сетевом receiver, эксплуатируемая удалённо, предоставила бы доступ к узлу на уровне root.

Чтобы снизить риск, используйте выделенный экземпляр Collector исключительно для сбора логов journald.
Если необходимо включить в тот же экземпляр дополнительные receiver, привязывайте их к `127.0.0.1` (loopback), а не к `0.0.0.0`, чтобы предотвратить внешний доступ.

### Монтирование томов

Смонтируйте каталог журнала хоста в контейнер в режиме только для чтения.

Задайте `directory: /run/log/journal` в конфигурации receiver `journald`, чтобы он соответствовал этому пути монтирования.

* В традиционных (неконтейнеризованных) системах Linux постоянный журнал хранится в `/var/log/journal`.
* В контейнеризованных средах Linux журнал обычно записывается в `/run/log/journal`.
  Это эфемерное хранилище в памяти.

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

## Пределы и ограничения

Логи принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подчиняются ограничениям и лимитам этого API.
Дополнительные сведения см. в разделе [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

## Связанные темы

* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace.")
* [Приём данных syslog с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.")
* [Приём логов подов Kubernetes с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs "Настройте OpenTelemetry Collector для приёма файлов логов подов Kubernetes в Dynatrace.")
* [Преобразование и фильтрация данных с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Настройте OpenTelemetry Collector для добавления, преобразования и отбрасывания данных OpenTelemetry.")