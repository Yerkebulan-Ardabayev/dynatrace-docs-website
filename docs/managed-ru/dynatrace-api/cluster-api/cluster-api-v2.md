---
title: Cluster API v2
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2
scraped: 2026-05-12T11:03:06.172444
---

# Cluster API v2

# Cluster API v2

* Опубликовано: 10 февраля 2020

Dynatrace Managed предоставляет функциональность на уровне кластера через REST-эндпойнты. Эта интерактивная документация также работает как REST-клиент, через который можно взаимодействовать с кластерами Dynatrace Managed.

Чтобы перейти к Cluster API

1. Откройте Cluster Management Console.
2. Откройте меню пользователя, нажав на иконку пользователя в правом верхнем углу.
3. Выберите **Cluster API v2**.

### Окружения

[Получить список всех существующих окружений](/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/list-managed-environments "Через Dynatrace API получите список всех существующих окружений.")

[Создать новое окружение](/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/create-managed-environment "Через Dynatrace API создайте новое окружение.")

[Получить свойства конкретного окружения](/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/list-specific-managed-environment "Через Dynatrace API получите свойства указанного окружения.")

[Обновить конкретное окружение](/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/update-specific-managed-environment "Через Dynatrace API обновите конкретное окружение.")

[Удалить конкретное окружение](/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/delete-specific-managed-environment "Через Dynatrace API удалите конкретное окружение.")

### Synthetic-локации и узлы

[Получить список всех приватных Synthetic-локаций кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all-locations "Получите список всех Synthetic-локаций через Synthetic v2 API в Dynatrace Managed.")

[Создать новые приватные Synthetic-локации](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location "Создайте приватную Synthetic-локацию через Synthetic API v2 в Dynatrace Managed.")

[Получить свойства указанных локаций кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-a-location "Получите параметры Synthetic-локации через Synthetic API v2 в Dynatrace Managed.")

[Обновить указанную приватную Synthetic-локацию кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location "Обновите приватную Synthetic-локацию через Synthetic API v2 в Dynatrace Managed.")

[Удалить указанную приватную Synthetic-локацию кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/delete-a-location "Удалите приватную Synthetic-локацию через Synthetic API v2 в Dynatrace Managed.")

[Получить список всех Synthetic-узлов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all "Получите список всех Synthetic-узлов через Synthetic API v2 в Dynatrace Managed.")

[Получить свойства указанных Synthetic-узлов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-node "Получите параметры Synthetic-узла через Synthetic API v2 в Dynatrace Managed.")

### Токены

[Получить список доступных токенов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-tokens "Узнайте, как через Dynatrace API получить список доступных токенов аутентификации Dynatrace Cluster API.")

[Создать новый токен кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens "Узнайте, как создать новый токен Dynatrace Cluster через API.")

[Обновить токен кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/update-cluster-token "Узнайте, как обновить токен Dynatrace Cluster через API.")

[Удалить токен кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/delete-cluster-token "Узнайте, как удалить токен Dynatrace Cluster через API.")

[Получить метаданные токена кластера по запросу](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-req "Узнайте, как получить метаданные токена по значению токена в запросе через API.")

[Получить метаданные токена кластера по ID](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-para "Узнайте, как получить метаданные токена по ID токена через API.")

### Управление пользователями

[Получить конфигурацию пользовательских сессий кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions-configuration "Узнайте, как получить конфигурацию пользовательских сессий через Cluster API.")

[Обновить конфигурацию пользовательских сессий кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration "Узнайте, как обновить конфигурацию пользовательских сессий Dynatrace Cluster через API.")

[Получить пользовательские сессии кластера](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions "Узнайте, как получить пользовательские сессии через Cluster API.")

[Удалить пользовательские сессии конкретного пользователя](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/delete-cluster-user-session "Узнайте, как удалить пользовательские сессии Dynatrace Cluster для конкретного пользователя через API.")

### Удалённый доступ

[Получить все запросы на доступ к кластеру](/managed/dynatrace-api/cluster-api/cluster-api-v2/remote-access/get-all-cluster-access-requests "Узнайте, как получить все запросы на доступ к кластеру.")

[Выдать разрешение на удалённый доступ](/managed/dynatrace-api/cluster-api/cluster-api-v2/remote-access/post-remote-access-permission "Узнайте, как выдать разрешение на удалённый доступ через Cluster API v2.")

[Получить запрос на доступ к кластеру](/managed/dynatrace-api/cluster-api/cluster-api-v2/remote-access/get-cluster-access-request "Узнайте, как получить запрос на доступ к кластеру.")

[Изменить состояние запроса на доступ](/managed/dynatrace-api/cluster-api/cluster-api-v2/remote-access/put-change-access-request-state "Узнайте, как изменить состояние запроса на доступ через Cluster API v2.")

### Лицензия

[Экспортировать данные лицензии](/managed/dynatrace-api/cluster-api/cluster-api-v2/export-license-data/get-export-license-data "Узнайте, как экспортировать агрегированное по часам использование лицензии в виде ZIP-файла.")

### Log Monitoring

[Получить статус Log Monitoring](/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/get-log-monitoring-status "Узнайте, как получить статус Log Monitoring в развёртываниях Managed через API.")

[Обновить лимит log events на кластер для Log Monitoring](/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring "Узнайте, как обновить общий лимит log events на кластер с учётом размера ресурсов кластера через API.")