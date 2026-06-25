---
title: Configure network availability monitoring (NAM) via Settings 2.0 API (workaround)
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/nam-workaround
scraped: 2026-05-12T12:03:02.647092
---

# Configure network availability monitoring (NAM) via Settings 2.0 API (workaround)

# Configure network availability monitoring (NAM) via Settings 2.0 API (workaround)

* How-to guide
* 1-min read
* Published Sep 25, 2024

Monaco doesn't support [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."), but you can configure [Synthetic monitors API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors "Create, read, update and delete Synthetic monitors. Currently browser and network availability monitors only.") via the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

## Access token configuration

To use [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."), you need an access token that has at least the following permissions:

* **Write settings** (`settings.write`)
* **Read settings** (`settings.read`)
* **Access problem and event feed, metrics, and topology** (`DataExport`)

## Monitor configuration

Definitions of [network availability monitoring (NAM)](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors "Create, read, update and delete Synthetic monitors. Currently browser and network availability monitors only.") are covered by the following schemas:

* [`builtin:synthetic.multiprotocol.config`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-config "View builtin:synthetic.multiprotocol.config settings schema table of your monitoring environment via the Dynatrace API.")
* [`builtin:synthetic.multiprotocol.name`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-name "View builtin:synthetic.multiprotocol.name settings schema table of your monitoring environment via the Dynatrace API.")
* [`builtin:synthetic.multiprotocol.outage-handling`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-outage-handling "View builtin:synthetic.multiprotocol.outage-handling settings schema table of your monitoring environment via the Dynatrace API.")
* [`builtin:synthetic.multiprotocol.performance-thresholds`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-performance-thresholds "View builtin:synthetic.multiprotocol.performance-thresholds settings schema table of your monitoring environment via the Dynatrace API.")
* [`builtin:synthetic.multiprotocol.scheduling`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-scheduling "View builtin:synthetic.multiprotocol.scheduling settings schema table of your monitoring environment via the Dynatrace API.")

The easiest way to create a new NAM configuration is to create it on the environment, get its configuration by downloading settings, and filtering for the settings you need.

List the required configuration in the `config.yaml` file. Each configuration needs to be in a separate JSON file. The following is an example (where values under `config/template` need to point to your specific configuration):

```
configs:



- id: NAM-config



config:



template: monitor-config.json



type:



settings:



schema: builtin:synthetic.multiprotocol.config



scope: MULTIPROTOCOL_MONITOR-D48EB7B8D7BC7B71



- id: NAM-name



config:



template: monitor-name.json



type:



settings:



schema: builtin:synthetic.multiprotocol.name



scope: MULTIPROTOCOL_MONITOR-D48EB7B8D7BC7B71



- id: NAM-outage



config:



template: monitor-outage.json



type:



settings:



schema: builtin:synthetic.multiprotocol.outage-handling



scope: MULTIPROTOCOL_MONITOR-D48EB7B8D7BC7B71



- id: NAM-thresholds



config:



template: monitor-thresholds.json



type:



settings:



schema: builtin:synthetic.multiprotocol.performance-thresholds



scope: MULTIPROTOCOL_MONITOR-D48EB7B8D7BC7B71



- id: NAM-scheduling



config:



template: monitor-scheduling.json



type:



settings:



schema: builtin:synthetic.multiprotocol.scheduling



scope: MULTIPROTOCOL_MONITOR-D48EB7B8D7BC7B71
```

## Related topics

* [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers.")
* [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Synthetic monitors API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors "Create, read, update and delete Synthetic monitors. Currently browser and network availability monitors only.")