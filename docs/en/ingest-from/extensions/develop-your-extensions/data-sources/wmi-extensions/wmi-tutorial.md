---
title: WMI data source tutorial
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial
scraped: 2026-02-17T21:32:21.557001
---

# WMI data source tutorial

# WMI data source tutorial

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Mar 30, 2022

This is a step-by-step tutorial for building a WMI data source-based extension. You will build a WMI extension that runs on OneAgent and monitors a Windows host.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Generate a developer certificate and key**](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#generate-certificate-and-key "Learn about WMI extensions in the Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Distribute the root certificate to Dynatrace components**](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#distribute-root-certificate "Learn about WMI extensions in the Extensions framework.")

## Before you begin

To successfully develop an Extensions extension and be able to complete this tutorial, you need to fulfill the following prerequisites:

* Admin access to a Dynatrace SaaS or Managed environment version 1.227+
* Windows host (virtual machine)
* OneAgent version 1.227+ deployed on the host
* Dynatrace CLI

  + Python 3.10
  + Access to pip package installer for Python
  + Install dt-cli

    ```
    pip install dt-cli
    ```

    For more information, see [Sign extensions](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").
* Your root certificate uploaded to Dynatrace and on the OneAgent host

## Step 1 Generate a developer certificate and key

```
dt extension genca



dt extension generate-developer-pem -o developer.pem --ca-crt ca.pem --ca-key ca.key --name 'JDoe'
```

The command generates the following files:

* `developer.pem` - your developer certificate
* `ca.pem` - your root certificate
* `ca.key` - your root key

## Step 2 Distribute the root certificate to Dynatrace components

### Upload to the Dynatrace Credential Vault

1. Go to **Credential Vault**.
2. Select **Add new credential**.
3. For **Credential type**, select **Public Certificate**.
4. Select the **Extension validation** credential scope.
5. Add a meaningful **Credential name**.
6. Upload the **Root certificate file**.
7. Select **Save**.

### Upload to OneAgent host that runs the extension

1. Go to the following directory:

   * Windows: `C:\ProgramData\dynatrace\oneagent\agent\config`
   * Linux: `/var/lib/dynatrace/oneagent/agent/config/`
2. Go to the `certificates` folder (create it if it doesn't exist)
3. Upload your root certificate (`ca.pem`) generated earlier

Your Dynatrace environment is ready to start creating your WMI extension.

**Next step**: [Extension package](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01 "Learn about WMI extensions in the Extensions framework.")