---
title: Visibility of segments
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-visibility
scraped: 2026-02-15T08:59:19.214806
---

# Visibility of segments

# Visibility of segments

* Latest Dynatrace
* Explanation
* 1-min read
* Published Mar 29, 2023

The **Visibility** setting determines who sees the segment in their list of segments.

* **Unlisted**âthese segments are visible only in the owner's list of segments. This prevents segment lists from becoming unnecessarily cluttered. This is the default setting.
* **Anyone in the environment**âthese segments are listed in everyone's list of segments.

![segments query](https://dt-cdn.net/images/segments-6-1000-e8d8694fe0.png)

It is important to understand that the **Visibility** setting doesn't affect general access to segments.

* Unlisted segments can still be made available to others by being referenced in apps, such as in shared notebooks and dashboards. Everyone has read-only access to all segments. This makes collaboration with segments simple.
* Permissions in IAM policies determine who can configure segments visible to anyone.
* Segments themselves don't contain any data. All queries, with or without segments, always respect data access permissions enforced by IAM policies.

## Segment permissions

Regardless of configured visibility, any segment can be accessed with `storage:filter-segments:read` permission. This guarantees that even unlisted segments that may be referenced in a shared notebook, can be used by anyone having access to that notebook.

For more information on segment permissons see [IAM policy statements](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-filter-segments-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").