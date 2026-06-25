---
title: Enable service monitoring
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring
scraped: 2026-05-12T12:05:14.495477
---

# Enable service monitoring

# Enable service monitoring

* How-to guide
* 2-min read
* Published Nov 09, 2023

To enable monitoring for this service, you first need to integrate Dynatrace with Amazon Web Services:

* [Set up Dynatrace SaaS integration](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")
* [Set up Dynatrace Managed integration](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed "Connect your Amazon account with Dynatrace Managed and start monitoring.")

## Add the service to monitoring

In order to view the service metrics, you must add the service to monitoring in your Dynatrace environment.

To add a service to monitoring

1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
2. On the AWS overview page, scroll down and select the desired AWS instance. Select the **Edit** button.
3. Scroll down and select **Add service**. Choose the service name from the dropdown list and select **Add service**.
4. Select **Save changes**.

Cloud-service monitoring consumption

All cloud services consume [Davis data units (DDUs)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs).

Once AWS cloud services are added to monitoring, you might have to wait 15-20 minutes before the metric values are displayed.

## Monitor resources based on tags

You can choose to monitor resources based on existing AWS tags, as Dynatrace automatically imports them from service instances. Nevertheless, the transition from AWS to Dynatrace tagging isn't supported for all AWS services. Expand the table below to see which cloud services are filtered by tagging.

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

To monitor resources based on tags

1. Go to **Settings** > **Cloud and virtualization** > **AWS** > **Edit** for the desired AWS instance.
2. For **Resources to be monitored**, select **Monitor resources selected by tags**.
3. Enter the **Key** and **Value**.
4. Select **Save**.

## Configure service metrics

Once you add a service, Dynatrace starts automatically collecting a suite of metrics for this particular service. These are **recommended** metrics.

Service-wide metrics are metrics for the whole service across all regions. Typically, these metrics include dimensions containing **Region** in their name. If selected, these metrics are displayed on a separate chart when viewing your AWS deployment in Dynatrace. Keep in mind that available dimensions differ among services.

To change a metric's **statistics**, you have to recreate that metric by choosing different statistics. You can choose among the following statistics: **Sum**, **Minimum**, **Maximum**, **Average**, and **Sample count**. The **Average + Minimum + Maximum** statistics enable you to collect all three statistics as one metric instead of one statistic for three metrics separately. This can reduce your expenses for retrieving metrics from your AWS deployment.

### Recommended metrics

* Are enabled by default
* Can't be disabled
* Can have recommended dimensions (enabled by default, can't be disabled)
* Can have optional dimensions (disabled by default, can be enabled)

### Optional metrics

Apart from the recommended metrics, most services have the possibility of enabling **optional** metrics.

* Can be added and configured manually

### Add and configure metrics

1. Go to **Settings** > **Cloud and virtualization** > **AWS**.
2. On the AWS overview page, scroll down and select **Edit** for the desired AWS instance.
3. Scroll down to the **Services** section and select **Manage services**.
4. To add a metric, select the service for which you want to add metrics.
5. Select **Add new metric**.
6. From the menu, select the metric you want.
7. Select **Add metric** to add the metric to monitoring.
8. To configure a metric, select **Edit**.
9. Select **Apply** to save your configuration.