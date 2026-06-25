---
title: Deployment API - GET последняя доступная версия образа ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/get-latest-image
scraped: 2026-05-12T11:56:49.951393
---

# Deployment API - GET последняя доступная версия образа ActiveGate

# Deployment API - GET последняя доступная версия образа ActiveGate

* Справочник
* Опубликовано 22 ноября 2023 г.

Получает последнюю доступную версию образа ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/image/gateway/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/image/gateway/latest` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ImageDto](#openapi-definition-ImageDto) | Успех |
| **404** | - | Образ ActiveGate не найден |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ImageDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| source | string | Расположение образа |
| tag | string | Тег образа |

### JSON-модели тела ответа

```
{



"source": "string",



"tag": "string"



}
```