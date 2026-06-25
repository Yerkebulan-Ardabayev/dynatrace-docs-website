# -*- coding: utf-8 -*-
"""L4-IF.72 -- wmi-tutorial-05.md  (unified analysis)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial"

TRANS = {
    # H1 (duplicated)
    "# WMI tutorial - unified analysis": "# WMI tutorial - унифицированный анализ",
    # meta
    "* How-to guide": "* Практическое руководство",
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Mar 30, 2022": "* Опубликовано 30 марта 2022 г.",
    # intro
    "Unified analysis pages are windows into performance analysis and troubleshooting for this newly monitored technology.": "Страницы унифицированного анализа предоставляют возможности анализа производительности и устранения неполадок для новой отслеживаемой технологии.",
    "They offer the possibility to eliminate further dashboarding or ad-hoc chart building. The `screens` section will define the details to be displayed on each entity's page as well as charts and lists of other related entities for quick drilldowns.": "Они позволяют отказаться от создания отдельных дашбордов и разовых графиков. Раздел `screens` определяет содержимое страницы каждой сущности: графики и списки связанных сущностей для быстрого перехода к деталям.",
    # Detailed page section
    "## Unified analysis detailed page": "## Страница детального анализа",
    "The details page is organized into `staticContent` and a `layout` for dynamic content that comprises `cards` (charts and lists).": "Страница сведений состоит из раздела `staticContent` и макета `layout` для динамического содержимого, включающего карточки `cards` (графики и списки).",
    "`staticContent`": "`staticContent`",
    "* `showProblems` - Show a panel for any Problems about this entity": "* `showProblems`: показывает панель проблем данной сущности",
    "* `showProperties` - Show the **Properties and tags** section": "* `showProperties`: показывает раздел **Properties and tags**",
    "* `showTags` - Show the tags applied to this entity": "* `showTags`: показывает теги, применённые к данной сущности",
    "* `showGlobalFilter` - Show the global filtering bar": "* `showGlobalFilter`: показывает глобальную панель фильтрации",
    "* `showAddTag` - Show the **Add tag** button": "* `showAddTag`: показывает кнопку **Add tag**",
    "The `layout` consists of different cards defined in the `chartsCards` and `entitiesListCards` subsections.": "Макет `layout` состоит из карточек, определяемых в подразделах `chartsCards` и `entitiesListCards`.",
    # Charts card section
    "## Charts card": "## Карточка графиков",
    "A chart card is a section of the screen that displays charts. All possible charts are defined in the card, and a number of them can be displayed at the same time on the screen. The others are available from the dropdown list above the chart.": "Карточка графиков: раздел экрана, отображающий графики. В карточке определяются все возможные графики; часть из них отображается одновременно, остальные доступны в раскрывающемся списке над графиком.",
    'Charts cards rely on [metric selectors](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") to correctly display metrics.': 'Карточки графиков используют [селекторы метрик](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройте селектор метрик для API метрик v2.") для корректного отображения метрик.',
    "Simple chart card example:": "Простой пример карточки графиков:",
    # Entity list section
    "## Entity list": "## Список сущностей",
    "An entity list is a list of entities that are somehow related to the currently viewed entity. Additional metrics can be charted in the details of each returned entity and will show as a single value in the list view.": "Список сущностей содержит объекты, связанные с текущей сущностью. Для каждой возвращаемой сущности можно строить дополнительные графики, которые отображаются как единое значение в представлении списка.",
    'Entity lists rely on [entity selectors](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") to correctly list related entities.': 'Списки сущностей используют [селекторы сущностей](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте селектор сущностей для эндпоинтов Environment API.") для корректного отображения связанных объектов.',
    "Simple entity list example:": "Простой пример списка сущностей:",
    "`$(entityConditions)` is a function that automatically maps to the currently viewed entity. This is mandatory for entity selectors used in the extension.": "`$(entityConditions)`: функция, которая автоматически сопоставляется с текущей сущностью. Её использование обязательно для селекторов сущностей в расширении.",
    # Properties card section
    "## The properties card": "## Карточка свойств",
    "The `propertiesCard` of an entity can also be modified to include additional properties or hide unnecessary ones. Properties are extracted from entity attributes (when type is `ATTRIBUTE`) or through an entity selector (when type is `RELATION`).": "Карточку свойств `propertiesCard` сущности можно изменить: добавить дополнительные свойства или скрыть ненужные. Свойства извлекаются из атрибутов сущности (если тип `ATTRIBUTE`) или через селектор сущности (если тип `RELATION`).",
    # Define section
    "## Define unified pages for your extension": "## Определение страниц унифицированного анализа для расширения",
    "1. Add the `screens` section to your `extension.yaml` using the template below.": "1. Добавьте раздел `screens` в файл `extension.yaml` по приведённому шаблону.",
    "2. Customize the details page settings for both the Generic Host and the Generic Network Device entity types.": "2. Настройте параметры страницы сведений для типов сущностей Generic Host и Generic Network Device.",
    "3. Use charts cards to display all the metrics of each entity.": "3. Используйте карточки графиков для отображения всех метрик каждой сущности.",
    "4. Add entity list cards so that a Generic Host can list out all Network Adapters and Interfaces running on it.": "4. Добавьте карточки списков сущностей, чтобы Generic Host отображал все работающие на нём сетевые адаптеры и интерфейсы.",
    "5. Add a relation based property so that a Generic Network Device displays what Generic Host it runs on.": "5. Добавьте свойство на основе связи, чтобы Generic Network Device отображал хост, на котором работает.",
    "6. Package and upload a new version of your extension.": "6. Соберите и загрузите новую версию пакета расширения.",
    "7. Validate your screens are showing up as expected.": "7. Проверьте, что страницы отображаются корректно.",
    # Results
    "## Results": "## Результаты",
    "Your customized unified analysis pages are displayed and populated as expected.": "Настроенные страницы унифицированного анализа отображаются и заполняются данными в соответствии с ожиданиями.",
    "![result](https://dt-cdn.net/images/wmi-tutorial-ua-details-1626-532b22a38b.png)": "![result](https://dt-cdn.net/images/wmi-tutorial-ua-details-1626-532b22a38b.png)",
    "result": "result",
}

PASS = {
    "title: WMI tutorial - unified analysis",
}

if __name__ == "__main__":
    build_one(REL, "wmi-tutorial-05.md", TRANS, PASS)
    qa_one(REL, "wmi-tutorial-05.md")
