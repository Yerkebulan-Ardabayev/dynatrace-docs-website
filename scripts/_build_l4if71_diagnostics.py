# -*- coding: utf-8 -*-
"""Builder for oneagent-diagnostics.md (L4-IF.71 canon)."""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/dynatrace-oneagent/oneagent-troubleshooting"
FN = "oneagent-diagnostics.md"

# Mojibake note: EN source has UTF-8 bytes read as latin-1.
# U+2026 ELLIPSIS  = â\x80¦  (bytes e2 80 a6)
# U+2019 RIGHT '   = â\x80\x99  (bytes e2 80 99)
# Keys below use the mojibake form exactly as norm() sees them.

TRANS = {
    # frontmatter
    "title: OneAgent diagnostics": "title: Диагностика OneAgent",
    # h1 (appears twice — same key, same value)
    "# OneAgent diagnostics": "# Диагностика OneAgent",
    # metadata
    "* 7-min read": "* Чтение: 7 мин",
    "* Published Oct 22, 2020": "* Опубликовано 22 октября 2020 г.",
    # intro
    "You can run fully automated OneAgent troubleshooting for Dynatrace SaaS and Managed environments starting with Dynatrace version 1.208.": "Полностью автоматизированное устранение неполадок OneAgent доступно для окружений Dynatrace SaaS и Managed начиная с версии Dynatrace 1.208.",
    "The workflow enables you to:": "Рабочий процесс позволяет:",
    "* Automatically pinpoint a OneAgent-related issue in highly dynamic environments, at a specific point in time": "* Автоматически выявлять связанные с OneAgent проблемы в высокодинамичных окружениях в конкретный момент времени",
    "* Easily collect the diagnostic data for a specific entity, and automatically get potential solutions for detected anomalies": "* Легко собирать диагностические данные для конкретной сущности и автоматически получать возможные решения для обнаруженных аномалий",
    "* Quickly resolve common issues on your own, reducing the amount of time spent on diagnosing": "* Быстро самостоятельно устранять типичные проблемы, сокращая время диагностики",
    "* Directly provide Dynatrace Support all the details they need to diagnose the issue": "* Напрямую передавать в Dynatrace Support все необходимые для диагностики подробности",
    # callout
    "Command-line diagnostics": "Диагностика через командную строку",
    'If you don\'t have access to Dynatrace or you would like to script diagnostic data collection, you can use the `oneagentctl` command to collect a subset of full diagnostics data right on the host where OneAgent is installed. For more information, see [Create support archive](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#create-support-archive "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").': 'Если доступ к Dynatrace отсутствует или нужно автоматизировать сбор диагностических данных, используйте команду `oneagentctl` для сбора подмножества полных диагностических данных прямо на хосте, где установлен OneAgent. Подробнее см. раздел [Создать архив поддержки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#create-support-archive "Узнайте, как выполнять задачи настройки OneAgent без переустановки.").',
    # ## Requirements
    "## Requirements": "## Требования",
    "* Dynatrace SaaS environment: Dynatrace version 1.202+": "* Окружение Dynatrace SaaS: Dynatrace версии 1.202+",
    "* Dynatrace Managed environment: Dynatrace version 1.208+": "* Окружение Dynatrace Managed: Dynatrace версии 1.208+",
    "* **View sensitive request data** environment permission": "* Разрешение окружения **View sensitive request data**",
    # ## Analyze automatically
    "## Analyze automatically": "## Автоматический анализ",
    "This procedure describes the default procedure: Dynatrace collects diagnostics data for a host or process and immediately analyzes it.": "Данная процедура описывает стандартный сценарий: Dynatrace собирает диагностические данные для хоста или процесса и немедленно анализирует их.",
    "If you prefer to collect and review the data before manually submitting it to Dynatrace for analysis, see [Collect and review locally](#collect-and-review-locally).": "Если требуется сначала собрать и проверить данные перед тем, как вручную передать их в Dynatrace для анализа, см. раздел [Собрать и проверить локально](#collect-and-review-locally).",
    "1. Go to **Hosts**.": "1. Перейдите в **Hosts**.",
    "2. Select the host you want to troubleshoot.": "2. Выберите хост, для которого нужно выполнить диагностику.",
    "3. Run diagnostics on the host or process level.": "3. Запустите диагностику на уровне хоста или процесса.",
    # mojibake ellipsis â\x80¦
    "* Host level: on the host page, open the browse menu (**\xe2\x80\xa6**) and select **Run OneAgent diagnostics**.": "* Уровень хоста: на странице хоста откройте меню (**...**) и выберите **Run OneAgent diagnostics**.",
    "Example menu selection": "Пример выбора пункта меню",
    "![OneAgent diagnostics: menu item](https://dt-cdn.net/images/diagnostics-menu-item2-950-0243641987.png)": "![OneAgent diagnostics: menu item](https://dt-cdn.net/images/diagnostics-menu-item2-950-0243641987.png)",
    "OneAgent diagnostics: menu item": "OneAgent diagnostics: пункт меню",
    "* Process level: on the host page, open a process page, and then select **Run OneAgent diagnostics** from the browse menu (**\xe2\x80\xa6**) on the process page.": "* Уровень процесса: на странице хоста откройте страницу процесса, затем выберите **Run OneAgent diagnostics** из меню (**...**) на странице процесса.",
    # mojibake right-quote â\x80\x99 in "isn't"
    "4. On the **Run Dynatrace OneAgent diagnostics** page, briefly describe what isn\xe2\x80\x99t working as expected from your point of view.": "4. На странице **Run Dynatrace OneAgent diagnostics** кратко опишите, что именно работает не так, как ожидается.",
    "Example OneAgent diagnostics page": "Пример страницы диагностики OneAgent",
    "![OneAgent diagnostics: run](https://dt-cdn.net/images/run-diagnostics-1548-2f9988d21a.png)": "![OneAgent diagnostics: run](https://dt-cdn.net/images/run-diagnostics-1548-2f9988d21a.png)",
    "OneAgent diagnostics: run": "OneAgent diagnostics: запуск",
    "5. Optional By default, 24 hours (1 day) of data is collected for analysis. If you need more data, select the **Advanced options** link, change the number of days, and select **Apply**.": "5. Необязательно. По умолчанию для анализа собираются данные за последние 24 часа (1 день). Если нужно больше данных, нажмите ссылку **Advanced options**, измените количество дней и нажмите **Apply**.",
    "6. Select **Start analysis**.": "6. Нажмите **Start analysis**.",
    # ### What happens next (used in BOTH Analyze automatically and Collect and review locally)
    "### What happens next": "### Что происходит далее",
    "Dynatrace does the following:": "Dynatrace выполняет следующее:",
    "* Collects diagnostic data for the last 24 hours (if you didn't change the default) of the affected host or process": "* Собирает диагностические данные за последние 24 часа (если значение по умолчанию не изменялось) для затронутого хоста или процесса",
    "* Stores the collected diagnostic data": "* Сохраняет собранные диагностические данные",
    "* Uploads the diagnostic data to an S3 bucket in the AWS region of your environment for further analysis": "* Загружает диагностические данные в корзину S3 в регионе AWS вашего окружения для дальнейшего анализа",
    "The **State** column describes the current phase of the process.": "Столбец **State** отражает текущую фазу процесса.",
    "**State** does not automatically refresh. Select **Refresh** to check for a state change.": "**State** не обновляется автоматически. Нажмите **Refresh**, чтобы проверить изменение статуса.",
    # State labels — kept EN (UI labels), same key used multiple times
    "Collecting": "Collecting",
    "Data collection is in progress.": "Сбор данных выполняется.",
    "While collecting data, you can:": "Во время сбора данных доступны следующие действия:",
    "* **Refresh** the page to update the progress.": "* **Refresh** для обновления хода выполнения.",
    "* **Cancel** diagnostic data collection.": "* **Cancel** для отмены сбора диагностических данных.",
    "Collected": "Collected",
    "Dynatrace has finished collecting diagnostic data.": "Dynatrace завершил сбор диагностических данных.",
    "After collecting data, you can:": "После сбора данных доступны следующие действия:",
    "* **Analyze** to submit the collected data to Dynatrace for analysis.": "* **Analyze** для передачи собранных данных в Dynatrace на анализ.",
    "* **Download** the collected data locally for your inspection.": "* **Download** для локальной загрузки собранных данных.",
    "* **Delete** the issue, including the collected diagnostic data.": "* **Delete** для удаления задачи вместе с собранными диагностическими данными.",
    "Sending in progress": "Sending in progress",
    "Diagnostic data is being transferred to Dynatrace for analysis.": "Диагностические данные передаются в Dynatrace для анализа.",
    "While sending data, you can:": "Во время передачи данных доступны следующие действия:",
    "* **Download** the collected diagnostic data.": "* **Download** для загрузки собранных диагностических данных.",
    "Sent to Dynatrace cloud": "Sent to Dynatrace cloud",
    "Diagnostic data has been transferred to Dynatrace for analysis.": "Диагностические данные переданы в Dynatrace для анализа.",
    "Analyzing": "Analyzing",
    # L104 stripped — no trailing spaces after norm()
    "Dynatrace is now analyzing the diagnostic data.": "Dynatrace выполняет анализ диагностических данных.",
    "While analyzing data, you can:": "Во время анализа данных доступны следующие действия:",
    "Analyzed": "Analyzed",
    # L113 stripped
    "The analysis is done. The number of associated alerts is shown in parentheses.": "Анализ завершён. Количество связанных оповещений указано в скобках.",
    "After an analysis, you can:": "После анализа доступны следующие действия:",
    "* **Download** the collected diagnostic data.": "* **Download** для загрузки собранных диагностических данных.",
    "Delete in progress": "Delete in progress",
    "The diagnostic data is being deleted. While deleting data, you can:": "Диагностические данные удаляются. Во время удаления доступно следующее действие:",
    "Deleted": "Deleted",
    "The diagnostic data has been deleted. Dynatrace keeps only a small set of information about who, when, where, and why the diagnostic data was collected.": "Диагностические данные удалены. Dynatrace сохраняет только минимальный набор сведений о том, кто, когда, где и зачем собирал диагностические данные.",
    "Canceled": "Canceled",
    "The diagnostics process was canceled manually before it was finished.": "Процесс диагностики был отменён вручную до его завершения.",
    # ### Review the Dynatrace analysis
    "### Review the Dynatrace analysis": "### Просмотр результатов анализа Dynatrace",
    "When the analysis is complete, Dynatrace sends the results back to your environment. If a potential solution is identified, Dynatrace lists it in the **Alerts section.**": "По завершении анализа Dynatrace отправляет результаты обратно в ваше окружение. Если выявлено возможное решение, Dynatrace отображает его в разделе **Alerts section.**",
    "Example": "Пример",
    "![OneAgent diagnostics: alerts](https://dt-cdn.net/images/public-alerts-1-1783-14caea955d.png)": "![OneAgent diagnostics: оповещения](https://dt-cdn.net/images/public-alerts-1-1783-14caea955d.png)",
    "OneAgent diagnostics: alerts": "OneAgent diagnostics: оповещения",
    # mojibake right-quote in "isn't"
    "In this example, you can see that the fully automated OneAgent troubleshooting workflow has detected that this OneAgent was mounted on a network file system (NFS), which isn\xe2\x80\x99t supported. Instructions for resolving the issue are included.": "В данном примере видно, что полностью автоматизированный рабочий процесс устранения неполадок OneAgent обнаружил, что OneAgent смонтирован в сетевой файловой системе (NFS), которая не поддерживается. Инструкции по устранению проблемы включены в результаты.",
    # ## Collect and review locally
    "## Collect and review locally": "## Сбор и локальная проверка данных",
    "This procedure describes how to collect diagnostics data for a host or process locally. Use this option if you prefer to collect and review the data before manually submitting it to Dynatrace for analysis.": "Данная процедура описывает, как собирать диагностические данные для хоста или процесса локально. Используйте этот вариант, если нужно сначала собрать и проверить данные перед тем, как вручную передать их в Dynatrace для анализа.",
    "If you instead want to collect data and submit it to Dynatrace automatically for analysis, see [Analyze automatically](#analyze-automatically).": "Если нужно собрать данные и автоматически передать их в Dynatrace для анализа, см. раздел [Автоматический анализ](#analyze-automatically).",
    # steps 5-8 (steps 1-4 reuse keys already defined above)
    "5. Select the **Advanced options** link.": "5. Нажмите ссылку **Advanced options**.",
    "6. Select **and store locally**.": "6. Выберите **and store locally**.",
    "* While you are here, you can also change the number of days of data to collect (default = `1 day`).": "* Здесь же можно изменить количество дней, за которые собираются данные (по умолчанию: `1 day`).",
    "7. Select **Apply**.": "7. Нажмите **Apply**.",
    "8. Select **Start collection** to collect diagnostic data and store it locally.": "8. Нажмите **Start collection** для сбора диагностических данных и их хранения локально.",
    # Dynatrace now: (second What happens next section)
    "Dynatrace now:": "Теперь Dynatrace:",
    # ### What to do with the collected data
    "### What to do with the collected data": "### Что делать с собранными данными",
    "Now that the data is collected, you can:": "После сбора данных доступны следующие действия:",
    "* **Download** the collected data.": "* **Download** для загрузки собранных данных.",
    "+ You can review the data. See [Contents of diagnostic data](#contents) for an overview of what's in the download.": "+ Просмотрите данные. Обзор содержимого загружаемого архива приведён в разделе [Содержимое диагностических данных](#contents).",
    "+ You can add the data to your support ticket.": "+ Добавьте данные к вашему обращению в службу поддержки.",
    "* **Analyze** the data.": "* **Analyze** для анализа данных.",
    # ### OneAgent troubleshooting in Dynatrace Managed air-gapped environments
    "### OneAgent troubleshooting in Dynatrace Managed air-gapped environments": "### Устранение неполадок OneAgent в изолированных окружениях Dynatrace Managed",
    "In a Dynatrace Managed air-gapped environment:": "В изолированном окружении Dynatrace Managed:",
    "1. Use the **Store locally** option under **Advanced options** as described above.": "1. Используйте параметр **Store locally** в разделе **Advanced options**, как описано выше.",
    "2. After diagnostic data is collected, you can add the data to your support ticket.": "2. После сбора диагностических данных добавьте их к вашему обращению в службу поддержки.",
    "3. Dynatrace can then fetch the diagnostic data from your support ticket, analyze it, and provide automated feedback to Dynatrace Support about detected anomalies.": "3. Затем Dynatrace извлечёт диагностические данные из вашего обращения, проанализирует их и предоставит Dynatrace Support автоматизированный отчёт об обнаруженных аномалиях.",
    "Stringent data privacy protections are enforced and logged throughout this process.": "На протяжении всего процесса применяются и журналируются строгие средства защиты конфиденциальности данных.",
    # ## OneAgent diagnostics overview
    "## OneAgent diagnostics overview": "## Обзор диагностики OneAgent",
    "For an overview of all OneAgent troubleshooting runs in your environment": "Для просмотра всех запусков диагностики OneAgent в вашем окружении:",
    # step 1 reuses "1. Go to **Hosts**." already defined
    # mojibake ellipsis in browse menu
    "2. Open the browse (**\xe2\x80\xa6**) menu and select **OneAgent diagnostics overview**.": "2. Откройте меню (**...**) и выберите **OneAgent diagnostics overview**.",
    "The **Dynatrace OneAgent diagnostics overview** page lists all OneAgent diagnostics activity in your environment. Expand any entry to see details. If the data has not been deleted (all diagnostic data is deleted automatically after 30 days), you can download it or delete it.": "Страница **Dynatrace OneAgent diagnostics overview** отображает всю диагностическую активность OneAgent в вашем окружении. Разверните любую запись для просмотра подробностей. Если данные не были удалены (все диагностические данные удаляются автоматически через 30 дней), их можно загрузить или удалить.",
    # ## Contents of diagnostic data
    "## Contents of diagnostic data": "## Содержимое диагностических данных",
    "All the collected diagnostic data is compressed into a `SupportArchive<ID number>` ZIP file that includes the following folders and files:": "Все собранные диагностические данные сжимаются в ZIP-файл `SupportArchive<ID number>`, который включает следующие папки и файлы:",
    "| Folder or file | Description |": "| Папка или файл | Описание |",
    "| --- | --- |": "| --- | --- |",
    "| `host` (folder) | Contains a snapshot of the topology information of the host entity including any relationships to other hosts. |": "| `host` (папка) | Содержит снимок топологической информации об объекте хоста, включая связи с другими хостами. |",
    "| `monitored_entities` (folder) | Contains a snapshot of the topology information of all involved process groups, process group instances, services, and service instances. |": "| `monitored_entities` (папка) | Содержит снимок топологической информации обо всех задействованных группах процессов, экземплярах групп процессов, службах и экземплярах служб. |",
    "| `agent_registration_entries` (JSON) | Contains information about which OneAgent code modules are connected to Dynatrace. |": "| `agent_registration_entries` (JSON) | Содержит информацию о том, какие кодовые модули OneAgent подключены к Dynatrace. |",
    "| `archive` (JSON) | Contains information about who, when, where, and why the diagnostic data was collected. |": "| `archive` (JSON) | Содержит информацию о том, кто, когда, где и зачем собирал диагностические данные. |",
    "| `monitoring_state` (JSON) | Contains information about the monitoring state of processes and related problems. |": "| `monitoring_state` (JSON) | Содержит информацию о состоянии мониторинга процессов и связанных проблемах. |",
    # mojibake right-quote in "you've"
    "| `support_archive` (ZIP) | Contains the local configuration of the OneAgent installed on the host or process where you\xe2\x80\x99ve run the troubleshooting, as well as the OneAgent-related log files. |": "| `support_archive` (ZIP) | Содержит локальную конфигурацию OneAgent, установленного на хосте или в процессе, для которых выполнялась диагностика, а также связанные с OneAgent файлы журналов. |",
    "| `diagnostic_files` ZIP | Contains information about the process group detection, auto-injection problems, and extension configuration. |": "| `diagnostic_files` ZIP | Содержит информацию об обнаружении групп процессов, проблемах автоматической инъекции и конфигурации расширений. |",
    # ## Data privacy
    "## Data privacy": "## Конфиденциальность данных",
    "To comply with regional data protection and privacy regulations, Dynatrace does the following:": "В целях соответствия региональным требованиям по защите данных и конфиденциальности Dynatrace выполняет следующее:",
    "* Masks some personal data before storing a support archive in Cassandra and uploading it to an AWS S3 bucket. For example, IBANs and URI credentials are replaced with `<masked>`. However, some personal data may not be masked.": "* Маскирует часть персональных данных перед сохранением архива поддержки в Cassandra и загрузкой его в корзину AWS S3. Например, IBAN и учётные данные URI заменяются на `<masked>`. При этом часть персональных данных может не быть замаскирована.",
    "* Writes audit log messages when support archives are created, analyzed, accessed, and deleted to ensure transparency in the use of support archives.": "* Записывает сообщения журнала аудита при создании, анализе, обращении и удалении архивов поддержки для обеспечения прозрачности их использования.",
    '* Provides access to OneAgent support archives only to users that have the **View sensitive request data** [environment permission](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").': '* Предоставляет доступ к архивам поддержки OneAgent только пользователям с [разрешением окружения](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на основе ролей") **View sensitive request data**.',
    '* Automatically deletes all diagnostic data 30 days after its collection. This [data retention period](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Check retention times for various data types.") is configurable.': '* Автоматически удаляет все диагностические данные через 30 дней после их сбора. Этот [период хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Проверьте сроки хранения различных типов данных.") настраивается.',
    "This applies to the data on the Dynatrace Cluster. You can also choose to delete collected diagnostic data earlier.": "Это относится к данным на кластере Dynatrace. Собранные диагностические данные также можно удалить раньше срока.",
    "For related details on OneAgent diagnostics, check the following pages:": "Дополнительные сведения, связанные с диагностикой OneAgent, см. на следующих страницах:",
    '* [Personal data captured by Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#oneagent-diagnostics "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")': '* [Персональные данные, собираемые Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#oneagent-diagnostics "Узнайте, какие типы данных конечных пользователей могут собираться при мониторинге Dynatrace и какие методы маскирования персональных данных доступны.")',
    '* [Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Check retention times for various data types.")': '* [Периоды хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Проверьте сроки хранения различных типов данных.")',
    # ## Troubleshooting
    "## Troubleshooting": "## Устранение неполадок",
    # mojibake right-quote in "wasn't"
    "Status: `Collecting of the diagnostic data wasn\xe2\x80\x99t possible within 20 minutes.`": "Статус: `Collecting of the diagnostic data wasn't possible within 20 minutes.`",
    "* If Dynatrace cannot collect diagnostic data within 20 minutes, it automatically tries again.": "* Если Dynatrace не может собрать диагностические данные в течение 20 минут, процесс автоматически повторяется.",
    "* If the retry fails as well, we suggest that you contact a Dynatrace product expert via live chat.": "* Если повторная попытка также завершается неудачно, рекомендуем обратиться к специалисту по продуктам Dynatrace через чат.",
    "`State` appears to be frozen.": "Статус `State` кажется застывшим.",
    # ## FAQ
    "## FAQ": "## Вопросы и ответы",
    "Can I access the S3 directly or use my own S3?": "Можно ли получить прямой доступ к S3 или использовать собственную корзину S3?",
    "No, you cannot access the S3 directly or use your own.": "Нет, прямой доступ к S3 и использование собственной корзины не поддерживаются.",
    "OneAgent diagnostics uploads the diagnostic data to the Dynatrace S3 bucket that is configured for the environment/cluster by Dynatrace. The S3 bucket used depends on the location of the environment/cluster.": "Диагностика OneAgent загружает диагностические данные в корзину S3 Dynatrace, настроенную для окружения/кластера компанией Dynatrace. Используемая корзина S3 зависит от местоположения окружения/кластера.",
}

# Lines that must remain verbatim EN
PASS = set()

if __name__ == "__main__":
    build_one(REL, FN, TRANS, PASS)
    qa_one(REL, FN)
