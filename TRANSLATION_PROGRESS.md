# Translation Progress — docs/managed/ → docs/managed-ru/

## L4-IF.58 (2026-06-18, Opus 4.8): K8s guides/metadata-automation семья ЗАКРЫТА (+3)

**Прогресс:** 2401 -> 2404/2655 = 90.55%, pending 254 -> 251, orphan 0. Директория `setup-on-k8s/guides/metadata-automation` 0/3 -> 3/3 — ЗАКРЫТА. Переведены 3 прозовых гайда: custom-properties-file (файл пользовательских свойств через value/secret), build-label-propagation (распространение меток сборки в OneAgent через аннотации), metadata-enrichment (каталог обогащения `dt_metadata.*`).

**Метод:** чистый реюз прозового line-parity builder из L4-IF.57 (`_build_meta_l4if58.py`): EN построчно, code-fence-aware (внутри ``` байт-идентично), source/scraped/пустые/`---` переносятся как есть, проза из dict {stripped EN -> stripped RU} с переносом отступа, PASS-набор для пустых table-header/разделителей/имён файлов (`1. dt\_metadata.properties`), любая непокрытая прозовая строка -> SystemExit. MOJI_RE нормализует `ï»¿`/BOM в ключах и EN-строке. Line-parity точная 81/260/298.

**Каноны (durable, metadata-automation):** metadata enrichment->«обогащение метаданными», enrichment directory->«каталог обогащения», build label propagation->«распространение меток сборки», custom properties file->«файл пользовательских свойств», injected->«внедрённый», pods->«поды», webhook->«вебхук» (в прозе; в коде EN), namespace->«пространство имён», namespace selector->«селектор пространств имён», secret->«секрет», annotation->«аннотация», mapping->«сопоставление», `DT_RELEASE_*`/`mapping.release.dynatrace.com/*`/`feature.dynatrace.com/*`/`fieldPath`/`fieldRef`/`namespaceSelector`/`metadataEnrichment` -> backtick EN. Bold UI **Properties and tags** остаётся EN; `**Please note:**`->«**Обратите внимание:**» (callout-лейбл, не product-UI -> переводится). `* N-min read`->«* Чтение: N мин», `* Published Jul 28, 2023`->«* Опубликовано 28 июля 2023 г.», `* Updated on Jan 27, 2026`->«* Обновлено 27 января 2026 г.». Title-атрибуты ссылок переводятся; URL + in-page anchor (`#default-behavior`, `#operator-enrichment-directory`) байт-идентичны EN.

**Source-quirks / fidelity:** EN-мойибейк `ï»¿` (BOM mis-decoded as Latin-1) перед `]` в build-label-propagation L18/L227 -> RU очищен (не зеркалится, канон «RU чистый» + QA флагует mojibake). Дублированный H1 (scraper-артефакт, заголовок 2x в каждом файле) зеркалится. EN-кварк двойного пробела `.  If` в table-описаниях `mapping.release.*` зеркал в RU (`.  Если`).

**QA:** `_qa_meta_l4if58.py` 3/3 PASS, 0 FAIL / 0 WARN. line-parity точная, em-dash=0, mojibake=0, BOM=0, URL-identity, code-fence byte-identity (49/199/227 fenced-строк), heading-levels, frontmatter source/scraped byte-eq — ALL GREEN. EN не тронут (md5 baseline `_en_baseline58.md5` OK до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен — RU md5 идентичен pre/post).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент построчно 3 пары: 0 фабрикаций, 0 пропусков, 3 high-risk негации/условия верны («not overwritten»->«не будут перезаписаны», «aren't validated»->«не проверяются», «if OneAgent enabled / if no OneAgent enabled» оба ветвления), терминология консистентна внутри и между файлами, идентификаторы/числа/код байт-идентичны, **Properties and tags** EN, URL/anchor точны, em-dash=0. Мой скепт-проход ДО ревью поймал 2 дефекта (fidelity «about the pods»->genitive «версии недавно развёрнутых подов» вместо «для»; управление «задать **для** `feature...` значение») -> исправлены в builder, ребилд+ре-QA чисто. [[feedback_em_dash_translation_blindspot]] [[feedback_translation_qa_blindspots]]

**Next (251):** setup-on-k8s/guides остаток 41 (migration 16 вкл. api-version-migration-guides 8, deployment-and-configuration 16, networking-security-compliance 9) + deployment 16 + reference 6 + прочее. Дальше extensions 47 / OTel 51 / azure 32 / AWS-остаток 17 / GCP 15 / oneagent 13.

## L4-IF.57 (2026-06-17, Opus 4.8): K8s guides/container-registries семья ЗАКРЫТА (+5)

**Прогресс:** 2396 -> 2401/2655 = 90.43%, pending 259 -> 254, orphan 0. Директория `setup-on-k8s/guides/container-registries` 0/5 -> 5/5 — ЗАКРЫТА. Переведены container-registries.md (индекс в `guides/`) + use-public-registry, use-private-registry, verify-image-signature, prepare-private-registry (реестры контейнеров, pull secret, Cosign/SBOM/SLSA-проверка подписей).

**Метод:** прозовый line-parity builder (`_build_cr_l4if57.py`) расширен per-file PASS-набором для технических строк (табличные строки с image-refs `public.ecr.aws/...`, разделители `| --- |`, номера сносок, таб-лейблы Helm/Kustomize/Manifest/Cosign/GitHub CLI/Docker CLI, code-only пункты) — копируются байт-в-байт без translation-map. REL-словарь: индекс-файл в `guides/`, остальные 4 в `guides/container-registries/`.

**Каноны (durable, container registries):** private/public/built-in registry->частный/публичный/встроенный реестр, container image(s)->образ(ы) контейнера, supply chain attacks->атаки на цепочку поставок, immutable->неизменяемый, signed->подписанный, signature verification->проверка подписи, attestation->аттестация, SBOM->спецификация состава ПО (SBOM), SLSA build provenance->происхождение сборки SLSA, multi-arch->мультиархитектурные, pull secret->pull secret (не переводим), rate limiting->ограничение частоты запросов, egress traffic->исходящий трафик. Режимы (Cloud-Native/Classic Full-Stack, Application/Kubernetes Observability) остаются EN. Required/Optional badge->Обязательно/Необязательно, ## Prerequisites->Предварительные требования, ## Related topics->Связанные темы, ## Learn more->Узнать больше.

**QA + Critical review:** `_qa_cr_l4if57.py` 5/5 PASS 0 FAIL/0 WARN (line-parity 52/315/298/383/245, em-dash=0, mojibake/BOM=0, URL-identity, code-fence/frontmatter byte-eq). Critical manual re-read 5 RU ДО финала поймал 5 калек «вы можете»->безличные + 2 badge-тавтологии («Обязательно Обязательные»->«Все требования…кроме необязательных») -> правка в builder (источник истины), ребилд+ре-QA чисто. EN не тронут.

## L4-IF.56 (2026-06-17, Opus 4.8): K8s high-availability семья ЗАКРЫТА (+3), mojibake-фикс соседа failure-policy

**Прогресс:** 2393 -> 2396/2655 = 90.24%, pending 262 -> 259, orphan 0. Директория `setup-on-k8s/guides/high-availability` 1/4 -> 4/4 — ЗАКРЫТА. Переведены 3 прозовых гайда: api-request-threshold (минимальный интервал между запросами), priority (priorityClass для критичных компонентов), high-availability (HA вебхука Operator). Первый не-AWS прозовый батч после AWS-серии: движок e44 (метрик-таблицы) НЕ применим, нужен line-parity перевод прозы.

**Метод:** новый builder `_build_haf_l4if56.py` (не e44): читает EN построчно, code-fence-aware, переносит source/scraped/блоки-кода/пустые строки байт-идентично, прозу берёт из dict {stripped EN line -> stripped RU line} с переносом отступа, пишет LF. Mojibake-insensitive lookup (`ï»¿`/BOM в ключах нормализуются). Любая непокрытая прозовая строка -> SystemExit (ловит leftover-EN). Line-parity 66/16/143 точная.

**Каноны (durable, K8s Operator guides):** `* 1-min read`->«* Чтение: 1 мин», `* Published Jul 28, 2023`->«* Опубликовано 28 июля 2023 г.», `* Updated on Feb 27, 2026`->«* Обновлено 27 февраля 2026 г.», `Dynatrace Operator version X+`->«Dynatrace Operator версии X+». pods->«поды», CSI driver->«CSI-драйвер», webhook->«вебхук» (в прозе; в коде/identifier'ах EN), priorityClass/replicas/topologySpreadConstraints/podDisruptionBudget/highAvailability/whenUnsatisfiable/ScheduleAnyway/DoNotSchedule -> backtick EN. high availability->«высокая доступность», topology spread constraints->«ограничения распределения (подов) по топологии», pod disruption budget->«бюджет прерывания работы подов», deprecated->«устарело»/«устаревш-», Legacy->«Прежнее», backward compatibility->«обратная совместимость», graceful shutdown->«корректное завершение работы». Title-атрибуты ссылок переводятся; in-page anchor (`#configure-high-availability`) и все URL байт-идентичны EN (канон URL-identity).

**Source-quirks / fidelity:** EN-мойибейк `ï»¿` (U+00EF U+00BB U+00BF, BOM mis-decoded as Latin-1) перед `]` в 3 ссылках (priority L14, high-availability L137/L141) -> RU очищен (не зеркалится; канон «RU чистый» + QA флагует mojibake). EN-комментарий в code-fence `# Deprecated, use the following values instead` НЕ переводится (внутри ```). em-dash в L126-дефиниции обойдён: «значением по умолчанию … является X вместо прежнего Y» (без «—»).

**Mojibake-фикс соседа (drive-to-closure):** уже зашипленный `failure-policy.md` (та же директория, вне pending) содержал 2 реальных мойибейка `` `silent`â ``/`` `fail`â `` = U+00E2 (обрывок UTF-8 em-dash `â€"` = U+2014). Independent-review субагент подтвердил. Исправлено -> `` `silent`: если… ``/`` `fail`: если… `` (двоеточие, §0 запрещает em-dash). Line-parity 41/41 сохранена, LF.

**QA:** `_qa_l4if56.py` 3/3 PASS, 0 FAIL / 2 WARN (calque «Вы можете» — есть и в зашипленном failure-policy.md, accepted). Comprehensive скан всех 4 HA-файлов: line-parity точная, em-dash=0, mojibake=0, URL-identity, code-fence byte-identity, frontmatter source/scraped byte-eq — ALL GREEN. EN не тронут (md5 baseline `_en_baseline56.md5` OK до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 1 MINOR -> SHIP):** Independent-review субагент построчно 3 пары: 0 инверсий смысла (true/false/ignored/default, ScheduleAnyway-vs-DoNotSchedule, higher-priority, scheduled-by-Kubernetes passive, last-remaining-pod, previously/now верны), все версии/числа/код-токены/URL/anchor байт-идентичны, title-атрибуты переведены, грамматика чистая. 1 MINOR: api L60 «requests for:» смягчён до «:»+список (читается верно). Мой скепт-проход поймал ДО ревью 3 грам-дефекта (genitive «версий»->«В версиях», управление «задать для X значение», висячее деепричастие «располагая узлы»->«причём узлы находятся») — исправлены, ребилд+ре-QA.

**Next (259):** setup-on-k8s 76->73 (остаток guides: deployment-and-configuration, migration, networking-security-compliance, metadata-automation, troubleshooting). Дальше OTel 51 / extensions 47 / azure 32 / AWS-остаток 19 (под-директории вне aws-all-services) / GCP 15 / oneagent 13 / technology-support 6.

## L4-IF.54+55 (2026-06-17, Opus 4.8): AWS broken-header батч ЗАКРЫТ (+5), aws-all-services 84/84 ПОЛНОСТЬЮ, словарь 1613->1754

**Прогресс:** 2388 -> 2393/2655 = 90.13%, pending 267 -> 262, orphan 0, все source = Managed (EN md5 baseline 0 diff). **Директория `aws-all-services` 79 -> 84/84 — ЗАКРЫТА ПОЛНОСТЬЮ.** Закрыты последние 5 broken-header: dynamodb-new, rds-new (1402 стр), trusted-advisor, glue (L4-IF.54, +4) + iot (L4-IF.55, +1, вынесен отдельно из-за mislabeled-header). 89 + 52 уникальных строк (2 ship-группы под планкой ~130).

**Метод:** реюз e44-движка + **3 broken-header COLMAP_OVERRIDE сигнатуры в B.TABLES** (header переводится по literal-тексту, per-column actions по фактическому смыслу колонок):
1. `Name|Description|Dimensions|Unit|Recommended` -> `['en','tr','en','unit','applic']` (dynamodb-new, rds-new)
2. `Name|Description|Statistics|Unit|Dimensions|Recommended` -> `['en','tr','en','unit','en','applic']` (glue — header консистентен с данными: Stat-колонка=статистики, Unit-колонка=единицы)
3. `Name|Unit|Statistics|Dimensions|Recommended` -> `['en','unit','en','en','applic']` (trusted-advisor, без Description)

**iot (L4-IF.55) — отдельный build:** та же сигнатура #2, НО данные MISLABELED (под "Statistics" стоят единицы `Count`, под "Unit" — статистики `Sum`), поэтому actions `['en','tr','unit','en','en','applic']` (col2=unit, col3=en) — faithful mirror AWS-бага. iot нельзя в один build с glue (одинаковый header, противоположный порядок данных). Словарь 1613->1702 (+89) ->1754 (+52). titles 79->83->84. Merge self-validation 89/89 и 52/52. analyzer 0 ROW?/UNIT?/APPLIC? в обоих. Flag-guard=0, em-dash=0.

**Каноны (durable, broken-header):** Name остаётся EN (findability) во всех; Description->перевод, Statistics (Sum/Average/Maximum/Multi)->EN, Dimensions->EN, Unit->перевод, Recommended (Applicable->Применимо). DynamoDB: capacity units->«единицы ёмкости», provisioned->«подготовленные», on-demand->«по требованию», global secondary index->«глобальный вторичный индекс», throughput->«пропускная способность», throttle->«регулирование», items->«элементы». RDS: burst bucket->«корзина всплеска», I/O credits->«кредиты ввода-вывода», throughput credits->«кредиты пропускной способности», swap space->«пространство подкачки», incoming(receive)/outgoing(transmit)->«входящий(принимаемый)/исходящий(передаваемый)», read from/written to disk->«прочитанных с/записанных на диск». Glue: executor->«исполнитель», JVM heap->«куча JVM», driver->«драйвер», stages/tasks->«этапы/задачи», killed->«принудительно завершённых», shuffle->«перемешивание», Spark/ETL EN, scale `0`-`1`->«шкала `0`-`1`». IoT: message broker->«брокер сообщений», dimension->«измерение», contains->«содержит», throttled->«подвергнутых регулированию», job execution->«выполнение задания», rules engine->«механизм правил», status-коды/MQTT-типы/shadow-ops EN в backticks.

**Source-quirks (зеркалены, no_unverified_claims):** rds-new 4 EN-описания ОБРЕЗАНЫ в источнике (`EBSIOBalance%`/`EBSByteBalance%` «...is available [for basic]», Network*Throughput «...and Amazon RDS», `BinLogDiskUsage` «...MariaDB instances,») -> RU обрывается в той же точке, НЕ дополняется. iot mislabeled header (Count под Statistics, Sum под Unit) -> зеркал. iot `ServerError` (стр.801) EN: Protocol-текст при `Region, JobId`-измерениях (AWS баг) -> зеркал. UNSUBSCRIBE rate-метрика EN говорит «rejected» (НЕ «throttled» как CONNECT/SUBSCRIBE/PUBLISH) -> RU «отклонённых» (self-validation поймала мою опечатку «throttled» ДО записи). rds-new сотни дубль-строк метрик с пустым EN-Description (разные Dimensions) -> пустые RU.

**QA:** `_qa_aws_l4if54.py` 4/4 + `_qa_aws_l4if55.py` 1/1 PASS, 0 FAIL/0 WARN. Независимый python-скан: line-parity все (871/1402/793/851/815), em-dash=0, mojibake-introduced=0, inline backtick multiset EN==RU 0 diff. EN не тронут (md5 baseline 0 diff до/после 2 ревью-субагентов, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** 2 independent-review субагента. L4-IF.54 (4 файла, спот-чек ~30 Description в rds-new): направления Read/Write/Receive/Transmit/ReadThroughput/WriteThroughput НЕ инвертированы, 4 обрезки зеркалены без дополнения, негации целы, broken-header порядок верен, числа/коды (HTTP 500/400, gp2, scale 0-1) целы, пустые EN->пустые RU. L4-IF.55 iot (cause-distinction sweep): 3 «rejected»-причины (quotas/internal error/rate) различены, throttled-vs-rejected-on-rate верно по метрике, авторизация-направление (could not authorize, made by broker outbound) верна, status changed-to vs status-is различены, mislabel + ServerError-баг зеркалены. [[feedback_translation_qa_blindspots]] [[feedback_em_dash_translation_blindspot]]

**Next (262):** **aws-all-services ПОЛНОСТЬЮ ЗАКРЫТА (84/84).** Дальше: проверить остальные AWS-поддиректории managed-ru (integrate-into-aws, cloudwatch-metrics, aws-metrics-ingest — в git помечены удалёнными из рабочего дерева 6 файлов: app-runner, cloudwatch-metric-streams, ec2-api, ec2-spot-fleet, cloudwatch-ecs, ecs-container-insights — проверить статус). Затем K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.53 (2026-06-17, Opus 4.8): AWS aws-service — builtin батч (+6), словарь 1581->1613

**Прогресс:** 2382 -> 2388/2655 = 89.94%, pending 273 -> 267, orphan 0, все source = Managed (EN md5 baseline 0 diff). Директория `aws-all-services` 73 -> 79/84 (осталось 5). Закрыты все 6 builtin-файлов: application-and-network-load-balancer / dynamo-db / elastic-block-store-ebs / elastic-load-balancer / rds / s3 (все `(built-in)`). 32 уникальные prose-строки + 6 titles — глубоко под планкой ~130 (метрик-таблицы переводят только Unit+заголовок, проза в основном уже в shipped-словаре от L4-IF.44-52).

**Метод:** чистый реюз e44-движка (`_build_aws_l4if53.py` импортит `_build_aws_l4if44` + durable UNIT-расширение). **Новая builtin TABLE-сигнатура в B.TABLES** (канон azure builtin L4-IF.42): `Metric key|Name|Unit|Aggregations|Monitoring consumption` -> заголовок + колонка Unit переводятся, ВСЕ identifier-колонки EN byte-identical: Metric key, **Name** (findability-метка в Metrics browser, как GCP/Azure builtin), Aggregations (autovalue/autoavgmaxmin), Monitoring consumption (DDUs). Переводы прозы в `_aws_merge53.py`, словарь `_aws_trans_l4if43.json` 1581->1613 (+32), `_aws_titles_l4if43.json` 73->79 (+6). intro = форма V1. Merge self-validation 32/32 (0 непокрытых / 0 неиспользованных). analyzer: 0 ROW?/UNIT?/APPLIC?/CELL. Flag-guard=0. em-dash=0 с 1-й итерации.

**Каноны (durable, builtin):** Unit `Percent (%)` -> «Процент (%)», `Per second` -> «В секунду» (shipped managed-ru канон, 27x), `Byte/second` -> «Байт в секунду», `Byte` -> «Байт» (все подтверждены grep'ом по shipped managed-ru, не выдуманы). Builtin-заголовок = `Ключ метрики|Имя|Единица измерения|Агрегации|Потребление мониторинга` (точно как azure-ru). Pure product-name title без «monitoring» -> identity EN (`Amazon ELB (Elastic Load Balancer) (built-in)`); title с «monitoring» -> «Мониторинг X (built-in)». «built-in» в скобках оставлен EN (azure-канон). View-metrics flow (AWS account page): «странице учётной записи AWS» (зеркалит azure account-page канон L4-IF.42), «Перейдите в **AWS**», «Выберите поле **Service**». «out-of-the-box» -> «из коробки», «Management Zones» -> «зоны управления» (350x shipped, без EN в скобках), «main dimension» -> «Основное измерение: `X`.». В метрик-таблицах Name остаётся EN (findability-метка).

**QA:** `_qa_aws_l4if53.py` 6/6 PASS, 0 FAIL/0 WARN. Независимый python-скан: line-parity 6/6 (686/734/730/726/734/640), em-dash=0, mojibake-introduced=0 (EN-mojibake в JSON-fence/captions byte-identical, не внесён мной), inline backtick-span multiset EN==RU 0 diff. EN не тронут (md5 baseline `_aws_batch53` 0 diff до/после ревью-субагента; managed/ builtin clean в git, [[feedback_workflow_agents_may_write]] проверен — субагент тронул 0 моих EN).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (построчно 6 пар, фокус на дельте EN!=RU) — 0 находок. Подтверждено: Name-колонка EN (канон), Unit переведён, identifier-колонки/JSON(~400 строк)/URL byte-identical, негации сохранены («**не** поддерживает зоны управления», «специфичных… нет, но…»), ELB title корректно EN, терминология консистентна по 6 файлам, em-dash=0. Мой скепт-проход (rendered builtin-таблица): Count -> Количество / Percent (%) -> Процент (%) переведены, Metric key/Aggregations/DDUs EN, заголовок канон.

**Next (267):** AWS aws-service остаток 5 в `aws-all-services` — broken-header (COLMAP_OVERRIDE через B.TABLES): **dynamodb-new** + **rds-new** (общая сигнатура `Name|Description|Dimensions|Unit|Recommended`, rds-new 1402 строки с частыми пустыми Description), **iot** (6-col `Name|Description|Statistics|Unit|Dimensions|Recommended` — Stat<->Unit swap против standard), **trusted-advisor** (5-col `Name|Unit|Statistics|Dimensions|Recommended` — без Description, минимум перевода), **glue** (metric-таблица после длинной Permissions-таблицы + instruction-блок «To ingest additional observability metrics»). Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.52 (2026-06-16, Opus 4.8): AWS aws-service — Amazon Kinesis standard батч (+1), словарь 1424->1581

**Прогресс:** 2381 -> 2382/2655 = 89.72%, pending 274 -> 273, orphan 0, все source = Managed (verify_corpus подтвердил +1, 0 без source / 0 non-managed). Директория `aws-all-services` 73/84 (осталось 11). Закрыт последний standard-формат streaming-файл: `aws-service-kinesis.md` (4 подтаблицы: Kinesis Data Analytics/Flink, Data Firehose, Data Streams KDS, Video Streams). 157 уникальных строк (146 описаний метрик + intro + H1 + read-time + date + 4 EN-подзаголовка + 3 main-dimension). Выше планки ~130, но это один цельный файл; нарочно отделён от msk-kafka (L4-IF.51) ради tractable-ревью (дедуп между двумя файлами ~0: 224 ячейки -> 223 уникальных).

**Метод:** чистый реюз e44-движка (`_build_aws_l4if52.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). Standard metric-таблица уже в базовом TABLES — расширений НЕ потребовалось (analyzer ROW?/UNIT?/APPLIC?=0). Переводы в `_aws_merge52.py`, словарь `_aws_trans_l4if43.json` 1424->1581 (+157), `_aws_titles_l4if43.json` 72->73 (+1). intro = форма V1. Продуктовые подзаголовки `### Amazon Kinesis Data Analytics` / `### Amazon Data Firehose` / `### Amazon Kinesis Data Streams (KDS)` / `### Amazon Kinesis Video Streams` = identity EN (канон `### ActiveMQ`/SageMaker). Merge self-validation 157/157 (0 непокрытых / 0 неиспользованных). Flag-guard=0. em-dash=0 с 1-й итерации.

**Каноны (durable, Kinesis/Flink/streaming):** stream -> «поток», data stream -> «поток данных», delivery stream -> «поток доставки», streaming source -> «потоковый источник», shard -> «шард», record -> «запись», consumer applications -> «потребительские приложения», delivered to X -> «доставленных в X», indexed/copied -> «проиндексированных/скопированных», put to -> «помещённых в», retrieved from -> «извлечённых из», backup -> «резервное копирование», failover -> «отработка отказа», throttling/throttled -> «регулирование», provisioned throughput exceeded -> «превышение подготовленной пропускной способности», bucket -> «корзина». Flink: operator/task -> «оператор/задача», task manager -> «менеджер задач», checkpoint -> «контрольная точка», watermark -> «водяной знак» (received/emitted -> «полученный/отправленный» — направление!), back pressure -> «обратное давление», idle -> «простаивает», offset commit -> «фиксация смещения», garbage collection -> «сборка мусора» (old -> «старого поколения»), heap -> «куча», KPU -> «единицы обработки Kinesis» (без `(KPU)` — нет в источнике). Video: fragment -> «фрагмент», frame -> «кадр», sent out from service -> «отправленных из сервиса», received by KVS -> «получен Kinesis Video Streams»; ACK-типы (`Buffering ACK`/`Persisted ACK`/`Received ACK`), `InletService`, `COPY`, status `Dropped`/`OK`/`ProcessingFailed`, Lambda/Flink/Kafka/Splunk/Redshift/NaN/CPU/HLS/HTTP и все API-имена EN. Success-rate «`1` ... successful ... `0` ... failure» -> «значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою» (обход em-dash, [[feedback_em_dash_translation_blindspot]]); «Age is the difference» -> «Возраст представляет собой разницу» (обход «X — это Y»). Статистики Minimum/Maximum/Average оставлены EN в прозе (канон Statistics-значений). read-time «Чтение: 33 мин», дата «Обновлено 10 января 2025 г.».

**Source-quirks / fidelity (зеркалены, не «исправлены»):** (a) `LambdaDelivery.DeliveryFailedRecords` EN-описание = «The number of successful Lambda invocations by Kinesis Data Analytics.» (AWS mislabel: метрика про failed-records, а текст про successful invocations) -> RU зеркалит дословно «Количество успешных вызовов Lambda…» (no_unverified_claims, не «чиню»). (b) Один KDS-ряд `GetRecords.Latency` EN «per GetRecords operation» БЕЗ backticks -> RU тоже без backticks (остальные вхождения `GetRecords` в backticks). (c) EN строка 29 BOM-мойибейк в «AWS IAM policy» -> RU чистый. Множество дубль-строк метрик с пустым EN-описанием (разные Statistics/Dimensions) -> пустые RU построчно.

**QA:** `_qa_aws_l4if52.py` 1/1 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq, em-dash, mojibake/BOM, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый python-скан: line-parity 1110/1110, em-dash=0, mojibake/BOM=0, inline backtick-span multiset EN==RU (217/217, 0 diff, fence-aware), все API/ACK/status/`InletService`-коды присутствуют. Регрессия qa43/47/48/49/50/51 PASS 0. EN не тронут (md5 baseline `_review_baseline52.md5` идентичен до/после ревью-субагента + `_en_baseline52.md5` 0 diff, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (8 категорий, все 4 подтаблицы построчно) — 0 находок. read/written (input/output stream), received/emitted (watermarks, In/Out records), retrieved-from/put-to, sent-out-from-service/received-by-KVS, delivered-to S3/ES/Redshift/Splunk (цели не перепутаны), bytes/records, fragments/frames/bytes (Video) НЕ инвертированы; success(`1`)/failure(`0`) верны; backtick-absence edge-case (`GetRecords`) верен; статистики EN; пустые ячейки сохранены; 2 EN-source-дефекта (LambdaDelivery mislabel, BOM) зеркалены/обойдены, не translation-ошибки. Мой скепт-проход (rendered) подтвердил: пустые EN -> пустые RU, 0 конкурирующих форм терминов (поток/доставка/шард/запись единообразны), double-space не внесён.

**Next (273):** AWS aws-service остаток 11 в `aws-all-services` — 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура движка, канон azure builtin L4-IF.42): application-and-network-load-balancer / dynamo-db / elastic-block-store-ebs / elastic-load-balancer / rds / s3; 4 broken-header (COLMAP_OVERRIDE как Ground Truth): dynamodb-new / rds-new 574 / glue / iot; trusted-advisor. Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.51 (2026-06-16, Opus 4.8): AWS aws-service — Amazon MSK (Kafka) standard батч (+1), словарь 1358->1424

**Прогресс:** 2380 -> 2381/2655 = 89.68%, pending 275 -> 274, orphan 0, все source = Managed (verify_corpus подтвердил +1, 0 без source / 0 non-managed). Директория `aws-all-services` +1 (`aws-service-msk-kafka.md`). 66 уникальных строк (62 описания метрик + intro + H1 + date + main-dimension), под проверенной планкой батча ~130.

**Метод:** чистый реюз e44-движка (`_build_aws_l4if51.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). Standard metric-таблица (`Name|Description|Unit|Statistics|Dimensions|Recommended`) уже в базовом TABLES — расширений НЕ потребовалось (analyzer ROW?/UNIT?/APPLIC?=0, чистый standard). Переводы в `_aws_merge51.py`, словарь `_aws_trans_l4if43.json` 1358->1424 (+66), `_aws_titles_l4if43.json` 71->72 (+1). intro = форма V1. Merge self-validation 66/66 (0 непокрытых / 0 неиспользованных). Flag-guard=0. em-dash=0 с 1-й итерации.

**Каноны (durable, Kafka):** broker -> «брокер», consumer -> «потребитель», produce (операция) -> «запись», partition -> «партиция», topic -> «топик», leader -> «лидер», leader replicas -> «реплики-лидеры», follower -> «фолловер» (follower request -> «запрос фолловера»), offset lag -> «отставание смещения» (max -> «максимальное» / aggregated -> «совокупное»), throttle/throttled -> «регулирование» (throttle queue -> «очередь регулирования», exempt from throttling -> «освобождённых от регулирования», throttled bytes -> «байт, подвергнутых регулированию»), fetch -> «извлечение», Rx/Tx -> «приём/передача» (dropped receive/transmit packages -> «отброшенных пакетов при приёме/передаче», received/transmitted by the broker -> «полученных/переданных брокером», network receive/transmit errors -> «сетевых ошибок приёма/передачи»), CPU idle time -> «времени простоя CPU», kernel/user space -> «пространство ядра / пользовательское пространство», network processors / request handler threads are idle -> «сетевые процессоры / потоки обработчика запросов простаивают», broker network and I/O threads -> «сетевые потоки и потоки ввода-вывода брокера», swap memory -> «память подкачки», under minIsr -> «ниже minIsr», under-replicated -> «с недостаточной репликацией», root disk -> «корневой диск», application/data logs -> «журналы приложения/данных», message conversions -> «преобразования сообщений». CPU/ZooKeeper/minIsr/NaN/bold-литералы (**Decommissioned** и т.п.) EN. `ZooKeeperSessionState` code-spans (`NOT_CONNECTED`:`0.0` ... `AUTH_FAILED`:`10.0`) байт-верны; «which may be one of the following» -> «который может принимать одно из следующих значений» (двоеточие, без em-dash).

**Source-quirks / fidelity (зеркалены):** `ProduceLocalTimeMsMean` EN-описание = «The mean time in milliseconds for the follower to send a response» (дубль `FetchFollowerResponseSendTimeMsMean`, AWS copy-paste) -> RU зеркалит тот же текст для обеих метрик (дедуп в 1 ключ); `FetchConsumerResponseSendTimeMsMean` EN-описание ПУСТОЕ (в отличие от Follower-близнеца) -> пустая RU; множество дубль-строк метрик с пустым EN (разные Statistics/Dimensions) -> пустые RU построчно.

**QA:** `_qa_aws_l4if51.py` 1/1 PASS, 0 FAIL/0 WARN. Независимый python-скан: line-parity 992/992, em-dash=0, mojibake/BOM=0, inline backtick-span multiset EN==RU (182/182, 0 diff, fence-aware), ZooKeeper-коды все присутствуют. Регрессия qa43/47/48/49/50 PASS 0. EN не тронут (md5 baseline до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (все ~149 строк таблиц построчно) — 0 находок. Направления In/Out (received from / sent to clients), Rx/Tx, free/used memory, earned/used credits, consumer/follower (не спутаны), max/aggregated offset lag, request/response queue НЕ инвертированы; негации (offline / under minIsr / under-replicated / exempt / idle) целы; ZooKeeper-коды байт-верны; терминология консистентна; пустые ячейки сохранены; ProduceLocalTime/FetchFollower-кварк зеркален верно (идентичный RU для обеих). Мой скепт-проход (rendered) подтвердил.

## L4-IF.50 (2026-06-16, Opus 4.8): AWS aws-service — streaming/messaging standard батч (+2), словарь 1254->1358

**Прогресс:** 2378 -> 2380/2655 = 89.64%, pending 277 -> 275, orphan 0, все source = Managed (verify_corpus подтвердил +2, 0 без source / 0 non-managed). Директория `aws-all-services` 70 -> 72/85 (осталось 13). Закрыта пара streaming/messaging: simple-message-queue-mq (Amazon MQ: ActiveMQ + RabbitMQ), elastic-mapreduce-emr (Amazon EMR). 104 уникальные строки (cells+проза), под проверенной планкой батча ~130.

**Метод:** чистый реюз e44-движка (`_build_aws_l4if50.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). Standard metric-таблица (`Name|Description|Unit|Statistics|Dimensions|Recommended`) уже в базовом TABLES — расширений НЕ потребовалось (analyzer ROW?/UNIT?/APPLIC?=0 в обоих, чистый standard). Переводы в `_aws_merge50.py`, общий словарь `_aws_trans_l4if43.json` 1254 -> 1358 (+104), `_aws_titles_l4if43.json` 69 -> 71 (+2). Оба intro = форма V1 (дословный shipped-шаблон). Merge self-validation: 104/104 matched (0 непокрытых / 0 неиспользованных). Flag-guard = 0. em-dash=0 с 1-й итерации.

**Каноны (durable, messaging/streaming):** broker -> «брокер», consumer -> «потребитель», producer -> «производитель», message -> «сообщение», destination -> «место назначения», queue -> «очередь», topic -> «топик», durable topic subscriber -> «устойчивый подписчик топика», acknowledged -> «подтверждённый», per minute -> «в минуту», network connector -> «сетевой коннектор», remote broker -> «удалённый брокер», journal files -> «файлы журнала», clean/unclean shutdown -> «штатное/нештатное завершение работы», job scheduler store -> «хранилище планировщика задач», storage/memory limit -> «лимит хранилища/памяти», non-persistent messages -> «непостоянные сообщения», transactions in progress -> «выполняемые транзакции», compute units -> «вычислительные единицы»; RabbitMQ: channel -> «канал», exchange -> «обменник», ready/unacknowledged messages -> «готовые/неподтверждённые сообщения», published -> «опубликованные», file descriptors -> «файловые дескрипторы», node -> «узел». EMR/Hadoop: YARN/HDFS/MapReduce/HBase/Hadoop EN; application -> «приложение», submitted -> «отправленных», completed/failed-to-complete/killed/pending/running -> «завершились / не удалось завершить / принудительно завершены / в состоянии ожидания (Pending) / выполняются» (НЕ путать, разные глаголы); resource container -> «контейнер ресурсов», resource manager -> «менеджер ресурсов», allocated/reserved/available/total -> «выделенный/зарезервированный/доступный/общий»; core node -> «основной узел», task node -> «узел задач», task tracker -> «трекер задач», data node -> «узел данных»; block -> «блок», replication -> «репликация», corrupt(ed) -> «повреждённый», bytes read from / written to HDFS|S3 -> «прочитанных из / записанных в» (направление!); job -> «задание» / task -> «задача» (различие!), map/reduce task -> «задача map/reduce», map slots -> «слоты map», scheduler -> «планировщик», idle -> «простаивает», accruing charges -> «накапливать расходы», backup -> «резервное копирование», elapsed minutes -> «прошедшие минуты», five-minute intervals -> «с интервалом в пять минут». bold литеральные состояния **Decommissioned/Lost/Rebooted/Unhealthy** остаются EN (канон lex/UI). Даты «Published Sep 08, 2020»/«Published Oct 15, 2020» и read-time «7-min/12-min read» уже в словаре с прошлых батчей.

**Source-quirks / fidelity (зеркалены, не «исправлены»):** (a) EMR `YARNMemoryAvailablePercentage` EN-описание начинается с опечатки «he percentage» (съеден T) -> RU нормальная грамматика «Процент …» (канон api-gateway/SES L4-IF.45), code-span `YARNMemoryAvailablePercentage`/`MemoryAvailableMB`/`MemoryTotalMB` байт-верны. (b) EMR `LiveDataNodes` EN-описание «percentage of data nodes» при Unit-колонке `Count` (кварк AWS) -> текст зеркалю «Процент …», unit-ячейку зеркалю «Количество». (c) MQ `CpuUtilization` (ActiveMQ) EN без финальной точки vs `SystemCpuUtilization` (RabbitMQ) EN с точкой — одинаковый текст, RU зеркалит различие точки построчно (две разные записи словаря). Дубль-строки метрик с пустым EN-описанием (разные Dimensions/Statistics: ConsumerCount/DequeueCount/…/Apps*/*Requested/*VCPU*) -> пустые RU построчно.

**QA:** `_qa_aws_l4if50.py` 2/2 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый python-скан по 2 RU: em-dash=0, mojibake=0/BOM=0, line-parity 920/901 точная, inline backtick-span multiset EN==RU (145/100 спанов, 0 diff, fence-aware). Регрессия qa43/47/48/49 PASS 0. EN не тронут (md5 baseline идентичен до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (все ~197 строк таблиц построчно EN/RU, фокус direction/polarity + negation + numbers + terminology) — 0 находок. Направления сверены с именами метрик и НЕ инвертированы: AppsCompleted/Failed/Killed/Pending/Running/Submitted, HDFS/S3 read-from/written-to, NetworkIn/Out, core-vs-task nodes, memory allocated/reserved/available/total, map-vs-reduce. Негации целы (couldn't/not-acknowledged/not-yet-allocated/no-replicas/does-not-apply); числа/коды/формулы (`0`/`1`/2000/100/256K/пять-минут/backtick-токены) целы; bold-состояния EN; обе CpuUtilization-формы с верным различием точки; 3 source-quirk зеркалены верно. Мой скепт-проход (rendered RU): пустые EN -> пустые RU, 0 конкурирующих форм терминов (место назначения/брокер/задание-vs-задача единообразны), double-space не внесён (совпадения = пустые ячейки `|  |` permission-таблицы, байт-идентичны EN).

**Next (275):** AWS aws-service остаток 13 в `aws-all-services` — streaming 2 (kinesis 171 / msk-kafka 73, ~244 строки) + 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура, канон azure builtin L4-IF.42) + 4 broken-header (dynamodb-new / rds-new 574 / glue / iot — COLMAP_OVERRIDE как Ground Truth) + trusted-advisor. Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.49 (2026-06-15, Opus 4.8): AWS aws-service — storage/network standard батч (+5), словарь 1125->1254

**Прогресс:** 2373 -> 2378/2655 = 89.53%, pending 282 -> 277, orphan 0, все source = Managed (verify_corpus подтвердил +5, 0 без source / 0 non-managed). Директория `aws-all-services` 64 -> 69/84. Закрыта семантическая семья «хранилище/сеть» (план L4-IF.47 Next): ebs-new (EBS), simple-storage-service-s3 (S3), storage-gateway, transit-gateway, elasticsearch-service-es (ES). 129 уникальных строк (cells+проза), проверенная планка батча ~130.

**Метод:** чистый реюз e44-движка (`_build_aws_l4if49.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). Standard metric-таблица (`Name|Description|Unit|Statistics|Dimensions|Recommended`) уже в базовом TABLES — расширений НЕ потребовалось (analyzer ROW?/UNIT?/APPLIC?=0 во всех 5, чистый standard). Переводы в `_aws_merge49.py`, общий словарь `_aws_trans_l4if43.json` 1125 -> 1254 (+129), `_aws_titles_l4if43.json` 64 -> 69 (+5). Все 5 intro = форма V1 (дословный shipped-шаблон). Merge self-validation: 129/129 matched (0 непокрытых / 0 неиспользованных) — поймала 1 опечатку до записи (см. source-quirk ebs). Flag-guard = 0. em-dash=0 с 1-й итерации.

**Каноны (durable):** burst bucket -> «корзина всплеска», I/O credits -> «кредиты ввода-вывода», throughput credits -> «кредиты пропускной способности», volume create credits -> «кредиты создания тома», normalized to 256K capacity units -> «нормализованных к единицам ёмкости по 256 КБ», snapshot -> «моментальный снимок», Availability Zone -> «зона доступности», IOPS -> «IOPS» (EN); gateway -> «шлюз», cache storage -> «кэш-хранилище», dirty (cache) -> «грязный», upload buffer -> «буфер выгрузки», working storage -> «рабочее хранилище», recovery point -> «точка восстановления», on-premises applications -> «локальные приложения», reporting period -> «отчётный период», NFS/SMB sessions -> «сеансы NFS/SMB», gateway VM -> «виртуальная машина шлюза»; transit gateway -> «транзитный шлюз», cross-account service -> «межаккаунтный сервис», black hole route -> «маршрут чёрной дыры», did not match a route -> «несоответствие ни одному маршруту», multicast -> «многоадресный», `IGMP Join/Query/Leave` -> backtick EN; bucket (S3) -> «корзина S3», downloaded/uploaded -> «скачанных/отправленных» (различие направления!), request/response body -> «тело запроса/ответа», HTTP 4xx/5xx client/server error -> «ошибки клиента/сервера», average/sum statistic -> «статистика average/sum» (значения EN); data nodes -> «узлы данных», dedicated master nodes -> «выделенные мастер-узлы», shards -> «шарды», primary/replica shards -> «первичные шарды / шарды-реплики», Java heap -> «куча Java», data at rest -> «данные в состоянии покоя», KMS customer master key -> «главный ключ клиента KMS», segment merges -> «слияния сегментов», searchable documents -> «документы, доступные для поиска», CPU credits -> «кредиты CPU», T2 instance types -> «типы экземпляров T2», accepting/blocking -> «принимает/блокирует». bold UI EN (**Amazon S3 service**, **AWS S3**), bold-негация **не** (канон lex.md). `* N-min read` -> «* Чтение: N мин»; `* Updated on Apr 08, 2025` -> «* Обновлено 8 апреля 2025 г.». built-in prose канон lambda-new: «Этот сервис отслеживает часть … Пока этот сервис настроен, нельзя включить сервис X (built-in)» (имя `(built-in)` EN).

**Source-quirks / fidelity (зеркалены, не «исправлены»):** (a) ebs `EBSReadOps` EN «all **Amazon EBS** volumes», но `EBSWriteOps` EN «all **EBS** volumes» (без Amazon) -> RU зеркалит различие построчно (merge self-validation поймала, пока ключ был унифицирован). (b) storage-gateway `WriteBytes` EN «written **to** … applications» vs `WriteTime` EN «write operations **from** … applications» (EN сам непоследователен) -> RU зеркалит каждый предлог. (c) storage-gateway `CachePercentDirty` мис-скрапнутый em-dash (`dirty`+em-dash+`that`) -> RU «являющегося «грязным», то есть …» БЕЗ em-dash (§0); пустые EN-описания дубль-строк (CachePercentDirty/Volume*) -> пустые RU. (d) transit-gateway `BytesOut` EN-описание «number of **packets** sent» на Bytes-метрике (кварк) -> зеркал. (e) es `MasterReachableFromNode` malformed code-span `/\_cluster/health/`` (лишний двойной backtick + экранированное подчёркивание) -> байт-верно.

**QA:** `_qa_aws_l4if49.py` 5/5 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый python-скан по 5 RU: em-dash=0, mojibake=0/BOM=0, line-parity 5/5. Регрессия qa43/47/48 PASS 0. EN не тронут (md5 baseline `_en_baseline49.md5` идентичен до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (946 изменённых пар построчно, фокус direction/polarity + negation + numbers + terminology) — 0 находок. Направления сверены с именами метрик и НЕ инвертированы: blackhole-matched vs no-route-NOT-matched (Bytes+Packets), accepting(`0`)/blocking(`1`) write requests, primary/replica shards allocated vs aren't-allocated (red/yellow/green), read/write, In/Out, download/upload, received/sent. Негации целы (`aren't`/`doesn't`/`не`); числа/коды (`0`/`1`/36ч/256K/4xx/5xx/T2/IOPS/версии) целы; все 7 source-quirks зеркалены верно. Мой скепт-проход (rendered RU глазами): подтвердил пустые EN -> пустые RU, malformed code-span байт-верно, ebs Amazon/EBS различие, em-dash=0, double-space не внесён, 0 конкурирующих форм терминов.

**Next (277):** AWS aws-service остаток 15 в `aws-all-services` — streaming 4 (kinesis 171 / msk-kafka / mq / emr, ~329 строк) + 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура, канон azure builtin L4-IF.42) + 4 broken-header (dynamodb-new / rds-new 574 / glue / iot — COLMAP_OVERRIDE как Ground Truth) + trusted-advisor. Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.48 (2026-06-15, Opus 4.8): AWS aws-service — compute/integration standard батч (+7), словарь 953->1125

**Прогресс:** 2366 -> 2373/2655 = 89.34%, pending 289 -> 282, orphan 0, все source = Managed (verify_corpus подтвердил +7, 0 без source / 0 non-managed). Директория `aws-all-services` 58 -> 64/84. Закрыта группа compute/integration (общие глаголы состояний задач/выполнений): appsync, codebuild, connect, lambda-new, step-functions, simple-workflow-service-swf (SWF), cloudhsm-v2.

**Метод:** переиспользован e44-движок (`_build_aws_l4if48.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). Standard metric-таблица (`Name|Description|Unit|Statistics|Dimensions|Recommended`) уже в базовом движке — расширений TABLES не потребовалось (analyzer: ROW?=0/UNIT?=0/APPLIC?=0 во всех 7, чистый standard, 172 уникальные строки). Переводы в `_aws_merge48.py`, общий словарь `_aws_trans_l4if43.json` 953 -> 1125 (+172), `_aws_titles_l4if43.json` 57 -> 64 (+7). Все 7 intro = форма V1 (дословный shipped-шаблон). Merge self-validation: 172/172 matched (0 непокрытых, 0 неиспользованных). Flag-guard = 0. em-dash=0 с 1-й итерации.

**Каноны (durable):** workflow (SWF) -> «рабочий процесс» (канон azure L4-IF.41); activity task -> «задача действия», decision task -> «задача принятия решения», worker -> «исполнитель», task list -> «список задач», continued as new -> «продолженных как новые»; activity (Step Functions) -> «действие», execution -> «выполнение», service task -> «сервисная задача», schedule state -> «состояние планирования», time out on close/start -> «истекает тайм-аут при закрытии/запуске», heartbeat -> «контрольный сигнал»; concurrency (Lambda) -> «параллелизм», provisioned/reserved/standard -> «подготовленный/зарезервированный/стандартный», invocation -> «вызов», dead-letter queue (DLQ) -> «очередь недоставленных сообщений (DLQ)», consumer group -> «группа потребителей», offset -> «смещение», recursive loop -> «рекурсивный цикл», event source mapping -> «сопоставление источников событий»; contact flow (Connect) -> «поток обращений», contact -> «обращение», agent -> «оператор», inbound/outbound -> «входящих/исходящих», packet loss -> «потери пакетов», service quota -> «сервисная квота»; subscription/unsubscription (AppSync) -> «подписка/отписка», client-side/server-side error -> «на стороне клиента/сервера»; HSM session keys -> «сеансовые ключи», token keys -> «ключи токенов», end-to-end encrypted -> «со сквозным шифрованием», Junction temperature -> «температура перехода», traffic to/from the HSM -> «трафика к/от HSM» (направление!), packets on input/output -> «на входе/выходе»; «built-in services» (родовое) -> «встроенные сервисы», НО имя сервиса `AWS Lambda (built-in)` остаётся EN (ревью-фикс MINOR-1). Дата «Updated on Nov 15, 2023» -> «Обновлено 15 ноября 2023 г.». Новый durable migration-link канон (встречается в 13 EN -new файлах): «Migrate from AWS classic (formerly 'built-in') services to cloud services» -> «Переход с классических (ранее «встроенных») сервисов AWS на облачные сервисы», title-attribute переведён, путь URL byte-identical.

**Source-quirks / fidelity (зеркалены, не «исправлены»):** appsync `PublishDataMessageSize` дубль-строка с пустым EN-описанием (вариант Sum) -> пустая RU-ячейка (flag-guard structural); codebuild/lambda/step-functions/swf/cloudhsm множество дубль-строк метрик с пустым описанием (различаются Dimensions/Statistics) -> пустые RU зеркалятся построчно; connect `ToInstancePacketLossRate` (последняя строка файла без финального перевода строки) переведена корректно.

**QA:** `_qa_aws_l4if48.py` 7/7 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый python-скан по 7 RU: em-dash=0, mojibake=0/BOM=0, line-parity 7/7. Регрессия qa43/44/45/46/47 PASS 0. EN не тронут (md5 baseline идентичен до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 1 MINOR -> FIX -> SHIP):** Independent-review субагент (все 7 пар построчно EN/RU, фокус direction/polarity + negation + numbers + terminology): 1 MINOR — в lambda-new имя сервиса `AWS Lambda (built-in)` в прозе (строка 825) было переведено «(встроенный)», что расходилось с EN-формой того же имени в таблицах файла (строки 492/636/718) -> выправлено на EN (re-merge + rebuild + re-QA, 0/0). Направления сверены с именами метрик и НЕ инвертированы: CloudHSM traffic к/от HSM + вход/выход, AppSync connect/disconnect/subscribe/unsubscribe success/client/server, Connect inbound/outbound + негация «не разрешены», Lambda provisioned/reserved/standard concurrency, SWF scheduled-vs-started TimedOutOn Close/Start/Heartbeat. Числа/коды/DLQ/2^31/диапазон 0-1/20 сек целы; негации не потеряны. Мой скепт-проход подтвердил: пустые EN-ячейки -> пустые RU, faithful-зеркало дублей, 0 конкурирующих форм.

**Next (282):** AWS aws-service остаток 20 в `aws-all-services` — 10 standard/крупные (ebs-new / elasticsearch-service-es / elastic-mapreduce-emr / kinesis 171 / mq / msk-kafka / s3 / storage-gateway / transit-gateway / trusted-advisor) + 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура) + 4 broken-header (dynamodb-new / rds-new / glue / iot — COLMAP_OVERRIDE как Ground Truth). Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.47 (2026-06-14, Opus 4.8): AWS aws-service — DB-семья standard батч (+6), словарь 724->953

**Прогресс:** 2360 -> 2366/2655 = 89.11%, pending 295 -> 289, orphan 0, все source = Managed (verify_corpus подтвердил +6). Директория `aws-all-services` 52 -> 58/85. Закрыта семантическая семья «базы данных» (общая терминология, высокий dedup): aurora, documentdb, dynamodb (DAX), elasticache, keyspaces-cassandra, neptune.

**Метод:** переиспользован e44-движок (`_build_aws_l4if47.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). Standard metric-таблица (`Name|Description|Unit|Statistics|Dimensions|Recommended`) уже в базовом движке — расширений TABLES не потребовалось (analyzer: ROW?=0/UNIT?=0/APPLIC?=0 во всех 6, чистый standard). 229 уникальных строк (208 cells + 21 template-проза) переведены в `_aws_merge47.py`, общий словарь `_aws_trans_l4if43.json` 724 -> 953 (+229), `_aws_titles_l4if43.json` 51 -> 57 (+6). Intro V1 (5 файлов) + V2 (documentdb, «view graphs… custom graphs») = дословные shipped-шаблоны. **Durable приём asciinorm расширен** нормализацией markdown-escape (`\_`/`\*`): RU-ключи Redis/Memcached-статистик пишутся обычным подчёркиванием, матчатся к реальным skeleton-ключам с `\_` программно (хранимый ключ остаётся byte-identical с EN). Merge self-validation: 229/229 matched (0 опечаток), 0 unused. Flag-guard = 0. em-dash=0 с 1-й итерации.

**Каноны (durable):** DB instance -> «экземпляр БД», DB cluster -> «кластер БД» (компактная форма доминирует в семье; **принципиальное различие:** EN «database instance» -> «экземпляр базы данных» сохранён там, где источник пишет полное слово, напр. Aurora ActiveTransactions); read/write capacity units -> «единицы ёмкости чтения/записи» (canon `Current capacity units` shipped); provisioned -> «подготовленные»; lag -> «отставание», «величина отставания»; primary instance -> «первичный экземпляр», read replica -> «реплика чтения»; throughput -> «пропускная способность»; cluster volume -> «том кластера»; buffer cache -> «буферный кэш», resultset cache -> «кэш результирующих наборов»; evicted -> «вытесненные», reclaimed -> «освобождённые», LRU -> «кэш наименее недавно использовавшихся (LRU)»; `This is derived from X statistic` -> «Вычисляется на основе статистики X»; `node or cluster` -> «узлом или кластером» (instrumental «handled by») / «узла или кластера» (genitive «utilization of»); throttled -> «подвергнутые регулированию»; swap -> «пространство подкачки»; `reported at 5-minute intervals` -> «регистрируется с интервалом в 5 минут» (canon L4-IF.45); transaction ID wraparound -> «зацикливание идентификаторов транзакций», unvacuumed -> «неочищенный»; lightweight transaction (LWT) -> «облегчённая транзакция (LWT)»; «node or cluster» CPU `of` vs requests `by` разведены по падежу. Boilerplate: «Any version of ActiveGate…» -> «Любая версия ActiveGate в развёртываниях Dynatrace SaaS и Managed», disable built-in -> shipped canon, role-based access — **dynamodb-вариант без `Environment`/ссылки** («you need an ActiveGate installed») зеркален дословно (отличается от shipped «Environment ActiveGate»-canon).

**Source-quirks / fidelity (зеркалены, не «исправлены»):** (a) elasticache EN строка 943 сама мислейблед — Name `SortedSetBasedCmds`, но описание «string-based» (съехало с `StringBasedCmds`); строки 944/945 `StringBasedCmds` с пустым описанием в EN -> RU зеркалит каждую ячейку по позиции (no_unverified_claims). (b) neptune `BackupRetentionPeriodStorageUsed` EN «used to support **from** the … window» (лишнее from) -> RU по смыслу «для поддержки окна хранения». (c) documentdb/neptune `VolumeWriteIOPs` EN «billed write I/O operations **from** a cluster volume» (from для записи — кварк AWS-доки) зеркален «из тома кластера». (d) aurora DDL «such as **example**, create, alter…» (скрап съел «for» из «for example») -> RU «например запросов create, alter и drop» (дословно по официальной AWS-доке). (e) neptune EN unit-колонки `VolumeReadIOPs`/`WriteIOPs`/`BytesLeftTotal` = `Bytes` вместо Count (EN-кварк) -> unit-ячейка зеркалится байт-верно.

**QA:** `_qa_aws_l4if47.py` 6/6 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый grep/python по 6 RU: em-dash=0, mojibake_bytes=0/BOM=0, line-parity 6/6, 0 leftover EN-прозы. Регрессия qa43/44/45/46 PASS 0. EN не тронут (mtime baseline идентичен до/после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен git status'ом).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (все 6 пар построчно EN/RU, обход таблиц по строкам, сверка Description с EN-Name): 0 находок — направления (Receive/Transmit, In/Out, Hit/Miss=found/not-found, Committed/RolledBack/Opened, primary/replica, read/write, max/min, evicted/reclaimed) сверены с именами метрик и не инвертированы; числа/формула (`2`,`146`,`483`,`648` (2^31 - 1 000 000)), `-1`, версии, backtick-токены (`keyspace_hits`/`master_repl_offset`/`InvalidRequest`) целы; отрицания не потеряны; терминология консистентна; em-dash=0; EN-кварки зеркалены, не выдуманы. Мой скепт-проход: подтвердил пустые EN-ячейки -> пустые RU (flag-guard structurally), faithful-зеркало elasticache-943/neptune-units, принципиальное «database instance» vs «DB instance», 0 конкурирующих форм (инференс/приём-передач/наименее давно = 0), double-space не внесён.

**Next (289):** AWS aws-service остаток 27 — compute/integration 7 (appsync/codebuild/connect/lambda-new/step-functions/swf/cloudhsm-v2, ~173 строки), storage/net 5 (ebs-new/s3/storage-gateway/transit-gateway/es, ~130), streaming 4 (kinesis 171/msk-kafka/mq/emr, ~329); затем 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура) + 4 broken-header (dynamodb-new/rds-new/glue/iot — COLMAP_OVERRIDE) + trusted-advisor. Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.46 (2026-06-14, Opus 4.8): AWS aws-service — standard батч-3 (+6), словарь 537->724

**Прогресс:** 2354 -> 2360/2655 = 88.89%, pending 301 -> 295, orphan 0, все source = Managed (verify_corpus подтвердил +6). Директория `aws-all-services` 46 -> 52/85. Закрыты 6 standard-формат leaf с Count/Minute-стилем UNIT-пробелов (план L4-IF.45): simple-notification-service-sns, direct-connect, database-migration-service-dms, elemental-mediaconnect, sagemaker, gamelift.

**Метод:** переиспользован e44-движок (`_build_aws_l4if46.py` импортит `_build_aws_l4if44` + durable UNIT-расширение L4-IF.45). 187 уникальных строк (cells+проза+intros+dates+versions) переведены в `_aws_merge46.py`, общий словарь `_aws_trans_l4if43.json` 537 -> 724 (+187), `_aws_titles_l4if43.json` 45 -> 51 (+6). Все 6 intro = форма V1 (дословный shipped-шаблон). Merge сам репортит непокрытые skeleton-ключи И неиспользованные переводы (187/187 matched, 0 опечаток) + guard «no em-dash / no mojibake». analyzer `_aws_analyze46.py`: ROW?=0 во всех 6 (чистый standard). Flag-guard = 0 флагов перед записью. em-dash=0 с 1-й итерации.

**Две нестандартности (разобраны до записи):** (1) **direct-connect** `DecibelMilliWatts` (dBm, уровень оптического сигнала) — реальный юнит, не в карте -> добавлен в UNIT-расширение «Децибел-милливатт» (durable). (2) **sagemaker Ground Truth таблица** имеет ПЕРЕСТАВЛЕННЫЕ колонки vs остальные: `Name|Description|Dimensions|Statistics|Unit|Recommended` (Dimensions и Unit поменяны). Добавлен как отдельная header-сигнатура в `B.TABLES` (нативный COLMAP_OVERRIDE движка, канон container-registry/mesh/stream-analytics L4-IF.40/41): header переведён по literal-тексту ячейки, данные по ФАКТИЧЕСКОМУ смыслу (Dimensions `Region, LabelingJobName` EN, Unit `None`/`Seconds` -> перевод, Recommended -> applic). Рендер проверен вживую.

**Каноны (durable):** intro V1 = дословный shipped-шаблон; `X is the main dimension.` -> «Основное измерение: `X`.»; read-time «Чтение: N мин»; даты «Опубликовано/Обновлено DD month YYYY г.». Новые термины: topic (SNS) -> «топик» (канон L4-IF.41 67x); subscription filter policies -> «политики фильтрации подписок»; bitrate -> «битрейт», packet rate -> «частота пакетов»; fiber connection -> «оптоволоконное соединение», ingress/egress -> «входящий/исходящий» (квалификатор EN в скобке сохранён); virtual interface -> «виртуальный интерфейс»; full load (DMS) -> «полная загрузка», replication instance -> «экземпляр репликации», source/target -> «источник»/«целевая система», validation -> «проверка», bulk -> «массово», resident set size (RSS) -> «размер резидентной памяти (RSS)»; FEC/ARQ/PAT/PMT/PTS/PCR/PID/TS/CAT -> «прямая коррекция ошибок»/«автоматический запрос повторной передачи»/таблицы+аббревиатуры EN в скобках; lost during transit -> «потерянных при передаче»; inference (SageMaker) -> «вывод» (канон L4-IF.45), download/load/unload -> «скачивание/загрузка/выгрузка», multi-model endpoint -> «мультимодельная конечная точка», overheads -> «накладные расходы», labeling job (Ground Truth) -> «задание разметки», work team -> «рабочая группа», dataset objects -> «объекты набора данных», annotated -> «аннотированный»; fleet (GameLift) -> «флот», game session -> «игровая сессия», matchmaking -> «подбор игроков», matchmaking ticket -> «тикет подбора игроков», potential match -> «потенциальный матч», placement -> «размещение», since the last report -> «с момента последнего отчёта», spot instance/fleet -> «spot-экземпляр/spot-флот», healthy/unhealthy -> «исправный/неисправный» (канон WorkSpaces L4-IF.45), host players/session -> «принимать игроков»/«обслуживать сессию», idle -> «простаивающий». Юниты L4-IF.45-расширения (Count/Minute -> «Количество в минуту», Microseconds -> «Микросекунда» и т.д.) применены в sagemaker/gamelift/dms.

**Source-quirks / fidelity (зеркалены, не «исправлены»):** sagemaker EN-опечатки `400%'` (backtick+%+апостроф вместо закрывающего backtick, 4 описания) и «on an instance uses» (лишнее uses) и «`100%`and» (нет пробела) -> RU рендерит смысл, малформированный code-span `400%'` зеркалится байт-верно; api-gateway/DMS «gives us the latency» -> нейтральное «показывает задержку». «X is the number» в SageMaker invocations -> «X означает количество» (обход em-dash в дефиниции `X — это Y`, [[feedback_em_dash_translation_blindspot]]).

**QA:** `_qa_aws_l4if46.py` 6/6 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый grep по 6 RU: em-dash=0 (`\x{2014}`), mojibake/BOM=0, line-parity 6/6. EN не тронут (mtime baseline 1778567xxx до и после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 0 MINOR -> SHIP):** Independent-review субагент (все 6 пар построчно EN/RU, фокус на direction/polarity): 0 находок — направления (Rx/Tx, ingress/egress, source/target, incoming/outgoing, read/write, connected/disconnected, healthy/unhealthy, min/max) сверены с именами метрик и не инвертированы; коды (4xx/5xx), проценты, аббревиатуры, dimension-имена байт-целы; терминология консистентна; em-dash=0. Мой скепт-проход на риск-парах (почти идентичные source-vs-target / recovered-vs-not / latency-vs-price) подтвердил соответствие именам метрик: ValidationBulkQuery**Source**/**Target**Latency, FEC**Recovered**/**Not**RecoveredPackets, Lowest**Latency**/**Price**Placement — не перепутаны.

**Next (295):** AWS aws-service остаток 33 — крупные kinesis/aurora/elasticache/msk-kafka/neptune/documentdb/mq/dynamodb + 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура) + 4 broken-header (dynamodb-new/rds-new/glue/iot — COLMAP_OVERRIDE как Ground Truth) + trusted-advisor/s3-builtin/ebs-builtin/lb-builtin. Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.45 (2026-06-14, Opus 4.8): AWS aws-service — standard батч-2 (+16), словарь 303->537

**Прогресс:** 2338 -> 2354/2655 = 88.66%, pending 317 -> 301, orphan 0, все source = Managed (verify_corpus подтвердил +16). Директория `aws-all-services` 30 -> 46/85. Закрыты 16 standard-формат leaf с наименьшим числом непокрытых строк (по analyzer-нарезке, 0 UNIT-пробелов): eventbridge, simple-queue-service-sqs, elastic-inference, elastic-transcoder, workspaces, iot-things-graph, simple-email-service-ses, acm-pca, api-gateway, datasync, elemental-mediaconvert, elemental-mediatailor, vpc (NAT gateways), elemental-mediapackage, quantum-ledger-database-qldb, opsworks.

**Метод:** переиспользован e44-движок (`_build_aws_l4if45.py` импортит `_build_aws_l4if44`, только BATCH_PATH + durable UNIT-расширение Count/Minute·Microseconds·Bits/Second·Kilobytes/Second·Megabytes/Second для будущих sagemaker/gamelift). 234 уникальные строки (cells+проза+headings+intros+dates+versions) переведены в `_aws_merge45.py`, общий словарь `_aws_trans_l4if43.json` 303 -> 537 (+234), `_aws_titles_l4if43.json` 29 -> 45 (+16). Переводы заданы ASCII-нормализованным ключом, матчатся к реальным (demoji/curly) skeleton-ключам программно (no hand-typed curly quotes); merge сам репортит непокрытые skeleton-ключи И неиспользованные мои переводы (self-validation против опечаток) + guard «no em-dash / no mojibake». analyzer `_aws_analyze45.py` дал per-file uncovered-count для ship-нарезки. Flag-guard = 0 флагов перед записью. em-dash=0 с 1-й итерации.

**Каноны (durable):** intro V1/V2 = дословные shipped-шаблоны (меняется имя сервиса); `X is the main dimension.` -> «Основное измерение: `X`.»; read-time «Чтение: N мин»; даты «Опубликовано/Обновлено DD month YYYY г.»; ActiveGate/Dynatrace version-строки по shipped-канону. Новые термины: event bus -> «шина событий», default/custom event bus -> «шина событий по умолчанию»/«пользовательская шина событий»; messages in flight (SQS) -> «в обработке»; visibility window -> «окно видимости»; inference request (Elastic Inference) -> «запрос на вывод»; pipeline (Transcoder) -> «конвейер», output -> «на выходе»; flow execution (IoT Things Graph) -> «выполнение потока»; hard bounces (SES) -> «жёсткие отказы»; round-trip time (RTT) -> «время кругового пути (RTT)» (канон L4-IF.38); source/destination location (DataSync) -> «исходное/целевое расположение»; ad avails/ads (MediaTailor) -> «рекламные блоки»/«рекламные объявления», ad decision server -> «сервер решений по рекламе (ADS)», origin server -> «сервер-источник»; NAT gateway (VPC) -> «шлюз NAT», from/to destination -> «из/в пункт назначения»; ledger (QLDB) -> «реестр», `reported in N-minute intervals` -> «(регистрируется с интервалом в N)» (вынесено в скобку для сохранения именной группы ячейки, ревью-фикс MINOR-1); swap space (OpsWorks) -> «пространство подкачки», `nice` в backticks EN. Edition-заголовки `### AWS Elemental MediaPackage Live`/`Video on Demand (VOD)` = EN (продуктовые имена). UI-кнопки **Enable detailed CloudWatch metrics**/**Logs**/**Tracing**/**Further details**/**Streams**/**Command types** = EN.

**Source-quirks / fidelity:** elastic-transcoder дубль-строка `BillableSDOutput` (с точкой и без) зеркалится обе; api-gateway/SES EN-опечатки («The total number API requests», «The number times emails») -> RU нормальная грамматика; ACM PCA permissions-абзац — link title-attribute переведён + lowercase link-text по канону base-словаря (ревью-фикс: первый проход оставил title EN + capital, выправлено до байт-консистентности с shipped-вариантами).

**QA:** `_qa_aws_l4if45.py` 16/16 PASS, 0 FAIL/0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM не внесён, URL multiset, heading-parity, fence-interior, DESC-NOCYR, pure-Latin-heading, EN-prose-leftover). Независимый grep по 16 RU: em-dash=0, mojibake/BOM=0, line-parity 16/16. Регрессия qa_l4if43/44 PASS 0. EN не тронут (find -newermt=0 до и после ревью-субагента, [[feedback_workflow_agents_may_write]] проверен).

**Critical review (0 CRIT / 0 MAJOR / 3 MINOR -> FIX -> SHIP):** Independent-review субагент (все 234 пары + сверка VPC/QLDB/MediaTailor/OpsWorks по EN-источнику): направления received/sent и from/to destination не инвертированы, числа/HTTP-коды/диапазоны/юниты целы. 3 MINOR (все style): (1) QLDB «reported in intervals» как finite-verb -> вынесено в скобку (применено); (2) inference «вывод» vs «инференс» — оставлено «вывод» (словарный термин, контекст «ускоритель Elastic Inference» снимает неоднозначность); (3) «регистрируется» vs «зафиксированных» — разные EN-глаголы, расхождение оправдано. Мой скепт-проход поймал ACM-PCA title-attribute расхождение (см. source-quirks) — другой дефект, чем у субагента (взаимность L4-IF.33b).

**Next (301):** AWS aws-service остаток 39 — крупные kinesis 171/aurora/elasticache/msk-kafka + 6 standard с UNIT-пробелами (sns/direct-connect/dms/mediaconnect/sagemaker 32 Count·Minute…/gamelift 59); затем 6 builtin (`Metric key|Name|Unit|Aggregations|Monitoring consumption` — нужна TABLE-сигнатура) + 4 broken-header (dynamodb-new/rds-new/glue/iot — COLMAP_OVERRIDE) + trusted-advisor/s3-builtin. Дальше K8s 52 / OTel 30 / extensions / azure-other / oneagent.

## L4-IF.43 (2026-06-14, Opus 4.8): AWS aws-service — первый батч 12, новый builder + boilerplate-канон

**Прогресс:** 2309 -> 2321/2655 = 87.42%, pending 346 -> 334, orphan 0, все source = Managed. Первый батч директории `ingest-from/amazon-web-services/integrate-with-aws/aws-all-services` (всего 84 aws-service-*.md, 0 было переведено). Закрыты 12 с малыми metric-таблицами: billing, api-usage, transfer-family, systems-manager-run-command, wafv2, service-catalog, cloudsearch, cognito, iot-analytics, robomaker, workmail, cloudfront.

**Метод (`_build_aws_l4if43.py` + `_qa_aws_l4if43.py`):** content-keyed dict (проза) + column-aware (таблицы) + flag-guard (L4-IF.39/42), line-parity by construction. 4 типа таблиц по header-сигнатуре: metric (Name/Statistics/Dimensions EN, Description/Unit перевод, Recommended -> Применимо), permissions (Имя|Разрешения, данные EN), preset (Сервис AWS|Предустановленный дашборд, Applicable -> Применимо), endpoints (Конечная точка|Сервис, данные EN). Image caption == alt -> copy EN. JSON-блоки byte-identical. RU wb/LF/no-trailing-nl. Словари `_aws_trans_l4if43.json` (155 ключей) + `_aws_titles_l4if43.json` переиспользуемы для остатка 72.

**Мойибейк (повтор L4-IF.35):** Write схлопывает невидимый 0x80 в JSON-ключах. Фикс: demoji в builder через `chr(0x..)`-последовательности нормализует EN-ключ поиска (ASCII-only в исходнике), JSON-ключи держим чистыми; пересборка ключей по ASCII-скелету. RU без мойибейк, BOM в link-text убран.

**Каноны (durable, corpus-grep-verified):** «X monitoring» -> «Мониторинг X»; preset dashboard -> «предустановленный дашборд» (корпус 283x, НЕ «готовый»); custom device -> «пользовательское устройство» (372x); viewer (CloudFront) -> «зритель»; throttled -> «подвергнутые регулированию»; partition -> «партиция»; provisioning artifact -> «артефакт подготовки»; bounced email -> «отклонённое»; Statistics-значения (Multi/Sum/Average/Maximum) EN; Unit `None` EN; «All monitored Amazon services Required» EN (findability). View-metrics + Enable-monitoring boilerplate взяты byte-канонично из shipped azure-cloud-services-metrics RU. Даты переводятся («Опубликовано 11 августа 2020 г.»), read-time «Чтение: N мин», How-to guide «Практическое руководство».

**QA:** `_qa_aws_l4if43.py` 12/12 PASS, 0 FAIL, 0 WARN (line-parity, frontmatter byte-eq \r-norm, em-dash=0, мойибейк/BOM не внесён, URL/heading/fence-interior/table-col integrity, DESC-NOCYR blind-spot, EN-prose-leftover, pure-Latin-heading). Independent-review субагент (построчно 12 пар EN/RU): 0 CRIT/0 MAJOR/0 MINOR. Мой скепт-проход: zeugma/инверсии/кальки чисто. EN не тронут (find -newermt = 0). SaaS->Managed замена подтверждена (старые HEAD-RU = `www.dynatrace.com/docs` SaaS scraped 03-03 -> мои `/managed/` 05-12).

**Next (334):** AWS aws-service остаток 72 (engine+словари готовы) / setup-on-k8s guides 52 / extensions 36 / azure-integrations 31 / OTel collector 30.

## L4-IF.41 (2026-06-11, Fable 5): Azure cloud-services-metrics — standard 28 (app/integration/messaging/IoT/misc)

**Прогресс:** 2265 -> 2293/2655 = 86.37%, pending 390 -> 362, orphan 0. azure-cloud-services-metrics: было 63/106, стало 91/106 (остаток: irregular 15 = builtin-* 10 + hdinsight/netapp/relay/application-insights/storage-account extraH2, + 1 hub). Закрыты все standard-layout leafs: api-management, app-configuration, application-gateway, automation-account, batch, blockchain, cache-for-redis (269 строк), cognitive-ink-recognizer, event-grid, event-hubs, front-door x2, ISE, iot-central, iot-hub, device-provisioning, key-vault, logic-apps, maps, media, mesh, notification-hub, power-bi, recovery-services-vault, search, signalr, stream-analytics, time-series-insights. ~415 новых уникальных Description + ~14 строк новой прозы.

**Файлы (28, build-script `_build_azure_metrics_l4if41.py` + `_qa_l4if41.py`):** размеры 55-268 строк; крупные: cache-for-redis (268, 12 повторов каждого описания main/instance-based/shard), iot-hub (128, d2c/c2d + routing + twins/direct-methods/jobs), notification-hub (122, PNS-блок APNS/GCM/MPNS/WNS).

**Метод (расширение column-aware engine, import L4-IF.40 -> 38 -> 37):** base-словари выигрывают для shared-строк. Новое:
- **COLMAP_OVERRIDE** для 2 broken-header файлов: mesh-application (header `Unit|Dimensions`, в данных колонки переставлены: dims в Unit-колонке, юниты в Dimensions) и stream-analytics (header `Dimensions|Description`, в данных desc в Dimensions-колонке, dims в Description). Заголовки переводятся по literal-тексту ячейки (канон container-registry L4-IF.40), данные — по ФАКТИЧЕСКОМУ смыслу через override-colmap. QA использует тот же override, иначе Name/Dimensions byte-EN check ловил бы ложные FAIL.
- **2 новых Recommended-лейбла** (time-series-insights, две колонки): `Recommended (Environment)` -> «Рекомендуется (Environment)», `Recommended (Event Source)` -> «Рекомендуется (Event Source)» (Environment/Event Source = сущности продукта, EN как в title).

**Каноны (durable, corpus-grep-verified):**
- throttled -> «подвергнутые регулированию» (Cosmos DB shipped 2x; применено ко всем WNS/GCM/MPNS/search/app-config/EventHub строкам); topic -> «топик» (корпус 67x, Event Grid + Service Bus endpoints); deprecated -> «(устарело)» в title (GCP shipped канон); has been retired -> «выведен из эксплуатации» (mesh).
- workflow -> «рабочий процесс» (Logic Apps/ISE семейство, 56 метрик); billed executions -> «оплачиваемые выполнения»; charged -> «за которые будет начислена плата» (НЕ «будут оплачены»; ревью-фикс).
- IoT: device twin -> «двойник»; direct method -> «прямой метод»; enrollment (DPS) -> «регистрация»; attestation -> «аттестация»; device-to-cloud/cloud-to-device -> «устройство-облако»/«облако-устройство» (кавычки-ёлочки, дефис); abandoned (c2d) -> «от которых устройство отказалось»; orphaned (routing) -> «остались без назначения»; fallback route -> «резервный маршрут»; IoT hub (нарицательное в DESC) -> «IoT-хаб».
- Messaging/notification: dead-lettered -> «недоставленные»; push -> «push-уведомления»; pushes that failed -> «push-уведомлений, не доставленных из-за»; PNS ж.р. («PNS не приняла», по подразумеваемой «службе»); payload -> «полезная нагрузка»; notification hub (нарицательное) -> «хаб уведомлений»; Captured (Event Hubs Capture) -> «захваченные»/«бэклог захвата»; installation operations -> «операции ... установок».
- Прочее: memory thrashing -> «пробуксовка памяти»; watermark delay (Stream Analytics) -> «задержка водяного знака»; warm store (TSI) -> «тёплое хранилище»; flattened events -> «события, преобразованные в плоскую структуру» (ревью-фикс от «развёрнутых»); partition (TSI event source) -> «партиция» (новый прецедент, в корпусе 0, выбран по узусу с «топик»); Vault (Key Vault DESC) -> «хранилище»; assets (Media) -> «ресурсы»; capacity units -> «единицы ёмкости»; QPU -> «единицы обработки запросов (QPU)»; Start Task (Batch) -> «стартовая задача»; origin (CDN) -> «источник»; AFDX edge -> «пограничный узел AFDX».
- Image captions EN byte-identical (28 шт., вкл. «Azure Integration Service Environment + Logic Apps»); H3 product-имена EN byte-identical (event-grid x3, front-door-cdn x2); recovery-services-vault title/H1 = чистое имя продукта без «monitoring» -> остаётся EN (включая frontmatter title).

**Source-quirks (fidelity, флаг):** (a) front-door `BackendRequestLatency` EN «sent by the HTTP/S proxyMySQL to the backend» — мусорная склейка «MySQL» в скрапе; RU рендерит смысл («HTTP/S-прокси»), мусор не зеркалится. (b) api-management EN опечатка «(depracated)» -> RU «(устаревший)» (согласовано с «сервис» в предложении; титульный канон «(устарело)» здесь не применим, отклонено из ревью с обоснованием). (c) media-service EN «content key polices» (typo) -> RU нормальное «политик». (d) cache-for-redis EN «The number errors» -> RU нормальная грамматика. (e) **blockchain `CpuUsagePercentageInDouble` EN-описание «The block number of the latest block committed» — подменённое описание в источнике** (противоречит Name+Unit=Percent); СОХРАНЕНО зеркально «Номер последнего зафиксированного блока» по правилу no_unverified_claims (правильный текст пришлось бы выдумывать, в строке нет внутреннего опровержения-факта; сервис retired, официальной доки нет). (f) **notification-hub `outgoing.wns.channeldisconnected` EN «is throttled» — копипаст-слип** (Name `channeldisconnected` + заголовок `X-WNS-DeviceConnectionStatus: Disconnected` в той же строке опровергают «throttled») -> RU «отключён» (класс DataWritten L4-IF.40: внутристрочный факт побеждает слип). (g) signalr EN-грамматика «The amount of user connection» -> RU нормальное «Количество пользовательских подключений».

**QA:** `_qa_l4if41.py` 28/28 PASS, 0 проблем (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL-identity multiset, fence, heading-parity + EN-headings byte-eq, DOUBLE-SPACE introduced-only, table-row integrity Name/Dimensions byte-EN по ФАКТИЧЕСКОМУ colmap (COLMAP_OVERRIDE), DESC-NOCYR + DESC-UNTRANSLATED blind-spot, APPLICABLE-LEFT, leftover-EN prose). Регрессия: qa_l4if37/38/40 PASS 0, qa_l4if39 FAIL=0/WARN=50 (известные легит). Build: 28/28 line-parity, 0 warnings (1 пропуск словаря пойман warning'ом на 1-м прогоне: front-door вариант «Number of client requests processed by the WAF» без «The»). verify_corpus 2293/362/0, source OK.

**Critical review (0 CRITICAL / 2 MAJOR / 5 MINOR, FIX-FIRST -> исправлено -> SHIP):**
- Independent-review субагент (все 28 пар построчно): MAJOR-1 WNS channeldisconnected (принято, фикс (f) выше); MAJOR-2 blockchain CPU-метрика (принято решение «зеркалить + флаг», см. (e)); MINOR принятые: гео-репликация «синхронизировать НА гео-вторичный кэш» (направление to), «за которые будет начислена плата» x2, flattened -> «преобразованных в плоскую структуру».
- ОТКЛОНЕНО с обоснованием: «(устаревший)» -> «(устарело)» (внутри предложения согласуется с «сервис», не титул); RTT «время кругового пути» -> «время приёма-передачи» (ломает канон L4-IF.38, shipped network-watcher/expressroute 5+ файлов; кандидат на directory-wide cleanup отдельно).
- Мой скепт-проход: EN-tree не тронут субагентом (mtime 06-05 baseline); WNS L105 поправлена, соседние L106/107 не задеты; направления сверены с Name-id (Incoming/Outgoing event-hubs, Inbound/Outbound signalr, d2c/c2d iot-hub, sent/received app-gw); broken-header rendering проверен вживую (mesh: dims EN + units RU в переставленных колонках; stream-analytics: desc RU в col «Измерения», dims EN в col «Описание» — зеркало EN-слома). Взаимность L4-IF.33b подтверждена в 4-й раз: субагент поймал внутристрочное противоречие (channeldisconnected), которое мои механические сканы не видят by design.

**Next (362):** azure-cloud-services-metrics irregular 15 (builtin-* 10 no-boilerplate: api-management-services, app-gateways, cosmos-db, event-hub, iot-hub, load-balancers, redis-cache, service-bus, sql-servers, storage-account; + hdinsight 147, netapp-files 90, relay 77, application-insights 94, storage-account 166 extraH2) + hub azure-cloud-services-metrics.md. Дальше AWS 101 / K8s 52.

## L4-IF.40 (2026-06-10, Fable 5): Azure cloud-services-metrics — DB/Containers/Storage +14, corpus-wide «г.» нормализация

**Прогресс:** 2251 -> 2265/2655 = 85.31%, pending 404 -> 390, orphan 0. azure-cloud-services-metrics: было 49/106, стало 63/106 (остаток standard 28 + irregular 15 + 1 hub). Закрыты целиком семейства: БД (mariadb, mysql, mysql-flexible-servers, postgresql, sql-database-hyperscale, sql-managed-instance), контейнеры (container-app, container-apps-environment, container-instances, container-registry), storage/data (data-lake-storage-gen1, data-share, storage-account-classic, storage-sync). 180 новых уникальных Description + ~30 строк новой прозы (dashboard/management-zone секции DB-семейства).

**Файлы (14, build-script `_build_azure_metrics_l4if40.py` + `_qa_l4if40.py`):** db-mariadb (99), db-mysql (102), db-mysql-flexible-servers (114), db-postgresql (146, 3 таблицы Single/Hyperscale/Flexible с H3-заголовками), sql-database-hyperscale (84), sql-managed-instance (70), container-app (66), container-apps-environment (59), container-instances (65), container-registry (67), data-lake-storage-gen1 (66), data-share (67, таблица без Description-колонки), storage-account-classic (142, 5 под-таблиц Blob/File/Queue/Table), storage-sync (70).

**Метод (расширение column-aware engine):** import L4-IF.38 (цепочка к L4-IF.37), base-словари выигрывают для shared-строк. Новое:
- **EXACT_LINE-слой** — полнострочные переводы ДО substring-replace цепочки (intro каждого файла, deprecation notices, management-zone блок, 3 варианта storage-classic абзацев). Причина: hyperscale prereq-строка содержит substring-ключ L4-IF.37 («To monitor the SQL Databases user kind…»), но отличается первым предложением («hyperscale type» vs «data warehouse type») — чистый replace оставил бы пол-строки EN. Урок: replace-композиция требует пост-скана.
- **Пост-build leftover-EN скан** с явным PASS_EN whitelist (image captions, bold product labels, rule-condition bullets, postgresql H3). Поймал на 1-м прогоне 3 H3-заголовка.
- **Broken-header обработка:** container-registry EN-таблица имеет безымянную 4-ю колонку (`| Name | Description | Unit |  | Recommended |`), значения Recommended съехали в неё -> `cell == "Applicable"` переводится в любой колонке.

**Каноны (durable, corpus-grep-verified):**
- management zone в прозе -> «зона управления» (корпус 334+116+110 vs 186 EN-UI); link-title set-up-management-zones -> «Создание зон управления и назначение прав доступа к ним.» (3x доминанта); Dashboard timeframe link-text -> «Временной диапазон и зона управления дашборда».
- Optionally -> «При желании» (без запятых-калек); section -> «раздел» (32x vs «секция» 24x API-specific); entities -> «сущности»; gain full visibility -> «получить полную видимость» (13x vs 11x); will be retired -> «будет выведен из эксплуатации» (+ классификатор «сервис»); Deprecation notice -> «Уведомление об устаревании» (1x прецедент).
- Rule-condition bullets management zone («* Service type: `Database`», «* Service type equals `Database`», Technology, Service topology) — EN целиком (UI-поля + UI-значения, корпус `**Service type**:` EN).
- Image captions/alt EN byte-identical (shipped канон dtu «Clone hide azure»); H3 product-имена под-таблиц EN byte-identical (anchor fidelity, L4-IF.33).
- Метрики-эхо: «X percent» (ресурсы) -> «Процент использования X»; «IO percent» -> «Процент ввода-вывода»; «X used/limit» -> «Использованное X»/«Лимит X»; Com_* MySQL counter-эхо («Com alter table»…) — EN намеренно (префикс счётчика + SQL-операторы, переводить нечего); Innodb/binlog/ibdata1/tempdb токены EN внутри RU-фраз.
- storage account -> «аккаунт хранилища» (1x прецедент + проектный «аккаунт»); file share -> «файловый ресурс»; снапшоты -> «моментальные снимки»; recall (File Sync cloud tiering) -> «отзыв данных»; heartbeat EN; revision -> «ревизия» (корпус 14x vs «редакция» 0); image pull/push -> «извлечение/отправка образов»; burst -> «всплески»; большие числа -> «1 000 000 000» (RU-пробелы, корпус 7x).
- Blob: токен-эхо «The number of Blob» -> «Количество Blob» (EN-токен), generic lowercase «base blob storage» -> «хранилище базовых BLOB-объектов».

**Source-quirks (fidelity, флаг):** (a) data-lake-gen1 `DataWritten` EN-описание «data written **from** the account» — слип направления в источнике; RU «записанных **в** аккаунт» (зеркалить = инверсия класса CRITICAL; короткие эхо-описания = смысловые лейблы, в отличие от прозаических claims, которые переводим дословно — egress-абзац storage-classic с EN-противоречием «egress from client into Azure» переведён как есть). (b) postgresql read/write_throughput Unit=Count в EN (должно быть байт/с) — byte-identical «Количество». (c) container-registry broken header — см. выше, сами заголовки сохранены byte-identical.

**QA:** `_qa_l4if40.py` 14/14 PASS, 0 проблем (line-parity, frontmatter byte-eq \r-norm, em-dash=0, mojibake/BOM, URL-identity, fence, heading-parity + EN-headings byte-eq, DOUBLE-SPACE introduced-only, table-row integrity Name/Dimensions byte-EN, **DESC-NOCYR blind-spot** скан Description-ячеек, APPLICABLE-LEFT, leftover-EN prose). Регрессия: qa_l4if37/38 PASS 0, qa_l4if39 FAIL=0/WARN=50 (известные легит). verify_corpus 2265/390/0, source OK.

**Critical review (0 CRITICAL / 1 MAJOR / 9 MINOR, FIX-FIRST -> исправлено -> SHIP):**
- Independent-review субагент: MAJOR-1 container-registry «Applicable» x5 в безымянной колонке (мой DESC-NOCYR скан не видел: не Description-колонка) -> исправлено через builder; MINOR: «управляемого окружения» -> «управляемой среды» (консистентность с boilerplate директории «в вашей среде Dynatrace» + MS-термин Container Apps), «Размер базового хранилища Blob» -> «Размер хранилища базовых BLOB-объектов» (base относится к blob), двусмысленное «который может использоваться» -> «которое может использовать сервис», «Размер пропускной способности» -> «Пропускная способность» (EN сам кривой «size of throughput»), «для всплеска» -> «для всплесков», дата без «г.».
- ОТКЛОНЕНО с обоснованием: «Workers percentage» -> «рабочих потоков» (ломает консистентность с 5 shipped-файлами «Процент рабочих процессов» = base-канон; кандидат на отдельный directory-wide cleanup); «ревизия» -> «редакция» (корпус 14x vs 0).
- Мой скепт-проход: направления сверены с Name-id метрик (ingress/egress, io_read/written, rx/tx, DataRead/Written, read/write_iops) — все верные; запятые-кальки OneAgent-строки убраны; EN не тронут субагентом (mtime 06-05 = mojibake-cleanup baseline, git EN-tree без новых изменений). Взаимность L4-IF.33b подтверждена в 3-й раз: субагент поймал broken-header класс, который оба моих скана пропустили.
- **Corpus-wide следствие ревью:** дата-канон «DD месяц YYYY г.» (L4-IF.34/35) нарушался в 272 legacy-строках (54 «Обновлено» + 219 «Опубликовано» минус 1 моя) по всему managed-ru -> нормализовано скриптом (regex `^\* (Опубликовано|Обновлено) D месяц YYYY$` + « г.», line-count assert, 272 файла), остаток 0, QA 37-40 после — зелёные.

**Next (390):** azure-cloud-services-metrics standard 28 (engine готов: api-management, app-configuration, application-gateway, automation-account, batch, blockchain, cache-for-redis 269-строк, cognitive-services, event-grid/hubs, front-door x2, integration-service-environment, iot x3, key-vault, logic-apps, maps, media, mesh, notification-hub, power-bi, recovery-services, search, signalr, stream-analytics, time-series-insights) + irregular 15 (builtin-* no-boilerplate, hdinsight/netapp/relay/application-insights/storage-account extraH2) + hub. Дальше AWS 101 / K8s 52.

## L4-IF.39 (2026-06-08, Opus 4.8): 7 разрозненных stragglers, 5 топ-секций -> 100%

**Прогресс:** 2244 -> 2251/2655 = 84.78%, pending 411 -> 404, orphan 0. Закрыты ВСЕ non-ingest-from pending -> в pending остался ТОЛЬКО `ingest-from` (404). Топ-секции на 100%: observe (319/319), analyze-explore-automate (86/86), license (42/42), secure (29/29), root `index.md`.

**Файлы (7, build-script `_build_l4if39.py` + `_qa_l4if39.py`):**
- `index.md` (80) — корневой навигационный хаб (карточки-ссылки + секции Deploy/Platform/Solutions/Observe/Extend/Manage/API).
- `observe/.../monitor-cluster-utilization-kubernetes.md` (63) — использование кластера K8s/OpenShift.
- `observe/.../service-types/merged-services.md` (74) — объединённые сервисы (deprecated UI).
- `observe/infrastructure-observability/vmware-vsphere-monitoring.md` (96) — мониторинг VMware через ActiveGate.
- `analyze-explore-automate/metrics-classic/self-monitoring-metrics.md` (131) — dsfm-метрики + Data Explorer queries (code-fences).
- `license/dps-for-hybrid.md` (145) — DPS for Hybrid (таблица сценариев + FAQ).
- `secure/.../vulnerability-analytics/vulnerability-evaluation.md` (136) — механизм оценки уязвимостей AppSec.

**Метод (новый класс билдера для гетерогенной прозы) — line-keyed dict + auto-copy + flag-guard:** итерируем EN-строки, `dict[lineno] -> RU` для прозы; auto-copy для blank/`---`/source/scraped/image/fence-interior/pure-code-token-li; всё прочее -> FLAG (ничего молча не остаётся EN). Для `index.md` card-grid: копируем EN-строку + ordered REPL только display-text (URL/image-alt/title byte-identical). RU пишется `open(wb)`/LF/без trailing-nl -> PostToolUse-форматтер не трогает .md, line-parity by construction. Flag поймал 2 пропуска (`Data Explorer query example` L94/L101) на 1-м прогоне.

**Каноны (durable, corpus-grep-verified):**
- UI-пути/кнопки EN bold: `**Settings** >` 419x vs 0 RU; `**Save changes**` 203x / `**Edit**` 243x EN; статусы `Resolved` 26x / `Critical` 6x EN; `management zone` EN 9x.
- tag-теги: Explanation -> «Пояснение» (27x), Prerequisites -> «Предварительные требования» (31x), Related topics -> «Связанные темы» (881x), How-to guide -> «Практическое руководство» (175x), `N-min read` -> «Чтение: N мин», Published/Updated -> «Опубликовано/Обновлено DD месяц YYYY г.».
- Security: third-party vuln -> «сторонняя уязвимость», code-level -> «на уровне кода» (НЕ «уровня кода» 0x), vulnerability feed -> «фид уязвимостей» (НЕ «канал» 0x), exposure -> «доступность» / «внешняя доступность» (corpus 17x, НЕ «подверженность»), runtime components -> «компоненты среды выполнения».
- License: account -> «аккаунт» (28x), rate card -> «тарифная карта», annual commitment -> «годовое обязательство», DPS / DPS for Hybrid / ODC EN.
- index card-text = краткий RU (Infrastructure Observability -> «Наблюдаемость инфраструктуры», Distributed traces -> «Распределённые трассировки»), product-имена EN (Davis AI/Smartscape/Data Explorer/Digital Experience/Application Security/OpenTelemetry).
- in-page TOC якоря (`#tpv`/`#clv`/`#create-merged-service` и т.п.) оставлены byte-identical: они сломаны и в EN (скрапер сбросил upstream `{#...}` attr_list), переведённые соседи в `secure/` тоже НЕ добавляли `{#...}` -> консистентность подкаталога + fidelity (флаг: in-page TOC не работает ни в EN, ни в RU нашего корпуса).

**HEAD держит СТАРЫЕ SaaS-версии этих RU** (`source: …/docs/…`, scraped 2026-03-06, тег `* Latest Dynatrace`, термины «каналы уязвимостей»/«степень подверженности»/«Сторонние компоненты»). Проект мигрировал SaaS -> Managed (коммит `b2311e2` «remove SaaS»). Новые RU = Managed (`/managed/`, scraped 05-12, frontmatter byte-eq с Managed EN). Поэтому git показывает ` M` (не `??`): это ожидаемая ЗАМЕНА SaaS-RU на Managed-RU, НЕ потеря. Терминология синхронизирована с on-disk Managed-корпусом (2244 файла), НЕ с устаревшим HEAD-SaaS. verify_corpus меряет working-tree -> эти 7 числились pending.

**QA:** `_qa_l4if39.py` 7/7 PASS, 0 FAIL (line-parity, frontmatter byte-eq с \r-норм, em-dash=0, mojibake/BOM=0, URL-identity multiset, heading-level parity, fence byte-identity, EN-leftover blind-spot скан Cyr-run/no-Cyr). 50 WARN = легитимные EN product-имена (DPS for Hybrid / Dynatrace Platform Subscription / GET a schema / POST an object / Google Cloud Marketplace), **0 EN-NOCYR** (нет сплошных EN-строк прозы). Независимый греп: em-dash=0, mojibake/BOM=0, double-space=0 во всех 7.

**Critical review (8 фиксов):**
- Мой скепт-проход +5: `likely` -> «скорее всего» (не «как правило» = habitual); «выделяемых ресурсов памяти» (parallelism с CPU-строками); «Правило можно изменить:» (вместо клинящего «выполнив следующее:»); vmware/dps `X is Y` -> двоеточие (не «X, это Y»).
- Independent-review субагент +3 (поймал то, что мой проход НЕ увидел, валидирует канон L4-IF.32): **L28 «Библиотеки передаются OneAgent» инвертировал направление** (читается дательно «OneAgent'у», тогда как EN = OneAgent *сообщает о* библиотеках; на L29 я же написал верно) -> «**Библиотеки**: OneAgent сообщает о них»; bare `exposure` -> «внешняя доступность» (disambig от uptime-availability); merged L20 причастие «выполняющих» -> «которые выполняют» (неоднозначно: сервисов/процессов).
- EN не тронут субагентом (mtime 05-12 baseline, git status чист по EN-tree). Взаимность durable: РЯ-грамматический проход и independent-review ловят РАЗНЫЕ классы дефектов -> нужны оба (L4-IF.33b подтверждён).

**Next:** только `ingest-from` 404. azure-cloud-services-metrics остаток 57 leaf + irregular 11 (column-aware engine готов) / AWS 101 / K8s 52.

## L4-IF.38 (2026-06-05, Opus 4.8): Azure cloud-services-metrics — networking +12

**Прогресс:** 2232 -> 2244/2655 = 84.52%, pending 423 -> 411, orphan 0. azure-cloud-services-metrics: было 37/106, стало 49/106 (остаток 57 leaf + 1 hub; из «остатка 69» закрыто всё networking-семейство).

**Файлы (12, build-script `_build_azure_metrics_l4if38.py` + `_qa_l4if38.py`):**
- DNS: traffic-manager (62), dns-zone (63), private-dns-zone (67).
- Сеть/интерфейсы: network-interface (64), network-watcher (77, 2 таблицы Connection Monitor / Preview), firewall (65), expressroute-circuit (66), virtual-network-gateways (72, спец-intro VPN/ExpressRoute).
- Load balancers: gateway-load-balancer (65), standard-load-balancer (69, note про built-in).
- DDoS/WAF: public-ip-addresses (86, 26 DDoS-метрик), web-application-firewall-policies (61).

**Метод:** переиспользован column-aware engine L4-IF.37 (`import` boilerplate PROSE/DATE/HEADER/UNIT/REC byte-identical). Добавлено: 12 TITLE_MAP, 2 даты (Jun 25 / Sep 18 2020), read-time «2 мин», load-balancer «monitors a part of» note, VNG-проза (2 предложения), 3 составных юнита public-ip + 77 DESC.

**Каноны (durable, новые/подтверждённые):**
- **Networking-термины:** probe -> «проба» (Azure RU canon, НЕ «зонд»); round-trip time / RTT -> «время кругового пути (RTT/мс)»; DDoS mitigation -> «подавление DDoS»; dropped -> «отброшенные», forwarded -> «пересланные», inbound -> «входящие»; ingress/egress -> «входящие/исходящие»; traffic selector mismatch -> «несоответствие селектора трафика»; SNAT ports -> «SNAT-портов»; backend -> «бэкенд»; peers (BGP) -> «пиры»; Record Sets -> «наборы записей»; point-to-site/site-to-site -> «точка-сеть»/«сеть-сеть» (ДЕФИС, не em-dash, §0); application/network rules -> «правила приложений»/«сетевые правила».
- **EN as-is:** Load Balancer, MSEE, ExpressRoute, VPN, Web Application Firewall, Traffic Manager, Connection Monitor (product/feature names); dimension-имена Port/Direction даже внутри склеенного скрапером Unit-cell.
- **Составной Unit-cell (public-ip скрап-склейка `Unit, Dimensions`):** переводим только токен единицы, имена измерений EN: `Byte, Port, Direction` -> `Байт, Port, Direction`; `Count, Port, Direction` -> `Количество, Port, Direction`; `Percent, Port` -> `Процент, Port`.
- **Average-агрегат:** род прилагательного по существительному (доступность=Средняя, статус=Средний, время=Среднее, пропускная способность=Средняя).
- **Source-quirk сохранён byte-identical (НЕ «чинил»):** firewall `ApplicationRuleHit` dimensions «Status, Reason, Protocol, Protocol» (Protocol дублирован в EN); EN clone-boilerplate L45 trailing hard-break «  » + «(**…**)» (реальный U+2026, не мойибейк) скопированы как есть.

**QA:** `_qa_l4if38.py` 0 проблем (line-parity 12/12, frontmatter byte-eq, em-dash=0, mojibake preserved, BOM=0, URL-identity, fence-parity, heading-parity, table-row integrity Name/Dimensions byte-EN, leftover-EN). Build: 12/12 line-parity, 0 warnings (все DESC/UNIT замаплены). Independent-review субагент: 0 CRIT/0 MAJOR/0 MINOR (SHIP); явно проверены dropped/forwarded и ingress/egress по всем 24 DDoS-строкам. Мой скепт-проход (НЕ доверять «all clean», L4-IF.33b): blind-spot-скан Description-ячеек без кириллицы = 0 пропусков (этот класс leftover-EN-скан QA не видит, т.к. скипает table-строки); 0 реальных двойных пробелов; EN не тронут субагентом (mtime baseline + git count=2). EN не закоммичен (дефолт проекта).

**Next (остаток azure-metrics 57 leaf + hub):** контейнеры (container-app/apps-environment/instances/registry), IoT (iot-hub/iot-hub-builtin/iot-central/device-provisioning), БД (db-mysql/mariadb/postgresql/mysql-flexible/sql-managed-instance/sql-database-hyperscale), storage (storage-account/-classic/-builtin/storage-sync/data-lake-storage-gen1), messaging (event-hubs/event-grid/service-bus/relay/notification-hub/signalr), прочее (cache-for-redis/application-insights/logic-apps/batch/hdinsight/...). Irregular 11 (builtin-* + storage-account) = отдельная обработка (нет std `| Name` header). Дальше AWS 101 / K8s 52.

## L4-IF.37 (2026-06-05, Opus 4.8): Azure cloud-services-metrics — БД/data/analytics +12

**Прогресс:** 2220 -> 2232/2655 = 84.07%, pending 435 -> 423, orphan 0. azure-cloud-services-metrics: было 25/106 (серия `monitor-azure-ai-*`), стало 37/106 (остаток 69: Group A 24, Group B 20, Group C 6, синглтоны 4, irregular 15).

**Файлы (12, build-script `_build_azure_metrics_l4if37.py` + `_qa_l4if37.py`):**
- SQL-семейство: sql-database-dtu (86), sql-database-vcore (91), sql-elastic-pool-dtu (81), sql-elastic-pool-vcore (80), sql-data-warehouse (96, legacy), synapse-analytics (99, 3 таблицы Workspace/Spark/SQL pool).
- Cosmos: cosmos-db-account-mongodb (99), cosmos-db-account-globaldocumentdb (141).
- data: data-factory (100, V1+V2 две таблицы), data-lake-analytics (68), data-explorer-cluster (88, Group C), machine-learning (99, спец-intro).

**Метод (новое — column-aware engine):** в отличие от `_build_azure_ai.py` (позиционный), новый билдер читает header КАЖДОЙ таблицы и маппит колонку по имени -> индекс. Это нужно потому что в одном файле бывают таблицы с РАЗНЫМ порядком колонок: synapse SQL-pool и event-grid имеют `Unit|Dimensions`, а основные `Dimensions|Unit`. Name + Dimensions всегда EN (Azure Metrics API identifiers, отображаются в UI на англ.), переводятся только Description/Unit/Recommended + лейблы header. Boilerplate (View service metrics, шаги 1-4, clone/hide) byte-identical с shipped `monitor-azure-ai-*` (L85).

**Каноны (durable):**
- header: `Name->Имя`, `Description->Описание`, `Dimensions->Измерения`, `Unit->Единица измерения`, `Recommended->Рекомендуется`.
- UNIT: Count->Количество, Percent->Процент, Byte->Байт, Bytes->Байты, MilliSecond->Миллисекунда, Second->Секунда, GigaByte->Гигабайт, MegaByte->Мегабайт, BytePerSecond/BytesPerSecond->Байт в секунду, PerSecond->В секунду. REC: Applicable->Применимо.
- title `X monitoring`->`Мониторинг X`; `(legacy)`->`(устаревшее)`; имена продуктов/тиров EN (Hyperscale, DTU, vCore, DWU, tempdb, In-Memory OLTP, Apache Spark, RU).
- intro: стандарт `Dynatrace ingests metrics from Azure Metrics API for X`->`Dynatrace получает метрики из Azure Metrics API для X`; ML-вариант `...for multiple preselected namespaces, including X`->`...для нескольких предварительно выбранных пространств имён, включая X`.
- migration-note: shipped azure-canon `Информацию о различиях между классическими службами... [Миграция с классических служб Azure (ранее «встроенных»)...]` (службы, не сервис — это устоявшаяся cross-page строка; в boilerplate остаётся «сервис»).
- терминология: workload group->группа рабочей нагрузки, ingestion->приём данных, run(ML)->запуск, workspace->рабочая область, dedicated gateway->выделенный шлюз, throttled->подвергнутых регулированию, deadlocks->взаимоблокировки, elastic pool->эластичный пул, data warehouse->хранилище данных, eviction->вытеснение, materialized view->материализованное представление, service-level objective->целевой уровень обслуживания.
- мойибейк `â¦` в `(**â¦**)` сохранён byte-identical (как 25 shipped azure-ai siblings; НЕ путать с GCP L4-IF.36 где `â¦`->«…» — разные подкаталоги, выбран consistency внутри директории). Directory-wide cleanup `â¦`->«…» по всем 37 azure-metric файлам = отдельная задача.
- malformed scraper-row (sql-data-warehouse: «Workload group allocation by cap resource percent» разорван на 2 строки со сдвигом колонок) обработан WHOLE_LINE-override, line-parity сохранён.

**QA авто 0 проблем** (`_qa_l4if37.py`): line-parity 12/12, frontmatter byte-eq(\r-norm), em-dash=0, mojibake preserved-not-introduced (per-marker count EN==RU), BOM=0, URL-identity, fence-count, heading-parity, table-row integrity (cell-count + Name/Dimensions byte-EN, WHOLE_LINE-whitelist), leftover-EN scan (allowlist: image-captions, V1/V2 headings). Доп. детектор EN-function-words на non-table строках = пусто.

**Critical review:** independent-review субагент (read-only, general-purpose) 0 CRITICAL / 0 MAJOR / 3 MINOR. Из 3: (1) «Data space allocated» якобы непоследователен — **отклонён как false-positive** (sql-database desc = «Allocated data storage», elastic-pool desc = «Data space allocated», два РАЗНЫХ EN -> два разных RU, верно; «фикс» внёс бы mistranslation, проверено грепом); (2-3) «узлы, это узлы» в machine-learning -> переформулировал без тавтологии. Свой пасс: +1 фикс ambiguity attachment («входов ... заблокированных» -> «заблокированных брандмауэром входов»). EN-файлы не тронуты (mtime 2026-05-12, субагент read-only соблюдён, [[feedback_workflow_agents_may_write]]). Изменения: только docs/managed-ru/ (12 ф.) + scripts/_build_azure_metrics_l4if37* / _qa_l4if37*.

**Next:** azure-cloud-services-metrics остаток (engine готов, переиспользуем): Group A 24 (cache-for-redis 269 крупный, application-gateway, event-grid mixed-header, iot-hub, batch ...), Group B 20 (`Description|Unit|Recommended`), Group C 6 (`Unit|Dimensions`), синглтоны 4, irregular 15 (no-boilerplate builtin-* + extraH2 Limitations/Additional notes/Install OneAgent). Дальше azure-integrations прочее (~32), AWS 101, K8s 52. GCP крупные how-to (deploy-k8 706 и серия) и OTel-on-GCF go-файлы (1125/1250) под отд. сессии.

## L4-IF.36 (2026-06-05, Opus 4.8): GCP gcp-guide walkthrough/concept +5

**Прогресс:** 2215 -> 2220/2655 = 83.62%, pending 440 -> 435, orphan 0. GCP остаток 20 -> 15 (gcp-guide крупные how-to 5, OTel-on-GCF 6, cloudrun.md 1, legacy 3).

**Файлы (5, ручной Write по line-parity, все <400 строк, метод L4-IF.25):**
- gcp-guide/migrate-gcp-function-1-to-k8s-1.md (51; how-to миграция Functions 1.0 -> k8s 1.0)
- gcp-guide/monitor-multiple-projects.md (103; how-to: metrics scope, gcloud CLI + IAM, мультипроект; 3 code-fence byte-identical)
- gcp-guide/migrate-gcp-function.md (179; how-to на v.1.0, 4 Step-card императив=H2, dimension-changes таблица 55 строк byte-identical, `â¦`->«…»)
- gcp-guide/deploy-k8/self-monitoring-gcp.md (105; how-to, 3 таблицы Metric|Description: левый столбец метрик EN, описания RU)
- gcp-guide/deploy-k8/gcp-autodiscovery.md (219; how-to Early Access, services-таблица 76 строк byte-identical, params-таблица badge)

**Каноны (durable):**
- title-атрибуты ссылок (tooltip) ПЕРЕВОДЯТСЯ; для повторных целевых тянул из gcp-guide hub (shipped L4-IF.35): deploy-k8 tooltip = «Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.», link-text = «Настройка интеграции метрик и логов Dynatrace с Google Cloud в новом кластере GKE Autopilot»; gcp-integrations tooltip = «Настройка и конфигурирование Dynatrace в Google Cloud.» (41x); root google-cloud-platform = link «Настройка Dynatrace на Google Cloud» + tooltip «Мониторинг Google Cloud с помощью Dynatrace.».
- tag-line: `How-to guide`->`Практическое руководство`, `N-min read`->`Чтение: N мин`, `Published <Mon> <D>, <Y>`->`Опубликовано <D> <месяц-род> <Y> г.`, `Early Access` остаётся EN (100/100 корпус).
- Step heading `## Шаг N <текст>` (без точки, как EN `## Step N <текст>`); Step-card bold = императив, согласован с H2 (канон Java L4-IF.26).
- термины: dimension->измерение, deployment->развёртывание, dashboard->дашборд, auto-discovery->автообнаружение, feature sets->наборы функций, monitoring scope->область мониторинга, metrics scope->область метрик, scoping project->проект области метрик, self-monitoring->самомониторинг, ingestion->приём (метрик/логов), enrichment->обогащение, environment->окружение (НЕ среда).
- Required/Optional badge в params-таблице: полная форма с точкой-разделителем «Обязательный./Необязательный.» (правка по критич. ревизии: без точки «Необязательный При установке» рвано; точка чинит причину единообразно по 5 строкам; корпус согласует прил. с сущ. «Необязательный порт/файл», но при придаточном нужен разделитель).
- self-monitoring Metric|Description: левый столбец (имена метрик дашборда) EN (metric-leaf канон Name/identifier EN), заголовок+описание RU.
- мойибейк: `â` (em-dash в `X environmentsâsuggested`) -> двоеточие (§0), `ï»¿` (BOM) -> удалить, `â¦` -> «…». Опечатки внутри code-fence (`autodicovery`/`shoud`/`withthe`) сохранены byte-identical.

**QA авто 5/5 PASS** (`_qa_l4if36.py`, усилен vs L4-IF.35): line-parity, frontmatter byte-eq(\r-norm), em-dash=0, mojibake/BOM=0, URL-identity, fence-position + **fence CONTENT byte-identity** (новое), heading-parity, **table-row integrity** (новое: no-CYR строки == EN byte-identical ловит искажённый идентификатор; CYR строки pipe-parity). 7 WARN = калька «вы можете» (легитимно, корпус допускает). verify_corpus: RU 2220 / pending 435 / orphan 0 / source OK.

**Critical review:** independent-review субагент 0 CRITICAL / 0 MAJOR / 2 MINOR (badge-конструкция -> исправлено точкой-разделителем 5 строк). EN-файлы не тронуты (mtime 2026-05-12, субагент read-only соблюдён). Изменения: только docs/managed-ru/ (5 ф.) + scripts/_qa_l4if36*.

**Next:** GCP крупные how-to отд. сессия (deploy-k8 706, set-up-gcp-integration-logs-only 651/metrics-only 654/on-existing-cluster 735, deploy-with-google-cloud-function 470; shared deploy-структура); OTel-on-GCF серия (6 ф., go-файлы 1125/1250 огромные = под-сессии); cloudrun.md (742); legacy (3). Дальше Azure 113 / AWS 101 / K8s guides 52.

## L4-IF.35 (2026-06-04, Opus 4.8): GCP per-service monitoring leaves + hubs +10

**Прогресс:** 2205 -> 2215/2655 = 83.43%, pending 450 -> 440. GCP остаток 30 -> 20 (gcp-guide subtree 10, OTel-on-GCF walkthroughs 6, cloudrun.md 1, legacy 3).

**Файлы (10):**
- 5 metric-leaf (build-script `_build_gcp_metrics_l4if35.py`, канон L4-IF.34): cloudrun/cloud-run-monitoring (51), gcp-functions/cloud-functions-monitoring (45), google-app-engine/app-engine-monitoring (80), google-compute-engine/compute-engine-monitoring (385), google-gke/google-kubernetes-engine-monitoring (156). 4-колоночные таблицы: header переведён, Name/identifier EN, Unit переведён.
- 5 hubs (build-script `_build_gcp_hubs_l4if35.py`, построчный dict): gcp-functions (35), google-compute-engine (26), google-app-engine (89), gcp-guide (56), gcp-supported-service-metrics-new (99; services-таблица 40 строк, link-text = title целевой страницы, yes/no -> да/нет).

**Каноны (durable):**
- UNIT map дополнен: NanoSecond -> Наносекунда, MebiByte -> Мебибайт (раньше отсутствовали).
- Title `X with Operations suite metrics monitoring` -> `Мониторинг X с метриками Operations suite` (спец-кейс; generic `X monitoring` -> `Мониторинг X` оставил бы EN-хвост в заголовке).
- Hub services-table: link-text каждой строки = RU-title целевой страницы (кросс-страничная консистентность); yes -> да / no -> нет; entity-id EN; footnote `[1](#fn-1-1-def)` byte-identical.

**QA авто 10/10 PASS** (`_qa_l4if35.py`): 0 FAIL / 0 WARN. line-parity, frontmatter byte-eq, em-dash=0, mojibake/BOM=0, URL-identity, code-fence, heading-parity, calque, EN-leftover + 4-col table-integrity (leaves).

**Critical review:** independent-review субагент 0 CRITICAL / 0 MAJOR / 1 MINOR (gcp-supported шаги: `необходимо` + императив -> `выполните следующие действия:`, исправлено). Мой скепт-проход: zeugma чисто (`без выделения серверов и управления ими`), em-dash=0. git status: EN не тронут, субагент не писал.

**Build-инфра урок:** сырой мойибейк (`U+00EF U+00BB U+00BF`, `U+00E2 U+0080 ..`) в Python-исходнике через Write-тул схлопывается (Windows). Фикс: `_MJ`/`MOJI` через `\uXXXX`-escape, патчить файл Python-скриптом, не Write-тулом. RU-вывод писать `open(..., "wb")` (байты, LF, без trailing newline), markdown-форматтер тогда не трогает.

**Flag (вне scope батча):** `dynatrace-activegate/activegate-sfm-metrics.md` весь unit-столбец оставлен EN (Count/Byte/Millisecond/MebiByte), в отличие от GCP/Azure-канона (Unit переводится). Отдельное решение по этому файлу за пользователем.

## L4-IF.26 (2026-05-27, Opus 4.7) — Java technology-support family +3

**Прогресс:** 2144/2655 = 80.75%, pending 511 (было 514). technology-support 21→18 (фактический счёт по `_missing_now.py`).

**Файлы (3, manual Write 1:1 line-parity):**
- `technology-support/application-software/java.md` (45; хаб Java, `Incompatibility alert`, OpenTelemetry/JVM/JDK/Heap/JMX/CPU/GraalVM каталог тем)
- `technology-support/application-software/java/set-up-event-and-memory-alerting.md` (55; OOM/OOT, Step-1/Step-2 card+H2, metric-events table)
- `technology-support/application-software/java/g1-garbage-collector-java-9.md` (57; концептуальная статья про G1 GC; mojibake `Oracleâs/donât/itâs/doesnât/âunassignedâ` нормализованы)

**Метод:** ручной Write по line-parity (все 3 файла <400 строк → ниже порога build_*-скрипта по уроку L4-IF.25). Tag-line на основе типа документа: java.md = 3 строки (Reference + Чтение + Обновлено), set-up = 2 строки (Чтение + Обновлено, how-to), g1 = 2 строки (Чтение + Обновлено, концепт).

**QA авто 3/3 PASS** (`_qa_aix_l4if19.py`): line-parity 45/55/57, URL-identity, code-fence byte-identity, em-dash/BOM/double-BOM/broken-â = 0, heading parity, hard-break parity, frontmatter byte-eq. Легитимные WARN'ы: set-up L49-50 (metric-keys строки таблицы), g1 L14 (`Hotspot VM Oracle Java 9` — имя VM, 4 ASCII подряд).

**Критическая ревизия +2 правки:**
1. set-up L32 `в вашей среде` → `в вашем окружении` (канон [[feedback_environment_okruzhenie]]).
2. set-up L20 card `**Создание метрических событий**` → `**Создайте метрические события**` (согласование с L18 `**Включите функцию OneAgent**`, оба imperative как в EN).

**Канон Java technology-support (durable):**
- Tag-line type-aware: `Reference` (если есть в EN L11) = 3 строки, how-to/концепт = 2 строки.
- Mojibake `â` (U+00E2) внутри prose-апострофа (`Oracleâs/donât/itâs/doesnât`) и curly-quotes (`âunassignedâ`) → русский перевод убирает их естественно (нет апострофов / переход на «...» русские кавычки).
- Mojibake `ï»¿` (BOM в anchor-link `[SAP Introscope Agentï»¿]`, `[OpenTelemetry supportï»¿]`) → удалить.
- Названия технологий EN: Java, JVM, JDK, OneAgent, OpenTelemetry, JMS, RabbitMQ, JDBC, SQL/NoSQL, MongoDB, Cassandra, Redis, Heap, JMX, CPU, GraalVM, Quarkus, Eden, survivor, old generation/young generation, CMS (Concurrent Mark & Sweep), GC, G1, Hotspot VM, IBM JVM, OpenJDK.
- Card-pattern `[![Step N](svg "Step N")` → alt+title `Шаг N` (переводим).
- Bold-фазы GC EN: `**Initial mark**`, `**Concurrent mark**`, `**Final mark**`, `**Evacuation**`, `**Full GC**` (имена фаз = API/UI термины).
- Hard-break trailing `  ` (2 пробела для line-break) сохраняем побайтно.

**Next:** technology-support мелкие (`nginx/manual-runtime-instrumentation.md` 50, `top-java-memory-problems.md` 194, `support-for-jvms.md` 208, `dotnet.md` 113, `nodejs.md` 129) или OneAgent zOS большие (`zos-java-custom-jmx-metrics.md` 378 — наименьший из 11 zOS остатков).

## L4-IF.22 (2026-05-24, Opus 4.7) — OneAgent Windows family +9 (Windows subtree ЗАКРЫТ ЦЕЛИКОМ, >80%)

**Прогресс:** 2131/2655 = 80.26%, pending 524 (было 533). OneAgent 32→23. **Поддерево `windows/` ЗАКРЫТО ЦЕЛИКОМ** → все desktop/server ОС OneAgent (AIX/Linux/Solaris/Windows) закрыты, остаётся только мейнфрейм zOS (~22) + 2 общих.

**Файлы (9):**
- хаб `windows.md` (42; build_textmap) — простой link-формат как linux
- `windows/installation/install-oneagent-on-windows.md` (126; build_textmap, boilerplate-канон от AIX/Solaris)
- `windows/installation/customize-oneagent-installation-on-windows.md` (559; **build_difflib** Windows←Linux: 408 equal из RU-linux + 151 replace/insert override)
- `windows/installation/oneagent-security-windows.md` (128; build_textmap)
- `windows/installation/disk-space-requirements-...-windows.md` (114; build_textmap, таблица 1-колоночная %PROGRAMFILES%, таблица updates EXE/MSI с Σ)
- `windows/installation/how-to-pass-a-proxy-...-windows.md` (30; build_textmap)
- `windows/operation/stop-restart-oneagent-on-windows.md` (43; build_textmap, `net stop/start`)
- `windows/operation/uninstall-oneagent-on-windows.md` (69; build_textmap, WMIC/msiexec/PowerShell)
- `windows/operation/update-oneagent-on-windows.md` (188; **build_derive** ≈100% из RU-linux подстановкой Linux→Windows)

**Инструмент:** `scripts/_build_windows_l4if22.py` — `build_textmap` (exact-EN-line→RU, copy EN для blank/code/frontmatter, авто hard-break, normalize мojibake), `build_difflib` (SequenceMatcher equal→copy RU-брат / replace→override), `build_derive` (RU-брат + Linux→Windows подстановка). QA `_qa_aix_l4if19.py` (4-й переиспользуемый прогон).

**QA авто 9/9 PASS.** Критич. ревизия +3: «вы можете изменить»→«можно изменить»; «`LocalSystem` это учётная запись»→period-split «`LocalSystem`. Это…»; двойное «установщик для Windows для установки»→«установщик Windows».

**⚠ ГЛАВНЫЙ УРОК — auto-QA PASS ≠ полный перевод.** customize прошёл QA как PASS, имея 13 непереведённых EN-строк (`**Default value**`, `**Possible values:**`, `### Command line/Changing location`, `## Silent installation`, `#### Command shell`, `For example:`, `* 9-min read`, version-бейдж). leftover-эвристика strip'ает bold+code → короткие лейблы не флагуются; difflib equal-блоки переводят только совпавшие с linux строки, OS-специфичные значения (`npcap`, `%PROGRAMFILES%`) остаются EN в replace без override. **Поймано строгим сканом «EN-фраза(3+ латиницы) И отсутствие кириллицы на строке» + спот-чтением границ equal/replace-блоков.** Скан добавлен в обязательный чеклист (легитимно EN: mode-names `fullstack: Full-Stack Monitoring`, feature `Log Monitoring`, bold-UI option-labels).

**Канон Windows (durable):** tag-line verify-per-file (operation/hub/disk-space=2 строки, install=3 с How-to guide); `net stop/start "Dynatrace OneAgent"`; реестр Windows; Npcap/WinPcap/oneagentmon/dtuser/LocalSystem/LocalService/NT AUTHORITY\SYSTEM EN; DigiCert; `where X is service name`→«является именем службы»; групповые политики; bold UI option-labels EN; normalize Î£→Σ.

**Next:** OneAgent zOS (~22, CICS/IMS/zDC/zRemote мейнфрейм) для полного закрытия OneAgent; либо Azure 115 / AWS 103 / K8s 88 / GCP 66 / OTel 52 / extensions 47 / technology-support 20.

## L4-IF.21 (2026-05-24, Opus 4.7) — OneAgent Linux installation family +8 (Linux subtree ЗАКРЫТ ЦЕЛИКОМ)

**Прогресс:** 2122/2655 = 79.92%, pending 533 (было 541). OneAgent 40→32. **Поддерево `linux/` ЗАКРЫТО ЦЕЛИКОМ** (installation L4-IF.21 + operation L4-IF.20).

**Файлы (8):** хаб `linux.md` (53) + `linux/installation/`:
- `how-to-pass-a-proxy-address-during-oneagent-installation-on-linux.md` (36; Write)
- `install-oneagent-on-linux.md` (121; Write, зеркало AIX-брата для boilerplate)
- `oneagent-security-linux.md` (126; Write)
- `disk-space-requirements-for-oneagent-installation-and-update-on-linux.md` (124; Write, 3 arch-колонки x86/ppcle/s390)
- `linux-non-privileged.md` (155; Write, большая таблица Linux System Capabilities)
- `install-oneagent-on-ppc-be-linux.md` (93; Write)
- `customize-oneagent-installation-on-linux.md` (537; **difflib-деривация билдером**)

**Метод:** 7 файлов ручной Write (зеркалят переведённых AIX-братьев для канона). customize (537) собран `scripts/_build_customize_linux_l4if21.py` + data-файл `scripts/_l4if21_customize_trans.txt`: difflib-opcodes(EN-aix, EN-linux) → `equal`-строки копируются из переведённого RU-aix (356/537=66%), `replace`/`insert` prose (101) из data-файла, blank/code-fence/frontmatter-source из EN. Канон наследуется даром (en-dash из â, tooltips, URL).

**Канон (durable):**
- Хаб `linux.md` = ПРОСТОЙ link-формат `[text](url "tooltip")` (НЕ complex-card как `aix.md`) — verify-per-file (урок L4-IF.20). 2 tag-line (нет «Обзор»).
- Литеральные сообщения установщика в backticks остаются EN (`Non-privileged mode is enabled`, `Failed to enable non-privileged mode`).
- Чистый дефис-сепаратор `-` в arch/capability-списках не трогаем (не mojibake; §0); mojibake `â`-сепаратор → en-dash «–».
- `file capabilities`/`Linux Filesystem Capabilities`/`ambient capabilities`/`Go Discovery` EN; `**Default value**`→«**Значение по умолчанию**», `**Prerequisite**`→«**Предварительное условие**».
- Полная-bold prose-фраза переводится (firewall «**The remote Dynatrace addresses…**»), не UI-label (авто-QA пропускает).

**QA авто 8/8 PASS** (`_qa_aix_l4if19.py`). **Критическая ревизия +11 правок:** 5 «вы можете»→«можно» (fresh non-customize); 6 customize (двойное «для»; 3× «(В)ы можете X»→«X можно»; «X это Y»→«является ли это X»; «Вы также можете»→«Также можно»). Финал: окружение 31/среда 0, мониторируемые 7/мониторимые 0, инъекция+внедрить split; грепы калек = 0.

**Durable вывод:** difflib-деривация (L4-IF.20) МАСШТАБИРУЕТСЯ на крупные файлы (customize 537, 66% из брата). Триггер: переведённый cross-OS/cross-version брат с ratio>0.5.

**Next:** OneAgent остаток 32 (windows 9, zos 21, `oneagent-configuration-via-command-line-interface` 831, `oneagent-diagnostics` 280). Альтернатива: K8s 88 / Azure 115 / AWS 103.

## L4-IF.20 (2026-05-22, Opus 4.7) — OneAgent Linux operation family +5 (linux/operation subtree ЗАКРЫТ)

**Прогресс:** 2114/2655 = 79.62%, pending 541 (было 546). OneAgent 45→40. **Поддерево `linux/operation/` ЗАКРЫТО ЦЕЛИКОМ** (5/5).

**Файлы (5):** поддерево `dynatrace-oneagent/installation-and-operation/linux/operation/`:
- `stop-restart-oneagent-on-linux.md` (60; + раздел Hot cloning + Stop/Start через SystemV/systemd)
- `uninstall-oneagent-on-linux.md` (32; uninstall.sh + пути логов/конфигов + dtuser + symlink)
- `update-oneagent-on-linux.md` (188; деривирован из AIX-брата)
- `update-oneagent-on-ppc-be-linux.md` (50; PPC mv-шаги + общий tail «Проверка версии»)
- `how-to-enable-deep-monitoring-for-applications-confined-by-apparmor.md` (236; тяжёлые кодоблоки правил AppArmor)

**Метод:** единый 1:1 line-map builder `scripts/_build_linux_operation_l4if20.py` для всех 5 (copy-EN-байт для blank/code-fence/code/frontmatter-source-scraped, перевод prose по индексу строки → line-parity + байт-идентичные кодоблоки + LF/без BOM/без trailing newline). `update-oneagent-on-linux` особо: ВЫВЕДЕН из уже переведённого `update-oneagent-on-aix` (difflib EN-aix vs EN-linux = 3 отличия: title / нет строки `* How-to guide` / disk-space-ссылка) → копия RU-aix минус 1 строка + 3 правки.

**Канон (durable):** `Hot cloning`→«Горячее клонирование»; `where X is the init.d script`→«является скриптом `init.d`» (без тире §0); `mandatory access control`→«мандатное управление доступом»; disk-space tooltip `directory structure and disk space requirements`→«структуре каталогов OneAgent и требованиях к дисковому пространству»; `Optional`→«Необязательно»; tag-line linux-семьи = 2 строки (нет `* How-to guide`, в отличие от AIX) `* Чтение: N мин` / `* Опубликовано/Обновлено DD месяца YYYY г.».

**QA авто 5/5 PASS** (`_qa_aix_l4if19.py`): line-parity (60/32/188/50/236), URL-identity, code-fence byte-identity, em-dash/BOM/double-BOM/broken-â=0, heading/hard-break parity, frontmatter byte-eq. apparmor `[WARN] leftover-EN [106,114,122,184,201]` = комментарии/плейсхолдер ВНУТРИ кодоблоков (легитимно EN). **Критическая ревизия (EN vs RU построчно): +1 правка** — stop-restart L42 потеряно «alternatively» → «можно также». Финальные грепы калек («вы можете»/«, это»/«среда») = 0; em-dash 0; мониторируемые/инъекция консистентны.

**Next:** OneAgent остаток 40 (zos 20+zos.md, windows install/operation 8+windows.md, linux installation 7+linux.md, oneagent-configuration-via-command-line-interface 45K, oneagent-diagnostics). Альтернатива: K8s 88 / Azure 115 / AWS 103.

---

## L4-IF.19 (2026-05-22, Opus 4.7) — OneAgent AIX installation family +4 (AIX subtree ЗАКРЫТ)

**Прогресс:** 2109/2655 = 79.43%, pending 546 (было 550). OneAgent 49→45. **Поддерево AIX ЗАКРЫТО ЦЕЛИКОМ** (operation L4-IF.18, disk-space ранее, теперь хаб + installation).

**Файлы (4):**
- `aix.md` (90, хаб: complex-card канон 1:1 с `aws-lambda-integration.md`)
- `aix/installation/oneagent-security-aix.md` (93, Reference)
- `aix/installation/install-oneagent-on-aix.md` (192, How-to; boilerplate у соседа `solaris/install-oneagent-on-solaris`)
- `aix/installation/customize-oneagent-installation-on-aix.md` (404, How-to; 20 CLI-параметров)

**Метод:** хаб+security = Write; install+customize = 1:1 line-map builder (`scripts/_build_install_aix_l4if19.py`, `scripts/_build_customize_aix_l4if19.py`) — copy-EN-byte для blank/code-fence/frontmatter, перевод prose по номеру строки.

**Канон (durable):** card-CTA `Read this guide`→`Читать руководство`/`Read this reference`→`Читать справочник`/`Read this troubleshooting guide`→`Читать руководство по устранению неполадок`; `* How-to guide/Reference/Troubleshooting`→`* Практическое руководство/Справочник/Устранение неполадок`; `Overview`→`Обзор`; `**Default value**`→`**Значение по умолчанию**` (12×); `Deprecated`→`Устарело`; `Optional`→`Необязательно` (188× vs 8); bold UI-метки шагов EN (`**Verify the signature**`/`**Set customized options**`); mojibake-сепаратор `â` в list-items → en-dash «–» (в коде L22 → правильный `--`); CLI title-attr унифицирован «…без переустановки OneAgent».

**QA авто 4/4** (`scripts/_qa_aix_l4if19.py`, переиспользуемый): line-parity (90/93/193/405), URL-identity (incl. external https), code-fence byte-identity, em-dash/BOM/double-BOM/broken-â = 0, heading parity, hard-break parity, frontmatter byte-eq. Намеренный фикс mojibake: customize L22 `â-set-host-group`→`--set-host-group` (битый CLI-флаг, верно по дублю L231).

**Критическая ревизия +3** (авто-QA семантику не ловит): (1) двойное «окружения»→«идентификатором вашего [окружения] Dynatrace»; (2) двойное «для»→«установщик командной строки OneAgent … для настройки»; (3) «которые это позволяют»→«которые делают это возможным». Финальные грепы калек = 0; консистентность окружение/инъекция/мониторируемые.

**Next:** OneAgent остаток 45 (zos ~22, linux install/operation ~12, windows install/operation ~8, общие 3). Альтернатива: K8s 88 / Azure 115 / AWS 103.

---

## L4-IF.15 (2026-05-22, Opus 4.7) — Go technology-support family +6

**Прогресс:** 2091/2655 = 78.76%, pending 564 (было 570).

**Файлы (6):** поддерево `ingest-from/technology-support/application-software/go/` целиком, кроме go-known-limitations.md (665 строк, отложен):
- `go.md` (66, хаб: возможности мониторинга Go + 4 раздела + 6 блог-ссылок)
- `go/configuration-and-analysis/enable-go-monitoring.md` (56, статический мониторинг, встроенные правила)
- `go/configuration-and-analysis/full-code-level-visibility.md` (26, CPU-профайлер, Background vs Service CPU)
- `go/configuration-and-analysis/end-to-end-request-monitoring.md` (34, Service flow, PurePath)
- `go/configuration-and-analysis/analyze-go-metrics.md` (103, 5 вкладок метрик + планирование горутин M/P/G)
- `go/support/supported-go-versions.md` (130, таблицы поддержки + матрица версий; cp+Edit для byte-identical таблиц версий)

**Метод:** ручной prose-перевод (как L4-IF.1-13), НЕ build-script — семейство prose-тяжёлое (хабы/руководства/референс), не репетитивные таблицы. Стиль сверен с переведёнными соседями ruby/rust/cpp (L4-AG.1c.1).

**Канон grounded ГРЕПОМ корпуса ДО написания (урок L4-IF.14):**
- tag-line: `Справочник` / `Чтение: N мин` / `Опубликовано: DD месяца YYYY` / `Обновлено: DD месяца YYYY` (двоеточие, без «г.» — как ruby/rust/cpp, НЕ широкий корпус с «г.»).
- injection→инъекция (78× vs внедрение 14×); instrumentation→инструментация (parallel к инъекции); **Goroutine→горутина** (новый канон семейства, declinable; в корпусе было 0 → установлен).
- заголовки: Support→Поддержка, Configuration and analysis→Настройка и анализ, See also→См. также, Prerequisites→Предварительные условия, Version matrix→Матрица версий.
- alt-текст изображений ПЕРЕВОДИТСЯ (канон adaptive-traffic-management), UI-имена в alt (Service flow/Hotspots) EN.
- блог-ссылки: Blog:→Блог: + перевод заголовка.

**QA авто 6/6 clean:** line-parity EXACT (66/56/26/34/103/130), em-dash 0, frontmatter source/scraped byte-equal, URL-list IDENTICAL, anchors IDENTICAL, headings parity, table-rows parity, **RU mojibake 0**.

**Критическая ручная ревизия: 0 дефектов.** Грепы (`, это`/«вы можете»/«просто»/«доступно для») = 0 калек; термины консистентны (горутина 38×, рабочий поток, контекст планирования); 5 «Goroutine» EN легитимны (bold UI-метки L24/L98 + формальное опр. M/P/G L75 + таблица L81). Подтверждение урока L4-IF.14: pre-write corpus-grounding → 0 post-write правок.

**Решения по mojibake (отступление от byte-preserve канона L4-IF):** broken `â` (битый em-dash между словами, double-encoded `c3a2 c280 c294`) и BOM `ï»¿` это битые байты scrape, не контент. По глобальному CLAUDE.md §0 (запрет em-dash) и §1 (корень причины) рендерю правильной пунктуацией РЯ / удаляю BOM (совпадает с прямыми соседями ruby/rust/cpp). Edit не матчит multi-byte control-символы → L14-15 supported-go-versions заменён Python byte-exact.

**Гоча:** `_normalize_newline.py` нормализовал 33 файла (trailing newline/CRLF, контент не менялся) — весь RU-корпус, не только батч; безопасно (выравнивает line-parity к EN).

**Next:** Go-поддерево остаток 1 (go-known-limitations.md 665 строк). Далее: technology-support остаток (~24 prose) / OTel kafka+walkthroughs / крупные Azure/K8s/GCP.

---

## L4-IF.14 (2026-05-22, Opus 4.7) — Azure AI metrics sub-family (build-script) +21

**Прогресс:** 2129/2655 = 80.19%, pending 526 (было 547).

**Файлы (21):** `ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-*.md` — когнитивные сервисы Azure: all-in-one, anomaly-detector, bing-{autosuggest,custom-search,entity-search,search,spell-check}, computer-vision, content-moderator, custom-vision-{prediction,training}, face, immersive-reader, language-understanding{,-authoring}, openai, personalizer, qna-maker, speech, text-analytics, translator.

**Метод:** build-script `scripts/_build_azure_ai.py` + QA `scripts/_review_azure_ai.py` (а не ручной prose-перевод — семейство высоко-репетативно: общий boilerplate «View service metrics» + варьируются title/версии/intro/таблица). Byte-safe substring-replace по EN: mojibake-эллипсис `**â¦**` (6 байт) и trailing-2-spaces hard-break проходят насквозь (ключи замен их не пересекают). Таблицы парсятся по ячейкам — Name+Dimensions EN, Description/Unit/Recommended переведены (снимает коллизию `| Latency | Latency |` у openai).

**Канон grounded ГРЕПОМ корпуса ДО написания:**
- `## Prerequisites` → `## Предварительные условия` (корпус 40/40 split → канон L4-IF.7).
- step-4 boilerplate → доминанта корпуса 33×.
- link-text `Enable service monitoring` → `Включение мониторинга сервиса` (32×).
- `**Dashboards**` остаётся EN (style-guide UI-bold, вопреки 15× «Панели мониторинга»).
- Units: Count→Количество, Byte→Байт, Percent→Процент, MilliSecond→Миллисекунда; Applicable→Применимо.

**QA авто 21/21 clean:** line-parity EXACT, em-dash 0, frontmatter source/scraped byte-equal, URL-list IDENTICAL, mojibake count EN==RU, 0 leftover-EN (~38 контрольных). Build-warnings 0 (полнота cell-maps: DESC_MAP 29 + UNIT_MAP 5 + REC_MAP).

**Критическая ручная ревизия: 0 дефектов** (openai/all-in-one/translator/bing-search целиком + все 21 title/H1 + греп ", это"/em-dash/double-space). Урок L4-IF.14: для структурированных таблиц + corpus-grounded boilerplate ноль дефектов это норма — защита смещена в pre-write греп, не post-write правки.

**Сохранённые баги источника:** all-in-one ServerErrors `5xx` без бэктиков + ClientErrors «client side» без дефиса; openai inline-версия «1.272+Environment»; content-moderator title без дефиса; openai title без «monitoring». **Гоча:** hdinsight + sql-managed-instance = OLD pre-restructure (scraped 2026-03, нет line-parity), не эталон.

**Next:** Azure остаток 118, K8s 92, GCP 65, AWS 61, OneAgent 56, OTel 54, extensions 47, technology-support 31.

---

## L4-IF.9 (2026-05-21, Opus 4.7) — lambda-otel-bridge-python.md

**Прогресс:** 2103/2655 = 79.21%, pending 552.

**Файл:** `ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-python.md`, 587 строк (OpenTelemetry interoperability in Python: Before you start с таблицей совместимости OneAgent↔OpenTelemetry API; Use OpenTelemetry Python instrumentation с примерами aiopg+PostgreSQL и botocore+DynamoDB; Use OpenTelemetry Python API SDK-style tracer; Trace AWS SQS and SNS messages with Python — 3 шага Install dependencies / Send / Receive с примером SQS-триггера и таблицей raw message delivery enabled/disabled).

**QA 8/8 OK:**
- Line-parity 587/587 EXACT
- Em-dash в RU: 0
- BOM `ï»¿` byte-perfect 8/8
- Broken char `â` byte-perfect 1/1 (manual-triggerâprocess)
- URLs IDENTICAL (15/15)
- Anchors IDENTICAL (6/6)
- Headings count: `^##` 8/8, `### Шаг` 3/3
- Frontmatter source/scraped byte-preserved

**Ручная критическая ревизия после авто-QA (lesson L4-IF.8 in action):**
- (1) «при использовании AWS Lambda с триггером SQS, мониторинг которой ведётся через» → «при использовании Lambda-функции с триггером SQS, мониторинг которой ведётся расширением» (согласование рода: AWS Lambda как сервис без склонения; "которой" теперь привязано к Lambda-функции).
- (2) «у span может быть только один родитель» → «у span'а может быть только один родитель» (склонение span'а в род.падеже).
- (3) «если вы хотите отслеживать их по отдельности» → «если требуется отслеживать их по отдельности» (выбраковка кальки "want to").
- (4) «Если вы вызовете отправителя и развернули пример, он будет автоматически вызван по SQS» → «Если вы развернули пример и вызвали отправителя, он будет автоматически запущен по SQS» (несогласование времён исправлено + invoked→запущен по контексту).
- (5) «Часто для батча сообщений приходится более одного узла» → «Часто на батч сообщений приходится более одного узла» (естественный предлог).
- (6) «Это может произойти даже когда сообщения» → «Это может произойти, даже когда сообщения» (запятая перед составным союзом «даже когда» в середине предложения).

**Lessons L4-IF.9:**
1. `span` (атомарный технический термин OpenTelemetry) склоняется через апостроф: `span'ов`, `span'у`, `у span'а`; канон из предыдущих файлов сохранён.
2. «AWS Lambda» как сервис, без склонения; «Lambda-функция» склоняется как существительное женского рода; при наличии «which/whose» в EN переключаемся на «Lambda-функция, которая/мониторинг которой».
3. EN bullet markers `+` (вложенные списки) сохранены byte-perfect, не заменены на `*` или `-`.
4. Auto-QA `grep -c "—"` + анкоры `grep -oE '\(#[a-z]'` + URL diff покрывают форму, но НЕ ловят кальки времени («Если вы X-ете и Y-ли»); нужна сплошная глазная проверка инструктивных конструкций «If you... it will...».
5. «want to» в инструкциях лучше менять на «требуется/нужно/необходимо», а не калькировать «вы хотите» (правило из TRANSLATION_STYLE_GUIDE.md, продолжен канон).

---


Started: 2026-05-12
Last update: 2026-05-21 (Opus 4.7 L4-IF.8 +2 = **2102/2655 = 79.17%**, pending 553. **L4-IF.8 batch AWS Lambda .NET OTel ЗАКРЫТ:** (1) ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration.md 1007 строк (Trace .NET Lambda functions, центральный документ .NET, Prerequisites / Installation / Compatibility OpenTelemetry+System.Diagnostics.DiagnosticSource / Initialization Function.cs / 3 примера трассировки входящих вызовов через AWS SDK / Amazon API Gateway HTTP / без `AwsLambda` пакета, Tracing AWS SDK calls включая DynamoDB+SQS/SNS, HttpClient instrumentation, container images); (2) ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native.md 467 строк (Trace AWS Lambda .NET Core functions with OpenTelemetry .NET, deprecated в пользу .md выше, 3 шага Set up export / Add dependencies / Add OpenTelemetry Tracer, ARN ADOT Collector Lambda Layer, ADOT Collector YAML config, CloudFormation, OtlpExporterOptions gRPC+HTTP). QA 7/7 ALL PASS × 2 файла = 14/14 OK: line-parity (1007/1007 + 467/467 EXACT), em-dash 0 в обоих, BOM/mojibake byte-perfect (ï»¿ 6/6 + 9/9, broken â 3/3), URLs identical (diff IDENTICAL × 2), headings count 16/16 + 9/9 EQ, frontmatter source+scraped byte-preserved, UI-bold EN-вербатим (**Settings**/**Preferences**/**OneAgent features**/**Send W3C Trace Context HTTP headers**/**HTTP exporter**/**gRPC exporter** EN; **Set up export**/**Add dependencies**/**Add OpenTelemetry Tracer** → русские названия шагов как в aws-lambda-otel-setup.md канон L4-IF.7), calques 0 (3 проблемных ', это'-конструкций отловлены grep после первичного прохода и поправлены: 'где `Function`, это настроенный класс-обработчик'→'где `Function` обозначает настроенный класс-обработчик', 'Учтите, это требует значительной работы'→'Учтите, что это требует значительной работы', 'Lambda layers, это региональный ресурс'→'Lambda layers являются региональным ресурсом'). Канон L4-IF.5/6/7 применён единообразно: How-to guide→Практическое руководство, X-min read→Чтение: X мин, Updated on Aug 24, 2023→Обновлено 24 августа 2023 г., Updated on Sep 23, 2022→Обновлено 23 сентября 2022 г., Step N→Шаг N (с переводом названий шагов в bold), AWS Lambda invocations→вызовы AWS Lambda, instrumentation→инструментация, auto-instrumentation→автоматическая инструментация, trace/tracing→трассировка/трассировать, span→span (EN), Activity/ActivitySource→Activity/ActivitySource (EN, имя класса .NET), exporter→экспортёр, endpoint→эндпоинт, propagation→propagation (EN, технический термин OpenTelemetry), cold start→холодный старт, wrapper-слой→wrapper-слой (EN+дефис, канон из aws-lambda-extension.md), Lambda functions→Lambda-функции (через дефис). Новая канон-точка L4-IF.8: имя класса .NET `Activity` склоняется как фем («Activity, трассирующая входящий запрос») для естественности; имя метода `Trace`/`TraceAsync` НЕ склоняется (бэктики). **Next:** ingest-from 553 (3 lambda-otel-bridge файла Python/Node.js/Java 587+779+631 = 1997 строк остаются в opentelemetry-interoperability/, AWS 62+ файлов integrate-with-aws/aws-all-services/aws-service-*.md мелкие, Azure 139, GCP 65, K8s 92, OTel 59, OneAgent 57). Prev L4-IF.6 +2 = 2097/2655 = 78.98% (AWS Lambda Classic prose файлов: (1) ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images.md 235 строк (How-to AWS Lambda container images, Step 1 Configuration / Step 2 Copy snippet / Step 3 Add extension, ENV-блок DT_TENANT/DT_CLUSTER_ID/DT_CONNECTION_BASE_URL/DT_CONNECTION_AUTH_TOKEN, два варианта `dt-awslayertool`/`AWS CLI`, sample `Dockerfile` для Node.js Lambda с интеграцией Dynatrace OneAgent extension); (2) ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension.md 389 строк (How-to центральный документ classic-интеграции для Python/Node.js/Java Lambda, 8 шагов навигатора Enable→Choose method→Endpoint→RUM→Layer name→Deployment→Configuration options→Dynatrace AWS integration, 6 методов конфигурации JSON/env-vars/Terraform/SAM/serverless/CloudFormation, Secrets Manager AWS OneAgent 1.295+, Filter cold starts, Monitoring overhead Python ~1000ms / Node.js ~700ms / Java >1000ms, ограничения Java handler-method/Node.js ES modules/Lambda Managed Instances). QA 10/10 ALL PASS × 2 файла = 20/20 OK: line-parity (235/389 EXACT), em-dash 0 (включая horizontal-bar/figure-dash variants), BOM/mojibake byte-perfect (tree-glyphs ├──/└── в файле 1 и `â¦` ellipsis в файле 2 совпадают по байтам после правки), URLs identical (13/42), headings 14/23 EQ, bullets 12/77 EQ, code-fences 8/0 EQ, frontmatter source+scraped byte-preserved, calques 0, EN signal-words 0 (false-positive «configuration» в URL-якоре `#configuration` отсеян). Канон L4-IF.5 применён единообразно: How-to guide→Практическое руководство, X-min read→Чтение: X мин, Updated on Jan 22 2026→Обновлено 22 января 2026 г., Step N→Шаг N, Prerequisites→Предварительные условия, Configuration→Конфигурация, Configuration options→Параметры конфигурации, Limitations / Known limitations→Ограничения / Известные ограничения, Related topics→Связанные темы, Optional→необязательный, Deployment→Развёртывание. **UI bolds оставлены EN** (Deploy Dynatrace, Start installation, AWS Lambda, Add layer, Specify an ARN, Enable Monitoring for AWS Lambda Functions, Capturing, Mapping Templates, Save, Edit, View all requests, Function cold start, Forward Tag 4 trace context extension, Use Lambda Proxy Integration, Integration Request, Web, Mobile, Frontend, Custom Applications, unmonitored hosts). **Lessons L4-IF.6:** (1) tree-glyph mojibake `├──`/`└──` НЕ Read-эквивалент `âââ`: исходник содержит 6-байтные последовательности (├── = c3 a2 c2 94 c2 9c c3 a2 c2 94 c2 80 c3 a2 c2 94 c2 80), буквальная запись `âââ` в Write даёт `c3 a2 c3 a2 c3 a2` (2 байта/глиф); решение: после Write вычитать байты строки из источника и собрать src_glyph_part + space + dst_name. (2) ellipsis mojibake `…` в menu **â¦** = 5-байт (c3 a2 c2 80 c2 a6), не 4-байт (c3 a2 c2 a6); одиночный data.replace(old,new) после Write фиксит byte-perfect. (3) EN signal-words «configuration»/«deployment» false-positive если внутри URL-якоря (#configuration) или bold-заголовка шага (**Конфигурация**); QA-script должен отсекать markdown-links целиком, иначе ложные срабатывания. (4) AWS Lambda layer (нижний регистр layer) оставляем как термин по аналогии с trace-lambda-functions.md (не «слой»). (5) em-dash mojibake `â` в исходнике на месте EN em-dash («whichâwithout configurationâprevents») заменяем на скобки или двоеточие (по CLAUDE.md §0): «что (без дополнительной конфигурации) не даёт». Расхождение `â` 6→1 байт между src/dst по дизайну, не баг. **3 минор-фикса critical-review ДО публикации:** (1) deploy-oneagent-on-lambda-container-images L134/138/142 tree-glyphs `âââ` (2-байт) → `├──`/`└──` (6-байт) через byte-rewrite после Write. (2) aws-lambda-extension L168 menu-ellipsis `â¦` (4-байт) → `â¦` (5-байт) через data.replace. (3) aws-lambda-extension L198+L322 EN em-dash mojibake `â` в prose → скобки/двоеточие. **ПРЕДЫДУЩИЕ:** L4-IF.5 +2 = 2095/2655 = 78.91%, pending 560 (deploy-oa-latest-lambda-container-images.md 227 + trace-lambda-functions.md 460). L4-IF.4 +3 = **2093/2655 = 78.83%**, pending 562. **L4-IF.4 batch 3 prose файлов ЗАКРЫТ:** (1) ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector.md 168 строк (How-to AWS Lambda log collection, OneAgent versions 1.263/1.275/1.291/1.295, JSON/env-var конфигурация EventTypes/Endpoint/AuthTokenSecretsManagerArn/Filter, 6 уровней логирования TRACE→FATAL); (2) ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md 188 строк (How-to Enable service monitoring, 98-строчная таблица тегирования сервисов AWS с yes/-, разделы Recommended/Optional metrics со статистиками Sum/Min/Max/Avg/SampleCount); (3) ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix.md 113 строк (Reference, структура каталогов OneAgent на AIX, ~9.4 ГБ total, INSTALL_PATH/LOG_PATH/DATA_STORAGE параметры, persistence.reliable_mode/total_limit_kb). QA 8/8 ALL PASS × 3 файла = 24/24 OK: line-parity (188/168/113 EXACT), em-dash 0, BOM/mojibake 0, URLs identical (3/25/6), headings 9/14/8 EQ, bullets 10/30/12 EQ, code-fences 0/0/0 EQ, frontmatter source+scraped byte-preserved, тег-канон, calques 0, EN signal-words 0. Канон L4-IF.3 применён единообразно: How-to guide→Практическое руководство, Reference→Справочник, 2-min/3-min/7-min read→Чтение: 2/3/7 мин, Published Nov 09, 2023→Опубликовано 9 ноября 2023 г., Updated on Dec 17, 2025→Обновлено 17 декабря 2025 г., Updated on Jun 25, 2025→Обновлено 25 июня 2025 г., Prerequisites→Предварительные условия, Deploy→Развёртывание, Usage→Использование, Configuration→Конфигурация, Limitations→Ограничения, Troubleshooting→Устранение неполадок, Related topics→Связанные темы; Optional→необязательный (NOT «Опциональный»). **3 минор-фикса critical-review ДО публикации:** (1) **aws-enable-service-monitoring L35** «до того, как» → «прежде чем» (стилистика). (2) **aws-enable-service-monitoring L161** «Метрики уровня сервиса, это метрики для всего сервиса» → «Метрики уровня сервиса собираются для всего сервиса» (тавтологический повтор «метрики» при длинном определении, перефразировка через глагол). (3) **collector L53** «а содержимое логов `function`, в виде простого текста» → «а содержимое логов `function` будет в виде простого текста» (пропущенный глагол после запятой = двусмысленность в РУ). **Lessons L4-IF.4:** (1) **«X, это Y» канон работает не везде** — годится для коротких определений (например «Dimension, это параметр»), но при длинных параллельных конструкциях («Service-wide metrics are metrics for the whole service across all regions») тавтологический повтор виден. Перефразировать через глагол («собираются»/«представляют») когда определение длинное. (2) **«до того, как» = риторическая калька** EN «before...» → «прежде чем» в контексте «нужно подождать X, прежде чем Y». (3) **EN parallel structure с пропущенным глаголом** («platform logs will be JSON data, while function logs will be plain text») в РУ требует ЯВНЫЙ повтор глагола «будет», запятая-сокращение «`function`, в виде» = двусмысленно. (4) **AIX-числа с десятичной запятой**: «1.5 GB» → «1,5 ГБ», «9.4 GB» → «9,4 ГБ», «1.1 GB» → «1,1 ГБ» (РУ-стандарт), но в коде/формулах десятичная точка сохраняется «(размер + размер) * 1.1». (5) **EN опечатка «genereted»** в `persistence.reliable_mode` PARAM_DESC сохранена как «генерируются» в РУ (мы переводим смысл, баг EN не правим). **Next milestone:** ingest-from остаток 562 (AWS 75, Azure 139, GCP 65, K8s 92, OTel 59, OneAgent 56, extensions 47, technology-support 26). **Prev L4-AG.1b.2:** +24 = **2079/2655 = 78.30%**, pending 576, Orphan RU 0, **dynatrace-api 1142/1142 = 100% ✅ КОРПУС DYNATRACE-API ПОЛНОСТЬЮ ЗАКРЫТ** (configuration-api JSON-models закрыты L4-AG.1b.2); **builtin schemas 307/307 (100%) ✅ ПОЛНЫЙ КОРПУС BUILTIN ЗАКРЫТ**. **L4-AG.1b.2 batch 2 финальных dynatrace-api JSON-models файлов ЗАКРЫТ** (automatically-applied-tags-api/models.md 1376 строк / management-zones-api/json-models.md 1371 строка). Build [`scripts/_build_dynatrace_api_l4ag1b2.py`](scripts/_build_dynatrace_api_l4ag1b2.py). Twin-pair 99% идентичны (различаются только title/H1/Deprecated-ссылками/intro/Published date/Related topics в одном из двух). Канон L4-AG.1c.1 / L4-AG.1b.1 повторён: TITLE_MAP + DATE_MAP + HEADING_MAP (H2 + Related topics) + H4_OBJECT_MAP (35 имён классов «#### Объект \\`Name\\`») + COMPARISON_MAP (26 ENUM-типов «Сравнение для атрибутов \\`X\\`») + KEY_TYPE_MAP (4 KEY-типа «Ключ для динамических атрибутов типа \\`X\\`») + PARA_MAP (длинная operator description + 2 варианта Deprecated + 2 варианта intro + TagInfo/SimpleTech/SimpleHostTech/Custom*MetadataKey шары) + STANDALONE_LINE_MAP (Parameters/JSON-модель) + TABLE_HEADER_MAP (| Поле | Тип | Описание |) + TOOLTIP_MAP + LINK_LABEL_MAP (longest-first sorting); JSON-блоки (60 ``` code fences = 30 примеров) safe-by-construction: содержат только API-ключи, не пересекаются с substring-маппингами. Mojibake EN-аудит: BOM 0, single 0, triple-apos 0, double-B 0, em/en-dash 0 (полностью чистые файлы). Line-parity 2/2 EXACT (1376/1371 строк). Verification: em-dash 0, mojibake leftover 0, EN signal-words leftover 0 (проверены: Operator/You can reverse/The element can hold/The value to compare/The comparison is case-sensitive/Comparison for `/The key for dynamic attributes/Predefined technology/Tag of a Dynatrace entity/This API is deprecated/Some JSON models/Parameters/JSON model/Deprecated/Published Aug/Published Apr/## Variations/## Related topics/#### The `/Element-Type-Description-header/Reference), calque `, и `/`, или ` 0. **Lessons L4-AG.1b.2:** (1) **Twin-pair 99% идентичных файлов с разными Deprecated-ссылками** (twin pair на уровне API endpoints вместо schemas) идеально консолидируется через PARA_MAP — 30+ повторяющихся фраз покрывают 99% содержимого, уникальные только 4 параграфа (Deprecated × 2 + intro × 2). (2) **JSON-блоки** (60 ``` code fences = 30 примеров): содержат только JSON-ключи «operator/value/negate/type/dynamicKey/source/key/context/attribute» — английские атрибуты, не используются как substring-цели в substring-passe. Safe-by-construction, не нужны спец-исключения. (3) **Имена JSON-классов** (35 объектов: ApplicationTypeComparison/CustomHostMetadataConditionKey/TagInfo/SimpleHostTech/...) **и ENUM-значения** (30 ATTRIBUTE/_KEY/_NAME) **НЕ переводим** — устоявшиеся API-идентификаторы. Переводим только wrapping prose: «Объект \\`Name\\`», «Сравнение для атрибутов \\`X\\`», «Ключ для динамических атрибутов типа \\`X\\`». (4) **DATE_MAP для Published date** — два варианта (Aug 13, 2019 vs Apr 29, 2020); канон обычно через regex `_translate_date_lines`, но при 2 вхождениях проще явный dict-перевод. (5) **Двойной пробел EN «\\`true\\`.  Possible values...»** в operator description заменён на одинарный («\\`true\\`. Возможные значения...») — РУ-стандарт одиночного пробела между предложениями важнее EXACT byte-equivalence. (6) **Typo источника** AzureSkuComparision/BitnessComparision/HypervisorTypeComparision (вместо Comparison) сохранены — баг EN-источника не правим (L4-AG.1b.1 lesson 2). (7) **dynatrace-api корпус ЗАКРЫТ 1142/1142 = 100%** — после builtin 307/307 это **второй полностью закрытый sub-корпус** проекта (builtin schemas + dynatrace-api). Следующий milestone — ingest-from (большой раздел integrations: AWS/Azure/GCP/Kubernetes/...). **Prev L4-AG.1b.1 batch 2 cluster-api hub-страниц ЗАКРЫТ** (cluster-api-v1.md 85 строк / cluster-api-v2.md 90 строк). Build [`scripts/_build_dynatrace_api_l4ag1b1.py`](scripts/_build_dynatrace_api_l4ag1b1.py). Канон L4-AG.1c.1 повторён: TITLE_MAP + HEADING_MAP + PARA_MAP + TOOLTIP_MAP (longest-first ДО LINK_LABEL_MAP) + LINK_LABEL_MAP (longest-first) + date_lines. Mojibake EN-аудит: BOM 0, single-â 0, triple 0, double-B 0, em/en-dash 0 (чистые файлы). Line-parity 2/2 EXACT (85/90 строк). Verification: em-dash 0, mojibake leftover 0, EN signal-words leftover 0, calque `, и`/`, или` 0. **Lessons L4-AG.1b.1:** (1) **hub-страницы list-of-links** = идеальный кейс для substring-pass канона L4-AG.1c.1 (longest-first TOOLTIP+LINK_LABEL разруливает HA- vs не-HA коллизии); (2) **наследованные баги EN-источника не правим** (например cluster-api-v1 lines 81-82: tooltip говорит «specific cluster user» для user-group ссылки — баг EN, не наша задача); (3) **«Internet proxy»→«Интернет-прокси»** — устоявшаяся пара в RU IT-документации; «High Availability» оставлен EN (термин), «развёртывания» переведено. **Prev L4-AG.1a.15a+b batch 7 финальных builtin schema-table 12-31KB ЗАКРЫТ** (5 в 15a: infrastructure-disk-edge-anomaly-detectors 12.2KB / management-zones 12.9KB / os-services-monitoring 12.3KB / tags-auto-tagging 12.0KB / anomaly-detection-infrastructure-hosts 16.3KB; 2 в 15b: appsec-notification-integration 20.8KB / problem-notifications 30.8KB). Build [`scripts/_build_schemas_l4ag1a15a.py`](scripts/_build_schemas_l4ag1a15a.py) + [`scripts/_build_schemas_l4ag1a15b.py`](scripts/_build_schemas_l4ag1a15b.py). **15a:** twin pair management-zones↔tags-auto-tagging (общий AttributeCondition + entityType enum), twin-like disk-edge↔os-services-monitoring (общие `$X(...) - Matches` bullet-описания match-pattern, triple-en-dash 24+35=59). Канон L4-AG.1a.9 TM_ENDASH через chr(0xE2)+chr(0x80)+chr(0x93). **15b NEW КАНОН: PLACEHOLDER_GLOSSARY** — глобальная substring подстановка повторяющихся placeholder-описаний ДО построчного парсинга. 11 nested типов problem-notifications (Email/Slack/Jira/AnsibleTower/OpsGenie/PagerDuty/VictorOps/WebHook/XMatters/Trello/ServiceNow) + 6 payload типов appsec используют идентичные placeholder-блоки (~30 уникальных placeholders повторяются ~100 раз). Replace ИХ через `GLOBAL_PHRASES` substring-pass на RU-эквиваленты; длинные cells получают частичный перевод (placeholders + intro переведены глобально, prefix через PARAM_DESC, остальное EN). **Mojibake-аудит EN:** 15a — triple-en-dash 59 (TM_ENDASH через chr()), mojibake-BOM в hyperlink-текстах (чистится `_normalize`), single 0 real. 15b — только mojibake-BOM 7+10 в hyperlink-текстах, никаких triple/double-B/single. **Verification 7/7 EXACT line-parity** (120/102/89/88/257/127/185 строк). **2 деф пойманы critical-review ДО публикации:** (1) **5 em-dash в моём переводе problem-notifications** (CLAUDE.md #0): 3 в `**{ProblemDetailsJSONv2}**` («recentComments — нет» → «recentComments не входит») + 2 в ServiceNow («Поле взаимоисключающее с полем **url/instanceName** — допустимо» → «: допустимо»). Фикс GLOBAL_PHRASES + PARAM_DESC. (2) **Signal-words detector ловит RU-переводы где сохранены технические термины:** `**Note:** Security notifications`, `**{CvssScore}**: CVSS score`, `**{DavisSecurityScore}**: [Davis`, `**{SecurityProblemUrl}**: URL` — все 4 = ПОДТВЕРЖДЁННЫЕ false positives при spot-check (детектор ловит подстроку, начинающую RU-предложение). **Финальный критичный обзор всех 7:** em-dash 0, mojibake-BOM 0, ENUM-leftover 0, ## Authentication-leftover 0, ## Parameters-leftover 0, single_a 0, calque 1 false positive (os-services-monitoring «отдельно, и часть параметров», правильное закрытие сложноподчинённого), signal-words 0 настоящих EN-leftover. **Lessons L4-AG.1a.15:** (1) **PLACEHOLDER_GLOSSARY = новый канон для notification-типа документов** — substring-replace ДО построчного парсинга работает на cells которые НЕЛЬЗЯ точно матчить целиком (длинные мульти-предложения с placeholder-списком; 100+ повторений placeholder-определений между 11 nested-объектами). Каждый cell получает частичный перевод (intro + placeholders), что покрывает ~85% объёма. (2) **Em-dash появляется в МОЁМ переводе через "тире" в substitution-маппинге**, не только через прямой EN-passthrough. Прогонять critical-review review-скриптом включая `chr(0x2014)` count после КАЖДОГО изменения PARAM_DESC/GLOBAL_PHRASES, не только после первого билда. (3) **Signal-word detector с substring-keys ловит false positives** на RU-переводах, где исходно EN-фраза начинала RU-предложение (например `**{CvssScore}**: CVSS score` — `CVSS score` намеренно сохранён как термин в RU). Не доверять детектору слепо, всегда spot-check'ить контекст. (4) **Twin pair вне sub-family** (management-zones↔tags-auto-tagging) консолидируется через общий PARAM_LABEL для shared полей (AttributeCondition.key enum 250 значений, operator enum 24 значения, Apply to... propagation 6 полей) — общий PARAM_LABEL покрывает ~70% обоих файлов, уникальные только SCHEMA_DESC и top-level fields. (5) **builtin корпус ЗАКРЫТ 307/307 = 100%** — впервые с начала проекта L4-AG.1a, 15 sub-батчей, 307 файлов, общий канон chr() для 8 типов typographic mojibake + PARAM_LABEL/PARAM_DESC/STRUCT/SCHEMA_DESC dict + line-parity exact + signal-word detector. **Next: L4-AG.1b или L4-AG.2** — переход к остальным dynatrace-api 4 pending + ИЛИ к другим разделам managed-ru (notifications/management). **Prev L4-AG.1a.14c batch 13 builtin openpipeline-data-forwarding ~19KB ЗАКРЫТ** (logs/spans/events/metrics/bizevents/events-sdlc/user-events/davis-events/usersessions/system-events/davis-problems/events-security/security-events = pipelines sub-family). Build [`scripts/_build_schemas_l4ag1a14b.py`](scripts/_build_schemas_l4ag1a14b.py) повторяет канон 14a + расширяет PARAM_LABEL под top-level pipelines-поля. **Канон pipeline-groups (L4-AG.1a.6) повторно применён к pipelines:** один SCHEMA_DESC «Содержит конфигурацию pipelines» + 13 уникальных DISPLAY_NAME с kind в скобках (логи/события/метрики либо EN-термины Dynatrace для API-имён с точкой). **Top-level PARAM_LABEL сужено до 3 ключей** (Pipeline metadata list, Custom pipeline id, Group role) — 9 stage-полей (Processing/Security context/Cost allocation/Product allocation/Storage/Smartscape node extraction/Smartscape edge extraction/Metrics extraction/Davis event extraction/Data extraction stage) + Display name + Routing намеренно оставлены EN-терминами по канону 14a «Processing stage» (устоявшиеся технические термины openpipeline, согласованность с предыдущим под-батчем). **Mojibake-аудит EN ДО билда:** BOM 0/13, single 0/13, triple-* 0/13, double-B 0/13, double-decoded WARN 0/13, mojibake-BOM `ï»¿` 13/13 (1 на файл, внутри hyperlink-текста `[See our documentation]ï»¿`), чистится `_normalize`. Самый лёгкий батч по mojibake (как и 14a). **Verification:** line-parity 13/13 EXACT (349 строк/файл, identical structure pipelines × 13 kinds), em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, signal-words 0, mojibake leftover 0, EN-DISPLAY_NAME leftover 0. **1 деф пойман при critical-review ПОСЛЕ первой сборки:** stage-поля изначально были «Stage для X» (калькообразно, особенно «Stage для storage» с двойным storage; не согласовано с уже принятым в 14a термином «Processing stage» EN). Фикс: 9 stage-ключей + «Display name» + «Routing» удалены из PARAM_LABEL (теперь `_param_row` возвращает None → строки проходят целиком в EN, ENUM-перевод глобальный сохраняется). Spot-check builtin-openpipeline-logs-pipelines.md строки 37-51 (top-level), 66-97 (Processor с 22 атрибутами) = **0 семантических деф**. **Lessons L4-AG.1a.14b:** (1) **Сужение PARAM_LABEL = метод сохранить термин** — если ключ должен остаться EN, не писать nop-pair `"X": "X"`, а просто не класть в dict; ENUM-перевод глобален через `t.replace()` ДО loop, так что описание enum переводится независимо. (2) **«Stage для X» = калька** — устоявшиеся термины openpipeline UI («Storage stage», «Security context stage») остаются EN целиком, как «Processing stage» в 14a. Канон: при наличии устоявшегося EN-термина из UI, не изобретать «Stage для X» оборот. (3) **3-х батчевая стратегия openpipeline-семьи 39** идёт по плану: 14a (ingest-sources 13 ✅) + 14b (pipelines 13 ✅) + **14c (data-forwarding 13 next)**. После 14a/b/c остаются appsec-notification-{alerting-profile,attack-alerting-profile,integration} + builtin-problem-notifications 20-30KB. Остаток builtin 20/307 (7%). **Prev L4-AG.1a.14a batch 13 builtin openpipeline-ingest-sources 18.2-18.4KB ЗАКРЫТ** (logs/spans/events/metrics/bizevents/events-sdlc/user-events/davis-events/usersessions/system-events/davis-problems/events-security/security-events = ingest-sources sub-family). Build [`scripts/_build_schemas_l4ag1a14a.py`](scripts/_build_schemas_l4ag1a14a.py) расширяет L4-AG.1a.13 канон: DISPLAY_NAME 13, SCHEMA_DESC 1 (один на семейство), PARAM_LABEL ~80, PARAM_DESC 2. **Канон pipeline-groups (L4-AG.1a.6) повторно применён к ingest-sources:** общий SCHEMA_DESC «Содержит конфигурацию ingest sources» + 13 уникальных DISPLAY_NAME с kind в скобках; (logs/events/metrics) → (логи/события/метрики), остальные (bizevents/usersessions/spans/events.sdlc/user.events/davis.events/system.events/davis.problems/events.security/security.events) = EN-термины Dynatrace либо API-имена с точкой. **Mojibake-аудит EN ДО билда:** BOM 0/13, single 0/13, triple-apos/em/en/nbh/lq/rq 0/13, double-B 0/13, double-decoded WARN 0/13, mojibake-BOM `ï»¿` 13/13 (1 на файл, внутри hyperlink-текста `[See our documentation]ï»¿`), чистится `_normalize`. Самый лёгкий батч по mojibake. **Verification:** line-parity 13/13 EXACT (351 строк/файл, identical structure ingest-sources × 13 kinds), em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`/`## Parameters`-leftover 0, calque `, и `/`, или ` 0, signal-words (Alert if/Choose whether/Note that) 0, single-a leftover 0, double-B 0. **2 деф пойманы spot-check ДО публикации:** (1) `[See our documentation﻿](...)` STRUCT key содержал BOMJ, который `_normalize` удалил ДО STRUCT replace — ключ не матчился, ссылка оставалась EN. Фикс: ключ STRUCT без BOMJ (mojibake-BOM съедается до пасса, канон L4-AG.1a.7). (2) **Несогласованность PARAM_LABEL:** `Source Type` (top-level) был оставлен EN, при этом `Source type` (вложенный в SmartscapeEdgeAttributes, маленькая `t`) переведён как «Тип source». Унифицировано — оба → «Тип source». Spot-check 4 разных kind-файла (bizevents/davis-problems/usersessions/security-events) heading + 5 SmartscapeNodeAttributes/Edge/CostAllocation = **0 семантических деф**. **Lessons L4-AG.1a.14a:** (1) **Sub-family из 13 идентичных файлов** (ingest-sources × 13 kinds) повторяет паттерн pipeline-groups (L4-AG.1a.6): один SCHEMA_DESC + 13 уникальных DISPLAY_NAME, общий PARAM_LABEL/PARAM_DESC покрывает все 13 файлов одним dict-проходом. Идеальная консолидация. (2) **STRUCT keys должны быть в форме ПОСЛЕ `_normalize`** — повтор урока L4-AG.1a.7 lesson 2: mojibake-BOM в ключе ломает replace. Канон: ВСЕ ключи замены (SCHEMA_DESC/STRUCT/PARAM_LABEL/PARAM_DESC) пишутся без `ï»¿`/BOMJ-байтов. (3) **PARAM_LABEL согласованность top-level vs nested:** одинаковые названия с разным регистром (`Source Type` vs `Source type`) должны переводиться единообразно — иначе spot-check находит EN-leftover. Канон: при добавлении PARAM_LABEL проверять оба регистра (`X type` ↔ `X Type`). (4) **3-х батчевая стратегия для openpipeline-семьи 39 файлов:** разбить на 14a (ingest-sources 13) + 14b (pipelines 13) + 14c (data-forwarding 13) — каждый под-батч консолидируется в идеальную семью, общий канон переносится. **Next L4-AG.1a.14b** 13 builtin-openpipeline-*-pipelines.md (18.5-18.6KB, idential sub-family) + L4-AG.1a.14c 13 builtin-openpipeline-*-data-forwarding.md (18.9-19.0KB). После 14a/b/c остаются appsec-notification-{alerting-profile,attack-alerting-profile,integration} + builtin-problem-notifications 20-30KB. Остаток builtin 33/307 (11%). **Prev L4-AG.1a.13 batch 14 builtin schema-table 7.5-11.3KB ЗАКРЫТ** (alerting-{maintenance-window,profile}, anomaly-detection-infrastructure-{aws,vmware}, anomaly-detection-kubernetes-workload, failure-detection-rulesets, monitoredentities-generic-type, process-{built-in-process-monitoring-rule,group-detection-flags,grouping-rules}, service-detection-{external,full}-web-{request,service} = 4 service-detection файла). Build [`scripts/_build_schemas_l4ag1a13.py`](scripts/_build_schemas_l4ag1a13.py) расширяет L4-AG.1a.12 канон: DISPLAY_NAME 14, SCHEMA_DESC ~17, PARAM_LABEL ~155, PARAM_DESC ~80; добавлена отдельная regex-функция `_process_rule_row` для process-built-in-process-monitoring-rule (80 параметров вида «Do (not )?monitor processes if X `-N`» + «Rule id: N»). **Mojibake-аудит EN ДО билда:** BOM 0/14, single_a_real 0/14, **triple-en-dash `–` (c3 a2 c2 80 c2 93) 4/14** только process-grouping-rules ($contains/$eq/$prefix/$suffix bullet-separator), никаких apos/em/nbh/lq/rq/double-B/WARN. mojibake-BOM `ï»¿` 21 вхождение в 10/14 файлов внутри hyperlink-текстов, чистится `_normalize` (канон L4-AG.1a.7), ключи SCHEMA_DESC БЕЗ BOMJ. **Twin-quad pair 4 service-detection файла** (external-web-request, external-web-service, full-web-request, full-web-service) консолидируют общие nested: condition, serviceIdContributor, transformationSet, contextRoot, contextIdContributor, valueOverride, transformation, reducedTransformation, publicDomainTransformationSet. Уникальные SCHEMA_DESC: external-web-request — `**All of the Contributors except for the port are always applied.**`, остальные 3 — `**All of the Contributors are always applied.**`. **Verification:** line-parity 14/14 EXACT (52-210 строк/файл), em-dash 0 (после фикса 3 деф), BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`/`## Parameters`-leftover 0, calque `, и `/`, или ` 5 = **все 5 false positives** (failure-detection-rulesets line 15 закрытие причастного оборота, monitoredentities lines 43+49 сложносочинённое, process-group-detection-flags line 39 запятая перед однородным определением). **5 деф пойманы review+spot-check в фикс-итерациях ДО публикации:** (1) em-dash в моём переводе monitoredentities-generic-type PARAM_DESC «Ключ атрибута — это уникальное имя» → «Ключ атрибута, это уникальное имя» (CLAUDE.md #0). (2) em-dash в моём переводе service-detection-full-web-{request,service} contextIdContributor PARAM_DESC «Context root — это первый сегмент» → «Context root, это первый сегмент» (одновременный фикс twin pair). (3) **alerting-profile MetadataFilter PARAM_DESC `Define filters for event properties. A maximum of 20 properties is allowed.` не транслировался** — empty-label row (col-1 = `metadataFilterItems` в backticks без подписи), `_param_row` справился, но PARAM_DESC ключа не было; добавил. (4) **17 длинных EN-labels в process-group-detection-flags** не были в PARAM_LABEL (Ignore versions, Use CATALINA\\_BASE, Automatically detect Cassandra clusters etc.) → `_param_row` возвращал None → строки целиком оставались EN. Фикс: добавил все 17 labels в PARAM_LABEL. (5) **process-built-in-process-monitoring-rule** 80+ параметров с уникальными labels вида «Do (not )?monitor processes if X `-N`» + «Rule id: N» обработан через отдельную regex-функцию `_process_rule_row` + словарь `PROCESS_RULE_HEAD` (2 формы) + список `PROCESS_RULE_TAIL_TOKENS` (21 паттерн EXE/Node.js/Kubernetes/Cloud Foundry/Docker/JAR/EXE path). **Spot-check 8 файлов** (alerting-maintenance-window 8 nested Schedule/Filter/Once-/Daily-/Weekly-/MonthlyRecurrence/TimeWindow/RecurrenceRange, alerting-profile MetadataFilter empty-label fix, anomaly-detection-kubernetes-workload 14 nested object'ов с 9 *Config-объектами «там есть пороги»/«в течение последних», process-built-in-process-monitoring-rule 80 regex-переведённых строк, process-group-detection-flags 17 длинных labels fix, process-grouping-rules triple-en-dash 4 в DetectionCondition bullet-list, service-detection-external-web-request twin-quad pair head с idContributorsType+condition+serviceIdContributor+transformationSet, failure-detection-rulesets 8 nested override/customRule/singleException): **0 семантических деф**. **Lessons L4-AG.1a.13:** (1) **Empty-label rows + длинные labels = двойной риск**: `_param_row` пропускает row только если `label and label not in PARAM_LABEL` ложно (т.е. label пустой ИЛИ в dict). Если label длинный и не в dict — return None и строка остаётся EN целиком. Spot-check + grep EN-signal-words критичен после auto-review «0 issues». (2) **Regex-функция для repeated label patterns** (process-built-in-process-monitoring-rule: 80 параметров с одинаковой структурой «Do (not )?monitor processes if X `-N`») — намного эффективнее 80 ключей в PARAM_LABEL; вынести в `_process_rule_row` с PROCESS_RULE_HEAD (2 формы) + PROCESS_RULE_TAIL_TOKENS (21 паттерн EXE/Node.js/etc.) + rest tail. Канон recommend: специальные большие repeated-pattern файлы заслуживают своей regex-функции. (3) **Twin-quad pair 4 файла** (4 service-detection файла) — больше чем twin pair, меньше чем семья: общие nested (condition/serviceIdContributor/transformationSet/contextRoot/...) дают максимальную консолидацию, уникальные только SCHEMA_DESC + Schema ID + некоторые поля idContributorsType. (4) **Лёгкий mojibake-батч 3 раза подряд** (L4-AG.1a.10 triple-apos 3, L4-AG.1a.12 double-B 2, L4-AG.1a.13 triple-en-dash 4) после тяжёлых L4-AG.1a.7-9-11. Большие батчи могут содержать только 1 тип mojibake — не предугадывать весь зоопарк. **Next L4-AG.1a.14** ~12-19KB openpipeline-семьи (3×12=36 файлов: ingest-sources/pipelines/data-forwarding) + appsec-notification-integration/problem-notifications 20-30KB. Остаток builtin 46/307 (15%). **Prev L4-AG.1a.12 batch 10 builtin schema-table 2.4-9.0KB ЗАКРЫТ** (anomaly-detection-metric-events, anomaly-detection-rum-mobile, anomaly-detection-rum-custom, anomaly-detection-services, anomaly-detection-databases, anomaly-detection-rum-web + cleanup 4 файла 2.3-2.4KB: synthetic-http-performance-thresholds, logmonitoring-schemaless-log-metric, rum-web-resource-cleanup-rules, devobs-sensitive-data-masking). Build [`scripts/_build_schemas_l4ag1a12.py`](scripts/_build_schemas_l4ag1a12.py) расширяет L4-AG.1a.11 канон: DISPLAY_NAME 10, SCHEMA_DESC ~14, PARAM_LABEL ~110, PARAM_DESC ~30. **Mojibake-аудит EN ДО билда:** BOM 0/10, single 0/10, triple-apos/em/en/nbh/lq/rq 0/10 (лёгкий батч), **double-B `DavisÂ®` 2/10** (metric-events line 79 `DavisÂ® AI` + logmonitoring-schemaless-log-metric line 15 `DavisÂ® data units`; константа `DB_R = chr(0xC2)+chr(0xAE)` инлайн-конкатенация в ключе). mojibake-BOM `ï»¿` 11 вхождений в 8/10 файлов внутри hyperlink-текстов (`[automated anomaly detection](https://...)`), чистится `_normalize` (канон L4-AG.1a.7), ключи SCHEMA_DESC БЕЗ BOMJ. **Twin pair rum-mobile ↔ rum-custom:** 99% идентичны — общий SCHEMA_DESC (2 параграфа), общие 11 nested object'ов (ErrorRateIncrease/SlowUserActions/UnexpectedLowLoad/UnexpectedHighLoad/4 Auto/4 Manual), идентичные PARAM_LABEL/PARAM_DESC; отличаются ТОЛЬКО DISPLAY_NAME (mobile vs custom) и Scope-таблица (MOBILE_APPLICATION vs CUSTOM_APPLICATION). Twin pair services ↔ databases: общие responseTime/failureRate/loadDrops/loadSpikes nested + общие PARAM_LABEL/PARAM_DESC; databases добавляет nested `databaseConnections` (3 поля). **Verification:** line-parity 10/10 EXACT (38-154 строк/файл), em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`/`## Parameters`-leftover 0, calque `, и `/`, или ` 0, single-A 0. **1 деф пойман EN-leftover detector ДО публикации:** rum-web строка 80 `Alert if the median response time of all user actions...` не транслировался — мой PARAM_DESC содержал только версию `of all REQUESTS` для services/databases. Фикс: добавил отдельный ключ `Alert if the median response time of all user actions degrades beyond **both** the absolute and relative thresholds:` для rum-web (там действительно `user actions`, не `requests`). **Spot-check 8 файлов** (metric-events 7 nested object'ов с EventTemplate/EntityFilter/MetadataItem + `DavisÂ®` mojibake-проверка, rum-mobile twin pair head, services twin pair head, databases nested databaseConnections, devobs-masking 3 enum-prefix Choose/Select подсказки, synthetic-http-perf-thresholds минимальный ThresholdEntry, logmonitoring-schemaless DavisÂ® в SCHEMA_DESC, rum-web-resource-cleanup-rules 3 `Например:` примера-регулярки): **0 семантических деф**. **Lessons L4-AG.1a.12:** (1) **Twin pair 99%-идентичных файлов** (rum-mobile ↔ rum-custom) даёт максимальную консолидацию: 1 SCHEMA_DESC + 1 PARAM_LABEL/PARAM_DESC покрывают оба файла одним dict-проходом — единственное различие в card-блоке (Schema ID + Scope). (2) **Двойной пробел в EN-параграфах** (`one week.  Depending on this expected value`) — в rum-web и databases встречается `.  ` (period + 2 spaces), отличается от rum-mobile/custom (`one week. Depending on this`). Нужны ОТДЕЛЬНЫЕ ключи PARAM_DESC для каждой вариации иначе матч не сработает. (3) **EN-leftover detector по signal-словам** (Alert if, Dynatrace learns, Choose whether...) после auto-review «0 issues» поймал 1 деф который пропустил линт. Spot-check + signal-word grep = belt-and-suspenders. (4) **Лёгкий mojibake-батч 2/3 раза подряд** (L4-AG.1a.10 triple-apos 3, L4-AG.1a.12 только double-B 2) после тяжёлого L4-AG.1a.11 (8 типов одновременно). Каждый батч может выявить новый тип ИЛИ оказаться чистым — расширять константы лениво, не предугадывая. **Next L4-AG.1a.13** ~10-15 builtin 9-12KB остаток (anomaly-detection-infrastructure-aws/vmware, alerting-maintenance-window, alerting-profile, process-detection-flags/grouping-rules, service-detection-{external,full}-web-{request,service}, anomaly-detection-kubernetes-workload, monitoredentities-generic-type, failure-detection-rulesets, process-built-in-process-monitoring-rule) — после остаются 12-19KB openpipeline-семьи (3×12=36 файлов: ingest-sources/pipelines/data-forwarding) и appsec-notification-integration/problem-notifications 20-30KB. Остаток builtin 60/307 (20%). **Prev L4-AG.1a.11 batch 8 builtin schema-table 6.05-6.81KB ЗАКРЫТ** (ownership-teams, anomaly-detection-kubernetes-node, anomaly-detection-kubernetes-namespace, elasticsearch-user-session-export-settings-v2, preferences-privacy, process-group-cloud-application-workload-detection, processavailability, failure-detection-environment-parameters). Build `scripts/_build_schemas_l4ag1a11.py` расширяет L4-AG.1a.10: DISPLAY_NAME 8, SCHEMA_DESC ~19, PARAM_LABEL ~115, PARAM_DESC ~38. Mojibake-аудит EN: BOM 0/8, single 7/8 (oба triple-mojibake седьмого+восьмого типов при hex-проверке), triple-apos 1, triple-en-dash 12 (processavailability, самый массовый файл), triple-em-dash `—` 1 (новый седьмой тип, ownership-teams), triple-quotes `"…"` 6 (новый восьмой тип, process-group-cloud-application). Константы `TM_EMDASH = chr(0xE2)+chr(0x80)+chr(0x94)`, `TM_LQUOTE`/`TM_RQUOTE` = U+201C/U+201D. Line-parity 8/8 EXACT, 0 EN-leftover после фикса. **Prev L4-AG.1a.10 batch 15 builtin schema-table 4.76-5.80KB ЗАКРЫТ** (rum-mobile-enablement, rum-web-app-detection, rum-web-manual-insertion, monitoredentities-generic-relation, rpc-based-sampling, opentelemetry-metrics, url-based-sampling, deployment-management-update-windows, process-custom-process-monitoring-rule, failure-detection-service-general-parameters, appsec-runtime-vulnerability-detection, anomaly-detection-kubernetes-cluster, sessionreplay-web-privacy-preferences, process-group-advanced-detection-rule, anomaly-detection-infrastructure-disks-per-disk-override). Build [`scripts/_build_schemas_l4ag1a10.py`](scripts/_build_schemas_l4ag1a10.py) расширяет L4-AG.1a.9: DISPLAY_NAME 15, SCHEMA_DESC ~40, PARAM_LABEL ~130, PARAM_DESC ~55. **Mojibake-аудит EN ДО билда:** BOM 0/15, single 0/15, triple-apos 3/15 = rum-mobile-enablement (`application's`+`there's`) + process-custom-process-monitoring-rule (`don't`). Никаких triple-en-dash/triple-nbhyphen/double-B/double-decoded WARN/single-â. mojibake-BOM `ï»¿` встречается внутри hyperlink-текстов нескольких файлов, чистится `_normalize` (канон L4-AG.1a.7). Line-parity 15/15 EXACT (47-113 строк/файл), em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`-leftover 0, calque `, и `/`, или ` 0. **Spot-check 7 файлов** (rum-mobile-enablement triple-apos в costAndTrafficControl + experienceAnalytics, rum-web-app-detection с большим примером URL-правил, rpc-based-sampling twin к url-based-sampling, deployment-management-update-windows 8 nested object'ов с recurrence-таблицами, anomaly-detection-kubernetes-cluster 10 nested object'ов с lowercase-фрагментами «кластер не готов», sessionreplay-web-privacy-preferences AllowList/BlockList twin, opentelemetry-metrics 2 mega-PARAM_DESC с Markdown bullet-комбо): **0 семантических деф**. **Twin pair rpc-based-sampling ↔ url-based-sampling:** общие PARAM_LABEL (`factor`, `Enabled`, sampling-rate prose), уникальные SCHEMA_DESC (RPC vs HTTP), уникальные «Specify the RPC ...»/«Specify the URL path ...». Twin pair sessionreplay AllowListRule ↔ BlockListRule полностью идентичен кроме `hideUserInteraction` (только в BlockList). **Lessons L4-AG.1a.10:** (1) **Лёгкий mojibake-батч** (только triple-apos в 3/15 файлах) после тяжёлых L4-AG.1a.7-9 — нормально, не каждый батч содержит весь зоопарк типов; (2) **Twin pair с уникальными SCHEMA_DESC** (RPC vs HTTP) — менее консолидируется чем openpipeline-routing 12 в L4-AG.1a.4, но PARAM-табличный канон twin'ов работает на любых семьях; (3) **8 nested object'ов в deployment-management-update-windows** = `_param_row` справляется с пустыми label-описаниями (-) для большинства строк, переводится только label; (4) **lowercase-фрагменты в anomaly-detection-kubernetes-cluster** (PodsSaturationConfig + 4 близнеца) корректно работают с обычным PARAM_LABEL словарём, начало предложения формируется через «Оповестить, если» + lowercase-фрагмент. **Next: L4-AG.1a.11** ~10-20 builtin 5.8-7.0KB остаток. Остаток builtin 78/307 (25%). Канон+история в TRANSLATION_PROGRESS.md header+Status (memory=указатель). **Prev L4-AG.1a.9 batch 12 builtin schema-table 3.76-4.43KB ЗАКРЫТ** (monitoring-slo, rum-web-enablement, service-detection-v2-for-oneagent, custom-metrics, synthetic-multiprotocol-config, user-action-custom-metrics, metric-metadata, declarativegrouping, rum-web-automatic-injection, anomaly-detection-infrastructure-disks, logmonitoring-log-agent-configuration, url-path-pattern-matching-rules). Build [`scripts/_build_schemas_l4ag1a9.py`](scripts/_build_schemas_l4ag1a9.py) расширяет L4-AG.1a.8: DISPLAY_NAME 12, SCHEMA_DESC ~18, PARAM_LABEL ~95, PARAM_DESC ~45. **Mojibake-аудит EN ДО билда (single/triple-apos/triple-endash/triple-nbhyphen/double-B + mojibake-BOM `ï»¿`):** BOM 0/12, single 0/12, **triple-apostrophe `'` (U+2019, bytes c3 a2 c2 80 c2 99)** 5/12 = monitoring-slo (`organizationâ€™s` ×1) + rum-web-enablement (`thereâ€™s` ×1) + service-detection-v2-for-oneagent (`opt-inâ€™s` ×3), **triple-en-dash `–` (U+2013, bytes c3 a2 c2 80 c2 93)** 4/12 = declarativegrouping (`$contains(svc) â€“ Matches` ×4 как bullet-separator), **triple-non-breaking-hyphen `‑` (U+2011, bytes c3 a2 c2 80 c2 91)** 6/12 = url-path-pattern-matching-rules (`lowâ€‘volatility`, `asâ€‘is`, `Catchâ€‘all`, `Nonâ€‘matches`, `highâ€‘cardinality`, `catchâ€‘alls`). double-B 0/12, mojibake-BOM `ï»¿` присутствует во многих файлах (съедается `_normalize`, ключи БЕЗ BOMJ по канону L4-AG.1a.7). Line-parity 12/12 EXACT, em-dash 0 (после фикса), BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`-leftover 0. **Review-скрипт [`scripts/_review_schemas_l4ag1a9.py`](scripts/_review_schemas_l4ag1a9.py)** 0 issues после фикса (3 типа triple-mojibake считаются раздельно). **2 дефа пойманы review ДО публикации:** (1) em-dash в моём переводе custom-metrics + user-action-custom-metrics строка 44 «Dimension — это набор» → «Dimension, это набор» (CLAUDE.md #0, twin pair фикс одновременно). (2) **2 новых типа triple-mojibake** пойманы review через `single_a leftover` heuristic — изначально я закодировал ключи через одиночный chr(0xE2), но hex-dump показал triple-en-dash (`c3 a2 c2 80 c2 93`) в declarativegrouping и triple-nbhyphen (`c3 a2 c2 80 c2 91`) в url-path-pattern; константы `TM_ENDASH` и `TM_NBHYPHEN` через `chr(0xE2)+chr(0x80)+chr(0x93)`/`chr(0xE2)+chr(0x80)+chr(0x91)` (L4-AG.1a.4 канон продлён). **Twin pair custom-metrics ↔ user-action-custom-metrics:** общие PARAM_LABEL/MetricValue/Filter nested; уникальные SCHEMA_DESC и PARAM_DESC из-за "user session" vs "user action" в тексте (не консолидируется до единого SCHEMA_DESC как mobile↔custom crash-rate, более «братская» чем «близнецовая»). Spot-check 6 файлов (declarativegrouping bullet-list с 4× triple-endash, url-path-pattern-matching-rules HUGE single-PARAM_DESC с 6× triple-nbhyphen + Markdown syntax описание, monitoring-slo nested ErrorBudgetBurnRate, service-detection-v2 3× идентичный SCHEMA_DESC с triple-apos, anomaly-detection-infrastructure-disks 8 nested object'ов, synthetic-multiprotocol-config 4 nested Step/Property/Constraint/RequestConfiguration с 5× «Option not supported yet», metric-metadata enum-prefix valueType с score/error разъяснением): 0 семантических деф. **Lessons L4-AG.1a.9:** (1) **Triple-mojibake пятый и шестой типы** после single (c3 a2), triple-apostrophe (c3 a2 c2 80 c2 99), double-B `®` (c3 82 c2 ae), double-decoded ⚠️ (c3 a2 c2 9a c2 a0 c3 af c2 b8 c2 8f) — теперь добавились triple-en-dash `–` (c3 a2 c2 80 c2 93) и triple-non-breaking-hyphen `‑` (c3 a2 c2 80 c2 91). Канон L4-AG.1a.4 через chr() конкатенацию применим к ЛЮБОМУ Unicode-символу из U+2010-U+2020 диапазона типографики. (2) **`single_a leftover` heuristic в review-скрипте** ловит ВСЕ типы triple-mojibake (потому что все они начинаются с c3 a2) — это полезный sentinel для «есть ещё какие-то typographic byte sequences, которые мы не учли». (3) **Twin pair с уникальными SCHEMA_DESC** (custom-metrics ↔ user-action-custom-metrics из-за "session" vs "action") — менее консолидируется чем mobile↔custom crash-rate из L4-AG.1a.8 (там SCHEMA_DESC идентичен), но всё равно общий PARAM_LABEL/Filter/MetricValue nested = экономия. (4) **Big single-PARAM_DESC файл (~3KB в одной cell)** url-path-pattern-matching-rules — `_param_row` справляется (cells через ` | `, не ` | ` внутри cdesc), но требует точного матча в PARAM_DESC ключе; spot-check критичен. **Next: L4-AG.1a.10** ~10-15 builtin 4.65-5.5KB (rum-mobile-enablement, rum-web-app-detection, rum-web-manual-insertion, monitoredentities-generic-relation, rpc-based-sampling, opentelemetry-metrics, url-based-sampling, deployment-management-update-windows, process-custom-process-monitoring-rule, failure-detection-service-general-parameters, appsec-runtime-vulnerability-detection, anomaly-detection-kubernetes-cluster, sessionreplay-web-privacy-preferences). Остаток builtin 93/307 (30%). Канон+история в TRANSLATION_PROGRESS.md header+Status (memory=указатель). **Prev L4-AG.1a.8 batch 9 builtin schema-table 3.8-4.1KB ЗАКРЫТ** (kubernetes-generic-metadata-enrichment, appsec-third-party-vulnerability-kubernetes-label-rule-settings, logmonitoring-timestamp-configuration, davis-anomaly-detectors, anomaly-detection-rum-mobile-crash-rate-increase, logmonitoring-custom-log-source-settings, anomaly-detection-rum-custom-crash-rate-increase, container-built-in-monitoring-rule, cloud-kubernetes-monitoring). Build [`scripts/_build_schemas_l4ag1a8.py`](scripts/_build_schemas_l4ag1a8.py) расширяет L4-AG.1a.7: DISPLAY_NAME 9, SCHEMA_DESC ~16, PARAM_LABEL ~70, PARAM_DESC ~40. Mojibake-аудит EN ДО билда: BOM-real 0/9, single 0/9, triple 0/9 (3 triple-mojibake файла — monitoring-slo / rum-web-enablement / service-detection-v2-for-oneagent — намеренно отложены в следующий батч под отдельный chr()-маппинг по канону L4-AG.1a.4), double-B 0/9, mojibake-BOM `ï»¿` присутствует в kubernetes-generic-metadata-enrichment (2) + anomaly-detection-rum-mobile-crash-rate-increase (1) + anomaly-detection-rum-custom-crash-rate-increase (1) + cloud-kubernetes-monitoring (5) — все съедены `_normalize` (канон L4-AG.1a.7), ключи SCHEMA_DESC/PARAM_DESC БЕЗ BOMJ. Line-parity 9/9 EXACT, em-dash 0 (после фикса), BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`-leftover 0. **Review-скрипт [`scripts/_review_schemas_l4ag1a8.py`](scripts/_review_schemas_l4ag1a8.py)** 0 issues после фикса. **1 деф пойман auto-review (em-dash в моём собственном переводе) ДО публикации:** logmonitoring-custom-log-source-settings строка 71 PARAM_DESC «${N} ... wildcard, где N — номер wildcard...» (длинное тире после «N») → «${N} ... wildcard; здесь N означает номер wildcard...» (CLAUDE.md #0). **Twin-семья rum-{mobile,custom}-crash-rate-increase 2 файла** (anomaly-detection-rum-mobile-crash-rate-increase + anomaly-detection-rum-custom-crash-rate-increase) идентичны кроме DISPLAY_NAME и Scope — общие SCHEMA_DESC + PARAM_LABEL + PARAM_DESC + 3 nested object'а (CrashRateIncrease/Auto/Fixed) консолидированы одним dict-проходом. Spot-check 4 файлов (kubernetes-generic-metadata-enrichment мега-PARAM_DESC с bullet'ами + Kubernetes-syntax prose, cloud-kubernetes-monitoring большие license-prose в каждом PARAM_DESC, davis-anomaly-detectors 5 nested object'ов, anomaly-detection-rum-mobile-crash-rate-increase twin-семья): 0 семантических деф. **Lessons L4-AG.1a.8:** (1) **Twin-семья 2-3 файлов** (mobile↔custom crash-rate-increase, как openpipeline-routing L4-AG.1a.4 12 файлов или openpipeline-pipeline-groups L4-AG.1a.6 12 файлов) идеально консолидируется через общие SCHEMA_DESC+PARAM_LABEL+PARAM_DESC; уникальные только DISPLAY_NAME и Scope в card-блоке. (2) **Auto-review em-dash в МОЁМ переводе** — повтор урока L4-AG.1a.5 lesson 2; em-dash check полезен и при «no-em-dash» правиле CLAUDE.md (после первого фикса остался ВТОРОЙ em-dash в той же строке через «N — номер», нужно прогонять review повторно до 0 issues). (3) **Triple-mojibake файлы можно намеренно отложить в следующий батч** для отдельного chr()-маппинга — упрощает текущий батч (никто не обязан тащить все размеры сразу). (4) **5 файлов с mojibake-BOM `ï»¿`** в cloud-kubernetes-monitoring (только PARAM_DESC под Prometheus/license/events documentation-ссылки) — `_normalize` чистит без вмешательства, ключи в форме ПОСЛЕ нормализации (канон L4-AG.1a.7). **Prev L4-AG.1a.7 batch 10 builtin schema-table 3.5-3.8KB ЗАКРЫТ** (hyperscaler-authentication-connections-azure, disk-options, mainframe-txmonitoring, rum-web-key-performance-metric-load-actions, container-technology, oneagent-side-masking-settings, anomaly-detection-kubernetes-pvc, appsec-code-level-vulnerability-rule-settings, appsec-third-party-vulnerability-rule-settings, failure-detection-service-http-parameters). Build [`scripts/_build_schemas_l4ag1a7.py`](scripts/_build_schemas_l4ag1a7.py) расширяет L4-AG.1a.6 (реюз `_normalize`/`_heading`/`_param_row`/`_nested_heading`): DISPLAY_NAME 10, SCHEMA_DESC ~16, PARAM_LABEL ~60, PARAM_DESC ~30. Mojibake-аудит EN ДО билда (single/triple/double-B + mojibake-BOM `ï»¿`): BOM-real 0/10, **single 8** (disk-options 4 + declarativegrouping вне батча 4), **triple 0/10**, double-B 0/10, **mojibake-BOM `ï»¿` 5/10** (rum-web-kpm-load-actions / container-technology / oneagent-side-masking / anomaly-detection-kubernetes-pvc / failure-detection-service-http-parameters — embedded inside hyperlink texts). Line-parity 10/10 EXACT, em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`-leftover 0. **Review-скрипт [`scripts/_review_schemas_l4ag1a7.py`](scripts/_review_schemas_l4ag1a7.py)** повторяет канон L4-AG.1a.6 + проверка mojibake-BOM drift + calque `, и ` / `, или `. **0 issues** (review-скрипт clean, после фикса). **2 дефа пойманы spot-check'ом, фикс-итерация ДО публикации:** (1) **WARN-emoji в disk-options был неверной длины:** видимое `â ï¸` в IDE/cat = 6 chars (12 bytes) `c3 a2 c2 9a c2 a0 c3 af c2 b8 c2 8f`, double-decoded ⚠️ (U+26A0 U+FE0F). Моя константа `WARN = "â ï¸"` = 4 chars и не матчилась с EN-cdesc. Фикс: `WARN = chr(0xE2)+chr(0x9A)+chr(0xA0)+chr(0xEF)+chr(0xB8)+chr(0x8F)` (lesson L4-AG.1a.4 canon продлён под double-decoded emoji). (2) **`_normalize` чистит mojibake-BOM ВЕЗДЕ (не только в начале файла):** мои SCHEMA_DESC ключи с `+ BOMJ +` теряли матч после нормализации → 4 файла оставались с EN-параграфом (container-technology «Dynatrace OneAgent automatically monitors...» 17 строка, oneagent-side-masking «A detailed reference...», anomaly-detection-kubernetes-pvc, failure-detection-service-http-parameters). Фикс: ключи SCHEMA_DESC БЕЗ `BOMJ` (mojibake-BOM съедается до пасса), RU-перевод тоже без `ï»¿`. **Lessons L4-AG.1a.7:** (1) **Double-decoded emoji** (⚠️ → 6-char visible `â ï¸`) — четвёртый тип mojibake после single/triple/double-B; видимый размер ≠ байтовый, использовать hex-dump + `chr()` конкатенацию по канону L4-AG.1a.4. (2) **`_normalize` агрессивно вычищает mojibake-BOM в любой позиции файла** (не только startswith) — ключи SCHEMA_DESC/PARAM_DESC должны быть в форме ПОСЛЕ `_normalize`, иначе матч не сработает. Канон: не вставлять `\xef\xbb\xbf` в ключи замены. (3) **Spot-check ОБЯЗАТЕЛЕН после auto-review «OK»** — review-script проверял mojibake-drift count, em-dash, struct, calque, но не EN-leftover целого параграфа в schema-description (то же урок что L4-AG.1a.4 lesson 4: повторяемая дыра). 4 EN-параграфа были видны ТОЛЬКО при чтении RU-файла глазами. (4) **`_normalize` поведение задокументировать в шапке билдера** — будущие батчи с mojibake-BOM не повторят регресс. **Prev L4-AG.1a.6 batch 37 builtin schema-table 3.0-3.5KB ЗАКРЫТ** (process-visibility, span-context-propagation, synthetic-http-advanced-execution, rum-provider-breakdown, process-process-monitoring, span-attribute, hyperscaler-authentication-connections-aws, logmonitoring-sensitive-data-masking-settings, cloud-kubernetes, span-event-attribute, rum-web-request-errors, openpipeline-{logs,spans,events,metrics,bizevents,events-sdlc,user-events,davis-events,usersessions,system-events,davis-problems,events-security,security-events}-pipeline-groups = 12 файлов pipeline-groups семьи, ibmmq-queue-managers, synthetic-multiprotocol-performance-thresholds, issue-tracking-integration, endpoint-detection-rules, logmonitoring-log-events, logmonitoring-log-storage-settings, logmonitoring-log-agent-feature-flags, anomaly-detection-disk-rules, rum-ip-mappings, service-detection-rules, rum-web-key-performance-metric-xhr-actions, failure-detection-environment-rules, resource-attribute). Build [`scripts/_build_schemas_l4ag1a6.py`](scripts/_build_schemas_l4ag1a6.py) расширяет L4-AG.1a.5 (реюз `_normalize`/`_heading`/`_param_row` с empty-label support / dual-marker enum / `_nested_heading` regex): DISPLAY_NAME 37, SCHEMA_DESC ~50, PARAM_LABEL ~115, PARAM_DESC ~35. **Семья openpipeline-*-pipeline-groups 12 файлов** идентично консолидируется: 1 общий SCHEMA_DESC «Содержит конфигурацию pipeline group» + 12 уникальных DISPLAY_NAME с (kind) в скобках + общий StageConfig + PipelineGroupComposition nested на 12. **Mojibake-аудит EN ДО билда** (single `\xc3\xa2` / triple `\xc3\xa2\xc2\x80\xc2\x99` / double-B `\xc3\x82\xc2\xae`): BOM 0/37, single 1/37 (process-process-monitoring `thatâ€™s` = triple, посчитан и как single), **triple 1/37** (process-process-monitoring строка 33 `inclusion rule thatâ€™s followed`), **double-B 2/37** (logmonitoring-log-events `DavisÂ®` ×2 в SCHEMA_DESC и в PARAM_DESC; ключи через `chr(0xC2)+chr(0xAE)` конкатенацию по L4-AG.1a.4/5 канону). Line-parity 37/37 EXACT, em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`-leftover 0. **Review-скрипт [`scripts/_review_schemas_l4ag1a6.py`](scripts/_review_schemas_l4ag1a6.py)** повторяет канон L4-AG.1a.5 + проверка mojibake-count drift EN vs RU + calque `, и ` / `, или `. 5 issues — **все false positives:** (1) mojibake drift в process-process-monitoring (EN-параграф полностью заменён на RU, mojibake-apostrophe не нужен в RU-эквиваленте); (2-3-4) `, и ` в process-visibility/endpoint-detection-rules/service-detection-rules — закрытие причастного оборота или сложносочинённое предложение, правильная русская пунктуация, не calque «A, B, и C» из 3+ элементов. Mojibake-drift в review — допустимое поведение когда EN-param с mojibake переводится в RU-эквивалент без apostrophe. **Spot-check 8 файлов** (process-visibility tri-mojibake-adjacent prose, process-process-monitoring triple-mojibake в deep monitoring параграфе, span-attribute deprecation + Masking enum-prefix твин с resource-attribute/span-event-attribute, cloud-kubernetes Bearer-token+endpointUrl, openpipeline-logs-pipeline-groups family head, openpipeline-security-events-pipeline-groups family tail (Pipeline Groups configuration (security.events)), logmonitoring-log-events double-B mojibake `DavisÂ®` ×2, failure-detection-environment-rules 21-enum serviceType cell): **0 семантических деф**. **Lessons L4-AG.1a.6:** (1) **Mojibake-drift в EN→RU не баг**, когда EN-параграф целиком заменён через SCHEMA_DESC/PARAM_DESC на RU-эквивалент без apostrophe — mojibake-байты остаются только в EN-исходнике; review должен учитывать это как ожидаемое поведение. (2) **Семья из 12 одинаковых pipeline-groups файлов** (как openpipeline-routing в L4-AG.1a.4) идеально консолидируется через 1 SCHEMA_DESC + 12 DISPLAY_NAME — паттерн повторяемый и для будущих семей. (3) **Double-B mojibake `Â®`** (bytes `\xc3\x82\xc2\xae`) — третий тип mojibake после single/triple; через `chr(0xC2)+chr(0xAE)` конкатенацию в исходнике dict-ключа. Распознан hex-dump'ом EN-файла. (4) **Calque-проверка `, и ` / `, или `** даёт false positives для закрытия причастного оборота и сложносочинённых предложений — нужно фильтровать только перечисления из 3+ элементов («X, Y, и Z»), а не пары «X, оборот, и Y». **Prev L4-AG.1a.5 batch 32 builtin schema-table 2.4-3.0KB ЗАКРЫТ** (bizevents-processing-metrics-rule, preferences-ipaddressmasking, disk-analytics-extension, virtualization-vmware, mainframe-mqfilters, rum-user-experience-score, synthetic-multiprotocol-outage-handling, rum-web-key-performance-metric-custom-actions, dt-javascript-runtime-app-monitoring, exclude-network-traffic, rum-web-browser-exclusion, deployment-oneagent-updates, rum-mobile-key-performance-metrics, host-monitoring-mode, rum-web-resource-types, synthetic-browser-outage-handling, rum-custom-enablement, synthetic-browser-performance-thresholds, mainframe-txstartfilters, span-capturing, container-monitoring-rule, rum-processgroup, rum-web-injection-cookie, anomaly-detection-frequent-issues, availability-process-group-alerting, apis-detection-rules, span-entry-points, attribute-masking, service-splitting-rules, rum-web-custom-errors, bizevents-processing-pipelines-rule, process-group-simple-detection-rule). Build [`scripts/_build_schemas_l4ag1a5.py`](scripts/_build_schemas_l4ag1a5.py) расширяет L4-AG.1a.4 (реюз `_normalize`/`_heading`/`_param_row` с dual-marker enum/`_nested_heading` regex; **empty-label теперь разрешён** — col-1 начинается с `\\`code\\`` без подписи, переводится только cdesc): DISPLAY_NAME 31, SCHEMA_DESC ~45, PARAM_LABEL ~95, PARAM_DESC ~25. Mojibake-аудит EN ДО билда (single `\xc3\xa2` vs triple `\xc3\xa2\xc2\x80\xc2\x99`): BOM 0/32, single 0/32, **triple 1/32** только `rum-custom-enablement.md` строка 44 `applicationâ€™s` (key через chr() L4-AG.1a.4 канон). Line-parity 32/32 EXACT, BOM 0, ENUM-leftover EN 0, `## Authentication`-leftover 0. **1 деф пойман auto-review:** `attribute-masking` строка 39 em-dash в моём же переводе («остальные — только нечувствительные части») → ; + новая фраза. **1 минор-фикс из spot-check (НЕ автоскриптом):** `rum-mobile-key-performance-metrics` строка 15 «**Tolerable**, и **Frustrating**» (лишняя запятая перед «и» — calque EN comma) → «**Tolerable** и **Frustrating**» (РУ-правило перечисления). Spot-check 8 файлов (rum-custom-enablement triple-mojibake fix + cost-control prose, attribute-masking длинная enum-prefix prose, host-monitoring-mode большой enum-prefix с oneagentctl-ссылкой, rum-mobile-kpm twin к web-kpm, dt-js-app-monitoring empty-label `appMonitoring`, rum-web-resource-types markdown regex с escape `\\*`/`\\.`, availability-pg-alerting большой enum-prefix bold-prefix prose, bizevents-processing-pipelines-rule empty-label `RuleTesting` JSON-комбо, span-capturing twin к span-entry-points SpanMatcher 5-row): 0 семантических деф. **Lessons L4-AG.1a.5:** (1) **empty-label rows** (col-1 = backtick-code без подписи) — добавить ветку в `_param_row`: `if label and label not in PARAM_LABEL: return None` + `new_label = PARAM_LABEL.get(label, label)` (пустой остаётся пустым, переводится только cdesc); раньше такие строки молча оставались EN (Lesson L4-AG.1a.4 расширен). (2) **Auto-review поймал em-dash в МОЁМ переводе** (не только в EN-исходнике) — em-dash check полезен и при «no-em-dash» правиле CLAUDE.md, не только для EN-чистки. (3) **Calque EN comma перед «и»** в RU-перечислениях («Satisfactory, Tolerable, и Frustrating») — типичная переводческая ошибка; в РУ перед последним элементом через «и» запятая НЕ ставится. Spot-check обязателен. (4) **2 разные схемы с одинаковым DISPLAY_NAME** (`Outage handling` в multiprotocol + browser) — один dict-entry покрывает оба, конфликта нет. **Prev L4-AG.1a.4 batch 30 builtin schema-table 2.2-2.4KB ЗАКРЫТ** (devobs-agent-optin, openpipeline-{spans,events,metrics,bizevents,events-sdlc,user-events,davis-events,usersessions,system-events,davis-problems,events-security,security-events}-routing = 12 файлов семьи routing, hyperscaler-authentication-aws-connection, kubernetes-security-posture-management, logmonitoring-log-dpp-rules, sessionreplay-web-resource-capturing, rum-mobile-beacon-endpoint, bizevents-processing-buckets-rule, rum-web-beacon-domain-origins, appsec-rule-settings, rum-web-custom-injection-rules, remote-environment, rum-web-rum-javascript-updates, appsec-notification-alerting-profile, rum-resource-timing-origins, dt-javascript-runtime-allowed-outbound-connections, rum-web-capture-custom-properties, synthetic-browser-kpms, synthetic-http-outage-handling). Build `scripts/_build_schemas_l4ag1a4.py` расширяет L4-AG.1a.3 (реюз `_normalize`/`_heading`/`_param_row` с dual-marker enum/`_nested_heading` regex): DISPLAY_NAME 30, SCHEMA_DESC ~28, PARAM_LABEL ~50, PARAM_DESC ~14; **семья openpipeline-routing 12 файлов** = 1 общий SCHEMA_DESC «Contains configuration of routing» + 12 уникальных DISPLAY_NAME в скобках (spans/events/metrics/.../security.events) + общий RoutingEntry nested-object на 12. Line-parity 30/30 EXACT, em-dash 0, BOM-leftover 0, ENUM-leftover EN 0, `## Authentication`-leftover 0. **1 деф пойман spot-check (НЕ автоскриптом):** synthetic-browser-kpms строка 17 параграф `**Visually complete**` оставался EN — корень: EN-файл содержит **triple-mojibake** `userâ€™s` = bytes `c3 a2 c2 80 c2 99` (3 chars U+00E2 U+0080 U+0099, апостроф `'` дважды передекодированный), а ключ в SCHEMA_DESC написан как одиночный `userâs` = bytes `c3 a2` (2 байта вместо 6). Фикс: ключ переписан через chr() конкатенацию `... user` + chr(0xE2) + chr(0x80) + chr(0x99) + `s ...` чтобы Python-source выдал точные 6 байт; replace сработал. Spot-check 8 файлов (rum-web-custom-injection-rules длинный Example head перед enum, remote-environment * лист в head Network scope, rum-mobile-beacon-endpoint двухстрочное desc, synthetic-browser-kpms triple-mojibake, bizevents-processing-buckets-rule DQL-link, synthetic-http-outage-handling 5 длинных параметр-меток, openpipeline-spans-routing twin-family, hyperscaler-aws WebIdentity nested, devobs-agent-optin, kubernetes-spm KSPM, logmonitoring-log-dpp-rules ProcessorDefinition+RuleTesting 2 nested, rum-web-rum-javascript-updates **Latest stable**/**Custom**, appsec-notification-alerting-profile Set<TriggerEvent>/Set<RiskLevel>): 0 семантических деф. **Lessons L4-AG.1a.4:** (1) **Mojibake-аудит ДО сборки должен различать однократное (1-char U+00E2 = 2 bytes) и тройное (3-char U+00E2 U+0080 U+0099 = 6 bytes)** — оба отображаются одинаково как `â...s` в IDE/Read, но Python-source одного видимого `â` создаёт только 2 байта и `str.replace` не находит EN-строку. Невидимые U+0080/U+0099 кодируем через `chr(0xE2)+chr(0x80)+chr(0x99)` в конкатенации dict-ключа. Hex-dump EN-файла даёт истину. (2) **Семья 12 идентичных файлов (openpipeline-routing)** идеально консолидируется: 1 общий SCHEMA_DESC + 12 уникальных DISPLAY_NAME + общий RoutingEntry nested-object покрывают 12 файлов одним dict-проходом. (3) **API-имена с точкой/дефисом не переводим** (events.sdlc, davis.problems, security.events, usersessions); только без точки: (events) → (события), (metrics) → (метрики). Канон с L4-AG.1a.3 ((logs) → (логи)). (4) **Auto-review НЕ ловит EN-leftover целый параграф** в schema-описании. Spot-check 6-8 файлов ОБЯЗАТЕЛЕН после каждой партии, особенно для файлов с длинными многоабзацными описаниями (kpms, beacon-endpoint, rum-resource-timing-origins). **Prev L4-AG.1a.3 batch 35 builtin schema-table 1.95-2.2KB ЗАКРЫТ** (cloud-development-environments, dashboards-image-allowlist, rum-web-beacon-endpoint, synthetic-http-scheduling, synthetic-synthetic-availability-settings, synthetic-http-assigned-applications, monitored-technologies-go, problem-fields, synthetic-browser-scheduling, logmonitoring-log-custom-attributes, synthetic-browser-assigned-applications, hub-channel-subscriptions, ownership-config, appsec-notification-attack-alerting-profile, rum-web-rum-javascript-file-name, usability-analytics, monitored-technologies-php, settings-subscriptions-service, attribute-block-list, attribute-allow-list, tokens-token-settings, synthetic-http-cookies, dashboards-presets, eec-local, monitored-technologies-wsmb, bizevents-http-capturing-variants, rum-web-xhr-exclusion, logmonitoring-log-buckets-rules, dashboards-general, rum-host-headers, networkzones, rum-web-ipaddress-exclusion, oneagent-features, host-monitoring-advanced, openpipeline-logs-routing). **Next: L4-AG.1a.5** ~30-40 builtin 2.4-3.0KB. Остаток builtin 193/307 (63%). Канон+история в TRANSLATION_PROGRESS.md header+Status (memory=указатель).
Source corpus: 2655 EN files in `docs/managed/`
Target corpus: 2077 RU files in `docs/managed-ru/` (после L4-AG.1b.1; **Orphan RU 0**, корпус консистентен; **builtin schemas 307/307 = 100%**; **dynatrace-api 1140/1142 = 99.8%**)
Translated: **2077 файлов** (EN AND RU), **78.23%**
Remaining: **578 файлов**

## P0 Rework выполнен 2026-05-14 (Opus 4.7)

Согласно Lesson L37 (Sonnet вырезал контент), 3 P0-файла пере-переведены Opus 4.7 с восстановлением утраченного:
- ✅ `ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus.md` — восстановлены прямые ссылки, scraped дата возвращена в EN-оригинал, удалена выдуманная секция «Связанные темы»
- ✅ `ingest-from/dynatrace-activegate/configuration/configure-activegate.md` (567/419 → 567/567) — восстановлены 1.247- conditional notes, property descriptions, http.client.* details
- ✅ `ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container.md` (1561/245 → 1561/1559) — **восстановлены оба AppArmor-профиля целиком** (~960 строк YAML), второй docker run, `--cgroupns=host` note

**Lesson L40:** при rework пере-перевод выполнять блочно с EN, сохраняя ВСЕ code-блоки 1-в-1 (включая пустые строки в коде). AppArmor-профили — это production-security конфиги, любая потеря строки = провал безопасности.

## Как пользоваться

1. `python scripts/translation_diff.py` — перегенерирует список НЕпереведённых файлов в `_pending.txt`.
2. Очередь батчей ниже. Каждый батч — одна тема, ~5–13 файлов.
3. После завершения батча Sonnet-агент ставит `[x]` напротив файла и обновляет `Last update` в шапке батча.
4. **Не закрывать батч пока не переведены ВСЕ файлы списка.** Это защита от «забыл что-то».
5. Когда батч закрыт — снова прогнать `translation_diff.py`. Если строка осталась — значит файл не переведён, реоткрыть.

## Status

| Batch | Тема | Files | Done | Status |
|-------|------|-------|------|--------|
| 1 | Migration & Scaling core | 10 | 10 | ✅ done |
| 2 | Hardware / sizing / install | 7 | 7 | ✅ done |
| 3 | High Availability & rack-aware | 7 | 7 | ✅ done |
| 4 | Cluster configuration | 13 | 13 | ✅ done |
| 5 | Cluster operation & self-monitoring (остаток managed-cluster/) | 27 | 27 | ✅ done |
| 6 | Upgrade | 19 | 19 | ✅ done |
| 7 | discover-dynatrace + platform + offline-doc + root indexes | 23 | 23 | ✅ done |
| 8 | secure/ — Application Security (полный раздел) | 28 | 28 | ✅ done |
| 9 | license/ — Licensing & consumption (полный раздел) | 42 | 42 | ✅ done |
| 10 | dynatrace-intelligence/ — Davis AI, Anomaly Detection, RCA (полный раздел) | 31 | 31 | ✅ done |
| 11 | deliver/ — CaC Monaco+Terraform, Ownership, Release monitoring, SLO, Test automation (полный раздел) | 40 | 40 | ✅ done |
| 12A | analyze-explore-automate/ — Dashboards, Explorer, Log Monitoring (33 файла) | 33 | 33 | ✅ done |
| 12B | analyze-explore-automate/ — Log processing functions, Metrics, Notifications, Smartscape (53 файла) | 53 | 53 | ✅ done |
| 13A | manage/ — IAM + tags + system (38 файлов) | 38 | 38 | ✅ done |
| 14 | whats-new/ — Release notes (полный раздел) | 66 | 66 | ✅ done |
| L1A | observe/application-observability/ (Batch 1, 54 файла) | 54 | 54 | ✅ done |
| L1B1 | observe/infrastructure-observability/ — container-platform-monitoring + hosts + process-groups + extensions/opentelemetry (49 файлов) | 49 | 49 | ✅ done |
| L1B2 | observe/infrastructure-observability/ — остаток: databases + networks + queues + cloud-platform-monitoring + vmware (26 файлов) | 26 | 26 | ✅ done |
| L1C | observe/digital-experience/web-applications/ (55 файлов: additional-configuration + analyze-and-use + initial-setup + troubleshooting) | 55 | 55 | ✅ done |
| L1D-quick | observe/digital-experience.md (Opus, root index) | 1 | 1 | ✅ done |
| L2A | dynatrace-api/basics/ (Opus, 5 файлов) | 5 | 5 | ✅ done |
| L2B | dynatrace-api/cluster-api/ root (Opus, 3 файла) | 3 | 3 | ✅ done |
| L2C | dynatrace-api/account-management-api/ + subscription-api/* (Opus, 12 файлов) | 12 | 12 | ✅ done |
| L2D | dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/ (Opus, 5 файлов) | 5 | 5 | ✅ done |
| L2E | cluster-v1/ остаток: info-known-servers, configuration-current-status, configuration-request-status | 3 | 3 | ✅ done |
| L2F | cluster-api-v1/internet-proxy-v1/ (9 endpoints: get/put/delete/test + HA-варианты) | 9 | 9 | ✅ done |
| L2G | cluster-api-v1/password-policy-v1/ (get + put) | 2 | 2 | ✅ done |
| L2H | cluster-api-v1/ssl-certificates-v1/ (cert-details + storage-status + post-store) | 3 | 3 | ✅ done |
| L2I | cluster-api-v1/users-v1/ (delete/get/get-all/post-create/post-create-bulk/put-update) | 6 | 6 | ✅ done |
| L2J | cluster-api-v1/user-groups-v1/ (delete-group/get-group/get-group-mz/get-groups-mz/get-user-groups/post-create-user-group/post-create-users-groups/put-update-group-mz/put-update-user-groups) | 9 | 9 | ✅ done |
| L2K | cluster-api-v2/ ВСЕ 8 подразделов (cluster-license/cluster-tokens/environments/export-license-data/log-monitoring/remote-access/synthetic-locations-and-nodes/user-management) | 31 | 31 | ✅ done |
| L2L | mission-control-api/ ВСЕ 3 подраздела (cluster-sso-client-registration/cluster-sso-token-generation/offline-bundle-packages) | 4 | 4 | ✅ done |
| L2M | Root index .md (mission-control-api.md + configuration-api.md + environment-api.md) | 3 | 3 | ✅ done |
| L2N | account-management-api/ closure (environment-management-api/ + post-notifications.md) | 2 | 2 | ✅ done |
| L2O | configuration-api/ старт: aws-privatelink (5) + data-privacy-api (2) + frequent-issue-detection-api (2) | 9 | 9 | ✅ done |
| L2P | configuration-api/ дальше: k8s-credentials-api (5) + maintenance-windows delete-mw + get-all (2) | 7 | 7 | ✅ done |
| L2Q | maintenance-windows-api closure: get-mw (527) + post-mw (724) + put-mw (778) | 3 | 3 | ✅ done |
| L2R | conditional-naming/ почти полностью: root index (32) + del-rule (43) + get-all (132) + get-rule (256) + post-rule (487) + put-rule (487). Остался json-models.md (1367) | 6 | 6 | ✅ done |
| L2S | environment-api/ ВСЕ 29 root indexes: activegates + anonymization + audit-logs + cluster-information (158) + credential-vault + custom-tags + deployment + entity-v2 + events-v1 + events-v2 + extensions-20 + hub + log-monitoring-v2 + metric-v1 + metric-v2 + metrics-units + network-zones + opentelemetry + problems + problems-v2 + releaseapi + remote-configuration + service-level-objectives-classic + settings + synthetic + synthetic-v2 + tokens-v1 + tokens-v2 + topology-and-smartscape (1122 строки суммарно) | 29 | 29 | ✅ done |
| L2T | environment-api/ малые подпапки: opentelemetry/ 3 endpoints (post-logs 83 + post-metrics 51 + post-traces 103) + anonymization/ 2 endpoints (get-job-status 111 + put-job 185) + releaseapi/ 1 endpoint (get-releaseall 335). 868 строк суммарно. | 6 | 6 | ✅ done |
| L2U | environment-api/ средние подпапки: audit-logs/ 2 endpoints (get-entry 426 + get-log 491) + custom-tags/ 3 endpoints (del-tags 196 + get-tags 327 + post-tags 455). 1895 строк суммарно. | 5 | 5 | ✅ done |
| L2V | environment-api/network-zones/ полностью: del-network-zone (129) + get-all (223) + get-global-config (146) + get-network-zone (201) + put-global-config (154) + put-network-zone (240). 1093 строки. | 6 | 6 | ✅ done |
| L2W | environment-api/activegates/ старт: 3 sub-index (activegate-info 21 + auto-update-config 25 + auto-update-jobs 29) + activegate-info/ полностью (get-activegate 491 + get-all 625). 1191 строка. | 5 | 5 | ✅ done |
| L2X | environment-api/activegates/auto-update-config/ полностью: get-global (204) + get-instance (157) + put-global (326) + put-instance (277). 964 строки. | 4 | 4 | ✅ done |
| L2Y | environment-api/activegates/auto-update-jobs/ полностью: delete-job (158) + get-job (308) + get-all-jobs (428) + get-activegates-jobs (277) + post-job (542). 1713 строк. **activegates/ закрыт целиком (14 файлов суммарно через L2W+L2X+L2Y).** | 5 | 5 | ✅ done |
| L2Z | environment-api/credential-vault/ полностью: del-credentials (132) + get-credentials (288) + get-all (476) + models (270) + post-credentials (416) + put-credentials (302). 1884 строки. **credential-vault/ закрыт целиком.** | 6 | 6 | ✅ done |
| L3A | environment-api/application-security старт: attacks.md sub-index (19) + vulnerabilities.md sub-index (20) + davis-security-advice (278) + attacks/ полностью (get-attack-details 886 + get-attacks 930). 2133 строки. **attacks/ закрыт целиком.** | 5 | 5 | ✅ done |
| L3B | application-security/vulnerabilities/ POSTs+PUT: post-mute-vulnerability (231) + post-unmute-vulnerability (231) + post-mute-vulnerabilities (366) + post-problems-unmute (370) + post-remediation-items-mute (354) + post-remediation-items-unmute (352) + post-remediation-item-tracking-link (380) + put-remediation-items (246). 2530 строк. | 8 | 8 | ✅ done |
| L3C | application-security/vulnerabilities/ small/medium GETs: get-remediation-item-entities (466) + get-vulnerable-functions (469) + get-remediation-item-details (732). 1667 строк. | 3 | 3 | ✅ done |
| L3D | application-security/vulnerabilities/ big GETs пара 1: get-vulnerability-events (849) + get-remediation-items (994). 1843 строки. | 2 | 2 | ✅ done |
| L3E | application-security/vulnerabilities/ big GET: get-vulnerability-details (1495). | 1 | 1 | ✅ done |
| L3F | application-security/vulnerabilities/ big GET: get-vulnerabilities (1822). **vulnerabilities/ 15 файлов закрыт целиком, application-security/ полностью завершён.** | 1 | 1 | ✅ done |
| L3G | configuration-api/conditional-naming/json-models.md (1367 строк, последний файл cond-naming/). **conditional-naming/ закрыт целиком (6 файлов).** | 1 | 1 | ✅ done |
| L3H | environment-api/tokens-v2/ 3 sub-index (activegate-tokens.md 25 + api-tokens.md 29 + tenant-tokens.md 25). 79 строк. | 3 | 3 | ✅ done |
| L3I | environment-api/tokens-v2/api-tokens/ 6 endpoints (del-token 134 + get-all 257 + get-token 224 + post-token-lookup 166 + post-token 213 + put-token 180). 1174 строки. **api-tokens/ закрыт целиком (6+1=7 файлов).** | 6 | 6 | ✅ done |
| L3J | environment-api/tokens-v2/activegate-tokens/ 4 endpoints (delete-activegate-token 162 + get-activegate-token 253 + get-all-activegate-tokens 384 + post-activegate-token 315). 1114 строк. **activegate-tokens/ закрыт целиком (4+1=5 файлов).** | 4 | 4 | ✅ done |
| L3K | environment-api/tokens-v2/tenant-tokens/ 3 endpoints (post-cancel 236 + post-finish 230 + post-start 234). 700 строк. **tenant-tokens/ закрыт целиком (3+1=4 файла). tokens-v2/ ЗАКРЫТ ЦЕЛИКОМ (7+1+3+1+4+1=17 файлов).** | 3 | 3 | ✅ done |
| L3L | environment-api/hub/ 10 endpoints: get-categories (178) + get-extension-v1-artifact (128) + get-items (274) + post-extension-20-to-evironment (154) + post-update-extension-20 (154) + put-extension-20-release-notes (156) + put-update-extension-20-metadata (162) + get-extension-v1 (645) + get-technology (645) + get-extension-20 (646). 3142 строки. **hub/ закрыт целиком (10+1=11 файлов).** | 10 | 10 | ✅ done |
| L3M | environment-api/events-v2/ 7 endpoints: get-event-property (227) + get-event-type (223) + get-event-properties (343) + get-event-types (335) + get-event (571) + post-event (736) + get-events (958). 3393 строки. **events-v2/ закрыт целиком (7+1=8 файлов).** | 7 | 7 | ✅ done |
| L3N | environment-api/entity-v2/ 6 endpoints: entity-selector (269) + get-entity-type (928) + post-custom-device (334) + get-all-entity-types (1181) + get-entity (927) + get-entities-list (654). 4293 строки. **entity-v2/ закрыт целиком (6+1=7 файлов).** | 6 | 6 | ✅ done |
| L3O | environment-api/problems-v2/ 9 файлов: comments/ 5 (del/get-all/get/post/put) + models.md (JSON-модели Evidence×5 + Impact×4) + problems/ 3 (post-close + get-problem-details + get-problems-list). 3393 строки. **problems-v2/ закрыт целиком (9+1 sub-index=10 файлов).** | 9 | 9 | ✅ done |
| L3Q | Зачистка 5 orphan RU (off-scope SaaS/Platform, переведены до Managed-only правила, EN-пары нет, не в nav): copilot-faq + azure-cassandra + setup-on-k8s/security-posture-management + database-app/postgres + secure/resolve-incidents-templates. verify_corpus Orphan RU 5→0. | 5 | 5 | ✅ done |
| L3P | environment-api/metric-v2/ 13 файлов: get-all-metrics + get-descriptor + get-data-points + post-ingest-metrics + delete-metric + delete-metrics + metric-selector (4101 стр, 22 трансформации) + metric-expressions + metric-faq + examples + examples/ 3 (list-all/select-multiple/select-subtree). **metric-v2/ закрыт целиком (13+1 sub-index=14 файлов).** em-dash 0, scope верный (read×3/write×2/ingest). | 13 | 13 | ✅ done |
| L3R | environment-api/extensions-20/ 19 файлов (15.05g, done-on-disk; запись задним числом — verify_corpus +19) | 19 | 19 | ✅ done |
| L3S | environment-api/metric-v1/ 6 файлов (15.05h, done-on-disk; запись задним числом — verify_corpus +6) | 6 | 6 | ✅ done |
| L3T | environment-api/tokens-v1/ 8 файлов (15.05i, done-on-disk; deprecated v1, парный к tokens-v2 L3J/K; запись задним числом — verify_corpus +8) | 8 | 8 | ✅ done |
| L3U | environment-api/problems/ (v1, deprecated) 8 файлов: comments/ 4 (del/get-all/post/put) + problems/ 4 (get-details 1146 + get-feed 1268 + get-status 272 + post-close 206). Глоссарий выровнен по problems-v2 RU-партнёру (L87: «Поле»/«смотрите»/периоды, ссылка «Tokens and authentication» англ.); v1-баннер из L3T (drop `* Deprecated` bullet → в фразу «Этот API устарел…»). Enum-списки + JSON вербатим (L85), включая mojibake `Âµs`/`â°`. em-dash 0 (вкл. фикс mojibake-em-dash в get-feed L21). **problems/ v1 закрыт целиком (8 файлов).** | 8 | 8 | ✅ done |
| L3V | environment-api/service-level-objectives-classic/ 6 файлов: delete-slo + get-all (387, SLO+SloBurnRate+SLOs объекты) + get-slo (339, SLO идентичен get-all L85) + post-slo (SloConfigItemDtoImpl+SloBurnRateConfig) + post-slo-alert (AbstractSloAlertDto+EntityShortRepresentation) + put-slo (SloConfigItemDtoImpl идентичен post-slo L85). НЕ deprecated (classic, активный API, без баннера). Глоссарий: env-api boilerplate по problems-v2 («Поле»/«смотрите»/периоды/ErrorEnvelope), SLO-домен из deliver/ RU («цель уровня обслуживания», «бюджет ошибок», «скорость расходования», «алерт»); `~~field~~` strikethrough + DEPRECATED→УСТАРЕЛО вербатим; BOM-mojibake `ï»¿` убран (broken-char 0); JSON+`\"SERVICE\"` вербатим L85; related-topics по уже принятому в корпусе рендеру. em-dash 0. **SLO-classic закрыт целиком (6 файлов).** | 6 | 6 | ✅ done |
| L3W | environment-api/synthetic-v2/ 27 файлов: 4 sub-index (synthetic-locations-v2/monitor-execution/network-availability-monitors/nodes-v2) + synthetic-configuration-v2/ 2 + synthetic-locations-v2/ 8 (вкл. json-models) + synthetic-monitor-execution/ 6 + synthetic-network-availability-monitors/ 5 + synthetic-nodes-v2/ 2. Активный API v2 (не deprecated, без баннера, L89). Глоссарий по problems-v2 RU (L87: Справочник/Опубликовано/Поле/смотрите/scope). Shared ErrorEnvelope+Error+ConstraintViolation идентичны (L85). JSON вербатим. BOM-mojibake ï»¿ убран (broken-char 0). em-dash 0. **synthetic-v2/ закрыт целиком (27 файлов).** | 27 | 27 | ✅ done |
| L3X | environment-api/synthetic/ (v1) 23 файла: 4 sub-index (synthetic-locations/monitors/nodes + third-party-synthetic) + synthetic-locations/ 8 + synthetic-monitors/ 6 (get-a/put-a/models/post-a крупные ~1.2K) + synthetic-nodes/ 2 + third-party-synthetic/ 3. **НЕ deprecated** (нет `* Deprecated` bullet → без баннера, L89; отличие от tokens-v1/problems-v1). Глоссарий по ПАРНОМУ L3W synthetic-v2 RU (L86/L87): synthetic-locations/ и synthetic-nodes/ — прямые твины, shared SyntheticLocations/LocationCollectionElement/ErrorEnvelope/Error/ConstraintViolation идентичны L85. «We have a new version» с mojibake `â` переведено прозой без em-dash, ссылка Synthetic API v2 англ. get-a-monitor↔put-a-monitor↔post-a-monitor общий объект идентичен L85. JSON вербатим. mojibake/BOM `â`/`Â`/`ï»¿` убран broken-char 0. em-dash 0. **synthetic/ v1 закрыт целиком (23 файла); пара synthetic v1↔v2 завершена.** | 23 | 23 | ✅ done |
| L3Z | environment-api/remote-configuration/ 14 файлов: 2 sub-index (activegate.md/oneagent.md, групповой card-формат с пустыми строками между группами + `## Связанные темы`) + activegate/ 5 (get-finished-jobs/get-current-job/get-job/post-job-preview/post-config-job) + oneagent/ 7 (те же 5 + execute-migration + post-dry-run). **АКТИВНЫЙ API без баннера** (нет `* Deprecated`, L89/L90; `* Reference`→`* Справочник`, даты переведены; oneagent/post-job-preview `* Updated on`→`* Обновлено 29 июля 2025`). **Twin activegate↔oneagent (L85):** 5 пар отличаются title (ActiveGate↔OneAgent), endpoint-path (`activeGates`↔`oneagents`), scope (`activeGates.read/write`↔`oneAgents.read/write`), «для ActiveGate»↔«для OneAgent»; shared объекты RemoteConfigurationManagementJob/JobSummary/JobList/Operation/RemoteIdentityOperationFailedEntityDto/ValidationResult/EntityValidationError/OperationValidationError + ErrorEnvelope/Error/ConstraintViolation идентичны. **Twin-расхождения сохранены:** post-config-job activegate prose «Ответ не отправляется…» ДО `### Коды ответа`, oneagent — ПОСЛЕ JSON-моделей перед `## Проверка payload` (структурно разное в источнике, оба верны); oneagent/post-config-job+post-dry-run+execute-migration имеют доп. `restart` query-param + `## Проверка payload` секцию с h3/h4. Глоссарий: «remote configuration management» как имя фичи англ. + «задание»/«операция» переведены; «job» domain → «задание»; source-bug «Lists completed configuration job» (ед.ч.) → RU мн.ч. «задания» (list-эндпоинт, смысл важнее опечатки, L93). `## Validate payload`→`## Проверка payload`, h3 `### Authentication/Response`→`### Аутентификация/Ответ`, h4 `#### Response codes/body objects/body JSON models` переведены. Request body Required-колонка header `| Поле | Тип | Описание | Обязательный |` Required→Обязательный/Optional→Необязательный. JSON вербатим (0x… и HOST-… значения различаются по источнику). em-dash 0; broken-char 0; **структурный паритет EN↔RU h1/h2/h3/h4/таблицы/код-фенсы 14/14 идеальный + line-parity h2 проверена (Python QA 0 issues)**. **remote-configuration/ закрыт целиком (14 файлов); dynatrace-api 700 pending/406 done.** | 14 | 14 | ✅ done |
| L3Y | environment-api/deployment/ 25 файлов: 4 sub-index (oneagent.md card-формат с `* Обзор` + activegate/bosh/orchestration `* Справочник`) + activegate/ 5 (get-latest-image/get-activegate-versions/download-latest/download-version/get-connectivity) + oneagent/ 9 (get-activegate-endpoints без `### Коды ответа` + source-bug-параграф, get-arns-for-lambda-layers, download-latest/version, get-version-latest, get-available-versions, get-connectivity-info, get-latest-version-lambda-classic, get-processmodule-config) + bosh/ 3 (download-version 2-кол. endpoint-блок + **PaaS token**/[Access tokens] вместо scope, get-bosh-checksum, get-available-version) + orchestration/ 4 (get-latest/get-latest-signature/get-version/get-version-signature). **АКТИВНЫЙ API** (нет `* Deprecated` → без баннера, L89/L90; `* Reference`→`* Справочник`, `* Overview`→`* Обзор`, даты переведены L3R-конвенция). Глоссарий по L3X synthetic v1 RU (L87): «Поле»/«В»/«Обязательный»/«Необязательный»/«access-токен со scope `InstallerDownload`»/«[Tokens and authentication]» англ.+«смотрите». Большие param-описания osType/installerType/flavor/arch/bitness/include идентичны между файлами (L85, перевод 1 раз+копия); shared ErrorEnvelope/Error/ConstraintViolation + пустой `#### Объект ResponseBody` (без таблицы) идентичны L85; JSON вербатим. BOM `ï»¿` убран в download-activegate-version/download-oneagent-version/download-bosh-version (broken-char 0). Source-bugs вербатим: дубль описания get-activegate-endpoints↔get-processmodule-config в oneagent.md card, double-period «образ ActiveGate..», «techtype Поле» без точки. em-dash 0; структурный паритет EN↔RU h1/h2/h3/h4/таблицы/код-фенсы 25/25 идеальный (Python QA 0 issues). **deployment/ закрыт целиком (25 файлов); dynatrace-api 714 pending/392 done.** | 25 | 25 | ✅ done |
| L4C | configuration-api/anomaly-detection-api/ process-groups (4) + disk-events (6) ЗАКРЫТЫ ЦЕЛИКОМ | 10 | 10 | ✅ done |
| L4D | configuration-api/anomaly-detection-api/ applications (3) + database (3) + services (3) + главный parent anomaly-detection-api.md (1) ЗАКРЫТЫ ЦЕЛИКОМ | 10 | 10 | ✅ done |
| L4E | configuration-api/remote-environments/ parent + 5 CRUD (get-all/get/del/post/put) ЗАКРЫТ ЦЕЛИКОМ (deprecated API) | 6 | 6 | ✅ done |
| L4F | configuration-api/credential-vault/ parent + 6 (get-all/get-credentials/del/models/post/put) ЗАКРЫТ ЦЕЛИКОМ (deprecated, twin env-api) | 7 | 7 | ✅ done |
| L4G | configuration-api/aws-credentials-api/ parent + 7 (get-all/get-credentials/get-services/delete/post-new/put-credentials/put-services) ЗАКРЫТ ЦЕЛИКОМ (АКТИВНЫЙ, без баннера) | 8 | 8 | ✅ done |
| L4H | configuration-api/azure-credentials-api/ parent + 7 (get-all/get-credentials/get-services/delete/post-new/put-credentials/put-services) ЗАКРЫТ ЦЕЛИКОМ (АКТИВНЫЙ, без баннера; структурный twin aws-credentials-api RU L85) | 8 | 8 | ✅ done |
| L4I | configuration-api/reports-api/ parent + 7 (del-report/get-all/get-report/post-report/put-report/subscribe-report/unsubscribe-report) ЗАКРЫТ ЦЕЛИКОМ (АКТИВНЫЙ, без баннера; L103 case b: env-api twin'а нет → anchor azure/aws-credentials RU; «report»→«отчёт») | 8 | 8 | ✅ done |
| L4J | configuration-api/alerting-profiles-api/ parent + 5 (del-profile/get-all/get-profile/post-profile/put-profile) ЗАКРЫТ ЦЕЛИКОМ (DEPRECATED, Settings API banner L4E канон; L103 case b: env-api twin'а нет → anchor remote-environments RU + k8s-credentials shared; «alerting profile»→«профиль оповещений») | 6 | 6 | ✅ done |
| L4K | configuration-api/notifications-api/post-a-notification (DEPRECATED, Settings API banner L4J канон) + mobile-symbolication-api parent + 9 endpoints (АКТИВНЫЙ, L89/L90 без баннера) ЗАКРЫТЫ ЦЕЛИКОМ. L103 case b: env-api twin'а нет → k8s-credentials shared. Domain corpus-доминанта: «symbol file»→«файл символов» (58×), «symbolication»→«символикация», «deobfuscation»→«деобфускация», «stack trace»→«трассировка стека», «Instrumentation Wizard»→«мастер инструментирования» | 11 | 11 | ✅ done |
| L4L | configuration-api/automatically-applied-tags-api/ parent + 5 CRUD (del/get-all/get/post/put-auto-tag) ЗАКРЫТЫ ЦЕЛИКОМ (DEPRECATED, two-link Settings banner «со schema [Automatically applied tags](…)(builtin:tags.auto-tagging).» по kubernetes-connection precedent + standalone «Deprecated»→«Устарело» L4B; L103 case b: env-api twin'а нет → k8s-credentials shared; «auto-tag»→«автоматически применяемый тег» corpus-prose, feature/banner-link EN-lock; «entity selector»→«селектор сущностей»; Related-topics link-text corpus-translated). **models.md (1376) DEFER L42 отд.сессия.** 0 деф с первого прогона | 6 | 6 | ✅ done |
| L4M | configuration-api/oneagent-configuration/ 4 parent + 10 endpoints (env-wide/in-host-group/on-host: get/put auto-update + technology-monitoring + oneagent-config) ЗАКРЫТ ЦЕЛИКОМ (13 АКТИВНЫХ + 1 DEPRECATED put-monitoring: bold-schema banner «со schema **Monitoring** (builtin:host.monitoring).» maintenance-windows L2Q canon, `* Deprecated` bullet опущен events-v1 L4A precedent = EN==RU+1; L103 case b: env-api twin'а нет → maintenance-windows + k8s-credentials shared; «auto-update»→«авто-обновление» corpus-prose, object/enum/`**setting**` EN-lock; Related-topics link-text translated). Splice-билдер CRLF→LF + 3-char `ï»¿` BOM strip. 3 деф пойманы-исправлены (CRLF newline-anchor, missing `### Response`, U+FEFF≠3-char BOM) → повторный 0 деф | 14 | 14 | ✅ done |
| L4O | configuration-api/calculated-metrics/ top parent + mobile-app-metrics/ (6) + rum-metrics/ (6) + synthetic-metrics/ (6) ЗАКРЫТЫ ЦЕЛИКОМ (АКТИВНЫЙ API L89/L90; service-metrics/ 7 ОТЛОЖЕН L42 — json-models 932 + post/put 767/798). L85/L86 twin: mobile/rum/synthetic = near-twins, splice-canon 1 раз. L103 case b: env-api calc-twin'а нет → config-api L99 (reports-api RU) + k8s-credentials RU shared. Domain corpus-доминанта: «calculated metric»→«вычисляемая метрика» (158× вычисляем*), «synthetic metric»→«синтетическая метрика» (единств. RU-прецедент) НО «synthetic monitor»/«clickpath» EN (229/80 EN-dominant), object/enum/title EN-lock. L101 12/12 период-по-источнику (mobile/synthetic post/put resp без точки, validate с точкой; rum оба с точкой). Related-topics link-текст = ФАКТИЧЕСКИЙ target RU H1 дословно (mobile «вычислеННых» ≠ «вычисляемых» прозы, НЕ нормализовано); title-attr corpus. Splice `_build_calcmetrics.py` CRLF→LF + BOM-strip. **Ревью `_review_calcmetrics.py` + НОВЫЙ SUSPECT-substring scan: 0 деф с ПЕРВОГО прогона structural+semantic** (force-sync 0=byte-identical L98/L100, line-parity EXACT 19/19, heading/fence/table 19/19, em-dash/mojibake/leftover/SUSPECT 0, EN-инварианты) + семантик spot-check (L101 12/12, env-leak 0, colon 42, shared Error ×12/×24/×12, target-H1 дословно, combined-block, enum EN-lock, прочтён rum/post 450). Правок не потребовалось. Lesson L4O: near-twin splice 1× на 3 подраздела; related-topics link = target RU H1 ДОСЛОВНО (расхождение не нормализовать); SUSPECT-scan усиление review против L4M-класса; common-term-by-dominance vs distinct-EN-term («metric»→рус vs «monitor»→EN) | 19 | 19 | ✅ done |
| L4N | configuration-api/plugins-api/ parent + 12 endpoints ЗАКРЫТ ЦЕЛИКОМ (АКТИВНЫЙ API без deprecated-баннера L89/L90; L103 case b: env-api plugins-twin'а нет → config-api L99 + k8s-credentials RU shared StubList/EntityShortRepresentation/Error/ConstraintViolation/ConfigurationMetadata; «plugin»→«плагин»/«endpoint»→«эндпоинт» corpus-доминанта prose, object/enum/ActiveGate/OneAgent/`**name**` EN-lock; image alt+caption EN L4D; combined-block card parent reports-api L4I канон, без `## Related topics`). Splice CRLF→LF. **Структурно 0 деф с первого прогона (line-parity EXACT 13/13), НО семантик spot-check поймал 3 деф: (1) parent delete-card описание EN (≠ `### `-заголовок), (2) `#### Response body JSON models` ####-вариант не покрыт (билдер+review только `### `), (3) get-plugin-binary `## Response` уникальная проза без codes-таблицы → исправлены, повторный 0 деф + UTF-8 leftover-scan 0 истинных.** Lesson L4N: card title/desc near-twin = 2 splice-строки; heading-правила+review-LEFTOVER на ВСЕ уровни; уникальная `## Response`-проза = отд. правило; structural-0≠готов, semantic spot-check обязателен (L4M подтверждён) | 13 | 13 | ✅ done |
| L4P | configuration-api/extensions-api/ parent + 15 endpoints ЗАКРЫТ ЦЕЛИКОМ (АКТИВНЫЙ API L89/L90; L103 case b: env-api twin'а нет → config-api L99 + k8s-credentials RU shared + plugins-api L4N sibling; «extension»→«расширение»/«instance»→«экземпляр»/«endpoint»→«эндпоинт» corpus, «host group»/«management zone» EN-lock L4B 36:10/81:16, object/enum/title EN-lock; L101 ВСЕ 6×400 БЕЗ точки vs plugins L4N С точкой — грепать). Структурно 0 деф с первого, семантик поймал 1 деф (parent prefix-substring `### View an extension` ⊂ `### View an extension's instance` → ГИБРИД) → fix + 0 деф. Lesson L4P: prefix-substring card-heading = гибридный RU+EN leftover, ловит только semantic/SUSPECT; common-term-by-dominance контекст-зависимо | 16 | 16 | ✅ done |
| L4Q | configuration-api/management-zones-api/ get-all + post-mz ЗАКРЫТ (DEPRECATED, L4L two-link Settings-banner «со schema [Management zones settings](…)(builtin:management-zones).» + standalone «Deprecated»→«Устарело» L4B; НЕТ parent index; json-models 1371 ОТЛОЖЕН L42 — паттерн conditional-naming L3G / autotags models.md; L103 case b: env-api mz-twin'а нет → k8s-credentials RU shared + L4L automatically-applied-tags RU twin структурно). **«management zone»→«зона управления» (КОНТЕКСТ-ЗАВИСИМО: целевая Related-topics страница RU H1 «Зоны управления» + corpus «зон* управления» 592 vs literal EN 197 + L4J precedent «ID зоны управления»; ПРОТИВОПОЛОЖНО L4P EN-lock 81:16 — там mz incidental cross-ref, здесь ПРЕДМЕТ батча)**; «custom device»→«пользовательское устройство» (единств. translated corpus precedent, twin переводит sibling entity-nouns); «dimensional»→«по измерениям» (corpus «измерение»). L101 грэп-по-источнику: get-all без 400; post-mz 400 ×2 = «Сбой. Невалидный ввод» БЕЗ точки (EN-источник БЕЗ точки — ПРОТИВОПОЛОЖНО L4L autotags post где С точкой; грепать, не копировать соседа), 201 «Успех. Зона управления создана. Ответ содержит ID новой зоны.» С точками, validate-204 «Validated. Переданная конфигурация валидна. Ответ без тела.» (Validated. EN-prefix L4I). BOM `ï»¿` в `[JSON modelsï»¿]` ×4 вычищен. Канон L99 (Возможные значения: ×10 с двоеточием env-leak 0; header `| Параметр | Тип | Описание | Где | Обязательный |`, Optional/Required-значения EN; `## Validate payload`/`#### Curl` EN; `### URL запроса` h3 по источнику; image alt+caption EN L4D). Related-topics link-текст = target RU H1 ДОСЛОВНО «[Зоны управления]» + title corpus (L4L/L4O lesson). **Критич.ревью `scripts/_review_mgmtzones.py` 0 деф с ПЕРВОГО прогона** (force-sync 0=JSON byte-identical L98/L100, line-parity EXACT 227/227 + 842/842, heading/fence/table-row 2/2, em-dash/mojibake/BOM/leftover-EN 0, EN-инварианты) + семантик spot-check (banner 1/1×2, env-leak 0, colon 10, L101 400×2 без точки, shared HTTP-код×2/нарушений×4/ошибке×2/Краткое×1/Метаданные×2, `#### Объект` 2/2+17/17, нет stray «management zone» в прозе, link-text EN, `[Зоны управления]`=target RU H1, SUSPECT hybrid 0). Правок не потребовалось (0-с-первого серия L4L/L4O/L4Q). **Lesson L4Q: (1) common-term-by-dominance КОНТЕКСТ-ЗАВИСИМО — термин решать по роли в конкретном доке (предмет vs incidental cross-ref), НЕ глобально; (2) L101 грепать EN-ячейку каждого файла (mz post 400 БЕЗ точки vs L4L autotags С точкой при идентичной структуре); (3) subtree без parent index = get-all+post-mz закрывают, huge json-models 1371 → L42 самостоятельно (паттерн L3G)** | 2 | 2 | ✅ done |
| L4R | configuration-api **orphan-parent cleanup**: 4 subsection parent index'а где endpoints были 100% done но `.md`-parent отсутствовал → подсекции ЗАКРЫТЫ ЦЕЛИКОМ: aws-privatelink (ACTIVE, +5 endpoints), data-privacy-api (ACTIVE, +2), k8s-credentials-api-api (DEPRECATED, +5), maintenance-windows-api (DEPRECATED, +5); + 2 standalone L85-twin: aws-supported-services + azure-supported-services (ACTIVE, полные L99 endpoint-доки, near-exact twins). Канон L99 (title/H1×2/`* Reference`/`* Published`/`* Updated on` EN-verbatim — reports-api/aws-credentials-api RU подтверждают; card-link parent L4D/L4I: concatenated `](url "title")[### ` glue сохранён, heading/body/title переведены, URL/anchor нетронуты). **НОВЫЙ anchor-rule: parent DEPRECATED-баннер ОБЯЗАН = verbatim-match баннеру СОБСТВЕННЫХ уже-переведённых endpoint'ов подсекции** (k8s two-link «со schema [Kubernetes connection settings](…)(builtin:cloud.kubernetes) и [Kubernetes platform monitoring settings](…)(builtin:cloud.kubernetes.monitoring).» L4L/L4Q; maintenance-windows «со schema **Maintenance windows** (builtin:alerting.maintenance-window).» L2Q/L4M — грепнут из endpoint RU, скопирован дословно, НЕ переведён заново с EN). EN-locks по RU-endpoint: «AWS PrivateLink»/«allowlist» (RU «список AWS-аккаунтов из allowlist»), «credentials» (aws-credentials family L4G/L4H), «maintenance window(s)»/«downtime» (L99/L4M), «data privacy» (RU endpoint); `**Data privacy**`/`**Maintenance windows**` bold EN. data-privacy cross-ref link-text EN `[Web application configuration - Data privacy API]` (target rum/web-app-config НЕ переведён, L4J); Related-topics link-text EN + title переведён (reports-api L4I). k8s BOM `ï»¿` в `[Explore Kubernetes in Dynatrace Hubï»¿]` вычищен. EN source-typo «Remove and account» → по смыслу «Удаление аккаунта» (L93). supported-services L99 full: «Запрос возвращает payload `application/json`», endpoint-table «ManagedDynatrace for Government»/«Environment ActiveGate» EN-verbatim (alerting-profiles RU подтверждает), `## Аутентификация`/«access token со scope `ReadConfig`»/`[Tokens and authentication]` EN/`## Параметры`/«В запросе нет настраиваемых параметров.»/`## Ответ`/`### Коды ответа`/`| Код | Тип | Описание |`/«Успех»/`#### Объект`/`### JSON-модели тела ответа`/`#### Curl` EN/`#### URL запроса`/`#### Тело ответа`/`#### Код ответа`; JSON force-sync byte-identical L98/L100. L101 период-по-источнику supported-services element-rows: cloudProviderServiceType/name С точкой (EN с точкой), displayName/entityType БЕЗ точки (EN без) — source-faithful. L85 twin aws↔azure (AWS→Azure, /aws/→/azure/, twin JSON, twin Related). **Критич.ревью `scripts/_review_l4r.py` (force-sync fence + line/heading/fence/table parity + em-dash CLAUDE#0 + mojibake/BOM + EN-инварианты + banner-verbatim-match + L101 period + leftover-EN-prose + URL-preservation): 0 деф с ПЕРВОГО прогона** (4-й 0-с-первого подряд: L4L/L4O/L4Q/L4R) + семантик spot-check (прочтены все 6: banner verbatim 2/2, glue intact, L4P prefix-substring hybrid 0, EN-locks верны, BOM clean k8s, JSON byte-identical через force-sync). Правок не потребовалось. **Lesson L4R: (1) orphan-parent cleanup batch = high-value L42-aligned — подсекция с 100% endpoints но без parent.md = «half-finished», закрывать parent-only батчем (мелкие low-risk файлы, доводят существующую работу); (2) parent DEPRECATED-баннер ОБЯЗАН verbatim-match баннеру СОБСТВЕННЫХ endpoint'ов (сильнейший anchor — читатель видит один баннер на parent + каждом endpoint API; грепать endpoint RU, не ре-деривить с EN); (3) L85 twin применим и к standalone-файлам без подсекции (aws↔azure-supported-services near-exact)** | 6 | 6 | ✅ done |
| L4S | configuration-api/rum/ 4 simple twin-подсекции (allowed-beacon-cors / content-resources / geographic-regions-ip-address / geographic-regions-ip-header) = 4 parent + 8 get/put-configuration ЗАКРЫТЫ ЦЕЛИКОМ (АКТИВНЫЙ API без deprecated-баннера L89/L90; L85/L86 структурные twin'ы — parent ~25стр + get/put-configuration). L103 case b: env-api/rum НЕ переведён → anchor = aws-privatelink RU (L4R, тот же get/put-configuration twin, свежайший) + plugins-api L4N shared-object canon (Error «HTTP-код статуса»/«Список нарушений ограничений»/«Сообщение об ошибке», ConstraintViolation «-Возможные значения:» leading-dash, ConfigurationMetadata «Версия Dynatrace.»/«Отсортированный список номеров версий конфигурации.» ×2 нормализовано L4M, ErrorEnvelope `\| - \|` verbatim). Канон L99: title/H1×2/`* Reference`/`* Published` EN-verbatim; intro «The **X** API enables you to manage Y» → «API **X** позволяет управлять Y» (data-privacy RU precedent); feature-name `**Allowed beacon domains**`/`**Content resources**`/`**Geographic regions - …**` + UI-menu `**Settings > …**` EN-bold-lock (style-guide §UI); «beacon origins»/«CORS»/«Cross Origin Resource Sharing» EN technical-term (data-privacy «data privacy» EN precedent); object/enum/`**domainNamePattern**`/`**Origin**`/`**from**`/`**to**`/BeaconForwarder EN-lock; «The element can hold these values»→«Возможные значения:» с двоеточием env-leak 0; `## Validate payload`/`#### Curl` EN, внутри-секции переведены; card-link parent L4R канон `[### Просмотр конфигурации`/`[### Обновление конфигурации` + glue `](url "title")[### ` сохранён; `## Related topics`→`## Связанные темы`. **Related-topics + cross-ref link-текст = ФАКТИЧЕСКИЙ target RU H1 ДОСЛОВНО (L4O/L4L): все 10 целей digital-experience переведены → грепнуты, link-text = их `# `-H1 побуквенно (web «Настройка allowlist источников маяков…», mobile/custom варианты), title-attr переведён.** L101 период-по-источнику ПО КАЖДОМУ ФАЙЛУ (грепать EN-ячейку, НЕ копировать соседа): **allowed-beacon-cors put 400 С точкой «Сбой. Невалидный ввод.» + validate-204 «Успех. Переданная конфигурация валидна…» (EN «Success.»); content-resources/geographic×2 put 400 БЕЗ точки «Сбой. Невалидный ввод»; content-resources validate-204 «Validated. Переданная конфигурация валидна…» (EN «Validated.» EN-prefix L4I) vs geographic×2 «Успех.» (EN «Success.»)** — substring-replace `Failed. The input is invalid`→`Сбой. Невалидный ввод` сохраняет точку источника автоматически; GET 200 «Успех» без точки (EN «Success» без точки). 204-update «Успех. Конфигурация обновлена. Ответ без тела.» ×4. BOM `ï»¿` (3-char `\xef\xbb\xbf` НЕ U+FEFF, L4M) в `[GET all countriesï»¿]`/`[GET regions of the countryï»¿]` (geographic-ip-address get/put) вычищен → link-text EN, URL `dt-url.net` verbatim. Source-quirks L93 verbatim: «ManagedDynatrace for Government» (typo без пробела), double-space `.  Rules`/`.  Если`, «the first matching rules applies» (typo, рендер по смыслу). Splice `scripts/_build_rum_cfg.py` (CRLF→LF L4M + BOM-strip, EN→RU exact-string ⇒ line-parity + code-fence byte-identical авто). **Критич.ревью `scripts/_review_rum_cfg.py` (по образцу `_review_l4r.py` + L4P SUSPECT-substring scan): structural+force-sync+L101+SUSPECT 0 деф; 1 SUSPECT false-positive («IP address mapping» внутри bold feature-name) → review усилен исключением `**…**` EN-lock-spans (L4P-класс: SUSPECT обязан исключать EN-инвариантные spans как title/H1) → 0 деф; ПЕРЕВОД правок НЕ потребовал (5-й 0-с-первого подряд L4L/L4O/L4Q/L4R/L4S)** + семантик spot-check 6 файлов (parent + оба L101-варианта put + BOM-файл + 3 get: banner 0 ACTIVE, env-leak 0, colon OK, L101 оба варианта верны, shared canon byte-exact, Related=target-H1 дословно, BOM clean, code-fence byte-identical, **from**/**to** EN). diff +12 (1531→1543, pending 1124→1112), em-dash 0. **Lesson L4S: (1) L101 substring-replace `Failed. The input is invalid`→RU без хвостовой точки автоматически сохраняет period-state источника (точка вне match-span) — устойчивее покопийного per-file правила; (2) validate-204 «Validated.»-prefix vs «Успех.» РЕШАЕТСЯ ПО EN-ячейке файла (content-resources «Validated.» vs allowed-beacon/geographic «Success.» при идентичной структуре — L4I/L4Q подтверждён); (3) SUSPECT-scan обязан вырезать `**bold**` (feature/UI EN-lock) как уже вырезает title/H1 — иначе false-positive на легит. EN-feature-name (L4P-класс расширен); (4) env-api/rum не переведён → anchor свежайший config-api twin того же get/put-configuration вида (aws-privatelink L4R), НЕ старый data-privacy — но domain-проза-precedent (data-privacy «API **X** позволяет…») переиспользуется** | 12 | 12 | ✅ done |
| L4T | configuration-api/rum/application-detection-configuration/ parent + 8 endpoints (del-rule/get-all/get-host-detection-config/get-rule/post-rule/put-host-detection-config/put-rule/reorder-rules) ЗАКРЫТА ЦЕЛИКОМ — 9 файлов, **АКТИВНЫЙ API** без deprecated-баннера (L89/L90), продолжение rum/ начатого L4S. **L4S lesson применён: anchor = СВЕЖАЙШИЙ same-subsection twin (content-resources L4S RU + aws-privatelink L4R RU), НЕ старый conditional-naming L2R** (там pre-L99 канон «Элемент может принимать»/«Ошибка. Входные данные некорректны»/«## Валидация payload» — НЕ использовать). L103 case b: env-api/rum НЕ переведён. Domain corpus-доминанта (target RU H1 «Проверка правил обнаружения приложений» подтверждает): «application detection rule»→«правило обнаружения приложений»; feature-name `**Applications detection rules**` EN-bold-lock (L4S); intro «The **X** API enables you to manage Y»→«API **X** позволяет управлять Y» (L4S/data-privacy precedent). **Related-topics link-текст = ФАКТИЧЕСКИЙ target RU H1 ДОСЛОВНО (L4O/L4L): rum-overview→«Мониторинг реальных пользователей», application-detection-rules→«Проверка правил обнаружения приложений», define-your-applications→«Определение приложений для Real User Monitoring»; title-attr переиспользован из established corpus (грепнут).** Канон L99: title/H1×2/`* Reference`/`* Published Jan 08 2019` EN-verbatim; shared StubList/EntityShortRepresentation/Error/ErrorEnvelope/ConstraintViolation/ConfigurationMetadata(DtoImpl) verbatim из plugins-api L4N/content-resources L4S RU («Упорядоченный список кратких представлений сущностей Dynatrace.»/«Краткое представление сущности Dynatrace.»/«HTTP-код статуса»/«Список нарушений ограничений»/«Сообщение об ошибке»/«Метаданные для отладки»/«Версия Dynatrace.»/«Отсортированный список номеров версий конфигурации.» ×2 L4M-нормализовано); «The element can hold these values»→«Возможные значения:» с двоеточием env-leak 0; enum/object/`**pattern**`/`**order**`/`**name**`/`**description**` + example bold `**two**`/`**domain**`/`**contains**`/`**booking.easyTravel**` EN-lock; `## Validate payload`/`#### Curl` EN, внутри-секции переведены; **Example канон reports-api L4I/alerting-profiles L4J: `## Пример`/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`/`#### Результат`; image alt+caption `![POST example]`/`POST example` EN-verbatim (L4D); «из примера [POST request](…)»/«[GET all rules request]» link-text EN**; card-link parent L4R канон 8 карточек 2 группы (`[### Список всех правил`/`[### Просмотр правила`/…/`[### Просмотр заголовков определения хоста`) glue `](url "title")[### ` сохранён; `## Related topics`→`## Связанные темы`. **L101 период-по-источнику: ВСЕ 400 С точкой «Сбой. Невалидный ввод.» (post/put-rule/put-host/reorder EN все С точкой, substring-replace `Failed. The input is invalid` сохраняет точку авто L4S); GET 200 «Успех» без точки (EN «Success»); validate-204 РЕШЕНО ПО EN-ячейке: post-rule/put-rule EN «Validated.» → «Validated. Переданная конфигурация валидна. Ответ без тела.» (EN-prefix L4I) vs put-host-detection-config EN «Success.» → «Успех. Переданная…»; 204-update «Успех. Конфигурация обновлена. Ответ без тела.»; del-204 «Удалено. Ответ без тела.»; reorder-204 «Успех. Порядок правил обнаружения приложений изменён…»**. BOM `\xef\xbb\xbf` (3-char L4M) в `[create an application firstï»¿]`(get/post/put-rule applicationIdentifier) вычищен → link-text «сначала создайте приложение», URL verbatim. Source-quirks L93 verbatim-by-meaning: «the the **pattern**» (double-the), «host detection headers configuration» (double-noun). Splice `scripts/_build_appdetect.py` (CRLF→LF L4M + BOM-strip, EN→RU exact-string ⇒ line-parity + code-fence byte-identical авто). **Критич.ревью `scripts/_review_appdetect.py` (по `_review_rum_cfg.py` L4S): structural 0 деф, НО 1 деф пойман — COMMON substring-collision `Application detection rule.`(generic) применён ДО `The unique name of the Application detection rule.`(specific) → RU+EN ГИБРИД `name | The unique name of the Правило обнаружения приложений.` (L4N/L4P-класс «structural-green ≠ semantic», поймал leftover-EN-PROSE+SUSPECT-scan); fix = longest-first reorder (specific перед generic) → повторный 0 деф** + семантик spot-check всех 9 (parent card-glue intact, post-rule Example+image+validate, put-rule validate+bold-prose, put-host validate «Успех.»-variant, get-host ConfigurationMetadata twin, reorder StubList+shared canon, del-rule 2-col `\| Код \| Описание \|`+example, get-all/get-rule objects). em-dash 0, code-fence byte-identical, line-parity exact. diff +9 (1543→1552, pending 1112→1103, dynatrace-api 580→589 done/526→517 pending). **Lesson L4T: (1) anchor = СВЕЖАЙШИЙ same-subsection twin, НЕ старейший родственник того же домена даже при идентичной CRUD-структуре (conditional-naming L2R = pre-L99 канон, использование сломало бы консистентность с L4S content-resources sibling) — подтверждение L4S lesson-4; (2) COMMON substring-collision generic⊂specific («Application detection rule.» ⊂ «The unique name of the Application detection rule.») даёт RU+EN ГИБРИД — longest/most-specific-first ОБЯЗАТЕЛЬНО в COMMON (не только per-file), L4N/L4P подтверждён; structural+LEFTOVER-PROSE+SUSPECT поймал, semantic spot-check обязателен; (3) Example-section bold prose-emphasis на enum/field/value (`**two**`/`**domain**`/`**contains**`) = EN-lock как `**pattern**` — SUSPECT-scan уже вырезает `**bold**` L4S** | 9 | 9 | ✅ done |
| L4U | configuration-api/rum/mobile-custom-app-configuration/ parent + apps/ (get-all/get-app/post-app/put-app/delete-app) + key-user-actions/ (get/post/del-configuration) + user-action-and-session-properties/ (get-all/get-property/post-property/put-property/delete-property) = 14 файлов, **АКТИВНЫЙ API** без deprecated-баннера (L89/L90, `* Reference`/`* Published Nov 05, 2020`, нет `* Deprecated`), продолжение rum/ начатого L4S/L4T. **anchor = СВЕЖАЙШИЙ same-subsection twin = L4T application-detection-configuration RU + L4S content-resources RU (L4T lesson #1), shared объекты verbatim из L4T appdetect RU**. L103 case b: env-api/rum НЕ имеет mobile-custom-app twin (только geographic-regions/rum-js-code/rum-manual-insertion-tags/user-sessions/rum-cookie-names — проверено `ls`). **Domain corpus-доминанта (грепнута в managed-ru/): «custom application»→«пользовательское приложение» (40× vs 0 кастомн*); «user action»→«пользовательское действие» (619× vs 80); «Instrumentation Wizard»→«мастер инструментирования» (L4K mobile-symbolication corpus «в мастере инструментирования», 6×); «endpoint»→«эндпоинт» (rum/plugins 42×); «request attribute»→«атрибут запроса» (54× vs 15 EN); «Session Replay» EN (348× corpus + style-guide product-lock, lowercase «session replay» prose тоже→Session Replay); «beacon» EN-lock (L4S beacon domains/origins/cors все EN → «beacon-эндпоинт»); «Apdex» EN (CLAUDE.md tech-term); `**tolerable**`/`**frustrated**`/`**origin**`/`**beaconEndpointType**` bold EN-lock (style-guide §UI + L99, L4S SUSPECT-exclusion); «opt-in mode»→«режим opt-in»; «cleanup rule»→«правило очистки»; «aggregation»→«агрегация».** Канон L99: title/H1×2/`* Reference`/`* Published Nov 05, 2020` EN-verbatim; shared StubList/EntityShortRepresentation/Error/ErrorEnvelope/ConstraintViolation verbatim из L4T appdetect RU («Упорядоченный список кратких представлений…»/«Краткое представление сущности Dynatrace.»/«HTTP-код статуса»/«Список нарушений ограничений»/«Сообщение об ошибке»); object-header `#### The \`X\` object`→`#### Объект \`X\`` (9 новых domain-объектов MobileCustomAppConfig/NewMobileCustomAppConfig/MobileCustomApdex/KeyUserActionMobile(List)/MobileSessionUserActionProperty(List/Short/Upd)); «The element can hold these values»→«Возможные значения:» с двоеточием (вкл. leading-dash `-Возможные значения:` в ConstraintViolation.parameterLocation, env-leak «Элемент может принимать» 0); enum-значения в backticks EN; `**Deprecated**.`→`**Устарело**.` field-level marker sessionReplayOnCrashEnabled (L4B/L4G: перевод+bold, НЕ API-баннер); `## Validate payload` EN (ALLOWED_EN, нет `#### Curl`/Example в этом батче), внутри-секции `### Аутентификация`/`### Ответ`/`#### Коды ответа` переведены; combined-block card parent 13 карточек 4 группы glue `](url "title")[### ` сохранён; `## Related topics`→`## Связанные темы`. **Related-topics link-текст = ФАКТИЧЕСКИЙ target RU H1 ДОСЛОВНО (L4O/L4L, все 3 target переведены — грепнуто): delete-application-mobile→«Удаление мобильного приложения», delete-application-custom→«Удаление пользовательского приложения», rum-concepts/user-actions→«Пользовательские действия»; title-attr переведён по corpus-шаблону.** **L101 период-по-источнику: ВСЕ 400 `Failed. The input is invalid` источник С точкой → substring-replace сохраняет точку авто (L4S, post/put-app/post/put-property); ВСЕ 404 `Failed. The specified entity doesn't exist` substring (период по источнику = все С точкой) → «Сбой. Указанная сущность не существует»; validate-204 РЕШЕНО ПО EN-ячейке: источник «Success. The submitted configuration is valid.» (НЕ «Validated.») → «Успех. Переданная конфигурация валидна. Ответ без тела.» (НЕ Validated.-prefix, L4S/L4T by-EN-cell); 3-col `\| Success \|`→`\| Успех \|` без точки; 201/204 full-cell «Успех. X создано/удалено/обновлено. Ответ содержит…/Ответ без тела.»; 409 «Сбой. applicationId уже используется…»/«Сбой. Достигнуто максимальное число…».** BOM `\xef\xbb\xbf` (3-char L4M) в `[regular expressionï»¿]` (cleanupRule cell get/post/put-property) вычищен → link-text «регулярное выражение», URL `dt-url.net/k9e0iaq` verbatim. Source-quirk L93 verbatim-by-meaning: «Get parameters of a session property its ID.» (parent, missing «by»). Splice `scripts/_build_mobilecustomapp.py` (CRLF→LF L4M + BOM-strip, EN→RU exact-string ⇒ line-parity + code-fence byte-identical авто; 1 build-итерация: пропущено standalone-правило parent heading `[### Create a user session property` строка 42 — combined-block покрыл только end-of-line `[### NextTitle`, добавлено отдельным правилом, +benign-MISS `[### View an app` уже покрыт combined-block убран). **Критич.ревью `scripts/_review_mobilecustomapp.py` (по `_review_appdetect.py` L4T + L4P SUSPECT-substring, check #12 уточнён: field-level `**Устарело**.` НЕ флагать как API-баннер, только standalone/`Этот API устарел`): structural+force-sync+L101+SUSPECT 0 деф С ПЕРВОГО ПРОГОНА** + семантик spot-check (post-app object+validate+ConstraintViolation, get-app `**Устарело**`-marker+shared-canon, get-property BOM-clean+origin-verbatim-source+request-attribute, delete-app Related=target-H1, post-configuration 409+200, parent 13 card-glue) — env-leak 0, colon все, leftover-EN-prose 0, session-replay-lowercase 0, нет кальки «кастомн*», JSON byte-identical 14/14, line-parity exact 14/14, em-dash 0. **Правок ПЕРЕВОДА не потребовалось (6-й 0-с-первого подряд: L4L/L4O/L4Q/L4R/L4S/L4U; L4T имел 1 пойман-фикс).** diff +14 (1552→1566 = 58.98%, pending 1103→1089, dynatrace-api 589→603 done/517→503 pending, Orphan RU 0). **Lesson L4U: (1) combined-block card-splice покрывает только `](url "title")[### NextTitle` (end-of-line heading) — standalone heading на line-start (parent group-первый: `[### List all apps`/`[### Create a user session property`) нужны ОТДЕЛЬНЫЕ правила, иначе пропуск (build-итерация поймала по MISS-счётчику + чтению parent); benign-MISS = правило на строку уже покрытую combined-block, убирать; (2) ACTIVE-API review check «no deprecated banner» обязан различать field-level `**Устарело**.` (L4B/L4G легит, sessionReplayOnCrashEnabled) vs API-баннер — иначе false-positive (уточнено: флагать только `Этот api устарел`/standalone `\nустарело\n`); (3) validate-204 в этом батче EN «Success.» (НЕ «Validated.») → «Успех.»-prefix, по EN-ячейке L4S/L4T — rum/-семейство неоднородно (content-resources L4S «Validated.», mobile-custom-app L4U «Success.»); (4) source verbatim-by-meaning L93: «session property its ID» (missing «by») рендерим по смыслу «по его ID».** | 14 | 14 | ✅ done |
| L4V | configuration-api/rum/web-application-configuration-api/ parent + data-privacy/5 (get-all-web-apps/get-default-app/get-web-app/put-default-app/put-web-app) + error-rules/2 (get/put-configuration) + key-user-actions/3 (del/get/post-configuration) = 11 файлов, **АКТИВНЫЙ API** L89/L90 (`* Reference`/`* Published Jan 24 2019`/`Sep 03 2019`/`Sep 24 2020` EN-verbatim, без `* Deprecated`), продолжение rum/ L4U. anchor = L4S content-resources RU (get/put-configuration twin: shared ErrorEnvelope/Error/ConstraintViolation вербатим, «Сбой. Невалидный ввод» БЕЗ точки = rum/-family ≠ L101-aws-с-точкой; «Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.») + L4U mobile-custom-app key-user-actions twin (del/get/post-configuration). EntityShortRepresentation/ConfigurationMetadata вербат L4G k8s-anchor. DataPrivacy-объекты (ApplicationDataPrivacy/SessionReplay*/MaskingRule) faithfully — env-api twin'а нет (L103 case b). title/H1×2/`* Reference`/`* Published` EN; `The element can hold`→`Возможные значения:` с двоеточием (вкл. leading-dash, env-leak 0); `## Validate payload` EN ALLOWED_EN («Validated.» EN-вербат L4E); BOM ï»¿ вычищен inline-link, dt-url.net URL EN; Session Replay/Davis AI/Apdex EN-lock; Related-topics link = target RU H1 дословно («Пользовательские действия»/«Настройка обнаружения ошибок для веб-приложений»); parent combined-block glue 7/7. **DEFER L42 → закрыто в L4W:** default-application/ + web-application/. **Lesson L4V:** (1) Write-tool добавляет trailing `\n` → RU +1стр vs EN (канон-twin EN==RU БЕЗ trailing-nl) — критревью поймал LINES-mismatch, фикс Python `b[:-1]`, strip-trailing-nl в пост-Write чек-лист; (2) rum/-family 400-канон = ближайший same-subsection twin L4S «Сбой. Невалидный ввод» без точки, НЕ by-family L101-aws с точкой; (3) EN-typo несбаланс-backtick `(`false)` зеркалить структурно. 0 деф structural+semantic после фикса trailing-nl (запись задним числом — Status-строка пропущена в сессии L4V, восстановлена в L4W). | 11 | 11 | ✅ done |
| L4W | configuration-api/rum/web-application-configuration-api/ **DEFER-completion (L42)**: default-application/2 (get-configuration 1388 / put-configuration 1589) + web-application/5 (del 44 / get-all 126 / get 1392 / post 1621 / put 1623) = 7 файлов, 7783 EN-строк. **→ web-application-configuration-api/ subsection 100% ЗАКРЫТА (L4V 11 + L4W 7 = 18ф).** **АКТИВНЫЙ API** L89/L90 (`* Reference`/`* Published Sep 03, 2019`/post `* Updated on Aug 18, 2025`, без `* Deprecated`). **Splice-twin L85/L86: `WebApplicationConfig` гигант + ~40 sub-объектов + JSON-модель (стр ~47-1392) БАЙТ-ИДЕНТИЧЕН get-web-application↔default/get-configuration (GET-twins) и post↔put-web-application↔default/put-configuration (POST/PUT-twins) → переведён ОДИН раз в COMMON (~200 field-desc) → splice в 5 крупных twin-файлов при near-zero marginal cost (L42 «big files» решается splice'ом, не дроблением).** anchor = СВЕЖАЙШИЙ same-subsection twin = L4V web-application-configuration-api RU (error-rules/key-user-actions/parent) + L4U mobile-custom-app shared-object canon (L4T lesson #1). L103 case b: env-api/rum web-application twin'а нет. Канон L99: title/H1×2/`* Reference`/`* Published`/`* Updated on` EN-verbatim; `The element can hold these values`→`Возможные значения:` с двоеточием (env-leak 0); `## Validate payload`/`#### Curl` EN ALLOWED_EN, внутри-секции переведены; validate-204 «Validated. Переданная конфигурация валидна. Ответ без тела.» (EN-cell «Validated.» L4I); 400 «Сбой. Невалидный ввод.» С точкой (L101 substring, EN с точкой); **bare GET-200 `\| Success \|`→`\| Успех \|` (L4V canon error-rules/key-user-actions/data-privacy)**; shared Error/ErrorEnvelope/ConstraintViolation/EntityShortRepresentation/StubList/ConfigurationMetadata вербатим L4U/L4V/L4M. Domain corpus-dom: «web application»→«веб-приложение» (73+44×), «conversion goal»→«цель конверсии», «user action»→«пользовательское действие» (L4U 619×), «user session»→«пользовательская сессия», «Real user monitoring settings.»→«Настройки мониторинга реальных пользователей.», «X enabled/disabled.»→«X включён/отключён.» (gender-agree by subject), «placeholder»→«плейсхолдер» (9× vs 0), «IP address»→«IP-адрес» (95×), «regular expression»→«регулярное выражение» (L4U), «subnet mask»→«маска подсети»; Session Replay/Apdex/Davis AI/CDN/CORS/RUM/JavaScript/AWS Lambda/W3C/SameSite/jQuery/AngularJS EN-lock, `**field**`/enum-backtick EN-lock (L4S SUSPECT-exclusion); Related-topics link-текст = target RU H1 дословно («Удаление веб-приложения» L4O/L4L). Source-quirk L93 verbatim-by-meaning: «Analize» (typo, *X* сохранён), «noting specified» (typo), «MATCHES_REGULAR_ERPRESSION» (typo в operand2), «applicationâ's»/«serverâ's» (mojibake apostrophe). Splice `scripts/_build_webappcfg.py` (CRLF→LF L4M + BOM-strip + **mojibake-apostrophe `â\x80\x99` normalize→`'` в build() ПЕРЕД заменами**, EN→RU exact-string ⇒ line-parity + code-fence byte-identical авто; per-file MISS 0). **Критич.ревью `scripts/_review_webappcfg.py` (по `_review_mobilecustomapp.py` L4U + L4P SUSPECT + НОВЫЙ check #14 bare-200-guard): structural 0 деф, НО 2 review-iter — поймано-фикс: (a) mojibake `â\x80\x99` в libraryFileLocation/serverRequestPathId (MOJIBAKE+LEFTOVER-EN) → build-normalize; (b) self-added em-dash «Рекомендуемое значение… — 3» (EN «is 3» без тире, CLAUDE#0) → «равно 3»; (c) 3-word EN-run «same site cookie» (SUSPECT) → «Атрибут cookie SameSite»; (d) missing «This is a model of the request body» canon (SUSPECT) → добавлен L4V; semantic spot-check поймал (e) bare `\| Success \|`→`\| Успех \|` (L4V canon, ОДНО слово ⇒ SUSPECT/leftover MISS — explicit guard добавлен) → итог 0 деф structural+semantic.** Семантик spot-check 7/7 (del Related=target-H1, get-all StubList, WebApplicationConfig+MonitoringSettings обж, post codes+validate+ErrorEnvelope, default-put twin-вариант). diff +7 (1577→1584 = 59.66%, pending 1071, dynatrace-api 614→621 done/492→485 pending, Orphan RU 0, source-check 0). **Lesson L4W:** (1) mojibake-apostrophe `â\x80\x99` (UTF-8-as-Latin1 для ’) в EN-ячейках — splice EN-string либо точные байты, либо нормализовать в build() ПЕРЕД заменами (выбрано normalize, robust против любых пропущенных); (2) bare single-word `\| Success \|`→`\| Успех \|` = L4V canon, ОДНО слово ⇒ SUSPECT(≥3-run)/leftover-EN структурно MISS ⇒ explicit per-cell review-guard ОБЯЗАТЕЛЕН (L4N/L4T «structural-green≠semantic» подтверждён 3-й раз, semantic spot-check поймал); (3) self-added em-dash из вольного перевода («is 3»→«— 3») — review EM-DASH-check (CLAUDE#0) держит; (4) splice одного гигантского shared-объекта 1× закрывает 5 крупных twin-файлов (7783 EN-строк) — L42 «big files separate session» = делать splice'ом в выделенной сессии, НЕ дробить subsection. | 7 | 7 | ✅ done |
| L4X | configuration-api/calculated-metrics/service-metrics/ = 7 файлов (parent + del-calculated-metric + get-all + get-calculated-metric + json-models 932 + post-calculated-metric 767 + put-calculated-metric 798). **→ calculated-metrics/ subsection 100% ЗАКРЫТА (L4O 19 + L4X 7 = 26ф; L4O-deferred L42 service-metrics закрыт splice'ом в выделенной сессии как L4W).** **АКТИВНЫЙ API** L89/L90 (`* Reference`/`* Published` EN-verbatim, без `* Deprecated`; rum-metrics RU twin подтверждает). **anchor = SAME-subsection L4O calculated-metrics RU** (service-строки уже отгружены в top-parent calculated-metrics.md: «вычисляемая метрика сервиса»/«метрик сервиса» genitive-sing.) + k8s/config shared (StubList/EntityShortRepresentation/Error/ErrorEnvelope/ConstraintViolation/ConfigurationMetadata вербатим L4O/L4M/L4U). **json-models СТРУКТУРА = conditional-naming L3G паттерн** (единственный json-models прецедент; L4O не имел json-models): Variations-intro «Некоторые JSON-модели API **X** различаются…», «Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models](url "title")», «Список фактических объектов см. в описании поля **type**…», `Parameters`/`JSON model` tab-labels EN, `### BOOLEAN`-type-headings EN, `XComparisonInfo`/`XDto` object-names EN — **НО headers + `Возможные значения:` (с двоеточием, НЕ L3G «Элемент может принимать») + EN-locks = L4O/L99** (двойной anchor: structural-prose от json-models-прецедента L3G, canon-elements от same-subsection L4O). Канон L99: title/H1×2/`* Reference`/`* Published` EN-verbatim; `## Validate payload`/`#### Curl` EN ALLOWED_EN, внутри-секции (`### Аутентификация`/`### Ответ`/`#### Коды ответа`) переведены; validate-204 «Validated. Переданная конфигурация валидна. Ответ без тела.» (EN-cell «Validated.» L4I); **400 «Сбой. Невалидный ввод» БЕЗ точки (L101: EN «Failed. The input is invalid» БЕЗ точки → substring-replace сохраняет авто; ПРОТИВОПОЛОЖНО L4W rum/web-app С точкой при идентичной структуре — грепать EN-ячейку КАЖДОГО subsection, НЕ копировать соседний batch)**; bare `\| Success \|`→`\| Успех \|` (L4W canon explicit guard). Example канон reports-api L4I/alerting-profiles L4J: `## Пример`/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`, `#### Curl` EN, «API-токен передаётся в заголовке **Authorization**.»/«Результат усечён до двух записей.»; `[POST request example]` link-text EN (L4T), title-attr переведён. Domain L4O corpus-dom: «calculated service metric»→«вычисляемая метрика сервиса», «service metric(s)»→«метрика/метрик сервиса» (genitive «сервиса» sing., L4O top-parent shipped — НЕ bare-generic rule, рендерится ТОЛЬКО внутри полных предложений/ячеек L4T longest-first ⇒ 0 hybrid); object/enum/`**field**`/`### TYPE`-headings/`XComparisonInfo` EN-lock. Related-topics link-текст = target RU H1 дословно («Вычисляемые метрики для сервисов»/«Многомерный анализ» L4O/L4L), title-attr переведён. Source-quirk L93 verbatim-by-meaning: `api-path`-артефакт EN сохранён, del-204 EN «the update was successful» (в delete-доке) → faithfully «обновление прошло успешно», `.This`→`.Эта` no-space зеркалим, markdown-escaped `'ESB\_INPUT\_NODE\_TYPE'` (НЕ `'ESB_INPUT_NODE_TYPE'`) escape сохранён. mojibake `â\x80\x{93,98,99}` (–/'/' double-encoded в UniversalTag/TagInfo «Itâs»/«colon â:â»/«not set â those») нормализован **codepoint-точно** `chr(0xE2)+chr(0x80)+chr(0xNN)` в build() ПЕРЕД заменами (L4W); BOM `ï»¿` strip L4M. Splice `scripts/_build_servicemetrics.py` (EN→RU exact-string ⇒ line-parity + code-fence byte-identical авто; per-file MISS 0). **Критич.ревью `scripts/_review_servicemetrics.py` (по `_review_calcmetrics.py` L4O + force-sync fence + line/heading/fence/table parity EXACT + em-dash + mojibake/BOM + SUSPECT-substring + no-old-env-canon + colon-guard + EN-инварианты): structural+force-sync 0 деф (fence byte-identical 0 force-sync), НО 1 review-iter — SUSPECT поймал leftover-EN «Type-specific comparison»/«inherits fields from the parent model» (R-key имел `'ESB_INPUT_NODE_TYPE'` вместо markdown-escaped `'ESB\_INPUT\_NODE\_TYPE'` → no-match) → fix `\\_` в Python-литерале → повторный 0 деф structural+semantic.** Семантик spot-check 7/7 (parent card-glue+Related=target-H1, del Example+204+«обновление прошло успешно», get-cm CalculatedServiceMetric катало+`Возможные значения:`+enum EN-lock, json-models Variations+UniversalTag-mojibake-clean+ESB escaped, post 400-без-точки+Validate-payload-EN+ErrorEnvelope, put twin-204). diff +7 (1584→1591 = 59.92%, pending 1064, dynatrace-api 621→628 done/485→478 pending, Orphan RU 0, source-check 0). **Lesson L4X:** (1) splice-builder fragile-char (mojibake/BOM) keys ОБЯЗАНЫ строиться из codepoints `chr(0xE2)+chr(0x80)+chr(0xNN)` — литералы коллапсируют при Write/Edit (typed `â\x80\x99` → single `â`); L4W `txt.replace("â","'")` оставил бы C1-хвост, нужен FULL 3-char unit; (2) markdown-escaped enum в ПРОЗЕ `'ESB\_INPUT\_NODE\_TYPE'` (≠ `'ESB_INPUT_NODE_TYPE'` в `**bold**`/cells) — R-key ДОЛЖЕН включать `\_` (Python `\\_`); SUSPECT поймал (structural-green≠semantic 4-й раз L4N/L4P/L4T/L4W); (3) L101 период РЕШАЕТСЯ ПО EN-ячейке КАЖДОГО subsection — calculated-metrics/service «Failed. The input is invalid» БЕЗ точки vs L4W rum/web-app С точкой идентичная структура (грепать, НЕ копировать соседний batch — L4Q подтверждён); (4) json-models = двойной anchor (structural-prose от json-models-прецедента L3G + canon-elements `Возможные значения:`/headers/EN-lock от same-subsection L4O, НЕ L3G «Элемент может принимать») — L4T lesson #1 (anchor=свежайший same-subsection) уточнён: structural-pattern может браться от типового прецедента др. subsection, но canon-elements ВСЕГДА same-subsection/newest; (5) L4O-deferred L42 subsection закрыт splice'ом 1 build-iter+1 review-iter, calculated-metrics/ ПОЛНОСТЬЮ закрыт. | 7 | 7 | ✅ done |
| L4Y | environment-api/rum/ = 24 файла: geographic-regions parent+5 (get-cities-country/get-cities-region/get-countries/get-regions-country/get-regions) + real-user-monitoring-javascript-code parent+7 (get-available-rum-javascript-versions/get-configured-rum-javascript-versions/get-current-version/get-list-injected-applications/get-most-recent-version/get-snippet-async/get-snippet-sync) + rum-cookie-names-get-cookie-names + rum-manual-insertion-tags parent+4 (get-inline-code/get-javascript-tag/get-oneagent-javascript-tag/get-oneagent-javascript-tag-with-sri) + user-sessions parent+3 (table/tree/user-session-structure). ~3688 EN-строк. **rum/ subsection ЗАКРЫТА ЦЕЛИКОМ.** **АКТИВНЫЙ API** L89/L90 (`* Reference`/`* Updated on May 02, 2022`/`* Published`, без `* Deprecated`). **ПЕРВЫЙ L4-era env-api batch.** **Anchor-решение (L103 + L4S lesson #4 + L4T lesson #1 распространены на env-api): env-api корпус pre-L99 НЕ-консистентен (events-v2 L3M = translated title/H1 + «Элемент может принимать значения»; SLO-classic L3V = title EN но `* Справочник`/`* Обновлено`) → anchor = СВЕЖАЙШИЙ L99, НЕ старый pre-L99 env-api родственник; env-api domain-проза-precedent (events-v2 RU) переиспользуется ТОЛЬКО где не конфликтует с L99; корпус мигрирует к L99, новые batches = newest canon.** Канон L99: title/H1×2/`* Reference`/`* Updated on`/`* Published` EN-verbatim (отличие от ВСЕГО прежнего env-api корпуса — документированное решение). shared Error/ErrorEnvelope/ConstraintViolation вербатим = L4S/events-v2 RU canon («HTTP-код состояния»/«Список нарушений ограничений»/«Сообщение об ошибке», ConstraintViolation intro «Список нарушений ограничений», bare `-` cells, `parameterLocation` `-Возможные значения:` leading-dash+двоеточие, ErrorEnvelope `\| - \|`). env-api domain-проза (events-v2 RU precedent, не конфликт с L99): «Запрос возвращает данные в формате `application/json`./`text/plain`.»/«## Аутентификация»/«Для выполнения запроса необходим access token со scope `X`.»/«О том, как получить и использовать токен, см. [Tokens and authentication](url).» (link-text EN corpus 188:40 L87/L4S)/«## Параметры» header `\| Параметр \| Тип \| Описание \| Где \| Обязательный \|` cells `path`/`query`/`Required`/`Optional`/типы EN/«Запрос не предоставляет настраиваемых параметров.»/«## Ответ»/«### Коды ответа» `\| Код \| Тип \| Описание \|`/«Ошибка на стороне клиента.»/«Ошибка на стороне сервера.»/«### Объекты тела ответа»/«### JSON-модели тела ответа»; object-header `#### The \`X\` object`→`#### Объект \`X\``. `The element can hold these values`→`Возможные значения:` с двоеточием (НЕ pre-L99 «Элемент может принимать»), env-leak 0. Example канон reports-api L4I: `## Пример`/`#### Curl` EN ALLOWED_EN/`#### URL запроса`/`#### Тело ответа`/`#### Код ответа`, «API-токен передаётся в заголовке **Authorization**.»/«Результат усечён до N записей.». **L101 период-по-источнику substring-replace `Success`/`Success.`/`Failed. The X is …` сохраняет точку источника авто** (199 «…никогда не возвращается.» С точкой, 200 «Успех. Ответ содержит…» С точкой, 400 «Сбой. Запрос отсутствует.», bare `Success`→`Успех` БЕЗ точки). **Related-topics link-текст = target RU H1 ДОСЛОВНО (L4O/L4L, грепнуто): rum-overview→«Мониторинг реальных пользователей», detection-of-ip→«Определение IP-адресов, геолокаций и user agent'ов», custom-queries-segmentation→«Пользовательские запросы, сегментация и агрегация данных сессий»; title-attr переведён. Inline/cross-ref link-text по corpus-dominance EN-lock: `[Tokens and authentication]` (188:40), snippet-format-names `[JavaScript tag]`/`[OneAgent JavaScript tag]`/`[OneAgent JavaScript tag with SRI]`/`[inline code]`/`[code snippet]` (7/5/5/5/4 EN:минор RU), `[RUM manual insertion tags API]`/`[Real User Monitoring JavaScript API]` = target-parent-H1 EN-verbatim per L99, endpoint-name `[GET the list of manually injected applications]`/`[GET regions of the country]` EN (ячейка-проза переведена), USQL/`User Session(s) Query Language` EN-lock corpus 165:0. Descriptive-prose-bullet link-text ПЕРЕВЕДЁН (style-guide §Links, ≠ target-H1-cross-ref): `[безагентный мониторинг]` (corpus 2:1)/`[Ручное внедрение для страниц приложения с автоматической инжекцией]`.** Domain: «user session»→«пользовательская сессия», «user action»→«пользовательское действие», «application»→«приложение», «browser»→«браузер», «country/region/city»→«страна/регион/город», «bounce»→«отказ», «rage click/tap»→«rage-клик/тап»; Synthetic/Session Replay/OpenKit/Apdex/RUM/JavaScript/USQL/CLS/FID/LCP/«Total blocking time»/«first contentful paint»/«time to interactive» EN-lock; `~~totalBlockingTime~~` strikethrough + field-marker `DEPRECATED`→`УСТАРЕЛО` (L4B/L4G, faithful source-render — FID/totalBlockingTime документированы в Dynatrace-источнике, НЕ editorialize по CLAUDE FID→INP: это перевод чужого источника, не наш authored-контент). BOM `ï»¿` (3-char L4M) в inline-link-text вычищен ([USQL documentation page]/[GET the list of manually injected applications]/[GET regions of the country]…), URL `dt-url.net` verbatim. Source-quirk L93 verbatim-by-meaning: «ManagedDynatrace for Government» (no-space typo), double-space/`.In the example` (no-space-after-period), «the of time between» (table.md), `GdaÅsk` mojibake ВНУТРИ JSON code-fence byte-verbatim (НИКОГДА не трогать fence). U+2014 double-encoded `\xe2\x80\x94` в ПРОЗЕ user-sessions.md/tree.md («columns—a flat list»/«"leaves"—selected fields») нормализован→ естественный RU с двоеточием. Splice `scripts/_build_rumenv.py` (CRLF→LF L4M + 3-char BOM-strip + MOJI codepoint-normalize L4X, EN→RU exact-string ⇒ line-parity + code-fence byte-identical авто; write `newline=''` БЕЗ trailing-nl L4V). 24 файла (1 delegation-omission: spec-list дан как 23, get-javascript-tag.md выпал → subagent поймал «spec says 24 but enumerated 23» → добавлен build-iter 2). **Критич.ревью `scripts/_review_rumenv.py` (по `_review_servicemetrics.py` L4X + НОВЫЙ generic LATIN-RUN scanner: strip fences/`**bold**`/`` `code` ``/links/EN-invariant-lines/ALLOWED_EN → flag ≥4-Latin-word residue): structural+force-sync+L101 0 деф; SUSPECT+LATIN-RUN поймали 4 РЕАЛЬНЫХ деф из 15 flags (11 verified false-positive = link-text-EN-per-canon)**: (a/b) get-snippet-async.md/get-snippet-sync.md entity-cell EN-leak (EN-string byte-identical в 3 файлах: get-current-version переведён, async/sync НЕТ — COMMON-coverage miss L4T-класс «shared string не в COMMON») → fix move entity-cell→COMMON (longest-first, byte-identical 3/3 verified); (c) parent:15 `[Agentless monitoring]`→`[безагентный мониторинг]` (corpus 2:1 RU, descriptive-prose-bullet ≠ target-H1 → style-guide §Links); (d) parent:16 `[Manual insertion for pages…]`→перевод (parallel-bullet consistency) → re-run → review **[OK] 0 деф** (refined ENLOCK с verified EN-lock terms L4S#3: target-parent-H1-EN + format-names + USQL-name). Семантик spot-check 6 файлов (user-session-structure 67-field UserSession+8 sub-obj+deprecated+WebVitals, table USQL-params+Example+JSON, get-countries shared-obj byte-exact, geographic-regions parent card-glue+Related=target-H1, get-javascript-tag, get-oneagent-js-with-sri link-text-EN-corpus) — env-leak 0, colon все, no fabrication/drop, faithful, em-dash 0, code-fence byte-identical, line-parity EXACT 24/24. diff +24 (1591→1615 = **60.83%**, pending 1064→1040, dynatrace-api 628→652 done/478→454 pending, Orphan RU 0, source-check 0). **Lesson L4Y:** (1) **ПЕРВЫЙ L4-era env-api: env-api корпус pre-L99 НЕ-консистентен (events-v2 L3M translated-title/«Элемент может принимать»; SLO-classic L3V `* Справочник`/`* Обновлено`) → anchor = freshest L99 (L4S#4/L4T#1 chain «свежайший НЕ старый родственник» распространён с config-api на env-api) + env-api domain-проза reused где не конфликт с L99; корпус мигрирует к L99**; (2) **delegation-brief omission: 24-list дан как 23 → subagent поймал «count≠enumerated» — ВСЕГДА сверять file-count vs enumerated list ПЕРЕД delegation + пробрасывать `grep -c _pending.txt` ground-truth**; (3) **generic LATIN-RUN scanner (strip EN-lock-spans→≥4-word residue) поймал entity-cell EN-leak что byte-identical-scan ПРОПУСТИЛ (BOM-strip→EN≠RU, prose untranslated)** — curated SUSPECT-list недостаточен, generic stripped-Latin-run net ОБЯЗАТЕЛЕН (L4P/L4S «structural≠semantic» 5-й раз подтверждён + расширен: generic scanner > hand-list); (4) **descriptive-prose-bullet link-text (parent intro `* [X](url) and`, link-text≠target-page-H1) = TRANSLATE (style-guide §Links + corpus-dominance), ОТЛИЧАТЬ от Related-topics/cross-ref link-text=target-RU-H1 (L4O/L4L)** — два правила для двух link-классов; (5) **link-text=target-parent-H1: H1 EN-verbatim per L99 ⇒ link-text на parent тоже EN-verbatim; review ENLOCK обязан включать verified target-H1-EN + corpus-dominant format-names + USQL-language-name (L4S#3 «scanner вырезает EN-lock-spans»)**; (6) **faithful source-render: FID/totalBlockingTime в Dynatrace-источнике → переводим как есть, НЕ editorialize по CLAUDE-правилу FID→INP (перевод чужого источника ≠ наш authored-контент)**. | 24 | 24 | ✅ done |
| L4Z | environment-api/topology-and-smartscape/ = 21 файл: applications-api (get-all/get-an-app/get-baseline/post-tags) + custom-device-api (create-custom-device-via-dynatrace-api/report-custom-device-metric-via-rest-api) + hosts-api parent+4 (del-tags/get-a-host/get-all/post-tags) + process-groups-api parent+3 (get-all/get-a-process-group/post-tags) + processes-api (get-all/get-a-process) + services-api (get-all/get-a-service/get-baseline/post-tags). ~19357 EN-строк. **topology-and-smartscape/ subsection ЗАКРЫТА ЦЕЛИКОМ** (21 = полный остаток, ground-truth `_pending.txt`; sub-parents applications/services/processes/custom-device-api.md в EN отсутствуют, top parent уже RU). Продолжение env-api L4-era после L4Y. **DEPRECATED API** (`* Deprecated` bullet + «This API is deprecated. Use [Monitored entities API] instead.»). **Anchor = СВЕЖАЙШИЙ same-subsection parent `topology-and-smartscape.md` RU (уже переведён, сильнейший per L4T#1)** + L4Y env-api L99 canon + shared Error/ErrorEnvelope/ConstraintViolation вербатим из L4Y rum RU (`docs/managed-ru/.../rum/geographic-regions/get-countries.md`, та же env-api семья 0-деф). **Deprecated-handling: KEEP `* Deprecated` bullet EN-verbatim (НЕ дропать — ОТЛИЧИЕ от L3T/L3U v1-banner-drop; same-subsection parent RU держит bullet ⇒ anchor=same-subsection-parent приоритетнее by-family v1-правила, L4T#1 расширен на deprecated-axis)** + проза «Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.» (link-text EN, title-attr переведён, EXACT из parent RU). get-baseline applications/services: источник БЕЗ deprecated-prose (только bullet) → banner COMMON не матчит, bullet EN сохранён, прозу НЕ фабриковать (faithful: отсутствие баннера зеркалится отсутствием). Канон L99/L4Y: title/H1×2 EN-verbatim (API-names «Applications API - GET all apps»/«Hosts API»/«Processes API - GET all processes»); `* Reference`/`* Updated on Mar 22, 2023` EN-verbatim; `The element can hold these values`→`Возможные значения:` с двоеточием; env-api domain-проза из L4Y («Запрос возвращает данные в формате `application/json`.»/POST «Запрос принимает данные…»/«## Аутентификация»/«Для выполнения запроса необходим access token со scope `DataExport`.»/«[Tokens and authentication]» EN/headers/«## Ответ»/«### Коды ответа»/«Ошибка на стороне клиента./сервера.»/«### Объекты тела ответа»/«### JSON-модели тела ответа»); `#### The X object`→`#### Объект X`; `## Response headers`→`## Заголовки ответа`; `### Request body objects`→`### Объекты тела запроса`; UpdateEntity body + «Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.» (L4V/L4Y); Example reports-api L4I (`## Пример`/`#### Curl` EN/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`, «API-токен передаётся в заголовке **Authorization**.»/«Результат усечён до N записей.»). **Twin-splice L4W-паттерн в масштабе ~19.4K строк:** get-all↔get-a-X byte-identical object-element-description STRINGS (ProcessGroupInstance/Host/Service/Application/AgentVersion/MonitoringState/TechnologyInfo/TagInfo/ProcessGroupInstanceModule/EntityShortRepresentation) → COMMON exact-string 1× применяется к обоим offset-независимо; 4× post-tags (UpdateEntity) near-identical; get-baseline applications↔services twins. Reuse проверенного `_build_rumenv.py` env-api COMMON (0-деф L4Y). L101 substring-replace сохраняет точку источника авто (204 «Успех. Параметры приложения/хоста/сервиса/группы процессов обновлены.» С точкой; 400 «Сбой. Невалидный ввод.» С точкой; bare `Success`→`Успех`; грепать EN-ячейку КАЖДОГО файла L4X#3). Related-topics link-текст = target RU H1 дословно (L4O/L4L; resolved observe/hosts H1 `# Hosts` EN → link-text EN, observe/process-groups `# Process groups` EN); endpoint/API-name link-text EN (`[Monitored entities API]`/`[Custom tags API]`/`[Timeseries API v1 - PUT a custom metric]`/`[Report custom device metric via REST API]`/`[Create custom device via the Dynatrace API]` corpus-dominant, ячейка-проза переведена); descriptive-prose link-text переведён (`[приложений]`/`[процессов]`/`[пользовательские теги]` L4Y#4). Domain: process→процесс, process group→группа процессов, host→хост, service→сервис, application→приложение, entity→сущность, baseline→базовая линия, pagination→постраничная разбивка, cursor→курсор, bitness→разрядность, monitored→отслеживаемый; Smartscape/Davis/OneAgent/PaaS/AWS/Azure/Cloud Foundry BOSH/Google Compute Engine/IBM CICS Transaction Gateway/`stemcell`(CF-артефакт) EN-lock; `**Hosts**`/`**Topology and Smartscape**`/`**series**`/`**custom device**`/`meIdentifier`/enum-backtick/`**field**` EN-lock; `Endpoint'ы`/`OneAgent'ов`/`Host Unit'ы` apostrophe-plural (env-api corpus L4Y); parent card-block glue `](url "title")[### ` сохранён (hosts-api.md/process-groups-api.md, headings «Получить список»/«Получить детали»/«Назначить теги»/«Удалить теги» по parent-anchor). Source-quirk L93 verbatim-by-meaning: process-groups-api/post-tags.md source `The request produces an `application/json`` БЕЗ «payload.» → RU БЕЗ точки (newline-anchored COMMON после longest `…payload.`); process-groups-api.md source «Assign custom tags to your **hosts**.» (говорит hosts) → зеркалим «…вашим хостам.»; hosts-api/del-tags.md Curl `-X POST` (не DELETE) byte-identical в fence; report-custom-device U+00E2 broken-em-dash `retrospectivelyâthe`→normalize→`:` (предложение целиком переведено, em-dash 0); 3-byte BOM в table-cell link-text (`Dynatrace classic licensingï»¿`/`Timeseries API v1 - PUT a custom metricï»¿`) strip → link-text EN, ячейка-проза переведена. Splice `scripts/_build_toposmart.py` (reuse `_build_rumenv.py` COMMON; CRLF→LF + 3-char BOM-strip + MOJI codepoint-normalize; longest-first; write `newline=''` no trailing-nl). **Критич.ревью `scripts/_review_toposmart.py` (копия `_review_rumenv.py` + ENLOCK расширен verified product-names): structural+force-sync+L101+SUSPECT+LATIN-RUN. 1 РЕАЛЬНЫЙ деф пойман-фикс: L4T generic⊂specific collision в report-custom-device-metric.md (per-file standalone-prose `The metric you're reporting must already exist…` = substring внутри `series` table-cell → per-file (runs-before-COMMON) перехватил → EN/RU гибрид) → fix newline-anchor per-file entry (`\n…\n`) → longer COMMON `series` cell применяется чисто → re-run 0 деф.** LATIN-RUN false-positives verified (product-names Cloud Foundry BOSH/Google Compute Engine/IBM CICS Transaction Gateway/Google Cloud Platform/Run/App Engine + API-name/target-H1 link-text → ENLOCK L4S#3). **Оркестратор-семантик spot-check 6ф (applications get-all deprecated-banner+pagination+headers+Example, hosts-api parent card-glue+Related=target-H1-EN, processes get-all↔get-a-process TWIN byte-identical object-strings + per-file path-param distinct, report-custom-device FIXED-defect clean+mojibake→colon, services get-baseline NO-banner-prose handled): 0 ДОПОЛНИТЕЛЬНЫХ деф — structural-green И semantic-green (1-й раз в L4-цепочке оркестратор-spot-check 0 доп.деф: subagent L4T-collision catch+fix во время build был полным; spot-check всё равно ОБЯЗАТЕЛЕН — verified-0 ≠ unchecked).** em-dash 0, code-fence byte-identical, line-parity EXACT 21/21. diff +21 (1615→1636 = **61.62%**, pending 1040→1019, dynatrace-api 652→673 done/454→433 pending, Orphan RU 0, source-check 0). **Lesson L4Z:** (1) **deprecated-banner handling = ПО same-subsection parent RU, НЕ by-family v1-banner-drop: L3T/L3U дропали `* Deprecated` bullet, но same-subsection parent `topology-and-smartscape.md` RU ДЕРЖИТ его → anchor=same-subsection-parent приоритетнее by-family (L4T#1 расширен: КАЖДАЯ canon-axis от свежайшего same-subsection, не от by-family прецедента)**; (2) **twin-splice масштабируется до ~19.4K строк/21ф одним батчем** (object-element STRINGS byte-identical get-all↔get-a-X → COMMON 1× offset-независимо; L4W подтверждён в 2.5× масштабе, L42 «big files» = splice в выделенной сессии НЕ дробление); (3) **per-file standalone-prose entry = substring длинной COMMON table-cell ⇒ ОБЯЗАН newline-anchored (`\n…\n`)** иначе per-file (runs-before-COMMON) перехватывает → EN/RU гибрид (L4T generic⊂specific в per-file-vs-COMMON разрезе); (4) get-baseline источник БЕЗ deprecated-prose (только bullet) — НЕ фабриковать (faithful: отсутствие зеркалится отсутствием, banner COMMON просто не матчит); (5) source-quirk L93: труункир. `…application/json` без «payload.»/parent «hosts» вместо «process groups»/Curl `-X POST` в delete — зеркалить verbatim-by-meaning НЕ «чинить»; (6) оркестратор-semantic-spot-check 0-доп-деф ВОЗМОЖЕН если subagent ловит L4T-класс во время build, но spot-check ОБЯЗАТЕЛЕН (structural≠semantic остаётся, цель — verified-0 не unchecked-0). | 21 | 21 | ✅ done |
| L4-AA | configuration-api/service-api/ partial — request-attributes-api/ (6: parent + del/get-all/get-request-attribute/post/put) + request-naming-api/ (8: parent + create-use-case/delete/get-a-rule/get-all/json-models 936/post-new-rule/put-a-rule) = 14 файлов, ~3.7K EN-строк. **Две самодостаточные sub-subsection'а service-api/ ЗАКРЫТЫ 100% ЦЕЛИКОМ** (остаток service-api/ = detection-rules 26 + failure-detection 15 + custom-services-api 7 = 48, отдельные батчи). **АКТИВНЫЙ API** L89/L90 (`* Reference`/`* Published Dec 05 2018`/`Mar 05 2019`/`Jun 25 2019`/`Sep 03 2019` EN-verbatim, без `* Deprecated`). **anchor = свежайший config-api same-family RU = L4X calculated-metrics/service-metrics RU** (shared Condition/ComparisonInfo/Placeholder/PropagationSource/UniversalTag-long/TagInfo-short/ConfigurationMetadata/EntityShortRepresentation/StubList/Error/ErrorEnvelope/ConstraintViolation + ВСЕ *ComparisonInfo/*Dto variation-объекты БАЙТ-ИДЕНТИЧНЫ EN → (en,ru) pary L4X verbatim) + k8s/config shared L4M/L4U. Strong post↔put twins (RA 95%, RN 96% identical) — twin handled IMPLICITLY: идентичные shared EN-строки получают идентичный RU через общую R-table (no explicit COMMON). json-models = canonical ComparisonInfo-variations (L4X service-metrics twin): structure L3G (Variations-intro «Некоторые JSON-модели API **Request naming** различаются…», Refer-to-JSON `[JSON models]` link-text EN, `### BOOLEAN`/`### ESB\_INPUT\_NODE\_TYPE` type-headings EN-verbatim, `Parameters`/`JSON model` standalone tab-labels EN) НО `Возможные значения:` с двоеточием + EN-locks = L4X/L99 (НЕ L3G «Элемент может принимать», 134× в json-models, env-leak 0). title/H1×2 EN-verbatim (вкл. use-case `# Create a new request naming rule`); `The element can hold these values`→`Возможные значения:`. **L101: 400 «Сбой. Невалидный ввод.» С точкой ВО ВСЕХ 14 (grep-verified единственная форма `Failed. The input is invalid.` С точкой — substring-replace сохраняет точку источника; ПРОТИВОПОЛОЖНО L4X calculated-metrics БЕЗ точки при идентичной структуре — грепать EN-ячейку КАЖДОГО subsection L4X#3)**; bare GET-200 `\| Success \|`→`\| Успех \|` (L4W/L4X); validate-204 «Validated.»-prefix EN-cell (L4I); RA del-204 «Удалено. Ответ без тела.»/RN delete-204 «Успех. Правило удалено. Ответ без тела.». `## Validate payload`/`#### Curl` EN ALLOWED_EN. **Related-topics link-текст = target RU H1 ДОСЛОВНО (L4O/L4L, resolved): `[Атрибуты запросов]`/`[Настройка именования запросов]`/`[Определение пользовательских сервисов]`; title-attr переведён. post-new-rule intro topic link-text `[Request naming API - Create a new rule]`/`[**POST a new request naming rule**]` = EN endpoint-name (L4T), title-attr переведён.** **create-a-new-request-naming-rule = USE-CASE narrative** (REST client / Dynatrace API Explorer tab-labels переведены, 7 numbered steps + image alt/caption переведены `![Доступ к API Explorer]`/`![Payload]`/`![Успешный запрос]`, «Try it out» UI-button EN consistent, dt-cdn URLs verbatim, code-fence force-synced). mojibake `â\x80\x{93,94,98,99}` codepoint-normalize (L4X), 3-char BOM strip (L4M, `[Service metrics API - JSON modelsï»¿]`→link-text EN), CRLF→LF. Source-quirk L93 verbatim: «mehtod argument»/«JAVA_HTTPURLCONNETION»/«Prune Whitespaces»/`\n\n` literal in cells/`.This`→`.Эта` no-space зеркалим. Splice `scripts/_build_serviceapi.py` (TIER-0 embedding-anchor: full sentences embedding link+title-attr с ORIGINAL-EN nested title-attr → ПЕРВЫМИ, до standalone (A) title-attr — L4T longest-first) + критич.ревью `scripts/_review_serviceapi.py` (копия `_review_servicemetrics.py` + ENLOCK + LEFTOVER excl. type-headings/tab-labels). **3 build-iter: (iter1) 17 деф — 4 self-em-dash (position/argumentIndex, CLAUDE#0) + 13 SUSPECT-EN (L4T ORDERING: use-case sentences embed title-attr что (A)/(B) generic pre-конвертировали → whole-sentence key не матчит; + missing L4X TagInfo-short 3 pary в json-models); (iter2) fix tiering+TagInfo+em-dash → 1 деф (image-alt `![X]` separate anchor от caption `X\n`); (iter3) +3 image-alt keys → 0 структурных деф.** Оркестратор-семантик spot-check 8ф (RA parent Tier-0-intro+cards+Related=H1, use-case Tier-0-links resolved+narrative+image-alt+fence, RA post↔put twin RequestAttribute byte-identical [genuine source-delta ValueCondition.operator NOT_EMPTY post≠put — faithful], RA get bare-Success+RequestAttribute, RN post-new-rule position-no-em-dash+JSON-models-ref+ComparisonInfo-doc-ref-EN, RN post↔put twin 2-line genuine-delta, json-models type-headings/tab-labels EN+TagInfo-short+Возможные×134, L101 400-period+204 across all 14): **0 ДОПОЛНИТЕЛЬНЫХ деф — structural-green И semantic-green**. em-dash global 0, line-parity EXACT 14/14, code-fence byte-identical. diff +14 (1636→1650 = **62.15%**, pending 1019→1005, dynatrace-api 673→687 done/433→419 pending, Orphan RU 0, source-check 0). **Lesson L4-AA:** (1) **L4T ordering в COMMON-tier: full sentence EMBEDDING a link+title-attr ОБЯЗАН идти ПЕРЕД standalone-фрагментом того же title-attr (longest/most-specific-first), иначе generic (A)/(B) pre-конвертирует nested anchor → whole-sentence key no-match → leftover-EN (use-case 13 SUSPECT) — TIER-0 embedding-anchor блок первым**; (2) **post↔put twin handled IMPLICITLY общей R-table (нет explicit COMMON-extract) — детерминированный exact-string replace даёт идентичный RU для идентичных shared EN; genuine source-delta (ValueCondition.operator NOT_EMPTY post≠put) зеркалится faithfully, НЕ «выравнивать»**; (3) **image alt-text `![X]` = ОТДЕЛЬНЫЙ anchor от caption `X\n` (заканчивается `]` vs `\n`) — нужны ОБА правила для consistency (caption переведён ⇒ alt переведён); UI-button-name в alt («Try it out») EN consistent**; (4) L101 период РЕШАЕТСЯ ПО EN-ячейке КАЖДОГО subsection — service-api С точкой vs L4X calculated-metrics БЕЗ точки идентичная структура (L4X#3/L4Q подтверждён 3-й раз); (5) json-models structure-prose от L3G-прецедента, canon-elements (`Возможные значения:`/headers/EN-lock) от same-subsection-family-newest L4X (L4X#4 подтверждён); (6) self-introduced em-dash из вольного перевода (position/argumentIndex) — review EM-DASH-check CLAUDE#0 держит, перефраз запятой/«или». | 14 | 14 | ✅ done |
| L4-AB | configuration-api/service-api/ остаток (service-api.md + custom-services-api/ 7 + detection-rules/ 26 + failure-detection/ 15) ЗАКРЫТ → service-api/ subsection 100% ЦЕЛИКОМ (L4-AA 14 + L4-AB 49 = 63ф); АКТИВНЫЙ; twin-splice 4 rule-type families; критич.ревью поймал системный leftover-EN на 18ф (fixed, 86 R-entries); [LATIN-RUN] net портирован в review-harness | 49 | 49 | ✅ done |
| L4-AC | configuration-api/anomaly-detection-api/ остаток (aws/hosts/vmware ×{parent+get-config+put-config}=9 АКТИВНЫЕ + metric-events/{post-event,json-models}=2 DEPRECATED) ЗАКРЫТ → **anomaly-detection-api/ subsection 100% ЦЕЛИКОМ** (L4C 10 + L4D 10 + L4-AC 11 + applications/database/services уже = вся подсекция). ~6.7K EN-строк. anchor = same-subsection L4D database/services/applications RU (твины parent×3 23-стр + get/put-config) + L4-AB failure-detection json-models RU. Deprecated: `* Deprecated` EN-verbatim + «Этот API устарел. Используйте [Settings API]…» link-text EN/title-attr RU. **L101 mixed per-file: hosts/put-config БЕЗ точки vs aws/vmware/metric-events С точкой (grep EN-ячейку каждого, L4X#3 5-й раз).** Splice via delegated subagent + критич.ревью `_review_anomaly_l4ac.py` (копия `_review_anomaly_l4d.py` + 11 PAIRS + `* Deprecated` инвариант + [LATIN-RUN] net интегрирован in-harness L4-AB#1). 0 структурных деф; LATIN-RUN 22→18 (18 LEGIT: img alt/caption EN + Related link-text EN+title-RU + json-models cross-ref EN+BOM-strip + type-names + `Required` value-cell EN); **1 РЕАЛЬНЫЙ деф пойман оркестратором: `VM CPU ready` leftover-EN в 5 ячейках 2ф (sibling `VM CPU usage`→`Загрузка VM CPU` переведён, `ready` нет) → fix `Готовность VM CPU` (structural≠semantic 7-й раз)**; короткий 2-4-слов no-Cyr scan 43 flag ВСЕ LEGIT (endpoint-tables/img/`JSON model` tab-labels). em-dash 0, line-parity EXACT 11/11, fences byte-identical. diff +11 (1699→1710 = **64.41%**, pending 956→945, dynatrace-api 736→747/370→359, Orphan RU 0). | 11 | 11 | ✅ done |
| L4-AD | configuration-api/dashboards-api/ = 9ф (parent + dashboards-api-tile-models 2026 + del-dashboard + get-all + get-dashboard + get-sharing-config + post-dashboard + put-dashboard + put-sharing-config) ЗАКРЫТ → **dashboards-api/ subsection 100% ЦЕЛИКОМ**. ~5843 EN-строк. **АКТИВНЫЙ Classic config API** (`* Reference`/`* Published`, без `* Deprecated`, line-parity EXACT EN==RU). anchor = свежайший same-family L4-AC anomaly-detection-api disk-events RU (boilerplate: `## Аутентификация`/`## Параметры`/`## Ответ`/`### Коды ответа`/`### Объекты тела ответа`/`### Объекты тела запроса`/`#### Объект \`X\``/`Возможные значения:` colon/Error/ErrorEnvelope/ConstraintViolation/EntityShortRepresentation/StubList/ConfigurationMetadata/`## Validate payload` EN/`#### Curl` EN/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`/`#### Результат`/«API-токен передаётся в заголовке **Authorization**.»/«Это модель тела запроса со всеми возможными элементами…») + tile-models json-models structure = L4-AB failure-detection/json-models RU (`## TYPE`-headings EN-verbatim, `Parameters`/`JSON model` tab-labels EN-literals, `#### Объект \`X\``). **Twin:** Dashboard/DashboardMetadata/Tile/DashboardFilter/DynamicFilters байт-идентичны get/post/put-dashboard → переведены 1×, identical RU; **genuine source-delta = post/put имеют `\| Required \|` колонку, get НЕ имеет → faithfully зеркалится НЕ выравнивать (L4-AA#2 подтверждён)**; DashboardSharing/DashboardSharePermissions/DashboardAnonymousAccess twin get-sharing↔put-sharing. **L101 MIXED per-file: post-dashboard ×2 (стр 518/659) + put-dashboard (518) `Failed. The input is invalid` БЕЗ точки → `Сбой. Невалидный ввод` БЕЗ точки; put-sharing-config:244 С точкой `Сбой. Невалидный ввод.` + :355 БЕЗ точки (MIXED в ОДНОМ файле — grep EN-ячейку per-cell, L4X#3 6-й раз).** cross-ref `[Dashboards API - Tile JSON modelsï»¿](https://dt-url.net/2wc3spx)` 3-char BOM strip → link-text EN canon-d (L4-AB rule c); inline doc-ref `[Tile JSON models](/managed/.../dashboards-api-tile-models "…")` link-text EN, prose+title-attr RU. parent card-glue `](url "title")[### ` сохранён (Title+Description+title-attr RU, url EN). Related `[Дашборды]` = target RU H1 (`docs/managed-ru/analyze-explore-automate/dashboards-classic.md` `# Дашборды`) L4O/L4L. corrupted em-dash `tileâa` (double-enc U+2014) post-dashboard:750 → `:` (em-dash BAN CLAUDE#0, faithful-by-meaning, единственный не-byte transform). put-dashboard validate-payload EN source-quirk dual `### Response`(no codes table)+`### Authentication` зеркалится L93. EN typos tile-models `Include (\`false')`/`DATA_EXLORER`/`"tileType":"Image"\|"TILE"` в fence byte-identical L93. `User Session Query`/`User session query` tile-type-name EN-lock; AWS/VMware/OpenStack/Synthetic/USQL/Apdex/Markdown EN-lock. **Build = delegated general-purpose subagent** (anchor-paths + canon-brief + 9 enumerated + ground-truth `grep -c`; self-report «0 деф» НЕ принят). **Критич.ревью (orchestrator mandatory)** `scripts/_review_dashboards.py` (копия `_review_anomaly_l4ac.py` + 9 PAIRS + integrated [LATIN-RUN] net + **NEW tighter 2-4-слов no-Cyrillic table-cell scan, L4-AC lesson #2 структурно закреплён**): **0 структурных деф** (line-parity EXACT 9/9 [37/2026/72/253/794/243/975/1000/443], fences byte-identical force-sync 0, em-dash 0, mojibake 0, leftover-EN 0, EN-invariants OK). LATIN-RUN 9→8 + SHORT-RUN 22 orchestrator-triaged: 8 LATIN LEGIT (4× doc-ref `[Dashboards API - Tile JSON models]` canon-d + 4× tileType type-name list EN-lock) + 22 SHORT ВСЕ LEGIT (endpoint-table `ManagedDynatrace for Government`/`Environment ActiveGate` EN-verbatim) + **1 РЕАЛЬНЫЙ деф tile-models:1928 descriptive inline link-text `[User session query](dtusql)` оставлен EN → shipped L4Y corpus (`environment-api/rum/user-sessions/table.md` переводит dtusql link-text) + L4Y#4 → fix `[запрос пользовательских сессий]` (structural-green≠semantic 8-й раз: L4N/L4P/L4T/L4W/L4Y/L4-AB/L4-AC/L4-AD)**. Семантик spot-check: L101-mixed PERFECT, parent card-glue+Related-target-H1, Dashboard-twin identical+genuine-source-delta faithful, validate-payload dual-section L93, corrupted-em-dash→colon faithful. diff +9 (1710→1719 = **64.75%**, pending 945→936, dynatrace-api 747→756/359→350, Orphan RU 0). **Lesson L4-AD:** (1) tighter 2-4-слов no-Cyr table-cell scan структурно интегрирован в harness (L4-AC#2 закреплён: net расширяется не сужается; 0 реальных, подтвердил endpoint-rows clean); (2) descriptive inline link-text к external `dt-url.net` = ПЕРЕВОД per shipped corpus precedent (L4Y user-sessions dtusql) + L4Y#4 ≠ doc-API cross-ref `[X - JSON models]` EN canon-d — проверять shipped corpus РЕАЛЬНЫМ grep'ом не только by-rule; (3) twin genuine-source-delta (post/put `\| Required \|` col vs get без) faithfully зеркалится НЕ выравнивать (L4-AA#2); (4) corrupted-codepoint em-dash в прозе → `:` faithful-by-meaning (em-dash BAN CLAUDE#0 > byte-fidelity); (5) delegated-build + orchestrator-mandatory review non-delegable (verified-0≠unchecked-0, L4Z#6 8-й раз). | 9 | 9 | ✅ done |
| L4-AE | environment-api/settings/ = 7ф (key-concepts.md `* Explanation` + objects/ 6 CRUD del/get-effective-values/get/get-objects/post/put) ЗАКРЫТ → settings/objects/ + key-concepts 100% (остаток settings/ = schemas.md + ~337 schemas/ ОТД.серия). ~1924 EN-строк. **АКТИВНЫЙ Settings 2.0**. anchor = same-subsection parent `settings.md` RU (glossary: settings object/schema/scope/external IDs/concurrency control EN-lock; объект/пагинация переведены) + L4-AD/L4Y/L4Z canon. object-table header `\| Элемент \| Тип \| Описание \|`(+4-col `\| Обязательный \|`, Required value-cell EN); Error env-api L4Y «HTTP-код состояния»; L101 per-cell grep (Success С точкой / bare Success БЕЗ / objectId-404 БЕЗ); BOM strip `[Dynatrace Documentation]` EN canon-d + `[here]`→`[здесь]` L4Y#4; key-concepts mojibake `â` ×7 →`:`/comma faithful (em-dash BAN L4-AD#4); `~~modificationInfo~~`+DEPRECATED→УСТАРЕЛО L4Y; `### Schemas`/`### Scopes`/`### External IDs` heading EN-lock (parent consistency); del source-typo «Updates» на DELETE faithful L93. Build = delegated subagent + критич.ревью `_review_settings_l4ae.py` (копия `_review_dashboards.py` env-api base + `* Explanation` + [LATIN-RUN]+SHORT + **NEW object-header в LEFTOVER**). Build-pass 0 структ., оркестратор REAL-grep shipped поймал **3 whole-class деф (structural≠semantic 9-й раз): (1) object-header EN ВСЕ 6ф 38×3-col+2×4-col (LATIN≥5/SHORT-2-4 ОБА пропускают = blind-spot → header в LEFTOVER portable L4-AC#2); shipped unanimous L4-AD 78×/L4Y 55×/L4-AC 194×; (2) `HTTP-код статуса`→`состояния` 14× (env-api≠config-api cross-family); (3) `### Внешние идентификаторы`→`### External IDs`** → fix WHOLE class `_fix_settings_l4ae.py` longest-first 4→3-col (L4-AA#1), 53 замены line-count unchanged → re-review **[OK] 0 деф** + re-grep 0. LATIN 6+SHORT 6 ВСЕ LEGIT (endpoint-rows). Семантик spot-check 5ф faithful, em-dash 0, line-parity EXACT 7/7 [113/152/243/326/434/347/309]. diff +7 (1719→1726 = **65.01%**, pending 936→929, dynatrace-api 350→343, Orphan RU 0). | 7 | 7 | ✅ done |
| L99 | em-dash cleanup в managed-ru/dynatrace-api/ (basics, cluster-api, etc, раннее переведённые с em-dash, отложено как technical debt) | TBD | 0 | ⚪ queued |
| 13+ | dynatrace-api (остаток 359: calculated-metrics/ ✅ L4O+L4X; service-api/ ✅ L4-AA+L4-AB; anomaly-detection-api/ ✅ ЗАКРЫТ ЦЕЛИКОМ L4C+L4D+L4-AC; dashboards-api 8 + settings/schemas 338 крупн.; env-api rum/topology ✅ L4Y/L4Z, settings 346) / ingest-from (586) | ~945 | 0 | ⚪ queued |

---

## Batch 1 — Migration & Scaling core (10 файлов) — ПРИОРИТЕТНЫЙ

**Тема пользователя:** «Бесшовная миграция кластера Dynatrace Managed при масштабировании»

- [x] `managed-cluster.md` — overview
- [x] `managed-cluster/basics.md` — basics index
- [x] `managed-cluster/basics/managed-deployments.md` — deployment types
- [x] `managed-cluster/operation/migrate-a-cluster.md` ⭐ ядро темы
- [x] `managed-cluster/installation/add-cluster-node.md` ⭐ horizontal scale-out
- [x] `managed-cluster/operation/remove-a-cluster-node.md` ⭐ scale-in
- [x] `managed-cluster/operation/ip-reconfiguration.md` — миграция IP
- [x] `managed-cluster/operation/back-up-and-restore-a-cluster.md` — backup/restore миграция
- [x] `managed-cluster/operation/estimating-cluster-backup-size.md` — sizing бэкапов
- [x] `managed-cluster/operation/change-storage-location.md` — миграция стораджа

Last update: 2026-05-12

---

## Batch 2 — Hardware / sizing / install (7 файлов)

- [x] `managed-cluster/installation.md`
- [x] `managed-cluster/installation/install-managed-cluster.md`
- [x] `managed-cluster/installation/customize-managed-cluster-install.md`
- [x] `managed-cluster/installation/managed-hardware-requirements.md`
- [x] `managed-cluster/installation/managed-cloud-requirements.md`
- [x] `managed-cluster/installation/operating-system-requirements.md`
- [x] `managed-cluster/installation/cluster-node-ports.md`

Last update: 2026-05-12

---

## Batch 3 — High Availability & rack-aware (7 файлов)

- [x] `managed-cluster/high-availability.md`
- [x] `managed-cluster/high-availability/premium-high-availability.md`
- [x] `managed-cluster/high-availability/rack-awareness.md`
- [x] `managed-cluster/high-availability/rack-aware-conversion-using-replication.md`
- [x] `managed-cluster/high-availability/rack-aware-conversion-using-restore.md`
- [x] `managed-cluster/high-availability/auto-repair.md`
- [x] `managed-cluster/high-availability/data-center-disaster-recovery-from-backup.md`

Last update: 2026-05-12

---

## Batch 4 — Cluster configuration (13 файлов)

- [x] `managed-cluster/configuration.md`
- [x] `managed-cluster/configuration/cluster-event-notifications.md`
- [x] `managed-cluster/configuration/cluster-node-capabilities.md`
- [x] `managed-cluster/configuration/cluster-remote-access.md`
- [x] `managed-cluster/configuration/configurable-properties-of-dynatrace-managed.md`
- [x] `managed-cluster/configuration/configure-cluster-preferences.md`
- [x] `managed-cluster/configuration/configure-emergency-contacts-managed.md`
- [x] `managed-cluster/configuration/configure-manage-user-sessions.md`
- [x] `managed-cluster/configuration/configure-smtp-server-connection.md`
- [x] `managed-cluster/configuration/dns-configuration-in-managed.md`
- [x] `managed-cluster/configuration/how-to-add-a-certificate-to-server-trust-store.md`
- [x] `managed-cluster/configuration/internet-proxy.md`
- [x] `managed-cluster/configuration/managed-elevated-permissions.md`

Last update: 2026-05-12

---

## Batch 5 — Operation & self-monitoring (остаток managed-cluster/, 27 файлов)

- [x] `managed-cluster/configuration/password-complexity-rules.md`
- [x] `managed-cluster/configuration/set-up-load-balancer.md`
- [x] `managed-cluster/configuration/sign-in-customization.md`
- [x] `managed-cluster/installation/cluster-offline-to-online.md`
- [x] `managed-cluster/installation/dynatrace-managed-offline.md`
- [x] `managed-cluster/installation/install-cluster-activegate.md`
- [x] `managed-cluster/installation/selinux.md`
- [x] `managed-cluster/installation/ssl-certificate-cluster-activegate.md`
- [x] `managed-cluster/installation/ssl-certificate-managed-cluster.md`
- [x] `managed-cluster/operation.md`
- [x] `managed-cluster/operation/apply-operating-system-patches-to-a-node.md`
- [x] `managed-cluster/operation/diagnostic-archives-for-managed-installations.md`
- [x] `managed-cluster/operation/export-license-data.md`
- [x] `managed-cluster/operation/manage-your-monitoring-environments.md`
- [x] `managed-cluster/operation/remove-a-cluster.md`
- [x] `managed-cluster/operation/start-stop-restart-cluster.md`
- [x] `managed-cluster/operation/start-stop-restart-node.md`
- [x] `managed-cluster/operation/update-cluster.md`
- [x] `managed-cluster/operation/update-dynatrace-managed-activegate.md`
- [x] `managed-cluster/basics/cluster-management-console.md`
- [x] `managed-cluster/basics/managed-components.md`
- [x] `managed-cluster/basics/mission-control-data-exchange.md`
- [x] `managed-cluster/basics/mission-control-proactive-support.md`
- [x] `managed-cluster/self-monitoring.md`
- [x] `managed-cluster/self-monitoring/hosted-self-monitoring.md`
- [x] `managed-cluster/self-monitoring/local-self-monitoring.md`
- [x] `managed-cluster/self-monitoring/private-self-monitoring.md`

Last update: 2026-05-12

---

## Batch 6 — Upgrade (19 файлов)

- [x] `upgrade.md`
- [x] `upgrade/saas-upgrade-assistant.md`
- [x] `upgrade/saas-upgrade-assistant/sua-get-started.md`
- [x] `upgrade/saas-upgrade-assistant/sua-update-config.md`
- [x] `upgrade/saas-upgrade-assistant/sua-update-dashboard-owners.md`
- [x] `upgrade/saas-upgrade-assistant/sua-update-editable-properties.md`
- [x] `upgrade/unavailable-in-managed.md`
- [x] `upgrade/up-execute-upgrade.md`
- [x] `upgrade/up-execute-upgrade/up-migrate-ag-extension.md`
- [x] `upgrade/up-execute-upgrade/up-migrate-ag.md`
- [x] `upgrade/up-execute-upgrade/up-migrate-cfg.md`
- [x] `upgrade/up-execute-upgrade/up-migrate-dto.md`
- [x] `upgrade/up-execute-upgrade/up-migrate-oa-extension.md`
- [x] `upgrade/up-execute-upgrade/up-migrate-oa.md`
- [x] `upgrade/up-get-started.md`
- [x] `upgrade/up-information.md`
- [x] `upgrade/up-plan.md`
- [x] `upgrade/up-plan/feasibility-checklist.md`
- [x] `upgrade/up-post-upgrade.md`

Last update: 2026-05-12

---

## Batch 7 — Small sections + root indexes (23 файла)

**Цель:** закрыть разделы discover-dynatrace, platform, offline-doc + 5 root-индексов.

### discover-dynatrace (10 файлов)
- [x] `discover-dynatrace/get-started.md`
- [x] `discover-dynatrace/get-started/dynatrace-ui.md`
- [x] `discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements.md`
- [x] `discover-dynatrace/get-started/dynatrace-ui/order-of-magnitude-notation.md`
- [x] `discover-dynatrace/get-started/glossary.md`
- [x] `discover-dynatrace/get-started/monitoring-environment.md`
- [x] `discover-dynatrace/get-started/platform-engineering.md`
- [x] `discover-dynatrace/get-started/serverless-monitoring.md`
- [x] `discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md`
- [x] `discover-dynatrace/what-is-dynatrace.md`

### platform (6 файлов)
- [x] `platform/oneagent.md`
- [x] `platform/oneagent/how-one-agent-works.md`
- [x] `platform/oneagent/monitoring-modes/enable-monitoring-modes.md`
- [x] `platform/oneagent/monitoring-modes/monitoring-modes.md`
- [x] `platform/oneagent/resource-attributes.md`
- [x] `platform/oneagent/supported-monitoring-types.md`

### offline-doc (2 файла)
- [x] `offline-doc/how-do-i-enable-synthetic-monitors.md`
- [x] `offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring.md`

### Root indexes (5 файлов)
- [x] `deliver.md`
- [x] `dynatrace-api.md`
- [x] `dynatrace-intelligence.md`
- [x] `ingest-from.md`
- [x] `whats-new.md`

Last update: 2026-05-12

---

## Batch 8 — Secure (28 файлов) — ЗАВЕРШЁН 2026-05-12

**Цель:** перевести весь раздел `secure/` — Application Security (RAP + RVA).
**Результат:** `secure/` исчез из `--by-section`, pending 2655→2458.

### secure/application-security (9 файлов)
- [x] `secure/application-security.md`
- [x] `secure/application-security/application-protection.md`
- [x] `secure/application-security/application-protection/app-sec-metrics.md`
- [x] `secure/application-security/application-protection/application-protection-rules.md`
- [x] `secure/application-security/application-protection/manage-attacks.md`
- [x] `secure/application-security/application-protection/security-notifications-rap.md`
- [x] `secure/application-security/application-protection/security-notifications-rap/email-integration.md`
- [x] `secure/application-security/application-protection/security-notifications-rap/jira-integration.md`
- [x] `secure/application-security/application-protection/security-notifications-rap/webhook-integration.md`

### secure/application-security/vulnerability-analytics (19 файлов)
- [x] `secure/application-security/vulnerability-analytics.md`
- [x] `secure/application-security/vulnerability-analytics/app-sec-metrics.md`
- [x] `secure/application-security/vulnerability-analytics/application-security-overview.md`
- [x] `secure/application-security/vulnerability-analytics/code-level-vulnerabilities.md`
- [x] `secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv.md`
- [x] `secure/application-security/vulnerability-analytics/code-level-vulnerabilities/filter-clv-vulnerabilities.md`
- [x] `secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities.md`
- [x] `secure/application-security/vulnerability-analytics/security-notifications-rva.md`
- [x] `secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration.md`
- [x] `secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration.md`
- [x] `secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities.md`
- [x] `secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md`

### secure (1 файл)
- [x] `secure/faq.md`

Last update: 2026-05-12

---

## Batch 9 — License (42 файла) — ЗАВЕРШЁН 2026-05-12

**Цель:** перевести весь раздел `license/` включая `license.md`.
**Результат:** `license/` исчез из `--by-section`, pending 2458→~2416.

### license/ (root + 8 прямых дочерних файлов)
- [x] `license.md`
- [x] `license/billing-reports.md`
- [x] `license/budget-alerts.md`
- [x] `license/cost-monitors.md`
- [x] `license/cost-overview.md`
- [x] `license/consumption-insights.md`
- [x] `license/dps-permissions.md`
- [x] `license/subscription-history.md`
- [x] `license/monitoring-consumption-classic.md`

### license/capabilities/app-infra-observability (4 файла)
- [x] `license/capabilities/app-infra-observability.md`
- [x] `license/capabilities/app-infra-observability/foundation-and-discovery.md`
- [x] `license/capabilities/app-infra-observability/full-stack-monitoring.md`
- [x] `license/capabilities/app-infra-observability/infrastructure-monitoring.md`
- [x] `license/capabilities/app-infra-observability/mainframe.md`

### license/capabilities/application-security (4 файла)
- [x] `license/capabilities/application-security.md`
- [x] `license/capabilities/application-security/runtime-application-protection.md`
- [x] `license/capabilities/application-security/runtime-vulnerability-analytics.md`
- [x] `license/capabilities/application-security/security-posture-management.md`

### license/capabilities/digital-experience-monitoring (7 файлов)
- [x] `license/capabilities/digital-experience-monitoring.md`
- [x] `license/capabilities/digital-experience-monitoring/browser-monitor-clickpath.md`
- [x] `license/capabilities/digital-experience-monitoring/http-monitor.md`
- [x] `license/capabilities/digital-experience-monitoring/real-user-monitoring.md`
- [x] `license/capabilities/digital-experience-monitoring/real-user-monitoring-property.md`
- [x] `license/capabilities/digital-experience-monitoring/real-user-monitoring-session-replay.md`
- [x] `license/capabilities/digital-experience-monitoring/third-party-api.md`

### license/capabilities/platform-extensions (6 файлов)
- [x] `license/capabilities/platform-extensions.md`
- [x] `license/capabilities/platform-extensions/custom-events-classic.md`
- [x] `license/capabilities/platform-extensions/custom-metrics-classic.md`
- [x] `license/capabilities/platform-extensions/custom-traces-classic.md`
- [x] `license/capabilities/platform-extensions/log-monitoring-classic.md`
- [x] `license/capabilities/platform-extensions/serverless-functions-classic.md`

### license/monitoring-consumption-classic (5 файлов)
- [x] `license/monitoring-consumption-classic/application-and-infrastructure-monitoring.md`
- [x] `license/monitoring-consumption-classic/application-security-units.md`
- [x] `license/monitoring-consumption-classic/davis-data-units.md`
- [x] `license/monitoring-consumption-classic/digital-experience-monitoring-units.md`
- [x] `license/monitoring-consumption-classic/log-monitoring-consumption-legacy.md`

### license/monitoring-consumption-classic/davis-data-units (5 файлов)
- [x] `license/monitoring-consumption-classic/davis-data-units/custom-traces.md`
- [x] `license/monitoring-consumption-classic/davis-data-units/ddu-events.md`
- [x] `license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption.md`
- [x] `license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation.md`
- [x] `license/monitoring-consumption-classic/davis-data-units/serverless-monitoring.md`

### license/subscription-and-license (1 файл)
- [x] `license/subscription-and-license/subscription-and-license-dps.md`

Last update: 2026-05-12

---

## Batch 10 — Dynatrace Intelligence (~31 файл) — ЗАВЕРШЁН 2026-05-12

**Цель:** перевести весь раздел `dynatrace-intelligence/` — Davis AI, Anomaly Detection, Root Cause Analysis.
**Результат:** `dynatrace-intelligence/` исчез из `--by-section`, pending ~2416→~2385.

### dynatrace-intelligence/ (root + ai-models)
- [x] `dynatrace-intelligence/ai-models.md`
- [x] `dynatrace-intelligence/ai-models/causal-correlation-analysis.md`
- [x] `dynatrace-intelligence/ai-models/seasonal-baseline.md`

### dynatrace-intelligence/anomaly-detection
- [x] `dynatrace-intelligence/anomaly-detection.md`
- [x] `dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection.md`
- [x] `dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications.md`
- [x] `dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-extension.md`
- [x] `dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure.md`
- [x] `dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database.md`
- [x] `dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services.md`
- [x] `dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration.md`
- [x] `dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold.md`
- [x] `dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining.md`
- [x] `dynatrace-intelligence/anomaly-detection/metric-events.md`
- [x] `dynatrace-intelligence/anomaly-detection/metric-events/metric-key-events.md`
- [x] `dynatrace-intelligence/anomaly-detection/metric-events/metric-selector-events.md`
- [x] `dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure.md`
- [x] `dynatrace-intelligence/anomaly-detection/static-thresholds.md`

### dynatrace-intelligence/root-cause-analysis
- [x] `dynatrace-intelligence/root-cause-analysis.md`
- [x] `dynatrace-intelligence/root-cause-analysis/concepts.md`
- [x] `dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/availability-events.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/error-events.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/info-events.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/monitoring-unavailable-events.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/slowdown-events.md`
- [x] `dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/warning-events.md`

Last update: 2026-05-12

---

## Batch 11 — deliver/ — Configuration as Code, Ownership, Release Monitoring, SLO, Test Automation (40 файлов) — ЗАВЕРШЁН 2026-05-12

**Цель:** перевести весь раздел `deliver/` — CaC Monaco+Terraform, Backstage, Ownership, Release monitoring, SLO (classic), Test automation.
**Результат:** `deliver/` исчез из `--by-section`, RU total 315 (310 translated), pending ~2385→~2345.

### deliver/ (root)
- [x] `deliver/backstage-integration.md`
- [x] `deliver/configuration-as-code.md`
- [x] `deliver/ownership.md`
- [x] `deliver/release-monitoring.md`
- [x] `deliver/service-level-objectives-classic.md`
- [x] `deliver/test-automation.md`

### deliver/configuration-as-code/
- [x] `deliver/configuration-as-code/monaco.md`
- [x] `deliver/configuration-as-code/terraform.md`

### deliver/configuration-as-code/monaco/
- [x] `deliver/configuration-as-code/monaco/configuration.md`
- [x] `deliver/configuration-as-code/monaco/guides.md`
- [x] `deliver/configuration-as-code/monaco/installation.md`

### deliver/configuration-as-code/monaco/configuration/
- [x] `deliver/configuration-as-code/monaco/configuration/projects.md`
- [x] `deliver/configuration-as-code/monaco/configuration/special-configuration-types.md`
- [x] `deliver/configuration-as-code/monaco/configuration/yaml-configuration.md`

### deliver/configuration-as-code/monaco/guides/
- [x] `deliver/configuration-as-code/monaco/guides/configuration-as-code-advanced-use-case.md`
- [x] `deliver/configuration-as-code/monaco/guides/deprecated-migration.md`
- [x] `deliver/configuration-as-code/monaco/guides/migrating-to-v2.md`
- [x] `deliver/configuration-as-code/monaco/guides/nam-workaround.md`
- [x] `deliver/configuration-as-code/monaco/guides/order-of-configurations.md`

### deliver/configuration-as-code/monaco/reference/
- [x] `deliver/configuration-as-code/monaco/reference/commands.md`
- [x] `deliver/configuration-as-code/monaco/reference/hardware-requirements.md`
- [x] `deliver/configuration-as-code/monaco/reference/supported-configuration.md`

### deliver/configuration-as-code/terraform/
- [x] `deliver/configuration-as-code/terraform/terraform-cli.md`

### deliver/configuration-as-code/terraform/guides/
- [x] `deliver/configuration-as-code/terraform/guides/export-utility.md`
- [x] `deliver/configuration-as-code/terraform/guides/migration.md`

### deliver/configuration-as-code/terraform/tutorials/
- [x] `deliver/configuration-as-code/terraform/tutorials/teraform-basic-example.md`
- [x] `deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example.md`

### deliver/ownership/
- [x] `deliver/ownership/assign-ownership.md`
- [x] `deliver/ownership/best-practices.md`
- [x] `deliver/ownership/ownership-teams.md`

### deliver/release-monitoring/
- [x] `deliver/release-monitoring/issue-tracking-integration.md`
- [x] `deliver/release-monitoring/monitor-releases-with-dynatrace.md`
- [x] `deliver/release-monitoring/version-detection-strategies.md`

### deliver/service-level-objectives-classic/
- [x] `deliver/service-level-objectives-classic/configure-and-monitor-slo.md`
- [x] `deliver/service-level-objectives-classic/slo-basics.md`
- [x] `deliver/service-level-objectives-classic/slo-definition-configuration-examples.md`
- [x] `deliver/service-level-objectives-classic/slo-mz-permissions.md`

### deliver/test-automation/
- [x] `deliver/test-automation/dynatrace-and-jmeter-integration.md`
- [x] `deliver/test-automation/dynatrace-and-loadrunner-integration.md`
- [x] `deliver/test-automation/neotys-integration.md`

Last update: 2026-05-12

---

## Batch 12A — analyze-explore-automate/ часть 1 (33 файла) — ЗАВЕРШЁН 2026-05-12

**Цель:** перевести dashboards-classic, explorer, log-monitoring (основные разделы, кроме log-processing-functions).
**Результат:** первая половина `analyze-explore-automate/` переведена, pending ~2345→~2312.

### analyze-explore-automate/ (root + dashboards-classic + explorer)
- [x] `analyze-explore-automate/dashboards-classic.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/filter-charts.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-graph.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-heatmap.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-honeycomb.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-pie.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-single-value.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-area.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-column.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-table.md`
- [x] `analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-top-list.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/create-dashboards.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/dashboard-json.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/share-dashboards.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports.md`
- [x] `analyze-explore-automate/dashboards-classic/dashboards-upgrade.md`
- [x] `analyze-explore-automate/dashboards-classic/metrics-browser.md`
- [x] `analyze-explore-automate/explorer.md`
- [x] `analyze-explore-automate/explorer/explorer-advanced-query-editor.md`
- [x] `analyze-explore-automate/explorer/explorer-quick-start.md`

### analyze-explore-automate/log-monitoring/ (основная часть)
- [x] `analyze-explore-automate/log-monitoring.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/lm-fluent-bit-logs-k8s.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation.md`

Last update: 2026-05-12

---

## Batch 12B — analyze-explore-automate/ часть 2 (53 файла) — ЗАВЕРШЁН 2026-05-13

**Цель:** перевести оставшиеся 53 файла `analyze-explore-automate/` — log-monitoring (log-processing, config, troubleshooting), metrics-classic, notifications-and-alerting, smartscape.
**Результат:** `analyze-explore-automate/` 100% завершён (86/86 файлов). RU total: 398, Translated: 393, Pending: 2262.

### analyze-explore-automate/log-monitoring/ (остаток — 30 файлов)
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/log-custom-source.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-ingest-json-txt-logs.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/log-storage.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-fluentd-k8s.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit.md`
- [x] `analyze-explore-automate/log-monitoring/acquire-log-data/syslog.md`
- [x] `analyze-explore-automate/log-monitoring/alert-log-data.md`
- [x] `analyze-explore-automate/log-monitoring/analyze-log-data.md`
- [x] `analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes.md`
- [x] `analyze-explore-automate/log-monitoring/analyze-log-data/log-events.md`
- [x] `analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics.md`
- [x] `analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer.md`
- [x] `analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring.md`
- [x] `analyze-explore-automate/log-monitoring/lmc-troubleshooting.md`
- [x] `analyze-explore-automate/log-monitoring/lmc-troubleshooting/lmc-ingest-warnings.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-configuration.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-data-format.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format.md`
- [x] `analyze-explore-automate/log-monitoring/log-monitoring-limits.md`
- [x] `analyze-explore-automate/log-monitoring/log-processing.md`
- [x] `analyze-explore-automate/log-monitoring/log-processing/log-processing-commands.md`
- [x] `analyze-explore-automate/log-monitoring/log-processing/log-processing-examples.md`
- [x] `analyze-explore-automate/log-monitoring/log-processing/log-processing-functions.md` ⚠️ (4475 строк — все функции переведены: Bitwise, Boolean, Casting, Comparison, Composite-data, Cryptographic, Date-time, Flow-control, Math, Network, Strings, Other)
- [x] `analyze-explore-automate/log-monitoring/methods-of-masking-sensitive-data.md`

### analyze-explore-automate/metrics-classic/ (5 файлов)
- [x] `analyze-explore-automate/metrics-classic.md`
- [x] `analyze-explore-automate/metrics-classic/all-metrics.md` ⚠️ (411KB — введение переведено, таблицы технических идентификаторов на EN)
- [x] `analyze-explore-automate/metrics-classic/built-in-metrics.md` ⚠️ (259KB — введение переведено, таблицы технических идентификаторов на EN)
- [x] `analyze-explore-automate/metrics-classic/metrics-mz.md`
- [x] `analyze-explore-automate/metrics-classic/self-monitoring-metrics.md`

### analyze-explore-automate/notifications-and-alerting/ (16 файлов)
- [x] `analyze-explore-automate/notifications-and-alerting.md`
- [x] `analyze-explore-automate/notifications-and-alerting/alerting-profiles.md`
- [x] `analyze-explore-automate/notifications-and-alerting/maintenance-windows.md`
- [x] `analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration.md`
- [x] `analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app.md`

### analyze-explore-automate/ (root + smartscape)
- [x] `analyze-explore-automate/smartscape-classic.md`

Last update: 2026-05-13

---

## Batch 13A — manage/ IAM + tags + system (38 файлов) — ЗАВЕРШЁН 2026-05-13

**Цель:** перевести IAM (27 файлов), tags-and-metadata (7 файлов), hub-managed.md, settings/settings-20.md, system-notifications.md.
**Результат:** manage/ раздел 50/79 файлов завершён. RU total: 448, Translated: 443, Pending: 2212.

### manage/ — Identity Access Management
- [x] `manage/identity-access-management.md`
- [x] `manage/identity-access-management/use-cases.md`
- [x] `manage/identity-access-management/user-and-group-management.md`
- [x] `manage/identity-access-management/use-cases/access-settings.md`
- [x] `manage/identity-access-management/permission-management.md`
- [x] `manage/identity-access-management/permission-management/account-management-permissions.md`
- [x] `manage/identity-access-management/permission-management/role-based-permissions.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies.md`
- [x] `manage/identity-access-management/permission-management/management-zones.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md`
- [x] `manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles.md`
- [x] `manage/identity-access-management/permission-management/management-zones/set-up-management-zones.md`
- [x] `manage/identity-access-management/permission-management/management-zones/management-zone-rules.md`
- [x] `manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones.md`
- [x] `manage/identity-access-management/user-and-group-management/user-groups-and-permissions.md`
- [x] `manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml.md`
- [x] `manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap.md`
- [x] `manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid.md`
- [x] `manage/identity-access-management/access-tokens-and-oauth-clients.md`
- [x] `manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy.md`
- [x] `manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md`
- [x] `manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token.md`
- [x] `manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token.md`
- [x] `manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md`

### manage/ — Tags and Metadata
- [x] `manage/tags-and-metadata.md`
- [x] `manage/tags-and-metadata/basic-concepts/tags-vs-metadata.md`
- [x] `manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging.md`
- [x] `manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale.md`
- [x] `manage/tags-and-metadata/reference/regular-expressions-in-dynatrace.md`
- [x] `manage/tags-and-metadata/setup/define-tags-based-on-environment-variables.md`
- [x] `manage/tags-and-metadata/setup/how-to-define-tags.md`

### manage/ — Hub, Settings, Notifications
- [x] `manage/hub-managed.md`
- [x] `manage/settings/settings-20.md`
- [x] `manage/system-notifications.md`

Last update: 2026-05-13

---

## Batch 14 — whats-new (66 файлов) — ЗАВЕРШЁН 2026-05-13

**Цель:** перевести весь раздел `whats-new/` (release notes + API changelogs).
**Результат:** whats-new/ 66/66 файлов завершён. RU total: 543, Translated: 538, Pending: 2117.

### whats-new/ — Root indexes & release notes
- [x] `whats-new.md`
- [x] `whats-new/activegate.md`
- [x] `whats-new/oneagent.md`
- [x] `whats-new/dynatrace-operator.md`
- [x] `whats-new/managed.md`
- [x] `whats-new/preview-releases.md`
- [x] `whats-new/technology.md`
- [x] `whats-new/technology/end-of-life-announcements.md`
- [x] `whats-new/technology/end-of-support-news.md`
- [x] `whats-new/dynatrace-api.md`

### whats-new/dynatrace-api/ — API changelog sprints (56 файлов)
- [x] `whats-new/dynatrace-api/sprint-302.md`
- [x] `whats-new/dynatrace-api/sprint-303.md`
- [x] `whats-new/dynatrace-api/sprint-304.md`
- [x] `whats-new/dynatrace-api/sprint-305.md`
- [x] `whats-new/dynatrace-api/sprint-306.md`
- [x] `whats-new/dynatrace-api/sprint-307.md`
- [x] `whats-new/dynatrace-api/sprint-308.md`
- [x] `whats-new/dynatrace-api/sprint-309.md`
- [x] `whats-new/dynatrace-api/sprint-310.md`
- [x] `whats-new/dynatrace-api/sprint-311.md`
- [x] `whats-new/dynatrace-api/sprint-312.md`
- [x] `whats-new/dynatrace-api/sprint-313.md`
- [x] `whats-new/dynatrace-api/sprint-314.md`
- [x] `whats-new/dynatrace-api/sprint-316.md`
- [x] `whats-new/dynatrace-api/sprint-317.md`
- [x] `whats-new/dynatrace-api/sprint-318.md`
- [x] `whats-new/dynatrace-api/sprint-319.md`
- [x] `whats-new/dynatrace-api/sprint-320.md`
- [x] `whats-new/dynatrace-api/sprint-321.md`
- [x] `whats-new/dynatrace-api/sprint-322.md`
- [x] `whats-new/dynatrace-api/sprint-325.md`
- [x] `whats-new/dynatrace-api/sprint-326.md`
- [x] `whats-new/dynatrace-api/sprint-327.md`
- [x] `whats-new/dynatrace-api/sprint-328.md`
- [x] `whats-new/dynatrace-api/sprint-329.md`
- [x] `whats-new/dynatrace-api/sprint-330.md`
- [x] `whats-new/dynatrace-api/sprint-331.md`
- [x] `whats-new/dynatrace-api/sprint-332.md`
- [x] `whats-new/dynatrace-api/sprint-333.md`
- [x] `whats-new/dynatrace-api/sprint-334.md`
- [x] `whats-new/dynatrace-api/sprint-335.md`
- [x] `whats-new/dynatrace-api/sprint-336.md`
- [x] `whats-new/dynatrace-api/sprint-337.md`
- [x] `whats-new/dynatrace-api/sprint-338.md`

Last update: 2026-05-13

---

## Batch L1A — observe/application-observability/ (54 файла) — ЗАВЕРШЁН 2026-05-13

**Цель:** перевести весь подраздел `observe/application-observability/` (54 файла) — distributed-traces, multidimensional-analysis, profiling-and-optimization, services-classic, services (request attributes, service detection v1/v2, calculated metrics, etc.).
**Результат:** observe/application-observability/ 54/54 файлов завершён. RU total: 596, Translated: 591, Pending: 2064.

### observe/application-observability/ (root)
- [x] `observe/application-observability.md`

### observe/application-observability/distributed-traces/
- [x] `observe/application-observability/distributed-traces.md`
- [x] `observe/application-observability/distributed-traces/analysis/connect-environments.md`
- [x] `observe/application-observability/distributed-traces/analysis/get-started.md`
- [x] `observe/application-observability/distributed-traces/concepts.md`
- [x] `observe/application-observability/distributed-traces/context-propagation.md`
- [x] `observe/application-observability/distributed-traces/use-cases/error-analysis.md`
- [x] `observe/application-observability/distributed-traces/use-cases/problems-logs-traces.md`
- [x] `observe/application-observability/distributed-traces/use-cases/segment-request.md`

### observe/application-observability/multidimensional-analysis/
- [x] `observe/application-observability/multidimensional-analysis.md`
- [x] `observe/application-observability/multidimensional-analysis/exception-analysis.md`
- [x] `observe/application-observability/multidimensional-analysis/top-database-statements.md`
- [x] `observe/application-observability/multidimensional-analysis/top-web-requests.md`

### observe/application-observability/profiling-and-optimization/
- [x] `observe/application-observability/profiling-and-optimization.md`
- [x] `observe/application-observability/profiling-and-optimization/continuous-thread-analysis.md`
- [x] `observe/application-observability/profiling-and-optimization/cpu-profiling.md`
- [x] `observe/application-observability/profiling-and-optimization/crash-analysis.md`
- [x] `observe/application-observability/profiling-and-optimization/memory-dump-analysis.md`
- [x] `observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage.md`
- [x] `observe/application-observability/profiling-and-optimization/memory-profiling.md`

### observe/application-observability/services-classic/
- [x] `observe/application-observability/services-classic.md`
- [x] `observe/application-observability/services-classic/analyze-individual-service-instances.md`
- [x] `observe/application-observability/services-classic/context-specific-drill-down.md`
- [x] `observe/application-observability/services-classic/monitor-key-requests.md`
- [x] `observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis.md`
- [x] `observe/application-observability/services-classic/service-analysis-new.md`
- [x] `observe/application-observability/services-classic/service-analysis-timing.md`
- [x] `observe/application-observability/services-classic/service-backtrace.md`
- [x] `observe/application-observability/services-classic/service-flow.md`
- [x] `observe/application-observability/services-classic/service-flow/service-flow-filtering.md`
- [x] `observe/application-observability/services-classic/service-flow/service-flow-metrics.md`
- [x] `observe/application-observability/services-classic/service-response-time-hotspots.md`

### observe/application-observability/services/
- [x] `observe/application-observability/services.md`
- [x] `observe/application-observability/services/always-on-app-profiling.md`
- [x] `observe/application-observability/services/calculated-service-metric.md`
- [x] `observe/application-observability/services/customize-api-definitions.md`
- [x] `observe/application-observability/services/request-attributes.md`
- [x] `observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments.md`
- [x] `observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data.md`
- [x] `observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes.md`

### observe/application-observability/services/service-detection/
- [x] `observe/application-observability/services/service-detection/service-detection-v1.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v2.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-settings.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services.md`
- [x] `observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service.md`

Last update: 2026-05-13

---

## Batch L1B2 — observe/infrastructure-observability/ остаток (26 файлов) — ЗАВЕРШЁН 2026-05-13

**Цель:** перевести оставшиеся 26 файлов раздела `observe/infrastructure-observability/`: databases/database-services-classic, networks-classic, queues (с вложенными), cloud-platform-monitoring (AWS/Azure/GCP), hosts/configuration, vmware permissions + индексные файлы.
**Результат:** observe/infrastructure-observability/ полностью закрыт. RU total: 669, Translated: 664, Pending: 1991.

### observe/infrastructure-observability/ (root + indexes)
- [x] `observe/infrastructure-observability.md`
- [x] `observe/infrastructure-observability/databases.md`
- [x] `observe/infrastructure-observability/networks.md`
- [x] `observe/infrastructure-observability/queues.md`

### observe/infrastructure-observability/cloud-platform-monitoring/
- [x] `observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring.md`
- [x] `observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring.md`
- [x] `observe/infrastructure-observability/cloud-platform-monitoring/gcp-monitoring.md`

### observe/infrastructure-observability/databases/database-services-classic/
- [x] `observe/infrastructure-observability/databases/database-services-classic.md`
- [x] `observe/infrastructure-observability/databases/database-services-classic/analyze-database-services-new.md`
- [x] `observe/infrastructure-observability/databases/database-services-classic/analyze-database-services.md`
- [x] `observe/infrastructure-observability/databases/database-services-classic/database-insights.md`
- [x] `observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored.md`
- [x] `observe/infrastructure-observability/databases/database-services-classic/improve-database-performance.md`
- [x] `observe/infrastructure-observability/databases/database-services-classic/support-for-sql-bind-variables.md`

### observe/infrastructure-observability/hosts/
- [x] `observe/infrastructure-observability/hosts/configuration.md`

### observe/infrastructure-observability/networks-classic/
- [x] `observe/infrastructure-observability/networks-classic/detect-network-errors.md`
- [x] `observe/infrastructure-observability/networks-classic/how-to-monitor-network-communication.md`
- [x] `observe/infrastructure-observability/networks-classic/ingest-netflow-records.md`
- [x] `observe/infrastructure-observability/networks-classic/network-monitoring-with-nettracer.md`
- [x] `observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring.md`

### observe/infrastructure-observability/queues/
- [x] `observe/infrastructure-observability/queues/analyze-queues.md`
- [x] `observe/infrastructure-observability/queues/configuration.md`
- [x] `observe/infrastructure-observability/queues/queue-concepts.md`
- [x] `observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md`
- [x] `observe/infrastructure-observability/queues/configuration/tags-and-management-zones.md`

### observe/infrastructure-observability/vmware-vsphere-monitoring/
- [x] `observe/infrastructure-observability/vmware-vsphere-monitoring/limit-infrastructure-monitoring-using-permissions.md`

Last update: 2026-05-13

---

## Batch L1C — observe/digital-experience/web-applications/ (55 файлов) — ЗАВЕРШЁН 2026-05-13

**Цель:** перевести весь подраздел `observe/digital-experience/web-applications/` — additional-configuration (11 файлов), analyze-and-use (15 файлов), initial-setup (28 файлов), troubleshooting (1 файл), root web-applications.md.
**Результат:** web-applications/ полностью закрыт. RU total: 725, Translated: 720, Pending: 1935.

### observe/digital-experience/web-applications/ (root)
- [x] `observe/digital-experience/web-applications.md`

### observe/digital-experience/web-applications/additional-configuration/ (11 файлов)
- [x] `observe/digital-experience/web-applications/additional-configuration/beacon-endpoint.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/customize-rum.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/modify-csp-for-rum.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/rum-javascript-version.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/session-replay-configuration.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/user-privacy-monitoring.md`
- [x] `observe/digital-experience/web-applications/additional-configuration/view-all-rum-data-ingested-from-your-web-application.md`

### observe/digital-experience/web-applications/analyze-and-use/ (15 файлов)
- [x] `observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/performance-analysis.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/visually-complete-top-findings.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics.md`
- [x] `observe/digital-experience/web-applications/analyze-and-use/world-map-view.md`

### observe/digital-experience/web-applications/initial-setup/ (28 файлов)
- [x] `observe/digital-experience/web-applications/initial-setup/app-health-check.md`
- [x] `observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions.md`
- [x] `observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions.md`
- [x] `observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder.md`
- [x] `observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum.md`
- [x] `observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs.md`
- [x] `observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups.md`
- [x] `observe/digital-experience/web-applications/initial-setup/rum-injection.md`
- [x] `observe/digital-experience/web-applications/initial-setup/selective-rum-rollout.md`
- [x] `observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring.md`
- [x] `observe/digital-experience/web-applications/initial-setup/snippet-formats.md`
- [x] `observe/digital-experience/web-applications/initial-setup/subresource-integrity.md`

(Note: initial-setup/ contained additional files not listed here that were translated in the previous session context)

### observe/digital-experience/web-applications/ (troubleshooting)
- [x] `observe/digital-experience/web-applications/troubleshooting.md`

Last update: 2026-05-13

---

## Batch L1D-quick — observe/digital-experience.md (1 файл, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `observe/digital-experience.md` (root index, 44 строки)

Last update: 2026-05-14

---

## Batch L2A — dynatrace-api/basics/ (5 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `dynatrace-api/basics/access-limit.md`
- [x] `dynatrace-api/basics/deprecation-migration-guides.md`
- [x] `dynatrace-api/basics/dynatrace-api-authentication.md` (261 строка, большие таблицы scopes)
- [x] `dynatrace-api/basics/dynatrace-api-response-codes.md`
- [x] `dynatrace-api/basics/preview-early-access.md`

Last update: 2026-05-14

---

## Batch L2B — dynatrace-api/cluster-api/ root (3 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `dynatrace-api/cluster-api.md`
- [x] `dynatrace-api/cluster-api/cluster-api-authentication.md`
- [x] `dynatrace-api/cluster-api/cluster-token-rotation-api.md` (213 строк)

Last update: 2026-05-14

---

## Batch L2C — dynatrace-api/account-management-api/ + subscription-api endpoints (12 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

### account-management-api root + reference-data
- [x] `dynatrace-api/account-management-api.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api.md`
- [x] `dynatrace-api/account-management-api/reference-data.md`
- [x] `dynatrace-api/account-management-api/reference-data/get-regions.md`
- [x] `dynatrace-api/account-management-api/reference-data/get-timezones.md`

### dynatrace-platform-subscription-api/ endpoints
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-monitors/get-forecast.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-all.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-subscription.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost-environment.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage.md`
- [x] `dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage-environment.md`

Last update: 2026-05-14

---

## Batch L2D — dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/ (5 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-maintenance.md`
- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration.md`
- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-off.md`
- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-on.md`
- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities.md`

Остаток в `cluster-v1/`: get-cluster-info-known-servers (230), get-cluster-nodes-configuration-current-status (290), get-cluster-nodes-configuration-request-status (284).

Last update: 2026-05-14

---

## Batch L2E — cluster-v1/ остаток (3 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-info-known-servers.md`
- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-current-status.md`
- [x] `dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-request-status.md`

**cluster-v1/ полностью закрыт: 8/8.**

Last update: 2026-05-14

---

## Batch L2F — cluster-api-v1/internet-proxy-v1/ (9 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `internet-proxy-v1/get-cluster-proxy-configuration.md`
- [x] `internet-proxy-v1/get-cluster-proxy-configuration-ha.md`
- [x] `internet-proxy-v1/get-cluster-proxy-configuration-ha-all.md`
- [x] `internet-proxy-v1/put-cluster-proxy-configuration.md`
- [x] `internet-proxy-v1/put-cluster-proxy-configuration-ha.md`
- [x] `internet-proxy-v1/delete-cluster-proxy-configuration.md`
- [x] `internet-proxy-v1/delete-cluster-proxy-configuration-ha.md`
- [x] `internet-proxy-v1/test-cluster-proxy-configuration.md`
- [x] `internet-proxy-v1/test-cluster-proxy-configuration-ha.md`

**internet-proxy-v1/ полностью закрыт: 9/9.**

Last update: 2026-05-14

---

## Batch L2G — cluster-api-v1/password-policy-v1/ (2 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `password-policy-v1/get-cluster-password-policy.md`
- [x] `password-policy-v1/put-cluster-password-policy.md`

**password-policy-v1/ полностью закрыт: 2/2.**

Last update: 2026-05-14

---

## Batch L2H — cluster-api-v1/ssl-certificates-v1/ (3 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `ssl-certificates-v1/get-cluster-ssl-cert-details.md`
- [x] `ssl-certificates-v1/get-cluster-ssl-cert-storage-status.md`
- [x] `ssl-certificates-v1/post-cluster-ssl-cert-store-status.md`

**ssl-certificates-v1/ полностью закрыт: 3/3.**

Last update: 2026-05-14

---

## Batch L2I — cluster-api-v1/users-v1/ (6 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `users-v1/delete-user.md`
- [x] `users-v1/get-user.md`
- [x] `users-v1/get-users.md`
- [x] `users-v1/post-create-user.md`
- [x] `users-v1/post-create-users.md` (bulk)
- [x] `users-v1/put-update-user.md`

**users-v1/ полностью закрыт: 6/6.**

Last update: 2026-05-14

---

## Batch L2J — cluster-api-v1/user-groups-v1/ (9 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `user-groups-v1/delete-group.md`
- [x] `user-groups-v1/get-group.md`
- [x] `user-groups-v1/get-group-mz.md`
- [x] `user-groups-v1/get-groups-mz.md`
- [x] `user-groups-v1/get-user-groups.md`
- [x] `user-groups-v1/post-create-user-group.md`
- [x] `user-groups-v1/post-create-users-groups.md` (bulk)
- [x] `user-groups-v1/put-update-group-mz.md`
- [x] `user-groups-v1/put-update-user-groups.md`

**user-groups-v1/ полностью закрыт: 9/9.** Объёмная структура, ~2800 строк суммарно. Все 9 endpoints используют общие объекты `GroupConfig`, `MzPermissionsForGroup`, `MzListForEnvironment`, `MzPermissionsList` — переводы консистентны across files.

Last update: 2026-05-14

---

## Batch L2K — cluster-api-v2/ ВСЕ 8 подразделов (31 файл, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `cluster-license/get-cluster-license-usage.md`
- [x] `cluster-tokens/create-cluster-tokens.md`
- [x] `cluster-tokens/delete-cluster-token.md`
- [x] `cluster-tokens/list-cluster-token-metadata-para.md`
- [x] `cluster-tokens/list-cluster-token-metadata-req.md`
- [x] `cluster-tokens/list-cluster-tokens.md`
- [x] `cluster-tokens/update-cluster-token.md`
- [x] `environments/create-managed-environment.md`
- [x] `environments/delete-specific-managed-environment.md`
- [x] `environments/list-managed-environments.md`
- [x] `environments/list-specific-managed-environment.md`
- [x] `environments/update-specific-managed-environment.md`
- [x] `export-license-data/get-export-license-data.md`
- [x] `export-license-data/get-export-license-data-hour.md` (843 строки)
- [x] `log-monitoring/get-log-monitoring-status.md`
- [x] `log-monitoring/post-update-log-events-per-cluster-for-log-monitoring.md`
- [x] `remote-access/get-all-cluster-access-requests.md`
- [x] `remote-access/get-cluster-access-request.md`
- [x] `remote-access/post-remote-access-permission.md`
- [x] `remote-access/put-change-access-request-state.md`
- [x] `synthetic-locations-and-nodes/delete-a-location.md`
- [x] `synthetic-locations-and-nodes/get-all.md`
- [x] `synthetic-locations-and-nodes/get-all-locations.md`
- [x] `synthetic-locations-and-nodes/get-a-location.md`
- [x] `synthetic-locations-and-nodes/get-node.md`
- [x] `synthetic-locations-and-nodes/post-a-location.md`
- [x] `synthetic-locations-and-nodes/put-a-location.md`
- [x] `user-management/delete-cluster-user-session.md`
- [x] `user-management/get-cluster-user-sessions.md`
- [x] `user-management/get-cluster-user-sessions-configuration.md`
- [x] `user-management/update-cluster-user-sessions-configuration.md`

**cluster-api-v2/ полностью закрыт: 31/31.** Большие environments (Environment + EnvironmentQuotas + EnvironmentStorage с 11 retention/storage объектами) повторяются в list/list-specific/create/update — переводы консистентны across files. get-export-license-data-hour 843 строки — самый большой файл (LicenseConsumption + EnvironmentLicenseConsumption + 9 вложенных объектов).

Last update: 2026-05-14

---

## Batch L2L — mission-control-api/ ВСЕ 3 подраздела (4 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `cluster-sso-client-registration/post-generate-sso-client-credentials.md`
- [x] `cluster-sso-token-generation/post-generate-sso-token.md`
- [x] `offline-bundle-packages/get-available-packages-updates.md`
- [x] `offline-bundle-packages/get-offline-package-update-bundle.md`

**mission-control-api/ полностью закрыт: 4/4.** OAuth API client + SSO token + offline bundle download.

Last update: 2026-05-14

---

## Batch L2M — Root index .md файлы (3 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `mission-control-api.md` — full OAuth flow guide
- [x] `configuration-api.md` — Configuration as Code introduction + 50+ endpoint links
- [x] `environment-api.md` — 60+ endpoint links по 22 разделам

Last update: 2026-05-14

---

## Batch L2N — account-management-api/ closure (2 файла, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `environment-management-api/environment-management-api.md` — GET all environments of an account
- [x] `post-notifications.md` — POST filter notifications (budget/cost/forecast/BYOK)

**account-management-api/ полностью закрыт: 14/14.** Раньше были 12 файлов в L2C; теперь добавлены 2 оставшихся.

Last update: 2026-05-14

---

## Batch L2O — configuration-api/ старт: aws-privatelink + data-privacy + frequent-issue-detection (9 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `aws-privatelink/get-configuration.md`
- [x] `aws-privatelink/get-allowlist.md`
- [x] `aws-privatelink/put-configuration.md`
- [x] `aws-privatelink/put-allowlist.md`
- [x] `aws-privatelink/delete-allowlist.md` — **aws-privatelink/ полностью закрыт: 5/5**
- [x] `data-privacy-api/get-configuration.md`
- [x] `data-privacy-api/put-configuration.md` — **data-privacy-api/ полностью закрыт: 2/2** (+ validate payload endpoint в составе put)
- [x] `frequent-issue-detection-api/get-configuration.md`
- [x] `frequent-issue-detection-api/put-configuration.md` — **frequent-issue-detection-api/ полностью закрыт: 2/2** (deprecated, рекомендован Settings API)

**3 малых подраздела configuration-api/ закрыты целиком.** Старт работы над configuration-api/ (321 файл всего). Следующие малые подразделы: maintenance-windows-api (5), conditional-naming (6 + json-models), aws-credentials-api, k8s-credentials-api-api.

Last update: 2026-05-14

---

## Batch L2P — configuration-api/ дальше: k8s-credentials-api ВСЯ + maintenance-windows частично (7 файлов, Opus) — ЗАВЕРШЁН 2026-05-14

- [x] `k8s-credentials-api-api/get-all.md`
- [x] `k8s-credentials-api-api/delete-credentials.md`
- [x] `k8s-credentials-api-api/get-credentials.md`
- [x] `k8s-credentials-api-api/post-new-credentials.md` (+ validate payload endpoint)
- [x] `k8s-credentials-api-api/put-credentials.md` (+ validate payload endpoint) — **k8s-credentials-api-api/ полностью закрыт: 5/5** (deprecated, рекомендован Settings API + builtin:cloud.kubernetes/builtin:cloud.kubernetes.monitoring schemas)
- [x] `maintenance-windows-api/delete-mw.md`
- [x] `maintenance-windows-api/get-all.md`

**Остаток maintenance-windows-api (для следующей сессии):** get-mw (527 строк), post-mw (724), put-mw (778). Каждый содержит огромную MaintenanceWindow + Schedule + Recurrence + Filter структуру. Идеально под отдельную сессию.

Last update: 2026-05-14

---

## Batch 13+ — Auto-generated (см. _pending.txt)

Запустить `python scripts/translation_diff.py --by-section` — он сгруппирует ~1579 оставшихся файлов по разделам (dynatrace-api/ ~993 + ingest-from/ ~586 остаток).

**Закрыто целиком в dynatrace-api/:** basics (5), cluster-api (71), account-management-api (14), mission-control-api (4), configuration-api/aws-privatelink (5), configuration-api/data-privacy-api (2), configuration-api/frequent-issue-detection-api (2), configuration-api/k8s-credentials-api-api (5) + 4 root index .md + maintenance-windows частично (2) = **114 endpoints**. Остаётся: configuration-api/ (~305 файлов), environment-api/ (~686 файлов). Следующее (новая сессия): maintenance-windows-api big 3 (get-mw + post-mw + put-mw) → conditional-naming → environment-api малые.

---

## Batch L3W — environment-api/synthetic-v2/ (27 файлов)

Активный API v2 (не deprecated, без баннера, L89). Глоссарий env-api boilerplate по problems-v2 RU (L87: `Справочник`/`Опубликовано <DD месяца YYYY>`/`Поле`/`смотрите`/`нужен access-токен со scope`). Sub-index страницы (4) рендерятся как tokens-v2 RU: `* Reference`/`* Published` оставлены англ. (scraper-метадата), переведены только карточки `[### …](url "title")` + «Связанные темы». Shared `ErrorEnvelope`+`Error`+`ConstraintViolation` идентичны во всех 27 файлах (L85), включая source-quirk `-Поле может принимать значения:` в `parameterLocation` и `* Reference`/`* Updated on <date>` vs `* Справочник`/`* Опубликовано`. JSON-блоки вербатим (вкл. пустые строки и pre-existing corruption `GdaÅsk` в `"name"`/`"city"` примеров — L85). BOM-mojibake `GET all nodesï»¿`/`JSON modelsï»¿`/`GET all countriesï»¿`/`GET regions of the countryï»¿` → BOM убран (broken-char 0). `~~peerCertificateExpiryDate~~` strikethrough + `DEPRECATED`→`УСТАРЕЛО` вербатим (3 файла execution). Source-факт «primaryGrailTags … only available for SaaS and not for Managed» переведён дословно (style guide: SaaS-only оставляем как есть). em-dash 0. **synthetic-v2/ закрыт целиком (27 файлов).**

- [x] `environment-api/synthetic-v2/synthetic-locations-v2.md` (sub-index)
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution.md` (sub-index)
- [x] `environment-api/synthetic-v2/synthetic-network-availability-monitors.md` (sub-index)
- [x] `environment-api/synthetic-v2/synthetic-nodes-v2.md` (sub-index)
- [x] `environment-api/synthetic-v2/synthetic-configuration-v2/get-configuration.md`
- [x] `environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/delete-a-location.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/get-all-locations.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/get-a-location.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/get-location-status.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/json-models.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/post-a-location.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/put-a-location.md`
- [x] `environment-api/synthetic-v2/synthetic-locations-v2/put-location-status.md`
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution/get-all-executions.md`
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution/get-batch-summary.md`
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution/get-execution-basic.md`
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution/get-execution-full.md`
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution/get-http-monitor.md`
- [x] `environment-api/synthetic-v2/synthetic-monitor-execution/post-batch-execution.md`
- [x] `environment-api/synthetic-v2/synthetic-network-availability-monitors/delete-monitor-definition.md`
- [x] `environment-api/synthetic-v2/synthetic-network-availability-monitors/get-all-monitors.md`
- [x] `environment-api/synthetic-v2/synthetic-network-availability-monitors/get-monitor-definition.md`
- [x] `environment-api/synthetic-v2/synthetic-network-availability-monitors/post-monitor-definition.md`
- [x] `environment-api/synthetic-v2/synthetic-network-availability-monitors/put-update-monitor-definition.md`
- [x] `environment-api/synthetic-v2/synthetic-nodes-v2/get-all.md`
- [x] `environment-api/synthetic-v2/synthetic-nodes-v2/get-node.md`

Last update: 2026-05-15l

## Batch L3X — environment-api/synthetic/ v1 (23 файла)

- [x] `environment-api/synthetic/synthetic-locations.md`
- [x] `environment-api/synthetic/synthetic-monitors.md`
- [x] `environment-api/synthetic/synthetic-nodes.md`
- [x] `environment-api/synthetic/third-party-synthetic.md`
- [x] `environment-api/synthetic/synthetic-locations/delete-a-location.md`
- [x] `environment-api/synthetic/synthetic-locations/get-all-locations.md`
- [x] `environment-api/synthetic/synthetic-locations/get-a-location.md`
- [x] `environment-api/synthetic/synthetic-locations/get-location-status.md`
- [x] `environment-api/synthetic/synthetic-locations/json-models.md`
- [x] `environment-api/synthetic/synthetic-locations/post-a-location.md`
- [x] `environment-api/synthetic/synthetic-locations/put-a-location.md`
- [x] `environment-api/synthetic/synthetic-locations/put-location-status.md`
- [x] `environment-api/synthetic/synthetic-monitors/delete-a-monitor.md`
- [x] `environment-api/synthetic/synthetic-monitors/get-all-monitors.md`
- [x] `environment-api/synthetic/synthetic-monitors/get-a-monitor.md`
- [x] `environment-api/synthetic/synthetic-monitors/models.md`
- [x] `environment-api/synthetic/synthetic-monitors/post-a-monitor.md`
- [x] `environment-api/synthetic/synthetic-monitors/put-a-monitor.md`
- [x] `environment-api/synthetic/synthetic-nodes/get-all.md`
- [x] `environment-api/synthetic/synthetic-nodes/get-node.md`
- [x] `environment-api/synthetic/third-party-synthetic/post-modify-state.md`
- [x] `environment-api/synthetic/third-party-synthetic/post-third-party-events.md`
- [x] `environment-api/synthetic/third-party-synthetic/post-third-party-monitors.md`

Last update: 2026-05-15m

## Batch L4I — configuration-api/reports-api/ parent + 7 endpoints ЗАКРЫТ ЦЕЛИКОМ (8 файлов, Opus) — ЗАВЕРШЁН 2026-05-16h

АКТИВНЫЙ configuration-api подраздел (без deprecated-баннера, L89/L90; `* Published Jan 16, 2020`). **L103 case (b):** env-api reports-twin'а НЕТ (проверено: `ls environment-api/` — нет reports) → anchor = свежепереведённый azure-credentials-api RU (L4H, k8s/credentials семья) для shared объектов.

**reports-api/ закрыт целиком (8/8):**
- [x] `configuration-api/reports-api.md` (parent, card-link индекс 7 эндпоинтов в 3 блоках + `## Связанные темы`, 36 строк)
- [x] `configuration-api/reports-api/del-report.md` (73 строки, 2-кол. Response codes, Example «из примера [POST request]»)
- [x] `configuration-api/reports-api/get-all.md` (238 строк, ReportStubList+DashboardReportStub, params type/sourceId)
- [x] `configuration-api/reports-api/get-report.md` (234 строки, DashboardReport+DashboardReportSubscription)
- [x] `configuration-api/reports-api/post-report.md` (511 строк, DashboardReport 4-кол. + Validate payload + EntityShortRepresentation/ErrorEnvelope/Error/ConstraintViolation)
- [x] `configuration-api/reports-api/put-report.md` (516 строк, near-twin POST + id-параметр + 201/204-коды)
- [x] `configuration-api/reports-api/subscribe-report.md` (311 строк, ReportSubscriptions, near-twin unsubscribe)
- [x] `configuration-api/reports-api/unsubscribe-report.md` (311 строк, near-twin subscribe)

**Канон L99 (config-api, АКТИВНЫЙ → без баннера):** frontmatter `title:` / `# H1`×2 / `* Reference` / `* Published Jan 16, 2020` EN-вербатим. `The element can hold these values * X`→`Возможные значения: * X` (С двоеточием, k8s-канон; вкл. **inline-вариант** в описании поля `schedule` и **leading-dash** `-The element can hold these values`→`-Возможные значения:` в `type`/`parameterLocation`). `In`→`Где` (header), cell `path`/`query`/`body`/`Required`/`Optional` EN-вербатим. Section-headers переведены; `## Validate payload`/`#### Curl` EN (ALLOWED_EN). Example-секции config-api канон.

**Канон-решения L4I (новые/подтверждённые):**
- **L103 (b) применён:** twin'а нет → anchor = ближайший config-api той же семьи (azure-credentials RU L4H). Shared `EntityShortRepresentation` («Краткое представление сущности Dynatrace.»/«Краткое описание…»/«ID…»/«Имя…»), `ErrorEnvelope`/`Error` («HTTP-код статуса»/«Список нарушений ограничений»/«Сообщение об ошибке»)/`ConstraintViolation` («-Возможные значения: * \`HEADER\`…») вербатим из azure RU.
- **Domain «report»→«отчёт» (обычное рус. слово, НЕ EN-вербатим):** отличие от L4G/L4H где «AWS/Azure credentials» оставались EN — там действовал k8s-family lock на feature-name `*-credentials`. «report» — общий термин, переводится. «dashboard»→«дашборд» (corpus-доминанта: 320×«дашборда»/195×«дашборд»; 0× «панель мониторинга» в API-корпусе). «subscriber/subscription/subscribe»→«подписчик/подписка/подписаться», «recipients»→«получатели», «schedule»→«расписание». Enum `DASHBOARD`/`WEEK`/`MONTH` + object-names EN-вербатим в `#### Объект`.
- **L101 (период ПО ИСТОЧНИКУ построчно):** ВСЕ reports 400 EN `| Failed. The input is invalid. |` С точкой → `Сбой. Невалидный ввод.` С точкой (5/5 единообразно, как L4G aws). 204-описания period-by-source: del `Успех. Отчёт удалён. Ответ без тела.` (точка, EN с точкой) vs put-204 `Успех. Отчёт обновлён. Ответ без тела` (без точки, EN без точки) vs post-validate `Validated. Переданный отчёт валиден. Ответ без тела.` (точка) vs put-validate без точки — расхождение строго по EN-источнику каждой строки.
- **«Validated.» EN-prefix сохранён** + «Переданный отчёт валиден.» (L4E канон, но domain `report`→`отчёт`, НЕ «конфигурация» как в credentials-канонах). 201: «Успех. Новый отчёт создан. Ответ содержит ID нового отчёта.»; subscribe «Успех. Новые подписки созданы. Тело ответа содержит ID отчёта.»; unsubscribe «Успех. Подписки отозваны…».
- **Example cross-ref:** «В этом примере запрос … из примера [POST request](/managed/…/post-report#example "Создание конфигурации отчёта через Dynatrace API.")» (L4D/azure-delete канон: link-текст укорочён EN `POST request`, «example»→«из примера», title переведён). Related-topics `[Subscribe to Dynatrace dashboard reports]` link-текст EN-вербатим + title «Узнайте, как подписаться на отчёты, генерируемые из дашбордов Dynatrace.» (L4F канон).
- **Source-quirks:** `DashboardReportStub` desc «A short representations of the report.» (грам. ошибка ед/мн в источнике) → «Краткое представление отчёта.» (смысл важнее опечатки, L93). put-report финальная фраза примера «…available in your environment» без точки и put-204/put-validate-204 без точки — сохранены по источнику. Двойные пробелы в описаниях `MONTH`/`WEEK`/`recipients`/`schedule`/put-`id` вербатим (L85).
- **Card-link parent:** heading/body/title переведены, URL/anchor нетронут, склейка `](url "title")[###` сохранена; `## Related topics`→`## Связанные темы` (у azure parent её не было, у reports есть — рендерим источник).

**Критический ревью (`scripts/_review_reports.py`, 0 дефектов с ПЕРВОГО прогона):** force-sync ```-fenced EN→RU = **0 файлов нуждались в sync** (ручная JSON-транскрипция byte-identical, тройные пустые строки + curl-блоки сохранены, L98/L100). line-parity EN==RU 8/8; heading/h4/fence/table-row паритет 8/8; em-dash 0; mojibake (`Â`/`Ã`/`ï»¿`/`â€`/`â`)/BOM 0; leftover-EN section-headers 0 (`## Validate payload`=канон-EN); EN-инварианты (title/H1×2/`* Reference`/`* Published`). Доп. семантич. spot-check: спурьёзного deprecated-баннера нет (API активный, 0), env-api leak «может принимать» = 0, «Возможные значения:» 13, L101 все 400 = `.` (5/5 по источнику), shared-obj канон («HTTP-код статуса»×6, «Краткое представление сущности Dynatrace»×4, «Список нарушений ограничений»×12), leftover-проза 0. **Правок не потребовалось** (6-й батч подряд 0-деф с первого прогона: L4B/L4E/L4F/L4G/L4H/L4I). verify_corpus.py: Translated **1438** (+8), Pending 1217, Orphan RU 0, source-check OK, dynatrace-api 475 done/631 pending.

**Lesson L4I:** выбор «переводить термин или оставлять EN-вербатим» зависит от того, feature-name это или общее слово. `*-credentials` (AWS/Azure/Kubernetes) — feature-name под k8s-family lock (L99-anchor) → EN. `report`/`dashboard`/`subscription` — общие слова домена → переводятся («отчёт»/«дашборд»/«подписка»), терминология сверяется с corpus-доминантой (grep `дашборд*` vs `панел* мониторинга` → дашборд). L103 case (b) anchor (config-api той же семьи) распространяется ТОЛЬКО на shared OpenAPI-объекты (ErrorEnvelope/Error/ConstraintViolation/EntityShortRepresentation), НЕ на domain-лексику.

**Следующее (configuration-api остаток ~629 в dynatrace-api):** alerting-profiles-api 5+parent (deprecated, post/put 750/776 КРУПНЫЕ — отдельная сессия по L42-осторожности), automatically-applied-tags-api (models.md 1376=L42 отд.), service-api(62)/rum(53); env-api rum(24)/topology-and-smartscape(21 HUGE). DEFER L42: anomaly-detection-api/ aws/ vmware/ hosts/ metric-events/; settings/schemas 338.

Last update: 2026-05-16h

## Batch L4G — configuration-api/aws-credentials-api/ parent + 7 endpoints ЗАКРЫТ ЦЕЛИКОМ (8 файлов, Opus) — ЗАВЕРШЁН 2026-05-16f

АКТИВНЫЙ configuration-api подраздел (без deprecated-баннера, L89/L90). Standalone (env-api aws-twin'а нет, в отличие от credential-vault L4F) → чистый L99 config-api канон + k8s-credentials-api-api как anchor для shared объектов.

**aws-credentials-api/ закрыт целиком (8/8):**
- [x] `configuration-api/aws-credentials-api.md` (parent, card-link индекс 7 эндпоинтов в 3 блоках, без `## Related topics`, 32 строки)
- [x] `configuration-api/aws-credentials-api/get-all.md` (83 строки, пустой `#### Объект ResponseBody` + EntityShortRepresentation)
- [x] `configuration-api/aws-credentials-api/get-credentials.md` (333 строки, дерево AwsCredentialsConfig 3-кол.)
- [x] `configuration-api/aws-credentials-api/get-services.md` (189 строк, AwsMonitoredServicesDto+ConfigurationMetadata+AwsSupportingServiceConfig/Metric)
- [x] `configuration-api/aws-credentials-api/delete-credentials.md` (335 строк, AwsCredentialsConfig 3-кол. + `## Формат ответа`)
- [x] `configuration-api/aws-credentials-api/post-new-credentials.md` (615 строк, AwsCredentialsConfig 4-кол. + `## Получение токена external ID` + `## Validate payload`)
- [x] `configuration-api/aws-credentials-api/put-credentials.md` (617 строк, near-twin POST + id-параметр + 204-код)
- [x] `configuration-api/aws-credentials-api/put-services.md` (391 строка, AwsMonitoredServicesDto 4-кол. + Validate payload)

**Канон L99 (config-api, АКТИВНЫЙ → без баннера, L89/L90):** frontmatter `title:` / `# H1`×2 / `* Reference` / `* Published <date>` (get-services/put-services `Jul 28, 2022`; остальные `Jun 27, 2019`) — EN-вербатим. `The element can hold these values * X`→`Возможные значения: * X` (С двоеточием, k8s-канон). `In`→`Где` (header), cell `path`/`body`/`Required`/`Optional` EN-вербатим. Section-headers переведены (`## Authentication`→`## Аутентификация` и т.д.); `## Validate payload` EN; `## GET the external ID token`→`## Получение токена external ID`; `## Response format`→`## Формат ответа`.

**Канон-решения L4G (новые/подтверждённые):**
- **Терминология «AWS credentials» EN-вербатим** по anchor k8s-credentials-api-api RU (та же семья `*-credentials API`, L99 lock). k8s RU: «конфигурация Kubernetes credentials»/«Kubernetes credentials» (EN). aws → «конфигурация AWS credentials»/«AWS credentials»/«эти credentials» (EN). **Отличие от L4F credential-vault** где было «учётные данные»: там был активный env-api twin как domain-источник (L102 cross-canon), здесь twin'а нет → anchor = k8s той же семьи, а не twin.
- shared объекты вербатим из k8s-credentials-api-api RU (L85/L99-anchor): `EntityShortRepresentation`→«Краткое представление сущности Dynatrace.»/description «Краткое описание сущности Dynatrace.»/id «ID сущности Dynatrace.»/name «Имя сущности Dynatrace.»; `ConfigurationMetadata`→«Метаданные для отладки»/clusterVersion «Версия Dynatrace.»/configurationVersions+currentConfigurationVersions «Отсортированный список номеров версий конфигурации.»; `ErrorEnvelope`/`Error` («HTTP-код статуса»/«Список нарушений ограничений»/«Сообщение об ошибке»)/`ConstraintViolation` (desc «Список нарушений ограничений», `-Возможные значения: * \`HEADER\`…`).
- **`**Deprecated**` field-level bold-маркер → `**Устарело**`** (перевод + bold сохранён). Расширение L4B (`DEPRECATED`→`УСТАРЕЛО`) на bold-инлайн-вариант в описаниях полей (supportingServicesToMonitor / keyBasedAuthentication / KeyBasedAuthentication-объект). НЕ оставлять EN (это описательная проза, не type-токен).
- **BOM `ï»¿` в inline-link-текстах вычищен** (broken-char 0): `[/aws/supportedServicesï»¿]`→`[/aws/supportedServices]`, `[documentationï»¿]`→`[документации]`, `[/aws/credentials/{id}/servicesï»¿]`→`[/aws/credentials/{id}/services]`. URL-пути в link-тексте EN-вербатим, описательное `documentation`→`документации`.
- **L101: ВСЕ aws 400-строки EN `| Failed. The input is invalid. |` С точкой** → `Сбой. Невалидный ввод.` С точкой (единообразно во всех 8 файлах; в отличие от L4F где near-twin post/put различались). `Validated. The submitted configuration is valid. Response doesn't have a body.` → `Validated. Переданная конфигурация валидна. Ответ без тела.` (L4E канон). 201/204-описания со ссылкой `\`GET /aws/credentials/{id}\`` + двойными пробелами вербатим.
- Пустой `#### The \`ResponseBody\` object` (get-all, без таблицы) → `#### Объект \`ResponseBody\`` (L3Y канон). Source-dup `The request consumes an \`application/json\` payload.` ×2 подряд (post/put-credentials/put-services) сохранён вербатим (рендерим источник). mojibake `doesnât` (put-credentials EN-источник) → переведено прозой «не существует» (RU без `â`; broken-char 0). Card-link parent: heading/body/title переведены, URL/anchor нетронут, склейка `](url "title")[###` сохранена; «credentials» в heading EN-вербатим («### Список всех credentials»).
- AwsCredentialsConfig-дерево (10 объектов: AwsCredentialsConfig/AwsAuthenticationData/KeyBasedAuthentication/RoleBasedAuthentication/ConfigurationMetadata/AwsSupportingServiceConfig/AwsSupportingServiceMetric/AwsConfigTag) идентично в delete/get-credentials (3-кол.) и post-new/put-credentials (4-кол. +Обязательный с EN-cell Required/Optional) — переведено 1 раз + копия (L85), `connectionStatus`/`partitionType`/`statistic`/`supportingServicesToMonitor` с двойными пробелами и enum вербатим.

**Критический ревью (`scripts/_review_awscred.py`, 0 дефектов с ПЕРВОГО прогона):** force-sync ```-fenced EN→RU = **0 файлов нуждались в sync** (ручная JSON-транскрипция byte-identical, большие AwsCredentialsConfig-JSON + тройные пустые строки сохранены, L98/L100). line-parity EN==RU 8/8; heading/h4/fence/table-row паритет 8/8; em-dash 0; mojibake (`Â`/`Ã`/`ï»¿`/`â€`/**`â`**)/BOM 0; leftover-EN section-headers 0 (вкл. `## Формат ответа`/`## Получение токена external ID`; `## Validate payload`=канон-EN); EN-инварианты (title/H1×2/`* Reference`/`* Published`). Доп. семантич. spot-check: спурьёзного deprecated-баннера нет (API активный), env-api leak «может принимать» = 0, BOM clean, `**Устарело**` переведён, L101 все 400 = `.` (период по источнику), k8s ConfigurationMetadata/EntityShortRepresentation/Error канон present. **Правок не потребовалось** (4-й батч подряд 0-деф с первого прогона: L4B/L4E/L4F/L4G). verify_corpus.py: Translated **1422** (+8), Pending 1233, Orphan RU 0, source-check OK, dynatrace-api 459 done/647 pending.

**Lesson L103:** выбор domain-источника терминологии: (а) если есть **активный env-api twin** того же API (deprecated config-api ↔ active env-api) → L102 cross-canon (domain-проза из twin RU); (б) если twin'а НЕТ → anchor = ближайший уже-переведённый config-api той же **семьи API** (для `*-credentials API` это k8s-credentials-api-api: «X credentials» EN-вербатим, shared объекты оттуда). Не смешивать: «AWS credentials» EN (семья k8s-canon) ≠ «учётные данные» (credential-vault twin). Решение принимать по наличию/отсутствию twin'а, а не «как в прошлом батче».

**Следующее (configuration-api остаток ~639):** azure-credentials-api 7+parent (АКТИВНЫЙ, прямой twin aws по структуре → L85 применить), alerting-profiles-api 5+parent (deprecated, post/put 750/776 крупные), reports-api 7, automatically-applied-tags-api (models.md 1376=L42 отд.). DEFER L42: anomaly-detection-api/ aws/ vmware/ hosts/ metric-events/; settings/schemas 338.

Last update: 2026-05-16f

## Batch L4F — configuration-api/credential-vault/ parent + 6 endpoints ЗАКРЫТ ЦЕЛИКОМ (7 файлов, Opus) — ЗАВЕРШЁН 2026-05-16e

Deprecated configuration-api подраздел закрыт целиком. Особенность: у него есть **активный twin** `environment-api/credential-vault/` (тот же API, переехавший в Environment API), уже переведённый. Применён L85/L86 twin-паттерн cross-canon: domain-фразировка из twin RU, config-api структурный канон сверху.

**credential-vault/ закрыт целиком (7/7):**
- [x] `configuration-api/credential-vault.md` (parent, card-link индекс 5 эндпоинтов + `## Related topics`, 35 строк)
- [x] `configuration-api/credential-vault/del-credentials.md` (76 строк, 2-кол. Response codes)
- [x] `configuration-api/credential-vault/get-all.md` (488 строк, CredentialsList+CredentialsResponseElement[14 полей]+CredentialAccessData+CredentialUsageHandler+ExternalVaultConfig + большой JSON)
- [x] `configuration-api/credential-vault/get-credentials.md` (263 строки, те же объекты)
- [x] `configuration-api/credential-vault/models.md` (273 строки, CertificateCredentials/PublicCertificateCredentials/TokenCredentials/UserPasswordCredentials/ExternalVault + unix-команды base64)
- [x] `configuration-api/credential-vault/post-credentials.md` (417 строк, Credentials+CredentialAccessData+CredentialsId+ErrorEnvelope/Error/ConstraintViolation)
- [x] `configuration-api/credential-vault/put-credentials.md` (407 строк, near-twin POST + id-параметр + 204-код обновления)

**Канон L99 применён (config-api, НЕ env-api):** frontmatter `title:` / `# H1`×2 / `* Reference` / `* Published Oct 14, 2019` (parent `* Updated on Oct 04, 2022`) — EN-вербатим. `The element can hold these values * X`→`Возможные значения: * X` (С двоеточием, k8s-канон). `In`→`Где` (header), cell `path`/`query`/`body`/`Required`/`Optional` EN-вербатим. `#### Curl` EN (Validate payload в credential-vault нет). `## Authentication`→`## Аутентификация`, `## Parameters`→`## Параметры`, `## Response`→`## Ответ`, `### Response codes`→`### Коды ответа`, `### Response/Request body objects`→`### Объекты тела ответа/запроса`, `#### The \`X\` object`→`#### Объект \`X\``, `### Response body JSON models`→`### JSON-модели тела ответа`, `### Request body JSON model`→`### JSON-модель тела запроса`, `## Variations of the \`Credentials\` object`→`## Варианты объекта \`Credentials\``, `## Example`→`## Пример`, `## Related topics`→`## Связанные темы`, `#### Request URL`→`#### URL запроса`, `#### Request/Response body`→`#### Тело запроса/ответа`, `#### Response code`→`#### Код ответа`.

**Канон-решения L4F (новые/подтверждённые):**
- **L85/L86 twin cross-canon (новое применение):** активный `environment-api/credential-vault/` уже переведён (тот же набор объектов). Domain-фразировка (descriptions, имена, семантика) взята из twin RU вербатим (CredentialsResponseElement 14 полей, CredentialAccessData, CredentialUsageHandler, ExternalVaultConfig, CertificateCredentials/PublicCertificate/Token/UserPassword/ExternalVault, «учётные данные»/«набор учётных данных»/«synthetic-мониторов»/«внешним vault»/«scope»). Сверху наложен **config-api структурный канон**: twin env-api `Элемент может принимать значения` → config-api `Возможные значения:` (С двоеточием); twin header `| В |` → `| Где |`; twin cell `Опциональный`/`Обязательный` → `Optional`/`Required` EN (config-api L99); twin env-api ErrorEnvelope/Error/ConstraintViolation («Неудача»/«Поле») → config-api k8s-credentials вариант («HTTP-код статуса»/«Список нарушений ограничений»/`-Возможные значения:`).
- **Deprecated-баннер новый паттерн** «...Use the [Credential vault API](url "Learn what the Dynatrace API for credentials offers.") from the Environment API instead.» → «Этот API устарел. Используйте [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Узнайте, что предлагает Dynatrace API для credentials.") из Environment API.» (title по environment-api.md RU канону; link-текст `[Credential vault API]` EN; «from the Environment API» → «из Environment API»; «instead»/«вместо него» опускается по frequent-issue/L4E канону).
- **Lesson L101 подтверждён в near-twin паре:** `post-credentials.md` EN строка `| **400** | [ErrorEnvelope] | Failed. The input is invalid. |` С точкой → RU `Сбой. Невалидный ввод.` С точкой; `put-credentials.md` EN `| **400** | [ErrorEnvelope] | Failed. The input is invalid |` БЕЗ точки → RU `Сбой. Невалидный ввод` БЕЗ точки. Две почти идентичные файла различаются ТОЛЬКО точкой по источнику — это эталонная демонстрация L101 (точка ПО ИСТОЧНИКУ конкретной строки, грепать перед применением, не копировать у соседа).
- BOM `ï»¿` в link-тексте `[Credential vault API - JSON modelsï»¿](https://dt-url.net/2sa3sen)` (post/put Credentials desc) → вычищен `[Credential vault API - JSON models]` (broken-char 0; twin его НЕ чистил — мы строже).
- `~~scope~~` strikethrough field-name вербатим + cell `DEPRECATED  ` → `УСТАРЕЛО  ` (L4B/L3W, двойной пробел сохранён; twin оставлял `DEPRECATED` EN — мы по последнему канону L4B переводим).
- `### CERTIFICATE`/`### PUBLIC\_CERTIFICATE`/`### TOKEN`/`### USERNAME\_PASSWORD` (models.md) — EN-вербатим (enum type-токены, не заголовки-прозы; twin тоже EN). Bare-строки `CertificateCredentials`/`Parameters`/`JSON model` EN-вербатим (scraper-артефакт OpenAPI-рендера, twin тоже EN, не `##`-заголовки).
- Source-typo: del-credentials EN «the request updates the set of credentials» (но endpoint DELETE, «deletion was successful») → переведено по фактическому действию «запрос удаляет» (логика операции важнее опечатки, как PUT-example L4E «updated»→present).
- `[synthetic monitors]`/`[POST request example]`/`[JSON models]` inline-link-текст EN, title переведён (L4D/L4E cross-ref канон; «synthetic monitors» → «synthetic-мониторов» по twin как описательная проза-ссылка, регистр по источнику: «Synthetic monitors»→«Synthetic-мониторов», «synthetic monitors»→«synthetic-мониторов»). Related-topics `[Configure browser/HTTP monitors]` link-текст EN + title «Узнайте о настройке browser-мониторов и clickpath.»/«…HTTP-мониторов.» (twin endpoint-file рендер).

**Критический ревью (`scripts/_review_credvault.py`, 0 дефектов с ПЕРВОГО прогона):** force-sync ```-fenced EN→RU = **0 файлов нуждались в sync** (ручная JSON-транскрипция byte-identical, большие JSON get-all/post/put/models/get-credentials + unix-команды + тройные пустые строки сохранены, L98/L100). line-parity EN==RU 7/7; heading/h4/fence/table-row паритет 7/7; em-dash 0 (EN « - » в scopes → «,» по twin, не em-dash); mojibake/BOM 0 (`ï»¿` вычищен); leftover-EN section-headers 0 (вкл. `## Варианты объекта`); EN-инварианты (title/H1×2/`* Reference`/`* Published`+`* Updated on`). Доп. семантический spot-check: deprecated-баннер единообразен 7/7, env-api leak «может принимать» = 0, BOM clean, L101 post=`.` put=без точки подтверждён программно, k8s shared-object канон present. **Правок не потребовалось** (3-й батч подряд 0-деф с первого прогона: L4B/L4E/L4F). verify_corpus.py: Translated **1414** (+7), Pending 1241, Orphan RU 0, source-check OK, dynatrace-api 451 done/655 pending.

**Lesson L102:** при наличии активного twin-подраздела (deprecated config-api ↔ активный env-api с тем же набором объектов) применять L85/L86 cross-canon: domain-прозу брать из twin RU вербатим, НО структурный слой (enum-формула `Возможные значения:`/`Элемент может принимать`, header `Где`/`В`, cell EN/переведён, shared Error-объекты k8s/env) накладывать по канону СВОЕГО API-семейства. Twin даёт консистентность терминологии между старой и новой версией одного API (читатель сравнивает), канон даёт консистентность внутри config-api. Не копировать twin структурно вслепую.

**Следующее (configuration-api остаток ~648):** aws-credentials-api 7+parent (АКТИВНЫЙ, 0/7 deprecated), azure-credentials-api 7+parent (АКТИВНЫЙ), alerting-profiles-api 5+parent (deprecated, post/put 750/776 крупные), automatically-applied-tags-api (models.md 1376 = L42 отд.). DEFER L42: anomaly-detection-api/ aws/ vmware/ hosts/ metric-events/; settings/schemas 338.

Last update: 2026-05-16e

## Batch L4E — configuration-api/remote-environments/ parent + 5 CRUD ЗАКРЫТ ЦЕЛИКОМ (6 файлов, Opus) — ЗАВЕРШЁН 2026-05-16d

Deprecated configuration-api подраздел закрыт целиком (parent index + полный CRUD):

**remote-environments/ закрыт целиком (6/6):**
- [x] `configuration-api/remote-environments.md` (parent, card-link индекс 5 эндпоинтов, 28 строк)
- [x] `configuration-api/remote-environments/get-all.md` (204 строки, RemoteEnvironmentConfigListDto + RemoteEnvironmentConfigStub)
- [x] `configuration-api/remote-environments/get-remote-environment.md` (149 строк, RemoteEnvironmentConfigDto)
- [x] `configuration-api/remote-environments/del-remote-environment.md` (71 строка, 2-кол. Response codes)
- [x] `configuration-api/remote-environments/post-remote-environment.md` (441 строка, + Validate payload)
- [x] `configuration-api/remote-environments/put-remote-environment.md` (417 строк, near-twin POST + id-параметр + 204-код обновления)

**Канон L99 применён (config-api, НЕ env-api):** frontmatter `title:` / `# H1`×2 / `* Reference` / `* Published Nov 19, 2019` — EN-вербатим. `The element can hold these values * X`→`Возможные значения: * X` (С двоеточием, k8s-канон; env-api leak «Элемент/Поле может принимать» = 0). `In`→`Где` (header), cell `path`/`body`/`Required`/`Optional` EN-вербатим, переведён только header колонки. `## Validate payload` / `#### Curl` — EN. `## Authentication`→`## Аутентификация`, `## Parameters`→`## Параметры`, `## Response`→`## Ответ`, `### Response codes`→`### Коды ответа`, `### Response/Request body objects`→`### Объекты тела ответа/запроса`, `#### The \`X\` object`→`#### Объект \`X\``, `### Response body JSON models`→`### JSON-модели тела ответа`, `### Request body JSON model`→`### JSON-модель тела запроса`, `## Example`→`## Пример`, `#### Request URL`→`#### URL запроса`, `#### Request/Response body`→`#### Тело запроса/ответа`, `#### Response code`→`#### Код ответа`. Внутри Validate payload: `### Authentication/Response`→`### Аутентификация/Ответ`, `#### Response codes/body objects/body JSON models`→переведены.

**Канон-решения L4E (новые/подтверждённые):**
- **Deprecated-баннер по frequent-issue-detection-api RU канону** (тот же EN-паттерн «...instead. Look for the **X** (`id`) schema.»): `This API is deprecated. Use the [Settings API](… "Find out what the Dynatrace Settings API offers.") instead. Look for the **Remote environment** (\`builtin:remote.environment\`) schema.` → `Этот API устарел. Используйте [Settings API](… "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Remote environment** (\`builtin:remote.environment\`).` (link-текст `[Settings API]` EN, bold schema-имя `**Remote environment**` EN, слово «schema» EN, «instead»/«вместо него» опускается по frequent-issue-канону).
- `Failed. The input is invalid.`→`Сбой. Невалидный ввод.` **С ТОЧКОЙ** (точка ПО ИСТОЧНИКУ: здесь EN-источник `| Failed. The input is invalid. |` с точкой, как k8s-credentials; отличается от L4D disk-events где источник без точки → RU без точки). Правило подтверждено: точка следует за источником.
- `Validated. The submitted configuration is valid. Response doesn't have a body`→`Validated. Переданная конфигурация валидна. Ответ без тела.` (Validated. EN + хвост переведён + точка по k8s/L4D канон-строке, shared boilerplate L85).
- `Success. The configuration has been deleted. The response doesn't have a body.`→`Успех. Конфигурация удалена. Ответ без тела.`; `Success. A new remote environment configuration has been created. The response contains the ID of the new configuration.`→`Успех. Новая конфигурация удалённого окружения создана. Тело ответа содержит ID конфигурации.`; `Success. The configuration has been updated. The response doesn't have a body.`→`Успех. Конфигурация обновлена. Ответ без тела.` (L4D-канон); `Success`→`Успех`.
- **Shared ErrorEnvelope/Error/ConstraintViolation вербатим из k8s-credentials-api-api RU (L85, L99-anchor):** `#### Объект \`Error\`` / `code|HTTP-код статуса` / `constraintViolations|Список нарушений ограничений` (без точки) / `message|Сообщение об ошибке`; ConstraintViolation desc-строка `Список нарушений ограничений` (без точки); `parameterLocation | string | -Возможные значения: * \`HEADER\` * \`PATH\` * \`PAYLOAD_BODY\` * \`QUERY\``.
- networkScope-описание идентично во всех 5 эндпоинтах (L85): `Сетевая область удалённого окружения:  * \`EXTERNAL\`: … * \`INTERNAL\`: … * \`CLUSTER\`: … Dynatrace SaaS может использовать только \`EXTERNAL\`.  Если не задано, используется \`EXTERNAL\`. Возможные значения: * …` (двойные пробелы scraper-артефакта сохранены вербатим). token-scope `**Fetch data from a remote environment**` (`RestRequestForwarding`) bold-имя EN.
- Source-bug вербатим: get-all/post/put `RemoteEnvironmentConfigStub.uri` описан как «The display name…» → переведено как есть `Отображаемое имя удалённого окружения.` (рендерим источник, не «чиним»).
- Card-link parent формат по L4D applications RU: `[### List all environments\n\nbody](url "title")[### View an environment…]` → heading→«### Список всех окружений»/«### Просмотр окружения»/«### Создание окружения»/«### Редактирование окружения»/«### Удаление окружения», body переведён, title переведён, URL/anchor нетронут, склейка `](url "title")[###` сохранена. Cross-ref `[POST request]` link-текст EN + title переведён («Создание удалённого окружения Dynatrace через Dynatrace API.»). PUT example source-typo «the request updated» (past) → present «обновляет» (регистр корпуса, смысл не меняется).

**Критический ревью (`scripts/_review_remote_env.py`, 0 дефектов с ПЕРВОГО прогона):** force-sync каждого ```-fenced блока EN→RU = **0 файлов нуждались в sync** (ручная JSON-транскрипция byte-identical, тройные пустые строки scraper-артефакта сохранены, L98/L100). line-parity EN==RU 6/6; heading/h4/fence/table-row паритет 6/6; em-dash 0 (нет самодобавленного «X — Y», CLAUDE rule #0); mojibake/BOM (`Â`/`Ã`/`ï»¿`/`â€`) 0; leftover-EN section-headers 0 (с поправкой `## Validate payload`/`#### Curl` = канон-EN); EN-инварианты (title/H1×2/`* Reference`/`* Published`) идентичны EN. Доп. семантический spot-check: deprecated-баннер канон единообразен во всех 6, нет env-api leak «может принимать», нет leftover-EN прозы, ID/числа (b597955c…/c89b9d9f…/200/201/204/400) сохранены. **Правок не потребовалось** (как L4B). verify_corpus.py: Translated **1407** (+6), Pending 1248, Orphan RU 0, source-check OK, dynatrace-api 444 done/662 pending.

**Lesson L101:** «точка после `Сбой. Невалидный ввод`» определяется ПО ИСТОЧНИКУ конкретного файла, НЕ по подразделу. k8s-credentials/remote-environments источник `| Failed. The input is invalid. |` с точкой → RU с точкой; L4D disk-events источник без точки → RU без точки. Проверять EN-ячейку грепом перед применением, не копировать вслепую правило соседнего батча. (Дополняет L4D-заметку про process-groups↔disk-events расхождение.)

**Следующее (configuration-api остаток ~656):** мелкие CRUD-подразделы под L99+L4E-канон (aws-credentials-api 7, azure-credentials-api 7, alerting-profiles-api 5, credential-vault 6 c models.md, automatically-applied-tags-api 6 но models.md 1376 строк = L42 отдельная сессия). DEFER L42 anomaly-detection-api/: aws/ vmware/ hosts/ metric-events/. settings/schemas 338 = огромный отдельный пласт.

Last update: 2026-05-16d

## Batch L4D — configuration-api/anomaly-detection-api/ applications + database + services + главный parent ЗАКРЫТЫ ЦЕЛИКОМ (10 файлов, Opus) — ЗАВЕРШЁН 2026-05-16c

Продолжение configuration-api/anomaly-detection-api/ (после L4C process-groups+disk-events). Закрыты 3 структурно-двойниковых подраздела целиком + главный parent:

**applications/ закрыт целиком (3/3):**
- [x] `anomaly-detection-api/anomaly-detection-api-applications.md` (parent index)
- [x] `anomaly-detection-api/anomaly-detection-api-applications/get-config.md` (430 строк)
- [x] `anomaly-detection-api/anomaly-detection-api-applications/put-config.md` (731 строка)

**database/ закрыт целиком (3/3):**
- [x] `anomaly-detection-api/anomaly-detection-api-database.md` (parent index)
- [x] `anomaly-detection-api/anomaly-detection-api-database/get-config.md` (433 строки)
- [x] `anomaly-detection-api/anomaly-detection-api-database/put-config.md` (750 строк)

**services/ закрыт целиком (3/3):**
- [x] `anomaly-detection-api/anomaly-detection-api-services.md` (parent index)
- [x] `anomaly-detection-api/anomaly-detection-api-services/get-config.md` (437 строк)
- [x] `anomaly-detection-api/anomaly-detection-api-services/put-config.md` (704 строки)

**Главный parent (1/1):**
- [x] `configuration-api/anomaly-detection-api.md` (51 строка, индекс на все подразделы вкл. ещё не переведённые aws/hosts/vmware)

**Канон L99 применён (config-api, НЕ env-api):** frontmatter `title:` / `# H1`×2 / `* Reference` / `* Published <date>` — EN-вербатим. `The element can hold these values * X`→`Возможные значения: * X` (С двоеточием, k8s-канон; env-api leak «Элемент/Поле может принимать» = 0). `In`→`Где`. Cell-значения `Required`/`Optional`/`body` — EN-вербатим, переведён только header колонки (`Required`→`Обязательный` в шапке). `## Validate payload` / `#### Curl` — EN. `## Authentication`→`## Аутентификация`, `## Parameters`→`## Параметры`, `## Response`→`## Ответ`, `### Response codes`→`### Коды ответа`, `### Response/Request body objects`→`### Объекты тела ответа/запроса`, `#### The \`X\` object`→`#### Объект \`X\``, `### Response body JSON models`→`### JSON-модели тела ответа`, `### Request body JSON model`→`### JSON-модель тела запроса`, `## Example`→`## Пример`, `## Related topics`→`## Связанные темы`, `#### Request URL`→`#### URL запроса`, `#### Request/Response body`→`#### Тело запроса/ответа`, `#### Response code`→`#### Код ответа`, `#### Result`→`#### Результат`.

**Канон-решения L4D (новые/подтверждённые):**
- `Failed. The input is invalid` → `Сбой. Невалидный ввод` **БЕЗ точки** (источник без точки, канон disk-events RU; отличается от process-groups `Failed. Invalid input.`→`Сбой. Невалидный ввод.` с точкой — точка ПО ИСТОЧНИКУ, L4C).
- `Success. Configuration has been updated...`→`Успех. Конфигурация обновлена. Ответ без тела.`; `Validated. ...`→`Validated. Переданная конфигурация валидна. Ответ без тела.` (Validated. EN + хвост переведён).
- «service/services/application/applications/database services» — **переведены** («сервис»/«приложение»/«сервис баз данных»): НЕ в keep-EN списке L4C (там только process group/disk event/host group/network zone). Отличие от L4C где «process group» оставался EN.
- Related-topics: link-**текст EN**, только **title переведён** (как disk-events `[Adjust the sensitivity...]` text EN + title «Настройка чувствительности обнаружения проблем для X.»). `DavisÂ®`→`Davis®` + title «Познакомьтесь с возможностями Davis AI.». `[Services]`/`[Databases]` text EN (doc-name, как `[Process groups]`), title переведён.
- Mojibake `Anomaly detectionâServices`/`âApplications`/`âDatabase services` (parent intro) → `Anomaly detection-Services` и т.д. (дефис, broken-char 0); UI-path `**Settings** > **Anomaly detection** > **X**` bold-токены EN-вербатим.
- Card-link parent формат (`[### Heading\n\nbody](url "title")[### Heading2...]`) по process-groups RU L4C: heading→«### Просмотр конфигурации»/«### Обновление конфигурации», title→«Просмотр/Обновление конфигурации обнаружения аномалий для X через Dynatrace API.». Главный top-parent (не sub-parent): `### Application`→`### Приложения`, `### Host`→`### Хосты`, `### AWS`/`### VMware`/`### Disk events` EN; link-text «View/Update configuration»→«Просмотр/Обновление конфигурации», disk-events titles по disk-events parent RU («Просмотр всех правил disk event … через Dynatrace API.»).
- image alt+caption (`![Anomaly detection config - services](url)` + строка-подпись) — **EN-вербатим** (канон process-groups RU get/put, scraper-артефакт).

**Критический ревью (`scripts/_review_anomaly_l4d.py`, 0 дефектов после фиксов):** скрипт force-sync'ит каждый ```-fenced блок EN→RU (код не переводится → byte-identity гарантирована, L98) — **0 файлов нуждались в sync = JSON-транскрипция вручную была верной**. Проверки: line-parity EN==RU, heading/h4/fence/table-row паритет, em-dash 0, mojibake/BOM (`Â`/`Ã`/`ï»¿`/`â€`) 0, leftover-EN section-headers 0 (с поправкой `## Validate payload`/`#### Curl` = канон-EN, не флагать), EN-инварианты (title/H1×2/`* Reference`/`* Published` идентичны EN). **2 дефекта пойманы-исправлены:** (1) самодобавленный em-dash в фразе «должны быть превышены **оба** порога — абсолютный и относительный» (6 файлов, ×2 каждый) → заменён на `: ` (CLAUDE rule #0 — em-dash главный маркер ИИ); (2) `database/put-config.md` пропущены объекты `LoadDropDetectionConfig`+`LoadSpikeDetectionConfig` в Request body objects (−20 строк, −2 h4, −10 table-row) → вставлены между FailureRateIncreaseThresholdConfig и ConfigurationMetadata по EN-порядку. verify_corpus.py: Translated **1401** (+10), Pending 1254, Orphan RU 0, source-check OK.

**Lesson L100:** при ручном написании RU-файла с большим verbatim-JSON не полагаться на «глаз» — обязателен post-pass скрипт, который force-sync'ит ```-fenced блоки EN→RU позиционно (assert равное число fence'ов) + line/heading/table-row паритет. Это ловит И JSON-дрейф, И структурные пропуски (здесь: целиком пропущенные 2 объекта в одном из 10 файлов — глазами не виден на 750 строках). Параллельно: грепом проверять «самодобавленный» em-dash (переводчик склонен вставлять «X — Y» там где в EN его не было; CLAUDE rule #0).

**Остаток anomaly-detection-api/ (отд. сессии, L42 большой файл = стоп):** aws/ (parent + get-config 602 + put-config 903), vmware/ (parent + get-config 597 + put-config 922), hosts/ (parent + get-config 967 + put-config 1170 — БОЛЬШИЕ), metric-events/ (json-models 688 + post-event 731 — нет parent .md). Канон L99+L4D применять ко всем. После anomaly-detection-api/ полностью: configuration-api/ rum / calculated-metrics / service-api (62) и т.д.

Last update: 2026-05-16c

## Batch L4C — configuration-api/anomaly-detection-api/ process-groups + disk-events ЗАКРЫТЫ ЦЕЛИКОМ (10 файлов, Opus) — ЗАВЕРШЁН 2026-05-16b

Старт configuration-api/anomaly-detection-api/ (31 файл всего). Закрыты 2 подраздела целиком:

**process-groups/ закрыт целиком (4/4):**
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups.md` (parent index)
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/del-config.md`
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/get-config.md`
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups/put-config.md`

**disk-events/ закрыт целиком (6/6):**
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events.md` (parent index)
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/del-event.md`
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/get-all.md`
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/get-event.md`
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/post-event.md`
- [x] `configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/put-event.md`

**Lesson L99 (КРИТИЧНО — канон configuration-api ≠ environment-api):** канон locked по самому свежему закрытому **configuration-api** RU (L2P: k8s-credentials-api-api/maintenance-windows-api/conditional-naming, 2026-05-14), НЕ по env-api L4A/L4B. Расхождения config-api vs env-api:
- H1×2 title — **оставляется EN вербатим** (k8s/maintenance/conditional-naming все EN). env-api L4B переводил действие — для config-api НЕ применять.
- `* Reference` / `* Published <date>` / `* Updated on <date>` — **оставляются EN вербатим** (config-api). env-api L4A/L4B → `* Справочник`/`* Опубликовано` — для config-api НЕ применять.
- ConstraintViolation element-вариант `-The element can hold these values * \`HEADER\`…` → **`-Возможные значения: * \`HEADER\`…`** (С двоеточием, config-api k8s-канон). env-api L95 `-Элемент может принимать значения` (без двоеточия) — для config-api НЕ применять. Тот же `Возможные значения:` для всех `The element can hold these values` (method/metric/operator/context/endpointStatus).
- Колонка `In` параметр-таблицы → **`Где`** (config-api k8s). env-api L96 → `В` — для config-api НЕ применять.
- Cell-значения `Required`/`Optional` в Parameters И в Request/Response body object-таблицах — **оставляются EN вербатим** (только заголовок колонки → `Обязательный`).
- `## Validate payload` — **оставляется EN** (k8s put line 302). `#### Curl` — EN.

**Канон-словарь L4C (config-api):** `## Authentication`→`## Аутентификация`, `## Parameters`→`## Параметры`/`## Parameter`→`## Параметр`, `## Response`→`## Ответ`, `### Response codes`→`### Коды ответа`, `### Response body objects`→`### Объекты тела ответа`, `### Request body objects`→`### Объекты тела запроса`, `### Response body JSON models`→`### JSON-модели тела ответа`, `### Request body JSON model`→`### JSON-модель тела запроса`, `#### The \`X\` object`→`#### Объект \`X\``, `## Example`→`## Пример`, `## Related topics`→`## Связанные темы`, `#### Request URL`→`#### URL запроса`, `#### Response body`→`#### Тело ответа`, `#### Request body`→`#### Тело запроса`, `#### Response code`→`#### Код ответа`, `#### Result`→`#### Результат`. Заголовки таблиц: `Code/Type/Description`→`Код/Тип/Описание`, `Element`→`Элемент`, `Parameter`→`Параметр`. Стандарт-фразы: produces→`Запрос возвращает payload`, consumes→`Запрос принимает payload`, consumes and produces→`Запрос принимает и возвращает payload`, scope-фраза/Tokens-фраза/`В запросе нет настраиваемых параметров.`/`Сбой. Невалидный ввод[.]` (точка ПО ИСТОЧНИКУ — process-groups с точкой, disk-events без), 204→`Успех. … Ответ без тела.`, 201→`Успех. … создано. Возвращается ID …`, `Validated.`→оставлено EN + перевод хвоста, `Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.` (k8s put RU).

**Мелочи:** mojibake `Â®`→`®` (Davis® AI); `â` в имени API parent (`Anomaly detectionâProcess groups`/`âDisk events`) → дефис `Anomaly detection-Process groups`/`-Disk events` (без em/en-dash, broken-char 0); BOM в link-тексте убран; Related-topics title `[Davis® AI]`→`"Познакомьтесь с возможностями Davis AI."` (канон dynatrace-api entity-v2 RU), `[Process groups]` title переведён (config-api переводит Related-titles: maintenance/conditional-naming прецедент), `adjust-sensitivity-infastructure` title→`"Настройка чувствительности обнаружения проблем для инфраструктуры."` (канон 2/3 corpus); «process group»/«disk event»/«host group»/«network zone» — feature-имена оставлены EN, «rule»→«правило», «sample»→«семпл», «custom»→«кастомный». del-event Response codes — 2-колоночная `| Код | Описание |` (без Type, по источнику). Parent card-headings: «List/View/Create/Edit/Delete X»→«Список всех/Просмотр/Создание/Редактирование/Удаление X» (noun-форма, conditional-naming-стиль). Inline prose-link `[manage]`→`[управлять]` (не имя дока → переводится).

**Критический ревью (0 дефектов, _review_anomaly.py EN↔RU):** строки 10/10 EN==RU (после strip trailing-newline — закрытые config-api RU без финального `\n`, last byte `)`), heading-паритет 10/10, fence-паритет 10/10, table-row-паритет 10/10, code-block byte-identical EN==RU все блоки (JSON с тройными пустыми строками + curl + URL вербатим), em-dash 0, mojibake/BOM (`ï»¿`/`Â`/`â`/`Ã`) 0, leftover-EN 0 (с поправкой: `## Validate payload`/`#### Curl` НЕ flag'ить — канон EN). 1 дефект пойман-исправлен в процессе: del-event `#### Request URL` забыл перевести → `#### URL запроса`. verify_corpus.py: Translated **1391** (+10), Pending 1264, Orphan RU 0, source-check OK.

**Остаток anomaly-detection-api/ (для следующих сессий, ~21 файл + parent):** applications(parent+get/put-config), aws(parent+get/put), database(parent+get/put), hosts(parent+get-config 967стр+put-config 1170стр — БОЛЬШИЕ, отд. сессия), metric-events(json-models 688+post-event 731), services(parent+get/put), vmware(parent+get-config 597+put-config 922), + parent `anomaly-detection-api.md`. Канон L99 применять ко всем (config-api, НЕ env-api).

Last update: 2026-05-16b

## Batch L4B — oneagent-on-a-host/ ЗАКРЫТ ЦЕЛИКОМ (1 файл, Opus) — ЗАВЕРШЁН 2026-05-16a

Снят DEFER из L4A. Единственный файл подраздела, 1205 строк, активный API (Published Feb 03 2020, без `* Deprecated` → без баннера, L90).

- [x] `environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md` (1205 строк)

**Метод (splice, для файлов с доминирующим verbatim-JSON):** RU head строки 1-329 (frontmatter+title×2, 33 query-параметра, Response codes, 16 объектов HostsListPage/HostAgentInfo/Host[~90 полей]/AgentVersion/AnyValue/HostGroup/EntityShortRepresentation/TechnologyInfo/TagInfo/ModuleInfo/ModuleInstance/PluginInfo/PluginInstance/ErrorEnvelope/Error/ConstraintViolation) авторски переведены в `_ru_head.txt`; JSON-блок строки 330-1202 (873 строки, 2 code-fence: hosts-ответ + error) СКОПИРОВАН ВЕРБАТИМ из EN Python-скриптом (`head + en[329:1202] + ["## Связанные темы", blank, переведённый bullet]`). Подтверждено: `en[329:1202]==ru[329:1202]` byte-identical. Этот метод исключает риск ручной транскрипции 800+ строк JSON с тройными пустыми строками.

**Канон-решения L4B:**
- `~~currentActiveGateId~~` strikethrough сохранён вербатим; `DEPRECATED  This field is deprecated…  Use the **currentActiveGateIds** field instead.` → `УСТАРЕЛО  Это поле устарело и предоставлено для обратной совместимости.  Используйте вместо него поле **currentActiveGateIds**.` (DEPRECATED→УСТАРЕЛО L3W, двойные пробелы сохранены).
- shared ErrorEnvelope/Error/ConstraintViolation = element-вариант L95: `| Элемент |`, `-Элемент может принимать значения * \`HEADER\`…` БЕЗ двоеточия/точек (источник «The element can hold», как activegates RU). 34 cell'а «The element can hold these values» → 34 «Элемент может принимать значения», enum-значения вербатим (9 spot-check byte-identical: availabilityState/detailedAvailabilityState[param+HostAgentInfo]/osType/cloudType/pluginState/Host.osType/Host.paasType/Host.hypervisorType).
- `* Reference`/`* Published Feb 03, 2020` → `* Справочник`/`* Опубликовано 03 февраля 2020`; «one of the following scopes» → «один из следующих scope:» + bullets `oneAgents.read`/`DataExport`. Optional→Необязательный (33/33), In→В, query вербатим.
- **network zone / management zone / host group оставлены англ.** (канон network-zones RU L2V: «network zone» 87×; «management zone» 1× — устоявшиеся feature-имена, не переводятся как «сетевая зона»).
- BOM `ï»¿` в link-текстах `[GET all network zones]`/`[GET available versions]`×3/`[Dynatrace classic licensing]` убран, link-текст англ. (имена вызовов/доков), title без изменений (без title-атрибута у этих ссылок).
- Related-topics: `## Related topics`→`## Связанные темы`; bullet `[OneAgent configuration on a host API](…oneagent-on-host "Управление конфигурацией OneAgent-инстансов на ваших хостах через Dynatrace API.")` — title по канону config-api RU (греп), link-текст англ.
- title H1×2 `OneAgent on a host - GET список хостов с деталями OneAgent` («OneAgent on a host» = имя API, не переводится; переведено действие).

**Критический ревью (0 дефектов):** em-dash 0, mojibake/BOM 0, JSON byte-identical EN==RU (873/873), heading 25/25, fence 4/4, table-row 220/220, строки 1205/1205, нет leftover EN-секций/метадаты, нет stale «Опциональный». verify_corpus.py: Translated 1381, Pending 1274, Orphan RU 0, oneagent-on-a-host pending 0.

**Lesson L98 (новое):** для файлов где >60% объёма = verbatim JSON-пример (здесь 873/1205 = 72%): не переводить вручную весь файл (риск порчи JSON-структуры/тройных пустых строк на 800+ строках). Метод splice: (1) автору перевести только «голову» (header+params+objects) в scratch-файл, (2) Python-скриптом склеить `RU_head + EN[json_slice] + RU_tail`, (3) assert'ами зафиксировать границы (`### Response body JSON models` / закрывающий fence / `## Related topics`), (4) проверить `en[a:b]==ru[a:b]` byte-identical. Границы JSON находить грепом `^\`\`\`$` + точные line-номера ДО написания скрипта (была off-by-one: закрывающий fence на en[1200]=строка1201, не en[1201]).

**L4A перепроверен 2026-05-16a:** все 11 файлов (metrics-units/log-monitoring-v2/events-v1) повторно прогнаны — em-dash 0, mojibake 0, паритет OK, L95-канон ConstraintViolation идентичен во всех (1 уникальная строка), L96 Необязательный/Обязательный, нет leftover EN. Дефектов 0, правок не потребовалось.

## Batch L4A — environment-api/ 3 малых подраздела ЦЕЛИКОМ (11 файлов, Opus) — ЗАВЕРШЁН 2026-05-15p

**metrics-units/ закрыт целиком (3/3)** — активный v2 API, источник `* Reference`/`* Published` → `* Справочник`/`* Опубликовано <DD месяца YYYY>`, без баннера (L89/L90, нет `* Deprecated`):

- [x] `environment-api/metrics-units/get-all-units.md`
- [x] `environment-api/metrics-units/get-unit.md`
- [x] `environment-api/metrics-units/get-unit-convert.md`

**log-monitoring-v2/ закрыт целиком (4/4)** — активный API, источник `* Reference`/`* Updated on` → `* Справочник`/`* Обновлено <date>`, без баннера; cross-link titles по log-monitoring-v2.md sub-index RU (L87: «Получение записей логов через Log Monitoring API v2.» и т.д.); «Log Monitoring» в link-тексте оставлен англ.; mojibake `â` (text/plain/json-lines, ampersand/key-value) → запятая/дефис (em-dash 0); BOM `ï»¿` в «Dynatrace search query language»/«documentation»/«DPS license» убран:

- [x] `environment-api/log-monitoring-v2/get-search-logs.md`
- [x] `environment-api/log-monitoring-v2/get-export-logs.md`
- [x] `environment-api/log-monitoring-v2/get-aggregate-logs.md`
- [x] `environment-api/log-monitoring-v2/post-ingest-logs.md`

**events-v1/ закрыт целиком (4/4)** — DEPRECATED, источник `* Reference`/`* Updated on Jun 13, 2022`/`* Deprecated` + «This API is deprecated. Use the [Events API v2]…» → RU `* Справочник`/`* Обновлено 13 июня 2022` (bullet `* Deprecated` ОПУСКАЕТСЯ) + баннер «Этот API устарел. Используйте вместо него [Events API v2](… "Узнайте, что можно делать с Dynatrace Events API v2.")." (порядок «Используйте вместо него [link]» по problems/comments-эндпоинт-канону, link-текст англ., title по events-v1.md sub-index RU L87). jenkins имеет `* Deprecated` bullet, но БЕЗ баннер-фразы в источнике → RU без баннера (рендерим что в источнике). Parameters-mapping req/opt/n/a и event-type enum — вербатим, колонки-заголовки переведены; Related-topics 3 bullets идентичны (link-текст англ., BOM в YouTube-ссылке убран):

- [x] `environment-api/events-v1/get-event.md`
- [x] `environment-api/events-v1/get-events-feed.md`
- [x] `environment-api/events-v1/post-event.md`
- [x] `environment-api/events-v1/push-deployment-events-from-jenkins.md`

**Lesson L95:** shared ErrorEnvelope/Error/ConstraintViolation у element-source-варианта («The element can hold these values», без `:`, описания без точки) рендерятся как `| Элемент | …` + `-Элемент может принимать значения * \`HEADER\` …` (БЕЗ двоеточия, БЕЗ точек) — это отдельный канон от Поле-варианта synthetic v1/remote-configuration (`-Поле может принимать значения:` с двоеточием). Критерий выбора — что в источнике (`element` vs `field`, есть `:` или нет, есть `.` или нет), L85 «идентично в подкаталоге» применяется ПОСЛЕ выбора варианта по источнику. Источник-партнёр для копирования канона — activegates RU (тот же source-text).

**Lesson L96:** «Optional/Required» в env-api param-таблице → `Необязательный`/`Обязательный` (НЕ `Опциональный` — это устаревший activegates-era вариант; по L91 берём самый свежий закрытый env-api RU = synthetic v1/remote-configuration). «In» колонка → `В`, `path`/`query`/`body`/`header` вербатим.

**Lesson L97:** DEPLOYED-status checker = `verify_corpus.py` (1380/2655, Orphan 0). `validate_translations.py` УСТАРЕЛ (ищет `..\docs\ru`, до реструктуризации на managed-ru/) — не использовать, паритет проверять греп-счётчиками heading/fence/table-row EN↔RU.

**DEFER (НЕ начат):** `environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md` — 1204 строки, единственный файл подраздела, активный API (Published Feb 03, 2020, без Deprecated → без баннера). Объекты HostsListPage/HostAgentInfo/Host/ModuleInfo/PluginInfo + огромные enum (detailedAvailabilityState ~35 значений) + `~~currentActiveGateId~~` strikethrough+`DEPRECATED`→`УСТАРЕЛО` вербатим (L3W) + большой JSON-пример. Отложен под отдельную сессию целиком (no half-finished, L42: большой файл = стоп).

Last update: 2026-05-15p

## Batch L4-IF.59 + L4-IF.60a-e — setup-on-k8s/guides/migration (2026-06-19)

Migration top-level fully translated (8 files, EN->RU line-parity builders + per-batch QA, all 0 FAIL/0 WARN):
- L4-IF.59 (3): migration.md (card-grid index), migration/migrate-dto-to-tenant.md, migration/migrate-to-helm.md
- L4-IF.60a-e (5): dynakube.md, migrate-to-dto.md, cloud-native-to-app-monitoring.md, classic-to-cloud-native.md, classic-to-app-monitoring.md

Builders: _build_migration_l4if59.py, _build_dynakube_l4if60a.py, _build_migrate_to_dto_l4if60b.py, _build_cn_to_appmon_l4if60c.py, _build_classic_to_cn_l4if60d.py, _build_classic_to_appmon_l4if60e.py (+ matching _qa_*).
QA gained strip-aware FENCE_RE (r"^\s*```") so list-indented code fences no longer false-positive as EN-leftover.
Critical review fixes: Manifest tab kept latin (was "Манифест") for Helm-pairing consistency; "Cloud native app only" caption -> "Только приложения (cloud-native)"; "перенести с X на Y" -> "выполнить миграцию с X на Y" x2; comparison label "Classic full-stack monitoring" -> "Мониторинг классического full-stack" (parallel to "Мониторинг приложений").
Progress: 2404 -> 2412 / 2655 (90.85%), pending 251 -> 243. Remaining migration: only api-version-migration-guides/ subfolder.
