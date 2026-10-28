---
title: Implicit propagation of tagging and management-zone rules
source: https://docs.dynatrace.com/managed/manage/tags-and-metadata-classic/basic-concepts/implicit-propagation-of-tagging-and-management-zone-rules
---

# Implicit propagation of tagging and management-zone rules

# Implicit propagation of tagging and management-zone rules

* Explanation
* 5-min read
* Updated on Oct 08, 2026

When you define an [auto-tagging rule](/managed/manage/tags-and-metadata-classic/setup/how-to-define-tags "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.") or a [management-zone rule](/managed/manage/identity-access-management-classic/permission-management/management-zones/management-zone-rules "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.") targeting a specific entity type, Dynatrace can automatically extend that rule's effect to related entity types through implicit propagation. These propagation paths are fixed and built into the Dynatrace rule engine; no additional configuration is required.

Implicit propagation means that metadata applied by a rule to a source entity type is automatically inherited by one or more target entity types, without any additional rule configuration. Propagation applies to newly created entities as well, so a child entity that appears after a rule is already active immediately inherits its parent's assignments.

Only auto-tagging rules and management-zone rules trigger implicit propagation. Conditional naming rules and entity-selector-based rules do not.

## Propagation paths

The following table lists all implicit propagation paths, the target entity types that inherit the metadata, and the rule types for which propagation is active.

| Source entity type | Propagates to | Available for | Notes |
| --- | --- | --- | --- |
| Process group | Process group instance | Auto-tagging, Management zones | Ensures tags and management-zone assignments applied to a logical process group automatically reach its runtime instances. |
| Process group | Process group instance, Container group | Management zones | Management-zone metadata flows to the instances and container groups related to the process group. |
| Process group | Container group instance | Management zones | Ensures containerized runtime instances receive process-group-level management-zone data. |
| Host | Kubernetes node | Auto-tagging, Management zones | Host-level metadata is propagated to the Kubernetes node that the host represents. |
| Host | EC2 instance, Container group instance | Management zones | Host-level metadata propagates to cloud instance representations and container group instances running on that host. |
| Hypervisor | vCenter | Management zones | Hypervisor-level metadata is visible on the associated vCenter object. |
| AWS credentials | AWS availability zone, AWS Lambda function, AWS application load balancer, AWS network load balancer, EC2 instance, Custom device, Custom device group, Auto scaling group, Relational database service | Management zones | Credential-level tags and labels propagate broadly across all AWS resource types discovered using those credentials. Expect wide propagation scope when targeting credential-level entities. |
| Cloud application | Cloud application instance | Management zones | Cloud-application metadata flows to its concrete running instances. |
| Synthetic test | Application | Management zones | Metadata on a synthetic test can flow to the application that the test targets. |

## When rules are evaluated

Auto-tagging, management-zone, and service naming rules are evaluated asynchronously against recently observed entities. During regular processing, rules that use standard conditions evaluate entities observed within the previous 2 hours, while entity-selector-based rules evaluate entities observed within the previous 6 hours. When a rule is created or changed, Dynatrace re-evaluates that rule for entities observed within the previous 7 days. The rule preview is different: it checks a specific rule on demand against entities observed within the previous 72 hours, but it doesn't apply tags or management zones.

An entity matches only when the entity and all attributes, relationships, and related entities required by the rule are available within the applicable evaluation timeframe. For example, a recently active entity might not match when the rule requires a related entity or relationship that wasn't observed within that timeframe.

You can't force a rule to evaluate inactive entities or configure a longer inactivity window. Dynatrace evaluates those entities again once they report data and the required rule data is available.

## Important considerations

* **Propagation is directional and not configurable.** Metadata flows only along the source-to-target edges listed above. There is no option to disable individual implicit propagation paths.
* **Propagation is not retroactive when a rule is removed.** Removing a rule stops future propagation, but does not automatically unassign tags or management zones that were already applied to target entities.
* **AWS credentials have broad scope.** When you apply a tag or management-zone rule to an AWS credentials entity, the result propagates to many AWS resource types simultaneously. Design your rules carefully to avoid unintended broad assignments.
* **Not all paths apply to auto-tagging.** Some implicit propagation paths are active for management zones only. Check the *Available for* column before relying on a specific path.
* **Conditional naming and entity-selector rules are excluded.** Implicit propagation is only triggered by auto-tagging rules and management-zone rules.

## Related topics

* [Define and apply tags](/managed/manage/tags-and-metadata-classic/setup/how-to-define-tags "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.")
* [Management-zone rules (Dynatrace Classic)](/managed/manage/identity-access-management-classic/permission-management/management-zones/management-zone-rules "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.")
* [Management zones (Dynatrace Classic)](/managed/manage/identity-access-management-classic/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")
* [Best practices and recommendations for tagging](/managed/manage/tags-and-metadata-classic/basic-concepts/best-practices-and-recommendations-for-tagging "Learn when it's recommended to use tags that leverage auto-detected metadata, as well as best practices for enriching Dynatrace monitoring with additional metadata.")