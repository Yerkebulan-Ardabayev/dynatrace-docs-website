---
title: Enable Kubernetes experience for existing clusters
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/enable-k8s-experience/existing-clusters
scraped: 2026-02-06T16:19:46.615282
---

# Включить Kubernetes для существующих кластеров.

# Включить Kubernetes для существующих кластеров.

* Последняя версия Dynatrace
* Практическое руководство
* 1 минута чтения
* Опубликовано 19 января 2024 г.

У вас есть возможность включить все или определенные кластеры Kubernetes для использования новых возможностей Kubernetes.

Это можно сделать с помощью API настроек с помощью [Таблица схемы приложения Kubernetes](/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes "View builtin:app-transition.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") или, альтернативно, настроив параметр, как описано ниже.

## Включить все кластеры

1. Откройте ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Настройки** > **Сбор и захват** > **Облако и виртуализация** > ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Включите **Новый опыт Kubernetes**.

## Включить определенные кластеры

1. В ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** выберите **Ожидание активации** в верхней строке меню.
2. Выберите **Активировать** для нужного кластера.

![Ожидается активация](https://dt-cdn.net/images/activation-pending-3718-f43bc57878.png)
3. Включите **Новый опыт Kubernetes**.

Когда вы включаете кластеры Kubernetes для нового опыта Kubernetes, Dynatrace начинает передавать данные наблюдения на платформу Dynatrace, включая Grail в качестве озера данных.