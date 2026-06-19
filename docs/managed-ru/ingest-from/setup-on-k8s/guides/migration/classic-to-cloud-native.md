---
title: Миграция с классического full-stack на режим cloud-native full-stack
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native
scraped: 2026-05-12T11:23:58.421376
---

# Миграция с классического full-stack на режим cloud-native full-stack

# Миграция с классического full-stack на режим cloud-native full-stack

* Чтение: 4 мин
* Обновлено 5 сентября 2025 г.

Dynatrace Operator версии 1.0.0+

В этом руководстве описаны шаги, необходимые для миграции вашего развёртывания Dynatrace с классического full-stack на [режим cloud-native full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание в Kubernetes.").

## Преимущества

Режим развёртывания cloud-native full-stack представляет собой значительное продвижение в области безопасности и использует облачные методы для внедрения OneAgent. Этот подход устраняет два ключевых ограничения традиционного режима full-stack:

* Режим cloud-native full-stack предотвращает состояния гонки, которые могут возникать, когда поды DaemonSet OneAgent и поды отслеживаемого приложения запускаются одновременно.
* Используя концепции Kubernetes, такие как admission webhooks и CSI driver для внедрения Code Module, мониторинг cloud-native full-stack снижает необходимые привилегии для OneAgent.

### Аспекты и последствия

* При переключении на мониторинг cloud-native full-stack ранее развёрнутые экземпляры OneAgent будут деактивированы, а глубокий мониторинг приложений остановится. Следовательно, перезапуск всех подов приложений, требующих глубокого мониторинга, становится обязательным. Перезапуск этих подов обеспечит повторное внедрение в приложения и позволит возобновить глубокий мониторинг.
* В режиме cloud-native full-stack идентификаторы хостов определяются иначе, что приводит к временному присутствию как новых, так и старых хостов на экранах списка хостов. Старые сущности хостов и связанные с ними данные подчиняются политике хранения данных, определённой Dynatrace, и остаются доступными в течение указанного срока.
* В режиме cloud-native full-stack правила мониторинга контейнеров игнорируются. Вместо них для точного управления внедрением OneAgent следует использовать [селекторы меток](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов").

## Миграция на cloud-native full-stack

В этом разделе приведена вся информация, необходимая для миграции с классического режима на режим cloud-native full-stack.

Использование среды выполнения контейнеров CRI-O

Описанная ниже стандартная процедура миграции требует OneAgent версии 1.281 или выше для кластеров Kubernetes, использующих CRI-O в качестве среды выполнения контейнеров, поэтому перед продолжением выполнения шагов ниже необходимо соответствующим образом обновить экземпляры OneAgent.

Если это обновление выполнить невозможно, воспользуйтесь процедурой [Запуск CRI-O с OneAgent версии 1.279 или ранее](#running-crio) для альтернативного порядка миграции, а затем вернитесь к шагу 1 этой процедуры.

1. Обновите установку с включённым CSI driver:

   Helm

   Manifest

   ```
   helm upgrade dynatrace-operator oci://docker.io/dynatrace/dynatrace-operator \



   --atomic \



   --csidriver.enabled="true" \ # By default CSI driver is enabled



   --namespace dynatrace
   ```

   **Kubernetes**

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
   ```

   **OpenShift**

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
   ```
2. Перенастройте (существующий) DynaKube для режима cloud-native full-stack:

   Следующее параллельное сравнение показывает, как перенастроить ресурс DynaKube CR с классического full-stack на мониторинг cloud-native full-stack:

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

   Дополнительные сведения о настройке DynaKube для режима cloud-native full-stack см. в сравнении ниже, обратитесь к [руководству по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме cloud-native full-stack в Kubernetes") или к [параметрам DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-cloudnativefullstack "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Кроме того, можно загрузить [пример пользовательского ресурса DynaKube](https://dt-url.net/9n636jg) для cloud-native full-stack из GitHub и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.
3. Примените пользовательский ресурс DynaKube:

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube. Валидирующий вебхук предоставит полезные сообщения об ошибках при наличии проблемы.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению экземпляров OneAgent в режиме classic full-stack и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого.
4. Дождитесь готовности экземпляров OneAgent:

   Dynatrace Operator подхватит изменения в пользовательском ресурсе DynaKube и обеспечит доступность новых экземпляров OneAgent на каждом узле.
5. Перезапустите рабочие нагрузки приложений:

   Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы инициировать внедрение OneAgent и включить глубокий мониторинг, предотвращая или минимизируя перерывы в мониторинге.

#### Запуск CRI-O с OneAgent версии 1.279 или ранее

В этом разделе описана процедура миграции для кластеров Kubernetes, использующих среду выполнения контейнеров CRI-O и работающих с OneAgent версии 279 или ранее.

Необходимо удалить хуки CRI-O, установленные и используемые для внедрения OneAgent в режиме classic full-stack. Дополнительные сведения о хуках CRI-O см. в этой [записи блога Red Hat](https://dt-url.net/fq039v2).

Показать пошаговые инструкции

Следуйте этим инструкциям, чтобы успешно выполнить миграцию с режима classic full-stack:

1. Удалите пользовательский ресурс DynaKube:

   Удалите DynaKube, настроенный в режиме classic full-stack, выполнив следующую команду:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   Это действие приведёт к удалению экземпляров OneAgent в режиме classic full-stack и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого. Кроме того, если в пользовательском ресурсе DynaKube настроен мониторинг Kubernetes, он остановится мгновенно при удалении ActiveGate.
2. Дождитесь завершения работы подов OneAgent.
3. Следуйте инструкциям в разделе [Очистка узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Процедуры обновления и удаления Dynatrace Operator"), чтобы удалить хуки Dynatrace CRI-O со всех узлов Linux.
4. Продолжите с шага 1 [стандартной процедуры миграции](#migrate).

## Изменения в ресурсах Kubernetes

Эта миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или добавляя новые компоненты для поддержки режима внедрения cloud-native. Ключевые изменения включают:

| Компонент | classic full-stack | cloud-native full-stack |
| --- | --- | --- |
| OneAgent | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах * Внедряет модули кода в поды приложений | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах |
| Dynatrace Webhook Server | * Проверяет определения DynaKube | * Проверяет определения DynaKube * Внедряет модули кода в поды приложений путём изменения определений подов |
| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание того, как работает развёртывание в Kubernetes.")  Обязательно | * Отсутствует | * Развёртывается как DaemonSet * Оптимизирует загрузку модулей кода для ускорения внедрения в поды и снижения потребления хранилища |