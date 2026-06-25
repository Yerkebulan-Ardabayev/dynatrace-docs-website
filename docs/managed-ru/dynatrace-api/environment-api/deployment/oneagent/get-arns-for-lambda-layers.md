---
title: Deployment API - View ARNs for AWS Lambda layers
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-arns-for-lambda-layers
scraped: 2026-05-12T11:58:25.644497
---

# Deployment API - View ARNs for AWS Lambda layers

# Deployment API - View ARNs for AWS Lambda layers

* Справочник
* Опубликовано 29 июля 2022 г.

Этот API предназначен для использования с актуальной реализацией AWS Lambda. Подробности смотрите в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности AWS Lambda и варианты интеграции").

Получает Amazon Resource Names (ARN) последней версии OneAgent для слоёв AWS Lambda для поддерживаемых сред выполнения AWS Lambda.

Обратите внимание: передача архитектуры, типа технологии или региона в параметре возвращает только релевантные слои.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/lambda/layer` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/lambda/layer` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| arch | string | Архитектура вашей ОС:  * Если не указано, показывает доступные слои для всех архитектур. * `x86`: архитектура x86. * `arm`: архитектура ARM. Поле может принимать значения: * `x86` * `arm` | query | Необязательный |
| techtype | string | Тип технологии среды выполнения lambda. Поле может принимать значения: * `java` * `nodejs` * `python` * `go` * `DotNet` | query | Необязательный |
| withCollector | string | Укажите, нужен ли встроенный log collector или только log collector. ONLY нельзя комбинировать с techtype Поле может принимать значения: * `included` * `excluded` * `only` | query | Необязательный |
| region | string | Регион слоя. Должен совпадать с регионом функции AWS Lambda | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LatestLambdaLayersMetainfo](#openapi-definition-LatestLambdaLayersMetainfo) | Успех. Payload содержит ARN последних доступных слоёв. |
| **404** | - | Не найдено. Подробности смотрите в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `LatestLambdaLayersMetainfo`

Актуальная информация о доступных слоях AWS lambda

| Поле | Тип | Описание |
| --- | --- | --- |
| arns | [LambdaDto[]](#openapi-definition-LambdaDto) | - |

#### Объект `LambdaDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| arch | string | - |
| arn | string | - |
| region | string | - |
| techType | string | - |
| withCollector | string | - |

### JSON-модели тела ответа

```
{



"arns": [



{



"arch": "string",



"arn": "string",



"region": "string",



"techType": "string",



"withCollector": "string"



}



]



}
```