---
title: Что нового в Dynatrace Managed версии 1.332
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-332
scraped: 2026-05-12T11:07:44.261845
---

# Что нового в Dynatrace Managed версии 1.332

# Что нового в Dynatrace Managed версии 1.332

* Заметки о выпуске
* 5-min read
* Updated on Apr 16, 2026
* Rollout start on Feb 16, 2026

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.332. Содержимое:

* [Обновления функций](#updates): 12
* [Несовместимые изменения](#breaking): 3
* [Исправления и обслуживание](#fixes): 8

## Обновления функций

Application Observability | Distributed Tracing

### Улучшенный опыт настройки мониторинга AWS Lambda

В этом выпуске представлен ряд улучшений удобства использования и надёжности рабочего процесса развёртывания Lambda, обеспечивающих согласованное поведение между типами развёртываний и предотвращающих распространённые ошибки настройки.

#### Автоматический выбор DT\_CONNECTION\_BASE\_URL с использованием ActiveGate

Для повышения надёжности и устранения ошибок настройки процесс развёртывания теперь автоматически определяет публичный **URL ActiveGate** в качестве `DT_CONNECTION_BASE_URL` при наличии такой возможности.

* Система автоматически выбирает доступный конечный пункт ActiveGate.
* URL кластера больше не используется как запасной вариант.

Это предотвращает проблемы соединения и обеспечивает корректную связь OneAgent.

**Если ActiveGate недоступен:**

* Вы получаете **чёткое, понятное сообщение об ошибке** с описанием проблемы.
* Необходимо вручную указать конечный пункт Dynatrace.
* Поле **Endpoint address** содержит встроенную подсказку с обновлёнными инструкциями.

#### Классическое поведение мониторинга Lambda для Managed-offline

* Классический мониторинг Lambda теперь **всегда включён**.
* Флажок **Enable Classic Lambda monitoring** **удалён** из интерфейса для предотвращения случайного отключения.
* Это обеспечивает непрерывность мониторинга без вмешательства Dynatrace ONE.

Application Observability | Distributed Tracing

### Улучшенная корреляция сервисов для триггеров обмена сообщениями AWS Lambda

Улучшена корреляция сервисов для триггеров обмена сообщениями в функциях AWS Lambda, отслеживаемых с помощью OneAgent AWS Lambda Layer.

Application Observability | Services

### Новая страница Services включена по умолчанию

Новая страница Service теперь включена по умолчанию во всех окружениях, чтобы вы могли воспользоваться новым дизайном и функциями анализа.

![Новая страница Service](https://dt-cdn.net/images/screenshot-2026-02-05-at-16-33-07-1621-548502a73b.png)

Новая страница Service

Application Security | Vulnerabilities

### Application Security теперь использует фид уязвимостей Dynatrace

В Dynatrace Managed версии 1.334 обнаружение уязвимостей сторонних компонентов будет обновлено для использования фида уязвимостей Dynatrace. Это обновление обеспечивает более точные, прозрачные и учитывающие угрозы данные об уязвимостях при сохранении широкого охвата критических рисков.

В рамках этого изменения небольшой процент ранее обнаруженных уязвимостей больше не будет охвачен и будет помечен как устаревший (deprecated). После переключения вы можете просмотреть эти элементы в обнаружении уязвимостей сторонних компонентов, используя фильтр **Status** > **Deprecated**.

FinOps

### Экспорт Cost Allocation теперь включает все возможности Dynatrace SaaS

Экспорт Cost Allocation теперь включает все возможности Dynatrace SaaS. Ранее экспорт включал только те возможности, которые настроены или уже поддерживаются функцией Cost Allocation.

Это обеспечивает полное представление стоимости и использования, позволяющее практикам FinOps работать с общими затратами на платформу независимо от текущей конфигурации или зрелости Cost Allocation.

Исторические данные доступны начиная с 26 января 2026 года.

Infrastructure Observability | Clouds

### Classic Cloud Platform Monitoring: новые метрики для Amazon CloudWatch и Azure Monitor

Следующие новые метрики теперь доступны для Amazon CloudWatch и Azure Monitor.

#### Azure DB for PostgreSQL — Flexible Server

| **Метрика** | **Отображаемое имя** | **Разрешение** | **Агрегации** |
| --- | --- | --- | --- |
| `client_connections_active` | Активные клиентские соединения | PT1M | Max, Min, Avg |
| `client_connections_waiting` | Ожидающие клиентские соединения | PT1M | Max, Min, Avg |
| `num_pools` | Количество пулов соединений | PT1M | Max, Min, Avg |
| `server_connections_active` | Активные серверные соединения | PT1M | Max, Min, Avg |
| `server_connections_idle` | Простаивающие серверные соединения | PT1M | Max, Min, Avg |
| `max_connections` | Максимальное количество соединений | PT30M | Max |
| `total_pooled_connections` | Общее количество соединений в пуле | PT1M | Max, Min, Avg |

Метрики пула соединений (`client_connections_*`, `num_pools`, `server_connections_*`, `total_pooled_connections`) разбиты по **DatabaseName** и **ServerName**; `max_connections` — только по **ServerName**.

#### Azure SQL Database — Hyperscale

| **Метрика** | **Отображаемое имя** | **Разрешение** | **Единица** | **Агрегации** |
| --- | --- | --- | --- | --- |
| `storage` | Использованное пространство данных | PT1M | Byte | Max, Min, Avg |

#### Amazon Aurora

| **Метрика** | **Отображаемое имя** | **Измерения** | **Единица** | **Статистики** |
| --- | --- | --- | --- | --- |
| `DBMaxConnections` | DB Cluster Max Connections (требуется: Database Insights Advanced и Performance Insights) | DBClusterIdentifier | Count | Multi |

#### Amazon RDS

| **Метрика** | **Отображаемое имя** | **Измерения** | **Единица** | **Статистики** |
| --- | --- | --- | --- | --- |
| `DBMaxConnections` | DB Instance Max Connections (требуется: Database Insights Advanced и Performance Insights) | DBInstanceIdentifier | Count | Multi |

Platform

### Запросы метрик могут включать значения удалённых сущностей

При ретроспективном запросе метрик некоторые отслеживаемые сущности могут быть недоступны и поэтому исключаются из результата. Это может приводить к неполному результату, особенно для метрик тарификации. Теперь можно использовать селектор сущностей, чтобы указать включение удалённых сущностей. Подробнее см. в разделе [Селектор сущностей — включение удалённых сущностей](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

Platform

### Добавлена поддержка PKCE для OpenID Connect

Dynatrace Managed теперь поддерживает PKCE (Proof Key for Code Exchange) для OpenID Connect. PKCE — расширение потока кода авторизации OAuth 2.0, предназначенное для предотвращения атак на перехват кода авторизации.

Для включения:

1. Перейдите в **CMC** > **User authentication** > **Single sign-on settings**.
2. Выберите **OpenID Connect** в качестве технологии SSO.
3. Включите **Use PKCE**.

![Функция PKCE для OpenID Connect](https://dt-cdn.net/images/screenshot-2026-02-05-at-16-44-29-1679-56b61f8202.png)

Функция PKCE для OpenID Connect

Platform

### Сворачивание панели настроек Data Explorer

Теперь можно свернуть панель настроек Data Explorer для освобождения места под диаграммы. Это особенно удобно на небольших экранах.

![Сворачивание панели настроек Data Explorer](https://dt-cdn.net/images/screenshot-2026-02-05-at-15-54-55-1481-ff94f6efd6.png)

Сворачивание панели настроек Data Explorer

Platform

### Новый параметр конфигурации для разграничения схожих отчётов о событиях

Теперь можно определить тег корреляции для всех источников событий: `dt.event.correlation_tag`. Этот необязательный тег позволяет явно создавать отдельные события даже при схожих данных отчёта о событии, например при одинаковых заголовке и сущности.

Подробнее см. в разделе [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.").

Platform | OneAgent

### OneAgent Health теперь включает атрибуты ресурсов

Теперь можно просматривать атрибуты ресурсов, захваченные кодовыми модулями, в [OneAgent Health](/managed/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems."). Для их просмотра выберите кодовый модуль в таблице данных и разверните раздел с подробностями.

Атрибуты ресурсов можно использовать в качестве входных данных для правил [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

![Атрибуты ресурсов OneAgent](https://dt-cdn.net/images/screenshot-2026-01-16-at-15-27-54-1953-b145ce28b5.png)

Атрибуты ресурсов OneAgent

Platform | OneAgent

### Мониторинг tmpfs через OneAgent доступен в режиме opt-in

Обновлён OneAgent: теперь он может отслеживать данные tmpfs в системах Linux. Мониторинг можно активировать в режиме opt-in в **Settings** > **Collect and capture** > **Infrastructure** > **OS** > **Enable tmpfs disk monitoring**.

## Несовместимые изменения

Platform

### Удалена обратная совместимость с ActiveGate старше версии 1.172

Начиная с ActiveGate версии 1.172, все ActiveGate поддерживают приоритизированные списки конечных пунктов. Для снижения сложности продукта поддержка неприоритизированных списков конечных пунктов прекращена.

Если вы всё ещё используете ActiveGate версий ниже 1.172, необходимо обновить их до поддерживаемой версии.

Platform

### Имя локального окружения самомониторинга больше нельзя изменять

Для улучшения поддержки Dynatrace кластеров Managed имя локального окружения самомониторинга установлено как «Local Self-Monitoring» и больше не может быть изменено через Cluster Management Console.

Если имя локального окружения самомониторинга было изменено ранее, оно будет сброшено до «Local-Self-Monitoring».

Platform

### Прекращение поддержки нативных мобильных приложений (iOS и Android) для Dynatrace

В рамках непрерывного стремления обеспечить оптимизированный и последовательный пользовательский опыт Dynatrace прекращает поддержку нативных мобильных приложений для iOS и Android. Это изменение соответствует стратегии единого адаптивного веб-интерфейса и использования современных гибких каналов уведомлений.

#### Ключевые даты

* **Последнее обновление приложения**: конец 2025 года
* **Дата прекращения поддержки**: June 30, 2026
* **Завершение поддержки**: June 30, 2026

#### Что изменится?

Нативные мобильные приложения Dynatrace перестанут быть доступны для загрузки и поддерживаться после даты прекращения поддержки.

Push-уведомления теперь будут доставляться через сторонние интеграции: Slack, Teams, PagerDuty, электронную почту и ntfy.

#### Рекомендуемые действия

* Начните использовать адаптивный веб-интерфейс.
* Настройте предпочтительные интеграции уведомлений через:

  + Dynatrace SaaS: [Workflows](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
  + Dynatrace Managed: [Уведомления о проблемах](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.")
* Удалите нативное приложение с устройств после даты прекращения поддержки.

## Исправления и обслуживание

### Исправленные ошибки в этом выпуске

* Исправлена проблема, при которой повторное открытие глобального переключателя временного диапазона приводило к дублированию строк часового пояса. (MGD-9441)
* Обновлена библиотека log4j для CVE-2025-68161 во избежание ложных срабатываний в сканерах безопасности. Сервер Dynatrace не подвержен этой уязвимости CVE. (MGD-9264)
* Исправлена проблема с модулем проверки работоспособности NGINX, отвечающим за перенаправление трафика между узлами кластера. (MGD-9000)
* **Уязвимость**: Введены дополнительные средства контроля доступа для внутреннего конечного пункта Hub API, маршрутизируемого через обратный прокси Mission Control. (ASDY-3035)

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.332](/managed/whats-new/dynatrace-api/sprint-332 "Changelog for Dynatrace API version 1.332")
* [Журнал изменений Dynatrace API версии 1.331](/managed/whats-new/dynatrace-api/sprint-331 "Changelog for Dynatrace API version 1.331")

## Поддержка операционных систем

### Предстоящие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы перестанут поддерживаться с 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление поставщика](https://www.suse.com/lifecycle/)

##### Следующие операционные системы перестанут поддерживаться с 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление поставщика](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы перестанут поддерживаться с 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление поставщика](https://aws.amazon.com/linux/)

### Прошедшие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы больше не поддерживаются с 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Объявление поставщика](https://wiki.debian.org/DebianReleases)