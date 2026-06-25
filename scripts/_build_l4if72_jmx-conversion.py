# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../addon-for-vscode/guides/jmx-conversion.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/addon-for-vscode/guides"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Jun 16, 2025": "* Опубликовано 16 июня 2025 г.",
    'The [Extensions Framework](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") for JMX has been available since version 1.213 and brings you new possibilities for visualizing and querying your data. Follow this guide to learn how to leverage Visual Studio Code to convert your 1.0 extensions to the new format automatically.': 'Платформа [Extensions Framework](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.") для JMX доступна начиная с версии 1.213 и открывает новые возможности визуализации и запросов к данным. Следуйте этому руководству, чтобы узнать, как использовать Visual Studio Code для автоматического преобразования расширений версии 1.0 в новый формат.',
    "## Prerequisites": "## Предварительные требования",
    "1. Complete the first-time setup for your editor": "1. Выполните первоначальную настройку редактора",
    'For simplicity, this guide will assume you have already configured your editor for first-time use. If you haven\'t used Dynatrace Extensions for VS Code before, follow our [Getting started guide](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes.") to complete your first-time setup.': 'Для простоты это руководство предполагает, что редактор уже настроен для первоначального использования. Если Dynatrace Extensions для VS Code ещё не использовались, следуйте [руководству по началу работы](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Настройте редактор Visual Studio Code и создайте первое расширение, загрузив его в Dynatrace за 5 минут."), чтобы выполнить первоначальную настройку.',
    'This guide assumes you have access to developer credentials. If you followed the [Getting started](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes.") guide, store the generated credentials in VS Code\'s global settings. An example is shown the [Settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#when-using-your-credentials "Details of settings available to configure Dynatrace Extensions") page.': 'В руководстве предполагается наличие доступа к разработческим учётным данным. Если следовали руководству [по началу работы](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Настройте редактор Visual Studio Code и создайте первое расширение, загрузив его в Dynatrace за 5 минут."), сохраните созданные учётные данные в глобальных настройках VS Code. Пример приведён на странице [Настройки](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#when-using-your-credentials "Сведения о настройках, доступных для конфигурации Dynatrace Extensions").',
    "2. Enable JMX 2.0 extensions in your environment": "2. Включите расширения JMX 2.0 в своём окружении",
    "Go to **Settings > Preferences > OneAgent features** and enable **Java Metric Extensions (JMX)**, then restart your monitored Java processes.": "Откройте **Settings > Preferences > OneAgent features** и включите **Java Metric Extensions (JMX)**, затем перезапустите отслеживаемые процессы Java.",
    "## Convert a JMX Extension as a new project": "## Преобразование расширения JMX как нового проекта",
    "### Initialize your workspace": "### Инициализация рабочего пространства",
    "1. Create a new folder on your computer and open it in VS Code.": "1. Создайте новую папку на компьютере и откройте её в VS Code.",
    "2. Press F1 then select the command **Dynatrace extensions: Initialize workspace**": "2. Нажмите F1 и выберите команду **Dynatrace extensions: Initialize workspace**",
    "3. Next, choose schema version **1.275.0** from the list": "3. Затем выберите из списка версию схемы **1.275.0**",
    "4. When prompted about certificates, choose **Use existing**": "4. При запросе о сертификатах выберите **Use existing**",
    "5. When prompted about project type, choose **JMX 1.0 Conversion**": "5. При запросе о типе проекта выберите **JMX 1.0 Conversion**",
    "Your workspace has been initialized, and you're ready to convert your old extension.": "Рабочее пространство инициализировано, и можно приступать к преобразованию старого расширения.",
    "### Convert your extension": "### Преобразование расширения",
    "1. You need to load the JMX 1.0 Extension for conversion. You can browse your local filesystem for a `.zip` or `plugin.json` file or browse your connected Dynatrace environment. As part of this guide, we'll do the latter. Choose to load it **Remotely**.": "1. Необходимо загрузить расширение JMX 1.0 для преобразования. Можно выбрать файл `.zip` или `plugin.json` в локальной файловой системе либо просмотреть подключённое окружение Dynatrace. В рамках этого руководства выберем второй вариант. Выберите загрузку **Remotely**.",
    "2. You are now presented with a list of extensions from your tenant. Choose which one you want to convert.": "2. Отобразится список расширений из тенанта. Выберите расширение, которое требуется преобразовать.",
    "After selecting an extension, you may be prompted for a new extension name if your old one is too long.": "После выбора расширения может появиться запрос на ввод нового имени расширения, если старое слишком длинное.",
    "3. Next, you should select a technology so that Process pages can be configured automatically. Choose one that applies to your Java process. Otherwise, choose **All other**.": "3. Затем выберите технологию, чтобы страницы Process можно было настроить автоматически. Выберите подходящую для процесса Java. В противном случае выберите **All other**.",
    "4. Optionally, we can also show the data on your Host's page. To follow along with this guide, select **Yes**.": "4. При желании данные также можно отображать на странице хоста. Чтобы продолжить работу с этим руководством, выберите **Yes**.",
    "The conversion will generate your new extension manifest at `extension/extension.yaml`.": "В результате преобразования новый манифест расширения будет создан по пути `extension/extension.yaml`.",
    "## Convert a JMX Extension standalone": "## Автономное преобразование расширения JMX",
    "If you don't want to initialize a new workspace for your project or you're already working within a registered workspace, you can run our automation as a standalone command.": "Если инициализировать новое рабочее пространство не требуется или работа уже ведётся в зарегистрированном рабочем пространстве, автоматизацию можно запустить как отдельную команду.",
    "Press F1 and select the command **Dynatrace Extensions: Convert JMX**. This workflow starts by first prompting you to load the extension and follows the same steps as mentioned above.": "Нажмите F1 и выберите команду **Dynatrace Extensions: Convert JMX**. Этот рабочий процесс начинается с запроса на загрузку расширения и выполняет те же шаги, что описаны выше.",
    "At the end, your new manifest will be placed in `extension/extension.yaml`, or you'll be prompted for a save destination if this folder doesn't exist in the currently opened workspace.": "По завершении новый манифест будет помещён в `extension/extension.yaml` либо появится запрос на выбор места сохранения, если данная папка не существует в текущем открытом рабочем пространстве.",
    "## Deploy and configure your new extension": "## Развёртывание и настройка нового расширения",
    "### Build and upload to Dynatrace": "### Сборка и загрузка в Dynatrace",
    "1. Build the extension by pressing F1 then clicking the command **Dynatrace extensions: Build**.": "1. Выполните сборку расширения: нажмите F1 и выберите команду **Dynatrace extensions: Build**.",
    "2. Then, choose to upload it to Dynatrace by clicking **Yes**.": "2. Затем выберите загрузку в Dynatrace, нажав **Yes**.",
    "3. Next, activate this extension by clicking **Yes**.": "3. Затем активируйте расширение, нажав **Yes**.",
    "### Add a monitoring configuration": "### Добавление конфигурации мониторинга",
    "1. Open your extension either from the prompt or from the Extensions menu in Dynatrace.": "1. Откройте расширение из запроса или из меню Extensions в Dynatrace.",
    "2. Add a monitoring configuration by clicking the button.": "2. Добавьте конфигурацию мониторинга, нажав кнопку.",
    "3. Select a Host running your Java process, then click **Next step**.": "3. Выберите хост, на котором выполняется процесс Java, затем нажмите **Next step**.",
    "4. On the next page click **Next step** once again, then add a description and click **Activate**.": "4. На следующей странице снова нажмите **Next step**, затем добавьте описание и нажмите **Activate**.",
    "Once your monitoring configuration is activated, data collection starts automatically.": "После активации конфигурации мониторинга сбор данных начинается автоматически.",
    "## Find your extension's data": "## Поиск данных расширения",
    "Open the details page of one of the hosts running your monitored Java process. You should see a card (towards the bottom) with a title starting with **JMX Metrics**.": "Откройте страницу сведений одного из хостов, на которых выполняется отслеживаемый процесс Java. Внизу страницы должна отображаться карточка с заголовком, начинающимся с **JMX Metrics**.",
    "From that card, select any of the processes listed. Then click `...` and choose **Metrics and logs analysis**.": "В этой карточке выберите любой из перечисленных процессов. Затем нажмите `...` и выберите **Metrics and logs analysis**.",
    "On the page that opens, you'll have multiple cards from your extension.": "На открывшейся странице отобразятся несколько карточек из вашего расширения.",
    "The cards on the Process page are only added if you selected a technology during the conversion.": "Карточки на странице Process добавляются только в том случае, если технология была выбрана в процессе преобразования.",
}

PASS = {
    "title: Migrate JMX extensions",
    "# Migrate JMX extensions",
}

if __name__ == "__main__":
    build_one(REL, "jmx-conversion.md", TRANS, PASS)
    qa_one(REL, "jmx-conversion.md")
