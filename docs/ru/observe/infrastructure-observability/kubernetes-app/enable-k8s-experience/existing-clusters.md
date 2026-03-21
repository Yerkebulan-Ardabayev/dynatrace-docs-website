---
title: Включение опыта Kubernetes для существующих кластеров
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience/existing-clusters
scraped: 2026-03-06T21:12:00.286290
---

# Включение Kubernetes experience для существующих кластеров


* Latest Dynatrace
* How-to guide
* 1-min read

У вас есть возможность включить новый Kubernetes experience для всех или отдельных кластеров Kubernetes.

Это можно сделать с помощью Settings API с использованием [таблицы схем приложения Kubernetes](../../../../dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes.md "View builtin:app-transition.kubernetes settings schema table of your monitoring environment via the Dynatrace API."), либо путём настройки параметра, описанного ниже.

Чтобы полностью отключить Kubernetes experience и прекратить мониторинг Kubernetes или связанное потребление лицензий, убедитесь, что параметр отключён как на уровне среды, так и на уровне кластера.

## Включение всех кластеров

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Включите **New Kubernetes experience**.

## Включение отдельных кластеров

1. В ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** выберите **Activation pending** в верхней панели меню.
2. Нажмите **Activate** для нужного кластера.

   ![Activation pending](https://dt-cdn.net/images/activation-pending-3718-f43bc57878.png)
3. Включите **New Kubernetes experience**.

После включения кластеров Kubernetes для нового Kubernetes experience Dynatrace начинает передавать данные наблюдаемости на платформу Dynatrace, включая Grail как хранилище данных.
