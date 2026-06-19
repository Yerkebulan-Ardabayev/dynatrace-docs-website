---
title: Миграция с манифестов на Helm для установки Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm
scraped: 2026-05-12T12:09:41.583818
---

# Миграция с манифестов на Helm для установки Dynatrace Operator

# Миграция с манифестов на Helm для установки Dynatrace Operator

* Чтение: 1 мин
* Опубликовано 22 июля 2024 г.

В этом руководстве описаны шаги, необходимые для миграции с использования манифестов на Helm. Этот подход упрощает процесс развёртывания и настройку Dynatrace Operator.

Для успешной миграции необходимо полностью удалить и переустановить Dynatrace Operator и его компоненты. Действуйте осторожно, так как это удалит и заново развернёт все компоненты, управляемые Dynatrace Operator.

Чтобы обеспечить чистую миграцию:

1. Удалите все развёрнутые пользовательские ресурсы Dynatrace, такие как EdgeConnect и DynaKube.

   ```
   kubectl delete edgeconnect --all



   kubectl delete dynakube --all
   ```
2. [Удаление Dynatrace Operator через манифесты](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#manifest-uninstall "Процедуры обновления и удаления Dynatrace Operator").

1. Установите Dynatrace Operator через Helm. Подробнее об инструкциях по установке см. [Начало работы с полной наблюдаемостью](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed#helm "Развёртывание Dynatrace Operator в режиме cloud-native full-stack в Kubernetes").

   Если вы используете Helm версии 4.0+, необходимо использовать `--rollback-on-failure` вместо флага `--atomic`.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --version <desired-version> \



   --create-namespace \



   --namespace dynatrace \



   --atomic
   ```

1. Заново разверните пользовательские ресурсы Dynatrace.

   ```
   kubectl apply -f edgeconnect.yaml



   kubectl apply -f dynakube.yaml
   ```