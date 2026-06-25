# -*- coding: utf-8 -*-
"""L4-IF.64 builder: setup-on-k8s/reference/workload-mutation.md (1 file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped: / separators,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Reference page on POD MUTATIONS: annotation/env-var/volume names, mount paths,
init-container names, YAML keys, spec.* stay byte-identical EN. Tables list these
identifiers in a "Name"/backticked column (kept EN) + "Example Values" (kept EN) +
"Description" (TRANSLATED). Header `| Name | Example Values | Description |` ->
`| Имя | Примеры значений | Описание |`; backticked-identifier headers (`| `name`
| `type` |`) and `| --- |` separators stay byte-identical.

Mojibake note: EN source has a double-encoded en-dash in "enrichment-specific"
(raw bytes c3 a2 c2 80 c2 93 -> reads as U+00E2 U+0080 U+0093 under UTF-8). MOJI_RE
collapses that sequence (plus BOM) from the EN line and from TRANS keys, so keys
match clean and RU is written without any dash or mojibake.
"""

import os
import re

# BOM, the "ï»¿" sequence, and the double-encoded en-dash (â\x80\x93) -> stripped.
MOJI_RE = re.compile("﻿|ï»¿|â")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/reference"

# per-file override of subdir (none needed here)
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "workload-mutation.md": {
        "title: Dynatrace pod mutations for application workloads": "title: Мутации подов Dynatrace для прикладных рабочих нагрузок",
        "# Dynatrace pod mutations for application workloads": "# Мутации подов Dynatrace для прикладных рабочих нагрузок",
        "* 3-min read": "* Чтение: 3 мин",
        "* Updated on Dec 04, 2025": "* Обновлено 4 декабря 2025 г.",
        # word-bearing table headers (identifiers in backticks stay EN)
        "| Name | Example Values | Description |": "| Имя | Примеры значений | Описание |",
        "| Name | Example Values |": "| Имя | Примеры значений |",
        "| `name` | `type` | Description |": "| `name` | `type` | Описание |",
        "| `mountPath` | `name` | `subPath` | `readOnly` | Description |": "| `mountPath` | `name` | `subPath` | `readOnly` | Описание |",
        "When you enable metadata enrichment or OneAgent for application pods, "
        "Dynatrace Operator uses a webhook to intercept workload creation events "
        "and applies mutations to the resulting pods. These mutations modify the "
        "pod specification to enable monitoring capabilities.": "Когда вы включаете обогащение метаданными или OneAgent для прикладных "
        "подов, Dynatrace Operator использует вебхук для перехвата событий "
        "создания рабочих нагрузок и применяет мутации к создаваемым подам. Эти "
        "мутации изменяют спецификацию пода, чтобы включить возможности "
        "мониторинга.",
        "## Common components": "## Общие компоненты",
        "Starting with Operator v1.7, the injection mechanisms have been unified to "
        "improve efficiency by reducing volume mounts and moving away from "
        "environment variables in favor of an improved init-container approach.": "Начиная с Operator v1.7, механизмы внедрения были унифицированы для "
        "повышения эффективности за счёт сокращения монтирований томов и отказа "
        "от переменных окружения в пользу улучшенного подхода с init-контейнером.",
        "These `annotations` are relevant for all types of Dynatrace webhook "
        "injections.": "Эти `annotations` относятся ко всем типам внедрений через вебхук "
        "Dynatrace.",
        "| `dynakube.dynatrace.com/injected` | `true` | Indicates that the webhook "
        "has processed the pod and either injected it or skipped injection |": "| `dynakube.dynatrace.com/injected` | `true` | Указывает, что вебхук "
        "обработал под и либо внедрил его, либо пропустил внедрение |",
        '| `dynakube.dynatrace.com/reason` | `"NoBootstrapperConfig"` | Only '
        "present when `dynakube.dynatrace.com/injected: false`, provides additional "
        "information about why injection was skipped |": '| `dynakube.dynatrace.com/reason` | `"NoBootstrapperConfig"` | '
        "Присутствует только при `dynakube.dynatrace.com/injected: false`, "
        "предоставляет дополнительную информацию о том, почему внедрение было "
        "пропущено |",
        "Possible values for `dynakube.dynatrace.com/reason`:": "Возможные значения для `dynakube.dynatrace.com/reason`:",
        "* `NoBootstrapperConfig`: Dynatrace Operator needs to provide "
        "configuration to every monitored namespace through secrets called "
        "`dynatrace-bootstrapper-config` and `dynatrace-bootstrapper-certs`. If the "
        "application is scheduled before these secrets are created, the webhook must "
        "skip injection.": "* `NoBootstrapperConfig`: Dynatrace Operator должен предоставлять "
        "конфигурацию каждому отслеживаемому пространству имён через секреты с "
        "именами `dynatrace-bootstrapper-config` и `dynatrace-bootstrapper-certs`. "
        "Если приложение планируется до создания этих секретов, вебхук должен "
        "пропустить внедрение.",
        "* `NoMutationNeeded`: [There are several ways users can opt a pod out of "
        "injection in an otherwise monitored namespace.](/managed/ingest-from/"
        "setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation"
        '/annotate "Configure monitoring for namespaces and pods") For such pods, '
        "this value is set as the `reason` for no injection.": "* `NoMutationNeeded`: [Существует несколько способов исключить под из "
        "внедрения в пространстве имён, которое в остальном отслеживается.]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'monitoring-and-instrumentation/annotate "Настройте мониторинг для '
        'пространств имён и подов") Для таких подов это значение задаётся как '
        "`reason` для отсутствия внедрения.",
        "These `volumes` are relevant for all types of Dynatrace Webhook injections.": "Эти `volumes` относятся ко всем типам внедрений через вебхук Dynatrace.",
        "| `dynatrace-input` | `projected` with `dynatrace-bootstrapper-config`"
        "(required `Secret`) and `dynatrace-bootstrapper-certs`(optional `Secret`) |": "| `dynatrace-input` | `projected` с `dynatrace-bootstrapper-config`"
        "(обязательный `Secret`) и `dynatrace-bootstrapper-certs`"
        "(необязательный `Secret`) |",
        "| `dynatrace-config` | `emptyDir` |": "| `dynatrace-config` | `emptyDir` |",
        "The `dynatrace-input` volume is used exclusively by the injected "
        "init-container and contains:": "Том `dynatrace-input` используется исключительно внедрённым "
        "init-контейнером и содержит:",
        "* Configuration necessary for the injection within the "
        "`dynatrace-bootstrapper-config` secret": "* Конфигурацию, необходимую для внедрения, в секрете "
        "`dynatrace-bootstrapper-config`",
        "* Necessary certificates within the `dynatrace-bootstrapper-certs` secret": "* Необходимые сертификаты в секрете `dynatrace-bootstrapper-certs`",
        "+ The exact content of the secrets depends on what is configured in the "
        "`DynaKube`": "+ Точное содержимое секретов зависит от того, что настроено в "
        "`DynaKube`",
        "+ A `projected` volume is used to avoid hitting the size limit of secrets "
        "when users provide a large number of certificates": "+ Том `projected` используется, чтобы не превысить ограничение на "
        "размер секретов, когда пользователи предоставляют большое количество "
        "сертификатов",
        "The `dynatrace-config` volume contains all the necessary configuration for "
        "the injection after setup by the init-container.": "Том `dynatrace-config` содержит всю необходимую конфигурацию для "
        "внедрения после настройки init-контейнером.",
        "Every user container, independent of injection type, will have this volume "
        "mount.": "Каждый пользовательский контейнер, независимо от типа внедрения, будет "
        "иметь это монтирование тома.",
        "| `/var/lib/dynatrace` | `dynatrace-config` | `<container-name>` |": "| `/var/lib/dynatrace` | `dynatrace-config` | `<container-name>` |",
        "The `dynatrace-config` volume, after setup by the init-container, contains "
        "all the necessary file-based configurations to enable monitoring "
        "capabilities. The OneAgent also uses this volume for storage.": "Том `dynatrace-config` после настройки init-контейнером содержит все "
        "необходимые файловые конфигурации для включения возможностей "
        "мониторинга. OneAgent также использует этот том для хранения.",
        "#### `volumeMounts` in `split-mounts` mode": "#### `volumeMounts` в режиме `split-mounts`",
        "Starting with Operator version 1.8.0, an optional annotation "
        "`dynatrace.com/split-mounts` can be applied to a pod to enable "
        "`split-mounts` mode.": "Начиная с Operator версии 1.8.0, к поду можно применить необязательную "
        "аннотацию `dynatrace.com/split-mounts`, чтобы включить режим "
        "`split-mounts`.",
        "| `dynatrace.com/split-mounts` | `true` | allows to inject into Dynatrace "
        "workloads (like ActiveGate) |": "| `dynatrace.com/split-mounts` | `true` | позволяет выполнять внедрение "
        "в рабочие нагрузки Dynatrace (например, ActiveGate) |",
        "There are four mount paths used when `split-mounts` mode is enabled instead "
        "of `/var/lib/dynatrace`. This prevents conflicts between Dynatrace "
        "application images and injected `/var/lib/dynatrace` volumeMount.": "При включённом режиме `split-mounts` вместо `/var/lib/dynatrace` "
        "используются четыре пути монтирования. Это предотвращает конфликты между "
        "образами приложений Dynatrace и внедрённым монтированием тома "
        "`/var/lib/dynatrace`.",
        "In case of ActiveGate `/var/lib/dynatrace/gateway/config_template`, the "
        "subdirectory becomes inaccessible when `/var/lib/dynatrace` mount path is "
        "used.": "В случае ActiveGate подкаталог "
        "`/var/lib/dynatrace/gateway/config_template` становится недоступным при "
        "использовании пути монтирования `/var/lib/dynatrace`.",
        "| `/var/lib/dynatrace/oneagent` | `dynatrace-config` | "
        "`<container-name>/oneagent` |": "| `/var/lib/dynatrace/oneagent` | `dynatrace-config` | "
        "`<container-name>/oneagent` |",
        "| `/var/lib/dynatrace/enrichment/dt_metadata.json` | `dynatrace-config` | "
        "`<container-name>/enrichment/dt_metadata.json` |": "| `/var/lib/dynatrace/enrichment/dt_metadata.json` | `dynatrace-config` "
        "| `<container-name>/enrichment/dt_metadata.json` |",
        "| `/var/lib/dynatrace/enrichment/dt_metadata.properties` | "
        "`dynatrace-config` | `<container-name>/enrichment/dt_metadata.properties` |": "| `/var/lib/dynatrace/enrichment/dt_metadata.properties` | "
        "`dynatrace-config` | "
        "`<container-name>/enrichment/dt_metadata.properties` |",
        "| `/var/lib/dynatrace/enrichment/endpoint` | `dynatrace-config` | "
        "`<container-name>/enrichment/endpoint` |": "| `/var/lib/dynatrace/enrichment/endpoint` | `dynatrace-config` | "
        "`<container-name>/enrichment/endpoint` |",
        "The `split-mounts` mode is always enabled for ActiveGates that are managed "
        "by Dynatrace Operator.": "Режим `split-mounts` всегда включён для ActiveGate, которыми управляет "
        "Dynatrace Operator.",
        "An init container named `dynatrace-operator` is added to enrich the "
        "container with metadata and/or inject the OneAgent.": "Init-контейнер с именем `dynatrace-operator` добавляется для обогащения "
        "контейнера метаданными и/или внедрения OneAgent.",
        "* Uses pod and cluster configuration (including pod name, UID, and cluster "
        "ID) as part of its config.": "* Использует конфигурацию пода и кластера (включая имя пода, UID и "
        "идентификатор кластера) как часть своей конфигурации.",
        "* Uses a default security context, or copies the securityContext of the "
        "Pod.": "* Использует контекст безопасности по умолчанию или копирует "
        "securityContext пода.",
        "* Uses resource limits depending on the type of injection:": "* Использует лимиты ресурсов в зависимости от типа внедрения:",
        "+ (standalone) Metadata: defaults are set": "+ (автономное) Метаданные: задаются значения по умолчанию",
        "+ OneAgent: can be configured in the `DynaKube`, otherwise": "+ OneAgent: можно настроить в `DynaKube`, иначе",
        "- without CSI: no defaults": "- без CSI: значения по умолчанию не заданы",
        "- with CSI: defaults are set": "- с CSI: задаются значения по умолчанию",
        "Example YAML": "Пример YAML",
        "This example shows both OneAgent injection and metadata enrichment enabled:": "В этом примере включены и внедрение OneAgent, и обогащение метаданными:",
        "## Workload mutation in OneAgent injection mode": "## Мутация рабочей нагрузки в режиме внедрения OneAgent",
        "In OneAgent injection mode, the mutations focus on enabling full-stack "
        "monitoring capabilities. This mode injects the OneAgent into your "
        "application pods to provide comprehensive application monitoring and deep "
        "visibility.": "В режиме внедрения OneAgent мутации направлены на включение возможностей "
        "full-stack мониторинга. Этот режим внедряет OneAgent в ваши прикладные "
        "поды, чтобы обеспечить комплексный мониторинг приложений и глубокую "
        "видимость.",
        "OneAgent injection specific arguments for the init-container": "Аргументы init-контейнера, специфичные для внедрения OneAgent",
        "* `--source=/opt/dynatrace/oneagent`: (Only relevant for [node-image-pull]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'node-image-pull "Configure node image pull")) Source path for copying '
        "OneAgent binaries": "* `--source=/opt/dynatrace/oneagent`: (Относится только к "
        "[node-image-pull](/managed/ingest-from/setup-on-k8s/guides/"
        'deployment-and-configuration/node-image-pull "Настройте загрузку '
        'образа на узле")) Исходный путь для копирования двоичных файлов '
        "OneAgent",
        "* `--target=/mnt/bin`: Destination path for copying OneAgent binaries": "* `--target=/mnt/bin`: Путь назначения для копирования двоичных файлов "
        "OneAgent",
        "* `--install-path=/opt/dynatrace/oneagent-paas`: Installation path where "
        "OneAgent binaries will be mounted in the user container (used for "
        "configuring the `ld.so.preload` file)": "* `--install-path=/opt/dynatrace/oneagent-paas`: Путь установки, по "
        "которому двоичные файлы OneAgent будут смонтированы в пользовательском "
        "контейнере (используется для настройки файла `ld.so.preload`)",
        "* `--technology=...`: (Only relevant for [node-image-pull](/managed/"
        "ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull") or when init-container downloads OneAgent) '
        "Specifies the OneAgent type to download/copy for reducing binary size "
        "(configured via pod or DynaKube annotations)": "* `--technology=...`: (Относится только к [node-image-pull](/managed/"
        "ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'node-image-pull "Настройте загрузку образа на узле") или когда '
        "init-контейнер загружает OneAgent) Указывает тип OneAgent для "
        "загрузки/копирования с целью уменьшения размера двоичного файла "
        "(настраивается через аннотации пода или DynaKube)",
        "* `--flavor=...`: (Only relevant when init-container downloads OneAgent) "
        "Specifies the OneAgent flavor to download/copy for reducing binary size "
        "(configured via pod annotations)": "* `--flavor=...`: (Относится только к случаю, когда init-контейнер "
        "загружает OneAgent) Указывает разновидность OneAgent для "
        "загрузки/копирования с целью уменьшения размера двоичного файла "
        "(настраивается через аннотации пода)",
        "| `oneagent.dynatrace.com/injected` | `true` |": "| `oneagent.dynatrace.com/injected` | `true` |",
        "| `DT_DEPLOYMENT_METADATA` | `orchestration_tech=Operator-cloud_native_fullstack;"
        "script_version=snapshot;orchestrator_id=b9c38fb3-6c0f-45f6-8c25-9eb3b4b5af2a` "
        "| Contains deployment metadata for OneAgent |": "| `DT_DEPLOYMENT_METADATA` | `orchestration_tech=Operator-cloud_native_fullstack;"
        "script_version=snapshot;orchestrator_id=b9c38fb3-6c0f-45f6-8c25-9eb3b4b5af2a` "
        "| Содержит метаданные развёртывания для OneAgent |",
        "| `LD_PRELOAD` | `/opt/dynatrace/oneagent-paas/agent/lib64/"
        "liboneagentproc.so` | Preloads the OneAgent library for monitoring |": "| `LD_PRELOAD` | `/opt/dynatrace/oneagent-paas/agent/lib64/"
        "liboneagentproc.so` | Предварительно загружает библиотеку OneAgent для "
        "мониторинга |",
        "These `volumes` are relevant for the OneAgent injection.": "Эти `volumes` относятся к внедрению OneAgent.",
        "| `oneagent-bin` | `csi` or `emptyDir` | Contains OneAgent binaries |": "| `oneagent-bin` | `csi` или `emptyDir` | Содержит двоичные файлы "
        "OneAgent |",
        "The `csi` mount uses the `csi.oneagent.dynatrace.com` driver and is always "
        "read-only.": "Монтирование `csi` использует драйвер `csi.oneagent.dynatrace.com` и "
        "всегда доступно только для чтения.",
        "These `volumeMounts` are relevant for the OneAgent injection.": "Эти `volumeMounts` относятся к внедрению OneAgent.",
        "| `/opt/dynatrace/oneagent-paas` | `oneagent-bin` |  | `true` | OneAgent "
        "installation directory |": "| `/opt/dynatrace/oneagent-paas` | `oneagent-bin` |  | `true` | Каталог "
        "установки OneAgent |",
        "| `/etc/ld.so.preload` | `dynatrace-config` | `oneagent/ld.so.preload` | "
        "`false` | Library preload configuration |": "| `/etc/ld.so.preload` | `dynatrace-config` | `oneagent/ld.so.preload` | "
        "`false` | Конфигурация предварительной загрузки библиотеки |",
        "## Pod mutation for metadata enrichment": "## Мутация пода для обогащения метаданными",
        "Starting with Dynatrace Operator version 1.9.0, the `metadataEnrichment` "
        "feature is automatically enabled for namespaces with OneAgent injection, "
        "even if the `enabled` parameter in `.spec.metadataEnrichment` is set to "
        "`false`.": "Начиная с Dynatrace Operator версии 1.9.0, функция `metadataEnrichment` "
        "автоматически включается для пространств имён с внедрением OneAgent, даже "
        "если параметр `enabled` в `.spec.metadataEnrichment` имеет значение "
        "`false`.",
        "These metadata enrichmentspecific mutations are therefore applied to pods "
        "in namespaces with OneAgent injection, even without explicitly enabling "
        "`metadataEnrichment` in the `DynaKube`. Explicitly disabling metadata "
        "enrichment on the pod level via the "
        "`metadata-enrichment.dynatrace.com/inject: false` annotation will also have "
        "no effect.": "Поэтому эти специфичные для обогащения метаданными мутации применяются к "
        "подам в пространствах имён с внедрением OneAgent, даже без явного "
        "включения `metadataEnrichment` в `DynaKube`. Явное отключение обогащения "
        "метаданными на уровне пода через аннотацию "
        "`metadata-enrichment.dynatrace.com/inject: false` также не будет иметь "
        "эффекта.",
        "In metadata-enrichment mode, Dynatrace Operator enhances pods with "
        "additional metadata.": "В режиме обогащения метаданными Dynatrace Operator дополняет поды "
        "дополнительными метаданными.",
        "Metadata enrichmentspecific arguments for the init-container": "Аргументы init-контейнера, специфичные для обогащения метаданными",
        "* `--metadata-enrichment`: Instructs the init-container to perform metadata "
        "enrichment": "* `--metadata-enrichment`: Указывает init-контейнеру выполнить "
        "обогащение метаданными",
        "* `--attribute=k8s.workload.kind=...`: The webhook determines this by "
        "following the `OwnerReferences` of the pod": "* `--attribute=k8s.workload.kind=...`: Вебхук определяет это, следуя "
        "`OwnerReferences` пода",
        "* `--attribute=k8s.workload.name=...`: The webhook determines this by "
        "following the `OwnerReferences` of the pod": "* `--attribute=k8s.workload.name=...`: Вебхук определяет это, следуя "
        "`OwnerReferences` пода",
        "* `--attribute=...`: Metadata propagated from the annotations of the pod's "
        "namespace appears as attributes": "* `--attribute=...`: Метаданные, распространённые из аннотаций "
        "пространства имён пода, появляются как атрибуты",
        "| `metadata.dynatrace.com/k8s.workload.kind` | `deployment` |": "| `metadata.dynatrace.com/k8s.workload.kind` | `deployment` |",
        "| `metadata.dynatrace.com/k8s.workload.name` | `example-app` |": "| `metadata.dynatrace.com/k8s.workload.name` | `example-app` |",
        "| `metadata-enrichment.dynatrace.com/injected` | `true` |": "| `metadata-enrichment.dynatrace.com/injected` | `true` |",
        "## Pod mutation for OneAgent injection with node-image-pull": "## Мутация пода для внедрения OneAgent с node-image-pull",
        "In OneAgent injection mode with [node-image-pull](/managed/ingest-from/"
        "setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Configure node image pull"), the Dynatrace Operator combines full-stack '
        "monitoring with metadata enrichment capabilities.": "В режиме внедрения OneAgent с [node-image-pull](/managed/ingest-from/"
        "setup-on-k8s/guides/deployment-and-configuration/node-image-pull "
        '"Настройте загрузку образа на узле") Dynatrace Operator сочетает '
        "full-stack мониторинг с возможностями обогащения метаданными.",
        "The key difference from other injection modes is that the `image` of the "
        "init-container is **not** the same as the `image` of the Operator/Webhook. "
        "Instead, it uses the `codeModulesImage` defined in the `DynaKube`.": "Ключевое отличие от других режимов внедрения в том, что `image` "
        "init-контейнера **не** совпадает с `image` Operator/Webhook. Вместо "
        "этого используется `codeModulesImage`, определённый в `DynaKube`.",
        "Due to not using the `image` of the Operator/Webhook, the `bootstrap` "
        "argument is not present in the init-container, as it is not needed.": "Поскольку `image` Operator/Webhook не используется, аргумент `bootstrap` "
        "отсутствует в init-контейнере, так как он не нужен.",
    },
}

# Lines copied verbatim: backticked-identifier headings, identifier table headers,
# and `| --- |` separators.
PASS = {
    "workload-mutation.md": {
        "### `annotations`",
        "### `volumes`",
        "### `volumeMounts`",
        "### `initContainers`",
        "### `env`",
        # pure backticked-identifier headers stay EN byte-identical
        "| `name` | `type` |",
        "| `mountPath` | `name` | `subPath` |",
        # separators stay byte-identical
        "| --- | --- |",
        "| --- | --- | --- |",
        "| --- | --- | --- | --- | --- |",
    },
}

# Word-bearing table headers translate (Name/Example Values/Description), while
# backticked identifiers inside mixed headers (name/type/mountPath/...) stay EN.


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
            # write the de-mojibaked form to keep RU clean
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
