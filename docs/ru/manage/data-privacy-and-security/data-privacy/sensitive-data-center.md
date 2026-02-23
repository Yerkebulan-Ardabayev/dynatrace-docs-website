---
title: Sensitive Data Center
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center
scraped: 2026-02-23T21:30:16.458616
---

# Sensitive Data Center

# Sensitive Data Center

* Latest Dynatrace
* App
* 9-min read
* Updated on Jan 21, 2026

## Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

storage:logs:read

Enables the app to query logs

storage:logs:write

Enables the app to write privacy audit logs

storage:buckets:read

Enables the app to list Grail buckets

state:app-states:read

Enables the app to read request data

state:app-states:write

Enables the app to store request data

state:app-states:delete

Enables the app to delete request policies

state:user-app-states:read

Enables the app to read user configuration

state:user-app-states:write

Enables the app to store user configuration

iam:service-users:use

Enables the app to process requests using a service user

email:emails:send

Enables the app to send status updates for requests

10

rows per page

Page

1

of 1

## Before you begin

Some one-time setup is necessary before using ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.

### Create service user

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** uses a service user to continue processing scans and requests while you aren't using the app. See [Create service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users#create-service-users "Service users") to learn how to create the service user. Follow the following instructions to set up the service user:

1. Name the service user `sensitive-data-center`. The name must match exactly.
2. Create a policy with the policy statement below, to grant the service user the required permissions.
3. Create a group to assign the policy to (for example, `sensitive-data-center-service-users`) and assign the service user to this group. For more details, see [Create policies based on a service user](/docs/manage/identity-access-management/user-and-group-management/access-service-users#policy "Service users").
4. This user must also be assigned to the `sensitive-data-center-users` group defined in the next section.

```
ALLOW app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW iam:users:read, iam:groups:read;



ALLOW storage:records:delete, storage:logs:write, storage:events:write;



ALLOW storage:fieldsets:read, storage:system:read, storage:logs:read, storage:events:read, storage:bizevents:read, storage:metrics:read, storage:spans:read, storage:buckets:read;



ALLOW email:emails:send;



ALLOW document:documents:read, document:documents:write, document:direct-shares:write, document:documents:delete, document:trash.documents:delete;



ALLOW automation:workflows:read, automation:workflows:write;
```

If you previously used **Privacy Rights**, rename your `privacy-rights` service user to `sensitive-data-center` rather than creating a new service user. Note that the required permissions have changed and you must also update them. Renaming your service user allows ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to automatically clean up the workflow used by **Privacy Rights**. Alternatively, a Workflows administrator can delete it manually.

### `sensitive-data-center-users` group

Assign users to this group when you want them to be able to create requests and scans. To view all matching data for requests and scans, these users need unrestricted access to data in [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."). For ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to function correctly, the group name must match exactly and a [policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") with the following permissions must be assigned to the group:

```
ALLOW app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW app-engine:functions:run;



ALLOW state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW state:user-app-states:read, state:user-app-states:write, state:user-app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW iam:service-users:use WHERE iam:service-user-email = "YOUR-SERVICE-USER-EMAIL-HERE";



ALLOW iam:users:read, iam:groups:read;



ALLOW storage:logs:write, storage:events:write;



ALLOW storage:fieldsets:read, storage:logs:read, storage:bizevents:read, storage:buckets:read;



ALLOW email:emails:send;



ALLOW document:documents:read;



ALLOW automation:workflows:read, automation:workflows:write;
```

Replace the placeholder value for `iam:service-user-email` with the email of your `sensitive-data-center` service user. To find the email of your service user:

1. In Dynatrace, go to [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.").
2. Select **Identity & access management** > **Service users**. You will see an overview table with all of your service users.
3. In the **Actions** column, select  >  **Edit**.
4. The service user's email is displayed at the top.

If you previously used **Privacy Rights**, this group is equivalent to the `Privacy Rights request assignees` group. You can edit the group name and reuse the same group, but note that you need to add additional permissions to the policy. These permissions support the Sensitive Data Scanner functionality, which is currently available as a [preview program](/docs/whats-new/preview-releases "Learn about our Preview releases and how you can participate in them.") in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.

### `sensitive-data-center-admins` group

Assign users to this group when you want them to be able to approve requests and delete data from Grail. All users assigned to this group must also be assigned to the `sensitive-data-center-users` group. For ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** to function correctly, the group name must match exactly and a [policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") with this permission must be assigned to the group:

```
ALLOW storage:records:delete;
```

If you previously used **Privacy Rights**, this group is equivalent to the `Privacy Rights request reviewers` group. You can edit the group name and reuse the same group, but note that the policy has changed.

### Configure audit logging

By default, audit logs go to the `default_logs` bucket. To change this, you can create a `privacy_audit` bucket to assign audit logs to. The name must match exactly. You can customize the retention period to suit your needs and restrict access to the bucket using IAM policies. You also need to [configure bucket assignment](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.") so that logs matching `log.source == "Sensitive Data Center"` are assigned to the `privacy_audit` bucket.

### Restrict access

As sensitive data is visible in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, we recommend you restrict access for users who don't need to create or review requests and scans. To prevent users from accessing ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, you can assign them to a group with the following policy:

```
DENY app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY state-management:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY iam:service-users:use WHERE iam:service-user-email = "YOUR-SERVICE-USER-EMAIL-HERE";
```

They should also be denied read access to audit logs in the `default_logs` or `privacy_audit` buckets (depending on your chosen audit logging configuration).

## Get started



![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** empowers you to address and manage customer requests related to data subject rights under applicable data protection laws (for example, GDPR and CCPA/CPRA).

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** helps you to:

* [Export personal data](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/export-personal-data "Export personal data with Sensitive Data Center export requests."): Review and export personal data that relates to a specific end user.
* [Delete personal data](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/delete-personal-data "Delete personal data with Sensitive Data Center deletion requests."): Review and delete personal data that relates to a specific end user.
* [Clean up data](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data "Clean up data with Sensitive Data Center cleanup requests."): Delete mistakenly ingested data for a specific timeframe.
* [Schedule scans](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan "Create a scheduled scan to maintain personal data with Sensitive Data Center."): Create scans for mistakenly ingested sensitive data, such as credit card numbers and IBANs, using the Sensitive Data Scanner. This functionality is only available as a [preview](/docs/whats-new/preview-releases "Learn about our Preview releases and how you can participate in them.").

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** currently supports export, deletion, and cleanup of Grail logs. Other data types are not supported.

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** uses a multi-party access control model to protect your data. This requires setup of policies, groups, and a service user before first use of the app. See [Prerequisites](#prerequisites) to learn more.

We recommend that you restrict access to the app, app state, service user, and audit logs to a small group of trusted users. The service user has extensive permissions and could be mistakenly or deliberately abused, for example, to delete a large volume of data. Users with access to the app state may be able to modify requests even if they don't have access to the app UI. To learn how to restrict access, see [Prerequisites](#prerequisites).

![Create a request to review and export personal data about a specific end-user. The overview includes details of all requests, including the relevant user identifier, assignees and reviewers, the current status of each request, as well as the defined due date. Audit logs and request policies can be accessed and managed from this page.](https://cdn.hub.central.dynatrace.com/hub/hub1_DVwrUOD.png)![In the export request form, you specify the user details such as user type, a user identifier to search for matching data in Grail, and the scope of the search in Grail (the timeframe and log buckets).](https://cdn.hub.central.dynatrace.com/hub/hub3_qr80Yha.png)![For each created request, the data matching the executed query are returned and can be viewed by number of log records, volume, data residency, as well as number of systems. The reviewer can then approve or reject export of this data.](https://cdn.hub.central.dynatrace.com/hub/hub4-final.png)

1 of 3Create a request to review and export personal data about a specific end-user. The overview includes details of all requests, including the relevant user identifier, assignees and reviewers, the current status of each request, as well as the defined due date. Audit logs and request policies can be accessed and managed from this page.

## Use cases

* Easily filter, query, and review data processed about a specific end-user in Grail.
* Export personal data relating to a specific end-user to respond to an access request (for example, right of access in the GDPR).
* Delete personal data relating to a specific end-user to comply with a deletion request (for example, right of erasure in the GDPR).
* Cleanup any mistakenly ingested data for a specific timeframe.

## Best practices

To limit the scope of requests:

* Use the shortest possible timeframe and select relevant buckets only.
* Make sure you aren't exporting personal data of other individuals or confidential data.
* Use [policies](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy "Create a policy to enrich or filter request results with Sensitive Data Center.") to help ensure that your organizationâs policies regarding sensitive data are followed.
* Minimize the number of logs you export/delete so it is easier to review the data.

## FAQ



I see a banner informing me that permissions are misconfigured, what should I do?

If you see a banner informing you that permissions are misconfigured, confirm that:

1. Permissions are configured correctly for the service user, to learn more see [Prerequisites](#prerequisites).
2. The simple workflow used by the app has not been mistakenly deleted or switched off. Users with the `automation:workflows:admin` permission can view and edit the workflow in **Workflows** after enabling admin mode. The workflow should be enabled on a schedule and include the appâs **Process deletion requests** workflow action.

I noticed that deletion and cleanup requests in the "Approved" state don't transition into the "Processing" state, what should I do?

If you notice that deletion and cleanup requests in the **Approved** state don't transition into the **Processing** state, confirm that:

1. Permissions are configured correctly for the service user, to learn more see [Prerequisites](#prerequisites).
2. The simple workflow used by the app has not been mistakenly deleted or switched off. Users with the `automation:workflows:admin` permission can view and edit the workflow in **Workflows** after enabling admin mode. The workflow should be enabled on a schedule and include the appâs **Process deletion requests** workflow action.

My request is in "Failed" state, what should I do?

If any deletion error occurs, then your request transitions into the **Failed** state. In the request details, further information will be provided for each failed task. Deletion and cleanup requests are processed in one or more tasks that cover specific timeframes. You can assume that deletion has succeeded for any timeframe not listed in the failed tasks. There are four reasons why a deletion task may fail:

1. **Invalid request:** the request was not accepted because either it uses [DQL that is unsupported for deletion](/docs/platform/grail/organize-data/record-deletion-in-grail "Find out how to delete records in Grail via API.") or it matches too many records. No data has been deleted. You can resolve this by creating a new request with a modified query and attempting deletion again for the failed timeframe(s).
2. **Trigger timeout:** due to a temporary outage, it was not possible to start deletion and the task timed out. No data has been deleted. We recommend you wait 12 hours or longer, then create a new request for the failed timeframe(s) to attempt deletion again.
3. **Processing timeout:** due to a temporary outage during deletion, the task has timed out. Data may have been partially deleted. We recommend you wait 12 hours or longer, then create a new request for the failed timeframe(s) to attempt deletion again.
4. **Internal error:** an internal error occurred during deletion. In this unlikely case, data may have been partially deleted for the timeframe. Please contact Support so we can assist you in resolving the issue.

Why do I get an error when I approve a request?

If you see an error, either you are missing permissions or the app is not yet fully set up. To approve a request, you must be a member of the `sensitive-data-center-admins` group. Confirm that you are in this group, the `sensitive-data-center` service user exists, and both the group and service user are configured as described in [Prerequisites](#prerequisites). The names must match exactly.

Why can't I see my audit logs in the Audit Log tab?

If no audit logs are visible in ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, check if bucket assignment is misconfigured.

If the `privacy_audit` bucket exists, bucket assignment must be configured to route ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** audit logs to it, as ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** only queries this bucket.

If the `privacy_audit` bucket does not exist, check if any other assignment rules are mistakenly assigning ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** audit logs to a different bucket than `default_logs`. If this is not the case, then your volume of log ingest is too high to use `default_logs` and you must configure the `privacy_audit` custom bucket (see [Prerequisites](#prerequisites)).

I previously used Privacy Rights. What happened to it?

**Privacy Rights** has been replaced by ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, which offers the same privacy rights request functionality combined with additional features for sensitive data management. To support these features, new IAM groups and policies are required, so additional one-time setup is necessary. For customers who previously used **Privacy Rights**, request data is retained in **Privacy Rights**, but requests and policies can no longer be created.

Why do I see failed scans?

The most likely cause of failed scans is misconfigured permissions for the service user. Check that the service user's name, two assigned groups, and the policies assigned to those groups exactly match the description in [Prerequisites](#prerequisites).

## Learning modules

[01Create a policy in Sensitive Data Center

* How-to guide
* Create a policy to enrich or filter request results with Sensitive Data Center.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy)[02Export personal data in Sensitive Data Center

* How-to guide
* Export personal data with Sensitive Data Center export requests.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/export-personal-data)[03Review audit logs in Sensitive Data Center

* How-to guide
* Review Sensitive Data Center audit logs.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/review-audit-logs)[04Delete personal data in Sensitive Data Center

* How-to guide
* Delete personal data with Sensitive Data Center deletion requests.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/delete-personal-data)[05Clean up data in Sensitive Data Center

* How-to guide
* Clean up data with Sensitive Data Center cleanup requests.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data)[06Create scheduled scan in Sensitive Data Center

* How-to guide
* Create a scheduled scan to maintain personal data with Sensitive Data Center.](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan)