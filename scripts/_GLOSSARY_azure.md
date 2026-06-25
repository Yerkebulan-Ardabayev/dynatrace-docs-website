# Glossary — ingest-from/microsoft-azure-services batch (L4-IF.73)

Shared canon for ALL Azure subagents. Grounded on existing `docs/managed-ru`
corpus (2580 shipped files, incl. 109 shipped Azure RU siblings under
`azure-cloud-services-metrics/` and the parent hubs). Counts in parentheses =
grep frequency in shipped corpus → these are NORMS, not inventions. Follow
verbatim for cross-file consistency. Deviating term choice is the #1 source of
subagent drift.

## Engine (do NOT reinvent, do NOT copy QA)

Each per-file builder reuses the shared deterministic engine. Write ONLY a tiny
builder; do NOT write your own QA — the orchestrator runs the single unified QA.

```python
# -*- coding: utf-8 -*-
"""L4-IF.73 — <relative path>.md"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one     # generic: takes rel_dir

REL = "ingest-from/microsoft-azure-services/<subdir>"   # dir of the file, no filename

TRANS = { "EN line (stripped)": "RU line", ... }   # every non-blank, non-fence prose line
PASS  = { "Line kept verbatim EN", ... }           # lines intentionally left EN

if __name__ == "__main__":
    build_one(REL, "<file>.md", TRANS, PASS)
    qa_one(REL, "<file>.md")
```

`build_one` guarantees STRUCTURE: line-parity, code fences verbatim (demoji-cleaned),
URLs byte-identical, frontmatter (`source:`/`scraped:`/`---`) untouched, blank lines
kept. It raises `UNTRANSLATED: <repr>` for any prose line not in TRANS/PASS — iterate
until it builds, then run `qa_one` to **0 FAIL**. Keys are matched after whitespace-
normalization + demoji + BOM-strip, so write **CLEAN EN keys** (no `ï»¿`, no mojibake)
and the engine matches the scraped line automatically. Example: the EN line
`...([App Service planï»¿](https://dt-url.net/f4031wl))...` → write the key WITHOUT the
`ï»¿`: `...([App Service plan](https://dt-url.net/f4031wl))...`.

Save each builder as `scripts/_build_azure_<slug>.py`. After writing, RUN it
(`python scripts/_build_azure_<slug>.py`) and keep iterating until build + qa_one
report 0 FAIL. Keep your final chat answer SHORT (filenames + line counts + QA
status) — do NOT paste the whole builder back.

## Hard rules

1. **Line-parity**: never add/remove/merge/split lines. Scraped code blocks are
   "exploded" (one token per line + blank lines) — leave them EXACTLY; they're inside
   ``` fences and pass through untouched.
2. **No em-dash `—`** (QA FAIL). For `X — это Y` def-constructions use a comma
   (`X, это Y`) or colon (`X: Y`); for inline lists use a colon. Never `—`.
3. **No mojibake in output** (`â Ã Â ï»¿` = QA FAIL). Scraped prose carries them —
   translate the CLEAN meaning, they vanish. Inside code fences the engine auto-cleans.
4. **Code blocks / YAML / JSON / CLI / az commands verbatim** (kept by engine). Never
   translate identifiers, keys, env-var names, `azureLogForwarding`, query text, ARM/
   Bicep, PowerShell.
5. **URLs byte-identical** — translate only link TEXT and the `"tooltip"` after the URL.
   Both sides of `[text](url "tooltip")` get RU; the `(url ...)` stays. **Every tooltip
   must be translated** (blindspot #9: a link whose visible text is Russian still hides
   an EN tooltip — translate it too).
6. **No calques**: never `вы можете / вы должны / вы хотите / вам нужно` (QA WARN). Use
   impersonal `можно / нужно / требуется`. `we recommend` → `рекомендуется`. Imperative
   for UI steps (`Select` → `Выберите`, `Go to` → `Откройте`, `Enable` → `Включите`,
   `Click` → `Нажмите`, `Enter` → `Введите`).
7. **TRANSLATE descriptive titles** (blindspot #16). `title: Monitor Azure X` →
   `title: Мониторинг Azure X`; the doubled `# Monitor Azure X` H1 (appears twice) →
   `# Мониторинг Azure X` (both lines). Product names inside stay EN (Azure X). Only a
   pure product/SDK name with no descriptive verb stays fully EN.

## Boilerplate lines (translate EXACTLY like this)

| EN | RU |
|---|---|
| `* Overview` | `* Обзор` |
| `* How-to guide` | `* Практическое руководство` |
| `* Reference` | `* Справочник` |
| `* Concept` | `* Концепция` |
| `* Tutorial` | `* Учебное руководство` |
| `* N-min read` / `* N-minute read` | `* Чтение: N мин` |
| `* Published Mon DD, YYYY` | `* Опубликовано DD месяца YYYY г.` |
| `* Updated on Mon DD, YYYY` | `* Обновлено DD месяца YYYY г.` |
| `## Capabilities` | `## Возможности` |
| `## Installation` | `## Установка` |
| `## Prerequisites` | `## Предварительные требования` |
| `## Requirements` | `## Требования` |
| `## Limitations` | `## Ограничения` |
| `## Related topics` | `## Связанные темы` |
| `## Configuration` | `## Настройка` |
| `## Troubleshooting` | `## Устранение неполадок` |

Date: day WITHOUT leading zero, month genitive, ` г.` suffix. Months genitive:
января, февраля, марта, апреля, мая, июня, июля, августа, сентября, октября, ноября,
декабря. Ex: `Published Jan 16, 2023` → `Опубликовано 16 января 2023 г.`;
`Updated on Jul 31, 2024` → `Обновлено 31 июля 2024 г.`

## Recurring related-topics link texts (use shipped RU form verbatim)

| EN link text | RU |
|---|---|
| `Set up Dynatrace on Microsoft Azure` | `Настройка Dynatrace в Microsoft Azure` |
| `OneAgent platform and capability support matrix` | `Матрица поддержки платформ и возможностей OneAgent` |
| `Serverless monitoring` | `Бессерверный мониторинг` |
| (parent hub link text) `Integration with Azure Monitor` | `Интеграция с Azure Monitor` |

## Term canon (grounded; counts = corpus frequency)

| EN | RU | note |
|---|---|---|
| monitor / monitoring | мониторинг / мониторить | |
| Monitor Azure X (title) | Мониторинг Azure X | descriptive title verb |
| subscription | подписка (37) | склоняется |
| resource group | группа ресурсов | Azure Portal bold UI label `**Resource group**` stays EN |
| credentials | учётные данные (105) | |
| endpoint(s) | эндпоинт / эндпоинты (598) | NOT «конечная точка» (0 in corpus) |
| tenant | тенант (120) | NOT «арендатор» |
| token | токен (NOT «маркер») | scope ids in backticks EN |
| deploy / deployment | развернуть / развёртывание | |
| workload(s) | рабочая нагрузка / рабочие нагрузки | |
| capability / capabilities | возможность / возможности | |
| full-stack monitoring | мониторинг полного стека | (corpus norm; keep `Full-stack` EN only inside product/mode labels) |
| distributed tracing | распределённая трассировка | trace → трассировка (NOT «трейс») |
| instrumentation | инструментирование | |
| out-of-the-box (OOTB) | готовый / «из коробки» | |
| metric(s) | метрика / метрики | |
| built-in (metrics/integration) | встроенный | lowercase prose |
| classic (metrics) | классические (метрики) | |
| self-monitoring | самомониторинг | |
| region(s) | регион / регионы | |
| scale set | масштабируемый набор | but **VM Scale Set / VMSS** product name → EN |
| dynamic plan / Consumption plan | динамический план / план Consumption | keep `Consumption`/`Premium` plan-name EN |
| App Service Plan | App Service Plan | EN (Azure product term) |
| log forwarding / log forwarder | log forwarding / log forwarder | KEEP EN (22/46× corpus); product «Azure Log Forwarder» EN |
| service principal | service principal | KEEP EN (no corpus RU; matches `service account` 28:0 EN neighbor norm) |
| managed identity | managed identity | KEEP EN; `system-assigned` / `user-assigned managed identity` → EN |
| roles / built-in roles | роли / встроенные роли | role NAMES (`Azure Event Hubs Data Receiver`) EN |
| event hub / Event Hubs | концентратор событий / Event Hubs | product `Azure Event Hubs` EN; lowercase generic «концентратор событий» if descriptive; when unsure keep `event hub` EN |
| trigger binding | привязка триггера | |
| site extension / VM extension | site extension / VM extension | KEEP EN (Azure feature names) |
| container / containerized | контейнер / контейнеризированный | |

## Kept EN (verbatim, do NOT translate)

- **Product / component names**: **Dynatrace**, **OneAgent**, **ActiveGate**, **Davis**,
  **Grail**, **Dynatrace Hub**, **Azure Monitor**, **Microsoft Azure**, **Azure**.
- **Azure service names**: **Azure App Service**, **App Service**, **App Service Plan**,
  **Web App for Containers**, **Azure Functions**, **Azure Spring Apps**, **Azure Service
  Fabric**, **Azure Kubernetes Service / AKS**, **Azure Virtual Machines**, **Azure
  Virtual Machine Scale Set / VM Scale Set / VMSS**, **Azure Arc**, **Azure Event Hubs**,
  **Azure Container Instances**, **Azure Monitor**, **Application Insights**, **Azure
  Portal**, **Azure CLI**, **Azure Native Integration**, **Azure Log Forwarder**.
- **Azure/cloud IAM concepts** (no corpus RU; keep EN like `service account`):
  **service principal**, **managed identity** (system-assigned / user-assigned),
  **app registration**, **client secret**, **client ID**, **tenant ID** (the bold UI
  label; prose «идентификатор тенанта» ok if generic).
- **Tech / runtime names**: **.NET / .NET Core**, **Java**, **Node.js**, **PHP**, **IIS**,
  **Windows**, **Linux**, **OpenTelemetry / OTel**, **OTLP**, **tracer / meter / exporter /
  span(спан, склоняется) / propagator** (OTel walkthrough canon — see shipped
  `opentelemetry/walkthroughs/dotnet.md`), **SDK**, **API**, **SKU**.
- **File / code identifiers**: env-var names (`ENABLE_USER_ASSIGNED_MANAGED_IDENTITY`,
  `EVENT_HUB_CONNECTION_CLIENT_ID`), `azureLogForwarding`, JSON/YAML keys, `az ...`
  commands, ARM/Bicep, PowerShell, package names, query text.
- **Azure Portal UI labels in bold**: keep the bold menu/button labels EN
  (`**Settings**`, `**Identity**`, `**Enable system assigned managed identity**`,
  `**Yes**`), translate the connecting verbs.

## UI-step phrasing (corpus norm)

- `Go to **Settings**` → `Откройте **Settings**`; `Select **X**` → `Выберите **X**`;
  `Turn on / Enable **X**` → `Включите **X**`; `Click **Save**` → `Нажмите **Save**`.
  Keep the bold UI label EN; translate only the verb and connectives.

## OpenTelemetry-on-Azure-Functions files (dotnet/nodejs/python + hub)

These follow the shipped **OTel walkthrough canon** (`opentelemetry/walkthroughs/*.md`,
L4-IF.66). Ground terminology there:
- `tracer` / `meter` / `exporter` / `propagator` → **EN**; `span` → **спан** (склоняется).
- `endpoint OTLP` → `эндпоинт OTLP`; `context propagation` / `allowlist` → EN.
- `* Updated on <date>` uses the date rule above.
- Code blocks (C#/JS/Python, `dotnet add package`, `npm install`, `pip install`) verbatim.
- `Trace Azure Functions written in .NET` (title) → `Трассировка Azure Functions на .NET`.

## Reminders against known blindspots

- #9 **Translate every `"tooltip"`** after a URL, even when link text is already Russian.
- #16 **Translate descriptive titles** (`Monitor X` → `Мониторинг X`), both H1 copies + `title:`.
- #11 `X: это Y` is wrong → `X, это Y`.
- #12 quantifier + indeclinable EN noun needs a RU anchor word («два экземпляра OneAgent»).
- #15 img `![alt]` should match its translated caption (descriptive → translate alt too;
  pure product-name → keep both EN).
- Bold UI labels (`**Settings**`) stay EN; the surrounding sentence is Russian.
