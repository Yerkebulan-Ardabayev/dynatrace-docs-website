# Глоссарий — ingest-from/technology-support + setup-on-container-platforms (L4-IF.74)

Заземлён грепом по 30 готовым tech-support RU-соседям. Движок line-parity `_zos_canon_l4if71` (см. AWS/GCP-глоссарии для механики build_one/qa_one).

## Механика (кратко)
Билдер `scripts/_build_ts74_<slug>.py`: `from _zos_canon_l4if71 import build_one, qa_one`; `TRANS={EN stripped: RU}`, `PASS={остаётся EN}`; итерируй по `UNTRANSLATED` до `OK`; `qa_one` → 0 FAIL. Ключ = строка EN после `.strip()`. Код/`---`/фенсы/`source:`/`scraped:` движок пропускает. Table-separator `| --- |` → PASS. Билдер пиши через Write, ответ короткий.

## Термины (tech-support норма)
| EN | RU |
|----|----|
| deployment | развёртывание |
| instance | экземпляр |
| region | регион |
| permission | разрешение |
| Step N | Шаг N |
| limitation | ограничение |
| known limitations | известные ограничения |
| workaround | обходное решение / обходной путь |
| supported / not supported | поддерживается / не поддерживается |

## Переводить
- `title:` + заголовки `#`/`##`/`###` (кроме чистого product-name: `# NGINX`, `# Kong`, `# Quarkus`, `# GraalVM`, `# Go`).
- **img alt — ПЕРЕВОДИТЬ** (tech-support норма RU 19:9), кроме product-name-alt; `![Step N]`→`![Шаг N]`.
- Тултипы `](url "EN")` — переводить.
- doc-type: `* Reference`→`* Справочник`, `* How-to guide`→`* Практическое руководство`, `* N-min read`→`* Чтение: N мин`, `* Updated on Mon DD, YYYY`→`* Обновлено DD <месяц> YYYY г.`, `* Published ...`→`* Опубликовано ...` (НЕ путать).
- bold-лейблы `**Note:**`/`**Example:**`/`**Prerequisites**` → RU.

## Оставлять EN
- Product/tech: NGINX, NGINX Plus, OpenResty, Tengine, Kong, Kong Gateway, Quarkus, GraalVM, Go, Java, Node.js, OneAgent, ActiveGate, Dynatrace, GDK, native image.
- Имена модулей/классов/API/флагов/переменных, код и команды в ` ``` `-фенсах и инлайн `code`.
- Имена метрик в таблицах; версии/даты в таблицах.

## Container (setup-on-container-platforms, k8s legacy) — доп. термины
- namespace → пространство имён; pod → под; node → узел; secret → секрет; cluster → кластер; deployment(k8s-объект) → в коде EN, в прозе развёртывание.
- Оставлять EN: Kubernetes, OpenShift, OneAgent Operator, DaemonSet, kubectl, oc, CRD, Helm, ConfigMap, Service Account (как в setup-on-k8s корпусе).
- «legacy» в title → «(устаревшее)» если описание.

## Анти-кальки
- «вы можете»→«можно», «вы должны»→«необходимо»; условные «если вы используете» — норма.
- НЕ `X: это Y` (норма `X, это Y`). Длинных тире `—` НЕ должно быть (QA FAIL). U+FEFF/`ï»¿` мойибейк — движок чистит, но проверь.
- Квантор + EN-сущ.: опорное русское слово.

## Эталоны
- tech-support готовые соседи: `docs/managed-ru/ingest-from/technology-support/**/*.md`.
- container: `docs/managed-ru/ingest-from/setup-on-container-platforms/**/*.md` и `docs/managed-ru/ingest-from/setup-on-k8s/**` (k8s-термины).
