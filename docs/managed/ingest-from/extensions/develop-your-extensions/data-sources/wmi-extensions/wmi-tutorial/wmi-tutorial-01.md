---
title: WMI tutorial - extension package
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01
scraped: 2026-05-12T12:15:54.373149
---

# WMI tutorial - extension package

# WMI tutorial - extension package

* How-to guide
* 1-min read
* Published Mar 30, 2022

Extensions extensions are based on a [YAML configuration file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework."). Its minimal contents are:

* `name` - Must begin with `custom:` for custom extensions
* `version`
* `author`
* `minDynatraceVersion` - Minimum Dynatrace version to enforce a minimum version of the extension schema

In this step you will

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create YAML file**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#create-file "Learn about WMI extensions in the Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Build your extension package**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#build-package "Learn about WMI extensions in the Extensions framework.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Upload your extension to Dynatrace Hub**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#upload-extension "Learn about WMI extensions in the Extensions framework.")

## Step 1 Create YAML file

Use the following template.

```
name: custom:demo.host-observability



version: # add version



minDynatraceVersion: "1.227"



author:



name: # add your name
```

Save your `extension.yaml` and developer key and certificates using the following structure:

```
my-sample-extension/



âââ src/



âââ extension.yaml



dashboards/



âââ dashboard.json



alerts/



âââ alert.json
```

## Step 2 Build and sign your extension package

In the `extensions` parent directory, run the following command:

```
dt extension assemble



dt extension sign --key ./developer.pem
```

These commands build your [extension package](/managed/ingest-from/extensions/concepts#package "Learn more about the concept of Dynatrace Extensions.") containing only the `extension.zip` archive and the `extension.zip.sig` signature file.

```
bundle.zip



|    extension.zip



|    extension.zip.sig
```

## Step 3 Upload your extension to Dynatrace Hub

To upload and activate your extension, run the following command:

```
dt extension upload bundle.zip
```

Example successful output:

```
C:\extension>dt extension upload bundle.zip



Tenant url: your-tenant-url



Api token: your-api-token



Extension upload successful!
```

For more information, see [Manage WMI extensions](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.").

## Results

Your extension shows up in Dynatrace as Active.

![result](https://dt-cdn.net/images/wmi-tutorial-hub-1050-7d02da15fb.png)

result

**Next step**: [WMI data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-02 "Learn about WMI extensions in the Extensions framework.")