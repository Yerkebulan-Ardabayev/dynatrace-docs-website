---
title: Миграция Dynatrace Operator в новую среду
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant
scraped: 2026-03-06T21:30:30.280689
---

* Latest Dynatrace

Если вы в настоящее время осуществляете мониторинг кластера Kubernetes с помощью Dynatrace OneAgent, развёрнутого через Dynatrace Operator, и вам необходимо перейти на другую среду Dynatrace, выберите один из следующих вариантов в соответствии с используемым методом развёртывания.

Kubernetes

OpenShift

1. Удалите существующий DynaKube (начиная с версии Dynatrace Operator 1.3.0 редактирование `spec.apiUrl` не допускается).

   ```
   kubectl delete dynakube dynakube -n dynatrace
   ```
2. Удалите существующий секрет, содержащий токены Dynatrace Operator и Data Ingest для аутентификации в кластере Dynatrace.

   ```
   kubectl delete secret dynakube -n dynatrace
   ```
3. Создайте новый секрет на основе новых токенов из вашей новой среды.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените новый DynaKube с обновлённым `spec.apiUrl`.

   ```
   kubectl apply -f dynakube.yaml
   ```
5. Перезапустите ваши приложения.

1. Удалите существующий DynaKube (начиная с версии Dynatrace Operator 1.3.0 редактирование `spec.apiUrl` не допускается).

   ```
   oc delete dynakube dynakube -n dynatrace
   ```
2. Удалите существующий секрет, содержащий токены Dynatrace Operator и Data Ingest для аутентификации в кластере Dynatrace.

   ```
   oc delete secret dynakube -n dynatrace
   ```
3. Создайте новый секрет на основе новых токенов из вашей новой среды.

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Примените новый DynaKube с обновлённым `spec.apiUrl`.

   ```
   oc apply -f dynakube.yaml
   ```
5. Перезапустите ваши приложения.
