---
title: Audit logs via API
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/configuration/audit-logs-api
---

# Audit logs via API

# Audit logs via API

* How-to guide
* 1-min read
* Updated on Oct 14, 2026

Audit logs are crucial for tracking changes and security-relevant events. Dynatrace can log such events so that you can review important changes: when the change was made, by whom, and what was changed.

The following events are logged:

* Any change to Dynatrace environment configuration
* Any change to environment API tokens
* Logins to Dynatrace
* Logouts from Dynatrace

The environment audit log records configuration changes and API requests. Ingested records are not audit events, whether the data arrives through the REST ingest endpoints (for example, `/api/v2/metrics/ingest`, `/api/v2/logs/ingest`, and OTLP endpoints), through OneAgent, or through an ActiveGate. Changes to the ingest configuration are recorded as configuration changes.

Changes to OAuth tokens and changes to Account Management configuration, such as SSO, are outside the scope of the environment audit log.

Audit logs include personal identifiable information (PII) such as email addresses and IP addresses of Dynatrace users.

## Enable audit logging

🔴 Disabled by default

To enable audit logging

1. Go to **Settings** > **Preferences** > **Log audit events**.
2. Turn on **Log all audit-related system events**.

Dynatrace retains audit logs for 30 days and automatically deletes them afterwards.

You can also enable audit logs via [Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api/put-configuration "Edit data privacy configuration via the Dynatrace API.").

## Access Dynatrace environment audit logs

You can access environment-wide audit logs via the [GET audit log](/managed/dynatrace-api/environment-api/audit-logs/get-log "View full audit log via Dynatrace API.") API call.

## Access Dynatrace Managed cluster audit logs

You can access cluster-wide audit logs of Dynatrace Managed clusters by viewing the audit log files stored in the file system. All audit log files are stored in the log folder. The path to the log folder is documented in [Hardware requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

Additionally, Dynatrace Managed offers an audit log viewer in the Cluster Management Console (**Audit log** in the navigation menu).

## Related topics

* [Audit logs API](/managed/dynatrace-api/environment-api/audit-logs "Read Dynatrace audit logs via Dynatrace API.")
* [Data privacy API - PUT configuration](/managed/dynatrace-api/configuration-api/data-privacy-api/put-configuration "Edit data privacy configuration via the Dynatrace API.")