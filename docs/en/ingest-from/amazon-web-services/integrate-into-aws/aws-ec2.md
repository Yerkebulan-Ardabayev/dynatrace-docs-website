---
title: Monitor Amazon Elastic Compute Cloud (EC2)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2
scraped: 2026-03-06T21:17:42.722106
---

# Monitor Amazon Elastic Compute Cloud (EC2)


* Classic
* How-to guide
* 1-min read
* Published Jan 16, 2023

## Capabilities

* Full-stack monitoring powered by OneAgent
* Enhanced support for EC2 metadata such as regions and more
* [AWS Systems Manager Distributor package](aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor.md "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package.") for easy deployment of OneAgent
* [Integration with CloudWatch](../integrate-with-aws/cloudwatch-metrics.md "Integrate metrics from Amazon CloudWatch.") for metrics, properties and tags from AWS

## Integrate OneAgent for fullstack monitoring

Monitoring Amazon EC2 instances works out of the box. Just run the regular [Linux](../../dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux.md "Learn how to download and install Dynatrace OneAgent on Linux.") and [Windows](../../dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows.md "Learn how to download and install Dynatrace OneAgent on Windows.") OneAgent installers.

Alternatively, you can use any infrastructure management tool such as Terraform to integrate OneAgent on your virtual machines. Dynatrace also provides an integration with the [AWS Systems Manager Distributor](aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor.md "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package.") so you can distribute and automatically deploy OneAgent on your EC2 instances.