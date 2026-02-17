---
title: Limit VMware infrastructure monitoring using permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/vmware-vsphere-monitoring/limit-infrastructure-monitoring-using-permissions
scraped: 2026-02-17T04:58:13.339024
---

# Limit VMware infrastructure monitoring using permissions

# Limit VMware infrastructure monitoring using permissions

* How-to guide
* Published Feb 10, 2021

The following applies to VMware only. For other virtualization platforms, you only need to install OneAgent for virtualized host monitoring, as the monitoring of virtualization management layers is supported only for VMware.

When you set up VMware monitoring, you can manage the infrastructural elements (such as hosts and VMs) that you want Dynatrace to monitor by setting or adjusting permissions in vCenter.

See the examples below for details on how to manage user permissions for your VMs.

## Prerequisites

* Administrator role with access to permissions management in vCenter

## Monitor all VMs in a resource pool

To monitor all VMs in a resource pool (or any other "parent" in VMware infrastructure hierarchy), you need to

Assign users read-only permissions to your VMware hosts

To assign users read-only permission to your VMware hosts

1. In vCenter, go to the host view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select the **Read-only** role.
4. Select **OK** to save your changes.

Because a VM might migrate to a different host at a later time, we recommend that you enable Dynatrace monitoring (add read-only permissions) on all hosts to which your VM might migrate.

Assign users read-only permissions to the resource pool

To assign users read-only permission to the resource pool

1. In vCenter, go to the resource pool view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select the **Read-only** role.
4. Select **Propagate to children**.
5. Select **OK** to save your changes.

After assigning users read-only permission to your VMware hosts and to the resource pool, the hosts and VMs to which you granted permissions will be visible in Dynatrace.

Example cluster view

![Dyna vmware01](https://dt-cdn.net/images/dyna-vmware01-1506-10eee7374d.png)

Example host view

![Host view](https://dt-cdn.net/images/2021-02-11-14-43-16-1521-d78906c12f.png)

## Exclude a single VM from monitoring

To exclude a single VM from Dynatrace monitoring, such as a VM that inherited read-only permissions from its parent, you need to remove user read permissions for the respective VM.

To remove a user's read permissions for a VM

1. In vCenter go to the VM view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select **No access** for the role.
4. Select **OK** to save your changes.

## Add a single VM to monitoring

To add a single VM to Dynatrace monitoring, you need to assign users read-only permission to the respective VM.

To assign users read-only permission to a VM

1. In vCenter go to the VM view.
2. Select **Permissions** and then select the `+` sign.
3. Select the user name and then select the **Read-only** role.
4. Select **OK** to save your changes.

## Related topics

* [VMware vSphere monitoring](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.")