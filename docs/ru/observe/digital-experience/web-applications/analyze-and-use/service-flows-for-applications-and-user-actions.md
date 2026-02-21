---
title: Service flows for applications and user actions
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions
scraped: 2026-02-21T21:12:29.753545
---

# Service flows for applications and user actions

# Service flows for applications and user actions

* How-to guide
* 1-min read
* Published Oct 04, 2017

Dynatrace enables you to easily grasp the service flow chain within the context of your application and even within the context of individual user actions. [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") shows you which services are called by each application or individual user action and helps you understand how these services call each other.

## Access service flow for an application

To access the service flow for an application

1. Go to **Web**.
2. Select the application you want to analyze.
3. Select the **Services** tile in the lower-right corner of the Performance analysis infographic.
4. Within the **Called services** section below, select **View service flow**.

   ![Serviceflow app 1](https://dt-cdn.net/images/01-serviceflow-app-1607-f0becdb963.png)

   ![Serviceflow app 2](https://dt-cdn.net/images/02-serviceflow-app-1434-ec6bb8c89f.png)

## Access service flow for a user action

To access the service flow for a user action

1. Go to **Web**.
2. Select the application that includes the user action you want to analyze.
3. Scroll down to the **Top 3 user actions** section, and select **View full details**.
4. On the **User actions** page, select the user action you want to analyze from the **Top 100 user actions** or the **Key user actions** lists.
5. On the **User action** page, scroll down to the **Top 3 web request contributors** section, and select **View full details**.
6. Select **View service flow**.

   ![Useraction serviceflow 1](https://dt-cdn.net/images/01-useraction-serviceflow-1607-63b0e6352a.png)

   ![Useraction serviceflow 2](https://dt-cdn.net/images/02-useraction-serviceflow-1613-8fcb6f87cc.png)