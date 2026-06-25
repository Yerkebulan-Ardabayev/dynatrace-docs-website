# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/advanced-configuration/dedicated-performance-profile.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/advanced-configuration"

TRANS = {
    "title: Dedicated performance profile configuration": "title: Настройка выделенного профиля производительности",
    "# Dedicated performance profile configuration": "# Настройка выделенного профиля производительности",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Updated on Apr 28, 2026": "* Обновлено 28 апреля 2026 г.",
    "The dedicated performance profile offers powerful performance optimization for your Dynatrace environment. With the dedicated profile, you can enhance the computing capabilities of your ActiveGate host to improve monitoring and analysis capabilities.": "Выделенный профиль производительности обеспечивает мощную оптимизацию производительности для окружения Dynatrace. С его помощью можно расширить вычислительные возможности хоста ActiveGate для улучшения возможностей мониторинга и анализа.",
    "## Limitations": "## Ограничения",
    "* The dedicated performance profile should be used on powerful instances, such as `C6i.2xlarge` (AWS), `Standard_F8s_v2` (Azure), or `c2-standard-8` (GCP).": "* Выделенный профиль производительности следует использовать на мощных инстансах, например `C6i.2xlarge` (AWS), `Standard_F8s_v2` (Azure) или `c2-standard-8` (GCP).",
    "* When using the dedicated performance profile, no other ActiveGate functionality should be running simultaneously with extensions.": "* При использовании выделенного профиля производительности никакая другая функциональность ActiveGate не должна работать одновременно с расширениями.",
    "* If you use ActiveGate groups, ensure that all ActiveGates within the group have the same custom configuration applied for the chosen performance profile.": "* При использовании групп ActiveGate убедитесь, что ко всем ActiveGate в группе применена одинаковая пользовательская конфигурация для выбранного профиля производительности.",
    "## Configuration": "## Конфигурация",
    "To configure the ActiveGate for the dedicated performance profile": "Настройка ActiveGate для выделенного профиля производительности",
    "1. Restrict ActiveGate functionality to Extensions only.": "1. Ограничьте функциональность ActiveGate только расширениями.",
    "agctl": "agctl",
    "custom.properties": "custom.properties",
    "ActiveGate version 1.333+": "ActiveGate версии 1.333+",
    'Use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Learn how to use agctl to configure and manage ActiveGate from the command line") to disable modules:': 'Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для отключения модулей:',
    "Modify the `custom.properties` file:": "Измените файл `custom.properties`:",
    "2. Modify ActiveGate memory settings via the `launcheruserconfig.conf` file.": "2. Измените настройки памяти ActiveGate через файл `launcheruserconfig.conf`.",
    '3. [Restart the ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to apply the configuration changes.': '3. [Перезапустите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.") для применения изменений конфигурации.',
    '4. [Set the performance profile of the ActiveGate](/managed/ingest-from/extensions/concepts#performance-profile "Learn more about the concept of Dynatrace Extensions.") to `Dedicated limits`.': '4. [Задайте профиль производительности ActiveGate](/managed/ingest-from/extensions/concepts#performance-profile "Подробнее о концепции Dynatrace Extensions.") как `Dedicated limits`.',
    "## Related topics": "## Связанные темы",
    '* [About Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.")': '* [О расширениях](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "dedicated-performance-profile.md", TRANS, PASS)
    qa_one(REL, "dedicated-performance-profile.md")
