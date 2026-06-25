# -*- coding: utf-8 -*-
"""L4-IF.62 G6 builder: setup-on-k8s/guides/networking-security-compliance
network-configurations batch (2 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for empty table headers / separators / bare filenames. Any prose line missing
from both raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain mojibake `﻿`/`ï»¿` before some `]`, and `â`
(stray) inside the TLS section bullet lines; MOJI_RE strips them from both the
EN line and the TRANS keys, so keys match clean and RU stays clean.
"""

import os
import re

# Strip BOM/mojibake fragments the EN sources sprinkle in:
#  - BOM `﻿` / `ï»¿` before some `]`
#  - mis-decoded en/em dash `â\x80\x93` / `â\x80\x94` used as a bullet separator
#    after a backtick identifier (e.g. `server.crt`<dash>Dynatrace ...).
MOJI_RE = re.compile("â[]|[﻿â]|ï»¿")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/networking-security-compliance"

# Per-file relative dir override (network-zones.md lives one level deeper).
REL = {
    "network-zones.md": SUB + "/network-configurations",
}

# ----------------------------------------------------------------------------
TRANS = {
    "network-configurations.md": {
        "title: Network configurations": "title: Сетевые конфигурации",
        "# Network configurations": "# Сетевые конфигурации",
        "* 4-min read": "* Чтение: 4 мин",
        "* Published Mar 25, 2024": "* Опубликовано 25 марта 2024 г.",
        "Configure Dynatrace in network-restricted environments with network "
        "configurations, proxy settings, and URL exclusions.": "Настройте Dynatrace в окружениях с сетевыми ограничениями с помощью "
        "сетевых конфигураций, настроек proxy и исключений URL.",
        "Network zones": "Network zones",
        "For details on setting up and managing network zones, initial endpoint "
        "setup, and advanced configurations in restricted environments, see [Using "
        "network zones in Kubernetes](/managed/ingest-from/setup-on-k8s/guides/"
        "networking-security-compliance/network-configurations/network-zones "
        '"Set up and use network zones in Kubernetes environments with the '
        'Dynatrace Operator.").': "Подробнее о настройке network zones и управлении ими, первоначальной "
        "настройке конечных точек и расширенных конфигурациях в окружениях с "
        "ограничениями см. [Использование network zones в Kubernetes]"
        "(/managed/ingest-from/setup-on-k8s/guides/"
        "networking-security-compliance/network-configurations/network-zones "
        '"Настройка и использование network zones в окружениях Kubernetes с '
        'помощью Dynatrace Operator.").',
        "## Configure proxy": "## Настройка proxy",
        "For Kubernetes Platform Monitoring with Dynatrace, you might need to "
        "configure a proxy, which facilitates all outgoing connections for "
        "Dynatrace Operator components (such as `csi-driver` and `operator`), "
        "OneAgent, and ActiveGate.": "Для мониторинга платформы Kubernetes с Dynatrace вам может "
        "понадобиться настроить proxy, который обеспечивает все исходящие "
        "соединения для компонентов Dynatrace Operator (таких как `csi-driver` "
        "и `operator`), OneAgent и ActiveGate.",
        "Depending on your proxy configuration, especially regarding credentials, "
        "there are two options for configuring your proxy in a DynaKube:": "В зависимости от конфигурации proxy, особенно в части учётных данных, "
        "существует два варианта настройки proxy в DynaKube:",
        "Without proxy credentials": "Без учётных данных proxy",
        "With proxy credentials": "С учётными данными proxy",
        "HTTPS proxies are supported for ActiveGate since version 1.289.": "HTTPS-proxy поддерживаются для ActiveGate начиная с версии 1.289.",
        "HTTPS proxies are supported for OneAgent since version 1.311.": "HTTPS-proxy поддерживаются для OneAgent начиная с версии 1.311.",
        "For proxies without credential requirements, provide your proxy URL in "
        "the `value` field:": "Для proxy, не требующих учётных данных, укажите URL вашего proxy в "
        "поле `value`:",
        "For proxies requiring credentials.": "Для proxy, требующих учётных данных.",
        "1. Create a Kubernetes secret containing your encrypted proxy URL, "
        "including the credentials.": "1. Создайте секрет Kubernetes, содержащий зашифрованный URL вашего "
        "proxy, включая учётные данные.",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "Rules for the proxy password": "Правила для пароля proxy",
        "Ensure the proxy password meets the following criteria:": "Убедитесь, что пароль proxy соответствует следующим критериям:",
        "| Requirements | Corresponding characters |": "| Требования | Соответствующие символы |",
        '| Characters allowed | [A-Za-z0-9] ! " # $ ( ) \\* - . / : ; < > ? @ [ ] ^ \\_ { | } |': '| Допустимые символы | [A-Za-z0-9] ! " # $ ( ) \\* - . / : ; < > ? @ [ ] ^ \\_ { | } |',
        r"| Characters not allowed | blank space ' ` , & = + % \ |": r"| Недопустимые символы | пробел ' ` , & = + % \ |",
        "The password in the custom resource or proxy secret must be URL-encoded. "
        'For example, `password!"#$()*-./:;<>?@[]^_{|}~` becomes '
        "`password!%22%23%24()*-.%2F%3A%3B%3C%3E%3F%40%5B%5D%5E_%7B%7C%7D~`.": "Пароль в пользовательском ресурсе или секрете proxy должен быть "
        'закодирован в формате URL. Например, `password!"#$()*-./:;<>?@[]^_{|}~` '
        "превращается в "
        "`password!%22%23%24()*-.%2F%3A%3B%3C%3E%3F%40%5B%5D%5E_%7B%7C%7D~`.",
        "2. Provide the name of the secret in the `valueFrom` section.": "2. Укажите имя секрета в разделе `valueFrom`.",
        "Dynatrace Operator version 1.0.0+": "Dynatrace Operator версии 1.0.0+",
        "The connection between OneAgent and Dynatrace code modules with ActiveGate "
        "will always bypass the proxy, ensuring direct communication for these "
        "components.": "Соединение между OneAgent, кодовыми модулями Dynatrace и ActiveGate "
        "всегда обходит proxy, обеспечивая прямую связь для этих компонентов.",
        "If you need to bypass the proxy for other reasons, see the next section.": "Если вам нужно обойти proxy по другим причинам, см. следующий раздел.",
        "### Exclude selected URLs from proxy configuration": "### Исключение выбранных URL из конфигурации proxy",
        "To set the list of URLs to exclude from the proxy configuration, add the "
        "following annotation to the DynaKube custom resource.": "Чтобы задать список URL, исключаемых из конфигурации proxy, добавьте "
        "следующую аннотацию в пользовательский ресурс DynaKube.",
        "Dynatrace Operator then excludes the listed URLs from the proxy settings. "
        "This exclusion applies specifically to Dynatrace Operator and the CSI "
        "driver. It doesn't affect the proxy settings for other components managed "
        "by Dynatrace Operator, such as OneAgent or ActiveGate.": "После этого Dynatrace Operator исключает перечисленные URL из настроек "
        "proxy. Это исключение применяется именно к Dynatrace Operator и CSI "
        "driver. Оно не влияет на настройки proxy для других компонентов, "
        "управляемых Dynatrace Operator, таких как OneAgent или ActiveGate.",
        "## Add trusted CA certificates": "## Добавление доверенных CA-сертификатов",
        "### ActiveGate, OneAgent and Dynatrace Operator components": "### Компоненты ActiveGate, OneAgent и Dynatrace Operator",
        "To add trusted CA certificates to ActiveGate, OneAgent and/or Dynatrace "
        "Operator, the certificates must be provided via a Kubernetes ConfigMap "
        "referenced in your DynaKube configuration.": "Чтобы добавить доверенные CA-сертификаты в ActiveGate, OneAgent и/или "
        "Dynatrace Operator, сертификаты необходимо предоставить через ConfigMap "
        "Kubernetes, на который ссылается ваша конфигурация DynaKube.",
        "1. Create a ConfigMap (replace `<ca-certificates>` with the CA "
        "certificates to be trusted).": "1. Создайте ConfigMap (замените `<ca-certificates>` на CA-сертификаты, "
        "которым нужно доверять).",
        "For example:": "Например:",
        "2. Apply the ConfigMap to your cluster.": "2. Примените ConfigMap к вашему кластеру.",
        "3. In your DynaKube, reference the ConfigMap in the `trustedCAs` field.": "3. В вашем DynaKube сошлитесь на ConfigMap в поле `trustedCAs`.",
        "4. Apply the DynaKube configuration to your cluster.": "4. Примените конфигурацию DynaKube к вашему кластеру.",
        "### Use `skipCertCheck` to bypass certificate verification": "### Использование `skipCertCheck` для обхода проверки сертификата",
        "To ignore certificate verification for Dynatrace Operator components "
        "(`operator` and `csi-driver`), set `skipCertCheck` in your DynaKube "
        "configuration. This setting should only be used if the custom certificate "
        "authority is unknown or can't be provided to Dynatrace Operator via the "
        "`trustedCAs` field.": "Чтобы игнорировать проверку сертификата для компонентов Dynatrace "
        "Operator (`operator` и `csi-driver`), задайте `skipCertCheck` в вашей "
        "конфигурации DynaKube. Эту настройку следует использовать только в том "
        "случае, если пользовательский удостоверяющий центр неизвестен или не "
        "может быть предоставлен Dynatrace Operator через поле `trustedCAs`.",
        "In Dynatrace Operator version 1.0.0 and earlier, the `skipCertCheck` "
        "setting was not applied during the image pulling process.": "В Dynatrace Operator версии 1.0.0 и более ранних настройка "
        "`skipCertCheck` не применялась в процессе загрузки образа.",
        "## Configure a server TLS certificate for ActiveGate": "## Настройка серверного TLS-сертификата для ActiveGate",
        "By default, ActiveGate uses a self-signed certificate, which can be "
        "replaced by a self-managed certificate as described in [Custom SSL "
        "certificate for ActiveGate](/managed/ingest-from/dynatrace-activegate/"
        "configuration/configure-custom-ssl-certificate-on-activegate "
        '"Learn how to configure the SSL certificate on your ActiveGate.").': "По умолчанию ActiveGate использует самоподписанный сертификат, который "
        "можно заменить самостоятельно управляемым сертификатом, как описано в "
        "разделе [Пользовательский SSL-сертификат для ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/"
        "configuration/configure-custom-ssl-certificate-on-activegate "
        '"Узнайте, как настроить SSL-сертификат на вашем ActiveGate.").',
        "To configure a server TLS certificate for the ActiveGate:": "Чтобы настроить серверный TLS-сертификат для ActiveGate:",
        "1. Create the [Kubernetes Opaque secret](https://dt-url.net/zm03qza) "
        "holding the ActiveGate certificate(s) and ActiveGate private key.": "1. Создайте [секрет Kubernetes типа Opaque](https://dt-url.net/zm03qza), "
        "содержащий сертификат(ы) ActiveGate и закрытый ключ ActiveGate.",
        "Where:": "Где:",
        "* `server.crt`Dynatrace Operator propagates ActiveGate certificate(s) "
        "from the file to OneAgents.": "* `server.crt`: Dynatrace Operator распространяет сертификат(ы) "
        "ActiveGate из файла на OneAgent.",
        "* `server.p12`ActiveGate certificate(s) and ActiveGate private key, "
        "ActiveGate reads the file and configures itself to use the provided "
        "private key and certificates.": "* `server.p12`: сертификат(ы) ActiveGate и закрытый ключ ActiveGate; "
        "ActiveGate читает файл и настраивается на использование предоставленного "
        "закрытого ключа и сертификатов.",
        "* `password`ActiveGate reads it and uses it to decrypt the `server.p12` "
        "file.": "* `password`: ActiveGate читает его и использует для расшифровки файла "
        "`server.p12`.",
        "`server.12` and `server.crt` files should contain the same "
        "certificate(s).": "Файлы `server.12` и `server.crt` должны содержать одни и те же "
        "сертификат(ы).",
        "2. Provide the name of the secret via the `tlsSecretName` field.": "2. Укажите имя секрета через поле `tlsSecretName`.",
    },
    "network-zones.md": {
        "title: Using network zones in Kubernetes": "title: Использование network zones в Kubernetes",
        "# Using network zones in Kubernetes": "# Использование network zones в Kubernetes",
        "* 5-min read": "* Чтение: 5 мин",
        "* Published Mar 25, 2024": "* Опубликовано 25 марта 2024 г.",
        "This page describes how to effectively use network zones within Kubernetes "
        "environments, emphasizing their configuration through DynaKube.": "На этой странице описано, как эффективно использовать network zones в "
        "окружениях Kubernetes, с акцентом на их настройку через DynaKube.",
        "To ensure a seamless setup process, we strongly advise you to thoroughly "
        "review this guide before making any configuration efforts. By doing so, "
        "network admins can gain a solid understanding of the prerequisites and "
        "steps involved, ensuring a successful deployment.": "Чтобы обеспечить бесперебойный процесс настройки, настоятельно "
        "рекомендуем внимательно изучить это руководство, прежде чем приступать к "
        "настройке. Это позволит сетевым администраторам получить чёткое "
        "понимание предварительных требований и необходимых шагов, обеспечивая "
        "успешное развёртывание.",
        "We assume a foundational understanding of network zones. See the following "
        "links for background information:": "Предполагается, что вы обладаете базовым пониманием network zones. "
        "Справочную информацию см. по следующим ссылкам:",
        '* [Network zones introduction](/managed/manage/network-zones "Find out '
        'how network zones work in Dynatrace.") and [basic information]'
        '(/managed/manage/network-zones/network-zones-basic-info#activate "Learn '
        'how to get started with network zones.")': '* [Введение в network zones](/managed/manage/network-zones "Узнайте, '
        'как network zones работают в Dynatrace.") и [базовая информация]'
        "(/managed/manage/network-zones/network-zones-basic-info#activate "
        '"Узнайте, как начать работу с network zones.")',
        '* [OneAgent](/managed/manage/network-zones/oneagent-connectivity "Find '
        "out how network zones prioritize ActiveGates for OneAgent "
        'connectivity.") and [ActiveGate](/managed/manage/network-zones/'
        'activegate-connectivity "Find out how network zones prioritize '
        'ActiveGates for Environment ActiveGate connectivity.") connectivity': "* Подключение [OneAgent](/managed/manage/network-zones/"
        'oneagent-connectivity "Узнайте, как network zones приоритизируют '
        'ActiveGate для подключения OneAgent.") и [ActiveGate]'
        '(/managed/manage/network-zones/activegate-connectivity "Узнайте, как '
        "network zones приоритизируют ActiveGate для подключения Environment "
        'ActiveGate.")',
        "## Network zones in Kubernetes environments": "## Network zones в окружениях Kubernetes",
        "Network zones are instrumental in managing and directing traffic flow "
        "among Dynatrace components, ensuring efficient communication within the "
        "network, whether in Kubernetes environments or traditional setups. By "
        "leveraging network zones, network admins can optimize traffic flow and "
        "accommodate environments with stringent network restrictions, such as "
        "limited egress capabilities.": "Network zones играют важную роль в управлении и направлении потоков "
        "трафика между компонентами Dynatrace, обеспечивая эффективную связь "
        "внутри сети, будь то в окружениях Kubernetes или в традиционных "
        "развёртываниях. Используя network zones, сетевые администраторы могут "
        "оптимизировать поток трафика и поддерживать окружения со строгими "
        "сетевыми ограничениями, например с ограниченными возможностями "
        "исходящего трафика.",
        "Network zones for Dynatrace components deployed on Kubernetes can easily "
        "be configured via the DynaKube custom resource, enabling tailored and "
        "effective network management.": "Network zones для компонентов Dynatrace, развёрнутых в Kubernetes, "
        "легко настраиваются через пользовательский ресурс DynaKube, что "
        "обеспечивает адаптированное и эффективное управление сетью.",
        "## Set up network zones": "## Настройка network zones",
        "This section categorizes setups into two distinct scenarios based on their "
        "characteristics:": "В этом разделе варианты настройки разделены на два отдельных сценария "
        "в зависимости от их характеристик:",
        "* [Kubernetes cluster with non-restricted egress]"
        "(#kubernetes-cluster-with-non-restricted-egress)": "* [Кластер Kubernetes с неограниченным исходящим трафиком]"
        "(#kubernetes-cluster-with-non-restricted-egress)",
        "* [Kubernetes cluster with restricted egress]"
        "(#kubernetes-cluster-with-restricted-egress)": "* [Кластер Kubernetes с ограниченным исходящим трафиком]"
        "(#kubernetes-cluster-with-restricted-egress)",
        "### Kubernetes cluster with non-restricted egress": "### Кластер Kubernetes с неограниченным исходящим трафиком",
        "In Kubernetes clusters without egress restrictions, the main purposes of "
        "network zones are to:": "В кластерах Kubernetes без ограничений исходящего трафика основные цели "
        "network zones следующие:",
        "* Efficiently direct traffic to prevent unnecessary global routing": "* Эффективно направлять трафик, чтобы предотвратить излишнюю "
        "глобальную маршрутизацию",
        "* Filter unreachable endpoints": "* Фильтровать недоступные конечные точки",
        "The adoption of network zones is therefore widely recommended for optimal "
        "traffic management of Dynatrace components.": "Поэтому использование network zones широко рекомендуется для "
        "оптимального управления трафиком компонентов Dynatrace.",
        "1. Configure a network zone by setting the `networkZone` field and make "
        "sure an ActiveGate is rolled out as part of the DynaKube configuration. "
        "The specified network zone will be automatically applied to rolled out "
        "ActiveGates and OneAgents by the Dynatrace Operator.": "1. Настройте network zone, задав поле `networkZone`, и убедитесь, что "
        "ActiveGate развёрнут в рамках конфигурации DynaKube. Указанная network "
        "zone будет автоматически применена к развёрнутым ActiveGate и OneAgent "
        "оператором Dynatrace Operator.",
        "2. Apply the DynaKube CR to the Kubernetes API.": "2. Примените DynaKube CR к Kubernetes API.",
        "After applying, the Dynatrace Operator will roll out Dynatrace components "
        "according the DynaKube configuration. As part of the rollout, ActiveGates "
        "and OneAgents receive available endpoints according to the specified "
        "network zone (with fallback mode *Any ActiveGate*) and can start "
        "communicating independently of each other's rollout status.": "После применения Dynatrace Operator развернёт компоненты Dynatrace в "
        "соответствии с конфигурацией DynaKube. В рамках развёртывания ActiveGate "
        "и OneAgent получают доступные конечные точки в соответствии с указанной "
        "network zone (с режимом резервирования *Any ActiveGate*) и могут "
        "начинать обмен данными независимо от статуса развёртывания друг друга.",
        "In this scenario, it is not required to manually create the network zone "
        "before applying the DynaKube custom resource, as network egress is not "
        "restricted. Creation of the network zone happens implicitly when the "
        "ActiveGate registers itself with the Dynatrace cluster, with *Any "
        "ActiveGate* configured as [fallback mode]"
        "(/managed/manage/network-zones/network-zones-basic-info#fallback-mode "
        '"Learn how to get started with network zones.").': "В этом сценарии не требуется вручную создавать network zone перед "
        "применением пользовательского ресурса DynaKube, поскольку исходящий "
        "трафик не ограничен. Создание network zone происходит неявно, когда "
        "ActiveGate регистрируется в кластере Dynatrace, при этом в качестве "
        "[режима резервирования]"
        "(/managed/manage/network-zones/network-zones-basic-info#fallback-mode "
        '"Узнайте, как начать работу с network zones.") настроен *Any '
        "ActiveGate*.",
        "### Kubernetes cluster with restricted egress": "### Кластер Kubernetes с ограниченным исходящим трафиком",
        "In Kubernetes clusters that enforce restricted egress, typically, only "
        "whitelisted components are permitted to interact with external networks. "
        "For Dynatrace, the ActiveGate is designed for this use case and serves as "
        "this crucial gateway component able to centralize all outbound "
        "communications towards the Dynatrace Cluster.": "В кластерах Kubernetes с принудительным ограничением исходящего "
        "трафика, как правило, только компоненты из списка разрешённых могут "
        "взаимодействовать с внешними сетями. В Dynatrace для этого сценария "
        "предназначен ActiveGate, который выступает в роли этого ключевого "
        "шлюзового компонента, способного централизовать все исходящие соединения "
        "к Dynatrace Cluster.",
        "Given that all Dynatrace components must communicate exclusively through "
        "the whitelisted ActiveGate, it is imperative that the network zone is "
        "configured to support this requirement. Hence, the network zone needs to "
        "ensure that only ActiveGates within the specified network zone are "
        "provided for communication, without resorting to any fallback options. To "
        "achieve that, the network zone must be created upfront with *None* as the "
        "fallback mode to prevent a lockdown of Dynatrace monitoring components.": "Поскольку все компоненты Dynatrace должны взаимодействовать "
        "исключительно через ActiveGate из списка разрешённых, крайне важно, "
        "чтобы network zone была настроена с учётом этого требования. Поэтому "
        "network zone должна гарантировать, что для связи предоставляются только "
        "ActiveGate в пределах указанной network zone, без обращения к каким-либо "
        "вариантам резервирования. Для этого network zone необходимо создать "
        "заранее с режимом резервирования *None*, чтобы предотвратить блокировку "
        "компонентов мониторинга Dynatrace.",
        "Dynatrace Operator version 0.14.0+ postpones OneAgent rollout and "
        "injection until at least one ActiveGate becomes available. Once an "
        "ActiveGate is available, OneAgents are deployed and OneAgent injection is "
        "performed. Application pods that have not been injected due to the "
        "postponement need to be manually restarted.": "Dynatrace Operator версии 0.14.0+ откладывает развёртывание и "
        "внедрение OneAgent до тех пор, пока не станет доступен хотя бы один "
        "ActiveGate. Как только ActiveGate становится доступен, OneAgent "
        "развёртываются и выполняется внедрение OneAgent. Поды приложений, в "
        "которые внедрение не было выполнено из-за отсрочки, необходимо "
        "перезапустить вручную.",
        "Additionally, it may be necessary to also [configure a proxy]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'network-configurations#configure-proxy "Configure Dynatrace in '
        "network-restricted environments, network-related settings and proxy "
        'configurations.") to facilitate controlled network access in Kubernetes '
        "clusters with restricted egress.": "Кроме того, может потребоваться также [настроить proxy]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'network-configurations#configure-proxy "Настройка Dynatrace в '
        "окружениях с сетевыми ограничениями, связанных с сетью параметров и "
        'конфигураций proxy.") для обеспечения контролируемого сетевого доступа '
        "в кластерах Kubernetes с ограниченным исходящим трафиком.",
        "1. Run the following command to create a network zone in fallback mode "
        "*None* using the [Dynatrace API](/managed/dynatrace-api/environment-api/"
        'network-zones/put-network-zone "Update a network zone via the Dynatrace '
        'API.").': "1. Выполните следующую команду, чтобы создать network zone с режимом "
        "резервирования *None* с помощью [Dynatrace API]"
        "(/managed/dynatrace-api/environment-api/"
        'network-zones/put-network-zone "Обновление network zone через '
        'Dynatrace API.").',
        "The API token must have the `networkZones.write` permission assigned.": "API-токену должно быть назначено разрешение `networkZones.write`.",
        "2. Configure a network zone by setting the `networkZone` field and make "
        "sure an ActiveGate is rolled out as part of the DynaKube configuration.": "2. Настройте network zone, задав поле `networkZone`, и убедитесь, что "
        "ActiveGate развёрнут в рамках конфигурации DynaKube.",
        "3. Apply the DynaKube CR to the Kubernetes API.": "3. Примените DynaKube CR к Kubernetes API.",
        "After deploying, Dynatrace Operator performs the following steps.": "После развёртывания Dynatrace Operator выполняет следующие шаги.",
        "1. Deploy ActiveGates.": "1. Развёртывает ActiveGate.",
        "2. Poll Dynatrace cluster for available ActiveGates in a certain interval "
        "until an ActiveGate becomes available.": "2. Опрашивает кластер Dynatrace на наличие доступных ActiveGate через "
        "определённый интервал, пока ActiveGate не станет доступен.",
        "3. Deploy OneAgents with available communication endpoints.": "3. Развёртывает OneAgent с доступными конечными точками связи.",
        "4. Perform OneAgent injection into application pods.": "4. Выполняет внедрение OneAgent в поды приложений.",
        "Application pods that have not been injected due to the postponement need "
        "to be manually restarted.": "Поды приложений, в которые внедрение не было выполнено из-за отсрочки, "
        "необходимо перезапустить вручную.",
        "Troubleshooting OneAgent injection of application pods": "Устранение неполадок внедрения OneAgent в поды приложений",
        "If application pods start before an ActiveGate becomes available, "
        "Dynatrace Operator skips OneAgent injection. This way, startup of "
        "applications won't be delayed, but applications will not be deeply "
        "monitored.": "Если поды приложений запускаются до того, как ActiveGate становится "
        "доступен, Dynatrace Operator пропускает внедрение OneAgent. Таким "
        "образом запуск приложений не задерживается, но приложения не будут "
        "глубоко мониториться.",
        "The following reasons can lead to skipped OneAgent injection:": "К пропуску внедрения OneAgent могут приводить следующие причины:",
        "* ActiveGates are still starting and none is yet registered with the "
        "Dynatrace cluster.": "* ActiveGate всё ещё запускаются, и ни один из них пока не "
        "зарегистрирован в кластере Dynatrace.",
        "* ActiveGates are crashing due to misconfiguration.": "* ActiveGate аварийно завершают работу из-за неправильной настройки.",
        "Dynatrace Operator adds the following annotations to every pod in case of "
        "skipped OneAgent injection:": "В случае пропуска внедрения OneAgent Dynatrace Operator добавляет "
        "следующие аннотации к каждому поду:",
        "Alternatively, Dynatrace Operator logs can be analyzed for skipped "
        "OneAgent injections.": "Кроме того, для выявления пропущенных внедрений OneAgent можно "
        "проанализировать логи Dynatrace Operator.",
        "## Related topics": "## Связанные темы",
        "* [Get started with network zones]"
        '(/managed/manage/network-zones/network-zones-basic-info "Learn how to '
        'get started with network zones.")': "* [Начало работы с network zones]"
        '(/managed/manage/network-zones/network-zones-basic-info "Узнайте, как '
        'начать работу с network zones.")',
        '* [Network zones](/managed/manage/network-zones "Find out how network '
        'zones work in Dynatrace.")': '* [Network zones](/managed/manage/network-zones "Узнайте, как network '
        'zones работают в Dynatrace.")',
    },
}

# Lines copied verbatim (empty table headers / separators / bare filenames).
PASS = {
    "network-configurations.md": {
        "| --- | --- |",
    },
    "network-zones.md": set(),
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
