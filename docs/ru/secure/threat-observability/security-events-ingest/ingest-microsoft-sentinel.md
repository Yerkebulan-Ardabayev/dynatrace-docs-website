---
title: Прием событий безопасности Microsoft Sentinel
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-sentinel
scraped: 2026-03-06T21:23:57.288661
---

# Приём событий безопасности Microsoft Sentinel


* Latest Dynatrace
* Практическое руководство
* Обновлено 12 августа 2025 г.

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, описан в [руководстве по миграции таблицы безопасности Grail](../migration.md "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Принимайте события безопасности Microsoft Sentinel и анализируйте их в Dynatrace.

## Начало работы

### Обзор

Интеграция Dynatrace с [Microsoft Sentinel](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel), облачной системой управления информацией и событиями безопасности (SIEM), позволяет пользователям унифицировать и контекстуализировать результаты анализа безопасности различных инструментов и продуктов DevSecOps, обеспечивая централизованную приоритизацию, визуализацию и автоматизацию обработки результатов безопасности.

Интеграция принимает [оповещения безопасности](https://learn.microsoft.com/en-us/azure/sentinel/security-alert-schema), генерируемые различными [коннекторами](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources?tabs=defender-portal), включая продукты Microsoft, такие как [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud), а также [коннекторы сторонних продуктов](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference).

### Сценарии использования

* Визуализируйте и создавайте отчёты о текущем состоянии безопасности и тенденциях по результатам безопасности в различных средах с помощью [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и совместного использования данных наблюдаемости в реальном времени.").
* Анализируйте и приоритизируйте результаты безопасности различных инструментов и продуктов единообразно с помощью [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами на основе данных наблюдаемости в едином настраиваемом рабочем пространстве.").
* Создавайте уведомления и заявки для критических результатов безопасности с помощью [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.").
* Используйте результаты безопасности как дополнительное измерение для поиска угроз и криминалистического анализа инцидентов с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../investigations.md "Объединяйте функциональные возможности Grail для расследований на основе фактов, включая разрешение инцидентов, анализ первопричин и поиск угроз.").

### Требования

Ниже приведены требования для Microsoft Sentinel и Dynatrace.

#### Microsoft Sentinel

* Установите [Azure CLI](https://dt-url.net/yb43whw).

#### Требования Dynatrace

* Разрешения:

  + Для запросов к полученным данным: `storage:security.events:read`.
* Токены:

  + Сгенерируйте токен доступа с областью `openpipeline.events_security` и сохраните его для дальнейшего использования. Подробнее см. [Dynatrace API — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как получить аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace откройте [**Hub**](../../../manage/hub.md "Информация о Dynatrace Hub.").
2. Найдите **Microsoft Sentinel** и выберите **Install**.
3. Выберите **Set up**, затем выберите **Configure new connection**.
4. Следуйте инструкциям на экране для настройки приёма данных.
5. Проверьте конфигурацию, выполнив следующий запрос в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами на основе данных наблюдаемости в едином настраиваемом рабочем пространстве."):

   ```
   fetch security.events


   | filter dt.system.bucket == "default_securityevents"


   | filter event.provider=="Microsoft Sentinel"
   ```

## Подробности

### Как это работает

![Как это работает — MSFT Sentinel](https://dt-cdn.net/images/architecture-diagram-2065-c0e021b96c.png)

1. События принимаются в Dynatrace

1. Microsoft Sentinel экспортирует результаты безопасности в [Azure Event Hubs](https://dt-url.net/zmc3wv9).
2. Приложение [Azure Function](https://dt-url.net/b643w2v) предварительно обрабатывает события и отправляет их в Dynatrace, используя выделенный [эндпоинт приёма событий безопасности](ingest-custom-data.md#default "Приём событий безопасности от сторонних продуктов через API.") [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.").

2. Результаты безопасности обрабатываются и сохраняются в Grail

1. Полученные данные сопоставляются с [Семантическим словарём Dynatrace](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.").
2. Данные сохраняются в [Grail](../../../platform/grail.md "Информация о том, что и как вы можете запрашивать данные Dynatrace.") в унифицированном формате, в бакете по умолчанию `default_securityevents`. Подробнее см. [Встроенные бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.").

### Мониторинг данных

После приёма данных Microsoft Sentinel в Grail вы можете мониторить данные в приложении (в Dynatrace перейдите в **Settings**, затем найдите и выберите **Microsoft Sentinel**).

![overview-connection](https://dt-cdn.net/images/settings-dynatrace-microsoft-sentinel-3941-9844470c4c.png)

Вы можете просмотреть

* График принятых данных по всем существующим подключениям за определённый период

  + Доступные действия: [Запрос принятых данных](#query)
* Таблицу с информацией о ваших подключениях

  + Доступные действия: [Удаление подключения](#remove)

### Визуализация и анализ результатов

Вы можете создать собственные [дашборды](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и совместного использования данных наблюдаемости в реальном времени.") или использовать наши шаблоны для визуализации и анализа результатов уязвимостей контейнеров.

1. В **Settings** откройте **Microsoft Sentinel**.
2. В разделе **Try our templates** выберите нужный шаблон дашборда.

### Автоматизация и оркестрация результатов

Вы можете создать собственные [рабочие процессы](../../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.") или использовать наши шаблоны для автоматизации и оркестрации результатов уязвимостей контейнеров.

1. В **Settings** откройте **Microsoft Sentinel**.
2. В разделе **Try our templates** выберите нужный шаблон рабочего процесса.

### Запрос принятых данных

Вы можете запрашивать принятые данные в [**![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами на основе данных наблюдаемости в едином настраиваемом рабочем пространстве.") или [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../investigations.md "Объединяйте функциональные возможности Grail для расследований на основе фактов, включая разрешение инцидентов, анализ первопричин и поиск угроз."), используя формат данных из [Семантического словаря](https://dt-url.net/3q03pb0).

1. В **Settings** откройте **Microsoft Sentinel**.
2. Выберите **Open with**.
3. Выберите **Investigations** или **Notebooks**.

### Оценка, сортировка и расследование обнаруженных угроз

Вы можете оценивать, сортировать и расследовать обнаруженные угрозы с помощью [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../../threats-and-exploits.md "Анализируйте, сортируйте и расследуйте обнаруженные угрозы и оповещения.").

1. Откройте ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Отфильтруйте по **Provider** > **Microsoft Sentinel**.

### Удаление подключений

Чтобы прекратить отправку событий в Dynatrace:

1. В **Settings** откройте **Microsoft Sentinel**.
2. Для подключения, которое вы хотите удалить, выберите **Delete**.
3. Следуйте инструкциям на экране для удаления ресурсов. Если вы использовали значения, отличные от указанных в диалоге настройки, скорректируйте их соответственно.

Это удалит ресурсы Dynatrace, созданные для этой интеграции.

### Лицензирование и стоимость

Информацию о тарификации см. в разделе [Events powered by Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace, основанных на Grail, в рамках модели подписки Dynatrace Platform.").

## Часто задаваемые вопросы

### Какая модель данных используется для журналов безопасности и событий, поступающих из Microsoft Sentinel?

[События обнаружения угроз](../../../semantic-dictionary/model/security-events.md#detection-finding-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.") хранят индивидуальные результаты обнаружения для каждого затронутого объекта, представленного затронутым ресурсом Azure.

### Какие дополнительные поля добавляются к основным полям событий, принятых из Microsoft Sentinel?

* Пространство имён `actor` добавляется для хранения всех полей, связанных с субъектом угрозы, если они присутствуют в оповещении:

  + `actor.ips` — список IP-адресов подозрительного субъекта
  + `actor.fqdns` — список FQDN подозрительного субъекта
  + `actor.geo.country.name` — название страны подозрительного субъекта
  + `actor.geo.city.name` — название города подозрительного субъекта
* Пространство имён `azure` добавляется для хранения полей, связанных с Azure, в оповещении:

  + `azure.tenant.id` — идентификатор тенанта Azure
  + `azure.subscription` — идентификатор подписки Azure
  + `azure.resource.id` — идентификатор затронутого ресурса Azure
  + `azure.resource.group` — имя группы ресурсов Azure
  + `azure.resource.type` — тип ресурса Azure
  + `azure.resource.name` — имя ресурса Azure

### Как нормализуется оценка риска для результатов Microsoft Sentinel?

Dynatrace нормализует уровни серьёзности и оценки риска для всех результатов, принятых через текущую интеграцию. Это помогает вам последовательно приоритизировать результаты независимо от их источника.
Подробнее о работе нормализации см. в разделе [Нормализация серьёзности и оценки](../concepts.md#normalization "Основные концепции, связанные с наблюдаемостью угроз").

* `dt.security.risk.level` напрямую сопоставляется с уровнем серьёзности (`AlertSeverity`), установленным Microsoft Sentinel.
* `dt.security.risk.score` напрямую сопоставляется с уровнем серьёзности (`AlertSeverity`), установленным Microsoft Sentinel.

| `dt.security.risk.level` (сопоставление с `AlertSeverity`) | `dt.security.risk.score` (сопоставление с `AlertSeverity`) |
| --- | --- |
| High -> HIGH | High -> 8.9 |
| Medium -> MEDIUM | Medium -> 6.9 |
| Low -> LOW | Low -> 3.9 |
| Informational -> NONE | 0.0 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Посмотреть в Dynatrace Hub

Приём событий безопасности Microsoft Sentinel.](https://www.dynatrace.com/hub/detail/microsoft-sentinel)

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Использование Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.")
