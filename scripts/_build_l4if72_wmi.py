# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/supported-extensions/data-sources/wmi.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/supported-extensions/data-sources"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Feb 01, 2022": "* Опубликовано 1 февраля 2022 г.",
    "Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly for WMI-monitored Windows services and components. To this end, Dynatrace offers the facility to bring WMI data into Dynatrace at scale and in the context to all other data. This works best if you have OneAgent on the monitored Windows box, but it also works in an agentless manner.": "Dynatrace предоставляет платформу для расширения наблюдаемости за данными, получаемыми непосредственно для служб и компонентов Windows, отслеживаемых через WMI. Это позволяет передавать данные WMI в Dynatrace в масштабе и в контексте всех остальных данных. Решение оптимально при наличии OneAgent на отслеживаемом Windows-хосте, однако работает и в безагентном режиме.",
    'First, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=wmi) to see if your technology is covered by an existing extension. If it isn\'t, you can build your own [Dynatrace WMI extension](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") to cover your Windows technology.': 'Сначала проверьте в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=wmi), охвачена ли ваша технология существующим расширением. Если нет, создайте собственное [расширение Dynatrace WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Узнайте, как создать расширение WMI с помощью платформы Extensions framework.") для вашей технологии Windows.',
    "## Before you begin": "## Перед началом работы",
    "1. Decide which of your Windows-based hosts will provide data for the extension.": "1. Определите, какие Windows-хосты будут предоставлять данные для расширения.",
    "2. WMI extensions can run locally on an OneAgent (recommended) or remotely on an ActiveGate.": "2. Расширения WMI могут выполняться локально на OneAgent (рекомендуется) или удалённо на ActiveGate.",
    '* When run locally on a Windows host, the extension will connect to the WMI interface automatically. Make sure Extension Execution Controller is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/managed/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.")': '* При локальном запуске на Windows-хосте расширение автоматически подключается к интерфейсу WMI. Убедитесь, что Extension Execution Controller включён на уровне среды или выбранного хоста. Подробнее см. в разделе [Extension Execution Controller](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Dynatrace Extensions.").',
    '* When monitored remotely, make sure your Windows-based ActiveGates belonging to the ActiveGate groups you designated for remote monitoring have remote permissions enabled. See [WMI data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") for more information.': '* При удалённом мониторинге убедитесь, что Windows-ActiveGate из назначенных групп ActiveGate имеют включённые удалённые разрешения. Подробнее см. в разделе [Источник данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Узнайте, как создать расширение WMI с помощью платформы Extensions framework.").',
    "## Manage WMI extensions": "## Управление расширениями WMI",
    "Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest WMI data into your Dynatrace environment.": "Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими с целью приёма данных WMI в среду Dynatrace.",
    "Required permission: **Change monitoring settings**": "Необходимое разрешение: **Change monitoring settings**",
    '1. In Dynatrace Hub, search for a WMI extension. You can use the "WMI" keyword to filter results.': '1. В Dynatrace Hub выполните поиск расширения WMI. Для фильтрации результатов используйте ключевое слово "WMI".',
    "2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.": "2. Выберите и установите нужное расширение. Это включает расширение в среде мониторинга.",
    "3. Add a monitoring configuration so that the extension can begin collecting data.": "3. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.",
    "Next, perform the following steps.": "Затем выполните следующие шаги.",
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    '**Define monitoring source**](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi#step-1 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")': '**Определение источника мониторинга**](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi#step-1 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик WMI.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")',
    '**Advanced properties**](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi#step-2 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': '**Дополнительные свойства**](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi#step-2 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик WMI.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
    '**Activate extension**](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi#step-3 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")': '**Активация расширения**](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi#step-3 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик WMI.")',
    "### Step 1 Define monitoring source": "### Шаг 1. Определение источника мониторинга",
    "#### Local monitoring": "#### Локальный мониторинг",
    '1. Select the host, host group or management zone for which you will run the extension, or choose to monitor the whole environment. The host needs to be running a OneAgent that is [enabled to run extensions](/managed/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").': '1. Выберите хост, группу хостов или зону управления, для которой будет запускаться расширение, или выберите мониторинг всей среды. На хосте должен быть запущен OneAgent, [настроенный для выполнения расширений](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Dynatrace Extensions.").',
    "2. Select **Next step**.": "2. Нажмите **Next step**.",
    "#### Remote monitoring": "#### Удалённый мониторинг",
    '1. Select **Monitor remotely** and choose the ActiveGate group to determine which ActiveGate or ActiveGates will run the extension. A Windows-based ActiveGate host needs to have remote permissions enabled. See [WMI data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") for more information': '1. Выберите **Monitor remotely** и укажите группу ActiveGate, чтобы определить, какой ActiveGate или ActiveGate будут запускать расширение. На Windows-хосте ActiveGate необходимо включить удалённые разрешения. Подробнее см. в разделе [Источник данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Узнайте, как создать расширение WMI с помощью платформы Extensions framework.").',
    "2. Select **Next step**.": "2. Нажмите **Next step**.",
    "3. Select **Add host** and provide connection details.": "3. Нажмите **Add host** и укажите сведения для подключения.",
    "* Host name or IP address": "* Имя хоста или IP-адрес",
    "* Username with permissions to access WMI data remotely": "* Имя пользователя с разрешениями на удалённый доступ к данным WMI",
    "* Password": "* Пароль",
    "You can add up to 100 hosts.": "Можно добавить до 100 хостов.",
    "Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them. When done, select **Next step**.": "Данные аутентификации, передаваемые в Dynatrace при активации конфигурации мониторинга, скрываются и не могут быть получены. После этого нажмите **Next step**.",
    "### Step 2 optional Advanced properties Optional": "### Шаг 2 (необязательно). Дополнительные свойства",
    "Some WMI extensions may require additional configuration. When done, select **Next step**": "Некоторые расширения WMI могут требовать дополнительной настройки. После этого нажмите **Next step**.",
    "### Step 3 Activate extension": "### Шаг 3. Активация расширения",
    "Provide final configuration details.": "Укажите финальные сведения о конфигурации.",
    "* **Description**": "* **Description**  ",
    "Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, it can give your teams details of this particular monitoring configuration.": "Текст с описанием данной конфигурации мониторинга. При устранении неполадок он поможет вашей команде получить подробные сведения о конкретной конфигурации.",
    "* **Feature sets**": "* **Feature sets**  ",
    "In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension": "В сильно сегментированных сетях наборы функций могут отражать сегменты среды. Их можно использовать для ограничения мониторинга определёнными сегментами. Наборы функций предопределены для каждого расширения.",
    "* **Variables**": "* **Variables**  ",
    "Some extensions offer variables with which you can pass custom strings to your extension and report them in the environment, for example, as your dimension. Some extensions contain the `ext.activationtag` variable that is passed as a dimension to your monitoring configuration. You can use it to associate the reported metrics with a particular version of your monitoring configuration.": "Некоторые расширения предлагают переменные, с помощью которых можно передавать пользовательские строки в расширение и отображать их в среде, например как измерение. Некоторые расширения содержат переменную `ext.activationtag`, которая передаётся в качестве измерения в конфигурацию мониторинга. Её можно использовать для связи отображаемых метрик с конкретной версией конфигурации мониторинга.",
    "When done, select **Activate**.": "После этого нажмите **Activate**.",
    "## Monitoring configuration as JSON": "## Конфигурация мониторинга в формате JSON",
    'The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") to learn how to use it to activate an extension using the Dynatrace API.': 'Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. О том, как использовать их для активации расширения через Dynatrace API, см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.").',
    "## Related topics": "## Связанные разделы",
    '* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")': '* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")',
}

PASS = {
    "title: Manage WMI extensions",
    "source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/wmi",
    "scraped: 2026-05-12T11:10:25.500038",
    "# Manage WMI extensions",
}

if __name__ == "__main__":
    build_one(REL, "wmi.md", TRANS, PASS)
    qa_one(REL, "wmi.md")
