---
title: Настройка расширенных прав доступа с помощью контекста безопасности
source: https://www.dynatrace.com/docs/platform/grail/organize-data/advanced-permission-setup
scraped: 2026-03-06T21:27:14.199849
---

# Настройка расширенных разрешений с помощью контекста безопасности


* Latest Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Обновлено 20 ноября 2025 г.

В этом руководстве описана настройка разрешений Dynatrace для ваших данных -- от базового управления доступом до расширенных конфигураций, таких как обогащение данных с помощью `dt.security_context`, применение процессоров OpenPipeline для условного доступа, а также управление политиками IAM с помощью границ и шаблонов для масштабируемого контроля.

Dynatrace имеет [модель разрешений для Grail](assign-permissions-in-grail.md "Узнайте, как назначать разрешения для бакетов и таблиц в Grail."). Она применяется ко всем телеметрическим данным, таким как метрики, события, спаны и логи.

Рекомендуется настраивать разрешения в соответствии с организационными направлениями и областями развертывания. Подходящие концепции включают группы хостов, кластеры Kubernetes и пространства имен Kubernetes. Эти атрибуты обычно доступны для всех телеметрических данных, поступающих через методы сбора Dynatrace, такие как OneAgent, OpenTelemetry или оператор Kubernetes. Следовательно, вы можете использовать эти атрибуты для включения [разрешений на уровне записей](assign-permissions-in-grail.md#grail-permissions-table-record "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.").

Для развертываний на основе Kubernetes убедитесь, что Dynatrace Operator имеет включенное [обогащение метаданными](../../../ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment.md "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes, прикрепляя соответствующие метаданные к сущностям, таким как поды, хосты и процессы, для лучшей наблюдаемости.").

Если вам нужна только базовая концепция разрешений, лучшим вариантом будет настройка разрешений на уровне бакетов. Затем вы можете маршрутизировать данные в нужный бакет в OpenPipeline, сопоставляя одно из упомянутых первичных полей Grail, связанных с развертыванием.

Для более детального контроля в Dynatrace вы можете настроить границы политик с более гранулярными ограничениями на уровне данных. По умолчанию доступны следующие атрибуты:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Любой другой атрибут, перечисленный в [модели разрешений](assign-permissions-in-grail.md#grail-permissions-table-record "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.")

Dynatrace предоставляет комплексную модель разрешений для Grail, которая применяется ко всем телеметрическим данным, включая метрики, логи, спаны и события.

## Общая настройка разрешений

Вы можете настроить контроль доступа к данным и сущностям, используя приведенные ниже руководства.

* [Настройка разрешений OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-security-context.md "Узнайте, как настроить разрешения Grail для OneAgent.")
* [Настройка разрешений Kubernetes](../../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md#security-context-and-cost-allocation "Руководства по обогащению телеметрии в Kubernetes")

* [Настройка разрешений для логов](../../../analyze-explore-automate/logs/lma-security-context.md "Используйте Dynatrace на базе Grail и DQL для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей обработки.")
* [Настройка разрешений для трассировок](../../../observe/application-observability/distributed-tracing/permissions.md "Управление разрешениями для распределенной трассировки на базе Grail.")
* [Настройка разрешений для сущностей](../../../manage/identity-access-management/use-cases/access-security-context.md "Предоставление доступа к сущностям с помощью контекста безопасности")
* [Настройка разрешений OpenPipeline](advanced-permission-setup.md#set-up-the-security-context-in-openpipeline "Настройка расширенных разрешений с помощью контекста безопасности.")

## Настройка контекста безопасности

Если разрешений на уровне атрибутов развертывания или бакетов недостаточно, Dynatrace позволяет настроить детальные разрешения, добавив атрибут `dt.security_context` к конкретным данным.

### Настройка контекста безопасности в OpenPipeline

Вы можете определить контекст безопасности на основе существующих атрибутов ресурсов для ваших [данных в OpenPipeline](../../openpipeline/getting-started/tutorial-configure-processing.md#process "Настройка источников, маршрутов и обработки данных в OpenPipeline.").
После настройки конвейера добавьте процессоры `Set Security Context` на вкладке `Permission`.

Для определения атрибута `dt.security_context`

1. Определите условие соответствия для фильтрации записей, которым нужно назначить контекст безопасности.

   Например: `matchesValue(http.route, "/basket")`
2. Добавьте `dt.security_context` для этих записей. Значение этого атрибута может быть литеральным значением, например `TeamA`, или значением, скопированным из другого поля записи.
3. Убедитесь, что контекст безопасности установлен корректно.

   При поступлении новых данных процессоры контекста безопасности OpenPipeline назначают атрибут `dt.security_context` со значением `TeamA`. Откройте Notebook для подтверждения того, что процессоры контекста безопасности обработали записи. Для проверки используйте DQL-запрос, например:

   `fetch logs | filter matchesValue(dt.security_context, "TeamA")`
4. Повторите эту настройку для всех применимых типов данных (логи, метрики, спаны).

На основе созданного атрибута вы можете применять политики безопасности для пользователей и групп, как описано в следующем разделе.

## Применение контроля доступа

Вы можете [применить контроль доступа](assign-permissions-in-grail.md "Узнайте, как назначать разрешения для бакетов и таблиц в Grail."), чтобы обеспечить доступ команд только к релевантным для них данным, используя выражения политик, такие как:

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("*-database-*");


ALLOW storage:logs:read WHERE storage:dt.security_context = "TeamA" AND storage:dt.host_group.id MATCH ("shared_host_*");
```

Вы также можете использовать [границы политик](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries.md "Ограничение политик безопасности с помощью границ политик для предоставления адаптированного доступа пользователям.") или [шаблоны политик](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating.md "Шаблоны политик") для более удобного управления контролем доступа.

## Связанные темы

* [Настройка разрешений Grail для OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-security-context.md "Узнайте, как настроить разрешения Grail для OneAgent.")
* [Обогащение метаданными всей телеметрии из Kubernetes](../../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Руководства по обогащению телеметрии в Kubernetes")
* [Настройка разрешений Grail для логов](../../../analyze-explore-automate/logs/lma-security-context.md "Используйте Dynatrace на базе Grail и DQL для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей обработки.")
* [Настройка разрешений Grail для распределенной трассировки](../../../observe/application-observability/distributed-tracing/permissions.md "Управление разрешениями для распределенной трассировки на базе Grail.")
* [Предоставление доступа к сущностям с помощью контекста безопасности](../../../manage/identity-access-management/use-cases/access-security-context.md "Предоставление доступа к сущностям с помощью контекста безопасности")
* [Примеры обработки OpenPipeline](../../openpipeline/use-cases/processing-examples.md "Изучите сценарии использования обработки OpenPipeline в Dynatrace на базе Grail.")
