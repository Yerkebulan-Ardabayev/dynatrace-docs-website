# -*- coding: utf-8 -*-
"""L4-IF.62 G4 builder: setup-on-k8s/guides/deployment-and-configuration batch (4 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, no trailing newline, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for bare version-tab labels / footnote markers / identifiers. Any prose line
missing from both raises SystemExit -> catches leftover-EN before writing.

Files:
- deployment-and-configuration.md           (card-grid hub: translate card heading,
                                              description as imperative, title attr; URLs/anchors byte-identical)
- deployment-and-configuration/activegate-pvc.md
- deployment-and-configuration/cluster-role-aggregation.md
- deployment-and-configuration/configure-startup-probes.md

EN sources contain the BOM-as-mojibake `ï»¿` (= UTF-8 bytes of U+FEFF read as
Latin-1) before some `]`; MOJI_RE strips it from both EN line and TRANS keys,
so keys are matched/written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
GUIDES = "ingest-from/setup-on-k8s/guides"
DEPCFG = GUIDES + "/deployment-and-configuration"

# rel dir per file
REL = {
    "deployment-and-configuration.md": GUIDES,
    "activegate-pvc.md": DEPCFG,
    "cluster-role-aggregation.md": DEPCFG,
    "configure-startup-probes.md": DEPCFG,
}

# ----------------------------------------------------------------------------
TRANS = {
    # ---- card-grid hub index page --------------------------------------
    "deployment-and-configuration.md": {
        "title: Deployment and configuration": "title: Развёртывание и настройка",
        "# Deployment and configuration": "# Развёртывание и настройка",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Mar 12, 2026": "* Обновлено 12 марта 2026 г.",
        "Explore a range of operational tasks and procedures related to Dynatrace.": "Изучите ряд эксплуатационных задач и процедур, связанных с Dynatrace.",
        # card 1 (opening heading line)
        "[### Deploy Dynatrace alongside Istio": "[### Развёртывание Dynatrace вместе с Istio",
        # subsequent lines: "<desc>](url \"title\")[### <next heading>"
        "Deployment of Dynatrace Operator alongside Istio in various scenarios.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "
        '"Deployment of Dynatrace Operator alongside Istio in various scenarios")'
        "[### Manage Dynatrace deployments using GitOps": "Развёртывание Dynatrace Operator вместе с Istio в различных сценариях.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "
        '"Развёртывание Dynatrace Operator вместе с Istio в различных сценариях")'
        "[### Управление развёртываниями Dynatrace с помощью GitOps",
        "Learn how to manage Dynatrace Operator and DynaKube using GitOps.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "
        '"How to deploy Dynatrace Operator and DynaKube using GitOps.")'
        "[### Configure node image pull": "Узнайте, как управлять Dynatrace Operator и DynaKube с помощью GitOps.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "
        '"Как развернуть Dynatrace Operator и DynaKube с помощью GitOps.")'
        "[### Настройка загрузки образов на узлах",
        "Configure node image pull with or without CSI driver.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull")'
        "[### Instrument ingress-nginx": "Настройте загрузку образов на узлах с CSI driver или без него.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Настройка загрузки образов на узлах")'
        "[### Инструментирование ingress-nginx",
        "Instrument ingress-nginx on Kubernetes.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx "
        '"Instrument ingress-nginx on Kubernetes")'
        "[### Kubernetes API Monitoring": "Инструментируйте ingress-nginx в Kubernetes.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx "
        '"Инструментирование ingress-nginx в Kubernetes")'
        "[### Мониторинг Kubernetes API",
        "Monitor the Kubernetes API using Dynatrace.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "
        '"Monitor the Kubernetes API using Dynatrace")'
        "[### Configure monitoring for namespaces and pods": "Отслеживайте Kubernetes API с помощью Dynatrace.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "
        '"Мониторинг Kubernetes API с помощью Dynatrace")'
        "[### Настройка мониторинга для пространств имён и подов",
        "Configure monitoring for Dynatrace namespaces and pods.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "
        '"Configure monitoring for namespaces and pods")'
        "[### Dynatrace Operator resource limits": "Настройте мониторинг для пространств имён и подов Dynatrace.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "
        '"Настройка мониторинга для пространств имён и подов")'
        "[### Лимиты ресурсов Dynatrace Operator",
        "Set resource limits for Dynatrace Operator components.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "
        '"Set resource limits for Dynatrace Operator components.")'
        "[### Probe timeouts": "Задайте лимиты ресурсов для компонентов Dynatrace Operator.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "
        '"Задайте лимиты ресурсов для компонентов Dynatrace Operator.")'
        "[### Тайм-ауты проверок работоспособности",
        "Resolve timeout issues in readiness- or liveness-probes caused by OneAgent injection.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/probe-timeout "
        '"Resolve timeout issues in readiness- or liveness-probes caused by OneAgent injection.")'
        "[### Update or uninstall Dynatrace Operator": "Устраните проблемы тайм-аутов в readiness- или liveness-проверках, вызванные внедрением OneAgent.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/probe-timeout "
        '"Устраните проблемы тайм-аутов в readiness- или liveness-проверках, вызванные внедрением OneAgent.")'
        "[### Обновление или удаление Dynatrace Operator",
        "Upgrade and uninstallation procedures for Dynatrace Operator.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")'
        "[### Auto-update for Dynatrace Operator": "Процедуры обновления и удаления Dynatrace Operator.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "
        '"Процедуры обновления и удаления Dynatrace Operator")'
        "[### Автообновление Dynatrace Operator",
        "Enable automatic updates of Dynatrace Operator following a GitOps approach.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "
        '"Enable automatic updates of Dynatrace Operator following a GitOps approach.")'
        "[### Configure auto-update for Dynatrace Operator components": "Включите автоматические обновления Dynatrace Operator, следуя подходу GitOps.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "
        '"Включите автоматические обновления Dynatrace Operator, следуя подходу GitOps.")'
        "[### Настройка автообновления для компонентов Dynatrace Operator",
        "Configure auto-updates for components managed by Dynatrace Operator.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "
        '"Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).")'
        "[### Dynatrace ActiveGate sizing guide": "Настройте автоматические обновления для компонентов, управляемых Dynatrace Operator.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "
        '"Настройте автоматические обновления для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).")'
        "[### Руководство по выбору размера Dynatrace ActiveGate",
        "Sizing guide for Dynatrace ActiveGate components]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "
        '"Set resource limits for Dynatrace ActiveGates")'
        "[### Configure startup probes for Dynatrace Operator": "Руководство по выбору размера для компонентов Dynatrace ActiveGate]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "
        '"Задайте лимиты ресурсов для Dynatrace ActiveGate")'
        "[### Настройка startup-проверок для Dynatrace Operator",
        "Configure startup probes for Dynatrace Operator, Webhook, and CSI Driver.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/configure-startup-probes "
        '"Setup startup probes for components managed by Dynatrace Operator.")': "Настройте startup-проверки для Dynatrace Operator, Webhook и CSI Driver.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/configure-startup-probes "
        '"Настройка startup-проверок для компонентов, управляемых Dynatrace Operator.")',
    },
    # ---- ActiveGate PVC -------------------------------------------------
    "activegate-pvc.md": {
        "title: Configure persistent storage for the ActiveGate": "title: Настройка постоянного хранилища для ActiveGate",
        "# Configure persistent storage for the ActiveGate": "# Настройка постоянного хранилища для ActiveGate",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Feb 04, 2026": "* Обновлено 4 февраля 2026 г.",
        "The [`log_analytics_collector`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "
        '"Learn which ActiveGate properties you can configure based on your needs and requirements.") '
        "ActiveGate module utilizes disk buffers to temporarily store data. To avoid data loss across "
        "ActiveGate restarts, we recommend attaching a "
        "[PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes) (PVC) to the ActiveGate.": "Модуль ActiveGate [`log_analytics_collector`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "
        '"Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.") '
        "использует дисковые буферы для временного хранения данных. Чтобы избежать потери данных при "
        "перезапусках ActiveGate, рекомендуется подключить "
        "[PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes) (PVC) к ActiveGate.",
        "## Adding a PersistentVolumeClaim": "## Добавление PersistentVolumeClaim",
        "The following snippet shows how you can attach the PersistentVolumeClaim to the ActiveGate in the DynaKube.": "В следующем фрагменте показано, как подключить PersistentVolumeClaim к ActiveGate в DynaKube.",
        "Kubernetes environments without a default StorageClass require you to set `storageClassName` field. "
        "Without it, the ActiveGate pod may fail to schedule with the error: "
        "`pod has unbound immediate PersistentVolumeClaims`. This requirement also applies to EEC "
        "(Extensions Execution Controller) deployments.": "В средах Kubernetes без StorageClass по умолчанию необходимо задать поле `storageClassName`. "
        "Без него под ActiveGate может не запланироваться с ошибкой: "
        "`pod has unbound immediate PersistentVolumeClaims`. Это требование также относится к развёртываниям EEC "
        "(Extensions Execution Controller).",
        "Ensure that the `storageClassName` value corresponds to a valid StorageClass in your cluster:": "Убедитесь, что значение `storageClassName` соответствует корректному StorageClass в вашем кластере:",
        "## Adjusting ActiveGate shutdown grace period": "## Изменение льготного периода завершения работы ActiveGate",
        "When the ActiveGate performs a graceful shutdown (for example, in a scale-in scenario), it needs to "
        "flush buffers to avoid data loss. In large environments, this can take longer than the default grace "
        "period of Kubernetes, which is 30s. To avoid this, setting a longer `terminationGracePeriodSeconds` "
        "on the ActiveGate pods can be helpful. You can change it as shown in the following snippet.": "Когда ActiveGate выполняет корректное завершение работы (например, в сценарии уменьшения масштаба), "
        "ему необходимо сбросить буферы, чтобы избежать потери данных. В крупных средах это может занять больше "
        "времени, чем льготный период Kubernetes по умолчанию, который составляет 30 с. Чтобы этого избежать, "
        "может быть полезно задать большее значение `terminationGracePeriodSeconds` для подов ActiveGate. "
        "Изменить его можно так, как показано в следующем фрагменте.",
    },
    # ---- ClusterRole aggregation ---------------------------------------
    "cluster-role-aggregation.md": {
        "title: ClusterRole aggregation for Kubernetes monitoring": "title: Агрегация ClusterRole для мониторинга Kubernetes",
        "# ClusterRole aggregation for Kubernetes monitoring": "# Агрегация ClusterRole для мониторинга Kubernetes",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Dec 09, 2025": "* Обновлено 9 декабря 2025 г.",
        "Dynatrace Operator version 1.8.0": "Dynatrace Operator версия 1.8.0",
        "Starting with Dynatrace Operator version 1.9.0, aggregated ClusterRoles are no longer used. "
        "The Dynatrace Operator deployment now uses standard ClusterRoles exclusively. This page applies "
        "only to Operator version 1.8. For the reasons behind this change, see the "
        "[1.9.0 release notes](/managed/whats-new/dynatrace-operator/dto-fix-1-9-0 "
        '"Release notes for Dynatrace Operator, version 1.9.0").': "Начиная с Dynatrace Operator версии 1.9.0, агрегированные ClusterRole больше не используются. "
        "В развёртывании Dynatrace Operator теперь используются исключительно стандартные ClusterRole. Эта страница "
        "относится только к Operator версии 1.8. Причины этого изменения см. в "
        "[примечаниях к выпуску 1.9.0](/managed/whats-new/dynatrace-operator/dto-fix-1-9-0 "
        '"Примечания к выпуску Dynatrace Operator, версия 1.9.0").',
        "In Dynatrace Operator version 1.8.0, the ActiveGate component uses a service account binding the "
        "`dynatrace-kubernetes-monitoring` ClusterRole. This ClusterRole is an **aggregated role** enabling "
        "simple and flexible configuration of assigned RBAC permissions. [1](#fn-1-1-def)": "В Dynatrace Operator версии 1.8.0 компонент ActiveGate использует ServiceAccount, привязывающий "
        "ClusterRole `dynatrace-kubernetes-monitoring`. Этот ClusterRole является **агрегированной ролью**, "
        "обеспечивающей простую и гибкую настройку назначенных разрешений RBAC. [1](#fn-1-1-def)",
        "ClusterRole aggregation is a Kubernetes RBAC feature that allows you to combine multiple ClusterRoles "
        "into a single aggregated ClusterRole. The aggregating ClusterRole uses label selectors to identify "
        "which other ClusterRoles should be included. For more information, see "
        "[ClusterRole aggregation in Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).": "Агрегация ClusterRole, это функция Kubernetes RBAC, которая позволяет объединять несколько ClusterRole "
        "в один агрегированный ClusterRole. Агрегирующий ClusterRole использует селекторы меток для определения "
        "того, какие другие ClusterRole следует включить. Подробнее см. "
        "[агрегация ClusterRole в документации Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).",
        "## Default permissions": "## Разрешения по умолчанию",
        "By default, the Dynatrace Operator installation creates a `dynatrace-kubernetes-monitoring-default` "
        "ClusterRole that contains the standard set of permissions required for Kubernetes platform monitoring. "
        'This ClusterRole is automatically labeled with `rbac.dynatrace.com/aggregate-to-monitoring: "true"`, '
        "so its permissions are included in the aggregated role.": "По умолчанию при установке Dynatrace Operator создаётся ClusterRole `dynatrace-kubernetes-monitoring-default`, "
        "который содержит стандартный набор разрешений, необходимых для мониторинга платформы Kubernetes. "
        'Этому ClusterRole автоматически присваивается метка `rbac.dynatrace.com/aggregate-to-monitoring: "true"`, '
        "поэтому его разрешения включаются в агрегированную роль.",
        "The default permissions are documented in the [security reference]"
        "(/managed/ingest-from/setup-on-k8s/reference/security#activegate "
        '"This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") '
        "and cover standard monitoring of:": "Разрешения по умолчанию описаны в [справочнике по безопасности]"
        "(/managed/ingest-from/setup-on-k8s/reference/security#activegate "
        '"На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых им разрешений") '
        "и охватывают стандартный мониторинг:",
        "* Pods, deployments, StatefulSets, and other workload resources.": "* Подов, деплойментов, StatefulSet и других ресурсов рабочих нагрузок.",
        "* Services and endpoints.": "* Сервисов и эндпоинтов.",
        "* Nodes and resource metrics.": "* Узлов и метрик ресурсов.",
        "* Events and cluster information.": "* Событий и информации о кластере.",
        "## Extending the ClusterRole with additional permissions": "## Расширение ClusterRole дополнительными разрешениями",
        "To extend the monitoring functionality beyond the default permissions, create additional ClusterRoles "
        'with the aggregation label. Any ClusterRole with the label `rbac.dynatrace.com/aggregate-to-monitoring: "true"` '
        "is automatically aggregated, and its permissions are granted to the ActiveGate service account.": "Чтобы расширить функциональность мониторинга за пределы разрешений по умолчанию, создайте дополнительные ClusterRole "
        'с меткой агрегации. Любой ClusterRole с меткой `rbac.dynatrace.com/aggregate-to-monitoring: "true"` '
        "автоматически агрегируется, и его разрешения предоставляются ServiceAccount ActiveGate.",
        "### Example: Allow monitoring of sensitive data": "### Пример: разрешение мониторинга конфиденциальных данных",
        "To enable monitoring of sensitive Kubernetes objects like Secrets and ConfigMaps, create a new ClusterRole:": "Чтобы включить мониторинг конфиденциальных объектов Kubernetes, таких как Secret и ConfigMap, создайте новый ClusterRole:",
        'The `rbac.dynatrace.com/aggregate-to-monitoring: "true"` label is required for your ClusterRole to be '
        "aggregated. Without this label, the permissions are not granted to the ActiveGate.": 'Метка `rbac.dynatrace.com/aggregate-to-monitoring: "true"` необходима, чтобы ваш ClusterRole был '
        "агрегирован. Без этой метки разрешения не предоставляются ActiveGate.",
        "The permissions are aggregated immediately after applying the ClusterRole and take effect without "
        "requiring a restart of Operator or ActiveGate pods.": "Разрешения агрегируются сразу после применения ClusterRole и вступают в силу без необходимости "
        "перезапуска подов Operator или ActiveGate.",
    },
    # ---- startup probes -------------------------------------------------
    "configure-startup-probes.md": {
        "title: Configure startup probes for Dynatrace Operator components": "title: Настройка startup-проверок для компонентов Dynatrace Operator",
        "# Configure startup probes for Dynatrace Operator components": "# Настройка startup-проверок для компонентов Dynatrace Operator",
        "* How-to guide": "* Практическое руководство",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Mar 12, 2026": "* Опубликовано 12 марта 2026 г.",
        "## Customize startup probes for Dynatrace Operator components": "## Настройка startup-проверок для компонентов Dynatrace Operator",
        "The default startup probe configuration is suitable for most environments, but you can customize the "
        "startup probes for Dynatrace Operator components to better align with your specific environment and "
        "operational requirements. Properly tuning these probes helps ensure that components are fully "
        "initialized and ready to operate before they begin handling requests.": "Конфигурация startup-проверки по умолчанию подходит для большинства окружений, но startup-проверки для "
        "компонентов Dynatrace Operator можно настроить так, чтобы они лучше соответствовали вашему конкретному "
        "окружению и эксплуатационным требованиям. Правильная настройка этих проверок помогает гарантировать, что "
        "компоненты полностью инициализированы и готовы к работе, прежде чем они начнут обрабатывать запросы.",
        "Startup probe customization can easily be done via the Helm `values.yaml` for the Dynatrace Operator, "
        "Webhook, or CSI driver.": "Настройку startup-проверки можно легко выполнить через Helm `values.yaml` для Dynatrace Operator, "
        "Webhook или CSI driver.",
        "* **Dynatrace Operator**": "* **Dynatrace Operator**",
        "* **Webhook**": "* **Webhook**",
        "* **CSI driver**": "* **CSI driver**",
    },
}

# Lines copied verbatim (bare version-tab labels / footnote markers / identifiers).
PASS = {
    "deployment-and-configuration.md": set(),
    "activegate-pvc.md": {
        "v1beta5",
        "v1beta4",
    },
    "cluster-role-aggregation.md": {
        "1",
    },
    "configure-startup-probes.md": set(),
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL[fname]
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
