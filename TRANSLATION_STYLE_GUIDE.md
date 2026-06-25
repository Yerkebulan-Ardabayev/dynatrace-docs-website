# Translation Style Guide — RU

Этот гайд читает каждый Sonnet-агент перед переводом, чтобы переводы оставались консистентными.

## Frontmatter

Сохраняем ВСЕ поля. Переводим **только** `title`. `source`, `scraped`, `updated`, любые id — копируем как есть.

```yaml
---
title: <ПЕРЕВЕДЁННЫЙ заголовок>
source: <оригинальный URL>
scraped: <оригинальная дата>
---
```

## Что НЕ переводим (оставляем как есть на английском)

### Названия продуктов и компонентов Dynatrace
- Dynatrace, Dynatrace Managed, Dynatrace SaaS
- OneAgent, ActiveGate, Cluster ActiveGate, Environment ActiveGate
- Mission Control, Davis AI, Davis CoPilot, Grail, AppEngine
- Smartscape, PurePath, Session Replay
- Cluster Management Console (CMC) / Cluster Console
- Investigations, Notebooks, Dashboards (если это **название продукта**, не общее слово)

### Технические термины (стандарт de facto)
- DQL, USQL, API, REST, SaaS, IaaS, PaaS
- TLS, SSL, mTLS, SSO, SAML, OIDC, LDAP, RBAC, IAM
- CPU, RAM, IOPS, RPS, NUMA
- Cassandra, Elasticsearch, NGINX, systemd, SELinux
- IP, DNS, FQDN, VPN, proxy (можно «прокси»), firewall (можно «фаервол»)

### UI-элементы (если в оригинале выделены `**bold**` или `[Button]`)
Оставляем английскую надпись как есть, потому что в реальном UI она английская:
```
EN: Click **Save changes** to apply.
RU: Нажмите **Save changes**, чтобы применить.
```

### Имена файлов, пути, команды, код
- `/opt/dynatrace-managed/launcher` — не переводим
- `dynatrace.sh stop` — не переводим
- блоки ```...``` — не переводим
- inline `code` — не переводим

## Что переводим

### Общие технические термины
| EN | RU |
|---|---|
| cluster | кластер |
| node | узел |
| backup | резервная копия / резервное копирование |
| restore | восстановление |
| deployment | развёртывание |
| migration | миграция |
| installation | установка |
| upgrade | обновление |
| latency | задержка |
| throughput | пропускная способность |
| storage | хранилище |
| environment | окружение / среда |
| monitoring | мониторинг |
| host | хост |
| transaction storage | хранилище транзакций |
| disaster recovery | аварийное восстановление |
| high availability | высокая доступность |
| rack awareness | rack-aware размещение (или «осведомлённость о стойках») |
| load balancer | балансировщик нагрузки |
| failover | переключение при отказе (failover можно оставить термином) |

### Заголовки
Переводим. Сохраняем уровень `#`, `##`, `###`.

### Списки, таблицы, ссылки
- Текст списков и таблиц — переводим.
- В ссылках `[текст](url "title")` — переводим **текст** и **title**, URL **не трогаем**.
- Якоря (`#backup-method`) **не трогаем**.

### Картинки
- `![alt-text](url "title")` — переводим `alt-text` и `title`, URL не трогаем.

## Стиль

- Обращение: **вы** (формальное), без капитализации.
- Тон: технический, нейтральный, инструктивный. Без маркетинга.
- Избегать кальки: «вы должны» → «необходимо» / «следует» / «нужно».
- Запятые перед «однако», «поэтому», «также», «например» — по правилам РЯ.
- Числа: 1, 2, 10 — арабские; «один из трёх» — для текста.
- Не сокращать «т.е.», «т.к.» в формальных абзацах — лучше «то есть», «так как».

## Запрещено

- **НЕ выдумывать** факты, которых нет в оригинале.
- **НЕ удалять** ссылки, картинки, фрагменты кода.
- **НЕ переводить** код, ID, hostnames, ENV-переменные.
- **НЕ менять** структуру Markdown (количество и уровень заголовков, порядок секций, табличные строки/колонки).
- **НЕ добавлять** «Введение», «Заключение» от себя.
- **НЕ упоминать** что текст переведён ИИ.
- **НЕ переводить** roadmap-даты как маркетинг (см. CLAUDE.md правило «tech-точность»).
- **НЕ упоминать** DQL/Grail/Apps как доступные в Managed (см. `feedback_dql_only_saas.md`). Если в оригинале SaaS-only фича — оставить как есть с пометкой «SaaS-only».

## Пример (фрагмент)

**EN:**
```markdown
* Updated on Jul 17, 2025

Cluster migration options depend on the details of your deployment environment (latency, proximity, and traffic volume), downtime tolerance, and data policies.
```

**RU:**
```markdown
* Updated on Jul 17, 2025

Варианты миграции кластера зависят от особенностей вашей среды развёртывания (задержка, расположение и объём трафика), допустимого времени простоя и политик работы с данными.
```

Дата `Updated on Jul 17, 2025` остаётся в оригинале — это metadata от scraper'а.
