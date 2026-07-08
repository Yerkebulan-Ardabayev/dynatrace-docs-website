---
title: Create a new request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule
---

# Create a new request naming rule

# Create a new request naming rule

* Reference
* Published Mar 05, 2019

This use case shows you how to use the **Request naming** API to create a new request naming rule.

Service request naming enables you to consolidate or refine requests across multiple services. Additionally, you can synchronize these rules across multiple Dynatrace environments.

Let's assume we have two requests from Drupal (the open-source CMS) named `/node/1` and `/node/1/edit`. The last parts of both names (`/1` and `/1/edit`) don't carry any valuable information. We can remove those parts and consolidate the two separate requests into one named `/node`. To achieve this, we need a request naming rule to rename every request where the URL **begins with** `/node` into simply `/node`, thereby consolidating them.

The configuration for such a rule looks like this:

```
{



"enabled": true,



"namingPattern": "/node",



"conditions": [



{



"attribute": "WEBREQUEST_URL_PATH",



"comparisonInfo": {



"type": "STRING",



"comparison": "BEGINS_WITH",



"value": "/node",



"negate": false,



"isCaseSensitive": false



}



}



],



"placeholders": []



}
```

The important components are:

* **conditions**—defines which requests will be renamed.
* **namingPattern**—defines the resulting name.

You can find descriptions of other fields in the **Parameters** section of the [**POST a new request naming rule** topic](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Create a request naming rule via the Dynatrace API.").

Now let's submit this configuration in an API call. How you execute REST calls is up to you—you can use any REST client or you can write a script like the one provided below. You can also use the Dynatrace [API Explorer](/managed/dynatrace-api#api-explorer "Find out what you need to use the Dynatrace API.") to familiarize yourself with endpoints and execute all the required requests.

REST client

Dynatrace API Explorer

1. Generate a new [access token for the Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API."). Be sure to assign **Read configuration** and **Write configuration** scopes to it.
2. Execute the [**POST a new request naming rule** request](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Create a request naming rule via the Dynatrace API.") with the token you created in the first step and the JSON configuration of the request naming rule from an example above as a payload.

1. Generate a new [access token for the Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API."). Be sure to assign **Read configuration** and **Write configuration** scopes to it.
2. Open the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Explore Dynatrace Managed, including navigation, browser requirements, timeframe selection, metric notation, and accessibility.") from the previous Dynatrace web UI, and select **Dynatrace API > Configuration API**.

   ![Access API explorer](https://dt-cdn.net/images/mz-1-1313-ec4939b8c8.png)

   Access API explorer
3. In the API Explorer, select **Authorize**.  
   The **Available authorizations** dialog appears.
4. Paste your token into the **ReadConfigToken** and **WriteConfigToken** fields and select **Authorize**.
5. Expand the **POST /service/requestNaming/** request and select **Try it out**.

   ![Try it out](https://dt-cdn.net/images/create-rnr-1-1460-fa51d43874.png)

   Try it out
6. Paste the JSON configuration of the request naming rule (see above) into the **body** field and select **Execute**.

   ![The payload](https://dt-cdn.net/images/create-rnr-2-1441-10b7c61eb9.png)

   The payload
7. A successful request returns the **201** code and a short representation of the request naming rule.

   ![Successful request](https://dt-cdn.net/images/create-rnr-3-1346-7baeb4f45b.png)

   Successful request

## Related topics

* [Set up request naming](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")