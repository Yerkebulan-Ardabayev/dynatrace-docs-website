# -*- coding: utf-8 -*-
"""L4-IF.70 builder: ingest-from/opentelemetry/collector.md (hub page)."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry"
FNAME = "collector.md"

TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_CONF = "How to configure the OpenTelemetry Collector."
RU_CONF = "Как настроить OpenTelemetry Collector."
TT_UCASES = "Configure your OpenTelemetry Collector instance for different use cases."
RU_UCASES = (
    "Настройте экземпляр OpenTelemetry Collector для различных сценариев использования."
)
TT_DEPLOY = "How to deploy the Dynatrace OpenTelemetry Collector."
RU_DEPLOY = "Как развернуть Dynatrace OpenTelemetry Collector."
TT_GRPC = (
    "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP."
)
RU_GRPC = (
    "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP."
)
TT_GH_REPO = "https://github.com/Dynatrace/dynatrace-otel-collector/"
TT_POLICY = "https://support.dynatrace.com/"

TRANS = {
    # --- frontmatter ---
    "title: OTel Collector for ingesting telemetry into Dynatrace": "title: OTel Collector для приёма телеметрии в Dynatrace",
    # --- h1 (repeated twice in source) ---
    "# OTel Collector for ingesting telemetry into Dynatrace": "# OTel Collector для приёма телеметрии в Dynatrace",
    # --- metadata ---
    "* Overview": "* Обзор",
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Apr 28, 2026": "* Обновлено 28 апреля 2026 г.",
    # --- intro paragraph ---
    'The OTel Collector (or just "Collector") is a network service application that you can use to batch and transform telemetry data. It acts as a proxy and can receive OTLP requests as well as data from other sources, transform these requests according to defined rules, and forward them to the backend.': 'OTel Collector (или просто "Collector"), сетевое сервисное приложение, позволяет группировать и преобразовывать данные телеметрии. Оно работает как прокси: принимает запросы OTLP, а также данные из других источников, преобразует их по заданным правилам и пересылает в бэкенд.',
    # --- diagram ---
    "The following diagram shows different components that the Collector can use to receive, process, and export telemetry data to Dynatrace.": "На следующей схеме показаны различные компоненты, которые Collector может использовать для приёма, обработки и экспорта данных телеметрии в Dynatrace.",
    "![The OTel Collector can receive, process, and export telemetry data to Dynatrace](https://cdn.bfldr.com/B686QPH3/as/5b86f3jgqb7frz6rtb85hjc/OpenTelemetry_-_Dynatrace_Collector_-_Light_Mode?auto=webp&format=png&position=1)": "![The OTel Collector can receive, process, and export telemetry data to Dynatrace](https://cdn.bfldr.com/B686QPH3/as/5b86f3jgqb7frz6rtb85hjc/OpenTelemetry_-_Dynatrace_Collector_-_Light_Mode?auto=webp&format=png&position=1)",
    "OTel Collector pipeline": "Конвейер OTel Collector",
    # --- Advantages section ---
    "## Advantages of using the Collector": "## Преимущества использования Collector",
    "In general, using the Collector alongside your service can be an advantage, since it allows your service to offload data quickly and takes care of additional handling such as retries, batching, encryption, or sensitive data filtering. It centralizes common processing tasks instead of duplicating them in each application.": "В целом использование Collector совместно с сервисом может быть выгодно, поскольку позволяет сервису быстро выгружать данные, а Collector берёт на себя дополнительную обработку (повторные попытки, группирование, шифрование, фильтрацию конфиденциальных данных). Общие задачи обработки централизуются, а не дублируются в каждом приложении.",
    "You should use the Collector if:": "Collector следует использовать, если:",
    "* You need to collect data from different data sources in different formats and you need an easy way to make them all deliver their data to a backend that would otherwise be incompatible.": "* Нужно собирать данные из различных источников в разных форматах и требуется простой способ доставить их все в бэкенд, который иначе был бы несовместим.",
    "* You need to have common processing of attributes on your telemetry data.": "* Необходима общая обработка атрибутов данных телеметрии.",
    "The Collector is a relatively lightweight component, so teams can deploy their own to avoid sharing the same configuration.": "Collector, относительно лёгкий компонент, позволяет командам развёртывать собственные экземпляры, не используя одну общую конфигурацию.",
    'The Collector is configured in a single YAML file. This eliminates the need to browse through multiple files and reduces maintenance. You can find more information on the configuration at [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "%s").'
    % TT_CONF: 'Collector настраивается в одном YAML-файле. Это устраняет необходимость просматривать несколько файлов и упрощает обслуживание. Дополнительные сведения о настройке см. в разделе [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "%s").'
    % RU_CONF,
    # --- Distributions section ---
    "## Distributions": "## Дистрибутивы",
    "The Collector comes in different distribution flavors and with different setup and deployment options.": "Collector поставляется в нескольких вариантах дистрибутива с различными параметрами установки и развёртывания.",
    # --- table header row ---
    "| Type | When should I use it? |": "| Тип | Когда использовать? |",
    # table separator -> PASS
    # --- table data rows ---
    "| Dynatrace OTel Collector Recommended | The preferred choice for most use cases. It ships with a set of verified and stable Collector components, typically used with Dynatrace setups. |": "| Dynatrace OTel Collector Recommended | Предпочтительный выбор для большинства сценариев использования. Поставляется с набором проверенных и стабильных компонентов Collector, типично применяемых в конфигурациях Dynatrace. |",
    '| Core | When you primarily want to convert between OTLP protocols (such as converting between HTTP and gRPC, see [Transform OTLP gRPC to HTTP with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "%s")), enforce memory usage constraints, or apply request batching. |'
    % TT_GRPC: '| Core | Когда нужно в первую очередь выполнять преобразование между протоколами OTLP (например, конвертацию между HTTP и gRPC, см. [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "%s")), применять ограничения использования памяти или группировать запросы. |'
    % RU_GRPC,
    "| Contrib | Ideal for test setups, as it contains all third-party components and doesn't require a custom build. It's generally not recommended for production systems, as it typically consumes more resources and may be less stable than an optimized Builder instance. |": "| Contrib | Идеально подходит для тестовых конфигураций, поскольку содержит все сторонние компоненты и не требует пользовательской сборки. Как правило, не рекомендуется для производственных систем, так как обычно потребляет больше ресурсов и может быть менее стабильным, чем оптимизированный экземпляр Builder. |",
    "| Collector Builder | When you need to fully customize the Collector instance and only run the components required for your use case. |": "| Collector Builder | Когда нужно полностью настроить экземпляр Collector и запускать только компоненты, необходимые для вашего сценария использования. |",
    # --- Dynatrace OTel Collector subsection ---
    "### Dynatrace OTel Collector": "### Dynatrace OTel Collector",
    "The Dynatrace distribution of the OpenTelemetry (OTel) Collector is a customized Collector build provided by Dynatrace. It is tailored for typical use cases in a Dynatrace context, and ships with an optimized and verified set of Collector components.": "Дистрибутив Dynatrace для OpenTelemetry (OTel) Collector представляет собой специализированную сборку Collector, предоставляемую Dynatrace. Он адаптирован для типичных сценариев использования в контексте Dynatrace и поставляется с оптимизированным и проверенным набором компонентов Collector.",
    "#### Dynatrace OTel Collector advantages": "#### Преимущества Dynatrace OTel Collector",
    "The Dynatrace OTel Collector offers the following advantages compared to other Collector distributions.": "Dynatrace OTel Collector предлагает следующие преимущества по сравнению с другими дистрибутивами Collector.",
    "* Covered by Dynatrace support, see [Dynatrace OTel Collector support](#support).": "* Поддерживается командой Dynatrace, см. [Поддержка Dynatrace OTel Collector](#support).",
    "* Collector components verified by Dynatrace.": "* Компоненты Collector проверены Dynatrace.",
    "* Security patches independent of OTel Collector releases.": "* Патчи безопасности выпускаются независимо от релизов OTel Collector.",
    "The Dynatrace OTel Collector preserves the standard configuration model and component semantics.": "Dynatrace OTel Collector сохраняет стандартную модель конфигурации и семантику компонентов.",
    "By avoiding proprietary abstractions or hidden defaults, it enables both humans and AI agents to reliably reuse standard OpenTelemetry references and examples with fewer errors.": "Отказавшись от проприетарных абстракций и скрытых значений по умолчанию, он позволяет как людям, так и ИИ-агентам надёжно повторно использовать стандартные справочные материалы и примеры OpenTelemetry с меньшим числом ошибок.",
    "#### Dynatrace OTel Collector support": "#### Поддержка Dynatrace OTel Collector",
    "The x86 64 and ARM64 builds of the Dynatrace OTel Collector distribution are supported by the Dynatrace Support team, in accordance with the [Dynatrace support policy﻿](%s)."
    % TT_POLICY: "Сборки x86 64 и ARM64 дистрибутива Dynatrace OTel Collector поддерживаются командой Dynatrace Support в соответствии с [политикой поддержки Dynatrace﻿](%s)."
    % TT_POLICY,
    "For full support coverage, contact Dynatrace through the official support channels.": "Для получения полной поддержки обращайтесь в Dynatrace через официальные каналы поддержки.",
    "Issues reported via GitHub are handled on a best‑effort basis; support contracts and SLAs don't apply.": "Проблемы, сообщённые через GitHub, обрабатываются по принципу «наилучших усилий»; контракты поддержки и SLA не применяются.",
    "Each minor version is supported for three months.": "Каждая минорная версия поддерживается в течение трёх месяцев.",
    "Fixes are provided either as a patch release for the latest supported minor version or as part of a subsequent minor version release.": "Исправления предоставляются либо в виде патч-релиза для последней поддерживаемой минорной версии, либо в составе последующего минорного релиза.",
    "#### Dynatrace OTel Collector components": "#### Компоненты Dynatrace OTel Collector",
    "For the full list of provided components, see [Components﻿](https://github.com/Dynatrace/dynatrace-otel-collector#components).": "Полный список предоставляемых компонентов см. на странице [Components](https://github.com/Dynatrace/dynatrace-otel-collector#components).",
    "#### Dynatrace OTel Collector use cases": "#### Сценарии использования Dynatrace OTel Collector",
    'For concrete use-case and configuration examples for the individual components, see [OTel Collector use cases](/managed/ingest-from/opentelemetry/collector/use-cases "%s").'
    % TT_UCASES: 'Конкретные примеры сценариев использования и конфигурации для отдельных компонентов см. в разделе [Сценарии использования OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases "%s").'
    % RU_UCASES,
    "#### Deploy the Dynatrace OTel Collector": "#### Развёртывание Dynatrace OTel Collector",
    'To deploy the Dynatrace OTel Collector, follow the steps as described in [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "%s").'
    % TT_DEPLOY: 'Чтобы развернуть Dynatrace OTel Collector, следуйте шагам, описанным в разделе [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "%s").'
    % RU_DEPLOY,
    "The Dynatrace OTel Collector ships with specific components, which are described in the [Dynatrace OTel Collector's GitHub repo﻿](%s)."
    % TT_GH_REPO: "Dynatrace OTel Collector поставляется со специальными компонентами, описанными в [репозитории GitHub Dynatrace OTel Collector](%s)."
    % TT_GH_REPO,
    # --- OpenTelemetry distributions subsection ---
    "### OpenTelemetry distributions": "### Дистрибутивы OpenTelemetry",
    "Dynatrace provides limited support for Core, Contrib, and Builder setups.": "Dynatrace обеспечивает ограниченную поддержку конфигураций Core, Contrib и Builder.",
    "This support covers only the components and their versions that are included in the Dynatrace OTel Collector.": "Эта поддержка распространяется только на компоненты и их версии, включённые в Dynatrace OTel Collector.",
    "For a fully supported Collector distribution, see [Dynatrace OTel Collector](#dt-collector-dist).": "Полностью поддерживаемый дистрибутив Collector см. в разделе [Dynatrace OTel Collector](#dt-collector-dist).",
    "#### Collector Core": "#### Collector Core",
    "The [Core distribution﻿](https://github.com/open-telemetry/opentelemetry-collector) contains the basic proxy service and a few fundamental service components.": "Дистрибутив [Core](https://github.com/open-telemetry/opentelemetry-collector) содержит базовый прокси-сервис и несколько фундаментальных сервисных компонентов.",
    "This includes:": "В их числе:",
    "* A receiver for OpenTelemetry protocol (OTLP) data over HTTP and gRPC.": "* receiver для данных протокола OpenTelemetry (OTLP) через HTTP и gRPC.",
    "* Processors for batching requests and ensuring memory usage constraints.": "* processor для группирования запросов и соблюдения ограничений использования памяти.",
    "* Exporters for console logging and OTLP over HTTP and gRPC.": "* exporter для вывода в консоль и OTLP через HTTP и gRPC.",
    "#### Collector Contrib": "#### Collector Contrib",
    "The [Contrib distribution﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib) builds on top of Core and enhances its functionality by shipping with a large number of additional receivers, processors, and exporters, contributed by third parties.": "Дистрибутив [Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) построен поверх Core и расширяет его функциональность за счёт большого числа дополнительных receiver, processor и exporter, предоставленных третьими сторонами.",
    "Given that the Contrib distribution is an all-in-one package and comes with all service components pre-compiled, it may use more system resources (storage and memory) than an optimized Collector build.": "Поскольку дистрибутив Contrib является комплексным пакетом и поставляется со всеми сервисными компонентами в предварительно скомпилированном виде, он может потреблять больше системных ресурсов (дисковое пространство и память), чем оптимизированная сборка Collector.",
    "Dynatrace recommends using the Contrib distribution only for testing purposes.": "Dynatrace рекомендует использовать дистрибутив Contrib только в целях тестирования.",
    "It shouldn't be used for production environments.": "Его не следует применять в производственных средах.",
    "#### Collector Builder": "#### Collector Builder",
    "In addition to the two distributions, OpenTelemetry also offers the [OpenTelemetry Collector Builder (OCB)﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/cmd/builder), a command line tool that allows you to build your own customized version of the Collector.": "Помимо двух дистрибутивов, OpenTelemetry предлагает [OpenTelemetry Collector Builder (OCB)](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/cmd/builder), инструмент командной строки для создания собственной настроенной версии Collector.",
    # --- Components section ---
    "## Components": "## Компоненты",
    # --- component kind headers -> PASS (kept EN per glossary) ---
    # "### Receiver" -> PASS
    # "### Processor Optional" -> PASS
    # "### Exporter" -> PASS
    # "### Services" -> PASS
    "A receiver is a component that allows data to come into the Collector. It can receive data from multiple sources. Many receivers come with default settings and don't need much configuration.": "receiver: компонент, позволяющий данным поступать в Collector. Он может принимать данные из нескольких источников. Многие receiver поставляются с настройками по умолчанию и не требуют значительной конфигурации.",
    "For a list of available receivers and their basic configuration, see the official [OpenTelemetry documentation on receivers﻿](https://opentelemetry.io/docs/collector/configuration/#receivers).": "Список доступных receiver и их базовую конфигурацию см. в официальной [документации OpenTelemetry по receiver](https://opentelemetry.io/docs/collector/configuration/#receivers).",
    "A processor is an optional component that transforms, filters, or enriches data before export.": "processor: необязательный компонент, который преобразует, фильтрует или обогащает данные перед экспортом.",
    "For a list of available processors and their basic configuration, see the official [OpenTelemetry documentation on processors﻿](https://opentelemetry.io/docs/collector/configuration/#processors). OpenTelemetry has a list of [recommended processors﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor#recommended-processors), but these are optional.": "Список доступных processor и их базовую конфигурацию см. в официальной [документации OpenTelemetry по processor](https://opentelemetry.io/docs/collector/configuration/#processors). В OpenTelemetry есть список [рекомендуемых processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor#recommended-processors), однако они необязательны.",
    "An exporter is a component that sends processed data to one or more backends. Exporters can support more than one data source.": "exporter: компонент, отправляющий обработанные данные в один или несколько бэкендов. exporter может поддерживать более одного источника данных.",
    "Because many exporters require additional configuration (for example, an endpoint), be sure to check the official [OpenTelemetry documentation on exporters﻿](https://opentelemetry.io/docs/collector/configuration/#exporters) for a list of available exporters and their configurations.": "Поскольку многие exporter требуют дополнительной настройки (например, эндпоинта), обязательно ознакомьтесь с официальной [документацией OpenTelemetry по exporter](https://opentelemetry.io/docs/collector/configuration/#exporters) для просмотра списка доступных exporter и их конфигураций.",
    "Services define pipelines that channel data through the Collector. They define which components work together to process OpenTelemetry data.": "Services определяют конвейеры, направляющие данные через Collector. Они задают, какие компоненты работают совместно для обработки данных OpenTelemetry.",
    **S,
}

PASS = {
    "| --- | --- |",
    "### Receiver",
    "### Processor Optional",
    "### Exporter",
    "### Services",
}


def _fixup_mojibake_keys():
    """Add TRANS entries whose keys contain raw mojibake bytes that norm() can't clean.

    norm() strips BOM-class chars and converts the 6-byte em-dash mojibake
    (c3 a2 c2 80 c2 94) to U+2014.  It does NOT touch the en-dash mojibake
    (c3 a2 c2 80 c2 91 read back as three Latin-1 chars U+00E2 U+0080 U+0091).
    We derive the exact normalized key by running norm() on the raw source line
    and map it to the RU translation here.
    """
    from _build_otel_uc_l4if68 import norm, read_lf

    en = read_lf(
        os.path.join(os.path.dirname(__file__), "..", "docs", "managed", REL, FNAME)
    )
    lines = en.split("\n")
    # Line 64: x86<en-dash-mojibake>64 ... [Dynatrace support policy<BOM>](url)
    k64 = norm(lines[63].strip())
    TRANS[k64] = (
        "Сборки x86-64 и ARM64 дистрибутива Dynatrace OTel Collector поддерживаются"
        " командой Dynatrace Support в соответствии с [политикой поддержки Dynatrace]"
        "(https://support.dynatrace.com/)."
    )
    # Line 67: ...best<en-dash-mojibake>effort...
    k67 = norm(lines[66].strip())
    TRANS[k67] = (
        "Проблемы, сообщённые через GitHub, обрабатываются по принципу"
        ' "наилучших усилий"; контракты поддержки и SLA не применяются.'
    )


if __name__ == "__main__":
    _fixup_mojibake_keys()
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
