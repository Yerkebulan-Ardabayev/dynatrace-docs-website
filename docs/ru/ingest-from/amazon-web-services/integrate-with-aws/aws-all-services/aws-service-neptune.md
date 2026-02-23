---
title: Amazon Neptune monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-neptune
scraped: 2026-02-23T21:37:26.753554
---

# Amazon Neptune monitoring

# Amazon Neptune monitoring

* How-to guide
* 11-min read
* Published Jul 06, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon Neptune. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

To enable monitoring for this service, you need

* ActiveGate version 1.197+

* For Dynatrace SaaS deployments, you need an Environment ActiveGate or a Multi-environment ActiveGate.

  For role-based access in [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") deployment, you need an [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") installed on an Amazon EC2 host.

* Dynatrace version 1.200+
* An updated [AWS monitoring policy](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Integrate metrics from Amazon CloudWatch.") to include the additional AWS services.

To [update the AWS IAM policyï»¿](https://dt-url.net/8q038eb), use the JSON below, containing the monitoring policy (permissions) for all supporting services.

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

Example of JSON policy for one single service.

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

![Neptune](https://dt-cdn.net/images/dashboard-27-2686-043659e494.png)

## Available metrics

`DBClusterIdentifier` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| BackupRetentionPeriodStorageUsed | The total amount of backup storage, in bytes, used to support from the Neptune DB cluster's backup retention window | Bytes | Multi | DBClusterIdentifier |  |
| BackupRetentionPeriodStorageUsed |  | Bytes | Multi | Region, EngineName |  |
| CPUUtilization | The percentage of CPU utilization | Percent | Multi | DBClusterIdentifier | Applicable |
| CPUUtilization |  | Percent | Multi | DBClusterIdentifier | Applicable |
| CPUUtilization |  | Percent | Multi | Region | Applicable |
| CPUUtilization |  | Percent | Multi | Region, DBInstanceIdentifier | Applicable |
| CPUUtilization |  | Percent | Multi | Region, DatabaseClass | Applicable |
| CPUUtilization |  | Percent | Multi | Region, EngineName | Applicable |
| ClusterReplicaLag | For a read replica, the amount of lag when replicating updates from the primary instance, in milliseconds | Milliseconds | Multi | DBClusterIdentifier | Applicable |
| ClusterReplicaLag |  | Milliseconds | Multi | DBClusterIdentifier, Role | Applicable |
| ClusterReplicaLag |  | Milliseconds | Multi | Region | Applicable |
| ClusterReplicaLag |  | Milliseconds | Multi | Region, DBInstanceIdentifier | Applicable |
| ClusterReplicaLag |  | Milliseconds | Multi | Region, DatabaseClass | Applicable |
| ClusterReplicaLag |  | Milliseconds | Multi | Region, EngineName | Applicable |
| ClusterReplicaLagMaximum | The maximum amount of lag between the primary instance and each Neptune DB instance in the DB cluster, in milliseconds | Milliseconds | Multi | DBClusterIdentifier |  |
| ClusterReplicaLagMaximum |  | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| ClusterReplicaLagMaximum |  | Milliseconds | Multi | Region |  |
| ClusterReplicaLagMaximum |  | Milliseconds | Multi | Region, DBInstanceIdentifier |  |
| ClusterReplicaLagMaximum |  | Milliseconds | Multi | Region, DatabaseClass |  |
| ClusterReplicaLagMaximum |  | Milliseconds | Multi | Region, EngineName |  |
| ClusterReplicaLagMinimum | The minimum amount of lag between the primary instance and each Neptune DB instance in the DB cluster, in milliseconds | Milliseconds | Multi | DBClusterIdentifier |  |
| ClusterReplicaLagMinimum |  | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| ClusterReplicaLagMinimum |  | Milliseconds | Multi | Region |  |
| ClusterReplicaLagMinimum |  | Milliseconds | Multi | Region, DBInstanceIdentifier |  |
| ClusterReplicaLagMinimum |  | Milliseconds | Multi | Region, DatabaseClass |  |
| ClusterReplicaLagMinimum |  | Milliseconds | Multi | Region, EngineName |  |
| EngineUptime | The amount of time that the instance has been running, in seconds | Seconds | Multi | DBClusterIdentifier | Applicable |
| EngineUptime |  | Seconds | Multi | DBClusterIdentifier, Role | Applicable |
| EngineUptime |  | Seconds | Multi | Region | Applicable |
| EngineUptime |  | Seconds | Multi | Region, DBInstanceIdentifier | Applicable |
| EngineUptime |  | Seconds | Multi | Region, DatabaseClass | Applicable |
| EngineUptime |  | Seconds | Multi | Region, EngineName | Applicable |
| FreeableMemory | The amount of available RAM, in bytes | Bytes | Multi | DBClusterIdentifier | Applicable |
| FreeableMemory |  | Bytes | Multi | DBClusterIdentifier, Role | Applicable |
| FreeableMemory |  | Bytes | Multi | Region | Applicable |
| FreeableMemory |  | Bytes | Multi | Region, DBInstanceIdentifier | Applicable |
| FreeableMemory |  | Bytes | Multi | Region, DatabaseClass | Applicable |
| FreeableMemory |  | Bytes | Multi | Region, EngineName | Applicable |
| GremlinRequestsPerSec | Number of requests per second to the Gremlin engine | Count/Second | Multi | DBClusterIdentifier | Applicable |
| GremlinRequestsPerSec |  | Count/Second | Multi | DBClusterIdentifier, Role | Applicable |
| GremlinRequestsPerSec |  | Count/Second | Multi | Region | Applicable |
| GremlinRequestsPerSec |  | Count/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| GremlinRequestsPerSec |  | Count/Second | Multi | Region, DatabaseClass | Applicable |
| GremlinRequestsPerSec |  | Count/Second | Multi | Region, EngineName | Applicable |
| GremlinWebSocketOpenConnections | The number of open WebSocket connections to Neptune | Count/Second | Multi | DBClusterIdentifier |  |
| GremlinWebSocketOpenConnections |  | Count/Second | Multi | DBClusterIdentifier, Role |  |
| GremlinWebSocketOpenConnections |  | Count/Second | Multi | Region |  |
| GremlinWebSocketOpenConnections |  | Count/Second | Multi | Region, DBInstanceIdentifier |  |
| GremlinWebSocketOpenConnections |  | Count/Second | Multi | Region, DatabaseClass |  |
| GremlinWebSocketOpenConnections |  | Count/Second | Multi | Region, EngineName |  |
| LoaderRequestsPerSec | Number of loader requests per second | Count/Second | Multi | DBClusterIdentifier |  |
| LoaderRequestsPerSec |  | Count/Second | Multi | DBClusterIdentifier, Role |  |
| LoaderRequestsPerSec |  | Count/Second | Multi | Region |  |
| LoaderRequestsPerSec |  | Count/Second | Multi | Region, DBInstanceIdentifier |  |
| LoaderRequestsPerSec |  | Count/Second | Multi | Region, DatabaseClass |  |
| LoaderRequestsPerSec |  | Count/Second | Multi | Region, EngineName |  |
| MainRequestQueuePendingRequests | The number of requests waiting in the input queue pending execution. Neptune starts throttling requests when they exceed the maximum queue capacity | Count/Second | Multi | DBClusterIdentifier | Applicable |
| MainRequestQueuePendingRequests |  | Count/Second | Multi | DBClusterIdentifier, Role | Applicable |
| MainRequestQueuePendingRequests |  | Count/Second | Multi | Region | Applicable |
| MainRequestQueuePendingRequests |  | Count/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| MainRequestQueuePendingRequests |  | Count/Second | Multi | Region, DatabaseClass | Applicable |
| MainRequestQueuePendingRequests |  | Count/Second | Multi | Region, EngineName | Applicable |
| NetworkReceiveThroughput | The incoming (receive) network traffic on the DB instance, including both customer database traffic and Neptune traffic used for monitoring and replication, in bytes/second | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region, DBInstanceIdentifier |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region, DatabaseClass |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region, EngineName |  |
| NetworkThroughput | The amount of network throughput both received from and transmitted to clients by each instance in the Neptune DB cluster, in bytes per second. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume. | Bytes/Second | Multi | DBClusterIdentifier | Applicable |
| NetworkThroughput |  | Bytes/Second | Multi | DBClusterIdentifier, Role | Applicable |
| NetworkThroughput |  | Bytes/Second | Multi | Region | Applicable |
| NetworkThroughput |  | Bytes/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| NetworkThroughput |  | Bytes/Second | Multi | Region, DatabaseClass | Applicable |
| NetworkThroughput |  | Bytes/Second | Multi | Region, EngineName | Applicable |
| NetworkTransmitThroughput | The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Neptune traffic used for monitoring and replication, in bytes/second | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region, DBInstanceIdentifier |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region, DatabaseClass |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region, EngineName |  |
| NumTxCommitted | The number of transactions successfully committed per second | Count/Second | Multi | DBClusterIdentifier |  |
| NumTxCommitted |  | Count/Second | Multi | DBClusterIdentifier, Role |  |
| NumTxCommitted |  | Count/Second | Multi | Region |  |
| NumTxCommitted |  | Count/Second | Multi | Region, DBInstanceIdentifier |  |
| NumTxCommitted |  | Count/Second | Multi | Region, DatabaseClass |  |
| NumTxCommitted |  | Count/Second | Multi | Region, EngineName |  |
| NumTxOpened | The number of transactions opened on the server per second | Count/Second | Multi | DBClusterIdentifier |  |
| NumTxOpened |  | Count/Second | Multi | DBClusterIdentifier, Role |  |
| NumTxOpened |  | Count/Second | Multi | Region |  |
| NumTxOpened |  | Count/Second | Multi | Region, DBInstanceIdentifier |  |
| NumTxOpened |  | Count/Second | Multi | Region, DatabaseClass |  |
| NumTxOpened |  | Count/Second | Multi | Region, EngineName |  |
| NumTxRolledBack | The number of transactions per second rolled back on the server because of errors | Count/Second | Multi | DBClusterIdentifier |  |
| NumTxRolledBack |  | Count/Second | Multi | DBClusterIdentifier, Role |  |
| NumTxRolledBack |  | Count/Second | Multi | Region |  |
| NumTxRolledBack |  | Count/Second | Multi | Region, DBInstanceIdentifier |  |
| NumTxRolledBack |  | Count/Second | Multi | Region, DatabaseClass |  |
| NumTxRolledBack |  | Count/Second | Multi | Region, EngineName |  |
| SnapshotStorageUsed | The total amount of backup storage consumed by all snapshots for a Neptune DB cluster outside its backup retention window, in bytes | Bytes | Multi | DBClusterIdentifier |  |
| SnapshotStorageUsed |  | Bytes | Multi | Region, EngineName |  |
| SparqlRequestsPerSec | The number of requests per second to the SPARQL engine | Count/Second | Multi | DBClusterIdentifier | Applicable |
| SparqlRequestsPerSec |  | Count/Second | Multi | DBClusterIdentifier, Role | Applicable |
| SparqlRequestsPerSec |  | Count/Second | Multi | Region | Applicable |
| SparqlRequestsPerSec |  | Count/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| SparqlRequestsPerSec |  | Count/Second | Multi | Region, DatabaseClass | Applicable |
| SparqlRequestsPerSec |  | Count/Second | Multi | Region, EngineName | Applicable |
| TotalBackupStorageBilled | The total amount of backup storage for which you are billed for a given Neptune DB cluster, in bytes | Bytes | Multi | DBClusterIdentifier |  |
| TotalBackupStorageBilled |  | Bytes | Multi | Region, EngineName |  |
| TotalClientErrorsPerSec | The total number per second of requests that errored out because of client-side issues | Count/Second | Multi | DBClusterIdentifier | Applicable |
| TotalClientErrorsPerSec |  | Count/Second | Multi | DBClusterIdentifier, Role | Applicable |
| TotalClientErrorsPerSec |  | Count/Second | Multi | Region | Applicable |
| TotalClientErrorsPerSec |  | Count/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| TotalClientErrorsPerSec |  | Count/Second | Multi | Region, DatabaseClass | Applicable |
| TotalClientErrorsPerSec |  | Count/Second | Multi | Region, EngineName | Applicable |
| TotalRequestsPerSec | The total number of requests per second to the server from all sources | Count/Second | Multi | DBClusterIdentifier | Applicable |
| TotalRequestsPerSec |  | Count/Second | Multi | DBClusterIdentifier, Role | Applicable |
| TotalRequestsPerSec |  | Count/Second | Multi | Region | Applicable |
| TotalRequestsPerSec |  | Count/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| TotalRequestsPerSec |  | Count/Second | Multi | Region, DatabaseClass | Applicable |
| TotalRequestsPerSec |  | Count/Second | Multi | Region, EngineName | Applicable |
| TotalServerErrorsPerSec | The total number per second of requests that errored out on the server because of internal failures | Count/Second | Multi | DBClusterIdentifier | Applicable |
| TotalServerErrorsPerSec |  | Count/Second | Multi | DBClusterIdentifier, Role | Applicable |
| TotalServerErrorsPerSec |  | Count/Second | Multi | Region | Applicable |
| TotalServerErrorsPerSec |  | Count/Second | Multi | Region, DBInstanceIdentifier | Applicable |
| TotalServerErrorsPerSec |  | Count/Second | Multi | Region, DatabaseClass | Applicable |
| TotalServerErrorsPerSec |  | Count/Second | Multi | Region, EngineName | Applicable |
| VolumeBytesUsed | The total amount of storage allocated to your Neptune DB cluster, in bytes. This is the amount of storage for which you are billed. It is the maximum amount of storage allocated to your DB cluster at any point in its existence, not the amount you are currently using. | Bytes | Multi | DBClusterIdentifier | Applicable |
| VolumeBytesUsed | The amount of storage used by your Neptune DB instance, in bytes. | Bytes | Multi | Region, EngineName | Applicable |
| VolumeBytesLeftTotal | The remaining available space for the cluster volume, as measured in bytes | Bytes | Multi | DBClusterIdentifier | Applicable |
| VolumeBytesLeftTotal |  | Bytes | Multi | Region | Applicable |
| VolumeBytesLeftTotal |  | Bytes | Multi | Region, EngineName | Applicable |
| VolumeReadIOPs | The average number of billed read I/O operations from a cluster volume, reported at 5-minute intervals. | Bytes | Multi | DBClusterIdentifier | Applicable |
| VolumeReadIOPs |  | Bytes | Multi | Region, EngineName | Applicable |
| VolumeWriteIOPs | The average number of write disk I/O operations to the cluster volume, reported at 5-minute intervals | Bytes | Multi | DBClusterIdentifier | Applicable |
| VolumeWriteIOPs |  | Bytes | Multi | Region, EngineName | Applicable |