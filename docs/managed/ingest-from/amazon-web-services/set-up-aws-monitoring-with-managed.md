---
title: Set up Dynatrace Managed for AWS monitoring
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed
scraped: 2026-05-12T12:13:23.222603
---

# Set up Dynatrace Managed for AWS monitoring

# Set up Dynatrace Managed for AWS monitoring

* Updated on Jun 27, 2022

You can integrate Dynatrace with [Amazon Web Services (AWS)ï»¿](https://www.dynatrace.com/technologies/aws-monitoring/) for intelligent monitoring of services running in the Amazon Cloud. AWS integration helps you stay on top of the dynamics of your data center in the cloud.

Dynatrace can be deployed with or without Environment ActiveGate.
While using the role-based access method, make sure that you meet one of the following deployment requirements:

* For deployments with Environment ActiveGate, the Environment ActiveGate must be hosted in AWS.
* For deployments without Environment ActiveGate, a Dynatrace Managed Server must be hosted in AWS.

## Overview

Follow these basic steps to integrate Dynatrace Managed with Amazon Web Services (AWS):

1. [Configure the access method](#access-method)
2. [Select your AWS partition](#partition)
3. [Adjust monitoring to your needs](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#define-aws-resource-tagging "Connect your Amazon account with Dynatrace Managed and start monitoring.")

Cloud-service monitoring consumption

All cloud services consume [Davis data units (DDUs)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs).

### AWS costs

Dynatrace makes Amazon API requests every five minutes. In addition to CloudWatch API calls, Dynatrace makes API calls to the monitored AWS services to learn about their instances, tags, etc. The list of called services and actions is available below in the [Create the monitoring policy](#monitoring-policy) section.

Here's a rough estimate of AWS monitoring costs:

| AWS service | Number of metrics | Daily cost per instance (USD) |
| --- | --- | --- |
| Elastic Compute Cloud (EC2) | 7 | $0.02016 |
| Elastic Block Store (EBS) | 8 | $0.02304 |
| Elastic Load Balancer (ELB) | 11 | $0.03168 |
| Relational Database Service (RDS) | 11 | $0.03168 |
| DynamoDB | 15 | $0.06912 |
| Lambda | 4 | $0.01152 |

Amazon charges

Amazon will charge about $0.01 per 1,000 metrics requested from the CloudWatch API and include the cost in the bill for the AWS account you use with Dynatrace.

## AWS monitoring policy

The AWS monitoring policy defines the minimal scope of permissions you need to give to Dynatrace to monitor the services running in your AWS account. Create it once and use it any time when enabling Dynatrace access to your AWS account.
If you don't want to add permissions to all services, and just select permissions for certain services, consult the table below. The table contains a set of permissions that are required for [All AWS cloud services](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.") and, for each cloud service, a list of optional permissions specific to that service.

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

## Access method

To get the information required for comprehensive AWS cloud-computing monitoring, Dynatrace needs to identify all the virtualized infrastructure components in your AWS environment and collect performance metrics related to those components. We use this information to understand the context of your applications, services, and hosts. For this to happen, you need to authorize Dynatrace to access your Amazon metrics.

Make sure that your Environment ActiveGate or Managed Cluster has a working connection to AWS. Configure your proxy for [Managed](/managed/managed-cluster/configuration/internet-proxy "Configure a proxy connection for your Managed Cluster if you don't have direct internet access.") or [ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy."), or allow access to `*.amazonaws.com` in your firewall settings.

## Role-based access with Environment ActiveGate or Dynatrace Managed Server

The instructions below apply whether or not the account hosting your ActiveGate is the same as your monitored account.

In a typical setup, you need to create two CloudFormation stacks using CloudFormation templates:

* A CloudFormation stack from the account hosting your ActiveGate, containing the following resources:

  + A role for your Environment ActiveGate or Dynatrace Managed Server hosted in your AWS infrastructure, on an Amazon EC2 host.
  + Its attached policy, which defines the monitored account permissions.
* A CloudFormation stack from the monitored account, containing the following resources:

  + A dedicated monitoring role for Dynatrace in your AWS account.
  + Its attached policy, which defines the Dynatrace authentication permissions to your AWS environment.

To monitor multiple accounts, add all resources to the **Resource** array in the template in [Step 1](#step1) and repeat [Step 2](#step2) to create a stack for each monitored account.

### Prerequisites for role-based access, with Environment ActiveGate or Dynatrace Managed Server

* [Dynatrace Managed Server](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") installed on an Amazon EC2 host. It must be able to assume a role within your AWS account that allows it to read the Dynatrace monitoring data.
* The ID of the AWS account that hosts the ActiveGate (for example, the account that hosts your Dynatrace components, which in this case is the one hosting Environment ActiveGate or Dynatrace Managed Server).
* The Amazon Web Services monitored account ID (the account you want to monitor).
* The name of the role with which your Environment ActiveGate or Dynatrace Managed Server was started.
* The External ID.

  How to get the External ID

  1. Go to **Settings**.
  2. Select **Cloud and virtualization** > **AWS** > **Connect new instance**.
  3. Under **Authentication method**, select **Role-based authentication**.
  4. Under **Your Amazon account ID**, select **Copy** to copy the token (the External ID).

To enable access to your Amazon account using role-based access, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a role for ActiveGate on the account that hosts ActiveGate**](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#step1 "Connect your Amazon account with Dynatrace Managed and start monitoring.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create a monitoring role for Dynatrace on your monitored account**](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#step2 "Connect your Amazon account with Dynatrace Managed and start monitoring.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Modify ActiveGate configuration**](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#step3 "Connect your Amazon account with Dynatrace Managed and start monitoring.")

### Step 1 Create a role for ActiveGate on the account that hosts ActiveGate

1. Create a YAML file and paste the contents of [github `role_based_access_AG_account_template.yml`ï»¿](https://dt-url.net/2t03ydj).

For multiple monitored accounts

For each account you want to monitor, in the **Resource** section of the template above, add a new item to the `!Sub` array in the following format: `'arn:aws:iam::<new_monitored_account_id>:role/<new_monitoring_role_name>'`.

Be sure to replace the placeholders (`<new_monitored_account_id>` and `<new_monitoring_role_name>`) with your own values.

2. Create the stack in your Amazon Console or using the CLI.

In the Amazon Console

1. In your Amazon Console, go to CloudFormation.
2. Go to **Stacks** and create a new stack with new resources.
3. Select **Template is ready**, upload the template you created above, and select **Next**.
4. In **Parameters**, for **MonitoredAccountID**, enter the ID of the account Dynatrace will monitor. Optionally, adapt other parameters as needed.
5. Enter a name for your stack, and then select **Next** twice.
6. Review your configuration, select **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, and select **Create stack**.

Using the CLI

Run the command below, making sure to replace the parameter values with your actual values.

You need to remove the angle brackets (`<` and `>`).

```
aws cloudformation create-stack \



--capabilities CAPABILITY_NAMED_IAM \



--stack-name <stack_name> \



--template-body <file:///home/user/template_file.yaml> \



--parameters ParameterKey=ActiveGateRoleName,ParameterValue=<role_name> ParameterKey=AssumePolicyName,ParameterValue=<policy_name> ParameterKey=MonitoringRoleName,ParameterValue=<monitoring_role_name> ParameterKey=MonitoredAccountID,ParameterValue=<monitored_account_id>
```

3. Go to the Amazon EC2 console, right-click an instance hosting your Environment ActiveGate, and select **Security** > **Modify IAM role**.
4. Select the role you created at step 1 (for example, Dynatrace\_ActiveGate\_role), and select **Apply**.

### Step 2 Create a monitoring role for Dynatrace on your monitored account

After the `Dynatrace_ActiveGate_role` is created on the account hosting the ActiveGate, create a role for the account to be monitored.

1. Create a YAML file and paste the content from the [github `role_based_access_monitored_account_template.yml`ï»¿](https://dt-url.net/pm03yni).
2. Create the stack in your Amazon Console or using the CLI.

   In the Amazon Console

   1. In your Amazon Console, go to CloudFormation.
   2. Go to **Stacks** and create a new stack with new resources.
   3. Select **Template is ready**, upload the template you created above, and select **Next**.
   4. In **Parameters**, enter:

   * The **External ID**. For details, see [Prerequisites](#env-ag)
   * The **ActiveGateRoleName** and the **ActiveGateAccountID** from the stack created in [Step 1](#step1).

   Optionally, adapt other parameters as needed.

   5. Enter a name for your stack, and then select **Next** twice.
   6. Review your configuration, enable **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, and select **Create stack**.

   Using the CLI

   Run the command below, making sure to replace the parameter values with your actual values.

   You need to remove the angle brackets (`<` and `>`).

   ```
   aws cloudformation create-stack \



   --capabilities CAPABILITY_NAMED_IAM \



   --stack-name <stack_name> \



   --template-body <file:///home/user/template_file.yaml> \



   --parameters ParameterKey=ExternalID,ParameterValue=<external_id> ParameterKey=ActiveGateRoleName,ParameterValue=<activegate_role_name> ParameterKey=ActiveGateAccountID,ParameterValue=<activegate_account_id>



   ParameterKey=RoleName,ParameterValue=<role_name> ParameterKey=PolicyName,ParameterValue=<policy_name>
   ```

### Step 3 Modify ActiveGate configuration

Starting with ActiveGate version 1.217, AWS monitoring is enabled by default. For configuration details, see [Customize ActiveGate properties](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#aws-monitoring "Learn which ActiveGate properties you can configure based on your needs and requirements."). The following configuration settings refer to earlier ActiveGate versions.

1. Edit the [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") configuration file of the ActiveGate that you want to use for AWS monitoring.
2. Set the following properties as below:

   ```
   [aws_monitoring]



   use_aws_proxy_role = false



   aws_monitoring_enabled = true
   ```

   ActiveGate version 1.183 or earlier

   ```
   [vertical.topology]



   use_aws_proxy_role = false
   ```

   ```
   [aws_monitoring]



   aws_monitoring_enabled = true
   ```

   Multiple ActiveGates

   It's enough to use only one ActiveGate dedicated for AWS monitoring. However, some deployment scenarios (for example, for redundancy purposes) might require multiple ActiveGates in your deployment.

   Make sure that only properly configured ActiveGates have `aws_monitoring_enabled` set to `true`.

   * They need network access to AWS endpoints.
   * For role-based monitoring, they must have proper roles attached.

   Keep in mind that Dynatrace cluster nodes contain embedded ActiveGates. Make sure to set the `aws_monitoring_enabled` property to `false` on these ActiveGates if they're not configured fully for AWS monitoring.

   If the ActiveGate is dedicated to AWS monitoring, you must also set the `MSGrouter` property to `false`:

   ```
   [collector]



   MSGrouter = false
   ```

   Remove `aws_proxy_account` and `aws_proxy_role` properties.
3. Save the file and [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Key-based access (AWS GovCloud and AWS China only)

Key-based authentication is only allowed for AWS GovCloud and China partitions.

In this scenario, you have to create an AWS monitoring policy and generate a key pair with that policy.

AWS IAM permissions boundaries may prohibit AWS actions required by Dynatrace. If you use an IAM permissions boundary on your AWS account, make sure that the actions from that policy are allowed in all AWS Regions within that permissions boundary.

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

Dynatrace can use access keys to make secure REST or Query protocol requests to the AWS service API. You'll need to generate an **Access key ID** and a **Secret access key** that Dynatrace can use to get metrics from Amazon Web Services.

6. In your Amazon Console, go to **Users** and select **Add Users**.
7. Enter the **User name**.
8. In the next screen, choose **Attach policies directly** and attach the policy that you created before.
9. Review the user details and select **Create user**.
10. From the list of users, select your newly created user name and go to **Security credentials**, then select **Create access key**.
11. In the **Access key best practices & alternatives** screen, select **Third-party service**, then select **Next**.
12. You will be transferred to the **Retrieve access keys** screen, where both your **Access key** and a **Secret access key** are present.
13. Store the **Access Key ID** name (AKID) and **Secret access key** values.
14. You can either download the user credentials or copy the credentials displayed online (select **Show**).

## Connect your Amazon account

Once you've granted AWS access to Dynatrace, it's time to connect Dynatrace to your Amazon AWS account.

1. In Dynatrace, go to **Settings > Cloud and virtualization > AWS** and select **Connect new instance**.
2. Select the **Role-based authentication** method.

   * Create a name for this connection. If you leave this field empty, the name **Role** will be used on Dynatrace pages to define this connection.
   * In the **Role** field, type the name of the role you created in Amazon for Dynatrace (for example, `Dynatrace_monitoring_role`).
   * Type your **Account ID** (the account you want us to pull metrics from).
   * Select **Connect** to verify and save the connection.
3. Once the connection is successfully verified and saved, your AWS account will be listed in the **Cloud and virtualization** settings page.  
   You should soon begin to see AWS cloud monitoring data.

## Select your AWS partition

If your AWS account is on a different partition than the default `aws` partition, you can select it and Dynatrace will connect to it instead.

To change your AWS partition

1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
2. Find the instance where you want to change the partition and select ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit the instance.
3. In the **AWS partition** list, select your partition.
4. Select **Save**.

## Adjust monitoring to your needs

You can alter the scope and content of your monitoring depending on your preferences by using tags and listing services needed.

### Limit monitored resources using tags

We recommend that you limit the scope of your AWS monitoring and reduce the number API calls to Amazon. You can use [tagging](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Add and configure AWS tags to limit AWS resources.") to limit the AWS resources (AWS service instances) that are monitored by Dynatrace.

## Set up metric events for alerting

To configure metric events for alerting, follow this [guide](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-set-up-metric-events-for-alerting "Set up and configure metric events for alerting.").

### Choose Cloud services to be monitored

Once your credentials are saved, you can decide which services will be monitored.
To select your preferred services

1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
2. Find the instance where you want to perform your monitoring and select ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit the instance.
3. In the **Services** section, select **Manage services**.
4. The following services are added by default: Amazon EC2, AWS Lambda, Amazon RDS, Amazon DynamoDB, Amazon ALB, Amazon ELB, Amazon S3, and Amazon EBS. You can extend this list by choosing services from the dropdown menu. The full list of services is also available at [All AWS cloud services](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.").
5. Select **Add service**
6. Select the service from the list and then select **Add service**.
7. Select **Save changes** to save your configuration.

## Related topics

* [Set up Dynatrace on Amazon Web Services](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.")
* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Limit API calls to AWS using tags](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Add and configure AWS tags to limit AWS resources.")