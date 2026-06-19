---
title: Миграция Dynatrace Operator в новое окружение
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant
scraped: 2026-05-12T12:08:59.979488
---

# Миграция Dynatrace Operator в новое окружение

# Миграция Dynatrace Operator в новое окружение

* Чтение: 2 мин
* Обновлено 5 сентября 2025 г.

Если вы в настоящее время отслеживаете кластер Kubernetes с помощью Dynatrace OneAgent, развёрнутого через Dynatrace Operator, и вам нужно выполнить миграцию в другое окружение Dynatrace, выберите один из следующих вариантов в зависимости от метода развёртывания.

Kubernetes

OpenShift

1. Удалите существующий DynaKube (начиная с версии Dynatrace Operator 1.3.0, изменение `spec.apiUrl` не допускается).

   ```
   kubectl delete dynakube dynakube -n dynatrace
   ```
2. Удалите существующий секрет, содержащий токены Dynatrace Operator и Data Ingest для аутентификации в Dynatrace Cluster.

   ```
   kubectl delete secret dynakube -n dynatrace
   ```
3. Создайте новый секрет на основе новых токенов из вашего нового окружения.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените новый DynaKube с обновлённым `spec.apiUrl`.

   ```
   kubectl apply -f dynakube.yaml
   ```
5. Перезапустите ваши приложения.

1. Удалите существующий DynaKube (начиная с версии Dynatrace Operator 1.3.0, изменение `spec.apiUrl` не допускается).

   ```
   oc delete dynakube dynakube -n dynatrace
   ```
2. Удалите существующий секрет, содержащий токены Dynatrace Operator и Data Ingest для аутентификации в Dynatrace Cluster.

   ```
   oc delete secret dynakube -n dynatrace
   ```
3. Создайте новый секрет на основе новых токенов из вашего нового окружения.

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените новый DynaKube с обновлённым `spec.apiUrl`.

   ```
   oc apply -f dynakube.yaml
   ```
5. Перезапустите ваши приложения.