---
title: List available Cluster tokens
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-tokens
scraped: 2026-05-12T11:06:03.716511
---

# List available Cluster tokens

# List available Cluster tokens

* Published Feb 12, 2020

Этот API-вызов возвращает список доступных токенов в вашем окружении.

Вывод можно сузить, добавив параметры. Токен должен соответствовать всем указанным параметрам.

Также можно задать лимит возвращаемых токенов.

Этот список может содержать токены, созданные автоматически (например, InstallerDownload, Mobile, ...) и не отображаемые на странице Settings. Удаление таких токенов может иметь непредвиденные побочные эффекты, поскольку они могут всё ещё использоваться.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Cluster token management** (`ClusterTokenManagement`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| limit | integer | Ограничивает максимальное число возвращаемых токенов.  Если не задан, используется значение `1000`.  Максимальное значение 1000000. | query | Optional |
| user | string | Фильтрует результирующий набор токенов по пользователю-владельцу токена. | query | Optional |
| permissions | string[] | Фильтрует результирующий набор токенов по scope'ам, назначенным токену.  Можно указать несколько разрешений в формате: `permissions=scope1&permissions=scope2`. Токен должен иметь *все* указанные scope'ы. Возможные значения: * `ClusterTokenManagement` * `ControlManagement` * `DiagnosticExport` * `EnvironmentTokenManagement` * `ExternalSyntheticIntegration` * `Nodekeeper` * `ReadSyntheticData` * `ServiceProviderAPI` * `UnattendedInstall` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `apiTokens.read` * `apiTokens.write` * `settings.read` * `settings.write` | query | Optional |
| from | integer | Использован после этого timestamp (UTC миллисекунды). | query | Optional |
| to | integer | Использован до этого timestamp (UTC миллисекунды). | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Успех |

### Объекты тела ответа

#### Объект `StubList`

Упорядоченный список кратких представлений сущностей Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Упорядоченный список кратких представлений сущностей Dynatrace. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

### JSON-модели тела ответа

```
{



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Пример

В этом примере запрос возвращает API-токены в окружении `myManaged.cluster.com` для пользователя `Pete` с разрешениями cluster token management.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/tokens?limit=1000&user=Pete&permissions=ClusterTokenManagement"



-H  "accept: application/json; charset=utf-8"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/tokens?limit=1000
```

#### Тело ответа

```
{



"values": [



{



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1",



"description": "Dynatrace entity 1 for the REST API example"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

#### Код ответа

`200`