---
title: Log processing (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-processing
scraped: 2026-02-17T21:27:55.307394
---

# Log processing (Logs Classic)

# Log processing (Logs Classic)

* Explanation
* 3-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace Log Monitoring can reshape incoming log data for better understanding, analysis, or further processing based on log processing rules that you create.

Information can be logged in a very wide variety of formats depending on the application or process, operating system or other factors. Log processing offers a central and flexible way of extracting value from those raw log lines.

For example, you can extract numerical values from log line via log processing, turn these into metrics on Dynatrace Platform, and include them in dashboards and problem detection.

Log processing does not affect [DDU](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") consumption of log ingest.

## Log processing rules

Go to **Settings** > **Log Monitoring** > **Processing** to view log processing rules that are in effect, reorder the existing rules, and create new rules. Rules are executed in the order in which they're listed, from top to bottom. This order is critical because a preceding rule may impact the log data that a subsequent rule uses in its definition.

Expand **Details** to examine a rule definition. A log processing rule consists of the following:

* **Rule name**
* **Matcher**
* **Rule definition**

You can turn any rule on or off in the **Active** column.

## Built-in rules

By default, log processing includes many enabled built-in rules responsible for cleaning up or normalizing log data. The name of every built-in rule starts with `[Built-in]`.

You cannot modify these rules directly, but you have the ability to turn them off, copy their definitions, and create new rules with your modifications.

## Add a log processing rule

To create a log processing rule

1. Go to **Settings** > **Log Monitoring** > **Processing**.
2. Select **Add rule**.
3. Provide the name for the log processing rule.
4. Provide a log query in the **Matcher** section.  
   A log search query narrows down the available log data for executing this specific rule. This is the same search query that you have been using in the [log viewer search query](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

   Matching based on previous rules is not supported

   The matcher operates on the initial data set before applying any processing rules. Matching records modified by preceding rules is not supported. For example, the modified field in rule 1 and used for matching in rule 2 will contain the original value for that field and will not use the modified field in rule 1.
5. Provide the processing rule definition.  
   The processing rule definition is a log processing instruction about how Dynatrace should transform or modify your log data narrowed down by the **Log query**.

   The rule definition is created using log processing [commands](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands "Use log processing commands that reshape your incoming log data for better analysis or further processing."), [functions](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-functions "Use log processing data types that reshape your incoming log data for better analysis or further processing."), and pattern matching that allows you to add, transform, or remove incoming log records. This gives you total control over how your log data is presented to Dynatrace Log Monitoring.
6. Test the log processing rule.  
   You can test the rule definition by either downloading the sample log or providing a fragment of the sample log manually in the **Log sample** text box.

   1. Select a log sample.

      * If you choose to download the sample log, the data used for testing the rule is the matched result of the **Log query**.
      * If you choose to provide a fragment of the log data manually, make sure it's in JSON format. Any textual log data should be inserted into the `content` field of the JSON.
   2. Run the test.

      Select **Test the rule**, and view the result in the **Test result** text box.
7. Select **Save changes**.