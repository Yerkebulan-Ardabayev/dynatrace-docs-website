---
title: Dynatrace Operator release notes version 0.10.1
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-0-10-1
scraped: 2026-02-22T21:23:38.006732
---

# Dynatrace Operator release notes version 0.10.1

# Dynatrace Operator release notes version 0.10.1

* Latest Dynatrace
* Release notes
* Published Dec 15, 2022

Release date: Dec 15, 2022

## Resolved issues

* Fixed the conversion webhook in the custom resource definition by updating the namespace field correctly.

* Immutable OneAgent support: communication information is now stored both in `Secret` (`TenantToken`), and `ConfigMap` (`TenantUUID`, `CommunicationEndpoints`). This fixes the restarts on communication endpoint changes by mounting them from the configmap, instead of adding the contents of the configmap directly to the arguments.

* Fixed the missing Docker labels on the release image.

* The node-driver-registrar component is updated to version 2.6.2.

* Fixed a bug for the read-only `hostMonitoring` mode: read-only `hostMonitoring` mode needs the CSI driver, but the CSI driver didn't behave correctly, which prevents the OneAgent pod to start.

* Fixed a bug causing pods to be incorrectly unmounted due to a locked database: when there are several pods requesting a volume at the same time, the CSI driver doesn't unmount pods correctly if the database is locked at mount time.