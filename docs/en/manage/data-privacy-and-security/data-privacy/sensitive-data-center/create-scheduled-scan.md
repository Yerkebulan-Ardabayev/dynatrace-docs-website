---
title: Create scheduled scan in Sensitive Data Center
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan
scraped: 2026-02-26T21:21:43.547319
---

# Create scheduled scan in Sensitive Data Center

# Create scheduled scan in Sensitive Data Center

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Dec 16, 2025
* Preview

You can configure scheduled scans in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to continuously monitor your environment for sensitive data. You can choose to monitor specific buckets or the entire environment, select sensitive data types from built-in rules, and define how often the scan runs.

## Configure scans in Sensitive Data Scanner

To create a recurring scan for continuous monitoring

1. Go to ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.
2. Go to the **Scanner** tab and select **Create scan**.
3. Choose one or more **Sensitive data types** from the list, such as email address, credit card numbers, or IP addresses.
4. Define the scan interval by selecting the cadence depending on your compliance needs.
5. Select the **Log bucket scope** by either choosing specific buckets from the list or the entire environment.
6. Optional Apply scan policies to refine the scope of the scanâfor example, to exclude known false positives. For details, see [Create a policy in Sensitive Data Center](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy "Create a policy to enrich or filter request results with Sensitive Data Center.").
7. Provide a meaningful name for the scan.
8. Select **Create scan** to save the configuration.

The scan runs automatically at the defined interval and alerts you when data matching the selected criteria is found.

## Review scan results

The scanner dashboard provides a clear overview of scan statuses and highlights when sensitive data is found. From there, you can drill down into a specific scan to review detailed findings and understand exactly what was detected.

You can review the results and examine the data flow from ingestion to the storage location.

For environments with high log ingest volume, scan results may be sampled. Sampling is adaptive and helps reduce processing costs while maintaining detection accuracy. The sampling rate adjusts automatically based on your current log ingest volume.

## Mitigate potential findings

Based on scan results, you can take immediate action:

* [Configure or adjust masking rules](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") to prevent similar data ingestion.
* Change access permissions for stored data.
* Update [data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").
* Use [cleanup functionality](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data "Clean up data with Sensitive Data Center cleanup requests.") to delete sensitive data as needed.