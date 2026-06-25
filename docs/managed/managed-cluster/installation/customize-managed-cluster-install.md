---
title: Customize Managed Cluster installation
source: https://docs.dynatrace.com/managed/managed-cluster/installation/customize-managed-cluster-install
scraped: 2026-05-12T11:25:09.126557
---

# Customize Managed Cluster installation

# Customize Managed Cluster installation

* Reference
* 9-min read
* Updated on May 08, 2026

Use command line parameters to override default settings of a Managed Cluster installation. By default, no parameters are requiredâthe Managed installer runs in interactive mode, prompting you to confirm or override default settings. Values entered interactively always take precedence over command line parameter values.

When you run the installer in interactive mode with command line parameters, the parameter values are presented as prompts instead of defaults. Any values entered at that point take precedence.

To install a Managed Cluster in non-interactive mode with default settings, use `--install-silent` together with `--license` to provide the license key.

## Default settings

* Installation path (binaries): `/opt/dynatrace-managed`
* Dynatrace Cluster data files: `/var/opt/dynatrace-managed`
* System user running Dynatrace processes: `dynatrace`
* System group running Dynatrace processes: `dynatrace`

To list all available command line options, run the installer with `--help` as root:

```
[root@localhost]# ./dynatrace-managed-installer.sh --help
```

## Initial configuration parameters

Use these parameters for initial server configuration. When specified, the installer generates an authentication token for the public REST API after successful installation and cluster registration.

| Parameter | Description |
| --- | --- |
| `--initial-environment <name>` | Name of the first monitoring environment. |
| `--initial-first-name <name>` | Administrator's first name. |
| `--initial-last-name <name>` | Administrator's last name. |
| `--initial-email <email>` | Administrator's email address. |
| `--initial-pass <pass>` | Administrator's password. |

## Installation mode parameters

| Parameter | Description |
| --- | --- |
| `--install` | Standard interactive installation. |
| `--install-silent` | Installs with default settings in non-interactive mode. Use other command line parameters to override specific defaults. Useful for automating installation. |
| `--install-new-dc-silent` | Premium High Availability only. Installs in a new data center in non-interactive mode. Use other command line parameters to override specific defaults. |
| `--upgrade` | Starts the update process from the command line. |
| `--system-check` | Checks whether the machine and operating system meet the requirements of the new version. |
| `--restore` | Restores a Dynatrace Managed installation from the backup file specified by `--backup-file`. Backup runs daily once configured in Dynatrace Managed. |
| `--reconfigure` | Reconfigures an existing installation using setup parameters. |
| `--uninstall` | Uninstalls Dynatrace Managed. |
| `--self-check` | Verifies that the installer file isn't corrupt. |
| `--backup-file <path>` | Full path to the backup file containing configuration and data. Used with `--restore`. |
| `--timeouts <component:value, ..>` | Extends timeouts for specified components. Use when:  * A specific component needs a longer timeout (for example, your OS firewall startup takes several minutes). * You have many environments and need more time for Server startup. |
| `--drop-x-forwarded-for` | Dynatrace uses the `X-Forwarded-For` header for features such as logging. Handle these headers according to security best practicesâincorrect handling may result in displaying and logging incorrect data if an attacker adds manipulated `X-Forwarded-For` headers to requests. |

Proxy configuration

The outermost reverse proxy from which Dynatrace can be accessed must be configured as detailed below.

* All requests that target Dynatrace are stripped from all X-Forwarded-For headers.
* The following request paths must be excluded from this behavior. Allow requests to these paths to keep X-Forwarded-For headers, as the related features require them.

  + `/bf`
  + `/mbeacon`
  + `/communication`

The Nginx proxy installed with Dynatrace Managed follows these rules by default. However, you can turn off this behavior during installation if Nginx isn't the outermost proxy from which clients access Dynatrace. In this case, configure the outermost proxy manually.

The following components can be configured with `--timeouts`:

| Component | Description |
| --- | --- |
| `proc` | Base timeout in seconds. This value is added to the component-specific timeouts listed below for Nodekeeper, Cassandra, Elasticsearch, Server, ActiveGate, and NGINX. |
| `ndk` | Nodekeeper startup process timeout seconds = `proc` + `ndk` |
| `cas` | Cassandra startup process timeout seconds = `proc` + `cas` |
| `els` | Elasticsearch startup process timeout seconds = `proc` + `els` |
| `srv` | Server startup process timeout seconds = `proc` + `svr` |
| `ag` | ActiveGate startup process timeout seconds = `proc` + `ag` |
| `ngx` | NGINX startup process timeout seconds = `proc` + `ngx` |
| `fw` | Firewall startup process timeout seconds = `fw` |

## Setup parameters

You can change the installation path and other settings using the following parameters:

### Binaries

| Parameter | Description |
| --- | --- |
| `--binaries-dir <path>` | Full path to the Dynatrace binaries directory. Using this parameter with SELinux enabled requires the semanage utility to be available on your system. **Default value**: `/opt/dynatrace-managed` |

### Licensing

| Parameter | Description |
| --- | --- |
| `--license <license-key>` | License key obtained from Dynatrace. |
| `--license-file <path>` | Dynatrace license file, used when a license key isn't provided. |

### Datastore

If you have SELinux enabled, the following parameters require the semanage utility to be available on your system.

| Parameter | Description |
| --- | --- |
| `--datastore-dir <path>` | Full path to the Dynatrace installation directory. Use a dedicated drive or partition for this directory. Only Dynatrace data not configured in other stores is kept here. If no specific paths are configured for other data stores, all Dynatrace data is stored here. **Default value**: `/var/opt/dynatrace-managed` |
| `--rpl-datastore-dir <path>` | Full path to Dynatrace Session Replay store. **Default value**: `/var/opt/dynatrace-managed/server/replayData` |
| `--cas-datastore-dir <path>` | Full path to the Dynatrace metrics repository directory. If you specify this location, Dynatrace stores metrics data here instead of in the main data location. **Default value**: `/var/opt/dynatrace-managed/cassandra` |
| `--els-datastore-dir <path>` | Full path to Dynatrace Elasticsearch store directory. **Default value**: `/var/opt/dynatrace-managed/elasticsearch` |
| `--svr-datastore-dir <path>` | Full path to Dynatrace raw transaction store directory. If you specify this location, Dynatrace stores raw transaction data here instead of in the main data location. **Default value**: `/var/opt/dynatrace-managed/server/` |

The default path `/var/opt/dynatrace-managed/server/replayData` can't be a mounting point.

### System user

To make the configuration as secure as possible, Dynatrace creates a unique Linux system user for Dynatrace Managed services.

The system user:

* Has only the read, write, and execute permissions needed for required files
* Has no home directory
* Has a `nologin` shell
* Has login disabled

These measures limit what an attacker can do if system security is compromised. If you use a default user account, set it up with the same principles.

The following parameters specify a system user who is authorized to run Dynatrace processes.

| Parameter | Description |
| --- | --- |
| `--system-user <user:group>` | User name and group name of the system user authorized to run Dynatrace processes. **Default value**: `dynatrace:dynatrace` |
| `--system-user-id <UID:GID>` | User ID and group ID of the system user authorized to run Dynatrace processes. **Default value**: `1011:1011` |

You can specify one or both parameters.

* The user/group name and user ID/group ID must be identical on all Cluster nodes to ensure proper access to shared storage (for example, backup).
* If you override the default user and group settings, the modified values automatically propagate as the new default to subsequent nodes added to the Cluster.

### Connectivity to Mission Control

| Parameter | Description |
| --- | --- |
| `--network-proxy` | If your machine uses a network proxy to connect to the Internet, put the address here in the following format: `protocol://[user:password@]server-address:port`. **Default value**: `none` |
| `--network-proxy-cert-file` | If your machine uses an HTTPS network proxy with a self-signed certificate, extend the trusted certificate store. Provide the full path to a public SSL certificate file in PEM format. |
| `--registration-token` | Token used for registration in Mission Control (optional for regular installation). |

### Managed Cluster

| Parameter | Description |
| --- | --- |
| `--cluster-ip` | If your machine has more than one network interface you need to decide which network interface will be used for Managed Cluster traffic and put its IP4 address here. |
| `--cluster-nodes <id:ip, ..>` | You can specify the node ID with the IP address. Use this when you restore a Managed Cluster and you must attach a replacement node that has a different IP address than the original. |
| `--seed-ip <ip>` | IPv4 address of the seed node in the Managed Cluster. |
| `--seed-auth <auth-token>` | Authentication token for connection to seed node. You'll find this after logging into the seed node, on the **Download node installer** page. This token is valid for three hours. |
| `--rack-dc <dc>` | For rack-aware deployments, provide the data center that contains the rack where you want to add the node. |
| `--rack-name <rack>` | For rack-aware deployments, provide the name of the rack where you want to add the node. |

### OneAgent

| Parameter | Description |
| --- | --- |
| `--install-agent <on|off>` | Enable/disable installation of self-monitoring OneAgent. **Default value**: `on` |
| `--agent-system-user <user:group>` | Name:group of system user who should run the self-monitoring agent. Use only if the default user for the agent can't be used. |
| `--agent-dir <path>` | Allows installation of self-monitoring OneAgent to a different directory. For example, on Linux: `/bin/sh Managed-installer.sh --agent-dir /opt/dt/self-monitoring`.  With `--agent-dir` set to `/data/dynatrace/`, the installer creates the symbolic link `/opt/dynatrace/oneagent` -> `/data/dynatrace` and places all OneAgent files into the specified directory (in this example, `/data/dynatrace`). Remove this symbolic link manually after you uninstall OneAgent. Using this parameter on Linux when SELinux is enabled requires the `semanage` binary to be available on your system. |

## SSL/TLS certificate parameters

Command line parameters can also help you install or update SSL/TLS certificates on Dynatrace Managed. For more information on installing fully qualified digital certificates, see [Can I use my own SSL certificate?](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")

| Parameter | Description |
| --- | --- |
| `--ssl-protocols "<protocols>"` | Space-separated list of protocols accepted by SSL connections. Replaces the default list. |
| `--ssl-ciphers "<ciphers>"` | Definition of ciphers accepted by SSL connections. Replaces the default definition. This definition must first be validated with an `openssl ciphers` command. |
| `--ciphers-autoupdate <on|off>` | Enable/disable cipher autoupdate, which sets default values for protocols and ciphers accepted by SSL connections on each upgrade/reconfiguration. **Default value for new nodes**: `on` |

### Other

| Parameter | Description |
| --- | --- |
| `--hosts <on|off>` | Enable/disable altering of `/etc/hosts` file. **Default value**: `on` |
| `--sudo-cmd "<cmd>"` | Command that should be used for executing system commands with superuser privileges. Should contain the variable `$CMD` (typed as `\$CMD`). By default the following is used: `/usr/bin/sudo \$CMD`. For example:  ```  dynatrace-managed.sh --sudo-cmd  "/usr/bin/pbrun \$CMD" ``` |
| `--no-start` | Upgrade only. Use this parameter when you don't want Dynatrace Managed to start immediately following an upgrade. |
| `--unregister` | Use this parameter when uninstalling a Managed Cluster to unregister the Cluster and release license from Mission Control. |
| `--version` | Print version information. |
| `--tmp-dir <path>` | Full path to the directory for installer temp files. |