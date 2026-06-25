---
title: Customize ActiveGate installation on Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate
scraped: 2026-05-12T11:36:30.860044
---

# Customize ActiveGate installation on Linux

# Customize ActiveGate installation on Linux

* 6-min read
* Updated on Feb 11, 2026

You do not need to specify any parameters to the installation command, unless you need to customize settings such as directory locations, proxy configuration, SSL certificates, etc. Command-line parameters and environment variables can be used to customize such settings.

## Installation command syntax

```
Dynatrace-ActiveGate-Linux-x86-<version>.sh [<parameter1>=<value1>]  [<parameter2>=<value2>] ...
```

Spaces between the parameter name and parameter value (around the `=` sign) are not allowed in the command syntax.

## Proxy configuration

Proxy configuration should be given in the following format. This will configure proxy for ActiveGate for all outgoing connections (in configuration section `http.client`):

```
PROXY=<proxy scheme><user>:<password>@<server>:<port>
```

Where:

* All components are optional except for `<server>`.
* If neither `<user>` nor `<password>` are provided, then the `@` character should be omitted.
* `<password>` can only be given if user name is specified.
* ':' after `<user>` can be given even if the password part is empty.
* `<proxy scheme>` is optional and can be 'http://' or 'https://'.
* `<user>` is optional.
* `<server>` can be an IP address or a DNS name, but not a path. For example, if '1.2.3.4/textaferslash' is provided, only the IP part ('1.2.3.4') will be extracted. The slash and the text that follow will be ignored.
* `<port>` is optional.

## Reverse proxy or load balancer configuration for ActiveGate

A reverse proxy or a load balancer can be placed on the path from an ActiveGate to the Dynatrace Cluster. This allows your ActiveGate to connect to any available node of the Cluster, spreading the load between the nodes.  
To do this, you need to:

* Provide the address of the reverse proxy/load balancer.
* Ensure that ActiveGate will ignore any further target address information sent from the Dynatrace Cluster, and will thus connect only to the address you have specified.

Such configuration settings can be specified during ActiveGate installation, by giving the following command-line parameters to the installer:

```
--ignore-cluster-runtime-info SERVER=<address of reverse proxy>
```

Alternatively, you can configure your ActiveGate after installation, by making changes to [ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.").

## Reverse proxy or load balancer configuration for OneAgent

A reverse proxy/load balancer can be placed on the path from OneAgent to ActiveGate. To do so, you need to configure the URL of the load balancer on the ActiveGate so OneAgents can use that endpoint to connect to the ActiveGate.

To specify the address, add the following command-line option:

```
DNSENTRYPOINT=https://<DOMAIN>:<PORT>
```

where:

* `<DOMAIN>` is the domain of your load balancer
* `<PORT>` is optional and defaults to `443`

Alternatively, you can configure the endpoints after installation by making changes to the [ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Configure ActiveGate properties to set up a reverse proxy or a load balancer for OneAgent.").

## User for ActiveGate service

To specify the user that runs the ActiveGate service, provide the following command-line option:

```
USER=<user>
```

The installer creates the user if the user doesn't already exist in the system, and the user doesn't require root privileges. If the parameter isn't specified, the installer creates user `dtuserag` to run the ActiveGate service. Instead of the default `dynatrace` group, the primary group for the existing user will be specified. However, you can use `USER=root` to force the ActiveGate service to run as root.

The `USER=root` parameter is not supported when installing a [synthetic-enabled ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

## Constraints for directory location and mount points

For the full list of ActiveGate directory locations, see [ActiveGate files and directories](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

`<customizable directory>/gateway`âthat is, `INSTALL/gateway`, `CONFIG/gateway`, `LOG/gateway`, `TEMP/gateway`, `PACKAGES_DIR/gateway`âcannot be a parent of another customizable directory, that is of `INSTALL`, `CONFIG`, `TEMP`, `LOG` or `PACKAGED_DIR`.

For example, do **not** specify:

```
INSTALL=/dynatrace



LOG=/dynatrace/gateway/logs



CONFIG=/dynatrace/gateway/config



TEMP=/dynatrace/gateway/tmp
```

Similarly, do **not** specify:

```
CONFIG=/var/lib/dynatrace



PACKAGES_DIR=/var/lib/dynatrace/gateway/packages
```

However, a common parent is allowed, for example:

```
INSTALL=/example/apps



CONFIG=/example/configs



LOG=/example/logs



TEMP=/example/tmp
```

Also see the [Temporary directory](#temporary) section.

### Dedicated directories

Any customizable directory must be exclusive to ActiveGate.

For example, do **not** specify:

```
INSTALL=/opt



CONFIG=/var/lib



LOG=/var/log



TEMP=/var/tmp
```

Instead, each path should include a subdirectory that is dedicated to ActiveGate, for example:

```
INSTALL=/opt/activegate



CONFIG=/var/lib/activegate



LOG=/var/log/activegate



TEMP=/var/tmp/activegate
```

### Spaces in directory location

ActiveGate does not support spaces in a directory location.

For example, do **not** specify:

```
CONFIG=/var/lib/dir\ with\ space
```

Similarly, do **not** specify:

```
CONFIG="/var/lib/dir with space"
```

### Mount points

During the install process, ActiveGate needs to create, delete and modify subdirectories under its top-level `INSTALL`, `CONFIG`, `LOG` and `TEMP` directories. There must be no filesystem mount points inside these directories.

For example, if you have provided the following `INSTALL` parameter:

```
INSTALL=/opt/MyActiveGate
```

The ActiveGate installer will create a subdirectory `gateway` in the installation path you have provided:  
`/opt/MyActiveGate/gateway`

As a result:

* The mount point `/opt/MyActiveGate` is **VALID**.
* The mount point `/opt/MyActiveGate/gateway` is **INVALID**.

## Installation directory

```
INSTALL=<directory>
```

Stores installation files in the specified directory. The default value for this parameter (if not specified) is `/opt/dynatrace`. This parameter is not permitted during update.

Installation directory

ActiveGate and OneAgent installed on the same host must **not** share the same installation directory.

## Directory for storing downloaded packages

```
PACKAGES_DIR=<directory>
```

Stores installation files of additional capabilities in the specified directory. The default value for this parameter (if not specified) is `/var/lib/dynatrace/packages`. Not permitted during update.

## Log directory

```
LOG=<directory>
```

Stores log files in the specified directory. The default value for this parameter (if not specified) is `/var/log/dynatrace`. Not permitted during update.

## Configuration directory

```
CONFIG=<directory>
```

Stores configuration files in the specified directory. The default value for this parameter (if not specified) is `/var/lib/dynatrace`. Not permitted during update.

## Temporary directory

```
TEMP=<directory>
```

Indicates the temporary directory to be used by ActiveGate. The default value for this parameter (if not specified) is `/var/tmp/dynatrace`. Not permitted during update.

If you have customized the temporary directory, ensure it is excluded from any automatic cleanup rules. Failure to do so may impact the reliable operation of Synthetic-enabled ActiveGate.

### Use of `/temp` or `/tmp`

Because of possible automatic purging, we recommend that you not use the `/temp` or `/tmp` directories or their subdirectories to install ActiveGate or store any data generated or used by ActiveGate.

Note that for Synthetic-enabled ActiveGate installed on Ubuntu 20.04 LTS and 22.04 LTS earlier than 1.331, write access to the `/tmp` directory is required for the installation of Chromium snap packages.

## CA certificate

You can use command-line parameters to specify a custom CA certificate during installation, to be added to the certificate store shipped with ActiveGate.  
In this way you can specify the CA proxy certificate (the certificate to be used when ActiveGate connects to the Dynatrace Cluster). This enables a connection to be established to the Dynatrace Cluster during installation, allowing the ActiveGate installer to download and install any required additional capabilities.

The certificate password is specified as a [file from which the password is read](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections.").

Absolute path to the location of the custom trusted root certificate(s) to add:

```
--ca-certificate-file=<path>
```

Absolute path to the location of the file containing the certificate password:

```
--ca-certificate-password-file=<path>
```

Command example:

```
[root@host]# ./Dynatrace-ActiveGate-Linux-1.217.sh --ca-certificate-file=/home/fred/myCert.jks  --ca-certificate-password-file=/home/fred/myPwd.txt
```

### Constraints for specifying SSL certificate

Directly specifying an SSL certificate for an ActiveGate is not applicable for Cluster ActiveGates.
Do not attempt to configure SSL certificates directly on a Cluster ActiveGate. If you do, the certificate will be overwritten by automatic management performed by Dynatrace.
For Cluster ActiveGates, you must upload your certificates using [the Cluster Management Console](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.") or [the Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate.").

## Custom SSL certificate

During installation you can specify the authentication certificate that ActiveGate provides to connecting clients, such as OneAgents or connections from browser clients. If such certificates are required, then this reduces the effort of post-installation configuration. To learn more, see [Custom SSL certificate for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

The certificate password is specified as a [file from which the password is read](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate#known-limitations "Learn how to configure the SSL certificate on your ActiveGate.").

Absolute path to the location of the authentication certificate ActiveGate provides to connecting clients, such as OneAgents or connections from browser clients (such as the RUM JavaScript):

```
--certificate-file=<path>
```

Absolute path to the location of the file containing the certificate password, for the authentication certificate ActiveGate provides to connecting clients:

```
--certificate-password-file=<path>
```

Command example:

```
[root@host]# ./Dynatrace-ActiveGate-Linux-x86-<version>.sh --certificate-file=/home/fred/myCert.p12  --certificate-password-file=/home/fred/myPwd.txt
```

## Network zone

```
--set-network-zone=<name>
```

Defines the [network zone](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") to which the ActiveGate belongs. An ActiveGate can belong to only one network zone. The name of a network zone is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a network zone name. The length of the string is limited to 256 characters.

To change or clear the network zone assignment after installation, use [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify network zone** action).

Alternatively, you can specify the network zone in the [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") file.

## Group

```
--set-group=<name>
```

Defines the ActiveGate group to which the ActiveGate belongs. An ActiveGate can belong to only one group. The name of an ActiveGate group is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a group name. The length of the string is limited to 256 characters. You can use ActiveGate groups to perform bulk actions on your ActiveGates, such as managing [Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") running on ActiveGates. If you want to assign your ActiveGate to a group, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

To change or clear the ActiveGate group assignment after installation, use [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (select the **modify ActiveGate group** action).

Alternatively, you can specify the ActiveGate group in the [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") file.

## Connection timeout

```
DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=<seconds>
```

Defines the maximum number of seconds (default: `120`, max: `240`) the installer will wait for a connection to the cluster. In Linux deployments, this parameter must be used as an environment variable.

The connection timeout, as specified by the `DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=<seconds>` environment variable, is used in two stages of the installation:

* When downloading additional (optional) capabilities.
* When waiting for connection to the cluster at the end of ActiveGate installation: this connection is then used by ActiveGate during its normal operation.

If the timeout occurs during the download of capabilities (if any), the additional capabilities will not be downloaded and the installation will fail. However, if the timeout occurs at the end of the installation processâthat is at the start of normal operation of ActiveGateâall the ActiveGate components will have been installed and ActiveGate will continue its attempts at connecting to the cluster. ActiveGate will keep trying to connect, even after the end of the installation process. If successful, ActiveGate will then operate normally.

To check if the installation and connection was successful, sign in to Dynatrace, in **Settings** select **Deployment Status**, and then select the **ActiveGates** tab.

For example:

```
[root@host]# export DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=240



[root@host]# Dynatrace-ActiveGate-Linux-x86-1.0.0.sh <... other parameters>
```

or you can use combined commands in a single line. For example:

```
[root@host]# export DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=240 ; Dynatrace-ActiveGate-Linux-x86-1.0.0.sh <... other parameters>
```

## FIPS compliance

ActiveGate version 1.315+

For Federal Information Processing Standard (FIPS) compliance, you can enable FIPS-compliant mode during ActiveGate installation.

FIPS-compliant mode cannot be changed after installation. To change the mode, you need to uninstall ActiveGate and reinstall it with the desired settings.

Command example:

```
[root@host]# ./Dynatrace-ActiveGate-Linux-x86-<version>.sh --fips-mode
```

where `--fips-mode` enables installation of ActiveGate in FIPS-compliant mode.

For information on requirements, limitations, and verification steps, see [host-based FIPS-compliant ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance#host-based-activegate-deployment "Learn about ActiveGate FIPS compliance").