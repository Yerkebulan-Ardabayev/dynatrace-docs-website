# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../data-sources/wmi-extensions.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Mar 04, 2026": "* Обновлено 4 марта 2026 г.",
    "Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your Windows Management Instrumentation (WMI) monitored devices.": "Dynatrace предоставляет платформу для расширения наблюдаемости с помощью данных, получаемых напрямую с устройств под мониторингом Windows Management Instrumentation (WMI).",
    "We assume the following:": "Предполагается следующее:",
    "* You possess sufficient Windows and WMI subject matter expertise to create a WMI extension.": "* У вас достаточно знаний по Windows и WMI для создания расширения WMI.",
    '* You\'re familiar with [Extensions basic concepts](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").': '* Вы знакомы с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").',
    "## Prerequisites and support": "## Предварительные требования и поддержка",
    'Learn the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions limits](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").': 'Изучите предварительные требования и область поддерживаемых технологий. Об ограничениях, применяемых к расширению, см. в разделе [Ограничения Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.").',
    "### Supported Dynatrace versions": "### Поддерживаемые версии Dynatrace",
    "* Dynatrace version 1.215+": "* Dynatrace версии 1.215+",
    "* Windows-based Environment ActiveGate version 1.215+": "* ActiveGate среды на базе Windows версии 1.215+",
    "* OneAgent version 1.221+ (local extensions)": "* OneAgent версии 1.221+ (локальные расширения)",
    "### Monitored host": "### Отслеживаемый хост",
    'Local WMI extensions can be run on any OneAgent-supported Windows host without any special requirements. Make sure Extension Execution Controller (EEC) is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/managed/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").': 'Локальные расширения WMI можно запускать на любом хосте Windows, поддерживаемом OneAgent, без дополнительных требований. Убедитесь, что Extension Execution Controller (EEC) включён на уровне среды или выбранного хоста. Дополнительные сведения см. в разделе [Extension Execution Controller](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Dynatrace Extensions.").',
    "A host you want to monitor using a remote WMI extension must meet the requirements described below, including remote permissions enabled and connectivity details configured to allow your ActiveGate to access the WMI monitoring data.": "Хост, который требуется отслеживать с помощью удалённого расширения WMI, должен соответствовать описанным ниже требованиям, включая включённые удалённые разрешения и настроенные параметры подключения, позволяющие ActiveGate получать доступ к данным мониторинга WMI.",
    "#### Remote enable permission on the host": "#### Разрешение на удалённое подключение на хосте",
    "A monitored host must have the **Remote enable** permission set.": "На отслеживаемом хосте должно быть установлено разрешение **Remote enable**.",
    "1. In the Microsoft [Server Manager](https://docs.microsoft.com/en-us/windows-server/administration/server-manager/server-manager) console, go to **Administrative Tools** > **Computer Management**.": "1. В консоли Microsoft [Server Manager](https://docs.microsoft.com/en-us/windows-server/administration/server-manager/server-manager) откройте **Administrative Tools** > **Computer Management**.",
    "2. Expand **Services and Applications**, right-click **WMI Control**, and select **Properties**.": "2. Разверните **Services and Applications**, щёлкните правой кнопкой мыши **WMI Control** и выберите **Properties**.",
    "3. Select the **Security** tab and then select the **Security** button.": "3. Выберите вкладку **Security**, затем нажмите кнопку **Security**.",
    "4. Add the user you'll use to call WMI and then select **Remote Enable** in the **Allow** column.": "4. Добавьте пользователя, который будет использоваться для вызовов WMI, и выберите **Remote Enable** в столбце **Allow**.",
    "For more information, see [Allowing Users Access to a Specific WMI Namespace](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection#allowing-users-access-to-a-specific-wmi-namespace) in the Microsoft documentation.": "Дополнительные сведения см. в документации Microsoft: [Allowing Users Access to a Specific WMI Namespace](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection#allowing-users-access-to-a-specific-wmi-namespace).",
    "#### Configure firewall to access remote WMI": "#### Настройка брандмауэра для доступа к удалённому WMI",
    "To configure the firewall to access remote WMI, issue the following commands:": "Для настройки брандмауэра для доступа к удалённому WMI выполните следующие команды:",
    "and": "и",
    "For more information, see [Setting up a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista) in the Microsoft documentation.": "Дополнительные сведения см. в документации Microsoft: [Setting up a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista).",
    "#### Disable Remote UAC": "#### Отключение удалённого UAC",
    "Disable Remote UAC when using a local administrator account (without Active Directory).": "Отключите удалённый UAC при использовании локальной учётной записи администратора (без Active Directory).",
    "For more information, see [Handling Remote Connections Under UAC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/user-account-control-and-wmi#handling-remote-connections-under-uac) in the Microsoft documentation.": "Дополнительные сведения см. в документации Microsoft: [Handling Remote Connections Under UAC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/user-account-control-and-wmi#handling-remote-connections-under-uac).",
    "#### Set up local user": "#### Настройка локального пользователя",
    "To establish a connection to a WMI remote host, you need to use either a standard user or a user with administrator privileges, depending on the kind of data you want. You will add this user in [monitoring configuration](#monitoring-configuration). We recommend that you create a dedicated local user group or user account on the target computer specifically for remote connections.": "Для подключения к удалённому хосту WMI используйте стандартного пользователя или пользователя с правами администратора в зависимости от требуемых данных. Этот пользователь добавляется в [конфигурацию мониторинга](#monitoring-configuration). Рекомендуется создать выделенную локальную группу пользователей или учётную запись на целевом компьютере специально для удалённых подключений.",
    "To limit user privileges to access only a remote connection to WMI": "Для ограничения прав пользователя доступом только к удалённому подключению к WMI",
    "1. In Windows, run the `DCOMCNFG` command.": "1. В Windows выполните команду `DCOMCNFG`.",
    "2. Go to **Component Services** > **Computers**, right-click **My Computer**, and select **Properties**.": "2. Откройте **Component Services** > **Computers**, щёлкните правой кнопкой мыши **My Computer** и выберите **Properties**.",
    "3. Select the **COM Security** tab.": "3. Выберите вкладку **COM Security**.",
    "4. Under **Launch and Activation Permissions**, select **Edit Limits**.": "4. В разделе **Launch and Activation Permissions** выберите **Edit Limits**.",
    "5. Select the **ANONYMOUS LOGON** name in the **Group or user names** box. Under **Permissions for ANONYMOUS LOGON**, select **Remote Launch** and **Remote Activation** in the **Allow** column.": "5. В поле **Group or user names** выберите **ANONYMOUS LOGON**. В разделе **Permissions for ANONYMOUS LOGON** выберите **Remote Launch** и **Remote Activation** в столбце **Allow**.",
    "6. Select **OK** to save.": "6. Выберите **OK** для сохранения.",
    "For more information, see the Microsoft documentation:": "Дополнительные сведения см. в документации Microsoft:",
    "* [Securing a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)": "* [Securing a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)",
    "* [Limiting access to WMI namespaces](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-namespace-security-with-the-wmi-control)": "* [Limiting access to WMI namespaces](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-namespace-security-with-the-wmi-control)",
    "* [Access to WMI Namespaces](https://docs.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces)": "* [Access to WMI Namespaces](https://docs.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces)",
    "#### Set up a fixed port for WMI": "#### Настройка фиксированного порта для WMI",
    "1. At the command prompt, enter:": "1. В командной строке введите:",
    "`winmgmt -standalonehost`": "`winmgmt -standalonehost`",
    "2. Stop the WMI service:": "2. Остановите службу WMI:",
    "`net stop winmgmt`": "`net stop winmgmt`",
    "3. Restart the WMI service in a new service host:": "3. Перезапустите службу WMI в новом хосте службы:",
    "`net start winmgmt`": "`net start winmgmt`",
    "4. Establish a new port number for the WMI service:": "4. Задайте новый номер порта для службы WMI:",
    "`netsh firewall add portopening TCP 24158 WMIFixedPort`": "`netsh firewall add portopening TCP 24158 WMIFixedPort`",
    "For more information, see [Setting Up a Fixed Port for WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) in the Microsoft documentation.": "Дополнительные сведения см. в документации Microsoft: [Setting Up a Fixed Port for WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi).",
}

PASS = {
    "title: WMI data source",
    "# WMI data source",
}

if __name__ == "__main__":
    build_one(REL, "wmi-extensions.md", TRANS, PASS)
    qa_one(REL, "wmi-extensions.md")
