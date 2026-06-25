---
title: Приём syslog через ActiveGate (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/syslog
scraped: 2026-05-12T12:00:29.234656
---

# Приём syslog через ActiveGate (Logs Classic)

# Приём syslog через ActiveGate (Logs Classic)

* Учебное руководство
* Чтение: 4 мин
* Обновлено 08 октября 2025 г.
* Предварительный просмотр

Предварительный просмотр ActiveGate версии 1.293+ Log Monitoring Classic

Предварительный просмотр

Это предварительная версия. Текущая конфигурация полностью совместима с будущими версиями, однако при общей доступности функции ожидается более высокая устойчивость к всплескам трафика и более надёжная обработка сбоев соединения.

Syslog (system logging protocol — протокол системного журналирования) — механизм ведения журналов, позволяющий системным администраторам управлять файлами журналов от различных компонентов системы: сетевых устройств, syslog-хостов Linux, syslog-серверов и других источников syslog.

Это руководство описывает настройку Environment ActiveGate на Linux для сбора syslog-журналов в сети и их приёма в Dynatrace.

## Предварительные требования

* Environment ActiveGate версии 1.293+ на Linux, установленный для [мониторинга удалённых технологий](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
* Сетевые устройства с включённым syslog или другие источники syslog, настроенные в сети. Обратитесь к RFC3164 и RFC5424 для подробностей. Dynatrace поддерживает широкий спектр реализаций syslog, включая RSysLog, Syslog-NG, NXLog и другие.

## Для кого предназначено это руководство?

Руководство предназначено для сетевых администраторов и администраторов Dynatrace, задача которых — включить приём syslog-журналов в Dynatrace.

## Включение приёма syslog

Включение приёма syslog-журналов требует:

* Развёртывания Environment ActiveGate в месте, обеспечивающем связность между ActiveGate и отслеживаемыми устройствами.
* Включения приёма syslog на ActiveGate.
* Опционально: адаптации конфигурации приёмника syslog по умолчанию.

1. **Разверните Environment ActiveGate**.

   Инструкции для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux "Узнайте, как установить ActiveGate на Windows, настроить установку и другое."). Используйте назначение [мониторинга удалённых технологий](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
2. **Включите приём syslog на ActiveGate**.

   Отредактируйте файл `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf` и добавьте следующий флаг:

   ```
   syslogenabled=true
   ```
3. Опционально **Отредактируйте конфигурацию приёмника syslog**.

   ActiveGate использует встроенный экземпляр Dynatrace OpenTelemetry Collector и хранит конфигурацию приёмника в файле `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml`. Collector устанавливается по умолчанию.

   Используйте эту конфигурацию только для приёма syslog.

   Если источники syslog используют порты по умолчанию для поддерживаемых протоколов, ActiveGate с включённым syslog должен сразу начать получать записи syslog.

   Конфигурацию нужно изменять только если источники syslog отправляют события на нестандартные порты.

   ```
   receivers:



   syslog/udp:



   udp:



   listen_address: '0.0.0.0:514'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   syslog/tcp:



   tcp:



   listen_address: '0.0.0.0:601'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   #  syslog/tcp_tls:



   #    tcp:



   #      listen_address: "0.0.0.0:6514"



   #      tls:



   #        cert_file: "/absolute/path/to/server.crt"



   #        key_file: "/absolute/path/to/server.key"



   #    protocol: rfc5424



   #    operators:



   #      - type: syslog_parser



   #        protocol: rfc5424



   #DO.NOT.MODIFY



   exporters:



   otlp_http/syslog: ${file:syslogendpoint.yaml}



   processors:



   batch:



   send_batch_size: 512



   send_batch_max_size: 1024



   transform:



   log_statements:



   - context: log



   statements:



   - set(body, attributes["message"])



   attributes:



   actions:



   - key: net.host.name



   action: delete



   - key: net.peer.name



   action: delete



   - key: net.peer.port



   action: delete



   - key: net.transport



   action: delete



   - key: net.host.ip



   action: delete



   - key: dt.ingest.port



   from_attribute: net.host.port



   action: upsert



   - key: dt.ingest.source.ip



   from_attribute: net.peer.ip



   action: upsert



   - key: net.peer.ip



   action: delete



   - key: net.host.port



   action: delete



   - key: syslog.hostname



   from_attribute: hostname



   action: upsert



   - key: hostname



   action: delete



   - key: syslog.facility



   from_attribute: facility



   action: upsert



   - key: facility



   action: delete



   - key: syslog.priority



   from_attribute: priority



   action: upsert



   - key: priority



   action: delete



   - key: syslog.proc_id



   from_attribute: proc_id



   action: upsert



   - key: proc_id



   action: delete



   - key: syslog.version



   from_attribute: version



   action: upsert



   - key: version



   action: delete



   - key: syslog.appname



   from_attribute: appname



   action: upsert



   - key: appname



   action: delete



   - key: message



   action: delete



   service:



   telemetry:



   metrics:



   level: none



   pipelines:



   logs/udp:



   receivers: [syslog/udp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   logs/tcp:



   receivers: [syslog/tcp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   #    logs/tcp_tls:



   #      receivers: [syslog/tcp_tls]



   #      processors: [transform, attributes, batch]



   #      exporters: [otlp_http/syslog]
   ```

   Конфигурацию по умолчанию также можно изменить для группировки набора различных устройств, настроив их использование определённого порта.

   **Примечание**: НЕ изменяйте конфигурацию экспортёра. Конфигурация по умолчанию указывает на встроенный Collector.

   Подробнее о конфигурации приёмника syslog: [Приём данных syslog с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.").
4. **Убедитесь, что приём syslog включён**.

   После включения приёма syslog проверьте следующие файлы журналов:

   Откройте новейший файл `ruxit_extensionmodule_*.log` в директории журналов `extensions`:

   * Linux: `/var/lib/dynatrace/remotepluginmodule/log/extensions`

   Он должен содержать следующую строку:

   ```
   Otel syslog enabled: true
   ```
5. **Включите syslog на устройствах, которые нужно отслеживать**.

   Способ включения syslog зависит от устройства и его платформы, обратитесь к соответствующей документации.

   **Пример**
   Настройка Rsyslog на Linux Ubuntu для пересылки syslog-журналов на удалённый сервер.

   Добавьте следующую строку в конфигурационный файл syslog-демона (`/etc/rsyslog.conf`)

   * UDP

     ```
     *.* @<ActiveGate host IP>:514
     ```
   * TCP

     ```
     *.* @@<ActiveGate host IP>:601
     ```

   `*.*` указывает демону пересылать все сообщения на указанный ActiveGate, прослушивающий указанный порт и IP-адрес. `<ActiveGate host IP>` должен указывать на IP-адрес ActiveGate с включённым syslog.

   Дополнительные примеры: [Syslog via OpenTelemetry Collector](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/).
6. **Убедитесь, что ActiveGate получает события syslog**.

   После того как источники syslog начнут отправлять записи журналов, откройте последний файл `dynatracesourceotelcollector.*.log` в `/var/lib/dynatrace/remotepluginmodule/agent/datasources/otelSyslog`.

   При получении записей журналов ActiveGate должны появляться записи как в примере ниже:

   ```
   [otelSyslog][otelSyslog][37448][err]LogRecord #3



   [otelSyslog][oteiSyslog][37448][err]ObservedTimestamp: 2024-05-06 @9:52:10.6748723 +8000 UTC



   [otelSyslog][otelSyslog][37448][err]Timestamp: 2624-05-@6 11:52:16 +90e0 UTC



   [otelSyslog][otelsyslog][37448][err]SeverityText: info



   [otelSyslog][otelSyslog][37443][err]SeverityNumber: Info(9)



   [otelSyslog][otelSyslog][37448][err]Body: Str(<30>May 6 11:52:10 SOME-HOST systemd[1]: Finished    Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Attributes:



   [otelSyslog][otelSyslog][37448][err]    -> priority: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> facility: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> appname: Str(systemd)



   [otelSyslog][otelSyslog][37448][err]    -> proc_id: Str(1)



   [otelSyslog][otelSyslog][37443][err]    -> log: Map({"source": "syslog"})



   [otelSyslog][otelSyslog][37443][err]    -> hostname: Str(SOME-HOST)



   [otelSyslog][otelSyslog][37443][err]    -> message: Str(Finished Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Trace ID:



   [otelSyslog][otelSyslog][37448][err]Span ID:



   [otelSyslog][otelSyslog][37443][err]Flags: 0
   ```

Подробнее об устранении неполадок приёмника syslog: [Collector troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/).

## Следующие шаги

После включения интеграции принятые через syslog события обогащаются специфичными для хоста атрибутами и становятся доступны для мониторинга и обработки журналов.

## Устранение неполадок

Посетите сообщество Dynatrace, а также ознакомьтесь с разделом [Устранение неполадок Log Monitoring (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Устраните проблемы, связанные с настройкой и конфигурацией Log Monitoring Classic.").

* [Syslog Ingestion via ActiveGate Troubleshooting Guide](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshooting](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)