# L4-IF.70 glossary — closes the whole `ingest-from/opentelemetry/` subtree (EN→RU)

Final 14 OTel files: `collector.md`, `collector/configuration.md`,
`collector/deployment.md`, `collector/scaling.md`,
`collector/use-cases/kubernetes/{k8s-enrich,k8s-podlogs,k8s-monitoring}.md`,
`otlp-api.md`, `otlp-api/ingest-traces.md`, `otlp-api/ingest-logs.md`,
`otlp-api/ingest-otlp-metrics/about-metrics-ingest.md`,
`integrations/{envoy,istio}.md`, `troubleshooting.md`.

Consistency with already-shipped siblings is priority #1. READ
`scripts/_build_otel_uc_l4if68.py` (the `S` boilerplate dict + canon) and the
shipped use-cases leaves first; mirror their wording on any matching line.

## Method (deterministic line-parity) — NOTE the rel_dir difference

Infra (already created, do NOT modify): `scripts/_otel_canon.py` exports
`S`, `build_one`, `qa_one`, `norm`, `read_lf`. `build_one`/`qa_one` take a
**`rel_dir` first argument** — these files are NOT under `use-cases/`, so pass the
correct dir for YOUR file (do NOT use the module's `SUB`).

Create `scripts/_build_l4if70_<slug>.py`:

```python
# -*- coding: utf-8 -*-
from _otel_canon import S, build_one, qa_one

REL = "ingest-from/opentelemetry/collector"   # <-- YOUR file's directory
FNAME = "collector.md"                          # <-- YOUR file

TRANS = {
    # ONLY lines unique to this file (lines already in S resolve automatically)
    **S,
}
PASS = set()  # EN-kept lines that have NO Russian (table separators, EN headers, etc.)

if __name__ == "__main__":
    build_one(REL, FNAME, TRANS, PASS)
    qa_one(REL, FNAME)
```

`rel_dir` per file (use EXACTLY):
- `collector.md` → `ingest-from/opentelemetry/collector`
- `configuration.md`, `deployment.md`, `scaling.md` → `ingest-from/opentelemetry/collector`
- `k8s-enrich.md`, `k8s-podlogs.md`, `k8s-monitoring.md` → `ingest-from/opentelemetry/collector/use-cases/kubernetes`
- `otlp-api.md` (the hub file) → `ingest-from/opentelemetry`
- `ingest-traces.md`, `ingest-logs.md` → `ingest-from/opentelemetry/otlp-api`
- `about-metrics-ingest.md` → `ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics`
- `envoy.md`, `istio.md` → `ingest-from/opentelemetry/integrations`
- `troubleshooting.md` → `ingest-from/opentelemetry`

Run it. On `UNTRANSLATED: '<line>'`, add a correct RU translation to TRANS (or add
the line verbatim to PASS if it has no Russian — e.g. a `| --- | --- |` table
separator, a bare footnote number, or an EN-kept component header). Re-run. Loop
until it builds and `qa_one` prints `[PASS] ... warns 0`.

- TRANS keys = EN line stripped of leading/trailing whitespace (indent reapplied
  automatically). Mojibake (`ï»¿`, mojibaked em-dash/apostrophe) is normalized
  automatically by `norm()` before matching — so write keys with the CLEAN char.
- `**S` MUST stay spread into TRANS. Extra unused S keys are harmless.
- Markdown tables: every row line (`| Type | When... |`) is a normal line → put the
  translated row in TRANS; the separator `| --- | --- |` goes in PASS (no Russian).

## Keep EN (do not translate)

- Collector component kinds, inline and as headers: `receiver`, `exporter`,
  `processor`, `connector`, `extension`/`Extensions` (component section, listed
  next to receivers/processors/exporters); headers `### Receiver(s)`,
  `### Processor(s)`, `### Exporter(s)`, `### Services`, `### Processor Optional`.
- Product/protocol/distribution names: OTel Collector, Collector, OpenTelemetry,
  OTLP, OneAgent, Dynatrace, ActiveGate, Kubernetes, Envoy, Istio, gRPC, HTTP,
  Core, Contrib, Collector Builder / OCB, Prometheus, FluentD, Jaeger, Zipkin.
- Literal config values / modes in quotes or backticks: `raw`, `flattened`,
  `gzip`, `none`, `delta`, `validate`, scopes (`logs.ingest`, `metrics.ingest`,
  `openTelemetryTrace.ingest`), env vars, YAML keys, file paths, regexes, all
  URLs and anchors, `code spans`, `${env:...}`.
- Image alt inside `![alt](url "title")`: keep `alt` EN; DO translate the
  `"title"` tooltip prose.

## Term canon (use EXACTLY — extends L4-IF.69)

| EN | RU |
|---|---|
| pipeline | конвейер |
| traces | трассировки (NOT трейсы) |
| endpoint | эндпоинт |
| span / spans | спан / спаны (decline normally) |
| scrape / scraping | сбор / собирать |
| backend | бэкенд |
| attribute / resource attributes | атрибут / атрибуты ресурса |
| API token | API-токен |
| access scope | область доступа |
| environment variable | переменная окружения |
| base URL | базовый URL |
| gateway | шлюз |
| throughput | пропускная способность |
| compression | сжатие |
| payload | полезная нагрузка (Payload size → Размер полезной нагрузки) |
| data point | точка данных |
| signal / signal type | сигнал / тип сигнала |
| (metric) dimension | измерение (метрики) |
| temporality | темпоральность (delta → дельта-темпоральность; cumulative → кумулятивная темпоральность; monotonic → монотонная) |
| aggregation | агрегация |
| load balancing | балансировка нагрузки |
| delta offset | дельта-смещение |
| instrumentation | инструментирование (manual → ручное; automatic → автоматическое) |
| distribution (Collector flavor) | дистрибутив |
| deployment | развёртывание |
| topology (vertical) | топология (вертикальная) |
| best practices | Рекомендации (heading) |

Doc-type metadata bullets (corpus-confirmed counts):
- `* Overview` → `* Обзор`
- `* Explanation` → `* Пояснение`
- `* Reference` → `* Справочник`
- `* Troubleshooting` → `* Устранение неполадок`
- `* How-to guide` → `* Практическое руководство` (already in S)
- `* N-min read` → `* Чтение: N мин`
- Dates `* Updated on Mon DD, YYYY` → `* Обновлено DD <месяц-род.> YYYY г.`;
  `* Published Mon DD, YYYY` → `* Опубликовано DD <месяц-род.> YYYY г.`

## Style (mandatory — CLAUDE.md §0)

- NEVER the em-dash `—`. Bullet `term—definition` → `term: definition` (colon).
  `X — это Y` → `X, это Y` (comma, corpus norm) or `X: Y`. `qa_one` FAILs on any `—`.
- NEVER calques `вы можете / вы должны / вы хотите` (or capitalized). Use impersonal
  `можно / нужно / требуется / следует`. `qa_one` WARNs on these. Conditional
  `если вы используете/запускаете/отправляете` is corpus-norm, NOT a calque — leave it.
- Faithful to source (§3): if EN has an obvious bug/typo (e.g. "OLTP" for "OTLP" in
  troubleshooting.md, a "traces pipeline" label in a logs recipe), reproduce it
  FAITHFULLY — do NOT silently "fix" it. Note it in your report.
- Natural technical Russian, connected book-style prose; no robotic literalism.

## Report back (concise)

- `DONE <fname>: <N> lines, QA PASS 0/0`.
- Non-obvious term choices; any EN source bug preserved verbatim (§3).
- Confirm you created exactly `scripts/_build_l4if70_<slug>.py` +
  `docs/managed-ru/<REL>/<fname>`. Run `git status` (read-only) to confirm; run NO
  other git commands; touch no other files.
