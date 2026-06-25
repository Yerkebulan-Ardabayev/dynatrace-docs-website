# -*- coding: utf-8 -*-
"""L4-IF.62 g5b builder: setup-on-k8s/guides/deployment-and-configuration (2 files).

GitOps / node-image-pull batch. Same prose line-parity engine as
_build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for identifier-only lines / bare footnote markers / EN component lines. Any prose
line missing from both raises SystemExit -> catches leftover-EN before writing.

EN sources contain mojibake `ï»¿` before some `]`; MOJI_RE strips it from both EN
line and TRANS keys, so keys are written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/deployment-and-configuration"

# both files live directly in deployment-and-configuration/
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "using-gitops.md": {
        "title: Manage Dynatrace deployments using GitOps": "title: Управление развёртываниями Dynatrace с помощью GitOps",
        "# Manage Dynatrace deployments using GitOps": "# Управление развёртываниями Dynatrace с помощью GitOps",
        "* 4-min read": "* Чтение: 4 мин",
        "* Published Mar 25, 2024": "* Опубликовано 25 марта 2024 г.",
        "With many companies today adopting GitOps for streamlined Kubernetes "
        "deployments, there's a growing interest in applying these practices to "
        "Dynatrace components. This guide focuses on deploying Dynatrace Operator with "
        "GitOps tools and setting up monitoring efficiently using the DynaKube custom "
        "resource (CR), aligning with modern deployment strategies.": "Поскольку сегодня многие компании внедряют GitOps для упрощённых "
        "развёртываний Kubernetes, растёт интерес к применению этих практик к "
        "компонентам Dynatrace. Это руководство посвящено развёртыванию Dynatrace "
        "Operator с помощью инструментов GitOps и эффективной настройке мониторинга "
        "с использованием пользовательского ресурса (CR) DynaKube, в соответствии с "
        "современными стратегиями развёртывания.",
        "## Using ArgoCD": "## Использование ArgoCD",
        "This section discusses deploying Dynatrace Operator and applying a DynaKube CR "
        "using [ArgoCD](https://dt-url.net/hi037z9). Additionally, it outlines options "
        "and tips for flexible integration with ArgoCD.": "В этом разделе рассматривается развёртывание Dynatrace Operator и применение "
        "CR DynaKube с помощью [ArgoCD](https://dt-url.net/hi037z9). Кроме того, в нём "
        "описаны варианты и советы по гибкой интеграции с ArgoCD.",
        "The following three points describe Dynatrace deployment options outlined by "
        "the subsections and combinations of them.": "Следующие три пункта описывают варианты развёртывания Dynatrace, изложенные "
        "в подразделах, и их комбинации.",
        "1. Individually [Deploy Dynatrace Operator](#deploy-dynatrace-operator) and "
        "[Apply DynaKube CR](#apply-dynakube-custom-resource) via ArgoCD Applications": "1. По отдельности [разверните Dynatrace Operator]"
        "(#deploy-dynatrace-operator) и [примените CR DynaKube]"
        "(#apply-dynakube-custom-resource) через ArgoCD Applications",
        "2. Apply ArgoCD's [App of Apps pattern](#applying-the-app-of-apps-pattern)": "2. Примените [паттерн App of Apps](#applying-the-app-of-apps-pattern) ArgoCD",
        "3. Use [multiple sources]"
        "(#using-multiple-sources-for-an-argocd-application-beta-feature) for an "
        "ArgoCD Application (beta feature)": "3. Используйте [несколько источников]"
        "(#using-multiple-sources-for-an-argocd-application-beta-feature) для ArgoCD "
        "Application (бета-функция)",
        "This guide was developed and tested with ArgoCD version 2.10.3.": "Это руководство было разработано и протестировано с ArgoCD версии 2.10.3.",
        "### Deploy Dynatrace Operator": "### Развёртывание Dynatrace Operator",
        "The following ArgoCD Application defines Dynatrace Operator deployment using "
        "the OCI-based Helm chart from Amazon ECR:": "Следующее ArgoCD Application определяет развёртывание Dynatrace Operator с "
        "использованием Helm-чарта на основе OCI из Amazon ECR:",
        "For deployment customization via Helm values, please refer to ArgoCD's [Helm "
        "user guide](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/).": "Для настройки развёртывания через значения Helm обратитесь к [руководству "
        "пользователя по Helm](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/) "
        "ArgoCD.",
        "The Application CR can be applied in the following ways:": "CR Application можно применить следующими способами:",
        "* Directly via *kubectl*": "* Напрямую через *kubectl*",
        "* By [applying the App of Apps pattern](#applying-the-app-of-apps-pattern)": "* Путём [применения паттерна App of Apps](#applying-the-app-of-apps-pattern)",
        "#### Multi-cluster deployments via ArgoCD ApplicationSet": "#### Развёртывания в нескольких кластерах через ArgoCD ApplicationSet",
        "To use ApplicationSet CRs for multi-cluster deployments, use the Application "
        "CR from above as a template and integrate it into an ApplicationSet CR "
        "according to [ArgoCD's official documentation]"
        "(https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource).": "Чтобы использовать CR ApplicationSet для развёртываний в нескольких "
        "кластерах, используйте приведённый выше CR Application в качестве шаблона и "
        "интегрируйте его в CR ApplicationSet в соответствии с [официальной "
        "документацией ArgoCD]"
        "(https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource).",
        "### Apply DynaKube custom resource": "### Применение пользовательского ресурса DynaKube",
        "The following ArgoCD Application references a Git repository holding a "
        "DynaKube CR under the specified filepath:": "Следующее ArgoCD Application ссылается на репозиторий Git, содержащий CR "
        "DynaKube по указанному пути к файлу:",
        "Replace the `repoURL`, `targetRevision`, and `path` source fields with "
        "meaningful values before applying the Application CR in either of these ways:": "Замените поля источника `repoURL`, `targetRevision` и `path` осмысленными "
        "значениями, прежде чем применять CR Application одним из следующих способов:",
        "For details on DynaKube CR configuration, see the [deployment modes]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Deploy Dynatrace Operator on Kubernetes") documentation.': "Подробнее о настройке CR DynaKube см. документацию по [режимам "
        "развёртывания](/managed/ingest-from/setup-on-k8s/deployment "
        '"Развёртывание Dynatrace Operator в Kubernetes").',
        "### Apply the App of Apps pattern": "### Применение паттерна App of Apps",
        "ArgoCD's [App Of Apps pattern](https://dt-url.net/s963lbz) describes a very "
        "common approach in the ArgoCD community enabling automatic cluster "
        "bootstrapping. In combination with [Sync Phases and Waves]"
        "(https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/), the App of "
        "Apps pattern provides sequential control over Application synchronization "
        "required for deploying Dynatrace Operator before applying a DynaKube CR "
        "[1](#fn-1-1-def).": "[Паттерн App Of Apps](https://dt-url.net/s963lbz) ArgoCD описывает очень "
        "распространённый в сообществе ArgoCD подход, обеспечивающий автоматическую "
        "начальную настройку кластера. В сочетании с [фазами и волнами синхронизации]"
        "(https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) паттерн App "
        "of Apps обеспечивает последовательный контроль над синхронизацией "
        "Application, необходимый для развёртывания Dynatrace Operator перед "
        "применением CR DynaKube [1](#fn-1-1-def).",
        "Add the `argocd.argoproj.io/sync-wave` annotation with the respective value "
        "to the Application CRs from the above sections as illustrated in the "
        "following snippet:": "Добавьте аннотацию `argocd.argoproj.io/sync-wave` с соответствующим "
        "значением к CR Application из приведённых выше разделов, как показано в "
        "следующем фрагменте:",
        "Both Application CRs are meant to be applied via the App of Apps pattern "
        "(which requires a parent Application CR).": "Оба CR Application предназначены для применения через паттерн App of Apps "
        "(который требует родительского CR Application).",
        "[Creating Custom Resource Definitions (CRDs)](https://dt-url.net/8g23lou) "
        "installed via the Helm chart can take several seconds, leading to the "
        "possibility that the initial application of the DynaKube CR will fail. To "
        "circumvent the given race condition, we recommend [configuring ArgoCD for the "
        "use of App of Apps](https://dt-url.net/ci03l8w) by changing the health "
        "assessment logic for Applications. Alternatively, automatic retries of "
        "synchronizations can be configured.": "[Создание определений пользовательских ресурсов (CRD)]"
        "(https://dt-url.net/8g23lou), устанавливаемых через Helm-чарт, может занять "
        "несколько секунд, из-за чего первоначальное применение CR DynaKube может "
        "завершиться неудачей. Чтобы обойти данное состояние гонки, мы рекомендуем "
        "[настроить ArgoCD для использования App of Apps](https://dt-url.net/ci03l8w), "
        "изменив логику оценки работоспособности для Application. В качестве "
        "альтернативы можно настроить автоматические повторные попытки синхронизации.",
        "### Use multiple sources for an ArgoCD Application (beta feature)": "### Использование нескольких источников для ArgoCD Application (бета-функция)",
        "Multiple sources for an Application is an ArgoCD beta feature and is subject "
        "to change in backwards-incompatible ways, according ArgoCD documentation.": "Несколько источников для Application являются бета-функцией ArgoCD и, согласно "
        "документации ArgoCD, могут изменяться обратно несовместимым образом.",
        "[Multiple sources for an Application]"
        "(https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/) "
        "enables you to use a single ArgoCD Application for deployment of Dynatrace "
        "Operator and DynaKube CR.": "[Несколько источников для Application]"
        "(https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/) "
        "позволяют использовать одно ArgoCD Application для развёртывания Dynatrace "
        "Operator и CR DynaKube.",
        "Additionally, the feature allows Helm value files to be sources from a Git "
        "repository other than the Helm chart itself, which was not possible in ArgoCD "
        "before.": "Кроме того, эта функция позволяет брать файлы значений Helm из репозитория "
        "Git, отличного от самого Helm-чарта, что ранее было невозможно в ArgoCD.",
        "Before applying, replace all placeholders with meaningful values and "
        "configure automatic retries[2](#fn-2-2-def).": "Перед применением замените все заполнители осмысленными значениями и настройте "
        "автоматические повторные попытки[2](#fn-2-2-def).",
        "[Creating Custom Resource Definitions (CRDs)](https://dt-url.net/id43ley) "
        "installed via the Helm chart can take several seconds, leading to the "
        "possibility of the initial application of the DynaKube resource failing. To "
        "ensure successful deployment, you need to configure retries by specifying a "
        "sync policy.": "[Создание определений пользовательских ресурсов (CRD)]"
        "(https://dt-url.net/id43ley), устанавливаемых через Helm-чарт, может занять "
        "несколько секунд, из-за чего первоначальное применение ресурса DynaKube может "
        "завершиться неудачей. Чтобы обеспечить успешное развёртывание, необходимо "
        "настроить повторные попытки, указав политику синхронизации.",
        "## Auto-update for Dynatrace Operator": "## Автоматическое обновление Dynatrace Operator",
        "For configuring automatic updates for Dynatrace Operator, see [Auto-update of "
        "Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "
        '"Enable automatic updates of Dynatrace Operator following a GitOps '
        'approach."), which explains integrating GitOps with dependency automation '
        "tools.": "О настройке автоматических обновлений Dynatrace Operator см. "
        "[Автоматическое обновление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "
        '"Включение автоматических обновлений Dynatrace Operator по подходу '
        'GitOps."), где описана интеграция GitOps с инструментами автоматизации '
        "зависимостей.",
        "## Related topics": "## Связанные темы",
        "* [Auto-update for Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "
        '"Enable automatic updates of Dynatrace Operator following a GitOps '
        'approach.")': "* [Автоматическое обновление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "
        '"Включение автоматических обновлений Dynatrace Operator по подходу '
        'GitOps.")',
    },
    "node-image-pull.md": {
        "title: Configure node image pull": "title: Настройка загрузки образов на узле",
        "# Configure node image pull": "# Настройка загрузки образов на узле",
        "* 6-min read": "* Чтение: 6 мин",
        "* Updated on Jan 27, 2026": "* Обновлено 27 января 2026 г.",
        "Dynatrace Operator version 1.5": "Dynatrace Operator версии 1.5",
        "The node image pull feature introduces new capabilities for image pulling of "
        "the Dynatrace code modules image, along with enhanced performance and "
        "security in the Dynatrace Operator. These enhancements enable the following "
        "improvements and use-cases:": "Функция загрузки образов на узле добавляет новые возможности для загрузки "
        "образа Dynatrace code modules, а также повышает производительность и "
        "безопасность в Dynatrace Operator. Эти улучшения обеспечивают следующие "
        "преимущества и сценарии использования:",
        "* Cloud-native full-stack monitoring works independently of the CSI driver "
        "[1](#fn-1-1-def)": "* Мониторинг Cloud-Native Full-Stack работает независимо от CSI driver "
        "[1](#fn-1-1-def)",
        "+ Cloud-native full-stack monitoring can be deployed via OpenShift "
        "OperatorHub": "+ Мониторинг Cloud-Native Full-Stack можно развернуть через OpenShift "
        "OperatorHub",
        "* Application monitoring works in combination with the public signed images": "* Мониторинг Application работает в сочетании с публичными подписанными "
        "образами",
        "* Combination of non-CSI and CSI-based Dynatrace code module injection (for "
        "details, see [Enforce CSI-less application monitoring](#mixed-mode)) "
        "[1](#fn-1-1-def)": "* Сочетание внедрения Dynatrace code module без CSI и на основе CSI "
        "(подробнее см. [Принудительный мониторинг Application без CSI](#mixed-mode)) "
        "[1](#fn-1-1-def)",
        "+ for mixed setups with/without node access like AWS Elastic Kubernetes "
        "Service with EC2 nodes and Fargate": "+ для смешанных конфигураций с доступом к узлам и без него, например AWS "
        "Elastic Kubernetes Service с узлами EC2 и Fargate",
        "+ for leveraging the benefits of the CSI driver, with specific exceptions for "
        "[NGINX instrumentation]"
        "(/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "
        '"Learn how to force instrumenting patched/non-standard NGINX binaries during '
        'runtime.")': "+ для использования преимуществ CSI driver, с отдельными исключениями для "
        "[инструментирования NGINX]"
        "(/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "
        '"Узнайте, как принудительно инструментировать пропатченные/нестандартные '
        'двоичные файлы NGINX во время выполнения.")',
        "Deployments using the cloud-native full-stack mode require Dynatrace Operator "
        "version 1.6+ and OneAgent version 1.317+.": "Развёртывания в режиме Cloud-Native Full-Stack требуют Dynatrace Operator "
        "версии 1.6+ и OneAgent версии 1.317+.",
        "With the node image pull feature enabled, Kubernetes-native integration into "
        "supply chain security tooling is greatly simplified. Additionally, the "
        "feature configures the operator to always pull images via the Kubernetes "
        "nodes, reducing the need for a `customPullSecret` when sourcing images from "
        "private registries.": "При включённой функции загрузки образов на узле значительно упрощается "
        "нативная для Kubernetes интеграция с инструментами безопасности цепочки "
        "поставок. Кроме того, эта функция настраивает оператор всегда загружать "
        "образы через узлы Kubernetes, снижая потребность в `customPullSecret` при "
        "получении образов из частных реестров.",
        "Dynatrace Operator deployments that do not utilize the CSI driver have "
        "increased storage requirements due to current Kubernetes concepts. Please "
        "refer to [Storage optimization without CSI driver](#storage-optimization) to "
        "learn how to minimize storage consumption.": "Развёртывания Dynatrace Operator, не использующие CSI driver, имеют "
        "повышенные требования к хранилищу из-за текущих концепций Kubernetes. О том, "
        "как минимизировать потребление хранилища, см. [Оптимизация хранилища без CSI "
        "driver](#storage-optimization).",
        "## Prerequisites": "## Предварительные требования",
        "* Dynatrace OneAgent version 1.311.72+": "* Dynatrace OneAgent версии 1.311.72+",
        "+ Recommended Dynatrace OneAgent version is 1.317+": "+ Рекомендуемая версия Dynatrace OneAgent: 1.317+",
        "* Dynatrace code modules image sourced from our [supported public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry") or your [private registry]'
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry").': "* Образ Dynatrace code modules, полученный из наших [поддерживаемых "
        "публичных реестров]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра") или вашего [частного реестра]'
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра").',
        "When using a private registry, you must ensure that all nodes are "
        "authenticated to access the registry.": "При использовании частного реестра необходимо убедиться, что все узлы "
        "аутентифицированы для доступа к реестру.",
        "Alternatively, the following options are available for providing registry "
        "credentials:": "В качестве альтернативы для предоставления учётных данных реестра доступны "
        "следующие варианты:",
        "* **With CSI driver**: You can specify a `customPullSecret` in the DynaKube "
        "configuration to provide the necessary credentials for image pulls.": "* **С CSI driver**: можно указать `customPullSecret` в конфигурации DynaKube, "
        "чтобы предоставить необходимые учётные данные для загрузки образов.",
        "* **Without CSI driver**: The `customPullSecret` will not be added to "
        "injected application pods. For security reasons, Dynatrace Operator does not "
        "replicate provided pull secrets into application namespaces or mount them to "
        "pods outside of Dynatrace Operator's control. Instead, you must manually "
        "configure pull secrets at one of the following levels:": "* **Без CSI driver**: `customPullSecret` не добавляется во внедряемые поды "
        "приложений. По соображениям безопасности Dynatrace Operator не реплицирует "
        "предоставленные pull secret в пространства имён приложений и не монтирует их "
        "в поды вне контроля Dynatrace Operator. Вместо этого необходимо вручную "
        "настроить pull secret на одном из следующих уровней:",
        "+ **Node level**: Configure registry authentication directly on each node.": "+ **Уровень узла**: настройте аутентификацию в реестре непосредственно на "
        "каждом узле.",
        "+ **Namespace level**: Add the pull secret to the namespace where application "
        "pods are deployed.": "+ **Уровень пространства имён**: добавьте pull secret в пространство имён, "
        "где развёрнуты поды приложений.",
        "+ **Pod level**: Configure the pull secret via the `imagePullSecrets` field "
        "in the pod specification of your application pods.": "+ **Уровень пода**: настройте pull secret через поле `imagePullSecrets` в "
        "спецификации пода ваших подов приложений.",
        "For more information on manual pull secret configuration, see [Kubernetes "
        "documentation on pulling images from private registries]"
        "(https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).": "Подробнее о ручной настройке pull secret см. [документацию Kubernetes по "
        "загрузке образов из частных реестров]"
        "(https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).",
        "### Limitations": "### Ограничения",
        "Note that the following configurations are not supported:": "Обратите внимание, что следующие конфигурации не поддерживаются:",
        "* Due to GKE Autopilot's dynamic provisioning of nodes and their sizes based "
        "on the aggregated resource requests of Pods to optimize resource "
        "utilization, GKE Autopilot is not suitable for the node image pull feature in "
        "combination with the CSI driver.": "* Из-за того что GKE Autopilot динамически выделяет узлы и определяет их "
        "размеры на основе совокупных запросов ресурсов подов для оптимизации "
        "использования ресурсов, GKE Autopilot не подходит для функции загрузки "
        "образов на узле в сочетании с CSI driver.",
        "+ We recommend using the feature without the CSI driver on GKE Autopilot "
        "systems or, alternatively, using the CSI driver in a standard setup with node "
        "image pull disabled.": "+ Мы рекомендуем использовать эту функцию без CSI driver в системах GKE "
        "Autopilot или, в качестве альтернативы, использовать CSI driver в "
        "стандартной конфигурации с отключённой загрузкой образов на узле.",
        "## Behavior and configuration": "## Поведение и настройка",
        "Known issue in Dynatrace Operator version 1.5": "Известная проблема в Dynatrace Operator версии 1.5",
        "We have identified an issue with cloud-native full-stack without using the "
        "CSI driver with details provided in the [Dynatrace Operator version 1.5.1 "
        "release notes](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "
        '"Release notes for Dynatrace Operator, version 1.5.1").': "Мы выявили проблему с Cloud-Native Full-Stack без использования CSI driver, "
        "подробности приведены в [примечаниях к выпуску Dynatrace Operator версии "
        "1.5.1](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "
        '"Примечания к выпуску Dynatrace Operator версии 1.5.1.").',
        "**This issue has been resolved with Dynatrace Operator version 1.6.0 and "
        "OneAgent version 1.317+.**": "**Эта проблема устранена в Dynatrace Operator версии 1.6.0 и OneAgent версии "
        "1.317+.**",
        "The feature is activated via a feature flag on DynaKube. The following two "
        "points outline the behavior and benefits of the feature based on whether the "
        "CSI driver has been deployed as part of the operator:": "Функция активируется через флаг функции в DynaKube. Следующие два пункта "
        "описывают поведение и преимущества функции в зависимости от того, был ли CSI "
        "driver развёрнут как часть оператора:",
        "* **With CSI driver** - Instead of downloading the code modules into the CSI "
        "driver pod, Dynatrace code modules images are directly pulled through the "
        "node. Each CSI driver pod creates a job for the node to download the code "
        "modules to the host filesystem, where they will be used by the CSI driver as "
        "usual. This approach reduces the need for a `customPullSecret` when sourcing "
        "images from private registries. [1](#fn-2-1-def)": "* **С CSI driver**: вместо загрузки code modules в под CSI driver образы "
        "Dynatrace code modules загружаются напрямую через узел. Каждый под CSI driver "
        "создаёт для узла задание на загрузку code modules в файловую систему хоста, "
        "где они будут использоваться CSI driver как обычно. Такой подход снижает "
        "потребность в `customPullSecret` при получении образов из частных реестров. "
        "[1](#fn-2-1-def)",
        "* **Without CSI driver** [2](#fn-2-2-def) - If the CSI driver is not "
        "installed in your cluster, you can leverage the node image pull feature with "
        "the code modules image to improve injection performance and resiliency. This "
        "approach prioritizes injection performance for a faster and more resilient "
        "injection over storage optimizations enabled by the CSI driver. **Note:** The "
        "`customPullSecret` is not supported with the node image pull feature when "
        "used without the CSI driver. When using private registries, you must manually "
        "configure pull secrets at the node, namespace, or pod level (see "
        "[Prerequisites](#prerequisites)).": "* **Без CSI driver** [2](#fn-2-2-def): если CSI driver не установлен в вашем "
        "кластере, можно использовать функцию загрузки образов на узле с образом code "
        "modules для повышения производительности и устойчивости внедрения. Такой "
        "подход отдаёт приоритет производительности внедрения для более быстрого и "
        "устойчивого внедрения по сравнению с оптимизациями хранилища, обеспечиваемыми "
        "CSI driver. **Примечание:** `customPullSecret` не поддерживается функцией "
        "загрузки образов на узле при использовании без CSI driver. При использовании "
        "частных реестров необходимо вручную настроить pull secret на уровне узла, "
        "пространства имён или пода (см. [Предварительные требования](#prerequisites)).",
        "Starting from [Dynatrace Operator version 1.8]"
        "(/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "
        '"Release notes for Dynatrace Operator, version 1.8.0"), the download jobs '
        "inherit the same `PriorityClass` as the CSI driver to ensure fast scheduling "
        "and preemption on congested clusters. You can configure the value via "
        "`csidriver.priorityClassValue` in the Helm values file. For guidance, see "
        "[Use priorityClass for critical Dynatrace components]"
        "(/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "
        '"Use priorityClass for critical Dynatrace components").': "Начиная с [Dynatrace Operator версии 1.8]"
        "(/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "
        '"Примечания к выпуску Dynatrace Operator версии 1.8.0."), задания загрузки '
        "наследуют тот же `PriorityClass`, что и CSI driver, чтобы обеспечить быстрое "
        "планирование и вытеснение в перегруженных кластерах. Значение можно настроить "
        "через `csidriver.priorityClassValue` в файле значений Helm. Указания см. в "
        "[Использование priorityClass для критически важных компонентов Dynatrace]"
        "(/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "
        '"Использование priorityClass для критически важных компонентов Dynatrace").',
        "Please refer to [Storage optimization without CSI driver]"
        "(#storage-optimization) to learn how to minimize storage consumption.": "О том, как минимизировать потребление хранилища, см. [Оптимизация хранилища "
        "без CSI driver](#storage-optimization).",
        "### DynaKube configuration": "### Настройка DynaKube",
        "Refer to the following DynaKube snippet for configuring the feature flag and "
        "specifying a Dynatrace code modules image from a [supported public]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Use a public registry") or [private registry]'
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry"):': "Для настройки флага функции и указания образа Dynatrace code modules из "
        "[поддерживаемого публичного]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Использование публичного реестра") или [частного реестра]'
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра") см. следующий фрагмент DynaKube:',
        "Known issue": "Известная проблема",
        "There is a known issue with OneAgent versions >= 1.313.0 to < 1.313.45. "
        "Please use Dynatrace code modules version 1.313.45+.": "Существует известная проблема с версиями OneAgent >= 1.313.0 и < 1.313.45. "
        "Используйте Dynatrace code modules версии 1.313.45+.",
        "Example image tag for `codeModulesImage` field:": "Пример тега образа для поля `codeModulesImage`:",
        "For more details on repositories and tag information, explore our [supported "
        "public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry").': "Подробнее о репозиториях и информации о тегах см. наши [поддерживаемые "
        "публичные реестры]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра").',
        "## Storage optimization without CSI driver": "## Оптимизация хранилища без CSI driver",
        "OneAgent version 1.315+": "OneAgent версии 1.315+",
        "Without the CSI driver, code module injection consumes ephemeral storage for "
        "each injection. OneAgent binaries are stored and mounted to the app pod in an "
        "`emptyDir` volume. To minimize storage consumption, you can either annotate "
        "individual application pods or configure this setting at the DynaKube level, "
        "as appropriate. These annotations should specify the application technology "
        "(e.g., Java), allowing precise control over code module injection into "
        "application containers and preventing unnecessary code module binaries from "
        "being copied.": "Без CSI driver внедрение code module потребляет эфемерное хранилище при "
        "каждом внедрении. Двоичные файлы OneAgent хранятся и монтируются в под "
        "приложения в томе `emptyDir`. Чтобы минимизировать потребление хранилища, "
        "можно либо добавить аннотации к отдельным подам приложений, либо настроить "
        "этот параметр на уровне DynaKube, в зависимости от ситуации. Эти аннотации "
        "должны указывать технологию приложения (например, Java), что обеспечивает "
        "точный контроль над внедрением code module в контейнеры приложений и "
        "предотвращает копирование ненужных двоичных файлов code module.",
        "If a CSI driver is deployed on the node, you can also manually configure code "
        "module injection to not use the CSI driver.": "Если CSI driver развёрнут на узле, можно также вручную настроить внедрение "
        "code module так, чтобы оно не использовало CSI driver.",
        "For more information, see [Enforce CSI-less application monitoring]"
        "(#mixed-mode).": "Подробнее см. [Принудительный мониторинг Application без CSI](#mixed-mode).",
        "If storage optimization is not configured (i.e., the "
        "`oneagent.dynatrace.com/technologies` annotation is missing), storage "
        "consumption will follow the guidelines outlined in the [storage requirements]"
        "(/managed/ingest-from/setup-on-k8s/reference/storage "
        '"A comprehensive overview of the storage requirements for different Dynatrace '
        'Operator deployment mode in Kubernetes environments").': "Если оптимизация хранилища не настроена (то есть аннотация "
        "`oneagent.dynatrace.com/technologies` отсутствует), потребление хранилища "
        "будет следовать рекомендациям, изложенным в [требованиях к хранилищу]"
        "(/managed/ingest-from/setup-on-k8s/reference/storage "
        '"Полный обзор требований к хранилищу для различных режимов развёртывания '
        'Dynatrace Operator в окружениях Kubernetes").',
        "Each configured technology, whether specified individually or as a "
        "comma-separated list, will be copied into a shared volume, consuming "
        "ephemeral storage.": "Каждая настроенная технология, указанная по отдельности или в виде списка "
        "через запятую, будет скопирована в общий том, потребляя эфемерное хранилище.",
        "### Technology identifiers": "### Идентификаторы технологий",
        "Here is a list of the identifiers you can use per technology:": "Ниже приведён список идентификаторов, которые можно использовать для каждой "
        "технологии:",
        "| Technology | Identifier |": "| Технология | Идентификатор |",
        "| [Java]"
        "(/managed/ingest-from/technology-support/application-software/java "
        '"Learn about all aspects of Dynatrace support for Java application '
        'monitoring.") | `java` |': "| [Java]"
        "(/managed/ingest-from/technology-support/application-software/java "
        '"Узнайте обо всех аспектах поддержки Dynatrace для мониторинга '
        'Java-приложений.") | `java` |',
        "| [.NET, .NET Core and .NET Framework]"
        "(/managed/ingest-from/technology-support/application-software/dotnet "
        '"Learn about all aspects of Dynatrace support for .NET application '
        'monitoring.") | `dotnet` |': "| [.NET, .NET Core и .NET Framework]"
        "(/managed/ingest-from/technology-support/application-software/dotnet "
        '"Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений '
        '.NET.") | `dotnet` |',
        "| [Node.js]"
        "(/managed/ingest-from/technology-support/application-software/nodejs "
        '"Read about Dynatrace support for Node.js applications.") | `nodejs` |': "| [Node.js]"
        "(/managed/ingest-from/technology-support/application-software/nodejs "
        '"Прочитайте о поддержке Dynatrace для приложений Node.js.") | `nodejs` |',
        "| [Python]"
        "(/managed/ingest-from/technology-support/application-software/python "
        '"Learn how to instrument your Python application with OpenTelemetry as a data '
        'source for Dynatrace.") | `python` |': "| [Python]"
        "(/managed/ingest-from/technology-support/application-software/python "
        '"Узнайте, как инструментировать Python-приложение с OpenTelemetry в качестве '
        'источника данных для Dynatrace.") | `python` |',
        "| [PHP]"
        "(/managed/ingest-from/technology-support/application-software/php "
        '"Read about Dynatrace support for PHP applications.") | `php` |': "| [PHP]"
        "(/managed/ingest-from/technology-support/application-software/php "
        '"Прочитайте о поддержке Dynatrace для приложений PHP.") | `php` |',
        "| [Go]"
        "(/managed/ingest-from/technology-support/application-software/go "
        '"Read an overview of Dynatrace support for Go applications.") | `go` |': "| [Go]"
        "(/managed/ingest-from/technology-support/application-software/go "
        '"Обзор поддержки Dynatrace для приложений Go.") | `go` |',
        "| Apache, IBM HTTP Server | `apache` |": "| Apache, IBM HTTP Server | `apache` |",
        "| [NGINX]"
        "(/managed/ingest-from/technology-support/application-software/nginx "
        '"Learn the details of Dynatrace support for NGINX.") | `nginx` |': "| [NGINX]"
        "(/managed/ingest-from/technology-support/application-software/nginx "
        '"Узнайте подробности поддержки NGINX в Dynatrace.") | `nginx` |',
        "### Annotate the application pod": "### Добавление аннотации к поду приложения",
        "To reduce the data copied into application pods, you can specify which "
        "OneAgent technologies are relevant for your application. Annotate your "
        "application pods as shown in the pod snippet below:": "Чтобы сократить объём данных, копируемых в поды приложений, можно указать, "
        "какие технологии OneAgent актуальны для вашего приложения. Добавьте аннотации "
        "к вашим подам приложений, как показано во фрагменте пода ниже:",
        "When specifying a comma-separated list of technology identifiers, ensure "
        "there are no whitespace characters within the annotation value.": "При указании списка идентификаторов технологий через запятую убедитесь, что "
        "в значении аннотации нет пробельных символов.",
        "Annotation values must use the exact technology identifiers listed in the "
        "table above.": "Значения аннотаций должны использовать точные идентификаторы технологий, "
        "перечисленные в таблице выше.",
        "If no `oneagent.dynatrace.com/technologies` is provided, all technologies "
        "will be copied to application pods.": "Если `oneagent.dynatrace.com/technologies` не указан, в поды приложений будут "
        "скопированы все технологии.",
        "If a single technology is used across your cluster, or if you want to set a "
        "default technology for Dynatrace code module injection, you can configure it "
        "at the DynaKube level to apply to all injected application pods.": "Если во всём кластере используется одна технология или если вы хотите задать "
        "технологию по умолчанию для внедрения Dynatrace code module, её можно "
        "настроить на уровне DynaKube, чтобы она применялась ко всем внедряемым подам "
        "приложений.",
        "Configure on DynaKube-level": "Настройка на уровне DynaKube",
        "Modify your DynaKube configuration by enabling the feature and restricting it "
        "to a specific technology or a set of multiple technologies:": "Измените конфигурацию DynaKube, включив функцию и ограничив её определённой "
        "технологией или набором из нескольких технологий:",
        "## Enforce CSI-less application monitoring": "## Принудительный мониторинг Application без CSI",
        "You can selectively configure Dynatrace code module injection without "
        "involving the CSI driver, even if the driver is available on the node.": "Можно выборочно настроить внедрение Dynatrace code module без участия CSI "
        "driver, даже если драйвер доступен на узле.",
        "In this case, code module injection behaves as described in [Storage "
        "optimization without the CSI driver](#storage-optimization).": "В этом случае внедрение code module ведёт себя так, как описано в "
        "[Оптимизация хранилища без CSI driver](#storage-optimization).",
        'To do this, use the `oneagent.dynatrace.com/volume-type: "ephemeral"` '
        "annotation, as shown in the code block below.": "Для этого используйте аннотацию "
        '`oneagent.dynatrace.com/volume-type: "ephemeral"`, как показано в блоке кода '
        "ниже.",
        "(The `oneagent.dynatrace.com/technologies` annotation is additional and "
        "optional, see [Annotate the application pod](#technologies).)": "(Аннотация `oneagent.dynatrace.com/technologies` является дополнительной и "
        "необязательной, см. [Добавление аннотации к поду приложения](#technologies).)",
        "To manually force the default behavior, set the "
        '`oneagent.dynatrace.com/volume-type: "csi"` annotation.': "Чтобы вручную принудительно задать поведение по умолчанию, установите "
        'аннотацию `oneagent.dynatrace.com/volume-type: "csi"`.',
        "In this case, [a CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "
        '"Components of Dynatrace Operator") needs to be available on the node for '
        "code module injection to work.": "В этом случае для работы внедрения code module на узле должен быть доступен "
        "[CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "
        '"Компоненты Dynatrace Operator").',
        "This approach allows you to combine the best of both methods: the storage "
        "optimizations provided by the CSI driver and the performance gains and "
        "enhanced resiliency of injection without the CSI driver for selected pods and "
        "applications.": "Такой подход позволяет сочетать лучшее из обоих методов: оптимизации "
        "хранилища, обеспечиваемые CSI driver, и прирост производительности и "
        "повышенную устойчивость внедрения без CSI driver для выбранных подов и "
        "приложений.",
        "Example scenarios:": "Примеры сценариев:",
        "* [NGINX instrumentation]"
        "(/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "
        '"Learn how to force instrumenting patched/non-standard NGINX binaries during '
        'runtime.") and prior injection are recommended without the CSI driver for '
        "higher resiliency, while other workloads can be injected using the CSI "
        "driver, thus eliminating the need for any vendor-specific annotations.": "* [Инструментирование NGINX]"
        "(/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "
        '"Узнайте, как принудительно инструментировать пропатченные/нестандартные '
        'двоичные файлы NGINX во время выполнения.") и предварительное внедрение '
        "рекомендуются без CSI driver для более высокой устойчивости, тогда как другие "
        "рабочие нагрузки можно внедрять с использованием CSI driver, что устраняет "
        "необходимость в каких-либо специфичных для поставщика аннотациях.",
        "* Mixed setups with and without node access, such as AWS Elastic Kubernetes "
        "Service (EKS) with EC2 nodes and Fargate, can be accommodated. Ensure the CSI "
        "driver is available on all nodes where code module injection based on CSI "
        "driver might occur.": "* Можно учитывать смешанные конфигурации с доступом к узлам и без него, "
        "например AWS Elastic Kubernetes Service (EKS) с узлами EC2 и Fargate. "
        "Убедитесь, что CSI driver доступен на всех узлах, где может происходить "
        "внедрение code module на основе CSI driver.",
    },
}

# Lines copied verbatim (identifier-only lines / bare footnote markers / EN headings).
PASS = {
    "using-gitops.md": {
        "1",
        "2",
    },
    "node-image-pull.md": {
        "cloudNativeFullStack applicationMonitoring",
        "1",
        "2",
        "applicationMonitoring cloudNativeFullStack OneAgent version 1.315+",
        "| --- | --- |",
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
