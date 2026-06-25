---
title: Configurable properties of Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configurable-properties-of-dynatrace-managed
scraped: 2026-05-12T11:52:58.100050
---

# Configurable properties of Dynatrace Managed

# Configurable properties of Dynatrace Managed

* Updated on Nov 04, 2025

The configurable Dynatrace Managed properties are stored in the `/opt/dynatrace-managed/server/conf/config.properties` file, but do not edit them in that file. It is overwritten during an update.

If you configure properties directly in `/opt/dynatrace-managed/server/conf/config.properties`, **your custom configuration won't be preserved during an update**.

Instead of editing `/opt/dynatrace-managed/server/conf/config.properties`, make all your edits in the `custom.settings` file located in the `/opt/dynatrace-managed/installer` directory of each cluster node. You can create the file if it doesn't already exist. During an upgrade, the installer reads `custom.settings` and modifies `config.properties` accordingly.

The `custom.settings` file specifies:

* The location of the file to be modified
* The section to modify
* The property and value to be set

## Example custom.settings edits

Suppose you have made two modifications to settings:

* Set the `connection-timeout` property to `3000000`
* Set the `proxy-off` property to `true`

To preserve these settings during upgrade:

1. Open the `custom.settings` file for editing.

   * File location: `/opt/dynatrace-managed/installer` directory of the cluster node.
   * Create the file in that location if it does not already exist.
2. Add one line to specify the configuration file to modify during the install.

   ```
   <server/conf/config.properties>
   ```

   Be sure to include the chevrons (`<` and `>`).
3. Add two lines to specify the section, property name, and property value to be modified for `connection-timeout`, which is in the `[settings]` section.

   ```
   [settings]



   connection-timeout=3000000
   ```
4. Add two lines to specify the section, property name, and property value to be modified for `proxy-off`, which is in the `[http.client.external]` section.

   ```
   [http.client.external]



   proxy-off = true
   ```
5. The resulting `custom.settings` file for this example should now look like this:

   ```
   <server/conf/config.properties>



   [settings]



   connection-timeout=3000000



   [http.client.external]



   proxy-off = true
   ```

With this `custom.settings` file placed on all of the cluster nodes in the `/opt/dynatrace-managed/installer` directory, every time you upgrade the node the installer will set `connection-timeout` to `3000000` and `proxy-off` to `true` in the `config.properties`, thus preserving your custom configuration.

Applies to service restarts

Dynatrace Managed also executes this custom configuration action with each restart of the Dynatrace service.