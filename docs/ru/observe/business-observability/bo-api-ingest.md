---
title: Ingest business events via API
source: https://www.dynatrace.com/docs/observe/business-observability/bo-api-ingest
scraped: 2026-02-18T21:24:25.657737
---

# Ingest business events via API

# Ingest business events via API

* Latest Dynatrace
* Reference
* 11-min read
* Updated on Aug 20, 2025

You can configure external business or IT systems to send business events to Dynatrace via API. Additionally, you can query data using DQL via API.

* Business Observability offers the **Business events API** to ingest JSON-format data into Dynatrace via the [`/bizevents/ingest` endpoint](#ingest-endpoint).
* The **Grail - DQL Query API** enables you to access records stored in Grail by making [DQL queries via API](#dql-via-api).

## Business events API: `/bizevents/ingest` endpoint

Business Observability offers the Business events API to ingest JSON data into Dynatrace via the POST method of the `/bizevents/ingest` endpoint.

To try out this API in the API Explorer

1. From the [user menu](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the latest Dynatrace") (previous Dynatrace), select **Environment API v2**.
2. Expand **Business events**, then **/bizevents/ingest**.

* **Endpoint URL**â`https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest`
* **Method**âPOST
* **Authentication**â[Access token](#access-token) or [OAuth](#oauth)
* **`Content-Type`** headerâvaries based on the [payload format](#payload-formats).

  + [Pure JSON](#pure-json): `application/json`
  + [CloudEvents](#cloudevents): `application/cloudevent+json` and `application/cloudevents+json`
  + [CloudEvents batch](#cloudevents-batch): `application/cloudevents-batch+json` and `application/cloudevents-batch+json`
* **Request body**â`{your event}`âsee the examples below.

Note that when ingesting business events, Dynatrace stores ingested top-level fields as top-level fields in Grail but converts complex JSON objects into stringsâsee the `customer` field in the [example Grail event](#grail-event) below.

If you are working in the latest Dynatrace, you can access this endpoint via `https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/bizevents/ingest`. This URL only supports [OAuth](#oauth) authentication.

### Supported request formats and examples

In addition to [pure JSON](#pure-json), Dynatrace offers the [CloudEvents](#cloudevents) and [CloudEvents batch](#cloudevents-batch) payload formats, specified in the `Content-Type` request header.

All three formats support the same request payloads. The Business events API limits payload size to 5 MB per request.

#### Pure JSON

There are no mandatory fields.

Example payload in pure JSON for ingesting a single event

```
{



"id":"2",



"paymentType":"paypal",



"plannedDeliveryDate":"01.01.2024",



"event.type":"com.bizevent.single",



"event.provider":"custom.provider",



"total":234,



"customer":{



"firstName":"John",



"lastName":"Doe"



},



"orderItemsProductIDs":[



"PR-102002002",



"QZ-123232"



]



}
```

How Grail stores the single event

Every top-level attribute is stored as a top-level field in Grail; nested JSON objects are stored as strings.

```
{



"timestamp":"2023-08-10T10:06:21.697000000+02:00",



"customer":"{\"firstName\":\"John\",\"lastName\":\"Doe\"}",



"event.id":"6f7c0c12-8386-4015-bcb2-296ba73ebd54",



"event.kind":"BIZ_EVENT",



"event.provider":"custom.provider",



"event.type":"com.bizevent.single",



"id":"2",



"orderItemsProductIDs":"[\"PR-102002002\",\"QZ-123232\"]",



"paymentType":"paypal",



"plannedDeliveryDate":"01.01.2024",



"total":234



}
```

Example payload in pure JSON for ingesting multiple events

```
[



{



"id":"1",



"paymentType":"paypal",



"plannedDeliveryDate":"01.01.2021",



"event.provider":"custom.provider.array",



"total":234,



"customer":{



"firstName":"John",



"lastName":"Doe"



},



"orderItemsProductIDs":[



"PR-102002002",



"QZ-123232"



]



},



{



"id":"1",



"paymentType":"paypal",



"plannedDeliveryDate":"01.01.2021",



"event.provider":"custom.provider.array",



"total":234,



"customer":{



"firstName":"John",



"lastName":"Doe"



},



"orderItemsProductIDs":[



"PR-102002002",



"QZ-123232"



]



}



]
```

#### CloudEvents

In the [CloudEvents standardï»¿](https://dt-url.net/gi02yvo), the required fields below can be enriched by additional data fields.

* `specversion`
* `source`âAutomatically converted to `event.provider`
* `type`âAutomatically converted to `event.type`
* `id`âAutomatically converted to `event.id`

Provide additional data in the `data` object fields. In the example below, the additional data is `paymentId`, `orderId`, and `person`.

Example CloudEvents payload

```
{



"specversion": "1.0",



"id": "8d8c6e5d-829d-4629-86fb-23cda5496fa9",



"source": "ba.dt.local",



"type": "com.dynatrace.business",



"time": "2023-08-07T07:07:13.532Z",



"data": {



"paymentId": "110",



"orderId": "5117",



"person": {



"firstName": "Max",



"lastName": "Meyer"



}



}



}
```

#### CloudEvents batch

The CloudEvents batch mode enables the ingestion of multiple events at a time. As in the previous example, required fields can be enriched by additional data fields, such as `paymentId` and `orderId`.

Example CloudEvents batch payload

```
[



{



"specversion": "1.0",



"id": "8d8c6e5d-829d-4629-86fb-23cda5496fa9",



"source": "ba.dt.local",



"type": "com.dynatrace.business",



"time": "2023-08-07T07:07:13.532Z",



"data": {



"paymentId": "110",



"orderId": "5717"



}



},



{



"specversion": "1.0",



"id": "37d9df29-ba57-4526-8ac7-6baa6ccbc9c4",



"source": "ba.dt.local",



"type": "com.dynatrace.business",



"time": "2023-08-07T07:07:14.532Z",



"data": {



"paymentId": "111",



"orderId": "5718"



}



}



]
```

### Business event enrichment

When you report business events, Dynatrace enriches them by adding more context. For example, Dynatrace adds information about your application, geolocation, device, and more. This pertains only to data ingested via the Business events API.

For details, see [Business event enrichment](/docs/observe/business-observability/bo-events-enrichment "Check what properties Dynatrace automatically adds to reported business events.").

### Practice using the Business events API endpoint

If you have a Dynatrace SaaS environment, import our **Hands-on Business Observability** notebook to step through the process of ingesting business events using the API endpoint. The Notebook guides you through configuring and testing the API using a public data source.

1. Copy and save the JSON file for the notebook.

   Getting started with Business Observability - External data sources JSON file

   ```
   {



   "version": "5",



   "defaultTimeframe": {



   "from": "now-2h",



   "to": "now"



   },



   "sections": [



   {



   "id": "4becc036-acd5-4985-ae63-e6cad53f2000",



   "type": "markdown",



   "markdown": "# Hands on Business Observability\n\n### What you will learn\n- [x] How to ingest \"[business events](https://www.dynatrace.com/support/help/platform-modules/business-observability/bo-api-ingest)\" (a.k.a generic data) into Dynatrace without OneAgent\n- [x] What are the prerequisites\n- [x] Importance of `event.provider` and `event.type` attributes\n- [x] Automating the ingest via AutomationEngine\n- [x] Enriching the data\n- [x] Analytics, Dashboards, and more\n\nReference:\n- Online documentation: [Business Observability](https://www.dynatrace.com/support/help/platform-modules/business-observability)\n- [Basic concepts of Dynatrace Business Observability](https://www.dynatrace.com/support/help/shortlink/bo-basic-concepts)"



   },



   {



   "id": "d7488bcb-d354-46b0-b2b7-53f35ec4753d",



   "type": "markdown",



   "markdown": "## What you need to know first...\n\n### Business event\n\nAn event is an action or occurrence that takes place within a system or a \"service\". The system ***produces a signal*** when an event occurs. An event becomes a business event when it generates business-grade data.\n\n### Business events can come from many sources\n- Non-OneAgent sources, example [CloudEvents](https://cloudevents.io/)\n- OneAgent, stored in the `bizevents` Grail table as bizevents data object\n- RUM data, stored in the `bizevents` Grail table as bizevents data object\n- Generic data ingest via bizevents API endpoint, stored in the `bizevents` Grail table as bizevents data object\n- Logs, currently stored in the `logs` table, as logs data object. Enhancements coming in future to allow log data sources to be stored as bizevents data object.\n\n### Why is this important?\n\nDynatrace prioritizes business events separately from observability data to ensure business-grade data.\n\n### What is Business-grade data?\n\nPrecise data that doesn't rely on samples to report baselines, identify trends, or alert on anomalies with statistical accuracy.\n\nBusiness-grade data is often required for business decisions and reporting where ***precision is critical***.\n\nContrast this with typical IT reporting which achieves statistical accuracy through sampling and extrapolation."



   },



   {



   "id": "199c0513-b8b8-4305-9231-a6fb49e70d75",



   "type": "markdown",



   "markdown": "## Listen and watch\n--- \n##### Prerequisites\n- OAuth2 bearer token for API access\n- [JSON format in request body](https://www.dynatrace.com/support/help/shortlink/bo-api-ingest#request-body) for BizEvents API endpoint\n\n##### Note\nOAuth2 will be key to accessing more and more critical aspects of the new platform. It is important for you to know how to do this.\n\nHowever, this is somewhat like a \"do once and forget\" task, so it is not often executed and thus many will lack practice.\n\nDo practice and exchange tips with your peers.\n\n##### Resources\nWhat is OAuth?\n- [Wikipeidea](https://en.wikipedia.org/wiki/OAuth)\n- [Youtube](https://www.youtube.com/watch?v=LD3NCUP5hW4)\n\nHow is it set in Dynatrace?\n- [Online docs](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/account-api-authentication)\n\n##### Demo\n- Creating OAuth2 bearer token\n- Take note of the unique properties of a bearer token\n- Building the API query and using the bearer token\n- Example of data ingest via your favourite API tool"



   },



   {



   "id": "b8ca400b-f7a0-4b1c-8b0a-b0489cc3d732",



   "type": "markdown",



   "markdown": "## Follow and do\n\nOverview of the tasks\n1. Automate\n1. Build query\n1. Enriching the data\n1. Build dashboards etc."



   },



   {



   "id": "92d1de22-7f09-4385-88cf-dab3aac40ffd",



   "type": "markdown",



   "markdown": "### Step 1: Automate \n--- \n\n- Create a workflow to ingest data from a public API source\n  - Use on-demand trigger\n- Create a task to get the bearer token\n  - Copy the payload from the example workflow or from here\n  ```\n  grant_type=client_credentials&client_id=[CLIENTID goes here]client_secret=[CLIENTSECRET goes here]\n  ```\n  - Replace the strings in square brackets with your own `clientid` and `clientsecret`\n- Create a task to get the data from a public API\n  - Use `Http request`\n  - Enter the external API URL in the `URL field`\n- Create a task to insert the data via the `bizevents` Dynatrace API\n  - Use `Http request`\n  - payload\n    - enter `{{result(\"name_of_task\").json.<replace with the data structure of your JSON results> }}`\n  - ensure you set the headers\n    - Content-Type\n      - Pure JSON: no mandatory fields. Content-Type `application/json`\n      - CloudEvent: Mandatory fields are Specversion, Source, Type, Id. Content-Type `application/cloudevent+json`\n      - CloudEvent batch (batch ingest of events): Mandatory fields as above. Content-Type `cloudevent-batch+json`\n    - Authorization\n      - `Bearer {{ result(\"get_bearer_token\").json.access_token }}`\n\n##### Discussion points\n- Use `Run Javascript task` if need to do advanced \"computation\" or \"logic\" with the data. (Industry term - \"transform the data\".)\n- [Jinja templating engine](https://www.dynatrace.com/support/help/platform-modules/cloud-automation/workflows/reference) can also be used within `Http request task` to \"transform\" the payload data"



   },



   {



   "id": "15ebff0c-6205-48e6-b1cc-faccbed6426b",



   "type": "markdown",



   "markdown": "### Step 2: Validate the data\n--- \n\nLet's start by validating what data we have first.\n\n##### Discussion points\n- What do you notice when you query the data? Is it easy to find out which dataset is yours?\n- What if you would like to define how your data will be processed further?"



   },



   {



   "id": "0786560c-8c2d-4583-9550-31309840fe9a",



   "type": "dql",



   "showTitle": false,



   "state": {



   "input": {



   "value": "fetch bizevents",



   "timeframe": {



   "from": "now-2h",



   "to": "now"



   }



   },



   "state": "idle",



   "visualizationSettings": {



   "chartSettings": {



   "gapPolicy": "connect",



   "circleChartSettings": {



   "groupingThresholdType": "absolute"



   }



   },



   "singleValue": {



   "showLabel": true,



   "label": "",



   "autoscale": true



   },



   "table": {



   "rowDensity": "condensed",



   "enableSparklines": false,



   "hiddenColumns": [],



   "lineWrapIds": [],



   "firstVisibleRowIndex": 0,



   "columnWidths": {}



   }



   }



   },



   "davisAnalytics": {



   "analyzerComponentState": {



   "resultState": {}



   }



   }



   },



   {



   "id": "85b10d2c-b709-4b34-8e71-d03b0c896738",



   "type": "markdown",



   "markdown": "### Step 3: Enriching the data\n---\n\n- [Predefined attributes](https://www.dynatrace.com/support/help/shortlink/ba-business-events-enrichment) automated if using OneAgent and RUM, further enrichment can be done\n- If using API, some important attributes require configuration\n- This is done via [Business events processing](https://www.dynatrace.com/support/help/shortlink/ba-business-events-processing)\n\nWe will enrich the incoming data set with the following 2 attributes\n- `event.provider`\n- `event.type`\n\n###### 3.1\nGo to Settings > Business Analytics > Ingest Pipeline > Processing\n\n###### 3.2\nGive the rule a name and add matcher\n\n###### 3.3\nAdd the necessary DQL under `Processor definition`.\n\n###### 3.4\nTest the rule and remember to Save\n\n###### 3.5\n- Trigger the workflow and query Dynatrace again, now with the `event.provider` attribute as a filter.\n- What do you notice now after you query for the data?"



   },



   {



   "id": "1416beec-b33f-4e5c-a054-6cb40897c7a0",



   "type": "markdown",



   "markdown": "### Step 4: Build dashboards etc.\n---\n\nNow that we have organized the data, let's see... what should we do with the data?\n\nEven if we would like to build dashboards, we need an objective, won't we?\n\nFor a start let's answer this question: ***\"Which are the most popular rental spots in the city?\"***\n\nBuild a dashboard that can visualize this data. Use category chats and switch it to horizontal. Play around with the visualization!\n\n##### Discussion points\n- From here, let's see what else can we do with the data..."



   },



   {



   "id": "1db4f97e-4ed9-4bf4-8215-885ccef7bef6",



   "type": "dql",



   "showTitle": false,



   "state": {



   "input": {



   "value": "fetch bizevents\n| summarize popular = count(), by: {RENT_NM}\n| filter popular < 1000\n| sort popular desc\n| limit 20",



   "timeframe": {



   "from": "now-2h",



   "to": "now"



   }



   },



   "state": "idle",



   "visualizationSettings": {



   "chartSettings": {



   "gapPolicy": "connect",



   "circleChartSettings": {



   "groupingThresholdType": "absolute"



   }



   },



   "singleValue": {



   "showLabel": true,



   "label": "",



   "autoscale": true



   },



   "table": {



   "rowDensity": "condensed",



   "enableSparklines": false,



   "hiddenColumns": [],



   "lineWrapIds": [],



   "firstVisibleRowIndex": 0,



   "columnWidths": {}



   }



   }



   },



   "davisAnalytics": {



   "analyzerComponentState": {



   "resultState": {}



   }



   }



   }



   ]



   }
   ```
2. In Dynatrace, go to **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
3. Expand ![Open Dashboards panel](https://dt-cdn.net/images/dashboards-app-dashboards-panel-open-6c03b43117.svg "Open Dashboards panel") the sidebar.
4. Select **Upload** to import the notebook.
5. Follow the tutorial instructions in the notebook.



## DQL queries via API

The Dynatrace Grail - DQL Query API enables third-party applications to retrieve data from Grail by executing DQL queries via API. You can only query data, not ingest it via this API.

To view Swagger documentation and try out this API in the latest Dynatrace

1. Search for "API" or "Dynatrace API."
2. From the dropdown list in the top-right corner of the page, select **Grail - DQL Query**.
3. Expand **Query Execution** to view its methods.

To run a query and to retrieve its result, you need to make two requests via separate methods.

1. To query Grail, execute the [POST `/query:execute`](#query-execute) request.
2. To retrieve the result, execute the [GET `/query:poll`](#query-poll) request.

### POST /query:execute method

* Endpoint URLâ`https://{your-environment-id}.apps.dynatrace.com/platform/storage/query/v1/query:execute`
* MethodâPOST
* Authenticationâ[OAuth](#oauth)
* `Content-Type` headerâ`application/json`
* Request bodyâ`{your DQL query}`

#### Request body example

```
{



"query": "fetch bizevents | summarize Count()"



}
```

#### Response body example

You will need to use the `requestToken` value from this response in the [`/query:poll`](#query-poll) request.

```
{



"state": "SUCCEEDED",



"requestToken": " +kuSj8qvRvq64GkG5CEHag==",



"progress": 100



}
```

### GET /query:poll method

* Endpoint URLâ`https://{your-environment-id}.apps.dynatrace.com/platform/storage/query/v1/query:poll`
* MethodâGET
* Authenticationâ[OAuth](#oauth)
* `Content-Type` headerâ`application/json` (Pure JSON)
* GET parameterâ`request-token`, used to identify the executed POST query

#### Request URL example

```
https://mySampleEnv.apps.dynatrace.com/platform/storage/query/v1/query:poll?request-token=%2BkuSj8qvRvq64GkG5CEHag%3D%3D
```

#### Response body example

```
{



"state": "SUCCEEDED",



"progress": 100,



"result": {



"records": [



{



"count()": "0"



}



],



"types": [



{



"indexRange": [



0,



0



],



"mappings": {



"count()": {



"type": "long"



}



}



}



],



"metadata": {



"grail": {



"canonicalQuery": "fetch bizevents\n| summarize count()",



"timezone": "Z",



"query": "fetch bizevents | summarize Count()",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"analysisTimeframe": {



"start": "2023-07-11T07:28:11.068767000Z",



"end": "2023-07-11T09:28:11.068767000Z"



},



"locale": "",



"executionTimeMilliseconds": 4155,



"notifications": [],



"queryId": "fa4b928f-caaf-46fa-bae0-6906e421076a",



"sampled": false



}



}



}



}
```

## Authentication

* The Business events API uses [access-token authentication](#access-token) for its `bizevents/ingest` endpoint URL in the previous Dynatrace (`https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest`).

  If you are working in the latest Dynatrace, you can access this endpoint via `https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/bizevents/ingest`. This URL only supports [OAuth](#oauth) for API access.
* The Grail - DQL Query API uses [OAuth](#oauth) for API access.

### Access token

To create a new access token for the `/bizevents/ingest` endpoint of the Business events API, follow the procedure described in [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

You need to select the **Ingest bizevents** token scope.

To authenticate a call, attach the token to the `Authorization` HTTP header preceding the `Api-Token` realm.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

### Set up and use OAuth for API access



For both the Business events API and the Grail - DQL Query API, you first need a valid bearer token for authentication, which you request by setting up OAuth for API access.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an OAuth client**](/docs/observe/business-observability/bo-api-ingest#oauth-client "Set up authentication for and ingest business events via API.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create an IAM policy**](/docs/observe/business-observability/bo-api-ingest#iam-policy "Set up authentication for and ingest business events via API.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Bind the policy to a group**](/docs/observe/business-observability/bo-api-ingest#bind-policy "Set up authentication for and ingest business events via API.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Obtain a bearer token**](/docs/observe/business-observability/bo-api-ingest#obtain-token "Set up authentication for and ingest business events via API.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Authenticate**](/docs/observe/business-observability/bo-api-ingest#authenticate "Set up authentication for and ingest business events via API.")

#### Step 1 Create an OAuth client

You can create new OAuth clients on the **Account Management** page in Dynatrace.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. From the top menu bar, select **Identity & access management** > **OAuth clients**.
3. Select **Create client**.
4. Provide the email address of the user who will own the client.
5. Provide a description for the new client.
6. Ensure that your client has the required permissions by selecting one or more options during client setup. For reading and writing business events, you require:

   * Read business events: (`storage:bizevents:read`)
   * Read Grail buckets: (`storage:buckets:read`)
   * Write/edit events: (`storage:events:write`) (only necessary for ingesting data via the [Business events API](#ingest-endpoint))
7. Select **Create client**.
8. Save the generated client secret to a password manager for future use. You will also require the generated client ID when [obtaining a bearer token](#obtain-token).

   The client secret is only displayed once upon creation, after which it's stored encrypted and can't be revealed.

#### Step 2 Create an IAM policy

To use the OAuth client, you need to ensure that the right IAM policy is assigned to your user.

To set up the policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. From the top menu bar, select **Identity & access management** > **Policy management**.
3. Select **Create policy** and set up the policy name and description. You'll need this information when you [bind this policy to a user group](#bind-policy) later. Read more about policy management in [Manage IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").
4. Add the following policy statements for writing and querying business events.

   ```
   ALLOW storage:buckets:read WHERE storage:table-name = "bizevents";



   ALLOW storage:bizevents:read;



   ALLOW storage:events:write;
   ```
5. Select **Create policy**.

#### Step 3 Bind the policy to a group

You can assign the [policy you created](#iam-policy) to a group that your user belongs to or add your user to a new group. See [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies#add-or-remove "Working with policies") for instructions on binding policies to groups.

#### Step 4 Obtain a bearer token

You can use the [OAuth client](#oauth-client) to obtain an OAuth 2.0 bearer token. Use the information below send a request to the bearer token URL. Use the token you receive in the response to [authenticate](#authenticate) to the [Business events API](#ingest-endpoint) or the [Grail - DQL Query API](#dql-via-api).

* Endpoint URL for requesting a tokenâ`https://sso.dynatrace.com/sso/oauth2/token`
* MethodâPOST
* `Content-Type` headerâ`application/x-www-form-urlencoded`
* Keys/parametersâYou can send the following keys or parameters in the request body. Make sure to URL encode all values.

  Key/Parameter

  Value

  Required

  `grant_type`

  `client_credentials`

  Required

  `client_id`

  `dt0s02.****`âThis is the client ID generated when you created an [OAuth client](#oauth-client).

  Required

  `client_secret`

  `dt0s02.***.****`âThis is the client secret generated when you created an [OAuth client](#oauth-client).

  Required

  `scope`

  A list of required scopes separated by a space, for example, `storage:bizevents:read storage:buckets:read storage:events:write`

  You can assign multiple scopes to a single token, or you can generate several tokens, each with different access levels and use them accordinglyâcheck your organization's security policies for the best practice.

  Required

  `resource`

  `urn:dtaccount:{your-account-UUID}`

  Optional if not defined in the client

  Required if defined in the client, with the same value as in the client

Example API request

Request headers

```
POST /sso/oauth2/token HTTP/2



Host: sso.dynatrace.com



content-type: application/x-www-form-urlencoded
```

Request body

```
grant_type=client_credentials&client_id=dt0s02.****&client_secret=dt0s02.***.****&scope=storage%3Abizevents%3Aread+storage%3Aevents%3Awrite+storage%3Abuckets%3Aread
```

Example API response

```
{



"scope": "storage:bizevents:read storage:events:write storage:buckets:read",



"token_type":"Bearer",



"expires_in":300,



"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjEifQ.eyJzdWIiOiI2YWUwMmFmNC01NmIwLTRhM2MtODI0OS1mYjc2ZDgyOTYwYTQiLCJyZXMiOiJ1cm46ZHRhY2NvdW50OjJiMjM2NDM4LTJhMzEtNDg3Mi04NjU1LWJjYTRmYThhZjkxNyIsIl9jbGFpbV9uYW1lcyI6eyJncm91cHMiOiIwIn0sInByZWZlcnJlZF91c2VybmFtZSI6ImRhbmllbC5tYXJzY2huaWdAZHluYXRyYWNlLmNvbSIsImd0IjoiY2MiLCJpbnQiOnRydWUsImF1ZCI6ImR0MHMwMi4zWkJZWkhWVCIsInNjb3BlIjoiYWNjb3VudC1pZG0tcmVhZCBhY2NvdW50LWlkbS13cml0ZSBhY2NvdW50LWVudi1yZWFkIGFjY291bnQtZW52LXdyaXRlIGFjY291bnQtdWFjLXJlYWQgYWNjb3VudC11YWMtd3JpdGUgaWFtLXBvbGljaWVzLW1hbmFnZW1lbnQgaWFtOnBvbGljaWVzOndyaXRlIGlhbTpwb2xpY2llczpyZWFkIGlhbTpiaW5kaW5nczp3cml0ZSBpYW06YmluZGluZ3M6cmVhZCBpYW06ZWZmZWN0aXZlLXBlcm1pc3Npb25zOnJlYWQgc3RvcmFnZTpiaXpldmVudHM6cmVhZCBzdG9yYWdlOmV2ZW50czp3cml0ZSIsIl9jbGFpbV9zb3VyY2VzIjp7IjAiOnsiZW5kcG9pbnQiOm51bGx9fSwiZXhwIjoxNjkxNjE1NTcxLCJpYXQiOjE2OTE2MTUyNzEsImp0aSI6ImJmNDZhNmFhLTRjZmItNDA1MS05ZmUzLTMzZTljMjc0OTdhZSIsImVtYWlsIjoiZGFuaWVsLm1hcnNjaG5pZ0BkeW5hdHJhY2UuY29tIn0.x3_dUuOmdqcrrsfuRyiUwKOOFSJ30fAQnpKGbJTNGy8N3qspKDO0OC36Z0GILc275bTsLY3fARzRQNBOW1Okmg",



"resource":"urn:dtaccount:2b236438-2a31-4872-8655-bca4fa8af917"



}
```

#### Step 5 Authenticate

To authenticate a call, attach the token to the `Authorization` HTTP header preceding the `Bearer` realm.

```
--header 'Authorization: Bearer abcdefjhij1234567890'
```