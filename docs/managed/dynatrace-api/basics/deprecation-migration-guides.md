---
title: "Migration guides for deprecated APIs"
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/deprecation-migration-guides
updated: 2026-02-09
---

# Migration guides for deprecated APIs

# Migration guides for deprecated APIs

* Reference
* Updated on Nov 20, 2025

The following APIs have been deprecated. For backward compatibility, the endpoints remain functional until further notice, but we recommend that you use the new options instead.

Every deprecated endpoint will eventually reach end of life (EOL) and be disabled. You won't be able to use them afterward. We provide enough time to switch to the new option before shutting down the old one. Even if the EOL date is not defined, you still should adapt your integrations to the new options.

## Deprecated

Deprecated API

What to use instead

Deprecated in version

End of life in version

Migration guide

Security context API

[Management zones API](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.")

[SaaS 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

[Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

Managed: 1.322

Monitored entities API v2 - Security context

[Management zones API](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.")

[SaaS 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

[Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

Managed: 1.322

Grail security context for monitored entities API

n/a

[Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

Managed: 1.322

Log security context API

n/a

[Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

Managed: 1.322

Business event security context API

n/a

[Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

Managed: 1.322

[Timeseries API v1](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.")

[Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")

[SaaS 1.305](/managed/whats-new/dynatrace-api/sprint-305#timeseries "Changelog for Dynatrace API version 1.305")

[Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")

End of 2025

Log Monitoring API v1

Log Management and Analytics: [Grail Query APIï»¿](https://developer.dynatrace.com/platform-services/services/storage/#grail-query-api)

Log Monitoring Classic: [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

For **Calculated metrics - Log Monitoring**, use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") endpoint with schemaId `builtin:logmonitoring.schemaless-log-metric`.

SaaS 1.280  
Managed 1.284

SaaS 1.325  
Managed 1.326

[Maintenance windows API [Environment]](/managed/dynatrace-api/environment-api/maintenance-windows "Learn how you can use the Dynatrace API to manage maintenance windows for periods of planned system downtime.")

[Maintenance windows API [Configuration]](/managed/dynatrace-api/configuration-api/maintenance-windows-api "Learn what the Dynatrace maintenance windows config API offers.")

[SaaS 1.173](/managed/whats-new/dynatrace-api/sprint-173 "Changelog for Dynatrace API version 1.173")  
Managed 1.174

[Topology and Smartscape](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.")

[Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")

[1.263](/managed/whats-new/dynatrace-api/sprint-242 "Changelog for Dynatrace API version 1.242")

[Topology and Smartscape to Monitored entities](/managed/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Migrate your automation to the Monitored entities API.")

[Credential vault API[Configuration]](/managed/dynatrace-api/configuration-api/credential-vault "Learn what the Dynatrace configuration API for credentials offers.")

[Credential vault API[Environment]](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.")

[1.252](/managed/whats-new/dynatrace-api/sprint-252 "Changelog for Dynatrace API version 1.252")

[Events API v1](/managed/dynatrace-api/environment-api/events-v1 "Find out what you can do with the Dynatrace Events API.")

[Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")

[SaaS 1.243](/managed/whats-new/dynatrace-api/sprint-243 "Changelog for Dynatrace API version 1.243")  
Managed 1.244

[Events v1 to Events v2](/managed/dynatrace-api/basics/deprecation-migration-guides/events-v1-to-v2 "Migrate your automation to Dynatrace Events API v2.")

[Problems API v1](/managed/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.")

[Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")

[SaaS 1.243](/managed/whats-new/dynatrace-api/sprint-243 "Changelog for Dynatrace API version 1.243")  
Managed 1.244

[Problems v1 to Problems v2](/managed/dynatrace-api/basics/deprecation-migration-guides/problems-v1-to-v2 "Migrate your automation to Dynatrace Problems API v2.")

[Tokens API v1](/managed/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")

[Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.")

[1.242](/managed/whats-new/dynatrace-api/sprint-242 "Changelog for Dynatrace API version 1.242")

[Tokens v1 to Access tokens](/managed/dynatrace-api/basics/deprecation-migration-guides/tokens-v1-to-v2 "Migrate your automation to the Dynatrace Access tokens API.")

Thresholds API

[Anomaly detection API - Metric event](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events "Learn what the Dynatrace Anomaly detection API for metric events offers.")

[SaaS 1.189](/managed/whats-new/dynatrace-api/sprint-189 "Changelog for Dynatrace API version 1.189")  
Managed 1.190

SaaS 1.275

[Timeseries v1 to Metrics v2ï»¿](https://docs.dynatrace.com/docs/shortlink/api-migration-timeseries)

## Migrated to Settings 2.0 framework

The following APIs have been migrated to the Settings 2.0 framework. Migrated configurations are handled via [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with a related schema.

Deprecated API

Schema to use instead

Deprecated in version

End of life in version

Migration guide

[Kubernetes credentials API](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api "Manage Kubernetes credentials via the Dynatrace configuration API.")

* **Kubernetes connection settings** (`builtin:cloud.kubernetes`)
* **Kubernetes platform monitoring settings** (`builtin:cloud.kubernetes.monitoring`)

1.288

[Kubernetes credentials to Settings 2.0](/managed/dynatrace-api/basics/deprecation-migration-guides/k8s-credentials-to-settings "Migrate your Kubernetes credentials automation to Dynatrace Settings API.")

[Cloud Foundry credentials API](/managed/dynatrace-api/configuration-api/cloud-foundry-foundations-credentials-api "Learn what the Dynatrace configuration API for Cloud Foundry credentials offers.")

**Cloud Foundry settings** (`builtin:cloud.cloudfoundry`)

1.288

[Cloud Foundry credentials to Settings 2.0](/managed/dynatrace-api/basics/deprecation-migration-guides/cloud-foundry-credentials-to-settings "Migrate your Cloud Foundry credentials automation to Dynatrace Settings API.")

[Automatically applied tags API](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api "Learn what the Dynatrace automatically applied tags API offers.")

**Automatically applied tags** (`builtin:tags.auto-tagging`)

[1.282](/managed/whats-new/dynatrace-api/sprint-282 "Changelog for Dynatrace API version 1.282")

[Management zones API](/managed/dynatrace-api/configuration-api/management-zones-api "Learn what the Dynatrace management zones config API offers.")

**Management zones settings** (`builtin:management-zones`)

[1.282](/managed/whats-new/dynatrace-api/sprint-282 "Changelog for Dynatrace API version 1.282")

[Remote environments API](/managed/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")

**Remote environment** (`builtin:remote.environment`)

[1.274](/managed/whats-new/dynatrace-api/sprint-274 "Changelog for Dynatrace API version 1.274")

[Anomaly detection API - Metric events](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events "Learn what the Dynatrace Anomaly detection API for metric events offers.")

**Metric events** (`builtin:anomaly-detection.metric-events`)

SaaS 1.265  
Managed 1.266

[Metric events to Settings 2.0](/managed/dynatrace-api/basics/deprecation-migration-guides/metric-events-to-settings "Migrate your metric events automation to Dynatrace Settings API.")

[Alerting profiles API](/managed/dynatrace-api/configuration-api/alerting-profiles-api "Learn what the Dynatrace alerting profiles API offers.")

**Problem alerting profiles** (`builtin:alerting.profile`)

SaaS 1.249  
Managed 1.250

[Alerting profiles to Settings 2.0](/managed/dynatrace-api/basics/deprecation-migration-guides/alerting-profiles-to-settings "Migrate your alerting profiles automation to Dynatrace Settings API.")

[Frequent issue detection API](/managed/dynatrace-api/configuration-api/frequent-issue-detection-api "Manage frequent issue detection configuration via the Dynatrace API.")

**Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`)

SaaS 1.249  
Managed 1.250

[Frequent issue detection to Settings 2.0](/managed/dynatrace-api/basics/deprecation-migration-guides/frequent-issues-to-settings "Migrate your frequent issue detection automation to Dynatrace Settings API.")

[Notifications API](/managed/dynatrace-api/configuration-api/notifications-api "Find out how to manage notification configuration via the Dynatrace Configuration API.")

**Problem notifications** (`builtin:problem.notifications`)

SaaS 1.249  
Managed 1.250

[OneAgent on a host API - Monitoring configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring "Manage the monitoring configuration of OneAgent instances via the Dynatrace API.")

**Monitoring** (`builtin:host.monitoring`)

[1.244](/managed/whats-new/dynatrace-api/sprint-244 "Changelog for Dynatrace API version 1.244")

[Maintenance windows API](/managed/dynatrace-api/configuration-api/maintenance-windows-api "Learn what the Dynatrace maintenance windows config API offers.")

**Maintenance windows** (`builtin:alerting.maintenance-window`)

[1.240](/managed/whats-new/dynatrace-api/sprint-240 "Changelog for Dynatrace API version 1.240")

[Maintenance windows to Settings 2.0](/managed/dynatrace-api/basics/deprecation-migration-guides/maintenance-windows-to-settings "Migrate your maintenance windows automation to Dynatrace Settings API.")

IBM MQ Tracing API

* **IBM MQ IMS bridges** (`builtin:ibmmq.ims-bridges`)
* **IBM MQ queue sharing groups** (`builtin:ibmmq.queue-sharing-group`)
* **IBM MQ queue managers** (`builtin:ibmmq.queue-managers`)

[1.238](/managed/whats-new/dynatrace-api/sprint-238 "Changelog for Dynatrace API version 1.238")

1.250
