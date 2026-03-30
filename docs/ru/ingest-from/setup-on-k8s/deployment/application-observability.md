---
title: Начало работы с мониторингом платформы Kubernetes + наблюдаемость приложений
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/application-observability
scraped: 2026-03-06T21:37:25.245616
---

На этой странице приведены инструкции по развёртыванию Dynatrace Operator для включения мониторинга платформы Kubernetes и наблюдаемости приложений. Эта конфигурация идеально подходит для мониторинга сред Kubernetes и контейнеризированных приложений.

## Сценарии использования

* Оценка и устранение неполадок в кластере и рабочих нагрузках Kubernetes
* Оптимизация использования ресурсов рабочих нагрузок Kubernetes
* Получение оповещений и событий для обнаружения аномалий кластера и реагирования на них
* Изучение метрик, событий и логов ваших подов и узлов в едином интерфейсе
* Устранение типичных проблем со здоровьем рабочих нагрузок Kubernetes
* Автоматическая распределённая трассировка между контейнерами
* Инсайты на уровне кода и сервисов в контейнерах приложений
* Профилирование и анализ потоков

Если вы хотите получить полное представление о вашей среде Kubernetes, ознакомьтесь с обзором развёртывания, чтобы узнать о полной наблюдаемости Full-Stack. Вы можете расширить наблюдаемость Kubernetes за счёт аналитики логов, цифрового опыта и безопасности приложений.

Предварительные требования

### Перед началом работы

Перед установкой Dynatrace в кластере Kubernetes убедитесь, что выполнены следующие требования:

* Ваш CLI `kubectl` подключён к кластеру Kubernetes, который вы хотите мониторить.
* У вас достаточно привилегий в отслеживаемом кластере для выполнения команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL вашей среды Dynatrace.
* Для OpenShift Dedicated необходима [роль cluster-admin](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка через Helm: используйте [Helm версии 3](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые версии платформ и дистрибутивы Kubernetes/OpenShift.

Настройка SCC требуется для OpenShift при развёртывании `cloudNativeFullStack` и `applicationMonitoring` с CSI-драйвером Dynatrace Operator.

Комбинация `hostMonitoring` и `applicationMonitoring` в кластере Kubernetes в одной среде не поддерживается.

## Варианты установки

Выберите **один из методов установки**, который лучше всего соответствует вашим потребностям.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Манифест**](#manifest)

## Helm

Dynatrace Operator версии 0.8.0+

Новые инструкции по установке и обновлению через Helm используют Helm-чарт, доступный из реестра OCI. Поэтому, если репозиторий Dynatrace в настоящее время добавлен в ваши локальные репозитории Helm, его можно безопасно удалить.

```
helm repo remove dynatrace
```

Процесс установки не зависит от того, используете ли вы Kubernetes или OpenShift. Платформа определяется автоматически во время установки.

1. Установите Dynatrace Operator

   При использовании Helm версии 4.0+ необходимо использовать `--rollback-on-failure` вместо флага `--atomic`.

   У вас есть два варианта:

   Установка по умолчанию / установка из реестра OCI

   Следующая команда работает как для стандартной установки, так и для установки с использованием реестра OCI.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \


   --create-namespace \


   --namespace dynatrace \


   --atomic
   ```

   Установка с дополнительной конфигурацией Helm-чарта

   Отредактируйте пример [`values.yaml`](https://github.com/Dynatrace/dynatrace-operator/blob/v1.8.1/config/helm/chart/default/values.yaml) из GitHub, а затем выполните команду установки, передав YAML-файл в качестве аргумента:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \


   --create-namespace \


   --namespace dynatrace \


   --atomic \


   -f values.yaml
   ```

   Если `installCRD` установлен в `false`, необходимо создать определение пользовательского ресурса вручную перед началом установки через Helm:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют дополнительной конфигурации.
2. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе Необходимые токены и разрешения.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Создайте YAML-файл пользовательского ресурса DynaKube.

   Пример пользовательского ресурса DynaKube для мониторинга приложений

   Вы можете просмотреть доступные параметры или руководства и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: dynakube


   namespace: dynatrace


   annotations:


   feature.dynatrace.com/k8s-app-enabled: "true"


   feature.dynatrace.com/injection-readonly-volume: "true"


   spec:


   # For detailed instructions on DynaKube parameters in the spec section, visit https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters


   # Dynatrace apiUrl including the /api path at the end.


   # Replace 'ENVIRONMENTID' with your environment ID.


   # For instructions on how to determine the environment ID and how to configure the apiUrl address, see https://www.dynatrace.com/support/help/reference/dynatrace-concepts/environment-id/.


   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api


   metadataEnrichment:


   enabled: true


   oneAgent:


   applicationMonitoring: {}


   activeGate:


   capabilities:


   - routing


   - kubernetes-monitoring


   resources:


   requests:


   cpu: 500m


   memory: 512Mi


   limits:


   cpu: 1000m


   memory: 1.5Gi
   ```
4. Необязательно: мониторинг потенциально конфиденциальных данных

   Для мониторинга потенциально конфиденциальных данных, таких как Secrets (значения маскируются перед приёмом) и ConfigMaps, необходимо создать ClusterRole, разрешающую доступ к этим ресурсам. Добавьте следующий фрагмент в конец вашего YAML-файла пользовательского ресурса DynaKube.

   Установка с мониторингом конфиденциальных данных

   ```
   ---


   apiVersion: rbac.authorization.k8s.io/v1


   kind: ClusterRole


   metadata:


   labels:


   rbac.dynatrace.com/aggregate-to-monitoring: "true"


   name: dynatrace-kubernetes-monitoring-sensitive


   rules:


   - apiGroups:


   - ""


   resources:


   - configmaps


   - secrets


   verbs:


   - list


   - watch


   - get
   ```

   Роль будет автоматически привязана к ClusterRole `dynatrace-kubernetes-monitoring` через правила агрегации. Для получения дополнительной информации об агрегации ClusterRole см. документацию по агрегации ClusterRole.
5. Примените пользовательский ресурс DynaKube

   Выполните приведённую ниже команду для применения пользовательского ресурса DynaKube, убедившись, что вы заменили `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Валидационный вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
6. Необязательно: проверка развёртывания

   Убедитесь, что ваш DynaKube работает и все поды в пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace


   NAME         APIURL                                          STATUS     AGE


   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI-драйвером вы должны увидеть следующие поды:

   ```
   > kubectl get pods -n dynatrace


   NAME                                  READY   STATUS    RESTARTS        AGE


   dynakube-activegate-0                 1/1     Running   0               50s


   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s


   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s


   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s


   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s


   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s


   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI-драйвер не является обязательным (см. шаг 2). При включении он развёртывается как DaemonSet, что приводит к созданию пода CSI-драйвера на каждом узле.

## Манифест

Kubernetes

OpenShift

1. Создайте пространство имён `dynatrace`

   ```
   kubectl create namespace dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes-csi.yaml
   ```

   Без CSI-драйвера

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют дополнительной конфигурации.

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе Необходимые токены и разрешения.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Создайте YAML-файл пользовательского ресурса DynaKube.

   Пример пользовательского ресурса DynaKube для мониторинга приложений

   Вы можете просмотреть доступные параметры или руководства и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: dynakube


   namespace: dynatrace


   annotations:


   feature.dynatrace.com/k8s-app-enabled: "true"


   feature.dynatrace.com/injection-readonly-volume: "true"


   spec:


   # For detailed instructions on DynaKube parameters in the spec section, visit https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters


   # Dynatrace apiUrl including the /api path at the end.


   # Replace 'ENVIRONMENTID' with your environment ID.


   # For instructions on how to determine the environment ID and how to configure the apiUrl address, see https://www.dynatrace.com/support/help/reference/dynatrace-concepts/environment-id/.


   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api


   metadataEnrichment:


   enabled: true


   oneAgent:


   applicationMonitoring: {}


   activeGate:


   capabilities:


   - routing


   - kubernetes-monitoring


   resources:


   requests:


   cpu: 500m


   memory: 512Mi


   limits:


   cpu: 1000m


   memory: 1.5Gi
   ```
5. Необязательно: мониторинг потенциально конфиденциальных данных

   Для мониторинга потенциально конфиденциальных данных, таких как Secrets (значения маскируются перед приёмом) и ConfigMaps, необходимо создать ClusterRole, разрешающую доступ к этим ресурсам. Добавьте следующий фрагмент в конец вашего YAML-файла пользовательского ресурса DynaKube.

   Установка с мониторингом конфиденциальных данных

   ```
   ---


   apiVersion: rbac.authorization.k8s.io/v1


   kind: ClusterRole


   metadata:


   labels:


   rbac.dynatrace.com/aggregate-to-monitoring: "true"


   name: dynatrace-kubernetes-monitoring-sensitive


   rules:


   - apiGroups:


   - ""


   resources:


   - configmaps


   - secrets


   verbs:


   - list


   - watch


   - get
   ```

   Роль будет автоматически привязана к ClusterRole `dynatrace-kubernetes-monitoring` через правила агрегации. Для получения дополнительной информации об агрегации ClusterRole см. документацию по агрегации ClusterRole.
6. Примените пользовательский ресурс DynaKube

   Выполните приведённую ниже команду для применения пользовательского ресурса DynaKube, убедившись, что вы заменили `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Валидационный вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
7. Необязательно: проверка развёртывания

   Убедитесь, что ваш DynaKube работает и все поды в пространстве имён Dynatrace запущены и готовы.

   ```
   > kubectl get dynakube -n dynatrace


   NAME         APIURL                                          STATUS     AGE


   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI-драйвером вы должны увидеть следующие поды:

   ```
   > kubectl get pods -n dynatrace


   NAME                                  READY   STATUS    RESTARTS        AGE


   dynakube-activegate-0                 1/1     Running   0               50s


   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s


   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s


   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s


   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s


   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s


   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI-драйвер не является обязательным (см. шаг 2). При включении он развёртывается как DaemonSet, что приводит к созданию пода CSI-драйвера на каждом узле.

1. Добавьте проект `dynatrace`

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Установите Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/openshift-csi.yaml
   ```

   Без CSI-драйвера

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/openshift.yaml
   ```

   Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace Operator завершат инициализацию:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Создайте секрет для токенов доступа

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе Необходимые токены и разрешения.

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Создайте YAML-файл пользовательского ресурса DynaKube.

   Пример пользовательского ресурса DynaKube для мониторинга приложений

   Вы можете просмотреть доступные параметры или руководства и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.

   ```
   apiVersion: dynatrace.com/v1beta5


   kind: DynaKube


   metadata:


   name: dynakube


   namespace: dynatrace


   annotations:


   feature.dynatrace.com/k8s-app-enabled: "true"


   feature.dynatrace.com/injection-readonly-volume: "true"


   spec:


   # For detailed instructions on DynaKube parameters in the spec section, visit https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters


   # Dynatrace apiUrl including the /api path at the end.


   # Replace 'ENVIRONMENTID' with your environment ID.


   # For instructions on how to determine the environment ID and how to configure the apiUrl address, see https://www.dynatrace.com/support/help/reference/dynatrace-concepts/environment-id/.


   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api


   metadataEnrichment:


   enabled: true


   oneAgent:


   applicationMonitoring: {}


   activeGate:


   capabilities:


   - routing


   - kubernetes-monitoring


   resources:


   requests:


   cpu: 500m


   memory: 512Mi


   limits:


   cpu: 1000m


   memory: 1.5Gi
   ```
5. Необязательно: мониторинг потенциально конфиденциальных данных

   Для мониторинга потенциально конфиденциальных данных, таких как Secrets (значения маскируются перед приёмом) и ConfigMaps, необходимо создать ClusterRole, разрешающую доступ к этим ресурсам. Добавьте следующий фрагмент в конец вашего YAML-файла пользовательского ресурса DynaKube.

   Установка с мониторингом конфиденциальных данных

   ```
   ---


   apiVersion: rbac.authorization.k8s.io/v1


   kind: ClusterRole


   metadata:


   labels:


   rbac.dynatrace.com/aggregate-to-monitoring: "true"


   name: dynatrace-kubernetes-monitoring-sensitive


   rules:


   - apiGroups:


   - ""


   resources:


   - configmaps


   - secrets


   verbs:


   - list


   - watch


   - get
   ```

   Роль будет автоматически привязана к ClusterRole `dynatrace-kubernetes-monitoring` через правила агрегации. Для получения дополнительной информации об агрегации ClusterRole см. документацию по агрегации ClusterRole.
6. Примените пользовательский ресурс DynaKube
   Выполните приведённую ниже команду для применения пользовательского ресурса DynaKube, убедившись, что вы заменили `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Валидационный вебхук предоставит полезные сообщения об ошибках, если возникнет проблема.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
7. Необязательно: проверка развёртывания

   Убедитесь, что ваш DynaKube работает и все поды в пространстве имён Dynatrace запущены и готовы.

   ```
   > oc get dynakube -n dynatrace


   NAME         APIURL                                          STATUS     AGE


   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   В конфигурации DynaKube по умолчанию с CSI-драйвером вы должны увидеть следующие поды:

   ```
   > oc get pods -n dynatrace


   NAME                                  READY   STATUS    RESTARTS        AGE


   dynakube-activegate-0                 1/1     Running   0               50s


   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s


   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s


   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s


   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s


   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s


   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI-драйвер не является обязательным (см. шаг 2). При включении он развёртывается как DaemonSet, что приводит к созданию пода CSI-драйвера на каждом узле.

## Лицензирование

Мониторинг платформы Kubernetes + наблюдаемость приложений требует подписку Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace."). Мониторинг платформы Kubernetes лицензируется по количеству подов в час (под-часы), а наблюдаемость приложений — по сумме памяти контейнеров ([ГиБ-часы](../../../license/capabilities/app-infra-observability/full-stack-monitoring.md#gib-hour "Узнайте, как рассчитывается потребление возможности Full-Stack Monitoring DPS.")).

## Дополнительные материалы

После успешной установки Dynatrace Operator следующие ресурсы могут быть полезны для дальнейшего изучения и устранения неполадок.

### Получение практических ответов

Начните анализировать свои кластеры Kubernetes и контейнеризированные приложения с Dynatrace и получайте практические ответы.### Руководства

Узнайте, как настроить Dynatrace Operator для поддержки конкретных сценариев использования.### Устранение неполадок

Устранение проблем, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами.

### Как это работает

Хотите узнать больше о компонентах Dynatrace в вашем кластере Kubernetes?### Справочник

Справочник по API и параметры конфигурации для всех компонентов Dynatrace в вашем кластере Kubernetes.### Примечания к выпуску Dynatrace Operator

Примечания к выпуску Dynatrace Operator.### Обновление или удаление

На этой странице приведены подробные инструкции по обновлению и удалению Dynatrace Operator.### Руководство по размеру Dynatrace ActiveGate

Руководство по выбору размера для компонентов Dynatrace ActiveGate

## Связанные темы

* Kubernetes Classic
