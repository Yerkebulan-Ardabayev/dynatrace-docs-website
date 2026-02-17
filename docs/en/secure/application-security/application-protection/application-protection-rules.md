---
title: Runtime Application Protection monitoring rules
source: https://www.dynatrace.com/docs/secure/application-security/application-protection/application-protection-rules
scraped: 2026-02-17T04:58:24.892366
---

# Runtime Application Protection monitoring rules

# Runtime Application Protection monitoring rules

* Latest Dynatrace
* How-to guide
* Updated on Jul 25, 2025

Dynatrace Runtime Application Protection rules allow you to

* [Set up fine-grained monitoring rules to block, monitor, or ignore future attacks](#handling-rules), based on [resource attributes](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."), and define multiple conditions for one rule. When creating a rule, you can check if conditions apply and how many process groups are affected.
  The rules you create override the global attack control settings for the selected technology.
* [Add attacks that you don't consider harmful to the allowlist](#exception-rules), by source IPs or attack patterns.

## Define specific attack control rules

To create an attack rule

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New)**.
2. On the **Monitoring rules** tab, select  **Add new rule**.
3. Define the rule:

   * **Rule name**: The name under which your rule will be listed.
   * **Attack control**: Specify how to control an attack that matches the rule criteria:

     + `Off; incoming attacks NOT detected or blocked.`
     + `Monitor; incoming attacks detected only.`
     + `Block; incoming attacks detected and blocked.`
   * **Attack type**: Select the attack type to which current configuration applies.
   * Optional **Specify where the rule is applied**: If you want the rule to apply only to a subset of your environment, select  **Add condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").
4. Select **Create**.
5. Restart processes.

You can edit, disable, enable, or remove rules at any time.

## Define exception (allowlist) rules

Based on specific criteria, you can create an exception monitoring rule for the attack.

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New)**.
2. On the **Allowlist rules** tab, select  **Add new rule**.
3. Define the exception rule:

   * **Attack control**: Select one of the options below:

     + `Off; incoming attacks NOT detected or blocked` to ignore the attacks based on the subsequently defined criteria
     + `Monitor; incoming attacks detected only` to monitor the attacks based on the subsequently defined criteria, but not block them
   * **Define the rule**: Select  **Add condition** to set up fine-grain conditions that need to be met to allow an attack.

     Most key/matcher combinations available in the drop-down list require OneAgent version 1.309+.

     For OneAgent versions earlier than 1.309, the only available options are:

     + key: `entry_point.payload`, matcher: `contains`
     + key: `actor.ip`, matcher: `is part of IP CIDR`

     To fully benefit from this functionality, make sure you're using the latest OneAgent version.
   * Optional **Specify where the rule is applied**: If you want the rule to apply only to a subset of your environment, select  **Add condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").
4. Select **Create**.

You can edit, disable, enable, or remove rules at any time.

## FAQ

* [How does Dynatrace actually block attacks?](/docs/secure/faq#block-attacks "Frequently asked questions about Dynatrace Application Security.")
* [How is an attacker's IP determined?](/docs/secure/faq#attacker "Frequently asked questions about Dynatrace Application Security.")

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")