---
title: Прием syslog с ActiveGate
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog
scraped: 2026-03-06T21:34:22.153555
---

# Приём syslog через ActiveGate


* Latest Dynatrace

ActiveGate версии 1.295+ (рекомендуется)

Syslog (сокращение от System Logging Protocol) -- это механизм журналирования, который позволяет системным администраторам контролировать и управлять файлами журналов из различных компонентов системы, таких как сетевые устройства, хосты Linux, серверы syslog или другие источники syslog.

В этом руководстве показано, как настроить Environment ActiveGate на Linux для сбора журналов syslog в вашей сети и их приёма в Dynatrace.

## Предварительные требования

* Environment ActiveGate версии 1.295+ на Linux, установленный для [мониторинга удалённых технологий](../../../ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose.md "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
* Ваши сетевые устройства имеют включённый syslog, или в вашей сети настроены другие источники syslog. Подробности см. в RFC 3164 и RFC 5424. Dynatrace поддерживает широкий спектр реализаций syslog, включая RSysLog, Syslog-NG, NXLog и другие.
* По умолчанию принимаемые syslog-записи должны быть в формате, определённом RFC 3164 и RFC 5424. Если ваши устройства создают нестандартные записи syslog, необходимо преобразовать их в поддерживаемый формат с помощью [обработки Dynatrace OpenPipeline](#process-non-standard-syslog).

  RFC 3164 требует настройки приёмника. Подробности см. в шаге **Редактирование конфигурации приёмника syslog** в разделе [Включение приёма syslog](#enable-syslog-ingestion).

## Аппаратные требования

Приём syslog выполняется ActiveGate. Пропускная способность приёма syslog зависит от оборудования, на котором развёрнут ваш ActiveGate.

| Процессоры | ОЗУ (ГБ) | Максимальная пропускная способность |
| --- | --- | --- |
| 4 | 16 | ~1 ТБ/день |
| 8 | 32 | ~2,7 ТБ/день |

## Целевая аудитория

Это руководство предназначено для сетевых администраторов и администраторов Dynatrace, которым поручено включить приём журналов syslog в Dynatrace.

## Включение приёма syslog

Для включения приёма syslog:

1. **Разверните Environment ActiveGate**.

   Разверните Environment ActiveGate в месте, обеспечивающем связность между ActiveGate и отслеживаемыми устройствами. См. инструкции для [Linux](../../../ingest-from/dynatrace-activegate/installation/linux.md "Узнайте, как установить ActiveGate на Windows, настроить установку и многое другое."), используя назначение [мониторинга удалённых технологий](../../../ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose.md "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
2. **Включите приём syslog на вашем ActiveGate**.

   Добавьте следующий флаг в файл `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`:

   ```
   syslogenabled=true
   ```
3. Необязательно. **Отредактируйте конфигурацию приёмника syslog**.

   ActiveGate использует встроенный экземпляр Dynatrace OpenTelemetry Collector и хранит конфигурацию приёмника в файле `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml`. Collector устанавливается по умолчанию.

   Используйте эту конфигурацию только для приёма syslog.

   Если ваши источники syslog используют порты по умолчанию для поддерживаемых протоколов, ваш ActiveGate с включённым syslog должен начать получать записи syslog сразу.

   Если ваши источники syslog отправляют события на пользовательские порты или используют протокол syslog RFC 3164, измените конфигурацию приёмника syslog. Подробности см. в [Приём данных syslog с помощью OpenTelemetry Collector](../../../ingest-from/opentelemetry/collector/use-cases/syslog.md "Настройка OpenTelemetry Collector для приёма данных syslog в Dynatrace.").

   Конфигурация приёмника syslog по умолчанию

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

   Не изменяйте [конфигурацию экспортёра](../../../ingest-from/opentelemetry/collector/use-cases/syslog.md#exporters "Настройка OpenTelemetry Collector для приёма данных syslog в Dynatrace."). Она предварительно настроена для пересылки ваших syslog-записей в среду Dynatrace.
4. **Убедитесь, что приём syslog включён**.

   Откройте последний файл журнала `ruxit_extensionmodule_*.log` в каталоге `/var/lib/dynatrace/remotepluginmodule/log/extensions` и убедитесь, что он содержит следующую строку:

   ```
   Otel syslog enabled: true
   ```
5. **Включите syslog на устройствах, которые хотите мониторить**.

   Способ включения syslog зависит от устройства и его платформы, поэтому обратитесь к соответствующей документации.

   Пример: Настройка Rsyslog на Linux Ubuntu для пересылки журналов syslog на удалённый сервер

   Добавьте следующую строку в файл конфигурации демона syslog (`/etc/rsyslog.conf`):

   * UDP

     ```
     *.* @<IP-адрес хоста ActiveGate>:514
     ```
   * TCP

     ```
     *.* @@<IP-адрес хоста ActiveGate>:601
     ```

   Конструкция `*.*` указывает демону пересылать все сообщения на указанный ActiveGate, прослушивающий заданный порт и IP-адрес. `<IP-адрес хоста ActiveGate>` должен указывать на IP-адрес ActiveGate с включённым syslog.

   Дополнительные примеры см. в [Syslog через OpenTelemetry Collector](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/)
6. **Убедитесь, что ActiveGate получает события syslog**.

   После того как ваши источники syslog начнут отправлять записи журналов, откройте последний файл `dynatracesourceotelcollector.*.log` в каталоге `/var/lib/dynatrace/remotepluginmodule/log/extensions/datasources/otelSyslog`.

   Если ActiveGate получает записи журналов, вы должны увидеть записи, как в примере ниже:

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

   Дополнительную информацию по устранению неполадок приёмника syslog см. в [Устранение неполадок Collector](https://opentelemetry.io/docs/collector/troubleshooting/).

Готово! Теперь ваши события, полученные через syslog, обогащены атрибутами хоста и доступны в Grail. Благодаря этому вы можете использовать эти записи syslog для анализа данных с помощью Dynatrace Intelligence, обработки журналов или запросов через DQL.

## Маскирование конфиденциальных данных

Приём syslog через ActiveGate поддерживает [OpenTelemetry Transform Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.136.0/processor/transformprocessor/README.md) и [OpenTelemetry Transformation Language (OTTL)](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.136.0/pkg/ottl/ottlfuncs/README.md) для обработки ваших данных syslog на границе сети, до того как конфиденциальные данные покинут вашу сеть.

Таким образом, вы можете маскировать или хешировать конфиденциальные данные в строках syslog, чтобы никакая конфиденциальная информация не попадала в Dynatrace.

Предположим, номер кредитной карты виден в syslog-записи следующим образом:

```
<14>2 2024-07-19T14:53:55Z example-host 0OOButHPbR 1234 - - New operation for CreditCard 1234567891011124
```

Чтобы замаскировать номер кредитной карты, добавьте следующую конфигурацию в узел [processors](../../../ingest-from/opentelemetry/collector/use-cases/syslog.md#processors "Настройка OpenTelemetry Collector для приёма данных syslog в Dynatrace.") файла `syslog.yaml`. Подробности см. в шаге **Редактирование конфигурации приёмника syslog** в разделе [Включение приёма syslog](#enable-syslog-ingestion).

```
processors:


transform/redact_credict_cart:


log_statements:


- context: log


statements:


- replace_pattern(body, "\\d{15,16}", "REDACTED")
```

Функция `replace_pattern` заменяет номер кредитной карты строкой `REDACTED`. Номер кредитной карты в содержимом определяется шаблоном `body, "\\d{15,16}"`.

## Добавление пользовательских атрибутов

Вы также можете изменить конфигурацию приёмника syslog по умолчанию, если хотите сгруппировать набор различных устройств, настроив их на использование определённого порта. Например, используя очень общие сообщения журналов, вы можете обогатить события syslog, отправляемые на определённые TCP-порты, пользовательскими атрибутами, используя конфигурацию, как в примере ниже.

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

Вы также можете использовать:

* `delete` для исключения определённых атрибутов из приёма.
* `upsert` для вставки нового атрибута в строку журнала, если ключ ещё не существует, или обновления атрибута, если ключ уже существует.

Например, если вы можете прочитать атрибут `net.peer.port`, его значение используется для `custom.remote.port`. В противном случае `custom.report.port` не устанавливается.

```
attributes:


actions:


- key: custom.remote.port


from_attribute: net.peer.port


action: upsert
```

Дополнительную информацию о настройке атрибутов см. в [Attributes Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.136.0/processor/attributesprocessor/README.md).

## Фильтрация данных

Вы можете фильтровать данные syslog для отбрасывания нерелевантных строк журналов и сокращения потребления на границе сети, до того как данные покинут вашу сеть.

Например, давайте проигнорируем строки журналов, классифицированные с syslog facility `21`. Ниже приведён пример такого сообщения syslog.

```
<21> 2024-07-19T14:53:55Z example-host 0OOButHPbR 1234 - - Spam mail
```

Добавьте следующий фильтр в файл `syslog.yaml`. Подробности см. в шаге **Редактирование конфигурации приёмника syslog** в разделе [Включение приёма syslog](#enable-syslog-ingestion).

```
filter/mail:


logs:


log_record:


- attributes["syslog.facility"] == 21
```

В результате все строки журналов с syslog facility `21` больше не принимаются.

## Обработка журналов с помощью парсеров технологических пакетов

Через OpenPipeline вы можете использовать и настраивать технологические пакеты. Технологический пакет -- это библиотека парсеров (правил обработки), которые обрабатывают журналы различных технологий, таких как Java, .NET и Microsoft IIS.

Парсеры помогают улучшить фильтрацию, устранение неполадок, метрики, оповещения и дашборды за счёт эффективного извлечения уровней журналов и релевантных атрибутов. Вы также можете использовать технологические пакеты для структурирования журналов технологий, которые не поддерживаются Dynatrace из коробки.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

Дополнительную информацию см. в [Обработка журналов с помощью парсеров технологических пакетов](../../../platform/openpipeline/use-cases/tutorial-technology-processor.md "Настройка конвейера обработки для структурирования технологических журналов в соответствии с Dynatrace Semantic Dictionary.").

## Обработка нестандартных syslog-записей

Иногда, даже когда принимаемые syslog-записи соответствуют формату, определённому протоколами syslog, они могут немного отклоняться от поддерживаемого стандарта. Например, они могут содержать дополнительный пробел или не иметь метки времени. Чтобы исправить это, преобразуйте такие записи syslog с помощью обработки Dynatrace OpenPipeline.

Когда есть отличия от стандарта syslog, OpenTelemetry Collector не может правильно разобрать такие записи syslog при приёме. Они всё равно пересылаются в Dynatrace, но не разбираются на конечной точке syslog. Из-за этого необработанные сообщения syslog видны в Dynatrace, например, в [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**](../lma-logs-app.md "Поиск, фильтрация и анализ журналов с помощью приложения Dynatrace Logs.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../dashboards-and-notebooks/notebooks.md "Анализ, визуализация и обмен данными наблюдаемости.").

Вы можете ожидать ошибки вроде этой:

```
Failed to process entry {"operator_id": "syslog_input_internal_parser", "operator_type": "syslog_parser", "error": "expecting a Stamp timestamp [col 5]", ...}
```

Чтобы исправить эту проблему, используйте OpenPipeline для разбора нестандартных syslog-записей с помощью встроенного [технологического пакета](#logs-technology-bundle) Syslog.

1. Создание конвейера для обработки

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** > **Pipelines**.
2. Нажмите **Pipeline** и введите имя для вашего нового конвейера, например **Non-standard syslog pipeline**.
3. Перейдите в **Processing** > **Processor** > **Technology bundle**.
4. Из списка выберите технологический пакет **Syslog**, а затем нажмите **Choose** в правом нижнем углу страницы.
5. Скопируйте условие технологического соответствия из раздела **Details**.
6. Нажмите **Save**.

Вы успешно создали конвейер и настроили его с процессором для структурирования записей syslog с помощью технологического пакета Syslog. Новый конвейер находится в списке конвейеров.

2. Маршрутизация данных в конвейер

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** > **Dynamic routing**.
2. Нажмите **Dynamic route** и введите следующие данные:

   * **Name**: описательное имя для нового динамического маршрута, например **Non-standard syslog**.
   * **Matching condition**: условие технологического соответствия, которое вы скопировали ранее.

     ```
     matchesValue(dt.openpipeline.source, "extension:syslog")
     ```
   * **Pipeline**: конвейер syslog, который вы создали ранее, например **Non-standard syslog pipeline**.
3. Нажмите **Add**.
4. Расположите новый динамический маршрут в правильной позиции в списке.
5. Нажмите **Save**.

Вы успешно настроили новый динамический маршрут. Все журналы syslog маршрутизируются в конвейер для обработки. Новый маршрут находится в списке маршрутов.

Подробнее о динамической маршрутизации см. в [Маршрутизация данных](../../../platform/openpipeline/getting-started/how-to-routing.md "Узнайте, как маршрутизировать данные в конвейер обработки OpenPipeline.").

3. Добавление пользовательских атрибутов

Необязательно

Вы можете обогащать syslog-записи при приёме пользовательскими атрибутами, что позволяет маршрутизировать различные потоки syslog в отдельные конвейеры. Подробности см. в [Добавление пользовательских атрибутов](#add-custom-attributes).

Дополнительные инструкции и информацию об анализе структурированных журналов см. в [Обработка журналов с помощью парсеров технологических пакетов](../../../platform/openpipeline/use-cases/tutorial-technology-processor.md "Настройка конвейера обработки для структурирования технологических журналов в соответствии с Dynatrace Semantic Dictionary.").

## Устранение неполадок

Посетите Dynatrace Community для руководств по устранению неполадок, а также см. [Устранение неполадок Log Management and Analytics](../lma-troubleshooting.md "Исправление проблем, связанных с настройкой и конфигурацией Log Management and Analytics.").

* [Руководство по устранению неполадок приёма Syslog через ActiveGate](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Устранение неполадок приёма Syslog](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)
