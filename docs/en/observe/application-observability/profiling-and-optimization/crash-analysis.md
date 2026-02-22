---
title: Crash analysis
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization/crash-analysis
scraped: 2026-02-22T21:13:00.703508
---

# Crash analysis

# Crash analysis

* How-to guide
* 7-min read
* Published Jul 19, 2017

Processes crash for a multitude of reasons and itâs often difficult to understand the root causes that contribute to such crashes. When a monitored process crashes, youâll see a process crash entry in the **Events** section of each affected process and host page. The example process below has some availability problems (shown in red on the timeline). By selecting the affected timeframe in the timeline, the **Events** section shows you the number of process crashes that occurred during that timeframe (1 crash in this example).

![Event details](https://dt-cdn.net/images/event-details-3321-d2e1237b17.png)

Select **Process crash details** to view a detailed list of the crashes that occurred during the selected timeframe. Here youâll find all details related to why each process crashed.

![Process crash](https://dt-cdn.net/images/process-crash-1418-427d215ec4.png)

The provided crash details include the signal that killed the process (for example, `Segmentation fault` or `Abort`), the execution stack frame that crashed, and more. The crash typeâsuch as a native core dump, Java core dump, or abnormal program exit due to an exceptionâdetermines which crash details are available.

This functionality works for all processes on each monitored host.

## Analyze additional crash artifacts

Crash details often include a **Download** button that provides access to additional crash artifacts, such as `hs_err_pid` files for Java crashes, text files that provide analysis of Linux and Windows core dumps, or files containing the .NET, Java, or Node.js exceptions that were potentially responsible for the crashes. For example, the **Segmentation fault** crash report above resulted in a core dump. OneAgent analyzed the core dump automatically and then produced the following report as a log artifact:

```
dumpproc version 1.108.0.20161025-115919, installer version 1.108.0.20161025-121046



2016-11-09 18:00:44: Application 'CreditCardAutho', inner pid '15891', outer pid '0', signal: 'Segmentation fault' (11)



process group ID: 0x441b2cb89962033d



process group instance ID: 0xfe58bab23100f42c



process group Name: easytravel-*-x*



threadCount: 1



thread: 0 - stack range: 0x7ffeda572000-0x7ffeda594000, size: 136 kB



0x00007ffeda592be0 0x00007f4de477604d libpthread-2.15.so!<imagebase>+0xf04d



0x00007ffeda592bf0 0x00000000004038d8 CreditCardAuthorizationS64!main+0x1b8



0x00007ffeda592c60 0x00007f4de41c676d libc-2.15.so!__libc_start_main+0xed



0x00007ffeda592d20 0x000000000040329a CreditCardAuthorizationS64!<imagebase>+0x329a



mapped files:



0000000000400000-000000000041e000 0 /home/labuser/easytravel-2.0.0-x64/CreditCardAuthorizationS64 (MD5: da5992daf5ba3b76c633c853c7da5e87)



000000000051d000-000000000051e000 1d /home/labuser/easytravel-2.0.0-x64/CreditCardAuthorizationS64 (MD5: da5992daf5ba3b76c633c853c7da5e87)



00007f4de41a5000-00007f4de4359000 0 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de4359000-00007f4de4558000 1b4 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de4558000-00007f4de455c000 1b3 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de455c000-00007f4de455e000 1b7 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)



00007f4de4563000-00007f4de4565000 0 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4565000-00007f4de4765000 2 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4765000-00007f4de4766000 2 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4766000-00007f4de4767000 3 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)



00007f4de4767000-00007f4de477f000 0 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de477f000-00007f4de497e000 18 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de497e000-00007f4de497f000 17 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de497f000-00007f4de4980000 18 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)



00007f4de4984000-00007f4de4a02000 0 /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4a02000-00007f4de4c01000 7e /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4c01000-00007f4de4c03000 7d /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4c03000-00007f4de4c05000 7f /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)



00007f4de4cc0000-00007f4de4ce2000 0 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)



00007f4de4ee2000-00007f4de4ee3000 22 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)



00007f4de4ee3000-00007f4de4ee5000 23 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)
```

## Protect sensitive user data

Crash reports might include sensitive personal information that should not be viewed by all users. For this reason, your Dynatrace administrator must enable the [**View logs** account-security option](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") and the [**View sensitive request data**](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") permissions in your user profile before you can view personal data. This option is disabled by default for all non-admin users and must be explicitly enabled before you can access log contents.

## Crash handling on Windows

In order for a generic Windows process crash (core dump) to be visible to Dynatrace, the crash must be detected by Windows Error Reporting. For this reason, the Windows Error Reporting service must be enabled.

![Process crashes 6](https://dt-cdn.net/images/process-crashes6-1142-db9303969a.png)

When a crash occurs on Windows, a dialog appears, asking if you want to debug or close the crashed application. This is not desirable for headless systems. You can disable this dialog by adding a value to the registry, as shown below:

`[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting] "DontShowUI"=dword:00000001`

![Process crashes 8](https://dt-cdn.net/images/process-crashes8-880-1d0cfb52b5.png)

You can learn about other valuable settings related to Windows Error Reporting by visiting [Microsoft documentationï»¿](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513638(v=vs.85).aspx).

## Linux core dump handling

In Linux, the way the kernel handles the core dump is set in `/proc/sys/kernel/core_pattern`. Beginning with kernel 2.6.19 (1), there are two methods of dealing with application crashes. The core dump might be written to a file pointed to by the `/proc/sys/kernel/core_pattern` entry or pushed to an applicationâthe entry must be prefixed with a vertical slash character (`|`) character.

Because Suse Linux uses the first method, the entry is similar to
`/proc/sys/kernel/core_pattern:core`. This means that a file with the name `core` is written in the current working directory of the crashed process.

Ubuntu and Red Hat generally rely on their own tools to report crash dumps, so the lines appear as follows:  
`|/usr/share/apport/apport %p %s %c %P`  
or  
`|/usr/libexec/abrt-hook-ccpp %s %c %p %u %g %t e`

In the last example, when a program crashes, the `coredump` output is pushed to `stdin` of the application given in the first parameter. Moreover, the kernel fills the values of any parameters formatted as `%[a-zA-Z]`. The `apport` reporting service overwrites the file `/proc/sys/kernel/core_pattern`. If `apport` is enabled (in `/etc/default/apport`), then the `/proc/sys/kernel/core_pattern` configuration setting is set when the `apport` crash reporting service starts on system boot.
[Read moreâ¦ï»¿](https://askubuntu.com/questions/420410/how-to-permanently-edit-the-core-pattern-file)

### Operating system changes

OneAgent installer performs the following changes to your system to handle core dumps.

#### Disabling ABRT and Apport

[ABRTï»¿](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-abrt) (Red Hat) and [Apportï»¿](https://launchpad.net/ubuntu/+source/apport) (Debian) services are stopped and disabled.

Both services are re-enabled during [OneAgent uninstallation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").

For more information, see [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#operating-system-changes "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

#### Core pattern handling

The OneAgent installer overwrites the core pattern with its own command but preserves the original pattern.

* The content of the original `/proc/sys/kernel/core_pattern` file is copied to:

  + OneAgent version 1.301 and earlier `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`
  + OneAgent version 1.302+ `/var/lib/dynatrace/oneagent/agent/backup/original_core_pattern`

  When OneAgent is uninstalled, the original core pattern present in this file, is restored to `/proc/sys/kernel/core_pattern`.
* The content of the original `kernel.core_pattern` option of `/etc/sysctl.conf` is copied to:

  + OneAgent version 1.301 and earlier `/opt/dynatrace/oneagent/agent/conf/original.sysctl.corepattern`
  + OneAgent version 1.302+ `/var/lib/dynatrace/oneagent/agent/backup/original.sysctl.corepattern`

  When OneAgent is uninstalled, the original core pattern present in this file is restored to `kernel.core_pattern` in `/etc/sysctl.conf`. If `kernel.core_pattern` was not present in `/etc/sysctl.conf` before OneAgent installation, the backup file is not created.

Depending on the original entry in `core_pattern`, Dynatrace will write different patterns to `core_pattern`. The possible configurations and expected entries after installation are listed below:

| Original core\_pattern entry | core\_pattern after ruxitdumpproc installation | Comment |
| --- | --- | --- |
| core | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Simple core dump without parameters. |
| core\_%s\_%e | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -kp %s,%e | Simple core dump with parameters in the filename. The `-kp` parameter is appended along with all kernel parameters needed for Dynatrace to substitute in the original filename. |
| /usr/share/apport/apport | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Core dump next application without parameters. The `-a` argument is not appended to the output `core_pattern` entry if there are no parameters. |
| /usr/share/apport/apport %p %s %c %P | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -a %p %s %c %P | Core dump next application with parameters. The `-a` argument gets appended along with all of the parameters after the binary path to `apport`. |

### Core handling by OneAgent dumpproc

When a crash occurs:

1. `rdp` is called to dump the core to OneAgent folders. This core is used by the Crash Reporting functionality.
2. OneAgent reads `original_core_pattern` and generates a core dump based on its settings. Therefore, if the original configuration specified a particular location for writing the core dump file, this will continue even after OneAgent is installed.
3. The core dump is analyzed to check if Dynatrace could have been the root cause of the crash.

   * If OneAgent determines that Dynatrace could have been at fault:

     + A support alert is generated. This is reported to our DevOps team.
     + The core dump is zipped and retained in addition to all involved libraries. This is needed for later offline analysis.
   * If OneAgent determines that Dynatrace is not at fault:

     + A crash is reported via the Dynatrace web UI to the user.
     + If it has any impact on the customer's application, a problem is opened and an appropriate event is generated for the involved processes as described above.

## Cleanup

The log and support alert directories are cleaned up automatically.

* For support alerts, we process the `core dump`, then zip it and keep it in order to be sent to cluster.
* For crashes (non-instrumented processes or instrumented ones where we decide Dynatrace is not at fault), we process and then delete the copy of the `core dump`.

## Related topics

* [View crash reports for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")
* [View crash reports for custom applications](/docs/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Check the latest crash reports for your custom applications.")
* [New: User session analysis](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")