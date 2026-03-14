---
title: Права доступа в Grail
source: https://www.dynatrace.com/docs/platform/grail/organize-data/assign-permissions-in-grail
scraped: 2026-03-06T21:13:24.120446
---

# Разрешения в Grail


* Latest Dynatrace
* Практическое руководство
* Чтение: 10 мин
* Обновлено 26 января 2026 г.

Разрешения могут быть назначены на уровне бакета, таблицы, записи и поля. Без разрешений ваши пользователи не смогут запрашивать данные из Grail.

![Логика разрешений бакетов и таблиц](https://dt-cdn.net/images/new-bucket-and-table-permissions-diagram-1991-07901aebd8.png)

## Настройка разрешений

Чтобы настроить разрешения на уровне бакета и таблицы:

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/). Если у вас несколько аккаунтов, выберите нужный.
2. Перейдите в **Identity & access management** > **Policy management**.
3. Выберите **Create policy**.
4. Добавьте данные политики:

   * **Name**
   * **Description**
   * **Policy statement** — используйте следующий формат:

     ```
     ALLOW storage:buckets:read WHERE <conditions>;


     ALLOW <table permission> WHERE <conditions>;
     ```

   Ниже приведены поддерживаемые разрешения для бакетов и таблиц.
5. Выберите **Create policy**.

## Разрешения для бакетов

Все разрешения для бакетов должны начинаться с `storage:buckets:read`. Их область можно ограничить с помощью оператора `WHERE`, который включает один из следующих операторов:

* `=` — проверка на равенство.
* `STARTSWITH` — проверка на префикс.
* `IN` — проверка на равенство для любого значения из списка.
* `MATCH` — проверка на соответствие шаблону для любого шаблона из списка. Обобщает и расширяет операторы `STARTSWITH` и `IN`.

После оператора `WHERE` вы можете фильтровать результаты, указав бакеты или таблицы:

* WHERE storage:bucket-name
* WHERE storage:table-name

Приведённый ниже пример показывает, как включить только бакеты с префиксом `default_` или бакет `common_logs`.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("default_*", "common_logs");
```

Подробнее см. в [Справочнике политик IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#storage "Полный справочник по политикам IAM и соответствующим условиям для всех сервисов Dynatrace.").

### Включённые запросы

Только для логов

Это применимо только при наличии `Log Management & Analytics - Retain with Included Queries` в вашем тарифном плане.

Включённые запросы

Подробнее о сохранённых данных логов и данных логов включённых запросов см. в [Retain with Included Queries](../../../license/capabilities/log-analytics.md#log-retain-included-queries "Узнайте, как рассчитывается потребление Dynatrace Log Analytics.").

Разрешения для бакетов позволяют определить доступ групп пользователей к:

* Всем сохранённым данным логов.
  Запросы могут генерировать потребление `Log Management & Analytics - Query`.
* Только данным логов включённых запросов.
  Запросы не будут генерировать дополнительное потребление `Log Management & Analytics - Query`.

Для определения доступа используется условие `storage:query-consumption`.
Это условие имеет два возможных значения:

* `ON_DEMAND`: запросы могут сканировать все сохранённые данные.
  Это значение по умолчанию: если не указано, пользователи имеют доступ ко всем сохранённым данным.
* `INCLUDED`: запросы могут сканировать только данные включённых запросов.

Это можно комбинировать с условием `storage:bucket-name` для ограничения доступа на уровне отдельных бакетов.

Примеры использования

Следующие примеры описывают, как использовать разрешения для бакетов, чтобы предоставить доступ к:

* Данным включённых запросов во всех бакетах.

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="INCLUDED";
  ```
* Данным включённых запросов в конкретном бакете (`common_logs`).

  ```
  ALLOW storage:buckets:read WHERE storage:bucket-name="common_logs" AND storage:query-consumption="INCLUDED";
  ```
* Данным включённых запросов во всех бакетах и дополнительно ко всем сохранённым данным в конкретном бакете (`common_logs`).

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="INCLUDED";


  ALLOW storage:buckets:read WHERE storage:bucket-name="common_logs" AND storage:query-consumption="ON_DEMAND";
  ```
* Всем сохранённым данным во всех бакетах.

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="ON_DEMAND";
  ```

  или

  ```
  ALLOW storage:buckets:read;
  ```

## Разрешения для таблиц

Помимо предоставления доступа к бакетам, необходимо также настроить разрешения для таблиц.

Подробнее см. в [Справочнике политик IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#storage "Полный справочник по политикам IAM и соответствующим условиям для всех сервисов Dynatrace.").

### Разрешения на уровне бакета

Вы можете ограничить разрешения таблиц определёнными бакетами с помощью оператора `WHERE`. Например:

```
ALLOW storage:logs:read WHERE storage:bucket-name="default_logs";
```

### Разрешения на уровне записей

Вы можете определить детализированные разрешения для записей, хранящихся в Grail. Разрешения добавляются к существующим разрешениям таблиц с помощью оператора `WHERE`. Например:

```
ALLOW storage:logs:read WHERE storage:dt.security_context="TeamA";
```

Поддерживаемые поля:

Для деталей, которые недоступны в виде выделенного поля, задайте поле `dt.security_context` либо в источнике данных, либо в пайплайне обработки.

### Комбинирование разрешений на уровне бакета и записей

Вы можете комбинировать разрешения на уровне бакета и записей в разрешениях для таблиц. Например, следующее выражение предоставит доступ ко всем логам в бакете `unrestricted_logs` и только к определённым записям в бакете `default_logs`:

```
ALLOW storage:logs:read WHERE storage:bucket-name="unrestricted_logs";


ALLOW storage:logs:read WHERE storage:bucket-name="default_logs" AND storage:dt.security_context="TeamA";
```

### Поддержка нескольких значений с оператором MATCH

Из соображений эффективности фильтры записей с операторами `=`, `IN` или `STARTSWITH` применяются к полям, содержащим одну строку. Могут быть случаи, когда поля, которые вы хотите использовать для фильтрации, содержат несколько значений с семантикой «для любого значения». Такой случай возможен с оператором `MATCH`.

Например, следующее выражение вернёт результаты для записей, где `dt.security_context` содержит строку с префиксом `crn-70400-` или массив, одним из элементов которого является строка с префиксом `crn-70400-`.

```
// will match both "crn-70400-alpha" and ["crn-70131", "crn-70400-beta", "crn-70500"]


ALLOW storage:logs:read WHERE storage:dt.security_context MATCH ("crn-70400-*");
```

Обратите внимание, что для получения семантики «для любого значения» необходимо использовать оператор `MATCH`. Использование `=`, `STARTSWITH` или `IN` для поля, содержащего массив, всегда вернёт `false`. Если вы ожидаете, что фильтры записей могут содержать массив, используйте оператор `MATCH` в ваших выражениях IAM.

Пример 1 — Предоставление команде доступа к логам

Как администратор Dynatrace, я хочу обеспечить, чтобы каждая из моих команд приложений могла получить доступ только к логам из собственного пространства имён Kubernetes (записи, идентифицируемые через `k8s.namespace.name`) и логам базовой инфраструктуры (записи, идентифицируемые через `dt.host_group.id`).

Решение:

Создайте политику для каждой команды, предоставляющую доступ к их логам.

Убедитесь, что пользователь имеет доступ ко всем соответствующим бакетам.

```
ALLOW storage:buckets:read WHERE ... // Убедитесь, что пользователь имеет доступ ко всем соответствующим бакетам


ALLOW storage:logs:read WHERE storage:k8s.namespace.name="namespace1";


ALLOW storage:logs:read WHERE storage:dt.host_group.id MATCH ("shared_host_*");
```

Пример 2 — Предоставление команде доступа к логам из лямбда-функций

Как администратор Dynatrace, я хочу настроить доступ для моих команд приложений к логам из лямбда-функций на основе тега команды. Например, `team` = `A`.

Решение:

1. Определите правило обработки логов с контекстом безопасности, которое добавляет поле `dt.security_context` на основе тега лямбда-функции.
2. Создайте политику для каждой команды, предоставляющую доступ на основе поля контекста безопасности.

   Убедитесь, что пользователь имеет доступ ко всем соответствующим бакетам.

   ```
   ALLOW storage:buckets:read WHERE ... // Убедитесь, что пользователь имеет доступ ко всем соответствующим бакетам


   ALLOW storage:logs:read WHERE storage:dt.security_context MATCH ("TeamA");
   ```

Пример 3 — Бизнес-аналитика

Как администратор, я хочу контролировать доступ к бизнес-событиям, содержащим финансовые данные. Их можно идентифицировать по полю `event.kind`.

Решение:

Создайте политику для предоставления конкретным пользователям доступа к записям в `bizevents` для определённого `event.kind` (`Opportunity Field History`).

Убедитесь, что пользователь имеет доступ ко всем соответствующим бакетам.

```
ALLOW storage:buckets:read WHERE ... // Убедитесь, что пользователь имеет доступ ко всем соответствующим бакетам


ALLOW storage:bizevents:read WHERE storage:event.kind="Opportunity Field History";
```

Пример 4 — Системные события

Как администратор, я хочу предоставить определённым пользователям доступ к событиям биллинга, но не к другим системным событиям.

Решение:

Создайте политику для предоставления доступа к записям в `dt_system_events` для конкретного `event.type` со значением `BILLING_EVENT`.

```
ALLOW storage:buckets:read WHERE storage:bucket-name="dt_system_events"


ALLOW storage:system:read WHERE storage:event.kind="BILLING_EVENT"
```

### Ограничения разрешений для записей

К разрешениям для записей применяются следующие ограничения конфигурации:

* Количество выражений на политику (100)
* Количество политик на аккаунт (200)

### Разрешения для сущностей

Разрешения для сущностей позволяют определять политики IAM, контролирующие доступ к данным о сущностях.

В отличие от данных мониторинга, разрешения для сущностей поддерживают фильтрацию только по полю `dt.security_context`.

Подробнее см. в [Предоставление доступа к сущностям с помощью контекста безопасности](../../../manage/identity-access-management/use-cases/access-security-context.md "Предоставление доступа к сущностям с помощью контекста безопасности").

## Разрешения для полей

Вы можете использовать разрешения для полей, чтобы скрывать поля, которые могут содержать конфиденциальные данные. Для этого мы предоставляем наборы полей (fieldsets). Поле считается конфиденциальным, когда оно входит в набор полей. После включения поля в набор полей только пользователи с соответствующими разрешениями смогут использовать его в DQL-запросах для фильтрации и группировки. Для остальных пользователей оно не будет отображаться в результатах запроса.

Для доступа к наборам полей требуется соответствующее разрешение, чтобы использовать конфиденциальные поля. Например, если вы хотите использовать поля `builtin-sensitive-spans` в DQL-запросах, вам необходимо следующее разрешение:

```
ALLOW storage:fieldsets:read WHERE storage:fieldset-name="builtin-sensitive-spans"
```

Три предопределённых набора полей:

* `builtin-sensitive-spans` — скрывает все поля в `spans`, которые считаются конфиденциальными
* `builtin-request-attributes-spans` — скрывает все поля в `spans`, содержащие данные атрибутов запросов, отмеченные как конфиденциальные
* `builtin-sensitive-user-events-and-sessions` — скрывает все поля в `user.events` и `user.sessions`, которые считаются конфиденциальными

* Предопределённые наборы полей применяются только к `spans`, `user.events` и `user.sessions`. Они не применяются к `logs` или `events`.
* Вы можете определить собственные наборы полей и область их применения (к бакетам, таблицам или ко всем бакетам и таблицам).
* Если у вас недостаточно разрешений, конфиденциальные поля не будут показаны в результатах.
* Вы можете использовать разрешения для полей со `smartscape`, но не с `entities`.

### Определение пользовательских наборов полей через API

Вы можете управлять пользовательскими наборами полей через REST API.

1. В Dynatrace найдите и выберите **Dynatrace API**.
2. В поле **Select a definition** выберите **Grail - Fieldsets**.
3. Пройдите аутентификацию с помощью API-токена.
   Подробности см. в [Аутентификация](../../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md "Создание персонализированных токенов платформы для доступа к сервисам Dynatrace через API.").
4. Выполните одно из следующих действий.

#### Пример

Этот вызов создаёт набор полей `sensitive-fields-retail`, удаляя поля `credit_card` и `DOB` из результатов DQL-запросов в бакете `logs_retail`.

##### URL запроса

```
POST https://myapps.mydomain.com/platform/storage/fieldsets/v1/fieldsets
```

##### Тело запроса

```
{
"name": "sensitive-fields-retail",
"description": "Sensitive fields retail",
"enabled": true,
"scope": "BUCKET",
"fields": [
"credit_card",
"DOB"
],
"buckets": [
"logs_retail"
]
}
```

Чтобы открыть поля `credit_card` и `DOB`, необходимо следующее разрешение:

```
ALLOW storage:fieldsets:read WHERE storage:fieldset-name="sensitive-fields-retail"
```

## Разрешения для файлов

Preview

Для управления справочными данными, хранящимися в Grail, необходимы следующие разрешения:

* `storage:files:read` — для чтения справочных данных через DQL.
* `storage:files:write` — для загрузки справочных данных через REST API.
* `storage:files:delete` — для удаления справочных данных через REST API.

Все эти разрешения поддерживают условие `storage:file-path` с одним из следующих операторов:

* `=` (равно) — указывает точное совпадение.
* `IN` — указывает диапазон.
* `startsWith` — с выражением в кавычках.

Следующий пример показывает, как предоставить полный доступ к справочным данным, хранящимся в `/lookups/`.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";


ALLOW storage:files:write WHERE storage:file-path startsWith "/lookups/";


ALLOW storage:files:delete WHERE storage:file-path startsWith "/lookups/";
```

Вы можете использовать структуру папок для управления доступом к различным подмножествам справочных файлов с помощью разрешений, как в следующем примере.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/public/";
```

Чтобы предоставить доступ только на чтение к конкретному файлу, можно использовать разрешение, подобное следующему.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/http_status_codes";
```

Подробнее см. в [Справочнике политик IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#storage "Полный справочник по политикам IAM и соответствующим условиям для всех сервисов Dynatrace.").

## Предопределённые глобальные политики

Существует несколько предопределённых глобальных политик, каждая из которых задана для таблицы (logs, events, bizevents, security events, metrics, entities, spans), а также три дополнительные общие политики:

* Чтение всех данных
* Чтение данных мониторинга по умолчанию
* Чтение всех системных данных

### Доступ ко всем логам

Эта политика предоставляет доступ ко всем логам из Grail и сужает разрешение бакета с помощью условия `WHERE`, ограничивающего результаты таблицей логов.

Это выражение предоставляет доступ ко всем встроенным и пользовательским бакетам.

```
ALLOW storage:buckets:read WHERE storage:table-name= "logs";


ALLOW storage:logs:read;
```

### Чтение всех данных

Это выражение разрешений предоставляет доступ ко всем таблицам и всем бакетам, поэтому его следует использовать только в обоснованных случаях.

```
ALLOW storage:buckets:read;


ALLOW storage:system:read,


storage:events:read,


storage:security.events:read,


storage:logs:read,


storage:metrics:read,


storage:entities:read,


storage:bizevents:read,


storage:spans:read,


storage:smartscape:read;
```

### Чтение всех данных мониторинга по умолчанию

Эта политика извлекает все данные мониторинга по умолчанию.

В первой строке это выражение политики предоставляет доступ ко всем бакетам по умолчанию. Условие `WHERE` сужает поиск до бакетов, имя которых начинается с `default`. Далее перечислены все необходимые разрешения для таблиц.

Это выражение не предоставляет доступ к пользовательским бакетам.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("default_*");


ALLOW storage:events:read,


storage:logs:read,


storage:metrics:read,


storage:entities:read,


storage:bizevents:read,


storage:spans:read,


storage:smartscape:read;
```

### Чтение всех системных данных

Это выражение разрешений сначала сужает результаты до системных бакетов, имя которых начинается с `dt`. Затем оно предоставляет доступ ко всем таблицам, содержащим системные данные, например, события аудита, события биллинга и события выполнения запросов. Может быть полезно для системных администраторов.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("dt_*");


ALLOW storage:system:read;
```

## Лучшие практики

* Убедитесь, что у вас также есть разрешения для бакетов.
* Если в любой другой доступной пользователю политике существует безусловное разрешение для таблицы, оператор `WHERE` не имеет значения и пользователь всегда сможет просматривать все записи из этой таблицы.
* Используйте оператор `MATCH` для упрощения выражений вместо комбинации `=`, `IN` и `STARTSWITH`, так как существует ограничение в 100 выражений на политику.
* При использовании оператора `MATCH` с подстановочными символами (`*`) в фильтрах записей рекомендуется размещать подстановочные символы перед или после разделителей слов, таких как: `-`, `_`, `.` или `/`. Это связано с тем, что `matchesValue`, используемый в DQL-запросах, работает лучше при наличии разделителей слов. Например, `... WHERE storage:dt.host_group.id MATCH ("db-tech-*")` более эффективен, чем `... WHERE storage:dt.host_group.id MATCH ("db-tech*")`.
* Объединяйте logs, events и metrics, где это применимо (для экономии в рамках ограничения в 100 выражений на политику — [синтаксис и примеры выражений политик IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax.md#iam-example-statements-combined "Синтаксис выражений политик IAM."))
* При создании пользовательских наборов полей избегайте включения в набор необходимых полей (таких как `timestamp`, `id`, `content`).

## Связанные темы

* [Работа с политиками](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками")
* [Лучшие практики DQL](../dynatrace-query-language/dql-best-practices.md "Лучшие практики использования Dynatrace Query Language.")
