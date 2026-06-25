# -*- coding: utf-8 -*-
"""L4-IF.62 g3 builder: setup-on-k8s/guides/deployment-and-configuration/
monitoring-and-instrumentation batch (3 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM, no trailing newline).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for identifier headings / EN component/mode tab labels / bare filenames. Any
prose line missing from both raises SystemExit -> catches leftover-EN before
writing.

Mojibake in EN sources (stripped from both EN line and TRANS keys via MOJI_RE
so keys are written clean and RU stays clean):
- `﻿` / `\xef\xbb\xbf` (BOM mis-decoded as Latin-1) before some `]`.
- `\xe2\x80\x94` (em-dash mis-decoded as Latin-1) mid-sentence in k8s file L16.
"""

import os
import re

# Mojibake codepoints found in these EN sources:
#   U+FEFF                      BOM
#   U+00EF U+00BB U+00BF        UTF-8 BOM bytes decoded as Latin-1 ("ï»¿")
#   U+00E2 U+0080 U+0094        UTF-8 em-dash bytes decoded as Latin-1 ("â\x80\x94")
MOJI_RE = re.compile("[﻿ï»¿â]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = (
    "ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
    "monitoring-and-instrumentation"
)

# all three files live directly in monitoring-and-instrumentation/
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "annotate.md": {
        "title: Configure monitoring for namespaces and pods": "title: Настройка мониторинга для пространств имён и подов",
        "# Configure monitoring for namespaces and pods": "# Настройка мониторинга для пространств имён и подов",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Mar 19, 2026": "* Обновлено 19 марта 2026 г.",
        "As part of monitoring your Kubernetes cluster with cloud-native full-stack "
        "or application monitoring, when applying metadata enrichment or "
        "automatically configuring your OTLP exporters, you might want to restrict it "
        "to certain namespaces and pods.": "В рамках мониторинга кластера Kubernetes с помощью cloud-native "
        "full-stack или application monitoring, при применении обогащения "
        "метаданными или автоматической настройке экспортёров OTLP вам может "
        "понадобиться ограничить его определёнными пространствами имён и подами.",
        "By default, Dynatrace Operator injects into **all namespaces**, except for:": "По умолчанию Dynatrace Operator выполняет внедрение во **все пространства "
        "имён**, за исключением:",
        "* Namespaces prefixed with `kube-` or `openshift-`.": "* Пространства имён с префиксом `kube-` или `openshift-`.",
        "* The namespace where Dynatrace Operator was installed.": "* Пространство имён, в котором был установлен Dynatrace Operator.",
        "We highly recommend using the `namespaceSelector` fields (see below) to keep "
        "full control over what is injected.": "Настоятельно рекомендуем использовать поля `namespaceSelector` (см. ниже), "
        "чтобы сохранять полный контроль над тем, что внедряется.",
        "## Monitor specific namespaces": "## Мониторинг определённых пространств имён",
        "When configuring Dynatrace Operator to inject OneAgent, to apply metadata "
        "enrichment or automatically configure OTLP exporters only in certain "
        "namespaces, set the `namespaceSelector` parameter in the DynaKube custom "
        "resource.": "При настройке Dynatrace Operator для внедрения OneAgent, применения "
        "обогащения метаданными или автоматической настройки экспортёров OTLP только "
        "в определённых пространствах имён задайте параметр `namespaceSelector` в "
        "пользовательском ресурсе DynaKube.",
        "The `namespaceSelector` and annotations described here only affect the "
        "injection done by the webhook part of Dynatrace Operator. They don't affect "
        "the Kubernetes API monitoring capabilities of ActiveGate or the host-level "
        "monitoring done by OneAgent.": "Описанные здесь `namespaceSelector` и аннотации влияют только на внедрение, "
        "выполняемое вебхук-частью Dynatrace Operator. Они не влияют на возможности "
        "мониторинга Kubernetes API в ActiveGate или мониторинг на уровне хоста, "
        "выполняемый OneAgent.",
        "For more information, see [DynaKube parameters for Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") (`.spec.metadataEnrichment`, '
        "`.spec.oneAgent.cloudNativeFullStack`, "
        "`.spec.oneAgent.applicationMonitoring`, and "
        "`.spec.otlpExporterConfiguration` fields).": "Дополнительные сведения см. в разделе [Параметры DynaKube для Dynatrace "
        "Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.") (поля `.spec.metadataEnrichment`, '
        "`.spec.oneAgent.cloudNativeFullStack`, "
        "`.spec.oneAgent.applicationMonitoring` и "
        "`.spec.otlpExporterConfiguration`).",
        "1. Label your namespaces.": "1. Добавьте метки к пространствам имён.",
        "2. Modify your DynaKube by adding the `namespaceSelector` to specify the "
        "label for monitoring.": "2. Измените DynaKube, добавив `namespaceSelector`, чтобы указать метку для "
        "мониторинга.",
        "For more details about configuring labels for selective monitoring, see "
        "[Labels and selectors](https://dt-url.net/vj038vk).": "Подробнее о настройке меток для выборочного мониторинга см. [Метки и "
        "селекторы](https://dt-url.net/vj038vk).",
        "To add exceptions for specific pods within the selected namespaces, you can "
        "[annotate the respective pods](#podexclusion).": "Чтобы добавить исключения для определённых подов в выбранных пространствах "
        "имён, можно [добавить аннотации к соответствующим подам](#podexclusion).",
        "## Exclude specific namespaces": "## Исключение определённых пространств имён",
        "To exclude certain namespaces from being monitored, modify the DynaKube "
        "custom resource as follows.": "Чтобы исключить определённые пространства имён из мониторинга, измените "
        "пользовательский ресурс DynaKube следующим образом.",
        "* `key` defines the key of the label. Starting with Kubernetes version 1.22, "
        "a default label `kubernetes.io/metadata.name` is added to namespaces.": "* `key` определяет ключ метки. Начиная с Kubernetes версии 1.22, к "
        "пространствам имён добавляется метка по умолчанию "
        "`kubernetes.io/metadata.name`.",
        "* `values` define the value of the label.": "* `values` определяет значение метки.",
        "Example with Kubernetes default label": "Пример с меткой Kubernetes по умолчанию",
        "If you run `kubectl describe namespace dynatrace`, you'll see:": "Если выполнить `kubectl describe namespace dynatrace`, отобразится:",
        "A valid selector example to exclude `dynatrace` would be:": "Пример корректного селектора для исключения `dynatrace`:",
        "The webhook will inject every namespace that matches all "
        "`namespaceselector`.": "Вебхук выполнит внедрение в каждое пространство имён, которое "
        "соответствует всем `namespaceselector`.",
        "For more details, see [Resources that support set-based requirements]"
        "(https://dt-url.net/hi03yvm).": "Подробнее см. [Ресурсы, поддерживающие требования на основе множеств]"
        "(https://dt-url.net/hi03yvm).",
        "## Exclude specific pods in monitored namespaces": "## Исключение определённых подов в отслеживаемых пространствах имён",
        "To exclude specific pods within monitored namespaces, annotate the pods "
        "accordingly.": "Чтобы исключить определённые поды в отслеживаемых пространствах имён, "
        "добавьте к подам соответствующие аннотации.",
        "Annotations available for fine-grained control include.": "Для точного управления доступны следующие аннотации.",
        "* `dynatrace.com/inject`: Disables all injection when set to `false`. "
        "However, setting it to `true` will have no effect; the annotation can only "
        "be used to exclude pods from injection.": "* `dynatrace.com/inject`: отключает всё внедрение, если задано значение "
        "`false`. Однако установка значения `true` не даёт никакого эффекта; "
        "аннотацию можно использовать только для исключения подов из внедрения.",
        "* `metadata-enrichment.dynatrace.com/inject`: Prevents [metric enrichment "
        "file](/managed/ingest-from/extend-dynatrace/extend-data "
        '"Learn how to automatically enrich your telemetry data with '
        'Dynatrace-specific fields.") addition when `false`.': "* `metadata-enrichment.dynatrace.com/inject`: предотвращает добавление "
        "[файла обогащения метрик](/managed/ingest-from/extend-dynatrace/extend-data "
        '"Узнайте, как автоматически обогащать данные телеметрии полями, '
        'специфичными для Dynatrace.") при значении `false`.',
        "* `oneagent.dynatrace.com/inject`: Disables OneAgent modifications when set "
        "to `false`.": "* `oneagent.dynatrace.com/inject`: отключает изменения OneAgent, если "
        "задано значение `false`.",
        "* `otlp-exporter-configuration.dynatrace.com/inject`: Disables [OTLP "
        "exporter auto-configuration]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "
        '"Automatically configure the OTLP exporter in applications instrumented '
        'with OpenTelemetry SDKs using Dynatrace Operator.") when set to `false`.': "* `otlp-exporter-configuration.dynatrace.com/inject`: отключает "
        "[автоматическую настройку экспортёра OTLP]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "
        '"Автоматически настройте экспортёр OTLP в приложениях, '
        "инструментированных с помощью OpenTelemetry SDK, используя Dynatrace "
        'Operator.") при значении `false`.',
        "## Exclude specific containers in monitored pods": "## Исключение определённых контейнеров в отслеживаемых подах",
        "Dynatrace Operator version 1.0.0+": "Dynatrace Operator версии 1.0.0+",
        "To exclude specific container images within monitored namespaces, annotate "
        "the pods or DynaKube accordingly (this can be useful to, for example, "
        "exclude sidecar containers).": "Чтобы исключить определённые образы контейнеров в отслеживаемых "
        "пространствах имён, добавьте соответствующие аннотации к подам или DynaKube "
        "(это может быть полезно, например, для исключения sidecar-контейнеров).",
        "This annotation can be applied at the **DynaKube level (affecting all pods)** "
        "or at the **individual pod level (affecting only the specified pod)**.": "Эту аннотацию можно применить на **уровне DynaKube (затрагивает все "
        "поды)** или на **уровне отдельного пода (затрагивает только указанный "
        "под)**.",
        "This excludes the container from all types of injection (OneAgent/metadata)": "Это исключает контейнер из всех видов внедрения (OneAgent/метаданные)",
        "## Monitor only specific pods": "## Мониторинг только определённых подов",
        "Dynatrace Operator version 0.8.0+": "Dynatrace Operator версии 0.8.0+",
        "Dynatrace Operator can be set to monitor namespaces without injecting into "
        "any pods, so you can choose which pods to monitor.": "Dynatrace Operator можно настроить на мониторинг пространств имён без "
        "внедрения в какие-либо поды, чтобы вы могли выбрать, какие поды "
        "отслеживать.",
        "1. Disable the automatic injection feature for the DynaKube deployment to "
        "your cluster.": "1. Отключите функцию автоматического внедрения для развёртывания DynaKube "
        "в вашем кластере.",
        "2. Use label selectors or manual annotations on the namespaces you want to "
        "monitor selectively.": "2. Используйте селекторы меток или аннотации вручную для пространств имён, "
        "которые вы хотите отслеживать выборочно.",
        "3. Annotate the pods you intend to monitor.": "3. Добавьте аннотации к подам, которые вы собираетесь отслеживать.",
        "* Works with `oneagent.dynatrace.com/inject`, "
        "`metadata-enrichment.dynatrace.com/inject`, and "
        "`otlp-exporter-configuration.dynatrace.com/inject` annotation.": "* Работает с аннотациями `oneagent.dynatrace.com/inject`, "
        "`metadata-enrichment.dynatrace.com/inject` и "
        "`otlp-exporter-configuration.dynatrace.com/inject`.",
        "## Fine-tuning of injection for `applicationMonitoring` without CSI driver": "## Тонкая настройка внедрения для `applicationMonitoring` без CSI driver",
        "This section has been deprecated with Dynatrace Operator version 1.5.0 and "
        "superseded by the new [node image pull]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull") feature.': "Этот раздел устарел с версии Dynatrace Operator 1.5.0 и был заменён новой "
        "функцией [node image pull]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Настройка node image pull").',
        "* `oneagent.dynatrace.com/flavor`: Set to `default` or `musl` to specify the "
        "binary compatibility. This indicates whether `glibc` or `musl` binaries "
        "should be downloaded, with `glibc` as the default setting. For containers "
        "based on `musl` (for example, Alpine), specify this annotation to ensure "
        "proper monitoring.": "* `oneagent.dynatrace.com/flavor`: задайте значение `default` или `musl`, "
        "чтобы указать двоичную совместимость. Это определяет, какие двоичные файлы "
        "следует загружать, `glibc` или `musl`, при этом `glibc` является настройкой "
        "по умолчанию. Для контейнеров на основе `musl` (например, Alpine) укажите "
        "эту аннотацию, чтобы обеспечить корректный мониторинг.",
        "+ Ignored if the CSI volume is or the [node image pull]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull") feature is used.': "+ Игнорируется, если используется том CSI или функция [node image pull]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Настройка node image pull").',
        "* `oneagent.dynatrace.com/technologies`: A comma-separated list of "
        "technologies. This filters the code modules to be downloaded, defaulting to "
        "`all`. Use this to tailor the OneAgent to monitor specific technologies "
        "within your application.": "* `oneagent.dynatrace.com/technologies`: список технологий, разделённых "
        "запятыми. Это фильтрует загружаемые модули кода, при этом значением по "
        "умолчанию является `all`. Используйте это, чтобы настроить OneAgent на "
        "мониторинг определённых технологий в вашем приложении.",
        "+ Ignored if the CSI volume is used.": "+ Игнорируется, если используется том CSI.",
        "* `oneagent.dynatrace.com/install-path`: Specifies the path where the "
        "OneAgent directory will be mounted. By default, it is set to "
        "`/opt/dynatrace/oneagent-paas`. Adjust this path based on your environment "
        "or requirements.": "* `oneagent.dynatrace.com/install-path`: указывает путь, по которому будет "
        "смонтирован каталог OneAgent. По умолчанию задано значение "
        "`/opt/dynatrace/oneagent-paas`. Скорректируйте этот путь в соответствии с "
        "вашим окружением или требованиями.",
        "Below is an example showcasing how to apply these annotations within your "
        "deployment.": "Ниже приведён пример, показывающий, как применить эти аннотации в вашем "
        "развёртывании.",
    },
    "instrument-nginx.md": {
        "title: Instrument ingress-nginx": "title: Инструментирование ingress-nginx",
        "# Instrument ingress-nginx": "# Инструментирование ingress-nginx",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Mar 18, 2026": "* Обновлено 18 марта 2026 г.",
        "The instructions below are relevant only for the [official Kubernetes "
        "ingress controller implementation from Google](https://dt-url.net/xr03xh3).": "Приведённые ниже инструкции актуальны только для [официальной реализации "
        "ingress-контроллера Kubernetes от Google](https://dt-url.net/xr03xh3).",
        "* Derivatives from the official project, such as the [Bitnami ingress "
        "controller](https://dt-url.net/ns03xjt), are not supported. However, you "
        "may instrument them manually by using the [runtime instrumentation]"
        "(/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "
        '"Learn how to force instrumenting patched/non-standard NGINX binaries '
        'during runtime.") for NGINX.': "* Производные от официального проекта, такие как [ingress-контроллер "
        "Bitnami](https://dt-url.net/ns03xjt), не поддерживаются. Однако вы можете "
        "инструментировать их вручную с помощью [инструментирования во время "
        "выполнения]"
        "(/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "
        '"Узнайте, как принудительно инструментировать пропатченные/'
        'нестандартные двоичные файлы NGINX во время выполнения.") для NGINX.',
        "* Chainguard's ingress-nginx-controller is a fork of the official "
        "Kubernetes ingress-nginx-controller (use the same instructions below). Use "
        "the `-debug` image variant (for example, "
        "`ingress-nginx-controller:latest-debug`) which includes the nginx debug "
        "symbols needed for runtime instrumentation.": "* ingress-nginx-controller от Chainguard является форком официального "
        "ingress-nginx-controller Kubernetes (используйте те же инструкции ниже). "
        "Используйте вариант образа `-debug` (например, "
        "`ingress-nginx-controller:latest-debug`), который включает отладочные "
        "символы nginx, необходимые для инструментирования во время выполнения.",
        "* The [ingress controller implementation from F5 NGINX]"
        "(https://dt-url.net/ph43xrd) can be instrumented automatically; no manual "
        "steps are required.": "* [Реализацию ingress-контроллера от F5 NGINX]"
        "(https://dt-url.net/ph43xrd) можно инструментировать автоматически; "
        "никаких действий вручную не требуется.",
        "The NGINX process of the official Kubernetes ingress-nginx controller "
        "container image can't be instrumented automatically. To manually instrument "
        "ingress-nginx on Kubernetes, follow the instructions below.": "Процесс NGINX в образе контейнера официального ingress-nginx контроллера "
        "Kubernetes невозможно инструментировать автоматически. Чтобы "
        "инструментировать ingress-nginx в Kubernetes вручную, следуйте приведённым "
        "ниже инструкциям.",
        "## Prerequisites": "## Предварительные требования",
        "ARM64 architecture is not supported.": "Архитектура ARM64 не поддерживается.",
        "* OneAgent version 1.227+": "* OneAgent версии 1.227+",
        "* The pod name must contain the substring `ingress-nginx-` to ensure proper "
        "instrumentation of the NGINX binary. We recommend maintaining the default "
        "pod name `ingress-nginx-controller`.": "* Имя пода должно содержать подстроку `ingress-nginx-`, чтобы обеспечить "
        "корректное инструментирование двоичного файла NGINX. Рекомендуем сохранять "
        "имя пода по умолчанию `ingress-nginx-controller`.",
        "## Instrument Kubernetes ingress-nginx": "## Инструментирование ingress-nginx в Kubernetes",
        "To instrument ingress-nginx on Kubernetes, you need to load the NGINX module "
        "manually via a ConfigMap.": "Чтобы инструментировать ingress-nginx в Kubernetes, необходимо вручную "
        "загрузить модуль NGINX через ConfigMap.",
        "Ensure that OneAgent is running and capable of instrumenting the "
        "ingress-nginx containers when applying changes to the ingress-nginx "
        "ConfigMap. If these conditions are not met, NGINX will fail to start.": "Убедитесь, что OneAgent запущен и способен инструментировать контейнеры "
        "ingress-nginx при применении изменений к ConfigMap ingress-nginx. Если эти "
        "условия не выполнены, NGINX не запустится.",
        "1. Edit the ConfigMap.": "1. Отредактируйте ConfigMap.",
        "2. Add the following value to the `main-snippet` key (below `data`).": "2. Добавьте следующее значение к ключу `main-snippet` (под `data`).",
        "Example:": "Пример:",
        "For `cloudNativeFullStack` and `applicationMonitoring` deployments, the path "
        "becomes:": "Для развёртываний `cloudNativeFullStack` и `applicationMonitoring` путь "
        "становится следующим:",
        "## Verify your configuration": "## Проверка вашей конфигурации",
        "If your pod isn't up and running, make sure that it hasn't exceeded either "
        "of the following:": "Если ваш под не запущен и не работает, убедитесь, что он не превысил ни "
        "один из следующих лимитов:",
        "* Its resource quota (especially for memory).": "* Свою квоту ресурсов (особенно по памяти).",
        "* The initial liveness/readiness probe timeouts. You might need to increase "
        "`initialDelaySeconds` for these probes.": "* Начальные тайм-ауты проверок liveness/readiness. Возможно, вам "
        "потребуется увеличить `initialDelaySeconds` для этих проверок.",
    },
    "k8s-api-monitoring.md": {
        "title: Kubernetes API Monitoring": "title: Мониторинг Kubernetes API",
        "# Kubernetes API Monitoring": "# Мониторинг Kubernetes API",
        "* 8-min read": "* Чтение: 8 мин",
        "* Updated on Dec 09, 2025": "* Обновлено 9 декабря 2025 г.",
        "Dynatrace obtains information about Kubernetes entities and metadata by "
        "querying the Kubernetes API. This information is used for [out-of-the-box "
        "alerting for Kubernetes]"
        "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "
        '"Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or '
        'workload level.") and to provide all observability signals in a proper '
        "Kubernetes context within the Dynatrace platform, for example, by creating "
        "relationships among applications, (micro-)services, databases, and "
        "Kubernetes entities such as pods, namespaces, and nodes.": "Dynatrace получает информацию о сущностях и метаданных Kubernetes, "
        "запрашивая Kubernetes API. Эта информация используется для [готового "
        "оповещения для Kubernetes]"
        "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "
        '"Настройка оповещений на уровне кластера, узла, пространства имён или '
        'рабочей нагрузки Kubernetes/OpenShift.") и для предоставления всех '
        "сигналов наблюдаемости в правильном контексте Kubernetes на платформе "
        "Dynatrace, например, путём создания связей между приложениями, "
        "(микро)сервисами, базами данных и сущностями Kubernetes, такими как поды, "
        "пространства имён и узлы.",
        "Dynatrace Operator manages the lifecycle of all Dynatrace components within "
        "a Kubernetes cluster and can be configured by deploying a DynaKube Custom "
        "Resource. Dynatrace ActiveGatethe Dynatrace component required to monitor "
        "the Kubernetes APIoffers a capability for Kubernetes API Monitoring.": "Dynatrace Operator управляет жизненным циклом всех компонентов Dynatrace в "
        "кластере Kubernetes и может быть настроен путём развёртывания "
        "пользовательского ресурса DynaKube. Dynatrace ActiveGate, компонент "
        "Dynatrace, необходимый для мониторинга Kubernetes API, предоставляет "
        "возможность мониторинга Kubernetes API.",
        "Follow the steps below to enable Kubernetes API monitoring.": "Чтобы включить мониторинг Kubernetes API, выполните приведённые ниже шаги.",
        "**Install Dynatrace Operator**](#install-dto)[![Step 2]"
        '(https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': "**Установка Dynatrace Operator**](#install-dto)[![Step 2]"
        '(https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
        "**Configure DynaKube**](#configure-dynakube)[![Step 3]"
        '(https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': "**Настройка DynaKube**](#configure-dynakube)[![Step 3]"
        '(https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
        "**Connect ActiveGate with Kubernetes API**](#connect-ag)": "**Подключение ActiveGate к Kubernetes API**](#connect-ag)",
        "## Step 1 Install Dynatrace Operator": "## Шаг 1. Установка Dynatrace Operator",
        "[Install Dynatrace Operator in any deployment mode]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Deploy Dynatrace Operator on Kubernetes")': "[Установите Dynatrace Operator в любом режиме развёртывания]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Развёртывание Dynatrace Operator в Kubernetes")',
        "## Step 2 Configure DynaKube": "## Шаг 2. Настройка DynaKube",
        "Configure the **ActiveGate** values of the DynaKube according to the [list "
        "of parameters]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#ag "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") and add `kubernetes-monitoring` to the ActiveGate '
        "capabilities.": "Настройте значения **ActiveGate** для DynaKube в соответствии со [списком "
        "параметров]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#ag "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.") и добавьте `kubernetes-monitoring` в возможности '
        "ActiveGate.",
        "## Step 3 Connect ActiveGate with Kubernetes API": "## Шаг 3. Подключение ActiveGate к Kubernetes API",
        "You have two options:": "У вас есть два варианта:",
        "* Connect the containerized ActiveGate to a local Kubernetes API endpoint.": "* Подключить контейнеризованный ActiveGate к локальной конечной точке "
        "Kubernetes API.",
        "* Connect the containerized ActiveGate to the public Kubernetes API URL.": "* Подключить контейнеризованный ActiveGate к публичному URL Kubernetes "
        "API.",
        "See below for instructions for both options.": "Инструкции для обоих вариантов приведены ниже.",
        "### Connect to a local Kubernetes API endpoint": "### Подключение к локальной конечной точке Kubernetes API",
        "You can enable monitoring by connecting a containerized ActiveGate to a "
        "local Kubernetes API endpoint.": "Вы можете включить мониторинг, подключив контейнеризованный ActiveGate к "
        "локальной конечной точке Kubernetes API.",
        "There are two ways to connect to the local Kubernetes API endpoint:": "Существует два способа подключения к локальной конечной точке Kubernetes "
        "API:",
        "* Recommended [Let Dynatrace Operator automatically handle the connection]"
        "(#auto)": "* Рекомендуется [позволить Dynatrace Operator автоматически управлять "
        "подключением](#auto)",
        "* [Configure the connection manually](#manual)": "* [Настроить подключение вручную](#manual)",
        "See below for details on both methods.": "Подробности об обоих методах приведены ниже.",
        "This feature flag is deprecated and enabled by default starting from "
        "Dynatrace Operator version 0.13.0.": "Этот флаг функции устарел и включён по умолчанию начиная с версии "
        "Dynatrace Operator 0.13.0.",
        "To connect automatically to the local Kubernetes API endpoint": "Чтобы подключиться автоматически к локальной конечной точке Kubernetes API",
        "1. Make sure to enable the **Read entities**, **Read settings**, and **Write "
        "settings** permissions (API v2) for your access token (see [Access tokens "
        "and permissions]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster")).': "1. Обязательно включите разрешения **Read entities**, **Read settings** и "
        "**Write settings** (API v2) для своего токена доступа (см. [Токены доступа "
        "и разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройка токенов и разрешений для мониторинга кластера Kubernetes")).',
        "2. Make sure that you have the `kubernetes-monitoring` capability enabled in "
        "your DynaKube custom resource.": "2. Убедитесь, что в вашем пользовательском ресурсе DynaKube включена "
        "возможность `kubernetes-monitoring`.",
        "3. Add the following annotation (see example below).": "3. Добавьте следующую аннотацию (см. пример ниже).",
        "After adding this annotation, the name of the cluster displayed in Dynatrace "
        "will be the same as the DynaKube custom resource where the annotation is "
        "configured. You can change the cluster name displayed in Dynatrace by "
        "adding the "
        "`feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "
        '"custom-cluster-name"` annotation as well.': "После добавления этой аннотации имя кластера, отображаемое в Dynatrace, "
        "будет совпадать с пользовательским ресурсом DynaKube, в котором настроена "
        "аннотация. Имя кластера, отображаемое в Dynatrace, можно изменить, также "
        "добавив аннотацию "
        "`feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "
        '"custom-cluster-name"`.',
        "Example with custom cluster name:": "Пример с пользовательским именем кластера:",
        "4. Apply your configuration.": "4. Примените вашу конфигурацию.",
        "To disable the configuration, remove the annotation.": "Чтобы отключить конфигурацию, удалите аннотацию.",
        "To connect to a local Kubernetes API endpoint manually, you only need to "
        "provide the unique Kubernetes cluster ID (the uuid of the kube-system "
        "namespace). The containerized ActiveGate then identifies the unique cluster "
        "ID and sends it over to Dynatrace.": "Чтобы подключиться к локальной конечной точке Kubernetes API вручную, вам "
        "нужно только указать уникальный идентификатор кластера Kubernetes (uuid "
        "пространства имён kube-system). Контейнеризованный ActiveGate затем "
        "определяет уникальный идентификатор кластера и отправляет его в Dynatrace.",
        "#### Step 1 Get the Kubernetes cluster ID": "#### Шаг 1. Получение идентификатора кластера Kubernetes",
        "Run the command below and grab the UID from the output.": "Выполните приведённую ниже команду и возьмите UID из вывода.",
        "#### Step 2 Provide the Kubernetes cluster ID in Dynatrace": "#### Шаг 2. Указание идентификатора кластера Kubernetes в Dynatrace",
        "1. Go to **Kubernetes**.": "1. Перейдите в **Kubernetes**.",
        "2. Select **Connect manually**.": "2. Выберите **Connect manually**.",
        "3. On the Kubernetes cluster connection settings page, provide a **Name**, "
        "and then turn on **Connect containerized ActiveGate to local Kubernetes API "
        "endpoint**.": "3. На странице настроек подключения кластера Kubernetes укажите **Name**, а "
        "затем включите **Connect containerized ActiveGate to local Kubernetes API "
        "endpoint**.",
        "4. For **Kubernetes cluster ID**, enter the UID obtained earlier.": "4. В поле **Kubernetes cluster ID** введите UID, полученный ранее.",
        "5. Select **Save changes** to save your configuration.": "5. Выберите **Save changes**, чтобы сохранить вашу конфигурацию.",
        "You can save your configuration even if the ActiveGate isn't ready to "
        "connect, and finish the configuration later. To verify if it's ready, "
        "select **Test configuration**.": "Вы можете сохранить вашу конфигурацию, даже если ActiveGate не готов к "
        "подключению, и завершить настройку позже. Чтобы проверить готовность, "
        "выберите **Test configuration**.",
        "### Connect to the public Kubernetes API": "### Подключение к публичному Kubernetes API",
        "To connect to the public Kubernetes API, follow the instructions that apply "
        "to your Kubernetes version:": "Чтобы подключиться к публичному Kubernetes API, следуйте инструкциям, "
        "которые применимы к вашей версии Kubernetes:",
        "* [Kubernetes version 1.24+](#k8s-new)": "* [Kubernetes версии 1.24+](#k8s-new)",
        "* [Kubernetes version earlier than 1.24](#k8s-old)": "* [Kubernetes версии ранее 1.24](#k8s-old)",
        "#### Kubernetes version 1.24+": "#### Kubernetes версии 1.24+",
        "1. Get the Kubernetes API URL.": "1. Получите URL Kubernetes API.",
        "If you set `enableIstio` to `true` in the [DynaKube custom resource]"
        "(https://dt-url.net/dynakube-samples), use the command below to get the "
        "Kubernetes API URL:": "Если вы задали для `enableIstio` значение `true` в [пользовательском "
        "ресурсе DynaKube](https://dt-url.net/dynakube-samples), используйте "
        "приведённую ниже команду, чтобы получить URL Kubernetes API:",
        "2. Create a file named `token-secret.yaml` with the following content:": "2. Создайте файл с именем `token-secret.yaml` со следующим содержимым:",
        "3. Apply the file to create the `dynatrace-activegate` secret.": "3. Примените файл, чтобы создать секрет `dynatrace-activegate`.",
        "4. Get the bearer token.": "4. Получите токен bearer.",
        "5. Go to **Kubernetes** and select **Connect manually**.": "5. Перейдите в **Kubernetes** и выберите **Connect manually**.",
        "6. On the Kubernetes cluster connection settings page, provide a **Name**, "
        "the **Kubernetes API URL**, and the **Bearer token** for the Kubernetes "
        "cluster.": "6. На странице настроек подключения кластера Kubernetes укажите **Name**, "
        "**Kubernetes API URL** и **Bearer token** для кластера Kubernetes.",
        "7. Select **Save changes**.": "7. Выберите **Save changes**.",
        "#### Kubernetes version earlier than 1.24": "#### Kubernetes версии ранее 1.24",
        "2. Get the bearer token.": "2. Получите токен bearer.",
        "Special instructions for Rancher distributions to get the API URL and the "
        "bearer token": "Особые инструкции для дистрибутивов Rancher по получению URL API и токена "
        "bearer",
        "For **Rancher distributions** of Kubernetes, you need to use the bearer "
        "token and API URL **of the Rancher server**, because this server manages "
        "and secures traffic to the Kubernetes API server. Follow the steps below.": "Для **дистрибутивов Rancher** Kubernetes необходимо использовать токен "
        "bearer и URL API **сервера Rancher**, поскольку этот сервер управляет "
        "трафиком к серверу Kubernetes API и защищает его. Выполните приведённые "
        "ниже шаги.",
        "1. Get the **Kubernetes API URL**.": "1. Получите **Kubernetes API URL**.",
        "2. Configure a user.": "2. Настройте пользователя.",
        "In the Rancher web UI, either create a new user or use an existing user to "
        "associate with the token. We recommend creating a new user.": "В веб-интерфейсе Rancher создайте нового пользователя или используйте "
        "существующего, чтобы связать его с токеном. Рекомендуем создать нового "
        "пользователя.",
        "3. Set permissions.": "3. Задайте разрешения.",
        "Make sure the user has either **Owner** or **Custom** permissions to the "
        "cluster you want to monitor.": "Убедитесь, что у пользователя есть разрешения **Owner** или **Custom** для "
        "кластера, который вы хотите отслеживать.",
        "**Recommended:** select **Custom** permissions, and be sure to select these "
        "two roles: **View all Projects** and **View Nodes**.": "**Рекомендуется:** выберите разрешения **Custom** и обязательно выберите "
        "эти две роли: **View all Projects** и **View Nodes**.",
        "4. Create an API key.": "4. Создайте ключ API.",
        "Go to **API & Keys** and create a key either for your specific account "
        "(enter your cluster name) or for all clusters (enter **No scope**). For "
        "security reasons, we recommend selecting the first option.": "Перейдите в **API & Keys** и создайте ключ либо для вашей конкретной "
        "учётной записи (введите имя вашего кластера), либо для всех кластеров "
        "(введите **No scope**). По соображениям безопасности рекомендуем выбрать "
        "первый вариант.",
        "Newly created keys display four fields. Make sure to use the content of the "
        "field called **Bearer token** to set up the connection to the Kubernetes "
        "API described in the next section.": "Вновь созданные ключи отображают четыре поля. Обязательно используйте "
        "содержимое поля под названием **Bearer token** для настройки подключения к "
        "Kubernetes API, описанной в следующем разделе.",
        "3. Go to **Kubernetes** and select **Connect manually**.": "3. Перейдите в **Kubernetes** и выберите **Connect manually**.",
        "4. On the Kubernetes cluster connection settings page, provide a **Name**, "
        "the **Kubernetes API URL**, and the **Bearer token** for the Kubernetes "
        "cluster.": "4. На странице настроек подключения кластера Kubernetes укажите **Name**, "
        "**Kubernetes API URL** и **Bearer token** для кластера Kubernetes.",
        "For Rancher distributions, you need the bearer token that was created in the "
        "Rancher web UI, as described in **Special instructions for Rancher "
        "distributions to get the API URL and the bearer token** above.": "Для дистрибутивов Rancher необходим токен bearer, созданный в "
        "веб-интерфейсе Rancher, как описано в разделе **Особые инструкции для "
        "дистрибутивов Rancher по получению URL API и токена bearer** выше.",
        "5. Select **Save changes**.": "5. Выберите **Save changes**.",
        "## Other Options": "## Другие варианты",
        "* If you can't use Dynatrace Operator, you can [deploy ActiveGate directly "
        "as a StatefulSet]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "
        '"Install and configure ActiveGate in Kubernetes as a StatefulSet.") (not '
        "recommended).": "* Если вы не можете использовать Dynatrace Operator, вы можете "
        "[развернуть ActiveGate напрямую как StatefulSet]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "
        '"Установка и настройка ActiveGate в Kubernetes как StatefulSet.") (не '
        "рекомендуется).",
        "* If you want to monitor several Kubernetes clusters with one ActiveGate and "
        "don't need to separate networks for administrative or operational traffic, "
        "you can [install an ActiveGate on a virtual machine using a conventional "
        "installer](/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm "
        '"Set up and configure an ActiveGate for Kubernetes platform monitoring in a '
        'virtual machine.").': "* Если вы хотите отслеживать несколько кластеров Kubernetes с помощью "
        "одного ActiveGate и вам не нужно разделять сети для административного или "
        "операционного трафика, вы можете [установить ActiveGate на виртуальной "
        "машине с помощью обычного установщика]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm "
        '"Настройка и конфигурирование ActiveGate для мониторинга платформы '
        'Kubernetes на виртуальной машине.").',
        "Dynatrace recommends to use the containerized ActiveGate for Kubernetes API "
        "monitoring": "Dynatrace рекомендует использовать контейнеризованный ActiveGate для "
        "мониторинга Kubernetes API",
        "## FAQ": "## Часто задаваемые вопросы",
        "Can I change settings for Kubernetes API monitoring?": "Можно ли изменить настройки мониторинга Kubernetes API?",
        "You can change Kubernetes cluster connection and monitoring settings at any "
        "time from your Kubernetes cluster details page.": "Вы можете изменить настройки подключения и мониторинга кластера Kubernetes "
        "в любое время на странице сведений о кластере Kubernetes.",
        "2. Find your Kubernetes cluster, and then select **Actions** > "
        "**Settings**.": "2. Найдите ваш кластер Kubernetes, а затем выберите **Actions** > "
        "**Settings**.",
        "3. Adjust your settings, and then select **Save changes**.": "3. Скорректируйте свои настройки, а затем выберите **Save changes**.",
        "How can I delete the Kubernetes Platform Monitoring configuration for a "
        "Kubernetes cluster?": "Как удалить конфигурацию Kubernetes Platform Monitoring для кластера "
        "Kubernetes?",
        "To delete the connection to a local Kubernetes API endpoint": "Чтобы удалить подключение к локальной конечной точке Kubernetes API",
        "3. Select **Use defaults**, and then select **Save changes**.": "3. Выберите **Use defaults**, а затем выберите **Save changes**.",
        "When does the ActiveGate get updated?": "Когда обновляется ActiveGate?",
        "ActiveGate is updated automatically on pod restart whenever there is a new "
        "version available, unless the image version is specified in `cr.yaml`.": "ActiveGate обновляется автоматически при перезапуске пода всякий раз, "
        "когда доступна новая версия, если только версия образа не указана в "
        "`cr.yaml`.",
    },
}

# Lines copied verbatim (identifier headings / EN component & mode tab labels /
# image lines whose alt-text stays EN / bare filenames). Corpus-consistent:
# Kubernetes/OpenShift tab labels and mode tab labels (Application monitoring,
# Metadata enrichment, ...) are kept English across the managed-ru K8s guides.
PASS = {
    "annotate.md": {
        # deployment-mode / feature identifiers (tab selectors)
        "cloudNativeFullStack",
        "applicationMonitoring",
        "metadataEnrichment",
        # Kubernetes/OpenShift code-tab labels
        "Kubernetes",
        "OpenShift",
        # mode tab labels (kept EN, corpus-consistent)
        "Metadata enrichment",
        "Cloud-native full-stack monitoring",
        "Application monitoring",
        "OTLP exporter configuration",
    },
    "instrument-nginx.md": {
        # Kubernetes/OpenShift code-tab labels (none here, but keep set non-fatal)
    },
    "k8s-api-monitoring.md": {
        # image line: alt-text stays EN (corpus has ~0 translated alt)
        '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
        # connection-method tab labels
        "Connect automatically",
        "Connect manually",
        # Kubernetes/OpenShift code-tab labels
        "Kubernetes",
        "OpenShift",
        "OpenShift v3.x",
        "OpenShift v4.x",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL.get(fname, SUB)
    en_path = os.path.join(BASE, "managed", sub, fname)
    ru_path = os.path.join(BASE, "managed-ru", sub, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {MOJI_RE.sub("", k): v for k, v in TRANS[fname].items()}
    passset = {MOJI_RE.sub("", k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        stripped = MOJI_RE.sub("", ln.strip())
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
            # write the mojibake-cleaned form so RU stays clean
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + stripped)
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
