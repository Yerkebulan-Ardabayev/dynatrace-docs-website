---
title: Customize OneAgent installation on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux
scraped: 2026-02-28T21:10:36.046969
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