---
title: Учебное руководство WMI: источник данных
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-02
scraped: 2026-05-12T12:16:19.016793
---

# WMI tutorial - источник данных

# WMI tutorial - источник данных

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 30 марта 2022 г.

Чтобы расширение собирало метрики и передавало их в Dynatrace, необходимо определить источник данных. В этом учебном руководстве используется источник данных WMI. Это должен быть раздел с именем `wmi` в расширении.

Раздел `wmi` определяет WMI-запросы для получения метрик, периодичность их выполнения и правила сопоставления результатов с метриками и измерениями Dynatrace. Группы и подгруппы служат для организации данных и задания общих свойств: измерений и частоты выполнения.

В расширении используются 3 WMI-запроса. Их нужно добавить в `extension.yaml` и передать результаты как метрики Dynatrace:

* Извлечь загрузку ЦП, пользовательское время и время простоя для каждого процессора хоста (разбивка по идентификатору ЦП).

  ```
  SELECT Name, PercentProcessorTime, PercentIdleTime, PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor WHERE Name LIKE '_Total'
  ```
* Извлечь суммарные, отправленные и полученные байты в секунду для каждого сетевого адаптера хоста.

  ```
  SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkAdapter
  ```
* Извлечь суммарные, отправленные и полученные байты в секунду для каждого сетевого интерфейса хоста.

  ```
  SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkInterface
  ```

## Советы

### Рекомендации по именованию метрик

Добавляйте к ключам метрик префикс с именем расширения, чтобы избежать конфликтов с другими метриками в Dynatrace. В этом упражнении каждый ключ метрики начинается с `custom.demo.host-observability`.

### Измерение хоста

Хост, на котором выполняется расширение, можно идентифицировать с помощью значения измерения `this:device.host`.

### Статические измерения

Измерения с фиксированными строками добавляются с помощью префикса `const:`.

## Определение источника данных

Добавьте раздел `wmi` в файл `extension.yaml` по приведённому шаблону.

1. Создайте две группы с именами `Host` и `Network` с интервалом выполнения 1 мин. В обеих группах должно быть измерение, идентифицирующее хост.
2. Создайте подгруппу для каждого WMI-запроса и сопоставьте полученные столбцы с метриками и измерениями.
3. Добавьте измерение `network.type` со значением `Adapter` или `Interface` в зависимости от WMI-запроса.
4. Соберите новую версию пакета расширения и загрузите её.
5. Настройте мониторинг хоста Windows. Это можно сделать при активации расширения в Dynatrace Hub.
6. Подождите одну минуту и проверьте сбор метрик.

Дополнительные сведения о синтаксисе источника данных WMI см. в разделе [Справочник по источнику данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Узнайте о расширениях WMI в платформе Extensions framework.").

```
wmi:



- group: Host



interval:



minutes: 1



dimensions:



- key: host



value: this:device.host



subgroups:



- subgroup: CPU



query: SELECT Name, PercentProcessorTime, PercentIdleTime, PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor WHERE Name LIKE '_Total'



metrics:



- key: custom.demo.host-observability.host.cpu.time.processor



value: column:PercentProcessorTime



- key: custom.demo.host-observability.host.cpu.time.idle



value: column:PercentIdleTime



- key: custom.demo.host-observability.host.cpu.time.user



value: column:PercentUserTime



dimensions:



- key: host.cpu.id



value: column:Name



- group: Network



interval:



minutes: 1



dimensions:



- key: host



value: this:device.host



subgroups:



- subgroup: Adapters



query: SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkAdapter



metrics:



- key: custom.demo.host-observability.network.bytes.persec



value: column:BytesTotalPersec



- key: custom.demo.host-observability.network.bytes.received.persec



value: column:BytesReceivedPersec



- key: custom.demo.host-observability.network.bytes.sent.persec



value: column:BytesSentPersec



dimensions:



- key: network.type



value: const:Adapter



- key: network.name



value: column:Name



- subgroup: Interfaces



query: SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkInterface



metrics:



- key: custom.demo.host-observability.network.bytes.persec



value: column:BytesTotalPersec



- key: custom.demo.host-observability.network.bytes.received.persec



value: column:BytesReceivedPersec



- key: custom.demo.host-observability.network.bytes.sent.persec



value: column:BytesSentPersec



dimensions:



- key: network.type



value: const:Interface



- key: network.name



value: column:Name
```

## Результаты

Шесть метрик должны появиться в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в браузере метрик Dynatrace."). Для их поиска отфильтруйте по тексту `custom.demo`.

![result](https://dt-cdn.net/images/wmi-tutorial-metricbrowser-1590-12b46b5f17.png)

result

**Следующий шаг**: [Метаданные метрик](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-03 "Узнайте о расширениях WMI в платформе Extensions framework.")