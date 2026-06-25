---
title: Service detection API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules
scraped: 2026-05-12T11:04:40.722571
---

# Service detection API

# Service detection API

* Reference
* Published Jun 19, 2019

API **Rule-based service detection** позволяет управлять конфигурацией правил обнаружения сервисов.

### Список всех

Обзор всех правил обнаружения сервисов для:

* [Полные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-all "Просмотр всех правил обнаружения сервисов для полных веб-запросов через Dynatrace API.")
* [Непрозрачные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-all "Просмотр всех правил обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.")
* [Полные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-all "Просмотр всех правил обнаружения сервисов для полных веб-сервисов через Dynatrace API.")
* [Непрозрачные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-all "Просмотр всех правил обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.")

### Просмотр правила

Получить параметры правила обнаружения сервисов для:

* [Полные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-a-rule "Просмотр правила обнаружения сервисов для полных веб-запросов через Dynatrace API.")
* [Непрозрачные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-a-rule "Просмотр правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.")
* [Полные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-a-rule "Просмотр правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.")
* [Непрозрачные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-rule "Просмотр правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.")

### Изменение порядка правил

Правила обнаружения сервисов выполняются одно за другим. Применяется первое совпавшее правило, дальнейшая обработка прекращается. Измените порядок правил обнаружения сервисов, чтобы получить нужный порядок выполнения.

* [Полные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/reorder-rules "Изменение порядка правил обнаружения сервисов для полных веб-запросов через Dynatrace API.")
* [Непрозрачные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/reorder-rules "Изменение порядка правил обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.")
* [Полные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/reorder-rules "Изменение порядка правил обнаружения сервисов для полных веб-сервисов через Dynatrace API.")
* [Непрозрачные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/reorder-rules "Изменение порядка правил обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.")

### Создание правила

Создать новое правило обнаружения сервисов для:

* [Полные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/post-a-rule "Создание правила обнаружения сервисов для полных веб-запросов через Dynatrace API.")
* [Непрозрачные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/post-a-rule "Создание правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.")
* [Полные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/post-a-rule "Создание правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.")
* [Непрозрачные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/post-rule "Создание правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.")

### Редактирование правила

Обновить существующее правило обнаружения сервисов или создать новое правило с указанным ID.

* [Полные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/put-a-rule "Редактирование правила обнаружения сервисов для полных веб-запросов через Dynatrace API.")
* [Непрозрачные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/put-a-rule "Редактирование правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.")
* [Полные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/put-a-rule "Редактирование правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.")
* [Непрозрачные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/put-rule "Редактирование правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.")

### Удаление правила

Удалить правило обнаружения сервисов, которое вам больше не нужно.

* [Полные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/del-a-rule "Удаление правила обнаружения сервисов для полных веб-запросов через Dynatrace API.")
* [Непрозрачные веб-запросы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/del-a-rule "Удаление правила обнаружения сервисов для непрозрачных и внешних веб-запросов через Dynatrace API.")
* [Полные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/del-a-rule "Удаление правила обнаружения сервисов для полных веб-сервисов через Dynatrace API.")
* [Непрозрачные веб-сервисы](/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/delete-rule "Удаление правила обнаружения сервисов для внешних и непрозрачных веб-сервисов через Dynatrace API.")

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")