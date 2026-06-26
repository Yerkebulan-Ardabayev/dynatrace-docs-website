---
title: Настройка Dynatrace Managed для мониторинга AWS
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed
scraped: 2026-05-12T12:13:23.222603
---

# Настройка Dynatrace Managed для мониторинга AWS

# Настройка Dynatrace Managed для мониторинга AWS

* Обновлено 27 июня 2022 г.

Dynatrace можно интегрировать с [Amazon Web Services (AWS)](https://www.dynatrace.com/technologies/aws-monitoring/) для интеллектуального мониторинга сервисов, работающих в облаке Amazon. Интеграция с AWS помогает отслеживать динамику центра обработки данных в облаке.

Dynatrace можно развернуть с Environment ActiveGate или без него.
При использовании метода доступа на основе ролей необходимо выполнить одно из следующих требований к развёртыванию:

* При развёртывании с Environment ActiveGate среда Environment ActiveGate должна быть размещена в AWS.
* При развёртывании без Environment ActiveGate Dynatrace Managed Server должен быть размещён в AWS.

## Обзор

Выполните следующие основные шаги для интеграции Dynatrace Managed с Amazon Web Services (AWS):

1. [Настройте метод доступа](#access-method)
2. [Выберите раздел AWS](#partition)
3. [Настройте мониторинг под свои потребности](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#define-aws-resource-tagging "Подключите Amazon-аккаунт к Dynatrace Managed и начните мониторинг.")

Потребление для мониторинга облачных сервисов

Все облачные сервисы потребляют [единицы данных Davis (DDU)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU)."). Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к получению 1 точки данных; 1 точка данных потребляет 0,001 DDU).

### Затраты AWS

Dynatrace выполняет API-запросы к Amazon каждые пять минут. Помимо API-вызовов CloudWatch, Dynatrace отправляет API-запросы к отслеживаемым сервисам AWS для получения сведений об экземплярах, тегах и т. д. Список вызываемых сервисов и действий доступен ниже в разделе [Создание политики мониторинга](#monitoring-policy).

Ниже приведена приблизительная оценка затрат на мониторинг AWS:

| Сервис AWS | Количество метрик | Суточная стоимость на экземпляр (USD) |
| --- | --- | --- |
| Elastic Compute Cloud (EC2) | 7 | $0,02016 |
| Elastic Block Store (EBS) | 8 | $0,02304 |
| Elastic Load Balancer (ELB) | 11 | $0,03168 |
| Relational Database Service (RDS) | 11 | $0,03168 |
| DynamoDB | 15 | $0,06912 |
| Lambda | 4 | $0,01152 |

Оплата Amazon

Amazon взимает около $0,01 за 1000 метрик, запрошенных через CloudWatch API, и включает эту стоимость в счёт для AWS-аккаунта, используемого с Dynatrace.

## Политика мониторинга AWS

Политика мониторинга AWS определяет минимальный набор разрешений, которые необходимо предоставить Dynatrace для мониторинга сервисов в AWS-аккаунте. Создайте её один раз и используйте каждый раз при предоставлении Dynatrace доступа к AWS-аккаунту.
Если не нужно добавлять разрешения для всех сервисов и требуется выбрать разрешения только для определённых, обратитесь к таблице ниже. В таблице содержится набор разрешений, необходимых для [всех облачных сервисов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также список необязательных разрешений для каждого облачного сервиса.

Разрешения, необходимые для интеграции мониторинга AWS:

* `"cloudwatch:GetMetricData"`
* `"cloudwatch:GetMetricStatistics"`
* `"cloudwatch:ListMetrics"`
* `"sts:GetCallerIdentity"`
* `"tag:GetResources"`
* `"tag:GetTagKeys"`
* `"ec2:DescribeAvailabilityZones"`

### Полный список разрешений для облачных сервисов

| Название | Разрешения |
| --- | --- |
| Все отслеживаемые сервисы Amazon (обязательно) | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
| AWS Certificate Manager Private Certificate Authority | `acm-pca:ListCertificateAuthorities` |
| Amazon MQ |  |
| Amazon API Gateway | `apigateway:GET` |
| AWS App Runner | `apprunner:ListServices` |
| Amazon AppStream | `appstream:DescribeFleets` |
| AWS AppSync | `appsync:ListGraphqlApis` |
| Amazon Athena | `athena:ListWorkGroups` |
| Amazon Aurora | `rds:DescribeDBClusters` |
| Amazon EC2 Auto Scaling | `autoscaling:DescribeAutoScalingGroups` |
| Amazon EC2 Auto Scaling (built-in) | `autoscaling:DescribeAutoScalingGroups` |
| AWS Billing |  |
| Amazon Keyspaces |  |
| AWS Chatbot |  |
| Amazon CloudFront | `cloudfront:ListDistributions` |
| AWS CloudHSM | `cloudhsm:DescribeClusters` |
| Amazon CloudSearch | `cloudsearch:DescribeDomains` |
| AWS CodeBuild | `codebuild:ListProjects` |
| Amazon Cognito |  |
| Amazon Connect |  |
| Amazon Elastic Kubernetes Service (EKS) | `eks:ListClusters` |
| AWS DataSync | `datasync:ListTasks` |
| Amazon DynamoDB Accelerator (DAX) | `dax:DescribeClusters` |
| AWS Database Migration Service (AWS DMS) | `dms:DescribeReplicationInstances` |
| Amazon DocumentDB | `rds:DescribeDBClusters` |
| AWS Direct Connect | `directconnect:DescribeConnections` |
| Amazon DynamoDB | `dynamodb:ListTables` |
| Amazon DynamoDB (built-in) | `dynamodb:ListTables`, `dynamodb:ListTagsOfResource` |
| Amazon EBS | `ec2:DescribeVolumes` |
| Amazon EBS (built-in) | `ec2:DescribeVolumes` |
| Amazon EC2 API |  |
| Amazon EC2 (built-in) | `ec2:DescribeInstances` |
| Amazon EC2 Spot Fleet | `ec2:DescribeSpotFleetRequests` |
| Amazon Elastic Container Service (ECS) | `ecs:ListClusters` |
| Amazon ECS Container Insights | `ecs:ListClusters` |
| Amazon ElastiCache (EC) | `elasticache:DescribeCacheClusters` |
| AWS Elastic Beanstalk | `elasticbeanstalk:DescribeEnvironments` |
| Amazon Elastic File System (EFS) | `elasticfilesystem:DescribeFileSystems` |
| Amazon Elastic Inference |  |
| Amazon Elastic Map Reduce (EMR) | `elasticmapreduce:ListClusters` |
| Amazon Elasticsearch Service (ES) | `es:ListDomainNames` |
| Amazon Elastic Transcoder | `elastictranscoder:ListPipelines` |
| Amazon Elastic Load Balancer (ELB) (built-in) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
| Amazon EventBridge | `events:ListEventBuses` |
| Amazon FSx | `fsx:DescribeFileSystems` |
| Amazon GameLift | `gamelift:ListFleets` |
| AWS Glue | `glue:GetJobs` |
| Amazon Inspector | `inspector:ListAssessmentTemplates` |
| AWS Internet of Things (IoT) |  |
| AWS IoT Analytics |  |
| Amazon Managed Streaming for Kafka | `kafka:ListClusters` |
| Amazon Kinesis Data Analytics | `kinesisanalytics:ListApplications` |
| Amazon Data Firehose | `firehose:ListDeliveryStreams` |
| Amazon Kinesis Data Streams | `kinesis:ListStreams` |
| Amazon Kinesis Video Streams | `kinesisvideo:ListStreams` |
| AWS Lambda | `lambda:ListFunctions` |
| AWS Lambda (built-in) | `lambda:ListFunctions`, `lambda:ListTags` |
| Amazon Lex | `lex:GetBots` |
| Amazon Application and Network Load Balancer (built-in) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
| Amazon CloudWatch Logs | `logs:DescribeLogGroups` |
| AWS Elemental MediaConnect | `mediaconnect:ListFlows` |
| AWS Elemental MediaConvert | `mediaconvert:DescribeEndpoints` |
| AWS Elemental MediaPackage Live | `mediapackage:ListChannels` |
| AWS Elemental MediaPackage Video on Demand | `mediapackage-vod:ListPackagingConfigurations` |
| AWS Elemental MediaTailor | `mediatailor:ListPlaybackConfigurations` |
| Amazon VPC NAT Gateways | `ec2:DescribeNatGateways` |
| Amazon Neptune | `rds:DescribeDBClusters` |
| AWS OpsWorks | `opsworks:DescribeStacks` |
| Amazon Polly |  |
| Amazon QLDB | `qldb:ListLedgers` |
| Amazon RDS | `rds:DescribeDBInstances` |
| Amazon RDS (built-in) | `rds:DescribeDBInstances`, `rds:DescribeEvents`, `rds:ListTagsForResource` |
| Amazon Redshift | `redshift:DescribeClusters` |
| Amazon Rekognition |  |
| AWS RoboMaker | `robomaker:ListSimulationJobs` |
| Amazon Route 53 | `route53:ListHostedZones` |
| Amazon Route 53 Resolver | `route53resolver:ListResolverEndpoints` |
| Amazon S3 | `s3:ListAllMyBuckets` |
| Amazon S3 (built-in) | `s3:ListAllMyBuckets` |
| Amazon SageMaker Batch Transform Jobs |  |
| Amazon SageMaker Endpoint Instances | `sagemaker:ListEndpoints` |
| Amazon SageMaker Endpoints | `sagemaker:ListEndpoints` |
| Amazon SageMaker Ground Truth |  |
| Amazon SageMaker Processing Jobs |  |
| Amazon SageMaker Training Jobs |  |
| AWS Service Catalog |  |
| Amazon Simple Email Service (SES) |  |
| Amazon Simple Notification Service (SNS) | `sns:ListTopics` |
| Amazon Simple Queue Service (SQS) | `sqs:ListQueues` |
| AWS Systems Manager - Run Command |  |
| AWS Step Functions |  |
| AWS Storage Gateway | `storagegateway:ListGateways` |
| Amazon SWF | `swf:ListDomains` |
| Amazon Textract |  |
| AWS IoT Things Graph |  |
| AWS Transfer Family | `transfer:ListServers` |
| AWS Transit Gateway | `ec2:DescribeTransitGateways` |
| Amazon Translate |  |
| AWS Trusted Advisor |  |
| AWS API Usage |  |
| AWS Site-to-Site VPN | `ec2:DescribeVpnConnections` |
| AWS WAF Classic |  |
| AWS WAF |  |
| Amazon WorkMail | `workmail:ListOrganizations` |
| Amazon WorkSpaces | `workspaces:DescribeWorkspaces` |

## Метод доступа

Для получения информации, необходимой для комплексного мониторинга облачных вычислений AWS, Dynatrace должен идентифицировать все компоненты виртуализированной инфраструктуры в AWS-окружении и собирать метрики производительности этих компонентов. Эта информация используется для понимания контекста приложений, сервисов и хостов. Для этого необходимо авторизовать доступ Dynatrace к метрикам Amazon.

Убедитесь, что Environment ActiveGate или Managed Cluster имеет рабочее подключение к AWS. Настройте прокси для [Managed](/managed/managed-cluster/configuration/internet-proxy "Настройка прокси-подключения для Managed Cluster при отсутствии прямого доступа в интернет.") или [ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Узнайте, как настроить свойства ActiveGate для работы через прокси."), либо разрешите доступ к `*.amazonaws.com` в настройках брандмауэра.

## Доступ на основе ролей с Environment ActiveGate или Dynatrace Managed Server

Приведённые ниже инструкции применяются независимо от того, совпадает ли аккаунт, в котором размещён ActiveGate, с отслеживаемым аккаунтом.

В типовой конфигурации необходимо создать два стека CloudFormation с использованием шаблонов CloudFormation:

* Стек CloudFormation из аккаунта, в котором размещён ActiveGate, содержащий следующие ресурсы:

  + роль для Environment ActiveGate или Dynatrace Managed Server, размещённого в инфраструктуре AWS на хосте Amazon EC2;
  + прикреплённую политику, определяющую разрешения отслеживаемого аккаунта.
* Стек CloudFormation из отслеживаемого аккаунта, содержащий следующие ресурсы:

  + выделенную роль мониторинга для Dynatrace в AWS-аккаунте;
  + прикреплённую политику, определяющую разрешения аутентификации Dynatrace для AWS-окружения.

Для мониторинга нескольких аккаунтов добавьте все ресурсы в массив **Resource** шаблона в [Шаге 1](#step1) и повторите [Шаг 2](#step2) для создания стека для каждого отслеживаемого аккаунта.

### Предварительные требования для доступа на основе ролей с Environment ActiveGate или Dynatrace Managed Server

* [Dynatrace Managed Server](/managed/managed-cluster/installation/install-managed-cluster "Установите Managed Cluster, загрузив и проверив установщик, запустив его и выполнив начальную конфигурацию."), установленный на хосте Amazon EC2. Он должен иметь возможность принять роль в AWS-аккаунте, разрешающую чтение данных мониторинга Dynatrace.
* Идентификатор AWS-аккаунта, в котором размещён ActiveGate (например, аккаунт, в котором размещены компоненты Dynatrace, в данном случае это аккаунт с Environment ActiveGate или Dynatrace Managed Server).
* Идентификатор отслеживаемого AWS-аккаунта (аккаунт, который требуется мониторить).
* Имя роли, с которой был запущен Environment ActiveGate или Dynatrace Managed Server.
* Внешний идентификатор (External ID).

  Как получить внешний идентификатор

  1. Перейдите в **Settings**.
  2. Выберите **Cloud and virtualization** > **AWS** > **Connect new instance**.
  3. В разделе **Authentication method** выберите **Role-based authentication**.
  4. В разделе **Your Amazon account ID** нажмите **Copy**, чтобы скопировать токен (внешний идентификатор).

Чтобы разрешить доступ к Amazon-аккаунту с использованием доступа на основе ролей, выполните следующие шаги.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание роли для ActiveGate в аккаунте, где размещён ActiveGate**](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#step1 "Подключите Amazon-аккаунт к Dynatrace Managed и начните мониторинг.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание роли мониторинга для Dynatrace в отслеживаемом аккаунте**](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#step2 "Подключите Amazon-аккаунт к Dynatrace Managed и начните мониторинг.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Изменение конфигурации ActiveGate**](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#step3 "Подключите Amazon-аккаунт к Dynatrace Managed и начните мониторинг.")

### Шаг 1 Создание роли для ActiveGate в аккаунте, где размещён ActiveGate

1. Создайте YAML-файл и вставьте содержимое [github `role_based_access_AG_account_template.yml`](https://dt-url.net/2t03ydj).

Для нескольких отслеживаемых аккаунтов

Для каждого аккаунта, который требуется отслеживать, в разделе **Resource** приведённого выше шаблона добавьте новый элемент в массив `!Sub` в следующем формате: `'arn:aws:iam::<new_monitored_account_id>:role/<new_monitoring_role_name>'`.

Обязательно замените заполнители (`<new_monitored_account_id>` и `<new_monitoring_role_name>`) собственными значениями.

2. Создайте стек в Amazon Console или через CLI.

В Amazon Console

1. В Amazon Console перейдите в CloudFormation.
2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
4. В разделе **Parameters** в поле **MonitoredAccountID** введите идентификатор аккаунта, который будет отслеживаться Dynatrace. При необходимости адаптируйте другие параметры.
5. Введите имя стека, затем дважды нажмите **Next**.
6. Проверьте конфигурацию, установите флажок **I acknowledge that AWS CloudFormation might create IAM resources with custom names** и нажмите **Create stack**.

Через CLI

Выполните приведённую ниже команду, заменив значения параметров фактическими.

Угловые скобки (`<` и `>`) необходимо удалить.

```
aws cloudformation create-stack \



--capabilities CAPABILITY_NAMED_IAM \



--stack-name <stack_name> \



--template-body <file:///home/user/template_file.yaml> \



--parameters ParameterKey=ActiveGateRoleName,ParameterValue=<role_name> ParameterKey=AssumePolicyName,ParameterValue=<policy_name> ParameterKey=MonitoringRoleName,ParameterValue=<monitoring_role_name> ParameterKey=MonitoredAccountID,ParameterValue=<monitored_account_id>
```

3. Перейдите в консоль Amazon EC2, щёлкните правой кнопкой мыши экземпляр, на котором размещён Environment ActiveGate, и выберите **Security** > **Modify IAM role**.
4. Выберите роль, созданную на шаге 1 (например, Dynatrace\_ActiveGate\_role), и нажмите **Apply**.

### Шаг 2 Создание роли мониторинга для Dynatrace в отслеживаемом аккаунте

После создания `Dynatrace_ActiveGate_role` в аккаунте, где размещён ActiveGate, создайте роль для отслеживаемого аккаунта.

1. Создайте YAML-файл и вставьте содержимое [github `role_based_access_monitored_account_template.yml`](https://dt-url.net/pm03yni).
2. Создайте стек в Amazon Console или через CLI.

   В Amazon Console

   1. В Amazon Console перейдите в CloudFormation.
   2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
   3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
   4. В разделе **Parameters** введите:

   * **External ID**. Подробнее см. [Предварительные требования](#env-ag).
   * **ActiveGateRoleName** и **ActiveGateAccountID** из стека, созданного в [Шаге 1](#step1).

   При необходимости адаптируйте другие параметры.

   5. Введите имя стека, затем дважды нажмите **Next**.
   6. Проверьте конфигурацию, установите флажок **I acknowledge that AWS CloudFormation might create IAM resources with custom names** и нажмите **Create stack**.

   Через CLI

   Выполните приведённую ниже команду, заменив значения параметров фактическими.

   Угловые скобки (`<` и `>`) необходимо удалить.

   ```
   aws cloudformation create-stack \



   --capabilities CAPABILITY_NAMED_IAM \



   --stack-name <stack_name> \



   --template-body <file:///home/user/template_file.yaml> \



   --parameters ParameterKey=ExternalID,ParameterValue=<external_id> ParameterKey=ActiveGateRoleName,ParameterValue=<activegate_role_name> ParameterKey=ActiveGateAccountID,ParameterValue=<activegate_account_id>



   ParameterKey=RoleName,ParameterValue=<role_name> ParameterKey=PolicyName,ParameterValue=<policy_name>
   ```

### Шаг 3 Изменение конфигурации ActiveGate

Начиная с ActiveGate версии 1.217, мониторинг AWS включён по умолчанию. Подробнее о конфигурации см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#aws-monitoring "Узнайте, какие свойства ActiveGate можно настроить в соответствии с потребностями и требованиями."). Следующие параметры конфигурации относятся к более ранним версиям ActiveGate.

1. Отредактируйте файл конфигурации [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить в соответствии с потребностями и требованиями.") ActiveGate, который планируется использовать для мониторинга AWS.
2. Задайте следующие свойства:

   ```
   [aws_monitoring]



   use_aws_proxy_role = false



   aws_monitoring_enabled = true
   ```

   ActiveGate версии 1.183 и ниже

   ```
   [vertical.topology]



   use_aws_proxy_role = false
   ```

   ```
   [aws_monitoring]



   aws_monitoring_enabled = true
   ```

   Несколько ActiveGate

   Достаточно одного ActiveGate, выделенного для мониторинга AWS. Однако некоторые сценарии развёртывания (например, для обеспечения избыточности) могут потребовать нескольких ActiveGate.

   Убедитесь, что только надлежащим образом настроенные ActiveGate имеют `aws_monitoring_enabled` со значением `true`.

   * Им необходим сетевой доступ к эндпоинтам AWS.
   * Для мониторинга на основе ролей к ним должны быть прикреплены соответствующие роли.

   Учтите, что узлы кластера Dynatrace содержат встроенные ActiveGate. Для таких ActiveGate, не настроенных полностью для мониторинга AWS, необходимо установить свойство `aws_monitoring_enabled` в `false`.

   Если ActiveGate предназначен только для мониторинга AWS, также необходимо установить свойство `MSGrouter` в `false`:

   ```
   [collector]



   MSGrouter = false
   ```

   Удалите свойства `aws_proxy_account` и `aws_proxy_role`.
3. Сохраните файл и [перезапустите основной сервис ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate в Windows или Linux.").

Доступ на основе ключей (только для AWS GovCloud и AWS China)

Аутентификация на основе ключей разрешена только для разделов AWS GovCloud и China.

В этом сценарии необходимо создать политику мониторинга AWS и сгенерировать пару ключей с этой политикой.

Границы разрешений AWS IAM могут запрещать действия AWS, необходимые Dynatrace. При использовании границы разрешений IAM в AWS-аккаунте убедитесь, что действия из этой политики разрешены во всех регионах AWS в пределах этой границы.

Для создания политики мониторинга AWS

1. В Amazon Console перейдите в **Identity and Access Management**.
2. Перейдите в **Policies** и выберите **Create policy**.
3. Выберите вкладку JSON и вставьте предопределённую политику из блока ниже.

   ```
   {



   "Version": "2012-10-17",



   "Statement": [



   {



   "Sid": "VisualEditor0",



   "Effect": "Allow",



   "Action": [



   "acm-pca:ListCertificateAuthorities",



   "apigateway:GET",



   "apprunner:ListServices",



   "appstream:DescribeFleets",



   "appsync:ListGraphqlApis",



   "athena:ListWorkGroups",



   "autoscaling:DescribeAutoScalingGroups",



   "cloudformation:ListStackResources",



   "cloudfront:ListDistributions",



   "cloudhsm:DescribeClusters",



   "cloudsearch:DescribeDomains",



   "cloudwatch:GetMetricData",



   "cloudwatch:GetMetricStatistics",



   "cloudwatch:ListMetrics",



   "codebuild:ListProjects",



   "datasync:ListTasks",



   "dax:DescribeClusters",



   "directconnect:DescribeConnections",



   "dms:DescribeReplicationInstances",



   "dynamodb:ListTables",



   "dynamodb:ListTagsOfResource",



   "ec2:DescribeAvailabilityZones",



   "ec2:DescribeInstances",



   "ec2:DescribeNatGateways",



   "ec2:DescribeSpotFleetRequests",



   "ec2:DescribeTransitGateways",



   "ec2:DescribeVolumes",



   "ec2:DescribeVpnConnections",



   "ecs:ListClusters",



   "eks:ListClusters",



   "elasticache:DescribeCacheClusters",



   "elasticbeanstalk:DescribeEnvironmentResources",



   "elasticbeanstalk:DescribeEnvironments",



   "elasticfilesystem:DescribeFileSystems",



   "elasticloadbalancing:DescribeInstanceHealth",



   "elasticloadbalancing:DescribeListeners",



   "elasticloadbalancing:DescribeLoadBalancers",



   "elasticloadbalancing:DescribeRules",



   "elasticloadbalancing:DescribeTags",



   "elasticloadbalancing:DescribeTargetHealth",



   "elasticmapreduce:ListClusters",



   "elastictranscoder:ListPipelines",



   "es:ListDomainNames",



   "events:ListEventBuses",



   "firehose:ListDeliveryStreams",



   "fsx:DescribeFileSystems",



   "gamelift:ListFleets",



   "glue:GetJobs",



   "inspector:ListAssessmentTemplates",



   "kafka:ListClusters",



   "kinesis:ListStreams",



   "kinesisanalytics:ListApplications",



   "kinesisvideo:ListStreams",



   "lambda:ListFunctions",



   "lambda:ListTags",



   "lex:GetBots",



   "logs:DescribeLogGroups",



   "mediaconnect:ListFlows",



   "mediaconvert:DescribeEndpoints",



   "mediapackage-vod:ListPackagingConfigurations",



   "mediapackage:ListChannels",



   "mediatailor:ListPlaybackConfigurations",



   "opsworks:DescribeStacks",



   "qldb:ListLedgers",



   "rds:DescribeDBClusters",



   "rds:DescribeDBInstances",



   "rds:DescribeEvents",



   "rds:ListTagsForResource",



   "redshift:DescribeClusters",



   "robomaker:ListSimulationJobs",



   "route53:ListHostedZones",



   "route53resolver:ListResolverEndpoints",



   "s3:ListAllMyBuckets",



   "sagemaker:ListEndpoints",



   "sns:ListTopics",



   "sqs:ListQueues",



   "storagegateway:ListGateways",



   "sts:GetCallerIdentity",



   "swf:ListDomains",



   "tag:GetResources",



   "tag:GetTagKeys",



   "transfer:ListServers",



   "workmail:ListOrganizations",



   "workspaces:DescribeWorkspaces"



   ],



   "Resource": "*"



   }



   ]



   }
   ```
4. Задайте имя политики.
5. Нажмите **Create policy**.

Dynatrace может использовать ключи доступа для выполнения безопасных запросов по протоколу REST или Query к API сервиса AWS. Необходимо сгенерировать **Access key ID** и **Secret access key**, которые Dynatrace будет использовать для получения метрик из Amazon Web Services.

6. В Amazon Console перейдите в **Users** и выберите **Add Users**.
7. Введите **User name**.
8. На следующем экране выберите **Attach policies directly** и прикрепите ранее созданную политику.
9. Проверьте данные пользователя и нажмите **Create user**.
10. В списке пользователей выберите только что созданного пользователя, перейдите в **Security credentials** и нажмите **Create access key**.
11. На экране **Access key best practices & alternatives** выберите **Third-party service**, затем нажмите **Next**.
12. Откроется экран **Retrieve access keys**, на котором отображаются **Access key** и **Secret access key**.
13. Сохраните значения **Access Key ID** (AKID) и **Secret access key**.
14. Можно либо загрузить учётные данные пользователя, либо скопировать отображаемые онлайн учётные данные (нажмите **Show**).

## Подключение Amazon-аккаунта

После предоставления Dynatrace доступа к AWS можно подключить Dynatrace к Amazon AWS-аккаунту.

1. В Dynatrace перейдите в **Settings > Cloud and virtualization > AWS** и нажмите **Connect new instance**.
2. Выберите метод **Role-based authentication**.

   * Задайте имя для этого подключения. Если поле оставить пустым, для определения подключения на страницах Dynatrace будет использоваться имя **Role**.
   * В поле **Role** введите имя роли, созданной в Amazon для Dynatrace (например, `Dynatrace_monitoring_role`).
   * Введите **Account ID** (аккаунт, из которого будут запрашиваться метрики).
   * Нажмите **Connect** для проверки и сохранения подключения.
3. После успешной проверки и сохранения подключения AWS-аккаунт отобразится на странице настроек **Cloud and virtualization**.
   Вскоре станут доступны данные мониторинга облака AWS.

## Выбор раздела AWS

Если AWS-аккаунт находится в разделе, отличном от раздела `aws` по умолчанию, его можно выбрать, и Dynatrace будет подключаться именно к нему.

Для изменения раздела AWS

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. Найдите экземпляр, для которого требуется изменить раздел, и нажмите ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для его редактирования.
3. В списке **AWS partition** выберите раздел.
4. Нажмите **Save**.

## Настройка мониторинга

Область и содержимое мониторинга можно настроить под свои потребности с помощью тегов и перечня необходимых сервисов.

### Ограничение отслеживаемых ресурсов с помощью тегов

Рекомендуется ограничить область мониторинга AWS и сократить количество API-вызовов к Amazon. Для ограничения ресурсов AWS (экземпляров сервисов AWS), отслеживаемых Dynatrace, можно использовать [теги](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавьте и настройте теги AWS для ограничения ресурсов AWS.").

## Настройка метрических событий для оповещений

Для настройки метрических событий для оповещений следуйте этому [руководству](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-set-up-metric-events-for-alerting "Настройка метрических событий для оповещений.").

### Выбор облачных сервисов для мониторинга

После сохранения учётных данных можно выбрать отслеживаемые сервисы.
Для выбора нужных сервисов

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. Найдите экземпляр, для которого требуется выполнить мониторинг, и нажмите ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для его редактирования.
3. В разделе **Services** нажмите **Manage services**.
4. По умолчанию добавлены следующие сервисы: Amazon EC2, AWS Lambda, Amazon RDS, Amazon DynamoDB, Amazon ALB, Amazon ELB, Amazon S3 и Amazon EBS. Список можно расширить, выбирая сервисы из выпадающего меню. Полный список сервисов также доступен в разделе [Все облачные сервисы AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.").
5. Нажмите **Add service**.
6. Выберите сервис из списка, затем нажмите **Add service**.
7. Нажмите **Save changes** для сохранения конфигурации.

## Связанные темы

* [Настройка Dynatrace для Amazon Web Services](/managed/ingest-from/amazon-web-services "Настройка и конфигурация мониторинга для Amazon Web Services.")
* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Изучите ключевые концепции, связанные с OneAgent, и узнайте, как устанавливать OneAgent на разных платформах и работать с ним.")
* [Ограничение API-вызовов к AWS с помощью тегов](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавьте и настройте теги AWS, чтобы ограничить ресурсы AWS.")