---
title: Управление зонами и принятые журналы данных (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring
scraped: 2026-03-06T21:28:58.652457
---

# Зоны управления и загружаемые данные журналов (Logs Classic)


* Пояснение

Log Monitoring Classic

Зоны управления — это механизм разделения информации, позволяющий сосредоточиться на конкретных частях топологии. Вы можете настроить зону управления так, чтобы она включала определённый набор отслеживаемых объектов [с помощью правил зоны управления](../../../manage/identity-access-management/permission-management/management-zones/management-zone-rules.md#rule-types "Define rules to limit the entities accessible within a management zone."). Используйте один из двух методов для анализа журналов, создаваемых объектом зоны управления.

* Загружайте журналы через OneAgent, который автоматически обнаруживает файлы журналов в топологическом контексте.
* Используйте [загрузку журналов](../acquire-log-data/logs-classic-ingestion-api.md "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") через API, что требует наличия определённых атрибутов для определения топологического контекста.

Если вы используете API загрузки журналов через [Log Monitoring API v2](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Push custom logs to Dynatrace via the Log Monitoring API v2."), вы можете отправить объект, представляющий одно событие, или массив объектов, представляющих несколько событий. Объект должен содержать хотя бы один из следующих ключей атрибутов, определяющих типы объектов, для которых загружаются данные журналов.

* `dt.entity.process_group_instance` — экземпляры группы процессов
* `dt.entity.custom_device` — пользовательские устройства
* `dt.entity.host` — хосты

Log Monitoring Classic проверяет в указанном выше порядке, принадлежит ли значение атрибута события журнала (и, следовательно, соответствующий объект) данной зоне управления. При первом совпадении Log Monitoring Classic прекращает проверку и назначает данные журнала зоне управления, которой принадлежит сопоставленный объект.

Если ваша зона управления уже предоставляет доступ к хосту, через который загружаются журналы, вы автоматически получаете доступ к этим журналам.

В [средстве просмотра журналов](log-viewer.md "Learn how to use Dynatrace log viewer to analyze log data.") нажмите кнопку **Фильтр** в строке меню, чтобы выбрать зону управления. Средство просмотра журналов отображает данные журналов для объектов, соответствующих перечисленным выше ключам атрибутов событий журнала.

Пользователи должны иметь разрешение **View logs** на уровне среды или уровне зоны управления, чтобы иметь возможность просматривать загруженные и автоматически назначенные данные журналов.

Средство просмотра журналов отображает данные журналов для не более чем 10 000 отслеживаемых объектов на зону управления. Если ваша зона управления содержит более 10 000 отслеживаемых объектов и вы хотите видеть данные журналов для всех отслеживаемых объектов, вы можете разбить зону управления на более мелкие зоны, содержащие менее 10 000 отслеживаемых объектов каждая.

Если вам необходимо фильтровать журналы по другим атрибутам, вы можете добавить [правило для включения размерных данных на основе журналов](../../../manage/identity-access-management/permission-management/management-zones/management-zone-rules.md#ui "Define rules to limit the entities accessible within a management zone.") в зону управления. Журналы, удовлетворяющие условиям такого правила, затем отображаются в средстве просмотра журналов после выбора зоны управления с помощью кнопки **Фильтр**.

## Связанные темы

* [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [API загрузки журналов (Logs Classic)](../acquire-log-data/logs-classic-ingestion-api.md "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")
* [Средство просмотра журналов (Logs Classic)](log-viewer.md "Learn how to use Dynatrace log viewer to analyze log data.")
* [Правила зон управления](../../../manage/identity-access-management/permission-management/management-zones/management-zone-rules.md "Define rules to limit the entities accessible within a management zone.")
