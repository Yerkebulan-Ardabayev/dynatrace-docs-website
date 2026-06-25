# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../data-sources/jmx.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources"

TRANS = {
    "* Reference": "* Справочник",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published May 15, 2023": "* Опубликовано 15 мая 2023 г.",
    "Dynatrace provides a framework to create metrics from [JMX MBeans](https://en.wikipedia.org/wiki/Java_Management_Extensions). Every process monitored by OneAgent Java code module is capable of processing JMX 2.0 extensions.": "Dynatrace предоставляет платформу для создания метрик из [JMX MBeans](https://en.wikipedia.org/wiki/Java_Management_Extensions). Каждый процесс, отслеживаемый модулем кода Java в OneAgent, может обрабатывать расширения JMX 2.0.",
    'You need to enable the **Java Metric Extensions (JMX)** [OneAgent feature](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")': 'Необходимо включить функцию OneAgent **Java Metric Extensions (JMX)** [OneAgent feature](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управление функциями OneAgent глобально и для каждой группы процессов.")',
    "## Background": "## Общие сведения",
    "[JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/package-summary.html) organizes data and functionality in an object oriented way. Every Java process has a [platform MBean server](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer) which manages a set of monitoring objects called MBeans.": "[JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/package-summary.html) организует данные и функции объектно-ориентированным способом. Каждый процесс Java имеет [платформенный сервер MBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer), который управляет набором объектов мониторинга, называемых MBeans.",
    "Every MBean has a unique [object name](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html). Every object name consists of a domain name and a list of key properties. Every key property consists of a name and a (string) value.": "Каждый MBean имеет уникальное [имя объекта](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html). Каждое имя объекта состоит из доменного имени и списка ключевых свойств. Каждое ключевое свойство состоит из имени и значения (строкового типа).",
    "JMX defines a standardized syntax to write those object names, for example, `java.lang:type=GarbageCollector,name=YoungGen`. Every MBean has 0 or more attributes (see [MBeanServer::getAttribute](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/MBeanServer.html#getAttribute(javax.management.ObjectName,java.lang.String))). Attributes can be of any Java type (including booleans, numbers and strings).": "JMX определяет стандартизированный синтаксис для записи имён объектов, например `java.lang:type=GarbageCollector,name=YoungGen`. Каждый MBean имеет 0 или более атрибутов (см. [MBeanServer::getAttribute](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/MBeanServer.html#getAttribute(javax.management.ObjectName,java.lang.String))). Атрибуты могут быть любого типа Java (включая булевы, числа и строки).",
    "Numeric attributes can be directly used to produce metrics in Dynatrace. It's also possible to extract numeric values from complex attributes.": "Числовые атрибуты можно напрямую использовать для создания метрик в Dynatrace. Также можно извлекать числовые значения из сложных атрибутов.",
    "## Prerequisites": "## Предварительные требования",
    "We assume the following:": "Предполагается следующее:",
    "* You possess sufficient JMX subject matter expertise to create an extension.": "* Наличие достаточной экспертизы по JMX для создания расширения.",
    '* You\'re familiar with [Extensions basic concepts](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").': '* Знакомство с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать YAML-файл расширения с помощью платформы Extensions.").',
    "## Supported Dynatrace versions": "## Поддерживаемые версии Dynatrace",
    "* Dynatrace version 1.265+": "* Dynatrace версии 1.265+",
    "* OneAgent version 1.265+": "* OneAgent версии 1.265+",
    "## JMX extension YAML file": "## YAML-файл расширения JMX",
    "Let's start with a minimal JMX extension:": "Рассмотрим минимальное расширение JMX:",
    "The first two parts should already be familiar to you, we will focus on the `jmx` section of the YAML file.": "Первые два раздела уже должны быть знакомы; рассмотрим раздел `jmx` YAML-файла.",
    "Groups and subgroups can be used to share configuration between multiple metrics. In our specific sample, we only have one group and one subgroup.": "Группы и подгруппы позволяют совместно использовать конфигурацию для нескольких метрик. В данном примере используется одна группа и одна подгруппа.",
    "## Extract metrics from MBeans": "## Извлечение метрик из MBeans",
    "Every subgroup has to select a set of MBeans that should contribute to a metric. This is done with the `query` field and follows the standard [JMX object name syntax](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html)": "Каждая подгруппа должна выбрать набор MBeans, которые будут участвовать в метрике. Это выполняется с помощью поля `query` и соответствует стандартному [синтаксису имён объектов JMX](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html)",
    "Here, the query is `java.lang:type=Threading`. This breaks down into looking for a bean in domain `java.lang` that has exactly one property with name `type` and value `Threading`.": "Здесь запрос: `java.lang:type=Threading`. Это означает поиск бина в домене `java.lang` с единственным свойством с именем `type` и значением `Threading`.",
    "Every subgroup also needs to define at least one metric that should be extracted from the selected MBeans. In our sample we create a Dynatrace gauge metric called `com.example.jmx.thread_count` by querying the numeric JMX attribute `ThreadCount` from the MBean `java.lang:type=Threading`.": "Каждая подгруппа также должна определять хотя бы одну метрику для извлечения из выбранных MBeans. В примере создаётся метрика типа gauge в Dynatrace с именем `com.example.jmx.thread_count` путём запроса числового атрибута JMX `ThreadCount` из MBean `java.lang:type=Threading`.",
    "OneAgent will automatically add the following dimensions to your metric:": "OneAgent автоматически добавит к метрике следующие измерения:",
    "* `dt.entity.process_group_instance`": "* `dt.entity.process_group_instance`",
    "* `dt.entity.process_group`": "* `dt.entity.process_group`",
    "* `dt.entity.host`": "* `dt.entity.host`",
    "* `dt.entity.container_group_instance`": "* `dt.entity.container_group_instance`",
    "* `dt.metrics.source`": "* `dt.metrics.source`",
    "* `dt.extension.config.id`": "* `dt.extension.config.id`",
    'For more information, see [JMX data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference "Learn about JMX extensions in the Extensions framework.").': 'Дополнительные сведения см. в [справочнике по источнику данных JMX](/managed/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference "Узнайте о расширениях JMX в платформе Extensions.").',
}

PASS = {
    "title: JMX data source",
    "# JMX data source",
}

if __name__ == "__main__":
    build_one(REL, "jmx.md", TRANS, PASS)
    qa_one(REL, "jmx.md")
