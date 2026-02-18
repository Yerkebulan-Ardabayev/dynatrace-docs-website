---
title: Dynatrace settings framework
source: https://www.dynatrace.com/docs/manage/settings/settings-20
scraped: 2026-02-18T21:29:20.555717
---

# Dynatrace settings framework

# Dynatrace settings framework

* Latest Dynatrace
* Explanation
* 4-min read
* Published Jan 18, 2023

The Settings 2.0 framework provides a unified instrument to control various configurations in Dynatrace. Whether you use the Dynatrace web UI or the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), you're setting the same configurations with the same effect.

Each Settings 2.0 configuration is represented by a *settings object* (which defines a particular set of parameters) and is based on a *settings schema* (which defines which parameters the configuration includes). Schemas are created and managed by Dynatrace; you cannot create your own schemas. Objects, on the other hand, are entirely within your control.

## Scope and hierarchy of settings

Many settings can be set for different scopes (for an entire monitoring environment or a specific entity). The default scope is global (the entire monitoring environment).

Configurations that are available via **Settings** (in Dynatrace, go to **Settings**) affect the entire environment. You can check for existing entity-level overrides of the environment-level setting. Select **More** (**â¦**) > **Hierarchy and overrides**. From here, you can easily navigate to entity-level configurations, which in turn provide information on the parent setting.

![Global settings with overrides](https://dt-cdn.net/images/settings-global-1717-6ffb544dd6.png)

The most specific setting always takes precedence. For example, a configuration on the host level overrides a configuration on the host-group level, and in turn, a host-group level configuration overrides an environment-level configuration.

![Entity-level settings](https://dt-cdn.net/images/settings-host-level-1238-af32c1f6d5.png)

If a setting is available at multiple levels, manage it on the highest possible level. High-level settings scale automatically to every child entity; you don't have to apply them manually.

## Ordered settings

For some settings, the order of the items is essential. For example, naming rules are evaluated in a particular order, and the first matching rule applies.

Ordered settings can be defined on the global and entity level. However, hierarchy works slightly differently hereâentity-level settings don't override global settings, they extend them. The list of entity-level settings is prepended on top of the global list; therefore, entity-level rules are evaluated first. If none of the entity-level rules apply, the evaluation continues with global rules.

You can easily re-order ordered items by dragging and dropping them to the required position.

![Settings - reorder list](https://dt-cdn.net/images/settings-reorder-1139-338c062399.png)

## Configuration history

Every Settings 2.0 configuration maintains a history of changes, keeping track of changes to the configuration and who made these changes. To access history, select **More** (**â¦**) > **Revision history**.

![Settings history](https://dt-cdn.net/images/settings-history-1242-a32e589da1.png)

## Permissions and access

Access to settings is controlled via [IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"). Policies enable you to create flexible and granular access to configurations, where users have access only to those settings where they have permissions assigned. No additional permissions are needed for policies to take effect. Policies grant access to configurations via both the Dynatrace web UI and the Settings API unless configured otherwise on the schema level.

If you need to configure fine-grained access to certain entities, you can do so via management zones or host groups. Note that an entity might be a part of multiple management zones but only one host group, which makes the host-group-based approach more direct, while the management-zone-based approach provides more flexibility.

To learn how to configure access policies for settings, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#settings "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."). Below you can find some sample policies.

Grant read and write access to the service-level objective definitions settings

```
ALLOW settings:objects:read, settings:objects:write, settings:schemas:read



WHERE settings:schemaId = "builtin:monitoring.slo";
```

Grant read and write access to all cloud automation settings

```
ALLOW settings:objects:read, settings:objects:write, settings:schemas:read



WHERE settings:schemaGroup = " group:cloud-automation";
```

Grant read-only access to management zones definitions

```
ALLOW settings:objects:read, settings:schemas:read



WHERE settings:schemaId = "builtin:management-zones";
```

Grant read and write access to all settings of the easyTravel host group and its hosts

```
ALLOW settings:schemas:read;



ALLOW settings:objects:read, settings:objects:write



WHERE settings:entity.hostGroup = "easyTravel";
```

Grant read and write access to all settings of all entities with the security context "easyTravel"

```
ALLOW settings:schemas:read;



ALLOW settings:objects:read, settings:objects:write



WHERE settings:dt.security_context = "easyTravel";
```

Grant read and write access to all settings of all entities within the easyTravel management zone

This policy also affects global settings that apply to the easyTravel management zone.

```
ALLOW settings:schemas:read;



ALLOW settings:objects:read, settings:objects:write



WHERE environment:management-zone = "easyTravel";
```

Grant read and write access to the infrastructure anomaly settings on hosts within the easyTravel management zone

```
ALLOW settings:schemas:read;



ALLOW settings:objects:read, settings:objects:write



WHERE settings:schemaId = "builtin:anomaly-detection.infrastructure-hosts" AND environment:management-zone = "easyTravel";
```

## Related topics

* [Settings 2.0 - Available schemas](/docs/dynatrace-api/environment-api/settings/schemas "View the entire settings schemas table of your monitoring environment via the Dynatrace API.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")