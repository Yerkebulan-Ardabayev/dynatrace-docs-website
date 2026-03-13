---
title: Set up Grail permissions for OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-security-context
scraped: 2026-03-06T21:23:33.828725
---

# Настройка разрешений Grail для OneAgent

# Настройка разрешений Grail для OneAgent

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Aug 19, 2025

В Dynatrace существует [модель разрешений для Grail](../../platform/grail/organize-data/assign-permissions-in-grail.md "Find out how to assign permissions to buckets and tables in Grail."). Она применяется ко всем данным телеметрии: метрикам, событиям, спанам и журналам.

Рекомендуется выстраивать разрешения в соответствии с организационной структурой и областями развёртывания. Подходящими концепциями являются группы хостов, кластеры Kubernetes и пространства имён Kubernetes. Эти атрибуты, как правило, доступны для всех данных телеметрии, принятых через методы сбора Dynatrace, такие как OneAgent, OpenTelemetry или оператор Kubernetes. Поэтому их можно использовать для включения [разрешений на уровне записей](../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

Для развёртываний на базе Kubernetes убедитесь, что оператор Dynatrace имеет включённое [обогащение метаданными](../setup-on-k8s/guides/metadata-automation/metadata-enrichment.md "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.").

Если вам требуется лишь базовая концепция разрешений, лучшим вариантом будет настройка разрешений на уровне бакета. Затем вы можете маршрутизировать данные в нужный бакет в OpenPipeline, сопоставляя одно из упомянутых первичных полей Grail, связанных с развёртыванием.

Для более детального контроля в Dynatrace можно настроить границы политик с более детальными ограничениями на уровне данных. По умолчанию доступны следующие атрибуты:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Любой другой атрибут, перечисленный в [модели разрешений](../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace предоставляет исчерпывающую модель разрешений для Grail, применимую ко всем данным телеметрии, включая метрики, журналы, спаны и события.

## Настройка контекста безопасности

Если разрешений на уровне атрибутов развёртывания или на уровне бакета недостаточно, Dynatrace позволяет настроить детальные разрешения, добавив атрибут `dt.security_context` к вашим данным. Этот контекст безопасности может отражать вашу архитектуру безопасности и быть даже иерархическим — путём кодирования его в строку: `department-A/department-AB/team-C`.

Необходимо убедиться, что атрибут присутствует в составе данных телеметрии и что OneAgent предоставляет значение непосредственно на уровне виртуальной машины.

Чтобы задать контекст безопасности для вашего хоста, используйте следующую команду:

* Linux и AIX

  ```
  ./oneagentctl --set-host-property=dt.security_context=easytrade_sec
  ```
* Windows

  ```
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`
  ```

Это добавит контекст безопасности ко всем метрикам, спанам, событиям и журналам, собираемым OneAgent на данном хосте.

Атрибут `dt.security_context` используется многими функциями Dynatrace и доступен для всех данных телеметрии. Его можно применять для [разрешений на уровне записей](../../platform/grail/organize-data/assign-permissions-in-grail.md#field-permissions "Find out how to assign permissions to buckets and tables in Grail.").
