# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide"

TT_AZMON = "Настройка и конфигурирование мониторинга Azure в Dynatrace."

TRANS = {
    "title: Enable service monitoring": "title: Включение мониторинга сервиса",
    "# Enable service monitoring": "# Включение мониторинга сервиса",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Updated on Apr 02, 2025": "* Обновлено 2 апреля 2025 г.",
    f'To enable monitoring for this service, you first need to [set up integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.").': f'Чтобы включить мониторинг этого сервиса, сначала нужно [настроить интеграцию с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "{TT_AZMON}").',
    "## Add the service to monitoring": "## Добавление сервиса в мониторинг",
    "In order to view the service metrics, you must add the service to monitoring in your Dynatrace environment.": "Чтобы просматривать метрики сервиса, нужно добавить его в мониторинг в среде Dynatrace.",
    "To add a service to monitoring": "Чтобы добавить сервис в мониторинг",
    "1. Go to **Settings** > **Cloud and virtualization** > **Azure**.": "1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.",
    "2. On the Azure overview page, select **Edit** for the desired Azure instance.": "2. На странице обзора Azure выберите **Edit** для нужного экземпляра Azure.",
    "3. Go to **Services** > **Add service**, choose the desired service name from the list, and select **Add service**.": "3. Откройте **Services** > **Add service**, выберите нужное имя сервиса из списка и нажмите **Add service**.",
    "4. Select **Save changes** to save your configuration.": "4. Нажмите **Save changes** для сохранения конфигурации.",
    "## Configure service metrics": "## Настройка метрик сервиса",
    "Once you add a service, Dynatrace starts automatically collecting a suite of metrics for this particular service. These are **recommended** metrics.": "После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для этого сервиса. Это **рекомендуемые** метрики.",
    "### Recommended metrics": "### Рекомендуемые метрики",
    "* Are enabled by default": "* Включены по умолчанию",
    "* Can't be disabled": "* Не могут быть отключены",
    "* Can have recommended dimensions (enabled by default, can't be disabled)": "* Могут сопровождаться рекомендуемыми измерениями (включены по умолчанию, не могут быть отключены)",
    "* Can have optional dimensions (disabled by default, can be enabled)": "* Могут сопровождаться дополнительными измерениями (отключены по умолчанию, можно включить)",
    "### Optional metrics": "### Дополнительные метрики",
    "Apart from the recommended metrics, most services have the possibility of enabling **optional** metrics.": "Помимо рекомендуемых метрик, для большинства сервисов можно включить **дополнительные** метрики.",
    "* Can be added and configured manually": "* Добавляются и настраиваются вручную",
    "### Add and configure metrics": "### Добавление и настройка метрик",
    "1. Go to **Settings** > **Cloud and virtualization** > **Azure**.": "1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.",
    "2. On the Azure overview page, scroll down and select **Edit** for the desired Azure instance.": "2. На странице обзора Azure прокрутите вниз и выберите **Edit** для нужного экземпляра Azure.",
    "3. Go to **Services** and select **Manage services**.": "3. Откройте **Services** и выберите **Manage services**.",
    "4. To add a metric, select the service for which you want to add metrics.": "4. Чтобы добавить метрику, выберите сервис, для которого нужно добавить метрики.",
    "5. Select **Add new metric**.": "5. Нажмите **Add new metric**.",
    "6. From the menu, select the metric you want.": "6. В меню выберите нужную метрику.",
    "7. Select **Add metric** to add the metric to monitoring.": "7. Нажмите **Add metric**, чтобы добавить метрику в мониторинг.",
    "8. To configure a metric, select **Edit**.": "8. Чтобы настроить метрику, выберите **Edit**.",
    "9. Select **Apply** to save your configuration.": "9. Нажмите **Apply** для сохранения конфигурации.",
    "## View service metrics": "## Просмотр метрик сервиса",
    "You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.": "Метрики сервиса можно просматривать в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.",
    "### View metrics on the custom device overview page": "### Просмотр метрик на странице обзора пользовательского устройства",
    "To access the custom device overview page": "Чтобы открыть страницу обзора пользовательского устройства",
    "1. Go to **Technologies & Processes**.": "1. Откройте **Technologies & Processes**.",
    "2. Filter by service name and select the relevant custom device group.": "2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.",
    "3. Once you select the custom device group, you're on the **custom device group overview page**.": "3. После выбора группы пользовательских устройств откроется **страница обзора группы пользовательских устройств**.",
    "4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.": "4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.",
    "### View metrics on your dashboard": "### Просмотр метрик на дашборде",
    "If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.": "Если для сервиса есть готовый дашборд, на странице **Dashboards** появится готовый дашборд для данного сервиса, содержащий все рекомендуемые метрики. Найти конкретные дашборды можно, отфильтровав по **Preset**, а затем по **Name**.",
    "For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.": "Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.",
    "You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.": "Вносить изменения в готовый дашборд напрямую нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню просмотра (**…**) и выберите **Clone**.",
    "To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.": "Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Чтобы скрыть дашборд, откройте меню просмотра (**…**) и выберите **Hide**.",
    "Hiding a dashboard doesn't affect other users.": "Скрытие дашборда не влияет на других пользователей.",
    "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)": "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)",
    "Clone hide azure": "Clone hide azure",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-enable-service-monitoring.md", TRANS, PASS)
    qa_one(REL, "azure-enable-service-monitoring.md")
