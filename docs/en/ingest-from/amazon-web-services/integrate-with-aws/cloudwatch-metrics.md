---
title: Monitor Amazon Web Services with CloudWatch metrics
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics
scraped: 2026-02-18T05:55:34.816706
---

# Monitor Amazon Web Services with CloudWatch metrics

# Monitor Amazon Web Services with CloudWatch metrics

* How-to guide
* 23-min read
* Updated on Feb 05, 2026

Follow this guide to start ingesting data remotely from Amazon CloudWatch.

Its main focus is on infrastructure monitoring of AWS services: Dynatrace monitoring AWS services via CloudWatch.

See [What's next?](#next) for Full-Stack and Log Monitoring of your AWS services.

After you have established the initial monitoring, you can add, remove, or modify service monitoring using the Dynatrace web UI, at scale, or using the Dynatrace API.

Details of collected measurements

To learn the measurements collected for each of the AWS services, see:

* [AWS cloud services enabled by default and metrics](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/default-aws-metrics "The list of classic (formerly 'built-in') metrics Dynatrace collects by default for AWS monitoring.")
* [AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.")

The Amazon Web Services infrastructure monitoring provides metrics from CloudWatch, infrastructure data available via public AWS API, and specific events. The data is collected in five-minute intervals.

## Cost of monitoring

* Each service monitored by Dynatrace through CloudWatch, as well as log processing and analysis, consumes [DDUs](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").
* Amazon may charge you extra for CloudWatch metric queries. For details on these additional costs, please consult [Amazon CloudWatch pricing online documentationï»¿](https://aws.amazon.com/cloudwatch/pricing/).

## Monitoring prerequisites

There are three prerequisites for the AWS monitoring setup:

1. Dynatrace admin permissions

To manage AWS monitoring configuration, you need permissions to read and modify the `builtin:cloud.aws` schema.

* Both `settings:objects:read` and `settings:objects:write` are required.
* They are included in the **Change monitoring settings** permissions.
* Read-only access is not supported.

See [Manage user permissions with roles](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") for details on how to manage and set permissions.

2. Allow ActiveGate to access URLs

To monitor Amazon Web Services, Dynatrace needs to be able to connect to the Amazon CloudWatch API and query it periodically. At least one ActiveGate needs to be able to connect to Amazon CloudWatch to perform the monitoring tasks. Your ActiveGate needs to be deployed on an EC2 instance and be able to connect to the endpoints listed below.

From Dynatrace version 1.267+, only role-based access can be used. Key-based authorization is no longer available for new credentials. For existing key-based credentials, you can keep using keys indefinitely. We recommend switching to role-based authentication using the dedicated button on the configuration page. Dynatrace automatically checks the configuration to ensure the correct configuration of roles.

[Key-based authentication](#key-based-authentication) is allowed only for AWS GovCloud and China partitions.

An ActiveGate capable of monitoring your AWS account for classic (built-in) supported services is already provided and available within the Dynatrace AWS account.

However, to monitor specific non-default AWS cloud services or if your AWS account exceeds 2,000 AWS resources, you must install and configure an Environment ActiveGate. Follow the [ActiveGate installation guide](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") and resume this guide when done.

You must install and configure an Environment ActiveGate if you want to monitor either or both of the following:

* More than 2,000 AWS resources (AWS service instances)
* [Non-default AWS Cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#aws-non-default "Monitor all AWS cloud services with Dynatrace and view available metrics.")

#### Allow ActiveGate to access AWS URLs

The integration accesses the following AWS API endpoints, so they must be accessible from your ActiveGate:

* AWS Security Token Service (AWS STS)

```
https://sts.<REGION>.amazonaws.com/
```

```
https://sts.amazonaws.com/
```

AWS STS global endpoint is not supported. Make sure that `sts.<REGION>.amazonaws.com` is accessible for the regions you want to monitor.

See [AWS STS Regionalized endpointsï»¿](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html) for more details.

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

Other endpoints may be required depending on the services you need to monitor.

Consult the tables below for endpoints specific to each service you might want to monitor and for AWS Regions supported by Dynatrace AWS Monitoring.

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

### AWS Regions supported by Dynatrace AWS Monitoring

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

Proxy

The most frequent cause of certificate issues with the TLS interception proxy is a missing proxy's CA certificate in the ActiveGate truststore.

If you're still having proxy issues, see:

* [Proxy for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.")
* [Trusted root certificates for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to specify a custom truststore file that is merged with Java's root certificates and used as a default on all connections.")
* [Custom SSL certificate for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.")

"Communication error."

Make sure that the URLs are whitelisted. Otherwise, you might get communication or timeout errors.

3. AWS monitoring policy and role-based authentication

To perform these steps, you need to have AWS admin privileges.

The AWS monitoring policy defines the minimal scope of permissions you need to give to Dynatrace to monitor the services running in your AWS account. Create it once and use it any time when enabling Dynatrace access to your AWS account.
If you don't want to add permissions to all services, and just select permissions for certain services, consult the table below. The table contains a set of permissions that are required for [all AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics."), a list of optional permissions specific to that service.

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

To get the information required for comprehensive AWS cloud-computing monitoring, you have to authorize Dynatrace to access your Amazon metrics. Dynatrace will identify all the virtualized infrastructure components in your AWS environment and collect performance metrics related to those components.

Next, select the deployment model that best describes your environment and follow the procedure for that model.

Deployment with no ActiveGate

Deployment with existing ActiveGate

Dynatrace SaaS needs a role-based monitoring access to your AWS account.

You won't be able to monitor non-default AWS cloud services without an AWS-hosted Environment ActiveGate.

You will need:

* AWS account ID
* Rights to assign role-based access to your AWS account
* **External ID**, which can be acquired as follows.

  1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
  2. Select **Connect new Instance**.
  3. Under **Authentication method** select **Role-based authentication**.
  4. Under **Your Amazon account ID** select **Copy** to copy the token (External ID).

To create role-based access

1. Download a YAML file with CloudFormation template from [cloud-snippets/role\_based\_access\_no\_AG\_template.ymlï»¿](https://dt-url.net/8b23yuo).
2. Create the stack in your Amazon Console:

   1. In your Amazon Console, go to CloudFormation.
   2. Go to **Stacks** and create a new stack with new resources.
   3. Select **Template is ready**, upload the template you've created above, and select **Next**.
   4. In **Parameters**, enter the **External ID**.
   5. Enter a name for your stack and select **Next** twice.
   6. Review your configuration and accept the policy terms.
   7. Select **Create stack**.

   Alternative: create stack via CLI

   To create the stack using the CLI, run the command below, making sure to replace the parameter values with your actual values.

   You also need to remove the angle brackets (`<` and `>`).

   ```
   aws cloudformation create-stack \



   --capabilities CAPABILITY_NAMED_IAM \



   --stack-name <stack_name> \



   --template-body <file:///home/user/template_file.yaml> \



   --parameters ParameterKey=ExternalID,ParameterValue=<external_id> ParameterKey=RoleName,ParameterValue=<role_name> ParameterKey=PolicyName,ParameterValue=<policy_name>
   ```

The instructions below are applicable whether or not the account hosting your ActiveGate is the same as your monitored account. In a typical setup, you need to create two CloudFormation stacks using CloudFormation templates:

* A CloudFormation stack from the account hosting your ActiveGate, containing the following resources:

  + A [role for your Environment ActiveGate](#create-role-ag) hosted in your AWS infrastructure, on an Amazon EC2 host.
  + Its attached policy, defining the monitored account permissions.
* A CloudFormation stack from the monitored account, containing the following resources:

  + A dedicated [monitoring role](#create-role-dt) for Dynatrace in your AWS account.
  + Its attached policy, defining the Dynatrace authentication permissions to your AWS environment.

To monitor multiple accounts, use the `role_based_access_AG_account_multiple_monitoring_roles_template.yml` and repeat the [Create a role for ActiveGate on the account that hosts ActiveGate](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#create-role-dt "Integrate metrics from Amazon CloudWatch.") steps to create a stack for each monitored account.

You will need:

* An ActiveGate installed on an Amazon EC2 host. It must be able to assume a role within your AWS account that allows it to read the Dynatrace monitoring data.
* The ID of the AWS account that hosts the ActiveGate (the account that hosts your Dynatrace components, which in this case is the one hosting the Environment ActiveGate).
* The Amazon Web Services monitored account ID (the account that you want to monitor).
* The name of the role with which your Environment ActiveGate was started.
* The **External ID**, which you can get as follows.

  1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
  2. Select **Connect new instance**.
  3. Under **Authentication method**, select **Role-based authentication**.
  4. Under **Token**, select **Copy** to copy the token (the External ID) to your clipboard.

Create a role for ActiveGate on the account that hosts ActiveGate

1. Download the [role\_based\_access\_AG\_account\_template.ymlï»¿](https://dt-url.net/pv0306t).
2. Create the stack in your Amazon Console:

   1. In your Amazon Console, go to CloudFormation.
   2. Go to **Stacks** and create a new stack with new resources.
   3. Select **Template is ready**, upload the template you created above, and then select **Next**.
   4. In **Parameters**, for **Monitored Account ID**, enter the ID of the account Dynatrace will monitor. Optionally, adapt other parameters as needed.
   5. Enter a name for your stack, and then select **Next** twice.
   6. Review your configuration, select **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, and select **Submit**.

You can also create a stack via CLI using the command below:

```
aws cloudformation create-stack \



--capabilities CAPABILITY_NAMED_IAM \



--stack-name <stack_name> \



--template-body <file:///home/user/template_file.yaml> \



--parameters ParameterKey=ActiveGateRoleName,ParameterValue=<role_name> ParameterKey=AssumePolicyName,ParameterValue=<policy_name> ParameterKey=MonitoringRoleName,ParameterValue=<monitoring_role_name> ParameterKey=MonitoredAccountID,ParameterValue=<monitored_account_id>
```

3. Go to the Amazon EC2 console, right-click an instance hosting your Environment ActiveGate, and select **Security** > **Modify IAM role**.
4. Select the role you created and select **Update IAM role**.

Create a monitoring role for Dynatrace on your monitored account

After the `Dynatrace_ActiveGate_role` is created on the account hosting the ActiveGate, create a role for the account to be monitored.

1. Download a YAML file with CloudFormation template from [role\_based\_access\_monitored\_account\_template.ymlï»¿](https://dt-url.net/f30301j).
2. Create the stack in your Amazon Console:

   1. In your Amazon Console, go to CloudFormation.
   2. Go to **Stacks** and create a new stack with new resources.
   3. Select **Template is ready**, upload the template you created above, and select **Next**.
   4. In **Parameters**, enter **External ID**, **ActiveGateRoleName** and **ActiveGateAccountID** from the stack you created. Optionally, adapt other parameters if needed.
   5. Enter a name for your stack, and then select **Next** twice.
   6. Review your configuration, enable **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, and select **Submit**.

You can also create a stack via CLI using the command below:

```
aws cloudformation create-stack \



--capabilities CAPABILITY_NAMED_IAM \



--stack-name <stack_name> \



--template-body <file:///home/user/template_file.yaml> \



--parameters ParameterKey=ExternalID,ParameterValue=<external_id> ParameterKey=ActiveGateRoleName,ParameterValue=<activegate_role_name> ParameterKey=ActiveGateAccountID,ParameterValue=<activegate_account_id>
```

Modify ActiveGate configuration

Starting with ActiveGate version 1.217, AWS monitoring is enabled by default. For configuration details, see Customize ActiveGate properties. The following configuration settings refer to earlier ActiveGate versions.

1. Edit the `custom.properties` file of your Environment ActiveGate.
2. Make the following property settings:

   ```
   [aws_monitoring]



   use_aws_proxy_role = false



   aws_monitoring_enabled = true
   ```

   If the ActiveGate is dedicated to AWS monitoring, you also need to set the MSGrouter property as follows:

   ```
   [collector]



   MSGrouter = false
   ```
3. Save the file and restart the ActiveGate main service.

Key-based authentication (AWS GovCloud and AWS China only)

Only for AWS GovCloud and China partitions is key-based authentication allowed.

In this scenario you have to create an AWS monitoring policy and generate a key pair with that policy.

AWS Identity and Access Management (IAM) permission boundaries may deny AWS actions required by Dynatrace. If you use IAM permission boundary on your AWS account, make sure that actions from policy are allowed in all AWS Regions within permission boundary.

To create the AWS monitoring policy

1. In your Amazon Console, go to **Identity and Access Management**.
2. Go to **Policies** and select **Create policy**.
3. Select the JSON tab and paste the predefined policy from the box below.

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
4. Give the policy a name.
5. Select **Create policy**.

You'll need to generate an **Access key** and a **Secret access key** that Dynatrace can use to get metrics from Amazon Web Services.

6. In your Amazon Console, go to **Users** and select **Add Users**.
7. Enter the **User name**.
8. In the next screen, choose **Attach policies directly** and attach the policy that you created before.
9. Review the user details and select **Create user**.
10. From the list of users, select your newly created user name and go to **Security credentials**, then select **Create access key**.
11. On **Access key best practices & alternatives**, select **Third-party service**, then select **Next**.
12. On **Retrieve access keys**, store the **Access Key ID** name (AKID) and **Secret access key** values.
13. You can either download the user credentials or copy the credentials displayed online (select **Show**).

Alternative: create AWS roles with Terraform

Terraform templates are an alternative way of creating and configuring AWS roles. For detailed instructions on how to create AWS roles with Terraform, see [Configuring AWS role-based access with Terraformï»¿](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws/role-based-access/terraform-templates)

## Create monitoring configuration

You can create, activate, and manage multiple monitoring connections. Each connection is defined by the credentials and/or access tokens required for Dynatrace to be able to pull in the data.

Why configuration is performed per connection

Allowing for multiple connections and configurations makes it possible to monitor even extremely complex environments. With such an approach, you don't need to configure everything at once. Instead, you can gradually add monitoring configurations to your existing setup. Such an architecture also makes it easy to react to the dynamic changes of the monitored environment, without needing to reconfigure the unaffected elements.

1. Add a new AWS connection

If you've followed all the prior steps, you're ready to configure Amazon Web Services monitoring.

To add a new AWS connection

1. Open ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
2. Select **Integration manager** tab.
3. Learn how to navigate and connect a new instance via [Integration manager](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app#integration-manager "Monitor all cloud platforms at once.").

2. AWS cloud services monitored by default

After Dynatrace connects to your AWS environment, it immediately starts monitoring [selected AWS services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#aws-default "Monitor all AWS cloud services with Dynatrace and view available metrics."). [Classic (formerly 'built-in') AWS metrics](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/default-aws-metrics "The list of classic (formerly 'built-in') metrics Dynatrace collects by default for AWS monitoring.") lists the metrics of AWS cloud services monitored by default.

3. Monitor other AWS services

In addition to AWS services, it's also possible to monitor all other AWS cloud services. AWS cloud services are enabled for monitoring per AWS connection.

To add a service to monitoring:

1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
2. On the AWS overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. Select **Add service**.
5. Select the service from the list and then select **Add service**.
6. Select **Save changes** to save your configuration.

You can add multiple cloud services by repeating the steps above.

Configuration of collected metrics per service

After you add a service, Dynatrace automatically starts collecting a set of metrics for this particular service.

Recommended metrics:

* Enabled by default
* Can not be disabled
* Can come with recommended dimensions (enabled by default, can't be disabled)
* Can come with optional dimensions (disabled by default, can be enabled)

Apart from the recommended metrics, most services have the possibility of enabling optional metrics that can be added and configured manually.

List of AWS cloud services and collected metrics

To see the complete list of AWS cloud services and learn about the metrics collected for each of them, see [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.").

Alternatively, you can check the list of supported AWS Services within in-product Dynatrace Hub (search for **AWS**) or in the [web version of Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=aws).

To add and configure metrics

1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
2. On the AWS overview page, find the connection that you want to change and select the edit icon next to its name.
3. Go to **Services** and select **Manage services**.
4. To add a metric select the service for which you want to add metrics and select **Add new metric**.
5. From the menu select **Add metric** for the metric you want to monitor.
6. Select **Edit** to configure the metric.
7. Select **Apply** to save your configuration.

After you select the cloud services and save your changes, monitoring of the newly added services starts automatically.

## What's next?

Within minutes, you'll see the data on your dashboards.

To see the core measurements per each of the AWS connections

1. Go to ![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS") **AWS Classic**.
2. Select the connection for which you want to see an overview of the AWS infrastructure.

You can also build your own dashboard from the metrics collected for your AWS instances. For details on building dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

Virtual Machines, containers, and deep code monitoring with Dynatrace OneAgent

Dynatrace OneAgent offers unparalleled depth of insight into hosts, containers, and code. To learn more, see [Set up Dynatrace on Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.").

Further configuration for notifications and alerts

After you set up AWS monitoring, you can:

* [Set up metric events for alerting](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-set-up-metric-events-for-alerting "Set up and configure metric events for alerting."). This enables you to create, enable, disable and configure recommended alerting rules.
* [Limit API calls to AWS using tags](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Add and configure AWS tags to limit AWS resources."). By default, Dynatrace monitors all Amazon Web Services that have been specified in your permission policy. Optionally, you can use tagging to limit the AWS resources that are monitored by Dynatrace.

Integrate CloudWatch Metric Streams

This method of monitoring does not require an ActiveGate. Dynatrace integration with Amazon CloudWatch Metric Streams provides a simple and safe way to ingest AWS metrics. Amazon CloudWatch Metric Streams allows all metrics issued in a given AWS region to be streamed through Kinesis Firehose to the Dynatrace API. For details, see [Amazon CloudWatch Metric Streams](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams "Ingest metrics from your AWS accounts using Amazon CloudWatch Metric Streams.").

OpenTelemetry and distributed tracing

It is also possible to [trace AWS Lambda .NET Core functions with OpenTelemetry .NET](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.").