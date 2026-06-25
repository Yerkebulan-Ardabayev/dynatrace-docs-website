# GLOSSARY — setup-on-k8s/guides translation canon (L4-IF.62)

Mandatory canon for EN→RU translation of Dynatrace Managed K8s Operator guides.
ALL listed strings MUST be translated exactly as below (consistency across files).
Grounded against the live `docs/managed-ru` corpus (frequency-checked).

## Hard rules (from CLAUDE.md + project)
- **NO em-dash `—` ever.** Use comma / colon / period. `X — это Y` → `X, это Y` or `X: Y`.
- **Line-parity**: RU file has EXACT same line count as EN. Blank lines, `---`, code fences, `source:`/`scraped:` frontmatter copied byte-identical.
- **Code fences (``` ... ```)**: copy interior verbatim, including comments inside code. Never translate code.
- **URLs and in-page anchors**: byte-identical to EN (`](/managed/...)`, `#anchor`). Do NOT translate or alter.
- **Link title-attributes** `](url "Title text")`: the Title text IS translated; the url is not.
- **Backticked identifiers** stay EN: `spec.*`, `feature.dynatrace.com/*`, field/param/CR names, `kubectl ...`, YAML keys, env vars, file paths.
- RU output: UTF-8, LF endings, no BOM, no trailing newline. No mojibake.

## Tag-line (top-of-page bullets) — corpus canon
- `* Reference` → `* Справочник`
- `* How-to guide` → `* Практическое руководство`
- `* N-min read` → `* Чтение: N мин`
- `* Published <Mon DD, YYYY>` → `* Опубликовано DD месяца YYYY г.`  (e.g. `* Опубликовано 28 июля 2023 г.`)
- `* Updated on <Mon DD, YYYY>` → `* Обновлено DD месяца YYYY г.`
- Months: января февраля марта апреля мая июня июля августа сентября октября ноября декабря.

## Headings — corpus canon (use EXACTLY)
- `## Prerequisites` → `## Предварительные требования`
- `## Steps` → `## Шаги`
- `## Limitations` / `## Known limitations` → `## Ограничения` / `## Известные ограничения`
- `## Example` / `## Examples` → `## Пример` / `## Примеры`
- `## Overview` → `## Обзор`
- `## Learn more` → `## Узнать больше`
- `## Related topics` → `## Связанные темы`
- `## Configuration` → `## Настройка`
- `## Requirements` → `## Требования`
- `### Permissions` / `### Resources` / `### Limitations` → `### Разрешения` / `### Ресурсы` / `### Ограничения`
- Required / Optional badge → `Обязательно` / `Необязательно` (if it precedes a sentence, split with a period: `Необязательно. При установке...`).

## Terms — translate
- pods → поды; pod → под
- namespace → пространство имён; namespace selector → селектор пространств имён
- secret → секрет; annotation → аннотация; label → метка
- mapping → сопоставление; supplementary metadata → дополнительные метаданные
- feature flag → флаг функции (in prose; the `feature.dynatrace.com/...` identifier stays EN in backticks)
- injected → внедрённый; injection (noun) → инъекция; inject (verb) → внедрять
- resource limits → лимиты ресурсов; requests and limits → запросы и лимиты
- init container → init-контейнер
- certificate → сертификат; token → токен (PaaS token → PaaS-токен)
- high availability → высокая доступность
- deprecated → устаревший (adj) / устарело (state); deprecation (process) → прекращение поддержки
- custom resource → пользовательский ресурс; conversion (apiVersion) → преобразование
- storage backend → бэкенд хранилища; in place → на месте; in favor of → в пользу
- Notice → Примечание; Reminder → Напоминание; Note → Примечание
- **Before** / **After** → **До** / **После**
- environment → окружение (NOT «среда»)

## Terms — keep ENGLISH (corpus-dominant / identifiers / product names)
- Kubernetes, OpenShift, Istio, NGINX, GitOps, ArgoCD, Helm, Manifest
- OneAgent, ActiveGate, Dynatrace Operator, DynaKube, EdgeConnect, CSI driver, DaemonSet, CRD
- ClusterRole, RBAC, ServiceAccount, sidecar, proxy, network zone
- liveness / readiness / startup probe → the words liveness/readiness/startup stay EN; "probe" in generic prose → «проверка работоспособности»
- seccomp, AppArmor, SCC (Security Context Constraints), Pod Security Standards / PSS
- mode names: Cloud-Native Full-Stack / Classic Full-Stack / Application Monitoring / Host Monitoring (and their `cloudNativeFullStack` etc. identifiers) — keep EN
- Component-name headings (`## Operator`, `## Webhook`, `## CSI driver`) → keep EN byte-identical (preserve inbound anchors)
- Image alt-text stays EN (corpus has ~0 translated alt). Bold UI labels that name product UI (**Settings**, **Properties and tags**) stay EN; callout labels (**Please note:** → **Обратите внимание:**) translate.

## Grammar watch (these are auto-QA blind spots — self-check)
- Relative pronoun gender/case must match the right noun (который/которая/которое).
- No «вы можете / вы должны» calque → use impersonal «можно / необходимо / следует».
- No double «для … для» or «установлен … установки» in one sentence — rephrase.
- Zeugma: «X и Y» sharing one object needing different cases → split (e.g. «создания монтирований … и управления ими»).
- Imperative in card/description text stays imperative (Configure → Настройте, not Настройка).
