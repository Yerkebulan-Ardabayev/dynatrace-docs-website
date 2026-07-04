# -*- coding: utf-8 -*-
"""Build: ingest-from/technology-support/application-software/java/quarkus.md

765 EN lines, but only 55 translatable prose/heading/table/link lines (rest is
code fences / package URLs / blanks). To avoid transcribing 55 long EN keys with
their exact apostrophes/backticks/FEFF, we extract the EXACT keys from the file
(same filter as build_one) and zip them with the RU list below, in first-
appearance order. An assert guards against drift. PASS = kept-EN lines.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one, _demoji
from _otel_canon import norm, read_lf

REL = "ingest-from/technology-support/application-software/java"
FNAME = "quarkus.md"

# Kept EN: H4 product name + markdown table separator.
PASS = {
    "#### OpenTelemetry",
    "| --- | --- |",
}

# RU translations, in order of first appearance of each unique translatable line
# (PASS lines excluded). Grounded on the shipped java sibling graalvm-native-image
# and the tech-support glossary: UI labels kept EN (**Hosts**/**Settings**/**Save
# changes**...), full-stack/Micrometer/native image kept EN, endpoint->эндпоинт,
# trace->трассировка, exporter->экспортёр, extension->расширение.
RU = [
    "title: Мониторинг нативных приложений Red Hat Quarkus",
    "# Мониторинг нативных приложений Red Hat Quarkus",
    "* Чтение: 3 мин",
    "* Обновлено 28 января 2026 г.",
    "[Red Hat Quarkus](https://www.redhat.com/en/topics/cloud-native-apps/what-is-quarkus), это Java-фреймворк с открытым исходным кодом, оптимизированный для GraalVM Native Images, чтобы сделать Java полноценным участником мира микросервисов. Quarkus принадлежит к семейству full-stack фреймворков, адаптированных для Kubernetes. Он включает современные библиотеки Java и следует последним стандартам Java.",
    "Узнайте, как Dynatrace может трассировать нативные Java-приложения и отслеживать метрики и логи приложения Quarkus, скомпилированного как native image.",
    "## Предварительные требования",
    "* Ваша версия GraalVM [поддерживается Dynatrace](/managed/ingest-from/technology-support#java-native-image \"Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.\").",
    "* GraalVM настроен на сборку native images. Подробнее см. в руководстве Quarkus [Building a native executable](https://quarkus.io/guides/building-native-image).",
    "* OneAgent или Dynatrace Operator установлен на машине, где будет выполняться приложение.",
    "Необходимая установка зависит от вашего приложения:",
    "| Если ваше приложение работает | См. инструкцию для |",
    "| на виртуальной машине или физическом сервере | [OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation \"Установка OneAgent на сервер в первый раз.\") |",
    "| как рабочая нагрузка в Kubernetes или OpenShift | [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment \"Развёртывание Dynatrace Operator в Kubernetes\") |",
    "## Трассировки",
    "Dynatrace может автоматически трассировать Quarkus-приложения, скомпилированные в режиме JIT (just-in-time) и выполняемые на OpenJDK HotSpot JVM и GraalVM.",
    "Для Quarkus-приложений, скомпилированных в режиме AOT (ahead-of-time) и выполняемых на GraalVM, см. [GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image \"Установка, настройка и управление модулем Dynatrace GraalVM Native Image.\") для начала работы.",
    "Информацию трассировки Quarkus можно экспортировать с помощью [OpenTelemetry](/managed/ingest-from/opentelemetry \"Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.\").",
    "Упрощённые варианты настройки при мониторинге через OneAgent",
    "Если ваша среда отслеживается OneAgent, вам доступны следующие упрощённые варианты настройки:",
    "* **[OneAgent OpenTelemetry Span Sensor](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#oneagent-otel-span-sensor \"Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.\")** Рекомендуется: автоматически захватывает вызовы OpenTelemetry API и сшивает их в трассировки OneAgent без необходимости в ручной настройке экспорта OTLP. Чтобы использовать этот подход, [включите OpenTelemetry Span Sensor](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration \"Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.\") и **не** настраивайте ручной экспорт OTLP.",
    "* **[Локальный эндпоинт OTLP через EEC](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent \"Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.\")**: для неконтейнеризованных сред можно отправлять трассировки на локальный эндпоинт OTLP по адресу `http://localhost:14499/otlp/v1/traces` после [включения Extension Execution Controller](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent \"Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.\"). Это устраняет необходимость в API-токенах и внешних эндпоинтах.",
    "Если вы предпочитаете метод на основе OneAgent, пропустите ручную настройку ниже.",
    "Если вы предпочитаете ручную настройку или не используете OneAgent, выполните следующие шаги.",
    "Чтобы вручную настроить экспорт OpenTelemetry, используйте [специфичные для Quarkus параметры настройки](https://dt-url.net/3g039zt) для настройки экспортёра на отправку данных трассировки на один из двух доступных эндпоинтов, [ActiveGate или OneAgent](/managed/ingest-from/opentelemetry/otlp-api \"Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.\").",
    "В следующем примере показано, как настроить `application.properties` для экспорта на эндпоинт Dynatrace SaaS. Он указывает URL API и необходимый заголовок [`Authorization`](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate \"Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.\") в процентной кодировке с API-токеном.",
    "## Метрики",
    "Red Hat рекомендует получать метрики из Quarkus с помощью библиотеки `quarkus-micrometer-registry-prometheus`.",
    "Чтобы узнать, как использовать метрики Micrometer в приложении Quarkus, см. руководство Quarkus [Micrometer metrics](https://quarkus.io/guides/micrometer).",
    "Dynatrace предлагает два подхода к получению метрик Micrometer из Prometheus: через API или через расширение.",
    "### Приём метрик Micrometer через Dynatrace API",
    "Используйте Dynatrace API для приёма метрик, полученных из библиотеки `quarkus-micrometer-registry-prometheus`.",
    "Подробнее о процедуре приёма см. [Отправка метрик Micrometer в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer \"Узнайте, как отправлять метрики Micrometer в Dynatrace.\").",
    "Для нативно собранных приложений обязательно следуйте подходу [Directly in Micrometer](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer#properties-direct \"Узнайте, как отправлять метрики Micrometer в Dynatrace.\").",
    "### Приём метрик Micrometer через расширение",
    "Используйте платформу Dynatrace [Extension 2.0](/managed/ingest-from/extensions \"Узнайте, как создавать Dynatrace Extensions и управлять ими.\") для приёма метрик Micrometer, полученных из [источника данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions \"Узнайте, как создать расширение Prometheus с помощью платформы Extensions.\"), для этого необходимо создать пользовательское расширение.",
    "В качестве отправной точки можно использовать приведённый ниже пример пользовательского расширения. Он адаптирован под библиотеку `quarkus-micrometer-registry-prometheus`. Обязательно используйте правильный эндпоинт метрик в своей конфигурации. Эндпоинт по умолчанию: `localhost:8080/q/metrics`.",
    "Пример расширения на основе Prometheus",
    "## Логи",
    "Dynatrace предлагает [различные варианты](/managed/ingest-from/extend-dynatrace/extend-logs \"Узнайте, как расширить наблюдаемость логов в Dynatrace.\") для сбора логов из ваших приложений и сред.",
    "Чтобы узнать, как настроить логирование в приложении Quarkus, см. руководство Quarkus [Configuring logging](https://quarkus.io/guides/logging).",
    "Для приведённой ниже процедуры предполагается, что ваше приложение записывает логи в файл `/var/log/quarkus-app.log`.",
    "1. Запустите нативное приложение Quarkus.",
    "2. Перейдите в **Hosts** и выберите свой хост.",
    "3. Прокрутите вниз до раздела **Process analysis** и в списке процессов выберите процесс своего нативного приложения Quarkus.",
    "4. В правой части панели **Process** выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg \"More\") > **Settings**.",
    "5. В настройках группы процессов выберите **Log monitoring** > **Add new log for monitoring**.",
    "6. Введите полный путь к файлу логов. Обязательно соблюдайте [требования к пути логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2#considerations-for-adding-text-log-files-manually \"Узнайте, как вручную добавлять файлы логов для анализа.\").",
    "7. Выберите **Save changes**.",
    "8. [Включите добавленные файлы логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 \"Узнайте, как включать и исключать источники логов для анализа.\") в своё хранилище логов.",
    "## Связанные темы",
    "* [Отправка метрик Micrometer в Dynatrace](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer \"Узнайте, как отправлять метрики Micrometer в Dynatrace.\")",
    "* [Управление расширениями Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions \"Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик Prometheus.\")",
    "* [Источник данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions \"Узнайте, как создать расширение Prometheus с помощью платформы Extensions.\")",
    "* [Эндпоинты Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api \"Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.\")",
]


def extract_keys():
    """Exact translatable EN keys, first-appearance order (mirrors build_one)."""
    en = read_lf(os.path.join(os.path.dirname(__file__), "..", "docs", "managed", REL, FNAME)).split("\n")
    passn = {norm(_demoji(k)) for k in PASS}
    keys, seen, in_fence = [], set(), False
    for ln in en:
        raw = _demoji(ln.strip())
        st = norm(raw)
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or st in ("", "---"):
            continue
        if raw.startswith("source:") or raw.startswith("scraped:"):
            continue
        if st in passn or st in seen:
            continue
        seen.add(st)
        keys.append(raw)
    return keys


KEYS = extract_keys()
assert len(KEYS) == len(RU), f"key/RU drift: {len(KEYS)} keys != {len(RU)} RU"
TRANS = dict(zip(KEYS, RU))
build_one(REL, FNAME, TRANS, PASS)
print("build OK")
qa_one(REL, FNAME)
