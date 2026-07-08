---
title: Custom SSL certificate for ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate
---

# Custom SSL certificate for ActiveGate

# Custom SSL certificate for ActiveGate

* 6-min read
* Updated on Feb 24, 2026

Not applicable to Cluster ActiveGate

The following procedure—of directly uploading an SSL certificate to an ActiveGate—is not applicable for Cluster ActiveGates.
Do not attempt to configure SSL certificates directly on a Cluster ActiveGate. If you do this, the certificate will be overwritten by automatic management performed by Dynatrace.
For Cluster ActiveGates, you must upload your certificates using [the Cluster Management Console](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.") or [the Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate.").

Connection to ActiveGate, from OneAgents or REST API, takes place over an encrypted HTTPS channel. ActiveGate presents a self-signed authentication certificate to all connecting clients. While OneAgent instances may ignore the validity of ActiveGate certificates (depending on configuration), connections from browser clients (such as the [RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications")) do verify that the hostname listed in the certificate is correct, before they send data.

ActiveGate can serve a custom certificate instead of the default one.

* Depending on the root CA that signed the custom ActiveGate certificate, additional configuration for OneAgent may be required. See [OneAgent security](/managed/ingest-from/dynatrace-oneagent/oneagent-security#trusted-root-certificates "Manage OneAgent security").
* Custom certificate configuration can also be applied during ActiveGate installation, by specifying installation parameters for [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#custom-ssl-certificate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#custom-ssl-certificate "Learn about the parameters that you can use with ActiveGate on Windows.") installations. To configure this, you need a file in PKCS#12 format that contains a private key and its corresponding certificate chain.

## Configure a custom SSL certificate

agctl

custom.properties

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#ssl-certificate "Learn how to use agctl to configure and manage ActiveGate from the command line") to configure a custom SSL certificate.

#### Set SSL certificate with minimum parameters:

```
agctl ssl-certificate set --certificate=/path/to/cert.crt --key=/path/to/key.pem
```

#### Set SSL certificate with all parameters:

```
agctl ssl-certificate set --certificate=/path/to/cert.crt --key=/path/to/key.pem --pem-password=secret --password=changeit --alias=mycert
```

#### Parameters:

* `--certificate`: Path to the certificate file in PEM format (required)
* `--key`: Path to the private key file in PEM format (required)
* `--pem-password`: Password for the private key file (if encrypted)
* `--password`: Password for the generated keystore (optional, auto-generated if not provided)
* `--alias`: Alias for the certificate in the keystore (optional)

After configuring the SSL certificate with `agctl`, you must [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

To configure ActiveGate to use a custom certificate, you need a file in **PKCS#12 format** that contains a private key and its corresponding certificate chain.

1. Copy the certificate file to the [ssl directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") and set correct permissions.

   On Linux, make sure that permissions of the copied certificate file include the ActiveGate user you designated to run the ActiveGate service. If you didn't specify a custom user during installation, the default user is `dtuserag`.

   On Windows, make sure that the `LocalService` account has permissions to access the copied certificate file.
2. Add the following entries to the `custom.properties` file in the [ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

   ```
   [com.compuware.apm.webserver]



   certificate-file = certificate-file.p12



   certificate-password = password



   certificate-alias = friendly-name
   ```

   You need to add the above entries in the `[com.compuware.apm.webserver]` section. If there already is such a section in your `custom.properties` file, then just add the properties to the section. If the section doesn't exist, then create the section heading as well.

   The certificate password, which you provide in the `certificate-password` property, will be obfuscated, following the [restart of ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux."). The obfuscated password is stored in the `certificate-password-encr` property, while the original property is deleted.

   **The value of `certificate-alias` must be specified in lower case.** If the certificate doesn't have a friendly name, you can omit the `certificate-alias` property.

## Managing certificates via REST API

The certificates can be managed remotely via REST API. Prepare a `PKCS#12` certificate file and you can upload it to ActiveGate using REST.

Authorization token

The API token is required for authorization. API tokens can be provided via HTTP headers or other means. See [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

API token used for the following actions must have `ActiveGate certificate management` permission.

#### Upload and activate certificate

The following REST point uploads and activates the selected certificate file. The password for the file must be the same as the password for the keys contained in the file, and they must be provided in an `X-Password` custom HTTP header.

`curl https://{address of ActiveGate}:{port}/e/{environment ID}/api/v1/certificate/{certificate file name} -H"Authorization: Api-Token {token}" -H"X-Password: {password}" -H"Content-Type: application/octet-stream" -T {path to certificate file}`

* The port is configurable, 9999 by default.
* The path to the certificate file can be just the name of a local file, or it can be a full path.
* The name of the certificate, as given in the URL, does not have to match the name of the file.

For example:

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12 \



-H "Authorization: Api-Token 123abc" \



-H "X-Password: myPassword" \



-H "Content-Type: application/octet-stream" \



-T cert.p12
```

If the API call is successful, the HTTP response will be `200` with JSON-formatted description of the content of the activated certificate file.

If the API call fails, the HTTP response will be a `4xx` or `5xx` error code, with a plain text message.

#### Replace active certificate

You can't replace an active certificate using this endpoint. The operation will return `HTTP 403 Forbidden`. To replace an active certificate, upload a new certificate under a different name, then delete the old certificate.

#### Delete certificate

Deletes the selected certificate on ActiveGate.

```
curl -XDELETE https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12 -H"Authorization: Api-Token 123abc"
```

If the certificate is deleted successfully, the API call will respond with HTTP `200` code with no content.

If the file with the specified name does not exist, the API call will respond with HTTP `404 Not found` code.

If the certificate file is currently in use, the API call will respond with HTTP `403 Forbidden` code.

#### Activate certificate

Activates an existing previously-uploaded certificate file using the specified password.

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/activate -H"Authorization: Api-Token 123abc" -d"{\"password\":\"pass\"}"
```

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/activate -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

If the certificate is successfully activated, the API call will respond with HTTP `200` code, with JSON-formatted description of the content of the activated certificate file.

If the requested certificate file does not exist on the ActiveGate, the API call will respond with HTTP `404` code.

If the provided password does not match, the API call responds with HTTP `400` code.

#### List all certificates

Returns a JSON-formatted list of all uploaded files.

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/list -H"Authorization: Api-Token 123abc"
```

If the active keystore is on the list, its entry will contain additional details.

Example response:

```
[



{



"name":"cert_demo.p12"



},



{      "name":"cert.p12",



"desc":[         {



"alias":"local",



"description":"Subject:CN=myActiveGate;Valid from:Fri Feb 15 13:16:58 CET 2019;Valid to:Sat Feb 15 13:16:58 CET 2020;Serial number:71d275dd3983c3cb9382437275dd3983c3cb93dbca"



},



{



"alias":"dynatrace",



"description":"Subject:CN=*.clients.dynatrace.org;Valid from:Thu Feb 21 10:06:03 CET 2019;Valid to:Fri Feb 21 10:06:03 CET 2020;Serial number:6dc7008ab269ecebeed03652ce08ab269ecebeeeb33"



}



]



},



{



"name":"cert_key_1.p12"



}



]
```

Note that the default self-signed certificate is not included in the list.

#### Describe certificate

This API call returns a JSON-formatted description of the selected file.

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -d"{\"password\":\"pass\"}"
```

If the requested certificate file does not exist on the ActiveGate, the API call will respond with HTTP `404` code.

If the password doesn't match, the API call responds with HTTP `400` code.

Example response:

```
{   "name":"cert.p12",



"desc":[      {



"alias":"local",



"description":"Subject:CN=myActiveGate;Valid from:Fri Feb 15 13:16:58 CET 2019;Valid to:Sat Feb 15 13:16:58 CET 2020;Serial number:7137275dd398c4182437275dd3983c3cb93dbca"



},



{



"alias":"dynatrace",



"description":"Subject:CN=*.clients.dynatrace.org;Valid from:Thu Feb 21 10:06:03 CET 2019;Valid to:Fri Feb 21 10:06:03 CET 2020;Serial number:6d2ce08ab269ecebeee7f1bd03652ce08ab269ecebeeeb33"



}



]



}
```

## Create a certificate file for testing

To create a self-signed `PKCS#12` certificate file for testing

1. Generate a key and a self-signed certificate:

   ```
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj "/CN=localhost"
   ```
2. Convert the generated files to `PKCS#12` format:

   ```
   openssl pkcs12 -export -inkey key.pem -in cert.pem -out cert_key.p12
   ```

   or, to set a friendly name, use:

   ```
   openssl pkcs12 -export -inkey key.pem -in cert.pem -out cert_key.p12 -name friendly-name
   ```

   remembering that the `friendly-name` must be given in lower case.

## Known limitations and support for multiple certificates

* The password for the `PKCS#12` file must be the same as the password for the key contained in this file.  
  Don't use the `-twopass` option in the `openssl pkcs12` command.
* It's not possible to use multiple certificate files: There can be only one ActiveGate certificate file, though the file can contain multiple certificates and keys.