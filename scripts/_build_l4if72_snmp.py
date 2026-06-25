# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/supported-extensions/data-sources/snmp.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/supported-extensions/data-sources"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on May 08, 2023": "* Обновлено 8 мая 2023 г.",
    "Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP-monitored devices. To this end, Dynatrace enables you to bring SNMP data into Dynatrace at scale and within the context of all other data.": "Dynatrace предоставляет платформу для расширения наблюдаемости за данными, получаемыми непосредственно с устройств, которые отслеживаются через SNMP. Это позволяет передавать данные SNMP в Dynatrace в масштабе и в контексте всех остальных данных.",
    "You can also extend your insights into data related to SNMP traps issued in your infrastructure.": "Также доступно расширение аналитики данными, связанными с SNMP-ловушками, поступающими из вашей инфраструктуры.",
    'First, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=snmp) to see if your device is covered by an existing extension. If it isn\'t, you can build your own [Dynatrace SNMP extension](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.") to cover your SNMP device.': 'Сначала проверьте в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=snmp), охвачено ли ваше устройство существующим расширением. Если нет, создайте собственное [расширение Dynatrace SNMP](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Узнайте, как создать расширение SNMP с помощью платформы Extensions framework.") для вашего устройства.',
    "## Before you begin": "## Перед началом работы",
    "1. Decide which SNMP will provide data for the extension. Dynatrace Extensions framework supports SNMP v2c and v3. Depending on the SNMP version, prepare the necessary authentication details.": "1. Определите, какой источник SNMP будет предоставлять данные для расширения. Платформа Dynatrace Extensions framework поддерживает SNMP v2c и v3. В зависимости от версии SNMP подготовьте необходимые данные аутентификации.",
    "2. Designate an ActiveGate group or groups that will remotely connect to your SNMP devices to pull data. All ActiveGates in each designated group need to be able to connect to your SNMP devices.": "2. Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к устройствам SNMP для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключаться к вашим устройствам SNMP.",
    '3. Learn [hardware requirements](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#hw "Learn how to create an SNMP extension using the Extensions framework.") for an ActiveGate performing SNMP monitoring.': '3. Изучите [требования к оборудованию](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#hw "Узнайте, как создать расширение SNMP с помощью платформы Extensions framework.") для ActiveGate, выполняющего мониторинг SNMP.',
    "## Manage SNMP extensions": "## Управление расширениями SNMP",
    "Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest SNMP data into your Dynatrace environment.": "Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими с целью приёма данных SNMP в среду Dynatrace.",
    "Required permission: **Change monitoring settings**": "Необходимое разрешение: **Change monitoring settings**",
    '1. In Dynatrace Hub, search for "snmp" to find an SNMP or SNMP traps extension.': '1. В Dynatrace Hub выполните поиск по запросу "snmp", чтобы найти расширение SNMP или SNMP traps.',
    "2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.": "2. Выберите и установите нужное расширение. Это включает расширение в среде мониторинга.",
    "3. Add a monitoring configuration so that the extension can begin collecting data.": "3. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.",
    "Next, perform the following steps.": "Затем выполните следующие шаги.",
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    '**ActiveGate group**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-1 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': '**Группа ActiveGate**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-1 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик и событий SNMP.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    '**Define devices**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-2 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")': '**Определение устройств**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-2 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик и событий SNMP.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")',
    '**Advanced properties**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-3 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")': '**Дополнительные свойства**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-3 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик и событий SNMP.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")',
    '**Activate extension**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-4 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")': '**Активация расширения**](/managed/ingest-from/extensions/supported-extensions/data-sources/snmp#step-4 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик и событий SNMP.")',
    "### Step 1 ActiveGate group": "### Шаг 1. Группа ActiveGate",
    "Select the ActiveGate group to determine which ActivGates will run the extension. When done, select **Next step**.": "Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение. После этого нажмите **Next step**.",
    "### Step 2 Define devices": "### Шаг 2. Определение устройств",
    "Select **Add device** to define the devices from which you want to pull data and provide the device connection details:": "Нажмите **Add device**, чтобы определить устройства, с которых нужно получать данные, и укажите сведения для подключения к устройству:",
    "* IP address or device name": "* IP-адрес или имя устройства",
    "* Port": "* Порт",
    "* SNMP version and related authentication details. Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.": "* Версия SNMP и соответствующие данные аутентификации. Данные аутентификации, передаваемые в Dynatrace при активации конфигурации мониторинга, скрываются и не могут быть получены.",
    "### Step 3 optional Advanced properties Optional": "### Шаг 3 (необязательно). Дополнительные свойства",
    "SNMP extensions only": "Только для расширений SNMP",
    "Select **Define** to configure optional advanced properties:": "Нажмите **Define**, чтобы настроить необязательные дополнительные свойства:",
    "* **Timeout in seconds**": "* **Timeout in seconds**  ",
    "The maximum time (in seconds) to wait for an SNMP query to return data. Default = `2` seconds.": "Максимальное время ожидания (в секундах) ответа на запрос SNMP. Значение по умолчанию: `2` секунды.",
    "* **Retries**": "* **Retries**  ",
    "The maximum number of retries for a query if it fails (total time for a query is `timeoutSecs` x `retries`). Default = `3` retries.": "Максимальное количество повторных попыток выполнения запроса в случае сбоя (общее время для одного запроса: `timeoutSecs` x `retries`). Значение по умолчанию: `3` попытки.",
    "* **Max repetitions**": "* **Max repetitions**  ",
    "Can be used to limit the amount of data returned for a single query and might in turn increase the number of requests sent to the device until all required data is collected. Default = `50` repetitions.": "Позволяет ограничить объём данных, возвращаемых за один запрос, что может привести к увеличению количества запросов к устройству до сбора всех необходимых данных. Значение по умолчанию: `50` повторений.",
    "* **Max OIDs per query**": "* **Max OIDs per query**  ",
    "Number of OIDs that can be queried in one SNMP request. Default = `60` OIDs. For most extensions, you don't need to change it. For the [F5 BIG-IP LTMï»¿](https://dt-url.net/jl036z9) extension, we recommend that you set it to `5`.": "Количество OID, которые можно запросить в одном запросе SNMP. Значение по умолчанию: `60` OID. Для большинства расширений изменение этого значения не требуется. Для расширения [F5 BIG-IP LTM](https://dt-url.net/jl036z9) рекомендуется установить значение `5`.",
    "* **Enable unconnected UDP**": "* **Enable unconnected UDP**",
    "When enabled, the UDP socket becomes unconnected. This allows it to accept responses from a different address than the one the request was sent to, or to ignore ICMP packets. Default value is `false`.": "При включении UDP-сокет переходит в несвязанный режим. Это позволяет принимать ответы с адреса, отличного от адреса назначения запроса, или игнорировать пакеты ICMP. Значение по умолчанию: `false`.",
    "SNMP Traps extensions only": "Только для расширений SNMP Traps",
    "Select **Add varbinding rule** to configure variable binding trimming:": "Нажмите **Add varbinding rule**, чтобы настроить усечение привязки переменных:",
    "* **Variable binding (OID) prefix**": "* **Variable binding (OID) prefix**  ",
    "The part of the OID that is matched for trimming.": "Часть OID, сопоставляемая для усечения.",
    "* **Number of octets trimmed**": "* **Number of octets trimmed**  ",
    "The number of octets at the end of the OID that you want to trim.": "Количество октетов в конце OID, которые нужно усечь.",
    "When done, select **Next step**": "После этого нажмите **Next step**.",
    "### Step 4 Activate extension": "### Шаг 4. Активация расширения",
    "Provide final configuration details.": "Укажите финальные сведения о конфигурации.",
    "* **Description**": "* **Description**  ",
    "Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.": "Текст с описанием данной конфигурации мониторинга. При устранении неполадок он поможет вашей команде получить подробные сведения о конкретной конфигурации.",
    "* **Feature sets**": "* **Feature sets**  ",
    "In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension. For SNMP traps extensions, select the **Events** feature set to enable the forwarding of trap messages as log events.": "В сильно сегментированных сетях наборы функций могут отражать сегменты среды. Их можно использовать для ограничения мониторинга определёнными сегментами. Наборы функций предопределены для каждого расширения. Для расширений SNMP traps выберите набор функций **Events**, чтобы включить пересылку сообщений-ловушек в виде событий журнала.",
    "* **Variables**": "* **Variables**  ",
    "Some extensions offer variables with which you can pass custom strings to your extension and report them in the environment, for example, as your dimension. Some extensions contain the `ext.activationtag` variable that is passed as a dimension to your monitoring configuration. You can use it to associate the reported metrics with a particular version of your monitoring configuration.": "Некоторые расширения предлагают переменные, с помощью которых можно передавать пользовательские строки в расширение и отображать их в среде, например как измерение. Некоторые расширения содержат переменную `ext.activationtag`, которая передаётся в качестве измерения в конфигурацию мониторинга. Её можно использовать для связи отображаемых метрик с конкретной версией конфигурации мониторинга.",
    "When done, select **Activate**.": "После этого нажмите **Activate**.",
    "## Monitoring configuration as JSON": "## Конфигурация мониторинга в формате JSON",
    'The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") to learn how to use it to activate an extension using the Dynatrace API.': 'Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. О том, как использовать их для активации расширения через Dynatrace API, см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.").',
    "## Custom MIB files": "## Пользовательские файлы MIB",
    "Management Information Base (MIB) is the database managing the entities in a network identified by OIDs. MIB provides a source of additional information related to OIDs declared in your extension.": "Management Information Base (MIB): база данных, управляющая сетевыми объектами, идентифицируемыми по OID. MIB служит источником дополнительной информации об OID, объявленных в расширении.",
    "ActiveGate comes with a default set of MIB files. If some of the OIDs used in your custom SNMP extension are not available in the default MIB files, you can add your own MIB file to the ActiveGate running the extension.": "ActiveGate поставляется с набором MIB-файлов по умолчанию. Если некоторые OID, используемые в пользовательском расширении SNMP, отсутствуют в файлах MIB по умолчанию, добавьте собственный MIB-файл в ActiveGate, на котором выполняется расширение.",
    "Custom MIB files are only applicable when you build your own SNMP extension. Dynatrace out-of-the-box SNMP extensions come with a predefined set of OIDs and do not dynamically load additional MIB files placed in the `mib-files-custom` directory.": "Пользовательские MIB-файлы применимы только при создании собственного расширения SNMP. Готовые расширения SNMP от Dynatrace содержат предопределённый набор OID и не загружают дополнительные MIB-файлы, помещённые в каталог `mib-files-custom`.",
    "When you create a custom SNMP or SNMP traps extension, the MIB files located in the `mib-files-custom` directory will be used by all such custom extensions running on the ActiveGate.": "При создании пользовательского расширения SNMP или SNMP traps MIB-файлы из каталога `mib-files-custom` будут использоваться всеми такими пользовательскими расширениями, работающими на ActiveGate.",
    "Place your custom MIB files in the `mib-files-custom` directory:": "Поместите пользовательские MIB-файлы в каталог `mib-files-custom`:",
    "* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/mib-files-custom/`": "* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/mib-files-custom/`",
    "* Windows: `C:\\%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata\\mib-files-custom\\`": "* Windows: `C:\\%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata\\mib-files-custom\\`",
    "The files stored in the `mib-files-custom` directory are preserved between updates.": "Файлы, хранящиеся в каталоге `mib-files-custom`, сохраняются между обновлениями.",
    "## Related topics": "## Связанные разделы",
    '* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")': '* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")',
}

PASS = {
    "title: Manage SNMP extensions",
    "source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/snmp",
    "scraped: 2026-05-12T11:10:19.929800",
    "# Manage SNMP extensions",
}

if __name__ == "__main__":
    build_one(REL, "snmp.md", TRANS, PASS)
    qa_one(REL, "snmp.md")
