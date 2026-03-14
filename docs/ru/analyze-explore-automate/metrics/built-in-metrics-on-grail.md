---
title: Встроенные метрики в Grail
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/built-in-metrics-on-grail
scraped: 2026-03-03T21:22:30.551812
---

# Встроенные метрики в Grail


* Последняя версия Dynatrace
* Справочник
* Чтение: 39 мин
* Обновлено 10 февраля 2026 г.

Метрики в Grail поддерживают многие из существующих [встроенных метрик](../metrics-classic/built-in-metrics.md "Ознакомьтесь с полным списком встроенных метрик Dynatrace."), перечисленных ниже.

В раскрывающихся разделах ниже описаны различия встроенных метрик в Grail по сравнению с аналогичными метриками Metrics Classic.

Переименованные ключи метрик

Метрики в Grail вводят рекомендации по улучшению ясности, единообразия и читаемости метрик, измерений и сущностей, предоставляемых Dynatrace, на всей платформе Dynatrace:

* Замена префикса `builtin:` на `dt.` для явного обозначения метрик и сущностей, предоставляемых Dynatrace.
* Предпочтение snake_case (`capacity_units`) вместо camelCase (`capacityUnits`) для улучшения читаемости.
* Повышение конкретности для более точного отражения измеряемых величин.

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.host.uptime | builtin:host.uptime |
| dt.host.disk.used.percent | builtin:host.disk.usedPct |
| dt.process.network.sessions.reset\_local | builtin:tech.generic.network.sessions.resetLocal |

Новые и отсутствующие ключи метрик

Благодаря улучшенной масштабируемости Grail больше нет необходимости разделять, распределять или предварительно агрегировать данные.

Метрика Metrics Classic `builtin:host.net.bytesRx` представляет байты, полученные хостами в вашей среде, измеряемые в байтах в секунду. Это предварительно агрегированная метрика на основе `builtin:host.net.nic.bytesRx`, которая измеряет байты, полученные парами хост-сетевой интерфейс. Предварительная агрегация помогает оптимизировать запросы и распределять нагрузку при выполнении запросов к классическим метрикам.

Соответственно, следующие два селектора метрик возвращают эквивалентные результаты при использовании Metrics Classic, но запрос к `builtin:host.net.bytesRx` выполняется быстрее (особенно в больших средах), поскольку агрегация на уровне хоста уже выполнена.

```
// запрос предварительно агрегированных данных на уровне хоста


builtin:host.net.bytesRx:splitBy("dt.entity.host"):avg
```

```
// запрос данных на уровне хоста и сетевого интерфейса


builtin:host.net.nic.bytesRx:splitBy("dt.entity.host"):avg
```

Однако Grail уже оптимизирован для таких запросов с высокой кардинальностью. Поскольку предварительно агрегированная метрика `builtin:host.net.bytesRx` больше не нужна, только `builtin:host.net.nic.bytesRx` поддерживается метриками в Grail и может быть запрошена как:

```
timeseries avg(dt.host.net.nic.bytes_rx), by:{dt.entity.host}
```

Запрос метрик расширений в Grail

Существует три вида метрик расширений Metrics Classic:

1. Расширения с префиксом `builtin:tech`
2. Расширения с префиксом `ext:`
3. Расширения без общего префикса

Подробности см. ниже.

#### Тип 1: Метрики расширений с префиксом `builtin:tech`

Метрики [Extension 1.0](../../ingest-from/extensions/develop-your-extensions.md "Разрабатывайте собственные расширения в Dynatrace.") отображаются в Metrics Classic с префиксом `builtin:tech`. В Grail эти метрики отображаются с префиксом `legacy`. Например:

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| legacy.cassandra.KeyCache.Hit.Rate | builtin:tech.cassandra.KeyCache.Hit.Rate |

Это переименование применяется ко всем метрикам [Extension 1.0](../../ingest-from/extensions/develop-your-extensions.md "Разрабатывайте собственные расширения в Dynatrace.") с префиксом `builtin:tech`, за исключением:

* [Метрик общих процессов](#processes), включая все метрики с префиксом `builtin:tech.generic`.
* [Метрик WebSphere](#websphere-application-server), включая все метрики с префиксом `builtin:tech.websphere`.

Это переименование не применяется к технологическим метрикам Metrics Classic, которые могут быть обновлены до [метрик среды выполнения](#runtimes) Grail, включая метрики с префиксами `builtin:tech.jvm`, `builtin:tech.go` и другие.

#### Тип 2: Метрики расширений с префиксом `ext:`

Метрики расширений с префиксом `ext:` предоставляются расширениями OneAgent или ActiveGate, либо являются [классическими метриками для интеграции с AWS](../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md "Интеграция метрик из Amazon CloudWatch.").
Независимо от источника, они ведут себя одинаково.

Их можно найти в Grail согласно следующим правилам переименования:

1. Удалить префикс `ext:`.
2. Преобразовать `camelCase` в `snake_case`.

Как показано в следующих примерах, переименование в snake_case зависит от контекста. `route53resolver` от AWS и другие компоненты являются собственными названиями и не переименовываются:

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| cloud.aws.dx.connection\_error\_count | ext:cloud.aws.dx.connectionErrorCount |
| cloud.aws.route53resolver.inbound\_query\_volume\_sum | ext:cloud.aws.route53resolver.inboundQueryVolumeSum |

#### Тип 3: Метрики расширений без общего префикса

Для них нет специального переименования, и во многих случаях их можно запрашивать как есть.

```
cloud.gcp.cloudfunctions_googleapis_com.function.active_instances:splitBy():avg
```

```
timeseries avg(cloud.gcp.cloudfunctions_googleapis_com.function.active_instances)
```

Метрики расширений со [специальными символами](../../platform/grail/dynatrace-query-language/dql-reference.md#field-naming-rules "Справочник по синтаксису Dynatrace Query Language.") являются исключением. Экранируйте эти метрики обратными кавычками для использования в DQL.

```
com.dynatrace.extension.snmp-generic-cisco-device.cpm.cpu.loadavg."5min":splitBy():avg
```

```
timeseries avg(`com.dynatrace.extension.snmp-generic-cisco-device.cpm.cpu.loadavg.5min`)
```

Запрос пользовательских метрик в Grail

Если вы не можете найти свою пользовательскую метрику в Grail, попробуйте запросить ключ метрики без суффикса `.count`.

Вы можете запрашивать пользовательские метрики как с помощью [селекторов метрик](../../dynatrace-api/environment-api/metric-v2/metric-selector.md "Настройте селектор метрик для Metric v2 API."), так и с помощью DQL. Однако ключ вашей пользовательской метрики может иметь другое имя в запросах DQL. Например, если вы отправляете метрику-счётчик с ключом `coffees.brewed`, как показано ниже с использованием [протокола отправки метрик](../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md "Узнайте, как работает протокол отправки данных для Dynatrace Metrics API.")

```
coffees.brewing count,delta=2
```

Dynatrace создаёт и сохраняет две метрики:

* Классическая метрика `coffees.brewing.count`
* Метрика Grail `coffees.brewing`

Вы можете запросить метрику Grail через DQL, используя исходный ключ метрики:

```
timeseries sum(coffees.brewing)
```

Это отличается от Metrics Classic, [который автоматически добавляет суффикс `.count` к метрикам-счётчикам](../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#format "Узнайте, как работает протокол отправки данных для Dynatrace Metrics API."). Для запроса классической метрики вам по-прежнему нужно использовать ключ `coffees.brewing.count`.

```
coffees.brewing.count:splitBy():value
```

Запрос вычисляемых метрик в Grail

Хотя [вычисляемые метрики сервисов](#calc-service) поддерживаются, другие вычисляемые метрики пока не поддерживаются в Grail.

* [Вычисляемые метрики RUM](../../observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web.md "Создание вычисляемых метрик и пользовательских диаграмм на основе вычисляемых метрик для веб-приложений.") (метрики с префиксом `calc:apps`) не поддерживаются в Grail.
* Вычисляемые метрики Log v1 (метрики с префиксом `calc:log`) не поддерживаются в Grail. См. [Обновление Log Monitoring Classic до Log Management and Analytics](../logs/logs-upgrade/logs-upgrade-to-lma.md "Log Management and Analytics — новейшее решение Dynatrace для мониторинга логов.").

## Биллинг

| Metric key (Grail) | Metric key (Classic) |
| --- | --- |
| dt.billing.foundation\_and\_discovery.usage | builtin:billing.foundation\_and\_discovery.usage |
| dt.billing.full\_stack\_monitoring.usage | builtin:billing.full\_stack\_monitoring.usage |
| dt.billing.infrastructure\_monitoring.usage | builtin:billing.infrastructure\_monitoring.usage |
| dt.billing.runtime\_application\_protection.usage | builtin:billing.runtime\_application\_protection.usage |
| dt.billing.runtime\_vulnerability\_analytics.usage | builtin:billing.runtime\_vulnerability\_analytics.usage |

## Облако

### AWS

Какие метрики AWS из Metrics Classic не поддерживаются в Grail?

### Azure

Какие метрики Azure из Metrics Classic не поддерживаются в Grail?

### Cloud Foundry

Какие метрики Cloud Foundry из Metrics Classic не поддерживаются в Grail?

### VMware

Какие метрики VMware из Metrics Classic не поддерживаются в Grail?

## Контейнеры

Новые метрики контейнеров теперь доступны для клиентов с [DPS](../../license.md "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace."). Новые метрики подчиняются новой модели лицензирования, отличной от текущей модели полного стека на основе хост-единиц.

Доступность метрик:

* Метрики Metrics Classic были прекращены.
* Новые метрики доступны сразу после развёртывания OneAgent.

## Инфраструктура

Подробный список метрик хостов и их доступности см. в разделе [Метрики хостов](../../observe/infrastructure-observability/hosts/reference/metrics.md "Метрики и классические метрики для мониторинга хостов").

### CPU

### DNS

### Диск

### Память

### Сеть

Многие классические метрики сети на уровне хоста могут быть воспроизведены с использованием метрик сети на уровне сетевого интерфейса в Grail. Подробнее см. в разделе [о новых и отсутствующих ключах метрик](#new-and-missing-metric-keys) выше.

### Доступность

### Прочее

## Kubernetes

ActiveGate версии 1.279+

Новые метрики Kubernetes теперь доступны для клиентов с [DPS](../../license.md "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace.") с запуском нового приложения Kubernetes.

Доступность метрик:

* Старые метрики Kubernetes недоступны в Grail.
* Новые метрики Kubernetes доступны сразу после начала мониторинга вашего кластера с помощью [нового приложения Kubernetes](../../observe/infrastructure-observability/kubernetes-app.md "Мониторинг и оптимизация Kubernetes с Dynatrace.").
* Некоторые новые метрики Kubernetes доступны только в Grail. У них нет эквивалента в виде классических метрик.

## Мейнфрейм

### Хост (логический раздел)

### Процесс (подсистема)

### JVM

### WebSphere Application Server

### WebSphere Liberty / z/OS Connect

## Среды выполнения

OneAgent версии 1.283+

Мы изменили доступность технологических метрик в Grail, что может повлиять на прямое соответствие между ключами метрик Metrics Classic и Grail. Нажмите, чтобы узнать больше об изменении.

### Apache

### Go

### IIS

### Java

### NGINX

### .NET

### Node.js

### PHP

## Процессы

Метрики процессов заменяют общие технологические метрики Metrics Classic с префиксом `builtin:tech.generic`.

### Nettracer

## Безопасность

Метрики безопасности были заменены [событиями безопасности](../../secure/threat-observability/concepts.md#security-events "Основные понятия, связанные с Threat Observability"). Соответственно, метрики безопасности не поддерживаются в Grail. Это затрагивает все метрики с префиксом `builtin:security`.

## Сервисы

Мы изменили доступность метрик сервисов в Grail, что может повлиять на прямое соответствие между ключами метрик Metrics Classic и Grail.

### Вычисляемые метрики сервисов

#### Новые измерения

#### Измерения, автоматически преобразованные из шаблонов подстановки классических метрик

#### Неподдерживаемые шаблоны подстановки

### Обработка сообщений

| Metric key (Grail) | Metric key (Classic) | Описание | Единица |
| --- | --- | --- | --- |
| dt.service.messaging.publish.count | None | Количество сообщений, отправленных в очереди или топики. | count |
| dt.service.messaging.receive.count | None | Количество сообщений, полученных из очередей или топиков. | count |
| dt.service.messaging.process.count | None | Количество успешно обработанных сообщений. | count |
| dt.service.messaging.process.failure\_count | None | Количество сообщений, обработка которых завершилась ошибкой. | count |

### Измерения в Grail

Новые метрики для очередей поддерживают следующие измерения.

| Измерение | Описание | Примеры значений |
| --- | --- | --- |
| messaging.destination.name | Имя очереди или топика | `authorQueue`, `orderEvents` |
| dt.entity.service | Идентификатор сервиса | `spring-kafka-producer` |
| messaging.system | Платформа обмена сообщениями | `kafka`, `rabbitmq`, `aws_sqs` |
| aws.account.id | Идентификатор учётной записи AWS | `123456789012` |
| aws.region | Регион AWS | `us-east-1` |
| k8s.cluster.name | Имя кластера Kubernetes | `prod-cluster` |
| k8s.namespace.name | Имя пространства имён Kubernetes | `payment-services` |

### Конечные точки

### Service mesh

## Синтетический мониторинг

### Метрики HTTP-мониторов

### Метрики мониторов браузера

### Метрики сторонних мониторов

### Метрики мониторов сетевой доступности

#### Общие метрики мониторов

#### Общие метрики шагов

#### Общие метрики запросов

#### Метрики ICMP

#### Метрики TCP

#### Метрики DNS

## Неподдерживаемые метрики

Следующие категории метрик Metrics Classic не поддерживаются в Grail:

* Метрики **A2TM**, включая все метрики с префиксом `builtin:a2tm`.
* Метрики **Lima**, включая все метрики с префиксом `builtin:lima`.
* Метрики **Classic Logs**, включая все метрики с префиксом `builtin:log`.
* Метрики **NAM**, включая все метрики с префиксом `builtin:nam`.
* Метрики **Span**, включая все метрики с префиксом `builtin:span`.
* Метрики **RUM Classic**, включая все метрики с префиксом `builtin:apps`. Подробнее см. [Миграция метрик RUM](upgrade/rum-metric-migration.md "Узнайте, как классические метрики RUM соответствуют их логическим эквивалентам в Grail.").
