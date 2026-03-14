---
title: Настройка прав доступа Grail для Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/permissions
scraped: 2026-03-06T21:12:31.901700
---

# Настройка разрешений Grail для Distributed Tracing

# Настройка разрешений Grail для Distributed Tracing

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 20, 2025

Dynatrace имеет [модель разрешений для Grail](../../../platform/grail/organize-data/assign-permissions-in-grail.md "Find out how to assign permissions to buckets and tables in Grail."). Она применяется ко всем данным телеметрии, таким как метрики, события, спаны и логи.

Мы рекомендуем настраивать разрешения в соответствии с организационными границами и областями развёртывания. Подходящими концепциями являются группы хостов, кластеры Kubernetes и пространства имён Kubernetes. Эти атрибуты обычно доступны для всех данных телеметрии, поступающих через методы сбора данных Dynatrace, такие как OneAgent, OpenTelemetry или Kubernetes operator. Таким образом, вы можете использовать эти атрибуты для включения [разрешений на уровне записей](../../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

Для развёртываний на основе Kubernetes убедитесь, что в Dynatrace Operator включено [обогащение метаданных](../../../ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment.md "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.").

Если вам нужна только базовая концепция разрешений, лучшим вариантом будет настройка разрешений на уровне бакета (bucket). Затем вы можете направлять данные в нужный бакет в OpenPipeline, сопоставляя одно из упомянутых первичных полей Grail, связанных с развёртыванием.

Для более детального контроля в Dynatrace вы можете настроить границы политик с более гранулярными ограничениями на уровне данных. По умолчанию вы можете использовать следующие атрибуты:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Любой другой атрибут, указанный в [модели разрешений](../../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace предоставляет комплексную модель разрешений для Grail, которая применяется ко всем данным телеметрии, включая метрики, логи, спаны и события.

## Настройка контекста безопасности

Если разрешения на основе атрибутов уровня развёртывания или уровня бакета недостаточны, Dynatrace позволяет настроить детальные разрешения путём добавления атрибута `dt.security_context` к вашим данным. Этот контекст может отражать вашу архитектуру безопасности и даже быть иерархическим, если кодировать это в строку, например: `department-A/department-AB/team-C`.

### Использование существующих тегов на источнике

Вы можете определить контекст безопасности на источнике через [OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-security-context.md "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](../../../ingest-from/opentelemetry/opentelemetry-security-context.md "Set up Grail permissions for OpenTelemetry.") или [метки и аннотации Kubernetes](../../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Guides for telemetry enrichment on Kubernetes"). Это позволяет использовать существующие метки и теги для управления разрешениями в Dynatrace.

## Настройка контекста безопасности в OpenPipeline

Альтернативно вы можете определить контекст безопасности на основе существующих атрибутов ресурсов для ваших [данных спанов в OpenPipeline](../../../platform/openpipeline/concepts/processing.md "Learn the core concepts of Dynatrace OpenPipeline processing."):

1. Отфильтруйте записи, к которым нужно добавить атрибут `dt.security_context`. Для этого откройте новый [notebook](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.") и создайте фильтрующий DQL-запрос, например:

```
fetch spans



| filter matchesPhrase(deployment.release_stage, "prod-")
```

Этот запрос позволяет отфильтровать записи спанов, к которым вы хотите добавить атрибут `dt.security_context`. Когда вы будете удовлетворены результатом запроса, скопируйте функцию обработки спанов из DQL-запроса, в данном случае: `matchesPhrase(deployment.release_stage, "prod-")`.

2. Определите правило контекста безопасности для спанов, используя полученную функцию, и укажите значение атрибута `dt.security_context`. Значением атрибута `dt.security_context` может быть литеральное значение, которое вы предоставляете, или имя другого атрибута; это значение будет использоваться как значение `dt.security_context`.

## Рекомендации по разрешениям для Distributed Tracing

Разрешения обычно настраиваются для распределённой трассировки таким образом, чтобы пользователи могли видеть полную сквозную трассировку. Трассировки часто охватывают несколько сервисов, хостов или кластеров, и разделение трассировок границами разрешений может привести к неполным или фрагментированным данным. Хотя аналитика трассировок на уровне сервиса пострадает в меньшей степени и приложение Distributed Tracing будет работать корректно, потенциальная потеря видимости влияет на аналитику и устранение неполадок.

При настройке разрешений для Distributed Tracing учитывайте следующие рекомендации:

1. Избегайте разделения трассировок — убедитесь, что пользователи могут получить доступ ко всем спанам в трассировке, относящимся к их роли или этапу развёртывания, ограничивая при этом доступ к конфиденциальным сервисам. Поэтому настраивайте разрешения гибко и избегайте границ, ограничивающих доступ к целым спанам внутри трассировки, так как это может помешать комплексному анализу. Например, предоставьте доступ ко всем спанам на соответствующем этапе развёртывания (например, staging или production) или в рамках организационных подразделений (например, отдел или географический регион) и ограничьте доступ только к конфиденциальным сервисам (например, SSO).
2. Используйте безопасность на уровне полей для конфиденциальных данных — вместо ограничения доступа к целым спанам или трассировкам используйте безопасность на уровне полей для защиты конфиденциальной информации.

   * Dynatrace автоматически идентифицирует выбранные атрибуты спанов, определённые в [Глобальном справочнике полей](../../../semantic-dictionary/fields.md "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), и запросы к [атрибутам, помеченным как конфиденциальные](../../../manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
   * Только пользователи с разрешениями полей `builtin-sensitive-spans` и `builtin-request-attributes-spans` [field permissions](../../../platform/grail/organize-data/assign-permissions-in-grail.md#field-permissions "Find out how to assign permissions to buckets and tables in Grail.") могут видеть эти конфиденциальные поля.
   * Также можно определить пользовательские наборы полей для указания конфиденциальных атрибутов и области их применения. Например, см. [Маскирование при отображении](../../../manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").
3. Используйте контекст безопасности для определения разрешений на отдельные записи спанов — Dynatrace позволяет настраивать поступающие данные спанов, добавляя атрибут [`dt.security_context`](../../business-observability/bo-event-processing/bo-security-context.md "Use Dynatrace powered by Grail and DQL to reshape incoming business events data for better understanding, analysis, or further processing.") к конкретным записям спанов. Это позволяет устанавливать дополнительные параметры, такие как разрешения для отдельных записей. Чтобы создать контекст безопасности для поступающих данных спанов, необходимо создать правило конвейера.

## Пользовательские разрешения для Distributed Tracing

При работе с ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** убедитесь, что вы ознакомились со всеми необходимыми разрешениями и настроили их:

1

Конфиденциальные атрибуты для спанов помечены как `sensitive-spans` в [Глобальном справочнике полей](../../../semantic-dictionary/fields.md "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

2

Чтобы узнать больше об ограниченном доступе к персональным данным и конфиденциальным атрибутам запросов, см. [Маскирование при отображении](../../../manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").