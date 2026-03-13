---
title: Ingest Microsoft Defender for Cloud security events
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-defender
scraped: 2026-03-06T21:24:00.859946
---

# Приём событий безопасности Microsoft Defender for Cloud

# Приём событий безопасности Microsoft Defender for Cloud

* Последняя версия Dynatrace
* Практическое руководство
* Обновлено 7 октября 2025 г.

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, см. в [руководстве по миграции таблицы безопасности Grail](/docs/secure/threat-observability/migration "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Принимайте события безопасности Microsoft Defender for Cloud и анализируйте их в Dynatrace.

## Начало работы

### Обзор

Интеграция Dynatrace с [платформой CNAPP Microsoft Defender for Cloud](https://dt-url.net/so23wzy) позволяет пользователям объединять и контекстуализировать результаты обнаружения уязвимостей из различных инструментов и продуктов DevSecOps, обеспечивая централизованную приоритизацию, визуализацию и автоматизацию результатов безопасности.

В первой версии этой интеграции мы предоставляем [оценку уязвимостей](https://dt-url.net/jt43w8r) образов контейнеров (часть [плана Microsoft Defender for Containers](https://dt-url.net/vm63w5d)) на базе возможностей [Microsoft Defender Vulnerability Management](https://dt-url.net/c483wfr).

### Варианты использования

* Визуализация и отчётность о текущем состоянии безопасности и тенденциях результатов безопасности в различных средах с помощью [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.").
* Анализ и приоритизация результатов безопасности из нескольких инструментов и продуктов единообразно с помощью [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.").
* Создание уведомлений и заявок для критических результатов безопасности с помощью [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.").
* Использование результатов безопасности как дополнительного измерения для поиска угроз и анализа инцидентов с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Сочетайте возможности Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.").

### Требования

Ниже приведены требования для Microsoft Defender for Cloud и Dynatrace.

#### Требования Microsoft Defender for Cloud

* [Включите оценку уязвимостей на базе Microsoft Defender Vulnerability Management](https://dt-url.net/nx63wk0)
* Установите [Azure CLI](https://dt-url.net/yb43whw).

#### Требования Dynatrace

* Разрешения:

  + Для запроса принятых данных: `storage:security.events:read`.
* Токены:

  + Сгенерируйте токен доступа с областью действия `openpipeline.events_security` и сохраните его. Подробнее см. в разделе [API Dynatrace — токены и аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования API Dynatrace.").

## Активация и настройка

1. В Dynatrace откройте  [**Hub**](/docs/manage/hub "Информация о Dynatrace Hub.").
2. Найдите **Microsoft Defender for Cloud** и выберите **Install**.
3. Выберите **Set up**, затем выберите  **Configure new connection**.
4. Следуйте инструкциям на экране для настройки приёма данных.

## Подробности

### Как это работает

![как это работает](https://dt-cdn.net/images/image-20250306-160951-3063-719dabfeb2.png)

1. События принимаются в Dynatrace

1. Microsoft Defender for Cloud [непрерывно экспортирует](https://dt-url.net/lla3wnv) результаты безопасности в [Azure Event Hubs](https://dt-url.net/zmc3wv9).
2. Приложение [Azure Function](https://dt-url.net/b643w2v) предварительно обрабатывает события и отправляет их в Dynatrace, используя [OpenPipeline](/docs/platform/openpipeline "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.") и специальную [конечную точку приёма событий безопасности](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data#default "Принимайте события безопасности из пользовательских сторонних продуктов через API.").

2. Результаты безопасности обрабатываются и сохраняются в Grail

1. Полученные данные сопоставляются с [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Познакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.").
2. Данные хранятся в [Grail](/docs/platform/grail "Информация о том, какие данные и как вы можете запрашивать в Dynatrace.") в унифицированном формате, в корзине по умолчанию `default_securityevents`. Подробнее см. в разделе [Встроенные корзины Grail](/docs/platform/grail/organize-data#built-in-grail-buckets "Информация о модели данных Grail, состоящей из корзин, таблиц и представлений.").

### Мониторинг данных

После приёма данных Microsoft Defender for Cloud в Grail вы можете мониторить свои данные в приложении (в Dynatrace перейдите в **Settings**, затем найдите и выберите **Microsoft Defender for Cloud**).

![msftdefender](https://dt-cdn.net/images/2025-06-05-11-31-30-1437-f22714114f.png)

Вы можете просматривать

* График принятых данных из всех существующих подключений за период

  + Доступные действия: [Запрос принятых данных](#query)
* Таблицу с информацией о ваших подключениях

  + Доступные действия: [Удаление подключения](#remove)

### Визуализация и анализ результатов

Вы можете создавать собственные [дашборды](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") или использовать наши шаблоны для визуализации и анализа результатов обнаружения уязвимостей контейнеров.

1. В **Settings** откройте **Microsoft Defender for Cloud**.
2. В разделе **Try our templates** выберите нужный шаблон дашборда.

### Автоматизация и оркестрация результатов

Вы можете создавать собственные [рабочие процессы](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.") или использовать наши шаблоны для автоматизации и оркестрации результатов обнаружения уязвимостей контейнеров.

1. В **Settings** откройте **Microsoft Defender for Cloud**.
2. В разделе **Try our templates** выберите нужный шаблон рабочего процесса.

### Запрос принятых данных

Вы можете запрашивать принятые данные в [**![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") или [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Сочетайте возможности Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз."), используя формат данных из [Semantic Dictionary](https://dt-url.net/3q03pb0).

1. В **Settings** откройте **Microsoft Defender for Cloud**.
2. Выберите **Open with** .
3. Выберите **Investigations** или **Notebooks**.

### Оценка, сортировка и расследование результатов обнаружения

Вы можете оценивать, сортировать и расследовать результаты обнаружения с помощью [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Понимание, сортировка и расследование результатов обнаружения и оповещений.").

1. Откройте ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Отфильтруйте по **Provider** > **Microsoft Defender for Cloud**.

### Удаление подключений

Чтобы прекратить отправку событий в Dynatrace

1. В **Settings** откройте **Microsoft Defender for Cloud**.
2. Для подключения, которое вы хотите удалить, выберите  **Delete**.
3. Следуйте инструкциям на экране для удаления ресурсов. Если вы использовали значения, отличные от указанных в диалоге настройки, скорректируйте их соответствующим образом.

Это удаляет ресурсы Dynatrace, созданные для этой интеграции.

### Лицензирование и стоимость

Информацию о тарификации см. в разделе [События на базе Grail](/docs/license/capabilities/events "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail с использованием модели подписки Dynatrace Platform.").

## Часто задаваемые вопросы

### Какая модель данных используется для логов и событий безопасности, поступающих из Microsoft Defender for Cloud?

* [События обнаружения уязвимостей](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Познакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.") хранят отдельные результаты обнаружения уязвимостей, о которых сообщает Microsoft Defender for Cloud для каждого образа контейнера и компонента.
* [**События сканирования уязвимостей**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Познакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.") указывают охват сканирований для отдельных образов контейнеров.

### Какие поля расширений добавляются к событиям, принятым из Microsoft Defender for Cloud?

Пространство имён `container_image` добавляется для хранения всей информации, связанной с образами контейнеров, со следующими полями:

* `container_image.digest` представляет дайджест образа контейнера; это значение может использоваться для сопоставления с контейнерами во время выполнения
* `container_image.repository` представляет имя репозитория контейнера
* `container_image.registry` представляет имя реестра контейнеров
* `container_image.tags` представляет помеченные версии образов контейнеров

### Какие типы активов Microsoft Defender for Cloud поддерживаются Dynatrace для контекстуализации среды выполнения?

`CONTAINER_IMAGE`: Все результаты из Microsoft Defender for Cloud генерируются при оценке уязвимостей образов контейнеров с установленным значением `CONTAINER_IMAGE` в поле `object.type`, и добавляется пространство имён `container_image`.

### Как мы нормализуем оценку рисков для результатов Microsoft Defender for Cloud?

Dynatrace нормализует уровни серьёзности и оценки рисков для всех результатов, принятых через текущую интеграцию. Это помогает вам приоритизировать результаты единообразно, независимо от их источника.
Подробнее о работе нормализации см. в разделе [Нормализация серьёзности и оценки](/docs/secure/threat-observability/concepts#normalization "Основные концепции, связанные с наблюдаемостью угроз").

* `dt.security.risk.level` сопоставляется непосредственно из уровня серьёзности, установленного Microsoft Defender for Cloud.
* `dt.security.risk.score` сопоставляется непосредственно из оценки серьёзности, установленной Microsoft Defender for Cloud.

| `dt.security.risk.level` (сопоставлено из `finding.severity`) | `dt.security.risk.score` (сопоставлено из `finding.score`) |
| --- | --- |
| Critical -> CRITICAL | 9.0-10.0 |
| High -> HIGH | 7.0-8.9 |
| Medium -> MEDIUM | 4.0-6.9 |
| Low -> LOW | 0.1-3.9 |
| Unknown, None -> NONE | 0.0 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучите в Dynatrace Hub

Принимайте результаты безопасности и события сканирования Microsoft Defender for Cloud.](https://www.dynatrace.com/hub/detail/microsoft-defender-for-cloud)

## Связанные темы

* [OpenPipeline](/docs/platform/openpipeline "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [События безопасности](/docs/semantic-dictionary/model/security-events "Познакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.")
