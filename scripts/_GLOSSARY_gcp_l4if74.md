# Глоссарий перевода — ingest-from/google-cloud-platform (L4-IF.74)

Заземлён грепом по 52 готовым RU-соседям (`docs/managed-ru/ingest-from/google-cloud-platform`, 3796 строк). Per-area нормы ОТЛИЧАЮТСЯ от AWS — не переноси AWS-решения вслепую.

## Как переводить (движок line-parity)

Идентично AWS-батчу. Билдер на файл `scripts/_build_gcp74_<slug>.py`:
```python
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
REL = "ingest-from/google-cloud-platform/gcp-integrations/gcp-guide"
TRANS = { "EN строка stripped": "RU перевод", ... }
PASS = { "строки остающиеся EN", ... }
build_one(REL, "<file>", TRANS, PASS)
qa_one(REL, "<file>")
```
- Ключ TRANS = строка EN-файла после `.strip()` (без отступа; в RU-значении отступ НЕ пиши).
- Пустые строки, `---`, строки внутри ```-фенсов, `source:`/`scraped:` — движок пропускает, в TRANS НЕ клади.
- Итерируй по `UNTRANSLATED: '<repr>'` (в TRANS или PASS) до сборки. Потом `qa_one` → **0 FAIL**.
- Билдер ПИШИ через Write, финальный ответ — короткий.

## Термины (корпус-норма GCP)

| EN | RU | Примечание |
|----|----|-----------|
| deployment | развёртывание | 78:12 |
| dashboard | дашборд | 92:0 |
| permission(s) | разрешение/разрешения |  |
| endpoint | эндпоинт |  |
| Step N | Шаг N |  |
| **region** | в ПРОЗЕ «регион»; в командах `gcloud`/коде/флагах `--region` — EN | корпус 20 EN (большинство в коде) |
| **instance** | в ПРОЗЕ «экземпляр»; в названиях ресурсов GCP / коде — EN | корпус 119 EN (Compute Engine instance, в коде) |
| role | роль (в прозе); `role`/имена ролей в коде/IAM — EN |  |
| token | токен |  |
| label | метка / лейбл (как у соседей) |  |
| project | проект | (GCP project) |
| service account | **service account (EN)** | GCP-сущность, как в коде |

## Оставлять EN

- **Product/service-names**: Google Cloud, GCP, Cloud Run, Cloud Functions (GCF), GKE, Compute Engine, Pub/Sub, Cloud Storage, BigQuery, Cloud Monitoring, Cloud Logging, App Engine, Kubernetes, OpenTelemetry, OTel, Dynatrace, OneAgent, ActiveGate.
- Код, команды (`gcloud ...`, `kubectl ...`), YAML/JSON, переменные окружения, ARN-подобные id — внутри ```-фенсов движок не трогает; инлайн `code` в бэктиках не трогай.
- Имена метрик в таблицах (`compute.googleapis.com/...`) — EN; переводи заголовки колонок и описания.

## Переводить (частые промахи субагентов)

- **`title:` и ВСЕ заголовки `#`/`##`/`###`** — ПЕРЕВОДИТЬ (корпус 51 RU : 1 EN). EN только у чистого product-name-заголовка (`## Cloud Run`).
  Doc-type: `* How-to guide`→`* Практическое руководство`; `* Reference`→`* Справочник`; `* Tutorial`→`* Руководство`; `* N-min read`→`* Чтение: N мин`; `* Updated on Mon DD, YYYY`→`* Обновлено DD <месяц> YYYY г.`; `* Published Mon DD, YYYY`→`* Опубликовано DD <месяц> YYYY г.` (НЕ путай Published/Updated!).
- **img alt — ПЕРЕВОДИТЬ** (GCP-норма RU 5:0, ОТЛИЧИЕ от AWS!). `![Описание скриншота](url)`. Чистый product-name-alt (`![OneAgent]`) оставляй EN. Нумерованные `![Step 1]`→`![Шаг 1]`.
- **Тултипы ссылок** `](url "English")` — переводить (корпус 310:1 RU). Product-name-тултип оставлять EN.
- **Bold-лейблы** `**Note:**`, `**Example:**`, `**Prerequisites**` → переводить.

## Анти-кальки

- «вы можете»→«можно»; «вы должны»→«необходимо/нужно»; «вы хотите»→«нужно/требуется». Условные «если вы используете/запускаете» — норма, НЕ трогать.
- НЕ `X: это Y` (норма дефиниции `X, это Y` запятая). Длинных тире `—` в RU быть НЕ должно (QA FAIL).
- Квантор + несклоняемое EN-сущ.: опорное русское слово («несколько экземпляров Cloud Run»).
- Зевгма: «для создания X и управления **ими**».

## Эталонные соседи (читать ДО перевода)

- OTel-языковые walkthroughs (для `opentelemetry-on-gcf-*`): `docs/managed-ru/ingest-from/opentelemetry/walkthroughs/{dotnet,go,nodejs,php}.md` — стиль OTel-инструкций (tracer/meter/exporter EN, span→спан).
- GCP guide: `docs/managed-ru/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/*.md` (готовые) — для set-up-gcp-integration-*.
- GCP integrations: `docs/managed-ru/ingest-from/google-cloud-platform/gcp-integrations/*.md` (готовые) — для cloudrun/legacy.
