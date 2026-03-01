---
title: Explore findings
source: https://www.dynatrace.com/docs/secure/vulnerabilities/explore-findings
scraped: 2026-03-01T21:27:54.342241
---

# Explore findings

# Explore findings

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

The **Findings** page, accessible by selecting the **Findings** tab in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, consolidates [vulnerability findings](/docs/secure/threat-observability/concepts#vuln-findings "Basic concepts related to Threat Observability") from Dynatrace and integrated external security tools into a single, actionable view. It helps reduce noise from multiple scanners (network, web app, cloud, container, SAST), providing developers and security teams with a holistic view of vulnerabilities across assets and layers of their environments.

By default, the **Findings** page displays Dynatraceâgenerated results (thirdâparty and codeâlevel). To extend it with external findings, set up integrations via [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline."). For the list of supported integrations and setup instructions, see [Security events ingest](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").

## Manage results

In the findings table available on the **Findings** page, you can explore and refine vulnerability finding data:

* [**Filter and sort**](#filter-sort) findings by severity, product, timeframe, segments, or any available column.
* [**Format table**](#format) to switch perspectives between basic and detailed information.
* [**Show only unique IDs**](#deduplicate) to remove recurring findings.
* [**Visualize results**](#visualize) in a chart.

### Filter and sort

You have several options to filter and sort findings:

* **Filter by timeframe**: Define the period from which your data is being queried. If you don't specify the timeframe, the default `Last 30 minutes` is applied, meaning that the data being fetched is from the last thirty minutes.

  Show me how

  1. In the timeframe section, select one of the preset options or select the calendar for customization.
  2. Select **Apply**.
* **Filter by segments**: Segments provide quick access to predefined logical filters. The segment selector allows you to filter results based on these predefined logical filters.

  Show me how

  1. Open the segment selector .
  2. In **Filter by segments**, select a segment.
  3. Optional To add more segments, select  **Segments**; if available, you can select a value for the selected segment.
  4. When you're happy with the selection, select **Apply**.

  Selecting one or multiple segments results in fewer findings.

  For more information on segments and how they work, see [Segments](/docs/manage/segments "Use segments to logically structure and conveniently filter observability data across apps.").
* **Filter by expressions**: In the filter field, you can use complex filter expressions to select which information is to be displayed, such as:

  + Add multiple filters on the same filter key
  + Use `AND` and `OR` operators
  + Use the wildcard (`*`) to search for patterns
  + Filter numbers with `>` and `<`

  Show me how

  To filter by expressions, you have two options:

  + **Option 1**: Manually type the expression in the filter field.
  + **Option 2**: Filter by field values in the results table (hover over a cell and select a filter from the context menu ).

  To reset the filters to the default mode, select ![Close tab](https://dt-cdn.net/images/xmark-d8bb8b39d8.svg "Close tab") on the right of the filter field.

  If the selected filter doesn't show in the table, go to the ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column") column settings and make sure to add the corresponding column to the table.

* **Sort columns**: You can sort the order of columns and of results.

  Show me how to sort the order of columns

  To select the order of columns, you have two options:

  + **Option 1**: From the column settings (select the column settings ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column"), then use the up and down arrows and select **Confirm**).
  + **Option 2**: From the results table (select a column title, then select  **Move left** or  **Move right**).

  Show me how to sort the order of results

  To select the order in which results in a column should be displayed:

  1. Select a column title.
  2. Select  **Sort ascending** or  **Sort descending**.

  If more than 100,000 findings are displayed, sorting isn't available. This limitation prevents performance issues with very large result sets.  
  To enable sorting, narrow your scope by applying filters.

### Format table

In the upper-left corner of the table, you can choose between two preset views of the results:

* Select **Overview** to display basic information about the findings.
* Select **Detailed** to include more detailed information.

You can easily switch between the two views and customize them (add or remove columns) according to your needs.

### Remove duplicates

Many vulnerability findings are cyclical, reappearing in every scan if the environment or feed hasn't changed. This can create noise.

To reduce this noise, ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** removes duplicates: only the latest event of a finding with the same ID is displayed.

Two findings are considered duplicates (same finding ID) if all of the following fields match:

* `object.id`
* `vulnerability.id`
* `component.name`
* `component.version`
* `product.name`
* `product.vendor`

For details on these fields, see the [Dynatrace semantic dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").

To drill into an issue or specific affected object and observe the full historyâeven if it contains periodic identical findingsâturn off **Show unique findings** at the top of the table.

### Visualize results

The chart on the **Findings** page allows you to visualize results based on your selected criteria.

![findings chart](https://dt-cdn.net/images/2025-12-17-14-39-12-1856-e9a22b8ff8.png)

* The X-axis displays the time when the findings were detected.
* The Y-axis displays the count of the detected findings.

Select different dimensions using the **Split by** options in the drop-down list:

* **Severity**: Shows the distribution of findings by severity level (for example, Critical, High, Medium, Low).
* **Affected object**: Groups findings by the impacted Dynatrace entity (such as process, service, or host).
* **Provider**: Separates findings based on the source that reported them (for example, Dynatrace Runtime Vulnerability Analytics or an external security tool).

These options help you quickly identify trends and concentrations across different dimensions, reducing noise and highlighting where attention is most needed.

## Gain insights

Selecting a finding in the **Findings** table opens the details pane, which provides full context about the vulnerability. This view helps you quickly assess severity, trace affected components, and connect findings to remediation workflows.

The details pane includes:

* **Detection details**: When the finding was detected and its unique event ID.
* **Identifiers**: Related CVEs and linked security problems.
* **Severity & scores**: Severity level, CVSS score, and risk scores (ingested or calculated).
* **Affected object**: Name, type, and ID of the impacted Dynatrace entity, with links to its page.
* **Component metadata**: Component name, version, and package URL.
* **Source & product**: Which feature or product reported the finding (for example, Runtime Vulnerability Analytics).
* **Scan information**: Scan ID and related ingestion details.

Select the **Source** tab for a complete list of information available from the ingested finding.

## Collaborate with other apps

You can extend your analysis beyond ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** by sharing or reusing findings in other Dynatrace apps:

* **Download findings data as CSV** for offline analysis.

  1. Optional On the **Findings** page, apply any filters to narrow down the results.
  2. Select ![Download table](https://dt-cdn.net/images/download-table-data-ebb09d49cd.svg "Download table") to save the current view as a CSV file.
* **Open findings in other apps** using the  menu in the details pane next to the finding name (for example, you can send a finding to the ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** app with a preset DQL query scoped to that event).
* **Open values** from the **Source** tab of a finding's details pane directly in another app for deeper analysis.

## Further resources

* [Introducing findings in the Vulnerabilities app: Unified, granular insights for smarter securityï»¿](https://www.dynatrace.com/news/blog/introducing-findings-in-the-vulnerabilities-app-unified-granular-insights-for-smarter-security/)