---
title: Учебное руководство WMI: пользовательская топология
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04
scraped: 2026-05-12T11:11:38.160603
---

# WMI tutorial - пользовательская топология

# WMI tutorial - пользовательская топология

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 30 марта 2022 г.

Чётко определённая модель топологии помогает упорядочить все метрики и данные, поступающие в Dynatrace.

Для расширения Extensions вся настройка выполняется в разделе `topology`, который делится на две части:

* `types`: определяет новые типы сущностей, которые отслеживает расширение
* `relationships`: определяет наличие и характер связей между этими типами сущностей

## Ключевые аспекты при определении типов

* `idPattern`: должен быть достаточно уникальным, чтобы идентифицировать каждый экземпляр устройства без дублирования
* `sources`: должен определять правила для всех метрик расширения, которые разбиваются по данной сущности
* `condition`: поддерживает функции, например `$prefix(...)`, для определения шаблонов ключей метрик
* `attributes`: необязательные сведения, извлекаемые из измерений метрик

## Ключевые аспекты при определении связей

* `sources`: любая метрика, соответствующая шаблону, будет проверяться на наличие связи. Это означает,
  что метрика должна принадлежать обоим типам сущностей, участвующим в связи.

## Поиск новых сущностей в интерфейсе

Откройте `../ui/entity/list/{entity-type}` в вашей среде Dynatrace. Например:

* `../ui/entity/list/wmi:generic_host`
* `../ui/entity/list/wmi:generic_network_device`

## Задачи

1. Добавьте раздел `topology` в файл `extension.yaml` по приведённому шаблону.
2. Определите два типа сущностей: Generic Host и Generic Network Device.
3. Убедитесь, что сетевые устройства содержат информацию о типе (`Adapter` или `Interface`).
4. Создайте связь между ними: Generic Network Device работает на Generic Host.
5. Соберите и загрузите новую версию пакета расширения.
6. Проверьте, что новые сущности созданы.

Дополнительные сведения о расширении топологии Dynatrace см. в разделе [Пользовательская модель топологии](/managed/ingest-from/extend-dynatrace/extend-topology "Обеспечьте контекстную насыщенность всех входящих наблюдений и их анализ в контексте связанных сущностей.")

```
topology:



types:



- name: wmi:generic_host



displayName: Generic Host



enabled: true



rules:



- idPattern: wmi_generic_host_{dt.entity.host}



sources:



- sourceType: Metrics



condition: $prefix(custom.demo.host-observability)



attributes: []



requiredDimensions: []



instanceNamePattern: Generic Host on {dt.entity.host}



- name: wmi:generic_network_device



displayName: Network device



enabled: true



rules:



- idPattern: wmi_generic_{dt.entity.host}_{network.type}_{network.name}



sources:



- sourceType: Metrics



condition: $prefix(custom.demo.host-observability.network)



attributes:



- pattern: '{network.name}'



key: wmi_network_name



displayName: Name



- pattern: '{network.type}'



key: wmi_network_type



displayName: Type



requiredDimensions: []



instanceNamePattern: Network {network.type} {network.name} on {dt.entity.host}



relationships:



- typeOfRelation: RUNS_ON



fromType: wmi:generic_network_device



toType: wmi:generic_host



enabled: true



sources:



- sourceType: Metrics



condition: $prefix(custom.demo.host-observability)
```

## Результаты

Должны появиться новые сущности типов Generic Host и Generic Network Device:

![hosts](https://dt-cdn.net/images/wmi-tutorial-topology-host-865-f2a80aa24a.png)

hosts

![network_devices](https://dt-cdn.net/images/wmi-tutorial-topology-nic-945-00a3fef761.png)

network\_devices

**Следующий шаг**: [Страница унифицированного анализа](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-05 "Узнайте о расширениях WMI в платформе Extensions framework.")