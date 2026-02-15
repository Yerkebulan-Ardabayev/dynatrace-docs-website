---
title: Log processing with classic pipeline
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-classic-log-processing
scraped: 2026-02-15T21:19:46.827160
---

# Log processing with classic pipeline

# Log processing with classic pipeline

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Dec 11, 2025

Dynatrace can transform your incoming log lines for improved clarity, analysis, and further transformation based on the log processing rules that you define. This approach is known as **log processing with the classic pipeline** or **classic log processing pipeline**.

Switch to log processing with OpenPipeline

Even thought the classic log processing pipeline is still available for some environments, we recommend switching to [log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.") as a powerful solution to manage, process, and analyze logs. Log processing with the classic pipeline will be deprecated at some point in the future.

Log processing occurs as log data arrives in the Dynatrace SaaS environment and before it is written to disk (stored). By setting log processing rules, you can process the log data as soon as it reaches Dynatrace. After the log data is processed, it's sent to storage and is available for further analysis. This method allows to process log data from all [log ingest](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") channels.

For example, you can extract numerical values from log lines using the classic log processing pipeline, turn these into metrics on the Dynatrace Platform, and include them in dashboards and problem detection.

DDU consumption

Log processing does not affect [DDU](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") consumption of log ingest.

Log processing with the classic pipeline is based on rules that contain a matcher and a processing rule definition.

* The matcher narrows down the available log data for executing this specific rule.
* The processing rule is a log processing instruction about how Dynatrace should transform or modify the log data from the matcher.

## Log processing steps

The classic log processing pipeline includes the following steps:

1. Automatic log processing on ingest

2. [Log processing with the classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.")

![Diagram - Steps of log processing with classic pipeline](https://dt-cdn.net/images/lma-log-processing-with-classic-pipeline-2500-3154c0acd9.png)

## Log processing rules

Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Log Monitoring** > **Processing** to view log processing rules that are in effect, reorder the existing rules, and create new rules. Rules are executed in the order in which they're listed, from top to bottom. This order is critical because a preceding rule may impact the log data that a subsequent rule uses in its definition.

All processing rules that match a log record are applied from top to bottom. An output from one rule is an input for the next one.

Expand **Details** to examine a rule definition. A log processing rule consists of the following:

* **Rule name**
* **Matcher**
* **Rule definition**

You can turn any rule on or off in the **Active** column.

## Built-in rules

By default, log processing with the classic pipeline includes many enabled built-in rules responsible for cleaning up or normalizing log data. The name of every built-in rule starts with `[Built-in]`.

You cannot modify these rules directly, but you have the ability to turn them off, copy their definitions, and create new rules with your modifications.

## Add a log processing rule

To create a log processing rule

1. Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Log Monitoring** > **Processing**.
2. Select **Add rule**.
3. Provide the name for the log processing rule.
4. Provide a log query in the **Matcher** section.  
   A log search query narrows down the available log data for executing this specific rule. Add a **Matcher** to your rule by pasting your [matcher-specific DQL query](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing.").

   Matching based on previous rules is not supported

   The matcher operates on the initial data set before applying any processing rules. Matching records modified by preceding rules is not supported. For example, the modified field in rule 1 and used for matching in rule 2 will contain the original value for that field and will not use the modified field in rule 1.
5. Provide the processing rule definition.  
   The processing rule definition is a log processing instruction about how Dynatrace should transform or modify your log data.

   The rule definition is created using log processing [commands](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-commands "Explore scenarios of how to use log processing commands in Dynatrace powered by Grail."), [functions](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-functions "Explore scenarios of how to use log processing functions in Dynatrace powered by Grail."), and pattern matching ([Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")) that allows you to add, transform, or remove incoming log records. This gives you total control over how your log data is presented to Dynatrace log monitoring.
6. Test the log processing rule.

   1. Provide a log sample.

      You can test the rule definition by providing a fragment of the sample log manually in the **Paste a log / JSON sample** text box. Make sure it's in JSON format. Any textual log data should be inserted into the `content` field of the JSON.
   2. Run the test.

      Select **Test the rule** and view the result in the **Test result** text box.
7. Select **Save changes**.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [DQL matcher in logs](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing.")