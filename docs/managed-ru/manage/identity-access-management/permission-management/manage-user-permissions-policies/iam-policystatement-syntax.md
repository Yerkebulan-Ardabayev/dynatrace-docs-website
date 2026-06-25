---
title: Синтаксис и примеры операторов политик IAM
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax
scraped: 2026-05-12T11:49:51.029568
---

# Синтаксис и примеры операторов политик IAM

# Синтаксис и примеры операторов политик IAM

* Reference
* 6-min read
* Updated on Feb 10, 2026

На этой странице описывается структура и синтаксис операторов политик IAM, а также приведены примеры работы с ними.

* Полный список поддерживаемых значений для каждого сервиса, разрешения и условия IAM см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.").

## Оператор ALLOW

Оператор политики обычно начинается с ключевого слова `ALLOW`, за которым следуют `permissions` (разрешения) и `conditions` (условия).

```
ALLOW `<permissions>` WHERE `<conditions>`;
```

* `ALLOW`: разрешить выполнение действия.
* `permissions`: конкретное действие, которое пользователь или группа могут выполнять с ресурсом в сервисе Dynatrace (например, `settings:objects:read`).

Подробности об операторе

Один оператор может содержать несколько `permission` и `condition`. Условие является необязательным. Политика может содержать не более 100 операторов.

Структура оператора в расширенном виде:

```
ALLOW <service:resource:action> WHERE <service:attribute> = 'value' AND <service:attribute> = "value";
```

* `service`: имя сервиса Dynatrace (например, `settings`, `storage` или `metrics`).
* `resource`: тип объекта или возможности в рамках сервиса (например, `objects`, `logs` или `apps`).
* `action`: конкретная операция, которую пользователь может выполнять с ресурсом (например, `read`, `write` или `create`).

Действия с ресурсами

Каждый ресурс предлагает определённый набор действий; не все действия доступны для всех ресурсов.

* `condition`: позволяет ограничить доступ на уровне ресурса или записи. Условие является необязательным (например, `storage:table-name = "application.snapshots"`). Условие состоит из трёх частей:

  + `service`: сервис Dynatrace, предоставляющий атрибут для условия (например, `storage`, `settings` или `metrics`).
  + `attribute`: конкретное свойство этого сервиса, проверяемое в условии (например, `table-name`, `dt.security_context` или `builtin:container.monitoring-rule`).
  + `value`: литерал (или параметр) для сравнения с атрибутом (например, `application.snapshots`, `default_security_events` или `builtin:container.monitoring-rule`).

## Оператор DENY

Оператор `DENY` всегда имеет приоритет над оператором `ALLOW`.

Пример:

```
DENY storage:logs:read;
```

Если назначен оператор `DENY` и он совпадает с заданным запросом, все последующие операторы `ALLOW` игнорируются.

Вместо использования `DENY` рекомендуется предоставлять пользователям только необходимый доступ с помощью выделенных операторов `ALLOW` с условиями или используя границы политик.

Рекомендуется избегать операторов `DENY` без условий, так как они заблокируют весь API для пользователей и могут создать сложные ситуации с политиками, которые трудно разрешить.

Dynatrace оценивает приоритет `DENY` следующим образом:

1. Проверить наличие безусловного `DENY` для запроса к сервису и отклонить, если совпадает.
2. Проверить наличие условного `DENY` для запроса к сервису, совпадающего с запросом, и отклонить, если совпадает.
3. Проверить наличие безусловного `ALLOW` для запроса к сервису и разрешить, если совпадает.
4. Проверить наличие условного `ALLOW` для запроса к сервису, совпадающего с запросом, и разрешить, если совпадает.
5. Если ничего не совпало, отклонить доступ.

## Синтаксис операторов политик

В таблице ниже приведены описания и примеры для каждого компонента синтаксиса политик.

Пример:

```
ALLOW settings:objects:read, settings:schemas:read WHERE settings:schemaId = "123" AND storage:table-name = "events";
```

| Компонент | Описание | Примеры |
| --- | --- | --- |
| `<permission>` | Конкретное действие, которое пользователь или группа могут выполнять с ресурсом в сервисе Dynatrace. | * `storage:logs:read` * `storage:buckets:write` * `environment:roles:viewer` * `openpipeline:configurations:write` * `storage:system:read (используется с условием, например storage:table-name = "dt.system.events")`  Дополнительные разрешения см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). |
| `<service>` | Имя сервиса Dynatrace. | * `settings` * `cloudautomation` * `environment` * `automation` * `openpipeline` * `business-analytics`  Дополнительные сервисы см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). |
| `<resource>` | Конкретный тип объекта или возможности в рамках сервиса. | * `logs` * `bucket-definitions` * `configurations` * `apps`  Дополнительные ресурсы см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). |
| `<action>` | Конкретная операция, которую пользователь может выполнять с ресурсом. | * `read` * `run` * `set` * `manage` * `execute`  Дополнительные действия см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). |
| `<condition>` | Добавление ограничения к разрешению на основе определённого атрибута или контекста. | * `WHERE` `<condition name>` `<condition operator>` = "`<condition value>`". + Пример: `WHERE settings:schemaId = "builtin:container.monitoring-rule" AND storage:table-name = "events"` * Для добавления нескольких условий в оператор используйте `AND`. * Условия являются необязательными. Значение `null` указывает на отсутствие условия. + Пример: `ALLOW settings:schemas:read WHERE null;` |
| `<condition name>` | Конкретное свойство сервиса для проверки в условии. | * `table-name` * `dt.security_context` * `schemaId`  Каждое разрешение в политике IAM содержит условия.  * Некоторые условия специфичны для разрешений и применяются только к определённому набору разрешений в сервисе, тогда как [глобальные условия](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Глобальные условия политик") применяются ко всем разрешениям.  Условия, поддерживаемые разрешениями, см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). |
| `<condition operator>` | Оператор для проверки условия. | * `=` * `!=` * `<` * `>` * `IN` (применяется только к спискам) * `startsWith` * `NOT IN` * `NOT startsWith`  Не каждый оператор применим к каждому атрибуту сервиса. Список поддерживаемых вариантов см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). |
| `<condition value>` | Литерал (или параметр) для сравнения с атрибутом. | Примеры для каждого оператора:  * **=** или **!=** : `WHERE settings:schemaId = "builtin:container.monitoring-rule"` * **IN** : `WHERE settings:schemaId IN ("builtin:container.monitoring-rule", "builtin:container.built-in-monitoring-rule")` * **NOT IN** : `WHERE storage:table-name = "events" NOT IN ("default_security_events", "default_security_custom_events")` * **NOT startsWith** : `WHERE storage:table-name NOT startsWith "application."` * **>** : `WHERE global:date-time > "2022-05-03T05:00:00+01:00"` * **<** : `WHERE global:time-of-day < "17:00+01:00"` * **startsWith** : `WHERE settings:schemaId startsWith "app:"` |
| `<comment>` | Комментарий, поясняющий политику. Всё, что находится между двойным слешем (`//`) и концом строки, является текстом комментария. | * Пример: `// Vulnerability service ALLOW vulnerability-service:vulnerabilities:read;` |

## Примеры операторов политик

Приведённые ниже примеры демонстрируют распространённые паттерны политик IAM для предоставления, ограничения или обусловленного доступа в различных сценариях.

* В примерах используется сервис настроек Dynatrace (`settings`), позволяющий управлять следующими разрешениями:

  + `schemas:read`
  + `objects:read`
  + `objects:write`

  Сервис настроек поддерживает условие `settings:schemaId`, которое поддерживает следующие операторы:

  + `IN`
  + `=`
  + `!=`
  + `startsWith`
  + `NOT startsWith`.

### Пример 1: простой оператор ALLOW

В этом примере пользователь, принадлежащий к группе с назначенной политикой, получает доступ на чтение ко всем схемам в сервисе `settings` Dynatrace.

```
ALLOW settings:schemas:read;
```

### Пример 2: условие — одиночное значение

Этот пример дополняет пример 1 условием, ограничивающим доступ на чтение только одной конкретной схемой в сервисе `settings` Dynatrace.

```
ALLOW settings:schemas:read WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

Условие добавляется к оператору с помощью ключевого слова `WHERE`, за которым следует условие, состоящее из трёх частей:

* имя условия (`settings:schemaId`)
* оператор условия (`=`)
* значение условия (`"builtin:container.monitoring-rule"`)

Таким образом, данный оператор означает: пользователь, принадлежащий к группе с назначенной политикой, может читать схемы в сервисе `settings`, но только если схема равна `builtin:container.monitoring-rule`.

При использовании оператора `!=` пользователь сможет читать схемы в сервисе `settings`, но только если схема НЕ равна `builtin:container.monitoring-rule`.

### Пример 3: условие — список значений

Этот пример дополняет пример 2, демонстрируя использование оператора `IN` со списком значений.

```
ALLOW settings:schemas:read WHERE settings:schemaId IN ("builtin:container.monitoring-rule", "builtin:container.built-in-monitoring-rule");
```

Значение условия в данном случае представляет собой список идентификаторов схем в скобках, разделённых запятыми.

Таким образом, данный оператор означает: пользователь, принадлежащий к группе с назначенной политикой, может читать схемы в сервисе `settings`, но только если идентификатор схемы входит в список из двух указанных идентификаторов:
`("builtin:container.monitoring-rule", "builtin:container.built-in-monitoring-rule")`

### Пример 4: операторы на отдельных строках

Каждая политика может содержать несколько операторов.

Пример политики с двумя операторами:

```
ALLOW settings:objects:read;



ALLOW settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

В этом примере пользователь, принадлежащий к группе с назначенной политикой, может:

* читать все `objects` в сервисе `settings` (в первом операторе нет условия)
* записывать `objects` в сервисе `settings` только там, где `settings:schemaId` равно `builtin:container.monitoring-rule`

### Пример 5: объединённые операторы

Вместо перечисления операторов разрешений на отдельных строках их можно объединить в одну строку:

```
ALLOW settings:objects:read, settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

Политика с таким оператором предоставляет доступ на чтение и запись к `builtin:container.monitoring-rule`, при этом условие WHERE применяется к обоим разрешениям.

### Пример 6: оператор с комментариями

Для пояснения политики или её операторов можно добавить одну или несколько строк комментариев:

```
// Read and Write access to monitoring-rule



ALLOW settings:objects:read, settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
```

Комментарий также можно добавить в строку оператора:

```
ALLOW settings:objects:read;  // Allows the user to read all `objects` in the `settings` service
```