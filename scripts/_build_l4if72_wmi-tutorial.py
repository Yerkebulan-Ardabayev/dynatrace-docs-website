# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../wmi-extensions/wmi-tutorial.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Mar 30, 2022": "* Опубликовано 30 марта 2022 г.",
    "This is a step-by-step tutorial for building a WMI data source-based extension. You will build a WMI extension that runs on OneAgent and monitors a Windows host.": "Это пошаговое учебное руководство по созданию расширения на основе источника данных WMI. В нём создаётся расширение WMI, работающее на OneAgent и выполняющее мониторинг хоста Windows.",
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    '**Generate a developer certificate and key**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#generate-certificate-and-key "Learn about WMI extensions in the Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': '**Создание разработческого сертификата и ключа**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#generate-certificate-and-key "Learn about WMI extensions in the Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    '**Distribute the root certificate to Dynatrace components**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#distribute-root-certificate "Learn about WMI extensions in the Extensions framework.")': '**Распространение корневого сертификата на компоненты Dynatrace**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#distribute-root-certificate "Learn about WMI extensions in the Extensions framework.")',
    "## Before you begin": "## Перед началом работы",
    "To successfully develop an Extensions extension and be able to complete this tutorial, you need to fulfill the following prerequisites:": "Для успешного создания расширения Extensions и прохождения этого руководства необходимо выполнить следующие предварительные требования:",
    "* Admin access to a Dynatrace SaaS or Managed environment version 1.227+": "* Доступ администратора к среде Dynatrace SaaS или Managed версии 1.227+",
    "* Windows host (virtual machine)": "* Хост Windows (виртуальная машина)",
    "* OneAgent version 1.227+ deployed on the host": "* OneAgent версии 1.227+, развёрнутый на хосте",
    "* Dynatrace CLI": "* Dynatrace CLI",
    "+ Python 3.10 or 3.14": "+ Python 3.10 или 3.14",
    "+ Access to pip package installer for Python": "+ Доступ к установщику пакетов pip для Python",
    "+ Install dt-cli": "+ Установите dt-cli",
    'For more information, see [Sign extensions](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").': 'Дополнительные сведения см. в разделе [Подписание расширений](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").',
    "* Your root certificate uploaded to Dynatrace and on the OneAgent host": "* Корневой сертификат загружен в Dynatrace и на хост OneAgent",
    "## Step 1 Generate a developer certificate and key": "## Шаг 1. Создание разработческого сертификата и ключа",
    "The command generates the following files:": "Команда создаёт следующие файлы:",
    "* `developer.pem` - your developer certificate": "* `developer.pem`: разработческий сертификат",
    "* `ca.pem` - your root certificate": "* `ca.pem`: корневой сертификат",
    "* `ca.key` - your root key": "* `ca.key`: корневой ключ",
    "## Step 2 Distribute the root certificate to Dynatrace components": "## Шаг 2. Распространение корневого сертификата на компоненты Dynatrace",
    "### Upload to the Dynatrace Credential Vault": "### Загрузка в хранилище учётных данных Dynatrace",
    "1. Go to **Credential Vault**.": "1. Откройте **Credential Vault**.",
    "2. Select **Add new credential**.": "2. Выберите **Add new credential**.",
    "3. For **Credential type**, select **Public Certificate**.": "3. В поле **Credential type** выберите **Public Certificate**.",
    "4. Select the **Extension validation** credential scope.": "4. Выберите область доступа к учётным данным **Extension validation**.",
    "5. Add a meaningful **Credential name**.": "5. Добавьте понятное **Credential name**.",
    "6. Upload the **Root certificate file**.": "6. Загрузите **Root certificate file**.",
    "7. Select **Save**.": "7. Выберите **Save**.",
    "### Upload to OneAgent host that runs the extension": "### Загрузка на хост OneAgent, на котором выполняется расширение",
    "1. Go to the following directory:": "1. Перейдите в следующий каталог:",
    "* Windows: `C:\\ProgramData\\dynatrace\\oneagent\\agent\\config`": "* Windows: `C:\\ProgramData\\dynatrace\\oneagent\\agent\\config`",
    "* Linux: `/var/lib/dynatrace/oneagent/agent/config/`": "* Linux: `/var/lib/dynatrace/oneagent/agent/config/`",
    "2. Go to the `certificates` folder (create it if it doesn't exist)": "2. Перейдите в папку `certificates` (создайте её, если она не существует)",
    "3. Upload your root certificate (`ca.pem`) generated earlier": "3. Загрузите корневой сертификат (`ca.pem`), сгенерированный ранее",
    "Your Dynatrace environment is ready to start creating your WMI extension.": "Среда Dynatrace готова к созданию расширения WMI.",
    '**Next step**: [Extension package](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01 "Learn about WMI extensions in the Extensions framework.")': '**Следующий шаг**: [Пакет расширения](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01 "Learn about WMI extensions in the Extensions framework.")',
}

PASS = {
    "title: WMI data source tutorial",
    "# WMI data source tutorial",
}

if __name__ == "__main__":
    build_one(REL, "wmi-tutorial.md", TRANS, PASS)
    qa_one(REL, "wmi-tutorial.md")
