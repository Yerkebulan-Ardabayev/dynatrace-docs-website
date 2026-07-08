---
title: Push notifications via the Dynatrace mobile app
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app
---

# Push notifications via the Dynatrace mobile app

# Push notifications via the Dynatrace mobile app

* 8-min read
* Updated on Jan 14, 2026

Dynatrace provides multiple channels for receiving alerts about detected problems in your environment. Besides traditional methods like email, Dynatrace integrates directly with popular third-party services such as Slack, Jira, and Opsgenie. Additionally, you can receive alerts via the Dynatrace mobile app.

Sunsetting native mobile apps (iOS & Android) for Dynatrace

As part of our ongoing commitment to delivering a streamlined and consistent user experience, Dynatrace is retiring its native mobile applications for iOS and Android. This change aligns with our strategy to provide a unified, responsive web interface and leverage modern, flexible notification channels.

#### Key dates

* **Last app update**: End of 2025
* **Sunset date**: June 30, 2026
* **Support ends**: June 30, 2026

#### What’s changing

The Dynatrace native mobile apps will no longer be available for download or supported after the sunset date.

We encourage you to access Dynatrace via the responsive web interface, which offers full functionality across all device types and screen sizes.

Push notifications will now be delivered through third-party integrations such as Slack, Teams, PagerDuty, email, and ntfy.

#### Why this change?

* **Unified experience**: A single responsive web platform ensures consistent functionality across all devices.
* **Flexibility**: You can choose your preferred communication tools for alerts and updates.

#### Recommended actions

* Begin using the responsive web interface.
* Set up your preferred notification integrations via:

  + Dynatrace SaaS: [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
  + Dynatrace Managed: [Problem notifications](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.")
* Remove the native app from your devices after the sunset date.

#### Need help?

For assistance with transitioning or setting up integrations, please see the Documentation links above or contact Support.

The rest of this page refers to the Dynatrace mobile app, which has a sunset date of June 30, 2026. See above for details.

The Dynatrace mobile app is available for [iOS﻿](https://dt-url.net/ue02yx1) and [Android﻿](https://dt-url.net/uf22yp6) devices. Its primary function is to deliver push notifications for issues detected within your monitoring environments. Notifications are fetched and updated in real-time, ensuring you stay informed about ongoing problems. This makes the mobile app a convenient and efficient way to manage alerts and monitor your environments when you're on the go.

Push notifications for each environment are filtered based on the management zones for which the user has at least read permissions. If a user lacks read permissions for a specific management zone, no push notifications will be sent for that zone.

In addition to the management zone filter for individual users, push notifications are also filtered by the environment’s **Default alerting profile**. Modifying the **Default alerting profile** affects all problem push notifications sent to all users within the environment.

**Key Features**

* Real-time alerts: Receive immediate push notifications for detected issues.
* Multi-environment support: Monitor multiple Dynatrace environments from a single app.
* Compatibility: Supports push notifications from Dynatrace SaaS and Dynatrace Managed environments.

## Aim and context

This guide shows how to use the Dynatrace mobile app to receive push notifications on detected problems within your monitoring environments.

## Target audience

This guide is written for:

* Operations engineers
* Pipeline engineers
* Systems engineers
* Site reliability engineers (SREs)
* Build automation engineers

## Prerequisites

### Android

* Android 9.0+
* [Dynatrace mobile app for Android﻿](https://dt-url.net/uf22yp6) installed on your mobile device. Ensure that the device has permanent access to the Internet.

### iOS

* iOS 16+
* [Dynatrace mobile app for iOS﻿](https://dt-url.net/ue02yx1) installed on your mobile device. Ensure that the device has permanent access to the Internet.

### Network

* If your Dynatrace Managed server is running behind a corporate firewall, you need to set up a Cluster ActiveGate that is **accessible from the internet**. The Cluster ActiveGate serves the REST API required for the mobile app. For more information on routing OneAgent traffic to Dynatrace, see [Route OneAgent traffic to Dynatrace, monitor cloud environments and remote technologies using extensions](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.").
* Your firewall must allow incoming network connections to the configured Cluster ActiveGate domain on the configured port.
* If there's a firewall in front of the Cluster ActiveGate, it must send the correct security certificates.
* Use the [DigiCert checker﻿](https://www.digicert.com/help/) to verify that the certificate of your publicly accessible ActiveGate passes all validation checks. iOS and Android block unsecured communication requests without a valid domain certificate.

## Mobile app API access token

The mobile app uses an API access token with the **Mobile** (`mobile`) scope assigned to it. To review the token, go to [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Explore Dynatrace Managed, including navigation, browser requirements, timeframe selection, metric notation, and accessibility.") > **Personal Access Tokens**.

## Dynatrace mobile app communication with Dynatrace Managed

There's a two-way comunication between Dynatrace Cluster and the mobile app.

1. The Dynatrace Managed cluster pushes minimal information (only the problem title and ID) through [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.").
2. Your mobile app can then fetch all detailed problem information on demand. Just select a notification to fetch updated information about a problem.

To access the problem details API, you need to install a [publicly accessible ActiveGate](/managed/managed-cluster/basics/managed-deployments#scenario-2-pure-dynatrace-managed-setup "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture."). Access is secured by the automatically generated user-specific API token mentioned above. This token is restricted to the mobile app API and can't be used for other API calls or to log into the cluster.

The following diagram illustrates how push notifications are sent out to your iOS and Android mobile devices and how problem details are fetched on demand.

![Dynatrace mobile app communication diagram](https://dt-cdn.net/images/dynatrace-mobile-app4-1058-9837cd4684.png)

Dynatrace mobile app communication diagram

## Start using

### Step 1 Log in to mobile app

1. In your Managed Environment, go to the user account menu in the upper-right corner and select **Receive alerts via mobile app**.
2. In the Dynatrace mobile app, select **Connect Managed Environment** to scan the generated QR code of your environment.

   Each time you reload or revisit the account menu QR code page, the previous code is deleted, a new code is created, and you need to reconnect the mobile app.

### Step 2 Display problems and vulnerabilities

The Dynatrace mobile app displays all connected environments and highlights the total number of active problems and vulnerabilities for each with a red indicator. This global indicator assists operations teams in prioritizing environments that have active issues.

![Dynatrace mobile app environment list](https://dt-cdn.net/images/mobile-app-env-list-600-0921471e08.png)

Dynatrace mobile app environment list

### Step 3 View problem details

The **Problems** list shows all active and closed problems within a specified period.

You can use the problem filter to

* Adjust the timeframe
* Filter by status, severity, or impact level
* Select a management zone.

  Note that only management zones loaded through the first page of problems are available in the management zone filter.

![Dynatrace mobile app problem list](https://dt-cdn.net/images/mobile-app-problem-list-600-266735348f.png)

Dynatrace mobile app problem list

Select a problem to see a summary of the issue and details about all events collected during the analysis of the problem.

![Dynatrace mobile app problem details](https://dt-cdn.net/images/mobile-app-problem-600-2935163498.png)

Dynatrace mobile app problem details

* **Show in Webview**—Available only in the Android version, as Apple store policies do not allow embedded Web links within native iOS apps.
* **View all**—Expands the entire affected topology for large problems.

### Step 4 View vulnerability details

The list of vulnerabilities within the app allows your security team to quickly review all the detected security vulnerabilities within your environments.

Each of these vulnerabilities shows its [Dynatrace Security Score (DSS)](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.") along with the number of affected entities and its Common Vulnerabilities and Exposures (CVE) number.

* To search, select **CVE ID**, **External ID**, or **Component** and then enter the search string.
* To change the sort order, select **Sorted by time** or **Sorted by DSS**.

![Dynatrace mobile app vulnerability list](https://dt-cdn.net/images/mobile-app-vulnerabilities-list-600-c86d309d03.png)

Dynatrace mobile app vulnerability list

Select a vulnerability to show details such as a risk assessment, information on the affected software stack, and a description of the vulnerability.

![Dynatrace mobile app vulnerability](https://dt-cdn.net/images/mobile-app-vulnerability-600-d347e53711.png)

Dynatrace mobile app vulnerability

### Step 5 Receive push notification

After you're logged into the Dynatrace, push notifications are received for all newly detected problems within all the connected environments.

Within the mobile app settings, you can disable or enable push notifications per environment.

All push notifications are filtered by the management zones for which you have at least viewer permissions.

To receive push notifications, you need the `View environment` permission assigned to your user as a role. Note that policy-based assignments are currently not supported for the mobile app.

If you don't receive push notifications:

* Verify that you have the right permissions for the environment and for the specific management zone in which the problem was detected.
* Verify that the Dynatrace mobile app has the necessary Android and iOS permissions to receive push notifications.
* Log out and in again to retry the push notification registration at the push notification provider.