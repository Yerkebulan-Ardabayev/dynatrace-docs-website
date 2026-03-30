---
title: Обогащение метаданными всей телеметрии, поступающей из Kubernetes
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment
scraped: 2026-03-06T21:23:30.344451
---

* Latest Dynatrace

## Предварительные требования

* Dynatrace Operator установлен и работает в вашем кластере Kubernetes.
* В вашем кластере применён действительный DynaKube.
* Включено обогащение метаданными.

## Сценарии использования

* Дополнение ваших метрик, логов, данных трассировки, событий и сущностей дополнительной информацией с помощью аннотаций и меток пространств имён Kubernetes.
* Дополнение ваших метрик, логов, данных трассировки, событий и сущностей дополнительной информацией с помощью переменных среды OpenTelemetry.
* Обогащённые данные могут использоваться для определения управления доступом пользователей или для решения задач распределения затрат в DPS.
* Обогащённые данные могут использоваться для маршрутизации в пайплайнах, сегментации по бакетам, сегментации и фильтрации.

## Контекст безопасности и распределение затрат

В Dynatrace вы можете настроить границы политик для детализированных ограничений на уровне данных. По умолчанию вы можете использовать `k8s.namespace.name` и `k8s.cluster.name`, но иногда этого недостаточно и требуется более детальный способ настройки границ.

Возможно, вы уже определили такие границы для себя и задали их в виде меток или аннотаций Kubernetes. Эта функция позволяет использовать их у источника для вашего контекста безопасности в Dynatrace. Если вы ещё этого не сделали, мы рекомендуем использовать имя кластера или пространства имён либо настроить специальную аннотацию для рабочих нагрузок Kubernetes, которая будет служить контекстом безопасности.

Аналогичным образом Dynatrace предоставляет решение для [распределения затрат](../../../../license/cost-allocation.md#assign-cost-centers-and-products-in-kubernetes-application-monitoring-deployments "Узнайте, как распределять затраты по центрам затрат и продуктам.") в DPS. Возможно, у вас уже есть необходимые данные, такие как подразделение и продукт, в существующих метках или аннотациях Kubernetes. Даже если нет, вам может быть удобно настроить распределение затрат в виде аннотации или метки Kubernetes, что и рекомендует Dynatrace. Эта функция позволяет использовать эти метки и аннотации для решения задач [распределения затрат](../../../../license/cost-allocation.md#assign-cost-centers-and-products-in-kubernetes-application-monitoring-deployments "Узнайте, как распределять затраты по центрам затрат и продуктам.") в DPS.

Поддерживаются следующие атрибуты:

* [`dt.security_context`](../../../../platform/grail/organize-data/assign-permissions-in-grail.md#grail-permissions-table-record "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.")
* [`dt.cost.costcenter`](../../../../semantic-dictionary/fields.md#dynatrace "Ознакомьтесь со списком глобальных полей с определённым семантическим значением в Dynatrace.")
* [`dt.cost.product`](../../../../semantic-dictionary/fields.md#dynatrace "Ознакомьтесь со списком глобальных полей с определённым семантическим значением в Dynatrace.")

## Доменные теги

Для упрощения таких задач, как выбор бакетов, сегментация, фильтрация и маршрутизация проблем, Dynatrace позволяет обогащать телеметрические данные с помощью существующих меток или аннотаций пространств имён Kubernetes. Эти теги становятся доступны как доменные поля, например `k8s.namespace.label.your_key` или `k8s.namespace.annotation.your_key`.

## Какие данные будут обогащены

## Варианты обогащения

В зависимости от конкретного сценария поддерживаются следующие варианты обогащения:

### Использование настроек для существующих меток и аннотаций пространств имён (рекомендуется)

Мы рекомендуем этот вариант, так как это единственный вариант, который обогащает все сигналы, включая метрики платформы Kubernetes, события и сущности — в отличие от переменных среды или ручных аннотаций подов. Используйте правила обогащения Kubernetes для применения существующих меток и аннотаций пространств имён.
Конфигурация на уровне тенанта применяется ко всем кластерам Kubernetes по умолчанию. Однако при необходимости вы можете переопределить её для конкретных кластеров.

Совет: если вы настроите правила до развёртывания DynaKube, вам не придётся ждать 45 минут для распространения правил.

1. Перейдите в **Kubernetes App** > **Namespace** > Выберите ваше пространство имён, чтобы увидеть обзор существующих меток.

   ![Детали пространства имён в приложении K8s с текущими метками](https://dt-cdn.net/images/namespace-labels-1997-2a0370e1ef.png)
2. Перейдите в **Settings** > **Cloud and virtualization** > **Kubernetes Telemetry Enrichment**.
3. Выберите **Add rule**.
4. Выберите `Annotation` или `Label` в выпадающем списке **Metadata type**.
5. Введите ключ аннотации/метки пространства имён в поле **Source**, следуя [соглашениям Kubernetes](https://dt-url.net/2c02sbn).
6. Чтобы использовать ключ аннотации или метки в качестве имени поля, включите **Enrich telemetry with label/annotation directly**.

   ![Обогащение телеметрии меткой/аннотацией напрямую](https://dt-cdn.net/images/enrich-telemetry-with-label-annotation-directly-693-b6d33d539e.png)
7. Для переназначения отключите **Enrich telemetry with label/annotation directly** и выберите значение из выпадающего списка **Target**.

   ![Настройки обогащения для переназначения](https://dt-cdn.net/images/enrichment-settings-for-remapping-663-33a85e6613.png)
8. Выберите **Save changes**.
9. После создания или изменения правил подождите до 45 минут, чтобы изменения вступили в силу. По истечении этого времени перезапустите ваши поды.
10. Перейдите к вашим данным и убедитесь, что метаданные успешно обогащены.

![Детали лога с обогащёнными метаданными](https://dt-cdn.net/images/enriched-log-652-55590251f6.png)

### Использование специальных аннотаций подов для метаданных Dynatrace

Этот вариант работает автоматически для сценариев OneAgent и OpenTelemetry с изменением кода.

Этот вариант предназначен для сценариев, когда метки или аннотации пространств имён не могут использоваться в качестве источника. Если оба метода присутствуют, аннотации, добавленные вручную, имеют приоритет.

В отличие от подхода на основе настроек, аннотации подов, добавленные вручную, не обеспечивают полного обогащения. Они не обогащают метрики Kubernetes, события Kubernetes или сущности.
Чтобы метрики OneAgent и метрики сервисов были обогащены этими атрибутами, они должны следовать соглашению `k8s.namespace.<label>/<annotation>.<key>: <value>`.

Для всестороннего обогащения рекомендуется подход на основе настроек.

Вы можете создать следующие аннотации на уровне пода:

```
metadata:


annotations:


metadata.dynatrace.com/dt.security_context: sre


metadata.dynatrace.com/dt.cost.costcenter: it_services


metadata.dynatrace.com/dt.cost.product: fin_app


metadata.dynatrace.com/k8s.namespace.label.domain: finance
```

Следующие атрибуты обогатят данные:

```
dt.security_context: sre


dt.cost.costcenter: it_services


dt.cost.product: fin_app


k8s.namespace.label.domain: finance
```

## Настройка OpenTelemetry

Для OTLP-конфигураций без OneAgent требуются дополнительные шаги для обогащения сигналов. Это можно сделать либо путём изменения кода для разбора файлов метаданных, предоставленных оператором, либо с помощью переменных среды.

### Включение автоматической настройки экспортёра OTLP OpenTelemetry (рекомендуется)

Автоматическая настройка экспортёра OTLP OpenTelemetry — рекомендуемый вариант для OTLP-конфигураций без инъекции OneAgent, так как он обеспечивает обогащение, сопоставимое с вариантом OneAgent. Включите его в DynaKube для автоматического обогащения телеметрии метаданными Dynatrace. Эта функция доступна для всех языков, поддерживаемых OpenTelemetry.

### Обогащение через изменение кода

Этот вариант подходит для автономных OTLP-конфигураций без инъекции OneAgent. Для оптимальных результатов обогатите OTLP-телеметрию, разбирая файлы метаданных Dynatrace и добавляя метаданные непосредственно в коде, как описано в разделе [Обогащение принимаемых данных специфическими полями Dynatrace](../../../extend-dynatrace/extend-data.md#operator-enrichment-directory "Узнайте, как автоматически обогащать телеметрические данные специфическими полями Dynatrace."). Примеры кода можно найти в разделе OpenTelemetry, например, для Java.
Этот подход обеспечивает обогащение, сопоставимое с вариантом OneAgent.

### Обогащение через переменную среды

Если изменение кода невозможно, вы можете использовать переменную среды [`OTEL_RESOURCE_ATTRIBUTES`](https://dt-url.net/ne03unx) для обогащения. Однако этот метод имеет ограничения: настройка может быть сложной, а некоторые свойства, такие как k8s.container.name и теги, должны задаваться как статические строки.

1. Создайте config map для атрибутов уровня кластера

1. Сохраните имя DynaKube

```
DYNAKUBE="dynakube" # set this to the name of your DynaKube / kubectl get dynakube -n dynatrace
```

2. Получите `k8s.cluster.uid`

```
K8S_CLUSTER_UID="$(kubectl get dynakube -o jsonpath='{.status.kubeSystemUUID}' -n dynatrace $DYNAKUBE)"
```

3. Получите `k8s.cluster.name`

```
K8S_CLUSTER_NAME="$(kubectl get dynakube -o jsonpath='{.status.kubernetesClusterName}' -n dynatrace $DYNAKUBE)"
```

4. Получите сущность Kubernetes `dt.entity.kubernetes_cluster`

```
DT_ENTITY_KUBERNETES_CLUSTER="$(kubectl get dynakube -o jsonpath='{.status.kubernetesClusterMEID}' -n dynatrace $DYNAKUBE)"
```

5. Создайте config map в целевом пространстве имён

```
kubectl create configmap dynatrace-metadata \


--from-literal K8S_CLUSTER_UID=$K8S_CLUSTER_UID \


--from-literal K8S_CLUSTER_NAME=$K8S_CLUSTER_NAME \


--from-literal DT_ENTITY_KUBERNETES_CLUSTER=$DT_ENTITY_KUBERNETES_CLUSTER \


--namespace <YOUR_NAMESPACE>
```

2. Задайте атрибуты K8s через Downward API в поде

Адаптируйте спецификацию пода Kubernetes, добавив следующие переменные среды. Вы можете включить их в манифест Deployment или Pod.

Теги и `k8s.container.name` нельзя задать через Downward API.
Они должны быть указаны как статические строки.

```
envFrom:


- configMapRef:


name: dynatrace-metadata


optional: false


env:


- name: K8S_CONTAINER_NAME


value: "" # replace with actual container name


- name: K8S_POD_NAME


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.name


- name: K8S_POD_UID


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.uid


- name: K8S_POD_NAMESPACE


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.namespace


- name: K8S_WORKLOAD_KIND


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.annotations['metadata.dynatrace.com/k8s.workload.kind'] # only works when metadata enrichment is enabled


- name: K8S_WORKLOAD_NAME


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.annotations['metadata.dynatrace.com/k8s.workload.name'] # only works when metadata enrichment is enabled


- name: K8S_NODE_NAME


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: spec.nodeName


- name: DT_SECURITY_CONTEXT # only works when automatic security context enrichment is configured


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.annotations['metadata.dynatrace.com/dt.security_context']


- name: DT_COST_PRODUCT # only works when automatic cost product enrichment is configured


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.annotations['metadata.dynatrace.com/dt.cost.product']


- name: DT_COST_COSTCENTER # only works when automatic cost center enrichment is configured


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: metadata.annotations['metadata.dynatrace.com/dt.cost.costcenter']
```

3. Добавьте атрибуты в `OTEL_RESOURCE_ATTRIBUTES`

В этом примере показаны все рекомендуемые атрибуты. Удалите атрибуты, которые не используются.

```
- name: OTEL_RESOURCE_ATTRIBUTES


value: k8s.cluster.name=$(K8S_CLUSTER_NAME),k8s.cluster.uid=$(K8S_CLUSTER_UID),k8s.node.name=$(K8S_NODE_NAME),k8s.workload.name=$(K8S_WORKLOAD_NAME),k8s.workload.kind=$(K8S_WORKLOAD_KIND),k8s.pod.name=$(K8S_POD_NAME),k8s.pod.uid=$(K8S_POD_UID),k8s.namespace.name=$(K8S_POD_NAMESPACE),k8s.container.name=$(K8S_CONTAINER_NAME),dt.entity.kubernetes_cluster=$(DT_ENTITY_KUBERNETES_CLUSTER),dt.security_context=$(DT_SECURITY_CONTEXT),dt.cost.costcenter=$(DT_COST_COSTCENTER),dt.cost.product=$(DT_COST_PRODUCT)
```

Чтобы узнать, как обогащать сигналы метаданными релизов с помощью переменной среды `OTEL_RESOURCE_ATTRIBUTES`, обратитесь к [стратегиям обнаружения версий](../../../../deliver/release-monitoring/version-detection-strategies.md#otel_resource_attributes "Метаданные для обнаружения версий в различных технологиях").

## Ограничения

* Лимит: 20 правил на область конфигурации.
* После создания или изменения правил подождите до 45 минут, чтобы изменения вступили в силу. По истечении этого времени перезапустите ваши поды.
* Аннотации подов `metadata.dynatrace.com`, установленные вручную, имеют приоритет.
* Атрибуты, добавленные вручную (кроме `dt.security_context`, `dt.cost.costcenter` или `dt.cost.product`), не обогащают метрики Kubernetes и события Kubernetes.
* Подход на основе настроек не работает совместно с аннотациями подов, добавленными вручную. Одновременное использование обоих методов может вызвать конфликты и привести к непредвиденному поведению.

## Устранение неполадок

### Проверка определения правила

* Убедитесь, что каждое правило указывает на правильный **тип метаданных** (`label` или `annotation`).
* Убедитесь, что **ключ источника** в правиле точно совпадает с ключом, существующим в пространстве имён.

### Проверка наличия исходных метаданных

* Откройте пространство имён в **приложении Dynatrace Kubernetes** и найдите ожидаемые метки/аннотации.
* Или выполните команду:

  ```
  kubectl get namespace <name> -o yaml
  ```

и проверьте разделы `metadata.labels` и `metadata.annotations`.

### Проверка включения обогащения метаданными

* Функция работает только если `metadataEnrichment` включено в конфигурации **DynaKube**.
* Если вы указываете `namespaceSelector` в DynaKube, убедитесь, что он соответствует тестируемому пространству имён.

### Подтверждение обогащения подов

* Проверьте любой под в пространстве имён:

  ```
  kubectl get pod <pod-name> -o yaml
  ```
* Найдите аннотации, начинающиеся с `metadata.dynatrace.com/...`. Их наличие означает, что метаданные обогащены.

## Примеры

Правила

Правила в `builtin:kubernetes.generic.metadata.enrichment`

```
"rules":


[


{


# rule #1


"type": "Annotation",


"source": "metadata.example.com/team",


"target": "dt.security_context"


},


{


# rule #2


"type": "Label",


"source": "department",


"target": "dt.cost.costcenter"


},


{


# rule #3


"type": "Label",


"source": "app/name",


"target": "dt.cost.product"


}


{


# rule #4


"type": "Label",


"source": "domain",


"primaryGrailTag": "true"


}


]
```

Пространство имён

Ваши существующие метки и аннотации пространства имён:

```
metadata:


annotations:


metadata.example.com/team: sre


labels:


department: it_services


app/name: fin_app


domain: finance
```

Под

Оператор создаст аннотации пода:

```
metadata:


annotations:


metadata.dynatrace.com:|


{


"dt.security_context": "sre",


"dt.cost.costcenter": "it_services",


"dt.cost.product": "fin_app",


"k8s.namespace.label.domain": "finance"


}
```

Телеметрия

Следующие атрибуты будут добавлены к данным:

```
dt.security_context: sre


dt.cost.costcenter: it_services


dt.cost.product: fin_app


k8s.namespace.label.domain: finance
```

## Связанные темы

* Обогащение принимаемых данных специфическими полями Dynatrace
* Обогащение OTLP-запросов данными Kubernetes
* Настройка каталога обогащения
