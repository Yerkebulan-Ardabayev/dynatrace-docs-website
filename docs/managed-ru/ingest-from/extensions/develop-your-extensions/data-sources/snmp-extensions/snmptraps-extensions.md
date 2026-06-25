---
title: Источник данных SNMP traps
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmptraps-extensions
scraped: 2026-05-12T11:15:04.029744
---

# Источник данных SNMP traps

# Источник данных SNMP traps

* Справочник
* Чтение: 9 мин
* Обновлено 6 мая 2026 г.

SNMP traps: стандартный способ уведомления центральной системы управления сетью о значимых проблемах и событиях в сетевой инфраструктуре.

Dynatrace предоставляет платформу для расширения анализа данных, связанных с SNMP traps, генерируемыми в инфраструктуре, и пересылки trap-сообщений от устройств SNMP в виде событий журнала.

Предполагается следующее:

* Устройства поддерживают генерацию SNMP traps
* Известно, как настроить устройства на отправку trap-сообщений, и имеются соответствующие полномочия
* Вы знакомы с [базовыми концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [файла extension YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.").

![Принцип работы источника данных SNMP Traps](https://cdn.bfldr.com/B686QPH3/as/kp4g9n43jxqtw76p4bjjbw/SNMP_traps_data_source_-_Light_Mode?auto=webp&format=png&position=1)

Принцип работы источника данных SNMP Traps

## Предварительные требования и поддержка

Ознакомьтесь с предварительными требованиями и перечнем поддерживаемых технологий. Сведения об ограничениях, применяемых к расширениям, см. в разделе [Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.").

### Поддерживаемые версии Dynatrace

* Dynatrace версии 1.236 и выше
* ActiveGate версии 1.235 и выше

### Поддерживаемые версии SNMP

* SNMPv2c и более ранние версии
* SNMPv3 с ActiveGate версии 1.251 и выше

### Требования к оборудованию

При отправке большого количества trap-сообщений операционная система может отбрасывать часть из них. Аналогичная ситуация возникает при достижении лимита журналов

Значения для EEC с профилем производительности по умолчанию

| Экземпляр | ЦП | Память (МиБ) | Расчётное количество trap-сообщений | Расчётное количество trap-сообщений для SNMPv3 |
| --- | --- | --- | --- | --- |
| c5.large | 5% | 45 МиБ | 30 тыс/мин (журналы включены) 45 тыс/мин (журналы отключены) | 17 тыс/мин (журналы включены) 32 тыс/мин (журналы отключены) |

Значения для EEC с высокопроизводительным профилем

| Экземпляр | ЦП | Память (МиБ) | Расчётное количество trap-сообщений | Расчётное количество trap-сообщений для SNMPv3 |
| --- | --- | --- | --- | --- |
| c5.large | 15% | 45 МиБ | 75 тыс/мин (журналы включены) 150 тыс/мин (журналы отключены) | 60 тыс/мин (журналы включены) 105 тыс/мин (журналы отключены) |

## Поддерживаемая аутентификация

### SNMP v2c и более ранние версии

Строки community.

### SNMP v3

Для SNMP v3 источник данных SNMP traps поддерживает уровни безопасности `NoAuthNoPriv`, `authNoPriv` и `authPriv`, а также следующие протоколы аутентификации:

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

Сведения об определении аутентификации в конфигурации мониторинга см. в разделе [Аутентификация](#authentication).

### Поддерживаемые сообщения

Источник данных SNMP traps поддерживает только SNMP traps. SNMP inform-запросы не поддерживаются.

## События

События trap-сообщений передают подробную информацию о каждом trap-сообщении в [лог-ингест](/managed/analyze-explore-automate/log-monitoring/acquire-log-data "Узнайте, как получать данные логов в Dynatrace Log Monitoring."). Trap-сообщение содержит следующие сведения:

### Контекст

Сущность, с которой связано событие журнала. IP-адрес устройства и OID переводятся в удобочитаемый формат с помощью [файлов MIB](#mib-files-snmp-traps).

### Сообщение

Фактическое trap-сообщение с указанием типа trap-сообщения.

### Атрибуты

Атрибуты, передаваемые в событие журнала.

#### Основные

* `event.type`: всегда имеет значение `LOG`
* `log.source`: всегда имеет значение `snmptraps`
* `loglevel`: всегда имеет значение `NONE`
* `snmp.version`: всегда имеет значение `1`, `2c` или `3`

### Dynatrace

Топологические свойства Dynatrace.

* `dt.source_entity`: идентификатор устройства (сущности), с которым связано событие журнала.

### Прочее

Все привязки переменных, сообщаемые вместе с trap-сообщением, и переменные, определённые расширением, добавляются в качестве атрибутов события журнала (например, `device.address` и `snmp.trap_oid`).

Дополнительные сведения о пользовательских атрибутах журналов и правилах их обработки см. в следующих источниках:

* [Создание пользовательского атрибута журнала](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes#create-a-custom-log-attribute "Узнайте, как создавать и использовать пользовательские атрибуты при приёме данных логов.")
* [Правила обработки журналов](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")

### Включение событий trap-сообщений

Выберите набор функций **Events**, чтобы включить пересылку событий trap-сообщений в лог-ингест.

При использовании набора функций по умолчанию расширение сообщает только одну метрику: количество trap-сообщений, отправленных указанным источником за заданный интервал.

### Log Viewer

В [Log Viewer](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Узнайте, как использовать средство просмотра логов Dynatrace для анализа данных логов.") откройте **Logs** и отфильтруйте события trap-сообщений по `log.source: snmptraps`.

Пример события trap-сообщения

![Пример события SNMP trap в Log Viewer](https://dt-cdn.net/images/log-viewer-1087-9f26695568.png)

Пример события SNMP trap в Log Viewer

## Определение области данных

* Имя расширения
* Версия расширения
* Частота сбора метрик (интервал)
* Имя метрики
* Два доступных измерения: отправитель trap-сообщения и OID trap-сообщения

### Пример файла YAML-определения

```
name: custom:snmptraps-extension-example



version: 1.0.0



minDynatraceVersion: "1.235"



author:



name: Dynatrace SNMP traps data source team



snmptraps:



- group: generic



interval:



minutes: 1



featureSet: basic



metrics:



- key: number-of-traps-received



value: calculated



type: count,delta
```

Определение области мониторинга SNMP traps начинается с узла YAML `snmptraps`. Все параметры под этим узлом относятся к объявленному [типу источника данных](/managed/ingest-from/extensions/concepts#data-source-type "Подробнее о концепции Dynatrace Extensions."), которым в данном случае является SNMP traps.

## Метрики

SNMP traps собирают только одну метрику: количество trap-сообщений, отправленных источником, определённым в конфигурации мониторинга, за заданный интервал. Единственный параметр настройки: ключ метрики.

Например:

```
metrics:



- key: myExtension.number-of-traps-received



value: calculated



type: count,delta
```

Строка ключа метрики должна соответствовать требованиям [протокола приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

### Рекомендации по именованию ключей метрик

Метрики, принимаемые в Dynatrace с помощью расширения, составляют лишь часть из тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Чтобы ключи метрик были уникальными и легко идентифицировались в Dynatrace, рекомендуется добавлять к имени метрики префикс в виде имени расширения. Это гарантирует уникальность ключа метрики и позволяет легко сопоставить метрику с конкретным расширением в среде.

## Набор функций

Наборы функций: категории, по которым организуются данные, собираемые расширением. Подробнее см. в разделе [Наборы функций](/managed/ingest-from/extensions/concepts#feature-sets "Подробнее о концепции Dynatrace Extensions."). Наборы функций можно определять на уровне расширения, группы или отдельной метрики.

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) можно ограничить мониторинг одним из наборов функций.

В сильно сегментированных сетях наборы функций могут соответствовать сегментам среды. При создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, имеющую доступ к этому сегменту.

Метрики, не отнесённые ни к одному набору функций, считаются метриками по умолчанию и всегда включаются в отчёт.

## Интервал

Интервал, с которым выполняется измерение данных. Интервалы можно задавать на уровне группы, подгруппы или отдельной метрики с точностью до одной минуты. Максимальный интервал: 2880 минут (2 суток, 48 часов).

Для источников данных JMX задать интервал невозможно.

Например:

```
interval:



minutes: 5
```

Приведённый формат поддерживается начиная со схемы версии 1.217. Для более ранних версий схемы используйте следующий формат (поддерживается до версии схемы 1.251 включительно):

```
interval: 5m
```

## Файлы MIB

Файлы Management Information Base (MIB) определяют и описывают объекты SNMP, идентифицируемые по OID, что позволяет Dynatrace декодировать trap-сообщения в читаемые данные событий. При получении trap-сообщения расширение использует файлы MIB для интерпретации OID и формирования информативных оповещений.

## Конфигурация мониторинга

После определения области конфигурации необходимо указать сетевые устройства, с которых будут собираться данные, и ActiveGate, которые будут выполнять расширение и подключаться к этим устройствам.

Конфигурация мониторинга: JSON-полезная нагрузка, определяющая параметры подключения, учётные данные и наборы функций для мониторинга. Подробнее см. в разделе [Запуск мониторинга](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Пример полезной нагрузки для активации расширения SNMP:

```
[



{



"scope": "ag_group-default",



"value": {



"version": "1.0.0",



"description": "traps from routers",



"enabled": true,



"featureSets": [



"basic"



],



"snmptraps": {



"sources" : [



{



"ip": "172.10.11.0/8",



"port": 8162,



"authentication": {



"community": "x120a1f"



}



},



{



"ip": "0.0.0.0/0",



"port": 162,



"authentication": {



"community": "public"



}



}



]



}



}



}



]
```

Когда исходный файл extension YAML готов, упакуйте, подпишите и загрузите его в среду Dynatrace. Подробнее см. в разделе [Управление жизненным циклом расширения](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Мастер активации расширений на основе Dynatrace Hub содержит динамически обновляемую JSON-полезную нагрузку с конфигурацией мониторинга

Также можно использовать Dynatrace API для загрузки схемы расширения, которая поможет создать JSON-полезную нагрузку для конфигурации мониторинга.

Используйте эндпоинт [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "Просмотрите схему расширения с помощью Dynatrace Extensions 2.0 API.").

Выполните следующий запрос:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Замените `{extension-name}` и `{extension-version}` значениями из файла extension YAML. Успешный вызов возвращает схему JSON.

### Область

Каждому хосту ActiveGate, выполняющему расширение, необходим корневой сертификат для проверки его подлинности. Подробнее см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

Область: группа ActiveGate, которая будет выполнять расширение. Все ActiveGate из группы будут одновременно запускать данную конфигурацию мониторинга. При использовании одного ActiveGate назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время или после установки. Подробнее см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

### Версия

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

### Описание

Понятное описание параметров данной конфигурации мониторинга.

### Включено

Если задано значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Источники

В конфигурации мониторинга необходимо определить источники trap-сообщений. Для определения источника укажите следующие сведения:

* Сеть, отправляющая пакеты с trap-сообщениями, в нотации CIDR. Для настройки адреса отдельного интерфейса добавьте маску подсети `32` после IP-адреса, например `172.10.11.0/32`.
* UDP-порт, на который отправляются trap-сообщения
* Учётные данные аутентификации

  + SNMPv1 и SNMPv2 аутентифицируются только по имени community.
  + SNMPv3 требует расширенной аутентификации, описанной в следующем разделе.

### Аутентификация

Сведения об аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, обфускируются и не могут быть получены повторно.

В зависимости от уровня безопасности сформируйте сведения об аутентификации по одному из приведённых ниже примеров. Список [поддерживаемых протоколов](#snmp-v3) см. ниже.

Уровень безопасности: authPriv

Уровень безопасности: authNoPriv

Уровень безопасности: NoAuthNoPriv

```
{



"ip": "10.10.10.10",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "user",



"securityLevel": "AUTH_PRIV",



"authPassword": "********",



"authProtocol": "SHA",



"privPassword": "********",



"privProtocol": "AES256C"



}
```

```
{



"ip": "10.10.10.10",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "user",



"securityLevel": "AUTH_NO_PRIV",



"authPassword": "********",



"authProtocol": "SHA"



}
```

```
{



"ip": "10.10.10.12",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "snmptest_SHA_AES256",



"securityLevel": "NO_AUTH_NO_PRIV"



}
```

### Дополнительные параметры

В некоторых SNMP traps OID привязок переменных содержат динамические части в конце, которые изменяются с каждым входящим trap-сообщением. Для предотвращения проблем при обработке SNMP traps можно настроить обрезку OID привязок переменных.

#### Формат

```
"advanced": {



"varbindings": [



{



"root": ".1.3.6",



"suffixLen": 1



}



]



}
```

* `root`: используется для сопоставления суффикса и его обрезки. Параметр `root` можно задать в необработанном (`1.3.6.1.4.1.9.9.41.1.2.3.1`) или разрешённом (`CISCO-SMI::ciscoMgmt.41.1.2.3.1`) формате.
* `suffixLen`: указывает количество октетов в конце OID, которые должны быть обрезаны.

#### Пример

В данном примере все привязки переменных в поддереве `CISCO-SMI::ciscoMgmt` заканчиваются на `34024`. С каждым последующим сгенерированным trap-сообщением это число будет увеличиваться.

До обрезки:

```
"event.type": "LOG",



"content": "SNMP trap (CISCO-SMI::ciscoMgmt.41.2.0.1) reported from 192.168.1.100\n",



"status": "NONE",



"timestamp": "1678712960382",



"loglevel": "NONE",



"log.source": "snmptraps",



"snmp.trap_oid": "CISCO-SMI::ciscoMgmt.41.2.0.1.",



"device.address": "192.168.1.100",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.2.34024": "PKI",



"SNMPv2-MIB::snmpTrapOID": ".1.3.6.1.4.1.9.9.41.2.0.1",



"DISMAN-EVENT-MIB::sysUpTimeInstance": "1660720758",



"snmp.version": "2c",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.5.34024": "Certificate chain validation has failed. The certificate has expired. Validity period ended on 2023-11-29T03:21:33Z",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.6.34024": "1004407027",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.3.34024": "4",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.4.34024": "CERTIFICATE_INVALID_EXPIRED"
```

Все привязки переменных, соответствующие значению, указанному в `root`, обрезаются.

После обрезки:

```
"event.type": "LOG",



"content": "SNMP trap (CISCO-SMI::ciscoMgmt.41.2.0.1) reported from 192.168.1.100\n",



"status": "NONE",



"timestamp": "1678712960382",



"loglevel": "NONE",



"log.source": "snmptraps",



"snmp.trap_oid": "CISCO-SMI::ciscoMgmt.41.2.0.1.",



"device.address": "192.168.1.100",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.2": "PKI",



"SNMPv2-MIB::snmpTrapOID": ".1.3.6.1.4.1.9.9.41.2.0.1",



"DISMAN-EVENT-MIB::sysUpTimeInstance": "1660720758",



"snmp.version": "2c",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.5": "Certificate chain validation has failed. The certificate has expired. Validity period ended on 2023-11-29T03:21:33Z",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.6": "1004407027",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.3": "4",



"CISCO-SMI::ciscoMgmt.41.1.2.3.1.4": "CERTIFICATE_INVALID_EXPIRED"
```

### Наборы функций

Укажите список наборов функций для мониторинга. Чтобы включить все наборы функций, укажите `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

Отправку trap-сообщений в виде [событий](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmptraps-extensions#events "Создайте расширение для SNMP traps с помощью платформы Dynatrace Extensions framework.") можно включить, задав `featureSets` значение `events`.