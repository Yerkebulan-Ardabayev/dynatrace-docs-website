# -*- coding: utf-8 -*-
"""L4-IF.64 builder: setup-on-k8s/reference/network.md (1 file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Reference/config page: parameter/field names, YAML keys, ports, CIDR/IP,
`feature.dynatrace.com/*`, backticked identifiers, kubectl/oc commands stay
byte-identical EN. Only prose + table-header words + link TITLE attributes
translate. Table separators / empty cells / bare footnote-number lines = PASS.

Note: EN source contains mojibake `ï»¿` before some `](` inside link TEXT (not
the URL). MOJI_RE strips it from EN line and TRANS keys, so keys match clean and
RU output stays clean (QA flags `ï»¿` in RU).
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/reference"

REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "network.md": {
        "title: Network traffic": "title: Сетевой трафик",
        "# Network traffic": "# Сетевой трафик",
        "* 3-min read": "* Чтение: 3 мин",
        "* Updated on Jan 02, 2026": "* Обновлено 02 января 2026 г.",
        "To ensure Dynatrace Operator components work correctly in a Kubernetes "
        "cluster, they need to be able to communicate with both the Dynatrace "
        "Cluster and the Kubernetes cluster.": "Чтобы компоненты Dynatrace Operator работали правильно в кластере "
        "Kubernetes, они должны иметь возможность взаимодействовать как с "
        "кластером Dynatrace, так и с кластером Kubernetes.",
        "Dynatrace Operator components are accessible through specific ports and "
        "access various resources inside and outside the Kubernetes cluster. For "
        "more details on which resources are accessed within the Kubernetes "
        "cluster, see the [Operator RBAC permissions]"
        "(/managed/ingest-from/setup-on-k8s/reference/security "
        '"This page provides an overview of the Dynatrace components, their '
        'default configurations, and the permissions they require") reference '
        "page.": "Компоненты Dynatrace Operator доступны через определённые порты и "
        "обращаются к различным ресурсам внутри и снаружи кластера Kubernetes. "
        "Подробнее о том, к каким ресурсам выполняется обращение внутри кластера "
        "Kubernetes, см. справочную страницу [Разрешения RBAC для Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/security "
        '"На этой странице приведён обзор компонентов Dynatrace, их конфигураций '
        'по умолчанию и требуемых ими разрешений").',
        # --- Ingress ---
        "## Ingress traffic": "## Входящий трафик",
        "| Source | Destination | Port | Note |": "| Источник | Назначение | Порт | Примечание |",
        "| kubelet | Dynatrace Operator `/healthz` | `TCP 10080` | Liveness probe "
        "[1](#fn-1-1-def) |": "| kubelet | Dynatrace Operator `/healthz` | `TCP 10080` | Liveness probe "
        "[1](#fn-1-1-def) |",
        "| Prometheus metrics scraper Optional | Dynatrace Operator `/metrics` | "
        "`TCP 8080` | Metrics address [2](#fn-1-2-def) |": "| Prometheus metrics scraper Необязательно | Dynatrace Operator `/metrics` | "
        "`TCP 8080` | Адрес метрик [2](#fn-1-2-def) |",
        "| kubelet | Dynatrace Webhook `/healthz` | `TCP 10080` | "
        "Liveness/Readiness probe [1](#fn-1-1-def) |": "| kubelet | Dynatrace Webhook `/healthz` | `TCP 10080` | "
        "Liveness/Readiness probe [1](#fn-1-1-def) |",
        "| kube-apiserver | Dynatrace Webhook `/inject`, `/label-ns`, `/validate*` "
        "| `TCP 8443` | Dynamic Admission Controller |": "| kube-apiserver | Dynatrace Webhook `/inject`, `/label-ns`, `/validate*` "
        "| `TCP 8443` | Dynamic Admission Controller |",
        "| Prometheus metrics scraperOptional | Dynatrace Webhook `/metrics` | "
        "`TCP 8080` | Metrics address [2](#fn-1-2-def) |": "| Prometheus metrics scraperНеобязательно | Dynatrace Webhook `/metrics` | "
        "`TCP 8080` | Адрес метрик [2](#fn-1-2-def) |",
        "| kubelet | Dynatrace Operator CSI driver `server` container `/healthz` | "
        "`TCP 9808` | Liveness probe [1](#fn-1-1-def) |": "| kubelet | Dynatrace Operator CSI driver `server` container `/healthz` | "
        "`TCP 9808` | Liveness probe [1](#fn-1-1-def) |",
        "| kubelet | Dynatrace Operator CSI driver `provisioner` container "
        "`/healthz` | `TCP 10090` | Liveness probe [1](#fn-1-1-def) |": "| kubelet | Dynatrace Operator CSI driver `provisioner` container "
        "`/healthz` | `TCP 10090` | Liveness probe [1](#fn-1-1-def) |",
        "| Prometheus metrics scraper Optional | Dynatrace Operator CSI driver "
        "`server` container `/metrics` | `TCP 8080` | Metrics address "
        "[2](#fn-1-2-def) |": "| Prometheus metrics scraper Необязательно | Dynatrace Operator CSI driver "
        "`server` container `/metrics` | `TCP 8080` | Адрес метрик "
        "[2](#fn-1-2-def) |",
        "| Prometheus metrics scraper Optional | Dynatrace Operator CSI driver "
        "`provisioner` container `/metrics` | `TCP 8090` | Metrics address "
        "[2](#fn-1-2-def) |": "| Prometheus metrics scraper Необязательно | Dynatrace Operator CSI driver "
        "`provisioner` container `/metrics` | `TCP 8090` | Адрес метрик "
        "[2](#fn-1-2-def) |",
        "| kubelet | ActiveGate `/rest/health` | `TCP 9999` | Readiness probe "
        "[1](#fn-1-1-def) |": "| kubelet | ActiveGate `/rest/health` | `TCP 9999` | Readiness probe "
        "[1](#fn-1-1-def) |",
        "| kubelet | Extension Execution Controller `/readyz` | `TCP 14599` | "
        "Readiness probe [1](#fn-1-1-def) |": "| kubelet | Extension Execution Controller `/readyz` | `TCP 14599` | "
        "Readiness probe [1](#fn-1-1-def) |",
        "| Application pods | ActiveGate `/*` | `TCP 9999` | Default `HTTPS` port |": "| Application pods | ActiveGate `/*` | `TCP 9999` | Порт `HTTPS` по умолчанию |",
        "| Application pods | ActiveGate `/*` | `TCP 9998` | Default `HTTP` port, "
        "Data ingest, API access |": "| Application pods | ActiveGate `/*` | `TCP 9998` | Порт `HTTP` по умолчанию, "
        "приём данных, доступ к API |",
        "| Application pods | Dynatrace Collector | [Telemetry ingest ports]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/"
        'telemetry-ingest#port-list "Enable Dynatrace telemetry ingest endpoints '
        'in Kubernetes for cluster-local data ingest.") | [Ingest telemetry data]'
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/"
        'telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in '
        'Kubernetes for cluster-local data ingest.") |': "| Application pods | Dynatrace Collector | [Порты приёма телеметрии]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/"
        'telemetry-ingest#port-list "Включите конечные точки приёма телеметрии '
        'Dynatrace в Kubernetes для локального приёма данных в кластере.") | '
        "[Приём данных телеметрии]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/"
        'telemetry-ingest "Включите конечные точки приёма телеметрии Dynatrace в '
        'Kubernetes для локального приёма данных в кластере.") |',
        "| kubelet | SQL Extension Executor container `/health/live` | `TCP 8080` "
        "| Liveness probe [1](#fn-1-1-def) |": "| kubelet | SQL Extension Executor container `/health/live` | `TCP 8080` "
        "| Liveness probe [1](#fn-1-1-def) |",
        "| kubelet | SQL Extension Executor container `/health/ready` | `TCP 8080` "
        "| Readiness probe [1](#fn-1-1-def) |": "| kubelet | SQL Extension Executor container `/health/ready` | `TCP 8080` "
        "| Readiness probe [1](#fn-1-1-def) |",
        # footnote 1 def (mojibake ï»¿ stripped from keys by MOJI_RE)
        "[Liveness probes](https://dt-url.net/dh03q2c) are used by Kubernetes to "
        "verify the container is running properly. If the request fails, the "
        "container will be restarted. [Readiness probes](https://dt-url.net/ml23qbl) "
        "are used by Kubernetes to verify the Pod is ready to accept traffic.": "[Проверки Liveness](https://dt-url.net/dh03q2c) используются Kubernetes для "
        "проверки того, что контейнер работает правильно. Если запрос не "
        "выполняется, контейнер будет перезапущен. [Проверки Readiness]"
        "(https://dt-url.net/ml23qbl) используются Kubernetes для проверки того, "
        "что под готов принимать трафик.",
        # footnote 2 def
        "[Metrics endpoints](https://dt-url.net/t543q6q) emit additional metrics "
        "in Prometheus format.": "[Конечные точки метрик](https://dt-url.net/t543q6q) выдают дополнительные "
        "метрики в формате Prometheus.",
        "No ingress traffic is accepted for EdgeConnect and OneAgent.": "Входящий трафик для EdgeConnect и OneAgent не принимается.",
        # --- Egress ---
        "## Egress traffic": "## Исходящий трафик",
        "Dynatrace Operator components have to access both the Kubernetes cluster "
        "and resources outside the Cluster to function properly. All resources in "
        "the namespace of Dynatrace Operator, with the default namespace being "
        "`dynatrace`, need to be able to resolve DNS requests.": "Компоненты Dynatrace Operator должны обращаться как к кластеру Kubernetes, "
        "так и к ресурсам за пределами кластера, чтобы работать правильно. Все "
        "ресурсы в пространстве имён Dynatrace Operator, где пространством имён по "
        "умолчанию является `dynatrace`, должны иметь возможность разрешать "
        "DNS-запросы.",
        "Depending on your setup, the default port may be different from "
        "`TCP 443`.": "В зависимости от вашей конфигурации порт по умолчанию может отличаться "
        "от `TCP 443`.",
        "| * Dynatrace Operator * Dynatrace Webhook * Dynatrace Operator CSI "
        "driver * ActiveGate * Extension Execution Controller | kube-dns | "
        "`TCP 53`, `UDP 53` [1](#fn-2-1-def) | Host name resolution for service "
        "discovery |": "| * Dynatrace Operator * Dynatrace Webhook * Dynatrace Operator CSI "
        "driver * ActiveGate * Extension Execution Controller | kube-dns | "
        "`TCP 53`, `UDP 53` [1](#fn-2-1-def) | Разрешение имён хостов для "
        "обнаружения сервисов |",
        "| Dynatrace Operator | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | "
        "Server-side configuration [2](#fn-2-2-def) |": "| Dynatrace Operator | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | "
        "Настройка на стороне сервера [2](#fn-2-2-def) |",
        "| Dynatrace Operator | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | "
        "Lifecycle management of components |": "| Dynatrace Operator | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | "
        "Управление жизненным циклом компонентов |",
        "| Dynatrace Webhook | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | "
        "Mutating/Validating/Conversion requests |": "| Dynatrace Webhook | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | "
        "Запросы Mutating/Validating/Conversion |",
        "| Dynatrace Operator CSI driver | Dynatrace server | `TCP 443` "
        "[1](#fn-2-1-def) | Default location for code module binaries "
        "[2](#fn-2-2-def) |": "| Dynatrace Operator CSI driver | Dynatrace server | `TCP 443` "
        "[1](#fn-2-1-def) | Расположение по умолчанию для двоичных файлов модуля "
        "кода [2](#fn-2-2-def) |",
        "| Dynatrace Operator CSI driver | kube-apiserver | `TCP 443` "
        "[1](#fn-2-1-def) | CSI volume handling |": "| Dynatrace Operator CSI driver | kube-apiserver | `TCP 443` "
        "[1](#fn-2-1-def) | Обработка томов CSI |",
        "| Dynatrace Operator CSI driver | private registry | `TCP 443` "
        "[1](#fn-2-1-def) | Optional Communication with private registry to "
        "access code modules [3](#fn-2-3-def) |": "| Dynatrace Operator CSI driver | private registry | `TCP 443` "
        "[1](#fn-2-1-def) | Необязательно Взаимодействие с приватным реестром для "
        "доступа к модулям кода [3](#fn-2-3-def) |",
        "| ActiveGate | Communication endpoints [4](#fn-2-4-def) | `TCP 443`, "
        "`TCP 9999` [1](#fn-2-1-def) | Observability information "
        "[2](#fn-2-2-def) |": "| ActiveGate | Communication endpoints [4](#fn-2-4-def) | `TCP 443`, "
        "`TCP 9999` [1](#fn-2-1-def) | Информация наблюдаемости "
        "[2](#fn-2-2-def) |",
        "| ActiveGate | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Collect "
        "resources |": "| ActiveGate | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Сбор "
        "ресурсов |",
        "| ActiveGate | Application Pods | Prometheus Exporter port "
        "[1](#fn-2-1-def) | Collect metrics |": "| ActiveGate | Application Pods | Prometheus Exporter port "
        "[1](#fn-2-1-def) | Сбор метрик |",
        "| OneAgent | Communication endpoints [4](#fn-2-4-def) | `TCP 443`, "
        "`TCP 9999` [1](#fn-2-1-def) | Observability information "
        "[2](#fn-2-2-def) |": "| OneAgent | Communication endpoints [4](#fn-2-4-def) | `TCP 443`, "
        "`TCP 9999` [1](#fn-2-1-def) | Информация наблюдаемости "
        "[2](#fn-2-2-def) |",
        "| EdgeConnect | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | "
        "Server-side configuration [2](#fn-2-2-def) |": "| EdgeConnect | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | "
        "Настройка на стороне сервера [2](#fn-2-2-def) |",
        "| EdgeConnect | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Optional "
        "Workflow interactions [5](#fn-2-5-def) |": "| EdgeConnect | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | "
        "Необязательно Взаимодействия с Workflow [5](#fn-2-5-def) |",
        "| Extension Execution Controller | ActiveGate | `TCP 443` "
        "[1](#fn-2-1-def) | Extension configuration and telemetry data "
        "[2](#fn-2-2-def) |": "| Extension Execution Controller | ActiveGate | `TCP 443` "
        "[1](#fn-2-1-def) | Настройка расширений и данные телеметрии "
        "[2](#fn-2-2-def) |",
        # egress footnote defs
        "Depending on your setup, the port may differ from the default.": "В зависимости от вашей конфигурации порт может отличаться от значения по "
        "умолчанию.",
        "Communication with hosts must be allowed as configured in [DynaKube]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") (`apiUrl`) or [EdgeConnect]'
        "(/managed/upgrade/unavailable-in-managed "
        '"Your selection is unavailable in Dynatrace Managed.") (`apiServer`) '
        "custom resources. Different communication endpoints may be used as "
        "fallback to ensure proper connection.": "Взаимодействие с хостами должно быть разрешено в соответствии с настройкой "
        "в пользовательских ресурсах [DynaKube]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.") (`apiUrl`) или [EdgeConnect]'
        "(/managed/upgrade/unavailable-in-managed "
        '"Ваш выбор недоступен в Dynatrace Managed.") (`apiServer`). Для '
        "обеспечения корректного подключения в качестве резервных могут "
        "использоваться разные конечные точки взаимодействия.",
        "Only required when `codeModulesImage` field is used.": "Требуется только при использовании поля `codeModulesImage`.",
        "[Supported connectivity schemes for ActiveGates]"
        "(/managed/ingest-from/dynatrace-activegate/"
        'supported-connectivity-schemes-for-activegates "Learn about the '
        "connectivity priorities between ActiveGate types as well as the "
        'priorities between ActiveGates and OneAgents.")': "[Поддерживаемые схемы подключения для ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/"
        'supported-connectivity-schemes-for-activegates "Узнайте о приоритетах '
        "подключения между типами ActiveGate, а также о приоритетах между "
        'ActiveGate и OneAgent.")',
        "Only required when Kubernetes Automation is enabled.": "Требуется только при включённой Kubernetes Automation.",
    },
}

# Lines copied verbatim (table separators / bare footnote-number lines).
PASS = {
    "network.md": {
        "| --- | --- | --- | --- |",
        "1",
        "2",
        "3",
        "4",
        "5",
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
            # copy verbatim but strip mojibake bytes if any (clean RU output)
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
