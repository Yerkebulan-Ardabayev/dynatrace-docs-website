---
title: Kubernetes credentials API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api
scraped: 2026-05-12T12:10:20.761560
---

# Kubernetes credentials API

# Kubernetes credentials API

* Reference
* Published Jun 27, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "Просмотр таблицы schema builtin:cloud.kubernetes окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes`) и [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "Просмотр таблицы schema builtin:cloud.kubernetes.monitoring окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`).

[### Список всех credentials

Обзор всех Kubernetes credentials, сохранённых в вашем окружении.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-all "Просмотр всех конфигураций Kubernetes credentials вашего окружения мониторинга через Dynatrace API.")[### Просмотр credentials

Получить конфигурацию credentials по ID конфигурации.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-credentials "Просмотр конфигурации Kubernetes credentials через Dynatrace API.")

[### Создание credentials

Создать новую конфигурацию credentials с нужными параметрами.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/post-new-credentials "Создание конфигурации Kubernetes credentials через Dynatrace API.")[### Редактирование credentials

Обновить существующую конфигурацию Kubernetes credentials. Также можно создать новые credentials с указанным ID.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/put-credentials "Редактирование конфигурации Kubernetes credentials через Dynatrace API.")[### Удаление credentials

Удалить ненужную конфигурацию credentials.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/delete-credentials "Удаление конфигурации Kubernetes credentials через Dynatrace API.")

## Связанные темы

* [Explore Kubernetes in Dynatrace Hub](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)