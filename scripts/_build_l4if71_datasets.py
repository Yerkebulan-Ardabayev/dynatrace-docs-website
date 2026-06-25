# -*- coding: utf-8 -*-
"""Builder for download-zos-datasets.md (L4-IF.71 canon)."""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer"
FN = "download-zos-datasets.md"

TRANS = {
    # frontmatter
    "title: Download z/OS product datasets": "title: Загрузка наборов данных продукта z/OS",
    # h1 (appears twice — same key, same value)
    "# Download z/OS product datasets": "# Загрузка наборов данных продукта z/OS",
    # metadata
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Nov 03, 2023": "* Обновлено 3 ноября 2023 г.",
    # intro paragraph
    "You can download the PAX file containing the CICS, IMS, z/OS Java, and zDC modules in two ways:": "PAX-файл, содержащий модули CICS, IMS, z/OS Java и zDC, можно загрузить двумя способами:",
    "* Dynatrace version 1.272+ Download via [Deployment API](#using-deploymentapi).": "* Dynatrace версии 1.272+: загрузка через [Deployment API](#using-deploymentapi).",
    "* Dynatrace version 1.276+ Download via [web UI](#using-webui).": "* Dynatrace версии 1.276+: загрузка через [веб-интерфейс](#using-webui).",
    "Starting with OneAgent release 1.275, the PAX file is no longer published on our FTP server.": "Начиная с версии OneAgent 1.275, PAX-файл больше не публикуется на FTP-сервере.",
    # ## Download the PAX file
    "## Download the PAX file": "## Загрузка PAX-файла",
    'You can download the latest or a specific PAX file version via web UI or the [Deployment API](/managed/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.") of OneAgent.': 'Можно загрузить последнюю или конкретную версию PAX-файла через веб-интерфейс или [Deployment API](/managed/dynatrace-api/environment-api/deployment/oneagent "Загрузка установщиков OneAgent через Dynatrace API.") OneAgent.',
    "The PAX file version must be less than or equal to the zRemote module version.": "Версия PAX-файла должна быть меньше или равна версии модуля zRemote.",
    # ### Download latest version via web UI
    "### Download latest version via web UI": "### Загрузка последней версии через веб-интерфейс",
    "1. Go to **Deploy Dynatrace** and select **Start installation**.": "1. Перейдите в **Deploy Dynatrace** и выберите **Start installation**.",
    "2. Select **z/OS** and **Download z/OS product datasets** to download the latest PAX file version.": "2. Выберите **z/OS** и **Download z/OS product datasets** для загрузки последней версии PAX-файла.",
    "The file name `dynatrace-zos-1.nnn.m.pax` includes the major release version `nnn` and minor version `m`.": "Имя файла `dynatrace-zos-1.nnn.m.pax` содержит номер основного выпуска `nnn` и номер дополнительного выпуска `m`.",
    # ### Download a specific version via web UI
    "### Download a specific version via web UI": "### Загрузка конкретной версии через веб-интерфейс",
    "You can download a specific PAX file version via web UI as follows:": "Конкретную версию PAX-файла можно загрузить через веб-интерфейс следующим образом:",
    "1. Go to **Settings** > **Monitoring** > **Monitoring overview**.": "1. Перейдите в **Settings** > **Monitoring** > **Monitoring overview**.",
    "2. Select **Download Dynatrace OneAgent or ActiveGate installer** and define your preferred version:": "2. Выберите **Download Dynatrace OneAgent or ActiveGate installer** и укажите нужную версию:",
    "1. Installer: `OneAgent - z/OS`": "1. Installer: `OneAgent - z/OS`",
    "2. Build: Select your preferred major version": "2. Build: выберите нужный основной выпуск",
    "3. Revision: Select your preferred minor version": "3. Revision: выберите нужный дополнительный выпуск",
    "![zos monitoring overview](https://dt-cdn.net/images/zos-monitoring-overview-1289-aa537f3578.png)": "![zos monitoring overview](https://dt-cdn.net/images/zos-monitoring-overview-1289-aa537f3578.png)",
    "zos monitoring overview": "zos monitoring overview",
    "3. Select **Continue** and **Download z/OS product datasets** to download your defined PAX file version.": "3. Нажмите **Continue** и **Download z/OS product datasets** для загрузки выбранной версии PAX-файла.",
    # ### Download latest version via Deployment API
    "### Download latest version via Deployment API": "### Загрузка последней версии через Deployment API",
    "You can download the latest PAX file version via Deployment API as follows:": "Последнюю версию PAX-файла можно загрузить через Deployment API следующим образом:",
    '1. Generate an [Access token](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the scope **PaaS integration - Installer download** (`InstallerDownload`).': '1. Создайте [токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для работы с Dynatrace API.") с областью видимости **PaaS integration - Installer download** (`InstallerDownload`).',
    '2. Download the latest PAX file via [Deployment API - Download latest OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API."):': '2. Загрузите последний PAX-файл через [Deployment API - Download latest OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузка последней версии установщика OneAgent через Dynatrace API."):',
    "| HTTP method | Dynatrace environment | Endpoint |": "| Метод HTTP | Окружение Dynatrace | Эндпоинт |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest` |": "| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest` |",
    "| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/latest` |": "| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/latest` |",
    "Below is a sample `curl` command for a SaaS environment that uses the Deployment API to download the latest PAX file version:": "Ниже приведён пример команды `curl` для окружения SaaS, загружающей последнюю версию PAX-файла через Deployment API:",
    "Replace `<environment>` with your Dynatrace environment ID and `<accessToken>` with your generated access token.": "Замените `<environment>` на идентификатор вашего окружения Dynatrace, а `<accessToken>` на сгенерированный токен доступа.",
    # ### Download a specific version via Deployment API
    "### Download a specific version via Deployment API": "### Загрузка конкретной версии через Deployment API",
    "You can download a specific PAX file version via Deployment API as follows:": "Конкретную версию PAX-файла можно загрузить через Deployment API следующим образом:",
    '2. List all available PAX file versions via [Deployment API - List available versions of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.").': '2. Получите список всех доступных версий PAX-файла через [Deployment API - List available versions of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "Получение списка доступных версий OneAgent через Dynatrace API.").',
    "| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe` |": "| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe` |",
    "| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/zos/mainframe` |": "| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/zos/mainframe` |",
    "Below is a sample `curl` command for a SaaS environment that uses the Deployment API to list all available PAX file versions:": "Ниже приведён пример команды `curl` для окружения SaaS, получающей список всех доступных версий PAX-файла через Deployment API:",
    "Replace `<environment>` with your Dynatrace environment ID and `<accessToken>` with your generated access token.": "Замените `<environment>` на идентификатор вашего окружения Dynatrace, а `<accessToken>` на сгенерированный токен доступа.",
    '3. Download a specific PAX file version via [Deployment API - Download OneAgent of specific version](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version "Download the OneAgent installer of the specific version via Dynatrace API."):': '3. Загрузите конкретную версию PAX-файла через [Deployment API - Download OneAgent of specific version](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version "Загрузка установщика OneAgent конкретной версии через Dynatrace API."):',
    "| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/{version}` |": "| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/{version}` |",
    "| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/version/{version}` |": "| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/version/{version}` |",
    "Below is a sample `curl` command for a SaaS environment that uses the Deployment API to download a specific PAX file version:": "Ниже приведён пример команды `curl` для окружения SaaS, загружающей конкретную версию PAX-файла через Deployment API:",
    "Replace `<environment>` with your Dynatrace environment ID, `<version>` with your selected PAX file version, and `<accessToken>` with your generated access token.": "Замените `<environment>` на идентификатор вашего окружения Dynatrace, `<version>` на выбранную версию PAX-файла, а `<accessToken>` на сгенерированный токен доступа.",
    # ## Extract product datasets
    "## Extract product datasets": "## Извлечение наборов данных продукта",
    "You can extract the product datasets from the PAX file as follows:": "Наборы данных продукта можно извлечь из PAX-файла следующим образом:",
    "1. Transfer the PAX file to your z/OS USS directory in binary mode.": "1. Передайте PAX-файл в каталог z/OS USS в двоичном режиме.",
    "2. Rename the PAX file from `dynatrace-zos-1.nnn.m.pax` to `dynatrace-zos.pax`.": "2. Переименуйте PAX-файл из `dynatrace-zos-1.nnn.m.pax` в `dynatrace-zos.pax`.",
    "3. Use the `EXTRACT` job below to extract the product datasets from the installation files. Before running the job, modify the following:": "3. Используйте задание `EXTRACT`, приведённое ниже, для извлечения наборов данных продукта из файлов установки. Перед запуском задания внесите следующие изменения:",
    "1. Determine the desired high-level qualifier for the install dataset names and set the `HLQ` variable accordingly.": "1. Определите нужный высокоуровневый квалификатор для имён наборов данных установки и задайте переменную `HLQ` соответствующим образом.",
    "2. Set `MYUSS` to the z/OS USS directory path where you placed the `dynatrace-zos.pax` file. If the directory path exceeds 42 characters, it might result in an error in the `STEP3` of the job. In such case, you need to modify the JCL to accommodate the continuation character.": "2. Задайте переменной `MYUSS` путь к каталогу z/OS USS, в который помещён файл `dynatrace-zos.pax`. Если путь к каталогу превышает 42 символа, это может привести к ошибке в шаге `STEP3` задания. В таком случае нужно изменить JCL для использования символа продолжения.",
    "3. Change the volume serial number `VOLSER` to match site standards.": "3. Измените серийный номер тома `VOLSER` в соответствии со стандартами вашего предприятия.",
    "EXTRACT job": "Задание EXTRACT",
    "If the job ends with a return code of `0`, the extraction was successful.": "Если задание завершается с кодом возврата `0`, извлечение прошло успешно.",
    "Optional Delete `dynatrace-zos.pax` and `dynatrace-oneagent-zos-java.jar` (if it is not needed) to free up disk space.": "Необязательно: удалите `dynatrace-zos.pax` и `dynatrace-oneagent-zos-java.jar` (если они не нужны), чтобы освободить дисковое пространство.",
    # ### Product datasets
    "### Product datasets": "### Наборы данных продукта",
    "The extraction process creates the following product datasets (the names are provided for the default high-level qualifier and the `R1nnnx` release version):": "В результате извлечения создаются следующие наборы данных продукта (имена приведены для высокоуровневого квалификатора по умолчанию и версии выпуска `R1nnnx`):",
    "* `DT.R1nnnx.SZDTAUTH`: Contains the zDC subsystem and the IMS module including IMS Connect": "* `DT.R1nnnx.SZDTAUTH`: содержит подсистему zDC и модуль IMS, включая IMS Connect",
    "* `DT.R1nnnx.SZDTLOAD`: Contains the CICS module": "* `DT.R1nnnx.SZDTLOAD`: содержит модуль CICS",
    "* `DT.R1nnnx.SZDTSAMP`: Includes sample JCL and CICS RDO definitions": "* `DT.R1nnnx.SZDTSAMP`: содержит образцы JCL и определения CICS RDO",
    "Disk space usage of the product datasets": "Использование дискового пространства наборами данных продукта",
    "On average, the product datasets and installation files in the z/OS USS directory use the following disk space:": "В среднем наборы данных продукта и файлы установки в каталоге z/OS USS занимают следующий объём дискового пространства:",
    # ### Define aliases
    "### Define aliases": "### Определение псевдонимов",
    "We recommend defining an `ALIAS` without the version number for the product datasets. Use these `ALIAS` in the zDC, CICS, and IMS module injection jobs. You can then perform maintenance without updating the jobs.": "Рекомендуется определять псевдоним `ALIAS` без номера версии для наборов данных продукта. Используйте эти `ALIAS` в заданиях внедрения модулей zDC, CICS и IMS. Это позволит выполнять техническое обслуживание без обновления заданий.",
    "For example:": "Например:",
}

# Lines that must remain verbatim EN:
# - dataset names, member names, JCL labels, inline code with version tokens
PASS = set()

if __name__ == "__main__":
    build_one(REL, FN, TRANS, PASS)
    qa_one(REL, FN)
