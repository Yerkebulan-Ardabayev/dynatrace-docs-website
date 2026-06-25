# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../data-sources/jmx/jmx-schema-reference.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/jmx"

TRANS = {
    "* Reference": "* Справочник",
    "* 4-min read": "* Чтение: 4 мин",
    "* Updated on Sep 15, 2025": "* Обновлено 15 сентября 2025 г.",
    "This is a general description of JMX data source-based extension YAML file and ways to declare metrics and dimensions you would like to collect using your extension.": "Это общее описание YAML-файла расширения на основе источника данных JMX, а также способов объявления метрик и измерений для сбора в расширении.",
    "## Metric values": "## Значения метрик",
    "The metric value can come from different sources.": "Значение метрики может поступать из разных источников.",
    "The most common source is a numeric JMX MBean attribute:": "Наиболее распространённый источник: числовой атрибут JMX MBean:",
    "This will look for an attribute named `ThreadCount`. The returned value must be either numeric (any subclass of `java.lang.Number`, such as `Integer`, `Long`, `Double`) or a `boolean` (converted to `0` for `false` and `1` for `true`).": "Выполняется поиск атрибута с именем `ThreadCount`. Возвращаемое значение должно быть числовым (любой подкласс `java.lang.Number`, например `Integer`, `Long`, `Double`) или булевым типом `boolean` (преобразуется в `0` для `false` и `1` для `true`).",
    "JMX allows defining attributes with complex-non numeric types. It is possible to extract a numeric value from such a non-numeric attribute value. This requires specifying which methods or fields should be accessed.": "JMX позволяет определять атрибуты со сложными нечисловыми типами. Из такого нечислового значения атрибута можно извлечь числовое значение, указав, к каким методам или полям следует обращаться.",
    "For example:": "Например:",
    "See [accessor syntax](#accessor-syntax) below for a detailed syntax description.": "Подробное описание синтаксиса см. в разделе [синтаксис аксессора](#accessor-syntax) ниже.",
    "A special case is to always use the same constant value instead of querying an attribute:": "Особый случай: всегда использовать одно и то же константное значение вместо запроса атрибута.",
    "If the `query` matches a single MBean, this metric will always produce the value `1`. This can be used to report just the presence of a specific MBean. If the query matches multiple MBeans, this metric will produce a value corresponding to the number of matches MBeans.": "Если `query` совпадает с одним MBean, метрика всегда возвращает значение `1`. Это позволяет фиксировать само наличие конкретного MBean. Если запрос совпадает с несколькими MBeans, метрика вернёт значение, соответствующее количеству совпавших MBeans.",
    "## Custom dimensions": "## Пользовательские измерения",
    "Every custom dimension consists of a constant `key` and a `value`. The value can come from different sources.": "Каждое пользовательское измерение состоит из константного `key` и `value`. Значение может поступать из разных источников.",
    "The simplest case is to set the dimension value to a constant string:": "Простейший случай: задать значение измерения в виде константной строки.",
    "This will produce a metric where dimension `k1` always has value `constant_value`.": "В результате создаётся метрика, в которой измерение `k1` всегда имеет значение `constant_value`.",
    "MBean object name key property value can be used as a dimension value:": "В качестве значения измерения можно использовать значение ключевого свойства имени объекта MBean:",
    "This will produce a metric where dimension `k1` corresponds to the value of the key property `name`. For example, the MBean `java.lang:type=GarbageCollector,name=YoungGen`, will produce a metric where dimension `k1` has the value `YoungGen`.": "В результате создаётся метрика, в которой измерение `k1` соответствует значению ключевого свойства `name`. Например, MBean `java.lang:type=GarbageCollector,name=YoungGen` создаст метрику, где измерение `k1` имеет значение `YoungGen`.",
    "If a process has 3 different garbage collectors, metrics with 3 different dimension values are produced and can be charted independently.": "Если у процесса есть 3 разных сборщика мусора, создаются метрики с 3 разными значениями измерений, которые можно отображать на графике независимо.",
    "An MBean attribute can also be used as a dimension value.": "Атрибут MBean также можно использовать в качестве значения измерения.",
    "This will produce a metric where dimension `k1` corresponds to the value of attribute `Name`. Currently, only immutable attributes are supported. The attribute for a specific MBean is only queried once when an MBean is first discovered by OneAgent.": "В результате создаётся метрика, в которой измерение `k1` соответствует значению атрибута `Name`. В настоящее время поддерживаются только неизменяемые атрибуты. Атрибут конкретного MBean запрашивается только один раз при первом обнаружении MBean агентом OneAgent.",
    "Similar to metric values, it is possible to extract the dimension value from a complex attribute using an accessor expression:": "Аналогично значениям метрик, значение измерения можно извлечь из сложного атрибута с помощью выражения аксессора:",
    "This will look for an attribute called `SomeAttribute`, call `getName` on it and use the returned value as the value for dimension `k1`.": "Выполняется поиск атрибута `SomeAttribute`, вызов `getName` на нём, а возвращаемое значение используется как значение измерения `k1`.",
    "## Accessor syntax": "## Синтаксис аксессора",
    "| Accessor | Description |": "| Аксессор | Описание |",
    "| --- | --- |": "| --- | --- |",
    "| `getSomeNumericValue()` | Call a method called `getSomeNumericValue` with no parameters. |": "| `getSomeNumericValue()` | Вызов метода `getSomeNumericValue` без параметров. |",
    "| `getSomeNumericValue` | Parenthesis are optional methods without parameters. |": "| `getSomeNumericValue` | Скобки не обязательны для методов без параметров. |",
    "| `getA().getB()` | Call a method called `getA`, then on the return value of this call a method called `getB`. |": "| `getA().getB()` | Вызов метода `getA`, затем вызов метода `getB` на возвращаемом значении. |",
    "| `getA(1)` | Call a method called `getA` with integer argument `1`. |": "| `getA(1)` | Вызов метода `getA` с целочисленным аргументом `1`. |",
    '| `getA("x")` | Call a method called `getA` with string argument `x`. |': '| `getA("x")` | Вызов метода `getA` со строковым аргументом `x`. |',
    '| `getA(1, "x")` | Call a method called `getA` with two arguments. |': '| `getA(1, "x")` | Вызов метода `getA` с двумя аргументами. |',
    "| `getA()[1]` | Call a method called `getA`, then from the return value extract value at index 1. |": "| `getA()[1]` | Вызов метода `getA`, затем извлечение значения с индексом 1 из возвращаемого значения. |",
    "## Extension variables": "## Переменные расширения",
    "### Use extension variables to filter MBeans": "### Использование переменных расширения для фильтрации MBeans",
    "Extension variables can be used to allow users of an extension to monitor only specific MBeans:": "Переменные расширения позволяют пользователям расширения отслеживать только конкретные MBeans:",
    "This creates a variable called `gc_name_filter` internally and `Garbage Collector Name` in the UI. The variable value will be used to pick a specific MBean. E.g. if the variable value is `YoungGen` then the complete object name query will be `java.lang:type=GarbageCollector,name=YoungGen`": "При этом создаётся переменная с внутренним именем `gc_name_filter` и отображаемым именем `Garbage Collector Name` в интерфейсе. Значение переменной используется для выбора конкретного MBean. Например, если значение переменной равно `YoungGen`, полный запрос имени объекта будет `java.lang:type=GarbageCollector,name=YoungGen`",
    "Every monitoring configuration can pick a specific value for this variable. To ensure that multiple monitoring configurations with different variable values are not mixed up in the UI, it is recommended to also add a dimension for the `name` property as demonstrated above.": "Каждая конфигурация мониторинга может выбрать конкретное значение для этой переменной. Чтобы несколько конфигураций мониторинга с разными значениями переменных не смешивались в интерфейсе, рекомендуется также добавить измерение для свойства `name`, как показано выше.",
    "### Use extension variables as dimension": "### Использование переменных расширения в качестве измерения",
    "Extension variables can also be used directly as the value of custom metric dimensions.": "Переменные расширения также можно использовать непосредственно в качестве значения пользовательских измерений метрик.",
    'This references a variable `my_variable` and adds an additional dimension to the metric. The variable value will be used as content for the dimension. For example, if the value is `My Value`, the dimension added would be `my_dimension="My Value"`.': 'Здесь используется переменная `my_variable`, которая добавляет дополнительное измерение к метрике. Значение переменной используется как содержимое измерения. Например, если значение равно `My Value`, добавляемое измерение будет `my_dimension="My Value"`.',
    "## Gauge value aggregation": "## Агрегирование значений gauge",
    "In the example above, we retrieve the number of threads from a single MBean. But in some cases, a JMX query might return several matching beans. Collecting the results will provide us with too much information. Instead, it's more helpful to calculate the minimum, maximum, or average values to understand the range.": "В приведённом выше примере количество потоков извлекается из одного MBean. Однако в некоторых случаях JMX-запрос может вернуть несколько совпадающих бинов. Сбор всех результатов даёт избыточный объём информации. Более полезно вычислять минимальное, максимальное или среднее значения для понимания диапазона.",
    "For that exact purpose, we provide `gauge_statcounter`, which works as a drop-in replacement for `gauge`. Unlike the regular `gauge`, which sums up the value, the `gauge_statcounter` includes distinct values such as:": "Для этой цели предусмотрен тип `gauge_statcounter`, который является прямой заменой `gauge`. В отличие от обычного `gauge`, суммирующего значения, `gauge_statcounter` включает отдельные значения:",
    "* `min`: the minimum value of the metric": "* `min`: минимальное значение метрики",
    "* `max`: the maximum value of the metric": "* `max`: максимальное значение метрики",
    "* `sum`: the sum of metric scraping": "* `sum`: сумма значений при сборе метрики",
    "* `count`: the number of scrape passes": "* `count`: количество проходов сбора",
    "Notice that average can be easily understood by dividing the sum by count.": "Среднее значение вычисляется простым делением суммы на количество.",
}

PASS = {
    "title: JMX data source reference",
    "# JMX data source reference",
}

if __name__ == "__main__":
    build_one(REL, "jmx-schema-reference.md", TRANS, PASS)
    qa_one(REL, "jmx-schema-reference.md")
