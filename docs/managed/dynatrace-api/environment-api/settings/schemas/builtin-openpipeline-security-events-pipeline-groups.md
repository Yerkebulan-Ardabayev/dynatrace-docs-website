---
title: Settings API - Pipeline Groups configuration (security.events) schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-pipeline-groups
---

# Settings API - Pipeline Groups configuration (security.events) schema table

# Settings API - Pipeline Groups configuration (security.events) schema table

* Published Sep 25, 2025

### Pipeline Groups configuration (security.events) (`builtin:openpipeline.security.events.pipeline-groups)`

Contains configuration of a pipeline group

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:openpipeline.security.events.pipeline-groups` | * `group:openpipeline.all.pipeline-groups` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.security.events.pipeline-groups` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:openpipeline.security.events.pipeline-groups` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.security.events.pipeline-groups` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Display name `displayName` | text | - | Required |
| Pipelines wrapped by this group `memberPipelines` | set | - | Required |
| stage configuration of the member pipelines `memberStages` | [StageConfig](#StageConfig) | - | Required |
| Composition `composition` | [PipelineGroupComposition](#PipelineGroupComposition)[] | - | Required |

##### The `StageConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Stage configuration type `type` | enum | The element has these enums * `include` * `exclude` * `includeAll` | Required |
| include stages `include` | Set<[StageType](#StageType)> | The element has these enums * `processing` * `securityContext` * `costAllocation` * `productAllocation` * `storage` * `smartscapeNodeExtraction` * `smartscapeEdgeExtraction` * `metricExtraction` * `davis` * `dataExtraction` | Required |
| exclude stages `exclude` | Set<[StageType](#StageType)> | The element has these enums * `processing` * `securityContext` * `costAllocation` * `productAllocation` * `storage` * `smartscapeNodeExtraction` * `smartscapeEdgeExtraction` * `metricExtraction` * `davis` * `dataExtraction` | Required |

##### The `PipelineGroupComposition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Placeholder for the wrapped pipeline `isPipelinePlaceholder` | boolean | - | Required |
| Pipeline ID `pipelineId` | setting | - | Required |
| stage configuration for this pipelines `stages` | [StageConfig](#StageConfig) | - | Required |