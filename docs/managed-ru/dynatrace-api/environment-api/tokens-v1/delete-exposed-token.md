---
title: Поиск и замена раскрытого токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token
scraped: 2026-05-12T12:11:19.795699
---

# Поиск и замена раскрытого токена

# Поиск и замена раскрытого токена

* Справочник
* Обновлено 17 мая 2022 г.

Если какой-либо из ваших токенов аутентификации Dynatrace API скомпрометирован (становится доступен публично) по любой причине, немедленно прекратите его использовать, удалите его как можно скорее и выпустите токен на замену по необходимости. Token API удобен для этой задачи.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получение ID раскрытого токена**](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token#get-old "Узнайте, как найти и заменить раскрытый токен аутентификации Dynatrace API с помощью Dynatrace API.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Удаление раскрытого токена**](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token#delete-old "Узнайте, как найти и заменить раскрытый токен аутентификации Dynatrace API с помощью Dynatrace API.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Создание нового токена для замены скомпрометированного**](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token#create-new "Узнайте, как найти и заменить раскрытый токен аутентификации Dynatrace API с помощью Dynatrace API.")

## Шаг 1 Получение ID раскрытого токена

Чтобы удалить токен, нужно получить его ID. Для этого выполните запрос [POST token lookup](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Узнайте, как использовать Dynatrace API для поиска метаданных токена аутентификации Dynatrace API.") с удаляемым токеном в качестве payload.

Запрос вернёт метаданные токена. Из метаданных вам понадобится:

* **ID** токена, чтобы удалить его.
* **userID** владельца токена, чтобы уведомить пользователя о том, что токен больше неработоспособен.
* **scope** токена, чтобы создать токен на замену.

#### Запрос

Отправьте POST-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/lookup
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/lookup

Отправьте его с payload `application/json` вида, где `0987654321jihgfedcba`, это токен:

```
{



"token": "0987654321jihgfedcba"



}
```

#### Ответ

Запрос возвращает метаданные токена в payload `application/json`:

```
{



"id": "a6e91657-1fa7-4742-af40-39469b92bd65",



"name": "John's token",



"userId": "john@mysampleenv.com",



"created": "2019-03-06T09:15:49Z",



"expires": "2019-04-05T09:15:49Z",



"scopes": [



"DataExport",



"ExternalSyntheticIntegration"



]



}
```

Из этих данных вам нужно получить **id**, который необходим для удаления этого токена.

## Шаг 2 Удаление раскрытого токена

Теперь удалите скомпрометированный токен. Для этого выполните [DELETE an existing token](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Узнайте, как удалить токен аутентификации Dynatrace API с помощью Dynatrace API."). Вам понадобится значение **id**, полученное на [шаге 1](#get-old).

В нашем примере ID удаляемого токена, это **a6e91657-1fa7-4742-af40-39469b92bd65**.

#### Запрос

Отправьте DELETE-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65

#### Ответ

Об успешном запросе сигнализирует код ответа **204**. Он не возвращает никакого содержимого.

## Шаг 3 Создание нового токена

Чтобы создать новый токен взамен раскрытого, выполните запрос [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Узнайте, как использовать Dynatrace API для создания нового токена аутентификации Dynatrace API."). Обязательно назначьте ему тот же scope.

Когда новый токен создан, передайте его пользователю в соответствии с политикой безопасности вашей организации.

#### Запрос

Отправьте POST-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens

Включите этот payload `application/json`:

```
{



"name": "John's token",



"scopes": [



"DataExport",



"ExternalSyntheticIntegration"



],



"expiresIn": {



"value": 30,



"unit": "DAYS"



}



}
```

#### Ответ

Запрос возвращает новый токен в payload `application/json`:

```
{



"token": "jihgfedcba0987654321"



}
```