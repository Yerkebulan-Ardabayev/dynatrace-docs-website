---
title: Миграция с classic full-stack на cloud-native full-stack режим
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native
---

# Миграция с classic full-stack на cloud-native full-stack режим

# Миграция с classic full-stack на cloud-native full-stack режим

* 4 минуты чтения
* Обновлено 05 сен 2025

Dynatrace Operator version 1.0.0+

В руководстве описаны шаги для миграции развёртывания Dynatrace с classic full-stack на [cloud-native full-stack режим](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание принципов развёртывания на Kubernetes.").

## Преимущества

Cloud-native full-stack режим развёртывания, это значительный шаг вперёд в области безопасности: для инъекции OneAgent используются cloud native методы. Этот подход устраняет два ключевых ограничения традиционного режима full stack:

* Cloud-native full-stack режим исключает состояния гонки, которые могут возникать при одновременном запуске подов DaemonSet OneAgent и подов отслеживаемых приложений.
* Использование концепций Kubernetes, таких как admission webhooks и CSI driver для инъекции Code Module, позволяет cloud-native full-stack мониторингу сократить необходимые привилегии для OneAgent.

### Замечания и последствия

* При переходе на cloud-native full-stack мониторинг ранее развёрнутые OneAgent деактивируются, а глубокий мониторинг приложений прекратится. В связи с этим перезапуск всех подов приложений, которым требуется глубокий мониторинг, становится обязательным. Перезапуск этих подов обеспечит повторную инъекцию приложений и возобновление глубокого мониторинга.
* В cloud-native full-stack режиме Host ID определяются иначе, что временно приводит к одновременному присутствию новых и старых хостов на экранах со списком хостов. Старые объекты хостов и связанные с ними данные подчиняются политике хранения данных, определённой в Dynatrace, и остаются доступными в течение заданного срока.
* В cloud-native full-stack режиме правила мониторинга контейнеров игнорируются. Вместо них для точного управления инъекцией OneAgent нужно использовать [label selectors](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для namespaces и подов").

## Миграция на cloud-native full-stack

В этом разделе приведена вся необходимая информация для миграции с classic на cloud-native full-stack режим.

Использование среды выполнения контейнеров CRI-O

Стандартная процедура миграции, описанная ниже, требует OneAgent версии 1.281 или выше для кластеров Kubernetes, использующих CRI-O в качестве среды выполнения контейнеров, поэтому перед выполнением следующих шагов необходимо соответствующим образом обновить OneAgent.

Если выполнить обновление не получается, следуйте процедуре [Работа с CRI-O и OneAgent версий 1.279 или более ранних](#running-crio) как альтернативному варианту миграции, а затем вернитесь к шагу 1 данной процедуры.

1. Обновить установку с включённым CSI driver:

   Helm

   Manifest

   ```
   helm upgrade dynatrace-operator oci://docker.io/dynatrace/dynatrace-operator \



   --reset-then-reuse-values \



   --atomic \



   --csidriver.enabled="true" \ # By default CSI driver is enabled



   --namespace dynatrace
   ```

   **Kubernetes**

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes-csi.yaml
   ```

   **OpenShift**

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift-csi.yaml
   ```
2. Перенастроить (существующий) DynaKube для cloud-native full-stack режима:

   В следующем сравнении показано, как перенастроить DynaKube CR с classic full-stack на cloud-native full-stack мониторинг:

   Мониторинг classic full-stack

   Мониторинг cloud-native full-stack

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   classicFullStack: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   cloudNativeFullStack: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   Дополнительная информация о настройке DynaKube для cloud-native full-stack режима: см. сравнение ниже, [руководство по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развернуть Dynatrace Operator в cloud-native full-stack режиме на Kubernetes") или [параметры DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-cloudnativefullstack "Список доступных параметров для настройки Dynatrace Operator на Kubernetes."). Также можно загрузить [пример custom resource DynaKube﻿](https://dt-url.net/9n636jg) для cloud-native full-stack из GitHub и адаптировать custom resource DynaKube под свои требования.
3. Применить custom resource DynaKube:

   Выполните команду ниже для применения custom resource DynaKube. При наличии ошибок validation webhook выведет полезные сообщения.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в режиме classic full-stack и, как следствие, к завершению глубокого мониторинга подов приложений вскоре после этого.
4. Дождаться готовности OneAgent:

   Dynatrace Operator подхватит изменения в custom resource DynaKube и обеспечит доступность новых OneAgent на каждом узле.
5. Перезапустить рабочие нагрузки приложений:

   Перезапустите все рабочие нагрузки приложений как можно скорее, чтобы инициировать инъекцию OneAgent и включить глубокий мониторинг, предотвращая или минимизируя его простои.

#### Работа с CRI-O и OneAgent версий 1.279 или более ранних

В этом разделе описана процедура миграции для кластеров Kubernetes, использующих среду выполнения контейнеров CRI-O и работающих с OneAgent версии 279 или более ранней.

Необходимо удалить хуки CRI-O, установленные и используемые для инъекции OneAgent в режиме classic full-stack. Дополнительные сведения о хуках CRI-O см. в [публикации блога Red Hat﻿](https://dt-url.net/fq039v2).

Показать пошаговые инструкции

Следуйте этим инструкциям для успешной миграции с classic full-stack режима:

1. Удалить custom resource DynaKube:

   Удалите DynaKube, настроенный в режиме classic full-stack, выполнив следующую команду:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   Это действие приведёт к удалению OneAgent в режиме classic full-stack и, как следствие, к завершению глубокого мониторинга подов приложений вскоре после этого. Кроме того, если в custom resource DynaKube настроен мониторинг Kubernetes, он мгновенно прекратится после удаления ActiveGate.
2. Дождитесь завершения работы подов OneAgent.
3. Следуйте инструкциям в разделе [Cleanup nodes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator.") для удаления хуков CRI-O Dynatrace со всех узлов Linux.
4. Перейдите к шагу 1 [стандартной процедуры миграции](#migrate).

## Изменения в ресурсах Kubernetes

Эта миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима cloud-native injection. Ключевые изменения:

| Компонент | classic full-stack | cloud-native full-stack |
| --- | --- | --- |
| OneAgent | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах * Инъецирует code modules в поды приложений | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах |
| Dynatrace Webhook Server | * Валидирует определения DynaKube | * Валидирует определения DynaKube * Инъецирует code modules в поды приложений путём изменения определений подов |
| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание принципов развёртывания на Kubernetes.")  Обязательно | * Отсутствует | * Развёртывается как DaemonSet * Оптимизирует загрузку code modules для ускорения инъекции подов и снижения потребления хранилища |