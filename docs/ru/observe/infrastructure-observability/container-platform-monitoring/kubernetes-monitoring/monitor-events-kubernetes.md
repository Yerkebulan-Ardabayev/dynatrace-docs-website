---
title: Мониторинг событий Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes
scraped: 2026-03-06T21:21:56.612300
---

## Предварительные требования

* ActiveGate версии 1.265+
* В Dynatrace перейдите в **Monitoring settings** > **Kubernetes** и убедитесь, что параметр **Monitor Kubernetes namespaces, services, workloads, and pods** включён.
* [Включите последнюю версию мониторинга логов Dynatrace](../../../../analyze-explore-automate/log-monitoring.md "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")

## Мониторинг событий Kubernetes для анализа и оповещений

Для полной наблюдаемости событий Kubernetes, автоматического анализа Davis и пользовательских оповещений необходимо включить мониторинг событий Kubernetes.

Чтобы включить мониторинг событий для определённых кластеров Kubernetes

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Найдите ваш кластер Kubernetes и в столбце **Actions** выберите **More** (**...**) > **Settings**.
3. На вкладке **Monitoring Settings** включите **Monitor events**.
4. Нажмите **Save changes**.

Когда вы включаете **Monitor events**, все события принимаются, и все [важные события](#important-events) учитываются при обнаружении корневых причин Davis. В качестве альтернативы, для максимальной гибкости и точного контроля над событиями, которые вы хотите принимать из Kubernetes, вы можете [фильтровать события](#filter).

### Выведенные события Kubernetes

Даже если **Monitor events** отключён, так называемые *выведенные* события Kubernetes всё равно принимаются. Эти выведенные события не являются нативными событиями Kubernetes, а создаются ActiveGate на основе информации от API-сервера Kubernetes.

Примеры выведенных событий:

* События cgroup OOM kill
* Изменения спецификации рабочих нагрузок (реплики, образы, переменные окружения, ресурсы, пробы) для

  + Deployments
  + StatefulSets
  + DaemonSets

Эти события не тарифицируются и используются для анализа корневых причин Davis.

### Просмотр событий

После включения мониторинга событий Kubernetes вы можете просматривать и анализировать события из кластера Kubernetes.

На странице сведений о кластере Kubernetes перейдите в раздел **Events**.

Вы можете фильтровать события по:

* Временному диапазону: выберите один из диапазонов на графике для просмотра открытых событий за этот период
* Конкретным событиям: выберите одну из групповых меток под графиком для просмотра определённых событий

Для получения дополнительной информации о событии нажмите **Details** для этого события.

События Kubernetes связаны с сущностями Kubernetes. Событие отображается на странице соответствующей сущности и на страницах связанных сущностей. Например, события подов отображаются на страницах сведений о кластере, пространстве имён, рабочей нагрузке и поде.

Вы также можете просматривать события на странице **Log viewer** (в Dynatrace перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**), которая позволяет выполнять расширенный поиск и фильтрацию.

Если среда поддерживает платформу, события хранятся в Grail. Следующий запрос DQL можно использовать в качестве шаблона для запроса определённых событий в [**Notebooks**](../../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") или [**Dashboards**](../../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

```
fetch events


| filter event.provider == "KUBERNETES_EVENT"
```

[Выведенные события Kubernetes](#inferred) не отображаются в **Log viewer**. Они принимаются напрямую как события.

## Фильтрация событий для мониторинга

По умолчанию фильтрация отключена, что означает приём всех событий. Чтобы настроить мониторинг только определённых событий

1. Включите **Filter events**.

   Если вы не видите переключатель **Filter events**, убедитесь, что сначала включён **Monitor events**.
2. [Настройте несколько полевых селекторов для каждой среды Kubernetes](#set-up-event-field-selectors).
3. Необязательно [Настройте анализ корневых причин Davis для всех важных событий Kubernetes](#important-events).
4. Нажмите **Save changes**.

### Настройка полевых селекторов событий

Фильтрация следует [синтаксису полевых селекторов, принятому в Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/), поэтому события можно выбирать на основе полей ресурса события, таких как `source.component`, `type` или `involvedObject`.

Выражение полевого селектора должно соответствовать следующим требованиям:

* Оно должно соответствовать следующему регулярному выражению: `^[\w\.]{1,1024}((=){1,2}|(!=))[^,!=]{0,256}(,[\w\.]{1,1024}?((=){1,2}|(!=))[^,!=]{0,256}){0,9}$`.
* Может содержать до 10 селекторов, разделённых запятыми. События, соответствующие всем селекторам, разделённым запятыми, будут приняты. Логический оператор — `AND`.
* Селектор состоит из трёх частей:

  + **Ключ:** Содержит до 1 024 буквенно-цифровых символов, подчёркиваний и точек.
  + **Оператор:** `=`, `==` или `!=`.
  + Необязательно **Значение:** Может содержать до 256 символов. Не может содержать восклицательные знаки, знаки равенства или запятые.

Например,

* Если вы установите выражение полевого селектора `involvedObject.namespace=hipster-shop,type=Warning`, выражение сохранит все события, связанные с пространством имён `hipster-shop`, которые имеют тип `Warning`.
* Если вы разделите выражение на два независимых полевых селектора, вы получите все события для пространства имён `hipster-shop` и все события типа `Warning`. Логический оператор в этом случае — `OR`.

**Примеры полевых селекторов событий:**

| **Полевые селекторы событий** | **Выражение полевого селектора** |
| --- | --- |
| Получить все события `Node` | `involvedObject.kind=Node` |
| Получить все события `Warning` | `type=Warning` |
| Получить все события `Pod` | `involvedObject.kind=Pod` |
| Получить все события объектов, связанных с определённым пространством имён | `involvedObject.namespace=<your_namespace>` (Убедитесь, что вы заменили `<your_namespace>` на имя вашего собственного пространства имён) |
| Получить все события `BackOff` для подов во всех пространствах имён | `reason=BackOff` |
| Получить все события с непустым полем типа | `type!=` |
| Получить все события контейнера nginx | `involvedObject.fieldPath==spec.containers{nginx}` |

Для настройки полевых селекторов событий выберите один из вариантов ниже:

Через веб-интерфейс

Через CLI

Через API

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Найдите ваш кластер Kubernetes и в столбце **Actions** выберите **More** (**...**) > **Settings**.
3. На вкладке **Monitoring Settings**

   * Включите **Filter events**.
   * Нажмите **Add events field selector**.
   * Введите **Field selector name** и **Field selector expression**.
4. Нажмите **Save changes**.

Пример команды:

```
kubectl get events --all-namespaces --field-selector involvedObject.namespace=hipster-shop,type=Warning
```

Вы можете определить полевые селекторы событий через [Dynatrace API](../../../../dynatrace-api/configuration-api/k8s-credentials-api-api.md "Manage Kubernetes credentials via the Dynatrace configuration API.").

Вы можете создать максимум 20 правил фильтрации событий на кластер Kubernetes.

### Мониторинг важных событий

При обнаружении проблем с приложениями, микросервисами или инфраструктурой Davis выполняет анализ корневых причин по всем важным событиям Kubernetes для узлов, пространств имён, рабочих нагрузок и подов.

Событие Kubernetes считается важным (релевантным для анализа корневых причин Davis), когда выполняется хотя бы одно из следующих двух условий.

* Причина события входит в предопределённый список [важных причин](#important-event-reasons).
* Тип события — `Warning`.

Важные причины событий

`BackOff`,
`DeadlineExceeded`,
`Killing`,
`NodeNotSchedulable`,
`OutOfDisk`,
`Preempting`

По умолчанию все эти события мониторятся, когда включён [**Monitor events**](#monitor-events). Если вы решите [фильтровать события](#filter), можно применить либо предопределённый фильтр важных событий, либо пользовательские фильтры событий. Если установлено несколько фильтров, они объединяются с помощью логического `OR`. Событие принимается, как только событие Kubernetes соответствует любому из фильтров.

Чтобы включить мониторинг важных событий при включённой фильтрации событий

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Найдите ваш кластер Kubernetes и в столбце **Actions** выберите **More** (**...**) > **Settings**.
3. На вкладке **Monitoring Settings** включите **Include important events**.

   Если вы не видите переключатель **Include important events**, убедитесь, что сначала включены **Monitor events** и **Filter events**.
4. Нажмите **Save changes**.

## Графики и оповещения

События Kubernetes доступны в метрике **Kubernetes: Event count** (`builtin:kubernetes.events`). Для фильтрации метрики количества событий по нужным событиям используйте измерения `k8s.event.reason` и `k8s.event.type`.

* Чтобы помочь вам понять распределение и развитие событий Kubernetes во времени, используйте [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") для создания графиков. Вы можете использовать графики для сравнения различных временных диапазонов, различных сущностей, фильтров событий и использования сложных выражений.
* Чтобы активировать оповещения при возникновении событий Kubernetes (например, всегда оповещать в случае события `Evicted`), определите [события метрик](../../../../dynatrace-intelligence/anomaly-detection/metric-events.md "Learn about metric events in Dynatrace") на основе метрики **Kubernetes: Event count**.

## Лицензирование

Для оценки количества событий, потребляющих DDU, вы можете запросить метрику `dsfm:active_gate.kubernetes.events.processed`, которая предоставляет информацию о количестве событий, принимаемых в Dynatrace для каждого кластера Kubernetes.

Пример запроса для 24-часового периода:

`dsfm:active_gate.kubernetes.events.processed:splitBy("dt.entity.kubernetes_cluster"):sum:auto:sort(value(sum,descending)):limit(10)`

Потребление DDU применяется к мониторингу событий Kubernetes. Подробности см. в [DDU для пользовательских событий Davis](../../../../license/monitoring-consumption-classic/davis-data-units/ddu-events.md "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.").

## Связанные темы

* [Настройка Dynatrace в Kubernetes](../../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes")
