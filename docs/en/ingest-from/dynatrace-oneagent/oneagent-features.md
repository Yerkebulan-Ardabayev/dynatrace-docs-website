---
title: OneAgent features
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-features
scraped: 2026-02-19T21:12:48.119125
---

# OneAgent features

# OneAgent features

* Latest Dynatrace
* 4-min read
* Updated on Feb 11, 2025

When you create your environment, OneAgent comes with a big set of features that are activated by default. Nevertheless, you always need to explicitly activate features added by newer versions of OneAgent and *opt-in* features, such as the automatic enrichment of log entries with the trace ID.

New OneAgent features are fully supported and tested as soon as theyâre available.

* For new environments, you can activate or deactivate OneAgent features (opt-in) based on the specific use case.
* For existing environments, newly added OneAgent features still require explicit activation from users with **Write settings** (`settings.write`) permission on the [Settings API - OneAgent features schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-features "View builtin:oneagent.features settings schema table of your monitoring environment via the Dynatrace API.").

## Scope

New OneAgent features typically are enabled globally (for the entire environment). However, you can choose to enable or disable them within the scope of a process group. Process group settings override the global settings for the same OneAgent feature.

## Use cases

* As new features are continuously added to OneAgent, you need to explicitly enable them within your existing monitoring environments to avoid unexpected changes.
* You may choose to disable certain OneAgent features at a fine-grained level when resolving issues. This can be useful in identifying the root cause of a problem down to a specific feature. To learn more, see [Troubleshooting OneAgent deep-monitoring issues](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-deep-monitoring-issues "Work with the Dynatrace Support team to troubleshoot OneAgent deep-monitoring issues.").

## Web UI or API

* You can enable or disable OneAgent features via the Dynatrace web UI on the **OneAgent features** page at the appropriate level (global or process group).
* You can use the Dynatrace [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to make the same settings via API calls.

### Configuration via web UI

To enable or disable OneAgent features via the Dynatrace web UI, use the **OneAgent features** page at the appropriate level.

Each feature on the **OneAgent features** page shows a list of requirements:

* **Min. OneAgent version** specifies the minimum OneAgent version required. You can enable a feature only when the OneAgent version meets the requirement.
* **Requires restart** specifies whether the feature requires a process restart before it becomes operational.

### Global configuration

To enable or disable a OneAgent feature globally

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Find the feature in the list and turn **Enabled** on or off.

### Process group configuration

To enable or disable a OneAgent feature for a process group

1. Go to **Smartscape Topology**.
2. Select **Processes**.
3. On the topology map, hover over the process and select the link icon to go to the process details page. For example:

   ![Link from Smartscape topology to process details page](https://dt-cdn.net/images/link-to-process-page-377-da0282e435.png)
4. On the process details page, select  > **Settings**.
5. On the **Process group settings** page, select the **OneAgent features** tab.
6. Select **Add override** to add a process-specific setting that overrides the environment setting.
7. Type a search string in the **Feature** box to find and select the feature.
8. Set the switches as needed for the override and then select **Save changes**.

### Configuration via API

Using the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), you can:

* **Enable/disable** your OneAgent feature settings.
* **Override the scope** of a OneAgent feature to have a different setting for a specific process group or process.
* **Export** the current configuration from an environment

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

To use the Settings API

1. To learn the JSON format required to post your configuration, use the [Get a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint. The schema ID is `builtin:oneagent.features`.

   Example: JSON payload to disable Java log-context enrichment for unstructured logs for a specific process group.

   ```
   [



   {



   "schemaId":  "builtin:oneagent.features",



   "scope": "PROCESS_GROUP-1",



   "value": {



   "enabled": false,



   "key": "JAVA_LOG_ENRICHMENT_UNSTRUCTURED"



   }



   }



   ]
   ```

   You can also change settings that are applied environment-wide using the environment scope.

   Example: JSON payload to enable Kafka Streams support globally

   Dynatrace version 1.244+

   ```
   [



   {



   "schemaId":  "builtin:oneagent.features",



   "scope": "Environment",



   "value": {



   "enabled": true,



   "key": "JAVA_KAFKA_STREAMS"



   }



   }



   ]
   ```
2. To send your configuration, use the [Post an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint.