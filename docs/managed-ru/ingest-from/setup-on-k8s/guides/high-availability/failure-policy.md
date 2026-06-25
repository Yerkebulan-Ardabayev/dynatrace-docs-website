---
title: Настройка политики отказа
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/failure-policy
scraped: 2026-05-12T12:09:31.713687
---

# Настройка политики отказа

# Настройка политики отказа

* Чтение: 1 мин
* Опубликовано 28 июля 2023 г.

Dynatrace Operator версии 0.11.0+

Убедитесь, что поды CSI-драйвера OneAgent запущены и работают.

Политика отказа определяет, что должно происходить, когда внедрение OneAgent не удаётся для конкретного пода в кластере Kubernetes. По умолчанию политика отказа установлена в значение `silent`. Вы можете переопределить политику отказа для всех инжектируемых подов, соответствующих DynaKube, задав для `feature.dynatrace.com/injection-failure-policy` одно из следующих значений.

* `silent`: если внедрение OneAgent не удаётся для конкретного пода, под продолжит работу без мониторинга.
* `fail`: если внедрение OneAgent не удаётся для конкретного пода, под не запустится, а сбой внедрения будет расценён как ошибка.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/injection-failure-policy: [fail|silent]
```