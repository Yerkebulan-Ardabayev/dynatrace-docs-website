---
title: Зоны управления и принятые данные журналов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring
scraped: 2026-05-12T11:08:37.139615
---

# Зоны управления и принятые данные журналов (Logs Classic)

# Зоны управления и принятые данные журналов (Logs Classic)

* Пояснение
* Чтение: 2 мин
* Обновлено 18 января 2023 г.

Log Monitoring Classic

Management zone — это механизм разделения информации, позволяющий сосредоточиться на конкретных частях топологии. Можно настраивать Management zone для включения определённого набора отслеживаемых сущностей [через правила Management zone](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules#rule-types "Определите правила для ограничения сущностей, доступных в Management zone."). Для анализа журналов, генерируемых сущностью Management zone, используйте один из двух методов:

* Приём журналов через OneAgent, который автоматически обнаруживает файлы журналов в топологическом контексте.
* Использование [приёма журналов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов.") через API, требующего определённых атрибутов для обнаружения топологического контекста.

При использовании API приёма журналов через [Log Monitoring API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправляйте пользовательские журналы в Dynatrace через Log Monitoring API v2.") можно отправлять объект, представляющий одно событие, или массив объектов для нескольких событий. Объект должен содержать хотя бы один из следующих ключей атрибутов, определяющих типы сущностей:

* `dt.entity.process_group_instance` — экземпляры групп процессов
* `dt.entity.custom_device` — пользовательские устройства
* `dt.entity.host` — хосты

Log Monitoring Classic проверяет в указанном порядке, принадлежит ли значение атрибута события журнала (и, следовательно, соответствующая сущность) данной Management zone. При первом совпадении проверка прекращается и данные журнала назначаются Management zone, которой принадлежит совпавшая сущность.

Если Management zone уже предоставляет доступ к хосту, через который принимаются журналы, доступ к этим журналам предоставляется автоматически.

В [просмотрщике журналов](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Узнайте, как использовать просмотрщик журналов Dynatrace для анализа данных.") нажмите кнопку **Filter** в строке меню для выбора Management zone. Просмотрщик отображает данные журналов для сущностей, совпадающих с перечисленными выше ключами атрибутов.

Для просмотра принятых и автоматически назначенных данных журналов пользователи должны иметь разрешение **View logs** на уровне окружения или Management zone.

Просмотрщик журналов отображает данные журналов для не более 10 000 отслеживаемых сущностей на Management zone. Если Management zone содержит более 10 000 сущностей, её можно разбить на более мелкие зоны менее чем из 10 000 сущностей каждая.

Для фильтрации журналов по другим атрибутам можно добавить [правило для включения журнально-основанных размерных данных](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules#ui "Определите правила для ограничения сущностей, доступных в Management zone.") в Management zone.

## Связанные темы

* [Log Monitoring API v2 — POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправляйте пользовательские журналы в Dynatrace через Log Monitoring API v2.")
* [API приёма журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов.")
* [Просмотрщик журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Узнайте, как использовать просмотрщик журналов Dynatrace для анализа данных.")
* [Правила Management zone](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Определите правила для ограничения сущностей, доступных в Management zone.")