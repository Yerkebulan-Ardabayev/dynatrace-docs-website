---
title: Customize ActiveGate installation on Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate
---

# Customize ActiveGate installation on Windows

# Customize ActiveGate installation on Windows

* 4-min read
* Published Apr 09, 2021

Additional installation parameters and options can be specified **on the command line** or they can be entered **in the installer UI**. They can be used to customize settings such as directory locations, proxy configuration, SSL certificates etc.

## Installation command syntax

```
Dynatrace-ActiveGate-Windows-x86-<version>.exe [<parameter1>=<value1>]  [<parameter2>=<value2>] ...
```

## Proxy configuration

In the installer UI, select the `Use proxy` check box. Then enter the configuration information into the box beneath the check box.
Proxy configuration, as entered in the installer UI, should be given in the following format. This will configure proxy for ActiveGate for all outgoing connections (in configuration section `http.client`):

`<proxy scheme><user>:<password>@<server>:<port>`

Where:

* All components are optional except for `<server>`.
* If neither `<user>` nor `<password>` are provided, then the `@` character should be omitted.
* `<password>` can only be given if user name is specified.
* ':' after `<user>` can be given even if the password part is empty.
* `<proxy scheme>` is optional and can be 'http://' or 'https://'.
* `<user>` is optional.
* `<server>` can be an IP address or a DNS name, but not a path. For example, if '1.2.3.4/textaferslash' is provided, only the IP part ('1.2.3.4') will be extracted. The slash and the text that follow will be ignored.
* `<port>` is optional.

## Reverse proxy or load balancer configuration

A reverse proxy or a load balancer can be placed on the path from an ActiveGate to the Dynatrace Cluster. This allows your ActiveGate to connect to any available node of the Cluster, spreading the load between the nodes.  
To do this, you need to:

* Provide the address of the reverse proxy/load balancer.
* Ensure that ActiveGate will ignore any further target address information sent from the Dynatrace Cluster, and will thus connect only to the address you have specified.

Such configuration settings can be specified during ActiveGate installation, by giving the following command-line parameters to the installer:

```
IGNORE_CLUSTER_RUNTIME_INFO=true SERVER=<address of reverse proxy>
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

## Installation directory

Absolute path to the location of the installation directory can be specified either in the installer UI or on the command line (ActiveGate version 1.232+). This folder will be used for installing ActiveGate executable files and libraries.

For example:

```
C:\ Dynatrace-ActiveGate-Windows-x86-1.0.0.exe INSTALL=D:\hosted_app\dynatrace
```

ActiveGate configuration and log files are not stored in this location: these files are always installed in %PROGRAMDATA%.

## CA certificate

**Directly specifying an SSL certificate for an ActiveGate is not applicable for Cluster ActiveGates.**
Do not attempt to configure SSL certificates directly on a Cluster ActiveGate. If you do, the certificate will be overwritten by automatic management performed by Dynatrace.
**For Cluster ActiveGates, you must upload your certificates using [the Cluster Management Console](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.") or [the Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate.").**

You can use command-line parameters to specify a custom CA certificate during installation, to be added to the certificate store shipped with ActiveGate.  
In this way you can specify the CA proxy certificate (the certificate to be used when ActiveGate connects to the Dynatrace Cluster). This enables a connection to be established to the Dynatrace Cluster during installation, allowing the ActiveGate installer to download and install any required additional capabilities.

The certificate password is specified as a [file from which the password is read](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections.").

Absolute path to the location of the custom trusted root certificate(s) to add:

```
CA_CERTIFICATE_FILE=<path>
```

Absolute path to the location of the file containing the certificate password:

```
CA_CERTIFICATE_PASSWORD_FILE=<path>
```

Command example:

```
C:\Dynatrace-ActiveGate-Windows-x86-<version>.exe CA_CERTIFICATE_FILE=D:\Users\Fred\myCert.jks CA_CERTIFICATE_PASSWORD_FILE=D:\Users\Fred\myPwd.txt
```

## Custom SSL certificate

During installation you can specify the authentication certificate that ActiveGate provides to connecting clients, such as OneAgents or connections from browser clients. If such certificates are required, then this reduces the effort of post-installation configuration. To learn more, see [Custom SSL certificate for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

The password is specified as a file from which the password is read.

Absolute path to the location of the authentication certificate ActiveGate provides to connecting clients, such as OneAgents or connections from browser clients (such as the RUM JavaScript):

```
CERTIFICATE_FILE=<path>
```

Absolute path to the location of the file containing the certificate password, for the authentication certificate ActiveGate provides to connecting clients:

```
CERTIFICATE_PASSWORD_FILE=<path>
```

Command example:

```
c:\Dynatrace-ActiveGate-Windows-x86-<version>.exe CERTIFICATE_FILE=D:\Users\Fred\myCert.p12 CERTIFICATE_PASSWORD_FILE=D:\Users\Fred\myPwd.txt
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

Defines the maximum number of seconds (default: `120`, max: `240`) the installer will wait for a connection to the cluster.

The connection timeout, as specified by the `DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=<seconds>` command-line parameter, is used in two stages of the installation:

* When downloading additional (optional) capabilities.
* When waiting for connection to the cluster at the end of ActiveGate installation: this connection is then used by ActiveGate during its normal operation.

If the timeout occurs during the download of capabilities (if any), the additional capabilities will not be downloaded and the installation will fail. However, if the timeout occurs at the end of the installation process—that is at the start of normal operation of ActiveGate—all the ActiveGate components will have been installed and ActiveGate will continue its attempts at connecting to the cluster. ActiveGate will keep trying to connect, even after the end of the installation process. If successful, ActiveGate will then operate normally.

To check if the installation and connection was successful, sign in to Dynatrace, in **Settings** select **Deployment Status**, and then select the **ActiveGates** tab.