---
title: Источник данных SNMP
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions
scraped: 2026-05-12T11:50:06.297939
---

# Источник данных SNMP

# Источник данных SNMP

* Справочник
* Чтение: 2 мин
* Обновлено 22 марта 2023 г.

Dynatrace предоставляет платформу для расширения наблюдаемости за счёт данных, получаемых непосредственно с устройств, отслеживаемых по SNMP.

Также предоставляется источник данных SNMP traps, сообщающий единственную метрику с количеством trap-сообщений, отправленных указанным источником за заданный интервал. Подробнее см. в разделе [Источник данных SNMP traps](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmptraps-extensions "Создайте расширение для SNMP traps с помощью платформы Dynatrace Extensions framework.").

Предполагается следующее:

* У вас достаточно знаний в области SNMP для создания расширения SNMP.
* Вы знакомы с [базовыми концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [файла extension YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.").

Ознакомьтесь с предварительными требованиями и перечнем поддерживаемых технологий. Сведения об ограничениях, применяемых к расширениям, см. в разделе [Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.").

## Поддерживаемые версии Dynatrace

* Dynatrace версии 1.215 и выше
* ActiveGate версии 1.215 и выше

## Поддерживаемые версии SNMP

* SNMP v2c
* SNMP v3

## Поддерживаемая аутентификация

### SNMP v2c

Строки community.

### SNMP v3

Для SNMP v3 источник данных SNMP поддерживает уровни безопасности `NoAuthNoPriv`, `authNoPriv` и `authPriv`, а также следующие протоколы аутентификации:

#### `authNoPriv`

| Протокол |  | RFC |
| --- | --- | --- |
| MD5 | HMAC-96-MD5 | [rfc3414](https://tools.ietf.org/html/rfc3414) |
| SHA | HMAC-96-SHA | [rfc3414](https://tools.ietf.org/html/rfc3414) |
| SHA224 | HMAC-128-SHA-224 | [rfc7860](https://tools.ietf.org/html/rfc7860) |
| SHA256 | HMAC-192-SHA-256 | [rfc7860](https://tools.ietf.org/html/rfc7860) |
| SHA384 | HMAC-256-SHA-384 | [rfc7860](https://tools.ietf.org/html/rfc7860) |
| SHA512 | HMAC-384-SHA-512 | [rfc7860](https://tools.ietf.org/html/rfc7860) |

#### `authPriv`

| Протокол |  | RFC | Примечания |
| --- | --- | --- | --- |
| DES | CBC-DES | [rfc3414](https://tools.ietf.org/html/rfc3414) |  |
| AES | CFB128-AES-128 | [rfc3826](https://tools.ietf.org/html/rfc3826) |  |
| AES192[1](#fn-1-1-def) |  | n/a | Расширение ключа Blumenthal |
| AES256[1](#fn-1-1-def) |  | n/a | Расширение ключа Blumenthal |
| AES192C[1](#fn-1-1-def) |  | n/a | Расширение ключа Reeder |
| AES256C[1](#fn-1-1-def) |  | n/a | Расширение ключа Reeder |

1

Данные алгоритмы шифрования не входят в официальную спецификацию, однако часто поддерживаются сетевыми устройствами. См. [SNMPv3 with AES-256](https://www.snmp.com/snmpv3/snmpv3_aes256.shtml).

Сведения об определении аутентификации в конфигурации мониторинга см. в разделе [Аутентификация SNMP](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmp-schema-reference#authentication "Узнайте о расширениях SNMP в платформе Extensions framework.").

## Требования к оборудованию

Мониторинг SNMP с помощью платформы Extensions выполняется через ActiveGate. Требования к хостам зависят от следующих факторов:

* Количество опрашиваемых устройств.
* Количество строк протокола приёма метрик, принятых за интервал опроса (1 минута). Уникальная комбинация метрики и измерения (кортеж) формирует одну строку.
* Настроен ли профиль производительности [EEC](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Dynatrace Extensions.") на высокие лимиты.

В зависимости от количества устройств и принятых строк к ActiveGate, выполняющим мониторинг SNMP, предъявляются следующие требования к оборудованию:

| Хост (тип EC2) | Процессоры | ОЗУ (ГБ) | Устройства SNMP | Принятые строки |
| --- | --- | --- | --- | --- |
| XS (`c5.large`) | 2 | 4 | 900 | 142 000 |
| S (`c5.xlarge`) | 4 | 8 | 1 800 | 284 000 |
| M (`c5.2xlarge`) | 8 | 16 | 4 000 | 632 000 |
| L (`c5.4xlarge`) | 16 | 32 | 6 000 | 940 000 |

Расчётные пределы по количеству устройств SNMP и принятых строк определены в ходе внутреннего тестирования. Фактические значения могут отличаться в зависимости от сложности конфигурации мониторинга.

Например, устройства SNMP, использованные в тестах, были оснащены 20 коммуникационными интерфейсами. Фактическое число интерфейсов напрямую влияет на загрузку процессора и потребление памяти.