---
title: Policy global attributes
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes
scraped: 2026-05-12T11:49:54.505224
---

# Policy global attributes

# Policy global attributes

* Reference
* 1-min read
* Published Dec 20, 2020

For some global conditions, the policy framework provides attributes that can be used in policy syntax. These attributes donât require any additional configuration in the form of defining binding parameters.

List of available global attributes:

| Global attribute | Description |
| --- | --- |
| `${global:levelId}` | [Organizational level](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt#list "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") of permission evaluation |
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