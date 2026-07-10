---
title: Configuration properties and parameters of ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate
---

# Configuration properties and parameters of ActiveGate

# Configuration properties and parameters of ActiveGate

* 17-min read
* Updated on May 19, 2026

## Before you begin

Understand the basic ActiveGate configuration concepts related to the property files.

Host-based ActiveGates—that is ActiveGates Module: OTLP Ingest deployed in a conventional manner, using an installer—and containerized ActiveGates use the same configuration properties, stored in the same configuration files. However, the actual values of these properties may differ and the properties are set or modified using different mechanisms: Host-based ActiveGates are configured directly on the host where ActiveGate is running, whereas containerized ActiveGates are configured using the configuration mechanism for your cloud platform.

* [How to deploy and configure a containerized ActiveGate in Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container "Deploy a containerized ActiveGate.")

## Basic rules for working with ActiveGate configuration

### ActiveGate configuration files

Many ActiveGate configuration settings (for example, connectivity and proxy settings, ciphers, or memory dump settings), are stored in the `config.properties` and `custom.properties` properties files, which are located in the **[ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")**.
The properties listed in the property files are applicable for both Environment ActiveGates and Cluster ActiveGates.

The `config.properties` and `custom.properties` files are divided into **sections**. Each section name is enclosed in square brackets, for example:

```
[collector]



MSGrouter = true



restInterface = true



DumpSupported = false
```

### config.properties

The `config.properties` configuration file contains ActiveGate's default installation settings and is not customizable.

This configuration file is overwritten during each update of ActiveGate.

### custom.properties

Settings stored in `custom.properties` override the corresponding settings in `config.properties`, and the file is copied to the new version of ActiveGate during the update.

The configuration files are split into `[sections]`, which are indicated in square brackets.  
To specify customized settings in `custom.properties`, enter section names and include the appropriate properties within these sections.

You can use the `config.txt` file as a reference when you add your custom settings to the `custom.properties` file. The `config.txt` file, which is also located in the ActiveGate configuration directory, is not used by ActiveGate, however it contains a reference list of possible configuration properties.
Alternatively, you can first locate the relevant section in the `config.properties` file and then copy the section title along with the names of the desired properties into `custom.properties`.  
After that, you can modify the entries in the section, as appropriate.

### launcheruserconfig.conf

ActiveGate launcher is a watchdog process that starts a Java virtual machine for your ActiveGate.
The launcher configuration is stored in the `launcheruserconfig.conf` file, in the **[ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")**. It contains launcher properties and parameters that are passed to the Java virtual machine.

For the Remote Plugin Module (RPM), the `launcheruserconfig.conf` file should be specifically placed in the `/var/lib/dynatrace/remotepluginmodule/agent/conf/` directory.

The `launcheruserconfig.conf` file is preserved during ActiveGate updates.

### Restart ActiveGate

If you modify your ActiveGate configuration, you must [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to put your changes into effect.

## Configure ActiveGate using `agctl`

ActiveGate version 1.333+

Starting with ActiveGate version 1.333, you can use the `agctl` command-line interface to manage ActiveGate configuration. The `agctl` tool simplifies configuration management by providing:

* **Dedicated commands** for common configuration tasks such as setting proxy endpoints, managing SSL certificates, configuring trust stores, and assigning ActiveGate groups.
* **Generic property command** that allows you to configure any property in the `custom.properties` file using the [agctl property](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Learn how to use agctl to configure and manage ActiveGate from the command line") command for properties that don't have dedicated commands.

For details on all available commands, parameters, and examples, see [agctl command-line interface](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface "Learn how to use agctl to configure and manage ActiveGate from the command line").

## Example usage of `agctl` to manage ActiveGate configuration

ActiveGate version 1.333+

In this example, let's change the log data queue path on a host-based ActiveGate.

For a host-based Environment or Cluster ActiveGate, you can change the path used for the log data queue with [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Learn how to use agctl to configure and manage ActiveGate from the command line"). The following steps use `/var/disk_queue` as an example for the new path.

1. Get familiar with the [`agctl` command-line interface prerequisites](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#prerequisites "Learn how to use agctl to configure and manage ActiveGate from the command line").
2. Connect to the host via SSH.
3. Stop the ActiveGate service:

```
systemctl stop dynatracegateway
```

4. Read the current path:

```
agctl property get --section=generic_ingest --key=disk_queue_path
```

5. Make sure the target directory `/var/disk_queue` exists, is writable, and has at least `disk_queue_max_size_mb` MB of free disk space available.
6. Change the path:

```
agctl property set --section=generic_ingest --key=disk_queue_path --value=/var/disk_queue
```

7. Optional: remove the directory pointed to by the old path.
8. Start the ActiveGate service:

```
systemctl start dynatracegateway
```

## ActiveGate memory limits

Memory usage limits for ActiveGate can be specified in the launcher configuration file `launcheruserconfig.conf` with the following properties:

* `-java.xmx.relative_part`—percentage of available RAM
* `-java.xmx.absolute_part`—absolute value of memory size, in MB

The configuration may include any combination of those properties, and the resulting memory limit is the sum of absolute part and relative part (calculated based on the available RAM).

**Examples:**

```
# Xmx = 0 MB + 83% of available RAM



-java.xmx.absolute_part=0



-java.xmx.relative_part=83
```

```
# Xmx = 2000 MB + 83% of available RAM



-java.xmx.absolute_part=2000



-java.xmx.relative_part=83
```

```
# Xmx = 2000 MB + 0 MB



-java.xmx.absolute_part=2000



-java.xmx.relative_part=0
```

## ActiveGate heartbeat port range

The ActiveGate launcher monitors the ActiveGate process on a local heartbeat port. This port is chosen by the launcher, from a pre-defined range of ports, as specified in the launcher configuration. The launcher finds a free port, in the given range, and then passes the port number to the ActiveGate process.

By default, the launcher will utilize ports above 50000 for heartbeat monitoring. Certain deployments may require you to configure different ports for this purpose. To specify the port range that the ActiveGate launcher should use, add or modify the property `-healthcheck.heartbeat.portrange`, in the launcher configuration file `launcheruserconfig.conf`, as in the example below.

```
-healthcheck.heartbeat.portrange=60100:60200
```

## Custom parameters for the ActiveGate Java process

To pass custom parameters to the ActiveGate Java process, specify the parameters in the launcher configuration file `launcheruserconfig.conf`:

* All lines after `-arguments_section.jvm` are passed as arguments to the JVM. This way, by supplying `-D` options, you can specify arguments for the ActiveGate.

For example:

```
# Xmx settings 80% of available RAM + 0 MB



-java.xmx.absolute_part=0



-java.xmx.relative_part=83



-healthcheck.heartbeat.portrange=60100:60200



-arguments_section.jvm



-Dsomecustomproperty=value
```

## ActiveGate modules

Different functional features provided by ActiveGate are referred to as **[modules](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.")**. When you are installing ActiveGate for a specific [purpose](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate."), a different set of modules is installed or enabled.

A module is active if the corresponding configuration property is listed with value `true` in the configuration section dedicated to the module. Note, however, that you can't enable all modules using `custom.properties` simply by changing the value of a property: if you installed your ActiveGate to serve as a private Synthetic location or to monitor mainframe, and you need to change your ActiveGate purpose, you have to reinstall the ActiveGate.  
Active modules are listed on the [Deployment status](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Configure Environment ActiveGate automatic updates---update mode, target version, and update windows---and download or install manually.") page.

Each module has a corresponding section in the configuration

In addition to configuration sections dedicated to specific ActiveGate functionality, each ActiveGate module has its own section in the ActiveGate configuration files. Settings specified in this section apply specifically to that module. This applies, for example, to proxy settings. However, not all settings can be repeated in this way and specified for a module: Each module section has only a limited number of options that it accepts. **Do NOT copy configuration settings between sections, unless specifically instructed to do so.**

### Manage modules using `agctl`

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Learn how to use agctl to configure and manage ActiveGate from the command line") to enable or disable ActiveGate modules.

After enabling or disabling modules with `agctl`, you must [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

#### Enable modules

```
# Enable a single module



agctl modules enable metrics_ingest



# Enable multiple modules (comma-separated, no spaces)



agctl modules enable MSGrouter,metrics_ingest,otlp_ingest
```

#### Disable modules

```
# Disable a single module



agctl modules disable synthetic



# Disable multiple modules



agctl modules disable aws_monitoring,azure_monitoring
```

## Module: AWS

AWS monitoring  
**Section: [aws\_monitoring]**

| Property | Description |
| --- | --- |
| `aws_monitoring_enabled` | Enables [AWS monitoring](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.") module. Possible values: `true` or `false`. |
| `aws_default_region` | Specify the default region used by [AWS monitoring](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.") module. Possible values: valid AWS Regions codes. For example: `us-east-1` |
| `aws_client_regions` | Specify regions used by [AWS monitoring](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.") module. Possible values: list of valid AWS Regions codes, separeated by `;`. For example: `us-east-1;eu-central-1` |

## Module: Azure

Microsoft Azure monitoring  
**Section: [azure\_monitoring]**

| Property | Description |
| --- | --- |
| `azure_monitoring_enabled` | Enables [Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.") module. Possible values: `true` or `false`. |

## Module: Cloud Foundry

Cloud Foundry monitoring  
**Section: [cloudfoundry\_monitoring]**

| Property | Description |
| --- | --- |
| `cloudfoundry_monitoring_enabled` | Enables [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.") module. Possible values: `true` or `false`. |

This section can contain proxy settings for communication with Cloud Foundry. If this section contains `proxy-off = true`, then there is no proxy for communication with Cloud Foundry. If it contains the `proxy-host` property, then this is the proxy to be used for Cloud Foundry monitoring, rather than the proxy specified in `[http.client.external]`.

ActiveGate version 1.247 and earlier If you have a `[cloudfoundry_monitoring]` section in your `custom.properties` file, you also need to have an `[http.client.external]` section, where you should specify all the remaining communication parameters that are to be used for Cloud Foundry communication.

[Set up proxy only for Cloud Foundry monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-cloud-foundry-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Module: Kubernetes

Kubernetes Platform Monitoring  
**Section: [kubernetes\_monitoring]**

| Property | Description |
| --- | --- |
| `kubernetes_monitoring_enabled` | Enables [Kubernetes Platform Monitoring](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.") module. Possible values: `true` or `false`. |

This section can contain proxy settings for communication with Kubernetes, along with other settings related to fine-tuning communication settings for Kubernetes Platform Monitoring.  
If this section contains `proxy-off = true`, then there is no proxy for communication with Kubernetes. If it contains the `proxy-host` property, then this is the proxy to be used for Kubernetes Platform Monitoring, rather than the proxy specified in `[http.client.external]`.

ActiveGate version 1.247 and earlier If you have a `[kubernetes_monitoring]` section in your `custom.properties` file, then you also need to have an `[http.client.external]` section, where you should specify all of the remaining communication parameters to be used for Kubernetes communication.

[Set up proxy only for Kubernetes Platform Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-kubernetes-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Module: Log Monitoring

**Section: [log\_analytics\_collector]**

| Property | Description |
| --- | --- |
| `log_analytics_collector_enabled` | Enables [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") module. Possible values: `true` or `false`. |

**Section: [generic\_ingest]**

Specifically for Log Monitoring, when configuring Log ingestion API, you can customize the log data queue properties. You can specify the temporary folder where the queued log data will be stored. The default is the temporary folder currently configured on your system (see [ActiveGate directories](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")). You can also change the maximum size of the queue that is used in that folder (the default size is 300 MB).

| Property | Default value | Description |
| --- | --- | --- |
| `disk_queue_path` | Current system-wide temporary folder | Specifies the path to the temporary folder where the queued log data will be stored. |
| `disk_queue_max_size_mb` | 300 MB | Specifies the maximum size of queued log data that can be stored in the temporary folder. |

## Module: VMware

VMware monitoring  
**Section: [vmware\_monitoring]**

| Property | Description |
| --- | --- |
| `vmware_monitoring_enabled` | Enables [VMware monitoring](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.") module. Possible values: `true` or `false`. |

## Module: Database insights

Oracle database insights  
**Section: [dbAgent]**

| Property | Description |
| --- | --- |
| `dbAgent_enabled` | Enables [Oracle database insights](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Learn how to extend your database monitoring to the database infrastructure layer.") module. Possible values: `true` or `false`. |

## Module: Extensions

**Section: [extension\_controller]**

| Property | Description |
| --- | --- |
| `extension_controller_enabled` | Enables the Extensions framework. Possible values: `true` or `false`. |

## Module: zRemote

Install the zRemote module for z/OS monitoring  
**Section: [zremote]**

| Property | Description |
| --- | --- |
| `zremote_enabled` | Enables the [zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring."). Possible values: `true` or `false`. |

## Module: Synthetic

Synthetic monitors from private Synthetic locations  
**Section: [synthetic]**

Proxy settings for Synthetic Monitoring. If this section contains `proxy-off = true`, then there is no proxy for Synthetic Monitoring. If it contains the `proxy-host` property, then this is the proxy to be used for Synthetic Monitoring, rather than the proxy specified in `[http.client.external]` (or in `[http.client]`, if `[http.client.external]` is not defined).

If you have a `[synthetic]` section in your `custom.properties` file, you can have an `[http.client.external]` section, where you should specify all of the remaining communication parameters to be used for Synthetic Monitoring. Alternatively, you can specify the remaining communication settings in the `[http.client]` section.

ActiveGate version 1.247 and earlier However, if you do create the `[http.client.external]` section, you have to specify all of the communication parameters there. Otherwise, the communication parameters for monitored environments (Cloud Foundry, Kubernetes, or Synthetic Monitoring) will revert to their factory defaults.

To learn more about the proxy-related properties for a Synthetic-enabled ActiveGate, see [Set up a proxy for private synthetic monitoring](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.").

Note that changing the `synthetic_enabled` property only works if you installed the ActiveGate to [run Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate#synthetic "Understand the basic concepts related to ActiveGate."). If you installed the ActiveGate to [route traffic, monitor cloud environments, or monitor remote technologies with extensions](/managed/ingest-from/dynatrace-activegate#route "Understand the basic concepts related to ActiveGate.") or [monitor mainframe](/managed/ingest-from/dynatrace-activegate#mainframe "Understand the basic concepts related to ActiveGate."), you have to reinstall the ActiveGate to use it for Synthetic Monitoring. For more information, see [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

If a comma (`,`) is part of a value, you need to add an escape backslash (`\`) before the comma.

Example: `proxy-password = foo\,bar`

| Property | Default value | Description |
| --- | --- | --- |
| `synthetic_enabled` | `false` in the **Default** deployment mode  `true` in the **Synthetic monitoring** deployment mode | Enables the ActiveGate to execute monitors from private Synthetic locations. |
| `synthetic_autoinstall` | `true` to automatically update the Synthetic engine | Automatically set to `true` at installation time for Synthetic-enabled ActiveGates. |
| `proxy-server` | unset | Proxy server address |
| `proxy-port` | unset | Proxy port (numeric) |
| `proxy-user` | unset | Proxy user name (optional) |
| `proxy-password` | unset | Proxy password (optional)  The password provided in the `proxy-password` property  is obfuscated following ActiveGate restart and the obfuscated password  is stored in the `proxy-password-encr` property. **Note**: A comma character, when intended to be a part of a value, should be escaped with a single backslash. For example, `proxy-password = foo\,bar`. |
| `proxy-off` | unset | Disable proxy communication between ActiveGate and tested resource. |
| `proxy-non-proxy-hosts` | unset | Do not use proxy when communicating with these hosts. |
| `chromium_repo` | unset  Specify the custom browser package repository on the HTTP server. Example: `https://172.18.0.100/chromium-repo` Only works if both `synthetic_autoinstall` and `synthetic_autoupgrade_chromium` are `true`. | Enables autoupdate of the browser from the [custom repository](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Learn how to create a private location for synthetic monitoring."). |

We recommend that you not edit the value of the `synthetic_autoupgrade_chromium` property in `custom.properties` because your changes might be overwritten.

`synthetic_autoupgrade_chromium` for autoupdating the browser can be defined at the location level (for locations with Environment ActiveGates) either [via the web UI](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser "Analyze and manage capacity usage at your private Synthetic locations.") or by using the [PUT a location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location "Update a private synthetic location via the Synthetic v2 API.") API call of the Synthetic locations API v2. For Cluster ActiveGates, you can configure this property via the [PUT a location (Dynatrace Managed)](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location "Update a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.") API call of the Cluster API v2. This property is not defined for ActiveGates that haven't been assigned to a location. For Activates assigned to a location, the default value is `true`.

## Module: Beacon forwarder

Using ActiveGate for Real User Monitoring  
**Section: [beacon\_forwarder]**

| Property | Description |
| --- | --- |
| `beacon_forwarder_enabled` | Enables the [Beacon forwarder module](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). Possible values: `true` or `false`. |

## Module: HTTP Metric API

Metric ingestion: a simple way to push any custom metrics to Dynatrace  
**Section: [metrics\_ingest]**

| Property | Description |
| --- | --- |
| `metrics_ingest_enabled` | Enables HTTP Metric API module which facilitates [metric ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."). Possible values: `true` or `false`. |

## Module: Memory dumps

Triggering and downloading of memory dumps  
**Section: [collector]**

| Property | Description |
| --- | --- |
| `DumpSupported` | Enables the [memory dumps module](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate."). Possible values: `true` or `false`. |

When your application experiences memory leaks or high object churn, it’s important that you get memory dumps so you can analyze these issues. In production environments, this is often a challenge when you can’t log into the environment and you have no other means of triggering memory dumps. Dynatrace enables you to both trigger and securely download memory dumps to the analysis tool of your choice.  
See [Configure ActiveGate for memory dump storage](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.").

## Module: OneAgent routing

ActiveGate knows about the runtime structure of your Dynatrace environment and routes messages from OneAgents to the correct server endpoints. It handles message routing, buffering, compression, authentication and accessing of sealed networks.  
**Section: [collector]**

| Property | Description |
| --- | --- |
| `MSGrouter` | Enables the OneAgent routing module, which routes of OneAgent and other ActiveGate traffic through Dynatrace. Possible values: `true` or `false`. |

## Module: OTLP Ingest

**Section: [otlp\_ingest]**
This module creates endpoints on the ActiveGate that can receive OpenTelemetry trace data (traces and spans), metrics, and logs in OTLP format. For more information, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

| Property | Description |
| --- | --- |
| `otlp_ingest_enabled` | Enables the OTLP ingest module, which facilitates OpenTelemetry [traces](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") and [metrics](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") ingest. Possible values: `true` or `false`. |

## Module: REST API

**Section: [collector]**   
You can use an ActiveGate to access the [Dynatrace API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API."). ActiveGate supports calls to all the Dynatrace API configuration and environment endpoints in both, v1 and v2 versions. To access the Dynatrace API using ActiveGate, use a URL in the following format: `https://{your-ActiveGate-domain}/e/{your-environment-id}/api/...`

| Property | Description |
| --- | --- |
| `restInterface` | Enables the REST API module, which facilitates access to Dynatrace API using REST. Possible values: `true` or `false`. |

## Module: debugging

**Section: [debugging]**   
You can use an ActiveGate to access the code-level data that you need to troubleshoot and debug quickly, in any environment, from development to production.

| Property | Description |
| --- | --- |
| `debugging_enabled` | Enables the Dynatrace Live Debugger module. Possible values: `true` or `false`. |

## Network zone

**Section: [connectivity]**

| Property | Default value | Description |
| --- | --- | --- |
| `networkZone` | unset | Defines the [network zone](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") to which the ActiveGate belongs. An ActiveGate can belong to only one network zone. The name of a network zone is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a network zone name. The length of the string is limited to 256 characters. ActiveGate restart is required after adding or changing this parameter. After restart, a network zone is automatically created in Dynatrace. |
| `bindToNetworkInterface` | unset | By default, ActiveGate listens on all available interfaces. If you want ActiveGate to listen only to a selected interface, you need to configure this property with the IP address assigned to the network interface. |

### Manage network zone using `agctl`

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#network-zone "Learn how to use agctl to configure and manage ActiveGate from the command line") to configure the network zone for your ActiveGate:

```
agctl network-zone set production-zone
```

After configuring the network zone with `agctl`, you must restart ActiveGate for the changes to take effect. See [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Alternatively, to modify network zone assignment centrally from the Dynatrace Cluster, you can use [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify network zone** action).

## Group

**Section: [collector]**

| Property | Default value | Description |
| --- | --- | --- |
| `group` | unset | [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") |

### Manage ActiveGate group using `agctl`

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#group "Learn how to use agctl to configure and manage ActiveGate from the command line") to assign your ActiveGate to a group:

```
agctl group set my.group
```

After configuring the ActiveGate group with `agctl`, you must restart ActiveGate for the changes to take effect. See [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Alternatively, to modify ActiveGate group assignment centrally from the Dynatrace Cluster, you can use [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify ActiveGate group** action).

## ActiveGate file cache

The ActiveGate file cache reduces traffic between the ActiveGate and the Dynatrace Cluster by allowing OneAgents to download automatic updates from the ActiveGate rather than the Cluster.

The file cache is activated automatically when ActiveGate is installed or updated. However, activation occurs only when the **minimum space requirement of 512 MB** is met. If the minimum space requirement is not met, caching is automatically deactivated.

The file cache can be fine-tuned or deactivated in ActiveGate configuration, in the `custom.properties` file:

**Section: [generic\_filecache]**

| Property | Default value | Description |
| --- | --- | --- |
| `generic_filecache_enabled` | `true` | Enables or disables ActiveGate file cache. Possible values: `true` or `false`. |
| `generic_filecache_path` | `<ActiveGate temporary directory>/generic_filecache` | Path of the ActiveGate file cache directory. The directory will be created if it does not exist (if the file permissions allow it). |
| `generic_filecache_size` | `2147483648` (2 GB) | The size of the ActiveGate file cache in bytes.  ActiveGate file cache will use no more space than specified in the configuration. If available space is less than the size specified in the configuration, ActiveGate will use the available space. |
| `generic_filecache_max_age` | `1209600000` (14 days) | The maximum file age for files stored in the ActiveGate file cache, in milliseconds. File age is counted from the time that a file was last used (not from upload/creation time).  If a file is not used for the configured maximum age, the file will be automatically removed. Files are also removed from the cache before their maximum age if there is insufficient space for new files. The LRU (least recently used) files are removed first. |

If the value contains a comma character, it must be escaped with a single backslash. For example, `proxy-password = foo\,bar`.

## Section: [com.compuware.apm.webserver]

| Property | Default value | Description |
| --- | --- | --- |
| `port-ssl` | `9999` | The port on which the ActiveGate listens for traffic from OneAgent—used for the HTTPS connection. You can configure this using the [agctl ssl-port](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#ssl-port "Learn how to use agctl to configure and manage ActiveGate from the command line") command. If you need to change the port value, see [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") and [Extension Execution Controller custom configuration](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration "Configure the Extension Execution Controller (EEC)."). |
| `port` | unset | The port on which the ActiveGate listens for traffic from OneAgent—used for the HTTP connection. It is disabled by default. On Linux, a value > 1024 is recommended to ensure no root privileges are required. |
| `ssl-protocols` | `TLSv1.2`, `TLSv1.3` | Supported SSL protocols. Can be one or a comma-separated list of values. Note that specifying a particular version does not automatically imply support for all the previous/lower versions—so you need to specify each version explicitly. The allowed values are `TLSv1.2` and `TLSv1.3` |
| `excluded-ciphers` | unset | A list of excluded ciphers. Ciphers are defined by a substring matching at least a part of the cipher name, for example: `excluded-ciphers = TLS_RSA_WITH,SHA$,TLS_ECDH` |
| `certificate-file` | unset | Path of the `PKCS#12` file containing certificates to be used by the ActiveGate web server. Also see [Configuration of custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate."). |
| `certificate-password` | unset | Password for the certificate file. |
| `certificate-alias` | unset | Friendly name of the certificate in the `PKCS#12` file. |

#### Operating over HTTPS vs HTTP

By default, ActiveGate operates in a secure way, by servicing incoming requests using HTTPS. This is specified by the `port-ssl` configuration property, which can be customized in the `custom.properties` file. However, if you want ActiveGate to use HTTP, you must specify the `port` property in the `custom.properties`.

Note that the secure way is the default and recommended one. However, you might want to choose the HTTP option for performance reasons. For example, if you have a load balancer installed in front of a Cluster ActiveGate and if the load balancer terminates incoming external SSL connections (see [the third deployment scenario](/managed/managed-cluster/basics/managed-deployments#scenario-3-integration-with-existing-it-landscape "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.")).

## Section: [http.client]

Communication settings used for AWS/VMware/Azure monitoring and for communicating with the Dynatrace Cluster (unless overridden in `[http.client.internal]`).
In particular, this section contains configuration properties related to proxy settings and connection timeouts.

[Specify common proxy settings for Dynatrace Cluster communication and AWS/VMware/Azure monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#proxy-for-cluster-aws-vmware-azure "Learn how to configure ActiveGate properties to set up a proxy.").

## Section: [http.client.internal]

Settings specific to communication with the Dynatrace Cluster only.  
In particular, this section can contain configuration properties related to proxy settings and connection timeouts.

If this section contains proxy-off = true, then there is no proxy for communication with the Dynatrace Cluster. If it contains the proxy-host property, then this is the proxy to be used for communication with the Dynatrace Cluster.

If this section does not exist, communication with the Dynatrace Cluster is defined by the settings in the `[http.client]` section.

ActiveGate version 1.247 and earlier If the `[http.client.internal]` section does exist in which a particular communication setting is not listed, then, for the purpose of communicating with the Dynatrace Cluster, the value of that setting is **assumed to be its factory default** (it is **not** inherited from `[http.client]`).

[Set up proxy only for Dynatrace Cluster communication](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-dynatrace-cluster-communication "Learn how to configure ActiveGate properties to set up a proxy.")

## Section: [http.client.external]

Communication settings for specific modules: Cloud Foundry, Kubernetes, and also for Synthetic Monitoring.  
In particular, this section can contain configuration properties related to proxy settings and connection timeouts.

If this section contains `proxy-off = true`, then there is no proxy for the modules. If it contains the `proxy-host` property, then this is the proxy to be used for the modules.

ActiveGate version 1.247 and earlier

Communication settings specified in `[http.client]` are **not always** used as defaults for the modules: If a particular communication setting is **not** specified in `[http.client.external]`, then that setting—for Cloud Foundry, Kubernetes or Synthetic Monitoring—will revert to its factory default value, rather than to the value specified in `[http.client]`.

Similarly, the entire `[http.client.external]` section does not exist, then all of the communication settings for Kubernetes and Cloud Foundry will revert to their factory default values; however, settings for Synthetic Monitoring will assume values as specified in the `[http.client]` section.

[Specify common proxy settings for Cloud Foundry, Kubernetes, and Synthetic Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#specify-common-proxy-settings-for-cloud-foundry-kubernetes-and-synthetic-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Section: [connectivity]

| Property | Default value | Description |
| --- | --- | --- |
| `reverseDnsLookupEnabled` | `true` | ActiveGate version 1.255+ Enabled or disables Fully Qualified Domain Name resolution using reverse DNS lookup. When enabled and standard FQDN resolution produces no result, the attempt to resolve the name using reverse DNS lookup is made. ActiveGates that were previously depicted by the IP address may now be presented by the hostname. Possible values: `true` or `false`. |

## Trusted root certificate

**Section: [collector]**

| Property | Default value | Description |
| --- | --- | --- |
| `trustedstore` | unset | Your trusted keystore (optional). The property `trustedstore` should contain the path to the file holding trusted certificates. That path should be relative to the ActiveGate SSL directory. Please also see [Trusted root certificates for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections."). |
| `trustedstore-exclusive` | unset | When set to `true`, ActiveGate will no longer merge the built-in trust store (shipped with JRE) with the custom trust store defined by you in `trustedstore`. The custom trust store will be the only trust store used for communication. |
| `trustedstore-password` | `changeit` | Password of your trusted keystore (optional) which is encrypted during ActiveGate start. The obfuscated password is then stored in `trustedstore-password-encr`. |
| `trustedstore-type` | `pkcs12` | Java default format of key and certificate databases (optional). |