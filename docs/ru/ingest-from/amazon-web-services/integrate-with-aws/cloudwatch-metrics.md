---
title: Мониторинг Amazon Web Services с метриками CloudWatch
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics
scraped: 2026-03-06T21:32:27.989679
---

* 23 минуты чтения

Следуйте этому руководству, чтобы начать удалённый приём данных из Amazon CloudWatch.

Основное внимание уделяется мониторингу инфраструктуры сервисов AWS: Dynatrace осуществляет мониторинг сервисов AWS через CloudWatch.

Информацию о мониторинге полного стека и журналов для ваших сервисов AWS см. в разделе [Что дальше?](#next).

После установки первоначального мониторинга вы можете добавлять, удалять или изменять мониторинг сервисов с помощью веб-интерфейса Dynatrace, в масштабе или через Dynatrace API.

Подробности о собираемых метриках

Для ознакомления с метриками, собираемыми для каждого из сервисов AWS, см.:

* Сервисы AWS с включённым мониторингом по умолчанию и их метрики метрик, которые Dynatrace собирает по умолчанию для мониторинга AWS.")
* Облачные сервисы AWS

Мониторинг инфраструктуры Amazon Web Services предоставляет метрики из CloudWatch, данные об инфраструктуре, доступные через публичный AWS API, и конкретные события. Данные собираются с пятиминутными интервалами.

## Стоимость мониторинга

* Каждый сервис, отслеживаемый Dynatrace через CloudWatch, а также обработка и анализ журналов потребляют DDU.").
* Amazon может взимать дополнительную плату за запросы метрик CloudWatch. Подробности о дополнительных расходах см. в [онлайн-документации по ценообразованию Amazon CloudWatch](https://aws.amazon.com/cloudwatch/pricing/).

## Предварительные требования для мониторинга

Для настройки мониторинга AWS необходимо выполнить три предварительных условия:

1. Права администратора Dynatrace

Для управления конфигурацией мониторинга AWS необходимы права на чтение и изменение схемы `builtin:cloud.aws`.

* Требуются как `settings:objects:read`, так и `settings:objects:write`.
* Они входят в разрешения **Change monitoring settings**.
* Доступ только для чтения не поддерживается.

Подробности об управлении и настройке разрешений см. в разделе Управление разрешениями пользователей с помощью ролей.

2. Разрешение ActiveGate на доступ к URL

Для мониторинга Amazon Web Services Dynatrace должен иметь возможность подключаться к API Amazon CloudWatch и периодически запрашивать его. По крайней мере один ActiveGate должен иметь возможность подключаться к Amazon CloudWatch для выполнения задач мониторинга. ActiveGate должен быть развёрнут на экземпляре EC2 и иметь возможность подключаться к конечным точкам, перечисленным ниже.

Начиная с версии Dynatrace 1.267+, может использоваться только доступ на основе ролей. Аутентификация на основе ключей больше недоступна для новых учётных данных. Для существующих учётных данных на основе ключей вы можете продолжать использовать ключи бессрочно. Мы рекомендуем перейти на аутентификацию на основе ролей с помощью специальной кнопки на странице конфигурации. Dynatrace автоматически проверяет конфигурацию для обеспечения правильной настройки ролей.

[Аутентификация на основе ключей](#key-based-authentication) разрешена только для разделов AWS GovCloud и China.

ActiveGate, способный осуществлять мониторинг вашей учётной записи AWS для классических (встроенных) поддерживаемых сервисов, уже предоставлен и доступен в учётной записи Dynatrace AWS (только для сред SaaS, размещённых в AWS).

Однако для мониторинга конкретных нестандартных облачных сервисов AWS или если ваша учётная запись AWS превышает 2000 ресурсов AWS, необходимо установить и настроить Environment ActiveGate. Следуйте руководству по установке ActiveGate и продолжите выполнение этого руководства после завершения.

Необходимо установить и настроить Environment ActiveGate, если вы хотите отслеживать одно из следующего или оба:

* Более 2000 ресурсов AWS (экземпляров сервисов AWS)
* [Нестандартные облачные сервисы AWS](aws-all-services.md#aws-non-default "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.")

#### Разрешение ActiveGate на доступ к URL AWS

Интеграция обращается к следующим конечным точкам AWS API, поэтому они должны быть доступны из вашего ActiveGate:

* AWS Security Token Service (AWS STS)

Environment ActiveGate версии 1.329+

```
https://sts.<REGION>.amazonaws.com/
```

Environment ActiveGate версии 1.328 и ниже

```
https://sts.amazonaws.com/
```

Начиная с версии Dynatrace 1.329, глобальная конечная точка AWS STS не поддерживается. Убедитесь, что `sts.<REGION>.amazonaws.com` доступен для регионов, которые вы хотите отслеживать.

Регион `us-west-2` теперь является регионом по умолчанию для ActiveGate. В случае проблем с подключением убедитесь, что конечная точка `sts.us-west-2.amazonaws.com` включена.

Подробности см. в [региональных конечных точках AWS STS](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html).

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

Другие конечные точки могут потребоваться в зависимости от сервисов, которые вам необходимо отслеживать.

Для получения конечных точек, специфичных для каждого сервиса, который вы хотите отслеживать, а также регионов AWS, поддерживаемых Dynatrace AWS Monitoring, обратитесь к таблицам ниже.

### Конечные точки AWS, которые должны быть доступны из ActiveGate, с соответствующими сервисами AWS

| Конечная точка | Сервис |
| --- | --- |
| `autoscaling.<REGION>.amazonaws.com` | Amazon EC2 Auto Scaling (встроенный), Amazon EC2 Auto Scaling |
| `lambda.<REGION>.amazonaws.com` | AWS Lambda (встроенный), AWS Lambda |
| `elasticloadbalancing.<REGION>.amazonaws.com` | Amazon Application and Network Load Balancer (встроенный), Amazon Elastic Load Balancer (ELB) (встроенный) |
| `dynamodb.<REGION>.amazonaws.com` | Amazon DynamoDB (встроенный), Amazon DynamoDB |
| `ec2.<REGION>.amazonaws.com` | Amazon EBS (встроенный), Amazon EC2 (встроенный), Amazon EBS, Amazon EC2 Spot Fleet, Amazon VPC NAT Gateways, AWS Transit Gateway, AWS Site-to-Site VPN |
| `rds.<REGION>.amazonaws.com` | Amazon RDS (встроенный), Amazon Aurora, Amazon DocumentDB, Amazon Neptune, Amazon RDS |
| `s3.<REGION>.amazonaws.com` | Amazon S3 (встроенный) |
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

Наиболее частой причиной проблем с сертификатами при использовании прокси с перехватом TLS является отсутствие CA-сертификата прокси в хранилище доверия ActiveGate.

Если проблемы с прокси сохраняются, см.:

* Прокси для ActiveGate
* Доверенные корневые сертификаты для ActiveGate
* Пользовательский SSL-сертификат для ActiveGate

«Ошибка связи.»

Убедитесь, что URL-адреса занесены в белый список. В противном случае могут возникать ошибки связи или истечения времени ожидания.

3. Политика мониторинга AWS и аутентификация на основе ролей

Для выполнения этих шагов необходимы права администратора AWS.

Политика мониторинга AWS определяет минимальный набор разрешений, который необходимо предоставить Dynatrace для мониторинга сервисов, работающих в вашей учётной записи AWS. Создайте её один раз и используйте каждый раз при предоставлении Dynatrace доступа к вашей учётной записи AWS.
Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для всех облачных сервисов AWS, а также список дополнительных разрешений, специфичных для каждого сервиса.

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
| Все отслеживаемые сервисы Amazon Обязательно | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
| AWS Certificate Manager Private Certificate Authority | `acm-pca:ListCertificateAuthorities` |
| Amazon MQ |  |
| Amazon API Gateway | `apigateway:GET` |
| AWS App Runner | `apprunner:ListServices` |
| Amazon AppStream | `appstream:DescribeFleets` |
| AWS AppSync | `appsync:ListGraphqlApis` |
| Amazon Athena | `athena:ListWorkGroups` |
| Amazon Aurora | `rds:DescribeDBClusters` |
| Amazon EC2 Auto Scaling | `autoscaling:DescribeAutoScalingGroups` |
| Amazon EC2 Auto Scaling (встроенный) | `autoscaling:DescribeAutoScalingGroups` |
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
| Amazon DynamoDB (встроенный) | `dynamodb:ListTables`, `dynamodb:ListTagsOfResource` |
| Amazon EBS | `ec2:DescribeVolumes` |
| Amazon EBS (встроенный) | `ec2:DescribeVolumes` |
| Amazon EC2 API |  |
| Amazon EC2 (встроенный) | `ec2:DescribeInstances` |
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
| Amazon Elastic Load Balancer (ELB) (встроенный) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
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
| AWS Lambda (встроенный) | `lambda:ListFunctions`, `lambda:ListTags` |
| Amazon Lex | `lex:GetBots` |
| Amazon Application and Network Load Balancer (встроенный) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
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
| Amazon RDS (встроенный) | `rds:DescribeDBInstances`, `rds:DescribeEvents`, `rds:ListTagsForResource` |
| Amazon Redshift | `redshift:DescribeClusters` |
| Amazon Rekognition |  |
| AWS RoboMaker | `robomaker:ListSimulationJobs` |
| Amazon Route 53 | `route53:ListHostedZones` |
| Amazon Route 53 Resolver | `route53resolver:ListResolverEndpoints` |
| Amazon S3 | `s3:ListAllMyBuckets` |
| Amazon S3 (встроенный) | `s3:ListAllMyBuckets` |
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

Для получения информации, необходимой для комплексного мониторинга облачных вычислений AWS, необходимо авторизовать Dynatrace для доступа к вашим метрикам Amazon. Dynatrace определит все виртуализированные компоненты инфраструктуры в вашей среде AWS и соберёт метрики производительности, связанные с этими компонентами.

Далее выберите модель развёртывания, наилучшим образом описывающую вашу среду, и следуйте соответствующей процедуре.

Развёртывание без ActiveGate

Развёртывание с существующим ActiveGate

Dynatrace SaaS требует доступа к вашей учётной записи AWS на основе ролей.

Без Environment ActiveGate, размещённого в AWS, мониторинг нестандартных облачных сервисов AWS будет недоступен.

Вам понадобятся:

* Идентификатор учётной записи AWS
* Права на назначение ролевого доступа к вашей учётной записи AWS
* **External ID**, который можно получить следующим образом.

  1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
  2. Нажмите **Connect new Instance**.
  3. В разделе **Authentication method** выберите **Role-based authentication**.
  4. В разделе **Your Amazon account ID** нажмите **Copy** для копирования токена (External ID).

Для создания доступа на основе ролей

1. Загрузите файл YAML с шаблоном CloudFormation из [cloud-snippets/role\_based\_access\_no\_AG\_template.yml](https://dt-url.net/8b23yuo).
2. Создайте стек в вашей консоли Amazon:

   1. В консоли Amazon перейдите в CloudFormation.
   2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
   3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
   4. В разделе **Parameters** введите **External ID**.
   5. Введите имя для вашего стека и дважды нажмите **Next**.
   6. Проверьте конфигурацию и примите условия политики.
   7. Нажмите **Create stack**.

   Альтернатива: создание стека через CLI

   Для создания стека с помощью CLI выполните команду ниже, заменив значения параметров своими фактическими значениями.

   Также необходимо удалить угловые скобки (`<` и `>`).

   ```
   aws cloudformation create-stack \


   --capabilities CAPABILITY_NAMED_IAM \


   --stack-name <stack_name> \


   --template-body <file:///home/user/template_file.yaml> \


   --parameters ParameterKey=ExternalID,ParameterValue=<external_id> ParameterKey=RoleName,ParameterValue=<role_name> ParameterKey=PolicyName,ParameterValue=<policy_name>
   ```

Приведённые ниже инструкции применимы независимо от того, совпадает ли учётная запись, в которой размещён ваш ActiveGate, с отслеживаемой учётной записью. В типичной установке необходимо создать два стека CloudFormation с использованием шаблонов CloudFormation:

* Стек CloudFormation из учётной записи, в которой размещён ваш ActiveGate, содержащий следующие ресурсы:

  + [Роль для вашего Environment ActiveGate](#create-role-ag), размещённого в вашей инфраструктуре AWS, на хосте Amazon EC2.
  + Прикреплённая политика, определяющая разрешения отслеживаемой учётной записи.
* Стек CloudFormation из отслеживаемой учётной записи, содержащий следующие ресурсы:

  + Специальная [роль мониторинга](#create-role-dt) для Dynatrace в вашей учётной записи AWS.
  + Прикреплённая политика, определяющая разрешения аутентификации Dynatrace в вашей среде AWS.

Для мониторинга нескольких учётных записей используйте `role_based_access_AG_account_multiple_monitoring_roles_template.yml` и повторяйте шаги [Создание роли для ActiveGate в учётной записи, в которой размещён ActiveGate](cloudwatch-metrics.md#create-role-dt "Интеграция метрик из Amazon CloudWatch.") для каждой отслеживаемой учётной записи.

Вам понадобятся:

* ActiveGate, установленный на хосте Amazon EC2. Он должен иметь возможность принимать роль в вашей учётной записи AWS, позволяющую ему читать данные мониторинга Dynatrace.
* Идентификатор учётной записи AWS, в которой размещён ActiveGate (учётная запись, в которой размещены ваши компоненты Dynatrace, в данном случае — та, в которой размещён Environment ActiveGate).
* Идентификатор отслеживаемой учётной записи Amazon Web Services (учётная запись, которую вы хотите отслеживать).
* Имя роли, с которой был запущен ваш Environment ActiveGate.
* **External ID**, который можно получить следующим образом.

  1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
  2. Нажмите **Connect new instance**.
  3. В разделе **Authentication method** выберите **Role-based authentication**.
  4. В разделе **Token** нажмите **Copy** для копирования токена (External ID) в буфер обмена.

Создание роли для ActiveGate в учётной записи, в которой размещён ActiveGate

1. Загрузите [role\_based\_access\_AG\_account\_template.yml](https://dt-url.net/pv0306t).
2. Создайте стек в вашей консоли Amazon:

   1. В консоли Amazon перейдите в CloudFormation.
   2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
   3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
   4. В разделе **Parameters** для **Monitored Account ID** введите идентификатор учётной записи, которую Dynatrace будет отслеживать. При необходимости скорректируйте другие параметры.
   5. Введите имя для вашего стека, затем дважды нажмите **Next**.
   6. Проверьте конфигурацию, установите флажок **I acknowledge that AWS CloudFormation might create IAM resources with custom names** и нажмите **Submit**.

Также можно создать стек через CLI с помощью команды ниже:

```
aws cloudformation create-stack \


--capabilities CAPABILITY_NAMED_IAM \


--stack-name <stack_name> \


--template-body <file:///home/user/template_file.yaml> \


--parameters ParameterKey=ActiveGateRoleName,ParameterValue=<role_name> ParameterKey=AssumePolicyName,ParameterValue=<policy_name> ParameterKey=MonitoringRoleName,ParameterValue=<monitoring_role_name> ParameterKey=MonitoredAccountID,ParameterValue=<monitored_account_id>
```

3. Перейдите в консоль Amazon EC2, щёлкните правой кнопкой мыши на экземпляре с вашим Environment ActiveGate и выберите **Security** > **Modify IAM role**.
4. Выберите созданную роль и нажмите **Update IAM role**.

Создание роли мониторинга для Dynatrace в отслеживаемой учётной записи

После создания `Dynatrace_ActiveGate_role` в учётной записи, в которой размещён ActiveGate, создайте роль для отслеживаемой учётной записи.

1. Загрузите файл YAML с шаблоном CloudFormation из [role\_based\_access\_monitored\_account\_template.yml](https://dt-url.net/f30301j).
2. Создайте стек в вашей консоли Amazon:

   1. В консоли Amazon перейдите в CloudFormation.
   2. Перейдите в **Stacks** и создайте новый стек с новыми ресурсами.
   3. Выберите **Template is ready**, загрузите созданный выше шаблон и нажмите **Next**.
   4. В разделе **Parameters** введите **External ID**, **ActiveGateRoleName** и **ActiveGateAccountID** из созданного вами стека. При необходимости скорректируйте другие параметры.
   5. Введите имя для вашего стека, затем дважды нажмите **Next**.
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

Начиная с ActiveGate версии 1.217, мониторинг AWS включён по умолчанию. Подробности конфигурации см. в разделе «Настройка свойств ActiveGate». Следующие параметры конфигурации относятся к более ранним версиям ActiveGate.

1. Отредактируйте файл `custom.properties` вашего Environment ActiveGate.
2. Задайте следующие параметры:

   ```
   [aws_monitoring]


   use_aws_proxy_role = false


   aws_monitoring_enabled = true
   ```

   Если ActiveGate предназначен исключительно для мониторинга AWS, также необходимо задать свойство MSGrouter следующим образом:

   ```
   [collector]


   MSGrouter = false
   ```
3. Сохраните файл и перезапустите основной сервис ActiveGate.

Аутентификация на основе ключей (только для AWS GovCloud и AWS China)

Аутентификация на основе ключей разрешена только для разделов AWS GovCloud и China.

В этом сценарии необходимо создать политику мониторинга AWS и сгенерировать пару ключей с этой политикой.

Граничные условия разрешений AWS Identity and Access Management (IAM) могут запрещать действия AWS, необходимые для Dynatrace. Если вы используете граничные условия разрешений IAM в своей учётной записи AWS, убедитесь, что действия из политики разрешены во всех регионах AWS в рамках граничных условий разрешений.

Для создания политики мониторинга AWS

1. В консоли Amazon перейдите в **Identity and Access Management**.
2. Перейдите в **Policies** и нажмите **Create policy**.
3. Выберите вкладку JSON и вставьте предустановленную политику из блока ниже.

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

Вам необходимо сгенерировать **Access key** и **Secret access key**, которые Dynatrace сможет использовать для получения метрик из Amazon Web Services.

6. В консоли Amazon перейдите в **Users** и нажмите **Add Users**.
7. Введите **User name**.
8. На следующем экране выберите **Attach policies directly** и прикрепите созданную ранее политику.
9. Проверьте данные пользователя и нажмите **Create user**.
10. В списке пользователей выберите имя только что созданного пользователя и перейдите в **Security credentials**, затем нажмите **Create access key**.
11. В разделе **Access key best practices & alternatives** выберите **Third-party service**, затем нажмите **Next**.
12. В разделе **Retrieve access keys** сохраните значения **Access Key ID** (AKID) и **Secret access key**.
13. Вы можете либо скачать учётные данные пользователя, либо скопировать учётные данные, отображаемые онлайн (нажмите **Show**).

Альтернатива: создание ролей AWS с помощью Terraform

Шаблоны Terraform — это альтернативный способ создания и настройки ролей AWS. Подробные инструкции по созданию ролей AWS с помощью Terraform см. в [настройке доступа AWS на основе ролей с помощью Terraform](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws/role-based-access/terraform-templates)

## Создание конфигурации мониторинга

Вы можете создавать, активировать и управлять несколькими подключениями мониторинга. Каждое подключение определяется учётными данными и/или токенами доступа, необходимыми Dynatrace для получения данных.

Почему конфигурация выполняется на уровне подключения

Поддержка нескольких подключений и конфигураций позволяет отслеживать даже крайне сложные среды. При таком подходе не нужно настраивать всё сразу. Вместо этого можно постепенно добавлять конфигурации мониторинга к существующей установке. Такая архитектура также упрощает реагирование на динамические изменения в отслеживаемой среде без необходимости перенастраивать незатронутые элементы.

1. Добавление нового подключения AWS

Если вы выполнили все предыдущие шаги, вы готовы к настройке мониторинга Amazon Web Services.

Для добавления нового подключения AWS

1. Откройте раздел ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
2. Выберите вкладку **Integration manager**.
3. Узнайте, как перемещаться и подключить новый экземпляр через [Integration manager](../../../observe/infrastructure-observability/cloud-platform-monitoring/clouds-app.md#integration-manager "Мониторинг всех облачных платформ одновременно.").

2. Облачные сервисы AWS, отслеживаемые по умолчанию

После подключения Dynatrace к вашей среде AWS он немедленно начинает отслеживать [выбранные сервисы AWS](aws-all-services.md#aws-default "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."). В разделе Классические (ранее «встроенные») метрики AWS метрик, которые Dynatrace собирает по умолчанию для мониторинга AWS.") перечислены метрики облачных сервисов AWS, отслеживаемых по умолчанию.

3. Мониторинг других сервисов AWS

Помимо стандартных сервисов AWS, можно также отслеживать все остальные облачные сервисы AWS. Облачные сервисы AWS включаются для мониторинга на уровне подключения AWS.

Для добавления сервиса в мониторинг:

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS найдите нужное подключение и нажмите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в этой строке.
3. В разделе **Services** нажмите **Manage services**.
4. Нажмите **Add service**.
5. Выберите сервис из списка и нажмите **Add service**.
6. Нажмите **Save changes** для сохранения конфигурации.

Вы можете добавить несколько облачных сервисов, повторив шаги выше.

Конфигурация собираемых метрик для каждого сервиса

После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для этого конкретного сервиса.

Рекомендуемые метрики:

* Включены по умолчанию
* Не могут быть отключены
* Могут поставляться с рекомендуемыми измерениями (включены по умолчанию, не могут быть отключены)
* Могут поставляться с необязательными измерениями (отключены по умолчанию, могут быть включены)

Помимо рекомендуемых метрик, для большинства сервисов есть возможность включить дополнительные необязательные метрики, которые можно добавить и настроить вручную.

Список облачных сервисов AWS и собираемых метрик

Полный список облачных сервисов AWS и метрик, собираемых для каждого из них, см. в разделе Все облачные сервисы AWS.

Также можно просмотреть список поддерживаемых сервисов AWS в Dynatrace Hub прямо в продукте (поиск **AWS**) или в [веб-версии Dynatrace Hub](https://www.dynatrace.com/hub/?query=aws).

Для добавления и настройки метрик

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS найдите нужное подключение и нажмите значок редактирования рядом с его именем.
3. Перейдите в **Services** и нажмите **Manage services**.
4. Для добавления метрики выберите сервис, для которого вы хотите добавить метрики, и нажмите **Add new metric**.
5. В меню нажмите **Add metric** для метрики, которую вы хотите отслеживать.
6. Нажмите **Edit** для настройки метрики.
7. Нажмите **Apply** для сохранения конфигурации.

После выбора облачных сервисов и сохранения изменений мониторинг вновь добавленных сервисов запускается автоматически.

## Что дальше?

В течение нескольких минут вы увидите данные на своих дашбордах.

Для просмотра основных метрик по каждому из подключений AWS

1. Перейдите в раздел ![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS") **AWS Classic**.
2. Выберите подключение, для которого хотите просмотреть обзор инфраструктуры AWS.

Вы также можете создать собственный дашборд на основе метрик, собранных для ваших экземпляров AWS. Подробности о создании дашбордов см. в разделе Dashboards Classic.

Виртуальные машины, контейнеры и глубокий мониторинг кода с Dynatrace OneAgent

Dynatrace OneAgent предлагает непревзойдённую глубину анализа хостов, контейнеров и кода. Подробности см. в разделе Настройка Dynatrace на Amazon Web Services.

Дополнительная настройка уведомлений и оповещений

После настройки мониторинга AWS вы можете:

* Настроить события метрик для оповещений. Это позволяет создавать, включать, отключать и настраивать рекомендуемые правила оповещений.
* Ограничить вызовы API к AWS с помощью тегов. По умолчанию Dynatrace отслеживает все сервисы Amazon Web Services, указанные в вашей политике разрешений. Дополнительно можно использовать теги для ограничения ресурсов AWS, отслеживаемых Dynatrace.

Интеграция CloudWatch Metric Streams

Этот метод мониторинга не требует ActiveGate. Интеграция Dynatrace с Amazon CloudWatch Metric Streams обеспечивает простой и безопасный способ приёма метрик AWS. Amazon CloudWatch Metric Streams позволяет передавать все метрики, формируемые в заданном регионе AWS, через Kinesis Firehose в Dynatrace API. Подробности см. в разделе Amazon CloudWatch Metric Streams.

OpenTelemetry и распределённая трассировка

Также возможна трассировка функций AWS Lambda .NET Core с помощью OpenTelemetry .NET.
