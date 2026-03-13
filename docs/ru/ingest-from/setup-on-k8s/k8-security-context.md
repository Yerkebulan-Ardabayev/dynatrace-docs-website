---
title: Set up Grail permissions for telemetry from Kubernetes and Kubernetes workloads
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/k8-security-context
scraped: 2026-03-05T21:36:49.757968
---

# Настройка разрешений Grail для телеметрии из Kubernetes и рабочих нагрузок Kubernetes

# Настройка разрешений Grail для телеметрии из Kubernetes и рабочих нагрузок Kubernetes

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Обновлено 20 ноября 2025 г.

В Dynatrace реализована [модель разрешений для Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Узнайте, как назначать разрешения для бакетов и таблиц в Grail."). Она распространяется на все телеметрические данные: метрики, события, спаны и журналы.

Рекомендуется настраивать разрешения в соответствии с организационной структурой и областями развёртывания. Подходящими концепциями являются группы хостов, кластеры Kubernetes и пространства имён Kubernetes. Как правило, эти атрибуты доступны для всех телеметрических данных, поступающих через методы сбора Dynatrace: OneAgent, OpenTelemetry или оператор Kubernetes. Следовательно, их можно использовать для включения [разрешений на уровне записей](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.").

Для развёртываний на основе Kubernetes убедитесь, что в Dynatrace Operator включено [обогащение метаданными](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes, прикрепляя соответствующие метаданные к сущностям: подам, хостам и процессам для улучшения наблюдаемости.").

Если требуется только базовая концепция разрешений, наилучшим вариантом является настройка разрешений на уровне бакетов. Затем можно маршрутизировать данные в нужный бакет в OpenPipeline, сопоставив одно из указанных первичных полей Grail, связанных с развёртыванием.

Для более тонкого управления в Dynatrace можно настроить границы политики с более детальными ограничениями на уровне данных. По умолчанию доступны следующие атрибуты:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Любой другой атрибут, перечисленный в [модели разрешений](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.")

Dynatrace предоставляет полноценную модель разрешений для Grail, распространяющуюся на все телеметрические данные, включая метрики, журналы, спаны и события.

## Настройка контекста безопасности в Kubernetes

Возможно, у вас уже определены собственные границы безопасности вне Dynatrace, которые заданы в виде меток или аннотаций Kubernetes. Если разрешений на уровне кластера или пространства имён Kubernetes недостаточно, Dynatrace позволяет настроить более детальные разрешения, используя собственные метки или аннотации Kubernetes в качестве источника [контекста безопасности](/docs/manage/identity-access-management/use-cases/access-security-context "Предоставление доступа к сущностям с использованием контекста безопасности") в Dynatrace.

Этот контекст безопасности может отражать вашу собственную архитектуру безопасности и даже быть иерархическим, если закодировать это в строку вида `department-A/department-AB/team-C`.

### Контекст безопасности на основе существующих меток или аннотаций пространства имён (рекомендуется)

С помощью функции обогащения метаданными Kubernetes можно использовать уже существующие метки и аннотации пространства имён в качестве источника контекста безопасности. Достаточно выбрать существующую метку, и она будет добавлена как `dt.security_context` к телеметрии.

Чтобы включить эту функцию, убедитесь, что в Dynatrace Operator включено [обогащение метаданными](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes, прикрепляя соответствующие метаданные к сущностям: подам, хостам и процессам для улучшения наблюдаемости.").

Подробнее см. [Использование настроек для применения существующих меток и аннотаций](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#enrichment-options "Руководства по обогащению телеметрии в Kubernetes").

### Контекст безопасности на основе выделенных аннотаций подов

[Выделенные аннотации подов](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#dedicated-annotations "Руководства по обогащению телеметрии в Kubernetes") предназначены только для сценариев, в которых метки или аннотации пространства имён не могут использоваться в качестве источника.

В отличие от подхода на основе настроек, вручную добавленные аннотации подов не обеспечивают полного обогащения. Они не обогащают метрики Kubernetes, события Kubernetes, сущности Kubernetes Smartscape и метрики Prometheus.

Можно указать `dt.security_context` в качестве аннотации пода:

```
metadata:



annotations:



metadata.dynatrace.com/dt.security_context: foo
```

Это автоматически работает для OneAgent и OpenTelemetry в сценариях, где выполняется обогащение [атрибутами непосредственно в коде приложения](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.").

Подробнее см. [контекст безопасности и распределение затрат](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#security-context-and-cost-allocation "Руководства по обогащению телеметрии в Kubernetes").

## Связанные темы

* [Мониторинг кластеров и рабочих нагрузок Kubernetes](https://www.dynatrace.com/technologies/kubernetes-monitoring/)
