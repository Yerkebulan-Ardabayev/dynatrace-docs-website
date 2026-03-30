---
title: Upgrade to Log Management and Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma
scraped: 2026-03-06T21:14:27.302891
---

# Upgrade to Log Management and Analytics


* Classic
* How-to guide
* 6-min read
* Updated on Jul 07, 2023

Log Management and Analytics is the latest Dynatrace log monitoring solution. With the introduction of Dynatrace Platform and Grail, we encourage you to upgrade to the latest log monitoring offer. If you use Dynatrace SaaS on AWS, your environment will be enabled for Log Management and Analytics powered by Grail with a phased rollout.

For more information about the phased rollout, please reach out to one of your Dynatrace Account team members. You can also reach out directly to Dynatrace product experts via live chat within your Dynatrace environment. Our product experts will get you in touch with your account team members and help with answers to any other questions you might have.

### How can I upgrade from Log Monitoring Classic to Log Management and Analytics?

Once your environment is enabled for activation:

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. In the banner message, select **Go to activation page** and select **Activate Logs powered by Grail**.
3. On the **Activate Grail for log and events** page you can select:

   * **Activate now**
   * **Wait 7 days**
4. Select **Confirm** to verify your choice.

* Only administrative users can activate Log Management and Analytics for the environment.
* Activating Log Management and Analytics is not reversible.

### Upgrade with existing data

You can choose to upgrade with your existing log data.

* If you choose **Wait 7 days** on the **Activate Grail for log and events** page, Grail activation will be postponed for 7 days.
  During that timeframe, your log data will be ingested into both Log Monitoring Classic and Grail. After the 7 day period ends, Grail will be activated automatically and you will begin using Log Management and Analytics with 7 days of existing data.
* If you require log data for a longer period before upgrading, contact a Dynatrace product expert via live chat and request the longer wait time.
* If upgrading with existing data is not important for you, choose **Activate now** on the **Activate Grail for log and events** page and Logs powered by Grail will become active in about 30 seconds.

### What changes after activation

After activating Log Management and Analytics, the following changes take place:

* Ingested log data

  + Ingested log data is saved in the Grail database.
  + Ingested log data can be routed to buckets with different retention periods.
* DDU consumption

  + When you activate Log Management and Analytics, you begin consuming DDUs under a new model with three dimensions: Ingest & Process, Retain, Query.
  + If you choose **Wait 7 days**, you'll still start consuming DDUs for ingestion and retention under the new model immediately and for querying after you run your first DQL query.
* API

  + The log export API will not be available. We recommend that you stop using Log GET search and Log GET aggregate. If you continue using them, they require an OAuth2 token with the `storage:logs:read` and `storage:buckets:read` scopes.
  + We recommend that you switch from existing APIs to the [Grail Query APIï»¿](https://developer.dynatrace.com/platform-services/services/storage/).
* No support for Management Zones

  + Management Zones configuration will not work with Grail. You have to use buckets and policies for access control. Please check the **User access** section below.

### What does not change after activation

After activating Log Management and Analytics, the following will not change:

* Ingestion configuration, including OneAgent configuration and generic API ingest.
* Log processing, including [processing rules](../../logs/lma-classic-log-processing.md#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.") with matchers based on the LQL syntax.
* Log metrics, including metric queries based on the LQL syntax.
* Log events, including event queries based on the LQL syntax.

However we recommend to convert your LQL matchers for log processing, metrics and events to highly performing DQL matcher.

### User access

The user access granting process depends on whether you are a new or existing user.

Management Zones configuration will not work with Grail. You have to use buckets and policies for access control.

* Assign policy to existing users  
  After activating Log Management and Analytics, all users who already had access to log data are assigned a new policy to access the log data in Grail.
* Assign policy to new users

  There are two options for configuring access policies for Grail:

  Assign policy using Account Admin

  In Dynatrace SaaS, only admin users can manage policies (users with account permission `Manage users`).  
  You need to have two policies, **Storage Events Read** and **Storage Logs Read** assigned, bound to a group.

  To check if your policies are assigned

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
  2. Go to **Identity & access management** > **Policy management**.
  3. Check if Storage Events Read and Storage Logs Read are present on the policy list.

  If **Storage Events Read** and **Storage Logs Read** are not present on you policy list, you need to add them manually:

  + **Storage Events Read**:  
    **Policy name**: Storage Events Read  
    **Policy description**: Enables reading events from GRAIL  
    **Policy statements**: `ALLOW storage:events:read`
  + **Storage Logs Read**:  
    **Policy name**: Storage Logs Read  
    **Policy description**: Enables reading logs from GRAIL  
    **Policy statements**: `ALLOW storage:logs:read`  
    For details, see [Manage IAM policies](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md#create "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

  To make a policy effective, you need to [bind it to a group](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md#add-or-remove "Working with policies").

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
  2. Select **Identity & access management** > **Group management**.  
     For details, see Working with policies.
  3. Edit the group to which you want to bind the policy (for example, Logs and events). Make sure the users who need to use the Logs and events have this group assigned to their names.
  4. Select the **Policies** tab.

  Assign policy via API

  1. Obtain an OAuth token
     Make a POST call with form parameters to SSO.

     + client\_id = [client\_id]
     + client\_secret = [secret]
     + grant\_type = client\_credentials
     + scope = `iam:policies:write iam:policies:read`

     In response, you get an authorization token

     ```
     {


     "scope": "iam:policies:read iam:policies:write",


     "token_type": "Bearer",


     "expires_in": 300,


     "access_token": "123(...)ABC"


     }
     ```
  2. Create a storage events read policy
     Make a POST call to IAM

     Body payload for the policy is:

     ```
     {


     "name": "Storage Events Read",


     "description": "Storage Events Read",


     "tags": [


     ],


     "statementQuery": "ALLOW storage:events:read;"
     ```
  3. Create a storage logs read policy
     Make a POST call to IAM

     Body payload for the policy is:

     ```
     {


     "name": "Storage Logs Read",


     "description": "Storage Logs Read",


     "tags": [


     ]  ,


     "statementQuery": "ALLOW storage:logs:read;"


     }
     ```

  Your newly created policies will be visible on the account level. To check it, go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management** > **Edit Storage Events Read**.