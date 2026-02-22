---
title: Install OneAgent on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris
scraped: 2026-02-22T21:11:56.821720
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