---
title: Multi-environment deployment of ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support
---

# Multi-environment deployment of ActiveGate

# Multi-environment deployment of ActiveGate

* 4-min read
* Updated on Feb 24, 2026

If you've set up several monitoring environments, it might be cumbersome to install and maintain multiple ActiveGates. Therefore, Dynatrace enables you to configure a single ActiveGate in support of multiple monitoring environments. Such an ActiveGate is referred to as a **multi-environment ActiveGate**.

This kind of configuration significantly reduces the maintenance and setup overhead. Thanks to this feature, you don't need to deploy multiple ActiveGates and don't need to adjust firewall settings for each additional Environment ActiveGate. Multi-environment ActiveGates are capable of handling all traffic from all the environments they are associated with.

Limitations

You **cannot** use an Environment ActiveGate configured for multi-environment support to:

* **Connect to environments from different clusters**
* Install the [zRemote module for z/OS monitoring](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.")
* Monitor remote technologies with the [Extensions framework](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* Execute monitors from [private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.")
* Run [Database insights](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Learn how to extend your database monitoring to the database infrastructure layer.")

All other ActiveGate features are supported.

[Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") are not supported on multi-environment ActiveGates or Cluster ActiveGates. To run Extensions, deploy a dedicated Environment ActiveGate for each environment and enable the [Extension Execution Controller (EEC)](/managed/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").

To configure an existing Environment ActiveGate for multi-environment support

1. **Make sure that the ActiveGate modules that are incompatible with multi-environment operation are disabled.** Which module is actually installed and enabled varies based on the [purpose](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") for which the ActiveGate was originally installed. Only one of the following modules can be present on the ActiveGate. However, if in doubt, disabling (and then removing) all of these particular modules at this point is acceptable:

   * ActiveGate Extensions—disabled in the `[extension_controller]` section
   * zRemote—disabled in the `[zremote]` section
   * Synthetic 1.0—disabled in the `[synthetic]` section

   agctl

   custom.properties

   ActiveGate version 1.333+

   You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Learn how to use agctl to configure and manage ActiveGate from the command line") to disable incompatible modules:

   ```
   agctl modules disable rpm,zremote,synthetic,extension_controller
   ```

   To disable the modules manually, locate the `custom.properties` file in the [configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), and make sure that the corresponding configuration properties are set to `false`:

   ```
   [rpm]



   rpm_enabled = false



   [zremote]



   zremote_enabled = false



   [synthetic]



   synthetic_enabled = false



   [extension_controller]



   extension_controller_enabled = false
   ```
2. **Make sure that the ActiveGate modules that are incompatible with multi-environment operation have been uninstalled.**

   * For Linux—execute one of the following commands, depending on which module needs to be uninstalled. If in doubt, execute all of the commands: If the commands are found, the respective modules will be uninstalled. If the commands are not found, it means that the modules are not present:

     ```
     sudo /opt/dynatrace/remotepluginmodule/uninstall.sh



     sudo /opt/dynatrace/zremote/uninstall.sh



     sudo /opt/dynatrace/synthetic/uninstall.sh
     ```
   * For Windows: locate and uninstall the following applications, if installed:

     + **Dynatrace Remote Plugin Module** (Extensions 1.0 only, not present in ActiveGate 1.301+)
     + **Dynatrace ZRemote**
     + **Dynatrace Synthetic**
3. **In the ActiveGate [configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), locate the `authorization.properties` file and familiarize yourself with the content.**  
   The `authorization.properties` file defines ActiveGate authorization for each environment as identified by the [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments."). ActiveGate authorizes via [tenant token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") and [individual ActiveGate token](/managed/ingest-from/dynatrace-activegate/activegate-security "Secure ActiveGates with dedicated tokens.").
   **One and only one of the sections will contain the property `mainTenant = true`.** This is for the environment from which the ActiveGate was downloaded and installed. **Do not remove this section or this entry.** Do not remove any other sections—relating to other environments—unless you do not want the ActiveGate to support those particular environments anymore.

   Format of the entries in `authorization.properties`:

   ```
   [<environment_ID>]



   tenantToken = <tenant_token>



   mainTenant = true     # identifies environment from which the ActiveGate was downloaded



   authToken = <individual_ActiveGate_token>
   ```

   For example:

   ```
   [mySampleEnv]



   tenantToken = abcdevjhij1234567890



   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJIHGFEDCBA01234567890ABCDEFGHIGKLMNOPQ



   mainTenant = true
   ```
4. **To create an individual ActiveGate token, see [Generate ActiveGate token](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.")**.
5. **To add more environments, add new sections to the `authorization.properties` file.**  
   List each Dynatrace environment you want the Environment ActiveGate to support. Use the following format:

   ```
   [<environment_ID>]



   tenantToken = <tenant_token>



   mainTenant = true



   authToken = <individual_ActiveGate_token>



   [<environment_ID>]



   tenantToken = <tenant_token>



   authToken = <individual_ActiveGate_token>
   ```

   For example:

   ```
   [mySampleEnv]



   tenantToken = abcdevjhij1234567890



   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJIHGFEDCBA01234567890ABCDEFGHIGKLMNOPQ



   mainTenant = true



   [myAnotherEnv]



   tenantToken = 0987654321jijvedcba



   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJZYXWVUTSRQPONMLKJIHGFE56GHMNO890ZABCD
   ```

   Ensure consistent configuration

   For correct operation, you must ensure that:

   * All environments that are to be supported by the same Environment ActiveGate run on the same Dynatrace Cluster.
   * The main environment, associated with the `mainTenant` configuration property, is correctly configured. Incorrect configuration of the main environment will result in the **rejection of the ActiveGate in all configured environments**: An error will be logged in the ActiveGate logs, with information stating that `mainTenant` configuration is invalid, and the ActiveGate will not appear on the Deployment Status pages on any of the environments.
6. **Save the `authorization.properties` file and [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").**
7. **Verify that the new environments have been added successfully.**  
   The [ActiveGate log file](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") should contain the entry listing the number of environments that the ActiveGate is working with, for example:

   ```
   Working mode is set to MULTITENANT with 5 tenant(s).
   ```

   If the log message does not list the number of environments that you have attempted to configure, scan the log file for entries indicating an error in the `authorization.properties` file. Error messages appear in this form:

   ```
   Error during parsing config file `...\conf\authorization.properties` - invalid configuration: ...
   ```