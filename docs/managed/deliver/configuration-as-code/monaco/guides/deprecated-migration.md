---
title: Migrate deprecated configuration types
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/deprecated-migration
---

# Migrate deprecated configuration types

# Migrate deprecated configuration types

* How-to guide
* 3-min read
* Published Oct 25, 2022

The migration described here is relevant for version 1.x.

Converting a version 1.x project to 2.x automatically replaces deprecated Config API types.

If your version 1.x project still uses these deprecated types, some configurations might be duplicated after deployment.
To ensure a smooth upgrade, you should migrate deprecated types before conversion to 2.x.

This guide shows you how to migrate deprecated configuration types.

## Issue

Initial `dashboard`, `request-naming-service`, and `app-detection-rule` configurations were all affected by conflicts between their Dynatrace entity name attributes.

For example, dashboards (but the same applies to `request-naming-service` and `app-detection-rule`) don't have a unique name within a Dynatrace environment. Unfortunately, the Dynatrace Monaco CLI depends on name uniqueness to identify resources. In the case of dashboards, this resulted in missed/invalid downloads and conflicts during deployments.

The solution to this was generating custom UUIDs based on the Dynatrace Monaco CLI metadata. This brings many advantages, but the downside is that Monaco lost track of already deployed dashboards. A dashboard deployment would therefore result in a redeployment (and duplication) of potentially dozens of dashboards in Dynatrace.

The following procedure describes how to migrate a `dashboard` configuration, but it applies equally to `request-naming-service` and `app-detection-rule` configurations.

## Migrate configuration

To migrate a `dashboard` configuration

1. Review the existing configuration.

   Existing `dashboard` configurations usually look similar to this:

   `config.yaml`

   ```
   config:



   - DashboardConfigId: config.json



   DashboardConfigId:



   - name: Monaco Test



   - owner: Monaco User



   - isShared: true
   ```

   With `DashboardConfigId` as the user-defined key that links configuration details and `config.json`. Custom properties `name`, `owner`, and `isShared` are substituted in `config.json`:

   `config.json`:

   ```
   {



   "dashboardMetadata": {



   "dashboardFilter": null,



   "name": "{{ .name }}",



   "owner": "{{ .owner }}",



   "shared": {{ .isShared }},



   "tilesNameSize": null



   },



   "tiles": [



   ...



   ]



   }
   ```

   In a folder structure similar to this:

   ```
   workdir/



   project/



   app-detection-rule/



   ...



   dashboard/



   config.json



   config.yaml



   environment.yaml
   ```
2. **Recommended:** Because the user-defined key (in our example, `DashboardConfigId`) is used to automatically generate Dynatrace entity IDs in version 2, the easiest way to migrate an existing configuration is to substitute it with the actual Dynatrace entity ID. Dashboard entity IDs can be looked up either via the Dynatrace API or the Dynatrace web UI:

   `config.yaml`:

   ```
   config:



   - <DT entity UUID>: config.json



   <DT entity UUID>:



   - name: Monaco Test



   - owner: Monaco User



   - isShared: true
   ```

   The configuration is now compatible with version 2 of the dashboard configuration type.

   **Alternative:** After a configuration is deprecated and a new version is provided, all subsequent downloads create configurations of the new version. The existing configuration is kept, but not updated anymore:

   ```
   workdir/



   project/



   app-detection-rule-v2/



   ...



   dashboard/



   config.json



   config.yaml



   dashboard-v2/



   config.json



   config.yaml



   environment.yaml
   ```

   Although the newly downloaded `config.yaml` includes valid configuration keys, other custom properties (for example, the owner) are dropped:

   `dashboard-v2/config.yaml`:

   ```
   config:



   - <DT entity UUID>: config.json



   <DT entity UUID>:



   - name: Monaco Test
   ```

   This method, however, allows us to identify configuration instances by their name property and copy/paste their existing Dynatrace entity IDs instead of retrieving them by API or web UI.
3. For the Dynatrace Monaco CLI to recognize version 2 configurations, the incremental version has to be appended to the config folder, and `dashboard` becomes `dashboard-v2`:

   ```
   workdir/



   project/



   app-detection-rule-v2/



   ...



   dashboard-v2/



   config.json



   config.yaml



   environment.yaml
   ```

## Related topics

* [Migrate configuration from Monaco 1.x to 2.x](/managed/deliver/configuration-as-code/monaco/guides/migrating-to-v2 "Migrate existing Monaco 1.x projects to version 2.x.")