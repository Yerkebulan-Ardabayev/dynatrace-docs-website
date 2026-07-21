---
title: Миграция с классического режима мониторинга полного стека на режим мониторинга приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring
---

# Миграция с классического режима мониторинга полного стека на режим мониторинга приложений

# Миграция с классического режима мониторинга полного стека на режим мониторинга приложений

* 3 мин чтения
* Обновлено 03 июня 2026

Dynatrace Operator версии 1.0.0+

В этом руководстве описаны шаги, необходимые для миграции развёртывания Dynatrace с классического мониторинга полного стека на [режим мониторинга приложений](/managed/ingest-from/setup-on-k8s/how-it-works#auto "Подробное описание того, как работает развёртывание на Kubernetes.").

## Преимущества

Для мониторинга только выбранных приложений на Kubernetes мониторинг приложений предлагает гибкий подход со следующими преимуществами:

* Режим мониторинга приложений, аналогично режиму cloud native full stack, предотвращает состояния гонки, которые могут возникать при одновременном запуске подов DaemonSet OneAgent и подов отслеживаемых приложений.
* За счёт использования концепций Kubernetes, таких как admission webhooks и CSI-драйвер для внедрения Code Module, режим мониторинга приложений снижает требуемый уровень привилегий для OneAgent.

### Соображения и последствия

* При переключении на мониторинг приложений ранее развёрнутые OneAgent будут деактивированы, а глубокий мониторинг приложений остановится. Соответственно, обязательным становится перезапуск всех подов приложений, которым требуется глубокий мониторинг. Перезапуск этих подов гарантирует повторное внедрение в приложения, что позволяет возобновить глубокий мониторинг.
* В режиме мониторинга приложений правила мониторинга контейнеров игнорируются. Вместо этого для точного управления внедрением OneAgent следует использовать [селекторы меток](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов").
* Для потоковой передачи логов можно:

  + [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").
  + [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

## Миграция на режим мониторинга приложений

В этом разделе приведена вся информация, необходимая для миграции с классического режима на режим мониторинга приложений.

Использование container runtime CRI-O

Описанная ниже стандартная процедура миграции требует версии OneAgent 1.281 или выше для кластеров Kubernetes, использующих CRI-O в качестве container runtime, поэтому перед выполнением приведённых ниже шагов нужно соответствующим образом обновить OneAgent.

Если это обновление выполнить нельзя, следует выполнить процедуру [Работа с CRI-O при версиях OneAgent 1.279 или более ранних](#running-crio) для альтернативного сценария миграции, а затем вернуться к шагу 1 этой процедуры.

1. Рекомендуется

   Обновить установку с включённым CSI-драйвером:

   Helm

   Манифест

   ```
   helm upgrade dynatrace-operator oci://docker.io/dynatrace/dynatrace-operator \



   --reset-then-reuse-values \



   --atomic \



   --csidriver.enabled="true" \ # By default CSI driver is enabled



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
2. Перенастроить (существующий) DynaKube для режима мониторинга приложений:

   Следующее сравнение бок о бок показывает, как перенастроить DynaKube CR с классического full-stack на мониторинг приложений:

   Классический мониторинг полного стека

   Мониторинг приложений

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

   Дополнительную информацию о настройке DynaKube для режима мониторинга приложений можно найти в [руководстве по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes") или в разделе [параметры DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "Список доступных параметров для настройки Dynatrace Operator на Kubernetes."). Также можно скачать [пример пользовательского ресурса DynaKube​](https://dt-url.net/0w036dz) для мониторинга приложений из GitHub и адаптировать пользовательский ресурс DynaKube под свои требования.
3. Применить пользовательский ресурс DynaKube:

   Выполнить приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube. Webhook валидации выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в классическом режиме full-stack и вскоре после этого к прекращению глубокого мониторинга подов приложений.
4. Дождаться готовности code modules:

   Dynatrace Operator подхватывает изменения в пользовательском ресурсе DynaKube и обеспечивает доступность code modules на каждом узле.

   CSI-драйвер генерирует события Kubernetes, привязанные к пользовательскому ресурсу DynaKube, когда code modules готовы и доступны на каждом узле. Перед переходом к следующему шагу нужно дождаться, пока событие будет зафиксировано для каждого узла.
5. Перезапустить рабочие нагрузки приложений:

   Незамедлительно перезапустить все рабочие нагрузки приложений, чтобы инициировать внедрение code module и включить глубокий мониторинг, минимизируя простои мониторинга.

#### Работа с CRI-O при версиях OneAgent 1.279 или более ранних

В этом разделе описана процедура миграции для кластеров Kubernetes, использующих container runtime CRI-O и версию OneAgent 279 или более раннюю.

Необходимо удалить хуки CRI-O, установленные и используемые для внедрения OneAgent в классическом режиме full-stack. Дополнительные сведения о хуках CRI-O приведены в этой [статье блога Red Hat​](https://dt-url.net/fq039v2).

Показать пошаговые инструкции

Чтобы успешно перейти с классического режима full-stack, нужно выполнить следующие инструкции:

1. Удалить пользовательский ресурс DynaKube:

   Удалить DynaKube, настроенный в классическом режиме full-stack, выполнив следующую команду:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   Это действие приведёт к удалению OneAgent в классическом режиме full-stack и вскоре после этого к прекращению глубокого мониторинга подов приложений. Кроме того, если мониторинг Kubernetes настроен в пользовательском ресурсе DynaKube, мониторинг Kubernetes немедленно прекратится с удалением ActiveGate.
2. Дождаться завершения работы подов OneAgent.
3. Выполнить инструкции из раздела [Очистка узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Пути обновления, процедуры обновления и руководство по удалению Dynatrace Operator."), чтобы удалить хуки CRI-O Dynatrace со всех узлов Linux.
4. Продолжить с шага 1 [стандартной процедуры миграции](#migrate).

## Изменения в ресурсах Kubernetes

Миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима мониторинга приложений. Основные изменения включают:

| Компонент | классический full-stack | Мониторинг приложений |
| --- | --- | --- |
| Dynatrace Oneagent | * Развёрнут как DaemonSet * Собирает метрики хоста на узлах * Внедряет code modules в поды приложений | * Отсутствует |
| Dynatrace Webhook Server | * Проверяет определения DynaKube | * Проверяет определения DynaKube * Внедряет code modules в поды приложений путём изменения определений подов |
| [CSI-драйвер Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание того, как работает развёртывание на Kubernetes.")  Опционально | * Отсутствует | * Развёрнут как DaemonSet * Оптимизирует загрузку code modules для ускорения внедрения в поды и снижения расхода хранилища |