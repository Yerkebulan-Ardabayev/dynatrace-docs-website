---
title: OAuth-клиенты
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients
scraped: 2026-05-12T11:13:51.624163
---

# OAuth-клиенты

# OAuth-клиенты

* Reference
* 2-min read
* Updated on Aug 05, 2025

OAuth-клиенты предоставляют учётные данные клиента в соответствии со стандартом OAuth. Учётными данными управляют администраторы Dynatrace; они используются для автоматизации управления учётными записями.

## Создание OAuth2-клиента

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/). Если у вас несколько учётных записей, выберите нужную.
2. На верхней панели навигации выберите **Identity & access management** > **OAuth clients**.
3. Нажмите **Create client**.
4. Укажите email пользователя, которому принадлежит клиент.
5. Введите описание нового клиента.
6. Выберите необходимые разрешения.  
   Это области доступа, которые клиент сможет предоставлять. Токены, созданные клиентом, могут иметь другие наборы областей.
7. Нажмите **Create client**.
8. Скопируйте сгенерированные данные в буфер обмена. Сохраните их в менеджере паролей для дальнейшего использования.

   Доступ к секрету клиента предоставляется только один раз при создании. Впоследствии просмотреть его невозможно.

## Запрос токена

После создания OAuth2-клиента запросите bearer-токен из системы Dynatrace SSO через вызов API.

|  |  |
| --- | --- |
| POST | `https://sso.dynatrace.com/sso/oauth2/token` |
| Content type | `application/x-www-form-urlencoded` |

Укажите следующие параметры в теле запроса. Обязательно выполните URL-кодирование всех значений.

| Параметр | Значение |
| --- | --- |
| grant\_type | `client_credentials` |
| client\_id | `{your-Client-ID}` |
| client\_secret | `{your-Client-secret}` |
| scope | Список необходимых областей доступа, разделённых пробелами, например `account-uac-read account-uac-write`.  Можно назначить несколько областей одному токену или сгенерировать несколько токенов с разными уровнями доступа и использовать их соответственно — проверьте политики безопасности вашей организации для выбора оптимального подхода. |
| resource | `urn:dtaccount:{your-account-UUID}` |

## Ответ

В этом примере ответ запроса содержит bearer-токен, который необходимо передавать при вызовах API.

```
{



"token_type": "Bearer",



"resource": "urn:dtaccount:{dynatrace-account-urn}",



"access_token": "{your-bearer-token}",



"expires_in": 300,



"scope": "app-engine:apps:run storage:buckets:read storage:logs:read"



}
```

| Параметр | Значение |
| --- | --- |
| token\_type | Обязательный. Тип выданного токена. Как правило, строка Bearer. |
| resource | Обязательный. Определяет целевой ресурс или контекст учётной записи, для которого действителен токен. |
| access\_token | Обязательный. Фактический токен, используемый для аутентификации API-запросов, выданный сервером авторизации. |
| expires\_in | Рекомендуемый. Срок действия токена в секундах. |
| scope | Необязательный. Определяет разрешения, предоставленные токену доступа. |

## Аутентификация

Для аутентификации вызова прикрепите токен к HTTP-заголовку **Authorization** перед областью **Bearer**.

```
--header 'Authorization: Bearer abcdefjhij1234567890'
```

Пример аутентификации:

```
curl --request GET \



--url https://api.dynatrace.com/env/v1/accounts/{accountUuid}/environments \



--header 'Authorization: Bearer abcdefjhij1234567890' \
```