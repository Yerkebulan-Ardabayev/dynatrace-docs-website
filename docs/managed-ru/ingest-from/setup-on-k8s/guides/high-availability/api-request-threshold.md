---
title: Настройка минимального интервала между запросами
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/api-request-threshold
scraped: 2026-05-12T12:09:33.527764
---

# Настройка минимального интервала между запросами

# Настройка минимального интервала между запросами

* Чтение: 1 мин
* Опубликовано 28 июля 2023 г.

Dynatrace Operator версии 1.2.0+

В версиях Dynatrace Operator с 0.11.0 до 1.2.0 эта конфигурация задавалась с помощью аннотации feature.dynatrace.com/dynatrace-api-request-threshold.

Dynatrace Operator регулярно обращается к Dynatrace, чтобы собирать информацию, необходимую для корректной работы.

Минимальный интервал между запросами от Dynatrace Operator, ранее жёстко заданный как 15 минут для снижения нагрузки на сеть, теперь можно настроить.

Чтобы задать этот интервал (в минутах), укажите поле `dynatraceApiRequestThreshold`.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



dynatraceApiRequestThreshold: 15



...
```

Operator выполняет три различных типа запросов:

* сведения о подключении ActiveGate
* сведения о подключении OneAgent
* проверка области действия токена

Указанный интервал отсчитывается независимо для каждого из этих типов запросов.