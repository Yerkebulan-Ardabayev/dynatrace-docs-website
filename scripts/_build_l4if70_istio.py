# -*- coding: utf-8 -*-
"""L4-IF.70 builder: ingest-from/opentelemetry/integrations/istio.md"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/integrations"
FNAME = "istio.md"

# Tooltip strings reused across link tooltips in this file
TT_FSM = "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged."
TT_HU = "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units."
TT_PE = "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model."
TT_CT = (
    "Understand how DDU consumption is calculated for spans ingested via the Trace API."
)
TT_META = "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability."
TT_TI = "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest."
TT_DEPL = "Deploy Dynatrace Operator on Kubernetes"
TT_ISTIO = "Deployment of Dynatrace Operator alongside Istio in various scenarios"

# RU tooltip prose (value side). Link TEXT was translated in the first pass, but the
# tooltip prose was left EN (blindspot #9: leftover-scan sees Cyrillic in link text
# and skips the line). These translate the "title" prose; reuse dominant corpus forms.
RU_FSM = "Узнайте, как тарифицируется и оплачивается ваше потребление возможности Dynatrace Full-Stack Monitoring DPS."
RU_HU = "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units."
RU_PE = "Узнайте, как рассчитывается потребление расширений платформы Dynatrace с использованием модели Dynatrace Platform Subscription."
RU_CT = (
    "Узнайте, как рассчитывается потребление DDU для спанов, принятых через Trace API."
)
RU_META = "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes, присоединяя релевантные метаданные к таким сущностям, как поды, хосты и процессы, для лучшей наблюдаемости."
RU_TI = "Включите эндпоинты приёма телеметрии Dynatrace в Kubernetes для приёма данных локально в кластере."
RU_DEPL = "Развёртывание Dynatrace Operator в Kubernetes"
RU_ISTIO = "Развёртывание Dynatrace Operator совместно с Istio в различных сценариях."

# NOTE: norm() strips BOM (ï»¿ / \xef\xbf\xbd etc.) before key lookup,
# so all keys below use the CLEAN (BOM-free) form of the source line.

TRANS = {
    # frontmatter
    "title: Configure OpenTelemetry tracing with Istio": "title: Настройка трассировки OpenTelemetry с Istio",
    # headings
    "# Configure OpenTelemetry tracing with Istio": "# Настройка трассировки OpenTelemetry с Istio",
    # metadata bullets
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Apr 07, 2026": "* Обновлено 07 апреля 2026 г.",
    # support-statement callout header
    "Support statement": "Заявление о поддержке",
    "This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.": "Данная интеграция основана на открытом исходном коде, управляемом соответствующими сообществами, и не подпадает под политику поддержки Dynatrace. Хотя мы стремимся оказывать помощь, об ошибках и запросах на добавление функций следует сообщать непосредственно в соответствующий проект. Dynatrace не может гарантировать исправления или новые функции в силу независимой природы проектов с открытым исходным кодом.",
    "Always use the most recent release version to ensure you have the latest patches and fixes deployed.": "Всегда используйте самую последнюю версию выпуска, чтобы гарантировать наличие актуальных исправлений и патчей.",
    # L21 — BOM stripped by norm(), key is the clean form
    "This page describes how to use Istio version 1.22+ with the [Istio OpenTelemetry extension provider](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider), and how to configure it to export OpenTelemetry traces to Dynatrace.": "На этой странице описывается, как использовать Istio версии 1.22+ с [провайдером расширения OpenTelemetry для Istio](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider) и как настроить его для экспорта трассировок OpenTelemetry в Dynatrace.",
    # System requirements
    "### System requirements": "### Системные требования",
    "Istio version 1.22+ (i.e., Istio releases that ship with Envoy 1.30+) is required to configure Istio OpenTelemetry trace configuration, including Dynatrace resource detection and sampling.": "Для настройки конфигурации трассировки Istio OpenTelemetry, включая обнаружение ресурсов Dynatrace и сэмплирование, требуется Istio версии 1.22+ (то есть выпуски Istio, поставляемые с Envoy 1.30+).",
    # Licensing impact
    "## Licensing impact": "## Влияние на лицензирование",
    # L29 — BOM in source stripped by norm()
    "In certain deployment setups, tracing with Istio version 1.22+ results in consumption of the following [rate card](https://www.dynatrace.com/pricing/) capabilities:": "В некоторых конфигурациях развёртывания трассировка с Istio версии 1.22+ приводит к потреблению следующих возможностей [прайс-листа](https://www.dynatrace.com/pricing/):",
    "* When using the Dynatrace resource detector and sampler:": "* При использовании детектора ресурсов и сэмплера Dynatrace:",
    # L33 — stripped key starts with "+" (no leading spaces after strip)
    '+ Classic Full-Stack or cloud-native Full-Stack deployments: Usage is included in [Full-Stack Monitoring (DPS)](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "%s") and [Host Units (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "%s").'
    % (
        TT_FSM,
        TT_HU,
    ): '+ Развёртывания Classic Full-Stack или cloud-native Full-Stack: использование включено в [Full-Stack Monitoring (DPS)](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "%s") и [Host Units (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "%s").'
    % (RU_FSM, RU_HU),
    # L34
    '+ For Application-Observability-only deployments: Usage incurs consumption of [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "%s") or [DDUs for custom traces (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces "%s").'
    % (
        TT_PE,
        TT_CT,
    ): '+ Для развёртываний только с Application Observability: использование приводит к потреблению [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "%s") или [DDU для пользовательских трассировок (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces "%s").'
    % (RU_PE, RU_CT),
    # L35
    '* Without the Dynatrace resource detector and sampler: Usage incurs consumption of [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "%s") or [DDUs for custom traces (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces "%s").'
    % (
        TT_PE,
        TT_CT,
    ): '* Без детектора ресурсов и сэмплера Dynatrace: использование приводит к потреблению [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "%s") или [DDU для пользовательских трассировок (Dynatrace Classic License)](/managed/license/monitoring-consumption-classic/davis-data-units/custom-traces "%s").'
    % (RU_PE, RU_CT),
    # Deployment considerations
    "## Deployment considerations": "## Соображения по развёртыванию",
    "It's possible to configure Istio OpenTelemetry tracing in a standalone deployment or in combination with Dynatrace Operator.": "Трассировку Istio OpenTelemetry можно настроить в автономном развёртывании или в сочетании с Dynatrace Operator.",
    "### Deployment in combination with Dynatrace Operator Recommended": "### Развёртывание в сочетании с Dynatrace Operator (рекомендуется)",
    'We recommend using the Istio OpenTelemetry integration in combination with a Dynatrace Operator deployment with [metadata enrichment](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "%s") and [telemetry ingest endpoints](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "%s") enabled. Other features like OneAgent or ActiveGate are not required.'
    % (
        TT_META,
        TT_TI,
    ): 'Рекомендуется использовать интеграцию Istio OpenTelemetry в сочетании с развёртыванием Dynatrace Operator с включёнными [обогащением метаданных](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "%s") и [эндпоинтами приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "%s"). Другие компоненты, такие как OneAgent или ActiveGate, не требуются.'
    % (RU_META, RU_TI),
    "This provides the following benefits compared to standalone usage:": "Это обеспечивает следующие преимущества по сравнению с автономным использованием:",
    "* Resilient and more efficient delivery of traces by providing retry and batching capabilities.": "* Надёжная и более эффективная доставка трассировок благодаря возможностям повторных попыток и группирования.",
    "* Optional routing through ActiveGate.": "* Опциональная маршрутизация через ActiveGate.",
    "* No additional access token required.": "* Дополнительный токен доступа не требуется.",
    "* No additional `ServiceEntries` required.": "* Дополнительные `ServiceEntries` не требуются.",
    "* Compatibility with Dynatrace Operator `enableIstio`.": "* Совместимость с параметром `enableIstio` Dynatrace Operator.",
    "### Standalone deployment": "### Автономное развёртывание",
    "It's possible to ingest Istio traces without a Dynatrace Operator instance deployed, but this comes with major downsides and should only be used if it's not possible to deploy Dynatrace Operator.": "Принимать трассировки Istio можно без развёртывания экземпляра Dynatrace Operator, однако это сопряжено со значительными недостатками и следует прибегать к этому варианту лишь в случае, если развёртывание Dynatrace Operator невозможно.",
    "Caveats when using standalone deployment:": "Предостережения при использовании автономного развёртывания:",
    "* No Kubernetes metadata will be available for traces. This means traces will not be automatically correlated with Kubernetes workloads or services in Dynatrace.": "* Метаданные Kubernetes будут недоступны для трассировок. Это означает, что трассировки не будут автоматически сопоставляться с рабочими нагрузками или сервисами Kubernetes в Dynatrace.",
    "* Potentially unreliable delivery of traces. The current implementation of the OTLP HTTP exporter in Envoy doesn't provide any means of retry or error handling in case of connectivity or other issues when sending traces to Dynatrace, which can lead to loss of traces.": "* Потенциально ненадёжная доставка трассировок. Текущая реализация экспортера OTLP HTTP в Envoy не предусматривает механизмов повторных попыток или обработки ошибок в случае проблем с подключением или иных проблем при отправке трассировок в Dynatrace, что может приводить к потере трассировок.",
    "* The required `ServiceEntry` is not compatible with the `enableIstio` option of Dynatrace Operator.": "* Требуемый `ServiceEntry` несовместим с параметром `enableIstio` Dynatrace Operator.",
    "### Other deployment considerations": "### Прочие соображения по развёртыванию",
    "Istio ambient mode": "Istio в режиме ambient",
    "#### Istio ambient mode support": "#### Поддержка Istio в режиме ambient",
    "Istio in ambient mode doesn't rely on Envoy proxies to route traffic, so tracing Istio traffic using the OpenTelemetry integration is not possible. If waypoint proxies are used, those would still emit traces, but the metadata would be misleading or wrong. Currently, there is no solution for end-to-end tracing in Istio ambient mode.": "Istio в режиме ambient не использует прокси Envoy для маршрутизации трафика, поэтому трассировка трафика Istio с помощью интеграции OpenTelemetry невозможна. При использовании waypoint-прокси они по-прежнему будут генерировать трассировки, однако метаданные могут быть некорректными или вводящими в заблуждение. В настоящее время решения для сквозной трассировки в режиме ambient Istio не существует.",
    # Steps
    "## Steps": "## Шаги",
    "### 1. Requirements": "### 1. Требования",
    "Check the following requirements before starting to deploy tracing for Istio.": "Перед началом развёртывания трассировки для Istio проверьте следующие требования.",
    # L77/L90/L116/L210: "Dynatrace Operator" appears as tab-header text multiple times
    "Dynatrace Operator": "Dynatrace Operator",
    # L79/L92/L118/L212: "Standalone" tab-header text
    "Standalone": "Автономный режим",
    # L81 — stripped key starts with "1."
    '1. Dynatrace Operator is [deployed](/managed/ingest-from/setup-on-k8s/deployment "%s").'
    % TT_DEPL: '1. Dynatrace Operator [развёрнут](/managed/ingest-from/setup-on-k8s/deployment "%s").'
    % RU_DEPL,
    # L83 — stripped key starts with "* For optimal" (no leading spaces)
    '* For optimal configuration, follow the guide for [deployment alongside Istio](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "%s").'
    % TT_ISTIO: '* Для оптимальной конфигурации следуйте руководству по [развёртыванию совместно с Istio](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "%s").'
    % RU_ISTIO,
    # L84
    '2. [Telemetry ingest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "%s") endpoints are enabled.'
    % TT_TI: '2. [Эндпоинты приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "%s") включены.'
    % RU_TI,
    "Either Dynatrace Operator is not deployed, or `enableIstio` is set to `false` in the DynaKube.": "Dynatrace Operator либо не развёрнут, либо в DynaKube для параметра `enableIstio` установлено значение `false`.",
    "### 2. Get configuration entries": "### 2. Получение конфигурационных записей",
    "1. In Dynatrace Hub, search for `Istio`.": "1. В Dynatrace Hub выполните поиск по запросу `Istio`.",
    "2. Filter by the category **Technology**.": "2. Отфильтруйте по категории **Technology**.",
    "3. Select the Hub entry **Istio Service Mesh**.": "3. Выберите запись Hub **Istio Service Mesh**.",
    "4. Select **Set up**.": "4. Выберите **Set up**.",
    "5. Use the provided and pre-configured snippets to deploy the following items in the next steps:": "5. Используйте предоставленные и предварительно настроенные сниппеты для развёртывания следующих элементов на следующих шагах:",
    # L100/L110: stripped key has no leading spaces
    "* Mesh configuration": "* Конфигурация сетки",
    "* Telemetry API": "* Telemetry API",
    "5. Configure the API token.": "5. Настройте API-токен.",
    "6. Use the provided and pre-configured snippets to deploy the following items in the next steps:": "6. Используйте предоставленные и предварительно настроенные сниппеты для развёртывания следующих элементов на следующих шагах:",
    # L111: stripped key has no leading spaces
    "* Service entry": "* Запись сервиса",
    "### 3. Apply the mesh configuration to your Istio installation": "### 3. Применение конфигурации сетки к установке Istio",
    "To use the telemetry ingest endpoints provided by the Dynatrace OTel Collector, we need to change the snippet obtained in step 2 by removing the API token header and changing the target service.": "Для использования эндпоинтов приёма телеметрии, предоставляемых Dynatrace OTel Collector, необходимо изменить сниппет, полученный на шаге 2: удалить заголовок API-токена и изменить целевой сервис.",
    "The resulting configuration should look like this, assuming the default ingest service name:": "Результирующая конфигурация должна выглядеть следующим образом при использовании имени сервиса приёма по умолчанию:",
    "Save the file as `meshconfig.yaml` and apply the configuration using the following command.": "Сохраните файл как `meshconfig.yaml` и примените конфигурацию с помощью следующей команды.",
    "Save the mesh configuration snippet you obtained in step 2 under `meshconfig.yaml` and configure Istio with the following command:": "Сохраните сниппет конфигурации сетки, полученный на шаге 2, в файле `meshconfig.yaml` и настройте Istio следующей командой:",
    "Existing Mesh configuration": "Существующая конфигурация сетки",
    "If you already use your own, custom Mesh configuration, you need to merge its content with the provided snippet. Otherwise, you can use the snippet as-is.": "Если вы уже используете собственную пользовательскую конфигурацию сетки, необходимо объединить её содержимое с предоставленным сниппетом. В противном случае сниппет можно использовать как есть.",
    "### 4. Deploy the service entry": "### 4. Развёртывание записи сервиса",
    "This step is only required for standalone deployment.": "Этот шаг требуется только для автономного развёртывания.",
    "No action required when using Dynatrace Operator.": "При использовании Dynatrace Operator никаких действий не требуется.",
    # L217 — BOM stripped by norm(); normed key has no BOM
    "Next, you need to deploy the [Istio service entry](https://istio.io/latest/docs/reference/config/networking/service-entry/) manifest you obtained in step 1 using `kubectl`. Save it to `dt-serviceentry.yaml` and run the following command:": "Затем необходимо развернуть манифест [записи сервиса Istio](https://istio.io/latest/docs/reference/config/networking/service-entry/), полученный на шаге 1, с помощью `kubectl`. Сохраните его в файл `dt-serviceentry.yaml` и выполните следующую команду:",
    "### 5. Enable tracing provider": "### 5. Включение провайдера трассировки",
    "As last configuration step, use the Istio telemetry API to enable the tracing provider.": "На последнем шаге конфигурации используйте Istio telemetry API для включения провайдера трассировки.",
    "Save the telemetry API manifest you obtained in step 2 to `dt-telemetry.yaml` and use `kubectl` to apply the configuration to the desired namespace.": "Сохраните манифест Telemetry API, полученный на шаге 2, в файл `dt-telemetry.yaml` и примените конфигурацию к нужному пространству имён с помощью `kubectl`.",
    "Multiple telemetry resources": "Несколько ресурсов телеметрии",
    "Do not deploy more than one telemetry resource within a given namespace, as doing so may lead to configuration conflicts and incomplete tracing information.": "Не развёртывайте более одного ресурса телеметрии в пределах одного пространства имён, так как это может привести к конфликтам конфигурации и неполной информации о трассировке.",
    "If you require different telemetry resources, deploy them to different namespaces or using different selectors.": "Если требуется несколько ресурсов телеметрии, разверните их в разных пространствах имён или с использованием разных селекторов.",
    "Pod restart": "Перезапуск подов",
    "Make sure to restart all applicable Kubernetes pods, to let the changes to the mesh configuration take effect.": "Убедитесь, что все применимые поды Kubernetes перезапущены, чтобы изменения конфигурации сетки вступили в силу.",
    "### 6. Verify the setup": "### 6. Проверка настройки",
    "Once the setup is complete and you have ingested your first data, you can verify if the traces show up in Dynatrace.": "После завершения настройки и приёма первых данных можно проверить, отображаются ли трассировки в Dynatrace.",
    # L247: image line — alt text kept EN per glossary rule
    "![trace](https://dt-cdn.net/images/istio-otel-tracing-2513-5da62a325b.png)": "![trace](https://dt-cdn.net/images/istio-otel-tracing-2513-5da62a325b.png)",
    # L249: bare "trace" caption below image
    "trace": "trace",
    **S,
}

# No EN-kept lines without Russian in this file
PASS = set()

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
