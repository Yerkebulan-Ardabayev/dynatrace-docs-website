---
title: Контейнеризованные автомасштабируемые частные расположения Synthetic на Kubernetes
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations
scraped: 2026-05-12T11:32:00.213007
---

# Контейнеризованные автомасштабируемые частные расположения Synthetic на Kubernetes

# Контейнеризованные автомасштабируемые частные расположения Synthetic на Kubernetes

* How-to guide
* 26-min read
* Updated on May 04, 2026

Dynatrace версии 1.264+

**Контейнеризованные автомасштабируемые частные расположения Synthetic на Kubernetes и его коммерческом дистрибутиве OpenShift** являются альтернативой развёртыванию Synthetic-enabled ActiveGate на отдельных хостах или виртуальных машинах с последующим назначением их в частные расположения для выполнения синтетических мониторов.

В отличие от отдельных Synthetic-enabled ActiveGate, которые разворачиваются и назначаются в частные расположения (и затем отслеживаются по метрикам использования), **контейнеризованные расположения разворачиваются целиком** с минимальным и максимальным количеством ActiveGate в качестве обязательных входных параметров.

Kubernetes и OpenShift — это не просто дополнительные поддерживаемые платформы для ActiveGate наряду с Windows и Linux; в рамках этого предложения контейнеризованные частные расположения Synthetic:

* Автомасштабируются (на основе метрик использования и заданного максимального/минимального количества ActiveGate).

* Просты в управлении и обслуживании.
* Поддерживают синтетический мониторинг облачно-нативных решений, требующих контейнерной разработки приложений.
* Могут быть развёрнуты быстрее при минимальных простоях.
* Автоматически отслеживаются по использованию ресурсов как часть операций автомасштабирования.

Управлять расположениями Kubernetes/OpenShift можно через веб-интерфейс Dynatrace и существующий [API v2 Synthetic - Locations, nodes, and configuration](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление расположениями Synthetic через Synthetic v2 API."). Дополнительные ранних эндпоинтов Early Access в этом API упрощают развёртывание расположений Kubernetes: новые эндпоинты помогают генерировать команды для выполнения на кластере Kubernetes.

На контейнеризованных расположениях можно выполнять как запланированные, так и [по запросу](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Выполнение синтетических мониторов по запросу из публичных или частных расположений.") все [типы синтетических мониторов](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.").

## Архитектура

Контейнеризованные частные расположения Synthetic разворачиваются целиком.

* Каждое расположение имеет несколько Synthetic-enabled **ActiveGate**, настроенных как **поды**. Вы указываете минимальное и максимальное количество ActiveGate при [настройке расположения](#initial-setup).
* **StatefulSet** считается **расположением**.

  В одном пространстве имён может быть одно или несколько расположений. См. разделы [Требования](#requirements) и [Рекомендации и предостережения](#recommend) ниже.

  В одном кластере Kubernetes может быть одно или несколько автомасштабируемых расположений.

Расположения масштабируются автоматически путём изменения количества ActiveGate на расположение следующими дополнительными компонентами архитектуры контейнеризованного расположения.

* **Synthetic metric adapter** запрашивает и получает [метрики использования](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#location-details "Анализ и управление использованием ресурсов в частных расположениях Synthetic.") для контейнеризованных ActiveGate от Dynatrace Cluster.

  На один кластер Kubernetes приходится один Synthetic metric adapter.

  Metric adapter настроен для взаимодействия с единственной средой Dynatrace.

  Установка Synthetic metric adapter требует [роли суперпользователя в Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles): см. раздел [Установка контейнеризованного расположения](#install) ниже.
* **Horizontal pod auto-scaler** масштабирует расположение, изменяя количество ActiveGate на основе данных об использовании, получаемых от Synthetic metric adapter.

  На одно расположение приходится один horizontal pod auto-scaler.

![Containerized locations for Synthetic Monitoring](https://cdn.bfldr.com/B686QPH3/as/skwmcbgm4knw3kshcxp34gq/Containerized_locations_for_synthetic_monitoring_-_Light_Mode?auto=webp&format=png&position=1)

Контейнеризованные расположения для синтетического мониторинга

## Требования

Контейнеризованные частные расположения Synthetic поддерживаются с Dynatrace версии 1.264+ на Kubernetes 1.22-1.25 с поддержкой постоянных томов и `kubectl`.

* Поддержка Kubernetes 1.26+ доступна в [рабочем процессе установки](#install).
* Поддерживаются все виды реализаций Kubernetes, как облачных, так и локальных (например, Amazon EKS или Minikube).
* Поддерживаются версии OpenShift, совместимые с поддерживаемыми версиями Kubernetes.

Для доступа к публичным репозиториям, где находятся Docker-образы для Synthetic-enabled ActiveGate и Synthetic metric adapter, требуется подключение к интернету. Расположения этих образов указаны в соответствующих файлах шаблонов: см. разделы [Установка контейнеризованного расположения](#install) и [Обновление контейнеризованного расположения](#update) ниже.

### Руководство по подбору размера

Ниже приведены **требования к оборудованию ActiveGate** по размерам.

* CPU и RAM requests — это ресурсы, зарезервированные подами при создании.
* CPU и RAM limits — максимальное потребление ресурсов на один под.
* Если расположение мониторируется с помощью [OneAgent](/managed/ingest-from/dynatrace-oneagent/oa-requirements "Требования к модулю кода OneAgent") или другого решения глубокого мониторинга, требования к памяти возрастут.
* Безбраузерный под в режиме FIPS имеет те же требования, что и обычный безбраузерный под.

Узел XS

Узел S

Узел M

|  | Под с поддержкой браузера | Безбраузерный под | Под с поддержкой браузера в режиме FIPS | Под с поддержкой браузера в режиме FIPS с корпоративным прокси |  | ActiveGate | Synthetic Engine | Browser worker | FIPS proxy | FIPS peer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Контейнеры | 4 | 2 | 5 | 6 |  | 1 | 1 | 2 | 1 | 1 |
| CPU requests | 1.4 vCPU | 0.4 vCPU | 1.9 vCPU | 2.05 vCPU |  | 0.3 vCPU | 0.25 vCPU | 2 × 0.5 vCPU | 0.5 vCPU | 0.15 vCPU |
| CPU limits | 3.8 vCPU | 0.8 vCPU | 5.3 vCPU | 5.6 vCPU |  | 0.3 vCPU | 0.5 vCPU | 2 × 1.5 vCPU | 1.5 vCPU | 0.3 vCPU |
| RAM requests | 3.25 GiB | 1.25 GiB | 3.5 GiB | 3.75 GiB |  | 0.25 GiB | 1 GiB | 2 × 1 GiB | 0.25 GiB | 0.25 GiB |
| RAM limits | 7 GiB | 3 GiB | 7.5 GiB | 8 GiB |  | 1 GiB | 2 GiB | 2 × 2 GiB | 0.5 GiB | 0.5 GiB |
| Эфемерное хранилище | 1.5 GiB | 1.3 GiB | 1.6 GiB | 1.7 GiB |  | 1.2 GiB | 0.1 GiB | 2 × 0.1 GiB | 0.1 GiB | 0.1 GiB |
| Постоянное хранилище | 3 GiB | 3 GiB | 3 GiB | 3 GiB |  |  |  |  |  |  |
| RAM-диск | 1 GiB | - | 1 GiB | 1 GiB |  |  |  |  |  |  |

|  | Под с поддержкой браузера | Безбраузерный под | Под с поддержкой браузера в режиме FIPS | Под с поддержкой браузера в режиме FIPS с корпоративным прокси |  | ActiveGate | Synthetic Engine | Browser worker | FIPS proxy | FIPS peer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Контейнеры | 6 | 2 | 7 | 8 |  | 1 | 1 | 4 | 1 | 1 |
| CPU requests | 2.65 vCPU | 0.65 vCPU | 3.15 vCPU | 3.3 vCPU |  | 0.3 vCPU | 0.5 vCPU | 4 × 0.5 vCPU | 0.5 vCPU | 0.15 vCPU |
| CPU limits | 7.3 vCPU | 1.3 vCPU | 8.8 vCPU | 9.1 vCPU |  | 0.3 vCPU | 1 vCPU | 4 × 1.5 vCPU | 1.5 vCPU | 0.3 vCPU |
| RAM requests | 5.75 GiB | 1.75 GiB | 6 GiB | 6.25 GiB |  | 0.25 GiB | 1.5 GiB | 4 × 1 GiB | 0.25 GiB | 0.25 GiB |
| RAM limits | 12 GiB | 4 GiB | 12.5 GiB | 13 GiB |  | 1 GiB | 3 GiB | 4 × 2 GiB | 0.5 GiB | 0.5 GiB |
| Эфемерное хранилище | 1.7 GiB | 1.3 GiB | 1.8 GiB | 1.9 GiB |  | 1.2 GiB | 0.1 GiB | 4 × 0.1 GiB | 0.1 GiB | 0.1 GiB |
| Постоянное хранилище | 6 GiB | 6 GiB | 6 GiB | 6 GiB |  |  |  |  |  |  |
| RAM-диск | 2 GiB | - | 2 GiB | 2 GiB |  |  |  |  |  |  |

|  | Под с поддержкой браузера | Безбраузерный под | Под с поддержкой браузера в режиме FIPS | Под с поддержкой браузера в режиме FIPS с корпоративным прокси |  | ActiveGate | Synthetic Engine | Browser worker | FIPS proxy | FIPS peer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Контейнеры | 14 | 2 | 15 | 16 |  | 1 | 1 | 12 | 1 | 1 |
| CPU requests | 7.15 vCPU | 1.15 vCPU | 7.65 vCPU | 7.8 vCPU |  | 0.3 vCPU | 1 vCPU | 12 × 0.5 vCPU | 0.5 vCPU | 0.15 vCPU |
| CPU limits | 20.3 vCPU | 2.3 vCPU | 21.8 vCPU | 22.1 vCPU |  | 0.3 vCPU | 2 vCPU | 12 × 1.5 vCPU | 1.5 vCPU | 0.3 vCPU |
| RAM requests | 14.25 GiB | 2.25 GiB | 14.5 GiB | 14.75 GiB |  | 0.25 GiB | 2 GiB | 12 × 1 GiB | 0.25 GiB | 0.25 GiB |
| RAM limits | 29 GiB | 5 GiB | 29.5 GiB | 30 GiB |  | 1 GiB | 4 GiB | 12 × 2 GiB | 0.5 GiB | 0.5 GiB |
| Эфемерное хранилище | 2.5 GiB | 1.3 GiB | 2.6 GiB | 2.7 GiB |  | 1.2 GiB | 0.1 GiB | 12 × 0.1 GiB | 0.1 GiB | 0.1 GiB |
| Постоянное хранилище | 12 GiB | 12 GiB | 12 GiB | 12 GiB |  |  |  |  |  |  |
| RAM-диск | 4 GiB | - | 4 GiB | 4 GiB |  |  |  |  |  |  |

### Рекомендации и предостережения

#### ActiveGate

* Рекомендуется использовать размер ActiveGate **S** и минимум два ActiveGate на расположение.
* При выборе размера узла учитывайте возможные ограничения, специфичные для используемого сервиса Kubernetes.
* Все ActiveGate в рамках одного расположения всегда одного размера.
* После задания размер ActiveGate для расположения нельзя изменить, поскольку постоянное хранилище не поддерживает изменение размера.
* Расположения Kubernetes подчиняются тем же правилам, что и другие расположения: ActiveGate нельзя добавить одновременно в несколько расположений.
* Нельзя смешивать контейнеризованные и неконтейнеризованные ActiveGate в одном расположении.
* Образ для Synthetic-enabled ActiveGate находится в публичном реестре; расположение этого образа указано в файле шаблона.

#### Расположения

* Рекомендуется устанавливать каждое расположение в собственном пространстве имён.
* При развёртывании более одного расположения в одном пространстве имён используйте разные имена для соответствующих ресурсов ActiveGate: см. раздел [Установка контейнеризованного расположения](#install) ниже.
* Расположения, совместно использующие одно пространство имён Kubernetes, должны быть подключены к той же среде Dynatrace, что и Synthetic metric adapter, для возможности автомасштабирования. Например, предположим, что расположение A и metric adapter настроены для среды X. Однако расположение A разделяет пространство имён с расположением B, настроенным для среды Y. В этом случае расположение A является автомасштабируемым, расположение B — нет.
* Если вы хотите установить расположение в одном пространстве имён с другими ресурсами Dynatrace, например [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "Установка ограничений ресурсов для компонентов Dynatrace Operator."), учтите более высокие [требования к оборудованию и системе](#requirements) для контейнеризованных Synthetic-enabled ActiveGate.

#### Synthetic metric adapter

* Рекомендуется развёртывать Synthetic metric adapter в собственном пространстве имён на кластер Kubernetes. Metric adapter может разделять пространство имён с расположением. Однако развёртывание metric adapter в собственном пространстве имён гарантирует, что он не будет удалён при удалении расположения.
* Metric adapter может взаимодействовать только с одной средой Dynatrace, поэтому автомасштабирование расположений работает только для этой среды.
* Образ для Synthetic metric adapter находится в публичном реестре; расположение этого образа указано в файле шаблона.

### Особенности автомасштабирования

Для автомасштабирования Synthetic metric adapter нуждается в доступе к Kubernetes API и расширяет его, определяя новый API-сервис: `v1beta1.external.metrics.k8s.io`.

Этот API-сервис определён в шаблоне Synthetic metric adapter: см. раздел [Установка и развёртывание контейнеризованного расположения](#install) ниже.

Определение API-сервиса в шаблоне metric adapter

```
apiVersion: apiregistration.k8s.io/v1



kind: APIService



metadata:



name: v1beta1.external.metrics.k8s.io



spec:



service:



name: dynatrace-metrics-apiserver



namespace: {{adapterNamespace}}



group: external.metrics.k8s.io



version: v1beta1



insecureSkipTLSVerify: true



groupPriorityMinimum: 100



versionPriority: 100
```

Synthetic metric adapter также изменяет существующий ресурс в своём шаблоне: ServiceAccount `horizontal-pod-autoscaler` в пространстве имён `kube-system`.

Изменение существующего ресурса в шаблоне metric adapter

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: hpa-controller-dynatrace-metrics



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: dynatrace-metrics-server-resources



subjects:



- kind: ServiceAccount



name: horizontal-pod-autoscaler



namespace: kube-system
```

#### Ограничения

Обратите внимание, что в кластере Kubernetes допускается только один внешний сервер метрик. Поэтому другие компоненты, выступающие в роли сервера метрик (например, дополнение KEDA или адаптер Prometheus), не могут использоваться совместно с Synthetic metric adapter.

## Установка контейнеризованного расположения

Установить контейнеризованное расположение можно только в предыдущем Dynatrace. В последней версии Dynatrace контейнеризованные расположения доступны только в режиме просмотра.

Настраивайте контейнеризованными расположениями в веб-интерфейсе Dynatrace: **Settings** > **Web and Mobile monitoring** > **Private Synthetic locations**.

### 1. Начальная настройка расположения Kubernetes/OpenShift

1. Выберите **Add Kubernetes location** или **Add OpenShift location** на странице **Private Synthetic locations**.
2. Введите **Location name** по вашему выбору.
3. Выберите **Geographic location**, например `San Francisco, California, United States`. (Обратите внимание, что нельзя **Save changes** до ввода имени и расположения.)
4. В разделе **ActiveGates**:

   1. Укажите **Minimum** и **Maximum number of ActiveGates** для вашего расположения. Эти настройки являются параметрами автомасштабирования, используемыми [horizontal pod auto-scaler](#architecture).
   2. Выберите **Node size** для ActiveGate (`XS`, `S` или `M`). См. также [Требования](#requirements) и [Рекомендации и предостережения](#recommend).
   3. **Deployment platform** предварительно выбрана в зависимости от вашего выбора Kubernetes или OpenShift.
5. Только Kubernetes. Если ваша реализация Kubernetes основана на версии выше 1.21-1.25, включите **Use Kubernetes version 1.26+**. См. также [Требования](#requirements) и [Рекомендации и предостережения](#recommend).

   Если вы измените этот параметр после скачивания шаблона расположения, необходимо повторить процедуру развёртывания.
6. Опционально. Вы можете отключить поддержку браузерных мониторов. В этом случае узел ActiveGate будет работать в [безбраузерном режиме](#browserless).
7. Опционально. Включите [генерацию проблем при отключении всех ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#outage-handling "Анализ и управление использованием ресурсов в частных расположениях Synthetic.").
8. **Save changes** перед переходом к развёртыванию [расположения](#deploy-location) и [metric adapter](#deploy-adapter).

Созданное расположение отображается на странице **Private Synthetic locations** с логотипом Kubernetes или OpenShift. Обратите внимание, что на данном этапе к расположению не назначены ActiveGate.

![Empty location](https://dt-cdn.net/images/containerized-empty-location-1351-ef0b3700e2.png)

Пустое расположение

### 2. Развёртывание расположения

Выберите ваше расположение в **Private Synthetic locations** для скачивания шаблона расположения и генерации команд для выполнения на кластере Kubernetes.

1. В разделе **Deployment** создайте **PaaS token** (**Create token**) или вставьте существующий токен. PaaS-токен необходим для генерации токенов подключения ActiveGate для связи с вашей средой Dynatrace.

   Существующие токены перечислены на странице **Access tokens**. Учтите, что PaaS-токен отображается только один раз при создании, после чего хранится в зашифрованном виде. Рекомендуем хранить PaaS-токен в менеджере паролей для повторного использования при создании дополнительных частных расположений в кластере Kubernetes.
2. Укажите **ActiveGate name** или используйте значение по умолчанию. Это имя используется как префикс для ActiveGate, развёртываемых в составе расположения. Первый ActiveGate называется `<prefix>-0`, второй `<prefix>-1` и т.д. Это имя также используется как имя StatefulSet.
3. Укажите имя **Location namespace** или используйте значение по умолчанию. (Оставьте **Metric adapter namespace** без изменений. Это поле нужно только для генерации [шаблона Synthetic metric adapter](#deploy-adapter).)

   Кнопка **Download synthetic.yaml** становится доступна после ввода PaaS-токена, имени ActiveGate и имени пространства имён расположения.

   Значения полей в разделе **Deployment** не сохраняются. При переходе на другую страницу их нужно ввести заново.

   ![Required fields for the location template](https://dt-cdn.net/images/k8s-location-tokens-namespace-1242-d9a86d7dce.png)

   Обязательные поля для шаблона расположения
4. Выберите **Download synthetic.yaml**. Это файл шаблона расположения. Вы можете переименовать файл для удобства идентификации.
5. Скопируйте скачанный шаблон расположения на ваш кластер Kubernetes.
6. Скопируйте и выполните сгенерированные команды на кластере Kubernetes. Ваш PaaS-токен автоматически добавляется к отображаемым командам.

   Выполняйте команды из того же расположения, что и файл шаблона.

   Если вы переименовали файл шаблона, используйте новое имя в командах.

   ![Commands to create the location namespace](https://dt-cdn.net/images/k8s-location-commands-1106-4b8fac8db7.png)

   Команды для создания пространства имён расположения
7. Опционально. Выполните следующую команду, чтобы получить список всех подов в заданном пространстве имён (`dynatrace` в примере ниже) и проверить их развёртывание.

   ```
   kubectl get pod -n dynatrace
   ```

   Вы также можете просмотреть поды на странице **Deployment Status** > **ActiveGates**, используя фильтры `Running in container: True` и `With modules: Synthetic`.

   ![ActiveGate deployment status filters](https://dt-cdn.net/images/k8s-location-deployment-status-1109-28df0f6a0c.png)

   Фильтры статуса развёртывания ActiveGate

### 3. Развёртывание Synthetic metric adapter

Эта процедура генерирует отдельный шаблон для Synthetic metric adapter. Затем вы выполняете сгенерированные команды на кластере Kubernetes для развёртывания metric adapter.

* Synthetic metric adapter необходимо развернуть только один раз на кластер Kubernetes.
* Установка Synthetic metric adapter требует [роли суперпользователя Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) для создания ClusterRole и ClusterRoleBinding.

1. В разделе **Deployment** создайте **Metrics token** (**Create token**) или вставьте существующий токен. Токен метрик — это [токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Узнайте о концепции токена доступа и его областях.") для получения данных об использовании из Dynatrace. Существующие токены перечислены на странице **Access tokens**.
2. Укажите имя **Metric adapter namespace** или используйте значение по умолчанию. (Оставьте **Location namespace** и **ActiveGate name** без изменений. Эти поля нужны только для генерации [шаблона расположения](#deploy-location).)

   Кнопка **Download synthetic-adapter.yaml** становится доступна после ввода токена метрик и имени пространства имён metric adapter.

   Значения полей в разделе **Deployment** не сохраняются. При переходе на другую страницу их нужно ввести заново.

   ![Required fields for the adapter template](https://dt-cdn.net/images/k8s-location-tokens-adapter-1213-fc6df4117a.png)

   Обязательные поля для шаблона adapter
3. Выберите **Download synthetic-adapter.yaml**. Это файл шаблона для Synthetic metric adapter.
4. Скопируйте скачанный шаблон metric adapter на ваш кластер Kubernetes.
5. Скопируйте и выполните сгенерированные команды на кластере Kubernetes. Ваш токен метрик автоматически добавляется к отображаемым командам.

   Выполняйте команды из того же расположения, что и файл шаблона.

   Если вы переименовали файл шаблона, используйте новое имя в командах.

   ![Commands to create the metric adapter namespace](https://dt-cdn.net/images/k8s-location-adapter-commands-1167-f2c11204cc.png)

   Команды для создания пространства имён metric adapter

## Установка контейнеризованного расположения с поддержкой FIPS

1. Переведите расположение в режим FIPS

   В настоящее время это возможно только через [REST API](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление расположениями Synthetic через Synthetic v2 API."), задав свойство `fipsMode` в JSON запроса.

   * Для создания нового расположения используйте вызов [POST location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location "Создание частного расположения Synthetic через Synthetic v2 API.").
   * Для обновления существующего расположения используйте вызов [PUT location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location "Обновление частного расположения Synthetic через Synthetic v2 API.").
2. Выполните дополнительную настройку

   С поддержкой браузера

   С поддержкой браузера и корпоративным прокси

   Безбраузерное

   Предоставьте сертификат для повторной подписи HTTPS-запросов (описано в разделе [Режим FIPS](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Узнайте, как настроить прокси для синтетического мониторинга.")):

   ```
   kubectl -n $NAMESPACE create secret tls synthetic-fips-proxy-cert --cert=squid.crt --key=squid.key
   ```

   1. Предоставьте сертификат для повторной подписи HTTPS-запросов (описано в разделе [Режим FIPS](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Узнайте, как настроить прокси.")):

      ```
      kubectl -n $NAMESPACE create secret tls synthetic-fips-proxy-cert --cert=squid.crt --key=squid.key
      ```
   2. Предоставьте конфигурацию корпоративного прокси для Squid (описано в разделе [Режим FIPS с корпоративным прокси](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-corporate-proxy "Узнайте, как настроить прокси.")):

      ```
      kubectl -n $NAMESPACE create secret generic synthetic-fips-proxy-peer --from-literal='peer.conf=cache_peer proxy.example.com parent 443 0 default no-digest proxy-only login=proxyuser:proxypass tls tls-min-version=1.2 tls-options=NO_SSLv3'
      ```
   3. Предоставьте конфигурацию корпоративного прокси для ActiveGate:

      * см. [Конфигурация прокси](#proxy)

   Дополнительная настройка не требуется.
3. Переходите к скачиванию и развёртыванию шаблона YAML, как описано в разделе [Установка](#deploy-location).

## Обновление контейнеризованного расположения или его ActiveGate

Обновить контейнеризованное расположение или его ActiveGate можно только в предыдущем Dynatrace. В последней версии Dynatrace контейнеризованные расположения доступны только в режиме просмотра.

Любые обновления расположения требуют повторного скачивания файла шаблона расположения и применения изменений через kubectl.

**Обновление версий ActiveGate**

1. Скачайте файл шаблона расположения.

   1. Выберите ваше расположение в **Private Synthetic locations**.
   2. В разделе **Deployment** повторно введите **PaaS token**, **ActiveGate name** и имя **Location namespace**, указанные при [развёртывании расположения](#deploy-location). Кнопка **Download synthetic.yaml** станет доступна.
   3. Выберите **Download synthetic.yml** для скачивания нового файла шаблона расположения.
   4. Переименуйте файл для удобства идентификации.
   5. Скопируйте файл шаблона на ваш кластер Kubernetes.
2. Выполните следующую команду для применения изменений на кластере Kubernetes. Используйте имя вашего файла шаблона расположения вместо `synthetic.yaml`. Выполняйте команду из того же расположения, что и файл шаблона.

   ```
   kubectl apply -f ./synthetic.yaml
   ```

При любом обновлении ActiveGate повторно разворачиваются в порядке, обратном порядку их развёртывания. Например, если расположение содержит ActiveGate `activegate-name-0` и `activegate-name-1`, первым останавливается и повторно разворачивается `activegate-name-1`.

Повторно развёртываемый под ActiveGate использует тот же постоянный том для обеспечения непрерывности логов.

## Удаление расположения или metric adapter на Kubernetes

Фрагменты кода для удаления расположения или metric adapter на Kubernetes можно сгенерировать только в предыдущем Dynatrace.

Команды, генерируемые при [развёртывании расположения](#deploy-location) и [Synthetic metric adapter](#deploy-adapter), также включают фрагменты кода для их удаления на Kubernetes. Вы можете скопировать и сохранить эти команды для дальнейшего использования.

В любой момент вы можете повторно сгенерировать команды для соответствующих пространств имён.

* Если вы переименовали файл шаблона, используйте новое имя в командах.
* Команды очистки, показанные ниже, не удаляют соответствующие пространства имён.

**Расположение**

1. Выберите ваше расположение в **Private Synthetic locations**.
2. Повторно введите **Paas token**, **ActiveGate name** и имя **Location namespace**.
3. **Скопируйте** и используйте команды **Cleanup** для расположения.

   ![Delete location resources](https://dt-cdn.net/images/k8s-location-delete-1111-8927775af1.png)

   Удаление ресурсов расположения

Обратите внимание, что эта процедура удаляет только ресурсы Kubernetes; [расположение, изначально настроенное в Dynatrace](#initial-setup), не удаляется.

**Synthetic metric adapter**

1. Выберите ваше расположение в **Private Synthetic locations**.
2. Повторно введите **Metrics token** и имя **Metric adapter namespace**.
3. **Скопируйте** и используйте команду **Cleanup** для metric adapter.

   ![Delete the metric adapter](https://dt-cdn.net/images/k8s-location-adapter-delete-1098-fe02e0d2db.png)

   Удаление metric adapter

Если [Synthetic metric adapter](#deploy-adapter) удалён или перестал работать, horizontal pod auto-scaler'ы больше не могут получать данные об использовании от Dynatrace, и ваши контейнеризованные расположения становятся [немасштабируемыми](#non-scalable).

## Доступ к PVC в нескольких зонах доступности на облачных кластерах

Использование кластера с несколькими зонами доступности (multi-AZ) с развёртываниями на основе PVC может привести к тому, что поды зависнут в состоянии ожидания при пересоздании. Это происходит потому, что хранилища вроде EBS не реплицируются между зонами.

PVC совместно используются только узлами в одной зоне доступности. Если в кластере с несколькими зонами узел пытается получить доступ к PVC из другой зоны, он зависнет в состоянии ожидания с сообщением об ошибке.

В настоящее время существует два возможных решения для развёртываний Kubernetes в нескольких зонах:

* Использование node affinity для ограничения подов конкретной зоной.
* Использование систем общего хранилища, таких как EFS.

### Использование node affinity для ограничения подов конкретной зоной

Вы можете настроить node affinity для использования только конкретных зон при развёртывании.

Настройка node affinity

1. Используйте следующую команду для определения зоны каждого узла:

   ```
   kubectl get nodes --show-labels
   ```
2. Найдите метку `failure-domain.beta.kubernetes.io/zone`, например `failure-domain.beta.kubernetes.io/zone=us-east-1a`.
3. Используйте команду kubectl label для установки пользовательской метки на узел:

   ```
   kubectl label nodes node name label=value
   ```

   Пример

   ```
   kubectl label nodes ip-10-179-202-73.ec2.internal zone=us-east-1a
   ```
4. Добавьте пользовательскую метку узла в раздел `nodeSelector` шаблона развёртывания Synthetic. Например:

   ```
   spec:



   nodeSelector:



   zone: us-east-1a
   ```
5. Сохраните изменения.
6. Примените шаблон.

Узлы с одинаковой меткой зоны будут развёрнуты в одной зоне доступности, и вы сможете совместно использовать PVC между ними без ошибок.

### Использование систем общего хранилища

Каждый облачный сервис предоставляет собственные варианты систем общего хранилища. Для объяснения принципа работы используем AWS EFS в качестве примера. Информацию о системах хранилища, используемых другими облачными провайдерами, см.:

* Google Cloud: [О поддержке Filestore для Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs/concepts/filestore-for-gke)
* Azure Storage: [Что такое Azure Files?](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)

  Стандартный драйвер SMB/CIFS не поддерживается для Azure Files. Подробности см. в статье [Crashes при изменении прав доступа к файлам с хранилищем Azure Files](https://access.redhat.com/solutions/7078656).

Предполагается, что у вас уже есть EFS. Если нет, см. [Начало работы с Amazon EFS](https://dt-url.net/vq02epe).

Учтите, что EFS может быть дороже EBS. Проверьте ценообразование.

Использование класса хранилища с EFS

1. Дополните шаблон развёртывания Synthetic, как в примере ниже:

   ```
   kind: StorageClass



   apiVersion: storage.k8s.io/v1



   metadata:



   name: efs-test



   provisioner: efs.csi.aws.com



   parameters:



   fileSystemId: fs-0c155dcd8425aa39d



   provisioningMode: efs-ap



   directoryPerms: "700"



   basePath: "/"
   ```
2. Измените раздел **volumeClaimTemplates** шаблона, как в примере ниже:

   ```
   volumeClaimTemplates:



   - metadata:



   name: persistent-storage



   spec:



   storageClassName: efs-test



   accessModes:



   - ReadWriteMany



   resources:



   requests:



   storage: 3Gi
   ```
3. Сохраните изменения.
4. Примените шаблон.

Теперь при повторном развёртывании пода на узле в другой зоне PVC должен автоматически привязаться к новой зоне развёртывания.

## NAM-мониторы на контейнеризованных расположениях

Мониторы доступности сети поддерживаются на контейнеризованных развёртываниях Synthetic-enabled ActiveGate, однако для ICMP-тестов требуются дополнительные разрешения.

Включение типа запроса ICMP для выполнения NAM

1. В **Settings** выберите и разверните **Web and mobile monitoring**.
2. В разделе **Web and mobile monitoring** выберите **Private Synthetic Locations**.
3. Нажмите **Add Kubernetes location**.
4. Настройте расположение и убедитесь, что включён параметр **Enable ICMP request type for Network Availability Monitors execution**.

* ICMP-мониторы используют исполняемый файл `ping`, которому требуется возможность `CAP_NET_RAW` для контейнера, выполняющего запросы (`synthetic-vuc`).
* Свойство `allowPrivilegeEscalation` в `securityContext` этого контейнера должно быть установлено в `true`, поскольку процесс, запускающий `ping`, по умолчанию не имеет необходимых привилегий.

Полный `securityContext` для контейнера `synthetic-vuc` с включёнными мониторами доступности сети должен выглядеть следующим образом.

```
securityContext:



readOnlyRootFilesystem: true



privileged: false



allowPrivilegeEscalation: true



runAsNonRoot: true



capabilities:



drop: ["all"]



add: ["NET_RAW"]
```

### OpenShift

OpenShift использует Security Context Constraint для ограничения возможностей, используемых подами.
По умолчанию развёртываемые поды будут использовать SCC `restricted-v2`, которое не допускает дополнительных возможностей.
Рекомендуемое решение: подготовить пользовательский Security Context Constraint.

1. Создайте выделенный Service Account (опционально)

   * Если пользовательский SCC используется только синтетическим развёртыванием, рекомендуется создать выделенный Service Account.

     ```
     oc -n $NAMESPACE create sa sa-dt-synthetic



     oc -n $NAMESPACE adm policy add-role-to-user edit system:serviceaccount:$NAMESPACE:sa-dt-synthetic
     ```
2. Создайте пользовательский Security Context Constraint

   * scc-dt-synthetic.yaml

     ```
     apiVersion: security.openshift.io/v1



     kind: SecurityContextConstraints



     metadata:



     name: scc-dt-synthetic



     allowPrivilegedContainer: false



     allowHostDirVolumePlugin: false



     allowHostIPC: false



     allowHostNetwork: false



     allowHostPID: false



     allowHostPorts: false



     runAsUser:



     type: MustRunAsRange



     seccompProfiles:



     - runtime/default



     seLinuxContext:



     type: MustRunAs



     fsGroup:



     type: MustRunAs



     supplementalGroups:



     type: MustRunAs



     volumes:



     - configMap



     - downwardAPI



     - emptyDir



     - persistentVolumeClaim



     - projected



     - secret



     users: []



     groups: []



     priority: null



     readOnlyRootFilesystem: true



     requiredDropCapabilities:



     - ALL



     defaultAddCapabilities: null



     allowedCapabilities:



     - NET_RAW



     allowPrivilegeEscalation: true
     ```
   * `priority` может быть установлен в любое число от 1 до 9. Если есть два или более SCC, удовлетворяющих требованиям, выбирается тот с более высоким приоритетом.

     ```
     oc create -f scc-dt-synthetic.yaml
     ```
3. Добавьте новый SCC к Service Account, используемому для синтетического развёртывания

   ```
   oc -n $NAMESPACE adm policy add-scc-to-user scc-dt-synthetic system:serviceaccount:$NAMESPACE:default
   ```

   * Если был создан SA `sa-dt-synthetic`, используйте его вместо `default`.

     ```
     oc -n $NAMESPACE adm policy add-scc-to-user scc-dt-synthetic system:serviceaccount:$NAMESPACE:sa-dt-synthetic
     ```

### Azure RedHat OpenShift (ARO)

Если кластер OpenShift развёрнут как ресурс Azure Red Hat OpenShift (ARO), по умолчанию Network Security Group не разрешает ICMP-трафик за пределы кластера.

Network Security Group ARO не поддаётся изменению, однако пользовательский NSG можно создать и импортировать при создании кластера ARO.
Подробности см. в статье [Bring your own Network Security Group (NSG) to an Azure Red Hat OpenShift (ARO) cluster](https://learn.microsoft.com/en-us/azure/openshift/howto-bring-nsg).

Запуск кластера с настройками по умолчанию позволяет использовать ICMP NAM-мониторы только для ресурсов внутри кластера OpenShift. Любые запросы за пределы кластера завершатся с ошибкой.

## Конфигурация прокси

Добавьте следующий код в начало вашего [файла шаблона расположения](#install) для вставки ресурса ConfigMap с информацией о прокси-сервере.

В приведённом примере кода:

* Прокси-сервер используется для подключений к Dynatrace Cluster и тестируемым ресурсам.
* Пространство имён (`namespace: dynatrace`) должно быть пространством имён расположения.

```
kind: ConfigMap



apiVersion: v1



data:



custom.properties: |-



[http.client]



proxy-server = 10.102.43.210



proxy-port = 3128



proxy-user = proxyuser



proxy-password = proxypass



metadata:



name: ag-custom-configmap



namespace: dynatrace



---
```

Добавьте следующий код в `spec.template.spec.volumes:`.

```
- name: ag-custom-volume



configMap:



name: ag-custom-configmap



items:



- key: custom.properties



path: custom.properties
```

Добавьте следующий код в конфигурацию контейнера ActiveGate в раздел `volumeMounts:`.

```
- name: ag-custom-volume



mountPath: /var/lib/dynatrace/gateway/config_template/custom.properties



subPath: custom.properties
```

## Совместимость с Dynatrace Operator

Если вы разворачиваете Dynatrace Operator в том же кластере Kubernetes, что и контейнеризованное расположение Synthetic, сгенерированный шаблон StatefulSet должен включать аннотацию пода `dynatrace.com/split-mounts: "true"`. Эта аннотация предотвращает конфликты, возникающие при инъекции Operator в образ ActiveGate, который уже содержит директорию `/var/lib/dynatrace`.

Начиная с Dynatrace версии 1.335 эта аннотация включается в шаблон расположения, генерируемый Dynatrace. Если вы управляете манифестом StatefulSet вручную или используете более раннюю версию, убедитесь, что аннотация присутствует в разделе `spec.template.metadata.annotations`. Подробности см. в [примечаниях к выпуску Dynatrace Operator 1.8.0](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Примечания к выпуску Dynatrace Operator версии 1.8.0.").

## Безбраузерные частные расположения Synthetic

В общем случае рекомендуется развёртывать полные синтетические частные расположения с поддержкой выполнения всех типов синтетических мониторов (HTTP, браузерных, NAM).

Если выполнение браузерных мониторов не требуется, рассмотрите развёртывание расположения в безбраузерном режиме. В этом режиме расположение (или ActiveGate в его составе) разворачивается без браузера, что снижает требования к оборудованию. Однако браузерные мониторы на безбраузерном расположении работать не будут.

Рассмотрите безбраузерные расположения как альтернативу синтетическим частным расположениям с поддержкой браузерных мониторов в следующих сценариях:

* Задачи, связанные с сетью и инфраструктурой (с использованием NAM-мониторов).
* Мониторинг API (с использованием HTTP-мониторов).

По сравнению со стандартным шаблоном вносятся следующие изменения:

1. Для переменной окружения `DT_SYNTHETIC_UNSUPPORTED_MONITORING_MODULES` в контейнере `synthetic-vuc` в секции `env:` устанавливается значение `browser`:

   ```
   - name: DT_SYNTHETIC_UNSUPPORTED_MONITORING_MODULES



   value: "browser"
   ```
2. Контейнеры `synthetic-vuc-worker` не включаются.
3. Том `chromium-cache` не задаётся и не монтируется.

## Настройка аутентификации Kerberos

Добавьте следующий код в начало вашего [файла шаблона расположения](#install) для вставки ресурса ConfigMap с информацией о вашем Kerberos-сервере.

В приведённом примере кода:

* Realm `EXAMPLE.COM` используется в аутентификации Kerberos.
* Домен `example.com` используется в аутентификации Kerberos.
* `kerberos.example.com` — имя хоста Key Distribution Center.
* Пространство имён (`namespace: dynatrace`) должно быть пространством имён расположения.

```
kind: ConfigMap



apiVersion: v1



data:



krb5.conf: |-



[libdefaults]



dns_lookup_realm = false



ticket_lifetime = 24h



renew_lifetime = 7d



forwardable = true



rdns = false



pkinit_anchors = FILE:/etc/pki/tls/certs/ca-bundle.crt



spake_preauth_groups = edwards25519



dns_canonicalize_hostname = fallback



qualify_shortname = ""



default_realm = EXAMPLE.COM



default_ccache_name = /tmp/krb5cc_%{uid}



[realms]



EXAMPLE.COM = {



kdc = kerberos.example.com



admin_server = kerberos.example.com



}



[domain_realm]



.example.com = EXAMPLE.COM



example.com = EXAMPLE.COM



metadata:



name: krb-map



namespace: dynatrace



---
```

Добавьте следующий код в `spec.template.spec.volumes:`.

```
- name: krb5-conf



configMap:



name: krb-map



items:



- key: krb5.conf



path: krb5.conf
```

Добавьте следующий код в конфигурацию каждого контейнера `synthetic-vuc-worker` в раздел `volumeMounts:`.

```
- name: krb5-conf



mountPath: /etc/krb5.conf



subPath: krb5.conf
```

## Synthetic metric adapter

### Отключение валидации доменного сертификата

Добавьте следующий код в шаблон Synthetic metric adapter в секцию `env:`:

```
- name: TLS_SECURE



value: "false"
```

Это отключает валидацию сертификата для подключения Synthetic metric adapter к Dynatrace Cluster (по умолчанию она активирована).

### Конфигурация прокси

Добавьте следующий код в шаблон Synthetic metric adapter в секцию `env:`:

```
- name: HTTPS_PROXY



value: "http://proxyuser:proxypass@10.102.43.210:3128"



- name: NO_PROXY



value: "172.20.0.0/16"  # do not proxy internal calls to Kubernetes cluster
```

Дополнительные сведения об этих переменных окружения см. в [документации пакета Go httpproxy](https://pkg.go.dev/golang.org/x/net/http/httpproxy#Config).

Способ получения Service CIDR зависит от дистрибутива Kubernetes; например, для AWS EKS можно использовать следующую команду:

```
aws eks describe-cluster --name my-cluster --query 'cluster.kubernetesNetworkConfig'
```

## Немасштабируемые контейнеризованные расположения

Автомасштабируемые расположения становятся немасштабируемыми по любой из следующих причин.

* Расположение достигает максимального количества подов в StatefulSet, а использование расположения превышает порог в 80%. Новые поды ActiveGate не создаются до увеличения максимального количества ActiveGate.
* [Synthetic metric adapter](#deploy-adapter) перестаёт работать, и horizontal pod auto-scaler'ы расположения не получают метрики, необходимые для автомасштабирования.

  Для проверки состояния pod auto-scaler можно использовать следующую команду. В примере ниже `dynatrace` — пространство имён расположения.

  ```
  kubectl describe hpa -n dynatrace
  ```

  Если в выводе `ScalingActive` установлен в `False`, auto-scaler не получает данные метрик.

## API: Synthetic - Locations, nodes, and configuration API v2

Вы можете автоматизировать развёртывание и управление контейнеризованными расположениями через существующий [API v2 Synthetic - Locations, nodes, and configuration](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление расположениями Synthetic через Synthetic v2 API."). В этот API добавлены ранние эндпоинты Early Access для упрощения развёртывания расположений Kubernetes. Новые эндпоинты помогают генерировать команды для выполнения на кластере Kubernetes.

![New endpoints for Kubernetes location deployment](https://dt-cdn.net/images/k8s-locations-endpoints-3168-a8f5b7f158.png)

Новые эндпоинты для развёртывания расположений Kubernetes

* Эндпоинт GET location YAML (`/synthetic/locations/{LocationId}/yaml`) получает [файл шаблона расположения](#install) на основе идентификатора расположения, [изначально настроенного](#install) для контейнеризованного развёртывания.
* Эндпоинт GET apply commands (`synthetic/locations/commands/apply`) получает список команд для [развёртывания расположения](#install) на Kubernetes/OpenShift.
* Эндпоинт GET delete commands (`synthetic/locations/{LocationId}/commands/delete`) получает команды для удаления контейнеризованного расположения.

## Связанные разделы

* [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Управление расположениями Synthetic через Synthetic v2 API.")
* [Установка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes")
* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")