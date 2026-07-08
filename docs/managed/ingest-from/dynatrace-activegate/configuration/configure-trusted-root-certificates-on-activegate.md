---
title: Trusted root certificates for ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate
---

# Trusted root certificates for ActiveGate

# Trusted root certificates for ActiveGate

* 7-min read
* Updated on Feb 24, 2026

There can be situations where it is necessary to add additional certificates to the certificate store shipped with ActiveGate. Follow the procedure described below to add an additional certificate to an existing ActiveGate.

### Alternatively, add certificates during ActiveGate installation Optional

If you prefer, additional trusted root certificates can also be specified during ActiveGate installation, by specifying installation parameters for [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#ca-certificate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#ca-certificate "Learn about the parameters that you can use with ActiveGate on Windows.").

## Determine if you need to add a CA certificate to ActiveGate

ActiveGate connects to other Dynatrace components (clusters, servers) or third-party systems (such as VMware, Cloud Foundry, Kubernetes or OpenShift) using SSL-secured channels. The root CA certificate store shipped with ActiveGate (the default certificate set shipped with Java) is sometimes insufficient to cover all the required use cases.

For example:

* A certificate has been issued by a Certifying Authority inside your own organization for a proxy, which takes SSL traffic
* Some servers in your organization use self-signed certificates

If such situations occur, an error in the ActiveGate log file will state that a certificate presented by a server to which your ActiveGate was trying to connect was not trusted. In these cases, you need to import the missing certificate to the ActiveGate.

Adding a certificate is a potential security concern. Consult your organization's security compliance team before adding a new trusted root certificate to ActiveGate to be sure that your organization's security will not be compromised by your actions. If an error is reported in the ActiveGate log stating that a certificate presented by a server, to which your ActiveGate was trying to connect, was not trusted, **do not** assume that you need to add a missing certificate. Further research is required before proceeding.  
**An invalid certificate error can also mean that there has been an attempt to breach the security of your organization. You should, therefore always investigate this possibility, when such an error is reported.**

## Configure trusted root certificates

### Determine the required CA certificates and prepare them as a file

If you want to configure truststore certificates for extensions, see [Oracle Database monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring#ssl "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.").  
To upload the certificate for custom Extensions verification, see [Upload your root certificate](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions#upload "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

Before you add a certificate to the ActiveGate, you need to obtain it and place it in the `ca.crt` file.
Obtaining the CA certificate is highly context-specific and there are no simple steps to follow. Consult appropriate sources in your organization to obtain the required certificates.

For details, see the [General information about CA certificates](#general-ca-certs-info) section below.

### Configure trust store

agctl

custom.properties

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#trust-store "Learn how to use agctl to configure and manage ActiveGate from the command line") to configure trusted root certificates.

#### Set trust store with minimum parameters:

```
agctl trust-store set --certificates=/path/to/ca.crt
```

#### Set trust store with custom filename and password:

```
agctl trust-store set --certificates=/path/to/ca.crt --truststore=custom-truststore.p12 --password=mypassword
```

#### Parameters:

* `--certificates`: Path to the certificate file(s) in PEM format (required)
* `--truststore`: File name for the truststore in the ActiveGate SSL directory (optional, default: `mytruststore.p12`)
* `--password`: Password for the truststore (optional, default: `changeit`)

After configuring the trust store with `agctl`, you must [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

Note that manual configuration requires creating a PKCS#12 truststore file using `keytool`.

1. **Create a truststore from the CA certificate file**

   Create an additional truststore containing just your CA certificates. At run-time, it will be merged by ActiveGate with the built-in JDK truststore.
   The truststore should be in the **PKCS#12 format**. The OpenSSL formats are not supported, so use the `keytool` command to perform the conversion.
   After the conversion , placethe certificate in the [ActiveGate SSL directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

   If you import multiple certificates, make sure that you provide a unique alias for each certificate that you import. If you use the same alias for each certificate, all previously used certificates will be overwritten.

   The following are Linux examples of creating a PKCS12 file from a CRT file or a PEM file, and placing it either directly in the [ActiveGate SSL directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), or in the current directory, to be copied later:

   ```
   /opt/dynatrace/gateway/jre/bin/keytool -import -file ca.crt -alias dt_k8s_api -storetype pkcs12 -keystore /var/lib/dynatrace/gateway/ssl/mytrusted.p12
   ```

   or

   ```
   /opt/dynatrace/gateway/jre/bin/keytool -import -file dt_k8s_api.pem -alias myCertAuthority -storetype pkcs12 -keystore mytrusted.p12
   ```

   Check permissions

   For Linux, check that the ActiveGate user (`dtuserag` by default) has the following permissions:

   * Write permission for the [ActiveGate SSL directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") (`/var/lib/dynatrace/gateway/ssl` by default)
   * Read permission for the created truststore
2. **Configure ActiveGate to use the custom truststore file**

   To configure ActiveGate to use the custom truststore file `mytrusted.p12`, make sure that the truststore file is in the [ActiveGate SSL directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), and then add the following entries to the `custom.properties` file in the [ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."):

   ```
   [collector]



   trustedstore = mytrusted.p12



   # the following entries are optional



   trustedstore-password = changeit



   trustedstore-type = PKCS12
   ```

   You can display the configured list of aliases and the certificate descriptions using the `keytool -list` command on the new truststore.  
   For example:

   ```
   # /opt/dynatrace/gateway/jre/bin/keytool -list -keystore /var/lib/dynatrace/gateway/ssl/mytrusted.p12



   Enter keystore password:



   Keystore type: PKCS12



   Keystore provider: SUN



   Your keystore contains 1 entry



   dt_k8s_api, Apr 26, 2020,



   trustedCertEntry,



   Certificate fingerprint (SHA-256): 08:18:9A:F2:29:31:0D:64:F0:1F:93:A1:CC:2E:A9:21:E9:DA:40:82:9B:A8:71:B7:A4:2C:6D:8C:B3:90:31:31
   ```

   Encrypted password

   The password will be stripped and encrypted when you restart the ActiveGate service.
3. **Restart ActiveGate service and verify certificate configuration**

   [Restart ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to make the changes take effect.  
   If everything has been configured correctly, the ActiveGate log should contain an entry saying:

   ```
   Custom certificate configuration created successfully.
   ```

## Configuration

**Section: [collector]**

| Property | Default value | Description |
| --- | --- | --- |
| `trustedstore` | unset | Your trusted keystore (optional). The property `trustedstore` should contain the path to the file holding trusted certificates. That path should be relative to the ActiveGate SSL directory. Please also see [Trusted root certificates for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to configure custom trusted root certificates on ActiveGate to establish secure SSL/TLS connections."). |
| `trustedstore-exclusive` | unset | When set to `true`, ActiveGate will no longer merge the built-in trust store (shipped with JRE) with the custom trust store defined by you in `trustedstore`. The custom trust store will be the only trust store used for communication. |
| `trustedstore-password` | `changeit` | Password of your trusted keystore (optional) which is encrypted during ActiveGate start. The obfuscated password is then stored in `trustedstore-password-encr`. |
| `trustedstore-type` | `pkcs12` | Java default format of key and certificate databases (optional). |

## Limitations

ActiveGate logs its actions related to the above configuration. The configured truststore will not be used (and the truststore configuration will be left unchanged) if any of the following is true:

* The `javax.net.ssl.trustStore` system property is specified.  
  If this property is specified, it takes precedence over the ActiveGate configuration.
* The configured truststore can't be read using the configured path, password, and type.
* The merged configuration can't be written to the `ssl/runtime.cacerts` file.

## General information about CA certificates

**The following general information about CA certificates may help you to determine the required certificates:**

To create a trusted SSL connection for your certificate authority, the following conditions must be met:

* Between the certificates presented by the server (API endpoint) and the certificates present in the ActiveGate truststore, a full certificate chain must be created.
* The root certificate of the chain must be included in the ActiveGate truststore, along with any other certificates NOT presented by the server/API endpoint.

To see which certificates the endpoint is presenting you can use the following command:

```
openssl s_client -connect <API_ENDPOINT>:<PORT> -showcerts -servername <API_ENDPOINT_HOSTNAME>
```

Some applications (for example OpenShift) can present different certificates depending on the SNI. ActiveGates will set the configured endpoint hostname in the SNI.

If the above command presents a full certificate chain then you must add the root certificate to the ActiveGate truststore. You can add the intermediates as well, but they are not necessary if the API endpoint presents them.

If the above command does not present a full certificate chain, then the root of the chain must be obtained elsewhere.

For example, the endpoint of the `openssl` request to this server—see below—only returns the server certificate, and not the root certificate.
You know that this server only presents a server certificate and not a root certificate because the error says `unable to get local issuer certificate`. If the root certificate were present, the error message would say "Self-signed certificate in certificate chain".
To create a valid SSL connection to this endpoint, you must obtain the root certificate separately.

```
openssl s_client -connect localhost:6443



CONNECTED(00000005)



depth=0 CN = kube-apiserver



verify error:num=20:unable to get local issuer certificate



verify return:1



depth=0 CN = kube-apiserver



verify error:num=21:unable to verify the first certificate



verify return:1



---



Certificate chain



0 s:CN = apiserver



i:CN = DynatraceRootAuth



---



Server certificate



-----BEGIN CERTIFICATE-----



MDIDYGCCAkigAwIBAgJIJ8SQ/FcmJiYwDQZJKoZIhvcNAQESBQAwFTETMBEGA1UE



AxMKa3ViZXJuZXRlczAeFw0yMTAxMjcxOTM1MDhaFw0yMjAxMjcxOTM1MDhaMBkx



FzAVBgNVBAMTDmt1YmUtYXBpc2VydmVyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A



MIIBCgKSAQEA15BVGULXSXZAM6a4Y7lR6JfSBOXIAq1sCoydH2AdhzqHu0mXj+Fd



sooRQ46f7bySZvMGFfLupmaAzH5kVJOVDQ2WoHPYVzAEhDji+SUBOi99AC0tevEa



ONLdkLGzR//2u8XND0iiswsGkK3yaNyPwCVnOnA3c4O32waMoM1VI9XGuNSqqfQF



6XUx8sGHG5bNVzfHOXh5CBJZ5JReDhW/J8CbPElYJPJaQcSpTVFx5ReTQqBLeBSy



eWyCwqMj/jAnKzpPffO478If/Uc8I5vS8zi2yPhYJhKqD0m1b96hH0slXKho25Ip



gpu4cIw03mQZMK558W4d6ccww/OvMbpKQQIDAQABo4GvMIGsMA4GA1UdDwEB/wQE



AwIFoDATBgNVHSUEDDAKBgfrBgEFBQcDATSBhAYDVR0RBH0we4IPamstazhzLWNs



b25lLTAwggprdWJlcm5ldGVzghJrdWJlcm5ldGVzLmRlZmF1bHSCFmt1YmVybmV0



ZXMuZGVmYXVsdC5zdmOCAGt1YmVybmV0ZXMuZGVmYXVsdC5zdmMuY2x1c3Rlci5s



b2NhbIcECmAAAYcErBcSvDANBgkqhkiG9w0BAQsFAAOCAQEAdmOq/Sp74xiLCa14



EI/9v7jUG+GqjD3HPpj/oXIdLHg6HA4nixxcxwnWAf2RAMVXBYn7qTDU6x7W5M+t



6M0uaCe8Od8oKjOKeQ31dfMpPbLYprKmcnuBriiN5gjfghINZKaZlGlX0GkBC9Ts



THYbmWfXfvfsX2xfpc4J0esfK+BafllEimCx8blnw1uY7CiCedEANePT+J5Q+m9L



m5pu7Qz/B4JDHLIJBArhFTBM6IIF6DhoqGUXM1XXqMlTVBpxz2vhf0N/HxcTaEBa



VWu7GZbk5mCYhngmRJ8PJ3uA8yajDT2muWm/la5oOI/GeuTgR98tqjXOXmz2NjvE



Zng1CA==



-----END CERTIFICATE-----



subject=CN = kube-apiserver



issuer=CN = kubernetes



---



Acceptable client certificate CA names



CN = kubernetes
```

The certificate below is an example root certificate for the above server certificate. Make sure that you only add root certificates that you trust, to your truststores.  
For example:

```
cat ca.crt | openssl x509 -text -noout



Certificate:



Data:



Version: 3 (0x2)



Serial Number: 0 (0x0)



Signature Algorithm: sha256WithRSAEncryption



Issuer: CN = kubernetes



Validity



Not Before: Jan 27 19:35:08 2021 GMT



Not After : Jan 25 19:35:08 2031 GMT



Subject: CN = kubernetes



Subject Public Key Info:
```

You can see that this is the root certificate you need because the subject and issuer are identical, and they match the issuer of the server certificate shown above ('kube-apiserver ').