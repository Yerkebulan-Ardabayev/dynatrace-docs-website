---
title: "Migration guides for deprecated APIs"
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/deprecation-migration-guides
updated: 2026-02-09
---

The following APIs have been deprecated. For backward compatibility, the endpoints remain functional until further notice, but we recommend that you use the new options instead.

Every deprecated endpoint will eventually reach end of life (EOL) and be disabled. You won't be able to use them afterward. We provide enough time to switch to the new option before shutting down the old one. Even if the EOL date is not defined, you still should adapt your integrations to the new options.

## Deprecated

Deprecated API

What to use instead

Deprecated in version

End of life in version

Migration guide

Security context API

Management zones API

SaaS 1.316

Managed 1.316

Managed: 1.322

Monitored entities API v2 - Security context

Management zones API

SaaS 1.316

Managed 1.316

Managed: 1.322

Grail security context for monitored entities API

n/a

Managed 1.316

Managed: 1.322

Log security context API

n/a

Managed 1.316

Managed: 1.322

Business event security context API

n/a

Managed 1.316

Managed: 1.322

Timeseries API v1

Metrics API v2

SaaS 1.305

Managed 1.316

End of 2025

Log Monitoring API v1

Log Management and Analytics: [Grail Query API](https://developer.dynatrace.com/platform-services/services/storage/#grail-query-api)

Log Monitoring Classic: Log Monitoring API

For **Calculated metrics - Log Monitoring**, use the Settings API endpoint with schemaId `builtin:logmonitoring.schemaless-log-metric`.

SaaS 1.280  
Managed 1.284

SaaS 1.325  
Managed 1.326

[Maintenance windows API [Environment]](/managed/dynatrace-api/environment-api/maintenance-windows "Learn how you can use the Dynatrace API to manage maintenance windows for periods of planned system downtime.")

[Maintenance windows API [Configuration]](/managed/dynatrace-api/configuration-api/maintenance-windows-api "Learn what the Dynatrace maintenance windows config API offers.")

SaaS 1.173  
Managed 1.174

Topology and Smartscape

Monitored entities

1.263

Topology and Smartscape to Monitored entities

[Credential vault API[Configuration]](/managed/dynatrace-api/configuration-api/credential-vault "Learn what the Dynatrace configuration API for credentials offers.")

[Credential vault API[Environment]](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.")

1.252

Events API v1

Events API v2

SaaS 1.243  
Managed 1.244

Events v1 to Events v2

Problems API v1

Problems API v2

SaaS 1.243  
Managed 1.244

Problems v1 to Problems v2

Tokens API v1

Access tokens API

1.242

Tokens v1 to Access tokens

Thresholds API

Anomaly detection API - Metric event

SaaS 1.189  
Managed 1.190

SaaS 1.275

[Timeseries v1 to Metrics v2](https://docs.dynatrace.com/docs/shortlink/api-migration-timeseries)

## Migrated to Settings 2.0 framework

The following APIs have been migrated to the Settings 2.0 framework. Migrated configurations are handled via Settings API with a related schema.

Deprecated API

Schema to use instead

Deprecated in version

End of life in version

Migration guide

Kubernetes credentials API

* **Kubernetes connection settings** (`builtin:cloud.kubernetes`)
* **Kubernetes platform monitoring settings** (`builtin:cloud.kubernetes.monitoring`)

1.288

Kubernetes credentials to Settings 2.0

Cloud Foundry credentials API

**Cloud Foundry settings** (`builtin:cloud.cloudfoundry`)

1.288

Cloud Foundry credentials to Settings 2.0

Automatically applied tags API

**Automatically applied tags** (`builtin:tags.auto-tagging`)

1.282

Management zones API

**Management zones settings** (`builtin:management-zones`)

1.282

Remote environments API

**Remote environment** (`builtin:remote.environment`)

1.274

Anomaly detection API - Metric events

**Metric events** (`builtin:anomaly-detection.metric-events`)

SaaS 1.265  
Managed 1.266

Metric events to Settings 2.0

Alerting profiles API

**Problem alerting profiles** (`builtin:alerting.profile`)

SaaS 1.249  
Managed 1.250

Alerting profiles to Settings 2.0

Frequent issue detection API

**Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`)

SaaS 1.249  
Managed 1.250

Frequent issue detection to Settings 2.0

Notifications API

**Problem notifications** (`builtin:problem.notifications`)

SaaS 1.249  
Managed 1.250

OneAgent on a host API - Monitoring configuration

**Monitoring** (`builtin:host.monitoring`)

1.244

Maintenance windows API

**Maintenance windows** (`builtin:alerting.maintenance-window`)

1.240

Maintenance windows to Settings 2.0

IBM MQ Tracing API

* **IBM MQ IMS bridges** (`builtin:ibmmq.ims-bridges`)
* **IBM MQ queue sharing groups** (`builtin:ibmmq.queue-sharing-group`)
* **IBM MQ queue managers** (`builtin:ibmmq.queue-managers`)

1.238

1.250
