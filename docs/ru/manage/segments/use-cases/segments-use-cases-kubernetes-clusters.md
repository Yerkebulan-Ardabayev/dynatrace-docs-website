---
title: Сегментация данных по кластерам Kubernetes
source: https://www.dynatrace.com/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters
scraped: 2026-03-06T21:13:18.908578
---

Настройте сегмент для сигналов и отслеживаемых сущностей, связанных с несколькими кластерами Kubernetes в общем стеке.

## Для кого это руководство

Эта статья предназначена для администраторов и операторов Kubernetes, которым необходимо организовывать и логически структурировать рабочие нагрузки в кластерах Kubernetes.

## Что вы узнаете

В этой статье вы узнаете, как создать сегмент для удобной фильтрации сигналов наблюдаемости и отслеживаемых сущностей в домене Kubernetes.

## Перед началом работы

Необходимые знания

* [Включение данных в сегменты](../concepts/segments-concepts-includes.md "Узнайте, как данные различных типов могут быть включены в сегменты.")
* [Сегменты в DQL-запросах](../concepts/segments-concepts-queries.md "Узнайте, как Grail оценивает сегменты во время выполнения запроса для возврата только совпадающих результатов.")
* [Начало работы с Kubernetes](../../../observe/infrastructure-observability/kubernetes-app/enable-k8s-experience.md "Включите Kubernetes для существующих кластеров или начните мониторинг новых кластеров.")

Предварительные требования

* Среда Dynatrace SaaS на базе Grail и AppEngine.
* У вас есть разрешения `storage:filter-segments:write` и `storage:filter-segments:read`. Чтобы узнать, как настроить разрешения, см. [Разрешения в Grail](../../../platform/grail/organize-data/assign-permissions-in-grail.md "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.").
* У вас есть лицензия и настроен [Kubernetes Platform Monitoring](../../../license/capabilities/container-monitoring/kubernetes-platform-monitoring.md "Узнайте, как рассчитывается потребление возможности Dynatrace Kubernetes Platform Monitoring DPS.").

## Шаги

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание сегмента для кластеров общего стека**](segments-use-cases-kubernetes-clusters.md#create "Настройте сегмент для сигналов и отслеживаемых сущностей, связанных с кластерами Kubernetes")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Включение сигналов наблюдаемости и отслеживаемых сущностей**](segments-use-cases-kubernetes-clusters.md#include "Настройте сегмент для сигналов и отслеживаемых сущностей, связанных с кластерами Kubernetes")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Анализ производительности и состояния всего стека**](segments-use-cases-kubernetes-clusters.md#analyze "Настройте сегмент для сигналов и отслеживаемых сущностей, связанных с кластерами Kubernetes")

### Шаг 1. Создание сегмента для кластеров общего стека

В нашем примере набор из нескольких отдельных кластеров Kubernetes составляет общий стек. Вместе эти кластеры образуют стек, который мы будем называть `dtp-dev3`.

1. Перейдите в ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments") **Segments** и выберите **Segment**, чтобы добавить новый сегмент
2. Укажите имя и описание сегмента

   * Выберите и отредактируйте **Untitled segment**, чтобы присвоить сегменту полезное в вашем контексте имя
     Для этого примера введите `dtp-dev3`
   * Выберите **Description** и опишите сегмент
     Для этого примера введите `Signals and entities of K8s clusters of dtp-dev3 deployment`
3. Выберите **Visibility** и установите значение `Anyone in the environment`, чтобы другие могли находить и использовать этот сегмент
4. Выберите **Save**

На данном этапе сегмент не указывает, какие данные он должен включать. В следующем разделе мы укажем данные для фильтрации с помощью этого сегмента.

### Шаг 2. Включение сигналов наблюдаемости и отслеживаемых сущностей

Поскольку сигналы наблюдаемости Kubernetes последовательно маркируются измерениями и полями `k8s.*`, наш сегмент воспользуется этим, ссылаясь на них напрямую.

1. Выберите **Add from data types** > **All data types**
2. Выберите **Type to filter**, чтобы включить все данные, соответствующие `k8s.cluster.name = dtp-dev3*`
3. Выберите **Run query**, чтобы получить предварительный просмотр совпадающих данных
4. Выберите **Save**, чтобы сохранить изменения

   ![Сигналы кластеров K8s](https://dt-cdn.net/images/segments-k8s-signals-2090-2e33448917.png)

Прямое включение сигналов наблюдаемости не приводит к автоматическому включению отслеживаемых сущностей, которые их генерируют. В следующем разделе мы включим эти сущности отдельно.

1. Выберите **Add from entities and topology** > **Kubernetes cluster (dt.entity.kubernetes\_cluster)**
2. Выберите **Type to filter**, чтобы включить все кластеры, соответствующие `entity.name = dtp-dev3*`
3. Выберите **Run query**, чтобы получить предварительный просмотр совпадающих кластеров

   ![Кластеры K8s](https://dt-cdn.net/images/segments-k8s-clusters-2090-36fbc5501d.png)
4. Выберите **Related entity** > **Kubernetes namespace**
5. Выберите **Run query** для вновь добавленного блока включения, чтобы получить предварительный просмотр пространств имён, связанных с нашими кластерами выше

   ![Пространства имён K8s кластеров](https://dt-cdn.net/images/segments-k8s-namespaces-2090-9f4067597b.png)
6. Выберите **Related entity** и выберите все дополнительные связанные сущности кластеров Kubernetes, на которых строится сегмент

   * Kubernetes namespace (уже включено)
   * Kubernetes node
   * Kubernetes pod
   * Kubernetes workload
   * Kubernetes service
   * Container group instance
   * Service
   * Host

В настоящее время отслеживаемые сущности включаются по их отдельным типам. В будущем мы сделаем это более гибким и позволим включать отслеживаемые сущности любого типа с помощью одного условия.

### Шаг 3. Анализ состояния и производительности всего стека

В этом шаге мы покажем, как

* Анализировать общее состояние нашего стека в ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**
* Анализировать состояние и производительность сервисов нашего стека в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**
* Анализировать рабочие нагрузки Kubernetes нашего стека в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

#### Problems

Чтобы проанализировать общее состояние нашего стека в ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**

1. Перейдите в ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**
2. Откройте селектор сегментов и в разделе **Filter by segments** выберите ранее созданный сегмент `dtp-dev3`
3. Выберите **Apply**, чтобы завершить выбор сегмента
4. Выберите **Update**, чтобы обновить список проблем

   ![Проблемы, затрагивающие сущности в dtp-dev3](https://dt-cdn.net/images/segments-k8s-problems-2140-1a51ddfe51.png)

Применяя наш сегмент, мы получаем отфильтрованный список проблем, затрагивающих любую отслеживаемую сущность любого типа в нашем стеке.

#### Services

Чтобы проанализировать состояние и производительность сервисов нашего стека в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**

1. Перейдите в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**
2. Откройте селектор сегментов и в разделе **Filter by segments** выберите ранее созданный сегмент `dtp-dev3`
3. Выберите **Apply**, чтобы завершить выбор сегмента

   ![Сервисы в dtp-dev3](https://dt-cdn.net/images/segments-k8s-services-2140-f351191c33.png)

Применяя наш сегмент, мы получаем отфильтрованный список сервисов, связанных с любым кластером нашего стека.

#### Dashboards

Чтобы проанализировать рабочие нагрузки Kubernetes нашего стека в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**
2. Выберите **Ready-made dashboards**
3. Выберите **Search documents** и введите `Kubernetes`
4. Выберите **Kubernetes Namespaces - Workloads**, чтобы открыть готовый дашборд
5. Откройте селектор сегментов и в разделе **Filter by segments** выберите ранее созданный сегмент `dtp-dev3`
6. Откройте фильтр дашборда **Cluster**, чтобы найти кластеры, отфильтрованные для выбранного сегмента

   ![Дашборд: рабочие нагрузки Kubernetes в пространствах имён](https://dt-cdn.net/images/segments-k8s-dashboard-workloads-2640-c406e3c410.png)

Применяя наш сегмент, мы сужаем контекст дашборда, что позволяет исключить весь посторонний шум одним нажатием.

Применение сегмента к дашбордам будет фильтровать данные, явно включённые в сегмент. Некоторые плитки могут больше не показывать результаты, потому что запрашиваемые данные не включены в применённый сегмент.

## Заключение

Вы настроили сегмент для набора кластеров Kubernetes, которые образуют общий стек. Вы узнали, как сегменты можно применять для удобной фильтрации данных в различных приложениях. Вы увидели пример того, как анализировать состояние и производительность среды мониторинга без необходимости писать или разбираться в хотя бы одной строке DQL.

Так же как и для кластеров Kubernetes, сегменты можно строить в контексте пространств имён Kubernetes. Просто используйте `k8s.namespace.name` и выберите все связанные сущности **Kubernetes namespaces (dt.entity.cloud\_application\_namespace)** вместо этого.
