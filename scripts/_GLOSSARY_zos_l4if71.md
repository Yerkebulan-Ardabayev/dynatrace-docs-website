# Глоссарий L4-IF.71 — dynatrace-oneagent (z/OS + CLI + diagnostics)

Заземлено ДОСЛОВНО на отгруженных соседях:
`zos/operation/zos-code-module-messages/ims-messages.md`, `.../zos-java-messages.md`
(message-файлы), `zos/installation/install-zremote.md`, `zos/installation.md`,
`zos/monitoring/monitor-zos-logs.md`, `zos.md` (install/monitoring проза).
Когда сомневаешься — `grep` по `docs/managed-ru/.../zos/` (норма соседа важнее
буквального перевода).

## Метаданные страницы (фиксировано корпусом)

- `* N-min read` → `* Чтение: N мин`
- `* Published <Mon DD, YYYY>` → `* Опубликовано <DD месяца YYYY> г.` (месяц родительный: января/февраля/марта/апреля/мая/июня/июля/августа/сентября/октября/ноября/декабря)
- `* Updated on <Mon DD, YYYY>` → `* Обновлено <DD месяца YYYY> г.`
- `## Related topics` → `## Связанные темы`
- `title:` во frontmatter переводится; `source:`/`scraped:` — байт-в-байт EN (движок сам).

## Структура message-файлов (dtax-messages, zdc-system-messages) — bullet-формат

Лейблы (фиксировано: ims-messages/zos-java-messages):
- `**Full message**` → `**Полное сообщение**` — **значение остаётся EN дословно** (это буквальный системный вывод, как код).
- `**Explanation**` → `**Пояснение**` — проза переводится.
- `**System action**` → `**Действие системы**` — проза переводится.
- `**User response**` → `**Реакция пользователя**` — проза переводится.

Движок `build_messages` сам подставляет лейблы и держит Full message EN. Субагент даёт
только `PROSE` (EN-значение → RU) для Explanation/System action/User response и `META`
(всё остальное: title/#/read/intro/continuation-абзацы/Related-topics).

Заголовки message-ID (`## ZDC000I`, `### ZDTP001S`) — passthrough EN (движок сам по regex).

### Повторяющиеся значения message-прозы (норма; дай ровно так)
- `Processing continues.` → `Обработка продолжается.`
- `Informational, processing continues.` → `Информационное сообщение, обработка продолжается.`
- `Processing fails.` → `Обработка завершается ошибкой.`
- `Processing terminates with a dump.` → `Обработка завершается с дампом.`
- `zDC terminates.` → `zDC завершает работу.`
- `zDC execution ends.` → `Выполнение zDC завершается.`
- `None` → `Нет` ; `None.` → `Нет.`
- `Please contact a Dynatrace product expert via live chat within your environment.` → `Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.`
- `Please contact a Dynatrace product expert via live chat within your Dynatrace environment.` → `Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.`
- `CICS code module is disabled.` → `Кодовый модуль CICS отключён.`

## z/OS терминология (норма соседей)

| EN | RU |
|---|---|
| module (zRemote/zDC/zLocal/CICS/IMS) | модуль (имена zRemote/zDC/zLocal — **EN**) |
| code module | кодовый модуль |
| subsystem | подсистема |
| dataset / data set | набор данных |
| address space | адресное пространство |
| region (CICS/IMS) | регион |
| started task | запускаемая задача (started task — если так у соседа) |
| member (PDS) | элемент |
| procedure / PROC | процедура |
| utility / utility program | служебная программа |
| storage (z/OS) | память (контекстно: память/хранилище) |
| mainframe | мейнфрейм |
| Hardware requirements | Требования к аппаратному обеспечению |
| System requirements | Системные требования |
| Supported operating systems | Поддерживаемые операционные системы |
| Installer overview | Обзор установщика |
| installation directory | каталог установки |
| recovery routine | подпрограмма восстановления |
| dynamic storage | динамическая память |
| data center | дата-центр |
| connection latency | задержка соединения |
| full-stack monitoring mode | режим Full-Stack Monitoring |
| host group | Host group (UI bold-лейбл — EN) |
| We recommend / You can | Мы рекомендуем / можно (НЕ «вы можете») |

## EN-lock (оставлять EN, НЕ переводить)
- Имена компонентов: `zRemote`, `zDC`, `zLocal`, `OneAgent`, `ActiveGate`, `Dynatrace`, `Db2`, `CICS`, `IMS`, `z/OS`, `z/OS Java`, `RTM`, `ABEND`, `EREP`, `JCL`, `PROC`, `STC`.
- Полные тексты системных сообщений (Full message value), коды (`R15`, `SYS1.LOGREC`, `SFT`, `@@`).
- UI bold-лейблы: `**Host groups**`, `**Db2 SQL statement fetch**` и аналогичные именованные настройки.
- Архитектуры/дистрибутивы/версии: `x86-64`, `s390`, `Xeon E5-2600 series`, `Red Hat Enterprise Linux`, `SUSE`, и т.п.
- img-alt — EN.

## Числа и единицы
- Разделитель тысяч: `4,000` → `4 000` (узкий пробел/обычный пробел как у соседа — обычный пробел).
- Единицы: `4GB` → `4 ГБ`, `20GB` → `20 ГБ`, `3 seconds` → `3 секунды`.

## CLI-файл (oneagent-configuration-via-command-line-interface)
- `oneagentctl` и все флаги/команды (`--set-host-group`, `--get-host-id` и т.п.) — **EN дословно** (это команды).
- Заголовки-команды (`## Set host group`) переводятся как действие («## Задать группу хостов»), якорь сохраняется (это h2, line-parity). Сверять с тем, как переведены соседние how-to в корпусе.
- Прозу-описание флага переводить; пример вывода в код-блоке — движок держит byte-identity.

## Жёсткие правила (из CLAUDE.md §0 + блайндспоты)
1. **НЕТ em-dash `—`** в RU. Дефиниция `X — это Y` → `X, это Y` или `X: Y`. Перечисление через `—` → `:`.
2. **НЕТ кальки** «вы можете/должны/хотите» (вкл. несмежные «вы всегда можете») → безличное «можно/нужно/требуется». Условное «если вы используете/запускаете» — норма, не трогать.
3. **Tooltip за ссылкой** `[текст](url "EN tooltip")` — переводить tooltip-прозу (product-name типа `"Db2"` — EN).
4. **Квантор + EN-сущ.** «два/оба/несколько receiver» → опора «два экземпляра/компонента <EN>».
5. **Link-text внутренней ссылки** = RU-`title:` целевого .md (если EN брал title как текст).
6. **mojibake** (`ï»¿`, `â€`, `Ã`) из EN — чистить в RU.
7. Код-блоки, URL, число/уровень заголовков — byte/identity (движок гарантирует, не ломать).
