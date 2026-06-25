---
title: Configure SSL certificate for Managed Cluster
source: https://docs.dynatrace.com/managed/managed-cluster/installation/ssl-certificate-managed-cluster
scraped: 2026-05-12T11:25:06.214839
---

# Configure SSL certificate for Managed Cluster

# Configure SSL certificate for Managed Cluster

* How-to guide
* 3-min read
* Updated on May 08, 2026

By default, Dynatrace manages SSL for youâeach Managed Cluster receives a dedicated subdomain of `dynatrace-managed.com` with a trusted SSL certificate. To use your own certificate instead, follow the steps below.

As of **April 17, 2025**, Chinese regulations require an ICP (Internet Content Provider) certification for all publicly accessible services using the `dynatrace-managed.com` domain. Since Dynatrace doesn't hold an ICP certificate due to the lack of a legal entity in China, the affected domains have been blocked by local network providers.

To maintain monitoring capabilities, Dynatrace recommends the following:

* Use internal DNS or IP addresses for Cluster ActiveGate endpoints.
* Avoid exposing the Dynatrace UI or endpoints to public Chinese networks.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review requirements**](/managed/managed-cluster/installation/ssl-certificate-managed-cluster#review-requirements "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Disable automatic certificate management**](/managed/managed-cluster/installation/ssl-certificate-managed-cluster#disable-automanagement "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Upload your certificate**](/managed/managed-cluster/installation/ssl-certificate-managed-cluster#upload-certificate "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")

## Step 1 Review requirements

You need the SSL certificate and key files you received from your certificate authority (CA):

* Server certificate (`.cer` or `.cert`)
* Root and intermediate certificates (`.cer` or `.cert`)
* Private key (`.pem`)

Encrypted private keys

Encrypted private keys aren't supported. To decrypt an SSL private key, run:

`openssl rsa -in encrypted.ssl.key -out decrypted.ssl.key`

* `encrypted.ssl.key`: your encrypted SSL private key file.
* `decrypted.ssl.key`: the output file for the decrypted key.

The command prompts you for the password and saves the decrypted key.

## Step 2 Disable automatic certificate management

To disable automatic certificate management:

1. Log in to the **Cluster Management Console**.
2. Go to **Settings > Preferences** and disable **Manage domain name and SSL certificates**.

Without automatic certificate management, Dynatrace falls back to a self-signed certificate. Self-signed certificates aren't trusted by browsers by defaultâon first access you'll see a security warning. Accept the exception in your browser's security settings to proceed, then install your trusted certificate as described in the next step.

## Step 3 Upload your certificate

1. Log in to the **Cluster Management Console**.
2. On the **Home** page, select the Managed Cluster node that needs the new certificate.
3. On the **Node Details** page, select **Edit SSL certificate**.

   Sample SSL certificates edit page

   ![Onprem ssl certificates](https://dt-cdn.net/images/onprem-ssl-certificates-1329-e9535c4e34.png)

   Onprem ssl certificates
4. Paste or upload the key files you received from your CA.

   * **Private key**: your private key.
   * **Public key certificate**: your server certificate.
   * **Certificate chain**: your root and intermediate certificates.

   All keys and certificates must be in PEM format with full `BEGIN` and `END` headers.

   **Key format**:

   ```
   -----BEGIN PRIVATE KEY-----



   (Private Key)



   -----END PRIVATE KEY-----
   ```

   **Certificate format**:

   ```
   -----BEGIN CERTIFICATE-----



   (SSL Certificate)



   -----END CERTIFICATE-----
   ```
5. Select **Save** to upload the certificates.

Name-mismatch error

Your certificate is tied to a specific hostname. To avoid a name-mismatch error, make sure the common name (domain name) in the certificate matches the address shown in the browser's address bar.