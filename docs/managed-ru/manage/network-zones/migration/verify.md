---
title: Проверка развёртывания сетевых зон (миграция)
source: https://docs.dynatrace.com/managed/manage/network-zones/migration/verify
scraped: 2026-05-12T11:52:26.908575
---

# Проверка развёртывания сетевых зон (миграция)

# Проверка развёртывания сетевых зон (миграция)

* Чтение 1 мин
* Опубликовано 28 янв 2020 г.

После завершения развёртывания убедитесь, что соединения работают как предполагалось, проверив количество OneAgent и ActiveGate в каждой сетевой зоне. Это можно сделать через Dynatrace API:

* Dynatrace SaaS: используйте вызовы сетевых зон из [Environment API](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API.").
* Dynatrace Managed: используйте вызовы сетевых зон из [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Узнайте об управлении окружениями, сетевыми зонами, Synthetic-расположениями, узлами и токенами в Dynatrace Managed с помощью Cluster API v2.").