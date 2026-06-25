---
title: Settings API key concepts
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/key-concepts
scraped: 2026-05-12T11:38:49.757612
---

# Settings API key concepts

# Settings API key concepts

* Explanation
* Updated on Mar 26, 2026

The Settings API exposes a hierarchy of configuration objects organized by schema and scope. Before you start working with it at scale, be sure you understand how the API persists objects, how values flow through the scope hierarchy, and how the API handles concurrency, pagination, and access control.

## Overview

Schemas define settings objects; scopes determine at what level a configuration applies. Each schema specifies the shape and constraints of a configuration type. The API provides distinct read endpoints depending on whether you need explicitly persisted values or the values currently in effect.

### Schemas

**Relevant endpoints:** [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API."), [View a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.")

A schema defines the structure of a settings object: its properties, their types and constraints, and behavioral attributes such as `multiObject`, `ordered`, and `maxObjects`. Every settings object you read or write refers to a schema by its `schemaId`.

* Use [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.") to discover which schemas your environment exposes.
* Use [View a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") to inspect a specific schema's property definitions before constructing a payload. This is particularly useful for understanding required fields, enumerations, and secret-type properties.

The `schemaId` you retrieve from the schema endpoints is what you pass as the `schemaId` parameter when reading or writing objects with [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API."), and the other object endpoints.

### Persisted objects vs. effective values

The API exposes two distinct views of settings data:

* [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") returns only objects you have explicitly persisted on the queried scopes. If you haven't written anything for a given schema/scope combination, the response is empty.
* [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.") evaluates the full configuration hierarchy: it walks up the scope tree and applies schema defaults where no explicit value exists. This endpoint always returns a result for a valid schema/scope combination, even if you have never persisted an object.

Use [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") when you need to manage or audit configuration state. Use [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.") when you need the value that is actually in effect for a given scope.

### Single-value vs. multi-value schemas

Settings schemas come in two flavors, controlled by the `multiObject` property on the schema definition:

* **Single-value** (`multiObject: false`)âno more than one object exists per scope. Absence means the schema default or the value set on a parent scope is in effect.
* **Multi-value** (`multiObject: true`)âzero or more objects can coexist on the same scope, up to the limit set by `maxObjects`. When the schema's `ordered` property is `true`, item order has semantic significance; use `insertAfter` and `insertBefore` on create/update requests to control positioning.

### Scopes

Every settings object targets exactly one scope, which you set via the `scope` field on creation. The `scopes` filter on [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") matches only objects that directly target the specified scope; it does not traverse the hierarchy. For example, filtering by `environment` will not return objects scoped to a host within that environment.

### External IDs

**Relevant endpoints:** [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") (request body), [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") (`externalIds` query parameter)

The `externalId` field lets you assign a stable, caller-defined identifier to a settings object at creation time (maximum 500 characters). This enables an **upsert pattern**: if an object with the given `externalId` already exists on the target scope, the request replaces it rather than creating a duplicate. You can also look up objects by their external IDs using the `externalIds` parameter on [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.").

### Optimistic locking

**Relevant endpoints:** [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), [View an object](/managed/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API."), [Edit an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API."), [Delete an object](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.")

The `updateToken` field is a concurrency control mechanism. The API generates and returns it with every retrieval request. Including it on a subsequent update or delete means the operation only proceeds if the object hasn't changed since you last fetched it; if it has changed, the API rejects the request so you can reconcile the conflict.

Omitting `updateToken` on a write or delete bypasses this check and unconditionally applies the change.

### Pagination

**Relevant endpoints:** [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.")

All list endpoints use cursor-based pagination via `nextPageKey`. The cursor appears in the response when more pages exist; pass it as the `nextPageKey` query parameter to fetch the next page.

**Important:** when `nextPageKey` is set, all other query parameters must be omitted. Filters, schema IDs, scopes, and field projections apply only to the first-page request and encode into the cursor for subsequent pages.

### Batch writes

[Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") accepts an array of objects in a single request. The API processes each object in the batch independently and returns its own HTTP status code in the response body; check per-item codes rather than relying on the top-level response status. A partially failed batch does not roll back successful items.

### Sparse fieldsets (`fields` parameter)

The `fields` query parameter lets you limit which top-level fields are returned in a response. When provided, it replaces the default field set entirelyâit is not additive. If you specify `fields=objectId,value`, you will get only those two fields; any other fields from the default set (such as `scope` or `schemaId`) are excluded.

Responses don't include `updateToken` by default. If you need it for optimistic locking, request it explicitly: `fields=objectId,value,scope,updateToken`.

### Secret-type properties

**Relevant endpoint:** [Edit an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")

The API masks properties of type `secret` in `GET` responses. On `PUT`, you can either send the plaintext value to update a secret, or send back the masked value to keep it unchangedâunless the schema restricts this for specific non-secret properties.

Some non-secret property definitions carry a `forceSecretResubmission` field. When `forceSecretResubmission: true`, you cannot update that non-secret property while keeping secrets masked â the API requires you to provide plaintext values for all secret properties in the same schema alongside that change.

This restriction closes a potential exfiltration vector. Consider a schema that stores both a secret (for example, an API key) and a destination URL. Without `forceSecretResubmission: true` on the URL property, an attacker with write access could change only the URL to a server they control while leaving the secrets maskedâthe server would silently re-use the stored plaintext the next time it called the API, forwarding the credential to the attacker. By requiring secret resubmission when the URL changes, the schema ensures the caller already knows the secrets before they can submit a valid update.

For non-secret properties where `forceSecretResubmission` is absent or `false`, you can update them freely while sending back masked values for secret properties. To check whether a specific non-secret property carries this restriction, inspect its definition in the schema.

### Dry-run validation (`validateOnly`)

**Relevant endpoints:** [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API."), [Edit an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")

Setting `validateOnly=true` runs the full server-side validation of the submitted objects without persisting anything. Use this to verify payload correctness before committing a write, particularly when working with unfamiliar schemas.

### Owner-based access control

Some schemas enable owner-based access control (`ownerBasedAccessControl: true` in the schema definition). For objects under such schemas, the creator becomes the owner and can manage fine-grained read/write permissions per user or group via the `/settings/objects/{objectId}/permissions` sub-resource. Non-owners with write scope can still modify the object's value, but cannot modify permissions.

The `adminAccess` query parameter, available on nearly all endpoints, allows a caller with the `settings:objects:admin` permission to bypass ownership restrictions and act as the effective owner of any object.

## Use cases

* **Audit configuration state**: Use [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") to retrieve only explicitly persisted values for a given schema and scope combination.
* **Retrieve the active configuration**: Use [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.") to get the value currently in effect, including schema defaults and values inherited from parent scopes.
* **Upsert without duplicating**: Assign an `externalId` on [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") to replace an existing object rather than create a duplicate.
* **Prevent conflicting updates**: Include `updateToken` on write and delete requests to detect and reject stale changes from concurrent modifications.
* **Test before persisting**: Use `validateOnly=true` on write requests to run full server-side validation without committing any changes.
* **Apply bulk changes efficiently**: Submit multiple objects in a single [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request instead of issuing one request per object.