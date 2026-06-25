---
title: Обнаружение облачных приложений и рабочих нагрузок
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection
scraped: 2026-05-12T11:37:57.224517
---

# Cloud application and workload detection

# Обнаружение облачных приложений и рабочих нагрузок

* How-to guide
* 6-min read
* Updated on May 13, 2024

Dynatrace обеспечивает автоматическое обнаружение облачных приложений и рабочих нагрузок в средах Cloud Foundry, Docker и Podman, а также Kubernetes/OpenShift. Облачные приложения и рабочие нагрузки объединяют похожие процессы в группы процессов и сервисы, что позволяет проводить анализ версий.

Обнаружение облачных приложений и рабочих нагрузок обеспечивает:

* Анализ [пространств имён, нагрузок и подов Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-workloads-kubernetes "Enable Kubernetes/OpenShift workloads integration for Dynatrace monitoring.")
* Метрики ресурсов контейнеров для контейнеров Kubernetes и Cloud Foundry
* Обнаружение версий сервисов, работающих в нагрузках Kubernetes

Начиная с Dynatrace version 1.258 и OneAgent version 1.257

* Функция включена по умолчанию.
* Функцию **Cloud application and workload detection** можно настраивать независимо для Kubernetes, Cloud Foundry и чистых сред Docker и Podman:

  1. Перейдите в **Settings**.
  2. Выберите **Processes and containers** > **Cloud application and workload detection**.
  3. Включите/отключите **Enable cloud application and workload detection […]** для **Cloud Foundry**, **Docker and Podman** или **Kubernetes/OpenShift** по мере необходимости.
  4. Выберите **Save changes**.

OneAgent versions 1.256 и ниже не поддерживают независимую конфигурацию для каждого типа среды. Для этих версий OneAgent обнаружение облачных приложений и рабочих нагрузок включается только при активации настройки для всех трёх сред: **Cloud Foundry**, **Docker and Podman**, **Kubernetes/OpenShift**.

Начиная с Dynatrace version 1.299 и OneAgent version 1.297, Dynatrace автоматически обнаруживает контейнеры на основе захваченных метаданных облачных провайдеров: AWS ECS, AWS Fargate, Azure Container Apps и многих других.
Обнаружение контейнеров можно настроить следующим образом:

1. Перейдите в **Settings**.
2. Выберите **Processes and containers** > **Cloud application and workload detection**.
3. Включите/отключите **Enable container detection for serverless container services** по мере необходимости.
4. Выберите **Save changes**.

Ниже описано, как использовать свойства нагрузок Kubernetes для группировки процессов схожих нагрузок. Кроме того, по-прежнему применяются [универсальные правила обнаружения процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") без учёта свойств контейнеров или платформ.

## Правила обнаружения нагрузок для Kubernetes

По умолчанию Dynatrace создаёт отдельные группы процессов и сервисы для каждой нагрузки Kubernetes.

Можно определять правила для поддержки стратегий выпуска (например, blue/green, canary), используя свойства нагрузок: **Namespace name**, **Base pod name** или **Container name**, а также переменные среды `DT_RELEASE_STAGE` и `DT_RELEASE_PRODUCT` для группировки процессов схожих нагрузок. Также можно задать [версию и версию сборки](/managed/deliver/release-monitoring/version-detection-strategies "Metadata for version detection in different technologies") развёрнутой нагрузки с помощью переменных среды `DT_RELEASE_VERSION` и `DT_RELEASE_BUILD_VERSION`. Это даёт расширенное представление о влиянии выпусков на ваши сервисы.

Правила ограничены пространствами имён Kubernetes, что позволяет легко переносить существующую среду по одному пространству имён. Применяется первое подходящее правило из списка. Если ни одно правило не совпадает, в качестве запасного варианта используется комбинация **Namespace name**, **Base pod name** и **Container name**.

Создание правила

1. Перейдите в **Settings**.
2. Выберите **Processes and containers** > **Cloud application and workload detection**.
3. Выберите **Add rule**.
4. Используйте комбинацию пяти входных переменных ниже для определения правила обнаружения групп процессов.

* **Namespace name**
* **Base pod name** (например, "paymentservice-" для "paymentservice-5ff6dbff57-gszgq")
* **Container name** (как определено в спецификации пода)
* **Stage** (`DT_RELEASE_STAGE`)
* **Product** (`DT_RELEASE_PRODUCT`)

  Если параметр **Product** включён, но не задан, по умолчанию используется **Base pod name**.
* Установите **Match operator** и **Namespace name** для определения пространств имён, к которым должно применяться правило.
* Выберите **Save changes**.

Обратите внимание, что изменения правил **Cloud application and workload detection** вступают в силу только после перезапуска подов.

Изменение правил по умолчанию может привести к созданию новых идентификаторов для групп процессов и сервисов, а также к потере пользовательских конфигураций для существующих групп процессов.

После получения новых идентификаторов группами процессов или сервисами учтите следующее:

* Пользовательские конфигурации не переносятся в новые группы процессов или сервисы. Это относится к именам, настройкам мониторинга, а также настройкам обнаружения ошибок и аномалий.
* Все существующие пользовательские оповещения, пользовательские графики на панелях мониторинга или фильтры, сопоставленные с перезаписанными идентификаторами отдельных групп процессов или сервисов, перестанут работать или отображать данные мониторинга.
* Интеграции с API Dynatrace, в которых запрашиваются конкретные группы процессов или сервисы, необходимо обновить.

### Влияние на именование групп процессов по умолчанию

OneAgent versions 1.241+

Dynatrace стремится предоставлять интуитивно понятные имена групп процессов для DevOps-команд. Создание правил для нагрузок Kubernetes также влияет на формирование содержательных имён групп процессов по умолчанию. Шаблон по умолчанию для `{ProcessGroup:DetectedName}` имеет вид: `«<tech_prefix> <product> <STAGE> <base_pod_name>»`, где:

* `<tech_prefix>` — имена обнаруженных технологий: имя технологии, исполняемый файл, путь и стартовый класс.
* `<product>`, `<STAGE>`, `<base_pod_name>` — необязательные переменные, используемые только при их включении в правило, применённое для соответствующего пространства имён Kubernetes.

**Пример:** `"index.js emailservice PROD"`, где:

* `index.js` — `<tech_prefix>`
* `emailservice` — `<product>`
* `PROD` — `<STAGE>`

В данном случае `<base_pod_name>` не используется и не включается в `{ProcessGroup:DetectedName}`.

Если именование групп процессов по умолчанию слишком общее или не соответствует вашим стандартам именования, его можно настроить с помощью [правил именования групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming").

### Пример — рекомендации по использованию меток Kubernetes

Рекомендуется передавать метки Kubernetes в переменные среды в конфигурации развёртывания (см. [Version detection with Kubernetes labels](/managed/deliver/release-monitoring/version-detection-strategies#kubernetes "Metadata for version detection in different technologies")) с помощью [Downward API](https://dt-url.net/5k03x6s):

* `app.kubernetes.io/version` -> `DT_RELEASE_VERSION`
* `app.kubernetes.io/name` -> `DT_RELEASE_PRODUCT`
* `app.kubernetes.io/stage` -> `DT_RELEASE_STAGE`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: emaildeploy
spec:
  selector:
    matchLabels:
      app: emailservice
  template:
    metadata:
      annotations:
        metrics.dynatrace.com/path: /stats/prometheus
        metrics.dynatrace.com/port: "15090"
        metrics.dynatrace.com/scrape: "true"
      labels:
        app: emailservice
        app.kubernetes.io/version: 0.3.6
        app.kubernetes.io/stage: production
        app.kubernetes.io/name: emailservice
        app.kubernetes.io/part-of: online-boutique
    spec:
      serviceAccountName: default
      terminationGracePeriodSeconds: 5
      containers:
      - name: server
        image: gcr.io/google-samples/microservices-demo/emailservice:v0.3.6
        ports:
        - containerPort: 8080
        env:
        - name: PORT
          value: "8080"
        - name: DT_RELEASE_VERSION
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app.kubernetes.io/version']
        - name: DT_RELEASE_PRODUCT
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app.kubernetes.io/name']
        - name: DT_RELEASE_STAGE
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['app.kubernetes.io/stage']
        - name: DISABLE_TRACING
          value: "1"
        - name: DISABLE_PROFILER
          value: "1"
        readinessProbe:
          periodSeconds: 5
          exec:
            command: ["/bin/grpc_health_probe", "-addr=:8080"]
        livenessProbe:
          periodSeconds: 5
          exec:
            command: ["/bin/grpc_health_probe", "-addr=:8080"]
        resources:
          requests:
            cpu: 100m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 128Mi
---
```

В качестве следующего шага эту конфигурацию можно легко использовать с одним правилом — **Namespace exists**.

![Add a Namespace exists rule for Kubernetes.](https://dt-cdn.net/images/add-rule-namespace-exists-1322-3ee911844e.png)

Add a Namespace exists rule for Kubernetes.

В результате применения конфигурации Dynatrace объединит похожие процессы и сервисы с одинаковыми значениями **Product**, **Stage**, **Container name** и **Namespace**. Поскольку все эти значения идентичны, правило также обеспечивает объединение нагрузок из разных кластеров Kubernetes в одну группу процессов.