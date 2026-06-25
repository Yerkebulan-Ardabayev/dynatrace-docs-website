# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/addon-for-vscode"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 5-min read": "* Чтение: 5 мин",
    "* Published Jun 16, 2025": "* Опубликовано 16 июня 2025 г.",
    "Get started with Dynatrace Extensions by following this guide to set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes.": "Начните работу с Dynatrace Extensions, следуя этому руководству: настройте редактор Visual Studio Code и соберите и загрузите первое расширение в Dynatrace за 5 минут.",
    "## Before you begin": "## Подготовка",
    "### Installation": "### Установка",
    "You can find **Dynatrace Extensions** in the Visual Studio Code [marketplace](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions). Install it from there or via the VS Code extension search.": "**Dynatrace Extensions** доступно в [магазине](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions) Visual Studio Code. Установить его можно оттуда или через поиск расширений VS Code.",
    "### Access token": "### Токен доступа",
    "Our VS Code add-on automates many operations around Extension 2.0 development by using the Dynatrace API.": "Дополнение VS Code автоматизирует многие операции разработки Extension 2.0, используя Dynatrace API.",
    'To get the most out of it, create an [API Access Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the following scopes:': 'Чтобы использовать все возможности дополнения, создайте [токен доступа к API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях.") со следующими областями доступа:',
    "The Dynatrace UI provides a dedicated template called **Extension Development**, which applies these exact token scopes.": "Интерфейс Dynatrace предоставляет специальный шаблон **Extension Development**, который применяет именно эти области доступа токена.",
    "### Connectivity settings": "### Настройки подключения",
    "This step is only required if your Dynatrace environment is accessible through a dedicated URL that uses a custom-signed or a self-signed SSL certificate.": "Этот шаг необходим только в том случае, если окружение Dynatrace доступно через выделенный URL, использующий пользовательский или самоподписанный SSL-сертификат.",
    "In this situation, you need to adapt your settings before you can continue with this guide. Go to **File > Preferences > Settings**, expand on **Extensions**, and find the **Dynatrace Extensions** section. Scroll down until you see **Tenant Connectivity Settings** and select **Edit in settings.json**.": "В этом случае необходимо настроить параметры перед продолжением работы с руководством. Откройте **File > Preferences > Settings**, разверните раздел **Extensions** и найдите секцию **Dynatrace Extensions**. Прокрутите вниз до **Tenant Connectivity Settings** и выберите **Edit in settings.json**.",
    "Register your dedicated environment URL in the file you've opened and either provide the path to your CA file or turn off SSL verification. For example:": "Зарегистрируйте URL выделенного окружения в открытом файле и укажите путь к CA-файлу или отключите проверку SSL. Например:",
    'Explore all the [tenant connectivity settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#tenant-connectivity-settings "Details of settings available to configure Dynatrace Extensions").': 'Ознакомьтесь со всеми [настройками подключения тенанта](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#tenant-connectivity-settings "Подробности настроек для конфигурации Dynatrace Extensions").',
    "## Connect to Dynatrace": "## Подключение к Dynatrace",
    "Begin by connecting with your Dynatrace environment. To connect, you need to do the following:": "Начните с подключения к окружению Dynatrace. Для этого выполните следующие действия:",
    "* Go to the Dynatrace Extensions view in the VS Code UI, then select the **Add environment** button as shown.": "* Откройте представление Dynatrace Extensions в интерфейсе VS Code и выберите кнопку **Add environment**, как показано.",
    "You'll need to provide the base URL to access Dynatrace. It should follow one of these patterns:": "Укажите базовый URL для доступа к Dynatrace. Он должен соответствовать одному из следующих шаблонов:",
    "+ `https://<Id>.live.dynatrace.com` for SaaS environments.": "+ `https://<Id>.live.dynatrace.com` для SaaS-окружений.",
    "+ `https://<Domain>/e/<Id>` for Managed environments.": "+ `https://<Domain>/e/<Id>` для Managed-окружений.",
    "+ `https://<Id>.apps.dynatrace.com` for the latest Dynatrace Platform.": "+ `https://<Id>.apps.dynatrace.com` для последней версии платформы Dynatrace.",
    "**Note**: Replace `<Id>` with your environment ID and `<Domain>` with your managed environment domain.": "**Примечание**: замените `<Id>` идентификатором окружения, а `<Domain>` соответствует домену управляемого окружения.",
    "* Provide the **API Access Token** you prepared earlier and optionally provide a label.": "* Укажите **API Access Token**, подготовленный ранее, и при необходимости добавьте метку.",
    "* Set this as your current environment.": "* Задайте это окружение как текущее.",
    'The add-on displays your environment in the list and will use the current environment for all API operations. Visit [Environments](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#environments "Details about the specialized activity bar views for Dynatrace Extensions") to learn more about using the Environment view.': 'Дополнение отображает окружение в списке и использует текущее окружение для всех операций API. Дополнительные сведения об использовании представления Environment см. в разделе [Environments](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#environments "Подробности о специализированных представлениях панели действий для Dynatrace Extensions").',
    "## Initialize your workspace": "## Инициализация рабочего пространства",
    "It's time to create your first project. If you need to open a different workspace folder, select **Open folder**. Otherwise, select the **Initialize workspace** button to start.": "Пришло время создать первый проект. Если нужно открыть другую папку рабочего пространства, выберите **Open folder**. В противном случае нажмите кнопку **Initialize workspace** для начала.",
    'To learn how to use the Workspaces view, visit [Extension 2.0 workspaces](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#extension-20-workspaces "Details about the specialized activity bar views for Dynatrace Extensions").': 'Сведения об использовании представления Workspaces см. в разделе [Extension 2.0 workspaces](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#extension-20-workspaces "Подробности о специализированных представлениях панели действий для Dynatrace Extensions").',
    "### 1. Schema validation": "### 1. Проверка схемы",
    "The workflow starts with your target schema version. Choose any from the list. It ensures that we can validate your extension manifest while you're writing it, allowing you to spot any issues early on.": "Рабочий процесс начинается с выбора целевой версии схемы из списка. Это позволяет проверять манифест расширения в процессе написания и выявлять проблемы на раннем этапе.",
    "### 2. Developer certificates": "### 2. Разработческие сертификаты",
    "Extensions use developer certificates for signing and packaging extensions. Choose **Generate new ones** to generate a new set of certificates kept in VS Code's storage.": "Extensions использует разработческие сертификаты для подписи и упаковки расширений. Выберите **Generate new ones**, чтобы создать новый набор сертификатов, хранящихся в хранилище VS Code.",
    'Check the extension\'s [settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings "Details of settings available to configure Dynatrace Extensions") to get the exact path to where your credentials are stored.': 'Сведения о точном пути хранения учётных данных см. в [настройках](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings "Подробности настроек для конфигурации Dynatrace Extensions") расширения.',
    "The workflow offers some additional convenience steps:": "Рабочий процесс предлагает несколько дополнительных удобных шагов:",
    "* Whether to use these certificates as defaults for all workspaces:": "* Использовать ли эти сертификаты по умолчанию для всех рабочих пространств:",
    "+ This will update your global settings for Dynatrace Extensions to reflect this choice.": "+ Это обновит глобальные настройки Dynatrace Extensions в соответствии с выбором.",
    "+ As part of this guide, choose **Yes**.": "+ В рамках данного руководства выберите **Yes**.",
    "* Whether to upload the new CA certificate to the Dynatrace Credentials Vault.": "* Загружать ли новый корневой сертификат в хранилище учётных данных Dynatrace.",
    "+ You need to provide a name and, optionally, a description.": "+ Укажите имя и при необходимости описание.",
    "+ As part of this guide, choose **Yes** and provide the additional details.": "+ В рамках данного руководства выберите **Yes** и укажите дополнительные сведения.",
    "* Whether to upload the new CA certificate to locally installed OneAgents and ActiveGates.": "* Загружать ли новый корневой сертификат в локально установленные OneAgent и ActiveGate.",
    "+ This step only appears if a local OneAgent or ActiveGate installation is detected.": "+ Этот шаг появляется только при обнаружении локальной установки OneAgent или ActiveGate.",
    "+ This step requires running VS Code with Administrator privileges.": "+ Этот шаг требует запуска VS Code с правами администратора.",
    "+ As part of this guide, choose **No**.": "+ В рамках данного руководства выберите **No**.",
    'To learn how to use your existing developer certificates, visit [Credentials](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#credentials "Details of settings available to configure Dynatrace Extensions").': 'Сведения об использовании имеющихся разработческих сертификатов см. в разделе [Credentials](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#credentials "Подробности настроек для конфигурации Dynatrace Extensions").',
    "### 3. Project template": "### 3. Шаблон проекта",
    "The final step of the workflow is to choose the type of project you want to start. It allows the extension to generate relevant files.": "Последний шаг рабочего процесса: выбор типа проекта. Это позволяет расширению создать нужные файлы.",
    "Since this is your first extension, choose **Extension 2.0 ⭐** at this step.": "Поскольку это первое расширение, на этом шаге выберите **Extension 2.0 ⭐**.",
    "This option is the default choice for new projects and will create the following starting setup:": "Этот вариант является выбором по умолчанию для новых проектов и создаёт следующую начальную структуру:",
    "* `extension` - the folder where all extension assets are placed.": "* `extension`: папка, в которой размещаются все ресурсы расширения.",
    "* `extension/extension.yaml` - this is your extension's manifest file.": "* `extension/extension.yaml`: файл манифеста расширения.",
    'To learn more about the other types of projects, visit [Project templates](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/commands#project-templates "Overview of all the commands available within Dynatrace Extensions").': 'Дополнительные сведения о других типах проектов см. в разделе [Project templates](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/commands#project-templates "Обзор всех команд, доступных в Dynatrace Extensions").',
    "In addition, all templates also create the following folders and files:": "Кроме того, все шаблоны создают следующие папки и файлы:",
    "* `.vscode` - a folder for storing workspace-specific VS Code settings.": "* `.vscode`: папка для хранения настроек VS Code, специфичных для рабочего пространства.",
    "* `dist` - a folder for storing all extension packages.": "* `dist`: папка для хранения всех пакетов расширений.",
    "* `config` - a folder for storing your monitoring configuration files.": "* `config`: папка для хранения файлов конфигурации мониторинга.",
    "* `.gitignore` - a file containing useful rules for ignoring unnecessary items from your git repository.": "* `.gitignore`: файл с правилами игнорирования ненужных элементов в репозитории git.",
    "## Make some changes to your extension": "## Внесение изменений в расширение",
    "Start by opening up the extension manifest and making some changes. Give your extension a name, and add yourself as the author.": "Откройте манифест расширения и внесите изменения: задайте имя расширению и добавьте себя в качестве автора.",
    "For example, update the `extension/extension.yaml` file with the following information:": "Например, обновите файл `extension/extension.yaml` следующими данными:",
    "Replace `<Your-Name>` with the author's name.": "Замените `<Your-Name>` именем автора.",
    "## Publish your extension": "## Публикация расширения",
    "Finally, perform the following steps to upload your extension to Dynatrace.": "Наконец, выполните следующие шаги для загрузки расширения в Dynatrace.",
    "1. Press the F1 key and choose the **Dynatrace extensions: Build** command. The workflow will build your extension, creating a package inside your `dist` folder.": "1. Нажмите клавишу F1 и выберите команду **Dynatrace extensions: Build**. Рабочий процесс соберёт расширение и создаст пакет в папке `dist`.",
    "2. When prompted about uploading your extension to Dynatrace, choose **Yes**.": "2. При запросе о загрузке расширения в Dynatrace выберите **Yes**.",
    "3. When prompted about activating this extension version, choose **Yes**.": "3. При запросе об активации этой версии расширения выберите **Yes**.",
    "Congratulations. You created, built, uploaded, and activated your first Extension 2.0. You can view this in the Dynatrace UI by navigating to Extensions.": "Расширение создано, собрано, загружено и активировано. Просмотреть его можно в интерфейсе Dynatrace, перейдя в раздел Extensions.",
}

PASS = {
    "title: Getting started",
    "# Getting started",
    # API token scope lines — pure EN identifiers, pass verbatim
    "* `WriteConfig`",
    "* `ReadConfig`",
    "* `credentialVault.read`",
    "* `credentialVault.write`",
    "* `extensions.read`",
    "* `extensions.write`",
    "* `extensionEnvironment.write`",
    "* `extensionEnvironment.read`",
    "* `extensionConfigurations.read`",
    "* `extensionConfigurations.write`",
    "* `metrics.read`",
    "* `entities.read`",
    "* `settings.read`",
    "* `settings.write`",
}

if __name__ == "__main__":
    build_one(REL, "getting-started.md", TRANS, PASS)
    qa_one(REL, "getting-started.md")
