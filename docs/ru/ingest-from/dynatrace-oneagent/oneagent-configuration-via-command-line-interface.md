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