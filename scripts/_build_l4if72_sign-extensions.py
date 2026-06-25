# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/develop-your-extensions/sign-extensions.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Updated on Apr 27, 2026": "* Обновлено 27 апреля 2026 г.",
    "Before uploading an extension to your Dynatrace environment, sign it to verify its authenticity. After signing, save the root certificate to a dedicated directory on each host running the extension, whether OneAgent or ActiveGate.": "Перед загрузкой расширения в окружение Dynatrace подпишите его для подтверждения подлинности. После подписания сохраните корневой сертификат в специальный каталог на каждом хосте, на котором выполняется расширение: OneAgent или ActiveGate.",
    "* In a development environment, each developer should have a unique leaf certificate. This ensures the traceability of changes.": "* В среде разработки каждый разработчик должен иметь уникальный листовой сертификат. Это обеспечивает прослеживаемость изменений.",
    "* In a production environment, each extension must be signed with its own leaf certificate. This guarantees the authenticity of each extension.": "* В производственной среде каждое расширение должно быть подписано собственным листовым сертификатом. Это гарантирует подлинность каждого расширения.",
    "## Sign your extension": "## Подписание расширения",
    "Depending on your needs, choose one of the following methods to sign and build your extension:": "В зависимости от потребностей выберите один из следующих методов для подписания и сборки расширения:",
    "* [`dt-extensions-sdk`](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/cli/sign.html) - an all-in-one CLI tool Recommended": "* [`dt-extensions-sdk`](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/cli/sign.html): универсальный инструмент командной строки. Рекомендуется",
    '* [VSCode Extension](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Introduction to the Dynatrace Extensions add-on for VS Code") - an all-in-one editor-based tool Recommended': '* [Расширение VSCode](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Введение в дополнение Dynatrace Extensions для VS Code"): универсальный инструмент на основе редактора. Рекомендуется',
    '* [Use OpenSSL](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl "Sign an extension manually with OpenSSL.") - a standard crypto library for manual control': '* [Использование OpenSSL](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl "Подпишите расширение вручную с помощью OpenSSL."): стандартная криптографическая библиотека для ручного управления',
    "Dynatrace CLI": "Dynatrace CLI",
    "You can also use the Dynatrace CLI (`dt-cli`) to sign your extension. Since its features are fully contained within `dt-extensions-sdk` CLI, only use it as a lighter alternative for CI/CD environments.": "Для подписания расширения также можно использовать Dynatrace CLI (`dt-cli`). Поскольку его функциональность полностью входит в состав CLI `dt-extensions-sdk`, применяйте его только как облегчённую альтернативу для сред CI/CD.",
    "Read more about [`dt-cli` on GitHub](https://github.com/dynatrace-oss/dt-cli).": "Подробнее о [`dt-cli` на GitHub](https://github.com/dynatrace-oss/dt-cli).",
    "## Upload your root certificate": "## Загрузка корневого сертификата",
    "Upload your root certificate to enhance the security of the Extensions framework.": "Загрузите корневой сертификат для повышения безопасности платформы Extensions.",
    "By doing this, you": "Это позволяет:",
    "* Verify the authenticity of distributed extensions.": "* проверять подлинность распространяемых расширений;",
    "* Prevent potential malicious extension distribution by an intruder who could take control of your environment.": "* предотвращать возможное распространение вредоносных расширений злоумышленником, получившим контроль над окружением.",
    "### Add certificate to the credential vault": "### Добавление сертификата в хранилище учётных данных",
    'Add your root certificate to the Dynatrace [credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault."). This is required before you can upload an extension ZIP file to your environment.': 'Добавьте корневой сертификат в [хранилище учётных данных](/managed/manage/credential-vault "Храните учётные данные и управляйте ими в хранилище учётных данных.") Dynatrace. Это необходимо сделать перед загрузкой ZIP-файла расширения в окружение.',
    "When adding the certificate, use the following settings:": "При добавлении сертификата используйте следующие настройки:",
    "* Credential type: `Public certificate`": "* Тип учётных данных: `Public certificate`",
    "* Credential scope: `Extension validation`": "* Область доступа учётных данных: `Extension validation`",
    'The [VS Code extension](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Introduction to the Dynatrace Extensions add-on for VS Code") does this automatically. If you work with multiple environments (for example, development and production), you must add the certificate to the credential vault of each environment separately.': 'Дополнение [VS Code](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Введение в дополнение Dynatrace Extensions для VS Code") выполняет это автоматически. При работе с несколькими окружениями (например, разработки и производства) необходимо добавить сертификат в хранилище учётных данных каждого окружения отдельно.',
    "For JMX extensions, adding the certificate to the credential vault is the only step required. You don't need to save the certificate to the host filesystem.": "Для расширений JMX достаточно добавить сертификат в хранилище учётных данных. Сохранять сертификат в файловой системе хоста не нужно.",
    "### Remote extensions": "### Удалённые расширения",
    "Upload your root certificate to each ActiveGate host within the ActiveGate group selected for running your extensions.": "Загрузите корневой сертификат на каждый хост ActiveGate в группе ActiveGate, выбранной для выполнения расширений.",
    "Save the `root.pem` certificate file in the following location:": "Сохраните файл сертификата `root.pem` в следующем расположении:",
    "* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/`": "* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/`",
    "* Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\certificates`": "* Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\certificates`",
    "### Local extensions": "### Локальные расширения",
    "Upload your root certificate to each OneAgent host or each OneAgent host within the host group selected for running your extensions.": "Загрузите корневой сертификат на каждый хост OneAgent или каждый хост OneAgent в группе хостов, выбранной для выполнения расширений.",
    "* Linux: `/var/lib/dynatrace/oneagent/agent/config/certificates`": "* Linux: `/var/lib/dynatrace/oneagent/agent/config/certificates`",
    "* Windows: `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config\\certificates`": "* Windows: `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config\\certificates`",
    "### Certificate file permissions": "### Права доступа к файлу сертификата",
    "For the Extension Execution Controller to read the certificate properly, ensure the certificate file has the correct permissions:": "Чтобы Extension Execution Controller мог правильно прочитать сертификат, убедитесь, что файл сертификата имеет корректные права доступа:",
    "Windows:": "Windows:",
    "* OneAgent: File should be accessible to `LOCAL_SYSTEM`": "* OneAgent: файл должен быть доступен для `LOCAL_SYSTEM`",
    "* ActiveGate: File should be accessible to `LOCAL_SERVICE`": "* ActiveGate: файл должен быть доступен для `LOCAL_SERVICE`",
    "Linux:": "Linux:",
    "* OneAgent: File should be accessible to `dtuser`": "* OneAgent: файл должен быть доступен для `dtuser`",
    "* ActiveGate: File should be accessible to `dtuserag`": "* ActiveGate: файл должен быть доступен для `dtuserag`",
    "## Upload a custom extension": "## Загрузка пользовательского расширения",
    "After signing your extension and uploading the root certificate, you can upload the custom extension to your Dynatrace environment.": "После подписания расширения и загрузки корневого сертификата можно загрузить пользовательское расширение в окружение Dynatrace.",
    "### Troubleshoot permission errors": "### Устранение ошибок прав доступа",
    "If you encounter any permission errors when accessing the certificate file (for example, `Error opening file /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem : Permission denied`):": "При возникновении ошибок прав доступа при обращении к файлу сертификата (например, `Error opening file /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem : Permission denied`):",
    "1. Check the file permissions:": "1. Проверьте права доступа к файлу:",
    "* Linux:": "* Linux:",
    "+ OneAgent: `ls -l /var/lib/dynatrace/oneagent/agent/config/certificates/root.pem`": "+ OneAgent: `ls -l /var/lib/dynatrace/oneagent/agent/config/certificates/root.pem`",
    "+ ActiveGate: `ls -l /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem`": "+ ActiveGate: `ls -l /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem`",
    "* Windows: Open the file properties and go to the **Security** tab.": "* Windows: откройте свойства файла и перейдите на вкладку **Security**.",
    "2. Verify the permissions match those described in [Certificate file permissions](#certificate-file-permissions).": "2. Убедитесь, что права доступа соответствуют описанным в разделе [Права доступа к файлу сертификата](#certificate-file-permissions).",
    '3. After correcting the file permissions, [restart the Extension Execution Controller](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration#restart-eec "Configure the Extension Execution Controller (EEC).") if the extension continues to fail.': '3. После исправления прав доступа к файлу [перезапустите Extension Execution Controller](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration#restart-eec "Настройте Extension Execution Controller (EEC)."), если расширение по-прежнему не работает.',
}

PASS = {
    "title: Sign extensions",
    "# Sign extensions",
}

if __name__ == "__main__":
    build_one(REL, "sign-extensions.md", TRANS, PASS)
    qa_one(REL, "sign-extensions.md")
