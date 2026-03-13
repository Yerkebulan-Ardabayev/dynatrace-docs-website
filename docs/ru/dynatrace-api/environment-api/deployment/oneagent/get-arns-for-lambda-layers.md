---
title: Deployment API - View ARNs for AWS Lambda layers
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-arns-for-lambda-layers
scraped: 2026-03-06T21:32:18.857315
---

# Deployment API — Просмотр ARN для слоёв AWS Lambda

# Deployment API — Просмотр ARN для слоёв AWS Lambda

* Справочник
* Опубликовано 29 июл. 2022 г.

Этот API предназначен для использования с последней реализацией AWS Lambda. Подробнее см. в разделе [AWS Lambda](../../../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration.md "Возможности AWS Lambda и варианты интеграции").

Получение Amazon Resource Names (ARN) последней версии OneAgent для слоёв AWS Lambda для поддерживаемых сред выполнения AWS Lambda.

Обратите внимание, что передача архитектуры, типа технологии или региона в качестве параметра возвращает только соответствующие слои.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/lambda/layer` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/lambda/layer` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью видимости `InstallerDownload`.

Информацию о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| arch | string | Архитектура вашей ОС:  * Если не указано — отображаются доступные слои для всех архитектур. * `x86`: архитектура x86. * `arm`: архитектура ARM. Элемент может принимать значения * `x86` * `arm` | query | Необязательный |
| techtype | string | Тип технологии среды выполнения lambda. Элемент может принимать значения * `java` * `nodejs` * `python` | query | Необязательный |
| withCollector | string | Укажите, хотите ли вы включить сборщик логов или использовать только сборщик логов. ONLY нельзя комбинировать с techtype. Элемент может принимать значения * `included` * `excluded` * `only` | query | Необязательный |
| region | string | Регион слоя. Должен совпадать с регионом функции AWS Lambda | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LatestLambdaLayersMetainfo](#openapi-definition-LatestLambdaLayersMetainfo) | Успешно. Payload содержит ARN последних доступных слоёв. |
| **404** | - | Не найдено. Подробности см. в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `LatestLambdaLayersMetainfo`

Актуальная информация о доступных слоях AWS Lambda

| Элемент | Тип | Описание |
| --- | --- | --- |
| arns | [LambdaDto[]](#openapi-definition-LambdaDto) | - |

#### Объект `LambdaDto`

| Элемент | Тип | Описание |
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
