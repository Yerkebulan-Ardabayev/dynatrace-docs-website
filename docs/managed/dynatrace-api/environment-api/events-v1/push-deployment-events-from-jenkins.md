---
title: Push deployment events from Jenkins
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1/push-deployment-events-from-jenkins
scraped: 2026-05-12T12:13:37.847230
---

# Push deployment events from Jenkins

# Push deployment events from Jenkins

* Reference
* Updated on Jun 13, 2022
* Deprecated

To configure Jenkins to push deployment events to Dynatrace.

1. Generate a new [access token for the Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").
2. Install the [HTTP Request Pluginï»¿](https://dt-url.net/3g23u1a) to your Jenkins installation.
3. In the Jenkins build configuration, click **Add build step** and select **HTTP Request**.

![Jenkins - add HTTP Request as build step](https://dt-cdn.net/images/jenkins-build-addbuildstep-httprequest-2-333-fec9e1de4a.png)

Jenkins - add HTTP Request as build step

4. In the **URL** field, type in the URL of your event API endpoint:

   * Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/events/
   * Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/events/
   * Environment ActiveGate https://{your-activegate-domain}/e/{your-environment-id}/api/v1/events
5. Select **POST** as the **HTTP mode**.
6. Click **Advanced** to see all the configuration fields.

![Jenkins - HTTP Request configuration](https://dt-cdn.net/images/jenkins-httprequest-1433-c9422103f1.png)

Jenkins - HTTP Request configuration

7. In the **Headers** section, select **APPLICATION\_JSON** in the field **Accept** .
8. Select **APPLICATION\_JSON** in the field **Content-type**.
9. Add a **Custom header**, type in **Authorization** in the **Header** field and **Api-Token {token}** in the **Value** field.

![Jenkins - Headers configuration](https://dt-cdn.net/images/jenkins-headers-1417-ef4687d080.png)

Jenkins - Headers configuration

10. Copy and adapt as needed the following payload into the **Request body** field. For more details on the payload fields, see [POST events](/managed/dynatrace-api/environment-api/events-v1/post-event "Create a custom event via the Dynatrace API.").

```
{



"eventType": "CUSTOM_DEPLOYMENT",



"attachRules": {



"tagRule": {



"meTypes": "PROCESS_GROUP_INSTANCE",



"tags": "Dev"



}



},



"deploymentName": "${JOB_NAME}",



"deploymentVersion": "1.1",



"deploymentProject": "CustomBankingService",



"remediationAction": "http://revertMe",



"ciBackLink": "${BUILD_URL}",



"source": "Jenkins",



"customProperties": {



"Jenkins Build Number": "${BUILD_ID}",



"Git commit": "${GIT_COMMIT}"



}



}
```

`${JOB_NAME}`, `${BUILD_URL}`, `${BUILD_ID}`, `${GIT_COMMIT}` are [environment variables set by Jenkinsï»¿](https://dt-url.net/x803uzw) during job execution.

11. Save the build configuration. Next time you build your project, the deployment event will be pushed to the monitored entities (for example, hosts and services) you have defined in the `tagRule` of the request body.