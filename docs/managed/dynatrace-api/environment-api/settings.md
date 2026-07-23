---
title: Settings API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings
---

# Settings API

# Settings API

* Reference
* Updated on Jul 09, 2026

[### Key concepts

Before you start, understand the key concepts of the Settings API, including scopes, schemas, external IDs, pagination, and concurrency control.](/managed/dynatrace-api/environment-api/settings/key-concepts "Explore the key concepts of the Settings API, including scopes, schemas, external IDs, pagination, and concurrency control.")

## Schemas

[### List schemas

Get an overview of all settings schemas in your environment.](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.")[### View a schema

Get parameters of a schema.](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.")

## Objects

[### List objects

Get an overview of settings objects.](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.")[### View an object

Get parameters of a settings object.](/managed/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.")

[### Create an object

Create a new settings object or validate the object you're working on.](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.")[### Edit an object

Update an existing settings object.](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")[### Delete an object

Delete a settings object you no longer need.](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.")[### View values

Check the actual configuration of a settings object.](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.")

## Permissions

[### List object permissions

Get all permissions set on a settings object.](/managed/dynatrace-api/environment-api/settings/objects/get-permissions "View all permissions on a settings object via the Dynatrace API.")[### Add object permission

Add permissions for a single accessor on a settings object.](/managed/dynatrace-api/environment-api/settings/objects/post-permission "Add permissions for a single accessor on a settings object via the Dynatrace API.")

[### View all-users permission

Get the all-users accessor permissions on a settings object.](/managed/dynatrace-api/environment-api/settings/objects/get-permission-all-users "View the all-users accessor permissions on a settings object via the Dynatrace API.")[### Update all-users permission

Update the all-users accessor permissions on a settings object.](/managed/dynatrace-api/environment-api/settings/objects/put-permission-all-users "Update the all-users accessor permissions on a settings object via the Dynatrace API.")[### Delete all-users permission

Remove the all-users accessor permissions from a settings object.](/managed/dynatrace-api/environment-api/settings/objects/del-permission-all-users "Remove the all-users accessor permissions on a settings object via the Dynatrace API.")

[### View accessor permission

Get the permissions of a specific accessor on a settings object.](/managed/dynatrace-api/environment-api/settings/objects/get-permission "View accessor permissions on a settings object via the Dynatrace API.")[### Update accessor permission

Update the permissions of a specific accessor on a settings object.](/managed/dynatrace-api/environment-api/settings/objects/put-permission "Update accessor permissions on a settings object via the Dynatrace API.")[### Delete accessor permission

Remove the permissions of a specific accessor from a settings object.](/managed/dynatrace-api/environment-api/settings/objects/del-permission "Remove accessor permissions on a settings object via the Dynatrace API.")

[### Transfer ownership

Transfer ownership of a settings object to another user.](/managed/dynatrace-api/environment-api/settings/objects/post-transfer-ownership "Transfer ownership of a settings object via the Dynatrace API.")

## Related topics

* [Dynatrace settings framework](/managed/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")