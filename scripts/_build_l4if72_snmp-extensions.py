# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../data-sources/snmp-extensions.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources"

TRANS = {
    "* Reference": "* Справочник",
    "* 2-min read": "* Чтение: 2 мин",
    "* Updated on Mar 22, 2023": "* Обновлено 22 марта 2023 г.",
    "Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP monitored devices.": "Dynatrace предоставляет платформу для расширения наблюдаемости за счёт данных, получаемых непосредственно с устройств, отслеживаемых по SNMP.",
    'We also provide an SNMP traps data source reporting a single metric that counts the number of traps sent by a defined source during a defined interval. For more information, see [SNMP traps data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmptraps-extensions "Create an SNMP traps extension using the Dynatrace Extensions framework.").': 'Также предоставляется источник данных SNMP traps, сообщающий единственную метрику с количеством trap-сообщений, отправленных указанным источником за заданный интервал. Подробнее см. в разделе [Источник данных SNMP traps](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmptraps-extensions "Create an SNMP traps extension using the Dynatrace Extensions framework.").',
    "We assume the following:": "Предполагается следующее:",
    "* You possess sufficient SNMP subject matter expertise to create an SNMP extension.": "* У вас достаточно знаний в области SNMP для создания расширения SNMP.",
    '* You\'re familiar with [Extensions basic concepts](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").': '* Вы знакомы с [базовыми концепциями Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") и общей структурой [файла extension YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").',
    'Learn the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").': 'Ознакомьтесь с предварительными требованиями и перечнем поддерживаемых технологий. Сведения об ограничениях, применяемых к расширениям, см. в разделе [Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").',
    "## Supported Dynatrace versions": "## Поддерживаемые версии Dynatrace",
    "* Dynatrace version 1.215+": "* Dynatrace версии 1.215 и выше",
    "* Environment ActiveGate version 1.215+": "* ActiveGate версии 1.215 и выше",
    "## Supported SNMP versions": "## Поддерживаемые версии SNMP",
    "* SNMP v2c": "* SNMP v2c",
    "* SNMP v3": "* SNMP v3",
    "## Supported authentication": "## Поддерживаемая аутентификация",
    "### SNMP v2c": "### SNMP v2c",
    "Community strings.": "Строки community.",
    "### SNMP v3": "### SNMP v3",
    "For SNMP v3, the SNMP data source supports the `NoAuthNoPriv`, `authNoPriv`, and `authPriv` security levels and the following authentication protocols:": "Для SNMP v3 источник данных SNMP поддерживает уровни безопасности `NoAuthNoPriv`, `authNoPriv` и `authPriv`, а также следующие протоколы аутентификации:",
    "#### `authNoPriv`": "#### `authNoPriv`",
    "| Protocol |  | RFC |": "| Протокол |  | RFC |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| MD5 | HMAC-96-MD5 | [rfc3414](https://tools.ietf.org/html/rfc3414) |": "| MD5 | HMAC-96-MD5 | [rfc3414](https://tools.ietf.org/html/rfc3414) |",
    "| SHA | HMAC-96-SHA | [rfc3414](https://tools.ietf.org/html/rfc3414) |": "| SHA | HMAC-96-SHA | [rfc3414](https://tools.ietf.org/html/rfc3414) |",
    "| SHA224 | HMAC-128-SHA-224 | [rfc7860](https://tools.ietf.org/html/rfc7860) |": "| SHA224 | HMAC-128-SHA-224 | [rfc7860](https://tools.ietf.org/html/rfc7860) |",
    "| SHA256 | HMAC-192-SHA-256 | [rfc7860](https://tools.ietf.org/html/rfc7860) |": "| SHA256 | HMAC-192-SHA-256 | [rfc7860](https://tools.ietf.org/html/rfc7860) |",
    "| SHA384 | HMAC-256-SHA-384 | [rfc7860](https://tools.ietf.org/html/rfc7860) |": "| SHA384 | HMAC-256-SHA-384 | [rfc7860](https://tools.ietf.org/html/rfc7860) |",
    "| SHA512 | HMAC-384-SHA-512 | [rfc7860](https://tools.ietf.org/html/rfc7860) |": "| SHA512 | HMAC-384-SHA-512 | [rfc7860](https://tools.ietf.org/html/rfc7860) |",
    "#### `authPriv`": "#### `authPriv`",
    "| Protocol |  | RFC | Notes |": "| Протокол |  | RFC | Примечания |",
    "| --- | --- | --- | --- |": "| --- | --- | --- | --- |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| DES | CBC-DES | [rfc3414](https://tools.ietf.org/html/rfc3414) |  |": "| DES | CBC-DES | [rfc3414](https://tools.ietf.org/html/rfc3414) |  |",
    "| AES | CFB128-AES-128 | [rfc3826](https://tools.ietf.org/html/rfc3826) |  |": "| AES | CFB128-AES-128 | [rfc3826](https://tools.ietf.org/html/rfc3826) |  |",
    "| AES192[1](#fn-1-1-def) |  | n/a | Blumenthal key extension |": "| AES192[1](#fn-1-1-def) |  | n/a | Расширение ключа Blumenthal |",
    "| AES256[1](#fn-1-1-def) |  | n/a | Blumenthal key extension |": "| AES256[1](#fn-1-1-def) |  | n/a | Расширение ключа Blumenthal |",
    "| AES192C[1](#fn-1-1-def) |  | n/a | Reeder key extension |": "| AES192C[1](#fn-1-1-def) |  | n/a | Расширение ключа Reeder |",
    "| AES256C[1](#fn-1-1-def) |  | n/a | Reeder key extension |": "| AES256C[1](#fn-1-1-def) |  | n/a | Расширение ключа Reeder |",
    "1": "1",
    "These encryption algorithms are not officially specified, but they are often supported by network devices. See [SNMPv3 with AES-256](https://www.snmp.com/snmpv3/snmpv3_aes256.shtml).": "Данные алгоритмы шифрования не входят в официальную спецификацию, однако часто поддерживаются сетевыми устройствами. См. [SNMPv3 with AES-256](https://www.snmp.com/snmpv3/snmpv3_aes256.shtml).",
    'To learn how to define authentication in your monitoring configuration, see [SNMP authentication](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmp-schema-reference#authentication "Learn about SNMP extensions in the Extensions framework.").': 'Сведения об определении аутентификации в конфигурации мониторинга см. в разделе [Аутентификация SNMP](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmp-schema-reference#authentication "Learn about SNMP extensions in the Extensions framework.").',
    "## Hardware requirements": "## Требования к оборудованию",
    "SNMP monitoring with the Extensions framework is performed by an ActiveGate. The requirements for the hosts depend on the following:": "Мониторинг SNMP с помощью платформы Extensions выполняется через ActiveGate. Требования к хостам зависят от следующих факторов:",
    "* Number of polled devices.": "* Количество опрашиваемых устройств.",
    "* Number of metric ingestion protocol lines ingested per polling interval (1 minute). A unique metric-dimension combination (tuple) results in a single line.": "* Количество строк протокола приёма метрик, принятых за интервал опроса (1 минута). Уникальная комбинация метрики и измерения (кортеж) формирует одну строку.",
    '* Whether you configured the [EEC](/managed/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.") performance profile to high limits.': '* Настроен ли профиль производительности [EEC](/managed/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.") на высокие лимиты.',
    "Depending on the number of devices and ingested lines, the ActiveGates performing SNMP monitoring need to meet the following hardware requirements:": "В зависимости от количества устройств и принятых строк к ActiveGate, выполняющим мониторинг SNMP, предъявляются следующие требования к оборудованию:",
    "| Host (EC2 instance type) | CPUs | RAM (GB) | SNMP devices | Ingested lines |": "| Хост (тип EC2) | Процессоры | ОЗУ (ГБ) | Устройства SNMP | Принятые строки |",
    "| XS (`c5.large`) | 2 | 4 | 900 | 142,000 |": "| XS (`c5.large`) | 2 | 4 | 900 | 142 000 |",
    "| S (`c5.xlarge`) | 4 | 8 | 1,800 | 284,000 |": "| S (`c5.xlarge`) | 4 | 8 | 1 800 | 284 000 |",
    "| M (`c5.2xlarge`) | 8 | 16 | 4,000 | 632,000 |": "| M (`c5.2xlarge`) | 8 | 16 | 4 000 | 632 000 |",
    "| L (`c5.4xlarge`) | 16 | 32 | 6,000 | 940,000 |": "| L (`c5.4xlarge`) | 16 | 32 | 6 000 | 940 000 |",
    "The estimated limits for the numbers of SNMP devices and ingested lines were determined in our internal tests. The actual values might vary depending on the complexity of your monitoring.": "Расчётные пределы по количеству устройств SNMP и принятых строк определены в ходе внутреннего тестирования. Фактические значения могут отличаться в зависимости от сложности конфигурации мониторинга.",
    "For example, the SNMP devices used in our tests were equipped with 20 communication interfaces. The actual number of interfaces has a direct impact on CPU usage and memory consumption.": "Например, устройства SNMP, использованные в тестах, были оснащены 20 коммуникационными интерфейсами. Фактическое число интерфейсов напрямую влияет на загрузку процессора и потребление памяти.",
}

PASS = {
    "title: SNMP data source",
    "# SNMP data source",
    "source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions",
}

if __name__ == "__main__":
    build_one(REL, "snmp-extensions.md", TRANS, PASS)
    qa_one(REL, "snmp-extensions.md")
