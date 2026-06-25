---
title: Audit logs API - GET audit log
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/audit-logs/get-log
scraped: 2026-05-12T11:36:50.709353
---

# Audit logs API - GET audit log

# Audit logs API - GET audit log

* Reference
* Published Dec 10, 2019

Получает audit log вашего Dynatrace-окружения.

Полный список может быть длинным, поэтому его можно сузить, указав фильтры (например, теги). Подробнее в секции **Parameters**.

Можно ограничить вывод, используя пагинацию:

1. Укажите количество результатов на странице в query-параметре **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в query-параметре **nextPageKey** для получения последующих страниц.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/auditlogs` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/auditlogs` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `auditLogs.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница всегда возвращается, если query-параметр **nextPageKey** не указан.  Если **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть опущены. | query | Optional |
| pageSize | integer | Количество записей лога в одном payload ответа.  Максимально допустимый размер страницы: 5000.  Если не задано, используется 1000. | query | Optional |
| filter | string | Фильтрует audit log. Можно использовать следующие критерии:  * User: `user("userIdentification")`. Применяется оператор `EQUALS`. * Event type: `eventType("value")`. Применяется оператор `EQUALS`. * Category зарегистрированной операции: `category("value")`. Применяется оператор `EQUALS`. * Entity ID: `entityId("id")`. Применяется оператор `CONTAINS`. * Settings schema ID: `dt.settings.schema_id("id")`. Применяется оператор `EQUALS`. * Settings scope ID: `dt.settings.scope_id("id")`. Применяется оператор `EQUALS`. * Settings key: `dt.settings.key("key")`. Применяется оператор `EQUALS`. * Settings object ID: `dt.settings.object_id("id")`. Применяется оператор `EQUALS`.  Для каждого критерия можно указать несколько альтернатив через запятую. В этом случае применяется логика OR. Например, `eventType("CREATE","UPDATE")` означает eventType "CREATE" или "UPDATE".  Можно задать несколько критериев через запятую, например `eventType("CREATE","UPDATE"),category("CONFIG")`. В ответ включаются только результаты, соответствующие **всем** критериям.  Значение критерия указывается как строка в кавычках. Следующие спецсимволы внутри кавычек нужно экранировать через тильду (`~`):  * Тильда `~` * Кавычка `"` | query | Optional |
| from | string | Начало запрашиваемого таймфрейма.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный таймфрейм две недели (`now-2w`). | query | Optional |
| to | string | Конец запрашиваемого таймфрейма.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущий таймстамп. | query | Optional |
| sort | string | Сортировка записей audit log:  * `timestamp`: Сначала старые. * `-timestamp`: Сначала новые.  Если не задано, применяется сортировка «сначала новые». | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AuditLog](#openapi-definition-AuditLog) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `AuditLog`

Audit log вашего окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| auditLogs | [AuditLogEntry[]](#openapi-definition-AuditLogEntry) | Список записей audit log, упорядоченный по таймстампу создания. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `AuditLogEntry`

Запись audit log.

| Элемент | Тип | Описание |
| --- | --- | --- |
| category | string | Категория зарегистрированной операции. Элемент может принимать значения * `ACTIVEGATE_TOKEN` * `BUILD_UNIT_V2` * `CONFIG` * `MANUAL_TAGGING_SERVICE` * `TENANT_LIFECYCLE` * `TOKEN` * `WEB_UI` |
| dt.settings.key | string | Ключ затронутого объекта setting для записей категории `CONFIG`. |
| dt.settings.object\_id | string | ID затронутого объекта setting для записей категории `CONFIG`. |
| dt.settings.object\_summary | string | Сводка значения для записей категории `CONFIG`. |
| dt.settings.schema\_id | string | ID schema или ID config для записей категории `CONFIG`. |
| dt.settings.scope\_id | string | Scope сохранения для записей категории `CONFIG`, например идентификатор ME. |
| dt.settings.scope\_name | string | Отображаемое имя scope для записей категории `CONFIG`. |
| entityId | string | ID сущности из **category**.  Например, это может быть config ID для категории `CONFIG` или token ID для категории `TOKEN`. |
| environmentId | string | ID Dynatrace-окружения, в котором произошла зарегистрированная операция. |
| eventType | string | Тип зарегистрированной операции.  * `LOGIN` -> Пользователь вошёл в систему. * `LOGOUT` -> Пользователь вышел из системы. * `CREATE` -> Объект создан. * `UPDATE` -> Объект обновлён. * `DELETE` -> Объект удалён. * `REVOKE` -> Токен ActiveGate отозван. * `TAG_ADD` -> Добавлен ручной тег. * `TAG_REMOVE` -> Удалён ручной тег. * `TAG_UPDATE` -> Обновлён ручной тег. * `REMOTE_CONFIGURATION_MANAGEMENT` -> Произошла операция, связанная с Remote Configuration Management. Элемент может принимать значения * `CREATE` * `DELETE` * `LOGIN` * `LOGOUT` * `REORDER` * `REVOKE` * `TAG_ADD` * `TAG_REMOVE` * `TAG_UPDATE` * `UPDATE` |
| logId | string | ID записи лога. |
| message | string | Зарегистрированное сообщение. |
| patch | string | Patch зарегистрированной операции в виде JSON.  Формат: расширенный RFC 6902. Patch также содержит предыдущее значение в поле **oldValue**. |
| success | boolean | Зарегистрированная операция успешна (`true`) или провалена (`false`). |
| timestamp | integer | Таймстамп создания записи в миллисекундах UTC. |
| user | string | ID пользователя, выполнившего зарегистрированную операцию. |
| userOrigin | string | Источник и IP-адрес **user**. |
| userType | string | Тип аутентификации **user**.  * `USER_NAME` -> Пользователь вошёл в UI. * `TOKEN_HASH` -> URL Token или DevOps Token, регистрируется хэш токена. * `SERVICE_NAME` -> Нет аутентифицированного пользователя, действие выполнено системным сервисом автоматически. * `PUBLIC_TOKEN_IDENTIFIER` -> API Token, регистрируется публичный ID токена. Элемент может принимать значения * `PUBLIC_TOKEN_IDENTIFIER` * `SERVICE_NAME` * `TOKEN_HASH` * `USER_NAME` |

#### Объект `AnyValue`

Схема, представляющая значение произвольного типа.

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"auditLogs": [



{



"category": "CONFIG",



"entityId": "MOBILE_RUM: MOBILE_APPLICATION-752C223D59734CD2",



"environmentId": "prod-env-13",



"eventType": "UPDATE",



"logId": "197425568800060000",



"patch": [



{



"oldValue": 20000,



"op": "replace",



"path": "/refreshTimeIntervalMillis",



"value": 30000



}



],



"success": true,



"timestamp": 1974255688445,



"user": "test.user@company.com",



"userOrigin": "webui (192.168.0.2)",



"userType": "USER_NAME"



}



],



"nextPageKey": "___a7acX3q0AAAAAACJidWlsdGluOnNlcnZpY2lUVEJCUzBaNVIxVjJOSGt6Y3oyLTcwMUZWRkxlclH__9rtpxferQ",



"pageSize": 5,



"totalCount": 10



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Пример

В этом примере запрос получает все логины (`filter=eventType(LOGIN)`) из audit log окружения **mySampleEnv** за последнюю неделю (`from=now-1w`).

API-токен передаётся в заголовке **Authorization**.

Ответ усечён до первых трёх записей.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs?filter=eventType%28LOGIN%29&from=now-1w' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs?filter=eventType%28LOGIN%29&from=now-1w
```

#### Тело ответа

```
{



"totalCount": 5820,



"nextPageKey": "vu8y3hPZ3q0AAAAAAi_neQJ8qUAAAAFu0T-ECgAAAW71TAgKAAAD6AAQZXZlbnRUeXBlKExPR0lOKQC-7zLeE9nerQ",



"auditLogs": [



{



"logId": "157607341600050000",



"eventType": "LOGIN",



"category": "WEB_UI",



"entityId": "240.204.62.255",



"environmentId": "yasmuoujsw",



"user": "Dynatrace support user #877988415",



"userType": "USER_NAME",



"userOrigin": "Forwarded: 240.204.62.255",



"timestamp": 1576073415531,



"success": true



},



{



"logId": "157607338800050000",



"eventType": "LOGIN",



"category": "WEB_UI",



"entityId": "55.199.177.119",



"environmentId": "yasmuoujsw",



"user": "Dynatrace support user #490812376",



"userType": "USER_NAME",



"userOrigin": "Forwarded: 55.199.177.119",



"timestamp": 1576073388150,



"success": true



},



{



"logId": "157607338300060000",



"eventType": "LOGIN",



"category": "WEB_UI",



"entityId": "75.16.11.184",



"environmentId": "umsaywsjuo",



"user": "Dynatrace support user #765684830",



"userType": "USER_NAME",



"userOrigin": "Forwarded: 75.16.11.184",



"timestamp": 1576073381543,



"success": true



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Audit logs via API](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Узнайте, как управлять audit logs через API.")