---
title: Configure elevated permissions in Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/managed-elevated-permissions
scraped: 2026-05-12T11:52:56.055954
---

# Configure elevated permissions in Dynatrace Managed

# Configure elevated permissions in Dynatrace Managed

* Published Apr 07, 2022

By default, the Dynatrace Managed cluster leverages `sudo` to elevate permissions for certain maintenance operations, and you don't need to perform any additional actions when running the installation for the purpose of setting up users, permissions, and services. However, when `sudo` is not available in your operating system, or when you're required to use an alternative command to elevate permissions, you must specify them during installation.

* In interactive mode, when you are asked about elevated permissions, pass a command prefix including a program such as `pbrun`, `sesudo`, or `suexec`
* In silent mode, you can specify this parameter via a [customized installation](/managed/managed-cluster/installation/customize-managed-cluster-install#other "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.")

In all command examples on this page, the following is assumed:

* `dynatrace` (default) is a user that runs all Dynatrace OS services
* Dynatrace Managed is installed in `/opt/dynatrace-managed/`
* The data directory is `/var/opt/dynatrace-managed/`

If your configuration is different, adjust your actions accordingly.

## When elevated permissions are required

An OS user who runs Dynatrace Managed services needs elevated permissions to perform the following tasks:

* Run installation or reconfiguration script
* Add or remove a cluster node
* Start, stop, restart, or check the status of services

For the complete list of commands that require elevated permissions, check `/opt/dtrun/dtrun.conf` file. The `/opt/dtrun` directory and all files inside are owned by root user for security reasons.

## Reconfigure dtrun sudo command

To simplify OS permission management, Dynatrace Managed uses a single script to run all commands that require elevated permissions. A script called **dtrun** is a wrapper for sudo or any other command you have to provide during installation. The location of `dtrun` is `/opt/dtrun/dtrun`, and all commands that `dtrun` can execute are listed in `/opt/dtrun/dtrun.conf`. Only the scripts and commands that are included in `/opt/dtrun/dtrun.conf` can be run.

If a cluster needs to run a command as the root user (for example, to add iptables, restart a component, or run the upgrader), it will use the SUDO\_COMMAND set during installation to try to gain elevated permissions.
You can also search for issues in the `/var/opt/dynatrace-managed/log/dtrun.log` log file.

If you need to reconfigure an existing installation to use a `sudo` alternative, you can run a reconfiguration script. For example, to change the sudo command to `pbrun`, use this script to rerun the installer:

```
sudo /opt/dynatrace-managed/installer/reconfigure.sh --sudo-cmd "/usr/bin/pbrun \$CMD"
```

## Troubleshooting

Misconfigured permissions may lead to various issues with, for example, Dynatrace Managed services or networking.
If there is an issue with permissions, you will see installation log entries such as:

```
sudo: pam_open_session: System error



sudo: policy plugin failed session initialization
```

Additionally, you will see issues in these logs:

* `/var/opt/dynatrace-managed/log/dtrun.log` (dtrun logs)
* `/var/opt/dynatrace-managed/log/launch-logging.log` (Services launcher script logs)

When troubleshooting issues with sudo or elevated permissions, the best approach is to run the entire configuration at once and compare.
Under the root user, all of the commands below should generate output:

```
cat /etc/sudoers | grep -i include



cat /etc/sudoers.d/dynatrace



su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun iptables -L -n'



cat /etc/sudoers | grep dynatrace



cat /etc/passwd | grep dynatrace



cat /etc/shadow | grep dynatrace



chage -l dynatrace
```

The `chage` command tells you if the password is about to expire (that can also cause issues with sudo access).

While adding a node to the cluster as a root user, you may encounter the following authentication error:

```
Installation failed, with status: installer unpacked, system verified, connected to Mission Control, connected to Dynatrace cluster, added to Dynatrace cluster, agent downloaded after 2 minutes 44 seconds.



Exit code: 5



Errors:



Installation failed, with error Dtrun doesn't work properly, check if command "/opt/dtrun/dtrun" is permitted to run with elevated privileges. The dtrun validation failed with error: sudo: PAM account management error: Authentication service cannot retrieve authentication info
```

The cause, in this case, may be that the `dynatrace` user is not able to gain elevated privileges for command `/opt/dtrun/dtrun`. During Managed installation, these privileges are automatically added to sudo config (if it's present and active in system) in following steps:

1. The installer looks for the following line in the `/etc/sudoers` file:

   ```
   #includedir /etc/sudoers.d
   ```

   If it's not present, it's added at the end of the file.
2. Installer creates sudo config file `/etc/sudoers.d/dynatrace` with following contents:

   ```
   Defaults:dynatrace !requiretty



   Defaults:dynatrace !env_reset



   dynatrace ALL=(root:root) NOPASSWD:/opt/dtrun/dtrun
   ```

   These settings give the `dynatrace` user the ability to launch `/opt/dtrun/dtrun` command with root rights, without asking for the password.

The `sudo-1.8.23-1.el7` and later, evaluates the PAM account stack and enforces any account restrictions enforced through PAM. This affects host-based access control as well as password expiration.

Add sudo to the list of allowed services in your access control rules and make sure that users do not have an expired password even for cases where ssh-keys are used for the login.

When you perform additional security checks to control what `dtrun` is allowed to execute, you can find out easily if `sudo` still works as expected by running the following command as a root user:

```
su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun service dynatrace-server status'
```

The following command is an example to verify permission elevation using a `sudo` alternative, `pbrun`:

```
su - dynatrace -s /bin/bash -c 'pbrun /opt/dtrun/dtrun service dynatrace-server status'
```