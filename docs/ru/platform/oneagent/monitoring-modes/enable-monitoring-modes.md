---
title: Enable OneAgent monitoring modes
source: https://www.dynatrace.com/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes
scraped: 2026-02-28T21:13:57.469040
---

# Enable OneAgent monitoring modes

# Enable OneAgent monitoring modes

* Latest Dynatrace
* How-to guide
* 8-min read
* Published Nov 26, 2025

By default, [OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") runs in Full-Stack monitoring mode, giving you complete visibility across hosts, processes, and services. If you prefer a lighter approach, you can switch to one of the two alternative modes that focus on essential infrastructure metrics:

* Infrastructure monitoring mode
* Discovery mode

## Select a default monitoring mode

You can define a default monitoring mode before installing OneAgent. This will change the default **Full-Stack** monitoring mode on the OneAgent deployment page (for Linux, Windows, and AIX operating systems) and in the ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** app (when deploying OneAgent from the **Install OneAgent** page).

To define a default monitoring mode

1. Go to **Settings** > **Preferences** > **OneAgent default mode**.
2. Select a **OneAgent default monitoring mode** from the dropdown list.
3. Select **Save changes**.

The selected value will be set as a default value for the chosen OneAgent deployment mode.

## Enable Infrastructure monitoring mode

You can turn on Infrastructure monitoring mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Infrastructure monitoring mode during OneAgent installation, use the `--set-monitoring-mode=infra-only` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Infrastructure monitoring mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Infrastructure**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=infra-only` parameter.
* Use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to turn on Infrastructure Monitoring mode at scale.
* To download the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:host.monitoring` as the schemaId and create your configuration object using [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

### Process injection

Process injection provides you with additional data for Infrastructure Observability. Process injection is enabled by default.

If you run your OneAgent as a container with Infrastructure monitoring mode enabled, process injection will not be performed.

Infrastructure monitoring mode enables you to monitor any infrastructure component and backing service written in Java. You can monitor backing services supported by default (for example, Kafka or ActiveMQ), and you can also build your own custom [JMX and PMI extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.") for infrastructure components and use them in Infrastructure monitoring mode.

Additionally, with process injection, Infrastructure monitoring mode provides runtime metrics for:

* Java
* .NET
* Node.js
* Golang
* PHP
* Web servers such as Apache HTTP, NGINX, or Microsoft IIS.

### Disable process auto-injection

We don't recommend turning off auto-injection, but if you're required to do so due to strict security requirements, you can choose among various options. Turning off auto-injection also prevents Dynatrace from discovering vulnerabilities or live debugging in your environment, even if you enable [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") or [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace."). You can turn off automatic injection at the host or environment level.

#### Disable auto-injection for a single host

After OneAgent installation with UI

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
3. Select **Host Monitoring**.
4. Go to **Advanced settings**.
5. Turn off **ProcessAgent Injection**, then select **Save changes**.
6. Restart the monitored processes on the host.

After OneAgent installation with command line

Use the [OneAgent command line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-auto-injection-enabled=false` parameter.

If you use oneagentctl to turn off automatic injection, you won't be able to control auto-injection in Infrastructure monitoring mode using the Dynatrace web UI at **Settings > Monitoring > Monitored technologies** or [OneAgent monitoring configuration API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.").

#### Disable auto-injection for an environment

Define custom process monitoring rules

You can turn off process injection for particular process groups using custom process monitoring rules.

Custom process monitoring rules give you fine-grained control over which processes OneAgent injects into, with an approach that scales easily within large environments. You donât need to adjust your system configuration, and a few rules can cover thousands of processes.

For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").

Disable runtime metrics

You can disable the collection on JMX/PMI and runtime metrics, which will result in disabling auto-injection in Infrastructure monitoring mode.

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. In the list of supported technologies, search for the **Java/.NET/Node.js/Golang/PHP runtime metrics + WebServer metrics in Infrastructure Mode** entry.
3. Select the pencil icon ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit it and then disable it.
4. Restart all processes on your infrastructure-monitored hosts.

Disable selected extensions

You can also turn off selected extensions collecting the metrics at the environment level.

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Supported technologies

   Custom extensions

   1. In the list of supported technologies, search for technologies marked as **JMX monitoring** in the **Type** column.
   2. Select the pencil icon ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit an extension of your choice.
   3. Turn off **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   1. In the list of custom extensions, search for extensions marked as **JMX** or **PMI** in the **Extension type** column.
   2. Select the extension name of your choice.
   3. Turn off **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   The setting at the host level takes precedence over environment settings. If a host is configured to **Use host configuration** for the extension and the extension isn't activated on this host, the environment configuration won't be applied. To make sure an extension is active on a single host level:

   1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and find an infrastructure-monitored host. You can filter by **Monitoring mode: Infrastructure only**.
   2. Open the host page.
   3. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
   4. In the **Monitored technologies** table, search for extensions of type **JMX extension**, **JMX monitoring**, or **PMI extension**.
   5. Select **Edit**. Use the **Activate `<extension name>` on this host** control.

### Filter hosts by injection status



When you turn off auto-injection, you can find such hosts using the **Auto-injection** filter on the **Deployment Status** page or [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Use Dynatrace web UI

1. Go to **Deployment Status** and then select the **OneAgents** tab.
2. Select the **Filter by** box, select **Auto-injection**, and select **Disabled manually**. You can also use one of the filters below to check other reasons. Note that a filter appears only if a host with a respective status is available in your deployment.

* **Enabled**  
  Auto-injection was successfully enabled.
* **Disabled manually**  
  Auto-injection was disabled [after OneAgent installation](#after-install), either using the Dynatrace web UI or `oneagentctl`.
* **Disabled on installation**  
  Auto-injection was disabled [during OneAgent installation](#during-install).
* **Disabled on sanity check**  
  Auto-injection wasn't enabled due to a failed test performed by the OneAgent installer before OneAgent installation started. Check the OneAgent installer log for details.
* **Failed on installation**  
  Auto-injection failed due to an error during OneAgent installation. Check the OneAgent installer log for details.

Use Dynatrace API

Run the [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") call with the `autoInjection` parameter set to `DISABLED_MANUAL`. The returned payload contains the list of OneAgents with auto-injection disabled [after OneAgent installation](#after-install) via either the Dynatrace web UI or `oneagentctl`.

## Enable Discovery monitoring mode

You can turn on Discovery mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Discovery mode during OneAgent installation, use the `--set-monitoring-mode=discovery` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Discovery mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Discovery**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=discovery` parameter.

### Code-module injection

For [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") and [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.") to work in Discovery mode, code-module injection is required. Code-module injection is disabled by default.

After [turning on Discovery mode](#enable-discovery-mode), you can turn on the code-module injection for a single host.

1. Go to the settings page of the desired host and select **Host monitoring**.
2. Go to **Advanced settings**.
3. Turn on **CodeModule Injection**, then select **Save changes**.
4. Restart the monitored processes on the host.

For details on how Application Security works in Discovery mode, see [Application Security: Discovery mode](/docs/secure/application-security#discovery "Access the Dynatrace Application Security functionalities.").