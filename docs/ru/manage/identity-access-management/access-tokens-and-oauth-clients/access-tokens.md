---
title: Access tokens classic
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
scraped: 2026-03-05T21:27:58.397956
---

# Классические токены доступа

# Классические токены доступа

* Classic
* Справочник
* Чтение займёт 2 минуты
* Обновлено 25 октября 2023 г.

В этой статье рассматриваются токены доступа, используемые в предыдущих версиях Dynatrace для аутентификации в классических API конфигурации и окружения. Для работы с последней версией Dynatrace см. разделы [Токены платформы](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") и [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

Любой внешний доступ к вашей среде мониторинга Dynatrace основывается на двух элементах: [идентификаторе окружения](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") и *токене доступа*.

Dynatrace использует несколько типов токенов:

* Токены доступа и персональные токены доступа предоставляют доступ к:

  + [Dynatrace API](/docs/dynatrace-api "Find out what you need to use the Dynatrace API.")
  + Загрузке установщиков OneAgent и ActiveGate
* [Персональные токены доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.") предоставляют доступ к некоторым конечным точкам Dynatrace API
* [Токены арендатора](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") позволяют OneAgent передавать данные в Dynatrace

## Формат токена

Dynatrace использует уникальный формат токена, состоящий из трёх компонентов, разделённых точками (`.`).

### Пример токена

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Компоненты токена

### Префиксы токенов

Этот предсказуемый формат предоставляет следующие возможности:

* Использование перехватчиков pre-commit в Git для предотвращения отправки токенов в репозитории исходного кода (например, с помощью таких инструментов, как [git-secrets](https://github.com/awslabs/git-secrets))
* Определение правил маскировки для скрытия секретных частей токенов при записи в лог-файлы
* Обнаружение токенов во внутренних файлах или сообщениях
* Включение [службы сканирования секретов GitHub](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning#about-secret-scanning-for-public-repositories) для выявления токенов, загруженных в публичные репозитории GitHub

Используйте следующее регулярное выражение для поиска токенов:

```
dt0[a-zA-Z]{1}[0-9]{2}\.[A-Z0-9]{24}\.[A-Z0-9]{64}
```

С выпуском Dynatrace версии 1.210 этот формат включён по умолчанию (все вновь создаваемые токены будут использовать новый формат).

Все существующие токены старого формата остаются действительными.

### Отключение нового формата

В течение ограниченного времени можно отказаться от использования нового формата токенов:

1. Перейдите в **Settings > Integration > Token settings**.
2. Отключите **Create Dynatrace API tokens in the new format**.

## Генерация токена доступа

Чтобы сгенерировать токен доступа:

1. Перейдите в раздел ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя токена.
   Dynatrace не требует уникальности имён токенов. Можно создать несколько токенов с одинаковым именем. Обязательно давайте каждому токену понятное имя. Правильное именование помогает эффективно управлять токенами и при необходимости удалять их.
4. Выберите необходимые области действия для токена.
5. Нажмите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для последующего использования.

   Доступ к токену возможен только один раз — в момент его создания. Впоследствии просмотреть токен будет невозможно.

## Области действия токенов

Токены доступа имеют детальные области действия для ограничения доступа к определённым функциям продукта из соображений безопасности.

### OpenPipeline

### API v2

### API v1

### PaaS

### Прочее

## Связанные темы

* [Tokens API v1](/docs/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")
