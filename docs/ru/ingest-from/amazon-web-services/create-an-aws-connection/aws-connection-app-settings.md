---
title: Create an AWS connection via Settings
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/create-an-aws-connection/aws-connection-app-settings
scraped: 2026-02-28T21:19:35.035332
---

# Create an AWS connection via Settings

# Create an AWS connection via Settings

* Latest Dynatrace
* How-to guide
* Updated on Jan 09, 2026

Onboard your AWS account in few steps that will generate a deployable CloudFormation template.

The CloudFormation stack will deploy core mandatory resources inside your AWS account (Dynatrace IAM monitoring role, AWS secrets, Dynatrace API integration Lambda function).

After a successful deployment, a connection from Dynatrace to your AWS account will be created. Dynatrace will then perform API calls to your AWS account to poll and push telemetry into your Dynatrace environment.

The new integration does not deploy or use ActiveGate compute resources inside your AWS account to poll or push telemetry.

The experience is transparent and fully managed by Dynatrace.

## Overview

### General recommendations

We highly discourage onboarding AWS accounts that are actively monitored by our classic AWS integration. Onboarding such accounts might increase the likelihood of AWS APIs throttling, potentially resulting in service interruptions.

### Limitations

* GovCloud and China partitions are not supported.
* Dynatrace is designed to support large and complex AWS environments. By default, a Dynatrace environment can accommodate up to 3,000 AWS connections (each connection representing a single AWS account).

  This is a soft limit. If you plan to exceed it (per Dynatrace environment), please open a support request to increase this limit.

* AWS does not support EventBridge API destinations in all Regions. Therefore, event ingest is not available in Regions that don't support it. See [EventBridge feature availabilityï»¿](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html#feature-availability-apid) for details.

## Prerequisites

Only a Dynatrace account administrator and an AWS administrator can successfully complete the initial prerequisites.

### 1. Create AWS IAM baseline

Actions in this section can and (should) only be performed by an AWS administrator.

All necessary [AWS permissions](#aws-permissions) must be granted to successfully deploy the CloudFormation stacks and associated AWS resources.

In environments where full duty separation is practiced, we recommend that the Dynatrace administrator shares the templates with the platform team/AWS administrators.

#### Core CFN templates

* [Main Deployment Stackï»¿](https://dynatrace-data-acquisition.s3.us-east-1.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-activation.yaml)
* [Integration Stackï»¿](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-nested-integration.yaml)
* [Monitoring IAM Role Stackï»¿](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-nested-monitoring-role.yaml)

#### Conditional CFN templates (deployed based on user opt-in during onboarding)

* [Firehose Log Streams Stackï»¿](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-stack-logs.yaml)
* [AWS EventBridge Integration Stackï»¿](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-stack-events.yaml)

#### AWS IAM permission policy for deploying the CloudFormation stacks

Make sure that an AWS user, or a role, used for the CloudFormation stacks deployment is granted with the following (minimum) permission policies.

To allow the least privilegeârestricting users creating the AWS connections that follow a specific naming pattern, use the value for `<Deployment-Stack-Name-Prefix>`. This ensures that any connection created must adhere to this exact [naming convention](#conn-model).

```
{



"Version": "2012-10-17",



"Statement": [



{



"Sid": "cloudformation0",



"Effect": "Allow",



"Action": [



"cloudformation:CreateStack",



"cloudformation:DescribeStacks",



"cloudformation:UpdateStack",



"cloudformation:ListStacks",



"cloudformation:DescribeStackResources",



"cloudformation:DeleteStack",



"cloudformation:CreateChangeSet",



"cloudformation:DescribeChangeSet",



"cloudformation:ExecuteChangeSet",



"cloudformation:CreateStackInstances",



"cloudformation:ListStackInstances",



"cloudformation:DescribeStackInstance",



"cloudformation:DeleteStackInstances",



"cloudformation:CreateStackSet",



"cloudformation:UpdateStackSet",



"cloudformation:DescribeStackSet",



"cloudformation:DescribeStackSetOperation",



"cloudformation:ListStackSetOperationResults",



"cloudformation:DeleteStackSet",



"cloudformation:TagResource",



"cloudformation:UntagResource"



],



"Resource": [



"arn:aws:cloudformation:*:<AWS-Account-ID>:stackset-target/*",



"arn:aws:cloudformation:<Deployment-Region>:<AWS-Account-ID>:stackset/Dynatrace*:*",



"arn:aws:cloudformation:<Deployment-Region>:<AWS-Account-ID>:stack/<Deployment-Stack-Name-Prefix>*/*",



"arn:aws:cloudformation:*:<AWS-Account-ID>:stack/StackSet-Dynatrace*/*",



"arn:aws:cloudformation:*:<AWS-Account-ID>:type/resource/*"



]



},



{



"Sid": "cloudformation1",



"Effect": "Allow",



"Action": [



"cloudformation:GetTemplate",



"cloudformation:ValidateTemplate",



"cloudformation:GetTemplateSummary"



],



"Resource": [



"*"



]



},



{



"Sid": "lambda",



"Effect": "Allow",



"Action": [



"lambda:CreateFunction",



"lambda:UpdateFunctionCode",



"lambda:UpdateFunctionConfiguration",



"lambda:GetFunction",



"lambda:InvokeFunction",



"lambda:DeleteFunction",



"lambda:TagResource",



"lambda:UntagResource"



],



"Resource": [



"arn:aws:lambda:<Deployment-Region>:<AWS-Account-ID>:function:DynatraceApiClientFunction*"



]



},



{



"Sid": "iam",



"Effect": "Allow",



"Action": [



"iam:CreatePolicy",



"iam:CreatePolicyVersion",



"iam:DeletePolicyVersion",



"iam:DeletePolicy",



"iam:CreateRole",



"iam:UpdateRole",



"iam:DeleteRole",



"iam:PassRole",



"iam:AttachRolePolicy",



"iam:PutRolePolicy",



"iam:DetachRolePolicy",



"iam:GetRole",



"iam:GetPolicy",



"iam:ListPolicyVersions",



"iam:TagPolicy",



"iam:TagRole",



"iam:UntagPolicy",



"iam:UntagRole",



"iam:GetRolePolicy",



"iam:UpdateAssumeRolePolicy",



"iam:DeleteRolePolicy"



],



"Resource": [



"arn:aws:iam::<AWS-Account-ID>:policy/<Deployment-Stack-Name-Prefix>*",



"arn:aws:iam::<AWS-Account-ID>:role/<Deployment-Stack-Name-Prefix>*",



"arn:aws:iam::<AWS-Account-ID>:role/Dynatrace*",



"arn:aws:iam::<AWS-Account-ID>:policy/Dynatrace*"



]



},



{



"Sid": "s3",



"Effect": "Allow",



"Action": [



"s3:GetObject",



"s3:CreateBucket",



"s3:DeleteBucket",



"s3:PutLifecycleConfiguration",



"s3:PutBucketTagging"



],



"Resource": [



"arn:aws:s3:::dynatrace*"



]



},



{



"Sid": "secretsmanager",



"Effect": "Allow",



"Action": [



"secretsmanager:CreateSecret",



"secretsmanager:DescribeSecret",



"secretsmanager:UpdateSecret",



"secretsmanager:GetSecretValue",



"secretsmanager:PutSecretValue",



"secretsmanager:TagResource",



"secretsmanager:DeleteSecret",



"secretsmanager:PutResourcePolicy",



"secretsmanager:DeleteResourcePolicy"



],



"Resource": [



"arn:aws:secretsmanager:<Deployment-Region>:<AWS-Account-ID>:secret:DynatraceAPIAccessToken*",



"arn:aws:secretsmanager:<Deployment-Region>:<AWS-Account-ID>:secret:DynatraceAPIPlatformToken*",



"arn:aws:secretsmanager:<Deployment-Region>:<AWS-Account-ID>:secret:/dynatrace/*"



]



},



{



"Sid": "kms0",



"Effect": "Allow",



"Action": [



"kms:CreateKey",



"kms:TagResource",



"kms:UntagResource"



],



"Resource": "*",



"Condition": {



"StringEquals": {



"aws:RequestTag/dt:CreatedBy": "Dynatrace"



}



}



},



{



"Sid": "kms1",



"Effect": "Allow",



"Action": [



"kms:CreateGrant",



"kms:RevokeGrant",



"kms:DescribeKey",



"kms:GetKeyPolicy",



"kms:PutKeyPolicy",



"kms:ScheduleKeyDeletion"



],



"Resource": "*",



"Condition": {



"StringEquals": {



"aws:ResourceTag/dt:CreatedBy": "Dynatrace"



}



}



},



{



"Sid": "kms2",



"Effect": "Allow",



"Action": [



"kms:CreateAlias",



"kms:DeleteAlias",



"kms:UpdateAlias"



],



"Resource": [



"arn:aws:kms:<Deployment-Region>:<AWS-Account-ID>:key/*"



],



"Condition": {



"StringEquals": {



"aws:ResourceTag/dt:CreatedBy": "Dynatrace"



}



}



},



{



"Sid": "kms3",



"Effect": "Allow",



"Action": [



"kms:CreateAlias",



"kms:DeleteAlias",



"kms:UpdateAlias"



],



"Resource": "arn:aws:kms:<Deployment-Region>:<AWS-Account-ID>:alias/dynatrace/*/keys/aws/integration/*"



},



{



"Sid": "logs0",



"Effect": "Allow",



"Action": [



"logs:DescribeLogGroups"



],



"Resource": "*"



},



{



"Sid": "logs1",



"Effect": "Allow",



"Action": [



"logs:DeleteLogGroup",



"logs:CreateLogGroup",



"logs:DeleteLogStream",



"logs:CreateLogStream",



"logs:DescribeLogStreams",



"logs:PutRetentionPolicy",



"logs:ListTagsForResource",



"logs:DescribeIndexPolicies",



"logs:AssociateKmsKey",



"logs:DisassociateKmsKey",



"logs:PutLogEvents",



"logs:TagResource"



],



"Resource": [



"arn:aws:logs:<Deployment-Region>:<AWS-Account-ID>:log-group:/aws/lambda/<Deployment-Stack-Name-Prefix>*",



"arn:aws:logs:<Deployment-Region>:<AWS-Account-ID>:log-group:/aws/lambda/DynatraceApiClientFunction-*"



]



}



]



}
```

At this point all, the AWS IAM baseline prerequisites have been completed. Keep in mind that the IAM role/user permissions are needed for each onboarded AWS account.

We recommend that an AWS administrator pre-create those IAM constructs programmatically.

### 2. Create the Dynatrace IAM baseline



Actions in this section can and (should) only be performed by the Dynatrace account administrator.

The new AWS Platform Monitoring has been integrated with the core Dynatrace Identity and Access Management (IAM) design.

Learn more about the basic concepts:

* [Users, service users](/docs/manage/identity-access-management/user-and-group-management/identity-concepts#users "Understand the key identity concepts in Dynatrace IAM")
* [Local groups, policies](/docs/manage/identity-access-management/user-and-group-management/access-group-management "Manage Dynatrace groups and their permissions.")
* [Platform tokens for service users](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens#allow-users-to-generate-platform-tokens-against-service-users "Create personalised platform tokens to access Dynatrace services via the API in your user context.")

In this documentation section context:

Dynatrace account admin
:   A built-in [user](/docs/manage/identity-access-management/use-cases/access-platform#who "Grant access to Dynatrace") with `View and manage users and groups` permission.

CloudsAdmins
:   A customer-created custom IAM group where its members will be able to create and manage AWS connections in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

CloudAdmin
:   An IAM user, member of the `CloudsAdmins` group. The name is used here solely for context; any Dynatrace IAM user can be used.

Service user
:   A non-interactive IAM identity, against which platform tokens will be created.

Platform token
:   The authentication and authorization secrets used to establish a secure communication with the Dynatrace APIs.
    In our context, two platform tokens are to be created:

    * `Settings PT`âallows the creation and managment of an AWS connection.
    * `Ingest PT`âallows the programmatic ingest of push-based telemetry from AWS.

Data-Acquisition AWS Integration App
:   A Dynatrace-created built-in IAM policy which contains all the (least privilege) permission scopes required to support the creation and management of an AWS connection from ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**. When using the new connection wizard, it will automatically create a new service user and linked platform tokens. It will also bind all required permissions to allow connection creation and management, and telemetry ingest from AWS (Firehose Logs and EventBridge Events).

#### Interactive IAM identity (IAM user)

1. [Create](/docs/manage/identity-access-management/user-and-group-management/access-group-management#account-management "Manage Dynatrace groups and their permissions.") the `CloudsAdmins` group.

   Once the `CloudsAdmins` group is created, select  **Permissions** > **Scope** and add the `Data-Acquisition AWS Integration App` and `Standard User` policies.

   Apply **Account-Wide** or **Environment-Wide**, then select **Save**.

   Validate: The `CloudsAdmins` **Permissions** section should show:

   * `Data-Acquisition AWS Integration App`
   * `Standard User`
2. [Assign](/docs/manage/identity-access-management/user-and-group-management/access-user-management#edit-existing-user "User management") your CloudAdmin IAM user (or any other Dynatrace IAM user) as a member of the `CloudsAdmins` group.

## Onboarding

Before you start, make sure all [prerequisites](#prerequisites) are completed.

1. Log in to Dynatrace as the IAM user (member of the `CloudsAdmins` IAM group) and open ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. Go to **Collect and capture** > **Cloud and virtualization** > **AWS** and select  **New connection**.

If the button is grayed out, it means you do not have the proper permissions to create a connection. Please, contact your administrator.

### 1. Select connection model

1. Enter a friendly connection name that is unique (for example, `MyEastProd3Account`).
2. Enter the **AWS Account ID** where you intend to deploy the connection.
3. Choose the **Deployment region**.

   The deployment region is the AWS Region from which the CloudFormation stack will be deployed.

   If you plan to use the event ingest option, make sure to select a deployment region that supports [EventBridge API destinationsï»¿](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html#feature-availability-apid).
4. Select **Next**.

### 2. Select observability option

1. Choose the **Recommended** observability path. Two paths are currently supported:

   * **Recommended**: The monitoring configuration is an opinionated (immutable) option, only monitored Regions are customizable. Per AWS member account, this flow provides:

     + AWS account resources inventory using ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** (for supported AWS services).
     + AWS account resources topology, depicted as rich resource entities using ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** (for supported AWS services).
     + Amazon CloudWatch API metric polling (per enabled region) for our recommended services (automatically opted-in).
     + The Regions that were selected, allowing the AWS administrator to deploy Amazon Data Firehose streams for logs ingest as stacksets on the AWS Organizations Console.
   * **Advanced**: The most [fine-grained path](/docs/ingest-from/amazon-web-services/manage-aws-connections#customize "Find out how to manage your AWS connections.") monitoring configuration. Allows the full customization any monitoring setting to meet advanced use cases.

   Regardless of the selected path, customizing all the supported monitoring settings is possible post-onboarding.

   The topology signal is an auto-enabled signal; you can't disable it.
2. Choose the monitored **AWS Regions** you want to monitor.

   The monitored regions are the AWS Regions in which Dynatrace can securely poll metrics, topology and push logs from.

   You need to enable `us-east-1` regardless of your desired monitored regions, since global AWS resources reside in `us-east-1`.
3. Select **Next**.

After a successful onboarding, you'll be able to customize monitored AWS Regions and all other supported monitoring settings, per AWS member account.

### 3. Get platform tokens for service users

1. Generate the settings and ingest tokens. Alternatively, you may also paste pre-existing tokens.
2. Select **Download** and **Next**.

   If the download button is grayed out, that means that the Dynatrace token fields are not populated with platform tokens.

### 4. Finalize

1. Go to the AWS Console and log in to the designated AWS account with an AWS IAM user that has all the needed permissions to deploy the CloudFormation stacks.
2. Select **Deploy the CloudFormation in AWS Console**.

If you practice roles duty separation, the Dynatrace admin may have no access/permissions to the AWS environment.

In this case, select the **Copy Deployment Link**.

Share this deeplink and the downloaded platform tokens CSV file with your platform team and/or AWS Admins.

This will allow them to deploy the CloudFormation stack with the wizard configurations that you have set.

3. Copy the settings and ingest tokens from the downloaded CSV file (the file name will follow the connection friendly name) and paste them into the corresponding CloudFormation parameters (settings token, ingest token).
4. Deploy the stack.
5. When the CloudFormation stacks deployment finishes successfully (which can take up to 15 minutes), go back to the wizard and confirm.

If the CloudFormation stack deployment failed, see [Troubleshooting](#troubleshooting).

### 5. Configure Health alerts and Warning signalsOptional

You can configure Health alerts and Warning signals now or [later](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app#alerting "Monitor all cloud platforms at once.").

Health alerts and warning signals help you monitor your infrastructure by providing clear, actionable insights. These features reduce the noise from infrastructure issues and improve alerting capabilities, so you can focus on what matters most. This is achieved through better categorization of detected malfunctions.

* For critical events, a Health alert is raised, triggering a [Dynatrace Problems](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") investigation.
* For non-critical situations, a Warning signal informs you of a potential challenge.

Successful onboarding involves two elements:

* In ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization** > **AWS**, the new AWS connection is `Healthy`.
* In the AWS CloudFormation console, the CloudFormation stacks are in `CREATE_COMPLETE` status.

## What's next?

* Go to [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once."). AWS resources with telemetry should start to appear shortly.
* See [Manage your AWS connections](/docs/ingest-from/amazon-web-services/manage-aws-connections "Find out how to manage your AWS connections.") to learn how to manage your newly created connection.
* Configure [CloudWatch log group subscriptions](/docs/ingest-from/amazon-web-services/ingest-telemetry/cloudwatch-logs-private-preview/aws-subscribe-log-groups-pp "Find out how to configure AWS log groups to be ingested into Dynatrace.").

## Troubleshooting



The New connection functionality is disabled. When I hover on it, I see a message that I don't have the permissions.

Make sure that your Dynatrace IAM user has the proper permission scopes to create and manage a connection. For details, see the [Create the Dynatrace IAM baseline](#iam-baseline) section.

The CloudFormation stack did not complete successfully. How do I troubleshoot for the root cause?

If your CloudFormation deployment fails, it's often related to a lack of AWS IAM permissions, AWS Service limits being reached, or Service Control Policies configured in your AWS Organizations.

To run our troubleshooting helper script to discover the root cause

1. Open AWS CloudShell in the **AWS Management Console**.

   Alternatively, you can run bash with AWS CLI installed.
2. Download the script:

   ```
   wget -q https://dynatrace-data-acquisition.s3.us-east-1.amazonaws.com/aws/deployment/cfn/da-activation-check.sh -O da-activation-check.sh && chmod +x ./da-activation-check.sh
   ```
3. Run the script to analyze the failure reason and script output `./da-activation-check.sh --stack-name <activation-stack-name>`.

   The activation main stack name follows the AWS connection name specified the Dynatrace connections list, for example, connection name: `MyEastProd3Account`

To find the failure reason manually

1. Go to the **AWS Management Console** > **CloudFormation** stack events and search for the root cause.
2. Also search nested stacks and stackset instances (if logs/events ingest was enabled) for failed events.

If you encounter an error that you cannot resolve on your own, [open a Dynatrace support ticketï»¿](https://www.dynatrace.com/services-support/dynatrace-one/) providing the script output.

The root cause of the CloudFormation deployment failure is an invalid or expired token. What can I do?

The best way to solve this issue is to delete the failed stack and repeat the deployment specifying valid tokens as parameters. You can start the deployment from the Dynatrace ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** web UI to generate a new API token.

The root cause of the CloudFormation deployment failures are related to permissions, as I can see messages indicating that I'm not authorized to perform X or Y. What can I do?

If you can see in the CloudFormation stack error messages, such as `"User: arn:aws: <...> is not authorized to perform: <...> on resource: <...>"`, it's because you haven't included the proper user/role permissions required from our policy. Update the setup by adding the required [AWS permissions](#aws-permissions), clean the current setup, and restart the process.

To learn how to clean the current setup, see [The CloudFormation stack did not complete successfully. I fixed the issue. How do I clean the current setup and start over?](#clean-setup)

The root cause of the CloudFormation deployment failure is that the 'Account XXX has not enabled 'Region-XYZ'. What can I do?

If you see, in the CloudFormation stack, error messages such as `"Account XXX has not enabled [Region-XYZ]: ..."`, clean the current setup, enable that Region or remove it from the deployment parameters, and restart the process.

To learn how to clean the current setup, see [The CloudFormation stack did not complete successfully. I fixed the issue. How do I clean the current setup and start over?](#clean-setup)

The root cause of the CloudFormation deployment failure is the creation of the Firehose DeliveryStream. What can I do?

If you see, in the CloudFormation stack, error messages such as `"You are not subscribed to this service"` or `"The AWS Access key Id needs a subscription for the service (Service Firehose)"`, this is because new services, such as Firehose, require it to be enabled on some new accounts. See [how to resolve problems when accessing a service in the AWS Management Consoleï»¿](https://repost.aws/knowledge-center/error-access-service).

After enabling it, clean the current setup and restart the process again.

To learn how to clean the current setup, see [The CloudFormation stack did not complete successfully. I fixed the issue. How do I clean the current setup and start over?](#clean-setup)

The root causes of the CloudFormation deployment failures are 404 or 400 errors. What can I do?

Please contact us at `awscloudmonitoring-preview@dynatrace.com` or open a Dynatrace support ticket sharing the errors you experienced.

The CloudFormation stack did not complete successfully. I fixed the issue. How do I clean the current setup and start over?

In the AWS CloudFormation console, delete the master Dynatrace stack. The main stack name follows the connection name in our example `MyEastProd3Account`. Follow the AWS [guidelines on deleting stacksï»¿](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html).

Once the stack and its nested stacks are completely deleted

1. In Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Cloud and virtualization** > **AWS (Preview)**.
2. Find and select the connection action menu on the right .
3. Select **Delete**.
4. You are now able to start the wizard and create a new connection.

Not all resources created are properly tagged in Dynatrace.

Even if your organization enforces tagging via Service Control Policies or IAM, some of the resources created by CloudFormation do not support tag propagation. For details, please see [AWS CloudFormation resource taggingï»¿](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).

I have enabled logs push-based ingest via Firehose, but I cannot seem to locate log records on Dynatrace.

Looking at the **Destination error logs** tab (AWS Firehose console), if you get this message:

`Delivery to the endpoint was unsuccessful. See Troubleshooting HTTP Endpoints in the Firehose documentation for more information. Response received with status code. 403: "requestId":"xxxx,"errorMessage":"The authorization token does not provide the necessary permissions. details: missing_scopes=[data-acquisition:logs:ingest]`

Verify that

1. The platform ingest token is assigned with the correct permission scope (`data-acquisition:logs:ingest`).
2. The Dynatrace service user linked to the token is also assigned with same token permission scope (`data-acquisition:logs:ingest`).
3. The platform ingest token has not expired or was deleted.
4. The service user has not been deleted.
5. The platform token environment scope is adjusted to the correct Dynatrace environment.

When creating the platform token, why is the "service user" option grayed out?

Your IAM user might not have permission to create platform tokens for (existing) service users. Contact you Dynatrace Admin to learn if the [prerequisites](#prerequisitesuisites) were followed. In this case, a [specific permission scope must be granted](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens#allow-users-to-generate-platform-tokens-against-service-users "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

## Share your feedback

The onboarding experience is an evolving core product feature. We are continually working to collect feedback.

During the Preview, we will reach out and ask for feedback. We highly appreciate your willingness to share any suggestions.
You can also share your feedback at our [dedicated Dynatrace Community channelï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-new-Cloud-Platform-Monitoring-PREVIEWS/m-p/286886/thread-id/4853#M4853)