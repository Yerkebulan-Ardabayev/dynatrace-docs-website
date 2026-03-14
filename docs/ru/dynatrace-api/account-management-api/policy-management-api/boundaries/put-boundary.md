---
title: Policy management API - PUT a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/put-boundary
scraped: 2026-03-05T21:33:42.980568
---

# Policy management API - PUT-запрос границы политики


* Latest Dynatrace
* Справочник
* Опубликовано 20 ноября 2025 г.

Обновляет или создает границу политики по UUID в пределах уровня. Вы не можете редактировать границу глобального уровня, так как они управляются Dynatrace.

Если указанная граница не существует, вместо нее [создается новая граница](post-boundary.md "Создание новой границы через Policy management API.").

Запрос потребляет и возвращает полезную нагрузку в формате `application/json`.

## Аутентификация

Для выполнения этого запроса вам необходимо разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`), назначенное вашему токену. Чтобы узнать, как его получить и использовать, см. [OAuth-клиенты](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | Идентификатор требуемой границы. | path | Обязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательный |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | JSON-тело запроса. Содержит границу политики. | body | Обязательный |

### Объекты тела запроса

#### Объект `PolicyBoundaryDto`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| name | string | Отображаемое имя границы политики. | Обязательный |
| boundaryQuery | string | Запрос границы политики. | Обязательный |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. | Обязательный |

#### Объект `Map`

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Ее необходимо адаптировать для использования в реальном запросе.

```
{


"name": "string",


"boundaryQuery": "string",


"metadata": {}


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Успешный ответ -- граница политики создана |
| **204** | - | Успешный ответ -- граница политики обновлена |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Ошибка. Запрос некорректен |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Ошибка. Указанный ресурс не найден. |

### Объекты тела ответа

#### Объект `PolicyBoundaryOverview`

| Элемент | Тип | Описание |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | Отображаемое имя границы политики. |
| boundaryQuery | string | Запрос границы политики. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. |

#### Объект `Condition`

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя условия. Указывает, какая часть **сервисов** проверяется условием. |
| operator | string | Оператор условия. |
| values | string[] | Список эталонных значений условия. |

#### Объект `Map`

#### Объект `ErrorDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки. |
| message | string | Краткое описание ошибки. |
| errorsMap | object | - |

### JSON-модели тела ответа

```
{


"uuid": "string",


"levelType": "string",


"levelId": "string",


"name": "string",


"boundaryQuery": "string",


"boundaryConditions": [


{


"name": "string",


"operator": "string",


"values": [


"string"


]


}


],


"metadata": {}


}
```

```
{


"code": 1,


"message": "string",


"errorsMap": {}


}
```

## Валидация полезной нагрузки

Рекомендуется проверить полезную нагрузку перед отправкой реального запроса. Код ответа **200** указывает на корректную полезную нагрузку.

Запрос потребляет полезную нагрузку в формате `application/json`.

### Аутентификация

Для выполнения этого запроса вам необходимо разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`), назначенное вашему токену. Чтобы узнать, как его получить и использовать, см. [OAuth-клиенты](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

### Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| policyUuid | - | Идентификатор политики для валидации. | path | Обязательный |
| levelId | - | Идентификатор уровня политики. Используйте одно из следующих значений в зависимости от типа уровня: * account: используйте UUID учетной записи. * environment: используйте ID среды. | path | Обязательный |
| levelType | - | Тип уровня [политики](https://dt-url.net/eu03uap). Доступны следующие значения: * `account`: политика учетной записи применяется ко всем средам учетной записи. * `environment`: политика среды применяется к определенной среде. Каждый уровень наследует политики вышестоящего уровня и дополняет их собственными политиками. | path | Обязательный |
| body | [CreateOrUpdateLevelPolicyRequestDto](#openapi-definition-CreateOrUpdateLevelPolicyRequestDto) | JSON-тело запроса. Содержит конфигурацию политики для валидации. | body | Обязательный |

### Объекты тела запроса

#### Объект `CreateOrUpdateLevelPolicyRequestDto`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| name | string | Отображаемое имя политики. | Обязательный |
| description | string | Краткое описание политики. | Обязательный |
| tags | string[] | Список тегов. | Необязательный |
| statementQuery | string | [Выражение](https://dt-url.net/ht03ucb) политики. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Ее необходимо адаптировать для использования в реальном запросе.

```
{


"name": "string",


"description": "string",


"tags": [


"string"


],


"statementQuery": "string"


}
```

## Пример

В этом примере запрос обновляет `name` границы политики с `UUID` **3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68** для учетной записи с `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request PUT \


--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68 \


--header 'Authorization: Bearer abcdefjhij1234567890' \


--header 'Content-Type: application/json' \


--data '{


"name": "host name",


"description": "storage:host.name = \"myHost\"",


"metadata": {}


}'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68
```

#### Тело запроса

```
{


"name": "host name",


"boundaryQuery": "storage:host.name = \"myHost\";",


"metadata": {}


}
```

#### Код ответа

204 - Успешный ответ -- граница политики обновлена.
