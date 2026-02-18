---
title: Permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/reference/permissions
scraped: 2026-02-18T05:32:57.029948
---

# Permissions

# Permissions

* Latest Dynatrace
* Reference
* 1-min read
* Published Jan 19, 2024

This guide outlines the necessary permissions for ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** and describes how to tailor them to fit specific roles and requirements.

## User permissions

To fully utilize all use cases of ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, a specific set of permissions is required. You can find the complete list of these permissions via Dynatrace Hub.

In Dynatrace Hub, select **Kubernetes** ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") to view the necessary permissions.

To manage permissions within ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, you can assign default policies to different roles assigned to user groups (such as **AppEngine User**, **Storage All Grail Data Read**).

## Tailoring permissions/policies

Dynatrace IAM allows for a highly detailed and flexible definition and assignment of permissions. These permissions can be grouped into policies and then assigned to users or groups. Additionally, permissions can be targeted to specific subsets of Kubernetes objects by using conditions, such as for particular clusters and/or namespaces.

For more information, see [Identity and access management (IAM)](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Example policy

```
ALLOW hub:catalog:read;



ALLOW storage:buckets:read, storage:entities:read, storage:events:read, storage:logs:read, storage:metrics:read;



ALLOW environment-api:api-tokens:write, environment-api:entities:read, environment-api:entities:write, environment-api:metrics:read, environment-api:security-problems:read, environment-api:slo:read;



ALLOW settings:objects:read, settings:objects:write, state:user-app-states:read, state:user-app-states:write;



ALLOW davis:analyzers:execute, unified-analysis:screen-definition:read;
```