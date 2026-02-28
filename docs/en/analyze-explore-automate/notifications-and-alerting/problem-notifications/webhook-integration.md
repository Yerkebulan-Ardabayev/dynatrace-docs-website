---
title: Send Dynatrace notifications via webhooks
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration
scraped: 2026-02-28T21:07:23.272197
---

# Send Dynatrace notifications via webhooks

# Send Dynatrace notifications via webhooks

* 3-min read
* Updated on Sep 11, 2024

Dynatrace offers several out-of-the-box integrations that automatically push problem notifications to third-party incident-management and ChatOps systems.
If however your third-party system isn't supported with an out-of-the-box integration, you can easily set up a customizable webhook integration. Using this approach, whenever Dynatrace detects a problem in your environment that affects real users, a webhook triggers an `HTTP POST` request to a target URL that you specify.

The payload message of the `HTTP POST` request is completely customizable. By default, requests use valid JSON syntaxâexcept when you define a different HTTP content type header, in which case you define a different HTTP content type header and Dynatrace skips the JSON validation and doesn't escape the payload based on JSON syntax.

Information placeholders, such as **{ProblemTitle}** and **{State}**, are used to fill the custom JSON with the dynamic information of each detected problem.

To integrate problem-notifications using a custom webhook:

1. Go to **Settings Classic** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Custom integration** from the available notification types.
4. Configure the notification:

   * **Display name**  
     This is the freeform name of this integration that will be displayed in Dynatrace on **Settings Classic** > **Integration** > **Problem notifications** when you finish this configuration.
   * Optional Turn on **Secret webhook URL**.
     Turn on this option to obfuscate the webhook URL (the webhook endpoint) in the notification settings, providing an additional layer of security by hiding sensitive information from display.
   * **Webhook URL**  
     Target URL where the **HTTP POST** should push the payload. This URL can contain HTTP parameters such as an authentication token, in case the destination system works with authentication tokens instead of basic authentication.
   * Optional **Additional HTTP headers**  
     Specify additional HTTP header fields, such as 'Content-Type' or 'Authorization'. These custom HTTP header fields can be used if the target endpoint needs an authentication token within the HTTP header or if you would like to send different content type such as 'text/plain' or 'application/xml'.
   * **Custom payload**  
     Once a problem is detected or resolved, this customizable payload is pushed through an **HTTP POST** to the target system.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with problem-related information such as problem state or title.
   * Optional Turn on **Accept any SSL certificate**.
   * Optional Turn on **Call webhook if new events merge into existing problems**.
   * Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
5. Select **Send test notification** to make sure your webhook integration is working.
6. **Save changes**.

## Example JSON with placeholders

Here is a valid JSON web hook problem-notification definition example:

```
{



"ImpactedEntities": {ImpactedEntities},



"ImpactedEntity": "{ImpactedEntity}",



"PID": "{PID}",



"ProblemDetailsHTML": "{ProblemDetailsHTML}",



"ProblemDetailsJSON": {ProblemDetailsJSON},



"ProblemID": "{ProblemID}",



"ProblemImpact": "{ProblemImpact}",



"ProblemTitle": "{ProblemTitle}",



"Problem URL": "https://example.com",



"State": "{State}",



"Tags": "{Tags}"



}
```

`{ImpactedEntities}` and `{ProblemDetailsJSON}` are JSON data types and must not have quotes around them.

After a problem has been detected, the placeholders are populated with the actual values and results, as shown in this example payload:

```
{



"ImpactedEntities": [



{"type": "HOST", "name": "MyHost1", "entity": "HOST-XXXXXXXXXXXXX" },



{"type": "SERVICE", "name": "MyService1", "entity": "SERVICE-XXXXXXXXXXXXX"}



],



"ImpactedEntity": "MyHost1, MyService1",



"PID": "99999",



"ProblemDetailsHTML": "<h1>Dynatrace problem notification test run details</h1>",



"ProblemDetailsJSON": {"ID" : "99999" },



"ProblemID": "999",



"ProblemImpact": "INFRASTRUCTURE",



"ProblemTitle": "Dynatrace problem notification test run",



"Problem URL": "https://example.com",



"State": "OPEN",



"Tags": "testtag1, testtag2"



}
```