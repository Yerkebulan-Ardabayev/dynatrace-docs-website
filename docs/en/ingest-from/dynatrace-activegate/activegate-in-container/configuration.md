---
title: Containerized ActiveGate configuration
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration
scraped: 2026-02-19T21:26:12.083967
---

# Containerized ActiveGate configuration

# Containerized ActiveGate configuration

* Latest Dynatrace
* 6-min read
* Published Sep 01, 2023

An ActiveGate container can be configured to some degree using container-specific methods via variables or secrets. More advanced settings require providing an ActiveGate `custom.properties` file. See [Advanced configuration](#advanced-configuration) to learn how to use Kubernetes mechanisms such as `ConfigMap` to map it into the `custom.properties`.

Sensitive information

To ensure security, you must pass the sensitive information to an ActiveGate container in a file containing a secret.

## Environment configuration

An ActiveGate container image does not hold any configuration related to your environment.

See below for the mandatory configuration settings to make your ActiveGate container work.

### Communication endpoints

This is a comma-separated list of the communication endpoints to be used by ActiveGate to send data to your Dynatrace environment.

To determine the endpoints, use [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.") in the Dynatrace API.

Environment variable

`DT_SERVER`

Mandatory?

### Environment ID

The Dynatrace [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

Environment variable

`DT_TENANT`

Mandatory?

### Token

The [tenant token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") is used by OneAgents and ActiveGates to report data to Dynatrace. Dynatrace automatically generates the tenant token for your ActiveGate.

To determine the token, use [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.") in the Dynatrace API.

Secret as a file

`/var/lib/dynatrace/secrets/tokens/tenant-token`

Mandatory?

### ActiveGate token

ActiveGate requires a unique ActiveGate token to authorize in the Dynatrace Cluster.

For instructions, see [Generate ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.").

Secret as a file

`/var/lib/dynatrace/secrets/tokens/auth-token`

Mandatory?

## Deployment settings

### Activation group

Defines the ActiveGate group to which the ActiveGate belongs. An ActiveGate can belong to only one group. The name of an ActiveGate group is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a group name. The length of the string is limited to 256 characters. You can use ActiveGate groups to perform bulk actions on your ActiveGates, such as managing [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on ActiveGates. If you want to assign your ActiveGate to a group, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Environment variable

Example

`DT_GROUP`

`myGroup`

### Network zone

Defines the [network zone](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") to which the ActiveGate belongs. An ActiveGate can belong to only one network zone. The name of a network zone is a string of alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`). Dots are used as separators, so you must not use a dot as the first character of a network zone name. The length of the string is limited to 256 characters.

Environment variable

Example

`DT_NETWORK_ZONE`

`myNetworkZone`

## Enabled modules

Containerized ActiveGate does not enable any functionalities by default. Enabled modules need to be specified using the `DT_CAPABILITIES` environment variable. Add a comma-separated list of module names as the variable value.

Environment variable

Example

`DT_CAPABILITIES`

`azure_monitoring,MSGrouter`

See [ActiveGate modules](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.") for a complete list. Generally, you should refer to the `custom.properties` section names as the module names, for example, `cloudfoundry_monitoring`.

The exceptions to this rule are the following modules that are stored in the `[collector]` section.

* `MSGrouter`âEnables message routing
* `restInterface`âEnables REST API module
* `java-script-agent-servlet`âEnables JavaScript agent

Not all modules are supported

Not all modules are supported in containerized deployments yet. For more information, see [ActiveGate purposes and functionality](/docs/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.").

## Network settings

### Proxy

The proxy used for communication with the Dynatrace Cluster to which ActiveGate sends data.

Secret as a file

Description

`/var/lib/dynatrace/secrets/internal-proxy/host`

Server address.

`/var/lib/dynatrace/secrets/internal-proxy/port`

Optional Port. If left empty, the default 8080 port is used.

`/var/lib/dynatrace/secrets/internal-proxy/scheme`

ActiveGate version 1.289+

Optional Scheme. If left empty, the default `http` scheme is used. This applies the most common setup, where the connection to the proxy is initiated using HTTP and automatically upgraded to a secure one. All further ActiveGate communication through the proxy is secured by SSL/TLS.

Must be set to `https` for proxies that do not support HTTP at all.

`/var/lib/dynatrace/secrets/internal-proxy/username`

Optional User name.

`/var/lib/dynatrace/secrets/internal-proxy/password`

Optional Password, see [Proxy password requirements](#proxy-password-requirements).

#### Advanced scenarios

For more advanced scenarios where one or more proxies are used for means other than communication with the Dynatrace Cluster, see [Proxy for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy."). Once you have crafted the required configuration, you can provide it to the ActiveGate container as a [custom.properties](#advanced-configuration) file.

#### Rules for the proxy password

The proxy password needs to meet the following requirements.

| Requirements | Corresponding characters |
| --- | --- |
| Characters allowed | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
| Characters not allowed | blank space ' ` , & = + % \ |

### Load balancer between ActiveGate and OneAgents

Dynatrace OneAgent accesses the ActiveGate via an auto-detected endpoint list. If a load balancer is placed on the path from OneAgent to the ActiveGate, such as Kubernetes [Serviceï»¿](https://kubernetes.io/docs/concepts/services-networking/service/), you need to explicitly set the endpoint to be used by OneAgents.

Environment variable

Example value

`DT_DNS_ENTRY_POINT`

`https://sg1.mydomain.com:9999`

### Load balancer between ActiveGate and the Dynatrace Cluster

A reverse proxy or a load balancer can be placed on the path from an ActiveGate to the Dynatrace Cluster. This allows your ActiveGate to connect to any available node of the Cluster, spreading the load between the nodes.  
To do this, you need to:

* Provide the address of the reverse proxy/load balancer.
* Ensure that ActiveGate will ignore any further target address information sent from the Dynatrace Cluster, and will thus connect only to the address you have specified.

![ActiveGate connecting to Dynatrace Cluster via reverse proxy/load balancer](https://dt-cdn.net/images/rev-proxy-001-1000-f7d875625b.png)

In this scenario, you need to set the following environment variables.

Environment variable

Example value

`DT_SERVER`

`https://load.balancer.com:9999`

`DT_IGNORE_CLUSTER_RUNTIME_INFO`

`true`

## SSL settings

### Custom SSL certificate

ActiveGate will serve a custom certificate instead of the default one. To configure this, you need a file in `PKCS#12` format that contains a private key and its corresponding certificate chain. For more information, see [Custom SSL certificate for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

Secret as a file

Description

`/var/lib/dynatrace/secrets/tls/server.p12`

Certificate file

`/var/lib/dynatrace/secrets/tls/password`

Optional Certificate password

`/var/lib/dynatrace/secrets/tls/alias`

Optional Certificate alias. The value must be specified in lower case.

### Trusted root certificates

Additional trusted root certificates can be used by ActiveGate. To configure this, you need a file in the `PEM` format that contains a list of certificates to be included in the trust store. For more information, see [Trusted root certificates for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to specify a custom truststore file that is merged with Java's root certificates and used as a default on all connections.").

Secret as a file

Description

`/var/lib/dynatrace/secrets/rootca/rootca.pem`

Certificate file

### HTTP port

An ActiveGate container by default opens HTTPS port `9999`. If you require your ActiveGate to communicate over plain HTTP, you need to explicitly specify the HTTP port.

Environment variable

Example

`DT_HTTP_PORT`

`8888`

## Advanced configuration

In addition to the configuration settings passed via environment variables or files, you can configure all other [configuration settings](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") by providing the contents of the `custom.properties` file.

1. Define `ConfigMap`.

   ```
   kind: ConfigMap



   apiVersion: v1



   data:



   custom.properties: |-



   [vmware_monitoring]



   vmware_monitoring_enabled = true



   metadata:



   name: vmware-config



   namespace: dynatrace
   ```
2. Reference `ConfigMap` in your deployment file.

   ```
   [...]



   volumeMounts:



   [...]



   - name: ag-conf



   mountPath: /var/lib/dynatrace/gateway/config_template/custom.properties



   subPath: custom.properties



   [...]



   volumes:



   - name: ag-conf



   configMap:



   name: vmware-config



   items:



   - key: custom.properties



   path: custom.properties
   ```