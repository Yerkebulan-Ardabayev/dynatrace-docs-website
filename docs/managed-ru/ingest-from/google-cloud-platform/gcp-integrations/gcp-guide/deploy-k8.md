---
title: Настройка интеграции метрик и логов Dynatrace GCP в новом кластере GKE Autopilot
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8
scraped: 2026-05-12T11:50:43.346179
---

# Настройка интеграции метрик и логов Dynatrace GCP в новом кластере GKE Autopilot

# Настройка интеграции метрик и логов Dynatrace GCP в новом кластере GKE Autopilot

* Практическое руководство
* Чтение: 15 мин
* Обновлено 8 октября 2024 г.

Dynatrace версии 1.230+

Следуйте инструкциям ниже, чтобы настроить мониторинг Google Cloud для метрик и логов в новом кластере GKE Autopilot с помощью Google Cloud Shell. В процессе настройки будет создана новая подписка Pub/Sub. В GKE запустятся два контейнера: пересыльщик метрик и пересыльщик логов. После установки в Dynatrace появятся метрики, логи, дашборды и оповещения для настроенных сервисов.

Если требуется запустить скрипт развёртывания на существующем стандартном кластере GKE или GKE Autopilot, см. раздел [Настройка интеграции логов и метрик Dynatrace с Google Cloud на существующем кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Развёртывание мониторинга логов и метрик для сервисов Google Cloud на существующем стандартном кластере GKE или GKE Autopilot").

Другие варианты развёртывания описаны в разделе [Альтернативные сценарии развёртывания](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Другие варианты настройки мониторинга логов и/или метрик для сервисов Google Cloud").

На этой странице описывается установка версии 1.0 интеграции GCP на кластер GKE.

* Если установлена [более ранняя версия](/managed/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Настройка мониторинга логов и метрик для сервисов GCP в контейнере Kubernetes."), необходимо выполнить [миграцию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция с Google Cloud integration версии 0.1 на версию 1.0 в Kubernetes и как Google Cloud Functions.").

## Ограничения

Интеграция логов Dynatrace GCP поддерживает обработку до 8 ГБ данных в час (при базовых ресурсах, без масштабирования). При больших нагрузках сообщения начнут накапливаться в подписке PubSub. Для измерения задержки используйте метрики: `Oldest unacked message age` и `Unacked messages`. Рекомендации по масштабированию см. в [руководстве по масштабированию](#scalingguide) ниже.

Интеграция метрик Dynatrace GCP поддерживает до 50 проектов GCP при стандартном развёртывании. Для мониторинга больших сред необходимо включить область метрик. См. раздел [Мониторинг нескольких проектов GCP: крупные среды](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик в Dynatrace из нескольких проектов Google Cloud.").

## Предварительные требования

Для развёртывания интеграции необходимо убедиться, что на машине, где выполняется установка, выполнены следующие требования.

* Только Linux
* Доступ к интернету
* Доступ к кластеру GKE
* Доступ к среде Dynatrace

  Необходимо настроить эндпоинт Dynatrace (URL среды, кластера или ActiveGate), на который кластер GKE будет отправлять метрики и логи. Убедитесь в наличии прямого сетевого доступа или в том, что промежуточный прокси или другой компонент не влияет на связь.

### Инструменты

Интеграцию Dynatrace GCP можно развернуть в Google Cloud Shell или bash.

При использовании bash необходимо установить:

* [Google Cloud SDK](https://dt-url.net/e8110336)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* [helm](https://helm.sh/docs/intro/install/)
* [jq (версия 1.6)](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (версия 4.9.x+)](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Разрешения GCP

Для запуска скрипта развёртывания требуется набор разрешений. Можно создать пользовательскую роль (см. ниже) и использовать её для развёртывания `dynatrace-gcp-monitor`.

1. Создайте YAML-файл с именем `dynatrace-gcp-monitor-helm-deployment-role.yaml` со следующим содержимым:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- pubsub.subscriptions.create



- pubsub.subscriptions.get



- pubsub.subscriptions.list



- pubsub.topics.attachSubscription



- pubsub.topics.create



- pubsub.topics.getIamPolicy



- pubsub.topics.list



- pubsub.topics.setIamPolicy



- pubsub.topics.update



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Каждая группа разрешений предназначена для управления различными ресурсами, входящими в интеграцию. Создание и доступ предназначены для новых ресурсов, обновление для повторного использования существующих, удаление для деинсталляции.

* container.configMaps: для маппинга секретов и других переменных, используемых контейнерами.
* container.deployments: для развёртывания в кластере K8s (включая поды, контейнеры и т. д.).
* container.namespaces: для пространства имён K8s, в котором развёртываются ресурсы.
* container.pods: для подов K8s.
* container.secrets: для секретов K8s, в которых хранятся конфиденциальные переменные.
* container.serviceAccounts: для service account, используемого в контексте K8s.
* iam.roles: для разрешений, необходимых для сбора данных.
* iam.serviceAccounts: для service account общего контекста.
* resourcemanager.projects: для управления проектом, в котором развёртывается интеграция.
* serviceusage.services: для управления API сервисов.
* pubsub.subscriptions: для подписки PubSub, используемой для сбора и приёма логов.
* pubsub.topics: для топика PubSub, используемого для сбора и приёма логов.

2. Выполните команду ниже, заменив `<your_project_ID>` на идентификатор проекта, в котором требуется развернуть интеграцию Dynatrace GCP.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Обязательно добавьте эту роль своему пользователю GCP. Подробности см. в разделе [Предоставление или отзыв одной роли](https://dt-url.net/vx03vid).

### Настройка экспорта логов

1. Запустите следующий shell-скрипт в проекте GCP, выбранном для развёртывания.

Обязательно замените `<your-subscription-name>` и `<your-topic-name>` на собственные значения.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Настройте [экспорт логов](https://dt-url.net/4743r02), чтобы отправлять нужные логи в созданный выше топик GCP Pub/Sub.

### Разрешения Dynatrace

Необходимо создать токен с набором разрешений.

1. Перейдите в раздел **Access tokens**.
2. Выберите **Generate new token**.
3. Введите имя токена.
4. В разделе **Template** выберите `GCP Services Monitoring`.
5. Нажмите **Generate**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Токен также можно создать и добавить разрешения вручную.

Добавить вручную

[Создайте API-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях применения.") и [включите следующие разрешения](/managed/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Узнайте, как пройти аутентификацию для использования Dynatrace API."):

* API v1:

  + **Чтение конфигурации**
  + **Запись конфигурации**
* API v2:

  + **Приём метрик**
  + **Чтение расширений**
  + **Запись расширений**
  + **Чтение конфигурации мониторинга расширений**
  + **Запись конфигурации мониторинга расширений**
  + **Чтение конфигурации среды расширений**
  + **Запись конфигурации среды расширений**
  + **Приём логов**
  + **Управление метаданными элементов Hub**
  + **Чтение данных Hub**
  + **Установка и обновление элементов Hub**

Для мониторинга логов из нескольких проектов необходимо создать **Log Routing Sinks** в каждом исходном проекте, указав в качестве назначения основной проект (в котором также развёрнуты интеграция, топик PubSub и подписка).
Подробности см. в разделе [Маршрутизация логов в поддерживаемые назначения](https://dt-url.net/cl038gj).

### Приём логов

* Определите, где будет выполняться приём логов, в зависимости от варианта развёртывания. Это важно при настройке [параметров](#param) интеграции.

  + **Для SaaS-развёртываний:** приём логов SaaS выполняется напрямую через Cluster API. Рекомендуется.
  + **Для Managed-развёртываний:** для приёма логов можно использовать существующий ActiveGate. Информацию о развёртывании см. в разделе [Установка ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").

Из-за особенностей реализации Cloud Functions 2-го поколения в GCP логи этих ресурсов будут привязаны к базовым экземплярам Cloud Run. Оба расширения должны быть включены.

Подробности см. в разделе [Сравнение версий Google Cloud Functions](https://dt-url.net/b6038q5).

## Установка

Выполните следующие шаги для завершения настройки.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Загрузить пакет развёртывания Helm в Google Cloud Shell**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#dwld "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настроить значения параметров**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#param "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Запустить скрипт развёртывания**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#script "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

### Шаг 1 Загрузка пакета развёртывания Helm в Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Шаг 2 Настройка значений параметров

1. Пакет развёртывания Helm содержит файл `values.yaml` с необходимой конфигурацией. Перейдите в `helm-deployment-package/dynatrace-gcp-monitor` и отредактируйте файл `values.yaml`, задав обязательные и необязательные значения параметров, как указано ниже.

   Рекомендуется сохранить этот файл для будущих обновлений, так как он потребуется при повторных развёртываниях. Учтите, что его схема может меняться: в таком случае следует использовать новый файл и переносить только значения параметров.

   | **Имя параметра** | **Описание** | **Значение по умолчанию** |
   | --- | --- | --- |
   | `parallelProcesses` | Необязательный. Количество параллельных процессов для всего цикла мониторинга логов | `1` |
   | `numberOfConcurrentLogForwardingLoops` | Необязательный. Количество воркеров, одновременно извлекающих логи из pubsub и отправляющих их в Dynatrace | `5` |
   | `numberOfConcurrentMessagePullCoroutines` | Необязательный. Количество параллельных корутин для извлечения сообщений из pub/sub | `10` |
   | `numberOfConcurrentPushCoroutines` | Необязательный. Количество параллельных корутин для отправки сообщений в Dynatrace | `5` |
   | `gcpProjectId` | Обязательный. Идентификатор проекта GCP, выбранного для развёртывания. | Идентификатор текущего проекта |
   | `deploymentType` | Обязательный. Оставьте значение `all`. | `all` |
   | `dynatraceAccessKey` | Обязательный. Ваш [API-токен Dynatrace](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях применения.") с [необходимыми разрешениями](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") |  |
   | `dynatraceUrl` | Обязательный. Для Managed приёма логов/метрик: URL кластера (`https://<your_cluster_IP_or_hostname>/e/<your_environment_ID>`). Для Managed приёма логов/метрик с существующим ActiveGate: URL ActiveGate (`https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`). **Примечание:** Чтобы узнать `<your-environment-id>`, см. раздел [Идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте о средах мониторинга и принципах работы с ними."). |  |
   | `logsSubscriptionId` | Обязательный. Идентификатор подписки Pub/Sub для приёмника логов. Подробности см. в разделе [Настройка экспорта логов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#pubsub "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot."). |  |
   | `dynatraceLogIngestUrl` | Необязательный. Укажите, если требуется принимать логи отдельно от метрик. Для Managed приёма логов с существующим ActiveGate: URL ActiveGate (`https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`). **Примечание:** Чтобы узнать `<your-environment-id>`, см. раздел [Идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте о средах мониторинга и принципах работы с ними."). |  |
   | `dynatraceAccessKeySecretName` | Необязательный. Позволяет указать ключ для получения эндпоинта из GCP Secret Manager вместо использования `dynatraceAccessKey`. |  |
   | `dynatraceUrlSecretName` | Необязательный. Позволяет указать ключ для получения эндпоинта из GCP Secret Manager вместо использования `dynatraceUrl`. |  |
   | `dynatraceLogIngestUrlSecretName` | Необязательный. Позволяет указать ключ для получения эндпоинта из GCP Secret Manager вместо использования `dynatraceLogIngestUrl`. |  |
   |  |  |  |
   | `requireValidCertificate` | Необязательный. При значении `true` Dynatrace требует SSL-сертификат вашей среды. Для Managed приёма логов с новым ActiveGate рекомендуется установить значение `false`. | `true` |
   | `selfMonitoringEnabled` | Необязательный. Отправка пользовательских метрик в GCP для быстрой диагностики корректности обработки и отправки метрик/логов в Dynatrace через `dynatrace-gcp-monitor`. Подробности см. в разделе [Метрики самомониторинга интеграции Dynatrace GCP](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace."). | `false` |
   | `serviceAccount` | Необязательный. Имя создаваемого service account |  |
   | `dockerImage` | Необязательный. Docker-образ Dynatrace GCP Monitor. Рекомендуется использовать значение по умолчанию, но при необходимости его можно изменить. | `dynatrace/dynatrace-gcp-monitor:v1-latest` |
   | `logIngestContentMaxLength` | Необязательный. Максимальная длина содержимого события лога. Должна быть меньше или равна настройке в среде Dynatrace. | `8192` |
   | `logIngestAttributeValueMaxLength` | Необязательный. Максимальная длина значения атрибута события лога. При превышении серверного лимита содержимое будет усечено. | `250` |
   | `logIngestRequestMaxEvents` | Необязательный. Максимальное количество событий лога в одном запросе к эндпоинту приёма логов. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `5000` |
   | `logIngestRequestMaxSize` | Необязательный. Максимальный размер в байтах одного запроса к эндпоинту приёма логов. При превышении серверного лимита запрос будет отклонён с кодом `413`. | `1048576` |
   | `logIngestEventMaxAgeSeconds` | Необязательный. Определяет максимальный возраст пересылаемого события лога. Должен быть меньше или равен настройке в среде Dynatrace. | `86400` |
   | `printMetricIngestInput` | Необязательный. При значении `true` GCP Monitor выводит строки метрик в stdout. | `false` |
   | `serviceUsageBooking` | Необязательный. Используется для метрик и определяет проект для квоты и биллинга, указанный вызывающей стороной. При значении `source` вызовы monitoring API списываются в проекте, где работает контейнер Kubernetes. При значении `destination` списываются в отслеживаемом проекте. Подробности см. в разделе [Мониторинг нескольких проектов GCP, стандартные среды, шаг 4](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик в Dynatrace из нескольких проектов Google Cloud."). | `source` |
   | `useProxy` | Необязательный. В зависимости от значения GCP Monitor использует следующие настройки прокси: Dynatrace (значение `DT_ONLY`), GCP API (значение `GCP_ONLY`) или оба (значение `ALL`). | По умолчанию настройки прокси не используются. |
   | `httpProxy` | Необязательный. HTTP-адрес прокси; используйте совместно с `USE_PROXY`. |  |
   | `httpsProxy` | Необязательный. HTTPS-адрес прокси; используйте совместно с `USE_PROXY`. |  |
   | `gcpServicesYaml` | Необязательный. Файл конфигурации для сервисов GCP. |  |
   | `queryInterval` | Необязательный. Интервал опроса метрик в минутах. Допустимые значения: `1`–`6` | `3` |
   | `vpcNetwork` | Необязательный. Существующая VPC Network, в которой будет развёрнут кластер Autopilot. Shared VPC не поддерживается. | `default` |
   | `useCustomSubnet` | Необязательный. Установите `true` только при использовании VPC network в пользовательском режиме. При значении `true` необходимо передать параметр `customSubnetName`. | `false` |
   | `customSubnetName` | Обязательный, только если `useCustomSubnet` равен `true`. Укажите имя подсети, в которой требуется развернуть Google Cloud Monitor. | `""` |
   | `scopingProjectSupportEnabled` | Необязательный. Установите `true` при настроенной области метрик, чтобы метрики собирались со всех проектов, добавленных в эту область. Подробности см. в разделе [Мониторинг нескольких проектов GCP: крупные среды](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправка метрик в Dynatrace из нескольких проектов Google Cloud."). | `false` |
   | `excludedProjects` | Необязательный. Разделённый запятыми список проектов, исключаемых из мониторинга (например, `<project_A>,<project_B>`) |  |
   | `excludedMetricsAndDimensions` | Необязательный. Список в формате YAML с метриками и их измерениями, исключаемыми из мониторинга. |  |
   | `metricAutodiscovery` | Необязательный. При значении `true` GCP Monitor запустит режим автообнаружения метрик, расширяя возможности выбора метрик для мониторинга. Подробности см. в разделе [Мониторинг проектов GCP с помощью автообнаружения](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Отправка любых метрик в Dynatrace из проектов Google Cloud."). | `false` |
   | `clusterIpv4Cidr` | Необязательный. Задайте диапазон IP-адресов для подов в этом кластере в нотации CIDR, если требуется пользовательский диапазон. |  |
   | `servicesIpv4Cidr` | Необязательный. Задайте диапазон IP для IP-адресов сервисов. Можно указать как размер маски подсети или в нотации CIDR. |  |
   | `useCustomMasterCidr` | Необязательный. При значении `true` можно указать диапазон IPv4 CIDR для master-сети. | `false` |
   | `masterIpv4Cidr` | Необязательный. Диапазон IPv4 CIDR требует, чтобы `useCustomMasterCidr` имел значение `true`, для использования в master-сети. |  |
2. Выберите сервисы для мониторинга в Dynatrace.

   По умолчанию интеграция Dynatrace GCP начинает мониторинг набора выбранных сервисов. Список поддерживаемых сервисов см. в разделе [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик.").

Информацию о потреблении DDU см. в разделе [Потребление при мониторинге](#ddu).

### Шаг 3 Запуск скрипта развёртывания

Скрипт развёртывания автоматически создаст новый кластер GKE Autopilot с именем `dynatrace-gcp-monitor` и развернёт в нём установку. Будут загружены последние версии расширений GCP.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster
```

Чтобы задать другое имя для нового кластера, выполните вместо этого команду ниже, заменив заполнитель (`<name-of-new-cluster>`) на нужное имя.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

Чтобы сохранить текущие версии существующих расширений и установить последние версии для остальных выбранных расширений при их отсутствии, выполните вместо этого команду ниже.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Проверка установки

Чтобы проверить успешность установки

1. Проверьте, работает ли контейнер.

   После установки может потребоваться несколько минут, прежде чем контейнер запустится.

   ```
   kubectl -n dynatrace get pods
   ```
2. Проверьте логи контейнера на наличие ошибок или исключений. Доступны два варианта:

   В Kubernetes CLI

   В консоли GCP

   Выполните следующие команды.

   ```
   kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics



   kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
   ```

   Чтобы проверить логи контейнера на ошибки в консоли GCP

   1. Перейдите в раздел **Logs explorer**.
   2. Используйте фильтры ниже для получения логов приёма метрик и/или логов из контейнера Kubernetes:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"` (для логов приёма метрик)
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"` (для логов приёма логов)
3. Проверьте, импортированы ли дашборды.

   Перейдите в раздел **Dashboards** и отфильтруйте по тегу **Tag** `Google Cloud`. Должно отображаться несколько дашбордов для сервисов Google Cloud.

## Выбор сервисов для мониторинга метрик

### Сервисы, включённые по умолчанию

В процессе развёртывания GCP Monitor будет включён мониторинг следующих сервисов:

* [Google APIs](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Мониторинг Google Cloud APIs и просмотр доступных метрик.")
* [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Мониторинг Google App Engine и просмотр доступных метрик.")
* [Google BigQuery](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Мониторинг Google BigQuery и просмотр доступных метрик.")
* [Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Мониторинг Google Cloud Functions и просмотр доступных метрик.")
* [Google Cloud Run](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Мониторинг Google Cloud Run и просмотр доступных метрик.")
* [Google Cloud Storage](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Мониторинг Google Cloud Storage и просмотр доступных метрик.")
* [Google Compute Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Мониторинг Google Compute Engine и просмотр доступных метрик.")
* [Google Firestore в режиме Datastore](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Мониторинг Google Cloud Firestore в режиме Datastore и просмотр доступных метрик.")
* [Google Filestore](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Мониторинг Google Filestore и просмотр доступных метрик.")
* [Google Kubernetes Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Мониторинг Google Kubernetes Engine и просмотр доступных метрик.")
* [Google Cloud Load Balancing](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Мониторинг Google Cloud Load Balancing и просмотр доступных метрик.")
* [Google Cloud Pub/Sub](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Мониторинг Google Cloud Pub/Sub и просмотр доступных метрик.")
* [Google Cloud Pub/Sub Lite](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Мониторинг Google Cloud Pub/Sub Lite и просмотр доступных метрик.")
* [Google Cloud SQL](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Мониторинг Google Cloud SQL и просмотр доступных метрик.")

Доступны дополнительные интеграции сервисов, но их необходимо включить. Список поддерживаемых сервисов см. в разделе [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик."). В следующем разделе описано управление ими. В качестве альтернативы можно использовать [автообнаружение](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Отправка любых метрик в Dynatrace из проектов Google Cloud.") для расширения охвата метрик.

### Управление включёнными сервисами

Управление включёнными сервисами осуществляется через Dynatrace Hub.

Отфильтруйте по «gcp»: в результатах появятся аннотации для элементов, уже доступных в вашей среде.

Чтобы включить новый сервис, выберите его в Hub и установите.

Сервис также можно отключить через Dynatrace Hub.

Чтобы проверить, требуют ли сервисы обновления, откройте их в Hub и ознакомьтесь с примечаниями к версии. Обновления могут включать новые метрики, новые ресурсы (дашборды) или другие изменения.

Все изменения включённых сервисов применяются в GCP Monitor в течение нескольких минут.

#### Наборы функций и доступные метрики

Чтобы узнать, какие метрики включены для конкретного сервиса, см. раздел [Поддерживаемые сервисы Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик."). По умолчанию включён только набор функций `defaultMetrics`. Для включения дополнительных наборов функций раскомментируйте их в файле `values.yaml` и повторно разверните GCP Monitor.

Текущую конфигурацию наборов функций можно найти в ConfigMap кластера с именем `dynatrace-gcp-function-config`.

#### Расширенное управление областью мониторинга

Для дополнительного уточнения области мониторинга используйте поле `filter_conditions` в файле `values.yaml`. Это требует повторного развёртывания GCP Monitor. Синтаксис см. в разделе [Фильтры GCP Monitoring](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).

Пример:

```
filter_conditions:



resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Включение оповещений

Для активации оповещений необходимо включить метрические события для оповещений в Dynatrace.

Чтобы включить метрические события

1. Перейдите в раздел **Settings**.
2. В разделе **Anomaly detection** выберите **Metric events**.
3. Отфильтруйте оповещения GCP и включите **On/Off** для нужных оповещений.

## Просмотр метрик и логов

После развёртывания интеграции можно:

* Просматривать метрики отслеживаемых сервисов: перейдите в раздел **Metrics** и отфильтруйте по `gcp`.
* Просматривать и анализировать логи GCP: перейдите в раздел **Logs** и для поиска логов GCP отфильтруйте по `cloud.provider: gcp`.

## Изменение параметров развёртывания

### Изменение параметров из `values.yaml`

Для загрузки нового файла `values.yaml` необходимо обновить Helm-релиз.

Чтобы обновить Helm-релиз

1. Определите используемую версию Helm-релиза.

   ```
   helm ls -n dynatrace
   ```
2. Выполните команду ниже, заменив `<your-helm-release>` значением из предыдущего шага.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

Подробности см. в разделе [Helm upgrade](https://helm.sh/docs/helm/helm_upgrade/).

### Изменение типа развёртывания

Чтобы изменить тип развёртывания (`all`, `metrics` или `logs`)

1. Определите используемую версию Helm-релиза.

   ```
   helm ls -n dynatrace
   ```
2. Удалите релиз.

   Обязательно замените `<your-helm-release>` именем релиза из предыдущего вывода.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Измените `deploymentType` в `values.yaml` на новое значение и сохраните файл.
4. Повторно запустите команду развёртывания. Подробности см. в разделе [Запуск скрипта развёртывания](#script).

## Проверка

Для диагностики возможных проблем с развёртыванием и подключением

1. [Проверьте установку](#verify)
2. [Включите самомониторинг](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.") Опционально
3. Проверьте лог-файл `dynatrace_gcp_<date_time>.log`, созданный в процессе установки.

* Этот файл создаётся при каждом запуске скрипта установки.
* Отладочная информация не содержит конфиденциальных данных, таких как ключ доступа Dynatrace.
* При обращении к эксперту Dynatrace через чат:

  + Предоставьте лог-файл `dynatrace_gcp_<date_time>.log`, описанный на предыдущем шаге.
  + Укажите информацию о версии.

    - Для проблем при установке проверьте файл `version.txt`.
    - Для проблем во время работы [проверьте логи контейнера](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace.").

## Руководство по масштабированию для логов

Стандартный контейнер с 1,25 vCPU и 1 ГиБ (при конфигурации по умолчанию) обеспечивает пропускную способность по логам до 8 ГБ/ч. Для достижения более высокой пропускной способности необходимо выделить контейнеру больше ресурсов (масштабирование вверх), увеличить количество реплик контейнера (масштабирование по горизонтали) и настроить конфигурационные параметры для эффективного использования выделенных ресурсов. Все переменные конфигурации можно найти и изменить в `dynatrace-gcp-monitor-config`.

В следующей таблице представлены протестированные конфигурации и достигнутая пропускная способность при масштабировании контейнеров вверх и по горизонтали:

| Достигнутая пропускная способность | Ресурсы машины | Наборы реплик | Значения переменных конфигурации |
| --- | --- | --- | --- |
| ~8 МБ/с => ~480 МБ/мин | 4 vCPU 4 ГиБ RAM | 1 | `PARALLEL_PROCESSES=4`,  `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20` |
| ~25 МБ/с => ~1,5 ГБ/мин => ~2 ТБ/день | 4 vCPU 4 ГиБ RAM | 4 | `PARALLEL_PROCESSES=4`,  `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20` |
| ~46 МБ/с => ~2,7 ГБ/мин => ~4 ТБ/день | 4 vCPU 4 ГиБ RAM | 6 | `PARALLEL_PROCESSES=4`,  `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20` |

## Руководство по автомасштабированию для логов

Автомасштабирование работает только для типа развёртывания `logs`, но не для `all`.

Рекомендуется вручную масштабировать контейнер до 4 vCPU и 4 ГиБ, а затем включать автомасштабирование.

GCP обеспечивает автомасштабирование контейнеров в обоих направлениях: **горизонтальном** и **вертикальном**. Dynatrace рекомендует только **горизонтальное** масштабирование.

При наличии машины 4 vCPU 4 ГиБ можно включить **горизонтальное** автомасштабирование. Горизонтальное масштабирование с базовыми ресурсами контейнера (1,25 vCPU, 1 ГиБ) **не** рекомендуется: тестирование не подтвердило его эффективность. Одна машина 4 vCPU работает лучше, чем четыре машины по 1 vCPU. Для включения горизонтального автомасштабирования используйте команду:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Автомасштабирование рекомендуется только при минимальной пропускной способности 450 МБ/мин и наличии машины 4 vCPU 4 ГиБ RAM. Автомасштабирование выполняет только горизонтальное масштабирование, но не вертикальное.

**Вертикальное** масштабирование **не** рекомендуется, так как при каждом увеличении машины необходимо изменять переменную среды для создания большего числа процессов, соответствующих ядрам машины.

## Удаление

1. Определите используемую версию Helm-релиза.

```
helm ls -n dynatrace
```

2. Удалите релиз.

Обязательно замените `<your-helm-release>` именем релиза из предыдущего вывода.

```
helm uninstall <your-helm-release> -n dynatrace
```

Также можно удалить пространство имён.

```
kubectl delete namespace dynatrace
```

3. Чтобы удалить все ресурсы мониторинга (дашборды и оповещения) из Dynatrace, необходимо удалить все расширения GCP.

Найти и удалить соответствующие расширения можно через Dynatrace Hub.

Обязательно удалите следующие ресурсы вручную:

* Исходную роль, созданную и привязанную к service account, используемому для развёртывания интеграции.
* Топик PubSub.
* Подписку PubSub.
* Приёмник LogRoute Sink.

## Потребление при мониторинге

### Приём метрик

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от числа отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробности см. в разделе [Расширение Dynatrace (единицы данных Davis)](/managed/license/monitoring-consumption-classic/davis-data-units "Понимание расчёта потребления мониторинга Dynatrace на основе единиц данных Davis (DDU).").

### Приём логов

Потребление DDU распространяется на облачный мониторинг логов. Подробности см. в разделе [DDU для мониторинга логов](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Понимание расчёта объёма потребления DDU для Dynatrace Log Monitoring Classic.").

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Устранение неполадок Google Cloud Monitor](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)