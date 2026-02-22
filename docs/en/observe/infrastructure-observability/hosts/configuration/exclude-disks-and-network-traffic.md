---
title: Exclude disks and network traffic from host monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic
scraped: 2026-02-22T21:26:59.663176
---

# Exclude disks and network traffic from host monitoring

# Exclude disks and network traffic from host monitoring

* How-to guide
* 4-min read
* Updated on Jul 08, 2024

OneAgent automatically detects and monitors the mount points and network traffic of a host, but you can exclude selected mount points or network traffic from monitoring.

## Exclude disks

Use the **Disk options** settings to create exception rules to remove disks from monitoring.

* Certain file systems (for example, `autofs`, `proc`, `cgroup`, `tmpfs`) are always excluded because monitoring them is not useful.
* You can create disk exclusion rules on the environment, host group, or host level. Exclusions set at a lower level override exclusions set at a higher level (for example, host-level exclusions override environment-level exclusions).

To create a disk exclusion rule

1. Go to the **Disk options** page for the correct level:

   * Environment

     Go to **Settings** > **Preferences** > **Disk options**.
   * Host group

     1. Go to **Deployment Status** > **OneAgents**.
     2. Filter the table by `Host group` and select the host group for which you want to create a disk exclusion rule.
     3. For any listed host (they are all in the selected host group), select the **Host group** link.
     4. Select **Disk options**.
   * Host

     1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host for which you want to create a disk exclusion rule.
     2. On the host overview page, select  > **Settings**.
     3. Select **Disk options**.

   After you are on the **Disk options** page, the steps for creating a disk exclusion rule are the same. The important difference is in the level to which the rule applies: environment, host group, or host.
2. Select **Add item**.
3. Select the **Operating system** of the excluded disk.
4. Set **Disk or mount point path** to the path to where the disk to be excluded from monitoring is mounted.

   **Examples:**

   * `/mnt/my_disk`
   * `/staff/emp1`
   * `C:\`
   * `/staff/*`
   * `/disk*`

   * Mount point paths are case-sensitive
   * The wildcard in `/staff/*` means to exclude every child folder of `/staff`
   * The wildcard in `/disk*` means to exclude every mount point starting with `/disk` (for example, `/disk1`, `/disk99`, and `/diskabc`)
5. Set **File system type** to the type of the file system to be excluded from monitoring.

   **Examples:**

   * `ext4`
   * `ext3`
   * `btrfs`
   * `ext*`

   * File system types are case-sensitive
   * The wildcard in `ext*` means to exclude matching file systems (for example, types `ext4` and `ext3`)
6. Select **Save changes**.

## Exclude network traffic

Use the **Exclude network traffic** settings to exclude traffic on specific network interfaces or hosts from monitoring.

### Exclude NIC

All network traffic from all selected NICs is excluded from monitoring.

1. On the **Exclude network traffic** page, under **Exclude NIC**, select **Add item**.
2. Set **Operating system** to the operating system of the network interface.
3. Set **Name** to the selected operating system's name for the network interface.
4. Select **Save changes**.

### Exclude IP

All network traffic from all selected host IP addresses is excluded from calculating connectivity (other metrics are still calculated). This can be useful, for example, to avoid false connectivity alerts.

To exclude an IP address from connectivity calculations

1. On the **Exclude network traffic** page, under **Exclude IP**, select **Add item**.
2. Enter an IP address whose traffic you want to exclude from connectivity calculations. Wildcards and ranges are not allowed.
3. Select **Save changes**.

## Disks not monitored by OneAgent

The following disks are not monitored by OneAgent. To exclude an additional filesystem type or mount point name, see [Exclude disks](#disk-options).

Operating system

Type

Excluded disks

All supported OS

File systems

`hsfs`

`devtmpfs`

`sysfs`

`rootfs`

`ramfs`

`proc`

`procfs`

`devpts`

`securityfs`

`cgroup`

`cpuset`

`pstore`

`mqueue`

`debugfs`

`autofs`

`hugetlbfs`

`fusectl`

`fuse.gvfsd-fuse`

`binfmt_misc`

`iso9660`

`none`

`rpc_pipefs`

Linux

File systems

`tmpfs`

`udf`

`squashfs`

Linux

Mount point

`/dev`

AIX

File systems

`cdrfs`

Solaris

Network interface

`mac`