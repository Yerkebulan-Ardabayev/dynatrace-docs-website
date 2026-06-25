---
title: Ротация cluster-токенов через API
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-token-rotation-api
scraped: 2026-05-12T12:14:09.740420
---

# Ротация cluster-токенов через API

# Ротация cluster-токенов через API

* Published Feb 28, 2020

Регулярная смена токенов аутентификации Dynatrace API — хорошая практика безопасности. Для ротации токенов управления кластером можно использовать Dynatrace Cluster API. С помощью Tokens API ротацию можно автоматизировать.

Чтобы открыть Dynatrace Cluster API:

1. Откройте Cluster Management Console.
2. Перейдите в User menu в правом верхнем углу.
3. Выберите **Cluster API**.

## Ротация токена

Чтобы ротировать cluster management токены через Tokens API:

1. Получите ID старого токена.

   ID нужен, чтобы отозвать токен и затем удалить его. Если у вас известно только значение токена, то для отзыва и последующего удаления потребуется его ID. Для этого отправьте запрос [POST token lookup](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Поиск метаданных токена аутентификации Dynatrace API через API.") с удаляемым токеном в payload. Запрос вернёт метаданные токена, включая ID, который понадобится позже.
2. Создайте новый токен.

   Чтобы создать новый токен на замену устаревшему, выполните запрос [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Создание нового токена аутентификации Dynatrace API через API."). Поскольку токен с одинаковыми параметрами создаётся регулярно, имеет смысл хранить его конфигурацию в системе контроля версий.
3. Отзовите старый токен. (Не удаляйте его до отзыва.)

   Для отзыва старого токена выполните [PUT an existing token](/managed/dynatrace-api/environment-api/tokens-v1/put-token "Обновление токена аутентификации Dynatrace API через API."). Понадобится значение **ID**, полученное на шаге 1.  
   Отозванный токен нельзя использовать для аутентификации, но он остаётся в окружении. Рекомендуем подождать неделю перед удалением отозванного токена на случай экстренной необходимости. Точную задержку смотрите в политиках безопасности вашей организации.  
   Если вы ротируете токен, которым сейчас аутентифицируете API-вызовы, замените его на новый токен из шага 2.
4. Удалите старый токен.

   После периода ожидания, когда старый токен отключён (отозван), удалите его. Для этого выполните [DELETE an existing token](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Удаление токена аутентификации Dynatrace API через Dynatrace API."). Понадобится **ID** токена, полученный на шаге 1.

## Пример ротации токена

Допустим, нужно ротировать токен со следующими параметрами:

* Имя токена: `ClusterTokenManager`.
* Scope токена: `Cluster token management`.
* Текущий токен: `0987654321jihgfedcba`.

С помощью Tokens API ротацию можно автоматизировать.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получить ID старого токена**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-1 "Ротация cluster management токенов через Cluster API.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создать новый токен**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-2 "Ротация cluster management токенов через Cluster API.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Отозвать старый токен**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-3 "Ротация cluster management токенов через Cluster API.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Удалить старый токен**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-4 "Ротация cluster management токенов через Cluster API.")

### Шаг 1. Получить ID старого токена

ID нужен, чтобы отозвать токен и затем удалить его.

Отправьте `POST`-запрос на `https://<your-domain>/api/cluster/v1/tokens/lookup`  
С payload `application/json`, где `0987654321jihgfedcba` — значение токена:

```
{



"token": "0987654321jihgfedcba"



}
```

Запрос вернёт метаданные токена в payload `application/json`:

```
{



"id": "3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5",



"name": "ClusterTokenManager",



"userId": "admin@mycluster.com",



"revoked": false,



"created": 1578902397474,



"lastUse": 1582130541813,



"scopes": [



"ClusterTokenManagement"



]



}
```

Сохраните значение **ID** токена (`3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`).  
Оно понадобится позже для отзыва и удаления токена.

### Шаг 2. Создать новый токен

Отправьте `POST`-запрос на `https://<your-domain>/api/cluster/v1/tokens`  
С payload `application/json`:

```
{



"name": "ClusterTokenManager",



"scopes": [



"ClusterTokenManagement"



],



"expiresIn": {



"value": 30,



"unit": "DAYS"



}



}
```

Запрос вернёт новый токен в payload `application/json`:

```
{



"token": "jihgfedcba0987654321"



}
```

### Шаг 3. Отозвать старый токен (3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5)

Сохранённый ID (шаг 1) токена, который нужно отозвать и затем удалить: `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`

Отправьте `PUT`-запрос с отзываемым токеном на `https://<your-domain>/api/cluster/v1/tokens/3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`  
С payload `application/json`:

```
{



"revoked": true



}
```

Об успешном запросе сигнализирует код ответа `204`. Тело ответа пустое.  
Токен с ID `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5` теперь отозван.

### Шаг 4. Удалить старый токен (3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5)

Чтобы удалить токен `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`, отправьте `DELETE`-запрос с ID отозванного токена на `https://<your-domain>/api/cluster/v1/tokens/3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`

Об успешном запросе сигнализирует код ответа `204`. Тело ответа пустое.  
Токен с ID `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5` теперь удалён.