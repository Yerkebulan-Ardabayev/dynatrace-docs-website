---
title: Syslog ingestion with ActiveGate (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog
scraped: 2026-03-05T21:37:13.258846
---

# Приём syslog с помощью ActiveGate (Logs Classic)

# Приём syslog с помощью ActiveGate (Logs Classic)

* Classic
* Руководство
* Время чтения: 4 мин
* Обновлено 8 октября 2025 г.
* Предварительная версия

Предварительная версия ActiveGate версии 1.293+ Log Monitoring Classic

Предварительная версия

Это предварительный релиз. Ваша текущая конфигурация полностью совместима с будущими версиями, но вы можете ожидать более высокую устойчивость к пиковым нагрузкам и лучшую обработку разрывов подключений, когда функция станет общедоступной.

Для новейшей версии Dynatrace см. [Приём syslog с помощью ActiveGate](../../logs/lma-log-ingestion/lma-log-ingestion-syslog.md "Принимайте данные логов syslog в Dynatrace с помощью ActiveGate и позвольте Dynatrace преобразовать их в содержательные сообщения логов.").

Syslog (системный протокол журналирования) — это механизм журналирования, позволяющий системным администраторам контролировать и управлять файлами логов из различных компонентов системы, таких как сетевые устройства, syslog хоста Linux, серверы syslog или другие источники syslog.

Это руководство показывает, как настроить ваш Environment ActiveGate на Linux для сбора логов syslog в вашей сети и их приёма в Dynatrace.

## Предварительные требования

* Environment ActiveGate версии 1.293+ на Linux, установленный для [мониторинга удалённых технологий](../../../ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose.md "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
* Ваши сетевые устройства имеют включённый syslog или в вашей сети настроены другие источники syslog. Обратитесь к RFC3164 и RFC5424 для подробностей. Dynatrace поддерживает широкий спектр реализаций syslog, включая RSysLog, Syslog-NG, NXLog и другие.

## Для кого предназначено это руководство?

Это руководство предназначено для сетевых администраторов и администраторов Dynatrace, которым поручено включить приём логов syslog в Dynatrace.

## Включение приёма syslog

Включение приёма логов syslog требует от вас:

* Развернуть Environment ActiveGate в месте, обеспечивающем связь между ActiveGate и контролируемыми устройствами.
* Включить приём syslog на ActiveGate.
* Необязательно в некоторых случаях вам потребуется адаптировать конфигурацию приёмника syslog по умолчанию.

1. **Развернуть Environment ActiveGate**.

   См. инструкции для [Linux](../../../ingest-from/dynatrace-activegate/installation/linux.md "Узнайте, как установить ActiveGate на Windows, настроить установку и другое."). Используйте назначение [мониторинг удалённых технологий](../../../ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose.md "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
2. **Включить приём syslog на вашем ActiveGate**.

   Отредактируйте файл `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf` и добавьте следующий флаг:

   ```
   syslogenabled=true
   ```
3. Необязательно **Отредактировать конфигурацию приёмника syslog**.

   ActiveGate использует встроенный экземпляр Dynatrace OpenTelemetry Collector и хранит конфигурацию приёмника в файле `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml`. Collector устанавливается по умолчанию.

   Используйте эту конфигурацию только для приёма syslog.

   Если ваши источники syslog используют порты по умолчанию для поддерживаемых протоколов, ваш ActiveGate с включённым syslog должен получать записи syslog сразу.

   Вам нужно изменить конфигурацию только если ваши источники syslog отправляют события на пользовательские порты.

   Показать содержимое файла...

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

   Вы также можете изменить конфигурацию по умолчанию, если хотите сгруппировать набор различных устройств, настроив их на использование определённого порта. Например, вы можете обогатить события syslog, отправляемые на определённые TCP-порты, используя конфигурацию, как в примере ниже

   ```
   receivers:



   syslog/f5:



   tcp:



   listen_address: "0.0.0.0:54526"



   protocol: rfc5424



   operators:



   - type: add



   field: attributes.log.source



   value: syslog



   - type: add



   field: attributes.dt.ip_addresses



   value: "1xx.xx.xx.xx1"



   - type: add



   field: attributes.instance.name



   value: "ip-1xx-xx-x-xx9.ec2.internal"



   - type: add



   field: attributes.device.type



   value: "f5bigip"



   syslog/host:



   tcp:



   listen_address: "0.0.0.0:54527"



   protocol: rfc5424



   operators:



   - type: add



   field: attributes.log.source



   value: syslog



   - type: add



   field: attributes.device.type



   value: "ubuntu-syslog"
   ```

   **Примечание**: НЕ изменяйте конфигурацию экспортёра. Конфигурация по умолчанию указывает на встроенный Collector.

   Дополнительные сведения о конфигурации приёмника syslog см. в разделе [Приём данных syslog с помощью OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector/use-cases/syslog.md "Настройте OpenTelemetry Collector для приёма данных syslog в Dynatrace.").
4. **Проверить включение приёма syslog**.

   После включения приёма syslog проверьте следующие файлы логов для подтверждения:

   Откройте новейший файл лога `ruxit_extensionmodule_*.log` в каталоге логов `extensions`:

   * Linux: `/var/lib/dynatrace/remotepluginmodule/log/extensions`

   Он должен содержать следующую строку:

   ```
   Otel syslog enabled: true
   ```
5. **Включить syslog на устройствах, которые вы хотите мониторить**.

   Способ включения syslog зависит от устройства и его платформы, обратитесь к соответствующей документации для получения подробностей.

   **Пример**
   Настройка Rsyslog на Linux Ubuntu для пересылки логов syslog на удалённый сервер.

   Добавьте следующую строку в файл конфигурации демона syslog (`/etc/rsyslog.conf`)

   * UDP

     ```
     *.* @<ActiveGate host IP>:514
     ```
   * TCP

     ```
     *.* @@<ActiveGate host IP>:601
     ```

   `*.*` указывает демону пересылать все сообщения на указанный ActiveGate, прослушивающий предоставленный порт и IP-адрес. `<ActiveGate host IP>` должен указывать на IP-адрес ActiveGate с включённым syslog.

   Дополнительные примеры см. в разделе [Syslog через OpenTelemetry Collector](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/)
6. **Проверить получение событий syslog ActiveGate**.

   После того как ваши источники syslog начнут отправлять записи логов, откройте последний файл `dynatracesourceotelcollector.*.log` в `/var/lib/dynatrace/remotepluginmodule/agent/datasources/otelSyslog`.

   Если ActiveGate получает записи логов, вы должны увидеть записи, аналогичные примеру ниже:

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

Дополнительные сведения об устранении неполадок приёмника syslog см. в разделе [Устранение неполадок Collector](https://opentelemetry.io/docs/collector/troubleshooting/).

## Следующие шаги

После включения интеграции события, принятые через syslog, обогащаются атрибутами, специфичными для хоста, и становятся доступными для мониторинга и обработки логов.

## Устранение неполадок

Посетите сообщество Dynatrace для ознакомления с руководствами по устранению неполадок, а также см. [Устранение неполадок Log Monitoring (Logs Classic)](../lmc-troubleshooting.md "Устранение проблем, связанных с настройкой и конфигурацией Log Monitoring Classic.").

* [Руководство по устранению неполадок приёма Syslog через ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Устранение неполадок приёма Syslog](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)
