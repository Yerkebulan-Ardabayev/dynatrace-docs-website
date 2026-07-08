---
title: ActiveGate auto-update configuration API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config
---

# ActiveGate auto-update configuration API

# ActiveGate auto-update configuration API

* Reference
* Updated on Jun 23, 2026

Use these endpoints to turn automatic updates for Environment ActiveGates on or off. The global endpoints read and set the environment-wide default (`globalSetting`: `ENABLED` or `DISABLED`). The per-ActiveGate endpoints read and set an override (`setting`: `ENABLED`, `DISABLED`, or `INHERITED`) and return the resulting `effectiveSetting`.

To configure the ActiveGate **target version**, **update mode** (automatic at earliest convenience, automatic during an update window, or no automatic updates), and **update windows**, use the Settings API with the [`builtin:deployment.activegate.updates`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-activegate-updates "View builtin:deployment.activegate.updates settings schema table of your monitoring environment via the Dynatrace API.") schema. ActiveGate and OneAgent share update windows through the [`builtin:deployment.management.update-windows`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-management-update-windows "View builtin:deployment.management.update-windows settings schema table of your monitoring environment via the Dynatrace API.") schema.

Per-ActiveGate settings override the environment-wide default. For the end-user workflow, see [Update ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Configure Environment ActiveGate automatic updates---update mode, target version, and update windows---and download or install manually.").

[### View global configuration

Get an overview of the global auto-update configuration of Environment ActiveGates.](/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-global "View the global auto-update configuration of your Environment ActiveGates via the Dynatrace API.")[### Edit global configuration

Update the global auto-update configuration of Environment ActiveGates.](/managed/dynatrace-api/environment-api/activegates/auto-update-config/put-global "Edit global auto-update configuration of your Environment ActiveGates via the Dynatrace API.")[### View ActiveGate configuration

Get an overview of the auto-update configuration of an Environment ActiveGate.](/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-instance "View the auto-update configuration of an Environment ActiveGate via the Dynatrace API.")[### Edit ActiveGate configuration

Update the configuration of auto-updates of an Environment ActiveGate.](/managed/dynatrace-api/environment-api/activegates/auto-update-config/put-instance "Edit the auto-update configuration of an Environment ActiveGate via the Dynatrace API.")

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")