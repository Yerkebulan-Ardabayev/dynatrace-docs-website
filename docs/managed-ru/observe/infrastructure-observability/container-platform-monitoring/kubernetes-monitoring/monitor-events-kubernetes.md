---
title: Мониторинг событий Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes
scraped: 2026-05-12T12:00:30.414729
---

# Monitor Kubernetes/OpenShift events

# Мониторинг событий Kubernetes/OpenShift

* 8-min read
* Updated on Jul 05, 2024

## Предварительные требования

* ActiveGate version 1.265+
* В Dynatrace перейдите в **Monitoring settings** > **Kubernetes** и убедитесь, что параметр **Monitor Kubernetes namespaces, services, workloads, and pods** включён.
* [Включите последнюю версию мониторинга журналов Dynatrace](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")

## Мониторинг событий Kubernetes для анализа и оповещений

Для полной наблюдаемости событий Kubernetes, автоматического анализа Davis и пользовательских оповещений необходимо включить мониторинг событий Kubernetes.

Чтобы включить мониторинг событий для конкретных кластеров Kubernetes:

1. Перейдите в раздел **Kubernetes**.
2. Найдите ваш кластер Kubernetes и в столбце **Actions** выберите **More** (**…**) > **Settings**.
3. На вкладке **Monitoring Settings** включите **Monitor events**.
4. Нажмите **Save changes**.

При включении **Monitor events** все события будут приниматься, а все [важные события](#important-events) будут учитываться при анализе первопричин Davis. Кроме того, для максимальной гибкости и точного контроля над событиями, принимаемыми из Kubernetes, можно [фильтровать события](#filter).

### Выведенные события Kubernetes

Даже если **Monitor events** отключён, так называемые *выведенные* события Kubernetes всё равно принимаются. Эти выведенные события не являются нативными событиями Kubernetes — они создаются ActiveGate на основе информации от сервера Kubernetes API.

Примеры выведенных событий:

* Завершения работы cgroup (OOM kill events).
* Изменения спецификации нагрузок (реплики, образы, переменные среды, ресурсы, пробы) для:

  + Deployments
  + StatefulSets
  + DaemonSets

Эти события не тарифицируются и учитываются при анализе первопричин Davis.

### Просмотр событий

После включения мониторинга событий Kubernetes можно просматривать и анализировать события из кластера Kubernetes.

На странице сведений о кластере Kubernetes перейдите в раздел **Events**.

События можно фильтровать по:

* Временному диапазону: выберите один из временных диапазонов на диаграмме для просмотра открытых событий за этот период.
* Конкретным событиям: выберите один из ярлыков групп под диаграммой для просмотра конкретных событий.

Для получения дополнительной информации о событии нажмите **Details** напротив него.

События Kubernetes связаны с сущностями Kubernetes. Событие отображается на соответствующей странице сущности и на страницах связанных сущностей. Например, события пода отображаются на странице сведений о кластере, пространстве имён, нагрузке и поде.

События также можно просматривать на странице **Log viewer** (в Dynatrace перейдите в раздел **Logs**), которая поддерживает расширенный поиск и фильтрацию.

[Выведенные события Kubernetes](#inferred) не отображаются в **Log viewer** — они принимаются непосредственно как события.

## Фильтрация отслеживаемых событий

По умолчанию фильтрация отключена — принимаются все события. Чтобы настроить мониторинг только определённых событий:

1. Включите **Filter events**.

   Если переключатель **Filter events** не отображается, убедитесь, что сначала включён **Monitor events**.
2. [Настройте несколько селекторов полей для каждой среды Kubernetes](#set-up-event-field-selectors).
3. Необязательно: [включите выполнение Davis анализа первопричин для всех важных событий Kubernetes](#important-events).
4. Нажмите **Save changes**.

### Настройка селекторов полей событий

Фильтрация следует [синтаксису селекторов полей Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/), поэтому события можно выбирать на основе полей ресурсов событий, таких как `source.component`, `type` или `involvedObject`.

Выражение селектора поля должно соответствовать следующим требованиям:

* Соответствовать регулярному выражению: `^[\w\.]{1,1024}((=){1,2}|(!=))[^,!=]{0,256}(,[\w\.]{1,1024}?((=){1,2}|(!=))[^,!=]{0,256}){0,9}$`.
* Содержать не более 10 селекторов, разделённых запятыми. Будут приняты события, соответствующие всем разделённым запятыми селекторам. Логический оператор — `AND`.
* Селектор состоит из трёх частей:

  + **Key (ключ):** содержит до 1024 буквенно-цифровых символов, символов подчёркивания и точек.
  + **Operator (оператор):** `=`, `==` или `!=`.
  + Необязательное **Value (значение):** может содержать до 256 символов. Не может содержать восклицательные знаки, знаки равенства или запятые.

Например:

* Если задать выражение селектора поля `involvedObject.namespace=hipster-shop,type=Warning`, оно сохранит все события, связанные с пространством имён `hipster-shop` и имеющие тип `Warning`.
* Если разделить выражение на два независимых селектора поля, будут получены все события для пространства имён `hipster-shop` и все события типа `Warning`. В данном случае логический оператор — `OR`.

**Примеры селекторов полей событий:**

| **Селекторы полей событий** | **Выражение селектора поля** |
| --- | --- |
| Получить все события `Node` | `involvedObject.kind=Node` |
| Получить все события `Warning` | `type=Warning` |
| Получить все события `Pod` | `involvedObject.kind=Pod` |
| Получить все события объектов из конкретного пространства имён | `involvedObject.namespace=<your_namespace>` (замените `<your_namespace>` именем вашего пространства имён) |
| Получить все события `BackOff` для подов во всех пространствах имён | `reason=BackOff` |
| Получить все события с непустым полем type | `type!=` |
| Получить все события контейнера nginx | `involvedObject.fieldPath==spec.containers{nginx}` |

Для настройки селекторов полей событий выберите один из вариантов:

Через веб-интерфейс

Через CLI

Через API

1. Перейдите в раздел **Kubernetes**.
2. Найдите ваш кластер Kubernetes и в столбце **Actions** выберите **More** (**…**) > **Settings**.
3. На вкладке **Monitoring Settings**:

   * Включите **Filter events**.
   * Нажмите **Add events field selector**.
   * Введите **Field selector name** и **Field selector expression**.
4. Нажмите **Save changes**.

Пример команды:

```
kubectl get events --all-namespaces --field-selector involvedObject.namespace=hipster-shop,type=Warning
```

Селекторы полей событий можно определить через [Dynatrace API](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api "Manage Kubernetes credentials via the Dynatrace configuration API.").

На один кластер Kubernetes можно создать не более 20 правил фильтрации событий.

### Мониторинг важных событий

При обнаружении проблем с приложениями, микросервисами или инфраструктурой Davis выполняет анализ первопричин для всех важных событий Kubernetes для узлов, пространств имён, нагрузок и подов.

Событие Kubernetes считается важным (значимым для анализа первопричин Davis), если выполняется хотя бы одно из следующих условий:

* Причина события входит в предустановленный список [важных причин](#important-event-reasons).
* Тип события — `Warning`.

Важные причины событий

`BackOff`,
`DeadlineExceeded`,
`Killing`,
`NodeNotSchedulable`,
`OutOfDisk`,
`Preempting`

По умолчанию все эти события отслеживаются при включении [**Monitor events**](#monitor-events). При [фильтрации событий](#filter) можно применять предустановленный фильтр важных событий или пользовательские фильтры. Если задано несколько фильтров, они объединяются с помощью логического `OR` — событие принимается, если оно соответствует любому из фильтров.

Чтобы включить мониторинг важных событий при включённой фильтрации:

1. Перейдите в раздел **Kubernetes**.
2. Найдите ваш кластер Kubernetes и в столбце **Actions** выберите **More** (**…**) > **Settings**.
3. На вкладке **Monitoring Settings** включите **Include important events**.

   Если переключатель **Include important events** не отображается, убедитесь, что сначала включены **Monitor events** и **Filter events**.
4. Нажмите **Save changes**.

## Построение диаграмм и оповещения

События Kubernetes доступны через метрику **Kubernetes: Event count** (`builtin:kubernetes.events`). Для фильтрации метрики счётчика событий по нужным событиям используйте измерения `k8s.event.reason` и `k8s.event.type`.

* Для понимания распределения и динамики событий Kubernetes с течением времени используйте [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для создания диаграмм. Диаграммы можно использовать для сравнения разных временных диапазонов, сущностей, фильтров событий и сложных выражений.
* Для создания оповещений при возникновении событий Kubernetes (например, всегда оповещать при событии `Evicted`) определите [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") на основе метрики **Kubernetes: Event count**.

## Лицензирование

Для оценки количества событий, потребляющих DDU, можно запросить метрику `dsfm:active_gate.kubernetes.events.processed`, которая предоставляет информацию о количестве событий, принимаемых в Dynatrace на кластер Kubernetes.

Пример запроса для временного диапазона 24 часа:

`dsfm:active_gate.kubernetes.events.processed:splitBy("dt.entity.kubernetes_cluster"):sum:auto:sort(value(sum,descending)):limit(10)`

Потребление DDU применяется к мониторингу событий Kubernetes. Подробнее см. в разделе [DDU для пользовательских событий Davis](/managed/license/monitoring-consumption-classic/davis-data-units/ddu-events "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.").

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")