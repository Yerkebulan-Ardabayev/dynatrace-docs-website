---
title: Переход с classic full-stack на режим application monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring
---

# Переход с classic full-stack на режим application monitoring

# Переход с classic full-stack на режим application monitoring

* Чтение: 3 мин
* Обновлено 03 июн 2026

Dynatrace Operator версии 1.0.0+

В этом руководстве описаны шаги, необходимые для перехода развёртывания Dynatrace с classic full-stack monitoring на [application monitoring mode](/managed/ingest-from/setup-on-k8s/how-it-works#auto "Подробное описание принципов развёртывания на Kubernetes.").

## Преимущества

Для мониторинга только выбранных приложений на Kubernetes application monitoring предлагает гибкий подход со следующими преимуществами:

* Режим application monitoring, аналогично cloud native full stack mode, предотвращает гонки состояний, которые могут возникать при одновременном запуске подов DaemonSet OneAgent и подов наблюдаемых приложений.
* Используя концепции Kubernetes, такие как admission webhooks и CSI driver для инжекции Code Module, режим application monitoring снижает необходимые привилегии для OneAgent.

### Рекомендации и последствия

* При переключении на application monitoring ранее развёрнутые OneAgent будут деактивированы, и глубокий мониторинг приложений остановится. Поэтому перезапуск всех подов приложений, требующих глубокого мониторинга, становится обязательным. Перезапуск этих подов гарантирует повторную инжекцию в приложения и позволяет возобновить глубокий мониторинг.
* В режиме application monitoring правила мониторинга контейнеров игнорируются. Вместо этого для точного управления инжекцией OneAgent следует использовать [label selectors](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов").
* Для потоковой передачи логов можно:

  + [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
  + [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

## Переход на режим application monitoring

В этом разделе собрана вся необходимая информация для перехода с classic на application monitoring mode.

Использование среды выполнения контейнеров CRI-O

Стандартная процедура перехода, описанная ниже, требует OneAgent версии 1.281 или выше для кластеров Kubernetes, использующих CRI-O в качестве среды выполнения контейнеров, поэтому перед продолжением необходимо соответствующим образом обновить OneAgent.

Если такое обновление невозможно, выполните процедуру [Запуск CRI-O с OneAgent версий 1.279 и ниже](#running-crio) для альтернативного сценария перехода, а затем вернитесь к шагу 1 данной процедуры.

1. Recommended

   Обновить установку с включённым CSI driver:

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
2. Перенастроить (существующий) DynaKube для режима application monitoring:

   Следующее сравнение «до и после» показывает, как перенастроить DynaKube CR с classic full-stack на application monitoring:

   Classic full-stack monitoring

   Application monitoring

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



   classicFullStack:



   args:



   - "--set-host-group=<host-group>"



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



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   Подробнее о настройке DynaKube для режима application monitoring см. в [deployment guide](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes") или [DynaKube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "Список доступных параметров для настройки Dynatrace Operator на Kubernetes."). Кроме того, можно скачать [образец DynaKube custom resource﻿](https://dt-url.net/0w036dz) для application monitoring из GitHub и адаптировать DynaKube custom resource под свои требования.
3. Применить DynaKube custom resource:

   Выполните приведённую ниже команду для применения DynaKube custom resource. При наличии проблем validation webhook выдаст полезные сообщения об ошибках.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в режиме classic full-stack и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого.
4. Дождаться готовности code modules:

   Dynatrace Operator получает изменения в DynaKube custom resource и обеспечивает доступность code modules на каждом узле.

   CSI driver генерирует события Kubernetes, прикреплённые к DynaKube custom resource, когда code modules готовы и доступны на каждом узле. Дождитесь появления события для каждого узла перед переходом к следующему шагу.
5. Перезапустить рабочие нагрузки приложений:

   Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы инициировать инжекцию code module, включить глубокий мониторинг и минимизировать перерывы в мониторинге.

#### Запуск CRI-O с OneAgent версий 1.279 и ниже

В этом разделе описана процедура перехода для кластеров Kubernetes, использующих среду выполнения контейнеров CRI-O и работающих с OneAgent версии 279 или более ранней.

Необходимо удалить CRI-O hooks, установленные и используемые для инжекции OneAgent в режиме classic full-stack. Дополнительные сведения о CRI-O hooks см. в этой [публикации блога Red Hat﻿](https://dt-url.net/fq039v2).

Показать пошаговые инструкции

Следуйте этим инструкциям для успешного перехода с режима classic full-stack:

1. Удалить DynaKube custom resource:

   Удалите DynaKube, настроенный в режиме classic full-stack, выполнив следующую команду:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   Это действие приведёт к удалению OneAgent в режиме classic full-stack и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого. Кроме того, если в DynaKube custom resource настроен мониторинг Kubernetes, мониторинг Kubernetes остановится незамедлительно после удаления ActiveGate.
2. Дождаться завершения работы подов OneAgent.
3. Следуйте инструкциям в разделе [Cleanup nodes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator."), чтобы удалить CRI-O hooks Dynatrace со всех Linux-узлов.
4. Перейдите к шагу 1 [стандартной процедуры перехода](#migrate).

## Изменения в ресурсах Kubernetes

Переход затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима application monitoring. Ключевые изменения:

| Компонент | classic full-stack | Application monitoring |
| --- | --- | --- |
| Dynatrace Oneagent | * Развёрнут как DaemonSet * Сбор метрик хоста на узлах * Инжекция code modules в поды приложений | * Отсутствует |
| Dynatrace Webhook Server | * Валидация определений DynaKube | * Валидация определений DynaKube * Инжекция code modules в поды приложений путём изменения определений подов |
| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание принципов развёртывания на Kubernetes.")  Optional | * Отсутствует | * Развёрнут как DaemonSet * Оптимизирует загрузку code modules для ускорения инжекции подов и снижения потребления хранилища |