---
title: Cluster API - Токены и аутентификация
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-authentication
scraped: 2026-05-12T11:24:01.272452
---

# Cluster API - Токены и аутентификация

# Cluster API - Токены и аутентификация

* Published Feb 28, 2020

Dynatrace Managed использует два типа API-токенов:

* Токен environment token management — для управления токенами окружений на основе ID окружения, переданного в API-вызове.
* Cluster API token — для управления кластером, даже если в нём несколько окружений. Это самый распространённый тип токена в Dynatrace Managed.

## Environment token management

Токен environment token management используется для аутентификации при вызове endpoint [Create new Cluster token](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens "Создание нового Dynatrace Cluster token через API."). Он позволяет создавать токен со scope `TokenManagement` для заданного окружения. Этот токен полезен при автоматизации создания токенов для большого числа окружений.

Короткий срок жизни

Из-за потенциального влияния на безопасность кластера и всех его окружений этот токен действителен только 24 часа.

### Генерация токена environment token management

Чтобы создать токен environment token management:

1. Перейдите в **Settings** > **API tokens**.
2. В разделе **Environment token management tokens** нажмите **Generate token**.
3. Введите имя токена.
4. Нажмите **Save**.
5. Нажмите **Copy**, чтобы скопировать токен, и вставьте его в безопасное место.

## Cluster configuration token

Cluster configuration token — это токен для работы с endpoint [Cluster API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1 "API для управления окружениями, network zones, synthetic locations, узлами и токенами.") или [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Управление окружениями, network zones, Synthetic locations, узлами и токенами в Dynatrace Managed через Cluster API v2."). Доступны следующие scopes:

* Cluster token management
* Service Provider API
* Read settings
* Write settings

Для аутентификации в Cluster API нужен действительный API-токен. Доступ к API контролируется через scope: токену также нужно назначить соответствующие разрешения. Смотрите описание каждого запроса, чтобы узнать необходимые разрешения.

### Генерация токена для cluster configuration

Чтобы создать cluster API token:

1. Перейдите в **Settings** > **API tokens**.
2. В разделе **Cluster tokens** нажмите **Generate token**.
3. Введите имя токена.
4. Dynatrace предоставляет следующие разрешения для API-токенов. Их можно задать в UI описанным выше способом или через Tokens API. Можно назначить несколько разрешений одному токену или сгенерировать несколько токенов с разным уровнем доступа: ориентируйтесь на политики безопасности вашей организации, чтобы выбрать лучший подход. Рекомендуем выдавать токенам один dedicated scope, чтобы ограничить потенциальный ущерб при утечке.

   | Название | API value | Описание |
   | --- | --- | --- |
   | Cluster token management | `ClusterTokenManagement` | Доступ к Tokens API и управление токенами. |
   | Service Provider API | `ServiceProviderAPI` | Доступ к операциям Cluster Management API. |
   | Read settings | `settings.read` | Разрешение на чтение настроек кластера (API v2). |
   | Write settings | `settings.write` | Разрешение на запись настроек кластера (API v2). |
5. Нажмите **Save**.
6. Нажмите **Copy**, чтобы скопировать токен, и вставьте его в безопасное место.

## Аутентификация

API-вызов можно аутентифицировать двумя способами: per call через HTTP-заголовок или query-параметр, либо per login через экран Cluster API.

### HTTP-заголовок

Можно аутентифицироваться, передав токен в HTTP-заголовке **Authorization** с realm **Api-Token**.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

Следующий пример показывает аутентификацию через HTTP-заголовок.

```
curl --request GET \



--url https://myManaged.cluster.com/api/cluster/v1/tokens \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

### Query-параметр

Можно аутентифицироваться, передав токен в качестве значения query-параметра **api-token**.

```
curl --request GET \



--url 'https://myManaged.cluster.com/api/cluster/v1/tokens?limit=1000&user=Pete&permissions=ClusterTokenManagement&api-token=abcdefjhij1234567890' \
```

### Экран Cluster API

1. В правом верхнем углу откройте user menu и выберите **Cluster Management API**.
2. В выпадающем меню в верхней панели выберите API definition: **Cluster Management API** или **Cluster API**.
3. В API explorer нажмите **Authorize**.  
   Появится диалог **Available authorizations**.
4. Вставьте токен в поле **Value** и нажмите **Authorize**.  
   Завершив, в том же диалоге можно нажать **Logout**, чтобы прекратить аутентификацию.