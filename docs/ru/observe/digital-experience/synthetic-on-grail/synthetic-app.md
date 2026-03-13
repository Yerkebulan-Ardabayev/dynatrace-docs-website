---
title: Synthetic app
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app
scraped: 2026-03-06T21:12:42.033714
---

# Приложение Synthetic

# Приложение Synthetic

* Latest Dynatrace
* Приложение
* Чтение: 7 мин
* Обновлено 10 июля 2025 г.

С помощью приложения ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** вы можете создавать и управлять синтетическими мониторами.

Предварительные требования

### Разрешения

В следующей таблице описаны необходимые разрешения.

geolocation:locations:lookup

позволяет запрашивать данные о географическом местоположении для приватных локаций

storage:buckets:read

позволяет запрашивать данные из Grail

storage:entities:read

позволяет запрашивать отслеживаемые сущности из Grail

storage:metrics:read

позволяет запрашивать метрики из Grail

storage:events:read

позволяет запрашивать события из Grail

storage:user.events:read

позволяет запрашивать события из Grail

storage:files:read

позволяет запрашивать события из Grail

document:documents:write

позволяет создавать и обновлять наборы фильтров

document:documents:read

позволяет запрашивать сохранённые наборы фильтров

document:documents:delete

позволяет удалять наборы фильтров

### Установка

Убедитесь, что приложение [установлено в вашей среде](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Начало работы

Сценарии использования

![Список синтетических мониторов с мощными фильтрами, ключевыми метриками и панелью предварительного просмотра с деталями конфигурации и последними результатами выполнения](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.synthetic/media/adca5313-1eec-4f64-b9b2-9ded18dd78b7.png)![Показывает результаты выполнения теста с акцентом на доступность и производительность, с детализацией на уровне монитора и шагов](https://cdn.hub.central.dynatrace.com/hub/health_QnbCRwv.png)![Сравнение предыдущих запусков HTTP-монитора для выявления замедлений, сбоев или улучшений с различиями во времени загрузки, кодах, ошибках и полезных нагрузках](https://cdn.hub.central.dynatrace.com/hub/compare_1ViF4zz.png)![Определение области действия и конфигурации монитора: частота, локации, критерии успешности и правила генерации проблем](https://cdn.hub.central.dynatrace.com/hub/configuration_6h5FfCa_BYo9Dvp.png)![Настройка приватной синтетической локации: географическое положение, назначенные ActiveGate и правила триггеров проблем самомониторинга](https://cdn.hub.central.dynatrace.com/hub/private_h1joYiz.png)

1 из 5 Список синтетических мониторов с мощными фильтрами, ключевыми метриками и панелью предварительного просмотра с деталями конфигурации и последними результатами выполнения

### Навигация и фильтрация

Страница синтетических мониторов является главной страницей приложения ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** и представляет собой центр управления вашими синтетическими мониторами. По умолчанию страница отображает все мониторы в вашей среде, активные или неактивные, в [таблице](#table) с ключевыми результатами по доступности и производительности, чтобы вы могли оценить состояние ваших мониторов с первого взгляда.
Мощные и гибкие [фильтры](#filters) позволяют сузить поиск синтетических мониторов.

Чтобы узнать, как создать новый монитор, см. [Создание мониторов](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app#create-monitors "View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.").

### Таблица мониторов

По умолчанию мониторы с открытыми проблемами (инцидентами) отображаются в алфавитном порядке в верхней части таблицы. Далее в алфавитном порядке отображаются включённые мониторы без проблем, за которыми следуют отключённые мониторы в алфавитном порядке.

Вы можете скрывать и сортировать столбцы в порядке возрастания или убывания. Выберите **Columns** в правом верхнем углу таблицы, чтобы указать, какие столбцы отображать или скрывать.

Элементы управления пагинацией в нижней части таблицы мониторов позволяют указать количество **строк на странице** и перемещаться по таблице мониторов от страницы к странице.

В столбцах отображается следующая информация для каждого монитора.

* **Monitor name** — выберите для просмотра краткого обзора монитора справа от страницы синтетических мониторов
* **Created** — дата и время создания монитора
* **Last modified** — идентификатор пользователя, который последним редактировал монитор, и дата и время изменения
* **ID** — полный идентификатор монитора
* **Last execution** — дата и время последнего выполнения из любой локации
* **Type** — тип монитора, например, `HTTP`
* **Frequency** — частота выполнения или `On demand`, как указано в конфигурации монитора
* **Availability** — средняя доступность за выбранный период
* **Duration** — средняя производительность за выбранный период в секундах

#### Предварительный просмотр монитора

В приложении ![Synthetic Classic](https://dt-cdn.net/images/synthetic-512-83ec796e54.png "Synthetic Classic") **Synthetic** для отображения панели предварительного просмотра монитора выберите имя монитора в столбце **Monitor name** на странице **Synthetic monitors**.

Для переключения между мониторами откройте панель предварительного просмотра для любого монитора, а затем выберите имя другого монитора для переключения предварительного просмотра на вновь выбранный монитор. Фильтры сохраняются.

Панель предварительного просмотра показывает:

* Плитки с важной информацией для быстрого обзора:

  + Простой/Доступен/Нет данных — статус доступности монитора в момент последнего выполненного теста
  + Активные инциденты — количество инцидентов, наблюдаемых в данный момент
  + Затронутые локации — количество локаций, где произошли простои в указанный период
  + Доступность — показатель доступности монитора в процентах за указанный период
  + Общее время простоя — суммарное время простоя по всем локациям за указанный период
  + Длительность — среднее время отклика по всем локациям за указанный период
* Список проблем, включая дату начала проблемы и длительность, или **No problems found**. Для анализа проблемы в приложении **Problems** выберите ссылку на проблему в списке.
* Список изменений. В последней версии Dynatrace этот раздел отображает изменения монитора: когда он был изменён, кто его изменил и что было изменено. Вы можете получить доступ к изменениям только за указанный период.
* Свойства, такие как тип монитора, локации, запросы в последнем выполнении, частота, шаги и теги.

Используйте элементы управления в правом верхнем углу панели предварительного просмотра для:

* Редактирования выбранного монитора
* Удаления выбранного монитора
* Включения отключённого монитора
* Отключения включённого монитора
* Отображения страницы отчётов для выбранного монитора (см. ниже)
* Закрытия панели предварительного просмотра

### Фильтры

Фильтры с возможностью множественного выбора помогают найти нужные мониторы. Вы также можете сохранять часто используемые фильтры. Разверните ![Open Dashboards panel](https://dt-cdn.net/images/dashboards-app-dashboards-panel-open-6c03b43117.svg "Open Dashboards panel") или сверните ![Close Dashboards panel](https://dt-cdn.net/images/dashboards-app-dashboards-panel-close-78d6b527ad.svg "Close Dashboards panel") фильтры, чтобы сосредоточиться на поиске или результатах. Фильтры автоматически сворачиваются при просмотре краткого обзора монитора.

Следующие категории фильтров (каждая с несколькими вариантами) позволяют искать мониторы.

* **Type** — тип монитора
* **Ongoing issues** — мониторы с проблемами доступности или производительности и без них
* **Frontend application** — связанное приложение [RUM](/docs/observe/digital-experience "Optimize end-user experience with Digital Experience Monitoring to ensure application performance and availability across all channels.")
* **Status** — активны ли мониторы или неактивны (отключены)
* **Locations** — [публичные](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") и [приватные](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") локации мониторинга
* **Device profile** — например, `desktop`, `Apple iPhone 8`
* **Last editor** — идентификатор пользователя, который последним редактировал монитор
* **Tags** — значения или пары ключ-значение, применённые к мониторам; вы можете выбрать теги для включения или исключения из поиска.
* **Edited during the timeframe** — мониторы, которые были или не были отредактированы в течение выбранного глобального периода
* **ISP / Cloud provider** — провайдер публичных синтетических локаций
* **Frequency** — частота мониторинга

#### Как работают фильтры

В каждой категории вы можете выбрать несколько фильтров. Например, при выборе мониторов по **Type** вы можете выбрать и **HTTP**, и **DNS** мониторы. Внутри категории фильтры применяются с использованием логики `OR` — отображаются мониторы, соответствующие любому из выбранных вариантов.

Варианты фильтров, отображаемые в большинстве категорий, зависят от ваших мониторов; доступны только те фильтры, которые релевантны для ваших мониторов. Например, если у вас нет HTTP-мониторов, вы не увидите опцию **HTTP** для фильтрации.

Отображается количество мониторов, соответствующих каждому фильтру. Например, список **Locations** показывает количество мониторов на каждой локации. Это число динамически обновляется на основе ваших фильтров в других категориях.

Вы можете выбирать фильтры в нескольких категориях. Категории фильтров применяются с использованием логики `AND`. Например, если вы выберете все мониторы **Network availability** (**DNS**, **ICMP** и **TCP**) и два тега, `IP` и `host-group`, результирующий список будет содержать мониторы сетевой доступности с тегом `IP` или `host-group`.

#### Наборы фильтров

Вы можете сохранять комбинации фильтров как именованные наборы фильтров для быстрого доступа к часто используемым критериям поиска — выберите **Save new filter** и укажите имя фильтра. Вы можете установить один набор фильтров по умолчанию, который будет применяться каждый раз при переходе в приложение ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**.

Выберите **More** ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") рядом с набором фильтров для дополнительных действий, таких как **Set as default**, **Rename**, **Duplicate** или **Delete**.

#### Панель фильтров

Панель фильтров ![Variable](https://dt-cdn.net/images/dashboards-app-dashboard-add-variable-821b40325c.svg "Variable") в верхней части страницы содержит фиксированный фильтр для поиска по имени монитора: выберите **Filter by name** и введите строку поиска. Все дополнительные фильтры или [наборы фильтров](#filter-sets), которые вы применяете, отображаются в панели фильтров, откуда вы можете очистить применённые фильтры.

### Управление синтетическими мониторами

В разделе **Create monitor** вы можете выбрать тип синтетического монитора, который хотите создать.

### Создание мониторов

Для создания монитора:

1. Выберите **+New monitor** в правом верхнем углу ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**.
2. Выберите один из вариантов:

* Browser — выбор этой опции позволит создать браузерный монитор в **Synthetic Classic**. Узнайте, как [создать одностраничный браузерный монитор](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.").
* HTTP — выбор этой опции позволит создать HTTP-монитор в приложении ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**. Узнайте, как [создать и настроить HTTP-монитор](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor "Learn how to set up and edit an HTTP monitor to check the performance and availability of your site.").
* Network availability — выбор этой опции позволит создать NAM-монитор в приложении ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**. Узнайте, как [настроить NAM-монитор](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor "Learn how to set up a NAM monitor to check the performance and availability of your site.").

### Отчёты

Для каждого типа монитора вы можете отобразить страницу отчётов. См.

* [Отчёты](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/network-availability-monitoring#reporting "ICMP, TCP, and DNS synthetic monitors") NAM-мониторов в **Synthetic**.
* [Отчёты](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors "Learn about the Synthetic details page for HTTP monitors.") HTTP-мониторов в **Synthetic**.
* [Отчёты](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.") HTTP-мониторов в **Synthetic Classic**.
* [Отчёты](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.") браузерных мониторов в **Synthetic Classic**.

### Расчёт общего времени простоя для синтетических мониторов

Общее время мониторинга разделяется на минутные точки данных. Все точки данных считаются выполнениями, хотя они не обязательно совпадают с реальными выполнениями.

На экране ниже синие точки данных совпадают с реальными выполнениями, а белые — нет.

![Выполнения включено/выключено и точки данных](https://dt-cdn.net/images/screenshot-2025-07-09-114246-1857-8ed42fbafd.png)

Например, если монитор настроен на выполнение тестов каждые пять минут, каждая пятая точка данных (синяя) совпадает с реальным выполнением. Все точки данных, следующие за первым неуспешным выполнением («недоступен») и предшествующие первому успешному выполнению («доступен»), считаются «недоступными». Таким образом, общее время простоя рассчитывается следующим образом:

Общее время простоя = первое реальное выполнение с недоступностью + все последующие точки данных с недоступностью.

![Общее время простоя в детальном интерфейсе](https://dt-cdn.net/images/total-downtime-1585-bf2c26bbf9.png)

## Учебные модули

Пройдите следующий процесс для изучения приложения ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**:

[01 Отчёты HTTP-мониторов

* Справочник
* Узнайте о странице Synthetic details для HTTP-мониторов.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors)[02 Отчёты браузерных мониторов

* Справочник
* Узнайте о странице Browser details для браузерных мониторов.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/browser-monitors-results-reporting)[03 Создание и настройка браузерного монитора

* Практическое руководство
* Узнайте, как создать и настроить браузерный монитор для проверки производительности и доступности вашего сайта.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-configure-browser-monitors)[04 Отчёты NAM-мониторов

* Справочник
* Просмотрите синтетические мониторы в вашей среде, найдите мониторы и получите краткий обзор выбранного монитора.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/nam-monitors-results-reporting-synthetic-app)[05 Выполнение мониторов по требованию

* Практическое руководство
* Узнайте о выполнении мониторов по требованию.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/on-demand-executions)[06 Приватные синтетические локации

* Практическое руководство
* Узнайте, как управлять приватными локациями в приложении Synthetic.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations)[07 Создание и настройка HTTP-монитора

* Практическое руководство
* Узнайте, как настроить и редактировать HTTP-монитор для проверки производительности и доступности вашего сайта.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor)[08 Создание NAM-монитора

* Практическое руководство
* Узнайте, как настроить NAM-монитор для проверки производительности и доступности вашего сайта.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-a-nam-monitor-synthetic-app)

## Сценарии использования

* Автоматический мониторинг и тестирование доступности и производительности приложений в продуктивных средах и средах разработки.
* Исправление проблем и оптимизация цифрового опыта до того, как это затронет пользователей.
* Синтетические возможности расширены для мониторинга инфраструктуры и сервисов, которые не предоставляют интерфейсы на основе HTTPS.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучите в Dynatrace Hub

Просмотрите состояние всех дата-центров и хостов и определите первопричину проблем инфраструктуры.](https://www.dynatrace.com/hub/detail/synthetic-preview/?internal_source=doc&internal_medium=link&internal_campaign=cross)