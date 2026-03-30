---
title: Получение Syslog с помощью ActiveGate (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog
scraped: 2026-03-05T21:37:13.258846
---

* 4 мин на чтение
* Предварительная версия

Предварительная версия ActiveGate версии 1.293+ Log Monitoring Classic

Предварительная версия

Это предварительная версия. Ваша текущая конфигурация полностью совместима с будущими версиями, но вы можете ожидать более высокой устойчивости к пикам трафика и лучшей обработки разрывов соединения, когда функция станет общедоступной.

Для самой новой Dynatrace версии, смотрите Получение Syslog с помощью ActiveGate.

Syslog, сокращение от system logging protocol (протокол системного журналирования), — это механизм журналирования, который позволяет системным администраторам контролировать и управлять файлами журналов от различных системных компонентов, таких как сетевые устройства, syslog хоста Linux, syslog-серверы или другие производители syslog.

Это руководство показывает, как настроить ваш Environment ActiveGate на Linux для сбора журналов syslog в вашей сети и передачи их в Dynatrace.

## Необходимые условия

* Environment ActiveGate версии 1.293+ на Linux, установленный для мониторинга удаленных технологий.
* На ваших сетевых устройствах включен syslog или у вас настроены другие производители syslog в вашей сети. Обратитесь к RFC3164 и RFC5424 для получения подробностей. Dynatrace поддерживает широкий спектр реализаций syslog, включая RSysLog, Syslog-NG, NXLog и другие.

## Для кого это предназначено?

Это руководство предназначено для сетевых администраторов и администраторов Dynatrace, которым поручено включить получение журналов syslog в Dynatrace.

## Включить получение Syslog

Включение приема журналов syslog требует выполнения следующих действий:

* Разверните Environment ActiveGate в месте, обеспечивающем связь между ActiveGate и контролируемыми устройствами.
* Включите прием журналов syslog на ActiveGate.
* В некоторых случаях, возможно, потребуется адаптировать конфигурацию приемника syslog по умолчанию.

1. **Разверните Environment ActiveGate**.

   Ознакомьтесь с инструкциями по Linux. Используйте назначение мониторинга удаленных технологий.
2. **Включите прием журналов syslog на вашем ActiveGate**.

   Отредактируйте файл `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf` и добавьте следующий флаг:

   ```
   syslogenabled=true
   ```
3. Необязательно **Отредактируйте конфигурацию приемника syslog**.

   ActiveGate использует встроенный экземпляр Dynatrace OpenTelemetry Collector и хранит конфигурацию приемника в файле `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml`. Collector установлен по умолчанию.

   Используйте эту конфигурацию только для приема журналов syslog.

   Если ваши производители syslog используют порты по умолчанию для поддерживаемых протоколов, ваш ActiveGate с включенным syslog должен сразу же получать записи журналов syslog.

   Вам нужно будет изменить конфигурацию только в том случае, если ваши производители syslog передают события на пользовательские порты.

   Покажите мне файл…

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

   Вы также можете изменить конфигурацию по умолчанию, если хотите сгруппировать набор различных устройств, настроив их на использование определенного порта. Например, вы можете обогатить события syslog, передаваемые на определенные TCP-порты, используя конфигурацию, как в примере ниже:

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

   **Примечание**: НЕ изменяйте конфигурацию экспортера. Конфигурация по умолчанию указывает на встроенный Collector.

   Для получения дополнительной информации о конфигурации приемника syslog, обратитесь к Прием данных syslog с помощью OpenTelemetry Collector.
4. **Убедитесь, что включен прием журналов syslog**.

   После включения приема журналов syslog проверьте следующие файлы журналов, чтобы убедиться в этом:

   Откройте самый новый файл `ruxit_extensionmodule_*.log` в каталоге журналов `extensions`:

   * Linux: `/var/lib/dynatrace/remotepluginmodule/log/extensions`

   В нем должна содержаться следующая строка:

   ```
   Otel syslog enabled: true
   ```
5. **Включите syslog на устройствах, которые вы хотите контролировать**.

   Способ включения syslog зависит от устройства и его платформы, обратитесь к конкретной документации для получения подробной информации.

   **Пример**
   Настройте Rsyslog на Linux Ubuntu для пересылки журналов syslog на удаленный сервер.

   Добавьте следующую строку в файл конфигурации демона syslog (`/etc/rsyslog.conf`)

   * UDP

     ```
     *.* @<ActiveGate host IP>:514
     ```
   * TCP

     ```
     *.* @@<ActiveGate host IP>:601
     ```

   `*.*` указывает демону пересылать все сообщения на указанный ActiveGate, прослушивающий указанный порт и IP-адрес. `<ActiveGate host IP>` должен указывать на IP-адрес ActiveGate с включенным syslog.

   Для получения дополнительных примеров, обратитесь к [Syslog via OpenTelemetry Collector](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/)
6. **Убедитесь, что ActiveGate получает события syslog**.

   После того, как ваши производители syslog начнут передавать записи журналов, откройте последний файл `dynatracesourceotelcollector.*.log` в `/var/lib/dynatrace/remotepluginmodule/agent/datasources/otelSyslog`.

   Если ActiveGate получает записи журналов, вы должны увидеть записи, как в примере ниже:

   ```
   [otelSyslog][otelSyslog][37448][err]LogRecord #3


   [otelSyslog][oteiSyslog][37448][err]ObservedTimestamp: 2024-05-06 @9:52:10.6748723 +8000 UTC


   [otelSyslog][otelSyslog][37448][err]Timestamp: 2624-05-@6 11:52:16 +90e0 UTC


   [otelSyslog][otelSyslog][37443][err]SeverityText: info


   [otelSyslog][otelSyslog][37448][err]SeverityNumber: Info(9)


   [otelSyslog][otelSyslog][37448][err]Body: Str(<30>May 6 11:52:10 SOME-HOST systemd[1]: Finished    Load Kernel Module fuse.)


   [otelSyslog][otelSyslog][37448][err]Attributes:


   [otelSyslog][otelSyslog][37448][err]    -> priority: Int(3)


   [otelSyslog][otelSyslog][37448][err]    -> facility: Int(3)


   [otelSyslog][otelSyslog][37448][err]    -> appname: Str(systemd)


   [otelSyslog][otelSyslog][37448][err]    -> proc_id: Str(1)


   [otelSyslog][otelSyslog][37443][err]    -> log: Map({â€œsource": â€œsyslog"})


   [otelSyslog][otelSyslog][37443][err]    -> hostname: Str(SOME-HOST)


   [otelSyslog][otelSyslog][37443][err]    -> message: Str(Finished Load Kernel Module fuse.)


   [otelSyslog][otelSyslog][37448][err]Trace ID:


   [otelSyslog][otelSyslog][37448][err]Span ID:


   [otelSyslog][otelSyslog][37443][err]Flags: 0
   ```

Для получения дополнительной информации об устранении неполадок приемника syslog, обратитесь к [Collector troubleshooting](https://opentelemetry.io/docs/collector/troubleshooting/).

## Следующие шаги

После включения интеграции события, полученные из syslog, обогащаются атрибутами, специфичными для хоста, и становятся доступными для мониторинга журналов и обработки.

## Устранение неполадок

Посетите Dynatrace Community для получения руководств по устранению неполадок, а также ознакомьтесь с Устранение неполадок мониторинга журналов (Logs Classic).

* [Руководство по устранению неполадок приема Syslog через ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Устранение неполадок приема Syslog](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)