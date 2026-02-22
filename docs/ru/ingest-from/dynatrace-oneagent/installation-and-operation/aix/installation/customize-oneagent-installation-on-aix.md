---
title: Customize OneAgent installation on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix
scraped: 2026-02-22T21:11:47.444632
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