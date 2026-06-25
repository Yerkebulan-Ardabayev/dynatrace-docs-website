---
title: AWS PrivateLink API - GET allowlist
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/get-allowlist
scraped: 2026-05-12T11:21:12.958184
---

# AWS PrivateLink API - GET allowlist

# AWS PrivateLink API - GET allowlist

* Reference
* Published Nov 19, 2020

Возвращает список AWS-аккаунтов из allowlist AWS PrivateLink.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AllowlistedAwsAccountList](#openapi-definition-AllowlistedAwsAccountList) | Успех. Список в теле ответа. |

### Объекты тела ответа

#### Объект `AllowlistedAwsAccountList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [AllowlistedAwsAccount[]](#openapi-definition-AllowlistedAwsAccount) | - |

#### Объект `AllowlistedAwsAccount`

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID AWS-аккаунта для добавления в allowlist |

### JSON-модели тела ответа

```
{



"values": [



{



"id": "string"



}



]



}
```