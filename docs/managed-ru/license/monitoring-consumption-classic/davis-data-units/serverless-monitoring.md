---
title: DDU для бессерверных функций
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring
scraped: 2026-05-12T11:52:02.760066
---

# DDU для бессерверных функций

# DDU для бессерверных функций

* 2-min read
* Published Mar 30, 2021

Dynatrace мониторирует бессерверные вычислительные технологии через интеграцию с провайдерами облачных платформ и интеграции трассировки.

## Метрики из интеграций с облачными провайдерами

Облачные сервисы (включая бессерверные функции и бессерверные контейнеры), мониторируемые с помощью интеграций с облачными провайдерами (Amazon CloudWatch, Azure Monitor или Google Cloud Operation Suite), как правило, потребляют пользовательские метрики. Подробнее см. в [DDU для пользовательских метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Логи приложений и платформ

Dynatrace позволяет принимать лог-файлы из ваших бессерверных облачных сервисов, что потребляет единицы Davis data units. Подробнее см. в [DDU для лог-файлов](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.").

## Трассировка AWS Lambda

Для [интеграции трассировки AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.") потребление мониторинга основано на единицах Davis data units. Dynatrace подсчитывает общее число вызовов (например, запросов) мониторируемых функций. За каждый вызов вычитается 0,002 DDU из доступной квоты.

Например, если вы мониторируете 1 функцию, вызываемую 1 миллион раз, потребление DDU рассчитывается следующим образом: `1 функция × 1 миллион вызовов × 0,002 веса DDU = 2 000 DDU в месяц на функцию`.

## Трассировка Azure Functions

Azure Functions предоставляет множество различных вариантов размещения с разными возможностями интеграции трассировки. [Трассировка Azure Functions на плане App Service (Dedicated)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") потребляет хост-единицы.

Для [трассировки Azure Functions на плане потребления (consumption plan)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans") потребление мониторинга основано на единицах Davis data units. Dynatrace подсчитывает общее число вызовов мониторируемых функций. За каждый вызов вычитается 0,002 DDU из доступной квоты.

Например, при мониторинге 1 функции с 1 миллионом вызовов потребление DDU составит: `1 функция × 1 миллион вызовов × 0,002 веса DDU = 2 000 DDU в месяц на функцию`.

## Трассировка Google Functions

Для [трассировки Google Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.") потребление мониторинга основано на единицах Davis data units. Dynatrace подсчитывает общее число вызовов мониторируемых функций. За каждый вызов вычитается 0,002 DDU из доступной квоты.

Например, при мониторинге 1 функции с 1 миллионом вызовов потребление DDU составит: `1 функция × 1 миллион вызовов × 0,002 веса DDU = 2 000 DDU в месяц на функцию`.

## Интеграции трассировки с мониторингом только приложений

Трассировка бессерверных вычислительных сервисов, таких как Azure Container Instances или AWS Fargate, потребляет хост-единицы. Подробнее см. в [Бессерверные функции](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring#serverless-functions "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

Подробнее о расчёте хост-единиц и потреблении мониторинга для бессерверного мониторинга с помощью мониторинга только приложений см. в [Мониторинг только приложений](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring#application-only-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Расширение Dynatrace (единицы Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDU для метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")