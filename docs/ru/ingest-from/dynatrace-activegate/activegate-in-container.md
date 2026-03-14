---
title: Контейнерный образ ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container
scraped: 2026-03-06T21:25:00.595701
---

# Контейнерный образ ActiveGate


* Последняя версия Dynatrace
* Чтение 2 мин
* Обновлено 9 мая 2025 г.

Dynatrace поддерживает запуск ActiveGate в контейнере. В качестве примера контейнерного развертывания на этой странице описывается, как развернуть контейнерный ActiveGate с помощью StatefulSet в Kubernetes/OpenShift.

## Предварительные требования

1. [Создайте токен доступа с областью действия `InstallerDownload`](../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.")
2. [Создайте токен аутентификации](activegate-security.md#generate-individual "Защитите ActiveGate с помощью выделенных токенов.")
3. Определите конечные точки связи ActiveGate и аутентификацию. Используйте API [GET информация о подключении для ActiveGate](../../dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity.md "Просмотрите информацию о подключении для ActiveGate через Dynatrace API.").
4. Получите UUID пространства имен kube-system
   Как извлечь UUID пространства имен kube-system

   Выполните приведенную ниже команду и сохраните UUID из вывода для дальнейшего использования.

   Kubernetes

   OpenShift

   ```
   kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

   ```
   oc get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

## Системные требования

Образ Dynatrace ActiveGate поддерживается на различных версиях Kubernetes и OpenShift. Полный список см. в разделе [Поддержка технологий - Kubernetes](../technology-support/support-model-and-issues.md "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы").

Образы доступны для следующих архитектур:

* x86-64
* ARM64 (AArch64)
* s390x
* PPC64le

## Реестры контейнеров

Для обеспечения бесшовной интеграции с вашими инструментами и адаптации к вашим потребностям мы предлагаем контейнерные образы различными способами для максимальной гибкости:

* [Встроенный реестр Dynatrace](../setup-on-k8s/guides/container-registries.md#default "Управление реестрами контейнеров в Dynatrace") по умолчанию
* [Публичные реестры](../setup-on-k8s/guides/container-registries/use-public-registry.md#supported-public-registries "Использование публичного реестра")
* [Собственный приватный реестр](../setup-on-k8s/guides/container-registries/prepare-private-registry.md "Хранение образов Dynatrace в приватных реестрах") Рекомендуется

Обратите внимание, что мультиархитектурные контейнерные образы Dynatrace, обеспечивающие совместимость с различными платформами, доступны только из [публичных реестров](../setup-on-k8s/guides/container-registries/use-public-registry.md#supported-public-registries "Использование публичного реестра"). Встроенный реестр Dynatrace предоставляет только образы для x86-64.

## Развертывание

Dynatrace предоставляет подписанные контейнерные образы для обеспечения подлинности и целостности, а также SBOM, содержащие список всех включенных программных компонентов.
Проверка подписей и просмотр SBOM позволяют эффективно управлять уязвимостями и снижать риски.
Подробности о проверке см. в разделе [Проверка аттестации Software Bill of Materials (SBOM)](../setup-on-k8s/guides/container-registries/verify-image-signature.md#sbom-attestation-verification "Проверка подписей образов Dynatrace").

Приватный или публичный реестр

Встроенный реестр Dynatrace

1. Создайте выделенное пространство имен.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Создайте секрет, содержащий данные аутентификации для сервера Dynatrace, используемого ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic dynatrace-tokens \


   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \


   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   ```
   oc -n dynatrace create secret generic dynatrace-tokens \


   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \


   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   Необходимо заменить

   * `<YOUR_TENANT_TOKEN>` значением `tenantToken`, полученным в разделе [Предварительные требования](#prereq) из информации о подключении.
   * `<YOUR_AUTH_TOKEN>` индивидуальным токеном ActiveGate, полученным в разделе [Предварительные требования](#prereq).
3. Создайте файл `ag-deployment-example.yaml` со следующим содержимым:

   ag-deployment-example.yaml

   ```
   apiVersion: v1


   kind: Service


   metadata:


   name: dynatrace-activegate


   namespace: dynatrace


   spec:


   type: ClusterIP


   selector:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   ports:


   - protocol: TCP


   port: 443


   targetPort: ag-https


   ---


   apiVersion: apps/v1


   kind: StatefulSet


   metadata:


   name: dynatrace-activegate


   namespace: dynatrace


   labels:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   spec:


   podManagementPolicy: Parallel


   serviceName: ""


   selector:


   matchLabels:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   template:


   metadata:


   labels:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   spec:


   affinity:


   nodeAffinity:


   requiredDuringSchedulingIgnoredDuringExecution:


   nodeSelectorTerms:


   - matchExpressions:


   - key: kubernetes.io/arch


   operator: In


   values:


   - <CPU_ARCHITECTURE>


   - key: kubernetes.io/os


   operator: In


   values:


   - linux


   containers:


   - name: activegate


   image: <REPOSITORY_URL>/dynatrace-activegate:<IMAGE_TAG>


   imagePullPolicy: Always


   ports:


   - containerPort: 9999


   name: ag-https


   protocol: TCP


   env:


   - name: DT_TENANT


   value: <YOUR_ENVIRONMENT_ID>


   - name: DT_SERVER


   value: <YOUR_COMMUNICATION_ENDPOINTS>


   - name: DT_ID_SEED_NAMESPACE


   value: dynatrace


   - name: DT_ID_SEED_K8S_CLUSTER_ID


   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>


   - name: DT_CAPABILITIES


   value: restInterface,kubernetes_monitoring,MSGrouter,metrics_ingest


   - name: DT_DEPLOYMENT_METADATA


   value: orchestration_tech=handcrated-ag-sts;script_version=none;orchestrator_id=none


   - name: DT_DNS_ENTRY_POINT


   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication


   volumeMounts:


   - name: dynatrace-tokens


   mountPath: /var/lib/dynatrace/secrets/tokens


   - name: truststore-volume


   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts


   readOnly: true


   subPath: k8s-local.jks


   - name: server-certs-storage


   mountPath: /var/lib/dynatrace/gateway/ssl


   - name: ag-lib-gateway-config


   mountPath: /var/lib/dynatrace/gateway/config


   - name: ag-lib-gateway-temp


   mountPath: /var/lib/dynatrace/gateway/temp


   - name: ag-lib-gateway-data


   mountPath: /var/lib/dynatrace/gateway/data


   - name: ag-log-gateway


   mountPath: /var/log/dynatrace/gateway


   - name: ag-tmp-gateway


   mountPath: /var/tmp/dynatrace/gateway


   livenessProbe:


   failureThreshold: 2


   httpGet:


   path: /rest/state


   port: ag-https


   scheme: HTTPS


   initialDelaySeconds: 30


   periodSeconds: 30


   successThreshold: 1


   timeoutSeconds: 1


   readinessProbe:


   failureThreshold: 3


   httpGet:


   path: /rest/health


   port: ag-https


   scheme: HTTPS


   initialDelaySeconds: 30


   periodSeconds: 15


   successThreshold: 1


   timeoutSeconds: 1


   resources:


   requests:


   cpu: 500m


   memory: 512Mi


   limits:


   cpu: 1000m


   memory: 1.5Gi


   securityContext:


   allowPrivilegeEscalation: false


   capabilities:


   drop:


   - all


   privileged: false


   readOnlyRootFilesystem: true


   runAsNonRoot: true


   seccompProfile:


   type: RuntimeDefault


   initContainers:


   - name: certificate-loader


   image: <REPOSITORY_URL>/dynatrace-activegate:<IMAGE_TAG>


   workingDir: /var/lib/dynatrace/gateway


   command: ['/bin/bash']


   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']


   volumeMounts:


   - mountPath: /var/lib/dynatrace/gateway/ssl


   name: truststore-volume


   volumes:


   - name: truststore-volume


   emptyDir: {}


   - name: dynatrace-tokens


   secret:


   secretName: dynatrace-tokens


   - name: server-certs-storage


   emptyDir: {}


   - name: ag-lib-gateway-config


   emptyDir: {}


   - name: ag-lib-gateway-temp


   emptyDir: {}


   - name: ag-lib-gateway-data


   emptyDir: {}


   - name: ag-log-gateway


   emptyDir: {}


   - name: ag-tmp-gateway


   emptyDir: {}


   updateStrategy:


   type: RollingUpdate
   ```
4. Измените YAML-файл развертывания.

   Добавьте данные конфигурации окружения в файл `ag-deployment-example.yaml`, обязательно заменив:

   * `CPU_ARCHITECTURE` на вашу архитектуру процессора. Допустимые значения: `amd64`, `arm64`, `s390x` и `ppcle64`
   * `<REPOSITORY_URL>` на один из [поддерживаемых реестров](../setup-on-k8s/guides/container-registries/use-public-registry.md#supported-public-registries "Использование публичного реестра")
   * `<IMAGE_TAG>` на правильный тег образа ([примеры](../setup-on-k8s/guides/container-registries/prepare-private-registry.md#image-tags "Хранение образов Dynatrace в приватных реестрах"))
   * `<YOUR_ENVIRONMENT_ID>` на идентификатор вашего окружения

     Для определения идентификатора окружения используйте следующий синтаксис:

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` значением `communicationEndpoints`, полученным в разделе [Предварительные требования](#prereq) из информации о подключении

     Список конечных точек связи сервера (`communicationEndpoints`) может изменяться со временем.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` UUID пространства имен kube-system, полученным в разделе [Предварительные требования](#prereq)

     Для архитектуры PPC64le требуется дополнительная настройка. Подробности см. в разделе [Контейнерный образ ActiveGate](activegate-in-container.md#additional-configuration "Развертывание контейнерного ActiveGate.").

   Опции:

   * Необязательно Включите AppArmor, если он доступен.

     Профиль AppArmor

     Для обеспечения совместимости с более широким спектром кластеров Kubernetes профиль AppArmor не указан в `ag-deployment-example.yaml`. Если AppArmor доступен в вашем кластере Kubernetes, мы рекомендуем дополнительно аннотировать StatefulSet профилем `runtime/default`.

     ```
     spec:


     template:


     metadata:


     annotations:


     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Необязательно Примените ограничения ресурсов в соответствии с рекомендациями по размерам.

     Рекомендации по размерам для мониторинга K8S и маршрутизации агентов

     В таблице ниже приведены рекомендуемые размеры CPU и памяти ActiveGate в зависимости от количества подов:

     | Количество подов | CPU | Память |
     | --- | --- | --- |
     | До 100 подов | 500 миллиядер (mCores) | 512 мебибайт (MiB) |
     | До 1 000 подов | 1 000 миллиядер (mCores) | 1 гибибайт (GiB) |
     | До 5 000 подов | 1 500 миллиядер (mCores) | 2 гибибайта (GiB) |
     | Более 5 000 подов | более 1 500 миллиядер (mCores)[1](#fn-1-1-def) | более 2 гибибайт (GiB)[1](#fn-1-1-def) |

     1

     Фактические значения зависят от вашего окружения.

     Эти ограничения следует рассматривать как руководство. Они предназначены для предотвращения замедления процесса запуска ActiveGate и чрезмерного использования ресурсов узла. Значения по умолчанию покрывают широкий спектр различных размеров кластеров; вы можете изменить их в соответствии с вашими потребностями на основе [метрик самодиагностики](../../analyze-explore-automate/metrics-classic/self-monitoring-metrics.md#activegate-insights "Изучите полный список метрик самодиагностики Dynatrace.") ActiveGate.

   Дополнительные параметры конфигурации см. в разделе [Конфигурация контейнерного ActiveGate](activegate-in-container/configuration.md "Узнайте, как настроить контейнерный ActiveGate.").
5. Разверните ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
6. Чтобы убедиться, что ActiveGate успешно подключился к серверу Dynatrace, перейдите в **Deployment Status** > **ActiveGates**.

1. Создайте выделенное пространство имен.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Создайте секрет, содержащий URL окружения и данные аутентификации для этого реестра.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret docker-registry dynatrace-docker-registry \


   --docker-server=<YOUR_ENVIRONMENT_URL> \


   --docker-username=<YOUR_ENVIRONMENT_ID> \


   --docker-password=<YOUR_INSTALLER_DOWNLOAD_TOKEN>
   ```

   ```
   oc -n dynatrace create secret docker-registry dynatrace-docker-registry \


   --docker-server=<YOUR_ENVIRONMENT_URL> \


   --docker-username=<YOUR_ENVIRONMENT_ID> \


   --docker-password=<YOUR_INSTALLER_DOWNLOAD_TOKEN> -n dynatrace
   ```

   Необходимо заменить

   * `<YOUR_ENVIRONMENT_URL>` URL вашего окружения (без `https://`). Пример: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` именем пользователя учетной записи Docker (совпадает с идентификатором в URL вашего окружения выше).

     Для определения идентификатора окружения используйте следующий синтаксис:

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_INSTALLER_DOWNLOAD_TOKEN>` токеном доступа с областью действия `InstallerDownload`, созданным в разделе [Предварительные требования](#prereq)
3. Создайте секрет, содержащий данные аутентификации для сервера Dynatrace, используемого ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic dynatrace-tokens \


   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \


   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   ```
   oc -n dynatrace create secret generic dynatrace-tokens \


   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \


   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```

   Необходимо заменить

   * `<YOUR_TENANT_TOKEN>` значением `tenantToken`, полученным в разделе [Предварительные требования](#prereq) из информации о подключении.
   * `<YOUR_AUTH_TOKEN>` индивидуальным токеном ActiveGate, полученным в разделе [Предварительные требования](#prereq).
4. Создайте файл `ag-deployment-example.yaml` со следующим содержимым:

   ag-deployment-example.yaml

   ```
   apiVersion: v1


   kind: Service


   metadata:


   name: dynatrace-activegate


   namespace: dynatrace


   spec:


   type: ClusterIP


   selector:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   ports:


   - protocol: TCP


   port: 443


   targetPort: ag-https


   ---


   apiVersion: apps/v1


   kind: StatefulSet


   metadata:


   name: dynatrace-activegate


   namespace: dynatrace


   labels:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   spec:


   podManagementPolicy: Parallel


   serviceName: ""


   selector:


   matchLabels:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   template:


   metadata:


   labels:


   app.kubernetes.io/component: activegate


   component.dynatrace.com/feature: activegate


   spec:


   affinity:


   nodeAffinity:


   requiredDuringSchedulingIgnoredDuringExecution:


   nodeSelectorTerms:


   - matchExpressions:


   - key: kubernetes.io/arch


   operator: In


   values:


   - amd64


   - key: kubernetes.io/os


   operator: In


   values:


   - linux


   containers:


   - name: activegate


   image: <YOUR_ENVIRONMENT_URL>/linux/activegate:raw


   imagePullPolicy: Always


   ports:


   - containerPort: 9999


   name: ag-https


   protocol: TCP


   env:


   - name: DT_TENANT


   value: <YOUR_ENVIRONMENT_ID>


   - name: DT_SERVER


   value: <YOUR_COMMUNICATION_ENDPOINTS>


   - name: DT_ID_SEED_NAMESPACE


   value: dynatrace


   - name: DT_ID_SEED_K8S_CLUSTER_ID


   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>


   - name: DT_CAPABILITIES


   value: restInterface,kubernetes_monitoring,MSGrouter,metrics_ingest


   - name: DT_DEPLOYMENT_METADATA


   value: orchestration_tech=handcrated-ag-sts;script_version=none;orchestrator_id=none


   - name: DT_DNS_ENTRY_POINT


   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication


   volumeMounts:


   - name: dynatrace-tokens


   mountPath: /var/lib/dynatrace/secrets/tokens


   - name: truststore-volume


   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts


   readOnly: true


   subPath: k8s-local.jks


   - name: server-certs-storage


   mountPath: /var/lib/dynatrace/gateway/ssl


   - name: ag-lib-gateway-config


   mountPath: /var/lib/dynatrace/gateway/config


   - name: ag-lib-gateway-temp


   mountPath: /var/lib/dynatrace/gateway/temp


   - name: ag-lib-gateway-data


   mountPath: /var/lib/dynatrace/gateway/data


   - name: ag-log-gateway


   mountPath: /var/log/dynatrace/gateway


   - name: ag-tmp-gateway


   mountPath: /var/tmp/dynatrace/gateway


   livenessProbe:


   failureThreshold: 2


   httpGet:


   path: /rest/state


   port: ag-https


   scheme: HTTPS


   initialDelaySeconds: 30


   periodSeconds: 30


   successThreshold: 1


   timeoutSeconds: 1


   readinessProbe:


   failureThreshold: 3


   httpGet:


   path: /rest/health


   port: ag-https


   scheme: HTTPS


   initialDelaySeconds: 30


   periodSeconds: 15


   successThreshold: 1


   timeoutSeconds: 1


   resources:


   requests:


   cpu: 500m


   memory: 512Mi


   limits:


   cpu: 1000m


   memory: 1.5Gi


   securityContext:


   allowPrivilegeEscalation: false


   capabilities:


   drop:


   - all


   privileged: false


   readOnlyRootFilesystem: true


   runAsNonRoot: true


   seccompProfile:


   type: RuntimeDefault


   initContainers:


   - name: certificate-loader


   image: <YOUR_ENVIRONMENT_URL>/linux/activegate:raw


   workingDir: /var/lib/dynatrace/gateway


   command: ['/bin/bash']


   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']


   volumeMounts:


   - mountPath: /var/lib/dynatrace/gateway/ssl


   name: truststore-volume


   imagePullSecrets:


   - name: dynatrace-docker-registry


   volumes:


   - name: truststore-volume


   emptyDir: {}


   - name: dynatrace-tokens


   secret:


   secretName: dynatrace-tokens


   - name: server-certs-storage


   emptyDir: {}


   - name: ag-lib-gateway-config


   emptyDir: {}


   - name: ag-lib-gateway-temp


   emptyDir: {}


   - name: ag-lib-gateway-data


   emptyDir: {}


   - name: ag-log-gateway


   emptyDir: {}


   - name: ag-tmp-gateway


   emptyDir: {}


   updateStrategy:


   type: RollingUpdate
   ```
5. Измените YAML-файл развертывания.

   Добавьте данные конфигурации окружения в файл `ag-deployment-example.yaml`, обязательно заменив:

   * `<YOUR_ENVIRONMENT_URL>` URL вашего окружения (без `https://`). Пример: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` именем пользователя учетной записи Docker (совпадает с идентификатором в URL вашего окружения выше)

     Для определения идентификатора окружения используйте следующий синтаксис:

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` значением `communicationEndpoints`, полученным в разделе [Предварительные требования](#prereq) из информации о подключении

     Список конечных точек связи сервера (`communicationEndpoints`) может изменяться со временем.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` UUID пространства имен kube-system, полученным в разделе [Предварительные требования](#prereq)

   Опции:

   * Необязательно Вы можете изменить версию образа, используя другой тег версии
     Версии

     + `raw` -- последний доступный образ
     + `1.sprint.patchlevel-raw` -- образ для определенной версии ActiveGate (например, `1.297.0-raw`)

   * Необязательно Включите AppArmor, если он доступен.

     Профиль AppArmor

     Для обеспечения совместимости с более широким спектром кластеров Kubernetes профиль AppArmor не указан в `ag-deployment-example.yaml`. Если AppArmor доступен в вашем кластере Kubernetes, мы рекомендуем дополнительно аннотировать StatefulSet профилем `runtime/default`.

     ```
     spec:


     template:


     metadata:


     annotations:


     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Необязательно Примените ограничения ресурсов в соответствии с рекомендациями по размерам.

     Рекомендации по размерам для мониторинга K8S и маршрутизации агентов

     В таблице ниже приведены рекомендуемые размеры CPU и памяти ActiveGate в зависимости от количества подов:

     | Количество подов | CPU | Память |
     | --- | --- | --- |
     | До 100 подов | 500 миллиядер (mCores) | 512 мебибайт (MiB) |
     | До 1 000 подов | 1 000 миллиядер (mCores) | 1 гибибайт (GiB) |
     | До 5 000 подов | 1 500 миллиядер (mCores) | 2 гибибайта (GiB) |
     | Более 5 000 подов | более 1 500 миллиядер (mCores)[1](#fn-2-1-def) | более 2 гибибайт (GiB)[1](#fn-2-1-def) |

     1

     Фактические значения зависят от вашего окружения.

     Эти ограничения следует рассматривать как руководство. Они предназначены для предотвращения замедления процесса запуска ActiveGate и чрезмерного использования ресурсов узла. Значения по умолчанию покрывают широкий спектр различных размеров кластеров; вы можете изменить их в соответствии с вашими потребностями на основе [метрик самодиагностики](../../analyze-explore-automate/metrics-classic/self-monitoring-metrics.md#activegate-insights "Изучите полный список метрик самодиагностики Dynatrace.") ActiveGate.

   Дополнительные параметры конфигурации см. в разделе [Конфигурация контейнерного ActiveGate](activegate-in-container/configuration.md "Узнайте, как настроить контейнерный ActiveGate.").
6. Разверните ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
7. Чтобы убедиться, что ActiveGate успешно подключился к серверу Dynatrace, перейдите в **Deployment Status** > **ActiveGates**.

### Дополнительная настройка для архитектуры PPC64le

Для завершения настройки контейнерного ActiveGate на архитектуре PPC64le необходимо выполнить еще два шага:

1. Увеличьте количество ядер CPU: чтобы соответствовать производительности архитектуры x86-64, количество ядер CPU следует увеличить в четыре раза.
2. Уменьшите количество потоков ActiveGate:

   * Создайте пользовательские свойства, как описано в разделе [Расширенная конфигурация](activegate-in-container/configuration.md#advanced-configuration "Узнайте, как настроить контейнерный ActiveGate.")
   * Добавьте следующие строки в custom.properties:

     ```
     [com.compuware.apm.webserver]


     threadpool-max-size=30


     async-worker-pool-coresize=60
     ```

Для достижения лучшей производительности мы настоятельно рекомендуем выполнить описанные выше шаги.

## Специализированные развертывания

* Для мониторинга Kubernetes/OpenShift выберите один из следующих вариантов:

  + Используйте [Dynatrace Operator](../setup-on-k8s/deployment.md "Развертывание Dynatrace Operator в Kubernetes")
  + Разверните [ActiveGate непосредственно как StatefulSet](../setup-on-k8s/deployment/other/ag-statefulset.md "Установка и настройка ActiveGate в Kubernetes как StatefulSet.")
* Для сбора логов из Kubernetes используйте [Log Monitoring](../../analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes.md "Dynatrace поддерживает сбор данных логов из систем оркестрации контейнеров Kubernetes через модуль логов OneAgent или модуль логов Kubernetes.").

## Образы, совместимые с FIPS

ActiveGate версии 1.315+

Доступен специальный образ ActiveGate, совместимый с FIPS. См. [Совместимость ActiveGate с FIPS](activegate-fips-compliance.md "Узнайте о совместимости ActiveGate с FIPS") для получения информации о требованиях, ограничениях, где получить образ и как проверить развертывание.
