# -*- coding: utf-8 -*-
"""L4-IF.70 builder: ingest-from/opentelemetry/collector/deployment.md"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/collector"
FNAME = "deployment.md"

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."

TT_CONF = "How to configure the OpenTelemetry Collector."
RU_CONF = "Как настроить OpenTelemetry Collector."

TT_K8SENR = "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."
RU_K8SENR = (
    "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes."
)

TRANS = {
    # frontmatter title
    "title: Deploy the Dynatrace OTel Collector": "title: Развёртывание Dynatrace OTel Collector",
    # page heading (appears twice)
    "# Deploy the Dynatrace OTel Collector": "# Развёртывание Dynatrace OTel Collector",
    # metadata bullets
    "* 9-min read": "* Чтение: 9 мин",
    "* Updated on Apr 10, 2026": "* Обновлено 10 апреля 2026 г.",
    # intro
    'This page describes how to deploy the Dynatrace distribution of the OTel Collector ("Dynatrace OTel Collector").': "На этой странице описано, как развернуть дистрибутив Dynatrace OTel Collector.",
    # Deployment modes section
    "## Deployment modes": "## Режимы развёртывания",
    "The Dynatrace OTel Collector can be [deployed](https://opentelemetry.io/docs/collector/quick-start/) as a standalone agent or gateway.": "Dynatrace OTel Collector можно [развернуть](https://opentelemetry.io/docs/collector/quick-start/) как автономный агент или шлюз.",
    "For illustrative purposes, the graphics below show the modes in a Kubernetes setup, but the same modes can also be used outside of Kubernetes.": "Для наглядности на рисунках ниже режимы показаны в среде Kubernetes, но те же режимы можно использовать и за пределами Kubernetes.",
    "Agent": "Агент",
    "Gateway": "Шлюз",
    "As an agent, the Dynatrace OTel Collector is deployed either with the application or on the same host as the application. This Dynatrace OTel Collector can receive telemetry data and enhance it with, for example, tags or infrastructure information.": "В режиме агента Dynatrace OTel Collector развёртывается вместе с приложением или на том же хосте, что и приложение. В этом режиме Dynatrace OTel Collector принимает данные телеметрии и дополняет их, например, тегами или информацией об инфраструктуре.",
    "![OTel Collector as agent](https://cdn.bfldr.com/B686QPH3/as/2h9fmzj68vw6vgts9t38hp/Collector_deployment_Agent_-_Light_Mode?auto=webp&format=png&position=1)": "![OTel Collector as agent](https://cdn.bfldr.com/B686QPH3/as/2h9fmzj68vw6vgts9t38hp/Collector_deployment_Agent_-_Light_Mode?auto=webp&format=png&position=1)",
    "OTel Collector as agent": "OTel Collector в режиме агента",
    "As a gateway, one or more Dynatrace OTel Collector instances can be deployed as standalone services. This Dynatrace OTel Collector can be deployed additionally, for example, per cluster, region, or data center. A load balancer can help scale the independently operating Dynatrace OTel Collector instances.": "В режиме шлюза один или несколько экземпляров Dynatrace OTel Collector развёртываются как автономные сервисы. Dynatrace OTel Collector в этом режиме можно развернуть дополнительно, например, на уровне кластера, региона или центра обработки данных. Балансировщик нагрузки помогает масштабировать независимо работающие экземпляры Dynatrace OTel Collector.",
    "![OTel Collector as gateway](https://cdn.bfldr.com/B686QPH3/as/ghvnk47j6phmrjjnv859chxr/Collector_deployment_Gateway_-_Light_Mode?auto=webp&format=png&position=1)": "![OTel Collector as gateway](https://cdn.bfldr.com/B686QPH3/as/ghvnk47j6phmrjjnv859chxr/Collector_deployment_Gateway_-_Light_Mode?auto=webp&format=png&position=1)",
    "OTel Collector as gateway": "OTel Collector в режиме шлюза",
    "It's also possible to combine these deployment modes and chain Dynatrace OTel Collector instances. Consider this if you're deploying the Dynatrace OTel Collector in large environments.": "Также можно комбинировать эти режимы развёртывания и выстраивать экземпляры Dynatrace OTel Collector в цепочку. Это стоит рассмотреть при развёртывании Dynatrace OTel Collector в больших средах.",
    # Deployment options section
    "## Deployment options": "## Варианты развёртывания",
    "The Dynatrace OTel Collector can be deployed for the following platforms:": "Dynatrace OTel Collector можно развернуть на следующих платформах:",
    "* [Kubernetes](#kubernetes)": "* [Kubernetes](#kubernetes)",
    "* [Docker](#docker)": "* [Docker](#docker)",
    "* [Windows, macOS, and Linux](#binary)": "* [Windows, macOS и Linux](#binary)",
    "* [Linux installer packages](#linux-installer-packages)": "* [Установочные пакеты Linux](#linux-installer-packages)",
    # Kubernetes subsection
    "### Kubernetes": "### Kubernetes",
    "For Kubernetes, the Dynatrace OTel Collector can be deployed in the following ways:": "Для Kubernetes Dynatrace OTel Collector можно развернуть следующими способами:",
    "* OpenTelemetry Kubernetes Operator": "* OpenTelemetry Kubernetes Operator",
    "* Helm": "* Helm",
    "* Raw manifest": "* Raw manifest",
    # Dynatrace access details
    "#### Dynatrace access details": "#### Параметры доступа Dynatrace",
    "Before you deploy the Dynatrace OTel Collector, you need to set up the necessary Kubernetes secrets for the Dynatrace access details.": "Перед развёртыванием Dynatrace OTel Collector необходимо настроить секреты Kubernetes с параметрами доступа к Dynatrace.",
    'Use kubectl to create Kubernetes secrets for the Dynatrace export details. Replace the placeholders (indicated by curly brackets) with the actual values for [the export URL and the API token](/managed/ingest-from/opentelemetry/otlp-api "%s").'
    % TT_OTLP: 'С помощью kubectl создайте секреты Kubernetes с данными экспорта в Dynatrace. Замените заполнители (указанные в фигурных скобках) фактическими значениями [URL экспорта и API-токена](/managed/ingest-from/opentelemetry/otlp-api "%s").'
    % RU_OTLP,
    # Kubernetes deployment variants
    "#### Kubernetes deployment variants": "#### Варианты развёртывания в Kubernetes",
    "The following sample configurations apply a resource limit of 512 megabytes. You may need to adjust this under `resources.limits.memory` for your particular use case.": "Приведённые ниже примеры конфигураций устанавливают ограничение ресурсов в 512 мегабайт. Для конкретного сценария использования это значение может потребоваться изменить в разделе `resources.limits.memory`.",
    "OpenTelemetry Operator": "OpenTelemetry Operator",
    "Helm": "Helm",
    "Raw manifest": "Raw manifest",
    # Prerequisites for Operator
    "#### Prerequisites": "#### Предварительные требования",
    "If you haven't installed OpenTelemetry Operator yet, first make sure [cert-manager](https://cert-manager.io/docs/installation/) is installed. Afterwards, you can deploy Operator with the following `kubectl` command:": "Если OpenTelemetry Operator ещё не установлен, сначала убедитесь, что установлен [cert-manager](https://cert-manager.io/docs/installation/). После этого можно развернуть Operator с помощью следующей команды `kubectl`:",
    "After the installation, deploy the Dynatrace OTel Collector either in [gateway or agent deployment mode](#deployment-modes), with one of the following configuration samples. Save it as `crd-dynatrace-collector.yaml` and deploy it with `kubectl apply`.": "После установки разверните Dynatrace OTel Collector в режиме [шлюза или агента](#deployment-modes), используя один из приведённых ниже примеров конфигурации. Сохраните файл как `crd-dynatrace-collector.yaml` и примените его командой `kubectl apply`.",
    "Custom Resource Definition": "Custom Resource Definition",
    "The Kubernetes CRD of the Operator can be found on [GitHub](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md).": "Kubernetes CRD для Operator можно найти на [GitHub](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md).",
    "Deploy as a gateway (Deployment)": "Развернуть как шлюз (Deployment)",
    "Deploy as an agent (DaemonSet)": "Развернуть как агент (DaemonSet)",
    "Choose one of the common [deployment modes](#deployment-modes) for the Dynatrace OTel Collector.": "Выберите один из стандартных [режимов развёртывания](#deployment-modes) для Dynatrace OTel Collector.",
    "The Helm charts below use `alternateConfig` to provide the Dynatrace OTel Collector configuration. With this entry, the default Helm chart configuration, as well as a possibly present `config` object, will be ignored.": "Представленные ниже Helm-чарты используют `alternateConfig` для передачи конфигурации Dynatrace OTel Collector. При использовании этого параметра стандартная конфигурация Helm-чарта, а также объект `config`, если он присутствует, будут проигнорированы.",
    # Helm steps
    "1. Save the following YAML configuration under `values-deployment.yaml`": "1. Сохраните следующую конфигурацию YAML в файл `values-deployment.yaml`",
    "2. Run the following commands to configure and install the Helm charts": "2. Выполните следующие команды для настройки и установки Helm-чартов",
    "1. Save the following YAML configuration under `values-daemonset.yaml`.": "1. Сохраните следующую конфигурацию YAML в файл `values-daemonset.yaml`.",
    "2. Run the following commands to configure and install the Helm charts.": "2. Выполните следующие команды для настройки и установки Helm-чартов.",
    # Network ports / Service / ConfigMap / Manifest tabs
    "Network ports": "Сетевые порты",
    "Make sure to configure and forward all relevant network ports, using the [`ports` configuration value](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).": "Обязательно настройте и пробросьте все необходимые сетевые порты, используя [значение конфигурации `ports`](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).",
    "Service": "Service",
    "Use `kubectl apply` with the following configuration to set up the service definitions and configure the correct ports.": "Примените следующую конфигурацию с помощью `kubectl apply`, чтобы создать определения сервиса и настроить нужные порты.",
    "ConfigMap": "ConfigMap",
    "Create a `ConfigMap` by applying the following configuration with `kubectl apply` to set up the Dynatrace OTel Collector configuration.": "Создайте `ConfigMap`, применив следующую конфигурацию с помощью `kubectl apply`, чтобы задать конфигурацию Dynatrace OTel Collector.",
    "Manifest": "Manifest",
    "Apply the following manifest configuration with `kubectl apply` to create the Dynatrace OTel Collector Deployment in [gateway mode](#deployment-modes).": "Примените следующую конфигурацию манифеста с помощью `kubectl apply`, чтобы создать Deployment Dynatrace OTel Collector в [режиме шлюза](#deployment-modes).",
    # Service account
    "Service account": "Сервисный аккаунт",
    'In Kubernetes, it is common to enrich OpenTelemetry signals using the [Kubernetes Attributes processor](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "%s"). This requires a Kubernetes service account, which is automatically configured when using Operator or Helm.'
    % TT_K8SENR: 'В Kubernetes принято обогащать сигналы OpenTelemetry с помощью [processor Kubernetes Attributes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "%s"). Для этого требуется сервисный аккаунт Kubernetes, который автоматически настраивается при использовании Operator или Helm.'
    % RU_K8SENR,
    "For raw manifests, this needs to be configured manually by adding a `spec.serviceAccountName: collector` entry to the deployment manifest.": "При использовании raw-манифестов это необходимо настраивать вручную, добавив запись `spec.serviceAccountName: collector` в манифест развёртывания.",
    # Docker section
    "### Docker": "### Docker",
    "Run the following command to download the most recent Dynatrace OTel Collector image:": "Выполните следующую команду для загрузки актуального образа Dynatrace OTel Collector:",
    'Next, ensure that the [Dynatrace OTel Collector configuration file](/managed/ingest-from/opentelemetry/collector/configuration "%s") exists in the current working directory and run the Dynatrace OTel Collector image with the following command:'
    % TT_CONF: 'Убедитесь, что [файл конфигурации Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "%s") находится в текущей рабочей директории, и запустите образ Dynatrace OTel Collector следующей командой:'
    % RU_CONF,
    "The `-v` parameter maps the local configuration file to the given container path, which is subsequently passed to the `--config` parameter.": "Параметр `-v` сопоставляет локальный файл конфигурации с указанным путём в контейнере, который затем передаётся в параметр `--config`.",
    "Make sure to map all required network ports with the [`-p` parameter](https://docs.docker.com/reference/cli/docker/container/run/#publish). For example, if you accept OTLP gRPC requests on the default port, you need to specify port 4317. For OTLP over HTTP specify port 4318.": "Обязательно пробросьте все необходимые сетевые порты с помощью [параметра `-p`](https://docs.docker.com/reference/cli/docker/container/run/#publish). Например, если принимаются запросы OTLP gRPC через порт по умолчанию, необходимо указать порт 4317. Для OTLP по HTTP укажите порт 4318.",
    # Docker compose
    "#### Docker compose": "#### Docker compose",
    "Use the following configuration in your compose file to deploy and run the Dynatrace OTel Collector image:": "Используйте следующую конфигурацию в файле compose для развёртывания и запуска образа Dynatrace OTel Collector:",
    "In the example above, `ports` is configured for gRPC and HTTP. Adjust the list of ports according to your specific use case.": "В приведённом примере `ports` настроен для gRPC и HTTP. Скорректируйте список портов в соответствии с конкретным сценарием использования.",
    # Windows / macOS / Linux section
    "### Windows, macOS, and Linux": "### Windows, macOS и Linux",
    "To install the Dynatrace OTel Collector binary manually:": "Чтобы установить бинарный файл Dynatrace OTel Collector вручную:",
    "1. Download the [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.48.0) for your operating system from GitHub.": "1. Загрузите [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.48.0) для своей операционной системы с GitHub.",
    "2. Decompress the archive file.": "2. Распакуйте архивный файл.",
    "3. Set up the desired configuration and save it to `otel-collector-config.yaml`.": "3. Настройте нужную конфигурацию и сохраните её в файл `otel-collector-config.yaml`.",
    "4. Run the `dynatrace-otel-collector` binary and pass the path to the configuration file using the `--config` parameter.": "4. Запустите бинарный файл `dynatrace-otel-collector` и передайте путь к файлу конфигурации с помощью параметра `--config`.",
    # Linux installer packages section
    "### Linux installer packages": "### Установочные пакеты Linux",
    "Dynatrace also provides DEB and RPM installer packages for Linux systems on x86-64 and ARM64 architectures.": "Dynatrace также предоставляет установочные пакеты DEB и RPM для Linux-систем на архитектурах x86-64 и ARM64.",
    "Required init system": "Требуемая система инициализации",
    "The installer packages require Systemd to be the active init system.": "Установочные пакеты требуют, чтобы активной системой инициализации был Systemd.",
    "To deploy the Dynatrace OTel Collector using an installer package, download the [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.48.0) for your operating system from GitHub, and install it using root privileges and the following commands.": "Для развёртывания Dynatrace OTel Collector с помощью установочного пакета загрузите [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.48.0) для своей операционной системы с GitHub и установите с правами суперпользователя, используя следующие команды.",
    "Replace the following two placeholders in the commands with their actual content:": "Замените в командах следующие два заполнителя их фактическими значениями:",
    "* `<VERSION>`: Replace with the version tag of the download.": "* `<VERSION>`: замените тегом версии загружаемого файла.",
    "* `<ARCH>`: Replace with the system architecture tag (that is, `x86_64` or `arm64`) of the download.": "* `<ARCH>`: замените тегом архитектуры системы (то есть `x86_64` или `arm64`) загружаемого файла.",
    "Debian (.deb)": "Debian (.deb)",
    "Red Hat (.rpm)": "Red Hat (.rpm)",
    # Service configuration subsection
    "#### Service configuration": "#### Конфигурация сервиса",
    'When first starting the service, it may fail to start if there is no [configuration file](/managed/ingest-from/opentelemetry/collector/configuration "%s") in place yet. By default, the Dynatrace OTel Collector attempts to find the file at `/etc/dynatrace-otel-collector/config.yaml`.'
    % TT_CONF: 'При первом запуске сервис может не запуститься, если [файл конфигурации](/managed/ingest-from/opentelemetry/collector/configuration "%s") ещё не создан. По умолчанию Dynatrace OTel Collector пытается найти файл по пути `/etc/dynatrace-otel-collector/config.yaml`.'
    % RU_CONF,
    "Custom configuration location": "Нестандартное расположение конфигурации",
    "If you wish to use a different path, you can override the default path with the `--config` parameter as part of the `OTELCOL_OPTIONS` variable in the Systemd environment file at `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:": "Если нужно использовать другой путь, можно переопределить путь по умолчанию с помощью параметра `--config` в составе переменной `OTELCOL_OPTIONS` в файле среды Systemd по пути `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:",
    "Subsequent package updates will replace this file, so be sure to back up and restore its content during an update of the Dynatrace OTel Collector package. Alternatively, you can override the configuration with the [`systemctl edit` command](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).": "При последующих обновлениях пакета этот файл будет заменён, поэтому во время обновления пакета Dynatrace OTel Collector обязательно сделайте резервную копию и восстановите его содержимое. Также можно переопределить конфигурацию с помощью [команды `systemctl edit`](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).",
    "To see all available configuration options, run the Dynatrace OTel Collector binary with the `--help` parameter.": "Чтобы просмотреть все доступные параметры конфигурации, запустите бинарный файл Dynatrace OTel Collector с параметром `--help`.",
    "After changing the configuration, make sure to restart the service using the following command and root privileges:": "После изменения конфигурации перезапустите сервис следующей командой с правами суперпользователя:",
    # Service status subsection
    "#### Service status": "#### Статус сервиса",
    "To view the current status of the Dynatrace OTel Collector service, run the following command with root privileges:": "Чтобы просмотреть текущий статус сервиса Dynatrace OTel Collector, выполните следующую команду с правами суперпользователя:",
    "To check the output of the Dynatrace OTel Collector service, run the following command with root privileges:": "Чтобы проверить вывод сервиса Dynatrace OTel Collector, выполните следующую команду с правами суперпользователя:",
    # Container image registries section
    "## Container image registries": "## Реестры образов контейнеров",
    "Container images for the Dynatrace OTel Collector:": "Образы контейнеров для Dynatrace OTel Collector:",
    "* [GitHub Container Registry (GHCR)](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)": "* [GitHub Container Registry (GHCR)](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)",
    "+ `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0`": "+ `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0`",
    "* [Amazon Elastic Container Registry (Amazon ECR)](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)": "* [Amazon Elastic Container Registry (Amazon ECR)](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)",
    "+ `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.48.0`": "+ `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.48.0`",
    "* [Docker Hub Container Registry](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)": "* [Docker Hub Container Registry](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)",
    "+ `dynatrace/dynatrace-otel-collector:0.48.0`": "+ `dynatrace/dynatrace-otel-collector:0.48.0`",
    **S,
}

PASS = set()  # no EN-kept lines outside of code fences for this file

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
