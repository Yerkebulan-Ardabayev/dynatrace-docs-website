---
title: Справочник по источнику данных SNMP
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmp-schema-reference
scraped: 2026-05-12T12:34:58.713623
---

# Справочник по источнику данных SNMP

# Справочник по источнику данных SNMP

* Справочник
* Чтение: 11 мин
* Обновлено 10 ноября 2025 г.

Это общее описание файла YAML расширения на основе источника данных SNMP и способов объявления метрик и измерений, которые требуется собирать с помощью расширения.

## Область данных

Создайте определение набора данных, который будет получен из инфраструктуры SNMP и принят в Dynatrace расширением.

Составьте перечень идентификаторов объектов SNMP (OID), на которые будут ссылаться метрики и измерения расширения.

В данном примере используется расширение, собирающее данные с универсальных устройств SNMP.

```
name: custom:snmp-example



version: 1.0.0



minDynatraceVersion: '1.235'



author:



name: Dynatrace



metrics:



- key: snmp.generic.snmp.in.pkts



- key: snmp.generic.silentdrops



- key: snmp.generic.if.lastchange



- key: snmp.generic.if.in.errors



snmp:



- group: generic-device



interval:



minutes: 5



dimensions:



- key: snmp.generic.device.address



value: this:device.address



- key: snmp.generic.device.port



value: this:device.port



subgroups:



- subgroup: SNMP health



table: false



metrics:



- key: snmp.generic.snmp.in.pkts



value: oid:1.3.6.1.2.1.11.1.0



type: count



- key: snmp.generic.silentdrops



value: oid:1.3.6.1.2.1.11.31.0



type: count



- subgroup: NIC status



table: true



dimensions:



- key: snmp.generic.if.descr



value: oid:1.3.6.1.2.1.2.2.1.2



- key: snmp.generic.if.type



value: oid:1.3.6.1.2.1.2.2.1.3



metrics:



- key: snmp.generic.if.lastchange



value: oid:1.3.6.1.2.1.2.2.1.9



type: gauge



- key: snmp.generic.if.in.errors



value: oid:1.3.6.1.2.1.2.2.1.14



type: count



dashboards:



- path: 'generic-device-dashboard.json'
```

Определение области мониторинга SNMP начинается с узла YAML `snmp`. Все параметры под этим узлом относятся к объявленному [типу источника данных](/managed/ingest-from/extensions/concepts#data-source-type "Подробнее о концепции Dynatrace Extensions."), которым в данном случае является SNMP.

Расширения SNMP опираются на OID, идентифицирующие все объекты MIB, включая значения метрик и сведений об устройствах.

## Измерения

На каждом уровне (расширение, группа, подгруппа) можно определить до 25 измерений.

Например:

```
dimensions:



- key: cisco-catalyst-health.temperature.desc



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.2
```

### Ключ измерения

Строка ключа измерения должна соответствовать требованиям [протокола приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

### Значение измерения

Помимо простого извлечения значения измерения из OID, можно использовать следующие методы:

* Обычный текст. Используйте префикс `const:`

  ```
  - key: snmp.com.dt.generic.extension.owner



  value: const:Joe.Doe@somedomain.com
  ```
* Переменная, определённая в конфигурации мониторинга. Используйте префикс `var:`. Подробнее см. в разделе [Переменные](#variables).

  ```
  - key: snmp.com.dt.generic.activation.tag



  value: var:ext.activationtag
  ```
* Сведения об устройстве, определённые в конфигурации мониторинга, такие как IP-адрес или порт. Используйте префикс `this:`. Применяйте `device.address` и `device.port`.

  ```
  - key: snmp.com.dt.generic.device.address



  value: this:device.address



  - key: snmp.com.dt.generic.device.port



  value: this:device.port
  ```

### Использование переменных с измерениями

Чтобы сделать измерение расширения настраиваемым с помощью данных из конфигурации мониторинга, используйте переменные, которые будут заменены значениями, переданными из конфигурации мониторинга. Переменные можно использовать непосредственно в качестве значения измерения или совместно с [фильтрами](#filters). Для использования переменных их необходимо предварительно объявить в файле extension YAML:

```
vars:



- id: ifNameFilter



displayName: Pattern matching interfaces for which metrics should be queried



type: pattern



- id: ext.activationtag



displayName: Extension activation tag



type: pattern
```

После этого на них можно ссылаться в определении измерения. Добавьте к имени переменной префикс `var`.

```
dimensions:



- key: interface_description



value: oid:.1.3.6.1.2.1.2.2.1.2



filter: var:ifNameFilter



- key: snmp.com.dt.generic.activation.tag



value: var:ext.activationtag
```

### Фильтрация извлечённых строк метрик

После определения фильтра в виде [переменной](#variables) можно добавить логику фильтрации на уровне измерения. В результате в отчёт попадёт только та метрика, значение измерения которой соответствует критериям фильтра. Если фильтры заданы для нескольких измерений, все они должны совпасть, чтобы была создана строка метрики.

```
filter: var:ifNameFilter
```

Определите фильтр на основе условия следующим образом:

* **Starts with**: используйте квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Ends with**: используйте квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Contains**: используйте квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Equals**: используйте квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для приведённых выше выражений также можно использовать квалификаторы:

  + `const:$and`: для объединения двух и более выражений оператором AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or`: для объединения двух и более выражений оператором OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not`: для отрицания выражения. Пример:

    ```
    filter: const:$not(<expr>)
    ```

## Метрики

На каждом уровне (расширение, группа, подгруппа) можно определить до 100 метрик.

Например:

```
snmp:



- group: catalyst-health



featureSet: temperature



interval:



minutes: 5



dimensions:



- key: device_name



value: oid:1.3.6.1.2.1.1.5



- key: this.device.address



value: this:device.address



metrics:



- key: cisco-catalyst-health.temperature.value



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.3



type: gauge



featureSet: basic



interval:



minutes: 5
```

### Ключ метрики

Строка ключа метрики должна соответствовать требованиям [протокола приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

Для схемы Extension 2.0 версии 1.215 узел метрики требует параметра `id` вместо `key`. Начиная со схемы Extension 2.0 версии 1.217 обязательно использование параметра `key`.

#### Рекомендации по именованию ключей метрик

Метрики, принимаемые в Dynatrace с помощью расширения, составляют лишь часть из тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Чтобы ключи метрик были уникальными и легко идентифицировались в Dynatrace, рекомендуется добавлять к имени метрики префикс в виде имени расширения. Это гарантирует уникальность ключа метрики и позволяет легко сопоставить метрику с конкретным расширением в среде.

### Значение метрики

OID, из которого нужно извлечь значение метрики.

### Тип

Платформа Dynatrace Extensions поддерживает полезные нагрузки метрик в форматах gauge (`gauge`) или count (`count`). Подробнее см. в разделе [Полезная нагрузка метрики](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API."). Для указания типа метрики используйте атрибут `type`.

## Метаданные метрики

Расширение может определять метаданные для каждой метрики, доступной в Dynatrace. Например, можно добавить отображаемое имя метрики и единицу измерения, которые используются для фильтрации в [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в обозревателе метрик Dynatrace.").

Все метаданные метрик задаются в разделе `metrics` файла YAML расширения, чтобы они были корректно связаны с конфигурацией метрики.

```
name: custom:example-extension-name



version: 1.0.0



minDynatraceVersion: "1.236"



author:



name: Dynatrace



metrics:



- key: your.metric.name



metadata:



displayName: Display name of the metric visible in Metrics browser



unit: Count
```

## Набор функций

Наборы функций: категории, по которым организуются данные, собираемые расширением. В данном примере создаётся расширение SNMP, которое отслеживает сетевые устройства и собирает метрики общего трафика пакетов и статистики транспортного уровня. Это отражено в организации метрик по соответствующим наборам функций: `total traffic` и `transport layer statistics`.

```
snmp:



- group: health



interval:



minutes: 5



dimensions:



- key: device_name



value: oid:1.3.6.1.2.1.1.5



- key: this.device.address



value: this:device.address



subgroups:



- subgroup: Traffic



featureSet: total traffic



metrics:



- key: outgoing_packets



value: oid:.1.3.6.1.2.1.11.1



type: count



- key: incoming_packets



value: oid:.1.3.6.1.2.1.11.1



type: count



- subgroup: TCP



featureSet: transport layer statistics



metrics:



- key: tcpActiveOpens



value: oid:1.3.6.1.2.1.6.5.0



type: count



- key: tcpPassiveOpens



value: oid:1.3.6.1.2.1.6.6.0



type: count



- subgroup: UDP



featureSet: transport layer statistics



metrics:



- key: udpNoPorts



value: oid:1.3.6.1.2.1.7.2.0



type: count



- key: udpInErrors



value: oid:1.3.6.1.2.1.7.3.0



type: count
```

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) можно ограничить мониторинг одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут соответствовать сегментам среды. При создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, имеющую доступ к этому сегменту.

Метрики, не отнесённые ни к одному набору функций, считаются метриками по умолчанию и всегда включаются в отчёт.

Метрика наследует набор функций подгруппы, которая в свою очередь наследует набор функций группы. При этом набор функций, заданный на уровне метрики, переопределяет набор функций на уровне подгруппы, который в свою очередь переопределяет набор функций на уровне группы.

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

Например

```
snmp:



- group: snmp-generic



interval:



minutes: 5



dimensions:



- key: device_name



value: oid:1.3.6.1.2.1.1.5



metrics:



- key: incoming_packets



value: oid:.1.3.6.1.2.1.11.1
```

## Файлы MIB

Файлы Management Information Base (MIB) определяют объекты SNMP, идентифицируемые по OID, что позволяет Dynatrace преобразовывать опрашиваемые метрики в понятные имена и значения. В процессе опроса расширение использует файлы MIB для интерпретации данных, полученных от сетевых устройств.

ActiveGate поставляется со стандартным набором файлов MIB. Набор по умолчанию можно дополнить собственными файлами.

### Разрешение OID

Если доступные расширению файлы MIB содержат соответствующие сведения, OID можно объявлять по их именам вместо числовых значений. Например:

```
subgroups:



- subgroup: Device health (Temperature)



table: true



dimensions:



- key: envmon.temperature.desc



value: oid:ciscoEnvMonTemperatureStatusDescr



metrics:



- key: envmon.temperature.value



value: oid:ciscoEnvMonTemperatureStatusValue



name: The current testpoint temperature (deg Celsius)



type: gauge
```

### Разрешение сетевых адресов

IP-адрес, возвращаемый из OID, может быть автоматически преобразован в строку формата IPv4 или IPv6. Используемый формат определяется файлом MIB.

Например, OID `1.3.6.1.4.1.3375.2.2.10.1.2.1.3` (`ltmVirtualServAddr`), IP-адрес виртуального сервера, возвращается в виде двоичного (шестнадцатеричного) значения. С использованием MIB он передаётся в формате IPv4 или IPv6, как определено сведениями из `ltmVitualServAddrType`.

```
subgroups:



- subgroup: virtualServer



table: true



dimensions:



- key: ltmvirtualserveraddrvalue



value: oid:1.3.6.1.4.1.3375.2.2.10.1.2.1.3
```

### Преобразование данных с помощью `$networkFormat`

Функция `$networkFormat` позволяет извлекать данные из OID с помощью OID-форматировщиков. Доступные типы для извлечения: `interfaceAlias`, `interfaceName`, `portComponent`, `networkAddress` (ipv4, ipv6, mac, dns), `local address`, `macAddress` и `agentCircuitId`.

В файле `extension.yaml` используйте `$networkFormat` в качестве значения любого измерения (например, `network.translation`), чтобы указать способ преобразования значений OID:

* Укажите два OID (один в качестве форматировщика, другой для целевых данных).

  + `*$networkFormat`(`oid:<formatter OID>,` `oid:<data OID>`)
* Один OID с типом форматировщика: используйте один OID с конкретным типом форматировщика.

  + `$networkFormat`(`const:<formatter type>`, `oid:<OID>`)
* Два OID или один OID и один форматировщик со значением по умолчанию: укажите значение `default` на случай сбоя преобразования.

  + `$networkFormat`(`oid:<formatter OID>`, `oid:<data OID>`, `default:<default value>`)

При ошибках преобразования (например, неподдерживаемые символы ASCII или отсутствие сведений в MIB) Dynatrace повторяет попытку. Если ошибка не устраняется, система переходит к режиму `rawString`, отображая непреобразованные данные.

Чтобы избежать проблем с преобразованием, убедитесь в наличии необходимых файлов MIB. Отсутствие файлов MIB приводит к выводу непреобразованных данных.

### Преобразование перечисляемых значений

Если OID является перечисляемым типом, расширение передаёт значение OID в виде строки с именем, а не просто числа.

Например, OID `1.3.6.1.2.1.2.2.1.7` (`ifAdminStatus`) является перечисляемым типом с возможными значениями `(1-up, 2-down, 3-testing)`. При использовании MIB расширение передаёт полную строку в качестве значения (например, `1-up` вместо `1`) для интерфейса в состоянии `up`.

### Добавление собственного файла MIB

Если некоторые OID расширения отсутствуют в стандартных файлах MIB, можно добавить собственный файл MIB в расширение.

#### Включение файла MIB в пакет расширения

Создайте каталог `snmp` рядом с файлом `extension.yaml` и поместите в него файл MIB. Например:

```
extension.zip



│   extension.yaml



│



└───alerts



│   |   alert.json



│



└───dashboards



|   │   dashboard.json



|



└───snmp



│   |   IF-MIB.txt
```

Отсутствующие сведения фиксируются в журнале, и передаётся исходное значение. Например, если источник данных не может определить тип сетевого адреса на основе доступных файлов MIB, в журнале появляется следующее сообщение и передаётся шестнадцатеричное значение.

```
"inetAddress translation: Unable to find inetAddress type. X, dimension: Y"`.
```

#### Расположение файлов MIB

Стандартные файлы MIB хранятся в:

* Linux: `/opt/dynatrace/remotepluginmodule/agent/res/mib-files`
* Windows: `C:\%PROGRAMFILES%\dynatrace\remotepluginmodule\agent\res\mib-files`

Файл MIB, добавленный в расширение, сохраняется в:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/runtime/datasources/working_directories/[ID]/snmp`
* Windows: `C:\%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\runtime\datasources\working_directories\[ID]\snmp`

где `[ID]`: строка, содержащая идентификатор конфигурации мониторинга и временную метку.

### Пользовательский каталог MIB для ActiveGate

Можно также добавить пользовательские файлы MIB непосредственно в ActiveGate. Эти файлы MIB будут использоваться всеми расширениями SNMP и SNMP Traps, работающими на данном ActiveGate.

Поместите пользовательские файлы MIB в каталог `mib-files-custom`:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/mib-files-custom/`
* Windows: `C:\%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata\mib-files-custom\`

Файлы, хранящиеся в каталоге `mib-files-custom`, сохраняются между обновлениями.

Если пользовательский файл MIB должен использоваться уже запущенным расширением, потребуется перезапустить службу EEC, чтобы расширение смогло прочитать файл MIB. Подробнее см. в разделе [Пользовательская конфигурация Extension Execution Controller](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration "Настройте Extension Execution Controller (EEC).").
Если расширение ещё не настроено, перезапускать службу EEC не нужно.
В обоих случаях перезапускать ActiveGate не требуется.

## Конфигурация мониторинга

После определения области конфигурации необходимо указать сетевые устройства, с которых будут собираться данные, и ActiveGate, которые будут выполнять расширение и подключаться к этим устройствам.

Убедитесь, что все ActiveGate из группы, определённой в качестве области, могут подключиться к соответствующему источнику данных. Назначить ActiveGate в группу можно во время или после установки. Подробнее см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

Конфигурация мониторинга: JSON-полезная нагрузка, определяющая параметры подключения, учётные данные и наборы функций для мониторинга. Подробнее см. в разделе [Запуск мониторинга](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Пример полезной нагрузки для активации расширения SNMP:

```
[



{



"scope": "ag_group-my-activegate-group",



"value": {



"version": "1.0.0",



"description": "my monitoring configuration",



"enabled": true,



"snmp": {



"devices": [



{



"ip": "snmp.company.org",



"port": 161,



"authentication": {



"type": "SNMPv2c",



"community": "public"



},



"advanced": {



"timeoutSecs": 5,



"retries": 0,



"maxRepetitions": 50,



"maxOidsPerQuery": null,



"enableUnconnectedUdp": true



}



}



]



},



"featureSets": [



"all"



]



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

Область: группа ActiveGate, которая будет выполнять расширение. Данную конфигурацию мониторинга запустит только один ActiveGate из группы. При использовании одного ActiveGate назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время или после установки. Подробнее см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

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

### Устройства

В одной конфигурации мониторинга можно определить до 100 устройств. Для определения устройства укажите следующие сведения:

* IP-адрес или имя устройства
* Порт
* Учётные данные аутентификации

  + Тип: `SNMPv2c` или `SNMPv3` (по конструкции `SNMPv2c` использует аутентификацию по строке community)

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



"userName": "snmptest_SHA_AES256",



"securityLevel": "AUTH_PRIV",



"authPassword": "916cb7fe3c80fc273413797bd063b8e320237e6159a47c06278ec818da58e3a4fb5f715bdb63313439f2d5e25a434386b3fe82dd0a643507d7452340b3c56d30=",



"authProtocol": "SHA512",



"privPassword": "EAB559FF7A04D73D77FE017271A3250B786FB2FD4DA0D45F60C9BE31311221262DB510A4AEC53A418297FC260DB6C91429880030BCAA8416FA1C2810C8E7B928=",



"privProtocol": "AES256C"



}
```

```
{



"ip": "10.10.10.10",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "snmptest_SHA_AES256",



"securityLevel": "AUTH_NO_PRIV",



"authPassword": "916cb7fe3c80fc273413797bd063b8e320237e6159a47c06278ec818da58e3a4fb5f715bdb63313439f2d5e25a434386b3fe82dd0a643507d7452340b3c56d30=",



"authProtocol": "SHA512"



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

Для подключения можно определить следующие дополнительные свойства:

* `timeoutSecs`
  Максимальное время ожидания (в секундах) ответа на запрос SNMP. По умолчанию: 1 секунда.
* `retries`
  Максимальное количество повторных попыток выполнения запроса при сбое (общее время запроса: `timeoutSecs` x `retries`). По умолчанию: 3 повторные попытки.
* `maxRepetitions`
  Позволяет ограничить объём данных, возвращаемых для одного запроса, что может увеличить количество запросов к устройству до сбора всех необходимых данных. По умолчанию: 100 повторений.
* `maxOidsPerQuery`
  Позволяет ограничить количество OID, запрашиваемых в одном запросе SNMP. По умолчанию: 60.
* `enableUnconnectedUdp`
  ActiveGate версии 1.297 и выше. При включении UDP-сокет переходит в несвязанный режим. Это позволяет принимать ответы с адреса, отличного от адреса отправки запроса, или игнорировать ICMP-пакеты.

### Наборы функций

Укажите список наборов функций для мониторинга. Чтобы включить все наборы функций, укажите `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Переменные

Если расширение объявляет переменные, можно задать значения, которые будут переданы в расширение в качестве фильтров или обычных строк. Подробнее см. в разделе [Объявление переменных](#declare-variables).

```
"vars":



{



"ifNameFilter": "$contains(1/1/1)",



"ifSpeedFilter": "$eq(4294967295)"



}
```