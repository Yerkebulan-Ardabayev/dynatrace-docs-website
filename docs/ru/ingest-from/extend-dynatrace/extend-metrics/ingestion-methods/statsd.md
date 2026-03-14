---
title: Отправка метрик StatsD в Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd
scraped: 2026-03-06T21:16:29.318435
---

# Отправка метрик StatsD в Dynatrace


* Latest Dynatrace
* 5-min read
* Updated on Jun 18, 2025

StatsD — это отраслевой стандарт для передачи произвольной статистики и других метрик вендор-независимым способом через UDP. Мы рекомендуем использовать Dynatrace OneAgent для загрузки ваших метрик, поскольку OneAgent поставляется с демоном StatsD из коробки. Это означает, что любое приложение или библиотека, поддерживающие StatsD, могут отправлять метрики в Dynatrace. Вам нужно лишь установить OneAgent и убедиться, что ваш клиент StatsD использует правильный порт (`18125` по умолчанию).

Поддерживаемый OneAgent

Демон StatsD доступен только на OneAgent, установленном на виртуальной машине или хосте, который вы хотите мониторить. OneAgent, развёрнутый на Kubernetes, например с помощью Dynatrace Operator, не поддерживается. Для сред Kubernetes мы рекомендуем [удалённый мониторинг StatsD](#remote) с использованием ActiveGate среды.

Если вы не можете установить OneAgent на хост с вашими метриками StatsD, вы можете использовать ActiveGate в качестве удалённого слушателя.

## Выберите метод загрузки StatsD

OneAgent

ActiveGate

OpenTelemetry Collector

Используйте OneAgent для прямой установки на хосте со StatsD. Подробнее см. [слушатель OneAgent](#oneagent-listener).

Если OneAgent не может быть установлен на хосте, используйте ActiveGate в качестве удалённого слушателя для сбора метрик StatsD. Подробнее см. [Удалённый StatsD](#remote-statsd).

Для распределённых сред или при использовании Kubernetes OpenTelemetry Collector предоставляет решение для загрузки метрик StatsD в Dynatrace. Подробнее см. [Ingest data from StatsD](../../../opentelemetry/collector/use-cases/statsd.md "Configure the OpenTelemetry Collector to ingest StatsD data.").

## Включение DynatraceStatsD

Слушатель DynatraceStatsD поставляется с OneAgent версии 1.201+. Вам нужно лишь включить загрузку метрик DynatraceStatsD на уровне среды, хоста или группы хостов. Обратите внимание, что конфигурации на уровне хоста и группы хостов переопределяют конфигурацию среды.

Включение на уровне среды

Для включения загрузки метрик DynatraceStatsD на уровне среды

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable Dynatrace StatsD**.

Включение на уровне группы хостов

Для включения загрузки метрик DynatraceStatsD на уровне группы хостов

1. Перейдите в **Settings** и выберите **Monitoring overview** > **Hosts**.
2. Выберите имя группы хостов для выбранного хоста.
3. На странице **Host group settings** выберите **Extension Execution Controller**.
4. Включите **Enable Dynatrace StatsD**.

Включение для отдельного хоста

Для включения загрузки метрик DynatraceStatsD только для выбранных хостов

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Найдите и выберите нужный хост для отображения страницы обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**...**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.
6. Включите **Enable Dynatrace StatsD**.

Включение удалённого StatsD

ActiveGate версии 1.227+

Если вы не можете использовать OneAgent для загрузки метрик StatsD, вы можете использовать ActiveGate среды в качестве точки загрузки DynatraceStatsD. Ваш ActiveGate должен иметь возможность подключения к клиенту StatsD по UDP.

Загрузка метрик DynatraceStatsD по умолчанию отключена на ActiveGate.

Для включения загрузки метрик DynatraceStatsD

1. Отредактируйте файл `extensionsuser.conf` в следующем каталоге

   * Linux
     `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
   * Windows
     `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`
2. Установите параметр `statsdenabled` в `true`:

   ```
   statsdenabled=true
   ```
3. Перезапустите службу Extension Execution Controller.

   * Linux
     Выполните следующие команды:

     + для систем с SystemV:

       ```
       service extensionsmodule stop


       service extensionsmodule start
       ```
     + для систем с systemd:

       ```
       systemctl stop extensionsmodule


       systemctl start extensionsmodule
       ```
   * Windows
     Используйте **Task Manager** и перезапустите службу `Dynatrace Extensions Controller` или выполните следующие команды:

     ```
     net stop "Dynatrace Extensions Controller"


     net start "Dynatrace Extensions Controller"
     ```

Обратите внимание, что порт по умолчанию для удалённого StatsD отличается от порта слушателя DynatraceStatsD на OneAgent (`18126`). См. [Удалённый StatsD](#remote-statsd).

Этот файл не изменяется при обновлении ActiveGate.

Убедитесь, что ваш ActiveGate может подключиться к вашему клиенту StatsD. Например, необходимо настроить DNS-имя для вашего ActiveGate и убедиться, что оно работает после назначения нового IP-адреса через DHCP.

## Порт связи

### Слушатель OneAgent

Порт UDP-прослушивания DynatraceStatsD для слушателя OneAgent по умолчанию — `18125`. При необходимости вы можете использовать команду [oneagentctl](../../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для проверки или изменения порта загрузки метрик. Изменение порта требует перезапуска OneAgent. Добавьте [`--restart-service`](../../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") к команде для автоматического перезапуска OneAgent.

#### Проверка порта загрузки

Используйте параметр `--get-extensions-statsd-port` для отображения текущего UDP-порта прослушивания DynatraceStatsd (по умолчанию = `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Установка пользовательского порта загрузки

Используйте параметр `--set-extensions-statsd-port=<arg>` для установки пользовательского UDP-порта прослушивания DynatraceStatsd.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Удалённый StatsD

Порт UDP-прослушивания DynatraceStatsD для удалённого слушателя по умолчанию — `18126`.

Для изменения порта прослушивания по умолчанию `18126` измените параметр `StatsdPort` в файле `extensionsuser.conf` ActiveGate:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Топологическая осведомлённость

При использовании DynatraceStatsD с OneAgent идентификатор хоста и имя хоста автоматически добавляются в качестве измерений к каждой метрике. Подробнее см. [Metric ingestion](../../extend-metrics.md "Learn how to extend metric observability in Dynatrace."). Обратите внимание, что мы уже работаем над дополнительным автоматическим обогащением метрик. При удалённой загрузке дополнительное обогащение не добавляется. Если вы хотите добавить контекст к вашим метрикам, вам нужно будет самостоятельно добавить измерения к вашим метрикам StatsD.

## Безопасность

Слушатель DynatraceStatsD на OneAgent принимает входящие данные только с адресов localhost. Это означает, что только процессы, работающие на том же хосте, что и OneAgent, могут использовать этот интерфейс. Это гарантирует, что неавторизованные программы не смогут отправлять данные в вашу среду Dynatrace.

## Формат метрик StatsD

DynatraceStatsD принимает следующие метрики в [нативном формате StatsD](https://github.com/statsd/statsd/blob/master/docs/metric_types.md):

* `count`

  ```
  <metric name>:<value>|c
  ```
* `gauge`

  ```
  <metric name>:<value>|g
  ```
* `time`

  ```
  <metric name>:<value>|ms
  ```
* `histogram`

  ```
  <metric name>:<value>|h
  ```
* `set` OneAgent версии 1.303+

  ```
  <metric name>:<value>|s
  ```
* `distribution`

  ```
  <metric name>:<value>|d
  ```

DynatraceStatsD расширяет оригинальный протокол, позволяя также отправлять измерения. Используйте следующий формат:

```
<metric name>:<value>|g|#<Dimension1>:<value>,<Dimension2>:<value>
```

## Ограничения источника данных и производительность

Ограничения основаны на тесте с развёртыванием Linux-машины в облаке AWS. Цель этого теста — определить, какую нагрузку StatsD может обработать инфраструктурный фреймворк.

### Спецификация оборудования

OneAgent и ActiveGate установлены на виртуальной машине на базе Linux в Amazon EC2, тип инстанса [c5.large](https://dt-url.net/rv031ec).

* CPU: x2
* RAM: 4 GiB
* Хранилище: EBS
* Пропускная способность сети: до 10 GBPS

|  | Всего записей | Пакеты | Строк на пакет | Соединения | Метрики |
| --- | --- | --- | --- | --- | --- |
| StatsD на OneAgent | 290,000 | 11,600 | 25 | 1 | 1 |
| StatsD на ActiveGate | 345,000 | 13,800 | 25 | 1 | 1 |
