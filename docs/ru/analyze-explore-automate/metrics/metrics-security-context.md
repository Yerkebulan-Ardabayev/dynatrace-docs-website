---
title: Настройка Grail разрешений для Metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/metrics-security-context
scraped: 2026-03-05T21:30:28.462282
---

# Настройка разрешений Grail для метрик


* Latest Dynatrace

В Dynatrace существует [модель разрешений для Grail](../../platform/grail/organize-data/assign-permissions-in-grail.md "Узнайте, как назначать разрешения бакетам и таблицам в Grail."). Она применяется ко всем данным телеметрии, таким как метрики, события, span-ы и логи.

Мы рекомендуем настраивать разрешения в соответствии с организационной структурой и областями развёртывания. Подходящими концепциями являются группы хостов, кластеры Kubernetes и пространства имён Kubernetes. Эти атрибуты обычно доступны для всех данных телеметрии, собираемых с помощью методов сбора Dynatrace, таких как OneAgent, OpenTelemetry или оператор Kubernetes. Таким образом, вы можете использовать эти атрибуты для включения [разрешений на уровне записей](../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Узнайте, как назначать разрешения бакетам и таблицам в Grail.").

Для развёртываний на базе Kubernetes убедитесь, что в Dynatrace Operator включено [обогащение метаданными](../../ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment.md "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes путём прикрепления релевантных метаданных к сущностям, таким как поды, хосты и процессы, для улучшения наблюдаемости.").

Если вам требуется только базовая концепция разрешений, лучшим вариантом будет настройка разрешений на уровне бакетов. Затем вы можете маршрутизировать данные в нужный бакет в OpenPipeline, сопоставляя одно из упомянутых первичных полей Grail, связанных с развёртыванием.

Для более детального контроля в Dynatrace вы можете настроить границы политик с более гранулярными ограничениями на уровне данных. По умолчанию вы можете использовать следующие атрибуты:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Любой другой атрибут, перечисленный в [модели разрешений](../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Узнайте, как назначать разрешения бакетам и таблицам в Grail.")

Dynatrace предоставляет комплексную модель разрешений для Grail, которая применяется ко всем данным телеметрии, включая метрики, логи, span-ы и события.

## Настройка контекста безопасности

Если разрешений на основе атрибутов уровня развёртывания или уровня бакетов недостаточно, Dynatrace позволяет настроить детализированные разрешения путём добавления атрибута `dt.security_context` к вашим данным. Этот контекст может представлять вашу архитектуру безопасности и даже быть иерархическим, закодированным в строку, например `department-A/department-AB/team-C`.

Для использования `dt.security_context` и других атрибутов для разрешений убедитесь, что эти атрибуты присутствуют в ваших данных телеметрии.

### Использование существующих тегов в источнике

Вы можете определить контекст безопасности в источнике через [OneAgent](../../ingest-from/dynatrace-oneagent/oneagent-security-context.md "Узнайте, как настроить разрешения Grail для OneAgent."), [OpenTelemetry](../../ingest-from/opentelemetry/opentelemetry-security-context.md "Настройка разрешений Grail для OpenTelemetry.") или [метки и аннотации Kubernetes](../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Руководства по обогащению телеметрии в Kubernetes"). Это позволяет использовать существующие метки и теги для управления разрешениями в Dynatrace.

## Настройка контекста безопасности в OpenPipeline

Вы можете определить контекст безопасности на основе существующих атрибутов ресурсов для ваших данных в OpenPipeline. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Metrics** > **Pipelines** и после настройки конвейера на вкладке **Permission** используйте опцию **Set Security Context processors**.

Для определения атрибута `dt.security_context`:

1. Определите условие сопоставления для фильтрации записей метрик, которым нужно назначить контекст безопасности, например:

   ```
   matchesValue(metric.key, "http.server.request.duration_bucket") and matchesValue(http.route, "/basket")
   ```
2. Добавьте `dt.security_context` для этих записей метрик. Значение этого атрибута может быть литеральным значением, таким как `TeamA`, или значением, скопированным из другого поля, присутствующего в записи метрики.
3. Убедитесь, что контекст безопасности настроен правильно.

Когда поступают новые данные метрик, процессоры контекста безопасности OpenPipeline добавляют атрибут `dt.security_context` со значением `TeamA` к соответствующим записям метрик. Чтобы убедиться, что процессоры контекста безопасности обработали записи метрик, откройте ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и выполните DQL-запрос, например:

```
timeseries median(http.server.request.duration_bucket), by:{http.route, dt.security_context} | filter matchesValue(dt.security_context, "TeamA")
```

На основе созданного атрибута вы можете применять политики безопасности для пользователей и групп.

## Связанные темы

* [Настройка разрешений Grail для OneAgent](../../ingest-from/dynatrace-oneagent/oneagent-security-context.md "Узнайте, как настроить разрешения Grail для OneAgent.")
* [Обогащение метаданными всей телеметрии, поступающей из Kubernetes](../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Руководства по обогащению телеметрии в Kubernetes")
* [Настройка разрешений Grail для логов](../logs/lma-security-context.md "Используйте Dynatrace на базе Grail и DQL для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей обработки.")
* [Настройка разрешений Grail для распределённой трассировки](../../observe/application-observability/distributed-tracing/permissions.md "Управление разрешениями для распределённой трассировки на базе Grail.")
* [Примеры обработки OpenPipeline](../../platform/openpipeline/use-cases/processing-examples.md "Изучите сценарии использования обработки OpenPipeline в Dynatrace на базе Grail.")
