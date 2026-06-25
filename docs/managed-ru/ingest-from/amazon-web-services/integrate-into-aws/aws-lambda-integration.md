---
title: Мониторинг AWS Lambda
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration
scraped: 2026-05-12T11:14:22.725864
---

# Мониторинг AWS Lambda

# Мониторинг AWS Lambda

* Пояснение
* Чтение: 3 мин
* Обновлено 17 февраля 2026 г.

Dynatrace обеспечивает сквозную наблюдаемость для функций AWS Lambda через распределённую трассировку, корреляцию логов и аналитику на базе ИИ с использованием автоинструментации без изменений в коде. Расширение OneAgent AWS Lambda собирает логи напрямую из Lambda-функций, предлагая альтернативу CloudWatch через Firehose с меньшей стоимостью, меньшей задержкой и более простой настройкой.

[#### Трассировка Lambda-функций

Мониторинг функций AWS Lambda.

* Практическое руководство

Читать руководство](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions)[#### Трассировка Lambda-функций на .NET

Трассировка функций AWS Lambda, использующих среду выполнения .NET

* Практическое руководство

Читать руководство](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration)

[#### Сбор логов AWS Lambda

Сбор логов из функций AWS Lambda

* Практическое руководство

Читать руководство](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector)[#### Мониторинг AWS Lambda (built-in)

Мониторинг AWS Lambda (built-in) и просмотр доступных метрик.

* Практическое руководство

Читать руководство](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin)

[#### Интеграция Dynatrace Lambda Layer в образы контейнеров

Развёртывание Dynatrace Lambda Layers при поставке через образ контейнера.

* Практическое руководство

Читать руководство](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/deploy-oa-latest-lambda-container-images)

## Интеграции

Инструментация AWS Lambda доступна для следующих сред выполнения:

| Среда выполнения | Версия Lambda layer[1](#fn-1-1-def) | Применимо к Lambda Classic |
| --- | --- | --- |
| Python | 1.321 (или выше) | Да |
| Node.js | 1.319 (или выше) | Да |
| Java | 1.319 (или выше) | Да |
| .NET | Скоро | Да |
| Go | 1.333 (или выше) | Только мониторинг логов |

1

Offline-кластеры Managed не поддерживаются.

Подробнее см. в разделе [Поддержка технологий](/managed/ingest-from/technology-support "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

## Потребление ресурсов мониторинга

Для AWS Lambda потребление ресурсов мониторинга рассчитывается на основе Davis data units. Подробности см. в разделе [Бессерверный мониторинг](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление при бессерверном мониторинге.").

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Изучите ключевые концепции OneAgent и узнайте, как устанавливать и эксплуатировать OneAgent на различных платформах.")