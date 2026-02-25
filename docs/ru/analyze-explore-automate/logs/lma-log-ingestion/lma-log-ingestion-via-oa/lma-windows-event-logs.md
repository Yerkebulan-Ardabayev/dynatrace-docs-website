---
title: Windows event logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-windows-event-logs
scraped: 2026-02-25T21:30:53.349888
---

# Windows event logs

# Windows event logs

* Latest Dynatrace
* Tutorial
* Updated on Aug 15, 2025

Windows Event Logs are a detailed record of notifications stored by the Windows operating system. These logs are used for troubleshooting and monitoring the health and security of a system. Dynatrace OneAgent is using native Windows API to gather all log records. There are three main logs:

* Application Logs: Contains events logged by applications or programs.
* System Logs: Contains events logged by Windows system components.
* Security Logs: Contains security-related events like login attempts and resource access.

Windows Event Logs are automatically detected and can be ingested using the Dynatrace OneAgent. You can provide custom Event Logs by the [Custom log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source#configure-log-source-mainclscuipage "Configure custom log sources to manually add log data sources that have not been autodetected.") configuration.

## Configure Windows event logs ingestion

There are multiple ways to configure your Windows event logs. To enable and customize their ingestion, follow the steps below.

### Set query timeout

Before you start the actual configuration, set the value for the **Windows Event Log query timeout**:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log monitoring** > **Advanced log settings**.
2. In the **Windows Event Log query timeout** field, input a value, in seconds, to define the maximum timeout value for the query extracting the Windows Event Logs.

### Enable Windows event log ingestion

The following configuration allows Windows event logs to be ingested and ready for analysis. Follow the steps below:

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Enable the **[Built-in] Windows system, application, and security logs** rule.

If the **[Built-in] Ingest all logs** option is enabled, Windows event logs are automatically included, and no additional configuration is required to enable their ingestion.

### Create an ingest rule based on the Windows event logs attributes

The steps below are required in case you want to customize log ingest rules when you need to collect only specific Windows event logs based on their attributes, rather than ingesting all available logs.

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.
3. Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
4. Select **Add condition**.
5. From the **Matcher attribute** dropdown, and select one or more of the Windows log [attributes](#attributes).
6. Input the matcher in the **Value** field, according to the chosen attribute, and select **Add matcher**.
7. Select **Save changes**.

### Create an ingest rule based on the Windows event logs name

The steps below are required in case you want to customize log ingest rules when you need to collect only specific Windows event logs based on their names, rather than ingesting all available logs.

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.
3. Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
4. Select **Add condition**.
5. From the **Matcher [attribute](#attributes)** dropdown, and select **Log source**.
6. Input one or more Windows log matchers in the **Value** field (**Windows Application Log**, **Windows Security Log**, or **Windows System Log**), and select **Add matcher**.
7. Select **Save changes**.

## Add a custom Windows event log source

Custom Windows event log sources are useful when you need to ingest logs from custom application logs or logs created by third-party software. For example, if your organization has a custom application, you can use this feature to collect and analyze its own dedicated event logs in Dynatrace.

To ingest custom Windows event logs, you can define a custom log source. Follow the steps below to configure and add a custom Windows event log source according to your requirements.

1. Go to **Settings** > **Log Monitoring** > **Custom log sources**.
2. Select **Add custom log source** and provide the name for your configuration in the **Rule name** field.
3. Optional Bind your rule to a **Process group** by selecting the process group name from the dropdown menu.
4. Select the **Windows Event** log option for the custom log source path.
5. Select **Add custom log source path**, and enter the full name for the event log source.
6. Select **Save changes**.
7. If required, add the corresponding ingest rule.

## Attributes selected in Windows event logs

For Windows event logs, Log Monitoring detects the following fields and sends them as custom attributes:

## Support for structured data

This feature enables the collection of structured data from Windows Event Logs in the **User Data** or **Event Data** branches (depending on the availability), along with their sub-branches. The collected data is transmitted along with the record content in the form of attributes.

To enable this feature, go to **Settings** > **Log Monitoring** > **Log module feature flags**, and enable the **Support for structured data in Windows Event Logs** feature flag.

Attribute names are assigned based on available information, such as tag names, the value of the **Name** field, or, if tag names are repeated and the **Name** field is absent, a sequential number is added to the tag name.

* Sub-branches without values and tags labeled as Binary are omitted.
* A prefix is always added to the attribute name `winlog.data`.
* Numbering of consecutive fields (if necessary, the same attribute name) also includes fields with empty values.

Given below are examples of branches and attributes:

Data in the EventData section

Event log raw data:

```
- <EventData>



<Data Name="CallerProcessId">16548</Data>



<Data Name="CallerProcessImageName">vctip</Data>



<Data Name="Type">client</Data>



</EventData>
```

Parsed attributes:

```
AttributeKey: winlog.data.CallerProcessId, AttributeValue: 16548



AttributeKey: winlog.data.CallerProcessImageName, AttributeValue: vctip



AttributeKey: winlog.data.Type, AttributeValue: client
```

Data in the UserData section

Event log raw data:

```
- <UserData>



-   <CbsPackageChangeState xmlns="http://manifests.microsoft.com/win/2004/08/windows/setup_provider">



<PackageIdentifier>KB5058405</PackageIdentifier>



<IntendedPackageState>5112</IntendedPackageState>



<IntendedPackageStateTextized></IntendedPackageStateTextized>



</CbsPackageChangeState>



</UserData>
```

Parsed attributes:

```
AttributeKey: winlog.data.CbsPackageChangeState.<xmlattr>.xmlns, AttributeValue: http://manifests.microsoft.com/win/2004/08/windows/setup_provider



AttributeKey: winlog.data.CbsPackageChangeState.PackageIdentifier, AttributeValue: KB5058405



AttributeKey: winlog.data.CbsPackageChangeState.IntendedPackageState, AttributeValue: 5112
```

Binary data and empty data fields

Event log raw data:

```
- <EventData>



<Data>WinRT Intellisense PPI - en-us</Data>



<Data>10.1.19041.685</Data>



<Data>(NULL)</Data>



<Data />



<Binary>7B31354532394146462D434231392D413230422D394138312D4230373635413633313135467D3030303063306133616532343933363166643732376335306533653966623534363139633030303030393034</Binary>



<Data>Test</Data>



</EventData>
```

Parsed attributes:

```
AttributeKey: winlog.data.Data1, AttributeValue: WinRT Intellisense PPI - en-us



AttributeKey: winlog.data.Data2, AttributeValue: 10.1.19041.685



AttributeKey: winlog.data.Data3, AttributeValue: (NULL)



AttributeKey: winlog.data.Data5, AttributeValue: Test
```