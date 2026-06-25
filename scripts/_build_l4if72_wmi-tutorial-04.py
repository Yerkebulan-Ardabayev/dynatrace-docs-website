# -*- coding: utf-8 -*-
"""L4-IF.72 -- wmi-tutorial-04.md  (custom topology)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial"

TRANS = {
    # H1 (duplicated)
    "# WMI tutorial - custom topology": "# WMI tutorial - пользовательская топология",
    # meta
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Mar 30, 2022": "* Опубликовано 30 марта 2022 г.",
    # intro
    "Having a well-defined topology model helps make sense of all the metrics and data ingested in Dynatrace.": "Чётко определённая модель топологии помогает упорядочить все метрики и данные, поступающие в Dynatrace.",
    "For an Extensions extension, this all happens in the `topology` section, which is split into two parts:": "Для расширения Extensions вся настройка выполняется в разделе `topology`, который делится на две части:",
    "* `types` - defines which new entity types the extension monitors": "* `types`: определяет новые типы сущностей, которые отслеживает расширение",
    "* `relationships` - defines if and how these entity types relate to each other": "* `relationships`: определяет наличие и характер связей между этими типами сущностей",
    # Key aspects - types
    "## Key aspects when defining types": "## Ключевые аспекты при определении типов",
    "* `idPattern` - Must be unique enough to represent each device instance without duplicating it": "* `idPattern`: должен быть достаточно уникальным, чтобы идентифицировать каждый экземпляр устройства без дублирования",
    "* `sources` - Must define rules for all metrics of the extension that should be split by this entity": "* `sources`: должен определять правила для всех метрик расширения, которые разбиваются по данной сущности",
    "* `condition` - Can make use of functions like `$prefix(...)` to define patterns for metric keys": "* `condition`: поддерживает функции, например `$prefix(...)`, для определения шаблонов ключей метрик",
    "* `attributes` - Are optional details that can be extracted from the dimensions of metrics": "* `attributes`: необязательные сведения, извлекаемые из измерений метрик",
    # Key aspects - relationships
    "## Key aspects when defining relationships": "## Ключевые аспекты при определении связей",
    "* `sources` - Any metric that matches the pattern will be evaluated for a relationship. This means": "* `sources`: любая метрика, соответствующая шаблону, будет проверяться на наличие связи. Это означает,",
    "it should belong to both entity types part of the relationship": "что метрика должна принадлежать обоим типам сущностей, участвующим в связи.",
    # Find entities
    "## Find your new entities in UI": "## Поиск новых сущностей в интерфейсе",
    "Navigate to `../ui/entity/list/{entity-type}` on your Dynatrace environment. For example:": "Откройте `../ui/entity/list/{entity-type}` в вашей среде Dynatrace. Например:",
    "* `../ui/entity/list/wmi:generic_host`": "* `../ui/entity/list/wmi:generic_host`",
    "* `../ui/entity/list/wmi:generic_network_device`": "* `../ui/entity/list/wmi:generic_network_device`",
    # Tasks
    "## Tasks": "## Задачи",
    "1. Add the `topology` section to your `extension.yaml` using the template below.": "1. Добавьте раздел `topology` в файл `extension.yaml` по приведённому шаблону.",
    "2. Define two entity types for a Generic Host and a Generic Network Device.": "2. Определите два типа сущностей: Generic Host и Generic Network Device.",
    "3. Ensure that network devices are aware of the type (`Adapter` or `Interface`).": "3. Убедитесь, что сетевые устройства содержат информацию о типе (`Adapter` или `Interface`).",
    "4. Create a relationship between the two where a Generic Network Device runs on a Generic Host.": "4. Создайте связь между ними: Generic Network Device работает на Generic Host.",
    "5. Package and upload a new version of your extension.": "5. Соберите и загрузите новую версию пакета расширения.",
    "6. Validate the new entities are created.": "6. Проверьте, что новые сущности созданы.",
    'For more information on extending the Dynatrace topology, see [Custom topology model](/managed/ingest-from/extend-dynatrace/extend-topology "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to.")': 'Дополнительные сведения о расширении топологии Dynatrace см. в разделе [Пользовательская модель топологии](/managed/ingest-from/extend-dynatrace/extend-topology "Обеспечьте контекстную насыщенность всех входящих наблюдений и их анализ в контексте связанных сущностей.")',
    # Results
    "## Results": "## Результаты",
    "You should see new entities created for your generic host and generic network device entity types:": "Должны появиться новые сущности типов Generic Host и Generic Network Device:",
    "![hosts](https://dt-cdn.net/images/wmi-tutorial-topology-host-865-f2a80aa24a.png)": "![hosts](https://dt-cdn.net/images/wmi-tutorial-topology-host-865-f2a80aa24a.png)",
    "hosts": "hosts",
    "![network_devices](https://dt-cdn.net/images/wmi-tutorial-topology-nic-945-00a3fef761.png)": "![network_devices](https://dt-cdn.net/images/wmi-tutorial-topology-nic-945-00a3fef761.png)",
    r"network\_devices": r"network\_devices",
    '**Next step**: [Unified analysis page](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-05 "Learn about WMI extensions in the Extensions framework.")': '**Следующий шаг**: [Страница унифицированного анализа](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-05 "Узнайте о расширениях WMI в платформе Extensions framework.")',
}

PASS = {
    "title: WMI tutorial - custom topology",
}

if __name__ == "__main__":
    build_one(REL, "wmi-tutorial-04.md", TRANS, PASS)
    qa_one(REL, "wmi-tutorial-04.md")
