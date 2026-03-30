---
title: Универсальная сетевая топология
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology/network-topology
scraped: 2026-03-06T21:19:17.250583
---

* 10 минут чтения

Расширение [SNMP Autodiscovery](https://www.dynatrace.com/hub/detail/snmp-autodiscovery) сканирует подсети и помогает пользователям обнаруживать полный инвентарь сетевых устройств с поддержкой SNMP. Кроме того, это расширение включает модель топологии, достаточно универсальную для того, чтобы большинство источников данных, относящихся к сетевым устройствам, можно было выразить через простой набор общих сущностей: сетевое устройство, сетевой порт и сетевой интерфейс.

Мы начали применять эту модель к некоторым из наших наиболее популярных SNMP-расширений для технологий Cisco, F5, Palo Alto и Juniper. Это позволило нам унифицировать все сетевые сущности, упростить запросы и отображать актуальные сетевые данные независимо от источника мониторинга.

Чтобы увидеть, как приложение Infrastructure & Operations визуализирует эти данные, см. [Supercharge your end-to-end infrastructure and operations observability experience](https://dt-url.net/vm03xd1) (блог Dynatrace).

## Сценарий

Это руководство проведёт вас через концепции, связывающие эту топологию воедино, и объяснит, как вы — как разработчик расширений или интегратор данных — можете использовать ту же модель.

Поскольку это техническое руководство, мы рассмотрим полный пример на основе упрощённой версии расширения F5 BIG-IP.

К этому руководству прилагаются три манифеста расширений:

* `1_initial.yaml` — немодифицированное расширение.

  Оно отслеживает балансировщик нагрузки F5, отправляя данные в Dynatrace, но без какого-либо знания модели.
* `2_basic.yaml` — демонстрирует базовое использование.

  Dynatrace теперь знает, что балансировщик нагрузки F5 является сетевым устройством с интерфейсами и портами. Другие приложения также будут его отображать.
* `3_advanced.yaml` — демонстрирует расширенное использование.

  Сетевое устройство и интерфейс теперь имеют доступ к большему количеству данных. Сетевому устройству также добавлены дополнительные атрибуты и графики для отображения.

Сведения об этих файлах см. в разделе [Файлы манифестов](#manifest-files) ниже.

Для более чёткого сравнения изменений между тремя манифестами можно использовать онлайн-инструмент, например [diffchecker](https://www.diffchecker.com/text-compare/).

## Шаг 1 Ключевые концепции

Важно понимать, что модель топологии в значительной мере определяется расширением SNMP Autodiscovery. Другим расширениям и интеграциям нужно лишь убедиться, что правильные данные отправляются в Dynatrace, и при необходимости определить дополнительные графики для отображения в веб-интерфейсе.

Рассмотрим сущности топологии и взаимосвязи.

### Сетевое устройство

(`network:device`)

* Сетевое устройство — это физическое устройство в сети. Это основная сущность, на которой работает ОС и выполняются технологии, необходимые для сетевых коммуникаций и других возможностей.
* Сетевое устройство идентифицируется по IP-адресу управления и обозначается системным именем.

### Сетевой порт

(`network:port`)

* Сетевой порт — это физический аппаратный сетевой порт на сетевом устройстве.
* Сетевой порт идентифицируется и обозначается своим MAC-адресом.

### Сетевой интерфейс

(`network:interface`)

* Сетевой интерфейс — это физический или виртуальный сетевой интерфейс (NIC). Как правило, это первая точка отсчёта при сетевых коммуникациях между устройствами.
* Сетевой интерфейс идентифицируется сочетанием MAC-адреса и имени интерфейса и обозначается своим именем.

### Взаимосвязи

Эти типы сущностей связаны следующими взаимосвязями:

* `network:port` `-runsOn->` `network:device`
* `network:interface` `-runsOn->` `network:device`
* `network:interface` `-isChildOf->` `network:port`

## Шаг 2 Базовое использование

Как упоминалось ранее, другим расширениям и интеграциям нужно лишь отправлять данные в правильном формате для использования этой топологии. Обязательные измерения должны присутствовать во всех метриках, тогда как необязательные измерения можно добавить к одной метрике для уменьшения излишнего разбиения данных.

### Измерения и метрики для сетевых устройств

Для сетевых устройств доступны следующие метрики и измерения.

* **Обязательные измерения**:

  + Ключ: `device.address`

    Использование: идентифицирует каждое устройство и определяет момент создания новых экземпляров сущностей
  + Ключ: `monitoring.mode`

    Использование: должно иметь фиксированное значение "Extension". Это влияет на интерфейс и сообщает Dynatrace, что данная сущность отслеживается.
  + Ключ: `sys.name`

    Использование: даёт устройству метку, обеспечивая сущности имя.
  + Ключ: `device.type`

    Использование: строка для обозначения типа устройства. Может быть именем технологии, производителем/моделью или просто меткой, например "L3 Switch". Заполнит атрибут `devType` сущности.
* **Необязательные (рекомендуемые) измерения**:

  + Ключ: `device.port`

    Использование: регистрирует прослушиваемый порт на устройстве. Дополнительные сущности не создаются, но атрибут `dt.listen\ports` будет заполнен из него.
  + Ключ: `sys.description`

    Использование: регистрирует описание устройства в атрибуте devDescription. Может быть информацией о производителе или любым описательным текстом.
* **Метрики**:

  + Ключ: `com.dynatrace.extension.network_device.sysuptime`

    Описание: время в системных тиках (1/100 секунды) с момента последней перезагрузки системы.
  + Ключ: `com.dynatrace.extension.network_device.cpu_usage`

    Описание: использование процессора системы, выраженное в процентах
  + Ключ: `com.dynatrace.extension.network_device.cpu_ratio`

    Описание: использование процессора системы, выраженное в виде отношения
  + Ключ: `com.dynatrace.extension.network_device.memory_used`

    Описание: объём памяти в килобайтах, используемый устройством
  + Ключ: `com.dynatrace.extension.network_device.memory_free`

    Описание: объём памяти в килобайтах, в настоящее время свободный на устройстве
  + Ключ: `com.dynatrace.extension.network_device.memory_total`

    Описание: общий (используемый и свободный) объём памяти в килобайтах, доступный на устройстве
  + Ключ: `com.dynatrace.extension.network_device.memory_usage`

    Описание: текущее использование памяти устройством, выраженное как процент от общей памяти

### Измерения и метрики для сетевых интерфейсов

Для сетевых интерфейсов доступны следующие метрики и измерения.

* **Обязательные измерения**:

  + Ключ: `mac.address`

    Использование: в сочетании с именем идентифицирует каждый интерфейс и момент создания новых экземпляров сущностей. Отдельно также идентифицирует сетевые порты и момент создания новых экземпляров.
  + Ключ: `if.name`

    Использование: в сочетании с MAC-адресом идентифицирует каждый интерфейс. Также даёт каждой сущности интерфейса имя.
* **Метрики**:

  + Ключ: `com.dynatrace.extension.network_device.if.status`

    Описание: метрика состояния, представляющая сетевой интерфейс, значение которой всегда равно 1, а её измерения указывают детали состояния.

    Дополнительные измерения (извлекаются как атрибуты сущности):
  + Ключ: `oper.status`

    Использование: рабочее состояние интерфейса (up/down/и т. д.).
  + Ключ: `admin.status`

    Использование: административное состояние интерфейса (up/down/и т. д.).
  + Ключ: `if.speed`

    Использование: скорость/пропускная способность интерфейса.
  + Ключ: `com.dynatrace.extension.network_device.if.bytes_in.count`

    Описание: объём трафика в байтах, входящего на сетевой интерфейс.
  + Ключ: `com.dynatrace.extension.network_device.if.bytes_out.count`

    Описание: объём трафика в байтах, исходящего из сетевого интерфейса.

### Чего следует ожидать на этом этапе?

Это должно гарантировать правильное создание сущностей сетевого устройства, сетевого порта и сетевого интерфейса на основе ваших данных. На данном этапе можно использовать приложение (Классические) Технологии или Infrastructure & Operations для визуализации этих устройств.

* В приложении (Классические) Технологии перейдите по адресу `../ui/apps/dynatrace.classic.technologies/ui/entity/list/network:interface`

  ![Сетевые устройства](https://dt-cdn.net/images/network-devices-classic-1105-6a410f8f74.png)
* В приложении Infrastructure & Operations выберите вкладку **Сетевые устройства**

  ![Сетевые устройства](https://dt-cdn.net/images/389541815-e685532f-7ddc-40c5-9b08-0d40e494e4af-1177-f87f6dc4be.png)

## Шаг 3 Расширенное использование

Опираясь на предыдущие изменения, этот раздел посвящён тому, как расширить сетевую модель с помощью дополнительных метрик, взаимосвязей с существующими сущностями и настройки интерфейса.

Во многих случаях у вас уже есть расширение или интеграция, отправляющие специализированные данные о конкретном типе сетевого устройства. В таких ситуациях модель может использоваться для создания связей "то же самое, что" от ваших существующих сущностей к универсальным, эффективно добавляя к ним новые метрики, настраивая их атрибуты и внедряя некоторые существующие графики в их интерфейс.

После реализации предложенных изменений выполните следующие дополнительные шаги:

1. Присоедините существующие данные к сетевому устройству:

   * Создайте новую запись в `topology.types` следующим образом:

     ```
     - name: network:device


     enabled: true


     displayName: Network device


     rules: [] # You will populate this at the next step
     ```
   * Добавьте правила для присоединения данных к сущности (замените `[]`)

     Примечание: можно определить существующий тип сущности, похожий на сетевое устройство, и скопировать все правила из его определения

     Убедитесь, что каждое правило определяет следующее:

     ```
     - idPattern: network_device_{device.address}


     instanceNamePattern: "{sys.name}"


     role: default
     ```

     Примечание: `device.address` и `sys.name` — это заполнители, которые могут содержать любое другое измерение, но они должны идентифицировать IP-адрес управления и имя устройства.
2. Присоедините существующие данные к сетевому интерфейсу:

   * Создайте новую запись в `topology.types` следующим образом:

     ```
     - name: network:interface


     enabled: true


     displayName: Network interface


     rules: [] # You will populate this in the next step
     ```
   * Добавьте правила для присоединения данных к сущности (замените `[]` выше).

     Примечание: можно определить существующий тип, похожий на сетевой интерфейс, и скопировать все правила из его определения.

     Убедитесь, что каждое правило определяет следующее:

     ```
     - idPattern: network_interface_{mac.address}_{if.name}


     instanceNamePattern: "{if.name}"


     role: default
     ```

     Примечание: `mac.address` и `if.name` — это заполнители, которые могут содержать любое другое измерение, но они должны идентифицировать MAC-адрес и имя интерфейса.
3. Создайте связи "то же самое, что":

   * Создайте две записи в `topology.relationships`. Каждая должна быть основана на данных, аналогичных тем, что использовались на предыдущих шагах.

     ```
     - fromType: ""  # Add your existing entity type that resembles a network device


     typeOfRelation: SAME_AS


     toType: `network:device`


     sources:


     - sourceType: Metrics


     condition: ""  # Match any of the metrics that you used for the network:device entity rule


     - fromType: ""  # Add your existing entity type that resembles a network interface


     typeOfRelation: SAME_AS


     toType: `network:interface`


     sources:


     - sourceType: Metrics


     condition: ""  # Match any of the metrics that you used for the network:interface entity rule
     ```
4. Настройте интерфейс:

   * Создайте новую запись в `screens` для сетевого устройства:

     ```
     screens:


     - entityType: network:device
     ```
   * Отобразите ссылку для перехода к специализированной сущности:

     Добавьте свойство типа `RELATION` в `propertiesCard`, указывающее на существующую сущность

     ```
     propertiesCard:


     properties:


     - type: RELATION


     relation:


     # replace your_type with your existing entity type


     entitySelectorTemplate: type(your_type),fromRelationships.isSameAs($(entityConditions))


     displayName: Linked entity


     conditions:


     # Replace your_type with your existing entity type


     - relatedEntity|entitySelectorTemplate=type(your_type),fromRelationships.isSameAs($(entityConditions))


     # Ensures it only appears on monitored devices


     - entityAttribute|devMonitoringMode=Extension
     ```
   * Отобразите существующие графики на экране сетевого устройства:

     Проще всего внедрить их по ссылке из экрана существующей сущности.

     **Примечание:** Никогда не определяйте ничего в `detailsSettings`, всегда используйте `detailsInjections`.

     ```
     detailsInjections:


     - type: CHART_GROUP


     key: my-custom-chart


     # replace your_type with your existing entity type


     entitySelectorTemplate: type(your_type),fromRelationships.isSameAs($(entityConditions))


     conditions:


     # Replace your_type with your existing entity type


     - relatedEntity|entitySelectorTemplate=type(your_type),fromRelationships.isSameAs($(entityConditions))


     # Ensures it only appears on monitored devices


     - entityAttribute|devMonitoringMode=Extension
     ```
   * Определите новые графики для сетевого устройства:

     ```
     detailsInjections:


     - type: CHART_GROUP


     key: my-custom-chart


     conditions:


     # Ensures it only appears on monitored devices


     - entityAttribute|devMonitoringMode=Extension


     chartsCards:


     - key: my-custom-chart


     type: CHART_GROUP


     # Rest of definition goes here...
     ```

### Чего следует ожидать на этом этапе?

Сущность сетевого устройства связана с расширенным набором метрик (поступающих из специализированного расширения), сообщает дополнительные атрибуты, отображает часть данных специализированного расширения на своей странице сведений и сохраняет ссылку для перехода к специализированной сущности.

![Обзор сетевого устройства](https://dt-cdn.net/images/network-device-overview-1473-e9624340d5.png)

## Файлы манифестов

### `1_initial.yaml`

Это немодифицированное расширение.

Оно отслеживает балансировщик нагрузки F5, отправляя данные в Dynatrace, но без какого-либо знания модели.

Show me the `1_initial.yaml` manifest file

```
name: custom:f5-load-balancer


version: 1.0.0


minDynatraceVersion: 1.289.0


author:


name: Dynatrace


snmp:


- group: f5


interval:


minutes: 1


dimensions:


- key: instance.name


value: oid:1.3.6.1.2.1.1.5.0


- key: failover.state


value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0


- key: sync.state


value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0


subgroups:


- subgroup: f5-instance-details


table: false


dimensions:


- key: instance.systemname


value: oid:1.3.6.1.4.1.3375.2.1.6.1.0


- key: instance.systemrelease


value: oid:1.3.6.1.4.1.3375.2.1.6.3.0


- key: instance.systemarch


value: oid:1.3.6.1.4.1.3375.2.1.6.5.0


- key: instance.productversion


value: oid:1.3.6.1.4.1.3375.2.1.4.2.0


metrics:


- key: f5.lb.sys.uptime


value: oid:1.3.6.1.4.1.3375.2.1.6.6.0


- subgroup: f5-interface-details


featureSet: interface


table: true


dimensions:


- key: interface.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1


- key: interface.enabled


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8


- key: interface.status


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17


- key: mac.address


value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)


metrics:


- key: f5.lb.sys.interface.status


value: const:1


- subgroup: f5-interface-metrics


featureSet: interface


table: true


dimensions:


- key: interface.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1


metrics:


- key: f5.lb.sys.interface.stat.bytes.in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3


type: count


- key: f5.lb.sys.interface.stat.bytes.out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5


type: count


- key: f5.lb.sys.interface.stat.pkts.in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2


type: count


- key: f5.lb.sys.interface.stat.pkts.out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4


type: count


- subgroup: f5-cpu


table: false


featureSet: instance-cpu


metrics:


- key: f5.lb.sys.global.host.cpu.idle1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0


- key: f5.lb.sys.global.host.cpu.iowait1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0


- key: f5.lb.sys.global.host.cpu.irq1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0


- key: f5.lb.sys.global.host.cpu.softirq1min


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0


- key: f5.lb.sys.global.host.cpu.stolen1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0


- key: f5.lb.sys.global.host.cpu.system1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0


- key: f5.lb.sys.global.host.cpu.user1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0


- subgroup: f5-memory


table: false


featureSet: instance-memory


metrics:


- key: f5.lb.sys.host.memory.total


value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0


- key: f5.lb.sys.host.memory.used


value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0


topology:


types:


- name: f5lb:instance


displayName: F5 BIG-IP Instance


rules:


- idPattern: f5_instance_{instance.name}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.uptime)


attributes:


- key: dt.ip_addresses


displayName: IP Address


pattern: '{device.address}'


- key: dt.dns_names


displayName: DNS Name


pattern: '{instance.name}'


- key: OSRelease


displayName: OS release


pattern: '{instance.systemrelease}'


- key: OSArchitecture


displayName: OS architecture


pattern: '{instance.systemarch}'


- key: OSName


displayName: OS name


pattern: '{instance.systemname}'


- key: ProductVersion


displayName: Product version


pattern: '{instance.productversion}'


- key: FailoverStatus


pattern: '{failover.state}'


displayName: Failover status


- key: SyncStatus


pattern: '{sync.state}'


displayName: Config sync status


role: default


- idPattern: f5_instance_{instance.name}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $prefix(f5.lb)


requiredDimensions: []


attributes: []


role: default


- name: f5lb:interface


displayName: F5 BIG-IP Interface


rules:


- idPattern: f5_interface_{instance.name}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.interface.status)


attributes:


- key: EnabledState


displayName: Enabled State


pattern: '{interface.enabled}'


- key: MacAddress


displayName: MAC Address


pattern: '{mac.address}'


- key: Status


displayName: Status


pattern: '{interface.status}'


role: default


- idPattern: f5_interface_{instance.name}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


requiredDimensions: []


attributes: []


role: default


relationships:


- fromType: f5lb:interface


typeOfRelation: RUNS_ON


toType: f5lb:instance


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


screens:


- entityType: f5lb:instance


detailsSettings:


staticContent:


showProblems: true


showProperties: true


showTags: true


showGlobalFilter: true


showAddTag: true


target: BOTH


layout:


autoGenerate: false


cards:


- key: f5_instance-charts-cpu


type: CHART_GROUP


- key: f5_instance-charts-memory


type: CHART_GROUP


chartsCards:


- key: f5_instance-charts-cpu


target: BOTH


mode: NORMAL


displayName: CPU


numberOfVisibleCharts: 4


chartsInRow: 4


charts:


- displayName: CPU Breakdown


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


stacked: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: Idle


- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: System


- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: User


visualization:


themeColor: DEFAULT


seriesType: AREA


- displayName: System CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- displayName: User CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- displayName: Idle CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- key: f5_instance-charts-memory


target: BOTH


mode: NORMAL


displayName: Memory


numberOfVisibleCharts: 4


hideEmptyCharts: true


charts:


- displayName: Memory breakdown


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


yAxes:


- key: y-absolute


position: LEFT


visible: true


- key: y-relative


position: RIGHT


visible: true


min: '0'


max: '100'


metrics:


- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


yAxisKey: y-absolute


visualization:


themeColor: BLUE


seriesType: AREA


displayName: Total


- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


yAxisKey: y-absolute


visualization:


themeColor: ORANGE


seriesType: AREA


displayName: Used
```

### `2_basic.yaml`

This showcases basic usage.

Dynatrace now knows that the F5 load balancer is a network device with interfaces and ports. Other apps will show it too.

Show me the `2_basic.yaml` manifest file

```
name: custom:f5-load-balancer


version: 1.1.0


minDynatraceVersion: 1.289.0


author:


name: Dynatrace


# In this example, we add the basic metrics & dimensions for the network model.


# We chose to spread them in-between the existing metrics where possible, but


# they could just as well be extracted into separate groups & subgroups.


snmp:


- group: f5


interval:


minutes: 1


dimensions:


- key: instance.name


value: oid:1.3.6.1.2.1.1.5.0


- key: failover.state


value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0


- key: sync.state


value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0


# Adding the mandatory dimensions here ensures they appear everywhere


- key: monitoring.mode


value: const:Extension


- key: sys.name


value: oid:1.3.6.1.2.1.1.5.0


- key: device.type


value: const:F5 Load balancer


subgroups:


- subgroup: f5-instance-details


table: false


dimensions:


- key: instance.systemname


value: oid:1.3.6.1.4.1.3375.2.1.6.1.0


- key: instance.systemrelease


value: oid:1.3.6.1.4.1.3375.2.1.6.3.0


- key: instance.systemarch


value: oid:1.3.6.1.4.1.3375.2.1.6.5.0


- key: instance.productversion


value: oid:1.3.6.1.4.1.3375.2.1.4.2.0


metrics:


- key: f5.lb.sys.uptime


value: oid:1.3.6.1.4.1.3375.2.1.6.6.0


- key: com.dynatrace.extension.network_device.sysuptime


value: oid:1.3.6.1.4.1.3375.2.1.6.6.0


- subgroup: f5-interface-details


featureSet: interface


table: true


dimensions:


- key: interface.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1


- key: if.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1


- key: interface.enabled


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8


- key: interface.status


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17


- key: mac.address


value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)


metrics:


- key: f5.lb.sys.interface.status


value: const:1


- key: com.dynatrace.extension.network_device.if.status


value: const:1


- subgroup: f5-interface-metrics


featureSet: interface


table: true


dimensions:


- key: interface.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1


metrics:


- key: f5.lb.sys.interface.stat.bytes.in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3


type: count


- key: f5.lb.sys.interface.stat.bytes.out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5


type: count


- key: com.dynatrace.extension.network_device.if.bytes_in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3


type: count


- key: com.dynatrace.extension.network_device.if.bytes_out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5


type: count


- key: f5.lb.sys.interface.stat.pkts.in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2


type: count


- key: f5.lb.sys.interface.stat.pkts.out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4


type: count


- subgroup: f5-cpu


table: false


featureSet: instance-cpu


metrics:


- key: com.dynatrace.extension.network_device.cpu_usage


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.29.0


- key: f5.lb.sys.global.host.cpu.idle1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0


- key: f5.lb.sys.global.host.cpu.iowait1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0


- key: f5.lb.sys.global.host.cpu.irq1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0


- key: f5.lb.sys.global.host.cpu.softirq1min


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0


- key: f5.lb.sys.global.host.cpu.stolen1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0


- key: f5.lb.sys.global.host.cpu.system1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0


- key: f5.lb.sys.global.host.cpu.user1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0


- subgroup: f5-memory


table: false


featureSet: instance-memory


metrics:


- key: f5.lb.sys.host.memory.total


value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0


- key: f5.lb.sys.host.memory.used


value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0


- key: com.dynatrace.extension.network_device.memory_used


value: oid:1.3.6.1.4.1.3375.2.1.7.1.4.0


- key: com.dynatrace.extension.network_device.memory_total


value: oid:1.3.6.1.4.1.3375.2.1.7.1.3.0


topology:


types:


- name: f5lb:instance


displayName: F5 BIG-IP Instance


rules:


- idPattern: f5_instance_{instance.name}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.uptime)


attributes:


- key: dt.ip_addresses


displayName: IP Address


pattern: '{device.address}'


- key: dt.dns_names


displayName: DNS Name


pattern: '{instance.name}'


- key: OSRelease


displayName: OS release


pattern: '{instance.systemrelease}'


- key: OSArchitecture


displayName: OS architecture


pattern: '{instance.systemarch}'


- key: OSName


displayName: OS name


pattern: '{instance.systemname}'


- key: ProductVersion


displayName: Product version


pattern: '{instance.productversion}'


- key: FailoverStatus


pattern: '{failover.state}'


displayName: Failover status


- key: SyncStatus


pattern: '{sync.state}'


displayName: Config sync status


role: default


- idPattern: f5_instance_{instance.name}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $prefix(f5.lb)


requiredDimensions: []


attributes: []


role: default


- name: f5lb:interface


displayName: F5 BIG-IP Interface


rules:


- idPattern: f5_interface_{instance.name}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.interface.status)


attributes:


- key: EnabledState


displayName: Enabled State


pattern: '{interface.enabled}'


- key: MacAddress


displayName: MAC Address


pattern: '{mac.address}'


- key: Status


displayName: Status


pattern: '{interface.status}'


role: default


- idPattern: f5_interface_{instance.name}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


requiredDimensions: []


attributes: []


role: default


relationships:


- fromType: f5lb:interface


typeOfRelation: RUNS_ON


toType: f5lb:instance


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


screens:


- entityType: f5lb:instance


detailsSettings:


staticContent:


showProblems: true


showProperties: true


showTags: true


showGlobalFilter: true


showAddTag: true


target: BOTH


layout:


autoGenerate: false


cards:


- key: f5_instance-charts-cpu


type: CHART_GROUP


- key: f5_instance-charts-memory


type: CHART_GROUP


chartsCards:


- key: f5_instance-charts-cpu


target: BOTH


mode: NORMAL


displayName: CPU


numberOfVisibleCharts: 4


chartsInRow: 4


charts:


- displayName: CPU Breakdown


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


stacked: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: Idle


- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: System


- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: User


visualization:


themeColor: DEFAULT


seriesType: AREA


- displayName: System CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- displayName: User CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- displayName: Idle CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- key: f5_instance-charts-memory


target: BOTH


mode: NORMAL


displayName: Memory


numberOfVisibleCharts: 4


hideEmptyCharts: true


charts:


- displayName: Memory breakdown


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


yAxes:


- key: y-absolute


position: LEFT


visible: true


- key: y-relative


position: RIGHT


visible: true


min: '0'


max: '100'


metrics:


- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


yAxisKey: y-absolute


visualization:


themeColor: BLUE


seriesType: AREA


displayName: Total


- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


yAxisKey: y-absolute


visualization:


themeColor: ORANGE


seriesType: AREA


displayName: Used
```

### `3_advanced.yaml`

This showcases advanced usage.

The network device and interface now have access to more data. The network device has also been given additional attributes and charts to display.

Show me the `3_advanced.yaml` manifest file

```
name: custom:f5-load-balancer


version: 1.2.0


minDynatraceVersion: 1.289.0


author:


name: Dynatrace


# In this example, we add topology rules for customizing the network model.


# And modify the screens to customize the UI of the network device.


# All other changes done so far stay the same.


snmp:


- group: f5


interval:


minutes: 1


dimensions:


- key: instance.name


value: oid:1.3.6.1.2.1.1.5.0


- key: failover.state


value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0


- key: sync.state


value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0


# Adding the mandatory dimensions here ensures they appear everywhere


- key: monitoring.mode


value: const:Extension


- key: sys.name


value: oid:1.3.6.1.2.1.1.5.0


- key: device.type


value: const:F5 Load balancer


subgroups:


- subgroup: f5-instance-details


table: false


dimensions:


- key: instance.systemname


value: oid:1.3.6.1.4.1.3375.2.1.6.1.0


- key: instance.systemrelease


value: oid:1.3.6.1.4.1.3375.2.1.6.3.0


- key: instance.systemarch


value: oid:1.3.6.1.4.1.3375.2.1.6.5.0


- key: instance.productversion


value: oid:1.3.6.1.4.1.3375.2.1.4.2.0


metrics:


- key: f5.lb.sys.uptime


value: oid:1.3.6.1.4.1.3375.2.1.6.6.0


- key: com.dynatrace.extension.network_device.sysuptime


value: oid:1.3.6.1.4.1.3375.2.1.6.6.0


- subgroup: f5-interface-details


featureSet: interface


table: true


dimensions:


- key: interface.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1


- key: if.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1


- key: interface.enabled


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8


- key: interface.status


value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17


- key: mac.address


value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)


metrics:


- key: f5.lb.sys.interface.status


value: const:1


- key: com.dynatrace.extension.network_device.if.status


value: const:1


- subgroup: f5-interface-metrics


featureSet: interface


table: true


dimensions:


- key: interface.name


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1


metrics:


- key: f5.lb.sys.interface.stat.bytes.in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3


type: count


- key: f5.lb.sys.interface.stat.bytes.out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5


type: count


- key: com.dynatrace.extension.network_device.if.bytes_in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3


type: count


- key: com.dynatrace.extension.network_device.if.bytes_out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5


type: count


- key: f5.lb.sys.interface.stat.pkts.in.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2


type: count


- key: f5.lb.sys.interface.stat.pkts.out.count


value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4


type: count


- subgroup: f5-cpu


table: false


featureSet: instance-cpu


metrics:


- key: com.dynatrace.extension.network_device.cpu_usage


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.29.0


- key: f5.lb.sys.global.host.cpu.idle1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0


- key: f5.lb.sys.global.host.cpu.iowait1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0


- key: f5.lb.sys.global.host.cpu.irq1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0


- key: f5.lb.sys.global.host.cpu.softirq1min


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0


- key: f5.lb.sys.global.host.cpu.stolen1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0


- key: f5.lb.sys.global.host.cpu.system1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0


- key: f5.lb.sys.global.host.cpu.user1m


value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0


- subgroup: f5-memory


table: false


featureSet: instance-memory


metrics:


- key: f5.lb.sys.host.memory.total


value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0


- key: f5.lb.sys.host.memory.used


value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0


- key: com.dynatrace.extension.network_device.memory_used


value: oid:1.3.6.1.4.1.3375.2.1.7.1.4.0


- key: com.dynatrace.extension.network_device.memory_total


value: oid:1.3.6.1.4.1.3375.2.1.7.1.3.0


topology:


types:


# These are already existing rules which we can copy & adjust


- name: f5lb:instance # Closely resembles a network device


displayName: F5 BIG-IP Instance


rules:


- idPattern: f5_instance_{instance.name}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.uptime)


attributes:


- key: dt.ip_addresses


displayName: IP Address


pattern: '{device.address}'


- key: dt.dns_names


displayName: DNS Name


pattern: '{instance.name}'


- key: OSRelease


displayName: OS release


pattern: '{instance.systemrelease}'


- key: OSArchitecture


displayName: OS architecture


pattern: '{instance.systemarch}'


- key: OSName


displayName: OS name


pattern: '{instance.systemname}'


- key: ProductVersion


displayName: Product version


pattern: '{instance.productversion}'


- key: FailoverStatus


pattern: '{failover.state}'


displayName: Failover status


- key: SyncStatus


pattern: '{sync.state}'


displayName: Config sync status


role: default


- idPattern: f5_instance_{instance.name}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $prefix(f5.lb)


requiredDimensions: []


attributes: []


role: default


- name: f5lb:interface # Closely resembles a network interface


displayName: F5 BIG-IP Interface


rules:


- idPattern: f5_interface_{instance.name}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.interface.status)


attributes:


- key: EnabledState


displayName: Enabled State


pattern: '{interface.enabled}'


- key: MacAddress


displayName: MAC Address


pattern: '{mac.address}'


- key: Status


displayName: Status


pattern: '{interface.status}'


role: default


- idPattern: f5_interface_{instance.name}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


requiredDimensions: []


attributes: []


role: default


# These are new rules added to customize the model


- name: network:device


enabled: true


displayName: Network device


rules:


- idPattern: network_device_{device.address} # must follow `network_device_{...}` pattern


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.uptime) # It's important to target specialized metrics, not the generic ones


attributes:


- key: dt.ip_addresses


displayName: IP Address


pattern: '{device.address}'


- key: dt.dns_names


displayName: DNS Name


pattern: '{instance.name}'


- key: OSRelease


displayName: OS release


pattern: '{instance.systemrelease}'


- key: OSArchitecture


displayName: OS architecture


pattern: '{instance.systemarch}'


- key: OSName


displayName: OS name


pattern: '{instance.systemname}'


- key: ProductVersion


displayName: Product version


pattern: '{instance.productversion}'


- key: FailoverStatus


pattern: '{failover.state}'


displayName: Failover status


- key: SyncStatus


pattern: '{sync.state}'


displayName: Config sync status


role: default


- idPattern: network_device_{device.address}


instanceNamePattern: '{instance.name}'


iconPattern: f5


sources:


- sourceType: Metrics


condition: $prefix(f5.lb)


requiredDimensions: []


attributes: []


role: default


- name: network:interface


enabled: true


displayName: Network interface


rules:


- idPattern: network_interface_{mac.address}_{interface.name} # must follow `network_interface_{...}_{...}` pattern


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $eq(f5.lb.sys.interface.status) # Again, we target specialized metrics, not generic ones


attributes:


- key: EnabledState


displayName: Enabled State


pattern: '{interface.enabled}'


- key: MacAddress


displayName: MAC Address


pattern: '{mac.address}'


- key: ifOperStatus


displayName: Operational status


pattern: '{interface.status}'


role: default


- idPattern: network_interface_{mac.address}_{interface.name}


instanceNamePattern: '{interface.name}'


iconPattern: network-interfaces


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


requiredDimensions: []


attributes: []


role: default


relationships:


- fromType: f5lb:interface


typeOfRelation: RUNS_ON


toType: f5lb:instance


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


# Adding the same as relationships


- fromType: f5lb:interface


typeOfRelation: SAME_AS


toType: network:interface


sources:


- sourceType: Metrics


condition: $prefix(f5.lb.sys.interface)


- fromType: f5lb:instance


typeOfRelation: SAME_AS


toType: network:device


sources:


- sourceType: Metrics


condition: $prefix(f5.lb)


screens:


# Customizing the screen for the network device


- entityType: network:device


propertiesCard:


properties:


# Show a link to the specialized entity


- type: RELATION


relation:


entitySelectorTemplate: type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))


displayName: F5 Load balancer


conditions:


# Apply only to devices that have a same as relation, who are monitored by Extension


# These 2 conditions are used althroughout the screen definition


- relatedEntity|entitySelectorTemplate=type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))


- entityAttribute|devMonitoringMode=Extension


# Must define everything in `detailsInjections` and not `detailsSettings`!


detailsInjections:


# This card is injected by reference, meaning we don't have to duplicate the definition again


- type: CHART_GROUP


key: f5_instance-charts-cpu


# When using `entitySelectorTemplate`, the card is understood to be defined as part of the


# resolved entity's screen definition, and not the current screen definition.


entitySelectorTemplate: type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))


conditions:


- relatedEntity|entitySelectorTemplate=type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))


- entityAttribute|devMonitoringMode=Extension


# Of course, full definitions are still supported


- type: CHART_GROUP


key: network-interfaces-list


chartsCards:


- key: network-interfaces-list


mode: NORMAL


target: BOTH # Use CLASSIC for Managed, PLATFORM for Platform, or BOTH for both


displayName: Traffic


numberOfVisibleCharts: 1


conditions:


# Even if your card is generic, you should still apply this condition so that only


# monitored devices display the card.


- entityAttribute|devMonitoringMode=Extension


charts:


- displayName: Traffic in/out


visualizationType: GRAPH_CHART


graphChartConfig:


metrics:


# metricSelector is required for Managed


- metricSelector: com.dynatrace.extension.network_device.if.bytes_in.count:splitBy("dt.entity.network:device)


# dqlQuery is required for Platform


dqlQuery: timeseries bytesIn=avg(com.dynatrace.extension.network_device.if.bytes_in.count),by:{`dt.entity.network:device`},filter:{`dt.entity.network:device`==$(entityId)}


visualization:


displayName: Bytes In


- metricSelector: com.dynatrace.extension.network_device.if.bytes_out.count:splitBy("dt.entity.network:device")


dqlQuery: timeseries bytesOut=avg(com.dynatrace.extension.network_device.if.bytes_out.count),by:{`dt.entity.network:device`},filter:{`dt.entity.network:device`==$(entityId)}


visualization:


displayName: Bytes Out


- entityType: f5lb:instance


detailsSettings:


staticContent:


showProblems: true


showProperties: true


showTags: true


showGlobalFilter: true


showAddTag: true


target: BOTH


layout:


autoGenerate: false


cards:


- key: f5_instance-charts-cpu


type: CHART_GROUP


- key: f5_instance-charts-memory


type: CHART_GROUP


chartsCards:


- key: f5_instance-charts-cpu


target: BOTH


mode: NORMAL


displayName: CPU


numberOfVisibleCharts: 4


chartsInRow: 4


charts:


- displayName: CPU Breakdown


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


stacked: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: Idle


- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: System


- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


displayName: User


visualization:


themeColor: DEFAULT


seriesType: AREA


- displayName: System CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- displayName: User CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- displayName: Idle CPU


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


metrics:


- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


visualization:


themeColor: BLUE


seriesType: LINE


- key: f5_instance-charts-memory


target: BOTH


mode: NORMAL


displayName: Memory


numberOfVisibleCharts: 4


hideEmptyCharts: true


charts:


- displayName: Memory breakdown


visualizationType: GRAPH_CHART


graphChartConfig:


connectGaps: true


yAxes:


- key: y-absolute


position: LEFT


visible: true


- key: y-relative


position: RIGHT


visible: true


min: '0'


max: '100'


metrics:


- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


yAxisKey: y-absolute


visualization:


themeColor: BLUE


seriesType: AREA


displayName: Total


- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")


dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}


yAxisKey: y-absolute


visualization:


themeColor: ORANGE


seriesType: AREA


displayName: Used
```

## FAQ

### Where does `device.address` come from?

You may have noticed there's no special OID-based capturing of the `device.address` dimension in the shared manifests. This is because the example given is based on the SNMP data source, which automatically adds these dimensions to every collected metric.

### Can this guide be used for any extension data source?

Yes. SNMP was given as an example as it is focused on network devices, but any extension can leverage this topology model so long as it sends the same metrics and dimensions described in this guide.

### Is it possible to extend the details UI within the Infrastructure & Operations Infrastructure & Operations app?

Not yet, but this capability is expected to be available soon, at which point this guide will be updated to include the additional usage details.