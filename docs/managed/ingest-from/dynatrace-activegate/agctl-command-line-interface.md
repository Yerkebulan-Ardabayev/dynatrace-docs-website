---
title: agctl - Command-line interface for ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface
---

# agctl - Command-line interface for ActiveGate

# agctl - Command-line interface for ActiveGate

* Reference
* 15-min read
* Published Feb 05, 2026

ActiveGate version 1.333+

`agctl` is a command-line interface for ActiveGate configuration management. It enables you to configure various ActiveGate settings directly from the command line without manually editing configuration files.

After modifying ActiveGate configuration with `agctl`, you need to restart ActiveGate for the changes to take effect. See [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

## Before you begin

### Prerequisites

* ActiveGate installed on your system
* Permissions to execute `agctl`. See the [Access agctl](#access-agctl) section that follows.

### Access agctl

Linux

Windows

On Linux systems, `agctl` is automatically added to the PATH for easier access. You can run it from any directory.

To execute `agctl`, you must belong to the ActiveGate service user group. By default, this is the `dtuserag` group. For details on user configuration, see:

* [Customize installation for ActiveGate](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#user-service "Learn about the command-line parameters that you can use with ActiveGate on Linux.")
* [Default settings](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings#service-account "Learn about the default settings with which ActiveGate is installed on Linux")

**Example: Run agctl**

```
agctl [command] [operation] [parameters]
```

On Windows systems, `agctl.bat` must be executed from the [ActiveGate installation directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

If you installed ActiveGate in a custom folder, the path to `agctl.bat` will be different.

`agctl.bat` must be run as administrator.

**Example: Run agctl.bat from the installation directory**

```
"C:\Program Files\dynatrace\gateway\agctl.bat" [command] [operation] [parameters]
```

## Command structure

```
agctl [command] [operation] [parameters]
```

Where:

* `[command]`: The specific ActiveGate feature to manage (for example, `group`, `modules`, `ssl-port`)
* `[operation]`: The action to perform (for example, `set`, `get`, `clear`, `enable`, `disable`)
* `[parameters]`: Command-specific parameters

## Available commands

| Command | Description |
| --- | --- |
| [help](#help) | Display help message |
| [group](#group) | Manage ActiveGate group configuration |
| [incoming-endpoint](#incoming-endpoint) | Manage reverse proxy for OneAgent configuration |
| [modules](#modules) | Manage modules configuration |
| [network-zone](#network-zone) | Manage network zone configuration |
| [outgoing-endpoint](#outgoing-endpoint) | Manage reverse proxy for ActiveGate configuration |
| [properties](#properties) | Set properties based on provided configuration file |
| [property](#property) | Manage individual custom properties |
| [ssl-certificate](#ssl-certificate) | Manage custom SSL certificate configuration |
| [ssl-port](#ssl-port) | Manage HTTPS port configuration |
| [support-archive](#support-archive) | Create support archive for troubleshooting |
| [trust-store](#trust-store) | Manage trust store configuration |
| [version](#version) | Get ActiveGate version |

### Help

Display help information for `agctl`.

#### Usage

```
agctl help
```

To get help for a specific command:

```
agctl [command] help
```

#### Examples

```
# Show general help



agctl help



# Show help for the group command



agctl group help
```

### Group

Manage the ActiveGate group configuration. Groups allow you to perform bulk actions on your ActiveGates.

For details on ActiveGate groups, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

#### Usage

```
agctl group set <NAME>



agctl group set --value=<NAME>



agctl group get



agctl group clear



agctl group help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Assign a group name to the ActiveGate |
| `get` | Display the current group name |
| `clear` | Remove the current group name |
| `help` | Show help for the group command |

#### Parameters for set

**Required (one of):**

* `<NAME>`: Group name provided as a positional argument
* `--value=<NAME>`: Group name provided as a named parameter (takes precedence if both are provided)

#### Naming rules

* Allowed characters: alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`)
* Dots act as separators and cannot be the first or last character
* Maximum length: 256 characters

#### Examples

```
# Set group using positional argument



agctl group set my.group



# Set group using named parameter



agctl group set --value=production.activegate



# Get current group



agctl group get



# Clear group configuration



agctl group clear
```

### Incoming endpoint

Manage reverse proxy configuration for OneAgent traffic. This configures the endpoint URLs that OneAgents use to connect through a reverse proxy.

For details, see [Set up reverse proxy for OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Configure ActiveGate properties to set up a reverse proxy or a load balancer for OneAgent.").

See also [Outgoing endpoint](#outgoing-endpoint) configuration.

#### Usage

```
agctl incoming-endpoint set <URLS>



agctl incoming-endpoint set --value=<URLS>



agctl incoming-endpoint get



agctl incoming-endpoint clear



agctl incoming-endpoint help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure incoming endpoint URLs |
| `get` | Display current endpoint URLs |
| `clear` | Remove current endpoint URLs |
| `help` | Show help for the incoming-endpoint command |

#### Parameters for set

**Required (one of):**

* `<URLS>`: Comma-separated list of URLs provided as a positional argument
* `--value=<URLS>`: Comma-separated list of URLs provided as a named parameter (takes precedence if both are provided)

#### URL format requirements

* Format: `https://<DOMAIN>:<PORT>`
* `<DOMAIN>` must be a fully qualified domain name (FQDN), IPv4, or IPv6 address
* `<PORT>` is optional and defaults to 443
* `/communication` path is optional
* Multiple URLs must be separated by commas

#### Examples

```
# Set single endpoint



agctl incoming-endpoint set https://proxy.example.com:443



# Set multiple endpoints



agctl incoming-endpoint set https://proxy1.example.com:443,https://proxy2.example.com:8443/communication



# Set using named parameter



agctl incoming-endpoint set --value=https://proxy.example.com/communication



# Get current configuration



agctl incoming-endpoint get



# Clear configuration



agctl incoming-endpoint clear
```

### Modules

Manage ActiveGate modules configuration. You can enable or disable specific functional modules based on your requirements.

For details on ActiveGate modules, see [Configuration properties and parameters](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.").

#### Usage

```
agctl modules enable <MODULES>



agctl modules enable --value=<MODULES>



agctl modules disable <MODULES>



agctl modules disable --value=<MODULES>



agctl modules get



agctl modules help
```

#### Operations

| Operation | Description |
| --- | --- |
| `enable` | Enable one or more modules |
| `disable` | Disable one or more modules |
| `get` | Display currently enabled modules |
| `help` | Show help for the modules command |

#### Parameters for enable and disable

**Required (one of):**

* `<MODULES>`: Comma-separated list of module names provided as a positional argument
* `--value=<MODULES>`: Comma-separated list of module names provided as a named parameter (takes precedence if both are provided)

#### Notes

Multiple module names must be separated by commas without spaces.

#### Examples

```
# Enable multiple modules



agctl modules enable MSGrouter,metrics_ingest



# Disable a module using named parameter



agctl modules disable --value=synthetic



# Get currently enabled modules



agctl modules get
```

### Network zone

Manage the network zone configuration. Network zones allow you to define routing boundaries for your monitoring infrastructure.

For details on network zones, see [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.").

#### Usage

```
agctl network-zone set <NAME>



agctl network-zone set --value=<NAME>



agctl network-zone get



agctl network-zone clear



agctl network-zone help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure a network zone name |
| `get` | Display the current network zone name |
| `clear` | Remove the current network zone name |
| `help` | Show help for the network-zone command |

#### Parameters for set

**Required (one of):**

* `<NAME>`: Network zone name provided as a positional argument
* `--value=<NAME>`: Network zone name provided as a named parameter (takes precedence if both are provided)

#### Naming rules

* Allowed characters: alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`)
* Dots act as separators and cannot be the first or last character
* Maximum length: 256 characters

#### Examples

```
# Set network zone using positional argument



agctl network-zone set my.zone



# Set network zone using named parameter



agctl network-zone set --value=production.zone



# Get current network zone



agctl network-zone get



# Clear network zone configuration



agctl network-zone clear
```

### Outgoing endpoint

Manage reverse proxy configuration for ActiveGate traffic. This configures the endpoint URLs that ActiveGate uses to connect to Dynatrace through a reverse proxy.

For details, see [Set up reverse proxy for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.").

See also [Incoming endpoint](#incoming-endpoint) configuration.

#### Usage

```
agctl outgoing-endpoint set <URLS>



agctl outgoing-endpoint set --value=<URLS>



agctl outgoing-endpoint get



agctl outgoing-endpoint clear



agctl outgoing-endpoint help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure outgoing endpoint URLs |
| `get` | Display current endpoint URLs |
| `clear` | Remove current endpoint URLs |
| `help` | Show help for the outgoing-endpoint command |

#### Parameters for set

**Required (one of):**

* `<URLS>`: Comma-separated list of URLs provided as a positional argument
* `--value=<URLS>`: Comma-separated list of URLs provided as a named parameter (takes precedence if both are provided)

#### URL format requirements

* Format: `https://<REVERSE_PROXY>:<REVERSE_PROXY_PORT>/communication`
* `<REVERSE_PROXY>` must be a fully qualified domain name (FQDN), IPv4, or IPv6 address
* `<REVERSE_PROXY_PORT>` is optional and defaults to 443
* `/communication` path is optional
* Multiple URLs must be separated by commas

#### Examples

```
# Set single outgoing endpoint



agctl outgoing-endpoint set https://proxy.example.com:443



# Set multiple endpoints



agctl outgoing-endpoint set https://proxy1.example.com:443,https://proxy2.example.com:8443/communication



# Set using named parameter



agctl outgoing-endpoint set --value=https://proxy.example.com/communication



# Get current configuration



agctl outgoing-endpoint get



# Clear configuration



agctl outgoing-endpoint clear
```

### Properties

Set multiple properties based on a provided configuration file. This command allows you to apply a complete configuration from a `.properties` file.

For details on ActiveGate properties, see [Configuration properties and parameters](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").

#### Usage

```
agctl properties set <PATH>



agctl properties set --value=<PATH>



agctl properties help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Apply configuration from a properties file |
| `help` | Show help for the properties command |

#### Parameters for set

**Required (one of):**

* `<PATH>`: Path to a `.properties` file provided as a positional argument
* `--value=<PATH>`: Path to a `.properties` file provided as a named parameter (takes precedence if both are provided)

#### Requirements

* File must have a `.properties` extension
* File must exist and be readable

#### Examples

```
# Apply configuration from a properties file



agctl properties set myconfig.properties



# Apply configuration using absolute path



agctl properties set --value=/home/user/activegate/myconfig.properties
```

### Property

Manage individual custom properties. This command sets, gets, or clears specific properties in the ActiveGate configuration.

For details on configuration sections and properties, see [Configuration properties and parameters](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").

#### Usage

```
agctl property set --section=<SECTION> --key=<KEY> --value=<VALUE>



agctl property get --section=<SECTION> --key=<KEY>



agctl property clear --section=<SECTION> --key=<KEY>



agctl property help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure a specific property |
| `get` | Display a specific property value |
| `clear` | Remove a specific property |
| `help` | Show help for the property command |

#### Parameters for set

**Required:**

* `--section=<SECTION>`: Configuration section name
* `--key=<KEY>`: Property key name
* `--value=<VALUE>`: Property value to set (multiple values can be comma-separated)

#### Parameters for get and clear

**Required:**

* `--section=<SECTION>`: Configuration section name
* `--key=<KEY>`: Property key name

#### Examples

```
# Set a property



agctl property set --section=collector --key=group --value=my.group



# Get a property value



agctl property get --section=collector --key=group



# Clear a property



agctl property clear --section=collector --key=group
```

### SSL certificate

Manage custom SSL certificate configuration for ActiveGate. This allows you to configure ActiveGate to use your own SSL certificate.

For details, see [Configure custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

#### Usage

```
agctl ssl-certificate set --certificate=<PATH> --key=<PATH> [--pem-password=<STRING>] [--password=<STRING>] [--alias=<STRING>]



agctl ssl-certificate get



agctl ssl-certificate clear



agctl ssl-certificate help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure a custom SSL certificate |
| `get` | Display current SSL certificate configuration |
| `clear` | Remove current SSL certificate configuration |
| `help` | Show help for the ssl-certificate command |

#### Parameters for set

**Required:**

* `--certificate=<PATH>`: Path to the certificate file in PEM format
* `--key=<PATH>`: Path to the private key file in PEM format

**Optional:**

* `--pem-password=<STRING>`: Password for the private key (if encrypted)
* `--password=<STRING>`: Password to encrypt the keystore (default: randomly generated)
* `--alias=<STRING>`: Certificate alias in the keystore (default: 1)

#### Notes

* Certificate and key files must exist and be in PEM format
* The keystore is created in the ActiveGate SSL directory
* See also: [Configure custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.")

#### Examples

```
# Set SSL certificate with minimum parameters



agctl ssl-certificate set --certificate=cert.crt --key=key.pem



# Set SSL certificate with all parameters



agctl ssl-certificate set --certificate=cert.crt --key=key.pem --pem-password=secret --password=changeit --alias=mycert



# Get current SSL certificate configuration



agctl ssl-certificate get



# Clear SSL certificate configuration



agctl ssl-certificate clear
```

### SSL port

Manage the HTTPS port configuration for ActiveGate. This allows you to change the port that ActiveGate uses for HTTPS communication.

#### Usage

```
agctl ssl-port set <PORT>



agctl ssl-port set --value=<PORT>



agctl ssl-port get



agctl ssl-port clear



agctl ssl-port help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure the HTTPS port |
| `get` | Display the current HTTPS port |
| `clear` | Remove custom HTTPS port (revert to default) |
| `help` | Show help for the ssl-port command |

#### Parameters for set

**Required (one of):**

* `<PORT>`: HTTPS port number provided as a positional argument
* `--value=<PORT>`: HTTPS port number provided as a named parameter (takes precedence if both are provided)

#### Port requirements

* Valid port range: 1-65535
* Using a port below 1024 requires elevated privileges on non-Windows systems

#### Examples

```
# Set HTTPS port using positional argument



agctl ssl-port set 9999



# Set HTTPS port using named parameter



agctl ssl-port set --value=8443



# Get current HTTPS port



agctl ssl-port get



# Clear custom port configuration



agctl ssl-port clear
```

### Support archive

Create a support archive for troubleshooting ActiveGate issues. The support archive contains diagnostic data, logs, and configuration information.

See also: [Collect diagnostic data with agctl](/managed/ingest-from/dynatrace-activegate/activegate-diagnostics#collect-diagnostic-data-with-agctl "Learn how to run ActiveGate diagnostics").

#### Usage

```
agctl support-archive create [--directory=<PATH>] [--days=<NUMBER>] [--modules=<MODULES>] [--stdout]



agctl support-archive help
```

#### Operations

| Operation | Description |
| --- | --- |
| `create` | Generate a support archive for troubleshooting |
| `help` | Show help for the support-archive command |

#### Parameters for create

**All parameters are optional:**

* `--directory=<PATH>`: Output directory for the support archive (default: current working directory)
* `--days=<NUMBER>`: Number of days of data to collect (default: 30)
* `--modules=<MODULES>`: Comma-separated list of modules to include (default: all modules)
* `--stdout`: Stream the support archive ZIP to stdout and console logs to stderr

#### Examples

```
# Create support archive with default settings



agctl support-archive create



# Create support archive for specific time period and modules



agctl support-archive create --directory=/home/user --days=3 --modules=MSGrouter,metrics_ingest



# Create support archive and output to stdout (useful for containers)



agctl support-archive create --stdout 1> sa.zip 2> out.txt
```

#### Use in containerized environments

For containerized ActiveGate deployments, you can use the `--stdout` parameter to extract the support archive:

Kubernetes

OpenShift

```
kubectl exec -n <namespace> <pod-name> -- agctl support-archive create --stdout > ag-support-archive.zip
```

```
oc exec -n <namespace> <pod-name> [-c <container>] -- agctl support-archive create --stdout > ag-support-archive.zip
```

The contents of the support archive are written to `stdout`, allowing them to be redirected to a ZIP file. Other output is sent to `stderr` to maintain the integrity of the archive file.

Windows PowerShell not supported

Make sure to use the command prompt (`cmd.exe`) on Windows; PowerShell isn't supported.

### Trust store

Manage trust store configuration for ActiveGate. The trust store contains trusted root certificates for SSL/TLS connections.

For details, see [Configure trusted root certificates on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections.").

#### Usage

```
agctl trust-store set --certificates=<PATH> [--truststore=<FILE>] [--password=<STRING>]



agctl trust-store get



agctl trust-store clear



agctl trust-store help
```

#### Operations

| Operation | Description |
| --- | --- |
| `set` | Configure the trust store |
| `get` | Display current trust store configuration |
| `clear` | Remove current trust store configuration |
| `help` | Show help for the trust-store command |

#### Parameters for set

**Required:**

* `--certificates=<PATH>`: Path to the chain of certificates in PEM format

**Optional:**

* `--truststore=<FILE>`: File name to create in the ActiveGate SSL directory (default: `mytruststore.p12`)
* `--password=<STRING>`: Password used for the trust store (default: `changeit`)

#### Notes

* The trust store is created in the ActiveGate SSL directory
* Certificates must be in PEM format
* See also: [Configure trusted root certificates on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections.")

#### Examples

```
# Set trust store with custom filename and password



agctl trust-store set --certificates=certs.crt --truststore=superstore.p12 --password=changeit



# Set trust store with default settings



agctl trust-store set --certificates=certs.crt



# Get current trust store configuration



agctl trust-store get



# Clear trust store configuration



agctl trust-store clear
```

### Version

Get the ActiveGate version information.

#### Usage

```
agctl version get



agctl version help
```

#### Operations

| Operation | Description |
| --- | --- |
| `get` | Display the current ActiveGate version |
| `help` | Show help for the version command |

#### Examples

```
# Get ActiveGate version



agctl version get
```

## Common use cases

Remember to [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") after making configuration changes for them to take effect.

### Initial ActiveGate configuration

After installing ActiveGate, you might want to configure multiple settings at once:

```
# Set ActiveGate group



agctl group set production.activegate



# Configure network zone



agctl network-zone set production.zone
```

### Configure reverse proxy

To set up ActiveGate behind a reverse proxy:

```
# Configure outgoing endpoint for ActiveGate to Dynatrace traffic



agctl outgoing-endpoint set https://proxy.example.com:443/communication



# Configure incoming endpoint for OneAgent to ActiveGate traffic



agctl incoming-endpoint set https://proxy.example.com:443/communication
```

### Module management

Enable specific modules based on your monitoring needs:

```
# Enable required modules



agctl modules enable MSGrouter,metrics_ingest



# Verify enabled modules



agctl modules get
```

### SSL certificate configuration

Configure a custom SSL certificate for ActiveGate:

```
# Set custom SSL certificate



agctl ssl-certificate set --certificate=/path/to/cert.crt --key=/path/to/key.pem --password=mypassword



# Verify configuration



agctl ssl-certificate get
```

### Troubleshooting

Create a support archive when experiencing issues:

```
# Create support archive for the last 7 days and save it to /tmp directory



agctl support-archive create --days=7 --directory=/tmp
```

## See also

* [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.")
* [Configuration properties and parameters of ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.")
* [ActiveGate diagnostics](/managed/ingest-from/dynatrace-activegate/activegate-diagnostics "Learn how to run ActiveGate diagnostics")
* [Customize installation for ActiveGate](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.")
* [Configure custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.")
* [Configure trusted root certificates on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections.")
* [Set up reverse proxy for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.")
* [Set up reverse proxy for OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Configure ActiveGate properties to set up a reverse proxy or a load balancer for OneAgent.")