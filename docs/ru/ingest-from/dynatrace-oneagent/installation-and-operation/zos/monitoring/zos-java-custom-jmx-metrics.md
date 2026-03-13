---
title: Monitor JMX metrics on z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics
scraped: 2026-03-05T21:29:53.332272
---

# Мониторинг JMX-метрик на z/OS

# Мониторинг JMX-метрик на z/OS

* Последняя версия Dynatrace
* Чтение: 5 мин
* Опубликовано 6 сентября 2022

JMX (Java Management Extensions) -- удобный инструмент для мониторинга приложений, написанных на Java. С помощью модуля кода OneAgent z/OS Java вы можете отслеживать любую метрику в вашей JVM, которая доступна через MBean.

* Каждая пользовательская JMX-метрика, находящаяся под мониторингом, потребляет единицы данных Davis. Концепция [Включенных метрик на единицу хоста](../../../../../license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation.md#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") не применима для мониторируемых LPAR на z/OS. Подробнее о единицах данных Davis см. [DDU для метрик](../../../../../license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation.md "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").
* [PMI (Performance Monitoring Infrastructure)](https://www.ibm.com/docs/en/was/9.0.5?topic=health-performance-monitoring-infrastructure-pmi) для IBM WebSphere Application Server в настоящее время не поддерживается.

## Определение

Атрибут `customJmxMetrics` определяет список [метрик](#metrics) для мониторинга. Для начала работы добавьте атрибут `customJmxMetrics` в ваш файл `dtconfig.json`, как показано в следующем примере.

Обычно вы создаете файл `dtconfig.json` во время [установки модуля кода z/OS Java](../installation/install-zos-java.md#download "Set up Java monitoring on z/OS using the Java module.") и устанавливаете атрибуты `Tenant`, `ClusterID` и `zdcName` для вашей среды.

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
| `name` | String | Задает имя метрики в Dynatrace. Должно начинаться с буквы. Допускаются только буквенно-цифровые символы или `.`. |
| `source` | Object | Определяет способ сбора метрики. Подробности см. в разделе [Источник](#source) ниже. |

## Источник

Источник определяет, как метрика собирается с помощью JMX. Каждый источник имеет следующие обязательные атрибуты:

| Поле | Тип | Описание |
| --- | --- | --- |
| `domain` | String | Доменное имя MBean. Может содержать подстановочные символы (`*`). |
| `keyProperties` | Пары ключ-значение | Ключевые свойства MBean. Значения могут содержать подстановочные символы (`*`). |
| `attribute` | String | Имя атрибута, содержащего значение метрики. |

Необязательные атрибуты источника:

| Поле | Тип | Описание |
| --- | --- | --- |
| `attributePath` | String | См. [CompositeData](#compositedata) ниже. |
| `allowAdditionalKeys` | Boolean | Если true, допускаются дополнительные ключевые свойства, помимо указанных в `keyProperties`, но они игнорируются. Если false, `keyProperties` должны совпадать точно; дополнительные ключи в имени приведут к несоответствию. |
| `calculateDelta` | bool | Если true, вычисляет изменение значений данного атрибута. Значение = атрибут(t) - атрибут(t-1). Полезно для монотонно возрастающих значений. |
| `calculateRate` | bool | Если true, вычисляет скорость изменений в секунду. Используется в сочетании с `calculateDelta` для преобразования абсолютного атрибута (например, количество запросов) в скорость (например, запросы в секунду). Значение = атрибут / интервал опроса. |
| `aggregation` | String | Агрегирует несколько значений, если более одного MBean соответствует фильтру по домену и ключевым свойствам. Агрегация по умолчанию -- `SUM`. Доступные агрегации: `SUM`, `AVG`, `MIN`, `MAX`. Например, этот атрибут можно использовать для агрегирования всех `MemoryPools` и вычисления их значения `SUM` или `MAX`. |
| `splittings` | List | Задает [разделения](#splittings). |

### AttributePath (CompositeData)

Для извлечения значений отдельных ключей, возвращаемых атрибутом в типе `CompositeData`, необходимо использовать механизм `attributePath` и указать на интересующий вас ключ.

Например, `HeapMemoryUsage` является типом `CompositeData`, который возвращает следующий список пар ключ-значение:

```
{



committed: integer,



init: integer,



max: integer,



used: integer



}
```

Если вы хотите извлечь значение `used` из атрибута `HeapMemoryUsage`, направьте `attributePath` на ключ `used`.

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

### Разделения (Splittings)

Разделения могут использоваться для определения дополнительных измерений (dimensions) для метрики.

```
"splittings": [



{



"name": "dimension",



"keyProperty": "name"



}



]
```

Каждое разделение имеет следующие обязательные атрибуты:

| Поле | Тип | Описание |
| --- | --- | --- |
| `name` | String | Задает имя для данного измерения. |
| `keyProperty` | String | Определяет, какое ключевое свойство `ObjectName` MBean используется для разделения. См. атрибут `keyProperties` в разделе [Источник](#source). |

Следующий пример показывает, как определить метрику, предоставляющую несколько измерений в рамках одного определения метрики:

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

На основе этого определения метрики следующие MBean:

* `java.lang:type=MemoryPool,name=G1 Eden Space`
* `java.lang:type=MemoryPool,name=G1 Survivor Space`

создадут одну метрику в Dynatrace с двумя измерениями:

* `java.lang.MemoryPoolUsage` с измерением `memory_type=G1 Eden Space`
* `java.lang.MemoryPoolUsage` с измерением `memory_type=G1 Survivor Space`

## Мониторинг

Перейдите в [Data Explorer](../../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") для анализа и построения графиков ваших пользовательских JMX-метрик. При необходимости вы можете закрепить графики на панели мониторинга. В следующем примере вы можете увидеть метрику `java.lang.MemoryPoolUsage`, разделенную по измерению `memory_type`:

![Data Explorer с JMX-метриками z/OS](https://dt-cdn.net/images/data-explorer-1643-7696285fbf.png)

Чтобы получить список метрик, доступных в вашей среде мониторинга, перейдите в **Metrics**, чтобы открыть [браузер метрик](../../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."). В следующем примере вы можете увидеть три метрики, которые мы создали выше:

![Браузер метрик с JMX-метриками z/OS](https://dt-cdn.net/images/metrics-browser-1636-1096adef93.png)

## Связанные темы

* [Браузер метрик](../../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser.")
* [Data Explorer](../../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.")
