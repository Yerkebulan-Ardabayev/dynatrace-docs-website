# -*- coding: utf-8 -*-
"""L4-IF.62 G8 secB builder: setup-on-k8s/guides networking-security-compliance
security-configurations + advanced-security-configurations batch (4 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for identifier headings / bare component lines. Any prose line missing from both
raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain mojibake `ï»¿` before some `]`, and `â` (em-dash
mojibake) inside the ActiveGate token component lines; MOJI_RE strips both
the `ï»¿` family and bare `â` from EN line + TRANS keys so keys match and RU
stays clean (RU translations avoid em-dash per glossary).
"""

import os
import re

# strip BOM-mojibake family + corrupted em-dash bytes (â + U+0080 + U+0094 ->
# `â\x80\x94`) from EN line + TRANS keys, so keys match and RU stays clean.
MOJI_RE = re.compile("[﻿ï»¿â]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SEC = "ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations"
ADV = "ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations"

# per-file relative subdir (advanced files live in ADV)
REL = {
    "openshift-configuration.md": SEC,
    "pod-security-standards.md": SEC,
    "token-rotation.md": SEC,
    "injection-readonly-volume.md": ADV,
}

# ----------------------------------------------------------------------------
TRANS = {
    "openshift-configuration.md": {
        "title: Additional OpenShift configurations": "title: Дополнительные настройки OpenShift",
        "# Additional OpenShift configurations": "# Дополнительные настройки OpenShift",
        "* 3-min read": "* Чтение: 3 мин",
        "* Updated on Feb 27, 2026": "* Обновлено 27 февраля 2026 г.",
        "Integrating Dynatrace Operator into OpenShift environments requires "
        "understanding the specifics of both platforms. This guide depicts the "
        "necessary configurations, focusing on [Security Context Constraints (SCCs)]"
        "(https://dt-url.net/sl0340s) and the use of Dynatrace Operator CSI driver "
        "in various scenarios.": "Интеграция Dynatrace Operator в окружения OpenShift требует понимания "
        "особенностей обеих платформ. В этом руководстве описаны необходимые "
        "настройки с упором на [Security Context Constraints (SCC)]"
        "(https://dt-url.net/sl0340s) и использование CSI driver Dynatrace Operator "
        "в различных сценариях.",
        "## Security Context Constraints (SCCs)": "## Security Context Constraints (SCC)",
        "In OpenShift, SCCs provide control over pod permissions in a manner akin to "
        "the built-in Role-Based Access Control (RBAC) system of Kubernetes. SCCs "
        "specify the actions a pod can perform and define its levels of resource "
        "access.": "В OpenShift SCC обеспечивают контроль над разрешениями подов подобно "
        "встроенной системе управления доступом на основе ролей (RBAC) в Kubernetes. "
        "SCC задают действия, которые может выполнять под, и определяют его уровни "
        "доступа к ресурсам.",
        "To get an overview of all default and custom SCCs in an OpenShift cluster, "
        "execute the following command:": "Чтобы получить обзор всех стандартных и пользовательских SCC в кластере "
        "OpenShift, выполните следующую команду:",
        "OpenShift provides [default SCCs](https://dt-url.net/e5027ls) for a more "
        "standardized approach, while also supporting custom SCCs to cover more "
        "specific requirements.": "OpenShift предоставляет [стандартные SCC](https://dt-url.net/e5027ls) для "
        "более стандартизированного подхода, а также поддерживает пользовательские "
        "SCC для покрытия более специфичных требований.",
        "### Dynatrace Operator": "### Dynatrace Operator",
        "This section provides an overview of the SCCs used by Dynatrace Operator "
        "and serves as a reference.": "В этом разделе приведён обзор SCC, используемых Dynatrace Operator, и он "
        "служит справочником.",
        "| Component | SCC used |": "| Компонент | Используемый SCC |",
        "### Code module injection for application monitoring": "### Внедрение кодового модуля для мониторинга приложений",
        "For application monitoring, Dynatrace Operator's webhook adds volumes of "
        "different types to the monitored pods:": "Для мониторинга приложений вебхук Dynatrace Operator добавляет к "
        "отслеживаемым подам тома разных типов:",
        "* `secret` volume for providing credentials and configuration data to the "
        "OneAgent.": "* Том `secret` для предоставления учётных данных и данных конфигурации "
        "для OneAgent.",
        "* `projected` volume for aggregating multiple sources of data, such as "
        "secrets, into a single volume for easier access by the OneAgent.": "* Том `projected` для агрегирования нескольких источников данных, таких как "
        "секреты, в единый том для упрощения доступа со стороны OneAgent.",
        "* `emptyDir` volume for storing ephemeral data produced due to the "
        "injection.": "* Том `emptyDir` для хранения эфемерных данных, образующихся в результате "
        "внедрения.",
        "* `csi` volume for injecting the OneAgent code module into the monitored "
        "pods.": "* Том `csi` для внедрения кодового модуля OneAgent в отслеживаемые поды.",
        "+ This volume type is only used if the CSI driver is installed and used "
        "for code module injection.": "+ Этот тип тома используется только если CSI driver установлен и применяется "
        "для внедрения кодового модуля.",
        "The default `restricted-v2` SCC allows such volumes, and our injected "
        "init-container meets this SCC's security requirements if the injected "
        "container also adheres to the same constraints.": "Стандартный SCC `restricted-v2` разрешает такие тома, и наш внедрённый "
        "init-контейнер удовлетворяет требованиям безопасности этого SCC, если "
        "внедрённый контейнер также соблюдает те же ограничения.",
        "If you want to use a custom SCC for your application pods, ensure it allows "
        "`secret`, `projected`, `emptyDir`, and `csi` volumes.": "Если вы хотите использовать пользовательский SCC для подов вашего "
        "приложения, убедитесь, что он разрешает тома `secret`, `projected`, "
        "`emptyDir` и `csi`.",
        "## CSI Inline Ephemeral Volume Security": "## Безопасность встраиваемых эфемерных томов CSI",
        "OpenShift version 4.13+": "OpenShift версии 4.13+",
        "The CSI driver requires specific labeling for validation by the [CSI Volume "
        "Admission plugin](https://dt-url.net/2l038e8).": "CSI driver требует особой маркировки для проверки плагином [CSI Volume "
        "Admission](https://dt-url.net/2l038e8).",
        "[The necessary label is automatically added to the `csidriver` resource]"
        "(https://dt-url.net/ry238f0). It is required for enabling CSI volumes "
        "injected by Dynatrace Operator using Webhook-based injection modes.": "[Необходимая метка автоматически добавляется к ресурсу `csidriver`]"
        "(https://dt-url.net/ry238f0). Она требуется для включения томов CSI, "
        "внедряемых Dynatrace Operator с помощью режимов внедрения на основе вебхука.",
    },
    "pod-security-standards.md": {
        "title: Apply Pod Security Standards": "title: Применение Pod Security Standards",
        "# Apply Pod Security Standards": "# Применение Pod Security Standards",
        "* 3-min read": "* Чтение: 3 мин",
        "* Updated on Jan 16, 2024": "* Обновлено 16 января 2024 г.",
        "Kubernetes version 1.25+": "Kubernetes версии 1.25+",
        "You can set namespace-based isolation levels for pods using [Pod Security "
        "Standards](https://dt-url.net/mp0345l), enforced by the built-in [Pod "
        "Security admission controller](https://dt-url.net/19238ro). These standards "
        "specify a list of controls, such as capabilities, seccomp profiles, and "
        "volume types.": "Можно задавать уровни изоляции подов на основе пространств имён с помощью "
        "[Pod Security Standards](https://dt-url.net/mp0345l), применяемые встроенным "
        "[контроллером допуска Pod Security](https://dt-url.net/19238ro). Эти "
        "стандарты задают перечень элементов управления, таких как возможности "
        "(capabilities), профили seccomp и типы томов.",
        "While the Pod Security admission controller is a built-in feature of "
        "Kubernetes, it is not necessarily enabled by default in all Kubernetes "
        "distributions. Moreover, for environments where enhanced or different "
        "security policies are required, third-party alternatives such as Open "
        "Policy Agent (OPA) can be utilized. For more information on using "
        "third-party tools to enforce pod security standards, see [enforcing pod "
        "security standards with third-party alternatives]"
        "(https://dt-url.net/ix038h9).": "Хотя контроллер допуска Pod Security является встроенной функцией "
        "Kubernetes, он не обязательно включён по умолчанию во всех дистрибутивах "
        "Kubernetes. Кроме того, для окружений, где требуются усиленные или иные "
        "политики безопасности, можно использовать сторонние альтернативы, такие как "
        "Open Policy Agent (OPA). Дополнительную информацию об использовании "
        "сторонних инструментов для применения стандартов безопасности подов см. в "
        "[применении стандартов безопасности подов со сторонними альтернативами]"
        "(https://dt-url.net/ix038h9).",
        "## Pod security standards": "## Pod Security Standards",
        "Pod Security Standards define three policies:": "Pod Security Standards определяют три политики:",
        "* [Privileged](https://dt-url.net/mv038z4): An unrestricted policy.": "* [Privileged](https://dt-url.net/mv038z4): неограниченная политика.",
        "* [Baseline](https://dt-url.net/4p238n8): Minimally restrictive policy.": "* [Baseline](https://dt-url.net/4p238n8): минимально ограничивающая политика.",
        "* [Restricted](https://dt-url.net/ut4387d): Heavily restricted policy.": "* [Restricted](https://dt-url.net/ut4387d): сильно ограничивающая политика.",
        "Pod Security Standards are a built-in feature of Kubernetes, and they cannot "
        "be extended or customized.": "Pod Security Standards являются встроенной функцией Kubernetes, и их нельзя "
        "расширить или настроить.",
        "## Configure pod security for the namespace": "## Настройка безопасности подов для пространства имён",
        "Pod security standards are applied at the namespace level when pods are "
        "created. If the default enforced profile set by the built-in admission "
        "controller is anything other than `privileged` (for example, `baseline` or "
        "`restricted`), at the [built-in admission controller level]"
        "(https://dt-url.net/yo4383i), the `privileged` profile needs to be "
        "configured for your namespace. Only the `privileged` policy is supported by "
        "Dynatrace Operator, as the CSI driver and OneAgent pods require more "
        "permissions than the `baseline` or `restricted` policies allow.": "Стандарты безопасности подов применяются на уровне пространства имён при "
        "создании подов. Если применяемый по умолчанию профиль, заданный встроенным "
        "контроллером допуска, отличается от `privileged` (например, `baseline` или "
        "`restricted`), на [уровне встроенного контроллера допуска]"
        "(https://dt-url.net/yo4383i) для вашего пространства имён необходимо "
        "настроить привилегированный профиль `privileged`. Dynatrace Operator "
        "поддерживает только привилегированную политику `privileged`, так как подам "
        "CSI driver и OneAgent требуется больше разрешений, чем допускают политики "
        "`baseline` или `restricted`.",
        "Run the following command to set the `dynatrace` namespace to `privileged`:": "Выполните следующую команду, чтобы задать для пространства имён `dynatrace` "
        "значение `privileged`:",
        "### Audit and warning modes": "### Режимы аудита и предупреждений",
        "The [audit and warning modes](https://dt-url.net/6l037ti) are applied to "
        "the deployment, DaemonSet, or other workload resources to catch violations "
        "even if a pod hasn't been created.": "[Режимы аудита и предупреждений](https://dt-url.net/6l037ti) применяются к "
        "deployment, DaemonSet или другим ресурсам рабочих нагрузок для выявления "
        "нарушений, даже если под ещё не был создан.",
        "## Troubleshooting": "## Устранение неполадок",
        "To understand why OneAgent pods might fail to be created under a restricted "
        "policy, use the following command.": "Чтобы понять, почему поды OneAgent могут не создаваться при ограничивающей "
        "политике, используйте следующую команду.",
        "The following event output shows a pod security standard violation "
        "preventing pod creation. This type of output is what you should watch out "
        "for when diagnosing deployment issues.": "Следующий вывод событий показывает нарушение стандарта безопасности подов, "
        "препятствующее созданию пода. Именно на такой вывод следует обращать "
        "внимание при диагностике проблем развёртывания.",
        "Similarly, to check why CSI driver pods might fail under the same "
        "conditions, use the following command.": "Аналогично, чтобы проверить, почему поды CSI driver могут давать сбой при "
        "тех же условиях, используйте следующую команду.",
    },
    "token-rotation.md": {
        "title: Token rotation": "title: Ротация токенов",
        "# Token rotation": "# Ротация токенов",
        "* Published Nov 03, 2025": "* Опубликовано 3 ноября 2025 г.",
        "Dynatrace environments provide an [API](/managed/dynatrace-api/"
        'environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens.") '
        "that enables tenant token rotation. When triggered, the API generates new "
        "tokens for OneAgents and ActiveGates.": "Окружения Dynatrace предоставляют [API](/managed/dynatrace-api/"
        'environment-api/tokens-v2/tenant-tokens "Ротация токенов тенанта '
        'Dynatrace."), который обеспечивает ротацию токенов тенанта. При запуске '
        "этот API создаёт новые токены для OneAgent и ActiveGate.",
        "After a tenant token rotation:": "После ротации токена тенанта:",
        "* Dynatrace Operator automatically detects and applies the new token.": "* Dynatrace Operator автоматически обнаруживает и применяет новый токен.",
        "* ActiveGate instances are automatically restarted.": "* Экземпляры ActiveGate автоматически перезапускаются.",
        "* OneAgents are automatically restarted.": "* Экземпляры OneAgent автоматически перезапускаются.",
        "* Log Monitoring pods are automatically restarted.": "* Поды Log Monitoring автоматически перезапускаются.",
        "Code modules are not restarted automatically. You must restart injected "
        "application pods.": "Кодовые модули не перезапускаются автоматически. Внедрённые поды приложений "
        "необходимо перезапустить вручную.",
        "## Operator-managed communication tokens": "## Токены связи, управляемые Operator",
        "Dynatrace Operator creates and manages communication tokens that enable "
        "secure communication between Dynatrace components:": "Dynatrace Operator создаёт токены связи и управляет ими, обеспечивая "
        "безопасную связь между компонентами Dynatrace:",
        "* ActiveGateNode Collection Controller token": "* Токен ActiveGate-Node Collection Controller",
        "* ActiveGateExtension Execution Controller token": "* Токен ActiveGate-Extension Execution Controller",
        "* EECDynatrace Collector token": "* Токен EEC-Dynatrace Collector",
        "## Manually rotating Operator-managed tokens": "## Ручная ротация токенов, управляемых Operator",
        "If you need to rotate any of the Operator-managed communication tokens, "
        "follow the instructions below.": "Если вам нужно выполнить ротацию любого из токенов связи, управляемых "
        "Operator, следуйте приведённым ниже инструкциям.",
        "1. Delete the existing secrets.": "1. Удалите существующие секреты.",
        "2. After the secret is removed, Dynatrace Operator automatically generates "
        "a new token and recreates the secret.": "2. После удаления секрета Dynatrace Operator автоматически создаёт новый "
        "токен и пересоздаёт секрет.",
        "You can verify the secret recreation using:": "Проверить пересоздание секрета можно с помощью:",
        "3. Restart the components that use the token.": "3. Перезапустите компоненты, которые используют токен.",
    },
    "injection-readonly-volume.md": {
        "title: Configure read-only CSI volumes": "title: Настройка томов CSI только для чтения",
        "# Configure read-only CSI volumes": "# Настройка томов CSI только для чтения",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Nov 20, 2025": "* Обновлено 20 ноября 2025 г.",
        "* Deprecated": "* Устарело",
        "Dynatrace Operator version 0.12.0+ and <1.7.0": "Dynatrace Operator версии 0.12.0+ и <1.7.0",
        "This is only relevant for Operator version after 0.12.0 and before 1.7.0.": "Это актуально только для версии Operator после 0.12.0 и до 1.7.0.",
        "After Operator version 1.7.0, all the CSI volumes injected by the Operator "
        "are readonly.": "Начиная с версии Operator 1.7.0, все тома CSI, внедряемые Operator, "
        "доступны только для чтения.",
        "### Prerequisites Deprecated": "### Предварительные требования Устарело",
        "* The Dynatrace Operator CSI driver installed on the Kubernetes cluster.": "* CSI driver Dynatrace Operator, установленный в кластере Kubernetes.",
        "* DynaKube configured to use the CSI driver. For example, ensure that "
        "`applicationMonitoring` is enabled with `useCSIDriver: true`.": "* DynaKube, настроенный на использование CSI driver. Например, убедитесь, "
        "что `applicationMonitoring` включён с `useCSIDriver: true`.",
        "`cloudNativeFullStack` is not supported on [BottleRocket]"
        "(https://dt-url.net/4c0365f).": "`cloudNativeFullStack` не поддерживается на [BottleRocket]"
        "(https://dt-url.net/4c0365f).",
        "### Enable feature flag Deprecated": "### Включение флага функции Устарело",
        "When using this feature flag, our CSI driver's resilience feature will not "
        "work. Use Operator version 1.7+ in case resilient read-only CSI volumes are "
        "required.": "При использовании этого флага функции функция отказоустойчивости нашего "
        "CSI driver работать не будет. Используйте версию Operator 1.7+, если "
        "требуются отказоустойчивые тома CSI только для чтения.",
        "* CSI driver's resilience feature: In case our CSI driver can't "
        "successfully provide a mount to an injected container for several minutes, "
        "it will back off, so the user application can start but without monitoring.": "* Функция отказоустойчивости CSI driver: если нашему CSI driver не удаётся "
        "успешно предоставить монтирование внедрённому контейнеру в течение "
        "нескольких минут, он отступит, чтобы приложение пользователя могло "
        "запуститься, но без мониторинга.",
        "To enable the injection of read-only CSI volumes, set the "
        "`feature.dynatrace.com/injection-readonly-volume` feature flag to `true`. "
        "When the feature flag is enabled, the injected CSI volume becomes "
        "read-only.": "Чтобы включить внедрение томов CSI только для чтения, задайте для флага "
        "функции `feature.dynatrace.com/injection-readonly-volume` значение `true`. "
        "Когда флаг функции включён, внедряемый том CSI становится доступным только "
        "для чтения.",
        "This enables usage of the CSI driver even on [BottleRocket]"
        "(https://dt-url.net/4c0365f) platforms where host monitoring OneAgents "
        "don't work. To accommodate this feature, extra ephemeral storage is added "
        "to allow the injected OneAgent to store logs and additional "
        "configurations.": "Это позволяет использовать CSI driver даже на платформах [BottleRocket]"
        "(https://dt-url.net/4c0365f), где OneAgent в режиме host monitoring не "
        "работает. Для поддержки этой функции добавляется дополнительное эфемерное "
        "хранилище, чтобы внедрённый OneAgent мог хранить логи и дополнительные "
        "конфигурации.",
        "A drawback to this approach is that if your pods terminate unexpectedly or "
        "are otherwise deleted, any logs stored in ephemeral storage will be lost.": "Недостаток этого подхода в том, что если ваши поды завершатся неожиданно "
        "или будут удалены иным образом, любые логи, хранящиеся в эфемерном "
        "хранилище, будут потеряны.",
    },
}

# Lines copied verbatim (identifier table rows / component-name rows).
PASS = {
    "openshift-configuration.md": {
        "| --- | --- |",
        "| Operator | `nonroot-v2` |",
        "| Webhook | `nonroot-v2` |",
        "| CSI driver | `privileged` |",
        "| OneAgent | `privileged` |",
        "| ActiveGate | `nonroot-v2` |",
        # mode-name identifier line (Cloud-Native Full-Stack / Application Monitoring)
        "cloudNativeFullStack applicationMonitoring",
    },
    "pod-security-standards.md": set(),
    "token-rotation.md": set(),
    "injection-readonly-volume.md": set(),
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
