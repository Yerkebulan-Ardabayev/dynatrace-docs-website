# -*- coding: utf-8 -*-
"""
L4-IF.35 hub builder: 5 GCP hub/index pages (manual 1:1 prose).

  gcp-integrations/gcp-functions.md                     (34)
  gcp-integrations/google-compute-engine.md             (25)
  gcp-integrations/google-app-engine.md                 (88)
  gcp-integrations/gcp-guide.md                          (55)
  gcp-integrations/gcp-supported-service-metrics-new.md (98)

Written through this script (binary, LF, no trailing newline, no BOM) instead of
the editor so the markdown formatter never reflows tables / wraps prose / breaks
line-parity.

Build-time guards (fail-fast): line-parity, per-line URL-set identity (URLs are
only ever copied), no em-dash, no mojibake in RU, every non-structural EN line
either translated or an explicit passthrough (else reported UNMATCHED).

EN source carries doubly-decoded scrape mojibake. clean() normalizes the lookup
key; the artifacts are written as \\uXXXX escapes (hexdump-verified) so no raw
mojibake ever sits in this source file. RU output is clean; passthrough lines
keep their original EN bytes.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_EN = os.path.join(ROOT, "docs", "managed", "ingest-from", "google-cloud-platform")
BASE_RU = os.path.join(
    ROOT, "docs", "managed-ru", "ingest-from", "google-cloud-platform"
)

URL_RE = re.compile(r"\]\(([^)\s]+)")
EMDASH = "—"

# Doubly-encoded UTF-8 scrape artifacts as they decode in the files (hexdump-
# verified): BOM EF BB BF -> U+00EF U+00BB U+00BF; smart punct E2 80 xx -> U+00E2 ..
_MJ = [
    ("ï»¿", ""),
    ("â", "'"),
    ("â", "'"),
    ("â", '"'),
    ("â", '"'),
    ("â", "-"),
    ("â", "-"),
]
# RU-output mojibake detector: lead bytes U+00E2/U+00EF/U+00C3 and C1 controls
# never occur in correct Russian. Guillemets U+00AB/U+00BB are legitimate and
# deliberately NOT listed.
MOJI = ["â", "ï", "Ã"] + [chr(c) for c in range(0x80, 0xA0)]


def clean(s):
    for bad, good in _MJ:
        s = s.replace(bad, good)
    return s


# ---------------------------------------------------------------- shared maps
COMMON = {
    "* Overview": "* Обзор",
    "* How-to guide": "* Практическое руководство",
    "## Related topics": "## Связанные темы",
    "## Prerequisites": "## Предварительные условия",
    "## Monitoring consumption": "## Потребление мониторинга",
    "### Metric ingestion": "### Приём метрик",
    "### Log ingestion": "### Приём логов",
    '* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")': '* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")',
    '* [Google Cloud integrations](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")': '* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")',
    '* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': '* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в разных операционных системах и на разных платформах.")',
    'All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").': 'Все облачные сервисы потребляют DDU. Объём потребления DDU на один экземпляр сервиса зависит от числа отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU). Подробнее см. [Расширение Dynatrace (единицы Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление при мониторинге Dynatrace на основе единиц Davis data units (DDU).").',
    'DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.': 'Потребление DDU применяется к облачному Log Monitoring. Подробнее см. [DDU для Log Monitoring Classic](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").',
}

GCP_FUNCTIONS = {
    "title: Google Cloud Functions monitoring": "title: Мониторинг Google Cloud Functions",
    "# Google Cloud Functions monitoring": "# Мониторинг Google Cloud Functions",
    "* 1-min read": "* Чтение: 1 мин",
    "* Updated on Jul 19, 2023": "* Обновлено 19 июля 2023 г.",
    'Google Cloud Functions lets you run your code without provisioning or managing servers. This deployment model is sometimes referred to as "serverless" or "Function as a Service" (FaaS).': "Google Cloud Functions позволяет запускать код без выделения серверов и управления ими. Эту модель развёртывания иногда называют «бессерверной» (serverless) или «функцией как услугой» (Function as a Service, FaaS).",
    "* A Google Cloud Function runs in an application on a container managed by Google. This lets you focus on writing code without worrying about the underlying application or infrastructure.": "* Google Cloud Function выполняется в приложении на контейнере, управляемом Google. Это позволяет сосредоточиться на написании кода, не заботясь о нижележащем приложении или инфраструктуре.",
    "* Google Cloud Functions are ephemeral. This means that the underlying container can be suspended or recycled when there's no request pending.": "* Google Cloud Functions эфемерны. Это значит, что нижележащий контейнер может быть приостановлен или переиспользован, когда нет ожидающих запросов.",
    "## Integration": "## Интеграция",
    '* [Integrate on Google Cloud Functions Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")': '* [Интеграция в Google Cloud Functions Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Node.js и Dynatrace.")',
    '* [Integrate on Google Cloud Functions Python](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Monitor Google Cloud Functions with OpenTelemetry for Python and Dynatrace.")': '* [Интеграция в Google Cloud Functions Python](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Python и Dynatrace.")',
    '* [Integrate on Google Cloud Functions GoLang](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Monitor Google Cloud Functions with OpenTelemetry for Go and Dynatrace.")': '* [Интеграция в Google Cloud Functions GoLang](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Go и Dynatrace.")',
    '* [Integrate on Google Cloud Functions .NET](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")': '* [Интеграция в Google Cloud Functions .NET](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Мониторинг Google Cloud Functions с помощью OpenTelemetry для .NET и Dynatrace.")',
    '* [Google Cloud Functions monitoring](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")': '* [Мониторинг Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Мониторинг Google Cloud Functions и просмотр доступных метрик.")',
    'For Google Cloud Functions, monitoring consumption is based on Davis data units. See [Serverless monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details.': 'Для Google Cloud Functions потребление при мониторинге рассчитывается в единицах Davis data units. Подробнее см. [DDU для бессерверных функций](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление при бессерверном мониторинге.").',
    "* [Google Cloud monitoring](https://www.dynatrace.com/technologies/google-cloud-monitoring/)": "* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)",
}

COMPUTE_ENGINE = {
    "title: Monitor Google Compute Engine": "title: Мониторинг Google Compute Engine",
    "# Monitor Google Compute Engine": "# Мониторинг Google Compute Engine",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Oct 03, 2018": "* Опубликовано 3 октября 2018 г.",
    "## Deploy OneAgent": "## Развёртывание OneAgent",
    'Monitoring Google Compute Engine instances works out-of-the-box by just running the regular [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.") and [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Learn how to download and install Dynatrace OneAgent on Windows.") OneAgent installers. You\'ll get full-stack visibility, from hosts to processes and services layer.': 'Мониторинг инстансов Google Compute Engine работает «из коробки»: достаточно запустить обычные установщики OneAgent для [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Узнайте, как загрузить и установить Dynatrace OneAgent в Linux.") и [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Узнайте, как загрузить и установить Dynatrace OneAgent в Windows."). Вы получите полную видимость всего стека: от хостов до уровня процессов и сервисов.',
    "## Update OneAgent": "## Обновление OneAgent",
    'You can update OneAgent by running regular [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.") and [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.") OneAgent update.': 'Обновить OneAgent можно с помощью обычного обновления OneAgent для [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent в Linux.") и [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Узнайте о различных способах обновления Dynatrace OneAgent в Windows.").',
    '* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': '* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в разных операционных системах и на разных платформах.")',
}

APP_ENGINE = {
    "title: Monitor Google App Engine": "title: Мониторинг Google App Engine",
    "# Monitor Google App Engine": "# Мониторинг Google App Engine",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jun 23, 2020": "* Опубликовано 23 июня 2020 г.",
    "The Google App Engine standard environment type supports applications that run on Java, .NET, Node.js, Golang, and more. For custom Docker images, Google App Engine provides flexible environment support.": "Стандартный тип окружения Google App Engine поддерживает приложения, работающие на Java, .NET, Node.js, Golang и других технологиях. Для собственных образов Docker Google App Engine предоставляет поддержку гибкого окружения (flexible environment).",
    '* Create a [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").': '* Создайте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей действия (scopes).").',
    '* Review the list of [supported applications and versions](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").': '* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").',
    "## Integrate OneAgent into the application image": "## Интеграция OneAgent в образ приложения",
    "To integrate OneAgent into a container deployment with a Dockerfile in Google App Engine flexible environment and activate instrumentation of your application, add the commands below to your current Dockerfile, making sure to enter your own values for the `DT_API_URL`, `DT_API_TOKEN`, and `DT_ONEAGENT_OPTIONS` arguments.": "Чтобы интегрировать OneAgent в развёртывание контейнера с Dockerfile в гибком окружении Google App Engine и активировать инструментирование приложения, добавьте приведённые ниже команды в текущий Dockerfile, указав собственные значения для аргументов `DT_API_URL`, `DT_API_TOKEN` и `DT_ONEAGENT_OPTIONS`.",
    "* `<environmentID>` should be replaced with your Dynatrace environment ID. If you're using Dynatrace Managed, you need to provide your Dynatrace Server URL (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).": "* `<environmentID>` нужно заменить идентификатором вашей среды Dynatrace. Если вы используете Dynatrace Managed, необходимо указать URL вашего Dynatrace Server (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).",
    "* `<token>`should be replaced with the PaaS token mentioned in the prerequisites.": "* `<token>` нужно заменить PaaS-токеном, указанным в предварительных условиях.",
    "* Technology support is enabled via `include` parameters. Valid options for `flavor=default` are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` and `go`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package. For Alpine Linux based environments, Dynatrace OneAgent supports the flavor `musl`. Valid options for `flavor=musl` are `all`, `go`, `java`, `apache`, `nginx`, and `nodejs`.": "* Поддержка технологий включается через параметры `include`. Допустимые значения для `flavor=default`: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` и `go`. Подключение отдельных опций поддержки технологий вместо поддержки всех технологий уменьшает размер пакета OneAgent. Для окружений на базе Alpine Linux Dynatrace OneAgent поддерживает flavor `musl`. Допустимые значения для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.",
    "The `wget` and `unzip` commands above might fail if they aren't provided by the base image.": "Приведённые выше команды `wget` и `unzip` могут не сработать, если они не предоставляются базовым образом.",
    "## Deploy the application image": "## Развёртывание образа приложения",
    "After integrating the OneAgent into the application Docker file, deploy the application. In order to do this, switch to the directory of the application that contains the `Dockerfile` and the `app.yaml` file, and run the following command in the `gcloud` CLI.": "После интеграции OneAgent в Docker-файл приложения разверните приложение. Для этого перейдите в каталог приложения, содержащий файлы `Dockerfile` и `app.yaml`, и выполните следующую команду в `gcloud` CLI.",
    "Google App Engine will take care of building the Docker image based on the Docker file provided, and thereby of downloading and installing the OneAgent code-modules into the application image.": "Google App Engine сам соберёт образ Docker на основе предоставленного Docker-файла и тем самым загрузит и установит code-modules OneAgent в образ приложения.",
    "## Update OneAgent": "## Обновление OneAgent",
    "Every time you want to update your version of Dynatrace OneAgent, you must redeploy your application. Google App Engine thus rebuilds the application image with the latest OneAgent components. Any newly started containers from this application image is then monitored with the latest version of OneAgent.": "Каждый раз, когда вы хотите обновить версию Dynatrace OneAgent, необходимо повторно развернуть приложение. После этого Google App Engine пересобирает образ приложения с новейшими компонентами OneAgent. Любые контейнеры, заново запущенные из этого образа приложения, затем отслеживаются с новейшей версией OneAgent.",
}

GCP_GUIDE = {
    "title: End-to-end guide for monitoring Google Cloud services integrating Operations Suite": "title: Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite",
    "# End-to-end guide for monitoring Google Cloud services integrating Operations Suite": "# Полное руководство по мониторингу сервисов Google Cloud с интеграцией Operations Suite",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jan 17, 2022": "* Опубликовано 17 января 2022 г.",
    "Dynatrace perfectly integrates with Google Cloud to provide deep visibility into the workloads that are running on this platform.": "Dynatrace идеально интегрируется с Google Cloud, обеспечивая глубокую видимость рабочих нагрузок, выполняющихся на этой платформе.",
    "## Google Cloud supported services": "## Поддерживаемые сервисы Google Cloud",
    'Dynatrace can analyze metrics from all services available in Google Operations API. To learn about monitoring the Google Cloud supported services, capabilities and configuration options, see [Google Cloud supported service metrics](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.").': 'Dynatrace может анализировать метрики всех сервисов, доступных в Google Operations API. Сведения о мониторинге поддерживаемых сервисов Google Cloud, возможностях и параметрах конфигурации см. в разделе [Метрики поддерживаемых сервисов Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Мониторинг сервисов Google Cloud с помощью Dynatrace и просмотр доступных метрик.").',
    "## Google Cloud overview": "## Обзорная страница Google Cloud",
    "Dynatrace provides the Google Cloud overview page. It includes views per Google Cloud project and lists of instances for VMs, SQLs, Cloud Functions, and Kubernetes.": "Dynatrace предоставляет обзорную страницу Google Cloud. Она включает представления по каждому проекту Google Cloud и списки инстансов для виртуальных машин, SQL, Cloud Functions и Kubernetes.",
    "If you are already monitoring Google Cloud and the overview is not available, you need to update the Google Cloud integration you have.": "Если вы уже отслеживаете Google Cloud, а обзорная страница недоступна, необходимо обновить имеющуюся у вас интеграцию с Google Cloud.",
    "## Set up metric and log ingest": "## Настройка приёма метрик и логов",
    'To start analyzing metrics and logs from all services available in the Google Operations API, see [Set up the Dynatrace Google Cloud metric and log integration on a new GKE Autopilot cluster](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") Recommended.': 'Чтобы начать анализировать метрики и логи всех сервисов, доступных в Google Operations API, см. [Настройка интеграции метрик и логов Dynatrace с Google Cloud в новом кластере GKE Autopilot](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") Рекомендуется.',
    "For other deployment options, see": "Другие варианты развёртывания см. в разделах",
    '* [Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")': '* [Настройка интеграции логов и метрик Dynatrace с Google Cloud в существующем кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Разверните мониторинг логов и метрик для сервисов Google Cloud в существующем стандартном кластере GKE или кластере GKE Autopilot")',
    '* [Set up the Dynatrace Google Cloud metric integration on a GKE cluster](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only "Set up metric monitoring for Google Cloud services on a GKE cluster.")': '* [Настройка интеграции метрик Dynatrace с Google Cloud в кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only "Настройте мониторинг метрик для сервисов Google Cloud в кластере GKE.")',
    '* [Set up the Dynatrace Google Cloud log integration on a GKE cluster](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")': '* [Настройка интеграции логов Dynatrace с Google Cloud в кластере GKE](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only "Настройте мониторинг логов для сервисов Google Cloud в контейнере Kubernetes (GKE).")',
    '* [Deploy the Dynatrace Google Cloud metric integration in Google Cloud Function](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Set up monitoring for Google Cloud services in Google Cloud Functions.")': '* [Развёртывание интеграции метрик Dynatrace с Google Cloud в Google Cloud Function](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Настройте мониторинг сервисов Google Cloud в Google Cloud Functions.")',
    'The [main deployment](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") describes how to install version 1.0 of the Google Cloud integration on a GKE cluster. If you already have earlier versions installed, you need to [migrate](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").': '[Основное развёртывание](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.") описывает, как установить версию 1.0 интеграции с Google Cloud в кластере GKE. Если у вас уже установлены более ранние версии, необходимо выполнить [миграцию](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Миграция интеграции с Google Cloud с версии 0.1 на версию 1.0 в Kubernetes и в виде Google Cloud Function.").',
    'After deploying the integration, [you can push metrics to Dynatrace from multiple Google Cloud projects](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").': 'После развёртывания интеграции [метрики в Dynatrace можно отправлять из нескольких проектов Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Отправляйте метрики в Dynatrace из нескольких проектов Google Cloud.").',
    'To check if your monitoring function processes and sends logs to Dynatrace properly, see [Self-monitoring for the Dynatrace Google Cloud integration](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").': 'Чтобы проверить, правильно ли ваша функция мониторинга обрабатывает и отправляет логи в Dynatrace, см. [Самомониторинг интеграции Dynatrace с Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Определите, правильно ли ваша функция самомониторинга обрабатывает и отправляет логи в Dynatrace.").',
}

GCP_SUPPORTED = {
    "title: Google Cloud supported services": "title: Поддерживаемые сервисы Google Cloud",
    "# Google Cloud supported services": "# Поддерживаемые сервисы Google Cloud",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Sep 23, 2024": "* Обновлено 23 сентября 2024 г.",
    "Dynatrace version 1.230+": "Dynatrace версии 1.230+",
    "This section refers to Google Cloud service metrics that are available with Google Cloud version 1.0 integration.": "Этот раздел относится к метрикам сервисов Google Cloud, доступным с интеграцией Google Cloud версии 1.0.",
    '* For Google Cloud service metrics that are available with earlier versions of the Google Cloud integration, see [Google Cloud supported service metrics (legacy)](/managed/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Supported GCP service metrics, metrics configuration, DDU consumption, and preset dashboard availability").': '* Метрики сервисов Google Cloud, доступные с более ранними версиями интеграции с Google Cloud, см. в разделе [Метрики поддерживаемых сервисов Google Cloud (устаревшее)](/managed/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Поддерживаемые метрики сервисов GCP, конфигурация метрик, потребление DDU и доступность готовых дашбордов").',
    '[Deploy Dynatrace integration](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")': '[Развёртывание интеграции Dynatrace](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")',
    "## Supported services for metrics": "## Поддерживаемые сервисы для метрик",
    "After deploying the Dynatrace integration, you can get insights into Google Cloud services metrics collected from the Google Operations API to ensure health of your cloud infrastructure.": "После развёртывания интеграции Dynatrace можно получать аналитику по метрикам сервисов Google Cloud, собранным через Google Operations API, чтобы обеспечивать работоспособность вашей облачной инфраструктуры.",
    "Below, see the list of Google Cloud supported services.": "Ниже приведён список поддерживаемых сервисов Google Cloud.",
    "| Services | Supported entities[1](#fn-1-1-def) | Supported logs | Logs entities |": "| Сервисы | Поддерживаемые сущности[1](#fn-1-1-def) | Поддерживаемые логи | Сущности логов |",
    "Services might have one entity, several entities, or none.": "У сервисов может быть одна сущность, несколько сущностей или ни одной.",
    "## Check available metrics": "## Проверка доступных метрик",
    "To check available metrics for a service, you need to": "Чтобы проверить доступные метрики для сервиса, выполните следующие действия:",
    "1. Find the extension in the [Hub](https://www.dynatrace.com/hub/?query=google&filter=all) and select it to open the overview page. See example: [Google Cloud Functions](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).": "1. Найдите расширение в [Hub](https://www.dynatrace.com/hub/?query=google&filter=all) и выберите его, чтобы открыть обзорную страницу. См. пример: [Google Cloud Functions](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).",
    "2. Scroll down to the bottom of the overview page of the extension to find the **Feature sets** section.": "2. Прокрутите обзорную страницу расширения до конца, чтобы найти раздел **Feature sets**.",
    "3. In the table, select the **default\\_metrics** dropdown.": "3. В таблице выберите раскрывающийся список **default\\_metrics**.",
    "4. Now, you can check all available metrics for the chosen service.": "4. Теперь можно проверить все доступные метрики для выбранного сервиса.",
}

SERVICE_TITLES = {
    "Google Cloud AI Platform monitoring (deprecated)": "Мониторинг Google Cloud AI Platform (устарело)",
    "Google Cloud AlloyDB monitoring": "Мониторинг Google Cloud AlloyDB",
    "Google Cloud APIs monitoring": "Мониторинг Google Cloud APIs",
    "Google Cloud Apigee monitoring": "Мониторинг Google Cloud Apigee",
    "Google App Engine with Operations suite metrics monitoring": "Мониторинг Google App Engine с метриками Operations suite",
    "Google Cloud Assistant Smart Home monitoring": "Мониторинг Google Cloud Assistant Smart Home",
    "Google BigQuery monitoring": "Мониторинг Google BigQuery",
    "Google Cloud Bigtable monitoring": "Мониторинг Google Cloud Bigtable",
    "Google Cloud DNS monitoring": "Мониторинг Google Cloud DNS",
    "Google Cloud Functions monitoring": "Мониторинг Google Cloud Functions",
    "Google Cloud IoT Core monitoring (deprecated)": "Мониторинг Google Cloud IoT Core (устарело)",
    "Google Cloud Router monitoring": "Мониторинг Google Cloud Router",
    "Google Cloud Run monitoring": "Мониторинг Google Cloud Run",
    "Google Cloud Storage monitoring": "Мониторинг Google Cloud Storage",
    "Google Cloud Tasks monitoring": "Мониторинг Google Cloud Tasks",
    "Google Cloud Composer monitoring": "Мониторинг Google Cloud Composer",
    "Google Compute Engine with Operations suite metrics monitoring": "Мониторинг Google Compute Engine с метриками Operations suite",
    "Google Cloud Data Loss Prevention monitoring": "Мониторинг Google Cloud Data Loss Prevention",
    "Google Cloud Storage Transfer Service monitoring": "Мониторинг Google Cloud Storage Transfer Service",
    "Google Cloud Dataflow monitoring": "Мониторинг Google Cloud Dataflow",
    "Google Cloud Dataproc monitoring": "Мониторинг Google Cloud Dataproc",
    "Google Cloud Firestore in Datastore mode monitoring": "Мониторинг Google Cloud Firestore in Datastore mode",
    "Google Cloud Filestore monitoring": "Мониторинг Google Cloud Filestore",
    "Google Cloud Firebase monitoring": "Мониторинг Google Cloud Firebase",
    "Google Cloud Firestore monitoring": "Мониторинг Google Cloud Firestore",
    "Google Cloud Hybrid Connectivity monitoring": "Мониторинг Google Cloud Hybrid Connectivity",
    "Google Kubernetes Engine monitoring": "Мониторинг Google Kubernetes Engine",
    "Google Cloud Load Balancing monitoring": "Мониторинг Google Cloud Load Balancing",
    "Google Managed Microsoft AD monitoring": "Мониторинг Google Managed Microsoft AD",
    "Google Cloud Memorystore monitoring": "Мониторинг Google Cloud Memorystore",
    "NetApp on Google Cloud monitoring": "Мониторинг NetApp on Google Cloud",
    "Google Cloud Network Security monitoring": "Мониторинг Google Cloud Network Security",
    "Operations: Cloud Monitoring & Logging": "Operations: Cloud Monitoring & Logging",
    "Google Cloud Pub/Sub monitoring": "Мониторинг Google Cloud Pub/Sub",
    "Google Cloud Pub/Sub Lite monitoring": "Мониторинг Google Cloud Pub/Sub Lite",
    "Google Cloud Spanner monitoring": "Мониторинг Google Cloud Spanner",
    "Google Cloud SQL monitoring": "Мониторинг Google Cloud SQL",
    "Google Cloud Virtual Private Cloud (VPC) monitoring": "Мониторинг Google Cloud Virtual Private Cloud (VPC)",
    "Google Cloud Network Topology monitoring": "Мониторинг Google Cloud Network Topology",
    "Google Vertex AI monitoring": "Мониторинг Google Vertex AI",
}

TIP_OVERRIDES = {
    "Monitor Google Cloud Data Loss Prevention (now part of Sensitive Data Protection) and view available metrics.": "Мониторинг Google Cloud Data Loss Prevention (теперь часть Sensitive Data Protection) и просмотр доступных метрик.",
    "Monitor Google Cloud's operations suite and view available metrics.": "Мониторинг пакета Operations suite Google Cloud и просмотр доступных метрик.",
}
TIP_GENERIC = re.compile(r"^Monitor (.+) and view available metrics\.$")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*?)(?:\s+\"([^\"]*)\")?\)")


def tr_tooltip(tip):
    if tip in TIP_OVERRIDES:
        return TIP_OVERRIDES[tip]
    m = TIP_GENERIC.match(tip)
    if m:
        return "Мониторинг {} и просмотр доступных метрик.".format(m.group(1))
    return None


def build_service_row(line, warns):
    cells = line.split("|")
    if len(cells) != 6:
        warns.append("SERVICE ROW col!=6: " + line)
        return line

    def repl(m):
        text, url, tip = m.group(1), m.group(2), m.group(3)
        ru_text = SERVICE_TITLES.get(text)
        if ru_text is None:
            warns.append("UNKNOWN SERVICE TITLE: " + text)
            ru_text = text
        if tip is not None:
            ru_tip = tr_tooltip(tip)
            if ru_tip is None:
                warns.append("UNKNOWN SERVICE TOOLTIP: " + tip)
                ru_tip = tip
            return '[{}]({} "{}")'.format(ru_text, url, ru_tip)
        return "[{}]({})".format(ru_text, url)

    cells[1] = LINK_RE.sub(repl, cells[1])
    yn = cells[3].strip()
    if yn == "yes":
        cells[3] = " да "
    elif yn == "no":
        cells[3] = " нет "
    elif yn != "":
        warns.append("UNKNOWN yes/no: " + repr(yn))
    return "|".join(cells)


FILES = {
    "gcp-integrations/gcp-functions.md": ("dict", GCP_FUNCTIONS),
    "gcp-integrations/google-compute-engine.md": ("dict", COMPUTE_ENGINE),
    "gcp-integrations/google-app-engine.md": ("dict_code", APP_ENGINE),
    "gcp-integrations/gcp-guide.md": ("dict", GCP_GUIDE),
    "gcp-integrations/gcp-supported-service-metrics-new.md": (
        "supported",
        GCP_SUPPORTED,
    ),
}


def urls(s):
    return sorted(URL_RE.findall(s))


def build(rel, mode, dct):
    warns = []
    with open(os.path.join(BASE_EN, rel), "r", encoding="utf-8") as f:
        en_lines = f.read().split("\n")
    out = []
    in_fm = en_lines[0] == "---"
    fm_close = 0
    in_code = False
    for ln in en_lines:
        raw = ln.rstrip("\r")
        if in_fm:
            if raw == "---":
                fm_close += 1
                out.append(raw)
                if fm_close == 2:
                    in_fm = False
                continue
            if raw.startswith("source:") or raw.startswith("scraped:"):
                out.append(raw)
                continue
            key = clean(raw)
            out.append(dct.get(key, raw))
            if key not in dct:
                warns.append("FM UNMATCHED: " + raw)
            continue
        if mode == "dict_code" and raw.startswith("```"):
            in_code = not in_code
            out.append(raw)
            continue
        if in_code:
            out.append(raw)
            continue
        if raw == "" or ("|" in raw and set(raw) <= set("| -")):
            out.append(raw)
            continue
        if raw.strip() == "1":  # footnote back-reference number
            out.append(raw)
            continue
        key = clean(raw)
        if key in COMMON:
            out.append(COMMON[key])
            continue
        if key in dct:
            out.append(dct[key])
            continue
        if mode == "supported" and raw.startswith("| ["):
            out.append(build_service_row(raw, warns))
            continue
        warns.append("UNMATCHED: " + raw)
        out.append(raw)

    if len(out) != len(en_lines):
        warns.append("LINE-PARITY EN={} RU={}".format(len(en_lines), len(out)))
    for i, (e, r) in enumerate(zip(en_lines, out)):
        if urls(clean(e)) != urls(r):
            warns.append(
                "URL DIFF L{}: EN={} RU={}".format(i + 1, urls(clean(e)), urls(r))
            )
    joined = "\n".join(out)
    if EMDASH in joined:
        warns.append("EM-DASH present in RU")
    for m in MOJI:
        if m in joined:
            warns.append("MOJIBAKE U+{:04X} in RU".format(ord(m)))
            break

    ru_path = os.path.join(BASE_RU, rel)
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "wb") as f:
        f.write(joined.encode("utf-8"))
    return len(en_lines), len(out), warns


def main():
    allw = 0
    for rel, (mode, dct) in FILES.items():
        en_n, ru_n, warns = build(rel, mode, dct)
        flag = "OK" if (en_n == ru_n and not warns) else "CHECK"
        print("  {:48s} EN={} RU={}  {}".format(rel.split("/")[-1], en_n, ru_n, flag))
        for w in warns:
            print("      ! " + w)
            allw += 1
    print("\nDone. {} warnings.".format(allw))


if __name__ == "__main__":
    main()
