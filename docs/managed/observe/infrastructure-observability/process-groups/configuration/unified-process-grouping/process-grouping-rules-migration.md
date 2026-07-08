---
title: Migrate to process grouping rules
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/unified-process-grouping/process-grouping-rules-migration
---

# Migrate to process grouping rules

# Migrate to process grouping rules

* How-to guide
* 3-min read
* Published Nov 10, 2025

This update combines the following into integrated process grouping rules:

* Simple detection rules
* Advanced detection rules
* Declarative process grouping rules

## Benefits of process grouping rules

You can now overwrite built-in detection rules and redefine process grouping and detection to activate split, merge, or no-monitoring. This combination now allows grouping based on environment variables, processes, properties, and user-defined strings. The same rules now apply across all agents and modes, reducing uncertainty about the right settings to change the default grouping.

## Migration scenarios

Depending on your previous process groups settings, there are two migration scenarios:

| Scenario | What happens |
| --- | --- |
| No previous detection rules | You are automatically migrated. |
| Existing declarative grouping, simple detection, or advanced detection rules | There is a [migration risk](#migration-risks) that process group entity IDs may change. You must migrate manually. |

### Migration constraints

| Total number of rules per scope | Limit |
| --- | --- |
| Declarative grouping + simple detection + advanced detection rules | < 400 |

## Migration Risks

Migrating to process grouping rules poses the following risks:

* Entity IDs will change for processes currently grouped by simple detection rules and advanced detection rules.
* The automatic migration may not meet all client needs, and manual adjustments may be necessary.

## Migrate manually to process grouping rules

### Prerequisites

* **Permissions**: To trigger the migration, you need either:

  + The `environment:roles:manage-settings` role.
  + Unconditional permissions for both `settings:objects:read` and `settings:objects:write`.

  For more information on roles and permissions, see [Identity and access management](/managed/manage/identity-access-management "Configure users, groups and permissions.").

  Without the required permissions, the **Migrate** button is unavailable.
* **OneAgent version**: You need OneAgent 1.329+ on all hosts.

### Migration process

For situations where previous detection rules exist, the rules are converted from the old settings as a read-only preview that allows manual verification. Once verified, you can press the **Migrate** button to switch to the new feature.

## Related topics

* [Configure process grouping rules](/managed/observe/infrastructure-observability/process-groups/configuration/unified-process-grouping/process-grouping-rules-configure "Learn how to split and merge process groups and process group instances through process grouping rules.")