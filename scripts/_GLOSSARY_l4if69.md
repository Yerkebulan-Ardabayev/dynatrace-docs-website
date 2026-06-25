# L4-IF.69 glossary — OTel collector/use-cases recipe leaves (EN→RU)

Shared rules for every subagent in this batch. Consistency with already-shipped
siblings (jaeger/zipkin/fluentd/statsd/filelog/netflow in
`scripts/_build_otel_uc_l4if68.py`) is the #1 priority. READ that file first and
mirror its wording for any matching line.

## Method (deterministic line-parity)

Infra (already created, do NOT modify): `scripts/_otel_canon.py` exports
`S` (dict of already-translated shared boilerplate), `SUB`, `build_one`, `qa_one`.

Create `scripts/_build_l4if69_<slug>.py`:

```python
# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one
TRANS = {
    # ONLY lines unique to this file (lines already in S resolve automatically)
    **S,
}
PASS = {"### Receivers", "### Processors", "### Exporters"}  # EN-kept headers; add "### Connectors" if present
if __name__ == "__main__":
    build_one(SUB, "<fname>", TRANS, PASS)
    qa_one(SUB, "<fname>")
```

Run it. On `UNTRANSLATED: '<line>'`, add a correct RU translation (or add the line
to PASS if it's an EN-kept component header) and re-run. Loop until it builds and
`qa_one` prints `[PASS] ... warns 0`.

- TRANS keys = EN line stripped of leading/trailing whitespace (indent reapplied
  automatically). Mojibake (`ï»¿` etc.) is normalized automatically.
- `**S` MUST stay spread into TRANS.

## Keep EN (do not translate)

- Config/component kinds inline and as headers: `receiver`, `exporter`,
  `processor`, `connector`; headers `### Receivers/Processors/Exporters/Connectors`.
- Product/protocol names: OTel Collector, Collector, OpenTelemetry, OTLP, OneAgent,
  Dynatrace, FluentD, Jaeger, Zipkin, Prometheus, Kafka, Kubernetes, NetFlow,
  StatsD, Syslog/syslog, Journald/journald, systemd, gRPC, HTTP.
- All URLs, anchors, `code spans`, `${env:...}`, YAML keys, file paths, regexes.
- Image alt inside `![alt](url "title")`: keep `alt` EN; DO translate the `"title"`
  tooltip prose.

## Term canon (use EXACTLY)

| EN | RU |
|---|---|
| pipeline | конвейер |
| traces | трассировки (NOT трейсы) |
| endpoint | эндпоинт |
| span / spans | спан / спаны (decline normally) |
| broker | брокер |
| topic | топик |
| consumer | потребитель |
| producer | производитель |
| scrape / scraping | сбор / собирать |
| bucket (histogram) | интервал |
| batch / batching | группа / группирование |
| sampling | сэмплирование |
| cold storage | холодное хранение |
| API token | API-токен |
| environment variable | переменная окружения |
| base URL | базовый URL |
| access scope | область доступа |
| backend | бэкенд |
| attribute | атрибут |
| resource attributes | атрибуты ресурса |

- H1/title pattern `Ingest X data with the OTel Collector` →
  `Приём данных X с помощью OTel Collector` (mirror jaeger/zipkin/fluentd exactly).
- Card/section-title canon: Batching→Группирование, Histogram summaries→Сводки
  гистограмм, Host monitoring→Мониторинг хостов, Mask sensitive data→Маскирование
  конфиденциальных данных, Sampling→Сэмплирование, Transform and
  filter→Преобразование и фильтрация, Memory limits→Ограничения памяти,
  Enrich with OneAgent→Обогащение с помощью OneAgent.
- Dates: `* Updated on Mon DD, YYYY` → `* Обновлено DD <месяц-в-род.> YYYY г.`;
  `* Published Mon DD, YYYY` → `* Опубликовано DD <месяц-в-род.> YYYY г.`
  (e.g. Dec 17, 2025 → 17 декабря 2025 г.). Reading time `* N-min read` →
  `* Чтение: N мин`. `* How-to guide` → `* Практическое руководство`;
  `* Explanation` → `* Пояснение`.

## Style (mandatory — CLAUDE.md §0)

- NEVER the em-dash `—`. Bullet `term—definition` → `term: definition` (colon).
  `X — это Y` → `X: Y` or `X, это Y`. (`qa_one` FAILs on any `—`.)
- NEVER calques `вы можете / вы должны / вы хотите` (or capitalized). Use impersonal
  `можно / нужно / требуется / следует`. (`qa_one` WARNs on these.)
- Faithful to source (§3): if EN has an obvious bug/typo (e.g. "traces pipeline" in
  a logs recipe, a misspelled config key), reproduce it FAITHFULLY — do NOT silently
  "fix" it. Note it in your report.
- Natural technical Russian, connected book-style prose; no robotic literalism.

## Report back (concise)

- `DONE <fname>: <N> lines, QA PASS 0/0`.
- Non-obvious term choices; any EN source bug preserved verbatim (§3).
- Confirm you created exactly `scripts/_build_l4if69_<slug>.py` +
  `docs/managed-ru/<SUB>/<fname>`. Run `git status` (read-only) to confirm; run NO
  other git commands; touch no other files.
