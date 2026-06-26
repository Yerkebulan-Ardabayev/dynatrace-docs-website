---
title: Мониторинг Amazon Web Services с помощью метрик CloudWatch
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics
scraped: 2026-05-12T11:06:54.358122
---

# Мониторинг Amazon Web Services с помощью метрик CloudWatch

# Мониторинг Amazon Web Services с помощью метрик CloudWatch

* Практическое руководство
* Чтение: 23 мин
* Обновлено 04 марта 2026 г.

Следуйте этому руководству, чтобы начать удалённый приём данных из Amazon CloudWatch.

Основное внимание уделяется мониторингу инфраструктуры сервисов AWS: Dynatrace отслеживает сервисы AWS через CloudWatch.

Сведения о мониторинге полного стека и логов AWS-сервисов см. в разделе [Что дальше?](#next).

После настройки первоначального мониторинга можно добавлять, удалять или изменять мониторинг сервисов через веб-интерфейс Dynatrace, в масштабе или с помощью Dynatrace API.

Сведения о собираемых измерениях

Сведения об измерениях, собираемых для каждого из сервисов AWS, см. в:

* [Облачные сервисы AWS, включённые по умолчанию, и метрики](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/default-aws-metrics "Список классических (ранее «встроенных») метрик, которые Dynatrace собирает по умолчанию для мониторинга AWS.")
* [Облачные сервисы AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.")

Мониторинг инфраструктуры Amazon Web Services обеспечивает сбор метрик из CloudWatch, данных инфраструктуры через публичный AWS API и определённых событий. Данные собираются с интервалом в пять минут.

## Стоимость мониторинга

* Каждый сервис, отслеживаемый Dynatrace через CloudWatch, а также обработка и анализ логов потребляют [DDU](/managed/license/monitoring-consumption-classic/davis-data-units "Принципы расчёта потребления мониторинга Dynatrace на основе единиц данных Davis (DDU).").
* Amazon может взимать дополнительную плату за запросы метрик CloudWatch. Подробнее о дополнительных расходах см. в [онлайн-документации по ценам Amazon CloudWatch](https://aws.amazon.com/cloudwatch/pricing/).

## Предварительные требования для мониторинга

Для настройки мониторинга AWS необходимо выполнить три предварительных условия:

1. Права администратора Dynatrace

Для управления конфигурацией мониторинга AWS необходимы разрешения на чтение и изменение схемы `builtin:cloud.aws`.

* Требуются как `settings:objects:read`, так и `settings:objects:write`.
* Они включены в разрешения **Change monitoring settings**.
* Доступ только для чтения не поддерживается.

Сведения об управлении разрешениями и их настройке см. в разделе [Управление разрешениями пользователей с помощью ролей](/managed/manage/identity-access-management/permission-management/role-based-permissions "Разрешения на основе ролей").

2. Разрешить ActiveGate доступ к URL

Для мониторинга Amazon Web Services Dynatrace необходимо периодически подключаться к Amazon CloudWatch API и отправлять запросы. Как минимум один ActiveGate должен иметь возможность подключаться к Amazon CloudWatch для выполнения задач мониторинга. ActiveGate должен быть развёрнут на экземпляре EC2 и иметь доступ к эндпоинтам, перечисленным ниже.

Начиная с Dynatrace версии 1.267+, можно использовать только доступ на основе ролей. Авторизация на основе ключей больше недоступна для новых учётных данных. Для существующих учётных данных на основе ключей можно продолжать использовать ключи бессрочно. Рекомендуется перейти на аутентификацию на основе ролей с помощью специальной кнопки на странице конфигурации. Dynatrace автоматически проверяет конфигурацию для обеспечения правильной настройки ролей.

[Аутентификация на основе ключей](#key-based-authentication) разрешена только для разделов AWS GovCloud и China.

#### Разрешить ActiveGate доступ к URL AWS

Интеграция обращается к следующим эндпоинтам AWS API, поэтому они должны быть доступны из вашего ActiveGate:

* AWS Security Token Service (AWS STS)

Environment ActiveGate версии 1.329+

```
https://sts.<REGION>.amazonaws.com/
```

Environment ActiveGate версии 1.328 и ниже

```
https://sts.amazonaws.com/
```

Начиная с Dynatrace версии 1.329 глобальный эндпоинт AWS STS не поддерживается. Убедитесь, что `sts.<REGION>.amazonaws.com` доступен для регионов, которые требуется отслеживать.

Регион `us-west-2` теперь является регионом ActiveGate по умолчанию. При возникновении проблем с подключением убедитесь, что эндпоинт `sts.us-west-2.amazonaws.com` доступен.

Подробнее см. в разделе [Регионализованные эндпоинты AWS STS](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html).

* AWS Resource Groups Tagging

  ```
  https://tagging.<REGION>.amazonaws.com/
  ```
* Amazon CloudWatch

  ```
  https://monitoring.<REGION>.amazonaws.com/
  ```
* Amazon EC2

  ```
  ec2.<REGION>.amazonaws.com
  ```

В зависимости от отслеживаемых сервисов могут потребоваться другие эндпоинты.

Обратитесь к таблицам ниже для получения эндпоинтов, специфичных для каждого отслеживаемого сервиса, и AWS-регионов, поддерживаемых Dynatrace AWS Monitoring.

### Эндпоинты AWS, которые должны быть доступны из ActiveGate, с соответствующими сервисами AWS

| Эндпоинт | Сервис |
| --- | --- |
| `autoscaling.<REGION>.amazonaws.com` | Amazon EC2 Auto Scaling (built-in), Amazon EC2 Auto Scaling |
| `lambda.<REGION>.amazonaws.com` | AWS Lambda (built-in), AWS Lambda |
| `elasticloadbalancing.<REGION>.amazonaws.com` | Amazon Application and Network Load Balancer (built-in), Amazon Elastic Load Balancer (ELB) (built-in) |
| `dynamodb.<REGION>.amazonaws.com` | Amazon DynamoDB (built-in), Amazon DynamoDB |
| `ec2.<REGION>.amazonaws.com` | Amazon EBS (built-in), Amazon EC2 (built-in), Amazon EBS, Amazon EC2 Spot Fleet, Amazon VPC NAT Gateways, AWS Transit Gateway, AWS Site-to-Site VPN |
| `rds.<REGION>.amazonaws.com` | Amazon RDS (built-in), Amazon Aurora, Amazon DocumentDB, Amazon Neptune, Amazon RDS |
| `s3.<REGION>.amazonaws.com` | Amazon S3 (built-in) |
| `acm-pca.<REGION>.amazonaws.com` | AWS Certificate Manager Private Certificate Authority |
| `apigateway.<REGION>.amazonaws.com` | Amazon API Gateway |
| `apprunner.<REGION>.amazonaws.com` | AWS App Runner |
| `appstream2.<REGION>.amazonaws.com` | Amazon AppStream |
| `appsync.<REGION>.amazonaws.com` | AWS AppSync |
| `athena.<REGION>.amazonaws.com` | Amazon Athena |
| `cloudfront.amazonaws.com` | Amazon CloudFront |
| `cloudhsmv2.<REGION>.amazonaws.com` | AWS CloudHSM |
| `cloudsearch.<REGION>.amazonaws.com` | Amazon CloudSearch |
| `codebuild.<REGION>.amazonaws.com` | AWS CodeBuild |
| `datasync.<REGION>.amazonaws.com` | AWS DataSync |
| `dax.<REGION>.amazonaws.com` | Amazon DynamoDB Accelerator (DAX) |
| `dms.<REGION>.amazonaws.com` | AWS Database Migration Service (AWS DMS) |
| `directconnect.<REGION>.amazonaws.com` | AWS Direct Connect |
| `ecs.<REGION>.amazonaws.com` | Amazon Elastic Container Service (ECS), Amazon ECS Container Insights |
| `elasticfilesystem.<REGION>.amazonaws.com` | Amazon Elastic File System (EFS) |
| `eks.<REGION>.amazonaws.com` | Amazon Elastic Kubernetes Service (EKS) |
| `elasticache.<REGION>.amazonaws.com` | Amazon ElastiCache (EC) |
| `elasticbeanstalk.<REGION>.amazonaws.com` | AWS Elastic Beanstalk |
| `elastictranscoder.<REGION>.amazonaws.com` | Amazon Elastic Transcoder |
| `es.<REGION>.amazonaws.com` | Amazon Elasticsearch Service (ES) |
| `events.<REGION>.amazonaws.com` | Amazon EventBridge |
| `fsx.<REGION>.amazonaws.com` | Amazon FSx |
| `gamelift.<REGION>.amazonaws.com` | Amazon GameLift |
| `glue.<REGION>.amazonaws.com` | AWS Glue |
| `inspector.<REGION>.amazonaws.com` | Amazon Inspector |
| `kafka.<REGION>.amazonaws.com` | Amazon Managed Streaming for Kafka |
| `models.lex.<REGION>.amazonaws.com` | Amazon Lex |
| `logs.<REGION>.amazonaws.com` | Amazon CloudWatch Logs |
| `api.mediatailor.<REGION>.amazonaws.com` | AWS Elemental MediaTailor |
| `mediaconnect.<REGION>.amazonaws.com` | AWS Elemental MediaConnect |
| `mediapackage.<REGION>.amazonaws.com` | AWS Elemental MediaPackage Live |
| `mediapackage-vod.<REGION>.amazonaws.com` | AWS Elemental MediaPackage Video on Demand |
| `opsworks.<REGION>.amazonaws.com` | AWS OpsWorks |
| `qldb.<REGION>.amazonaws.com` | Amazon QLDB |
| `redshift.<REGION>.amazonaws.com` | Amazon Redshift |
| `robomaker.<REGION>.amazonaws.com` | AWS RoboMaker |
| `route53.amazonaws.com` | Amazon Route 53 |
| `route53resolver.<REGION>.amazonaws.com` | Amazon Route 53 Resolver |
| `api.sagemaker.<REGION>.amazonaws.com` | Amazon SageMaker Endpoints, Amazon SageMaker Endpoint Instances |
| `sns.<REGION>.amazonaws.com` | Amazon Simple Notification Service (SNS) |
| `sqs.<REGION>.amazonaws.com` | Amazon Simple Queue Service (SQS) |
| `storagegateway.<REGION>.amazonaws.com` | AWS Storage Gateway |
| `swf.<REGION>.amazonaws.com` | Amazon SWF |
| `transfer.<REGION>.amazonaws.com` | AWS Transfer Family |
| `workmail.<REGION>.amazonaws.com` | Amazon WorkMail |
| `workspaces.<REGION>.amazonaws.com` | Amazon WorkSpaces |

### Регионы AWS, поддерживаемые Dynatrace AWS Monitoring

* `us-gov-west-1`: AWS GovCloud (US)
* `us-gov-east-1`: AWS GovCloud (US-East)
* `us-east-1`: US East (N. Virginia)
* `us-east-2`: US East (Ohio)
* `us-west-1`: US West (N. California)
* `us-west-2`: US West (Oregon)
* `eu-west-1`: EU (Ireland)
* `eu-west-2`: EU (London)
* `eu-west-3`: EU (Paris)
* `eu-central-1`: EU (Frankfurt)
* `eu-central-2`: EU (Zurich)
* `eu-north-1`: EU (Stockholm)
* `eu-south-1`: EU (Milan)
* `eu-south-2`: EU (Spain)
* `ap-east-1`: Asia Pacific (Hong Kong)
* `ap-east-2`: Asia Pacific (Taipei)
* `ap-south-1`: Asia Pacific (Mumbai)
* `ap-south-2`: Asia Pacific (Hyderabad)
* `ap-southeast-1`: Asia Pacific (Singapore)
* `ap-southeast-2`: Asia Pacific (Sydney)
* `ap-southeast-3`: Asia Pacific (Jakarta)
* `ap-southeast-4`: Asia Pacific (Melbourne)
* `ap-southeast-5`: Asia Pacific (Malaysia)
* `ap-southeast-6`: Asia Pacific (New Zealand)
* `ap-southeast-7`: Asia Pacific (Thailand)
* `ap-northeast-1`: Asia Pacific (Tokyo)
* `ap-northeast-2`: Asia Pacific (Seoul)
* `ap-northeast-3`: Asia Pacific (Osaka)
* `sa-east-1`: South America (Sao Paulo)
* `cn-north-1`: China (Beijing)
* `cn-northwest-1`: China (Ningxia)
* `ca-central-1`: Canada (Central)
* `ca-west-1`: Canada West (Calgary)
* `il-central-1`: Israel (Tel Aviv)
* `me-central-1`: Middle East (UAE)
* `me-south-1`: Middle East (Bahrain)
* `mx-central-1`: Mexico (Central)
* `af-south-1`: Africa (Cape Town)
* `us-iso-east-1`: US ISO East
* `us-isob-east-1`: US ISOB East (Ohio)
* `us-iso-west-1`: US ISO West

Прокси

Наиболее частой причиной проблем с сертификатами при использовании TLS-перехватывающего прокси является отсутствие CA-сертификата прокси в хранилище доверенных сертификатов ActiveGate.

Если проблемы с прокси сохраняются, обратитесь к:

* [Прокси для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Настройка свойств ActiveGate для использования прокси.")
* [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Настройка пользовательских доверенных корневых сертификатов на ActiveGate для защищённых SSL/TLS-соединений.")
* [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Настройка SSL-сертификата на ActiveGate.")

«Ошибка связи.»

Убедитесь, что URL-адреса занесены в белый список. В противном случае могут возникнуть ошибки связи или тайм-аута.

3. Политика мониторинга AWS и аутентификация на основе ролей

Для выполнения этих шагов необходимы права администратора AWS.

Политика мониторинга AWS определяет минимальный набор разрешений, которые необходимо предоставить Dynatrace для мониторинга сервисов, работающих в вашей учётной записи AWS. Создайте её один раз и используйте при каждом включении доступа Dynatrace к учётной записи AWS.
Если вы не хотите добавлять разрешения для всех сервисов и хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также список необязательных разрешений, специфичных для каждого сервиса.

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

Для получения информации, необходимой для комплексного мониторинга облачных вычислений AWS, необходимо авторизовать доступ Dynatrace к вашим метрикам Amazon. Dynatrace идентифицирует все виртуализированные компоненты инфраструктуры в вашем окружении AWS и соберёт метрики производительности для этих компонентов.

Далее выберите модель развёртывания, наиболее подходящую для вашего окружения, и следуйте соответствующей процедуре.

#### Развёртывание с существующим ActiveGate

Мониторинг облачных сервисов AWS невозможен без Environment ActiveGate, размещённого в AWS.

Приведённые ниже инструкции применимы независимо от того, совпадает ли учётная запись, в которой размещён ваш ActiveGate, с отслеживаемой учётной записью. В типичной конфигурации требуется создать два стека CloudFormation с использованием шаблонов CloudFormation:

* Стек CloudFormation из учётной записи, в которой размещён ваш ActiveGate, содержащий следующие ресурсы:

  + [Роль для вашего Environment ActiveGate](#create-role-ag), размещённого в инфраструктуре AWS на хосте Amazon EC2.
  + Прикреплённая политика, определяющая разрешения отслеживаемой учётной записи.
* Стек CloudFormation из отслеживаемой учётной записи, содержащий следующие ресурсы:

  + Выделенная [роль мониторинга](#create-role-dt) для Dynatrace в вашей учётной записи AWS.
  + Прикреплённая политика, определяющая разрешения аутентификации Dynatrace для вашего окружения AWS.

Для мониторинга нескольких учётных записей используйте `role_based_access_AG_account_multiple_monitoring_roles_template.yml` и повторите шаги [Создание роли для ActiveGate в учётной записи, где размещён ActiveGate](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#create-role-dt "Интеграция метрик из Amazon CloudWatch.") для создания стека для каждой отслеживаемой учётной записи.

Вам понадобится:

* ActiveGate, установленный на хосте Amazon EC2. Он должен иметь возможность принять роль в вашей учётной записи AWS, позволяющую ему читать данные мониторинга Dynatrace.
* Идентификатор учётной записи AWS, в которой размещён ActiveGate (учётная запись, в которой размещены компоненты Dynatrace, в данном случае это учётная запись, в которой размещён Environment ActiveGate).
* Идентификатор отслеживаемой учётной записи Amazon Web Services (учётная запись, которую требуется мониторить).
* Имя роли, с которой был запущен ваш Environment ActiveGate.
* **External ID**, который можно получить следующим образом.

  1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
  2. Выберите **Connect new instance**.
  3. В разделе **Authentication method** выберите **Role-based authentication**.
  4. В разделе **Token** выберите **Copy**, чтобы скопировать токен (External ID) в буфер обмена.

Создание роли для ActiveGate в учётной записи, где размещён ActiveGate

1. Скачайте [YAML-файл с шаблоном CloudFormation](https://dt-url.net/pv0306t).
2. Создайте стек в Amazon Console:

   1. В Amazon Console перейдите в CloudFormation.
   2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
   3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
   4. В разделе **Parameters** для **Monitored Account ID** введите идентификатор учётной записи, которую будет отслеживать Dynatrace. При необходимости скорректируйте другие параметры.
   5. Введите имя стека и дважды нажмите **Next**.
   6. Проверьте конфигурацию, установите флажок **I acknowledge that AWS CloudFormation might create IAM resources with custom names** и нажмите **Submit**.

Также можно создать стек через CLI с помощью команды ниже:

```
aws cloudformation create-stack \



--capabilities CAPABILITY_NAMED_IAM \



--stack-name <stack_name> \



--template-body <file:///home/user/template_file.yaml> \



--parameters ParameterKey=ActiveGateRoleName,ParameterValue=<role_name> ParameterKey=AssumePolicyName,ParameterValue=<policy_name> ParameterKey=MonitoringRoleName,ParameterValue=<monitoring_role_name> ParameterKey=MonitoredAccountID,ParameterValue=<monitored_account_id>
```

3. Перейдите в консоль Amazon EC2, щёлкните правой кнопкой мыши по экземпляру, где размещён ваш Environment ActiveGate, и выберите **Security** > **Modify IAM role**.
4. Выберите созданную роль и нажмите **Update IAM role**.

Создание роли мониторинга для Dynatrace в отслеживаемой учётной записи

После создания `Dynatrace_ActiveGate_role` в учётной записи, где размещён ActiveGate, создайте роль для отслеживаемой учётной записи.

1. Скачайте YAML-файл с шаблоном CloudFormation из [github role\_based\_access\_AG\_account\_template.yml](https://dt-url.net/f30301j).
2. Создайте стек в Amazon Console:

   1. В Amazon Console перейдите в CloudFormation.
   2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
   3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
   4. В разделе **Parameters** введите **External ID**, **ActiveGateRoleName** и **ActiveGateAccountID** из созданного стека. При необходимости скорректируйте другие параметры.
   5. Введите имя стека и дважды нажмите **Next**.
   6. Проверьте конфигурацию, включите **I acknowledge that AWS CloudFormation might create IAM resources with custom names** и нажмите **Submit**.

Также можно создать стек через CLI с помощью команды ниже:

```
aws cloudformation create-stack \



--capabilities CAPABILITY_NAMED_IAM \



--stack-name <stack_name> \



--template-body <file:///home/user/template_file.yaml> \



--parameters ParameterKey=ExternalID,ParameterValue=<external_id> ParameterKey=ActiveGateRoleName,ParameterValue=<activegate_role_name> ParameterKey=ActiveGateAccountID,ParameterValue=<activegate_account_id>
```

Изменение конфигурации ActiveGate

Начиная с ActiveGate версии 1.217 мониторинг AWS включён по умолчанию. Сведения о конфигурации см. в разделе «Настройка свойств ActiveGate». Следующие параметры конфигурации относятся к более ранним версиям ActiveGate.

1. Отредактируйте файл `custom.properties` вашего Environment ActiveGate.
2. Задайте следующие параметры:

   ```
   [aws_monitoring]



   use_aws_proxy_role = false



   aws_monitoring_enabled = true
   ```

   Если ActiveGate предназначен исключительно для мониторинга AWS, необходимо также установить свойство MSGrouter следующим образом:

   ```
   [collector]



   MSGrouter = false
   ```
3. Сохраните файл и перезапустите основной сервис ActiveGate.

Аутентификация на основе ключей (только для AWS GovCloud и AWS China)

Аутентификация на основе ключей разрешена только для разделов AWS GovCloud и China.

В этом сценарии необходимо создать политику мониторинга AWS и сгенерировать пару ключей с этой политикой.

Границы разрешений AWS Identity and Access Management (IAM) могут запрещать действия AWS, необходимые Dynatrace. Если в вашей учётной записи AWS используется граница разрешений IAM, убедитесь, что действия из политики разрешены во всех регионах AWS в пределах этой границы.

Создание политики мониторинга AWS

1. В Amazon Console перейдите в **Identity and Access Management**.
2. Перейдите в **Policies** и нажмите **Create policy**.
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

Необходимо сгенерировать **Access key** и **Secret access key**, которые Dynatrace будет использовать для получения метрик из Amazon Web Services.

6. В Amazon Console перейдите в **Users** и нажмите **Add Users**.
7. Введите **User name**.
8. На следующем экране выберите **Attach policies directly** и прикрепите созданную ранее политику.
9. Проверьте сведения о пользователе и нажмите **Create user**.
10. В списке пользователей выберите только что созданного пользователя и перейдите в **Security credentials**, затем нажмите **Create access key**.
11. В разделе **Access key best practices & alternatives** выберите **Third-party service**, затем нажмите **Next**.
12. В разделе **Retrieve access keys** сохраните значения **Access Key ID** (AKID) и **Secret access key**.
13. Можно скачать учётные данные пользователя или скопировать их, отображаемые онлайн (нажмите **Show**).

Альтернатива: создание ролей AWS с помощью Terraform

Шаблоны Terraform, это альтернативный способ создания и настройки ролей AWS. Подробные инструкции по созданию ролей AWS с помощью Terraform см. в [Настройке доступа на основе ролей AWS с помощью Terraform](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws/role-based-access/terraform-templates)

## Создание конфигурации мониторинга

Можно создавать, активировать и управлять несколькими подключениями мониторинга. Каждое подключение определяется учётными данными и/или токенами доступа, необходимыми Dynatrace для получения данных.

Почему конфигурация выполняется для каждого подключения

Поддержка нескольких подключений и конфигураций позволяет отслеживать даже сложные окружения. При таком подходе не нужно настраивать всё сразу: можно постепенно добавлять конфигурации мониторинга к существующей настройке. Такая архитектура также упрощает реагирование на динамические изменения отслеживаемого окружения без необходимости перенастройки незатронутых элементов.

1. Добавление нового подключения AWS

Если вы выполнили все предыдущие шаги, можно переходить к настройке мониторинга Amazon Web Services.

Добавление нового подключения AWS

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**. На странице перечислены уже настроенные подключения AWS.

   Если вы не предоставили ActiveGate, необходимый для мониторинга AWS (см. [Предварительные требования](#capable-activegate)), соответствующее сообщение отобразится на экране и продолжить настройку будет невозможно.

   1. Изменение или удаление существующих подключений

   Изменять уже настроенные подключения можно в любой момент.

   1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**. На странице перечислены существующие подключения.
   2. Отредактируйте подключения по необходимости.

      * Чтобы изменить существующее подключение или отслеживаемые в нём сервисы, нажмите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Изменить") в соответствующей строке.
      * Чтобы удалить существующее подключение, нажмите **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Удалить") в соответствующей строке.
2. Выберите **Connect new instance** и заполните следующие поля.

   * Переключатель **Enabled**: убедитесь, что он включён, если требуется отслеживать эту конфигурацию.
   * **Connection name**: введите описательное имя подключения.
   * **Authentication method**: выберите `Role-based authentication`.
   * **IAM role...**: введите имя роли, созданной в Amazon для Dynatrace (`Dynatrace_monitoring_role` или пользовательское имя роли, если оно было задано). Используйте роль, содержащую [все необходимые разрешения](#aws-policy-and-authentication).
   * **Your Amazon account ID**: введите идентификатор учётной записи Amazon (учётная запись, из которой Dynatrace будет получать метрики).
3. Нажмите **Connect** для проверки и сохранения подключения.

   Выбор другого раздела AWS

   Если ваша учётная запись AWS находится в другом разделе, отличном от раздела AWS по умолчанию, используйте список **AWS partition** для выбора раздела.

   Ограничение сбора данных

   Можно ограничить данные, получаемые из CloudWatch, задав фильтр на основе тегов для определённых ресурсов. Подробнее о фильтрации на основе тегов см. в разделе [Ограничение вызовов API к AWS с помощью тегов](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags#configure-dynatrace-to-use-aws-tags "Добавление и настройка тегов AWS для ограничения ресурсов AWS.").

2. Облачные сервисы AWS, отслеживаемые по умолчанию

После подключения Dynatrace к окружению AWS начинается немедленный мониторинг [выбранных сервисов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#aws-default "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."). Список метрик облачных сервисов AWS, отслеживаемых по умолчанию, см. в разделе [Классические (ранее «встроенные») метрики AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/default-aws-metrics "Список классических (ранее «встроенных») метрик, которые Dynatrace собирает по умолчанию для мониторинга AWS.").

3. Мониторинг других сервисов AWS

Помимо сервисов AWS, можно также отслеживать все остальные облачные сервисы AWS. Облачные сервисы AWS включаются для мониторинга для каждого подключения AWS.

Добавление сервиса в мониторинг:

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS найдите подключение, которое требуется изменить, и нажмите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Изменить") в соответствующей строке.
3. В разделе **Services** выберите **Manage services**.
4. Нажмите **Add service**.
5. Выберите сервис из списка и нажмите **Add service**.
6. Нажмите **Save changes** для сохранения конфигурации.

Можно добавить несколько облачных сервисов, повторив указанные шаги.

Настройка собираемых метрик для каждого сервиса

После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для этого сервиса.

Рекомендуемые метрики:

* Включены по умолчанию
* Нельзя отключить
* Могут иметь рекомендуемые измерения (включены по умолчанию, нельзя отключить)
* Могут иметь необязательные измерения (отключены по умолчанию, можно включить)

Помимо рекомендуемых метрик, большинство сервисов поддерживают возможность включения необязательных метрик, которые можно добавлять и настраивать вручную.

Список облачных сервисов AWS и собираемых метрик

Полный список облачных сервисов AWS и сведения о метриках, собираемых для каждого из них, см. в разделе [Все облачные сервисы AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.").

Также можно ознакомиться со списком поддерживаемых сервисов AWS в Dynatrace Hub внутри продукта (выполните поиск по **AWS**) или в [веб-версии Dynatrace Hub](https://www.dynatrace.com/hub/?query=aws).

Добавление и настройка метрик

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS найдите подключение, которое требуется изменить, и нажмите значок редактирования рядом с его именем.
3. Перейдите в **Services** и выберите **Manage services**.
4. Чтобы добавить метрику, выберите сервис, для которого нужно добавить метрики, и нажмите **Add new metric**.
5. В меню выберите **Add metric** для метрики, которую требуется отслеживать.
6. Нажмите **Edit** для настройки метрики.
7. Нажмите **Apply** для сохранения конфигурации.

После выбора облачных сервисов и сохранения изменений мониторинг новых сервисов запускается автоматически.

## Что дальше?

В течение нескольких минут данные появятся на ваших панелях мониторинга.

Просмотр основных измерений для каждого из подключений AWS

1. Перейдите в **AWS**.
2. Выберите подключение, для которого требуется просмотреть обзор инфраструктуры AWS.

Также можно создать собственную панель мониторинга из метрик, собранных для ваших экземпляров AWS. Подробнее о создании панелей мониторинга см. в разделе [Панели мониторинга](/managed/analyze-explore-automate/dashboards-classic "Создание, управление и использование классических панелей мониторинга Dynatrace.").

Виртуальные машины, контейнеры и глубокий мониторинг кода с помощью Dynatrace OneAgent

Dynatrace OneAgent обеспечивает непревзойдённую глубину анализа хостов, контейнеров и кода. Подробнее см. в разделе [Настройка Dynatrace для Amazon Web Services](/managed/ingest-from/amazon-web-services "Настройка и конфигурация мониторинга для Amazon Web Services.").

Дальнейшая настройка уведомлений и оповещений

После настройки мониторинга AWS можно:

* [Настроить события метрик для оповещения](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-set-up-metric-events-for-alerting "Настройка и конфигурация событий метрик для оповещения."). Это позволяет создавать, включать, отключать и настраивать рекомендуемые правила оповещений.
* [Ограничить вызовы API к AWS с помощью тегов](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавление и настройка тегов AWS для ограничения ресурсов AWS."). По умолчанию Dynatrace отслеживает все Amazon Web Services, указанные в вашей политике разрешений. При необходимости можно использовать теги для ограничения ресурсов AWS, отслеживаемых Dynatrace.

Интеграция CloudWatch Metric Streams

Этот метод мониторинга не требует ActiveGate. Интеграция Dynatrace с Amazon CloudWatch Metric Streams обеспечивает простой и безопасный способ приёма метрик AWS. Amazon CloudWatch Metric Streams позволяет передавать все метрики в заданном регионе AWS через Kinesis Firehose в Dynatrace API. Подробнее см. в разделе [Amazon CloudWatch Metric Streams](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams "Приём метрик из учётных записей AWS с помощью Amazon CloudWatch Metric Streams.").

OpenTelemetry и распределённая трассировка

Также можно [трассировать функции AWS Lambda .NET Core с помощью OpenTelemetry .NET](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Использование OpenTelemetry для трассировки функций AWS Lambda .NET Core.").