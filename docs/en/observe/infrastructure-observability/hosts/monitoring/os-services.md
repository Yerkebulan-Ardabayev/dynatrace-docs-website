---
title: OS services monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring/os-services
scraped: 2026-02-06T16:31:57.431344
---

# OS services monitoring

# OS services monitoring

* How-to guide
* 14-min read
* Updated on Jan 14, 2026

Dynatrace provides out-of-the-box availability monitoring of OS services.

You can monitor hosts in full-stack monitoring mode or use lightweight monitoring modes. For more information, see [Infrastructure and Discovery monitoring modes](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Find out what's included in Dynatrace Infrastructure Monitoring mode.").

## Requirements

* Linux systemd version 230+ is required on the monitored host to monitor relations between processes and OS services.
* Linux systemd version 250+ is required on the monitored host for improved OS services detection performance by less frequent refreshes.

## OS services alerting options

Depending on your monitoring requirements, you can choose between basic or advanced alerting of OS services. The Discovery mode allows only basic alerting, while the Full-Stack and Infrastructure monitoring modes also allow advanced alerting.

### 1. Basic alerting (Service status)

Basic alerting provides insight only into the service status. The system will monitor an OS service's current status and alert you when it changes from running to failed.

With the service status property in ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment."), you can query the current status of the service.

#### Example

```
fetch `dt.entity.os:service`



| fieldsAdd status
```

![Service status - Basic monitoring](https://dt-cdn.net/images/os-service-status-dashboard-example-light-919-5bd9bbe242.png)

If the alert is enabled, events and problems are created when a service status changes, such as when a service goes from running to failed. For more details, refer to [Host availability](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability "Check host availability, interpret host availability states, and see how maintenance windows are reflected in host availability charts.").

#### Failed service alert

![Failed service alert](https://dt-cdn.net/images/os-service-failed-1486-77d0ea5343.png)

### Advanced alerting (Service availability metric)

Advanced alerting provides access to the service status and the service availability metric. In addition to OS service status changes, you get more granular information about service availability on a per-minute basis. This enables more complex business logic, for example, if you want to be notified if a service is stopped for longer than 10 minutes. You can create alerting rules to monitor availability and trigger an alert when needed.

#### Example

```
timeseries count(dt.osservice.availability),



by:{dt.osservice.display_name, dt.osservice.status}



| filter dt.osservice.display_name=="apache2"
```

![Service status - Advanced monitoring](https://dt-cdn.net/images/os-service-availability-dashboard-example-light-1148-5dde972c54.png)

## Monitor a service

To monitor an OS service, perform the following steps.

1. Access OS services monitoring

In Dynatrace, go to **OS services monitoring** for the level you are configuring.

* Settings are defined at the environment level.
* The host group level inherits all settings from the environment.
  Additionally, you can add configurations for specific host groups.
* The host level inherits all settings from the host group.
  Additionally, you can add configurations for specific hosts.

### Environment level

Go to **Settings** > **Collect and capture** > **Infrastructure** > **OS** > **OS services monitoring**.

### Host-group level

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **OS services monitoring**.

### Host level

1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **OS services monitoring**.

2. Add service monitoring policy

Based on the service state and the rules, the service monitoring policy defines the way Dynatrace is monitoring your service. By default, Dynatrace comes with `Auto-start Windows OS Services` and `Auto-start Linux OS Services` policies for auto-started Windows and Linux services with failed status.

Limits

Note that the default limit of OS Service entities is 100,000 per cluster.
In larger environments with many hosts, we recommend creating precise rules that match only the important services for your infrastructure. Creating rules that are too general (for example, matching all services on thousands of hosts) may result in reaching the limit (entity explosion), leading to the disappearance of OS services from Dynatrace.
Also, `Auto-start Windows OS Services` and `Auto-start Linux OS Services` can be used as a starting point for further refining the policies.

The order of service monitoring policies is important. Policies that are higher on the list will proceed before those on lower positions until they are fulfilled. This allows for the creation of selective alerts or monitoring with minimal policies. For example, if you want to monitor all auto-started services and not just those created by Microsoft, you need to add a policy with disabled alerting and/or monitoring that will verify if the manufacturer is Microsoft.

1. On **OS services monitoring** for the level you are configuring based on your OS, select **Add policy** and define the policy, which is a collection of rules.
2. **System**: select your operating system.
3. **Rule name**: enter the name that will be displayed in the **Summary** field.
4. **Monitor**: decide whether you want to monitor service availability using the **OS service availability** (`builtin:osservice.availability`) metric. If available, the metric sends the service status every 10 seconds. The status is carried by the [**Service status**](#service-status) (`dt.osservice.status`) dimension.  
   Note that the metric consumes data points. For more information, see [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
5. **Alert**: decide whether you want alerting for your policy.
6. OneAgent version 1.257+ **Alert if service is not installed**: whether you want to receive alerts about OS services that are not installed on the host.
7. **Service status**: set the service status for which an alert should be triggered.

   Windows

   Linux

   You can use logic operations to monitor the service status. For example, `$eq(running)` monitors the running service state.

   Available logic operations:

   * `$not($eq(paused))` â Matches services that are in state different from paused.
   * `$or($eq(paused),$eq(running))` â Matches services that are either in paused or running state.

   These are the service statuses you can monitor. Use one of the following values as a parameter for this condition:

   * `running`
   * `stopped`
   * `start_pending`
   * `stop_pending`
   * `continue_pending`
   * `pause_pending`
   * `paused`

   You can use logic operations to monitor the service status. For example, `$eq(active)` monitors the active service state.

   Available logic operations:

   * `$not($eq(active))` â Matches services with state different from active.
   * `$or($eq(inactive),$eq(failed))` â Matches services that are either in inactive or failed state.

   These are the service statuses you can monitor. Use one of the following values as a parameter for this condition:

   * `reloading`
   * `activating`
   * `deactivating`
   * `failed`
   * `inactive`
   * `active`
8. Optional OneAgent version 1.257+ **Alerting delay**: the number of 10-second measurement cycles for a service to be in configured state before an event is generated. This doesn't apply to alerts for services that are not installed.

Next, you need to select which services you want to monitor based on service properties.

3. Select services you want to monitor

1. Select **Add rule**.
2. Optional **Rule scope**: select either **OS Service** or **Host**. By default, the **OS Service** option is selected.

If you selected **Host**:

* OneAgent version 1.277+ **Custom metadata** used for matching:

  + **Key** specifies the metadata key you want to match
  + **Condition** in which you can define a string that:

    - Dynatrace version 1.310+ `$match(ver*_1.2.?)` â Matches string with wildcards. Use `*` for any number of characters (including zero) and `?` for exactly one character.
    - `$contains(production)` â Matches if production appears anywhere in the host metadata value.
    - `$eq(production)` â Matches if production matches the host metadata value exactly.
    - `$prefix(production)` â Matches if production matches the prefix of the host metadata value.
    - `$suffix(production)` â Matches if production matches the suffix of the host metadata value.

    Available logic operations:

    - `$not($eq(production))` â Matches if the host metadata value is different from production.
    - `$and($prefix(production),$suffix(main))` â Matches if host metadata value starts with production and ends with main.
    - `$or($prefix(production),$suffix(main))` â Matches if host metadata value starts with production or ends with main.

    When including special characters such as brackets `(` and `)` within your matching expressions, escape these characters with a tilde `~`. For example, to match a metadata value that includes brackets, like `my(amazing)property`, you would write `$eq(my~(amazing~)property)`.

    Conditions are case insensitive.

If you selected **OS Service**, proceed according to your operating system.

Windows

Linux

* **Service property** used for matching:

  + **Display name** visible for system user.
  + **Path** to the binary used by OS service.
  + **Manufacturer** from the binary file of the service.
  + **Service Name**
  + **Startup Type**

A monitoring rule may consist of multiple detection rules. All detection rules must be satisfied for the OS Service to match, as a logical `AND` operation is applied across all specified conditions.

Additional information on Display name, Path, Manufacturer, and Service Name

With these properties, we define the services to be monitored based on:

* Display name visible to a system user
* Path to the service binary
* Manufacturer of the service
* Service name representing the name or ID under which OS service is recognized
* **Condition** in which you can define a string that:

  + Starts with â use `$prefix` qualifier, for example `$prefix(ss)`.
  + Ends with â use `$suffix` qualifier, for example `$suffix(hd)`.
  + Equals â use `$eq` qualifier, for example `$eq(sshd)`.
  + Contains â use `$contains` qualifier, for example `$contains(ssh)`.
  + Dynatrace version 1.310+ Matches â use `$match` qualifier, for example `$match(ip?tables*)`, where `*` matches any number of characters (including zero) and `?` matches exactly one character.

  Available logic operations:

  + `$not($eq(sshd))` â Matches if the service's property value is different from `sshd`.
  + `$and($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` and ends with `hd`.
  + `$or($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` or ends with `hd`.

  When including special characters such as brackets `(` and `)` within your matching expressions, escape these characters with a tilde `~`. For example, to match a property value that includes brackets, like `my(amazing)property`, you would write `$eq(my~(amazing~)property)`.

  Conditions are case insensitive.

Additional information on Startup Type

With this property we define the services to be monitored based on their startup type.

* **Condition** in which you can define a string that:

  + Equals â use `$eq` qualifier, for example `$eq(manual)`.

  Available logic operations:

  + `$not($eq(auto))` â Matches services with startup type different from Automatic.
  + `$or($eq(auto),$eq(manual))` â Matches if service's startup type is either Automatic or Manual.

  Use one of the following values as a parameter for this condition:

  + `manual` for Manual - the service starts only if needed or if you invoke something to start the service.
  + `manual_trigger` for Manual (Trigger Start) - the service starts along with the startup of another service.
  + `auto` for Automatic - the service starts automatically.
  + `auto_delay` for Automatic (Delayed Start) - the service startup is delayed until the system has finished booting.
  + `auto_trigger` for Automatic (Trigger Start) - the service starts automatically on startup and may be started or stopped due to certain operating system events.
  + `auto_delay_trigger` for Automatic (Delayed Start, Trigger Start)
  + `disabled` for Disabled

**Service property** used for matching:

* **Service Name**
* **Startup Type**

Additional information on Service Name

With this property we define the services to be monitored based on the service name.

**Condition** in which you can define a string that:

* Dynatrace version 1.310+ `$match(ip?tables*)` â Matches string with wildcards. Use `*` for any number of characters (including zero) and `?` for exactly one character.
* `$contains(ssh)` â Matches if `ssh` appears anywhere in the service's property value.
* `$eq(sshd)` â Matches if `sshd` matches the service's property value exactly.
* `$prefix(ss)` â Matches if `ss` matches the prefix of the service's property value.
* `$suffix(hd)` â Matches if `hd` matches the suffix of the service's property value.

Available logic operations:

* `$not($eq(sshd))` â Matches if the service's property value is different from `sshd`.
* `$and($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` and ends with `hd`.
* `$or($prefix(ss),$suffix(hd))` â Matches if service's property value starts with `ss` or ends with `hd`.

Additional information on Startup Type

With this property, we define the services to be monitored based on their startup type.

**Condition** in which you can define a string that:

* `$eq(enabled)` â Matches services with startup type equal to enabled.

Available logic operations:

* `$not($eq(enabled))` â Matches services with startup type different from enabled.
* `$or($eq(enabled),$eq(disabled))` - Matches services that are either enabled or disabled.

Use one of the following values as a parameter for this condition:

`enabled`, `enabled-runtime`

The service is marked as ready for startup.

`static`

The unit file is not enabled and has no provisions for enabling in the install unit file section. Static units are installed as dependencies and can only be masked, but are not always executed. They will be executed only if another unit depends on them or if they're manually started.

`disabled`

The unit file is not enabled, but it contains an install section with installation instructions.

4. Add custom properties

OneAgent version 1.247+

Dynatrace version 1.247+

Optional

1. Select **Add property** to specify a custom key-value property for the policy.

   Custom message in the Event details

   For example, a property with a **Key** set to `custom.message` and **Value** set to `The {dt.osservice.name} is with status {dt.osservice.status}` (including placeholders `{dt.osservice.name}` and `{dt.osservice.status}`) will extract the OS service name and status values once the rule is triggered. If the placeholder substitution fails, both the key and the value will be unavailable.

   ![os-service-custom-message](https://dt-cdn.net/images/screenshot-2022-09-02-at-11-00-08-665-79313a8bcc.png)

   ![os-service-custom-message-in-event](https://dt-cdn.net/images/screenshot-2022-09-02-at-11-45-39-991-335a005b28.png)

   For OneAgent version 1.255+, the `{dt.osservice.display_name}` placeholder is available.

   Additionally, you can utilize specific dt flags in the **Key** field to tailor the behavior of problem notifications and Davis AI analysis:

   * `dt.event.title`: Customizes the title of the problem.
   * `dt.event.description`: Provides a detailed description for the problem.
   * `dt.event.allow_davis_merge`: Controls how Davis AI decides to merge events, based on your settings.
2. Select **Save changes**.

## Manage monitored OS services

To manage the OS services

1. In Dynatrace, go to **OS services monitoring** for the level you are configuring.

   Host level

   1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
   2. Find and select your host to display the host overview page.
   3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

   4. In the host settings, select **OS services monitoring**.

   Host-group level

   1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
   2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
   3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

      The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

      The **Host group** property is not displayed when the selected host doesn't belong to any host group.
   4. Select the host group name in any row.

      As you have filtered by host group, all displayed hosts go to the same host group.

   5. In the host group settings, select **OS services monitoring**.

   Environment level

   Go to **Settings** > **Monitoring** > **OS services monitoring**.
2. The OS services you monitor are displayed in a table under the **Add policy** button.

   * To stop monitoring a listed service, turn the **Enabled** setting off.
   * To delete a service from the table, select the delete button in the **Delete** column
   * To view and edit details, select the expand control in the **Details** column.

## Monitor service availability

Dynatrace version 1.243+

OneAgent version 1.243+

The [Host overview](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") page contains the **OS services analysis** section listing the OS services for which any policy (with active alerting or monitoring) is fulfilled.

1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Select any host to go to its overview page.
3. In the **OS services analysis** section, select the service name to open the **Service overview** page.

For more information, see [OS services analysis](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#os-services "Monitor hosts with Dynatrace.").

## Configure at scale using Settings API

You can use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure your service availability monitoring at scale.

1. To learn the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:os-services-monitoring` as the schemaId.
2. Based on the `builtin:os-services-monitoring` schema, create your configuration object.
3. To create your configuration, use [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

## Limitations

On Linux, systemd OS services with the following startup types are supported:

* `enabled`
* `enabled-runtime`
* `static`
* `disabled`
* `indirect`