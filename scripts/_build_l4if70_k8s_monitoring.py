# -*- coding: utf-8 -*-
"""L4-IF.70 builder: k8s-monitoring.md (Monitor Kubernetes clusters with the OTel Collector).

File: docs/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring.md
Output: docs/managed-ru/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring.md
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/collector/use-cases/kubernetes"
FNAME = "k8s-monitoring.md"

TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_LOGAPI = (
    "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply."
)
RU_LOGAPI = "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются."
TT_METAPI = (
    "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."
)
RU_METAPI = "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются."
TT_DEPLOY = "How to deploy the Dynatrace OpenTelemetry Collector."
RU_DEPLOY = "Как развернуть Dynatrace OpenTelemetry Collector."
TT_CONFIG = "How to configure the OpenTelemetry Collector."
RU_CONFIG = "Как настроить OpenTelemetry Collector."
TT_EXPLORER = "Query for metrics and transform results to gain desired insights."
RU_EXPLORER = (
    "Запрашивайте метрики и преобразовывайте результаты для получения нужных сведений."
)
TT_DASHBOARDS = "Learn how to create, manage, and use Dynatrace Dashboards Classic."
RU_DASHBOARDS = (
    "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic."
)
TT_K8S_SETUP = "Ways to deploy and configure Dynatrace on Kubernetes"
RU_K8S_SETUP = "Способы развёртывания и настройки Dynatrace в Kubernetes"
TT_AGENT = "How to deploy the Dynatrace OpenTelemetry Collector."
RU_AGENT = "Как развернуть Dynatrace OpenTelemetry Collector."
TT_K8SMON = "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters."
RU_K8SMON = (
    "Настройте OpenTelemetry Collector для мониторинга ваших кластеров Kubernetes."
)

TRANS = {
    # --- frontmatter / title ---
    "title: Monitor Kubernetes clusters with the OTel Collector": "title: Мониторинг кластеров Kubernetes с помощью OTel Collector",
    # --- H1 (appears twice per line-parity) ---
    "# Monitor Kubernetes clusters with the OTel Collector": "# Мониторинг кластеров Kubernetes с помощью OTel Collector",
    # --- metadata bullets ---
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Nov 20, 2025": "* Обновлено 20 ноября 2025 г.",
    # --- intro paragraphs ---
    "The OTel Collector provides extensive support for Kubernetes cluster and workload monitoring. It supports various receivers to collect critical metrics about the Kubernetes cluster, nodes, and objects.": "OTel Collector обеспечивает широкую поддержку мониторинга кластеров Kubernetes и рабочих нагрузок. Он поддерживает различные компоненты receiver для сбора критически важных метрик о кластере Kubernetes, узлах и объектах.",
    'This use case explains how to set up your Collector to get full visibility into your Kubernetes clusters through [**Data Explorer**](/managed/analyze-explore-automate/explorer "%s") or custom dashboards in Dashboards Classic.'
    % TT_EXPLORER: 'Этот сценарий использования объясняет, как настроить ваш Collector для получения полной видимости в кластерах Kubernetes через [**Data Explorer**](/managed/analyze-explore-automate/explorer "%s") или пользовательские панели мониторинга в Dashboards Classic.'
    % RU_EXPLORER,
    # --- callout: Dynatrace Operator ---
    "Dynatrace Operator": "Dynatrace Operator",
    'Dynatrace recommends using the [Dynatrace Operator for Kubernetes monitoring](/managed/ingest-from/setup-on-k8s "%s").'
    % TT_K8S_SETUP: 'Dynatrace рекомендует использовать [Dynatrace Operator для мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s "%s").'
    % RU_K8S_SETUP,
    "However, this use case is designed specifically for OpenTelemetry users who choose not to deploy the Dynatrace Operator.": "Однако этот сценарий использования предназначен специально для пользователей OpenTelemetry, которые предпочитают не развёртывать Dynatrace Operator.",
    'Setting up the Collector as described below will make Kubernetes monitoring data available to be used in [Data Explorer](/managed/analyze-explore-automate/explorer "%s") and [Dashboards](/managed/analyze-explore-automate/dashboards-classic "%s").'
    % (
        TT_EXPLORER,
        TT_DASHBOARDS,
    ): 'Настройка Collector, описанная ниже, сделает данные мониторинга Kubernetes доступными для использования в [Data Explorer](/managed/analyze-explore-automate/explorer "%s") и [Dashboards](/managed/analyze-explore-automate/dashboards-classic "%s").'
    % (RU_EXPLORER, RU_DASHBOARDS),
    # --- Prerequisites section ---
    "* One of the following Collector distributions with the [Kubernetes Clusterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver), [Kubernetes Eventsï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8seventsreceiver), and [Kubelet Statsï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver) receivers:": "* Один из следующих дистрибутивов Collector с receiver [Kubernetes Cluster](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver), [Kubernetes Events](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8seventsreceiver) и [Kubelet Stats](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver):",
    '+ The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % TT_LEARN: '+ [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % RU_LEARN,
    '+ [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ [OTel Collector Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ A [custom-built OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % TT_LEARN: '+ [специально собранный OTel Collector](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % RU_LEARN,
    '* Collector deployment in [agent mode](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "%s") for node and cluster level telemetry'
    % TT_AGENT: '* Развёртывание Collector в [режиме агента](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "%s") для телеметрии уровня узла и кластера'
    % RU_AGENT,
    '* The [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") of your Dynatrace environment'
    % TT_OTLP: '* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") вашей среды Dynatrace'
    % RU_OTLP,
    '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope'
    % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа'
    % RU_OTLP,
    "* [Kubernetes configured](#kubernetes-configuration) for the required role-based access control": "* [Kubernetes, настроенный](#kubernetes-configuration) для необходимого управления доступом на основе ролей",
    'See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "%s") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "%s") on how to set these up with the configurations provided below.'
    % (
        TT_DEPLOY,
        TT_CONFIG,
    ): 'См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "%s") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "%s"), чтобы узнать, как настроить это с помощью приведённых ниже конфигураций.'
    % (RU_DEPLOY, RU_CONFIG),
    # --- Demo configurations section ---
    "## Demo configurations": "## Демонстрационные конфигурации",
    "### RBAC configuration": "### Конфигурация RBAC",
    "Configure the following `rbac.yaml` file with your Kubernetes instance, to allow the Collector to use the Kubernetes API with the service-account authentication type.": "Настройте следующий файл `rbac.yaml` для вашего экземпляра Kubernetes, чтобы разрешить Collector использовать Kubernetes API с типом аутентификации service-account.",
    "### Collector configuration": "### Конфигурация Collector",
    "Service account": "Service account",
    "In addition to the Collector configuration, be sure to also update your Kubernetes configuration to match the service account name used in the [RBAC file](#kubernetes-configuration)": "В дополнение к конфигурации Collector обязательно обновите конфигурацию Kubernetes, чтобы она соответствовала имени service account, указанному в [файле RBAC](#kubernetes-configuration)",
    "(see entries for [Helmï»¿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.127.2/charts/opentelemetry-collector/values.yaml#L245-L252) and [Operatorï»¿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).": "(см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.127.2/charts/opentelemetry-collector/values.yaml#L245-L252) и [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).",
    "Configuration validation": "Проверка конфигурации",
    '[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "%s") to avoid any configuration issues.'
    % TT_CONFIG: '[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "%s"), чтобы избежать проблем с конфигурацией.'
    % RU_CONFIG,
    "Cumulativetodelta processor recommendation": "Рекомендация по processor cumulativetodelta",
    "It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) to a value higher than how often the Collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.": "Рекомендуется устанавливать параметр `max_staleness` [processor cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor) в значение, превышающее частоту получения Collector метрик (например, как часто метрики принимаются через OTLP или каков интервал сбора Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут накапливаться в памяти с течением времени.",
    # --- Components section ---
    "For our configuration, we configured the following components:": "Для нашей конфигурации мы настроили следующие компоненты:",
    "#### Receivers": "#### Receivers",
    "Under `receivers`, we specify the following receivers as active receiver components for our deployment:": "В разделе `receivers` мы указываем следующие компоненты receiver в качестве активных компонентов для нашего развёртывания:",
    "* [`otlp`ï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver): To accept OTLP traces.": "* [`otlp`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/receiver/otlpreceiver): для приёма трассировок OTLP.",
    "* [`k8sevents`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8seventsreceiver): To receive Kubernetes events from the Kubernetes API server. [1](#fn-1-1-def)": "* [`k8sevents`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8seventsreceiver): для получения событий Kubernetes от сервера Kubernetes API. [1](#fn-1-1-def)",
    "* [`k8s_cluster`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver): To receive cluster-level metrics and entity events from the Kubernetes API server.": "* [`k8s_cluster`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/k8sclusterreceiver): для получения метрик уровня кластера и событий сущностей от сервера Kubernetes API.",
    "* [`kubeletstats`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver): To receive node-level metrics. This receiver requires the environment variable `K8S_NODE_NAME` to be set to `spec.nodeName` using the [Kubernetes Downward APIï»¿](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) (see [exampleï»¿](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)).": "* [`kubeletstats`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/kubeletstatsreceiver): для получения метрик уровня узла. Для этого receiver необходимо задать переменную окружения `K8S_NODE_NAME` со значением `spec.nodeName` с помощью [Kubernetes Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) (см. [пример](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)).",
    "1": "1",
    "The `k8sevents` receiver is currently in alpha stage and may undergo significant changes. Despite its early stage of maturity, it has been included in the Dynatrace distribution of the Collector to support early adoption and experimentation. Be aware that stability, performance, and feature completeness are not guaranteed at this stage.": "Receiver `k8sevents` в настоящее время находится на стадии альфа и может претерпевать значительные изменения. Несмотря на раннюю стадию зрелости, он включён в дистрибутив Dynatrace Collector для поддержки раннего освоения и экспериментирования. Следует учитывать, что стабильность, производительность и полнота функциональности на данном этапе не гарантированы.",
    "#### Processors": "#### Processors",
    "Under `processors`, we specify the following processors:": "В разделе `processors` мы указываем следующие компоненты processor:",
    "* [`filter`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor): To filter Kubernetes attributes.": "* [`filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor): для фильтрации атрибутов Kubernetes.",
    "* [`k8sattributes`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor): To extract and provide pod data.": "* [`k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor): для извлечения и предоставления данных подов.",
    "* [`transform`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor): To transform Kubernetes metrics. This requires the environment variable `CLUSTER_NAME` to be set with the name of the cluster. Set the variable value to an arbitrary name that you want your cluster to show up with inside Dynatrace.": "* [`transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor): для преобразования метрик Kubernetes. Для этого необходимо задать переменную окружения `CLUSTER_NAME` с именем кластера. Задайте произвольное имя, под которым кластер будет отображаться в Dynatrace.",
    "* [`cumulativetodelta`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor): To enable conversion of cumulative metrics.": "* [`cumulativetodelta`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/cumulativetodeltaprocessor): для включения преобразования кумулятивных метрик.",
    "#### Exporters": "#### Exporters",
    "Under `exporters`, we specify the [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.": "В разделе `exporters` мы указываем [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.",
    "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.",
    '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)'
    % TT_OTLP: '* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)'
    % RU_OTLP,
    '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s")'
    % TT_OTLP: '* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s")'
    % RU_OTLP,
    "#### Extensions": "#### Extensions",
    "Under `extensions`, we specify the [`k8sleaderelector` extensionï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/extension/k8sleaderelector) to choose the leader of the agent replicas, which is going to scrape and export cluster-level telemetry.": "В разделе `extensions` мы указываем [extension `k8sleaderelector`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/extension/k8sleaderelector) для выбора ведущего среди реплик агентов, который будет собирать и экспортировать телеметрию уровня кластера.",
    "This ensures that only one collector instance scrapes the data at a time to avoid telemetry duplication.": "Это гарантирует, что в каждый момент времени данные собирает только один экземпляр Collector, что позволяет избежать дублирования телеметрии.",
    "#### Service pipelines": "#### Сервисные конвейеры",
    "Under `service`, we assemble our receiver, processor, and exporter objects into pipelines for traces, metrics, and logs. These pipelines allow us to send OpenTelemetry signals via the Collector instance and have them automatically enriched with additional Kubernetes-specific details.": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейеры для трассировок, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector с их автоматическим обогащением дополнительными сведениями, специфичными для Kubernetes.",
    # --- Use Data Explorer section ---
    "## Use Data Explorer": "## Использование Data Explorer",
    "Data Explorer greatly enhances your abilities to query and visualize metrics.": "Data Explorer значительно расширяет возможности запроса и визуализации метрик.",
    'For more information, see [Data Explorer](/managed/analyze-explore-automate/explorer "%s").'
    % TT_EXPLORER: 'Дополнительные сведения см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "%s").'
    % RU_EXPLORER,
    # --- Use custom dashboards section ---
    "## Use custom dashboards": "## Использование пользовательских панелей мониторинга",
    'To set up custom dashboards, see [Dashboards](/managed/analyze-explore-automate/dashboards-classic "%s").'
    % TT_DASHBOARDS: 'Сведения о настройке пользовательских панелей мониторинга см. в разделе [Dashboards](/managed/analyze-explore-automate/dashboards-classic "%s").'
    % RU_DASHBOARDS,
    # --- Limits and limitations section (from S) ---
    # Already in S: "## Limits and limitations", the Data/metrics/logs lines, "For more information see:"
    # Already in S: the metrics limitations and logs links
    **S,
}

# Component-block headers at #### level are kept EN (Receivers/Processors/Exporters/Extensions).
# The file uses #### not ### for these sub-headers.
PASS = {
    "#### Receivers",
    "#### Processors",
    "#### Exporters",
    "#### Extensions",
}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
