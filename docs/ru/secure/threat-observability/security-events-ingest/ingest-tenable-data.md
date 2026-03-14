---
title: Прием результатов уязвимостей, событий сканирования и журналов аудита Tenable
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-tenable-data
scraped: 2026-03-06T21:23:59.180814
---

# Приём результатов анализа уязвимостей, событий сканирования и журналов аудита Tenable

# Приём результатов анализа уязвимостей, событий сканирования и журналов аудита Tenable

* Latest Dynatrace
* Расширение
* Обновлено 30 сентября 2025 г.

Эта страница обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для миграции, см. в [руководстве по миграции на таблицу безопасности Grail](../migration.md "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Приём результатов анализа уязвимостей, событий сканирования и журналов аудита Tenable в Dynatrace в качестве событий безопасности.

## Начало работы

### Обзор

[Tenable](https://dt-url.net/2o23xof) предоставляет надёжные решения для идентификации, приоритизации и устранения уязвимостей, что критически важно для снижения киберрисков и защиты цифровой инфраструктуры. Интеграция результатов Tenable в Dynatrace повышает общий уровень безопасности за счёт обеспечения комплексной видимости и упрощённого управления уязвимостями.

### Сценарии использования

С помощью принятых данных вы можете реализовать различные сценарии, такие как:

* [Визуализация и анализ результатов безопасности](../../use-cases/visualize-and-analyze-security-findings.md "Визуализация, приоритизация и анализ принятых результатов безопасности.")
* [Обнаружение пробелов в охвате результатов безопасности](../../use-cases/discover-coverage-gaps-in-security-scans.md "Выявление слепых зон в жизненном цикле разработки программного обеспечения (SDLC).")
* [Автоматизация и оркестрация результатов безопасности](../../use-cases/automate-and-orchestrate-security-findings.md "Регулярная проверка критических результатов безопасности и автоматическое создание тикетов Jira или уведомлений Slack.")

### Требования

#### Поддерживаемые продукты Tenable

* [Tenable Vulnerability Management](https://dt-url.net/fy43w0l) (для уязвимостей и событий сканирования)
* [Tenable Web App Scanning](https://dt-url.net/og63xed) (для уязвимостей и событий сканирования)
* [Tenable One](https://dt-url.net/c703wbm) (для журналов аудита)

  (скоро будут добавлены новые)

#### Требования Tenable

* [Сгенерируйте ключ доступа и секретный ключ API](https://dt-url.net/77i3w5n) со следующими ролями:

  + **Basic** для управления уязвимостями и сканирования веб-приложений

    Для получения полных деталей сканирования убедитесь, что настроенный API-ключ имеет доступ на чтение сканирований и истории сканирований. Подробности о требуемых API см. в разделе [API, используемые для получения данных](#apis).
  + **Administrator** или **Custom** для журналов аудита

  Подробности см. в [Роли и привилегии, предоставляемые Tenable](https://dt-url.net/rv63woq).

#### Требования Dynatrace

* ActiveGate версии 1.299+
* Разрешения:

  + Для запуска ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: перейдите в **Hub**, выберите ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** и откройте **Technical information**.
  + Для запросов к принятым данным: `storage:security.events:read`.
* Токены:

  + Сгенерируйте токен доступа с областью `openpipeline.events_security` и сохраните его для дальнейшего использования. Подробности см. в [Dynatrace API — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace найдите **Tenable** и выберите **Install**.
2. Следуйте инструкциям на экране для настройки расширения.
3. Проверьте конфигурацию, выполнив следующие запросы в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализ, визуализация и обмен данными наблюдаемости."):

   * Для уязвимостей и сканирований активов:

     ```
     fetch security.events



     | filter dt.system.bucket=="default_securityevents"



     | filter event.provider == "Tenable"
     ```
   * Для журналов аудита:

     ```
     fetch logs



     | filter log.source == "Tenable"
     ```
4. После установки и успешной работы расширения вы можете получить к нему доступ и управлять им в Dynatrace через ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. Подробности см. в [О расширениях](../../../ingest-from/extensions/concepts.md "Узнайте больше о концепции расширений Dynatrace.").

Теперь вы можете [визуализировать результаты](#visualize), [анализировать журналы аудита](#analyze) и [автоматизировать уведомления](#automate).

## Подробности

### Как это работает

![Как работает интеграция с Tenable](https://dt-cdn.net/images/2024-12-18-16-47-03-1173-dd965318f4.png)

Интеграция Dynatrace с Tenable — это [расширение](../../../ingest-from/extensions.md "Узнайте, как создавать и управлять расширениями Dynatrace."), работающее на Dynatrace ActiveGate. После включения и настройки расширения Dynatrace Tenable:

1. Оно периодически обращается к продуктам Tenable и получает новые результаты, сканирования и журналы аудита из [API Tenable](#apis).

   API, используемые для получения данных

   * API для управления уязвимостями:

     + [Экспорт активов](https://dt-url.net/6c23wk1)
     + [Список сканирований](https://dt-url.net/qr43wwo)
     + [Список истории сканирований](https://dt-url.net/ph63wgp)
     + [Получение деталей сканирования](https://dt-url.net/bs83wh5)
     + [Получение деталей актива](https://dt-url.net/j0a3w41)
     + [Экспорт уязвимостей](https://dt-url.net/hac3w16)
   * API для журналов аудита:

     + [Просмотр журнала активности](https://dt-url.net/dse3wjb)
   * API для сканирования веб-приложений:

     + [Поиск конфигураций сканирования](https://dt-url.net/ig03xj1)
     + [Поиск сканирований](https://dt-url.net/fi23xnz)
     + [Экспорт результатов](https://dt-url.net/c443xfn)
2. Полученные данные принимаются в Dynatrace и сопоставляются с [семантическим словарём Dynatrace](https://dt-url.net/z1c3xsm).
3. Данные хранятся в бакете `default_securityevents` (подробности см. в [Встроенные бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.")).

### Визуализация

1. Откройте ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** и перейдите к **Tenable**.
2. В разделе **Extension content** выберите нужный [готовый дашборд](../../../analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-dashboards.md "Используйте готовые дашборды для визуализации данных.").
3. В фильтре **Product** выберите **Tenable**, чтобы просмотреть данные, предоставленные Tenable, такие как критические уязвимости и затронутые объекты.

   ![Фильтр по продукту Tenable](https://dt-cdn.net/images/2024-12-11-20-34-24-686-e8338d8bd3.png)

Пример результата:

![Дашборд с фильтром Tenable](https://dt-cdn.net/images/umsaywsjuo-4308-76ecd2e8b2.png)

### Анализ

Откройте [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализ, визуализация и обмен данными наблюдаемости.") или [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../investigations.md "Комбинация функций Grail для расследований на основе доказательств.") для [запроса](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.") принятых данных, используя формат данных из [семантического словаря](https://dt-url.net/3q03pb0).

Примеры построения запросов приведены ниже.

#### Запрос логов по времени и действиям

```
fetch logs



| filter log.source == "Tenable"



| makeTimeseries logs=countDistinctExact(id), by:{audit.action}, time:{toTimestamp(received)}, interval:{3h}
```

Пример результата:

![Логи по времени и действиям](https://dt-cdn.net/images/image-20241209-153005-1988-af39449c8c.png)

#### Запрос распределения уязвимостей по уровню риска

```
fetch security.events



| filter dt.system.bucket=="default_securityevents"



| filter event.type == "VULNERABILITY_FINDING"



| filter event.provider == "Tenable"



| dedup {object.id, vulnerability.id}, sort:{timestamp}



| summarize Vulnerabilities=countDistinctExact(vulnerability.id), by:{dt.security.risk.level}



| fieldsAdd order=if(dt.security.risk.level=="CRITICAL", 1, else:



if(dt.security.risk.level=="HIGH", 2, else:



if(dt.security.risk.level=="MEDIUM", 3, else:



if(dt.security.risk.level=="LOW", 4, else:5))))



| sort order asc
```

Пример результата:

![Распределение уязвимостей по уровню риска](https://dt-cdn.net/images/2024-12-11-19-40-07-1277-3f2f43c90a.png)

#### Запрос топ-10 сканирований с наибольшим охватом хостов

```
fetch security.events



| filter dt.system.bucket=="default_securityevents"



| filter event.type == "VULNERABILITY_SCAN"



| filter event.provider == "Tenable"



| dedup {object.id, scan.id}



| summarize Hosts=countDistinctExact(object.id), by:{scan.name}



| sort Hosts desc



| limit 10
```

Пример результата:

![Запрос топ-10 сканирований с наибольшим охватом хостов](https://dt-cdn.net/images/2024-12-11-19-42-02-1753-871fb9630c.png)

### Автоматизация уведомлений

1. Скачайте [пример рабочего процесса для Jira](https://dt-url.net/od23qa1) или [пример рабочего процесса для Slack](https://dt-url.net/ko43qsm).
2. Откройте [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../../analyze-explore-automate/workflows.md "Автоматизация IT-процессов с помощью Dynatrace Workflows."), выберите ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, затем выберите скачанный файл.
3. Настройте рабочий процесс под ваши потребности для создания уведомлений о критических результатах Tenable.

### Лицензирование и стоимость

Информацию о тарификации см. в [События на базе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail в модели подписки Dynatrace Platform.").

## Наборы функций

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) вы можете ограничить мониторинг одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут отражать сегменты вашей среды. Затем, при создании конфигурации мониторинга, вы можете выбрать набор функций и соответствующую группу ActiveGate, которая может подключаться к конкретному сегменту.

Все метрики, не отнесённые ни к одному набору функций, считаются набором по умолчанию и передаются всегда.

Метрика наследует набор функций подгруппы, которая, в свою очередь, наследует набор функций группы. Набор функций, определённый на уровне метрики, имеет приоритет над набором функций подгруппы, который, в свою очередь, имеет приоритет над набором функций группы.

## Часто задаваемые вопросы

### Почему моя конфигурация показывает ошибку?

Сообщение об ошибке: `Failed to assign monitoring configuration to ActiveGate. Reason: Extension com.dynatrace.extension.tenable(<version-number>) not available in cache yet (queued for download)`

Если ваша конфигурация показывает указанное выше сообщение об ошибке, это просто означает, что ActiveGate всё ещё загружает расширение для кластера. Статус должен измениться через несколько минут.

### Почему я вижу дублирующиеся события?

Дублирующиеся события в расширении Tenable, скорее всего, связаны с тем, что первый приём запускается несколько раз. Когда конфигурация мониторинга назначается ActiveGate, первое выполнение запускает экспорт за более длительный временной период (настраивается в параметрах конфигурации мониторинга). Каждый раз при перезапуске расширения (из-за обновления, сброса ActiveGate, переключения на резерв и т.д.) первый приём запускается снова.

Вы можете выполнить DQL-запрос и применить [**dedup**](../../../platform/grail/dynatrace-query-language/commands/filtering-commands.md#dedup "Команды фильтрации и поиска DQL") к событиям, используя поля `object.id`, `scan.id` и `finding.id`.

* Для `VULNERABILITY_FINDING` уникальный идентификатор — `{object.id, finding.id}`.
* Для `VULNERABILITY_SCAN` уникальный идентификатор — `{object.id, scan.id}`.

Пример:

```
fetch security.events



| filter dt.system.bucket=="default_securityevents"



| filter event.type == "VULNERABILITY_FINDING"



| filter event.provider == "Tenable"



| dedup {object.id, finding.id}, sort:{timestamp}
```

### Почему некоторые события сканирования имеют одинаковое время начала и окончания?

При получении уязвимостей расширение Tenable пытается сопоставить данные с недавними выполнениями сканирования. Если сканирование, упомянутое в уязвимости Tenable, не может быть найдено (например, из-за отсутствия разрешений), расширение создаёт событие сканирования на основе этого результата. Такие события сканирования имеют одинаковое время начала и окончания — момент обнаружения уязвимости.

### Почему мои данные не принимаются?

Если вы установили и настроили расширение, но данные не принимаются, выполните следующие шаги.

1. Откройте расширение и перейдите в **Health**, чтобы проверить статус конфигурации мониторинга.
2. Если статус не `OK`, прокрутите вниз до **Logs** и выберите **Run query**, чтобы увидеть информацию об ошибке.
3. Если информации об ошибке недостаточно, или статус показывает `OK`, но данные по-прежнему не поступают, извлеките архив поддержки из ActiveGate для дальнейшего устранения неполадок.

   Как извлечь архив поддержки

   1. Найдите идентификатор ActiveGate для ActiveGate, выполняющего конфигурацию, и извлеките архив поддержки. Подробности см. в [Диагностика ActiveGate: локальный сбор и анализ](../../../ingest-from/dynatrace-activegate/activegate-diagnostics.md#collect-and-review-locally "Узнайте, как запустить диагностику ActiveGate").
   2. Распакуйте архив поддержки и найдите файл лога расширения по пути `COLLECTOR/<id>/remotepluginmodule/log/extensions/datasources/com.dynatrace.extension.tenable/python3.log`.
4. Если информации по-прежнему недостаточно для устранения неполадок, включите флаг `Debug logs` в конфигурации мониторинга и обратитесь в службу поддержки Dynatrace.

Распространённые причины отсутствия приёма данных:

* Нет связи между ActiveGate и облаком Tenable

  **Рекомендация**: попробуйте выполнить curl-запрос к URL облака Tenable с ActiveGate, чтобы убедиться в наличии связи.
* Неправильный ключ доступа и/или секретный ключ

  **Рекомендация**: дважды проверьте учётные данные, настроенные в конфигурации мониторинга.
* Недостаточные разрешения у пользователя API

  **Рекомендация**: убедитесь, что пользователь API может вызывать [API, используемые для получения данных](#apis).

## Какие поля расширения добавляются поверх основных полей событий, принятых из Tenable?

Пространство имён `tenable` добавляется для извлечения нескольких специфических атрибутов Tenable для удобства пользователей поверх исходного JSON, который хранится в поле `event.original_content`.

**Примеры**:

* `tenable.vpr`
* `tenable.last_found`
* `tenable.first_found`
* `tenable.last_fixed`

## Какие типы активов Tenable поддерживаются Dynatrace для контекстуализации во время выполнения?

`HOST` — все результаты из Tenable Vulnerability Management, полученные при сканировании хостов, сопоставляются со значением `HOST` в поле `object.type`, и добавляется пространство имён `host` с соответствующими полями:

* `host.name` — имя хоста, определённое Tenable.
* `host.ip` — IP-адрес хоста, просканированный Tenable.
* `host.fqdn` — полное доменное имя хоста, определённое Tenable.

Контекстуализация во время выполнения может быть выполнена по полю `host.ip`.

### Как нормализуется оценка риска для результатов Tenable?

Dynatrace нормализует степень серьёзности и оценки риска для всех результатов, принятых через текущую интеграцию. Это помогает приоритизировать результаты единообразно, независимо от их источника.
Подробности о том, как работает нормализация, см. в [Нормализация серьёзности и оценок](../concepts.md#normalization "Основные концепции, связанные с наблюдаемостью угроз").

Уровни и оценки риска Dynatrace сопоставляются с исходной [серьёзностью Tenable](https://dt-url.net/j103w2v).

Tenable использует оценку VPR. Однако уровни серьёзности устанавливаются на основе оценок CVSS (v2 или v3, в зависимости от [конфигурации](https://dt-url.net/tg23we5)). Поэтому Dynatrace сопоставляет серьёзность с уровнем риска, а затем назначает соответствующую оценку риска.

* `dt.security.risk.level` берётся из уровня серьёзности Tenable и сопоставляется с исходными значениями в `finding.severity`.
* `dt.security.risk.score` сопоставляется с уровнем риска по набору статических оценок.

| `dt.security.risk.level` (сопоставлено из `finding.severity`) | `dt.security.risk.score` (сопоставлено из `dt.security.risk.level`) |
| --- | --- |
| critical -> CRITICAL | 10.0 |
| high -> HIGH | 8.9 |
| medium -> MEDIUM | 6.9 |
| low -> LOW | 3.9 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследуйте в Dynatrace Hub

Приём результатов анализа уязвимостей, событий сканирования и журналов аудита Tenable.](https://www.dynatrace.com/hub/detail/tenable/)

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.")
