---
title: Мониторинг метрик JMX в z/OS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics
scraped: 2026-05-12T11:24:13.931739
---

# Мониторинг метрик JMX в z/OS

# Мониторинг метрик JMX в z/OS

* Чтение: 5 мин
* Опубликовано 6 сентября 2022 г.

JMX (Java Management Extensions) удобен для мониторинга приложений, созданных на Java. С помощью кодового модуля z/OS Java OneAgent можно отслеживать любую метрику JVM, доступную через MBean.

* Каждая отслеживаемая пользовательская метрика JMX потребляет Davis data units. Концепция [Included metrics per host unit](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Узнайте, как рассчитывается потребление Davis data units и связанные расходы на мониторируемые метрики.") неприменима для мониторируемых LPAR в z/OS. Подробнее о Davis data units см. в разделе [DDUs for metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Узнайте, как рассчитывается потребление Davis data units и связанные расходы на мониторируемые метрики.").
* [PMI (Performance Monitoring Infrastructure)](https://www.ibm.com/docs/en/was/9.0.5?topic=health-performance-monitoring-infrastructure-pmi) для IBM WebSphere Application Server в настоящее время не поддерживается.

## Определение

Атрибут `customJmxMetrics` задаёт список [метрик](#metrics) для мониторинга. Чтобы начать, добавьте атрибут `customJmxMetrics` в файл `dtconfig.json`, как показано в следующем примере.

Как правило, файл `dtconfig.json` создаётся при [установке кодового модуля z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Настройте мониторинг Java в z/OS с помощью модуля Java."), где задаются атрибуты `Tenant`, `ClusterID` и `zdcName` для вашего окружения.

```
{



"Tenant": "myTenant",



"ClusterID": myCluster,



"ZdcName": "DEFAULT",



"customJmxMetrics": [



{



"name": "java.lang.CurrentThreadCount",



"source":



{



"domain": "java.lang",



"keyProperties": {



"type": "Threading",



},



"attribute": "ThreadCount"



}



}



]



}
```

## Метрики

Каждая метрика имеет следующие обязательные атрибуты:

| Поле | Тип | Описание |
| --- | --- | --- |
| `name` | String | Задаёт имя метрики в Dynatrace. Должно начинаться с буквы. Допустимы только буквенно-цифровые символы или `.`. |
| `source` | Object | Определяет способ сбора метрики. Подробнее см. раздел [Source](#source) ниже. |

## Source

Source определяет, как метрика собирается с помощью JMX. Каждый source имеет следующие обязательные атрибуты:

| Поле | Тип | Описание |
| --- | --- | --- |
| `domain` | String | Имя домена MBean. Может содержать символы подстановки (`*`). |
| `keyProperties` | Key, Value pairs | Ключевые свойства MBean. Значения могут содержать символы подстановки (`*`). |
| `attribute` | String | Имя атрибута, содержащего значение метрики. |

Необязательные атрибуты source:

| Поле | Тип | Описание |
| --- | --- | --- |
| `attributePath` | String | См. раздел [CompositeData] ниже.(#compositedata) |
| `allowAdditionalKeys` | Boolean | Если `true`, дополнительные ключевые свойства помимо указанных в `keyProperties` допустимы, но игнорируются. Если `false`, `keyProperties` должны совпадать точно; дополнительные ключи приведут к несовпадению. |
| `calculateDelta` | bool | Если `true`, вычисляется изменение значений указанного атрибута. Значение = attribute(t) - attribute(t-1). Полезно для монотонно возрастающих значений. |
| `calculateRate` | bool | Если `true`, вычисляется скорость изменений в секунду. Используется вместе с `calculateDelta` для преобразования абсолютного атрибута (например, Request Count) в скорость (например, Requests per Second). Значение = attribute / интервал запроса. |
| `aggregation` | String | Агрегирует несколько значений, если более одного MBean соответствует фильтру домена и ключевых свойств. Агрегация по умолчанию: `SUM`. Доступные агрегации: `SUM`, `AVG`, `MIN`, `MAX`. Например, можно агрегировать все `MemoryPools` и вычислять значение `SUM` или `MAX`. |
| `splittings` | List | Задаёт [splittings](#splittings). |

### AttributePath (CompositeData)

Чтобы извлечь значения отдельных ключей, возвращаемых атрибутом с типом `CompositeData`, используйте механизм `attributePath` и укажите нужный ключ.

Например, `HeapMemoryUsage` имеет тип `CompositeData` и возвращает следующий список пар ключ-значение:

```
{



committed: integer,



init: integer,



max: integer,



used: integer



}
```

Чтобы извлечь значение `used` из атрибута `HeapMemoryUsage`, укажите в `attributePath` ключ `used`.

```
{



"customJmxMetrics": [



{



"name": "java.lang.HeapMemoryUsage",



"source":



{



"domain": "java.lang",



"keyProperties": {



"type": "Memory"



},



"attribute": "HeapMemoryUsage",



"attributePath": "get(\"used\")"



}



}



]



}
```

### Splittings

Splittings позволяют задавать дополнительные измерения для метрики.

```
"splittings": [



{



"name": "dimension",



"keyProperty": "name"



}



]
```

Каждый splitting имеет следующие обязательные атрибуты:

| Поле | Тип | Описание |
| --- | --- | --- |
| `name` | String | Задаёт имя измерения. |
| `keyProperty` | String | Определяет, какое ключевое свойство `ObjectName` MBean используется для splitting. См. атрибут `keyProperties` раздела [source](#source). |

Следующий пример показывает, как задать метрику с несколькими измерениями в рамках одного определения метрики:

```
{



"customJmxMetrics": [



{



"name": "java.lang.MemoryPoolUsage",



"source":



{



"domain": "java.lang",



"keyProperties": {



"type": "MemoryPool",



"name": "*"



},



"attribute": "Usage",



"attributePath": "get(\"used\")",



"splittings": [



{



"name": "memory_type",



"keyProperty": "name"



}



]



}



}



]



}
```

На основе этого определения метрики следующие MBeans:

* `java.lang:type=MemoryPool,name=G1 Eden Space`
* `java.lang:type=MemoryPool,name=G1 Survivor Space`

дадут в Dynatrace одну метрику с двумя измерениями:

* `java.lang.MemoryPoolUsage` с измерением `memory_type=G1 Eden Space`
* `java.lang.MemoryPoolUsage` с измерением `memory_type=G1 Survivor Space`

## Мониторинг

Перейдите в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужной информации.") для анализа и построения графиков пользовательских метрик JMX. При необходимости можно закрепить графики на дашборде. В следующем примере показана метрика `java.lang.MemoryPoolUsage` с разбивкой по измерению `memory_type`:

![Data Explorer с метриками JMX z/OS](https://dt-cdn.net/images/data-explorer-1643-7696285fbf.png)

Data Explorer с метриками JMX z/OS

Чтобы получить список метрик, доступных в вашем окружении мониторинга, перейдите в **Metrics** для открытия [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."). В следующем примере показаны три метрики, созданные выше:

![Metrics browser с метриками JMX z/OS](https://dt-cdn.net/images/metrics-browser-1636-1096adef93.png)

Metrics browser с метриками JMX z/OS

## Связанные темы

* [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace.")
* [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужной информации.")