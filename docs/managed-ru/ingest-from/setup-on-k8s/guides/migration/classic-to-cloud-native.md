---
title: Миграция из режима classic full-stack в режим cloud-native full-stack
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native
---

# Миграция из режима classic full-stack в режим cloud-native full-stack

# Миграция из режима classic full-stack в режим cloud-native full-stack

* Чтение: 4 мин
* Обновлено 05 сентября 2025 г.

Dynatrace Operator версии 1.0.0+

В этом руководстве описаны шаги, необходимые для миграции развёртывания Dynatrace из режима classic full-stack в [режим cloud-native full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание на Kubernetes.").

## Преимущества

Режим развёртывания cloud-native full-stack представляет собой значительный шаг вперёд в области безопасности, используя облачно-нативные методы для инъекции OneAgent. Такой подход устраняет два ключевых ограничения, присущих традиционному режиму full stack:

* Режим cloud-native full-stack предотвращает состояния гонки, которые могут возникать при одновременном запуске подов DaemonSet OneAgent и подов отслеживаемого приложения.
* Используя концепции Kubernetes, такие как admission webhooks и CSI driver для инъекции Code Module, мониторинг cloud-native full-stack снижает набор привилегий, требуемых для OneAgent.

### Нюансы и последствия

* При переходе на мониторинг cloud-native full-stack ранее развёрнутые OneAgent деактивируются, и глубокий мониторинг приложений прекращается. Соответственно, требуется перезапуск всех подов приложений, для которых нужен глубокий мониторинг. Перезапуск этих подов обеспечит повторную инъекцию в приложения, что позволит возобновить глубокий мониторинг.
* В режиме cloud-native full-stack идентификаторы хостов определяются иначе, из-за чего на экранах списка хостов временно присутствуют одновременно новые и старые хосты. Старые сущности хостов и связанные с ними данные подчиняются политике хранения данных, определённой в Dynatrace, и остаются доступными в течение указанного срока.
* В режиме cloud-native full-stack правила мониторинга контейнеров игнорируются. Вместо них для точного управления инъекцией OneAgent следует использовать [селекторы меток](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов").

## Миграция в cloud-native full-stack

В этом разделе содержится вся информация, необходимая для миграции из режима classic full-stack в режим cloud-native full-stack.

Использование container runtime CRI-O

Стандартная процедура миграции, описанная ниже, требует OneAgent версии 1.281 или выше для кластеров Kubernetes, использующих в качестве container runtime CRI-O, поэтому перед выполнением приведённых ниже шагов нужно соответствующим образом обновить OneAgent.

Если такое обновление выполнить нельзя, следуй процедуре [Запуск CRI-O с версиями OneAgent 1.279 или более ранними](#running-crio) для альтернативного сценария миграции, а затем вернись к шагу 1 этой процедуры.

1. Обновление установки с включённым CSI driver:

   Helm

   Манифест

   ```
   helm upgrade dynatrace-operator oci://docker.io/dynatrace/dynatrace-operator \



   --reset-then-reuse-values \



   --atomic \



   --csidriver.enabled="true" \ # По умолчанию CSI driver включён



   --namespace dynatrace
   ```

   **Kubernetes**

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/kubernetes-csi.yaml
   ```

   **OpenShift**

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.0/openshift-csi.yaml
   ```
2. Переконфигурирование (существующего) DynaKube для режима cloud-native full-stack:

   Следующее сравнение бок о бок показывает, как переконфигурировать DynaKube CR из режима classic full-stack в мониторинг cloud-native full-stack:

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

   Дополнительную информацию о том, как настроить DynaKube для режима cloud-native full-stack, можно найти в сравнении ниже, в [руководстве по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме cloud-native full-stack на Kubernetes") или в разделе [параметры DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-cloudnativefullstack "Список доступных параметров для настройки Dynatrace Operator на Kubernetes."). Также можно скачать [образец пользовательского ресурса DynaKube﻿](https://dt-url.net/9n636jg) для cloud-native full-stack из GitHub и адаптировать пользовательский ресурс DynaKube в соответствии со своими требованиями.
3. Применение пользовательского ресурса DynaKube:

   Выполни приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube. Если возникнет проблема, validation webhook выдаст понятные сообщения об ошибках.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в режиме classic full-stack, а вскоре после этого, соответственно, к прекращению глубокого мониторинга подов приложений.
4. Ожидание готовности OneAgent:

   Dynatrace Operator подхватит изменения в пользовательском ресурсе DynaKube и обеспечит доступность новых OneAgent на каждом узле.
5. Перезапуск рабочих нагрузок приложений:

   Незамедлительно перезапусти все рабочие нагрузки приложений, чтобы запустить инъекцию OneAgent и включить глубокий мониторинг, предотвращая или минимизируя простои мониторинга.

#### Запуск CRI-O с версиями OneAgent 1.279 или более ранними

В этом разделе описана процедура миграции для кластеров Kubernetes, использующих container runtime CRI-O и работающих на версии OneAgent 279 или более ранней.

Необходимо удалить хуки CRI-O, установленные и используемые для инъекции OneAgent в режиме classic full-stack. Дополнительные сведения о хуках CRI-O смотри в этой [статье блога Red Hat﻿](https://dt-url.net/fq039v2).

Показать пошаговые инструкции

Следуй этим инструкциям для успешной миграции из режима classic full-stack:

1. Удаление пользовательского ресурса DynaKube:

   Удали DynaKube, настроенный в режиме classic full-stack, выполнив следующую команду:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   Это действие приведёт к удалению OneAgent в режиме classic full-stack, а вскоре после этого, соответственно, к прекращению глубокого мониторинга подов приложений. Кроме того, если мониторинг Kubernetes настроен в пользовательском ресурсе DynaKube, мониторинг Kubernetes прекратится мгновенно вместе с удалением ActiveGate.
2. Дождись завершения работы подов OneAgent.
3. Следуй инструкциям в разделе [Очистка узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator."), чтобы удалить хуки CRI-O Dynatrace со всех узлов Linux.
4. Продолжи с шага 1 [стандартной процедуры миграции](#migrate).

## Изменения в ресурсах Kubernetes

Эта миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима инъекции cloud-native. Основные изменения:

| Компонент | classic full-stack | cloud-native full-stack |
| --- | --- | --- |
| OneAgent | * Развёрнут как DaemonSet * Собирает метрики хоста на узлах * Инъецирует code modules в поды приложений | * Развёрнут как DaemonSet * Собирает метрики хоста на узлах |
| Dynatrace Webhook Server | * Валидирует определения DynaKube | * Валидирует определения DynaKube * Инъецирует code modules в поды приложений путём изменения определений подов |
| [CSI driver Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание того, как работает развёртывание на Kubernetes.")  Обязательно | * Отсутствует | * Развёрнут как DaemonSet * Оптимизирует загрузку code modules для ускорения инъекции подов и снижения потребления хранилища |