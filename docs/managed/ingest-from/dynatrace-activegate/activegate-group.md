---
title: ActiveGate group
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-group
---

# ActiveGate group

# ActiveGate group

* 2-min read
* Updated on Feb 24, 2026

You can use ActiveGate groups to perform bulk actions on your ActiveGates, such as managing [Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") running on ActiveGates or connecting your [Cloud Foundry foundations](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.").

## Requirements

* The name of an ActiveGate group is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`).
* Dots are used as separators, so you must not use a dot as the first character of a group name.
* The length of the string is limited to 256 characters.

## Assign ActiveGate to a group

An ActiveGate can belong to only one group. By default, an ActiveGate is assigned to the `default` group. You can assign an ActiveGate to a group during or after installation.

### Assign to a group during installation

To assign an ActiveGate to a group, you can use the `--set-group` installation parameter during installation. Note that you can't use this parameter during an ActiveGate update. For example:

Linux

Windows

```
/bin/bash Dynatrace-ActiveGate-Linux-x86-<version>.sh --set-group=my-group
```

```
Dynatrace-ActiveGate-Windows-x86-<version>.exe --set-group=my-group
```

### Assign to a group after installation

To assign ActiveGates to a group, you can use [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify ActiveGate group** action).

Alternatively, you can assign an ActiveGate to a group using [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#group "Learn how to use agctl to configure and manage ActiveGate from the command line") or by editing the `custom.properties` file:

agctl

custom.properties

ActiveGate version 1.333+

```
agctl group set mygroup
```

After assigning the ActiveGate to a group with `agctl`, you need to [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

1. Edit the `custom.properties` file in the [ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") and configure the `group` parameter in the `[collector]` section. For example:

   ```
   [collector]



   group = mygroup
   ```

   For more information, see [Basic rules for working with ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#basic-rules "Learn which ActiveGate properties you can configure based on your needs and requirements.").
2. Save the `custom.properties` file and [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

## Extensions

An ActiveGate running a remote extension needs to belong to an ActiveGate group because Dynatrace uses a group to instruct the extension where it should run. If you plan to use a single ActiveGate to run a remote extension, assign it to a dedicated group containing only that ActiveGate.

When activating the extension, you need to specify an ActiveGate group that will run your extension. You can select an ActiveGate group either during the Dynatrace Hub-based activation workflow, or specify an ActiveGate group name in the JSON payload used to activate the extension using the Dynatrace API.

## Cloud Foundry foundations

When connecting Dynatrace to Cloud Foundry foundations, you specify an ActiveGate group responsible for querying Cloud Foundry for data. For more information, see [Connect your Cloud Foundry foundations with Dynatrace](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.")