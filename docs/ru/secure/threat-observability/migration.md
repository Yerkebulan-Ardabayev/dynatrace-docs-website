---
title: Руководство по миграции таблицы безопасности Grail
source: https://www.dynatrace.com/docs/secure/threat-observability/migration
scraped: 2026-03-05T21:34:18.947110
---

* Latest Dynatrace

Dynatrace вводит новую таблицу `security.events` в [Grail](../../platform/grail.md "Информация о том, что и как можно запрашивать в данных Dynatrace."), улучшая способ потребления, хранения и запросов данных событий безопасности. Это руководство объясняет преимущества, изменения в управлении доступом, изменения в импорте и запросах, а также необходимые действия пользователей.

Миграция на новую таблицу `security.events` должна быть завершена к концу декабря 2025 года. Чтобы предотвратить любые нарушения в ваших рабочих процессах, убедитесь, что миграция завершена до этого срока.

Обратитесь к данному руководству за подробными инструкциями по завершению перехода.

## Зачем выполнять миграцию?

Новая таблица `security.events` улучшает управление данными безопасности за счёт:

* **Упрощённых запросов событий безопасности** — вы можете напрямую получать события безопасности с помощью команды `fetch security.events` (см. [Примеры DQL для данных безопасности](dql-examples.md "Примеры DQL для данных безопасности на базе Grail.")).
* **Поддержки запросов без кода** — Dashboards и Notebooks позволяют анализировать события безопасности с помощью удобных фильтров, не требуя предварительных знаний DQL (см. [Исследование событий безопасности](../../analyze-explore-automate/dashboards-and-notebooks/explore-data.md#explore-security-events "Исследуйте свои данные с помощью нашего интерфейса.")).
* **Усиленного контроля доступа** — отдельные разрешения обеспечивают безопасность на уровне таблиц и записей без влияния на другие таблицы событий (см. [Разрешения в Grail](../../platform/grail/organize-data/assign-permissions-in-grail.md "Узнайте, как назначать разрешения бакетам и таблицам в Grail.")).
* **Улучшенной производительности запросов** — запросы сканируют только события безопасности, что снижает сложность и повышает эффективность.
* **Улучшенного импорта данных** — поддерживается встроенный вложенный JSON и введены специальные поля для доступа к необработанным данным событий.

## Что изменилось и что необходимо сделать

С введением таблицы `security.events` некоторые обновления происходят автоматически, а другие требуют ручных действий. Ниже приведён обзор.

### Автоматические обновления

* **Политики доступа к данным по умолчанию** — обновлены для включения событий безопасности.
* **Генерируемые Dynatrace события безопасности** — записываются в старую и новую таблицы до завершения миграции.
* **Предоставленные Dynatrace процессоры и конвейеры** — будут перенесены и будут работать без проблем с новой областью импорта.
* **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** и готовые примеры документации** — скорректированы для запросов к новой таблице событий безопасности.

### Необходимые ручные обновления

* **Пользовательские политики доступа** — обновите вручную для предоставления разрешений к новой таблице `security.events` (см. [Обновления контроля доступа](#access)).
* **URL-адреса импорта сторонних продуктов** — измените конечную точку импорта с `/events.security` на `/security.events` (см. [Обновления импорта данных](#data)).
* **Пользовательские конвейеры обработки** — выполните ручную миграцию источников через ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Security events** (см. [Обновления импорта данных](#data)).
* **Пользовательские запросы** — измените запросы DQL для обращения к `security.events` вместо `events` (см. [Обновления запросов DQL](#query)).
* **Миграция подключений для приложений/расширений интеграции** — если вы уже установили и настроили [интеграции безопасности](security-events-ingest.md#ingest "Импорт внешних данных безопасности в Grail."), необходимо выполнить одно из следующих действий:

  + Переконфигурировать URL-адрес стороннего продукта, указав `/security.events`. Это позволит существующим подключениям продолжить работу и отображать данные из новой таблицы.
  + Пересоздать подключения и следовать инструкциям на экране, которые уже включают обновлённую конечную точку.

## Обновления контроля доступа

* (Автоматически) Политики доступа по умолчанию обновляются автоматически:

  + `All Grail data read access` — чтение всех данных Grail, включая события безопасности.
  + `Read Security Events` — чтение только событий безопасности.
  + `OpenPipeline Ingest` — продолжение импорта событий безопасности с использованием существующих разрешений.
* (Вручную) Пользовательские политики требуют ручных изменений:

  + Новый вариант:

    ```
    // предыдущие события безопасности в таблице данных events


    ALLOW storage:buckets:read WHERE storage:bucket-name IN ("default_security_events", "default_security_custom_events");


    ALLOW storage:events:read;


    // новые разрешения для таблицы


    ALLOW storage:buckets:read WHERE storage:table-name = 'security.events';


    ALLOW storage:security.events:read;
    ```
  + Предыдущий вариант:

    ```
    ALLOW storage:buckets:read WHERE storage:bucket-name IN ("default_security_events", "default_security_custom_events");


    ALLOW storage:events:read;
    ```
* (Вручную) Для более детального контроля доступа используйте новые бакеты:

  + Чтение генерируемых Dynatrace событий:

    - Новый: `default_securityevents_builtin`
    - Предыдущий: `default_security_events`
  + Чтение импортированных извне событий:

    - Новый: `default_securityevents`
    - Предыдущий: `default_security_custom_events`

## Обновления импорта данных

Генерируемые Dynatrace события хранятся как в устаревшей, так и в новой таблице до завершения миграции. Однако события, связанные с [Kubernetes Security Posture Management](../../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Настройка и включение Security Posture Management в Kubernetes."), больше не дублируются и теперь доступны исключительно в новой таблице `security.events`. Все остальные генерируемые Dynatrace события продолжают записываться в обе таблицы в течение периода миграции.

* (Автоматически) Предоставленные Dynatrace процессоры и конвейеры работают без проблем с новой областью импорта.
* (Вручную) Обновите URL-адреса импорта сторонних продуктов:

  + Конвейер по умолчанию:

    - Новый: `/platform/ingest/v1/security.events`
    - Предыдущий: `/platform/ingest/v1/events.security`
  + Пользовательский конвейер:

    - Новый: `/platform/ingest/v1/security.events/<custom_ingest_source>`
    - Предыдущий: `/platform/ingest/v1/events.security/<custom_ingest_source>`

    Пример новых конвейеров по умолчанию и пользовательских

    Новые конвейеры по умолчанию и пользовательские через **Settings** > **Process and contextualize** > **OpenPipeline** > **Security events (New)**:

    ![settings-openpipeline-security-events](https://dt-cdn.net/images/custom-settings-openpipeline-security-events-3382-de1282230f.png)
* (Вручную) Выполните миграцию пользовательских источников импорта через ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Security events**.
* (Вручную) Скопируйте и при необходимости скорректируйте существующие пользовательские процессоры в ваших пользовательских конвейерах в новую область импорта `security.events` OpenPipeline.

## Обновления запросов DQL

* (Автоматически) ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** и готовые примеры документации, поставляемые с приложениями и расширениями Dynatrace, теперь обращаются к `security.events`.
* (Автоматически) Встроенные запросы в приложениях Dynatrace обновляются автоматически, где это применимо.
* (Вручную) Обновите ваши пользовательские запросы в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, чтобы запрашивать данные из `security.events` вместо `events`.

  + Для запроса только последних данных полностью переключитесь на запросы к `security.events`.
  + Для запроса как исторических, так и новых событий безопасности измените запросы для выборки из обеих таблиц.
  + Для запроса только исторических данных можно продолжать использовать старые запросы.

  Для массового обновления нескольких запросов в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** или ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** скачайте JSON-файл документа и используйте текстовый редактор для поиска и замены.

### Примеры обновления запросов

#### Запрос всех событий безопасности

* Новый:

```
fetch security.events
```

* Предыдущий:

```
fetch events | filter event.kind == "SECURITY_EVENT"
```

#### Запрос генерируемых Dynatrace событий

* Новый:

```
fetch security.events | filter dt.system.bucket=="default_securityevents_builtin"
```

* Предыдущий:

```
fetch events | filter dt.system.bucket=="default_security_events"
```

#### Запрос импортированных событий

* Новый:

```
fetch security.events | filter dt.system.bucket=="default_securityevents"
```

* Предыдущий:

```
fetch events | filter dt.system.bucket=="default_security_custom_events"
```

#### Запрос импортированных событий в старой и новой таблицах событий безопасности

```
// Получить все мигрированные события безопасности


fetch security.events


| filter dt.system.bucket!="default_securityevents_builtin"


| append [


// Получить все события безопасности, которые не были мигрированы


fetch events


| filter event.kind == "SECURITY_EVENT"


// Исключить генерируемые Dynatrace события безопасности, так как они записываются в обе таблицы


| filter dt.system.bucket!="default_security_events"


]
```
