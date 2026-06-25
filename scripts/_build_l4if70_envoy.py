# -*- coding: utf-8 -*-
"""L4-IF.70 builder: integrations/envoy.md (EN -> RU)."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/integrations"
FNAME = "envoy.md"

# TT_OTLP reused from _build_otel_uc_l4if68 via S (already has the right strings).
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."

TRANS = {
    # --- frontmatter ---
    "title: Configure OpenTelemetry tracing with Envoy": "title: Настройка трассировки OpenTelemetry с Envoy",
    # --- page headings ---
    "# Configure OpenTelemetry tracing with Envoy": "# Настройка трассировки OpenTelemetry с Envoy",
    # --- metadata bullets ---
    "* 4-min read": "* Чтение: 4 мин",
    "* Updated on Apr 07, 2026": "* Обновлено 07 апреля 2026 г.",
    # --- support statement block ---
    "Support statement": "Заявление о поддержке",
    "This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.": "Данная интеграция основана на коде с открытым исходным кодом, регулируемом соответствующими сообществами, и не подпадает под политику поддержки Dynatrace. Мы стремимся оказывать помощь, однако проблемы и запросы функций следует сообщать непосредственно в соответствующий проект. Dynatrace не может гарантировать исправления или функции ввиду независимой природы OSS-проектов.",
    "Always use the most recent release version to ensure you have the latest patches and fixes deployed.": "Всегда используйте самую последнюю версию релиза, чтобы иметь актуальные патчи и исправления.",
    # --- intro sentence ---
    "This page describes how to configure your Envoy version 1.30+ instance to export traces to Dynatrace.": "На этой странице описано, как настроить экземпляр Envoy версии 1.30+ для экспорта трассировок в Dynatrace.",
    # --- prerequisites section (H3) ---
    "### Prerequisites": "### Предварительные требования",
    '* The [OTLP traces URL](/managed/ingest-from/opentelemetry/otlp-api "%s") for the export.'
    % TT_OTLP: '* [URL для трассировок OTLP](/managed/ingest-from/opentelemetry/otlp-api "%s") для экспорта.'
    % RU_OTLP,
    "* The OneAgent Envoy code module is disabled.": "* Кодовый модуль OneAgent для Envoy отключён.",
    "To do this:": "Для этого:",
    "1. Go to the applicable configuration page:": "1. Перейдите на соответствующую страницу конфигурации:",
    "+ For the entire environment, go to **Settings** > **Monitoring** > **Monitored technologies**.": "+ Для всей среды перейдите в **Settings** > **Monitoring** > **Monitored technologies**.",
    "+ For a particular host, go to **Your host** > **Host settings** > **General**.": "+ Для отдельного хоста перейдите в **Your host** > **Host settings** > **General**.",
    "2. Find **Envoy** in the list of monitored technologies and select  **Edit**.": "2. Найдите **Envoy** в списке отслеживаемых технологий и выберите **Edit**.",
    "3. Select the **Monitor Envoy** toggle, as appropriate, to disable the OneAgent Envoy code module.": "3. Выберите переключатель **Monitor Envoy** при необходимости, чтобы отключить кодовый модуль OneAgent для Envoy.",
    # --- steps section ---
    "### Steps": "### Шаги",
    "1. Get configuration entries": "1. Получить записи конфигурации",
    "1. In Dynatrace Hub, search for `Envoy`.": "1. В Dynatrace Hub выполните поиск `Envoy`.",
    "2. Select the Hub entry for Envoy.": "2. Выберите запись Hub для Envoy.",
    "3. Select **Set up**.": "3. Выберите **Set up**.",
    "4. Configure the API token.": "4. Настройте API-токен.",
    "5. Proceed with the following steps and use (and adjust) the two provided configuration snippets where applicable.": "5. Выполните следующие шаги и используйте (при необходимости скорректировав) два предоставленных фрагмента конфигурации там, где применимо.",
    "2. Add Dynatrace cluster entry for OpenTelemetry export": "2. Добавить запись кластера Dynatrace для экспорта OpenTelemetry",
    # Note: line 48 has mojibake BOM (ï»¿) after "cluster" and after "step 2" --
    # norm() strips BOM_CLS before matching, so key uses the clean string.
    "For Envoy to send traces to Dynatrace, you first need to configure a [cluster](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) entry for Dynatrace in the Envoy configuration file. For that, add the [cluster configuration entry as obtained in step 2](#snippets) under the top-level `clusters` key.": "Чтобы Envoy мог отправлять трассировки в Dynatrace, сначала нужно настроить запись [cluster](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) для Dynatrace в файле конфигурации Envoy. Для этого добавьте [запись конфигурации cluster, полученную на шаге 2](#snippets), под ключом верхнего уровня `clusters`.",
    "3. Dynatrace-specific configuration for the OpenTelemetry tracer": "3. Конфигурация, специфичная для Dynatrace, для tracer OpenTelemetry",
    # Note: line 52 has two mojibake BOMs (ï»¿) after "filter" and after "file" --
    # norm() strips them, so key uses clean chars.
    "Next, you need to add the tracing provider to the [HTTP connection manager filter](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management#http-connection-management) in the [Envoy configuration file](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static#listeners).": "Затем нужно добавить провайдер трассировки к [фильтру HTTP connection manager](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management#http-connection-management) в [файле конфигурации Envoy](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static#listeners).",
    'Use the [tracer configuration entry you obtained in step 2](#snippets), configure the [API token](#prerequisites) under `tracing` - `provider` - `typed_config` - `http_service` - `request_headers_to_add` - `header` - `value` (the correct syntax is `value: "Api-Token YOUR_API_TOKEN_HERE"`), and add the tracer configuration under aforementioned `filters` entry.': 'Используйте [запись конфигурации tracer, полученную на шаге 2](#snippets), настройте [API-токен](#prerequisites) в разделе `tracing` - `provider` - `typed_config` - `http_service` - `request_headers_to_add` - `header` - `value` (правильный синтаксис: `value: "Api-Token YOUR_API_TOKEN_HERE"`), и добавьте конфигурацию tracer в упомянутую выше запись `filters`.',
    "4. Verify the setup": "4. Проверить настройку",
    "Once the setup is complete and you have ingested your first data, you can verify if the traces show up in Dynatrace.": "После завершения настройки и приёма первых данных можно проверить, отображаются ли трассировки в Dynatrace.",
    # --- image line (alt stays EN; no tooltip to translate) ---
    "![trace](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)": "![trace](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)",
    # --- standalone "trace" caption line (EN kept, no Russian content) ---
    # Put in PASS below.
    # --- related topics ---
    "## Related topics": "## Связанные темы",
    '* [Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Learn how to extend observability in Dynatrace with Prometheus metrics.")': '* [Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Узнайте, как расширить наблюдаемость в Dynatrace с помощью метрик Prometheus.")',
    '* [Istio/Envoy proxy metrics](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection")': '* [Метрики прокси Istio/Envoy](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Приём метрик Istio и обнаружение топологии")',
    **S,
}

# Lines kept verbatim (no Russian content):
# "trace" is a standalone EN alt-text echo line — no CYR needed.
PASS = {
    "trace",
}

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
