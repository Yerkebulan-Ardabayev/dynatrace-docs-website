---
title: Grant access to Grail
source: https://www.dynatrace.com/docs/manage/identity-access-management/use-cases/access-grail
scraped: 2026-02-28T21:18:38.037137
---

# Grant access to Grail

# Grant access to Grail

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 01, 2024

This tutorial will guide you through the process of setting up data access on Grail for your users. Access control to data in Grail happens on multiple levels: buckets, tables, records, and fields.

## Who this is for

This tutorial is for Dynatrace account administrators who need to use default policies to grant users access to data stored in Grail.

## What you'll learn

In this tutorial, you'll learn

1. Which default policies are available for Grail access
2. How to use those policies to grant access to monitoring data stored in Grail

## Steps

We start by learning about available policies, and then we learn how to use those policies to grant access to monitoring data stored in Grail.

### 1. Default policies

Dynatrace comes with a set of built-in policies for data access. Their names all start with the `storage` prefix. For example, take a look at the **Storage Default Monitoring Read** policy, which provides the following two permissions:

```
ALLOW storage:buckets:read WHERE storage:bucket-name STARTSWITH "default_;"



ALLOW storage:events:read,storage:logs:read,storage:metrics:read,storage:entities:read,storage:bizevents:read,storage:spans:read;
```

This grants a user access to all tables and to all default buckets (they have the `default_` prefix). Once custom buckets are created, users must get explicit access to them to access them.

**Note**: Built-in policies all provide unconditional table access. Once you start adopting record-level permissions, you'll need to replace the default policies with your own.

### 2. Grant access to data stored in Grail

#### Storage Default Monitoring Read

Administrators can use this permission to give users access to the tables and data stored in default buckets (default bucket names start with the `default_` prefix). This policy will be adjusted automatically as new tables are added to Grail in the future.

Be aware that this policy only covers default buckets. Once custom buckets are added to Grail, administrators need to define additional permissions.

```
ALLOW storage:buckets:read WHERE storage:bucket-name startsWith âdefault_â;ALLOW storage:events:read, storage:logs:read, storage:metrics:read, storage:entities:read, storage:bizevents:read, storage:spans:read;
```

#### Storage Read per table

Each table includes a policy that combines table and bucket access called **Storage** `<tablename>` **Read**. Administrators can use this policy to grant a user group access to a certain table and the assigned buckets.

```
ALLOW storage:buckets:read WHERE storage:table-name = âlogsâ;



ALLOW storage:logs:read;
```

#### Storage All System Data Read

The **Storage All System Data Read** policy grants access to Dynatrace internal data such as auditing events and query execution events. Administrators can add this policy to those users who need access to this type of data.

```
ALLOW storage:buckets:read;ALLOW storage:system:read;ALLOW storage:events:read, storage:logs:read, storage:metrics:read, storage:entities:read, storage:bizevents:read,storage:spans:read;
```

#### Storage All Grail Data Read

The **Storage All Grail Data Read** policy grants unfiltered access to all data in Grail.

```
ALLOW storage:buckets:read;



ALLOW storage:system:read;



ALLOW storage:events:read, storage:logs:read, storage:metrics:read, storage:entities:read, storage:bizevents:read,storage:spans:read;
```

For full details, see [bucket and table permissions for Grail documentation](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").