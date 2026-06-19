---
title: Миграция с классического full-stack на режим мониторинга приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring
scraped: 2026-05-12T12:09:39.766252
---

# Миграция с классического full-stack на режим мониторинга приложений

# Миграция с классического full-stack на режим мониторинга приложений

* Чтение: 3 мин
* Обновлено 5 сентября 2025 г.

Dynatrace Operator версии 1.0.0+

В этом руководстве описаны шаги, необходимые для миграции вашего развёртывания Dynatrace с классического full-stack мониторинга на [режим мониторинга приложений](/managed/ingest-from/setup-on-k8s/how-it-works#auto "Подробное описание того, как работает развёртывание в Kubernetes.").

## Преимущества

Для мониторинга только выбранных приложений в Kubernetes мониторинг приложений предлагает гибкий подход со следующими преимуществами:

* Режим мониторинга приложений, как и режим cloud native full stack, предотвращает состояния гонки, которые могут возникать при одновременном запуске подов OneAgent DaemonSet и подов отслеживаемых приложений.
* За счёт использования концепций Kubernetes, таких как admission webhooks и CSI driver для внедрения Code Module, режим мониторинга приложений снижает требуемые привилегии для OneAgent.

### Особенности и последствия

* При переключении на мониторинг приложений ранее развёрнутые OneAgent будут деактивированы, и глубокий мониторинг приложений прекратится. Следовательно, перезапуск всех подов приложений, которым требуется глубокий мониторинг, становится обязательным. Перезапуск этих подов гарантирует повторное внедрение в приложения, что позволяет возобновить глубокий мониторинг.
* В режиме мониторинга приложений правила мониторинга контейнеров игнорируются. Вместо этого следует использовать [селекторы меток](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов") для точного управления внедрением OneAgent.
* Мониторинг логов требует [дополнительной настройки](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

## Миграция на режим мониторинга приложений

В этом разделе приведена вся информация, необходимая для миграции с классического режима на режим мониторинга приложений.

Использование среды выполнения контейнеров CRI-O

Стандартная процедура миграции, описанная ниже, требует OneAgent версии 1.281 или выше для кластеров Kubernetes, использующих CRI-O в качестве среды выполнения контейнеров, поэтому перед продолжением выполнения шагов ниже необходимо соответствующим образом обновить OneAgent.

Если это обновление выполнить невозможно, воспользуйтесь процедурой [Запуск CRI-O с OneAgent версии 1.279 или ранее](#running-crio) для альтернативного порядка миграции, а затем вернитесь к шагу 1 этой процедуры.

1. Рекомендуется

   Обновите установку с включённым CSI driver:

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
2. Перенастройте (существующий) DynaKube на режим мониторинга приложений:

   В следующем параллельном сравнении показано, как перенастроить DynaKube CR с классического full-stack на мониторинг приложений:

   Мониторинг классического full-stack

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

   Дополнительные сведения о настройке DynaKube для режима мониторинга приложений см. в [руководстве по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes") или в [параметрах DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Кроме того, можно загрузить [образец пользовательского ресурса DynaKube](https://dt-url.net/0w036dz) для мониторинга приложений из GitHub и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.
3. Примените пользовательский ресурс DynaKube:

   Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube. Валидирующий вебхук выдаст полезные сообщения об ошибках при наличии проблемы.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в классическом full-stack режиме и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого.
4. Дождитесь готовности code modules:

   Dynatrace Operator подхватывает изменения в пользовательском ресурсе DynaKube и обеспечивает доступность code modules на каждом узле.

   CSI driver генерирует события Kubernetes, привязанные к пользовательскому ресурсу DynaKube, когда code modules готовы и доступны на каждом узле. Дождитесь, пока событие будет зарегистрировано для каждого узла, прежде чем переходить к следующему шагу.
5. Перезапустите рабочие нагрузки приложений:

   Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы запустить внедрение code module и включить глубокий мониторинг, сводя к минимуму перерывы в мониторинге.

#### Запуск CRI-O с OneAgent версии 1.279 или ранее

В этом разделе описана процедура миграции для кластеров Kubernetes, использующих среду выполнения контейнеров CRI-O и работающих с OneAgent версии 279 или ранее.

Необходимо удалить хуки CRI-O, установленные и используемые для внедрения OneAgent в классическом full-stack режиме. Дополнительные сведения о хуках CRI-O см. в этой [записи блога Red Hat](https://dt-url.net/fq039v2).

Показать пошаговые инструкции

Следуйте этим инструкциям для успешной миграции с классического full-stack режима:

1. Удалите пользовательский ресурс DynaKube:

   Удалите DynaKube, настроенный в классическом full-stack режиме, выполнив следующую команду:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   Это действие приведёт к удалению OneAgent в классическом full-stack режиме и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого. Кроме того, если в пользовательском ресурсе DynaKube настроен мониторинг Kubernetes, мониторинг Kubernetes немедленно прекратится с удалением ActiveGate.
2. Дождитесь завершения работы подов OneAgent.
3. Следуйте инструкциям в разделе [Очистка узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Процедуры обновления и удаления Dynatrace Operator"), чтобы удалить хуки Dynatrace CRI-O со всех узлов Linux.
4. Продолжите с шага 1 [стандартной процедуры миграции](#migrate).

## Изменения в ресурсах Kubernetes

Миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима мониторинга приложений. Ключевые изменения включают:

| Компонент | классический full-stack | Мониторинг приложений |
| --- | --- | --- |
| Dynatrace Oneagent | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах * Внедряет code modules в поды приложений | * Отсутствует |
| Dynatrace Webhook Server | * Проверяет определения DynaKube | * Проверяет определения DynaKube * Внедряет code modules в поды приложений путём изменения определений подов |
| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание того, как работает развёртывание в Kubernetes.")  Необязательно | * Отсутствует | * Развёртывается как DaemonSet * Оптимизирует загрузку code modules для ускорения внедрения в поды и снижения потребления хранилища |