---
title: Policy global conditions
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions
scraped: 2026-05-12T11:49:52.174517
---

# Policy global conditions

# Policy global conditions

* Reference
* 4-min read
* Published Jul 22, 2022

Global conditions (with the `global:` prefix) are conditions that can be applied to any policy statement because they are not service-specific. Service-specific conditions supported by each service are documented in [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Environment and user conditions

### global:environmentId

Global condition `global:environmentId` returns the environmentId for services within the environment's scope.

### global:userGroup

Global condition `global:userGroup` returns a list of groups IDs the user is a member of

#### Examples

This policy provides users with access to a specific environment ID. This may be useful if the policy needs to be assigned on a cluster level. Alternatively, this situation can also be solved by assigning an unconditional policy at the environment level.

```
ALLOW environment:roles:viewer WHERE global:environmentId = "130fc95d-8917-4305-b5dc-4c96190ec6ac";
```

This policy provides users with access only if they are a member of the groups that are specified in the policy. Consider using this approach if you want to have a limited number of policies for managing access.

```
ALLOW environment:roles:viewer WHERE global:userGroup = "basic-monitoring-access";
```

## Date and time global conditions

The following are simple examples of how to work with time-based conditions in policy statements.

### global:date

Global condition `global:date` is used as in the following example.

```
ALLOW service:resource:permission WHERE global:date > "2022-05-03Z" AND global:date < "2022-05-05Z";
```

In this example the policy grants access on the 4th of May 2022 in the UTC time zone.

Operators: `<`, `>`, `=`

See [Date and time formats](#date-and-time-formats) below for details on date and time formats.

### global:date-time

Global condition `global:date-time` is used as in the following example.

```
ALLOW service:resource:permission WHERE global:date-time > "2022-05-03T05:00:00+01:00";
```

Operators: `<`, `>`

See [Date and time formats](#date-and-time-formats) below for details on date and time formats.

### global:time-of-day

Global condition `global:time-of-day` is used as in the following example.

```
ALLOW service:resource:permission WHERE global:time-of-day > "09:00+01:00" AND global:time-of-day < "17:00+01:00";
```

Operators: `<`, `>`

See [Date and time formats](#date-and-time-formats) below for details on date and time formats.

### global:week-day

Global condition `global:week-day` is used as in the following example.

```
ALLOW service:resource:permission WHERE global:week-day = "Monday";
```

Operators: `=`, `!=`, `IN`

See **Date and time formats** below for details on date and time formats.

### Date and time formats

For `global:date`, `global:date-time`, and `global:time-of-day`, specify the value with a time zone according to [ISO/WD 8601-1ï»¿](https://dt-url.net/bi03p33), where the character `Z` is used to designate that the date is in UTC.

Format: day of week

The policy is active on specific days of the week (GMT time zone).

Example:

```
ALLOW service:resource:permission WHERE global:week-day = "Monday";
```

Operators: `=`, `!=`, `IN`

Format: date

The policy is active during a specified date range. The time zone must be specified.

Example:

```
ALLOW service:resource:permission WHERE global:date > "2022-05-03Z" AND global:date < "2022-05-05Z";
```

In this example the policy grants access on the 4th of May 2022 in UTC time zone.
Operators: `<`, `>`, `=`

Format: date and time

The policy is active according to a specified date and time. The time zone must be
specified.

Example:

```
ALLOW service:resource:permission WHERE global:date-time > "2022-05-03T05:00:00+01:00";
```

Operators: `<`, `>`

Format: time of day

The policy is active each day during a specified time range. The time zone must be specified.

Example:

```
ALLOW service:resource:permission WHERE global:time-of-day > "09:00+01:00" AND global:time-of-day < "17:00+01:00";
```

Operators: `<`, `>`