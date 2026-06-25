---
title: Private self-monitoring environment
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring/private-self-monitoring
scraped: 2026-05-12T11:53:29.169776
---

# Private self-monitoring environment

# Private self-monitoring environment

* Published Nov 17, 2021

If you have very strict data privacy requirements or you need full control over data residency and access, you can opt out any time from sending self-monitoring data to Dynatrace.

### Opt out of reporting self-monitoring data

To opt out of reporting Dynatrace Managed self-monitoring data, you need cluster administrator permissions.

1. Sign in to your Dynatrace Managed Cluster Management Console.
2. Go to **Settings** to display the Dynatrace Managed settings page.
3. Select **Preferences**.
4. Turn off **Dynatrace deployment health monitoring**.

If this setting is disabled - Please contact a Dynatrace product expert via live chat within your environment.

### Set up your own self-monitoring

To retain high availability of your self-monitoring data, we recommend that you set up cross-cluster monitoring. For example, have a pre-production cluster monitor a production cluster, and vice versa. If one cluster goes down, you still have access to self-monitoring data to troubleshoot on your own or with our support and services teams.

For advanced configuration of a self-monitoring environment, dashboards, alerting, and naming rules, reach our to our expert [ACE Servicesï»¿](https://www.dynatrace.com/services-support/expert-services/) team.