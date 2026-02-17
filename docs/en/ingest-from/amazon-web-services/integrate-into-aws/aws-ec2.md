---
title: Monitor Amazon Elastic Compute Cloud (EC2)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2
scraped: 2026-02-17T04:49:04.203756
---

# Monitor Amazon Elastic Compute Cloud (EC2)

# Monitor Amazon Elastic Compute Cloud (EC2)

* How-to guide
* 1-min read
* Published Jan 16, 2023

## Capabilities

* Full-stack monitoring powered by OneAgent
* Enhanced support for EC2 metadata such as regions and more
* [AWS Systems Manager Distributor package](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package.") for easy deployment of OneAgent
* [Integration with CloudWatch](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.") for metrics, properties and tags from AWS

## Integrate OneAgent for fullstack monitoring

Monitoring Amazon EC2 instances works out of the box. Just run the regular [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.") and [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Learn how to download and install Dynatrace OneAgent on Windows.") OneAgent installers.

Alternatively, you can use any infrastructure management tool such as Terraform to integrate OneAgent on your virtual machines. Dynatrace also provides an integration with the [AWS Systems Manager Distributor](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor "Install OneAgent on your EC2 instances using the Dynatrace AWS Systems Manager Distributor package.") so you can distribute and automatically deploy OneAgent on your EC2 instances.