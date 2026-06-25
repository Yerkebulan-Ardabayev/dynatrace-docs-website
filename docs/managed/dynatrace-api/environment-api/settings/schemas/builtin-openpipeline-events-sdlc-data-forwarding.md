---
title: Settings API - Data forwarding configuration (events.sdlc) schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-data-forwarding
scraped: 2026-05-12T11:39:06.792819
---

# Settings API - Data forwarding configuration (events.sdlc) schema table

# Settings API - Data forwarding configuration (events.sdlc) schema table

* Published Sep 25, 2025

### Data forwarding configuration (events.sdlc) (`builtin:openpipeline.events.sdlc.data-forwarding)`

Contains configuration of data forwarding

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:openpipeline.events.sdlc.data-forwarding` | * `group:openpipeline.all.data-forwarding` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.events.sdlc.data-forwarding` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:openpipeline.events.sdlc.data-forwarding` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.events.sdlc.data-forwarding` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Forwarding name `forwardingName` | text | - | Required |
| Pipeline Type `dataForwardingType` | enum | The element has these enums * `raw` * `processed` | Required |
| List of ingest sources `ingestSources` | set | - | Required |
| List of built-in ingest sources `builtinIngestSources` | set | - | Required |
| Pipelines `pipelines` | set | - | Required |
| Built-in pipelines `builtinPipelines` | set | - | Required |
| Query which determines whether the record should be routed to the target pipeline of this rule. `matcher` | text | - | Required |
| Cloud Vendor Type `cloudVendorType` | enum | The element has these enums * `aws` * `azure` * `gcp` | Required |
| AWS Connection `awsConnection` | [AwsConnection](#AwsConnection) | - | Required |
| Azure Connection `azureConnection` | [AzureConnection](#AzureConnection) | - | Required |
| GCP Connection `gcpConnection` | [GcpConnection](#GcpConnection) | - | Required |
| Segmentation and prefix of the data `bulkPattern` | text | - | Required |
| Bulk size for transmission `bulkSize` | integer | - | Optional |
| Processing `processing` | [Stage](#Stage) | - | Optional |

##### The `AwsConnection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| AWS connection `connectionId` | text | - | Required |
| S3 Bucket ARN `arn` | text | - | Required |

##### The `AzureConnection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Azure connection `connectionId` | text | - | Required |
| Container Connection URL `containerUrl` | text | - | Required |

##### The `GcpConnection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| GCP connection `connectionId` | text | - | Required |
| GCS Bucket Name `bucketName` | text | - | Required |

##### The `Stage` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Processors of stage `processors` | [Processor](#Processor)[] | - | Required |

##### The `Processor` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Processor identifier `id` | text | - | Required |
| Type `type` | enum | Processor type The element has these enums * `fieldsAdd` * `fieldsRemove` * `fieldsRename` * `dql` * `technology` * `drop` * `bucketAssignment` * `noStorage` * `securityContext` * `counterMetric` * `samplingAwareCounterMetric` * `valueMetric` * `histogramMetric` * `samplingAwareValueMetric` * `samplingAwareHistogramMetric` * `davis` * `bizevent` * `sdlcEvent` * `azureLogForwarding` * `securityEvent` * `costAllocation` * `productAllocation` * `smartscapeNode` * `smartscapeEdge` | Required |
| Matcher (DQL) `matcher` | text | [See our documentationï»¿](https://dt-url.net/bp234rv) | Required |
| Description `description` | text | - | Required |
| Sample data `sampleData` | text | - | Optional |
| Enabled `enabled` | boolean | - | Required |
| DQL processor attributes `dql` | [DqlAttributes](#DqlAttributes) | - | Required |
| Fields add processor attributes `fieldsAdd` | [FieldsAddAttributes](#FieldsAddAttributes) | - | Required |
| Fields rename processor attributes `fieldsRename` | [FieldsRenameAttributes](#FieldsRenameAttributes) | - | Required |
| Fields remove processor attributes `fieldsRemove` | [FieldsRemoveAttributes](#FieldsRemoveAttributes) | - | Required |
| Technology processor attributes `technology` | [TechnologyAttributes](#TechnologyAttributes) | - | Required |
| Bucket assignment processor attributes `bucketAssignment` | [BucketAssignmentAttributes](#BucketAssignmentAttributes) | - | Required |
| Security context processor attributes `securityContext` | [SecurityContextAttributes](#SecurityContextAttributes) | - | Required |
| Counter metric processor attributes `counterMetric` | [CounterMetricAttributes](#CounterMetricAttributes) | - | Required |
| Sampling-aware counter metric processor attributes `samplingAwareCounterMetric` | [SamplingAwareCounterMetricAttributes](#SamplingAwareCounterMetricAttributes) | - | Required |
| Value metric processor attributes `valueMetric` | [ValueMetricAttributes](#ValueMetricAttributes) | - | Required |
| Histogram metric processor attributes `histogramMetric` | [HistogramMetricAttributes](#HistogramMetricAttributes) | - | Required |
| Sampling aware value metric processor attributes `samplingAwareValueMetric` | [SamplingAwareValueMetricAttributes](#SamplingAwareValueMetricAttributes) | - | Required |
| Sampling aware histogram metric processor attributes `samplingAwareHistogramMetric` | [SamplingAwareHistogramMetricAttributes](#SamplingAwareHistogramMetricAttributes) | - | Required |
| Davis event extraction processor attributes `davis` | [DavisAttributes](#DavisAttributes) | - | Required |
| Bizevent extraction processor attributes `bizevent` | [BizeventAttributes](#BizeventAttributes) | - | Required |
| SdlcEvent extraction processor attributes `sdlcEvent` | [SdlcEventAttributes](#SdlcEventAttributes) | - | Required |
| Smartscape node extraction processor attributes `smartscapeNode` | [SmartscapeNodeAttributes](#SmartscapeNodeAttributes) | - | Required |
| Smartscape edge extraction processor attributes `smartscapeEdge` | [SmartscapeEdgeAttributes](#SmartscapeEdgeAttributes) | - | Required |
| Azure log forwarding processor attributes `azureLogForwarding` | [AzureLogForwardingAttributes](#AzureLogForwardingAttributes) | - | Required |
| Security event extraction processor attributes `securityEvent` | [SecurityEventAttributes](#SecurityEventAttributes) | - | Required |
| Cost allocation processor attributes `costAllocation` | [CostAllocationAttributes](#CostAllocationAttributes) | - | Required |
| Product allocation processor attributes `productAllocation` | [ProductAllocationAttributes](#ProductAllocationAttributes) | - | Required |

##### The `DqlAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| DQL script `script` | text | - | Required |

##### The `FieldsAddAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fields to Add `fields` | [FieldsAddAttributesEntry](#FieldsAddAttributesEntry)[] | - | Required |

##### The `FieldsRenameAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fields to rename `fields` | [FieldsRenameAttributesEntry](#FieldsRenameAttributesEntry)[] | - | Required |

##### The `FieldsRemoveAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fields to remove `fields` | set | - | Required |

##### The `TechnologyAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Custom matcher `customMatcher` | text | Custom matching condition which should be used instead of technology matcher. | Optional |
| Technology ID `technologyId` | text | - | Required |

##### The `BucketAssignmentAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Bucket name `bucketName` | text | - | Required |

##### The `SecurityContextAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Security context value assignment `value` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |

##### The `CounterMetricAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metric key `metricKey` | text | - | Required |
| List of dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |

##### The `SamplingAwareCounterMetricAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metric key `metricKey` | text | - | Required |
| List of dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Sampling `sampling` | enum | The element has these enums * `disabled` * `enabled` | Optional |
| Aggregation `aggregation` | enum | The element has these enums * `disabled` * `enabled` | Optional |

##### The `ValueMetricAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metric key `metricKey` | text | - | Required |
| Field with metric value `field` | text | - | Required |
| Default value with metric value `defaultValue` | text | - | Optional |
| List of dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |

##### The `HistogramMetricAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metric key `metricKey` | text | - | Required |
| Field with metric value `field` | text | - | Required |
| Default value with metric value `defaultValue` | text | - | Optional |
| List of dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |

##### The `SamplingAwareValueMetricAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metric key `metricKey` | text | - | Required |
| Field with metric value `field` | text | - | Required |
| Default value with metric value `defaultValue` | text | - | Optional |
| List of dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Sampling `sampling` | enum | The element has these enums * `disabled` * `enabled` | Optional |
| Aggregation `aggregation` | enum | The element has these enums * `disabled` * `enabled` | Optional |
| Measurement `measurement` | enum | The element has these enums * `field` * `duration` | Required |

##### The `SamplingAwareHistogramMetricAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metric key `metricKey` | text | - | Required |
| Field with metric value `field` | text | - | Required |
| Default value with metric value `defaultValue` | text | - | Optional |
| List of dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Sampling `sampling` | enum | The element has these enums * `disabled` * `enabled` | Optional |
| Aggregation `aggregation` | enum | The element has these enums * `disabled` * `enabled` | Optional |
| Measurement `measurement` | enum | The element has these enums * `field` * `duration` | Required |

##### The `DavisAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Properties `properties` | [DavisEventProperty](#DavisEventProperty)[] | - | Required |

##### The `BizeventAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Event type `eventType` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Event provider `eventProvider` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Field extraction `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### The `SdlcEventAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Event type `eventType` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Event provider `eventProvider` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Event category `eventCategory` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Event status `eventStatus` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Field extraction `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### The `SmartscapeNodeAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Node type `nodeType` | text | - | Required |
| Node ID field name `nodeIdFieldName` | text | - | Required |
| ID components `idComponents` | [SmartscapeIdComponentsEntry](#SmartscapeIdComponentsEntry)[] | - | Required |
| Extract node `extractNode` | boolean | - | Required |
| Node name `nodeName` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Fields to extract `fieldsToExtract` | [SmartscapeFieldExtractionEntry](#SmartscapeFieldExtractionEntry)[] | - | Required |
| Static edges to extract `staticEdgesToExtract` | [SmartscapeStaticEdgeExtractionEntry](#SmartscapeStaticEdgeExtractionEntry)[] | - | Required |

##### The `SmartscapeEdgeAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Source type `sourceType` | text | - | Required |
| Source ID field name `sourceIdFieldName` | text | - | Required |
| Edge type `edgeType` | text | - | Required |
| Target type `targetType` | text | - | Required |
| Target ID field name `targetIdFieldName` | text | - | Required |

##### The `AzureLogForwardingAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ForwarderConfigId `forwarderConfigId` | text | - | Required |
| Field Extraction `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### The `SecurityEventAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Field Extraction `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### The `CostAllocationAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| The strategy to set the cost allocation field `value` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |

##### The `ProductAllocationAttributes` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| The strategy to set product allocation field `value` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |

##### The `FieldsAddAttributesEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fields's name `name` | text | - | Required |
| Field's value `value` | text | - | Required |

##### The `FieldsRenameAttributesEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fields's name `fromName` | text | - | Required |
| New field's name `toName` | text | - | Required |

##### The `GenericValueAssignment` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type of value assignment `type` | enum | The element has these enums * `constant` * `multiValueConstant` * `field` | Required |
| Constant value `constant` | text | - | Required |
| Constant multi value `multiValueConstant` | list | - | Required |
| Value from field `field` | [ValueAssignmentFromFieldEntry](#ValueAssignmentFromFieldEntry) | - | Required |

##### The `FieldExtractionEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Strategy for field extraction `strategy` | enum | The element has these enums * `equals` * `startsWith` | Optional |
| Field value extraction type `extractionType` | enum | The element has these enums * `constant` * `field` | Required |
| Source field name `sourceFieldName` | text | - | Required |
| Destination field name `destinationFieldName` | text | - | Optional |
| Default value `defaultValue` | text | - | Optional |
| Destination field name `constantFieldName` | text | - | Required |
| Constant value to be assigned to field `constantValue` | text | - | Required |

##### The `DavisEventProperty` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Strategy for field extraction `strategy` | enum | The element has these enums * `equals` * `startsWith` | Optional |
| Key `key` | text | - | Required |
| Value `value` | text | - | Required |

##### The `FieldExtraction` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Fields Extraction type `type` | enum | The element has these enums * `include` * `exclude` * `includeAll` | Required |
| Fields `include` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Fields `exclude` | set | - | Required |

##### The `SmartscapeIdComponentsEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ID component `idComponent` | text | - | Required |
| Referenced field name `referencedFieldName` | text | - | Required |

##### The `SmartscapeFieldExtractionEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Strategy for field extraction `strategy` | enum | The element has these enums * `equals` * `startsWith` | Optional |
| Field name `fieldName` | text | - | Required |
| Referenced field name `referencedFieldName` | text | - | Required |

##### The `SmartscapeStaticEdgeExtractionEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Edge type `edgeType` | text | - | Required |
| Target type `targetType` | text | - | Required |
| Target ID field name `targetIdFieldName` | text | - | Required |

##### The `ValueAssignmentFromFieldEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Source field name `sourceFieldName` | text | - | Required |
| Default value `defaultValue` | text | - | Optional |