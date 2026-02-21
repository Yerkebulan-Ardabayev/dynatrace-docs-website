---
title: Settings API - GET a schema
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/get-schema
scraped: 2026-02-21T21:10:44.345339
---

# Settings API - GET a schema

# Settings API - GET a schema

* Reference
* Published Feb 24, 2021

Gets parameters of the specified settings schema.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/{schemaId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/schemas/{schemaId}` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| schemaId | string | The ID of the required schema. | path | Required |
| schemaVersion | string | The version of the required schema.  If not set, the most recent version is returned. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SchemaDefinitionRestDto](#openapi-definition-SchemaDefinitionRestDto) | Success |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Forbidden. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The specified schema doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SchemaDefinitionRestDto` object

| Element | Type | Description |
| --- | --- | --- |
| allowedScopes | string[] | A list of scopes where the schema can be used. |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | A list of constrains limiting the values to be accepted by the schema. |
| deletionConstraints | [DeletionConstraint[]](#openapi-definition-DeletionConstraint) | Constraints limiting the values to be deleted. |
| description | string | A short description of the schema. |
| displayName | string | The display name of the schema. |
| documentation | string | An extended description of the schema and/or links to documentation. |
| dynatrace | string | The version of the data format. |
| enums | object | A list of definitions of enum properties. |
| keyProperty | string | Name of the key property in this schema. |
| maturity | string | The maturity of the schema. Possible values:  * PREVIEW: Preview features are not generally available, but might be available in specific environments as part of early-access programs. These are the most likely to change in incompatible ways. * EARLY\_ADOPTER: Features marked "early adopter" are available in all environments, but are not mature enough to warrant the "general availability" designation. We don't expect incompatible changes for these, but please be aware, that these are not fully stable yet and incompatible changes may be necessary in rare cases. * GENERAL\_AVAILABILITY: Features marked "general availability" are the most stable. While the schemas will still evolve over time, care will be taken to only do so in a backward-compatible manner.  In any case, automations should make use of the `schemaVersion` field when writing settings objects. The element can hold these values * `EARLY_ADOPTER` * `GENERAL_AVAILABILITY` * `PREVIEW` |
| maxObjects | integer | The maximum amount of objects per scope.  Only applicable when **multiObject** is set to `true`. |
| metadata | object | Metadata of the setting. |
| multiObject | boolean | Multiple (`true`) objects per scope are permitted or a single (`false`) object per scope is permitted. |
| ordered | boolean | If `true` the order of objects has semantic significance.  Only applicable when **multiObject** is set to `true`. |
| properties | object | A list of schema's properties. |
| schemaConstraints | [SchemaConstraintRestDto[]](#openapi-definition-SchemaConstraintRestDto) | Constraints limiting the values as a whole to be accepted in this configuration element. |
| schemaGroups | string[] | Names of the groups, which the schema belongs to. |
| schemaId | string | The ID of the schema. |
| tableColumns | object | Table column definitions for use in the ui. |
| types | object | A list of definitions of types.  A type is a complex property that contains its own set of subproperties. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Customization for UI elements |
| version | string | The version of the schema. |

#### The `ComplexConstraint` object

A constraint on the values accepted for a complex settings property.

| Element | Type | Description |
| --- | --- | --- |
| checkAllProperties | boolean | Defines if modification of any property triggers secret resubmission check. |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| maximumPropertyCount | integer | The maximum number of properties that can be set. |
| minimumPropertyCount | integer | The minimum number of properties that must be set. |
| properties | string[] | A list of properties (defined by IDs) that are used to check the constraint. |
| skipAsyncValidation | boolean | Whether to skip validation on a change made from the UI. |
| timeout | integer | The maximum time in seconds the custom validator is allowed to run. |
| type | string | The type of the constraint. The element can hold these values * `CUSTOM_VALIDATOR_REF` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LESS_THAN` * `LESS_THAN_OR_EQUAL` * `PROPERTY_COUNT_RANGE` * `SECRET_RESUBMISSION` * `UNKNOWN` |

#### The `DeletionConstraint` object

A constraint on the values that are going to be deleted.

| Element | Type | Description |
| --- | --- | --- |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| schemaIds | string[] | The IDs of schemas that should be checked for references to this schema. |
| timeout | integer | The maximum time in seconds the custom validator is allowed to run. |
| type | string | The type of the deletion constraint. The element can hold these values * `CUSTOM_VALIDATOR_REF` * `REFERENTIAL_INTEGRITY` * `UNKNOWN` |

#### The `EnumType` object

Definition of an enum property.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the property. |
| displayName | string | The display name of the property. |
| documentation | string | An extended description and/or links to documentation. |
| enumClass | string | An existing Java enum class that holds the allowed values of the enum. |
| items | [EnumValue[]](#openapi-definition-EnumValue) | A list of allowed values of the enum. |
| type | string | The type of the property. The element can hold these values * `enum` |

#### The `EnumValue` object

An allowed value for an enum property.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the value. |
| displayName | string | The display name of the value. |
| enumInstance | string | The name of the value in an existing Java enum class. |
| icon | string | The icon of the value. |
| value | string | The allowed value of the enum. |

#### The `AnyValue` object

A schema representing an arbitrary value type.

#### The `PropertyDefinition` object

Configuration of a property in a settings schema.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | A list of constraints limiting the values to be accepted. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Configuration of a datasource for a property. |
| default | string | The default value to be used when no value is provided.  If a non-singleton has the value of `null`, it means an empty collection. |
| description | string | A short description of the property. |
| displayName | string | The display name of the property. |
| documentation | string | An extended description and/or links to documentation. |
| forceSecretResubmission | boolean | Defines if value is allowed to be modified when secret properties are not |
| items | [Item](#openapi-definition-Item) | An item of a collection property. |
| maxObjects | integer | The maximum number of **objects** in a collection property.  Has the value of `1` for singletons. |
| metadata | object | Metadata of the property. |
| migrationPattern | string | Pattern with references to properties to create a new value. |
| minObjects | integer | The minimum number of **objects** in a collection property. |
| modificationPolicy | string | Modification policy of the property. The element can hold these values * `ALWAYS` * `DEFAULT` * `NEVER` |
| nullable | boolean | The value can (`true`) or can't (`false`) be `null`. |
| precondition | [Precondition](#openapi-definition-Precondition) | A precondition for visibility of a property. |
| referencedType | string | The type referenced by the property value |
| subType | string | The subtype of the property's value. |
| type | string | The type of the property's value. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Customization for UI elements |

#### The `Constraint` object

A constraint on the values accepted for a settings property.

| Element | Type | Description |
| --- | --- | --- |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| disallowDangerousRegex | boolean | Whether to disallow usage of dangerous regexes |
| maxLength | integer | The maximum allowed length of string values. |
| maximum | number | The maximum allowed value. |
| minLength | integer | The minimum required length of string values. |
| minimum | number | The minimum allowed value. |
| pattern | string | The regular expression pattern for valid string values. |
| skipAsyncValidation | boolean | Whether to skip validation on a change made from the UI. |
| timeout | integer | The maximum time in seconds the custom validator is allowed to run. |
| type | string | The type of the constraint. The element can hold these values * `CUSTOM_VALIDATOR_REF` * `LENGTH` * `NOT_BLANK` * `NOT_EMPTY` * `NO_WHITESPACE` * `PATTERN` * `RANGE` * `REGEX` * `TRIMMED` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | A list of properties for which the combination of values must be unique. |

#### The `DatasourceDefinition` object

Configuration of a datasource for a property.

| Element | Type | Description |
| --- | --- | --- |
| filterProperties | string[] | The properties to filter the datasource options on. |
| fullContext | boolean | Whether this datasource expects full setting payload as the context. |
| identifier | string | The identifier of a custom data source of the property's value. |
| resetValue | string | When to reset datasource value in the UI on filter change. The element can hold these values * `ALWAYS` * `INVALID_ONLY` * `NEVER` |
| useApiSearch | boolean | If true, the datasource should use the api to filter the results instead of client-side filtering. |
| validate | boolean | Whether to validate input to only allow values returned by the datasource. |

#### The `Item` object

An item of a collection property.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [Constraint[]](#openapi-definition-Constraint) | A list of constraints limiting the values to be accepted. |
| datasource | [DatasourceDefinition](#openapi-definition-DatasourceDefinition) | Configuration of a datasource for a property. |
| description | string | A short description of the item. |
| displayName | string | The display name of the item. |
| documentation | string | An extended description and/or links to documentation. |
| metadata | object | Metadata of the items. |
| referencedType | string | The type referenced by the item's value. |
| subType | string | The subtype of the item's value. |
| type | string | The type of the item's value. |
| uiCustomization | [UiCustomization](#openapi-definition-UiCustomization) | Customization for UI elements |

#### The `UiCustomization` object

Customization for UI elements

| Element | Type | Description |
| --- | --- | --- |
| callback | [UiCallbackCustomization](#openapi-definition-UiCallbackCustomization) | UI customization options for defining custom callbacks |
| expandable | [UiExpandableCustomization](#openapi-definition-UiExpandableCustomization) | UI customization for expandable section |
| table | [UiTableCustomization](#openapi-definition-UiTableCustomization) | Customization for UI tables |
| tabs | [UiTabsCustomization](#openapi-definition-UiTabsCustomization) | UI customization for tabs |

#### The `UiCallbackCustomization` object

UI customization options for defining custom callbacks

| Element | Type | Description |
| --- | --- | --- |
| buttons | [UiButtonCustomization[]](#openapi-definition-UiButtonCustomization) | UI customization for defining buttons that call functions when pressed |

#### The `UiButtonCustomization` object

UI customization for defining a button that calls a function when pressed

| Element | Type | Description |
| --- | --- | --- |
| description | string | The description to be shown in a tooltip when hovering over the button |
| displayName | string | The label of the button |
| identifier | string | The identifier of the function to be called when the button is pressed |
| insert | string | The position where the button should be shown in the UI The element can hold these values * `FIRST` * `LAST` |

#### The `UiExpandableCustomization` object

UI customization for expandable section

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name |
| expanded | boolean | Defines if the item should be expanded by default |
| sections | [UiExpandableSectionCustomization[]](#openapi-definition-UiExpandableSectionCustomization) | A list of sections |

#### The `UiExpandableSectionCustomization` object

Expandable section customization for UI

| Element | Type | Description |
| --- | --- | --- |
| description | string | The description |
| displayName | string | The display name |
| expanded | boolean | Defines if the section should be expanded by default |
| properties | string[] | A list of properties |

#### The `UiTableCustomization` object

Customization for UI tables

| Element | Type | Description |
| --- | --- | --- |
| columns | [UiTableColumnCustomization[]](#openapi-definition-UiTableColumnCustomization) | A list of columns for the UI table |
| emptyState | [UiEmptyStateCustomization](#openapi-definition-UiEmptyStateCustomization) | UI customization for empty state in a table |

#### The `UiTableColumnCustomization` object

Customization for UI table columns

| Element | Type | Description |
| --- | --- | --- |
| builtinColumnRef | string | The ui specific builtin column-implementation for this column. |
| columnRef | string | The referenced column from the 'tableColumns' property of the schema for this column. |
| displayName | string | The display name for this column. |
| id | string | The id for this column used for filtering. Required for conflicting or pathed columns - otherwise the ref is used. |
| items | [UiTableColumnItemCustomization[]](#openapi-definition-UiTableColumnItemCustomization) | The possible items of this column. |
| propertyRef | string | The referenced property for this column. |
| type | string | The ui specific type for this column. |
| width | string | The width this column should take up on the table. |

#### The `UiTableColumnItemCustomization` object

Customization for UI table column items

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of this item. |
| icon | string | The icon of this item. |
| value | string | The value of this item. |

#### The `UiEmptyStateCustomization` object

UI customization for empty state in a table

| Element | Type | Description |
| --- | --- | --- |
| text | string | The text to be shown in the empty state |

#### The `UiTabsCustomization` object

UI customization for tabs

| Element | Type | Description |
| --- | --- | --- |
| groups | [UiTabGroupCustomization[]](#openapi-definition-UiTabGroupCustomization) | A list of groups |

#### The `UiTabGroupCustomization` object

Tab group customization for UI

| Element | Type | Description |
| --- | --- | --- |
| description | string | The description |
| displayName | string | The display name |
| properties | string[] | A list of properties |

#### The `Precondition` object

A precondition for visibility of a property.

| Element | Type | Description |
| --- | --- | --- |
| expectedValue | string | The expected value of the property.  Only applicable to properties of the `EQUALS` type. |
| expectedValues | - | A list of valid values of the property.  Only applicable to properties of the `IN` type. |
| pattern | string | The Regular expression which is matched against the property.  Only applicable to properties of the `REGEX_MATCH` type. |
| precondition | [Precondition](#openapi-definition-Precondition) | A precondition for visibility of a property. |
| preconditions | [Precondition[]](#openapi-definition-Precondition) | A list of child preconditions to be evaluated.  Only applicable to properties of the `AND` and `OR` types. |
| property | string | The property to be evaluated. |
| type | string | The type of the precondition. The element can hold these values * `AND` * `EQUALS` * `IN` * `NOT` * `NULL` * `OR` * `REGEX_MATCH` |

#### The `SchemaConstraintRestDto` object

| Element | Type | Description |
| --- | --- | --- |
| byteLimit | integer | The maximum allowed size in bytes for the sum over all persisted values for the schema |
| customMessage | string | A custom message for invalid values. |
| customValidatorId | string | The ID of a custom validator. |
| flattenCollections | boolean | Whether to flatten collection properties when checking for uniqueness, so only disjoint collections are considered unique |
| skipAsyncValidation | boolean | Whether to skip validation on a change made from the UI. |
| type | string | The type of the schema constraint. The element can hold these values * `BYTE_SIZE_LIMIT` * `CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_CUSTOM_VALIDATOR_REF` * `MULTI_SCOPE_UNIQUE` * `UNIQUE` * `UNKNOWN` |
| uniqueProperties | string[] | The list of properties for which the combination of values needs to be unique |

#### The `TableColumn` object

The definition of a table column to be used in the ui.

| Element | Type | Description |
| --- | --- | --- |
| pattern | string | Pattern with references to properties to create a single value for the column. |

#### The `SchemaType` object

A list of definitions of types.

A type is a complex property that contains its own set of subproperties.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [ComplexConstraint[]](#openapi-definition-ComplexConstraint) | A list of constraints limiting the values to be accepted. |
| description | string | A short description of the property. |
| displayName | string | The display name of the property. |
| documentation | string | An extended description and/or links to documentation. |
| properties | object | Definition of properties that can be persisted. |
| searchPattern | string | The pattern for the summary search(for example, "Alert after *X* minutes.") of the configuration in the UI. |
| summaryPattern | string | The pattern for the summary (for example, "Alert after *X* minutes.") of the configuration in the UI. |
| type | string | Type of the reference type. The element can hold these values * `object` |
| version | string | The version of the type. |
| versionInfo | string | A short description of the version. |

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



"allowedScopes": [



"host",



"application"



],



"constraints": [



{



"checkAllProperties": false,



"customMessage": "string",



"customValidatorId": "my-min-max",



"maximumPropertyCount": 2,



"minimumPropertyCount": 1,



"properties": [



"string"



],



"skipAsyncValidation": false,



"timeout": 5,



"type": "CUSTOM_VALIDATOR_REF"



}



],



"deletionConstraints": [



{



"customMessage": "string",



"customValidatorId": "my-min-max",



"schemaIds": [



"my-schema-id"



],



"timeout": 5,



"type": "CUSTOM_VALIDATOR_REF"



}



],



"description": "Dynatrace disables monitoring of containers that do not run any applications",



"displayName": "Built-in container monitoring rules",



"documentation": "string",



"dynatrace": "1",



"enums": {},



"keyProperty": "keyProperty",



"maturity": "GENERAL_AVAILABILITY",



"maxObjects": 10,



"metadata": {},



"multiObject": true,



"ordered": true,



"properties": {},



"schemaConstraints": [



{



"byteLimit": 500000,



"customMessage": "string",



"customValidatorId": "my-min-max",



"flattenCollections": true,



"skipAsyncValidation": false,



"type": "BYTE_SIZE_LIMIT",



"uniqueProperties": [



"my-prop-1",



"my-prop-2"



]



}



],



"schemaGroups": [



"group:some.1",



"group:some.2"



],



"schemaId": "builtin:container.built-in-monitoring-rule",



"tableColumns": {},



"types": {},



"uiCustomization": {



"callback": {



"buttons": [



{



"description": "string",



"displayName": "string",



"identifier": "string",



"insert": "FIRST"



}



]



},



"expandable": {



"displayName": "string",



"expanded": true,



"sections": [



{



"description": "string",



"displayName": "string",



"expanded": true,



"properties": [



"string"



]



}



]



},



"table": {



"columns": [



{



"builtinColumnRef": "summary",



"columnRef": "myCustomColumn",



"displayName": "Color",



"id": "color",



"items": [



{



"displayName": "Active",



"icon": "CRITICAL",



"value": "ACTIVE"



}



],



"propertyRef": "apiColor",



"type": "cell-color-picker",



"width": "10%"



}



],



"emptyState": {



"text": "string"



}



},



"tabs": {



"groups": [



{



"description": "string",



"displayName": "string",



"properties": [



"string"



]



}



]



}



},



"version": "1.4.2"



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