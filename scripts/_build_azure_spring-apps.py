# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-spring"

TT_SPRING = "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps."
TT_ENABLE = "Включение мониторинга Azure в Dynatrace."
TT_DASH = "Узнайте, как создавать и редактировать дашборды Dynatrace."

TRANS = {
    "title: Monitor Azure Spring Apps": "title: Мониторинг Azure Spring Apps",
    "# Monitor Azure Spring Apps": "# Мониторинг Azure Spring Apps",
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Aug 19, 2020": "* Опубликовано 19 августа 2020 г.",
    "Dynatrace ingests metrics for multiple preselected namespaces, including Azure Spring Apps. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая Azure Spring Apps. Для каждого экземпляра сервиса можно просматривать метрики, разбивать их по различным измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.",
    "## Prerequisites": "## Предварительные требования",
    "* Dynatrace version 1.200+": "* Dynatrace версии 1.200+",
    "* Environment ActiveGate version 1.195+": "* Environment ActiveGate версии 1.195+",
    "## Enable monitoring": "## Включение мониторинга",
    f'To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").': f'О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "{TT_ENABLE}").',
    "## Activate OneAgent Recommended": "## Активация OneAgent (рекомендуется)",
    f'For an end-to-end view into your Spring Apps workloads, you can [set up OneAgent integration with Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.").': f'Для комплексного мониторинга рабочих нагрузок Spring Apps можно [настроить интеграцию OneAgent с Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "{TT_SPRING}").',
    "## View service metrics": "## Просмотр метрик сервиса",
    "You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.": "Метрики сервиса можно просматривать в окружении Dynatrace на странице **custom device overview page** или на странице **Dashboards**.",
    "### View metrics on the custom device overview page": "### Просмотр метрик на странице custom device overview",
    "To access the custom device overview page": "Чтобы перейти на страницу custom device overview",
    "1. Go to **Technologies & Processes**.": "1. Откройте **Technologies & Processes**.",
    "2. Filter by service name and select the relevant custom device group.": "2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.",
    "3. Once you select the custom device group, you're on the **custom device group overview page**.": "3. После выбора группы откроется страница **custom device group overview page**.",
    "4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.": "4. На странице **custom device group overview page** перечислены все экземпляры (пользовательские устройства) группы. Выберите экземпляр, чтобы перейти на страницу **custom device overview page**.",
    "### View metrics on your dashboard": "### Просмотр метрик на дашборде",
    "If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.": "Если для сервиса существует готовый дашборд, на странице **Dashboards** появится готовый дашборд с рекомендуемыми метриками для этого сервиса. Найти нужные дашборды можно с помощью фильтров **Preset** и **Name**.",
    "For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.": "Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Для этого откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.",
    "You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.": "Готовый дашборд нельзя изменить напрямую, но его можно клонировать и отредактировать. Чтобы клонировать дашборд, откройте меню просмотра (**…**) и выберите **Clone**.",
    "To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.": "Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню просмотра (**…**) и выберите **Hide**.",
    "Hiding a dashboard doesn't affect other users.": "Скрытие дашборда не влияет на других пользователей.",
    "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)": "![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)",
    "Clone hide azure": "Clone hide azure",
    "![Spring](https://dt-cdn.net/images/2021-03-12-11-35-07-1496-2bea71b55d.png)": "![Spring](https://dt-cdn.net/images/2021-03-12-11-35-07-1496-2bea71b55d.png)",
    "Spring": "Spring",
    "## Available metrics": "## Доступные метрики",
    "| Name | Description | Dimensions | Unit | Recommended |": "| Имя | Описание | Измерения | Единица измерения | Рекомендуется |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| jvm.gc.live.data.size | Size of old generation memory pool after a full GC | AppName, Pod | Byte | Applicable |": "| jvm.gc.live.data.size | Размер пула памяти старшего поколения после полного GC | AppName, Pod | Byte | Applicable |",
    "| jvm.gc.max.data.size | Max size of old generation memory pool | AppName, Pod | Byte | Applicable |": "| jvm.gc.max.data.size | Максимальный размер пула памяти старшего поколения | AppName, Pod | Byte | Applicable |",
    "| jvm.gc.memory.allocated | Incremented for an increase in the size of the young generation memory pool after one GC to before the next | AppName, Pod | Byte | Applicable |": "| jvm.gc.memory.allocated | Увеличивается при росте размера пула памяти младшего поколения от одного GC до начала следующего | AppName, Pod | Byte | Applicable |",
    "| jvm.gc.memory.promoted | Count of positive increases in the size of the old generation memory pool before GC to after GC | AppName, Pod | Byte | Applicable |": "| jvm.gc.memory.promoted | Количество положительных приростов размера пула памяти старшего поколения до и после GC | AppName, Pod | Byte | Applicable |",
    "| jvm.gc.pause.total.count | GC pause count | AppName, Pod | Count | Applicable |": "| jvm.gc.pause.total.count | Количество пауз GC | AppName, Pod | Count | Applicable |",
    "| jvm.gc.pause.total.time | GC pause total time | AppName, Pod | MilliSecond | Applicable |": "| jvm.gc.pause.total.time | Суммарное время пауз GC | AppName, Pod | MilliSecond | Applicable |",
    "| jvm.memory.committed | Memory assigned to JVM in bytes | AppName, Pod | Byte | Applicable |": "| jvm.memory.committed | Память, выделенная JVM, в байтах | AppName, Pod | Byte | Applicable |",
    "| jvm.memory.max | The maximum amount of memory in bytes that can be used for memory management | AppName, Pod | Byte | Applicable |": "| jvm.memory.max | Максимальный объём памяти в байтах, доступный для управления памятью | AppName, Pod | Byte | Applicable |",
    "| jvm.memory.used | App memory used in bytes | AppName, Pod | Byte | Applicable |": "| jvm.memory.used | Использованная приложением память в байтах | AppName, Pod | Byte | Applicable |",
    "| process.cpu.usage | App JVM CPU usage percentage | AppName, Pod | Percent | Applicable |": "| process.cpu.usage | Процент использования CPU JVM приложением | AppName, Pod | Percent | Applicable |",
    "| system.cpu.usage | The recent CPU usage for the whole system | AppName, Pod | Percent | Applicable |": "| system.cpu.usage | Недавнее использование CPU для всей системы | AppName, Pod | Percent | Applicable |",
    "| tomcat.global.error | Tomcat global error | AppName, Pod | Count | Applicable |": "| tomcat.global.error | Глобальная ошибка Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.global.received | Tomcat total received bytes | AppName, Pod | Byte | Applicable |": "| tomcat.global.received | Всего получено байт Tomcat | AppName, Pod | Byte | Applicable |",
    "| tomcat.global.request.avg.time | Tomcat request average time | AppName, Pod | MilliSecond | Applicable |": "| tomcat.global.request.avg.time | Среднее время запроса Tomcat | AppName, Pod | MilliSecond | Applicable |",
    "| tomcat.global.request.max | Tomcat request maximum time | AppName, Pod | MilliSecond | Applicable |": "| tomcat.global.request.max | Максимальное время запроса Tomcat | AppName, Pod | MilliSecond | Applicable |",
    "| tomcat.global.request.total.count | Tomcat request total count | AppName, Pod | Count | Applicable |": "| tomcat.global.request.total.count | Суммарное количество запросов Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.global.request.total.time | Tomcat request total time | AppName, Pod | MilliSecond | Applicable |": "| tomcat.global.request.total.time | Суммарное время запросов Tomcat | AppName, Pod | MilliSecond | Applicable |",
    "| tomcat.global.sent | Tomcat total sent bytes | AppName, Pod | Byte | Applicable |": "| tomcat.global.sent | Всего отправлено байт Tomcat | AppName, Pod | Byte | Applicable |",
    "| tomcat.sessions.active.current | Tomcat session active count | AppName, Pod | Count | Applicable |": "| tomcat.sessions.active.current | Количество активных сессий Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.sessions.active.max | Tomcat session maximum active count | AppName, Pod | Count | Applicable |": "| tomcat.sessions.active.max | Максимальное количество активных сессий Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.sessions.alive.max | Tomcat session maximum alive time | AppName, Pod | MilliSecond | Applicable |": "| tomcat.sessions.alive.max | Максимальное время жизни сессии Tomcat | AppName, Pod | MilliSecond | Applicable |",
    "| tomcat.sessions.created | Tomcat session created count | AppName, Pod | Count | Applicable |": "| tomcat.sessions.created | Количество созданных сессий Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.sessions.expired | Tomcat session expired count | AppName, Pod | Count | Applicable |": "| tomcat.sessions.expired | Количество истёкших сессий Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.sessions.rejected | Tomcat session rejected count | AppName, Pod | Count | Applicable |": "| tomcat.sessions.rejected | Количество отклонённых сессий Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.threads.config.max | Tomcat configuration maximum thread count | AppName, Pod | Count | Applicable |": "| tomcat.threads.config.max | Максимальное количество потоков по конфигурации Tomcat | AppName, Pod | Count | Applicable |",
    "| tomcat.threads.current | Tomcat current thread count | AppName, Pod | Count | Applicable |": "| tomcat.threads.current | Текущее количество потоков Tomcat | AppName, Pod | Count | Applicable |",
    "## Related topics": "## Связанные темы",
    f'* [Monitor Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.")': f'* [Мониторинг Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "{TT_SPRING}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-azure-spring-apps.md", TRANS, PASS)
    qa_one(REL, "monitor-azure-spring-apps.md")
