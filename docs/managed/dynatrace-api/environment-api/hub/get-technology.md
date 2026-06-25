---
title: Hub capabilities API - GET a technology
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-technology
scraped: 2026-05-12T11:54:59.277395
---

# Hub capabilities API - GET a technology

# Hub capabilities API - GET a technology

* Reference
* Published Feb 07, 2023

Gets the information for the specified technology.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/technologies/{slug}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/technologies/{slug}` |

## Authentication

To execute this request, you need an access token with `hub.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| slug | string | Slug of the technology to be fetched | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ItemDetails](#openapi-definition-ItemDetails) | OK |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ItemDetails` object

Public metadata for an item.

| Element | Type | Description |
| --- | --- | --- |
| authorLogo | string | Url for the author's logo. |
| authorName | string | Name of the author of the item. |
| clusterCompatible | boolean | Checks if the item is compatible with the cluster version. |
| clusterMaxVersion | integer | The maximum supported cluster version for this item. |
| clusterMinVersion | integer | The minimum cluster version required to use this item. |
| description | string | Description of the item. |
| descriptionBlocks | [DescriptionBlock[]](#openapi-definition-DescriptionBlock) | - |
| documentationLink | string | An absolute link to a documentation page explaining the item. |
| extension1Details | [Extension1Details](#openapi-definition-Extension1Details) | Additional details of the extension version 1. |
| extension2Details | [Extension2Details](#openapi-definition-Extension2Details) | Additional details of the extension. |
| itemId | string | Unique Id of the item. |
| logo | string | The logo of the item. Can be a URL or Base64 encoded. Intended for html tags. |
| marketingLink | string | An absolute link to a marketing page promoting how the item can be used with dynatrace. |
| name | string | Name of the item. |
| notCompatibleReason | string | The reason why the item is not compatible with the cluster version. |
| relatedItems | [RelatedItem[]](#openapi-definition-RelatedItem) | Related items. |
| tags | string[] | Grouping of items with keywords. |
| technologyDetails | [TechnologyDetails](#openapi-definition-TechnologyDetails) | Additional details of the technology. |
| type | string | Represents the type of item. It can be TECHNOLOGY, EXTENSION1 or EXTENSION2. The element can hold these values * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` |

#### The `DescriptionBlock` object

Represents a section of data describing the given capability.

| Element | Type | Description |
| --- | --- | --- |
| images | [Image[]](#openapi-definition-Image) | Collection of images (in case of gallery). |
| source | string | Source of the description block (in case of markdown). |
| sourceId | string | Optional identifier of special description blocks. |
| title | string | Title of the description block. |
| type | string | Type of the data, either markdown or gallery. The element can hold these values * `GALLERY` * `MARKDOWN` |

#### The `Image` object

Information about the image details of a capability.

| Element | Type | Description |
| --- | --- | --- |
| alt | string | Alternate text for the image. |
| src | string | Url of the image. |
| title | string | Title of the image. |

#### The `Extension1Details` object

Additional details of the extension version 1.

| Element | Type | Description |
| --- | --- | --- |
| releases | [Extension1Release[]](#openapi-definition-Extension1Release) | A list of versions for the extension version 1. |

#### The `Extension1Release` object

Extension version 1 release details.

| Element | Type | Description |
| --- | --- | --- |
| artifactSha256 | string | SHA-256 hash of the extension version 1. |
| artifactTitle | string | The title of the extension version 1. |
| releaseNotes | string | The associated release notes. |
| version | string | The version number of the extension version 1 release. |

#### The `Extension2Details` object

Additional details of the extension.

| Element | Type | Description |
| --- | --- | --- |
| distributed | boolean | Whether this extension is available in the central hub catalog. |
| extensionName | string | Fully qualified name of the extension. |
| recommendedCatalogVersion | string | Recommended version of this extension to use. This is the latest compatible published release. |
| releases | [ExtensionRelease[]](#openapi-definition-ExtensionRelease) | Releases for the extension. |

#### The `ExtensionRelease` object

Extensions releases information

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | Represents whether this version is active version |
| artifactSha256 | string | Sha256 hash for the distributed extension. |
| assetsInfo | [AssetInfo[]](#openapi-definition-AssetInfo) | Assets types and its count |
| configuredFeatureSets | string[] | Configured feature sets for an installed release |
| dataSources | string[] | Available data sources for the given release |
| distributed | boolean | Represents whether the release is distributed |
| featureSets | object | Feature sets contained in the given release |
| minClusterVersion | integer | Minimum cluster version for the release |
| registered | boolean | Represents whether extension is already registered |
| releaseNotes | string | Release notes for the extension. |
| unpublished | boolean | Represents whether the extension is unpublished. |
| unpublishedDescription | string | The description why the extension was unpublished. |
| unpublishedSeverity | integer | The severity of unpublished extension. 5 indicates an error state |
| version | string | Version number of the extension. |

#### The `AssetInfo` object

Assets types and its count

| Element | Type | Description |
| --- | --- | --- |
| assetType | string | - |
| count | integer | - |

#### The `FeatureSetDetails` object

Additional information about a Feature Set

| Element | Type | Description |
| --- | --- | --- |
| description | string | Optional description for the feature set |
| displayName | string | Optional display name of the feature set |
| isRecommended | boolean | Marks the feature set as recommended (selected by default during activation) |
| metrics | [MetricDto[]](#openapi-definition-MetricDto) | Feature set metrics |

#### The `MetricDto` object

Metric gathered by an extension

| Element | Type | Description |
| --- | --- | --- |
| key | string | Metric key |
| metadata | [MetricMetadataDto](#openapi-definition-MetricMetadataDto) | Metric metadata |

#### The `MetricMetadataDto` object

Metric metadata

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the metric |
| displayName | string | The name of the metric in the user interface |
| unit | string | The unit of the metric |

#### The `RelatedItem` object

Related items.

| Element | Type | Description |
| --- | --- | --- |
| description | string | - |
| externalLink | string | External link (marketing/documentation) that can provide with additional information. |
| hasClusterLink | boolean | Indicates whether there is a page within the product to activate this item. |
| iconUrl | string | The logo of the item. Can be a URL or Base64 encoded. Intended for html tags |
| id | string | - |
| name | string | - |
| type | string | Represents the type of item. It can be TECHNOLOGY, EXTENSION1 or EXTENSION2. The element can hold these values * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` |

#### The `TechnologyDetails` object

Additional details of the technology.

| Element | Type | Description |
| --- | --- | --- |
| activationLink | string | Represents the installation/public navigation link for the technology. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"authorLogo": "string",



"authorName": "string",



"clusterCompatible": true,



"clusterMaxVersion": 1,



"clusterMinVersion": 1,



"description": "string",



"descriptionBlocks": [



{



"images": [



{



"alt": "string",



"src": "string",



"title": "string"



}



],



"source": "string",



"sourceId": "string",



"title": "string",



"type": "GALLERY"



}



],



"documentationLink": "string",



"extension1Details": {



"releases": [



{



"artifactSha256": "string",



"artifactTitle": "string",



"releaseNotes": "string",



"version": "string"



}



]



},



"extension2Details": {



"distributed": true,



"extensionName": "string",



"recommendedCatalogVersion": "string",



"releases": [



{



"active": true,



"artifactSha256": "string",



"assetsInfo": [



{



"assetType": "string",



"count": 1



}



],



"configuredFeatureSets": [



"string"



],



"dataSources": [



"string"



],



"distributed": true,



"featureSets": {},



"minClusterVersion": 1,



"registered": true,



"releaseNotes": "string",



"unpublished": true,



"unpublishedDescription": "string",



"unpublishedSeverity": 1,



"version": "string"



}



]



},



"itemId": "string",



"logo": "string",



"marketingLink": "string",



"name": "string",



"notCompatibleReason": "string",



"relatedItems": [



{



"description": "string",



"externalLink": "string",



"hasClusterLink": true,



"iconUrl": "string",



"id": "string",



"name": "string",



"type": "EXTENSION1"



}



],



"tags": [



"string"



],



"technologyDetails": {



"activationLink": "string"



},



"type": "EXTENSION1"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```