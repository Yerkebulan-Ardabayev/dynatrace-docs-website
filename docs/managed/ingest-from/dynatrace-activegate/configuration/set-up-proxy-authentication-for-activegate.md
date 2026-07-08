---
title: Proxy for ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate
---

# Proxy for ActiveGate

# Proxy for ActiveGate

* 5-min read
* Updated on Jun 09, 2026

Your ActiveGate connectivity configuration allows you to define one or more proxies for outgoing connections: You can use a [single proxy for all outgoing traffic](#proxy-for-cluster-aws-vmware-azure), or you can specify **different proxies for different purposes**, or you can even **define exceptions by turning off proxy use for specific connections**, while using proxies for other connections.

To see this configuration in a wider context, refer to the [supported connectivity schemes](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") and in particular to the [proxy and load balancer configuration](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#proxies "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").

## Proxy configuration properties

ActiveGate proxy configuration consists of the following settings. Depending on the type of communication for which you want to use (or disable) a proxy, the following configuration properties can appear in [different configuration sections](#advanced) of your ActiveGate configuration.

| Property | Description |
| --- | --- |
| `proxy-server` | Server address (hostname or IP address) |
| `proxy-port` | Port Optional  If left empty, the default `8080` port is used. |
| `proxy-scheme` | Scheme Optional  If left empty, the default `http` scheme is used. This applies the most common setup, where the connection to the proxy is initiated using HTTP and automatically upgraded to a secure one. All further ActiveGate communication through the proxy is secured by SSL/TLS.  Must be set to `https` for proxies that do not support HTTP at all. |
| `proxy-user` | User name Optional |
| `proxy-domain` | User domain in the case of NTLM authentication |
| `proxy-password` | Password Optional  The password provided in the `proxy-password` property is obfuscated after ActiveGate restart, and the obfuscated password is stored in the `proxy-password-encr` property.  If a comma (`,`) is part of a value, you need to add an escape backslash (`\`) before the comma. For example, `proxy-password = foo\,bar`. |
| `proxy-off` | If set to `true`, causes proxy to be disabled for the particular type of communication. |
| `proxy-non-proxy-hosts` | A list of hosts for communication with which proxy should not be used by ActiveGate  The hosts in the list should be separated by `|` characters. You can also use an asterisk `*` as a wildcard character to match any string. There can be only one wildcard character, either at the beginning or the end of the hostname. For example, `proxy-non-proxy-hosts=*.foo.com|localhost` indicates that every host in the `foo.com` domain and the `localhost` should be accessed directly even if a proxy server is specified. For a full description of allowed syntax, see the syntax for the `http.nonProxyHosts` parameter in [Networking Properties﻿](https://dt-url.net/kk02v8r).  ActiveGate version 1.335+ CIDR notation is supported for the following technologies:  * `cloudfoundry_monitoring` * `kubernetes_monitoring`  For example, `proxy-non-proxy-hosts=10.0.0.0/8` will disable proxy for addresses in the range `10.0.0.0`–`10.255.255.255`. |
| `proxy-authentication-schemes` | ActiveGate version 1.271+  A list of proxy authentication schemes Optional  This is a prioritized list of proxy authentication schemes that ActiveGate should use when authenticating with the proxy server.  * Starting with the first scheme on the list, ActiveGate will attempt to authenticate and, in case of failure, proceed to the next scheme on the list. * If this property is not defined, ActiveGate will try to authenticate using all available schemes.  Supported values: `NTLM`, `BASIC` |

## Specify proxy configuration for ActiveGate

ActiveGate proxy configuration can be specified during ActiveGate installation on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#linux_proxy "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#windows_proxy "Learn about the parameters that you can use with ActiveGate on Windows.") (only the setting for all outgoing connections), or it can be configured after ActiveGate is installed.

agctl

custom.properties

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Learn how to use agctl to configure and manage ActiveGate from the command line") to configure proxy properties in the `http.client` section:

```
# Set proxy server and port



agctl property set --section=http.client --key=proxy-server --value=127.0.0.1



agctl property set --section=http.client --key=proxy-port --value=8080



# Set basic authentication credentials (if required)



agctl property set --section=http.client --key=proxy-user --value=username



agctl property set --section=http.client --key=proxy-password --value=password
```

After configuring proxy settings with `agctl`, you must [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

Note that after the service is restarted, the proxy password is encrypted and moved from the `proxy-password` property to `proxy-password-encr`.

1. Edit the `custom.properties` file [in the ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")
2. Specify the proxy-related parameters in the appropriate configuration section of the `custom.properties` file, depending for which purpose you want to use the proxy (see examples below). For example:

   ```
   [http.client]



   proxy-server=127.0.0.1



   proxy-port=8080



   # basic authentication credentials



   proxy-user=username



   proxy-password=password
   ```
3. Save the `custom.properties` file.
4. [Restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

   Note that after the service is restarted, the proxy password, as specified by you in the configuration, is encrypted and moved from the `proxy-password` property to `proxy-password-encr`.

## ActiveGate proxy settings for simple proxy configuration scenarios

The following simple proxy configuration scenarios for ActiveGate are the most common and widely used. If you have special and more complex requirements, you can also define an [advanced configuration](#advanced).

### ActiveGate proxy settings for all outgoing traffic

![ActiveGate proxy settings for all outgoing traffic](https://cdn.bfldr.com/B686QPH3/as/hp3r3rfrghg4g673rh5nmkv/ActiveGate-Proxy_settings_for_all_outgoing_traffic-Light_Mode?auto=webp&format=png&position=1)

ActiveGate proxy settings for all outgoing traffic

The following configuration covers the most common case of specifying proxy settings for ActiveGate outgoing connection to both the Dynatrace Cluster as well as monitored technologies, such as AWS, VMware, or Azure.

Specify the proxy-related parameters in the `[http.client]` section of the `custom.properties` file— including those parameters related to authentication, if required:

agctl

custom.properties

ActiveGate version 1.333+

```
# Set proxy server and port



agctl property set --section=http.client --key=proxy-server --value=127.0.0.1



agctl property set --section=http.client --key=proxy-port --value=8080



# Set basic authentication credentials (if required)



agctl property set --section=http.client --key=proxy-user --value=username



agctl property set --section=http.client --key=proxy-password --value=password
```

```
[http.client]



proxy-server=127.0.0.1



proxy-port=8080



# basic authentication credentials



proxy-user=username



proxy-password=password
```

### ActiveGate proxy settings for Dynatrace Cluster only

![ActiveGate proxy settings for Dynatrace Cluster only](https://cdn.bfldr.com/B686QPH3/as/fj8ggn9tspgv85xmmhnc8wsb/ActiveGate-Proxy_settings_for_Dynatrace_Cluster_only-Light_Mode?auto=webp&format=png&position=1)

ActiveGate proxy settings for Dynatrace Cluster only

To set up a proxy specifically for Dynatrace Cluster, while allowing outgoing monitoring traffic to connect directly to monitored technologies, define proxy settings in the `[http.client.internal]` section of ActiveGate configuration.

agctl

custom.properties

ActiveGate version 1.333+

```
# Set proxy server and port



agctl property set --section=http.client.internal --key=proxy-server --value=127.0.0.1



agctl property set --section=http.client.internal --key=proxy-port --value=8080



# Set basic authentication credentials (if required)



agctl property set --section=http.client.internal --key=proxy-user --value=username



agctl property set --section=http.client.internal --key=proxy-password --value=password
```

```
[http.client.internal]



proxy-server=127.0.0.1



proxy-port=8080



# basic authentication credentials



proxy-user=username



proxy-password=password
```

### ActiveGate proxy for outgoing monitoring traffic, with direct connection to Dynatrace Cluster

![ActiveGate proxy for outgoing monitoring traffic only](https://cdn.bfldr.com/B686QPH3/as/t3wh55p62fbf4h9w26nrwjr/ActiveGate-Proxy_for_outgoing_monitoring_traffic-Light_Mode?auto=webp&format=png&position=1)

ActiveGate proxy for outgoing monitoring traffic only

To set up a proxy specifically for outgoing monitoring traffic, but keep connection to Dynatrace Cluster direct:

* Specify proxy configuration in the `[http.client]` section of the `custom.properties` file.
* Turn proxy off in the `[http.client.internal]` section.

**For example:**

agctl

custom.properties

ActiveGate version 1.333+

```
# Set proxy for all traffic in http.client section



agctl property set --section=http.client --key=proxy-server --value=127.0.0.1



agctl property set --section=http.client --key=proxy-port --value=8080



agctl property set --section=http.client --key=proxy-user --value=username



agctl property set --section=http.client --key=proxy-password --value=password



# Disable proxy for Dynatrace Cluster communication



agctl property set --section=http.client.internal --key=proxy-off --value=true
```

```
[http.client]



proxy-server=127.0.0.1



proxy-port=8080



# basic authentication credentials



proxy-user=username



proxy-password=password



[http.client.internal]



proxy-off=true
```

## Advanced proxy configuration scenarios for ActiveGate

To set up a proxy for **outgoing connections from ActiveGate**—that is for connections to monitored technologies or to the Dynatrace Cluster—edit the [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") file and set properties in the appropriate section. Depending on the configuration section in which the properties are specified, the proxy (and other communication settings) affect only selected types of connections:

* `[http.client]`—proxy settings for all ActiveGate outgoing connections, including the Dynatrace Cluster as well as all monitored technologies.
* `[http.client.internal]`—proxy settings specifically for the communication with Dynatrace Cluster. These settings override the settings specified in `[http.client]`
* `[http.client.external]`—proxy settings specifically for monitored technologies: CloudFoundry, Kubernetes, private Synthetic monitoring. These settings override the settings specified in `[http.client]`
* `[<technology name>]`—proxy settings specifically for the particular monitored technology, such as `cloudfoundry_monitoring`, `kubernetes_monitoring`, `synthetic`. These settings override the settings specified in `[http.client]` and `[http.client.external]`. Note that Settings for many of these technologies can be specified jointly in `[http.client.external]`.

This precedence and inheritance of configuration settings between different configuration sections can be pictured graphically as follows:

![Proxy inheritance](https://cdn.bfldr.com/B686QPH3/as/7qvbpp4prm5qks5b6m6x7mxv/ActiveGate-Advanced_proxy_configuration_scenarios_for_ActiveGate-Light_Mode?auto=webp&format=png&position=1)

Proxy inheritance

### ActiveGate proxy for Kubernetes, CloudFoundry, and private Synthetic Monitoring

You can specify proxy settings for a number of monitored technologies at once. Settings given in the `http.client.external` section affect Kubernetes, CloudFoundry, and private Synthetic monitoring (this set might be extended in the future):

agctl

custom.properties

ActiveGate version 1.333+

```
# Set proxy server and port for external monitoring traffic



agctl property set --section=http.client.external --key=proxy-server --value=127.0.0.1



agctl property set --section=http.client.external --key=proxy-port --value=8080



# Set basic authentication credentials (if required)



agctl property set --section=http.client.external --key=proxy-user --value=username



agctl property set --section=http.client.external --key=proxy-password --value=password
```

```
[http.client.external]



proxy-server=127.0.0.1



proxy-port=8080



# basic authentication credentials



proxy-user=username



proxy-password=password
```

### Different proxies for Kubernetes, CloudFoundry and private Synthetic Monitoring

You can also specify dedicated proxy settings for a particular monitored technology:

* CloudFoundry in the `cloudfoundry_monitoring` section
* Kubernetes in the `kubernetes_monitoring` section
* private Synthetic Monitoring in the `synthetic` section

**For example:**

agctl

custom.properties

ActiveGate version 1.333+

```
agctl property set --section=kubernetes_monitoring --key=proxy-server --value=127.0.0.1



agctl property set --section=kubernetes_monitoring --key=proxy-port --value=8080



agctl property set --section=kubernetes_monitoring --key=proxy-user --value=username



agctl property set --section=kubernetes_monitoring --key=proxy-password --value=password
```

```
[kubernetes_monitoring]



proxy-server=127.0.0.1



proxy-port=8080



# basic authentication credentials



proxy-user=username



proxy-password=password
```

**See also:** [How to set up an ActiveGate proxy for private Synthetic monitoring](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")

### ActiveGate proxy settings for AWS role-based access

[AWS-specific proxy configuration](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/troubleshoot-aws-monitoring-setup#proxy "Troubleshoot your Dynatrace deployment for AWS monitoring.") is described separately.