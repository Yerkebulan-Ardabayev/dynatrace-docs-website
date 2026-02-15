---
title: Troubleshooting OneAgent installation
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation
scraped: 2026-02-15T21:18:44.153552
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