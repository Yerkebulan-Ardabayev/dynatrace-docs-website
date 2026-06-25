# -*- coding: utf-8 -*-
"""L4-IF.70 builder: k8s-podlogs.md (Kubernetes pod logs use case).

Ingest Kubernetes pod logs with the OTel Collector.
REL = ingest-from/opentelemetry/collector/use-cases/kubernetes
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/collector/use-cases/kubernetes"
FNAME = "k8s-podlogs.md"

# Tooltip fragments reused from _build_otel_uc_l4if68 constants (mirrored here for key assembly)
TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
TT_K8SENR = "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."
TT_FILELOG = "Configure the OpenTelemetry Collector to ingest log data into Dynatrace."
TT_DEPLOY = "How to deploy the Dynatrace OpenTelemetry Collector."

RU_K8SENR = (
    "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes."
)
RU_FILELOG = "Настройте OpenTelemetry Collector для приёма данных логов в Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
RU_DEPLOY = "Как развернуть Dynatrace OpenTelemetry Collector."

TRANS = {
    # --- frontmatter / title ---
    "title: Ingest Kubernetes pod logs with the OTel Collector": "title: Приём логов подов Kubernetes с помощью OTel Collector",
    # --- H1 (appears twice in source) ---
    "# Ingest Kubernetes pod logs with the OTel Collector": "# Приём логов подов Kubernetes с помощью OTel Collector",
    # --- metadata bullets ---
    "* 4-min read": "* Чтение: 4 мин",
    # --- intro paragraph ---
    "The following configuration example shows how you configure a Collector instance to fetch logs from all Kubernetes pods. It also shows how to enrich the logs with Kubernetes metadata in order to automatically link OpenTelemetry services to pods and attach the logs to the Kubernetes services and pods.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для получения логов из всех подов Kubernetes. Также показано, как обогатить логи метаданными Kubernetes, чтобы автоматически связать сервисы OpenTelemetry с подами и прикрепить логи к сервисам и подам Kubernetes.",
    # --- Prerequisites section ---
    "* A deployed ActiveGate for Kubernetes API monitoring": "* Развёрнутый ActiveGate для мониторинга Kubernetes API",
    "* One of the following Collector distributions with the [Filelog](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver) receiver and the [Kubernetes Attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) processor:": "* Один из следующих дистрибутивов Collector с [receiver Filelog](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver) и [processor Kubernetes Attributes](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor):",
    "* the OTel Collector deployed on each node": "* OTel Collector, развёрнутый на каждом узле",
    '* The [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") of your Dynatrace environment'
    % TT_OTLP: '* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") вашей среды Dynatrace'
    % RU_OTLP,
    '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope'
    % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа'
    % RU_OTLP,
    "* [Kubernetes configured](#kubernetes-configuration) for the required role-based access control": "* [Kubernetes настроен](#kubernetes-configuration) для обязательного управления доступом на основе ролей",
    '* Kubernetes Secrets set up as shown in [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "%s")'
    % TT_DEPLOY: '* Kubernetes Secrets настроены, как показано в разделе [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "%s")'
    % RU_DEPLOY,
    # --- Demo configuration section ---
    "Kubernetes configuration": "Конфигурация Kubernetes",
    'This sample configuration uses the same Kubernetes enrichment approach as the use case at [Enrich OTLP requests with Kubernetes data](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "%s").'
    % TT_K8SENR: 'В данном примере конфигурации используется тот же подход к обогащению данными Kubernetes, что и в сценарии использования [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "%s").'
    % RU_K8SENR,
    "In addition to the Collector configuration, be sure to also update your Kubernetes configuration for the following components:": "В дополнение к конфигурации Collector обязательно обновите конфигурацию Kubernetes для следующих компонентов:",
    "* **Service account**: Specify the same service account name used in the [RBAC file](#kubernetes-configuration) (see entries for [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))": "* **Service account**: укажите то же имя сервисного аккаунта, что используется в [файле RBAC](#kubernetes-configuration) (см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L184-L191), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))",
    "* **Mounted volumes**: Specify the file system volumes where your Kubernetes host keeps the relevant log files (see entries for [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L241), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))": "* **Смонтированные тома**: укажите тома файловой системы, в которых ваш хост Kubernetes хранит соответствующие файлы логов (см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L241), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))",
    "* **Mount paths**: Specify the file system paths, to which the previously configured volumes should be mounted within the container (see entries for [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L244), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))": "* **Пути монтирования**: укажите пути файловой системы, по которым ранее настроенные тома должны монтироваться внутри контейнера (см. записи для [Helm](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.100.0/charts/opentelemetry-collector/values.yaml#L244), [Operator](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md#opentelemetrycollectorspec))",
    # --- Kubernetes configuration section ---
    "## Kubernetes configuration": "## Конфигурация Kubernetes",
    "Configure the following `rbac.yaml` file with your Kubernetes instance, to allow the OTel Collector to use the Kubernetes API with the service-account authentication type.": "Настройте следующий файл `rbac.yaml` для своего экземпляра Kubernetes, чтобы разрешить OTel Collector использовать Kubernetes API с типом аутентификации на основе сервисного аккаунта.",
    # --- GKE Autopilot section ---
    "Configuration for GKE Autopilot or AWS EKS": "Конфигурация для GKE Autopilot или AWS EKS",
    "If you are running the Collector on GKE Autopilot or AWS EKS, you need the following adjustments in the configuration:": "При запуске Collector в GKE Autopilot или AWS EKS необходимы следующие изменения в конфигурации:",
    '* **Deployment mode**: The Collector needs to be deployed as a DaemonSet to be able to access the pod log files on the host. For details on deploying the Collector as a DaemonSet, see [Deployment instructions](/managed/ingest-from/opentelemetry/collector/deployment "%s").'
    % TT_DEPLOY: '* **Режим развёртывания**: Collector необходимо развернуть как DaemonSet, чтобы иметь возможность обращаться к файлам логов подов на хосте. Подробнее о развёртывании Collector как DaemonSet см. в разделе [Инструкции по развёртыванию](/managed/ingest-from/opentelemetry/collector/deployment "%s").'
    % RU_DEPLOY,
    "* **Volume mount**: Volume mounts to `/var/log/pods` are required to be read-only, otherwise the Collector will not be able to access the log files": "* **Монтирование тома**: монтирование томов к `/var/log/pods` должно быть доступно только для чтения, иначе Collector не сможет обратиться к файлам логов",
    "within that directory.": "в этом каталоге.",
    "Below is an example configuration for a Collector DaemonSet with the required volume mounts for gathering the pod logs:": "Ниже приведён пример конфигурации DaemonSet Collector с необходимыми монтированиями томов для сбора логов подов:",
    # --- Components section ---
    "For our configuration, we configured the following components.": "Для нашей конфигурации мы настраиваем следующие компоненты.",
    # --- Receivers description ---
    "Under `receivers`, we specify the `filelog` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем receiver `filelog` в качестве активного компонента receiver для нашего экземпляра Collector.",
    "The Filelog receiver supports a number of [configuration parameters](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver/README.md), which enable you to customize its behavior. For the example, we use the following:": "Receiver Filelog поддерживает ряд [параметров конфигурации](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/receiver/filelogreceiver/README.md), позволяющих настроить его поведение. В данном примере мы используем следующие:",
    "* `include`—Specifies the path pattern of the files we want to ingest.": "* `include`: задаёт шаблон пути к файлам, которые мы хотим принимать.",
    "* `start_at`—Specifies if the receiver should read from the beginning of the file or, for the most recent entries only, the end.": "* `start_at`: задаёт, должен ли receiver читать с начала файла или, только для самых последних записей, с конца.",
    "* `operators`—Configures the [`container`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/container.md) operator, which automatically parses each log entry.": "* `operators`: настраивает оператор [`container`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/stanza/docs/operators/container.md), который автоматически разбирает каждую запись лога.",
    # --- Processors description ---
    "Under `processors`, we specify the [`k8sattributes` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) with the following parameters:": "В разделе `processors` мы указываем [processor `k8sattributes`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/k8sattributesprocessor) со следующими параметрами:",
    "* `extract`—Specifies which information should be extracted.": "* `extract`: задаёт, какая информация должна извлекаться.",
    "* `pod_association`—Specifies how the pod information is linked to attributes.": "* `pod_association`: задаёт, как сведения о поде привязываются к атрибутам.",
    # --- Exporters description ---
    "Under `exporters`, we specify the default [`otlp_http` exporter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token, as set up and configured under [Kubernetes Secrets](#kubernetes-secrets).": "В разделе `exporters` мы указываем стандартный [exporter `otlp_http`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/exporter/otlphttpexporter) и настраиваем его с помощью URL нашего Dynatrace API и необходимого токена аутентификации, настроенного в разделе [Kubernetes Secrets](#kubernetes-secrets).",
    # --- Service pipelines description ---
    "Under `service`, we assemble our receiver, processor, and exporter objects into pipelines for traces, metrics, and logs. These pipelines allow us to send OpenTelemetry signals via the Collector instance and have them automatically enriched with additional Kubernetes-specific details.": "В разделе `service` мы собираем объекты receiver, processor и exporter в конвейеры для трассировок, метрик и логов. Эти конвейеры позволяют отправлять сигналы OpenTelemetry через экземпляр Collector и автоматически обогащать их дополнительными сведениями, специфичными для Kubernetes.",
    # --- Related topics ---
    '* [Ingest logs from files with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "%s")'
    % TT_FILELOG: '* [Приём логов из файлов с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "%s")'
    % RU_FILELOG,
    **S,
}

# EN-kept component section headers (no Russian translation needed)
PASS = {"### Receivers", "### Processors", "### Exporters"}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
