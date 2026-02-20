---
title: Управление политиками API - PUT граница политики
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/put-boundary
scraped: 2026-02-20T21:28:14.993907
---

# Управление политиками API - PUT граница политики

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Обновляет или создает границу политики по uuid внутри уровня. Вы не можете редактировать глобальную границу уровня, поскольку они управляются Dynatrace.

Если указанная граница не существует, вместо этого [создается новая граница](/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary "Создать новую границу через управление политиками API.").

Запрос потребляет и производит полезную нагрузку `application/json`.

PUT

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`) в вашем токене. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | Идентификатор необходимой границы. | path | Обязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учетной записи. | path | Обязательный |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | JSON тело запроса. Содержит границу политики | body | Обязательный |

### Объекты тела запроса

#### Объект `PolicyBoundaryDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Отображаемое имя границы политики. | Обязательный |
| boundaryQuery | string | Запрос границы политики. | Обязательный |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. | Обязательный |

#### Объект `Map`

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Она должна быть скорректирована для использования в фактическом запросе.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Успешный ответ - граница политики создана |
| **204** | - | Успешный ответ - граница политики обновлена |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Неудача. Запрос недействителен |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Неудача. Указанный ресурс не найден. |

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
| name | string | Имя условия. Оно указывает, какая часть **сервисов** проверяется условием. |
| operator | string | Оператор условия. |
| values | string[] | Список ссылочных значений условия. |

#### Объект `Map`

#### Объект `ErrorDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки. |
| message | string | Краткое описание ошибки. |
| errorsMap | object | - |

### Модели тела ответа JSON

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



]



,



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

## Проверка полезной нагрузки

Мы рекомендуем проверить полезную нагрузку перед отправкой ее с фактическим запросом. Код ответа **200** указывает на действительную полезную нагрузку.

Запрос потребляет полезную нагрузку `application/json`.

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}/validation/{policyUuid}`

### Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`) в вашем токене. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

### Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| policyUuid | - | Идентификатор политики, которую необходимо проверить. | path | Обязательный |
| levelId | - | Идентификатор уровня политики. Используйте один из следующих значений, в зависимости от типа уровня:  * account: используйте UUID учетной записи. * environment: используйте идентификатор среды. | path | Обязательный |
| levelType | - | Тип уровня политики. Доступные значения:  * `account`: политика учетной записи применяется ко всем средам учетной записи. * `environment`: политика среды применяется к конкретной среде.  Каждый уровень наследует политики более высокого уровня и расширяет их своими политиками. | path | Обязательный |
| body | [CreateOrUpdateLevelPolicyRequestDto](#openapi-definition-CreateOrUpdateLevelPolicyRequestDto) | JSON тело запроса. Содержит конфигурацию политики, которую необходимо проверить. | body | Обязательный |

### Объекты тела запроса

#### Объект `CreateOrUpdateLevelPolicyRequestDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Отображаемое имя политики. | Обязательный |
| description | string | Краткое описание политики. | Обязательный |
| tags | string[] | Список тегов. | Необязательный |
| statementQuery | string | [Утверждение](https://dt-url.net/ht03ucb) политики. | Обязательный |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Она должна быть скорректирована для использования в фактическом запросе.

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

204 - Успешный ответ - граница политики обновлена.