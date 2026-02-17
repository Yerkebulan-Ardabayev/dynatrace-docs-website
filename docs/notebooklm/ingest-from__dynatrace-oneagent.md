# Dynatrace Documentation: ingest-from/dynatrace-oneagent

Generated: 2026-02-17

Files combined: 61

---


## Source: adaptive-traffic-management.md


---
title: Adaptive Traffic Management for distributed tracing
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management
scraped: 2026-02-16T21:14:21.300703
---

# Adaptive Traffic Management for distributed tracing

# Adaptive Traffic Management for distributed tracing

* Latest Dynatrace
* Overview
* 1-min read
* Published Dec 15, 2022

Adaptive Traffic Management is the intelligent sampling mechanism used in Dynatrace. It ensures trace data captured by OneAgent doesn't exceed the trace volume included with Full-Stack monitoring, while maintaining a statistically valid dataset.

[### Adaptive Traffic Management concepts

Understand different terms related to Adaptive Traffic Management, such as **Full-Stack included trace volume** or **adaptive trace sampling rate**.](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-concepts "Basic concepts related to Adaptive Traffic Management.")[### Adaptive Traffic Management for Dynatrace Platform Subscription (DPS)

Discover Adaptive Traffic Management for Dynatrace Platform Subscription (DPS) and learn how to monitor, increase, or decrease the trace data capture rate. With Dynatrace Platform Subscription (DPS), you can extend trace ingest for Full-Stack to increase the trace capture rate. This requires your explicit opt-in. In its default configuration Adaptive Traffic Management guarantees that no extend trace ingest is being charged.](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-saas-dps "Learn how Adaptive Traffic Management works with Dynatrace Platform Subscription (DPS) and how it manages trace sampling for Full-Stack monitored hosts and applications.")[### Adaptive Traffic Management for Dynatrace classic license

Discover Adaptive Traffic Management for Dynatrace classic license and learn how to monitor, increase, or decrease the trace data capture rate.](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-saas-classic "Learn how Adaptive Traffic Management works with Dynatrace classic license and how to adjust trace sampling for HTTP and RPC requests.")


---


## Source: customize-oneagent-installation-on-aix.md


---
title: Customize OneAgent installation on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix
scraped: 2026-02-17T04:53:16.446054
---

# Customize OneAgent installation on AIX

# Customize OneAgent installation on AIX

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Sep 19, 2018

The AIX installer can be used with command-line parameters when you can't use the default settings. Note that all parameters listed below are optional.

## Passing installation parameters

For example:

```
â-set-host-group=My.HostGroup_123-456
```

## Removed installation parameters

Convert to the newer `--set-param=<value>` parameters now. The equivalent `PARAM=<value>` parameters are not supported by the OneAgent installer starting with version 1.213.

| Removed `PARAM=<value>` parameter | New `--set-param=<value>` parameter |
| --- | --- |
| `SERVER` | `--set-server` |
| `TENANT` | `--set-tenant` |
| `TENANT_TOKEN` | `--set-tenant-token` |
| `PROXY` | `--set-proxy` |
| `HOST_GROUP` | `--set-host-group` |
| `DISABLE_SYSTEM_LOGS_ACCESS` | `--set-system-logs-access-enabled` |

## Installation path

The `INSTALL_PATH` parameter allows installation to a different directory. For example:

```
INSTALL_PATH=/data/dynatrace/agent
```

The installer creates the symbolic link `/opt/dynatrace/oneagent` > `/data/dynatrace/agent` and the OneAgent installation files are placed in the specified directory (in this example, `/data/dynatrace/agent`). Note that this symbolic link needs to be removed manually after OneAgent is uninstalled.

The `INSTALL_PATH` parameter doesn't control the OneAgent [log and configuration files](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.") directories. To customize the log path, use the [`LOG_PATH`](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#log-path "Learn how you can use AIX installer with command line parameters.") parameter.

### Custom directory requirements

Make sure that your custom installation directory path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be an already existing symbolic link.
* The value must not be a child directory of `/var/lib/dynatrace`.

## Log path

OneAgent version 1.213

Default value: `/var/log/dynatrace/oneagent`

The `LOG_PATH` parameter allows you to customize your OneAgent log directory, which is `/var/log/dynatrace/oneagent` by default. For example:

```
LOG_PATH=/data/dynatrace/logs
```

### Custom directory requirements

Make sure that your custom log path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be an already existing symbolic link.
* The value must not be a child directory of `/var/lib/dynatrace`.

The value must not point to `/opt/dynatrace/oneagent/log`, which is the default log location for OneAgent versions earlier than 1.203.

### Changing location

You can only customize the log directory path during OneAgent installation.

To change the path, uninstall and re-install OneAgent, specifying the desired path using the command-line parameter.

## Data storage

OneAgent version 1.199

Default value: `/var/lib/dynatrace/oneagent/datastorage`

The `DATA_STORAGE` parameter allows you to define a directory dedicated to storing large runtime data produced by OneAgent in full-stack monitoring mode, such as crash reports or memory dumps.

For example:

```
DATA_STORAGE=/data/dynatrace/runtime
```

## Communication endpoint

**Default value**: `environment specific`

The address of the OneAgent communication endpoint, which is a Dynatrace component that OneAgent sends data to. Depending on your deployment, it can be a Dynatrace Cluster or ActiveGate. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value. To change it, use the IP address or a name. Add the port number following a colon.

To set the communication endpoint, pass it as a parameter value:

```
--set-server=https://100.20.10.1:443
```

OneAgent and Dynatrace Cluster automatically maintain a working connection. If an endpoint detail changes, the cluster notifies OneAgent of the change and OneAgent automatically updates the endpoint you set using the `--set-server` to the new working value.

To change the endpoint after installation, use `--set-server` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Environment ID

**Default value**: `environment specific`

The Dynatrace [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") you received with your activation email. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value. If you're selling Dynatrace-based services, use this option to set your customers' IDs from the pool of IDs you purchased from Dynatrace.

To set the environment ID, pass it as a parameter value:

```
--set-tenant=mySampleEnv
```

To change the tenant after installation, use `--set-tenant` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Token

**Default value**: `environment specific`

The tenant token that is used for authentication when OneAgent connects to the communication endpoint to send data. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value.

To set a token, pass it as a parameter value:

```
--set-tenant-token=abcdefghij123456
```

See [Access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") to learn how to obtain a token.

To change the tenant token after installation, use `--set-tenant-token` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Network zones

**Default value**: `unset`

To learn about network zone naming rules and other reference information, see [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

Use the `--set-network-zone` parameter to instruct OneAgent to communicate via the specified network zone:

```
--set-network-zone=your.network.zone
```

To change or clear the network zone assignment after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify network zone** action).

Alternatively, you can use `--set-network-zone` on the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Proxy

**Default value**: `unset`

The address of the proxy server. Use the IP address or a name, and add the port number following a colon. For an authenticating proxy you can specify a username and password like this `username:password@172.1.1.128:8080` where both username and password need to be URL encoded.

To set a proxy, pass it as a parameter value:

```
--set-proxy=172.1.1.128:8080
```

Dynatrace also supports IPv6 addresses.

To change or clear the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Port range

Deprecated

Starting with OneAgent version 1.301, OneAgent doesn't use the TCP ports for its own inter-process communication. In case OneAgent occupies your applications' ports, upgrade OneAgent to version 1.301+.

**Default value**: `50000:50100`

Watchdog is a binary used for starting and monitoring OneAgent monitoring processes:

* `oneagentos`âoperating system monitoring
* `oneagentplugin`âmonitoring using [OneAgent extensions](/docs/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`âmonitoring using local [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`â[Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`â[network monitoring](/docs/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Use the `--set-watchdog-portrange=<arg>` parameter to change the watchdog listening port range to `<arg>`. The `<arg>` must contain two port numbers separated by a colon (`:`). For example `50000:50100`. The maximum supported port range is from 1024 to 65535. The port range must cover at least 4 ports. The port number starting the range must be lower. For example:

```
--set-watchdog-portrange=50000:50100
```

To change port range after installation, use `--set-watchdog-portrange` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#portrange "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Auto-update

Use the `--set-auto-update-enabled=<arg>` to enable or disable OneAgent auto-update. For example:

```
--set-auto-update-enabled=true
```

After you set the parameter to `false`, you won't be able to control OneAgent automatic updates using the Dynatrace web UI at **Settings** > **Updates** > **OneAgent updates**.

## Host group

**Default value**: `unset`

The name of a group you want to assign the host to. For details, see [Organize your environment using host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Host group string requirements:

* Can contain only alphanumeric characters, hyphens, underscores, and periods
* Must not start with `dt.`
* Maximum length is 100 characters

To assign a host to the host group, pass the host group name as a parameter value:

```
--set-host-group=My.HostGroup_123-456
```

To remove the host from a group, you need to [uninstall OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.") or pass an empty value `--set-host-group=""` when running a OneAgent update. You can't remove the host from a group using the `HOST_GROUP` parameter when updating OneAgent.

To change or clear the host group assignment after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host group** action).

Alternatively, you can use `--set-host-group` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Monitoring mode

**Default value**: `fullstack`

Activates one of the OneAgent monitoring modes:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

To enable a specific monitoring mode, set the `--set-monitoring-mode` parameter to one of the following values:

* `fullstack`
* `infra-only`
* `discovery`

For example:

```
--set-monitoring-mode=infra-only
```

To change the monitoring mode after installation, use `--set-monitoring-mode` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#infrastructure-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") or set it using the [Host settings](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") page.

## Custom host name

**Default value**: `unset`

Use the `--set-host-name` to override an automatically detected host name. The host name value must not contain the `<`, `>`, `&`, `CR` (carriage return), and `LF` (line feed) characters and the maximum length is 256 characters.

This command adds a custom host name to display in the UI, but the detected host name is not changed. For details, see [Set custom host names](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

To set the host name:

```
--set-host-name=myhostname
```

To change the host name after installation, use `--set-host-name` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Custom host metadata

**Default value**: `unset`

Once configured, custom metadata is displayed as a set of properties at the bottom of the **Properties and tags** section of the host overview page. The property values must not contain the `=` (except key-value delimiter) and whitespace characters. The maximum length is 256 characters including the key-value delimiter.

To add or change host properties:

```
--set-host-property=AppName --set-host-property=Environment=Dev
```

You can add or change more than one property in the same command.

To change the host metadata after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select **modify host properties** action).

Alternatively, you can use `--set-host-property` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Custom host tags

**Default value**: `unset`

Once configured, the tags are displayed at the top of the **Properties and tags** section of the host overview page. The property values must not contain the `=` (except key-value delimiter) and whitespace characters. The maximum length is 256 characters including the key-value delimiter.

To add or change host tags:

```
--set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk
```

You can add or change more than one tag in the same command. It is allowed to define tags with the same key but different values.

To change the host tags after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host tags** action).

Alternatively, you can use `--set-host-tag` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Host ID source

**Default value**: `auto`

Available on all supported platforms for OneAgent version 1.223+. For OneAgent version 1.221 and earlier, this feature is supported only for Citrix Virtual Apps and Desktops.

It's particularly important to keep your host ID static in dynamic virtual environments where hosts are recreated on a daily basis.

To **define the source for host ID generation**, use `--set-host-id-source` and set it to one of the predefined values:

* `auto` â Let Dynatrace generate the host ID automatically
* `ip-addresses` â Generate host ID based on the host IP address
* `mac-addresses` â Generate host ID based on the host's NIC MAC address
* `fqdn` â Generate host ID based on the host fully qualified domain name (FQDN) in the `host.domain` format. If the FQDN doesn't contain a dot character, the NIC MAC address is used instead.
* If you monitor multiple environments, you can split the hosts with identical IPs, MAC addresses, or FQDNs using a different namespace for each environment. The namespace can contain only alphanumeric characters, hyphens, underscores, and periods; the maximum length is 256 characters:

* `ip-addresses;namespace=<namespace>`
* `mac-addresses;namespace=<namespace>`
* `fqdn;namespace=<namespace>`

For example, to set the host ID source to `ip-addresses` and assign it to a namespace called `test`, run the OneAgent installer with the following parameter:

```
--set-host-id-source="ip-addresses;namespace=test"
```

To install OneAgent on a Citrix host, set the host ID source to `FQDN`:

```
--set-host-id-source="fqdn;namespace=test"
```

### Custom directory requirements

Make sure that your custom data storage meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be an already existing symbolic link.
* The value must not be a child directory of `/var/lib/dynatrace`.

### Changing location

If you use the parameter to change the location for an already installed OneAgent:

* Existing files are not migrated to the new location

* After you set or change the `DATA_STORAGE` parameter, you must restart deep-monitored processes, so that OneAgents monitoring them can pick up the new path to store runtime data. Otherwise, memory dumps and other runtime data won't be saved. You will be notified to restart a corresponding process on the **Process overview** page.

## Access to system logs

OneAgent downloads AIX system logs for the purpose of diagnosing issues that may be caused by conditions in your environment. For details, see [System logs downloaded by OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix#system-logs-downloaded-by-oneagent "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").

To disable access to logs:

```
--set-system-logs-access-enabled=false
```

To enable access to logs:

```
--set-system-logs-access-enabled=true
```

If you need to change this access after installation, use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

Note that this is a self-diagnostics setting that is not related to [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

## Skipping operating system support check

Setting this parameter to `true` will enable OneAgent installation on an otherwise unsupported platform. Dynatrace does not take responsibility for such installations.

This parameter is not preserved across automatic updates.

For information about the OneAgent auto-update mechanism, see [Update Dynatrace OneAgent on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix "Learn how you can update Dynatrace OneAgent on AIX.").

Default value: `false`

The `SKIP_OS_SUPPORT_CHECK` parameter allows you to force OneAgent installation on an otherwise unsupported platform.

For example:

```
SKIP_OS_SUPPORT_CHECK=true
```

For supported platforms, see [Technology support](/docs/ingest-from/technology-support#aix "Find technical details related to Dynatrace support for specific platforms and development frameworks.").


---


## Source: disk-space-requirements-for-oneagent-installation-and-update-on-aix.md


---
title: OneAgent files and disk space requirements on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix
scraped: 2026-02-17T04:53:09.751538
---

# OneAgent files and disk space requirements on AIX

# OneAgent files and disk space requirements on AIX

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Jun 25, 2025

This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.

|  |  | Default directory | Can be modified? |
| --- | --- | --- | --- |
| Size of installation (with temporary installation files removed) | ~700 MB | `/opt/dynatrace/oneagent` | Yes [1](#fn-1-1-def) |
| Persistent configuration | ~5 MB | `/var/lib/dynatrace/oneagent/agent/config` | No |
| Temporary files, runtime configuration | 200 MB | `/var/lib/dynatrace/oneagent/agent/runtime` | No |
| Logs | 1 GB | `/var/log/dynatrace/oneagent` [2](#fn-1-2-def) | Yes [3](#fn-1-3-def) |
| Crash reports, memory dumps | 3 GB | `/var/lib/dynatrace/oneagent/datastorage` | Yes [4](#fn-1-4-def) |
| Log analytics persistence | ~1 GB [5](#fn-1-5-def) | `/var/lib/dynatrace/oneagent/datastorage/loganalytics` | Yes [4](#fn-1-4-def) |
| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | `/var/lib/dynatrace/oneagent/agent/runtime/extensions/persistence` | Yes [5](#fn-1-5-def) [6](#fn-1-6-def) |
| Additional space required for updates | ~1.4 GB | See [Space required for updates](#updates) |  |
| **Total** | **~9.4 GB** |  |  |

1

Use the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#installation-path "Learn how you can use AIX installer with command line parameters.") installation parameter.

2

For OneAgent version 1.201 and earlier, the default location for log files is `/opt/dynatrace/oneagent/log`.

3

Use the [LOG\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#log-path "Learn how you can use AIX installer with command line parameters.") installation parameter.

4

Use the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#data-storage "Learn how you can use AIX installer with command line parameters.") installation parameter.

5

The size depends on the number of ingested logs.

6

Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/docs/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.

7

The reliability mechanism does not work if the requirement is not met. For more information see [Persistence details](#persistence).

For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").

## OneAgent files aging mechanism

OneAgent in Full-Stack Monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").

## Space required for updates

When calculating the space required for updates, we take into account the installer file size and the size of the installation process, that is the space required to deploy OneAgent files.

|  |  |
| --- | --- |
| Installer file size | ~120 MB |
| Installation process size | ~1.1 GB |

Additional space required for updates is calculated using the 10% safety margin:

`(installer file size + size of the installation process) * 1.1`

### Size of the installation process

The size of the installation process is calculated as follows:

`3 * installer file size + size of the installation`

The installer size must be multiplied by 3 to account for:

* Downloaded installer file (`/var/lib/dynatrace/oneagent`)
* Archive, which is separated from the installer script (`/opt/dynatrace/oneagent`)
* Unpacked external TAR (`/opt/dynatrace/oneagent`)

In terms of space requirements, there's no real difference between manual installation of the new version (when an older version is already installed), automatic update, and updates that are triggered by restarting the OneAgent container. In all these cases, the installation process is performed exactly the same way. What differs is the method through which the update is triggered.

## Persistence details

The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.

### General information

* Persistent storage of data requires 2136 MB of free disk space:

  + 600 MB of free disk space to be used by the reliability mechanism
  + 1.5 GB of free disk space to be used as a buffer
* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.
* The volume is used proportionally to the load of logs ingest.
* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).

### Configuration

Windows configuration file: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

**Variable**

**Description**

`persistence.reliable_mode`

`true` - reliable mode turned on; SFM logs genereted if space requirement not met
`false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism

`persistence.total_limit_kb`

Maximum volume limit for Extensions Log Persistence in kilobytes.
By default: 600 MB
Can be modified manually if the requirement can't be met on the host.


---


## Source: install-oneagent-on-aix.md


---
title: Install OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix
scraped: 2026-02-17T04:53:19.806128
---

# Install OneAgent on AIX

# Install OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Nov 07, 2025

This page describes how to download and install Dynatrace OneAgent on AIX.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements

### Permissions

* You need [Download/install OneAgent](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") permissions to download and install OneAgent.
* You need administrator rights for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the internet).
* You need permissions and credentials for restarting all your application services.

### Resources

* Check the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.").
* Your host requires 200 MB free memory to run OneAgent installation and update.
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### Limitations

* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.
* The support for [Log management and Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") and [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") on AIX hosts is limited:

  + log detection in log module is limited only to custom log sources.

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation

1. In Dynatrace Hub, search for **OneAgent**.
2. Select **Set up** > **AIX**.
3. Paste a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you'll use later.
4. In the **Download OneAgent** box, select  **Copy** to copy the `wget` command to the clipboard.
5. Log into your AIX host and then paste and execute the `wget` command that you just copied.

   * The `wget` command isn't installed on AIX by default. Either install it or use an alternative means of downloading OneAgent.
   * If you receive an error while downloading OneAgent, install the required certificate by downloading the root CA file from [Comodoï»¿](https://support.comodo.com/index.php?/Knowledgebase/Article/View/854/75/root-addtrustexternalcaroot) and then concatenating the content of the CRT file to `/var/ssl/cert.pem`. You can alternatively skip the certificate check by adding the parameter `--no-check-certificate`.
   * If you plan to download OneAgent directly to a server, note that outdated or missing libraries (for example, CA certificates or OpenSSL) will prevent the installer from downloading. We use encrypted connections. OpenSSL is required to enable `wget` to access the server.
6. **Verify the signature**

   After the download is complete, select  **Copy** in the **Verify signature** box to copy the `wget` command to the clipboard, then paste the provided command into your terminal window and execute it. Make sure your system is up to date, especially SSL and related certificate libraries.
7. Optional **Set customized options**

   * Enable monitoring of [Virtual I/O Server](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix#vios-installation "Learn how to download and install Dynatrace OneAgent on AIX.") logical partition.
   * Set a [network zone](/docs/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.
   * If your environment is segmented (for example, into development and production), consider [organizing your hosts into host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").
   * You can override the automatically detected [host name](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.
   * You can also apply [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the host to organize your monitored environments in a meaningful way.
   * Define [Properties](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.") to the host to automatically add metadata.
   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

     It is not available if the Virtual I/O Server monitoring option is enabled.

   The OneAgent command-line installer provides more options to [customize your installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
8. Copy the command provided in the **Run the installer with root rights** text field.
9. Run the installer.  
   Paste the command into your terminal and execute it.

   * You need root privileges. You'll need to make the script executable before you can run it as root.
   * You can use `su` or `sudo` to run the installation script. To do this, type the following command into the directory where you downloaded the installation script.  
     `sudo /bin/sh Dynatrace-OneAgent-AIX-1.0.0.sh`

   For a summary of the changes made to your system by OneAgent installation, see [OneAgent security on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").
10. On AIX, Dynatrace supports deep-code monitoring for Java, Apache, WebLogic, and Websphere applications. It's automated for OneAgent version 1.189+. For earlier releases, you need to perform some configuration on AIX, which can be easily done both for single applications as well as shell-wide.

    Automated injection of deep-code monitoring is enabled by default in Dynatrace version 1.195+ for fresh OneAgent 1.189+ installations.

    You can enable deep-code monitoring after you install OneAgent and it successfully connects to Dynatrace. On the **Hosts** page, find your host, go to **Host settings** > **Monitoring**, and select **Allow AIX kernel extension**.

## Installation on Virtual I/O Server (VIOS)

Use the generic installation steps to download the OneAgent, and then, after you have the OneAgent installer on your VIOS machine, issue the following commands.

1. Initiate the OEM installation and set up environment.

   ```
   oem_setup_env
   ```
2. Sign in to the `system` group.

   ```
   newgrp system
   ```
3. Install OneAgent.

   * The `--set-monitoring-mode=infra-only` parameter enables Infrastructure Monitoring.
   * The `--set-auto-injection-enabled=false` parameter disables automatic injection into processes.

   ```
   /bin/sh Dynatrace-OneAgent.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
   ```
4. Return to the Virtual I/O Server prompt.

   ```
   exit
   ```

## Manual OneAgent injection

If you can't use the unified monitoring approach, you can inject OneAgent manually.

Processes that have been given special privileges using AIX's Role-Based Access Control (RBAC) system can't be auto-injected. This is a safety mechanism of the operating system to restrict unknown code from being run with elevated privileges. For example, an Apache or IHS web server might have been given the `PV_NET_PORT` privilege to allow starting the server as a non-root user but still letting it bind into restricted ports like port `80`. In this case, any libraries configured for preloading, including OneAgent, will be silently ignored. In such cases, only manual OneAgent injection will work.

Manual OneAgent injection

IBM Java 1.6 â 1.8

IBM/Apache HTTP Server

Prepend your application command with the following commands:

```
export DT_HOME=/opt/dynatrace/oneagent



export LDR_PRELOAD64=$DT_HOME/agent/lib64/liboneagentproc.so



export LDR_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so
```

The `DT_HOME` variable must point to your OneAgent installation folder. If you customized your OneAgent installation directory, adjust `DT_HOME` variable accordingly. You can omit either the 32-bit or 64-bit entry, depending on your environment.

Edit your `httpd.conf` and add the following two lines at a location of your choice:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so



OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

Alternatively, if you prefer to leave your `httpd.conf` unchanged, you can specify the same directives using the command line:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so"



-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"



-k start
```

* `tenantUUID` is the [environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") ID of your Dynatrace environment that should be pulled from `dynatrace-env.sh` (located in the OneAgent installation root directory). The `tenantUUID` parameter is represented in the script as `DT_TENANT`.
* `tenantToken` is the [token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") that OneAgent uses to send data Dynatrace. It should be pulled from `dynatrace-env.sh` (or `ruxitagent.conf`, depending on your OneAgent version), which is located in the OneAgent installation root directory. The `tenantToken` parameter is represented in the script as `DT_TENANTTOKEN`.

  This token should not be confused with Dynatrace API or PaaS tokens. Those tokens can't be used here.
* `communicationEndpoints` corresponds to one or multiple HTTP addresses that represent Dynatrace Servers or ActiveGates. The `communicationEndpoints` parameter is represented in the script as `DT_CONNECTION_POINT`. For example, the `dynatrace-env.sh` (located in the OneAgent installation root directory) may contain the following:

  ```
  export DT_CONNECTION_POINT="https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication"
  ```

  In this case, the parameter would be

  ```
  server=https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication
  ```

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.


---


## Source: oneagent-security-aix.md


---
title: OneAgent security on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix
scraped: 2026-02-17T04:53:14.679413
---

# OneAgent security on AIX

# OneAgent security on AIX

* Latest Dynatrace
* Reference
* 3-min read
* Published Nov 12, 2020

To fully automate the monitoring of your operating systems, processes, and network interfaces, Dynatrace requires privileged access to your operating system during both installation and operation.

OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Permissions

### Installation

OneAgent installer requires admin privileges to:

* Add an entry for OneAgent to `/etc/rc.shutdown`
* Register OneAgent service in the system's init via the `mkitab` command

### Operation

The OneAgent requires admin privileges to:

* Access the list of open sockets for each process.
* Access the list of libraries loaded for each process.
* Access the name and path of the executable file for each process.
* Access command line parameters for each process.
* Monitor network traffic.
* Read application configuration files.
* Load `oneagentkmod`  kernel extension to enable automatic injection into processes

## Operating system changes

* The `oneagentkmod` kernel extension is loaded upon OneAgent service startup.

## Files modified

* `/etc/rc.shutdown` and `/etc/inittab` have an entry added for `oneagent` service.

## Files added

### Installation

The OneAgents installer adds the following files to your system:

* OneAgent binaries and configuration files are saved in `/opt/dynatrace/oneagent`. Note that you can change the location using [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#installation-path "Learn how you can use AIX installer with command line parameters.") parameter.

### Operation

OneAgent adds the following files to your system:

* OneAgent temporary files and runtime configuration are saved in `/var/lib/dynatrace/oneagent/runtime`.
* OneAgent persistent configuration is saved in `/var/lib/dynatrace/oneagent/config`.
* Large runtime data, such as memory dumps, is saved in `/var/lib/dynatrace/oneagent/datastorage`. Note that you can change the location of large runtime data using the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#data-storage "Learn how you can use AIX installer with command line parameters.") parameter.

## System logs downloaded by OneAgent

OneAgent downloads certain system logs so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or installations run as automatic updates.
System logs downloaded by OneAgent on AIX are:

* `/etc/security/limits`
* `/var/adm/ras/errlog`
* `/var/log/kern`
* `/var/log/syslog`

Revoking access to system logs

To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.  
For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Globally writable directories

The OneAgent directory structure contains globally writable directories (`1777` permissions). Changing these permissions by users is not supported.

### OneAgent injection mechanism

Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.

Similarly, certain log files require global write permissions (`666`) to allow applications running under various users to write to them.

### System security

We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.

* We keep the number of globally writable directories as limited as possible.
* All these directories have a sticky bit set (actual permissions are `1777`). Only the file's owner, the directory's owner, or the root user can modify the files in the directory. This is standard practice that makes the permissions more robust. It's also used for the `/tmp` directory to prevent ordinary users from deleting or moving other users' files.


---


## Source: enable-auto-injection.md


---
title: Automated injection of deep-code monitoring on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/enable-auto-injection
scraped: 2026-02-17T04:53:08.132750
---

# Automated injection of deep-code monitoring on AIX

# Automated injection of deep-code monitoring on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jun 22, 2022

On AIX, Dynatrace supports deep-code monitoring for Java, Apache, WebLogic and Websphere applications. Since OneAgent version 1.189, you only need to **Allow AIX kernel extension** on your AIX **Host settings** page in Dynatrace. For earlier releases, you need to perform some configuration on AIX, see [Install OneAgent on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Learn how to download and install Dynatrace OneAgent on AIX.").

## Enable automated injection

To enable automated injection

1. After you install OneAgent and it successfully connects to Dynatrace, in Dynatrace, go to **Hosts** and select your AIX host.
2. On the host details page, select **More** (**â¦**) > **Settings**.
3. Select the **AIX kernel extension** tab.
4. Turn on **Allow AIX kernel extension**.  
   OneAgent will then begin collecting deep-code monitoring data.

You can use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure your automated injection.

1. To learn the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:host.monitoring.aix-kernel-extension` as the schemaId.
2. Based on the `builtin:host.monitoring.aix-kernel-extension` schema, create your configuration object.
3. To create your configuration, use [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

## Update OneAgent version 1.187 and earlier

If you manually configured your AIX host to inject OneAgent code modules, we recommend that you clear the `LDR_PRELOAD` and the `LDR_PRELOAD64` environment variables after you enable the automated injection. This enables you to uninstall OneAgent simply using the [uninstall script](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix "Learn how you can remove OneAgent from your AIX-based system.") without the need to clear the environment variables.


---


## Source: stop-restart-oneagent-on-aix.md


---
title: Stop/restart OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix
scraped: 2026-02-17T04:53:11.390027
---

# Stop/restart OneAgent on AIX

# Stop/restart OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:

1. Go to **Settings > Monitoring overview**.
2. Click the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.
3. Slide the **Monitoring** switch to the **Off** position.
4. Restart all processes for which monitoring has been disabled.

## Stop and start OneAgent using the command line

* [Restart OneAgent via `oneagentctl` command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").
* If you use configuration management tools like Puppet or Ansible, you can alternatively stop the OneAgent service using the shell command. The `oneagent` service script is located in `<INSTALL_PATH>/agent/initscripts/`.

  To stop OneAgent, use root privileges and execute the `oneagent` service script with the `stop` parameter.

  If you stop OneAgent service, monitoring will be disabled until the service is restarted.

  To start OneAgent, use root privileges and execute the `oneagent` service script with the `start` parameter.

Learn more about [how OneAgent interacts with your OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").


---


## Source: uninstall-oneagent-on-aix.md


---
title: Uninstall OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix
scraped: 2026-02-17T04:53:18.069360
---

# Uninstall OneAgent on AIX

# Uninstall OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system. Go to the `/opt/dynatrace/oneagent/agent` directory and, using root rights, run the `uninstall.sh` script.

## Following uninstallation

Following uninstallation, log files and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.

For a complete OneAgent uninstallation, remove the following:

* Log files located at:

  + OneAgent version 1.203+ `/var/log/dynatrace/oneagent`
  + OneAgent version 1.201 and earlier `/opt/dynatrace/oneagent/log`
* Configuration files located at `/var/lib/dynatrace/oneagent/agent/config`.
* Clear the `LDR_PRELOAD` and the `LDR_PRELOAD64` environment variables.


---


## Source: update-oneagent-on-aix.md


---
title: Update Dynatrace OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix
scraped: 2026-02-17T04:53:13.065549
---

# Update Dynatrace OneAgent on AIX

# Update Dynatrace OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

OneAgent installed in full-stack mode has a built-in, configurable auto-update mechanism.

See [OneAgent update](/docs/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") for an overview of OneAgent update, including how to monitor updates and how to create update windows.

## Configure OneAgent updates

You can configure OneAgent update globally, per host group, and per host.

Configure global OneAgent update

When automatic updates are turned on globally, whenever a new version of OneAgent becomes available, all of your installed OneAgent instancesâexcept where you have turned off auto-updates at the host group or host levelâwill automatically download the update and upgrade their binaries and configuration files.

Automatic update settings at the host group and individual host level override global settings.

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. Select one of the update options:

   * **Automatic updates at earliest convenience**  
     Update all OneAgents automatically, regardless of update windows.
   * **Automatic updates during update windows**  
     Update all OneAgents automatically during the selected update window.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host group OneAgent update

OneAgent update settings at the host group level override global settings and are overridden by settings at the host level.

1. Open the **Host group settings** page.  
   Access alternatives:

   * Go to **Settings** > **Monitoring** > **Monitoring overview**, find any host that is in the host group you want to configure, and select the host group name (not the host name).
   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**, open a host page, and expand the **Properties and tags** section. If the host belongs to a group, there is a link to it under **Host group**.
   * Go to **Deployment Status** > **OneAgents**. If a host belongs to a host group, a link to the host group settings page is displayed under the host name.
2. On the **Host group settings** page, select **OneAgent updates** on the left side of the page.
3. Select one of the update options:

   * **Inherit global update settings**  
     Follow the global update settings for updating OneAgents in this host group.

     + The current global setting is displayed in parentheses on this line.
     + To go to the global configuration page, select the `global` link.
   * **Automatic updates at earliest convenience**  
     Update all OneAgents in this host group automatically, regardless of update windows. Ignore the global update settings.
   * **Automatic updates during update windows**  
     Update all OneAgents in this host group automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents in this host group. Ignore the global update settings.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host-level OneAgent update

OneAgent update settings at the host level override OneAgent update settings at the global and host group levels.

1. Open the **Host** page for the host you want to configure.  
   Access options:

   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and then select the host.
   * Go to **Settings** > **Monitoring** > **Monitoring overview**, select the **Hosts** tab, and then select the host.
2. On the **Host** page, open the browse menu (**â¦**) and select **Settings**.
3. Select **OneAgent updates** on the left side of the page.
4. Select one of the update options:

   * **Inheritâ¦**  
     Follow the host group or global update settings for updating this OneAgent.

     + If the selected host belongs to a host group, the current host group setting is displayed in parentheses on this line, and the group name is a link to the host group configuration page.
     + If the selected host does not belong to a host group, the global setting is displayed in parentheses on this line, and "global" is a link to the global configuration page (**Settings** > **Updates** > **OneAgent updates**).
   * **Automatic updates at earliest convenience**  
     Update this OneAgent automatically, regardless of update windows. Ignore the host group update settings.
   * **Automatic updates during update windows**  
     Update this OneAgent automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update this OneAgent. Ignore the global update settings.

Manually update OneAgent on individual hosts

To manually update OneAgent running on an individual host:

1. Go to **Settings > Monitoring > Monitoring overview**.
2. Select the **Hosts** tab.
3. To update OneAgent or download the latest version, select **Update** next to the name of the host you're interested in.

   The **Update** button appears only if the installed version of OneAgent on a specific host is outdated and if it is a full-stack OneAgent. This button doesn't appear with PaaS and standalone OneAgents.
4. Select **Update now**.  
   If the **Update now** button is disabled, you don't have permissions to download the installer.

Alternatively, you can download the latest version of the OneAgent installer, copy it manually to the target host, and perform installation directly on the target host.

Select OneAgent version to install on new hosts

To control which version of OneAgent is automatically installed on all new hosts:

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In **Update mode**, select **No automatic updates** to disable automatic OneAgent updates.

   For details on how to disable OneAgent automatic updates on Paas/Kubernetes, see [DynaKube parameters for Dynatrace Operator on Kubernetes/OpenShift](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
3. In **Target version**, select the version of OneAgent to install on all new hosts.

The selected OneAgent version is also used for PaaS integrations.

Select OneAgent version to update to

To select which version of OneAgent to update to

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In the **Target version** list, you can specify a particular version by OneAgent version number or select a relative target version:

   * **Latest stable version**  
     The most recent stable OneAgent version that is available in your environment. The actual version number is displayed in parentheses.
   * **Previous stable version**  
     The stable version before **Latest stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *two* less than the latest version number.
   * **Older stable version**  
     The stable version before **Previous stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *four* less than the latest version number.

* **Specific OneAgent version**

The target version is used for:

* Automatic updates
* Automatic updates during maintenance windows
* Manual updates when you select the version you want to update to

You can set the target version and update mode at:

* **Environment level**
  Affects all OneAgents of an environment. Is also used for Deployment API.
* **Host group**
  Affects all OneAgents of a host-group. Overrides the environment level. Does not affect Deployment API.
* **Host**
  Affects OneAgent on this host. Overrides host group and environment-level configuration. Does not affect Deployment API.

If you select an older version than a currently deployed version, you won't be able to downgrade OneAgent. You will need to install a newer version over an existing OneAgent version.

## System requirements

### Disk space

For details, see [OneAgent files and disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.")

### Free memory

Your host requires 200 MB free memory to run OneAgent update.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### OneAgent command-line interface

Run `oneagentctl` with the `--version` parameter. For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.


---


## Source: aix.md


---
title: AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix
scraped: 2026-02-17T04:45:50.459593
---

# AIX

# AIX

* Latest Dynatrace
* Overview
* 1-min read
* Published Jul 19, 2017

Dynatrace supports full-stack OneAgent installation on IBM AIX. For analytical information about the supported OneAgent capabilities for AIX, see the [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms."). For the supported AIX versions, check the [OneAgent supported technologies and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Installation

[#### OneAgent files and disk space requirements on AIX

Find out what the disk space requirements are for OneAgent installation on AIX.

* Reference

Read this reference](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix)[#### OneAgent security on AIX

Learn about Dynatrace OneAgent security and modifications to your AIX-based system.

* Reference

Read this reference](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix)

[#### Install OneAgent on AIX

Learn how to download and install Dynatrace OneAgent on AIX.

* How-to guide

Read this guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix)[#### Customize OneAgent installation on AIX

Learn how you can use AIX installer with command line parameters.

* How-to guide

Read this guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix)

### Operation

[#### Automated injection of deep-code monitoring on AIX

Learn how to enable automated OneAgent injection of deep-code monitoring on AIX.

* How-to guide

Read this guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/enable-auto-injection)[#### Update Dynatrace OneAgent on AIX

Learn how you can update Dynatrace OneAgent on AIX.

* How-to guide

Read this guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix)

[#### Stop/restart OneAgent on AIX

Learn how to stop and restart OneAgent on AIX.

* How-to guide

Read this guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix)[#### Uninstall OneAgent on AIX

Learn how you can remove OneAgent from your AIX-based system.

* How-to guide

Read this guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix)

### See also

[#### OneAgent configuration via command-line interface

Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.

* Reference

Read this reference](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface)[#### Troubleshooting OneAgent installation

Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.

* Troubleshooting

Read this troubleshooting guide](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation)


---


## Source: customize-oneagent-installation-on-linux.md


---
title: Customize OneAgent installation on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux
scraped: 2026-02-17T04:52:43.159479
---

# Customize OneAgent installation on Linux

# Customize OneAgent installation on Linux

* Latest Dynatrace
* 7-min read
* Published Sep 19, 2018

The Linux installer can be used with command line parameters when you can't use the default settings. Note that all parameters listed below are optional.

## Passing installation parameters

To pass the parameters, append them to the installer command and separate them with spaces.

For example:

```
Dynatrace-OneAgent-Linux.sh --set-host-group=my_host_group --set-monitoring-mode=infra-only
```

## Removed installation parameters

Convert to the newer `--set-param=<value>` parameters now. The equivalent `PARAM=<value>` parameters are not supported by the OneAgent installer starting with version 1.213.

| Removed `PARAM=<value>` parameter | New `--set-param=<value>` parameter |
| --- | --- |
| `SERVER` | `--set-server` |
| `TENANT` | `--set-tenant` |
| `TENANT_TOKEN` | `--set-tenant-token` |
| `PROXY` | `--set-proxy` |
| `HOST_GROUP` | `--set-host-group` |
| `APP_LOG_CONTENT_ACCESS` | `--set-app-log-content-access` |
| `DISABLE_SYSTEM_LOGS_ACCESS` | `--set-system-logs-access-enabled` |

If you mix equivalent `PARAM=<value>` and `--set-param=<value>` settings, the `--set-param=<value>` setting overrides the `PARAM=<value>` setting.

## Installation path

**Default value**: `/opt/dynatrace/oneagent`

**Prerequisite**: Using this parameter when SELinux is enabled requires the semanage utility to be available on your system.

The **`INSTALL_PATH`** parameter allows installation to a different directory. For example:

```
/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh INSTALL_PATH=/data/dynatrace/agent
```

The installer creates the symbolic link `/opt/dynatrace/oneagent` > `/data/dynatrace/agent` and the OneAgent installation files are placed in the specified directory (in this example, `/data/dynatrace/agent`). Note that this symbolic link needs to be removed manually after OneAgent is uninstalled.

The `INSTALL_PATH` parameter doesn't control the OneAgent [log and configuration files](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.") directories. To customize the log path, use the `LOG_PATH` parameter.

Additionally, the default installation paths should not be symbolic links. Specifically, `/var/lib/dynatrace` cannot be altered, except for the `/var/lib/dynatrace/oneagent/datastorage` part, which can be modified using the `DATA_STORAGE` option.

Installation directory

ActiveGate and OneAgent installed on the same host must **not** share the same installation directory.

### Custom directory requirements

Make sure that your custom installation directory path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be an already existing symbolic link.
* The value must not be a child directory of `/var/lib/dynatrace`.

## Log path

**Default value**: `/var/log/dynatrace/oneagent`

**Prerequisite**: Using this parameter when SELinux is enabled requires the semanage utility to be available on your system.

The **`LOG_PATH`** parameter allows you to customize your OneAgent log directory. For example:

```
/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh LOG_PATH=/data/dynatrace/logs
```

### Custom directory requirements

Make sure that your custom log path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be an already existing symbolic link.
* The value must not be a child directory of `/var/lib/dynatrace`.

* Avoid using `/opt/dynatrace/oneagent/log`, which is the default log location for OneAgent versions earlier than 1.203.

### Changing location

If you use the parameter to change the location for an already installed OneAgent:

* Existing files are not migrated to the new location

* After you set or change the `LOG_PATH` parameter, you must restart deep-monitored processes, so that OneAgents monitoring them can pick up the new path to store logs. You will be notified to restart a corresponding process on the **Process overview** page.

## Data storage

OneAgent version 1.199

**Default value**: `/var/lib/dynatrace/oneagent/datastorage`

**Prerequisite**: Using this parameter when SELinux is enabled requires the semanage utility to be available on your system.

The **`DATA_STORAGE`** parameter allows you to define a directory dedicated to storing large runtime data produced by OneAgent in full-stack monitoring mode, such as crash reports or memory dumps.
For example:

`/bin/sh Dynatrace-OneAgent-Linux.sh DATA_STORAGE=/data/dynatrace/runtime`

## Communication endpoint

**Default value**: `environment specific`

The address of the OneAgent communication endpoint, which is a Dynatrace component that OneAgent sends data to. Depending on your deployment, it can be a Dynatrace Cluster or ActiveGate. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value. To change it, use the IP address or a name. Add the port number following a colon.

To set the communication endpoint, pass it as a parameter value:

```
--set-server=https://100.20.10.1:443
```

OneAgent and Dynatrace Cluster automatically maintain a working connection. If an endpoint detail changes, the cluster notifies OneAgent of the change and OneAgent automatically updates the endpoint you set using the `--set-server` to the new working value.

To change the endpoint after installation, use `--set-server` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Environment ID

**Default value**: `environment specific`

The Dynatrace [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") you received with your activation email. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value. If you're selling Dynatrace-based services, use this option to set your customers' IDs from the pool of IDs you purchased from Dynatrace.

To set the environment ID, pass it as a parameter value:

```
--set-tenant=mySampleEnv
```

To change the tenant after installation, use `--set-tenant` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Token

**Default value**: `environment specific`

The tenant token that is used for authentication when OneAgent connects to the communication endpoint to send data. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value.

To set a token, pass it as a parameter value:

```
--set-tenant-token=abcdefghij123456
```

See [Access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") to learn how to obtain a token.

To change the tenant token after installation, use `--set-tenant-token` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Network zones

**Default value**: `unset`

To learn about network zone naming rules and other reference information, see [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

Use the `--set-network-zone` parameter to instruct OneAgent to communicate via the specified network zone:

```
--set-network-zone=your.network.zone
```

To change or clear the network zone assignment after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify network zone** action).

Alternatively, you can use `--set-network-zone` on the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Proxy

**Default value**: `unset`

The address of the proxy server. Use the IP address or a name, and add the port number following a colon. For an authenticating proxy you can specify a username and password like this `username:password@172.1.1.128:8080` where both username and password need to be URL encoded.

To set a proxy, pass it as a parameter value:

```
--set-proxy=172.1.1.128:8080
```

Dynatrace also supports IPv6 addresses.

To change or clear the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Port range

Deprecated

Starting with OneAgent version 1.301, OneAgent doesn't use the TCP ports for its own inter-process communication. In case OneAgent occupies your applications' ports, upgrade OneAgent to version 1.301+.

**Default value**: `50000:50100`

Watchdog is a binary used for starting and monitoring OneAgent monitoring processes:

* `oneagentos`âoperating system monitoring
* `oneagentplugin`âmonitoring using [OneAgent extensions](/docs/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`âmonitoring using local [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`â[Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`â[network monitoring](/docs/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Use the `--set-watchdog-portrange=<arg>` parameter to change the watchdog listening port range to `<arg>`. The `<arg>` must contain two port numbers separated by a colon (`:`). For example `50000:50100`. The maximum supported port range is from 1024 to 65535. The port range must cover at least 4 ports. The port number starting the range must be lower. For example:

```
--set-watchdog-portrange=50000:50100
```

To change port range after installation, use `--set-watchdog-portrange` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#portrange "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Auto-update

Use the `--set-auto-update-enabled=<arg>` to enable or disable OneAgent auto-update. For example:

```
--set-auto-update-enabled=true
```

After you set the parameter to `false`, you won't be able to control OneAgent automatic updates using the Dynatrace web UI at **Settings** > **Updates** > **OneAgent updates**.

## Host group

**Default value**: `unset`

The name of a group you want to assign the host to. For details, see [Organize your environment using host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Host group string requirements:

* Can contain only alphanumeric characters, hyphens, underscores, and periods
* Must not start with `dt.`
* Maximum length is 100 characters

To assign a host to the host group, pass the host group name as a parameter value:

```
--set-host-group=My.HostGroup_123-456
```

To remove the host from a group, you need to [uninstall OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.") or pass an empty value `--set-host-group=""` when running a OneAgent update. You can't remove the host from a group using the `HOST_GROUP` parameter when updating OneAgent.

To change or clear the host group assignment after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host group** action).

Alternatively, you can use `--set-host-group` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Monitoring mode

**Default value**: `fullstack`

Activates one of the OneAgent monitoring modes:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

To enable a specific monitoring mode, set the `--set-monitoring-mode` parameter to one of the following values:

* `fullstack`
* `infra-only`
* `discovery`

For example:

```
--set-monitoring-mode=infra-only
```

To change the monitoring mode after installation, use `--set-monitoring-mode` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#infrastructure-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") or set it using the [Host settings](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") page.

## Custom host name

**Default value**: `unset`

Use the `--set-host-name` to override an automatically detected host name. The host name value must not contain the `<`, `>`, `&`, `CR` (carriage return), and `LF` (line feed) characters and the maximum length is 256 characters.

This command adds a custom host name to display in the UI, but the detected host name is not changed. For details, see [Set custom host names](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

To set the host name:

```
--set-host-name=myhostname
```

To change the host name after installation, use `--set-host-name` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Custom host metadata

**Default value**: `unset`

Once configured, custom metadata is displayed as a set of properties at the bottom of the **Properties and tags** section of the host overview page. The property values must not contain the `=` (except key-value delimiter) and whitespace characters. The maximum length is 256 characters including the key-value delimiter.

To add or change host properties:

```
--set-host-property=AppName --set-host-property=Environment=Dev
```

You can add or change more than one property in the same command.

To change the host metadata after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select **modify host properties** action).

Alternatively, you can use `--set-host-property` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Custom host tags

**Default value**: `unset`

Once configured, the tags are displayed at the top of the **Properties and tags** section of the host overview page. The property values must not contain the `=` (except key-value delimiter) and whitespace characters. The maximum length is 256 characters including the key-value delimiter.

To add or change host tags:

```
--set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk
```

You can add or change more than one tag in the same command. It is allowed to define tags with the same key but different values.

To change the host tags after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host tags** action).

Alternatively, you can use `--set-host-tag` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Host ID source

**Default value**: `auto`

Available on all supported platforms for OneAgent version 1.223+. For OneAgent version 1.221 and earlier, this feature is supported only for Citrix Virtual Apps and Desktops.

It's particularly important to keep your host ID static in dynamic virtual environments where hosts are recreated on a daily basis.

To **define the source for host ID generation**, use `--set-host-id-source` and set it to one of the predefined values:

* `auto` â Let Dynatrace generate the host ID automatically
* `ip-addresses` â Generate host ID based on the host IP address
* `mac-addresses` â Generate host ID based on the host's NIC MAC address
* `fqdn` â Generate host ID based on the host fully qualified domain name (FQDN) in the `host.domain` format. If the FQDN doesn't contain a dot character, the NIC MAC address is used instead.
* If you monitor multiple environments, you can split the hosts with identical IPs, MAC addresses, or FQDNs using a different namespace for each environment. The namespace can contain only alphanumeric characters, hyphens, underscores, and periods; the maximum length is 256 characters:

* `ip-addresses;namespace=<namespace>`
* `mac-addresses;namespace=<namespace>`
* `fqdn;namespace=<namespace>`

For example, to set the host ID source to `ip-addresses` and assign it to a namespace called `test`, run the OneAgent installer with the following parameter:

```
--set-host-id-source="ip-addresses;namespace=test"
```

To install OneAgent on a Citrix host, set the host ID source to `FQDN`:

```
--set-host-id-source="fqdn;namespace=test"
```

### Custom directory requirements

Make sure that your custom data storage path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be an already existing symbolic link.
* The value must not be a child directory of `/var/lib/dynatrace`.

### Changing location

If you use the parameter to change the location for an already installed OneAgent:

* Existing files are not migrated to the new location

* After you set or change the `DATA_STORAGE` parameter, you must restart deep-monitored processes, so that OneAgents monitoring them can pick up the new path to store runtime data. Otherwise, memory dumps and other runtime data won't be saved. You will be notified to restart a corresponding process on the **Process overview** page.

## Access to system logs

**Default value**: `true`

OneAgent downloads Linux system logs for the purpose of diagnosing issues that may be caused by conditions in your environment. For details, see [System logs downloaded by OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#system-logs "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

To disable access to logs:

```
--set-system-logs-access-enabled=false
```

To enable access to logs:

```
--set-system-logs-access-enabled=true
```

If you need to change this access after installation, use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."):

Note that this is a self-diagnostics setting and is not related to [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

## Log Monitoring

**Default value**: `true`

When set to `true`, allows OneAgent to access log files for the purpose of Log Monitoring. Accepted values are (`true`, `false`) or (`1`, `0`). This option can alternatively be [enabled/disabled through the Web UI](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

For example:
`--set-app-log-content-access=true`

If you need to enable or disable Log Monitoring after installation, use `-set-app-log-content-access` in [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Automatic injection

Do not set this parameter to `true` during the installation process.

**Default value**: `true`

You can set the `--set-auto-injection-enabled=<arg>` parameter to `true` or `false` to disable or enable OneAgent auto-injection.

For more information, see [Automatic injection](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Local metric ingestion

**Default value**: `14449`

You can use the `--set-extensions-ingest-port=<arg>` parameter to change the default communication port used for local metric ingestion. The port is used by [OneAgent REST API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), [Scripting integration](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") (`dynatrace_ingest`), and [Telegraf](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace.").

For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## StatsD metric ingest

**Default value**: `18125`

You can use the `--set-extensions-statsd-port=<arg>` parameter to change the default [DynatraceStatsD](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.") UDP listening port.

For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## Non-privileged mode

### **`NON_ROOT_MODE`**

**Default value**: `1` (OneAgent version 1.193+. For earlier versions `0`)

When you install OneAgent in non-privileged mode, you only need to grant elevated privileges to OneAgent during the installation. Elevated privileges are dropped as soon as OneAgent is deployed.

Since version 1.193, OneAgent is installed in non-privileged mode by default. Existing installations aren't switched to non-privileged mode.

To switch an installed OneAgent to non-privileged mode, you need to manually append the `NON_ROOT_MODE=1` parameter to the installation command. Example:
`sudo /bin/sh Dynatrace-Agent-Linux-1.0.0.sh NON_ROOT_MODE=1`  
To switch the installer back to the default mode for consecutive updates, run it with `NON_ROOT_MODE=0`.

Note that non-privileged mode requires Linux kernel capabilities that are available in these versions:

* Linux kernel version 2.6.26+ for OneAgent installation without root privileges.
* Linux kernel version 4.3+ (recommended systemd version 221+) for OneAgent automatic updates and full operation without root privileges.
  For more information, see [Linux non-privileged mode](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.")

### **`DISABLE_ROOT_FALLBACK`**

**Default value**: `0`

Used in conjunction with the `NON_ROOT_MODE` parameter to block the superuser permission level for OneAgent run in the non-privileged mode. The root privileges are required for automatic updates and selected operations on kernel versions between 2.6.26 and 4.3, that is versions without the support for Linux ambient capabilities.

`sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh NON_ROOT_MODE=1 DISABLE_ROOT_FALLBACK=1`

To switch the installer back to use the superuser permission level for subsequent updates, run it with `DISABLE_ROOT_FALLBACK=0`.

For more information, see the [permission requirements for OneAgent installation and operation on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.").

* The uninstall process doesn't delete the unprivileged user from the system (whether or not it's `dtuser` or specified by the `USER parameter`).
* The unprivileged `username` is preserved during upgrades, unless a new username is specified during upgrade.

## Specifying non-privileged user and group

### **`USER`**

**Default value**: `dtuser`

Specifies the name of the non-privileged user, which is used by unprivileged OneAgent processes. Unprivileged processes are those that don't need root privileges. These processes on Linux are called `Network OneAgent` and `Plugin OneAgent`.

* The default behavior is that the Dynatrace installer uses `dtuser` for the name of the unprivileged user.
* If the `USER=<username>` parameter is specified, the installer uses `<username>` as the name of the unprivileged user.

In either case, the Dynatrace installer checks whether a required user (`dtuser` or the user specified by the `USER` parameter) already exists in the system.

* If a user and a group with the same name both exist and this user has that group set as its primary one, the user is used to start the OneAgent network and plugin modules.
* If a user doesn't exist, the Dynatrace installer creates this user and group and later starts these unprivileged processes with this new user.
* If a user exists in the system but doesn't have a group with the same name set as its primary one, the installation is abortedâto use a group with a different name, you must use the `GROUP` parameter.

`USER` string requirements:

* Can contain only alphanumeric characters, hyphen `-`, underscore `_`, and dot `.`
* Minimum length is 3 characters
* Maximum length is 32 characters
* Can't be a [user identifierï»¿](https://man7.org/linux/man-pages/man7/credentials.7.html) string

### **`GROUP`**

**Default value**: `dtuser`

Can only be used in conjunction with the `USER` parameter and is used to specify the primary group for the user passed via the `USER` parameter. If you don't specify the `GROUP` parameter, the installer assumes it's the same as the `USER`, for both existing and non-existing users. If you specify the group using the `GROUP` parameter, and a user doesn't exist, the installer creates the user and assigns it to the specified group. You also use the `GROUP` parameter to specify an unprivileged user that belongs to a specific group, with a different name than the user name. To harden your system security, we strongly recommend use of a dedicated user group to run OneAgent processes.

`GROUP` string requirements:

* Can contain only alphanumeric characters, hyphen `-`, underscore `_`, and dot `.`
* Minimum length is 3 characters
* Maximum length is 32 characters
* Can't be a [group identifierï»¿](https://man7.org/linux/man-pages/man7/credentials.7.html) string

## Skipping operating system support check

Setting this parameter to `true` will enable OneAgent installation on an otherwise unsupported platform. Dynatrace does not take responsibility for such installations.

This parameter is not preserved across automatic updates.

For information about the OneAgent auto-update mechanism, see [Update OneAgent on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.").

**Default value**: `false`

The **`SKIP_OS_SUPPORT_CHECK`** parameter allows you to force OneAgent installation on an otherwise unsupported platform.

For example:

```
/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh SKIP_OS_SUPPORT_CHECK=true
```

For supported platforms, see [Technology support](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.").


---


## Source: disk-space-requirements-for-oneagent-installation-and-update-on-linux.md


---
title: OneAgent files and disk space requirements on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux
scraped: 2026-02-17T04:52:56.487110
---

# OneAgent files and disk space requirements on Linux

# OneAgent files and disk space requirements on Linux

* Latest Dynatrace
* 4-min read
* Updated on Jun 25, 2025

This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.

## Full-stack and Infrastructure Monitoring mode

The same disk space requirements apply to both Full-stack and Infrastructure monitoring modes.

## OneAgent directories and their sizes

|  | **Linux (x86)** | **Linux (ppcle)** | **Linux (s390)** | Default directory | Can be modified? |
| --- | --- | --- | --- | --- | --- |
| Size of installation | ~1.3 GB | ~500 MB | ~480 MB | `/opt/dynatrace/oneagent` | Yes [1](#fn-1-1-def) |
| Persistent configuration | ~5 MB | ~5 MB | ~5 MB | `/var/lib/dynatrace/oneagent/agent/config` | No |
| Temporary files, runtime configuration | 200 MB | 200 MB | 200 MB | `/var/lib/dynatrace/oneagent/agent/runtime` | No |
| Logs | 1 GB | 1 GB | 1 GB | `/var/log/dynatrace/oneagent` [2](#fn-1-2-def) | Yes [3](#fn-1-3-def) |
| Crash reports, memory dumps | 3 GB | 3 GB | 3 GB | `/var/lib/dynatrace/oneagent/datastorage` | Yes [4](#fn-1-4-def) |
| Log analytics persistence | ~1 GB [5](#fn-1-5-def) | ~1 GB [5](#fn-1-5-def) | ~1 GB [5](#fn-1-5-def) | `/var/lib/dynatrace/oneagent/datastorage/loganalytics` | Yes [4](#fn-1-4-def) |
| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | 600 MB + 1.5 GB buffer | 600 MB + 1.5 GB buffer | `/var/lib/dynatrace/oneagent/agent/runtime/extensions/persistence` | Yes [6](#fn-1-6-def) [7](#fn-1-7-def) |
| Additional space required for updates | ~2.6 GB | ~950 MB | ~880 MB | See [Space required for updates](#updates) |  |
| **Total** | **~11.7 GB** | **~8.7 GB** | **~8.6 GB** |  |  |

1

Use the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.") installation parameter.

2

For OneAgent version 1.201 and earlier, the default location for log files is `/opt/dynatrace/oneagent/log`.

3

Use the [LOG\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#log-path "Learn how to use the Linux installer with command line parameters.") installation parameter.

4

Use the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters.") installation parameter.

5

The size depends on the number of ingested logs.

6

Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/docs/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.

7

The reliability mechanism does not work if the requirement is not met. For more information see [Persistence details](#persistence).

For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

## OneAgent files aging mechanism

OneAgent in full-stack monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").

## Dynatrace Managed self-monitoring

For OneAgent self-monitoring for Dynatrace Managed requirements on Linux, see [the directory structure of Dynatrace Managedï»¿](https://docs.dynatrace.com/managed/shortlink/managed-directory-structure).

## Space required for updates

When calculating the space required for updates, we take into account the installer file size and the size of the installation process, that is the space required to deploy OneAgent files.

The figures provided below are examples and should be used as a general guide. For the accurate size of installation, see the **Size of installation** in the [OneAgent directories and their sizes](#sizes) section.

|  | **Linux (x86)** | **Linux (ppcle)** | **Linux (s390)** |
| --- | --- | --- | --- |
| Installer file size | ~260 MB | ~90 MB | ~80 MB |
| Installation process size | ~2.1 GB | ~770 MB | ~720 MB |

Additional space required for updates is calculated using the 10% safety margin:

`(installer file size + size of the installation process) * 1.1`

### Size of the installation process

The size of the installation process is calculated as follows:

`3 * installer file size + size of the installation`

The installer size must be multiplied by 3 to account for:

* Downloaded installer file (`/var/lib/dynatrace/oneagent`)
* Archive, which is separated from the installer script (`/opt/dynatrace/oneagent`)
* Unpacked external TAR (`/opt/dynatrace/oneagent`)

In terms of space requirements, there's no real difference between manual installation of the new version (when an older version is already installed), automatic update, and updates that are triggered by restarting the OneAgent container. In all these cases, the installation process is performed exactly the same way. What differs is the method through which the update is triggered.

## Persistence details

The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.

### General information

* Persistent storage of data requires 2136 MB of free disk space:

  + 600 MB of free disk space to be used by the reliability mechanism
  + 1.5 GB of free disk space to be used as a buffer
* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.
* The volume is used proportionally to the load of logs ingest.
* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).

### Configuration

Windows configuration file: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

**Variable**

**Description**

`persistence.reliable_mode`

`true` - reliable mode turned on; SFM logs genereted if space requirement not met
`false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism

`persistence.total_limit_kb`

Maximum volume limit for Extensions Log Persistence in kilobytes.
By default: 600 MB
Can be modified manually if the requirement can't be met on the host.


---


## Source: how-to-pass-a-proxy-address-during-oneagent-installation-on-linux.md


---
title: How to pass a proxy address during OneAgent installation on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-linux
scraped: 2026-02-17T04:52:58.118580
---

# How to pass a proxy address during OneAgent installation on Linux

# How to pass a proxy address during OneAgent installation on Linux

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

The OneAgent installer recognizes the `--set-proxy` (recommended since version 1.185) or `PROXY` parameters. The value of these parameters is the proxy server address. Add the port number following a colon, for example `172.1.1.128:8080`. For an authenticating proxy you can specify username and password like this `username:password@172.1.1.128:8080` where both username and password need to be URL encoded. We also support IPv6 addresses.

Parameter names are case sensitive, so use `ALL CAPS` for parameter names.

## Passing a proxy address to the installer

Let's say you're running an openSUSE server, you've downloaded your OneAgent installer to the `/tmp` directory and your proxy IP address is `10.1.1.5`. In such a scenario you would begin the installation like this:

```
cd /tmp



chmod +x Dynatrace-OneAgent-Linux-0.5.0-20140217-175809.sh



su -c 'Dynatrace-OneAgent-Linux-0.5.0-20140217-175809.sh --set-proxy=10.1.1.5'
```

## Change proxy after installation

If you need to change the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").


---


## Source: install-oneagent-on-linux.md


---
title: Install OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux
scraped: 2026-02-17T04:53:04.811580
---

# Install OneAgent on Linux

# Install OneAgent on Linux

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 22, 2026

This page describes how to download and install Dynatrace OneAgent on Linux.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements

You can install OneAgent on any Linux system that's [supported by Dynatrace](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks."), regardless of the packaging system your distribution depends on.

### Permissions

* You need [Download/install OneAgent](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") permissions to download and install OneAgent.
* You only need [root rights](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.") to start OneAgent installation. This requires that your system meets [specific requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#system-req "Find out when Dynatrace OneAgent requires root privileges on Linux."). Otherwise, add the `NON_ROOT_MODE=0` parameter to the installation command to disable OneAgent non-privileged mode.
* You need permissions and credentials for restarting all your application services.

### Resources

* Check the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.").
* Your host requires 200 MB free memory to run OneAgent installation and update.
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### Limitations

There are certain limitations when deploying OneAgent on a Linux host Oracle Database Server 19c and/or with mounted NFS drives. See [Troubleshoot OneAgent installation](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.").

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.
3. Paste a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you'll use later.
4. **Select installer type**
   OneAgent supports the following CPU architectures:

   * `Linux ARM` - ARM64 (AARch64) including [AWS Graviton processorsï»¿](https://aws.amazon.com/ec2/graviton/)
   * `PowerPC (BE)` - 64-bit PowerPC (ppc64be) [Learn more](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux.")
   * `PowerPC (LE)` - 64-bit PowerPC (ppc64le)
   * `s390` - 64-bit IBM Z mainframe (s390) [Learn more](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.")
   * `x86-64` - 64-bit Intel/AMD
5. **Download the installer**  
   Paste the provided command into your terminal window and execute it.
6. **Verify the signature**  
   After the download is complete, select  **Copy** in the **Verify signature** box to copy the `wget` command to the clipboard, then paste the provided command into your terminal window and execute it. Make sure your system is up to date, especially SSL and related certificate libraries.
7. Optional **Set customized options**

   * Set a [network zone](/docs/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.
   * If your environment is segmented (for example, into development and production), consider [organizing your hosts into host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").
   * You can override automatically detected [host name](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.
   * You can also apply [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the host to organize your monitored environments in a meaningful way.
   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * Disable [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

   OneAgent command-line installer provides more options to [customize your installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
8. **Run the installer**  
   Paste the command into your terminal window and execute it. You'll need root access only to start OneAgent installation. Elevated privileges are dropped as soon as Dynatrace OneAgent is deployed.

   If youâre on an Ubuntu Server

   ```
   sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

   If youâre using Red Hat Enterprise Linux

   ```
   su -c '/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh'
   ```

   If you start a root session

   ```
   /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

* If you plan to download Dynatrace OneAgent directly to a server, note that outdated or missing libraries (for example, CA certificates or OpenSSL) prevent the installer from downloading.
* Dynatrace uses encrypted connections. OpenSSL is required to enable `wget` to access the server. You can also download the installer by selecting **Download OneAgent installer** in the page footer and saving the installer script to any location you want, which bypasses the `wget` command altogether.

What happens during installation?

Dynatrace OneAgent is a set of specialized services configured specifically for your monitoring environment. The role of these services is to monitor various aspects of your hosts, including hardware, operating system, and application processes.

During the installation process, the installer:

* Installs executable code and libraries that are used by Dynatrace OneAgent. OneAgent binaries are installed in the `/opt/dynatrace/oneagent` directory and startup scripts are created in `/etc/init.d` (on systemd systems, startup scripts are created in `/etc/systemd/system/`). One of the Linux OneAgent components, `liboneagentproc.so`, is located in the system library directory (`/lib` or `/lib64` depending on your architecture) and is enabled at `/etc/ld.so.preload`.
* Creates its own user (`dtuser`). This user is created without a password. It's not possible to login with this user. For security purposes, services that donât require root privileges will run under this user. Installation, however, still requires root access.
* Checks the systemâs global proxy settings.
* Checks for a connection to Dynatrace Server or ActiveGate (if you installed ActiveGate and downloaded the OneAgent installer after ActiveGate was connected to Dynatrace).
* Detects all SELinux-aware applications and adjusts the SELinux security policy accordingly.
* Allows Dynatrace OneAgent to inject its own libraries into monitored processes.
* Modifies the core pattern configuration so that OneAgent can detect and report process crashes. The original core\_pattern configuration will still work following installation and will be preserved in `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`, where you can define your own core settings using the format as specified in [Linux Programmer's Manualï»¿](https://man7.org/linux/man-pages/man5/core.5.html).

For a summary of the changes made to your system by OneAgent installation, see [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.


---


## Source: install-oneagent-on-ppc-be-linux.md


---
title: Install OneAgent on PPC BE Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux
scraped: 2026-02-06T16:30:49.933952
---

# Install OneAgent on PPC BE Linux

# Install OneAgent on PPC BE Linux

* Latest Dynatrace
* 3-min read
* Updated on Jan 22, 2026

To install Dynatrace OneAgent when you have a Dynatrace SaaS deployment, go to [Dynatrace.comï»¿](https://www.dynatrace.com) and **Login** using the username and password you received from Dynatrace in your signup confirmation email. If you have a Dynatrace Managed deployment, [access the Cluster Management Console and choose the environmentï»¿](https://docs.dynatrace.com/managed/shortlink/managed-monitoring-environment) you want to monitor. Then continue with the installation steps provided below.

## Requirements

* You need the [permissions](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.") for the following actions:

  + To create a directory where you want to install OneAgent
  + To change firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).
  + To restart your application services
* You also need to check the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.").
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on whether your Dynatrace deployment is SaaS or Managed, and depending on your network layout and security settings, you may choose to either provide direct access to the Dynatrace cluster, or you can [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

* On PPC BE Linux, OneAgent supports only Java and Apache/IHS.
* You don't need root access to install OneAgent on PPC BE Linux.
* You can install OneAgent in any directory.

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.
3. Choose the **PowerPC (BE)** installer type from the list. Copy the command provided in the **Use this command on the target host to download OneAgent for Linux PowerPC (BE)** text field
4. Login to your PPC BE Linux host and execute the command you copied from Dynatrace.

   * If you plan to download Dynatrace OneAgent directly to a server, note that outdated or missing libraries (for example, CA certificates or OpenSSL) will prevent the download.
   * Dynatrace uses encrypted connections. OpenSSL is required to enable `wget` to access the server. You can also download the ZIP archive of OneAgent by clicking the **Download OneAgent installer** link in the page footer and saving the installer script to any location; this bypasses the `wget` command altogether.
5. In your file system, create a folder for OneAgent installation. For example, `/opt/dynatrace/oneagent`.
6. Unzip the ZIP archive of OneAgent into the newly created folder.

   All monitored applications must to be able to read the OneAgent library. Ensure that the permissions allow this.
7. You have two options now: either monitor every application on your host or just a single application.

   All applications

   Single application

   To automatically monitor every application on your host, enable the `liboneagentproc.so` component of OneAgent. This is located in the system library directory (`/lib` or `/lib64` depending on your architecture), at `/etc/ld.so.preload`.

   ## You've arrived!

   Great, the setup is complete! You can now take a look around your new monitoring environment.

   You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

   One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.

   To monitor a single application, you need to restart it first. Prepend the application start command with the following commands:

   ```
   DT_HOME=<installation directory>



   export DT_HOME



   LD_PRELOAD=$DT_HOME/agent/<system library>/liboneagentproc.so



   export LD_PRELOAD
   ```

   Where:

   * `<installation directory>` is the directory where OneAgent is installed
   * `<system library>` is `/lib` or `/lib64` depending on your architecture

   ## You've arrived!

   Great, setup is complete! You can now take a look around your new monitoring environment. If you have a SaaS deployment, you can access your monitoring environment anytime by going to [Dynatrace.comï»¿](https://www.dynatrace.com) and clicking the **Login** button in the upper-right corner. If you have a Dynatrace Managed deployment, you can [access your monitoring environment through the Cluster Management Consoleï»¿](https://docs.dynatrace.com/managed/shortlink/managed-monitoring-environment).


---


## Source: linux-non-privileged.md


---
title: OneAgent non-privileged mode on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged
scraped: 2026-02-17T04:52:41.347246
---

# OneAgent non-privileged mode on Linux

# OneAgent non-privileged mode on Linux

* Latest Dynatrace
* 7-min read
* Published Jul 19, 2017

By default, OneAgent is installed in the non-privileged mode, in which superuser privileges are used once to initiate the installation process.

OneAgent is then run under an unprivileged user, retaining the complete set of functionalities.

## System requirements

To install OneAgent in non-privileged mode, your system must meet the following requirements:

* The filesystem must support [extended attributesï»¿](https://man7.org/linux/man-pages/man7/xattr.7.html).
* The system must have `libcap2` installed. For example, the default Red Hat Enterprise Linux 5 installation doesn't have `libcap2`.
* The filesystem must not be mounted as `noexec` or `nosuid`.
* Linux Filesystem Capabilities must be enabled. For example, SUSE Linux Enterprise Server 11 has Linux Filesystem Capabilities disabled by default. For more information, see [Non-privileged mode and Linux Filesystem Capabilities](#cap) below.

See [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#permissions "Learn about Dynatrace OneAgent security and modifications to your Linux-based system") to learn about monitoring actions executed by OneAgent that require privileged access.

## Privileges during installation

When run in non-privileged mode, the OneAgent installer requires superuser privileges to:

* Set file capabilities for OneAgent binaries located at `/opt/dynatrace/oneagent/agent/lib[64]/*`.
* Invoke the `oneagent` service script to start `oneagentwatchdog`.
* On systems with systemd, communicate with systemd daemon via d-bus to run the following commands:

  + `systemctl <start|stop|enable|disable> oneagent.service`
  + `systemctl daemon-reload`
* On systems with SysV, execute `/sbin/chkconfig` to add the `oneagent` service script to autostart or to remove it.
* Write to `/proc/sys/kernel/core_pattern`.

Superuser privileges are dropped when the Dynatrace OneAgent service script is executed:

* On systems with systemd, the unprivileged user is included in the service definition (unit file). The systemd daemon thus runs the OneAgent service script in unprivileged mode.
* On systems with SysV, the privileges are dropped in the script when starting the OneAgent Watchdog process.

## Linux System Capabilities

Dynatrace OneAgent Watchdog starts and runs all other processes under an unprivileged user without superuser access. OneAgent binaries leverage the following Linux System Capabilities.

| Binary | Linux System Capabilities |
| --- | --- |
| oneagentwatchdog | `cap_sys_resource`[1](#fn-1-1-def)- for setting [system resource limitsï»¿](https://man7.org/linux/man-pages/man3/getrlimit.3p.html) when starting OneAgent processes |
| oneagentos | `cap_dac_override`[2](#fn-1-2-def) - for filesystem access `cap_chown`[2](#fn-1-2-def) [3](#fn-1-3-def) - for setting ownership of files replaced in the filesystem (e.g., `runc` binary) `cap_fowner` [2](#fn-1-2-def) - for setting ownership of files replaced in the filesystem `cap_sys_ptrace` - for reading data from `/proc` pseudo-filesystem and tracing processes `cap_sys_resource`[3](#fn-1-3-def) - for reading processes resource limits `cap_setuid`[4](#fn-1-4-def) - for temporary elevation of privileges to execute certain operations; for details, see [Automatic updates and operation](#autoupdate) `cap_kill` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) `cap_setfcap` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) `cap_fsetid` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) |
| oneagentnettracer | `cap_bpf` (kernel >=5.8)[7](#fn-1-7-def) `cap_perfmon` (kernel >=5.8)[7](#fn-1-7-def) `cap_sys_admin` (kernel <5.8, or when `cap_bpf` is explicitly blocked)[7](#fn-1-7-def) `cap_dac_override` `cap_sys_ptrace` `cap_sys_resource` |
| oneagentnetwork | `cap_net_raw` - for opening raw sockets `cap_net_admin`[8](#fn-1-8-def)- for reading network interface information |
| oneagentloganalytics | `cap_dac_read_search` - for access to all logs stored on host `cap_sys_ptrace` - for reading data from `/proc` pseudo-filesystem |
| oneagentplugin | `cap_set_gid`[1](#fn-1-1-def)- for adding docker to the process supplementary groups list, which allows for the container data to be retrieved |
| oneagenthelper[9](#fn-1-9-def) | `cap_sys_admin` - for `mount()` syscall `cap_dac_override` - for inspection and modification of filesystems of the running containers `cap_sys_ptrace` - for tracing the `Docker` daemon `cap_sys_chroot` - for `chroot()` syscall `cap_fowner` - for changing ownership and permissions of files within container filesystem `cap_fsetid` - for changing ownership and permissions of files within container filesystem |
| OneAgent Installer executed during auto-update | `cap_dac_override` - for filesystem access `cap_chown` - for filesystem access `cap_fowner` - for filesystem access `cap_fsetid` - for filesystem access `cap_kill` - to be able to signal all the running processes, e.g. stopped orphaned OneAgent processes `cap_setfcap` - for setting Linux Filesystem capabilities file capabilities on agent binaries during the installation |
| oneagentosconfig | `cap_setuid`[6](#fn-1-6-def)- for execution of privileged operations during the installation process `cap_setgid`[6](#fn-1-6-def)- for setting group ownership of files during the installation process |
| oneagenteventstracer | `cap_sys_admin` - for `perf_event_open()` syscall `cap_dac_override` - for access to `/sys/kernel/debug/tracing` |
| oneagentdmidecode | `cap_dac_override` - for filesystem access |
| oneagentmntconstat | `cap_dac_read_search` - for retrieving disk occupation stats with `statvfs64()` `cap_sys_chroot` - for `setns()` syscall `cap_sys_admin` - for `setns()` syscall `cap_sys_ptrace` - for accessing `/proc/1/ns` |
| oneagentebpfdiscovery | `cap_bpf` (kernel >=5.8)[7](#fn-1-7-def) `cap_perfmon` (kernel >=5.8)[7](#fn-1-7-def) `cap_sys_admin` (kernel <5.8, or when `cap_bpf` is explicitly blocked)[7](#fn-1-7-def) `cap_dac_override` - for write access to /sys/kernel/debug/tracing `cap_sys_resource` - for removing memory usage limitation of the bpf program |

1

Required only during initialization phase and is unconditionally dropped afterwards.

2

Not used if [auto-updates](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#enable-or-disable-auto-update "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") and [automatic injection](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") are disabled.

3

Kept in permitted set only and raised to the effective set when needed.

4

Only if ambient capabilities aren't supported.

5

Not used if [auto-updates](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#enable-or-disable-auto-update "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") are disabled.

6

Only if ambient capabilities are supported.

7

Only for kernels 5.8 and newer, unless usage of unprivileged `cap_bpf` is [blocked by the OSï»¿](https://ubuntu.com/blog/whats-new-in-security-for-ubuntu-21-10), then it fallbacks to `cap_sys_admin`. For older kernel versions, `cap_sys_admin` is enabled instead.

8

Only on kernels older than 2.6.33.

9

Not started if [automatic injection](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") is disabled.

Enable Linux Filesystem Capabilities

Linux Filesystem Capabilities are required to install OneAgent in non-privileged mode. SUSE Linux Enterprise Server 11 has Linux Filesystem Capabilities disabled by default. These capabilities might also be disabled in other supported Linux distributions or as the result of a custom configuration. The OneAgent installer prints the following message if Linux Filesystem Capabilities are disabled:

```
Warning: Failed to enable non-privileged mode, kernel does not support file capabilities.
```

You can also check the kernel boot options to see if Linux Filesystem Capabilities are enabled. Run the following command to check your kernel boot options.

```
cat /proc/cmdline
```

If you find `file_caps=1` in the output, your setup is fine.

To enable Linux Filesystem Capabilities, add `file_caps=1` to your kernel boot options. For example, on SUSE Linux Enterprise Server 11, use [YaSTï»¿](https://doc.opensuse.org/documentation/leap/reference/html/book-reference/cha-grub2.html#sec-grub2-yast2-config), edit kernel boot options, add `file_caps=1`, and reboot the machine.

## Privileges during automatic updates and operation

The scope of privileges required by OneAgent depends on whether the kernel supports Linux ambient capabilities. As a general rule, kernel 4.3+ supports ambient capabilities. However, in the case of Red Hat Enterprise Linux, these may be supported in older kernel versions because of the Red Hat policy to backport patches. This makes ambient capabilities supported by kernel versions as old as 3.10.x.

Kernels with ambient capabilities (version 4.3+)

Kernels without ambient capabilities (version 2.6.26 to 4.3)

During an automatic update, the installer starts under an unprivileged `dtuser` with proper ambient capabilities set. OneAgent doesn't require root access to perform an automatic update.

Red Hat Enterprise Linux 7 has a too low `systemd` (v219 instead of the required v221), and to be able to run automatic updates in non-privileged mode, we're temporarily elevating the privileges to run `systemctl <start|stop|enable|disable> oneagent.service`.

OneAgent will work under the non-privileged `dtuser` in the majority of cases. When the kernel doesn't provide ambient capabilities, it automatically elevates its privileges to the superuser level using `setuid(0)` in the following cases:

* OneAgent automatic updates
* Host OSI ID generation on Azure hosts
* Docker containers properties detection
* Self-diagnostics

If you don't want to grant the superuser permission level to OneAgent, you can disable it by adding the `DISABLE_ROOT_FALLBACK=1` parameter to the OneAgent installation command. For example:

`sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh NON_ROOT_MODE=1 DISABLE_ROOT_FALLBACK=1`

In such cases, you must perform [manual updates on individual hosts](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux#manual-update "Learn about the different ways to update OneAgent on Linux."). We don't recommend using the `DISABLE_ROOT_FALLBACK=1` parameter for OneAgents on Azure or Docker containers.

## How do I know if OneAgent operates in non-privileged mode?

The installer prints a message at the end of OneAgent installation. Depending on the kernel version and its support for ambient capabilities, you will see one of the following messages:

* `Non-privileged mode is enabled`  
  The kernel supports ambient capabilities, the root access is not used for updates or operation.
* `Enabled non-privileged mode, but ambient capabilities are not supported by kernel`  
  The kernel is within the minimum supported version, but due to non-supported ambient capabilities, OneAgent needs to elevate privileges in select cases, see above.
* `Failed to enable non-privileged mode`  
  The kernel doesn't meet the minimum version requirements to enable non-privileged mode.


---


## Source: oneagent-security-linux.md


---
title: OneAgent security on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux
scraped: 2026-02-17T04:53:01.482849
---

# OneAgent security on Linux

# OneAgent security on Linux

* Latest Dynatrace
* 5-min read
* Published Nov 11, 2020

To fully automate the monitoring of your operating systems, processes, and network interfaces, OneAgent performs the following changes to your system.

OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Permissions

By default, OneAgent is installed in non-privileged mode, in which superuser privileges are used once to initiate the installation process. OneAgent is then run under an unprivileged user, retaining the complete set of functionalities. For details and system requirements, see [OneAgent non-privileged mode on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.")

### Operation

OneAgent performs the following privileged operations. Depending on whether OneAgent runs in non-privileged or privileged mode, the scope of operations is the same, only the underlying mechanism differs. In privileged mode, OneAgent runs as root, while non-privileged mode utilizes the Linux System Capabilities.

* Access the list of open sockets for each process.
* Access the list of libraries loaded for each process.
* Access the name and path of the executable file for each process.
* Access command-line parameters for each process.
* Monitor network traffic.
* Read application configuration files.
* Parse executables for Go Discovery.
* Gather monitoring data related to Docker containers.

If you have Log Monitoring enabled, root privileges are also required for:

* Accessing system logs: `/var/log/syslog` and `/var/log/messages`.
* Accessing the list of open file handlers for each process (`/proc` file system).
* Accessing the log file for each process.

## Operating system changes

The OneAgent installer performs the following changes to your system:

* The `dtuser` user is created. You can change the default name using the `USER` [installation parameter](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#user "Learn how to use the Linux installer with command line parameters.").
* The `oneagent` service is registered in the system init.
* `ABRT` (Red Hat) and `Apport` (Debian) services are stopped and disabled.
* A custom SELinux module is installed on systems with SELinux enabled. The sources of the SELinux module installed by the OneAgent installer are available under `{install-dir}/agent/SELinuxPolicy`, `/opt/dynatrace/oneagent/agent/SELinuxPolicy` by default.
* Installs OneAgent components in the system library directories.
* Sets up `/etc/ld.so.preload` to automatically monitor processes.

## Files modified

### Installation

The OneAgent installer modifies the following system files:

* `/proc/sys/kernel/core_pattern` and `/etc/sysctl.conf` are modified to enable core dump processing by `oneagentdumpproc`. The original `core_pattern` configuration will still work following installation and will be preserved in `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`, where you can define your own core settings using the format as specified in [Linux Programmer's Manualï»¿](https://man7.org/linux/man-pages/man5/core.5.html). See [Linux core dump handling](/docs/observe/application-observability/profiling-and-optimization/crash-analysis#linux-core-dump-handling "Learn how Dynatrace can help you gain insight into process crashes.") for more information.
* `/etc/ld.so.preload` is modified to enable auto-injection into processes.

### Operation

OneAgent modifies the following files during its operation:

* The OneAgent wrapper overwrites the `/var/vcap/packages/runc/bin/runc` file (Garden runc) to allow injection. This happens periodically during runtime. The original file is stored as `runc-original` and is restored by the [uninstall script](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").
* On [CRI-Oï»¿](https://cri-o.io/) hosts (OCI-based implementation of Kubernetes Container Runtime Interface), the crio hook (`oneagent_crio_injection-0.1.0.json`) is copied to the path specified in the `hooks_dir` parameter of the CRI-O configuration file (`/etc/crio/crio.conf`). If the `hooks_dir` parameter is not set, one of the default paths is used, either `/etc/containers/oci/hooks.d/` or `/usr/share/containers/oci/hooks.d/`. The hook is removed by the uninstall script.

## Files added

### Installation

The OneAgent installer adds the following files to your system:

* OneAgent binaries and configuration files are saved in `/opt/dynatrace/oneagent`. Note that you can change the location using the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.") parameter.
* Startup scripts are copied to `/etc/init.d` on systems with SystemV and to `/etc/systemd/system` on systems with systemd.
* `liboneagentproc.so` is placed in the system library directories, which vary depending on a distribution. For example,

  + Ubuntu 14.04 (with 32-bit libraries installed): `/lib32` and `/lib/x86_64-linux-gnu`
  + Fedora 25: `/lib64`
  + OpenSUSE 42.2: `/lib` and `/lib64`
  + CentOS 7.3 and Red Hat Enterprise Linux 6: `/lib` and `/lib64`

### Operation

* OneAgent temporary files and runtime configuration are saved in `/var/lib/dynatrace/oneagent/runtime`.
* OneAgent persistent configuration is saved in `/var/lib/dynatrace/oneagent/agent/config`.
* Large runtime data, such as memory dumps, is saved in `/var/lib/dynatrace/oneagent/datastorage`. Note that you can change the location of large runtime data using the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters.") parameter.

## System logs downloaded by OneAgent

OneAgent downloads certain system logs so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or automatic updates.

* `/var/log/boot.log`
* `/var/log/dmesg`
* `/var/log/dpkg.log`
* `/var/log/kern.log`
* `/var/log/messages`
* `/var/log/syslog`
* `/var/log/yum.log`
* `/var/log/audit/audit.log`
* `/var/log/zypper.log`
* `/etc/nsswitch.conf`
* Output of `/usr/sbin/apparmor_status` command
* Output of `/bin/journalctl --utc -a -n 10000` command

Revoking access to system logs

To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.  
For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Globally writable directories

The [OneAgent directory structure](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.") contains globally writable directories (`1777` permissions). Changing these permissions by users is not supported.

### OneAgent injection mechanism

Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.

Similarly, certain log files require global write permissions (`666`) to allow applications running under various users to write to them.

### System security

We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.

* We keep the number of globally writable directories as limited as possible.
* All these directories have a sticky bit set (actual permissions are `1777`). Only the file's owner, the directory's owner, or the root user can modify the files in the directory. This is standard practice that makes the permissions more robust. It's also used for the Linux `/tmp` directory to prevent ordinary users from deleting or moving other users' files.


---


## Source: flatcar-os.md


---
title: Flatcar support on SELinux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/flatcar-os
scraped: 2026-02-17T04:52:46.470707
---

# Flatcar support on SELinux

# Flatcar support on SELinux

* Latest Dynatrace
* 1-min read
* Published May 30, 2023

OneAgent can now be deployed on [Flatcarï»¿](https://dt-url.net/u5034bo). However, due to certain limitations with how SELinux operates on this operating system, you need to address the following configuration constraints:

* Flatcar operates on a read-only filesystem. As a result, if you intend to use SELinux with OneAgent, it requires a specific configuration. For more information about container compatibility with SELinux policy, see the following Flatcar documentation: [Check a containerâs compatibility with SELinux policyï»¿](https://dt-url.net/ns0342m).
* Use a default path to install OneAgent with SELinux enabled.

* By default, Flatcar uses the Multi-Category Security (MCS) policy. To ensure compatibility, you need to change this setting to the `targeted` policy in the `/etc/selinux/config` file.

  ```
  SELINUXTYPE=targeted
  ```


---


## Source: how-to-enable-deep-monitoring-for-applications-confined-by-apparmor.md


---
title: How to enable deep monitoring for applications confined by AppArmor
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor
scraped: 2026-02-17T04:52:48.128676
---

# How to enable deep monitoring for applications confined by AppArmor

# How to enable deep monitoring for applications confined by AppArmor

* Latest Dynatrace
* 2-min read
* Published Aug 08, 2017

AppArmor is a mandatory access control system that restricts applications to a limited set of resources. For each confined application, a profile exists that specifies what operations the application is allowed to perform as well as the paths in the file system that the application is allowed to access. In order to enable deep monitoring of applications confined by AppArmor, a custom rule set for OneAgent must be included in the profiles of these applications.

The definition of a rule set, as well as a walkthrough for adding a rule set to an existing profile, is presented in the example below. In this example, we enable deep monitoring of an Apache Tomcat web server, for which the bootstrapper script is located under `/usr/sbin/tomcat-sysd`.

We assume that the directory structure for AppArmor is the following:

```
/etc/apparmor.d/



|--- usr.sbin.tomcat-sysd
```

Where `usr.sbin.tomcat-sysd` is the file that defines the AppArmor profile for Tomcat.

1. Create a new directory and a new rule set for OneAgent within this directory named `agentinjection`.

   ```
   /etc/apparmor.d/



   |--- usr.sbin.tomcat-sysd



   |--- dynatrace-oneagent



   |--- agentinjection
   ```
2. The content of `/etc/apparmor.d/dynatrace-oneagent/agentinjection` should be as follows:

   ```
   #include <abstractions/base>



   #include <abstractions/nameservice>



   # Process Agent injection



   /etc/ld.so.preload r,



   # Host identifier calculation



   /sys/class/net/ r,



   /sys/devices/virtual/net/** r,



   /sys/devices/*/*{,/*}/net/** r,



   # OneAgent directories



   /opt/dynatrace/oneagent/agent/** mr,



   /var/lib/dynatrace/oneagent/** r,



   /var/lib/dynatrace/oneagent/agent/runtime/** w,



   /var/lib/dynatrace/oneagent/agent/config/{discovery_entry_point,ruxit_shm_v*} w,



   /var/lib/dynatrace/enrichment/** r,



   # This path must be adjusted if LOG_PATH installation parameter was used



   /var/log/dynatrace/oneagent/** rkw,



   # This path must be adjusted if DATA_STORAGE installation parameter was used



   /var/lib/dynatrace/oneagent/datastorage/** rkw,



   # Needed for Process Agent to determine whether specialized agent should be loaded and to calculate PGI ID



   /proc/[0-9]*/{cgroup,cmdline,environ,maps,mem,mountinfo,stat,statm,task/*/maps,task/*/mem} r,



   # Miscellaneous



   /dev/random rw,



   /etc/os-release r,



   /proc/sys/fs/file-nr r,



   /proc/sys/kernel/hostname r,



   /proc/{uptime,vmstat} r,



   /sys/devices/system/cpu/ r,



   /sys/fs/cgroup{,/,/**} r,



   /tmp/** rw,



   /var/tmp/ r,



   /var/tmp/** rw,



   /{,var/}run/utmp rk,



   /proc/cgroups r,
   ```

   If you used the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") installation parameter to define a custom directory dedicated to storing large runtime data, edit the following line and add your custom directory

   ```
   # This path must be adjusted if DATA_STORAGE installation parameter was used



   /var/lib/dynatrace/oneagent/datastorage/** rkw,
   ```
3. Include the rule set in the Tomcat profile (`/etc/apparmor.d/usr.sbin.tomcat-sysd`).

   ```
   /usr/sbin/tomcat-sysd {



   #include <dynatrace-oneagent/agentinjection>



   ... (rest of the rules that were already present in the profile)



   }
   ```
4. Verify that the defined profile works correctly:

   1. Reload AppArmor service.
   2. Restart Tomcat.
   3. Verify on the Web UI that the deep monitoring is working for Tomcat process.
   4. Inspect audit logs to ensure that there are no AppArmor denials.

Please keep in mind that although the rule set provided in this example was extensively tested, it may need to be extended or modified due to environmental differences and the custom installation path for OneAgent is not supported.

### Warnings for access denials in audit logs

In case you experience denials related to OneAgent for other processes in the system, add the following subset of rules to the profiles of these processes.

```
# Process injection



/etc/ld.so.preload r,



/etc/oneagentproc/ld.so.preload r,



/var/log/dynatrace/oneagent/process/* rkw,
```

Although this step is optional because failed injections of OneAgent to other processes won't affect the functionality of your applications. Still, it may be required if you are running an IDS or other automated system that reports warnings for access denials found in audit logs.


---


## Source: stop-restart-oneagent-on-linux.md


---
title: Stop/restart OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux
scraped: 2026-02-17T04:53:03.143796
---

# Stop/restart OneAgent on Linux

# Stop/restart OneAgent on Linux

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:

1. Go to **Settings > Monitoring overview**.
2. Click the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.
3. Slide the **Monitoring** switch to the **Off** position.
4. Restart all processes for which monitoring has been disabled.

Hot cloning

Hot cloning is generally not supported by OneAgent due to host ID generation requirements. When hot cloning a host with OneAgent installed, follow these steps to ensure proper functionality:

1. Stop OneAgent on the original host.
2. Clone the host.
3. Start OneAgent.
4. Perform process restarts on the new host.

## Restart using OneAgent command-line interface

When you use the `set` parameters, you need to restart OneAgent service to apply changes. You can use the `--restart-service` parameter with the command that triggers the restart automatically. In some cases you'll also need to restart monitored applications. You can also use the restart parameter on its own, without other parameters. See an example command below.

```
./oneagentctl --set-proxy=my-proxy.com --restart-service
```

For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Stop OneAgent using the command line

If you use configuration management tools like Puppet or Ansible, you can alternatively stop the OneAgent service using the following command:

* for systems with SystemV: `service oneagent stop`
* for systems with systemd: `systemctl stop oneagent`

where `oneagent` is the `init.d` script for OneAgent.

If you stop OneAgent service, monitoring will be disabled until the service is restarted.

## Start OneAgent using the command line

To start Dynatrace OneAgent again, use the following command:

* for systems with SystemV: `service oneagent start`
* for systems with systemd: `systemctl start oneagent`

where `oneagent` is the `init.d` script for OneAgent.

Learn more about [how Dynatrace interacts with your OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").


---


## Source: uninstall-oneagent-on-linux.md


---
title: Uninstall OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux
scraped: 2026-02-17T04:52:52.958090
---

# Uninstall OneAgent on Linux

# Uninstall OneAgent on Linux

* Latest Dynatrace
* 1-min read
* Updated on Oct 20, 2025

OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system.

Go to the `/opt/dynatrace/oneagent/agent` directory and, using root rights, run the `uninstall.sh` script.

## Following uninstallation

Following uninstallation, log files, the user running OneAgent, and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.

For a complete OneAgent uninstallation, remove the following:

* Log files located at:

  + OneAgent version 1.203+: `/var/log/dynatrace/oneagent`
  + OneAgent version 1.201 and earlier: `/opt/dynatrace/oneagent/log`
* Configuration files located at `/var/lib/dynatrace/oneagent/agent/config`.
* The user running OneAgent, `dtuser`.
* Optional If you use a custom installation path, the installer creates a symbolic link in the default directory (`/opt/dynatrace/oneagent`) to the custom installation path.
  This symbolic link needs to be removed manually after OneAgent is uninstalled.
  For more information, see [Installation path](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.").


---


## Source: update-oneagent-on-linux.md


---
title: Update OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux
scraped: 2026-02-17T04:53:06.458186
---

# Update OneAgent on Linux

# Update OneAgent on Linux

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

OneAgent installed in full-stack mode has a built-in, configurable auto-update mechanism.

See [OneAgent update](/docs/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") for an overview of OneAgent update, including how to monitor updates and how to create update windows.

## Configure OneAgent updates

You can configure OneAgent update globally, per host group, and per host.

Configure global OneAgent update

When automatic updates are turned on globally, whenever a new version of OneAgent becomes available, all of your installed OneAgent instancesâexcept where you have turned off auto-updates at the host group or host levelâwill automatically download the update and upgrade their binaries and configuration files.

Automatic update settings at the host group and individual host level override global settings.

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. Select one of the update options:

   * **Automatic updates at earliest convenience**  
     Update all OneAgents automatically, regardless of update windows.
   * **Automatic updates during update windows**  
     Update all OneAgents automatically during the selected update window.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host group OneAgent update

OneAgent update settings at the host group level override global settings and are overridden by settings at the host level.

1. Open the **Host group settings** page.  
   Access alternatives:

   * Go to **Settings** > **Monitoring** > **Monitoring overview**, find any host that is in the host group you want to configure, and select the host group name (not the host name).
   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**, open a host page, and expand the **Properties and tags** section. If the host belongs to a group, there is a link to it under **Host group**.
   * Go to **Deployment Status** > **OneAgents**. If a host belongs to a host group, a link to the host group settings page is displayed under the host name.
2. On the **Host group settings** page, select **OneAgent updates** on the left side of the page.
3. Select one of the update options:

   * **Inherit global update settings**  
     Follow the global update settings for updating OneAgents in this host group.

     + The current global setting is displayed in parentheses on this line.
     + To go to the global configuration page, select the `global` link.
   * **Automatic updates at earliest convenience**  
     Update all OneAgents in this host group automatically, regardless of update windows. Ignore the global update settings.
   * **Automatic updates during update windows**  
     Update all OneAgents in this host group automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents in this host group. Ignore the global update settings.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host-level OneAgent update

OneAgent update settings at the host level override OneAgent update settings at the global and host group levels.

1. Open the **Host** page for the host you want to configure.  
   Access options:

   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and then select the host.
   * Go to **Settings** > **Monitoring** > **Monitoring overview**, select the **Hosts** tab, and then select the host.
2. On the **Host** page, open the browse menu (**â¦**) and select **Settings**.
3. Select **OneAgent updates** on the left side of the page.
4. Select one of the update options:

   * **Inheritâ¦**  
     Follow the host group or global update settings for updating this OneAgent.

     + If the selected host belongs to a host group, the current host group setting is displayed in parentheses on this line, and the group name is a link to the host group configuration page.
     + If the selected host does not belong to a host group, the global setting is displayed in parentheses on this line, and "global" is a link to the global configuration page (**Settings** > **Updates** > **OneAgent updates**).
   * **Automatic updates at earliest convenience**  
     Update this OneAgent automatically, regardless of update windows. Ignore the host group update settings.
   * **Automatic updates during update windows**  
     Update this OneAgent automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update this OneAgent. Ignore the global update settings.

Manually update OneAgent on individual hosts

To manually update OneAgent running on an individual host:

1. Go to **Settings > Monitoring > Monitoring overview**.
2. Select the **Hosts** tab.
3. To update OneAgent or download the latest version, select **Update** next to the name of the host you're interested in.

   The **Update** button appears only if the installed version of OneAgent on a specific host is outdated and if it is a full-stack OneAgent. This button doesn't appear with PaaS and standalone OneAgents.
4. Select **Update now**.  
   If the **Update now** button is disabled, you don't have permissions to download the installer.

Alternatively, you can download the latest version of the OneAgent installer, copy it manually to the target host, and perform installation directly on the target host.

Select OneAgent version to install on new hosts

To control which version of OneAgent is automatically installed on all new hosts:

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In **Update mode**, select **No automatic updates** to disable automatic OneAgent updates.

   For details on how to disable OneAgent automatic updates on Paas/Kubernetes, see [DynaKube parameters for Dynatrace Operator on Kubernetes/OpenShift](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
3. In **Target version**, select the version of OneAgent to install on all new hosts.

The selected OneAgent version is also used for PaaS integrations.

Select OneAgent version to update to

To select which version of OneAgent to update to

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In the **Target version** list, you can specify a particular version by OneAgent version number or select a relative target version:

   * **Latest stable version**  
     The most recent stable OneAgent version that is available in your environment. The actual version number is displayed in parentheses.
   * **Previous stable version**  
     The stable version before **Latest stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *two* less than the latest version number.
   * **Older stable version**  
     The stable version before **Previous stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *four* less than the latest version number.

* **Specific OneAgent version**

The target version is used for:

* Automatic updates
* Automatic updates during maintenance windows
* Manual updates when you select the version you want to update to

You can set the target version and update mode at:

* **Environment level**
  Affects all OneAgents of an environment. Is also used for Deployment API.
* **Host group**
  Affects all OneAgents of a host-group. Overrides the environment level. Does not affect Deployment API.
* **Host**
  Affects OneAgent on this host. Overrides host group and environment-level configuration. Does not affect Deployment API.

If you select an older version than a currently deployed version, you won't be able to downgrade OneAgent. You will need to install a newer version over an existing OneAgent version.

## System requirements

### Disk space

For details, see [OneAgent files and disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.")

### Free memory

Your host requires 200 MB free memory to run OneAgent update.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### OneAgent command-line interface

Run `oneagentctl` with the `--version` parameter. For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.


---


## Source: update-oneagent-on-ppc-be-linux.md


---
title: Update OneAgent on PPC BE Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-ppc-be-linux
scraped: 2026-02-17T04:52:49.743019
---

# Update OneAgent on PPC BE Linux

# Update OneAgent on PPC BE Linux

* Latest Dynatrace
* 1-min read
* Published Aug 21, 2019

To update an installed OneAgent instance on PPC BE follow the instructions below:

1. Redo all steps of the [initial installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux.") but install OneAgent to a new directory.
2. Stop all monitored processes.
3. Rename the current OneAgent installation directory (for example, `/opt/dynatrace/oneagent` to `/opt/dynatrace/oneagent-old`) and use the following command:

   ```
   mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old
   ```

   This folder can be deleted following OneAgent update.
4. Rename the updated OneAgent folder to point to the original installation directory (for example, from `/opt/dynatrace/oneagent-update` to `/opt/dynatrace/oneagent`) using the following command:

   ```
   mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent
   ```
5. Restart all processes that are to be monitored.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### OneAgent command-line interface

Run `oneagentctl` with the `--version` parameter. For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.


---


## Source: linux.md


---
title: OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux
scraped: 2026-02-17T04:45:48.790672
---

# OneAgent on Linux

# OneAgent on Linux

* Latest Dynatrace
* 1-min read
* Published Jul 19, 2017

Dynatrace supports OneAgent installation on Linux. For analytical information about the supported OneAgent capabilities for Linux, see the [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms."). For the supported Linux distributions, check the [OneAgent supported technologies and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Installation

[Disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.")

[OneAgent security](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system")

[OneAgent non-privileged mode on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.")

[Install OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.")

[Install OneAgent on PPC BE Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux.")

[Customize installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.")

[How to pass a proxy address](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-linux "Find out how to force Dynatrace OneAgent on Linux to use a proxy for communication with your environment.")

### Operation

[OneAgent files and logs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.")

[Update OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.")

[Update OneAgent on PPC BE Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-ppc-be-linux "Learn about the different ways to update OneAgent on PPC BE Linux.")

[Stop/restart OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux.")

[Uninstall OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.")

[How to enable deep monitoring for applications confined by AppArmor](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor "Read a step-by-step example of monitoring an application that's confined by AppArmor.")
[Flatcar support on SELinux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/flatcar-os "SELinux limitations and configuration")

### See also

[OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

[OneAgent aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.")

[Troubleshoot](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.")


---


## Source: install-oneagent-on-solaris.md


---
title: Install OneAgent on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris
scraped: 2026-02-17T04:52:34.765545
---

# Install OneAgent on Solaris

# Install OneAgent on Solaris

* Latest Dynatrace
* 7-min read
* Updated on Jan 22, 2026

This page describes how to download and install Dynatrace OneAgent on Solaris.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements

### Permissions

* You need administrator rights for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).
* You need permissions and credentials for restarting all your application services.

### Resources

All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### Limitations

* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.
* [Infrastructure Monitoring](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") mode isn't supported on Solaris hosts.

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Solaris**.
3. Choose the CPU architecture of your environment.
4. Provide a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes."). This token is required to download the OneAgent installer from your environment. If you don't have a PaaS token, you can generate one right in the UI. The token is automatically appended to the download command you'll use later.
5. Click **Copy** to copy the `wget` command.
6. Log into your Solaris host and execute the `wget` command.

   * The `wget` command isn't installed on Solaris by default. Either install it or use an alternative means of downloading OneAgent.
7. Create a folder on your local system for OneAgent (for example, `/opt/dynatrace/oneagent`) and unzip the zip-archive into the folder.

   In contrast to other platforms, root access isn't required for installation of OneAgent on Solaris. OneAgent can be installed in any directory.

   * As all monitored applications need to be able to read the library, ensure that the permissions allow this.

     + Give global read permissions to `/opt/dynatrace/oneagent`
     + Give global write permissions to `/opt/dynatrace/oneagent/logs`
   * Be sure to reference the folder correctly in the subsequent steps of your deployment.
8. On Solaris, Dynatrace only supports Java and Apache HTTP Server applications and as such you need to decide which applications to monitor. You can do this just for a single application, or shell wide. Just follow the relative instructions below.

   Monitoring a single application

   To monitor a single application, execute your command and prepend it with the following commands.

   ```
   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so



   export LD_PRELOAD_64



   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so



   export LD_PRELOAD
   ```

   The `DT_HOME` variable points to your OneAgent installation folder. You can omit either the 32-bit or 64-bit entry, depending on your environment.

   Configure WebSphere Application Server via the Administrative console

   The unified approach works just as well for WebSphere, however you may want to configure your WebSphere via the Administrative console. This works for OneAgent v1.141 and above.

   1. Start the WebSphere server via the WebSphere UI or the command line. For example: `/opt/ibm/WebSphere<version>/AppServer/bin/sh startServer.sh server1`
   2. Open the Administrative Console via the WebSphere UI or enter the URL in your web browser. For example:`http://localhost:9060/ibm/console`. When accessing the server remotely, specify the machine's hostname rather than `localhost`.
   3. Enter your user ID and password and then log in.
   4. Navigate to **Server** > **Application servers** > `[yourprofilename]`> **Java and Process Management** > **Process Definition** > **Environment Entries** > **New**.
   5. Add 3 entries to the list.

      ```
      DT_HOME=/opt/dynatrace/oneagent



      LD_PRELOAD_64=/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



      LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
      ```

      You can omit either the 32-bit or 64-bit entry, depending on your environment. The `DT_HOME` variable must point to your OneAgent installation folder.
   6. Apply the changes and save the configuration.

   Configure Oracle WebLogic via the startup script

   To monitor Oracle WebLogic you need to add the following lines to the WebLogic startup script (`startWebLogic.sh`)

   ```
   # Monitor WebLogic with Dynatrace OneAgent



   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so



   export LD_PRELOAD_64



   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so



   export LD_PRELOAD



   # WebLogic checks and startup, this is part of your script, add the 3 lines prior to this.



   echo "starting weblogic with Java version:"



   ${JAVA_HOME}/bin/java ${JAVA_VM} -version



   if [ "${WLS_REDIRECT_LOG}" = "" ] ; then



   echo "Starting WLS with line:"



   echo "${JAVA_HOME}/bin/java ${JAVA_VM} ${MEM_ARGS} ${JAVA_OPTIONS} -Dweblogic.Name=${SERVER_NAME}



   -Djava.security.policy=${WL_HOME}/server/lib/weblogic.policy ${PROXY_SETTINGS} ${SERVER_CLASS}"



   ${JAVA_HOME}/bin/java ${JAVA_VM} ${MEM_ARGS} ${JAVA_OPTIONS} -Dweblogic.Name=${SERVER_NAME}



   -Djava.security.policy=${WL_HOME}/server/lib/weblogic.policy ${PROXY_SETTINGS} ${SERVER_CLASS}



   else



   echo "Redirecting output from WLS window to ${WLS_REDIRECT_LOG}"



   ${JAVA_HOME}/bin/java ${JAVA_VM} ${MEM_ARGS} ${JAVA_OPTIONS} -Dweblogic.Name=${SERVER_NAME}



   -Djava.security.policy=${WL_HOME}/server/lib/weblogic.policy ${PROXY_SETTINGS}



   ${SERVER_CLASS} 2>&1 >"${WLS_REDIRECT_LOG}"



   fi
   ```

   You can omit either the 32-bit or 64-bit entry, depending on your environment. The `DT_HOME` variable must point to your OneAgent installation folder.

   Monitoring every Java and Apache HTTP service in your execution context

   You can set up OneAgent to monitor every application in your current application context. To do this, add the following lines to the startup script of the application you want to monitor. Ensure that they're executed prior to the application itself. You should not do this system-wide or for login users.

   OneAgent v1.141 and above

   OneAgent v1.137 to v1.139

   ```
   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so



   export LD_PRELOAD_64



   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so



   export LD_PRELOAD
   ```

   ```
   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   . $DT_HOME/dynatrace-agent64.sh



   . $DT_HOME/dynatrace-agent32.sh
   ```

   `LD_PRELOAD` will not carry over into `sudo` or `su` calls. Moreover, calling `sudo` in an execution context that has `LD_PRELOAD` set will lead to an error message that the library is in a non-secure location. This has no negative impact. This message can be ignored.

If you use the WebLogic admin server to restart managed nodes on Solaris, see [Troubleshoot OneAgent installation on Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris#weblogic-admin "Find out how to solve problems related to installing OneAgent on Solaris.") to learn how to modify the startup script.

## OneAgent versions older than v1.137 and fallback

If your OneAgent is older than v1.137, or if you have problems with the unified monitoring approach, you can inject OneAgent manually.

Manual OneAgent injection

Generic Java applications

Apache HTTP Server

Modify the command line of your Java application:

```
DT_HOME=/opt/dynatrace/oneagent



. $DT_HOME/dynatrace-java-env.sh 64



java $JAVA_OPTS <MainClass>
```

Make sure that you include the `$JAVA_OPTS` variable in your command. For 32-bit Java processes, omit the `64` parameter.

The following steps are required to configure Dynatrace to monitor Apache HTTP server or running on Solaris:

Edit your `httpd.conf` and add the following two lines in a location of your choice:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/solaris-<arch>-<bitness>/liboneagentloader.so



OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

Alternatively, if you prefer to leave your `httpd.conf` unchanged, you can specify the same directives using the command line:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/solaris-<arch>-<bitness>/liboneagentloader.so"



-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"



-k start
```

* `tenantUUID` is the environment ID of your Dynatrace environment that should be pulled from `dynatrace-env.sh` (located in the OneAgent installation root directory). The `tenantUUID` parameter is represented in the script as `DT_TENANT`.
* `tenantToken` is the token that OneAgent uses to connect to Dynatrace Server. It should be pulled from `dynatrace-env.sh` (located in the OneAgent installation root directory). The `tenantToken` parameter is represented in the script as `DT_TENANTTOKEN`.

  This token should not be confused with Dynatrace API or PaaS tokens. Those tokens can't be used here.
* `communicationEndpoints` corresponds to one or multiple HTTP addresses that represent Dynatrace Servers or ActiveGates. The `communicationEndpoints` parameter is represented in the script as `DT_CONNECTION_POINT`. For example, the `dynatrace-env.sh` (located in the OneAgent installation root directory) may contain the following:

  ```
  export DT_CONNECTION_POINT="https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication"
  ```

  In this case, the parameter would be

  ```
  server=https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication
  ```

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.


---


## Source: troubleshoot-oneagent-installation-on-solaris.md


---
title: Troubleshooting OneAgent installation on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris
scraped: 2026-02-17T04:52:38.072365
---

# Troubleshooting OneAgent installation on Solaris

# Troubleshooting OneAgent installation on Solaris

* Latest Dynatrace
* 3-min read
* Published Sep 19, 2018

Find out how to solve problems related to installing OneAgent on Solaris.

SSL handshake failed

While downloading, you may encounter the following error:

```
Releasing 0x0000000239ae1890 (new refcount 1).



Initiating SSL handshake.



SSL handshake failed.



Closed fd 5



Unable to establish SSL connection.
```

This can be caused by selecting the wrong SSL or TLS protocol on handshake. As different operating systems act differently (both server and client side), you must specify some protocols manually under certain conditions.

For this specific case, to select the correct protocol, you must specify `--secure-protocol=tlsv1_2` as an additional parameter of the `wget` command. The command should appear as follows:

```
wget --secure-protocol=tlsv1_2



-O Dynatrace-OneAgent-Solaris-xxx-1.xxx.xxx.zip



"https://xxx/xxx/api/v1/deployment/installer/agent/solaris/paas/latest?Api-Token=xxx&arch=x86"
```

It can also be set permanently by creating the file `~/.wgetrc` with the following content:

`secureprotocol = tlsv1_2`

Could not find required opcodes in caller trying to resolve main

You may encounter the following error message when you start your Java application:

```
severe  [hooking   ] Could not find required opcodes in caller trying to resolve main
```

This happens if you use one of the unified monitoring scripts `dynatrace-agentXX.sh` but additionally have OneAgent referenced in `JAVA_OPTS`.

* Ensure that `dynatrace-java-env.sh` isn't called anywhere in your shell when you use the `dynatrace-agentXX.sh` script.
  `dynatrace-java-env.sh` is deprecated and should only be used as a fallback.
* Check for and remove the following parameter from your Java command line or startup scripts (specific directory may vary):

  `-agentpath:/opt/dynatrace/oneagent/agent/lib64/liboneagentloader.so`

Following this, the error message should go away.

LD\_PRELOAD\_64: parameter not set

You may encounter an error like this when you use `dynatrace-agentXX.sh` in a shell script.

```
Info: using DT_HOME: /opt/dynatrace/oneagent



.profile[33] LD_PRELOAD_64: parameter not set
```

This happens if use `set -u` to treat unset variables and parameters as errors. `dynatrace-agentXX.sh` does export variables which, though they may not yet exist in your script, are nevertheless needed and key to proper function. To overcome this, call `set +u` ahead of `dynatrace-agentXX.sh` in your script.

```
# avoid error



set +u



DT_HOME=/opt/dynatrace/oneagent



export DT_HOME



. $DT_HOME/dynatrace-agent64.sh
```

ld.so.1: sudo: warning: /opt/dynatrace/oneagent/agent/lib/liboneagentproc.so: open failed: illegal insecure pathname

You may encounter an error like this when you set `LD_PRELOAD` in your execution environment and call sudo or su. This happens because OneAgent isn't installed in the secure `ld_preload` directory. This error message has no negative impact and can be ignored. To avoid this, ensure that you don't set `LD_PRELOAD` in an execution context where you want to use sudo.

See [Further detail on this topicï»¿](https://docs.oracle.com/cd/E19253-01/816-5165/ld.so.1-1/index.html#Security)

Why doesn't OneAgent start to monitor Apache process after restart?

Following installation of OneAgent, your Apache web server must be *completely* restarted to enable monitoring. To do this correctly, it's important to understand the difference between "partial" and "complete" restarts. In the case of partial restarts, the main Apache process re-reads its configuration files, re-opens its log files, and then restarts its worker processes. OneAgent however, requires a complete Apache web server restart in which all workers andâmost importantlyâthe main Apache process are shut down entirely and then restarted.

See [Stopping and Restarting Apache HTTP Serverï»¿](https://httpd.apache.org/docs/2.4/stopping.html) for more information on the different types of available restarts.

## How to perform a complete restart

You may be accustomed to restarting Apache by issuing an `apachectl restart` command. However, this command only results in a partial Apache restart.

To execute a complete Apache restart and enable deep monitoring with Dynatrace OneAgent, you need to first invoke a complete shutdown using the `apachectl stop` command. Only following this step can you restart the server using `apachectl start` .

It's fine to use `service apache2 restart` on Ubuntu systems. Note however that whatever commands you use, you'll likely need superuser rights (sudo).

I use WebLogic admin server to restart the managed nodes on Solaris. I can't set environment variables.

If you have trouble setting the environment variables

1. Shut down the managed nodes and Node Manager (make sure no process is running under the functional ID).
2. Back up the `$Domain_home/startNodeManagerMx.sh` script.
3. Modify the `startNodeManagerMx.sh` script to add the lines below.  
   (After running `commEnv.sh`, refer to the script under `/apps/wldomains/wls-aabb-1a` on `aaaabbb01a`).

   ```
   DT_HOME="/opt/dynatrace/oneagent"



   export DT_HOME



   source "$DT_HOME/dynatrace-env.sh"



   LD_PRELOAD="$DT_HOME/agent/lib/liboneagentproc.so"



   export LD_PRELOAD
   ```
4. Start a new session.
5. Start Node Manager.
6. Get a PID while Node Manager is working.

   Use the command line `$ pargs -e pid |grep LD` to see if the environment is there.

   Example:

   ```
   aabb@aaaabbb01a:/apps/wldomains/wls-aabb-1a$pargs -e 26531 |grep LD



   envp[27]: envp[28]: LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
   ```
7. Start managed nodes from the console.
8. Check the log directory to make sure a new log is generated:

   ```
   ls -ltr /opt/dynatrace/oneagent/log/java
   ```

For more details on setting up Oracle WebLogic monitoring, see [Configure Oracle WebLogic via startup script](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris#weblogic "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).")


---


## Source: uninstall-oneagent-on-solaris.md


---
title: Uninstall OneAgent on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/uninstall-oneagent-on-solaris
scraped: 2026-02-17T04:52:39.652560
---

# Uninstall OneAgent on Solaris

# Uninstall OneAgent on Solaris

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Nov 13, 2025

To uninstall OneAgent on Solaris, revert any configuration changes that were made when OneAgent was [installed](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).").

* Remove environment variables that are set.
  For example:

  + `DT_HOME`
  + `LD_PRELOAD`
* Restore any application configuration that reference OneAgent.
  For example:

  + `httpd.conf LoadModule`
* Delete any downloaded files.

Although these configuration options are common, your environment may require additional steps based on your configuration during install. For details specific to your setup, refer to the [installation guide](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") and reverse the steps you applied for your applications.

Reinstalling OneAgent

If the configuration files are removed and OneAgent is reinstalled, the host will appear as a new host with a different internal identifier.


---


## Source: update-oneagent-on-solaris.md


---
title: Update OneAgent on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/update-oneagent-on-solaris
scraped: 2026-02-17T04:52:36.389843
---

# Update OneAgent on Solaris

# Update OneAgent on Solaris

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

To update an installed OneAgent instance on Solaris (x86 and SPARC) follow the instructions below:

1. Redo all steps of the [initial installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") but install OneAgent to a new directory.
2. Stop all monitored processes.
3. Rename the current OneAgent installation directory (for example, `/opt/dynatrace/oneagent-old`) using the following command:

   `mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old`.

   This folder can be deleted following OneAgent update.
4. Rename the updated OneAgent folder to point to the original installation directory (for example, `/opt/dynatrace/oneagent`) using the following command:

   `mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent`
5. Restart all processes that are to be monitored.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.


---


## Source: solaris.md


---
title: Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris
scraped: 2026-02-17T04:45:47.218903
---

# Solaris

# Solaris

* Latest Dynatrace
* 1-min read
* Updated on Nov 18, 2025

Dynatrace supports Oracle Solaris (x86 and SPARC) for Java, Apache HTTP server and IBM HTTP server. If your infrastructure is based on these technologies you can use Dynatrace OneAgent to effectively monitor your hosts, services, and user experience. For analytical information about the supported OneAgent capabilities for Solaris, see the [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

### Installation

[Install OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).")

### Operation

[Troubleshoot](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris "Find out how to solve problems related to installing OneAgent on Solaris.")

[Update OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/update-oneagent-on-solaris "Learn how you can update Dynatrace OneAgent on Solaris.")

[Uninstall OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/uninstall-oneagent-on-solaris "Find out how to configure Dynatrace to stop monitoring applications of different technologies that run on Solaris (x86 and SPARC).")


---


## Source: customize-oneagent-installation-on-windows.md


---
title: Customize OneAgent installation on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows
scraped: 2026-02-17T04:54:00.507079
---

# Customize OneAgent installation on Windows

# Customize OneAgent installation on Windows

* Latest Dynatrace
* 9-min read
* Updated on Jan 21, 2026

OneAgent installer for Windows is provided and used as a self-extracting EXE file. The installer can also be extracted and used directlyâas an MSI package. This later approach is mostly used in [Group Policy deployment](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Learn how to download and install Dynatrace OneAgent on Windows.").

You can customize the installation by specifying command-line parameters for selected settings, or you can rely on default settings.
However, note that parameters marked below as `environment-specific`âthat is, parameters that set the communication endpoint, environment ID, and tokenâare:

* mandatory
* pre-configured only for the EXE version of the installer.
  Therefore, when using the installer as and MSI package, you must specify these parameters explicitly.

## Passing installation parameters

### Command line

To pass the parameters, append them to the installer command and separate them with spaces.

For example, for the EXE version of the installer:

```
.\Dynatrace-OneAgent-Windows.exe --set-host-group=my_host_group --set-monitoring-mode=infra-only INSTALL_PATH="C:\installdir"
```

When using the installer as an MSI package, you can directly append only the `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER`, and `SKIP_OS_SUPPORT_CHECK` parameters. This type of installation is usually run in silent mode, as part of [Group Policy deployment](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Learn how to download and install Dynatrace OneAgent on Windows."). The `--set-param=<value>` has to be placed inside of `ADDITIONAL_CONFIGURATION` (`ADDITIONAL_CONFIGURATION="--set-param=<value>"`).  
For more information on command-line syntax, see [Silent installation](#silent-installation).

### Installer UI

You can also add the `--set-param=<value>` parameters in the **Configure OneAgent settings** installation screen.

![OneAgent windows customize](https://dt-cdn.net/images/windows-customize-495-ec2f24e000.png)

Parameters supported by the installer UI

The UI of the OneAgent installer for Windows supports only the `--set-param=<value>` parameters.

The following parameters are NOT supported by the installer UI: `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER`, and `SKIP_OS_SUPPORT_CHECK`.

## Removed installation parameters

Starting with version 1.213, the following parameters are only accepted if specified using the `--set-param=<value>` syntax. For these specific parameters, the equivalent `PARAM=<value>` syntax is no longer supported:

| Removed `PARAM=<value>` parameter | New `--set-param=<value>` parameter |
| --- | --- |
| `SERVER` | `--set-server` |
| `TENANT` | `--set-tenant` |
| `TENANT_TOKEN` | `--set-tenant-token` |
| `PROXY` | `--set-proxy` |
| `HOST_GROUP` | `--set-host-group` |
| `APP_LOG_CONTENT_ACCESS` | `--set-app-log-content-access` |

## MSI installation parameters

`INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER` and `USER` are a special kind of parameter adhering to [MSI public property syntaxï»¿](https://docs.microsoft.com/en-us/windows/win32/msi/public-properties). They won't be replaced by equivalent `--set-param=<value>` parameters. You can use them only on the installer command line, not in the installer UI.

## Installation path

**Default value**: `%PROGRAMFILES%\dynatrace\oneagent`

The **`INSTALL_PATH`** parameter allows OneAgent installation to a directory of your choice.

For example:  
`.\Dynatrace-OneAgent-Windows.exe INSTALL_PATH="C:\test dir"`

This parameter is not supported by the installer UI.

The `INSTALL_PATH` parameter doesn't control the OneAgent [log and configuration files](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.") directories. To customize the log path, use the `LOG_PATH` parameter.

### Custom directory requirements

Make sure that your custom installation path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be a child directory of `%PROGRAMDATA%\dynatrace`.

## Log path

**Default value**: `%PROGRAMDATA%\dynatrace\oneagent\log`

The **`LOG_PATH`** parameter allows you to customize your OneAgent log directory.

For example:

`.\Dynatrace-OneAgent-Windows.exe LOG_PATH=C:\dynatrace\logs`

This parameter is not supported by the installer UI.

### Custom directory requirements

Make sure that your custom log path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be a child directory of `%PROGRAMDATA%\dynatrace`.

### Changing location

If you use the parameter to change the location for an already installed OneAgent:

* Existing files are not migrated to the new location

* After you set or change the `LOG_PATH` parameter, you must restart deep-monitored processes so that OneAgents monitoring them can pick up the new path to store logs. You will be notified to restart a corresponding process on the **Process overview** page.

## Data storage

OneAgent version 1.199

**Default value**: `%PROGRAMDATA%\dynatrace\oneagent\datastorage`

The **`DATA_STORAGE`** parameter allows you to define a directory dedicated to storing large runtime data produced by OneAgent in full-stack monitoring mode, such as crash reports or memory dumps.

For example:

`.\Dynatrace-OneAgent-Windows.exe DATA_STORAGE=D:\data\dynatrace\runtime`

This parameter is not supported by the installer UI.

### Custom directory requirements

Make sure that your custom data storage path meets the following requirements:

* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.
* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.
* The value must be an absolute path and must not point to the root volume directory.

* The value must not be a child directory of `%PROGRAMDATA%\dynatrace`.

### Changing location

If you use the parameter to change the location for an already installed OneAgent:

* Existing files are not migrated to the new location

* After you set or change the `DATA_STORAGE` parameter, you must restart deep-monitored processes, so that OneAgents monitoring them can pick up the new path to store runtime data. Otherwise, memory dumps and other runtime data won't be saved. You will be notified to restart a corresponding process on the **Process overview** page.

## Communication endpoint

**Default value**: `environment specific`

The address of the OneAgent communication endpoint, which is a Dynatrace component that OneAgent sends data to. Depending on your deployment, it can be a Dynatrace Cluster or ActiveGate. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value. To change it, use the IP address or a name. Add the port number following a colon.

To set the communication endpoint, pass it as a parameter value:

```
--set-server=https://100.20.10.1:443
```

OneAgent and Dynatrace Cluster automatically maintain a working connection. If an endpoint detail changes, the cluster notifies OneAgent of the change and OneAgent automatically updates the endpoint you set using the `--set-server` to the new working value.

To change the endpoint after installation, use `--set-server` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Environment ID

**Default value**: `environment specific`

The Dynatrace [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") you received with your activation email. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value. If you're selling Dynatrace-based services, use this option to set your customers' IDs from the pool of IDs you purchased from Dynatrace.

To set the environment ID, pass it as a parameter value:

```
--set-tenant=mySampleEnv
```

To change the tenant after installation, use `--set-tenant` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Token

**Default value**: `environment specific`

The tenant token that is used for authentication when OneAgent connects to the communication endpoint to send data. If you install OneAgent using the Dynatrace **Deploy** page, this is already set to the correct value.

To set a token, pass it as a parameter value:

```
--set-tenant-token=abcdefghij123456
```

See [Access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") to learn how to obtain a token.

To change the tenant token after installation, use `--set-tenant-token` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Network zones

**Default value**: `unset`

To learn about network zone naming rules and other reference information, see [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

Use the `--set-network-zone` parameter to instruct OneAgent to communicate via the specified network zone:

```
--set-network-zone=your.network.zone
```

To change or clear the network zone assignment after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify network zone** action).

Alternatively, you can use `--set-network-zone` on the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Proxy

**Default value**: `unset`

The address of the proxy server. Use the IP address or a name, and add the port number following a colon. For an authenticating proxy you can specify a username and password like this `username:password@172.1.1.128:8080` where both username and password need to be URL encoded.

To set a proxy, pass it as a parameter value:

```
--set-proxy=172.1.1.128:8080
```

Dynatrace also supports IPv6 addresses.

To change or clear the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Port range

Deprecated

Starting with OneAgent version 1.301, OneAgent doesn't use the TCP ports for its own inter-process communication. In case OneAgent occupies your applications' ports, upgrade OneAgent to version 1.301+.

**Default value**: `50000:50100`

Watchdog is a binary used for starting and monitoring OneAgent monitoring processes:

* `oneagentos`âoperating system monitoring
* `oneagentplugin`âmonitoring using [OneAgent extensions](/docs/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`âmonitoring using local [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`â[Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`â[network monitoring](/docs/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Use the `--set-watchdog-portrange=<arg>` parameter to change the watchdog listening port range to `<arg>`. The `<arg>` must contain two port numbers separated by a colon (`:`). For example `50000:50100`. The maximum supported port range is from 1024 to 65535. The port range must cover at least 4 ports. The port number starting the range must be lower. For example:

```
--set-watchdog-portrange=50000:50100
```

To change port range after installation, use `--set-watchdog-portrange` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#portrange "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Auto-update

Use the `--set-auto-update-enabled=<arg>` to enable or disable OneAgent auto-update. For example:

```
--set-auto-update-enabled=true
```

After you set the parameter to `false`, you won't be able to control OneAgent automatic updates using the Dynatrace web UI at **Settings** > **Updates** > **OneAgent updates**.

## Host group

**Default value**: `unset`

The name of a group you want to assign the host to. For details, see [Organize your environment using host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Host group string requirements:

* Can contain only alphanumeric characters, hyphens, underscores, and periods
* Must not start with `dt.`
* Maximum length is 100 characters

To assign a host to the host group, pass the host group name as a parameter value:

```
--set-host-group=My.HostGroup_123-456
```

To remove the host from a group, you need to [uninstall OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.") or pass an empty value `--set-host-group=""` when running a OneAgent update. You can't remove the host from a group using the `HOST_GROUP` parameter when updating OneAgent.

To change or clear the host group assignment after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host group** action).

Alternatively, you can use `--set-host-group` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Monitoring mode

**Default value**: `fullstack`

Activates one of the OneAgent monitoring modes:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

To enable a specific monitoring mode, set the `--set-monitoring-mode` parameter to one of the following values:

* `fullstack`
* `infra-only`
* `discovery`

For example:

```
--set-monitoring-mode=infra-only
```

To change the monitoring mode after installation, use `--set-monitoring-mode` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#infrastructure-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") or set it using the [Host settings](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") page.

## Custom host name

**Default value**: `unset`

Use the `--set-host-name` to override an automatically detected host name. The host name value must not contain the `<`, `>`, `&`, `CR` (carriage return), and `LF` (line feed) characters and the maximum length is 256 characters.

This command adds a custom host name to display in the UI, but the detected host name is not changed. For details, see [Set custom host names](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

To set the host name:

```
--set-host-name=myhostname
```

To change the host name after installation, use `--set-host-name` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Custom host metadata

**Default value**: `unset`

Once configured, custom metadata is displayed as a set of properties at the bottom of the **Properties and tags** section of the host overview page. The property values must not contain the `=` (except key-value delimiter) and whitespace characters. The maximum length is 256 characters including the key-value delimiter.

To add or change host properties:

```
--set-host-property=AppName --set-host-property=Environment=Dev
```

You can add or change more than one property in the same command.

To change the host metadata after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select **modify host properties** action).

Alternatively, you can use `--set-host-property` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Custom host tags

**Default value**: `unset`

Once configured, the tags are displayed at the top of the **Properties and tags** section of the host overview page. The property values must not contain the `=` (except key-value delimiter) and whitespace characters. The maximum length is 256 characters including the key-value delimiter.

To add or change host tags:

```
--set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk
```

You can add or change more than one tag in the same command. It is allowed to define tags with the same key but different values.

To change the host tags after installation, use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host tags** action).

Alternatively, you can use `--set-host-tag` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Host ID source

**Default value**: `auto`

Available on all supported platforms for OneAgent version 1.223+. For OneAgent version 1.221 and earlier, this feature is supported only for Citrix Virtual Apps and Desktops.

It's particularly important to keep your host ID static in dynamic virtual environments where hosts are recreated on a daily basis.

To **define the source for host ID generation**, use `--set-host-id-source` and set it to one of the predefined values:

* `auto` â Let Dynatrace generate the host ID automatically
* `ip-addresses` â Generate host ID based on the host IP address
* `mac-addresses` â Generate host ID based on the host's NIC MAC address
* `fqdn` â Generate host ID based on the host fully qualified domain name (FQDN) in the `host.domain` format. If the FQDN doesn't contain a dot character, the NIC MAC address is used instead.
* If you monitor multiple environments, you can split the hosts with identical IPs, MAC addresses, or FQDNs using a different namespace for each environment. The namespace can contain only alphanumeric characters, hyphens, underscores, and periods; the maximum length is 256 characters:

* `ip-addresses;namespace=<namespace>`
* `mac-addresses;namespace=<namespace>`
* `fqdn;namespace=<namespace>`

For example, to set the host ID source to `ip-addresses` and assign it to a namespace called `test`, run the OneAgent installer with the following parameter:

```
--set-host-id-source="ip-addresses;namespace=test"
```

To install OneAgent on a Citrix host, set the host ID source to `FQDN`:

```
--set-host-id-source="fqdn;namespace=test"
```

## Access to system logs

OneAgent can download system logs for the purpose of diagnosing issues that may be caused by conditions in your environment. OneAgent doesn't currently download any Windows system logs, but this can change in future releases.

`--set-system-logs-access-enabled=false` disables access to logs  
`--set-system-logs-access-enabled=true` enables access to logs

If you need to change this access after installation, use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."):

Note that this is a self-diagnostics setting that is not related to [Log Monitoring](#log-monitoring).

## Log Monitoring

**Default value**: `true`

When set to `true`, allows OneAgent to access log files for the purpose of Log Monitoring. Accepted values are (`true`, `false`) or (`1`, `0`). This option can alternatively be [enabled/disabled through the Web UI](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

For example:
`--set-app-log-content-access=true`

If you need to enable or disable Log Monitoring after installation, use `-set-app-log-content-access` in [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Automatic injection

Do not set this parameter to `true` during the installation process.

**Default value**: `true`

You can set the `--set-auto-injection-enabled=<arg>` parameter to `true` or `false` to disable or enable OneAgent auto-injection.

For more information, see [Automatic injection](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Local metric ingestion

**Default value**: `14449`

You can use the `--set-extensions-ingest-port=<arg>` parameter to change the default communication port used for local metric ingestion. The port is used by [OneAgent REST API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), [Scripting integration](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") (`dynatrace_ingest`), and [Telegraf](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace.").

For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## StatsD metric ingest

**Default value**: `18125`

You can use the `--set-extensions-statsd-port=<arg>` parameter to change the default [DynatraceStatsD](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.") UDP listening port.

For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## OneAgent extension user

The **Default value**: `LocalSystem` (OneAgent version 1.195+)

Use the **`USER`** parameter to define the user running the process responsible for [Dynatrace extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") functionality. For example:

`.\Dynatrace-OneAgent-Windows.exe USER=LocalService`

This parameter is not supported by the installer UI.

If you don't add the `USER` parameter:

* For fresh OneAgent 1.195+ installations, the default `LocalSystem` account will be used to run OneAgent extensions, but Python extensions will be spawned as `LocalService`.
* For fresh OneAgent deployments prior to version 1.195, OneAgent will use the `dtuser` account.
* Updating the OneAgent preserves the previously configured user account. To change it, you must reinstall OneAgent setting the `USER` parameter to a new value.

The `USER` parameter can have one of the following values:

* Recommended `LocalSystem` is the default user account used to run OneAgent extensions starting with OneAgent version 1.195. Applied automatically when the `USER` parameter isn't used. This parameter value makes OneAgent use the `NT AUTHORITY\SYSTEM` privileged system account to run OneAgent extensions. Effectively, no local user account is created. As a result, all OneAgent modules, including all extensions except Python extensions, are fully functional. Python extensions will run as `LocalService`.
* `LocalService`: This parameter makes OneAgent use the `NT AUTHORITY\LOCAL SERVICE` system account to run OneAgent extensions. While this reduced set of privileges is enough for most of the extensions to operate, there are some that won't be able to produce data effectively (namely, extensions that collect Performance Monitor counters, such as MS SQL or .NET extensions). If you're unsure about which extensions you might use, it's best to use the `LocalSystem` parameter value instead.
* Deprecated `no_create` disabled user creation when installing OneAgent prior to OneAgent version 1.209. Starting with the version 1.209, when you use the `no_create` parameter, the OneAgent installer applies the `LocalSystem` parameter without any warning. The `no_create` setting is not converted to `LocalSystem` for existing installations when running an update. To convert, you must reinstall OneAgent setting the `USER` parameter to a new value.
* Deprecated `dtuser` was the default user account used to run OneAgent extensions prior to OneAgent version 1.195. It made the installer create a local user account with the same name in the system. Starting with the version 1.209, when you use the `dtuser` parameter, the OneAgent installer applies the `LocalSystem` parameter without any warning. Starting with OneAgent version 1.239, the `dtuser` setting is converted to `LocalSystem` for existing installations when running an update.

When deploying Dynatrace on Windows Server Domain Controller, make sure the `USER` parameter is set to `LocalSystem`, or alternatively `LocalService`, to avoid propagation of `dtuser` across the domain, which can cause interference with existing `dtuser` accounts on hosts that have Dynatrace installed.

## Silent installation

When using the silent installation mode, the OneAgent installer should be pre-configured with appropriate parameter values, since interactive dialogs and prompts will not be displayed during installation.

The environment specific parameters are preconfigured only for the EXE version of the installer. When using the installer in the form of an MSI package, you must specify all of these parameters yourself.

### MSI packageâsilent installation

To set up silent command-line installation when using an MSI package, add `/quiet /qn` as in these examples:

#### Command shell

```
msiexec /i C:\some\path\Dynatrace-OneAgent-Windows.msi ADDITIONAL_CONFIGURATION="--set-server=https://someserver.com --set-tenant=xxx --set-tenant-token=xxx --set-host-group=myGroup" /quiet /qn
```

#### PowerShell 3.0+

```
msiexec /i C:\some\path\Dynatrace-OneAgent-Windows.msi --% ADDITIONAL_CONFIGURATION="--set-server=https://someserver.com --set-tenant=xxx --set-tenant-token=xxx --set-host-group=myGroup" /quiet /qn
```

Note the `--%` stop-parsing symbol used in the PowerShell command.

### EXE installerâsilent installation

To set up silent command-line installation for an EXE version of the installer, add `--quiet` as in this example:

```
.\Dynatrace-OneAgent-Windows.exe --set-host-group="myGroup" --quiet
```

## Packet capture driver (pcap)

OneAgent version 1.229+

The `PCAP_DRIVER` parameter allows you to specify which packet capture driver will be installed and used for network metrics collection.

Example:

```
.\Dynatrace-OneAgent-Windows.exe PCAP_DRIVER=npcap
```

**Default value**: `npcap`

**Possible values:**

Value

Description

`npcap`

`PCAP_DRIVER=npcap` installs the `Npcap` driver.

This option uninstalls any installation of WinPcap or outdated Npcap previously installed by OneAgent. If you installed WinPcap or Npcap manually, however, you'll need to uninstall it yourself.

`winpcap`

`PCAP_DRIVER=winpcap` installs the `WinPcap` driver.

This option does **NOT** uninstall or overlay any existing installation of `Npcap` or `WinPcap`.

`auto`

Deprecated with OneAgent version 1.255+

`PCAP_DRIVER=auto` automatically determines which driver to install. This option does **NOT** uninstall or overlay any existing installation of `Npcap` or `WinPcap`. During installation, if no packet capture driver is found, `Npcap` is installed by default.

`disabled`

Available with OneAgent version 1.249+

`PCAP_DRIVER=disabled` disables the installation of any packet capture driver and disables the OneAgent network monitoring module. If any packet capture driver is already installed on the host, you'll need to uninstall manually.

* This parameter is not supported by the installer web UI.
* The value of this parameter persists through updates.
* If you install `Npcap` during OneAgent installation, the installer creates a scheduled task called `npcapwatchdog`.

  + This task ensures that the `Npcap` driver functions correctly after Windows feature updates. The task runs in the background and has no effect on the performance or functionality of the system.
  + While the `npcapwatchdog` task is meant to prevent issues with Windows updates, you can remove it. However, if removed, the Npcap driver may need to be reinstalled before it can be used again.

For more information, see

* [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows#installation "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")
* [Install OneAgent on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#winpcapuninstall "Learn how to download and install Dynatrace OneAgent on Windows.")

## Skipping operating system support check

Setting this parameter to `true` will enable OneAgent installation on an otherwise unsupported platform. Dynatrace does not take responsibility for such installations.

This parameter is not supported by the installer UI.

This parameter is not preserved across automatic updates.

For information about the OneAgent auto-update mechanism, see [Update Dynatrace OneAgent on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.").

**Default value**: `false`

The **`SKIP_OS_SUPPORT_CHECK`** parameter allows you to force OneAgent installation on an otherwise unsupported platform.

For example:
`.\Dynatrace-OneAgent-Windows.exe SKIP_OS_SUPPORT_CHECK=true`

For supported platforms, see [Technology support](/docs/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.").


---


## Source: disk-space-requirements-for-oneagent-installation-and-update-on-windows.md


---
title: OneAgent files and disk space requirements on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows
scraped: 2026-02-17T04:53:53.827193
---

# OneAgent files and disk space requirements on Windows

# OneAgent files and disk space requirements on Windows

* Latest Dynatrace
* 4-min read
* Updated on Jun 25, 2025

This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.

## Full-stack and Infrastructure Monitoring mode

The same disk space requirements apply to both Full-stack and Infrastructure monitoring modes.

## OneAgent directories and their sizes

|  |  | Default directory | Can be modified? |
| --- | --- | --- | --- |
| Size of installation (with temporary installation files removed) | ~775 MB | `%PROGRAMFILES%\dynatrace\oneagent` | Yes [1](#fn-1-1-def) |
| Persistent configuration | ~10 MB | `%PROGRAMDATA%\dynatrace\oneagent\agent\config` | No |
| Temporary files, runtime configuration | 200 MB | `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime` | No |
| Logs | 1 GB | `%PROGRAMDATA%\dynatrace\oneagent\log` | Yes [2](#fn-1-2-def) |
| Crash reports, memory dumps | 3 GB | `%PROGRAMDATA%\dynatrace\oneagent\datastorage` | Yes [3](#fn-1-3-def) |
| Log analytics persistence | ~1 GB [4](#fn-1-4-def) | `%PROGRAMDATA%\dynatrace\oneagent\datastorage\loganalytics` | Yes [3](#fn-1-3-def) |
| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime\extensions\persistence` | Yes [5](#fn-1-5-def) [6](#fn-1-6-def) |
| Additional space required for updates | ~3.4 GB | See [Space required for installation and updates](#updates) |  |
| **Total** | **~11.5 GB** |  |  |

1

Use the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.") installation parameter.

2

Use the [LOG\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#log-path "Learn how to use the OneAgent installer for Windows.") installation parameter.

3

Use the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.") installation parameter.

4

The size depends on the number of ingested logs.

5

Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/docs/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.

6

The reliability mechanism does not work if the requirement is not met. For more information, see [Persistence details](#persistence).

For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").

## OneAgent files aging mechanism

OneAgent in full-stack monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").

## Space required for updates

When calculating the space required for updates, we take into account the compressed EXE installer file size, the extracted MSI package, and the size of the installation process (the space required to deploy OneAgent files).

|  | Size | Description | Removed after | Claimed by | Path |
| --- | --- | --- | --- | --- | --- |
| 1 | ~130 MB | EXE installer downloaded by AutoUpdate | OneAgent restart or next version installed [1](#fn-2-1-def) | AutoUpdate | `%PROGRAMDATA%\dynatrace\oneagent` |
| 2 | ~750 MB | Extracted MSI installer | End of the installation | OneAgent Installation | `%PROGRAMDATA%\dynatrace\oneagent` |
| 3 | ~750 MB | Extra storage for temporary installation files | End of the installation | OneAgent Installation | `%APPDATA%` |
| 4 | ~750 MB | Copy of the MSI installer saved by Windows | Next version installed | Windows installer | `%WINDIR%\Installer` |
| 5 | ~750 MB | Installed files | Next version installed | OneAgent Installation | `[Installation path]` |
| Î£ | ~3130 MB |  |  |  |  |

1

If you download the EXE installer manually, the installation process won't remove it.

Additional space required for installation and updates is calculated using the 10% safety margin:

`(size of the installation process [2+3+4+5] + installer files size [1]) * 1.1`

Required disk space for OneAgent installation and update on a single drive is ~3.4 GB calculated using this formula.

Note that the EXE installer is compressed, which explains the difference in size in comparison to the MSI installer.

In terms of space requirements, there's no real difference between manual installation of the new version (when an older version is already installed), automatic update, and updates that are triggered by restarting the OneAgent container. In all these cases, the installation process is performed exactly the same way. What differs is the method through which the update is triggered.

## Persistence details

The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.

### General information

* Persistent storage of data requires 2136 MB of free disk space:

  + 600 MB of free disk space to be used by the reliability mechanism
  + 1.5 GB of free disk space to be used as a buffer
* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.
* The volume is used proportionally to the load of logs ingest.
* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).

### Configuration

Windows configuration file: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

**Variable**

**Description**

`persistence.reliable_mode`

`true` - reliable mode turned on; SFM logs genereted if space requirement not met
`false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism

`persistence.total_limit_kb`

Maximum volume limit for Extensions Log Persistence in kilobytes.
By default: 600 MB
Can be modified manually if the requirement can't be met on the host.


---


## Source: how-to-pass-a-proxy-address-during-oneagent-installation-on-windows.md


---
title: How to pass a proxy address during OneAgent installation on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows
scraped: 2026-02-17T04:53:52.168300
---

# How to pass a proxy address during OneAgent installation on Windows

# How to pass a proxy address during OneAgent installation on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

The Windows installer allows you to enter a proxy address during installation, so in the majority of cases you don't need to worry about adding extra command line parameters. Command line parameters are particularly useful when you're deploying a [Group Policy installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.") or other automated task.

The OneAgent installer recognizes the `--set-proxy` parameter. The value of the parameter is the proxy server address. Add the port number following a colon (for example, `172.1.1.128:8080`). For an authenticating proxy, you can specify the username and password like this `username:password@172.1.1.128:8080`, where both username and password need to be URL encoded. Dynatrace also supports IPv6 addresses.

Parameter names are case-sensitive, so use `ALL CAPS` for parameter names.

## Passing a proxy address to the installer

Let's say you've downloaded your OneAgent installer to the `C:\Users\Admin\Downloads` folder and your proxy IP address is `10.1.1.5`. In such a scenario you would begin the installation like this:

```
C:\Users\Admin\Downloads>Dynatrace-OneAgent-Windows-1.171.0.exe  --set-proxy=10.1.1.5
```

## Change proxy after installation

If you need to change the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").


---


## Source: install-oneagent-on-windows.md


---
title: Install OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows
scraped: 2026-02-17T04:53:58.725381
---

# Install OneAgent on Windows

# Install OneAgent on Windows

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Jan 22, 2026

This page describes how to download and install Dynatrace OneAgent on Windows.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements and prerequisites

* You need [administrator rights](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system") for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).
* You need permissions and credentials for restarting all your application services.
* You need to check also the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.").
* The host on which you install OneAgent needs at least 200 MB RAM.
* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").
* For OneAgent version 1.253 and earlier, we recommend that you [uninstall any existing `WinPcap` driver](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#uninstall-winpcap-driver-to-allow-npcap-installation "Learn how to download and install Dynatrace OneAgent on Windows.") to allow `Npcap` installationâdo this on all Windows versions, except for `Windows Server 2019 build 1809 without hotfix KB5066187`.
  For OneAgent version 1.255+, `Npcap` is installed by default and may cause a network disruption on `Windows Server 2016`, `Windows Server 2019 build 1809`, and `Windows Server 2019 build 1809 without hotfix KB5066187`. To prevent it, upgrade your hosts with the hotfix [KB5066187ï»¿](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5066187) or use [other documented options](/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring#potential-network-disruption-during-oneagent-installation-on-windows "Learn more about troubleshooting network monitoring.").

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Uninstall WinPcap driver to allow Npcap installation

If you have the `WinPcap` driver installed, we recommend that you remove it prior to OneAgent installation and let the OneAgent installer install the appropriate packet capture driver as packaged with the OneAgent installer: `Npcap` is the recommended packet capture driver for OneAgent.

`Npcap` is the successor to `WinPcap` and is best suited for Dynatrace network analysis. The `Npcap` driver provided with the OneAgent installer is packaged in such a way that its DLL library files are seamlessly integrated with Dynatrace software, enabling unattended updates.

For more information, see:

* [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")
* [Customize OneAgent installation on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.")

During the upgrade from `WinPcap` to `Npcap`, you might encounter network disruptions that can be mitigated by upgrading your Windows Server version and/or disabling `Microsoft Network Monitor Driver`. For more details, see [Potential network disruptions during OneAgent installation on Windows](/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring#disruptionnetwork "Learn more about troubleshooting network monitoring.")

## Re-installation or repair of installation

OneAgent installer for Windows doesn't support the `modify` and `repair` operations. You can't reinstall OneAgent using the same installer version as was used to install the currently installed OneAgent. To reinstall OneAgent, uninstall it first or simply install a newer version.

## Installation

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Windows**.
3. Paste a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you'll use later.
4. Download the installer. There are two options:

   * Select **Download OneAgent installer** to download the installer for Windows (EXE file) for single-server installation.
   * Download via Windows Command Prompt. Copy and run the `powershell` command. It is generated automatically when you provide the PaaS token.

     This command will only work with PowerShell 3.0 and TLS 1.2 (or later).

   Get MSI package

   If you want to use Group Policy to automatically distribute OneAgent to your Windows hosts, you'll need the MSI package along with the batch file. To get the MSI package:

   1. Download the OneAgent installer provided as an EXE file.
   2. Run it with the `--unpack-msi` parameter. This extracts the MSI package and the installation batch file. Optionally, you can specify an existing path. If you skip the path, the files are saved to a working directory. For example:

   ```
   C:\Downloads\Dynatrace-OneAgent-Windows.exe --unpack-msi "C:\installers"
   ```

   When using the `--unpack-msi` parameter, no other [installation parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.") are allowed. Add the `--quiet` parameter to run the MSI package extraction in quiet mode. Use the `--help` parameter to display a pop-up window with a list of available parameters.

   Copy and paste the MSI package and the batch file when configuring Group Policy for Dynatrace installation. The default installation should work in most cases, but if you need to customize it, you can modify the [installation parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows."). Then, you have to create a distribution point, assign a package (the OneAgent MSI package with parameters), specify a command to install the MSI package as [silent installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#silent-installation "Learn how to use the OneAgent installer for Windows."), and publish your policy.
5. Optional **Set customized options**  
   At this point, the Dynatrace UI allows you to customize your OneAgent installation: You can specify a number of customizations interactively on-screen. Based on your entries, an installation command will be generated and displayed, for use in the next step of installation (see below).  
   You can:

   * Set a [network zone](/docs/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.
   * Organize your hosts into [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."), if your environment is segmented (for example, into development and production).
   * Override automatically detected [host name](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.
   * Apply [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the host to organize your monitored environments in a meaningful way.
   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * Disable [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

   **If further customizations are required, you can specify [additional options on the command line](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.").**
6. If you have not specified any custom options, simply run the executable file and follow the instructions as displayed.
   If you have specified custom options above, use the generated command, and run it from the download directory. The command will contain all the installation parameters reflecting the custom settings you have specified.
7. Restart all processes that you want to monitor. Youâll be prompted with a list of the processes that need to be restarted. Note that you can restart your processes at any time, even during your organizationâs next planned maintenance period. Though until all processes have been restarted, youâll only see a limited set of metrics, for example CPU or memory consumption.

What happens during installation?

OneAgent is a set of specialized services that have been configured specifically for your monitoring environment. The role of these services is to monitor various aspects of your hosts, including hardware, operating system, and application processes.

During the installation process, the installer:

* Installs executable code and libraries that are used by OneAgent.
* Creates entries in the Windows Registry that start OneAgent as a `SYSTEM` service. Additionally, the `oneagentmon` device and (optionally) `Npcap` or `WinPcap` are installed to allow better integration with the operating system and to facilitate the capture of network statistics.
* Checks the systemâs global proxy settings.
* Checks for a connection to Dynatrace Server or ActiveGate (if you installed ActiveGate and downloaded the OneAgent installer after ActiveGate was connected to Dynatrace).
* OneAgent version 1.193 and earlier Creates its own user (`dtuser`) to run OneAgent extensions. This user is a member of the **Performance Monitoring Users** group, and can only log in as a service. The password is randomly generated during installation and stored encrypted. You can't change the password. For security purposes, the `dtuser` is not allowed to:

  + Access computer from the network.
  + Log in as a batch job.
  + Log in locally.
  + Log in through Remote Desktop Services.  
    The `dtuser` is required for Dynatrace to operate properly, therefore you must not delete it. If, for some reason, the `dtuser` was deleted, next update will recreate it.
* OneAgent version 1.195+ For fresh OneAgent 1.195+ installations, the default `LocalSystem account` is used to run OneAgent extensions.
  For a summarized view of the changes made to your system by OneAgent installation, see [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.


---


## Source: oneagent-security-windows.md


---
title: OneAgent security on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows
scraped: 2026-02-17T04:53:50.612602
---

# OneAgent security on Windows

# OneAgent security on Windows

* Latest Dynatrace
* 5-min read
* Published Nov 12, 2020

To fully automate the monitoring of your operating systems, processes, and network interfaces, Dynatrace requires privileged access to your operating system during both installation and operation.

OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Permissions

OneAgent requires admin privileges on Windows, for both installation and operation.

### Installation

OneAgent installer requires admin privileges to:

* Create the OneAgent service.
* Modify certain registry keys.
* Install packet capture driver (Npcap or WinPcap) for network metrics collection. For more information, see [Packet capture driver (pcap)](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").
* Install [oneagentmon device](/docs/discover-dynatrace/get-started/glossary#o "Get acquainted with Dynatrace terminology.").

### Operation

OneAgent requires admin privileges to:

* List all processes.
* Get memory statistics for all processes.
* Read each process command line and environment.
* View the descriptions of executable files.
* Read application configuration for Apache and IIS
* View the list of libraries loaded for each process.
* Read Windows registry keys.
* Read .NET application domain for .NET 2.0, 3.0, and 3.5.
* Start monitoring network traffic.
* Parse executables for Go Discovery.
* Gather monitoring data related to Docker containers.

## Operating system changes

OneAgent performs the following changes to your system:

### Installation

OneAgent installer modifies the following aspects of your system:

* Starting with version 1.195, no user account is created to run OneAgent extensions. Instead, the `NT AUTHORITY\SYSTEM` privileged system account is used. For more information, see [OneAgent extension user](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#oneagent-extension-user "Learn how to use the OneAgent installer for Windows.").
* The `Dynatrace OneAgent` service is created.
* The Dynatrace OneAgent program is registered with Windows Installer.
* `oneagentmon` driver is installed and `OneAgentMon` device is created. It's required to enable automatic injection into processes.
* Registry sub-trees are created:

  + `HKEY_LOCAL_MACHINE\SOFTWARE\Dynatrace\OneAgent`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\oneagentmon`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Dynatrace OneAgent`
  + `HKEY_LOCAL_MACHINE\SOFTWARE\Caphyon\Advanced Installer`
* [Troubleshooting: Network Agent initialization failure on Windowsï»¿](https://dt-url.net/7c438ee)
* The `Npcap` driver is installed with the `/admin_only` flag set, which restricts Npcap's packet reading and writing to users with Administrator privileges only. Unprivileged users can't access Npcap's functionality on a monitored host. Note that WinPcap doesn't offer this restriction. For more information, see [Customize OneAgent installation on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").

  Make sure these Npcap and WinPcap operations are permitted in your system's security settings:

  + **Npcap:** Writing registry values to `SYSTEM\CurrentControlSet\Services\npcap`
  + **Npcap:** Reading and writing registry values to `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\NpcapInst`
  + **Winpcap:** Reading and writing registry values to `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst` and `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst`
  + **Npcap and Winpcap:** Loading `wpcap.dll` and `packet.dll` located in `C:\WINDOWS\system32\Npcap` / `C:\WINDOWS\system32\WinPcap`
  + **Npcap and Winpcap:** Reading registry values regarding present network interfaces in [`SYSTEM\CurrentControlSet\Control\Network\{Network-Service-GUID}`ï»¿](https://dt-url.net/lz036sy)\*

## Files added

### Installation

OneAgents installer adds the following files to your system:

* OneAgent binaries and configuration files are saved in `%PROGRAMFILES%\dynatrace\oneagent`. Note that you can change the location using the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.") parameter.
* Installer temporary files are saved in `C:\AI_RecycleBin`. The folder is deleted after the installation is complete.

### Operation

* OneAgent temporary files and runtime configuration are saved in `%PROGRAMDATA%\dynatrace\oneagent\runtime`.
* OneAgent persistent configuration is saved in `%PROGRAMDATA%\dynatrace\oneagent\config`.
* Large runtime data, such as memory dumps, is saved in `%PROGRAMDATA%\dynatrace\oneagent\datastorage`. Note that you can change the location of large runtime data using the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.") parameter.

## System logs downloaded by OneAgent

OneAgent downloads Security, System, and Application system logs from the last 14 days so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or automatic updates.

Revoking access to system logs

To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.  
For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Globally writable directories

The [OneAgent directory structure](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.") contains globally writable directories (directories where the `Everyone` user group can write, modify, or execute). Changing these permissions by users is not supported.

### OneAgent injection mechanism

Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.

Similarly, certain log files require global write permissions to allow applications running under various users to write to them.

### System security

We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.

* We keep the number of globally writable directories as limited as possible.
* We leverage advanced file permissions and use the `Creator Owner` permission to limits access to files.

## Installer signing

The OneAgent installer is signed against one or more [DigiCert root certificatesï»¿](https://www.digicert.com/kb/digicert-root-certificates.htm). For regularly maintained systems, Windows verifies that the OneAgent installer has been published by a verified publisher.

If your Windows-based system has been offline since March 2021 or longer, Windows won't be able to verify the installer and the OneAgent installer publisher will appear as **Unknown publisher** when you attempt an installation or update. In such a case, you need to download the latest certificate from [DigiCert root certificatesï»¿](https://www.digicert.com/kb/digicert-root-certificates.htm) and add it to your system. Among all the DigiCert certificates, the `DigiCert Global Root G3` is mandatory for successful verification of the OneAgent installer.

* See [How to: View certificates with the MMC snap-inï»¿](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in) in Microsoft docs to learn which root certificates are installed in your system.
* Download the latest root certificates from [DigiCert root certificatesï»¿](https://www.digicert.com/kb/digicert-root-certificates.htm).

### Windows 2008 R2

Starting with OneAgent version 1.225, the installer is signed using the SHA-2 algorithm. Consequently, Windows 2008 R2 hosts are required to have SHA-2 code signing support installed. If you use Windows Update, the updates were offered to you automatically (KB4474419 and KB4490628). If, however, your Windows 2008 R2 system doesn't support verifying SHA-2 signed installers, OneAgent auto-update and installation won't work if `Applocker` is configured to block unknown publishers and/or security warnings may be displayed. For more information, see the Microsoft [2019 SHA-2 Code Signing Support requirement for Windows and WSUSï»¿](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f) announcement.


---


## Source: stop-restart-oneagent-on-windows.md


---
title: Stop/restart OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows
scraped: 2026-02-17T04:53:55.448996
---

# Stop/restart OneAgent on Windows

# Stop/restart OneAgent on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:

1. Go to **Settings > Monitoring overview**.
2. Click the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.
3. Slide the **Monitoring** switch to the **Off** position.
4. Restart all processes for which monitoring has been disabled.

## Restart using OneAgent command-line interface

When you use the `set` parameters, you need to restart OneAgent service to apply changes. You can use the `--restart-service` parameter with the command that triggers the restart automatically. In some cases you'll also need to restart monitored applications. You can also use the restart parameter on its own, without other parameters. See an example command below.

```
.\oneagentctl.exe --set-proxy=my-proxy.com --restart-service
```

For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Stop OneAgent using the command line

If you use configuration management tools like Puppet or Ansible, you can stop the OneAgent service using the `net stop "Dynatrace OneAgent"` command, where `Dynatrace OneAgent` is the service name for OneAgent.

You can't stop the OneAgent service using the command line if that service is a part of another process, such as Java bytecode instrumentation. If you stop OneAgent service, monitoring will be disabled until the service is restarted.

## Start OneAgent using the command line

To start OneAgent again, use the following command:

`net start "Dynatrace OneAgent"`, where `Dynatrace OneAgent` is the service name for OneAgent.

Learn more about [how Dynatrace interacts with your OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").


---


## Source: uninstall-oneagent-on-windows.md


---
title: Uninstall Dynatrace OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows
scraped: 2026-02-17T04:53:57.108768
---

# Uninstall Dynatrace OneAgent on Windows

# Uninstall Dynatrace OneAgent on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

Your OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system.

## Uninstall OneAgent using Windows Control Panel

Use the Windows **Control Panel** to remove OneAgent.

After all OneAgent files have been removed from your system, you'll need to reboot your machine to remove the agent libraries from memory.

## Uninstall OneAgent silently

### Command line

To silently uninstall OneAgent using Windows command line, run the following WMIC commands as an administrator.

```
> wmic product where name='Dynatrace OneAgent' call uninstall /nointeractive
```

or

```
> wmic product where name='Dynatrace OneAgent' get IdentifyingNumber



IdentifyingNumber



{12345678-ABCD-1234-ABCD-12345678ABCD}



> msiexec /x {12345678-ABCD-1234-ABCD-12345678ABCD} /quiet /l*vx uninstall.log
```

You can omit `/l*vx uninstall.log` if the log file is not relevant to you.

### PowerShell

```
PS> $app = Get-WmiObject win32_product -filter "Name like 'Dynatrace OneAgent'"



PS> msiexec /x $app.IdentifyingNumber /quiet /l*vx uninstall.log
```

## After you uninstall OneAgent

Following uninstallation, log files, the user running OneAgent, and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.

For a complete OneAgent uninstallation, remove the following:

* Log files located at `%PROGRAMDATA%\dynatrace\oneagent\log`.
* Configuration files located at `%PROGRAMDATA%\dynatrace\oneagent\agent\config`.


---


## Source: update-oneagent-on-windows.md


---
title: Update Dynatrace OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows
scraped: 2026-02-17T04:54:02.129353
---

# Update Dynatrace OneAgent on Windows

# Update Dynatrace OneAgent on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

OneAgent installed in full-stack mode has a built-in, configurable auto-update mechanism.

See [OneAgent update](/docs/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") for an overview of OneAgent update, including how to monitor updates and how to create update windows.

## Configure OneAgent updates

You can configure OneAgent update globally, per host group, and per host.

Configure global OneAgent update

When automatic updates are turned on globally, whenever a new version of OneAgent becomes available, all of your installed OneAgent instancesâexcept where you have turned off auto-updates at the host group or host levelâwill automatically download the update and upgrade their binaries and configuration files.

Automatic update settings at the host group and individual host level override global settings.

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. Select one of the update options:

   * **Automatic updates at earliest convenience**  
     Update all OneAgents automatically, regardless of update windows.
   * **Automatic updates during update windows**  
     Update all OneAgents automatically during the selected update window.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host group OneAgent update

OneAgent update settings at the host group level override global settings and are overridden by settings at the host level.

1. Open the **Host group settings** page.  
   Access alternatives:

   * Go to **Settings** > **Monitoring** > **Monitoring overview**, find any host that is in the host group you want to configure, and select the host group name (not the host name).
   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**, open a host page, and expand the **Properties and tags** section. If the host belongs to a group, there is a link to it under **Host group**.
   * Go to **Deployment Status** > **OneAgents**. If a host belongs to a host group, a link to the host group settings page is displayed under the host name.
2. On the **Host group settings** page, select **OneAgent updates** on the left side of the page.
3. Select one of the update options:

   * **Inherit global update settings**  
     Follow the global update settings for updating OneAgents in this host group.

     + The current global setting is displayed in parentheses on this line.
     + To go to the global configuration page, select the `global` link.
   * **Automatic updates at earliest convenience**  
     Update all OneAgents in this host group automatically, regardless of update windows. Ignore the global update settings.
   * **Automatic updates during update windows**  
     Update all OneAgents in this host group automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update OneAgents in this host group. Ignore the global update settings.

Manually triggering **Update now to target version** will update all hosts running the selected OS and architecture combination, regardless of their automatic update status.

Configure host-level OneAgent update

OneAgent update settings at the host level override OneAgent update settings at the global and host group levels.

1. Open the **Host** page for the host you want to configure.  
   Access options:

   * Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and then select the host.
   * Go to **Settings** > **Monitoring** > **Monitoring overview**, select the **Hosts** tab, and then select the host.
2. On the **Host** page, open the browse menu (**â¦**) and select **Settings**.
3. Select **OneAgent updates** on the left side of the page.
4. Select one of the update options:

   * **Inheritâ¦**  
     Follow the host group or global update settings for updating this OneAgent.

     + If the selected host belongs to a host group, the current host group setting is displayed in parentheses on this line, and the group name is a link to the host group configuration page.
     + If the selected host does not belong to a host group, the global setting is displayed in parentheses on this line, and "global" is a link to the global configuration page (**Settings** > **Updates** > **OneAgent updates**).
   * **Automatic updates at earliest convenience**  
     Update this OneAgent automatically, regardless of update windows. Ignore the host group update settings.
   * **Automatic updates during update windows**  
     Update this OneAgent automatically during the selected update window. Ignore the global update settings.

     + When you choose this setting, a list of available update windows is displayed. Select one.
     + To configure a new update window for OneAgent updates, go to **Settings** > **Updates** > **Update windows for OneAgent updates**.
   * **No automatic updates**  
     Do not automatically update this OneAgent. Ignore the global update settings.

Manually update OneAgent on individual hosts

To manually update OneAgent running on an individual host:

1. Go to **Settings > Monitoring > Monitoring overview**.
2. Select the **Hosts** tab.
3. To update OneAgent or download the latest version, select **Update** next to the name of the host you're interested in.

   The **Update** button appears only if the installed version of OneAgent on a specific host is outdated and if it is a full-stack OneAgent. This button doesn't appear with PaaS and standalone OneAgents.
4. Select **Update now**.  
   If the **Update now** button is disabled, you don't have permissions to download the installer.

Alternatively, you can download the latest version of the OneAgent installer, copy it manually to the target host, and perform installation directly on the target host.

Select OneAgent version to install on new hosts

To control which version of OneAgent is automatically installed on all new hosts:

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In **Update mode**, select **No automatic updates** to disable automatic OneAgent updates.

   For details on how to disable OneAgent automatic updates on Paas/Kubernetes, see [DynaKube parameters for Dynatrace Operator on Kubernetes/OpenShift](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
3. In **Target version**, select the version of OneAgent to install on all new hosts.

The selected OneAgent version is also used for PaaS integrations.

Select OneAgent version to update to

To select which version of OneAgent to update to

1. Go to **Settings** > **Updates** > **OneAgent updates**.
2. In the **Target version** list, you can specify a particular version by OneAgent version number or select a relative target version:

   * **Latest stable version**  
     The most recent stable OneAgent version that is available in your environment. The actual version number is displayed in parentheses.
   * **Previous stable version**  
     The stable version before **Latest stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *two* less than the latest version number.
   * **Older stable version**  
     The stable version before **Previous stable version**. The currently corresponding version number is displayed in parentheses. The OneAgent version number increases by *two* for each release, so this number will be *four* less than the latest version number.

* **Specific OneAgent version**

The target version is used for:

* Automatic updates
* Automatic updates during maintenance windows
* Manual updates when you select the version you want to update to

You can set the target version and update mode at:

* **Environment level**
  Affects all OneAgents of an environment. Is also used for Deployment API.
* **Host group**
  Affects all OneAgents of a host-group. Overrides the environment level. Does not affect Deployment API.
* **Host**
  Affects OneAgent on this host. Overrides host group and environment-level configuration. Does not affect Deployment API.

If you select an older version than a currently deployed version, you won't be able to downgrade OneAgent. You will need to install a newer version over an existing OneAgent version.

## System requirements

### Disk space

For details, see [OneAgent files and disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.")

### Free memory

Your host requires 200 MB free memory to run OneAgent update.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### OneAgent command-line interface

Run `oneagentctl` with the `--version` parameter. For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.


---


## Source: windows.md


---
title: OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows
scraped: 2026-02-17T04:45:54.992853
---

# OneAgent on Windows

# OneAgent on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

You can install OneAgent on Windows using installer provided as a self-extracting EXE fileâfor single-server installationâand also as an MSI package, for Group Policy deployments. For analytical information about the supported OneAgent capabilities for Windows, see the [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms."). For the supported Windows versions, check the [OneAgent supported technologies and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Installation

[Disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.")

[OneAgent security](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")

[Install OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Learn how to download and install Dynatrace OneAgent on Windows.")

[Customize installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.")

[How to pass a proxy address](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows "Find out how to force Dynatrace OneAgent on Windows to use a proxy for communication with your environment.")

### Operation

[OneAgent files and logs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.")

[Update OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.")

[Stop/restart OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows.")

[Uninstall OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows "Learn how you can remove Dynatrace OneAgent from your system.")

### See also

[OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

[Troubleshoot](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.")


---


## Source: install-cics.md


---
title: Install the CICS module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics
scraped: 2026-02-17T04:56:10.056923
---

# Install the CICS module

# Install the CICS module

* Latest Dynatrace
* 14-min read
* Updated on Jan 28, 2026

With the CICS module, you can get observability for your CICS transactions and programs including DB2, DLI, and VSAM calls.

Observability for

Including

CICS transactions

Transactions initiated using

* IBM MQ Bridge and Trigger Monitor
* CICS Transaction Gateway, HTTP/S, SOAP over HTTP/S, JSON using non-Java JSON pipeline
* 3270 terminal

CICS programs

* Programs invoked using CICS LINK
* Transaction details for DPL LINK and START TRANSACTION requests in a distributed trace

Database calls

Database calls with their SQL statements from CICS to Db2 and IMS DB via the DL/I access method

File access

[File access](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access "File access monitoring of CICS applications using the CICS module.") from CICS via the VSAM and BDAM access methods.

Trace your CICS transactions end-to-end with Dynatrace

Analyze the performance of your transactions end-to-end using the [Service flow](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").

![CICS service flow](https://dt-cdn.net/images/cics-trace-2357-0a7717e199.png)

Use the [PurePath distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") to drill down to the code level and to optimize your programs.

![CICS code-level](https://dt-cdn.net/images/cics-code-level-1984-d6aeff52fb.png)

Understand exceptions in the context of your transactions down to the Db2 database layer.

![CICS distributed trace with exception](https://dt-cdn.net/images/cics-distributed-trace-1986-97b2240549.png)

Detect CICS anomalies and isolate fault domains with Dynatrace

Dynatrace Intelligence automatically pinpoints the root cause of problems and assesses their user impact so that you can prioritize mitigation strategies and reduce the mean time to repair.

![CICS automatic fault domain isolation](https://dt-cdn.net/images/cics-problem-1985-100d80f55c.png)

Analyze failures with exception details in the context of transactions.

![CICS failure analysis](https://dt-cdn.net/images/cics-exceptions-1985-478b6f8ba6.png)

## Installation

The CICS module includes a PLT program that initiates at CICS startup. This program uses hooks to instrument CICS terminal and application owning regions, creating events of interest. It forwards monitoring data to the zDC subsystem via shared buffers.

You need to install the CICS module in every CICS region you want to monitor. If Dynatrace is already installed on a CICS and you want to update your CICS module without restarting the CICS region, see [Update the CICS module without region restart](#cics-update).

You need to add the [z/OS Java module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#middleware "Set up Java monitoring on z/OS using the Java module.") to each CICS Transaction Gateway you want to monitor.

### CTS 6.2 support

Beginning with OneAgent version 1.299, we are providing support for CTS 6.2, which is a major change and follows the latest security enhancements for the CICS subsystem.

CTS 6.2 support requires the `DFHBPZDT` load module that is supplied in the `SZDTAUTH` to be available at CICS region startup.
Recommended installation procedure:

Add a line similar to the example below to a PROGxx parmlib member. Note that the `SZDTAUTH` should be APF authorized.

```
LPA ADD MODNAME(DFHBPZDT) DSNAME(<hlq>.SZDTAUTH)
```

To add the module to LPA immediately, enter a console command similar to the below example.

```
SETPROG LPA,ADD,MODNAME=DFHBPZDT,DSNAME=<hlq>.SZDTAUTH
```

Alternatively, it is also possible to add `DFHBPZDT` to the `STEPLIB` of the CICS 6.2 regions where the Dynatrace agent is installed.
However, we do not recommend adding the entire `SZDTAUTH` to the CICS STEPLIB.

To verify the installation, CTS 6.2 prints the following mesage:

```
DFHKE0010  HVPAC449 Vendor table DFHBPZDT for product ID ZDT has been loaded
```

### CICS library definition

You can dynamically add the load library as a CICS library definition in the CSD. The CEDA definition is in `SZDTSAMP` member `CICRDO`. You can find it in the example in the next section.

If you don't want to use the CICS Library definition, you need to add the following PDS (or its contents) to the DFHRPL concatenation:

```
// DD DISP=SHR,DSN=<hlq>.SZDTLOAD
```

Regardless of which option you decide to use, you need to tailor the DSN by replacing `<hlq>` with the high-level qualifier you set during [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Download and install the Dynatrace product datasets for z/OS.").

### Dynatrace CICS programs and transaction

The CICS resource definitions for the Dynatrace CICS module can be found in `SZDTSAMP` member `CICRDO`, which is provided for use with the batch `RDO` utility `DFHCSDUP`.

We recommend to use these transaction and group names, but you can change them in accordance with your installation policies. Coordinate the group name and group list name with your CICS administrator. Replace `XYZLIST` with the name of your group list (`GRPLIST`).

While we recommend to use the default transaction ID `DTAX` for `ZDTPLT`, you can also use a custom transaction ID instead of `DTAX` in your definitions if you have conflicting transaction definitions.

### CICS startup program list table

Add the CICS startup program (`ZDTPLT`) after the `DFHDELIM` entry in your PLTPI source code and assemble the table.

This step is optional for test installations because the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") can be used instead to enable the module after CICS initialization. We recommend that you place the `ZDTPLT` entry immediately before the `TYPE=FINAL` specification.

The JCL procedure `DFHAUPLE` in `CICSHLQ.SDFHINST(DFHAUPLE)` can be used to build the PLTPI table.

An example of the PLTPI table that contains the CICS startup program

```
*



* PLT USED TO SUPPORT DYNATRACE CODE MODULE INITIALIZATION



*



DFHPLT TYPE=INITIAL,SUFFIX=SI



DFHPLT TYPE=ENTRY,PROGRAM=DFHDELIM



* Other PLT startup programs here...



DFHPLT TYPE=ENTRY,PROGRAM=ZDTPLT



DFHPLT TYPE=FINAL



END
```

Compuware Xpediter Global storage protection users

The PLT startup program (`ZDTPLT`) initializes the CICS module's exit work area, which CICS obtains on its behalf. Products such as Compuware Xpediter/CICS may be configured to enforce strict storage access controls and may abend `ZDTPLT` and prevent the CICS module from starting unless it is excluded from these controls. If you use the Xpediter/CICS global storage protection feature, add a `monitor exceptions` entry to the XDDBPINP DD in the CICS region JCL to exclude `ZDTPLT*`. For example:

```
DBPA 17.02 TRAN=*,PROGRAM=ZDTPLT*,CSECT=*
```

### CICS shutdown program list table

Add the CICS shutdown program (`ZDTPLTSD`) before the `DFHDELIM` entry in your PLTSD source code and assemble the table.

We recommend to place the `ZDTPLTSD` entry immediately after the `TYPE=INITIAL` specification.

The JCL procedure `DFHAUPLE` in `CICSHLQ.SDFHINST(DFHAUPLE)` can be used to build the PLTSD table.

An example of the PLTSD table that contains the CICS shutdown program

```
*



* PLT USED TO SUPPORT DYNATRACE CODE MODULE SHUTDOWN



*



DFHPLT TYPE=INITIAL,SUFFIX=SD



DFHPLT TYPE=ENTRY,PROGRAM=ZDTPLTSD



* Other PLT shutdown programs here...



DFHPLT TYPE=ENTRY,PROGRAM=DFHDELIM



DFHPLT TYPE=FINAL



END
```

### Connect the CICS module to a zDC subsystem

The PLT startup program (`ZDTPLT`) automatically connects to the default zDC subsystem at CICS region initialization.

If multiple zDCs subsystems are running, it connects to the zDC that specifies `DEFAULT(YES)`, unless an `INITPARM` override parameter in the CICS SYSIN parameters specifies that it must connect to a zDC with a particular name:

```
INITPARM=(ZDTPLT='MEPC,<option>'),
```

`<option>` sets the log level for the CICS module; see [Logging](#logging).

To verify the connectivity between the CICS module and the zDC subsystem, [send a ping message](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction#ping "Manage the CICS module via DTAX transactions.").

## Customization

### CICSPlex name grouping

You can group CICS regions belonging to the same CICSPlex into a single process group. To do so

1. Go to **Settings** > **Mainframe** > **Transaction monitoring**.
2. Turn on **Group CICS regions that belong to the same CICSPlex**.
3. Add `MASPLTWAIT(YES)` to your LMAS parameter. It instructs the CICS region to wait for the CICSPlex to become available before proceeding. If the CICSPlex isn't available, the module can't consider it.
4. Optional The `MASINITTIME(10)` timeout interal defaults to 10 minutes. You can customize it in the range of 5 minutes to 59 minutes.

If you enabled CICSPlex name grouping **after** the CICS region is up, you need to run the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") `DTAX DISABLE` and `DTAX ENABLE`.

### CICS web services support

The CICS module can trace the CICS web services invoked through a SOAP request or a JSON request (non-Java JSON pipeline). You need OneAgent version 1.257 or later to trace JSON requests.

To trace the CICS web service provider programs that are invoked by handler programs from CICS SOAP pipelines or from CICS non-Java JSON pipelines, update the provider pipeline config (`.xml`) file with `ZDTSOAPH` as shown below.

Only pipelines using the standard terminal handler are supported by Dynatrace. If you are running a non-standard terminal handler, it can be instrumented via the CICS and IMS SDK. As a starting point, you can use the following code samples:

* [ADKJSONAï»¿](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsona.txt)âCICS assembler example of starting paths for JSON requests in a user-written apphandler.
* [ADKJSONCï»¿](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsonc.txt)âCICS COBOL example of starting paths for JSON requests in a user-written apphandler.

#### CICS SOAP pipeline

`DFHPITP` is the app handler program used in the CICS SOAP pipeline config that invokes the service provider programs. In addition to the `DFHPITP` in the pipeline, the CICS code module also supports user-written terminal programs.

Update your pipeline config file to include `ZDTSOAPH` in the `<headerprogram>` stanza under the SOAP handler element. Note that all SOAP pipelines have the SOAP handler element `<cics_soap_1.1_handler>` or `<cics_soap_1.2_handler>` where `ZDTSOAPH` is added. Below is a sample CICS SOAP provider pipeline updated with `ZDTSOAPH`.

To trace outbound SOAP requests that originate within CICS transactions that are traced by a CICS module, add the `<headerprogram>` stanza to the service requester pipeline definitions of those SOAP services that should be traced. Outbound SOAP requests that occur within CICS transactions that aren't traced are ignored. However, tracing isn't limited to requests from SOAP programs that act as CICS SOAP service providers.

```
<?xml version="1.0" encoding="EBCDIC-CP-US"?>



<provider_pipeline



xmlns="http://www.ibm.com/software/htp/cics/pipeline"



xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance"



xsi:schemaLocation="http://www.ibm.com/software/htp/



cics/pipeline/provider.xsd ">



<service>



<terminal_handler>



<cics_soap_1.1_handler>



<headerprogram>



<program_name>ZDTSOAPH</program_name>



<namespace>*</namespace>



<localname>*</localname>



<mandatory>true</mandatory>



</headerprogram>



</cics_soap_1.1_handler>



</terminal_handler>



</service>



<apphandler>DFHPITP</apphandler>



</provider_pipeline>
```

#### OneAgent version 1.257+ CICS non-Java JSON pipeline

`DFHPIJT` is the terminal handler program used in the CICS non-Java JSON pipeline that invokes the service provider programs. To trace the CICS web service provider invoked through the non-Java JSON pipeline, update your pipeline config file to include `ZDTSOAPH` in the `<handler>` stanza under the `<default_http_transport_handler_list>` xml tags. Below is a sample CICS non-Java JSON provider pipeline updated with `ZDTSOAPH`.

```
<?xml version="1.0" encoding="EBCDIC-CP-US"?>



<provider_pipeline xmlns="http://www.ibm.com/software/htp/cics/pipeline">



<transport>



<default_http_transport_handler_list>



<handler>



<program>ZDTSOAPH</program><handler_parameter_list/>



</handler>



</default_http_transport_handler_list>



</transport>



<service>



<terminal_handler>



<handler>



<program>DFHPIJT</program><handler_parameter_list/>



</handler>



</terminal_handler>



</service>



</provider_pipeline>
```

### Route DTAX messages using TDQueue

Optional To route DTAX messages to the Dynatrace TDQueue (Transient Data Queue), use the `ZDTQ` resource definition provided above in your `CICRDO` member.

DTAX messages will only be written to the ZDTQ TDQueue if the queue is open. If you use the supplied resource definition, the queue remains closed due to the `OPENTIME(DEFERRED)` attribute. You can manually open it by using the `CEMT INQUIRE|SET TDQUEUE` command or you can set up the queue to open at initialization time, by modifying the TDQUEUE definition for ZDTQ to use the `OPENTIME(INITIAL)` attribute.

## Logging

You can control the CICS module log level either by using the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") or by specifying an optional `INITPARM` at CICS region startup.

```
INITPARM=(ZDTPLT='MEPC,<Option>'),
```

`<Option>` sets the logging level for CICS module. Accepted values are:

1. `FINE` | `F` for fine logging. We recommend to enable it only when the CICS module has difficulties during startup.
2. `INFO` | `I` for info logging. This is the default.
3. `WARNING` | `W` for warning messages logging.
4. `SEVERE` | `S` for severe messages logging.

```
Example:



INITPARM=(ZDTPLT='MEPC,SEVERE'),
```

There are two different sets of CICS logs:

* One set of messages occurs when the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") issues the `DISABLE` and `ENABLE` commands. These messages are written to the CICS CSMT Transient Data Queue(usually written to MSGUSR). View these messages in the CICS job spool. DTAX also writes a set of messages to the CEEOUT SYSOUT statement when errors occur in the connection between the zDC and the DTAX transaction. View these messages in the CICS Job spool. As long as the DTAX transaction can connect to the zDC, it logs its messages to the zRemote.
* The CICS module monitoring transaction activity routes its log messages to the zDC, and subsequently to the zRemote. The log shows if any corrupted distributed traces, timeouts, or other errors occurred. You may also see some statistical information in these logs.

You can access the CICS logs via the [zRemote logs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#logging "Prepare and install the zRemote for z/OS monitoring.").

## Update without region restart

To update your CICS module to a newer version without restarting the region

1. [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Download and install the Dynatrace product datasets for z/OS.") and [extract them](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Download and install the Dynatrace product datasets for z/OS.").
2. Use the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") to disable the CICS module in the CICS region with the `DISABLE` command.
3. Copy the CICS modules in the `SZDTLOAD` dataset into the Dynatrace `DFHRPL` dataset defined to your CICS region.
4. Use the CICS command `CEMT I PROG(ZDT*)` to display the CICS modules. Use the `SET PROG(ZDT*) NEWCOPY` command to tell CICS a new version of each program will be used.
5. Use the DTAX transaction to enable the CICS module with the `ENABLE` command. Verify that the new CICS module version is displayed on the DTAX panel.

## FAQ

How can I verify whether the CICS module and resources are installed correctly?

The group name might be different, as well as the two-character suffix representing the CICS release of the module (for example, CTS52 uses 69).

From the CICS region, look for these messages to validate the CICS module resources have been defined:

```
CICSAPPL Install for group XXXX has completed successfully.



CICSAPPL OWNER CSSY Resource definition for ZDTAGT72 has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTDC2 has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTDC2A has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTPLT has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTPLTSD has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTSOAPH has been added.



CICSAPPL OWNER CSSY TRANSACTION definition entry for DTAX has been added.
```

How can I verify whether the CICS module PLT program is invoked?

The CICS module logs initialization messages to the zRemote log.

The zRemote log can be accessed from within Dynatrace, in the same manner as all the other module log files. Look for log entries similar to the following:

```
2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registering a pgi for the job: HVBAC021, host=10.30.220.41, groupId= f39f4801966aa7c7, pgir.groupInstanceID= fad6dee63cfd1522, hostID= 95c0bb0371704b8c, nodeID= fad6dee63cfd1522, groupName=HVBAC021, hostGroup=, processGroupType= 28



2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registered SubAgent[C021,51,32aa8d038887d1c9] with zDC[Z021,52], rc=true



2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021], subagentid[32aa8d038887d1c9] snaId[NETD    .HVBAC021], CICS release 54 was successfully registered with zdc[52] using protocol version=7.2.0, allocator=pooled.



2019-05-09 20:19:13.789 UTC [d37f9842] info    [native] ASID[52], smfID[S0W1], sysid[Z021], jobName[AFVBZ021] - ZDC955I  - Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021.



2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP008I - ZDTP008I ZDTAGT71.



2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP020I - ZDTP020I Active Sensors: MQ DB2 DB2R SOAP CTG DB2Fetch DLI DLIR HTTP .
```

What should I do if a CICS region cannot connect to the zDC?

Check the job log of the affected CICS regions for the following message, where `yyyy` is the subsystem ID of the zDC that the CICS region is trying to connect to. It might be blank if the CICS region is trying to connect to the default subsystem that is configured with the DEFAULT(YES) parameter. We recommend to simply search for the error message code.

```
ZDTP004W zDC yyyy unavailable
```

Verify that the zDC with that subsystem ID is started. If so, try to issue the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") command `ENABLE` to re-enable the connections.

How can I detect a version incompatibility?

Ensure that the CICS module version is less than or equal to zRemote module version. Don't connect newer CICS modules to older zRemote modules. Following is a sample message in the zRemote log when an CICS module version is incompatible with the zRemote version.

```
severe  [native] CICS14CR1[asid = 108] is trying to initialize with an invalid protocol version number : x.xxx.xx
```


---


## Source: install-ims.md


---
title: Install the IMS module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims
scraped: 2026-02-17T04:56:14.596889
---

# Install the IMS module

# Install the IMS module

* Latest Dynatrace
* 21-min read
* Updated on Nov 18, 2025

With the IMS module, you can get observability for your IMS transactions and programs including IBM MQ and database calls.

Observability for

Including

Transactions

* IMS
* Fast Path
* [BMPï»¿](https://www.ibm.com/docs/en/ims/15.1.0?topic=bmps-batch-message-processing-transaction-oriented)

Transactions initiated using

* IBM MQ Bridge and Trigger Monitor
* IMS TM Resource Adapter, IMS SOAP Gateway, and IMS Connect
* 3270 terminal

Database calls

Database calls with their SQL statements from IMS to Db2 and IMS DB via

* the DL/I access method
* the Fast Path access methods

## Installation

The IMS module captures data on various IMS transaction processing events and forwards monitoring data to the zDC subsystem via shared buffers.

To install the Dynatrace IMS module:

1. Install the IMS module into the Control Region of each IMS DB/DC and DCCTL system that you want to monitor. This is enough to cover all message processing regions associated with the Control Region.
   Note that installing the IMS module into a DBCTL only system is not supported.
2. You need to add the Dynatrace exit to each IMS Connect that you want to monitor.
3. You need to add the [z/OS Java module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#middleware "Set up Java monitoring on z/OS using the Java module.") to each IMS SOAP Gateway you want to monitor.

IMS restart

4. You must re-execute the injection job after each IMS restart. For more details, see the [Injection notes](#injection-notes).

### Updating a previously installed version of Dynatrace

If you have Dynatrace installed and are upgrading to a newer release, you can jump to section [Update without region restart](#update) later in this document.

### IMS Connect

Add the authorized Dynatrace dataset `<hlq>.SZDTAUTH` to the IMS Connect job STEPLIB to permit IMS Connect to load the Dynatrace exit HWSTECL0.

* If you use IMS Connect Extensions, concatenate SZDTAUTH after the IMS Connect Extensions library.
* If you use a locally developed HWSTECL0 exit, concatenate SZDTAUTH ahead of the dataset that contains the local exit.

The IMS Connect exit can be enabled to create PurePath nodes in a distributed trace. Activate the required [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS IMS Connect**.

* If the IMS Connect exit is configured to create PurePath nodes, the exit will connect to the default zDC subsystem name. The target zDC subsystem name can be overridden by specifying the following DDNAME and keyword parameter in the IMS Connect startup JCL:

```
//ZDTPARMS DD *



ZDCID=<zDC_Id>
```

The IMS Connect exit is required to support the IMS Connect API protocol and to support the IMS SOAP Gateway in cases when the SOAP Gateway has not been configured to insert a tracking ID using the `iogmgmt` tracking command.

### IMS Control region

You must run the Injection Utility to install the IMS module into the control region.

1. Authorize `<hlq>.SZDTAUTH` by adding it to the APF list
2. Run the ZDTINST job from the `<hlq>.SZDTSAMP` PDS.

Detail information on the parameters can also be found in the ZDTINST PDS member.

Sample JCL with positional parameters:

```
//S1       EXEC PGM=ZDTIINST,PARM='<IMS_Id>,<zDC_Id>'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

Sample JCL with keyword parameters:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=<IMS_Id>



ZDC=<zDC_Id>
```

The injection utility (ZDTIINST) supports changing the size of `pathid` tables without requiring an IMS restart and re-injection of the module. A path table size can be changed by using the `M` action code with a path table segment specification as the sixth parameter and, optionally, the target IMSID as the seventh parameter.

Below is the complete list and description of the positional parameters of the injection utility. All parameters must be upper case:

```
// ...    PARM='<IMS_Id>,<zDC_Id>,<ActionCode>|<PathTableSize>,



<WaitZdcMin>,<Y|N>,<PathTableSegm>,<PathTableIms>'
```

The injection utility parameters can be specified as either positional or keyword parameters. There are seven positional parameters. Keyword parameters must be specified in a SYSIN file. The positional parameters on the EXEC JCL statement are still valid, however any new parameters added in the future will only be added as SYSIN keyword values. If an EXEC PARM parameter value is found, no SYSIN parameters will be considered. The recommended method is to use a SYSIN file and keyword parameters.

Symbol

Position

Keyword

Description

Required

`<IMS_Id>`

1

IMSID=

The four-character IMSID of the control region.

This parameter is not needed when you're using the garbage collection function to reclaim ECSA storage that contains no longer used IMS modules.

Required

`<zDC_Id>`

2

ZDC=

The four-character zDCID used in the SUBSYSTEM\_ID() parameter of the target zDC.

This parameter is not needed when the requested target zDC is the DEFAULT zDC. In that case type in the asterisk (`*`) or omit the parameter.

Required

`<ActionCode>|<PathTableSize>`

3

ACTION= | SIZE=

The one-character action code or the value for `pathid` table size.

#### Action code

Action codes specify an action to be taken on the previously injected IMS module. An action code is not applicable to the initial injection of the IMS module and is mutually exclusive with the `pathid` table size value.

If a valid action code is specified, the injection program doesn't re-inject the IMS module and performs the specified action on the already injected module. This means that no new versions of the IMS modules will be loaded.

Action codes are:

* **E**: Enable (switch on) an injected IMS module that was previously disabled.
* **D**: Disable (switch off) an injected IMS module. The IMS module is no longer invoked. Use the `E` action code to re-enable it.
* **G**: Garbage collection. If the IMS module has been updated and injected, ECSA storage for the old (unused) load modules of the IMS module is reclaimed with this function. See the [Garbage collection notes](#gc-notes) section for more information.
* **M**: Modify the recovery option of the injected IMS module when this value is used in conjunction with the fifth parameter, `<Y|N>`.  
  Alternatively, modify the size of any previously allocated path tables, when used in conjunction with the sixth parameter `<PathTableSegm>`, and optionally the seventh parameter `<PathTableIms>`.  
  Alternatively, modify the size of any previously allocated Fast Path SMO (Shared Memory Object) when used in conjunction with the `FPATHSIZE=` statement.
* **F**: Free all resource locks and reset the `pathid` table pointers. This action code should never be used unless the `E` action has failed because a IMS module resource is locked or as directed by Dynatrace Support.

#### Table size value

The `pathid` tables size value is used for the initial IMS module injection and is mutually exclusive with actions codes. If the IMS module is already injected, the table size value is ignored.

The table size value can be expressed as SEGM=nnnn, where nnnn is up to a 4 digit number of 1-megabyte segments

The actual number of usable entries may be higher, as the storage is allocated above the specified quota. The number of entries will be adjusted upwards to use all available allocated storage.

If the parameter is omitted upon initial IMS module injection, a default of four segments (4 MB) is used. This provides space for 8,191 entries (approximately 2,048 entries per segment).

The number of allocated entries should correspond to the expected number of IMS distributed traces during any one-minute interval. When the number of traced IMS transactions exceeds the number of available table slots, new distributed traces are not recorded.

#### No third parameter specified

If no third parameter is set, the injection program injects the IMS module.

You can also use this option to update the IMS module. In that case existing table size will remain intact.

Optional

`<WaitZdcMin>`

4

ZDCWAIT=

The wait time for the target zDC to initialize, in minutes (max two digits).

The default value is 30 minutes. The target zDC must have been initialized at least once since the last system IPL before the IMS module can complete initialization.

Optional

`<Y|N>`

5

DUMP=

Indicates whether the IMS module should capture an SVC dump when ABEND recovery is driven.

This parameter can be specified during initial injection of the IMS module or in conjunction with the `M` or `E` action codes (parameter number 3) to toggle on/off the dump capture during recovery for the previously injected IMS module.

The default value is `Y`, which means dump capture is enabled.

Optional

`<PathTableSegm>`

6

SEGM=

The value that resizes `pathid` tables.

This parameter is only applicable in conjunction with the `M` action code (parameter number 3). The format of value is `SEGM=nnnn`, where `nnnn` is the number (up to 4 digits) of 1-megabyte segments.

Optional

`<PathTableIms>`

7

PATHIMS=

The value (up to 4 characters) that specifies the IMSID for which the pathid table is to be resized.

This parameter is only applicable in conjunction with the `M` action code (parameter number 3) and the `<PathTableSegm>` value (parameter number 6).

If an IMSID is specified, only the pathid table for that IMS is resized.  
If the parameter is omitted, only the `pathid` table for the local IMS (specified as parameter number 1) is resized.  
If the asterisk (`*`) is specified, the `pathid` table for the local IMS **and** `pathid` tables allocated locally for all remote IMSIDs are resized.

Optional

n/a

n/a

REMOTESEGM=

Sets the number of segments to use when allocating remote pathid tables. The format of the value is `REMOTESEGM=nnnn`, where `nnnn` is the number (up to 4 digits) of 1-megabyte segments.

The parameter is optional, valid only as a `SYSIN` parameter, and ignored when the `ACTION=` keyword is specified. When omitted, the default value of `4` megabytes is used.

This parameter doesn't change the size of any existing remote pathid tables. To change the allocation of an existing remote pathid table you must use the `ACTION=M`, `SEGM=`, and `PATHIMS=` keywords.

Optional

Example 1. Inject the IMS module into IMS IB01 for zDC ZDC1.

Accept the default `PathTableSize` and wait for up to 20 minutes for ZDC1 to initialize.

With positional parameter:

Note that the third positional parameter is not specified.

```
//S1       EXEC PGM=ZDTIINST,PARM='IB01,ZDC1,,20'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IB01



ZDC=ZDC1



ZDCWAIT=20
```

Example 2. Disable the IMS module previously injected into IMSB for zDC ZDC1.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSB,ZDC1,D'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSB



ZDC=ZDC1



ACTION=D
```

Example 3. Enable the previously injected, but disabled IMS module in IMSB for zDC ZDC1.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSB,ZDC1,E'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSB



ZDC=ZDC1



ACTION=E
```

Example 4. Inject the IMS module into IMS IMSA for zDC ZDC1.

Specify that IMS module ABEND recovery should also capture an SVC dump.

With positional parameter:

Accept the defaults for the third and fourth parameters.

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,,,Y'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



DUMP=Y
```

Example 5. Set IMS module ABEND recovery dump capture off for a previously injected IMS module.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,M,,N'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



DUMP=N
```

Example 6. Change the size of the path table for the local IMS.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,M,,,SEGM=3'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



SEGM=3
```

Example 7: Change the size of the path table for IMS IMSB which is a remote IMS to IMSA.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,M,,,SEGM=1,IMSB'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



SEGM=1



PATHIMS=IMSB
```

Example 8: Inject and set the remote pathid table size to 2 megabytes.

Use the `REMOTESEGM=2` parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



REMOTESEGM=2
```

### Fast Path transaction tracing

Symbol

Position

Keyword

Description

Required

n/a

n/a

FPATH=

Indicates whether to activate Fast Path transaction tracing:

* **Y**: Inject and enable Fast Path hooks. Enables hooks that are injected but disabled.
* **N** (Default): Does not inject Fast Path hooks. Disables hooks that are injected and enabled.

Valid only as a SYSIN parameter and only for IMS Version 15 or later.

If omitted or specified incorrectly, no action is taken.

Optional

n/a

n/a

FPATHSIZE=

The size of the Fast Path SMO (Shared Memory Object) for Fast Path transaction tracing, in 1 MB segments. The range is `1`-`9999`. The default is `4`.

This value can be used on the initial injection of the IMS module, or in conjunction with a modify action statement (`ACTION=M`) to resize the Fast Path SMO.

Valid only as a SYSIN parameter and only for IMS Version 15 or later.

Optional

Example 9: Inject and enable Fast Path transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



FPATH=Y
```

Example 10: Disable Fast Path transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



FPATH=N
```

Example 11: Inject and enable Fast Path transaction tracing and override the default SMO size of 4 megabytes.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



FPATH=Y



FPATHSIZE=8
```

Example 12: Change the size of the Fast Path SMO post injection.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



FPATHSIZE=2
```

### BMP transaction tracing

IMS module version 1.259+

Symbol

Position

Keyword

Description

Required

n/a

n/a

BMP=

Indicates whether to activate transaction tracing for BMP regions:

* **Y**: Enables transaction tracing for BMP regions.
* **N** (Default): Disables transaction tracing for BMP regions.

Valid only as a SYSIN parameter.

If omitted or specified incorrectly, BMP transaction tracing will be disabled.

Optional

## BMP transaction tracing notes

Automatic tracking for transaction-oriented BMPs (message input is from the IMS message queues) will be the same as currently exists for MPP/IFP regions: if the input message is being tracked by a control region sensor, a path will be started for the transaction in the BMP region.
Automatic tracking for work performed by batch (non-transaction oriented) BMPs can only be done if the input message is via an MQGET (see restrictions below). Otherwise, batch BMP support means the agent performs initialization services for the BMP region (allocates work areas and places sensors) but does not start any paths.
For both transaction-oriented and batch BMPs, a path is started for the BMP region whenever the application issues an MQGET, provided all of the following are true:

1. Instrumentation is enabled for the z/OS IMS MPR MQ filter in the UI Settings.
2. Another sensor has not already started a path for the BMP region.
3. The MQ queue name for the MQGET is included or not excluded by its presence or absence from the IMS MQ filters list (**Settings** > **Mainframe** > **IBM MQ Filters**).
4. A DL/I CHKP call is made before the first MQGET. This is only required for batch-oriented BMPs.

For both transaction-oriented and batch BMPs, the SDK can be used to instrument the application to send the event messages to start and end paths.
There is no capability to limit the tracking to specific BMP job names or PSBs or to track batch work other than IMS BMPs.

Example 13: Enable BMP transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



BMP=Y
```

Example 14: Disable BMP transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



BMP=N
```

## Garbage collection notes

When updating the IMS module you can reclaim ECSA storage used by the old version of the IMS module.

After the injection job for the updated IMS module is run, IMS Message Region activity is necessary to update internal control blocks to point to the new version of the IMS module. After that, you can re-run the injection job with the `G` action code set in parameter number 3. This marks the old version of the IMS module as a candidate for deletion.

After at least 3 hours, run the injection job with the `G` action code set in parameter number 3 once again. This releases the ECSA storage containing the old version of the IMS module.

You can run the injection job with the `G` action code set in parameter number 3 repeatedly; there is no negative side effect to doing so. But in order to have the garbage collection process reclaim unused module storage, the process must be invoked at least twice after an IPL, with at least 3 hours between the first and second invocation.

## Injection notes

Start the zDC at least once after the system IPL before executing the IMS module injection job.

If the target zDC has not been up since the last IPL, the injection job waits for it to come up. The wait time defaults to 30 minutes but can be set by the `<WaitZdcMin>` parameter. If the zDC is still not up after this time then injection cannot proceed and the injection job terminates with user `ABEND` code of 100.

If the zDC has been up at least once since the last system IPL, the injection job can complete even when the zDC is not currently up. In this case warning messages are issued indicating that the zDC is not started and data collection is not available, and the injection job completes with `RC=4`.

Start and fully initialize the IMS system before you execute the IMS module injection job. If you stop and start the IMS system, the injection job must be re-run. If you start a new IMS-dependent region or stop and restart one, no action is required.

When the IMS module is updated in a previously injected IMS, re-execute the IMS module injection job to pick up the updated IMS module load modules. Do not specify an action code for the injection job in parameter number 3. The IMS **does not** require a restart after the IMS module update.

We recommend that you use an automation facility like IMS Time-Controlled Operations (TCO) to execute the IMS module injection job.

All IMS module injection messages are written to the job log. You can control the level of messages by including specific DDNAMEs in the injection job JCL. If no DDNAMEs are included, the default is level 4 for informational messages. The specific DDNAMEs and message levels are the following:

* `//DTMSGLV0 DD SYSOUT=*` For finest level 0 DEBUG messages and above
* `//DTMSGLV2 DD SYSOUT=*` For fine level 2 DEBUG messages and above
* `//DTMSGLV4 DD SYSOUT=*` For informational level 4 messages and above
* `//DTMSGLV5 DD SYSOUT=*` For warning level 5 messages and above

Injection job failures typically result in a user `ABEND` code of 100. In most cases, the cause of failure can be determined by prior diagnostic messages that have been written to SYSPRINT.

Depending on your z/OS system parameters, a symptom dump may also be written to the job log, but a dump is not captured unless one of the following DDNAMEs is included in the injection job JCL:

```
//SYSABEND DD SYSOUT=*



//SYSMDUMP DD DSN=DT.IMSAGENT.INJECT.SDUMP,DISP=(OLD,KEEP,KEEP)
```

Both sample JCL members ZDTINST (injection utility) and ZDTIDIAG (diagnostic utility) contain a final step to execute procedure ZDTZLOGC. The function of the ZDTZLOGC step is to copy the job's spool output to an HFS log file so that it will automatically be included in a support archive. There is a new JCL procedure (ZDTZLOGC), REXX program (ZDTZLOGR), and assembler program (ZDTZLOGS) included for this function. To implement it do the following:

1. Copy sample JCL member ZDTZLOGC to a PDS to contain the modified JCL. Within the JCL PROC the DSN for the DD names SYSEXEC and SZDTAUTH must be changed.  
   `//SYSEXEC DD DISP=SHR,DSN=<hlq>.SZDTSAMP` <- change `DSN` to where `REXX` exec `ZDTZLOGR` resides (see step 3)  
   `//SZDTAUTH DD DISP=SHR,DSN=<hlq>.SZDTAUTH` <- change `DSN` to where program `ZDTZLOGS` resides
2. Both sample members ZDTINST and ZDTIDIAG contain a JCLLIB statement that must be changed and the ZDTZLOGC proc step must have the `<ZDC Id>` supplied.  
   `JCLLIB ORDER=(<hlq>.SZDTSAMP)` <- change `DSN` to where the `ZDTZLOGC` JCL proc resides (see step 1)  
   `//ZDTZLOGC EXEC ZDTZLOGC,ZDC='<ZDC Id>',COND=(EVEN)` <- change ZDC Id (for example, `MEPC` or `*` for default zDC)

## Logging

There are two sets of IMS module logs.

* The first set of IMS messages comes from the IMS injection job. These are messages that occur during injection of the module into the IMS control region. These messages only appear in the job spool of the IMS module injection job.
* The second set of IMS messages comes from the IMS module as it monitors IMS activity. These messages are sent to the zDC and then are routed to the zRemote.

You can access the IMS module logs via the [zRemote logs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#logging "Prepare and install the zRemote for z/OS monitoring.").

## Update without region restart

To update your IMS module to a newer version without restarting the region

1. [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Download and install the Dynatrace product datasets for z/OS.") and [extract them](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Download and install the Dynatrace product datasets for z/OS.").
2. Update the injection job to point to the new `<hlq>.SZDTAUTH`. If you have [defined an alias](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#alias "Download and install the Dynatrace product datasets for z/OS."), redefine the alias. For example:

   ```
   DELETE 'DT.DYNTRC.SZDTAUTH' NOSCRATCH



   DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12710.SZDTAUTH'))
   ```
3. Run the injection job without the action code to pick up the updated IMS module. For more details, see the [Injection notes](#injection-notes).
4. To recover the ECSA used by the old version of the IMS module see section [Garbage collection notes](#gc-notes).

## FAQ

How can I deactivate the IMS module?

If an ABEND occurs in the IMS module, the recovery process produces ABEND diagnostics if possible, and then it disables the IMS module. The IMS system continues to function. When this occurs, a series of WTO messages are written to the system log for the IMS control region and/or IMS dependent region. A sample normal message set follows:

```
ZDTI032W Recovery routine entered.



ZDTI036W ZDTIII15 0000000 20221103 10.51 VER 1.255.0 ABEND at offset 007874.



ZDTI033W Successful ABEND recovery, agent disabled.
```

Different or additional messages might be issued if abnormal conditions are encountered by the recovery process (for example, when dynamic storage cannot be obtained, retry is not permitted, or no SDWA was passed). All of the messages related to the ABEND recovery process are documented in the [z/OS module messages](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Messages that are created by the Dynatrace z/OS modules.") section.

A Software (SFT) Error Record further describing the ABEND is usually written to the z/OS system SYS1.LOGREC data set. You should run the z/OS EREP utility program to print the Software (SFT) Error Record associated with the ABEND.

Optionally, an SVC dump might be taken during recovery, depending on the ABEND recovery option specified or defaulted to when the IMS module was injected. The default action is to capture an SVC dump when ABEND recovery is driven. This option can be specified as a parameter when the IMS module is initially injected or specified in conjunction with the Modify or Enable function parameters to toggle dump capture during recovery on or off for a previously injected IMS module.

When the IMS module is disabled as a result of the ABEND recovery process, it remains disabled until explicitly reenabled using the IMS module injection program.

How can I detect a version incompatibility?

Ensure that the IMS module version is less than or equal to zRemote module version. Don't connect newer IMS modules to older zRemote modules. Following is a sample message in the zRemote log when an IMS module version is incompatible with the zRemote version.

```
severe  [native] IMS14CR1[asid = 108] is trying to initialize with an invalid protocol version number : x.xxx.xx
```


---


## Source: customize-zremote.md


---
title: Customize the zRemote module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote
scraped: 2026-02-17T04:58:04.751424
---

# Customize the zRemote module

# Customize the zRemote module

* Latest Dynatrace
* 9-min read
* Updated on Aug 11, 2022

You can customize the zRemote module to enable optional features and optimize its performance.

## User configuration files

The following configuration files are retained in the event of a zRemote update or uninstallation. You can make changes here.

You must restart the zRemote service to apply new settings.

### zRemote module user configuration

The zRemote module user configuration file (`zremoteagentuserconfig.conf`) allows you to override the default configuration defined in `ruxitagent.conf`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

### Watchdog user configuration

Dynatrace version 1.277+ The watchdog user configuration file (`watchdoguserconfig.conf`) allows you to override the default configuration defined in `oneagentzwatchdog.ini`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

Available parameters for configuration:

Parameter

Unit

Default value

Description

-healthcheck.heartbeat.timeout

Seconds

900

The connection timeout between the zRemote service and your Dynatrace environment

-healthcheck.memory.limit\_absolute

MiB

500

Absolute input for the memory calculation limit of the child process

-healthcheck.memory.limit\_percentage

%

20

Percentage input for the memory calculation limit of the child process

Effective memory limit calculation

Effective limit = percentage limit Ã available physical memory on the system + absolute limit

For example:

0.2 Ã 5 GiB + 500 MiB = 1.5 GiB effective memory limit

## Organize LPARs with host groups

Host groups are helpful when you want to organize multiple LPARs connecting to a single zRemote module. An LPAR can be assigned to a host group by setting the `[HostGroup]` attribute in the `zremoteagentuserconfig.conf` file. An LPAR can belong to only one host group.

To assign an LPAR to a host group, specify the group name in between a pair of `[HostGroup]` attributes. The `[HostGroup]` attribute pair can occur anywhere in the `zremoteagentuserconfig.conf` file.

```
[HostGroup]



<LPAR_Name1>=<HostGroupName>



<LPAR_Name2>=<HostGroupName>



[HostGroup]
```

The LPAR name is the 8 characters logical partition name defined in the `LPARNAME()` parameter in `IEASYMxx` member in z/OS.

The LPAR name is also displayed in the `Properties and tags` section on the host screen.

The following requirements apply to the `<HostGroupName>` string:

* Can contain only alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`)
* Must not start with `dt.`
* Maximum length is 100 characters

Combining three LPARs to a single host group

In this example, we add three LPARsâ`LPARA`, `LPARB`, and `LPARC` to a single host group `TEST_HOST`.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=TEST_HOST



LPARC=TEST_HOST



[HostGroup]
```

Assigning three LPARs to different host groups

In this example we assign each LPAR to a separate host group.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=PROD_HOST



LPARC=PERF_HOST



[HostGroup]
```

* In host settings, only the **General**, **Monitoring**, and **Detected processes** menus are applicable for a z/OS host group.
* Store your host group settings only in the `zremoteagentuserconfig.conf` file and migrate your host group settings from the `ruxitagent.conf` file.
* Host group settings take effect during zRemote start up. You must restart the zRemote module after defining host group in the `zremoteagentuserconfig.conf` file.

## Fetch full SQL statements from Db2 databases

Dynatrace can provide insight into SQL statements based on tracing of Db2 and DL/I database calls. These SQL statements are shown in Dynatrace, for example, as:

* **FETCH (PROGNAME;165;3)**
* **CLOSE (PROGNAME;441;2)**

The string represents the program name (DBRM name), the line number, and the section number.

Example for captured SQL statements

![zRemote SQL statement fetch off](https://dt-cdn.net/images/zremote-sql-fetch-off-1600-5beae13988.png)

zRemote module version 1.241+ Dynatrace can provide deeper insight into Db2 database calls by fetching the full SQL statements from the Db2 catalog. With the **SQL statement fetch** feature enabled, the SQL statements are shown in Dynatrace, for example, as:

* **FETCH (GETTAB INTO : H , : H , : H , : H , : H)**
* **CLOSE (GETTAB)**

Example for captured SQL statements with enabled SQL statement fetch feature

![zRemote SQL statement fetch on](https://dt-cdn.net/images/zremote-sql-fetch-on-1602-ff3d0f1c32.png)

### Enable SQL statement fetch

The **SQL statement fetch** feature is disabled by default. To enable it

1. Install and configure the IBM Data Server Driver for ODBC and CLI software on [Linuxï»¿](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-linux-unix-operating-systems) or [Windowsï»¿](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-windows-operating-systems). Further reading: [IBM Db2 ODBC CLI driver Download and Installation informationï»¿](https://www.ibm.com/support/pages/db2-odbc-cli-driver-download-and-installation-information).

   In the installation step take note of the location of the CLI driver library:

   * `libdb2.so` for Linux
   * `db2app64.dll` for Windows

   Before configuring the driver, it might be necessary to contact the DBA requesting the database connectivity information (such as database credentials, location, and IP and port). In the configuration step, take note of the Db2 aliases (or DSN).

   Both are required in the next steps.

   * The zRemote module supports only 64-bit CLI driver.
   * We strongly recommend that you set the connection timeout for every DB alias, for example, ConnectTimeout=2
     for two seconds in db2cli.ini on Linux
   * Be sure to test the CLI driver configuration to ensure good Db2 connections, for example:

     ```
     \<cli-driver-path\>/bin/db2cli validate -connect -database \<db-location\>:\<ip\>:\<port\> -user \<id\> -passwd \<pw\>



     \<cli-driver-path\>/bin/db2cli validate -connect -dsn \<db-alias\>
     ```
   * To configure the CLI driver, you need Db2 credentials that grant access to Db2 connections (from distributed using DDF/DRDA) and grants to select on CATALOG, specifically on SYSPACKSTMT.
2. In the `zremoteagentuserconfig.conf` file of the zRemote module, define the CLI driver library and Db2 alias group (similar as defining host groups), for example:

   ```
   # Linux



   cli_driver_lib=/opt/IBM/CLIDRIVER/lib/libdb2.so



   # ... or Windows



   cli_driver_lib=C:/IBM/CLIDRIVER/bin/db2app64.dll



   [DbAlias]



   dbHost1.dbName1=alias1



   dbHost2.dbName2=alias2



   dbHostN.dbNameN=aliasN



   [DbAlias]



   # Beginning with zRemote 1.279 it is possible to set the new flag sqlStmtExtended, if



   # true the full (fetched) SQL statement is appended with its old (unfetched) format,



   # for example, from an example above "FETCH (GETTAB INTO : H , : H , : H , : H , : H)"



   # would be shown as "FETCH (GETTAB INTO : H , : H , : H , : H , : H) (PROGNAME;165;3)".



   # The default is false. Note: if enabled this setting would affect the aggregation count.



   sqlStmtExtended=false
   ```

   where `dbHost` is the z/OS SMF ID and `dbName` is the Db2 subsystem name. All is case sensitive.
3. Optional Define `sqlStmtCacheFileName=/tmp/sqlStmtCacheFileName`, as an example, to cache the fetched SQL statements to a file and use it upon a zRemote module restart, thus reducing Db2 interactions. Be sure to use the appropriate fully qualified file name.
4. Restart the zRemote module.

   * The zRemote module will only enable the **SQL statement fetch** feature if the CLI driver can be loaded successfully and there is at least one DB2 alias defined.
   * If the Db2 alias is later found to be invalid, the feature is disabled.

## Enable secure zLocal-zRemote connection

zRemote module version 1.267+

By default, the zLocal and zRemote use a proprietary communication protocol via plain sockets. You can configure them to communicate via TLS by configuring AT-TLS for the zLocal and setting the SSL flags for the zRemote as shown below.

### AT-TLS configuration for the zLocal

Depending on your requirements, there are different ways to configure AT-TLS for zLocal. For more details, refer to [Application Transparent Transport Layer Security data protectionï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=applications-application-transparent-transport-layer-security-data-protection) in IBM documentation. You can use the example AT-TLS configuration below as a template.

Example of an AT-TLS configuration

```
TTLSRule                       <client-rule>



{



RemoteAddr                 <ALL | specific-ip-addr>



RemotePortRange            <zdclistenerport>



Direction                  Outbound



TTLSGroupActionRef         <group-action>



TTLSEnvironmentActionRef   <environment-action>



TTLSConnectionActionRef    <connection-action>



}



TTLSGroupAction                <group-action>



{



TTLSEnabled                On



Trace                       <trace-level>



}



TTLSEnvironmentAction          <environment-action>



{



HandshakeRole              Client



TTLSKeyringParmsRef        <keyring-parms>



TTLSCipherParmsRef         <cipher-parms>



}



TTLSKeyringParms               <keyring-parms>



{



#   A certificate matches that of the zRemote's certificate



#   must be loaded into RACF and connected to the Keyring here.



Keyring                    <pub-key-or-certificate>



}



TTLSCipherParms                <cipher-parms>



{



...



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384



...



}



TTLSConnectionAction           <connection-action>



{



TTLSConnectionAdvancedParmsRef  <connection-advanced-parms>



}



TTLSConnectionAdvancedParms    <connection-advanced-parms>



{



SSLv2                      Off



SSLv3                      Off



TLSv1                      Off



TLSv1.1                    Off



TLSv1.2                    On



TLSv1.3                    On



}
```

Be sure the userId used in the zDC job is the same one that owns the certificate.
Otherwise, the connection to the TSL handshake will fail (with SSL accept error -1 and code 5).

### SSL/TLS settings for the zRemote

To enable SSL/TLS for the zRemote

1. Open the `zremoteagentuserconfig.conf` file.
2. Set `sslEnabled` to `true`.
3. Specify the absolute paths to your private key (`sslPrivateKey`) and certificate (`sslCertificate`) PEM files.
4. Optional Define specific TLS cipher suites. For information about allowed cipher suite names and their string format, refer to [OpenSSL documentationï»¿](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).

Show configuration template

```
# Must be true to enable secure connection; all other SSL settings are ignored if false



sslEnabled=true



# Absolute paths to your private key (with the pass-phrase stripped) and certificate PEM files.



# Beginning with zRemote module version 1.301.0, multiple private-key/certificate pairs delimited



# by a semicolon can be specified. For example:



# sslPrivateKey=<private-key-1.pem; private-key-2.pem; ...; private-key-n.pem>



# sslCertificate=<certificate-1.pem; certificate-2.pem; ...; certificate-n.pem>



sslPrivateKey=<private-key.pem>



sslCertificate=<certificate.pem>



# Optional: TLS cipher suites allowed according to OpenSSL



# Example: sslCiphers=ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384



sslCiphers=<cipher-suites>
```

## Ignore invalid connection attempts

If a specific process regularly pings the zRemote module to detect its availability, and these pings reach the zRemote listener port, the zRemote module logs an invalid connection attempt. These invalid connection attempts increase the zRemote log size over time.

To ignore connection attempts from specific processes, list their IP addresses (separated by semicolons) in the `zremoteagentuserconfig.conf` file, for example:

```
ignoreHandshakeEndpoints=192.168.0.1;10.0.0.2
```

## Opt out of new IMS MPR process ID calculation

zRemote module version 1.253+

The IMS message processing region (MPR) process IDs could change, resulting in new process and service entities in Dynatrace. To prevent this process ID change, weâve introduced a more stable ID calculation with the consequence that all IMS MPR process and service entities will change once but then remain stable after an update of the zRemote module with version 1.253.

To opt out of the new IMS MPR process ID calculation, set the flag `useOldImsPgiCalc` in the `zremoteagentuserconfig.conf` file to `true`.

```
useOldImsPgiCalc=true
```


---


## Source: install-zremote.md


---
title: Install the zRemote module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote
scraped: 2026-02-16T21:21:19.341811
---

# Install the zRemote module

# Install the zRemote module

* Latest Dynatrace
* 8-min read
* Updated on Jan 22, 2026

The zRemote module processes monitoring data received from the zLocal and routes that data, compressed and encrypted, via its local ActiveGate to Dynatrace. Hence, the zRemote module offloads much of the processing work from the CICS, IMS, and z/OS Java code modules incurred in instrumenting subsystems and applications to an open system.

You can [customize the zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote "Customize the zRemote module for your needs.") to enable optional features like **Host groups** and **Db2 SQL statement fetch**.

## Hardware requirements

The hardware requirements of the machine where the zRemote module runs depend on the number of anticipated CICS and IMS transactions to be monitored per second. See the hardware requirements for x86-64 and s390 architecture machines below.

* For CICS and IMS development environments: a small or medium-sized machine.
* For CICS and IMS production environments: a large or extra-large machine.
* For z/OS Java environments: a small or medium-sized machine.

Hardware requirements

Small (DEV)

Medium (DEV)

Large (PROD)

X-Large (PROD)

**Anticipated monitored CICS/IMS transactions per second**

**4,000**

**7,500**

**15,000**

**30,000**

Required CPU cores on x86-64 architecture (Xeon E5-2600 series)

2

4

8

16

Required [IFL processorsï»¿](https://www.ibm.com/products/integrated-facility-for-linux) on s390 architecture

1

1

1

2

Required memory

4GB

6GB

8GB

16GB

Required disk space

20GB

20GB

20GB

20GB

* The hardware requirements are for the case when the zRemote module and its ActiveGate are used for mainframe monitoring only.
* Multiple [zDC subsystems](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).") can be connected to a single zRemote as long as the number of monitored transactions matches the hardware requirements.

## System requirements

We recommend installing the zRemote module on an IBM Z or LinuxONE mainframe, on an supported Linux operating system for s390. The following system requirements apply:

* The zDC subsystem and the zRemote module to which it connects must be located within the same data center to avoid performance and security issues.

  + The zRemote will write a warning to its logs after a connection latency of 3 seconds.
  + The zRemote will drop the connection after a connection latency of 10 seconds.
* The zRemote only supports a [host-based ActiveGate installation](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") configured for a single environment.
* Monitoring of the host running the zRemote with OneAgent is only supported in [full-stack monitoring mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

### Supported operating systems

You can install the zRemote module on any Linux and Windows operating system listed below.

| Distribution | Versions | CPU architectures |
| --- | --- | --- |
| Oracle Linux | 8.10 | x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4 | s390, x86-64 |
| Rocky Linux | 8.10 | x86-64 |
| SUSE Enterprise Linux | 15.6 | s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04 | s390 |
| Windows | 10, 11 | x86-64 |
| Windows Server | 2016, 2019, 2022, 2025 | x86-64 |

## Installer overview

The overview outlines the key components of the zRemote application, the zRemote configuration, and their default installation directories. Non-persistent directories are replaced during updates and uninstallation.

### zRemote application and installation directories

Linux

Windows

Base path: `/opt/dynatrace/zremote`

Base path: `C:/Program Files/dynatrace/zremote`

All of the following directories are not retained in the event of a zRemote update or uninstallation. If you make changes here, they will be overwritten or deleted.

Directory

Component

Description

`agent/lib64`

noneagentz

The zRemote binary

`agent/lib64`

oneagentzwatchdog

A binary that provides the service capabilities for the zRemote service and controls resource limits

`agent/lib64`

oneagentdumpproc

A binary that supports creating dumps when the main application crashes

`agent/lib64/zos-s390-64/<version>`

dtzagent

A binary deployed to the UNIX part of the mainframe to support OneAget communications. For more details, see [Install the zDC subsystem](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).")

`agent/lib64/zos-s390-64/<version>`

libdtzagent.so

A binary deployed to the UNIX part of the mainframe to support agent communications. For more details, see [Install the zDC subsystem](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).")

`agent/conf`

ruxitagent.conf

The default zRemote configuration file

`agent/conf`

oneagentzwatchdog.ini

The default watchdog configuration file

`agent/conf`

.pem

Application certificates

`agent`

installer.version

The installer version of the zRemote binary, which is usually the same as the zRemote version

`agent`

zremote

Linux only The service script for running the zRemote application

uninstallation.sh

Linux only The service script for uninstalling the zRemote application.

It removes everything except the persistent user configuration and log files.

### zRemote configuration and installation directories

Linux

Windows

Base path: `/var/lib/dynatrace/zremote`

Base path: `C:/Program Files/dynatrace/zremote`

All of the following directories are not retained during zRemote update or uninstallation. If you make changes here, they will be overwritten or deleted.

Directory

Component

Description

`agent`

runtime

Contains the connection details as specified by your Dynatrace environment.

`config`

instance.properties

Contains the ID of the currently registered instance.

`config`

version.properties

Contains the full version number of the zRemote module.

state

Contains the address of the last successful server connection to indicate a properly established connection.

The following directories are retained in case of update or uninstallation. You can make changes here. For more details, see [Customize the zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote "Customize the zRemote module for your needs.").

Directory

Component

Description

`agent/conf`

zremoteagentuserconfig.conf

The configuration file for zRemote module customization

`agent/conf`

watchdoguserconfig.conf

The configuration file for watchdog customization

## Installation

The zRemote module is downloaded and installed automatically during the ActiveGate installation procedure on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Linux.") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Windows.").

1. In Dynatrace Hub, select **ActiveGate** > **Set up**.
2. On the **Install Environment ActiveGate** page, select **Linux** or **Windows**.
3. Linux only Select installer type **s390** (recommended) or **x86/64**.
4. Select the purpose **Install the zRemote module for z/OS monitoring**, download the installer, and start the installation procedure.
5. Optional Customize the listening port selection.

   By default, the zRemote module listens on port 8898 for connections from the zLocal running as part of the zDC. To listen on a different port, set the `zdclistenerport` parameter to your port in the `zremoteagentuserconfig.conf` file. Make sure this port is not blocked by a firewall.

For details on the default installation settings, see ActiveGate default installation settings for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Learn about the default settings with which ActiveGate is installed on Windows.").

For details on customizing the installation, see customize ActiveGate installation on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Learn about the parameters that you can use with ActiveGate on Windows.").

## Logging

The zRemote logs are created on the machine where the zRemote module is installed, in the default directories for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Learn about the default settings with which ActiveGate is installed on Windows."). You can view the zRemote logs either directly on the machine hosting the zRemote or by requesting them from Dynatrace via the [OneAgent diagnostics](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") workflow.

The actual zRemote log should contain the following messages:

* Log messages that are sent from all CICS/IMS code modules and the zDC.
* Log messages that are sent from the zLocal.

## Update and maintenance

To stay current, you can update the zRemote module automatically to a newer version by using the [ActiveGate auto-update procedure](/docs/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.").

To manually update the zRemote module

Linux

Windows

1. If you have customized the installation, back up the `zremoteagentuserconfig.conf` file of the zRemote module and the `custom.properties` file of the ActiveGate. The installer should not overwrite these files, but we recommended backing them up for safety.
2. Uninstall the zRemote module.

   ```
   /opt/dynatrace/gateway/uninstall.sh
   ```
3. Install the zRemote module.

   ```
   ./bin/bash Dynatrace-ActiveGate-Linux-<arch>-<version>.sh --enable-zremote
   ```

1. If you have customized the installation, back up the `zremoteagentuserconfig.conf` file of the zRemote module and the `custom.properties` file of the ActiveGate. The installer should not overwrite these files, but we recommended backing them up for safety.
2. Uninstall the zRemote module via the Windows Control Panel.
3. [Install the zRemote module](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Windows.") by executing the installer.

### Operations

To stop, start, or restart the zRemote module, you can use the following commands.

Linux

Windows

You need root privileges to execute these commands.

To query the current status of the zRemote module:

```
service zremote status
```

To stop, start, or restart the zRemote module:

```
service zremote stop|start|restart|forcestop
```

The difference between `stop` and `forcestop` is that the `stop` command instructs the process to execute its controlled shutdown routine, while `forcestop` forces the process shutdown.

You need admin privileges to execute these commands.

On Windows, the zRemote module can be maintained using the **Services** tab of the Windows Task Manager. You can also use the following command:

```
sc stop|start|restart "Dynatrace zRemote"
```

The `sc` command is asynchronous, so you need to query the status of the service, to determine when it has fully stopped:

```
sc query "Dynatrace zRemote"
```


---


## Source: download-zos-datasets.md


---
title: Download z/OS product datasets
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets
scraped: 2026-02-16T21:30:13.309751
---

# Download z/OS product datasets

# Download z/OS product datasets

* Latest Dynatrace
* 5-min read
* Updated on Nov 03, 2023

You can download the PAX file containing the CICS, IMS, z/OS Java, and zDC modules in two ways:

* Dynatrace version 1.272+ Download via [Deployment API](#using-deploymentapi).
* Dynatrace version 1.276+ Download via [web UI](#using-webui).

Starting with OneAgent release 1.275, the PAX file will no longer be published on our FTP server.

## Download the PAX file

You can download the latest or a specific PAX file version via web UI or the [Deployment API](/docs/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.") of OneAgent.

The PAX file version must be less than or equal to the zRemote module version.

### Download latest version via web UI

1. Search for **Deploy OneAgent**
2. Select **z/OS** and **Download z/OS product datasets** to download the latest PAX file version.

The file name `dynatrace-zos-1.nnn.m.pax` includes the major release version `nnn` and `m` minor.

### Download a specific version via web UI

You can download a specific PAX file version via web UI as follows:

1. Go to **Settings** > **Monitoring** > **Monitoring overview**.
2. Select **Download Dynatrace OneAgent or ActiveGate installer** and define your preferred version:

   1. Installer: `OneAgent - z/OS`
   2. Build: Select your preferred major version
   3. Revision: Select your preferred minor version

   ![zos monitoring overview](https://dt-cdn.net/images/zos-monitoring-overview-1289-aa537f3578.png)
3. Select **Continue** and **Download z/OS product datasets** to download your defined PAX file version.

   The file name `dynatrace-zos-1.nnn.m.pax` includes the major release version `nnn` and `m` minor.

### Download latest version via Deployment API

You can download the latest PAX file version via Deployment API as follows:

1. Generate an [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the scope **PaaS integration - Installer download** (`InstallerDownload`).
2. Download the latest PAX file via [Deployment API - Download latest OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API."):

   HTTP method

   Dynatrace environment

   Endpoint

   GET

   SaaS

   `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest`

   GET

   Managed

   `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/latest`

   Below is a sample `curl` command for a SaaS environment that uses the Deployment API to download the latest PAX file version:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Replace `<environment>` with your Dynatrace environment ID and `<accessToken>` with your generated access token.

### Download a specific version via Deployment API

You can download a specific PAX file version via Deployment API as follows:

1. Generate an [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the scope **PaaS integration - Installer download** (`InstallerDownload`).
2. List all available PAX file versions via [Deployment API - List available versions of OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.").

   HTTP method

   Dynatrace environment

   Endpoint

   GET

   SaaS

   `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe`

   GET

   Managed

   `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/zos/mainframe`

   Below is a sample `curl` command for a SaaS environment that uses the Deployment API to list all available PAX file versions:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe" -H "accept: */*" -H "Authorization: Api-Token <accessToken>"
   ```

   Replace `<environment>` with your Dynatrace environment ID and `<accessToken>` with your generated access token.
3. Download a specific PAX file version via [Deployment API - Download OneAgent of specific version](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version "Download the OneAgent installer of the specific version via Dynatrace API."):

   HTTP method

   Dynatrace environment

   Endpoint

   GET

   SaaS

   `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/{version}`

   GET

   Managed

   `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/version/{version}`

   Below is a sample `curl` command for a SaaS environment that uses the Deployment API to download a specific PAX file version:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/<version>" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Replace `<environment>` with your Dynatrace environment ID, `<version>` with your selected PAX file version, and `<accessToken>` with your generated access token.

## Extract product datasets

You can extract the product datasets from the PAX file as follows:

1. Transfer the PAX file to your z/OS USS directory in binary mode.
2. Rename the PAX file from `dynatrace-zos-1.nnn.m.pax` to `dynatrace-zos.pax`.
3. Use the `EXTRACT` job below to extract the product datasets from the installation files. Before running the job, modify the following:

   1. Determine the desired high-level qualifier for the install dataset names and set the `HLQ` variable accordingly.
   2. Set `MYUSS` to the z/OS USS directory path where you placed the `dynatrace-zos.pax` file. If the directory path exceeds 42 characters, it might result in an error in the `STEP3` of the job. In such case, you need to modify the JCL to accommodate the continuation character.
   3. Change the volume serial number `VOLSER` to match site standards.

   EXTRACT job

   ```
   //EXTRACT JOB ('ACCTINFO'),'User name or comment',NOTIFY=&SYSUID,



   //             MSGLEVEL=(1,1),CLASS=A,MSGCLASS=X,REGION=0M,



   //             COND=(0,NE)



   //*



   //* !!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



   //*



   //* When upgrading the zDC to version 1.213+ while



   //* the CICS code module is enabled, it is important to follow



   //* the below steps in the given sequence.



   //*



   //* 1. Stop the zDC



   //* 2. Wait for 15 minutes for the CICS code module to



   //*    reset/cleanup the control blocks



   //* 3. Upgrade the zDC to newer version



   //* 4. Start the zDC



   //*



   //* !!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



   //*



   //* This job extracts the product installation datasets from



   //* the installation files at <MYUSS>/GIMZIP to



   //* <hlq>.<rel>.SZDT* libraries.



   //*



   //* Change the JOB card and the SET statements below to meet



   //* site standards.



   //*



   //* Verify if the SMPCPATH and SMPJHOME DD below points to the



   //* correct PATH to meet site standards.



   //*



   //* WARNING!



   //* This JCL must be in mixed case and sequence numbers are not allowed



   //*



   // EXPORT SYMLIST=*



   // SET HLQ='DT'             <== HLQ of the target PDS datasets



   // SET REL='R12770'         <== Release number



   // SET VOLSER='NSM001'      <== Volume of the target PDS datasets



   // SET MYUSS='/u/dt'        <== USS work directory



   //*



   //*



   //STEP1   EXEC PGM=IKJEFT01,DYNAMNBR=10



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH rm -Rf &MYUSS/GIMZIP



   BPXBATCH SH cd &MYUSS &&  +



   pax -rvf dynatrace-zos.pax GIMZIP



   //*



   //*



   //STEP2    EXEC PGM=GIMUNZIP,PARM='HASH=YES'



   //SMPDIR   DD PATH='&MYUSS/GIMZIP/',PATHDISP=KEEP



   //SMPCPATH DD PATH='/usr/lpp/smp/classes/',PATHDISP=KEEP



   //SMPJHOME DD PATH='/usr/lpp/java/J8.0/',PATHDISP=KEEP



   //SMPOUT   DD SYSOUT=*



   //SYSPRINT DD SYSOUT=*



   //SYSUT3   DD UNIT=SYSALLDA,SPACE=(CYL,(25,5))



   //SYSUT4   DD UNIT=SYSALLDA,SPACE=(CYL,(25,5))



   //SYSIN    DD *,SYMBOLS=EXECSYS



   <GIMUNZIP>



   <ARCHDEF archid="AUTHLIB"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTAUTH">



   </ARCHDEF>



   <ARCHDEF archid="LOAD"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTLOAD">



   </ARCHDEF>



   <ARCHDEF archid="SAMPLE"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTSAMP">



   </ARCHDEF>



   </GIMUNZIP>



   /*



   //*



   //STEP3   EXEC PGM=IKJEFT01,DYNAMNBR=10



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH export ussdir=&MYUSS &&+



   cp ${ussdir}/GIMZIP/dynatrace-oneagent-zos-java.jar +



   ${ussdir}/dynatrace-oneagent-zos-java.jar



   //*



   //*



   //STEP4   EXEC PGM=IKJEFT01,DYNAMNBR=55



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH rm -Rf &MYUSS/GIMZIP



   //
   ```

   If the job ends with a return code of `0`, the extraction was successful.

   Optional Delete `dynatrace-zos.pax` and `dynatrace-oneagent-zos-java.jar` (if it is not needed) to free up disk space.

### Product datasets

The extraction process creates the following product datasets (the names are provided for the default high-level qualifier and the `R1nnnx` release version):

* `DT.R1nnnx.SZDTAUTH`: Contains the zDC subsystem and the IMS module including IMS Connect
* `DT.R1nnnx.SZDTLOAD`: Contains the CICS module
* `DT.R1nnnx.SZDTSAMP`: Includes sample JCL and CICS RDO definitions

Disk space usage of the product datasets

On an average, the product datasets and installation files in the z/OS USS directory use the following disk space:

```
Dsname                Tracks(3390) %Used



---------------------------------------



DT.R1nnnm.SZDTAUTH      893          5



DT.R1nnnm.SZDTLOAD       61         27



DT.R1nnnm.SZDTSAMP     1221         24
```

```
./GIMZIP/                      8K



./dynatrace-zos-1.nnn.m.pax    5M
```

### Define aliases

We recommend defining an `ALIAS` without the version number for the product datasets. Use these `ALIAS` in the zDC, CICS, and IMS module injection jobs. You can then perform maintenance without updating the jobs.

For example:

```
DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12770.SZDTAUTH'))



DEFINE ALIAS(NAME('DT.DYNTRC.SZDTLOAD') RELATE('DT.R12770.SZDTLOAD'))
```


---


## Source: installation.md


---
title: z/OS installation overview
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation
scraped: 2026-02-17T04:53:25.901767
---

# z/OS installation overview

# z/OS installation overview

* Latest Dynatrace
* 1-min read
* Published Jul 22, 2016

Since the z/OS modules require multiple components in both the mainframe environment and open systems, the installation process is more complex than the standard OneAgent installation. However, with a bit of planning and coordination with the varied architecture groups, the installation of the code modules can go smoothly.

Efficient z/OS module installation is typically a team effort involving the following:

* **Open Systems Administrator**âInstalls the zRemote module.
* **Mainframe Systems Programmer**âDownloads and installs the Dynatrace product datasets for z/OS.
* **Mainframe Security Administrator**âSets up security for the zDC subsystem.
* **Mainframe Systems Programmer**âInstalls the modules on each technology you want to monitor.

Depending on your team, a single individual may be able to administer more than one of the required tasks.

![z/OS monitoring architecture](https://dt-cdn.net/images/zos-architecture-1745-8d165d1510.png)

## Related topics

* [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")


---


## Source: monitor-cics-file-access.md


---
title: Monitor file access of CICS applications
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access
scraped: 2026-02-17T04:56:11.626633
---

# Monitor file access of CICS applications

# Monitor file access of CICS applications

* Latest Dynatrace
* 1-min read
* Published Jan 13, 2023

With Dynatrace, you can monitor the VSAM and BDAM file access calls from your CICS applications using the CICS module. Each accessed file in a CICS region is represented as a database service on the [Databases](/docs/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.") page, including metrics like response time, failure rate, and throughput.

![File access on the Database page](https://dt-cdn.net/images/file-sensor-db-3052-6d5ec51cdd.png)

The [Distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") page lists the file operations and logical file names that are being accessed on the [PurePath method-level](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces."). The file operations are aggregated per logical file name (for example, in the image below, the `READNEXT` operation was executed 21 times on the file `EXMPCAT`).

![File access calls in the Distributed traces page](https://dt-cdn.net/images/file-sensor-pp-3142-684de155b6.png)

## Get started

To start monitoring the file access calls from your CICS applications

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Activate the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS CICS file monitoring sensor**.
3. Restart your CICS region or allow [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") to pick up the new configuration setting in the next 5 minutes interval.

## Remote files

In the application program, if the file control API has a `SYSID` clause with the remote `SYSID`, the file is recognized as a remote file. However, if the file is defined as remote in the `CEDA` definition, the CICS module doesn`t recognize the file as a remote file.

## Turn off File access monitoring

To turn off file access monitoring, toggle the `z/OS CICS file monitoring` sensor and the `Instrumentation enabled (change needs a process restart)` to off. The CICS region need not have to be restarted for the settings to take effect. The DTAX transaction picks up the file sensor changes (on/off) within 5 minutes.


---


## Source: monitor-zos-logs.md


---
title: Monitor z/OS logs
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs
scraped: 2026-02-17T04:56:05.134542
---

# Monitor z/OS logs

# Monitor z/OS logs

* Latest Dynatrace
* 4-min read
* Updated on Jan 28, 2026

zRemote module version 1.297+ zDC module version 1.291+

Log analysis is typically one of the first steps in troubleshooting application problems. When a critical issue arises, it is therefore essential that you have the right logs to quickly and easily understand the full scope of what is happening within your applications.

Dynatrace can automatically discover and collect logs from monitored IBM CICS regions and IBM IMS subsystems. All collected logs are enriched with metadata to map them to the entity model of z/OS hosts (logical partitions) and z/OS processes (regions and subsystems). This allows you to extend your root cause analysis for any issue identified by Dynatrace Intelligence causal AI with logs automatically linked to your applications.

To learn more about related use cases, see [Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.").

The following log sources are supported:

* CICS module version 1.291+ MSGUSR DD statement for IBM CICS regions
* IMS module version 1.295+ Primary and secondary master terminal for IBM IMS subsystems

Log Management and Analytics requires a license:

* For Dynatrace Platform Subscription, a [Log Management and Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") capability.
* For Dynatrace classic licensing, [Davis data units](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

## Get started

Collection of logs from z/OS requires a [Log ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis."). You can get started by using one of the existing built-in rules.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Activate log ingest rule**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#ingest-rules "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Mask sensitive log data**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#mask-data "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Analyze log data**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#analyze-logs "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")

### Step 1 Activate log ingest rule

Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.

Activate one of the following built-in rules to ingest discovered logs from your IBM CICS regions and IBM IMS subsystems to Dynatrace.

Rule

Condition

Scope

**z/OS CICS message user**

**Log source** is: `z/OS CICS message user`

**Log record level** is any of: `ERROR` or `WARN`

Environment

**z/OS IMS master terminal**

**Log source** is any of: `z/OS IMS primary master` or `z/OS IMS secondary master`

**Log record level** is any of: `ERROR` or `WARN`

Environment

![z/OS log settings](https://dt-cdn.net/images/zos-log-settings-1651-077ed26fb6.png)

#### Limit the scope of rules

If necessary, you can limit the scope of a log ingest rule to a specific group of LPARs (hosts group) or LPAR (host) so that logs are ingested only for those.

To do this, define a [Log ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") with the required [scope](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#scopes "Include and exclude specific log sources already known to OneAgent for storage and analysis.") (host group or host).

#### Control which logs are ingested

If necessary, you can use attributes to precisely control which logs are ingested.

To do this, define a [Log ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") with specific attributes so that only logs that match those attributes are ingested. For example, you can use the following attributes.

Attribute

Description

Search dropdown logic

**Log source**

Matching is based on a **Log source** attribute. For CICS, select the `z/OS CICS message user`. For IMS, select either or both of `z/OS IMS primary master` or `z/OS IMS secondary master`.

Can be entered manually. No time limit.

**Log record level**[1](#fn-1-1-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**Log content**

Matching is based on the content of the log; wildcards are supported in the form of an asterisk.

Can be entered manually. No time limit.

**Process group**

Matching is based on the process group ID.

Entities visible in the last 3 days are listed.

1

Log record level attribute, transformed by OneAgent, is different than the log `status` attribute transformed by the Dynatrace server. Learn more by accessing the [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") page.

### Step 2 optional Mask sensitive log data

Configure masking of sensitive data as described in [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

### Step 3 Analyze log data

Dynatrace Log Analytics enables novel ways to analyze telemetry data, significantly expanding the observability use cases for IBM Z mainframes.

For example, you can quickly investigate specific error log lines in the **Log Viewer**. Thanks to the enriched log data, the log lines are connected to the respective **z/OS Host** page.

![z/OS logs in Log viewer](https://dt-cdn.net/images/zos-log-view-1856-7977ddf3ad.png)

![z/OS logs on Host page](https://dt-cdn.net/images/zos-log-host-1622-00c71be1be.png)

You can also perform advanced queries in **Notebooks** with the Dynatrace Query Language (DQL). For example, with DQL, you can quickly query all abends or drill down into specific job statistics.

![DQL query for z/OS logs](https://dt-cdn.net/images/zos-log-dql-1630-0cc40d3a7d.png)

## FAQ

Which metadata is added to the ingested z/OS logs?

All ingested logs are enriched with the following metadata: `dt.process.name`, `host.name`, `log.source`, `os.name`, `zos.job_id`, `zos.job_name`, `zos_job_step_id`, `dt.entity.host`, `dt.entity.process_group`, `dt.entity.process_group_instance`, and `dt.source_entity`.

This metadata is used to map the logs to the entity model of z/OS processes.


---


## Source: zos-java-custom-jmx-metrics.md


---
title: Monitor JMX metrics on z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics
scraped: 2026-02-17T04:56:08.818052
---

# Monitor JMX metrics on z/OS

# Monitor JMX metrics on z/OS

* Latest Dynatrace
* 5-min read
* Published Sep 06, 2022

JMX (Java Management Extensions) is handy for monitoring applications built using Java. With the OneAgent z/OS Java code module, you can monitor any metric in your JVM that is exposed via an MBean.

* Every monitored custom JMX metric consumes Davis data units. The concept of [Included metrics per host unit](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") isn't applicable for monitored LPARs on z/OS. To learn more about Davis data units, see [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").
* [PMI (Performance Monitoring Infrastructure)ï»¿](https://www.ibm.com/docs/en/was/9.0.5?topic=health-performance-monitoring-infrastructure-pmi) for the IBM WebSphere Application Server is currently not supported.

## Definition

The `customJmxMetrics` attribute defines a list of [metrics](#metrics) to be monitored. To get started, add the `customJmxMetrics` attribute to your `dtconfig.json` file as shown in the following example.

Typically, you've created the `dtconfig.json` file during the [z/OS Java code module installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Set up Java monitoring on z/OS using the Java module.") and have set the attributes `Tenant`, `ClusterID`, and `zdcName` to your environment.

```
{



"Tenant": "myTenant",



"ClusterID": myCluster,



"ZdcName": "DEFAULT",



"customJmxMetrics": [



{



"name": "java.lang.CurrentThreadCount",



"source":



{



"domain": "java.lang",



"keyProperties": {



"type": "Threading",



},



"attribute": "ThreadCount"



}



}



]



}
```

## Metrics

Each metric has the following mandatory attributes:

| Field | Type | Description |
| --- | --- | --- |
| `name` | String | Sets the name of the metric in Dynatrace. It must start with a letter. Only alphanumeric characters or `.` are allowed. |
| `source` | Object | Specifies how the metric is collected. For details, see the [Source](#source) section below. |

## Source

The source specifies how a metric is collected using JMX. Each source has the following mandatory attributes:

| Field | Type | Description |
| --- | --- | --- |
| `domain` | String | Domain name of the MBean. It can contain wildcards (`*`). |
| `keyProperties` | Key, Value pairs | Key properties of the MBean. Values can contain wildcards (`*`). |
| `attribute` | String | Name of the attribute that contains the metric value. |

Optional source attributes are:

| Field | Type | Description |
| --- | --- | --- |
| `attributePath` | String | See [CompositeData] below.(#compositedata) |
| `allowAdditionalKeys` | Boolean | If true, additional key properties other than those specified in `keyProperties` are allowed but ignored. If false, the `keyProperties` need to match exactly; additional keys in the name will lead to a mismatch. |
| `calculateDelta` | bool | If true, calculate the change in values of the given attribute. Value = attribute(t) - attribute(t-1). This is useful for monotonically increasing values. |
| `calculateRate` | bool | If true, calculate the rate of changes per second. This is used in combination with `calculateDelta` to convert an absolute attribute (for example, Request Count) to a rate (for example, Requests per Second). Value = attribute / query interval. |
| `aggregation` | String | Aggregates multiple values if more than one MBean matches the domain and key property filter. Default aggregation is `SUM`. Available aggregations are: `SUM`, `AVG`, `MIN`, `MAX`. For example, you can use this attribute to aggregate all `MemoryPools` and calculate their `SUM` or `MAX` value. |
| `splittings` | List | Set [splittings](#splittings). |

### AttributePath (CompositeData)

To extract values of individual keys returned as `CompositeData` type by an attribute, you need to use the `attributePath` mechanism and point to the key you're interested in.

For example, `HeapMemoryUsage` is a `CompositeData` type that returns the following list of value-key pairs:

```
{



committed: integer,



init: integer,



max: integer,



used: integer



}
```

If you want to extract the value of `used` from the `HeapMemoryUsage` attribute, point the `attributePath` to the `used` key.

```
{



"customJmxMetrics": [



{



"name": "java.lang.HeapMemoryUsage",



"source":



{



"domain": "java.lang",



"keyProperties": {



"type": "Memory"



},



"attribute": "HeapMemoryUsage",



"attributePath": "get(\"used\")"



}



}



]



}
```

### Splittings

Splittings can be used to define additional dimensions for a metric.

```
"splittings": [



{



"name": "dimension",



"keyProperty": "name"



}



]
```

Each splitting has the following mandatory attributes:

| Field | Type | Description |
| --- | --- | --- |
| `name` | String | Sets the name for this dimension. |
| `keyProperty` | String | Defines which key property of the `ObjectName` of an MBean is used for splitting. See the `keyProperties` attribute of the [source](#source). |

The following example shows how to define a metric providing multiple dimensions within a single metric definition:

```
{



"customJmxMetrics": [



{



"name": "java.lang.MemoryPoolUsage",



"source":



{



"domain": "java.lang",



"keyProperties": {



"type": "MemoryPool",



"name": "*"



},



"attribute": "Usage",



"attributePath": "get(\"used\")",



"splittings": [



{



"name": "memory_type",



"keyProperty": "name"



}



]



}



}



]



}
```

Based on this metric definition, the following MBeans:

* `java.lang:type=MemoryPool,name=G1 Eden Space`
* `java.lang:type=MemoryPool,name=G1 Survivor Space`

will result in a single metric in Dynatrace with two dimensions:

* `java.lang.MemoryPoolUsage` with the dimension `memory_type=G1 Eden Space`
* `java.lang.MemoryPoolUsage` with the dimension `memory_type=G1 Survivor Space`

## Monitoring

Go to [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to analyze and chart your custom JMX metrics. If needed, you can pin your charts to a dashboard. In the following example, you can see the `java.lang.MemoryPoolUsage` metric split by the dimension `memory_type`:

![Data Explorer with z/OS JMX metrics](https://dt-cdn.net/images/data-explorer-1643-7696285fbf.png)

To get a list of metrics available in your monitoring environment, Go to **Metrics** to open the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."). In the following example, you can see the three metrics that we have created above:

![Metrics browser with z/OS JMX metrics](https://dt-cdn.net/images/metrics-browser-1636-1096adef93.png)

## Related topics

* [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.")
* [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")


---


## Source: zos-opentelemetry.md


---
title: Extend traces using OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry
scraped: 2026-02-17T04:53:22.664786
---

# Extend traces using OpenTelemetry

# Extend traces using OpenTelemetry

* Latest Dynatrace
* 7-min read
* Updated on Sep 23, 2022

[OpenTelemetryï»¿](https://dt-url.net/y903u4j) is a collection of tools, APIs, and SDKs that enable you to use telemetry data (distributed traces, metrics, and logs) to get insights into your application's performance and behavior.

OpenTelemetry with the z/OS Java code module enables you to enrich or extend distributed traces.

* Enrich distributed traces with project-specific additions (for example, you can add business-relevant data to your traces or capture developer-specific diagnostics).
* Extend distributed traces (for example, you can capture a Java Transport that is not supported out of the box by Dynatrace or fill observability gaps between applications to achieve transactional insights).

OpenTelemetry metrics and logs are currently not supported by the z/OS Java code module.

Licensing

* OpenTelemetry distributed traces captured by the z/OS Java code module are included in the mainframe license.

## OpenTelemetry interoperability

OpenTelemetry version 1.0+

Enabling OpenTelemetry interoperability connects the z/OS Java code module to the OpenTelemetry API. When enabled, the code module redirects certain OpenTelemetry API usage (for example, `GlobalOpenTelemetry`) to the internal Dynatrace OpenTelemetry SDK.

The z/OS Java code module forwards the captured [OpenTelemetry Spansï»¿](https://opentelemetry.io/docs/concepts/signals/traces/#spans-in-opentelemetry), via the [zDC subsystem](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.") and [zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring."), to your Dynatrace environment.

![z/OS Java OpenTelemetry](https://dt-cdn.net/images/zos-java-otel-1369-e7b35738b0.png)

Recommendation: avoid using the OpenTelemetry SDK in your applications together with the Dynatrace OpenTelemetry interoperability because it could result in conflicts.

### Enable OpenTelemetry interoperability

OpenTelemetry interoperability is disabled by default. To enable it, add the `OpenTelemetry: EnableIntegration` attribute to your `dtconfig.json` file as shown in the following example.

Typically, you've created the `dtconfig.json` file during the [z/OS Java code module installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Set up Java monitoring on z/OS using the Java module.") and have set the attributes `Tenant`, `ClusterID`, and `zdcName` to your environment.

```
{



"OpenTelemetry": {



"EnableIntegration": true



}



}
```

Alternatively, you can add the `open-telemetry-enable-integration` option to the JVM argument of the z/OS Java code module:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=open-telemetry-enable-integration=true
```

## OpenTelemetry instrumentation samples

To support various use cases, OpenTelemetry enables you to add vendor-neutral custom instrumentation to your applications. Instrumenting applications with OpenTelemetry requires programming knowledge and access to the applicationâs code. To learn how to instrument your application, refer to [OpenTelemetry documentationï»¿](https://dt-url.net/7603uf3) and [OpenTelemetry Java documentationï»¿](https://dt-url.net/n823ur4).

See the examples below for using [OpenTelemetry Javaï»¿](https://dt-url.net/yo43um9).

Enrich traces with project-specific additions

This example shows how you can capture an additional operation in a Java application running on a WebSphere Application Server monitored by Dynatrace.

1. Define a `Tracer`.

   ```
   import io.opentelemetry.api.GlobalOpenTelemetry;



   import io.opentelemetry.api.trace.Tracer;



   public final class RestaurantOpenTelemetry {



   public static Tracer getTracer() {



   return GlobalOpenTelemetry.getTracer("restaurant", "0.0.1");



   }



   }
   ```
2. Use the `Tracer` to capture an operation including some attributes.

   ```
   import io.opentelemetry.api.trace.Span;



   import io.opentelemetry.api.trace.SpanKind;



   import io.opentelemetry.context.Scope;



   public class MenuDao {



   public Order newOrder(String customer) {



   // OpenTelemetry: create a span and define it's scope



   Span span = RestaurantOpenTelemetry.getTracer().spanBuilder("MenuDao.newOrder")



   .setSpanKind(SpanKind.INTERNAL)



   .setAttribute("customer", customer)



   .startSpan();



   try (Scope scope = span.makeCurrent()) {



   // Your application code: create a new order



   Order order = new Order();



   order.setCustomer(customer);



   order.setStatus("pending");



   // OpenTelemetry: add order ID to the span



   span.setAttribute("newOrderId", order.getId());



   return order;



   } finally {



   // OpenTelemetry: close the span



   span.end();



   }



   }



   }
   ```

The `MenuDao.newOrder` operation is displayed as a span on the **Code level** tab in the Dynatrace web UI with the captured span attributes (`customer`, `newOrderId`) and measured execution time.

![z/OS OpenTelemetry code-level](https://dt-cdn.net/images/zos-opentelemetry-1-1926-e67ad2add3.png)

Extend end-to-end traces

This example shows how you can trace an audit service running on a WebSphere Application Server (monitored by Dynatrace) that uses a Java transport that is not supported out of the box. We use Java serialization (object output streams) as an example for such an unsupported Java transport.

To learn more about context propagation, refer to the official [OpenTelemetry Context Propagation documentationï»¿](https://dt-url.net/j503uhz).

**Service A** writes an audit entry to the `ObjectOutputStream`:

```
import io.opentelemetry.api.GlobalOpenTelemetry;



import io.opentelemetry.context.Context;



import io.opentelemetry.context.propagation.TextMapPropagator;



public class AuditService {



public static void sendAuditEntry(Order order) {



// Your application code: declare an audit entry



Map<String, String> auditEntry = new HashMap<>();



auditEntry.put("name", order.getId().toString());



auditEntry.put("description", order.getCustomer());



// OpenTelemetry: Inject current context of audit entry and propagate it



TextMapPropagator propagator = GlobalOpenTelemetry.getPropagators().getTextMapPropagator();



propagator.inject(



Context.current(),



auditEntry,



Map::put



);



// Your application code: write audit entry to objectOutputStream (Socket)



Socket socket = new Socket(host, port);



ObjectOutputStream objectOutputStream = new ObjectOutputStream(socket.getOutputStream())) {



objectOutputStream.writeObject(auditEntry);



}



}
```

**Service B** reads an audit entry from the `ObjectInputStream`:

```
import io.opentelemetry.api.GlobalOpenTelemetry;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.SpanKind;



import io.opentelemetry.context.Context;



import io.opentelemetry.context.Scope;



import io.opentelemetry.context.propagation.TextMapGetter;



public class AuditService {



private static void receivedAuditEntry(Map<String, String> auditEntry) {



// OpenTelemetry: declare the tracer, create a span and define it's scope



Span span = GlobalOpenTelemetry.getTracer("auditing-center", "0.0.1")



.spanBuilder("auditEntry")



.setSpanKind(SpanKind.SERVER)



.setAttribute("auditName", auditEntry.get("name"))



.startSpan();



try (Scope scope = span.makeCurrent()) {



// Your application code: process audit entry



// ...



}



span.end();



}



public static void readAuditEntryFromSocket(Socket socket) {



ObjectInputStream objectInputStream = new ObjectInputStream(socket.getInputStream());



Object input = objectInputStream.readObject();



// OpenTelemetry: extract context of audit entry



Context context = GlobalOpenTelemetry.getPropagators().getTextMapPropagator()



.extract(



Context.current(),



input,



new TextMapGetter<Map<String, String>>(){ /* ... */ });



try (Scope scope = context.makeCurrent()) {



receivedAuditEntry((Map<String, String>) input);



}



// ...



}



}
```

Dynatrace displays the full end-to-end trace as a distributed trace that contains the `auditEntry` as a service method which includes the captured attributes and measured execution time. The `auditEntry` service method is the result of the traced `receivedAuditEntry` method with its new span. The fact that it is displayed as a child of the `/orderReceived` service method is the result of the `inject` and `extract` calls of the `TextMapPropagator`.

![z/OS OpenTelemetry service](https://dt-cdn.net/images/zos-opentelemetry-2-1926-9f66be4562.png)

## Suppress spans from specific instrumentations

You can suppress spans coming from a particular instrumentation scope/library. To do so, add the library name to the `OpenTelemetry: DisabledSensors` parameter in name via the `dtconfig.json` file. You can use an asterisk (`*`) to exclude all instrumentation scope/library names starting with the preceding string. You can't use asterisk at the beginning or in the middle of a library name.

```
{



"OpenTelemetry": {



"EnableIntegration": true,



"DisabledSensors": [



"com.example.MyLib",



"opentelemetry.urllib3*"



]



}



}
```

Alternatively, you can add the `open-telemetry-disabled-sensors` option to the JVM argument of the z/OS Java code module:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=open-telemetry-disabled-sensors=com.example.MyLib:opentelemetry.urllib3*
```

If you specify exclusions in the command line, the exclusions in the `dtconfig.json` file ignored.

Use colon `:` as the separator for instrumentation scope/library names in the command line.

The examples above suppress spans from the `com.example.MyLib` instrumentation scope/library and spans from all libraries starting with the name `opentelemetry.urllib3`.

## Rules for spans that Dynatrace will report

Depending on the `SpanKind`, Dynatrace will suppress some OpenTelemetry spans:

* A span needs to either be of kind `SpanKind.SERVER` or `SpanKind.CONSUMER` or it needs to have another span (`SpanContext`) as a non-remote parent. Usually, this is handled by the Dynatrace Servlet sensor, which creates a `SERVER` span and sets it as the current, active span.
* Child spans of spans of kind `SpanKind.CLIENT` or `SpanKind.PRODUCER` will be suppressed. For example, after Dynatrace creates a span of kind `SpanKind.CLIENT` for a synchronous outgoing HTTP call, all spans created in the thread will be suppressed until the HTTP call, and thus the HTTP Span, is finished. You can of course create new spans in the called service which will be linked correctly.

Suppressed spans will not be visible in distributed traces.

## Define a request attribute for span attributes

You can define a [request attribute](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") for any captured span attribute. To do so

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select **Define a new request attribute** and enter the name and data type of your request attribute.
3. Select **Add new data source** and select `Span attribute` as the **Request attribute source**.
4. Enter your **Attribute key**.
5. Select **Save**.

To learn more details about span attributes and how to capture them, see [Span settings](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.").

![Use Span attribute as a request attribute](https://dt-cdn.net/images/screenshot-2022-09-30-at-09-24-35-1883-e2f2b63693.png)

You can find the **Attribute key** of your spans on the [Distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") page in the **Code level** tab under **Span attributes**.

![Span attributes](https://dt-cdn.net/images/span-attributes-1916-1967c4e21e.png)


---


## Source: ibm-mq-monitoring.md


---
title: Set up IBM MQ tracing on z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring
scraped: 2026-02-16T21:26:30.680876
---

# Set up IBM MQ tracing on z/OS

# Set up IBM MQ tracing on z/OS

* Latest Dynatrace
* 1-min read
* Updated on May 16, 2022

With Dynatrace you can get observability for IBM MQ on z/OS:

* The CICS, IMS, and z/OS Java modules can trace messages in your applications initiated by IBM MQ clients, including their producer and consumer services across tiers. To learn more about messages queues in Dynatrace, see [Queues](/docs/observe/infrastructure-observability/queues "Monitor and analyze your message queues with Dynatrace.").
* The ActiveGate extension can collect metrics from IBM MQ servers. To learn more about it, see [IBM MQ ActiveGate extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

## Tracing

Dynatrace can automatically create a continuous [service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") for IBM MQ when the producer and consumer services use the same queue or topic name. If the producer and consumer services refer to different queue or topic names, IBM MQ configuration might be required to create a continuous service flow.

Without IBM MQ configuration, Dynatrace can still trace all messages, but the service flow will be broken.

The table lists the available IBM MQ configuration items for queues and topics.

Item

Description

Your action

Queue manager

Queue manager with its queues

Define your queue managers, including alias queues, remote queues, and cluster queues within a single configuration item.

z/OS Queue sharing group

Group of queue managers that access the same shared queues

Specify which queue managers and shared queues belong to a queue-sharing group within a single configuration item.

z/OS IMS bridge

The IBM MQ component that allows direct access to the IMS system

Specify which queue managers and queues belong to an IMS bridge within a single configuration item.

## Manage IBM MQ configuration

You can manage an IBM MQ configuration automatically by installing an [IBM MQ extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") and activating **Retrieve topology for improved transaction tracing** to retrieve the IBM MQ configuration of your environment and send it to the Settings API. This can also be done manually via the web UI or the Settings API.

### Manual configuration via web UI

To manage the IBM MQ configuration via the Dynatrace web UI, go to **Settings** > **Mainframe** to find the following menu options:

* IBM MQ queue managers
* IBM MQ queue sharing groups
* IBM MQ IMS bridges

### Manual configuration via Settings API

You can manage the IBM MQ configuration via the Dynatrace [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

Settings API for IBM MQ tracing:

* [Create queue manager configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qm-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Update queue manager configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qm-api-update "Configure Dynatrace for IBM MQ tracing.")
* [Create queue sharing group configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qsg-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Update queue sharing group configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qsg-api-update "Configure Dynatrace for IBM MQ tracing.")
* [Create IMS bridge configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#ims-bridge-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Update IMS bridge configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#ims-bridge-api-update "Configure Dynatrace for IBM MQ tracing.")

## Related topics

* [IBM MQ tracing](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing "Configure Dynatrace for IBM MQ tracing.")


---


## Source: zos.md


---
title: Dynatrace for z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos
scraped: 2026-02-17T04:45:51.571616
---

# Dynatrace for z/OS

# Dynatrace for z/OS

* Latest Dynatrace
* 8-min read
* Updated on Nov 15, 2022

With Dynatrace, you can get complete transactional insights into your workloads from the mobile frontend down to mainframe programs and everything in between so that you can troubleshoot anomalies on the code level. Furthermore, Dynatrace can accompany you in your hybrid cloud journey with end-to-end observability from the mainframe to the cloud.

Learn how Dynatrace addresses the most typical mainframe challenges:

Is the mainframe part of the problem?

The AI-powered fault domain isolation pinpoints the root-cause of problems and assesses their user impact so that you can prioritize mitigation strategies and reduce the mean-time to repair.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-4-2556-d7363d4d4a.png)

All monitored LPARs, regions, and applications are contributing to this fault domain isolation.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-5-2556-eaa580abc1.png)

Who is calling the mainframe and how often?

Backtrace transactions using the [Service backtrace](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.") to understand your mainframe workloads and benefit from potential IBM discounts (see for example the IBM [mobileï»¿](https://www.ibm.com/common/ssi/ShowDoc.wss?docURL=/common/ssi/rep_ca/0/877/ENUSZP14-0280/index.html&lang=en&request_locale=en) and [public cloudï»¿](https://www.ibm.com/common/ssi/cgi-bin/ssialias?htmlfid=897/ENUS216-319&infotype=AN&subtype=CA) workload discounts to lower your monthly peak rolling 4-hour average MSU value).

The Service backtrace below shows how a CICS transaction interactions with both a mobile application and a web application. You can clearly see how often these applications call the CICS transaction, and also which of their requests failed.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-3-2554-c2353b4392.png)

What transactions are expensive or slow?

Analyze the performance of your transactions using via the [service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") to verify if they fulfill the defined SLOs with service-level metrics. The request count for example can indicate when a transaction is called too often from an open-system, which could result in additional costs.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-1-2558-21736786aa.png)

Use the [PurePath distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") code-level insights to optimize your programs.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-6-2072-233541ed1b.png)

Modernize programs on z/OS for hybrid cloud?

Use Dynatrace to ensure business continuity for traditional environments by monitoring middleware technologies like enterprise service buses or message queues. While transforming your mainframe programs to make them accessible for cloud functions with z/OS Connect EE, monitored by Dynatrace.

See the end-to-end trace from z/OS Connect EE down to an IMS DL/I database below.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-2-2557-a3531aae62.png)

## Set up monitoring

Dynatrace provides code modules for CICS, IMS, and z/OS Java technologies so that you can achieve seamless observability with trace and metric insights. To learn more about the supported technologies, see [Mainframe technology support](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.").

![z/OS monitoring architecture](https://dt-cdn.net/images/zos-architecture-1745-8d165d1510.png)

The CICS, IMS, and z/OS Java modules interact with the Dynatrace z/OS Data Collection (zDC) subsystem via a shared memory object (SMO) within an LPAR. The zDC subsystem manages this SMO, to which the modules write their monitoring data.

The zLocal, hosted in the z/OS [Unix System Servicesï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS) environment, runs as part of the zDC. It manages the TCP/IP connection to the zRemote module, reads monitoring data from SMO, and transfers these data to the zRemote.

The zRemote module processes monitoring data received from the zLocal and routes that data, compressed and encrypted, via its local ActiveGate to Dynatrace. Hence, the zRemote module offloads much of the processing work from the modules incurred in instrumenting subsystems and applications to an open system.

To get started, see [z/OS installation overview](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation "Installation overview of Dynatrace z/OS modules.").

## Licensing

Monitoring of the CICS, IMS, and z/OS Java modules are consumed based on million service units (MSUs).

Dynatrace Platform Subscription, see [Mainframe Monitoring](/docs/license/capabilities/app-infra-observability/mainframe "Learn how your consumption of the Dynatrace Mainframe Monitoring DPS capability is billed and charged.").

Dynatrace classic licensing, see [Mainframe Monitoring on IBM z/OS](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring#mainframe-msu "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## FAQ

Who needs to be involved in a typical Dynatrace for z/OS installation?

To find the procedure and the people involved people, see [z/OS installation overview](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation "Installation overview of Dynatrace z/OS modules.").

Can I use host groups to organize multiple LPARs?

Yes, you can organize multiple LPARs using host groups. For more information, see [Define host groups to organize multiple LPARs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote#host-groups "Customize the zRemote module for your needs.").

What does a volatile service mean and how can I solve related problems?

A **volatile CICS** or **volatile IMS** is created automatically by Dynatrace when the maximum number of service IDs that can be generated per region (process) is exceeded. To increase the limit of service IDs that can be generated, contact a Dynatrace product expert via live chat within your Dynatrace environment.

### CICS and IMS modules

How does the CICS and IMS modules instrumentation work?

The CICS module uses hooks to instrument CICS terminal and application owning regions, creating events of interest.

The IMS module uses the logging facility to instrument IMS control and message processing regions, creating events of interest from parsing binary logs.

Both modules use hooks to instrument IBM MQ, Db2, and DL/I.

No byte code instrumentation is used by the CICS and IMS modules.

### How much GCP time do the CICS and IMS modules consume while instrumenting applications?

The CICS and IMS consume some general-purpose central processor (GCP) time while instrumenting applications on IBM Z, but this overhead is typically very low (in the range of 1%-2%, depending on the type of monitored transactions). See the examples below.

| Industry of customer | Country | Code module | Measured in year | Measurement method | GCP time overhead |
| --- | --- | --- | --- | --- | --- |
| Financial (Bank) | Italy | CICS | 2023 | HIS profiling[1](#fn-1-1-def) | < 1.9 % |
| Financial (Bank) | Spain | CICS | 2020 | HIS profiling[1](#fn-1-1-def) | < 1.0 % |
| Insurance | Germany | CICS | 2020 | ran their own tests | < 1.0 % |
| Insurance | Germany | IMS | 2020 | HIS profiling[1](#fn-1-1-def) | < 1.0 % |
| Financial (Bank) | Germany | CICS | 2019 | ran their own tests | < 1.0 % |
| Insurance | Germany | IMS | 2017 | HIS profiling[1](#fn-1-1-def) | < 1.61 % |
| Insurance | Germany | IMS | 2017 | HIS profiling[1](#fn-1-1-def) | < 0.33 % |
| Financial (Bank) | Austria | CICS | 2015 | HIS profiling[1](#fn-1-1-def) | < 2.04 % |

1

Using the [Hardware Instrumentation Servicesï»¿](https://www.ibm.com/docs/en/zos/2.1.0?topic=aids-hardware-instrumentation-services) from IBM.

* The GCP time overhead numbers are calculated relatively to the address spaces in which the modules are running. When you compare the GCP time overhead relatively to the LPAR, then these numbers are even lower.
* For example, 2% GCP time overhead in CICS address spaces represents only 1% GCP time overhead per LPAR if the CICS workloads consume only 50% of the total GCP time on a given LPAR compared to other workloads (such as jobs and system tasks).

Can the CICS and IMS modules capture dynamic SQL statements?

No, the CICS and IMS modules can only capture static SQL statements.

### z/OS Java module

Can I monitor the Servants of my WebSphere Application Server with the z/OS Java module?

The WebSphere Application Server on z/OS allows you to spin up [Servantsï»¿](https://www.ibm.com/docs/en/was-zos/9.0.5?topic=zos-websphere-application-server-terminology) dynamically depending on the workload.

In Dynatrace, you can use the **process identifier** on each metric to distinguish between different Servants, as shown in the image below.

![Metrics process identifier](https://dt-cdn.net/images/was-process-id-1607-06f91781b9.png)

However, Servants can't be incorporated into the WebSphere Application Server process group detection because whenever you spin up a new Servant, a new process entity is created, and the current monitoring context is lost.

Which attributes are evaluated for WebSphere Application Server process group detection?

Dynatrace uses the following attributes to detect and create WebSphere Application Server process entities:

* Server name
* Node name
* Cell name

Dynatrace groups all process entities belonging to the same WebSphere Application Server cluster name into a process group.

Can I merge process groups created by the z/OS Java module into a single process group?

No, process groups created by the z/OS Java module can't be modified or merged.

As an alternative you can organize your process groups by [defining metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") or [defining tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") based on environmental variables. Both concepts apply to z/OS Java as well. Note that you can define environment variables only on the process level, not on the host level.

Can I tag processes created by the z/OS Java module?

Yes. You can tag processes created by the z/OS Java module by [defining metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") or [defining tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") based on environmental variables. Note that you can define environment variables only on the process level, not on the host level.

Can I define custom services using the z/OS Java module?

The z/OS Java module does not support custom services purely via configuration. Instead, you can create custom traces using the z/OS Java module's [OpenTelemetry interoperability](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry "Use OpenTelemetry to close observability gaps in your Java applications on z/OS.").

Can I use span attributes captured by the z/OS Java module as a request attribute?

Yes. To learn how to set up a request attribute for any captured span attribute, see [Define a request attribute for span attributes](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry#request-attribute "Use OpenTelemetry to close observability gaps in your Java applications on z/OS.").

## Linux on Z

With Dynatrace, you can get [Full-Stack Monitoring with Host monitoring (DPS)](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") for Linux on Z using [OneAgent on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more."). To learn more about the supported technologies on the s390 architecture, see [Technology support](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Related topics

* [[Blog] Eliminate inefficiencies and innovate faster on IBM Zï»¿](https://www.dynatrace.com/news/blog/eliminate-inefficiencies-and-innovate-faster-by-optimizing-hybrid-mainframe-environments-on-ibm-z/ "Eliminate inefficiencies and innovate faster by optimizing hybrid mainframe environments on IBM Z.")
* [[Blog] Transform z/OS Java applicationsï»¿](https://www.dynatrace.com/news/blog/transform-mainframe-applications-into-z-os-java-services-with-end-to-end-transaction-visibility-and-anomaly-detection-preview/ "Transform z/OS Java applications into microservices with end-to-end transaction visibility and anomaly detection.")
* [[Blog] Managing hybrid cloud infrastructureï»¿](https://www.dynatrace.com/news/blog/managing-hybrid-cloud-infrastructure-with-an-observability-platform/ "Managing a mainframe-powered hybrid cloud infrastructure with Dynatrace as an observability platform.")
* [[Video] Get insights for z/OS Connect apps with Dynatraceï»¿](https://www.youtube.com/watch?v=6WuHzvQV7yk "Learn how to modernize for hybrid cloud with the Dynatrace z/OS Connect end-to-end observability.")
* [[Video] Extend the Dynatrace value for z/OS ï»¿](https://www.youtube.com/watch?v=XUw7YmpBx4E "Learn how to capture additional monitoring data of your z/OS business applications using the CICS/IMS SDK.")


---


## Source: installation-and-operation.md


---
title: Install OneAgent on a server
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation
scraped: 2026-02-17T04:45:09.568972
---

# Install OneAgent on a server

# Install OneAgent on a server

* Latest Dynatrace
* 3-min read
* Updated on Jan 22, 2026

Follow this guide to install Dynatrace OneAgent for the very first time.

Once you've followed this guide, you'll have OneAgent installed onto a host and can use Dynatrace to monitor that host and its processes.

The information on this page is platform-agnostic.

For OS-specific information on OneAgent installation and advanced operation, select your OS for the detailed instructions.

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

## Prerequisites

This guide assumes that you have:

* A Dynatrace environment.
* Administrator access to a Linux, Windows, or AIX host (that doesn't have any existing OneAgent installations).
* A network that supports SSL communication.

## OneAgent setup

To download and install OneAgent on a host:

1. In **Dynatrace Hub**, select **OneAgent**.
2. Select **Set up** .
   The **Install OneAgent** window opens.
3. Enter or select the appropriate parameters (see the screenshot below for an example).

   * **OS type**

     Choose **Linux**, **Windows**, or **AIX** according to your host's OS.

   * **Architecture** (Linux only)
   * **Monitoring mode**
     Options are **Full-Stack**, **Infrastructure**, or **Discovery**.
     If you are using a free Dynatrace trial, select **Full-Stack** to see everything that Dynatrace is capable of observing.
     You can always change the monitoring mode after installation.
   * For **Optional parameters**, you might want to add a **Custom host name** for easier identification.
     The rest of the parameters are out of scope for this guide.

   ![OneAgent setup parameters](https://dt-cdn.net/images/screenshot-2025-02-05-at-15-06-49-2992-637e933241.png)
4. Select **Generate token** to generate an API token that lets your Dynatrace environment access OneAgent.
   Copy the token and save it somewhere safe, because you will not be able to access it again.
   You don't need to do anything else with this token right now.

5. Download OneAgent.
   Either use the provided CLI command or select  **Download**.
6. Verify the signature.
   Use the provided CLI command.
   (Note: Linux and AIX only.)
7. Install OneAgent.
   Either use the provided CLI command or run the executable by selecting it in the GUI.
   Follow the steps as described in the installer.

   If you install via the GUI, you should add the following options in the **Optional: advanced command-line settings** screen:
   `--set-monitoring-mode=fullstack --set-app-log-content-access=true`
8. When the installer shows a **Congratulations! Dynatrace OneAgent was successfully installed!** message, OneAgent is installed on the host.
   Select **Finish** to exit the installer.
9. Because OneAgent can't inject itself into running processes, you'll need to restart all processes that you want OneAgent to monitor.
10. To confirm that OneAgent is monitoring your host, open Dynatrace and go to **Infrastructure & Operations** > **Host**.
    If everything is working as expected, you'll see the name of your host in the **Hosts** table.
    See the screenshot below for an example.

    ![Infrastructure & Operations view of a newly added OneAgent on host](https://dt-cdn.net/images/screenshot-2025-02-04-at-13-32-36-2598-439524d1f9.png)

OneAgent is now set up and monitoring your host. See [Get started with Dynatrace](/docs/discover-dynatrace/get-started "Learn about Dynatrace monitoring capabilities, concepts, and deployment models and find out how to get started with SaaS and Managed deployments.") to continue your first journey with Dynatrace.

## Related topics

* [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")
* [Infrastructure & Operations](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")
* [Host-level settings](/docs/observe/infrastructure-observability/hosts/configuration "Host-level settings")
* [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.")


---


## Source: oa-requirements.md


---
title: OneAgent requirements
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oa-requirements
scraped: 2026-02-16T21:14:51.531833
---

# OneAgent requirements

# OneAgent requirements

* Latest Dynatrace
* 3-min read
* Updated on Jul 02, 2025

## OneAgent CPU requirements for the x86-64 architecture

This section outlines the CPU specifications to run Dynatrace OneAgent. Ensuring your system meets these requirements is essential for reliable and efficient operation.

### Minimum Supported Microarchitecture Level: **x86-64-v2**

The binary deliverables of the Dynatrace OneAgent rely on the support of the instructions included in the x86-64-v2 microarchitecture level[1](#fn-1-1-def).

1

The Dynatrace OneAgent version where this is enforced is will be announced in a future release.

#### Intel

Nehalem was the first Intel architecture to fully support the x86-64-v2 baseline. Please consult the [Intel product specificationï»¿](https://www.intel.com/content/www/us/en/products/overview.html) for further information.

**Example Intel CPUs:**

* **Intel Core i7-920** â Desktop (LGA 1366)
* **Intel Xeon X5550** â Server (LGA 1366)
* **Intel Core i5-750** â Mainstream desktop (LGA 1156)
* **Intel Xeon L5520** â Low-power server CPU

#### AMD

Bulldozer and its successors support the x86-64-v2 baseline. For some CPUs, support was added at a specific stepping. Please consult the [AMD product specificationï»¿](https://www.amd.com/en/products/specifications.html) for further information.

**Example AMD CPUs:**

* **AMD FX-4100** â Desktop (AM3+)
* **AMD Opteron 6200 Series** â Server (Socket G34)
* **AMD A8-3870K** â APU (FM1)
* **AMD FX-8350** â High-performance desktop (AM3+)

* **x86-64-v2** is a baseline that includes support for SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, and CMPXCHG16B instructions.
* Systems not meeting the x86-64-v2 baseline will not be able to run the Dynatrace OneAgent.
* Virtualized environments should ensure CPU feature passthrough is enabled to meet the microarchitecture requirements.

## OneAgent memory requirements

Deep monitoring an application with Dynatrace OneAgent implies an increase of per-application memory demand compared to execution without Dynatrace OneAgent. In addition to the memory required to load the OneAgent code module binary code into the application process, memory is also utilized to maintain monitored application state information, communication buffers, etc.

Memory demand isn't a constant number or proportion of application memory requirements, but depends on technology, monitoring configurations, application properties, and the executed load. See [About memory demand variance](#about-memory-demand-variance) below for further insights on memory demand.

### OneAgent code module memory requirement

As outlined above, monitoring memory demand depends on multiple factors. To facilitate straight forward resource planning, we recommend that you account for an additional **200MB** memory budget for monitored application processes. This number will suffice monitoring of a vast number of applications. Empirical observations show memory demand well below **100MB** for most applications.

The monitoring memory demand refers to resident set size (RSS) or equivalent quantification on non Linux operating systems. RSS is a key quantifier for applying memory limits to processes.

#### Cloud platform memory limits

Kubernetes and other cloud platforms feature definition of memory limits for workloads. The defined limits apply (roughly spoken) to RSS and workloads are automatically terminated once they exceed the defined memory limit.

As Dynatrace OneAgent code modules increase memory demand of monitored applications, memory limits must be adjusted accordingly.

### About memory demand variance

OneAgent code module deep monitoring memory demand can't be expressed exactly as a constant number or proportion of memory consumed by the application process. It's the sum of memory required for basic OneAgent code module operation (for example, communication buffers) and dynamic monitoring data gathered by OneAgent code modules. Dynamic monitoring data memory demand depends on configuration settings, application base technology, and the application itself.

#### Application dependent memory demand

Code level visibility and hotspot analysis mandate the recording of function execution time and frequency. Therefore, the number of functions in the application and their execution defines the number data items and ultimately the memory footprint needed to measure function performance. The same applies to distributed traces informationâthe memory demand for gathering distributed traces information depends on the number of concurrent requests processed by the application and the complexity (i.e., the length of the PurePath) of the executions triggered by these requests.

#### Configuration dependent memory demand

Custom service monitoring is an example for monitoring configuration dependent memory demand. The definition of a custom service increases base memory budget for selected function instrumentation and dynamical memory budget for the increased number of distributed traces data collected for custom service calls. In .NET technology, instrumentation of additional assemblies for the custom service can significantly increase startup memory demand (see below).

#### Technology dependent memory demand

OneAgent code modules are optimized to efficiently use memory and to free resources when they're no longer needed, to burden application execution as little as possible. So, memory demand might vary over application execution time.

Dependent on OneAgent code module, memory demand might peak at application startup. This is especially true for .NET technology. Preparing .NET assemblies for monitoring causes memory footprint to spike, as assembly code temporarily resides twice in memory. Once the injection process is completed, the .NET runtime retains both the original assemblies and the instrumented versions of the application logic in memory. This is a known issue of Microsoft .NET technology and can't be mitigated by the Dynatrace OneAgent.


---


## Source: oneagent-aging-mechanism.md


---
title: OneAgent file aging mechanism
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism
scraped: 2026-02-17T04:52:44.842058
---

# OneAgent file aging mechanism

# OneAgent file aging mechanism

* Latest Dynatrace
* 6-min read
* Updated on Sep 08, 2022

OneAgent in the installer-based deployment uses a built-in aging mechanism that makes sure the OneAgent files are kept within a reasonable size.

Aging mechanism is not used in the application-only mode.

Optimal OneAgent disk usage is determined based on the following limits:

* The minimum required space is 200 MB \* 3 = 600 MB (logs, alerts, crash reports).
* The default required space is 1 GB \* 3 = 3 GB (logs, alerts, crash reports).

The two type of files that contribute most to OneAgent disk space usage during its operation are OneAgent log files and runtime data such as crash and memory dumps.

## Log files

The maximum disk space occupied by OneAgent log files is very well managed by the OneAgent aging mechanism. Logs grow in size slowly and steadily. A continuous cleanup process that runs every minute keeps the log size within reasonable constraints. We designed the log aging mechanism with inside knowledge on how OneAgent-related events are logged, so log file aging doesn't require additional configuration.

## Runtime data

Unlike log files, large runtime data files such as crash and memory dumps are generated ad hoc and can cause rapid spikes in disk usage. To mitigate this, use the `DATA_STORAGE` installation parameter to specify a custom directory for large runtime data. Locate the custom directory on a resource where tight disk size constraints are not as critical as they are on the disk where OneAgent is installed.

For more information on customizing OneAgent installation, see the OS-specific help: [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#data-storage "Learn how you can use AIX installer with command line parameters.").

## Emergency cleanup

In an emergency situation, when free disk space reaches `3%` threshold, OneAgent cleans all the files from directories managed by the aging mechanism except the latest installer logs and OneAgent OS module log

## OneAgent aging mechanism rules

The OneAgent aging mechanism ensures that the disk space used by OneAgent is constantly within predefined limits. To do that, a number of rules are applied to OneAgent directories. If necessary, you can contact a Dynatrace product expert via live chat to modify some of the aging rules.

### Log directory

* Linux/AIX `/var/log/dynatrace/oneagent`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\log`

The file aging mechanism checks the files and subdirectories in the main log directory and removes the oldest files when:

* The total directory size is above 1 GB
* Any file in this directory is older than 14 days

There are additional rules for subdirectories:

* `{log-dir}/process`  
  Files are removed when any of these conditions are true:

  + The files in this directory use more than 300 MB in total
  + Any file in this directory is older than 14 days
  + This directory contains more than 1000 files (newest files are preserved; oldest files are removed)
* `{log-dir}/installer`  
  Files are removed when any of these conditions are true:

  + The files in this directory use more than 30 MB in total
  + Any file in this directory is older than 180 days
    On Windows, the `driver.log` file is preserved.
* `{log-dir}/dumpproc`  
  Files are removed when any of these conditions are true:

  + The files in this directory use more than 100 MB in total
  + Any file in this directory is older than 14 days
  + This directory contains more than 1000 files (newest files are preserved; oldest files are removed)

### Data storage directory

* Linux/AIX `/var/lib/dynatrace/oneagent/datastorage`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\datastorage`
* `{data_storage_dir}/supportalerts`  
  Files are removed when any of these conditions are true:

  + This directory contains more than 10 files
  + The files in this directory use more than 1 GB in total
  + Any of the files in this directory is older than 7 days
* `{data_storage_dir}/memorydump`  
  Files are removed when any of these conditions are true:

  + Any of the files in this directory is older than 2 hours
  + The files in this directory use more than 20 GB in total
* `{data_storage_dir}/crashreports`  
  Files are removed when any of these conditions are true:

  + They have already been reported to Dynatrace
  + This directory contains more than 100 files
  + The files in this directory use more than 1 GB in total
  + Any of the files in this directory is older than 3 days

### Runtime directory

* Linux/AIX `/var/lib/dynatrace/oneagent/agent/runtime`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime`

The OneAgent file aging mechanism checks the subdirectories starting with `0x`. Checks are performed recursively.

* If the `0x*` directory contains a dump subdirectory and all the files in it are older than 3 days, then the dump subdirectory is removed.
* If all the files and directories in the `0x*` directory are older than 7 days, the whole directory is removed.
* This directory is also fully cleaned up during OneAgent update.

### Installation bin directory

* Linux/AIX `/opt/dynatrace/oneagent/bin`
* Windows `%PROGRAMFILES%\dynatrace\oneagent\bin`
* `{install-dir}/bin`  
  OneAgent deploys a number of file artifacts during the update process, specifically in cases of injectable technology modules. All injectable module files are stored in versioned folders. When OneAgent is active, it performs file cleanup according to the following criteria:

  + The currently used version is always preserved.
  + OneAgent scans all the monitored processes and determines which libraries are used.
  + The library list is compared to the contents of the bin directory. Unused binaries from the 32-bit and 64-bit directories are removed, regardless of whether Host monitoring is enabled or disabled. For binaries in the `any` directory, cleanup occurs only if Host monitoring is enabled. The OneAgent aging mechanism retains the current version and the 10 most recent previous versions, keeping a total of 11 versions.

## Aging mechanism for OneAgent in application-only monitoring mode

If you don't have access to the infrastructure layer, Dynatrace also provides the option of application-only monitoring for [Kubernetes](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), [OpenShift](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), [CloudFoundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") or [SAP Business Technology Platform](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Install OneAgent on SAP Business Technology Platform.").

The aging mechanism in application-only monitoring mode manages the logs of the OneAgent modules. All of them are located in the respective subdirectories of the default OneAgent log directory:

* Linux/AIX `/var/log/dynatrace/oneagent`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\log`

### Log rotation

Each OneAgent module limits its number of logs to 5. Each of these 5 files is limited to 10 MB.

### Log aging

OneAgent purges the log files at startup when:

* A log file is older than 14 days
* The combined size of all log files exceeds 300 MB
* There are more than 1,000 log files

To prevent unnecessary delays in your application's startup, the OneAgent bulk purge limit is set to delete a maximum of 50 of the oldest files.


---


## Source: configuration.md


---
title: Enable the OpenTelemetry Span Sensor for OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration
scraped: 2026-02-17T05:08:45.550402
---

# Enable the OpenTelemetry Span Sensor for OneAgent

# Enable the OpenTelemetry Span Sensor for OneAgent

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Feb 09, 2026

In addition to the application-side configuration, several Dynatrace-specific settings let you control how OpenTelemetry data is used in Dynatrace.

To learn how to send OpenTelemetry data to a Dynatrace OneAgent, see [Use OneAgent with OpenTelemetry data](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.").

## Prerequisites

Java

Go

Node.js

PHP

.NET and .NET Core

.NET Framework

Python

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-framework-1-def), 1.4 - 1.54[1](#fn-monitoring-framework-1-def) |
| [OpenTracingï»¿](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

To enable OpenTelemetry Java

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (Java)**.

Existing tracers are replaced and will no longer work after you enable OpenTelemetry Java.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7, 1.8 - 1.11.0, 1.11.1 - 1.27, 1.28 - 1.39 |

Opt-in

To enable OpenTelemetry Go

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (Go) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for Go support.

OneAgent version 1.217 and earlier The OpenTelemetry Go Sensor propagates Dynatrace context across processes only if **Send W3C Trace Context HTTP headers** is enabled:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Turn on **Send W3C trace context HTTP headers**.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://www.npmjs.com/package/@opentelemetry/api) | 1[1](#fn-monitoring-framework-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

Opt-in

To enable OpenTelemetry Node.js:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

1. Find and enable **OpenTelemetry (Node.js) [Opt-In]**.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

Opt-in

To enable OpenTelemetry PHP:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (PHP) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for PHP support.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

To enable OpenTelemetry .NET and .NET Core:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (.NET) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for .NET support.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

To enable OpenTelemetry .NET Framework:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (.NET) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for .NET support.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-python) | 1.1+ |

Opt-in

To enable OpenTelemetry Python:

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Find and enable **OpenTelemetry (Python) [Opt-In]**.

Existing tracers are not affected by OneAgent OpenTelemetry for Python support.

## Attribute redaction

The OneAgent code module's OpenTelemetry Span Sensor automatically captures all OpenTelemetry attributes.
If you want to prevent the accidental storage of personal data, you can exclude specific attribute keys for which the values must not be persisted.
By omitting attributes containing personal data, you can meet your organization's privacy requirements and control the scope of stored monitoring data.

To configure attribute storage and masking settings for your environment

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Select **Server-side service monitoring** > **Attribute capturing**.
3. optional To change the default OpenTelemetry attribute persistence, go to **Preferences**.

   * To store all attributes except the ones in the **Blocked attributes** list, select **Allow all attributes**
   * To block all attributes except the ones in the **Allowed attributes** list, select **Block all attributes**

   Only one setting preference is possible.
4. Add an attribute name to the attribute list.

   1. On the **Attribute capturing** page, select **Blocked attributes** or **Allowed attributes**.

      Allowed attributes list Dynatrace recommends a few basic attributes to generally be included, such as `service.name` or `service.version`. For ease of use, Dynatrace comes with a default configuration that can be adjusted.
   2. Select **Add item** to add a new key to the attribute list and enter the key.
   3. Select **Save changes**.
5. Perform the following actions to mask a stored attribute value.

   1. On the **Attribute capturing** page, select **Attribute data masking**.
   2. Select **Add item** to add a new key to the masked attributed list.
   3. Enter a stored value key and select an option from the **Masking** dropdown list. To learn more about masking options, see [OpenTelemetry traces](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#otel-traces "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").
   4. Select **Save changes**.

You can then find the attribute key on the **Distributed traces** page on the [**Summary** tab](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#summary-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

## Trace search limitations

### Resource attributes

Searching by resource attribute is limited to the service name: filter by `Service name` on the **Distributed traces** page.

### Span attributes

Searching by span attribute is limited to the span name: filter by `Request` on the **Distributed traces** page.

## How the Span Sensor works

For more information about the OneAgent code module's OpenTelemetry Span Sensor, see [Detect OpenTelemetry spans using the OneAgent code module's OpenTelemetry Span Sensor](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#oneagent-otel-span-sensor "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.").

### Entry points

To avoid possible conflicts with existing PurePath distributed traces, OneAgent ingests by default only spans with a [span kindï»¿](https://opentelemetry.io/docs/concepts/signals/traces/#span-kind) of `Server` or `Consumer`. This usually is not an issue, as instrumentation libraries typically configure the appropriate span kind, however something to take into account if your application fully uses manual instrumentation.

This behavior can be customized with an [entry point rule](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings#span-entry-points "Learn how to configure span settings for OpenTelemetry and OpenTracing."). To do that, in Dynatrace go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **OpenTelemetry** > **Span entry points** and create a new rule with the appropriate action and matcher entry.

### Span hierarchy

Depending on your setup, you may experience "flat span enrichment". This is when spans are displayed in Dynatrace as a flat list instead of a tree hierarchy. While this generally is the default behavior with OneAgent ingestion of OpenTelemetry traces, the hierarchy may still reflect actual span relations as defined by the instrumentation, depending on the involved OneAgent code modules and their support for the instrumented technologies.

Leaf spans

When merging OpenTelemetry spans into OneAgent sensor traces, make sure that OpenTelemetry spans are leaf spans and not in-between OneAgent spans.

### Attribute capturing

As OneAgent ingests spans already [upon their creation](#point-of-ingestion), not all eventual attributes may be already present at the initial ingest. Any attributes added at a later point are highlighted in Dynatrace with an `initial value not set` note and cannot be used for span capture rules, as they were not yet available when the rules were being evaluated.

### Context propagation

When ingesting OpenTelemetry traces automatically with the OneAgent Span Sensor, there is a difference between the context propagation of OpenTelemetry traces and OneAgent traces.

While propagation of OpenTelemetry traces may be already handled properly by your application, it is also important to consolidate them with the OneAgent-specific trace. This can be achieved with a [context propagation rule](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings#span-context-propagation "Learn how to configure span settings for OpenTelemetry and OpenTracing."). To configure this, in Dynatrace go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **OpenTelemetry** > **Span context propagation** and create a context propagation rule with a `Propagate` action and a matcher entry for the span in question (for example, based on the span name or instrumentation library).

Try to avoid trace consolidation for technologies already covered natively by OneAgent sensors. Merging such OpenTelemetry spans into a OneAgent trace may lead to undefined states.

## Export to third-party backends while using OneAgent

While OpenTelemetry traces are always exported to other backends as is, a small data adjustment takes place when your OneAgent-instrumented application starts a fresh OpenTelemetry trace. This applies only to new traces and not when a trace is continued via context propagation.

In that case, OneAgent may have already created a new trace object when OpenTelemetry was initialized. If these two traces (with separate IDs) are not reconciled, telemetry data might be duplicated or fragmented. To mitigate this and still keep Dynatrace PurePath traces consistent, OneAgent uses the following approach:

* The OpenTelemetry trace ID takes precedence in exports to third parties
* On the Dynatrace backend, the PurePath trace ID is assigned instead

To enable correlation between these two IDs, Dynatrace creates additional [span linksï»¿](https://opentelemetry.io/docs/specs/otel/overview/#links-between-spans) for each span, linking to the OpenTelemetry trace.

The ID rewrite applies only to newly started traces (not context propagation) and to the OpenTelemetry SDKs for Go, Java, JavaScript, PHP, and Python but not to .NET.

## Limitations

### Java

* OneAgent version 1.294 and earlier OneAgent replaces installed global OpenTelemetry SDK components `TracerProvider`, `Propagator`, and `ContextManager`.
  Therefore, with OpenTelemetry Java enabled, traces are no longer seen by this SDK or exported to backends like Jaeger.
* OneAgent version 1.259+ To avoid duplicates, OneAgent [ignores spans from some automatic instrumentation libraries](#java-span-dropping).
* When OneAgent and OpenTelemetry sensors are both present for the same technology, you may experience additional overhead.

### Go

* OneAgent can only instrument Tracer implementation of the default OpenTelemetry SDK.
* When both OneAgent and OpenTelemetry sensors are present for the same technology, you may experience the following limitations:

  + Duplicate nodes in distributed traces
  + Additional overhead

### Node.js

* OneAgent version 1.331+ To avoid duplicates, OneAgent [ignores spans from some automatic instrumentation libraries](#nodejs-span-dropping).
* OneAgent version 1.329 and earlier When OneAgent and OpenTelemetry instrument the same module (such as HTTP or GRPC), you may experience the following limitations:

  + Duplicate nodes in distributed traces
  + Disconnected distributed traces
  + Additional overhead
* OneAgent version 1.261 and earlier OneAgent replaces installed global OpenTelemetry SDK components `TracerProvider`, `Propagator`, and `ContextManager`.
  Therefore, with OpenTelemetry Node.js enabled, traces are no longer seen by this SDK or exported to backends like Jaeger.

### PHP

* OneAgent version 1.313+ To avoid duplicates, OneAgent [ignores spans from some automatic instrumentation libraries](#php-span-dropping).

### Python

* When both OneAgent and OpenTelemetry sensors are present for the same technology, you may experience the following limitations:

  + Duplicate nodes in distributed traces
  + Disconnected distributed traces
  + Additional overhead

### All languages

* OneAgent captures OpenTelemetry resource attributes only if they are provided via the `OTEL_SERVICE_NAME` and `OTEL_RESOURCE_ATTRIBUTES` environment variables. When using the OpenTelemetry trace ingest API, this limitation doesn't apply.
* You can't create [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") (commonly used for trace searching and filtering) based on OpenTelemetry resource attributes.
* OneAgent truncates attribute values exceeding 4,096 characters.

## Prevention of span duplication in Java

OneAgent version 1.259+

To avoid possible span duplicates for areas covered by OpenTelemetry and OneAgent, OneAgent skips spans from the following automatic instrumentation Java libraries if OneAgent is configured to instrument your Java application and ingest OpenTelemetry spans.

Such spans are skipped only by OneAgent. Exports to third parties (for example, other backends or the Collector) remain unaffected.

io.opentelemetry.akka-http-10.0

io.opentelemetry.apache-dbcp-2.0

io.opentelemetry.apache-httpasyncclient-4.1

io.opentelemetry.apache-httpclient-2.0

io.opentelemetry.apache-httpclient-4.0

io.opentelemetry.apache-httpclient-4.3

io.opentelemetry.apache-httpclient-5.0

io.opentelemetry.async-http-client-1.9

io.opentelemetry.async-http-client-2.0

io.opentelemetry.c3p0-0.9

io.opentelemetry.cassandra-3.0

io.opentelemetry.cassandra-4.0

io.opentelemetry.cassandra-4.4

io.opentelemetry.cxf-jaxrs-3.2

io.opentelemetry.google-http-client-1.19

io.opentelemetry.grpc-1.6

io.opentelemetry.http-url-connection

io.opentelemetry.java-http-client

io.opentelemetry.jaxrs-1.0

io.opentelemetry.jaxrs-1.0-common

io.opentelemetry.jaxrs-2.0-annotations

io.opentelemetry.jaxrs-2.0-common

io.opentelemetry.jaxrs-2.0-cxf-3.2

io.opentelemetry.jaxrs-2.0-jersey-2.0

io.opentelemetry.jaxrs-2.0-resteasy-3.0

io.opentelemetry.jaxrs-2.0-resteasy-3.1

io.opentelemetry.jaxrs-3.0-annotations

io.opentelemetry.jaxrs-3.0-jersey-3.0

io.opentelemetry.jaxrs-3.0-resteasy-6.0

io.opentelemetry.jaxrs-annotations-2.0

io.opentelemetry.jaxrs-annotations-3.0

io.opentelemetry.jaxrs-client-1.1

io.opentelemetry.jaxrs-client-2.0

io.opentelemetry.jaxrs-client-2.0-resteasy-3.0

io.opentelemetry.jaxws-2.0

io.opentelemetry.jaxws-2.0-axis2-1.6

io.opentelemetry.jaxws-2.0-cxf-3.0

io.opentelemetry.jaxws-2.0-metro-2.2

io.opentelemetry.jaxws-cxf-3.0

io.opentelemetry.jaxws-common

io.opentelemetry.jaxws-jws-api-1.1

io.opentelemetry.jdbc

io.opentelemetry.jedis-1.4

io.opentelemetry.jedis-3.0

io.opentelemetry.jedis-4.0

io.opentelemetry.jersey-2.0

io.opentelemetry.jetty-11.0

io.opentelemetry.jetty-8.0

io.opentelemetry.jetty-httpclient-9.2

io.opentelemetry.jms-1.1

io.opentelemetry.jms-3.0

io.opentelemetry.jsp-2.3

io.opentelemetry.kafka-clients

io.opentelemetry.kafka-clients-0.11

io.opentelemetry.kafka-clients-2.6

io.opentelemetry.kafka-streams-0.11

io.opentelemetry.lettuce-5.1

io.opentelemetry.liberty

io.opentelemetry.liberty-20.0

io.opentelemetry.mongo-3.1

io.opentelemetry.netty-3.8

io.opentelemetry.netty-4.0

io.opentelemetry.netty-4.1

io.opentelemetry.okhttp-2.2

io.opentelemetry.okhttp-3.0

io.opentelemetry.orcale-ucp-11.2 ([sic!ï»¿](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/4fd52c5a7c73e8186a575cd08a20c55ccb8a0419/instrumentation/oracle-ucp-11.2/library/src/main/java/io/opentelemetry/instrumentation/oracleucp/v11_2/ConnectionPoolMetrics.java#L18))

io.opentelemetry.rabbitmq-2.7

io.opentelemetry.reactor-kafka-1.0

io.opentelemetry.reactor-netty-1.0

io.opentelemetry.resteasy-3.0

io.opentelemetry.resteasy-3.1

io.opentelemetry.resteasy-6.0

io.opentelemetry.rmi

io.opentelemetry.servlet-2.2

io.opentelemetry.servlet-3.0

io.opentelemetry.servlet-5.0

io.opentelemetry.servlet-javax-common

io.opentelemetry.spring-jms-2.0

io.opentelemetry.spring-jms-6.0

io.opentelemetry.spring-kafka-2.7

io.opentelemetry.spring-rabbit-1.0

io.opentelemetry.spring-rmi-4.0

io.opentelemetry.spring-webflux-5.0

io.opentelemetry.spring-webflux-5.3

io.opentelemetry.spring-ws-2.0

io.opentelemetry.tomcat-10.0

io.opentelemetry.tomcat-7.0

io.opentelemetry.tomcat-jdbc

io.opentelemetry.undertow-1.4

io.opentelemetry.vibur-dbcp-11.0

## Prevention of span duplication in Node.js

OneAgent version 1.331+

To avoid possible span duplicates for areas covered by OpenTelemetry and OneAgent, OneAgent skips spans from the following automatic instrumentation Node.js libraries if OneAgent is configured to instrument your Node.js application and ingest OpenTelemetry spans.

Such spans are skipped only by OneAgent. Exports to third parties (for example, other backends or the Collector) remain unaffected.

@opentelemetry/instrumentation-http

@opentelemetry/instrumentation-undici

@opentelemetry/instrumentation-aws-sdk

@opentelemetry/instrumentation-aws-lambda

@opentelemetry/instrumentation-connect

@opentelemetry/instrumentation-graphql

@opentelemetry/instrumentation-grpc

@opentelemetry/instrumentation-ioredis

@opentelemetry/instrumentation-redis

@opentelemetry/instrumentation-kafkajs

@opentelemetry/instrumentation-memcached

@opentelemetry/instrumentation-mongodb

@opentelemetry/instrumentation-tedious

@opentelemetry/instrumentation-mysql

@opentelemetry/instrumentation-mysql2

@opentelemetry/instrumentation-oracledb

@opentelemetry/instrumentation-pg

@opentelemetry/instrumentation-amqplib

## Prevention of span duplication in PHP

OneAgent version 1.313+

To avoid possible span duplicates for areas covered by OpenTelemetry and OneAgent, OneAgent skips spans from the following automatic instrumentation PHP libraries if OneAgent is configured to instrument your PHP application and ingest OpenTelemetry spans.

Such spans are skipped only by OneAgent. Exports to third parties (for example, other backends or the Collector) remain unaffected.

io.opentelemetry.contrib.php.curl

io.opentelemetry.contrib.php.laravel

io.opentelemetry.contrib.php.mongodb

io.opentelemetry.contrib.php.mysqli

io.opentelemetry.contrib.php.pdo

io.opentelemetry.contrib.php.slim

io.opentelemetry.contrib.php.symfony

io.opentelemetry.contrib.php.wordpress


---


## Source: oneagent-otel.md


---
title: Use OneAgent with OpenTelemetry data
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel
scraped: 2026-02-16T21:13:25.053290
---

# Use OneAgent with OpenTelemetry data

# Use OneAgent with OpenTelemetry data

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Sep 30, 2025

There are two ways to use OneAgent with OpenTelemetry:

* Send OpenTelemetry traces to the [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").
* Detect OpenTelemetry spans from trace data, using the OneAgent code module's OpenTelemetry Span Sensor.

![OneAgent send data to Dynatrace](https://dt-cdn.net/images/screenshot-2025-09-30-at-12-44-35-2430-bc1bd03d62.png)

For most use cases, Dynatrace recommends exporting OTLP directly to Dynatrace without deploying a OneAgent.

## Send OpenTelemetry traces to the OTLP endpoint exposed by OneAgent

Dynatrace OneAgent offers a local-only OTLP endpoint for traces.
This is shown in the figure above, where the application uses the local-only OTLP endpoint.

* Local-only means OneAgent provides the endpoint exclusively at `127.0.0.1` (localhost).
* Traces-only means OneAgent only accepts tracing information, not metrics or logs.

Content encoding support

OneAgent does not support content compression using the HTTP header [`Content-Encoding`ï»¿](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Encoding) yet. Pay particular attention to that when [instrumenting a Ruby application](/docs/ingest-from/opentelemetry/walkthroughs/ruby "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.") as the OpenTelemetry SDK for Ruby uses by default `Content-Encoding: gzip`.

If you need to use content compression, please export to SaaS, the Collector, or ActiveGate.

To send traces to OneAgent, you first need to enable the **Extension Execution Controller**. You can do this globally for the whole environment, for host groups, or only for specific hosts.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

With the EEC enabled, the OneAgent installations on the respective hosts will start accepting OTLP traces on URL `http://localhost:14499/otlp/v1/traces`.

OneAgent uses the TCP port 14499 as default port for this endpoint. You can change the port with [`oneagentctl`](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api#communication-port "Use the Dynatrace API to retrieve the metrics of monitored entities.").

EEC unavailable on container setups

The EEC ingestion endpoint is only available with [Full-Stack and Infrastructure Monitoring](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") deployments. It is **not** available with [containerized setups](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"). Please use [ActiveGate](#export-to-saas-and-activegate) as export endpoint for container applications.

### Export details

Calls to these API endpoints need to adhere to the following protocol details:

* Use of HTTPâgRPC is not yet supported
* Use of the binary format of Protocol BuffersâJSON is not yet supported
* Does not support content compression using the `Content-Encoding` header

### Authentication

Because it's a local-only endpoint, OneAgent does not require authentication.

### Network requirements

* Make sure there are no local restrictions for the used TCP port (default: 14499)

  Because the OTLP communication is exclusively local, there should not be much network configuration to consider unless you have restricted local network communication, in which case you need to make sure there are no local restrictions on the used TCP port (default: 14499).

## Detect OpenTelemetry spans using the OneAgent code module's OpenTelemetry Span Sensor

The OneAgent code module includes an OpenTelemetry Span Sensor which can create new spans based on OpenTelemetry API calls.
This is shown in the figure above, where the code module (with the OpenTelemetry Span Sensor) sends data via the OpenTelemetry protocol.

Use this approach

* For services that are already instrumented by OneAgent automatically.
* To extend visibility into frameworks and libraries instrumented with OpenTelemetry.
* To customize the distributed traces.

This feature is for advanced users only, who want to create custom spans using OpenTelemetry API calls.

The feature described on this page provides the same functionality as the OneAgent SDK for span detection, but uses OpenTelemetry instead.

If you enable this feature while also exporting OTLP data, you will create duplicate spans.

OpenTelemetry span data can be captured for Java, Go, Node.js, PHP, and .NET, on all platforms supported by OneAgent.
For setup and configuration of the OneAgent Span Sensor, see [Enable the OpenTelemetry Span Sensor for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

When the OneAgent OpenTelemetry Span Sensor is enabled, API calls like this example are automatically detected and included in the trace waterfall view.
Since OneAgent captures these spans automatically, exporting them to an OTLP endpoint will create duplicate traces.

The following example shows what OneAgent would detect and stitch into the OneAgent trace without the complexity of manual propagation.

```
GET /calculate-price/ABC123  # OneAgent



âââ SELECT FROM products     # OneAgent



âââ calculate-discount       # OpenTelemetry



â   âââ seasonal-rules       # OpenTelemetry



â   âââ loyalty-calculation  # OpenTelemetry



âââ INSERT INTO prices       # OneAgent
```

These auto-instrumented spans are woven together with your manual OpenTelemetry spans into a single trace.

```
@RestController



public class PricingController {



private static final Tracer tracer = GlobalOpenTelemetry.getTracer("pricing-service");



@GetMapping("/calculate-price/{productId}")



public PriceResponse calculatePrice(@PathVariable String productId) {



Product product = productRepository.findById(productId);



Span calcSpan = tracer.spanBuilder("calculate-discount")



.setAttribute("product.category", product.getCategory())



.startSpan();



double discount;



try (Scope scope = calcSpan.makeCurrent()) {



discount = applySeasonalRules(product);



discount += applyCustomerLoyalty(product);



} finally {



calcSpan.end();



}



return priceRepository.save(new PriceResponse(product, discount));



}



private double applySeasonalRules(Product product) {



Span span = tracer.spanBuilder("seasonal-rules")



.setAttribute("season", "winter-sale")



.startSpan();



try (Scope scope = span.makeCurrent()) {



return calculateSeasonalDiscount();



} finally {



span.end();



}



}



private double applyCustomerLoyalty(Product product) {



Span span = tracer.spanBuilder("loyalty-calculation").startSpan();



try (Scope scope = span.makeCurrent()) {



return calculateLoyaltyDiscount();



} finally {



span.end();



}



}



}
```


---


## Source: oneagent-configuration-via-command-line-interface.md


---
title: OneAgent configuration via command-line interface
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface
scraped: 2026-02-06T16:30:55.688261
---

# OneAgent configuration via command-line interface

# OneAgent configuration via command-line interface

* Latest Dynatrace
* Reference
* 20-min read
* Updated on Sep 17, 2025

Use the `oneagentctl` command-line interface to perform some post-installation OneAgent configuration at the individual host level.

## Location

The tool location depends on whether you customized the OneAgent installation using the `<INSTALL_PATH>` parameter:

* **Linux** or **AIX**:  
  `<INSTALL_PATH>/agent/tools`, by default `/opt/dynatrace/oneagent/agent/tools`  
  You need root privileges.
* **Docker-based deployment**  
  `<INSTALL_PATH>/agent/tools`, by default `/opt/dynatrace/oneagent/agent/tools`  
  Note that this path will differ for a volume-based deployment.
* **Windows**:  
  `<INSTALL_PATH>\agent\tools`, by default `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`  
  You need administrator privileges. If you try to run `oneagentctl` in a non-admin Windows console, Windows will display a User Account Control pop-up and fail.

## Parameter types

The `oneagentctl` command accepts the `get` parameter to check the state or value of a setting, and the `set` parameter to change a setting. Note that you can use multiple `set` parameters in a single command.

## OneAgent restart

When you use the `set` parameters, you need to restart OneAgent service to apply changes. You can use the `--restart-service` parameter with the command that triggers the restart automatically. In some cases you'll also need to restart monitored applications. You can also use the restart parameter on its own, without other parameters. See an example command below.

* **Linux** or **AIX**:  
  `./oneagentctl --set-proxy=my-proxy.com --restart-service`
* **Windows**:  
  `.\oneagentctl.exe --set-proxy=my-proxy.com --restart-service`

## Display help

Use the `--help` parameter to display all supported parameters.

* **Linux** or **AIX**:  
  `./oneagentctl --help`
* **Windows**:  
  `.\oneagentctl.exe --help`

## Display OneAgent version

Use the `--version` parameter to display the OneAgent version.

* **Linux** or **AIX**:  
  `./oneagentctl --version`
* **Windows**:  
  `.\oneagentctl.exe --version`

## OneAgent communication

### Set OneAgent communication settings

Use the `--set-server` parameter to set a OneAgent communication endpoint. Use the IP address or name, combined with the `/communication` suffix. Depending on your deployment, it can be a Dynatrace Server, Dynatrace Managed Cluster, or ActiveGate.

Run the following command to adjust OneAgent connection settings:

* **Linux** or **AIX**:  
  `./oneagentctl --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`
* **Windows**:  
  `.\oneagentctl.exe --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`

To define multiple endpoints, separate them by semicolon and add the quotes. For example, `--set-server="https://server1;https://server2"`.

These parameters require restart of OneAgent, as well as restart of all the applications monitored with deep code modules. Add [`--restart-service`](#oneagent-restart) to the command to restart OneAgent automatically (version 1.189+) or stop and start OneAgent process manually. For OS-specific instructions, see [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

This command will immediately change the OS module connection endpoint, but the code modules won't be able to read the new setting until the next restart.

OneAgent and Dynatrace Cluster automatically maintain a working connection. If an endpoint detail changes, the cluster notifies OneAgent of the change and OneAgent automatically updates the endpoint you set using the `--set-server` to the new working value.

Directing OneAgent traffic through ActiveGate

Routing OneAgent traffic through an ActiveGate can enhance the security of your data by ensuring it remains within controlled network paths and is encrypted during transmission.

1. Determine the IP address or hostname of the ActiveGate that will handle traffic.
2. [Set the Communication Endpoint](#set-oneagent-communication-settings).

   Configure OneAgent by specifying the ActiveGate as its new endpoint. For example:

   ```
   .\oneagentctl.exe --set-server=https://<activegate-endpoint>:9999/communication --restart-service
   ```
3. [Check if auto-update is enabled](#check-if-auto-update-is-enabled).

### Show current communication endpoints

Use the `--get-server` parameter to display the endpoints that OneAgent is to send the data to. These can be Dynatrace Server, Dynatrace Managed Cluster or ActiveGate.

* **Linux** or **AIX**:  
  `./oneagentctl --get-server`
* **Windows**:  
  `.\oneagentctl.exe --get-server`

Starting with OneAgent version 1.207, endpoints are reported using a format in which endpoints of equal priority are grouped using braces (`{...}`) and sorted according to connection priority. An asterisk (`*`) indicates the endpoint to which OneAgent currently sends the data. Endpoints are separated by a semicolon (`;`).
For example:

```
{https://endpoint1.com/communication;https:/10.0.0.0/communication;*https://endpoint3.com/communication}{https://endpoint4.com:9999/communication}
```

### Set environment ID

Use the `--set-tenant` parameter to set an [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). By default, this is already set to the correct value. If you're selling Dynatrace-based services, use this option to set your customers' IDs from the pool of IDs you purchased from Dynatrace.

* **Linux** or **AIX**:  
  `./oneagentctl --set-tenant=abc123456`
* **Windows**:  
  `.\oneagentctl.exe --set-tenant=abc123456`

Always use in combination with `--set-tenant-token`, which defines the [tenant token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") for internal authentication.

### Show environment ID

The Dynatrace [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") you received with your activation email.

Use the `--get-tenant` parameter to display the environment ID:

* **Linux** or **AIX**:  
  `./oneagentctl --get-tenant`
* **Windows**:  
  `.\oneagentctl.exe --get-tenant`

### Set tenant token

Use the `--set-tenant-token` parameter to set the [tenant token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it."), which is used to authenticate communication with the defined endpoint. Always use in combination with `--set-tenant`.

* **Linux** or **AIX**:  
  `./oneagentctl --set-tenant-token=abcdefg123456790`
* **Windows**:  
  `.\oneagentctl.exe --set-tenant-token=abcdefg123456790`

### Show tenant token

Use the `--get-tenant-token` parameter to display the currently defined token:

* **Linux** or **AIX**:  
  `./oneagentctl --get-tenant-token`
* **Windows**:  
  `.\oneagentctl.exe --get-tenant-token`

### Set proxy configuration

Use the `--set-proxy` parameter to set a proxy server:

* **Linux** or **AIX**:  
  `./oneagentctl --set-proxy=my-proxy.com`
* **Windows**:  
  `.\oneagentctl.exe --set-proxy=my-proxy.com`

### Clear proxy configuration

Use the `--set-proxy` parameter set to an empty value to clear proxy configuration:

* **Linux** or **AIX**:  
  `./oneagentctl --set-proxy=`
* **Windows**:  
  `.\oneagentctl.exe --set-proxy=`

Restart OneAgent service to apply changes.

### Show current proxy

Use the `--get-proxy` parameter to display the currently defined proxy OneAgent connects through:

* **Linux** or **AIX**:  
  `./oneagentctl --get-proxy`
* **Windows**:  
  `.\oneagentctl.exe --get-proxy`

### Exclude specific IPs from proxy

Use the `--set-no-proxy` parameter to exclude certain domains or IP addresses from using the proxy:

* **Linux** or **AIX**:  
  `./oneagentctl --set-no-proxy=my-proxy.com`
* **Windows**:  
  `.\oneagentctl.exe --set-no-proxy=my-proxy.com`

### Show current no-proxy settings

Use the `--get-no-proxy` parameter to view the currently configured settings for domains and IP ranges excluded from using the proxy:

* **Linux** or **AIX**:  
  `./oneagentctl --get-no-proxy`
* **Windows**:  
  `.\oneagentctl.exe --get-no-proxy`

### Check current port range

OneAgent consists of different processes that communicate via a TCP port with a watchdog. At startup, OneAgent watchdog attempts to open the first available port between port 50000 and 50100. In some cases you may need this port for your own applications that are started after OneAgent.

Use the `--get-watchdog-portrange` parameter to check the current port range defined for the watchdog.

* **Linux** or **AIX**:  
  `./oneagentctl --get-watchdog-portrange`
* **Windows**:  
  `.\oneagentctl.exe --get-watchdog-portrange`

### Set a new port range

Deprecated

Starting with OneAgent version 1.301, OneAgent doesn't use the TCP ports for its own inter-process communication. In case OneAgent occupies your applications' ports, upgrade OneAgent to version 1.301+.

Watchdog is a binary used for starting and monitoring OneAgent monitoring processes:

* `oneagentos`âoperating system monitoring
* `oneagentplugin`âmonitoring using [OneAgent extensions](/docs/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`âmonitoring using local [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`â[Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`â[network monitoring](/docs/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Use the `--set-watchdog-portrange=arg` parameter to change the watchdog listening port range to `<arg>`. The `<arg>` must contain two port numbers separated by a colon (`:`). For example `50000:50100`. The maximum supported port range is from 1024 to 65535. The port range must cover at least 4 ports. The port number starting the range must be lower.

* **Linux** or **AIX**:  
  `./oneagentctl --set-watchdog-portrange=50000:50100`
* **Windows**:  
  `.\oneagentctl.exe --set-watchdog-portrange=50000:50100`

## Automatic updates

For more information, see update OneAgent topics for [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows."), and [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix "Learn how you can update Dynatrace OneAgent on AIX.").

### Check if auto-update is enabled

Use the `get-auto-update-enabled` parameter to check whether OneAgent auto-update is enabled:

* **Linux** or **AIX**:  
  `./oneagentctl --get-auto-update-enabled`
* **Windows**:  
  `.\oneagentctl.exe --get-auto-update-enabled`

### Enable or disable auto-update

Set the `--set-auto-update-enabled` parameter to `true` or `false` to disable or enable OneAgent auto-update:

* **Linux** or **AIX**:  
  `./oneagentctl --set-auto-update-enabled=true`
* **Windows**:  
  `.\oneagentctl.exe --set-auto-update-enabled=true`

After you use this command to disable auto-updates, you won't be able to control OneAgent automatic updates using Dynatrace at **Settings** > **Updates** > **OneAgent updates**.

## Log monitoring

For more information, see [Log Monitoring](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.").

### Check if Log Monitoring is enabled

Use the `--get-app-log-content-access` parameter to check whether Log Monitoring is enabled:

* **Linux**:  
  `./oneagentctl --get-app-log-content-access`
* **Windows**:  
  `.\oneagentctl.exe --get-app-log-content-access`

### Enable or disable Log Monitoring

Set the `--set-app-log-content-access` parameter to `true` or `false` to disable or enable Log Monitoring:

* **Linux**:  
  `./oneagentctl --set-app-log-content-access=true`
* **Windows**:  
  `.\oneagentctl.exe --set-app-log-content-access=true`

## Create support archive

OneAgent version 1.225+

If you don't have access to Dynatrace or you would like to script diagnostic data collection, you can use the `oneagentctl` command to collect a [subset](#contents) of the full [OneAgent diagnostics](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") data right on the host where OneAgent is installed. With the diagnostic data collected for OneAgent, you can:

* Easily collect the diagnostic data for a specific host
* Directly provide Dynatrace Support the details they need to diagnose the issue

The command requires the OneAgent service to be running.

To create a support archive with diagnostic data, run `oneagentctl` with the `--create-support-archive` parameter. By default, the support archive contains the data for a 7-day time frame and is created in the current working directory. Optionally, you can set a custom directory and timeframe with the `directory` and `days` parameters. Note that `onegentctl` won't create a directory; you must point it to an existing directory with a relative or absolute path. For example:

* **Linux** or **AIX**:  
  `./oneagentctl --create-support-archive directory=/data/support-archive days=30`
* **Windows**:  
  `.\oneagentctl.exe --create-support-archive directory=C:\data\support-archive days=30`

The command saves the archive as the `support_archive_agent_YYYY-MM-DD_hhmmss.zip` file. For example:

```
Creating support archive from last 30 days in C:\data\support-archive



Waiting 30s for archive request to be processed



Processing archive, waiting up to 15m 0s



Archive saved as C:\data\support-archive\support_archive_agent_2021-09-07_121619.zip
```

### Contents of diagnostic data

All the collected diagnostic data is compressed into a `support_archive_agent_YYYY-MM-DD_hhmmss.zip` archive that includes the following subset of the full [OneAgent diagnostics](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") data:

Folder or file

Description

`support_archive` (ZIP)

Contains the local configuration of the OneAgent installed on the host or process where youâve run the troubleshooting, as well as the OneAgent-related log files.

`diagnostic_files` (ZIP)

Contains information about process group detection, auto-injection problems, and extension configuration.

## Access to system logs for proactive support

OneAgent downloads specific system logs so that Dynatrace can diagnose issues that may be caused by conditions in your environment. The logs are also saved in the support archive. Most often such issues are related to deep monitoring or auto-update installations.

### Check if access to system logs is enabled

Use the `--get-system-logs-access-enabled` parameter to check whether access to system logs is enabled:

* **Linux** or **AIX**:  
  `./oneagentctl --get-system-logs-access-enabled`
* **Windows**:  
  `.\oneagentctl.exe --get-system-logs-access-enabled`

### Enable or disable access to system logs

Set the `--set-system-logs-access-enabled` parameter to `true` or `false` to disable or enable access to system logs:

* **Linux** or **AIX**:  
  `./oneagentctl --set-system-logs-access-enabled=true`
* **Windows**:  
  `.\oneagentctl.exe --set-system-logs-access-enabled=true`
  Restart OneAgent service to apply changes.

Note that the `--set-system-logs-access-enabled` and `--get-system-logs-access-enabled` parameters refer to a self-diagnostics setting and are not related to [Log Monitoring](#log-monitoring).

Disabling system log access limits our ability to diagnose and solve issues proactively. With access to system logs revoked, you may need to manually provide Dynatrace with the contents of your system logs to help us diagnose issues within your environment.

## Host ID

Dynatrace assigns a unique ID to each host monitored in your environment. Host IDs can be used as parameters in Dynatrace API requests, for example [Topology and Smartscape API - Hosts API](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api "Learn how you can use the Dynatrace API to manage monitored hosts."). The host ID also constitutes the URL of the **Host overview** page, for example, `https://environment.org/#newhosts/hostdetails;id=HOST-6E56EE455C84E232`.

### Display your host ID

To find a host ID, use the `--get-host-id` parameter. For example:

* **Linux** or **AIX**:  
  `./oneagentctl --get-host-id`
* **Windows**:  
  `.\oneagentctl.exe --get-host-id`

### Define the host ID source

Available on all supported platforms for OneAgent version 1.223+. For OneAgent version 1.221 and earlier, this feature is supported only for Citrix Virtual Apps and Desktops.

It's particularly important to keep your host ID static in dynamic virtual environments where hosts are recreated on a daily basis.

To **define the source for host ID generation**, use `--set-host-id-source` and set it to one of the predefined values:

* `auto` â Let Dynatrace generate the host ID automatically
* `ip-addresses` â Generate host ID based on the host IP address
* `mac-addresses` â Generate host ID based on the host's NIC MAC address
* `fqdn` â Generate host ID based on the host fully qualified domain name (FQDN) in the `host.domain` format. If the FQDN doesn't contain a dot character, the NIC MAC address is used instead.
* If you monitor multiple environments, you can split the hosts with identical IPs, MAC addresses, or FQDNs using a different namespace for each environment. The namespace can contain only alphanumeric characters, hyphens, underscores, and periods; the maximum length is 256 characters.

  + `ip-addresses;namespace=<namespace>`
  + `mac-addresses;namespace=<namespace>`
  + `fqdn;namespace=<namespace>`

For example, to set the host ID source to `ip-addresses` and assign it to a namespace called `test`, run `oneagentctl` with the following parameter:

* **Linux** or **AIX**:  
  `./oneagentctl --set-host-id-source="ip-addresses;namespace=test"`
* **Windows**:  
  `.\oneagentctl.exe --set-host-id-source="ip-addresses;namespace=test"`

After you change the host ID source, you must restart all your monitored applications and then restart the OneAgent service to create the new host entity in your environment. You can use the `--restart-service` parameter with `oneagentctl` to restart OneAgent automatically or stop and start OneAgent process manually. For OS-specific instructions, see [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

To **check the host ID source**, use the `--get-host-id-source` parameter:

* **Linux** or **AIX**:  
  `./oneagentctl --get-host-id-source`
* **Windows**:  
  `.\oneagentctl.exe --get-host-id-source`

For host ID source set to `ip-addresses` and the `test` namespace, the command will return the following result:

```
ip-addresses;namespace=test
```

## Host groups

For an overview of how to use host groups, see [Organize your environment using host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").

Alternatively, to modify host group assignment centrally from the Dynatrace Cluster, you can use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host group** action).

### Change host group assignment

Use the `--set-host-group` parameter to change the host group assignment.

To assign the host to `MyHostGroup`:

* **Linux** or **AIX**:  
  `./oneagentctl --set-host-group=MyHostGroup`
* **Windows**:  
  `.\oneagentctl.exe --set-host-group=MyHostGroup`

Host group string requirements:

* Can contain only alphanumeric characters, hyphens, underscores, and periods
* Must not start with `dt.`
* Maximum length is 100 characters

Using `--set-host-group` requires restart of OneAgent, as well as restart of all the monitored services. Add [`--restart-service`](#oneagent-restart) to the command to restart OneAgent automatically (version 1.189+) or stop and start OneAgent process manually. For OS-specific instructions, see [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

Changing the host group assignments results in recalculation of process group IDs, which impacts data aggregation. To read more about the impact of host group changes on process group detection, see [Organize your environment using host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups#how-host-groups-affect-your-monitoring-environment "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").

### Clear host group assignment

Use the `--set-host-group` parameter with an empty value to clear the host group assignment:

* **Linux** or **AIX**:  
  `./oneagentctl --set-host-group=`
* **Windows**:  
  `.\oneagentctl.exe --set-host-group=`

### Display host group assignment

Use the `--get-host-group` parameter to display the current host group assignment:

* **Linux** or **AIX**:  
  `./oneagentctl --get-host-group`
* **Windows**:  
  `.\oneagentctl.exe --get-host-group`

## Host tags and metadata

Within dynamic or large environments, manual host tagging can be impractical. For dynamic deployments that include frequently changing host instances and names (for example, AWS or MS Azure), you can use dedicated `oneagentctl` parameters to apply custom tags, names, and metadata to your hosts.

The `oneagentctl` methods listed below allow only for editing the metadata added using `oneagentctl` itself or previously using the configuration files. Tags and metadata added using Dynatrace, as well as retrieved from a monitored environment (for example the AWS tags) are not editable with `oneagentctl` and won't be displayed using `--get-host-tags` and `--get-host-properties` parameters.

### Cloud metadata detection

By default, the `oneagentos` process automatically detects cloud environments such as AWS, Azure, and Google Compute Engine. It sends requests to the dedicated Metadata API located at the internal IP address `169.254.169.254`. The OneAgent uses the retrieved metadata to provide additional context about the monitored resources within these environments.

### Custom host name

Use the `oneagentctl` command-line tool with the `--set-host-name` parameter to override an automatically detected host name. A host name must not contain the `<`, `>`, `&`, `CR` (carriage return), or `LF` (line feed) characters. The maximum length is 256 characters.

This command adds a custom host name to display in the UI, but the detected host name is not changed. For details, see [Set custom host names](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

To change the host name:

* **Linux** or **AIX**:
  `./oneagentctl --set-host-name=myhostname`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=myhostname`

To revert to the auto-detected host name, set the `--set-host-name` parameter to an empty value, as in `--set-host-name=""`. For example:

* **Linux** or **AIX**:
  `./oneagentctl --set-host-name=""`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=""`

The change might not be reflected in the Dynatrace web UI for up to 6 minutes.

Using `--set-host-name` requires restart of OneAgent. Add `--restart-service` to the command to restart OneAgent automatically (version 1.189+) or stop and start the OneAgent process manually. For OS-specific instructions, see [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

To show the host name:

* **Linux** or **AIX**:  
  `./oneagentctl --get-host-name`
* **Windows**:  
  `.\oneagentctl.exe --get-host-name`

### Custom host metadata

Once configured, custom metadata is displayed as a set of properties at the bottom of the **Properties and tags** section of the host overview page. The property values must not contain an `=` character (unless used as a key-value delimiter) or whitespace characters. The maximum length is 256 characters, including the key-value delimiter. The key name must not start with a `#` character.

Alternatively, to modify host metadata centrally from the Dynatrace Cluster, you can use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host properties** action).

For versions earlier than 1.189, use a [host metadata configuration file](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#edit-the-host-metadata-configuration-file "Learn how to tag and set additional properties for a monitored host.").

To **add or change host properties**, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-property=AppName --set-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --set-host-property=AppName --set-host-property Environment=Dev`

You can add or change more than one property in the same command.

Set a security context for your host

To set a security context for your host, use the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-property=dt.security_context=easytrade_sec`
* **Windows**  
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`

The `dt.security_context` is utilized by multiple features within Dynatrace, such as [Log security context](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.") and [Business events security context](/docs/observe/business-observability/bo-event-processing/bo-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming business events data for better understanding, analysis, or further processing.").
Additionally, if you're an account administrator looking to grant access to monitored entities based on their security context, see [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").

To **remove host properties**, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

You can remove more than one property with a single command. If a property key that's passed in the command doesn't exist, a non-zero exit code will be returned, but all the existing properties passed in the command will be removed. After you remove host properties, they remain visible in Dynatrace for up to 7 hours.

To **show all properties** configured for the host, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --get-host-properties`
* **Windows**  
  `.\oneagentctl.exe --get-host-properties`

### Custom host tags

After you configure custom host tags, they are displayed at the top of the **Properties and tags** section of the host overview page. A property value must not contain `=` (unless used as a key-value delimiter) or whitespace characters. The maximum length is 256 characters, including the key-value delimiter. A key name must not start with `#`.

Alternatively, to modify host tags centrally from the Dynatrace Cluster, you can use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify host tags** action).

To **add or change host tags**, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**  
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`

You can add or change more than one tag in the same command. It is allowed to define tags with the same key but different values.

To **remove tags**, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --remove-host-tag=role=fallback --remove-host-tag=Gdansk`
* **Windows**  
  `.\oneagentctl.exe --remove-host-tag=role=fallback --remove-host-tag=Gdansk`

You can remove more than one tag with the same command. If a tag passed in the command doesn't exist, a non-zero exit code is returned, but all the existing tags passed in the command are removed. After you remove tags, they remain visible in Dynatrace for up to 6 hours.

To **show all tags** configured for the host, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --get-host-tags`
* **Windows**  
  `.\oneagentctl.exe --get-host-tags`

## Monitoring modes

Activates one of the OneAgent monitoring modes:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

To enable a specific monitoring mode, set the `--set-monitoring-mode` parameter to one of the values:

* `fullstack`
* `infra-only`
* `discovery`

For example:

```
--set-monitoring-mode=infra-only
```

Use Infrastructure Monitoring mode or Discovery mode in place of Full-Stack Monitoring mode. With this approach, you receive infrastructure health data, with no application or user performance data. For details, see [Monitoring modes](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Find out what's included in Dynatrace Infrastructure Monitoring mode.").

### Check which monitoring mode is enabled

Use the `--get-monitoring-mode` parameter to check which monitoring mode is enabled:

* **Linux** or **AIX**:  
  `./oneagentctl --get-monitoring-mode`
* **Windows**:  
  `.\oneagentctl.exe --get-monitoring-mode`

The command returns one of the following:

* `fullstack`: Full-Stack Monitoring mode
* `infra-only`: Infrastructure Monitoring mode
* `discovery`: Discovery mode

Changing the Infrastructure Monitoring mode requires restart of OneAgent, as well as restart of all monitored services. Add [`--restart-service`](#oneagent-restart) to the command to restart OneAgent automatically (version 1.189+) or stop and start the OneAgent process manually. For OS-specific instructions, see [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

## Automatic injection for Infrastructure Monitoring mode

OneAgent version 1.213

Automatic OneAgent injection is enabled by default in Infrastructure Monitoring mode. It's required to collect JMX/PMI metrics and to handle Application Security in Infrastructure Monitoring mode.

For more information, see [Infrastructure and Discovery monitoring modes](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Find out what's included in Dynatrace Infrastructure Monitoring mode.").

### Check if auto-injection is enabled

Use the `get-auto-injection-enabled` parameter to check whether OneAgent auto-injection is enabled:

* **Linux** or **AIX**:  
  `./oneagentctl --get-auto-injection-enabled`
* **Windows**:  
  `.\oneagentctl.exe --get-auto-injection-enabled`

### Enable or disable auto-injection

Set the `--set-auto-injection-enabled` parameter to `true` or `false` to enable or disable OneAgent auto-injection:

To enable auto-injections:

* **Linux** or **AIX**:  
  `./oneagentctl --set-auto-injection-enabled=true`
* **Windows**:  
  `.\oneagentctl.exe --set-auto-injection-enabled=true`

To disable auto-injections:

* **Linux** or **AIX**:  
  `./oneagentctl --set-auto-injection-enabled=false`
* **Windows**:  
  `.\oneagentctl.exe --set-auto-injection-enabled=false`

For more information, see [Disable auto-injection](/docs/observe/infrastructure-observability/hosts/monitoring-modes#disable-auto-injection "Find out what's included in Dynatrace Infrastructure Monitoring mode.").

## Metric ingestion

Local metric ingestion is currently supported only on Windows and Linux.

You can use the `oneagentctl` command to check or change communication ports used for local metric ingestion using the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), [Scripting integration](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration."), [Telegraf](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace."), or [DynatraceStatsd](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client."). Changing the metric ingestion port requires restart of OneAgent. Add [`--restart-service`](#oneagent-restart) to the command to restart OneAgent automatically.

See [Metrics ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") to learn more.

### OneAgent API, scripting integration, and Telegraf

The default metric ingestion port is `14499`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the port. Changing the metric ingestion port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

### Check the ingestion port

Use the `--get-extensions-ingest-port` parameter to show the current local ingestion port, `14499` by default.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Set a custom ingestion port

Use the `--set-extensions-ingest-port=<arg>` parameter to set a custom local ingestion port.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Configure proxy

Configure your host proxy to allow localhost traffic going to the metric ingestion port, `14499` by default.

### StatsD

### OneAgent listener

The default DynatraceStatsD UDP listening port for the OneAgent listener is `18125`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the metric ingestion port. Changing the port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

#### Check the ingestion port

Use the `--get-extensions-statsd-port` parameter to show the current DynatraceStatsd UDP listening port (default = `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Set a custom ingestion port

Use the `--set-extensions-statsd-port=<arg>` parameter to set a custom DynatraceStatsd UDP listening port.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Remote StatsD

The default DynatraceStatsD UDP listening port for a remote listener is `18126`.

To change the default `18126` listening port, modify the `StatsdPort` parameter in the ActiveGate `extensionsuser.conf` file:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Network zones

To learn about network zone naming rules and other reference information, see [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

Alternatively, to modify network zone assignment centrally from the Dynatrace Cluster, you can use [Remote configuration management](/docs/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify network zone** action).

### Set a network zone

Use the `--set-network-zone` parameter to instruct OneAgent to communicate via the specified network zone. The name of a network zone is a string of alphanumeric characters. You can also use hyphens (`-`), underscores (`_`), and a dot (`.`) as a seperator. The network zone name must not start with a dot. The length of the string is limited to 256 characters. Network zone names are not case-sensitive. Dynatrace stores these names in lowercase. For more information, see the section on [network zone naming](/docs/manage/network-zones/network-zones-basic-info#naming "Learn network zones basics.")

* On **Linux** or **AIX**:  
  `./oneagentctl --set-network-zone=<your.network.zone>`
* On **Windows**:  
  `.\oneagentctl.exe --set-network-zone=<your.network.zone>`

#### Reset a network zone

You can reset the network zone setting by passing an empty network zone name:

* On **Linux** or **AIX**:  
  `./oneagentctl --set-network-zone=""`
* On **Windows**:  
  `.\oneagentctl.exe --set-network-zone=""`

### Display network zone setting

Use the `--get-network-zone` parameter to display the current network zone configuration:

* On **Linux** or **AIX**:  
  `./oneagentctl --get-network-zone`
* On **Windows**:  
  `.\oneagentctl.exe --get-network-zone`

## Passing configuration parameters during installation

You can pass the `--set-*` parameters at installation time. The configuration parameters are applied right before OneAgent service starts and there's no need to restart it to apply your configuration.

Linux and AIX

Windows

To pass through the configuration parameters, simply add the parameter and precede the value with the equals sign (`=`). For example:

```
/bin/sh Dynatrace-OneAgent-Linux.sh â-set-host-group=test_group
```

### EXE installer

To pass the configuration parameters through using the EXE installer, simply add the parameter and precede the value with the equals sign (`=`). For example:

```
Dynatrace-OneAgent-Windows.exe --set-host-group=test_group
```

### MSI package

You can also pass the configuration parameters through using the MSI package. This time however, you must use an extra `ADDITIONAL_CONFIGURATION` parameter. For example:

```
Dynatrace-OneAgent-Windows.msi ADDITIONAL_CONFIGURATION="--set-host-group=test_group"
```

## FIPS 140 cryptographic algorithms

OneAgent version 1.245+

OneAgent uses the FIPS mode to be compliant with the FIPS 140-3 computer security standard.

### Check if FIPS 140 is enabled

Use the `--get-fips-enabled` to check if OneAgent uses FIPS 140 validated cryptographic algorithms.

* On **Linux** or **AIX**  
  `./oneagentctl --get-fips-enabled`
* On **Windows**  
  `.\oneagentctl.exe --get-fips-enabled`

### Enable or disable FIPS 140

Enabling or disabling of FIPS 140 validated cryptographic algorithms can only be done during installation.

Set the `--set-fips-enabled` parameter to `true` or `false` to enable or disable the FIPS 140 validated cryptographic algorithms on OneAgent. The default value for first time installation is `false`.

To enable FIPS mode:

* On **Linux**, **AIX** or **Windows**:
  Run the installer with `--set-fips-enabled=true`

To disable FIPS mode:

* On **Linux**, **AIX** or **Windows**:
  Run the installer with `--set-fips-enabled==false`

If you want to enable FIPS mode for application-only deployment, go to `/paas/package/agent` and delete `dt_fips_disabled.flag`.

## cap\_setuid for OS Agent

GPFS monitoring

OneAgent version 1.293+

Enabling `cap_setuid` for OS Agent is required for GPFS monitoring.

Following parameters are only available in [OneAgent non-privileged mode on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.").

* `get-osagent-cap-setuid-enabled`
* `set-osagent-cap-setuid-enabled`

You can enable `cap_setuid` for OS Agent starting from OneAgent version 1.293+, but you can use GPFS monitoring only from OneAgent version 1.295+.

### Check if cap\_setuid for OS Agent is enabled

Use the `get-osagent-cap-setuid-enabled` parameter to check whether cap\_setuid for OS Agent is enabled:

`./oneagentctl --get-osagent-cap-setuid-enabled`

### Enable or disable cap\_setuid for OS Agent

Set the `--set-osagent-cap-setuid-enabled` parameter to `true` or `false` to disable or enable cap\_setuid for OS Agent:

`./oneagentctl --set-osagent-cap-setuid-enabled=true`


---


## Source: oneagent-features.md


---
title: OneAgent features
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-features
scraped: 2026-02-17T04:45:56.668631
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


---


## Source: oneagent-health.md


---
title: OneAgent health overview
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-health
scraped: 2026-02-17T05:02:50.137216
---

# OneAgent health overview

# OneAgent health overview

* Latest Dynatrace
* 4-min read
* Updated on Jan 15, 2026

The OneAgent health overview empowers you to discover all your deployed [OneAgent modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") at scale and detect anomalies before they become problems. With the OneAgent health overview, for example, you can discover:

* Outdated OneAgent modules that require an update to continue full Dynatrace support.
* Connectivity issues between OneAgent modules and your Dynatrace Cluster.
* Incompatible OneAgent modules that require corrective actions.
* Processes that require a restart to continue monitoring.
* OneAgent modules where auto-update is disabled.

## Get started

To get started with the OneAgent health overview, go to **OneAgent Health**.

![OneAgent Health](https://dt-cdn.net/images/oneagent-health-1744-afe02d9e3b.png)

The **OneAgent health overview** comprises

* An area chart focusing on the [Health state metric](#health-state-metric).

  The area chart includes data on OneAgent modules during the selected timeframe. You can split the area chart by health state, monitoring state, module type, module version, process type, and operating system type.
* A data table presenting a variety of attributes of the contributing OneAgent modules.

  The data table contains real-time data of the OneAgent modules seen in your environment in the last 5 minutes. You can filter it by specific attributes. To display additional attributes, select **Configure columns**.

  Above the data table, the lowest and highest compatible OneAgent versions for this Dynatrace cluster are displayed.

  The environment permission [Install OneAgent](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") is required to visualize data in this table.

Select a specific data point in the area chart to see the contributing OneAgent modules in the data table.

## Health state metric

The **Health state** metric (`dsfm:cluster.oneagent.agent_modules`) indicates the health state of your deployed OneAgent modules. It is divided into four classesâCritical, Warning, Info, and Healthy. Each class has different implications.

Health state

Implications

Critical

* A OneAgent module struggles with problems that might result in monitoring outage.
* Corrective action is required.

Warning

* A OneAgent module struggles with anomalies that might impact monitoring availability.
* Corrective action is recommended.

Info

* The health of a OneAgent module could be improved to ensure monitoring availability.
* Corrective action is not necessary.

Healthy

* A OneAgent module is healthy without monitoring disturbances.
* No action is required.

### Health state examples

The following conditions are applied to your OneAgent modules and result in specific recommendations.

Health state

Condition

Recommendation

Critical

Installer version date older than 11 months

Update OneAgent to a newer version to maintain full Dynatrace support.

Critical

Module heartbeat is 180 seconds overdue

Dynatrace hasnât received data from this module for 180 seconds. There might be communication problems, or your process might have exited unexpectedly.

Critical

Host ID conflict

Multiple monitored hosts report that theyâre using the same host identifier. This unexpected situation might be the result of machine cloning. Please contact a Dynatrace product expert via live chat within your environment.

Critical

Host quota exceeded

Monitoring is currently disabled. Please contact a Dynatrace product expert via live chat within your environment.

Critical

Installer version marked as faulty by Dynatrace

Update OneAgent to a newer version. Processes might also need to be restarted.

Critical

Module version marked as faulty by Dynatrace

Update OneAgent to a newer version. A process restart might also be required.

Warning

Installer version is between 9 and 11 months old

Update to a newer OneAgent version to stay current.

Warning

Minimum OneAgent version incompatible

Update OneAgent to a newer version. A process restart might also be required, even if youâve already updated your module.

Warning

Maximum OneAgent version incompatible

Only OneAgent versions that are equal to or lower than the Dynatrace cluster version can be connected. Download a compatible OneAgent version from this cluster.

Info

Process restart needed

Your module version is outdated. Restart your process to update the module to a newer OneAgent version.

Info

Auto-update suppressed

Enable auto-update to stay current.

### Limitations

* Only the **Health state** metric includes the z/OS Java module and AWS Lambda, Azure, and Google Cloud integrations.
* Only OneAgent modules seen in the last 5 minutes are shown in the data table.
* Only the data table can be filtered by management zone.


---


## Source: oneagent-security-context.md


---
title: Set up Grail permissions for OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-security-context
scraped: 2026-02-16T21:13:00.103708
---

# Set up Grail permissions for OneAgent

# Set up Grail permissions for OneAgent

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Aug 19, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This security context can represent your security architecture and could even be hierarchical by encoding this into a string: `department-A/department-AB/team-C`.

You need to ensure the attribute exists as part of the telemetry data and that OneAgent provides the value directly at the VM level.

To set a security context for your host, use the following command:

* Linux and AIX

  ```
  ./oneagentctl --set-host-property=dt.security_context=easytrade_sec
  ```
* Windows

  ```
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`
  ```

This adds the security context to all metrics, spans, events, and logs collected by OneAgent on this host.

The `dt.security_context` is utilized by many features in Dynatrace and available for all telemetry data. You can use it for [record-level security](/docs/platform/grail/organize-data/assign-permissions-in-grail#field-permissions "Find out how to assign permissions to buckets and tables in Grail.").


---


## Source: troubleshoot-oneagent-deep-monitoring-issues.md


---
title: Troubleshooting OneAgent deep-monitoring issues
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-deep-monitoring-issues
scraped: 2026-02-17T04:54:08.485819
---

# Troubleshooting OneAgent deep-monitoring issues

# Troubleshooting OneAgent deep-monitoring issues

* Latest Dynatrace
* 3-min read
* Published Jul 16, 2018

Dynatrace OneAgent is supported on many [platforms](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") and offers deep monitoring for many [technologies and frameworks](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks."). The Dynatrace team tests all possible deep-monitoring scenarios, but to streamline our supportability in situations in which deep monitoring might not work as planned, you can leverage the [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") page.

## Use cases

Settings on the **OneAgent features** page make it possible to disable certain OneAgent functionality at a fine-grained level to facilitate issue resolution. This can be useful for identifying the root cause of a problem, all the way down to a specific feature.

These settings also make it possible to temporarily disable certain features that might lead to problems while retaining all other functionality. At the same time, the Dynatrace Support team can work on a permanent fix.

Before deactivating OneAgent settings

We don't recommended deactivating OneAgent feature settings without first consulting Dynatrace Support. When you disable a specific OneAgent feature in your environment, OneAgent stops capturing observability data for this feature, so you might miss important information.

## Settings

Each feature on the **OneAgent features** page can be turned off for the entire environment, a specific process group, or a single process.

### Environment settings

To turn a feature on or off for the entire environment

1. Go to **Settings**.
2. Select **Preferences** > **OneAgent features**.
3. Find the feature. You can enter a filter string above the table.
4. Expand the entry to:

   * Optional Review the feature description
   * Optional Review metadata
   * Optional Follow a link to relevant release notes
5. Change the **Enabled** setting as needed.

All instrumentation features can be enabled or disabled by the main toggle, and some of them have two additional options:

* **Activate this feature also in OneAgents only fulfilling the minimum Opt-In version**  
  This setting activates a feature with a minimum opt-in version when first released. Usually, you can activate a feature if it fulfills the minimum OneAgent version, but some of them are first released as opt-in features with a minimum opt-in version. This is useful when a General Availability (GA) OneAgent feature is greater than a minimum opt-in version. If you already enabled the feature during opt-in, you can still use the OneAgent without upgrading to the new GA version.
* **Instrumentation enabled**  
  This setting has an immediate effect. However, upon restart/startup of a process, the feature won't be added to your application. This means that the feature will have no impact on your application. The downside is that, if you re-enable the feature later, you'll need to restart the affected processes.

### Process-specific settings

If a specific feature is problematic only in the context of a specific process group, you can disable the feature for just that process group and leave the rest of your environment untouched.

To turn a feature on or off for a particular process or group of processes

1. Go to **Smartscape Topology**.
2. Select **Processes**.
3. On the topology map, hover over the process and select the link icon to go to the process details page. For example:

   ![Link from Smartscape topology to process details page](https://dt-cdn.net/images/link-to-process-page-377-da0282e435.png)
4. On the process details page, select **More** (**â¦**) > **Settings** and then select the **OneAgent features** tab.
5. Select **Add override** to add a process-specific setting that overrides the environment setting.
6. Type a search string in the **Feature** box to find and select the feature.
7. Set the switches as needed for the override and then select **Save changes**.


---


## Source: troubleshoot-oneagent-installation.md


---
title: Troubleshooting OneAgent installation
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation
scraped: 2026-02-17T04:52:59.849472
---

# Troubleshooting OneAgent installation

# Troubleshooting OneAgent installation

* Latest Dynatrace
* Troubleshooting
* 13-min read
* Updated on Oct 17, 2025

Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.

## General troubleshooting

Why doesn't OneAgent start to monitor Apache process after restart?

Following installation of OneAgent, your Apache web server must be *completely* restarted to enable monitoring. To do this correctly, it's important to understand the difference between "partial" and "complete" restarts. In the case of partial restarts, the main Apache process re-reads its configuration files, re-opens its log files, and then restarts its worker processes. OneAgent however, requires a complete Apache web server restart in which all workers andâmost importantlyâthe main Apache process are shut down entirely and then restarted.

See [Stopping and Restarting Apache HTTP Serverï»¿](https://httpd.apache.org/docs/2.4/stopping.html) for more information on the different types of available restarts.

## How to perform a complete restart

**Linux and AIX**

You may be accustomed to restarting Apache by issuing an `apachectl restart` command. However, this command only results in a partial Apache restart.

To execute a complete Apache restart and enable deep monitoring with Dynatrace OneAgent, you need to first invoke a complete shutdown using the `apachectl stop` command. Only following this step can you restart the server using `apachectl start` .

It's fine to use `service apache2 restart` on Ubuntu systems. Note however that whatever commands you use, you'll likely need superuser rights (sudo).

**Windows**

On Windows, you can either use the built-in Windows Service Management or Apache Service Monitor (`httpd.exe`) to restart Apache services. Restarting the Apache service with Windows Service Management guarantees the complete restart. With `httpd.exe`, you may be accustomed to restarting Apache by issuing a `httpd.exe -k restart -n "Apache2.4"` command. However, this command only results in a partial Apache restart.

To execute a complete Apache restart and enable deep monitoring with OneAgent, you need to first invoke a complete shutdown using the `httpd.exe -k stop -n "Apache2.4"` command. Only following this step can you restart the server using `httpd.exe -k start -n "Apache2.4"`.

What can I do when OneAgent blocks a port I need?

Deprecated

Starting with OneAgent version 1.301, OneAgent doesn't use the TCP ports for its own inter-process communication. In case OneAgent occupies your applications' ports, upgrade OneAgent to version 1.301+.

OneAgent consists of different processes that communicate via a TCP port with a watchdog. At startup, OneAgent watchdog attempts to open the first available port between port 50000 and 50100. In some cases you may need this port for your own applications that are started after OneAgent. In such cases, you can change the port range that the OneAgent watchdog uses by calling OneAgent command-line interface.

You can change the watchdog listening port by using `set-watchdog-portrange` via [oneagentctl command-line tool](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") :

For example, to change port range to `50005:50105`, go to the [oneagentctl directory](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") and run the following command:

* On **Linux** or **AIX**:  
  `./oneagentctl --set-watchdog-portrange 50005:50105`
* On **Windows**:  
  `.\oneagentctl.exe --set-watchdog-portrange 50005:50105`  
  Restart OneAgent service to apply changes.

See [Which network ports does Dynatrace Server use?ï»¿](https://docs.dynatrace.com/managed/shortlink/managed-network-ports) for information on the ports used by Dynatrace.

Server certificate check failed

OneAgent is shipped with trusted Dynatrace SSL certificates, which are used to verify that OneAgent connects successfully to Dynatrace Server or ActiveGate.

If your environment uses a proxy (thereby requiring an update to the remote server's SSL certificate) or you have an Environment ActiveGate with its own custom certificate, you might encounter a `Server certificate check failed` message during the initial connection check.

To resolve this issue, see [OneAgent security](/docs/ingest-from/dynatrace-oneagent/oneagent-security#trusted-root-certificates "Manage OneAgent security").

Processes not detected?

One of the following may have occurred

* The process isnât supported by our monitoring technology. You can always check which [process types Dynatrace supports](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* The process isnât working on your server. Make sure your servers are running and that the processes are operational.
* There is delay in communication between Dynatrace and your OneAgent. If this is the case, wait a few moments and try again.
* Your OneAgent isnât working properly. Go to **Settings** > **Monitoring** > **Monitoring overview** to confirm that monitoring is enabled for the host running your software.

If you're still unable to resolve this issue, contact a Dynatrace product expert via live chat within your Dynatrace environment. Also, consider installing OneAgent on a different machine.

OneAgent problems began after a significant host OS update.

We do not support major operating system modifications to a host on which OneAgent is installed.

OS changes that can affect OneAgent include updates or modifications such as:

* System kernel patch
* Major OS upgrade
* Any other modification to the system configuration that results in a significant update or modification to the OS

Major OS modifications may lead to problems such as:

* OneAgent monitoring problems
* OneAgent service restart or deletion
* OneAgent uninstallation

To make major OS modifications to a OneAgent host

1. Uninstall OneAgent
2. Apply the OS modifications
3. Reinstall OneAgent  
   Reinstallation may require you to provide connection details to the installer. However, part of the OneAgent configuration will remain after uninstallation, such as the host identification.

This information applies to all operating systems on which full-stack OneAgent installation is supported.

SDK initialization and error handling

If the SDK stub encounters issues loading or initializing the OneAgent module (particularly if [`onesdk_initialize`ï»¿](https://dt-url.net/mp038qp) or [`onesdk_initalize_2`ï»¿](https://dt-url.net/dz238k4) returns an error code), enable logging for the SDK stub to diagnose the problem.

Use one of these options to enable logging:

* Set the `DT_LOGLEVELSDK={level}` environment variable (the easiest option).
* Call the `onesdk_stub_set_logging_level(ONESDK_LOGGING_LEVEL_{LEVEL})` function.
* If your program passes command line arguments to the SDK ([`onesdk_stub_process_cmdline_args`ï»¿](https://dt-url.net/t50394g)), use the `--dt_loglevelsdk={level}` command line argument.

Whichever option you choose, be sure to apply it before calling `onesdk_initialize` or `onesdk_initalize_2`.

By default, after logging is enabled, the stub's log output is directed to `stderr`. If you need an alternative method to process stub log messages, see the [`onesdk_stub_set_logging_callback`ï»¿](https://dt-url.net/hn03995) function documentation.

If initialization fails, the most frequently encountered error code is `ONESDK_ERROR_LOAD_AGENT` (numerical code `2952658951`, `-1342308345` or `0xaffe0007`, error message `"Could not load agent."`).

The two primary causes of this issue are:

* **Cause**: OneAgent is not installed on the host where the program is executed.

  **Solution**: Install OneAgent and restart the program.
* **Cause**: The program is initiated with a debugger, so OneAgent will not inject.

  **Solution**: Launch the program without the debugger. You can still attach the debugger later, after the program is running.

Post-initialization SDK troubleshooting

After successfully initializing the SDK, you might still encounter issues, such as missing paths in the UI or unexpected error codes like `ONESDK_INVALID_HANDLE`. In such cases:

* Check messages from the OneAgent logging callbacks. See the documentation for [`onesdk_agent_set_warning_callback`ï»¿](https://dt-url.net/2r43812) and [`onesdk_agent_set_verbose_callback`ï»¿](https://dt-url.net/8w6389l).
* Examine the OneAgent log files.

  See the following pages for exact locations of log files:

  + [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")
  + [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system")

  You can increase the OneAgent log level by setting the `DT_LOGLEVELFILE={level}` environment variable or passing the `--dt_loglevelfile={level}` command line argument to the SDK.

  Alternatively, you can use `DT_LOGLEVELCON={level}` or `--dt_loglevelcon={level}` if you want to receive OneAgent log output via `stderr`.
* In certain scenarios, [`onesdk_agent_get_current_state`ï»¿](https://dt-url.net/l9838z9) can provide further insights.

## OS-specific troubleshooting

### Linux

OneAgent installed on Chef Habitat deployments doesn't inject into processes

Even though you can successfully install OneAgent on machines hosting services deployed by Chef Habitat, OneAgent won't be able to inject into the processes, because in such deployments, the Chef Habitat uses its own supervisor host-specific glibc, not the system-level glibc OneAgent relies on.

#### Workaround

As a workaround, create an `ld.so.preload` file for each glibc version installed by Chef whose content points to the OneAgent Process Module on the Chef Habitat supervisor host. Run the following command as root:

```
[ -d /hab/pkgs/core/glibc ] && for v in $(find /hab/pkgs/core/glibc -type d -name etc); do sudo echo "/opt/dynatrace/oneagent/agent/bin/current/linux-x86-64/liboneagentproc.so" > $v/ld.so.preload && echo "Installed workaround in '$v'"; done
```

You must run this command every time Chef Habitat updates the glibc version. You can also run it as a cron job. In such cases, make sure it runs before the start of the service you want to monitor. Otherwise, you'll need to restart the service to enable OneAgent injection.

Operation not permitted

If you see an `Operation not permitted` error in the Linux console or the installation logs, make sure that OneAgent installation isn't blocked by antivirus software installed on the host.

OneAgent communication issues with SELinux enabled

OneAgent supports SELinux only when the targeted policy is loaded, the multi-level security policy is not supported. If you attempt to install OneAgent on a system where SELinux with multi-level security mode policy, you will get the following error message: `Installation with SELinux loaded in multi-level security mode is not supported. Dynatrace OneAgent may not work correctly.`

If you are using a system with SELinux in enforcing mode and injected OneAgents are failing to communicate, yet communication works just fine for the OneAgent OS module, try the following actions. Note that the example below is based on the `httpd` process, but this can also happen for NGINX and other processes.

1. Check `/var/log/audit/audit.log` or `journalctl` for denials, for example:

   ```
   # grep type=AVC /var/log/audit/audit.log



   # journalctl --utc -a -t "audit"
   ```
2. If you find a denial for the process in question, for example:

   ```
   type=AVC msg=audit(1535366769.867:209537): avc:  denied  { name_connect } for  pid=8348 comm="httpd" dest=9999 scontext=unconfined_u:system_r:httpd_t:s0 tcontext=system_u:object_r:jboss_management_port_t:s0 tclass=tcp_socket`
   ```

   first, check if SElinux allows the communication using the following command:

   ```
   # sesearch -AC -s httpd_t -t jboss_management_port_t
   ```

   To interpret the command output, see [Using SELinux booleansï»¿](https://wiki.gentoo.org/wiki/SELinux/Tutorials/Using_SELinux_booleans).
3. To find out if the communication is not allowed, execute the following command:

   ```
   # setsebool -P httpd_can_network_connect on
   ```

   The command will persistently (retained across host reboots) enable the `httpd_can_network_connect` SELinux boolean, allowing OneAgent to be injected into the `httpd` process to establish connection to ActiveGate.
4. Restart the process and verify that the communication works.

OneAgent on NFS drives

OneAgent on Linux was reported to be unstable when deployed on poor quality NFS drives. In order for the automatic injection and automatic updates to work properly, ensure that your OneAgent deployment meets the following recommendations:

#### Custom installation path

Customize OneAgent installation so that it's not located in the NFS directories (the default OneAgent location is `/opt/dynatrace`). Use the OneAgent `INSTALL_PATH` parameter. For more information, see [Customize OneAgent installation on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.").

#### Runtime path

Ensure that the runtime path `/var/lib/dynatrace/oneagent` is not located in NFS directories.

#### Filesystem availability

Filesystem availability is critical not only for OneAgent monitoring, but also for startup of any processes on the host. Even if you customize OneAgent installation, it still creates symbolic links to `/opt/dynatrace` for its deep monitoring modules and automatic injection. Make sure that `/opt/dynatrace` is available during system startup as early as possible. OneAgent starts up relatively early, so `/opt/dynatrace` needs to be available as early in the startup process as possible.

#### Stopping processes for OneAgent update

If, in the presence of NFS, you observe OneAgent update problems, make sure to stop any processes that may have OneAgent deep code monitoring modules enabled before you start OneAgent update.

#### FUSE not supported

Any file system that relies on FUSE is not supported.

We're working on fixing the NFS-deployment-related issues, so you can expect these guidelines to evolve over time.

Splunk incompatibility

The `splunkd` component of Splunk version 8.2+ crashes when OneAgent automatic injection is enabled.

#### Problem

According to [Splunk issue SPL-207550ï»¿](https://docs.splunk.com/Documentation/Splunk/8.2.1/ReleaseNotes/Knownissues) (external link), Splunk fails to start after installation on Linux if a Dynatrace OneAgent exists, with error `ERROR: pid XXXX terminated with signal 4 (core dumped)`, because there is a conflict between the splunk watchdog and Dynatrace OneAgent libraries.

#### Workaround

Set the following in `server.conf`, `[watchdog]`:  
`usePreloadedPstacks = false`

Compatibility with antivirus software

Blocking mutex in the Linux kernel can cause CrowdStrike Falcon to block OneAgent when reading the process data from `/proc`, which contains one subdirectory per process running on the system.

* When OneAgent tries to read `/proc/<pid>`, CrowdStrike Falcon blocks mutex in the kernel for process ID directory creation. OneAgent will be in uninterruptible state, which means you can clear the processes only by rebooting the server or waiting for the I/O to respond.
* OneAgent installation can be affected at any time due to the lack of a single rule that causes the issue.

Oracle Database Server 19c does not respond

#### Problem

OneAgent auto instrumentation is not possible when Oracle Database Server 19c is installed, due to incompatibility with OneAgent Process Module.

#### Details

OneAgent Process Module requires basic functionality from system `libc` library to perform auto instrumentation. When another product overrides the functionality (`__errno_location` function in this case), the Process Module is unable to distinguish between the symbol provided by `libc` and the product. Calling the symbol provided by the product results in a crash, as it is not yet initialised at the time.

#### Scope

Linux hosts with Oracle Database Server 19c

#### Solution

Any one of the below options is sufficient:

* Use Oracle Database Server 21c or newer
* Disable Process Agent injection via `oneagentctl --set-auto-injection-enabled false`
* Run the following snippet and replace `[PATH-TO-DATABASE-EXECUTABLE]` with the path to your Oracle Database 19c executable

  ```
  unshare -m -- sh -c 'mount --bind /dev/null /etc/ld.so.preload && [PATH-TO-DATABASE-EXECUTABLE]'
  ```
* Set the `LD_AUDIT` environment variable so it applies to the Oracle Database at start up. For more information including specific steps, see [Preventing loading of the process module on Linuxï»¿](https://community.dynatrace.com/t5/Troubleshooting/Preventing-loading-of-the-process-module-on-Linux/ta-p/213303).
* Disable Process Agent injection via `builtin:host.monitoring.advanced` schema / UI. ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Warning This will disable all code modules on that host, including manually enabled code modules.

If there are any processes on the hosts which require Code Module injection, they can be manually enabled via LD\_PRELOAD=/lib{64}/liboneagentproc.so environment variable.
For further assistance, reach out to Dynatrace support specialists in chat.

### Windows

Compatibility with antivirus software

To ensure seamless functioning of OneAgent and to avoid overhead, we recommend excluding all files in the OneAgent installation directory from antivirus scan.

We also recommend that you configure your antivirus software so that it treats the OneAgent process as trusted and non-malicious. Refer to the documentation of your antivirus solution to learn how to do this.

If you're using McAfee, you may experience CPU overhead. To resolve this issue, set McAfee to **Exploit Prevention Compatibility Mode**.

1. Disable Self-Protection and Exploit Prevention in the ENS console.
2. Set these registry values as a DWORD:

   * `HKEY_LOCAL_MACHINE\SOFTWARE\McAfee\Endpoint\Ips\BO\dwBOCompatibilityMode=1`
   * `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\McAfee\EndPoint\Ips\BO\dwBOCompatibilityMode=1`
3. Re-enable Self-Protection and Exploit Prevention in the ENS console.

Processes not detected?

One of the following may have occurred

* The process isnât supported by our monitoring technology. You can check which [process types Dynatrace supports](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* The process isnât working on your server. Make sure your servers are running and that the processes are operational.
* There is delay in communication between Dynatrace and your OneAgent. If this is the case, wait a few moments and try again.
* Your OneAgent isnât working properly. Go to **Settings** > **Monitoring** > **Monitoring overview** to confirm that monitoring is enabled for the host running your software.

If you're still unable to resolve this issue, contact a Dynatrace product expert via live chat within your Dynatrace environment. Also, consider installing OneAgent on a different machine.

How can I repair OneAgent installation?

The OneAgent Windows installer doesn't support the modify and repair operations. You can't reinstall OneAgent using the same installer version as the installed OneAgent.

To reinstall OneAgent on Windows, either uninstall it and then reinstall it, or install a newer version over the existing version.

Failed OneAgent update due to missing MSI package in Windows Installer Cache

OneAgent Windows installer utilizes the Windows Installer Cache, which is located by default at `C:\Windows\Installer`. It stores important files required for uninstalling and updating the product. If you encounter log entries similar to the following in the installation log (default location: `C:\ProgramData\dynatrace\oneagent\log\installer\installation_msiexec_*.log`):

```
MSI (s) (C0:E4) [09:27:14:308]: Warning: Local cached package 'C:\Windows\Installer\312c0.msi' is missing.



...



Error 1714. The older version of Dynatrace OneAgent cannot be removed.  Contact your technical support group.  System Error 1612.



MSI (s) (C0:54) [09:27:56:489]: Product: Dynatrace OneAgent -- Error 1714. The older version of Dynatrace OneAgent cannot be removed.  Contact your technical support group.  System Error 1612.
```

Try the following steps to resolve the issue:

1. Download and unpack the MSI package from the installer of the currently installed version by following the [Get MSI Package](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#msi "Learn how to download and install Dynatrace OneAgent on Windows.") instructions.
2. Copy the MSI package to `C:\Windows\Installer`, and rename it to match the name referenced in the log (in this example, `312c0.msi`).

For more information, see [Missing Windows Installer cache requires a computer rebuildï»¿](https://dt-url.net/gs03u5l).

AI\_RecycleBin folder is filling up disk space

This is a known issue with [Advanced Installerï»¿](https://dt-url.net/e303ta4). As a workaround, the OneAgent installer clears the `AI_RecycleBin` at the end of the installation. However, this cleanup might not work if the installation fails in an early stage, such as in the case of a [missing MSI package in Windows Installer Cache](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#missing-msi "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows."). For more details, see the discussion on [Advanced Installer forumsï»¿](https://dt-url.net/w503uks).

### AIX

Injection not working due to manual configuration of previous version

If you used OneAgent for AIX prior to version 1.137 you may have configured it via `JAVA_OPTS` using the `dynatrace-java-env.sh` script. You need to remove this prior to using the unified monitoring scripts `dynatrace-agentXX.sh`.

* Make sure that `dynatrace-java-env.sh` isn't called anywhere in your shell when you use the `dynatrace-agentXX.sh` script.
  `dynatrace-java-env.sh` is deprecated and should only be used as a fallback.
* Check for and remove the following parameter from your Java command line or startup scripts (specific directory may vary):

  `-agentpath:/opt/dynatrace/oneagent/agent/lib64/liboneagentloader.so`

LDR\_PRELOAD64: parameter not set

You may encounter an error like this when you use `dynatrace-agentXX.sh` in a shell script.

```
Info: using DT_HOME: /opt/dynatrace/oneagent



.profile[33] LDR_PRELOAD64: parameter not set
```

This happens if you use `set -u` to treat unset variables and parameters as errors. The `dynatrace-agentXX.sh` script exports variables which, though they may not yet exist in your script, are nevertheless needed and key to proper operation. To overcome this, call `set +u` ahead of the `dynatrace-agentXX.sh` script.

```
# avoid error



set +u



export DT_HOME=/opt/dynatrace/oneagent



. $DT_HOME/dynatrace-agent64.sh
```


---
