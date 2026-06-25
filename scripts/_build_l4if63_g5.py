# -*- coding: utf-8 -*-
"""L4-IF.63 builder (g5): setup-on-k8s extend-observability + deployment/other batch.

Three files:
  - ingest-from/setup-on-k8s/deployment/other/container-buildtime.md
  - ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest.md
  - ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config.md

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {normalized_EN: stripped_RU}; PASS = {normalized_EN copied as-is}.
Any prose line missing from both raises SystemExit -> catches leftover-EN.

EN sources carry double-encoded UTF-8 mojibake (see MOJI_FIX). normalize() strips
the BOM-family and folds the 3-char mojibake runs to plain ASCII on BOTH the EN line
and the TRANS keys, so keys are written in clean text. RU values are authored clean.
"""

import os
import re

# BOM-family mojibake: U+FEFF plus the 3 Latin-1 code points of a UTF-8 BOM (EF BB BF).
MOJI_RE = re.compile("[﻿ï»¿]")

# Double-encoded UTF-8 punctuation, stored as 3 Latin-1 code points each (a run that
# should have been one Unicode char). Built from bytes to stay formatter-proof:
#   E2 80 94 = em-dash       -> "-"
#   E2 80 99 = right quote    -> "'"
#   E2 80 91 = nb-hyphen      -> "-"
# Normalized on BOTH the EN line and the TRANS keys, so keys are clean ASCII. RU
# values are authored clean (em-dash spots use a comma; the auto-config hyphen
# becomes "autonastroyke" in Cyrillic).
MOJI_FIX = [
    (bytes([0xE2, 0x80, 0x94]).decode("latin-1"), "-"),
    (bytes([0xE2, 0x80, 0x99]).decode("latin-1"), "'"),
    (bytes([0xE2, 0x80, 0x91]).decode("latin-1"), "-"),
]


def normalize(s):
    s = MOJI_RE.sub("", s)
    for bad, good in MOJI_FIX:
        s = s.replace(bad, good)
    return s


BASE = os.path.join(os.path.dirname(__file__), "..", "docs")

# Map each filename -> its relpath under docs/managed (and docs/managed-ru).
REL = {
    "container-buildtime.md": "ingest-from/setup-on-k8s/deployment/other/container-buildtime.md",
    "telemetry-ingest.md": "ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest.md",
    "otlp-auto-config.md": "ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config.md",
}

# ----------------------------------------------------------------------------
TRANS = {
    # =====================================================================
    "container-buildtime.md": {
        "title: Application observability via container build-time injection": "title: Наблюдаемость приложений через внедрение во время сборки контейнера",
        "# Application observability via container build-time injection": "# Наблюдаемость приложений через внедрение во время сборки контейнера",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Oct 17, 2025": "* Обновлено 17 октября 2025 г.",
        "Inject Dynatrace code modules into a container during its build process.": "Внедрение модулей кода Dynatrace в контейнер во время процесса его сборки.",
        "This method of application instrumentation has limitations in linking "
        "Kubernetes workloads with monitored containers/processes. To achieve proper "
        "relationships and linking, consider using [automatic application-only "
        "injection](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "
        '"Deploy Dynatrace Operator in application monitoring mode to Kubernetes").': "У этого метода инструментирования приложений есть ограничения при связывании "
        "рабочих нагрузок Kubernetes с отслеживаемыми контейнерами/процессами. Чтобы "
        "добиться корректных связей и сопоставления, рассмотрите возможность "
        "использования [автоматического внедрения только на уровне приложения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "
        '"Разверните Dynatrace Operator в режиме application monitoring в Kubernetes").',
        "## Prerequisites": "## Предварительные требования",
        "* Review the list of [supported applications and versions]"
        "(/managed/ingest-from/technology-support "
        '"Find technical details related to Dynatrace support for specific platforms '
        'and development frameworks.").': "* Ознакомьтесь со списком [поддерживаемых приложений и версий]"
        "(/managed/ingest-from/technology-support "
        '"Найдите технические подробности о поддержке Dynatrace конкретных платформ '
        'и фреймворков разработки.").',
        "* [Create an access token with `PaaS Integration - InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/"
        'access-tokens#paas-token "Learn the concept of an access token and its '
        'scopes.") scope.': "* [Создайте токен доступа с областью `PaaS Integration - InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/"
        'access-tokens#paas-token "Изучите концепцию токена доступа и его областей '
        'действия (scopes).").',
        "* Storage requirements:": "* Требования к хранилищу:",
        "+ ~325 MB for glibc": "+ ~325 МБ для glibc",
        "+ ~290 MB for musl": "+ ~290 МБ для musl",
        "+ ~650 MB for glibc and musl combined": "+ ~650 МБ для glibc и musl вместе",
        "* For ARM architecture, ensure `wget` and `unzip` are installed.": "* Для архитектуры ARM убедитесь, что установлены `wget` и `unzip`.",
        "Container buildtime injection and cgroup v2": "Внедрение во время сборки контейнера и cgroup v2",
        "If Container buildtime injection is used with [cgroup v2]"
        "(https://kubernetes.io/docs/concepts/architecture/cgroups/), the "
        "`builtin:containers.*` metrics are reported to Dynatrace only if all the "
        "following conditions are respected:": "Если внедрение во время сборки контейнера используется с [cgroup v2]"
        "(https://kubernetes.io/docs/concepts/architecture/cgroups/), метрики "
        "`builtin:containers.*` отправляются в Dynatrace только при соблюдении всех "
        "следующих условий:",
        "* The **Kubernetes API** is accessible (see [Grant viewer role to service "
        "accounts](/managed/observe/infrastructure-observability/"
        "container-platform-monitoring/kubernetes-monitoring/"
        "leverage-tags-defined-in-kubernetes-deployments#viewer "
        '"Organize and filter your monitored applications by importing labels and '
        'annotations from your Kubernetes/OpenShift environment."))': "* Доступен **Kubernetes API** (см. [Предоставление роли viewer служебным "
        "учётным записям](/managed/observe/infrastructure-observability/"
        "container-platform-monitoring/kubernetes-monitoring/"
        "leverage-tags-defined-in-kubernetes-deployments#viewer "
        '"Упорядочивайте и фильтруйте отслеживаемые приложения, импортируя метки и '
        'аннотации из вашего окружения Kubernetes/OpenShift."))',
        "* The pod runs a **single container**": "* Под запускает **один контейнер**",
        "## Deploy": "## Развёртывание",
        "To integrate OneAgent into the application image, follow the steps below.": "Чтобы интегрировать OneAgent в образ приложения, выполните шаги ниже.",
        "Kubernetes/OpenShift v4.0": "Kubernetes/OpenShift v4.0",
        "OpenShift v3.11": "OpenShift v3.11",
        "ARM": "ARM",
        "1. Sign in to Docker with your Dynatrace environment ID as username and "
        "access token as password.": "1. Войдите в Docker, указав ID вашего окружения Dynatrace в качестве имени "
        "пользователя и токен доступа в качестве пароля.",
        "2. Add the following lines of code to the application image, after the last "
        "`FROM` command:": "2. Добавьте следующие строки кода в образ приложения после последней команды "
        "`FROM`:",
        # mojibake: `<technology>` + em-dash -> normalized key has "<technology>`-OneAgent"
        "* `<technology>`-OneAgent code module required for your application. "
        "Available options are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, "
        "`php`, `go`, and `sdk`. You can specify several code modules, separated by "
        "hyphen (`-`), for example `java-go`. Including specific technology-support "
        "options, rather than support for all technology options, results in a smaller "
        "OneAgent package.": "* `<technology>`, модуль кода OneAgent, необходимый для вашего приложения. "
        "Доступные варианты: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, "
        "`php`, `go` и `sdk`. Можно указать несколько модулей кода, разделённых "
        "дефисом (`-`), например `java-go`. Включение определённых опций поддержки "
        "технологий вместо поддержки всех технологий приводит к уменьшению размера "
        "пакета OneAgent.",
        "What if my Docker image is based on Alpine Linux?": "Что делать, если мой образ Docker основан на Alpine Linux?",
        "Dynatrace OneAgent supports Alpine Linux based environments.": "Dynatrace OneAgent поддерживает окружения на основе Alpine Linux.",
        "Valid options here are: `all`, `dotnet`, `php`, `java`, `apache`, `nginx`, "
        "`nodejs`, and `go`.": "Допустимые варианты здесь: `all`, `dotnet`, `php`, `java`, `apache`, "
        "`nginx`, `nodejs` и `go`.",
        "3. Build your application image.": "3. Соберите образ вашего приложения.",
        "Build the Docker image from your Dockerfile to use it in your Kubernetes "
        "environment.": "Соберите образ Docker из вашего Dockerfile, чтобы использовать его в вашем "
        "окружении Kubernetes.",
        "You can monitor your application containers with a different Dynatrace "
        "environment.": "Контейнеры вашего приложения можно отслеживать с помощью другого окружения "
        "Dynatrace.",
        "For OneAgent version 1.139+, if you have an existing application image where "
        "you've already added the OneAgent code modules for a specific Dynatrace "
        "environment, you can have the OneAgent report to another Dynatrace "
        "environment without rebuilding your application image.": "Для OneAgent версии 1.139+, если у вас есть готовый образ приложения, в "
        "который вы уже добавили модули кода OneAgent для определённого окружения "
        "Dynatrace, можно настроить отправку данных OneAgent в другое окружение "
        "Dynatrace без пересборки образа приложения.  ",
        "For this, you need to make a call to the REST endpoint of your second "
        "Dynatrace environment. Don't forget to adapt the respective placeholders "
        "`<environmentID>` and `<token>`.": "Для этого необходимо обратиться к REST-эндпоинту вашего второго окружения "
        "Dynatrace. Не забудьте подставить соответствующие плейсхолдеры "
        "`<environmentID>` и `<token>`.",
        "In return, you get a JSON object that covers the required information that "
        "needs to be passed as an environment variable to the application container.": "В ответ вы получите объект JSON, содержащий необходимую информацию, которую "
        "нужно передать в контейнер приложения в виде переменной окружения.  ",
        "Make sure you set the environment variables of the application container as "
        "described below:": "Убедитесь, что переменные окружения контейнера приложения заданы, как "
        "описано ниже:",
        "* `DT_TENANT`: equals `tenantUUID`": "* `DT_TENANT`: равно `tenantUUID`",
        "* `DT_TENANTTOKEN`: equals `tenantToken`": "* `DT_TENANTTOKEN`: равно `tenantToken`",
        "* `DT_CONNECTION_POINT`: semi-colon separated list of "
        "`communicationEndpoints`": "* `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённый точкой "
        "с запятой",
        "4. Optional Configure network zones": "4. Необязательно. Настройте сетевые зоны",
        "You can configure network zones as an environment variable:": "Сетевые зоны можно настроить в виде переменной окружения:",
        "* `DT_NETWORK_ZONE`: equals `your.network.zone`": "* `DT_NETWORK_ZONE`: равно `your.network.zone`",
        "See [network zones](/managed/manage/network-zones "
        '"Find out how network zones work in Dynatrace.") for more information.': "Подробнее см. [сетевые зоны](/managed/manage/network-zones "
        '"Узнайте, как работают сетевые зоны в Dynatrace.").',
        "5. Optional Configure a proxy address": "5. Необязательно. Настройте адрес прокси",
        "In case you run an environment with proxy, you need to set the `DT_PROXY` "
        "environment variable in the application container to pass the proxy "
        "credentials to OneAgent.": "Если вы используете окружение с прокси, необходимо задать переменную "
        "окружения `DT_PROXY` в контейнере приложения, чтобы передать учётные данные "
        "прокси в OneAgent.",
        "For Alpine Linux-based containers, you might need to update the `wget` "
        "shipped with the Alpine image to allow for proxy authentication for the "
        "download of OneAgent.": "Для контейнеров на основе Alpine Linux может потребоваться обновить `wget`, "
        "поставляемый с образом Alpine, чтобы разрешить аутентификацию через прокси "
        "при загрузке OneAgent.",
        "1. Define variables with optional default values using `ARG` instructions, "
        "as shown below.": "1. Определите переменные с необязательными значениями по умолчанию с помощью "
        "инструкций `ARG`, как показано ниже.",
        # mojibake: `you` + right-quote + `re` -> normalized key has "you're"
        "* You can override the default values within the OpenShift `BuildConfig`. "
        "Replace `<environmentID>` with your Dynatrace environment ID. If you're "
        "using Dynatrace Managed, you need to provide your Dynatrace Server URL "
        "(`https://<YourDynatraceServerURL>/e/<environmentID>/api`). Replace `<token>` "
        "with the PaaS token mentioned above.": "* Значения по умолчанию можно переопределить в `BuildConfig` OpenShift. "
        "Замените `<environmentID>` на ID вашего окружения Dynatrace. Если вы "
        "используете Dynatrace Managed, необходимо указать URL вашего сервера "
        "Dynatrace (`https://<YourDynatraceServerURL>/e/<environmentID>/api`). "
        "Замените `<token>` на PaaS-токен, упомянутый выше.",
        "* Technology support is enabled via `include` parameters. Valid options for "
        "`flavor=default` are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, "
        "`php`, `go`, and `sdk`. Including specific technology-support options, rather "
        "than support for all technology options, results in a smaller OneAgent "
        "package.": "* Поддержка технологий включается через параметры `include`. Допустимые "
        "варианты для `flavor=default`: `all`, `java`, `apache`, `nginx`, `nodejs`, "
        "`dotnet`, `php`, `go` и `sdk`. Включение определённых опций поддержки "
        "технологий вместо поддержки всех технологий приводит к уменьшению размера "
        "пакета OneAgent.",
        "OneAgent supports the flavor `musl` for Alpine Linux based environments. "
        "Valid options for `flavor=musl` are `all`, `java`, `apache`, `nginx`, and "
        "`nodejs`.": "OneAgent поддерживает вариант `musl` для окружений на основе Alpine Linux. "
        "Допустимые варианты для `flavor=musl`: `all`, `java`, `apache`, `nginx` и "
        "`nodejs`.",
        "2. Add the following commands to your current Dockerfile to integrate "
        "OneAgent and activate instrumentation of your application.": "2. Добавьте следующие команды в ваш текущий Dockerfile, чтобы "
        "интегрировать OneAgent и активировать инструментирование вашего приложения.",
        "The commands above that use `wget` and `unzip` might fail if they aren't "
        "provided by the base image.": "Приведённые выше команды, использующие `wget` и `unzip`, могут завершиться "
        "ошибкой, если они не предоставляются базовым образом.",
        "In an OpenShift context the above Dockerfile could be used for binary builds "
        "as follows:": "В контексте OpenShift приведённый выше Dockerfile можно использовать для "
        "двоичных сборок следующим образом:",
        "1. Set the following build-time variables:": "1. Задайте следующие переменные времени сборки:",
        "* `$DT_API_URL` (The API URL of your Dynatrace environment)": "* `$DT_API_URL` (URL API вашего окружения Dynatrace)",
        "* `$DT_PAAS_TOKEN` (The PaaS token to download the code modules)": "* `$DT_PAAS_TOKEN` (PaaS-токен для загрузки модулей кода)",
        "* `$DT_ONEAGENT_TECHNOLOGY` (The module that is downloaded, for example "
        "`php`)": "* `$DT_ONEAGENT_TECHNOLOGY` (Загружаемый модуль, например `php`)",
        "2. Add the following commands to the Dockerfile:": "2. Добавьте следующие команды в Dockerfile:",
        "## Update": "## Обновление",
        "You need to manually update OneAgent by rebuilding the container image every "
        "time a new version of a code module is needed.": "OneAgent необходимо обновлять вручную, пересобирая образ контейнера каждый "
        "раз, когда требуется новая версия модуля кода.",
        "## Uninstall": "## Удаление",
        "To uninstall OneAgent from application monitoring": "Чтобы удалить OneAgent из мониторинга приложений",
        "Docker multi-stage image builds": "Многоэтапные сборки образов Docker",
        "Classic integration": "Классическая интеграция",
        "1. Remove the two lines of code from the application image.": "1. Удалите две строки кода из образа приложения.",
        "2. Rebuild the application image.": "2. Пересоберите образ приложения.",
        "1. Remove the following commands from your Dockerfile.": "1. Удалите следующие команды из вашего Dockerfile.",
    },
    # =====================================================================
    "telemetry-ingest.md": {
        "title: Enable Dynatrace telemetry ingest endpoints": "title: Включение конечных точек приёма телеметрии Dynatrace",
        "# Enable Dynatrace telemetry ingest endpoints": "# Включение конечных точек приёма телеметрии Dynatrace",
        "* Updated on Nov 04, 2025": "* Обновлено 04 ноября 2025 г.",
        "Dynatrace Operator version 1.6+": "Dynatrace Operator version 1.6+",
        "Enable Dynatrace telemetry endpoints in Kubernetes for cluster-local data "
        "ingest.": "Включение конечных точек телеметрии Dynatrace в Kubernetes для приёма данных "
        "внутри кластера.",
        "* Ingest data via [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/), "
        "[Jaeger](https://www.jaegertracing.io/), "
        "[StatsD](https://github.com/statsd/statsd) or "
        "[Zipkin](https://zipkin.io/) endpoints": "* Приём данных через конечные точки [OTLP]"
        "(https://opentelemetry.io/docs/specs/otel/protocol/), "
        "[Jaeger](https://www.jaegertracing.io/), "
        "[StatsD](https://github.com/statsd/statsd) или "
        "[Zipkin](https://zipkin.io/)",
        "* Analyze context-rich data with built-in apps, DQL, Notebooks and "
        "Dashboards": "* Анализ насыщенных контекстом данных с помощью встроенных приложений, DQL, "
        "Notebooks и Dashboards",
        "## Prerequisites": "## Предварительные требования",
        "* The [data ingest token](/managed/ingest-from/setup-on-k8s/deployment/"
        'tokens-permissions#dataIngestToken "Configure tokens and permissions to '
        'monitor your Kubernetes cluster") requires the token scopes '
        "`openTelemetryTrace.ingest`, `logs.ingest`, and `metrics.ingest` and must be "
        "provided via the `dataIngestToken` field in the same [secret]"
        "(/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed#create-secret-helm "
        '"Deploy Dynatrace Operator for Kubernetes observability.") as your API '
        "token.": "* [Токен приёма данных](/managed/ingest-from/setup-on-k8s/deployment/"
        'tokens-permissions#dataIngestToken "Настройка токенов и разрешений для '
        'мониторинга кластера Kubernetes") требует областей токена '
        "`openTelemetryTrace.ingest`, `logs.ingest` и `metrics.ingest` и должен быть "
        "предоставлен через поле `dataIngestToken` в том же [секрете]"
        "(/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed#create-secret-helm "
        '"Разверните Dynatrace Operator для Kubernetes observability."), что и ваш '
        "API-токен.",
        "## Setup and Use": "## Настройка и использование",
        "The following two steps explain how to setup and use telemetry ingest "
        "endpoints.": "Следующие два шага описывают, как настроить и использовать конечные точки "
        "приёма телеметрии.",
        "Kubernetes App onboarding": "Подключение через Kubernetes App",
        "If you got your DynaKube from the [onboarding screen of the Dynatrace "
        "Kubernetes App](/managed/ingest-from/setup-on-k8s/quickstart "
        '"Deploy Dynatrace Operator on Kubernetes") the telemetry ingest service name '
        "will be set to `telemetry-ingest.dynatrace`. See [Customize the name of the "
        "telemetry ingest service](#customize-the-service-name) to change it.": "Если вы получили ваш DynaKube с [экрана подключения приложения Dynatrace "
        "Kubernetes App](/managed/ingest-from/setup-on-k8s/quickstart "
        '"Развёртывание Dynatrace Operator на Kubernetes"), имя сервиса приёма '
        "телеметрии будет задано как `telemetry-ingest.dynatrace`. Чтобы изменить "
        "его, см. [Настройка имени сервиса приёма телеметрии]"
        "(#customize-the-service-name).",
        "1. Create DynaKube": "1. Создайте DynaKube",
        "To enable telemetry ingest endpoints, specify a list of desired protocols in "
        "the DynaKube field `.spec.telemetryIngest.protocols`. Please find more "
        "information about the exact values in our [DynaKube reference]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#telemetry-ingest-v1beta5 "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") documentation.': "Чтобы включить конечные точки приёма телеметрии, укажите список нужных "
        "протоколов в поле DynaKube `.spec.telemetryIngest.protocols`. Подробнее о "
        "точных значениях см. в нашей документации [справочника по DynaKube]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#telemetry-ingest-v1beta5 "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.").',
        "Data routing": "Маршрутизация данных",
        "With an ActiveGate running in the Kubernetes cluster, the [OpenTelemetry "
        "Collector](/managed/ingest-from/opentelemetry/collector "
        '"Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel '
        'Collector, to ingest telemetry from OpenTelemetry.") will be configured to '
        "route all ingested data through the in-cluster ActiveGate instead of "
        "connecting directly to a public ActiveGate. Additionally, the capabilities "
        "required for telemetry ingest will automatically be enabled.": "При наличии ActiveGate, работающего в кластере Kubernetes, [OpenTelemetry "
        "Collector](/managed/ingest-from/opentelemetry/collector "
        '"Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel '
        'Collector, для приёма телеметрии из OpenTelemetry.") будет настроен на '
        "маршрутизацию всех принимаемых данных через ActiveGate внутри кластера "
        "вместо прямого подключения к публичному ActiveGate. Кроме того, "
        "автоматически будут включены возможности, необходимые для приёма "
        "телеметрии.",
        "If no in-cluster ActiveGate is deployed (i.e., `.spec.activeGate` is not "
        "specified), the OpenTelemetry Collector will be configured to communicate "
        "directly with your Dynatrace tenant.": "Если ActiveGate внутри кластера не развёрнут (то есть `.spec.activeGate` не "
        "указан), OpenTelemetry Collector будет настроен на прямое взаимодействие с "
        "вашим тенантом Dynatrace.",
        "OTel collector image": "Образ OTel collector",
        "OTel collector image is sourced from our [supported public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry"), make sure the used `tag` exists! Alternatively, '
        "you can use your [private registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry").': "Образ OTel collector берётся из наших [поддерживаемых публичных реестров]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра"), убедитесь, что используемый `tag` '
        "существует! В качестве альтернативы можно использовать ваш [частный реестр]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра").',
        "2. Configure applications": "2. Настройте приложения",
        "Once the DynaKube is applied, the Dynatrace Operator will deploy the "
        "Dynatrace OpenTelemetry Collector with the default image ([configurable "
        "using `.spec.templates.otelCollector.imageRef`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extensions-collector-image-ref "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.")) and a Kubernetes service named '
        "`<dynakube-name>-telemetry-ingest.dynatrace` ([configurable using "
        "`.spec.telemetryIngest.serviceName`](#customize-the-service-name)) for "
        "telemetry ingest. The used port number depends on the protocol your "
        "application supports. To find the respective port numbers, please see the "
        "[reference](#port-list) below.": "После применения DynaKube Dynatrace Operator развернёт Dynatrace "
        "OpenTelemetry Collector с образом по умолчанию ([настраивается с помощью "
        "`.spec.templates.otelCollector.imageRef`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extensions-collector-image-ref "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.")) и сервис Kubernetes с именем '
        "`<dynakube-name>-telemetry-ingest.dynatrace` ([настраивается с помощью "
        "`.spec.telemetryIngest.serviceName`](#customize-the-service-name)) для "
        "приёма телеметрии. Используемый номер порта зависит от протокола, который "
        "поддерживает ваше приложение. Чтобы найти соответствующие номера портов, см. "
        "[справочник](#port-list) ниже.",
        "The following snippet shows how you can configure an application using an "
        "environment variable that is instrumented with the OpenTelemetry SDK:": "Следующий фрагмент показывает, как настроить приложение, инструментированное "
        "с помощью OpenTelemetry SDK, используя переменную окружения:",
        "### Ports reference": "### Справочник по портам",
        "The following ports are open for telemetry data ingestion:": "Для приёма данных телеметрии открыты следующие порты:",
        "| Name | Protocol | Port |": "| Имя | Протокол | Порт |",
        "| OTLP GRPC | TCP | 4317 |": "| OTLP GRPC | TCP | 4317 |",
        "| OTLP HTTP | TCP | 4318 |": "| OTLP HTTP | TCP | 4318 |",
        "| Zipkin | TCP | 9411 |": "| Zipkin | TCP | 9411 |",
        "| Jaeger GRPC | TCP | 14250 |": "| Jaeger GRPC | TCP | 14250 |",
        "| Jaeger Thrift Binary | UDP | 6832 |": "| Jaeger Thrift Binary | UDP | 6832 |",
        "| Jaeger Thrift Compact | UDP | 6831 |": "| Jaeger Thrift Compact | UDP | 6831 |",
        "| Jaeger Thrift HTTP | TCP | 14268 |": "| Jaeger Thrift HTTP | TCP | 14268 |",
        "| StatsD | UDP | 8125 |": "| StatsD | UDP | 8125 |",
        "## Additional configurations": "## Дополнительные настройки",
        "### Use HTTPS endpoints": "### Использование конечных точек HTTPS",
        "By default, the ingest endpoints operate in HTTP mode. If you want to encrypt "
        "the telemetry traffic by using HTTPS, you can reference a [Kubernetes TLS "
        "secret](https://dt-url.net/yw03zsm) via "
        "[`.spec.telemetryIngest.tlsRefName`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes."). The ingest endpoints will then be configured to use '
        "referenced certificates and listen for HTTPS.": "По умолчанию конечные точки приёма работают в режиме HTTP. Если требуется "
        "шифровать трафик телеметрии с помощью HTTPS, можно сослаться на [секрет "
        "Kubernetes TLS](https://dt-url.net/yw03zsm) через "
        "[`.spec.telemetryIngest.tlsRefName`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."). Тогда конечные точки приёма будут настроены на использование '
        "указанных сертификатов и прослушивание HTTPS.",
        "Example for an OpenTelemetry instrumented application using HTTPS": "Пример для инструментированного OpenTelemetry приложения с использованием "
        "HTTPS",
        "The following snippet shows how you can configure an application that is "
        "instrumented with the OpenTelemetry SDK through the environment variable:": "Следующий фрагмент показывает, как настроить приложение, инструментированное "
        "с помощью OpenTelemetry SDK, через переменную окружения:",
        "### Customize the name of the telemetry ingest service": "### Настройка имени сервиса приёма телеметрии",
        "By default, the service name for telemetry ingest is "
        "`<dynakube-name>-telemetry-ingest.dynatrace`, but it can be customized by "
        "setting [`.spec.telemetryIngest.serviceName`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes."). The provided value will be used as a service name, but the '
        "services will still be in the namespace of the DynaKube, which is where also "
        "the Dynatrace OpenTelemetry Collector is deployed.": "По умолчанию имя сервиса для приёма телеметрии, это "
        "`<dynakube-name>-telemetry-ingest.dynatrace`, но его можно настроить, задав "
        "[`.spec.telemetryIngest.serviceName`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."). Указанное значение будет использовано как имя сервиса, но '
        "сервисы по-прежнему будут находиться в пространстве имён DynaKube, где также "
        "развёрнут Dynatrace OpenTelemetry Collector.",
        "Be aware that having multiple DynaKubes with the same service name will cause "
        "service name collisions.": "Учтите, что наличие нескольких DynaKube с одинаковым именем сервиса приведёт "
        "к конфликтам имён сервисов.",
        "For example, if you set `.spec.telemetryIngest.serviceName` to "
        "`my-telemetry-ingest`, the endpoints are available at "
        "`http://my-telemetry-ingest.dynatrace:4318`.": "Например, если задать для `.spec.telemetryIngest.serviceName` значение "
        "`my-telemetry-ingest`, конечные точки будут доступны по адресу "
        "`http://my-telemetry-ingest.dynatrace:4318`.",
        "Example": "Пример",
        "### Proxy settings": "### Настройки прокси",
        "Any proxy specified in [`.spec.proxy`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") will be propagated to the OpenTelemetry Collector via '
        "environment variables `HTTP_PROXY` and `HTTPS_PROXY`. If an in-cluster "
        "ActiveGate is used, the URL of the in-cluster ActiveGate will automatically "
        "be added to the `NO_PROXY` environment variable to avoid unnecessary "
        "communication loops.": "Любой прокси, указанный в [`.spec.proxy`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."), будет передан в OpenTelemetry Collector через переменные '
        "окружения `HTTP_PROXY` и `HTTPS_PROXY`. Если используется ActiveGate внутри "
        "кластера, URL этого ActiveGate будет автоматически добавлен в переменную "
        "окружения `NO_PROXY`, чтобы избежать ненужных циклов взаимодействия.",
        "#### Trusted CAs": "#### Доверенные центры сертификации (CA)",
        "If you need to use certificates for proxy communication, they can be "
        "specified in [`.spec.trustedCAs`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes."). System CAs from the OpenTelemetry Collector container image '
        "are loaded together with CAs in `trustedCAs`. The system CAs contain the "
        "certificates required for communication with public ActiveGates.": "Если для взаимодействия через прокси требуется использовать сертификаты, их "
        "можно указать в [`.spec.trustedCAs`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."). Системные CA из образа контейнера OpenTelemetry Collector '
        "загружаются вместе с CA из `trustedCAs`. Системные CA содержат сертификаты, "
        "необходимые для взаимодействия с публичными ActiveGate.",
        "### ActiveGate persistent storage": "### Постоянное хранилище ActiveGate",
        "When telemetry ingest is used with an in-cluster ActiveGate, ingested data is "
        "buffered on a PersistentVolume on the ActiveGate until data has been "
        "transfered successfully. For this purpose, a [PersistentVolumeClaim is "
        "mounted to the ActiveGate]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "
        '"Set up a persistent storage for containerized ActiveGate to be used as '
        'temporary storage for ingested data."). The following example illustrates '
        "the default PVC configured to the ActiveGate by the operator if no custom PVC "
        "is specified:": "Когда приём телеметрии используется с ActiveGate внутри кластера, "
        "принимаемые данные буферизуются на PersistentVolume на ActiveGate до тех "
        "пор, пока данные не будут успешно переданы. Для этого к ActiveGate "
        "монтируется [PersistentVolumeClaim]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "
        '"Настройте постоянное хранилище для контейнеризированного ActiveGate, '
        'используемое как временное хранилище для принимаемых данных."). Следующий '
        "пример иллюстрирует PVC по умолчанию, настраиваемый для ActiveGate "
        "оператором, если пользовательский PVC не указан:",
        "Default storage class": "Класс хранилища по умолчанию",
        "Please ensure a [default storage class]"
        "(https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1) is "
        "defined. Otherwise, the PersistentVolumeClaim of the ActiveGate cannot be "
        "provisioned.": "Убедитесь, что определён [класс хранилища по умолчанию]"
        "(https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1). "
        "В противном случае PersistentVolumeClaim для ActiveGate не может быть "
        "подготовлен.",
        "A custom PersistentVolumeClaim can be configured in "
        "[`.spec.activegate.volumeClaimTemplate`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.").': "Пользовательский PersistentVolumeClaim можно настроить в "
        "[`.spec.activegate.volumeClaimTemplate`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.").',
        "#### Ephemeral volume": "#### Эфемерный том",
        "For test purposes, a PVC can be replaced by local ephemeral storage using "
        "[`.spec.activeGate.useEphemeralVolume`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.").': "В тестовых целях PVC можно заменить локальным эфемерным хранилищем с помощью "
        "[`.spec.activeGate.useEphemeralVolume`]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.").',
        "Using `.spec.activeGate.useEphemeralVolume` is not recommended for production "
        "environments.": "Использование `.spec.activeGate.useEphemeralVolume` не рекомендуется для "
        "производственных окружений.",
        "### ActiveGate time for shutdown": "### Время на завершение работы ActiveGate",
        "If an ActiveGate is shut down (for example, in scale-in scenarios), it needs "
        "some time to flush its buffers by sending all the buffered data to Dynatrace.": "Если ActiveGate завершает работу (например, в сценариях масштабирования "
        "вниз), ему требуется некоторое время, чтобы сбросить свои буферы, отправив "
        "все буферизованные данные в Dynatrace.",
        "In large environments, this can take some time and Kubernetes could "
        "potentially terminate the ActiveGate too early. To expand the so-called "
        "termination grace period, you can increase the duration via "
        "['.spec.activegate.terminationGracePeriodSeconds']"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") to give the ActiveGate pod more time to gracefully shut down.': "В крупных окружениях это может занять некоторое время, и Kubernetes "
        "потенциально может завершить работу ActiveGate слишком рано. Чтобы расширить "
        "так называемый период ожидания завершения (termination grace period), можно "
        "увеличить длительность через "
        "['.spec.activegate.terminationGracePeriodSeconds']"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."), чтобы дать поду ActiveGate больше времени на корректное '
        "завершение работы.",
        "## Related topics": "## Связанные темы",
        "* [DynaKube parameters for Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.")': "* [Параметры DynaKube для Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.")',
    },
    # =====================================================================
    "otlp-auto-config.md": {
        "title: Enable automatic OpenTelemetry OTLP exporter configuration": "title: Включение автоматической настройки экспортёра OpenTelemetry OTLP",
        "# Enable automatic OpenTelemetry OTLP exporter configuration": "# Включение автоматической настройки экспортёра OpenTelemetry OTLP",
        "* Published Nov 24, 2025": "* Опубликовано 24 ноября 2025 г.",
        "Dynatrace Operator version 1.8.0+": "Dynatrace Operator version 1.8.0+",
        "Dynatrace Operator can automatically configure the OpenTelemetry OTLP "
        "exporter for applications instrumented with an [OpenTelemetry SDK]"
        "(https://opentelemetry.io/docs/languages/). This is done by injecting "
        "environment variables into your application pods at startup, allowing "
        "telemetry data to be sent directly to Dynatrace.": "Dynatrace Operator может автоматически настраивать экспортёр OpenTelemetry "
        "OTLP для приложений, инструментированных с помощью [OpenTelemetry SDK]"
        "(https://opentelemetry.io/docs/languages/). Это делается путём внедрения "
        "переменных окружения в поды вашего приложения при запуске, что позволяет "
        "отправлять данные телеметрии напрямую в Dynatrace.",
        "## Enable OTLP auto-configuration": "## Включение автонастройки OTLP",
        "### Provide a data ingest token": "### Предоставьте токен приёма данных",
        "You need to provide a [data ingest token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "
        '"Configure tokens and permissions to monitor your Kubernetes cluster") to '
        "the Dynatrace Operator. This token is passed to your application as part of "
        "the OTLP exporter configuration.": "Необходимо предоставить [токен приёма данных]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "
        '"Настройка токенов и разрешений для мониторинга кластера Kubernetes") в '
        "Dynatrace Operator. Этот токен передаётся вашему приложению как часть "
        "настройки экспортёра OTLP.",
        "### Update your DynaKube resource": "### Обновите ваш ресурс DynaKube",
        "Add the `otlpExporterConfiguration` section to your DynaKube custom resource. "
        "This enables auto-configuration for all signals (metrics, traces, logs):": "Добавьте раздел `otlpExporterConfiguration` в ваш пользовательский ресурс "
        "DynaKube. Это включает автонастройку для всех сигналов (метрик, трассировок, "
        "логов):",
        "You can enable injection for each signal type (metrics, traces, logs) "
        "separately.": "Внедрение можно включать для каждого типа сигнала (метрики, трассировки, "
        "логи) отдельно.",
        "The following secrets are created in each [injected namespace]"
        "(#namespace-selector):": "Следующие секреты создаются в каждом [пространстве имён с внедрением]"
        "(#namespace-selector):",
        "* `dynatrace-otlp-exporter-certs` holds the certificates required for "
        "communication with the configured endpoint, which is one of the following:": "* `dynatrace-otlp-exporter-certs` содержит сертификаты, необходимые для "
        "взаимодействия с настроенной конечной точкой, которая является одной из "
        "следующих:",
        "+ The TLS certificate for the ActiveGate.": "+ TLS-сертификат для ActiveGate.",
        "+ Certificates contained in `.spec.trustedCAs`, if provided and no ActiveGate "
        "with TLS certificates is available.": "+ Сертификаты, содержащиеся в `.spec.trustedCAs`, если они предоставлены и "
        "недоступен ActiveGate с TLS-сертификатами.",
        "* `dynatrace-otlp-exporter-config` holds a copy of the [data ingest token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "* `dynatrace-otlp-exporter-config` содержит копию [токена приёма данных]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "
        '"Настройка токенов и разрешений для мониторинга кластера Kubernetes").',
        "Secrets are updated automatically when the token or certificate changes, but "
        "only new pods will receive updated values. Restart your application pods "
        "subsequent to a change to avoid authentication or communication issues.": "Секреты обновляются автоматически при изменении токена или сертификата, но "
        "обновлённые значения получат только новые поды. Перезапустите поды вашего "
        "приложения после изменения, чтобы избежать проблем с аутентификацией или "
        "взаимодействием.",
        "**Notes**:": "**Примечания**:",
        "* OTLP exporter configuration [is skipped](#verify-config) in case "
        "prerequisites are not fulfilled.": "* Настройка экспортёра OTLP [пропускается](#verify-config), если не "
        "выполнены предварительные требования.",
        # mojibake: `OTLP_*`) ` + em-dash + ` even` -> normalized key has ") - even"
        "* By default, if any `OTEL_EXPORTER_OTLP_*` environment variable is already "
        "present in the container spec, Dynatrace Operator will skip the injection of "
        "endpoint configuration (aka. `OTEL_EXPORTER_OTLP_*`) - even if the existing "
        "configuration doesn't overlap with what would be added automatically. To "
        "allow Dynatrace Operator to override the existing configuration, enable "
        "[override mode](#override). Resource attributes (`OTEL_RESOURCE_ATTRIBUTES`) "
        "are not affected by this logic and will still be set or extended.": "* По умолчанию, если в спецификации контейнера уже присутствует какая-либо "
        "переменная окружения `OTEL_EXPORTER_OTLP_*`, Dynatrace Operator пропустит "
        "внедрение настройки конечной точки (то есть `OTEL_EXPORTER_OTLP_*`), даже "
        "если существующая настройка не пересекается с тем, что было бы добавлено "
        "автоматически. Чтобы разрешить Dynatrace Operator переопределять "
        "существующую настройку, включите [режим переопределения](#override). На "
        "атрибуты ресурсов (`OTEL_RESOURCE_ATTRIBUTES`) эта логика не влияет, они "
        "по-прежнему будут заданы или дополнены.",
        "### Verify the auto-configuration": "### Проверьте автонастройку",
        "If the OTLP auto-configuration has been injected successfully, your "
        "application pod receives the following annotation:": "Если автонастройка OTLP была успешно внедрена, под вашего приложения "
        "получает следующую аннотацию:",
        "If something goes wrong, the pod is annotated with a reason for the failure:": "Если что-то идёт не так, под аннотируется причиной сбоя:",
        "## Injected OTLP configuration": "## Внедрённая настройка OTLP",
        "### Environment variables": "### Переменные окружения",
        "The following environment variables are injected into your application "
        "containers:": "В контейнеры вашего приложения внедряются следующие переменные окружения:",
        "| Variable | Value |": "| Переменная | Значение |",
        "| `DT_API_TOKEN` | `dataIngestToken provided by user` |": "| `DT_API_TOKEN` | `dataIngestToken provided by user` |",
        "| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | "
        "`https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/traces` |": "| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | "
        "`https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/traces` |",
        "| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` | `http/protobuf` |": "| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` | `http/protobuf` |",
        "| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | "
        "`authorization=Api-Token $(DT_API_TOKEN)` |": "| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | "
        "`authorization=Api-Token $(DT_API_TOKEN)` |",
        "| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | "
        "`https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/metrics` |": "| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | "
        "`https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/metrics` |",
        "| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | `http/protobuf` |": "| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | `http/protobuf` |",
        "| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | "
        "`authorization=Api-Token $(DT_API_TOKEN)` |": "| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | "
        "`authorization=Api-Token $(DT_API_TOKEN)` |",
        "| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` | `delta` |": "| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` | `delta` |",
        "| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | "
        "`https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/logs` |": "| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | "
        "`https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/logs` |",
        "| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | `http/protobuf` |": "| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | `http/protobuf` |",
        "| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | "
        "`authorization=Api-Token $(DT_API_TOKEN)` |": "| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | "
        "`authorization=Api-Token $(DT_API_TOKEN)` |",
        "| `OTEL_RESOURCE_ATTRIBUTES` | "
        "`k8s.cluster.name=dynakube,k8s.container.name=app ...` |": "| `OTEL_RESOURCE_ATTRIBUTES` | "
        "`k8s.cluster.name=dynakube,k8s.container.name=app ...` |",
        "### Resource attributes": "### Атрибуты ресурсов",
        "Dynatrace Operator adds resource attributes in `OTEL_RESOURCE_ATTRIBUTES` to "
        "enrich OpenTelemetry data providing topology and additional context on data "
        "points for a rich Dynatrace experience:": "Dynatrace Operator добавляет атрибуты ресурсов в `OTEL_RESOURCE_ATTRIBUTES`, "
        "чтобы обогатить данные OpenTelemetry, предоставляя топологию и "
        "дополнительный контекст для точек данных ради насыщенного опыта работы с "
        "Dynatrace:",
        "* `k8s.cluster.name`": "* `k8s.cluster.name`",
        "* `k8s.container.name`": "* `k8s.container.name`",
        "* `k8s.workload.name`": "* `k8s.workload.name`",
        "* `k8s.cluster.uid`": "* `k8s.cluster.uid`",
        "* `k8s.pod.name`": "* `k8s.pod.name`",
        "* `k8s.pod.uid`": "* `k8s.pod.uid`",
        "* `k8s.node.name`": "* `k8s.node.name`",
        "* `k8s.namespace.name`": "* `k8s.namespace.name`",
        "* `k8s.workload.kind`": "* `k8s.workload.kind`",
        "* `dt.kubernetes.cluster.id`": "* `dt.kubernetes.cluster.id`",
        "* `dt.entity.kubernetes_cluster`": "* `dt.entity.kubernetes_cluster`",
        "The values for those attributes are derived from the cluster and pod "
        "metadata. Furthermore, all metadata provided in the "
        "`metadata.dynatrace.com/<key>: <value>` annotations on the namespace or on "
        "the injected pod are added as resource attributes.": "Значения этих атрибутов выводятся из метаданных кластера и пода. Кроме того, "
        "все метаданные, указанные в аннотациях "
        "`metadata.dynatrace.com/<key>: <value>` на пространстве имён или на поде с "
        "внедрением, добавляются как атрибуты ресурсов.",
        "Any attributes you have already set in `OTEL_RESOURCE_ATTRIBUTES` are "
        "preserved, and the above attributes are appended.": "Все атрибуты, которые вы уже задали в `OTEL_RESOURCE_ATTRIBUTES`, "
        "сохраняются, а перечисленные выше атрибуты добавляются к ним.",
        # mojibake: `auto` + nb-hyphen + `configuration` -> normalized key has "auto-configuration"
        "Resource attributes are always injected when auto-configuration is enabled, "
        "regardless of existing OTLP exporter settings or whether override mode is "
        "enabled.": "Атрибуты ресурсов всегда внедряются при включённой автонастройке, "
        "независимо от существующих настроек экспортёра OTLP и от того, включён ли "
        "режим переопределения.",
        "## Limitations": "## Ограничения",
        "### Application pods using `envFrom`": "### Поды приложений, использующие `envFrom`",
        "When you populate your environment variables using `envFrom`, Dynatrace "
        "Operator is not able to discover environment variables that are already set. "
        "In this case, the injected Dynatrace OTLP exporter config takes precedence "
        "over values coming from `envFrom`, even without using the [override mode]"
        "(#override).": "Когда вы заполняете переменные окружения с помощью `envFrom`, Dynatrace "
        "Operator не может обнаружить уже заданные переменные окружения. В этом случае "
        "внедрённая настройка экспортёра Dynatrace OTLP имеет приоритет над "
        "значениями из `envFrom`, даже без использования [режима переопределения]"
        "(#override).",
        "### Hardcoded SDK configuration": "### Жёстко заданная настройка SDK",
        "* In OTel SDKs, programmatic configuration takes precedence over environment "
        "variables. Ensure the standard exporter environment variables are supported "
        "by your application.": "* В OTel SDK программная настройка имеет приоритет над переменными "
        "окружения. Убедитесь, что стандартные переменные окружения экспортёра "
        "поддерживаются вашим приложением.",
        "* Dynatrace always uses protocol `http/protobuf`. If your application is "
        "restricted to gRPC, the injected protocol variable will have no effect and "
        "communication will fail.": "* Dynatrace всегда использует протокол `http/protobuf`. Если ваше "
        "приложение ограничено протоколом gRPC, внедрённая переменная протокола не "
        "будет иметь эффекта, и взаимодействие завершится сбоем.",
        "## Route OTLP traffic via ActiveGate": "## Маршрутизация трафика OTLP через ActiveGate",
        "If an in-cluster ActiveGate is deployed with the same DynaKube that is used "
        "for OTLP auto-configuration, the traffic is routed through this ActiveGate. "
        "Without the in-cluster ActiveGate the traffic is sent directly to your "
        "Dynatrace tenant.": "Если ActiveGate внутри кластера развёрнут с тем же DynaKube, который "
        "используется для автонастройки OTLP, трафик маршрутизируется через этот "
        "ActiveGate. Без ActiveGate внутри кластера трафик отправляется напрямую в "
        "ваш тенант Dynatrace.",
        "## Injection control": "## Управление внедрением",
        "### Namespace selector": "### Селектор пространств имён",
        "To limit auto-configuration to specific namespaces, you can use a namespace "
        "selector:": "Чтобы ограничить автонастройку определёнными пространствами имён, можно "
        "использовать селектор пространств имён:",
        "### Pod and container annotations": "### Аннотации подов и контейнеров",
        "For fine-grained control beyond the [namespace selector]"
        "(#namespace-selector), you can use annotations to control injection "
        "behaviour on the pods directly:": "Для более точного управления помимо [селектора пространств имён]"
        "(#namespace-selector) можно использовать аннотации, чтобы управлять "
        "поведением внедрения непосредственно на подах:",
        "Per default automatic injection and therefore OTLP exporter "
        "auto-configuration is enabled for all namespaces (controlled via "
        "[feature-flag](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "
        '"List the feature flags to configure Dynatrace Operator on Kubernetes.")).': "По умолчанию автоматическое внедрение и, следовательно, автонастройка "
        "экспортёра OTLP включены для всех пространств имён (управляется через "
        "[флаг функции](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "
        '"Список feature flags для настройки Dynatrace Operator в Kubernetes.")).',
        "You can control the OTLP exporter auto-configuration using either existing "
        "annotations that control all Dynatrace injections at once (see the "
        "[documentation]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#podexclusion "
        '"Configure monitoring for namespaces and pods") for more information) or by '
        "adding `otlp-exporter-configuration.dynatrace.com/inject: true/false` to a "
        "Pod.": "Управлять автонастройкой экспортёра OTLP можно либо с помощью существующих "
        "аннотаций, которые управляют всеми внедрениями Dynatrace одновременно (см. "
        "[документацию]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#podexclusion "
        '"Настройка мониторинга для пространств имён и подов") для получения '
        "дополнительной информации), либо добавив "
        "`otlp-exporter-configuration.dynatrace.com/inject: true/false` к поду.",
        "Known inconsistency in Dynatrace Operator 1.8": "Известная несогласованность в Dynatrace Operator 1.8",
        "There is a known inconsistency on how these flags work between OTLP exporter "
        "configuration injection and OneAgent injection. The value of "
        "`feature.dynatrace.com/inject` is used as default value for "
        "`dynatrace.com/inject`, the annotation "
        "`otlp-exporter-configuration.dynatrace.com/inject` defaults to `true`. This "
        "will be fixed in the next Dynatrace Operator release.": "Существует известная несогласованность в том, как эти флаги работают между "
        "внедрением настройки экспортёра OTLP и внедрением OneAgent. Значение "
        "`feature.dynatrace.com/inject` используется как значение по умолчанию для "
        "`dynatrace.com/inject`, а аннотация "
        "`otlp-exporter-configuration.dynatrace.com/inject` по умолчанию имеет "
        "значение `true`. Это будет исправлено в следующем выпуске Dynatrace "
        "Operator.",
        "Injection flag combinations": "Комбинации флагов внедрения",
        "| `dynatrace.com/inject` [1](#fn-1-1-def) | "
        "`otlp-exporter-configuration.dynatrace.com/inject` [2](#fn-1-2-def) | "
        "`feature.dynatrace.com/automatic-injection` [3](#fn-1-3-def) | Injected |": "| `dynatrace.com/inject` [1](#fn-1-1-def) | "
        "`otlp-exporter-configuration.dynatrace.com/inject` [2](#fn-1-2-def) | "
        "`feature.dynatrace.com/automatic-injection` [3](#fn-1-3-def) | Внедрено |",
        "| `false` | <n/a> | <n/a> | Not applicablenot injected |": "| `false` | <n/a> | <n/a> | Неприменимоне внедрено |",
        "| `true` / unset [4](#fn-1-4-def) | `false` | <n/a> | Not applicablenot "
        "injected |": "| `true` / unset [4](#fn-1-4-def) | `false` | <n/a> | Неприменимоне "
        "внедрено |",
        "| `true` / unset [4](#fn-1-4-def) | `true` | <n/a> | Applicableinjected |": "| `true` / unset [4](#fn-1-4-def) | `true` | <n/a> | Применимовнедрено |",
        "| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `true` / unset "
        "[4](#fn-1-4-def) | Applicableinjected |": "| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `true` / unset "
        "[4](#fn-1-4-def) | Применимовнедрено |",
        "| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `false` | Not "
        "applicablenot injected |": "| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `false` | "
        "Неприменимоне внедрено |",
        "[1](#fn-1-1-def) set on application Pod": "[1](#fn-1-1-def) задаётся на поде приложения",
        "[2](#fn-1-2-def) set on application Pod": "[2](#fn-1-2-def) задаётся на поде приложения",
        "[3](#fn-1-3-def) set on the DynaKube": "[3](#fn-1-3-def) задаётся на DynaKube",
        "[4](#fn-1-4-def) default `true`": "[4](#fn-1-4-def) по умолчанию `true`",
        "[5](#fn-1-5-def) value of `feature.dynatrace.com/automatic-injection` used as "
        "default": "[5](#fn-1-5-def) значение `feature.dynatrace.com/automatic-injection` "
        "используется по умолчанию",
        "## Enable environment variable overrides": "## Включение переопределений переменных окружения",
        "By default, any existing configuration (for example, already set environment "
        "variables) is not altered, overwritten, or removed. This includes all "
        "environment variables matching the pattern `OTEL_EXPORTER_OTLP_*`. If any of "
        "those environment variables already exist in a container specification, no "
        "automatic configuration is made **at all**, even if the activated signal does "
        "not directly conflict with the existing configuration.": "По умолчанию любая существующая настройка (например, уже заданные переменные "
        "окружения) не изменяется, не перезаписывается и не удаляется. Это включает "
        "все переменные окружения, соответствующие шаблону `OTEL_EXPORTER_OTLP_*`. "
        "Если какая-либо из этих переменных окружения уже существует в спецификации "
        "контейнера, автоматическая настройка не выполняется **вообще**, даже если "
        "активированный сигнал напрямую не конфликтует с существующей настройкой.",
        "For example, if only `traces` is activated in "
        "`.spec.otlpExporterConfiguration.signals` and the container has "
        "`OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` already set, "
        "`OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` won't be configured on your pod.": "Например, если в `.spec.otlpExporterConfiguration.signals` активированы "
        "только `traces`, а в контейнере уже задана "
        "`OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`, то "
        "`OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` не будет настроена на вашем поде.",
        "To enable this override, you can turn on the override mode:": "Чтобы включить это переопределение, можно включить режим переопределения:",
        "With `.spec.otlpExporterConfiguration.overrideEnvVars: true`, Dynatrace "
        "Operator will:": "При `.spec.otlpExporterConfiguration.overrideEnvVars: true` Dynatrace "
        "Operator будет:",
        "* Add configuration for signals not yet present (in this example, `metrics`)": "* Добавлять настройку для сигналов, которые ещё отсутствуют (в этом примере "
        "`metrics`)",
        "* Overwrite configuration for signals already present": "* Перезаписывать настройку для уже присутствующих сигналов",
        "* Retain existing configurations if they don't conflict with the configured "
        "signals": "* Сохранять существующие настройки, если они не конфликтуют с настроенными "
        "сигналами",
        "The following examples have the above DynaKube configuration with `metrics` "
        "enabled and `overrideEnvVars` set to `true`.": "В следующих примерах используется приведённая выше конфигурация DynaKube с "
        "включёнными `metrics` и `overrideEnvVars`, установленным в `true`.",
        "### Simple override": "### Простое переопределение",
        "**Before**": "**До**",
        "**After**": "**После**",
        "### Simple addition of the new signal": "### Простое добавление нового сигнала",
        "### OTLP general configuration environment variables": "### Переменные окружения общей настройки OTLP",
        "A special case is the use of `OTEL_EXPORTER_OTLP_ENDPOINT` and its companion "
        "environment variables. These variables provide defaults for all signals at "
        "once. If such a variable is already set for the container, it is not removed. "
        "Instead, the signal-specific configuration is added and takes precedence.": "Особый случай, это использование `OTEL_EXPORTER_OTLP_ENDPOINT` и "
        "сопутствующих ему переменных окружения. Эти переменные задают значения по "
        "умолчанию сразу для всех сигналов. Если такая переменная уже задана для "
        "контейнера, она не удаляется. Вместо этого добавляется настройка для "
        "конкретного сигнала, и она имеет приоритет.",
        "In this example, metrics will now be sent to the Dynatrace endpoint, while "
        "traces and logs would still be reported to the previously configured "
        "endpoint.": "В этом примере метрики теперь будут отправляться в конечную точку Dynatrace, "
        "а трассировки и логи по-прежнему будут отправляться в ранее настроенную "
        "конечную точку.",
        "## `NO_PROXY` support": "## Поддержка `NO_PROXY`",
        "If you choose to have an ActiveGate and a proxy configured on your "
        "application pods, the ActiveGate service is automatically added to the "
        "`NO_PROXY` environment variable. If the environment variable does not yet "
        "exist, it will be created.": "Если вы решите настроить ActiveGate и прокси на подах вашего приложения, "
        "сервис ActiveGate автоматически добавляется в переменную окружения "
        "`NO_PROXY`. Если эта переменная окружения ещё не существует, она будет "
        "создана.",
        "You can opt-out of of this by adding the following annotation to your "
        "DynaKube:": "От этого можно отказаться, добавив следующую аннотацию в ваш DynaKube:",
        "## Related topics": "## Связанные темы",
        "* [DynaKube parameters for Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.")': "* [Параметры DynaKube для Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.")',
    },
}

# Lines copied verbatim (bare identifiers / lines with no translatable prose).
PASS = {
    "container-buildtime.md": set(),
    "telemetry-ingest.md": {
        "| --- | --- | --- |",
    },
    "otlp-auto-config.md": {
        "| --- | --- |",
        "| --- | --- | --- | --- |",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    rel = REL[fname]
    en_path = os.path.join(BASE, "managed", rel)
    ru_path = os.path.join(BASE, "managed-ru", rel)
    en_lines = read_lf(en_path).split("\n")
    tmap = {normalize(k): v for k, v in TRANS[fname].items()}
    passset = {normalize(k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        stripped = normalize(ln.strip())
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        if stripped == "":
            out.append(ln)
            continue
        if stripped == "---":
            out.append(ln)
            continue
        if stripped.startswith("source:") or stripped.startswith("scraped:"):
            out.append(ln)
            continue
        if stripped in tmap:
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + tmap[stripped])
            continue
        if stripped in passset:
            out.append(ln)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    for fn in TRANS:
        build(fn)
