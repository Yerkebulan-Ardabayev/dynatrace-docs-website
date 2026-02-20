---
title: Network configurations
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations
scraped: 2026-02-20T21:16:51.786782
---

# Network configurations

# Network configurations

* Latest Dynatrace
* 4-min read
* Published Mar 25, 2024

Configure Dynatrace in network-restricted environments with network configurations, proxy settings, and URL exclusions.

Network zones

For details on setting up and managing network zones, initial endpoint setup, and advanced configurations in restricted environments, see [Using network zones in Kubernetes](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones "Set up and use network zones in Kubernetes environments with the Dynatrace Operator.").

## Configure proxy

For Kubernetes Platform Monitoring with Dynatrace, you might need to configure a proxy, which facilitates all outgoing connections for Dynatrace Operator components (such as `csi-driver` and `operator`), OneAgent, and ActiveGate.

Depending on your proxy configuration, especially regarding credentials, there are two options for configuring your proxy in a DynaKube:

Without proxy credentials

With proxy credentials

HTTPS proxies are supported for ActiveGate since version 1.289.  
HTTPS proxies are supported for OneAgent since version 1.311.

For proxies without credential requirements, provide your proxy URL in the `value` field:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



proxy:



value: http://<my-super-proxy>
```

For proxies requiring credentials.

1. Create a Kubernetes secret containing your encrypted proxy URL, including the credentials.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   ```
   oc -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   Rules for the proxy password

   Ensure the proxy password meets the following criteria:

   | Requirements | Corresponding characters |
   | --- | --- |
   | Characters allowed | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
   | Characters not allowed | blank space ' ` , & = + % \ |

   The password in the custom resource or proxy secret must be URL-encoded. For example, `password!"#$()*-./:;<>?@[]^_{|}~` becomes `password!%22%23%24()*-.%2F%3A%3B%3C%3E%3F%40%5B%5D%5E_%7B%7C%7D~`.
2. Provide the name of the secret in the `valueFrom` section.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



   proxy:



   valueFrom: my-proxy-secret
   ```

Dynatrace Operator version 1.0.0+

The connection between OneAgent and Dynatrace code modules with ActiveGate will always bypass the proxy, ensuring direct communication for these components.

If you need to bypass the proxy for other reasons, see the next section.

### Exclude selected URLs from proxy configuration

To set the list of URLs to exclude from the proxy configuration, add the following annotation to the DynaKube custom resource.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/no-proxy: "some.url.com,other.url.com"
```

Dynatrace Operator then excludes the listed URLs from the proxy settings. This exclusion applies specifically to Dynatrace Operator and the CSI driver. It doesn't affect the proxy settings for other components managed by Dynatrace Operator, such as OneAgent or ActiveGate.

## Add trusted CA certificates

### ActiveGate, OneAgent and Dynatrace Operator components

To add trusted CA certificates to ActiveGate, OneAgent and/or Dynatrace Operator, the certificates must be provided via a Kubernetes ConfigMap referenced in your DynaKube configuration.

1. Create a ConfigMap (replace `<ca-certificates>` with the CA certificates to be trusted).

   ```
   apiVersion: v1



   kind: ConfigMap



   metadata:



   name: mycaconfigmap



   namespace: dynatrace



   data:



   certs: |



   <ca-certificates>
   ```

   For example:

   ```
   data:



   certs: |



   -----BEGIN CERTIFICATE-----



   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



   -----END CERTIFICATE-----
   ```
2. Apply the ConfigMap to your cluster.

   ```
   kubectl apply -f my-ca-configmap.yaml
   ```
3. In your DynaKube, reference the ConfigMap in the `trustedCAs` field.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



   trustedCAs: mycaconfigmap
   ```
4. Apply the DynaKube configuration to your cluster.

   ```
   kubectl apply -f dynakube-config.yaml
   ```

### Use `skipCertCheck` to bypass certificate verification

To ignore certificate verification for Dynatrace Operator components (`operator` and `csi-driver`), set `skipCertCheck` in your DynaKube configuration. This setting should only be used if the custom certificate authority is unknown or can't be provided to Dynatrace Operator via the `trustedCAs` field.

In Dynatrace Operator version 1.0.0 and earlier, the `skipCertCheck` setting was not applied during the image pulling process.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



skipCertCheck: true
```

## Configure a server TLS certificate for ActiveGate

By default, ActiveGate uses a self-signed certificate, which can be replaced by a self-managed certificate as described in [Custom SSL certificate for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

To configure a server TLS certificate for the ActiveGate:

1. Create the [Kubernetes Opaque secretï»¿](https://dt-url.net/zm03qza) holding the ActiveGate certificate(s) and ActiveGate private key.

   ```
   kubectl -n dynatrace create secret generic mytlssecret --from-file=server.p12=<myag.p12> --from-file=server.crt=<myag.crt> --from-literal=password=<mypassword>
   ```

   Where:

   * `server.crt`âDynatrace Operator propagates ActiveGate certificate(s) from the file to OneAgents.
   * `server.p12`âActiveGate certificate(s) and ActiveGate private key, ActiveGate reads the file and configures itself to use the provided private key and certificates.
   * `password`âActiveGate reads it and uses it to decrypt the `server.p12` file.

   `server.12` and `server.crt` files should contain the same certificate(s).
2. Provide the name of the secret via the `tlsSecretName` field.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   ...



   activeGate:



   tlsSecretName: <mytlssecret>



   ...
   ```