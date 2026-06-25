# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/sign-extensions"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Apr 21, 2021": "* Опубликовано 21 апреля 2021 г.",
    "## Use OpenSSL": "## Использование OpenSSL",
    "To sign your extension manually, use OpenSSL. For Windows, you need to download and install an [OpenSSL binary](https://wiki.openssl.org/index.php/Binaries) of your choice. We tested the procedure with OpenSSL 1.1.1k.": "Для подписания расширения вручную используйте OpenSSL. Для Windows необходимо загрузить и установить [бинарный файл OpenSSL](https://wiki.openssl.org/index.php/Binaries) по выбору. Процедура проверена с OpenSSL 1.1.1k.",
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")',
    '**Create the root key and certificate**](#create-root-key-and-cert)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': '**Создание корневого ключа и сертификата**](#create-root-key-and-cert)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")',
    '**Add your root certificate to the Dynatrace credential vault**](#add-root-cert)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': '**Добавление корневого сертификата в хранилище учётных данных Dynatrace**](#add-root-cert)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")',
    '**Create a developer certificate**](#create-dev-cert)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")': '**Создание разработческого сертификата**](#create-dev-cert)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")',
    '**Sign your extension**](#sign-extension)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")': '**Подписание расширения**](#sign-extension)[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")',
    '**Verify signature**](#verify-signature)[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")': '**Проверка подписи**](#verify-signature)[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")',
    "**Create extension package**](#create-extension-package)": "**Создание пакета расширения**](#create-extension-package)",
    "### Create the root key and certificate": "### Создание корневого ключа и сертификата",
    "Your company should issue developer certificates from a company-wide root certificate. When developers sign their extensions with their own developer certificates, Dynatrace will be able to verify the extension authenticity against your root certificate stored in the Dynatrace credential vault and on the hosts where extensions are executed.": "Компания должна выпускать разработческие сертификаты на основе общекорпоративного корневого сертификата. Когда разработчики подписывают расширения собственными разработческими сертификатами, Dynatrace может проверить подлинность расширения по корневому сертификату, хранящемуся в хранилище учётных данных Dynatrace и на хостах, где выполняются расширения.",
    "Run the following commands to generate your organization's root certificate. Do not set the password. Password-protected certificates are not supported by Dynatrace.": "Выполните следующие команды для создания корневого сертификата организации. Не задавайте пароль. Dynatrace не поддерживает сертификаты, защищённые паролем.",
    "When generating the root certificate, you need to explicitly define the certificate extension by pointing the `-extfile` property to the `ca.txt` file. The file should contain the following data:": "При создании корневого сертификата необходимо явно определить расширение сертификата, указав свойство `-extfile` на файл `ca.txt`. Файл должен содержать следующие данные:",
    "This generates your `root.pem` root certificate.": "В результате создаётся корневой сертификат `root.pem`.",
    "Note that you can also use an existing root certificate to generate developer certificates. Dynatrace accepts only PFX, P12, and PEM formats, so you may need to convert the existing certificate to one of the allowed formats. Refer to the OpenSSL documentation for conversion instructions.": "Обратите внимание, что для создания разработческих сертификатов можно также использовать существующий корневой сертификат. Dynatrace принимает только форматы PFX, P12 и PEM, поэтому может потребоваться преобразование существующего сертификата в один из допустимых форматов. Инструкции по преобразованию см. в документации OpenSSL.",
    "### Add your root certificate to the Dynatrace credential vault": "### Добавление корневого сертификата в хранилище учётных данных Dynatrace",
    "1. Go to **Credential Vault**.": "1. Откройте **Credential Vault**.",
    "2. Select **Add new credential**.": "2. Выберите **Add new credential**.",
    "3. For **Credential type**, select **Public Certificate**.": "3. В поле **Credential type** выберите **Public Certificate**.",
    "4. Select the **Extension validation** credential scope.": "4. Выберите область доступа учётных данных **Extension validation**.",
    "5. Add a meaningful **Credential name**.": "5. Введите понятное **Credential name**.",
    "6. Upload the **Root certificate file**.": "6. Загрузите **Root certificate file**.",
    "7. Select **Save**.": "7. Нажмите **Save**.",
    "### Create a developer certificate": "### Создание разработческого сертификата",
    "To create your developer certificate, you need to create a developer certificate signing request and then issue the certificate.": "Для создания разработческого сертификата необходимо сформировать запрос на подпись разработческого сертификата, а затем выпустить сертификат.",
    "#### Create a developer certificate signing request": "#### Создание запроса на подпись разработческого сертификата",
    "Run the following commands to generate the certificate signing request (CSR) to the root CA:": "Выполните следующие команды для создания запроса на подпись сертификата (CSR) к корневому удостоверяющему центру:",
    "When filling in the fields for the Distinguished Name (DN), make sure that at least one of the fields is different than the DN you defined for the root certificate.": "При заполнении полей Отличительного имени (DN) убедитесь, что хотя бы одно поле отличается от DN, заданного для корневого сертификата.",
    "The result is the `developer.csr` CSR that you'll use to issue the developer certificate from the root certificate.": "В результате создаётся CSR `developer.csr`, который используется для выпуска разработческого сертификата на основе корневого сертификата.",
    "#### Issue a developer certificate": "#### Выпуск разработческого сертификата",
    "Run the following commands to generate the developer certificate:": "Выполните следующие команды для создания разработческого сертификата:",
    "When generating the developer certificate, you need to explicitly define the certificate extension by pointing the `-extfile` property to the `developer.txt` file. The file should contain the following data:": "При создании разработческого сертификата необходимо явно определить расширение сертификата, указав свойство `-extfile` на файл `developer.txt`. Файл должен содержать следующие данные:",
    "The result is the `developer.pem` certificate file that you'll use for signing your extensions.": "В результате создаётся файл сертификата `developer.pem`, который используется для подписания расширений.",
    "### Sign your extension": "### Подписание расширения",
    "With the developer certificate in place, use the following command to sign your extension. Make sure that your `extension.zip` file is in the directory from which you run the command.": "Имея разработческий сертификат, используйте следующую команду для подписания расширения. Убедитесь, что файл `extension.zip` находится в каталоге, из которого выполняется команда.",
    "The result is an `extension.zip.sig` signature file.": "В результате создаётся файл подписи `extension.zip.sig`.",
    "### Verify signature": "### Проверка подписи",
    "Use the following command to verify the `extension.zip.sig` signature file against the `root.pem` root certificate:": "Используйте следующую команду для проверки файла подписи `extension.zip.sig` по корневому сертификату `root.pem`:",
    "Linux": "Linux",
    "Windows": "Windows",
    "The output should contain the phrase `Verification successful`.": "Вывод должен содержать фразу `Verification successful`.",
    "### Create extension package": "### Создание пакета расширения",
    'For the final step, create an [extension package](/managed/ingest-from/extensions/concepts#package "Learn more about the concept of Dynatrace Extensions.") containing only the `extension.zip` archive and the `extension.zip.sig` signature file.': 'На завершающем этапе создайте [пакет расширения](/managed/ingest-from/extensions/concepts#package "Подробнее о концепции Dynatrace Extensions."), содержащий только архив `extension.zip` и файл подписи `extension.zip.sig`.',
    'You can now upload the extension package to your Dynatrace environment. For more information, see [Manage Extensions](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': 'Теперь можно загрузить пакет расширения в окружение Dynatrace. Дополнительные сведения см. в разделе [Управление расширениями](/managed/upgrade/unavailable-in-managed "Выбранный вами раздел недоступен в Dynatrace Managed.").',
}

PASS = {
    "title: Sign extensions manually with OpenSSL",
    "# Sign extensions manually with OpenSSL",
}

if __name__ == "__main__":
    build_one(REL, "manually-openssl.md", TRANS, PASS)
    qa_one(REL, "manually-openssl.md")
