---
title: Deployment API - GET the latest available ActiveGate image version
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/activegate/get-latest-image
scraped: 2026-03-02T21:29:58.784822
---

# Deployment API — GET последней доступной версии образа ActiveGate

# Deployment API — GET последней доступной версии образа ActiveGate

* Справочник
* Опубликовано 22 ноября 2023 г.

Получение последней доступной версии образа ActiveGate.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/image/gateway/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/image/gateway/latest` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `InstallerDownload`.

Чтобы узнать, как получить и использовать токен, см. раздел [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

Запрос не предусматривает настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ImageDto](#openapi-definition-ImageDto) | Успешно |
| **404** | - | Образ ActiveGate не найден |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ImageDto`

| Элемент | Тип | Описание |
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
