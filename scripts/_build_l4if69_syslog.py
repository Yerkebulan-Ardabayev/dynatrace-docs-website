# -*- coding: utf-8 -*-
"""L4-IF.69 builder: ingest-from/opentelemetry/collector/use-cases/syslog.md.

Mirrors the filelog/netflow sibling recipes (_build_otel_uc_l4if68.py): shared
boilerplate comes from S; only the lines unique to the syslog recipe are added
here. Component headers ### Receivers/Processors/Exporters are kept EN via PASS.
"""

from _otel_canon import S, SUB, build_one, qa_one

TRANS = {
    # title / H1 (H1 appears twice in source; one key covers both)
    "title: Ingest syslog data with the OTel Collector": "title: Приём данных syslog с помощью OTel Collector",
    "# Ingest syslog data with the OTel Collector": "# Приём данных syslog с помощью OTel Collector",
    # intro
    "The following configuration example shows how to configure a Collector instance to receive data from syslog and send it to the Dynatrace backend.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для приёма данных из syslog и их отправки в бэкенд Dynatrace.",
    # prerequisites: distribution bullet with attributes processor + Syslog receiver
    "* One of the following Collector distributions with the [attributes processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/attributesprocessor) and the [Syslog receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/syslogreceiver):": "* Один из следующих дистрибутивов Collector с [processor attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/attributesprocessor) и [receiver Syslog](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/syslogreceiver):",
    # Receivers section prose
    "Under `receivers`, we specify two instances of the `syslog` receiver as active receiver components for our Collector instance.": "В разделе `receivers` мы указываем два экземпляра receiver `syslog` в качестве активных компонентов receiver для нашего экземпляра Collector.",
    "The Syslog receiver supports a number of [configuration parameters](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/syslogreceiver/README.md), which enable you to customize its behavior. For our example, we use the following:": "Receiver Syslog поддерживает ряд [параметров конфигурации](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/syslogreceiver/README.md), позволяющих настроить его поведение. В нашем примере мы используем следующие:",
    "* `tcp`—Specifies a TCP listener for the receiver and configures ports 54526 and 54527": "* `tcp`: задаёт TCP-приёмник для receiver и настраивает порты 54526 и 54527",
    "* `protocol`—Specifies the RFC 5424 implementation for our receiver (alternatively, RFC 3164 is also supported)": "* `protocol`: задаёт реализацию RFC 5424 для нашего receiver (в качестве альтернативы также поддерживается RFC 3164)",
    "* `operators`—Configures the operators we apply to each log entry. For our example, we use the [add](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/add.md) operator to add additional information.": "* `operators`: настраивает операторы, применяемые к каждой записи лога. В нашем примере мы используем оператор [add](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/add.md) для добавления дополнительной информации.",
    "+ `field`—Specifies the name of value we are adding": "+ `field`: задаёт имя добавляемого значения",
    "+ `value`—Specifies the content of the value we are adding": "+ `value`: задаёт содержимое добавляемого значения",
    # Processors section prose
    "Under `processors`, we configure the `attributes` processor to drop and adjust the indicated attributes in our OTLP request.": "В разделе `processors` мы настраиваем processor `attributes` для удаления и корректировки указанных атрибутов в нашем запросе OTLP.",
    # Service pipelines section prose
    "Under `service`, we eventually assemble our receiver, processor, and exporter objects into a logs pipeline, which uses the receiver instances to obtain syslog data and ingest it into Dynatrace using OTLP.": "В разделе `service` мы в итоге собираем наши объекты receiver, processor и exporter в конвейер логов, который использует экземпляры receiver для получения данных syslog и их приёма в Dynatrace с помощью OTLP.",
    # related topics: leaf-only bullet
    '* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")': '* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")',
    **S,
}

PASS = {"### Receivers", "### Processors", "### Exporters"}

if __name__ == "__main__":
    build_one(SUB, "syslog.md", TRANS, PASS)
    qa_one(SUB, "syslog.md")
