---
title: Sign extensions manually with OpenSSL
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl
scraped: 2026-05-12T12:11:37.267488
---

# Sign extensions manually with OpenSSL

# Sign extensions manually with OpenSSL

* How-to guide
* 4-min read
* Published Apr 21, 2021

## Use OpenSSL

To sign your extension manually, use OpenSSL. For Windows, you need to download and install an [OpenSSL binaryï»¿](https://wiki.openssl.org/index.php/Binaries) of your choice. We tested the procedure with OpenSSL 1.1.1k.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create the root key and certificate**](#create-root-key-and-cert)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add your root certificate to the Dynatrace credential vault**](#add-root-cert)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Create a developer certificate**](#create-dev-cert)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Sign your extension**](#sign-extension)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Verify signature**](#verify-signature)[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Create extension package**](#create-extension-package)

### Create the root key and certificate

Your company should issue developer certificates from a company-wide root certificate. When developers sign their extensions with their own developer certificates, Dynatrace will be able to verify the extension authenticity against your root certificate stored in the Dynatrace credential vault and on the hosts where extensions are executed.

Run the following commands to generate your organization's root certificate. Do not set the password. Password-protected certificates are not supported by Dynatrace.

```
openssl genrsa -out root.key 2048



openssl req -new -key root.key -out root.csr
```

When generating the root certificate, you need to explicitly define the certificate extension by pointing the `-extfile` property to the `ca.txt` file. The file should contain the following data:

```
basicConstraints=critical, CA:true, pathlen:0



subjectKeyIdentifier    = hash



authorityKeyIdentifier  = keyid:always



keyUsage                = keyCertSign
```

```
openssl x509 -req -days 10000 -in root.csr -signkey root.key -out root.pem -extfile ca.txt
```

This generates your `root.pem` root certificate.

Note that you can also use an existing root certificate to generate developer certificates. Dynatrace accepts only PFX, P12, and PEM formats, so you may need to convert the existing certificate to one of the allowed formats. Refer to the OpenSSL documentation for conversion instructions.

### Add your root certificate to the Dynatrace credential vault

1. Go to **Credential Vault**.
2. Select **Add new credential**.
3. For **Credential type**, select **Public Certificate**.
4. Select the **Extension validation** credential scope.
5. Add a meaningful **Credential name**.
6. Upload the **Root certificate file**.
7. Select **Save**.

### Create a developer certificate

To create your developer certificate, you need to create a developer certificate signing request and then issue the certificate.

#### Create a developer certificate signing request

Run the following commands to generate the certificate signing request (CSR) to the root CA:

```
openssl genrsa -out developer.key 2048
```

```
openssl req -new -key developer.key -out developer.csr
```

When filling in the fields for the Distinguished Name (DN), make sure that at least one of the fields is different than the DN you defined for the root certificate.

The result is the `developer.csr` CSR that you'll use to issue the developer certificate from the root certificate.

#### Issue a developer certificate

Run the following commands to generate the developer certificate:

```
openssl req -new -key developer.key -out developer.csr
```

When generating the developer certificate, you need to explicitly define the certificate extension by pointing the `-extfile` property to the `developer.txt` file. The file should contain the following data:

```
subjectKeyIdentifier    = hash



authorityKeyIdentifier  = keyid:always



keyUsage                = digitalSignature
```

```
openssl x509 -req -days 10000 -in developer.csr -CA root.pem -CAkey root.key -CAcreateserial -out developer.pem -extfile developer.txt
```

The result is the `developer.pem` certificate file that you'll use for signing your extensions.

### Sign your extension

With the developer certificate in place, use the following command to sign your extension. Make sure that your `extension.zip` file is in the directory from which you run the command.

```
openssl cms -sign -signer developer.pem -inkey developer.key -binary -in extension.zip -outform PEM -out extension.zip.sig
```

The result is an `extension.zip.sig` signature file.

### Verify signature

Use the following command to verify the `extension.zip.sig` signature file against the `root.pem` root certificate:

Linux

Windows

```
openssl cms -verify -CAfile root.pem -in extension.zip.sig -binary -content extension.zip -inform PEM -out /dev/null
```

```
openssl cms -verify -CAfile root.pem -in extension.zip.sig -binary -content extension.zip -inform PEM -out NUL
```

The output should contain the phrase `Verification successful`.

### Create extension package

For the final step, create an [extension package](/managed/ingest-from/extensions/concepts#package "Learn more about the concept of Dynatrace Extensions.") containing only the `extension.zip` archive and the `extension.zip.sig` signature file.

```
bundle.zip



|    extension.zip



|    extension.zip.sig
```

You can now upload the extension package to your Dynatrace environment. For more information, see [Manage Extensions](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").