# -*- coding: utf-8 -*-
"""Builder for zos-opentelemetry.md (L4-IF.71 canon).

EN source: docs/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry.md
RU target: docs/managed-ru/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry.md

Mojibake notes (scraping artifact in EN source):
  U+00EF U+00BB U+00BF (BOM lookalike) = ï»¿  — appears after some link texts
  U+00E2 U+0080 U+0099 RIGHT '          = â\x80\x99  in "you've", "it's", "isn't"
  U+00E2 U+0080 U+0099 RIGHT '          = â\x80\x99  in "applicationâs" (missing space/apostrophe)
Keys are written in clean EN (the engine's _demoji() handles mojibake matching).
"""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring"
FN = "zos-opentelemetry.md"

# ---------------------------------------------------------------------------
# TRANS: EN key (clean, no leading/trailing whitespace) -> RU value
# Rules:
#   - code-fences, blank lines, ---, source:, scraped: -> passthrough (engine)
#   - title: -> translate
#   - EN-lock: OneAgent, z/OS, z/OS Java, OTLP, OpenTelemetry component names
#     (exporter/receiver/processor/tracer/meter), SpanKind constants, dtconfig.json,
#     JVM args, class/method names, image alt-text stays EN
#   - OTel canon (from corpus): trace -> трассировка, span -> спан,
#     distributed trace -> распределённая трассировка,
#     instrumentation -> инструментирование,
#     context propagation -> распространение контекста,
#     endpoint -> эндпоинт
#   - No em-dash; no "вы можете/должны/хотите" calques
# ---------------------------------------------------------------------------

TRANS = {
    # --- frontmatter ---
    "title: Extend traces using OpenTelemetry": "title: Расширение трассировок с помощью OpenTelemetry",
    # --- h1 (appears twice in source) ---
    "# Extend traces using OpenTelemetry": "# Расширение трассировок с помощью OpenTelemetry",
    # --- metadata ---
    "* 7-min read": "* Чтение: 7 мин",
    "* Updated on Sep 23, 2022": "* Обновлено 23 сентября 2022 г.",
    # --- intro prose ---
    # mojibake: "OpenTelemetryï»¿" -> engine demojis to "OpenTelemetry"
    "[OpenTelemetry](https://dt-url.net/y903u4j) is a collection of tools, APIs, and SDKs that enable you to use telemetry data (distributed traces, metrics, and logs) to get insights into your application's performance and behavior.": "[OpenTelemetry](https://dt-url.net/y903u4j): набор инструментов, API и SDK, позволяющих использовать данные телеметрии (распределённые трассировки, метрики и логи) для анализа производительности и поведения приложения.",
    "OpenTelemetry with the z/OS Java code module enables you to enrich or extend distributed traces.": "OpenTelemetry совместно с кодовым модулем z/OS Java позволяет обогащать или расширять распределённые трассировки.",
    "* Enrich distributed traces with project-specific additions (for example, you can add business-relevant data to your traces or capture developer-specific diagnostics).": "* Обогащать распределённые трассировки данными, специфичными для проекта (например, добавлять бизнес-релевантные данные в трассировки или захватывать диагностику для разработчиков).",
    "* Extend distributed traces (for example, you can capture a Java Transport that is not supported out of the box by Dynatrace or fill observability gaps between applications to achieve transactional insights).": "* Расширять распределённые трассировки (например, захватывать Java Transport, не поддерживаемый Dynatrace из коробки, или устранять пробелы в наблюдаемости между приложениями для получения транзакционной аналитики).",
    "OpenTelemetry metrics and logs are currently not supported by the z/OS Java code module.": "Метрики и логи OpenTelemetry в настоящее время не поддерживаются кодовым модулем z/OS Java.",
    # callout header (no fence, plain text line)
    "Licensing": "Лицензирование",
    "* OpenTelemetry distributed traces captured by the z/OS Java code module are included in the mainframe license.": "* Распределённые трассировки OpenTelemetry, захваченные кодовым модулем z/OS Java, включены в лицензию мейнфрейма.",
    # --- ## OpenTelemetry interoperability ---
    "## OpenTelemetry interoperability": "## Совместимость с OpenTelemetry",
    "OpenTelemetry version 1.0+": "OpenTelemetry версии 1.0+",
    "Enabling OpenTelemetry interoperability connects the z/OS Java code module to the OpenTelemetry API. When enabled, the code module redirects certain OpenTelemetry API usage (for example, `GlobalOpenTelemetry`) to the internal Dynatrace OpenTelemetry SDK.": "При включении совместимости с OpenTelemetry кодовый модуль z/OS Java подключается к OpenTelemetry API. После включения модуль перенаправляет определённые обращения к OpenTelemetry API (например, `GlobalOpenTelemetry`) во внутренний Dynatrace OpenTelemetry SDK.",
    # mojibake: "OpenTelemetry Spansï»¿" -> engine demojis to "OpenTelemetry Spans"
    'The z/OS Java code module forwards the captured [OpenTelemetry Spans](https://opentelemetry.io/docs/concepts/signals/traces/#spans-in-opentelemetry), via the [zDC subsystem](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.") and [zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring."), to your Dynatrace environment.': 'Кодовый модуль z/OS Java передаёт захваченные [спаны OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/traces/#spans-in-opentelemetry) через [подсистему zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Настройка мониторинга Java на z/OS с помощью модуля Java.") и [модуль zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.") в окружение Dynatrace.',
    "![z/OS Java OpenTelemetry](https://dt-cdn.net/images/zos-java-otel-1369-e7b35738b0.png)": "![z/OS Java OpenTelemetry](https://dt-cdn.net/images/zos-java-otel-1369-e7b35738b0.png)",
    "z/OS Java OpenTelemetry": "z/OS Java OpenTelemetry",
    "Recommendation: avoid using the OpenTelemetry SDK in your applications together with the Dynatrace OpenTelemetry interoperability because it could result in conflicts.": "Рекомендация: не используйте OpenTelemetry SDK в приложениях совместно с механизмом совместимости Dynatrace OpenTelemetry, поскольку это может привести к конфликтам.",
    # --- ### Enable OpenTelemetry interoperability ---
    "### Enable OpenTelemetry interoperability": "### Включение совместимости с OpenTelemetry",
    "OpenTelemetry interoperability is disabled by default. To enable it, add the `OpenTelemetry: EnableIntegration` attribute to your `dtconfig.json` file as shown in the following example.": "Совместимость с OpenTelemetry отключена по умолчанию. Чтобы включить её, добавьте атрибут `OpenTelemetry: EnableIntegration` в файл `dtconfig.json`, как показано в следующем примере.",
    # mojibake: "you've" -> engine demojis "youâ\x80\x99ve" -> "you've"
    'Typically, you\'ve created the `dtconfig.json` file during the [z/OS Java code module installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Set up Java monitoring on z/OS using the Java module.") and have set the attributes `Tenant`, `ClusterID`, and `zdcName` to your environment.': 'Как правило, файл `dtconfig.json` создаётся при [установке кодового модуля z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Настройка мониторинга Java на z/OS с помощью модуля Java.") с указанием атрибутов `Tenant`, `ClusterID` и `zdcName` для вашего окружения.',
    "Alternatively, you can add the `open-telemetry-enable-integration` option to the JVM argument of the z/OS Java code module:": "Альтернативно можно добавить параметр `open-telemetry-enable-integration` в аргумент JVM кодового модуля z/OS Java:",
    # --- ## OpenTelemetry instrumentation samples ---
    "## OpenTelemetry instrumentation samples": "## Примеры инструментирования OpenTelemetry",
    # mojibake: "applicationâ\x80\x99s" -(_demoji)-> "application’s"; "ï»¿" -(_demoji)-> U+FEFF -(norm)-> removed
    # Key uses ’ escape so formatter cannot replace it with ASCII apostrophe.
    "To support various use cases, OpenTelemetry enables you to add vendor-neutral custom instrumentation to your applications. Instrumenting applications with OpenTelemetry requires programming knowledge and access to the application’s code. To learn how to instrument your application, refer to [OpenTelemetry documentation](https://dt-url.net/7603uf3) and [OpenTelemetry Java documentation](https://dt-url.net/n823ur4).": "Для поддержки различных сценариев использования OpenTelemetry позволяет добавлять независимое от поставщика пользовательское инструментирование в приложения. Инструментирование приложений с помощью OpenTelemetry требует знания программирования и доступа к коду приложения. Инструкции по инструментированию приложения см. в [документации OpenTelemetry](https://dt-url.net/7603uf3) и [документации OpenTelemetry Java](https://dt-url.net/n823ur4).",
    # mojibake: "OpenTelemetry Javaï»¿" -> engine demojis to "OpenTelemetry Java"
    "See the examples below for using [OpenTelemetry Java](https://dt-url.net/yo43um9).": "Ниже приведены примеры использования [OpenTelemetry Java](https://dt-url.net/yo43um9).",
    # callout header
    "Enrich traces with project-specific additions": "Обогащение трассировок данными, специфичными для проекта",
    "This example shows how you can capture an additional operation in a Java application running on a WebSphere Application Server monitored by Dynatrace.": "Этот пример показывает, как захватить дополнительную операцию в Java-приложении, работающем на WebSphere Application Server под мониторингом Dynatrace.",
    "1. Define a `Tracer`.": "1. Определите `Tracer`.",
    "2. Use the `Tracer` to capture an operation including some attributes.": "2. Используйте `Tracer` для захвата операции вместе с атрибутами.",
    "The `MenuDao.newOrder` operation is displayed as a span on the **Code level** tab in the Dynatrace web UI with the captured span attributes (`customer`, `newOrderId`) and measured execution time.": "Операция `MenuDao.newOrder` отображается как спан на вкладке **Code level** в веб-интерфейсе Dynatrace с захваченными атрибутами спана (`customer`, `newOrderId`) и измеренным временем выполнения.",
    "![z/OS OpenTelemetry code-level](https://dt-cdn.net/images/zos-opentelemetry-1-1926-e67ad2add3.png)": "![z/OS OpenTelemetry: уровень кода](https://dt-cdn.net/images/zos-opentelemetry-1-1926-e67ad2add3.png)",
    "z/OS OpenTelemetry code-level": "z/OS OpenTelemetry: уровень кода",
    # callout header
    "Extend end-to-end traces": "Расширение сквозных трассировок",
    "This example shows how you can trace an audit service running on a WebSphere Application Server (monitored by Dynatrace) that uses a Java transport that is not supported out of the box. We use Java serialization (object output streams) as an example for such an unsupported Java transport.": "Этот пример показывает, как трассировать сервис аудита на WebSphere Application Server (под мониторингом Dynatrace), использующий Java-транспорт, не поддерживаемый из коробки. В качестве примера такого неподдерживаемого транспорта используется Java serialization (потоки вывода объектов).",
    # mojibake: "OpenTelemetry Context Propagation documentationï»¿" -> engine demojis
    "To learn more about context propagation, refer to the official [OpenTelemetry Context Propagation documentation](https://dt-url.net/j503uhz).": "Подробнее о распространении контекста см. в официальной [документации OpenTelemetry Context Propagation](https://dt-url.net/j503uhz).",
    "**Service A** writes an audit entry to the `ObjectOutputStream`:": "**Service A** записывает запись аудита в `ObjectOutputStream`:",
    "**Service B** reads an audit entry from the `ObjectInputStream`:": "**Service B** считывает запись аудита из `ObjectInputStream`:",
    "Dynatrace displays the full end-to-end trace as a distributed trace that contains the `auditEntry` as a service method which includes the captured attributes and measured execution time. The `auditEntry` service method is the result of the traced `receivedAuditEntry` method with its new span. The fact that it is displayed as a child of the `/orderReceived` service method is the result of the `inject` and `extract` calls of the `TextMapPropagator`.": "Dynatrace отображает полную сквозную трассировку как распределённую трассировку, содержащую `auditEntry` в качестве метода сервиса с захваченными атрибутами и измеренным временем выполнения. Метод сервиса `auditEntry` является результатом трассировки метода `receivedAuditEntry` с его новым спаном. Отображение в качестве дочернего элемента метода сервиса `/orderReceived` является результатом вызовов `inject` и `extract` компонента `TextMapPropagator`.",
    "![z/OS OpenTelemetry service](https://dt-cdn.net/images/zos-opentelemetry-2-1926-9f66be4562.png)": "![z/OS OpenTelemetry: сервис](https://dt-cdn.net/images/zos-opentelemetry-2-1926-9f66be4562.png)",
    "z/OS OpenTelemetry service": "z/OS OpenTelemetry: сервис",
    # --- ## Suppress spans from specific instrumentations ---
    "## Suppress spans from specific instrumentations": "## Подавление спанов из определённых инструментирований",
    "You can suppress spans coming from a particular instrumentation scope/library. To do so, add the library name to the `OpenTelemetry: DisabledSensors` parameter in name via the `dtconfig.json` file. You can use an asterisk (`*`) to exclude all instrumentation scope/library names starting with the preceding string. You can't use asterisk at the beginning or in the middle of a library name.": "Можно подавлять спаны из определённой области инструментирования/библиотеки. Для этого добавьте имя библиотеки в параметр `OpenTelemetry: DisabledSensors` файла `dtconfig.json`. Допускается использование звёздочки (`*`) для исключения всех имён областей инструментирования/библиотек, начинающихся с указанной строки. Использование звёздочки в начале или середине имени библиотеки не допускается.",
    "Alternatively, you can add the `open-telemetry-disabled-sensors` option to the JVM argument of the z/OS Java code module:": "Альтернативно можно добавить параметр `open-telemetry-disabled-sensors` в аргумент JVM кодового модуля z/OS Java:",
    "If you specify exclusions in the command line, the exclusions in the `dtconfig.json` file ignored.": "Если исключения указаны в командной строке, исключения в файле `dtconfig.json` игнорируются.",
    "Use colon `:` as the separator for instrumentation scope/library names in the command line.": "В командной строке используйте двоеточие `:` в качестве разделителя имён областей инструментирования/библиотек.",
    "The examples above suppress spans from the `com.example.MyLib` instrumentation scope/library and spans from all libraries starting with the name `opentelemetry.urllib3`.": "Приведённые примеры подавляют спаны из области инструментирования/библиотеки `com.example.MyLib`, а также спаны из всех библиотек, имя которых начинается с `opentelemetry.urllib3`.",
    # --- ## Rules for spans that Dynatrace will report ---
    "## Rules for spans that Dynatrace will report": "## Правила отбора спанов для отчётности Dynatrace",
    "Depending on the `SpanKind`, Dynatrace will suppress some OpenTelemetry spans:": "В зависимости от `SpanKind`, Dynatrace подавляет часть спанов OpenTelemetry:",
    "* A span needs to either be of kind `SpanKind.SERVER` or `SpanKind.CONSUMER` or it needs to have another span (`SpanContext`) as a non-remote parent. Usually, this is handled by the Dynatrace Servlet sensor, which creates a `SERVER` span and sets it as the current, active span.": "* Спан должен иметь тип `SpanKind.SERVER` или `SpanKind.CONSUMER`, либо иметь другой спан (`SpanContext`) в качестве нелокального (non-remote) родителя. Как правило, это обеспечивает Dynatrace Servlet sensor, который создаёт спан типа `SERVER` и устанавливает его как текущий активный спан.",
    "* Child spans of spans of kind `SpanKind.CLIENT` or `SpanKind.PRODUCER` will be suppressed. For example, after Dynatrace creates a span of kind `SpanKind.CLIENT` for a synchronous outgoing HTTP call, all spans created in the thread will be suppressed until the HTTP call, and thus the HTTP Span, is finished. You can of course create new spans in the called service which will be linked correctly.": "* Дочерние спаны спанов типа `SpanKind.CLIENT` или `SpanKind.PRODUCER` будут подавляться. Например, после того как Dynatrace создаёт спан типа `SpanKind.CLIENT` для синхронного исходящего HTTP-вызова, все спаны, создаваемые в потоке, подавляются до завершения HTTP-вызова и соответствующего HTTP Span. В вызываемом сервисе можно создавать новые спаны, которые будут связаны корректно.",
    "Suppressed spans will not be visible in distributed traces.": "Подавленные спаны не будут отображаться в распределённых трассировках.",
    # --- ## Define a request attribute for span attributes ---
    "## Define a request attribute for span attributes": "## Определение атрибута запроса для атрибутов спана",
    'You can define a [request attribute](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") for any captured span attribute. To do so': 'Для любого захваченного атрибута спана можно определить [атрибут запроса](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и научитесь использовать их на всех уровнях представлений анализа сервисов."). Для этого:',
    "1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.": "1. Перейдите в **Settings** > **Server-side service monitoring** > **Request attributes**.",
    "2. Select **Define a new request attribute** and enter the name and data type of your request attribute.": "2. Нажмите **Define a new request attribute** и укажите имя и тип данных атрибута запроса.",
    "3. Select **Add new data source** and select `Span attribute` as the **Request attribute source**.": "3. Нажмите **Add new data source** и выберите `Span attribute` в качестве **Request attribute source**.",
    "4. Enter your **Attribute key**.": "4. Введите **Attribute key**.",
    "5. Select **Save**.": "5. Нажмите **Save**.",
    'To learn more details about span attributes and how to capture them, see [Span settings](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.").': 'Подробнее об атрибутах спана и их захвате см. в разделе [Настройки span](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings "Узнайте, как настраивать параметры span для OpenTelemetry и OpenTracing.").',
    "![Use Span attribute as a request attribute](https://dt-cdn.net/images/screenshot-2022-09-30-at-09-24-35-1883-e2f2b63693.png)": "![Использование атрибута спана как атрибута запроса](https://dt-cdn.net/images/screenshot-2022-09-30-at-09-24-35-1883-e2f2b63693.png)",
    "Use Span attribute as a request attribute": "Использование атрибута спана как атрибута запроса",
    'You can find the **Attribute key** of your spans on the [Distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") page in the **Code level** tab under **Span attributes**.': '**Attribute key** спанов можно найти на странице [Distributed traces](/managed/observe/application-observability/distributed-traces "Получите наблюдаемость высокораспределённых cloud-native архитектур для эффективной трассировки и анализа транзакций в режиме реального времени.") на вкладке **Code level** в разделе **Span attributes**.',
    "![Span attributes](https://dt-cdn.net/images/span-attributes-1916-1967c4e21e.png)": "![Атрибуты span](https://dt-cdn.net/images/span-attributes-1916-1967c4e21e.png)",
    "Span attributes": "Атрибуты span",
}

# Lines that must remain verbatim EN (none needed — all handled via TRANS or engine passthrough)
PASS = set()

if __name__ == "__main__":
    build_one(REL, FN, TRANS, PASS)
    qa_one(REL, FN)
