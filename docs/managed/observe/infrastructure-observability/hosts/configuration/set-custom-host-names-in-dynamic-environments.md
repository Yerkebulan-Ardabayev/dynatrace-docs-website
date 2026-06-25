---
title: Set custom host names
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments
scraped: 2026-05-12T11:22:14.203101
---

# Set custom host names

# Set custom host names

* How-to guide
* 5-min read
* Published Dec 18, 2017

Dynatrace automatically identifies and monitors the infrastructure on which itâs deployed, including all detected hosts. It detects hosts, technologies, locations, services, applications, and dependencies between those entities. Every hosts gets a name automatically.

However, detected host names can be unintuitive or confusing, especially within large and dynamic deployments that include frequently changing host instances and names (for example, within AWS, Azure, or Google Cloud).

To help you out with this, Dynatrace lets you rename hosts manually and programmatically so you see more human-friendly names in the Dynatrace web interface.

This functionality offers you ways to apply a more readable or useful display name to a host.

* If you [apply a naming rule](#rule) in your environment, for every host that matches the rule criteria, the host's custom name will be displayed on the **Hosts** page, host details page, host processes page, host networking page, and so on.
* Exception to the above: you can [manually override naming rules](#manual) on any host, in which case the manually provided host name is displayed instead of the rule-based name.
* You can also use the [oneagentctl command-line tool](#oneagentctl) to set a custom host name.
* Regardless of how you set a custom name, however, **the detected name remains unchanged**.

See below for details.

## Rename one host manually

If you're monitoring a relatively static environment in which host instances are stable, you can enter a custom host name on the **Host settings** page for the selected host.

1. Go to **Hosts** and select a host.
2. On the host details page, select **More** (**â¦**) > **Settings** in the upper-right corner.
3. On the **General** page, type a new **Host name**.

* If you need to revert the name change, select the **Reset name to detected** link that is displayed on the **Host settings** page after renaming a host.
* A host name set manually overrides any applicable naming rules.

## Rename multiple hosts automatically

You can create one or more host naming rules in Dynatrace to automatically rename monitored hosts that match the rules.

* Keep in mind that any new naming rules will apply to already detected hosts that are active and online.
* A host name that has been set manually (see previous section) overrides all naming rules. To make naming rules apply to a host whose name has been manually changed, first revert the manual name change by selecting the **Reset name to detected** link on the **Host settings** page.

To create a host naming rule that will be applied automatically to all matching hosts

1. Go to **Settings** > **Monitoring > Host naming**.
2. On the **Host naming** page, select **Add a new rule**.
3. Enter a **Rule name**.
4. Set **Host name format** to the name you want to display. This can include:

   * Static text that you type or paste into the box.
   * Placeholders that you select from the list that is automatically displayed when you select in the edit box.

   Example: type `CPU cores =`  and then select the `{Host:CpuCores}` placeholder from the edit box list. That would generate the host name `CPU cores = 8` for a host with 8 CPU cores.
5. Optional Under **Rule applies to entities matching the following properties**, focus your rule on a specific host group or technology.

   * Select a host group to apply the rule only to hosts in the selected host group.
   * Select a technology to apply the rule only to hosts running under a selected technology such as Kubernetes or OpenShift.
6. Optional Under **Conditions**, use the lists to build a condition for the naming rule.

   Example: to apply this rule only to Windows hosts

   * Select `OS type`
   * Select `equals`
   * Select `Windows`

   To add another condition, select **Add condition** and repeat this step.
7. Select **Preview** to list matching entities by the current **Name** and the **New name** that will be displayed after the rule is applied.

   * If the rule still needs work, edit the rule and then select **Preview** again to see the changes.
   * If you are satisfied with the preview list, select **Create rule**.
8. Optional To add another rule, repeat the procedure.

## Rename with command-line tool

OneAgent version 1.189+

Use the `oneagentctl` command-line tool with the `--set-host-name` parameter to override an automatically detected host name. A host name must not contain the `<`, `>`, `&`, `CR` (carriage return), or `LF` (line feed) characters. The maximum length is 256 characters.

This command adds a custom host name to display in the UI, but the detected host name is not changed. For details, see [Set custom host names](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

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

Using `--set-host-name` requires restart of OneAgent. Add `--restart-service` to the command to restart OneAgent automatically (version 1.189+) or stop and start the OneAgent process manually. For OS-specific instructions, see [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), or [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

To show the host name:

* **Linux** or **AIX**:  
  `./oneagentctl --get-host-name`
* **Windows**:  
  `.\oneagentctl.exe --get-host-name`

For more information on `oneagentctl`, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Rename with configuration file

OneAgent version 1.187 and earlier

Use the configuration file only for OneAgent version 1.187 and earlier. For later versions, use the `oneagentctl` command-line tool as explained in the previous section.

To override an automatically detected host name using a configuration file

1. Create a simple `hostname.conf` file on the monitored host (must be OneAgent version 1.187 or earlier).

   * For Windows, create the file in `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
     Note that Unicode encoding is not available on Windows.
   * For Linux, create the file in `/var/lib/dynatrace/oneagent/agent/config`
2. Create a host naming rule in the `hostname.conf` file:

   Example:

   ```
   My App Server
   ```

After you restart the **Dynatrace OneAgent** service, Dynatrace will pick up the new host name and apply it to the host. Note that the host name entered on the **Host settings** page takes precedence over the name stored in the `hostname.conf` configuration file.