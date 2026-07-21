---
title: DDU для бессерверных функций
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units/serverless-monitoring
---

# DDU для бессерверных функций

# DDU для бессерверных функций

* Чтение за 2 мин
* Опубликовано 30 марта 2021 г.

Dynatrace отслеживает бессерверные вычислительные технологии через интеграцию с облачными платформами и трассировочные интеграции.

## Метрики, полученные из интеграций облачных провайдеров

Облачные сервисы (включая бессерверные функции и бессерверные контейнеры), которые отслеживаются с помощью интеграций облачных провайдеров для Amazon CloudWatch, Azure Monitor или Google Cloud Operation Suite, обычно потребляют пользовательские метрики. Подробности см. в разделе [DDU для пользовательских метрик](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Логи приложений и платформы

Dynatrace позволяет получать файлы логов из бессерверных облачных сервисов, что расходует Davis data units. Подробности см. в разделе [DDU для файлов логов](/managed/license/classic-licensing/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").

## Трассировка AWS Lambda

Для [интеграции трассировки AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.") потребление при мониторинге рассчитывается на основе Davis data units. Dynatrace подсчитывает общее число вызовов (например, запросов) отслеживаемых функций. За каждый вызов из доступной квоты списывается 0,002 DDU.

Например, если отслеживается 1 функция и эта функция вызывается 1 миллион раз, потребление DDU рассчитывается так: `1 функция × 1 миллион вызовов × вес 0,002 DDU = 2000 DDU в месяц на функцию`.

## Трассировка Azure Function

Azure Functions предоставляет много разных вариантов размещения с разными возможностями интеграции трассировки. [Трассировка Azure Functions в плане App Service (Dedicated)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") расходует host units.

Для [трассировки Azure Functions в consumption plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans") потребление при мониторинге рассчитывается на основе Davis data units. Dynatrace подсчитывает общее число вызовов (например, запросов) отслеживаемых функций. За каждый вызов из доступной квоты списывается 0,002 DDU.

Например, если отслеживается 1 функция и эта функция вызывается 1 миллион раз, потребление DDU рассчитывается так: `1 функция × 1 миллион вызовов × вес 0,002 DDU = 2000 DDU в месяц на функцию`.

## Трассировка Google Functions

Для [трассировки Google Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.") потребление при мониторинге рассчитывается на основе Davis data units. Dynatrace подсчитывает общее число вызовов (например, запросов) отслеживаемых функций. За каждый вызов из доступной квоты списывается 0,002 DDU.

Например, если отслеживается 1 функция и эта функция вызывается 1 миллион раз, потребление DDU рассчитывается так: `1 функция × 1 миллион вызовов × вес 0,002 DDU = 2000 DDU в месяц на функцию`.

## Трассировочные интеграции с мониторингом только приложений

Трассировка бессерверных вычислительных сервисов, таких как контейнерные инстансы Azure или AWS Fargate, расходует host units. Подробнее см. в разделе [Бессерверные функции](/managed/license/classic-licensing/application-and-infrastructure-monitoring#serverless-functions "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

Подробности о расчёте host units и потреблении при мониторинге для бессерверного мониторинга с использованием [мониторинга только приложений, включая PaaS и некоторые Serverless](/managed/license/classic-licensing/application-and-infrastructure-monitoring#application-only-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Связанные темы

* [Цены на Dynatrace﻿](https://www.dynatrace.com/pricing/)
* [Классическое лицензирование Dynatrace](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.")
* [Расширение Dynatrace (Davis data units)](/managed/license/classic-licensing/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDU для метрик](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")