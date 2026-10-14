---
title: Define tags and metadata for hosts
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts
---

# Define tags and metadata for hosts

# Define tags and metadata for hosts

* How-to guide
* 5-min read
* Updated on Oct 02, 2026

Within dynamic or large environments, manual host tagging can be impractical. For dynamic deployments that include frequently changing host instances and names (for example, AWS or MS Azure), you should automate adding tags and metadata to your hosts.

### Tags

To automate the addition of tags to your hosts using OneAgent versions 1.189+, use OneAgent command-line parameters. For earlier versions, use the host tag configuration file.

### OneAgent command-line parameters for tags

OneAgent version 1.189+

To add or change host tags, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**  
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
  You can add or change more than one tag in the same command. You can also define tags with the same key but different values.

For more information on `oneagentctl`, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

### Edit the host tag configuration file

OneAgent version 1.187 and earlier

UTF-8 encoded

Any `hostautotag.conf` or `hostcustomproperties.conf` files created should be encoded in UTF-8.

During OneAgent installation, the installer creates a simple `hostautotag.conf` configuration file on the monitored host. On Windows, the file is located in `%PROGRAMDATA%\dynatrace\oneagent\agent\config`, and on Linux in `/var/lib/dynatrace/oneagent/agent/config`.

The file should contain a list of strings or key/value pairs that will be reported to the server with every file change. New lines or spaces are used to separate tag values. For example:

```
TestHost Gdansk role=fallback
```

### Result

After you configure them, the tags are displayed at the top of the **Properties and tags** section of the host overview page.

Tags created using `oneagentctl` behave similarly to [automated, rule-based tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.") and [environment variable-based tags](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.").

They are prefixed with the `[Environment]` string and can't be removed manually from a host. They can only be removed through a `oneagentctl` command. To remove a tag, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --remove-host-tag=TestHost`
* **Windows**  
  `.\oneagentctl.exe --remove-host-tag=TestHost`

For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

Tags configured with `--set-host-tag` are reported to Dynatrace as part of the active monitoring data stream. If host monitoring is disabled, OneAgent stops sending entity data and `[Environment]` tags eventually disappear from the **Properties and tags** section. OneAgent preserves the tag configuration locally and automatically restores tags in Dynatrace when monitoring is re-enabled.

### Other options for automated tagging

You can also set up automated tagging of the hosts in your environment using:

* [Automated rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.")
* [Environment variables](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.")
* [Smartscape and topology API](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.")

## Host metadata

To automate the addition of metadata to your hosts using OneAgent versions 1.189+, use command-line parameters. For earlier versions, use the host metadata configuration file.

### OneAgent command-line parameters for host metadata

OneAgent version 1.189+

To add or change host properties, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
  You can add or change more than one property in the same command.

When custom host metadata is used to enrich metrics and other telemetry, the keys and values might be adjusted to meet normalization requirements: keys are converted to lowercase, unsupported characters are replaced with an underscore (`_`), and keys or values that exceed the maximum length are truncated. As a result, an enriched value can differ from what you set here.

To set a security context for your host, use the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-tag=dt.security_context=easytrade_sec`
* **Windows**  
  `.\oneagentctl.exe --set-host-tag=dt.security_context=easytrade_sec`

OneAgent reserves the `dt.` prefix for host tags and properties. Aside from `dt.security_context`, `dt.cost.costcenter`, and `dt.cost.product`, OneAgent silently drops any other `dt.`-prefixed tag or property you set via these commands or the Remote Configuration Management API.

To **remove host properties**, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Edit the host metadata configuration file

OneAgent version 1.187 and earlier

The process of configuring properties is similar to the one for tags, but here they're configured through the `hostcustomproperties.conf` file, which you need to create and add to your OneAgent configuration directories.

* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
* All Unix-like systems: `/var/lib/dynatrace/oneagent/agent/config`

### Result

After you configure them, custom properties are displayed in the **Environment custom meta data** section of **Properties and tags** on the host overview page. You can then set up [automatic tagging rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.") to enable tagging of these properties.

## Custom resource attributes

To report your own [resource attributes](/managed/ingest-from/dynatrace-oneagent/resource-attributes#host-level-resource-attributes "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.") for a host, set host tags whose keys use the `primary_tags.` prefix.

* **Linux** and **AIX**
  `/opt/dynatrace/oneagent/agent/tools/oneagentctl --set-host-tag="primary_tags.environment=production"`
* **Windows**
  `"%PROGRAMFILES%\dynatrace\oneagent\agent\tools\oneagentctl.exe" --set-host-tag="primary_tags.environment=production"`

The key is stored, and matched, in full, including the prefix.

OneAgent reports these attributes for the host entity. The processes and containers running on the host don't inherit them; those get their resource attributes from the `dt_metadata` enrichment files instead.

You can then filter entities by these attributes with the [resource attributes criterion](/managed/dynatrace-api/environment-api/entity-v2/entity-selector#resourceattributes "Learn the Environment API v2 entity selector syntax for filtering monitored entities by type, name, tag, management zone, and health state.") of the Environment API v2 entity selector, and match them in [management-zone rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules#resource-attribute-conditions "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.") and in [automatically applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags#resource-attribute-conditions "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.").

Host properties set with `--set-host-property` or `hostcustomproperties.conf`, and host tags whose keys don't use the `primary_tags.` prefix, are not reported as resource attributes on the host entity. They still appear on the host overview page—tags at the top of the **Properties and tags** section, custom properties in its **Environment custom meta data** section—but you can't match them in resource-attribute rules or the entity selector.

For the full `--set-host-tag` syntax, see [Set host tags](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

The `dt.` prefix is reserved at both ends of this path. OneAgent drops any `dt.`-prefixed tag or property other than the three allowed keys when you set it, as noted under [Host metadata](#host-metadata), and Dynatrace never stores a `dt.`-prefixed key on the entity, so you can't match one in a rule or filter by it in the entity selector. Note the difference from the `dt_` prefix—with an underscore instead of a dot—which is not reserved and whose keys are the first to be kept when a host reports more resource attributes than Dynatrace stores.

The number of resource attributes Dynatrace stores per host, and their maximum key and value lengths, are limited. See [Resource attribute limits and excluded keys](/managed/ingest-from/dynatrace-oneagent/resource-attributes#ra-limits "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.").

## Related topics

* [Ownership](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.")