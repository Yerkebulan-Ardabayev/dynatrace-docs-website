---
title: Policy global attributes (Dynatrace Classic)
source: https://docs.dynatrace.com/managed/manage/identity-access-management-classic/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes-classic
---

# Policy global attributes (Dynatrace Classic)

# Policy global attributes (Dynatrace Classic)

* Reference
* 1-min read
* Updated on Oct 08, 2026

For some global conditions, the policy framework provides attributes that can be used in policy syntax. These attributes don’t require any additional configuration in the form of defining binding parameters.

List of available global attributes:

| Global attribute | Description |
| --- | --- |
| `${global:levelId}` | [Organizational level](/managed/manage/identity-access-management-classic/permission-management/manage-user-permissions-policies/iam-policy-mgt-classic#list "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") of permission evaluation |
| `${global:userGroup}` | List of UUIDs of groups user is assigned to |

#### Examples

This policy lets users access all management zones that have the same name as their assigned groups.

```
ALLOW environment:roles:viewer WHERE environment:management-zone IN ('${global:userGroup}');
```

This policy provides users with access to the management zone that has the same name as an environment ID. This may be useful if your naming conventions are designed around environment IDs.

```
ALLOW environment:roles:viewer WHERE environment:management-zone = "${global:levelId}";
```