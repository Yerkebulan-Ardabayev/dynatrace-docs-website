---
title: Plugins API - DELETE plugin ZIP file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/delete-plugin-binary
scraped: 2026-05-12T11:21:03.233727
---

# Plugins API - DELETE plugin ZIP file

# Plugins API - DELETE plugin ZIP file

* Reference
* Published Jun 07, 2019

Удаляет ZIP-файл указанного плагина из Dynatrace.

Удаление файла плагина деинсталлирует плагин, делая его недоступным для использования.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID плагина, который нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Пример

В этом примере запрос удаляет **MathPlugin** с ID **custom.remote.python.simple\_math** из окружения **mySampleEnv**. Код ответа **204** указывает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/binary \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/binary
```

#### Код ответа

204