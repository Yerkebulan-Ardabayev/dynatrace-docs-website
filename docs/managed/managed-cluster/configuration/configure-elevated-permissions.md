---
title: Configure elevated permissions
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-elevated-permissions
---

# Configure elevated permissions

# Configure elevated permissions

* How-to guide
* 4-min read
* Updated on Jun 18, 2026

To configure how Dynatrace Managed elevates operating system permissions for maintenance operations, follow these steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review elevated permissions**](/managed/managed-cluster/configuration/configure-elevated-permissions#review-elevated-permissions "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure during installation**](/managed/managed-cluster/configuration/configure-elevated-permissions#configure-during-installation "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Reconfigure dtrun**](/managed/managed-cluster/configuration/configure-elevated-permissions#reconfigure-dtrun "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Verify elevated permissions**](/managed/managed-cluster/configuration/configure-elevated-permissions#verify-elevated-permissions "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")

The command examples on this page assume the following configuration:

* `dynatrace` (default) is a user that runs all Dynatrace OS services
* The Dynatrace Managed installation directory is `/opt/dynatrace-managed/`
* The data directory is `/var/opt/dynatrace-managed/`

If your configuration is different, adjust your actions accordingly.

## Step 1 Review elevated permissions

An OS user who runs Dynatrace Managed services needs elevated permissions to perform the following tasks:

* Run the installation or reconfiguration script
* Add or remove a Managed Cluster node
* Start, stop, restart, or check the status of services

For the complete list of commands that require elevated permissions, check the `/opt/dtrun/dtrun.conf` file. The root user owns the `/opt/dtrun` directory and all files inside it for security reasons.

## Step 2 Configure during installation

By default, Dynatrace Managed uses `sudo` to elevate permissions for maintenance operations. You don't need to configure a different command when `sudo` is available and allowed by your operating system policies.

If `sudo` isn't available, or if your operating system policies require a different elevation command, specify the command during installation.

* In interactive mode, enter a command prefix that includes a program such as `pbrun`, `sesudo`, or `suexec` when the installer asks about elevated permissions.
* In silent mode, specify the parameter through a [customized installation](/managed/managed-cluster/installation/customize-managed-cluster-install#other "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.").

## Step 3 Reconfigure dtrun

Dynatrace Managed uses the `dtrun` script to run commands that require elevated permissions. The `dtrun` script wraps `sudo` or the alternative command you provide during installation.

The location of `dtrun` is `/opt/dtrun/dtrun`. The `/opt/dtrun/dtrun.conf` file lists the commands that `dtrun` can run. `dtrun` can run only the scripts and commands included in `/opt/dtrun/dtrun.conf`.

If a Managed Cluster node needs to run a command as the root user, the Managed Cluster uses the `SUDO_COMMAND` set during installation to gain elevated permissions. Examples include adding iptables rules, restarting a component, or running the upgrader.

If you need to reconfigure an existing installation to use a `sudo` alternative, you can run a reconfiguration script. For example, to change the sudo command to `pbrun`, use this script to rerun the installer:

```
sudo /opt/dynatrace-managed/installer/reconfigure.sh --sudo-cmd "/usr/bin/pbrun \$CMD"
```

## Step 4 Verify elevated permissions

Verify that `dtrun` can run commands with elevated permissions.

To verify permission elevation with `sudo`, run the following command as the root user:

```
su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun service dynatrace-server status'
```

To verify permission elevation with the `pbrun` `sudo` alternative, run the following command as the root user:

```
su - dynatrace -s /bin/bash -c 'pbrun /opt/dtrun/dtrun service dynatrace-server status'
```

After verification succeeds, Dynatrace Managed can use the configured elevated permissions command for maintenance operations.

## Frequently asked questions

Where can you find elevated permission logs

If there is an issue with permissions, installation logs can contain entries such as:

```
sudo: pam_open_session: System error



sudo: policy plugin failed session initialization
```

Check the following logs for elevated permission issues:

* `/var/opt/dynatrace-managed/log/dtrun.log` (dtrun logs)
* `/var/opt/dynatrace-managed/log/launch-logging.log` (Services launcher script logs)

How can you check the sudo configuration

When troubleshooting `sudo` or elevated permission issues, run the entire configuration check and compare the output. The following commands should generate output when you run them as the root user:

```
cat /etc/sudoers | grep -i include



cat /etc/sudoers.d/dynatrace



su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun iptables -L -n'



cat /etc/sudoers | grep dynatrace



cat /etc/passwd | grep dynatrace



cat /etc/shadow | grep dynatrace



chage -l dynatrace
```

The `chage` command tells you if the password is about to expire. Password expiration can cause issues with sudo access.

Why does node installation fail with an account management error

While adding a node to the Managed Cluster as a root user, you may encounter the following authentication error:

```
Installation failed, with status: installer unpacked, system verified, connected to Mission Control, connected to Dynatrace cluster, added to Dynatrace cluster, agent downloaded after 2 minutes 44 seconds.



Exit code: 5



Errors:



Installation failed, with error Dtrun doesn't work properly, check if command "/opt/dtrun/dtrun" is permitted to run with elevated privileges. The dtrun validation failed with error: sudo: PAM account management error: Authentication service cannot retrieve authentication info
```

The cause may be that the `dynatrace` user can't gain elevated privileges for `/opt/dtrun/dtrun`. During Managed installation, the installer automatically adds these privileges to the sudo configuration if sudo is present and active in the system.

1. The installer looks for the following line in the `/etc/sudoers` file:

   ```
   #includedir /etc/sudoers.d
   ```

   If the line isn't present, the installer adds it to the end of the file.
2. The installer creates the sudo configuration file `/etc/sudoers.d/dynatrace` with the following contents:

   ```
   Defaults:dynatrace !requiretty



   Defaults:dynatrace !env_reset



   dynatrace ALL=(root:root) NOPASSWD:/opt/dtrun/dtrun
   ```

   These settings let the `dynatrace` user start `/opt/dtrun/dtrun` with root rights without entering a password.

`sudo-1.8.23-1.el7` and later evaluate the PAM account stack and enforce account restrictions through PAM. The PAM account stack evaluation affects host-based access control and password expiration.

Add sudo to the list of allowed services in your access control rules. Make sure users don't have an expired password, even when they use SSH keys to sign in.

How can you troubleshoot dtrun command restrictions

When you perform additional security checks to control what `dtrun` can run, verify that the configured elevation command still works.

To verify `sudo`, run the following command as the root user:

```
su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun service dynatrace-server status'
```

To verify the `pbrun` `sudo` alternative, run the following command as the root user:

```
su - dynatrace -s /bin/bash -c 'pbrun /opt/dtrun/dtrun service dynatrace-server status'
```