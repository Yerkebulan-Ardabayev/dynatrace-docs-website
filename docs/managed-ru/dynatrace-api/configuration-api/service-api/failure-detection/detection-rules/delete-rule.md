---
title: Failure detection API - DELETE a detection rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/delete-rule
scraped: 2026-05-12T11:16:22.329260
---

# Failure detection API - DELETE a detection rule

# Failure detection API - DELETE a detection rule

* Reference
* Published Jan 11, 2021

Удаляет указанное правило обнаружения сбоев.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого правила обнаружения сбоев. Должен быть валидным UUID по RFC 4122. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Правило обнаружения сбоев удалено. Ответ без тела. |
| **404** | Сбой. Указанная сущность не существует. |