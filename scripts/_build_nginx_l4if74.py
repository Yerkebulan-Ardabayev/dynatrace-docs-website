# -*- coding: utf-8 -*-
"""nginx.md MONSTER builder (L4-IF.74).

635 KB / 6886 lines, but ~6240 are NGINX package URLs / image names (auto-PASS,
kept EN) and ~110 are version-table rows (programmatic cell translation: versions
/dates/OneAgent-versions stay EN, status + column headers -> RU). Only ~40 prose
lines are real translation (TRANS). Custom loop (not build_one) for the auto-PASS
+ programmatic table handling.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import qa_one, _demoji
from _build_otel_uc_l4if68 import norm, read_lf

REL = "ingest-from/technology-support/application-software"
FN = "nginx.md"
BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
EN = os.path.join(BASE, "managed", REL, FN)
RU = os.path.join(BASE, "managed-ru", REL, FN)

# ---- prose / headings (real translation) ----
TRANS = {
    "title: NGINX": "title: NGINX",
    "# NGINX": "# NGINX",
    "* Reference": "* Справочник",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Oct 23, 2025": "* Обновлено 23 октября 2025 г.",
    "With the NGINX code module of OneAgent, you can get observability for your NGINX instances and processed web requests.":
        "С помощью кодового модуля NGINX в OneAgent можно получить наблюдаемость для экземпляров NGINX и обрабатываемых веб-запросов.",
    "## Support lifecycle": "## Жизненный цикл поддержки",
    "Dynatrace supports a variety of NGINX, NGINX Plus, OpenResty, and Tengine versions, see the tables below. A notification appears on the NGINX process page in the Dynatrace web UI if an attempt is made to instrument an unsupported version.":
        "Dynatrace поддерживает множество версий NGINX, NGINX Plus, OpenResty и Tengine, см. таблицы ниже. Если выполняется попытка инструментировать неподдерживаемую версию, на странице процесса NGINX в веб-интерфейсе Dynatrace появляется уведомление.",
    "If your OneAgent build date is newer than a specific NGINX release date, the NGINX code module may be able to instrument your NGINX release even if it's not listed in the supported version tables.":
        "Если дата сборки OneAgent новее даты выпуска конкретной версии NGINX, кодовый модуль NGINX может инструментировать ваш выпуск NGINX, даже если он не указан в таблицах поддерживаемых версий.",
    "### Support for NGINX": "### Поддержка NGINX",
    "### Support for NGINX Plus": "### Поддержка NGINX Plus",
    "### Supported for OpenResty": "### Поддержка OpenResty",
    "### Support for Tengine": "### Поддержка Tengine",
    "Support for the latest NGINX release is typically included in the next subsequent OneAgent releases.":
        "Поддержка последнего выпуска NGINX, как правило, включается в ближайшие последующие выпуски OneAgent.",
    "Support for the latest NGINX Plus release may differ from the NGINX support lifecycle, but we aim to stay current.":
        "Поддержка последнего выпуска NGINX Plus может отличаться от жизненного цикла поддержки NGINX, но мы стремимся поддерживать актуальность.",
    "Support for the latest OpenResty release may differ from the NGINX support lifecycle, but we aim to stay current.":
        "Поддержка последнего выпуска OpenResty может отличаться от жизненного цикла поддержки NGINX, но мы стремимся поддерживать актуальность.",
    "Support for the latest Tengine release may differ from the NGINX support lifecycle, but we aim to stay current.":
        "Поддержка последнего выпуска Tengine может отличаться от жизненного цикла поддержки NGINX, но мы стремимся поддерживать актуальность.",
    "Support details for NGINX versions 1.4 - 1.11.4":
        "Сведения о поддержке версий NGINX 1.4 - 1.11.4",
    "Support for the CPU architecture PPCLE was added with OneAgent version 1.169 and ARM64 (AArch64) with OneAgent version 1.189.":
        "Поддержка архитектуры CPU PPCLE добавлена в OneAgent версии 1.169, а ARM64 (AArch64) - в OneAgent версии 1.189.",
    "Supported binaries for which Dynatrace has debug information available":
        "Поддерживаемые бинарные файлы, для которых у Dynatrace есть отладочная информация",
    "The NGINX code module uses debug information from the NGINX packages for instrumenting NGINX. Standard NGINX package sources are regularly discovered by Dynatrace to support new binaries. If you use other binaries (for example, custom builds), you need to provide their debug packages locally.":
        "Кодовый модуль NGINX использует отладочную информацию из пакетов NGINX для инструментирования NGINX. Источники стандартных пакетов NGINX регулярно обнаруживаются Dynatrace для поддержки новых бинарных файлов. Если вы используете другие бинарные файлы (например, пользовательские сборки), необходимо предоставить их отладочные пакеты локально.",
    "See [OneAgent support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix) for more information.":
        "Подробнее см. [матрицу поддержки OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix).",
    "See [OneAgent support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#os-code-modules \"Learn which capabilities are supported by OneAgent on different operating systems and platforms.\") for more details.":
        "Подробнее см. [матрицу поддержки OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#os-code-modules \"Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на платформах.\").",
    "## NGINX HTTP connection metrics": "## Метрики HTTP-соединений NGINX",
    "## NGINX Plus metrics": "## Метрики NGINX Plus",
    "The NGINX module captures HTTP connection metrics if you build your NGINX with [http\\_stub\\_status\\_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html).":
        "Модуль NGINX собирает метрики HTTP-соединений, если вы собрали NGINX с [http\\_stub\\_status\\_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html).",
    "The NGINX module captures NGINX Plus metrics from [NGINX Plus Status API (up to R15) or NGINX Plus API (R16+)](https://www.nginx.com/blog/transitioning-to-nginx-plus-api-configuration-monitoring/).":
        "Модуль NGINX собирает метрики NGINX Plus из [NGINX Plus Status API (до R15) или NGINX Plus API (R16+)](https://www.nginx.com/blog/transitioning-to-nginx-plus-api-configuration-monitoring/).",
    "NGINX deep monitoring is currently not supported on Windows.":
        "Глубокий мониторинг NGINX в настоящее время не поддерживается в Windows.",
    "Support on Windows": "Поддержка в Windows",
    "Which modules of NGINX are supported for outgoing web requests?":
        "Какие модули NGINX поддерживаются для исходящих веб-запросов?",
    "How to build NGINX with http\\_stub\\_status\\_module":
        "Как собрать NGINX с http\\_stub\\_status\\_module",
    "Use the `--with-http_stub_status_module` configuration parameter.":
        "Используйте параметр конфигурации `--with-http_stub_status_module`.",
    "How to check if an NGINX binary was built with http\\_stub\\_status\\_module":
        "Как проверить, собран ли бинарный файл NGINX с http\\_stub\\_status\\_module",
    "Invoke `nginx -V` on your command line. This will return the NGINX configuration parameters.":
        "Выполните `nginx -V` в командной строке. Будут возвращены параметры конфигурации NGINX.",
    "Make sure that the output contains the `--with-http_stub_status_module` parameter.":
        "Убедитесь, что вывод содержит параметр `--with-http_stub_status_module`.",
    "Where I can find the OneAgent build date?": "Где найти дату сборки OneAgent?",
    "The OneAgent build date is part of the OneAgent intaller version, for example 1.254.0.**20221012-201831**.":
        "Дата сборки OneAgent является частью версии установщика OneAgent, например 1.254.0.**20221012-201831**.",
    "The API needs to be turned on and accessible by the NGINX module. If the API is protected by NGINX authentication, ensure it's accessible from localhost for HTTP GET requests. The Nginx module requires the API configuration to be available from the start (adding the configuration during Nginx runtime and reloading it is not supported).":
        "API должен быть включён и доступен для модуля NGINX. Если API защищён аутентификацией NGINX, убедитесь, что он доступен с localhost для HTTP-запросов GET. Модуль NGINX требует, чтобы конфигурация API была доступна с момента запуска (добавление конфигурации во время работы NGINX и её перезагрузка не поддерживаются).",
    "A notification appears on the NGINX process page in Dynatrace if the API for extended NGINX Plus metrics is not accessible.":
        "Если API для расширенных метрик NGINX Plus недоступен, на странице процесса NGINX в Dynatrace появляется уведомление.",
    "![NGINX supported versions](https://dt-cdn.net/images/nginx-instrumentation-simplified-1800-9148ec25fc.png)":
        "![Поддерживаемые версии NGINX](https://dt-cdn.net/images/nginx-instrumentation-simplified-1800-9148ec25fc.png)",
    "The following image can help you to determine if a NGINX release is qualified for support:":
        "Следующее изображение поможет определить, подходит ли выпуск NGINX для поддержки:",
    "NGINX supported versions": "Поддерживаемые версии NGINX",
    "Supported if the used binary is in the list of [supported binaries](/managed/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries \"Learn the details of Dynatrace support for NGINX.\") or the corresponding debug information is available locally.":
        "Поддерживается, если используемый бинарный файл есть в списке [поддерживаемых бинарных файлов](/managed/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries \"Узнайте подробности о поддержке NGINX в Dynatrace.\") или соответствующая отладочная информация доступна локально.",
    "Supported if the used binary is either in the list of [supported binaries](/managed/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries \"Learn the details of Dynatrace support for NGINX.\") or the corresponding debug information is available locally.":
        "Поддерживается, если используемый бинарный файл либо есть в списке [поддерживаемых бинарных файлов](/managed/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries \"Узнайте подробности о поддержке NGINX в Dynatrace.\"), либо соответствующая отладочная информация доступна локально.",
    "Supported if the used binary is in the list of [supported binaries](/managed/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries \"Learn the details of Dynatrace support for NGINX.\").":
        "Поддерживается, если используемый бинарный файл есть в списке [поддерживаемых бинарных файлов](/managed/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries \"Узнайте подробности о поддержке NGINX в Dynatrace.\").",
}

# ---- table cells ----
COL = {
    "Observability for": "Наблюдаемость для", "Including": "Включая",
    "Incoming web requests": "Входящие веб-запросы",
    "Outgoing web requests": "Исходящие веб-запросы",
    "All incoming web requests to NGINX": "Все входящие веб-запросы к NGINX",
    "Outgoing web requests originating from a [supported module of NGINX](#nginx-supported-modules)":
        "Исходящие веб-запросы, исходящие от [поддерживаемого модуля NGINX](#nginx-supported-modules)",
    "* Traffic and requests * Response sizes * Accepted, active, and dropped connections":
        "* Трафик и запросы * Размеры ответов * Принятые, активные и сброшенные соединения",
    "Server zones  * Traffic and requests per server zone  Upstreams  * Traffic and requests * Upstream health  Caches  * Cache performance * Cache usage":
        "Серверные зоны  * Трафик и запросы на серверную зону  Апстримы  * Трафик и запросы * Состояние апстримов  Кэши  * Производительность кэша * Использование кэша",
    "NGINX version": "Версия NGINX", "NGINX Plus version": "Версия NGINX Plus",
    "OpenResty version": "Версия OpenResty", "Tengine version": "Версия Tengine",
    "Vendor released": "Выпущено вендором", "Vendor End of life": "Окончание поддержки вендором",
    "First supported Dynatrace OneAgent version": "Первая поддерживаемая версия Dynatrace OneAgent",
    "Last supported Dynatrace OneAgent version": "Последняя поддерживаемая версия Dynatrace OneAgent",
    "Modules of NGINX": "Модули NGINX", "Versions": "Версии",
    "All versions supported": "Все версии поддерживаются",
}
STATUS = [
    ("Not supported", "Не поддерживается"),
    ("Supported", "Поддерживается"),
    ("Limited", "Ограниченно"),
]
TABLE_SEP = re.compile(r"^\|[\s|:\-]+\|?$")
PKG = re.compile(r"https?://|\.tgz|\.deb|\.rpm|k8s\.gcr\.io|gcr\.io")
IDTOKEN = re.compile(r"^[#*+\-\s]*[\w.\-:~/\\]+$")  # bare identifier/version (allows md-escaped \_)
CYR = re.compile(r"[А-Яа-яЁё]")


def tr_cell(c):
    c = c.strip()
    if not c or c == "-":
        return c
    if c in COL:
        return COL[c]
    for en, ru in STATUS:
        if c.startswith(en):
            return ru + c[len(en):]  # keep [n](#fn..) suffix
    return c  # versions/dates/OneAgent-versions/fn-refs unchanged


def tr_row(raw):
    parts = raw.split("|")
    inner = parts[1:-1] if parts[0] == "" and parts[-1] == "" else parts
    out = [" " + tr_cell(p) + " " for p in inner]
    return "|" + "|".join(out) + "|"


def _clean(s):
    # strip the BOM scraping artifact in both its mojibake forms (canon L4-IF.66)
    return s.replace("ï»¿", "").replace("﻿", "")


def is_pkg(raw):
    body = raw.lstrip("#*+- ").strip()
    if body.startswith(("http://", "https://")):  # URL list/heading line
        return True
    # bare package/version identifier line (no Cyrillic, no spaced prose)
    if not CYR.search(raw) and IDTOKEN.match(raw) and re.search(r"\d", body):
        return True
    return False


def main():
    en_lines = read_lf(EN).split("\n")
    tmap = {norm(_clean(_demoji(k))): v for k, v in TRANS.items()}
    out, in_fence = [], False
    for ln in en_lines:
        raw = _clean(_demoji(ln.strip()))
        st = norm(raw)
        indent = ln[: len(ln) - len(ln.lstrip())]
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence or st == "" or st == "---":
            out.append(_clean(_demoji(ln)))
            continue
        if raw.startswith(("source:", "scraped:")):
            out.append(ln)
            continue
        if st in tmap:
            out.append(indent + tmap[st])
            continue
        if TABLE_SEP.match(raw):
            out.append(indent + raw)
            continue
        if raw.startswith("|"):
            out.append(indent + tr_row(raw))
            continue
        if raw in ("1", "2"):  # footnote numbers
            out.append(indent + raw)
            continue
        if is_pkg(raw):
            out.append(indent + raw)
            continue
        raise SystemExit(f"UNTRANSLATED: {ln!r}")
    assert len(out) == len(en_lines), f"parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(RU), exist_ok=True)
    with open(RU, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK {FN}: {len(out)} lines")


if __name__ == "__main__":
    main()
    qa_one(REL, FN)
