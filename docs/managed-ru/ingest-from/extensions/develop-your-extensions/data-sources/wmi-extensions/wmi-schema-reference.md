---
title: Справочник по источнику данных WMI
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference
scraped: 2026-05-12T12:16:25.507564
---

# Справочник по источнику данных WMI

# Справочник по источнику данных WMI

* Справочник
* Чтение: 10 мин
* Обновлено 10 ноября 2025 г.

Это общее описание YAML-файла расширения на основе источника данных WMI и способов объявления метрик и измерений для сбора с помощью расширения.

Пошаговое руководство по созданию расширения WMI также доступно в разделе [Учебное руководство по источнику данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Узнайте о расширениях WMI в платформе Extensions framework.").

## Область данных

Создайте перечень устройств, на которые ссылается расширение, а также [свойства WMI](#wql-queries), которые будут источником значений метрик и измерений.

В этом примере создаётся простое расширение, собирающее данные о дисках и сетевых параметрах с устройств под мониторингом WMI.

```
name: custom:wmi-extension



version: 0.0.1



minDynatraceVersion: '1.236'



author:



name: Dynatrace



vars:



- id: deviceFilter



displayName: Filter



type: variable



wmi:



- group: WMIClasses



interval:



minutes: 1



featureSet: basic



dimensions:



- key: counter.name



value: Name



subgroups:



- subgroup: LogicalDisk



wmiNamespace: root\cimv2



query: SELECT DeviceID, FreeSpace, Name, Size, DriveType FROM Win32_LogicalDisk WHERE var:deviceFilter



dimensions:



- key: disk.id



value: column:DeviceID



- key: disk.type



value: column:DriveType



metrics:



- key: size



value: column:Size



type: gauge



featureSet: basic



- key: freeSpace



value: column:FreeSpace



type: gauge



featureSet: basic



- subgroup: Network



interval:



minutes: 1



wmiNamespace: root\cimv2



query: SELECT Name, MACAddress, Speed, ServiceName FROM Win32_NetworkAdapter



dimensions:



- key: mac



value: column:MACAddress



- key: service.name



value: column:ServiceName



metrics:



- key: speed



value: column:Speed



type: gauge



featureSet: basic
```

Определение области мониторинга WMI начинается с узла YAML `wmi`. Все параметры этого узла относятся к объявленному [типу источника данных](/managed/ingest-from/extensions/concepts#data-source-type "Подробнее о концепции Dynatrace Extensions.") (в данном случае WMI).

## WQL-запросы

Расширения WMI используют пространства имён WMI и их классы. Расширение WMI извлекает значения измерений и метрик из свойств классов WMI с помощью [WQL-запросов](https://docs.microsoft.com/en-us/windows/win32/wmisdk/querying-with-wql).

Большинство классов и свойств, связанных с расширениями, находятся в пространстве имён `root\civm2`. Дополнительные сведения о пространствах имён и классах WMI см. в документации Microsoft: [Windows Management Instrumentation](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page).

В этом примере из класса [`Win32_LogicalDisk`](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-logicaldisk) в пространстве имён `root\cimv2` (`wmiNamespace` определён на уровне группы) запрашиваются свойства диска (`DeviceID`, `FreeSpace` и `Size`), а результаты фильтруются по диску C с ненулевым `FreeSpace`. Фильтрация реализована через переменную; см. [конфигурацию мониторинга](#monitoring-configuration) ниже. Значения, полученные из WMI, назначаются измерениям и метрикам и передаются в Dynatrace.

```
name: custom:wmi.wql.example



version: 0.0.1



minDynatraceVersion: "1.236"



author:



name: Dynatrace



vars:



- id: deviceFilter



displayName: Filter



type: variable



wmi:



- group: WMIClasses



featureSet: basic



interval:



minutes: 1



wmiNamespace: root\cimv2



query: SELECT DeviceID, FreeSpace, Size FROM Win32_LogicalDisk WHERE var:deviceFilter



dimensions:



- key: disk.id



value: column:DeviceID



metrics:



- key: size



value: column:Size



type: gauge



- key: freeSpace



value: column:FreeSpace



type: gauge
```

### Пример конфигурации мониторинга для WQL-запроса

В этом примере показано, как передать переменную `deviceFilter`, объявленную ранее в `extension.yaml`.

```
[



{



"scope": "ag_group-my-activegate-group",



"value": {



"version": "1.0.0",



"description": "WMI Simple",



"enabled": true,



"activationContext": "REMOTE",



"wmiRemote": {



"devices": [



{



"host" : "192.168.0.1",



"user" : "DOMAIN\\Administrator",



"password" : "Password1"



}



]



},



"featureSets": ["basic"],



"vars": {



"deviceFilter": "DeviceID = 'C:' and FreeSpace > 0"



}



}



}



]
```

## Измерения

На каждом уровне (расширение, группа, подгруппа) можно определить до 25 измерений.

### Ключ измерения

Строка ключа измерения должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

### Значение измерения

Помимо простого извлечения значения измерения из свойства, можно использовать следующие методы:

* Значение, извлечённое WQL-запросом. Используйте префикс `column:`.

  ```
  dimensions:



  - key: disk.id



  value: column:DeviceID
  ```

  Свойство `DeviceID` необходимо предварительно запросить в связанной группе или подгруппе, чтобы использовать его как значение измерения.
* Простой текст. Используйте префикс `const:`.

  ```
  dimensions:



  - key: extension.owner



  value: const:Joe.Doe@somedomain.com
  ```
* Переменная, определённая в конфигурации мониторинга. Используйте префикс `var:`.

  ```
  dimensions:



  - key: public_ip



  value: var:public_ip



  - key: agent_version



  value: var:agent_version
  ```
* Сведения об устройстве, определённые в конфигурации мониторинга, такие как IP-адрес или порт устройства. Используйте `this:device.host`.

  ```
  dimensions:



  - key: hostname



  value: this:device.host
  ```

### Использование переменных с измерениями

Чтобы сделать измерение расширения настраиваемым с помощью данных из конфигурации мониторинга, используйте переменные, которые заменяются значениями из конфигурации мониторинга. Для работы с переменными необходимо сначала объявить их в YAML-файле расширения:

```
vars:



- id: oneagent_version



displayName: OneAgent version



type: variable
```

После этого можно ссылаться на них в определении измерения. Добавьте к имени переменной префикс `var`.

```
dimensions:



- key: oneagent_version



value: var:agent_version
```

### Фильтрация извлечённых измерений

При извлечении значения измерения можно добавить логику фильтрации с помощью [WQL-запросов](#wql-queries), в результате чего будут передаваться только измерения, соответствующие критериям фильтрации.

```
query: SELECT DeviceID, FreeSpace, Size FROM Win32_LogicalDisk WHERE var:deviceFilter
```

Определите фильтр как запрос в конфигурации мониторинга и передайте его расширению в виде [переменной](#variables):

```
"vars": {



"deviceFilter": "DeviceID = 'C:' and FreeSpace > 0"



}
```

## Метрики

На каждом уровне (расширение, группа, подгруппа) можно определить до 100 метрик.

Например:

```
wmi:



- group: WMIClasses



interval:



minutes: 1



wmiNamespace: root\cimv2



query: SELECT DeviceID, FreeSpace, Size FROM Win32_LogicalDisk



dimensions:



- key: disk.id



value: column:DeviceID



metrics:



- key: size



value: column:Size



type: gauge



- key: freeSpace



value: column:FreeSpace



type: gauge
```

### Ключ метрики

Строка ключа метрики должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.").

В Dynatrace версий 1.215 и 1.217 узел метрики требует параметр `id` вместо `key`. Начиная с Dynatrace версии 1.219, рекомендуется использовать параметр `key`, так как `id` будет считаться устаревшим.

#### Рекомендации по ключам метрик

Метрики, передаваемые в Dynatrace с помощью расширения, являются частью тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Для уникальности и удобства идентификации ключей метрик рекомендуется добавлять к имени метрики префикс с именем расширения. Это гарантирует уникальность ключа метрики и позволяет легко отнести метрику к конкретному расширению в среде.

### Значение метрики

Свойство WMI, из которого извлекается значение метрики.

### Тип

Платформа Dynatrace Extensions поддерживает нагрузку метрик в форматах gauge (`gauge`) или count (`count`). Дополнительные сведения см. в разделе [Нагрузка метрики](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Узнайте, как работает протокол приёма данных Dynatrace Metrics API."). Для указания типа метрики используйте атрибут `type`.

## Метаданные метрик

Расширение может определять метаданные для каждой метрики, доступной в Dynatrace. Например, можно добавить отображаемое имя метрики и единицу измерения, которые используются для фильтрации в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в обозревателе метрик Dynatrace.").

Определяйте все метаданные метрик в разделе `metrics` YAML-файла расширения, чтобы они корректно сопоставлялись с конфигурацией метрики.

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

Наборы функций: категории, по которым организуются данные, собираемые расширением. В этом примере создаётся расширение WMI, выполняющее мониторинг устройств и собирающее метрики статистики транспортного протокола и дисков устройств. Это отражено в организации метрик по связанным наборам функций `tcp` и `physicalDisks`.

```
wmi:



group: Network_TCP



interval:



minutes: 1



featureSet: tcp



subgroups:



- subgroup: TCPv4



query: SELECT  ConnectionsActive, ConnectionsEstablished FROM Win32_PerfFormattedData_Tcpip_TCPv4



metrics:



- key: com.dynatrace.extension.host-observability.network.tcp.connections.active



value: column:ConnectionsActive



- key: com.dynatrace.extension.host-observability.network.tcp.connections.established



value: column:ConnectionsEstablished



dimensions:



- key: network.tcp.version



value: const:ipv4



- key: this.device



value: this:device.host



- subgroup: disk



query: SELECT Name, DiskBytesPersec, DiskReadBytesPersec FROM Win32_PerfFormattedData_PerfDisk_PhysicalDisk



featureSet: physicalDisks



metrics:



- key: com.dynatrace.extension.host-observability.disk.bytes.persec



value: column:DiskBytesPersec



- key: com.dynatrace.extension.host-observability.disk.read.persec.bytes



value: column:DiskReadBytesPersec



dimensions:



- key: disk.type



value: const:Physical



- key: disk.name



value: column:Name



- key: this.device



value: this:device.host
```

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) можно ограничить мониторинг одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут отражать сегменты среды. При создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, которая может подключаться к этому сегменту.

Все метрики, не отнесённые ни к одному набору функций, считаются метриками по умолчанию и передаются всегда.

Метрика наследует набор функций подгруппы, которая, в свою очередь, наследует набор функций группы. При этом набор функций, определённый на уровне метрики, имеет приоритет над набором функций подгруппы, а набор функций подгруппы имеет приоритет над набором функций группы.

## Интервал

Интервал, с которым выполняются измерения данных. Интервалы можно определять на уровне группы, подгруппы или отдельной метрики с детализацией в одну минуту. Максимальный интервал составляет 2880 минут (2 дня, 48 часов).

Для источников данных JMX установка интервала недоступна.

Например:

```
interval:



minutes: 5
```

Приведённый формат поддерживается начиная со схемы версии 1.217. Для более ранних версий схемы используйте следующий формат (поддерживается до схемы версии 1.251):

```
interval: 5m
```

```
wmi:



- group: Host



interval:



minutes: 1



query: SELECT Name, PercentProcessorTime FROM Win32_PerfFormattedData_PerfOS_Processor



metrics:



- key: com.dynatrace.extension.host-observability.host.cpu.time.processor



value: column:PercentProcessorTime



dimensions:



- key: host.cpu.id



value: column:Name
```

## Конфигурация мониторинга WMI

После определения области конфигурации необходимо указать сетевые устройства, с которых будут собираться данные, и ActiveGate, которые будут выполнять расширение и подключаться к устройствам.

Убедитесь, что все ActiveGate из группы ActiveGate, определённой как область, могут подключаться к соответствующему источнику данных. ActiveGate можно назначить в группу во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

Конфигурация мониторинга: JSON-нагрузка, определяющая сведения о подключении, учётные данные и наборы функций для мониторинга. Дополнительные сведения см. в разделе [Начало мониторинга](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Пример нагрузки для активации расширения WMI:

```
[



{



"scope": "ag_group-ActiveGate-group-name",



"value": {



"version": "1.0.0",



"description": "WMI Simple",



"enabled": true,



"activationContext": "REMOTE",



"wmiRemote": {



"devices": [



{



"host" : "192.168.0.1",



"user" : "DOMAIN\\Administrator",



"password" : "Password1"



}



]



},



"featureSets": ["basic"],



"vars": {



"deviceFilter": "DeviceID = 'C:' and FreeSpace > 0"



}



}



}



]
```

Когда первоначальный YAML расширения готов, упакуйте его, подпишите и загрузите в среду Dynatrace. Дополнительные сведения см. в разделе [Управление жизненным циклом расширения](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Мастер активации расширений на базе Dynatrace Hub содержит динамически обновляемую JSON-нагрузку с конфигурацией мониторинга.

Затем можно использовать Dynatrace API для загрузки схемы расширения, которая поможет создать JSON-нагрузку для конфигурации мониторинга.

Используйте эндпоинт [GET схемы расширения](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "Просмотрите схему расширения с помощью Dynatrace Extensions 2.0 API.").

Выполните следующий запрос:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Замените `{extension-name}` и `{extension-version}` значениями из YAML-файла расширения. При успешном вызове возвращается JSON-схема.

### Область

Каждый хост OneAgent или ActiveGate, на котором выполняется расширение, требует наличия корневого сертификата для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

#### Удалённое расширение

Для удалённого расширения областью является группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет запускать эту конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. ActiveGate можно назначить в группу во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

#### Локальное расширение

Для локального расширения областью является хост, группа хостов, зона управления или среда, в которой будет выполняться расширение.

* При определении хоста как области используйте следующий формат:

  ```
  "scope": "<HOST_ID>",
  ```

  Замените `<HOST_ID>` идентификатором сущности хоста, как в этом примере:

  ```
  "scope": "HOST-A1B2345678C9D001",
  ```
* При определении группы хостов как области используйте следующий формат:

  ```
  "scope": "HOST_GROUP-<HOST_GROUP_ID>",
  ```

  Замените `<HOST_GROUP_ID>` идентификатором сущности группы хостов, как в этом примере:

  ```
  "scope": "HOST_GROUP-AB123C4D567E890",
  ```

  Идентификатор группы хостов можно найти в URL страницы [настроек группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace помогает упорядочивать хосты, процессы и сервисы с помощью групп хостов."). Например:

  ```
  https://{your-environment-id}.live.dynatrace.com/#settings/hostgroupconfiguration;id=HOST_GROUP-AB123C4D567E890;hostGroupName=my-host-group
  ```
* При определении зоны управления как области используйте следующий формат:

  ```
  "scope": "management_zone-<MANAGEMENT-ZONE>",
  ```

  Замените `<MANAGEMENT-ZONE>` именем зоны управления, как в этом примере:

  ```
  "scope": "management_zone-sampleManagementZone",
  ```

  Зону управления можно найти на [странице зон управления](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Применяйте зоны управления для организации окружения Dynatrace и контроля доступа пользователей к определённым данным.").
* При определении среды как области используйте следующий формат:

  ```
  "scope": "environment",
  ```

  Также можно добавить теги для фильтрации хостов, на которых будет применяться эта конфигурация:

  ```
  "activationTags": [



  "dt.owner:lama"



  ]
  ```

### Версия

Версия данной конфигурации мониторинга. Одно расширение может выполняться с несколькими конфигурациями мониторинга.

### Описание

Описание конфигурации мониторинга в удобочитаемом виде.

### Включено

Если установлено значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Контекст активации

Установите для `activationContext` значение `REMOTE` для удалённых расширений и `LOCAL` для локальных расширений.

### Устройства

Только для удалённых расширений.

В одной конфигурации мониторинга в разделе `wmiRemote` можно определить до 100 устройств. Для определения устройства укажите следующие сведения:

* Хост
* Учётные данные аутентификации

### Аутентификация

Только для удалённых расширений.

Сведения об аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются и не могут быть получены обратно.

При аутентификации расширения на хосте Windows применяются стандартные концепции управления пользователями Windows. Если ActiveGate, выполняющий расширение, находится в том же домене, достаточно указать имя пользователя и пароль. Можно также указать домен, не забыв экранировать обратную косую черту (`\`).

Например:

```
"devices": [



{



"host" : "172.18.147.100",



"user" : ".\\WMIUser",



"password" : "SomePassword"



},



{



"host" : "exchange.lab.dynatrace.org",



"user" : "Exchange-Domain\\WMIUser",



"password" : "SomePassword2"



}



]
```

Рекомендуется создать выделенную локальную группу пользователей или учётную запись на целевом компьютере специально для удалённых подключений.

### Наборы функций

Добавьте список наборов функций для мониторинга. Чтобы передавать все наборы функций, укажите `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Переменные

Если расширение объявляет переменные, можно определить значения, которые передаются в расширение как фильтры или обычные строки. Дополнительные сведения см. в разделе [Использование переменных с измерениями](#declare-variables).

```
"vars": {



"mailboxName": "win-4u1vg1uqvla",



"deviceFilter": "DeviceID = 'C:'",



"ipFilter" : "DNSDomain='home'"



}
```