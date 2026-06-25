# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/advanced-configuration/custom-dashboards.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/advanced-configuration"

TRANS = {
    "title: Distribute custom dashboards with your extensions": "title: Распределение пользовательских панелей мониторинга с расширениями",
    "# Distribute custom dashboards with your extensions": "# Распределение пользовательских панелей мониторинга с расширениями",
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Aug 07, 2025": "* Обновлено 7 августа 2025 г.",
    "After your extension starts sending data to Dynatrace, you can create a custom dashboard, export its definition to a JSON file, and add the JSON to your extension archive.": "После того как расширение начнёт отправлять данные в Dynatrace, можно создать пользовательскую панель мониторинга, экспортировать её определение в JSON-файл и добавить JSON в архив расширения.",
    "## Dashboards Classic": "## Dashboards Classic",
    'If you\'re using [Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic."), follow these procedures.': 'При использовании [Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.") следуйте приведённым ниже процедурам.',
    'After your extension starts sending data to Dynatrace, you can [create a custom dashboard](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.") and then export its definition to a JSON file and add it to your extension archive. You can export a dashboard definition through the Dynatrace web UI or Dynatrace API.': 'После того как расширение начнёт отправлять данные в Dynatrace, можно [создать пользовательскую панель мониторинга](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать панели мониторинга Dynatrace."), затем экспортировать её определение в JSON-файл и добавить в архив расширения. Экспортировать определение панели можно через веб-интерфейс Dynatrace или Dynatrace API.',
    "### Export dashboard JSON in web UI": "### Экспорт JSON панели мониторинга через веб-интерфейс",
    "1. Go to **Dashboards**.": "1. Откройте **Dashboards**.",
    "2. In the row for the dashboard you want to export, select **More** (**…**) > **Export**.": "2. В строке нужной панели мониторинга выберите **More** (**…**) > **Export**.",
    "A JSON file with the dashboard's name is downloaded to your local machine.": "На локальный компьютер будет загружен JSON-файл с именем панели мониторинга.",
    'For more information, see [Edit Dynatrace dashboard JSON](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.").': 'Дополнительные сведения см. в разделе [Редактирование JSON панели мониторинга Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Узнайте, как экспортировать, редактировать и импортировать JSON панели мониторинга Dynatrace.").',
    "### Export dashboard JSON using API": "### Экспорт JSON панели мониторинга через API",
    "1. Go to **Dashboards** and display the dashboard.": "1. Откройте **Dashboards** и перейдите к нужной панели мониторинга.",
    "2. In the dashboard URL, find the `id` parameter (for example, `id=d996b25e-593c-4213-8ad3-c87319a8830a`) and save the parameter value.": "2. В URL панели мониторинга найдите параметр `id` (например, `id=d996b25e-593c-4213-8ad3-c87319a8830a`) и сохраните его значение.",
    '3. Use the [Get a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard "View a dashboard via the Dynatrace Classic API.") API endpoint to get the dashboard JSON definition.': '3. Используйте конечную точку API [Get a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard "Просмотр панели мониторинга через Dynatrace Classic API.") для получения JSON-определения панели.',
    "Run the following command to get the dashboard definition. For this example, we use the Dynatrace SaaS URL:": "Выполните следующую команду для получения определения панели мониторинга. В данном примере используется URL Dynatrace SaaS:",
    "Replace:": "Замените:",
    '* `{env-id}` with your [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': '* `{env-id}` на [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Знакомство с окружениями мониторинга и работа с ними.").',
    '* `{api-token}` with an [API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': '* `{api-token}` на [API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для использования Dynatrace API.") с необходимыми [разрешениями](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.").',
    "* `{dashboard-id}` with the dashboard identifier you determined in the previous step.": "* `{dashboard-id}` на идентификатор панели мониторинга, определённый на предыдущем шаге.",
    "4. The call returns the JSON payload containing the dashboard definition. Save it as a JSON file.": "4. Вызов возвращает JSON-полезную нагрузку с определением панели мониторинга. Сохраните её как JSON-файл.",
    "### Add your dashboard to the extension package": "### Добавление панели мониторинга в пакет расширения",
    "Add your dashboard JSON file to your extension package and reference it in your extension YAML file.": "Добавьте JSON-файл панели мониторинга в пакет расширения и укажите на него в файле YAML расширения.",
    "For the following package structure:": "Для следующей структуры пакета:",
    'Use the following reference in the top level of your [YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework."):': 'Используйте следующую ссылку на верхнем уровне [файла YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью Extensions framework."):',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "custom-dashboards.md", TRANS, PASS)
    qa_one(REL, "custom-dashboards.md")
