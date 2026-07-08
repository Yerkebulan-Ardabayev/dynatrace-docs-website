---
title: Update configuration in SaaS Upgrade Assistant
source: https://docs.dynatrace.com/managed/upgrade/saas-upgrade-assistant/sua-update-config
---

# Update configuration in SaaS Upgrade Assistant

# Update configuration in SaaS Upgrade Assistant

* Updated on Mar 11, 2025

Latest Dynatrace

You can directly update the imported configuration from Dynatrace Managed in ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** and deploy it to your environment in the following ways:

* Update via **Enter edit mode**—This allows you to modify your configurations without worrying about correct formats, without re-uploading the package or losing your deployment data.
* Update via [editable properties](/managed/upgrade/saas-upgrade-assistant/sua-update-editable-properties "Learn how to update configuration in SaaS Upgrade Assistant via editable properties.")—You can choose the single or bulk edit mode.

## Configuration structure

Let's review a configuration's structure to fully understand how edit mode works.

When you export or deploy configurations, each item is represented as a JSON payload. However, JSON payloads alone are not enough to efficiently perform operations like bulk editing or preparing a list of dependencies. That's why some information is additionally extracted as metadata. The extracted information can be referenced from inside the JSON using a special format.

To sum up, each configuration consists of the following data:

* Raw JSON—JSON after metadata extraction (extracted properties are referenced by their ID using `{{.propertyId}}` format)
* Metadata such as:

  + Name
  + Scope (only for "built-in" configurations)
  + Regular properties—the properties that can be edited with the **Bulk edit** functionality or in the **Edit properties** tab.
  + Configuration references—also called "reference properties." These are the properties that create dependencies between configurations, which can be previewed in the **Dependencies** tab.

When you use ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** to review configurations, the **JSON** tab doesn't show the raw JSON, but the JSON with all metadata already completed. This lets you preview the final payload deployed to your target environment. However, if you use edit mode to correct your configurations, you'll notice that the layout is closer to the above structure. This is so that you can fully manage both the raw JSON and the extracted metadata.

## How to edit a configuration in SaaS Upgrade Assistant

### Enter edit mode

There are two ways to enter edit mode:

* Select the context menu  icon of the chosen configuration, then select **Enter edit mode**.
* Select the pencil  icon in the lower-right corner of the JSON preview.

![How to access Enter edit mode ](https://dt-cdn.net/images/how-to-access-enter-edit-mode-1761-6b0529cc66.png)

How to access Enter edit mode

### Edit mode wizard

The top of the page displays the name of the configuration being edited and offers you the following actions:

* To change the page layout, use the columns  and rows  icons.
* To display the in-app guidelines, select **Learn more about edit mode**.

  The in-app micro guide contains detailed instructions on how to perform the following operations.

  **Edit JSON payload:**

  + Edit values
  + Add a new JSON node
  + Remove JSON node

  **Manage configuration properties (metadata):**

  + Edit values
  + Delete property
  + Add existing property to the JSON payload
  + Add a new property
* To preview changes, select **Validate and preview changes**. This option is active only if changes are detected. The preview window will then allow you to save your changes.
* To cancel your changes, select **Cancel**.

### JSON editor

The editor allows you to modify the underlying JSON by adding, editing, or removing nodes. Hover over a JSON node to see a set of icons representing available actions. The editor will ensure that the JSON format is correct.

### Table of properties representing extracted metadata

At the top of the table, there's a search bar and an option to create a property. For each property in the table, you can:

* View and copy the property ID
* View the category of the property
* Edit the property's value
* Remove the property
* Find the property in the JSON

Actions can differ for each property type, for example, the name property can't be removed, and the scope property can change its category. You can read more about those differences in the [Types of properties and how to manage them](#manage-properties) section.

Keep consistency between JSON and the table

Not all properties in the table need to be included in the JSON. For instance, the scope property is rarely included (instead, it's purposely added to the preview on the top level).

However, it is mandatory for all property IDs present in JSON to have their corresponding property in the table. For example, if a JSON node contains the value: `{{.extractedIDs.id_APPLICATION_2BAAB3940FB8931A}}`, then it is expected of the table to contain a property with the ID: `.extractedIDs.id_APPLICATION_2BAAB3940FB8931A`. Otherwise, the validation will fail, and you'll have to correct errors before you can save your changes.

Note that the removed properties, even though they just change visually and stay in the table (so you can undo the removal if you need to), are omitted during validation.

See the edit mode wizard

![The edit mode wizard](https://dt-cdn.net/images/the-edit-mode-wizard-1905-b26dcc95bf.png)

The edit mode wizard

## Types of properties and how to manage them

### Name

**ID:** `.name`

**Category:** `Metadata`

This is the simplest type of property. Every configuration has a name. It's used in ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** for display and can't be removed. For some configurations, names are extracted from JSON during the processing stage of the package upload, and they may represent different JSON nodes. If no suitable node is found, the default name will be assigned, for example: `unnamed disk options`.

Changes to such `unnamed` values won't be deployed to your target environment, but they can make configurations easier to find while working with ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**.

### Regular property

**ID:** starts with either `.extractedIDs` or `.customIDs`, for example `.extractedIDs.id_APPLICATION_2BAAB3940FB8931A`.

**Category:** varies

This is the property type that can be edited with the **Bulk edit** functionality or in the **Edit properties** tab. Apart from editing the value, edit mode also allows for the creation or removal of such properties. Properties you create can later be edited with the **Bulk edit**. Another new possibility is adding more occurrences to the JSON.

### Config reference property (dependency)

**Example ID:** `.syntheticlocation__SYNTHETIC_LOCATION22AAF80F0E2CAF4B__id`

**Category:** `Reference`

Sometimes configurations reference each other, which affects their deployment order and requirements. Dependent configurations must always be deployed together with their dependencies. This is not always a desired behavior, especially when dealing with cyclic dependencies. You can handle such cases in edit mode by removing or modifying the reference properties. You can even add new dependencies if desired.

**Note:** Any changes in reference properties require the dependency graph to be rebuilt. This is done automatically, but you might observe a longer saving time when working with such properties.

### Scope

**ID:** `.scope`

**Categories:** `String`, `Config reference`, or `Property reference`.

This property is available only for some types of configuration, but it's mandatory when present and can't be removed. It's the only type of property that can change its category. There are three possibilities:

* **String**—usually `environment`, meaning a global scope, but you can modify it freely according to your needs.
* **Config reference**—works in the same way as config reference properties described above. Changing it affects dependencies.
* **Property reference**—usually used when some entity is the scope of your configuration. For example, `disk options` are defined per host. Each `disk options` configuration will have a regular property of the host category, for example, `HOST-51FEDB44E1BB4DF4` with property ID `.extractedIDs.id_HOST_51FEDB44E1BB4DF4`. Scope references the host property by using its ID as value.

  See property reference example

  ![See the property reference example](https://dt-cdn.net/images/property-reference-example-1504-ea92d27d48.png)

  See the property reference example

## Create property

To create a new property, both regular and reference, select  **Create property** and fill in the pop-up window.

For regular properties, you need to select a category first, and then provide the value of the property. Property ID will be automatically filled in based on the value.

If you want to provide your own property ID, turn off **Use the value as property ID**.

## Revert changes

While edit mode allows you to modify a configuration freely, it also allows you to introduce problematic changes. If your modifications don't bring the desired effect, or if you saved some changes mistakenly, you can revert your changes to the original state.

There are a few things to keep in mind when reverting configurations:

* Reverting to the original state means returning to the state right after uploading the configuration package. Any changes made by editing properties, updating dashboard owners, or using edit mode will be lost. This includes changes made by other users.
* This operation can't be undone.
* Configurations already deployed to the target environment won't be affected. If some configurations were already deployed, you need to be aware of possible inconsistencies.
* This operation always includes reloading configurations and rebuilding the dependency graph, so it can take a while.

Reverting configurations can be done on multiple levels:

* **Single configuration**—as with edit mode, select the context menu  icon of the chosen configuration, and then select **Revert changes**.
* **Filtered configurations**

  1. Go to the **Upgrade details: configuration** tab and set your filters.
  2. Select the context menu  icon below the **Configuration objects** graph.
  3. Select **Revert changes to all (number)**.
* **All configurations**

  1. Go to the **Upgrade details: configuration** tab.
  2. Select the context menu  icon at the bottom of the page.
  3. Select **Revert changes to all (number)**.

When reverting only some configurations, other ones will be unaffected.

After the revert operation, you'll see a list of configurations with their content reverted.

It's also possible that all configurations taking part in the revert are already in the original state. In that case, the revert won't be performed.

## Use edit mode to solve known issues

### Failed to store configuration (Unacceptable space in the configuration name)

Some configurations don't allow trailing spaces in the configuration name, for example, `application-web` configurations. You may see the following error message after deployment:

`Given property 'applicationName' with value: 'Title ' violates the following constraint: Must not have leading or trailing spaces.`

This issue can be solved by editing the name property in edit mode. In this case, `Title`  (notice the space) needs to be changed to `Title` (no space).

![Unacceptable space](https://dt-cdn.net/images/space-to-be-removed-935-162db8f1c4.png)

Unacceptable space

### Exception when parsing DQL query

Log matching rules must be converted from LQL to DQL before the deployment. ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** doesn't handle the conversion itself. For details, see [Conversion to DQL for Logs﻿](https://docs.dynatrace.com/docs/shortlink/lma-conversion-to-dql).

However, you can use edit mode to manually correct simple queries.

Let's see this configuration of type `builtinlogmonitoring.schemaless-log-metric` as an example:

```
{



enabled: true



key: "log.test1"



query: "host.name="HOST1""



measure: "OCCURRENCE"



dimensions: []



}
```

Trying to deploy this configuration will result in the deploy error with the following message:

`Caught exception when parsing DQL query 'host.name="HOST1"'`.

With edit mode, you can fix this configuration by replacing the query with `matchesValue(host.name, "HOST1")`, which is valid DQL.

### Constraints violated

This issue can apply to many different cases, but let's take a look at the one related to `calculated-metrics-service`. The following error message could be encountered after deployment:

`At least one condition of the following types must be used: [SERVICE_DISPLAY_NAME, SERVICE_PUBLIC_DOMAIN_NAME, SERVICE_WEB_APPLICATION_ID, SERVICE_WEB_CONTEXT_ROOT, SERVICE_WEB_SERVER_NAME, SERVICE_WEB_SERVICE_NAME, SERVICE_WEB_SERVICE_NAMESPACE, REMOTE_SERVICE_NAME, REMOTE_ENDPOINT, AZURE_FUNCTIONS_SITE_NAME, AZURE_FUNCTIONS_FUNCTION_NAME, CTG_GATEWAY_URL, CTG_SERVER_NAME, ACTOR_SYSTEM, ESB_APPLICATION_NAME, SERVICE_TAG, SERVICE_TYPE, PROCESS_GROUP_TAG, PROCESS_GROUP_NAME]`

This can be resolved by adding an appropriate JSON node in edit mode. Here, that would be a condition inside the `conditions` array, for example:

```
conditions: [



0: {



attribute: "SERVICE_WEB_SERVICE_NAME"



comparisonInfo: {



caseSensitive: false



comparison: "EXISTS"



negate: false



type: "STRING"



value: null



values: null



}



}



]
```

### Given entity ID not found

Not all entities need to be migrated when upgrading from Managed to SaaS. Sometimes, you may need to simply get rid of an entity ID—such as getting rid of test steps from Synthetic monitors. This can now be achieved by removing JSON nodes in edit mode.

## FAQ

What does "raw" JSON mean?

Raw JSON is the content of a JSON payload file stored by ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** without any processing. It's what you see in the JSON editor when using edit mode. That means the IDs of extracted properties are exposed to you and you must manage their usage.

What happens during the configuration export?

When exporting configurations, Monaco will create a separate directory for each configuration type. Inside the directory, we can find many raw JSONs and a single `config.yaml` file. This YAML file contains the metadata for all JSONs in the directory.

How can I edit the config.yaml file using edit mode?

The `config.yaml` file contains multiple entries, each for one configuration. Only the item related to the edited configuration is modified. Additionally, not all YAML properties are editable with edit mode. Let's take a look at the following fragment of the `config.yaml` file as an example:

```
configs:



- id: 955423ac-a4e5-3dc6-952a-adc35b736f01



config:



name: [Built-in] cloud:aws:cloudtrail



parameters:



extractedIDs:



type: value



value:



id_69de2278_ef7a_4b9a_bdc5_a78c9210ea4e: 69de2278-ef7a-4b9a-bdc5-a78c9210ea4e



id_249491df_4970_421d_8575_5bf555357c14: 249491df-4970-421d-8575-5bf555357c14



networkzone__useast1__id:



configId: us-east-1



configType: network-zone



property: id



type: reference



template: 955423ac-a4e5-3dc6-952a-adc35b736f01.json



skip: false



originObjectId: vu9U3hXa3q0AAAABACNidWlsdGluOmxvZ21vbml0b3JpbmcubG9nLWRwcC1ydWxlcwAGdGVuYW50AAZ0ZW5hbnQAJGM1ODQxMTJmLTk1MWUtNDRkNC1hNjg3LTg4MmMyYmEyZDhlMr7vVN4V2t6t



type:



settings:



schema: builtin:logmonitoring.log-dpp-rules



schemaVersion: 1.0.20



scope: environment
```

With edit mode, you can edit:

* `config.name`
* `type.settings.scope`
* `config.parameters`—All operations are supported; you can manage properties of both value and reference type, you can change their values, remove them, or add new properties.

Edit mode doesn't support editing the following YAML properties:

* `id`—Necessary to identify the config.
* `config.template`—Binds JSON with its metadata.
* `config.skip`—Automatically changed during the deployment depending on which configurations are included.
* `config.originObjectId`—Refers to the source configuration and is used during deployment as an additional identifier.
* `type.settings.schema` and `type.settings.schemaVersion` (for "built-in" configurations)—Necessary to deploy configurations to correct APIs.
* `type.api` (if not “built-in”)—Necessary to deploy configurations to correct APIs.