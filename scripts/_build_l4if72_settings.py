# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../addon-for-vscode/settings.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/addon-for-vscode"

TRANS = {
    "* Reference": "* Справочник",
    "* 4-min read": "* Чтение: 4 мин",
    "* Updated on Mar 23, 2026": "* Обновлено 23 марта 2026 г.",
    "You can define all settings either globally or for each workspace.": "Все настройки можно задать глобально или для каждого рабочего пространства.",
    "You can learn more about accessing these settings in Visual Studio Code's [official documentation](https://code.visualstudio.com/docs/getstarted/settings).": "Подробнее о доступе к этим настройкам см. в [официальной документации](https://code.visualstudio.com/docs/getstarted/settings) Visual Studio Code.",
    "## Credentials": "## Учётные данные",
    "**Dynatrace Extensions** can either generate all the credentials required for Extension 2.0 development or allow you to bring your own credential files.": "**Dynatrace Extensions** может либо создать все учётные данные, необходимые для разработки Extension 2.0, либо позволить использовать собственные файлы учётных данных.",
    "### When using your credentials": "### При использовании собственных учётных данных",
    "You need to provide your files by using these settings:": "Необходимо указать файлы с помощью следующих настроек:",
    "| Setting | Description |": "| Настройка | Описание |",
    "| --- | --- |": "| --- | --- |",
    '| `dynatraceExtensions.developerCertkeyLocation` | This is the path to your [developer credential](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions#cert "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.") file. |': '| `dynatraceExtensions.developerCertkeyLocation` | Путь к файлу [разработческих учётных данных](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions#cert "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework."). |',
    "| `dynatraceExtensions.rootOrCaCertificateLocation` | is the path to your root (CA) certificate. |": "| `dynatraceExtensions.rootOrCaCertificateLocation` | Путь к корневому сертификату (CA). |",
    "Example usage:": "Пример использования:",
    "### When generating credentials": "### При создании учётных данных",
    "You can customize the details that are embedded into the generated certificates by using these settings:": "Сведения, встраиваемые в создаваемые сертификаты, можно настроить с помощью следующих параметров:",
    "| Setting | Default value | Description |": "| Настройка | Значение по умолчанию | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| `dynatraceExtensions.certificateCommonName` | Extension Developer | The certificate's common name (CN) attribute. |": "| `dynatraceExtensions.certificateCommonName` | Extension Developer | Атрибут общего имени (CN) сертификата. |",
    "| `dynatraceExtensions.certificateOrganization` |  | The certificate's organization (O) attribute. |": "| `dynatraceExtensions.certificateOrganization` |  | Атрибут организации (O) сертификата. |",
    "| `dynatraceExtensions.certificateOrganizationUnit` |  | The certificate's organization unit (OU) attribute. |": "| `dynatraceExtensions.certificateOrganizationUnit` |  | Атрибут подразделения организации (OU) сертификата. |",
    "| `dynatraceExtensions.certificateStateOrProvince` |  | The certificate's state or province (ST) attribute. |": "| `dynatraceExtensions.certificateStateOrProvince` |  | Атрибут штата или провинции (ST) сертификата. |",
    "| `dynatraceExtensions.certificateCountryCode` |  | The certificate's country code (C) attribute. |": "| `dynatraceExtensions.certificateCountryCode` |  | Атрибут кода страны (C) сертификата. |",
    "## Behavior": "## Поведение",
    "The add-on aims to allow users to customize their extension development experience as much as possible. The following settings allow turning various features on or off on demand.": "Дополнение стремится предоставить пользователям максимальные возможности для настройки процесса разработки расширений. Следующие настройки позволяют включать или отключать различные функции по требованию.",
    "### Features": "### Функции",
    '| `dynatraceExtensions.metricSelectorsCodeLens` | true | [Metric selector code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#metric-selectors "Overview of all Dynatrace Extensions features to help you develop apps") |': '| `dynatraceExtensions.metricSelectorsCodeLens` | true | [Code lens для селектора метрик](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#metric-selectors "Обзор всех функций Dynatrace Extensions для разработки приложений") |',
    '| `dynatraceExtensions.entitySelectorsCodeLens` | true | [Entity selector code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#entity-selectors "Overview of all Dynatrace Extensions features to help you develop apps") |': '| `dynatraceExtensions.entitySelectorsCodeLens` | true | [Code lens для селектора сущностей](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#entity-selectors "Обзор всех функций Dynatrace Extensions для разработки приложений") |',
    '| `dynatraceExtensions.fastDevelopmentMode` | false | [Fast development mode](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#fast-development-mode "Overview of all Dynatrace Extensions features to help you develop apps") |': '| `dynatraceExtensions.fastDevelopmentMode` | false | [Режим быстрой разработки](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#fast-development-mode "Обзор всех функций Dynatrace Extensions для разработки приложений") |',
    '| `dynatraceExtensions.wmiCodeLens` | true | [WMI queries code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#windows-management-interface-wmi-queries "Overview of all Dynatrace Extensions features to help you develop apps") |': '| `dynatraceExtensions.wmiCodeLens` | true | [Code lens для запросов WMI](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#windows-management-interface-wmi-queries "Обзор всех функций Dynatrace Extensions для разработки приложений") |',
    '| `dynatraceExtensions.screenCodeLens` | true | [Unified analysis screen code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#unified-analysis-screens "Overview of all Dynatrace Extensions features to help you develop apps") |': '| `dynatraceExtensions.screenCodeLens` | true | [Code lens для экранов унифицированного анализа](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#unified-analysis-screens "Обзор всех функций Dynatrace Extensions для разработки приложений") |',
    "### Logging": "### Журналирование",
    "| `dynatraceExtensions.logging.level` | `INFO` | The minimum level of log messages |": "| `dynatraceExtensions.logging.level` | `INFO` | Минимальный уровень сообщений журнала |",
    "| `dynatraceExtensions.logging.maxFiles` | 10 | The maximum number of log files (by age) kept on disk. |": "| `dynatraceExtensions.logging.maxFiles` | 10 | Максимальное количество файлов журнала (по возрасту), хранимых на диске. |",
    "| `dynatraceExtensions.logging.maxFileSize` | 10 | The maximum size of a single log file (in MB). |": "| `dynatraceExtensions.logging.maxFileSize` | 10 | Максимальный размер одного файла журнала (в МБ). |",
    "### Tenant Connectivity Settings": "### Настройки подключения к тенанту",
    "The add-on always performs web requests to your Dynatrace environment over HTTPS. In specific scenarios—for example, in Dynatrace Managed—your environment may be accessible through a dedicated endpoint that uses either a custom-signed or a self-signed SSL certificate. While valid for encryption, most frameworks and browsers don't recognize these certificates as trusted, which causes requests to fail.": "Дополнение всегда выполняет веб-запросы к среде Dynatrace по HTTPS. В некоторых сценариях, например в Dynatrace Managed, среда может быть доступна через выделенный эндпоинт, использующий SSL-сертификат с пользовательской подписью или самоподписанный сертификат. Хотя такие сертификаты обеспечивают шифрование, большинство фреймворков и браузеров не признают их доверенными, что приводит к сбою запросов.",
    "The `dynatraceExtensions.tenantConnectivitySettings` setting is only available from your `settings.json` file and represents an array of environment endpoints that require special settings for HTTPS connectivity. Each entry in the array is an object with the following details:": "Параметр `dynatraceExtensions.tenantConnectivitySettings` доступен только из файла `settings.json` и представляет собой массив эндпоинтов среды, требующих специальных настроек для подключения по HTTPS. Каждый элемент массива является объектом со следующими полями:",
    "| Attribute | Default value | Description |": "| Атрибут | Значение по умолчанию | Описание |",
    '| `tenantUrl` | "" | The base URL to your Dynatrace environment. The add-on will use the URL to decide when to apply special connectivity settings on web requests. |': '| `tenantUrl` | "" | Базовый URL вашей среды Dynatrace. Дополнение использует этот URL для определения момента применения специальных настроек подключения к веб-запросам. |',
    '| `certificatePath` | "" | The path on disk to a Root/CA file in `.pem` or `.crt` format. The add-on will load this file and add it to the list of trusted CAs for the given `tenantUrl`. |': '| `certificatePath` | "" | Путь на диске к файлу Root/CA в формате `.pem` или `.crt`. Дополнение загрузит этот файл и добавит его в список доверенных центров сертификации для указанного `tenantUrl`. |',
    "| `disableSSLVerification` | `false` | When enabled, the add-on ignores SSL certificates for the given `tenantUrl`. Enable this only when using self-signed certificates on your Dynatrace endpoint. |": "| `disableSSLVerification` | `false` | При включении дополнение игнорирует SSL-сертификаты для указанного `tenantUrl`. Включайте только при использовании самоподписанных сертификатов на эндпоинте Dynatrace. |",
    "Example:": "Пример:",
    "* Adding a custom certificate to the trusted CAs:": "* Добавление пользовательского сертификата в список доверенных центров сертификации:",
    "* Using a self-signed certificate on an endpoint:": "* Использование самоподписанного сертификата на эндпоинте:",
    "## Diagnostics": "## Диагностика",
    "| `dynatraceExtensions.diagnostics.all` | true | All diagnostics |": "| `dynatraceExtensions.diagnostics.all` | true | Вся диагностика |",
    "| `dynatraceExtensions.diagnostics.extensionName` | true | The name of the extension |": "| `dynatraceExtensions.diagnostics.extensionName` | true | Имя расширения |",
    "| `dynatraceExtensions.diagnostics.metricKeys` | true | Keys used for metric definitions |": "| `dynatraceExtensions.diagnostics.metricKeys` | true | Ключи, используемые для определений метрик |",
    "| `dynatraceExtensions.diagnostics.cardKeys` | true | Keys of cards referenced/defined in the screens section |": "| `dynatraceExtensions.diagnostics.cardKeys` | true | Ключи карточек, на которые ссылаются или которые определены в разделе screens |",
    "| `dynatraceExtensions.diagnostics.snmp` | true | SNMP data source, especially the use of OIDs |": "| `dynatraceExtensions.diagnostics.snmp` | true | Источник данных SNMP, в частности использование OID |",
    'Learn more about Dynatrace Extensions [custom diagnostics.](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#diagnostics "Overview of all Dynatrace Extensions features to help you develop apps")': 'Подробнее о [пользовательской диагностике](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#diagnostics "Обзор всех функций Dynatrace Extensions для разработки приложений") Dynatrace Extensions.',
    "## Python environment": "## Среда Python",
    "The settings in this section allow you to customize the details of your virtual environment when working with Python extensions.": "Параметры этого раздела позволяют настроить виртуальную среду при работе с расширениями Python.",
    '| `dynatraceExtensions.pythonExtraPlatforms` | `[ "linux_x86_64", "win_amd64" ]` | A list of platforms to build Python packages for. |': '| `dynatraceExtensions.pythonExtraPlatforms` | `[ "linux_x86_64", "win_amd64" ]` | Список платформ для сборки пакетов Python. |',
    "| `dynatraceExtensions.pythonExtraPlatformsOnly` | false | When enabled, the `Dynatrace extensions: Build` command builds only for the platforms specified above. |": "| `dynatraceExtensions.pythonExtraPlatformsOnly` | false | При включении команда `Dynatrace extensions: Build` выполняет сборку только для платформ, указанных выше. |",
    "| `dynatraceExtensions.pythonBuildVersion` | `3.10 + 3.14` | Options are `3.10 + 3.14`, `3.10`, or `3.14`. Select `3.10` to roll back for EEC versions earlier than `1.333.x`. |": "| `dynatraceExtensions.pythonBuildVersion` | `3.10 + 3.14` | Возможные значения: `3.10 + 3.14`, `3.10` или `3.14`. Выберите `3.10` для отката к версиям EEC ранее `1.333.x`. |",
}

PASS = {
    "title: Settings",
    "# Settings",
}

if __name__ == "__main__":
    build_one(REL, "settings.md", TRANS, PASS)
    qa_one(REL, "settings.md")
