---
title: Amazon GameLift monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-gamelift
scraped: 2026-02-19T21:30:21.215502
---

# Amazon GameLift monitoring

# Amazon GameLift monitoring

* How-to guide
* 10-min read
* Published Jul 06, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon GameLift. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

To enable monitoring for this service, you need

* ActiveGate version 1.197+

  + For Dynatrace SaaS deployments, you need an Environment ActiveGate or a Multi-environment ActiveGate.
  + For Dynatrace Managed deployments, you can use any kind of ActiveGate.

    For role-based access (whether in a [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") or [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) deployment), you need an [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") installed on an Amazon EC2 host.
* Dynatrace version 1.203+
* An updated [AWS monitoring policy](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Integrate metrics from Amazon CloudWatch.") to include the additional AWS services.  
  To [update the AWS IAM policyï»¿](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), use the JSON below, containing the monitoring policy (permissions) for all supporting services.

JSON predefined policy for all supporting services

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

If you don't want to add permissions to all services, and just select permissions for certain services, consult the table below. The table contains a set of permissions that are required for [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.") and, for each supporting service, a list of optional permissions specific to that service.

Permissions required for AWS monitoring integration:

* `"cloudwatch:GetMetricData"`
* `"cloudwatch:GetMetricStatistics"`
* `"cloudwatch:ListMetrics"`
* `"sts:GetCallerIdentity"`
* `"tag:GetResources"`
* `"tag:GetTagKeys"`
* `"ec2:DescribeAvailabilityZones"`

### Complete list of permissions for cloud services



| Name | Permissions |
| --- | --- |
| All monitored Amazon services Required | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
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

See the example of JSON policy for one single service below.

JSON policy for Amazon API Gateway

```
{



"Version": "2012-10-17",



"Statement": [



{



"Sid": "VisualEditor0",



"Effect": "Allow",



"Action": [



"apigateway:GET",



"cloudwatch:GetMetricData",



"cloudwatch:GetMetricStatistics",



"cloudwatch:ListMetrics",



"sts:GetCallerIdentity",



"tag:GetResources",



"tag:GetTagKeys",



"ec2:DescribeAvailabilityZones"



],



"Resource": "*"



}



]



}
```

In this example, from the complete list of permissions you need to select

* `"apigateway:GET"` for **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"`, and `"ec2:DescribeAvailabilityZones"` for **All AWS cloud services**.

### AWS endpoints that need to be reachable from ActiveGate with corresponding AWS services



| Endpoint | Service |
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

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring "Enable AWS monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

After you add the service to monitoring, a preset dashboard containing all recommended metrics is automatically listed on your **Dashboards** page. To look for specific dashboards, filter by **Preset** and then by **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **AWS**, select the desired AWS instance, and then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.

To remove a dashboard from the dashboards page, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

To check the availability of preset dashboards for each AWS service, see the list below.

### Preset dashboard availability list



| AWS service | Preset dashboard |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | Not applicable |
| AWS Lambda (built-in) | Not applicable |
| Amazon Application and Network Load Balancer (built-in) | Not applicable |
| Amazon DynamoDB (built-in) | Not applicable |
| Amazon EBS (built-in) | Not applicable |
| Amazon EC2 (built-in) | Not applicable |
| Amazon Elastic Load Balancer (ELB) (built-in) | Not applicable |
| Amazon RDS (built-in) | Not applicable |
| Amazon S3 (built-in) | Not applicable |
| AWS Certificate Manager Private Certificate Authority | Not applicable |
| All monitored Amazon services | Not applicable |
| Amazon API Gateway | Not applicable |
| AWS App Runner | Not applicable |
| Amazon AppStream | Applicable |
| AWS AppSync | Applicable |
| Amazon Athena | Applicable |
| Amazon Aurora | Not applicable |
| Amazon EC2 Auto Scaling | Applicable |
| AWS Billing | Applicable |
| Amazon Keyspaces | Applicable |
| AWS Chatbot | Applicable |
| Amazon CloudFront | Not applicable |
| AWS CloudHSM | Applicable |
| Amazon CloudSearch | Applicable |
| AWS CodeBuild | Applicable |
| Amazon Cognito | Not applicable |
| Amazon Connect | Applicable |
| AWS DataSync | Applicable |
| Amazon DynamoDB Accelerator (DAX) | Applicable |
| AWS Database Migration Service (AWS DMS) | Applicable |
| Amazon DocumentDB | Applicable |
| AWS Direct Connect | Applicable |
| Amazon DynamoDB | Not applicable |
| Amazon EBS | Not applicable |
| Amazon EC2 Spot Fleet | Not applicable |
| Amazon EC2 API | Applicable |
| Amazon Elastic Container Service (ECS) | Not applicable |
| Amazon ECS Container Insights | Applicable |
| Amazon Elastic File System (EFS) | Not applicable |
| Amazon Elastic Kubernetes Service (EKS) | Applicable |
| Amazon ElastiCache (EC) | Not applicable |
| AWS Elastic Beanstalk | Applicable |
| Amazon Elastic Inference | Applicable |
| Amazon Elastic Transcoder | Applicable |
| Amazon Elastic Map Reduce (EMR) | Not applicable |
| Amazon Elasticsearch Service (ES) | Not applicable |
| Amazon EventBridge | Applicable |
| Amazon FSx | Applicable |
| Amazon GameLift | Applicable |
| AWS Glue | Not applicable |
| Amazon Inspector | Applicable |
| AWS Internet of Things (IoT) | Not applicable |
| AWS IoT Things Graph | Applicable |
| AWS IoT Analytics | Applicable |
| Amazon Managed Streaming for Kafka | Applicable |
| Amazon Kinesis Data Analytics | Not applicable |
| Amazon Data Firehose | Not applicable |
| Amazon Kinesis Data Streams | Not applicable |
| Amazon Kinesis Video Streams | Not applicable |
| AWS Lambda | Not applicable |
| Amazon Lex | Applicable |
| Amazon CloudWatch Logs | Applicable |
| AWS Elemental MediaTailor | Applicable |
| AWS Elemental MediaConnect | Applicable |
| AWS Elemental MediaConvert | Applicable |
| AWS Elemental MediaPackage Live | Applicable |
| AWS Elemental MediaPackage Video on Demand | Applicable |
| Amazon MQ | Applicable |
| Amazon VPC NAT Gateways | Not applicable |
| Amazon Neptune | Applicable |
| AWS OpsWorks | Applicable |
| Amazon Polly | Applicable |
| Amazon QLDB | Applicable |
| Amazon RDS | Not applicable |
| Amazon Redshift | Not applicable |
| Amazon Rekognition | Applicable |
| AWS RoboMaker | Applicable |
| Amazon Route 53 | Applicable |
| Amazon Route 53 Resolver | Applicable |
| Amazon S3 | Not applicable |
| Amazon SageMaker Batch Transform Jobs | Not applicable |
| Amazon SageMaker Endpoints | Not applicable |
| Amazon SageMaker Endpoint Instances | Not applicable |
| Amazon SageMaker Ground Truth | Not applicable |
| Amazon SageMaker Processing Jobs | Not applicable |
| Amazon SageMaker Training Jobs | Not applicable |
| AWS Service Catalog | Applicable |
| Amazon Simple Email Service (SES) | Not applicable |
| Amazon Simple Notification Service (SNS) | Not applicable |
| Amazon Simple Queue Service (SQS) | Not applicable |
| AWS Systems Manager - Run Command | Applicable |
| AWS Step Functions | Applicable |
| AWS Storage Gateway | Applicable |
| Amazon SWF | Applicable |
| Amazon Textract | Applicable |
| AWS Transfer Family | Applicable |
| AWS Transit Gateway | Applicable |
| Amazon Translate | Applicable |
| AWS Trusted Advisor | Applicable |
| AWS API Usage | Applicable |
| AWS Site-to-Site VPN | Applicable |
| AWS WAF Classic | Applicable |
| AWS WAF | Applicable |
| Amazon WorkMail | Applicable |
| Amazon WorkSpaces | Applicable |

![GameLift](https://dt-cdn.net/images/gamelift-dashboard-1-2982-7671d496d8.png)

## Available metrics

`FleetId` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| ActivatingGameSessions | Game sessions with `Activating` status, which means they are in the process of starting up | Count | Multi | FleetId | Applicable |
| ActivatingGameSessions |  | Count | Multi | Region, MetricGroups | Applicable |
| ActiveGameSessions | Game sessions with `Active` status, which means they are able to host players, and are hosting zero or more players | Count | Multi | FleetId | Applicable |
| ActiveGameSessions |  | Count | Multi | Region, MetricGroups | Applicable |
| ActiveInstances | Instances with `Active` status, which means they are running active server processes | Count | Multi | FleetId | Applicable |
| ActiveInstances |  | Count | Multi | Region, MetricGroups | Applicable |
| ActiveServerProcesses | Server processes with `Active` status, which means they are running and able to host game session | Count | Multi | FleetId | Applicable |
| ActiveServerProcesses |  | Count | Multi | Region, MetricGroups | Applicable |
| AvailableGameSessions | Active, healthy server processes that are not currently being used to host a game session and can start a new game session without a delay to spin up new server processes or instances | Count | Multi | FleetId | Applicable |
| AvailableGameSessions |  | Count | Multi | Region, MetricGroups | Applicable |
| AverageWaitTime | Average amount of time that game session placement requests in the queue in `Pending` status have been waiting to be fulfilled | Seconds | Multi | Region, QueueName | Applicable |
| AverageWaitTime |  | Seconds | Sum | Region, QueueName | Applicable |
| CurrentPlayerSessions | Player sessions with either `Active` status (player is connected to an active game session) or `Reserved` status (player has been given a slot in a game session but hasn't yet connected) | Count | Multi | FleetId | Applicable |
| CurrentPlayerSessions |  | Count | Multi | Region, MetricGroups | Applicable |
| CurrentTickets | Matchmaking requests currently being processed or waiting to be processed | Count | Multi | Region, ConfigurationName | Applicable |
| CurrentTickets |  | Count | Sum | Region, ConfigurationName | Applicable |
| DesiredInstances | Target number of active instances that GameLift is working to maintain in the fleet | Count | Multi | FleetId |  |
| FirstChoiceNotViable | Game sessions successfully placed but that aren't in the first-choice fleet, because that fleet isn't considered viable (such as a spot fleet with a high interruption rate) | Count/Minute | Multi | Region |  |
| FirstChoiceNotViable |  | Count/Minute | Multi | Region, QueueName |  |
| FirstChoiceNotViable |  | Count/Minute | Sum | Region |  |
| FirstChoiceNotViable |  | Count/Minute | Sum | Region, QueueName |  |
| FirstChoiceOutOfCapacity | Game sessions successfully placed but that aren't in the first-choice fleet, because that fleet doesn't have any available resources | Count/Minute | Multi | Region | Applicable |
| FirstChoiceOutOfCapacity |  | Count/Minute | Multi | Region, QueueName | Applicable |
| FirstChoiceOutOfCapacity |  | Count/Minute | Sum | Region | Applicable |
| FirstChoiceOutOfCapacity |  | Count/Minute | Sum | Region, QueueName | Applicable |
| GameSessionInterruptions | Number of game sessions on spot instances that have been interrupted | Count/Minute | Multi | FleetId |  |
| GameSessionInterruptions |  | Count/Minute | Multi | Region, MetricGroups |  |
| GameSessionInterruptions |  | Count/Minute | Sum | FleetId |  |
| GameSessionInterruptions |  | Count/Minute | Sum | Region, MetricGroups |  |
| HealthyServerProcesses | Active server processes that are reporting healthy | Count | Multi | FleetId | Applicable |
| HealthyServerProcesses |  | Count | Multi | Region, MetricGroups | Applicable |
| IdleInstances | Active instances that are currently hosting zero (0) game sessions. This metric measures capacity that is available but unused. | Count | Multi | FleetId | Applicable |
| IdleInstances |  | Count | Multi | Region, MetricGroups | Applicable |
| InstanceInterruptions | Number of spot instances that have been interrupted | Count/Minute | Multi | FleetId |  |
| InstanceInterruptions |  | Count/Minute | Multi | Region, MetricGroups |  |
| InstanceInterruptions |  | Count/Minute | Sum | FleetId |  |
| InstanceInterruptions |  | Count/Minute | Sum | Region, MetricGroups |  |
| LowestLatencyPlacement | Game sessions that were successfully placed in a region that offers the queue's lowest possible latency for the players | Count/Minute | Multi | Region | Applicable |
| LowestLatencyPlacement |  | Count/Minute | Multi | Region, QueueName | Applicable |
| LowestLatencyPlacement |  | Count/Minute | Sum | Region | Applicable |
| LowestLatencyPlacement |  | Count/Minute | Sum | Region, QueueName | Applicable |
| LowestPricePlacement | Game sessions that were successfully placed in a fleet with the queue's lowest possible price for the chosen region | Count/Minute | Multi | Region |  |
| LowestPricePlacement |  | Count/Minute | Multi | Region, QueueName |  |
| LowestPricePlacement |  | Count/Minute | Sum | Region |  |
| LowestPricePlacement |  | Count/Minute | Sum | Region, QueueName |  |
| MatchAcceptancesTimedOut | For matchmaking configurations that require acceptance, the potential matches that timed out during acceptance since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| MatchesAccepted | For matchmaking configurations that require acceptance, the potential matches that were accepted since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| MatchesCreated | Potential matches that were created since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| MatchesPlaced | Matches that were successfully placed into a game session since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| MatchesRejected | For matchmaking configurations that require acceptance, the potential matches that were rejected by at least one player since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| MaxInstances | Maximum number of instances that are allowed for the fleet | Count | Multi | FleetId |  |
| MinInstances | Minimum number of instances allowed for the fleet | Count | Multi | FleetId |  |
| PercentAvailableGameSessions | Percentage of game session slots on all active server processes (healthy or unhealthy) that are not currently being used (calculated as `AvailableGameSessions` / [`ActiveGameSessions` + `AvailableGameSessions` + unhealthy server processes]) | Percent | Average | FleetId | Applicable |
| PercentAvailableGameSessions |  | Percent | Average | Region, MetricGroups | Applicable |
| PercentHealthyServerProcesses | Percentage of all active server processes that are reporting healthy (calculated as `HealthyServerProcesses` / `ActiveServerProcesses`) | Percent | Multi | FleetId | Applicable |
| PercentHealthyServerProcesses |  | Percent | Multi | Region, MetricGroups | Applicable |
| PercentIdleInstances | Percentage of all active instances that are idle (calculated as `IdleInstances` / `ActiveInstances`) | Percent | Multi | FleetId | Applicable |
| PercentIdleInstances |  | Percent | Multi | Region, MetricGroups | Applicable |
| PlacementsCanceled | Game session placement requests canceled before timing out since the last report | Count/Minute | Multi | Region, QueueName | Applicable |
| PlacementsCanceled |  | Count/Minute | Sum | Region, QueueName | Applicable |
| PlacementsFailed | Game session placement requests that failed for any reason since the last report | Count/Minute | Multi | Region, QueueName | Applicable |
| PlacementsFailed |  | Count/Minute | Sum | Region, QueueName | Applicable |
| PlacementsStarted | New game session placement requests added to the queue since the last report | Count/Minute | Multi | Region, QueueName | Applicable |
| PlacementsStarted |  | Count/Minute | Sum | Region, QueueName | Applicable |
| PlacementsSucceeded | Game session placement requests that resulted in a new game session since the last report | Count/Minute | Multi | Region, QueueName | Applicable |
| PlacementsSucceeded |  | Count/Minute | Sum | Region, QueueName | Applicable |
| PlacementsTimedOut | Game session placement requests that reached the queue's timeout limit without being fulfilled since the last report | Count/Minute | Multi | Region, QueueName | Applicable |
| PlacementsTimedOut |  | Count/Minute | Sum | Region, QueueName | Applicable |
| PlayerSessionActivations | Player sessions that transitioned from `Reserved` to `Active` status since the last report | Count/Minute | Multi | FleetId | Applicable |
| PlayerSessionActivations |  | Count/Minute | Multi | Region, MetricGroups | Applicable |
| PlayerSessionActivations |  | Count/Minute | Sum | FleetId | Applicable |
| PlayerSessionActivations |  | Count/Minute | Sum | Region, MetricGroups | Applicable |
| PlayersStarted | Players in matchmaking tickets that were added since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| QueueDepth | Number of game session placement requests in the queue with `Pending` status | Count | Multi | Region, QueueName | Applicable |
| QueueDepth |  | Count | Sum | Region, QueueName | Applicable |
| ServerProcessAbnormalTerminations | Server processes that were shut down due to abnormal circumstances since the last report | Count/Minute | Multi | FleetId | Applicable |
| ServerProcessAbnormalTerminations |  | Count/Minute | Sum | FleetId | Applicable |
| ServerProcessAbnormalTerminations |  | Count/Minute | Multi | Region, MetricGroups | Applicable |
| ServerProcessAbnormalTerminations |  | Count/Minute | Sum | Region, MetricGroups | Applicable |
| ServerProcessActivations | Server processes that successfully transitioned from `Activating` to `Active` status since the last report | Count/Minute | Multi | FleetId | Applicable |
| ServerProcessActivations |  | Count/Minute | Sum | FleetId | Applicable |
| ServerProcessActivations |  | Count/Minute | Multi | Region, MetricGroups | Applicable |
| ServerProcessActivations |  | Count/Minute | Sum | Region, MetricGroups | Applicable |
| ServerProcessTerminations | Server processes that were shut down since the last report | Count/Minute | Multi | FleetId | Applicable |
| ServerProcessTerminations |  | Count/Minute | Sum | FleetId | Applicable |
| ServerProcessTerminations |  | Count/Minute | Multi | Region, MetricGroups | Applicable |
| ServerProcessTerminations |  | Count/Minute | Sum | Region, MetricGroups | Applicable |
| TicketsFailed | Matchmaking requests that resulted in failure since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| TicketsStarted | New matchmaking requests that were created since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| TicketsTimedOut | Matchmaking requests that reached the timeout limit since the last report | Count/Minute | Sum | Region, ConfigurationName | Applicable |
| TimeToMatch | For matchmaking requests that were put into a potential match before the last report, the amount of time between ticket creation and potential match creation | Seconds | Multi | Region, ConfigurationName | Applicable |
| TimeToTicketCancel | For matchmaking requests that were canceled before the last report, the amount of time between ticket creation and cancellation | Seconds | Multi | Region, ConfigurationName | Applicable |
| TimeToTicketSuccess | For matchmaking requests that succeeded before the last report, the amount of time between ticket creation and successful match placement | Seconds | Multi | Region, ConfigurationName | Applicable |