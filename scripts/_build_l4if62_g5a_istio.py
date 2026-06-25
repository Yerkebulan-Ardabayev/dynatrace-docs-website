# -*- coding: utf-8 -*-
"""L4-IF.62 g5a builder: istio-deployment.md (single file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied verbatim}
for identifier headings / bare-token lines. Any prose line missing from both
raises SystemExit -> catches leftover-EN before writing.

Note: EN source contains mojibake `ï»¿` before some link `]`/text; MOJI_RE strips
it from both EN line and TRANS keys, so keys are written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/deployment-and-configuration"
FNAME = "istio-deployment.md"

# ----------------------------------------------------------------------------
TRANS = {
    "title: Deploy Dynatrace alongside Istio": "title: Развёртывание Dynatrace вместе с Istio",
    "# Deploy Dynatrace alongside Istio": "# Развёртывание Dynatrace вместе с Istio",
    "* 10-min read": "* Чтение: 10 мин",
    "* Updated on Oct 22, 2025": "* Обновлено 22 октября 2025 г.",
    "This guide explains how Dynatrace components can be deployed alongside Istio. "
    "A Dynatrace deployment on Kubernetes contains several components that need to "
    "communicate with each other, with the Dynatrace cluster and other external "
    "resources.": "В этом руководстве описано, как компоненты Dynatrace можно развернуть "
    "вместе с Istio. Развёртывание Dynatrace в Kubernetes содержит несколько "
    "компонентов, которым необходимо взаимодействовать друг с другом, с кластером "
    "Dynatrace и другими внешними ресурсами.",
    "For more information on communication of Dynatrace Operator and its managed "
    "components, see the [network traffic]"
    "(/managed/ingest-from/setup-on-k8s/reference/network "
    '"Network traffic requirements for the Dynatrace Operator components in a '
    'Kubernetes cluster.") reference page.': "Дополнительную информацию о взаимодействии Dynatrace Operator и управляемых "
    "им компонентов см. на справочной странице [Сетевой трафик]"
    "(/managed/ingest-from/setup-on-k8s/reference/network "
    '"Требования к сетевому трафику для компонентов Dynatrace Operator в кластере '
    'Kubernetes.").',
    "## Limitations": "## Ограничения",
    "* Istio injection into the Dynatrace Operator namespace is not supported.": "* Инъекция Istio в пространство имён Dynatrace Operator не поддерживается.",
    "* Istio spin-offs are currently not supported (for example, Maistra or "
    "OpenShift Service Mesh).": "* Производные сборки Istio в настоящее время не поддерживаются (например, "
    "Maistra или OpenShift Service Mesh).",
    "* Istio East-West (sidecar combined with ambient) deployment is not "
    "supported.": "* Развёртывание Istio East-West (sidecar в сочетании с ambient) не "
    "поддерживается.",
    "## Setup considerations": "## Вопросы для рассмотрения при настройке",
    "This guide covers two predefined configurations of Istio, chosen for their "
    "simplicity and common use cases. While Istio offers extensive customization "
    "options, these configurations serve as a starting point. This section "
    "explains the configuration scenarios and provides guidance on selecting the "
    "right Dynatrace setup that best suits your needs. Note that Dynatrace does "
    "not impose any limitations on how you configure Istio.": "В этом руководстве рассматриваются две предопределённые конфигурации Istio, "
    "выбранные за их простоту и распространённость сценариев использования. Хотя "
    "Istio предлагает обширные возможности настройки, эти конфигурации служат "
    "отправной точкой. В этом разделе описаны сценарии конфигурации и приводятся "
    "рекомендации по выбору подходящей настройки Dynatrace, наиболее "
    "соответствующей вашим потребностям. Обратите внимание, что Dynatrace не "
    "накладывает никаких ограничений на то, как вы настраиваете Istio.",
    "* **Default Istio configuration** Recommended": "* **Конфигурация Istio по умолчанию** Рекомендуется",
    "This represents the default deployment of Istio, meaning no special mesh "
    "configuration. It's basically the result of following the official [Istio "
    "installation guide](https://dt-url.net/hm03u3r).": "Это стандартное развёртывание Istio, то есть без особой конфигурации "
    "сетки. По сути, это результат следования официальному [руководству по "
    "установке Istio](https://dt-url.net/hm03u3r).",
    "This means Istio is installed either via Helm or `istioctl` in sidecar mode "
    "with the CNI node agent.": "Это означает, что Istio устанавливается через Helm или `istioctl` в режиме "
    "sidecar с узловым агентом CNI.",
    "Follow the [setup guide for the default Istio configuration]"
    "(#setup-guide-for-default-istio-configuration) if Istio is deployed "
    "accordingly.": "Следуйте [руководству по настройке конфигурации Istio по умолчанию]"
    "(#setup-guide-for-default-istio-configuration), если Istio развёрнут "
    "соответствующим образом.",
    "* **Secure Istio configuration**": "* **Защищённая конфигурация Istio**",
    'This represents a "secure" configuration of Istio. However, this does not '
    "mean that we consider this the best practice for security configuration in "
    "Istio or that this should be seen as a guide for securing Istio. This setup "
    "is based on settings that are most likely to influence the deployed Dynatrace "
    "components and their connections. This scenario assumes that Istio is deployed "
    "with strict mTLS and `outboundTrafficPolicy` set to `REGISTRY_ONLY`. These "
    "options severely limit the incoming and outgoing connections for workloads in "
    "the mesh.": "Это защищённая конфигурация Istio. Однако это не означает, что мы считаем "
    "её лучшей практикой настройки безопасности в Istio или что её следует "
    "рассматривать как руководство по защите Istio. Эта настройка основана на "
    "параметрах, которые с наибольшей вероятностью влияют на развёрнутые "
    "компоненты Dynatrace и их соединения. Этот сценарий предполагает, что Istio "
    "развёрнут со строгим mTLS и `outboundTrafficPolicy`, установленным в "
    "`REGISTRY_ONLY`. Эти параметры существенно ограничивают входящие и исходящие "
    "соединения для рабочих нагрузок в сетке.",
    "Choose this configuration if any point below applies:": "Выберите эту конфигурацию, если применим любой из приведённых ниже пунктов:",
    "+ If you have enabled mTLS in strict mode.": "+ Если вы включили mTLS в строгом режиме.",
    "+ If you have an `outboundTrafficPolicy` set to `REGISTRY_ONLY`.": "+ Если у вас `outboundTrafficPolicy` установлен в `REGISTRY_ONLY`.",
    "If none of the points above apply, choose [Default Istio configuration]"
    "(#setup-guide-for-default-istio-configuration).": "Если ни один из приведённых выше пунктов не применим, выберите [Конфигурацию "
    "Istio по умолчанию](#setup-guide-for-default-istio-configuration).",
    "Follow the [setup guide for the secure Istio configuration]"
    "(#setup-guide-for-secure-istio-configuration) if Istio is deployed "
    "accordingly.": "Следуйте [руководству по настройке защищённой конфигурации Istio]"
    "(#setup-guide-for-secure-istio-configuration), если Istio развёрнут "
    "соответствующим образом.",
    "### Other deployment considerations": "### Другие вопросы для рассмотрения при развёртывании",
    "Disable injection of CNI pods": "Отключение инъекции в поды CNI",
    "#### Disable injection of CNI pods": "#### Отключение инъекции в поды CNI",
    "This is relevant to you if all of the following applies to your deployment:": "Это актуально для вас, если к вашему развёртыванию применимо всё следующее:",
    "* Not supported Dynatrace Operator is deployed inside the mesh.": "* Не поддерживается Dynatrace Operator развёрнут внутри сетки.",
    "* Istio is deployed using sidecars.": "* Istio развёрнут с использованием sidecar.",
    "* Istio is configured to use the CNI component.": "* Istio настроен на использование компонента CNI.",
    "* You have not configured any namespace selector in the DynaKube that would "
    "exclude the `istio-system` namespace.": "* Вы не настроили в DynaKube ни одного селектора пространств имён, который "
    "исключал бы пространство имён `istio-system`.",
    "In all scenarios, you should exclude the Istio CNI pods from being injected "
    "by the Dynatrace Operator. Otherwise, when adding a new node to the cluster, "
    "it is possible that a deadlock situation will occur.": "Во всех сценариях следует исключить поды Istio CNI из инъекции Dynatrace "
    "Operator. В противном случае при добавлении нового узла в кластер возможно "
    "возникновение взаимоблокировки.",
    "Both the CSI driver and Istio's CNI agent are DeamonSets, and will therefore "
    "be deployed on any (new) node in the cluster.": "И CSI driver, и агент CNI Istio являются DaemonSets, поэтому будут "
    "развёрнуты на любом (новом) узле кластера.",
    "* The CSI driver pod will be injected by Istio with an init container that "
    "waits for the correct setup of the redirection rules needed for the proxy "
    "sidecar to work.": "* В под CSI driver Istio внедрит init-контейнер, который ожидает "
    "корректной настройки правил перенаправления, необходимых для работы proxy "
    "sidecar.",
    "* The CNI pod will be injected by Dynatrace to include the required OneAgent "
    "binaries for instrumentation that are provided via a volume provisioned by "
    "the CSI driver on that Node.": "* В под CNI Dynatrace внедрит необходимые для инструментирования бинарные "
    "файлы OneAgent, которые предоставляются через том, подготавливаемый CSI "
    "driver на этом узле.",
    "This leads to a situation where both pods cannot start:": "Это приводит к ситуации, когда оба пода не могут запуститься:",
    "* The CNI pod is waiting for the CSI driver to become ready to provide the "
    "volume.": "* Под CNI ожидает, пока CSI driver не будет готов предоставить том.",
    "* The CSI pod is waiting for the CNI agent to provide the redirections for "
    "the proxy.": "* Под CSI ожидает, пока агент CNI не предоставит перенаправления для proxy.",
    "Also all other workloads that are target of either the Istio or Dynatrace "
    "injection and get scheduled on that Node will be affected and won't be able "
    "to start.": "Кроме того, это затронет все остальные рабочие нагрузки, которые являются "
    "целью инъекции Istio или Dynatrace и планируются на этот узел, и они не "
    "смогут запуститься.",
    "The easiest way to exclude the CNI pods from the injection by the Dynatrace "
    'Operator is to add the annotation `oneagent.dynatrace.com/inject: "false"`. '
    "For example, for a Helm deployment of Istio, add the following to the values "
    "of the `cni` chart:": "Самый простой способ исключить поды CNI из инъекции Dynatrace Operator, "
    'это добавить аннотацию `oneagent.dynatrace.com/inject: "false"`. Например, '
    "для развёртывания Istio через Helm добавьте следующее в значения чарта "
    "`cni`:",
    "Native sidecar support": "Поддержка нативных sidecar",
    "#### Native sidecar support": "#### Поддержка нативных sidecar",
    "Istio 1.28 deployed on a compatible Kubernetes cluster (>=1.29) will use "
    "native sidecar containers. This new type of sidecar container is currently "
    "not supported by Dynatrace Operator. Disable native sidecars in your Istio "
    "deployment by adding the following environment variable to the pilot "
    "deployment.": "Istio 1.28, развёрнутый на совместимом кластере Kubernetes (>=1.29), будет "
    "использовать нативные контейнеры sidecar. Этот новый тип контейнера sidecar "
    "в настоящее время не поддерживается Dynatrace Operator. Отключите нативные "
    "sidecar в вашем развёртывании Istio, добавив следующую переменную окружения "
    "в развёртывание pilot.",
    "Example values for the Istio helm chart:": "Пример значений для helm-чарта Istio:",
    "## Setup guide for default Istio configuration": "## Руководство по настройке конфигурации Istio по умолчанию",
    "Because Dynatrace supports Istio in the default configuration, you only need "
    "to enable the `enableIstio` parameter in the [DynaKube]"
    "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
    '"List the available parameters for setting up Dynatrace Operator on '
    "Kubernetes.\"). However, you don't need to set this parameter if you don't "
    "plan to use a restrictive `outboundTrafficPolicy`.": "Поскольку Dynatrace поддерживает Istio в конфигурации по умолчанию, вам "
    "нужно лишь включить параметр `enableIstio` в [DynaKube]"
    "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
    '"Список доступных параметров для настройки Dynatrace Operator в '
    'Kubernetes."). Однако задавать этот параметр не требуется, если вы не '
    "планируете использовать ограничительный `outboundTrafficPolicy`.",
    "When this parameter is enabled, Dynatrace Operator will deploy "
    "`ServiceEntries` and `VirtualServices` to enable communication from inside "
    "the mesh to all relevant Dynatrace components and the Dynatrace environment. "
    "The `ServiceEntries` and `VirtualServices` work regardless of whether "
    "Dynatrace Operator's namespace itself is part of the mesh (if no "
    "`discoveryfilter` is set in Istio).": "Когда этот параметр включён, Dynatrace Operator развернёт `ServiceEntries` "
    "и `VirtualServices`, чтобы обеспечить взаимодействие изнутри сетки со всеми "
    "соответствующими компонентами Dynatrace и окружением Dynatrace. "
    "`ServiceEntries` и `VirtualServices` работают независимо от того, является "
    "ли само пространство имён Dynatrace Operator частью сетки (если в Istio не "
    "задан `discoveryfilter`).",
    "This enables all workloads and OneAgents to connect to the ActiveGate "
    "instance and all required connections to the Dynatrace environment. "
    "Therefore, all Dynatrace features are expected to work.": "Это позволяет всем рабочим нагрузкам и экземплярам OneAgent подключаться к "
    "экземпляру ActiveGate и устанавливать все необходимые соединения с "
    "окружением Dynatrace. Поэтому ожидается, что все функции Dynatrace будут "
    "работать.",
    "`ServiceEntries` result in additional DNS queries executed by each sidecar "
    "proxy. This can put additional load on your DNS server.": "`ServiceEntries` приводят к дополнительным DNS-запросам, выполняемым каждым "
    "proxy sidecar. Это может создать дополнительную нагрузку на ваш DNS-сервер.",
    "To minimize the number of URLs, and therefore DNS queries, make sure the "
    "network zones in your Dynatrace environment are configured correctly. For a "
    "detailed setup description, see [Kubernetes network zone docs]"
    "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones#kubernetes-cluster-with-restricted-egress "
    '"Set up and use network zones in Kubernetes environments with the Dynatrace '
    'Operator.").': "Чтобы минимизировать количество URL-адресов и, соответственно, "
    "DNS-запросов, убедитесь, что network zones в вашем окружении Dynatrace "
    "настроены правильно. Подробное описание настройки см. в [документации по "
    "network zone для Kubernetes]"
    "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones#kubernetes-cluster-with-restricted-egress "
    '"Настройка и использование network zones в окружениях Kubernetes с '
    'Dynatrace Operator.").',
    "If this is not possible or sufficient in your environment, see [Istio DNS "
    "proxying](https://dt-url.net/ab23uvy) for another possible mitigation.": "Если это невозможно или недостаточно в вашем окружении, см. [Istio DNS "
    "proxying](https://dt-url.net/ab23uvy) как ещё один возможный способ "
    "смягчения.",
    "### How `enableIstio` works": "### Как работает `enableIstio`",
    "The `enableIstio` attribute is a convenience feature that automatically "
    "creates `ServiceEntries` and `VirtualServices` for connection endpoints "
    "required by:": "Атрибут `enableIstio`, это функция для удобства, которая автоматически "
    "создаёт `ServiceEntries` и `VirtualServices` для конечных точек соединения, "
    "необходимых:",
    "* Dynatrace Operator: Uses `apiUrl` defined in DynaKube.": "* Dynatrace Operator: использует `apiUrl`, определённый в DynaKube.",
    "* ActiveGate: Uses the `/v1/deployment/installer/gateway/connectioninfo` "
    "endpoint.": "* ActiveGate: использует конечную точку "
    "`/v1/deployment/installer/gateway/connectioninfo`.",
    "* OneAgent injected into user containers: Uses the "
    "`/v1/deployment/installer/agent/connectioninfo`, which respects the "
    "`networkZone` attribute for routing.": "* OneAgent, внедрённый в пользовательские контейнеры: использует "
    "`/v1/deployment/installer/agent/connectioninfo`, который учитывает атрибут "
    "`networkZone` для маршрутизации.",
    "Note that `enableIstio` attribute will not consider pre-existing "
    "`ServiceEntries` and `VirtualServices`. Using this attribute prematurely "
    "might lead to conflicts in Istio configurations. In complex setups, manual "
    "configuration may yield better outcomes.": "Обратите внимание, что атрибут `enableIstio` не учитывает уже "
    "существующие `ServiceEntries` и `VirtualServices`. Преждевременное "
    "использование этого атрибута может привести к конфликтам в конфигурациях "
    "Istio. В сложных настройках ручная настройка может дать лучшие результаты.",
    "Changes to the `enableIstio` attribute require you to remove and reapply "
    "your DynaKube for the update to take effect.": "Изменения атрибута `enableIstio` требуют удаления и повторного применения "
    "вашего DynaKube, чтобы обновление вступило в силу.",
    "Manual configuration": "Ручная настройка",
    "Manual configuration of `ServiceEntries` and `VirtualServices` may be "
    "required in the following cases:": "Ручная настройка `ServiceEntries` и `VirtualServices` может потребоваться в "
    "следующих случаях:",
    "#### ActiveGate": "#### ActiveGate",
    "* **Requirement**: Necessary if the ActiveGate pod is part of the mesh.": "* **Требование**: необходимо, если под ActiveGate является частью сетки.",
    "* **Configuration**: Manually configure `ServiceEntries` and "
    "`VirtualServices` based on the output of the "
    "`/v1/deployment/installer/gateway/connectioninfo` endpoint.": "* **Конфигурация**: вручную настройте `ServiceEntries` и `VirtualServices` "
    "на основе вывода конечной точки "
    "`/v1/deployment/installer/gateway/connectioninfo`.",
    "#### `cloudNativeFullstack` and `applicationMonitoring`": "#### `cloudNativeFullstack` и `applicationMonitoring`",
    "* **Requirement**: Necessary if injected user applications are part of the "
    "mesh.": "* **Требование**: необходимо, если внедрённые пользовательские приложения "
    "являются частью сетки.",
    "* **Configuration**: Manually configure `ServiceEntries` and "
    "`VirtualServices` based on the output of the "
    "`/v1/deployment/installer/agent/connectioninfo` endpoint.": "* **Конфигурация**: вручную настройте `ServiceEntries` и `VirtualServices` "
    "на основе вывода конечной точки "
    "`/v1/deployment/installer/agent/connectioninfo`.",
    "## Setup guide for secure Istio configuration": "## Руководство по настройке защищённой конфигурации Istio",
    "In such a restricted environment, and depending on your required Dynatrace "
    "features and other considerations, it might be necessary to create a few "
    "additional configuration rules for Istio. There are a few things to consider "
    "regarding the Dynatrace components when deciding how to deploy Dynatrace "
    "Operator.": "В таком ограниченном окружении и в зависимости от необходимых вам функций "
    "Dynatrace и других соображений может потребоваться создать несколько "
    "дополнительных правил конфигурации для Istio. Принимая решение о том, как "
    "развернуть Dynatrace Operator, следует учесть ряд моментов, касающихся "
    "компонентов Dynatrace.",
    "* Even if routing is enabled on the ActiveGate, OneAgents will fall back to "
    "directly connecting to the Dynatrace environment if the ActiveGate is not "
    "reachable (for example because it's inside the mesh). That means no "
    "monitoring data is lost if some OneAgents can't connect to the ActiveGate "
    "because of the chosen deployment strategy.": "* Даже если на ActiveGate включена маршрутизация, экземпляры OneAgent "
    "вернутся к прямому подключению к окружению Dynatrace, если ActiveGate "
    "недоступен (например, потому что он находится внутри сетки). Это означает, "
    "что данные мониторинга не теряются, если некоторые экземпляры OneAgent не "
    "могут подключиться к ActiveGate из-за выбранной стратегии развёртывания.",
    "* The monitoring modes `classicFullStack` or `cloudNativeFullStack` create "
    "pods with host networking enabled. That means those pods can never be part "
    "of the mesh, as Istio does not support pods with host networking. For "
    "`classicFullStack`, those pods handle all application metrics, while for "
    "`cloudNativeFullStack`, only host monitoring is affected.": "* Режимы мониторинга `classicFullStack` или `cloudNativeFullStack` создают "
    "поды с включённым host networking. Это означает, что такие поды никогда не "
    "могут быть частью сетки, поскольку Istio не поддерживает поды с host "
    "networking. Для `classicFullStack` такие поды обрабатывают все метрики "
    "приложения, тогда как для `cloudNativeFullStack` затрагивается только "
    "мониторинг хоста.",
    "* Some features of the ActiveGate might require direct connections to pods "
    "(for example, metric scraping). With mTLS enabled in Istio, direct "
    "connections to pod IPs are not possible. For a workaround for metric "
    "scraping, see [Istio metric merging]"
    "(#metric-scraping-using-istio-metric-merging).": "* Некоторые функции ActiveGate могут требовать прямых соединений с подами "
    "(например, сбор метрик (scraping)). При включённом в Istio mTLS прямые "
    "соединения с IP-адресами подов невозможны. Обходной путь для сбора метрик "
    "см. в разделе [Объединение метрик Istio]"
    "(#metric-scraping-using-istio-metric-merging).",
    "### Deployment outside the mesh": "### Развёртывание вне сетки",
    "In this scenario, the least complex deployment is outside the mesh. You "
    "still have to enable the `enableIstio` parameter in the DynaKube. The "
    "possible downsides of this deployment might include:": "В этом сценарии наименее сложным является развёртывание вне сетки. Вам "
    "по-прежнему необходимо включить параметр `enableIstio` в DynaKube. Возможные "
    "недостатки такого развёртывания могут включать:",
    "* Communication from inside the mesh to the ActiveGate will not be secured "
    "by mTLS. However, the communication is still encrypted via HTTPS.": "* Взаимодействие изнутри сетки с ActiveGate не будет защищено mTLS. Однако "
    "взаимодействие по-прежнему шифруется через HTTPS.",
    "* The ActiveGate is not able to connect to any pod or service inside the "
    "mesh. If metric scraping is your only concern, see the [Metric scraping "
    "using Istio metric merging](#metric-scraping-using-istio-metric-merging) "
    "workaround (not applicable for Istio ambient).": "* ActiveGate не может подключиться к какому-либо поду или сервису внутри "
    "сетки. Если вас беспокоит только сбор метрик, см. обходной путь [Сбор "
    "метрик с использованием объединения метрик Istio]"
    "(#metric-scraping-using-istio-metric-merging) (неприменимо для Istio "
    "ambient).",
    "Depending on whether most of your monitored workloads are part of the mesh "
    "or most of your targets for metric scraping are inside the mesh, deploying "
    "only the ActiveGate inside the mesh can be a more suitable option.": "В зависимости от того, является ли большая часть ваших отслеживаемых "
    "рабочих нагрузок частью сетки или большая часть ваших целей для сбора "
    "метрик находится внутри сетки, развёртывание внутри сетки только ActiveGate "
    "может быть более подходящим вариантом.",
    "### ActiveGate deployment inside the mesh": "### Развёртывание ActiveGate внутри сетки",
    "The most compatible deployment option is to deploy only the ActiveGate "
    "inside the mesh. This deployment option makes the most sense if most of your "
    "monitored workloads are also part of the mesh or if you need the ActiveGate "
    "to directly connect to pods inside the mesh (for example, for Prometheus "
    "scraping).": "Наиболее совместимый вариант развёртывания, это развернуть внутри сетки "
    "только ActiveGate. Этот вариант развёртывания наиболее целесообразен, если "
    "большая часть ваших отслеживаемых рабочих нагрузок также является частью "
    "сетки или если вам нужно, чтобы ActiveGate напрямую подключался к подам "
    "внутри сетки (например, для сбора (scraping) Prometheus).",
    "1. Make sure that the Dynatrace Operator namespace is not labeled for Istio "
    "injection (`istio-injection` or `istio.io/dataplane-mode` label is not set).": "1. Убедитесь, что пространство имён Dynatrace Operator не помечено для "
    "инъекции Istio (метка `istio-injection` или `istio.io/dataplane-mode` не "
    "задана).",
    "2. Label the ActiveGate pods for Istio by adding the following to your "
    "DynaKube:": "2. Пометьте поды ActiveGate для Istio, добавив следующее в ваш DynaKube:",
    "Sidecar": "Sidecar",
    "Ambient": "Ambient",
    "Restart your ActiveGate pods to trigger the injection.": "Перезапустите поды ActiveGate, чтобы запустить инъекцию.",
    "3. Optional You can enable communication from OneAgents outside the mesh to "
    "the ActiveGate by deploying the following `PeerAuthentication` resource:": "3. Необязательно Можно включить взаимодействие экземпляров OneAgent вне "
    "сетки с ActiveGate, развернув следующий ресурс `PeerAuthentication`:",
    "All communication to the ActiveGate will still be encrypted using HTTPS.": "Всё взаимодействие с ActiveGate по-прежнему будет шифроваться с "
    "использованием HTTPS.",
    "Configure Dynatrace Operator CSI driver with Istio in registry-only mode "
    "and custom codeModulesImage": "Настройка Dynatrace Operator CSI driver с Istio в режиме registry-only и "
    "пользовательским codeModulesImage",
    "### Configure Dynatrace Operator CSI driver with Istio in registry-only "
    "mode": "### Настройка Dynatrace Operator CSI driver с Istio в режиме registry-only",
    "When using Istio configured to `REGISTRY_ONLY` mode with the "
    "`codeModulesImage` field for CSI driver, you need to apply additional "
    "configuration to ensure proper communication with the image registry.": "При использовании Istio, настроенного в режим `REGISTRY_ONLY`, с полем "
    "`codeModulesImage` для CSI driver необходимо применить дополнительную "
    "конфигурацию для обеспечения надлежащего взаимодействия с реестром образов.",
    "#### Prerequisites": "#### Предварительные требования",
    "* Istio is installed and configured in `REGISTRY_ONLY` mode.": "* Istio установлен и настроен в режиме `REGISTRY_ONLY`.",
    "* Not supported Dynatrace Operator CSI driver is injected with Istio.": "* Не поддерживается Dynatrace Operator CSI driver внедрён с помощью Istio.",
    "* `codeModulesImage` field is specified in the CSI driver configuration.": "* Поле `codeModulesImage` указано в конфигурации CSI driver.",
    "#### Configure `ServiceEntry` for CSI driver": "#### Настройка `ServiceEntry` для CSI driver",
    "1. Create a `ServiceEntry`.": "1. Создайте `ServiceEntry`.",
    "The `ServiceEntry` configuration allows the Dynatrace Operator CSI driver to "
    "communicate with the specified image registry. Without this configuration, "
    "the image pull process will fail. See an example of `ServiceEntry` for "
    "`docker.io` below.": "Конфигурация `ServiceEntry` позволяет Dynatrace Operator CSI driver "
    "взаимодействовать с указанным реестром образов. Без этой конфигурации "
    "процесс загрузки образа завершится сбоем. См. пример `ServiceEntry` для "
    "`docker.io` ниже.",
    "2. Apply the `ServiceEntry`.": "2. Примените `ServiceEntry`.",
    "Save and apply the above configuration to a file.": "Сохраните приведённую выше конфигурацию в файл и примените её.",
    "## Metric scraping using Istio metric merging": "## Сбор метрик с использованием объединения метрик Istio",
    "[Dynatrace metric scraping]"
    "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "
    '"Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, '
    'and monitoring consumption.") is done via the ActiveGate and configured via '
    "annotations. This results in the ActiveGate connecting directly to the pods "
    "on the configured endpoint to scrape the metrics. As stated earlier, this "
    "direct connection does not work with strict mTLS.": "[Сбор метрик Dynatrace]"
    "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "
    '"Прием метрик из конечных точек Prometheus в Kubernetes, оповещения по '
    'метрикам и потребление мониторинга.") выполняется через ActiveGate и '
    "настраивается с помощью аннотаций. В результате ActiveGate подключается "
    "напрямую к подам на настроенной конечной точке для сбора метрик. Как "
    "указано ранее, такое прямое соединение не работает со строгим mTLS.",
    "Istio ambient mode does not support metric merging as it requires a sidecar "
    "proxy. However, in ambient mode it's possible for the ActiveGate to directly "
    "connect to the pod IPs and scrape the configured targets. Depending on your "
    "mTLS policy, this might only be possible for pods inside the mesh if the "
    "ActiveGate is also part of the mesh.": "Режим Istio ambient не поддерживает объединение метрик, поскольку для него "
    "требуется proxy sidecar. Однако в режиме ambient ActiveGate может напрямую "
    "подключаться к IP-адресам подов и собирать данные с настроенных целей. В "
    "зависимости от вашей политики mTLS это может быть возможно только для подов "
    "внутри сетки, если ActiveGate также является частью сетки.",
    "Istio provides a feature called [metric merging]"
    "(https://dt-url.net/5y43ufx) that uses the (widely adopted) "
    "`prometheus.io/...` annotations to configure an additional endpoint in the "
    "sidecar proxy that serves Istio and Envoy metrics as well as the application "
    "metrics defined by the annotations. This newly created endpoint is excepted "
    "from mTLS and therefore reachable from outside the mesh despite having mTLS "
    "in strict mode.": "Istio предоставляет функцию под названием [объединение метрик]"
    "(https://dt-url.net/5y43ufx), которая использует (широко применяемые) "
    "аннотации `prometheus.io/...` для настройки дополнительной конечной точки в "
    "proxy sidecar, которая предоставляет метрики Istio и Envoy, а также метрики "
    "приложения, определённые аннотациями. Эта вновь созданная конечная точка "
    "исключена из mTLS и поэтому доступна извне сетки, несмотря на наличие mTLS "
    "в строгом режиме.",
    "You can now point the Dynatrace annotations to this endpoint to scrape "
    "metrics of Istio and the application. If you don't want to scrape the "
    "additional Istio and Envoy metrics, you can exclude them by using the "
    "`metrics.dynatrace.com/filter` annotation and excluding `istio_*` and "
    "`envoy_*` metrics.": "Теперь можно направить аннотации Dynatrace на эту конечную точку, "
    "чтобы собирать метрики Istio и приложения. Если вы не хотите собирать "
    "дополнительные метрики Istio и Envoy, их можно исключить с помощью "
    "аннотации `metrics.dynatrace.com/filter`, исключив метрики `istio_*` и "
    "`envoy_*`.",
    "This way, an ActiveGate outside (or inside) the mesh can scrape the metrics "
    "from pods inside the mesh.": "Таким образом, ActiveGate вне сетки (или внутри неё) может собирать "
    "метрики с подов внутри сетки.",
    "Example of all required annotations:": "Пример всех необходимых аннотаций:",
    "Keep in mind that Istio will rewrite the `prometheus.io/...` annotations to "
    "the generated endpoint and port when applying the above pod. That means that "
    "the resulting pod in the cluster will not match the applied YAML.": "Имейте в виду, что Istio перепишет аннотации `prometheus.io/...` на "
    "сгенерированные конечную точку и порт при применении приведённого выше "
    "пода. Это означает, что итоговый под в кластере не будет соответствовать "
    "применённому YAML.",
    "## Troubleshooting": "## Устранение неполадок",
    "Istio service registry": "Реестр сервисов Istio",
    "You can get all services known to Istio (a service registry) by executing "
    "the following command inside the `pilot` container of the `istiod` pod.": "Получить все известные Istio сервисы (реестр сервисов) можно, выполнив "
    "следующую команду внутри контейнера `pilot` пода `istiod`.",
    "This dumps all known services as JSON. It should contain entries for the "
    "Dynatrace tenant and ActiveGate in the cluster.": "Это выводит все известные сервисы в формате JSON. Он должен содержать "
    "записи для тенанта Dynatrace и ActiveGate в кластере.",
    "If not, check if `enableIstio` is set to `true` in the DynaKube.": "Если нет, проверьте, установлен ли `enableIstio` в `true` в DynaKube.",
    "## Related topics": "## Связанные темы",
    "* [Configure OpenTelemetry tracing with Istio]"
    "(/managed/ingest-from/opentelemetry/integrations/istio "
    '"Learn how to configure Istio on Kubernetes to deploy pre-configured proxy '
    'services for OpenTelemetry tracing.")': "* [Настройка трассировки OpenTelemetry с Istio]"
    "(/managed/ingest-from/opentelemetry/integrations/istio "
    '"Узнайте, как настроить Istio в Kubernetes для развёртывания '
    'предварительно настроенных proxy-сервисов для трассировки OpenTelemetry.")',
}

# Lines copied verbatim (identifier headings / bare tokens). None here.
PASS = set()


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build():
    en_path = os.path.join(BASE, "managed", SUB, FNAME)
    ru_path = os.path.join(BASE, "managed-ru", SUB, FNAME)
    en_lines = read_lf(en_path).split("\n")
    tmap = {MOJI_RE.sub("", k): v for k, v in TRANS.items()}
    passset = {MOJI_RE.sub("", k) for k in PASS}
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
        raise SystemExit(f"[{FNAME}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{FNAME}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {FNAME}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    build()
