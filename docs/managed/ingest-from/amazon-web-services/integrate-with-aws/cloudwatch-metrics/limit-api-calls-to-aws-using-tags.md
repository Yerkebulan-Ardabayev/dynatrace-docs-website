---
title: Limit API calls to AWS using tags
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags
scraped: 2026-05-12T11:27:39.491231
---

# Limit API calls to AWS using tags

# Limit API calls to AWS using tags

* How-to guide
* 2-min read
* Published Jul 19, 2017

By default, Dynatrace monitors all Amazon Web Services that have been specified in your permission policy. Optionally, you can use tagging to limit the AWS resources (AWS service instances) that are monitored by Dynatrace.

## Add tags in AWS

To add a tag

1. Sign in to your AWS Management Console and go to the dashboard of the service you want to tag.
2. Select **Instances** to see a list of your environments, then select an instance.
3. In the panel below the list, select **Tags**.
4. Select **Add/Edit tags**, then select **Create tag**.
5. Enter a tag key/value pair (for example, 'monitor\_dynatrace' for **Key**, and 'true' for **Value**).
6. Select **Save**.

Dynatrace monitoring tags work for built-in: EC2, RDS, ELB, EBS, auto-scaling groups, DynamoDB, Lambda, and most cloud services.
Expand the table below to see which services can be filtered by tags.

### Tag filtering per service

| Name | Tags monitoring & filtering |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | yes |
| AWS Lambda (built-in) | yes |
| Amazon Application and Network Load Balancer (built-in) | yes |
| Amazon DynamoDB (built-in) | yes |
| Amazon EBS (built-in) | yes |
| Amazon EC2 (built-in) | yes |
| Amazon Elastic Load Balancer (ELB) (built-in) | yes |
| Amazon RDS (built-in) | yes |
| Amazon S3 (built-in) | yes |
| AWS Certificate Manager Private Certificate Authority | yes |
| Amazon API Gateway | yes |
| AWS App Runner | yes |
| Amazon AppStream | yes |
| AWS AppSync | yes |
| Amazon Athena | yes |
| Amazon Aurora | yes |
| Amazon EC2 Auto Scaling | - |
| AWS Billing | - |
| Amazon Keyspaces | yes |
| AWS Chatbot | - |
| Amazon CloudFront | yes |
| AWS CloudHSM | yes |
| Amazon CloudSearch | - |
| AWS CodeBuild | yes |
| Amazon Cognito | - |
| Amazon Connect | - |
| AWS DataSync | yes |
| Amazon DynamoDB Accelerator (DAX) | yes |
| AWS Database Migration Service (AWS DMS) | yes |
| Amazon DocumentDB | yes |
| AWS Direct Connect | yes |
| Amazon DynamoDB | yes |
| Amazon EBS | yes |
| Amazon EC2 Spot Fleet | - |
| Amazon EC2 API | - |
| Amazon Elastic Container Service (ECS) | yes |
| Amazon ECS Container Insights | yes |
| Amazon Elastic File System (EFS) | yes |
| Amazon Elastic Kubernetes Service (EKS) | yes |
| Amazon ElastiCache (EC) | yes |
| AWS Elastic Beanstalk | yes |
| Amazon Elastic Inference | yes |
| Amazon Elastic Transcoder | - |
| Amazon Elastic Map Reduce (EMR) | yes |
| Amazon Elasticsearch Service (ES) | yes |
| Amazon EventBridge | yes |
| Amazon FSx | yes |
| Amazon GameLift | - |
| AWS Glue | yes |
| Amazon Inspector | yes |
| AWS Internet of Things (IoT) | - |
| AWS IoT Things Graph | - |
| AWS IoT Analytics | - |
| Amazon Managed Streaming for Kafka | yes |
| Amazon Kinesis Data Analytics | yes |
| Amazon Data Firehose | yes |
| Amazon Kinesis Data Streams | yes |
| Amazon Kinesis Video Streams | yes |
| AWS Lambda | yes |
| Amazon Lex | yes |
| Amazon CloudWatch Logs | yes |
| AWS Elemental MediaTailor | yes |
| AWS Elemental MediaConnect | - |
| AWS Elemental MediaConvert | yes |
| AWS Elemental MediaPackage Live | yes |
| AWS Elemental MediaPackage Video on Demand | yes |
| Amazon MQ | - |
| Amazon VPC NAT Gateways | yes |
| Amazon Neptune | yes |
| AWS OpsWorks | yes |
| Amazon Polly | - |
| Amazon QLDB | yes |
| Amazon RDS | yes |
| Amazon Redshift | yes |
| Amazon Rekognition | - |
| AWS RoboMaker | yes |
| Amazon Route 53 | yes |
| Amazon Route 53 Resolver | yes |
| Amazon S3 | yes |
| Amazon SageMaker Batch Transform Jobs | - |
| Amazon SageMaker Endpoints | yes |
| Amazon SageMaker Endpoint Instances | yes |
| Amazon SageMaker Ground Truth | - |
| Amazon SageMaker Processing Jobs | - |
| Amazon SageMaker Training Jobs | - |
| AWS Service Catalog | - |
| Amazon Simple Email Service (SES) | - |
| Amazon Simple Notification Service (SNS) | yes |
| Amazon Simple Queue Service (SQS) | yes |
| AWS Systems Manager - Run Command | - |
| AWS Step Functions | - |
| AWS Storage Gateway | yes |
| Amazon SWF | - |
| Amazon Textract | - |
| AWS Transfer Family | yes |
| AWS Transit Gateway | yes |
| Amazon Translate | - |
| AWS Trusted Advisor | - |
| AWS API Usage | - |
| AWS Site-to-Site VPN | yes |
| AWS WAF Classic | - |
| AWS WAF | - |
| Amazon WorkMail | yes |
| Amazon WorkSpaces | yes |

## Configure Dynatrace to use AWS tags

Dynatrace enables you to use up to 10 AWS tags at a time. Once configured, Dynatrace takes tagged services into account when querying performance counters.

AWS tag key/value pairs are executed with an OR operator. Keys don't need to be unique.

Tag-based AWS monitoring offers a lot of flexibility and is particularly helpful if:

* You leverage multiple Dynatrace environments and you want to monitor distinct AWS services running under the same AWS account.  
  **Tag examples:** `monitor_dynatrace : myenvironment1; monitor_dynatrace : myenvironment2`
* You need to monitor the same AWS account, but distinguish between production and staging services.  
  **Tag examples:**  
  `monitor_dynatrace : production; monitor_dynatrace : staging`

To assign tags to a specific AWS instance

1. [Set up Dynatrace for AWS monitoring](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Monitor AWS with Dynatrace").
2. In Dynatrace, go to **Settings** > **Cloud and virtualization** > **AWS** and select the AWS instance.
3. For **Resources to be monitored**, select **Monitor resources selected by tags**.
4. Enter the **Key** and **Value**.
5. Select **Save**.