---
title: Runtime Application Protection monitoring rules
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/application-protection-rules
---

# Runtime Application Protection monitoring rules

# Runtime Application Protection monitoring rules

* How-to guide
* Updated on Feb 23, 2026

What you’ll find on this page

* [How to define attack‑handling rules to block, monitor, or ignore attacks](#handling-rules)
* [How to create exception (allowlist) rules for attacks you consider safe](#exception-rules)
* [Frequently asked questions](#faq)

Dynatrace Runtime Application Protection rules allow you to

* [Set up fine-grained monitoring rules to block, monitor, or ignore future attacks](#handling-rules), based on [resource attributes](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields."), and define multiple conditions for one rule. When creating a rule, you can check if conditions apply and how many process groups are affected.
  The rules you create override the global attack control settings for the selected technology.
* [Add attacks that you don't consider harmful to the allowlist](#exception-rules), by source IPs or attack patterns.

## Define specific attack control rules

1. Go to **Settings** > **Application security** > **Application Protection** > **Monitoring rules**.
2. Select **Add new rule**.
3. Optional Name your rule (if not, a name will be assigned to it automatically once you create the rule, based on your criteria).
4. For **Attack control**, specify how to control an attack that matches the rule criteria:

   * `Off; incoming attacks NOT detected or blocked.`
   * `Monitor; incoming attacks detected only.`
   * `Block; incoming attacks detected and blocked.`
5. For **Attack type**, select the attack type to which current configuration applies.
6. Optional If you want the rule to apply only to a subset of your environment, for **Specify where the rule is applied**, select **Add new condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").
7. Optional To check if a rule applies, select **Preview matching process group instances**. This lists process group instances that currently match the criteria.
8. Select **Save changes**.
9. Restart processes.

You can edit, disable, enable, or remove rules at any time.

## Define exception (allowlist) rules

1. Go to **Settings** > **Application Security** > **Application Protection** > **Allowlist** and select **Add new exception rule**.
2. For **Define attack control for chosen criteria**, select one of the options below:

   * `Off; incoming attacks NOT detected or blocked` to ignore the attacks based on the subsequently defined criteria
   * `Monitor; incoming attacks detected only` to monitor the attacks based on the subsequently defined criteria, but not block them
3. For **Define the rule**, select **Add new condition** to set up fine-grain conditions that need to be met to allow an attack.

   Most key/matcher combinations available in the drop-down list require OneAgent version 1.309+.

   For OneAgent versions earlier than 1.309, the only available options are:

   * key: `entry_point.payload`, matcher: `contains`
   * key: `actor.ip`, matcher: `is part of IP CIDR`

   To fully benefit from this functionality, make sure you're using the latest OneAgent version.
4. Optional If you want the rule to apply only to a subset of your environment, for **Specify where the rule is applied**, select **Add new condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").
5. Optional To check if a rule applies, select **Preview matching process group instances**. This lists process group instances that currently match the criteria.
6. Select **Save changes**.

You can edit, disable, enable, or remove rules at any time.

## FAQ

* [How does Dynatrace actually block attacks?](/managed/secure/faq#block-attacks "Frequently asked questions about Dynatrace Application Security.")
* [How is an attacker's IP determined?](/managed/secure/faq#attacker "Frequently asked questions about Dynatrace Application Security.")

## Related topics

* [Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")