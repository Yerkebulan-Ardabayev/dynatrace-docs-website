# Dynatrace Documentation: ingest-from/edgeconnect.md

Generated: 2026-02-16

Files combined: 1

---


## Source: edgeconnect.md


---
title: Configure and deploy EdgeConnect
source: https://www.dynatrace.com/docs/ingest-from/edgeconnect
scraped: 2026-02-15T21:22:17.659873
---

# Configure and deploy EdgeConnect

# Configure and deploy EdgeConnect

* Latest Dynatrace
* How-to guide
* 24-min read
* Updated on Oct 16, 2025

Use EdgeConnect to make apps and workflows interact securely with your systems. EdgeConnect is available as a Docker container and can run in any container runtime environment.

In the following schematic, arrows point in the direction of connection initiation. EdgeConnect connects itself to AppEngine and runs a user-defined subset of HTTP(S) requests inside the desired network on behalf of the Dynatrace runtime.

![EdgeConnect connectivity scheme](https://dt-cdn.net/images/edgeconnect-security-801-2e3e1a781e.webp)

EdgeConnect can also operate behind an HTTP proxy:

![EdgeConnect behind a proxy](https://dt-cdn.net/images/edgeconnect-proxy-1000-f43df1adec.webp)

## Configure EdgeConnect

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Select  **New EdgeConnect**.
3. Enter the **Name** and the **Host patterns**.

### User permissions

A regular platform user is only granted read-only access for EdgeConnect configurations through `app-engine:edge-connects:read` permission bound to the Standard and Pro user [default policies](/docs/manage/identity-access-management/permission-management/default-policies#access "Dynatrace default policies reference").

If you want to configure EdgeConnect so that it can connect to your environment, your user needs to belong to a group bound to the policy with specific IAM permissions.

The Admin [default policy](/docs/manage/identity-access-management/permission-management/default-policies#access "Dynatrace default policies reference") already contains the necessary scopes, so an admin user can fully manage EdgeConnect configurations by default.

If you need to create your own policy for your admin users, you need to include the following permissions in your policy.

#### Read EdgeConnect configurations

```
ALLOW app-engine:edge-connects:read;
```

#### Create a new EdgeConnect configuration

```
ALLOW app-engine:edge-connects:write, oauth2:clients:manage WHERE oauth2:scopes = "app-engine:edge-connects:connect";
```

You need OAuth client management permission to create the OAuth client for a new EdgeConnect.

#### Update an EdgeConnect configuration:

```
ALLOW app-engine:edge-connects:write;
```

#### Rotate the OAuth client secret of an EdgeConnect

```
ALLOW oauth2:clients:manage where oauth2:scopes="app-engine:edge-connects:connect";
```

#### Delete an EdgeConnect

```
ALLOW app-engine:edge-connects:delete, oauth2:clients:manage WHERE oauth2:scopes = "app-engine:edge-connects:connect";
```

You need OAuth client management permission to delete the OAuth client for an EdgeConnect.

To adjust the policies and group memberships of users, go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** and select **People**, **Groups**, or **Policies**. For more information, see [Manage IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

### Create a new EdgeConnect configuration

Before [deploying an EdgeConnect](#deploy) in your network, you need to map specific HTTP request host patterns to specific EdgeConnect instances.

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Select  **New EdgeConnect**.

   * Enter a unique name for the EdgeConnect instance.

     + Name must be [RFC 1123 Label Namesï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names) compliant with maximum length of 50 characters
   * Provide the host patterns of the requests that should be handled by the EdgeConnect instance.

     You can use a wildcard to replace the first parts of the host domain. For example, `*.myapp.org` matches `staging.myapp.org` and `prod.myapp.org`.
3. Select **Create**.
4. Download the `edgeConnect.yaml` configuration file that was created. This file is the configuration file that needs to be used for configuring the EdgeConnect image to be run [in the next section](#config).

   Be aware that the OAuth client secret is only displayed to you once and can not be retrieved later on. Subsequently, the configuration file can still be downloaded but the OAuth client secret won't be preset anymore.

Any HTTP request (from your app functions, workflows, or ad-hoc functions) that matches a defined host pattern is handled by an EdgeConnect instance that you specify in that configuration.

For example, given a host pattern of `staging.myapp.org` in its configuration, the Dynatrace runtime will route an HTTP request with the URL `https://staging.myapp.org/test.html` to that EdgeConnect.

Now you're ready to deploy the respective EdgeConnect in your network.

## Deploy EdgeConnect

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Ensure connectivity**](#connectivity)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure EdgeConnect image**](#config)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Get EdgeConnect container image**](#image)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Run the container**](#run)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Validate the connection**](#validate)

Complete the following steps to get your EdgeConnect up and running.

### Step 1 Ensure connectivity

EdgeConnect needs to be able to connect to Dynatrace and your internal systems.

#### Connectivity to Dynatrace

EdgeConnect initiates the following connections to operate.

* `https://sso.dynatrace.com/sso/oauth2/token`
* `https://<your environment ID>.apps.dynatrace.com`

EdgeConnect does not require any inbound connection from Dynatrace.

#### Connectivity in your network

EdgeConnect requires connectivity to any application in your network that you want Dynatrace to connect to for app functions, ad-hoc functions, or workflow actions. If your EdgeConnect communicates behind a proxy over HTTPS, you also need to add the trusted certificates of the hosts EdgeConnect connects to. If the HTTP proxy performs the TLS interception, you also need to add the certificate of this proxy. For instructions, see [certificates](#run-certificates).

### Step 2 Configure EdgeConnect image

The EdgeConnect docker container needs an `edgeConnect.yaml` configuration file that should be downloaded from **Settings** >  **General** > **External Requests** when you initially [created the configuration](#createconfiguration).
You reference the file when you run the EdgeConnect docker image.

Note that you need to reference the `name`, `oauth.client_id`, and `oauth.client_secret` as configured in the app. Otherwise, EdgeConnect won't be allowed to connect to the platform.

Example `edgeConnect.yaml`

```
name: my-corporate-network



api_endpoint_host: abc12345.apps.dynatrace.com



oauth:



endpoint: https://sso.dynatrace.com/sso/oauth2/token



client_id: <DYNATRACE_TOKEN_PLACEHOLDER>



client_secret: *******



resource: urn:dtenvironment:abc12345



restrict_hosts_to:



- "internal.example.org"



- "*.example.com"



certificate_paths:



- "/path/to/some/certificate.cer"



- "/path/to/another/certificate.pem"



proxy:



server: proxy.example.org



port: 8037



exceptions:



- "*.foo.com"



- "noproxy.example.org"



auth:



user: "proxy-user"



password: "*******"



secrets:



- name: My secret



token: <DYNATRACE_TOKEN_PLACEHOLDER>.some-token-secret



from_env: MY_SECRET



restrict_hosts_to:



- dynatrace.com



- name: My other secret



token: <DYNATRACE_TOKEN_PLACEHOLDER>.another-token-secret



from_file: /path/to/my/other/secret



restrict_hosts_to:



- internal.example.com
```

You can override certain configuration values via environment variables.
Refer to the table below for environment variable names of each field.

#### Field descriptions

The `edgeConnect.yaml` fields and the names of the corresponding environment variables are described in the table below.
Please note that some environment variable names use both single (`_`) and double underscore symbols (`__`).

Field

Environment Variable

Description

`name`

`EDGE_CONNECT_NAME`

The technical identifier of the EdgeConnect.

This has to match the name that was specified in the [configuration added in the app](#appconfigurations).

`api_endpoint_host`

`EDGE_CONNECT_API_ENDPOINT_HOST`

Your environment base URL.

`oauth.endpoint`

`EDGE_CONNECT_OAUTH__ENDPOINT`

The token endpoint URL of Dynatrace SSO.

`oauth.client_id`

`EDGE_CONNECT_OAUTH__CLIENT_ID`

The ID of the OAuth client that was created along with the [EdgeConnect configuration](#appconfigurations).

`oauth.client_secret`

`EDGE_CONNECT_OAUTH__CLIENT_SECRET`

The secret of the OAuth client that was created along with the [EdgeConnect configuration](#appconfigurations).

`oauth.resource`

`EDGE_CONNECT_OAUTH__RESOURCE`

The URN identifying your tenant.

`restrict_hosts_to` Optional

`EDGE_CONNECT_RESTRICT_HOSTS_TO`

Restricts outgoing HTTP requests to specified hosts.

* You can use a wildcard to replace the first parts of the host domain. For example, `*.myapp.org` will match `staging.myapp.org` and `prod.myapp.org`. Use a YAML list or separate multiple entries with commas.
* If `restrict_hosts_to` is configured, any other requests are rejected, including host patterns specified in [host pattern mapping](#appconfigurations) that don't match this configuration.
* `restrict_hosts_to` is only used to additionally restrict connections. You still need to create [host pattern mapping](#appconfigurations) for EdgeConnect to be able to connect to your internal resources.

`certificate_paths` Optional

`EDGE_CONNECT_CERTIFICATE_PATHS`

For communication over TLS-encrypted channels (HTTPS and secure WebSockets), EdgeConnect verifies the identity of a host based on its certificate. The parameter lists such certificates. You must mount these certificates into the EdgeConnect container. The parameter lists the paths to certificates in the container itself. For more information, see [certificates](#run-certificates) instructions.

EdgeConnect supports certificate files in the PEM (`.pem`, `.crt`, or `.cer`) and DER (`.der`) formats.

`proxy.server` Optional

`EDGE_CONNECT_PROXY__SERVER`

Server address (hostname or IP address) of the proxy.

`proxy.port` Optional

`EDGE_CONNECT_PROXY__PORT`

Port of the proxy.

`proxy.exceptions` Optional

`EDGE_CONNECT_PROXY__EXCEPTIONS`

A list of hosts for which EdgeConnect should *not* use the configured proxy for communication.

You can use a wildcard to replace the first parts of a host domain. For example, `*.myapp.org` will match `staging.myapp.org` and `prod.myapp.org`. Use a YAML list or separate multiple entries with commas.

`proxy.auth.user` Optional

`EDGE_CONNECT_PROXY__AUTH__USER`

User name for authentication with the proxy, using the "Basic" HTTP authentication scheme.

`proxy.auth.password` Optional

`EDGE_CONNECT_PROXY__AUTH__PASSWORD`

Password for authentication with the proxy, using the "Basic" HTTP authentication scheme.

`secrets` Optional

N/A

An optional list of secrets. Refer to [the table below](#edgeconnect-yaml-secrets-fields) for details on how the list items are structured.

##### Secrets

Whenever requests are sent to services outside the Dynatrace platform, secrets are likely required to authenticate these service interactions (e.g., API tokens or secrets within webhook URLs).
However, your apps and workflows should never contain plain secret values to avoid unintended leakage.

Instead, EdgeConnect offers support for placeholder tokens that you can use in your requests' query parameters, headers, and bodies.
EdgeConnect then securely replaces occurrences of these tokens on the fly with actual secret values that you configure in your `edgeConnect.yaml` file.

This section explains how to configure such secrets.
EdgeConnect can read secrets from two sources: from environment variables or from files mounted into your EdgeConnect container.

Field

Environment Variable

Description

`name`

N/A

A human-readable name that identifies your secret. Used for logging purposes.

`token`

N/A

A placeholder for secrets that you can include in your requests. EdgeConnect will replace occurrences of `token` in query parameters, headers, and bodies by the secret's actual value.

Secret tokens need to adhere to the following format: `dt0e01.<token_name>.<token_secret>`, where `<token_name>` has to be a base-32 string of length 15 and `<token_secret>` has to be a base-32 string of length 40.

On Linux, you can use the following command to generate a cryptographically secure token:

```
echo "dt0e01.`openssl rand -out /dev/stdout 15 \



| base32 \



| tr '[:lower:]' '[:upper:]'`.`\



openssl rand -out /dev/stdout 40 \



| base32 \



| tr '[:lower:]' '[:upper:]'`"
```

Note that this command requires `openssl` to be available on your system as well as the `base32` utility (which is part of GNU coreutils and is typically pre-installed on popular distributions).

`from_env` Optional

N/A

The environment variable that holds the actual secret value. Note that exactly one of `from_env` or `from_file` must be configured.

`from_file` Optional

N/A

The file that contains the actual secret value. Note that exactly one of `from_env` or `from_file` must be configured.

`restrict_hosts_to`

N/A

The hosts that this secret is restricted to. Only if a request targets one of the hosts in this list, its query parameters, headers and body will be scanned for occurrences of `token` which will be replaced by the actual secret value.
Requests to hosts that aren't covered by `restrict_hosts_to` will fail if they contain the given `token` to avoid its accidental leakage to mistrusted hosts.

If you run [EdgeConnect in Kubernetes via Dynatrace Operator](#kubernetes), the above fields are configured using the parameters of a custom Kubernetes resource as explained in [EdgeConnect parameters for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters "List of configuration parameters for EdgeConnect.").

### Step 3 Get EdgeConnect container image

To run the EdgeConnect container, you first need to get the image.

#### Verify EdgeConnect container image

Dynatrace provides signed container images to ensure authenticity and integrity, along with a Software Bill of Materials (SBOM) that lists all included software components.
Verifying the signatures and reviewing the SBOMs enables effective vulnerability management and risk mitigation.
For verification details, see [Verify Software Bill of Materials (SBOM) Attestation](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature#sbom-attestation-verification "Verify Dynatrace image signatures").

```
docker pull dynatrace/edgeconnect:latest
```

We recommend that you always run (and regularly upgrade to) the latest available version of EdgeConnect.

You'll be notified on a successful download.

```
Status: Downloaded image for dynatrace/edgeconnect:latest



docker.io/dynatrace/edgeconnect:latest
```

### Step 4 Run the container

1. Go to the directory with the `edgeConnect.yaml` file you created.
2. Run the container.

   ```
   docker run \



   --mount type=bind,src=${PWD}/edgeConnect.yaml,dst=/edgeConnect.yaml \



   -d --restart always \



   dynatrace/edgeconnect \
   ```

Customizing the location of the `edgeConnect.yaml` config file

You can customize the location from where the configuration file is loaded via the environment variable `EDGE_CONNECT_CONFIG_PATH`.

For example, setting `EDGE_CONNECT_CONFIG_PATH` to `/etc/config` will cause EdgeConnect to load the file `/etc/config/edgeConnect.yaml` inside the container's file system.

#### Custom TLS certificates

For communication over TLS-encrypted channels (HTTPS and secure WebSockets), EdgeConnect verifies the identity of a host based on its certificate.

To communicate with hosts that use custom certificates, you must add paths to the certificates to the `certificate_paths` parameter of the `edgeConnect.yaml` file (or to the `EDGE_CONNECT_CERTIFICATE_PATHS` environment variable) and mount the certificates into the EdgeConnect container.
Certificates are usually mounted in `/etc/edge_connect_certs` per convention, but you can also provide a custom directory instead.

EdgeConnect supports certificate files in the PEM (".pem", ".crt" or ".cer") and DER (".der") format.

1. Edit the `edgeConnect.yaml` file and add the target path in your EdgeConnect container where the certificates are stored. For example:

   ```
   certificate_paths:



   - "/etc/edge_connect_certs/certificate.pem"
   ```
2. Mount a custom certificate into the EdgeConnect container. You can use the `-v` parameter when running the container. For example:

   ```
   docker run \



   --mount type=bind,src=${PWD}/edgeConnect.yaml,dst=/edgeConnect.yaml \



   -d --restart always \



   -v /host/path/to/certificate.pem:/etc/edge_connect_certs/certificate.pem



   dynatrace/edgeconnect \
   ```

   Where,

   * `/host/path/to/certificate.pem` is the path to the certificate on the host
   * `/etc/edge_connect_certs/certificate.pem` is the target path in your EdgeConnect container where the certificate file will be mounted

Proxy with TLS interception

If you are using EdgeConnect behind an HTTP proxy that performs TLS interception, it is necessary to add the proxy's certificate to the `certificate_paths` field, to ensure that EdgeConnect can verify the proxy's identity.

##### Troubleshooting

If EdgeConnect aborts an HTTPS connection due to a certificate verification failure, this can be caused by incomplete configuration or invalid SSL certificates. The table below lists common certificate verification errors that might appear as part of the EdgeConnect container logs.

Error Message

Explanation

Suggested Action

"self-signed certificate"

"self-signed certificate in certificate chain"

"unable to get issuer certificate"

"unable to get local issuer certificate"

These errors point out that EdgeConnect fails to verify the CA certificates involved in signing the certificate of the target host EdgeConnect is connecting to.

Please make sure that all certificates that either directly or indirectly sign the target server's certificate are listed in the `certificate_paths` configuration field, as described in the [table above](#edgeconnect-yaml-fields).

"hostname mismatch"

This error is raised when a server presents a certificate that does not match the host name EdgeConnect is trying to connect to.
This can happen, for example, if a TLS connection is intercepted within your network or redirected to a different host.

Please make sure that EdgeConnect's network traffic isn't subject to undesired interception or redirection.

"certificate has expired"

This error indicates that the certificate of the target host, or one of the CA certificates used to sign it, has expired.

Please make sure that all certificates involved in the certificate chain are still valid and renew any expired ones.

#### Secrets

Follow these steps to make EdgeConnect replace secret tokens in your requests:

1. Edit the `edgeConnect.yaml` file and add the corresponding configuration for your secrets (see the [table above](#edgeconnect-yaml-secrets-fields) for field descriptions). The following example illustrates a configuration covering a secret loaded from an environment variable as well as a secret loaded from a file:

   ```
   secrets:



   - name: My secret



   token: <DYNATRACE_TOKEN_PLACEHOLDER>.some-token-secret



   from_env: MY_SECRET



   restrict_hosts_to:



   - dynatrace.com



   - name: My other secret



   token: <DYNATRACE_TOKEN_PLACEHOLDER>.another-token-secret



   from_file: /path/to/my/other/secret



   restrict_hosts_to:



   - internal.example.com
   ```
2. Provide the value for secret environment variables and secret files into your EdgeConnect container. For that purpose, you can use the `-e` parameter to configure values for environment variables passed to the container and the `-v` parameter for mounting secret files. For example:

   ```
   docker run \



   --mount type=bind,src=${PWD}/edgeConnect.yaml,dst=/edgeConnect.yaml \



   -d --restart always \



   -e MY_SECRET=******* \



   -v /host/path/to/my/other/secret:/container/path/to/mounted/secret



   dynatrace/edgeconnect \
   ```

   Where,

   * `MY_SECRET` is the name of the environment variable that holds the secret value of "My secret" (represented by `"*******"`)
   * `/host/path/to/my/other/secret` is the path to the secret file on the host system
   * `/container/path/to/mounted/secret` is the target path in your EdgeConnect container where the secret file is mounted

### Step 5 Validate the connection

Validate the EdgeConnect successfully connected to the platform.

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Check the **Availability** column. It should display **online**.

   * If it's still offline, check the Docker container's logs for error messages.
   * If the app says that there are online EdgeConnect instances, congratulations! You have safely connected your environment to the Dynatrace platform.

     From now on, any HTTP request that occurs as part of an app function, ad hoc function, or workflow action matching a host pattern, will be transparently run by EdgeConnect instead of directly by the Dynatrace runtime.

## Running EdgeConnect in Kubernetes

Dynatrace Operator provides specific support for running EdgeConnect via an EdgeConnect custom resource. There are three deployment scenarios:

* Use the Dynatrace Operator to only deploy the EdgeConnect as described in [Set up EdgeConnect](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect "Deploy and configure EdgeConnect on Kubernetes using Dynatrace."). You still create the EdgeConnect configuration in the app and follow the instructions in **Actions** > **Deploy EdgeConnect** > **Deploy via Dynatrace Operator**.
* Make the Dynatrace Operator provision an EdgeConnect configuration as explained in [Provision EdgeConnect for Dynatrace environment](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision "Provision EdgeConnect for a Dynatrace environment.") so that the Operator will fully manage the lifecycle of EdgeConnect. The Operator will create the configuration itself, and the host patterns of the EdgeConnect are specified in the EdgeConnect custom resource. You can't edit these configurations in the app.
* Set up EdgeConnect without the Dynatrace Operator as described in <#no-operator>.

### Running EdgeConnect in Kubernetes without using the Dynatrace Operator

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Ensure connectivity**](#no-operator-connectivity)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure EdgeConnect deployment**](#no-operator-configure-deployment)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Apply the deployment**](#no-operator-deployment)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Validate the connection**](#no-operator-validate)

Complete the following steps to deploy EdgeConnect on Kubernetes without the Dynatrace Operator.

### Step 1 Ensure connectivity

Follow the instructions in [Ensure connectivity](#connectivity) to make certain that Dynatrace is reachable from your Kubernetes cluster.

### Step 2 Configure EdgeConnect deployment

Download the `edgeConnect.yaml` config when you [create the configuration](#createconfiguration), it contains all configuration values necessary for setting up EdgeConnect.
Save the example below in a file called `deployment.yaml` and replace the values surrounded by `< >` with the values in your `edgeConnect.yaml`.

```
apiVersion: v1



kind: Secret



metadata:



name: edge-connect-oauth



namespace: dynatrace



stringData:



oauth-client-id: <oauth.client_id from edgeConnect.yaml>



oauth-client-secret: <oauth.client_secret from edgeConnect.yaml>



---



apiVersion: v1



kind: Secret



metadata:



name: edge-connect-config



namespace: dynatrace



stringData:



edge-connect-config-file: |



certificate_paths:



- "/etc/edge_connect_certs/some_certificate.cer"



- "/etc/edge_connect_certs/another_certificate.pem"



secrets:



- name: My secret



token: <DYNATRACE_TOKEN_PLACEHOLDER>.some-token-secret



from_env: MY_SECRET



restrict_hosts_to:



- dynatrace.com



- name: My other secret



token: <DYNATRACE_TOKEN_PLACEHOLDER>.another-token-secret



from_file: /path/to/my/other/secret



restrict_hosts_to:



- internal.example.com



---



apiVersion: apps/v1



kind: Deployment



metadata:



name: example-edge-connect



namespace: dynatrace



spec:



replicas: 1



selector:



matchLabels:



app: edge-connect



template:



metadata:



labels:



app: edge-connect



spec:



containers:



- name: edge-connect



image: dynatrace/edgeconnect:latest



imagePullPolicy: IfNotPresent



env:



- name: EDGE_CONNECT_NAME



value: <name from edgeConnect.yaml>



- name: EDGE_CONNECT_API_ENDPOINT_HOST



value: <api_endpoint_host from edgeConnect.yaml>



- name: EDGE_CONNECT_OAUTH__ENDPOINT



value: <oauth.endpoint from edgeConnect.yaml>



- name: EDGE_CONNECT_OAUTH__RESOURCE



value: <oauth.resource from edgeConnect.yaml>



volumeMounts:



- name: secrets



mountPath: "/etc/edge_connect"



readOnly: true



- name: config



mountPath: "/edgeConnect.yaml"



subPath: "edgeConnect.yaml"



readOnly: true



volumes:



- name: secrets



secret:



secretName: edge-connect-oauth



items:



- key: oauth-client-id



path: oauth/client_id



- key: oauth-client-secret



path: oauth/client_secret



- name: config



secret:



secretName: edge-connect-config



items:



- key: edge-connect-config-file



path: edgeConnect.yaml
```

#### Configuring EdgeConnect in Kubernetes

There are three ways of configuring EdgeConnect in Kubernetes.
The example above uses all three of them for demonstration.

##### Environment variables

Environment variables can be used to configure most EdgeConnect settings.
Check the table in [Field descriptions](#edgeconnect-yaml-fields) for more information.

##### Mapped files

Files mounted into the folder `/etc/edge_connect` will be mapped to config values.
The file path in this folder represents the various `.yaml` fields, for example:

* `/etc/edge_connect/name` will be mapped to the `name` field in `edgeConnect.yaml`, which is equivalent to setting the `EDGE_CONNECT_NAME` environment variable.
* `/etc/edge_connect/oauth/client_id` will be mapped to `oauth.client_id` in `edgeConnect.yaml`, which is equivalent to setting the `EDGE_CONNECT_OAUTH__CLIENT_ID` environment variable.

All configuration values that can be set with environment variables, as documented in [Field descriptions](#edgeconnect-yaml-fields), can also be configured using mapped files.

##### Mounting edgeConnect.yaml

It is possible to mount `edgeConnect.yaml` in the EdgeConnect container directly.
Note that some settings can only be configured this way, for example `secrets` (see the [table above](#edgeconnect-yaml-secrets-fields)).

### Step 3 Apply the deployment

1. Go to the directory containing the `deployment.yaml` file you created.
2. Apply the deployment.

   ```
   kubectl apply -f ./deployment.yaml
   ```

### Step 4 Validate the connection

Validate EdgeConnect successfully connected to the platform.

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Check the **Availability** column. It should display **online**.

   * If it's still offline, check the container's logs for error messages.
   * If the app says that there are online EdgeConnect instances, congratulations! You have safely connected your environment to the Dynatrace platform.

     From now on, any HTTP request that occurs as part of an app function, ad hoc function, or workflow action matching a host pattern, will be transparently run by EdgeConnect instead of directly by the Dynatrace runtime.

## Using multiple EdgeConnect configurations and instances

You can create multiple EdgeConnect configurations in your environment, each with its own different host pattern configuration as explained in [Create a new EdgeConnect configuration](#createconfiguration). For each EdgeConnect configuration, you can [deploy](#deploy) multiple instances to split the EdgeConnect request load on multiple EdgeConnects for load balancing. In this case, matching requests will be distributed across EdgeConnect instances with free capacity.

### Host patterns

Note that a single host pattern can be used in only one EdgeConnect configuration, not shared across EdgeConnect configurations. For example, given an EdgeConnect configuration named `staging` that contains `staging.myapp.org` as a host pattern, you can't use the same host pattern in an EdgeConnect configuration named `myapp`.

However, you can use an overlapping host pattern `*.myapp.org` in `myapp`. In this case, the Dynatrace JavaScript runtime will choose the EdgeConnect configuration with the most specific host pattern for a matching request's URL, so a request to `https://staging.myapp.org/test.html` would always be redirected to EdgeConnect instances of configuration `staging`. Consequently, the EdgeConnect configuration chosen for a given URL is deterministic.

#### Test your configurations

To test in advance which EdgeConnect would handle a given URL based on the EdgeConnect configurations in your respective environment

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Select **URL verification**.

   * On the **Find matching EdgeConnects** tab, enter your URL and select **Match** to find EdgeConnects to handle your request.
   * On the **Test HTTP request** tab, enter an HTTP request and select **Run test** to run the request in the Dynatrace runtime and verify the connection to an EdgeConnect.

### Host mappings

The above uniqueness constraint of a host pattern per EdgeConnect configuration is problematic if you want to administer different EdgeConnect configurations, each meant to reach different internal services that share the same host names, such as services running on a generic host name like `localhost`.

Another common example is accessing the Kubernetes API via `kubernetes.default.svc.cluster.local` when EdgeConnect is deployed in a Kubernetes cluster and is meant to be used to manage that cluster via requests from the Dynatrace JavaScript runtime. You can have only one EdgeConnect configuration with the host pattern `kubernetes.default.svc.cluster.local`; you can't do this when you have multiple Kubernetes clusters that you want to manage via EdgeConnect.

The solution to this problem is to use *host mappings*, where you configure a mapping from a host specified in the host patterns (which is unique across configurations as mentioned above) and rewrite the host of matching requests to the needed generic host name before handing over the request to the EdgeConnect container.

#### Host mappings in the settings

To configure a host mapping

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Select the configuration you want to edit.
3. In the settings panel for the selected configuration, expand **Host mappings**.
4. Define one or more rules (**From** and **To**) for mapping requests matching one of the host patterns to another host. Any request where the host matches one of the hosts in **From** will be rewritten to the host in **To**.

##### Example 1

In this example, EdgeConnect configuration `service-a` defines the host pattern `localhost-service-a` and configures as a host mapping a mapping of `localhost-service-a` to `localhost`.

A request to `http://localhost-service-a/myservice` in the Dynatrace JavaScript runtime will be redirected to that EdgeConnect configuration `service-a`. However, the host of the request would be rewritten so that a connected EdgeConnect instance will actually make the request to `http://localhost/myservice`. Another EdgeConnect configuration `service-b` could accordingly configure host pattern `localhost-service-b` and a host mapping of `localhost-service-b` to `localhost` in order to access `http://localhost/otherservice` via a request in the Dynatrace JavaScript runtime targeting `http://localhost-service-b/otherservice`.

##### Example 2

In this example, EdgeConnect configuration `k8-api-dev` defines the host pattern `kubernetes-api-dev-cluster` and configures a host mapping of `kubernetes-api-dev-cluster` to `kubernetes.default.svc.cluster.local`.

A request to `https://kubernetes-api-dev-cluster/api/v1/pods` in the Dynatrace JavaScript runtime will be redirected to the EdgeConnect instances running the configuration of EdgeConnect configuration `k8-api-dev`. However, the host of the request would be rewritten so that a connected EdgeConnect instance will actually make the request to `https://kubernetes.default.svc.cluster.local/api/v1/pods`.

You'd deploy EdgeConnect containers for that configuration in your `dev` Kubernetes cluster and would reliably be able to manage that cluster via HTTPS requests from the Dynatrace runtime. At the same time, you also have a production Kubernetes cluster that you want to manage accordingly. So you create another EdgeConnect configuration `k8-api-production` configuring the host pattern `kubernetes-api-production-cluster` and a host mapping of `kubernetes-api-production-cluster` to `kubernetes.default.svc.cluster.local`, and deploy instances of it in the production Kubernetes cluster. As a result, you can target the Kubernetes API of the desired cluster reliably by making a request to either `https://kubernetes-api-dev-cluster/api/v1/pods` or `https://kubernetes-api-production-cluster/api/v1/pods`.

For details on this example, see [Set up manually EdgeConnect for Kubernetes Connector](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/kubernetes-automation/edge-connect-kubernetes-automation-manual-setup "Set up manually EdgeConnect for Kubernetes Connector to be able to use our wide range of Kubernetes Connector actions in your workflow.").

## System Requirements

For a typical EdgeConnect deployment, we recommend 1 GB of memory and 1 CPU. Memory requirements might vary depending on the payload size of the handled requests.
EdgeConnect requires the following network connectivity.

* HTTPS(443) to `https://sso.dynatrace.com/sso/oauth2/token`
* HTTPS(443) and WSS-Secure websocket(443) `https://<your environment ID>.apps.dynatrace.com`
  as well as to any target system EdgeConnect requests shall connect to.

## Security

Security-related configuration requirements and recommendations for EdgeConnect are based on the "least privilege" principle.

### What EdgeConnect does

* EdgeConnect establishes a WebSocket secure connection (WSS/443) to AppEngine and thus doesn't require any inbound connection. To achieve this, EdgeConnect must be able to create an outbound WSS/443 connection to your Dynatrace environment.
* EdgeConnect works in the environment context and transparently performs any HTTP(S) requests in AppEngine matching the defined host patterns. Anyone with the respective permissions to trigger an app function, ad hoc JavaScript, or workflow in an environment can issue HTTP(S) requests to the matching hosts.

### What you should do

* Restrict EdgeConnect deployments to the network required to reach the intended systems only.
* Define the EdgeConnect host pattern configuration as specifically as possible so only the required HTTP(S) requests are forwarded.
* Use the EdgeConnect local configuration to restrict the allowed hosts to reach ([see the optional `restrict_hosts_to` property](#config) in the table above). Defined host patterns can never exceed the local host restriction. A local host restriction alone doesn't result in any HTTP(S) request forwarding.

## Limits

To make sure EdgeConnect performs well, the EdgeConnect requests and responses are subject to the following limits:

### Request timeout

There is a timeout of 120 seconds for every request that runs over EdgeConnect. Note that this matches the maximum execution time of functions. If a function times out, all outgoing requests will be cancelled automatically.

### Payload size limit

The body of a request or response run over EdgeConnect may not exceed 6MB. If this limit is exceeded, the respective request will fail with the HTTP error code 400.

### Concurrent requests limit

There is a limit of 20 concurrent requests that a single EdgeConnect container can process at the same time. Subsequent requests are likely to run into the request timeout. As a workaround, deploy multiple EdgeConnect containers.


---
