# Glossary — ingest-from/extensions batch (L4-IF.72)

Shared canon for ALL extensions subagents. Grounded on existing `docs/managed-ru`
corpus (2533 shipped files). Counts in parentheses = grep frequency in shipped
corpus → these are NORMS, not inventions. Follow verbatim for cross-file
consistency. Deviating term choice is the #1 source of subagent drift.

## Engine (do NOT reinvent)

Each per-file builder reuses the shared deterministic engine:

```python
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one     # generic: takes rel_dir

REL = "ingest-from/extensions/<subdir>"
TRANS = { "EN line (stripped)": "RU line", ... }     # every non-blank, non-fence prose line
PASS  = { "Line kept verbatim EN", ... }             # lines intentionally left EN

if __name__ == "__main__":
    build_one(REL, "<file>.md", TRANS, PASS)
    qa_one(REL, "<file>.md")
```

`build_one` guarantees STRUCTURE: line-parity, code fences verbatim (demoji-cleaned),
URLs byte-identical, frontmatter untouched. It raises `UNTRANSLATED: <repr>` for any
prose line not in TRANS/PASS — iterate until it builds, then run `qa_one` to 0 FAIL.
Keys are matched after whitespace-normalization + demoji, so write CLEAN EN keys
(no mojibake) and the engine matches the scraped mojibake line automatically.

## Hard rules

1. **Line-parity**: never add/remove/merge/split lines. The scraped code blocks are
   "exploded" (one token per line + blank lines) — leave them EXACTLY, they're inside
   ``` fences and pass through untouched.
2. **No em-dash `—`** (QA FAIL). For `**Term**—definition` bullets and `X — Y` →
   use colon `**Term**: definition` / `X: Y` or a comma / new sentence.
3. **No mojibake in output** (`â Ã Â ï»¿` = QA FAIL). Scraped prose has them
   (`Databaseâspecific`, `â¦`, `toolsï»¿`) — translate the CLEAN meaning, they vanish.
   Inside code fences the engine auto-cleans them; don't touch code.
4. **Code blocks / YAML / JSON / commands verbatim** (kept by engine). Never translate
   identifiers, keys, `featureSets`, `sqlOracle`, `ag_group-...`, query text.
5. **URLs byte-identical** — translate only link TEXT and the `"tooltip"` after the URL.
   Both sides of `[text](url "tooltip")` get RU; the `(url ...)` stays.
6. **No calques**: never `вы можете / вы должны / вы хотите` (QA WARN). Use impersonal
   `можно / нужно / требуется` or 2nd-person-plural-less phrasing. `we recommend` →
   `рекомендуется`. Imperative for UI steps (`Select` → `Выберите`, `Go to` → `Откройте`).

## Boilerplate lines (translate EXACTLY like this)

| EN | RU |
|---|---|
| `* How-to guide` | `* Практическое руководство` |
| `* Reference` | `* Справочник` |
| `* Explanation` | `* Пояснение` |
| `* Tutorial` | `* Учебное руководство` |
| `* N-min read` / `* N-minute read` | `* Чтение: N мин` |
| `* 1-min read` | `* Чтение: 1 мин` |
| `* Published Mon DD, YYYY` | `* Опубликовано DD месяца YYYY г.` |
| `* Updated on Mon DD, YYYY` | `* Обновлено DD месяца YYYY г.` |

Date: day WITHOUT leading zero, month genitive, ` г.` suffix.
Months genitive: января, февраля, марта, апреля, мая, июня, июля, августа, сентября,
октября, ноября, декабря. Ex: `Published Jun 16, 2025` → `Опубликовано 16 июня 2025 г.`;
`Updated on Jan 28, 2026` → `Обновлено 28 января 2026 г.`; `Mar 04, 2026` → `4 марта 2026 г.`

## Term canon (grounded; counts = corpus frequency)

| EN | RU | note |
|---|---|---|
| extension(s) | расширение / расширения (459) | склоняется |
| Extensions (framework, capital, product) | Extensions | EN — product name, e.g. "Extensions framework" → "платформа Extensions" / "среда Extensions framework" keep "Extensions framework" EN |
| Extensions framework | Extensions framework | keep EN |
| data source(s) | источник данных (40+) | склоняется |
| feature set(s) | набор функций / наборы функций (120) | |
| dimension(s) | измерение / измерения (1472) | |
| metric key | ключ метрики (34) | |
| metric(s) | метрика / метрики | |
| set of metrics / metric set | набор метрик (26) | |
| monitoring configuration | конфигурация мониторинга (21) | |
| environment configuration | конфигурация окружения (13) | |
| extension package | пакет расширения (5) | |
| credentials | учётные данные (435) | |
| credential vault | хранилище учётных данных (28) | lowercase prose; capital heading `#### Credential vault` → `#### Хранилище учётных данных` |
| endpoint(s) | эндпоинт / эндпоинты (528) | NOT «конечная точка» |
| scope (ActiveGate group / access) | область доступа (27) | the JSON `"scope"` key stays EN |
| regular expression | регулярное выражение (75) | |
| performance profile | профиль производительности | descriptive option; values `Default`/`High limits`/`Dedicated limits` in backticks → EN |
| soft limit / hard limit | мягкий предел / жёсткий предел | |
| monitoring definitions | определения мониторинга | |
| topology | топология | |
| remote / local extension | удалённое / локальное расширение | |
| signed extension / sign | подписанное расширение / подписать | |
| signature | подпись | |
| certificate | сертификат | |
| root / developer certificate | корневой / разработческий сертификат | |
| query | запрос | SQL `SELECT`/query text in code stays EN |
| schema reference | справочник схемы | heading e.g. "SQL data source reference" → "Справочник по источнику данных SQL" |
| token | токен | `extensions.read`/`extensions.write` scopes EN backtick |
| permission(s) | разрешение / разрешения | |
| Manage monitoring settings (classic perm) | Manage monitoring settings | EN — classic permission name |
| tenant token / personal token | токен тенанта / персональный токен | |

## Kept EN (verbatim, do NOT translate)

- Product / component names: **Dynatrace**, **OneAgent**, **ActiveGate**, **Extension
  Execution Controller / EEC** (114× EN, 0 translated), **Dynatrace Hub**, **Dynatrace CLI
  / dt-cli**, **Davis**, **Grail**, **Dynatrace Intelligence**.
- Data-source tech names: **SNMP**, **WMI**, **JMX**, **Prometheus**, **SQL**, **Python**,
  **JDBC**, **MBeans**, **OID**, **MIB**, **SNMP traps / snmptraps**.
- Databases: **Oracle Database**, **Microsoft SQL Server**, **IBM DB2**, **MySQL**,
  **PostgreSQL**, **SAP Hana**, **Snowflake**.
- File / code identifiers: `extension.yaml`, `extension.zip`, `.sig`, `.tsr`, `dt-cli`,
  `featureSets`, `sqlOracle`, `ag_group-...`, `extensions.read`, `extensions.write`,
  field names, JSON/YAML keys, query text, `Default`/`High limits`/`Dedicated limits`.
- UI labels that the corpus keeps EN: **Manage monitoring settings** (classic permission).
- VS Code add-on: **Visual Studio Code** / **VS Code**, **Dynatrace Extensions** (the
  add-on name); command/menu identifiers in backticks EN.

## UI-step phrasing (corpus norm)

- `Go to **Settings** and select **Preferences** > **X**.` →
  `Откройте **Settings** и выберите **Preferences** > **X**.` — keep the bold UI menu
  names EN (Settings/Preferences/Hosts/Deployment Status/More/OneAgents are UI labels;
  corpus keeps menu-path bold labels EN), translate the connective verbs.
  (Check neighbor norm: most managed-ru keeps `**Settings**` EN in menu paths.)
- `Turn on **X**` → `Включите **X**` (X EN if UI toggle label).
- `Select **More** (**…**)` → `Выберите **More** (**…**)`.

## Per-structure notes

- **SQL `*-monitoring.md`** (8 files, strong shared template): intro "After you define
  the scope…" + `## Example payload` + `## Parameters` with `### Enabled / Description /
  Version / Feature sets / Endpoints / Authentication / #### Credential vault / ### Scope`.
  Keep the per-field headings; the JSON payload + `"scope"` format block are code (verbatim).
  Reuse identical RU for the shared sentences across all 8 so they stay byte-consistent.
- **schema-reference.md / sql-reference.md** (Reference, big): YAML examples in fences
  (verbatim) + prose explanations + tables. Table header cells translate; identifier
  cells (YAML keys, type names) stay EN. Translate prose around each YAML block.
- **wmi-tutorial-0N.md**: step-by-step tutorial pages; imperative voice.
- **Hub/card pages** (concepts.md tail, develop-your-extensions.md): card pattern
  `[![alt](img "tip")\n\n### Title\n\nDesc](url "tooltip")` — translate `### Title`,
  Desc, and tooltip; keep img URL + alt per corpus (alt == caption norm: translate
  descriptive alt, keep product-name alt EN).

## Tooltip blindspot (recurring #9 — CHECK every link)

A link `[RU text](url "EN tooltip")` whose visible text is already Russian still hides
an untranslated EN tooltip — the leftover-scanner is blind to it (line has Cyrillic).
Translate the `"tooltip"` too. Common shared tooltips in this batch:
- `"Learn how to sign an extension, upload certificates and custom extensions, and
  configure certificate permissions using the Dynatrace Extensions Framework."` →
  `"Узнайте, как подписать расширение, загрузить сертификаты и пользовательские
  расширения и настроить разрешения сертификатов с помощью платформы Dynatrace
  Extensions Framework."`
- `"Understand the basic concepts of ActiveGate groups."` →
  `"Изучите основные концепции групп ActiveGate."`
- `"Learn more about the concept of Dynatrace Extensions."` →
  `"Подробнее о концепции Dynatrace Extensions."`
