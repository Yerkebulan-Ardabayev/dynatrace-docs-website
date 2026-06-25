---
title: Configure SELinux
source: https://docs.dynatrace.com/managed/managed-cluster/installation/selinux
scraped: 2026-05-12T11:53:36.960187
---

# Configure SELinux

# Configure SELinux

* How-to guide
* 3-min read
* Updated on May 08, 2026

SELinux (Security-Enhanced Linux) is a Linux kernel security module that uses mandatory access control (MAC) to restrict processes and users to policies defined by the system administrator. It's available for most Linux distributions and enabled by default on newer Red Hat Enterprise Linux distributions.

Dynatrace Managed automatically detects the SELinux mode during installation and applies the correct file contexts so its services can run in `enforcing` mode. This requires the `semanage` utility on your system. Installation fails if the package is missing.

* **New installations**âno additional steps required.
* **Existing installations**âafter enabling SELinux, run the `reconfigure.sh` script:

  ```
  /opt/dynatrace-managed/installer/reconfigure.sh
  ```
* **Older versions**âchange SELinux mode to `permissive`.

## Enable SELinux

Before enabling SELinux, make sure your system has the following packages:

* `policycoreutils`
* `selinux-utils`
* `selinux-basics`

The steps below use Ubuntu as an example.

1. Use the `apt` command to install the following packages:

   ```
   sudo apt install policycoreutils selinux-utils selinux-basics
   ```
2. Activate SELinux:

   ```
   sudo selinux-activate
   ```

   You should see:

   ```
   SE Linux is activated. You may need to reboot now.
   ```
3. Set SELinux to enforcing mode:

   ```
   sudo selinux-config-enforcing
   ```
4. Stop Dynatrace Managed services:

   ```
   ./dynatrace.sh stop
   ```

   See [Start/stop/restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.") for details.
5. Restart your system.  
   SELinux relabelling starts after the reboot. When finished, the system reboots one more time automatically.
6. Check the SELinux status:

   ```
   # sestatus



   SELinux status:                 enabled



   SELinuxfs mount:                /sys/fs/selinux



   SELinux root directory:         /etc/selinux



   Loaded policy name:             default



   Current mode:                   enforcing



   Mode from config file:          error (Success)



   Policy MLS status:              enabled



   Policy deny_unknown status:     allowed



   Memory protection checking:     requested (insecure)



   Max kernel policy version:      31
   ```
7. Reconfigure Dynatrace Managed with SELinux enabled:

   ```
   /opt/dynatrace-managed/installer/reconfigure.sh
   ```

## Disable SELinux

To disable SELinux, follow these steps:

1. Open `/etc/selinux/config` and set `SELINUX` to `disabled`:

   ```
   SELINUX=disabled
   ```
2. Stop Dynatrace Managed services:

   ```
   ./dynatrace.sh stop
   ```

   See [Start/stop/restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.") for details.
3. Reboot your system.
4. Reconfigure Dynatrace Managed after disabling SELinux:

   ```
   /opt/dynatrace-managed/installer/reconfigure.sh
   ```

## Operating system changes

If SELinux is in `enforcing` mode and you use custom paths for installation or storage, the Managed installer updates the file context of all Dynatrace Managed directories to `usr_t`. For a custom path `/custom-dir/dynatrace-managed`, it runs:

```
semanage fcontext -a -t usr_t "/custom-dir/dynatrace-managed"
```

```
semanage fcontext -a -t usr_t "/custom-dir/dynatrace-managed/.*"
```

```
restorecon -R /custom-dir/dynatrace-managed
```