---
title: Настройка Dynatrace на Amazon Web Services
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services
scraped: 2026-03-06T21:15:47.416400
---

Dynatrace предлагает как мониторинг инфраструктуры всех сервисов AWS, так и полный мониторинг стека (full-stack) для сервисов, которые можно инструментировать с помощью технологии OneAgent. Помимо этого, вы можете выбрать мониторинг логов, генерируемых облачными сервисами, а также собственных сервисов, размещённых на виртуальных машинах или в контейнерах.

Дополнительные причины для мониторинга AWS с помощью Dynatrace см. в разделе [AWS](https://www.dynatrace.com/hub/detail/aws/?query=aws) в Dynatrace Hub.

## Новый мониторинг облачных платформ

Узнайте, как интегрировать Dynatrace с AWS.

[![AWS Cloud Monitoring (Preview)](https://dt-cdn.net/hub/aws_eABzzSW.png "AWS Cloud Monitoring (Preview)")

### Мониторинг облачной платформы AWS

Последняя версия Dynatrace

Подключите свои аккаунты AWS к Dynatrace и управляйте вновь созданными подключениями AWS непосредственно из раздела ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.](amazon-web-services/aws-onboarding.md "Learn about our latest AWS Cloud Platform Monitoring.")

## Классический мониторинг облачных платформ

Узнайте, как интегрировать Dynatrace с Amazon CloudWatch.

[### Комплексное руководство по мониторингу сервисов AWS

Настройте мониторинг инфраструктуры для AWS и принимайте данные в Dynatrace удалённо из CloudWatch.](amazon-web-services/integrate-with-aws/cloudwatch-metrics.md "Integrate metrics from Amazon CloudWatch.")[### Приём потоков метрик Amazon CloudWatch

Передавайте метрики CloudWatch, выпущенные в заданном регионе AWS, через Amazon Data Firehose в Dynatrace.](amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams.md "Ingest metrics from your AWS accounts using Amazon CloudWatch Metric Streams.")[### Мониторинг логов

Мониторинг логов, генерируемых облачными сервисами AWS, а также собственных сервисов, размещённых на виртуальных машинах или в контейнерах.](amazon-web-services/integrate-with-aws/aws-logs-ingest.md "Ingest logs from your AWS accounts.")[### Облачные сервисы AWS

Мониторинг дополнительных облачных сервисов AWS и просмотр их специфических метрик в Dynatrace.](amazon-web-services/integrate-with-aws/aws-all-services.md "Monitor all AWS cloud services with Dynatrace and view available metrics.")

## Полная наблюдаемость за вычислительными и бессерверными ресурсами AWS

Узнайте, как интегрировать Dynatrace в платформу AWS с помощью OneAgent.

[### Amazon EC2

Распространяйте и автоматически развёртывайте OneAgent на экземплярах EC2 с помощью AWS Systems Manager Distributor.](amazon-web-services/integrate-into-aws/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor.md "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package.")[### Amazon ECS

Развёртывание OneAgent в Elastic Container Service.](amazon-web-services/integrate-into-aws/aws-ecs.md "Monitor Amazon Elastic Container Service (ECS)")[### Amazon EKS

Развёртывание OneAgent и мониторинг Amazon Elastic Kubernetes Service.](amazon-web-services/integrate-into-aws/aws-eks.md "Install OneAgent on Elastic Kubernetes Service.")[### AWS App Runner

Развёртывание OneAgent на AWS App Runner.](amazon-web-services/integrate-into-aws/app-runner.md "Install OneAgent on AWS App Runner.")[### AWS Elastic Beanstalk

Развёртывание OneAgent на AWS Elastic Beanstalk.](amazon-web-services/integrate-into-aws/aws-beanstalk.md "Install OneAgent on AWS Elastic Beanstalk.")[### AWS Fargate

Развёртывание OneAgent на AWS Fargate.](amazon-web-services/integrate-into-aws/aws-fargate.md "Install OneAgent on AWS Fargate.")[### AWS Lambda

Интеграция с AWS Lambda.](amazon-web-services/integrate-into-aws/aws-lambda-integration.md "AWS Lambda capabilities and integration options")

## Связанные темы

* [Мониторинг Amazon Web Services](../observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring.md "Monitor AWS with Dynatrace")
* [Мониторинг бессерверных сервисов](../discover-dynatrace/get-started/serverless-monitoring.md "Serverless observability with Dynatrace")
