---
title: AWS Marketplace private offer
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/aws-platform/aws-marketplace
scraped: 2026-02-20T21:24:02.306386
---

# AWS Marketplace private offer

# AWS Marketplace private offer

* How-to guide
* 3-min read
* Published May 26, 2025

The Dynatrace Platform Service can be licensed via the [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-si2angoettdnc?applicationId=AWSMPContessa) according to a private offer.

This page describes how to link your private offer with a Dynatrace environment.
You can either link an existing Dynatrace environment that was created with AWS, or create and link a new environment.

If you do not yet have a private offer, reach out to Dynatrace sales at [sales@dynatrace.com](mailto:sales@dynatrace.com).

## Key terms

Private offer
:   A customer-specific license proposal that has been prepared by Dynatrace. It includes a custom [rate cardï»¿](https://www.dynatrace.com/pricing/rate-card) with the agreed-upon capabilities and prices.

Public cloud service
:   Computing services offered by a third-party provider. Dynatrace can be licensed via a public cloud service.

Dynatrace environment
:   A [Dynatrace environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") is where all your Dynatrace performance analysis takes place. Environments have a unique identifier in the format `abc12345`.

## Prerequisites

* You already have a customized private offer for Dynatrace in the AWS Marketplace.
* If you are linking an existing Dynatrace account, your Dynatrace user needs to have the **View and manage account billing information** permissions for that account.

## Steps

Follow the steps below to link your private offer to a Dynatrace account.

Link an existing Dynatrace account

Create a new Dynatrace account to link

If you already have an existing Dynatrace account and environment on AWS, follow the steps below to link the account to your AWS Marketplace private offer.
This can be either a trial or production environment, as long as it is in an active state.

1. In AWS Marketplace, open your Dynatrace private offer.
2. Accept your Dynatrace private offer.
3. Select **Set up your account**.
4. On the **Welcome to your new Dynatrace Platform Subscription** page, select **Link existing account**.
5. Sign in as the Dynatrace user that is assigned to the account you want to link.

   1. Enter the email address, then select **Next**.
   2. Enter the account password, then select **Next**.
6. Depending on how many accounts the user is assigned to, do one of the following:

   * One account: The account is recognized automatically and you can continue to the next step.
   * Multiple accounts: In the **Account to link** drop-down menu, select the specific account that you want to link this private offer to.
     Then, continue to the next step.
   * More than 20 accounts: In the **Account UUID** field, specify the Account UUID from the account that you want to link this private offer to.
     Then, continue to the next step.

     To get your Account UUID, go to **Account Management** and copy the UUID from the URL of the address field of your browser.
7. Once you've signed in with the chosen account, your account information is displayed in **User details**, **Account details**, and **Environments**.
   This is the account that will be linked to your private offer, so verify the details are correct.
8. Select the check box next to **I agree to link this Dynatrace account with my marketplace subscription.**, then select **Next**.

   This step cannot be undone.

When the **Congratulations!** window appears, your private offer is now linked to the chosen Dynatrace account.

Your subscription information in **Account Management** will reflect the fully-credited new license within three days.
In the meantime, you can start using your Dynatrace environment according to the account's existing license (if you linked an existing account) or with a trial license (if you created a new account).

Select **Open Dynatrace** to start using Dynatrace and [Set up Dynatrace on Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.").

If you don't yet have a Dynatrace account, follow the steps below to create an account and link it to your AWS Marketplace private offer.

1. In AWS Marketplace, open your Dynatrace private offer.
2. Accept your Dynatrace private offer.
3. Select **Set up your account**.
4. On the **Welcome to your new Dynatrace Platform Subscription** page, select **Create a new account**.
5. Enter the required information as described on the page:

   1. **User details**
   2. **Account details**
   3. **Environment details**
6. Select **Create account**.

A **You're almost done!** window appears.
Dynatrace creates a new account and environment according to the information that you have entered.
This step may take up to 5 minutes to complete.

When the account is successfully created, a **Congratulations!** window appears.
Your private offer is now linked to the Dynatrace account that you just created.

Your subscription information in **Account Management** will reflect the fully-credited new license within three days.
In the meantime, you can start using your Dynatrace environment according to the account's existing license (if you linked an existing account) or with a trial license (if you created a new account).

Select **Open Dynatrace** to start using Dynatrace and [Set up Dynatrace on Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.").

## Related topics

* [Discover Dynatrace](/docs/discover-dynatrace "Discover Dynatrace")