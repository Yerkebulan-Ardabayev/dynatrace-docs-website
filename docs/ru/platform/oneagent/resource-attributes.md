---
title: Resource attributes
source: https://www.dynatrace.com/docs/platform/oneagent/resource-attributes
scraped: 2026-02-27T21:28:49.442702
---

# Resource attributes

# Resource attributes

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jul 23, 2025

## Host-level resource attributes

All monitoring artifacts that leave a given host, that is have the host as its resource, are enriched with the host-level resource attributes.

Host-level resource attributes are resource attributes of monitored hosts. All events raised by and measurements coming from OneAgent components running on a given host are enriched with those attributes. You can then use them in your queries to structure and filter the monitoring data.

You can also use some of the attributes to create policies to manage data access. See [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") and search for fields tagged as Permission

If you have access to a host with OneAgent installed, you can inspect the `dt_host_metadata.json` and `dt_host_metadata.properties` to see the scope of resource attributes enrichment provided by OneAgent. For more information, see [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

### Custom host-level attributes

You can create your own attributes by configuring key-value tags and properties set via [oneagentctl](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or through [Remote configuration management of OneAgents and ActiveGates](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API."). Custom tags and properties defined this way are reported as flat, first-level resource attributes.

The key tags with no value are ignored.

Tags assigned through [automated rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), [environment variables](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables."), and [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.") are not included.

As the keys depend on your configuration, they aren't covered by Semantic Dictionary.

Tag names can't be prefixed with `dt.` except for the following tags that are subject to your configuration:

* `dt.security_context` - attribute to manage data access using policies. See [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").
* `dt.cost.costcenter` - attribute to assign usage to a Cost Center. See [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.").
* `dt.cost.product` - attribute to assign usage to a Product or Application ID. See [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.").

Attributes coming from custom properties and tags don't override the built-in enrichments if they have the same name. When creating your custom properties and tags, check [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") to make sure your name isn't already used.

#### Handling name clashes when merging custom properties and tags

Host-level resource attributes can be imported from host custom properties and tags. The `hostcustomproperties.conf` and `hostautotag.conf` files are the sources for these attributes. If they follow the `key=value` pattern, the same keys can exist in both files but with different values. When merged, the content from `hostautotag.conf` takes priority over the content from `hostcustomproperties.conf`, as tags take priority in case of a name clash.

If a name clash happens when merging resource attributes at different levels, the lowest level takes priority.

### General host-level attributes

All host-level resource attributes follow [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities."), unless stated otherwise.

#### AWS

#### Azure

#### Google Cloud

#### OpenStack

#### Kubernetes

#### BOSH

### Resource attributes normalization

To ensure consistent and reliable metric ingestion, resource attributes normalization is applied to all relevant internal metric keys and values. This process helps prevent metrics from being dropped due to invalid or malformed dimensions.

#### Dimension key rules

| Rule description | Details |
| --- | --- |
| **Invalid Characters** | An invalid character or a series of invalid characters is replaced with one underscore `_`. For example, `zaÃ³$%Ä` is replaced with `za_`. |
| **Empty Keys** | Dimensions with no valid characters are skipped |
| **Key Length Limit** | OneAgent version 1.317+ Max. 350 characters (previously max. 100 characters) |

#### Dimension value rules

| Rule description | Details |
| --- | --- |
| **Allowed Characters** | All non-control characters (ASCII & Unicode) |
| **Control Characters** | Not allowed. A control character (that is a character used as an instruction and is not displayed; for example, line break, tab) or a series of those characters is replaced with one underscore `_`. |
| **Value Length Limit** | OneAgent version 1.313+ Max. 2048 characters (previously max. 255 characters) |
| **Quoted Values** | If value starts and ends with `"`, it is escaped |

#### Dimension limits

To align with the current specification, a specific dimension hierarchy and defined limits are used to prevent warnings and metric drops caused by exceeding those limits.

By default, the global dimension limit is equal to `100` and the customer-defined dimension limit is 40% of the global limit.