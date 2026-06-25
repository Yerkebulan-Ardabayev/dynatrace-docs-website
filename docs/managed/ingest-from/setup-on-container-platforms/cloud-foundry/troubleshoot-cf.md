---
title: Troubleshooting OneAgent deployment issues on Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/troubleshoot-cf
scraped: 2026-05-12T11:09:25.777114
---

# Troubleshooting OneAgent deployment issues on Cloud Foundry

# Troubleshooting OneAgent deployment issues on Cloud Foundry

* 1-min read
* Published Apr 23, 2020

Find out how to troubleshoot the possible issues you might encounter when deploying OneAgent on Cloud Foundry and how to access the OneAgent log files.

* [OneAgent deployment issues on Cloud Foundry for application-only monitoringï»¿](https://dt-url.net/7a637wx)

## Log files

You can troubleshoot issues regarding OneAgent deployment on Cloud Foundry by examining the logs. Depending on your deployment strategy, these are located at the following paths:

* [OneAgent for application-only monitoring log filesï»¿](https://dt-url.net/86437m0)

### OneAgent BOSH log files

For deployments using OneAgent BOSH, log files are accessible at the following locations:

* **Default path**: `/opt/dynatrace/oneagent` (symlink to `/var/vcap/data/dynatrace/oneagent/log`)
* `/var/vcap/data/dynatrace/oneagent/log`
* `/var/vcap/sys/log/dynatrace`

You need root permission to access the `/var/vcap/data/dynatrace` directory.

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")