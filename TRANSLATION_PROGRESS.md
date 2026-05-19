# Translation Progress — docs/managed/ → docs/managed-ru/

Started: 2026-05-12
Last update: 2026-05-19 (Opus 4.7 +30 = **1756/2655 = 66.14%**, pending 899, Orphan RU 0, dynatrace-api 793 done/313 pending; **L4-AF environment-api/settings/schemas.md parent + 29 schemas/app-dynatrace-*.md = 30ф ЗАКРЫТ → app-dynatrace schema-tables 100% (остаток settings/schemas/ = 307 builtin-* + get-all.md + get-schema.md = 309ф = ОТДЕЛЬНАЯ серия L4-AG, вероятно twin-splice — builtin schema-доки очень повторяющиеся). ~1.9K EN-строк, БЕЗ fenced code. **АКТИВНЫЙ Settings 2.0 API** (title/source/scraped + ОБА `# Settings API - X schema table` H1 + `* Reference`(parent only)/`* Published <date>` EN-verbatim; без `* Deprecated`; line-parity EXACT EN==RU). **anchor = shipped L4-AE objects/ same-subsection (L4T#1 сильнейший: только что отгружен, та же подсекция environment-api/settings/)**. Auth-предложение: schemas EN структурно ≠ objects EN (combined single-line + bold **Read settings** vs split), но canon-инвариантные части ПО shipped objects/ RU: «Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](url).» (НЕ «этого запроса», НЕ «использовать его» — orchestrator REAL-grep shipped поймал script-deviation ДО build). `## Аутентификация`/`## Параметры` ПЕРЕВОД; ENUM-фраза `The element has these enums`→`Возможные значения:` двоеточие (L99/L4-AE, НЕ pre-L99 «Элемент может принимать»), enum-список `* \`a\` * \`b\`` verbatim. **DISPLAY_NAME = SINGLE source of truth (builder), используется И parent-row builder И per-file `### <Name> (\`app:...)\`` heading — имя резолвится единственным образом; 362 parent-rows + 29 ### headings, 0 missing, duplicate-names детерминированы (consistency guarantee).** **`Property`→`Свойство` = НОВАЯ header-форма**: distinct source-term ≠ corpus-dominant `Element`(643×)/`Поле`(70×)/`Parameter`, НЕ в L4-AE EN-lock-списке, 0 shipped precedent → faithful translate, становится first-occurrence канон для 307 builtin L4-AG (EN-lock-список авторитетен: переводим что НЕ в списке). `schema`/`Settings API` EN-lock (`Получить schema через Settings API`). EN-verbatim: schema-meta `| Schema ID | Schema groups | Scope |` + sep + value-row; GET-endpoint table (`|  |  |  |` + GET/Managed/SaaS/Environment ActiveGate + URL); **scopes-column ЦЕЛИКОМ EN-verbatim (scope/scopes L4-AE EN-lock, 0/362 non-verbatim)**; `[Tokens and authentication]` link-text EN; IBM `| [IBM Integration Bus | IBM App Connect Enterprise](url) |` literal-`|`-в-link-text source-quirk byte-identical EN==RU (L93 faithful mirror). BOM: 3-char `ï»¿` ВНУТРИ link-text gitlab/kubernetes/SRG/slack strip (0 residual в 30ф); `[here]`→`[здесь]` descriptive-prose link-text ПЕРЕВОД (L4Y#4) ≠ `[Tokens and authentication]` EN; product/UI EN-lock (Microsoft Azure App registrations/Red Hat Event Streams/kube-system/Kubernetes Connector/Dynatrace Operator/guardians/objectives/workflow/Business flow/AppEngine/KPI/Smartscape). description-line под `### Name` = whole-line exact map (DESCRIPTIONS/NOTES/LINK_LINES `\n…\n`-anchored). Build `scripts/_build_schemas_l4af.py` (CRLF→LF + U+FEFF + 3-char-BOM strip, exact-string canon, line-parity EXACT — только текст ВНУТРИ строки). **Pre-build orchestrator audit (feedback_full_audit_before_action) поймал+фикс 3: (1) PARAM_DESC `Correlation ID` desc-cell повторяет label → leftover-EN (biz-flow:45) → +`ID корреляции` + `KPI`-identity; (2)+(3) STRUCT auth-предложение 2 canon-deviation vs shipped objects/ («этого запроса»→«запроса», «использовать его»→«использовать токен»).** **Критич.ревью (orchestrator mandatory)** `scripts/_review_schemas_l4af.py` (копия `_review_settings_l4ae.py` + **импортирует builder DISPLAY_NAME = consistency-gate 391 проверок (parent-row name ≡ per-file ###-heading name)** + schema-EN-invariants meta/H1/Reference/Published/schema-meta/GET-endpoint/Tokens-link + LEFTOVER + integrated LATIN-RUN≥5 + SHORT 2-4w + schemas EN-verbatim cell-vocab excl): build-pass review 0 структурных деф, НО orchestrator semantic-read РЕАЛЬНОГО shipped RU поймал **1 whole-class деф (structural-green≠semantic 10-й раз): parent table-header `| Name | Schema | Scopes |` — `Name` leftover-EN (single-word-cell: LATIN-RUN≥5 И SHORT≥2w ОБА пропускают, Name=1 слово)** → fix `Name`→`Имя` (corpus-dominant `| Имя |` 5× shipped; `Schema`/`Scopes` EN-lock L4-AE) + header в harness LEFTOVER exact-match portable forward → rebuild + **independent re-review [OK] 0 структурных деф**. LATIN-RUN 48 + SHORT-RUN 8 orchestrator-triage ВСЕ LEGIT (scopes-column EN-verbatim 0/362 + product/acronym EN-lock внутри переведённых ячеек; comprehensive desc-scan ВСЕХ 29 app param-desc на tell-tale EN (the/with/your/this/…) = **0 suspect leftover-EN — НЕТ L4-AC `VM CPU ready` класса**). Семантик spot-check 6ф (abuseipdb/biz-flow/gitlab/SRG/kubernetes/schemas.md-parent): faithful, 3 build-fixes verified working (Correlation ID→ID корреляции, auth-канон, Name→Имя), em-dash 0, mojibake 0, BOM 0 residual, line-parity EXACT 30/30 (parent 377==377). diff +30 (1726→1756 = **66.14%**, pending 929→899, dynatrace-api 763→793/343→313, ingest-from 586 НЕ тронут, Orphan RU 0, source-check 0). **Lesson L4-AF:** (1) **single-word-cell table-header (`| Name | Schema | Scopes |`, Name=1 слово) = структурный blind-spot LATIN-RUN(≥5) И SHORT(≥2w) ОБА пропускают → добавлен в review-harness LEFTOVER exact-match portable forward (L4-AE object-table-header lesson подтверждён, net расширяется НЕ сужается, 3-й header-класс: object-table L4-AE / 5-col-param / single-word-index L4-AF)**; (2) **NEW header-форма по distinct-source-term: `Property`≠corpus `Element/Field/Parameter`, НЕ в L4-AE EN-lock-списке, 0 shipped precedent → faithful translate `Свойство` = first-occurrence канон (задаёт канон для 307 builtin L4-AG); EN-lock-список авторитетен — переводим то, что НЕ в нём, НЕ конфлируем distinct source-terms ради corpus-frequency**; (3) **auth-предложение cross-file canon из shipped same-subsection objects/ (L4T#1): EN структурно различается (combined+bold vs split) НО RU canon-инвариантные части (запроса/использовать токен) ОБЯЗАНЫ совпадать с shipped — orchestrator REAL-grep shipped per-canon-axis поймал script-deviation ДО build (full_audit_before_action: 10-мин аудит < 3-час итерации; pre-build REAL-grep non-delegable как и post-build)**; (4) **review импортирует builder DISPLAY_NAME = единый source-of-truth consistency-gate (parent-row name ≡ per-file ###-heading name, 391 проверка, детерминирован на duplicate-names) — структурно исключает «имя резолвится двумя путями»**; (5) delegated-build self-report НЕ доверять: orchestrator pre-build audit (3 фикса) + post-build semantic-read (1 whole-class фикс) non-delegable, structural≠semantic 10-й раз (L4N/L4P/L4T/L4W/L4Y/L4-AB/L4-AC/L4-AD/L4-AE/L4-AF; verified-0 ≠ unchecked-0). ИСТОРИЯ L4-AE ниже:** **L4-AE environment-api/settings/ = 7ф (key-concepts.md `* Explanation` + objects/ 6 CRUD: del-object/get-effective-values/get-object/get-objects/post-object/put-object) ЗАКРЫТ → settings/objects/ + key-concepts 100% (остаток settings/ = schemas.md + ~337 settings/schemas/ = ОТДЕЛЬНАЯ серия, не этот батч). ~1924 EN-строк. **АКТИВНЫЙ Settings 2.0 API** (`* Reference`/`* Published <date>` EN-verbatim; key-concepts `* Explanation`/`* Updated on Mar 26, 2026` EN-verbatim; без `* Deprecated`; line-parity EXACT EN==RU). **anchor = same-subsection parent `settings.md` RU (translated 2026-05-14, сильнейший glossary L4T#1/L4Z#1): settings object/settings schema/schema/schemas/scope/scopes/external ID(s)/concurrency control/upsert/endpoint(s) EN-lock; объект/пагинация/оптимистичная блокировка/фактические значения переведены** + ACTIVE-boilerplate L4-AD dashboards-api RU + env-api L4Y/L4Z canon. title/H1×2/`* Reference`/`* Published`/`* Explanation`/`* Updated on` EN-verbatim; endpoint-table rows (`DELETE/GET/POST/PUT`/`ManagedDynatrace for Government`/`Environment and Cluster ActiveGate (default port 9999)`/URL) EN-verbatim; `## Аутентификация`/«Для выполнения запроса необходим access token со scope `X`.»/«О том, как получить и использовать токен, см. [Tokens and authentication](url).» (link-text EN L4Y 188:40)/«Запрос возвращает данные в формате `application/json`.»/«Запрос принимает и возвращает данные в формате `application/json`.» (consumes+produces)/«**Примечание**: Также требуется scope `settings.read`.»/`## Параметры` `\| Параметр \| Тип \| Описание \| Где \| Обязательный \|` (path/query/body/Required/Optional cells EN)/`## Ответ`/`### Коды ответа` `\| Код \| Тип \| Описание \|`/`### Объекты тела ответа`/`### Объекты тела запроса`/`### JSON-модель тела запроса`/`### JSON-модели тела запроса`/`### JSON-модели тела ответа`/`#### Объект \`X\``/`Возможные значения:` colon (L99/L4Y, НЕ pre-L99 «Элемент может принимать»)/ConstraintViolation `-Возможные значения:` leading-dash+colon/«Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.». **object/element-table header `\| Элемент \| Тип \| Описание \|` + 4-col `\| Элемент \| Тип \| Описание \| Обязательный \|` (Required/Optional value-cell EN-verbatim, ТОЛЬКО header переводится — L4-AC/L4-AA).** L101 per-cell grep EN-ячейку (L4X#3 7-й раз): `Success. Response doesn't have a body.`→«Успех. Ответ не содержит тела.» С точкой; bare `Success`→«Успех» БЕЗ точки; `Failed. X.`→«Сбой. X.» С точкой; `No object available for the given objectId`→«Нет объекта для указанного objectId» БЕЗ точки; `Multi-status: …`→«Multi-status: …»; `Client/Server side error.`→«Ошибка на стороне клиента/сервера.». **Error-канон env-api L4Y: «HTTP-код состояния»/«Список нарушений ограничений»/«Сообщение об ошибке» (НЕ config-api «статуса»).** BOM `ï»¿` 3-char strip: `[Dynatrace Documentation](dt-url.net/ky03459)` generic doc-ref link-text EN canon-d; `[here]`→`[здесь]` descriptive inline ПЕРЕВОД (L4Y#4); `[Tokens and authentication]` EN-lock. **key-concepts mojibake: double-enc U+2014 `â` в прозе (`false\`)âno`/`entirelyâit`/`maskedâunless`/`URLâan` ×7) → `:`/запятая/новая фраза faithful-by-meaning (em-dash BAN CLAUDE#0 > byte, L4-AD#4).** `~~modificationInfo~~` strikethrough kept + `DEPRECATED`→`УСТАРЕЛО` faithful source-render (L4Y); inline `(deprecated)` в fields-list EN faithful. **domain-vocabulary headings `### Schemas`/`### Scopes`/`### External IDs` EN-lock** (parent EN-lock'ает термин inline → within-doc+parent consistency; `### Пагинация`/`### Пакетная запись`/`### Оптимистичная блокировка`/`### Свойства типа secret`/`### Управление доступом на основе владельца`/`### Пробная валидация (\`validateOnly\`)`/`### Разреженные наборы полей (параметр \`fields\`)` conceptual = ПЕРЕВОД). source-quirk L93: del-object «Updates the specified settings object. Deletion cannot be undone!» (verb «Updates» на DELETE-доке) зеркалим «Обновляет указанный settings object. Удаление нельзя отменить!». **Build = delegated general-purpose subagent** (anchor-paths + canon-brief + 7 enumerated + ground-truth `grep -c`; self-report «0 деф» НЕ принят). **Критич.ревью (orchestrator mandatory)** `scripts/_review_settings_l4ae.py` (копия `_review_dashboards.py`, base→environment-api, 7 PAIRS, `* Explanation` инвариант, integrated [LATIN-RUN]≥5 + SHORT 2-4w, **+ NEW object-table-header `\| Element \| Type \| Description \|`(+`\| Required \|`) в LEFTOVER exact-match**): build-pass review 0 структурных деф, НО оркестратор РЕАЛЬНЫМ grep'ом shipped-корпуса (НЕ by-rule, L4-AD#2) поймал **3 whole-class деф (structural-green≠semantic 9-й раз)**: (1) object-table header оставлен EN ВСЕ 6 endpoint-ф (38×3-col + 2×4-col) — LATIN-RUN≥5/SHORT-2-4w ОБА пропускают (3-слов header, 1-словные ячейки <5-run = НОВЫЙ net blind-spot); shipped ACTIVE unanimous L4-AD 78×/L4Y 55×/L4-AC 194× `\| Элемент \| Тип \| Описание \|`; (2) `HTTP-код статуса`→`HTTP-код состояния` 14× (env-api L4Y rum 9×/toposmart 19× `состояния`; settings=env-api семья, subagent взял config-api `статуса` = cross-family canon-mismatch); (3) `### Внешние идентификаторы`→`### External IDs` (parent domain-term EN-lock, sibling `### Schemas`/`### Scopes` consistency). Fix WHOLE class grep-audit all 7 (L4-AB#2) `scripts/_fix_settings_l4ae.py` longest-first 4-col ПЕРЕД 3-col (L4-AA#1: 3-col EN = prefix-substring 4-col), 53 замены line-count unchanged → re-review independent **[OK] 0 структурных деф** + whole-class re-grep 0 (0 EN-header / 0 `статуса` / 0 `Внешние идентификаторы`, канон `Элемент` 38ф + `состояния` 14×). LATIN-RUN 6 + SHORT-RUN 6 ВСЕ LEGIT (endpoint-table EN-verbatim). Семантик spot-check 5ф (key-concepts mojibake→colon+link-text+domain-lock; del source-typo «Updates» faithful; post request-body-model+Multi-status-207+twin SettingsObjectResponse; get-objects modificationInfo→УСТАРЕЛО+`[здесь]`+BOM-strip; get-eff EffectiveSettingsValue+origin): faithful, em-dash 0, line-parity EXACT 7/7 [113/152/243/326/434/347/309], fences byte-identical force-sync 0. diff +7 (1719→1726 = **65.01%**, pending 936→929, dynatrace-api 350→343, ingest-from 586 не тронут, Orphan RU 0, source-check 0). **Lesson L4-AE:** (1) **object/element-table header `\| Element \| Type \| Description \|` (3-слов, 1-словные ячейки) = структурный blind-spot LATIN-RUN(≥5) И SHORT(2-4w) ОБА пропускают → добавлен в review-harness LEFTOVER exact-match, portable forward (L4-AC#2 «net расширяется» 3-й раз); канон взят shipped-corpus REAL-grep'ом unanimous, НЕ by-rule (L4-AD#2 подтверждён)**; (2) **cross-family canon-axis: settings=environment-api ⇒ Error «HTTP-код состояния» по env-api L4Y/L4Z anchor, НЕ config-api «статуса» — anchor по СЕМЬЕ файла (env-api), freshest-SAME-family > freshest-ACTIVE-any (L4Y#1/L4S#4 chain уточнён)**; (3) domain-vocabulary heading EN-lock по parent same-subsection если parent EN-lock'ает термин inline (L4T#1 расширен на heading-axis: `### Schemas`/`### Scopes`/`### External IDs` EN ≠ conceptual headings ПЕРЕВОД); (4) parent same-subsection RU (translated) = сильнейший glossary anchor, term-locks прямо оттуда (L4T#1/L4Z#1 подтверждён); (5) delegated-build self-report «0 деф» НЕ доверять, orchestrator REAL-grep shipped-corpus per-canon-axis non-delegable (verified-0≠unchecked-0; structural≠semantic 9-й раз: L4N/L4P/L4T/L4W/L4Y/L4-AB/L4-AC/L4-AD/L4-AE). ИСТОРИЯ L4-AD ниже:** **L4-AD configuration-api/dashboards-api/ = 9ф (parent + dashboards-api-tile-models 2026 + del-dashboard + get-all + get-dashboard + get-sharing-config + post-dashboard + put-dashboard + put-sharing-config) ЗАКРЫТ → dashboards-api/ subsection 100% ЦЕЛИКОМ. ~5843 EN-строк. **АКТИВНЫЙ Classic config API** (`* Reference`/`* Published`, без `* Deprecated`, line-parity EXACT EN==RU). anchor = свежайший same-family L4-AC anomaly-detection-api disk-events RU (boilerplate `## Аутентификация`/`## Параметры`/`## Ответ`/`### Коды ответа`/`### Объекты тела ответа`/`### Объекты тела запроса`/`#### Объект \`X\``/`Возможные значения:` colon-L99/Error/ErrorEnvelope/ConstraintViolation/EntityShortRepresentation/StubList/ConfigurationMetadata/`## Validate payload` EN ALLOWED_EN/`#### Curl` EN/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`/`#### Результат`/«API-токен передаётся в заголовке **Authorization**.»/«Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.») + tile-models json-models structure = L4-AB failure-detection/json-models RU (`## TYPE`-headings EN-verbatim, `Parameters`/`JSON model` tab-labels EN-literals, `#### Объект \`X\``). title/H1×2/`* Reference`/`* Published`/endpoint-rows (`ManagedDynatrace for Government`/`Environment ActiveGate`/URL)/scope-backtick/`[Tokens and authentication]` link-text EN-verbatim. **Twin: Dashboard/DashboardMetadata/Tile/DashboardFilter/DynamicFilters байт-идентичны get/post/put-dashboard → переведены 1× identical RU; genuine source-delta = post/put имеют `\| Required \|` колонку, get НЕ имеет → faithfully зеркалится НЕ выравнивать (L4-AA#2 подтверждён); DashboardSharing/DashboardSharePermissions/DashboardAnonymousAccess twin get-sharing↔put-sharing.** **L101 MIXED per-file: post-dashboard стр 518/659 + put-dashboard 518 `Failed. The input is invalid` БЕЗ точки → `Сбой. Невалидный ввод` БЕЗ точки; put-sharing-config:244 С точкой `Сбой. Невалидный ввод.` + :355 БЕЗ точки (MIXED в ОДНОМ файле — grep EN-ячейку per-cell, L4X#3 6-й раз).** cross-ref `[Dashboards API - Tile JSON modelsï»¿](https://dt-url.net/2wc3spx)` 3-char BOM strip → link-text EN canon-d (L4-AB rule c); inline doc-ref `[Tile JSON models](/managed/.../dashboards-api-tile-models "…")` link-text EN, prose+title-attr RU. parent card-glue `](url "title")[### ` сохранён (Title+Description+title-attr RU, url EN-verbatim); intro «API **Dashboards Classic** позволяет управлять конфигурацией ваших дашбордов.». Related `[Дашборды]` = target RU H1 (`docs/managed-ru/analyze-explore-automate/dashboards-classic.md` `# Дашборды`) L4O/L4L. Domain: dashboard→дашборд, tile→плитка, sharing→совместный доступ, preset→предустановленный, owner→владелец. corrupted em-dash `tileâa` (double-enc U+2014) post-dashboard:750 → `:` (em-dash BAN CLAUDE#0 > byte-fidelity, faithful-by-meaning, единственный не-byte transform). put-dashboard validate-payload EN source-quirk dual `### Response`(no codes table)+`### Authentication` зеркалится L93. EN typos tile-models `Include (\`false')`/`DATA_EXLORER`/`"tileType":"Image"\|"TILE"` в fence byte-identical L93. `User Session Query`/`User session query` tile-type-name EN-lock; AWS/VMware/OpenStack/Synthetic/USQL/Apdex/Markdown EN-lock. **Build = delegated general-purpose subagent** (anchor-paths + canon-brief + 9 enumerated + ground-truth `grep -c`; self-report «0 деф» НЕ принят, structural≠semantic). **Критич.ревью (orchestrator mandatory)** `scripts/_review_dashboards.py` (копия `_review_anomaly_l4ac.py` + 9 PAIRS + integrated [LATIN-RUN]≥5 net + **NEW tighter 2-4-слов no-Cyrillic table-cell scan — L4-AC lesson #2 структурно закреплён в harness, net расширяется не сужается**): **0 структурных деф** (line-parity EXACT 9/9 [37/2026/72/253/794/243/975/1000/443], fences byte-identical force-sync=0, em-dash 0, mojibake 0, leftover-EN 0, EN-invariants OK). LATIN-RUN 9→8 + SHORT-RUN 22 orchestrator-triaged: 8 LATIN LEGIT (4× doc-ref `[Dashboards API - Tile JSON models]` canon-d EN + 4× tileType enum→type-name list EN-lock) + 22 SHORT ВСЕ LEGIT (endpoint-table `ManagedDynatrace for Government`/`Environment ActiveGate` EN-verbatim) + **1 РЕАЛЬНЫЙ деф пойман оркестратором: tile-models:1928 descriptive inline link-text `[User session query](https://dt-url.net/dtusql)` оставлен EN-capitalized — shipped L4Y corpus `environment-api/rum/user-sessions/table.md` ПЕРЕВОДИТ dtusql link-text + L4Y#4 descriptive-prose link-text=ПЕРЕВОД → fix `[запрос пользовательских сессий]` (structural-green≠semantic 8-й раз: L4N/L4P/L4T/L4W/L4Y/L4-AB/L4-AC/L4-AD)** → re-run 0 структ.деф + LATIN-RUN 8 (все LEGIT). Семантик spot-check: L101-mixed PERFECT (grep EN-ячейку per-cell verified), parent card-glue+Related=target-RU-H1 `[Дашборды]`, Dashboard-twin identical RU + genuine-source-delta `\| Required \|` faithful, validate-payload dual-section faithful L93, corrupted-em-dash→colon faithful. diff +9 (1710→1719 = **64.75%**, pending 945→936, dynatrace-api 747→756/359→350, Orphan RU 0, source-check 0). **Lesson L4-AD:** (1) tighter 2-4-слов no-Cyr table-cell scan структурно интегрирован в review-harness (L4-AC#2 закреплён: copy `_review_<prev>` тянет integrated short-scan, net расширяется НЕ сужается; 0 реальных деф но подтвердил endpoint-rows EN-verbatim clean — verified-clean ≠ unchecked); (2) **descriptive inline link-text к external `dt-url.net` = ПЕРЕВОД per shipped corpus precedent (L4Y user-sessions dtusql) + L4Y#4 ≠ doc-API cross-ref `[<API> - JSON models]` EN canon-d — проверять shipped corpus РЕАЛЬНЫМ grep'ом, не только by-rule (две конкурирующие link-text-axis: external-doc-descriptive=ПЕРЕВОД vs API-cross-ref=EN)**; (3) twin genuine-source-delta (post/put `\| Required \|` col vs get без неё) faithfully зеркалится НЕ «выравнивать» (L4-AA#2 подтверждён 2-й раз); (4) corrupted-codepoint em-dash в прозе (`tileâa` double-enc U+2014) → `:` faithful-by-meaning (em-dash BAN CLAUDE#0 приоритетнее byte-fidelity — единственный осознанный не-byte transform, задокументирован); (5) delegated-build + orchestrator-mandatory-critical-review non-delegable (subagent self-report «0 деф» НЕ доверять, structural≠semantic; verified-0 ≠ unchecked-0, L4Z#6 8-й раз). ИСТОРИЯ L4-AC ниже:** **L4-AC configuration-api/anomaly-detection-api/ остаток = 11ф (aws/hosts/vmware ×{parent+get-config+put-config}=9 АКТИВНЫЕ + metric-events/{post-event 731,json-models 688}=2 DEPRECATED) ЗАКРЫТ → anomaly-detection-api/ subsection 100% ЦЕЛИКОМ (L4C process-groups+disk-events 10 + L4D applications/database/services+parent 10 + L4-AC 11; вся подсекция RU). ~6.7K EN-строк. parent ×3 = 23-строчные твины уже-RU `anomaly-detection-api-database.md` (только entity Database services→AWS/Hosts/VMware + prose-specifics + Related-link меняются). **Anchor = same-subsection L4D database/services/applications RU** (get/put-config boilerplate: `## Аутентификация`/`## Параметры`/`## Ответ`/`### Коды ответа`/`### Объекты тела ответа`/`#### Объект \`X\``/`| Элемент | Тип | Описание |`/`Обнаружение включено (\`true\`) или отключено (\`false\`).`/`Метаданные, полезные для отладки`/Error/ErrorEnvelope/ConstraintViolation/`## Validate payload`+`Validated. Переданная конфигурация валидна. Ответ без тела.`) + **json-models = L4-AB failure-detection/json-models RU** (`### TYPE`-headings EN / `Parameters`+`JSON model` tab-labels EN-literals / `#### Объект \`X\`` / `Возможные значения:` двоеточие L99 ×11, `может принимать` 0). **DEPRECATED (metric-events 2ф): KEEP `* Deprecated` bullet EN-verbatim + `* Updated on Apr 26, 2023` EN + проза «Этот API устарел. Используйте [Settings API](…) . Ищите schema **Metric events** (\`builtin:anomaly-detection.metric-events\`).» (link-text `Settings API` EN cross-ref, title-attr RU, `schema`/`Metric events`/backtick-id EN-lock consistent). metric-events родителя НЕТ ни в EN ни в RU — НЕ фабриковать (faithful absence).** title/H1×2 EN-verbatim; endpoint-table rows (GET/PUT/POST + `ManagedDynatrace for Government`/`Environment ActiveGate` + URL) EN-verbatim; image alt `![Anomaly detection config - X - updated]` + caption-строка EN-verbatim (matches shipped L4D database anchor — НЕ переводить); Related-topics link-text EN (`Adjust the sensitivity of anomaly detection for infrastructure`, target H1 EN) + title-attr RU; json-models doc-ref `[Metric events anomaly detection API - JSON models](dt-url.net)` link-text EN canon-d + 3-char BOM `ï»¿` strip; `Required` value-cell EN-verbatim (L4D anchor, только header→`Обязательный`); mojibake `Anomaly detection?AWS`(double-enc en-dash)→`-` как database-anchor рендерит `Anomaly detection-Database services`, `Davis® AI`(Â strip). **L101 MIXED per-file: hosts/put-config `Failed. The input is invalid` БЕЗ точки → `Сбой. Невалидный ввод` БЕЗ точки; aws/vmware/put-config + metric-events/post-event С точкой → С точкой (grep EN-ячейку КАЖДОГО, L4X#3 5-й раз).** EN-typo source-quirk L93 verbatim-by-meaning: vmware get/put `configuraiton`/`cofiguration`/`cofing` → перевод по смыслу; hosts/put-config Example-проза «for database services» (copy-paste err в EN, link→hosts) зеркалим «для сервисов баз данных» link-text EN/title-attr RU; hosts/put-config Curl `-d '{<truncated - see the Request body section below>}'` byte-identical в fence. Domain: `VM CPU usage`→`Загрузка VM CPU` ⇒ `VM CPU ready`→`Готовность VM CPU` (descriptive subject переведён, `VM CPU` acronym EN-lock — consistency внутри одной таблицы). Build = delegated general-purpose subagent (anchor-paths + canon-brief + 11 enumerated + ground-truth `grep -c`); критич.ревью `scripts/_review_anomaly_l4ac.py` (копия `_review_anomaly_l4d.py` + 11 PAIRS + `* Deprecated`/`* Updated on` инварианты + **[LATIN-RUN] net интегрирован in-harness как hard structural-gate, L4-AB#1/L4Y#3 эскалирован: portable в КАЖДЫЙ review с новым vocab-доменом**). **Критич.ревью (orchestrator mandatory):** 0 структурных деф (line-parity EXACT 11/11, fences byte-identical force-sync, em-dash 0, mojibake 0, leftover-EN headers 0, EN-invariants incl `* Deprecated` OK). LATIN-RUN 22 flag → orchestrator triage: 21 LEGIT EN-lock (img alt+caption ×6 = L4D database anchor; Related link-text ×8 EN+title-attr RU; json-models cross-ref ×2 canon-d EN+BOM-strip; type-name identifiers ×1; `Required` value-cell) + **1 РЕАЛЬНЫЙ деф-класс `VM CPU ready` (5 ячеек vmware get+put-config: sibling `VM CPU usage`→`Загрузка VM CPU` переведён, `ready`-ячейки оставлены EN — structural-green≠semantic 7-й раз: L4N/L4P/L4T/L4W/L4Y/L4-AB/L4-AC) → fix `Готовность VM CPU`** → re-run review 0 структ.деф + LATIN-RUN 18 (все LEGIT). Доп. tighter 2-4-слов no-Cyrillic scan = 43 flag ВСЕ LEGIT (endpoint-tables/img alt-caption/`JSON model` tab-labels). Оркестратор-семантик spot-check: L101 period-edge PERFECT (hosts БЕЗ точки vs aws/vmware С точкой grep-verified), deprecated-handling correct (`* Deprecated` EN + проза RU + Settings API link EN + title-attr RU), json-models structure correct (`Возможные значения:` ×11 / `### TYPE`/`Parameters`/`JSON model` EN / `#### Объект`), parent-twin correct, aws/get-config object-cells boilerplate = database anchor verbatim. diff +11 (1699→1710, pending 956→945, dynatrace-api 736→747/370→359, Orphan RU 0, source-check 0). **Lesson L4-AC:** (1) **[LATIN-RUN] net ДОЛЖЕН быть hard structural-gate в КАЖДОМ review-harness с новым vocab-доменом (L4-AB#1/L4Y#3 структурно закреплён: copy `_review_<prev>` ВСЕГДА тянет integrated LATIN-RUN, НЕ optional orchestrator-step)**; (2) **LATIN-RUN ловит ≥5-слов run, НО внутри-табличная inconsistency (sibling `usage`→RU переведён, `ready`-cell EN) = 5-слов flag → орк-triage обязателен; добавить tighter 2-4-слов no-Cyr scan для коротких leftover-EN которые LATIN-RUN(≥5) пропускает (structural≠semantic 7-й раз — net расширяется, не сужается)**; (3) **L4D shipped same-subsection anchor авторитетнее generic by-family для image alt+caption (database RU держит EN-verbatim `Anomaly detection config - X - updated` ⇒ AWS/Hosts/VMware EN-verbatim, L4T#1 на каждую canon-axis подтверждён); `Required` value-cell EN-verbatim из L4D anchor (только header переводится)**; (4) L101 mixed per-file в ОДНОЙ подсекции OK (hosts БЕЗ vs aws/vmware С точкой — substring/grep EN-ячейку per-file, L4X#3 5-й раз); (5) deprecated metric-events родителя нет ни в EN ни в RU — faithful absence НЕ фабриковать (L4Z#4 подтверждён); (6) delegated-build + orchestrator-mandatory-critical-review модель: subagent self-report «0 деф» НЕ доверять (structural≠semantic), orchestrator review-harness + semantic spot-check = non-delegable (verified-0 ≠ unchecked-0, L4Z#6). ИСТОРИЯ L4-AB ниже:** **L4-AB configuration-api/service-api/ остаток = 49ф (service-api.md parent + custom-services-api/ 7 + detection-rules/ 26 [parent + models.md 1756 + 4 rule-type families ×6: full-web-request/full-web-service/opaque-web-request/opaque-web-service] + failure-detection/ 15 [parent + json-models.md 1318 + detection-rules ×7 + parameter-set ×6]) ЗАКРЫТ → **service-api/ subsection 100% ЦЕЛИКОМ** (L4-AA 14 + L4-AB 49 = 63ф). ~15.2K EN-строк. **АКТИВНЫЙ API** L89/L90 (без `* Deprecated`, `* Reference`/`* Published <date>`/title/H1×2 EN-verbatim, line-parity EXACT EN==RU). anchor = L4-AA service-api R-table reused verbatim (~90% shared: ВСЕ `#### The X object`-headings, *ComparisonInfo/*Dto, Condition/Placeholder/PropagationSource/UniversalTag/TagInfo/Error*/ErrorEnvelope/ConstraintViolation/StubList/EntityShortRep/ConfigMeta, L99 phrases, ## Authentication/Parameters/Response headings, response-code cells, table headers, k8s/config L4M/L4U). **4 rule-type families ~85% twin** (84 diff-строк после rule-type-token нормализации) → twin-splice IMPLICIT через общую R-table (identical EN→identical RU, L4Z/L4W метод в 2.3× масштабе 49ф/4-family). **L101 MIXED period в ОДНОМ subsection**: `Failed. The input is invalid` БЕЗ точки (5×) И С точкой (39×) → substring `("Failed. The input is invalid","Сбой. Невалидный ввод")` сохраняет точку источника per-cell АВТО (L4X#3 4-й раз — грепать EN-ячейку, mixed OK). json-models structure L3G (`### TYPE`-headings/`Parameters`/`JSON model` tab-labels EN) + `Возможные значения:` двоеточие L4O/L99 (НЕ «Элемент может принимать»). **Link-text 3 правила**: (a) descriptive nav-bullet (service-api.md/detection-rules.md `[Полные веб-запросы]`/`[Создание вычисляемой метрики сервиса]`) ПЕРЕВЕДЕНО L4Y#4; (b) doc-ref cross-ref `[Service detection API - JSON models]`/`[Failure detection API - JSON models]`(`dt-url.net`) EN-verbatim (target не RU, canon-d/L4Y#5, surrounding-prose переведена, 3-char BOM `ï»¿` strip L4M); (c) `[запрос на изменение порядка]` reorder-embedding link-text ПЕРЕВЁДЕН L4Y#4, title-attr RU. Anomalous endpoint `## PUT a custom service rule` H2 (custom-services-api/put-rule.md) EN-verbatim (L99/L4T endpoint-name-as-heading; corpus 0 `## VERB`-headings — source-quirk зеркалить L93). Splice `scripts/_build_serviceapi_ab.py` (L4-AA R reused + **86 new entries**: TIER-0d FD-embedding-intros/8 service-detection-body-cells/card-descr/attribute-cell-prefixes/12 json-models-condition-forms + 44 nav-bullet link-text bracket-anchored) + критич.ревью `scripts/_review_serviceapi_ab.py` (копия `_review_serviceapi.py` + **NEW [LATIN-RUN] defect-класс ПОРТИРОВАН из `scripts/_latinscan_ab.py`** — generic stripped-Latin-run net hard-gated В harness: L4Y#3 структурно закреплён). **Критический ревью (orchestrator mandatory)**: build-pass-1 review 0 структурных деф НО независимый orchestrator generic-LATIN-RUN net поймал **СИСТЕМНЫЙ leftover-EN класс на 18ф** (ВСЕ 4 rule-type families + failure-detection + custom-services + models.md + service-api.md 40+ nav-link-text): inherited L4-AA SUSPECT покрывал только request-attributes/naming vocab, detection-rules cell-vocab НЕ покрыт (**structural-green≠semantic 6-й раз**: L4N/L4P/L4T/L4W/L4Y/L4-AB). Fix WHOLE class (grep-audit все family/verb twins НЕ только flagged): 86 R-entries + LATIN-RUN портирован в review. 3 build/review-iter этого раунда (36→11→1→0 деф). Финал independently re-verified: review [OK] 0 деф (incl LATIN-RUN=0), `_latinscan_ab.py` 94 flags ВСЕ EN-lock (orchestrator triaged: doc-ref link-text 42 + object/enum/type-names 51 + endpoint-H2 1, 0 leftover-prose; `Service detection API - JSON models` подтверждён genuine markdown cross-ref `[X](dt-url.net)` с переведённой surrounding-prose, corpus-precedent L4-AA `[Service metrics API - JSON models]` идентичен), line-parity EXACT 49/49, em-dash global 0 (63ф), Orphan RU 0, diff +49 (1650→1699, pending 1005→956, dynatrace-api 687→736/419→370). **Lesson L4-AB:** (1) **reused-curated-SUSPECT под NEW vocab-domain под-покрывает → generic LATIN-RUN net ОБЯЗАН быть В review-harness, НЕ optional orchestrator-step (L4Y#3 эскалирован: портировать [LATIN-RUN] в `_review_*`, structural-gate каждый batch с новым доменом)**; (2) systematic leftover-class охватывает ВСЕ family/verb twins не только flagged-file → fix WHOLE class через grep-audit; (3) doc-ref cross-ref link-text `[<API> - JSON models]` EN-verbatim где target не RU, surrounding-prose переведена (canon-d/L4Y#5 подтверждён); (4) descriptive nav-bullet link-text ПЕРЕВОД ≠ doc-ref/Related cross-ref EN — 2 правила L4Y#4; (5) anomalous endpoint `## VERB` H2 = EN-verbatim L99/L4T (corpus 0 `## VERB` — source-quirk зеркалить L93); (6) L101 mixed-period в ОДНОМ subsection OK — substring сохраняет точку источника per-cell (L4X#3 4-й раз); (7) twin-splice масштаб 49ф/4-family ~85% (L4Z в 2.3×, implicit R-table). ИСТОРИЯ L4-AA ниже:** **L4-AA configuration-api/service-api/ partial = 14ф: request-attributes-api/ (6) + request-naming-api/ (8, вкл. json-models 936 + use-case create-a-new-rule) ЗАКРЫТЫ 100% (остаток service-api/ = detection-rules 26 + failure-detection 15 + custom-services-api 7 = 48, отд. батчи). АКТИВНЫЙ API L89/L90 (`* Reference`/`* Published` EN-verbatim, без `* Deprecated`). anchor = свежайший config-api same-family RU = L4X calculated-metrics/service-metrics (shared Condition/ComparisonInfo/Placeholder/PropagationSource/UniversalTag-long/TagInfo-short/ConfigMeta/EntityShortRep/StubList/Error*/ConstraintViolation + ВСЕ *ComparisonInfo/*Dto байт-идентичны EN → (en,ru) L4X verbatim) + k8s/config L4M/L4U. Strong post↔put twins (RA 95%/RN 96%) — twin IMPLICIT через общую R-table (детерминированный exact-string replace, genuine source-delta ValueCondition.operator зеркалится faithfully). json-models = L4X ComparisonInfo-variations twin: L3G structure (Variations-intro/`[JSON models]`-EN/`### TYPE`-headings EN/`Parameters`/`JSON model` tab-labels EN) НО `Возможные значения:` двоеточие+EN-locks=L4X/L99 (НЕ L3G «Элемент может принимать», 134× env-leak 0). title/H1×2 EN-verbatim (вкл. use-case H1). **L101: 400 «Сбой. Невалидный ввод.» С точкой ВО ВСЕХ 14 (grep-verified единств. форма С точкой; substring сохраняет; ПРОТИВОПОЛОЖНО L4X calculated-metrics БЕЗ точки идентичная структура — грепать EN-ячейку КАЖДОГО L4X#3)**; bare GET-200 `\| Success \|`→`\| Успех \|` (L4W/L4X); validate-204 «Validated.»-prefix EN-cell L4I; `## Validate payload`/`#### Curl` EN ALLOWED_EN. Related-topics link-текст = target RU H1 дословно L4O/L4L (`[Атрибуты запросов]`/`[Настройка именования запросов]`/`[Определение пользовательских сервисов]`); post-new-rule topic link-text `[Request naming API - Create a new rule]`/`[**POST a new request naming rule**]` = EN endpoint-name L4T, title-attr переведён. **create-a-new-request-naming-rule = USE-CASE narrative** (REST client/Dynatrace API Explorer tab-labels переведены, 7 steps + image alt/caption переведены, «Try it out» UI-button EN consistent, dt-cdn URLs verbatim, fence force-synced). mojibake codepoint-normalize L4X + 3-char BOM strip L4M (`[Service metrics API - JSON modelsï»¿]`→link-text EN). Source-quirk L93: «mehtod»/«JAVA_HTTPURLCONNETION»/«Prune Whitespaces»/`\n\n` literal/`.This`→`.Эта` зеркалим. Splice `scripts/_build_serviceapi.py` (**TIER-0 embedding-anchor: full sentence embedding link+title-attr с ORIGINAL-EN nested title-attr ПЕРВЫМ, до standalone (A) — L4T longest-first**) + критич.ревью `scripts/_review_serviceapi.py` (копия `_review_servicemetrics.py` + LEFTOVER excl. type-headings/tab-labels). **3 build-iter: iter1 17деф (4 self-em-dash position/argumentIndex CLAUDE#0 + 13 SUSPECT-EN = L4T-ordering use-case + missing L4X TagInfo-short); iter2 1деф (image-alt `![X]` ≠ caption `X\n` anchor); iter3 +3 image-alt → 0 структурных.** Оркестратор-семантик spot-check 8ф = **0 ДОП.деф (structural-green И semantic-green)**. em-dash global 0, line-parity EXACT 14/14, fence byte-identical. diff +14 (1636→1650, pending 1040→1005? нет: 1019→1005, dynatrace-api 673→687/433→419). **Lesson L4-AA:** (1) **L4T ordering в COMMON: full sentence EMBEDDING link+title-attr ОБЯЗАН ПЕРЕД standalone-фрагментом того же title-attr (longest-first) иначе generic pre-конвертирует nested anchor → no-match leftover-EN (use-case 13 SUSPECT) — TIER-0 embedding-block первым**; (2) post↔put twin IMPLICIT общей R-table (нет explicit COMMON); genuine source-delta faithfully зеркалится НЕ «выравнивать»; (3) image alt `![X]` = ОТДЕЛЬНЫЙ anchor от caption `X\n` (нужны ОБА; UI-button-name в alt EN consistent); (4) L101 период ПО EN-ячейке КАЖДОГО subsection (service-api С точкой vs L4X calc-metrics БЕЗ — L4X#3 3-й раз); (5) json-models structure от L3G-прецедента, canon-elements от same-family-newest L4X (L4X#4); (6) self-em-dash из вольного перевода — review CLAUDE#0 держит. ИСТОРИЯ L4Z ниже:** **L4Z environment-api/topology-and-smartscape/ = 21ф (applications-api 4 + custom-device-api 2 + hosts-api parent+4 + process-groups-api parent+3 + processes-api 2 + services-api 4) ЗАКРЫТ → topology-and-smartscape/ subsection 100% (полный остаток, ground-truth `_pending.txt`). ~19.4K EN-строк. **DEPRECATED API** (`* Deprecated` bullet + «This API is deprecated. Use [Monitored entities API] instead.»). Продолжение env-api L4-era после L4Y. **Anchor = СВЕЖАЙШИЙ same-subsection parent `topology-and-smartscape.md` RU (уже переведён, сильнейший per L4T#1)** + L4Y env-api L99 canon + shared Error/ErrorEnvelope/ConstraintViolation вербатим из L4Y rum RU (та же env-api семья 0-деф). **Deprecated-handling: KEEP `* Deprecated` bullet EN-verbatim (НЕ дропать — ОТЛИЧИЕ от L3T/L3U v1-banner-drop; same-subsection parent RU держит bullet ⇒ anchor=same-subsection-parent приоритетнее by-family v1-правила, L4T#1 расширен на КАЖДУЮ canon-axis)** + проза «Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.» (link-text EN, title-attr переведён, EXACT из parent RU). get-baseline applications/services: источник БЕЗ deprecated-prose (только bullet) → banner COMMON не матчит, bullet EN, прозу НЕ фабриковать (faithful: отсутствие зеркалится отсутствием). Канон L99/L4Y: title/H1×2 EN-verbatim (API-names «Applications API - GET all apps»/«Hosts API»); `* Reference`/`* Updated on Mar 22, 2023` EN-verbatim; `The element can hold these values`→`Возможные значения:` с двоеточием; env-api domain-проза L4Y («Запрос возвращает/принимает данные в формате `application/json`.»/«## Аутентификация»/«access token со scope `DataExport`»/«[Tokens and authentication]» EN/«## Заголовки ответа»/«### Объекты тела запроса»/«Ошибка на стороне клиента./сервера.»); UpdateEntity body + «Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.»; Example reports-api L4I (`#### Curl` EN/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`, «API-токен передаётся в заголовке **Authorization**.»/«Результат усечён до N записей.»). **Twin-splice L4W в масштабе ~19.4K строк:** get-all↔get-a-X byte-identical object-element STRINGS (ProcessGroupInstance/Host/Service/Application/AgentVersion/MonitoringState/TechnologyInfo/TagInfo/ProcessGroupInstanceModule/EntityShortRepresentation) → COMMON 1× offset-независимо; 4× post-tags (UpdateEntity)/get-baseline applications↔services twins. Reuse `_build_rumenv.py` COMMON (0-деф L4Y). L101 substring сохраняет точку источника (204 «Успех. Параметры X обновлены.» С точкой; 400 «Сбой. Невалидный ввод.» С точкой; bare `Success`→`Успех»; грепать EN-ячейку КАЖДОГО L4X#3). Related-topics link-текст = target RU H1 дословно (observe/hosts H1 `# Hosts` EN → link-text EN, observe/process-groups `# Process groups` EN); endpoint/API-name link-text EN (`[Monitored entities API]`/`[Custom tags API]`/`[Timeseries API v1 - PUT a custom metric]` corpus-dominant, ячейка-проза переведена); descriptive-prose link-text переведён (`[приложений]`/`[процессов]` L4Y#4). Domain: process→процесс, process group→группа процессов, host→хост, service→сервис, application→приложение, entity→сущность, baseline→базовая линия, pagination→постраничная разбивка, bitness→разрядность, monitored→отслеживаемый; Smartscape/Davis/OneAgent/PaaS/AWS/Azure/Cloud Foundry BOSH/Google Compute Engine/IBM CICS Transaction Gateway/`stemcell` EN-lock; `**Hosts**`/`**Topology and Smartscape**`/`**series**`/`**custom device**`/`meIdentifier`/enum-backtick/`**field**` EN-lock; `Endpoint'ы`/`OneAgent'ов`/`Host Unit'ы` apostrophe-plural (env-api corpus L4Y); parent card-glue `](url "title")[### ` сохранён. Source-quirk L93 verbatim-by-meaning: process-groups/post-tags труункир. `…application/json` без «payload.» (newline-anchored COMMON после longest)/process-groups-api.md «Assign…to your **hosts**.» (говорит hosts)→зеркалим/del-tags Curl `-X POST` byte-identical в fence/report-custom-device U+00E2 broken-em-dash `retrospectivelyâ`→normalize→`:` (em-dash 0)/3-byte BOM в link-text strip→link-text EN. Splice `scripts/_build_toposmart.py` (reuse `_build_rumenv.py` COMMON) + критич.ревью `scripts/_review_toposmart.py` (копия `_review_rumenv.py` + ENLOCK +verified product-names): structural+force-sync+L101+SUSPECT+LATIN-RUN. **1 РЕАЛЬНЫЙ деф пойман-фикс: L4T generic⊂specific collision report-custom-device (per-file standalone-prose `The metric you're reporting must already exist…` = substring внутри `series` table-cell → per-file runs-before-COMMON перехватил → EN/RU гибрид) → newline-anchor per-file (`\n…\n`) → COMMON `series` cell чисто → 0 деф.** LATIN-RUN false-positives verified (product-names + API/target-H1 link-text → ENLOCK L4S#3). **Оркестратор-семантик spot-check 6ф (applications get-all banner+pagination+headers+Example, hosts-api parent card-glue+Related=target-H1-EN, processes get-all↔get-a-process TWIN byte-identical + per-file path-param distinct, report-custom-device FIXED clean+mojibake→colon, services get-baseline NO-banner handled): 0 ДОПОЛНИТЕЛЬНЫХ деф — structural-green И semantic-green (1-й раз в L4-цепочке 0 доп.деф у оркестратора: subagent L4T-catch+fix во время build полный; spot-check ОБЯЗАТЕЛЕН — verified-0 ≠ unchecked).** em-dash 0, code-fence byte-identical, line-parity EXACT 21/21. diff +21 (1615→1636, pending 1040→1019, dynatrace-api 652→673/454→433). **Lesson L4Z:** (1) **deprecated-banner = ПО same-subsection parent RU НЕ by-family v1-drop (L3T/L3U дропали bullet, parent topology-and-smartscape.md держит → anchor=same-subsection-parent приоритетнее by-family, L4T#1 расширен: КАЖДАЯ canon-axis от свежайшего same-subsection)**; (2) **twin-splice масштабируется до ~19.4K/21ф одним батчем** (object-element STRINGS byte-identical get-all↔get-a-X → COMMON 1× offset-независимо, L4W в 2.5× масштабе, L42 «big files»=splice в выделенной сессии НЕ дробление); (3) **per-file standalone-prose = substring длинной COMMON cell ⇒ newline-anchor (`\n…\n`)** иначе per-file (runs-before-COMMON) перехватывает → EN/RU гибрид (L4T в per-file-vs-COMMON разрезе); (4) get-baseline БЕЗ deprecated-prose (только bullet) — НЕ фабриковать (faithful: отсутствие зеркалится отсутствием); (5) source-quirk L93 verbatim-by-meaning (труункир. payload/«hosts»-в-process-groups/`-X POST`-в-delete) НЕ «чинить»; (6) оркестратор-spot-check 0-доп-деф ВОЗМОЖЕН если subagent ловит L4T-класс в build, но spot-check ОБЯЗАТЕЛЕН (structural≠semantic остаётся, цель verified-0 ≠ unchecked-0). ИСТОРИЯ L4Y ниже:** **L4Y environment-api/rum/ = 24ф (geographic-regions parent+5 + real-user-monitoring-javascript-code parent+7 + rum-cookie-names + rum-manual-insertion-tags parent+4 + user-sessions parent+3) ЗАКРЫТ → rum/ subsection 100%. ПЕРВЫЙ L4-era env-api batch. АКТИВНЫЙ API L89/L90 (`* Reference`/`* Updated on May 02, 2022`/`* Published` EN-verbatim, без `* Deprecated`). Anchor-решение (L103 + L4S#4 + L4T#1 распространены на env-api): env-api корпус pre-L99 НЕ-консистентен (events-v2 L3M translated-title/«Элемент может принимать»; SLO-classic L3V `* Справочник`/`* Обновлено`) → anchor = СВЕЖАЙШИЙ L99, НЕ старый pre-L99 env-api родственник; env-api domain-проза-precedent (events-v2 RU) reused ТОЛЬКО где не конфликт с L99; корпус мигрирует к L99, новые batches = newest canon. Канон L99: title/H1×2/`* Reference`/`* Updated on`/`* Published` EN-verbatim (отличие от ВСЕГО прежнего env-api корпуса — документировано). shared Error/ErrorEnvelope/ConstraintViolation вербатим = L4S/events-v2 RU («HTTP-код состояния»/«Список нарушений ограничений»/«Сообщение об ошибке», ConstraintViolation `-Возможные значения:` leading-dash+двоеточие, bare `-`, ErrorEnvelope `\| - \|`). env-api domain-проза (events-v2 RU, не конфликт L99): «Запрос возвращает данные в формате `application/json`./`text/plain`.»/«## Аутентификация»/«Для выполнения запроса необходим access token со scope `X`.»/«О том, как получить и использовать токен, см. [Tokens and authentication](url).» (link-text EN corpus 188:40 L87)/«## Параметры» header `\| Параметр \| Тип \| Описание \| Где \| Обязательный \|` cells path/query/Required/Optional EN/«## Ответ»/«### Коды ответа» `\| Код \| Тип \| Описание \|`/«Ошибка на стороне клиента./сервера.»/«### Объекты тела ответа»/«### JSON-модели тела ответа»; `#### The \`X\` object`→`#### Объект \`X\``. `The element can hold these values`→`Возможные значения:` с двоеточием (НЕ pre-L99 «Элемент может принимать»), env-leak 0. Example reports-api L4I (`## Пример`/`#### Curl` EN/`#### URL запроса`/`#### Тело ответа`/`#### Код ответа`, «API-токен передаётся в заголовке **Authorization**.»/«Результат усечён до N записей.»). L101 substring-replace сохраняет точку источника авто (199 С точкой, 200 «Успех. Ответ содержит…» С точкой, 400 «Сбой. Запрос отсутствует.», bare `Success`→`Успех` БЕЗ точки). Related-topics link-текст = target RU H1 дословно (L4O/L4L: «Мониторинг реальных пользователей»/«Определение IP-адресов, геолокаций и user agent'ов»/«Пользовательские запросы, сегментация и агрегация данных сессий»); inline/cross-ref link-text corpus-dominance EN-lock (`[Tokens and authentication]` 188:40, snippet-format-names `[JavaScript tag]`/`[OneAgent JavaScript tag(/with SRI)]`/`[inline code]`/`[code snippet]` 7/5/5/5/4, `[RUM manual insertion tags API]`/`[Real User Monitoring JavaScript API]` = target-parent-H1-EN per L99, endpoint-name `[GET the list of manually injected applications]`/`[GET regions of the country]` EN ячейка-проза переведена, USQL/`User Session(s) Query Language` EN corpus 165:0); descriptive-prose-bullet link-text ПЕРЕВЕДЁН (style-guide §Links ≠ target-H1-cross-ref: `[безагентный мониторинг]` corpus 2:1/`[Ручное внедрение для страниц приложения с автоматической инжекцией]`). Domain: user session→пользовательская сессия, user action→пользовательское действие, bounce→отказ, rage click/tap→rage-клик/тап; Synthetic/Session Replay/OpenKit/Apdex/RUM/JavaScript/USQL/CLS/FID/LCP/«Total blocking time» EN-lock; `~~totalBlockingTime~~`+`DEPRECATED`→`УСТАРЕЛО` faithful source-render (FID/totalBlockingTime в источнике → НЕ editorialize по CLAUDE FID→INP: перевод чужого источника ≠ наш authored). BOM `ï»¿` 3-char strip inline-link, URL `dt-url.net` verbatim; source-quirk L93 «ManagedDynatrace for Government»/double-space/`GdaÅsk`-mojibake-в-fence byte-verbatim; U+2014 `\xe2\x80\x94` в прозе user-sessions/tree → RU с двоеточием. Splice `scripts/_build_rumenv.py` + критич.ревью `scripts/_review_rumenv.py` (по `_review_servicemetrics.py` + НОВЫЙ generic LATIN-RUN scanner): structural+force-sync+L101 0 деф; SUSPECT+LATIN-RUN поймали 4 РЕАЛЬНЫХ из 15 (11 false-positive=link-text-EN-per-canon): async/sync entity-cell EN-leak (byte-identical в 3ф, COMMON-coverage miss → move→COMMON) + parent:15/16 descriptive-bullet link-text перевод → re-run **[OK] 0 деф** (ENLOCK refined L4S#3). Семантик spot-check 6ф (user-session-structure 67-field+sub-obj+deprecated+WebVitals, table USQL+Example+JSON, get-countries shared-obj byte-exact, geographic parent card+Related, get-javascript-tag, oneagent-js-sri) — 0 деф, faithful, em-dash 0, line-parity EXACT 24/24. **Lesson L4Y:** (1) ПЕРВЫЙ L4-era env-api: pre-L99 корпус НЕ-консистентен → anchor freshest L99 (L4S#4/L4T#1 chain с config-api на env-api) + env-api domain-проза reused где не конфликт; (2) delegation-brief omission 24→23 (get-javascript-tag выпал, subagent поймал «count≠enumerated») → сверять file-count vs enumerated + `grep -c _pending.txt` ground-truth ПЕРЕД delegation; (3) generic LATIN-RUN scanner поймал entity-cell EN-leak что byte-identical-scan ПРОПУСТИЛ (BOM-strip→EN≠RU) — generic stripped-Latin-run net ОБЯЗАТЕЛЕН > curated SUSPECT (structural≠semantic 5-й раз); (4) descriptive-prose-bullet link-text=TRANSLATE (style-guide §Links+corpus) ≠ Related-topics/cross-ref link-text=target-RU-H1 (L4O/L4L) — два правила; (5) link-text=target-parent-H1 ⇒ EN-verbatim (H1 EN per L99), review ENLOCK включает verified target-H1-EN+format-names+USQL-name (L4S#3); (6) faithful source-render: документированные-в-источнике FID/totalBlockingTime переводим как есть, НЕ editorialize. ИСТОРИЯ L4X ниже:** **L4X configuration-api/calculated-metrics/service-metrics/ = 7ф (parent + del/get-all/get-calculated-metric/json-models 932 + post 767 + put 798) ЗАКРЫТ → calculated-metrics/ subsection 100% (L4O 19 + L4X 7 = 26ф; L4O-deferred L42 закрыт). АКТИВНЫЙ API L89/L90 (`* Reference`/`* Published` EN-verbatim, без `* Deprecated`, rum-metrics RU twin подтверждает). anchor = SAME-subsection L4O calculated-metrics RU (service-строки уже в top-parent: «вычисляемая метрика сервиса»/«метрик сервиса») + k8s/config shared (L4M/L4U); json-models СТРУКТУРА (Variations-intro / «Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models]» / «Список фактических объектов см. в описании поля **type**») = conditional-naming L3G паттерн (единств. json-models прецедент, L4O не имел), НО headers + `Возможные значения:` + EN-locks = L4O/L99 (НЕ L3G «Элемент может принимать»). `Parameters`/`JSON model` tab-labels EN (L3G). title/H1×2/`* Reference`/`* Published` EN; `## Validate payload`/`#### Curl` EN ALLOWED_EN, внутри-секции переведены; validate-204 «Validated. Переданная конфигурация валидна. Ответ без тела.» (EN-cell «Validated.» L4I); **400 «Сбой. Невалидный ввод» БЕЗ точки (L101: EN «Failed. The input is invalid» БЕЗ точки — substring-replace сохраняет авто, ≠ L4W rum/web-app С точкой; грепать EN-ячейку)**; bare `| Success |`→`| Успех |` (L4W canon explicit guard); shared StubList/EntityShortRepresentation/Error/ErrorEnvelope/ConstraintViolation/ConfigurationMetadata вербатим L4O/L4M/L4U. Example канон reports-api L4I: `## Пример`/`#### URL запроса`/`#### Тело запроса`/`#### Тело ответа`/`#### Код ответа`, `#### Curl` EN, «API-токен передаётся в заголовке **Authorization**.»/«Результат усечён до N записей.»; `[POST request example]` link-text EN (L4T). Domain L4O corpus-dom: «calculated service metric»→«вычисляемая метрика сервиса», «service metric(s)»→«метрика/метрик сервиса» (genitive сервиса sing., L4O top-parent shipped); object/enum/`**field**`/`### BOOLEAN`-type-headings/`XComparisonInfo` EN-lock. Related-topics link-текст = target RU H1 дословно («Вычисляемые метрики для сервисов»/«Многомерный анализ» L4O/L4L), title-attr переведён. Source-quirk L93: `api-path`-артефакт EN verbatim, del-204 EN «the update was successful» (в delete-доке) рендерим faithfully «обновление прошло успешно», `.This`→`.Эта` no-space зеркалим, escaped `ESB\_INPUT\_NODE\_TYPE` markdown-escape сохранён. mojibake `â\x80\x{93,98,99}` (–/'/' double-encoded в UniversalTag/TagInfo «Itâs»/«colon â:â»/«not set â those») нормализован codepoint-точно в build() ПЕРЕД заменами (L4W); BOM `ï»¿` strip L4M. Splice `_build_servicemetrics.py`, критич.ревью `_review_servicemetrics.py` (force-sync fence + line/heading/fence/table parity EXACT + em-dash + mojibake/BOM + SUSPECT + no-old-env-canon + colon-guard + EN-инварианты). **Lesson L4X:** (1) splice-builder fragile-char (mojibake/BOM) keys ДОЛЖНЫ строиться из codepoints `chr(0xE2)+chr(0x80)+chr(0xNN)` — литералы коллапсируют при Write/Edit (typed `â\x80\x99` → single `â`), L4W `txt.replace("â","'")` оставлял бы C1-хвост `\x80\x99`; (2) markdown-escaped enum в прозе `'ESB\_INPUT\_NODE\_TYPE'` (НЕ `'ESB_INPUT_NODE_TYPE'`) — R-key ДОЛЖЕН включать `\_` (Python `\\_`), SUSPECT поймал leftover-EN (structural-green≠semantic 4-й раз); (3) L101 период РЕШАЕТСЯ ПО EN-ячейке КАЖДОГО subsection — calculated-metrics/service «Failed. The input is invalid» БЕЗ точки vs rum/web-app L4W С точкой при идентичной структуре (грепать, НЕ копировать соседний batch); (4) json-models structure = L3G паттерн но headers/element-can-hold/EN-lock = L4O/L99 (двойной anchor: structural-prose от json-models-прецедента, canon-elements от same-subsection) — 1 build-iter + 1 review-iter (escaped-enum fix) → 0 деф structural+semantic; (5) calculated-metrics/ subsection ЗАКРЫТА полностью (L4O+L4X), L4O-deferred L42 service-metrics закрыт splice'ом в выделенной сессии как и L4W. ИСТОРИЯ L4W ниже:** **L4W configuration-api/rum/web-application-configuration-api/ DEFER-completion — default-application/2 (get/put-configuration 1388/1589) + web-application/5 (del 44 / get-all 126 / get 1392 / post 1621 / put 1623) = 7ф ЗАКРЫТ → web-application-configuration-api/ subsection 100% (L4V 11 + L4W 7 = 18ф). АКТИВНЫЙ API L89/L90 (`* Reference`/`* Published Sep 03, 2019`/post `* Updated on Aug 18, 2025`, без `* Deprecated`). Splice-twin L85/L86: `WebApplicationConfig` гигант + ~40 sub-объектов + JSON-модель (стр ~47-1392) БАЙТ-ИДЕНТИЧЕН get-web-application↔default/get-configuration (GET-twins) и post↔put-web-application↔default/put-configuration (POST/PUT-twins) → переведён ОДИН раз в COMMON (~200 field-desc), splice в 5 крупных → 7783 EN-строк закрыты при near-zero marginal cost. anchor = СВЕЖАЙШИЙ same-subsection twin = L4V web-application-configuration-api RU (error-rules/key-user-actions/parent) + L4U mobile-custom-app shared-object canon (L4T lesson #1). L103 case b: env-api/rum web-application twin'а нет. Канон L99: title/H1×2/`* Reference`/`* Published`/`* Updated on` EN-verbatim; `The element can hold these values`→`Возможные значения:` с двоеточием (env-leak 0); `## Validate payload`/`#### Curl` EN ALLOWED_EN, внутри-секции переведены; validate-204 «Validated. Переданная конфигурация валидна. Ответ без тела.» (EN-cell «Validated.» L4I); 400 «Сбой. Невалидный ввод.» С точкой (L101 substring, EN с точкой); **bare GET-200 `| Success |`→`| Успех |` (L4V canon error-rules/key-user-actions/data-privacy)**; shared Error/ErrorEnvelope/ConstraintViolation/EntityShortRepresentation/StubList/ConfigurationMetadata вербатим L4U/L4V/L4M. Domain corpus-dom: «web application»→«веб-приложение» (73+44×), «conversion goal»→«цель конверсии», «user action»→«пользовательское действие» (L4U 619×), «user session»→«пользовательская сессия», «Real user monitoring settings.»→«Настройки мониторинга реальных пользователей.», «X enabled/disabled.»→«X включён/отключён.» (gender-agree), «placeholder»→«плейсхолдер», «IP address»→«IP-адрес», «regular expression»→«регулярное выражение» (L4U); Session Replay/Apdex/Davis AI/CDN/CORS/RUM/JavaScript/AWS Lambda/W3C/SameSite EN-lock, `**field**`/enum-backtick EN-lock (L4S SUSPECT-exclusion); Related-topics link-текст = target RU H1 дословно («Удаление веб-приложения» L4O/L4L). Source-quirk L93 verbatim-by-meaning: «Analize» (typo), «noting specified» (typo), «MATCHES_REGULAR_ERPRESSION» (typo). Splice `_build_webappcfg.py` (CRLF→LF L4M + BOM-strip + **mojibake-apostrophe `â\x80\x99` normalize→`'`**); критич.ревью `_review_webappcfg.py` (structural+force-sync+L101+SUSPECT+bare-200-guard). **Lesson L4W:** (1) mojibake-apostrophe `â\x80\x99` (UTF-8-as-Latin1 для ’) в EN-ячейках applicationâ's/serverâ's — splice EN-string ДОЛЖЕН либо точные байты, либо нормализовать в build() ПЕРЕД заменами (выбрано: `txt.replace("â","'")`, robust; критревью поймал MOJIBAKE+LEFTOVER-EN); (2) bare single-word `| Success |`→`| Успех |` = L4V canon, ОДНО слово ⇒ SUSPECT(≥3-run)/leftover-EN MISS ⇒ нужен explicit per-cell review-guard (L4N/L4T «structural-green≠semantic» подтверждён 3-й раз: semantic spot-check поймал, structural 0 деф); (3) self-added em-dash в «Рекомендуемое значение... — 3» (EN «is 3» без тире) — критревью EM-DASH-check поймал (CLAUDE#0) → «равно 3»; (4) 3-word EN-run «same site cookie» в RU-ячейке → SUSPECT поймал → рефраз «Атрибут cookie SameSite» (SameSite EN-lock standard-term); (5) splice одного гигантского shared-объекта 1× → все 5 крупных twin-файлов готовы — L42 «big files separate session» решается splice'ом, не дроблением; 1 build-iter + 2 review-iter (мojibake/Success/em-dash/sameSite пойманы-фикс) → итог 0 деф structural+semantic.**)
Source corpus: 2655 EN files in `docs/managed/`
Target corpus: 1756 RU files in `docs/managed-ru/` (после L4-AF; **Orphan RU 0**, корпус консистентен)
Translated: **1756 файлов** (EN AND RU), **66.14%**
Remaining: **899 файлов**

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
