# -*- coding: utf-8 -*-
"""L4-IF.57 builder: setup-on-k8s/guides/container-registries batch (5 files).

Derives RU from EN line-by-line (code-fence-aware), same guarantees as
_build_haf_l4if56.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for technical table rows / image refs / footnote numbers. Any prose line missing
from both raises -> catches leftover-EN.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
GUIDES = "ingest-from/setup-on-k8s/guides"
SUB = GUIDES + "/container-registries"

# container-registries.md is the index page in guides/; the rest live in
# guides/container-registries/.
REL = {
    "container-registries.md": GUIDES,
}

# ----------------------------------------------------------------------------
TRANS = {
    "container-registries.md": {
        "title: Container registries": "title: Реестры контейнеров",
        "# Container registries": "# Реестры контейнеров",
        "* 2-min read": "* Чтение: 2 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "To prioritize seamless integration with your tooling and adaptability to "
        "your needs, we offer our container images in various ways to maximize flexibility:": "Чтобы обеспечить бесшовную интеграцию с вашими инструментами и "
        "адаптируемость под ваши потребности, мы предлагаем образы контейнеров "
        "несколькими способами для максимальной гибкости:",
        "* Dynatrace built-in registry default": "* Встроенный реестр Dynatrace по умолчанию",
        "* Public registries": "* Публичные реестры",
        "* Bring your own private registry Recommended": "* Используйте собственный частный реестр Рекомендуется",
        "## Dynatrace built-in registry": "## Встроенный реестр Dynatrace",
        "default": "по умолчанию",
        "As the default behavior, Dynatrace Operator retrieves images from the "
        "built-in Dynatrace registry, prioritizing convenience and minimizing "
        "configuration complexities for cloud-native monitoring setup.": "По умолчанию Dynatrace Operator получает образы из встроенного реестра "
        "Dynatrace, отдавая приоритет удобству и сводя к минимуму сложность "
        "настройки для cloud-native мониторинга.",
        "Nevertheless, the concurrent retrieval of multiple images from the "
        "Dynatrace built-in registry raises the potential for rate limiting. We "
        "therefore recommend using our endorsed public registries or, ideally, "
        "establishing your private registry. Leveraging public and private "
        "registries enhances operational efficiency and performance, particularly "
        "under high-demand conditions.": "Тем не менее одновременное получение нескольких образов из встроенного "
        "реестра Dynatrace повышает вероятность ограничения частоты запросов. "
        "Поэтому мы рекомендуем использовать одобренные нами публичные реестры "
        "или, что предпочтительнее, создать собственный частный реестр. "
        "Использование публичных и частных реестров повышает операционную "
        "эффективность и производительность, особенно при высокой нагрузке.",
        "## Public registries": "## Публичные реестры",
        "To accommodate diverse infrastructure requirements and organizational "
        "preferences, Dynatrace images are available on [selected public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry"). These images adhere to best practices, ensuring '
        "immutability and signing for enhanced security and resilience against "
        "potential supply chain risks.": "Чтобы удовлетворить разнообразные требования к инфраструктуре и "
        "организационные предпочтения, образы Dynatrace доступны в [избранных "
        "публичных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра"). Эти образы соответствуют лучшим '
        "практикам, обеспечивая неизменяемость и подписание для повышения "
        "безопасности и устойчивости к потенциальным рискам цепочки поставок.",
        "If you seek greater control over your image hosting environment, Dynatrace "
        "offers the option to replicate images and signatures to private registries.": "Если вам нужен больший контроль над средой размещения образов, Dynatrace "
        "предлагает возможность реплицировать образы и подписи в частные реестры.",
        "## Bring your own private registry": "## Используйте собственный частный реестр",
        "Recommended": "Рекомендуется",
        "For optimal performance in high-demand and dynamic environments, we "
        "recommend using a [private registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry"). Furthermore, to meet security standards and '
        "ensure software integrity while mitigating supply chain risks, image "
        "scanning and [signature verification]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Verify Dynatrace image signatures") against Dynatrace images are recommended.': "Для оптимальной производительности в условиях высокой нагрузки и "
        "динамичных сред мы рекомендуем использовать [частный реестр]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра"). Кроме того, для соответствия '
        "стандартам безопасности и обеспечения целостности ПО при снижении рисков "
        "цепочки поставок рекомендуется сканирование образов и [проверка подписей]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Проверка подписей образов Dynatrace") образов Dynatrace.',
        "By replicating Dynatrace images to your private registry, you can "
        "seamlessly merge excellent delivery performance with the assurance of "
        "secure, signed, and immutable images.": "Реплицируя образы Dynatrace в свой частный реестр, вы "
        "беспрепятственно сочетаете отличную производительность доставки с "
        "гарантией безопасных, подписанных и неизменяемых образов.",
        "## Learn more": "## Узнать больше",
        "[### Use Dynatrace public registry": "[### Использование публичного реестра Dynatrace",
        "Configure Dynatrace Operator and DynaKube to use images from our supported "
        "public registries.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Use a public registry")[### Use your own private registry': "Настройте Dynatrace Operator и DynaKube на использование образов из "
        "поддерживаемых нами публичных реестров.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Использование публичного реестра")[### Использование собственного частного реестра',
        "Configure Dynatrace Operator and DynaKube to use images from your own "
        "private registry.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry")[### Store Dynatrace images in private registries': "Настройте Dynatrace Operator и DynaKube на использование образов из "
        "вашего собственного частного реестра.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра")[### Хранение образов Dynatrace в частных реестрах',
        "Learn how to replicate Dynatrace images into your private registries.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Store Dynatrace images in private registries")[### Verify Dynatrace image signatures': "Узнайте, как реплицировать образы Dynatrace в ваши частные реестры.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Хранение образов Dynatrace в частных реестрах")[### Проверка подписей образов Dynatrace',
        "Verify Dynatrace image signatures to ensure integrity and secure software "
        "supply chain.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Verify Dynatrace image signatures")': "Проверяйте подписи образов Dynatrace, чтобы обеспечить целостность и "
        "безопасную цепочку поставок ПО.]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Проверка подписей образов Dynatrace")',
    },
    "use-public-registry.md": {
        "title: Use a public registry": "title: Использование публичного реестра",
        "# Use a public registry": "# Использование публичного реестра",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "To accommodate diverse infrastructure requirements and organizational "
        "preferences, Dynatrace images are available on selected public registries. "
        "These images adhere to best practices, ensuring immutability and signing "
        "for enhanced security and resilience against potential supply chain risks.": "Чтобы удовлетворить разнообразные требования к инфраструктуре и "
        "организационные предпочтения, образы Dynatrace доступны в избранных "
        "публичных реестрах. Эти образы соответствуют лучшим практикам, "
        "обеспечивая неизменяемость и подписание для повышения безопасности и "
        "устойчивости к потенциальным рискам цепочки поставок.",
        "Explore our supported public registries with multi-arch Dynatrace "
        "container images supporting ARM64 (AArch64), x86-64, s390x, and PPC64le CPU "
        "architectures on Linux, ensuring compatibility across various platforms.": "Ознакомьтесь с поддерживаемыми нами публичными реестрами, где размещены "
        "мультиархитектурные образы контейнеров Dynatrace с поддержкой архитектур "
        "ЦП ARM64 (AArch64), x86-64, s390x и PPC64le на Linux, что обеспечивает "
        "совместимость с различными платформами.",
        "This page provides instructions for using Dynatrace signed and immutable "
        "container images hosted on supported public registries.": "На этой странице приведены инструкции по использованию подписанных и "
        "неизменяемых образов контейнеров Dynatrace, размещённых в поддерживаемых "
        "публичных реестрах.",
        "## Prerequisites": "## Предварительные требования",
        "Before you begin, be sure to meet the following prerequisites:": "Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:",
        "* Required Dynatrace Operator version is v0.11 or later": "* Обязательно Версия Dynatrace Operator: v0.11 или новее",
        "* Required Target CPU architectures are ARM64 (AArch64), x86-64, s390x, and/or ppc64le": "* Обязательно Целевые архитектуры ЦП: ARM64 (AArch64), x86-64, s390x и/или ppc64le",
        "* Required Allow egress traffic to public registry": "* Обязательно Разрешите исходящий трафик к публичному реестру",
        "#### Limitations": "#### Ограничения",
        "Note that the following configurations are not supported in combination "
        "with public registries:": "Обратите внимание, что следующие конфигурации не поддерживаются в "
        "сочетании с публичными реестрами:",
        "* Application monitoring without CSI driver": "* Application monitoring без CSI-драйвера",
        "* Host monitoring without CSI driver": "* Host monitoring без CSI-драйвера",
        "* Classic Full-Stack monitoring - Alternatively, use a private registry for "
        "[Classic Full-Stack monitoring]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#classic-full-stack "
        '"Store Dynatrace images in private registries")': "* Classic Full-Stack monitoring. В качестве альтернативы используйте "
        "частный реестр для [Classic Full-Stack monitoring]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#classic-full-stack "
        '"Хранение образов Dynatrace в частных реестрах")',
        "Start using these fortified images today for a safer and more efficient "
        "containerized monitoring experience:": "Начните использовать эти защищённые образы уже сегодня для более "
        "безопасного и эффективного мониторинга в контейнерах:",
        "* [Deploy Dynatrace Operator](#deploy-dynatrace-operator-with-images-from-public-registry) "
        "with container images from a public registry": "* [Разверните Dynatrace Operator](#deploy-dynatrace-operator-with-images-from-public-registry) "
        "с образами контейнеров из публичного реестра",
        "* [Configure DynaKube](#configure-dynakube-to-use-images-from-public-registry) "
        "to use container images from a public registry for monitoring components": "* [Настройте DynaKube](#configure-dynakube-to-use-images-from-public-registry) "
        "на использование образов контейнеров из публичного реестра для компонентов мониторинга",
        "## Supported public registries": "## Поддерживаемые публичные реестры",
        "Dynatrace publishes its container images to [Amazon ECR]"
        "(https://gallery.ecr.aws/dynatrace) and [Docker Hub](https://hub.docker.com/u/dynatrace):": "Dynatrace публикует свои образы контейнеров в [Amazon ECR]"
        "(https://gallery.ecr.aws/dynatrace) и [Docker Hub](https://hub.docker.com/u/dynatrace):",
        "Available from Dynatrace Operator version 1.0.0": "Доступно с версии Dynatrace Operator 1.0.0",
        "Rate limiting": "Ограничение частоты запросов",
        "Be aware that, when accessing public registries, there is a potential risk "
        "of encountering rate limiting. To ensure a smoother experience and reduce "
        "this risk, we recommend using a private registry or authenticating against "
        "the respective registry.": "Учтите, что при обращении к публичным реестрам существует потенциальный "
        "риск столкнуться с ограничением частоты запросов. Чтобы обеспечить более "
        "стабильную работу и снизить этот риск, мы рекомендуем использовать частный "
        "реестр или проходить аутентификацию в соответствующем реестре.",
        "Image tagging": "Тегирование образов",
        "Dynatrace employs version-based image tagging for its container images and "
        "does **not** use mutable image tags like `latest`. For more information on "
        "tags, please visit the respective public registry repository.": "Dynatrace применяет тегирование образов на основе версий и **не** "
        "использует изменяемые теги образов, такие как `latest`. Дополнительные "
        "сведения о тегах см. в репозитории соответствующего публичного реестра.",
        "## Deploy Dynatrace Operator with images from public registry": "## Развёртывание Dynatrace Operator с образами из публичного реестра",
        "By default, the Dynatrace Operator image `dynatrace/dynatrace-operator` is "
        "served by the public registry on AWS ECR.": "По умолчанию образ Dynatrace Operator `dynatrace/dynatrace-operator` "
        "предоставляется публичным реестром на AWS ECR.",
        "Dynatrace Operator consists of multiple components (operator, webhook, CSI "
        "driver), all of which use the same `dynatrace-operator` image with specific "
        "deployment configurations per component.": "Dynatrace Operator состоит из нескольких компонентов (operator, webhook, "
        "CSI driver), каждый из которых использует один и тот же образ "
        "`dynatrace-operator` со специфичной конфигурацией развёртывания для "
        "каждого компонента.",
        "If you are using Helm version 4.0+, you must use `--rollback-on-failure` "
        "instead of the `--atomic` flag.": "Если вы используете Helm версии 4.0+, необходимо указывать "
        "`--rollback-on-failure` вместо флага `--atomic`.",
        "The following command installs Dynatrace Operator and configures container "
        "images to be pulled from a public registry:": "Следующая команда устанавливает Dynatrace Operator и настраивает загрузку "
        "образов контейнеров из публичного реестра:",
        "Alternatively, an existing installation can be upgraded as follows:": "Кроме того, существующую установку можно обновить следующим образом:",
        "Use the following kustomization to conveniently install or update Dynatrace "
        "Operator by applying the necessary manifests.": "Используйте следующую kustomization, чтобы удобно установить или обновить "
        "Dynatrace Operator, применив необходимые манифесты.",
        "To avoid tedious and error-prone editing of large YAML files, we recommend "
        "using either Helm or Kustomize for manifest manipulation.": "Чтобы избежать утомительного и подверженного ошибкам редактирования "
        "больших YAML-файлов, мы рекомендуем использовать Helm или Kustomize для "
        "работы с манифестами.",
        "If you prefer to make your modifications directly, however, be sure to "
        "adjust the `image` fields on all containers and pods where the "
        "`dynatrace-operator` image occurs.": "Если же вы предпочитаете вносить изменения напрямую, обязательно "
        "скорректируйте поля `image` во всех контейнерах и подах, где встречается "
        "образ `dynatrace-operator`.",
        "## Configure DynaKube to use images from public registry": "## Настройка DynaKube на использование образов из публичного реестра",
        "**Classic Full-Stack** monitoring is not supported in combination with a "
        "public registry.": "Мониторинг **Classic Full-Stack** не поддерживается в сочетании с "
        "публичным реестром.",
        "For PPC64le architecture, additional configuration is required. For "
        "details, see [ActiveGate container image]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "
        '"Deploy a containerized ActiveGate.").': "Для архитектуры PPC64le требуется дополнительная настройка. Подробнее см. "
        "[Образ контейнера ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "
        '"Развёртывание контейнеризированного ActiveGate.").',
        "The Dynatrace Operator can easily be instructed to use images from a public "
        "registry by configuring the respective `image` fields in the DynaKube "
        "custom resource. The configured images will be deployed to your Kubernetes "
        "cluster to set up monitoring components.": "Dynatrace Operator можно легко настроить на использование образов из "
        "публичного реестра, задав соответствующие поля `image` в пользовательском "
        "ресурсе DynaKube. Настроенные образы будут развёрнуты в вашем кластере "
        "Kubernetes для настройки компонентов мониторинга.",
        "The following DynaKube snippet demonstrates how to configure [Cloud-Native "
        "Full-Stack monitoring setup](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"In-depth description on how the deployment on Kubernetes works.") '
        "leveraging the public Amazon ECR registry.": "Следующий фрагмент DynaKube демонстрирует, как настроить [Cloud-Native "
        "Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"Подробное описание того, как работает развёртывание в Kubernetes.") с '
        "использованием публичного реестра Amazon ECR.",
        "Note that the `version` field has no effect when the `image` and/or "
        "`codeModulesImage` fields are set.": "Обратите внимание, что поле `version` не действует, если заданы поля "
        "`image` и/или `codeModulesImage`.",
        "After configuring the required fields, the DynaKube custom resource must be "
        "applied to the Kubernetes cluster.": "После настройки необходимых полей пользовательский ресурс DynaKube нужно "
        "применить к кластеру Kubernetes.",
        "Looking for more examples?": "Нужно больше примеров?",
        "#### Application and Kubernetes Observability with Amazon ECR": "#### Application and Kubernetes Observability с Amazon ECR",
        "The following custom resource describes how to configure DynaKube for "
        "[Application Observability and Kubernetes observability]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Deploy Dynatrace Operator on Kubernetes"):': "Следующий пользовательский ресурс описывает, как настроить DynaKube для "
        "[Application Observability и Kubernetes observability]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Развёртывание Dynatrace Operator в Kubernetes"):',
        "## Verify image signature": "## Проверка подписи образа",
        "All of our immutable and signed container images adhere to best practices, "
        "enhancing security and shielding against supply chain attacks. To learn how "
        "to verify signatures and guarantee software integrity, see [Verify "
        "Dynatrace image signatures]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Verify Dynatrace image signatures").': "Все наши неизменяемые и подписанные образы контейнеров соответствуют "
        "лучшим практикам, повышая безопасность и защищая от атак на цепочку "
        "поставок. О том, как проверять подписи и гарантировать целостность ПО, см. "
        "[Проверка подписей образов Dynatrace]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Проверка подписей образов Dynatrace").',
        "## Related topics": "## Связанные темы",
        "* [Use a private registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry")': "* [Использование частного реестра]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра")',
        "* [Store Dynatrace images in private registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Store Dynatrace images in private registries")': "* [Хранение образов Dynatrace в частных реестрах]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Хранение образов Dynatrace в частных реестрах")',
    },
    "use-private-registry.md": {
        "title: Use a private registry": "title: Использование частного реестра",
        "# Use a private registry": "# Использование частного реестра",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Jan 27, 2026": "* Обновлено 27 января 2026 г.",
        "For users seeking greater control over their image hosting environment, "
        "Dynatrace offers the option to replicate images and signatures to private "
        "registries.": "Для пользователей, которым нужен больший контроль над средой размещения "
        "образов, Dynatrace предлагает возможность реплицировать образы и подписи в "
        "частные реестры.",
        "We recommend using a private registry for optimal performance and no rate "
        "limiting risks in high-demand and dynamic environments. Furthermore, to "
        "meet security standards and ensure software integrity while mitigating "
        "supply chain risks, image scanning and signature verification against "
        "Dynatrace images can be applied and is recommended.": "Мы рекомендуем использовать частный реестр для оптимальной "
        "производительности и отсутствия рисков ограничения частоты запросов в "
        "условиях высокой нагрузки и динамичных сред. Кроме того, для соответствия "
        "стандартам безопасности и обеспечения целостности ПО при снижении рисков "
        "цепочки поставок можно применять сканирование образов и проверку подписей "
        "образов Dynatrace, что и рекомендуется.",
        "By replicating Dynatrace images to your private registry, you can "
        "seamlessly merge excellent delivery performance with the assurance of "
        "secure, signed, and immutable images. Additionally, we provide multi-arch "
        "images to ensure compatibility across various platforms supporting ARM64 "
        "(AArch64) and x86-64 CPU architectures on Linux.": "Реплицируя образы Dynatrace в свой частный реестр, вы "
        "беспрепятственно сочетаете отличную производительность доставки с гарантией "
        "безопасных, подписанных и неизменяемых образов. Кроме того, мы "
        "предоставляем мультиархитектурные образы для обеспечения совместимости с "
        "различными платформами с поддержкой архитектур ЦП ARM64 (AArch64) и x86-64 "
        "на Linux.",
        "This page provides instructions for using Dynatrace signed and immutable "
        "container images hosted on a private registry.": "На этой странице приведены инструкции по использованию подписанных и "
        "неизменяемых образов контейнеров Dynatrace, размещённых в частном реестре.",
        "## Prerequisites": "## Предварительные требования",
        "Before you begin, be sure to meet the following prerequisites:": "Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:",
        "* Required Dynatrace Operator version is v0.11 or later": "* Обязательно Версия Dynatrace Operator: v0.11 или новее",
        "* Required Target CPU architectures are ARM64 (AArch64) and/or x86-64": "* Обязательно Целевые архитектуры ЦП: ARM64 (AArch64) и/или x86-64",
        "* Required Allow egress traffic to public registry": "* Обязательно Разрешите исходящий трафик к публичному реестру",
        "* Required Private registry with Dynatrace images stored": "* Обязательно Частный реестр с сохранёнными образами Dynatrace",
        "For guidance on storing Dynatrace images in your private registry, see "
        "[Store Dynatrace images in private registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Store Dynatrace images in private registries").': "Указания по хранению образов Dynatrace в частном реестре см. в разделе "
        "[Хранение образов Dynatrace в частных реестрах]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Хранение образов Dynatrace в частных реестрах").',
        "## Create a pull secret": "## Создание pull secret",
        "When Dynatrace container images are served by a private registry requiring "
        "authentication, a pull secret is **required** if node image pull is not "
        "used and any of the following conditions apply:": "Когда образы контейнеров Dynatrace предоставляются частным реестром, "
        "требующим аутентификации, pull secret **обязателен**, если не используется "
        "загрузка образов на узле и выполняется любое из следующих условий:",
        "* DynaKube configured for Full Observability ([Cloud-Native Full-Stack]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"In-depth description on how the deployment on Kubernetes works.") monitoring)': "* DynaKube настроен для Full Observability (мониторинг [Cloud-Native "
        "Full-Stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"Подробное описание того, как работает развёртывание в Kubernetes."))',
        "* DynaKube configured for Application Observability ([Application-Only]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#auto "
        '"In-depth description on how the deployment on Kubernetes works.") '
        "monitoring) **with** CSI driver enabled": "* DynaKube настроен для Application Observability (мониторинг "
        "[Application-Only](/managed/ingest-from/setup-on-k8s/how-it-works#auto "
        '"Подробное описание того, как работает развёртывание в Kubernetes.")) '
        "**с** включённым CSI driver",
        "Since Dynatrace Operator version 0.14.0, `customPullSecret` field is "
        "required unless [node image pull]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull") feature is used.': "Начиная с Dynatrace Operator версии 0.14.0, поле `customPullSecret` "
        "обязательно, если не используется функция [загрузки образов на узле]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Настройка загрузки образов на узле").',
        "The pull secret (the `customPullSecret` field in a DynaKube configuration) "
        "is generally used for authenticating against the private registry and "
        "accessing its artifacts (images). The following points describe the "
        "requirements for a pull secret in more detail:": "Pull secret (поле `customPullSecret` в конфигурации DynaKube) обычно "
        "используется для аутентификации в частном реестре и доступа к его "
        "артефактам (образам). В следующих пунктах подробнее описаны требования к "
        "pull secret:",
        "* When Cloud-Native Full-Stack or Application-Only monitoring with the CSI "
        "driver is configured, the CSI driver requires a pull secret to access the "
        "private registry as it attempts to directly download the Dynatrace Code "
        "Modules image from the private registry.": "* Когда настроен мониторинг Cloud-Native Full-Stack или Application-Only с "
        "CSI driver, CSI driver требует pull secret для доступа к частному реестру, "
        "так как он пытается напрямую загрузить образ Dynatrace Code Modules из "
        "частного реестра.",
        "* When using the [node image pull feature]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull") without the CSI driver, the `customPullSecret` '
        "field only affects components managed by Dynatrace Operator (in the "
        "`dynatrace` namespace). For injected application pods, you must manually "
        "configure pull secrets at the node, namespace, or pod level. For details, "
        "see [node image pull prerequisites]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "
        '"Configure node image pull").': "* При использовании [функции загрузки образов на узле]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Настройка загрузки образов на узле") без CSI driver поле `customPullSecret` '
        "влияет только на компоненты, управляемые Dynatrace Operator (в "
        "пространстве имён `dynatrace`). Для внедряемых подов приложений необходимо "
        "вручную настроить pull secret на уровне узла, пространства имён или пода. "
        "Подробнее см. [предварительные требования для загрузки образов на узле]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "
        '"Настройка загрузки образов на узле").',
        "To create a pull secret, follow this [Kubernetes documentation]"
        "(https://dt-url.net/p403yu6) on how to create a Kubernetes secret based on "
        "existing credentials or by providing credentials on the command line.": "Чтобы создать pull secret, следуйте этой [документации Kubernetes]"
        "(https://dt-url.net/p403yu6) о том, как создать секрет Kubernetes на основе "
        "существующих учётных данных или путём указания учётных данных в командной строке.",
        "## Deploy Dynatrace Operator with images from private registry": "## Развёртывание Dynatrace Operator с образами из частного реестра",
        "This section guides you through deploying Dynatrace Operator with its "
        "container image coming from a private registry.": "В этом разделе описано развёртывание Dynatrace Operator, образ контейнера "
        "которого берётся из частного реестра.",
        "Dynatrace Operator consists of multiple components (operator, webhook, CSI "
        "driver), all of which use the same `dynatrace-operator` image with specific "
        "deployment configurations per component.": "Dynatrace Operator состоит из нескольких компонентов (operator, webhook, "
        "CSI driver), каждый из которых использует один и тот же образ "
        "`dynatrace-operator` со специфичной конфигурацией развёртывания для "
        "каждого компонента.",
        "The following command installs Dynatrace Operator and configures container "
        "images to be pulled from a private registry (for example, "
        '"registry.my-company.com") by setting the `imageRef.repository`, '
        "`imageRef.tag`, and `customPullSecret` (is propagated into "
        "`imagePullSecrets` of PodSpecs) values:": "Следующая команда устанавливает Dynatrace Operator и настраивает загрузку "
        "образов контейнеров из частного реестра (например, "
        '"registry.my-company.com"), задавая значения `imageRef.repository`, '
        "`imageRef.tag` и `customPullSecret` (распространяется в `imagePullSecrets` "
        "спецификаций подов):",
        "If you are using Helm version 4.0+, you must use `--rollback-on-failure` "
        "instead of the `--atomic` flag.": "Если вы используете Helm версии 4.0+, необходимо указывать "
        "`--rollback-on-failure` вместо флага `--atomic`.",
        "Alternatively, an already existing installation can be upgraded as follows:": "Кроме того, уже существующую установку можно обновить следующим образом:",
        "To avoid tedious and error-prone editing of large YAML files, we recommend "
        "using Helm for manifest generation via `helm template`.": "Чтобы избежать утомительного и подверженного ошибкам редактирования "
        "больших YAML-файлов, мы рекомендуем использовать Helm для генерации "
        "манифестов через `helm template`.",
        "If you prefer to make your modifications directly, however, be sure to "
        "adjust the `image` and `imagePullSecrets` fields on all containers and pods "
        "where the `dynatrace-operator` image occurs.": "Если же вы предпочитаете вносить изменения напрямую, обязательно "
        "скорректируйте поля `image` и `imagePullSecrets` во всех контейнерах и "
        "подах, где встречается образ `dynatrace-operator`.",
        "## Configure DynaKube to use images from private registry": "## Настройка DynaKube на использование образов из частного реестра",
        "To instruct Dynatrace Operator to use container images from a private "
        "registry, just configure a pull secret via the `customPullSecret` field for "
        "registry authentification and respective `image` fields in the DynaKube "
        "custom resource. The configured images will be deployed to your Kubernetes "
        "cluster to set up monitoring components.": "Чтобы Dynatrace Operator использовал образы контейнеров из частного "
        "реестра, просто настройте pull secret через поле `customPullSecret` для "
        "аутентификации в реестре и соответствующие поля `image` в пользовательском "
        "ресурсе DynaKube. Настроенные образы будут развёрнуты в вашем кластере "
        "Kubernetes для настройки компонентов мониторинга.",
        "The following DynaKube snippet demonstrates how to configure [Cloud-Native "
        "Full-Stack monitoring setup](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"In-depth description on how the deployment on Kubernetes works.") using '
        "Dynatrace container images from a private registry.": "Следующий фрагмент DynaKube демонстрирует, как настроить [Cloud-Native "
        "Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"Подробное описание того, как работает развёртывание в Kubernetes.") с '
        "использованием образов контейнеров Dynatrace из частного реестра.",
        "Note that the `version` field has no effect when the `image` and/or "
        "`codeModulesImage` fields are set.": "Обратите внимание, что поле `version` не действует, если заданы поля "
        "`image` и/или `codeModulesImage`.",
        "After configuring the required fields, the DynaKube custom resource must be "
        "applied to the Kubernetes cluster.": "После настройки необходимых полей пользовательский ресурс DynaKube нужно "
        "применить к кластеру Kubernetes.",
        "For additional information regarding `customPullSecret` field, `image` "
        "fields, or the DynaKube custom resource, see further examples below or go "
        "to the [DynaKube parameters for Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") reference page.': "Дополнительные сведения о поле `customPullSecret`, полях `image` или "
        "пользовательском ресурсе DynaKube см. в примерах ниже или на справочной "
        "странице [Параметры DynaKube для Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").',
        "Looking for more examples?": "Нужно больше примеров?",
        "#### Application and Kubernetes Observability": "#### Application и Kubernetes Observability",
        "The following custom resource snippet describes how to configure DynaKube "
        "for [Application Observability and Kubernetes observability]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Deploy Dynatrace Operator on Kubernetes") with container images from your '
        "private registry:": "Следующий фрагмент пользовательского ресурса описывает, как настроить "
        "DynaKube для [Application Observability и Kubernetes observability]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Развёртывание Dynatrace Operator в Kubernetes") с образами контейнеров из '
        "вашего частного реестра:",
        "## Verify image signature": "## Проверка подписи образа",
        "All of our immutable and signed container images adhere to best practices, "
        "enhancing security and shielding against supply chain attacks. To learn how "
        "to verify signatures and guarantee software integrity, see [Verify "
        "Dynatrace image signatures]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Verify Dynatrace image signatures").': "Все наши неизменяемые и подписанные образы контейнеров соответствуют "
        "лучшим практикам, повышая безопасность и защищая от атак на цепочку "
        "поставок. О том, как проверять подписи и гарантировать целостность ПО, см. "
        "[Проверка подписей образов Dynatrace]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Проверка подписей образов Dynatrace").',
        "## Related topics": "## Связанные темы",
        "* [Store Dynatrace images in private registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Store Dynatrace images in private registries")': "* [Хранение образов Dynatrace в частных реестрах]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Хранение образов Dynatrace в частных реестрах")',
        "* [Use a public registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Use a public registry")': "* [Использование публичного реестра]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Использование публичного реестра")',
    },
    "verify-image-signature.md": {
        "title: Verify Dynatrace image signatures": "title: Проверка подписей образов Dynatrace",
        "# Verify Dynatrace image signatures": "# Проверка подписей образов Dynatrace",
        "* 4-min read": "* Чтение: 4 мин",
        "* Updated on Apr 16, 2026": "* Обновлено 16 апреля 2026 г.",
        "In the contemporary landscape, supply chain attacks have become a prevalent "
        "threat vector. Our approach to countering this risk involves delivering "
        "immutable and signed images, which serve as the cornerstone for bolstering "
        "security measures.": "В современных условиях атаки на цепочку поставок стали распространённым "
        "вектором угроз. Наш подход к противодействию этому риску заключается в "
        "поставке неизменяемых и подписанных образов, которые служат основой для "
        "усиления мер безопасности.",
        "This page outlines the process of verifying Dynatrace image signatures, "
        "thereby establishing authenticity and safeguarding software integrity.": "На этой странице описан процесс проверки подписей образов Dynatrace, что "
        "позволяет установить подлинность и защитить целостность ПО.",
        "## Prerequisites": "## Предварительные требования",
        "Before you begin, be sure to meet the following prerequisites:": "Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:",
        "* Required [Cosign](https://docs.sigstore.dev/cosign/system_config/installation/) "
        "for image signature verification": "* Обязательно [Cosign](https://docs.sigstore.dev/cosign/system_config/installation/) "
        "для проверки подписи образов",
        "* Optional [GitHub CLI](https://cli.github.com/) for SLSA provenance "
        "verification via GitHub attestation API": "* Необязательно [GitHub CLI](https://cli.github.com/) для проверки "
        "происхождения SLSA через GitHub attestation API",
        "* Required Read access to Dynatrace image repositories when using a private registry": "* Обязательно Доступ на чтение к репозиториям образов Dynatrace при использовании частного реестра",
        "## Verify image signatures using Cosign": "## Проверка подписей образов с помощью Cosign",
        "The following sections describe how Dynatrace image signatures can be "
        "verified using Cosign. For simplicity, all examples reference Dynatrace "
        "component repositories on public Amazon ECR, but are valid and applicable "
        "to any registry holding Dynatrace images.": "В следующих разделах описано, как проверять подписи образов Dynatrace с "
        "помощью Cosign. Для простоты во всех примерах используются репозитории "
        "компонентов Dynatrace в публичном Amazon ECR, однако они верны и применимы "
        "к любому реестру, содержащему образы Dynatrace.",
        "If you are looking for alternatives to Amazon ECR, see [Supported public "
        "registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry").': "Если вы ищете альтернативы Amazon ECR, см. [Поддерживаемые публичные "
        "реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра").',
        "Image signing is only performed on Dynatrace images of supported public "
        "registries. Images on the Dynatrace built-in registry are not signed.": "Подписание образов выполняется только для образов Dynatrace из "
        "поддерживаемых публичных реестров. Образы во встроенном реестре Dynatrace "
        "не подписываются.",
        "Dynatrace signs images with Cosign, but only signing data for Dynatrace "
        "Operator is uploaded to the public Sigstore transparency log. This allows "
        "standard verification for the Operator. For other images, the "
        "`--insecure-ignore-tlog` flag is required during verification.": "Dynatrace подписывает образы с помощью Cosign, но в публичный журнал "
        "прозрачности Sigstore выгружаются данные о подписи только для Dynatrace "
        "Operator. Это позволяет выполнять стандартную проверку для Operator. Для "
        "остальных образов при проверке требуется флаг `--insecure-ignore-tlog`.",
        "Dynatrace Operator is an open-source project hosted and built on GitHub. As "
        "a consequence, signing and verification slightly differs from other "
        "Dynatrace components.": "Dynatrace Operator является проектом с открытым исходным кодом, который "
        "размещается и собирается на GitHub. Поэтому подписание и проверка немного "
        "отличаются от других компонентов Dynatrace.",
        "Keyless verification": "Проверка без ключа",
        "Public key verification": "Проверка по открытому ключу",
        "The following command shows a keyless way to verify the Dynatrace Operator "
        "image signature:": "Следующая команда показывает способ проверки подписи образа Dynatrace "
        "Operator без ключа:",
        "The following command shows how to verify the Dynatrace Operator image "
        "signature using the public key of the respective GitHub release:": "Следующая команда показывает, как проверить подпись образа Dynatrace "
        "Operator с помощью открытого ключа соответствующего релиза GitHub:",
        "The following command shows how to verify the Dynatrace ActiveGate image "
        "signature using the public key from `ca.dynatrace.com`:": "Следующая команда показывает, как проверить подпись образа Dynatrace "
        "ActiveGate с помощью открытого ключа из `ca.dynatrace.com`:",
        "The following command shows how to verify the Dynatrace Code Modules image "
        "signature using the public key from `ca.dynatrace.com`:": "Следующая команда показывает, как проверить подпись образа Dynatrace Code "
        "Modules с помощью открытого ключа из `ca.dynatrace.com`:",
        "The following command shows how to verify the Dynatrace OneAgent image "
        "signature using the public key from `ca.dynatrace.com`:": "Следующая команда показывает, как проверить подпись образа Dynatrace "
        "OneAgent с помощью открытого ключа из `ca.dynatrace.com`:",
        "The following command shows how to verify the Dynatrace Kubernetes Node "
        "Configuration Collector image signature using the public key from "
        "`ca.dynatrace.com`:": "Следующая команда показывает, как проверить подпись образа Dynatrace "
        "Kubernetes Node Configuration Collector с помощью открытого ключа из "
        "`ca.dynatrace.com`:",
        "The following command shows how to verify the Dynatrace EdgeConnect image "
        "signature using the public key from `ca.dynatrace.com`:": "Следующая команда показывает, как проверить подпись образа Dynatrace "
        "EdgeConnect с помощью открытого ключа из `ca.dynatrace.com`:",
        "## Verify Software Bill of Materials (SBOM) Attestation": "## Проверка аттестации спецификации состава ПО (SBOM)",
        "Attestations enable users to confirm that a Software Bill of Materials "
        "(SBOM) comes from a trusted source in the software supply chain. By "
        "trusting the container image producer's declaration of the included "
        "software, users can safely integrate the SBOM into their workflows.": "Аттестации позволяют пользователям подтвердить, что спецификация состава "
        "ПО (SBOM) поступает из доверенного источника в цепочке поставок ПО. "
        "Доверяя заявлению производителя образа контейнера о включённом ПО, "
        "пользователи могут безопасно интегрировать SBOM в свои рабочие процессы.",
        "Use the following command to verify the Software Bill of Materials (SBOM) "
        "attestation[1](#fn-1-1-def) of a Dynatrace Operator[2](#fn-1-2-def) image:": "Используйте следующую команду для проверки аттестации спецификации "
        "состава ПО (SBOM)[1](#fn-1-1-def) образа Dynatrace Operator[2](#fn-1-2-def):",
        "Supported from Dynatrace Operator version 0.12.0.": "Поддерживается с версии Dynatrace Operator 0.12.0.",
        "Dynatrace Operator image is available on Amazon ECR from version 1.0.0. For "
        "more information, see [supported public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry").': "Образ Dynatrace Operator доступен в Amazon ECR начиная с версии 1.0.0. "
        "Дополнительные сведения см. в разделе [Поддерживаемые публичные реестры]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра").',
        "Retrieve SBOM file from verification output": "Извлечение файла SBOM из вывода проверки",
        "The SBOM in CycloneDX format can be extracted from the in-toto attestation "
        "by extending the command from above with `jq`[3](#fn-2-3-def) filters:": "SBOM в формате CycloneDX можно извлечь из аттестации in-toto, дополнив "
        "приведённую выше команду фильтрами `jq`[3](#fn-2-3-def):",
        "The [jq CLI](https://jqlang.github.io/jq/) is a useful tool for working with JSON.": "[jq CLI](https://jqlang.github.io/jq/) является полезным инструментом для работы с JSON.",
        "Executing the command creates the `sbom.json` file in the local file "
        "system, containing the SBOM of the Dynatrace Operator image.": "Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, "
        "содержащий SBOM образа Dynatrace Operator.",
        "ActiveGate version 1.303+": "ActiveGate версии 1.303+",
        "Use the following command to verify the Software Bill of Materials (SBOM) "
        "attestation of a Dynatrace ActiveGate image.": "Используйте следующую команду для проверки аттестации спецификации "
        "состава ПО (SBOM) образа Dynatrace ActiveGate.",
        "Make sure to specify the desired CPU architecture. Options are `amd64`, "
        "`arm64`, and `s390x`.": "Обязательно укажите нужную архитектуру ЦП. Доступны варианты `amd64`, "
        "`arm64` и `s390x`.",
        "The SBOM in CycloneDX format can be extracted from the in-toto attestation "
        "by extending the command from above with `jq`[1](#fn-3-1-def) filters:": "SBOM в формате CycloneDX можно извлечь из аттестации in-toto, дополнив "
        "приведённую выше команду фильтрами `jq`[1](#fn-3-1-def):",
        "Executing the command creates the `sbom.json` file in the local file "
        "system, containing the SBOM of the Dynatrace ActiveGate image.": "Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, "
        "содержащий SBOM образа Dynatrace ActiveGate.",
        "EdgeConnect version 1.473+": "EdgeConnect версии 1.473+",
        "Use the following command to verify the Software Bill of Materials (SBOM) "
        "attestation of a Dynatrace EdgeConnect image.": "Используйте следующую команду для проверки аттестации спецификации "
        "состава ПО (SBOM) образа Dynatrace EdgeConnect.",
        "The SBOM in CycloneDX format can be extracted from the in-toto attestation "
        "by extending the command from above with `jq`[1](#fn-4-1-def) filters:": "SBOM в формате CycloneDX можно извлечь из аттестации in-toto, дополнив "
        "приведённую выше команду фильтрами `jq`[1](#fn-4-1-def):",
        "Executing the command creates the `sbom.json` file in the local file "
        "system, containing the SBOM of the Dynatrace EdgeConnect image.": "Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, "
        "содержащий SBOM образа Dynatrace EdgeConnect.",
        "## Verify SLSA Build Provenance Attestation": "## Проверка аттестации происхождения сборки SLSA",
        "[SLSA](https://slsa.dev) build provenance attestations provide a verifiable "
        "record of where and how a container image was built. Verifying these "
        "attestations confirms that the image was produced by the expected source "
        "repository and build workflow, protecting against tampering in the build "
        "and distribution process.": "Аттестации происхождения сборки [SLSA](https://slsa.dev) предоставляют "
        "проверяемую запись о том, где и как был собран образ контейнера. Проверка "
        "этих аттестаций подтверждает, что образ создан ожидаемым исходным "
        "репозиторием и рабочим процессом сборки, защищая от подмены в процессе "
        "сборки и распространения.",
        "Use the following command to verify the SLSA build provenance "
        "attestation[1](#fn-5-1-def) of a Dynatrace Operator[2](#fn-5-2-def) image:": "Используйте следующую команду для проверки аттестации происхождения "
        "сборки SLSA[1](#fn-5-1-def) образа Dynatrace Operator[2](#fn-5-2-def):",
        "Supported from Dynatrace Operator version 1.9.0.": "Поддерживается с версии Dynatrace Operator 1.9.0.",
        "On success, Cosign confirms that the signing certificate, transparency log "
        "entry, and OIDC issuer are valid, and that the attestation was produced by "
        "a trusted Dynatrace build workflow.": "В случае успеха Cosign подтверждает, что сертификат подписи, запись в "
        "журнале прозрачности и издатель OIDC действительны, а аттестация создана "
        "доверенным рабочим процессом сборки Dynatrace.",
        "Retrieve provenance details from verification output": "Извлечение сведений о происхождении из вывода проверки",
        "The [SLSA Provenance v1](https://slsa.dev/spec/v1.0/provenance) payload can "
        "be extracted from the in-toto attestation by extending the command from "
        "above with `jq`[3](#fn-6-3-def) filters:": "Полезную нагрузку [SLSA Provenance v1](https://slsa.dev/spec/v1.0/provenance) "
        "можно извлечь из аттестации in-toto, дополнив приведённую выше команду "
        "фильтрами `jq`[3](#fn-6-3-def):",
        "The output contains the full SLSA Provenance v1 predicate, including the "
        "source repository, build workflow, git commit, and the GitHub Actions "
        "invocation that produced the image.": "Вывод содержит полный предикат SLSA Provenance v1, включая исходный "
        "репозиторий, рабочий процесс сборки, git-коммит и вызов GitHub Actions, "
        "создавший образ.",
        "Alternatively, you can use the [GitHub CLI](https://cli.github.com/) to "
        "verify the attestation directly against the GitHub attestation API:": "Кроме того, можно использовать [GitHub CLI](https://cli.github.com/) "
        "для проверки аттестации напрямую через GitHub attestation API:",
        "On success, the command prints `Verification succeeded!` and lists the "
        "matched attestations, including the build repository, workflow, and signer "
        "identity.": "В случае успеха команда выводит `Verification succeeded!` и перечисляет "
        "совпавшие аттестации, включая репозиторий сборки, рабочий процесс и "
        "идентификацию подписавшего.",
        "## Related topics": "## Связанные темы",
        "* [Use a public registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Use a public registry")': "* [Использование публичного реестра]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "
        '"Использование публичного реестра")',
        "* [Use a private registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry")': "* [Использование частного реестра]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра")',
        "* [Store Dynatrace images in private registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Store Dynatrace images in private registries")': "* [Хранение образов Dynatrace в частных реестрах]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "
        '"Хранение образов Dynatrace в частных реестрах")',
    },
    "prepare-private-registry.md": {
        "title: Store Dynatrace images in private registries": "title: Хранение образов Dynatrace в частных реестрах",
        "# Store Dynatrace images in private registries": "# Хранение образов Dynatrace в частных реестрах",
        "* 7-min read": "* Чтение: 7 мин",
        "* Published Feb 29, 2024": "* Опубликовано 29 февраля 2024 г.",
        "For users seeking greater control over their image hosting environment, "
        "Dynatrace offers the option to replicate images and signatures to private "
        "registries.": "Для пользователей, которым нужен больший контроль над средой размещения "
        "образов, Dynatrace предлагает возможность реплицировать образы и подписи в "
        "частные реестры.",
        "We recommend using a private registry for optimal performance and no rate "
        "limiting risks in high-demand and dynamic environments. Furthermore, to "
        "meet security standards and ensure software integrity while mitigating "
        "supply chain risks, image scanning and signature verification against "
        "Dynatrace images can be applied and is recommended.": "Мы рекомендуем использовать частный реестр для оптимальной "
        "производительности и отсутствия рисков ограничения частоты запросов в "
        "условиях высокой нагрузки и динамичных сред. Кроме того, для соответствия "
        "стандартам безопасности и обеспечения целостности ПО при снижении рисков "
        "цепочки поставок можно применять сканирование образов и проверку подписей "
        "образов Dynatrace, что и рекомендуется.",
        "By replicating Dynatrace images to your private registry, you can "
        "seamlessly merge excellent delivery performance with the assurance of "
        "secure, signed, and immutable images. We provide multi-arch images to "
        "ensure compatibility across various platforms supporting ARM64 (AArch64) "
        "and x86-64 CPU architectures on Linux.": "Реплицируя образы Dynatrace в свой частный реестр, вы "
        "беспрепятственно сочетаете отличную производительность доставки с гарантией "
        "безопасных, подписанных и неизменяемых образов. Мы предоставляем "
        "мультиархитектурные образы для обеспечения совместимости с различными "
        "платформами с поддержкой архитектур ЦП ARM64 (AArch64) и x86-64 на Linux.",
        "This page offers guidance on securely storing Dynatrace immutable images in "
        "a private registry. It includes instructions for pulling images, verifying "
        "image signatures, and pushing them to your preferred private registry.": "На этой странице приведены указания по безопасному хранению неизменяемых "
        "образов Dynatrace в частном реестре. Она включает инструкции по загрузке "
        "образов, проверке подписей образов и их отправке в выбранный вами частный "
        "реестр.",
        "## Prerequisites": "## Предварительные требования",
        "Before you begin, be sure to meet the following prerequisites:": "Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:",
        "* Required Private registry": "* Обязательно Частный реестр",
        "* Required Write access to image repositories for Dynatrace images": "* Обязательно Доступ на запись к репозиториям образов для образов Dynatrace",
        "* Optional [Skopeo](https://github.com/containers/skopeo/blob/main/install.md) "
        "for easy copying of our multi-arch images": "* Необязательно [Skopeo](https://github.com/containers/skopeo/blob/main/install.md) "
        "для удобного копирования наших мультиархитектурных образов",
        "* Optional [Cosign](https://docs.sigstore.dev/system_config/installation/) "
        "for image signature verification": "* Необязательно [Cosign](https://docs.sigstore.dev/system_config/installation/) "
        "для проверки подписи образов",
        "## Dynatrace container images": "## Образы контейнеров Dynatrace",
        "Dynatrace immutable and signed container images are available on various "
        "container registries. For more details on repositories and tag information, "
        "explore our [supported public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry").': "Неизменяемые и подписанные образы контейнеров Dynatrace доступны в "
        "различных реестрах контейнеров. Подробнее о репозиториях и тегах см. в "
        "наших [поддерживаемых публичных реестрах]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра").',
        "We strongly recommend choosing one of our supported public registries from "
        "which to copy container images.": "Мы настоятельно рекомендуем выбрать один из поддерживаемых нами публичных "
        "реестров, из которого копировать образы контейнеров.",
        "Please do not use the Dynatrace built-in registry for copying images to "
        "private registries.": "Пожалуйста, не используйте встроенный реестр Dynatrace для копирования "
        "образов в частные реестры.",
        "An exception applies for the OneAgent image for Classic Full-Stack, where "
        "the respective image **must** be copied from the built-in registry to work "
        "properly.": "Исключение составляет образ OneAgent для Classic Full-Stack, где "
        "соответствующий образ **необходимо** копировать из встроенного реестра для "
        "корректной работы.",
        "### Observability options": "### Опции наблюдаемости",
        "Depending on the [observability options]"
        "(/managed/ingest-from/setup-on-k8s/deployment#observability-options-for-kubernetes "
        '"Deploy Dynatrace Operator on Kubernetes") you choose, you might want to '
        "only copy required images. The following table outlines the relations "
        "between Dynatrace images and observability options.": "В зависимости от выбранных [опций наблюдаемости]"
        "(/managed/ingest-from/setup-on-k8s/deployment#observability-options-for-kubernetes "
        '"Развёртывание Dynatrace Operator в Kubernetes") можно скопировать '
        "только необходимые образы. В следующей таблице показаны связи между "
        "образами Dynatrace и опциями наблюдаемости.",
        "| Observability option | Dynatrace Operator | Dynatrace ActiveGate | "
        "Dynatrace Code Module | Dynatrace OneAgent |": "| Опция наблюдаемости | Dynatrace Operator | Dynatrace ActiveGate | "
        "Dynatrace Code Module | Dynatrace OneAgent |",
        "| Full observability  (Classic Full-Stack) | required | required | - | "
        "required [1](#fn-1-1-def) |": "| Full observability  (Classic Full-Stack) | требуется | требуется | - | "
        "требуется [1](#fn-1-1-def) |",
        "| Full observability  (Cloud-Native Full-Stack) | required | required | "
        "required | required |": "| Full observability  (Cloud-Native Full-Stack) | требуется | требуется | "
        "требуется | требуется |",
        "| Kubernetes Observability | required | required | - | - |": "| Kubernetes Observability | требуется | требуется | - | - |",
        "| Application Observability | required | required | required | - |": "| Application Observability | требуется | требуется | требуется | - |",
        "Must be replicated from Dynatrace built-in registry. See [Support for "
        "Classic Full-Stack monitoring](#classic-full-stack) for further details.": "Необходимо реплицировать из встроенного реестра Dynatrace. Подробнее см. "
        "[Поддержка мониторинга Classic Full-Stack](#classic-full-stack).",
        "### Image tags": "### Теги образов",
        "To show how versioning directly relates to image tagging, the following "
        "table lists real examples of image tags for Dynatrace container images.": "Чтобы показать, как версионирование напрямую связано с тегированием "
        "образов, в следующей таблице приведены реальные примеры тегов образов "
        "контейнеров Dynatrace.",
        "Note how Dynatrace ActiveGate, Code Modules, and OneAgent share a similar "
        "versioning approach, while Dynatrace Operator, which follows a distinct "
        "release cadence, uses a different versioning approach.": "Обратите внимание, что Dynatrace ActiveGate, Code Modules и OneAgent "
        "используют схожий подход к версионированию, тогда как Dynatrace Operator, "
        "который следует отдельному циклу выпусков, использует другой подход к "
        "версионированию.",
        "In all cases, version-based image tagging is employed with container "
        "images. Mutable image tags like 'latest' are not used.": "Во всех случаях для образов контейнеров применяется тегирование на основе "
        "версий. Изменяемые теги образов, такие как 'latest', не используются.",
        "| Container image | Image tag |": "| Образ контейнера | Тег образа |",
        "### Image signature verification": "### Проверка подписи образов",
        "All of our immutable and signed container images adhere to best practices, "
        "enhancing security and shielding against supply chain attacks. To learn how "
        "to verify signatures and guarantee software integrity, see [Verify "
        "Dynatrace image signatures]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Verify Dynatrace image signatures").': "Все наши неизменяемые и подписанные образы контейнеров соответствуют "
        "лучшим практикам, повышая безопасность и защищая от атак на цепочку "
        "поставок. О том, как проверять подписи и гарантировать целостность ПО, см. "
        "[Проверка подписей образов Dynatrace]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Проверка подписей образов Dynatrace").',
        "## Copy Dynatrace container images": "## Копирование образов контейнеров Dynatrace",
        "The following guide describes how to copy Dynatrace container images from "
        "public Amazon ECR to our private registry with the following example "
        "attributes.": "В следующем руководстве описано, как копировать образы контейнеров "
        "Dynatrace из публичного Amazon ECR в наш частный реестр со следующими "
        "примерными атрибутами.",
        "| Private container registry address | `registry.my-company.com` |": "| Адрес частного реестра контейнеров | `registry.my-company.com` |",
        "| Dynatrace Operator repository | `dynatrace-operator` |": "| Репозиторий Dynatrace Operator | `dynatrace-operator` |",
        "| Dynatrace ActiveGate repository | `dynatrace-activegate` |": "| Репозиторий Dynatrace ActiveGate | `dynatrace-activegate` |",
        "| Dynatrace Code Modules repository | `dynatrace-codemodules` |": "| Репозиторий Dynatrace Code Modules | `dynatrace-codemodules` |",
        "| Dynatrace OneAgent repository | `dynatrace-oneagent` |": "| Репозиторий Dynatrace OneAgent | `dynatrace-oneagent` |",
        "| Dynatrace K8s Node Config Collector repository | "
        "`dynatrace-k8s-node-config-collector` |": "| Репозиторий Dynatrace K8s Node Config Collector | "
        "`dynatrace-k8s-node-config-collector` |",
        "The instructions below to copy container images to your private registry:": "Инструкции ниже по копированию образов контейнеров в ваш частный реестр:",
        "Skopeo (recommended)": "Skopeo (рекомендуется)",
        "Recommended": "Рекомендуется",
        "Due to its support for easy copying of multi-arch images and "
        "signatures[1](#fn-2-1-def), we strongly recommend that you use the Skopeo "
        "CLI for copying container images. To learn more about the Skopeo CLI, see "
        "[Skopeo GitHub repository](https://github.com/containers/skopeo).": "Благодаря поддержке удобного копирования мультиархитектурных образов и "
        "подписей[1](#fn-2-1-def) мы настоятельно рекомендуем использовать Skopeo "
        "CLI для копирования образов контейнеров. Подробнее о Skopeo CLI см. в "
        "[репозитории Skopeo на GitHub](https://github.com/containers/skopeo).",
        "In the following instructions, be sure to always replace `<tag>` with an "
        "available version (see the [Supported public registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Use a public registry") section).': "В следующих инструкциях обязательно всегда заменяйте `<tag>` доступной "
        "версией (см. раздел [Поддерживаемые публичные реестры]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "
        '"Использование публичного реестра")).',
        "#### Copy Dynatrace Operator image": "#### Копирование образа Dynatrace Operator",
        "The following command shows how to copy the Dynatrace Operator image to our "
        "private registry:": "Следующая команда показывает, как скопировать образ Dynatrace Operator в "
        "наш частный реестр:",
        "#### Copy Dynatrace ActiveGate image": "#### Копирование образа Dynatrace ActiveGate",
        "The following command shows how to copy the Dynatrace ActiveGate image to "
        "our private registry:": "Следующая команда показывает, как скопировать образ Dynatrace ActiveGate "
        "в наш частный реестр:",
        "#### Copy Dynatrace Code Modules image": "#### Копирование образа Dynatrace Code Modules",
        "The following command shows how to copy the Dynatrace Code Modules image to "
        "our private registry:": "Следующая команда показывает, как скопировать образ Dynatrace Code "
        "Modules в наш частный реестр:",
        "#### Copy Dynatrace OneAgent image": "#### Копирование образа Dynatrace OneAgent",
        "The following command shows how to copy the Dynatrace OneAgent image to our "
        "private registry:": "Следующая команда показывает, как скопировать образ Dynatrace OneAgent в "
        "наш частный реестр:",
        "#### Copy Dynatrace K8s Node Config Collector image": "#### Копирование образа Dynatrace K8s Node Config Collector",
        "The following command shows how to copy the Dynatrace K8s Node Config "
        "Collector image to our private registry:": "Следующая команда показывает, как скопировать образ Dynatrace K8s Node "
        "Config Collector в наш частный реестр:",
        "Requires `use-sigstore-attachments` to be set to `true` in *Skopeo*'s "
        "[container registries]"
        "(https://github.com/containers/image/blob/main/docs/containers-registries.d.5.md#individual-configuration-sections) "
        "configuration.": "Требует установки `use-sigstore-attachments` в `true` в конфигурации "
        "[реестров контейнеров]"
        "(https://github.com/containers/image/blob/main/docs/containers-registries.d.5.md#individual-configuration-sections) "
        "*Skopeo*.",
        "We strongly recommend that you use the Skopeo CLI instead of Docker CLI for "
        "copying Dynatrace container images from public to private registries, as "
        "the Docker CLI does not provide an easy way to copy multi-arch images and "
        "signatures.": "Мы настоятельно рекомендуем использовать Skopeo CLI вместо Docker CLI для "
        "копирования образов контейнеров Dynatrace из публичных реестров в частные, "
        "так как Docker CLI не предоставляет удобного способа копировать "
        "мультиархитектурные образы и подписи.",
        "If you still want to use Docker CLI, please refer to the [official Docker "
        "CLI documentation](https://docs.docker.com/engine/reference/commandline/cli/).": "Если вы всё же хотите использовать Docker CLI, обратитесь к [официальной "
        "документации Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).",
        "### Support for Classic Full-Stack monitoring": "### Поддержка мониторинга Classic Full-Stack",
        "[Classic Full-Stack monitoring]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#classic "
        '"In-depth description on how the deployment on Kubernetes works.") requires '
        "a pre-configured Dynatrace OneAgent image, which is available **only** via "
        "the Dynatrace built-in registry.": "[Classic Full-Stack monitoring]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#classic "
        '"Подробное описание того, как работает развёртывание в Kubernetes.") '
        "требует предварительно настроенного образа Dynatrace OneAgent, который "
        "доступен **только** через встроенный реестр Dynatrace.",
        "Consequently, the OneAgent image must be replicated via the Dynatrace "
        "built-in registry as described below.": "Следовательно, образ OneAgent необходимо реплицировать через встроенный "
        "реестр Dynatrace, как описано ниже.",
        "Prerequisites": "Предварительные требования",
        "#### Before you begin": "#### Прежде чем начать",
        "Make sure you meet the following prerequisites:": "Убедитесь, что выполнены следующие предварительные требования:",
        "* Required Non-optional prerequisites from the top": "* Обязательно Все требования из начала страницы, кроме необязательных",
        "* Required Credentials for Dynatrace built-in registry": "* Обязательно Учётные данные для встроенного реестра Dynatrace",
        "#### Obtain Dynatrace built-in registry credentials": "#### Получение учётных данных встроенного реестра Dynatrace",
        "As the Dynatrace built-in registry requires authentication, you need to "
        "know your monitoring environment ID and provide a PaaS token for the login:": "Поскольку встроенный реестр Dynatrace требует аутентификации, вам нужно "
        "знать ID вашей среды мониторинга и указать токен PaaS для входа:",
        "* To determine `<your-environment-id>`, see [environment ID]"
        "(/managed/discover-dynatrace/get-started/monitoring-environment "
        '"Understand and learn how to work with monitoring environments.").': "* Чтобы определить `<your-environment-id>`, см. [ID среды]"
        "(/managed/discover-dynatrace/get-started/monitoring-environment "
        '"Узнайте, как работать со средами мониторинга.").',
        "* To determine `<your-paas-token>`, see [PaaS token]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Learn the concept of an access token and its scopes.").': "* Чтобы определить `<your-paas-token>`, см. [токен PaaS]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Изучите понятие токена доступа и его областей действия.").',
        "Example login using *Skopeo* CLI:": "Пример входа с помощью *Skopeo* CLI:",
        "Please note that this section only addresses configurations of Classic "
        "Full-Stack monitoring.": "Обратите внимание, что этот раздел касается только конфигураций "
        "мониторинга Classic Full-Stack.",
        "#### Copy Dynatrace OneAgent image for Classic Full-Stack monitoring": "#### Копирование образа Dynatrace OneAgent для мониторинга Classic Full-Stack",
        "The Dynatrace built-in registry only supports x86-64 architectures running "
        "Linux. As a consequence, we recommend that you explicitly set/override the "
        "architecture and operating system.": "Встроенный реестр Dynatrace поддерживает только архитектуры x86-64 под "
        "управлением Linux. Поэтому мы рекомендуем явно задавать/переопределять "
        "архитектуру и операционную систему.",
        "How to determine OneAgent image tag": "Как определить тег образа OneAgent",
        "The Dynatrace built-in registry provides the following OneAgent image tag "
        "formats:": "Встроенный реестр Dynatrace предоставляет следующие форматы тегов образа "
        "OneAgent:",
        "For image replication, we recommend that you copy raw images (images with "
        "the tag suffix `-raw`).": "Для репликации образов мы рекомендуем копировать raw-образы (образы с "
        "суффиксом тега `-raw`).",
        "To understand which OneAgent versions are available for replication, you "
        "can use the following Deployment APIs:": "Чтобы понять, какие версии OneAgent доступны для репликации, можно "
        "использовать следующие Deployment API:",
        "* [List available versions of OneAgent]"
        "(/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "
        '"List available versions of OneAgent via Dynatrace API.") to get an '
        "overview of available OneAgent versions.": "* [Список доступных версий OneAgent]"
        "(/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "
        '"Список доступных версий OneAgent через Dynatrace API.") для обзора '
        "доступных версий OneAgent.",
        "* [View the latest version of OneAgent]"
        "(/managed/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "
        '"View the latest version of OneAgent via Dynatrace API."), if you want to '
        "understand the OneAgent version behind `latest` or automate OneAgent image "
        "replication.": "* [Просмотр последней версии OneAgent]"
        "(/managed/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "
        '"Просмотр последней версии OneAgent через Dynatrace API."), если вы хотите '
        "понять, какая версия OneAgent скрывается за `latest`, или автоматизировать "
        "репликацию образа OneAgent.",
        "The following examples show how OneAgent versions translate to image tags "
        "available in the Dynatrace built-in registry:": "Следующие примеры показывают, как версии OneAgent соотносятся с тегами "
        "образов, доступными во встроенном реестре Dynatrace:",
        "| OneAgent version | OneAgent image tag |": "| Версия OneAgent | Тег образа OneAgent |",
        "Before executing the following command, be sure to replace "
        "`<tag-with-raw-suffix>` and `<environment-id>`:": "Перед выполнением следующей команды обязательно замените "
        "`<tag-with-raw-suffix>` и `<environment-id>`:",
        "For more information on configuring a DynaKube custom resource, see our "
        "examples of how to [use private registries]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry").': "Дополнительные сведения о настройке пользовательского ресурса DynaKube см. "
        "в наших примерах того, как [использовать частные реестры]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра").',
        "## Related topics": "## Связанные темы",
        "* [Use a private registry]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Use a private registry")': "* [Использование частного реестра]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "
        '"Использование частного реестра")',
        "* [Verify Dynatrace image signatures]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Verify Dynatrace image signatures")': "* [Проверка подписей образов Dynatrace]"
        "(/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "
        '"Проверка подписей образов Dynatrace")',
    },
}

# Technical lines copied verbatim (table rows, image refs, footnote numbers, tool tabs).
PASS = {
    "container-registries.md": set(),
    "use-public-registry.md": {
        "| Amazon ECR | Docker Hub |",
        "| --- | --- |",
        "| public.ecr.aws/dynatrace/dynatrace-activegate | dynatrace/dynatrace-activegate |",
        "| public.ecr.aws/dynatrace/dynatrace-codemodules | dynatrace/dynatrace-codemodules |",
        "| public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector | dynatrace/dynatrace-k8s-node-config-collector |",
        "| public.ecr.aws/dynatrace/dynatrace-logmodule | dynatrace/dynatrace-logmodule |",
        "| public.ecr.aws/dynatrace/dynatrace-oneagent | dynatrace/dynatrace-oneagent |",
        "| public.ecr.aws/dynatrace/dynatrace-operator[1](#fn-1-1-def) | dynatrace/dynatrace-operator |",
        "| public.ecr.aws/dynatrace/dynatrace-otel-collector | dynatrace/dynatrace-otel-collector |",
        "| public.ecr.aws/dynatrace/edgeconnect | dynatrace/edgeconnect |",
        "1",
        "Helm",
        "Kustomize",
        "Manifest",
    },
    "use-private-registry.md": {
        "Helm",
        "Manifest",
    },
    "verify-image-signature.md": {
        "### Dynatrace Operator",
        "### Dynatrace ActiveGate",
        "### Dynatrace Code Modules",
        "### Dynatrace OneAgent",
        "### Dynatrace Kubernetes Node Configuration Collector",
        "### Dynatrace EdgeConnect",
        "Cosign",
        "GitHub CLI",
        "1",
        "2",
        "3",
    },
    "prepare-private-registry.md": {
        "| --- | --- | --- | --- | --- |",
        "| --- | --- |",
        "|  |  |",
        "1",
        "| dynatrace-operator | `docker.io/dynatrace/dynatrace-operator:v1.5.0` |",
        "| dynatrace-activegate | `public.ecr.aws/dynatrace/dynatrace-activegate:1.301.70.20241127-162512` |",
        "| dynatrace-codemodules | `public.ecr.aws/dynatrace/dynatrace-codemodules:1.301.70.20241127-162512` |",
        "| dynatrace-oneagent | `public.ecr.aws/dynatrace/dynatrace-oneagent:1.301.70.20241127-162512` |",
        "| dynatrace-k8s-node-config-collector | `public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:1.0.0` |",
        "Docker CLI",
        "* `latest`",
        "* `latest-raw`",
        "* `<major>.<minor>.<revision>`",
        "* `<major>.<minor>.<revision>-raw`",
        "| latest | **latest-raw** |",
        "| 1.283.114.20240129-173640 | **1.283.114-raw** |",
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
