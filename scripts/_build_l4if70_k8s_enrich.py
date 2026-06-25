# -*- coding: utf-8 -*-
"""L4-IF.70 builder: k8s-enrich.md (Kubernetes enrichment use-case leaf)."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/collector/use-cases/kubernetes"
FNAME = "k8s-enrich.md"

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_DEPLOY = "How to deploy the Dynatrace OpenTelemetry Collector."
TT_CONF = "How to configure the OpenTelemetry Collector."
TT_ENRICHF = "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields."
RU_ENRICHF = "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."

TRANS = {
    # --- frontmatter / title ---
    "title: Enrich OTLP requests with Kubernetes data": "title: Обогащение запросов OTLP данными Kubernetes",
    "# Enrich OTLP requests with Kubernetes data": "# Обогащение запросов OTLP данными Kubernetes",
    # --- reading time ---
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Sep 24, 2025": "* Обновлено 24 сентября 2025 г.",
    # --- intro ---
    "The following configuration example shows how to configure a Collector instance to enrich OTLP telemetry data with additional Kubernetes metadata. This includes, for example, pod, deployment, and cluster details and allows Dynatrace to correctly map the provided telemetry data to the appropriate entities within Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для обогащения данных телеметрии OTLP дополнительными метаданными Kubernetes. Это включает, например, сведения о поде, развёртывании и кластере, что позволяет Dynatrace корректно сопоставлять предоставленные данные телеметрии с соответствующими сущностями в Dynatrace.",
    "Dynatrace recommends using ActiveGate to enhance status and performance monitoring of your Kubernetes cluster.": "Dynatrace рекомендует использовать ActiveGate для расширения мониторинга состояния и производительности вашего кластера Kubernetes.",
    "Deploying ActiveGate enables the Dynatrace Kubernetes application to visualize Kubernetes and OpenTelemetry data and map it to the corresponding Kubernetes entities.": "Развёртывание ActiveGate позволяет приложению Dynatrace Kubernetes визуализировать данные Kubernetes и OpenTelemetry и сопоставлять их с соответствующими сущностями Kubernetes.",
    # --- prerequisites ---
    "* A deployed ActiveGate for Kubernetes API monitoring Optional": "* Развёрнутый ActiveGate для мониторинга Kubernetes API (необязательно)",
    "* One of the following Collector distributions with the [Kubernetes Attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) and [Transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) processors:": "* Один из следующих дистрибутивов Collector с processor [Kubernetes Attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) и [Transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor):",
    '+ The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % TT_LEARN: '+ [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % RU_LEARN,
    '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % TT_LEARN: '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % RU_LEARN,
    '* the OTel Collector deployed in [agent mode](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "How to deploy the Dynatrace OpenTelemetry Collector.")': '* OTel Collector, развёрнутый в [режиме агента](/managed/ingest-from/opentelemetry/collector/deployment#dynatrace-docs--agent "Как развернуть Dynatrace OpenTelemetry Collector.")',
    '* The [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") of your Dynatrace environment'
    % TT_OTLP: '* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") вашей среды Dynatrace'
    % RU_OTLP,
    '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope'
    % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа'
    % RU_OTLP,
    "* [Kubernetes configured](#kubernetes-configuration) for the required role-based access control": "* [Kubernetes настроен](#kubernetes-configuration) для необходимого управления доступом на основе ролей",
    # --- see also line ---
    'See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.': 'См. [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.") и [Настройку Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector."), чтобы узнать, как настроить ваш Collector с приведённой ниже конфигурацией.',
    # --- demo configuration callout ---
    "Service account": "Service account",
    "In addition to the Collector configuration, be sure to also update your Kubernetes configuration to match the service account name used in the [RBAC file](#kubernetes-configuration) (see entries for [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).": "Помимо конфигурации Collector, необходимо также обновить конфигурацию Kubernetes, чтобы она соответствовала имени сервисного аккаунта, используемому в [файле RBAC](#kubernetes-configuration) (см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec)).",
    # --- configuration validation ---
    '[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.': '[Проверьте ваши настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "Как настроить OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.',
    # --- kubernetes configuration section ---
    "## Kubernetes configuration": "## Конфигурация Kubernetes",
    "Configure the following `rbac.yaml` file with your Kubernetes instance, to allow the OTel Collector to use the Kubernetes API with the service-account authentication type.": "Настройте следующий файл `rbac.yaml` в вашем экземпляре Kubernetes, чтобы разрешить OTel Collector использовать Kubernetes API с типом аутентификации через сервисный аккаунт.",
    # --- components section ---
    "For our configuration, we configured the following components.": "Для нашей конфигурации мы настраиваем следующие компоненты.",
    # --- receivers ---
    "Under `receivers`, we specify the standard `otlp` receiver as an active receiver component for our Collector instance.": "В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.",
    "This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).": "Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).",
    # --- processors ---
    "Under `processors`, we specify the [`k8sattributes` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) with the following parameters:": "В разделе `processors` мы указываем [processor `k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) со следующими параметрами:",
    "* `extract`—Specifies which information should be extracted.": "* `extract`: задаёт, какие сведения следует извлекать.",
    "* `pod_association`—Specifies how the pod information is linked to attributes.": "* `pod_association`: задаёт, как информация о поде связывается с атрибутами.",
    "Note that the `k8s.container.name` attribute will only be extracted if the pod from which the incoming": "Обратите внимание: атрибут `k8s.container.name` будет извлечён только в том случае, если под, из которого поступает",
    "signal has been received contains only one container, or if the ingested signal contains the `k8s.container.id` resource attribute.": "входящий сигнал, содержит только один контейнер, либо если принятый сигнал содержит атрибут ресурса `k8s.container.id`.",
    "Otherwise, the k8sattributes processor will not be able to correctly associate the correct container.": "В противном случае processor k8sattributes не сможет корректно сопоставить нужный контейнер.",
    "Dynatrace Operator enriches OpenTelemetry data from Kubernetes pods with `metadata.dynatrace.com` annotations. When these annotations are present, the `k8sattributes` processor extracts them.": "Dynatrace Operator обогащает данные OpenTelemetry из подов Kubernetes аннотациями `metadata.dynatrace.com`. При наличии этих аннотаций processor `k8sattributes` извлекает их.",
    "We also configure the [`transform` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) to have Kubernetes cluster information automatically added as resource attributes for all telemetry signals.": "Мы также настраиваем [processor `transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) для автоматического добавления информации о кластере Kubernetes в качестве атрибутов ресурса для всех сигналов телеметрии.",
    # --- exporters ---
    "Under `exporters`, we specify the default [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.": "В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации.",
    "For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.": "Для этого мы задаём следующие две переменные окружения и ссылаемся на них в значениях конфигурации `endpoint` и `Authorization`.",
    '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)'
    % TT_OTLP: '* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)'
    % RU_OTLP,
    '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s")'
    % TT_OTLP: '* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s")'
    % RU_OTLP,
    # --- service pipelines ---
    "Under `service`, we assemble our receiver, processor, and exporter objects into pipelines for traces, metrics, and logs. These pipelines allow us to send OpenTelemetry signals via the Collector instance and have them automatically enriched with additional Kubernetes-specific details.": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейеры для трассировок, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector с их автоматическим обогащением дополнительными сведениями, специфичными для Kubernetes.",
    # --- limits ---
    'Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/managed/ingest-from/opentelemetry/otlp-api "%s") and is subject to the API\'s limits and restrictions.'
    % TT_OTLP: 'Данные принимаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "%s") и подчиняются ограничениям и лимитам этого API.'
    % RU_OTLP,
    "For more information see:": "Дополнительные сведения см.:",
    '* [OpenTelemetry metrics limitations](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "%s")'
    % "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.": '* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "%s")'
    % "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.",
    '* [Dynatrace metrics mapping](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "%s")'
    % "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.": '* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "%s")'
    % "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.",
    '* [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s")'
    % "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.": '* [Приём логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "%s")'
    % "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.",
    # --- related topics ---
    '* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "%s")'
    % TT_ENRICHF: '* [Обогащение принимаемых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "%s")'
    % RU_ENRICHF,
    **S,
}

PASS = {"### Receivers", "### Processors", "### Exporters", "### Service pipelines"}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
