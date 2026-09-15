---
title: Network zones - Settings API
source: https://docs.dynatrace.com/managed/manage/network-zones/manage-via-settings-api
---

# Network zones - Settings API

# Network zones - Settings API

* How-to guide
* 2-min read
* Published Jul 16, 2026

You can manage network zones programmatically using the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [`builtin:networkzones.zones`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-networkzones-zones "View builtin:networkzones.zones settings schema table of your monitoring environment via the Dynatrace API.") schema. This page covers the network-zone-specific details. For general Settings API behavior—pagination, filtering, and error responses—see the [Settings API reference](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

## Authentication

All requests require an API token. To learn how to obtain and use it, see [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

The required token permission depends on the operation:

* **Read settings** (`settings.read`)—required for listing all network zones and retrieving a single network zone
* **Write settings** (`settings.write`)—required for creating, updating, and deleting network zones

## Operations

All operations use the `/api/v2/settings/objects` endpoint. Prepend the base URL for your deployment to the path shown in the table below:

* Managed - Environment `https://{your-environment-id}.live.dynatrace.com`
* Managed - Cluster `https://{your-activegate-domain}:9999/e/{your-environment-id}`

| Operation | Method | Path | Required scope |
| --- | --- | --- | --- |
| [List all network zones](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") | `GET` | `/api/v2/settings/objects?schemaIds=builtin:networkzones.zones` | `settings.read` |
| [Get a single network zone](/managed/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.") | `GET` | `/api/v2/settings/objects/{object-id}` | `settings.read` |
| [Create a network zone](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") | `POST` | `/api/v2/settings/objects` | `settings.write` |
| [Update a network zone](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") | `PUT` | `/api/v2/settings/objects/{object-id}` | `settings.write` |
| [Delete a network zone](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") | `DELETE` | `/api/v2/settings/objects/{object-id}` | `settings.write` |

## Network zone fields

The create and update operations accept a `value` object in the request body. Its properties are described below.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Unique identifier of the network zone. Alphanumeric characters, hyphens (`-`), and underscores (`_`) only. Maximum 256 characters. Cannot be changed after creation. |
| `description` | string | No | Human-readable description of the network zone. |
| `alternativeZones` | array of strings | Yes | List of alternative network zone IDs to use when no ActiveGate in this zone is available. Can be empty. See [Alternative network zone](/managed/manage/network-zones/network-zones-basic-info#alternative "Learn how to get started with network zones."). |
| `fallbackMode` | string | Yes | Routing behavior when no ActiveGate is available in this zone or its alternatives. See [Fallback mode](/managed/manage/network-zones/network-zones-basic-info#fallback-mode "Learn how to get started with network zones.") for a description of each option. Valid values: `ANY_ACTIVE_GATE` (default), `ONLY_DEFAULT_ZONE`, `NONE`. |

## Examples

### Get a single network zone

```
GET /api/v2/settings/objects/{object-id}
```

Response; not all properties are shown in this example:

```
{



"objectId": "<objectId>",



"created": 1782827712752,



"modified": 1782887796575,



"scope": "environment",



"schemaId": "builtin:networkzones.zones",



"value": {



"id": "my-network-zone",



"alternativeZones": [],



"fallbackMode": "ANY_ACTIVE_GATE"



}



}
```

### Create a network zone

```
POST /api/v2/settings/objects



[



{



"schemaId": "builtin:networkzones.zones",



"scope": "environment",



"value": {



"id": "my-network-zone",



"description": "My new network zone",



"alternativeZones": [],



"fallbackMode": "ANY_ACTIVE_GATE"



}



}



]
```

Response; returns the status and object ID of the created network zone:

```
[



{



"code": 200,



"objectId": "<objectId>"



}



]
```

### Update a network zone

The request body must include all fields; this is a full replacement, not a partial update. The `id` field must be present but cannot be changed.

```
PUT /api/v2/settings/objects/{object-id}



{



"value": {



"id": "my-network-zone",



"description": "Updated description",



"alternativeZones": [],



"fallbackMode": "ANY_ACTIVE_GATE"



}



}
```

Response:

```
{



"code": 200,



"objectId": "<objectId>"



}
```

### Delete a network zone

```
DELETE /api/v2/settings/objects/{object-id}
```

A successful deletion returns `204 No Content` with no response body.

## Related topics

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")
* [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")