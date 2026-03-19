---
name: dynatrace-translate
description: "Translate Dynatrace documentation from English to Russian. ALWAYS use this skill when the user says anything related to translating documentation: 'переведи', 'перевод', 'translate', mentions a file path like 'observe/dashboards.md', says 'переведи всё новое', 'что нового', 'какие статьи', 'новые статьи', or anything about translating Dynatrace docs. Also trigger when the user pastes English Dynatrace documentation text and asks to translate it."
---

# Dynatrace Documentation Translator

You are translating Dynatrace technical documentation from English to Russian for the site https://yerkebulan-ardabayev.github.io/dynatrace-docs-website/

## Project location

The project is at: `/sessions/pensive-sleepy-ramanujan/mnt/my_develop_code/dynatrace-docs-website/`

- English sources: `docs/en/`
- Russian translations: `docs/ru/`
- Navigation config: `mkdocs.yml`
- Terminology: `scripts/terminology.yaml`

## What the user will say

The user will say things like:

- `переведи observe/dashboards.md`
- `переведи всё новое`
- `что нового для перевода?`
- Or paste raw English markdown text

## Workflow

### If user asks "что нового" / "какие статьи" / "что переводить"

Run the detect script and show results:

```bash
cd /sessions/pensive-sleepy-ramanujan/mnt/my_develop_code/dynatrace-docs-website
python scripts/detect_changes.py --source-dir docs/en --target-dir docs/ru --report /tmp/changes.json --markdown /tmp/changes.md
```

Show the user a summary of new/updated articles with their paths.

### If user says "переведи <path>" (specific file)

1. **Read** the English source from `docs/en/<path>`
2. **Read** terminology from `scripts/terminology.yaml` — load the `keep_as_is` list
3. **Translate** following the rules below
4. **Write** the result to `docs/ru/<path>` (create parent dirs if needed)
5. **Update nav** by running: `python scripts/place_translation.py --file docs/ru/<path>`
6. **Tell the user** it's done and they just need to `git push`

### If user says "переведи всё новое"

1. Run detect_changes.py to find all new/updated files
2. For each file, do the translate workflow above
3. Summarize what was translated

### If user pastes English text directly

1. Translate the text following the rules below
2. Ask where to save it (or infer from context)
3. Save and update nav

## Translation Rules

These are critical for quality:

### Terminology — DO NOT translate these terms:
Read `scripts/terminology.yaml` before translating. The `keep_as_is` list contains product names that must stay in English: Dynatrace, OneAgent, ActiveGate, Grail, Davis, DQL, Smartscape, OpenPipeline, SaaS, Managed, Kubernetes, Docker, OpenTelemetry, etc.

### Markdown preservation
- Keep ALL markdown formatting exactly as-is: headers (#), links [text](url), code blocks, tables, lists
- Keep ALL code examples, CLI commands, API endpoints, file paths unchanged
- Keep YAML frontmatter (between ---) — only translate the `title:` value
- Keep image references unchanged

### Translation style
- Professional technical Russian, formal style (вы, не ты)
- Short, clear sentences — avoid overly complex constructions
- Use established Russian IT terminology where it exists
- When a term has no good Russian equivalent, keep the English term

### Frontmatter handling
```yaml
---
title: Original English Title → title: Переведённый заголовок
source: https://docs.dynatrace.com/...  → keep unchanged
scraped: 2024-01-01T00:00:00  → keep unchanged
---
```

### Quality checks after translation
- No CJK characters (Chinese/Japanese/Korean) in the output
- No CSS artifacts (`.css-abc123-xyz` patterns)
- Protected terms from terminology.yaml remain in English
- All markdown links are intact
- File is not empty / not just frontmatter

## After saving the file

Always run:
```bash
python scripts/place_translation.py --file docs/ru/<path>
```

This updates mkdocs.yml navigation (switches `en/<path>` → `ru/<path>`).

Then tell the user: "Готово! Осталось только `git push` — и сайт обновится."
