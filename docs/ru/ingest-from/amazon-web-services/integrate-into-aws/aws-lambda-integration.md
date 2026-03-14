---
title: Мониторинг AWS Lambda
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration
scraped: 2026-03-06T21:18:18.856655
---

# Monitor AWS Lambda

# Monitor AWS Lambda

* Classic
* Объяснение
* Чтение: 3 мин
* Обновлено 12 января 2026 г.

Dynatrace обеспечивает сквозную наблюдаемость функций AWS Lambda посредством распределённой трассировки, корреляции журналов и аналитики на основе ИИ с использованием автоматической инструментации без изменения кода. Расширение OneAgent для AWS Lambda собирает журналы непосредственно из функций Lambda, предлагая альтернативу CloudWatch через Firehose с меньшими затратами, меньшей задержкой и более простой настройкой.

[#### Trace Lambda functions

Мониторинг функций AWS Lambda.

* Практическое руководство

Читать руководство](aws-lambda-integration/trace-lambda-functions.md)[#### Trace .NET Lambda functions

Трассировка функций AWS Lambda с использованием среды выполнения .NET

* Практическое руководство

Читать руководство](aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration.md)

[#### AWS Lambda log collection

Сбор журналов из функций AWS Lambda

* Практическое руководство

Читать руководство](aws-lambda-integration/collector.md)[#### Monitor AWS Lambda (built-in)

Мониторинг AWS Lambda (встроенный) и просмотр доступных метрик.

* Практическое руководство

Читать руководство](../integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin.md)

[#### Integrate Dynatrace Lambda Layer on container images

Развёртывание Dynatrace Lambda Layers при развёртывании через образ контейнера.

* Практическое руководство

Читать руководство](aws-lambda-integration/deploy-oa-latest-lambda-container-images.md)

## Интеграции

Инструментация AWS Lambda доступна для следующих сред выполнения:

| Среда выполнения | Версия Lambda layer[1](#fn-1-1-def) | Применимо к Lambda Classic |
| --- | --- | --- |
| Python | 1.321 (или новее) | Да |
| Node.js | 1.319 (или новее) | Да |
| Java | 1.319 (или новее) | Да |
| .NET | Скоро | Да |
| GO | Скоро | Только мониторинг журналов |

1

Управляемые автономные кластеры не поддерживаются.

Дополнительные сведения см. в разделе [Поддержка технологий](../../technology-support.md "Найдите технические подробности, связанные с поддержкой Dynatrace для конкретных платформ и фреймворков разработки.").

## Потребление мониторинга

Для AWS Lambda потребление мониторинга рассчитывается на основе единиц данных Davis. Подробности см. в разделе [Мониторинг бессерверных функций](../../../license/monitoring-consumption-classic/davis-data-units/serverless-monitoring.md "Поймите, как рассчитывается потребление мониторинга бессерверных функций.").

## Связанные темы

* [Dynatrace OneAgent](../../dynatrace-oneagent.md "Ознакомьтесь с важными концепциями, связанными с OneAgent, и узнайте, как установить и эксплуатировать OneAgent на различных платформах.")
