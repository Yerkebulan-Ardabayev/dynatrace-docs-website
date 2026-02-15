---
title: How to enable deep monitoring for applications confined by AppArmor
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor
scraped: 2026-02-15T21:18:42.692248
---

# How to enable deep monitoring for applications confined by AppArmor

# How to enable deep monitoring for applications confined by AppArmor

* Latest Dynatrace
* 2-min read
* Published Aug 08, 2017

AppArmor is a mandatory access control system that restricts applications to a limited set of resources. For each confined application, a profile exists that specifies what operations the application is allowed to perform as well as the paths in the file system that the application is allowed to access. In order to enable deep monitoring of applications confined by AppArmor, a custom rule set for OneAgent must be included in the profiles of these applications.

The definition of a rule set, as well as a walkthrough for adding a rule set to an existing profile, is presented in the example below. In this example, we enable deep monitoring of an Apache Tomcat web server, for which the bootstrapper script is located under `/usr/sbin/tomcat-sysd`.

We assume that the directory structure for AppArmor is the following:

```
/etc/apparmor.d/



|--- usr.sbin.tomcat-sysd
```

Where `usr.sbin.tomcat-sysd` is the file that defines the AppArmor profile for Tomcat.

1. Create a new directory and a new rule set for OneAgent within this directory named `agentinjection`.

   ```
   /etc/apparmor.d/



   |--- usr.sbin.tomcat-sysd



   |--- dynatrace-oneagent



   |--- agentinjection
   ```
2. The content of `/etc/apparmor.d/dynatrace-oneagent/agentinjection` should be as follows:

   ```
   #include <abstractions/base>



   #include <abstractions/nameservice>



   # Process Agent injection



   /etc/ld.so.preload r,



   # Host identifier calculation



   /sys/class/net/ r,



   /sys/devices/virtual/net/** r,



   /sys/devices/*/*{,/*}/net/** r,



   # OneAgent directories



   /opt/dynatrace/oneagent/agent/** mr,



   /var/lib/dynatrace/oneagent/** r,



   /var/lib/dynatrace/oneagent/agent/runtime/** w,



   /var/lib/dynatrace/oneagent/agent/config/{discovery_entry_point,ruxit_shm_v*} w,



   /var/lib/dynatrace/enrichment/** r,



   # This path must be adjusted if LOG_PATH installation parameter was used



   /var/log/dynatrace/oneagent/** rkw,



   # This path must be adjusted if DATA_STORAGE installation parameter was used



   /var/lib/dynatrace/oneagent/datastorage/** rkw,



   # Needed for Process Agent to determine whether specialized agent should be loaded and to calculate PGI ID



   /proc/[0-9]*/{cgroup,cmdline,environ,maps,mem,mountinfo,stat,statm,task/*/maps,task/*/mem} r,



   # Miscellaneous



   /dev/random rw,



   /etc/os-release r,



   /proc/sys/fs/file-nr r,



   /proc/sys/kernel/hostname r,



   /proc/{uptime,vmstat} r,



   /sys/devices/system/cpu/ r,



   /sys/fs/cgroup{,/,/**} r,



   /tmp/** rw,



   /var/tmp/ r,



   /var/tmp/** rw,



   /{,var/}run/utmp rk,



   /proc/cgroups r,
   ```

   If you used the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") installation parameter to define a custom directory dedicated to storing large runtime data, edit the following line and add your custom directory

   ```
   # This path must be adjusted if DATA_STORAGE installation parameter was used



   /var/lib/dynatrace/oneagent/datastorage/** rkw,
   ```
3. Include the rule set in the Tomcat profile (`/etc/apparmor.d/usr.sbin.tomcat-sysd`).

   ```
   /usr/sbin/tomcat-sysd {



   #include <dynatrace-oneagent/agentinjection>



   ... (rest of the rules that were already present in the profile)



   }
   ```
4. Verify that the defined profile works correctly:

   1. Reload AppArmor service.
   2. Restart Tomcat.
   3. Verify on the Web UI that the deep monitoring is working for Tomcat process.
   4. Inspect audit logs to ensure that there are no AppArmor denials.

Please keep in mind that although the rule set provided in this example was extensively tested, it may need to be extended or modified due to environmental differences and the custom installation path for OneAgent is not supported.

### Warnings for access denials in audit logs

In case you experience denials related to OneAgent for other processes in the system, add the following subset of rules to the profiles of these processes.

```
# Process injection



/etc/ld.so.preload r,



/etc/oneagentproc/ld.so.preload r,



/var/log/dynatrace/oneagent/process/* rkw,
```

Although this step is optional because failed injections of OneAgent to other processes won't affect the functionality of your applications. Still, it may be required if you are running an IDS or other automated system that reports warnings for access denials found in audit logs.