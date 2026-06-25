# -*- coding: utf-8 -*-
"""L4-IF.62 g2 builder: setup-on-k8s/guides/.../updates-and-maintenance (3 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor/image targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM), no trailing newline.

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for EN component/option/tab labels, bare image/UI lines, separators. Any prose line
missing from both raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain mojibake `ï»¿` (before some `]`) and `â\x80\x93`
(misdecoded en-dash inside "Operator-managed"). MOJI_RE strips both from the EN
line and from TRANS keys, so keys are written clean and RU stays clean.
"""

import os
import re

# ï»¿ , the BOM, and the misdecoded en-dash sequence "â\x80\x93".
MOJI_RE = re.compile("﻿|ï»¿|â\x80\x93")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance"

# all three files live directly in updates-and-maintenance/
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "auto-update-components.md": {
        "title: Configure auto-update for Dynatrace Operator managed components": "title: Настройка автообновления компонентов, управляемых Dynatrace Operator",
        "# Configure auto-update for Dynatrace Operator managed components": "# Настройка автообновления компонентов, управляемых Dynatrace Operator",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 05 сентября 2025 г.",
        "Dynatrace Operator manages the rollout and updates of the following components in Kubernetes:": "Dynatrace Operator управляет развёртыванием и обновлениями следующих компонентов в Kubernetes:",
        "* OneAgent: Configured in the DynaKube": "* OneAgent: настраивается в DynaKube",
        "* ActiveGate: Configured in the DynaKube": "* ActiveGate: настраивается в DynaKube",
        "* EdgeConnect: Configured by the EdgeConnect Custom Resource (CR)": "* EdgeConnect: настраивается пользовательским ресурсом (CR) EdgeConnect",
        "The default settings for OneAgent and ActiveGate automatically roll out updates "
        "as soon as they become available. DynaKube also defaults to update all pods when "
        "updates are detected automatically. Note that updates may take up to 15 minutes "
        "due to Dynatrace Operator checking for updates at 15-minute intervals. If you set "
        "a custom `image` or `version`, it will disable automatic updates.": "Настройки по умолчанию для OneAgent и ActiveGate автоматически развёртывают "
        "обновления, как только они становятся доступны. DynaKube также по умолчанию "
        "обновляет все поды при автоматическом обнаружении обновлений. Обратите внимание, "
        "что обновления могут занимать до 15 минут, так как Dynatrace Operator проверяет "
        "наличие обновлений с интервалом 15 минут. Если задать пользовательское значение "
        "`image` или `version`, автоматические обновления будут отключены.",
        "## Configure OneAgent auto-update": "## Настройка автообновления OneAgent",
        "Set the target version on the Dynatrace Server to a relative version, for example, "
        "`Latest stable version`. Dynatrace Operator will periodically check for updates and "
        "propagate them to the Kubernetes environment. An update of the OneAgent version will "
        "always cause restart of the OneAgent pods.": "Задайте целевую версию на Dynatrace Server в виде относительной версии, например "
        "`Latest stable version`. Dynatrace Operator будет периодически проверять наличие "
        "обновлений и распространять их в окружение Kubernetes. Обновление версии OneAgent "
        "всегда вызывает перезапуск подов OneAgent.",
        "Minimal DynaKube configuration that uses auto-update:": "Минимальная конфигурация DynaKube, использующая автообновление:",
        "Update windows currently do not apply in Kubernetes environments.": "Окна обновления в настоящее время не применяются в окружениях Kubernetes.",
        "If `autoUpdate` is set to `false` in the DynaKube, the OneAgents will not get version "
        "updates based on the target version of the Dynatrace environment after the initial "
        "deployment of the OneAgents.": "Если для `autoUpdate` в DynaKube задано значение `false`, OneAgent не будут получать "
        "обновления версий на основе целевой версии окружения Dynatrace после первоначального "
        "развёртывания OneAgent.",
        "We do not recommend setting `autoUpdate: false` directly. To control OneAgent version "
        "updates, we recommend doing one of the following:": "Не рекомендуется задавать `autoUpdate: false` напрямую. Для управления обновлениями "
        "версий OneAgent рекомендуется сделать одно из следующего:",
        "* Set `autoUpdate: true` and set the target version in the Dynatrace environment's web UI": "* Задать `autoUpdate: true` и указать целевую версию в веб-интерфейсе окружения Dynatrace",
        "* Configure the `image` field in the DynaKube": "* Настроить поле `image` в DynaKube",
        "* Configure the `version` field in the DynaKube": "* Настроить поле `version` в DynaKube",
        "## Configure code module auto-update of monitored applications": "## Настройка автообновления модуля кода отслеживаемых приложений",
        "While new images are downloaded, applications are only updated when restarted. Keep in "
        "mind that autoscaling also injects the most recent CodeModule.": "Хотя новые образы загружаются, приложения обновляются только при перезапуске. Учитывайте, "
        "что автомасштабирование также внедряет самый последний CodeModule.",
        "## Configure ActiveGate auto-update": "## Настройка автообновления ActiveGate",
        "Similar to OneAgent, the ActiveGate update can be configured in the UI, resulting in a "
        "changed ActiveGate image, visible to Dynatrace Operator.": "Как и для OneAgent, обновление ActiveGate можно настроить в интерфейсе, что приводит к "
        "изменению образа ActiveGate, видимого для Dynatrace Operator.",
    },
    "dto-auto-update.md": {
        "title: Auto-update for Dynatrace Operator": "title: Автообновление Dynatrace Operator",
        "# Auto-update for Dynatrace Operator": "# Автообновление Dynatrace Operator",
        "* 2-min read": "* Чтение: 2 мин",
        "* Published Mar 25, 2024": "* Опубликовано 25 марта 2024 г.",
        "Dynatrace Operator manages and auto-updates the components it deploys. To achieve a "
        "similar effect for Dynatrace Operator itself, we recommend using GitOps and open-source "
        "tools.": "Dynatrace Operator управляет развёртываемыми им компонентами и автоматически их "
        "обновляет. Чтобы добиться аналогичного эффекта для самого Dynatrace Operator, "
        "рекомендуется использовать GitOps и инструменты с открытым исходным кодом.",
        "## Recommended setup": "## Рекомендуемая настройка",
        "* Keep the Dynatrace Operator configuration in a Git repository.": "* Храните конфигурацию Dynatrace Operator в репозитории Git.",
        "* Use [ArgoCD](https://dt-url.net/hi037z9) to deploy the configuration from the Git "
        "repository into the Kubernetes environment.": "* Используйте [ArgoCD](https://dt-url.net/hi037z9), чтобы развернуть конфигурацию из "
        "репозитория Git в окружение Kubernetes.",
        "* Implement [Renovate](https://dt-url.net/vn237h6) to automatically update the Git "
        "repository with the latest Dynatrace Operator configurations.": "* Внедрите [Renovate](https://dt-url.net/vn237h6), чтобы автоматически обновлять "
        "репозиторий Git последними конфигурациями Dynatrace Operator.",
        "## Automated update workflow": "## Автоматизированный процесс обновления",
        "The workflow outlined below is a direct result of the recommended setup, ensuring that "
        "Dynatrace Operator is automatically kept up to date in your Kubernetes environment.": "Описанный ниже процесс является прямым результатом рекомендуемой настройки и "
        "обеспечивает автоматическое поддержание Dynatrace Operator в актуальном состоянии в "
        "вашем окружении Kubernetes.",
        "1. ArgoCD deploys the configuration from the Git repository into the Kubernetes environment.": "1. ArgoCD развёртывает конфигурацию из репозитория Git в окружение Kubernetes.",
        "2. Renovate detects a new release of Dynatrace Operator and updates the version in the "
        "Git repository.": "2. Renovate обнаруживает новый выпуск Dynatrace Operator и обновляет версию в "
        "репозитории Git.",
        "3. ArgoCD notices the change in the Git repository and updates Dynatrace Operator in the "
        "Kubernetes environment accordingly.": "3. ArgoCD замечает изменение в репозитории Git и соответственно обновляет Dynatrace "
        "Operator в окружении Kubernetes.",
        "### Deploy with ArgoCD": "### Развёртывание с помощью ArgoCD",
        "[Argo](https://dt-url.net/wt4379d) offers a suite of open-source tools for Kubernetes app "
        "deployment and management. ArgoCD, a continuous delivery tool, is used to keep the "
        "Dynatrace Operator configuration in sync with the Kubernetes cluster.": "[Argo](https://dt-url.net/wt4379d) предлагает набор инструментов с открытым исходным "
        "кодом для развёртывания приложений Kubernetes и управления ими. ArgoCD, инструмент "
        "непрерывной поставки, используется для синхронизации конфигурации Dynatrace Operator с "
        "кластером Kubernetes.",
        "After you set up ArgoCD in your cluster, create an `ApplicationSet` YAML that specifies "
        "the source Helm chart for Dynatrace Operator, the version you want to deploy, and the "
        "target environment for the deployment.": "После настройки ArgoCD в вашем кластере создайте YAML `ApplicationSet`, в котором "
        "указаны исходный Helm chart для Dynatrace Operator, версия, которую вы хотите "
        "развернуть, и целевое окружение для развёртывания.",
        "ArgoCD ApplicationSet example": "Пример ArgoCD ApplicationSet",
        "### Automate updates with Renovate": "### Автоматизация обновлений с помощью Renovate",
        "Renovate automates the updating of dependencies in Git repositories. Integrating Renovate "
        "into your workflow ensures that the Dynatrace Operator version specified in your "
        "`ApplicationSet` is always up to date. Use the [Renovate guide](https://dt-url.net/67637gq) "
        "for instructions on updating ArgoCD configurations.": "Renovate автоматизирует обновление зависимостей в репозиториях Git. Интеграция Renovate "
        "в ваш процесс гарантирует, что версия Dynatrace Operator, указанная в вашем "
        "`ApplicationSet`, всегда актуальна. Используйте [руководство по Renovate]"
        "(https://dt-url.net/67637gq) для инструкций по обновлению конфигураций ArgoCD.",
        "## Related topics": "## Связанные темы",
        "* [Manage Dynatrace deployments using GitOps]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "
        '"How to deploy Dynatrace Operator and DynaKube using GitOps.")': "* [Управление развёртываниями Dynatrace с помощью GitOps]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "
        '"Как развернуть Dynatrace Operator и DynaKube с помощью GitOps.")',
    },
    "update-uninstall-operator.md": {
        "title: Update or uninstall Dynatrace Operator": "title: Обновление или удаление Dynatrace Operator",
        "# Update or uninstall Dynatrace Operator": "# Обновление или удаление Dynatrace Operator",
        "* 9-min read": "* Чтение: 9 мин",
        "* Updated on Jan 02, 2026": "* Обновлено 02 января 2026 г.",
        "This page provides detailed instructions on how to update or uninstall Dynatrace Operator "
        "in Kubernetes and OpenShift environments.": "На этой странице приведены подробные инструкции по обновлению или удалению Dynatrace "
        "Operator в окружениях Kubernetes и OpenShift.",
        "Dynatrace Operator manages the deployment and lifecycle of all Dynatrace components in your "
        "Kubernetes clusters (for example, OneAgent, ActiveGate, and code modules). This includes, "
        "depending on the configuration, automatic updates for these components. Dynatrace Operator "
        "itself needs to be updated either by applying new manifests or by using helm charts.": "Dynatrace Operator управляет развёртыванием и жизненным циклом всех компонентов Dynatrace "
        "в ваших кластерах Kubernetes (например, OneAgent, ActiveGate и модулей кода). В "
        "зависимости от конфигурации это включает автоматические обновления этих компонентов. Сам "
        "Dynatrace Operator необходимо обновлять либо применением новых манифестов, либо с помощью "
        "helm chart.",
        "We recommend using an up-to-date Operator version (at least version n-2) and always using "
        "the latest patch version of that Operator version (for example, 0.10.4 instead of 0.10.0).": "Рекомендуется использовать актуальную версию Operator (не ниже версии n-2) и всегда "
        "использовать последнюю патч-версию этой версии Operator (например, 0.10.4 вместо 0.10.0).",
        "## Update Dynatrace Operator": "## Обновление Dynatrace Operator",
        "To update Dynatrace Operator, select **one of the following options**, depending on your "
        "deployment approach:": "Чтобы обновить Dynatrace Operator, выберите **один из следующих вариантов** в зависимости "
        "от вашего подхода к развёртыванию:",
        '[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")': '[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)": "**Helm**](#helm)",
        "### Manifest": "### Manifest",
        "For `classicFullStack`, `applicationMonitoring`, or `hostMonitoring` without CSI driver "
        "execute the following command.": "Для `classicFullStack`, `applicationMonitoring` или `hostMonitoring` без CSI driver "
        "выполните следующую команду.",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "Starting with Dynatrace Operator version 1.4.0, the `kubernetes-csi.yaml` includes all "
        "Dynatrace Operator components. For more details, see [Dynatrace Operator release notes "
        "version 1.4.0](/managed/whats-new/dynatrace-operator/dto-fix-1-4-0#upgrade-from-dynatrace-operator-version-1-3-0 "
        '"Release notes for Dynatrace Operator, version 1.4.0").': "Начиная с версии Dynatrace Operator 1.4.0, `kubernetes-csi.yaml` включает все компоненты "
        "Dynatrace Operator. Подробнее см. [примечания к выпуску Dynatrace Operator версии 1.4.0]"
        "(/managed/whats-new/dynatrace-operator/dto-fix-1-4-0#upgrade-from-dynatrace-operator-version-1-3-0 "
        '"Примечания к выпуску Dynatrace Operator, версия 1.4.0").',
        "If you're using the CSI driver, use this command instead:": "Если вы используете CSI driver, используйте вместо этого следующую команду:",
        "### Helm": "### Helm",
        "1. Upgrade the Helm chart.": "1. Обновите Helm chart.",
        "The `values.yaml` file may have changed in newer versions. If existing values are no "
        "longer valid, they will be silently ignored as there's no validation for this.": "Файл `values.yaml` мог измениться в более новых версиях. Если существующие значения "
        "больше не действительны, они будут молча проигнорированы, так как проверка для этого "
        "отсутствует.",
        "Upgrade from the OCI registry": "Обновление из реестра OCI",
        "To upgrade to the latest release from the OCI registry, run the following command.": "Чтобы обновиться до последнего выпуска из реестра OCI, выполните следующую команду.",
        "Note that the `helm repo` command does not support OCI registries. You can only use the "
        "`helm pull`, `helm show`, `helm install`, and `helm upgrade` commands with OCI.": "Обратите внимание, что команда `helm repo` не поддерживает реестры OCI. С OCI можно "
        "использовать только команды `helm pull`, `helm show`, `helm install` и `helm upgrade`.",
        "Upgrade from a Dynatrace Operator version < 0.8.0": "Обновление с версии Dynatrace Operator < 0.8.0",
        "### Upgrade from old Dynatrace Operator versions with Helm": "### Обновление со старых версий Dynatrace Operator с помощью Helm",
        "If you use a Dynatrace Operator version earlier than v0.8.0 in a Helm deployment, follow "
        "the steps below to migrate to the latest Dynatrace Operator version with Helm.": "Если вы используете версию Dynatrace Operator ранее v0.8.0 в развёртывании Helm, "
        "выполните приведённые ниже шаги для перехода на последнюю версию Dynatrace Operator с "
        "помощью Helm.",
        "#### Step 1 Upgrade the custom resource definition": "#### Шаг 1 Обновите определение пользовательского ресурса",
        "According to your [configuration of the `values.yaml` file]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml), "
        "select one of the options below.": "В соответствии с вашей [конфигурацией файла `values.yaml`]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) "
        "выберите один из вариантов ниже.",
        "* If `installCRD` is set to `true`, the custom resource definition will be automatically "
        "upgraded and managed by Helm.": "* Если для `installCRD` задано значение `true`, определение пользовательского ресурса "
        "будет автоматически обновлено и управляться Helm.",
        "* If `installCRD` is set to `false`, you need to upgrade the custom resource definition "
        "manually before starting the Helm installation:": "* Если для `installCRD` задано значение `false`, необходимо обновить определение "
        "пользовательского ресурса вручную перед запуском установки Helm:",
        "#### Step 2 Upgrade the Helm chart": "#### Шаг 2 Обновите Helm chart",
        "Delete the CRD section and the secrets from your existing values.yaml file or use and "
        "customize the [`values.yaml` sample from GitHub]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml). "
        "Upgrade the helm chart:": "Удалите раздел CRD и секреты из существующего файла values.yaml либо используйте и "
        "настройте [пример `values.yaml` из GitHub]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml). "
        "Обновите helm chart:",
        "The above changes make your old values unusable, therefore setting the `--reuse-values` "
        "flag isn't possible for migration.": "Указанные выше изменения делают ваши старые значения непригодными, поэтому задать флаг "
        "`--reuse-values` для миграции невозможно.",
        "On certain Dynatrace Operator versions, a failed upgrade can break Helm rollback, "
        "resulting in a non-functional setup. This is due to the DynaKube stored `apiVersions`. "
        "For more information, see [Update or uninstall Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "
        '"Upgrade and uninstallation procedures for Dynatrace Operator").': "На некоторых версиях Dynatrace Operator неудачное обновление может нарушить откат Helm, "
        "что приводит к нерабочей установке. Это связано с хранимыми DynaKube `apiVersions`. "
        "Подробнее см. [Обновление или удаление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "
        '"Процедуры обновления и удаления Dynatrace Operator").',
        "If this error occurs": "Если возникает эта ошибка",
        "1. [Uninstall Dynatrace Operator](#uninstall-dynatrace-operator).": "1. [Удалите Dynatrace Operator](#uninstall-dynatrace-operator).",
        "2. Delete the DynaKube custom resource definition.": "2. Удалите определение пользовательского ресурса DynaKube.",
        "3. [Install the desired Dynatrace Operator version](#update).": "3. [Установите нужную версию Dynatrace Operator](#update).",
        "4. Restart application workloads as needed.": "4. При необходимости перезапустите рабочие нагрузки приложений.",
        "## Update ActiveGate pods": "## Обновление подов ActiveGate",
        "Typically, ActiveGate pods are updated automatically on pod restart whenever there is a "
        "new version available (unless the image already specifies a certain version). However, if "
        "you need to manually restart ActiveGate pods, run the command below.": "Обычно поды ActiveGate обновляются автоматически при перезапуске пода, когда доступна "
        "новая версия (если только образ уже не задаёт определённую версию). Однако если вам "
        "нужно вручную перезапустить поды ActiveGate, выполните приведённую ниже команду.",
        "## Update Access tokens": "## Обновление токенов доступа",
        "If you need to update your Dynatrace access tokens, follow the steps below.": "Если вам нужно обновить токены доступа Dynatrace, выполните приведённые ниже шаги.",
        '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
        "**Find current tokens**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#find-token "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 2]'
        '(https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': "**Найдите текущие токены**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#find-token "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 2]'
        '(https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
        "**Delete your secret**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-old-secret "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 3]'
        '(https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': "**Удалите ваш секрет**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-old-secret "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 3]'
        '(https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
        "**Create new tokens**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-token "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 4]'
        '(https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")': "**Создайте новые токены**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-token "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 4]'
        '(https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")',
        "**Create a new secret with updated tokens**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-secret "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 5]'
        '(https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")': "**Создайте новый секрет с обновлёнными токенами**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-secret "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 5]'
        '(https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")',
        "**Delete the old tokens**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-token "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")': "**Удалите старые токены**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-token "
        '"Процедуры обновления и удаления Dynatrace Operator")',
        "### Step 1 Find current access tokens": "### Шаг 1 Найдите текущие токены доступа",
        "Find and save your currently used tokens.": "Найдите и сохраните используемые в настоящее время токены.",
        "After generating new tokens, you'll need to [delete the old ones](#delete-token).": "После генерации новых токенов вам нужно будет [удалить старые](#delete-token).",
        "### Step 2 Delete your secret": "### Шаг 2 Удалите ваш секрет",
        "To delete the secret, run one of the commands below.": "Чтобы удалить секрет, выполните одну из приведённых ниже команд.",
        "In Kubernetes, used tokens are stored in a secret named `dynakube` by default. If the "
        "DynaKube custom resource has a different name, or the `tokens` field in DynaKube is set, "
        "make sure that the new secret has the same name as defined there.": "В Kubernetes используемые токены по умолчанию хранятся в секрете с именем `dynakube`. "
        "Если пользовательский ресурс DynaKube имеет другое имя или задано поле `tokens` в "
        "DynaKube, убедитесь, что новый секрет имеет то же имя, что определено там.",
        "### Step 3 Create new access tokens": "### Шаг 3 Создайте новые токены доступа",
        "For instructions on how to create the tokens, see [Access tokens and permissions]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "Инструкции по созданию токенов см. в разделе [Токены доступа и разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").',
        "### Step 4 Create a new secret with updated access tokens": "### Шаг 4 Создайте новый секрет с обновлёнными токенами доступа",
        "To create a new secret with the updated tokens, run one of the commands below, making sure "
        "to replace the placeholders with the new tokens.": "Чтобы создать новый секрет с обновлёнными токенами, выполните одну из приведённых ниже "
        "команд, обязательно заменив подстановочные значения новыми токенами.",
        "* For Dynatrace Operator token:": "* Для токена Dynatrace Operator:",
        "* For Dynatrace Operator and Data Ingest token:": "* Для токена Dynatrace Operator и Data Ingest:",
        "Dynatrace Operator picks up the updated secrets in approximately five minutes. Removing "
        "DynaKube and reapplying it forces an instant reconciliation.": "Dynatrace Operator подхватывает обновлённые секреты примерно за пять минут. Удаление "
        "DynaKube и его повторное применение принудительно запускает мгновенную сверку.",
        "### Step 5 Delete the old access token": "### Шаг 5 Удалите старый токен доступа",
        "After the new tokens are in place, delete the old ones.": "После того как новые токены установлены, удалите старые.",
        "1. In Dynatrace, go to **Access Tokens** and look for the [old token](#find-token).": "1. В Dynatrace перейдите в **Access Tokens** и найдите [старый токен](#find-token).",
        "2. Select **Delete**.": "2. Выберите **Delete**.",
        "## Uninstall Dynatrace Operator": "## Удаление Dynatrace Operator",
        "The following guide outlines the recommended steps for a clean uninstallation of Dynatrace "
        "Operator.": "В следующем руководстве описаны рекомендуемые шаги для чистого удаления Dynatrace "
        "Operator.",
        # card line: "Remove Dynatrace Operator-managed components" (mojibake en-dash stripped)
        "**Remove Dynatrace Operatormanaged components**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator-components "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 2 optional]'
        '(https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")': "**Удалите компоненты, управляемые Dynatrace Operator**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator-components "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 2 optional]'
        '(https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")',
        "Optional **Restart your monitored applications**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#restart-apps "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 3]'
        '(https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': "Необязательно **Перезапустите отслеживаемые приложения**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#restart-apps "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 3]'
        '(https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
        "**Remove Dynatrace Operator**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 4 optional]'
        '(https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")': "**Удалите Dynatrace Operator**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator "
        '"Процедуры обновления и удаления Dynatrace Operator")[![Step 4 optional]'
        '(https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")',
        "Optional **Cleanup nodes**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "
        '"Upgrade and uninstallation procedures for Dynatrace Operator")': "Необязательно **Очистите узлы**]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "
        '"Процедуры обновления и удаления Dynatrace Operator")',
        "**Important for CRI-O Runtime users with classicFullStack**": "**Важно для пользователей среды выполнения CRI-O с classicFullStack**",
        "OneAgent version 1.279 and below": "OneAgent версии 1.279 и ниже",
        "If you're using CRI-O as your cluster's container runtime with `classicFullStack`, "
        "complete the steps outlined in [Migrate from classic full-stack to cloud-native full-stack "
        "mode](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "
        '"Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") '
        "as part of the uninstallation process.": "Если вы используете CRI-O в качестве среды выполнения контейнеров вашего кластера с "
        "`classicFullStack`, выполните шаги, описанные в разделе [Миграция из режима classic "
        "full-stack в режим cloud-native full-stack]"
        "(/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "
        '"Перенесите ваше развёртывание Dynatrace из режима classic full-stack в режим '
        'cloud-native full-stack.") в рамках процесса удаления.',
        "### Step 1 Remove Dynatrace Operatormanaged components": "### Шаг 1 Удалите компоненты, управляемые Dynatrace Operator",
        "Delete DynaKube custom resources to allow Dynatrace Operator to fully delete all related "
        "Dynatrace Operatormanaged components from your Kubernetes cluster. Wait for those "
        "components to be removed to make sure the cleanup is completed successfully.": "Удалите пользовательские ресурсы DynaKube, чтобы позволить Dynatrace Operator полностью "
        "удалить все связанные компоненты, управляемые Dynatrace Operator, из вашего кластера "
        "Kubernetes. Дождитесь удаления этих компонентов, чтобы убедиться, что очистка завершена "
        "успешно.",
        "Why is additional cleanup necessary?": "Зачем нужна дополнительная очистка?",
        "Most resources related to a DynaKube are cleaned up automatically through the Kubernetes "
        "ownership system: when you delete a DynaKube, Kubernetes automatically removes all "
        "resources that have an `OwnerReference` pointing to that DynaKube.": "Большинство ресурсов, связанных с DynaKube, очищаются автоматически через систему "
        "владения Kubernetes: когда вы удаляете DynaKube, Kubernetes автоматически удаляет все "
        "ресурсы, имеющие `OwnerReference`, указывающую на этот DynaKube.",
        "However, some resources require additional cleanup steps due to Kubernetes limitations:": "Однако некоторые ресурсы требуют дополнительных шагов очистки из-за ограничений "
        "Kubernetes:",
        "* **CSI driver dependencies**: Applications using the CSI driver must shut down before the "
        "CSI driver can be safely removed. This prevents potential data corruption or mounting issues.": "* **Зависимости CSI driver**: приложения, использующие CSI driver, должны быть "
        "остановлены, прежде чем CSI driver можно будет безопасно удалить. Это предотвращает "
        "возможное повреждение данных или проблемы с монтированием.",
        "* **Cross-namespace resources**: Kubernetes `OwnerReferences` only work within the same "
        "namespace. Because Dynatrace Operator creates resources such as `Secrets` in your "
        "application namespaces, it must clean these up separately.": "* **Межпространственные ресурсы**: `OwnerReferences` в Kubernetes работают только в "
        "пределах одного пространства имён. Поскольку Dynatrace Operator создаёт ресурсы, такие "
        "как `Secrets`, в пространствах имён ваших приложений, он должен очищать их отдельно.",
        "### Step 2 optional Optional **If you used the CSI driver**: Restart your monitored applications": "### Шаг 2 необязательно Необязательно **Если вы использовали CSI driver**: перезапустите отслеживаемые приложения",
        "To ensure that CSI volumes are properly unmounted and disconnected from the CSI driver "
        "before proceeding with the uninstallation, use the following command to identify "
        "applications that use the CSI driver and need to be restarted.": "Чтобы убедиться, что тома CSI правильно отмонтированы и отключены от CSI driver перед "
        "продолжением удаления, используйте следующую команду для определения приложений, которые "
        "используют CSI driver и требуют перезапуска.",
        "The output will show a list of pods in the format `namespace pod` for each application "
        "that uses the CSI driver.": "Вывод покажет список подов в формате `namespace pod` для каждого приложения, которое "
        "использует CSI driver.",
        "### Step 3 Remove Dynatrace Operator": "### Шаг 3 Удалите Dynatrace Operator",
        "After all Dynatrace Operatormanaged components have been successfully removed, you can "
        "safely uninstall Dynatrace Operator.": "После того как все компоненты, управляемые Dynatrace Operator, успешно удалены, можно "
        "безопасно удалить Dynatrace Operator.",
        "1. Delete Dynatrace Operator.": "1. Удалите Dynatrace Operator.",
        "Helm": "Helm",
        "Openshift": "Openshift",
        "* If the CSI driver was **not** installed (you used `kubernetes.yaml` during installation):": "* Если CSI driver **не** был установлен (вы использовали `kubernetes.yaml` при установке):",
        "* If the CSI driver **was** installed (you used `kubernetes-csi.yaml` during installation):": "* Если CSI driver **был** установлен (вы использовали `kubernetes-csi.yaml` при установке):",
        "* If the CSI driver was **not** installed (you used `openshift.yaml` during installation):": "* Если CSI driver **не** был установлен (вы использовали `openshift.yaml` при установке):",
        "* If the CSI driver **was** installed (you used `openshift-csi.yaml` during installation):": "* Если CSI driver **был** установлен (вы использовали `openshift-csi.yaml` при установке):",
        "2. Delete the namespace.": "2. Удалите пространство имён.",
        "### Step 4 optional Clean up nodes": "### Шаг 4 необязательно Очистите узлы",
        "Depending on the monitoring mode, OneAgent and CSI driver data might remain on the node. To "
        "ensure a clean state, use a cleanup script to remove unnecessary data.": "В зависимости от режима мониторинга данные OneAgent и CSI driver могут оставаться на "
        "узле. Чтобы обеспечить чистое состояние, используйте скрипт очистки для удаления "
        "ненужных данных.",
        "The script deploys a DaemonSet that runs a cleanup procedure on all Linux nodes in the "
        "cluster (amd64, arm64, ppc64le, s390x).": "Скрипт развёртывает DaemonSet, который выполняет процедуру очистки на всех узлах Linux в "
        "кластере (amd64, arm64, ppc64le, s390x).",
        "Before running the node cleanup, ensure that no DynaKube is deployed and all monitored "
        "pods have been restarted.": "Перед запуском очистки узлов убедитесь, что ни один DynaKube не развёрнут и все "
        "отслеживаемые поды перезапущены.",
        "1. Download the script.": "1. Загрузите скрипт.",
        "2. Make the script executable.": "2. Сделайте скрипт исполняемым.",
        "3. Run the script.": "3. Запустите скрипт.",
        "By default, the script uses the `dynatrace` namespace. To specify a different namespace, "
        "pass it as an argument:": "По умолчанию скрипт использует пространство имён `dynatrace`. Чтобы указать другое "
        "пространство имён, передайте его в качестве аргумента:",
        "The script performs the following actions:": "Скрипт выполняет следующие действия:",
        "* Executes the OneAgent uninstall script, if present.": "* Выполняет скрипт удаления OneAgent, если он присутствует.",
        "* Removes OneAgent directories (`/var/lib/dynatrace`, `/opt/dynatrace`, `/var/log/dynatrace`).": "* Удаляет каталоги OneAgent (`/var/lib/dynatrace`, `/opt/dynatrace`, `/var/log/dynatrace`).",
        "* Removes the CSI driver data directory.": "* Удаляет каталог данных CSI driver.",
        "* Reports the cleanup status for each node.": "* Сообщает о статусе очистки для каждого узла.",
        "After all cleanup pods complete successfully, the DaemonSet is automatically deleted. If "
        "any cleanup fails, the DaemonSet remains for investigation.": "После успешного завершения всех подов очистки DaemonSet удаляется автоматически. Если "
        "какая-либо очистка завершается неудачей, DaemonSet остаётся для исследования.",
    },
}

# Lines copied verbatim (EN component/option/tab labels, separators, bare filenames).
PASS = {
    "auto-update-components.md": set(),
    "dto-auto-update.md": set(),
    "update-uninstall-operator.md": set(),
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
