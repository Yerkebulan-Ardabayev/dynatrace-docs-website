---
title: Tokens API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1
scraped: 2026-05-12T12:01:20.905613
---

# Tokens API v1

# Tokens API v1

* Reference
* Updated on May 17, 2022

Этот API устарел. Используйте [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Управление токенами аутентификации Dynatrace API.") вместо него.

API **Tokens** позволяет управлять токенами аутентификации Dynatrace API в вашем окружении.

### Список всех токенов

[Получить обзор](/managed/dynatrace-api/environment-api/tokens-v1/get-all-tokens "Узнайте, как использовать Dynatrace API для получения списка всех токенов аутентификации Dynatrace API.") всех токенов, доступных в вашем окружении.

### Просмотр токена

Получить метаданные токена либо [по его ID](/managed/dynatrace-api/environment-api/tokens-v1/get-token-metadata "Узнайте, как использовать Dynatrace API для получения метаданных токена аутентификации Dynatrace API."), либо [по самому токену](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Узнайте, как использовать Dynatrace API для поиска метаданных токена аутентификации Dynatrace API.").

### Создание токена

[Создать новый токен](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Узнайте, как использовать Dynatrace API для создания нового токена аутентификации Dynatrace API.") с заданным scope и сроком действия.

### Редактирование токена

[Обновить](/managed/dynatrace-api/environment-api/tokens-v1/put-token "Узнайте, как использовать Dynatrace API для обновления токена аутентификации Dynatrace API.") существующий токен. Можно отозвать токен или изменить его scope.

### Удаление токена

[Удалить токены](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Узнайте, как удалить токен аутентификации Dynatrace API через Dynatrace API."), которые больше не нужны окружению.

---

### Внедрение ротации токенов

[Настройка](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation "Узнайте, как использовать Dynatrace API для регулярной ротации токенов аутентификации Dynatrace API в окружении.") регулярного обновления токенов.

### Поиск и удаление скомпрометированного токена

[Найти и удалить](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token "Узнайте, как найти и заменить скомпрометированный токен аутентификации Dynatrace API через Dynatrace API.") скомпрометированный токен.