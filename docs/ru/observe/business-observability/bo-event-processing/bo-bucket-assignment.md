---
title: Назначение бакетов бизнес-событий через классический конвейер
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing/bo-bucket-assignment
scraped: 2026-03-06T21:14:35.723933
---

# Business event bucket assignment via classic pipeline

* Latest Dynatrace

Бизнес-события могут храниться в бакетах с различными периодами хранения. Вы создаёте правила с матчер-специфичными запросами DQL для назначения совпадающих бизнес-событий в определённый бакет. Период хранения по умолчанию для встроенного бакета бизнес-событий (`default_bizevents`) составляет 35 дней. Вы также можете создавать [пользовательские бакеты](../../../platform/grail/organize-data/assign-permissions-in-grail.md#custom-grail-buckets "Find out how to assign permissions to buckets and tables in Grail.") с определённым периодом хранения.

Для пользовательских бакетов возможный период хранения варьируется от 1 дня до 10 лет плюс дополнительная неделя.

Бизнес-события могут храниться в различных бакетах, которые определяют время хранения и разрешения доступа. Вы можете создавать правила с матчер-специфичными запросами DQL для назначения совпадающих бизнес-событий в бакет. По умолчанию каждое входящее бизнес-событие сохраняется в бакете по умолчанию с периодом хранения 35 дней. Также можно задавать более длительные или более короткие периоды.

## Выбор периода хранения

1. Перейдите в **Settings** > **Business Observability** > **Ingest Pipeline** > **Bucket assignment**.
2. В разделе **Business event bucket assignment** выберите **Add rule** и задайте имя правила.
3. Выберите **Bucket**.
4. Добавьте **Matcher** к вашему правилу, введя или вставив [матчер-специфичный DQL-запрос](../../../analyze-explore-automate/logs/lma-classic-log-processing.md#dql-functions "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation."). События, соответствующие вашему правилу, будут назначены в выбранный бакет. Если ни одно правило не совпало, события будут назначены в бакет по умолчанию.
5. Выберите **Save changes**.

## Примеры матчеров

* Если вам нужно добавить только один тип события (например, `com.easytrade.buy-assets`), матчер будет выглядеть следующим образом:

```
matchesValue(event.type, "com.easytrade.buy-assets")
```

* Для двух типов событий в рамках одного провайдера событий матчер будет выглядеть так:

```
matchesValue(event.type, "com.easytrade.buy-assets") or matchesValue(event.type, "com.  easytrade.sell-assets")
```

* В данном случае, однако, нужно охватить все типы событий провайдера EasyTrade, поэтому достаточно использовать:

```
matchesValue(event.provider, "www.easytrade.com")
```
