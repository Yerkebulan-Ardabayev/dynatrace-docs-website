# -*- coding: utf-8 -*-
"""L4-IF.62 g7-secA builder: setup-on-k8s/guides/networking-security-compliance
security-configurations batch (3 files: hub + enable-app-armor + seccomp).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM), no trailing newline.

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for tab-label identifiers / bare component lines. Any prose line missing from
both raises SystemExit -> catches leftover-EN before writing.

Note on mojibake in EN sources:
- `ï»¿` (U+00EF U+00BB U+00BF, a UTF-8 BOM read as Latin-1) appears before some
  `]` in links.
- `â\x80\x94` (U+00E2 U+0080 U+0094, an em-dash read as Latin-1) appears in some
  prose lines.
MOJI_RE strips BOTH from the EN line and from the TRANS/PASS keys, so keys are
matched clean and RU output never contains mojibake or em-dash.
"""

import os
import re

# Strip BOM-mojibake (ï»¿ / U+FEFF) and em-dash-mojibake (â\x80\x94) before match.
MOJI_RE = re.compile("﻿|ï»¿|â")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/networking-security-compliance"
SUBC = SUB + "/security-configurations"

# Per-file relative dir override (filename key -> rel dir).
REL = {
    "security-configurations.md": SUB,
    "enable-app-armor.md": SUBC,
    "seccomp.md": SUBC,
}

# ----------------------------------------------------------------------------
TRANS = {
    "security-configurations.md": {
        "title: Security configurations": "title: Конфигурации безопасности",
        "# Security configurations": "# Конфигурации безопасности",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "This page provides a comprehensive guide to security in your environment.": "На этой странице приведено полное руководство по безопасности в вашем окружении.",
        '[![AppArmor](https://dt-cdn.net/images/1200px-apparmor-logo-svg-1200-73ca8a312c.png "AppArmor")': '[![AppArmor](https://dt-cdn.net/images/1200px-apparmor-logo-svg-1200-73ca8a312c.png "AppArmor")',
        "### Enable AppArmor": "### Включение AppArmor",
        "Apply AppArmor profiles on Dynatrace components for enhanced security.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "
        '"Apply AppArmor profiles on Dynatrace components for enhanced security.")'
        "[### Seccomp profiles": "Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "
        '"Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")'
        "[### Профили seccomp",
        "Overview of seccomp profile configuration for Dynatrace components.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp "
        '"Overview of seccomp profile configuration for Dynatrace components.")'
        "[### Apply Pod Security Standards": "Обзор настройки профиля seccomp для компонентов Dynatrace.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp "
        '"Обзор настройки профиля seccomp для компонентов Dynatrace.")'
        "[### Применение Pod Security Standards",
        "Configure Pod Security Standards for the Dynatrace namespace.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/pod-security-standards "
        '"Configure Pod Security Standards for the Dynatrace namespace.")'
        "[### Additional OpenShift configurations": "Настройка Pod Security Standards для пространства имён Dynatrace.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/pod-security-standards "
        '"Настройка Pod Security Standards для пространства имён Dynatrace.")'
        "[### Дополнительные конфигурации OpenShift",
        "Configure Dynatrace Operator in OpenShift environments.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "
        '"Configure Dynatrace Operator in OpenShift environments.")'
        "[### Token rotation": "Настройка Dynatrace Operator в окружениях OpenShift.]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "
        '"Настройка Dynatrace Operator в окружениях OpenShift.")'
        "[### Ротация токенов",
        "Token rotation procedure for Dynatrace Operator-managed tokens]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/token-rotation "
        '"This page describes token rotation behavior for Dynatrace environments and explains how to manually rotate communication tokens created and managed by Dynatrace Operator.")': "Процедура ротации токенов, управляемых Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/token-rotation "
        '"На этой странице описано поведение ротации токенов для окружений Dynatrace и объясняется, как вручную выполнять ротацию токенов связи, созданных и управляемых Dynatrace Operator.")',
    },
    "enable-app-armor.md": {
        "title: Enable AppArmor for enhanced security": "title: Включение AppArmor для повышения безопасности",
        "# Enable AppArmor for enhanced security": "# Включение AppArmor для повышения безопасности",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Mar 09, 2026": "* Обновлено 9 марта 2026 г.",
        # NOTE: BOM-mojibake after AppArmor is stripped by MOJI_RE -> key is clean.
        "You can make Dynatrace Operator more secure by enabling [AppArmor](https://dt-url.net/3403y6b).": "Сделать Dynatrace Operator более безопасным можно, включив [AppArmor](https://dt-url.net/3403y6b).",
        "## Enable AppArmor for Dynatrace Operator, Webhook, and CSI driver": "## Включение AppArmor для Dynatrace Operator, Webhook и CSI driver",
        "Depending on whether you deployed Dynatrace Operator using **Helm** or by directly applying **YAML manifests**.": "В зависимости от того, развернули ли вы Dynatrace Operator с помощью **Helm** или путём прямого применения **манифестов YAML**.",
        "Helm": "Helm",
        "Manifest": "Manifest",
        "AppArmor configuration changes in Kubernetes 1.31+": "Изменения настройки AppArmor в Kubernetes 1.31+",
        "Starting with Kubernetes version 1.31, AppArmor profiles are configured using "
        "`securityContext.appArmorProfile` instead of pod annotations. The previous "
        "`operator.apparmor`, `webhook.apparmor`, and `csidriver.apparmor` Helm values "
        "are deprecated. Use the `appArmorProfile` values shown below instead. The "
        "deprecated values are supported until Kubernetes 1.30 and OpenShift 4.17 reach "
        "end of support (July 2027).": "Начиная с версии Kubernetes 1.31 профили AppArmor настраиваются с помощью "
        "`securityContext.appArmorProfile` вместо аннотаций подов. Прежние значения "
        "Helm `operator.apparmor`, `webhook.apparmor` и `csidriver.apparmor` устарели. "
        "Вместо них используйте значения `appArmorProfile`, показанные ниже. Устаревшие "
        "значения поддерживаются, пока Kubernetes 1.30 и OpenShift 4.17 не достигнут "
        "окончания поддержки (июль 2027 г.).",
        "Add the `appArmorProfile` field to `podSecurityContext` in your `values.yaml` "
        "to enable AppArmor for Dynatrace Operator and Webhook:": "Добавьте поле `appArmorProfile` в `podSecurityContext` в вашем `values.yaml`, "
        "чтобы включить AppArmor для Dynatrace Operator и Webhook:",
        "For the **CSI driver**, set `appArmorProfile` on each container's "
        "`securityContext` individually:": "Для **CSI driver** задайте `appArmorProfile` в `securityContext` каждого "
        "контейнера по отдельности:",
        "On Kubernetes version 1.31+, AppArmor profiles are configured using "
        "`securityContext.appArmorProfile` instead of pod annotations.": "В Kubernetes версии 1.31+ профили AppArmor настраиваются с помощью "
        "`securityContext.appArmorProfile` вместо аннотаций подов.",
        "AppArmor pod annotation deprecation": "Прекращение поддержки аннотации подов AppArmor",
        "On Kubernetes version 1.30 and earlier, AppArmor was configured using the "
        "`container.apparmor.security.beta.kubernetes.io/<container-name>: runtime/default` "
        "pod annotation. This approach is deprecated. Instead, use "
        "`securityContext.appArmorProfile`, which is natively supported on Kubernetes "
        "version 1.31+.": "В Kubernetes версии 1.30 и более ранних AppArmor настраивался с помощью "
        "аннотации подов "
        "`container.apparmor.security.beta.kubernetes.io/<container-name>: runtime/default`. "
        "Этот подход устарел. Вместо него используйте "
        "`securityContext.appArmorProfile`, который изначально поддерживается в "
        "Kubernetes версии 1.31+.",
        "* **Dynatrace Operator and Webhook** require updating the `securityContext` in "
        "the deployment YAML:": "* **Dynatrace Operator и Webhook** требуют обновления `securityContext` в "
        "YAML развёртывания:",
        "* **CSI driver** requires setting `appArmorProfile` on each container's "
        "`securityContext` in the DaemonSet:": "* **CSI driver** требует задания `appArmorProfile` в `securityContext` "
        "каждого контейнера в DaemonSet:",
        "## Enable AppArmor for operator-deployed components": "## Включение AppArmor для компонентов, развёрнутых оператором",
        "To enable AppArmor for components that are deployed by the Dynatrace Operator "
        "into monitored clusters, you need to opt in for each component separately.": "Чтобы включить AppArmor для компонентов, которые Dynatrace Operator "
        "развёртывает в отслеживаемые кластеры, необходимо подключить его для каждого "
        "компонента отдельно.",
        "### ActiveGate": "### ActiveGate",
        "On Kubernetes 1.31+, AppArmor is configured via `securityContext`. On older "
        "clusters, an annotation is used instead. The Operator automatically selects the "
        "appropriate method based on the cluster version. To opt in, add the following "
        "annotation to your DynaKube:": "В Kubernetes 1.31+ AppArmor настраивается через `securityContext`. На более "
        "старых кластерах вместо этого используется аннотация. Оператор автоматически "
        "выбирает подходящий метод в зависимости от версии кластера. Чтобы подключить "
        "его, добавьте в ваш DynaKube следующую аннотацию:",
        "### OneAgent": "### OneAgent",
        # NOTE: em-dash-mojibake (â\x80\x94) after `securityContext` is stripped by
        # MOJI_RE -> key is clean ("`securityContext`  no user action").
        "On Kubernetes 1.31+, the Operator automatically applies AppArmor via "
        "`securityContext`  no user action is required. On Kubernetes 1.30 and earlier, "
        "AppArmor for OneAgent is not automatically applied. To use a custom AppArmor "
        "profile on older clusters, see [Enable a custom AppArmor profile for OneAgent]"
        "(#custom-apparmor).": "В Kubernetes 1.31+ оператор автоматически применяет AppArmor через "
        "`securityContext`, действий со стороны пользователя не требуется. В Kubernetes "
        "1.30 и более ранних AppArmor для OneAgent не применяется автоматически. Чтобы "
        "использовать пользовательский профиль AppArmor на более старых кластерах, см. "
        "[Включение пользовательского профиля AppArmor для OneAgent](#custom-apparmor).",
        "### EdgeConnect": "### EdgeConnect",
        "To enable AppArmor for EdgeConnect, add the AppArmor annotation via the DynaKube "
        "`spec.edgeConnect.annotations` field:": "Чтобы включить AppArmor для EdgeConnect, добавьте аннотацию AppArmor через "
        "поле DynaKube `spec.edgeConnect.annotations`:",
        "The `container.apparmor.security.beta.kubernetes.io` annotation was deprecated "
        "in Kubernetes 1.30 and removed in Kubernetes 1.31. On Kubernetes 1.31+, the "
        "annotation has no effect for EdgeConnect. `securityContext`-based AppArmor "
        "configuration for EdgeConnect is not yet supported.": "Аннотация `container.apparmor.security.beta.kubernetes.io` устарела в "
        "Kubernetes 1.30 и удалена в Kubernetes 1.31. В Kubernetes 1.31+ эта аннотация "
        "не действует для EdgeConnect. Настройка AppArmor для EdgeConnect на основе "
        "`securityContext` пока не поддерживается.",
        "### Enable a custom AppArmor profile for OneAgent": "### Включение пользовательского профиля AppArmor для OneAgent",
        "You can restrict the OneAgent access to a desired set of features. See below "
        "for how to enable a custom AppArmor profile and apply it to the OneAgent pods.": "Доступ OneAgent можно ограничить нужным набором функций. Ниже описано, как "
        "включить пользовательский профиль AppArmor и применить его к подам OneAgent.",
        '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
        "**Create a custom OneAgent AppArmor profile**]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#create-profile "
        '"Apply AppArmor profiles on Dynatrace components for enhanced security.")'
        '[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': "**Создание пользовательского профиля AppArmor для OneAgent**]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#create-profile "
        '"Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")'
        '[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
        "**Install the profile on all worker nodes**]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#install-profile "
        '"Apply AppArmor profiles on Dynatrace components for enhanced security.")'
        '[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': "**Установка профиля на все рабочие узлы**]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#install-profile "
        '"Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")'
        '[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
        "**Enforce the profile on all OneAgent pods**]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#enforce-profile "
        '"Apply AppArmor profiles on Dynatrace components for enhanced security.")': "**Принудительное применение профиля ко всем подам OneAgent**]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#enforce-profile "
        '"Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")',
        "#### Step 1 Create a custom OneAgent AppArmor profile": "#### Шаг 1. Создание пользовательского профиля AppArmor для OneAgent",
        "See [Run OneAgent as a Docker container]"
        "(/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#with-apparmor "
        '"Install and update Dynatrace OneAgent as a Docker container.") for details on '
        "how to create a custom AppArmor profile.": "Подробнее о том, как создать пользовательский профиль AppArmor, см. [Запуск "
        "OneAgent как контейнера Docker]"
        "(/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#with-apparmor "
        '"Установка и обновление Dynatrace OneAgent как контейнера Docker.").',
        "#### Step 2 Install the profile on all worker nodes": "#### Шаг 2. Установка профиля на все рабочие узлы",
        "OneAgent is deployed as a daemonset by default, which means pods that use the "
        "AppArmor profile will be used on every node. You therefore need to install the "
        "OneAgent AppArmor profile **on all nodes**.": "OneAgent по умолчанию развёртывается как daemonset, что означает, что поды, "
        "использующие профиль AppArmor, будут задействованы на каждом узле. Поэтому "
        "профиль AppArmor для OneAgent необходимо установить **на всех узлах**.",
        # NOTE: two BOM-mojibake occurrences in this line are stripped by MOJI_RE.
        "Depending on the environment, this can be done in several ways, such as by "
        "using the [kube-apparmor-manager](https://dt-url.net/5g034s7) or the "
        "[security-profiles-operator](https://dt-url.net/uz23475). Please refer to the "
        "official documentation of these tools on how to apply them in your cluster.": "В зависимости от окружения это можно сделать несколькими способами, например "
        "с помощью [kube-apparmor-manager](https://dt-url.net/5g034s7) или "
        "[security-profiles-operator](https://dt-url.net/uz23475). О том, как "
        "применять эти инструменты в вашем кластере, см. их официальную документацию.",
        "#### Step 3 Enforce the profile on all OneAgent pods": "#### Шаг 3. Принудительное применение профиля ко всем подам OneAgent",
        "To enable AppArmor for all the OneAgent pods, add the "
        "`container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent: localhost/oneagent` "
        "annotation to one of the following fields, depending on your deployment:": "Чтобы включить AppArmor для всех подов OneAgent, добавьте аннотацию "
        "`container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent: localhost/oneagent` "
        "в одно из следующих полей в зависимости от вашего развёртывания:",
        "* `oneAgent.classicFullStack.annotations`": "* `oneAgent.classicFullStack.annotations`",
        "* `oneAgent.cloudNativeFullStack.annotations`": "* `oneAgent.cloudNativeFullStack.annotations`",
        "* `oneAgent.hostMonitoring.annotations`": "* `oneAgent.hostMonitoring.annotations`",
        "Example for `cloudNativeFullStack` deployment:": "Пример для развёртывания `cloudNativeFullStack`:",
    },
    "seccomp.md": {
        "title: Seccomp profiles": "title: Профили seccomp",
        "# Seccomp profiles": "# Профили seccomp",
        "* Explanation": "* Пояснение",
        "* 5-min read": "* Чтение: 5 мин",
        "* Published Mar 24, 2026": "* Опубликовано 24 марта 2026 г.",
        "## What is seccomp?": "## Что такое seccomp?",
        "Seccomp (secure computing mode) is a Linux kernel security feature that "
        "restricts the system calls a process is allowed to make. By applying a seccomp "
        "profile to a container, you limit which kernel-level operations it can perform, "
        "reducing the attack surface of your workloads. Kubernetes supports configuring "
        "seccomp profiles at both the pod and container level through the "
        "`securityContext` field, making it a key mechanism for meeting security "
        "standards such as the Kubernetes [Pod Security Standards]"
        "(https://kubernetes.io/docs/concepts/security/pod-security-standards/).": "Seccomp (secure computing mode), это функция безопасности ядра Linux, "
        "которая ограничивает системные вызовы, которые разрешено выполнять процессу. "
        "Применяя профиль seccomp к контейнеру, вы ограничиваете, какие операции на "
        "уровне ядра он может выполнять, уменьшая поверхность атаки ваших рабочих "
        "нагрузок. Kubernetes поддерживает настройку профилей seccomp как на уровне "
        "пода, так и на уровне контейнера через поле `securityContext`, что делает её "
        "ключевым механизмом для соответствия стандартам безопасности, таким как "
        "Kubernetes [Pod Security Standards]"
        "(https://kubernetes.io/docs/concepts/security/pod-security-standards/).",
        "There are three seccomp profile types in Kubernetes:": "В Kubernetes есть три типа профилей seccomp:",
        # NOTE: em-dash-mojibake after **RuntimeDefault** stripped by MOJI_RE.
        "* **RuntimeDefault**The container runtime's built-in default profile. It "
        "permits a curated set of common system calls while blocking potentially "
        "dangerous ones.": "* **RuntimeDefault**: встроенный профиль по умолчанию среды выполнения "
        "контейнеров. Он разрешает выверенный набор распространённых системных "
        "вызовов, блокируя потенциально опасные.",
        "* **Localhost**A custom profile loaded from a JSON file on the node's "
        "filesystem.": "* **Localhost**: пользовательский профиль, загружаемый из JSON-файла в "
        "файловой системе узла.",
        "* **Unconfined**No seccomp filtering is applied; all system calls are allowed.": "* **Unconfined**: фильтрация seccomp не применяется, разрешены все системные "
        "вызовы.",
        "All Dynatrace Operator infrastructure components (operator, webhook, and CSI "
        "driver) and operator-deployed components (ActiveGate, EdgeConnect) use the "
        "`RuntimeDefault` seccomp profile. The exception is OneAgent, which is "
        "unconfined (no seccomp profile set). The `RuntimeDefault` profile is suitable "
        "for most workloads and satisfies the **restricted** Pod Security Standard.": "Все инфраструктурные компоненты Dynatrace Operator (operator, webhook и CSI "
        "driver) и компоненты, развёртываемые оператором (ActiveGate, EdgeConnect), "
        "используют профиль seccomp `RuntimeDefault`. Исключением является OneAgent, "
        "который работает без ограничений (профиль seccomp не задан). Профиль "
        "`RuntimeDefault` подходит для большинства рабочих нагрузок и удовлетворяет "
        "стандарту **restricted** Pod Security Standard.",
        "## OneAgent seccomp profile": "## Профиль seccomp для OneAgent",
        "The OneAgent runs without a seccomp profile (unconfined) by default. This "
        "default was chosen to ensure compatibility with the widest range of platforms "
        "and container runtimes, as the OneAgent requires access to a broader set of "
        "system calls for deep host-level monitoring.": "По умолчанию OneAgent работает без профиля seccomp (unconfined). Это значение "
        "по умолчанию было выбрано для обеспечения совместимости с самым широким "
        "набором платформ и сред выполнения контейнеров, поскольку OneAgent требует "
        "доступа к более широкому набору системных вызовов для глубокого мониторинга "
        "на уровне хоста.",
        "### Configure a custom seccomp profile for OneAgent": "### Настройка пользовательского профиля seccomp для OneAgent",
        "Dynatrace Operator version 1.2.0+": "Dynatrace Operator версии 1.2.0+",
        "If your security policies require a seccomp profile on the OneAgent, you can "
        "configure one using the `secCompProfile` field under the appropriate OneAgent "
        "mode in your DynaKube custom resource.": "Если ваши политики безопасности требуют профиля seccomp для OneAgent, его "
        "можно настроить с помощью поля `secCompProfile` под соответствующим режимом "
        "OneAgent в вашем пользовательском ресурсе DynaKube.",
        # NOTE: em-dash-mojibake after `node` stripped by MOJI_RE.
        "**Limitation:** The OneAgent seccomp profile is always applied with the type "
        "`Localhost`. This means you must provide a custom seccomp profile JSON file on "
        "each nodeyou cannot set the type to `RuntimeDefault` or `Unconfined` through "
        "this field.": "**Ограничение:** профиль seccomp для OneAgent всегда применяется с типом "
        "`Localhost`. Это означает, что необходимо предоставить пользовательский "
        "JSON-файл профиля seccomp на каждом узле: задать тип `RuntimeDefault` или "
        "`Unconfined` через это поле нельзя.",
        "Cloud-native full stack": "Cloud-native full stack",
        "Classic full stack": "Classic full stack",
        "Host monitoring": "Host monitoring",
        "The `Localhost` type requires that the seccomp profile JSON file is present on "
        "the node's local filesystem, under the kubelet's configured seccomp profile "
        "root directory (by default `/var/lib/kubelet/seccomp/`). For the examples "
        "above, the profile file would need to be located at "
        "`/var/lib/kubelet/seccomp/my-seccomp-profile.json` on every node where the "
        "OneAgent is scheduled.": "Тип `Localhost` требует, чтобы JSON-файл профиля seccomp присутствовал в "
        "локальной файловой системе узла, в настроенном корневом каталоге профилей "
        "seccomp kubelet (по умолчанию `/var/lib/kubelet/seccomp/`). Для приведённых "
        "выше примеров файл профиля должен располагаться по пути "
        "`/var/lib/kubelet/seccomp/my-seccomp-profile.json` на каждом узле, где "
        "запланирован OneAgent.",
        "To learn how to create and manage `Localhost` seccomp profiles, refer to the "
        "Kubernetes documentation:": "О том, как создавать профили seccomp типа `Localhost` и управлять ими, см. "
        "документацию Kubernetes:",
        "* [Restrict a Container's Syscalls with seccomp]"
        "(https://kubernetes.io/docs/tutorials/security/seccomp/)": "* [Restrict a Container's Syscalls with seccomp]"
        "(https://kubernetes.io/docs/tutorials/security/seccomp/)",
        "* [Set the seccomp profile for a Container]"
        "(https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-seccomp-profile-for-a-container)": "* [Set the seccomp profile for a Container]"
        "(https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-seccomp-profile-for-a-container)",
        "## Configure seccomp for the Dynatrace init container": "## Настройка seccomp для init-контейнера Dynatrace",
        "Dynatrace Operator version 0.11.2+": "Dynatrace Operator версии 0.11.2+",
        "The seccomp profile for the Dynatrace init container (used for code module "
        "injection) is controlled by the "
        "`feature.dynatrace.com/init-container-seccomp-profile` feature flag.": "Профиль seccomp для init-контейнера Dynatrace (используемого для инъекции "
        "модуля кода) управляется флагом функции "
        "`feature.dynatrace.com/init-container-seccomp-profile`.",
        "Starting with Dynatrace Operator version 1.9.0, the default value of this "
        'feature flag changed from `"false"` to `"true"`. This means the init '
        "container now has the `RuntimeDefault` seccomp profile applied by default, "
        "helping meet the requirements of the **restricted** Pod Security Standard for "
        "your monitored Kubernetes workloads.": "Начиная с версии Dynatrace Operator 1.9.0 значение этого флага функции по "
        'умолчанию изменилось с `"false"` на `"true"`. Это означает, что к '
        "init-контейнеру теперь по умолчанию применяется профиль seccomp "
        "`RuntimeDefault`, что помогает выполнить требования стандарта **restricted** "
        "Pod Security Standard для ваших отслеживаемых рабочих нагрузок Kubernetes.",
        "If you are running Dynatrace Operator version 0.11.2 through 1.8.x, you must "
        "explicitly enable this feature flag to apply the `RuntimeDefault` profile:": "Если вы используете Dynatrace Operator версий с 0.11.2 по 1.8.x, для "
        "применения профиля `RuntimeDefault` необходимо явно включить этот флаг "
        "функции:",
        "To disable the seccomp profile on the init container (on any version), set the "
        'feature flag to `"false"`:': "Чтобы отключить профиль seccomp для init-контейнера (в любой версии), задайте "
        'для флага функции значение `"false"`:',
        'When set to `"false"`, the init container will not have a seccomp profile '
        "set, and the default behavior of your container runtime will be used instead.": 'При значении `"false"` для init-контейнера профиль seccomp не будет задан, '
        "и вместо этого будет использоваться поведение по умолчанию вашей среды "
        "выполнения контейнеров.",
    },
}

# Lines copied verbatim (none needed for this batch beyond TRANS identity keys).
PASS = {
    "security-configurations.md": set(),
    "enable-app-armor.md": set(),
    "seccomp.md": set(),
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
