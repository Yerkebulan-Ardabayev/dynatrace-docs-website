---
title: View AWS monitoring results
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/view-aws-monitoring-results
scraped: 2026-05-12T12:25:19.022204
---

# View AWS monitoring results

# View AWS monitoring results

* Explanation
* 3-min read
* Published Jul 19, 2018

## Your home dashboard

The **AWS account** tile is included on your home dashboard by default. This tile gives you a high-level overview of the AWS services in your account, distinguishing between healthy and unhealthy services. The contents of this tile vary based on your Amazon account configuration and the services you're running in your environment (EC2, RDS, EBS and ECB).

![AWS dashboard](https://dt-cdn.net/images/aws-dashboard-296-4a8fa91d21.png)

AWS dashboard

## AWS account page

Each **AWS account page** gives you an overview of the Amazon services running under that account. On this page you see:

* Dynamics of your environment. The **Environment dynamics** section shows you daily totals of EC2 instances segmented by Availability Zone. We present a 7 day overview with special attention paid to increases and decreases in total instance numbers.
* List of Elastic Load Balancers (ELB) and their backend EC2 instances.
* List of monitored cloud services integrating CloudWatch metrics into Dynatrace monitoring.
* List of load balancers in your environment.
* List of Amazon Relational Database Services (RDS) instances
* Number of S3 buckets.

![The Environment dynamics section shows you daily totals of EC2 instances](https://dt-cdn.net/images/aws-environment-dynamics-nosupsrv-1071-bd28ce9f23.png)

The Environment dynamics section shows you daily totals of EC2 instances

Serverless scenarios aren't instances and won't be displayed as instances in your AWS setup. Integrate with CloudWatch to have them show up as cloud services in Dynatrace.

## Host page

When we discover a monitored host running in Amazon cloud, we include an icon in the upper-left corner to indicate that the machine is cloud-based.

Each **Host** page details the health of the hardware resources that that host relies on.

For disks we offer both **Disk latency** and **EBS latency** metrics. When it comes to EBS metrics, Dynatrace discovers how local disks and EBS volumes are mapped together. We also detect striped volumes which helps us better understand the logic of your infrastructure.

For CPU we provide 2 perspectives of CPU usageâAWS perspective (**CPU AWS**: how much AWS CPU resource the EC2 instance consumes) and operating system perspective (**CPU utilization** ). The operating system perspective comes from Dynatrace OneAgent, and includes among other things, process breakdown so that you know what the CPU cycles are used for.

For more information, see [Host monitoring with Dynatrace](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.").

## Relational Database Service page

On each **Relational Database Service** (RDS) page we show you key performance metrics for that RDS instance and its properties, including engine type and version, endpoint, port, and Availability Zone.

For multi-Availability Zone, high availability (HA) deployments (RDS running in primary and standby mode), Dynatrace also shows the secondary Availability Zone. When a service disruption affecting the primary zone takes place and your RDS fails over to the secondary Availability Zone, the primary Availability Zone is automatically updated, while other properties (for example, endpoint) remain the same.

![AWS RDS](https://dt-cdn.net/images/aws-rds-798-44e97675cc.webp)

AWS RDS

## Smartscape

Smartscape shows Availability Zones as data centers. All Amazon services in an Availability Zone belong to the same data center.

To help you understand the relationships within your monitoring environment, we enable you to navigate directly to Smartscape from all EC2 instance (host) pages, RDS instance pages, and ELB pages.

![Smartscape AWS datacenter az](https://dt-cdn.net/images/smartscape-aws-datacenter-az-1051-35d491b93a.png)

Smartscape AWS datacenter az

## Problems page

When Amazon cloud is identified as the root cause of a problem, or when your cloud-based application suffers from problems, the cloud environment and its performance are factored into our event correlation and root cause analysis.

## Super search

Any time you need information regarding one of your Amazon services, type the service's name, ID, or other attribute into the search field on the menu bar. You can search based on any of the following attributes:

* EC2 name, instance ID, IP address, public or private host name
* RDS name or endpoint
* EBS volume ID
* ELB name
* Auto Scaling Group name

![AWS search](https://dt-cdn.net/images/aws-search-883-2d74fc27c9.png)

AWS search