---
title: Источник данных JMX
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/jmx
scraped: 2026-05-12T12:07:20.698039
---

# Источник данных JMX

# Источник данных JMX

* Справочник
* Чтение: 2 мин
* Опубликовано 15 мая 2023 г.

Dynatrace предоставляет платформу для создания метрик из [JMX MBeans](https://en.wikipedia.org/wiki/Java_Management_Extensions). Каждый процесс, отслеживаемый модулем кода Java в OneAgent, может обрабатывать расширения JMX 2.0.

Необходимо включить функцию OneAgent **Java Metric Extensions (JMX)** [OneAgent feature](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управление функциями OneAgent глобально и для каждой группы процессов.")

## Общие сведения

[JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/package-summary.html) организует данные и функции объектно-ориентированным способом. Каждый процесс Java имеет [платформенный сервер MBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer), который управляет набором объектов мониторинга, называемых MBeans.

Каждый MBean имеет уникальное [имя объекта](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html). Каждое имя объекта состоит из доменного имени и списка ключевых свойств. Каждое ключевое свойство состоит из имени и значения (строкового типа).

JMX определяет стандартизированный синтаксис для записи имён объектов, например `java.lang:type=GarbageCollector,name=YoungGen`. Каждый MBean имеет 0 или более атрибутов (см. [MBeanServer::getAttribute](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/MBeanServer.html#getAttribute(javax.management.ObjectName,java.lang.String))). Атрибуты могут быть любого типа Java (включая булевы, числа и строки).

Числовые атрибуты можно напрямую использовать для создания метрик в Dynatrace. Также можно извлекать числовые значения из сложных атрибутов.

## Предварительные требования

Предполагается следующее:

* Наличие достаточной экспертизы по JMX для создания расширения.
* Знакомство с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать YAML-файл расширения с помощью платформы Extensions.").

## Поддерживаемые версии Dynatrace

* Dynatrace версии 1.265+
* OneAgent версии 1.265+

## YAML-файл расширения JMX

Рассмотрим минимальное расширение JMX:

```
# required extension metadata



name: custom:com.example.jmx



version: 1.0.0



minDynatraceVersion: 1.265.0



author:



name: John Doe



# optional metric metadata



metrics:



- key: com.example.jmx.thread_count



metadata:



displayName: Thread Count



description: Number of active Java threads



unit: Count



# defines how to create metrics from JMX MBeans



jmx:



groups:



- group: jvm



subgroups:



- subgroup: basic



query: java.lang:type=Threading



metrics:



- key: com.example.jmx.thread_count



type: gauge



value: attribute:ThreadCount
```

Первые два раздела уже должны быть знакомы; рассмотрим раздел `jmx` YAML-файла.

Группы и подгруппы позволяют совместно использовать конфигурацию для нескольких метрик. В данном примере используется одна группа и одна подгруппа.

## Извлечение метрик из MBeans

Каждая подгруппа должна выбрать набор MBeans, которые будут участвовать в метрике. Это выполняется с помощью поля `query` и соответствует стандартному [синтаксису имён объектов JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html)

Здесь запрос: `java.lang:type=Threading`. Это означает поиск бина в домене `java.lang` с единственным свойством с именем `type` и значением `Threading`.

Каждая подгруппа также должна определять хотя бы одну метрику для извлечения из выбранных MBeans. В примере создаётся метрика типа gauge в Dynatrace с именем `com.example.jmx.thread_count` путём запроса числового атрибута JMX `ThreadCount` из MBean `java.lang:type=Threading`.

OneAgent автоматически добавит к метрике следующие измерения:

* `dt.entity.process_group_instance`
* `dt.entity.process_group`
* `dt.entity.host`
* `dt.entity.container_group_instance`
* `dt.metrics.source`
* `dt.extension.config.id`

Дополнительные сведения см. в [справочнике по источнику данных JMX](/managed/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference "Узнайте о расширениях JMX в платформе Extensions.").