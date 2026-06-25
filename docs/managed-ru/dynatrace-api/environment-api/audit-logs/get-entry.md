---
title: Audit logs API - GET audit log entry
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/audit-logs/get-entry
scraped: 2026-05-12T11:36:52.040804
---

# Audit logs API - GET audit log entry

# Audit logs API - GET audit log entry

* Reference
* Published Dec 10, 2019

Получает указанную запись audit log.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/auditlogs/{id}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/auditlogs/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `auditLogs.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID запрашиваемой записи лога. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AuditLogEntry](#openapi-definition-AuditLogEntry) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректный формат ID. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

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

В этом примере запрос получает запись audit log с ID **157607396300050000**.

Эта запись сохраняет информацию об изменении конфигурации dashboard с ID **14b3bfe7-69d8-48bf-b08a-4f9a2ff3f703**. Изменение: перемещение и изменение размера tile, выполненное Dynatrace-пользователем с user ID **643541629**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs/157607396300050000' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/auditlogs/157607396300050000
```

#### Тело ответа

```
{



"logId": "157607396300050000",



"eventType": "UPDATE",



"category": "CONFIG",



"entityId": "DASHBOARDS_SETTINGS: 14b3bfe7-69d8-48bf-b08a-4f9a2ff3f703",



"environmentId": "yasmuoujsw",



"user": "Dynatrace user #643541629",



"userType": "USER_NAME",



"userOrigin": "webui (240.204.62.255)",



"timestamp": 1576074315483,



"success": true,



"patch": [



{



"op": "replace",



"path": "/tiles/24/top",



"value": 304,



"oldValue": 380



},



{



"op": "replace",



"path": "/tiles/24/left",



"value": 304,



"oldValue": 798



},



{



"op": "replace",



"path": "/tiles/24/width",



"value": 608,



"oldValue": 304



},



{



"op": "replace",



"path": "/tiles/24/height",



"value": 608,



"oldValue": 304



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Audit logs via API](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Узнайте, как управлять audit logs через API.")