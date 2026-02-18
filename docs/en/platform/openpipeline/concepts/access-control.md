---
title: Owner-based access control in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/concepts/access-control
scraped: 2026-02-18T05:52:43.451937
---

# Owner-based access control in OpenPipeline

# Owner-based access control in OpenPipeline

* Latest Dynatrace
* Explanation
* 1-min read
* Published Jan 09, 2026

Access control provides fine-grained permission management, balancing development team autonomy with administrator oversight for secure and sustainable ownership. It restricts who can create, edit, view, or share settings objects, while maintaining environment-level permissions.

Availability

Owner-based control is available for pipelines and ingest sources, and not routing.

## Access control and permissions

Access control and permissions are related concepts. For the settings objects where owner-based control is available

* Permissions are specific to the configuration scope setting schema.

  Permissions grant read or write permission at the environment level and are assigned to users or user groups by an administrator. If owner-based control is available for a settings object, permissions alone won't grant access to the settings object. The owner (or administrator) needs to share access for each object with the users or user groups.
* Access control is specific to the settings object.

  Owner-based access control grants view or edit access to a specific object and is defined by its owner. Access control alone doesn't grant access to a specific object if the user doesn't have sufficient permissions on the environment level. The administrator needs to grant the users or user groups sufficient permissions for the owner to share access with them.

Therefore, a settings object, such as a pipeline, can be accessed by a user who is one of the following:

* The owner of the object with sufficient permissions (`settings:objects:read` and `settings:objects:write`)
* An accessor of the object with view or edit access and sufficient permissions (`settings:objects:read` or `settings:objects:write`)
* Administrator (`settings:objects:admin`)

Show me examples

* Example 1: Grant edit access to a custom ingest source to a user.

  + The administrator assigns read and write permissions.

    ```
    ALLOW settings:objects:read, settings:objects:write WHERE settings:schemaId = "builtin:openpipeline.events.ingest-sources"
    ```
  + The owner shares view and edit access to the custom ingest source they own.

  The accessor can view and edit the custom event ingest source and view event built-in ingest sources.
* Example 2: Grant view access to all pipelines to a user group.

  + The administrator assigns read permissions.

    ```
    ALLOW settings:objects:read WHERE settings:schemaGroup IN ("group:openpipeline.all.pipelines")
    ```
  + The owners of custom pipelines share view access.

  The user group can view all built-in pipelines and the custom pipelines to which they have been given access. Because the user group lacks write permissions, the user group can't create or edit custom pipelines, even if owners share edit access.

## Owner

Owners manage settings objects and can share access with other users or transfer ownership at any time, without relying on centralized administrator intervention. The initial owner of the settings object is the user who creates it. Right after it's created, it's private, and only the owner and the administrator can see, access, and manage it.

Owners can:

* Make the settings object public by sharing view access with all users.
* Share the settings object with specific users or user groups.
* Transfer ownership to another user or user group.

## Accessor

Accessors are users who can view or edit settings objects as specified by the owner and according to their permissions.

## Administrator

Administrators maintain complete oversight at the environment level and can control settings objects created by other users, ensuring continuity if the owner is unavailable. Administrators don't need to be an owner or accessor to see settings objects.

Administrators can:

* Access in view and edit mode all settings objects in an environment.
* Manage settings objects where the owner is unavailable.
* Transfer ownership of any settings object.

## Use cases

* Empower teams with self-service configuration.
* Delegate rights, maintaining governance and compliance.

## Related topics

* [Set access control in OpenPipeline](/docs/platform/openpipeline/getting-started/set-access-control "Distribute OpenPipeline ingest source and pipeline management via owner-based access control.")