---
title: JMX data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx
scraped: 2026-03-06T21:36:35.777912
---

# Источник данных JMX

# Источник данных JMX

* Latest Dynatrace
* Reference
* 2-min read
* Published May 15, 2023

Dynatrace предоставляет фреймворк для создания метрик из [JMX MBeans](https://en.wikipedia.org/wiki/Java_Management_Extensions). Каждый процесс, отслеживаемый модулем кода Java для OneAgent, способен обрабатывать расширения JMX 2.0.

Необходимо включить [функцию OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Java Metric Extensions (JMX)**.

## Общие сведения

[JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/package-summary.html) организует данные и функциональность объектно-ориентированным образом. Каждый процесс Java содержит [сервер platform MBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer), управляющий набором объектов мониторинга — MBean.

Каждый MBean имеет уникальное [имя объекта](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html). Каждое имя объекта состоит из имени домена и списка ключевых свойств. Каждое ключевое свойство включает имя и значение (строку).

JMX определяет стандартизированный синтаксис для записи имён объектов, например `java.lang:type=GarbageCollector,name=YoungGen`. Каждый MBean имеет 0 или более атрибутов (см. [MBeanServer::getAttribute](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/MBeanServer.html#getAttribute(javax.management.ObjectName,java.lang.String))). Атрибуты могут быть любого типа Java (включая булевы значения, числа и строки).

Числовые атрибуты можно напрямую использовать для создания метрик в Dynatrace. Также возможно извлекать числовые значения из сложных атрибутов.

## Предварительные требования

Предполагается следующее:

* Вы обладаете достаточными знаниями в области JMX для создания расширения.
* Вы знакомы с [базовыми концепциями расширений](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

## Поддерживаемые версии Dynatrace

* Dynatrace версии 1.265+
* OneAgent версии 1.265+

## YAML-файл расширения JMX

Начнём с минимального расширения JMX:

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

Первые две части должны быть вам уже знакомы; сосредоточимся на разделе `jmx` YAML-файла.

Группы и подгруппы можно использовать для совместного использования конфигурации между несколькими метриками. В данном примере у нас только одна группа и одна подгруппа.

## Извлечение метрик из MBean

Каждая подгруппа должна выбирать набор MBean, которые должны участвовать в формировании метрики. Это делается с помощью поля `query` и следует стандартному [синтаксису имени объекта JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html).

Здесь запрос — `java.lang:type=Threading`. Это означает поиск бина в домене `java.lang`, у которого есть ровно одно свойство с именем `type` и значением `Threading`.

Каждая подгруппа также должна определять хотя бы одну метрику, которую необходимо извлечь из выбранных MBean. В нашем примере мы создаём метрику типа gauge в Dynatrace с именем `com.example.jmx.thread_count`, запрашивая числовой атрибут JMX `ThreadCount` из MBean `java.lang:type=Threading`.

OneAgent автоматически добавляет следующие измерения к вашей метрике:

* `dt.entity.process_group_instance`
* `dt.entity.process_group`
* `dt.entity.host`
* `dt.entity.container_group_instance`
* `dt.metrics.source`
* `dt.extension.config.id`

Дополнительные сведения см. в [справочнике по источнику данных JMX](/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference "Learn about JMX extensions in the Extensions framework.").
