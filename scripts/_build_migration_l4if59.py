# -*- coding: utf-8 -*-
"""L4-IF.59 builder: setup-on-k8s/guides/migration batch (3 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Files:
- migration.md            (card-grid index; cards are concatenated link lines)
- migrate-dto-to-tenant.md (numbered steps + code, Kubernetes/OpenShift tabs)
- migrate-to-helm.md       (numbered steps + code + 2 cross-links)
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides"

# per-file relative dir override (default SUB/migration)
REL = {
    "migration.md": SUB,
}

TRANS = {
    "migration.md": {
        "title: Migration guides": "title: Руководства по миграции",
        "# Migration guides": "# Руководства по миграции",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "Explore step-by-step migration guides to help you transition between "
        "different Dynatrace monitoring setups.": "Изучите пошаговые руководства по миграции, которые помогут вам перейти "
        "между различными вариантами настройки мониторинга Dynatrace.",
        "[### Migrate from classic full-stack to cloud-native full-stack": "[### Миграция с классического full-stack на cloud-native full-stack",
        'Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack deployment.](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.")[### Migrate from classic full-stack to application monitoring mode': 'Перенесите ваше развёртывание Dynatrace с классического full-stack на развёртывание cloud-native full-stack.](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Перенесите ваше развёртывание Dynatrace с классического full-stack на режим cloud-native full-stack.")[### Миграция с классического full-stack на режим мониторинга приложений',
        'Migrate your Dynatrace deployment from classic full-stack to application monitoring mode.](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring "Migrate your Dynatrace deployment from classic full-stack to application monitoring mode.")[### Migrate from cloud-native full-stack to application monitoring mode': 'Перенесите ваше развёртывание Dynatrace с классического full-stack на режим мониторинга приложений.](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring "Перенесите ваше развёртывание Dynatrace с классического full-stack на режим мониторинга приложений.")[### Миграция с cloud-native full-stack на режим мониторинга приложений',
        'Migrate your Dynatrace deployment from cloud-native full-stack to application monitoring mode.](/managed/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring "Migrate your Dynatrace deployment from cloud-native full-stack to application monitoring mode.")[### Migrate Dynatrace Operator to a new environment': 'Перенесите ваше развёртывание Dynatrace с cloud-native full-stack на режим мониторинга приложений.](/managed/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring "Перенесите ваше развёртывание Dynatrace с cloud-native full-stack на режим мониторинга приложений.")[### Миграция Dynatrace Operator в новое окружение',
        'Migrate monitoring to a new Dynatrace environment on Kubernetes clusters.](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant "Migrate monitoring to a new Dynatrace environment on Kubernetes clusters.")[### Migrate from OneAgent Operator to Dynatrace Operator': 'Перенесите мониторинг в новое окружение Dynatrace в кластерах Kubernetes.](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant "Перенесите мониторинг в новое окружение Dynatrace в кластерах Kubernetes.")[### Миграция с OneAgent Operator на Dynatrace Operator',
        'Migrate from deprecated OneAgent Operator to Dynatrace Operator.](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Detailed instructions how to migrate from deprecated OneAgent Operator to Dynatrace Operator using kubectl/oc")[### Migrate from manifests to Helm': 'Перенесите с устаревшего OneAgent Operator на Dynatrace Operator.](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Подробные инструкции по миграции с устаревшего OneAgent Operator на Dynatrace Operator с помощью kubectl/oc")[### Миграция с манифестов на Helm',
        'Migrate from manifests to Helm for Dynatrace Operator installation.](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm "Migrate from manifests to Helm for Dynatrace Operator installation.")[### Migrate DynaKube to newer apiVersion': 'Перенесите с манифестов на Helm для установки Dynatrace Operator.](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm "Перенесите с манифестов на Helm для установки Dynatrace Operator.")[### Миграция DynaKube на новую apiVersion',
        'Migrate from your old `DynaKube` with an older `apiVersion` to the newest supported for a given Dynatrace Operator version.](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.")': 'Перенесите ваш старый `DynaKube` с устаревшей `apiVersion` на новейшую поддерживаемую для данной версии Dynatrace Operator.](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube "Перенесите ваш ресурс DynaKube CR на новые apiVersion в зависимости от используемой версии Operator.")',
    },
    "migrate-dto-to-tenant.md": {
        "title: Migrate Dynatrace Operator to a new environment": "title: Миграция Dynatrace Operator в новое окружение",
        "# Migrate Dynatrace Operator to a new environment": "# Миграция Dynatrace Operator в новое окружение",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "If you're currently monitoring your Kubernetes cluster with a Dynatrace "
        "OneAgent rolled out through the Dynatrace Operator and you need to migrate "
        "to a different Dynatrace environment, select one of the following options, "
        "based on your deployment method.": "Если вы в настоящее время отслеживаете кластер Kubernetes с помощью "
        "Dynatrace OneAgent, развёрнутого через Dynatrace Operator, и вам нужно "
        "выполнить миграцию в другое окружение Dynatrace, выберите один из следующих "
        "вариантов в зависимости от метода развёртывания.",
        "1. Delete the existing DynaKube (starting with Dynatrace Operator version "
        "1.3.0, editing `spec.apiUrl` is not allowed).": "1. Удалите существующий DynaKube (начиная с версии Dynatrace Operator "
        "1.3.0, изменение `spec.apiUrl` не допускается).",
        "2. Delete the existing secret that holds the Dynatrace Operator and Data "
        "Ingest tokens for authenticating to the Dynatrace Cluster.": "2. Удалите существующий секрет, содержащий токены Dynatrace Operator и Data "
        "Ingest для аутентификации в Dynatrace Cluster.",
        "3. Create a new secret based on new tokens from your new environment.": "3. Создайте новый секрет на основе новых токенов из вашего нового окружения.",
        "4. Apply the new DynaKube with the updated `spec.apiUrl`.": "4. Примените новый DynaKube с обновлённым `spec.apiUrl`.",
        "5. Restart your applications.": "5. Перезапустите ваши приложения.",
    },
    "migrate-to-helm.md": {
        "title: Migrate from manifests to Helm for Dynatrace Operator installation": "title: Миграция с манифестов на Helm для установки Dynatrace Operator",
        "# Migrate from manifests to Helm for Dynatrace Operator installation": "# Миграция с манифестов на Helm для установки Dynatrace Operator",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Jul 22, 2024": "* Опубликовано 22 июля 2024 г.",
        "This guide describes the steps required to migrate from using manifests to "
        "Helm. This approach simplifies the deployment process and configuration of "
        "Dynatrace Operator.": "В этом руководстве описаны шаги, необходимые для миграции с использования "
        "манифестов на Helm. Этот подход упрощает процесс развёртывания и настройку "
        "Dynatrace Operator.",
        "For the successful migration, you need to completely uninstall and reinstall "
        "Dynatrace Operator and its components. Proceed with caution as this will "
        "remove and redeploy all components managed by Dynatrace Operator.": "Для успешной миграции необходимо полностью удалить и переустановить "
        "Dynatrace Operator и его компоненты. Действуйте осторожно, так как это "
        "удалит и заново развернёт все компоненты, управляемые Dynatrace Operator.",
        "To ensure a clean migration:": "Чтобы обеспечить чистую миграцию:",
        "1. Remove all deployed Dynatrace custom resources such as EdgeConnect and "
        "DynaKube.": "1. Удалите все развёрнутые пользовательские ресурсы Dynatrace, такие как "
        "EdgeConnect и DynaKube.",
        '2. [Uninstall Dynatrace Operator via manifests](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#manifest-uninstall "Upgrade and uninstallation procedures for Dynatrace Operator").': '2. [Удаление Dynatrace Operator через манифесты](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#manifest-uninstall "Процедуры обновления и удаления Dynatrace Operator").',
        '1. Install Dynatrace Operator via Helm. For more information about install instructions, see [Get started with full observability](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed#helm "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes").': '1. Установите Dynatrace Operator через Helm. Подробнее об инструкциях по установке см. [Начало работы с полной наблюдаемостью](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed#helm "Развёртывание Dynatrace Operator в режиме cloud-native full-stack в Kubernetes").',
        "If you are using Helm version 4.0+, you must use `--rollback-on-failure` "
        "instead of the `--atomic` flag.": "Если вы используете Helm версии 4.0+, необходимо использовать "
        "`--rollback-on-failure` вместо флага `--atomic`.",
        "1. Redeploy Dynatrace custom resources.": "1. Заново разверните пользовательские ресурсы Dynatrace.",
    },
}

# Lines copied verbatim (tab labels / bare product names).
PASS = {
    "migration.md": set(),
    "migrate-dto-to-tenant.md": {
        "Kubernetes",
        "OpenShift",
    },
    "migrate-to-helm.md": set(),
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL.get(fname, SUB + "/migration")
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
