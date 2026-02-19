---
title: Queue tags and management zones
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones
scraped: 2026-02-19T21:21:48.717362
---

# Queue tags and management zones

# Queue tags and management zones

* How-to guide
* 2-min read
* Published May 16, 2022

You can use tags and management zones to organize queue entities in your environment and simplify searches for them. Tags and management zones are applied to queue entities just as they are for other entities, but they must be applied via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Define an automatically applied tag

Follow the steps below to automatically apply a tag to queue entities. To learn more about tags, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

1. Go to **Settings** > **Tags** > **Automatically applied tags**.
2. Select **Create tag** and type a name for the new tag in the **Tag name** field.
3. Select **Add a new rule**.
4. Optional Specify an **Optional tag value**. This value will appear next to the tag name after a `:` and is used to provide more precise information about the queue entity.
5. From the **Rule type** list, choose the **Entity selector** type.
6. Use one of the following code snippets to apply tags from a service, process group, host, or host group entity to a queue entity via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."). Replace `yourKey:yourValue` with your own tag values.

   Producer services

   Consumer services

   Process groups

   Hosts

   Host groups

   ```
   type(QUEUE),toRelationships.indirectlySendsToQueue(type(SERVICE),tag("yourKey:yourValue "))
   ```

   ```
   type(QUEUE),toRelationships.listensOnQueue(type(SERVICE),fromRelationships.calls(type(SERVICE),tag("yourKey:yourValue")))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isInstanceOf(type(PROCESS_GROUP),tag("yourKey:yourValue"))))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),tag("yourKey:yourValue"))))
   ```

   ```
   type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.isInstanceOf(type(HOST_GROUP),tag(("yourKey:yourValue")))))
   ```
7. Select **Preview** to verify the results returned by the specific entity selector.
8. Select **Save changes**.

Example of a rule-based entity selector

![Queue entity selector](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Add queue entities to existing management zones

Follow the steps below to add queue entities to existing management zones. To learn more about management zones, see [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.").

1. Go to **Settings** > **Preferences** > **Management zones**.
2. Edit an existing management zone and select **Add a new rule**.
3. In the **Rule applies to** list, choose the **Entity selector**.
4. Use one of the following code snippets to add a queue entity based on tags from a service, process group, host, or host group entity to a management zone via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."). Replace `yourKey:yourValue` with your own tag values.

Producer services

Consumer services

Process groups

Hosts

Host groups

```
type(QUEUE),toRelationships.indirectlySendsToQueue(type(SERVICE),tag("yourKey:yourValue "))
```

```
type(QUEUE),toRelationships.listensOnQueue(type(SERVICE),fromRelationships.calls(type(SERVICE),tag("yourKey:yourValue")))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isInstanceOf(type(PROCESS_GROUP),tag("yourKey:yourValue"))))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),tag("yourKey:yourValue"))))
```

```
type(QUEUE),toRelationships.isInstanceOf(type(QUEUE_INSTANCE),fromRelationships.runsOn(type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.isInstanceOf(type(HOST_GROUP),tag(("yourKey:yourValue")))))
```

5. Select **Preview** to verify the results returned by the specific entity selector.
6. To save your management zone configuration, select **Save changes** at the bottom right corner of the page.

Example of a management zone based on the entity selector

![Management zone for queues](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Related topics

* [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")