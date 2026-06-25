# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/advanced-configuration/eec-custom-configuration.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/advanced-configuration"

TRANS = {
    "title: Extension Execution Controller custom configuration": "title: Пользовательская конфигурация Extension Execution Controller",
    "# Extension Execution Controller custom configuration": "# Пользовательская конфигурация Extension Execution Controller",
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Updated on Sep 22, 2025": "* Обновлено 22 сентября 2025 г.",
    "The Extension Execution Controller (EEC) can be used standalone, out of the box. This topic explains how to modify your EEC.": "Extension Execution Controller (EEC) можно использовать в автономном режиме без дополнительной настройки. В этом разделе описана процедура изменения конфигурации EEC.",
    "## Modify the EEC configuration": "## Изменение конфигурации EEC",
    "To modify the EEC configuration, edit the `extensionsuser.conf` file, which is located at:": "Для изменения конфигурации EEC отредактируйте файл `extensionsuser.conf`, расположенный по следующим путям:",
    "* Using ActiveGate (for installation in the default location):": "* При использовании ActiveGate (установка по умолчанию):",
    "+ Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\extensionsuser.conf`": "+ Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\extensionsuser.conf`",
    "+ Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`": "+ Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`",
    "* Using OneAgent:": "* При использовании OneAgent:",
    "+ Windows: `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config\\extensionsuser.conf`": "+ Windows: `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config\\extensionsuser.conf`",
    "+ Linux: `/var/lib/dynatrace/oneagent/agent/config/extensionsuser.conf`": "+ Linux: `/var/lib/dynatrace/oneagent/agent/config/extensionsuser.conf`",
    "## Restart the EEC service": "## Перезапуск службы EEC",
    "After modifying the `extensionsuser.conf`, you need to restart the EEC service:": "После изменения файла `extensionsuser.conf` требуется перезапустить службу EEC:",
    "Linux": "Linux",
    "Windows": "Windows",
    "To restart the EEC service on a Linux system, run the following commands:": "Для перезапуска службы EEC в системе Linux выполните следующие команды:",
    "* For systems with SystemV:": "* Для систем с SystemV:",
    "* For systems with systemd:": "* Для систем с systemd:",
    "To restart the EEC service on a Windows system, either start **Task Manager** and restart the `Dynatrace Extensions Controller` service or run the following commands:": "Для перезапуска службы EEC в системе Windows запустите **Диспетчер задач** и перезапустите службу `Dynatrace Extensions Controller` либо выполните следующие команды:",
    "## Change port used to communicate with ActiveGate": "## Изменение порта для связи с ActiveGate",
    "By default, the EEC sends data via port 9999, which is used by ActiveGate.": "По умолчанию EEC отправляет данные через порт 9999, используемый ActiveGate.",
    "If you modify the port using the ActiveGate `custom.properties` file, you also have to modify the port that's used by the EEC. To do so, edit the `extensionsuser.conf` file to replace `PORT` with the target port and then restart the EEC service.": "При изменении порта в файле `custom.properties` ActiveGate необходимо также изменить порт, используемый EEC. Для этого отредактируйте файл `extensionsuser.conf`, заменив `PORT` на целевой порт, и перезапустите службу EEC.",
    "The port needs to be configured for the ActiveGate plugin module and the EEC.": "Порт необходимо настроить как для модуля плагинов ActiveGate, так и для EEC.",
    "## Change EEC port used to communicate with the extension": "## Изменение порта EEC для связи с расширением",
    "This port is used for communication between the EEC and existing extension (data source) processes.": "Этот порт используется для связи между EEC и существующими процессами расширения (источника данных).",
    "To add it, edit the `extensionsuser.conf` file and insert": "Для добавления отредактируйте файл `extensionsuser.conf` и вставьте следующее:",
    "## Enable/disable custom code extensions for data sources": "## Включение/отключение расширений с пользовательским кодом для источников данных",
    "Extensions leveraging sensitive data sources can significantly enhance the functionality and flexibility of your custom monitoring. However, they can also introduce potential vulnerabilities. Disabling custom extensions for these sensitive data sources can significantly reduce the risk of unauthorized access or data leakage.": "Расширения, работающие с конфиденциальными источниками данных, могут значительно расширить функциональность и гибкость пользовательского мониторинга. Однако они также могут создавать потенциальные уязвимости. Отключение пользовательских расширений для таких источников данных существенно снижает риск несанкционированного доступа или утечки данных.",
    "To enable or disable custom code extensions for a data source": "Включение или отключение расширений с пользовательским кодом для источника данных",
    "1. [Modify the EEC configuration](#modify-eec) to replace `<DSID>` with the data source ID for which you want to enable or disable custom code extensions.": "1. [Измените конфигурацию EEC](#modify-eec), заменив `<DSID>` на идентификатор источника данных, для которого требуется включить или отключить расширения с пользовательским кодом.",
    "2. [Restart the EEC service](#restart-eec).": "2. [Перезапустите службу EEC](#restart-eec).",
    "## Elevate privileges for local extensions on Windows": "## Повышение привилегий для локальных расширений в Windows",
    "By default, all local extensions on Windows (except WMI ones running on OneAgent) are executed with a LOCAL SERVICE account, which has lower privileges than the LOCAL SYSTEM account that is the default one for OneAgent and EEC.": "По умолчанию все локальные расширения в Windows (кроме WMI-расширений, работающих на OneAgent) выполняются с учётной записью LOCAL SERVICE, которая имеет меньше привилегий, чем учётная запись LOCAL SYSTEM, используемая по умолчанию для OneAgent и EEC.",
    "In case an extension requires elevated privileges, you can configure it to run as LOCAL SYSTEM manually.": "Если расширению требуются повышенные привилегии, его можно вручную настроить для запуска с учётной записью LOCAL SYSTEM.",
    "Open the `extensionsuser.conf` file and add the `elevated_privileges_extensions` parameter as follows:": "Откройте файл `extensionsuser.conf` и добавьте параметр `elevated_privileges_extensions` следующим образом:",
    "The `extensionVersion` can either be a specific version in the format `<major>.<minor>.<patch>`, for example `1.0.1`, or a wildcard character `*` that can be used to specify that all versions of a particular extension will have elevated privileges.": "Параметр `extensionVersion` может быть конкретной версией в формате `<major>.<minor>.<patch>`, например `1.0.1`, или символом подстановки `*`, указывающим, что все версии данного расширения будут иметь повышенные привилегии.",
    "When adding more than one extension, use a comma-separated list.": "При добавлении нескольких расширений используйте список, разделённый запятыми.",
    "Only Dynatrace extensions can be elevated, while custom ones cannot. In case an extension was configured to run with elevated privileges but was already executed (the process is running), it’s necessary to force the process to restart by either restarting the OneAgent service or temporarily disabling and re-enabling the extension monitoring configuration.": "Повышение привилегий доступно только для расширений Dynatrace; пользовательские расширения не могут быть повышены. Если расширение настроено на выполнение с повышенными привилегиями, но уже запущено (процесс работает), необходимо принудительно перезапустить процесс путём перезапуска службы OneAgent или временного отключения и повторного включения конфигурации мониторинга расширения.",
    "## Related topics": "## Связанные темы",
    '* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")': '* [Разработка собственных расширений](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace.")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "eec-custom-configuration.md", TRANS, PASS)
    qa_one(REL, "eec-custom-configuration.md")
