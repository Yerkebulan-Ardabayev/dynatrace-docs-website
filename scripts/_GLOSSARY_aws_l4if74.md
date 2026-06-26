# Глоссарий перевода — ingest-from/amazon-web-services (L4-IF.74)

Заземлён грепом по 118 готовым RU-соседям (`docs/managed-ru/ingest-from/amazon-web-services`, 83 627 строк) через `scripts/_corpus_norms.py`. Эти нормы ОБЯЗАТЕЛЬНЫ — не изобретать свои.

## Как переводить (движок line-parity)

EN-исходник: `docs/managed/<REL>/<file>` → RU-результат: `docs/managed-ru/<REL>/<file>`.

Билдер на файл (`scripts/_build_awsXX_<slug>.py`):

```python
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
REL = "ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics"
TRANS = {
    "title: Monitor Amazon EC2": "title: Мониторинг Amazon EC2",
    "# Monitor Amazon EC2": "# Мониторинг Amazon EC2",
    "Some English prose line exactly as in the file (stripped).": "Русский перевод этой строки.",
}
PASS = {  # строки, остающиеся EN дословно (см. ниже что оставлять)
    "CloudWatch",
}
build_one(REL, "ec2-builtin.md", TRANS, PASS)
qa_one(REL, "ec2-builtin.md")
```

Правила движка:
- **Ключ TRANS = строка EN-файла, `.strip()`-нутая** (без ведущих/хвостовых пробелов). Отступ (indent) движок сохраняет сам — в значении RU отступ НЕ писать.
- Пустые строки, `---`, строки внутри ` ``` `-фенсов, `source:`/`scraped:` frontmatter — движок пропускает дословно. Их в TRANS НЕ класть.
- **Каждая** прочая непустая строка обязана быть либо в TRANS (перевод), либо в PASS (оставить EN). Иначе билдер кинет `UNTRANSLATED: '<repr>'`.
- Итерация: запускай билдер → на первой непокрытой строке он печатает `UNTRANSLATED: ...` → добавь её в TRANS или PASS → повторяй, пока не соберётся (`OK <file>: N lines`).
- Потом `qa_one(REL, file)` → добивайся **0 FAIL** (WARN разбираем вручную после).
- Билдер ПИШИ через файл (`Write`), НЕ печатай весь словарь в финальном ответе (лимит вывода). Финальный ответ — короткий: какие файлы собраны, сколько строк, статус QA, замеченные边 спорные места.

## Термины (корпус-норма AWS)

| EN | RU | Примечание |
|----|----|-----------|
| endpoint | эндпоинт | НЕ «конечная точка» |
| region | регион |  |
| bucket | бакет | (S3 bucket) |
| policy | политика | (в прозе; в JSON `policy` остаётся) |
| permission(s) | разрешение/разрешения | 617:0 |
| role | роль | в прозе; имена ролей и `role` в JSON/code остаются EN |
| credentials | учётные данные |  |
| instance | экземпляр |  |
| deployment | развёртывание |  |
| dashboard | дашборд |  |
| token | токен | (`API token` → «API-токен») |
| tag | тег |  |
| metric | метрика |  |
| namespace | **namespace (EN)** | CloudWatch namespace остаётся EN |
| Step N | Шаг N |  |
| environment | окружение / среда (как у соседей) |  |

## Оставлять EN (PASS / внутри прозы)

- **Product/service-names**: CloudWatch, Lambda, EC2, ECS, EKS, S3, IAM, ARN, App Runner, Elastic Beanstalk, Auto Scaling, Fargate, Spot Fleet, VPC, CloudFormation, Kinesis, SQS, SNS, RDS, DynamoDB и т.п.
- **img alt — EN** (корпус 209 EN : 24 RU). `![Lambda environment variables](url)` → alt НЕ переводить. **Исключение:** нумерованные шаги `![Step 1]` → `![Шаг 1]` (это единственный RU-класс alt в корпусе).
- **Имена метрик в таблицах** (CPUUtilization, NetworkIn, DiskReadOps…) — EN. Переводятся только описания/заголовки колонок («Метрика», «Описание», «Единица»).
- Код, команды, JSON, YAML, ARN, поля API — внутри ` ``` ` фенсов не трогаются движком; инлайновый `code` в бэктиках оставляй как есть.

## Переводить (НЕ оставлять EN — частые промахи субагентов)

- **`title:`-frontmatter и все `# H1`/`## H2`… заголовки прозы** — ПЕРЕВОДИТЬ (корпус 110 RU : 8 EN titles). `title: Monitor Amazon EKS` → `title: Мониторинг Amazon EKS`. EN остаётся только у чистого product-name-заголовка (`## CloudWatch`).
  Doc-type строки: `* How-to guide` → `* Практическое руководство`; `* Reference` → `* Справочник`; `* Tutorial` → `* Руководство`; `* N-min read` → `* Чтение: N мин`; `* Updated on Mon DD, YYYY` → `* Обновлено DD <месяц> YYYY г.`.
- **Тултипы ссылок** `](url "English text")` — переводить текст в кавычках (корпус 680 RU : 14 EN). Product-name-тултип (`"CloudWatch"`) оставлять EN.
- **Bold-лейблы** `**Default value**`, `**Possible values:**`, `**Example:**`, `**Note:**` → переводить («**Значение по умолчанию**», «**Возможные значения:**», «**Пример:**», «**Примечание:**»).

## Анти-кальки (русский стиль)

- «вы можете» → «можно»; «вы должны» → «необходимо/нужно»; «вы хотите» → «нужно/требуется». (Условные «если вы используете/запускаете» — норма, НЕ трогать.)
- НЕ ставить `X: это Y` — норма дефиниции `X, это Y` (запятая) или просто тире опускать. **Длинных тире `—` в RU быть НЕ должно вообще** (QA это FAIL-ит).
- Квантор + несклоняемое EN-сущ.: «два экземпляра EC2», «несколько ролей IAM» (опорное русское слово), не «два EC2 instance».
- Зевгма падежей: «для создания X и управления **ими**» (управление требует творительного), не «создания и управления X».

## Эталонные соседи (читать для стиля/терминов ДО перевода)

- `docs/managed-ru/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-api.md`
- `docs/managed-ru/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-spot-fleet.md`
- `docs/managed-ru/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs.md`
- `docs/managed-ru/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/troubleshoot-aws-monitoring-setup.md`
