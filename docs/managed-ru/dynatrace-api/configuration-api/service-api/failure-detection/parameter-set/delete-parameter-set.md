---
title: Failure detection API - DELETE a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/delete-parameter-set
scraped: 2026-05-12T11:16:11.409630
---

# Failure detection API - DELETE a parameter set

# Failure detection API - DELETE a parameter set

* Reference
* Published Jan 11, 2021

Удаляет указанный набор параметров обнаружения сбоев.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого набора параметров обнаружения сбоев. Должен быть валидным UUID по RFC 4122. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Набор параметров обнаружения сбоев удалён. Ответ без тела. |
| **404** | Сбой. Указанная сущность не существует. |